"""Contre-lecture du brouillon 6 : empreintes des deux consignes et compte des marques (aucun appel de modèle)."""
import hashlib, re, sys
def blocs(chemin):
    lignes = open(chemin, encoding="utf-8").read().split("\n")
    sortie, dedans, cur = [], False, []
    for l in lignes:
        if l.startswith("```"):
            if dedans:
                sortie.append("\n".join(cur)); cur = []
            dedans = not dedans
            continue
        if dedans:
            cur.append(l)
    return sortie
for f in sys.argv[1:]:
    b = blocs(f)
    print(f, "blocs :", len(b))
    for i, t in enumerate(b):
        print(" bloc", i, hashlib.sha256(t.encode()).hexdigest(), len(t), "car.",
              {m: t.count(m) for m in ("{title}", "{proposal}", "{controls}", "{plan}", "{reference}")})
