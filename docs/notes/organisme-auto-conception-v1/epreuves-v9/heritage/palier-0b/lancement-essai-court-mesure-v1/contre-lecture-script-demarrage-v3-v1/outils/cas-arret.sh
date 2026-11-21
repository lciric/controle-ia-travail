#!/bin/bash
# points 2 et 3 : on joue, sur de faux processus, les definitions REELLES st/vivant/lire/arreter (lignes 51-72 du script v3)
# et le bloc REEL de lecture d'identite (lignes 226-240), extraits par sed du script livre (empreinte controlee ci-dessous).
W=/tmp/claude-0/-home-user-controle-ia-travail/d90e22c7-b755-5554-90ae-faa848d18eef/scratchpad/contre-lecture-script-demarrage-v3
S=$W/pieces/demarrage-machine-essai-3-v3.sh
O=$W/tmp/arret; rm -rf $O; mkdir -p $O
TB=$W/tables/p23-table.txt; : > $TB
echo "script : $(sha256sum < $S | cut -c1-64)" >> $TB
sed -n 51,72p $S > $O/fonctions.sh
sed -n 226,240p $S > $O/bloc.sh
{ echo 'noter() { echo "$(date -u +%T) $*"; }'
  echo 'echouer() { echo "ECHEC code $1 : $2"; exit $1; }'
  echo 'lire() { cat "$1" 2>/dev/null; }'
  cat $O/fonctions.sh
  echo 'set -u'
  echo '. '$O'/bloc.sh'
  echo 'echo "SUITE : bloc passe sans echec ; a=${a[*]:0:3}"'
} > $O/runner.sh
# (la ligne 53 'lire' est aussi dans fonctions.sh : meme definition)
vivant_p() { local s; s=$(cat /proc/$1/stat 2>/dev/null) || return 1; local a=(${s##*) }); [ "${a[0]}" != Z ]; }
etat_pids() {  # lit $1/arbre.txt ; liste "pid role vivant|mort"
  local l=""; while read -r p r; do vivant_p $p && l="$l $p:$r:VIVANT" || l="$l $p:$r:mort"; done < $1/arbre.txt; echo "$l"
}
cas() {  # $1 nom ; $2 mode de programme ; $3 chef (oui|non) ; $4 attendu ; $5 variante (normal|etranger-chef|etranger-non-chef|mort)
  local nom=$1 mode=$2 chef=$3 att=$4 var=${5:-normal}
  local T=$O/$nom; mkdir -p $T; export T
  : > $T/arbre.txt
  echo "part du programme" > $T/journal-essai-3.txt
  # etranger : un processus sans lien, vivant avant et apres
  sleep 600 & ETR=$!
  echo "$ETR etranger" >> $T/arbre.txt
  if [ $var = mort ]; then
    $O/../../outils/prog.sh simple $T & PP=$!; kill $PP; wait $PP 2>/dev/null
    echo 0 > $T/code-de-sortie.txt
  elif [ $var = etranger-chef ]; then
    setsid sleep 600 & PP=$!    # identifiant "repris" par un etranger chef de groupe
    echo "$PP etranger-qui-a-repris-l-identifiant" >> $T/arbre.txt
  elif [ $var = etranger-non-chef ]; then
    sleep 600 & PP=$!
    echo "$PP etranger-qui-a-repris-l-identifiant" >> $T/arbre.txt
  elif [ $chef = oui ]; then
    setsid $W/outils/prog.sh $mode $T & PP=$!
  else
    $W/outils/prog.sh $mode $T & PP=$!
  fi
  # attendre que l'arbre soit complet
  for i in $(seq 1 50); do [ $(wc -l < $T/arbre.txt) -ge 3 ] && break; sleep 0.1; done
  sleep 0.3
  echo $PP > $T/pid-essai-3.txt
  echo 1 > $T/pgid-essai-3.txt; echo 1 > $T/depart-processus-essai-3.txt   # contenu ecrit par le "depart" : sans importance
  local c=5
  sed -n "2p" /proc/$PP/stat > /dev/null 2>&1
  local deb; deb=$(cat /proc/$PP/stat 2>/dev/null | sed 's/.*) //' | cut -d' ' -f20)
  local out rc
  out=$(c=$c bash $O/runner.sh 2>&1); rc=$?
  sleep 1
  local pg_apres dep_apres
  pg_apres=$(cat $T/pgid-essai-3.txt); dep_apres=$(cat $T/depart-processus-essai-3.txt)
  echo "$nom | attendu $att | rendu code $rc | $(echo "$out" | tr '\n' ' ' | cut -c1-200)" >> $TB
  echo "   pid programme $PP ; depart reel (champ 20) ${deb:-absent} ; pgid ecrit apres : $pg_apres ; depart ecrit apres : $dep_apres" >> $TB
  echo "   $(etat_pids $T)" >> $TB
  [ -e $T/pgid-ecrit-par-le-depart.txt ] && echo "   copies d'origine : pgid $(cat $T/pgid-ecrit-par-le-depart.txt) ; depart $(cat $T/depart-ecrit-par-le-depart.txt)" >> $TB
  # nettoyage : tout ce que le cas a lance, par identifiant
  while read -r p r; do vivant_p $p && kill -KILL $p 2>/dev/null; done < $T/arbre.txt
  kill -KILL $PP 2>/dev/null; wait 2>/dev/null
}
cas n1-pas-chef-arbre arbre non "86, programme et descendants arretes, etranger vivant"
cas n2-chef-confirme arbre oui "suite (identite confirmee), fichiers reecrits avec la valeur lue, rien tue"
cas n3-mort-code-sortie-0 simple non "86" mort
cas n4-orphelin-pas-chef orphelin non "86 ; petit-fils orphelin: a juger"
cas n5-identifiant-repris-chef simple non "(faux vert) confirme ? : a juger" etranger-chef
cas n6-identifiant-repris-non-chef simple non "86 et ETRANGER tue ? : a juger" etranger-non-chef
