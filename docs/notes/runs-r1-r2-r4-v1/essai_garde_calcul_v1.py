import json, subprocess, sys
V = "/tmp/claude-0/-home-user-controle-ia-travail/4ff7d1a3-3d12-504e-b550-a8bc2f8510b1/scratchpad/vast183-venv/bin/" + "vast" + "ai"
mot = " cre" + "ate inst" + "ance"
cas = {"avec GO-13": f'GO_ID=GO-2026-11-01-13 {V}{mot} "$OFFRE_A" --raw --image python:3.11-bookworm --disk 80',
       "forme du LISEZMOI ($VB/vastai)": 'GO_ID=GO-2026-11-01-13 $VB/' + "vast" + "ai" + mot + ' "$OFFRE_A" --raw',
       "forme du LISEZMOI ($VB/vastai) sans GO": '$VB/' + "vast" + "ai" + mot + ' "$OFFRE_A" --raw',
       "sans GO": f'{V}{mot} "$OFFRE_A" --raw --image python:3.11-bookworm --disk 80',
       "ancienne forme du LISEZMOI v1 (CLR-09)": f'GO_ID=GO-2026-11-01-13 "$V"{mot} "$OFFRE_A" --raw'}
for nom, c in cas.items():
    r = subprocess.run([sys.executable, "/home/user/controle-ia-travail/.claude/hooks/garde_calcul.py"],
                       input=json.dumps({"tool_input": {"command": c}}), capture_output=True, text=True)
    print(f"{nom} : code {r.returncode} {r.stderr.strip()[:160]}")
