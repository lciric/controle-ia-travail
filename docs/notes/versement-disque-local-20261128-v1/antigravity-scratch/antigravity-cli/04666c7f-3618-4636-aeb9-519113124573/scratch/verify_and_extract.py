import hashlib
import pathlib
import subprocess
import sys

repo = r"C:\Users\lciri\OneDrive\Documents\controle-ia-travail"
wt = pathlib.Path(r"C:\Users\lciri\.gemini\antigravity-cli\brain\cd7c89b9-9752-4dac-b846-2c58efd89737\scratch\wt-b8-exec-v5")
dest = pathlib.Path(r"C:\Users\lciri\.gemini\antigravity-cli\brain\cd7c89b9-9752-4dac-b846-2c58efd89737\scratch\jetoniseur-v1")
commit = "e5677bbf2696e9364da7f4bf191abcc5de16eabc"

print("=== RUN DIR FILES ===")
run_dir = wt / "runs" / "20261125-052722-iib-lecture-1-dommage-v5"
for p in sorted(run_dir.iterdir()):
    print(p.name)

print("=== CHECK LECTURE 1 SHA256 COMPANIONS ===")
targets = [
    "diag/20261123-043944-iib-course-reel/lecture-iib-1-dommage-exploratoire-non-opposable-v1.json",
    "runs/20261125-052722-iib-lecture-1-dommage-v5/manifeste.json",
]
all_ok = True
for rel in targets:
    p = wt / rel
    s = wt / (rel + ".sha256")
    actual = hashlib.sha256(p.read_bytes()).hexdigest()
    comp = s.read_text(encoding="utf-8").strip() if s.exists() else "MISSING"
    ok = (comp.split()[0] == actual) if s.exists() else False
    all_ok = all_ok and ok
    print(f"{rel} | actual={actual} | companion={comp} | match={ok}")

print("=== CHECK & EXTRACT TOKENIZER RAW BYTES ===")
print((dest / "LISEZMOI.md").read_text(encoding="utf-8"))
expected = {}
for line in (dest / "empreintes-jetoniseur-v1.txt").read_text(encoding="utf-8").splitlines():
    if line.strip():
        h, name = line.strip().split()
        expected[name] = h

tok_ok = True
for name in ["config.json", "generation_config.json", "tokenizer.json", "tokenizer_config.json"]:
    raw = subprocess.check_output(["git", "-C", repo, "cat-file", "blob", f"{commit}:jetoniseur/{name}"])
    out = dest / "jetoniseur" / name
    out.write_bytes(raw)
    h = hashlib.sha256(out.read_bytes()).hexdigest()
    ok = (h == expected[name])
    tok_ok = tok_ok and ok
    print(f"jetoniseur/{name} | actual={h} | expected={expected[name]} | match={ok}")

if not all_ok or not tok_ok:
    sys.exit(2)
