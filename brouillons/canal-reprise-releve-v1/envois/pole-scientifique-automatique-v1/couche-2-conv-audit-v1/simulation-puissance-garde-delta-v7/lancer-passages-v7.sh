#!/bin/sh
# Lance les passages de la v7 (R12 : aucune sortie existante n'est écrasée, le script refuse). Deux voies, une par processeur :
#   sh lancer-passages-v7.sh voie1     sh lancer-passages-v7.sh voie2
# À lancer depuis le dossier du script. Chaque passage écrit lui-même sa sortie, son journal et son manifeste (GD4-05).
# Durée maximale par passage : 1 500 s (25 minutes) ; au-delà, relancer avec --repetitions 1000 sous un autre nom et le dire.
set -u
S=simulation-puissance-garde-delta-v7
V6=../simulation-puissance-garde-delta-v6/simulation-puissance-garde-delta-v6.py
PY="python3 -I -B $S.py"
LIM="timeout 1500"
# paramètres décidés (R-416, R-435, R-446) et périmètre de la v7 : k = 8, τ = 0,01, δ = 0,05, 288 unités, lecture (A), m = 2 (seuil 40),
# seuil 160 en référence ; biais 0 et δ/4 = 0,0125 ; K_h ∈ {10, 5} × K_s ∈ {10, 5, 3} (produit cartésien, --K-s) ; 2 000 répétitions
DECIDES="--repetitions 2000 --comparateurs 8 --K 10,5 --K-s 10,5,3 --taux 0.01 --deltas 0.05 --biais 0,0.0125 --tailles 288 --lecture-ebh A --m 8,2 --sans-n80"
case "$1" in
voie1)
  # (iv) identité avec la v6 : rejeu, par le script v7, de deux commandes v6 (mêmes options, même graine ; seuls le script et la sortie changent)
  $LIM $PY --repetitions 2000 --comparateurs 8 --K 10,5,3 --taux 0.01 --deltas 0.05 --biais 0,0.0125 --tailles 160,288,300,400 --lecture-ebh A --m 8,2 --sortie $S-sortie-rejeu-v6-principale.json
  echo "rejeu v6 principale : code $?"
  $LIM $PY --repetitions 2000 --comparateurs 8 --K 10,5,3 --taux 0.01 --deltas 0.05 --biais 0,0.0125 --tailles 160,288,300,400 --lecture-ebh A --m 8,2 --sans-n80 --effet-unite-comparateurs 1.0 --sortie $S-sortie-rejeu-v6-dispersion-1.0-independante.json
  echo "rejeu v6 dispersion 1.0 : code $?"
  # (i) échelle logit (v6), K_s ≠ K_h : σ = 0, 0,5, 1,0
  $LIM $PY $DECIDES --sortie $S-sortie-logit-0.json
  echo "logit 0 : code $?"
  $LIM $PY $DECIDES --effet-unite-comparateurs 0.5 --sortie $S-sortie-logit-0.5.json
  echo "logit 0.5 : code $?"
  $LIM $PY $DECIDES --effet-unite-comparateurs 1.0 --sortie $S-sortie-logit-1.0.json
  echo "logit 1.0 : code $?"
  ;;
voie2)
  # (ii) échelle bêta (doute 1), K_s ≠ K_h : σ de référence 0,5 et 1,0
  $LIM $PY $DECIDES --effet-unite-comparateurs 0.5 --echelle-dispersion beta --sortie $S-sortie-beta-0.5.json
  echo "beta 0.5 : code $?"
  $LIM $PY $DECIDES --effet-unite-comparateurs 1.0 --echelle-dispersion beta --sortie $S-sortie-beta-1.0.json
  echo "beta 1.0 : code $?"
  # (iii) n80 sous la loi bêta à σ = 1,0, (K_h, K_s) = (10, 10) et (5, 5), à 288 unités (les cellules de ce passage doublent celles de beta-1.0 : mêmes étiquettes, mêmes tirages)
  $LIM $PY --repetitions 2000 --comparateurs 8 --K 10,5 --taux 0.01 --deltas 0.05 --biais 0,0.0125 --tailles 288 --lecture-ebh A --m 8,2 --effet-unite-comparateurs 1.0 --echelle-dispersion beta --sortie $S-sortie-n80-beta-1.0.json
  echo "n80 beta 1.0 : code $?"
  ;;
*) echo "usage : sh lancer-passages-v7.sh voie1|voie2"; exit 2;;
esac
