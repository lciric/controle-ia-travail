#!/bin/bash
# Banc v5 : joue tous les cas du script de démarrage v5 (lot v4 rejoué, plus les cas des corrections R1, R3, R4 bis de la v5), l'un après l'autre (place limitée : chaque cas retire sa racine
# et son clone), et écrit une ligne par cas dans travail/lot-v5.txt ; pose travail/lot-v5-fini à la fin.
# Emploi : lot-v5.sh
set -u
O=$(cd "$(dirname "$0")" && pwd)
ESS=$(dirname "$O")
AUT=$(dirname "$(dirname "$ESS")")
F=$ESS/travail/fabricant
C=$ESS/travail/cas
L=$ESS/travail/lot-v5.txt
: > "$L"
CHEMIN=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
PS=PATH=$O/chemin-setsid:$CHEMIN
cas() {  # nom, attendu, données, réglages...
  local nom=$1 att=$2 ud=$3; shift 3
  bash "$O/jouer-cas.sh" "$nom" "$ud" "$@" > /dev/null 2>&1
  local R=$C/$nom/resume.txt code echec reste fich ps prog etat
  code=$(sed -n 's/^code du script de démarrage : \([0-9]*\) ;.*/\1/p' "$R")
  echec=$(sed -n 's/^--- échec écrit : //p' "$R" | cut -c1-90)
  reste=$(sed -n 's/^--- processus du cas encore vivants à la fin : //p' "$R")
  fich=$(sed -n '/^--- fichiers du cas portant/,/^(fin de liste)/p' "$R" | grep -c -v -e '^---' -e '^(fin')
  ps=$(sed -n 's/^--- ps : .*lignes portant le jeton : //p' "$R")
  prog=$(sed -n 's/^--- base créée : .* faux programme lancé : //p' "$R")
  etat=$(sed -n '/^--- dernier état versé/,/^---/p' "$R" | grep -E '^(code du depart|code de sortie|echec) ' | tr '\n' ';' | cut -c1-150)
  local v5; v5=$(grep -E '^--- (premier démarrage|charge extraite|groupe de contrôle :|membres du groupe)' "$R" | sed 's/^--- //' | tr '\n' ';' | cut -c1-330)
  echo "$nom | attendu $att | rendu $code | $([ "$code" = "$att" ] && echo TENU || echo ÉCHEC) | échec : $echec | programme lancé : $prog | restants : $reste | jeton fichiers $fich, ps $ps | état : $etat | v5 : $v5" >> "$L"
}
JA=$AUT/essais/travail/jeton-factice-autre.txt
cas s1-sain 0 "$F/ud-sain"
cas q2-portes-sans-banc 19 "$F/ud-sain" SANS_BANC=1
cas q3-h0-vieux-de-3h 21 "$F/ud-h0-moins-3h"
cas q3-h0-dans-1h 21 "$F/ud-h0-plus-1h"
cas z1-jeton-vide 22 "$F/ud-jeton-vide"
cas z2-sans-jeton 22 "$F/ud-sain.sans-jeton"
cas z3-h0-faux 21 "$F/ud-h0-faux"
cas z4-second-demarrage 20 "$F/ud-sain" ESSAI_BASE_PRESENTE=1
cas a1-apt-echec 30 "$F/ud-sain" FAUX_APT_ECHEC=1
cas q5-assistant-de-production 30 "$F/ud-sain" ESSAI_DEMARRAGE_DEPOT_URL=https://github.com/lciric/controle-ia-travail.git FAUX_APT_ECHEC=1
cas b1-jeton-refuse 41 "$F/ud-sain" "SERVEUR_JETON=$JA"
cas b2-commit-absent 41 "$F/ud-sain" ESSAI_DEMARRAGE_COMMIT=72af51409a6e243b178ef2b941471e4b1de5d3a3
cas e3-script-altere-dans-la-charge 18 "$F/ud-script-altere"
cas t1-temoin-de-fuite 99 "$F/ud-temoin-fuite"
for m in fichier:81 lien:81 modif:81 suppression:81 git-fichier:55 sous-git:55 git-vide:55 git-valide:55 dossier-vide:0 chmod:0; do
  cas "cl-q3-${m%%:*}" "${m##*:}" "$F/ud-sain" "FAUX_PIP_PLANTE=${m%%:*}"
done
cas p2-git-avant-demarrer 56 "$F/ud-sain" "FAUX_PY_GIT=$C/p2-git-avant-demarrer/base/racine"
cas q6-enfant 86 "$F/ud-sain" FAUX_SETSID=enfant FAUX_DUREE_S=150 "$PS"
cas q6-mort 85 "$F/ud-sain" FAUX_SETSID=mort "$PS"
H=$(date -u -d "+170 seconds" +%Y-%m-%dT%H:%M:%SZ)
cas p3-code-5-identite-confirmee 0 "$F/ud-sain" FAUX_SETSID=tardif FAUX_DUREE_S=300 "$PS" \
  "ESSAI_DEMARRAGE_OPT_GARDIEN=--intervalle-s 1 --delai-force-s 5 --heure-arret-duree $H"
cas p4-lanceur-tue-pendant-l-attente 87 "$F/ud-sain" FAUX_SETSID=tue "$PS"
cas p4-lanceur-tue-apres-l-attente 0 "$F/ud-sain" FAUX_SETSID=tue-tard "$PS"
cas p5-gardien-refuse 84 "$F/ud-sain" FAUX_SETSID=gardien-bloque FAUX_DUREE_S=150 "$PS"
cas cl-q5-lanceur-refuse-au-depart 85 "$F/ud-sain" FAUX_SETSID=sorties "$PS"
cas c1-commit-avec-git 50 "$F/ud-sain" ESSAI_DEMARRAGE_COMMIT=d5e6371fa644922db4101b93a4b69ec5e7366497
cas c2-git-laisse-par-l-extraction 51 "$F/ud-sain" "PATH=$O/chemin-tar-laisse-git:$CHEMIN"
cas c3-commit-autre 53 "$F/ud-sain" ESSAI_DEMARRAGE_COMMIT=5b65d93a4af04b66837c8265265bd4ee6fbb9a8e
cas d1-pip-echec 61 "$F/ud-sain" FAUX_PIP_ECHEC=1
cas e1-piece-alteree 72 "$F/ud-piece-alteree"
cas e2-piece-en-trop 71 "$F/ud-piece-en-trop"
cas f1-racine-alteree-apres-c 81 "$F/ud-sain" "FAUX_PIP_ALTERER=$C/f1-racine-alteree-apres-c/base/racine/requirements-cpu.txt"
cas f2-gardien-refuse-avant-depart 82 "$F/ud-sain" "ESSAI_DEMARRAGE_OPT_GARDIEN=--intervalle-s 1 --ecart-max-arret-duree-s 3600"
cas v1-arret-de-place-et-plafond 0 "$F/ud-sain" FAUX_DUREE_S=30 FAUX_SORTIE_OCTETS=2500000 \
  "ESSAI_DEMARRAGE_OPT_GARDIEN=--intervalle-s 1 --delai-force-s 5 --seuil-libre-octets 999999999999999"
# --- v4 : cas des corrections
cas r4-e-script-absent 18 "$F/ud-e-script-absent"
cas r4-e-script-vide 18 "$F/ud-e-script-vide"
cas r4-charge-sans-script-e-script-vide 18 "$F/ud-sans-script-e-vide"
cas r1-n4-orphelin-non-chef 86 "$F/ud-sain" FAUX_SETSID=enfant FAUX_ORPHELIN=1 FAUX_DUREE_S=150 "$PS"
cas r1-petit-fils-orphelin-gardien-refuse 84 "$F/ud-sain" FAUX_SETSID=gardien-bloque FAUX_ORPHELIN=1 FAUX_DUREE_S=150 "$PS"
H=$(date -u -d "+170 seconds" +%Y-%m-%dT%H:%M:%SZ)
cas r1-petit-fils-orphelin-arret-du-gardien 0 "$F/ud-sain" FAUX_SETSID=tardif FAUX_ORPHELIN=1 FAUX_DUREE_S=300 "$PS" \
  "ESSAI_DEMARRAGE_OPT_GARDIEN=--intervalle-s 1 --delai-force-s 5 --heure-arret-duree $H"
# --- v5 : cas des corrections
cas r4bis-e-script-absent-puis-reprise 18 "$F/ud-e-script-absent" DEUX_FOIS=1
cas r4bis-e-script-vide-puis-reprise 18 "$F/ud-e-script-vide" DEUX_FOIS=1
cas r1v5-descendant-session-neuve-gardien-refuse 84 "$F/ud-sain" FAUX_SETSID=gardien-bloque FAUX_EVADE=1 FAUX_DUREE_S=150 "$PS"
cas r1v5-descendant-session-neuve-non-chef 86 "$F/ud-sain" FAUX_SETSID=enfant FAUX_EVADE=1 FAUX_DUREE_S=150 "$PS"
cas r1v5-repli-sans-cgroupe-descendant-session-neuve 84 "$F/ud-sain" FAUX_SETSID=gardien-bloque FAUX_EVADE=1 FAUX_DUREE_S=150 "$PS" \
  ESSAI_DEMARRAGE_CGROUPE=
cas r1v5-repli-chemin-non-cgroupe 0 "$F/ud-sain" "ESSAI_DEMARRAGE_CGROUPE=$C/r1v5-repli-chemin-non-cgroupe/pas-un-cgroupe"
cas r3v5-repli-code-5-non-chef 86 "$F/ud-sain" FAUX_SETSID=enfant FAUX_DUREE_S=150 "$PS" ESSAI_DEMARRAGE_CGROUPE=
H=$(date -u -d "+170 seconds" +%Y-%m-%dT%H:%M:%SZ)
cas r3v5-repli-code-5-tardif 86 "$F/ud-sain" FAUX_SETSID=tardif FAUX_DUREE_S=150 "$PS" ESSAI_DEMARRAGE_CGROUPE=
H=$(date -u -d "+170 seconds" +%Y-%m-%dT%H:%M:%SZ)
cas r1v5-descendant-session-neuve-arret-du-gardien 0 "$F/ud-sain" FAUX_SETSID=tardif FAUX_EVADE=1 FAUX_DUREE_S=300 "$PS" \
  "ESSAI_DEMARRAGE_OPT_GARDIEN=--intervalle-s 1 --delai-force-s 5 --heure-arret-duree $H"
date -u +%FT%TZ > "$ESS/travail/lot-v5-fini"
