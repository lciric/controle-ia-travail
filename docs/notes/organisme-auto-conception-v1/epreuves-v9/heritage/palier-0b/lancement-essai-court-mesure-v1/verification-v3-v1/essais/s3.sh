#!/bin/bash
# Scénario générique sur le gardien v3. Écrit seulement sous v3/e/NOM.
# Usage : s3.sh NOM MODE SEUIL_N SEUIL_LIBRE|auto-MARGE OCTETS PAS DUREE_S KILLCHEF(0|1) TEMOIN(0|1)
#   SEUIL_LIBRE « auto-M » : seuil = octets libres relevés au départ − M (place factice, jamais en remplissant le disque).
set -u
V=/tmp/claude-0/-home-user-controle-ia-travail/d90e22c7-b755-5554-90ae-faa848d18eef/scratchpad/verificateur-gardien-v2/v3
P=${PIECES:-$V/pieces}
N=$1; MODE=$2; SN=$3; SL=$4; OCT=$5; PAS=$6; DUREE=$7; KILL=$8; TEMOIN=$9
T=$V/e/$N/tenue
S=$V/e/$N/sorties
M=$V/e/$N/marqueur
mkdir -p "$T"
case "$SL" in
  auto-*) MARGE=${SL#auto-}
          set -- $(stat -f -c '%a %S' "$V/e")
          SL=$(( $1 * $2 - MARGE ))
          echo "seuil de place factice : $SL" ;;
esac
if [ "$TEMOIN" = 1 ]; then
  setsid nohup /bin/sleep 120 < /dev/null > /dev/null 2>&1 &
  TP=$!
  echo "témoin sans lien : $TP"
fi
bash $P/demarrer-essai-court-v2.sh "$T" $P/lanceur-factice-v.sh "$S" "$PAS" "$OCT" "$DUREE" "$MODE" "$M"
bash $P/demarrer-gardien-essai-court-v3.sh "$T" --sorties "$S" --seuil-n "$SN" --seuil-libre-octets "$SL" --duree-etape-4-s 100000 --intervalle-s 1 --delai-force-s 5
if [ "$KILL" = 1 ]; then
  sleep 2
  CHEF=$(cat "$T/pid-essai-court.txt")
  echo "chef $CHEF tué par moi (SIGKILL) à $(date -u +%H:%M:%S.%N)"
  kill -9 "$CHEF"
fi
GP=$(cat "$T/pid-gardien-essai-court.txt")
for i in $(seq 1 90); do
  if [ ! -e "/proc/$GP" ]; then break; fi
  sleep 1
done
echo "gardien $GP : $(stat -c %n /proc/$GP 2>/dev/null || echo absent) après $i s"
echo "--- descendants relevés (journal) : $(grep -o 'descendants_vivants=[^;]*' "$T/journal-de-tenue-essai-court.txt" | sort -u | tr '\n' ' ')"
for p in $(grep -o 'descendants_vivants=[0-9,]*' "$T/journal-de-tenue-essai-court.txt" | sed 's/descendants_vivants=//' | tr ',' '\n' | sort -u); do
  echo "descendant $p : $(stat -c %n /proc/$p 2>/dev/null || echo absent)"
done
echo "--- fin du journal :"
tail -n 3 "$T/journal-de-tenue-essai-court.txt" | cut -c1-400
echo "--- arret-gardien.txt :"
cat "$T/arret-gardien.txt" 2>/dev/null | cut -c1-400 || true
[ -f "$T/arret-gardien.txt" ] || echo "(absent)"
echo "--- mesure-essai-court.txt :"
cat "$T/mesure-essai-court.txt" 2>/dev/null || echo "(absent)"
if [ "$TEMOIN" = 1 ]; then
  echo "--- témoin $TP : $(stat -c %n /proc/$TP 2>/dev/null || echo ABSENT)"
fi
if [ -f "$M.pid" ]; then
  BP=$(cat "$M.pid")
  echo "enfant/orphelin $BP : $(stat -c %n /proc/$BP 2>/dev/null || echo absent)"
  echo "dossiers de source maintenant : $(ls -d $S/etape-4/couche-mecanique/bras-1-a-3/*/*/* | wc -l)"
  sleep 3
  echo "dossiers de source 3 s plus tard : $(ls -d $S/etape-4/couche-mecanique/bras-1-a-3/*/*/* | wc -l)"
fi
