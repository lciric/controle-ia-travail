"""Marge de compétence honnête au pilote : part pondérée des paires « proposition, contrôle de référence » jugées couvertes
par les étiqueteurs fidèles (série 1), dans la population des paires et non dans le sous-échantillon stratifié.

Usage : python d_couverture_honnete_ponderee.py <depot> <sortie.json>

Le sous-échantillon étiqueté (480 paires) est stratifié par famille et par décision du juge de 8 milliards, 80 paires par
strate (préenregistrement du pilote, « Métrique ») : sa part brute de « Yes » (0,181 pour les contrôles) n'est PAS la part
de la population. L'estimation pondère chaque paire par l'inverse de sa probabilité de tirage (champ `poids`).
Témoin : la part brute des contrôles doit retrouver 0,181 (`brouillons/T0.5-pilote-double-etiquetage-v1/resultat.md`).
Aucun texte n'est lu : étiquettes, familles, strates et poids seulement.
"""
import json, pathlib, sys
from collections import defaultdict
depot, SORTIE = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2])
e = json.load(open(depot / "diag/20261012-150724-t05-pilote-analyse/echantillon-etiquetage.json"))["resultat"]
l = json.load(open(depot / "diag/20261012-150724-t05-pilote-analyse/etiquettes.json"))["resultat"]["elements"]
res = {"paires_totales": e["paires_totales"], "strates_population": e["strates"], "familles": {}}
par = defaultdict(list)
for x in l:
    par[x["famille"]].append(x)
for fam, xs in par.items():
    brut = sum(x["etiquette"] == "Yes" for x in xs) / len(xs)
    w = sum(x["poids"] for x in xs)
    pond = sum(x["poids"] * (x["etiquette"] == "Yes") for x in xs) / w
    strates = {}
    for oui in (True, False):
        s = [x for x in xs if bool(x["oui_8b"]) == oui]
        strates["juge_oui" if oui else "juge_non"] = {"n": len(s), "part_yes": sum(x["etiquette"] == "Yes" for x in s) / len(s), "poids_unitaire": s[0]["poids"]}
    pop = e["strates"][f"{fam}|oui"] + e["strates"][f"{fam}|non"]
    res["familles"][fam] = {"n_etiquetees": len(xs), "part_brute_yes": brut, "part_ponderee_yes": pond, "somme_des_poids": w,
                            "paires_de_la_population": pop, "part_oui_du_juge_dans_la_population": e["strates"][f"{fam}|oui"] / pop, "strates": strates}
    print(fam, "| brute", round(brut, 4), "| pondérée", round(pond, 4), "| population", pop, "| strates", json.dumps(strates))
res["temoin"] = {"part_brute_controles": res["familles"]["controls"]["part_brute_yes"], "attendu": 0.181}
SORTIE.write_text(json.dumps(res, indent=1, ensure_ascii=False), encoding="utf-8")
print("TEMOIN", res["temoin"])
