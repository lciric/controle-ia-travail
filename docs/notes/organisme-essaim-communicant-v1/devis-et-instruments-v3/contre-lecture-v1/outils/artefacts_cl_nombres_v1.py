"""Artefacts neufs du contre-lecteur contre le contrôle des nombres v3 (textes en mémoire, rien d'écrit sur la pièce).
Chaque artefact change la valeur EFFECTIVE (exécutée par Python) d'une constante contrôlée ; attendu : refus.
Usage : python -B artefacts_cl_nombres_v1.py DOSSIER_V3"""
import sys, re
sys.path.insert(0, sys.argv[1])
import calcul_devis_essaim_v3 as C
CLES = ("BORNE_TEST", "VERIF", "PLANTEES", "PRIX_MULTI", "TOUR_CENTRAL", "TOUR_PIRE")
sain, _ = C.lire("devis_multi_v2")
aff, _ = C.lire("devis_affinage_v5")
ancre = "PLANTEES_PIRE, PLANTEES_CENTRAL, FAUSSES_ET_COPIES = 13, 10, 8"
assert sain.count(ancre) == 1
def effectif(texte, nom):
    ns = {"__name__": "artefact"}
    try:
        exec(compile(texte.split("\ndef ")[0], "art", "exec"), ns)  # en-tête de module seulement
        return ns.get(nom)
    except Exception as ex:
        return f"exception {type(ex).__name__}"
def essai(nom, texte, attendu, f=None, cle="BORNE_TEST"):
    f = f or (lambda t: C.comparer(C.nombres_tests(t), CLES))
    try:
        f(texte); rendu = "passe"
    except C.Refus:
        rendu = "refus"
    except Exception as ex:
        rendu = f"exception {type(ex).__name__}"
    ok = (rendu == "passe") == (attendu == "passe")
    print(f"{'TENUE' if ok else 'CASSEE'} | {nom} | attendu {attendu} | rendu {rendu}")
essai("N0 sain", sain, "passe")
essai("N1 BORNE_TEST redéfinie dans un bloc `if True:` de niveau module",
      sain.replace(ancre, ancre + '\nif True:\n    BORNE_TEST = {"opus": 9.99, "kimi": 9.99, "argon": 9.99}', 1), "refus")
essai("N2 affectation par indice : BORNE_TEST['kimi'] = 9.99",
      sain.replace(ancre, ancre + '\nBORNE_TEST["kimi"] = 9.99', 1), "refus")
essai("N3 appel de méthode : PRIX['kimi'] = (2.0, 12.0) via PRIX.update",
      sain.replace(ancre, ancre + '\nPRIX.update({"kimi": (2.0, 12.0)})', 1), "refus")
essai("N4 redéfinition dans un bloc try",
      sain.replace(ancre, ancre + '\ntry:\n    VERIF_PIRE = 0.50\nexcept Exception:\n    pass', 1), "refus")
essai("N5 expression d'affectation (morse) au niveau module",
      sain.replace(ancre, ancre + '\n(VERIF_PIRE := 0.50)', 1), "refus")
essai("N6 globals() écrit", sain.replace(ancre, ancre + '\nglobals()["VERIF_PIRE"] = 0.50', 1), "refus")
# affinage : une seconde mention de marge écrite avec une espace fine insécable (U+202F) avant « % »
m = re.search(r"marge de 10 %", aff); print("   (mentions de marge dans la pièce :", len(re.findall(r"marge de \d+\s?%", aff)), ")")
essai("N7 affinage : « marge de 15 % » ajoutée (espace fine insécable)", aff + "\nToute relance porte une marge de 15 % en plus.\n", "refus",
      lambda t: C.comparer(C.nombres_affinage(t), ("MARGE_AFFINAGE", "AIGUILLEUR_AFFINAGE")))
essai("N8 affinage : « marge de 15 pour cent » ajoutée", aff + "\nToute relance porte une marge de 15 pour cent en plus.\n", "refus",
      lambda t: C.comparer(C.nombres_affinage(t), ("MARGE_AFFINAGE", "AIGUILLEUR_AFFINAGE")))
