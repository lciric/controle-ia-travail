#!/usr/bin/env bash
# piloter_poste_v4.sh — essai Lean, D-1a, v4 (contre-lecture courte de la v3 b6ca886d…, R-2307). **Non éprouvé** (aucune machine
# joignable depuis la session cloud). À lancer depuis un poste qui joint la machine par SSH ; le poste ne porte ni le jeton de
# Hetzner ni aucune clé de modèle. Ordre complet, session (S) et poste (P) :
#   S1  minuterie_v4 creer-et-armer …   intention, fichier de rattrapage et échéance AVANT l'appel ; étiquette unique ;
#       réponse perdue ⇒ recherche répétée par étiquette ; minuterie DÉTACHÉE (PID versé) ; la mère arme une tâche
#       programmée unique (send_later) à l'échéance − 1 h qui lance `minuterie_v4 detruire --pas d1a`  [CLC3-07]
#   P1  piloter_poste_v4.sh avant IP CLE COMMIT    installation réseau ouvert ; sonde « ouverte » (cas sain)
#   S2  pare-feu du nuage en coupure, puis minuterie_v4 verifier-coupure --serveur N --pare-feu F --journal J
#       (le serveur porte exactement ce pare-feu, à l'état « applied ») ; sinon, pas de phase « apres »  [CLC2-06]
#   P2  piloter_poste_v4.sh apres IP CLE SORTIES   nftables, sonde « fermée », dépôt du harnais APRÈS la coupure,
#       épinglage du vérificateur du noyau, **premier pas `noyau`** (arrêt s'il échoue), épreuve, mesures
#   S3  minuterie_v4 detruire --pas d1a (ou --identifiant N) ; la minuterie détachée constate l'absence (deux lectures)
# Installation et coupure : scripts v1 inchangés.
set -euo pipefail
PHASE=${1:?phase}; IP=${2:?adresse}; CLE=${3:?clé ssh jetable}
S=(ssh -i "$CLE" -o StrictHostKeyChecking=accept-new -o BatchMode=yes "root@$IP")
ICI=$(cd "$(dirname "$0")" && pwd)
V1="$ICI/../lean_essai_d1a_v1"
PAQ="$ICI/../../src/controle_ia/lean_essai"
if [ "$PHASE" = avant ]; then
  COMMIT=${4:?commit de Mathlib}
  scp -i "$CLE" -o BatchMode=yes "$V1/installer_chaine_v1.sh" "$V1/couper_reseau_v1.sh" "$PAQ/sonde_reseau_v1.py" "root@$IP:/root/"
  "${S[@]}" bash /root/installer_chaine_v1.sh "$COMMIT"
  "${S[@]}" python3 -B /root/sonde_reseau_v1.py --attendu ouverte
elif [ "$PHASE" = apres ]; then
  SORTIES=${4:?dossier local des sorties}
  mkdir -p "$SORTIES"
  "${S[@]}" bash /root/couper_reseau_v1.sh > "$SORTIES/coupure-v4.txt"
  "${S[@]}" python3 -B /root/sonde_reseau_v1.py --attendu fermee > "$SORTIES/sonde-apres-coupure-v4.json"
  "${S[@]}" install -d -m 0755 /opt/harnais/artefacts_r5_v4 /opt/harnais/noyau
  scp -i "$CLE" -o BatchMode=yes "$PAQ/gardes_lean_v4.py" "$PAQ/executeur_bac_v4.py" "$PAQ/epreuve_isolement_v4.py" \
      "$PAQ/sonde_reseau_v1.py" "root@$IP:/opt/harnais/"
  scp -i "$CLE" -o BatchMode=yes "$PAQ/verificateur_noyau_v4.lean" "root@$IP:/opt/harnais/noyau/"
  scp -i "$CLE" -o BatchMode=yes "$ICI"/artefacts_r5_v4/* "root@$IP:/opt/harnais/artefacts_r5_v4/"
  "${S[@]}" python3 -B /opt/harnais/epreuve_isolement_v4.py epingler-verificateur > "$SORTIES/verificateur-epingle-v4.json"
  "${S[@]}" python3 -B /opt/harnais/epreuve_isolement_v4.py noyau > "$SORTIES/premier-pas-noyau-v4.json"   # set -e : arrêt si non conforme
  rc=0; "${S[@]}" python3 -B /opt/harnais/epreuve_isolement_v4.py epreuve > "$SORTIES/epreuve-isolement-v4.json" || rc=$?
  echo "code de sortie de l'épreuve : $rc (0 = conforme)" > "$SORTIES/epreuve-code-v4.txt"
  "${S[@]}" python3 -B /opt/harnais/epreuve_isolement_v4.py mesurer > "$SORTIES/mesures-v4.json"
  "${S[@]}" python3 -B /root/sonde_reseau_v1.py --attendu fermee > "$SORTIES/sonde-fin-v4.json"
  "${S[@]}" cat /opt/harnais/journal-installation-v1.txt /opt/harnais/chaine-v1.json > "$SORTIES/installation-v4.txt"
  echo "fin de la phase « apres » : la session détruit la machine maintenant (minuterie_v4 detruire)"
else
  echo "phase inconnue : $PHASE" >&2; exit 2
fi
