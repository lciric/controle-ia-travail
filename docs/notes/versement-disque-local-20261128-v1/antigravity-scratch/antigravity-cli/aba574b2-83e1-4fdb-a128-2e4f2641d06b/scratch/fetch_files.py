import hashlib
import os
import pathlib
import subprocess
import sys

REPO = "lciric/controle-ia-travail"

FILES = [
    (
        "barreau8/cote-expose-pieces-lecture-v1",
        "docs/notes/barreau8-cote-expose-pieces-lecture-v1/specification-lectures-dommage-diffusion-course-v5-v1-brouillon3.md",
    ),
    (
        "c5d90370",
        "docs/notes/barreau8-cote-expose-pieces-lecture-v1/rapport-developpeur-code-lectures-v5-v1.md",
    ),
    ("c5d90370", "scripts/lecture_iib_1_dommage_v5.py"),
    ("c5d90370", "scripts/lecture_iib_2_diffusion_v5.py"),
    ("c5d90370", "scripts/lecture_iib_audit_r4_v5.py"),
    ("c5d90370", "src/controle_ia/iib/configuration_lectures_v5.py"),
    ("c5d90370", "src/controle_ia/iib/entrees_lectures_v5.py"),
    ("c5d90370", "src/controle_ia/iib/lectures_v5.py"),
    ("c5d90370", "tests/test_lectures_iib_v5_v1.py"),
]

TARGETS = [
    pathlib.Path(
        r"C:\Users\lciri\.gemini\antigravity-cli\brain\cd7c89b9-9752-4dac-b846-2c58efd89737\scratch\cl-code-lectures-v5"
    ),
    pathlib.Path(
        r"C:\Users\lciri\.gemini\antigravity-cli\brain\aba574b2-83e1-4fdb-a128-2e4f2641d06b\scratch\cl-code-lectures-v5"
    ),
]


def fetch_raw(ref: str, rel_path: str):
    url = f"repos/{REPO}/contents/{rel_path}?ref={ref}"
    proc = subprocess.run(
        ["gh", "api", "-H", "Accept: application/vnd.github.raw", url],
        capture_output=True,
    )
    if proc.returncode != 0:
        return None, proc.stderr.decode("utf-8", errors="replace")
    return proc.stdout, None


def save_all(rel_path: str, data: bytes):
    for root in TARGETS:
        dest = root / rel_path
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_bytes(data)


def main():
    for ref, rel_path in FILES:
        data, err = fetch_raw(ref, rel_path)
        if data is None:
            print(f"ERROR fetching {rel_path}@{ref}: {err}", file=sys.stderr)
            sys.exit(1)
        save_all(rel_path, data)
        sha = hashlib.sha256(data).hexdigest()
        print(f"OK  {sha}  {len(data):8d}  {rel_path} ({ref})")

        # Check for .sha256 companion
        sha_path = rel_path + ".sha256"
        sdata, _ = fetch_raw(ref, sha_path)
        if sdata is not None:
            save_all(sha_path, sdata)
            print(f"SHA {sdata.decode('utf-8', errors='replace').strip()}  [{sha_path}]")


if __name__ == "__main__":
    main()
