import hashlib
import json
import os
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
VAST_EXE = SCRATCH / "venv-py314" / "Scripts" / "vastai.exe"
WT_B8 = SCRATCH / "wt-b8-puissance"
WT_DR = SCRATCH / "lecture-dr"

# 1. Restaurer les 8 .sha256 suivis par Git dans wt-b8-puissance (sans toucher à versement/)
j_b8 = SCRATCH / "journal-lecture-sondes-barreau8-v1"
if not j_b8.exists():
    subprocess.run(
        ["git", "-C", str(WT_B8), "checkout", "--", "diag", "docs"],
        check=True,
    )
    st_b8 = subprocess.check_output(
        ["git", "-C", str(WT_B8), "status", "--porcelain", "--untracked-files=all"],
        text=True,
    ).strip()
    assert st_b8 == "", f"wt-b8-puissance encore non vide:\n{st_b8}"
    bord = (
        WT_B8
        / "versement/20261124-122719-rejeu-activations-voie-a"
        / "sortie-passe/livraison/bordereau-livraison-passe-barreau8-v1.json"
    )
    sha_b = hashlib.sha256(bord.read_bytes()).hexdigest()
    assert sha_b.startswith("85bae5dcd979"), f"Bordereau inattendu: {sha_b}"
    r_sc = subprocess.run(
        [
            str(PY_EXE), "-m", "controle_ia.scellement", "verifier",
            "docs/notes/barreau8-conductrice-lecture-sondes-v1/mandat-lecteur-sondes-barreau8-v3.md",
            "docs/notes/barreau8-conductrice-lecture-sondes-v1/mandat-juge-lecture-sondes-barreau8-v3.md",
            "docs/notes/barreau8-cote-expose-pieces-lecture-v1/liste-exclus-ordre-course-lue-v2.md",
            "registres/qui-a-lu-quoi-v23.md",
        ],
        cwd=str(WT_B8),
        env={**os.environ, "PYTHONPATH": str(WT_B8 / "src"), "PYTHONUTF8": "1"},
        capture_output=True, text=True,
    )
    assert r_sc.returncode == 0, f"Sceaux B8: {r_sc.stderr}"
    print("WT_B8_PRET_ET_PROPRE_OK: OUI (arbre vide, bordereau LF 85bae5dcd979…, 4 sceaux OK)", flush=True)
else:
    print("INFO_B8: journal déjà créé (lecteur en cours, non touché)", flush=True)

# 2. Avancement rapide de 62647167
vk = Path.home() / ".config" / "vastai" / "vast_api_key"
vast_key = os.environ.get("VAST_API_KEY", "").strip() or vk.read_text("utf-8").strip()
try:
    logs = subprocess.check_output(
        [str(VAST_EXE), "logs", "62647167"],
        env={**os.environ, "VAST_API_KEY": vast_key, "PYTHONUTF8": "1"},
        text=True, timeout=20, stderr=subprocess.STDOUT,
    )
    print("62647167 dernières lignes:", " | ".join(logs.splitlines()[-3:]), flush=True)
except Exception:
    pass

# 3. Exécution unique de lecture_v2 dans lecture-dr
deja = list((WT_DR / "diag").glob("*-dose-reponse-lecture")) + list(
    (WT_DR / "runs").glob("*-dose-reponse-lecture")
)
assert not deja, f"Lecture déjà présente : {deja}"

run_lect = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S") + "-dose-reponse-lecture"
gitdir_wt = Path(
    subprocess.check_output(["git", "-C", str(WT_DR), "rev-parse", "--git-dir"], text=True).strip()
)
if not gitdir_wt.is_absolute():
    gitdir_wt = (WT_DR / gitdir_wt).resolve()
sp_file = gitdir_wt / "info" / "sparse-checkout"
sp_txt = sp_file.read_text("utf-8").rstrip("\n")
sp_file.write_bytes((sp_txt + f"\n/diag/{run_lect}/\n/runs/{run_lect}/\n").encode("utf-8"))

st_dr = subprocess.check_output(["git", "-C", str(WT_DR), "status", "--porcelain"], text=True).strip()
assert st_dr == "", f"lecture-dr non propre:\n{st_dr}"

print(f"\n>>> LANCEMENT UNIQUE DE lecture_v2 ({run_lect}) — ~1 à 2 min...", flush=True)
rc = subprocess.call(
    [
        str(PY_EXE), "-m", "controle_ia.dose_reponse.lecture_v2",
        "--run-id", run_lect,
        "--dossier", "donnees/20261125-093202-dose-reponse",
        "--resultat-course", "diag/20261125-093202-dose-reponse/episodes-dose-reponse.json",
        "--prereg", "prereg/T0.6-organisme-consigne-cachee-dose-reponse-v1.md",
    ],
    cwd=str(WT_DR),
    env={
        **os.environ,
        "PYTHONPATH": str(WT_DR / "src"),
        "PYTHONUTF8": "1",
        "PYTHONDONTWRITEBYTECODE": "1",
    },
)
assert rc == 0, f"lecture_v2 sortie en code {rc}"

# 4. Vérifier les sceaux produits et pousser sur origin/calcul/dose-reponse-v1
produits = []
for sub_d in (f"diag/{run_lect}", f"runs/{run_lect}"):
    for sf in sorted((WT_DR / sub_d).rglob("*.sha256")):
        att, nom = sf.read_text("utf-8").strip().split(None, 1)
        cible = sf.parent / Path(nom.lstrip("*")).name
        assert hashlib.sha256(cible.read_bytes()).hexdigest() == att
    for fp in sorted((WT_DR / sub_d).rglob("*")):
        if fp.is_file():
            produits.append(fp.relative_to(WT_DR).as_posix())

subprocess.run(["git", "-C", str(WT_DR), "add", "--sparse", *produits], check=True)
subprocess.run(
    [
        "git", "-C", str(WT_DR), "-c", "commit.gpgsign=false", "commit",
        "-m", f"Dose-reponse : lecture hors ligne du cout ({run_lect})",
    ],
    check=True,
)
subprocess.run(
    ["git", "-C", str(WT_DR), "push", "origin", "HEAD:refs/heads/calcul/dose-reponse-v1"],
    check=True,
)
sha_dr = subprocess.check_output(
    ["git", "-C", str(WT_DR), "rev-parse", "--short", "HEAD"], text=True
).strip()
print(f"PUSH_CALCUL_DR_OK: {run_lect} @ {sha_dr}", flush=True)

# 5. Verser les mêmes fichiers sur origin/main sans toucher à REPO
subprocess.run(["git", "-C", str(REPO), "fetch", "origin", "main"], check=True)
p_main = subprocess.check_output(["git", "-C", str(REPO), "rev-parse", "origin/main"], text=True).strip()
tmp_idx = SCRATCH / "_tmp_idx_lect_dr"
tmp_idx.unlink(missing_ok=True)
env_i = {**os.environ, "GIT_INDEX_FILE": str(tmp_idx), "PYTHONUTF8": "1"}
try:
    subprocess.run(
        ["git", "-c", "core.protectNTFS=false", "-C", str(REPO), "read-tree", p_main],
        env=env_i, check=True,
    )
    for rf in produits:
        b_s = subprocess.check_output(
            ["git", "-C", str(REPO), "hash-object", "-w", "--stdin"],
            input=(WT_DR / rf).read_bytes(),
        ).decode().strip()
        subprocess.run(
            [
                "git", "-c", "core.protectNTFS=false", "-C", str(REPO),
                "update-index", "--add", "--cacheinfo", f"100644,{b_s},{rf}",
            ],
            env=env_i, check=True,
        )
    t_s = subprocess.check_output(["git", "-C", str(REPO), "write-tree"], env=env_i, text=True).strip()
    msg_m = f"Versement resultat scelle lecture cout dose-reponse ({run_lect})\n"
    c_s = subprocess.check_output(
        ["git", "-C", str(REPO), "commit-tree", t_s, "-p", p_main],
        input=msg_m.encode("utf-8"), env=env_i,
    ).decode().strip()
    subprocess.run(["git", "-C", str(REPO), "push", "origin", f"{c_s}:refs/heads/main"], check=True)
    print(f"VERSEMENT_MAIN_OK: {c_s[:12]}", flush=True)
finally:
    tmp_idx.unlink(missing_ok=True)

# 6. Afficher les clés et l'état de l'audit R4 pour préparer le verdict R13
res_p = WT_DR / f"diag/{run_lect}/lecture-cout-dose-reponse.json"
res = json.loads(res_p.read_text("utf-8"))
print("\n=== RÉSUMÉ STRUCTUREL DE lecture-cout-dose-reponse.json ===", flush=True)
print("SHA256:", hashlib.sha256(res_p.read_bytes()).hexdigest(), flush=True)
print("Clés racine:", sorted(res.keys()), flush=True)
if "resultat" in res and isinstance(res["resultat"], dict):
    r_in = res["resultat"]
    print("Clés resultat:", sorted(r_in.keys()), flush=True)
    for k in ("ligne", "issue", "echelle_intensite", "echelle_proportion", "intensites", "audit_symetrie", "reserves"):
        if k in r_in:
            print(f"  {k}:", json.dumps(r_in[k], ensure_ascii=False)[:800], flush=True)
