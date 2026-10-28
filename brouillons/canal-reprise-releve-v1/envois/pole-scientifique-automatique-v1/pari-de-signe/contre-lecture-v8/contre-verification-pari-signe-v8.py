"""Contre-vérification (R2) de la conception v8 du pari apparié borné et du code v7 version 25.
Processeur seul ; aucun fichier du dépôt modifié ; graines par numpy.random.SeedSequence (R9).
Lancement : REP=1000 /opt/venv-essaim-sim-v1/bin/python -I -B contre-verification-pari-signe-v8.py > …-sortie.json
"""
import copy
import io
import json
import math
import os
import random
import sys
import time
import unittest

sys.dont_write_bytecode = True
DOSSIER = ("/home/claude/canal-conv-audit-n04/brouillons/canal-reprise-releve-v1/envois/"
           "pole-scientifique-automatique-v1/orchestrateur-pole-v7")
sys.path.insert(0, DOSSIER)
import numpy as np  # noqa: E402
from pole import pari_apparie as pa, engagement_apparie as ea, monde_banque_scores as mbs  # noqa: E402
from pole.outils import empreinte_objet  # noqa: E402
from essais.test_v7_monde_banque_scores import banque_synthetique  # noqa: E402

REP = int(os.environ.get("REP", "1000"))
GRAINE = 2026102723
sortie = {"manifeste": {"python": sys.version, "numpy": np.__version__, "graine_racine": GRAINE, "REP": REP,
                        "dossier_code": DOSSIER}}
t0 = time.time()


def rng(section, indice):
    ss = np.random.SeedSequence(GRAINE, spawn_key=(section, indice))
    return random.Random(int(ss.generate_state(1, dtype=np.uint64)[0]))


# ---- U : les essais nommés passent-ils ? -------------------------------------------------------------------------
def section_U():
    noms = ["essais.test_v7_pari_apparie.CorrectionsV8", "essais.test_v7_engagement_apparie.Construction.test_cle_de_l_heritage",
            "essais.test_v7_engagement_apparie.Jugement.test_bout_en_bout", "essais.test_v7_pari_apparie", "essais.test_v7_engagement_apparie"]
    res = {}
    for n in noms:
        suite = unittest.defaultTestLoader.loadTestsFromName(n)
        r = unittest.TextTestRunner(stream=io.StringIO(), verbosity=0).run(suite)
        res[n] = {"lances": r.testsRun, "echecs": len(r.failures), "erreurs": len(r.errors)}
    return res


# ---- monde A′ : martingale ×1,5 / ×0,5 à pile ou face, 20 pas par partie ---------------------------------------------
def partie_A_prime(r, pas=20):
    """Trajectoire = logarithme cumulé de l'e-processus, unité par unité (convention de `Course.ajouter_trajectoire`)."""
    cumul, traj = 0.0, []
    for _ in range(pas):
        cumul += math.log(1.5) if r.random() < 0.5 else math.log(0.5)
        traj.append(cumul)
    return traj


def course_politique(r, generations, politique, fiches=4, alpha=0.05):
    """politique ∈ {"honnete", "saut_sans_declaration", "saut_declaration_mensongere", "abandon_avant_partie_mensonger",
    "saut_empreinte_absente"}. Rend (au moins une promotion, e finale max, erreur levée ?)."""
    c = pa.Course(alpha=alpha)
    noms = [f"f{i}" for i in range(fiches)]
    c.entrer("g1", noms, alpha)
    erreur = None
    for g in range(generations):
        declarations = {}
        for f in noms:
            if f in c.gelees or f in c.arretees or f in c.promues:
                continue
            traj = partie_A_prime(r)
            monte = traj[-1] >= 0.0
            emp = f"{f}-g{g}"
            if politique == "honnete" or monte:
                c.ajouter_trajectoire(f, traj, empreinte_unites=emp)
            elif politique == "saut_declaration_mensongere":
                declarations[f] = "monde indisponible"  # mensonge : la partie a été calculée et vue
            elif politique == "abandon_avant_partie_mensonger":
                c.abandonner(f, avant_partie=True, motif="hors sujet")  # mensonge : la partie a été vue
            elif politique in ("saut_sans_declaration", "saut_empreinte_absente"):
                pass
        try:
            c.lire(sans_partie=declarations)
        except ValueError as e:
            erreur = str(e)[:80]
            break
    return bool(c.promues), max(math.exp(c.log_e[f]) for f in noms), erreur


def section_B():
    res = {}
    for ip, pol in enumerate(("honnete", "saut_sans_declaration", "saut_declaration_mensongere", "abandon_avant_partie_mensonger")):
        for G in (10, 30):
            r = rng(2, 100 * ip + G)
            prom = e_tot = 0.0
            erreurs = 0
            for _ in range(REP):
                p, e, err = course_politique(r, G, pol)
                prom += p
                e_tot += e
                erreurs += err is not None
            res[f"{pol}_G{G}"] = {"P_au_moins_une_fausse_promotion": prom / REP, "E_e_max": e_tot / REP,
                                  "courses_refusees_par_lire": erreurs}
    return res


# ---- A : chemins restants, cas par cas -------------------------------------------------------------------------------
def section_A():
    res = {}
    # (1) empreinte absente : la même partie deux fois est acceptée
    c = pa.Course(0.05)
    c.entrer("g", ["a"], 0.04)
    c.ajouter_trajectoire("a", [math.log(2)])
    c.lire()
    try:
        c.ajouter_trajectoire("a", [math.log(2)])
        res["empreinte_absente_meme_partie_deux_fois"] = "acceptée (e = %.3g)" % math.exp(c.log_e["a"])
    except ValueError as e:
        res["empreinte_absente_meme_partie_deux_fois"] = "refusée : " + str(e)
    # (2) même partie, empreinte donnée la première fois et absente la seconde
    c = pa.Course(0.05)
    c.entrer("g", ["a"], 0.04)
    c.ajouter_trajectoire("a", [math.log(2)], empreinte_unites="u")
    c.lire()
    try:
        c.ajouter_trajectoire("a", [math.log(2)])
        res["empreinte_puis_absente"] = "acceptée"
    except ValueError as e:
        res["empreinte_puis_absente"] = "refusée"
    # (3) deux fiches (relance sous une autre identité) lisent la même empreinte : accepté
    c = pa.Course(0.05)
    c.entrer("g", ["a"], 0.02)
    c.ajouter_trajectoire("a", [math.log(2)], empreinte_unites="u")
    c.lire()
    c.entrer("g2", ["a-relancee"], 0.02)
    try:
        c.ajouter_trajectoire("a-relancee", [math.log(2)], empreinte_unites="u")
        res["relance_autre_identite_meme_unites"] = "acceptée"
    except ValueError as e:
        res["relance_autre_identite_meme_unites"] = "refusée"
    # (4) recouvrement partiel : sur-ensemble d'unités = empreinte différente = accepté (banque qui grandit)
    b = banque_synthetique(random.Random(43), unites_par_partie=(100, 0, 100))
    m1 = mbs.MondeBanqueScores(b, 17)
    e1 = ea.construire(m1, {"noir": {"coefficients": {"blanc": 1, "noir": -1}}}, tau=0.05)
    r1 = ea.evaluer(m1, e1)
    b2 = copy.deepcopy(b)
    ajout = [copy.deepcopy(ep) for ep in b["episodes"] if ep["partie"] == "epreuve" and ep["unite"].endswith("-0")]
    for ep in ajout:
        ep["unite"] = ep["unite"] + "bis"
        ep["id"] = ep["id"] + "bis"
    b2["episodes"].extend(ajout)
    m2 = mbs.MondeBanqueScores(b2, 17)
    e2 = ea.construire(m2, {"noir": {"coefficients": {"blanc": 1, "noir": -1}}}, tau=0.05)
    r2 = ea.evaluer(m2, e2)
    c = pa.Course(0.05)
    c.entrer("g", ["a"], 0.05)
    c.ajouter_trajectoire("a", [0.0], empreinte_unites=r1["empreinte_unites"])
    c.lire()
    try:
        c.ajouter_trajectoire("a", [0.0], empreinte_unites=r2["empreinte_unites"])
        etat = "acceptée"
    except ValueError:
        etat = "refusée"
    res["sur_ensemble_banque_grandie"] = {"unites_1": r1["unites_lues"], "unites_2": r2["unites_lues"],
                                          "empreintes_differentes": r1["empreinte_unites"] != r2["empreinte_unites"],
                                          "seconde_partie": etat, "meme_cle": e1["empreinte_cle"] == e2["empreinte_cle"]}
    # (5) le refus de lire ne change rien à l'état (puis déclaration acceptée)
    c = pa.Course(0.05)
    c.entrer("g", ["a", "b"], 0.04)
    c.ajouter_trajectoire("a", [math.log(3)])
    try:
        c.lire()
    except ValueError:
        pass
    res["refus_lire_etat_intact"] = {"generation": c.generation, "sans_partie": dict(c.sans_partie), "lectures": c.lectures}
    # (6) abandon « avant partie » après lire : toujours accepté (déclaration à la charge de l'orchestrateur)
    c = pa.Course(0.05)
    c.entrer("g", ["a"], 0.04)
    c.lire(sans_partie={"a": "x"})
    c.abandonner("a", avant_partie=True, motif="m")
    res["abandon_avant_partie_apres_lire"] = c.abandons["a"]
    # (7) second abandon d'une gelée sans partie : silencieux, sans trace
    n = len(c.abandons)
    c.abandonner("a", motif="autre motif")
    res["second_abandon_gelee_trace"] = (c.abandons["a"], len(c.abandons) == n)
    # (8) la clé : partie et Λ présents ; développement ≠ épreuve ; Λ changée ⇒ clé changée
    cle = e1["cle_heritage"]
    res["cle"] = {"champs": sorted(cle), "lambdas": cle["lambdas"], "partie": cle["partie"]}
    ed = ea.construire(m1, {"noir": {"coefficients": {"blanc": 1, "noir": -1}}}, tau=0.05, partie="developpement")
    res["cle_dev_differente"] = ed["empreinte_cle"] != e1["empreinte_cle"]
    sauve = pa.LAMBDAS
    pa.LAMBDAS = (0.1, 0.3)
    el = ea.construire(m1, {"noir": {"coefficients": {"blanc": 1, "noir": -1}}}, tau=0.05)
    pa.LAMBDAS = sauve
    res["cle_lambdas_differente"] = el["empreinte_cle"] != e1["empreinte_cle"]
    # (9) empreinte_unites : dépend de la banque, de la partie, des identifiants — et seulement d'eux
    res["empreinte_unites_recalcul"] = r1["empreinte_unites"] == empreinte_objet(
        {"banque": m1.empreinte, "partie": "epreuve", "unites": sorted(f"epr-{u}" for u in range(100))})
    # (10) E[max(1, e_20)] exact (binomial) : le 1,77 de la v8
    E = sum(math.comb(20, k) * 0.5 ** 20 * max(1.0, 1.5 ** k * 0.5 ** (20 - k)) for k in range(21))
    res["E_max_1_e20"] = E
    # (11) espérance de l'abandon « mensonger » à une génération : E[e·1(e≥1)] + P(e<1)
    res["E_abandon_mensonger_une_generation"] = E  # identique par construction
    return res


sortie["U"] = section_U()
sortie["A"] = section_A()
sortie["B"] = section_B()
sortie["manifeste"]["duree_s"] = round(time.time() - t0, 1)
print(json.dumps(sortie, ensure_ascii=False, indent=1, default=str))
