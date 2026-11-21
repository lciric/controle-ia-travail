#!/bin/bash
# Scénario sur le gardien v4 (départ v3 du programme factice, départ v4 du gardien). Écrit seulement sous v4/e/NOM.
# Usage : s4.sh NOM MODE DELTA_S SEUIL_LIBRE|auto-M MESURE(desarme|arme|-) SEUIL_N OCTETS PAS DUREE_S KILLCHEF TEMOIN
#   DELTA_S : heure d'arrêt de durée = maintenant + DELTA_S secondes (négatif : heure passée).
#   MESURE « - » : option non passée (valeur d'emploi : désarmé).
set -u
V=/tmp/claude-0/-home-user-controle-ia-travail/d90e22c7-b755-5554-90ae-faa848d18eef/scratchpad/verificateur-gardien-v2/v4
P=$V/pieces
PY=/home/user/controle-ia-travail/.venv/bin/python
N=$1; MODE=$2; DELTA=$3; SL=$4; MES=$5; SN=$6; OCT=$7; PAS=$8; DUREE=$9
shift 9
KILL=$1; TEMOIN=$2
T=$V/e/$N/tenue
S=$V/e/$N/sorties
M=$V/e/$N/marqueur
mkdir -p "$T"
case "$SL" in
  auto-*) MARGE=${SL#auto-}
          set -- $(stat -f -c '%a %S' "$V/e")
          SL=$(( $1 * $2 - MARGE )) ;;
esac
H=$(date -u -d "@$(( $(date +%s) + DELTA ))" +%Y-%m-%dT%H:%M:%SZ)
OPT=()
if [ "$MES" != "-" ]; then OPT=(--arret-mesure "$MES"); fi
echo "heure d'arrêt de durée : $H (maintenant $(date -u +%H:%M:%SZ)) ; seuil de place $SL ; mesure ${MES}"
if [ "$TEMOIN" = 1 ]; then
  setsid nohup /bin/sleep 120 < /dev/null > /dev/null 2>&1 &
  TP=$!
  echo "témoin sans lien : $TP"
fi
bash $P/demarrer-essai-3-v3.sh --lanceur $P/lanceur-factice-v.sh "$T" "$S" "$PAS" "$OCT" "$DUREE" "$MODE" "$M" > /dev/null
bash $P/demarrer-gardien-essai-3-v4.sh "$T" "$PY" --sorties "$S" --heure-arret-duree "$H" --seuil-n "$SN" --seuil-libre-octets "$SL" --duree-etape-4-s 100000 --intervalle-s 1 --delai-force-s 5 "${OPT[@]}"
echo "code du départ du gardien : $?"
if [ "$KILL" = 1 ]; then
  sleep 2
  CHEF=$(cat "$T/pid-essai-3.txt")
  echo "chef $CHEF tué par moi (SIGKILL)"
  kill -9 "$CHEF"
fi
GP=$(cat "$T/pid-gardien-essai-3.txt" 2>/dev/null || echo 0)
for i in $(seq 1 ${ATTENTE:-60}); do
  if [ ! -e "/proc/$GP" ]; then break; fi
  sleep 1
done
echo "gardien $GP : $(stat -c %n /proc/$GP 2>/dev/null || echo absent) après $i s ; maintenant $(date -u +%H:%M:%SZ)"
echo "--- arret-gardien.txt :"
cat "$T/arret-gardien-essai-3.txt" 2>/dev/null | cut -c1-330 || true
cat "$T/arret-gardien.txt" 2>/dev/null | cut -c1-330 || echo "(absent)"
echo "--- mesure : $( [ -f "$T/mesure-essai-3.txt" ] && echo PRÉSENTE || echo absente )"
[ -f "$T/mesure-essai-3.txt" ] && grep -E 'état du dossier' "$T/mesure-essai-3.txt" | cut -c1-260
echo "--- descendants relevés : $(grep -o 'descendants_vivants=[0-9,]*' "$T/journal-de-tenue-essai-3.txt" | sed 's/descendants_vivants=//' | tr ',' '\n' | sort -u | tr '\n' ' ')"
for p in $(grep -o 'descendants_vivants=[0-9,]*' "$T/journal-de-tenue-essai-3.txt" | sed 's/descendants_vivants=//' | tr ',' '\n' | sort -u); do
  echo "descendant $p : $(stat -c %n /proc/$p 2>/dev/null || echo absent)"
done
echo "--- fin du journal :"
tail -n 2 "$T/journal-de-tenue-essai-3.txt" | cut -c1-300
if [ "$TEMOIN" = 1 ]; then
  echo "--- témoin $TP : $(stat -c %n /proc/$TP 2>/dev/null || echo ABSENT)"
fi
if [ -f "$M.pid" ]; then
  BP=$(cat "$M.pid")
  echo "enfant/orphelin $BP : $(stat -c %n /proc/$BP 2>/dev/null || echo absent)"
fi
echo "--- code-de-sortie : $(cat $T/code-de-sortie.txt 2>/dev/null || echo absent)"
