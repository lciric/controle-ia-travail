"""Complements au rejeu des predictions : P4 contre une autre reference (poids egaux),
repliques ecartees du bras N, plus petite distance a une borne de tolerance.

Contre-lecteur, modele F. Bibliotheque standard seule, aucun tirage.
Usage : python3 complements_predictions_contre_lecteur_v1.py MESURES.json SORTIE.json
"""
import json
import os
import sys


def main():
    mesures, sortie = sys.argv[1], sys.argv[2]
    if os.path.exists(sortie):
        raise SystemExit("refus : la sortie existe deja")
    with open(mesures, encoding="utf-8") as f:
        d = json.load(f)
    ea = d["estimateur_et_agregation"]
    R = {}
    cs = [c for c in ea if c["J"] == 5 and c["rho_grille"] >= 0.6 - 1e-12]

    def ident(c):
        return {"loi": c["loi"], "profil": c["profil"], "rho": c["rho_grille"], "n": c["n"],
                "repliques": c["repliques"],
                "repliques_ecartees_bras_N": c["bras_N_votes_effectifs_indefinis"]}

    for nom, ref in (("majorite_stricte", "F_majorite_stricte"), ("poids_egaux", "poids_egaux"),
                     ("unanimite", "U")):
        g = [(c["bras"][ref]["erreur_equilibree"] - c["bras"]["N"]["erreur_equilibree"], c)
             for c in cs]
        gm, cm = max(g, key=lambda x: x[0])
        R[f"P4_gain_de_N_contre_{nom}"] = {"cellules": len(g), "max": gm, "cellule": ident(cm),
                                           "cellules_a_0.02_ou_plus": sum(1 for x, _ in g if x >= 0.02)}
    ec = sorted(c["bras_N_votes_effectifs_indefinis"] for c in cs)
    R["bras_N_repliques_ecartees_rho_0.6_ou_plus"] = {
        "min": ec[0], "mediane": ec[len(ec) // 2], "max": ec[-1],
        "cellules_avec_plus_de_100_ecartees": sum(1 for x in ec if x > 100),
        "cellule_du_max": ident(max(cs, key=lambda c: c["bras_N_votes_effectifs_indefinis"]))}
    # plus petite distance a une borne
    best = None
    for c in ea:
        e = c["estimateur"]
        for nomv, v, bornes in (("biais", abs(e["biais"]), [0.05]), ("eqm", e["eqm"], [0.10]),
                                ("couverture", e["couverture"], [0.90, 0.98]),
                                ("part_indefini", e["part_indefini"], [0.02])):
            for b in bornes:
                dist = abs(v - b)
                if best is None or dist < best["distance"]:
                    best = {"distance": dist, "grandeur": nomv, "valeur": v, "borne": b,
                            "J": c["J"], "loi": c["loi"], "profil": c["profil"],
                            "rho": c["rho_grille"], "n": c["n"]}
    R["plus_petite_distance_a_une_borne_sur_780"] = best
    with open(sortie, "w", encoding="utf-8") as f:
        json.dump(R, f, ensure_ascii=False, indent=1)
        f.write("\n")
    print(json.dumps(R, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
