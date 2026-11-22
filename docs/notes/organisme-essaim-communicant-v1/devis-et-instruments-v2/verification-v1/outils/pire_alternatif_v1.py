"""Recalcule le « pire » du devis essaim sous les conventions des pièces que le devis dit importer, pour mesurer l'écart.
Lit calcul-devis-essaim-v1.json (chemin en argument) ; n'écrit que sur la sortie standard. Aucun appel.
Variantes :
  P0 = pire du devis (contrôle : doit redonner resume_usd.*.pire)
  P1 = borne par test du devis multi-générations v2 (BORNE_TEST + VERIF_PIRE) au lieu de l'arrondi au dixième
  P2 = P1 + fausses et copies testées (FAUSSES_ET_COPIES = 8 par génération, C.7 : « fausse refusée, copie au même verdict »)
  P3 = P2 + proposeurs et aiguilleur à leur plafond de session (3,00 ; 0,25) au lieu des jetons du régime
"""
import json, math, sys

d = json.load(open(sys.argv[1], encoding="utf-8"))
COURSES = d["unites"]["courses_par_ligne"]
prix = {k: (v["entree"], v["sortie"]) for k, v in d["tarifs_usd_par_million"].items()}
BORNE_V2 = {"claude-1": 1.50, "kimi": 0.80}  # devis_multi_generations_v2.py l. 20 (opus, kimi) ; argon v2 à 10/50 : écarté, autre tarif


def par_test_devis(p):
    return math.ceil(12 * (8000 * p[0] + 4000 * p[1]) / 1e6 * 10 - 1e-9) / 10 + 0.10


def calc(esp, regime, variante):
    p = prix[esp]
    je, js = d["unites"]["jetons_proposeur"][regime]
    tot = 0.0
    for l, rr in COURSES.items():
        n, na = rr[regime]
        n_p = n * 25
        n_c = 2 * n_p
        n_m = 12 * na
        plantees = 13 + (8 if variante in ("P2", "P3") else 0)
        t = n_c + n * 2 * 3 * plantees
        pt = par_test_devis(p)
        if variante != "P0" and esp in BORNE_V2:
            pt = BORNE_V2[esp] + 0.10
        if variante == "P3":
            fixe = n_p * 3.00 + n_c * 0.25 + n_m * (3000 * p[0] + 400 * p[1]) / 1e6
        else:
            fixe = (n_p * (je * p[0] + js * p[1]) + n_m * (3000 * p[0] + 400 * p[1]) + n_c * (2000 * p[0] + 300 * p[1])) / 1e6
        tot += fixe + t * pt
    return round(tot, 2)


print("espece regime | P0 (devis) | contrôle P0 = devis | P1 | P2 | P3")
for esp in ("kimi", "claude-1", "fable-5-2", "argon", "claude-2", "astra"):
    for r in ("bas", "attendu", "haut"):
        p0 = calc(esp, r, "P0")
        ref = d["resume_usd"][r][esp]["pire"]
        print(esp, r, "|", p0, "|", abs(p0 - ref) < 0.05, "|", calc(esp, r, "P1"), "|", calc(esp, r, "P2"), "|", calc(esp, r, "P3"))
