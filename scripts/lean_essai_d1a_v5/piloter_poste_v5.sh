#!/usr/bin/env bash
# piloter_poste_v5.sh — essai Lean, D-1a, v5 (contre-lecture machine de la v4 918662a7…, R-2323). **Non éprouvé** (aucune
# machine joignable depuis la session cloud). Lancé par la session locale, sur l'ordinateur de Lazar (macOS ou Linux), depuis
# la racine du clone ; le serveur ne reçoit ni le jeton de Hetzner ni aucune clé de modèle. Corps identique à la v4 ; seuls
# changent la minuterie (minuterie_v5) et l'ordre, fixé par docs/notes/g0-deux-semaines-v1/lean-outillage-d1a-v1/
# procedure-poste-local-d1a-v5.md, qui fait foi :
#   L1  minuterie_v5 preparer, acces-creer ; commit et poussée du fichier de rattrapage et du fichier d'accès ;
#       la mère prouve le même projet et s'arme (tâches à heure absolue H et H + 24 h) AVANT toute création
#   L2  minuterie_v5 creer-et-armer --detache --sortie F ; lecture de F ; verifier-minuterie --journal-minuterie J
#   P1  piloter_poste_v5.sh avant IP CLE COMMIT    installation réseau ouvert ; sonde « ouverte » (cas sain)
#   L3  minuterie_v5 acces-couper, puis verifier-coupure (le serveur porte exactement ce pare-feu, « applied »)
#   P2  piloter_poste_v5.sh apres IP CLE SORTIES   nftables, sonde « fermée », harnais déposé APRÈS la coupure,
#       épinglage du vérificateur du noyau, **premier pas `noyau`** (arrêt s'il échoue), épreuve, mesures
#   L4  minuterie_v5 detruire --identifiant N --journal J ; inventaire ; acces-supprimer ; pièces poussées
# Installation et coupure : scripts v1 inchangés ; harnais Lean : modules et artefacts v4 inchangés.
set -euo pipefail
PHASE=${1:?phase}; IP=${2:?adresse}; CLE=${3:?clé ssh jetable}
S=(ssh -i "$CLE" -o StrictHostKeyChecking=accept-new -o BatchMode=yes "root@$IP")
ICI=$(cd "$(dirname "$0")" && pwd)
V1="$ICI/../lean_essai_d1a_v1"
V4="$ICI/../lean_essai_d1a_v4"
PAQ="$ICI/../../src/controle_ia/lean_essai"
if [ "$PHASE" = avant ]; then
  COMMIT=${4:?commit de Mathlib}
  scp -i "$CLE" -o BatchMode=yes "$V1/installer_chaine_v1.sh" "$V1/couper_reseau_v1.sh" "$PAQ/sonde_reseau_v1.py" "root@$IP:/root/"
  "${S[@]}" bash /root/installer_chaine_v1.sh "$COMMIT"
  "${S[@]}" python3 -B /root/sonde_reseau_v1.py --attendu ouverte
elif [ "$PHASE" = apres ]; then
  SORTIES=${4:?dossier local des sorties}
  mkdir -p "$SORTIES"
  "${S[@]}" bash /root/couper_reseau_v1.sh > "$SORTIES/coupure-v5.txt"
  "${S[@]}" python3 -B /root/sonde_reseau_v1.py --attendu fermee > "$SORTIES/sonde-apres-coupure-v5.json"
  "${S[@]}" install -d -m 0755 /opt/harnais/artefacts_r5_v4 /opt/harnais/noyau
  scp -i "$CLE" -o BatchMode=yes "$PAQ/gardes_lean_v4.py" "$PAQ/executeur_bac_v4.py" "$PAQ/epreuve_isolement_v4.py" \
      "$PAQ/sonde_reseau_v1.py" "root@$IP:/opt/harnais/"
  scp -i "$CLE" -o BatchMode=yes "$PAQ/verificateur_noyau_v4.lean" "root@$IP:/opt/harnais/noyau/"
  scp -i "$CLE" -o BatchMode=yes "$V4"/artefacts_r5_v4/* "root@$IP:/opt/harnais/artefacts_r5_v4/"
  "${S[@]}" python3 -B /opt/harnais/epreuve_isolement_v4.py epingler-verificateur > "$SORTIES/verificateur-epingle-v5.json"
  "${S[@]}" python3 -B /opt/harnais/epreuve_isolement_v4.py noyau > "$SORTIES/premier-pas-noyau-v5.json"   # set -e : arrêt si non conforme
  rc=0; "${S[@]}" python3 -B /opt/harnais/epreuve_isolement_v4.py epreuve > "$SORTIES/epreuve-isolement-v5.json" || rc=$?
  echo "code de sortie de l'épreuve : $rc (0 = conforme)" > "$SORTIES/epreuve-code-v5.txt"
  "${S[@]}" python3 -B /opt/harnais/epreuve_isolement_v4.py mesurer > "$SORTIES/mesures-v5.json"
  "${S[@]}" python3 -B /root/sonde_reseau_v1.py --attendu fermee > "$SORTIES/sonde-fin-v5.json"
  "${S[@]}" cat /opt/harnais/journal-installation-v1.txt /opt/harnais/chaine-v1.json > "$SORTIES/installation-v5.txt"
  echo "fin de la phase « apres » : la session locale détruit la machine maintenant (minuterie_v5 detruire --identifiant N)"
else
  echo "phase inconnue : $PHASE" >&2; exit 2
fi
