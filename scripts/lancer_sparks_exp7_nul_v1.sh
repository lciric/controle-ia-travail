#!/usr/bin/env bash
# Préparation du lancement de SPARKS-EXP7-NUL depuis la session (ne crée rien) : vérifie GO-2026-11-04-04 dans
# `registres/go.md` (type calcul, plafond 25 USD, échéance, non révoqué), le sceau du texte, puis imprime la commande
# de création à lancer par la session, littérale (`vastai create instance`) pour que la garde `.claude/hooks/garde_calcul.py`
# la voie et revérifie le GO. L'amorce revérifie le GO sur l'instance avant tout calcul.
#   bash scripts/lancer_sparks_exp7_nul_v1.sh <OFFRE> <PRIX_HEURE_USD> <COMMIT>
set -euo pipefail
OFFRE="${1:?identifiant de l'offre}"; PRIX="${2:?prix horaire total de l'offre (dph_total)}"; COMMIT="${3:?commit}"
cd "$(dirname "$0")/.."
PYTHONPATH=src python3 -I -B -c "import sys; sys.path.insert(0, 'src/controle_ia/sparks_exp7_nul_v1'); import go; sys.exit(go.main(['registres/go.md']))"
PYTHONPATH=src python3 -B -m controle_ia.scellement verifier prereg/SPARKS-EXP7-NUL-preenregistrement-v1.md
python3 -I -c "import sys; p=float(sys.argv[1]); assert 0 < p <= 2.0, 'au-delà de 2 USD/h, moins de 11 h 15 tiennent sous 25 USD (marge 10 %)'" "$PRIX"
git cat-file -e "$COMMIT^{commit}"
cat <<EOF
Commande à lancer par la session (jetons lus depuis l'environnement, jamais écrits dans un fichier) :
GO_ID=GO-2026-11-04-04 vastai create instance $OFFRE --image pytorch/pytorch:2.9.1-cuda12.8-cudnn9-runtime --disk 120 \\
  --env "-e COMMIT=$COMMIT -e PRIX_HEURE_USD=$PRIX -e GH_TOKEN=\$GH_TOKEN -e HF_TOKEN=\$HF_TOKEN -e DEPOT_URL=https://github.com/lciric/controle-ia-travail.git" \\
  --args bash -c "\$(cat scripts/amorce_instance_sparks_exp7_nul_v1.sh)"
Image et disque : à confirmer contre le dernier lancement réussi (traces/p3-v1-*/p3-lancement-v1-appel2/) ; disque :
110 à 122 modèles × 0,2 Go de couches ≈ 24,5 Go ; au pire 122 × 3 essais (deux réentraînements) × 0,2 Go ≈ 73 Go,
plus l'environnement et le modèle de départ (calcul) : 120 Go demandés.
EOF
