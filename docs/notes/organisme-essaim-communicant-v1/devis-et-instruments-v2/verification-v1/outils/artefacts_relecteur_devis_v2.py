"""Artefacts du relecteur contre le contrôle des nombres de calcul_devis_essaim_v2.py (aucun écrit sur la pièce : textes en
mémoire). Usage : artefacts_relecteur_devis_v2.py DOSSIER_COPIE_V2"""
import sys

sys.path.insert(0, sys.argv[1])
import calcul_devis_essaim_v2 as C  # noqa: E402

CLES = ("BORNE_TEST", "VERIF", "PLANTEES", "PRIX_MULTI", "TOUR_CENTRAL", "TOUR_PIRE")
sain, _ = C.lire("devis_multi_v2")


def essai(nom, texte, attendu, f=None):
    f = f or (lambda t: C.comparer(C.nombres_tests(t), CLES))
    try:
        f(texte)
        rendu = "passe"
    except C.Refus as ex:
        rendu = "refus"
    except Exception as ex:  # noqa: BLE001
        rendu = f"exception {type(ex).__name__}"
    print(f"{'TENUE' if (rendu == 'passe') == (attendu == 'passe') else 'CASSEE'} | {nom} | attendu {attendu} | rendu {rendu}")


essai("R0 sain", sain, "passe")
essai("R1 prix de Kimi 10 → 12 en sortie", sain.replace('"kimi": (2.0, 10.0)', '"kimi": (2.0, 12.0)', 1), "refus")
# R2 : redéfinition plus bas : Python garderait la seconde valeur, la lecture prend la première
red = sain.replace("PLANTEES_PIRE, PLANTEES_CENTRAL, FAUSSES_ET_COPIES = 13, 10, 8",
                   "PLANTEES_PIRE, PLANTEES_CENTRAL, FAUSSES_ET_COPIES = 13, 10, 8\nBORNE_TEST = {\"opus\": 9.99, \"kimi\": 9.99, \"argon\": 9.99}", 1)
essai("R2 BORNE_TEST redéfinie plus bas (valeur effective 9,99)", red, "refus")
# R3 : même nombre écrit autrement (doit passer : la valeur ne change pas)
essai("R3 0.80 écrit 0.8", sain.replace('"kimi": 0.80', '"kimi": 0.8', 1), "passe")
# R4 : vérificateur scindé en deux lignes
essai("R4 VERIF scindé en deux affectations (0.06 ; 0.12)",
      sain.replace("VERIF_CENTRAL, VERIF_PIRE = 0.06, 0.10", "VERIF_CENTRAL = 0.06\nVERIF_PIRE = 0.12", 1), "refus")
# R5 : tours au pire réels changés dans le code, commentaire laissé à 12
essai("R5 borne opus recalculée à 10 tours mais commentaire « 12 × » gardé (1.50 → 1.12)",
      sain.replace('"opus": 1.50', '"opus": 1.12', 1), "refus")
aff, _ = C.lire("devis_affinage_v5")
essai("R6 marge d'affinage 10 % → 15 %", aff.replace("marge de 10 %", "marge de 15 %", 1), "refus",
      lambda t: C.comparer(C.nombres_affinage(t), ("MARGE_AFFINAGE", "AIGUILLEUR_AFFINAGE")))
essai("R7 marge 10 % gardée dans le texte, majoration de 25 % ajoutée ailleurs (le pire doit-il la prendre ?)", aff, "passe",
      lambda t: C.comparer(C.nombres_affinage(t), ("MARGE_AFFINAGE", "AIGUILLEUR_AFFINAGE")))
con, _ = C.lire("conception")
essai("R8 C.8 105 % → 110 %", con.replace("Plafond par bras et par monde à 105 % du budget", "Plafond par bras et par monde à 110 % du budget", 1), "refus",
      lambda t: C.comparer(C.nombres_conception(t), ("PLAFOND_C8",)))
essai("R9 ligne C.8 dupliquée : « 105 % » puis « 150 % » plus bas",
      con.replace("Plafond par bras et par monde à 105 % du budget", "Plafond par bras et par monde à 105 % du budget.\n- Plafond par bras et par monde à 150 % du budget", 1), "refus",
      lambda t: C.comparer(C.nombres_conception(t), ("PLAFOND_C8",)))
