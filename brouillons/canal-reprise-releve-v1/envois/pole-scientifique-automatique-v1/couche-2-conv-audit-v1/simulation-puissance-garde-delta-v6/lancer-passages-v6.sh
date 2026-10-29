#!/bin/sh
# Lance les passages de la v6 (R12 : aucune sortie existante n'est écrasée, le script refuse). Deux voies, une par processeur :
#   sh lancer-passages-v6.sh voie1     sh lancer-passages-v6.sh voie2
# À lancer depuis le dossier du script. Chaque passage écrit lui-même sa sortie, son journal et son manifeste (GD4-05).
# Durée maximale par passage : 1 500 s (25 minutes) ; au-delà, relancer avec --repetitions 1000 sous un autre nom et le dire.
set -u
S=simulation-puissance-garde-delta-v6
PY="python3 -I -B $S.py"
LIM="timeout 1500"
# paramètres décidés (R-416, R-435, R-446) : k = 8, τ = 0,01, δ = 0,05, K_h = 10, 5, 3 ; biais 0 et δ/4 = 0,0125 ;
# tailles 160, 288, 300, 400 ; lecture (A), m = 2 (seuil 40) et seuil 160 en référence ; 2 000 répétitions
DECIDES="--repetitions 2000 --comparateurs 8 --K 10,5,3 --taux 0.01 --deltas 0.05 --biais 0,0.0125 --tailles 160,288,300,400 --lecture-ebh A --m 8,2"
case "$1" in
voie1)
  # (i) passage principal (avec n80, sur les comparateurs seuls)
  $LIM $PY $DECIDES --sortie $S-sortie-principale.json
  echo "principale : code $?"
  # (ii) sensibilité à la dispersion des comparateurs, indépendante entre comparateurs
  $LIM $PY $DECIDES --sans-n80 --effet-unite-comparateurs 0.5 --sortie $S-sortie-dispersion-0.5-independante.json
  echo "dispersion 0.5 indépendante : code $?"
  $LIM $PY $DECIDES --sans-n80 --effet-unite-comparateurs 1.0 --sortie $S-sortie-dispersion-1.0-independante.json
  echo "dispersion 1.0 indépendante : code $?"
  # (iii) α_c = 0,025 (seuils 320 et 80)
  $LIM $PY $DECIDES --sans-n80 --alpha 0.025 --sortie $S-sortie-alpha-0.025.json
  echo "alpha 0.025 : code $?"
  # complémentaire (GD5-01, hors de la liste) : effet d'unité sur A (logit 1,0), lien tenu et lien coupé, avec e-BH à k = 8
  $LIM $PY $DECIDES --sans-n80 --effet-unite-a 1.0 --lien-coupe --sortie $S-sortie-effet-A-1.0.json
  echo "effet A 1.0 : code $?"
  ;;
voie2)
  # (iv) rejeu de deux commandes v5 (mêmes options, même graine ; seuls le script et la sortie changent)
  $LIM $PY --repetitions 2000 --comparateurs 1,3,8 --tailles 160,300,400,650 --K 10,3 --taux 0.01 --biais 0,0.0125 --deltas 0.05,0.075 --lecture-ebh A,B --m 8,2,16 --sans-n80 --sortie $S-sortie-rejeu-v5-principale.json
  echo "rejeu v5 principale : code $?"
  $LIM $PY --repetitions 2000 --comparateurs 8 --tailles 160,400,650 --K 10,3 --taux 0.01 --biais 0 --deltas 0.05,0.075 --lecture-ebh A,B --fiches-nulles 2 --m 8,4,18 --sans-n80 --sortie $S-sortie-rejeu-v5-fiches-nulles-2.json
  echo "rejeu v5 fiches nulles : code $?"
  # (ii) suite : avec corrélation ρ = 0,17 entre comparateurs
  $LIM $PY $DECIDES --sans-n80 --effet-unite-comparateurs 0.5 --correlation-comparateurs 0.17 --sortie $S-sortie-dispersion-0.5-rho-0.17.json
  echo "dispersion 0.5 rho 0.17 : code $?"
  $LIM $PY $DECIDES --sans-n80 --effet-unite-comparateurs 1.0 --correlation-comparateurs 0.17 --sortie $S-sortie-dispersion-1.0-rho-0.17.json
  echo "dispersion 1.0 rho 0.17 : code $?"
  # complémentaire (P-9, hors de la liste) : n80 des comparateurs seuls sous dispersion, à 288 unités seulement
  $LIM $PY --repetitions 2000 --comparateurs 8 --K 10,5,3 --taux 0.01 --deltas 0.05 --biais 0,0.0125 --tailles 288 --lecture-ebh A --m 8,2 --effet-unite-comparateurs 0.5 --sortie $S-sortie-n80-dispersion-0.5.json
  echo "n80 dispersion 0.5 : code $?"
  $LIM $PY --repetitions 2000 --comparateurs 8 --K 10,5,3 --taux 0.01 --deltas 0.05 --biais 0,0.0125 --tailles 288 --lecture-ebh A --m 8,2 --effet-unite-comparateurs 1.0 --sortie $S-sortie-n80-dispersion-1.0.json
  echo "n80 dispersion 1.0 : code $?"
  ;;
*) echo "usage : sh lancer-passages-v6.sh voie1|voie2"; exit 2;;
esac
