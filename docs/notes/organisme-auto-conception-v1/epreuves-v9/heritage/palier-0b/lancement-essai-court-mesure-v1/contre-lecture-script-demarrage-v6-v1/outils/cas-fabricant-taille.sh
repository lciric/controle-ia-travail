#!/bin/bash
# Fabricant v6 : taille annoncee, frontiere 32768/32769, empreinte E_SCRIPT, jeton factice nulle part hors du fichier produit.
# Usage : cas-fabricant-taille.sh RACINE_BANC (neuve)
set -u
RB=$1
V6=/home/user/controle-ia-travail/docs/notes/organisme-auto-conception-v1/epreuves-v9/heritage/palier-0b/lancement-essai-court-mesure-v1/auteur-script-demarrage-v6
FAB=$V6/fabriquer-donnees-demarrage-v6.sh
REEL=$V6/demarrage-machine-essai-3-v6.sh
mkdir -m 700 $RB || exit 2
git init -q --bare $RB/distant.git
export TOKV=$(printf 'Zq9_-%.0s' $(seq 1 20))
[ ${#TOKV} = 100 ] || exit 2
run() {  # $1 dossier $2 script ; rend le code
  mkdir -m 700 $1
  FABRICANT_BANC=oui FABRICANT_SCRIPT=$2 FABRICANT_DEPOT_DISTANT=$RB/distant.git /bin/bash $FAB TOKV $1/sortie > $1/stdout 2> $1/stderr
}
echo "=== F0 : script reel, jeton factice de 100 signes ==="
run $RB/f0 $REEL; echo "code $?"
cat $RB/f0/stdout
echo "taille du fichier produit : $(wc -c < $RB/f0/sortie)"
echo "E_SCRIPT dans le fichier : $(sed -n 's/^E_SCRIPT=//p' $RB/f0/sortie)"
echo "empreinte du texte reduit  : $(sha256sum < $RB/f0/sortie.script-reduit.sh | cut -c1-64)"
echo "=== fuite du jeton factice : fichiers contenant le jeton ==="
grep -rlF "$TOKV" $RB/f0 | sed "s|$RB/||"
echo "(attendu : f0/sortie seulement)"
echo "=== frontiere : script reel + ligne ': HEX' de L signes ==="
i=0; H=
while [ ${#H} -lt 400 ]; do H=$H$(printf %s $i | sha256sum | cut -c1-64); i=$((i+1)); done
for L in $(seq 60 2 300); do
  s=$RB/e$L.sh; cp $REEL $s; printf ': %s\n' ${H:0:$L} >> $s
  d=$RB/g$L; run $d $s; rc=$?
  if [ $rc = 0 ]; then N=$(sed -n 's/^taille en lecture stricte.*: \([0-9]*\) octets.*/\1/p' $d/sortie.empreintes.txt); else N=$(sed -n 's/.*de \([0-9]*\) octets en lecture stricte.*/\1/p' $d/stderr); fi
  echo "L=$L code=$rc strict=$N"
  [ $rc != 0 ] && break
  rm -rf $d $s
done
