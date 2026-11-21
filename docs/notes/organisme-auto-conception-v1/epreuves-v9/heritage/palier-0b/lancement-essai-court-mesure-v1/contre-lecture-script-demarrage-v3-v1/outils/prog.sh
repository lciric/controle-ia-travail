#!/bin/bash
# faux programme : $1 mode (arbre|orphelin|simple) ; $2 dossier de tenue (T) ; ecrit les identifiants vus dans $2/arbre.txt
T=$2
echo "$$ programme" >> $T/arbre.txt
case $1 in
  arbre)
    sleep 600 & echo "$! enfant-sleep" >> $T/arbre.txt
    ( echo "$BASHPID enfant-sous-shell" >> $T/arbre.txt; sleep 600 & echo "$! petit-enfant-sleep" >> $T/arbre.txt; wait ) &
    wait ;;
  orphelin)
    # le fils lance un petit-fils puis se termine : le petit-fils est reparente (identifiant de parent 1 ou sous-reaper)
    ( sleep 600 & echo "$! petit-fils-orphelin" >> $T/arbre.txt ) &
    sleep 600 & echo "$! enfant-sleep-vivant" >> $T/arbre.txt
    wait ;;
  *) wait ;;
esac
