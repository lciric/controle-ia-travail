"""Les dix PDF de correction-v6/pdf/ contre la v1 (citations-synthese-v1.json, contrôlé par empreinte), contre leur
compagnon, et contre la table du traitement (empreinte et nombre de pages). Lecture seule.
Usage : python3 -I -B pdf_c6_contre_v1.py
"""
import hashlib, json, re, subprocess, sys
from pathlib import Path
RD = Path("/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/revue-detection")
J = RD / "redaction/citations-synthese-v1.json"
TR = RD / "traitement-verifications-v5-par-correcteur-v1.md"
assert hashlib.sha256(J.read_bytes()).hexdigest() == "2186860541680a114add5f71c27895e8eba2d614ff2a2aa671756fff7355692c"
assert hashlib.sha256(TR.read_bytes()).hexdigest() == "aabed8bca47cd9fe7cf7e530267afef121b7e9fa75973ec40b53cf44c386d7ab"
ref = {k: v for k, v in json.loads(J.read_bytes())["pdfs"].items()}
table = {}
for l in TR.read_text(encoding="utf-8").splitlines():
    m = re.match(r"\| (\w+) \| `([^`]+)` \| (\d+) \| `([0-9a-f]{64})` \| oui \|", l)
    if m:
        table[m.group(1)] = (m.group(2), int(m.group(3)), m.group(4))
fautes = 0
print(f"# {len(table)} lignes dans la table du traitement")
for cle, (rel, pages, sha) in sorted(table.items()):
    p = RD / "correction-v6/pdf" / rel
    h = hashlib.sha256(p.read_bytes()).hexdigest()
    comp = p.with_name(p.name + ".sha256").read_text().split()
    npages = int(re.search(r"Pages:\s+(\d+)", subprocess.run(["pdfinfo", str(p)], capture_output=True, text=True).stdout).group(1))
    v1 = ref[cle]["sha256"]; v1nom = Path(ref[cle]["chemin"]).name
    ok = h == v1 == sha == comp[0] and comp[1] == p.name and npages == pages and v1nom == p.name
    fautes += not ok
    print(f"{'ÉGAL' if ok else 'FAUTE'} | {cle} | {rel} | calculée {h[:16]}… | v1 {v1[:16]}… ({v1nom}) | compagnon {comp[0][:16]}… | table {sha[:16]}… | pages {npages}/{pages}")
print(f"# BILAN : {fautes} faute(s)")
sys.exit(1 if fautes else 0)
