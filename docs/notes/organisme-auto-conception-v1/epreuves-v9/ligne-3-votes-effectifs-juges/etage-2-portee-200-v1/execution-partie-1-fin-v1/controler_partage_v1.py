"""Geste 5 : contrôle sur pièce du partage (ligne 3, étage 2). Ne lit que le fichier passé en argument.

Contrôles : 100 témoins par moitié ; 50 et 50 par classe dans chaque moitié ; 10 et 10 par item (item non nul) ;
listes des moitiés sans doublon et disjointes ; comptes par strate égaux aux longueurs des listes.
N'imprime aucun identifiant : seulement des comptes et des verdicts. Code 0 si tout tient, 1 sinon.
"""
import json
import sys
from collections import Counter


def main(chemin: str) -> int:
    with open(chemin, "rb") as f:
        p = json.loads(f.read().decode("utf-8"))
    lecture, etalonnage, comptes = p["lecture"], p["etalonnage"], p["comptes"]
    par_classe = {"lecture": Counter(), "etalonnage": Counter()}
    par_item = {"lecture": Counter(), "etalonnage": Counter()}
    for s in comptes:
        for moitie in ("lecture", "etalonnage"):
            par_classe[moitie][s["classe"]] += s[moitie]
            if s.get("item") is not None:
                par_item[moitie][s["item"]] += s[moitie]
    classes = sorted(set(par_classe["lecture"]) | set(par_classe["etalonnage"]))
    items = sorted(set(par_item["lecture"]) | set(par_item["etalonnage"]))
    controles = {
        "lecture_100": len(lecture) == 100,
        "etalonnage_100": len(etalonnage) == 100,
        "sans_doublon": len(set(lecture)) == len(lecture) and len(set(etalonnage)) == len(etalonnage),
        "moities_disjointes": not (set(lecture) & set(etalonnage)),
        "comptes_egaux_aux_listes": sum(par_classe["lecture"].values()) == len(lecture)
        and sum(par_classe["etalonnage"].values()) == len(etalonnage),
        "deux_classes": len(classes) == 2,
        "classe_50_50": all(par_classe[m][c] == 50 for m in ("lecture", "etalonnage") for c in classes),
        "cinq_items": len(items) == 5,
        "item_10_10": all(par_item[m][i] == 10 for m in ("lecture", "etalonnage") for i in items),
    }
    sortie = {
        "fichier": chemin,
        "n_lecture": len(lecture),
        "n_etalonnage": len(etalonnage),
        "n_strates": len(comptes),
        "par_classe": {m: dict(sorted(par_classe[m].items())) for m in par_classe},
        "par_item": {m: dict(sorted(par_item[m].items())) for m in par_item},
        "controles": controles,
        "verdict": "tenu" if all(controles.values()) else "non tenu",
    }
    print(json.dumps(sortie, ensure_ascii=False, indent=1))
    return 0 if all(controles.values()) else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1]))
