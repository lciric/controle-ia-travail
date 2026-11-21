#!/bin/bash
# Commande à l'octet (contre-lecture E5 et vérification, mode 4) sur le lanceur v2 copié dans le dossier v3 : argv par bash
# (« env » remplacé par un enregistreur) pour les deux extractions et le lanceur ; trois lanceurs altérés (objets faux).
# Usage : argv-v3.sh NOM
set -u
E=$(cd "$(dirname "$0")" && pwd)
B=$(cd "$E/.." && pwd)
D=$E/e/$1
if [ -e "$D" ]; then echo "refus : $D existe" >&2; exit 1; fi
mkdir -p "$D"
PY=/home/user/controle-ia-travail/.venv/bin/python
REC="$PY -I $E/contre-lecture-v1-copie/enregistreur.py"
L=$B/lancer-essai-court-v2.sh
SORTIES=/home/user/palier-0b-racine/diag/heritage-palier-0b-v1/etapes-3-a-6-essai-court-mesure-v1
argv_de() {
  grep '^env -C ' "$1" | sed "s|^env |$REC |" > "$2.sh"
  bash "$2.sh" > "$2.txt"
}
argv_de "$B/complement-1-v3-extraction-v1.md" "$D/argv-extraction-v1"
argv_de "$B/complement-1-v3-extraction-v2.md" "$D/argv-extraction-v2"
argv_de "$L" "$D/argv-lanceur"
echo "--- diff extraction v1 / lanceur (seul le 10e argument doit différer) :"
diff "$D/argv-extraction-v1.txt" "$D/argv-lanceur.txt"
echo "diff code $?"
echo "--- diff extraction v1 / extraction v2 :"
diff "$D/argv-extraction-v1.txt" "$D/argv-extraction-v2.txt"
echo "diff code $?"
echo "lignes « env » du lanceur : $(grep -c '^env ' "$L")"
sed 's|^env -C \(.*\) -B |env -C \1 -b |' "$L" > "$D/altere-octet.sh"
sed 's|^env -C \(.*\)/home/user/palier-0b-racine /home|env -C \1/home/user/palier-0b-racine --en-trop /home|' "$L" > "$D/altere-argument.sh"
sed 's|^\(env -C .*\)$|\1\n\1|' "$L" > "$D/altere-deux-lignes.sh"
for f in altere-octet altere-argument altere-deux-lignes; do
  "$PY" -I -B "$B/verifier-commande-v2.py" "$B/complement-1-v3-extraction-v1.md" "$D/$f.sh" "$SORTIES" > "$D/$f-verif.txt"
  echo "$f : code du vérificateur $? (attendu 1) : $(tail -n 1 "$D/$f-verif.txt")"
done
for x in v1 v2; do
  "$PY" -I -B "$B/verifier-commande-v2.py" "$B/complement-1-v3-extraction-$x.md" "$L" "$SORTIES" > "$D/vrai-$x-verif.txt"
  echo "lanceur, extraction $x : code $? (attendu 0) : $(tail -n 1 "$D/vrai-$x-verif.txt")"
done
