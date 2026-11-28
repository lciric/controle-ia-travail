import os
import subprocess
from pathlib import Path

REPO = Path(r"C:\Users\lciri\OneDrive\Documents\controle-ia-travail")
env = os.environ.copy()
env["GIT_TERMINAL_PROMPT"] = "0"

def git_run(*args, check=True):
    p = subprocess.run(
        ["git", "-C", str(REPO), "-c", "credential.helper=", "-c", "credential.helper=!gh auth git-credential", *args],
        env=env, capture_output=True, text=True, timeout=90,
    )
    if check and p.returncode != 0:
        raise RuntimeError(f"git {args} failed rc={p.returncode}: {p.stdout} {p.stderr}")
    return p

# Save our R-5406 line from HEAD before resetting to origin/main
head_dec = git_run("show", "HEAD:registres/decisions.md").stdout
r_line = [ln for ln in head_dec.splitlines() if ln.startswith("- R-5406 (2026-11-25T10:40Z)")][0]
r5408_line = r_line.replace("- R-5406 (", "- R-5408 (", 1)

# Reset soft to 94ea50849, checkout origin/main cleanly while keeping our 8 new untracked/added files
# Easier: save the 8 new files' bytes in memory, reset --hard origin/main, restore them + append R-5408!
NEW_FILES = [
    "registres/qui-a-lu-quoi-v23.md",
    "registres/qui-a-lu-quoi-v23.md.sha256",
    "docs/notes/barreau8-cote-moniteurs-entrees-v1/attestation-course-et-oracle-additif-1-v1.json",
    "docs/notes/barreau8-cote-moniteurs-entrees-v1/attestation-course-et-oracle-additif-1-v1.json.sha256",
    "docs/notes/barreau8-cote-expose-pieces-lecture-v1/liste-exclus-ordre-course-lue-v2.md",
    "docs/notes/barreau8-cote-expose-pieces-lecture-v1/liste-exclus-ordre-course-lue-v2.md.sha256",
    "docs/notes/barreau8-cote-expose-pieces-lecture-v1/liste-exclus-ordre-course-lue-v2-erratum-1.md",
    "docs/notes/barreau8-cote-expose-pieces-lecture-v1/liste-exclus-ordre-course-lue-v2-erratum-1.md.sha256",
]
saved = {rel: (REPO / rel).read_bytes() for rel in NEW_FILES}

git_run("reset", "--hard", "origin/main")

for rel, data in saved.items():
    p = REPO / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_bytes(data)

dec_path = REPO / "registres/decisions.md"
dec_txt = dec_path.read_text(encoding="utf-8")
assert "R-5407" in dec_txt and "R-5408" not in dec_txt
dec_txt = dec_txt.rstrip("\n") + "\n" + r5408_line + "\n"
dec_path.write_bytes(dec_txt.replace("\r\n", "\n").encode("utf-8"))

git_run("add", "registres/decisions.md", *NEW_FILES)
pc = git_run("commit", "-m", "R-5408 : D-15 validee conforme, liste des exclus v2 et qui-a-lu-quoi v23 scelles")
print("COMMIT_OK:", pc.stdout.strip()[:200])
pp = git_run("push", "origin", "main")
print("PUSH_OK:", (pp.stdout or pp.stderr).strip()[:200])
