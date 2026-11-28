import json
import pathlib

s = pathlib.Path(r"C:\Users\lciri\.gemini\antigravity-cli\brain\47f4b159-cbf8-4611-bc3f-fc9630ef47d9\scratch")
n = 0
for d in (s / "phase2_curated", s / "v2_lit" / "lit_curated"):
    for f in d.glob("*.json"):
        if json.loads(f.read_text(encoding="utf-8")).get("modele_curation") == "flash_lite":
            f.unlink()
            n += 1
            print("retire", f.name)
print("lots flash_lite retires:", n)
print("V1 lots valides:", len(list((s / "phase2_curated").glob("batch_*.json"))), "/ 246")
print("LIT lots valides:", len(list((s / "v2_lit" / "lit_curated").glob("lit_batch_*.json"))), "/ 318")
