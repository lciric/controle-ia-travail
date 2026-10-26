#!/usr/bin/env bash
# verser_dossier_v2.sh DOSSIER RUN BRANCHE MESSAGE : vérifie le run, cherche les clés, empreinte et pousse un dossier du
# collisionneur sur une branche orpheline neuve. v2 : la v1 (outils/session-depot-bloc-notes-v1, 736fa8b) avec le
# bloc-notes, l'interpréteur (venv du second pilote) et la session de cette instance ; __pycache__ retiré avant l'empreinte.
set -euo pipefail
S=/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad
PY=/opt/essaim-m3-venv-pilote2-v1/bin/python
d=$1; run=$2; br=$3; msg=$4; nom=$(basename "$d"); nom=${nom%-v1}
cd "$d"
[ -f LISEZMOI-v1.md ] || { echo "LISEZMOI-v1.md manquant" >&2; exit 3; }
git -C /home/user/controle-ia-travail ls-remote --exit-code origin "refs/heads/$br" >/dev/null 2>&1 && { echo "$br existe déjà (R12)" >&2; exit 3; }
find . -name __pycache__ -type d -prune -exec rm -rf {} +
$PY -I -B collisionneur_v2.py verifier "$run" | tail -1
/opt/essaim-m3-venv-pilote2-v1/bin/pip freeze > pip-freeze-collisionneur.txt
python3 -I -B $S/scripts/cherche_cles_v1.py "$d"
find . -type f ! -name 'EMPREINTES-v1.txt*' -printf '%P\n' | LC_ALL=C sort | xargs sha256sum > EMPREINTES-v1.txt
sha256sum EMPREINTES-v1.txt > EMPREINTES-v1.txt.sha256
w=$S/verse-$nom; [ ! -e "$w" ] || { echo "$w existe déjà" >&2; exit 3; }
git -C /home/user/controle-ia-travail worktree add -q --detach "$w"
cd "$w"; git checkout -q --orphan "$br"; git rm -rq --cached . ; find . -mindepth 1 -maxdepth 1 ! -name .git -exec rm -rf {} +
mkdir "$nom"; cp -a "$d"/. "$nom"/
python3 -I -B $S/scripts/cherche_cles_v1.py "$w/$nom"
git add "$nom"; git commit -qm "$msg

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01VJdZpSMxSdk2SJ1ScmdfNv"
git push -q -u origin "$br" 2>&1 | grep -v '^remote:' || true
git -C /home/user/controle-ia-travail ls-remote origin "refs/heads/$br"; cut -c1-16 "$nom/EMPREINTES-v1.txt.sha256"
