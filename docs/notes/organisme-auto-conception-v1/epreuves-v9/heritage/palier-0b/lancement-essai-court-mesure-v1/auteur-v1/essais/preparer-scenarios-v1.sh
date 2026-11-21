#!/bin/bash
# Fabrique, pour chaque scénario, un dossier (tenue/ vide ; sorties/ non créé) et un lanceur factice tiré du vrai lanceur
# (constantes et ligne de commande seules changées), qui lance le programme factice de la racine factice.
# Usage : preparer-scenarios-v1.sh DOSSIER_DES_ESSAIS VRAI_LANCEUR TETE_FACTICE EMPREINTE_FACTICE
set -eu
E=$1
L=$2
T=$3
H=$4
R="$E/racine-factice"
P="$R/prog/programme-factice-v1.py"
PY=/home/user/controle-ia-travail/.venv/bin/python
FAB="$E/fabriquer-lanceur-factice-v1.py"

scenario() {  # nom options-du-programme-factice...
  local nom=$1
  shift
  local D="$E/scenarios/$nom"
  mkdir -p "$D/tenue"
  "$PY" -I -B "$FAB" "$L" "$D/lanceur-factice.sh" "$R" "$T" "$H" "$P" "$D/sorties" \
    "$PY -I -B $P $D/sorties $*"
}

scenario s1-sain-place --delai-etape-3 1 --pas 0.5 --max-sources 8
scenario s2-artefact-place --delai-etape-3 1 --pas 0.5 --max-sources 8 --sans-fin
scenario s3-sain-mesure-n --delai-etape-3 1 --pas 0.5 --max-sources 12
scenario s4-artefact-mesure-n --delai-etape-3 1 --pas 0.5 --max-sources 40 --octets-par-source 100000
scenario s5-sain-mesure-duree --delai-etape-3 1 --pas 1 --max-sources 10
scenario s6-artefact-mesure-duree --delai-etape-3 1 --pas 1 --max-sources 8 --sans-fin
scenario s7-artefact-arret-force --delai-etape-3 1 --pas 0.5 --max-sources 4 --sans-fin --ignorer-terme
scenario s8-artefact-mesure-n1 --delai-etape-3 1 --pas 30 --max-sources 3 --sans-fin
echo "scénarios prêts sous $E/scenarios"
