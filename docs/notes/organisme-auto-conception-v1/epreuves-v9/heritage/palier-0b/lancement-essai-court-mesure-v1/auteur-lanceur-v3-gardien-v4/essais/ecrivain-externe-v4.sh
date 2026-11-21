#!/bin/bash
# Correction 2 de l'erratum 2 (rejouée sur la v4, arrêt de mesure ARMÉ) : un écrivain hors de l'arbre du programme
# (enfant-b.py de la vérification v2, lancé par moi en session à part, jamais relevé par le gardien) crée un dossier de source
# toutes les 0,2 s sous etape-4 ; le gardien arrête le programme par n. Attendu : « dossier NON figé » après dix paires.
# L'écrivain est arrêté ensuite par moi, par son identifiant.
# Usage : ecrivain-externe-v4.sh NOM COPIE
set -u
E=$(cd "$(dirname "$0")" && pwd)
B=$(cd "$E/.." && pwd)
PY=/home/user/controle-ia-travail/.venv/bin/python
NOM=$1
COPIE=$2
D=$E/e/$NOM
T=$D/tenue
S=$D/sorties
M=$D/marqueur
W=$D/ecrivain
I=$D/interprete-factice
if [ -e "$D" ]; then echo "refus : $D existe" >&2; exit 1; fi
mkdir -p "$T"
cp "$E/interprete-factice-v4.sh" "$I"
chmod u+x "$I"
printf '%s\n' "$PY" -I -B "$E/copies/verification-v2/prog-v.py" "$S" 0.5 1000 60 simple "$M" > "$I.args"
bash "$B/demarrer-essai-3-v3.sh" "$T" "$COPIE" "$I" "$S"
H=$(date -u -d "@$(( $(date -u +%s) + 3600 ))" +%Y-%m-%dT%H:%M:%SZ)
bash "$B/demarrer-gardien-essai-3-v4.sh" "$T" "$PY" --sorties "$S" --heure-arret-duree "$H" --arret-mesure arme --seuil-n 8 --seuil-libre-octets 1 --duree-etape-4-s 100000 --intervalle-s 1 --delai-force-s 5
GP=$(cat "$T/pid-gardien-essai-3.txt")
sleep 1.5
setsid nohup "$PY" -I -B "$E/copies/verification-v2/enfant-b.py" "$S" "$W" < /dev/null > /dev/null 2>&1 &
echo "écrivain externe lancé par moi : processus $!"
for i in $(seq 1 90); do
  if [ ! -e "/proc/$GP" ]; then break; fi
  sleep 1
done
echo "=== gardien $GP : $(stat -c %n /proc/$GP 2>/dev/null || echo absent) après $i s"
echo "--- arret-gardien.txt :"
cat "$T/arret-gardien.txt"
WP=$(cat "$W.pid")
echo "--- écrivain $WP : $(stat -c %n /proc/$WP 2>/dev/null || echo absent)"
kill -9 "$WP"
sleep 2
echo "--- écrivain arrêté par moi par son identifiant : $(stat -c %n /proc/$WP 2>/dev/null || echo absent)"
