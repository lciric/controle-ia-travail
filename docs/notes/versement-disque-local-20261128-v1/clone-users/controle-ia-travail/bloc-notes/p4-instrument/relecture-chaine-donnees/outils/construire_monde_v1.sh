#!/usr/bin/env bash
# Relecture « données et fuites » de la chaîne de P4-instrument, v1 : monde jouet du relecteur.
# Dépôt jetable : clone partagé du dépôt de travail (lecture seule, objets par référence), arbre réduit au code gelé
# (src, tests, scripts, .claude, dépendances) et aux invites lues par le run jouet ; aucun fichier de prereg/, donnees/,
# diag/, runs/ du dépôt de travail n'est extrait (ni P3-consignes, ni textes d'action) ; module de P4 et chaîne versés ;
# monde jouet par les outils du rédacteur (run jouet de P3 synthétique, configuration jouet, textes synthétiques des
# fenêtres, préenregistrement jouet tiré du brouillon 4). Écrit seulement sous W. Aucun réseau.
set -euo pipefail
W=/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/p4-instrument/relecture-chaine-donnees
CH=/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/p4-instrument/chaine
MOD=/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/p4-instrument/module
B4=/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/p4-instrument/P4-instrument-v1-brouillon4.md
PY=/tmp/claude-0/-home-user/5a6b9d1d-b17d-59a1-a770-8737a831fe0a/scratchpad/scellement-revalidation/venv-gpu-neuf/bin/python
export PYTHONDONTWRITEBYTECODE=1 TMPDIR=$W/tmp HOME=$W/maison GIT_CONFIG_NOSYSTEM=1
J=$W/jouet
[ -e "$J" ] && { echo "$J existe déjà (R12)"; exit 2; }
mkdir -p "$J"
cd "$J"
git clone -q --shared --no-checkout /home/user/controle-ia-travail source
cd source
git config user.email essai@invalid; git config user.name essai; git config commit.gpgsign false
BASE=$(git rev-parse HEAD); echo "base (HEAD du dépôt de travail) : $BASE"
git read-tree HEAD
git rm -r -q --cached docs brouillons diag runs donnees livrables papiers traces prereg registres
git checkout HEAD -- docs/sources/invites-2606.08892-v1
git commit -qm "relecture : arbre réduit (code gelé et invites)"
git checkout -q -f HEAD
GELES=". :(exclude)prereg :(exclude)brouillons :(exclude)registres :(exclude)docs :(exclude)diag :(exclude)runs :(exclude)donnees :(exclude)livrables :(exclude)papiers :(exclude)traces :(exclude)CLAUDE.md"
# shellcheck disable=SC2086
git diff --quiet 7a54d431d89745839220f882b41b13e8c62ecfdd HEAD -- $GELES && echo "arbre gelé du jouet = 7a54d43 : oui"
V=docs/procedures/P4-instrument-v1
mkdir -p "$V"
for n in mesures_conception_p4_v1.py instrument_p4_v1.py lecture_p4_v1.py test_instrument_p4_v1.py test_lecture_p4_v1.py test_gardes_p4_v1.py; do
    cp "$MOD/$n" "$MOD/$n.sha256" "$V/"
done
for f in "$CH"/*.sh "$CH"/*.py; do cp "$f" "$V/"; (cd "$V" && sha256sum "$(basename "$f")" > "$(basename "$f").sha256"); done
(cd "$V" && sha256sum -c --quiet ./*.sha256) && echo "module et chaîne versés : sceaux conformes"
git add "$V" && git commit -qm "relecture : C jouet (module de P4 et chaîne versés)"
C=$(git rev-parse HEAD); echo "C jouet : $C"
mkdir -p "$J/travail"
MONDE=$("$PY" -B "$CH/outils_essais_p4_v1.py" monde . "$V" "$J/travail" prereg/P4-instrument-config-v1.json)
echo "monde jouet : $MONDE"
CFG_SHA=$(printf '%s' "$MONDE" | python3 -c 'import json, sys; print(json.load(sys.stdin)["config"])')
"$PY" -B "$CH/outils_essais_p4_v1.py" fenetres donnees/synth/textes-fenetres-p3.jsonl
"$PY" -B "$CH/outils_essais_p4_v1.py" candidat "$B4" "$J/travail/candidat-essai.md" . \
    7a54d431d89745839220f882b41b13e8c62ecfdd "$CFG_SHA" 1102 > /dev/null
echo "candidat d'essai (tiré du brouillon 4) : $(sha256sum "$J/travail/candidat-essai.md" | cut -d' ' -f1)"
"$PY" -B "$CH/outils_essais_p4_v1.py" jouet "$J/travail/candidat-essai.md" prereg/P4-instrument-v1.md . "$CFG_SHA" 1102
git add -A prereg "$V" diag runs docs && git add -f donnees
git commit -qm "relecture : S jouet (texte et configuration jouets, monde jouet, textes synthétiques des fenêtres)"
S=$(git rev-parse HEAD); echo "S jouet : $S"
echo "$S" > "$J/S.txt"
git clone -q --bare . "$J/distant.git"
echo "dépôt distant local : $J/distant.git"
du -sh "$J" 2>/dev/null | cut -f1 | sed 's/^/place prise par le monde jouet : /'
find "$J" -name __pycache__ -type d | head -3 | sed 's/^/__pycache__ écrit : /'
echo "FIN DE LA CONSTRUCTION"
