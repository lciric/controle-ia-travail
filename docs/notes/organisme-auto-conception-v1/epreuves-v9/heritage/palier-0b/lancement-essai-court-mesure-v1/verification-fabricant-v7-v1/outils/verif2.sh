#!/bin/bash
# Complément : mutation d'un octet qui passe tous les contrôles du v6 (dans un commentaire entier, retiré à la réduction),
# et dans une ligne protégée ; témoin v6 contre v7.
set -u
W=/tmp/claude-0/-home-user-controle-ia-travail/d90e22c7-b755-5554-90ae-faa848d18eef/scratchpad/verification-fabricant-v7
FAB=$W/fab
T=$W/tables/table-cas2.txt
OUT=$W/tables/sorties2
rm -rf "$OUT" "$W/depot-vide.git" "$W/entrees2"
mkdir -p "$OUT" "$W/entrees2"
git init -q --bare "$W/depot-vide.git"
: > "$T"
export FABRICANT_BANC=oui FABRICANT_DEPOT_DISTANT=$W/depot-vide.git
JF=FACTICE_ESSAI_aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
SCR=$FAB/demarrage-machine-essai-3-v6.sh
sed '2s/Essai 3/Essai 4/' "$SCR" > "$W/entrees2/commentaire.sh"
echo "commentaire : octets différents $(cmp -l "$SCR" "$W/entrees2/commentaire.sh" | wc -l)" >> "$T"
cat "$SCR" "$FAB/essais-outils/queue-a2-chaine.txt" > "$W/entrees2/a2.sh"
for fb in v6 v7; do
  for e in commentaire a2; do
    o=$OUT/$fb-$e
    if [ $e = a2 ]; then x=(FABRICANT_REDUCTEUR=$FAB/essais-outils/reducteur-artefact.sh REDUCTEUR_MODE=naif); else x=(); fi
    r=$(env "${x[@]}" FABRICANT_SCRIPT=$W/entrees2/$e.sh JETON_FACTICE_ESSAI=$JF /bin/bash "$FAB/fabriquer-donnees-demarrage-$fb.sh" JETON_FACTICE_ESSAI "$o" 2>&1); c=$?
    echo "$fb $e : code $c ; $(printf '%s\n' "$r" | grep -m1 '^refus' | cut -c1-120) ; E_SCRIPT dans les données : $(grep -m1 '^E_SCRIPT=' "$o" 2>/dev/null | cut -c1-30)" >> "$T"
  done
done
# fichiers laissés après refus v7
echo "fichiers laissés par v7 : $(ls "$OUT" | grep -c '^v7-')" >> "$T"
rm -rf "$OUT" "$W/entrees2"
cat "$T"
