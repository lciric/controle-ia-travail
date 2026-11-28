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

# 1. État de l'instance Vast.ai 62647167 et de la branche suite sondes v2
print("=== 1. ÉTAT VAST.AI 62647167 & BRANCHE SUITE SONDES V2 ===")
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
print("Instances Vast présentes:", sorted(str(i.get("id")) for i in insts))
i64 = next((i for i in insts if str(i.get("id")) == "62647167"), None)
if i64:
    print(f"62647167: status={i64.get('actual_status')} | cpu={i64.get('cpu_util')}% | mem={i64.get('mem_usage')}Go")
    try:
        logs = subprocess.check_output(
            [str(VAST_EXE), "logs", "62647167"],
            env={**os.environ, "VAST_API_KEY": vast_key, "PYTHONUTF8": "1"},
            text=True, timeout=20, stderr=subprocess.STDOUT,
        )
        print("  dernières lignes:", mask(" | ".join(logs.splitlines()[-6:])))
    except Exception:
        pass
else:
    print("62647167: ABSENTE (terminée et autodétruite !)")

ls_suite = subprocess.check_output(
    ["git", "-C", str(REPO), "ls-remote", "origin", "refs/heads/calcul/sondes-v2-epreuve-plantee-v4-suite"],
    text=True,
).strip()
print("Branche suite sondes v2:", ls_suite or "(calcul en cours)")
if ls_suite:
    subprocess.run(["git", "-C", str(REPO), "fetch", "origin", "calcul/sondes-v2-epreuve-plantee-v4-suite"], check=True)
    f_suite = subprocess.check_output(["git", "-C", str(REPO), "ls-tree", "-r", "--name-only", "FETCH_HEAD"], text=True).splitlines()
    et_json = [f for f in f_suite if "etalon/rapport-monde-plante-v4-etalon-" in f and f.endswith(".json")]
    autres = [f for f in f_suite if "rapport-monde-plante-v4-etalon-" not in f]
    print(f"Rapports étalon poussés: {len(et_json)} | Autres fichiers: {autres}")

# 2. Suite de notice-lecture-sondes-v7.md (L88 à la fin : commande exacte de l'audit R4 Barreau 8)
print("\n=== 2. FIN DE notice-lecture-sondes-v7.md (SECTION 5 AUDIT) ===")
not_p = WT_B8 / "docs/notes/barreau8-cote-moniteurs-sorties-v1/notice-lecture-sondes-v7.md"
lns_n = not_p.read_text("utf-8").splitlines()
print("\n".join(lns_n[87:]))

# 3. Sous-commandes CLI exactes de lecture_sondes_v6.py
print("\n=== 3. CLI DE lecture_sondes_v6.py ===")
lv6 = (WT_B8 / "src/controle_ia/barreau8_moniteurs/lecture_sondes_v6.py").read_text("utf-8").splitlines()
print("\n".join(lv6[-95:]))
