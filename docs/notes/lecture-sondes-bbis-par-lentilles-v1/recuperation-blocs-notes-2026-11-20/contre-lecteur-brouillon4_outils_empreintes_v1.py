# Recalcul des empreintes citées par les lignes neuves du brouillon 4 (contre-lecteur, 2026-11-19).
# Index : empreintes SHA-256 des fichiers suivis de la branche des lentilles (HEAD) et de origin/main, hors chemins cloisonnés.
import hashlib, re, subprocess, sys
INTERDITS = ("diag/", "runs/", "docs/verdicts/", "brouillons/ii-b-saboteur-budget-v1/")
def blobs(ref):
    out = subprocess.run(["git", "ls-tree", "-r", ref], capture_output=True, text=True, check=True).stdout
    for l in out.splitlines():
        meta, chemin = l.split("\t", 1)
        if chemin.startswith(INTERDITS) or "consigne-privee" in chemin or "conception-ii-b" in chemin: continue
        yield meta.split()[2], chemin
index = {}
for ref in ("HEAD", "origin/main"):
    objs = list(blobs(ref))
    p = subprocess.run(["git", "cat-file", "--batch"], input="\n".join(o for o, _ in objs).encode() + b"\n", capture_output=True, check=True).stdout
    pos = 0
    for o, chemin in objs:
        nl = p.index(b"\n", pos); taille = int(p[pos:nl].split()[2]); contenu = p[nl+1:nl+1+taille]; pos = nl + 1 + taille + 1
        index.setdefault(hashlib.sha256(contenu).hexdigest(), set()).add(f"{ref}:{chemin}")
b3 = open(sys.argv[1], encoding="utf-8").read(); b4 = open(sys.argv[2], encoding="utf-8").read()
neuves = [l for l in b4.splitlines() if l not in set(b3.splitlines())]
texte = "\n".join(neuves)
entieres = sorted(set(re.findall(r"(?<![0-9a-f])[0-9a-f]{64}(?![0-9a-f])", texte)))
print("empreintes entières dans les lignes neuves :", len(entieres))
for h in entieres:
    print(h[:12], "->", sorted(index.get(h, {"INTROUVABLE dans les deux arbres (hors cloisonnés)"}))[:3])
prefixes = sorted(set(re.findall(r"`([0-9a-f]{8})…`", texte)))
print("préfixes « xxxxxxxx… » dans les lignes neuves :", len(prefixes))
for p8 in prefixes:
    t = sorted({c for h, cs in index.items() if h.startswith(p8) for c in cs})
    print(p8, "->", t[:3] if t else "aucun fichier suivi (peut être un commit ou une pièce hors dépôt)")
