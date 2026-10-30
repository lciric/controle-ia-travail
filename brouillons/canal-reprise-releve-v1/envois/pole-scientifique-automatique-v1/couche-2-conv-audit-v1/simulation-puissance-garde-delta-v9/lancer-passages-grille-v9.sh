#!/bin/sh
# v9, GD8-01 : prolongement de la grille de la table de lecture. Lancé depuis le dossier v9.
# Script exécuté : le script v8 SCELLÉ, inchangé (sha256 4c7c93a9…), lu dans le dossier v8 (lecture seule) : les cellules
# prolongées sont ainsi produites par le même code que les cellules de la v8 (mêmes options, mêmes étiquettes de graine).
# Les options nouvelles de la v9 (GD8-07, GD8-08) sont dans simulation-puissance-garde-delta-v9.py et désactivées par défaut ;
# l'identité v8 = v9 hors de ces options est vérifiée à part (verif-identite-v8-v9).
#   sh lancer-passages-grille-v9.sh voie1|voie2|voie3
# Le commit est lu par l'appelant (`git rev-parse HEAD`, lecture seule, GD8-09) et passé en argument COMMIT.
set -u
V8=../simulation-puissance-garde-delta-v8/simulation-puissance-garde-delta-v8.py
S=simulation-puissance-garde-delta-v9
PY="python3 -I -B $V8"
LIM="timeout 2400"
COMMIT="${COMMIT:?COMMIT absent : le lire par git rev-parse HEAD avant le lancement}"
COMMUN="--repetitions 2000 --taux 0.01 --deltas 0.05 --biais 0,0.0125 --lecture-ebh A --m 8,2 --sans-n80 --commit-declare"
TAILLES4="--tailles 288,400,500,650"
N80="--n80-fiche --cibles-n80 0.8,0.9"
COMB="--echelle-dispersion beta --combiner-dispersion-a-et-comparateurs"
passage() {  # passage NOM OPTIONS...
  nom=$1; shift
  echo "$(date -u +%FT%TZ) début $nom"
  $LIM $PY $COMMUN "$COMMIT" "$@" --sortie $S-sortie-$nom.json
  echo "$(date -u +%FT%TZ) $nom : code $?"
}
ab() { echo "$COMB --effet-unite-beta $1 --rho-comparateurs $2"; }
R1="--comparateurs 8 --K 10,5 --K-s 10 $TAILLES4 $N80"
case "$1" in
voie1)
  passage meme-rho0.20 $R1 $(ab 0.20 0.20)
  passage double-rhoB0.17 $R1 $(ab 0.34 0.17)
  passage meme-rho0.35 $R1 $(ab 0.35 0.35)
  ;;
voie2)
  passage meme-rho0.125 $R1 $(ab 0.125 0.125)
  passage double-rhoB0.10 $R1 $(ab 0.20 0.10)
  passage double-rhoB0.125 $R1 $(ab 0.25 0.125)
  passage meme-rho0.30 $R1 $(ab 0.30 0.30)
  ;;
voie3)  # facultatif, si le temps le permet : ρ_A = 2 ρ_B à ρ_B = 0,20 (ρ_A = 0,40)
  passage double-rhoB0.20 $R1 $(ab 0.40 0.20)
  ;;
*) echo "usage : sh lancer-passages-grille-v9.sh voie1|voie2|voie3"; exit 2;;
esac
