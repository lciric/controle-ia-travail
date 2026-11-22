#!/usr/bin/env python3
"""Devis en dollars de l'expérience « essaim qui communique » (conception : relecture de Fable, section D) — v1.

Aucun appel, aucun réseau, aucune dépense. Bibliothèque standard seule.
Chaque tarif est lu dans une pièce du dépôt, à son empreinte vérifiée (refus si l'empreinte diffère) ; un tarif dont la
pièce primaire est absente du disque est repris de la pièce secondaire qui le cite, et marqué comme tel.

Usage : python3 -I -B calcul_devis_essaim_v1.py SORTIE.json   (refuse d'écraser, R12)
"""
import hashlib
import json
import math
import os
import re
import sys

DEPOT = "/home/user/controle-ia-travail"

PIECES = {
    "conception": ("docs/notes/organisme-essaim-communicant-v1/reponse-fable-demande-7-v1/relecture-fable-api.md",
                   "dd60dd678b215326d16cd46e1fb180a522d3f82ec8ba15e9519edd9d42277a0c"),
    "fable_module": ("src/controle_ia/relecture_fable_api_v3.py",
                     "95bea064c753ca24e6a7619b99f1b03bd64700fac8568b3c598ec67bb985eb62"),
    "argon_enveloppe": ("rapports/fille-ideation-1-v1/appel-argon-v5.sh",
                        "37c0205e26f83cbdcdf5ad7f1e4094a21c7dcc70afb72d15ef0d260a770a132a"),
    "calcul_devis_v2": ("docs/notes/organisme-auto-conception-v1/calcul-devis-course-auto-conception-v2.json",
                        "91f5cf8f147689eb2fa9ff9db8b6e3b91b15496174e03f07a66d691676c2db2b"),
    "devis_affinage_v5": ("docs/notes/organisme-affinage-mentors-v1/devis-course-affinage-mentors-v5.md",
                          "521470096f98861d0a4183b24b1ab313af9fb365ee398da4b82afbfbbbfb3f30"),
    "devis_multi_v2": ("docs/notes/organisme-multi-generations-v1/outils-v2/devis_multi_generations_v2.py", None),
    "devis_v4_sortie": ("docs/notes/organisme-multi-generations-v1/sorties-v4/devis-v4.json",
                        "1fdfaa5118d9053b6b8f0f95772f589b9f025f674517c32aea1ec335b37ecc96"),
    "devis_auto_v1": ("docs/notes/organisme-auto-conception-v1/devis-course-auto-conception-v1.md",
                      "50e7d2f1dc713098edf5d69b6f46ded96a42423f6c50c528b02cf3781f96a80b"),
}
# Pièces primaires citées par les devis, vérifiées absentes du disque (R11) : leur tarif n'est repris que par citation.
ABSENTES = {
    "relais_reel_v2": "/home/user/ideation-organism/orchestrator/pole/relais_reel_v2.py (98c3e79e…, cité par devis_affinage_v5 § 1)",
    "prix_astra_v2": DEPOT + "/docs/notes/organisme-conception-propre-v1/prix-astra-v2.md (bf211a07…, cité par calcul_devis_v2)",
}


def lire(nom):
    rel, attendu = PIECES[nom]
    chemin = os.path.join(DEPOT, rel)
    octets = open(chemin, "rb").read()
    sha = hashlib.sha256(octets).hexdigest()
    if attendu is None:
        comp = open(chemin + ".sha256", encoding="utf-8").read().split()[0]
        attendu = comp
    if sha != attendu:
        raise SystemExit(f"refus : empreinte de {rel} = {sha}, attendue {attendu}")
    return octets.decode("utf-8"), sha


def tarifs():
    t = {}
    src = {}
    txt, sha = lire("fable_module")
    pe = float(re.search(r"^PRIX_ENTREE_USD_PAR_MJ = ([0-9.]+)$", txt, re.M).group(1))
    ps = float(re.search(r"^PRIX_SORTIE_USD_PAR_MJ = ([0-9.]+)$", txt, re.M).group(1))
    t["fable-5-2"] = (pe, ps)
    src["fable-5-2"] = {"piece": PIECES["fable_module"][0], "sha256": sha, "lignes": "99-100",
                        "statut": "tarif écrit dans le code, d'après la compétence de Claude Code ; facturé tel quel par la relecture (en-tête de la conception)"}
    txt, sha = lire("argon_enveloppe")
    m = re.search(r"--prix-entree ([0-9.]+) --prix-sortie ([0-9.]+)", txt)
    t["argon"] = (float(m.group(1)), float(m.group(2)))
    src["argon"] = {"piece": PIECES["argon_enveloppe"][0], "sha256": sha, "lignes": "29",
                    "statut": "prix figés de l'enveloppe ; sortie « SUPPOSÉ » selon devis_affinage_v5 § 1"}
    js, sha = lire("calcul_devis_v2")
    prix = json.loads(js)["prix"]
    for cle, nom in (("prop-claude-1", "claude-1"), ("prop-claude-2", "claude-2"), ("prop-kimi", "kimi"),
                     ("prop-astra", "astra"), ("prop-carbon", "carbon")):
        pe, ps = prix[cle]["usd_par_million"]
        t[nom] = (float(pe), float(ps))
        src[nom] = {"piece": PIECES["calcul_devis_v2"][0], "sha256": sha, "champ": f"prix.{cle}",
                    "source_citee": prix[cle]["source"],
                    "statut": "repris par citation ; pièce primaire non relue ici"}
    src["claude-1"]["primaire_absente"] = ABSENTES["relais_reel_v2"]
    src["claude-2"]["primaire_absente"] = ABSENTES["relais_reel_v2"]
    src["astra"]["primaire_absente"] = ABSENTES["prix_astra_v2"]
    src["carbon"]["statut"] = "borne haute donnée par la mère (R-3271), remise du lot non comptée"
    # contrôle croisé : l'enveloppe d'Argon et le calcul v2 doivent dire la même chose
    if tuple(prix["prop-argon"]["usd_par_million"]) != t["argon"]:
        raise SystemExit("refus : prix d'Argon divergents entre l'enveloppe et le calcul v2")
    return t, src


# ---- unités de la conception (section D), recopiées ; vérifiées contre ses tableaux plus bas ----------------------------
REGIMES = ("bas", "attendu", "haut")
COURSES = {  # lignes du tableau « Nombre de courses de bras » : (courses de bras, courses porteuses de messages)
    "pilote_AA": {"bas": (24, 8), "attendu": (36, 12), "haut": (36, 12)},
    "confirmatoire": {"bas": (60, 20), "attendu": (96, 32), "haut": (192, 64)},
    "bras_instrument": {"bas": (8, 4), "attendu": (32, 16), "haut": (48, 24)},
    "familles_inedites": {"bas": (0, 0), "attendu": (36, 12), "haut": (60, 20)},
}
TOTAUX_FABLE = {"courses": {"bas": 92, "attendu": 200, "haut": 336},
                "appels_proposeur": {"bas": 2300, "attendu": 5000, "haut": 8400},
                "appels_aiguilleur": {"bas": 4600, "attendu": 10000, "haut": 16800},
                "appels_message": {"bas": 384, "attendu": 864, "haut": 1440}}
PROPOSEUR_PAR_COURSE = 25          # « environ 25 par course »
CARTES_PAR_APPEL = 2               # C.1 : deux cartes par appel exactement
MESSAGES_PAR_COURSE_A = 12
JETONS_PROPOSEUR = {"bas": (4000, 3000), "attendu": (9000, 6000), "haut": (20000, 16000)}
JETONS_MESSAGE = (3000, 400)       # [HYPOTHÈSE] de Fable
JETONS_AIGUILLEUR = (2000, 300)    # [HYPOTHÈSE] de Fable, « sans pièce »
GENERATIONS = 3

# ---- test de mort : forme du noyau à monde planté (devis multi-générations v2, formule importée par la v4) -------------
# un test = tours d'expérimentateur + un vérificateur d'Argon ; central 2 tours de 8 000 / 2 000 jetons + 0,06 USD ;
# pire 12 tours de 8 000 / 4 000 jetons + 0,10 USD. Plantées testées par génération : central 10, pire 13.
TEST_TOURS = {"central": (2, 8000, 2000, 0.06), "pire": (12, 8000, 4000, 0.10)}
PLANTEES_PAR_GENERATION = {"central": 10, "pire": 13}
LIGNEES_PAR_COURSE = 2  # (a) 1 archive, (b) 4 lignées, (c) 1 : 6 jeux pour 3 courses de bras (C.7 « chaque lignée de (b) »)
PLAFOND_SESSION = {"proposeur": 3.00, "aiguilleur": 0.25}  # devis auto-conception v1 § 4 et calcul (PLAFONDS_SESSION)


def cout(n, e, s, p):
    return n * (e * p[0] + s * p[1]) / 1e6


def taux_promus():
    js, sha = lire("devis_v4_sortie")
    reps = json.loads(js)["central_v4"]["representants_promus_simules"]
    # 4 proposeurs × 6 cartes = 24 cartes par génération dans la simulation v4
    return sum(reps) / (24 * len(reps)), reps, sha


def verifier_formule_tests():
    txt, sha = lire("devis_multi_v2")
    ok = ("BORNE_TEST = {\"opus\": 1.50" in txt and "VERIF_CENTRAL, VERIF_PIRE = 0.06, 0.10" in txt
          and "PLANTEES_PIRE, PLANTEES_CENTRAL, FAUSSES_ET_COPIES = 13, 10, 8" in txt
          and "(8000 * PRIX[m][0] + 2000 * PRIX[m][1])" in txt)
    if not ok:
        raise SystemExit("refus : la formule de test du devis multi-générations v2 n'est pas celle recopiée")
    return sha


def unites(regime):
    c = sum(COURSES[l][regime][0] for l in COURSES)
    m = sum(COURSES[l][regime][1] for l in COURSES) * MESSAGES_PAR_COURSE_A
    p = c * PROPOSEUR_PAR_COURSE
    return {"courses": c, "appels_proposeur": p, "appels_aiguilleur": p * CARTES_PAR_APPEL, "appels_message": m}


def devis_ligne(n_courses, n_courses_a, regime, prix, taux, mode):
    """mode « estimation » : jetons du régime, tests centraux ; « pire » : jetons du régime, tests au pire."""
    pe = JETONS_PROPOSEUR[regime]
    n_p = n_courses * PROPOSEUR_PAR_COURSE
    n_c = n_p * CARTES_PAR_APPEL
    n_m = n_courses_a * MESSAGES_PAR_COURSE_A
    cle = "central" if mode == "estimation" else "pire"
    tours, te, ts, verif = TEST_TOURS[cle]
    t_cartes = n_c * (taux if mode == "estimation" else 1.0)
    t_plantees = n_courses * LIGNEES_PAR_COURSE * GENERATIONS * PLANTEES_PAR_GENERATION[cle]
    par_test = tours * (te * prix[0] + ts * prix[1]) / 1e6 + verif
    if mode == "pire":
        par_test = math.ceil(tours * (te * prix[0] + ts * prix[1]) / 1e6 * 10 - 1e-9) / 10 + verif
    lignes = {
        "proposeurs": {"appels": n_p, "jetons_entree": n_p * pe[0], "jetons_sortie": n_p * pe[1], "usd": cout(n_p, pe[0], pe[1], prix)},
        "messages": {"appels": n_m, "jetons_entree": n_m * JETONS_MESSAGE[0], "jetons_sortie": n_m * JETONS_MESSAGE[1],
                     "usd": cout(n_m, *JETONS_MESSAGE, prix)},
        "aiguilleur": {"appels": n_c, "jetons_entree": n_c * JETONS_AIGUILLEUR[0], "jetons_sortie": n_c * JETONS_AIGUILLEUR[1],
                       "usd": cout(n_c, *JETONS_AIGUILLEUR, prix)},
        "juge_statistique": {"appels": 0, "usd": 0.0},
        "tests_de_mort_cartes": {"tests": round(t_cartes, 1), "usd_par_test": round(par_test, 4), "usd": t_cartes * par_test,
                                 "appels_par_test": tours + 1},
        "tests_de_mort_objets_de_controle": {"tests": t_plantees, "usd_par_test": round(par_test, 4), "usd": t_plantees * par_test,
                                             "appels_par_test": tours + 1},
    }
    for v in lignes.values():
        v["usd"] = round(v["usd"], 2)
    total = sum(v["usd"] for v in lignes.values())
    budget_egalise = total - lignes["tests_de_mort_objets_de_controle"]["usd"]
    perimetre_fable = lignes["proposeurs"]["usd"] + lignes["messages"]["usd"] + lignes["aiguilleur"]["usd"]
    return {"lignes": lignes, "total_usd": round(total, 2), "hors_objets_de_controle_usd": round(budget_egalise, 2),
            "perimetre_section_D_sans_tests_usd": round(perimetre_fable, 2)}


def borne_dure(regime):
    u = unites(regime)
    return round(u["appels_proposeur"] * PLAFOND_SESSION["proposeur"] + u["appels_aiguilleur"] * PLAFOND_SESSION["aiguilleur"], 2)


def egalisation(rho=5.0, regime="attendu"):
    """C.1 : (b) reçoit le budget de communication de (a) converti en appels de proposeur, chaîne aval comprise."""
    pe, ps = JETONS_PROPOSEUR[regime]
    eq = lambda e, s: e + rho * s
    com = MESSAGES_PAR_COURSE_A * eq(*JETONS_MESSAGE)
    prop = 24 * eq(pe, ps)
    appel_seul = eq(pe, ps)
    appel_chaine = appel_seul + CARTES_PAR_APPEL * eq(*JETONS_AIGUILLEUR)
    return {"rho": rho, "regime": regime, "communication_eq": com, "proposeurs_a_eq": prop,
            "part_communication_sur_proposeurs": round(com / prop, 4),
            "appels_en_plus_pour_b_sans_chaine": int(com // appel_seul),
            "appels_en_plus_pour_b_chaine_aval_comprise": int(com // appel_chaine),
            "reliquat_eq_chaine_comprise": com - int(com // appel_chaine) * appel_chaine,
            "dit_par_la_conception": "environ un dixième ; deux appels de plus (26 sur 24)"}


def main(argv):
    if len(argv) != 2 or os.path.exists(argv[1]):
        print("usage : calcul_devis_essaim_v1.py SORTIE.json (neuve)", file=sys.stderr)
        return 2
    lire("conception")
    lire("devis_affinage_v5")
    lire("devis_auto_v1")
    prix, sources = tarifs()
    taux, reps, sha_v4 = taux_promus()
    sha_multi = verifier_formule_tests()
    rhos = {k: round(v[1] / v[0], 4) for k, v in prix.items()}
    controle = {r: unites(r) for r in REGIMES}
    ecarts = [f"{k}|{r}: calcul {controle[r][k]} contre conception {TOTAUX_FABLE[k][r]}"
              for k in TOTAUX_FABLE for r in REGIMES if controle[r][k] != TOTAUX_FABLE[k][r]]
    jetons_fable = {r: {"entree_millions": controle[r]["appels_proposeur"] * JETONS_PROPOSEUR[r][0] / 1e6,
                        "sortie_millions": controle[r]["appels_proposeur"] * JETONS_PROPOSEUR[r][1] / 1e6} for r in REGIMES}
    par_espece = {}
    for esp, p in sorted(prix.items()):
        par_espece[esp] = {}
        for r in REGIMES:
            par_espece[esp][r] = {}
            for mode in ("estimation", "pire"):
                lignes = {l: devis_ligne(COURSES[l][r][0], COURSES[l][r][1], r, p, taux, mode) for l in COURSES}
                par_espece[esp][r][mode] = {"par_ligne": lignes,
                                            "total_usd": round(sum(v["total_usd"] for v in lignes.values()), 2),
                                            "hors_objets_de_controle_usd": round(sum(v["hors_objets_de_controle_usd"] for v in lignes.values()), 2),
                                            "perimetre_section_D_sans_tests_usd": round(sum(v["perimetre_section_D_sans_tests_usd"] for v in lignes.values()), 2),
                                            "tests_de_mort_usd": round(sum(v["lignes"]["tests_de_mort_cartes"]["usd"] + v["lignes"]["tests_de_mort_objets_de_controle"]["usd"] for v in lignes.values()), 2)}
    pire_espece = {r: max(par_espece, key=lambda e: par_espece[e][r]["pire"]["total_usd"]) for r in REGIMES}
    resume = {r: {esp: {"estimation": par_espece[esp][r]["estimation"]["total_usd"],
                        "estimation_hors_objets_de_controle": par_espece[esp][r]["estimation"]["hors_objets_de_controle_usd"],
                        "estimation_perimetre_D_sans_tests": par_espece[esp][r]["estimation"]["perimetre_section_D_sans_tests_usd"],
                        "estimation_tests_de_mort": par_espece[esp][r]["estimation"]["tests_de_mort_usd"],
                        "pire": par_espece[esp][r]["pire"]["total_usd"],
                        "pire_tests_de_mort": par_espece[esp][r]["pire"]["tests_de_mort_usd"]} for esp in par_espece} for r in REGIMES}
    instruments = {r: {esp: {l: par_espece[esp][r]["estimation"]["par_ligne"][l]["total_usd"]
                             for l in ("pilote_AA", "bras_instrument")} for esp in par_espece} for r in REGIMES}
    sortie = {
        "version": "calcul-devis-essaim-v1",
        "script_sha256": hashlib.sha256(open(os.path.abspath(__file__), "rb").read()).hexdigest(),
        "pieces": {k: {"chemin": v[0]} for k, v in PIECES.items()},
        "pieces_primaires_absentes": ABSENTES,
        "tarifs_usd_par_million": {k: {"entree": v[0], "sortie": v[1], **sources[k]} for k, v in prix.items()},
        "rapport_sortie_sur_entree_par_espece": rhos,
        "unites": {"courses_par_ligne": COURSES, "proposeur_par_course": PROPOSEUR_PAR_COURSE,
                   "jetons_proposeur": JETONS_PROPOSEUR, "jetons_message": JETONS_MESSAGE, "jetons_aiguilleur": JETONS_AIGUILLEUR,
                   "test_de_mort": TEST_TOURS, "plantees_par_generation": PLANTEES_PAR_GENERATION,
                   "lignees_par_course": LIGNEES_PAR_COURSE, "taux_promus_estimation": round(taux, 4),
                   "taux_promus_source": {"representants_promus_simules": reps, "sha256": sha_v4,
                                          "statut": "proposeurs synthétiques (simulation v4), non mesuré sur vrais modèles"},
                   "formule_tests_sha256": sha_multi},
        "controle_des_totaux_de_la_conception": {"recalcules": controle, "ecarts": ecarts, "jetons_proposeur": jetons_fable},
        "egalisation_C1": egalisation(),
        "devis_par_espece": par_espece,
        "resume_usd": resume,
        "instruments_payants_estimation_usd": instruments,
        "espece_la_plus_chere_au_pire": pire_espece,
        "borne_dure_plafonds_de_session_usd": {r: borne_dure(r) for r in REGIMES},
        "borne_dure_note": "proposeurs × 3,00 + aiguilleur × 0,25 ; messages et tests de mort sans plafond de session établi pour ce rôle : non bornés ici",
    }
    with open(argv[1], "x", encoding="utf-8") as f:
        json.dump(sortie, f, ensure_ascii=False, indent=1, sort_keys=True)
    print(json.dumps({"ecarts": ecarts, "egalisation": sortie["egalisation_C1"], "resume": resume,
                      "pire_espece": pire_espece, "borne_dure": sortie["borne_dure_plafonds_de_session_usd"]}, ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
