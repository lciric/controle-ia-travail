#!/bin/bash
# Banc v5, corrections R1 et R3 : joue les fonctions RÉELLES d'identité et d'arrêt du script v5 (lire, st, vivant, membre,
# reference, moi, arreter, identite5), extraites telles quelles entre leurs deux repères, sur de faux processus
# (prog-arret.sh) et des étrangers sans lien. Chaque cas est joué avec un groupe de contrôle cgroup v2 propre au cas
# (« cg ») et en repli sans groupe (« sans »). Écrit travail/cas-arret.txt.
# Fonctions jouées : ref5 = reference puis identite5 (code 5 du départ) ; ref0 = reference au code 0, 86 si refusée ;
# arreter = arrêt, la référence étant écrite par le banc (reel ou faux).
# Emploi : cas-arret-v5.sh RACINE_CGROUP2
set -u
O=$(cd "$(dirname "$0")" && pwd)
ESS=$(dirname "$O")
S=$(dirname "$ESS")/demarrage-machine-essai-3-v5.sh
RC=$1
W=$ESS/travail/cas-arret
[ ! -e "$W" ] || { echo "refus : $W existe"; exit 1; }
mkdir -p "$W"
TB=$ESS/travail/cas-arret.txt
echo "script : $(sha256sum < "$S" | cut -c1-64)" > "$TB"
sed -n "/^# >>> fonctions d'identite et d'arret/,/^# <<< fin des fonctions d'identite et d'arret/p" "$S" > "$W/fonctions.sh"
echo "fonctions extraites : $(grep -c . "$W/fonctions.sh") lignes, sha256 $(sha256sum < "$W/fonctions.sh" | cut -c1-16)…" >> "$TB"
printf '%s\n' 'noter() { echo "$(date -u +%T) $*"; }' 'echouer() { echo "ECHEC code $1 : $2"; exit $1; }' \
  "set -u" ". $W/fonctions.sh" 'P=$(lire $T/pid-essai-3.txt) REF_F=$BASE/depart-lu-par-le-script-essai-3.txt' \
  'ref5() { reference; identite5; }' \
  'ref0() { reference || echouer 86 "reference refusee : rien n'"'"'est arrete"; echo "reference : $(lire $REF_F)"; }' \
  '"$@"' 'echo "SUITE : $1 passe sans echec"' > "$W/runner.sh"
vivant_p() { local s a; s=$(cat /proc/$1/stat 2>/dev/null) || return 1; a=(${s##*) }); [ "${a[0]}" != Z ]; }
depart_p() { local s a; s=$(cat /proc/$1/stat 2>/dev/null) && a=(${s##*) }) && echo "${a[19]}"; }
attendre_arbre() { local i; for i in $(seq 1 100); do [ "$(grep -c . "$1/arbre.txt")" -ge "$2" ] && return 0; sleep 0.05; done; }
# cas : nom groupe(cg|sans) attendu fonction mode(arbre|orphelin|evade|simple) lancement(chef|non-chef|etranger-chef|
#       etranger-non-chef|mort) depart(inconnu|reel|faux) ; pour arreter, depart = référence écrite par le banc
cas() {
  local nom=$1-$2 grp=$2 att=$3 fn=$4 mode=$5 lanc=$6 dep=$7
  local T=$W/$nom G=; mkdir -p "$T"; : > "$T/arbre.txt"
  if [ $grp = cg ]; then G=$RC/essai-3-banc-v5-arret-$nom; mkdir "$G" || { echo "$nom : groupe impossible" >> "$TB"; return; }; fi
  sleep 600 & local ETR=$!; echo "$ETR etranger-sans-lien" >> "$T/arbre.txt"
  local PP=
  case $lanc in
    chef) ( [ -z "$G" ] || echo $BASHPID > "$G/cgroup.procs"; exec setsid /bin/bash "$O/prog-arret.sh" "$mode" "$T" ) & PP=$! ;;
    non-chef) ( [ -z "$G" ] || echo $BASHPID > "$G/cgroup.procs"; exec setsid /bin/bash -c "$O/prog-arret.sh $mode $T; :" ) & ;;
    etranger-chef) setsid sleep 600 & PP=$!; echo "$PP etranger-qui-reprend-l-identifiant" >> "$T/arbre.txt" ;;
    etranger-non-chef) sleep 600 & PP=$!; echo "$PP etranger-qui-reprend-l-identifiant" >> "$T/arbre.txt" ;;
    mort) ( [ -z "$G" ] || echo $BASHPID > "$G/cgroup.procs"; exec /bin/bash "$O/prog-arret.sh" simple "$T" ) & PP=$!; wait $PP ;;
  esac
  case $mode in arbre) attendre_arbre "$T" 5 ;; orphelin) attendre_arbre "$T" 4 ;; evade) attendre_arbre "$T" 4 ;; *) attendre_arbre "$T" 2 ;; esac
  [ -z "$PP" ] && PP=$(sed -n 's/ programme$//p' "$T/arbre.txt" | head -n 1)
  [ $lanc = non-chef ] && sleep 0.3  # le fils orphelin a quitté
  [ $mode = evade ] && sleep 0.3     # le père du descendant en session neuve est mort
  echo "$PP" > "$T/pid-essai-3.txt"; echo inconnu > "$T/pgid-essai-3.txt"
  local c=5; [ $fn = ref0 ] && c=0
  case $fn:$dep in
    ref*:inconnu) echo inconnu > "$T/depart-processus-essai-3.txt" ;;
    ref*:reel) depart_p "$PP" > "$T/depart-processus-essai-3.txt" ;;
    ref*:faux) echo $(( $(depart_p "$PP") + 1 )) > "$T/depart-processus-essai-3.txt" ;;
    arreter:reel) depart_p "$PP" > "$T/depart-lu-par-le-script-essai-3.txt" ;;
    arreter:faux) echo $(( $(depart_p "$PP") + 1 )) > "$T/depart-lu-par-le-script-essai-3.txt" ;;
  esac
  local out rc
  out=$(T=$T BASE=$T CGROUPE=$G c=$c bash "$W/runner.sh" $fn 2>&1); rc=$?
  local l="" p r
  while read -r p r; do vivant_p "$p" && l="$l $p:$r:VIVANT" || l="$l $p:$r:mort"; done < "$T/arbre.txt"
  local ok=ÉCHEC; [ "$rc" = "${att%%;*}" ] && ok=TENU
  echo "$nom | $fn, code du départ $c | attendu code ${att%%;*}, ${att#*;} | rendu code $rc | $ok" >> "$TB"
  echo "   $(printf '%s' "$out" | tr '\n' ' ' | cut -c1-300)" >> "$TB"
  echo "   processus :$l" >> "$TB"
  [ -n "$G" ] && echo "   membres du groupe après la fonction : [$(tr '\n' ' ' < "$G/cgroup.procs")]" >> "$TB"
  # nettoyage par identifiant : processus de l'arbre, puis membres du groupe, puis retrait du groupe
  while read -r p r; do vivant_p "$p" && kill -KILL "$p" 2>/dev/null; done < "$T/arbre.txt"
  if [ -n "$G" ]; then
    for p in $(cat "$G/cgroup.procs"); do kill -KILL "$p" 2>/dev/null; done
    for i in $(seq 1 50); do [ -z "$(cat "$G/cgroup.procs")" ] && break; sleep 0.1; done
    rmdir "$G"
  fi
  wait 2>/dev/null
}
for g in cg sans; do
  if [ $g = cg ]; then a1="86;programme et descendants morts, étranger vivant"; a2="0;suite, rien tué"; a4="86;tout mort, petit-fils orphelin compris ; étranger vivant"
    a8="0;arreter : tout mort, descendant en session neuve compris ; étranger vivant"
  else a1="86;référence refusée en repli au code 5 : rien tué"; a2="86;référence refusée en repli au code 5 : rien tué"; a4="86;référence refusée en repli au code 5 : rien tué"
    a8="0;arreter en repli : arbre, session et groupe morts ; descendant en session neuve VIVANT (limite du repli)"; fi
  cas n1-non-chef-arbre $g "$a1" ref5 arbre non-chef inconnu
  cas n2-chef-code-5 $g "$a2" ref5 arbre chef inconnu
  cas n2b-chef-code-0 $g "0;référence prise, rien tué" ref0 arbre chef reel
  cas n3-mort $g "86;rien tué" ref5 simple mort inconnu
  cas n4-orphelin-non-chef $g "$a4" ref5 orphelin non-chef inconnu
  cas n4b-orphelin-chef-arret $g "0;arreter : tout mort, orphelin compris ; étranger vivant" arreter orphelin chef reel
  cas n5-identifiant-repris-chef $g "86;étranger ni adopté ni tué" ref5 simple etranger-chef inconnu
  cas n6-identifiant-repris-non-chef $g "86;étranger ni adopté ni tué" ref5 simple etranger-non-chef inconnu
  cas n7-arret-reference-autre $g "0;arreter : rien tué (référence autre d'un top)" arreter arbre chef faux
  cas n8-descendant-session-neuve-pere-mort $g "$a8" arreter evade chef reel
  cas n9-code-0-heure-du-depart-autre $g "86;référence refusée (heure écrite par le départ autre d'un top) : rien tué" ref0 arbre chef faux
done
cat "$TB"
