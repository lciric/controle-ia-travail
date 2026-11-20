"""Contrôles avant lecture (mandat, geste 2) : mélange planté de l'alarme
(A2 l. 104) et P2 (PR l. 134 et l. 316). N'ouvre pas `criteres_mecaniques`.
Usage : python3 -I -B controles_avant_lecture_v1.py RESULTAT.json SORTIE.json
"""
import itertools
import json
import sys

ATTENDU_MELANGE = {
    "suites_qui_changent": 1000,
    "suites_a_effet": 500,
    "suites_sans_effet": 500,
    "suites_sans_changement": 1000,
}
REGLES_P2 = ["S_1", "S_2", "U", "F_au_moins_un"]
BORNE_P2 = 0.02
PREDIT_P2 = 0.01


def main():
    src, dst = sys.argv[1], sys.argv[2]
    with open(src, encoding="utf-8") as f:
        data = json.load(f)
    data.pop("criteres_mecaniques", None)

    # C0-a
    melange = []
    ok_melange = True
    ms = []
    for e in data["alarme"]:
        c = e["comptes_du_melange_plante"]
        bon = all(c.get(k) == v for k, v in ATTENDU_MELANGE.items()) and e["suites"] == 2000
        ok_melange &= bon
        ms.append(e["m"])
        melange.append({"m": e["m"], "comptes": c, "suites": e["suites"], "conforme": bon})
    ok_melange &= sorted(ms) == [10, 20, 40]

    # C0-b : cellules à deux juges, profils égaux et symétriques
    cellules = [e for e in data["estimateur_et_agregation"]
                if e["J"] == 2 and str(e["profil"]).startswith("egal_")]
    pire = None
    hors_borne = []
    hors_predit = 0
    for e in cellules:
        ee = {r: e["bras"][r]["erreur_equilibree"] for r in REGLES_P2}
        m = max(abs(ee[a] - ee[b]) for a, b in itertools.combinations(REGLES_P2, 2))
        cle = {"loi": e["loi"], "profil": e["profil"], "rho": e["rho_grille"], "n": e["n"]}
        if pire is None or m > pire[0]:
            pire = (m, cle, e.get("theorie_p2", {}).get("ecart_maximal"))
        if m > BORNE_P2:
            hors_borne.append({**cle, "ecart": m})
        if m > PREDIT_P2:
            hors_predit += 1
    profils = sorted({e["profil"] for e in cellules})
    lois = sorted({e["loi"] for e in cellules})
    sortie = {
        "C0_a_melange_plante": {"cellules": melange, "conforme": ok_melange},
        "C0_b_P2": {
            "cellules_lues": len(cellules),
            "profils": profils,
            "lois": lois,
            "regles": REGLES_P2,
            "ecart_maximal_observe": pire[0],
            "cellule_de_l_ecart_maximal": pire[1],
            "ecart_maximal_rapporte_par_le_banc_dans_cette_cellule": pire[2],
            "cellules_hors_de_0_02": hors_borne,
            "cellules_hors_de_0_01_prediction": hors_predit,
            "P2_tenue": len(hors_borne) == 0,
        },
    }
    with open(dst, "w", encoding="utf-8") as f:
        json.dump(sortie, f, ensure_ascii=False, indent=1)
        f.write("\n")


if __name__ == "__main__":
    main()
