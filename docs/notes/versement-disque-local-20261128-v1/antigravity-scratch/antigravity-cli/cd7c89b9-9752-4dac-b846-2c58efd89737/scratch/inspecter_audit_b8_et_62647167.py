import json
import os
import re
import subprocess
import urllib.request
from pathlib import Path

REPO = Path(r"C:\Users\lciri\OneDrive\Documents\controle-ia-travail")
SCRATCH = Path(
    r"C:\Users\lciri\.gemini\antigravity-cli\brain"
    r"\cd7c89b9-9752-4dac-b846-2c58efd89737\scratch"
)
VAST_EXE = SCRATCH / "venv-py314" / "Scripts" / "vastai.exe"
WT_B8 = SCRATCH / "wt-b8-puissance"
WT_DR = SCRATCH / "lecture-dr"

# 1. État de l'instance 62647167 (sondes v2, 72 cœurs) et de la branche suite
print("=== 1. ÉTAT VAST.AI 62647167 & SONDES V2 ===")
vk = Path.home() / ".config" / "vastai" / "vast_api_key"
vast_key = os.environ.get("VAST_API_KEY", "").strip() or vk.read_text("utf-8").strip()

def mask(txt: str) -> str:
    if vast_key:
        txt = txt.replace(vast_key, "***")
    return re.sub(r"(gh[opsu]_|github_pat_|hf_)[A-Za-z0-9_]{8,}", r"\1***", txt)

req = urllib.request.Request(
    "https://console.vast.ai/api/v0/instances/",
    headers={"Authorization": f"Bearer {vast_key}", "Accept": "application/json"},
)
with urllib.request.urlopen(req, timeout=20) as resp:
    insts = json.loads(resp.read().decode("utf-8")).get("instances", [])
i64 = next((i for i in insts if str(i.get("id")) == "62647167"), None)
if i64:
    print(f"62647167: status={i64.get('actual_status')} | cpu={i64.get('cpu_util')}% | mem={i64.get('mem_usage')}Go")
    try:
        logs = subprocess.check_output(
            [str(VAST_EXE), "logs", "62647167"],
            env={**os.environ, "VAST_API_KEY": vast_key, "PYTHONUTF8": "1"},
            text=True, timeout=20, stderr=subprocess.STDOUT,
        )
        print("  dernières lignes:", mask(" | ".join(logs.splitlines()[-5:])))
    except Exception:
        pass
else:
    print("62647167: ABSENTE (terminée et autodétruite !)")

ls_suite = subprocess.check_output(
    ["git", "-C", str(REPO), "ls-remote", "origin", "refs/heads/calcul/sondes-v2-epreuve-plantee-v4-suite"],
    text=True,
).strip()
print("Branche suite sondes v2:", ls_suite or "(calcul en cours)")

# 2. Vérifier le booléen d'audit R4 du lecteur du texte (sans ouvrir aucune aire ni dose jugée)
p_aud_lt = WT_DR / "diag/20261126-095224-lecteur-du-texte-dose-reponse/audit-r4-lecteur-du-texte-dose-reponse.json"
aud_lt = json.loads(p_aud_lt.read_text("utf-8"))
print("\n=== 2. BOOLÉEN AUDIT R4 DU LECTEUR DU TEXTE (SANS CHIFFRES) ===")
print("Clés audit-r4 lecteur texte:", sorted(aud_lt.keys()))
for k in ("declenche", "motifs", "declencheurs", "conditions_concernees", "echantillons"):
    if k in aud_lt:
        v = aud_lt[k]
        if isinstance(v, dict):
            print(f"  {k}: dict keys={sorted(v.keys())}")
        else:
            print(f"  {k}: {v}")

# 3. Lire les règles exactes de l'audit de symétrie (d3) dans Barreau 8 (texte scellé + additif 1 + additif 2)
print("\n=== 3. RÈGLES EXACTES DE L'AUDIT DE SYMÉTRIE BARREAU 8 ===")
for rel_f in (
    "prereg/lecture-sondes-barreau8-v1.md",
    "prereg/lecture-sondes-barreau8-v1-addendum-organisme-change-v1.md",
    "prereg/lecture-sondes-barreau8-v1-addendum-2-format-entrees-v1.md",
):
    lns = (WT_B8 / rel_f).read_text("utf-8").splitlines()
    print(f"\n*** {rel_f} ({len(lns)} lignes) ***")
    for idx, ln in enumerate(lns):
        if any(w in ln.lower() for w in ("audit de sym", "auditeur", "liste fermée", "(d3)", "plancher haut")):
            deb, fin = max(0, idx - 2), min(len(lns), idx + 22)
            print(f"[L{deb+1}..L{fin}]\n" + "\n".join(lns[deb:fin]) + "\n---")
