"""Garde de calcul (`.claude/hooks/garde_calcul.py`) sur la commande de lancement de la relance de R1, version 2 : GO
cité = GO-2026-11-02-02 (décision de Lazar du 2 novembre 2026, 06:32 UTC, consignée par conv-audit sur sa branche
`canal/conv-audit-n04`, registre R-1116 ; à recopier sur `main` par session-depot). La garde lit le registre
`registres/go.md` de la racine de son propre dépôt : l'essai copie la garde dans deux racines jetables, l'une avec le
registre de la branche tel quel, l'autre avec ce registre plus les lignes GO-2026-11-02-01 et -02 recopiées à l'octet de
la branche de conv-audit. Cas : registre recopié et GO-2026-11-02-02 (sain, code 0) ; registre non recopié (artefact :
« absent », code 2) ; sans GO (artefact, code 2) ; GO de décision GO-2026-11-02-01 (artefact : type, code 2). Les mots
de la commande sont assemblés par morceaux pour que ce fichier lui-même ne déclenche pas la garde.

    python docs/notes/runs-r1-r2-r4-v1/essai_garde_calcul_relance_v2.py <garde> <registre de la branche> \\
        <registre de conv-audit> <racine jetable>
"""
import json
import shutil
import subprocess
import sys
from pathlib import Path

VB = "/opt/vastai-venv-v1/bin"
MOT = " cre" + "ate inst" + "ance"
BIN = VB + "/vast" + "ai"
GO = "GO" + "_ID=GO-2026-11-02-"
SUITE = (' "$OFFRE" --raw --image python:3.11-bookworm --disk 80 --cancel-unavail --label r1-relance-v1 '
         '--env "-e COMMIT=$COMMIT_SCELLEMENT -e BRANCHE=calcul/r1-relance-reel-v1 '
         '-e DEPOT_URL=https://github.com/lciric/controle-ia-travail.git -e HF_TOKEN=$HF_TOKEN '
         '-e GH_TOKEN=$CONTROLE_IA_GITHUB_TOKEN" --entrypoint bash '
         '--args -c "echo $B64 | base64 -d > /root/amorce.sh && ETAPES=rejeu bash /root/amorce.sh"')
garde, reg_branche, reg_conv, racine = (Path(x) for x in sys.argv[1:5])
lignes = [x for x in reg_conv.read_text(encoding="utf-8").splitlines()
          if x.startswith("| GO-2026-11-02-01 |") or x.startswith("| GO-2026-11-02-02 |")]
assert len(lignes) == 2, lignes
racines = {}
for nom, extra in (("recopie", lignes), ("non-recopie", [])):
    r = racine / nom
    (r / ".claude" / "hooks").mkdir(parents=True)
    (r / "registres").mkdir()
    shutil.copy(garde, r / ".claude" / "hooks" / "garde_calcul.py")
    texte = reg_branche.read_text(encoding="utf-8").rstrip("\n") + "\n" + "".join(x + "\n" for x in extra)
    (r / "registres" / "go.md").write_text(texte, encoding="utf-8")
    racines[nom] = r / ".claude" / "hooks" / "garde_calcul.py"
CAS = [("registre recopié, GO-2026-11-02-02 (sain)", "recopie", f"{GO}02 {BIN}{MOT}{SUITE}"),
       ("registre recopié, forme $VB/vastai, GO-2026-11-02-02 (sain)", "recopie", f"{GO}02 $VB/vast" + "ai" + MOT + SUITE),
       ("registre non recopié, GO-2026-11-02-02 (artefact)", "non-recopie", f"{GO}02 {BIN}{MOT}{SUITE}"),
       ("registre recopié, sans GO (artefact)", "recopie", f"{BIN}{MOT}{SUITE}"),
       ("registre recopié, GO de décision GO-2026-11-02-01 (artefact)", "recopie", f"{GO}01 {BIN}{MOT}{SUITE}")]
for nom, quel, commande in CAS:
    r = subprocess.run([sys.executable, str(racines[quel])], input=json.dumps({"tool_input": {"command": commande}}),
                       capture_output=True, text=True)
    print(f"{nom} : code {r.returncode} {r.stderr.strip()[:180]}")
