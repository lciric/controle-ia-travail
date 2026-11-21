#!/bin/bash
# Correction 2 de l'erratum 2, artefact déterministe : un écrivain hors de l'arbre du programme (enfant-b.py de la vérification,
# lancé par moi en session à part, jamais relevé par le gardien) crée un dossier de source toutes les 0,2 s sous etape-4 ; le
# gardien arrête le programme par n. Attendu : « dossier NON figé » après dix paires. L'écrivain est arrêté ensuite par moi,
# par son identifiant. (Le cas « petit-enfant détaché » de la vérification dépend d'une course : le gardien relève parfois B
# pendant la courte vie de A, et l'arrête ; alors le dossier est réellement figé.)
# Usage : ecrivain-externe-v3.sh NOM
set -u
E=$(cd "$(dirname "$0")" && pwd)
B=$(cd "$E/.." && pwd)
NOM=$1
D=$E/e/$NOM
T=$D/tenue
S=$D/sorties
M=$D/marqueur
W=$D/ecrivain
if [ -e "$D" ]; then echo "refus : $D existe" >&2; exit 1; fi
mkdir -p "$T"
bash "$B/demarrer-essai-court-v2.sh" "$T" "$E/lanceur-py-v3.sh" "$E/verification-v2-copie/prog-v.py" "$S" 0.5 1000 60 simple "$M"
bash "$B/demarrer-gardien-essai-court-v3.sh" "$T" --sorties "$S" --seuil-n 8 --seuil-libre-octets 1 --duree-etape-4-s 100000 --intervalle-s 1 --delai-force-s 5
GP=$(cat "$T/pid-gardien-essai-court.txt")
sleep 1.5
setsid nohup /home/user/controle-ia-travail/.venv/bin/python -I -B "$E/verification-v2-copie/enfant-b.py" "$S" "$W" < /dev/null > /dev/null 2>&1 &
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
