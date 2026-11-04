#!/usr/bin/env bash
# Préparation d'un démarrage ou d'un redémarrage de SPARKS-EXP7-NUL pour l'addendum n° 1 depuis la session (ne crée
# rien, ne parle pas à Vast) : vérifie GO-2026-11-04-04 (base et extension à 40 USD), le sceau du texte v1, la liste
# fermée et l'addendum scellé au commit lancé, puis la dépense projetée (état écrit par la session) ; imprime la
# commande littérale à lancer par la session, pour que `.claude/hooks/garde_calcul.py` la voie et revérifie le GO.
#   bash scripts/lancer_sparks_exp7_nul_v2.sh <OFFRE> <PRIX_HEURE_USD> <PRIX_STOCKAGE_HEURE_USD> <COMMIT> <COMMIT_CODE> <ETAT_DEPENSE.json>
set -euo pipefail
OFFRE="${1:?offre}"; PRIX="${2:?prix horaire de la carte}"; STOCK="${3:?prix horaire du stockage}"
COMMIT="${4:?commit lancé}"; CODE="${5:?commit du code}"; ETAT="${6:?état de dépense}"
cd "$(dirname "$0")/.."
P=src/controle_ia/sparks_exp7_nul_v2
python3 -I -B -c "import sys; sys.path.insert(0, '$P'); import go; sys.exit(go.main(['registres/go.md']))"
PYTHONPATH=src python3 -B -m controle_ia.scellement verifier prereg/SPARKS-EXP7-NUL-preenregistrement-v1.md
python3 -I -B -c "import sys; sys.path.insert(0, '$P'); import garde_code; sys.exit(garde_code.main(sys.argv[1:]))" lancement . "$CODE" "$COMMIT"
python3 -I -B -c "import sys; sys.path.insert(0, '$P'); import depense; sys.exit(depense.main(sys.argv[1:]))" projeter "$ETAT"
cat <<FIN
Commande à lancer par la session (jetons lus depuis l'environnement, jamais écrits dans un fichier) :
GO_ID=GO-2026-11-04-04 vastai create instance $OFFRE --image pytorch/pytorch:2.9.1-cuda12.8-cudnn9-runtime --disk 120 \\
  --env "-e COMMIT=$COMMIT -e COMMIT_CODE=$CODE -e PRIX_HEURE_USD=$PRIX -e PRIX_STOCKAGE_HEURE_USD=$STOCK -e GH_TOKEN=\$GH_TOKEN -e HF_TOKEN=\$HF_TOKEN -e DEPOT_URL=https://github.com/lciric/controle-ia-travail.git" \\
  --args bash -c "\$(cat scripts/amorce_instance_sparks_exp7_nul_v2.sh)"
Redémarrage (copies par lots, phase causale) : même vérification avec l'état à jour, puis « vastai start instance <ID> ».
Fin du contrôle causal ou échéance : python3 -m controle_ia.sparks_exp7_nul_v2.depense instance ETAT.json, puis
« vastai destroy instance <ID> » par son identifiant (R10), consigné dans registres/arrets.md.
FIN
