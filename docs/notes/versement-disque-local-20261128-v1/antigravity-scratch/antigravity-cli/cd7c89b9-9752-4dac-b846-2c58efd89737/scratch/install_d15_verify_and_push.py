import hashlib
import os
import subprocess
import sys
from pathlib import Path

REPO = Path(r"C:\Users\lciri\OneDrive\Documents\controle-ia-travail")
SCRATCH = Path(r"C:\Users\lciri\.gemini\antigravity-cli\brain\cd7c89b9-9752-4dac-b846-2c58efd89737\scratch")
D15_SRC = SCRATCH / "d15-sortie" / "attestation-course-et-oracle-additif-1-v1.json"
D15_SHA_SRC = SCRATCH / "d15-sortie" / "attestation-course-et-oracle-additif-1-v1.json.sha256"
D15_DST = REPO / "docs/notes/barreau8-cote-moniteurs-entrees-v1/attestation-course-et-oracle-additif-1-v1.json"
D15_SHA_DST = REPO / "docs/notes/barreau8-cote-moniteurs-entrees-v1/attestation-course-et-oracle-additif-1-v1.json.sha256"
EXPECTED_D15 = "8ed8a6a9bd041e0ca63a2ac58000e44d7f8f4b73cdbcebfe70467ac06f01e595"

raw = D15_SRC.read_bytes()
assert hashlib.sha256(raw).hexdigest() == EXPECTED_D15
D15_DST.write_bytes(raw)
D15_SHA_DST.write_bytes(D15_SHA_SRC.read_bytes())

# Real venv-py314 validation via lecture_sondes_v6 (full stack, zero stubs!)
sys.path.insert(0, str(REPO / "src"))
from controle_ia import scellement
from controle_ia.barreau8_moniteurs import lecture_sondes_v6 as ls

for p in (
    D15_DST,
    REPO / "docs/notes/barreau8-cote-expose-pieces-lecture-v1/liste-exclus-ordre-course-lue-v2.md",
    REPO / "docs/notes/barreau8-cote-expose-pieces-lecture-v1/liste-exclus-ordre-course-lue-v2-erratum-1.md",
    REPO / "registres/qui-a-lu-quoi-v23.md",
    REPO / "docs/notes/barreau8-cote-moniteurs-entrees-v1/etats-lectures-iib-v1.json",
):
    print("SCELLEMENT_OK:", p.name, scellement.verifier(p)[:16])

pieces = ls.Pieces()
fake_mandat = f"{pieces.attestation_ordre[1]} {EXPECTED_D15}"
res_ordre = ls.exiger_attestation_ordre(REPO, pieces, fake_mandat)
print("EXIGER_ATTESTATION_ORDRE_OK:", res_ordre["sha256"][:16], res_ordre["verdict_mecanique"])

res_course = ls.exiger_attestation_course(REPO, pieces, fake_mandat, "20261123-043944-iib-course-reel", "20261123-043944-iib-course-reel")
print("EXIGER_ATTESTATION_COURSE_OK:", res_course)

res_acc = ls.exiger_accord(REPO / "registres/go.md", "GO-2026-11-24-28")
print("EXIGER_ACCORD_OK:", res_acc[:16])

# Commit & push main
env = os.environ.copy()
env["GIT_TERMINAL_PROMPT"] = "0"
def git_run(*args):
    return subprocess.run(
        ["git", "-C", str(REPO), "-c", "credential.helper=", "-c", "credential.helper=!gh auth git-credential", *args],
        env=env, capture_output=True, text=True, timeout=90,
    )

to_add = [
    "registres/decisions.md",
    "registres/qui-a-lu-quoi-v23.md",
    "registres/qui-a-lu-quoi-v23.md.sha256",
    "docs/notes/barreau8-cote-moniteurs-entrees-v1/attestation-course-et-oracle-additif-1-v1.json",
    "docs/notes/barreau8-cote-moniteurs-entrees-v1/attestation-course-et-oracle-additif-1-v1.json.sha256",
    "docs/notes/barreau8-cote-expose-pieces-lecture-v1/liste-exclus-ordre-course-lue-v2.md",
    "docs/notes/barreau8-cote-expose-pieces-lecture-v1/liste-exclus-ordre-course-lue-v2.md.sha256",
    "docs/notes/barreau8-cote-expose-pieces-lecture-v1/liste-exclus-ordre-course-lue-v2-erratum-1.md",
    "docs/notes/barreau8-cote-expose-pieces-lecture-v1/liste-exclus-ordre-course-lue-v2-erratum-1.md.sha256",
]
git_run("add", *to_add)
pc = git_run("commit", "-m", "R-5406 : D-15 validee conforme, liste des exclus v2 et qui-a-lu-quoi v23 scelles")
print("COMMIT:", pc.returncode, (pc.stdout or pc.stderr).strip()[:200])
pp = git_run("push", "origin", "main")
print("PUSH:", pp.returncode, (pp.stdout or pp.stderr).strip()[:200])

# Check CPU time of running task-510 puissance python process
ps_out = subprocess.check_output(
    ["powershell", "-NoProfile", "-Command",
     "Get-CimInstance Win32_Process | Where-Object { $_.CommandLine -like '*puissance*' } | ForEach-Object { $p = Get-Process -Id $_.ProcessId -ErrorAction SilentlyContinue; if ($p) { \"$($p.Id) CPU=$($p.CPU)s WS=$([math]::Round($p.WorkingSet64/1MB,1))MB Start=$($p.StartTime)\" } }"],
    text=True, timeout=30,
).strip()
print("PUISSANCE_PROC:", ps_out or "(not found)")
