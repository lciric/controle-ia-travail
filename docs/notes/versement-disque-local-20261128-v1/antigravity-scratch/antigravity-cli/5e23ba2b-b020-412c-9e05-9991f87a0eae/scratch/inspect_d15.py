import os, re, json, hashlib, pathlib

repo = pathlib.Path(r"C:\Users\lciri\OneDrive\Documents\controle-ia-travail")

def ls(rel):
    p = repo / rel
    if not p.exists():
        print(f"[MISSING] {rel}")
        return
    print(f"=== DIR {rel} ===")
    for root, dirs, files in os.walk(p):
        rel_root = os.path.relpath(root, repo)
        for f in sorted(files):
            print(f"  {rel_root}\\{f}")

for d in [
    "docs/notes/barreau8-cote-expose-pieces-lecture-v1",
    "docs/notes/barreau8-iib-v1",
    "docs/notes/rejeu-activations-saboteur-voie-a-v1",
    "docs/notes/saboteur-budget-ordre-etalonnage-v5",
    "brouillons/ii-b-saboteur-budget-v5",
    "registres/iib-reconception",
    "registres/iib-executante",
    "versement",
]:
    ls(d)

def grep_file(rel, pattern):
    p = repo / rel
    if not p.exists():
        print(f"[MISSING] {rel}")
        return
    print(f"=== GREP {rel} /{pattern}/ ===")
    rx = re.compile(pattern, re.I)
    for i, line in enumerate(p.read_text(encoding="utf-8", errors="replace").splitlines(), 1):
        if rx.search(line):
            print(f"  L{i}: {line[:260]}")

grep_file("registres/scellements-v1.md", r"oracle|etalonnage|voie-A|voie A|additif-ordre|20261123-043944|extrait-course|designation|regle|iib|v5")
grep_file("registres/go.md", r"GO-2026-11-22-75|voie A|oracle|etalonnage|20261123-043944|barreau 8|sondes|dommage|diffusion|D-15|D-13")
grep_file("registres/depenses.md", r"20261123|20261122|20261121|voie A|etalonnage|iib|saboteur|61859391|61875617|62031392")
grep_file("registres/decisions.md", r"20261123-043944|extrait-course|attestation-course|D-15|D-13|oracle.*d[eé]sign|r[eè]gle.*oracle|62031392|61875617|61859391|lectures-v5-executees|ETATS-COURSE-IIB|LIVRAISON-PASSE-IIB")
