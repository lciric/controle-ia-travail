#!/bin/bash
# Essai 3, palier 0b : demarrage de la machine, v6. Execute par l'amorce (amorce-demarrage-essai-3-v6.sh) depuis le
# texte qu'elle a lu une fois en memoire et hache (TEXTE : ce script, reduit par le fabricant de ses lignes de commentaire
# entieres et de ses lignes vides), apres avoir pose H0_PREVU, JETON_DEMARRAGE et CHARGE ; ou, en mode
# --boucle-de-versement, par bash -c sur ce meme texte (aucun fichier relu).
# v5 : programme dans un groupe de controle cgroup v2 propre, arrete par ce groupe ; heure de depart de reference lue dans
# /proc par ce script, sans tolerance.
# v6 : groupe de controle exige (sans lui, ou s'il refuse l'inscription, code 88 et rien n'est lance ; plus de repli) ;
# au code 86, cgroup.kill du groupe puis controle qu'il est vide ; a l'heure d'arret + 60 s, cgroup.kill en filet par la
# boucle de versement, groupe vide controle et ecrit dans l'etat.
set -u -o pipefail
COMMIT=d7f949acd9ac92e998e57663d2cc741de93f18c3
REFERENCE=ab90e73b0c824544150f450819a38c7db76dd1cac505942fd66b5375f96591b4
BRANCHE=recuperation/palier-0b-programme-1-essai-3-v1
DEPOT_URL=https://github.com/lciric/controle-ia-travail.git
BASE=/srv/essai-3 SECRET=/root/essai-3-secret APT_GET=apt-get PY_SYS=/usr/bin/python3 INTERVALLE=1800 ATTENTE=20
OPT_GARDIEN= AGE_MAX=7200 PLAFOND=1048576 H_ARRET=
PIECES="b989db6e2e17772b74ec8ac99a5ed2708bf305d212a5e6825ed210759b7b5865 lancer-essai-3-v4.sh
64b2c0ce03e1e586547580cbed62f8e8c84bbd798c695a588202955809105937 demarrer-essai-3-v4.sh
ba39fe9be5d6fbf760e409d7677ed60662f6118103cb7bd75b93a6786d6246ed gardien-essai-3-v4.py
b333b2eb4bac58c567e0a2efa479ae424dccc6fa9d88fe5a4d95011cb2ce6232 demarrer-gardien-essai-3-v4.sh"
CGROUPE=  # groupe de controle du programme : sous le premier cgroup v2 monte
while read -r x m y x; do [ "$y" = cgroup2 ] && { CGROUPE=$m/essai-3-programme; break; }; done < /proc/self/mounts
ESSAI=
for v in BASE SECRET DEPOT_URL APT_GET PY_SYS INTERVALLE ATTENTE OPT_GARDIEN COMMIT REFERENCE CHARGE CGROUPE H_ARRET; do
  n=ESSAI_DEMARRAGE_$v
  [ -z "${!n+x}" ] || ESSAI="$ESSAI $v"
done
if [ -n "$ESSAI" ]; then
  [ "${ESSAI_DEMARRAGE_BANC:-}" = oui ] || { echo "refus : portes sans banc :$ESSAI"; exit 19; }
  for v in $ESSAI; do n=ESSAI_DEMARRAGE_$v; printf -v $v %s "${!n}"; done
fi
J=$BASE/journal-demarrage-essai-3.txt T=$BASE/tenue VERIF=$BASE/tenue-verification R=$BASE/racine D=$BASE/depot.git
V=$BASE/versement S=$BASE/sorties/etapes-3-a-6-essai-3 PY=$BASE/venv/bin/python AS=$BASE/assistant-jeton.sh
PROTO=${DEPOT_URL%%:*} HOTE=${DEPOT_URL#*://} HOTE=${HOTE%%/*}
REF_F=$BASE/depart-lu-par-le-script-essai-3.txt GC_F=$BASE/groupe-de-controle-essai-3.txt
HA_F=$BASE/heure-arret-essai-3.txt FILET_F=$BASE/filet-essai-3.txt
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
    noter "tentative $k de $1"
    [ $k = 3 ] || sleep $ATTENTE
  done
  return 1
}
# >>> fonctions d'identite et d'arret (v6 ; extraites telles quelles par le banc entre ces deux reperes)
lire() { cat "$1" 2>/dev/null; }
# st : /proc/PID/stat lu par la commande interne read (sans fourche) dans a (a[0] etat, a[1] parent, a[2] groupe,
# a[3] session, a[19] heure de depart) ; faux si l'identifiant est mal forme, le processus absent ou zombie
st() { local s; [[ "${1:-}" =~ ^[0-9]+$ ]] && { read -r s < /proc/$1/stat; } 2>/dev/null || return 1; a=(${s##*) }); [ ${a[0]} != Z ]; }
vivant() { [ -n "$1" ] && st $1 && { [ -z "$2" ] || [ ${a[19]} = $2 ]; }; }
membre() { [ -n "$CGROUPE" ] && grep -qx "$1" "$CGROUPE/cgroup.procs" 2>/dev/null; }
reference() {  # R3 : heure de depart de P lue dans /proc par ce script, sans tolerance, gardee dans REF_F ; acceptee
  # seulement si P est membre du groupe de controle du programme (lu avant et apres, meme heure) ; au code 0, l'heure
  # ecrite par le depart doit etre la meme, au top pres
  local x d
  [[ "${P:-}" =~ ^[0-9]+$ ]] && [ $P -gt 1 ] && st $P || return 1
  x=${a[19]} d=$(lire $T/depart-processus-essai-3.txt)
  if [ "$c" = 0 ]; then [ "$d" = $x ] || return 1; fi
  membre $P && st $P && [ ${a[19]} = $x ] || return 1
  echo $x > $REF_F
}
moi() {  # $1 est-il le programme lance ? heure de depart egale a la reference prise par ce script, sans tolerance
  local d
  st "${1:-}" && [ $1 -gt 1 ] || return 1
  d=$(lire $REF_F)
  [[ "$d" =~ ^[0-9]+$ ]] && [ ${a[19]} = $d ]
}
vider() {  # cgroup.kill du groupe du programme (ses seuls membres), puis controle qu'il est vide (10 s au plus)
  local i
  [ -n "$CGROUPE" ] && [ -f "$CGROUPE/cgroup.kill" ] || { noter "groupe absent"; return 1; }
  echo 1 > $CGROUPE/cgroup.kill || noter "cgroup.kill refuse"
  for i in $(seq 1 100); do
    [ -z "$(lire $CGROUPE/cgroup.procs)" ] && { noter "groupe vide"; return 0; }
    sleep 0.1
  done
  noter "groupe NON vide : [$(lire $CGROUPE/cgroup.procs | tr '\n' ' ')]"
  return 1
}
echouer86() {  # code 86 : le groupe du programme est arrete par cgroup.kill et controle vide ; aucun etranger n'est vise
  local r=vide
  vider || r="NON vide"
  echouer 86 "$1 ; cgroup.kill : groupe $r"
}
filet() {  # heure d'arret + 60 s : cgroup.kill en filet, controle du groupe vide, ecrit dans l'etat
  local r=vide
  vider || r="NON vide"
  echo "filet $(h) : cgroup.kill ; groupe $r" > $FILET_F
}
arreter() {  # programme lance : membres de son groupe de controle, descendants, membres de sa session et de son groupe ;
  # jamais un etranger : si P vit sans etre le programme lance, rien n'est arrete, et la comparaison est refaite avant
  # tout arret force
  local p l x s m q i e n f g
  p=$(lire $T/pid-essai-3.txt); [[ "$p" =~ ^[0-9]+$ ]] && [ $p -gt 1 ] || p=
  g=; [ -n "$CGROUPE" ] && [ -f "$CGROUPE/cgroup.procs" ] && g=$CGROUPE
  [ -n "$p$g" ] || { noter "arret : rien a viser"; return 0; }
  st $$; m=${a[3]} s=
  if [ -n "$p" ] && st $p; then
    moi $p || { noter "arret : $p autre : rien"; return 0; }
    s=${a[3]}
  else
    s=$p  # programme mort : sa session et son groupe, s'il en etait le chef, ne portent plus que ses restes
  fi
  [ "$s" = "$m" ] && s=  # jamais notre propre session
  l=$p n=1
  if [ -n "$g" ]; then for x in $(lire $g/cgroup.procs); do [[ " $l " = *" $x "* ]] || l="$l $x"; done; fi
  while [ $n = 1 ]; do
    n=0
    for f in /proc/[0-9]*; do
      x=${f#/proc/}
      { [ $x = $$ ] || [ $x = $BASHPID ]; } && continue
      st $x || continue
      { [[ " $l " = *" ${a[1]} "* ]] || { [ -n "$s" ] && [ ${a[3]} = "$s" ]; } || { [ -n "$p" ] && [ ${a[2]} = "$p" ]; }; } \
        && [[ " $l " != *" $x "* ]] && l="$l $x" n=1
    done
  done
  e= f=; for x in $l; do st $x && e="$e $x:${a[19]}"; done
  for x in $e; do kill -TERM ${x%:*} 2>/dev/null; done
  for i in $(seq 1 30); do
    if [ -n "$g" ]; then
      for x in $(lire $g/cgroup.procs); do [[ "$e " = *" $x:"* ]] || { st $x && e="$e $x:${a[19]}" && kill -TERM $x 2>/dev/null; }; done
    fi
    q=; for x in $e; do st ${x%:*} && [ ${a[19]} = ${x#*:} ] && q="$q $x"; done
    [ -z "$q" ] && { [ -z "$g" ] || [ -z "$(lire $g/cgroup.procs)" ]; } && break
    sleep 1
  done
  if [ -n "$p" ] && st $p && ! moi $p; then noter "arret : $p autre : rien de force"; return 0; fi
  for x in $q; do st ${x%:*} && [ ${a[19]} = ${x#*:} ] && kill -KILL ${x%:*}; done
  if [ -n "$g" ] && [ -n "$(lire $g/cgroup.procs)" ]; then
    if echo 1 > $g/cgroup.kill; then f=" ; cgroup.kill"; else f=" ; cgroup.kill refuse"; fi
  fi
  for i in $(seq 1 50); do { [ -z "$g" ] || [ -z "$(lire $g/cgroup.procs)" ]; } && break; sleep 0.1; done
  noter "arrete :${e:- aucun} ; forces :${q:- aucun}$f ; groupe ${g:-aucun}${g:+ : [$(lire $g/cgroup.procs | tr '\n' ' ')]}"
}
identite5() {  # code 5 du depart : identite = reference prise par ce script ; 86 si elle manque ou differe
  moi "$P" || echouer86 "code 5 : $P non confirme"
  [ ${a[2]} = $P ] && [ ${a[3]} = $P ] || { arreter; echouer86 "code 5 : non chef"; }
  cp $T/pgid-essai-3.txt $T/pgid-ecrit-par-le-depart.txt && cp $T/depart-processus-essai-3.txt $T/depart-ecrit-par-le-depart.txt
  echo $P > $T/pgid-essai-3.txt && echo ${a[19]} > $T/depart-processus-essai-3.txt
  noter "ATTENTION : code 5 ; identite $P, depart ${a[19]}"
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
  echo "groupe de controle du programme : $(lire $GC_F) ; membres : $(lire "$(lire $GC_F)/cgroup.procs" | wc -l)"
  echo "reference (heure de depart lue par le script) : $(lire $REF_F)"
  echo "heure d'arret : $(lire $HA_F) ; filet : $(lire $FILET_F)"
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
  local n=0 gp gd k v hf r w
  noter "boucle : debut ($BASHPID)"
  CGROUPE=$(lire $GC_F)
  hf=$(( $(date -d "$(lire $HA_F)" +%s) + 60 ))
  while :; do
    n=$((n + 1))
    [ -f $FILET_F ] || [ $(date +%s) -lt $hf ] || filet
    gp=$(lire $T/pid-gardien-essai-3.txt); gd=$(lire $BASE/depart-gardien-essai-3.txt)
    v=0; vivant "$gp" "$gd" && v=1
    if [ $v = 0 ] && [ ! -f $FILET_F ] && [ -z "$(lire $CGROUPE/cgroup.procs)" ]; then
      echo "filet inutile : groupe vide $(h)" > $FILET_F
    fi
    if [ $v = 0 ] && [ -f $FILET_F ]; then
      [ -f $T/code-de-sortie.txt ] || echo "code 87 : lanceur sans code" > $BASE/echec-demarrage-essai-3.txt
      verser "versement $n : dernier"
      echo "fin : gardien absent le $(h), $n versements" > $BASE/fin-essai-3.txt
      verser "fichier fin"
      noter "boucle : fin"
      return 0
    fi
    verser "versement $n"
    for ((k = 0; k < INTERVALLE; k += w)); do
      [ $v = 1 ] && ! vivant "$gp" "$gd" && break
      [ -f $FILET_F ] || [ $(date +%s) -lt $hf ] || break
      w=$((INTERVALLE - k < 60 ? INTERVALLE - k : 60))
      r=$((hf - $(date +%s)))
      [ -f $FILET_F ] || [ $r -ge $w ] || w=$((r > 0 ? r : 1))
      sleep $w
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
[ -n "${TEXTE:-}" ] || { echo "refus : texte absent"; exit 18; }
if [ -e $BASE ] || [ -L $BASE ]; then
  [ -d $BASE ] && echo "$(h) $BASE present" >> $J
  exit 20
fi
mkdir -p $BASE || exit 20
exec >> $J 2>&1
noter "demarrage v6, H0_PREVU ${H0_PREVU:-absent}, essai :${ESSAI:- aucun}"
[[ "${H0_PREVU:-}" =~ ^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z$ ]] && t=$(date -d $H0_PREVU +%s) \
  || echouer 21 "H0_PREVU"
AGE=$(( $(date +%s) - t ))
[ $AGE -le $AGE_MAX ] && [ $AGE -ge -600 ] || echouer 21 "H0_PREVU : $AGE s"
[[ "$JETON" =~ ^[A-Za-z0-9_-]{20,100}$ ]] || echouer 22 "jeton"
umask 077
mkdir -m 700 -p $SECRET && printf '%s\n' "$JETON" > $SECRET/jeton || echouer 23 "jeton"
unset JETON
umask 022
[ "$(stat -c %a $SECRET/jeton)" = 600 ] || echouer 23 "droits du jeton"
printf '%s\n' '#!/bin/bash' '[ "${1:-}" = get ] || exit 0' 'p= q=' \
  'while IFS= read -r l && [ -n "$l" ]; do case $l in protocol=*) p=${l#*=} ;; host=*) q=${l#*=} ;; esac; done' \
  "[ \"\$p\" = $PROTO ] && [ \"\$q\" = $HOTE ] || exit 0" "IFS= read -r j < $SECRET/jeton || exit 1" \
  'printf "username=x-access-token\npassword=%s\n" "$j"' > $AS && chmod 700 $AS || echouer 24 "assistant"

pas a "paquets"
export DEBIAN_FRONTEND=noninteractive
essayer $APT_GET -o DPkg::Lock::Timeout=600 update || echouer 30 "apt update"
essayer $APT_GET -o DPkg::Lock::Timeout=600 install -y --no-install-recommends git python3 python3-venv ca-certificates \
  xz-utils || echouer 31 "paquets"
command -v git && [ -x $PY_SYS ] || echouer 32 "git ou $PY_SYS absent"
fait
g() { git -C $V config "$@"; }
git init -q $V && g user.name "machine essai 3" && g user.email essai-3@machine.invalid && g credential.helper $AS \
  && g remote.origin.url $DEPOT_URL && printf '%s\n' '#!/bin/bash' 'while read -r l ls r rs; do' \
  "  [ \"\$r\" = refs/heads/$BRANCHE ] && [ -n \"\${ls//0/}\" ] || { echo \"garde : refus vers \$r\"; exit 1; }" \
  '  [ -z "${rs//0/}" ] || git merge-base --is-ancestor $rs $ls || { echo "garde : refus, non descendante"; exit 1; }' \
  'done' > $V/.git/hooks/pre-push && chmod 755 $V/.git/hooks/pre-push || echouer 25 "versement"

pas b "clonage"
git init -q --bare $D && git -C $D config credential.helper $AS && git -C $D config remote.origin.url $DEPOT_URL \
  && git -C $D config remote.origin.pushurl aucune-poussee-depuis-ce-depot || echouer 40 "depot"
essayer git -C $D fetch -q --depth 1 origin $COMMIT || echouer 41 "clonage"
[ "$(git -C $D rev-parse --verify -q "$COMMIT^{commit}")" = $COMMIT ] || echouer 42 "commit absent"
fait

pas c "racine"
gitr() { G=$(find $R -name .git | head -n 5); [ -z "$G" ] || echouer $1 ".git dans la racine : $G"; }
mkdir $R && git -C $D archive --format=tar $COMMIT | tar -x -C $R || echouer 50 "extraction"
gitr 51
(cd $R && LC_ALL=C find . -type f ! -path ./COMMIT-DE-LA-COPIE.txt ! -path ./EMPREINTES-DE-LA-COPIE.txt -print0 \
  | LC_ALL=C sort -z | xargs -0 sha256sum) > $BASE/liste-de-la-copie.txt || echouer 52 "empreintes"
L=$(sha256sum < $BASE/liste-de-la-copie.txt | cut -c1-64)
[ $L = $REFERENCE ] || echouer 53 "liste $L"
cp $BASE/liste-de-la-copie.txt $R/EMPREINTES-DE-LA-COPIE.txt && echo $COMMIT > $R/COMMIT-DE-LA-COPIE.txt \
  || echouer 54 "copie"
fait

pas d "venv"
$PY_SYS -m venv $BASE/venv || echouer 60 "venv"
(cd $BASE && essayer $BASE/venv/bin/pip install --no-input --disable-pip-version-check -r $R/requirements-cpu.txt) \
  || echouer 61 "pip"
[ -f $PY ] && [ -x $PY ] || echouer 62 "interpreteur absent"
$BASE/venv/bin/pip freeze
fait

pas e "pieces"
[ -n "${CHARGE:-}" ] && [ -d "$CHARGE" ] && mkdir $T || echouer 70 "charge ou tenue"
[ $(find $CHARGE -mindepth 1 | wc -l) = 5 ] || echouer 71 "charge : pas 5 entrees"
while read -r e f; do
  [ -f $CHARGE/$f ] && [ ! -L $CHARGE/$f ] && cp $CHARGE/$f $T/$f || echouer 71 "piece $f absente"
  L=$(sha256sum < $T/$f | cut -c1-64)
  [ $L = $e ] || echouer 72 "empreinte de $f : $L"
done <<< "$PIECES"
chmod 755 $T/*.sh
fait

pas f "departs"
# groupe de controle cgroup v2 propre au programme, exige : sans lui, ou s'il refuse une inscription, rien n'est lance
[ -n "$CGROUPE" ] || echouer 88 "aucun cgroup v2"
[ "$(stat -f -c %T "${CGROUPE%/*}" 2>/dev/null)" = cgroup2fs ] || echouer 88 "${CGROUPE%/*} : pas cgroup v2"
mkdir "$CGROUPE" && [ -f "$CGROUPE/cgroup.kill" ] \
  || echouer 88 "$CGROUPE : creation ou cgroup.kill"
( echo $BASHPID > "$CGROUPE/cgroup.procs" ) || echouer 88 "$CGROUPE non inscriptible"
echo $CGROUPE > $GC_F
gitr 55
[ -n "$H_ARRET" ] || H_ARRET=$(date -u -d @$((t + 94 * 3600)) +%FT%TZ) || echouer 80 "heure d'arret"
[[ "$H_ARRET" =~ ^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z$ ]] && echo $H_ARRET > $HA_F || echouer 80 "heure d'arret"
mkdir $VERIF $BASE/sorties || echouer 80 "dossiers"
/bin/bash $T/lancer-essai-3-v4.sh $VERIF $R $PY $S --verifier-seulement
c=$?
[ $c = 0 ] && [ "$(lire $VERIF/code-de-sortie.txt)" = 0 ] || echouer 81 "verification : code $c"
GARDE=(--sorties $S --heure-arret-duree $H_ARRET --arret-mesure desarme --seuil-libre-octets 8000000000 $OPT_GARDIEN)
$PY_SYS -I -B $T/gardien-essai-3-v4.py --tenue $VERIF "${GARDE[@]}" --verifier-seulement || echouer 82 "gardien"
gitr 56
# le depart joue dans un sous-shell qui entre d'abord dans le groupe (sinon : 88, rien n'est lance) : le programme et
# tous ses descendants y naissent ; setsid : session neuve, qui ne croise jamais celle de ce script
( echo $BASHPID > "$CGROUPE/cgroup.procs" || exit 88
  exec "${SANS[@]}" setsid -w /bin/bash $T/demarrer-essai-3-v4.sh $T $R $PY $S ) &
wait $!
c=$?
echo $c > $BASE/code-depart-essai-3.txt
[ $c = 88 ] && echouer 88 "inscription du depart refusee"
[ $c = 0 ] || [ $c = 5 ] || echouer 83 "depart : code $c"
P=$(lire $T/pid-essai-3.txt)
# reference prise ici, aussitot, dans /proc, sans tolerance
if reference; then noter "reference : $P, $(lire $REF_F)"
else noter "reference : ${P:-?} non confirme (code $c)"; fi
for i in $(seq 1 300); do
  k=$(lire $T/code-de-sortie.txt) && break
  st "$P" || { arreter; echouer 87 "lanceur mort sans code"; }
  grep -q "part du programme" $T/journal-essai-3.txt && break
  sleep 1
done
[ -z "$k" ] || [ $k = 0 ] || { arreter; echouer 85 "programme arrete, code $k"; }
[ -f $REF_F ] || echouer86 "${P:-?} non confirme (code $c)"
[ $c = 5 ] && identite5
"${SANS[@]}" /bin/bash $T/demarrer-gardien-essai-3-v4.sh $T $PY_SYS "${GARDE[@]}" \
  || { arreter; echouer 84 "gardien refuse"; }
s=$(lire /proc/$(lire $T/pid-gardien-essai-3.txt)/stat) && a=(${s##*) }) && echo ${a[19]} > $BASE/depart-gardien-essai-3.txt
fait

pas g "boucle de versement"
# la boucle joue le texte en memoire, controle par l'amorce (aucun fichier relu) ; le texte ne porte aucun jeton
setsid nohup /bin/bash -c "$TEXTE" essai-3-boucle --boucle-de-versement < /dev/null &
echo $! > $BASE/pid-versement-essai-3.txt
fait
exit 0
: remplissage bETSqn99dHp5iQ3dJ8Pkdhh8RkJ6bd84l2A6YO5YXPmXmQ3Q9CSWC3gvbOLXkqyM45g+JcY9eFut
: remplissage bU9YSyul1lCsSJLylRdXxk2R0onZxF9yIria10pX0GB2ojec4/1/16I5Qy6hrdzzOSpdtkLZC1hT
: remplissage RK656BhBE7W8/DNwUShdVQiOjkjzgJGn4C6SjQpWq9vvSh1xLN0NA5GU3LPq8oyeE9dsb8uflARB
: remplissage f1kBSzALVEZlWGmDlhY9umjkcTXepZ93hOhelIpHqmOPfim6XtJ65UsEzhe1ngcY8m7kAHAsjYgW
: remplissage 80b5LBG8QDjeTyFt6iA+ZNp7K8Tic3MC0QF7Do+0Z492ndvroB3tCs+20lrrp8NZEYtIMDSLovqb
: remplissage XKyIrLmaFq/oTWvhgX1zLfLEd1FED7O/V072Dl+IpQDx3/yCpnI6RO+YH4RSMHX24PNqHuQejnAz
: remplissage gi0ZVzZsyPb4mS5Rg4NJl2I6JyNiYUfpUaxxJhoG6NxvRPtTujrrdVYvPpk3B9Vd4GH0YdC6XD8m
: remplissage /irytcTw+kArhHupBBxQyRtwTO95zZO1WuKwDNRf/CNyAR4z4EpRNCK5u+wBAm3T0MtzsCYABDKB
: remplissage tDWlvSsBuMLQDFQxIETwY0gLxgq1BHPP0NdXgRM3PnxL9bEAb72qdNqHyohF5PCUAztFN8mM3lf1
: remplissage 3p36fAgjPHRdesBmhy0h0Nvhm+uFLyJCIFwoT3x+2pIn2TZyqkiqxcYm47izizklbaGnvXusu8YA
: remplissage ++MLqNvlgKTzWlL7eVFa6+13mqwkDKUDH5FHxzHHrBvQnfYJ8AJFeem1aDMRyCgDaxpY4DB4lkzT
: remplissage vuTymmKP3m4v64/Md1yUZgOUXASxcz3Bvnrzb4azvUYwsWLQrXgyZUPCT0GwUwarsGOjvclYs22P
: remplissage hZx028C/BWOPynx9rp7z4HuxJvwAvhobw+kexen7jBwV0QnBTJLxlp/5JJgkOCpJ/0SO/GMSlIa6
: remplissage Hrd+vPIQL9AIjGAmyC351e4vCwwYXcBL124r68Z4TQDn0bI6GDzE2+KH5F+Fc0RvP3wxC1tczkKC
: remplissage Ip/S8nz4N/pev4HTwPR/HJ0evbJq/mr9fkdZiDZ8cftnZ4o2+lYxLJ/R2y9AysADRVyJNxUwr+Xa
: remplissage bt6LRIOTyMaYVpsBD9KGfLP+oKXjTSBsN44ovggbyfeTKi0bqB2bFWq7BocF1bprqxDwBS1ATtNM
: remplissage WE4UJyJ50cebhDstGf2NwxQd7XcHb8QM+UAsAThD95fPwbJxyuMcE1dnymgGjvMCNJuoLdzwLamy
: remplissage BGx5kiieelJHxmArJZOVCNwnwDK71yHZZ5G9ZX1ATGNGsDSFtxjUjJcHl4U9eUpWna03XTANByok
: remplissage rEBUoB456CmB2nzO/5eEh2CBxSAWKTj2Wdi60M7G/0FcBNuojJO9MZGZ8qhY3qQPpP7bFqkZO77+
: remplissage JwaJUFhftmtbChSQ2ZD+7iqqDIlraV9homyzfAKY7sLUa7ERAhUT+4RzRFu6N8w69CZRsKuGUToB
: remplissage thJ9lx8uTvsTPS5zeyiyaV68dLUkhEpjt1ZQMUFMzGyeAKXnwjRM5n6D1RQFZjzh4qyQJ3rMYQjU
: remplissage DwMzoVcx8CYbSFDagTJLuN1AL7fOjIxmh3ldgLUPXXLj521TkEmNmsCqb29c/xcT3JIz8WSdKgf3
: remplissage 3N2zwFOdUgNfwUPhJd89THqpPqiN207EC9CNoRp0srvHFlPZk0AoY2YV5zg1LEh6Pknk37hFoPCb
: remplissage Iy8OnJvMbn7kKBs97uyz2O5nifvZqBUXzEgPa4d4R+2hygno6zHVot4tvmyl7UX/hvoc6WZelHtE
: remplissage hEWaZkSzFUYX1chbrUuX3SqmR3M/VQZ4MPMbx3HTTLN+KoD1DYoSaZ9r4Js517auIFCgJfJmCa1B
: remplissage OpqA/rai/wo2yBu5fX6liOP9FObjZ/zDHp6LU6uaogc8T3TbFwfsupmssxY2EcUTGmkt0N5I3faV
: remplissage uK7dXt3voZaocURZgYlbCGI0l7LM/OYkBYSt0iJp7rybwVrNmjsYm6WWR998qZd9YsEVha/82Cqo
: remplissage l76Z2jzycRdHqjHKM0EaqYMw5bxFzzF5tvLWddhir4AmSCdhPLIN4rCDxnb5RD6p9zjKfyqVN+Em
: remplissage eZU8hQffJm7POsrXrsuACYyh7wneB0id4RyhvkFOAh1mdJdRC5k0CRQCXDs5LkE+RcKamLe1GtHX
: remplissage jgzZGHsD92WzplQDdK5lQNWcDyJMzC1idDpb4AVE4k6h6kuBi5VlKq4+K3BAiEppL3Tyo1S6lbxm
: remplissage fob4TTSfkd4g7nH5dhD4ejwbp4unpAgBuAmmLw0G8KYwceqnqRKoKlaOlVCG71agi39Ehqa4aXZL
: remplissage j5D1tNX4J5BaesW9nTsGYJNc6YMQtvTCANRV6DH5Qo9+xYIJjpyuu01broM3n9Tx3YCY9cZV7zuI
: remplissage 0GG3OPm8YBOecVz01PuHDjbnu2FA2cO0jSV+AfPfBYhoZ9e9W62tgHoXi4C2Sg0OHPsCRKy5UPMf
: remplissage jjQUul+Uhg/HUPpSGS4RDKXuijRHeX8qQMJ6Da6L7wS+UXwLZ3KLroYSrQwhKazqyZK8S6Lpw/9R
: remplissage xyKliowfBrg+Hv+/vwHxUoqkAr9ULOoSGgMNVN9PJZ4fSxC/13L0kxydm4gD59AwyDtYgU/stIhT
: remplissage k89ING/5EarFn1MN5dv1JwpDV/Htj3iIg2pACNRgtGjYtN5Ta4go2R7XunpAPxIlUA50duYJJ0Hi
: remplissage Eng6WCQeRpb0q6p0TPEa++7La12uT/xzb/7GFN5rniAmru6bvFAzjD79XHZrEAdrhkMv4TxApRWw
: remplissage 08T6f5ftpYkZlWVmUQ8gy7qpNJT+rcMNoEUU/FP5mwFXJQ6qQZ6xhyh7N5kYzDk4UNy6eH43jj/l
: remplissage PE5B1mXNIf4bS2AAq+laSsR47IqEpgyfFbFAEXmkDBuF/pzqAzcw/DZ1XPUNFFfVEJBi1n9qTwkX
: remplissage iXKXwYLcpTd/jocvDR91NMvQ5exl++RIVA2keIkHyLLLSIM4xhVC+KksgjkHu44r5Lf8XG7dx9WU
: remplissage PREtDIgT+lf0HJOr09XbE3R0W/AMnS1yaMLnywD2Y391SH8oZVLlrXayUwedCLAFQhJP0qk2WOY7
: remplissage XbRVrH3p8vrAGkduzfOc68W2vFOD/cDEgbqh+QE/0dgqlyiym0Y77EHZQys00Bknf6w82WmixSbY
: remplissage m7Fqyh+nQjV5EsnL/eLShgSn6S1gihMirjttZneStw6r88X4cMM9M64XAatx8OePm8cYPpkDc1sC
: remplissage lt/WWX/gDORtab9yoYqCf7BYRJe3fKyAKsQTCg15PjOCpDsBC2sIHj/xJf44XwSGgcpV4xLfc0Ve
: remplissage RqKhbv8GK79A8yM79oI0hOzs8sntiK9XYDF1qQzFV/H123mTXePr9OjcQGQr0w4iW8mu8TQPW7+w
: remplissage omKYf+myXFAqH5W6NjsvxtXwnurOU6t3Q19wi4NrVHWV5DtXX4UClbucZ3O5uxJO9dqsHMrBA+g0
: remplissage 9KjcxXsrAokCHC5Elknr+J4fRysg+TolUrR8ljt8kGFea5HUm+s4pZ/9Mx7nqfchE6CijOWw9PBS
: remplissage Me/ddF3x4TeoVgr+gw7ne8uDuD5PqtcR/rPvbKonR1qE5ELFI2ylKSWwIqp6OChEaq0QmdwB1NBU
: remplissage SOcHDaW87blqM5jExRJeAYZouq8yY4Yi10Tmg8VGkzgzEkJuxkUnFbrZtFuErf2ns//h9dFqS821
: remplissage VY4NjNjgCOGrsoTkdIW1wHjbBqhRlyaENJR7WRe069SFHdQX3grMnfC2yUaLG8jtNLYHUD2YQ6lD
: remplissage 1ujxv4aooL2LXxcoXspLqFcZOw+fKTrnG4sv4GI9sqTcdGnBCPK348RZgc0zL6+ZrIRP12ej++jU
: remplissage e4rHMoUiASqT1osgro6tG6QPR3tRadTUpQ1csKqDOiD29l679ZA3rYlO1xUnAn/tRH8hstdEMdeg
: remplissage n24U0+r+ULcWJuSo5YjpI9puvREguX+s4kXul5h+dQTb/zCuOahW+pmcuqpTYZ4KqkQQZ5jf307M
: remplissage UVyMmRAmG8TNlsiFczQMrOQCe+uCYKzx2+FX9O1EwfWaPxcAnLkijWLuoKpEqab3zwt3WFE3qHUw
: remplissage DG9+jNireu5ZyAmH+391l7QcBPqNGvG4u2Kv+m3XfoN9glmFmsQQbRiYmRxTQHAKp2MmxelFnKkn
: remplissage OnvDpUg1x1PkXRyX32rk1jRHJXmszN4rduyFKmAN5DKqg/ND53zJymYVlm65IwGpJskkqJpWA3Qk
: remplissage ZlHbtgc/dO/vIrvzjvaDI2OXRAwzDPh2Ee/LJEc5Q/Mqww94wi+VerBMF/IPqLkJdcqNy+9fHMDE
: remplissage o4q+2EfKXWb+rzP8pU+S8KVU/TIdw5NI7oEg7EFZe7nXhF/lFNrSo3SIBIzx8j4xubfE4Ybithqb
: remplissage /p5F+CoV9CYeGBnLzZn4SL8qaD215gZHB7GGO7pdnHbr134xFVUELCso9cUh5wLIOtejj5jvJypk
: remplissage fr8ICO5DXy8YXeZsjIdsfQG4TlAXzGfb/0pe7f6CYyfNeRIPJaWgwJrnvjyYU0u2cvhKijao0hig
: remplissage KGBUXoTTynp2DD7zz4kGGHxZlD1vrkXhKo0QSH3jDrEX8rM4t7Vmcj4V6njySk53YSNvDsx/RmD1
: remplissage cBz+deFQphJ7B1pXvQiZsg+Ep6lWQCZJis4IE0Ty08OJOS3NTMXZJp+ub03Oxd9/sArYiFOihv4H
: remplissage iUANsHWffvO/pSqZhANjlnqSuq1D9G8pC1bgFB+guk2VJzorN6iwQwONqiRsWa8WNZ5KEc6m3vp9
: remplissage XJwrmNaxPGZFKCjEOJRwFfv+d6DqsTWRzJTucEydCmGwr6qiou3v+ezqSPBGphYUMP3ohaKlLIes
: remplissage ofr3DploNTJ25DTH22TTk6yQE22Q3DVCc4aH/gJW15ovxC7KEyVNBYHIRlk5kYjbvXnrIEWGE2gm
: remplissage LAOXDXCUpKqem5R2kTK4MviUdURsBzwGXcy3Z+T5ILxd3D1Q0EuUe1Y2xbDbwGa3EFZ2P4hn2NP8
: remplissage 4dDyQd0PjPZBQAC7DDYoAQ+kDiShxa2PYW/9Z99h0K2LvZyfVT2G9UtSluCtq+9KlPmJSMTmuhnK
: remplissage N7XwgEdEpBThWKAPLiBpALx/gFTXP1RSY7DD6unHouSRkescgjSaPXg9INxAZ5H6XrIb+/tPPqlc
: remplissage u+cEq7q77EuZKxlfzevZ6cyk6KGigqHaCbFSfGuYPAbRTKuEHJrv6zNdTQR37NTFOvKDCi5s3Cz3
: remplissage MXRSUm6yJGre29x0bZwa/LUjVf1gd4yNL3VjIFUbKAmyD9kM0XglCYANx3+i78ov5hLc8ujLFtjT
: remplissage gtibwgGvXHvRdQ==
