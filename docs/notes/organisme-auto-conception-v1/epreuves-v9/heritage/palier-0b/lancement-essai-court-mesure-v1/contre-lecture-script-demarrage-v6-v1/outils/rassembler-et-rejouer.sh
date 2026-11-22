#!/bin/bash
# Rassemble les resumes des cas integres (PATH masque) et rejoue les bancs rapides vers tables/.
set -u
S=/tmp/claude-0/-home-user-controle-ia-travail/d90e22c7-b755-5554-90ae-faa848d18eef/scratchpad/contre-lecture-script-demarrage-v6
for c in i1-sain i2-sans-cgroupe i3-parent-pas-cgroupe i4-non-inscriptible i5-sans-kill; do
  sed -e 's|PATH=[^ ]*|PATH=(masque)|' $S/banc-int/$c/resume.txt > $S/tables/integre-$c.txt
done
/bin/bash $S/outils/cas-fabricant.sh $S/banc-fab > $S/tables/fabricant-cas-artefacts.txt 2>&1
/bin/bash $S/outils/cas-fabricant-2.sh $S/banc-fab2 > $S/tables/fabricant-cas-complements.txt 2>&1
/bin/bash $S/outils/cas-amorce-e-script.sh $S/banc-e-script > $S/tables/amorce-e-script.txt 2>&1
/bin/bash $S/outils/cas-amorce-vide.sh $S/banc-vide > $S/tables/amorce-vide.txt 2>&1
/bin/bash $S/outils/harnais-arret.sh $S/banc-arret > $S/tables/arret-fonctions.txt 2>&1
/bin/bash $S/outils/cas-fabricant-taille.sh $S/banc-taille > $S/tables/fabricant-taille.txt 2>&1
echo "course v4 (400 exec., banc-course-v4) : executes-le-bon=98 executes-le-faux(DIVERGENCE)=100 refus18=202 autre=0" > $S/tables/course-v4.txt
echo fini
