#!/bin/bash
# Banc v4, corrections R1 et R3 : joue les fonctions RÉELLES d'identité et d'arrêt du script v4 (lire, st, vivant, moi,
# arreter, identite5), extraites telles quelles entre leurs deux repères, sur de faux processus (prog-arret.sh) et des
# étrangers sans lien (cas du relecteur n1 à n6, repris de son cas-arret.sh, plus n4b et n7). Écrit travail/cas-arret.txt.
# Emploi : cas-arret-v4.sh
set -u
O=$(cd "$(dirname "$0")" && pwd)
ESS=$(dirname "$O")
S=$(dirname "$ESS")/demarrage-machine-essai-3-v4.sh
W=$ESS/travail/cas-arret
[ ! -e "$W" ] || { echo "refus : $W existe"; exit 1; }
mkdir -p "$W"
TB=$ESS/travail/cas-arret.txt
echo "script : $(sha256sum < "$S" | cut -c1-64)" > "$TB"
sed -n "/^# >>> fonctions d'identite et d'arret/,/^# <<< fin des fonctions d'identite et d'arret/p" "$S" > "$W/fonctions.sh"
echo "fonctions extraites : $(grep -c . "$W/fonctions.sh") lignes, sha256 $(sha256sum < "$W/fonctions.sh" | cut -c1-16)…" >> "$TB"
printf '%s\n' 'noter() { echo "$(date -u +%T) $*"; }' 'echouer() { echo "ECHEC code $1 : $2"; exit $1; }' \
  "set -u" ". $W/fonctions.sh" 'P=$(lire $T/pid-essai-3.txt)' '"$@"' 'echo "SUITE : $1 passe sans echec"' > "$W/runner.sh"
vivant_p() { local s a; s=$(cat /proc/$1/stat 2>/dev/null) || return 1; a=(${s##*) }); [ "${a[0]}" != Z ]; }
depart_p() { local s a; s=$(cat /proc/$1/stat 2>/dev/null) && a=(${s##*) }) && echo "${a[19]}"; }
attendre_arbre() { local i; for i in $(seq 1 100); do [ "$(grep -c . "$1/arbre.txt")" -ge "$2" ] && return 0; sleep 0.05; done; }
# cas : nom attendu fonction mode lancement(chef|non-chef|etranger-chef|etranger-non-chef|mort) depart(inconnu|reel|faux)
cas() {
  local nom=$1 att=$2 fn=$3 mode=$4 lanc=$5 dep=$6
  local T=$W/$nom; mkdir -p "$T"; : > "$T/arbre.txt"
  sleep 600 & local ETR=$!; echo "$ETR etranger-sans-lien" >> "$T/arbre.txt"
  local H; H=$(date -u +%Y-%m-%dT%H:%M:%S.%NZ) PP=
  case $lanc in
    chef) setsid /bin/bash "$O/prog-arret.sh" "$mode" "$T" & PP=$! ;;
    non-chef) setsid /bin/bash -c "$O/prog-arret.sh $mode $T; :" & ;;
    etranger-chef) setsid sleep 600 & PP=$!; echo "$PP etranger-qui-reprend-l-identifiant" >> "$T/arbre.txt"
      H=$(date -u -d '-60 seconds' +%Y-%m-%dT%H:%M:%S.%NZ) ;;
    etranger-non-chef) sleep 600 & PP=$!; echo "$PP etranger-qui-reprend-l-identifiant" >> "$T/arbre.txt"
      H=$(date -u -d '-60 seconds' +%Y-%m-%dT%H:%M:%S.%NZ) ;;
    mort) /bin/bash "$O/prog-arret.sh" simple "$T" & PP=$!; wait $PP ;;
  esac
  case $mode in arbre) attendre_arbre "$T" 5 ;; orphelin) attendre_arbre "$T" 4 ;; *) attendre_arbre "$T" 2 ;; esac
  [ -z "$PP" ] && PP=$(sed -n 's/ programme$//p' "$T/arbre.txt" | head -n 1)
  [ $lanc = non-chef ] && sleep 0.3  # le fils orphelin a quitté
  echo "$PP" > "$T/pid-essai-3.txt"; echo "$H" > "$T/heure-lancement-essai-3.txt"
  echo inconnu > "$T/pgid-essai-3.txt"
  case $dep in
    inconnu) echo inconnu > "$T/depart-processus-essai-3.txt" ;;
    reel) depart_p "$PP" > "$T/depart-processus-essai-3.txt" ;;
    faux) echo $(( $(depart_p "$PP") - 1 )) > "$T/depart-processus-essai-3.txt" ;;
  esac
  local out rc
  out=$(T=$T bash "$W/runner.sh" $fn 2>&1); rc=$?
  local l="" p r
  while read -r p r; do vivant_p "$p" && l="$l $p:$r:VIVANT" || l="$l $p:$r:mort"; done < "$T/arbre.txt"
  local ok=ÉCHEC; [ "$rc" = "${att%%;*}" ] && ok=TENU
  local verdict=${att#*;}
  echo "$nom | $fn | attendu code ${att%%;*}, ${verdict} | rendu code $rc | $ok" >> "$TB"
  echo "   $(printf '%s' "$out" | tr '\n' ' ' | cut -c1-260)" >> "$TB"
  echo "   processus :$l" >> "$TB"
  while read -r p r; do vivant_p "$p" && kill -KILL "$p" 2>/dev/null; done < "$T/arbre.txt"
  wait 2>/dev/null
}
cas n1-non-chef-arbre "86;programme et descendants morts, étranger vivant" identite5 arbre non-chef inconnu
cas n2-chef-confirme "0;suite, rien tué" identite5 arbre chef inconnu
cas n3-mort "86;rien tué" identite5 simple mort inconnu
cas n4-orphelin-non-chef "86;tout mort, petit-fils orphelin compris ; étranger vivant" identite5 orphelin non-chef inconnu
cas n4b-orphelin-chef-arret "0;arreter : tout mort, orphelin compris ; étranger vivant" arreter orphelin chef reel
cas n5-identifiant-repris-chef "86;étranger ni adopté ni tué" identite5 simple etranger-chef inconnu
cas n6-identifiant-repris-non-chef "86;étranger ni adopté ni tué" identite5 simple etranger-non-chef inconnu
cas n7-arret-heure-de-depart-autre "0;arreter : rien tué (heure de départ écrite autre)" arreter arbre chef faux
cat "$TB"
