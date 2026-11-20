"""Résumé de l'aide : tout sauf les dictionnaires par cellule (remplacés par
leur taille et un comptage de leurs mots).
Usage : python3 -I -B resumer_aide_v1.py AIDE.json SORTIE.txt
"""
import json
import sys
from collections import Counter


def compter_mots(d):
    c = Counter()
    def visite(x):
        if isinstance(x, dict):
            for k, v in x.items():
                if k == "mot" or k.startswith("mot") or k.startswith("clause"):
                    if isinstance(v, str):
                        c[f"{k}={v}"] += 1
                visite(v)
        elif isinstance(x, list):
            for v in x:
                visite(v)
    visite(d)
    return dict(c)


def reduire(x, prof=0):
    if isinstance(x, dict):
        out = {}
        for k, v in x.items():
            if k in ("par_cellule", "cellules", "par_cellule_et_rho_prime") or (isinstance(v, dict) and len(v) > 40):
                out[k] = {"<taille>": len(v), "<mots>": compter_mots(v)}
            else:
                out[k] = reduire(v, prof + 1)
        return out
    if isinstance(x, list):
        if len(x) > 30:
            return {"<liste>": len(x), "<premier>": reduire(x[0], prof + 1), "<mots>": compter_mots(x)}
        return [reduire(v, prof + 1) for v in x]
    return x


def main():
    src, dst = sys.argv[1], sys.argv[2]
    with open(src, encoding="utf-8") as f:
        a = json.load(f)["criteres_mecaniques"]
    with open(dst, "w", encoding="utf-8") as f:
        json.dump(reduire(a), f, ensure_ascii=False, indent=1)
        f.write("\n")


if __name__ == "__main__":
    main()
