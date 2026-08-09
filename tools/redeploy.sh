#!/bin/zsh
# One-command site refresh: sync articles -> build -> deploy -> commit+push.
set -e
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

python3 tools/sync_site.py
cd site
npx quartz build

# quartz build wipes public/, which destroys the vercel link — restore it
# from the stable copy kept at site/.vercel
cp -r .vercel public/ 2>/dev/null || true
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
