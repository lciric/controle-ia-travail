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
WT_DR = SCRATCH / "lecture-dr"

gh_tok = subprocess.check_output(["gh", "auth", "token"], text=True, timeout=20).strip()
vk = Path.home() / ".config" / "vastai" / "vast_api_key"
vast_key = os.environ.get("VAST_API_KEY", "").strip() or vk.read_text("utf-8").strip()

def mask(s: str) -> str:
    for sec in (gh_tok, vast_key):
        if sec and len(sec) >= 8:
            s = s.replace(sec, "***")
    return re.sub(r"(gh[opsu]_|github_pat_|hf_)[A-Za-z0-9_]{8,}", r"\1***", s)

# 1. État de l'instance 62647167 et de la branche calcul/sondes-v2-epreuve-plantee-v4-suite
print("=== 1. ÉTAT VAST.AI 62647167 ET BRANCHE SUITE SONDES V2 ===")
req = urllib.request.Request(
    "https://console.vast.ai/api/v0/instances/",
    headers={"Authorization": f"Bearer {vast_key}", "Accept": "application/json"},
)
with urllib.request.urlopen(req, timeout=25) as resp:
    insts = json.loads(resp.read().decode("utf-8")).get("instances", [])

ids_vast = sorted(str(i.get("id")) for i in insts)
print("Instances Vast actives/présentes:", ids_vast)
i64 = next((i for i in insts if str(i.get("id")) == "62647167"), None)
if i64:
    print(f"62647167: status={i64.get('actual_status')} | cpu={i64.get('cpu_util')}% | mem={i64.get('mem_usage')}Go")
    try:
        logs = subprocess.check_output(
            [str(VAST_EXE), "logs", "62647167"],
            env={**os.environ, "VAST_API_KEY": vast_key, "PYTHONUTF8": "1"},
            text=True, timeout=25, stderr=subprocess.STDOUT,
        )
        print(mask("\n".join(logs.splitlines()[-15:])))
    except Exception as e:
        print("Logs info:", mask(repr(e)))
else:
    print("62647167: ABSENTE (terminée et autodétruite !)")

ls_suite = subprocess.check_output(
    ["git", "-C", str(REPO), "ls-remote", "origin", "refs/heads/calcul/sondes-v2-epreuve-plantee-v4-suite"],
    text=True,
).strip()
print("Branche suite sur GitHub:", ls_suite or "(pas encore poussée)")
if ls_suite:
    subprocess.run(
        ["git", "-C", str(REPO), "fetch", "origin", "calcul/sondes-v2-epreuve-plantee-v4-suite"],
        check=True,
    )
    f_suite = subprocess.check_output(
        ["git", "-C", str(REPO), "ls-tree", "-r", "--name-only", "FETCH_HEAD"],
        text=True,
    ).splitlines()
    et_json = [f for f in f_suite if "etalon/rapport-monde-plante-v4-etalon-" in f and f.endswith(".json")]
    autres = [f for f in f_suite if "rapport-monde-plante-v4-etalon-" not in f]
    print(f"Rapports étalon sur la branche suite: {len(et_json)} (attendu: 75) | Autres fichiers: {autres}")

# 2. Suivi non intrusif du journal lecteur Barreau 8 (noms et tailles seuls, zéro lecture de sortie)
print("\n=== 2. JOURNAL LECTEUR BARREAU 8 (NON INTRUSIF) ===")
j_b8 = SCRATCH / "journal-lecture-sondes-barreau8-v1"
if not j_b8.exists():
    print("journal-lecture-sondes-barreau8-v1 : non créé (en attente d'étape 0)")
else:
    for fp in sorted(j_b8.iterdir()):
        info = f"  {fp.name}: {fp.stat().st_size} octets"
        if fp.suffix in (".pid", ".code", ".nom-de-course") and fp.stat().st_size <= 64:
            info += f" -> {fp.read_text('utf-8', errors='replace').strip()!r}"
        print(info)

# 3. Lecture des consignes post-course dans ordre-de-lancement-dose-reponse-v6-scelle.md
print("\n=== 3. ORDRE DE LANCEMENT V6 SCELLÉ (ÉTAPES APRÈS LA COURSE) ===")
ordre_txt = subprocess.check_output(
    ["git", "-C", str(REPO), "show", "origin/main:docs/notes/code-dose-reponse-consigne-cachee-v1/ordre-de-lancement-dose-reponse-v6-scelle.md"],
).decode("utf-8")
lignes_o = ordre_txt.splitlines()
print(f"Total lignes ordre v6: {len(lignes_o)}")
if len(lignes_o) <= 320:
    print(ordre_txt)
else:
    for idx, lg in enumerate(lignes_o, 1):
        if lg.startswith("#"):
            print(f"  L{idx}: {lg}")
    print("\n--- Dernières 240 lignes de ordre-de-lancement-dose-reponse-v6-scelle.md ---")
    print("\n".join(lignes_o[-240:]))

# 4. Interface exacte de lancer_lecteur_texte_dose_reponse_v2.sh et lecteur_texte_dose_reponse_v2.py
print("\n=== 4. SCRIPT lancer_lecteur_texte_dose_reponse_v2.sh ===")
print((WT_DR / "scripts/lancer_lecteur_texte_dose_reponse_v2.sh").read_text("utf-8"))

print("\n=== 5. CLI DE lecteur_texte_dose_reponse_v2.py ===")
lt_py = (WT_DR / "scripts/lecteur_texte_dose_reponse_v2.py").read_text("utf-8").splitlines()
print("\n".join(lt_py[:45]))
print("...\n" + "\n".join(lt_py[-65:]))

# 6. Dernière version de qui-a-lu-quoi sur origin/main et G0-critere-3-designation-course-v1.md
reg_files = subprocess.check_output(
    ["git", "-C", str(REPO), "ls-tree", "--name-only", "origin/main:registres"], text=True
).splitlines()
print("\n=== 6. VERSIONS QUI-A-LU-QUOI SUR ORIGIN/MAIN ===")
print([f for f in reg_files if "qui-a-lu-quoi" in f])

c3_txt = subprocess.check_output(
    ["git", "-C", str(REPO), "show", "origin/main:prereg/G0-critere-3-designation-course-v1.md"],
).decode("utf-8").splitlines()
print(f"\n=== 7. APERÇU G0-critere-3-designation-course-v1.md ({len(c3_txt)} lignes) ===")
print("\n".join(c3_txt[:120]))
