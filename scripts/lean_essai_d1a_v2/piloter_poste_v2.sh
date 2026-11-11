#!/usr/bin/env bash
# piloter_poste_v2.sh — essai Lean, D-1a, v2 (contre-lecture 2077ae26…, R-2300). **Non éprouvé** (aucune machine joignable
# depuis la session cloud). À lancer depuis un poste qui joint la machine par SSH ; le poste ne porte ni le jeton de Hetzner ni
# aucune clé de modèle. Ordre complet, session (S) et poste (P) :
#   S1  python -m controle_ia.lean_essai.minuterie_v2 creer-et-veiller … (GO, devis lu dans l'API, minuterie dans le même
#       processus, lancé en arrière-plan ; une seconde machine sous le même GO est refusée sans mot de Lazar)  [CLL-06]
#   P1  piloter_poste_v2.sh avant IP CLE COMMIT      (installation réseau ouvert ; sonde attendue « ouverte » : cas sain)
#   S2  pare-feu du nuage en coupure (hetzner_v1.ClientHetzner.poser_regles, regles_coupure), puis
#       hetzner_v2.verifier_coupure_nuage(pare-feu, serveur) : relevé consigné au journal ; sinon, pas de phase « apres »  [CLL-13]
#   P2  piloter_poste_v2.sh apres IP CLE RACINE SORTIES   (nftables, sonde « fermée », harnais déposé après la coupure, choix
#       de la variante, épreuve, mesures ; le bac v2 refuse tout item sans réseau éprouvé fermé)
#   S3  python -m controle_ia.lean_essai.minuterie_v2 detruire --identifiant N … (« détruire maintenant », retentatives
#       jusqu'à l'absence constatée) ; la minuterie de S1 constate l'absence et s'arrête.  [CLL-05, CLL-13]
# Installation et coupure : scripts v1 inchangés (installer_chaine_v1.sh, couper_reseau_v1.sh).
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
  "${S[@]}" bash /root/couper_reseau_v1.sh > "$SORTIES/coupure-v2.txt"
  "${S[@]}" python3 -B /root/sonde_reseau_v1.py --attendu fermee > "$SORTIES/sonde-apres-coupure-v2.json"
  "${S[@]}" install -d -m 0755 /opt/harnais/artefacts_r5_v2
  scp -i "$CLE" -o BatchMode=yes "$PAQ/gardes_lean_v2.py" "$PAQ/executeur_bac_v2.py" "$PAQ/epreuve_isolement_v2.py" \
      "$PAQ/sonde_reseau_v1.py" "root@$IP:/opt/harnais/"
  scp -i "$CLE" -o BatchMode=yes "$ICI"/artefacts_r5_v2/* "root@$IP:/opt/harnais/artefacts_r5_v2/"
  "${S[@]}" python3 -B /opt/harnais/epreuve_isolement_v2.py choisir-variante > "$SORTIES/variante-v2.json"
  rc=0; "${S[@]}" python3 -B /opt/harnais/epreuve_isolement_v2.py epreuve > "$SORTIES/epreuve-isolement-v2.json" || rc=$?
  echo "code de sortie de l'épreuve : $rc (0 = conforme)" > "$SORTIES/epreuve-code-v2.txt"
  "${S[@]}" python3 -B /opt/harnais/epreuve_isolement_v2.py mesurer > "$SORTIES/mesures-v2.json"
  "${S[@]}" python3 -B /root/sonde_reseau_v1.py --attendu fermee > "$SORTIES/sonde-fin-v2.json"
  "${S[@]}" cat /opt/harnais/journal-installation-v1.txt /opt/harnais/chaine-v1.json > "$SORTIES/installation-v2.txt"
  echo "fin de la phase « apres » : la session détruit la machine maintenant (minuterie_v2 detruire)"
else
  echo "phase inconnue : $PHASE" >&2; exit 2
fi
