"""Indices (1 à 16) des formulations qui portent chaque fente, par famille ; et indices où figure « si / if »
(mot entier), pour la réserve 14. Aucun texte affiché."""
import json, re, sys
cfg = json.load(open(sys.argv[1], encoding="utf-8"))
fentes = sorted(set(re.findall(r"\{([A-Z_]+)\}", json.dumps(cfg["vivier"]))))
for fam, liste in cfg["vivier"].items():
    print(f"--- {fam}")
    for f in fentes:
        idx = [i for i, s in enumerate(liste, 1) if "{" + f + "}" in s]
        if idx: print(f"   {{{f}}} : {idx}")
    print("   mot « if » :", [i for i, s in enumerate(liste, 1) if re.search(r"\bif\b", s, re.I)])
    print("   mot « unless/otherwise/or else » :", [i for i, s in enumerate(liste, 1) if re.search(r"\b(unless|otherwise|or else)\b", s, re.I)])
print("--- témoins : fentes", [ (i, sorted(set(re.findall(r'\{([A-Z_]+)\}', s)))) for i, s in enumerate(cfg["temoins_sham"], 1) if "{" in s])
print("    mot « if » :", [i for i, s in enumerate(cfg["temoins_sham"], 1) if re.search(r"\bif\b", s, re.I)])
