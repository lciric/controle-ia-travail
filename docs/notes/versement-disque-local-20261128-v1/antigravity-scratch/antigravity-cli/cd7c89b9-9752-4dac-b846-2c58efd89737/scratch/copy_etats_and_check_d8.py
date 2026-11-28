import hashlib
import os
import stat
from pathlib import Path

REPO = Path(r"C:\Users\lciri\OneDrive\Documents\controle-ia-travail")
SCRATCH = Path(r"C:\Users\lciri\.gemini\antigravity-cli\brain\cd7c89b9-9752-4dac-b846-2c58efd89737\scratch")
WT_EXEC = SCRATCH / "wt-b8-exec-v5"

EXPECTED_ETATS = "7329f08be94adda1ae0e5f44ea9d9b80dd7f614310343b39a39e87d1abab9e0c"
REL_ETATS = Path("docs/notes/barreau8-cote-moniteurs-entrees-v1/etats-lectures-iib-v1.json")

entrees_dir = REPO / "docs/notes/barreau8-cote-moniteurs-entrees-v1"
print("ENTREES_DIR:")
for p in sorted(entrees_dir.iterdir()):
    st = p.stat()
    print(f"  {p.name} size={st.st_size} mode={oct(st.st_mode)}")

dst_json = REPO / REL_ETATS
dst_sha = REPO / (str(REL_ETATS) + ".sha256")
if dst_json.exists():
    print("DST_JSON_ALREADY_EXISTS_SHA:", hashlib.sha256(dst_json.read_bytes()).hexdigest())
else:
    src_json = WT_EXEC / REL_ETATS
    src_sha = WT_EXEC / (str(REL_ETATS) + ".sha256")
    raw = src_json.read_bytes()
    h = hashlib.sha256(raw).hexdigest()
    assert h == EXPECTED_ETATS, f"SHA mismatch: {h}"
    try:
        dst_json.write_bytes(raw)
        dst_sha.write_bytes(src_sha.read_bytes())
        print("COPIED_ETATS_OK:", h)
    except Exception as e:
        print("COPY_ERR:", repr(e))

d8_dir = REPO / "donnees" / "20261114-001352-t07-lecture-reel"
print("D8_DIR_EXISTS:", d8_dir.exists())
if d8_dir.exists():
    for p in sorted(d8_dir.iterdir()):
        print(f"  D8_FILE: {p.name} size={p.stat().st_size}")

vers_dir = REPO / "versement" / "20261124-122719-rejeu-activations-voie-a"
print("VERS_DIR_EXISTS:", vers_dir.exists())
if vers_dir.exists():
    for p in sorted(vers_dir.rglob("*")):
        if p.is_file():
            print(f"  VERS_FILE: {p.relative_to(vers_dir)} size={p.stat().st_size}")
