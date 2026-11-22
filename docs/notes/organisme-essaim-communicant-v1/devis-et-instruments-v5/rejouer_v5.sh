#!/bin/bash
# Rejoue les épreuves du dossier v5 (lanceur v3, registre v2) dans un dossier NEUF et compare aux sorties versées.
# Racine trouvée au-dessus de ce dossier, sinon DEPOT_CONTROLE_IA, sinon refus ; puis exportée. Aucun appel, aucun réseau.
# Le devis, le contrôle des nombres, le vrai pire et le test de mort sont inchangés depuis la v4 : `rejouer_v4.sh` les rejoue.
set -euo pipefail
ICI=$(cd "$(dirname "$0")" && pwd)
OUT=${1:?usage : rejouer_v5.sh DOSSIER_NEUF}
d="$ICI"; while [ "$d" != "/" ] && [ ! -f "$d/docs/sha256sums-lancement-v2.txt" ]; do d=$(dirname "$d"); done
if [ -f "$d/docs/sha256sums-lancement-v2.txt" ]; then RAC="$d"; else RAC="${DEPOT_CONTROLE_IA:-}"; fi
[ -n "$RAC" ] && [ -f "$RAC/docs/sha256sums-lancement-v2.txt" ] || { echo "racine du dépôt introuvable : donner DEPOT_CONTROLE_IA" >&2; exit 3; }
export DEPOT_CONTROLE_IA="$RAC"
PY=${PY:-$([ -x "$RAC/.venv/bin/python" ] && echo "$RAC/.venv/bin/python" || echo python3)}
mkdir "$OUT"; OUT=$(cd "$OUT" && pwd)
cd "$ICI"
echo "== compagnons"; for f in *.sha256; do sha256sum -c --quiet "$f"; done; echo "tenu"
echo "== épreuves du lanceur v3 et du registre v2 (hors horodatages)"
$PY -I -B epreuves_lanceur_pilote_v3.py "$OUT/epreuves-lanceur-pilote-v3.json" "$OUT/journaux" > "$OUT/epreuves.stdout"
$PY -I -B comparer_hors_horodatages_v1.py "$OUT/epreuves-lanceur-pilote-v3.json" epreuves-lanceur-pilote-v3.json
echo "== pytest"
(cd "$OUT" && $PY -B -m pytest -q -p no:cacheprovider "$ICI/test_lanceur_pilote_essaim_v3.py")
echo "rejeu tenu"
