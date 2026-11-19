#!/bin/bash
# Passe 1 (regle ecrite dans grille_ab_v1.py avant tout resultat) : les deux cases de la passe 0 dont un taux aux trois
# lectures n'est pas sous le seuil d'au moins deux erreurs de Monte-Carlo, rejouees sur graine neuve, R = 4000, B = 1000.
cd "$(dirname "$0")"
export PYTHONDONTWRITEBYTECODE=1
printf 'K16 g00 3 45\nKH g00 3 60\n' > ../sorties/cases_ab_passe1.txt
cat ../sorties/cases_ab_passe1.txt | xargs -P 2 -L 1 sh -c 'python3 -B grille_ab_v1.py $0 $1 $2 $3 4000 1000 1 ../sorties/ab_$0_$1_k$2_T$3_p1.json 2> ../sorties/ab_$0_$1_k$2_T$3_p1.err'
date -u +%FT%TZ > ../sorties/FINI_ab_passe1
