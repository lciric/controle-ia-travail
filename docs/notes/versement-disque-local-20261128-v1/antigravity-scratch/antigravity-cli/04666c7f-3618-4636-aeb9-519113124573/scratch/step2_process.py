import hashlib
import os
import pathlib
import shutil
import subprocess
import sys

repo = r"C:\Users\lciri\OneDrive\Documents\controle-ia-travail"
scratch = pathlib.Path(r"C:\Users\lciri\.gemini\antigravity-cli\brain\cd7c89b9-9752-4dac-b846-2c58efd89737\scratch")
wt = scratch / "wt-b8-exec-v5"
py = str(scratch / "venv-py314" / "Scripts" / "python.exe")

def check_sha(rel_path: str) -> str:
    p = wt / rel_path
    s = wt / (rel_path + ".sha256")
    actual = hashlib.sha256(p.read_bytes()).hexdigest()
    comp = s.read_text(encoding="utf-8").strip()
    expected = comp.split()[0]
    ok = (actual == expected)
    print(f"CHECK {rel_path} | sha256={actual} | companion_ok={ok}")
    if not ok:
        raise RuntimeError(f"SHA256 mismatch for {rel_path}")
    return actual

print("=== 1. VERIFY LECTURE (2) OUTPUTS ===")
run2_dir = wt / "runs" / "20261125-085524-iib-lecture-2-diffusion-v5"
print("RUN2_FILES:", [p.name for p in sorted(run2_dir.iterdir())])
check_sha("diag/20261123-043944-iib-course-reel/lecture-iib-2-diffusion-exploratoire-non-opposable-v1.json")
check_sha("diag/20261123-043944-iib-course-reel/lecture-iib-2-mots-ponderes-exploratoire-non-opposable-v1.json")
check_sha("runs/20261125-085524-iib-lecture-2-diffusion-v5/manifeste.json")

print("=== 2. COPY & VERIFY AUDIT R4 REPORT ===")
audit_dir = wt / "docs" / "notes" / "barreau8-cote-expose-pieces-lecture-v1"
audit_dir.mkdir(parents=True, exist_ok=True)
for fname in ("audit-r4-lecture-1-iib-v5-v1.md", "audit-r4-lecture-1-iib-v5-v1.md.sha256"):
    shutil.copyfile(scratch / fname, audit_dir / fname)
check_sha("docs/notes/barreau8-cote-expose-pieces-lecture-v1/audit-r4-lecture-1-iib-v5-v1.md")

print("=== 3. COMMIT LECTURE (2) + AUDIT R4 ===")
to_add_1 = [
    "diag/20261123-043944-iib-course-reel/lecture-iib-2-diffusion-exploratoire-non-opposable-v1.json",
    "diag/20261123-043944-iib-course-reel/lecture-iib-2-diffusion-exploratoire-non-opposable-v1.json.sha256",
    "diag/20261123-043944-iib-course-reel/lecture-iib-2-mots-ponderes-exploratoire-non-opposable-v1.json",
    "diag/20261123-043944-iib-course-reel/lecture-iib-2-mots-ponderes-exploratoire-non-opposable-v1.json.sha256",
    "runs/20261125-085524-iib-lecture-2-diffusion-v5/manifeste.json",
    "runs/20261125-085524-iib-lecture-2-diffusion-v5/manifeste.json.sha256",
    "docs/notes/barreau8-cote-expose-pieces-lecture-v1/audit-r4-lecture-1-iib-v5-v1.md",
    "docs/notes/barreau8-cote-expose-pieces-lecture-v1/audit-r4-lecture-1-iib-v5-v1.md.sha256",
]
subprocess.run(["git", "-C", str(wt), "add", "--"] + to_add_1, check=True)
subprocess.run(["git", "-C", str(wt), "commit", "-m", "barreau 8 : exécution lecture (2) de la diffusion course v5 et rapport d'audit R4"], check=True)
commit_l2 = subprocess.check_output(["git", "-C", str(wt), "rev-parse", "HEAD"], text=True).strip()
print("COMMIT_L2=", commit_l2)
st1 = subprocess.check_output(["git", "-C", str(wt), "status", "--porcelain"], text=True).strip()
print("STATUS_AFTER_L2=", repr(st1))
if st1:
    raise RuntimeError(f"Dirty worktree after L2 commit: {st1}")

print("=== 4. EXTRACT & VERIFY V5 EXTRACTOR SCRIPT ===")
src_commit = "ff4b3f2261800d994f5a527fbfc2a1f22978dfb8"
expected_script_sha = "862ccc147da66e6ce705867f0de621c70038565f1219fb55c5a0872e33d4f9e7"
for suffix in ("", ".sha256"):
    src_blob = f"{src_commit}:docs/notes/barreau8-cote-expose-pieces-lecture-v1/extrait_iib_etats_lectures_cote_moniteurs_v5.py{suffix}"
    raw = subprocess.check_output(["git", "-C", repo, "cat-file", "blob", src_blob])
    out_p = wt / "scripts" / f"extrait_iib_etats_lectures_cote_moniteurs_v5.py{suffix}"
    out_p.write_bytes(raw)
actual_script_sha = check_sha("scripts/extrait_iib_etats_lectures_cote_moniteurs_v5.py")
if actual_script_sha != expected_script_sha:
    raise RuntimeError(f"Script SHA mismatch: {actual_script_sha} != {expected_script_sha}")

print("=== 5. RUN V5 EXTRACTOR SCRIPT ===")
env = os.environ.copy()
env["PYTHONPATH"] = "src"
env["PYTHONDONTWRITEBYTECODE"] = "1"
cmd = [
    py,
    "scripts/extrait_iib_etats_lectures_cote_moniteurs_v5.py",
    "--racine", ".",
    "--run-id", "20261123-043944-iib-course-reel",
    "--registre-sondes", r"C:\Users\lciri\OneDrive\Documents\controle-ia-travail\registres\sondes-iib-v1.md",
    "--sortie", "docs/notes/barreau8-cote-moniteurs-entrees-v1/etats-lectures-iib-v1.json",
]
res = subprocess.run(cmd, cwd=str(wt), env=env, capture_output=True, text=True)
print("EXTRACTOR_EXIT_CODE=", res.returncode)
print("EXTRACTOR_STDOUT=", res.stdout.strip())
if res.stderr.strip():
    print("EXTRACTOR_STDERR=", res.stderr.strip())
if res.returncode != 0:
    sys.exit(res.returncode)

check_sha("docs/notes/barreau8-cote-moniteurs-entrees-v1/etats-lectures-iib-v1.json")

print("=== 6. COMMIT V5 EXTRACTOR + 13 STATES EXTRACT ===")
to_add_2 = [
    "scripts/extrait_iib_etats_lectures_cote_moniteurs_v5.py",
    "scripts/extrait_iib_etats_lectures_cote_moniteurs_v5.py.sha256",
    "docs/notes/barreau8-cote-moniteurs-entrees-v1/etats-lectures-iib-v1.json",
    "docs/notes/barreau8-cote-moniteurs-entrees-v1/etats-lectures-iib-v1.json.sha256",
]
subprocess.run(["git", "-C", str(wt), "add", "--"] + to_add_2, check=True)
subprocess.run(["git", "-C", str(wt), "commit", "-m", "barreau 8 : extrait v5 des treize états des lectures pour le côté moniteurs"], check=True)
commit_ext = subprocess.check_output(["git", "-C", str(wt), "rev-parse", "HEAD"], text=True).strip()
print("COMMIT_EXTRACTOR=", commit_ext)
st2 = subprocess.check_output(["git", "-C", str(wt), "status", "--porcelain"], text=True).strip()
print("STATUS_AFTER_EXTRACTOR=", repr(st2))
if st2:
    raise RuntimeError(f"Dirty worktree after extractor commit: {st2}")
