import hashlib
import os
import subprocess
import sys
from pathlib import Path

BASE = Path(r"C:\Users\lciri\.gemini\antigravity-cli\brain\54d22d59-e9ed-4f2e-9191-bbb2bfc9cf24\scratch\note-attelage\sources")
REPO = "lciric/controle-ia-travail"
RUN_DIR = "runs/collisionneur-protocole-x-attelage-plan-turing-v1-20261124-181153"
REF_RUN = "831a7e38"

FILES_MAIN = [
    "docs/notes/protocole-x-v2/protocole-x-v2.md",
    "docs/notes/protocole-x-v2/protocole-x-v2-1-boucle-fermee.md",
    "registres/livre-cout-protocole-x-v1.md",
]

FILES_RUN = [
    f"{RUN_DIR}/question-etage3.md",
    f"{RUN_DIR}/question-etage3.md.sha256",
    f"{RUN_DIR}/faits.md",
    f"{RUN_DIR}/faits.md.sha256",
    f"{RUN_DIR}/engagement.md",
    f"{RUN_DIR}/engagement.md.sha256",
    f"{RUN_DIR}/especes.json",
    f"{RUN_DIR}/especes.json.sha256",
    f"{RUN_DIR}/etat.md",
    f"{RUN_DIR}/verifier-fin.log",
    f"{RUN_DIR}/verifier-fin.log.sha256",
    f"{RUN_DIR}/journal.jsonl",
    f"{RUN_DIR}/journal-etage3.txt",
    f"{RUN_DIR}/lecture-double/lecture-opus-v1.md",
    f"{RUN_DIR}/lecture-double/lecture-opus-v1.md.sha256",
    f"{RUN_DIR}/lecture-double/lecture-astra-v1.md",
    f"{RUN_DIR}/lecture-double/lecture-astra-v1.md.sha256",
    f"{RUN_DIR}/lecture-double/journal-lecteur-astra.txt",
    f"{RUN_DIR}/lecture-double/journal-lecteur-astra-2.txt",
    f"{RUN_DIR}/lecture-double/dossier-aveugle-v1.md.sha256",
]

for tour in ["E3-T1-conception", "E3-T2-critique-croisee", "E3-T3-reponse"]:
    for lettre in ["A", "B", "C", "D", "E"]:
        FILES_RUN.append(f"{RUN_DIR}/cellules/{tour}-{lettre}.md")
        FILES_RUN.append(f"{RUN_DIR}/cellules/{tour}-{lettre}.md.sha256")


def fetch_file(rel_path: str, ref: str, sub: str) -> None:
    dest = BASE / sub / rel_path
    dest.parent.mkdir(parents=True, exist_ok=True)
    cmd = [
        "gh",
        "api",
        "-H",
        "Accept: application/vnd.github.raw+json",
        f"repos/{REPO}/contents/{rel_path}?ref={ref}",
    ]
    res = subprocess.run(cmd, capture_output=True)
    if res.returncode != 0:
        print(f"ERREUR {ref}:{rel_path} -> {res.stderr.decode('utf-8', 'replace')}", file=sys.stderr)
        sys.exit(1)
    dest.write_bytes(res.stdout)
    h = hashlib.sha256(res.stdout).hexdigest()
    print(f"OK [{ref}] {rel_path} ({len(res.stdout)} octets) sha256={h[:16]}...")


def main() -> None:
    extra = sys.argv[1:]
    for p in FILES_MAIN:
        fetch_file(p, "main", "main")
    for p in FILES_RUN:
        fetch_file(p, REF_RUN, "run")
    for spec in extra:
        ref, p = spec.split(":", 1)
        fetch_file(p, ref, "ref-style")


if __name__ == "__main__":
    main()
