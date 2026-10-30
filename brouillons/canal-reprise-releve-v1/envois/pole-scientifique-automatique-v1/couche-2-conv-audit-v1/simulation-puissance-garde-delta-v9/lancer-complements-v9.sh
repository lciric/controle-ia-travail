#!/bin/sh
# v9 : compléments, lancés avec le script v9 (simulation-puissance-garde-delta-v9.py) depuis le dossier v9.
#   sh lancer-complements-v9.sh rhoh|graines|partielle
# partielle (GD8-03) : strates à portée partielle (γ_A = 0,4, γ_B = f·0,4, f = 0,5), S ∈ {2 ; 3}, brut et étalonné, ρ = 0,17, 288 et 400 unités (options R3 de la v8).
# rhoh (GD8-07) : ρ honnête = 2 × ρ saboté, pour A et les comparateurs (--facteur-rho-honnetes 2, SUPPOSÉ), options R1 de la v8 (n80 et n90 de la
#   fiche aux deux seuils, 2 000 répétitions, quatre cellules) ; à comparer aux passages v8 meme-rho0.05, meme-rho0.10, meme-rho0.17.
# graines (GD8-04) : puissances clés (ρ_A = ρ_B = 0,17 ; 288 et 400 unités ; quatre cellules K_h ∈ {10 ; 5} × biais ∈ {0 ; δ/4}) sous huit graines
#   maîtresses 11 à 18 (autres que celles de la v8 : 20261029, 1, 2, 3, et de GD8), sans n80 ; moyenne et erreur type par tableaux-v9.py.
# Le commit est lu par l'appelant (git rev-parse HEAD, lecture seule) et passé par la variable COMMIT (GD8-09).
set -u
S=simulation-puissance-garde-delta-v9
PY="python3 -I -B $S.py"
LIM="timeout 2400"
COMMIT="${COMMIT:?COMMIT absent}"
COMMUN="--repetitions 2000 --taux 0.01 --deltas 0.05 --biais 0,0.0125 --lecture-ebh A --m 8,2 --sans-n80 --commit-declare"
COMB="--echelle-dispersion beta --combiner-dispersion-a-et-comparateurs"
passage() {
  nom=$1; shift
  echo "$(date -u +%FT%TZ) début $nom"
  $LIM $PY $COMMUN "$COMMIT" "$@" --sortie $S-sortie-$nom.json
  echo "$(date -u +%FT%TZ) $nom : code $?"
}
ab() { echo "$COMB --effet-unite-beta $1 --rho-comparateurs $2"; }
R1="--comparateurs 8 --K 10,5 --K-s 10 --tailles 288,400,500,650 --n80-fiche --cibles-n80 0.8,0.9"
case "$1" in
rhoh)
  passage rhoh2x-meme-rho0.05 $R1 $(ab 0.05 0.05) --facteur-rho-honnetes 2
  passage rhoh2x-meme-rho0.10 $R1 $(ab 0.10 0.10) --facteur-rho-honnetes 2
  passage rhoh2x-meme-rho0.17 $R1 $(ab 0.17 0.17) --facteur-rho-honnetes 2
  ;;
graines)
  for G in 11 12 13 14 15 16 17 18; do
    passage graine$G-meme-rho0.17 --graine $G --comparateurs 8 --K 10,5 --K-s 10 --tailles 288,400 $(ab 0.17 0.17)
  done
  ;;
partielle)
  R3="--comparateurs 8 --K 10,5 --K-s 10 --tailles 288,400 $(ab 0.17 0.17)"
  for S_ in 3 2; do
    passage strates-partielle-f0.5-S$S_-g0.4-brut $R3 --strates $S_ --amplitude-strates 0.4 --portee-strates partielle --fraction-strates-comparateurs 0.5
    passage strates-partielle-f0.5-S$S_-g0.4-calibre $R3 --strates $S_ --amplitude-strates 0.4 --portee-strates partielle --fraction-strates-comparateurs 0.5 --calibrage-par-strate
  done
  ;;
*) echo "usage : sh lancer-complements-v9.sh rhoh|graines|partielle"; exit 2;;
esac
