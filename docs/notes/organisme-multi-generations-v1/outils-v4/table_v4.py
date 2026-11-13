"""Table par monde des parties v4 (lecture seule des `partie-v4-monde-*.json`) : composantes certifiées, restantes après la
génération 1 (avec et sans masquage), neuves certifiées en générations 2 et 3, fausses découvertes. Bibliothèque standard.
Usage : `python3 -I -B table_v4.py DOSSIER_SORTIES_V4 SORTIE.json`."""
import glob
import json
import os
import sys


def main(argv):
    if len(argv) != 3 or os.path.exists(argv[2]):
        print("usage : table_v4.py DOSSIER SORTIE.json (neuve)")
        return 2
    lignes = []
    for p in sorted(glob.glob(os.path.join(argv[1], "partie-v4-monde-*.json")), key=lambda x: int(x.rsplit("-", 1)[1].split(".")[0])):
        r = json.load(open(p, encoding="utf-8"))["resultat"]
        if not r["conforme"]:
            lignes.append({"monde": r["monde"], "conforme": False, "refus": r["refus"]})
            continue
        cl = {k: v["classe"] for k, v in r["c8"].items()}
        gm = r["masquage"]["generations"]
        lignes.append({
            "monde": r["monde"], "conforme": True, "refus": r["refus"],
            "certifiees": [f"{k}:{cl[k]}" for k in r["certifiees"]],
            "conditionnelles": {k: {"condition": c, "condition_certifiee": r["c8"][c]["certifiee"],
                                    "puissance_c8": r["c8"][k]["puissance"], "part_marginale": r["part_marginale"].get(k)}
                                for k, c in r["conditions"].items()},
            "captees_g1": gm[0]["captes"],
            "restantes_apres_g1_masquage": [f"{k}:{cl[k]}" for k in r["masquage"]["certifiees_non_captees_apres_g1"]],
            "restantes_apres_g1_sans_masquage": [f"{k}:{cl[k]}" for k in r["sans_masquage_g1"]["certifiees_non_captees_apres_g1"]],
            "neuves_certifiees_g2": r["masquage"]["certifiees_neuves_g2"], "neuves_certifiees_g3": r["masquage"]["certifiees_neuves_g3"],
            "retenues": [h["retenues"] for h in gm], "promues": [h["promues"] for h in gm],
            "fausses_decouvertes": [h["fausses_decouvertes"] for h in gm]})
    with open(argv[2], "x", encoding="utf-8") as f:
        json.dump(lignes, f, ensure_ascii=False, indent=1, sort_keys=True)
    for l in lignes:
        print(json.dumps(l, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
