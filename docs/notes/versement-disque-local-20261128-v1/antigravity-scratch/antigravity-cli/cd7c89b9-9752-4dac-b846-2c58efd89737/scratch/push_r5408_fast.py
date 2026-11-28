import hashlib
import os
import shutil
import subprocess
from pathlib import Path

REPO = Path(r"C:\Users\lciri\OneDrive\Documents\controle-ia-travail")
SCRATCH = Path(r"C:\Users\lciri\.gemini\antigravity-cli\brain\cd7c89b9-9752-4dac-b846-2c58efd89737\scratch")
WT = SCRATCH / "wt-main-push"
env = os.environ.copy()
env["GIT_TERMINAL_PROMPT"] = "0"

# Clean stale index.lock if no git.exe is running
lock = REPO / ".git" / "index.lock"
if lock.exists():
    ps = subprocess.check_output(["tasklist", "/FI", "IMAGENAME eq git.exe"], text=True)
    if "git.exe" not in ps:
        lock.unlink()
        print("REMOVED_STALE_INDEX_LOCK")
    else:
        raise RuntimeError("git.exe still running!")

def git_run(cwd, *args, check=True, timeout=120):
    p = subprocess.run(
        ["git", "-C", str(cwd), "-c", "credential.helper=", "-c", "credential.helper=!gh auth git-credential",
         "-c", "core.longpaths=true", "-c", "core.protectNTFS=false", *args],
        env=env, capture_output=True, text=True, timeout=timeout,
    )
    if check and p.returncode != 0:
        raise RuntimeError(f"git {args} failed rc={p.returncode}: {p.stdout} {p.stderr}")
    return p

# Save our R-5406 line and 8 new files directly from commit e1c7ce951
head_dec = git_run(REPO, "show", "e1c7ce951:registres/decisions.md").stdout
r_lines = [ln for ln in head_dec.splitlines() if ln.startswith("- R-5406 (2026-11-25T10:40Z)")]
assert r_lines, "R-5406 line not found in e1c7ce951"
r5408_line = r_lines[0].replace("- R-5406 (", "- R-5408 (", 1)

NEW_FILES = [
    ("registres/qui-a-lu-quoi-v23.md", "325ba2dd760afb607fc064f669807f93eb967dea2759f4de33b9b324b7e03e7a"),
    ("registres/qui-a-lu-quoi-v23.md.sha256", None),
    ("docs/notes/barreau8-cote-moniteurs-entrees-v1/attestation-course-et-oracle-additif-1-v1.json",
     "8ed8a6a9bd041e0ca63a2ac58000e44d7f8f4b73cdbcebfe70467ac06f01e595"),
    ("docs/notes/barreau8-cote-moniteurs-entrees-v1/attestation-course-et-oracle-additif-1-v1.json.sha256", None),
    ("docs/notes/barreau8-cote-expose-pieces-lecture-v1/liste-exclus-ordre-course-lue-v2.md",
     "43b9d4e1fe903509326b7501406c2b3233f8e5b762f44b7bf1d083ddc2e0c3e0"),
    ("docs/notes/barreau8-cote-expose-pieces-lecture-v1/liste-exclus-ordre-course-lue-v2.md.sha256", None),
    ("docs/notes/barreau8-cote-expose-pieces-lecture-v1/liste-exclus-ordre-course-lue-v2-erratum-1.md",
     "975e21905f521c8fb66555d23c22d10388f21d213014eb1b0c8044957ae51ef8"),
    ("docs/notes/barreau8-cote-expose-pieces-lecture-v1/liste-exclus-ordre-course-lue-v2-erratum-1.md.sha256", None),
]
saved = {}
for rel, exp in NEW_FILES:
    b = subprocess.check_output(["git", "-C", str(REPO), "show", f"e1c7ce951:{rel}"], env=env)
    if exp:
        assert hashlib.sha256(b).hexdigest() == exp, f"SHA mismatch {rel}"
    saved[rel] = b

# Fetch latest origin/main
git_run(REPO, "fetch", "origin", "main")
if WT.exists():
    git_run(REPO, "worktree", "remove", "--force", str(WT), check=False)
    if WT.exists():
        shutil.rmtree(WT, ignore_errors=True)

git_run(REPO, "worktree", "add", "--no-checkout", "--detach", str(WT), "origin/main")
git_run(WT, "sparse-checkout", "init", "--cone")
git_run(WT, "sparse-checkout", "set",
        "registres",
        "docs/notes/barreau8-cote-moniteurs-entrees-v1",
        "docs/notes/barreau8-cote-expose-pieces-lecture-v1")
git_run(WT, "checkout")

for rel, data in saved.items():
    p = WT / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_bytes(data)

dec_path = WT / "registres/decisions.md"
dec_txt = dec_path.read_text(encoding="utf-8")
assert "R-5407" in dec_txt and "R-5408" not in dec_txt
dec_txt = dec_txt.rstrip("\n") + "\n" + r5408_line + "\n"
dec_path.write_bytes(dec_txt.replace("\r\n", "\n").encode("utf-8"))

git_run(WT, "add", "registres/decisions.md", *[r for r, _ in NEW_FILES])
pc = git_run(WT, "commit", "-m", "R-5408 : D-15 validee conforme, liste des exclus v2 et qui-a-lu-quoi v23 scelles")
print("COMMIT_OK:", pc.stdout.strip()[:200])
pp = git_run(WT, "push", "origin", "HEAD:refs/heads/main")
print("PUSH_OK:", (pp.stdout or pp.stderr).strip()[:200])
print("NEW_MAIN_HEAD:", git_run(WT, "rev-parse", "HEAD").stdout.strip())
