import hashlib
import json
import os
import re
import subprocess
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(r"C:\Users\lciri\OneDrive\Documents\controle-ia-travail")
SCRATCH = Path(
    r"C:\Users\lciri\.gemini\antigravity-cli\brain"
    r"\cd7c89b9-9752-4dac-b846-2c58efd89737\scratch"
)
PY_EXE = SCRATCH / "venv-py314" / "Scripts" / "python.exe"
WT_B8 = SCRATCH / "wt-b8-puissance"
WT_DR_LECT = SCRATCH / "lecture-dr"

# 0. Coup d'œil rapide à l'instance 62647167 et à la branche suite
vk = Path.home() / ".config" / "vastai" / "vast_api_key"
vast_key = os.environ.get("VAST_API_KEY", "").strip() or vk.read_text("utf-8").strip()
req = urllib.request.Request(
    "https://console.vast.ai/api/v0/instances/",
    headers={"Authorization": f"Bearer {vast_key}", "Accept": "application/json"},
)
with urllib.request.urlopen(req, timeout=20) as resp:
    insts = json.loads(resp.read().decode("utf-8")).get("instances", [])
i64 = next((i for i in insts if str(i.get("id")) == "62647167"), None)
print("62647167:", f"running (cpu={i64.get('cpu_util')}%)" if i64 else "ABSENTE (terminée et autodétruite !)", flush=True)
ls_suite = subprocess.check_output(
    ["git", "-C", str(REPO), "ls-remote", "origin", "refs/heads/calcul/sondes-v2-epreuve-plantee-v4-suite"],
    text=True,
).strip()
print("Branche suite:", ls_suite or "(calcul en cours)", flush=True)

# 1. Vérification ultra-rapide (< 2 s) des SEULS fichiers texte du bordereau B8 si le lecteur ne tourne pas déjà
j_b8 = SCRATCH / "journal-lecture-sondes-barreau8-v1"
if not j_b8.exists():
    bord_liv = WT_B8 / "versement/20261124-122719-rejeu-activations-voie-a/sortie-passe/livraison/bordereau-livraison-passe-barreau8-v1.json"
    hashes_b8 = set(re.findall(r"\b[0-9a-f]{64}\b", bord_liv.read_text("utf-8")))
    fixes = 0
    for ext in ("*.json", "*.jsonl", "*.md", "*.txt", "*.csv"):
        for f in (WT_B8 / "versement").rglob(ext):
            raw = f.read_bytes()
            if hashlib.sha256(raw).hexdigest() not in hashes_b8 and b"\r\n" in raw:
                raw_lf = raw.replace(b"\r\n", b"\n")
                if hashlib.sha256(raw_lf).hexdigest() in hashes_b8:
                    f.write_bytes(raw_lf)
                    fixes += 1
    subprocess.run(["git", "-C", str(WT_B8), "update-index", "--refresh"], check=False, capture_output=True)
    st_b8 = subprocess.check_output(["git", "-C", str(WT_B8), "status", "--porcelain", "--untracked-files=all"], text=True).strip()
    assert st_b8 == "", f"wt-b8-puissance non vide : {st_b8}"
    print(f"WT_B8_PRET_RAPIDE_OK (corrections LF texte suppl.={fixes}, arbre vide, journal libre)", flush=True)
else:
    print("INFO_B8: journal-lecture-sondes-barreau8-v1 présent (lecteur déjà en cours, non touché)", flush=True)

# 2. Exécution unique en direct de lecture_v2 dans lecture-dr (~1 à 2 minutes sur processeur)
existants = list((WT_DR_LECT / "diag").glob("*-dose-reponse-lecture")) + list((WT_DR_LECT / "runs").glob("*-dose-reponse-lecture"))
assert not existants, f"Une lecture existe déjà : {existants}"

for sub in ("prereg", "brouillons", "registres"):
    p_sub = WT_DR_LECT / sub
    if not p_sub.exists():
        continue
    for sf in sorted(p_sub.rglob("*.sha256")):
        m = re.match(r"^([0-9a-f]{64})\s+\*?(.+)$", sf.read_text("utf-8").strip().splitlines()[0])
        if m:
            cible = sf.parent / Path(m.group(2).strip()).name
            if cible.is_file() and hashlib.sha256(cible.read_bytes()).hexdigest() != m.group(1):
                raw_lf = cible.read_bytes().replace(b"\r\n", b"\n")
                assert hashlib.sha256(raw_lf).hexdigest() == m.group(1), f"Sceau invalide: {cible}"
                cible.write_bytes(raw_lf)

subprocess.run(["git", "-C", str(WT_DR_LECT), "update-index", "--refresh"], check=False, capture_output=True)
run_lect_id = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S") + "-dose-reponse-lecture"
gitdir_wt = Path(subprocess.check_output(["git", "-C", str(WT_DR_LECT), "rev-parse", "--git-dir"], text=True).strip())
if not gitdir_wt.is_absolute():
    gitdir_wt = (WT_DR_LECT / gitdir_wt).resolve()
sp_file = gitdir_wt / "info" / "sparse-checkout"
sp_file.write_bytes((sp_file.read_text("utf-8").rstrip("\n") + f"\n/diag/{run_lect_id}/\n/runs/{run_lect_id}/\n").encode("utf-8"))

assert subprocess.check_output(["git", "-C", str(WT_DR_LECT), "status", "--porcelain"], text=True).strip() == ""
print(f"\n>>> LANCEMENT EN DIRECT DE lecture_v2 ({run_lect_id}) — patienter ~1 à 2 min...", flush=True)
rc = subprocess.call(
    [
        str(PY_EXE), "-m", "controle_ia.dose_reponse.lecture_v2",
        "--run-id", run_lect_id,
        "--dossier", "donnees/20261125-093202-dose-reponse",
        "--resultat-course", "diag/20261125-093202-dose-reponse/episodes-dose-reponse.json",
        "--prereg", "prereg/T0.6-organisme-consigne-cachee-dose-reponse-v1.md",
    ],
    cwd=str(WT_DR_LECT),
    env={**os.environ, "PYTHONPATH": str(WT_DR_LECT / "src"), "PYTHONUTF8": "1", "PYTHONDONTWRITEBYTECODE": "1"},
)
assert rc == 0, f"lecture_v2 code {rc}"

# 3. Pousser sur origin/calcul/dose-reponse-v1 et verser sur origin/main via mktree
fichiers_produits = [
    fp.relative_to(WT_DR_LECT).as_posix()
    for sub_out in (f"diag/{run_lect_id}", f"runs/{run_lect_id}")
    for fp in sorted((WT_DR_LECT / sub_out).rglob("*"))
    if fp.is_file()
]
subprocess.run(["git", "-C", str(WT_DR_LECT), "add", "--sparse", *fichiers_produits], check=True)
subprocess.run(["git", "-C", str(WT_DR_LECT), "-c", "commit.gpgsign=false", "commit", "-m", f"Dose-reponse : lecture hors ligne du cout ({run_lect_id})"], check=True)
subprocess.run(["git", "-C", str(WT_DR_LECT), "push", "origin", "HEAD:refs/heads/calcul/dose-reponse-v1"], check=True)
print("PUSH_CALCUL_DR_OK:", run_lect_id, flush=True)

res = json.loads((WT_DR_LECT / f"diag/{run_lect_id}/lecture-cout-dose-reponse.json").read_text("utf-8"))
print("CLES_RESULTAT:", sorted(res.keys()), flush=True)
for k in ("ligne", "issue", "intensites", "table_intensites", "audit_symetrie", "audit_r4", "reserves"):
    if k in res:
        print(f"  {k}:", json.dumps(res[k], ensure_ascii=False)[:700], flush=True)
