import json
import os
import subprocess
import urllib.request
from pathlib import Path

REPO = Path(r"C:\Users\lciri\OneDrive\Documents\controle-ia-travail")
SCRATCH = Path(
    r"C:\Users\lciri\.gemini\antigravity-cli\brain"
    r"\cd7c89b9-9752-4dac-b846-2c58efd89737\scratch"
)
PY_EXE = SCRATCH / "venv-py314" / "Scripts" / "python.exe"
WT_DR = SCRATCH / "lecture-dr"

# 1. Coup d'œil rapide à 62647167, à la branche suite et au PID 8800 de Barreau 8
vk = Path.home() / ".config" / "vastai" / "vast_api_key"
vast_key = os.environ.get("VAST_API_KEY", "").strip() or vk.read_text("utf-8").strip()
req = urllib.request.Request(
    "https://console.vast.ai/api/v0/instances/",
    headers={"Authorization": f"Bearer {vast_key}", "Accept": "application/json"},
)
with urllib.request.urlopen(req, timeout=20) as resp:
    insts = json.loads(resp.read().decode("utf-8")).get("instances", [])
i64 = next((i for i in insts if str(i.get("id")) == "62647167"), None)
print("=== 1. SUIVI RAPIDE 62647167 & BARREAU 8 ===")
print("62647167:", f"status={i64.get('actual_status')} cpu={i64.get('cpu_util')}%" if i64 else "ABSENTE (terminée et autodétruite !)")
ls_suite = subprocess.check_output(
    ["git", "-C", str(REPO), "ls-remote", "origin", "refs/heads/calcul/sondes-v2-epreuve-plantee-v4-suite"],
    text=True,
).strip()
print("Branche suite sondes v2:", ls_suite or "(pas encore poussée)")

j_b8 = SCRATCH / "journal-lecture-sondes-barreau8-v1"
if j_b8.exists():
    verrou = (j_b8 / "3-lecture.verrou").exists()
    code_f = j_b8 / "3-lecture.code"
    err_sz = (j_b8 / "3-lecture.erreurs").stat().st_size if (j_b8 / "3-lecture.erreurs").exists() else -1
    print(f"Barreau 8 (PID 8800): en_cours={verrou} | 3-lecture.erreurs={err_sz} octets | code={code_f.read_text().strip() if code_f.is_file() else 'en cours'}")

# 2.Lire les sections Seuil / Plan / Critères gelés de prereg/T0.6-organisme-consigne-cachee-dose-reponse-v1.md
print("\n=== 2. PRÉENREGISTREMENT T0.6-organisme-consigne-cachee-dose-reponse-v1.md ===")
prereg_txt = (WT_DR / "prereg/T0.6-organisme-consigne-cachee-dose-reponse-v1.md").read_text("utf-8").splitlines()
print(f"Total lignes: {len(prereg_txt)}")
for idx, lg in enumerate(prereg_txt, 1):
    if lg.startswith("#"):
        print(f"  L{idx}: {lg}")
# Afficher depuis Hypothèse / Prédiction / Métrique / Seuil / Critères gelés jusqu'à la fin
start_idx = next((i for i, lg in enumerate(prereg_txt) if lg.startswith("## Hypothèse") or lg.startswith("## Prédiction")), max(0, len(prereg_txt) - 220))
print("\n".join(prereg_txt[start_idx:]))

# 3. Fin de G0-critere-3-designation-course-v1.md (lignes 120 à 197 : table K complète)
print("\n=== 3. FIN DE G0-critere-3-designation-course-v1.md (L121-fin) ===")
c3_txt = (WT_DR / "prereg/G0-critere-3-designation-course-v1.md").read_text("utf-8").splitlines()
print("\n".join(c3_txt[120:]))

# 4. Modèles de verdicts récents dans docs/verdicts/ sur origin/main
verdicts_list = subprocess.check_output(
    ["git", "-C", str(REPO), "ls-tree", "--name-only", "origin/main:docs/verdicts"], text=True
).splitlines()
print("\n=== 4. FICHIERS DANS docs/verdicts/ SUR ORIGIN/MAIN ===")
print(verdicts_list[-20:])

# 5. Pré-contrôle verifier-code du lecteur du texte dans lecture-dr (sans toucher aux données)
print("\n=== 5. PRÉ-CONTRÔLE verifier-code DU LECTEUR DU TEXTE ===")
is_sh = subprocess.check_output(["git", "-C", str(WT_DR), "rev-parse", "--is-shallow-repository"], text=True).strip()
print("is-shallow-repository:", is_sh)
r_vc = subprocess.run(
    [str(PY_EXE), "-P", "-B", "scripts/lecteur_texte_dose_reponse_v2.py", "verifier-code", "--racine", "."],
    cwd=str(WT_DR),
    env={**os.environ, "PYTHONPATH": str(WT_DR / "src"), "PYTHONUTF8": "1"},
    capture_output=True, text=True,
)
print(f"verifier-code rc={r_vc.returncode}\n  out={r_vc.stdout.strip()}\n  err={r_vc.stderr.strip()}")
