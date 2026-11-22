#!/bin/bash
# Compare par programme les identifiants v11 de la liste v2 avec ceux de echecs-avec.txt
D=/tmp/claude-0/-home-user-controle-ia-travail/d90e22c7-b755-5554-90ae-faa848d18eef/scratchpad/contre-lecture-greffon-v2-b
LISTE=/home/user/arbre-main-suite-greffon/tests/echecs-connus-v2.txt
AVEC=/home/user/controle-ia-travail/registres/essaim/vers-mere/annexe-comparaison-greffon-2026-11-22-v1/echecs-avec.txt
grep -v '^#' "$LISTE" | cut -f1 | grep 'test_lancer_course_auto_conception_v11' | sort > "$D/tables/ids-liste-v11.txt"
grep '^FAILED ' "$AVEC" | sed 's/^FAILED //; s/ - .*$//' | grep 'test_lancer_course_auto_conception_v11' | sort > "$D/tables/ids-echecs-avec-v11.txt"
wc -l "$D/tables/ids-liste-v11.txt" "$D/tables/ids-echecs-avec-v11.txt"
echo "--- seulement liste:"; comm -23 "$D/tables/ids-liste-v11.txt" "$D/tables/ids-echecs-avec-v11.txt"
echo "--- seulement echecs-avec:"; comm -13 "$D/tables/ids-liste-v11.txt" "$D/tables/ids-echecs-avec-v11.txt"
echo "--- communs:"; comm -12 "$D/tables/ids-liste-v11.txt" "$D/tables/ids-echecs-avec-v11.txt" | wc -l
# v1: 4 lignes
grep -v '^#' "$LISTE" | cut -f1 | grep -v v11 | sort > "$D/tables/ids-liste-v1-4.txt"
grep -v '^#' /home/user/arbre-main-suite-greffon/tests/echecs-connus-v1.txt | cut -f1 | sort > "$D/tables/ids-v1.txt"
echo "--- v1 vs 4 lignes v2:"; comm -3 "$D/tables/ids-v1.txt" "$D/tables/ids-liste-v1-4.txt" | wc -l
echo "--- lignes complètes v1 dans v2 (identiques):"; grep -v '^#' /home/user/arbre-main-suite-greffon/tests/echecs-connus-v1.txt | sort | comm -23 - <(grep -v '^#' "$LISTE" | sort) | wc -l
echo "--- echecs-avec: lignes FAILED hors liste v2 (total):"; grep '^FAILED ' "$AVEC" | sed 's/^FAILED //; s/ - .*$//' | sort | comm -23 - <(grep -v '^#' "$LISTE" | cut -f1 | sort) | wc -l
