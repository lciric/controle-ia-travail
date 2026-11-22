#!/usr/bin/env python3
"""Épreuves (R5) du contrôle des nombres de `calcul_devis_essaim_v2.py` : texte sain de la pièce (doit passer), artefacts où
un nombre diffère (doivent refuser), bornes par test attendues. Aucun appel. Usage : python3 -I -B epreuves_devis_v2.py SORTIE.json"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import calcul_devis_essaim_v2 as C  # noqa: E402


def essai(nom, f, attendu_refus):
    try:
        f()
        refus = None
    except C.Refus as ex:
        refus = str(ex)
    return {"epreuve": nom, "attendu": "refus" if attendu_refus else "passe", "rendu": "refus" if refus else "passe",
            "motif": refus, "tenue": (refus is not None) == attendu_refus}


def main(argv):
    if len(argv) != 2 or os.path.exists(argv[1]):
        return 2
    sain, _ = C.lire("devis_multi_v2")
    cles = ("BORNE_TEST", "VERIF", "PLANTEES", "PRIX_MULTI", "TOUR_CENTRAL", "TOUR_PIRE")
    res = [essai("pièce saine", lambda: C.comparer(C.nombres_tests(sain), cles), False)]
    for nom, a, b in (("borne opus 1.50 → 1.40", '"opus": 1.50', '"opus": 1.40'),
                      ("vérificateur au pire 0.10 → 0.12", "VERIF_CENTRAL, VERIF_PIRE = 0.06, 0.10", "VERIF_CENTRAL, VERIF_PIRE = 0.06, 0.12"),
                      ("fausses et copies 8 → 6", "PLANTEES_PIRE, PLANTEES_CENTRAL, FAUSSES_ET_COPIES = 13, 10, 8", "PLANTEES_PIRE, PLANTEES_CENTRAL, FAUSSES_ET_COPIES = 13, 10, 6"),
                      ("tour central 2000 → 3000 jetons de sortie", "(8000 * PRIX[m][0] + 2000 * PRIX[m][1])", "(8000 * PRIX[m][0] + 3000 * PRIX[m][1])"),
                      ("tours au pire 12 → 10 (commentaire de la borne)", "# 12 × (8 000", "# 10 × (8 000")):
        if a not in sain:
            res.append({"epreuve": nom, "tenue": False, "motif": "motif absent de la pièce"})
            continue
        art = sain.replace(a, b, 1)
        res.append(essai("artefact : " + nom, lambda art=art: C.comparer(C.nombres_tests(art), cles), True))
    t1, _ = C.lire("calcul_devis_v1_py")
    res.append(essai("plafonds sains", lambda: C.comparer(C.nombres_plafonds(t1), ("PLAFONDS_SESSION",)), False))
    art = t1.replace('"aiguilleur": 0.25', '"aiguilleur": 0.30', 1)
    res.append(essai("artefact : plafond de l'aiguilleur 0.25 → 0.30", lambda: C.comparer(C.nombres_plafonds(art), ("PLAFONDS_SESSION",)), True))
    t4, _ = C.lire("monde_riche_v4")
    res.append(essai("dénominateur 4 × 6 sain", lambda: C.comparer(C.nombres_simulation_v4(t4), ("SIMULATION_V4",)), False))
    art = t4.replace("for _c in range(6):", "for _c in range(5):", 1)
    res.append(essai("artefact : 6 cartes → 5", lambda: C.comparer(C.nombres_simulation_v4(art), ("SIMULATION_V4",)), True))
    N = C.nombres_tests(sain)
    N.update(C.nombres_plafonds(t1))
    attendu = {"claude-1": 1.60, "kimi": 0.90, "claude-2": 3.50, "astra": 3.50, "fable-5-2": 2.80, "argon": 2.90, "carbon": 2.90}
    prix, _ = C.tarifs()
    rendu = {e: round(C.borne_test(prix[e], N)[0], 4) for e in attendu}
    res.append({"epreuve": "bornes au pire par test (pièce : 1,50 + 0,10 ; 0,80 + 0,10 ; 3,40 + 0,10 ; formule sinon)", "attendu": attendu,
                "rendu": rendu, "tenue": rendu == attendu})
    with open(argv[1], "x", encoding="utf-8") as f:
        json.dump(res, f, ensure_ascii=False, indent=1)
    for r in res:
        print(r["tenue"], r["epreuve"])
    return 0 if all(r["tenue"] for r in res) else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
