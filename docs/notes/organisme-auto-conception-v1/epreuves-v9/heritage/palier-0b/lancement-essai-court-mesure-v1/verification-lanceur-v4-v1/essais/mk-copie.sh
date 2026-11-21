#!/bin/bash
# Ma copie : git archive du commit (dépôt lu seulement) extrait dans v5/copie, plus les deux fichiers de la copie
# (commit ; liste = MA liste refaite par ls-tree/cat-file).
set -eu
V=/tmp/claude-0/-home-user-controle-ia-travail/d90e22c7-b755-5554-90ae-faa848d18eef/scratchpad/verificateur-gardien-v2/v5
C=d7f949acd9ac92e998e57663d2cc741de93f18c3
git -C /home/user/controle-ia-travail archive --format=tar $C | tar -x -C $V/copie
echo $C > $V/copie/COMMIT-DE-LA-COPIE.txt
cp $V/ma-liste.txt $V/copie/EMPREINTES-DE-LA-COPIE.txt
echo "copie : $(find $V/copie -type f | wc -l) fichiers (liste et commit compris)"
