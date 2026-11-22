#!/bin/bash
# Script de la charge VIDE (E_SCRIPT = empreinte du vide, donc "bon") : l'amorce doit refuser 18 ; et script sain avec octets proches.
# Usage : cas-amorce-vide.sh RB(neuf)
set -u
RB=$1
O=/tmp/claude-0/-home-user-controle-ia-travail/d90e22c7-b755-5554-90ae-faa848d18eef/scratchpad/contre-lecture-script-demarrage-v6/outils
mkdir -m 700 $RB || exit 2
: > $RB/vide.sh
/bin/bash $O/construire-donnees-amorce.sh v6 bon $RB/vide.sh $RB/d-vide
ESSAI_DEMARRAGE_CHARGE=$RB/ch /bin/bash $RB/d-vide < /dev/null; echo "code (vide, E_SCRIPT = empreinte du vide) : $?"
# script sans saut de ligne final : l'octet final compte-t-il ?
printf '#!/bin/bash\necho STUB-SANS-NL' > $RB/sansnl.sh
/bin/bash $O/construire-donnees-amorce.sh v6 bon $RB/sansnl.sh $RB/d-sansnl
ESSAI_DEMARRAGE_CHARGE=$RB/ch2 /bin/bash $RB/d-sansnl < /dev/null; echo "code (sans saut de ligne final) : $?"
# script avec lignes vides finales
printf '#!/bin/bash\necho STUB-NL-MULTIPLES\n\n\n' > $RB/nlmult.sh
/bin/bash $O/construire-donnees-amorce.sh v6 bon $RB/nlmult.sh $RB/d-nlmult
ESSAI_DEMARRAGE_CHARGE=$RB/ch3 /bin/bash $RB/d-nlmult < /dev/null; echo "code (lignes vides finales) : $?"
