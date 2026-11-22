#!/bin/bash
# Banc v6, R2 (course réécrite, visant la COPIE PRIVÉE elle-même, constat du relecteur de la v4) : pendant que l'amorce
# tourne, un processus de même uid guette le dossier privé « $CHARGE.script.* », puis y remplace en boucle, par renommage
# atomique, le fichier « s.sh » tantôt par le texte contrôlé (stub 1, celui dont E_SCRIPT est l'empreinte), tantôt par un
# autre (stub 2). Les deux stubs affichent « STUB-MARQUE 1 » ou « STUB-MARQUE 2 » et sortent en 7. Lecture divergente :
# code 7 et marque 2 (le texte exécuté n'est pas celui dont l'empreinte a été contrôlée).
#   v6 (à éprouver : lecture unique en mémoire, hachage et exécution des mêmes octets) : attendu 0 lecture divergente ;
#   v4 (objet vrai : hachage du fichier, puis lecture du fichier) : au moins 1 attendue ; sinon la course est sans puissance.
# Données fabriquées par les vrais fabricants v4 et v6 (FABRICANT_SCRIPT = stub 1 ; banc ; dépôt FACTICE ; jeton factice).
# Emploi : course-amorce.sh N DEPOT_FACTICE_SANS_BRANCHE
set -u
N=$1
O=$(cd "$(dirname "$0")" && pwd); ESS=$(dirname "$O"); V6=$(dirname "$ESS"); AUT=$(dirname "$V6")
W=$ESS/travail/course
[ ! -e "$W" ] || { echo "refus : $W existe"; exit 1; }
mkdir -p "$W/st1" "$W/st2"
JB=$AUT/essais/travail/jeton-factice.txt
S6=$V6/demarrage-machine-essai-3-v6.sh
stub() {  # $1 : marque
  echo '#!/bin/bash'; echo '# script temoin de la course (stub)'; grep -E '^(BRANCHE|DEPOT_URL)=' "$S6"
  grep -E '^(PIECES=")?[0-9a-f]{64} [a-z0-9.-]+"?$' "$S6" | sed -e 's/^PIECES="//' -e 's/"$//' -e 's/^/: /'
  echo "echo \"STUB-MARQUE $1\""; echo 'exit 7'
}
stub 1 > "$W/st1/stub.sh"; stub 2 > "$W/st2/stub.sh"
export FABRICANT_BANC=oui FABRICANT_DEPOT_DISTANT=$2 FABRICANT_SCRIPT=$W/st1/stub.sh
bash "$O/fabricant-avec-jeton.sh" "$JB" "$AUT/v4/fabriquer-donnees-demarrage-v4.sh" "$W/ud-v4" > "$W/fabrication-v4.txt" 2>&1
bash "$O/fabricant-avec-jeton.sh" "$JB" "$V6/fabriquer-donnees-demarrage-v6.sh" "$W/ud-v6" > "$W/fabrication-v6.txt" 2>&1
# texte contrôlé de chaque version : v4, le stub 1 tel quel ; v6, le stub 1 réduit par le fabricant
cp "$W/st1/stub.sh" "$W/controle-v4.sh"
cp "$W/ud-v6.script-reduit.sh" "$W/controle-v6.sh"
T=$W/course.txt
: > "$T"
for v in 6 4; do
  UD=$W/ud-v$v
  [ -s "$UD" ] || { echo "v$v : données absentes (voir fabrication-v$v.txt)" >> "$T"; continue; }
  E1=$(sed -n 4p "$UD" | cut -d= -f2)
  echo "v$v : E_SCRIPT $E1 ; texte contrôlé $(sha256sum < "$W/controle-v$v.sh" | cut -c1-64)" >> "$T"
  ok=0 alt=0 r18=0 autre=0 vu=0
  for i in $(seq 1 "$N"); do
    R=$W/run-v$v
    rm -rf "$R" "$R".script.*
    rm -f "$W/vu-v$v"
    ( d=
      until [ -n "$d" ]; do for x in "$R".script.*; do [ -d "$x" ] && d=$x; done; done
      echo "$d" > "$W/vu-v$v"
      while :; do cp "$W/controle-v$v.sh" "$d/rA"; mv -f "$d/rA" "$d/s.sh"; cp "$W/st2/stub.sh" "$d/rB"; mv -f "$d/rB" "$d/s.sh"; done ) 2>/dev/null &
    RP=$!
    out=$(ESSAI_DEMARRAGE_CHARGE=$R bash "$UD" 2>&1); c=$?
    kill "$RP"; wait "$RP" 2>/dev/null
    [ -s "$W/vu-v$v" ] && vu=$((vu + 1))
    s=$(printf '%s\n' "$out" | sed -n 's/^STUB-MARQUE //p')
    if [ "$c" = 7 ] && [ "$s" = 1 ]; then ok=$((ok + 1))
    elif [ "$c" = 7 ] && [ "$s" = 2 ]; then alt=$((alt + 1)); echo "v$v essai $i : LECTURE DIVERGENTE : $(printf '%s' "$out" | head -c 200)" >> "$W/divergentes.txt"
    elif [ "$c" = 18 ]; then r18=$((r18 + 1))
    else autre=$((autre + 1)); echo "v$v essai $i : code $c : $(printf '%s' "$out" | head -c 200)" >> "$W/autres.txt"; fi
  done
  rm -rf "$R" "$R".script.*
  echo "v$v : essais $N ; dossier privé trouvé par le remplaçant avant sa fin : $vu ; lu = contrôlé : $ok ; LECTURES DIVERGENTES (code 7, marque 2) : $alt ; refus 18 : $r18 ; autres codes : $autre" >> "$T"
done
rm -f "$W/ud-v4" "$W/ud-v6"  # données portant le jeton factice
cat "$T"
