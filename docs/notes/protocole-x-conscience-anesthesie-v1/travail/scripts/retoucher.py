"""Applique des remplacements exacts (chacun doit apparaître une fois et une seule) à un ou plusieurs fichiers."""
import json, sys
spec = json.load(open(sys.argv[1], encoding='utf-8'))
for chemin in sys.argv[2:]:
    s = open(chemin, encoding='utf-8').read()
    for avant, apres in spec:
        n = s.count(avant)
        if n != 1:
            print(f"[{chemin}] {n} occurrence(s) pour : {avant[:70]!r}")
            if n == 0:
                continue
            sys.exit(1)
        s = s.replace(avant, apres)
    open(chemin, 'w', encoding='utf-8').write(s)
    print("ok", chemin)
