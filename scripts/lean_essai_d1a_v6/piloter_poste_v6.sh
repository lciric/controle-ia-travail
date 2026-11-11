#!/usr/bin/env bash
# piloter_poste_v6.sh — essai Lean, D-1a, v6 (contre-lecture machine de la v5 897b7438…, R-2333). **Non éprouvé** (aucune
# machine joignable depuis la session cloud). Lancé par la session locale, sur l'ordinateur de Lazar (macOS ou Linux), depuis
# la racine du clone, **hors du bac à sable de Claude Code** et **en arrière-plan**, sorties dans des fichiers (CLC5-05, note 9).
# Le serveur ne reçoit ni le jeton de Hetzner ni aucune clé de modèle. Corps de la v5, plus des bornes (note 8) :
#   - chaque commande SSH s'exécute sous `timeout` **côté serveur** (coreutils d'Ubuntu ; rien à installer sur le poste) ;
#   - `ConnectTimeout` et `ServerAlive*` bornent une connexion qui pend (SSH et scp).
# IP est l'adresse du **serveur** loué (`minuterie_v6 adresse-serveur --identifiant N`), jamais celle du poste ; SORTIES est un
# dossier du poste hors du dépôt ; rien n'est versé sans `minuterie_v6 garde-poste` (CLC5-07). L'ordre fait foi dans
# docs/notes/g0-deux-semaines-v1/lean-outillage-d1a-v1/procedure-poste-local-d1a-v6.md.
set -euo pipefail
PHASE=${1:?phase}; IP=${2:?adresse du serveur}; CLE=${3:?clé ssh jetable}
O=(-o BatchMode=yes -o ConnectTimeout=30 -o ServerAliveInterval=30 -o ServerAliveCountMax=4)
S=(ssh -i "$CLE" -o StrictHostKeyChecking=accept-new "${O[@]}" "root@$IP")
C=(scp -i "$CLE" "${O[@]}")
ICI=$(cd "$(dirname "$0")" && pwd)
V1="$ICI/../lean_essai_d1a_v1"
V4="$ICI/../lean_essai_d1a_v4"
PAQ="$ICI/../../src/controle_ia/lean_essai"
if [ "$PHASE" = avant ]; then
  COMMIT=${4:?commit de Mathlib}
  "${C[@]}" "$V1/installer_chaine_v1.sh" "$V1/couper_reseau_v1.sh" "$PAQ/sonde_reseau_v1.py" "root@$IP:/root/"
  "${S[@]}" timeout 5400 bash /root/installer_chaine_v1.sh "$COMMIT"
  "${S[@]}" timeout 300 python3 -B /root/sonde_reseau_v1.py --attendu ouverte
elif [ "$PHASE" = apres ]; then
  SORTIES=${4:?dossier local des sorties, hors du dépôt}
  mkdir -p "$SORTIES"
  "${S[@]}" timeout 300 bash /root/couper_reseau_v1.sh > "$SORTIES/coupure-v6.txt"
  "${S[@]}" timeout 300 python3 -B /root/sonde_reseau_v1.py --attendu fermee > "$SORTIES/sonde-apres-coupure-v6.json"
  "${S[@]}" timeout 60 install -d -m 0755 /opt/harnais/artefacts_r5_v4 /opt/harnais/noyau
  "${C[@]}" "$PAQ/gardes_lean_v4.py" "$PAQ/executeur_bac_v4.py" "$PAQ/epreuve_isolement_v4.py" "$PAQ/sonde_reseau_v1.py" \
      "root@$IP:/opt/harnais/"
  "${C[@]}" "$PAQ/verificateur_noyau_v4.lean" "root@$IP:/opt/harnais/noyau/"
  "${C[@]}" "$V4"/artefacts_r5_v4/* "root@$IP:/opt/harnais/artefacts_r5_v4/"
  "${S[@]}" timeout 1800 python3 -B /opt/harnais/epreuve_isolement_v4.py epingler-verificateur > "$SORTIES/verificateur-epingle-v6.json"
  "${S[@]}" timeout 3600 python3 -B /opt/harnais/epreuve_isolement_v4.py noyau > "$SORTIES/premier-pas-noyau-v6.json"   # set -e : arrêt si non conforme
  rc=0; "${S[@]}" timeout 7200 python3 -B /opt/harnais/epreuve_isolement_v4.py epreuve > "$SORTIES/epreuve-isolement-v6.json" || rc=$?
  echo "code de sortie de l'épreuve : $rc (0 = conforme ; 124 = borne de temps atteinte)" > "$SORTIES/epreuve-code-v6.txt"
  "${S[@]}" timeout 3600 python3 -B /opt/harnais/epreuve_isolement_v4.py mesurer > "$SORTIES/mesures-v6.json"
  "${S[@]}" timeout 300 python3 -B /root/sonde_reseau_v1.py --attendu fermee > "$SORTIES/sonde-fin-v6.json"
  "${S[@]}" timeout 60 cat /opt/harnais/journal-installation-v1.txt /opt/harnais/chaine-v1.json > "$SORTIES/installation-v6.txt"
  echo "fin de la phase « apres » : la session locale détruit la machine maintenant (minuterie_v6 detruire --identifiant N)"
else
  echo "phase inconnue : $PHASE" >&2; exit 2
fi
