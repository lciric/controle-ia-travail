#!/usr/bin/env bash
# piloter_poste_v1.sh — essai Lean, D-1a, v1. **Non éprouvé** (aucune machine joignable depuis la session cloud : SSH refusé,
# R-821 ; consigne de la mère du 11 novembre). À lancer depuis un poste qui joint la machine par SSH (voie décidée par Lazar).
# Le poste ne porte ni le jeton de Hetzner ni aucune clé de modèle ; la session porte le jeton et pose le pare-feu du nuage
# entre les deux phases (hetzner_v1.regles_coupure), puis détruit la machine par son identifiant (minuterie_v1).
#   phase « avant » : installation réseau ouvert, sonde réseau attendue « ouverte » (cas sain de la sonde) ;
#   [session : pare-feu du nuage en coupure, vérifié appliqué]
#   phase « apres » : nftables, sonde attendue « fermée », dépôt du harnais (après la coupure), choix de la variante
#                     d'énumération, épreuve d'isolement et essais R5, mesures, rapatriement des sorties.
# Usage : piloter_poste_v1.sh avant IP CLE COMMIT | piloter_poste_v1.sh apres IP CLE RACINE_HARNAIS SORTIES
set -euo pipefail
PHASE=${1:?phase}; IP=${2:?adresse}; CLE=${3:?clé ssh jetable}
S=(ssh -i "$CLE" -o StrictHostKeyChecking=accept-new -o BatchMode=yes "root@$IP")
ICI=$(cd "$(dirname "$0")" && pwd)
if [ "$PHASE" = avant ]; then
  COMMIT=${4:?commit de Mathlib}
  scp -i "$CLE" -o BatchMode=yes "$ICI/installer_chaine_v1.sh" "$ICI/couper_reseau_v1.sh" "root@$IP:/root/"
  "${S[@]}" bash /root/installer_chaine_v1.sh "$COMMIT"
  scp -i "$CLE" -o BatchMode=yes "$ICI/../../src/controle_ia/lean_essai/sonde_reseau_v1.py" "root@$IP:/root/"
  "${S[@]}" python3 -B /root/sonde_reseau_v1.py --attendu ouverte
elif [ "$PHASE" = apres ]; then
  RACINE=${4:?racine du harnais (src/controle_ia/lean_essai)}; SORTIES=${5:?dossier local des sorties}
  mkdir -p "$SORTIES"
  "${S[@]}" bash /root/couper_reseau_v1.sh > "$SORTIES/coupure-v1.txt"
  "${S[@]}" python3 -B /root/sonde_reseau_v1.py --attendu fermee > "$SORTIES/sonde-apres-coupure-v1.json"
  "${S[@]}" install -d -m 0755 /opt/harnais/artefacts_r5_v1
  scp -i "$CLE" -o BatchMode=yes "$RACINE/gardes_lean_v1.py" "$RACINE/executeur_bac_v1.py" "$RACINE/epreuve_isolement_v1.py" \
      "$RACINE/sonde_reseau_v1.py" "root@$IP:/opt/harnais/"
  scp -i "$CLE" -o BatchMode=yes "$ICI"/artefacts_r5_v1/* "root@$IP:/opt/harnais/artefacts_r5_v1/"
  "${S[@]}" python3 -B /opt/harnais/epreuve_isolement_v1.py choisir-variante > "$SORTIES/variante-v1.json"
  rc=0; "${S[@]}" python3 -B /opt/harnais/epreuve_isolement_v1.py epreuve > "$SORTIES/epreuve-isolement-v1.json" || rc=$?
  echo "code de sortie de l'épreuve : $rc (0 = conforme)" > "$SORTIES/epreuve-code-v1.txt"
  "${S[@]}" python3 -B /opt/harnais/epreuve_isolement_v1.py mesurer > "$SORTIES/mesures-v1.json"
  "${S[@]}" python3 -B /root/sonde_reseau_v1.py --attendu fermee > "$SORTIES/sonde-fin-v1.json"
  "${S[@]}" cat /opt/harnais/journal-installation-v1.txt /opt/harnais/chaine-v1.json > "$SORTIES/installation-v1.txt"
else
  echo "phase inconnue : $PHASE" >&2; exit 2
fi
