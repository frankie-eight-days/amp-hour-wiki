#!/bin/zsh
# One-command site refresh: sync articles -> build -> deploy -> commit+push.
set -e
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

python3 tools/sync_site.py
cd site
npx quartz build

# quartz build wipes public/, which destroys the vercel link and config —
# restore both from the stable copies kept at site/
cp -r .vercel public/ 2>/dev/null || true
cp vercel.json public/ 2>/dev/null || true

# force LIGHT as the default theme (darkmode plugin defaults to OS preference
# with a dark fallback; we want light unless the visitor explicitly toggles).
# The theme bootstrap lives in the hashed prescript-*.js bundle.
LC_ALL=C find public -name 'prescript-*.js' -exec sed -i '' \
  's/window.matchMedia("(prefers-color-scheme: light)").matches?"light":"dark"/"light"/g' {} +
cd public
if [ ! -d .vercel ]; then
  npx vercel link --yes --project amphour-wiki --scope frankie-eight-days-projects
  cp -r .vercel ../
fi
npx vercel deploy --prod --yes --archive=tgz

cd "$ROOT"
N=$(ls articles/wiki/*.md | grep -v prompt | wc -l | tr -d ' ')
git add -A
git commit -m "sync: $N articles

Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>" || true
git push
