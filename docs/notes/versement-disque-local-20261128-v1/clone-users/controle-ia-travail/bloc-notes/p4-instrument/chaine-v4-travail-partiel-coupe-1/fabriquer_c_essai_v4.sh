#!/usr/bin/env bash
# Outil de travail du correcteur de la chaîne v4 (non versé), décliné de …/chaine-v3-travail/fabriquer_c_essai_v3.sh :
# dépôt « C d'essai » = clone partagé du dépôt de travail (lecture seule, objets par référence), commit sans les PDF, puis
# commit des préalables d'essai : module de P4 v3 (`…/p4-instrument/module-v3/`, six fichiers et leurs sceaux) et chaîne
# v4 (`…/p4-instrument/chaine-v4/`, vingt et un scripts, scellés ici) versés sous docs/procedures/P4-instrument-v1/ ;
# candidat 2 d'essai tiré du candidat 1 par `ecrire_candidat2_v2.py` (module v3, scripts de l'instance de la chaîne v4,
# tests collectés, paires du module v3 corrigées par sa vérification (`paires-texte-module-v3-corrigees-vm3-v2.json`)
# puis paires de la chaîne v4 produites par `outils_essais_p4_v1.py paires-v4`).
# Usage : fabriquer_c_essai_v4.sh DOSSIER_NEUF
set -euo pipefail
X=$(realpath -m "$1")
P4=/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/p4-instrument
CH=$P4/chaine-v4; MOD=$P4/module-v3
PM=$P4/verification-module-v3/travail/paires-texte-module-v3-corrigees-vm3-v2.json
PY=/tmp/claude-0/-home-user/5a6b9d1d-b17d-59a1-a770-8737a831fe0a/scratchpad/scellement-revalidation/venv-gpu-neuf/bin/python
export PYTHONDONTWRITEBYTECODE=1 GIT_OPTIONAL_LOCKS=0
[ -e "$X" ] && { echo "$X existe déjà"; exit 2; }
(cd "$(dirname "$PM")" && sha256sum -c --quiet "$(basename "$PM").sha256") || { echo "paires du module v3 : sceau non conforme"; exit 2; }
mkdir -p "$X" && cd "$X"
git clone -q --shared --no-checkout /home/user/controle-ia-travail depot
cd depot
git config user.email essai@invalid; git config user.name essai; git config commit.gpgsign false
git read-tree HEAD
echo "tête du dépôt de travail : $(git rev-parse HEAD)"
git rm -r -q --cached docs/sources/pdf docs/sources/lecture-pdf-niveau1 docs/sources/lecture-pdf-niveau2
git commit -qm "essai : sans les PDF de docs/sources (place disque)"
git checkout -q -f HEAD
V=docs/procedures/P4-instrument-v1
[ ! -e "$V" ] || { echo "$V existe déjà dans le dépôt de travail"; exit 2; }
mkdir -p "$V"
for n in mesures_conception_p4_v1.py instrument_p4_v1.py lecture_p4_v1.py test_instrument_p4_v1.py test_lecture_p4_v1.py test_gardes_p4_v1.py; do
    cp "$MOD/$n" "$MOD/$n.sha256" "$V/"
    (cd "$V" && sha256sum -c --quiet "$n.sha256")
done
for f in "$CH"/*.sh "$CH"/*.py; do cp "$f" "$V/"; (cd "$V" && sha256sum "$(basename "$f")" > "$(basename "$f").sha256"); done
echo "scripts de la chaîne versés : $(ls "$CH"/*.sh "$CH"/*.py | wc -l)"
git add "$V" && git commit -qm "essai : préalables (module de P4 v3 et chaîne v4 versés)"
echo "C d'essai : $(git rev-parse HEAD)"
N=$(PYTHONPATH=src "$PY" -B -m pytest --collect-only -q -p no:cacheprovider tests "$V/test_instrument_p4_v1.py" \
    "$V/test_lecture_p4_v1.py" "$V/test_gardes_p4_v1.py" 2>/dev/null | sed -n 's/^\([0-9]*\) tests\{0,1\} collected.*/\1/p')
echo "tests collectés : $N"
mkdir -p "$X/travail"
"$PY" -B "$CH/outils_essais_p4_v1.py" paires-v4 "$X/travail/paires-chaine-v4-essai.json" > /dev/null
"$PY" -I -B -c 'import json, sys
m = json.load(open(sys.argv[1], encoding="utf-8")); c = json.load(open(sys.argv[2], encoding="utf-8"))
json.dump(m + c, open(sys.argv[3], "w", encoding="utf-8"), ensure_ascii=False, indent=1)' "$PM" "$X/travail/paires-chaine-v4-essai.json" "$X/travail/paires-module-v3-et-chaine-v4-essai.json"
"$PY" -B "$P4/ecrire_candidat2_v2.py" "$P4/P4-instrument-v1-candidat1.md" "$X/travail/P4-instrument-v1-candidat2-essai.md" \
    "$MOD" "$CH" "$N" "$X/travail/paires-module-v3-et-chaine-v4-essai.json" > /dev/null
echo "candidat 2 d'essai : $X/travail/P4-instrument-v1-candidat2-essai.md $(sha256sum "$X/travail/P4-instrument-v1-candidat2-essai.md" | cut -d' ' -f1)"
find "$X" "$CH" "$MOD" -name __pycache__ | head -3
