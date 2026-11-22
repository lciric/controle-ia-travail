#!/bin/bash
# E_SCRIPT absent, vide, faux, bon : code, charge laissee, reprise. Usage : cas-amorce-e-script.sh RACINE(neuve)
set -u
RB=$1
O=/tmp/claude-0/-home-user-controle-ia-travail/d90e22c7-b755-5554-90ae-faa848d18eef/scratchpad/contre-lecture-script-demarrage-v6/outils
mkdir -m 700 $RB || exit 2
printf '#!/bin/bash\necho STUB-BON\n' > $RB/bon.sh
printf '%-6s %-7s %-4s %-22s %s\n' version variante code "charge/prive laisses" sortie
for VER in v6 v4; do
  for VAR in absent vide faux bon; do
    D=$RB/d-$VER-$VAR
    /bin/bash $O/construire-donnees-amorce.sh $VER $VAR $RB/bon.sh $D > /dev/null || exit 2
    CH=$RB/ch-$VER-$VAR
    ESSAI_DEMARRAGE_CHARGE=$CH /bin/bash $D > $RB/s-$VER-$VAR.txt 2>&1 < /dev/null
    rc=$?
    ch=non; [ -e $CH ] && ch=CHARGE
    pv=$(ls -d $CH.script.* 2>/dev/null | wc -l)
    printf '%-6s %-7s %-4s %-22s %s\n' $VER $VAR $rc "$ch/prive=$pv" "$(tr '\n' ' ' < $RB/s-$VER-$VAR.txt | cut -c1-100)"
  done
done
echo "--- reprise apres un 18 (meme dossier de charge, donnees saines) ---"
for VER in v6 v4; do
  for VAR in absent vide faux; do
    CH=$RB/ch-$VER-$VAR
    ESSAI_DEMARRAGE_CHARGE=$CH /bin/bash $RB/d-$VER-bon > $RB/r-$VER-$VAR.txt 2>&1 < /dev/null
    printf '%-6s apres-%-7s code=%s %s\n' $VER $VAR $? "$(tr '\n' ' ' < $RB/r-$VER-$VAR.txt | cut -c1-100)"
  done
done
echo "--- v6 : E_SCRIPT absent n'extrait rien : le dossier de charge n'existe pas ? ---"
[ -e $RB/ch-v6-absent ] && echo "CHARGE PRESENTE (avant reprise : voir ci-dessus)" || echo "aucune charge (verifie apres reprise : $(ls -d $RB/ch-v6-absent* 2>/dev/null | wc -l) entrees)"
