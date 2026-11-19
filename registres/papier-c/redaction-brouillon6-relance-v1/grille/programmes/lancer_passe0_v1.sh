#!/bin/bash
# Passe 0 de la grille de la clause de repli (graine racine 20261119, derivation par case : grille_commun_v1.generateur).
# 1) C-P3c : 8 modeles d'erreur x 3 attaques x k = 3, 5 x T = 45, 60 = 96 cases, R = 8000 essais, plus 4 cases d'effet.
# 2) C-P3a et C-P3b : 7 modeles (E40 homogene deja joue par le redacteur pour g = 0 et 0,10) x 3 x 2 x 2 = 84 cases,
#    R = 1000 essais, B = 1000 tirages ; plus 2 cases de recoupement E40 (cas sain) et 2 cases d'effet (artefact, R = 400).
# Quatre processus a la fois ; une sortie JSON par case ; les erreurs vont dans un .err par case.
cd "$(dirname "$0")"
export PYTHONDONTWRITEBYTECODE=1
S=../sorties
: > $S/cases_c_passe0.txt; : > $S/cases_ab_passe0.txt
for m in E30 E40 E60 EH K16 KH MH M616; do for a in g00 g10 g20; do for k in 3 5; do for T in 45 60; do
  echo "$m $a $k $T 8000" >> $S/cases_c_passe0.txt; done; done; done; done
for m in P3 P6; do for T in 45 60; do echo "$m g10 5 $T 8000" >> $S/cases_c_passe0.txt; done; done
echo "E40 g00 3 45 1000" >> $S/cases_ab_passe0.txt
echo "E40 g10 5 60 1000" >> $S/cases_ab_passe0.txt
echo "P3 g10 5 60 400" >> $S/cases_ab_passe0.txt
echo "P6 g10 5 60 400" >> $S/cases_ab_passe0.txt
for a in g20 g10 g00; do for m in E30 E60 EH K16 KH MH M616; do for k in 3 5; do for T in 45 60; do
  echo "$m $a $k $T 1000" >> $S/cases_ab_passe0.txt; done; done; done; done
cat $S/cases_c_passe0.txt | xargs -P 4 -L 1 sh -c 'python3 -B grille_c_v1.py $0 $1 $2 $3 $4 0 ../sorties/c_$0_$1_k$2_T$3_p0.json 2> ../sorties/c_$0_$1_k$2_T$3_p0.err'
date -u +%FT%TZ > $S/FINI_c_passe0
cat $S/cases_ab_passe0.txt | xargs -P 4 -L 1 sh -c 'python3 -B grille_ab_v1.py $0 $1 $2 $3 $4 1000 0 ../sorties/ab_$0_$1_k$2_T$3_p0.json 2> ../sorties/ab_$0_$1_k$2_T$3_p0.err'
date -u +%FT%TZ > $S/FINI_ab_passe0
