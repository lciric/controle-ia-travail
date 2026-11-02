"""Structure de la sortie scellée : clés, types, tailles (aucune écriture hors de a1-audit-v1)."""
import json, sys
E = "/tmp/claude-0/-home-claude/03748db6-42ca-5241-871c-5399d39c1451/scratchpad/a1-audit-v1/entree/sortie/"
def resume(o, prof=0, maxp=3, nom="racine"):
    pad = "  " * prof
    if isinstance(o, dict):
        print(f"{pad}{nom}: dict[{len(o)}]")
        if prof < maxp:
            for i, (k, v) in enumerate(o.items()):
                if i >= 40: print(f"{pad}  … ({len(o)-40} de plus)"); break
                resume(v, prof+1, maxp, repr(k))
    elif isinstance(o, list):
        print(f"{pad}{nom}: list[{len(o)}]")
        if prof < maxp and o:
            resume(o[0], prof+1, maxp, "[0]")
    else:
        s = repr(o)
        print(f"{pad}{nom}: {type(o).__name__} = {s[:120]}")
for f, p in (("sortie", "attaque-goodhart-v2.json"), ("manifeste", "manifeste.json")):
    o = json.load(open(E + p))
    print("=" * 20, p)
    resume(o, 0, int(sys.argv[1]) if len(sys.argv) > 1 else 2)
