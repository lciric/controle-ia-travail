"""Cherche les clés secrètes des banques v3, v4 et v5 dans des fichiers à pousser — v1.

N'imprime jamais une clé : seulement, par fichier, le nombre d'écritures trouvées (décimal, hexadécimal minuscule et
majuscule, hexadécimal sur 32 chiffres, 16 octets gros- et petit-boutiste). Code 0 si rien n'est trouvé, 2 sinon.

Usage : python3 -I chercher_cles_v1.py DOSSIER_BANQUE CHEMIN [CHEMIN…]   (un chemin peut être un dossier : parcouru)
"""
import json, pathlib, sys

banque = pathlib.Path(sys.argv[1])
motifs = []
for v in ("v3", "v4", "v5"):
    e = int(json.loads((banque / f"banque-confrontation-{v}-cle.json").read_text(encoding="utf-8"))["entropie_seed_sequence"])
    h = format(e, "x")
    ecr = [str(e).encode(), h.encode(), h.upper().encode(), format(e, "032x").encode(), format(e, "032X").encode()]
    if e < 2 ** 128:
        ecr += [e.to_bytes(16, "big"), e.to_bytes(16, "little")]
    motifs.append((v, ecr))
fichiers = []
for c in sys.argv[2:]:
    p = pathlib.Path(c)
    fichiers += sorted(q for q in p.rglob("*") if q.is_file()) if p.is_dir() else [p]
total = 0
for f in fichiers:
    if f.name.endswith("-cle.json"):
        print(f"{f}\tREFUS : fichier de clé dans la liste à pousser"); total += 1; continue
    o = f.read_bytes()
    n = {v: sum(o.count(m) for m in ecr) for v, ecr in motifs}
    total += sum(n.values())
    print(f"{f}\t" + " ".join(f"{v}={k}" for v, k in n.items()))
print(f"fichiers : {len(fichiers)} ; écritures de clé trouvées : {total}")
sys.exit(2 if total else 0)
