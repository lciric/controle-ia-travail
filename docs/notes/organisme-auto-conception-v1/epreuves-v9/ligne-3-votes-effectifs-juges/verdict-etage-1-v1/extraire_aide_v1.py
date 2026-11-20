"""Extrait le bloc `criteres_mecaniques` (l'aide, marquée telle) du résultat,
APRÈS l'application propre des critères (geste 5 du mandat).
Usage : python3 -I -B extraire_aide_v1.py RESULTAT.json SORTIE.json
"""
import json
import sys


def main():
    src, dst = sys.argv[1], sys.argv[2]
    with open(src, encoding="utf-8") as f:
        data = json.load(f)
    aide = data.get("criteres_mecaniques")
    with open(dst, "w", encoding="utf-8") as f:
        json.dump({"marque": "AIDE du code (criteres_mecaniques), jamais le verdict",
                   "criteres_mecaniques": aide}, f, ensure_ascii=False, indent=1)
        f.write("\n")


if __name__ == "__main__":
    main()
