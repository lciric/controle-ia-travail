import hashlib
import shutil
from pathlib import Path

SCRATCH = Path(r"C:\Users\lciri\.gemini\antigravity-cli\brain\cd7c89b9-9752-4dac-b846-2c58efd89737\scratch")
SRC_DIR = SCRATCH / "lecture-sondes-v2-etalon"
DL = Path(r"C:\Users\lciri\Downloads")

def sha256_file(p: Path) -> str:
    h = hashlib.sha256()
    with p.open("rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()

rep_name = "rapport-resultats-sondes-v2-etalon-v1.md"
json_name = "synthese-partielle-r0-130-etalon-v1.json"

rep_h = sha256_file(SRC_DIR / rep_name)
json_h = sha256_file(SRC_DIR / json_name)

shutil.copy2(SRC_DIR / rep_name, DL / rep_name)
(DL / (rep_name + ".sha256")).write_bytes(f"{rep_h}  {rep_name}\n".encode("ascii"))
shutil.copy2(SRC_DIR / json_name, DL / json_name)
(DL / (json_name + ".sha256")).write_bytes(f"{json_h}  {json_name}\n".encode("ascii"))

assert sha256_file(DL / rep_name) == rep_h
assert sha256_file(DL / json_name) == json_h
print(f"DOWNLOADS_OK: {DL / rep_name} ({rep_h[:12]}...), {DL / json_name} ({json_h[:12]}...)")
