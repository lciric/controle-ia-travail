#!/bin/bash
# Lance, dans l'ordre, toutes les sorties de la conception (aucun réseau, aucune clé) ; une sortie existante n'est jamais
# écrasée (chaque script refuse). Heures relevées par `date -u`. Usage : bash lancer_sorties_v1.sh DOSSIER_SORTIES
set -u
O="$1"; D="$(cd "$(dirname "$0")" && pwd)"; P="python3 -I -B"
cd "$D"
j() { echo "$(date -u +%Y-%m-%dT%H:%M:%SZ) $*" >> "$O/journal-sorties-v1.txt"; }
j "début ; python $(python3 -c 'import platform,numpy;print(platform.python_version(), numpy.__version__)')"
$P essais_monde_riche_v1.py > "$O/essais-v1.stdout" 2> "$O/essais-v1.stderr"; j "essais code $?"
$P faire_exemples_v1.py "$O" > "$O/exemples-v1.stdout" 2>&1; j "exemples code $?"
$P verifier_monde_kimi_v1.py --devis "$O/exemple-devis-synthetique-v1.json" --exigences "$O/exigences-monde-riche-v1.json" \
   --sortie "$O/rapport-verificateur-exemple-synthetique-v1.json" > "$O/verificateur-exemple-v1.stdout" 2>&1; j "vérificateur exemple code $?"
$P variantes_v67_v1.py > "$O/variantes-v67-v1.stdout" 2>&1; j "variantes v67 code $?"
$P normes_coefficients_v1.py > "$O/normes-coefficients-v1.stdout" 2>&1; j "normes code $?"
$P puissance_monde_riche_v1.py etalonnage "$O/etalonnage-r1000-v1.json" --repetitions 1000 > "$O/etalonnage-r1000-v1.stdout" 2>&1; j "étalonnage code $?"
$P puissance_monde_riche_v1.py attribution "$O/attribution-w12-v1.json" --mondes 12 > "$O/attribution-w12-v1.stdout" 2>&1; j "attribution code $?"
$P puissance_monde_riche_v1.py doublons "$O/doublons-w12-v1.json" --mondes 12 > "$O/doublons-w12-v1.stdout" 2>&1; j "doublons code $?"
$P puissance_monde_riche_v1.py detection "$O/detection-w12-r40-v1.json" --mondes 12 --repetitions 40 --tirages 200 400 800 --m 40 > "$O/detection-w12-r40-v1.stdout" 2>&1; j "détection code $?"
$P puissance_monde_riche_v1.py generations "$O/generations-w12-g3-n400-v1.json" --mondes 12 --generations 3 --tirages 400 --m 40 --eps 0.01 > "$O/generations-w12-g3-n400-v1.stdout" 2>&1; j "générations code $?"
j "fin"
