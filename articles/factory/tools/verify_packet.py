#!/usr/bin/env python3
"""Check an extraction packet against the bundle it came from.

  python3 verify_packet.py <concept>

Fails on: quotes not verbatim in any bundle passage, episodes not present in the
bundle, episode title/url disagreeing with the bundle, missing required fields,
reception language in claim_text. Warns on thin packets and duplicate claims.
"""
import json, os, re, sys, collections

ROOT = "/Users/frankwalsh/Documents/vibecoding/amp_hour_wiki"
RECEPTION = re.compile(
    r"\bcame around\b|\badoption\b|\bdismissed\b|\bhosts disagreed\b|\breception\b|"
    r"\bdivided\b|\bwidely praised\b|\bcriticis|\bcriticiz|\bwas well received\b|"
    r"\bwarmly received\b|\bfan favourite\b|\bfan favorite\b|\bpodcast\b|\bthe show\b", re.I)
FIELDS = ("claim_text", "quote_verbatim", "speaker", "episode", "episode_title",
          "episode_url", "depth_regraded", "kind")

norm = lambda s: re.sub(r"[^a-z0-9 ]+", "", re.sub(r"\s+", " ", (s or "").lower())).strip()


def main(concept):
    bundle = json.load(open(f"{ROOT}/articles/factory/bundles/{concept}.json"))
    pkt = json.load(open(f"{ROOT}/articles/factory/packets/{concept}.json"))
    ps = bundle["passages"]
    eps = {p["episode"] for p in ps if p.get("episode")}
    meta = {}
    for p in ps:
        if p.get("episode"):
            meta.setdefault(p["episode"], (p.get("episode_title"), p.get("episode_url")))
    haystack = {}
    for p in ps:
        if p.get("episode"):
            haystack.setdefault(p["episode"], []).append(norm(p["text"]))
    allhay = norm(" || ".join(p["text"] for p in ps))

    fail, warn = [], []
    claims = pkt["claims"]
    for i, c in enumerate(claims):
        for f in FIELDS:
            if f not in c:
                fail.append(f"claim {i}: missing field {f}")
        e = c.get("episode")
        if e not in eps:
            fail.append(f"claim {i}: episode {e} not in bundle")
            continue
        t, u = meta[e]
        if c.get("episode_title") != t:
            fail.append(f"claim {i}: ep {e} title {c.get('episode_title')!r} != bundle {t!r}")
        if c.get("episode_url") != u:
            fail.append(f"claim {i}: ep {e} url mismatch")
        q = norm(c.get("quote_verbatim"))
        if not q:
            fail.append(f"claim {i}: empty quote_verbatim")
        elif not any(q in h for h in haystack[e]):
            where = "found in another episode" if q in allhay else "NOT FOUND anywhere"
            fail.append(f"claim {i} (ep {e}): quote not verbatim in that episode's "
                        f"passages [{where}]: {c['quote_verbatim'][:90]!r}")
        if RECEPTION.search(c.get("claim_text", "")):
            fail.append(f"claim {i}: reception/meta language: "
                        f"{RECEPTION.search(c['claim_text']).group(0)!r}")
        if c.get("depth_regraded") not in ("explains", "opinion"):
            fail.append(f"claim {i}: bad depth_regraded {c.get('depth_regraded')!r}")

    if pkt.get("concept") != concept:
        fail.append("packet concept mismatch")
    if len(claims) < 55:
        warn.append(f"thin packet: {len(claims)} claims")
    dup = [k for k, n in collections.Counter(norm(c.get("claim_text"))[:80]
                                             for c in claims).items() if n > 1]
    if dup:
        warn.append(f"{len(dup)} near-duplicate claim openings")

    out = {"concept": concept, "claims": len(claims),
           "episodes": len({c["episode"] for c in claims}),
           "bundle_episodes": len(eps),
           "kinds": dict(collections.Counter(c.get("kind") for c in claims)),
           "fail": fail[:40], "n_fail": len(fail), "warn": warn,
           "pass": not fail}
    print(json.dumps(out, indent=1))
    sys.exit(0 if not fail else 1)


if __name__ == "__main__":
    main(sys.argv[1])
