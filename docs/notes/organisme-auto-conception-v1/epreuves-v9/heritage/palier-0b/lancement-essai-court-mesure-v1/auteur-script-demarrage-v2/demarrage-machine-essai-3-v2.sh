#!/bin/bash
# @DONNEES-DE-DEMARRAGE@
# Essai 3, palier 0b : demarrage de la machine, v2
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
for v in BASE SECRET DEPOT_URL APT_GET PY_SYS INTERVALLE ATTENTE OPT_GARDIEN COMMIT REFERENCE; do
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
vivant() {
  local s a
  [ -n "$1" ] && s=$(cat /proc/$1/stat 2>/dev/null) || return 1
  a=(${s##*) })
  [ -z "$2" ] || [ "${a[19]:-}" = "$2" ]
}
lire() { cat "$1" 2>/dev/null; }
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
noter "demarrage v2, H0_PREVU ${H0_PREVU:-absent}, essai :${ESSAI:- aucun}"
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
mkdir $R && git -C $D archive --format=tar $COMMIT | tar -x -C $R || echouer 50 "extraction"
G=$(find $R -name .git | head -n 5)
[ -z "$G" ] || echouer 51 "la racine contient un .git : $G"
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
fait

pas e "pieces de la tenue"
mkdir $BASE/charge $T || echouer 70 "dossiers"
sed -n '/^__CHARGE_DES_PIECES__$/,$p' "$SCRIPT" | sed 1d | base64 -d | tar -xJ --no-same-owner -C $BASE/charge \
  || echouer 70 "charge illisible"
[ $(find $BASE/charge -mindepth 1 | wc -l) = 4 ] || echouer 71 "charge : autre chose que quatre entrees"
while read -r e f; do
  [ -f $BASE/charge/$f ] && [ ! -L $BASE/charge/$f ] && cp $BASE/charge/$f $T/$f || echouer 71 "piece $f absente"
  L=$(sha256sum < $T/$f | cut -c1-64)
  [ $L = $e ] || echouer 72 "empreinte de $f : $L, attendue $e"
done <<< "$PIECES"
chmod 755 $T/*.sh
fait

pas f "departs"
G=$(find $R -name .git | head -n 5)
[ -z "$G" ] || echouer 55 "un .git avant le depart : $G"
H_ARRET=$(date -u -d @$((t + 94 * 3600)) +%FT%TZ) || echouer 80 "heure d'arret"
noter "arret de duree : $H_ARRET ; age de H0_PREVU : $AGE s"
mkdir $VERIF $BASE/sorties || echouer 80 "dossiers"
/bin/bash $T/lancer-essai-3-v4.sh $VERIF $R $PY $S --verifier-seulement
c=$?
[ $c = 0 ] && [ "$(lire $VERIF/code-de-sortie.txt)" = 0 ] || echouer 81 "verification seule : code $c"
GARDE=(--sorties $S --heure-arret-duree $H_ARRET --arret-mesure desarme --seuil-libre-octets 8000000000 $OPT_GARDIEN)
$PY_SYS -I -B $T/gardien-essai-3-v4.py --tenue $VERIF "${GARDE[@]}" --verifier-seulement || echouer 82 "parametres du gardien"
/bin/bash $T/demarrer-essai-3-v4.sh $T $R $PY $S
c=$?
echo $c > $BASE/code-depart-essai-3.txt
[ $c = 0 ] || [ $c = 5 ] || echouer 83 "depart de l'essai : code $c"
[ $c = 0 ] || noter "ATTENTION : depart, code 5 : aucun signal du gardien"
for i in $(seq 1 300); do
  k=$(lire $T/code-de-sortie.txt) && break
  grep -q "part du programme" $T/journal-essai-3.txt && break
  sleep 1
done
[ -z "$k" ] || [ $k = 0 ] || echouer 85 "programme arrete au depart, code $k"
/bin/bash $T/demarrer-gardien-essai-3-v4.sh $T $PY_SYS "${GARDE[@]}" || echouer 84 "gardien refuse : programme SANS gardien"
s=$(lire /proc/$(lire $T/pid-gardien-essai-3.txt)/stat) && a=(${s##*) }) && echo ${a[19]} > $BASE/depart-gardien-essai-3.txt
fait

pas g "boucle de versement"
setsid nohup /bin/bash "$SCRIPT" --boucle-de-versement < /dev/null &
echo $! > $BASE/pid-versement-essai-3.txt
noter "boucle lancee : $!"
fait
exit 0
