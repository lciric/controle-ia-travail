"""Affiche la structure de la configuration (clés, types, longueurs) sans aucun texte — v1.
Rédacteur neuf du brouillon 7. Usage : python3 -B -I structure_config_v1.py CONFIG"""
import json, sys
cfg = json.load(open(sys.argv[1], encoding="utf-8"))
def voir(o, chemin, prof):
    if isinstance(o, dict):
        print("  " * prof + f"{chemin} : objet, {len(o)} clés")
        for k, v in o.items():
            voir(v, f"{chemin}.{k}", prof + 1)
    elif isinstance(o, list):
        print("  " * prof + f"{chemin} : liste, {len(o)} éléments, types {sorted({type(x).__name__ for x in o})}")
    elif isinstance(o, str):
        print("  " * prof + f"{chemin} : texte, {len(o)} caractères")
    else:
        print("  " * prof + f"{chemin} : {type(o).__name__}")
voir(cfg, "$", 0)
