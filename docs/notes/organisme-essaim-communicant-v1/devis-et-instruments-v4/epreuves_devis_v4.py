#!/usr/bin/env python3
"""Épreuves du contrôle des nombres de `calcul_devis_essaim_v4.py` (v4 : plus les 8 artefacts N1 à N8 de la contre-lecture de la v3,
`devis-et-instruments-v3/contre-lecture-v1/outils/artefacts_cl_nombres_v1.py`, recopiés, et des artefacts neufs). Texte de la v3 : : les 9 artefacts du contre-lecteur de la v2 (R1 à R9,
recopiés de `verification-v1/outils/artefacts_relecteur_devis_v2.py`, textes en mémoire), son cas sain R0, puis les artefacts
de l'auteur (v2) et des artefacts neufs. Aucun appel. Usage : python3 -I -B epreuves_devis_v3.py SORTIE.json"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import calcul_devis_essaim_v4 as C  # noqa: E402

CLES = ("BORNE_TEST", "VERIF", "PLANTEES", "PRIX_MULTI", "TOUR_CENTRAL", "TOUR_PIRE")
RES = []


def essai(nom, texte, attendu, f=None):
    f = f or (lambda t: C.comparer(C.nombres_tests(t), CLES))
    try:
        f(texte)
        rendu, motif = "passe", None
    except C.Refus as ex:
        rendu, motif = "refus", str(ex)
    except Exception as ex:  # noqa: BLE001
        rendu, motif = f"exception {type(ex).__name__}", str(ex)
    RES.append({"epreuve": nom, "attendu": attendu, "rendu": rendu, "motif": motif, "tenue": rendu == attendu})


def main(argv):
    if len(argv) != 2 or os.path.exists(argv[1]):
        return 2
    sain, _ = C.lire("devis_multi_v2")
    aff, _ = C.lire("devis_affinage_v5")
    con, _ = C.lire("conception")
    t1, _ = C.lire("calcul_devis_v1_py")
    t4, _ = C.lire("monde_riche_v4")
    fa = lambda t: C.comparer(C.nombres_affinage(t), ("MARGE_AFFINAGE", "AIGUILLEUR_AFFINAGE", "MAJORATION_AFFINAGE"))
    fc = lambda t: C.comparer(C.nombres_conception(t), ("PLAFOND_C8",))
    # --- contre-lecteur, R0 à R9 ---
    essai("R0 sain", sain, "passe")
    essai("R1 prix de Kimi 10 → 12 en sortie", sain.replace('"kimi": (2.0, 10.0)', '"kimi": (2.0, 12.0)', 1), "refus")
    essai("R2 BORNE_TEST redéfinie plus bas (9,99)", sain.replace("PLANTEES_PIRE, PLANTEES_CENTRAL, FAUSSES_ET_COPIES = 13, 10, 8",
          "PLANTEES_PIRE, PLANTEES_CENTRAL, FAUSSES_ET_COPIES = 13, 10, 8\nBORNE_TEST = {\"opus\": 9.99, \"kimi\": 9.99, \"argon\": 9.99}", 1), "refus")
    essai("R3 0.80 écrit 0.8", sain.replace('"kimi": 0.80', '"kimi": 0.8', 1), "passe")
    essai("R4 VERIF scindé en deux affectations (0.06 ; 0.12)", sain.replace("VERIF_CENTRAL, VERIF_PIRE = 0.06, 0.10", "VERIF_CENTRAL = 0.06\nVERIF_PIRE = 0.12", 1), "refus")
    essai("R5 borne opus 1.50 → 1.12", sain.replace('"opus": 1.50', '"opus": 1.12', 1), "refus")
    essai("R6 marge d'affinage 10 % → 15 % (première mention)", aff.replace("marge de 10 %", "marge de 15 %", 1), "refus", fa)
    essai("R7 pièce d'affinage saine (majoration de 25 % lue et rapportée)", aff, "passe", fa)
    essai("R8 C.8 105 % → 110 %", con.replace("Plafond par bras et par monde à 105 % du budget", "Plafond par bras et par monde à 110 % du budget", 1), "refus", fc)
    essai("R9 ligne C.8 dupliquée : 105 % puis 150 %", con.replace("Plafond par bras et par monde à 105 % du budget",
          "Plafond par bras et par monde à 105 % du budget.\n- Plafond par bras et par monde à 150 % du budget", 1), "refus", fc)
    # --- artefacts de l'auteur (v2) ---
    for nom, a, b in (("vérificateur au pire 0.10 → 0.12", "VERIF_CENTRAL, VERIF_PIRE = 0.06, 0.10", "VERIF_CENTRAL, VERIF_PIRE = 0.06, 0.12"),
                      ("fausses et copies 8 → 6", "FAUSSES_ET_COPIES = 13, 10, 8", "FAUSSES_ET_COPIES = 13, 10, 6"),
                      ("tour central 2000 → 3000", "(8000 * PRIX[m][0] + 2000 * PRIX[m][1])", "(8000 * PRIX[m][0] + 3000 * PRIX[m][1])"),
                      ("tours au pire 12 → 10", "# 12 × (8 000", "# 10 × (8 000")):
        essai("auteur : " + nom, sain.replace(a, b, 1), "refus")
    # --- neufs ---
    essai("neuf : seconde mention des tours au pire ailleurs dans la pièce", sain + "\n# 14 × (8 000 × entrée + 4 000 × sortie)\n", "refus")
    essai("neuf : VERIF_PIRE augmenté plus bas (+=)", sain + "\nVERIF_PIRE += 0.5\n", "refus")
    essai("neuf : PRIX redéfini dans une boucle de niveau module", sain + "\nfor PRIX in [{}]:\n    pass\n", "refus")
    essai("neuf : seconde ligne aiguilleur dans la pièce d'affinage", aff + "\n| aiguilleur (une carte) | 1 000 ; 2 000 | 100 ; 200 | 0 ; 0 | — |\n", "refus", fa)
    essai("neuf : majoration mentionnée deux fois", aff + "\n- **Majoration de 40 %** ajoutée\n", "refus", fa)
    essai("neuf : mention voisine « par bras et par monde … 120 % »", con + "\n- plafond par bras et par monde relevé à 120 %\n", "refus", fc)
    essai("plafonds sains", t1, "passe", lambda t: C.comparer(C.nombres_plafonds(t), ("PLAFONDS_SESSION",)))
    essai("plafonds : PLAFONDS_SESSION redéfini plus bas", t1 + "\nPLAFONDS_SESSION = {\"proposeur\": 3.0, \"aiguilleur\": 9.0, \"juge\": 0.6}\n", "refus",
          lambda t: C.comparer(C.nombres_plafonds(t), ("PLAFONDS_SESSION",)))
    essai("simulation v4 saine", t4, "passe", lambda t: C.comparer(C.nombres_simulation_v4(t), ("SIMULATION_V4",)))
    essai("simulation v4 : 6 → 5 cartes", t4.replace("for _c in range(6):", "for _c in range(5):", 1), "refus",
          lambda t: C.comparer(C.nombres_simulation_v4(t), ("SIMULATION_V4",)))
    essai("simulation v4 : seconde définition de course", t4 + "\ndef course(*a):\n    return None\n", "refus",
          lambda t: C.comparer(C.nombres_simulation_v4(t), ("SIMULATION_V4",)))
    # --- v4 : artefacts N1 à N8 de la contre-lecture de la v3 (recopiés) et neufs ---
    ancre = "PLANTEES_PIRE, PLANTEES_CENTRAL, FAUSSES_ET_COPIES = 13, 10, 8"
    fa2 = lambda t: C.comparer(C.nombres_affinage(t), ("MARGE_AFFINAGE", "AIGUILLEUR_AFFINAGE"))
    for nom, ajout in (("N1 BORNE_TEST redéfinie dans un bloc if True:", '\nif True:\n    BORNE_TEST = {"opus": 9.99, "kimi": 9.99, "argon": 9.99}'),
                       ("N2 affectation par indice BORNE_TEST['kimi']", '\nBORNE_TEST["kimi"] = 9.99'),
                       ("N3 PRIX.update", '\nPRIX.update({"kimi": (2.0, 12.0)})'),
                       ("N4 redéfinition dans un bloc try", '\ntry:\n    VERIF_PIRE = 0.50\nexcept Exception:\n    pass'),
                       ("N5 expression d'affectation (morse)", '\n(VERIF_PIRE := 0.50)'),
                       ("N6 globals() écrit", '\nglobals()["VERIF_PIRE"] = 0.50'),
                       ("neuf : morse caché dans une affectation", '\n_X = (VERIF_PIRE := 0.50)'),
                       ("neuf : redéfinition par attribut de module", '\nimport sys as _s\n_s.modules[__name__].VERIF_PIRE = 0.5'),
                       ("neuf : redéfinition dans un with", '\nwith open("/dev/null") as _f:\n    VERIF_PIRE = 0.5'),
                       ("neuf : exec d'une chaîne", '\nexec("VERIF_PIRE = 0.5")')):
        essai(nom, sain.replace(ancre, ancre + ajout, 1), "refus")
    essai("N7 « marge de 15 % » avec espace fine insécable", aff + "\nToute relance porte une marge de 15\u202f% en plus.\n", "refus", fa2)
    essai("N8 « marge de 15 pour cent »", aff + "\nToute relance porte une marge de 15 pour cent en plus.\n", "refus", fa2)
    essai("neuf : « Marge : 15 % » (autre tournure, majuscule)", aff + "\nMarge : 15 % en plus.\n", "refus", fa2)
    essai("neuf : majoration « 40 pour cent » ajoutée", aff + "\nune majoration de 40 pour cent\n", "refus", fa)
    essai("neuf : C.8 « 150 pour cent » voisin", con + "\n- plafond par bras et par monde relevé à 150 pour cent\n", "refus", fc)
    essai("neuf : plafonds redéfinis dans un if", t1 + "\nif True:\n    PLAFONDS_SESSION = {\"proposeur\": 9.0}\n", "refus",
          lambda t: C.comparer(C.nombres_plafonds(t), ("PLAFONDS_SESSION",)))
    with open(argv[1], "x", encoding="utf-8") as f:
        json.dump(RES, f, ensure_ascii=False, indent=1)
    for r in RES:
        print("TENUE " if r["tenue"] else "CASSÉE", r["epreuve"], "|", r["rendu"])
    return 0 if all(r["tenue"] for r in RES) else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
