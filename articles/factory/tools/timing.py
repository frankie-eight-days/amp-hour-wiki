#!/usr/bin/env python3
"""Per-article timing capture for the factory run.

Extraction agents call one function:

    import sys; sys.path.insert(0, "articles/factory/tools")
    from timing import append_timing

    append_timing("altium", {
        "t_extract_s": 412.5,     # your own reading + packet assembly wall time
        "t_kimi_s": 96.2,         # printed by kimi_write.py as t_kimi_s
        "t_lint_s": 0.1,          # printed by lint.py as t_lint_s
        "passages_in": 250, "claims_kept": 88, "claims_killed": 162,
        "article_words": 3543, "revisions": 1,
    })

Every field is optional. `concept` is added for you, `ts_start` defaults to now,
`t_gather_s` defaults to 0.0 (bundles are prebuilt), and `t_total_s` is summed
from the phase timings when you do not supply it. Records append as JSON lines
to articles/factory/_timing.jsonl; writes are lock-protected so parallel agents
cannot interleave.

Partial records are fine and expected — kimi_write.py appends its own
{t_kimi_s, article_words} the moment the call returns. `summarize()` merges all
records for a concept, last non-null value winning, so the agent's later record
completes what the tools already recorded.

Shell callers can use the CLI instead:

    python3 timing.py --concept altium --t-extract-s 412.5 --claims-kept 88
    python3 timing.py --summary          # aggregate table over everything so far

`stopwatch()` is there if you want to time a block rather than compute it:

    with stopwatch() as t:
        ...
    append_timing(concept, {"t_extract_s": t.seconds})
"""
import argparse, datetime, json, os, time
from contextlib import contextmanager

ROOT = "/Users/frankwalsh/Documents/vibecoding/amp_hour_wiki"
TIMING = os.environ.get("FACTORY_TIMING",
                        os.path.join(ROOT, "articles/factory/_timing.jsonl"))

FIELDS = ("concept", "t_gather_s", "t_extract_s", "t_kimi_s", "t_lint_s",
          "t_total_s", "passages_in", "claims_kept", "claims_killed",
          "article_words", "revisions", "ts_start")
PHASES = ("t_gather_s", "t_extract_s", "t_kimi_s", "t_lint_s")


def append_timing(concept, record=None, path=TIMING, **kw):
    """Append one timing record for `concept`. Returns the record written."""
    rec = dict(record or {})
    rec.update(kw)
    rec["concept"] = concept
    rec.setdefault("ts_start", datetime.datetime.now().astimezone().isoformat())
    rec.setdefault("t_gather_s", 0.0)
    if rec.get("t_total_s") is None:
        parts = [rec.get(p) for p in PHASES if isinstance(rec.get(p), (int, float))]
        rec["t_total_s"] = round(sum(parts), 3) if parts else None
    for k in PHASES + ("t_total_s",):
        if isinstance(rec.get(k), (int, float)):
            rec[k] = round(float(rec[k]), 3)
    ordered = {k: rec[k] for k in FIELDS if k in rec}
    ordered.update({k: v for k, v in rec.items() if k not in FIELDS})

    os.makedirs(os.path.dirname(path), exist_ok=True)
    line = json.dumps(ordered) + "\n"
    with open(path, "a") as f:                 # O_APPEND: one write, no interleave
        f.write(line)
    return ordered


@contextmanager
def stopwatch():
    class T:
        seconds = None
    t = T()
    start = time.monotonic()
    try:
        yield t
    finally:
        t.seconds = round(time.monotonic() - start, 3)


def _earliest(a, b):
    try:
        return a if datetime.datetime.fromisoformat(a) <= \
            datetime.datetime.fromisoformat(b) else b
    except ValueError:
        return a


def load(path=TIMING):
    """Merge records per concept; the last non-null value for a field wins,
    except ts_start, which keeps the earliest across partial records.

    `article_words` is written by both tools: kimi_write.py counts the whole
    document, lint.py counts the body above the References table. lint runs
    last, so the body count is what survives — that is the intended number."""
    if not os.path.exists(path):
        return {}
    merged = {}
    for line in open(path):
        line = line.strip()
        if not line:
            continue
        try:
            r = json.loads(line)
        except json.JSONDecodeError:
            continue
        c = r.get("concept")
        if not c:
            continue
        cur = merged.setdefault(c, {"concept": c})
        for k, v in r.items():
            if v is None:
                continue
            if k == "ts_start" and cur.get("ts_start"):
                cur["ts_start"] = _earliest(cur["ts_start"], v)
            else:
                cur[k] = v
    for r in merged.values():
        parts = [r.get(p) for p in PHASES if isinstance(r.get(p), (int, float))]
        if parts:
            r["t_total_s"] = round(sum(parts), 3)
    return merged


def summarize(path=TIMING):
    recs = list(load(path).values())
    if not recs:
        return {"articles": 0}
    import statistics

    def stats(key):
        vals = [r[key] for r in recs if isinstance(r.get(key), (int, float))]
        if not vals:
            return None
        return {"n": len(vals), "total": round(sum(vals), 1),
                "mean": round(statistics.mean(vals), 1),
                "median": round(statistics.median(vals), 1),
                "min": round(min(vals), 1), "max": round(max(vals), 1)}

    out = {"articles": len(recs)}
    for k in PHASES + ("t_total_s", "passages_in", "claims_kept", "claims_killed",
                       "article_words", "revisions"):
        s = stats(k)
        if s:
            out[k] = s
    slow = sorted((r for r in recs if isinstance(r.get("t_total_s"), (int, float))),
                  key=lambda r: -r["t_total_s"])[:10]
    out["slowest"] = [{"concept": r["concept"], "t_total_s": r["t_total_s"]}
                      for r in slow]
    kept = sum(r.get("claims_kept", 0) or 0 for r in recs)
    killed = sum(r.get("claims_killed", 0) or 0 for r in recs)
    if kept + killed:
        out["claim_keep_rate"] = round(kept / (kept + killed), 3)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--concept")
    ap.add_argument("--path", default=TIMING)
    ap.add_argument("--summary", action="store_true")
    for f in FIELDS:
        if f in ("concept", "ts_start"):
            continue
        ap.add_argument("--" + f.replace("_", "-"),
                        type=float if f.startswith("t_") else int)
    ap.add_argument("--ts-start")
    a = ap.parse_args()
    if a.summary:
        print(json.dumps(summarize(a.path), indent=1))
        return
    if not a.concept:
        raise SystemExit("--concept required (or use --summary)")
    rec = {f: getattr(a, f) for f in FIELDS
           if f != "concept" and getattr(a, f, None) is not None}
    print(json.dumps(append_timing(a.concept, rec, path=a.path)))


if __name__ == "__main__":
    main()
