import hashlib
import json
import os
import shutil
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

# 1. Suivi en direct de 62647167 (sondes v2) et du PID 8800 (Barreau 8)
print("=== 1. SUIVI 62647167 & BARREAU 8 ===")
vk = Path.home() / ".config" / "vastai" / "vast_api_key"
vast_key = os.environ.get("VAST_API_KEY", "").strip() or vk.read_text("utf-8").strip()
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
        print("  dernières lignes:", " | ".join(logs.splitlines()[-3:]))
    except Exception:
        pass
else:
    print("62647167: ABSENTE (terminée et autodétruite !)")

ls_suite = subprocess.check_output(
    ["git", "-C", str(REPO), "ls-remote", "origin", "refs/heads/calcul/sondes-v2-epreuve-plantee-v4-suite"],
    text=True,
).strip()
print("Branche suite sondes v2:", ls_suite or "(calcul en cours)")

j_b8 = SCRATCH / "journal-lecture-sondes-barreau8-v1"
if j_b8.exists():
    verrou = (j_b8 / "3-lecture.verrou").exists()
    code_f = j_b8 / "3-lecture.code"
    err_sz = (j_b8 / "3-lecture.erreurs").stat().st_size if (j_b8 / "3-lecture.erreurs").exists() else -1
    sort_sz = (j_b8 / "3-lecture.sortie").stat().st_size if (j_b8 / "3-lecture.sortie").exists() else -1
    print(
        f"Barreau 8 (PID 8800): en_cours={verrou} | code={code_f.read_text().strip() if code_f.is_file() else 'en cours'} "
        f"| sortie={sort_sz}o | erreurs={err_sz}o"
    )

# 2. Ajouter les sous-dossiers sûrs de docs/ dans lecture-dr (sans organisme-boucle-reelle-v1) et valider verifier-code
print("\n=== 2. AJOUT SPARSE SÛR DANS lecture-dr ET VALIDATION verifier-code ===")
gitdir_wt = Path(subprocess.check_output(["git", "-C", str(WT_DR), "rev-parse", "--git-dir"], text=True).strip())
if not gitdir_wt.is_absolute():
    gitdir_wt = (WT_DR / gitdir_wt).resolve()
sp_file = gitdir_wt / "info" / "sparse-checkout"
lignes_sp = sp_file.read_text("utf-8").splitlines()
ajouts = [
    "/docs/decisions/",
    "/docs/verdicts/",
    "/docs/sources/",
    "/docs/notes/code-dose-reponse-consigne-cachee-v1/",
]
# Ajouter aussi tout sous-dossier cité dans CODE-LECTEUR-DU-TEXTE-DOSE-REPONSE-*.json
for jf in (WT_DR / "registres/code-lecteur-du-texte-dose-reponse").glob("*.json"):
    d_code = json.loads(jf.read_text("utf-8"))
    for k_f in d_code.get("fichiers", {}):
        p_parent = "/" + str(Path(k_f).parent.as_posix()).strip("/") + "/"
        if p_parent != "//" and "|" not in p_parent and p_parent not in lignes_sp and p_parent not in ajouts:
            ajouts.append(p_parent)
    cl_p = d_code.get("contre_lecture")
    if isinstance(cl_p, str) and cl_p:
        p_parent = "/" + str(Path(cl_p).parent.as_posix()).strip("/") + "/"
        if "|" not in p_parent and p_parent not in lignes_sp and p_parent not in ajouts:
            ajouts.append(p_parent)

for a in ajouts:
    if a not in lignes_sp:
        lignes_sp.append(a)
sp_file.write_bytes(("\n".join(lignes_sp) + "\n").encode("utf-8"))
subprocess.run(
    ["git", "-c", "core.protectNTFS=false", "-C", str(WT_DR), "read-tree", "--reset", "-u", "HEAD"],
    check=True,
)
st_dr = subprocess.check_output(["git", "-C", str(WT_DR), "status", "--porcelain"], text=True).strip()
assert st_dr == "", f"lecture-dr non propre: {st_dr}"

r_vc = subprocess.run(
    [str(PY_EXE), "-P", "-B", "scripts/lecteur_texte_dose_reponse_v2.py", "verifier-code", "--racine", "."],
    cwd=str(WT_DR),
    env={**os.environ, "PYTHONPATH": str(WT_DR / "src"), "PYTHONUTF8": "1"},
    capture_output=True, text=True,
)
print(f"verifier-code rc={r_vc.returncode}")
print("  stdout:", r_vc.stdout.strip())
if r_vc.stderr.strip():
    print("  stderr:", r_vc.stderr.strip())
assert r_vc.returncode == 0, "verifier-code encore en échec"

# 3. Lire le code de src/controle_ia/dose_reponse/lecture_v2.py (zéro ouverture du résultat JSON !)
print("\n=== 3. CODE DE lecture_v2.py (SCHÉMA DU RÉSULTAT ET DE L'AUDIT R4) ===")
code_lv2 = (WT_DR / "src/controle_ia/dose_reponse/lecture_v2.py").read_text("utf-8")
print(code_lv2)

# 4. Préparer le dossier prêt-à-glisser pour le sous-agent neuf R13 (sans lire le JSON)
paquet = SCRATCH / "paquet-juge-r13-cout-dr"
paquet.mkdir(parents=True, exist_ok=True)
pieces_juge = [
    (WT_DR / "prereg/T0.6-organisme-consigne-cachee-dose-reponse-v1.md", "T0.6-organisme-consigne-cachee-dose-reponse-v1.md"),
    (WT_DR / "diag/20261126-082824-dose-reponse-lecture/lecture-cout-dose-reponse.json", "lecture-cout-dose-reponse.json"),
    (WT_DR / "runs/20261126-082824-dose-reponse-lecture/manifeste.json", "manifeste-20261126-082824-dose-reponse-lecture.json"),
]
print("\n=== 4. PAQUET PRÊT POUR LE JUGE NEUF R13 ===")
print("Dossier:", paquet)
for src_p, dst_name in pieces_juge:
    dst_p = paquet / dst_name
    shutil.copyfile(src_p, dst_p)
    h = hashlib.sha256(dst_p.read_bytes()).hexdigest()
    print(f"  {dst_name} ({dst_p.stat().st_size} octets) sha256={h}")
