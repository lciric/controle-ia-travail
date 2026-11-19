"""Affiche les seuls NOMS de champs d'un fichier JSON lu sur l'entrée standard (jamais une valeur).
Usage : python3 -I cles_json.py [chemin.pointe ...]  -> pour chaque chemin, liste triée des clés du dictionnaire visé.
Sans argument : clés de la racine."""
import json, sys
d = json.load(sys.stdin)
chemins = sys.argv[1:] or [""]
for ch in chemins:
    x = d
    ok = True
    for part in [p for p in ch.split(".") if p]:
        if isinstance(x, dict) and part in x:
            x = x[part]
        else:
            ok = False
            break
    if not ok:
        print(f"[{ch or 'racine'}] : chemin absent")
    elif isinstance(x, dict):
        print(f"[{ch or 'racine'}] : dictionnaire, clés = {sorted(x.keys())}")
    else:
        print(f"[{ch or 'racine'}] : présent (valeur non affichée)")
