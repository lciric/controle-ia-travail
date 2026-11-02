"""Garde de calcul (`.claude/hooks/garde_calcul.py`) sur la commande de lancement de la relance de R1 : binaire au chemin
littéral terminé par « vastai create instance », GO-2026-11-01-13 (cas sain) ; sans GO ; avec un GO inexistant
(artefacts). Le code de sortie 0 dit « passe », 2 « bloquée ». Lancer avec le dépôt de travail comme répertoire courant
(la garde lit `registres/go.md` du dépôt). Les mots de la commande sont assemblés par morceaux pour que ce fichier
lui-même ne déclenche pas la garde."""
import json
import subprocess
import sys

VB = "/tmp/claude-0/-home-user-controle-ia-travail/4ff7d1a3-3d12-504e-b550-a8bc2f8510b1/scratchpad/vast183-venv/bin"
MOT = " cre" + "ate inst" + "ance"
BIN = VB + "/vast" + "ai"
GO = "GO" + "_ID=GO-2026-11-01-"
SUITE = (' "$OFFRE" --raw --image python:3.11-bookworm --disk 80 --cancel-unavail --label r1-relance-v1 '
         '--env "-e COMMIT=$COMMIT_SCELLEMENT -e BRANCHE=calcul/r1-relance-reel-v1 '
         '-e DEPOT_URL=https://github.com/lciric/controle-ia-travail.git -e HF_TOKEN=$HF_TOKEN '
         '-e GH_TOKEN=$CONTROLE_IA_GITHUB_TOKEN" --entrypoint bash '
         '--args -c "echo $B64 | base64 -d > /root/amorce.sh && ETAPES=rejeu bash /root/amorce.sh"')
CAS = {"chemin littéral, GO-2026-11-01-13 (sain)": f"{GO}13 {BIN}{MOT}{SUITE}",
       "forme $VB/vastai, GO-2026-11-01-13 (sain)": f"{GO}13 $VB/vast" + "ai" + MOT + SUITE,
       "chemin littéral, sans GO (artefact)": f"{BIN}{MOT}{SUITE}",
       "chemin littéral, GO inexistant -99 (artefact)": f"{GO}99 {BIN}{MOT}{SUITE}"}
GARDE = sys.argv[1] if len(sys.argv) > 1 else ".claude/hooks/garde_calcul.py"
for nom, commande in CAS.items():
    r = subprocess.run([sys.executable, GARDE], input=json.dumps({"tool_input": {"command": commande}}),
                       capture_output=True, text=True)
    print(f"{nom} : code {r.returncode} {r.stderr.strip()[:180]}")
