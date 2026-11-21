#!/bin/bash
# Compare les argv obtenus par bash pour la ligne du complément (ligne 37) et celle du lanceur (ligne 96), « env » remplacé par un enregistreur.
D=/tmp/claude-0/-home-user-controle-ia-travail/d90e22c7-b755-5554-90ae-faa848d18eef/scratchpad/contre-lecteur-gardien-palier-0b
A=/home/user/controle-ia-travail/docs/notes/organisme-auto-conception-v1/epreuves-v9/heritage/palier-0b/lancement-essai-court-mesure-v1/auteur-v1
PY=/home/user/controle-ia-travail/.venv/bin/python
REC="$PY -I $D/enregistreur.py"
sed -n 37p "$D/complement-v3.md" | sed "s|^env |$REC |" > "$D/ligne-complement.sh"
sed -n 96p "$A/lancer-essai-court-v1.sh" | sed "s|^env |$REC |" > "$D/ligne-lanceur.sh"
bash "$D/ligne-complement.sh" > "$D/argv-complement.txt"
bash "$D/ligne-lanceur.sh" > "$D/argv-lanceur.txt"
wc -l "$D/argv-complement.txt" "$D/argv-lanceur.txt"
diff "$D/argv-complement.txt" "$D/argv-lanceur.txt"
echo "diff code $?"
grep -c '^env ' "$A/lancer-essai-court-v1.sh"
grep -n 'env ' "$A/lancer-essai-court-v1.sh"
