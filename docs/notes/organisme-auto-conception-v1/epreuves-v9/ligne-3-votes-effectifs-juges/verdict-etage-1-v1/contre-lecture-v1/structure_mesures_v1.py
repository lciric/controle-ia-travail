"""Structure du fichier des mesures : noms de cles et types seulement, AUCUNE valeur.

Contre-lecteur, modele F. Sert a ecrire le programme de rejeu sans rien lire
des mesures avant les controles avant lecture.
Usage : python3 structure_mesures_v1.py CHEMIN_JSON [PROFONDEUR]
"""
import json
import sys


def forme(x, prof, maxprof, indent):
    pad = "  " * indent
    if isinstance(x, dict):
        cles = list(x.keys())
        print(f"{pad}dict[{len(cles)}]")
        if prof >= maxprof:
            print(f"{pad}  cles: {cles[:40]}")
            return
        # dictionnaire homogene a beaucoup de cles : trois premieres seulement
        montre = cles if len(cles) <= 45 else cles[:3]
        for k in montre:
            print(f"{pad}  {k!r}:")
            forme(x[k], prof + 1, maxprof, indent + 2)
        if len(montre) < len(cles):
            print(f"{pad}  ... ({len(cles)} cles ; dernieres : {cles[-2:]})")
    elif isinstance(x, list):
        types = sorted({type(e).__name__ for e in x})
        print(f"{pad}list[{len(x)}] de {types}")
        if x and isinstance(x[0], (dict, list)) and prof < maxprof:
            print(f"{pad}  [0]:")
            forme(x[0], prof + 1, maxprof, indent + 2)
    else:
        print(f"{pad}{type(x).__name__}")


def main():
    chemin = sys.argv[1]
    maxprof = int(sys.argv[2]) if len(sys.argv) > 2 else 6
    with open(chemin, encoding="utf-8") as f:
        d = json.load(f)
    forme(d, 0, maxprof, 0)


if __name__ == "__main__":
    main()
