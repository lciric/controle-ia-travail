#!/bin/bash
# Faux programme des essais d'arrêt (repris du relecteur, prog.sh) : $1 mode (arbre|orphelin|evade|simple), $2 dossier T ;
# écrit « identifiant rôle » de chacun de ses processus dans T/arbre.txt.
T=$2
echo "$$ programme" >> $T/arbre.txt
case $1 in
  arbre)
    sleep 600 & echo "$! enfant-sleep" >> $T/arbre.txt
    ( echo "$BASHPID enfant-sous-shell" >> $T/arbre.txt; sleep 600 & echo "$! petit-enfant-sleep" >> $T/arbre.txt; wait ) &
    wait ;;
  orphelin)
    ( sleep 600 & echo "$! petit-fils-orphelin" >> $T/arbre.txt ) &
    sleep 600 & echo "$! enfant-sleep-vivant" >> $T/arbre.txt
    wait ;;
  evade)  # v5 (R1) : un fils lance un descendant qui ouvre sa propre session (setsid sans fourche), puis meurt
    ( setsid sleep 600 & echo "$! descendant-session-neuve-pere-mort" >> $T/arbre.txt ) &
    sleep 600 & echo "$! enfant-sleep-vivant" >> $T/arbre.txt
    wait ;;
  *) wait ;;
esac
