#!/bin/bash
# Rejoue les calculs et les épreuves du dossier v4 dans un dossier NEUF et compare aux sorties versées.
# Depuis le commit : la racine est trouvée au-dessus de ce dossier (docs/sha256sums-lancement-v2.txt), puis exportée
# dans DEPOT_CONTROLE_IA pour les copies hors du dépôt (cale des relecteurs). Depuis un bloc-notes : la donner
# (DEPOT_CONTROLE_IA=/racine bash rejouer_v4.sh DOSSIER_NEUF [--long]). Aucun chemin deviné : sans racine, refus.
# --long : test de mort par programme v3 (≈ 3 min) et bases sur la case de la v3 (≈ 25 min).
# v4 : aucune comparaison ne dépend de l'emplacement des pièces ; chaque étape dit « tenu » ou s'arrête (set -e).
set -euo pipefail
ICI=$(cd "$(dirname "$0")" && pwd)
OUT=${1:?usage : rejouer_v4.sh DOSSIER_NEUF [--long]}
LONG=${2:-}
d="$ICI"; while [ "$d" != "/" ] && [ ! -f "$d/docs/sha256sums-lancement-v2.txt" ]; do d=$(dirname "$d"); done
if [ -f "$d/docs/sha256sums-lancement-v2.txt" ]; then RAC="$d"; else RAC="${DEPOT_CONTROLE_IA:-}"; fi
[ -n "$RAC" ] && [ -f "$RAC/docs/sha256sums-lancement-v2.txt" ] || { echo "racine du dépôt introuvable : donner DEPOT_CONTROLE_IA" >&2; exit 3; }
export DEPOT_CONTROLE_IA="$RAC"
PY=${PY:-$([ -x "$RAC/.venv/bin/python" ] && echo "$RAC/.venv/bin/python" || echo python3)}
mkdir "$OUT"; OUT=$(cd "$OUT" && pwd)
cd "$ICI"
echo "== compagnons"; for f in *.sha256; do sha256sum -c --quiet "$f"; done; echo "tenu"
echo "== devis v4 et contrôle des nombres (octet)"
$PY -I -B calcul_devis_essaim_v4.py "$OUT/calcul-devis-essaim-v4.json" > /dev/null; cmp "$OUT/calcul-devis-essaim-v4.json" calcul-devis-essaim-v4.json
$PY -I -B epreuves_devis_v4.py "$OUT/epreuves-devis-v4.json" > /dev/null; cmp "$OUT/epreuves-devis-v4.json" epreuves-devis-v4.json; echo "tenu"
echo "== outils des relecteurs (v2 et contre-lecture de la v3) par une cale d'import (octet)"
mkdir "$OUT/cale"; cp calcul_devis_essaim_v4.py racine_depot_v1.py "$OUT/cale/"
echo 'from calcul_devis_essaim_v4 import *  # cale : les outils des relecteurs importent sous un ancien nom' > "$OUT/cale/calcul_devis_essaim_v3.py"
cp "$OUT/cale/calcul_devis_essaim_v3.py" "$OUT/cale/calcul_devis_essaim_v2.py"
NV="$RAC/docs/notes/organisme-essaim-communicant-v1"
$PY -I -B "$NV/devis-et-instruments-v2/verification-v1/outils/artefacts_relecteur_devis_v2.py" "$OUT/cale" > "$OUT/r2.txt"; cmp "$OUT/r2.txt" artefacts-relecteur-v2-sur-devis-v4.txt
$PY -I -B "$NV/devis-et-instruments-v3/contre-lecture-v1/outils/artefacts_cl_nombres_v1.py" "$OUT/cale" > "$OUT/cl.txt" 2>&1; cmp "$OUT/cl.txt" artefacts-contre-lecture-v3-sur-devis-v4.txt; echo "tenu"
echo "== vrai pire (octet)"
$PY -I -B calcul_vrai_pire_v4.py "$OUT/calcul-vrai-pire-v4.json" > /dev/null; cmp "$OUT/calcul-vrai-pire-v4.json" calcul-vrai-pire-v4.json; echo "tenu"
echo "== lanceur v2, garde v2, registre, adaptateur (hors horodatages) et pytest"
$PY -I -B epreuves_lanceur_pilote_v2.py "$OUT/epreuves-lanceur-pilote-v2.json" "$OUT/lanceur" > /dev/null
$PY -I -B comparer_hors_horodatages_v1.py "$OUT/epreuves-lanceur-pilote-v2.json" epreuves-lanceur-pilote-v2.json
(cd "$OUT" && $PY -B -m pytest -q -p no:cacheprovider "$ICI/test_lanceur_pilote_essaim_v2.py")
if [ "$LONG" = "--long" ]; then
  echo "== test de mort par programme v3 (hors horodatages)"
  $PY -I -B test_de_mort_programme_v3.py "$OUT/test-de-mort-programme-v3-sortie.json" "$OUT/tdm" > /dev/null
  $PY -I -B comparer_hors_horodatages_v1.py "$OUT/test-de-mort-programme-v3-sortie.json" test-de-mort-programme-v3-sortie.json
  echo "== bases sur la case servie, script et sortie de la v3 (hors horodatages)"
  B3="$NV/devis-et-instruments-v3"
  (cd "$B3" && $PY -I -B bases_case_servie_v1.py "$OUT/bases-case-servie-v1-sortie.json" > /dev/null)
  $PY -I -B comparer_hors_horodatages_v1.py "$OUT/bases-case-servie-v1-sortie.json" "$B3/bases-case-servie-v1-sortie.json"
fi
echo "rejeu tenu"
