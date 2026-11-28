import hashlib
import json
import pathlib
import subprocess
import sys

REPO = "lciric/controle-ia-travail"
REF = "c5d90370"
ROOT = pathlib.Path(
    r"C:\Users\lciri\.gemini\antigravity-cli\brain\aba574b2-83e1-4fdb-a128-2e4f2641d06b\scratch\cl-code-lectures-v5"
)

EXACT_FILES = [
    "src/controle_ia/__init__.py",
    "src/controle_ia/gardes.py",
    "src/controle_ia/scellement.py",
    "src/controle_ia/manifeste.py",
    "src/controle_ia/harnais/__init__.py",
    "src/controle_ia/harnais/run_harnais_factice.py",
    "src/controle_ia/harnais/formats.py",
    "src/controle_ia/t06/__init__.py",
    "src/controle_ia/t06/test_croise.py",
    "src/controle_ia/t06/cout.py",
    "scripts/mots_et_cout_t06_v3.py",
    "tests/iib_distillation_v5_outils.py",
    "tests/test_iib_lanceur_v5.py",
    "tests/iib_v5_outils.py",
]


def gh_raw(rel_path: str):
    url = f"repos/{REPO}/contents/{rel_path}?ref={REF}"
    p = subprocess.run(
        ["gh", "api", "-H", "Accept: application/vnd.github.raw", url],
        capture_output=True,
    )
    if p.returncode != 0:
        return None
    return p.stdout


def main():
    # List pure Python modules inside src/controle_ia/iib at c5d90370
    p = subprocess.run(
        ["gh", "api", f"repos/{REPO}/contents/src/controle_ia/iib?ref={REF}"],
        capture_output=True,
        text=True,
    )
    if p.returncode != 0:
        print("ERROR listing src/controle_ia/iib:", p.stderr, file=sys.stderr)
        sys.exit(1)
    entries = json.loads(p.stdout)
    iib_py = [
        e["path"]
        for e in entries
        if e["type"] == "file" and e["name"].endswith(".py")
    ]

    all_paths = sorted(set(EXACT_FILES + iib_py))
    for rel in all_paths:
        dest = ROOT / rel
        if dest.exists():
            continue
        data = gh_raw(rel)
        if data is None:
            print(f"MISS {rel}")
            continue
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_bytes(data)
        print(f"OK   {hashlib.sha256(data).hexdigest()[:12]}  {rel}")


if __name__ == "__main__":
    main()
