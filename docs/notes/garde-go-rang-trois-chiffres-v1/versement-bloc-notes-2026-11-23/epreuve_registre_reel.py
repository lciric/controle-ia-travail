import json, subprocess, sys
HOOK = "/home/user/controle-ia-travail/.claude/hooks/garde_calcul.py"
VERBE = "vast" + "ai cre" + "ate instance 1"
for ident in ["GO-2026-11-22-117", "GO-2026-11-22-124", "GO-2026-11-22-75", "GO-2026-11-22-102",
              "GO-2026-11-22-1170", "GO-2026-11-22-115", "GO-2099-01-01-01"]:
    e = json.dumps({"tool_name": "Bash", "tool_input": {"command": f"GO_ID={ident} {VERBE}"}})
    r = subprocess.run([sys.executable, HOOK], input=e, capture_output=True, text=True)
    print(ident, "-> code", r.returncode, r.stderr.strip())
