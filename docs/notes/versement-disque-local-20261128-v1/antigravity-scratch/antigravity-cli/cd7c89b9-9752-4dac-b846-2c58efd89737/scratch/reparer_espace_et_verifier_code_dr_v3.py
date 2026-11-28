import hashlib
import json
import os
import re
import shutil
import stat
import subprocess
import urllib.request
from pathlib import Path

REPO = Path(r"C:\Users\lciri\OneDrive\Documents\controle-ia-travail")
SCRATCH = Path(
    r"C:\Users\lciri\.gemini\antigravity-cli\brain"
    r"\cd7c89b9-9752-4dac-b846-2c58efd89737\scratch"
)
PY_EXE = SCRATCH / "venv-py314" / "Scripts" / "python.exe"
VAST_EXE = SCRATCH / "venv-py314" / "Scripts" / "vastai.exe"
WT_DR = SCRATCH / "lecture-dr"

# 1. Préparer EN PREMIER le paquet (~130 Ko) pour le sous-agent neuf R13 (zéro lecture des valeurs)
paquet = SCRATCH / "paquet-juge-r13-cout-dr"
paquet.mkdir(parents=True, exist_ok=True)
print("=== 1. PAQUET PRÊT POUR LE JUGE NEUF R13 ===")
print("Dossier:", paquet)
for src_p, dst_name in [
    (
        WT_DR / "prereg/T0.6-organisme-consigne-cachee-dose-reponse-v1.md",
        "T0.6-organisme-consigne-cachee-dose-reponse-v1.md",
    ),
    (
        WT_DR / "diag/20261126-082824-dose-reponse-lecture/lecture-cout-dose-reponse.json",
        "lecture-cout-dose-reponse.json",
    ),
    (
        WT_DR / "runs/20261126-082824-dose-reponse-lecture/manifeste.json",
        "manifeste-20261126-082824-dose-reponse-lecture.json",
    ),
]:
    dst_p = paquet / dst_name
    shutil.copyfile(src_p, dst_p)
    h = hashlib.sha256(dst_p.read_bytes()).hexdigest()
    print(f"  {dst_name} ({dst_p.stat().st_size}o) sha256={h}")
print("PAQUET_R13_PRET: OUI", flush=True)

# 2. Suivi non intrusif de Barreau 8 (PID 8800) et de Vast.ai 62647167
print("\n=== 2. ÉTAT BARREAU 8 (PID 8800) & INSTANCE 62647167 ===")
j_b8 = SCRATCH / "journal-lecture-sondes-barreau8-v1"
if j_b8.exists():
    verrou = (j_b8 / "3-lecture.verrou").exists()
    code_f = j_b8 / "3-lecture.code"
    err_sz = (j_b8 / "3-lecture.erreurs").stat().st_size if (j_b8 / "3-lecture.erreurs").exists() else -1
    sort_sz = (j_b8 / "3-lecture.sortie").stat().st_size if (j_b8 / "3-lecture.sortie").exists() else -1
    code_val = code_f.read_text("utf-8").strip() if code_f.is_file() else "en cours"
    print(f"Barreau 8: verrou={verrou} | code={code_val} | sortie={sort_sz}o | erreurs={err_sz}o")

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
print("Branche suite sondes v2:", ls_suite or "(calcul en cours)", flush=True)

# 3. Compléter uniquement les petits dossiers de notes demandés par verifier-code (jamais docs/sources)
print("\n=== 3. VALIDATION DE verifier-code DANS lecture-dr ===")
cone_dirs = [
    "src",
    "scripts",
    "tests",
    "prereg",
    "brouillons",
    "registres",
    ".claude",
    "docs/decisions",
    "docs/verdicts",
    "docs/notes/code-dose-reponse-consigne-cachee-v1",
    "docs/notes/piece-mots-et-cout-v1",
    "donnees/20261125-093202-dose-reponse",
    "donnees/20261124-144844-banque-dose-reponse-extraction-v2",
    "donnees/20261007-082440-t05-extraction",
    "diag/20261125-093202-dose-reponse",
    "diag/20261126-082824-dose-reponse-lecture",
    "diag/20261006-134235-t05-corpus",
    "runs/20261125-093202-dose-reponse",
    "runs/20261126-082824-dose-reponse-lecture",
]

for essai in range(1, 7):
    subprocess.run(
        ["git", "-c", "core.protectNTFS=false", "-C", str(WT_DR), "sparse-checkout", "set", "--cone", *cone_dirs],
        check=True,
    )
    subprocess.run(
        ["git", "-c", "core.protectNTFS=false", "-C", str(WT_DR), "read-tree", "--reset", "-u", "HEAD"],
        check=True,
    )
    r_vc = subprocess.run(
        [str(PY_EXE), "-P", "-B", "scripts/lecteur_texte_dose_reponse_v2.py", "verifier-code", "--racine", "."],
        cwd=str(WT_DR),
        env={**os.environ, "PYTHONPATH": str(WT_DR / "src"), "PYTHONUTF8": "1"},
        capture_output=True, text=True,
    )
    if r_vc.returncode == 0:
        print(f"verifier-code OK (essai {essai}) : {r_vc.stdout.strip()}")
        break
    m_abs = re.search(r"lecture-dr[\\/](.+?) absent", r_vc.stderr)
    if m_abs:
        rel_miss = m_abs.group(1).replace("\\", "/")
        par_miss = Path(rel_miss).parent.as_posix()
        assert not par_miss.startswith("docs/sources") and "|" not in par_miss, f"Chemin risqué: {par_miss}"
        if par_miss not in cone_dirs:
            print(f"  ajout sous-dossier requis: {par_miss}")
            cone_dirs.append(par_miss)
            continue
    print("verifier-code ÉCHEC:", r_vc.returncode, r_vc.stderr.strip())
    break

st_dr = subprocess.check_output(["git", "-C", str(WT_DR), "status", "--porcelain"], text=True).strip()
usage = shutil.disk_usage("C:\\")
print(f"lecture-dr propre={st_dr == ''} | C: libre={usage.free / (1024**3):.2f} Gio")

# 4. Afficher le code de lecture_v2.py (pour vérifier le schéma de la clé audit sans ouvrir le JSON)
print("\n=== 4. CODE DE src/controle_ia/dose_reponse/lecture_v2.py ===")
print((WT_DR / "src/controle_ia/dose_reponse/lecture_v2.py").read_text("utf-8"))
