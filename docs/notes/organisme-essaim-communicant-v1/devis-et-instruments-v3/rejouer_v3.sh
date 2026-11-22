#!/bin/bash
# Rejoue les calculs et les épreuves du dossier v3 dans un dossier NEUF et compare aux sorties versées.
# Depuis le commit : la racine du dépôt est trouvée au-dessus de ce dossier (docs/sha256sums-lancement-v2.txt).
# Depuis un bloc-notes : DEPOT_CONTROLE_IA=/chemin/de/la/racine bash rejouer_v3.sh DOSSIER_NEUF [--long]
# --long ajoute les bases sur la case servie (≈ 20 min) et le test de mort par programme (≈ 3 min).
# Python : PY (défaut : .venv/bin/python de la racine si présent, sinon python3). Aucun appel, aucun réseau.
set -euo pipefail
ICI=$(cd "$(dirname "$0")" && pwd)
OUT=${1:?usage : rejouer_v3.sh DOSSIER_NEUF [--long]}
LONG=${2:-}
mkdir "$OUT"
OUT=$(cd "$OUT" && pwd)
RAC=$(cd "$ICI" && d="$ICI"; while [ "$d" != "/" ] && [ ! -f "$d/docs/sha256sums-lancement-v2.txt" ]; do d=$(dirname "$d"); done; [ -f "$d/docs/sha256sums-lancement-v2.txt" ] && echo "$d" || echo "${DEPOT_CONTROLE_IA:-}")
[ -n "$RAC" ] && [ -f "$RAC/docs/sha256sums-lancement-v2.txt" ] || { echo "racine du dépôt introuvable : donner DEPOT_CONTROLE_IA" >&2; exit 3; }
PY=${PY:-$([ -x "$RAC/.venv/bin/python" ] && echo "$RAC/.venv/bin/python" || echo python3)}
cd "$ICI"
echo "== empreintes des compagnons"; for f in *.sha256; do sha256sum -c --quiet "$f"; done; echo "conformes"
echo "== devis v3 et contrôle des nombres (octet)"
$PY -I -B calcul_devis_essaim_v3.py "$OUT/calcul-devis-essaim-v3.json" > /dev/null; cmp "$OUT/calcul-devis-essaim-v3.json" calcul-devis-essaim-v3.json
$PY -I -B epreuves_devis_v3.py "$OUT/epreuves-devis-v3.json" > /dev/null; cmp "$OUT/epreuves-devis-v3.json" epreuves-devis-v3.json
echo "== pilote v2 et coût réduit v2 (octet)"
$PY -I -B calcul_pilote_essaim_v2.py "$OUT/calcul-pilote-essaim-v2.json" > /dev/null; cmp "$OUT/calcul-pilote-essaim-v2.json" calcul-pilote-essaim-v2.json
$PY -I -B calcul_devis_cout_reduit_v2.py "$OUT/calcul-devis-cout-reduit-v2.json" > /dev/null; cmp "$OUT/calcul-devis-cout-reduit-v2.json" calcul-devis-cout-reduit-v2.json
echo "== gardes du lanceur (hors horodatages) et pytest"
$PY -I -B epreuves_gardes_pilote_v1.py "$OUT/epreuves-gardes-pilote-v1.json" "$OUT/journaux-gardes" > /dev/null
$PY -I -B comparer_hors_horodatages_v1.py "$OUT/epreuves-gardes-pilote-v1.json" epreuves-gardes-pilote-v1.json
(cd "$OUT" && $PY -B -m pytest -q -p no:cacheprovider "$ICI/test_gardes_pilote_essaim_v1.py")
if [ "$LONG" = "--long" ]; then
  echo "== test de mort par programme v2 (hors horodatages)"
  $PY -I -B test_de_mort_programme_v2.py "$OUT/test-de-mort-programme-v2-sortie.json" "$OUT/tdm-travail" > /dev/null
  $PY -I -B comparer_hors_horodatages_v1.py "$OUT/test-de-mort-programme-v2-sortie.json" test-de-mort-programme-v2-sortie.json
  echo "== bases sur la case servie (hors horodatages)"
  $PY -I -B bases_case_servie_v1.py "$OUT/bases-case-servie-v1-sortie.json" > /dev/null
  $PY -I -B comparer_hors_horodatages_v1.py "$OUT/bases-case-servie-v1-sortie.json" bases-case-servie-v1-sortie.json
fi
echo "rejeu tenu"
