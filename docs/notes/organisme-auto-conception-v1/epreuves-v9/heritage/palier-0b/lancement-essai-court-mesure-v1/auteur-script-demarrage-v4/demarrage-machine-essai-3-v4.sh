#!/bin/bash
# Essai 3, palier 0b : demarrage de la machine, v4. Lu par l'amorce (amorce-demarrage-essai-3-v4.sh), qui a extrait
# la charge dans $CHARGE, copie ce script dans un fichier prive et pose H0_PREVU et JETON_DEMARRAGE ; ou joue seul en
# mode --boucle-de-versement. v4 : depart dans une session neuve ; identite et arret par heure de depart ; arret par
# session et par groupe (corrections R1 et R3 de la contre-lecture de la v3).
set -u -o pipefail
COMMIT=d7f949acd9ac92e998e57663d2cc741de93f18c3
REFERENCE=ab90e73b0c824544150f450819a38c7db76dd1cac505942fd66b5375f96591b4
BRANCHE=recuperation/palier-0b-programme-1-essai-3-v1
DEPOT_URL=https://github.com/lciric/controle-ia-travail.git
BASE=/srv/essai-3 SECRET=/root/essai-3-secret APT_GET=apt-get PY_SYS=/usr/bin/python3 INTERVALLE=1800 ATTENTE=20
OPT_GARDIEN= AGE_MAX=7200 PLAFOND=1048576
PIECES="b989db6e2e17772b74ec8ac99a5ed2708bf305d212a5e6825ed210759b7b5865 lancer-essai-3-v4.sh
64b2c0ce03e1e586547580cbed62f8e8c84bbd798c695a588202955809105937 demarrer-essai-3-v4.sh
ba39fe9be5d6fbf760e409d7677ed60662f6118103cb7bd75b93a6786d6246ed gardien-essai-3-v4.py
b333b2eb4bac58c567e0a2efa479ae424dccc6fa9d88fe5a4d95011cb2ce6232 demarrer-gardien-essai-3-v4.sh"
ESSAI=
for v in BASE SECRET DEPOT_URL APT_GET PY_SYS INTERVALLE ATTENTE OPT_GARDIEN COMMIT REFERENCE CHARGE; do
  n=ESSAI_DEMARRAGE_$v
  [ -z "${!n+x}" ] || ESSAI="$ESSAI $v"
done
if [ -n "$ESSAI" ]; then
  [ "${ESSAI_DEMARRAGE_BANC:-}" = oui ] || { echo "refus : portes d'essai sans banc :$ESSAI"; exit 19; }
  for v in $ESSAI; do n=ESSAI_DEMARRAGE_$v; printf -v $v %s "${!n}"; done
fi
SCRIPT=$(readlink -f "${BASH_SOURCE[0]}")
J=$BASE/journal-demarrage-essai-3.txt T=$BASE/tenue VERIF=$BASE/tenue-verification R=$BASE/racine D=$BASE/depot.git
V=$BASE/versement S=$BASE/sorties/etapes-3-a-6-essai-3 PY=$BASE/venv/bin/python AS=$BASE/assistant-jeton.sh
PROTO=${DEPOT_URL%%:*} HOTE=${DEPOT_URL#*://} HOTE=${HOTE%%/*}
export GIT_TERMINAL_PROMPT=0 GIT_CONFIG_NOSYSTEM=1 GIT_CONFIG_GLOBAL=/dev/null HOME=${HOME:-/root}
# environnement des departs : sans les reglages de git et d'apt du script (le programme n'en herite pas)
SANS=(env -u DEBIAN_FRONTEND -u GIT_TERMINAL_PROMPT -u GIT_CONFIG_NOSYSTEM -u GIT_CONFIG_GLOBAL)
PAS=0
h() { date -u +%FT%TZ; }
noter() { echo "$(h) $*"; }
pas() { PAS=$1; noter "pas ($1) : debut : $2"; }
fait() { noter "pas ($PAS) : fait"; }
echouer() {
  noter "ECHEC du pas ($PAS), code $1 : $2"
  echo "code $1, pas ($PAS) : $2" > $BASE/echec-demarrage-essai-3.txt
  [ -d $V/.git ] && verser "echec au pas ($PAS), code $1"
  exit $1
}
essayer() {
  local k
  for k in 1 2 3; do
    "$@" && return 0
    noter "tentative $k de $1 echouee"
    [ $k = 3 ] || sleep $ATTENTE
  done
  return 1
}
# >>> fonctions d'identite et d'arret (v4 ; extraites telles quelles par le banc entre ces deux reperes)
lire() { cat "$1" 2>/dev/null; }
# st : etat de /proc/PID/stat dans a (a[0] etat, a[1] parent, a[2] groupe, a[3] session, a[19] heure de depart)
st() { local s; s=$(cat /proc/$1/stat 2>/dev/null) || return 1; a=(${s##*) }); [ ${a[0]} != Z ]; }
vivant() { [ -n "$1" ] && st $1 && { [ -z "$2" ] || [ ${a[19]} = $2 ]; }; }
moi() {  # $1 est-il le programme lance ? heure de depart egale a celle ecrite par le depart v4 ; si celui-ci a ecrit
         # « inconnu » (code 5) : heure de depart dans [heure de lancement ecrite - 5 s, + 2 s] (horloge de demarrage a 1 s)
  local d h b k
  [[ "${1:-}" =~ ^[0-9]+$ ]] && [ $1 -gt 1 ] && st $1 || return 1
  d=$(lire $T/depart-processus-essai-3.txt)
  if [[ "$d" =~ ^[0-9]+$ ]]; then [ ${a[19]} = $d ]; return; fi
  h=$(date -d "$(lire $T/heure-lancement-essai-3.txt)" +%s%3N) && b=$(sed -n 's/^btime //p' /proc/stat) \
    && k=$(getconf CLK_TCK) || return 1
  k=$(( b * 1000 + a[19] * 1000 / k ))
  st $1 && [ $k -ge $((h - 5000)) ] && [ $k -le $((h + 2000)) ]
}
arreter() {  # programme lance, ses descendants, et les membres de sa session et de son groupe ; jamais un etranger
  local p l x s m q i e n f
  p=$(lire $T/pid-essai-3.txt)
  [[ "$p" =~ ^[0-9]+$ ]] && [ $p -gt 1 ] || { noter "arret : identifiant ecrit illisible ($p) : rien n'est arrete"; return 0; }
  st $$; m=${a[3]}
  if st $p; then
    moi $p || { noter "arret : $p n'est pas le programme lance (heure de depart autre) : rien n'est arrete"; return 0; }
    s=${a[3]}
  else
    s=$p  # programme mort : sa session et son groupe, s'il en etait le chef, ne portent plus que ses restes
  fi
  [ "$s" = "$m" ] && s=  # jamais notre propre session
  l=$p n=1
  while [ $n = 1 ]; do
    n=0
    for f in /proc/[0-9]*; do
      x=${f#/proc/}
      { [ $x = $$ ] || [ $x = $BASHPID ]; } && continue
      st $x || continue
      { [[ " $l " = *" ${a[1]} "* ]] || [ "${a[3]}" = "$s" ] || [ ${a[2]} = $p ]; } && [[ " $l " != *" $x "* ]] && l="$l $x" n=1
    done
  done
  e=; for x in $l; do st $x && e="$e $x:${a[19]}"; done
  for x in $e; do kill -TERM ${x%:*}; done
  for i in $(seq 1 30); do
    q=; for x in $e; do st ${x%:*} && [ ${a[19]} = ${x#*:} ] && q="$q $x"; done
    [ -z "$q" ] && break
    sleep 1
  done
  for x in $q; do st ${x%:*} && [ ${a[19]} = ${x#*:} ] && kill -KILL ${x%:*}; done
  noter "programme arrete (identifiant:heure de depart) :${e:- aucun} ; forces :${q:- aucun}"
}
identite5() {  # code 5 du depart : identite lue sur le programme, refusee si l'heure de depart differe
  moi "$P" || echouer 86 "depart code 5 : $P n'est pas le programme lance (absent, ou heure de depart autre) : rien n'est arrete"
  [ ${a[2]} = $P ] && [ ${a[3]} = $P ] || { arreter; echouer 86 "depart code 5 : programme non chef de sa session et de son groupe"; }
  cp $T/pgid-essai-3.txt $T/pgid-ecrit-par-le-depart.txt && cp $T/depart-processus-essai-3.txt $T/depart-ecrit-par-le-depart.txt
  echo $P > $T/pgid-essai-3.txt && echo ${a[19]} > $T/depart-processus-essai-3.txt
  noter "ATTENTION : depart, code 5 ; identite lue sur le programme : session et groupe $P, depart ${a[19]}"
}
# <<< fin des fonctions d'identite et d'arret
etat() {
  local p d gp gd
  p=$(lire $T/pid-essai-3.txt); d=$(lire $T/depart-processus-essai-3.txt); [ "$d" = inconnu ] && d=
  gp=$(lire $T/pid-gardien-essai-3.txt); gd=$(lire $BASE/depart-gardien-essai-3.txt)
  echo "heure : $(h)"
  echo "versement : $1"
  echo "n : $(find $S/etape-4/couche-mecanique/bras-1-a-3 -mindepth 3 -maxdepth 3 -type d 2>/dev/null | wc -l)"
  echo "octets libres : $(df -B1 --output=avail $BASE | tail -n 1)"
  echo "programme : ${p:-aucun} $(vivant "$p" "$d" && echo vivant || echo absent)"
  echo "gardien : ${gp:-aucun} $(vivant "$gp" "$gd" && echo vivant || echo absent)"
  echo "code du depart : $(lire $BASE/code-depart-essai-3.txt)"
  echo "code de sortie : $(lire $T/code-de-sortie.txt)"
  echo "echec : $(lire $BASE/echec-demarrage-essai-3.txt)"
}
verser() {
  local d=$V/essai-3 f
  mkdir -p $d/tenue
  cp -f $J $d/
  for f in journal-de-tenue-essai-3.txt arret-gardien.txt; do
    [ -f $T/$f ] && cp -f $T/$f $d/tenue/
  done
  for f in journal-essai-3.txt sortie-gardien-essai-3.txt; do
    [ -f $T/$f ] && tail -c $PLAFOND $T/$f > $d/tenue/$f
  done
  for f in $T/inventaire-etape-*-essai-3.txt.sha256; do
    [ -f $f ] && cp -f ${f%.sha256} $f $d/tenue/
  done
  [ -f $BASE/fin-essai-3.txt ] && cp -f $BASE/fin-essai-3.txt $d/
  etat "$1" > $d/etat-essai-3.txt
  if git -C $V add -A . && git -C $V commit -q -m "$1" && essayer git -C $V push -q origin HEAD:refs/heads/$BRANCHE; then
    noter "versement $1 : pousse"
  else
    noter "ECHEC du versement $1"
  fi
}
boucle() {
  local n=0 gp gd k
  noter "boucle : debut ($BASHPID)"
  while :; do
    n=$((n + 1))
    gp=$(lire $T/pid-gardien-essai-3.txt); gd=$(lire $BASE/depart-gardien-essai-3.txt)
    if ! vivant "$gp" "$gd"; then
      [ -f $T/code-de-sortie.txt ] || echo "code 87 : lanceur arrete sans ecrire son code" > $BASE/echec-demarrage-essai-3.txt
      verser "versement $n : dernier"
      echo "fin : gardien absent le $(h), $n versements" > $BASE/fin-essai-3.txt
      verser "fichier fin"
      noter "boucle de versement : fin"
      return 0
    fi
    verser "versement $n"
    for ((k = 0; k < INTERVALLE; k += 60)); do
      vivant "$gp" "$gd" || break
      sleep $((INTERVALLE - k < 60 ? INTERVALLE - k : 60))
    done
  done
}

if [ "${1:-}" = --boucle-de-versement ]; then
  unset JETON_DEMARRAGE
  exec >> $J 2>&1
  boucle
  exit
fi
JETON=${JETON_DEMARRAGE:-}
unset JETON_DEMARRAGE
if [ -e $BASE ] || [ -L $BASE ]; then
  [ -d $BASE ] && echo "$(h) demarrage refuse : $BASE present" >> $J
  exit 20
fi
mkdir -p $BASE || exit 20
exec >> $J 2>&1
noter "demarrage v3, H0_PREVU ${H0_PREVU:-absent}, essai :${ESSAI:- aucun}"
[[ "${H0_PREVU:-}" =~ ^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z$ ]] && t=$(date -d $H0_PREVU +%s) \
  || echouer 21 "H0_PREVU absent ou mal forme"
AGE=$(( $(date +%s) - t ))
[ $AGE -le $AGE_MAX ] && [ $AGE -ge -600 ] || echouer 21 "H0_PREVU vieux de $AGE s, hors de -600 a $AGE_MAX"
[[ "$JETON" =~ ^[A-Za-z0-9_-]{20,100}$ ]] || echouer 22 "jeton absent ou mal forme"
umask 077
mkdir -m 700 -p $SECRET && printf '%s\n' "$JETON" > $SECRET/jeton || echouer 23 "fichier du jeton"
unset JETON
umask 022
[ "$(stat -c %a $SECRET/jeton)" = 600 ] || echouer 23 "droits du fichier du jeton autres que 600"
printf '%s\n' '#!/bin/bash' '[ "${1:-}" = get ] || exit 0' 'p= q=' \
  'while IFS= read -r l && [ -n "$l" ]; do case $l in protocol=*) p=${l#*=} ;; host=*) q=${l#*=} ;; esac; done' \
  "[ \"\$p\" = $PROTO ] && [ \"\$q\" = $HOTE ] || exit 0" "IFS= read -r j < $SECRET/jeton || exit 1" \
  'printf "username=x-access-token\npassword=%s\n" "$j"' > $AS && chmod 700 $AS || echouer 24 "assistant"

pas a "git et Python du systeme"
export DEBIAN_FRONTEND=noninteractive
essayer $APT_GET -o DPkg::Lock::Timeout=600 update || echouer 30 "liste des paquets"
essayer $APT_GET -o DPkg::Lock::Timeout=600 install -y --no-install-recommends git python3 python3-venv ca-certificates \
  xz-utils || echouer 31 "paquets"
command -v git && [ -x $PY_SYS ] || echouer 32 "git ou $PY_SYS absent"
fait
g() { git -C $V config "$@"; }
git init -q $V && g user.name "machine essai 3" && g user.email essai-3@machine.invalid && g credential.helper $AS \
  && g remote.origin.url $DEPOT_URL && printf '%s\n' '#!/bin/bash' 'while read -r l ls r rs; do' \
  "  [ \"\$r\" = refs/heads/$BRANCHE ] && [ -n \"\${ls//0/}\" ] || { echo \"garde : refus vers \$r\"; exit 1; }" \
  '  [ -z "${rs//0/}" ] || git merge-base --is-ancestor $rs $ls || { echo "garde : refus, non descendante"; exit 1; }' \
  'done' > $V/.git/hooks/pre-push && chmod 755 $V/.git/hooks/pre-push || echouer 25 "preparation du versement"

pas b "clonage, profondeur 1"
git init -q --bare $D && git -C $D config credential.helper $AS && git -C $D config remote.origin.url $DEPOT_URL \
  && git -C $D config remote.origin.pushurl aucune-poussee-depuis-ce-depot || echouer 40 "depot local"
essayer git -C $D fetch -q --depth 1 origin $COMMIT || echouer 41 "clonage impossible"
[ "$(git -C $D rev-parse --verify -q "$COMMIT^{commit}")" = $COMMIT ] || echouer 42 "commit absent du clone"
fait

pas c "racine par git archive"
gitr() { G=$(find $R -name .git | head -n 5); [ -z "$G" ] || echouer $1 "la racine contient un .git : $G"; }
mkdir $R && git -C $D archive --format=tar $COMMIT | tar -x -C $R || echouer 50 "extraction"
gitr 51
(cd $R && LC_ALL=C find . -type f ! -path ./COMMIT-DE-LA-COPIE.txt ! -path ./EMPREINTES-DE-LA-COPIE.txt -print0 \
  | LC_ALL=C sort -z | xargs -0 sha256sum) > $BASE/liste-de-la-copie.txt || echouer 52 "liste des empreintes"
L=$(sha256sum < $BASE/liste-de-la-copie.txt | cut -c1-64)
[ $L = $REFERENCE ] || echouer 53 "liste de la copie $L, attendue $REFERENCE"
cp $BASE/liste-de-la-copie.txt $R/EMPREINTES-DE-LA-COPIE.txt && echo $COMMIT > $R/COMMIT-DE-LA-COPIE.txt \
  || echouer 54 "fichiers de la copie"
fait

pas d "environnement Python"
$PY_SYS -m venv $BASE/venv || echouer 60 "environnement"
(cd $BASE && essayer $BASE/venv/bin/pip install --no-input --disable-pip-version-check -r $R/requirements-cpu.txt) \
  || echouer 61 "paquets Python"
[ -f $PY ] && [ -x $PY ] || echouer 62 "interpreteur absent"
$BASE/venv/bin/pip freeze
fait

pas e "pieces de la tenue (charge extraite par l'amorce dans ${CHARGE:-?})"
[ -n "${CHARGE:-}" ] && [ -d "$CHARGE" ] && mkdir $T || echouer 70 "charge absente ou dossier de tenue"
[ $(find $CHARGE -mindepth 1 | wc -l) = 5 ] || echouer 71 "charge : autre chose que cinq entrees (script et quatre pieces)"
while read -r e f; do
  [ -f $CHARGE/$f ] && [ ! -L $CHARGE/$f ] && cp $CHARGE/$f $T/$f || echouer 71 "piece $f absente"
  L=$(sha256sum < $T/$f | cut -c1-64)
  [ $L = $e ] || echouer 72 "empreinte de $f : $L, attendue $e"
done <<< "$PIECES"
chmod 755 $T/*.sh
fait

pas f "departs"
gitr 55
H_ARRET=$(date -u -d @$((t + 94 * 3600)) +%FT%TZ) || echouer 80 "heure d'arret"
mkdir $VERIF $BASE/sorties || echouer 80 "dossiers"
/bin/bash $T/lancer-essai-3-v4.sh $VERIF $R $PY $S --verifier-seulement
c=$?
[ $c = 0 ] && [ "$(lire $VERIF/code-de-sortie.txt)" = 0 ] || echouer 81 "verification seule : code $c"
GARDE=(--sorties $S --heure-arret-duree $H_ARRET --arret-mesure desarme --seuil-libre-octets 8000000000 $OPT_GARDIEN)
$PY_SYS -I -B $T/gardien-essai-3-v4.py --tenue $VERIF "${GARDE[@]}" --verifier-seulement || echouer 82 "parametres du gardien"
gitr 56
# R1 : le depart joue dans une session neuve (setsid -w, attendu) : le programme et ses restes n'y croisent jamais la
# session de ce script ; le lanceur y prend en plus sa propre session (setsid du depart v4)
"${SANS[@]}" setsid -w /bin/bash $T/demarrer-essai-3-v4.sh $T $R $PY $S
c=$?
echo $c > $BASE/code-depart-essai-3.txt
[ $c = 0 ] || [ $c = 5 ] || echouer 83 "depart de l'essai : code $c"
P=$(lire $T/pid-essai-3.txt)
for i in $(seq 1 300); do
  k=$(lire $T/code-de-sortie.txt) && break
  st "$P" || { arreter; echouer 87 "lanceur arrete sans ecrire son code"; }
  grep -q "part du programme" $T/journal-essai-3.txt && break
  sleep 1
done
[ -z "$k" ] || [ $k = 0 ] || { arreter; echouer 85 "programme arrete au depart, code $k"; }
[ $c = 5 ] && identite5
"${SANS[@]}" /bin/bash $T/demarrer-gardien-essai-3-v4.sh $T $PY_SYS "${GARDE[@]}" \
  || { arreter; echouer 84 "gardien refuse : programme arrete avant le versement de l'echec"; }
s=$(lire /proc/$(lire $T/pid-gardien-essai-3.txt)/stat) && a=(${s##*) }) && echo ${a[19]} > $BASE/depart-gardien-essai-3.txt
fait

pas g "boucle de versement"
setsid nohup /bin/bash "$SCRIPT" --boucle-de-versement < /dev/null &
echo $! > $BASE/pid-versement-essai-3.txt
fait
exit 0
