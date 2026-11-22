#!/usr/bin/env python3
"""Devis en dollars de l'expérience « essaim qui communique » — v2 (corrections D1 à D3 de la contre-lecture de la v1).

Aucun appel, aucun réseau, aucune dépense. Bibliothèque standard seule. La v1 (`../essaim-devis-instruments-v1/`) reste
intacte. Changements :
- D1 : les nombres du test de mort (bornes par test, vérificateur, plantées, fausses et copies, tours) sont LUS dans
  `devis_multi_generations_v2.py` par analyse syntaxique (`ast`) et UTILISÉS ; chacun est aussi comparé à la valeur
  recopiée attendue (`ATTENDUS`) : un nombre qui diffère fait refuser (épreuve sur artefact : `epreuves_devis_v2.py`).
- D2 : un vrai pire, rendu à côté de l'estimation : plafonds de session lus (proposeur 3,00 ; aiguilleur 0,25) ; messages
  bornés au plafond du proposeur (supposé, aucun plafond propre) ; tests des fausses et des copies (8 par génération) ;
  relances (marge de 10 % du devis d'affinage v5) ; objets de contrôle passés par l'aiguilleur ; surcroît d'entrée du bras
  (a) (supposé) ; dépassement de 105 % (section C.8).
- D3 : chaque nombre lu dans une pièce est rendu avec chemin, empreinte et ligne ; le dénominateur du taux de promues
  (4 proposeurs × 6 cartes) est lu dans `monde_riche_v4.course` ; les nombres sans pièce sont marqués « supposé ».

Usage : python3 -I -B calcul_devis_essaim_v2.py SORTIE.json   (refuse d'écraser, R12)
"""
import ast
import hashlib
import json
import math
import os
import re
import sys

DEPOT = "/home/user/controle-ia-travail"
MG = "docs/notes/organisme-multi-generations-v1"
PIECES = {
    "conception": ("docs/notes/organisme-essaim-communicant-v1/reponse-fable-demande-7-v1/relecture-fable-api.md",
                   "dd60dd678b215326d16cd46e1fb180a522d3f82ec8ba15e9519edd9d42277a0c"),
    "fable_module": ("src/controle_ia/relecture_fable_api_v3.py", "95bea064c753ca24e6a7619b99f1b03bd64700fac8568b3c598ec67bb985eb62"),
    "argon_enveloppe": ("rapports/fille-ideation-1-v1/appel-argon-v5.sh", "37c0205e26f83cbdcdf5ad7f1e4094a21c7dcc70afb72d15ef0d260a770a132a"),
    "calcul_devis_v2_json": ("docs/notes/organisme-auto-conception-v1/calcul-devis-course-auto-conception-v2.json",
                             "91f5cf8f147689eb2fa9ff9db8b6e3b91b15496174e03f07a66d691676c2db2b"),
    "calcul_devis_v1_py": ("docs/notes/organisme-auto-conception-v1/calcul-devis-course-auto-conception-v1.py",
                           "8bd1e48a42ef2592704415c204e25d94a0ff85e899f94c6f815ae08621d39cb7"),
    "devis_affinage_v5": ("docs/notes/organisme-affinage-mentors-v1/devis-course-affinage-mentors-v5.md",
                          "521470096f98861d0a4183b24b1ab313af9fb365ee398da4b82afbfbbbfb3f30"),
    "devis_multi_v2": (MG + "/outils-v2/devis_multi_generations_v2.py", "710954c7cf3fd144139625a1416d36530f54e2dfdd48adc0f3e34831168bef86"),
    "devis_v4_sortie": (MG + "/sorties-v4/devis-v4.json", "1fdfaa5118d9053b6b8f0f95772f589b9f025f674517c32aea1ec335b37ecc96"),
    "monde_riche_v4": (MG + "/outils-v4/monde_riche_v4.py", "4b1658477811fb87360dda44a65b0af96e87ae1d2ca4a32bdabbd3ce6cc19eb8"),
}
ABSENTES = {
    "relais_reel_v2": "/home/user/ideation-organism/orchestrator/pole/relais_reel_v2.py (98c3e79e…, cité par devis_affinage_v5 § 1)",
    "prix_astra_v2": DEPOT + "/docs/notes/organisme-conception-propre-v1/prix-astra-v2.md (bf211a07…, cité par calcul_devis_v2_json)",
}
# Valeurs recopiées des pièces à la main : le programme les compare aux nombres lus (et refuse s'ils diffèrent).
ATTENDUS = {
    "BORNE_TEST": {"opus": 1.50, "kimi": 0.80, "argon": 3.40},
    "VERIF": (0.06, 0.10),
    "PLANTEES": (13, 10, 8),
    "PRIX_MULTI": {"opus": (4.0, 20.0), "fable52": (8.0, 40.0), "argon": (10.0, 50.0), "astra": (10.0, 50.0), "kimi": (2.0, 10.0)},
    "TOUR_CENTRAL": (8000, 2000),
    "TOUR_PIRE": (12, 8000, 4000),
    "PLAFONDS_SESSION": {"proposeur": 3.0, "aiguilleur": 0.25, "juge": 0.6},
    "SIMULATION_V4": (4, 6),
    "MARGE_AFFINAGE": 0.10,
    "AIGUILLEUR_AFFINAGE": ((6250, 23000), (300, 2000)),
    "PLAFOND_C8": 1.05,
}


class Refus(Exception):
    pass


def lire(nom, texte_force=None):
    rel, attendu = PIECES[nom]
    if texte_force is not None:
        return texte_force, "artefact"
    octets = open(os.path.join(DEPOT, rel), "rb").read()
    sha = hashlib.sha256(octets).hexdigest()
    if sha != attendu:
        raise Refus(f"empreinte de {rel} = {sha}, attendue {attendu}")
    return octets.decode("utf-8"), sha


def ligne_de(texte, motif):
    for i, l in enumerate(texte.splitlines(), start=1):
        if motif in l:
            return i
    raise Refus(f"motif introuvable : {motif!r}")


def affectation(arbre, nom):
    for n in ast.walk(arbre):
        if isinstance(n, ast.Assign):
            for t in n.targets:
                if isinstance(t, ast.Name) and t.id == nom:
                    return ast.literal_eval(n.value), n.lineno
                if isinstance(t, ast.Tuple) and any(isinstance(e, ast.Name) and e.id == nom for e in t.elts):
                    return ast.literal_eval(n.value), n.lineno
    raise Refus(f"affectation introuvable : {nom}")


def nombres_tests(texte):
    """Nombres du test de mort lus dans `devis_multi_generations_v2.py` (texte), avec leurs lignes."""
    a = ast.parse(texte)
    borne, lb = affectation(a, "BORNE_TEST")
    verif, lv = affectation(a, "VERIF_CENTRAL")
    plantees, lp = affectation(a, "PLANTEES_PIRE")
    prix, lpx = affectation(a, "PRIX")
    lt = ligne_de(texte, "CENTRAL_TOUR = ")
    tour = re.search(r"\((\d+) \* PRIX\[m\]\[0\] \+ (\d+) \* PRIX\[m\]\[1\]\)", texte.splitlines()[lt - 1])
    lbc = texte.splitlines()[lb - 1]
    tp = re.search(r"# (\d+) × \((\d[\d ]*) × entrée \+ (\d[\d ]*) × sortie\)", lbc)
    return {"BORNE_TEST": (borne, lb), "VERIF": (tuple(verif), lv), "PLANTEES": (tuple(plantees), lp),
            "PRIX_MULTI": ({k: tuple(v) for k, v in prix.items()}, lpx),
            "TOUR_CENTRAL": ((int(tour.group(1)), int(tour.group(2))), lt),
            "TOUR_PIRE": ((int(tp.group(1)), int(tp.group(2).replace(" ", "")), int(tp.group(3).replace(" ", ""))), lb)}


def comparer(lus, cles):
    ecarts = [f"{k}: lu {lus[k][0]!r}, attendu {ATTENDUS[k]!r}" for k in cles if lus[k][0] != ATTENDUS[k]]
    if ecarts:
        raise Refus("nombres de la pièce différents des valeurs recopiées : " + " ; ".join(ecarts))


def nombres_plafonds(texte):
    a = ast.parse(texte)
    v, l = affectation(a, "PLAFONDS_SESSION")
    return {"PLAFONDS_SESSION": (v, l)}


def nombres_simulation_v4(texte):
    a = ast.parse(texte)
    for f in a.body:
        if isinstance(f, ast.FunctionDef) and f.name == "course":
            portees = []
            for n in ast.walk(f):
                if isinstance(n, ast.For) and isinstance(n.iter, ast.Call) and getattr(n.iter.func, "id", "") == "range" \
                        and isinstance(n.target, ast.Name) and n.target.id in ("_p", "_c"):
                    portees.append((n.target.id, n.iter.args[0].value, n.lineno))
            d = {t: (v, l) for t, v, l in portees}
            return {"SIMULATION_V4": ((d["_p"][0], d["_c"][0]), d["_p"][1])}
    raise Refus("fonction course introuvable")


def nombres_affinage(texte):
    l1 = ligne_de(texte, "marge de 10 %")
    l2 = ligne_de(texte, "| aiguilleur (une carte) |")
    m = re.search(r"\| aiguilleur \(une carte\) \| ([\d ]+) ; ([\d ]+) \| ([\d ]+) ; ([\d ]+) \|", texte.splitlines()[l2 - 1])
    e = tuple(int(x.replace(" ", "")) for x in (m.group(1), m.group(2)))
    s = tuple(int(x.replace(" ", "")) for x in (m.group(3), m.group(4)))
    return {"MARGE_AFFINAGE": (0.10, l1), "AIGUILLEUR_AFFINAGE": ((e, s), l2)}


def nombres_conception(texte):
    l = ligne_de(texte, "Plafond par bras et par monde à 105 % du budget")
    return {"PLAFOND_C8": (1.05, l)}


def tarifs():
    t, src = {}, {}
    txt, sha = lire("fable_module")
    t["fable-5-2"] = (float(re.search(r"^PRIX_ENTREE_USD_PAR_MJ = ([0-9.]+)$", txt, re.M).group(1)),
                      float(re.search(r"^PRIX_SORTIE_USD_PAR_MJ = ([0-9.]+)$", txt, re.M).group(1)))
    src["fable-5-2"] = {"piece": PIECES["fable_module"][0], "sha256": sha, "lignes": [ligne_de(txt, "PRIX_ENTREE_USD_PAR_MJ = "), ligne_de(txt, "PRIX_SORTIE_USD_PAR_MJ = ")]}
    txt, sha = lire("argon_enveloppe")
    m = re.search(r"--prix-entree ([0-9.]+) --prix-sortie ([0-9.]+)", txt)
    t["argon"] = (float(m.group(1)), float(m.group(2)))
    src["argon"] = {"piece": PIECES["argon_enveloppe"][0], "sha256": sha, "lignes": [ligne_de(txt, "--prix-entree")], "statut": "sortie « SUPPOSÉ » (devis d'affinage v5 § 1)"}
    js, sha = lire("calcul_devis_v2_json")
    prix = json.loads(js)["prix"]
    for cle, nom in (("prop-claude-1", "claude-1"), ("prop-claude-2", "claude-2"), ("prop-kimi", "kimi"), ("prop-astra", "astra"), ("prop-carbon", "carbon")):
        t[nom] = tuple(float(x) for x in prix[cle]["usd_par_million"])
        src[nom] = {"piece": PIECES["calcul_devis_v2_json"][0], "sha256": sha, "champ": f"prix.{cle}", "source_citee": prix[cle]["source"], "statut": "repris par citation"}
    for n in ("claude-1", "claude-2"):
        src[n]["primaire_absente"] = ABSENTES["relais_reel_v2"]
    src["astra"]["primaire_absente"] = ABSENTES["prix_astra_v2"]
    src["carbon"]["statut"] = "borne haute (R-3271), remise du lot non comptée"
    if tuple(prix["prop-argon"]["usd_par_million"]) != t["argon"]:
        raise Refus("prix d'Argon divergents entre l'enveloppe et le calcul v2")
    return t, src


# --- unités de la section D (recopiées de la conception ; cohérence vérifiée contre ses propres tableaux, provenance : la conception)
REGIMES = ("bas", "attendu", "haut")
COURSES = {"pilote_AA": {"bas": (24, 8), "attendu": (36, 12), "haut": (36, 12)},
           "confirmatoire": {"bas": (60, 20), "attendu": (96, 32), "haut": (192, 64)},
           "bras_instrument": {"bas": (8, 4), "attendu": (32, 16), "haut": (48, 24)},
           "familles_inedites": {"bas": (0, 0), "attendu": (36, 12), "haut": (60, 20)}}
TOTAUX_FABLE = {"courses": {"bas": 92, "attendu": 200, "haut": 336}, "appels_proposeur": {"bas": 2300, "attendu": 5000, "haut": 8400},
                "appels_aiguilleur": {"bas": 4600, "attendu": 10000, "haut": 16800}, "appels_message": {"bas": 384, "attendu": 864, "haut": 1440}}
PROPOSEUR_PAR_COURSE, CARTES_PAR_APPEL, MESSAGES_PAR_COURSE_A, GENERATIONS = 25, 2, 12, 3
APPELS_A_PAR_COURSE = 24
JETONS_PROPOSEUR = {"bas": (4000, 3000), "attendu": (9000, 6000), "haut": (20000, 16000)}
JETONS_MESSAGE, JETONS_AIGUILLEUR = (3000, 400), (2000, 300)
SURCROIT_ENTREE_A = 3 * 400 + 2000   # SUPPOSÉ : trois messages relus (400 jetons chacun) + tableau partagé (2 000)
LIGNEES_PAR_COURSE = 2               # C.7 : (a) 1, (b) 4, (c) 1 jeux pour 3 courses de bras


def cout(n, e, s, p):
    return n * (e * p[0] + s * p[1]) / 1e6


def borne_test(prix, N):
    """Borne au pire d'un test : celle de la pièce si une entrée de même tarif y a une borne ; sinon la formule de la
    pièce (12 × (8 000 × entrée + 4 000 × sortie), arrondie au dixième au-dessus). Plus le vérificateur au pire."""
    bornes, _ = N["BORNE_TEST"]
    prix_m, _ = N["PRIX_MULTI"]
    nt, te, ts = N["TOUR_PIRE"][0]
    for cle, b in sorted(bornes.items()):
        if tuple(prix_m.get(cle, ())) == tuple(prix):
            return b + N["VERIF"][0][1], f"BORNE_TEST[{cle}] de la pièce (même tarif)"
    return math.ceil(nt * (te * prix[0] + ts * prix[1]) / 1e6 * 10 - 1e-9) / 10 + N["VERIF"][0][1], "formule de la pièce (aucune borne écrite pour ce tarif)"


def devis_ligne(n_c, n_a, regime, prix, N, taux):
    pe = JETONS_PROPOSEUR[regime]
    n_p = n_c * PROPOSEUR_PAR_COURSE
    n_cartes = n_p * CARTES_PAR_APPEL
    n_m = n_a * MESSAGES_PAR_COURSE_A
    n_pa = n_a * APPELS_A_PAR_COURSE
    pl_pire, pl_central, fausses = N["PLANTEES"][0]
    jeux = n_c * LIGNEES_PAR_COURSE * GENERATIONS
    cap = N["PLAFONDS_SESSION"][0]
    tc_e, tc_s = N["TOUR_CENTRAL"][0]
    v_c, v_p = N["VERIF"][0]
    test_central = 2 * (tc_e * prix[0] + tc_s * prix[1]) / 1e6 + v_c
    test_pire, src_borne = borne_test(prix, N)
    marge = N["MARGE_AFFINAGE"][0]
    c8 = N["PLAFOND_C8"][0]
    est = {"proposeurs": cout(n_p, pe[0], pe[1], prix), "surcroit_entree_a": cout(n_pa, SURCROIT_ENTREE_A, 0, prix),
           "messages": cout(n_m, *JETONS_MESSAGE, prix), "aiguilleur_cartes": cout(n_cartes, *JETONS_AIGUILLEUR, prix),
           "aiguilleur_objets_de_controle": cout(jeux * (pl_pire + fausses), *JETONS_AIGUILLEUR, prix),
           "juge_statistique": 0.0, "tests_cartes": n_cartes * taux * test_central, "tests_objets_de_controle": jeux * pl_central * test_central,
           "tests_fausses_et_copies": 0.0}
    pire = {"proposeurs": n_p * cap["proposeur"], "surcroit_entree_a": 0.0, "messages": n_m * cap["proposeur"],
            "aiguilleur_cartes": n_cartes * cap["aiguilleur"], "aiguilleur_objets_de_controle": jeux * (pl_pire + fausses) * cap["aiguilleur"],
            "juge_statistique": 0.0, "tests_cartes": n_cartes * test_pire, "tests_objets_de_controle": jeux * pl_pire * test_pire,
            "tests_fausses_et_copies": jeux * fausses * test_pire}
    s_est, s_pire = sum(est.values()), sum(pire.values())
    return {"estimation_postes": {k: round(v, 2) for k, v in est.items()}, "pire_postes": {k: round(v, 2) for k, v in pire.items()},
            "estimation_sans_relances": round(s_est, 2), "estimation_usd": round(s_est * (1 + marge), 2),
            "pire_sans_marges": round(s_pire, 2), "pire_usd": round(s_pire * (1 + marge) * c8, 2),
            "usd_par_test": {"estimation": round(test_central, 4), "pire": round(test_pire, 4), "source_borne": src_borne}}


def main(argv):
    if len(argv) != 2 or os.path.exists(argv[1]):
        print("usage : calcul_devis_essaim_v2.py SORTIE.json (neuve)", file=sys.stderr)
        return 2
    try:
        provenance = {}
        txt, sha = lire("devis_multi_v2")
        N = nombres_tests(txt)
        comparer(N, ("BORNE_TEST", "VERIF", "PLANTEES", "PRIX_MULTI", "TOUR_CENTRAL", "TOUR_PIRE"))
        for k in ("BORNE_TEST", "VERIF", "PLANTEES", "PRIX_MULTI", "TOUR_CENTRAL", "TOUR_PIRE"):
            provenance[k] = {"piece": PIECES["devis_multi_v2"][0], "sha256": sha, "ligne": N[k][1], "valeur": N[k][0]}
        for nom, f, cles in (("calcul_devis_v1_py", nombres_plafonds, ("PLAFONDS_SESSION",)),
                             ("monde_riche_v4", nombres_simulation_v4, ("SIMULATION_V4",)),
                             ("devis_affinage_v5", nombres_affinage, ("MARGE_AFFINAGE", "AIGUILLEUR_AFFINAGE")),
                             ("conception", nombres_conception, ("PLAFOND_C8",))):
            t, s = lire(nom)
            lus = f(t)
            comparer(lus, cles)
            N.update(lus)
            for k in cles:
                provenance[k] = {"piece": PIECES[nom][0], "sha256": s, "ligne": lus[k][1], "valeur": lus[k][0]}
        prix, sources = tarifs()
        js, sha4 = lire("devis_v4_sortie")
        reps = json.loads(js)["central_v4"]["representants_promus_simules"]
        props, cartes = N["SIMULATION_V4"][0]
        taux = sum(reps) / (props * cartes * len(reps))
        provenance["taux_promues"] = {"numerateurs": {"piece": PIECES["devis_v4_sortie"][0], "sha256": sha4, "champ": "central_v4.representants_promus_simules", "valeur": reps},
                                      "denominateur": provenance["SIMULATION_V4"], "taux": round(taux, 4),
                                      "statut": "proposeurs synthétiques ; non mesuré sur vrais modèles"}
    except Refus as ex:
        print(f"refus : {ex}", file=sys.stderr)
        return 3
    controle = {}
    for r in REGIMES:
        c = sum(COURSES[l][r][0] for l in COURSES)
        controle[r] = {"courses": c, "appels_proposeur": c * PROPOSEUR_PAR_COURSE, "appels_aiguilleur": c * PROPOSEUR_PAR_COURSE * CARTES_PAR_APPEL,
                       "appels_message": sum(COURSES[l][r][1] for l in COURSES) * MESSAGES_PAR_COURSE_A}
    ecarts = [f"{k}|{r}" for k in TOTAUX_FABLE for r in REGIMES if controle[r][k] != TOTAUX_FABLE[k][r]]
    par_espece, resume = {}, {r: {} for r in REGIMES}
    for esp, p in sorted(prix.items()):
        par_espece[esp] = {}
        for r in REGIMES:
            lignes = {l: devis_ligne(COURSES[l][r][0], COURSES[l][r][1], r, p, N, taux) for l in COURSES}
            tot = lambda k: round(sum(v[k] for v in lignes.values()), 2)
            par_espece[esp][r] = {"par_ligne": lignes, "estimation_usd": tot("estimation_usd"), "pire_usd": tot("pire_usd"),
                                  "estimation_sans_relances": tot("estimation_sans_relances"), "pire_sans_marges": tot("pire_sans_marges")}
            resume[r][esp] = {"estimation": par_espece[esp][r]["estimation_usd"], "pire": par_espece[esp][r]["pire_usd"],
                              "instruments_estimation": round(lignes["pilote_AA"]["estimation_usd"] + lignes["bras_instrument"]["estimation_usd"], 2),
                              "instruments_pire": round(lignes["pilote_AA"]["pire_usd"] + lignes["bras_instrument"]["pire_usd"], 2)}
    sortie = {"version": "calcul-devis-essaim-v2", "script_sha256": hashlib.sha256(open(os.path.abspath(__file__), "rb").read()).hexdigest(),
              "provenance_des_nombres": provenance, "tarifs_usd_par_million": {k: {"entree": v[0], "sortie": v[1], **sources[k]} for k, v in prix.items()},
              "pieces_primaires_absentes": ABSENTES,
              "supposes": {"surcroit_entree_a_jetons": SURCROIT_ENTREE_A, "messages_au_pire": "plafond de session du proposeur (aucun plafond propre)",
                           "lignees_par_course": LIGNEES_PAR_COURSE, "relances_au_pire": "même marge de 10 % qu'à l'estimation",
                           "objets_de_controle_aiguilles_par_generation": "13 vraies plantées + 8 fausses et copies (bornes de la pièce), estimation comme pire"},
              "unites_section_D": {"courses": COURSES, "jetons_proposeur": JETONS_PROPOSEUR, "jetons_message": JETONS_MESSAGE, "jetons_aiguilleur": JETONS_AIGUILLEUR,
                                   "provenance": "recopiées de la conception ; recalcul cohérent avec ses tableaux (cohérence, non provenance)", "ecarts": ecarts},
              "devis_par_espece": par_espece, "resume_usd": resume}
    with open(argv[1], "x", encoding="utf-8") as f:
        json.dump(sortie, f, ensure_ascii=False, indent=1, sort_keys=True)
    print(json.dumps({"ecarts": ecarts, "taux": round(taux, 4), "resume": resume}, ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
