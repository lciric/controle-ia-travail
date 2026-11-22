#!/bin/bash
# Fonctions d'arret du script v6 REEL (extraites entre les reperes, texte non modifie), jouees sur un faux programme :
# un descendant en session neuve, pere mort, dans un vrai cgroup v2 de banc ; un etranger hors du groupe.
# Usage : harnais-arret.sh RB(neuf)
set -u
RB=$1
S6=/home/user/controle-ia-travail/docs/notes/organisme-auto-conception-v1/epreuves-v9/heritage/palier-0b/lancement-essai-court-mesure-v1/auteur-script-demarrage-v6/demarrage-machine-essai-3-v6.sh
mkdir -m 700 $RB || exit 2
sed -n '/^# >>> fonctions d.identite/,/^# <<< fin des fonctions/p' $S6 > $RB/fonctions.sh
echo "fonctions extraites : $(wc -l < $RB/fonctions.sh) lignes, empreinte $(sha256sum < $RB/fonctions.sh | cut -c1-16)"
BASE=$RB/base; T=$BASE/tenue; V=$BASE/versement
REF_F=$BASE/ref.txt FILET_F=$BASE/filet.txt GC_F=$BASE/gc.txt
mkdir -p $T
h() { date -u +%FT%TZ; }
noter() { echo "$(h) $*"; }
PAS=x
echouer() { noter "ECHEC du pas ($PAS), code $1 : $2"; exit $1; }   # identique a l'original sauf le versement (pas de depot V ici)
. $RB/fonctions.sh
etat() { local s a; read -r s < /proc/$1/stat 2>/dev/null || { echo absent; return; }; a=(${s##*) }); [ ${a[0]} = Z ] && echo mort-zombie || echo VIVANT; }

# etranger : hors du groupe, session propre, parent = ce harnais (qui n'est pas dans le groupe)
setsid sleep 600 < /dev/null > /dev/null 2>&1 &
ETR=$!
echo "etranger : $ETR $(etat $ETR)"

nouveau_cas() {  # $1 nom ; cree groupe $G, faux programme (pere mort + evade), ecrit pid ; pose EV et PP
  G=/sys/fs/cgroup/unified/ca-arret-$1
  mkdir $G || exit 3
  : > $RB/ev-$1.txt
  cat > $RB/prog-$1.sh <<EOF
#!/bin/bash
echo \$\$ > $G/cgroup.procs
( setsid tail -f $RB/ev-$1.txt < /dev/null > /dev/null 2>&1 & echo \$! > $RB/ev-$1.pid )
exit 0
EOF
  chmod 755 $RB/prog-$1.sh
  setsid /bin/bash $RB/prog-$1.sh < /dev/null > /dev/null 2>&1 &
  PP=$!
  for i in $(seq 1 100); do [ -s $RB/ev-$1.pid ] && break; sleep 0.05; done
  EV=$(cat $RB/ev-$1.pid)
  echo $PP > $T/pid-essai-3.txt
  sleep 0.3
  echo "  [$1] programme(pere) $PP $(etat $PP) ; descendant $EV $(etat $EV) ; groupe : [$(cat $G/cgroup.procs | tr '\n' ' ')] ; session du descendant : $(read -r s < /proc/$EV/stat; a=(${s##*) }); echo ${a[3]})"
}
fin_cas() {  # $1 nom : bilan et nettoyage (par identifiants)
  echo "  [$1] APRES : descendant $EV $(etat $EV) ; etranger $ETR $(etat $ETR) ; membres du groupe : [$(cat $G/cgroup.procs | tr '\n' ' ')]"
  for x in $(cat $G/cgroup.procs); do kill -KILL $x 2>/dev/null; done
  kill -KILL $EV 2>/dev/null
  for i in $(seq 1 30); do [ -z "$(cat $G/cgroup.procs)" ] && break; sleep 0.1; done
  rmdir $G
}
echo "$(date +%s)" > /dev/null
CGROUPE_ORIG=
case_run() {  # $1 nom ; $2 fonction a jouer ; $3 CGROUPE a donner ('G' = le vrai groupe, '' = aucun, autre = chemin)
  nouveau_cas $1
  case "$3" in G) CGROUPE=$G ;; *) CGROUPE=$3 ;; esac
  echo "$PP" > /dev/null
  rm -f $FILET_F $REF_F
  echo "--- $1 : $2 avec CGROUPE='$CGROUPE'"
  ( $2 "essai" ) 2>&1 | sed 's/^/    /'
  [ -f $FILET_F ] && echo "    FILET_F : $(cat $FILET_F)"
  fin_cas $1
}
case_run A-echouer86-code86 echouer86 G
case_run B-filet filet G
case_run C-arreter arreter G
echo "=== temoin rouge : sans groupe, le descendant en session neuve echappe-t-il a arreter ? ==="
case_run D-arreter-sans-groupe arreter ''
echo "=== temoin rouge : groupe factice (dossier ordinaire, cgroup.procs non videable) : vider doit dire NON vide ==="
mkdir $RB/faux-groupe; echo 424242 > $RB/faux-groupe/cgroup.procs; : > $RB/faux-groupe/cgroup.kill
CGROUPE=$RB/faux-groupe
( vider; echo "vider rend $?" ) 2>&1 | sed 's/^/    /'
( echouer86 "essai" ) 2>&1 | sed 's/^/    /'
kill -KILL $ETR
echo "etranger retire : $ETR $(etat $ETR)"
