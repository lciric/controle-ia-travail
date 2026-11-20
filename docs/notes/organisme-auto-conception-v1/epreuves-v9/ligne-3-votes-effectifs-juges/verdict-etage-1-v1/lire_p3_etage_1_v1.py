"""Lecture de la prédiction P3 (PR l. 135) sous ses quatre lectures (bras C ou
bras P ; contre la majorité stricte ou contre les poids égaux), cinq juges,
et sous les deux sens de la clause « aucun gain en blocs ».
gain = erreur équilibrée de la référence − erreur équilibrée du bras étalonné
(positif : le bras étalonné fait mieux). Moyennes sur 2 000 répliques.
N'ouvre pas `criteres_mecaniques`. Aucun tirage.
Usage : python3 -I -B lire_p3_etage_1_v1.py RESULTAT.json SORTIE.json
"""
import json
import sys

LECTURES = [("C", "F_majorite_stricte"), ("P", "F_majorite_stricte"),
            ("C", "poids_egaux"), ("P", "poids_egaux")]
EGAUX = {"egal_0.05", "egal_0.1", "egal_0.2", "egal_0.3"}
DISSYM = {"severe", "indulgent"}


def gain(e, bras, ref):
    return e["bras"][ref]["erreur_equilibree"] - e["bras"][bras]["erreur_equilibree"]


def main():
    src, dst = sys.argv[1], sys.argv[2]
    with open(src, encoding="utf-8") as f:
        data = json.load(f)
    data.pop("criteres_mecaniques", None)
    ea = [e for e in data["estimateur_et_agregation"] if e["J"] == 5]
    ech_tous = [e for e in ea if e["loi"] == 1 and e["profil"] in EGAUX | DISSYM]
    ech_egaux = [e for e in ech_tous if e["profil"] in EGAUX]
    blocs = [e for e in ea if e["loi"] == 4 and e["n"] == 400 and e["rho_grille"] >= 0.6 - 1e-12]
    out = {"definition_gain": "EE(référence) − EE(bras étalonné), moyennes sur 2 000 répliques",
           "cellules_clause_1_loi_1_taux_egaux_entre_juges": len(ech_tous),
           "cellules_clause_1_loi_1_taux_egaux_seulement": len(ech_egaux),
           "cellules_clause_2_loi_4_n400_rho_ge_0_6": len(blocs),
           "lectures": {}}
    for bras, ref in LECTURES:
        g1 = [gain(e, bras, ref) for e in ech_tous]
        g1e = [gain(e, bras, ref) for e in ech_egaux]
        g2 = [(gain(e, bras, ref), e["profil"], e["rho_grille"]) for e in blocs]
        sans = sum(1 for g, _, _ in g2 if g <= 0)
        avec = sum(1 for g, _, _ in g2 if g > 0)
        gmax2 = max(g2)
        clause1 = max(g1) >= 0.02
        clause2_cellule = sans > 0          # convention déclarée : atteinte dans une cellule
        clause2_toutes = avec == 0          # autre sens : aucun gain dans aucune cellule
        out["lectures"][f"{bras} contre {ref}"] = {
            "clause_1_plus_grand_gain_168": max(g1),
            "clause_1_plus_grand_gain_112_taux_egaux": max(g1e),
            "clause_1_atteinte": clause1,
            "clause_2_sans_gain": sans, "clause_2_avec_gain": avec,
            "clause_2_plus_grand_gain": gmax2[0],
            "clause_2_cellule_du_plus_grand_gain": {"profil": gmax2[1], "rho": gmax2[2]},
            "clause_2_gain_0_02_atteint_quelque_part": any(g >= 0.02 for g, _, _ in g2),
            "clause_2_atteinte_convention_declaree": clause2_cellule,
            "clause_2_atteinte_sens_aucune_cellule_avec_gain": clause2_toutes,
            "mot_convention_declaree": "réfutée" if (clause1 or clause2_cellule) else "non réfutée",
            "mot_sens_aucune_cellule": "réfutée" if (clause1 or clause2_toutes) else "non réfutée",
        }
    with open(dst, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
        f.write("\n")


if __name__ == "__main__":
    main()
