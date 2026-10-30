#!/bin/sh
# Lance les vérifications de la v8 l'une après l'autre (à lancer depuis le dossier du script ; R12 : les sorties existantes ne sont jamais écrasées, mode « x »).
set -u
V7=../simulation-puissance-garde-delta-v7
POLE=../../orchestrateur-pole-v7/pole/pari_apparie.py
GD7=../contre-lecture-garde-delta-v7
S=simulation-puissance-garde-delta-v8.py
nice -n 10 python3 -I -B verif-identite-v7-v8.py $V7/simulation-puissance-garde-delta-v7.py $S verif-identite-v7-v8-sortie.json > verif-identite-v7-v8-journal.txt 2>&1; echo "identite v7 : $?"
nice -n 10 python3 -I -B verif-identite-gd7-v8.py $S $GD7 verif-identite-gd7-v8-sortie.json > verif-identite-gd7-v8-journal.txt 2>&1; echo "identite gd7 : $?"
nice -n 10 python3 -I -B verif-copule-strates-v8.py $S verif-copule-strates-v8-sortie.json > verif-copule-strates-v8-journal.txt 2>&1; echo "copule strates : $?"
nice -n 10 python3 -I -B verif-ebh-pole-v8.py $S $POLE verif-ebh-pole-v8-sortie.json > verif-ebh-pole-v8-journal.txt 2>&1; echo "ebh pole : $?"
nice -n 10 python3 -I -B precision-rho-pilote-v8.py precision-rho-pilote-v8-sortie.json > precision-rho-pilote-v8-journal.txt 2>&1; echo "precision rho : $?"
nice -n 10 python3 -I -B chiffres-v7-repris-v8.py $V7 chiffres-v7-repris-v8-sortie.json > chiffres-v7-repris-v8-journal.txt 2>&1; echo "chiffres v7 : $?"
# Lancés à la main (dossier de travail neuf, hors du dossier de la v8), mêmes options d'isolement (-I -B) :
#   python3 -I -B verif-sans-git-v8.py $S DOSSIER_NEUF verif-sans-git-v8-sortie.json
#   python3 -I -B essais-entrees-v8.py $S DOSSIER_NEUF essais-entrees-v8-sortie.json > essais-entrees-v8-journal.txt 2>&1
# Les sorties de ces deux vérifications portent l'empreinte du script scellé (4c7c93a9…).
