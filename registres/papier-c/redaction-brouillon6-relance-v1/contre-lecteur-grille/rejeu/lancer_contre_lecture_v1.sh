#!/bin/bash
# Rejeux du contre-lecteur. Quatre processus a la fois.
cd "$(dirname "$0")"
export PYTHONDONTWRITEBYTECODE=1
S=sorties
cat > $S/taches.txt <<'T'
programmes/grille_ab_v1.py K16 g00 3 45 1000 1000 0 S/ab_K16_g00_k3_T45_p0.json
programmes/grille_ab_v1.py MH g20 5 60 1000 1000 0 S/ab_MH_g20_k5_T60_p0.json
programmes/grille_ab_v1.py P6 g10 5 60 400 1000 0 S/ab_P6_g10_k5_T60_p0.json
programmes/grille_c_v1.py E30 g00 3 45 8000 0 S/c_E30_g00_k3_T45_p0.json
programmes/grille_c_v1.py K16 g00 3 45 8000 0 S/c_K16_g00_k3_T45_p0.json
cp3c_lecture_ii_v1.py E30 g00 3 45 2000 1000 S/ii_E30_g00_k3_T45.json
cp3c_lecture_ii_v1.py E30 g10 5 60 2000 1000 S/ii_E30_g10_k5_T60.json
cp3c_lecture_ii_v1.py E60 g10 5 60 2000 1000 S/ii_E60_g10_k5_T60.json
cp3c_lecture_ii_v1.py M616 g10 3 45 2000 1000 S/ii_M616_g10_k3_T45.json
cp3c_lecture_ii_v1.py KH g20 5 60 2000 1000 S/ii_KH_g20_k5_T60.json
cp3c_lecture_ii_v1.py KH g10 5 60 2000 1000 S/ii_KH_g10_k5_T60.json
cp3c_lecture_ii_v1.py MH g20 5 60 2000 1000 S/ii_MH_g20_k5_T60.json
cp3c_lecture_ii_v1.py MH g20 3 45 2000 1000 S/ii_MH_g20_k3_T45.json
ab_cases_neuves_v1.py K16s20 g00 3 45 1000 1000 0 S/abn_K16s20_g00_k3_T45.json
ab_cases_neuves_v1.py K16s60 g00 3 45 1000 1000 0 S/abn_K16s60_g00_k3_T45.json
ab_cases_neuves_v1.py K10 g00 3 45 1000 1000 0 S/abn_K10_g00_k3_T45.json
ab_cases_neuves_v1.py KHs60 g00 3 45 1000 1000 0 S/abn_KHs60_g00_k3_T45.json
meca1_independant_v1.py 20000 > S/meca1_v1.txt
T
sed -i "s# S/# $S/#g" $S/taches.txt
date -u +%FT%TZ > $S/DEBUT
cat $S/taches.txt | xargs -P 4 -I{} sh -c 'python3 -B {} 2>> sorties/erreurs.txt'
date -u +%FT%TZ > $S/FINI
