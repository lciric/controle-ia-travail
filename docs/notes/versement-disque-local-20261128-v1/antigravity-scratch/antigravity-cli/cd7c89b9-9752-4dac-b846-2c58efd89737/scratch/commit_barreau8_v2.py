import hashlib
import shutil
import subprocess
import sys
from pathlib import Path

REPO = Path(r"C:\Users\lciri\OneDrive\Documents\controle-ia-travail")
SCRATCH = Path(r"C:\Users\lciri\.gemini\antigravity-cli\brain\cd7c89b9-9752-4dac-b846-2c58efd89737\scratch")
CL_DIR = SCRATCH / "cl-code-lectures-v5"
V2_DIR = CL_DIR / "v2-corrige"
WT = SCRATCH / "wt-b8-code-v5"

CODE_FILES = [
    ("src/controle_ia/iib/configuration_lectures_v5.py", "3c8232036bb84938ae3086e8ae9e8d565a68a2248e0d9ad64a2b5d34d9821c4f"),
    ("src/controle_ia/iib/entrees_lectures_v5.py", "d97eff6317794f094fefd74bb7ff164273e28385802e86a5fbc4d96fd3b07357"),
    ("src/controle_ia/iib/lectures_v5.py", "831bfa14d9fec9f5ebfeeb63c42c952de6acabd067ba4a454bcce97e663636ef"),
    ("scripts/lecture_iib_1_dommage_v5.py", "11b41164372bde2f5cac573dba22325c75cc3352cd85cead4315832c9fd28367"),
    ("scripts/lecture_iib_2_diffusion_v5.py", "0a381a4c39011089a8ef5a92677d12e477935dc2bf427bed8e569bbce09efec3"),
    ("scripts/lecture_iib_audit_r4_v5.py", "ec4c1a219ae020675491370a11e253b04bb19dd2abe784531da1dc4068d155ce"),
    ("tests/test_lectures_iib_v5_v1.py", "85967c0cee5468801a57996ae9663748ad94027321af62b5dc671902adc51e80"),
]

REPORT_FILES = [
    (CL_DIR / "contre-lecture-code-lectures-v5-neon-v1.md", "docs/notes/barreau8-cote-expose-pieces-lecture-v1/contre-lecture-code-lectures-v5-neon-v1.md", "073ee9667d15c1311674962562d3bc63ae9057ef43a461d5373c0486f107650c"),
    (V2_DIR / "corrections-cl-neon-code-lectures-v5-v1.md", "docs/notes/barreau8-cote-expose-pieces-lecture-v1/corrections-cl-neon-code-lectures-v5-v1.md", "e37e8eb256b06a2ee22bafed5210718815c1c3c34583abdf92028d42f68bbcf2"),
    (V2_DIR / "rapport-developpeur-code-lectures-v5-v1-erratum-1.md", "docs/notes/barreau8-cote-expose-pieces-lecture-v1/rapport-developpeur-code-lectures-v5-v1-erratum-1.md", "d707d9e3f654578f448827f349f826f23bd55a163685ca845289d7e449b58a62"),
    (CL_DIR / "verification-corrections-code-lectures-v5-neon-v1.md", "docs/notes/barreau8-cote-expose-pieces-lecture-v1/verification-corrections-code-lectures-v5-neon-v1.md", "e761575e13885ab233ff254b74e5ec1366eb96a992d2d11c74f5d55103c0e35a"),
]

def sha256_bytes(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()

def write_sha(p: Path, h: str) -> Path:
    comp = Path(str(p) + ".sha256")
    comp.write_bytes(f"{h}  {p.name}\n".encode("utf-8"))
    return comp

def run(cmd, cwd=None):
    print("RUN:", cmd)
    r = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True)
    if r.stdout:
        print(r.stdout.strip())
    if r.returncode != 0:
        print("STDERR:", r.stderr.strip(), file=sys.stderr)
        sys.exit(r.returncode)
    return r

# 1. Prepare strictly sparse worktree on barreau8/code-lectures-v5-cote-expose-v1 (NO donnees/, runs/, diag/, traces/!)
if WT.exists():
    run(["git", "-C", str(REPO), "worktree", "remove", "--force", str(WT)])

run(["git", "-C", str(REPO), "-c", "core.protectNTFS=false", "worktree", "add", "--no-checkout", "-B", "barreau8/code-lectures-v5-cote-expose-v1", str(WT), "origin/barreau8/code-lectures-v5-cote-expose-v1"])
run(["git", "-C", str(WT), "config", "core.longpaths", "true"])
run(["git", "-C", str(WT), "sparse-checkout", "init", "--no-cone"])
p_sc = subprocess.run(
    ["git", "-C", str(WT), "sparse-checkout", "set", "--no-cone", "--stdin"],
    input="/src/controle_ia/iib/\n/scripts/lecture_iib_*\n/tests/test_lectures_iib_v5_v1.py*\n/docs/notes/barreau8-cote-expose-pieces-lecture-v1/\n",
    text=True, capture_output=True
)
if p_sc.returncode != 0:
    print(p_sc.stderr, file=sys.stderr)
    sys.exit(p_sc.returncode)
run(["git", "-C", str(WT), "-c", "core.protectNTFS=false", "checkout"])

# Verify zero cloisonne directories exist in WT
for forbidden in ("donnees", "runs", "diag", "traces", "verdict", "coffre"):
    assert not (WT / forbidden).exists(), f"FORBIDDEN DIR PRESENT: {forbidden}"

# 2. Copy & verify all 7 code/test files + .sha256 into WT
to_add = []
for rel, expected in CODE_FILES:
    src = V2_DIR / rel
    dst = WT / rel
    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.write_bytes(src.read_bytes())
    got = sha256_bytes(dst)
    assert got == expected, f"Hash mismatch on {rel}: {got} != {expected}"
    comp = write_sha(dst, got)
    to_add.extend([rel, rel + ".sha256"])

# 3. Copy & verify all 4 reports + .sha256 into WT AND into main repo
for src, rel, expected in REPORT_FILES:
    data = src.read_bytes()
    got = hashlib.sha256(data).hexdigest()
    assert got == expected, f"Hash mismatch on report {rel}: {got} != {expected}"
    for root in (WT, REPO):
        dst = root / rel
        dst.parent.mkdir(parents=True, exist_ok=True)
        dst.write_bytes(data)
        write_sha(dst, got)
    to_add.extend([rel, rel + ".sha256"])

run(["git", "-C", str(WT), "add", "--"] + to_add)
run(["git", "-C", str(WT), "status", "--short"])
msg = (
    "Barreau 8, côté exposé : corrections CLN-01 à CLN-07 et vérification conforme du code des lectures v5 (GO-2026-11-24-37)\n\n"
    "Contre-lecture classe B (Gemini 4 Neon neuf, 073ee966), corrections par un développeur neuf (e37e8eb2, erratum 1 d707d9e3),\n"
    "vérification finale par le même contre-lecteur : verdict « conforme » sans constat résiduel ni régression (e761575e).\n"
    "168 essais collectés (+15 neufs), 81/81 unitaires autonomes verts, 15 modules gelés intacts, strict cloisonnement respecté."
)
run(["git", "-C", str(WT), "commit", "-m", msg])
run(["git", "-C", str(WT), "rev-parse", "HEAD"])
print("ALL_OK")
