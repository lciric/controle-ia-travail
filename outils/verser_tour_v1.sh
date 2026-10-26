#!/usr/bin/env bash
# verser_tour_v1.sh NOM : vérifie, cherche les clés, empreinte et pousse un tour du collisionneur sur sa branche orpheline.
set -euo pipefail
S=/tmp/claude-0/-home-user-controle-ia-travail/325f961c-9943-5b73-9387-393664866547/scratchpad
t=$1; R=${2:-R-419}; d=$S/collisionneur-$t-v1; br=donnees/collisionneur-$t-v1
cd $d
/opt/essaim-m3-venv-v1/bin/python -I -B collisionneur_v2.py verifier run-$t-e3t1-v1
/opt/essaim-m3-venv-v1/bin/pip freeze > pip-freeze-collisionneur.txt
[ -f LISEZMOI-v1.md ] || { echo "LISEZMOI-v1.md manquant" >&2; exit 3; }
python3 -I -B $S/scripts/cherche_cles_v1.py $d
find . -type f ! -name EMPREINTES-v1.txt ! -name EMPREINTES-v1.txt.sha256 -printf '%P\n' | LC_ALL=C sort | xargs sha256sum > EMPREINTES-v1.txt
sha256sum EMPREINTES-v1.txt > EMPREINTES-v1.txt.sha256
w=$S/verse-$t; rm -rf $w; git -C /home/user/controle-ia-travail worktree add -q --detach $w
cd $w; git checkout -q --orphan $br; git rm -rq --cached . ; find . -mindepth 1 -maxdepth 1 ! -name .git -exec rm -rf {} +
mkdir collisionneur-$t; cp -a $d/. collisionneur-$t/
python3 -I -B $S/scripts/cherche_cles_v1.py $w/collisionneur-$t
git add collisionneur-$t; git commit -qm "Collisionneur v2.5, tour III.1 « $t » ($R, GO-2026-10-24-07) : sorties, empreintes

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_017hDPN1tZfNVQcefqrergK6"
git push -q -u origin $br; git log --oneline -1; cut -c1-16 collisionneur-$t/EMPREINTES-v1.txt.sha256
