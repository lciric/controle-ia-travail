#!/bin/bash
# Joue UN cas du script v6 reel (par l'amorce v6 reelle et les donnees du fabricant v6 reel), sur factices locaux.
# Usage : lot-integre.sh RB NOM [VAR=VAL ...]    (RB : dossier prepare par preparer-distant.sh)
set -u
RB=$1 NOM=$2; shift 2
V6=/home/user/controle-ia-travail/docs/notes/organisme-auto-conception-v1/epreuves-v9/heritage/palier-0b/lancement-essai-court-mesure-v1/auteur-script-demarrage-v6
AUT=/home/user/controle-ia-travail/docs/notes/organisme-auto-conception-v1/epreuves-v9/heritage/palier-0b/lancement-essai-court-mesure-v1/auteur-script-demarrage-v6/essais-outils
W=$RB/$NOM
mkdir -m 700 $W || exit 2
git clone -q --bare $RB/partage.git $W/distant.git || exit 2
git -C $W/distant.git config uploadpack.allowAnySHA1InWant true
export TOKV=$(printf 'Zq9_-%.0s' $(seq 1 20))
FABRICANT_BANC=oui FABRICANT_DEPOT_DISTANT=$W/distant.git /bin/bash $V6/fabriquer-donnees-demarrage-v6.sh TOKV $W/donnees > $W/fabricant.txt 2>&1 || { echo "fabricant refuse"; cat $W/fabricant.txt; exit 3; }
unset TOKV
G=/sys/fs/cgroup/unified/ca-banc-$NOM
export ESSAI_DEMARRAGE_BANC=oui ESSAI_DEMARRAGE_BASE=$W/base ESSAI_DEMARRAGE_SECRET=$W/secret ESSAI_DEMARRAGE_DEPOT_URL=file://$W/distant.git
export ESSAI_DEMARRAGE_APT_GET=$AUT/faux-apt-get.sh ESSAI_DEMARRAGE_PY_SYS=$AUT/faux-python3.sh
export ESSAI_DEMARRAGE_INTERVALLE=5 ESSAI_DEMARRAGE_ATTENTE=1 ESSAI_DEMARRAGE_OPT_GARDIEN="--intervalle-s 1 --delai-force-s 5"
export ESSAI_DEMARRAGE_CHARGE=$W/charge-amorce ESSAI_DEMARRAGE_CGROUPE=$G
export FAUX_JOURNAL=$W/faux-journal.txt FAUX_JOURNAL_PROGRAMME=$W/programme.txt FAUX_DUREE_S=4
export NO_PROXY=127.0.0.1,localhost
ATT=300
for kv in "$@"; do
  case "$kv" in
    ATT=*) ATT=${kv#ATT=} ;;
    ESSAI_DEMARRAGE_CGROUPE=THREADED)
      mkdir -p $G-thr/x && echo threaded > $G-thr/x/cgroup.type; export ESSAI_DEMARRAGE_CGROUPE=$G-thr/x/essai-3-programme ;;
    *=*) export "$kv" ;;
  esac
done
cp $W/donnees $W/part-001
/bin/bash $W/part-001 > $W/sortie-script.txt 2>&1 < /dev/null
CODE=$?
PV=$(cat $W/base/pid-versement-essai-3.txt 2>/dev/null)
if [ -n "$PV" ]; then
  for i in $(seq 1 $ATT); do [ -e /proc/$PV ] || break; sleep 1; done
fi
{
  echo "cas $NOM : code du script $CODE ; reglages : $*"
  echo "sortie directe : $(head -c 200 $W/sortie-script.txt | tr '\n' ' ')"
  echo "echec ecrit : $(cat $W/base/echec-demarrage-essai-3.txt 2>/dev/null || echo aucun)"
  echo "code depart : $(cat $W/base/code-depart-essai-3.txt 2>/dev/null || echo -)"
  echo "groupe ecrit : $(cat $W/base/groupe-de-controle-essai-3.txt 2>/dev/null || echo non) ; reference : $(cat $W/base/depart-lu-par-le-script-essai-3.txt 2>/dev/null || echo aucune)"
  echo "heure d'arret : $(cat $W/base/heure-arret-essai-3.txt 2>/dev/null || echo -) ; filet : $(cat $W/base/filet-essai-3.txt 2>/dev/null || echo aucun)"
  echo "pid programme ecrit : $(cat $W/base/tenue/pid-essai-3.txt 2>/dev/null || echo aucun) ; faux programme lance : $([ -f $W/programme.txt ] && echo OUI || echo non) ; gardien : $([ -f $W/base/tenue/pid-gardien-essai-3.txt ] && echo lance || echo non)"
  echo "journal (pas, echec, arret, filet) :"
  grep -E "pas \(|ECHEC|arrete|groupe|filet|reference|ATTENTION|boucle" $W/base/journal-demarrage-essai-3.txt 2>/dev/null | cut -c1-200
  echo "dernier etat verse :"; cat $W/base/versement/essai-3/etat-essai-3.txt 2>/dev/null
  echo "jeton factice hors donnees/part-001/secret : $(grep -rlF "$(printf 'Zq9_-%.0s' $(seq 1 20))" $W 2>/dev/null | grep -v -e '/donnees$' -e '/part-001$' -e '/secret/jeton$' | tr '\n' ' ')"
} > $W/resume.txt 2>&1
cat $W/resume.txt
# nettoyage par identifiants
for g in $G $G-thr/x/essai-3-programme; do
  if [ -f $g/cgroup.procs ]; then for x in $(cat $g/cgroup.procs); do kill -KILL $x 2>/dev/null; done; fi
done
for i in $(seq 1 30); do [ -z "$(cat $G/cgroup.procs 2>/dev/null)" ] && break; sleep 0.1; done
rmdir $G 2>/dev/null
rmdir $G-thr/x/essai-3-programme $G-thr/x $G-thr 2>/dev/null
rm -rf $W/base/racine $W/base/depot.git $W/distant.git $W/base/venv
