#!/bin/sh
# Compléments de la v8 : incertitude de graine de n80 (GD2-07, mesurée et non plus seulement citée). Même script scellé, mêmes options que les passages
# `meme-rho0.05` et `meme-rho0.17`, restreintes à K_h = 5, biais δ/4 (ligne la plus exigeante) et 288 unités, avec trois graines maîtresses autres que 20261029.
# Les sorties portent le préfixe « complement- » (elles ne sont pas lues par les tableaux principaux).
#   sh lancer-complements-v8.sh voieA | voieB       À lancer depuis le dossier du script. GD7-09 : aucune commande git.
set -u
S=simulation-puissance-garde-delta-v8
PY="python3 -I -B $S.py"
LIM="timeout 1500"
COMMIT="non lu : aucune commande git permise à la lignée conv-audit pour cette tâche, dépôt non interrogé (GD7-09)"
COMMUN="--repetitions 2000 --taux 0.01 --deltas 0.05 --biais 0.0125 --lecture-ebh A --m 8,2 --sans-n80 --commit-declare"
COMB="--echelle-dispersion beta --combiner-dispersion-a-et-comparateurs"
passage() {
  nom=$1; shift
  $LIM $PY $COMMUN "$COMMIT" "$@" --sortie $S-complement-$nom.json
  echo "$nom : code $?"
}
un() {  # un GRAINE RHO
  passage graine$1-meme-rho$2 --graine $1 --comparateurs 8 --K 5 --K-s 10 --tailles 288 --n80-fiche --cibles-n80 0.8,0.9 $COMB --effet-unite-beta $2 --rho-comparateurs $2
}
case "$1" in
voieA) un 1 0.17; un 2 0.17; un 3 0.17 ;;
voieB) un 1 0.05; un 2 0.05; un 3 0.05 ;;
*) echo "voie inconnue"; exit 2 ;;
esac
