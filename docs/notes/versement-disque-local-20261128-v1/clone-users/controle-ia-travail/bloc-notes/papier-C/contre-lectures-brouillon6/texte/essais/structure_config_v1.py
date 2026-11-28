"""Structure de la configuration brouillon 3 : clés, types, longueurs ; aucune chaîne affichée."""
import json, sys
cfg = json.load(open(sys.argv[1], encoding="utf-8"))
def walk(x, chemin, prof):
    if isinstance(x, dict):
        print(f"{'  '*prof}{chemin} : objet ({len(x)} clés)")
        if prof < 3:
            for k, v in x.items():
                walk(v, f"{chemin}.{k}", prof + 1)
    elif isinstance(x, list):
        types = sorted({type(e).__name__ for e in x})
        print(f"{'  '*prof}{chemin} : liste ({len(x)}) {types}")
    elif isinstance(x, str):
        print(f"{'  '*prof}{chemin} : chaîne ({len(x)} caractères)")
    else:
        print(f"{'  '*prof}{chemin} : {type(x).__name__} = {x!r}")
walk(cfg, "$", 0)
