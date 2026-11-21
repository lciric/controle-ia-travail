#!/bin/bash
# Banc v4, correction R2 (course du relecteur, p1-course.sh, reprise) : pendant que l'amorce tourne, un processus de même
# uid remplace en boucle, par renommage atomique, le script de la charge par l'un ou l'autre de deux scripts témoins
# (« stubs ») qui affichent l'empreinte du fichier d'où ils sont lus et sortent en 7. Compte, sur N exécutions, celles où
# le script LU n'est pas celui dont l'empreinte a été contrôlée (« lecture divergente »).
#   v4 (à éprouver) : attendu 0 lecture divergente ; v3 (objet vrai, relu par chemin) : lectures divergentes possibles.
# Données fabriquées par les vrais fabricants v3 et v4 (FABRICANT_SCRIPT = stub 1 ; banc ; dépôt FACTICE).
# Emploi : course-amorce.sh N DEPOT_FACTICE_SANS_BRANCHE
set -u
N=$1
O=$(cd "$(dirname "$0")" && pwd); ESS=$(dirname "$O"); V4=$(dirname "$ESS"); AUT=$(dirname "$V4")
W=$ESS/travail/course
[ ! -e "$W" ] || { echo "refus : $W existe"; exit 1; }
mkdir -p "$W/st1" "$W/st2"
JB=$AUT/essais/travail/jeton-factice.txt
{ echo '#!/bin/bash'; echo '# script temoin de la course (stub)'; grep -E '^(BRANCHE|DEPOT_URL)=' "$V4/demarrage-machine-essai-3-v4.sh"
  # les quatre lignes d'empreinte des pièces, exigées par le fabricant, en commentaires
  grep -E '^(PIECES=")?[0-9a-f]{64} [a-z0-9.-]+"?$' "$V4/demarrage-machine-essai-3-v4.sh" | sed -e 's/^PIECES="//' -e 's/"$//' -e 's/^/# /'
  echo 'echo "STUB-SHA $(sha256sum < "${BASH_SOURCE[0]}" | cut -c1-64)"'; echo 'exit 7'; } > "$W/st1/stub.sh"
{ cat "$W/st1/stub.sh"; echo '# variante 2'; } > "$W/st2/stub.sh"
export FABRICANT_BANC=oui FABRICANT_DEPOT_DISTANT=$2 FABRICANT_SCRIPT=$W/st1/stub.sh
for v in 3 4; do
  FAB=$AUT/v$v/fabriquer-donnees-demarrage-v$v.sh
  [ $v = 4 ] && FAB=$V4/fabriquer-donnees-demarrage-v4.sh
  bash "$O/fabricant-avec-jeton.sh" "$JB" "$FAB" "$W/ud-v$v" > "$W/fabrication-v$v.txt" 2>&1
done
T=$W/course.txt
: > "$T"
for v in 3 4; do
  UD=$W/ud-v$v
  [ -s "$UD" ] || { echo "v$v : données absentes (voir fabrication-v$v.txt)" >> "$T"; continue; }
  E1=$(sed -n 4p "$UD" | cut -d= -f2)
  ok=0 alt=0 r18=0 autre=0
  for i in $(seq 1 "$N"); do
    R=$W/run-v$v
    rm -rf "$R" "$R".script.*
    F=$R/demarrage-machine-essai-3-v$v.sh
    ( until [ -e "$F" ]; do :; done
      while :; do cp "$W/st1/stub.sh" "$W/rA"; mv -f "$W/rA" "$F"; cp "$W/st2/stub.sh" "$W/rB"; mv -f "$W/rB" "$F"; done ) &
    RP=$!
    out=$(ESSAI_DEMARRAGE_CHARGE=$R bash "$UD" 2>&1); c=$?
    kill "$RP"; wait "$RP" 2>/dev/null
    s=$(printf '%s\n' "$out" | sed -n 's/^STUB-SHA //p')
    if [ "$c" = 7 ] && [ "$s" = "$E1" ]; then ok=$((ok + 1))
    elif [ "$c" = 7 ]; then alt=$((alt + 1))
    elif [ "$c" = 18 ]; then r18=$((r18 + 1))
    else autre=$((autre + 1)); echo "v$v essai $i : code $c : $(printf '%s' "$out" | head -c 200)" >> "$W/autres.txt"; fi
  done
  rm -rf "$R" "$R".script.*
  echo "v$v : essais $N ; lu = contrôlé : $ok ; LECTURES DIVERGENTES (code 7, empreinte autre que E_SCRIPT) : $alt ; refus 18 : $r18 ; autres codes : $autre" >> "$T"
done
cat "$T"
