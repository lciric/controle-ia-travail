#!/usr/bin/env bash
# Préparation d'un démarrage de SPARKS-EXP7-NUL, v3 (version neuve de `lancer_sparks_exp7_nul_v2.sh`, R12), depuis la session ;
# ne crée rien et ne parle pas à Vast : vérifie GO-2026-11-04-04 (base et extension à 40 USD), le sceau du texte v1, la liste
# fermée et l'addendum scellé au commit lancé, la dépense projetée (état écrit par la session), puis imprime la commande
# littérale (création, ou redémarrage sur ordre écrit), pour que `.claude/hooks/garde_calcul.py` la voie et revérifie le GO.
#   bash scripts/lancer_sparks_exp7_nul_v3.sh creation <OFFRE> <PRIX_CARTE> <PRIX_STOCKAGE> <COMMIT> <COMMIT_CODE> <ETAT.json> [ECHEANCE_UTC_S]
#   bash scripts/lancer_sparks_exp7_nul_v3.sh redemarrage <ID> <PRIX_CARTE> <PRIX_STOCKAGE> <COMMIT> <COMMIT_CODE> <ETAT.json>
set -euo pipefail
QUOI="${1:?creation ou redemarrage}"; CIBLE="${2:?offre ou identifiant}"; PRIX="${3:?prix carte}"; STOCK="${4:?prix stockage}"
COMMIT="${5:?commit lancé}"; CODE="${6:?commit du code}"; ETAT="${7:?état de dépense}"; ECH="${8:-1795046400}"
case "$ECH" in ''|*[!0-9]*) echo "ECHEANCE_UTC_S non entière" >&2; exit 2;; esac
[ "$ECH" -le 1795046400 ] || { echo "échéance au-delà de la fin du 18 novembre : refus" >&2; exit 2; }
cd "$(dirname "$0")/.."
P2=src/controle_ia/sparks_exp7_nul_v2; P3=src/controle_ia/sparks_exp7_nul_v3
python3 -I -B -c "import sys; sys.path.insert(0, '$P2'); import go; sys.exit(go.main(['registres/go.md']))"
PYTHONPATH=src python3 -B -m controle_ia.scellement verifier prereg/SPARKS-EXP7-NUL-preenregistrement-v1.md
python3 -I -B -c "import sys; sys.path.insert(0, '$P3'); import garde_code; sys.exit(garde_code.main(sys.argv[1:]))" lancement . "$CODE" "$COMMIT"
python3 -I -B -c "import sys; sys.path.insert(0, '$P2'); import depense; sys.exit(depense.main(sys.argv[1:]))" projeter "$ETAT"
if [ "$QUOI" = creation ]; then cat <<FIN
Commande de création à lancer par la session (jetons lus depuis l'environnement, jamais écrits) :
GO_ID=GO-2026-11-04-04 vastai create instance $CIBLE --image pytorch/pytorch:2.9.1-cuda12.8-cudnn9-runtime --disk 120 \\
  --env "-e COMMIT=$COMMIT -e COMMIT_CODE=$CODE -e PRIX_HEURE_USD=$PRIX -e PRIX_STOCKAGE_HEURE_USD=$STOCK -e ECHEANCE_UTC_S=$ECH -e GH_TOKEN=\$GH_TOKEN -e HF_TOKEN=\$HF_TOKEN -e DEPOT_URL=https://github.com/lciric/controle-ia-travail.git" \\
  --args bash -c "\$(cat scripts/amorce_instance_sparks_exp7_nul_v3.sh)"
Avant la création : tir réel de la minuterie (R-1477) ; image : curl et git présents (l'amorce refuse sinon).
FIN
elif [ "$QUOI" = redemarrage ]; then
case "$CIBLE" in ''|*[!0-9]*) echo "identifiant d'instance : chiffres seuls (R10)" >&2; exit 2;; esac
cat <<FIN
Redémarrage sur ordre écrit :
1. écrire ordres/ordre-NNN.json (numéro neuf ; deja_usd = dépense cumulée de l'état ; copie : cas, premier, copie_minutes ;
   causal : ordres/causal/cle-ouverte-v1.json et ordres/causal/reponses/<lecteur>/<cas>/reponse-v2.json, scellés) sur la
   branche calcul/sparks-exp7-nul-v3-ordres, committer, pousser ;
2. GO_ID=GO-2026-11-04-04 vastai start instance $CIBLE
3. copie : vastai copy $CIBLE:/root/sparks/lots/lot-NNN/ <DOSSIER_LOCAL_HORS_SERVI>, puis sha256sum -c MANIFESTE-LOT.txt dans ce dossier,
   pendant la fenêtre de copie_minutes ; le conteneur sort seul ensuite ;
4. causal ou fin : la machine se détruit elle-même (minuterie, après poussée vérifiée) ; contrôle par la session.
Repli de destruction par la session : vastai destroy instance $CIBLE -y (sans -y, vastai 1.8.3 ne détruit rien, R-1482) ;
aucune sortie brute de vastai affichée ni journalisée (R-1480) ; consigné dans registres/arrets.md.
FIN
else echo "creation ou redemarrage" >&2; exit 2; fi
