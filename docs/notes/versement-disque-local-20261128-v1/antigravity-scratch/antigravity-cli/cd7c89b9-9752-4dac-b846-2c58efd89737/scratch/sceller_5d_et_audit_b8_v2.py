import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
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
WT_DR = SCRATCH / "lecture-dr"
WT_B8 = SCRATCH / "wt-b8-puissance"
PAQ_5D = SCRATCH / "paquet-juge-r13-doses-critere3"

def sha_bytes(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()

def ecrire_scelle(root: Path, rel: str, texte: str) -> str:
    p = root / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    b = (texte.strip() + "\n").encode("utf-8")
    h = sha_bytes(b)
    p.write_bytes(b)
    (root / f"{rel}.sha256").write_bytes(f"{h}  {rel}\n".encode("utf-8"))
    return h

# ==============================================================================
# 1. RETROUVER LE COMMIT / FICHIER doses-jugees-critere-3.json ET SCELLER 5(d)
# ==============================================================================
print("=== 1. RESTAURATION & SCELLEMENT ÉTAPE 5(d) ===")
reflog = subprocess.check_output(["git", "-C", str(WT_DR), "reflog", "-n", "15", "--oneline"], text=True)
print("Reflog WT_DR:\n" + reflog.strip())

# Chercher si un commit récent du reflog portait déjà doses-jugees-critere-3.json
commit_dj = None
for line in reflog.splitlines():
    sha_c = line.split()[0]
    ls_c = subprocess.check_output(["git", "-C", str(WT_DR), "ls-tree", "-r", "--name-only", sha_c], text=True).splitlines()
    if any("doses-jugees-critere-3.json" in f for f in ls_c):
        commit_dj = sha_c
        break

if commit_dj:
    print(f"Commit portant doses-jugees-critere-3.json trouvé dans reflog : {commit_dj}")
    subprocess.run(["git", "-C", str(WT_DR), "checkout", "-B", "calcul/dose-reponse-20261125-093202-doses-jugees-critere3", commit_dj], check=True)

candidats_dj = list(WT_DR.glob("diag/**/doses-jugees-critere-3.json"))
if not candidats_dj:
    # Vérifier dans PAQ_5D où il a été copié avant le checkout -B
    src_paq = PAQ_5D / "doses-jugees-critere-3.json"
    assert src_paq.is_file(), "doses-jugees-critere-3.json introuvable même dans PAQ_5D !"
    doc_dj = json.loads(src_paq.read_text("utf-8"))
    run_id_dj = doc_dj["run_id"]
    p_dj = WT_DR / "diag" / run_id_dj / "doses-jugees-critere-3.json"
    p_dj.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src_paq, p_dj)
    rel_dj = f"diag/{run_id_dj}/doses-jugees-critere-3.json"
    h_dj = sha_bytes(p_dj.read_bytes())
    (WT_DR / f"{rel_dj}.sha256").write_bytes(f"{h_dj}  {rel_dj}\n".encode("utf-8"))
    print(f"Restauré depuis PAQ_5D vers {rel_dj}")
else:
    p_dj = candidats_dj[0]
    rel_dj = p_dj.relative_to(WT_DR).as_posix()

h_dj = sha_bytes(p_dj.read_bytes())
print(f"Fichier doses-jugees : {rel_dj} | sha256={h_dj}")
assert h_dj == "bc70017e45fb3d0a0f6b12d433c9b48abb99746ffa08369e6e4b5a900e590982", h_dj

# Re-sceller les deux rapports R4 et R13 (au cas où le reset de branche les aurait effacés)
p_aud_md = WT_DR / "docs/verdicts/audit-r4-lecteur-du-texte-dose-reponse-v1.md"
p_ver_md = WT_DR / "docs/verdicts/verdict-verification-doses-jugees-critere-3-v1.md"

# Relire depuis sceller_5d_et_audit_b8.py pour ne pas dupliquer 180 lignes
ancien_script = (SCRATCH / "sceller_5d_et_audit_b8.py").read_text("utf-8")
ns = {}
exec(compile(ancien_script.split("# 1. SCELLER")[1].split("h_aud_5d =")[0].split("subprocess.run")[1].split("\n", 1)[1], "<extraits>", "exec"), ns)
md_audit_5d = ns["md_audit_5d"]
md_verdict_5d = ns["md_verdict_5d"].replace("diag/20261126-095224-lecteur-du-texte-dose-reponse/doses-jugees-critere-3.json", rel_dj)

h_aud_5d = ecrire_scelle(WT_DR, "docs/verdicts/audit-r4-lecteur-du-texte-dose-reponse-v1.md", md_audit_5d)
h_ver_5d = ecrire_scelle(WT_DR, "docs/verdicts/verdict-verification-doses-jugees-critere-3-v1.md", md_verdict_5d)
print("Audit R4 5(d) scellé:", h_aud_5d)
print("Verdict R13 5(d) scellé:", h_ver_5d)

reg_dr = WT_DR / "registres/dose-reponse-v1.md"
reg_txt = reg_dr.read_text("utf-8")
if "DOSES-JUGEES-CRITERE-3" not in reg_txt:
    ts_dj = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    ligne_dj = f"| DOSES-JUGEES-CRITERE-3 | {ts_dj} | {rel_dj} | {h_dj} |\n"
    reg_dr.write_text(reg_txt.rstrip() + "\n" + ligne_dj, encoding="utf-8")
    print("Ligne inscrite:", ligne_dj.strip())

print("\nContenu de registres/dose-reponse-v1.md:")
print(reg_dr.read_text("utf-8"))

to_add = [
    "runs/20261126-095224-lecteur-du-texte-dose-reponse",
    "diag/20261126-095224-lecteur-du-texte-dose-reponse",
    rel_dj,
    f"{rel_dj}.sha256",
    "docs/verdicts/audit-r4-lecteur-du-texte-dose-reponse-v1.md",
    "docs/verdicts/audit-r4-lecteur-du-texte-dose-reponse-v1.md.sha256",
    "docs/verdicts/verdict-verification-doses-jugees-critere-3-v1.md",
    "docs/verdicts/verdict-verification-doses-jugees-critere-3-v1.md.sha256",
    "registres/dose-reponse-v1.md",
]
for extra_d in sorted(WT_DR.glob("runs/*doses-jugees*")) + sorted(WT_DR.glob("diag/*doses-jugees*")):
    to_add.append(extra_d.relative_to(WT_DR).as_posix())

subprocess.run(["git", "-C", str(WT_DR), "add", "-f", *to_add], check=True)
st_dr = subprocess.check_output(["git", "-C", str(WT_DR), "status", "--porcelain"], text=True)
if st_dr.strip():
    subprocess.run(
        ["git", "-C", str(WT_DR), "commit", "-m", "dose-reponse: etape 5d lecteur du texte, audit R4, verification R13 et DOSES-JUGEES-CRITERE-3 (KA-3)"],
        check=True,
    )
subprocess.run(["git", "-C", str(WT_DR), "push", "-u", "origin", "calcul/dose-reponse-20261125-093202-doses-jugees-critere3"], check=True)
print("PUSH_5D_OK: calcul/dose-reponse-20261125-093202-doses-jugees-critere3")

# ==============================================================================
# 2. LANCER LA COMMANDE OFFICIELLE `lecture_sondes_v6 audit` SUR BARREAU 8
# ==============================================================================
print("\n=== 2. EXÉCUTION DE `lecture_sondes_v6 audit` SUR BARREAU 8 ===")
p_am = WT_B8 / "diag/20261126-083755-lecture-sondes-barreau8/audit-mecanique-lecture-sondes-barreau8-v1.json"
if not p_am.is_file():
    env_b8 = {**os.environ, "PYTHONPATH": str(WT_B8 / "src"), "PYTHONUTF8": "1"}
    cmd_aud = [
        str(PY_EXE), "-m", "controle_ia.barreau8_moniteurs.lecture_sondes_v6",
        "audit",
        "--racine", str(WT_B8),
        "--registre", "registres/sondes-iib-v1.md",
        "--sondes-legeres", "donnees/20261009-001125-t07-entrainement-sondes/sondes-figees-legeres.npz",
        "--planchers", "donnees/20261108-152213-planchers-800/planchers-800-sondes-principales.npz",
        "--sondes-neuves", "donnees/20261108-190600-sondes-dissimulation/sondes-dissimulation-et-plancher-800.npz",
    ]
    proc = subprocess.run(cmd_aud, cwd=str(WT_B8), env=env_b8, capture_output=True, text=True)
    print("STDOUT audit B8:\n" + proc.stdout)
    if proc.stderr:
        print("STDERR audit B8:\n" + proc.stderr)
    if proc.returncode != 0:
        sys.exit(proc.returncode)
else:
    print("Sortie déjà existante:", p_am)

sha_am = sha_bytes(p_am.read_bytes())
doc_am = json.loads(p_am.read_text("utf-8"))
res_am = doc_am.get("resultat", doc_am)
print(f"AUDIT_MECANIQUE_B8_OK: sha256={sha_am}")
print("Clés résultat audit mécanique:", sorted(res_am.keys()))
print("Ligne issue audit mécanique:", res_am.get("ligne"))
print("Défauts établis:", res_am.get("defauts"))

PAQ_AUD_B8 = SCRATCH / "paquet-auditeur-r4-barreau8"
if PAQ_AUD_B8.exists():
    shutil.rmtree(PAQ_AUD_B8)
PAQ_AUD_B8.mkdir(parents=True, exist_ok=True)

for fp in [
    WT_B8 / "prereg/lecture-sondes-barreau8-v1.md",
    WT_B8 / "prereg/lecture-sondes-barreau8-v1-addendum-organisme-change-v1.md",
    WT_B8 / "prereg/lecture-sondes-barreau8-v1-addendum-2-format-entrees-v1.md",
    WT_B8 / "docs/notes/barreau8-cote-moniteurs-sorties-v1/constantes-reportees-additif-2-v1.json",
    WT_B8 / "docs/notes/barreau8-cote-moniteurs-entrees-v1/etats-lectures-iib-v1.json",
    WT_B8 / "diag/20261126-083755-lecture-sondes-barreau8/lecture-sondes-barreau8-v1.json",
    p_am,
    WT_B8 / "registres/sondes-iib-v1.md",
]:
    dst = PAQ_AUD_B8 / fp.name
    shutil.copy2(fp, dst)
    print(f"  {fp.name} ({dst.stat().st_size}o) sha256={sha_bytes(dst.read_bytes())}")

# ==============================================================================
# 3. ÉTAT VAST.AI 62647167 & SONDES V2
# ==============================================================================
print("\n=== 3. ÉTAT VAST.AI 62647167 & BRANCHE SUITE SONDES V2 ===")
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
