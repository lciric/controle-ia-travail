"""Affiche la structure (clés, types, longueurs) du résultat de l'étage 1,
sans jamais descendre dans le bloc `criteres_mecaniques` (l'aide).
Usage : python3 -I -B structure_resultat_v1.py RESULTAT.json SORTIE.txt
"""
import json
import sys

AIDE = "criteres_mecaniques"


def decrire(obj, chemin, profondeur, lignes, max_prof=7):
    if isinstance(obj, dict):
        lignes.append(f"{'  ' * profondeur}{chemin}: dict[{len(obj)}]")
        if profondeur >= max_prof:
            return
        for k, v in obj.items():
            if k == AIDE:
                lignes.append(f"{'  ' * (profondeur + 1)}{k}: <aide, non ouverte>")
                continue
            decrire(v, k, profondeur + 1, lignes, max_prof)
    elif isinstance(obj, list):
        lignes.append(f"{'  ' * profondeur}{chemin}: list[{len(obj)}]")
        if obj and profondeur < max_prof:
            decrire(obj[0], chemin + "[0]", profondeur + 1, lignes, max_prof)
    else:
        rep = repr(obj)
        if len(rep) > 80:
            rep = rep[:80] + "..."
        lignes.append(f"{'  ' * profondeur}{chemin}: {type(obj).__name__} = {rep}")


def main():
    src, dst = sys.argv[1], sys.argv[2]
    with open(src, encoding="utf-8") as f:
        data = json.load(f)
    lignes = []
    decrire(data, "<racine>", 0, lignes)
    with open(dst, "w", encoding="utf-8") as f:
        f.write("\n".join(lignes) + "\n")


if __name__ == "__main__":
    main()
