"""Contre-vérification de la conception v10 du pari apparié borné et du code v7, version 28 (contre-lecture R2).

Usage (rien n'est écrit dans le dépôt ; sortie JSON sur la sortie standard) :
    REP=200 /opt/venv-essaim-sim-v1/bin/python -I -B contre-verification-pari-signe-v10.py RACINE_ORCHESTRATEUR > sortie.json

Sections :
  A  les contrôles de la contre-lecture v9 (A1 à A7) rejoués contre la version 28, et de nouveaux (A8 à A10) — cas sains
     et artefacts (R5) ;
  G  la chaîne de K9-1 (copie renommée, tranche d'avance, fiche non lancée) rejouée par l'interface de la version 28 ;
  H  chaînes nouvelles par l'interface de la version 28, toutes gardes en place (Lignees, Course(journal=…), clés, plan
     scellé, `evaluer` qui journalise), sur une banque **à nul exact** (seuils scellés égaux par construction) :
     H1 évaluation privée (sans journal) puis « sans partie » ; H2 espionne de même génération (même contraste, autre
     étiquette `population`) et « sans partie » décidée après son issue ; H3 graine du monde comme étiquette d'ordre ;
  C  la formule `esperance_conditionnelle` de la démonstration contre une simulation ; « 0,5 ≈ 14 points de rappel ».
Graines : numpy.random.SeedSequence(ENTROPIE, spawn_key=(section, indice)) (R9), converties en entiers pour `random`.
"""

import copy
import hashlib
import importlib.util
import json
import math
import os
import platform
import random
import statistics
import sys
import time

import numpy as np

RACINE = os.path.abspath(sys.argv[1])
REP = int(os.environ.get("REP", "200"))
ENTROPIE = 2026102810
sys.path.insert(0, RACINE)

from pole import engagement_apparie as ea  # noqa: E402
from pole import monde_banque_scores as mbs  # noqa: E402
from pole import pari_apparie as pa  # noqa: E402
from pole.outils import graine_derivee  # noqa: E402

_spec = importlib.util.spec_from_file_location("demo_pari_apparie_v7",
                                               os.path.join(RACINE, "demonstrations", "demo_pari_apparie_v7.py"))
demo = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(demo)

SECTIONS = {"A": 1, "G": 2, "H": 3, "H3": 4, "C": 5}


def graine(section, *i):
    s = np.random.SeedSequence(ENTROPIE, spawn_key=(SECTIONS[section],) + tuple(i))
    return int(s.generate_state(1, dtype=np.uint64)[0])


def sha(chemin):
    with open(chemin, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


def essai(f):
    try:
        return {"issue": "acceptée", "valeur": f()}
    except Exception as e:  # noqa: BLE001
        return {"issue": "refusée", "erreur": f"{type(e).__name__}: {str(e)[:170]}"}


def ajouter(c, fiche, r):
    return c.ajouter_trajectoire(fiche, r["trajectoire_log_min"], unites=r["identifiants_unites"],
                                 empreinte_cle=r["empreinte_cle"], empreinte_unites=r["empreinte_unites"])


# ---------------------------------------------------------------------------------------------------------------------
def section_A():
    s = {}
    rng = random.Random(graine("A", 1))
    b = demo.banque(rng, 2, 20, developpement=20)
    m = mbs.MondeBanqueScores(b, 5)
    t1, t2 = demo.unites_de_tranche(m, 1), demo.unites_de_tranche(m, 2)
    plan = {1: t1, 2: t2}
    coef = {"blanc": 1, "juge": -1}
    E_ep = ea.construire(m, {"c": {"coefficients": coef}}, 0.05, alpha_c=0.05, m_c=1, partie="epreuve", plan_tranches=plan)
    E_dev = ea.construire(m, {"c": {"coefficients": coef}}, 0.05, alpha_c=0.05, m_c=1, partie="developpement")
    E_tau = ea.construire(m, {"c": {"coefficients": coef}}, 0.10, alpha_c=0.05, m_c=1, partie="epreuve", plan_tranches=plan)

    # A1 : champs de la clé ; version de l'e-processus
    s["A1_champs_de_la_cle"] = sorted(E_ep["cle_heritage"])
    s["A1_e_processus"] = E_ep["cle_heritage"].get("e_processus")

    # A2 : une fiche, plusieurs clés
    lg = ea.Lignees()
    lg.entrer("f", E_dev)
    s["A2_lignees_meme_fiche_seconde_cle"] = essai(lambda: lg.entrer("f", E_ep))["issue"]
    c = pa.Course(alpha=0.05)
    c.entrer("g1", ["f"], 0.05, cles={"f": E_dev["empreinte_cle"]})
    r_dev = ea.evaluer(m, E_dev, generation=1, unites=m.unites("developpement"))
    r_ep1 = ea.evaluer(m, E_ep, generation=1)
    s["A2_course_avec_cles_partie_developpement"] = essai(lambda: ajouter(c, "f", r_dev))["issue"]
    c.lire()
    s["A2_course_avec_cles_partie_epreuve_meme_fiche"] = essai(lambda: ajouter(c, "f", r_ep1))
    c0 = pa.Course(alpha=0.05)  # sans `cles` : la garde de K9-2 n'existe pas
    c0.entrer("g1", ["f"], 0.05)
    ajouter(c0, "f", r_dev)
    c0.lire()
    s["A2_course_sans_cles_partie_epreuve_meme_fiche"] = essai(lambda: ajouter(c0, "f", r_ep1))["issue"]

    # A3 : copie renommée (refusée attendue) et variantes de même substance (clé différente ?)
    lg3 = ea.Lignees()
    lg3.entrer("fx", E_ep)
    renommee = ea.construire(m, {"autre_nom": {"coefficients": {"juge": -1, "blanc": 1}}}, 0.05, plan_tranches=plan)
    s["A3_copie_renommee_meme_cle"] = renommee["empreinte_cle"] == E_ep["empreinte_cle"]
    s["A3_copie_renommee_lignees"] = essai(lambda: lg3.entrer("fy", renommee))["issue"]
    c3 = pa.Course(alpha=0.05)
    c3.entrer("g1", ["fx"], 0.01, cles={"fx": E_ep["empreinte_cle"]})
    s["A3_copie_renommee_course_entrer"] = essai(lambda: c3.entrer("g1b", ["fy"], 0.01, cles={"fy": renommee["empreinte_cle"]}))["issue"]
    variantes = {
        "population_etiquette_libre": dict(population="vivier-espion"),
        "plan_autrement_decoupe": dict(plan_tranches={1: t1[:10], 2: t1[10:] + t2}),
        "plan_meme_tranches_generations_decalees": dict(plan_tranches={2: t1, 3: t2}),
        "coefficient_0_999999": dict(contrastes={"c": {"coefficients": {"blanc": 0.999999, "juge": -1}}}),
    }
    s["A3_variantes"] = {}
    for nom, kw in variantes.items():
        args = dict(plan_tranches=plan)
        args.update(kw)
        contr = args.pop("contrastes", {"c": {"coefficients": coef}})
        e_v = ea.construire(m, contr, 0.05, **args)
        lgv = ea.Lignees()
        lgv.entrer("fx", E_ep)
        s["A3_variantes"][nom] = {"cle_differente": e_v["empreinte_cle"] != E_ep["empreinte_cle"],
                                  "lignees_seconde_fiche": essai(lambda: lgv.entrer("fz", e_v))["issue"]}
    # même tranche, même génération, deux fiches « population » différente : les deux parties acceptées par la course
    e_pop = ea.construire(m, {"c": {"coefficients": coef}}, 0.05, plan_tranches=plan, population="vivier-espion")
    lgp = ea.Lignees()
    cp = pa.Course(alpha=0.05, journal=lgp)
    lgp.entrer("O", E_ep)
    lgp.entrer("S", e_pop)
    cp.entrer("g1", ["O", "S"], 0.05, cles={"O": E_ep["empreinte_cle"], "S": e_pop["empreinte_cle"]})
    rS = ea.evaluer(m, e_pop, generation=1, fiche="S", journal=lgp)
    rO = ea.evaluer(m, E_ep, generation=1, fiche="O", journal=lgp)
    s["A3_population_meme_tranche_deux_fiches"] = {"S": essai(lambda: ajouter(cp, "S", rS))["issue"],
                                                  "O": essai(lambda: ajouter(cp, "O", rO))["issue"],
                                                  "finales_egales": abs(rS["trajectoire_log_min"][-1] - rO["trajectoire_log_min"][-1]) < 1e-9,
                                                  "ordres_differents": rS["trajectoire_log_min"] != rO["trajectoire_log_min"]}

    # A3b : la course publiée v28 porte-t-elle une affirmation par deux fiches ? (proposeur reconstruit)
    rngp = random.Random(graine_derivee(graine_derivee(20261028, "course"), "proposeur"))
    chemin_course = os.path.join(os.path.dirname(RACINE), "pari-de-signe", "demonstration-v28", "course.json")
    with open(chemin_course, encoding="utf-8") as f:
        publie = json.load(f)
    entrees = {n for g in publie["journal"] for n in g["nouvelles"]}
    par_coef = {}
    for g in range(1, 5):
        for nom, fiche in demo.propositions(rngp, g, 6).items():
            if nom in entrees:
                cle = json.dumps(sorted(fiche["coefficients"].items())) + json.dumps(fiche.get("strate"))
                par_coef.setdefault(cle, []).append(nom)
    s["A3b_fiches_entrees"] = len(entrees)
    s["A3b_affirmations_portees_par_plusieurs_fiches"] = {k: v for k, v in par_coef.items() if len(v) > 1}

    # A4 : banque grandie d'une unité ; identité stable, absente, ou ré-étiquetée
    rng4 = random.Random(graine("A", 4))
    b1 = demo.banque(rng4, 1, 40)
    extra = [dict(e, id=e["id"].replace("epr-1-0-", "epr-1-extra-"), unite="epr-1-extra")
             for e in b1["episodes"] if e["unite"] == "epr-1-0"]

    def grandie(identite):
        b2 = copy.deepcopy(b1)
        b2["episodes"] += copy.deepcopy(extra)
        if identite is None:
            b2.pop("identite", None)
        else:
            b2["identite"] = identite
        return b2

    m1 = mbs.MondeBanqueScores(b1, 9)
    e1 = ea.construire(m1, {"c": {"coefficients": coef}}, 0.05)
    r1 = ea.evaluer(m1, e1, generation=1, unites=m1.unites("epreuve"))
    s["A4"] = {}
    for nom, ident in (("meme_identite", b1["identite"]), ("identite_reetiquetee", b1["identite"] + "-bis")):
        m2 = mbs.MondeBanqueScores(grandie(ident), 9)
        e2 = ea.construire(m2, {"c": {"coefficients": coef}}, 0.05)
        r2 = ea.evaluer(m2, e2, generation=2, unites=m2.unites("epreuve"))
        c4 = pa.Course(alpha=0.05)
        c4.entrer("g1", ["f", "f2"], 0.05, cles={"f": e1["empreinte_cle"]})
        ajouter(c4, "f", r1)
        c4.lire(sans_partie={"f2": "non lancée"})
        s["A4"][nom] = {"identifiants_communs": len(set(r1["identifiants_unites"]) & set(r2["identifiants_unites"])),
                        "cle_identique": e1["empreinte_cle"] == e2["empreinte_cle"],
                        "seconde_partie_meme_fiche": essai(lambda: ajouter(c4, "f", r2))["issue"],
                        "partie_par_une_fiche_neuve": essai(lambda: ajouter(c4, "f2", r2))["issue"]}
    b1s = copy.deepcopy(b1)
    b1s.pop("identite")
    m1s = mbs.MondeBanqueScores(b1s, 9)
    m2s = mbs.MondeBanqueScores(grandie(None), 9)
    r1s = ea.evaluer(m1s, ea.construire(m1s, {"c": {"coefficients": coef}}, 0.05), generation=1, unites=m1s.unites("epreuve"))
    r2s = ea.evaluer(m2s, ea.construire(m2s, {"c": {"coefficients": coef}}, 0.05), generation=2, unites=m2s.unites("epreuve"))
    s["A4"]["sans_identite_declaree_identifiants_communs"] = len(set(r1s["identifiants_unites"]) & set(r2s["identifiants_unites"]))

    # A5 : journal — évaluation privée, seconde évaluation, génération du journal, journal modifiable
    lg5 = ea.Lignees()
    c5 = pa.Course(alpha=0.05, journal=lg5)
    lg5.entrer("f", E_ep)
    c5.entrer("g1", ["f"], 0.05, cles={"f": E_ep["empreinte_cle"]})
    prive = ea.evaluer(m, E_ep, generation=1)  # partie calculée, sans journal : l'interface l'accepte
    s["A5a_evaluation_privee_sans_journal"] = "acceptée" if prive["unites"] > 0 else "?"
    s["A5a_puis_sans_partie_course_avec_journal"] = essai(lambda: sorted(c5.lire(sans_partie={"f": "monde indisponible"})))["issue"]
    lg5b = ea.Lignees()
    ea.evaluer(m, E_ep, generation=1, fiche="f", journal=lg5b)
    s["A5b_seconde_evaluation_journalisee"] = essai(lambda: ea.evaluer(m, E_ep, generation=1, fiche="f", journal=lg5b))["issue"]
    # A5c : la génération du journal est celle que l'appelant passe : lire la tranche 2 pendant la génération 1
    lg5c = ea.Lignees()
    c5c = pa.Course(alpha=0.05, journal=lg5c)
    lg5c.entrer("f", E_ep)
    c5c.entrer("g1", ["f"], 0.05, cles={"f": E_ep["empreinte_cle"]})
    r_g1 = ea.evaluer(m, E_ep, generation=1, fiche="f", journal=lg5c)
    avance = ea.evaluer(m, E_ep, generation=2, fiche="f", journal=lg5c)  # tranche 2 lue pendant la génération 1
    ajouter(c5c, "f", r_g1)
    s["A5c_tranche_2_journalisee_pendant_la_generation_1"] = essai(lambda: sorted(c5c.lire()))["issue"]
    s["A5c_puis_ajoutee_en_generation_2"] = essai(lambda: ajouter(c5c, "f", avance))["issue"]
    # A5d : le journal est une liste que l'appelant peut réécrire (ce que fait la démonstration, l. 201)
    lg5d = ea.Lignees()
    c5d = pa.Course(alpha=0.05, journal=lg5d)
    lg5d.entrer("f", E_ep)
    c5d.entrer("g1", ["f"], 0.05, cles={"f": E_ep["empreinte_cle"]})
    ea.evaluer(m, E_ep, generation=1, fiche="f", journal=lg5d)
    lg5d.journal[:] = []
    s["A5d_entree_effacee_puis_sans_partie"] = essai(lambda: sorted(c5d.lire(sans_partie={"f": "x"})))["issue"]

    # A6 : déclarations « sans partie » indues ; trace de la redite
    c6 = pa.Course(alpha=0.05)
    c6.entrer("g1", ["a", "b"], 0.04)
    c6.abandonner("a", avant_partie=True, motif="m1")
    c6.abandonner("a", motif="m2")
    s["A6_redite_tracee"] = c6.abandons.get(("redite", "a"))
    c6.ajouter_trajectoire("b", [0.1], unites={("x", "b", 1)})
    s["A6_sans_partie_pour_gelee"] = essai(lambda: c6.lire(sans_partie={"a": "gelée"}))["issue"]
    s["A6_sans_partie_pour_fiche_avec_partie"] = essai(lambda: c6.lire(sans_partie={"b": "x"}))["issue"]

    # A7 : étiquette d'ordre, tranche libre, graine du monde
    s["A7_etiquette_ordre_libre"] = essai(lambda: ea.evaluer(m, E_ep, generation=1, etiquette_ordre="a"))["issue"]
    s["A7_unites_libres_avec_plan"] = essai(lambda: ea.evaluer(m, E_ep, generation=1, unites=t1[:5]))["issue"]
    E_sans_plan = ea.construire(m, {"c": {"coefficients": coef}}, 0.05)
    s["A7_tranche_libre_sans_plan_sous_ensemble_quelconque"] = essai(lambda: ea.evaluer(m, E_sans_plan, generation=1, unites=t1[::3])["unites"])["issue"]
    m_autre = mbs.MondeBanqueScores(b, 6)  # même banque, autre graine du monde
    ta = ea.evaluer(m, E_ep, generation=1)["trajectoire_log_min"]
    tb_ = essai(lambda: ea.evaluer(m_autre, E_ep, generation=1)["trajectoire_log_min"])
    s["A7_meme_engagement_monde_d_autre_graine"] = tb_["issue"]
    if tb_["issue"] == "acceptée":
        s["A7_trajectoires_differentes"] = ta != tb_["valeur"]
        s["A7_finale_identique"] = abs(ta[-1] - tb_["valeur"][-1]) < 1e-9
    s["A7_graine_du_monde_dans_l_engagement"] = any("graine" in k for k in E_ep) or any("graine" in k for k in E_ep["cle_heritage"])

    # A8 : abandon « avant partie » contredit par le journal (même fiche, ou autres fiches de la même tranche)
    lg8 = ea.Lignees()
    c8 = pa.Course(alpha=0.05, journal=lg8)
    lg8.entrer("f", E_ep)
    lg8.entrer("h", E_tau)
    c8.entrer("g1", ["f", "h"], 0.05, cles={"f": E_ep["empreinte_cle"], "h": E_tau["empreinte_cle"]})
    ea.evaluer(m, E_ep, generation=1, fiche="f", journal=lg8)
    s["A8_avant_partie_alors_que_sa_partie_est_au_journal"] = essai(lambda: c8.abandonner("f", avant_partie=True, motif="x"))["issue"]
    rh = ea.evaluer(m, E_tau, generation=1, fiche="h", journal=lg8)
    ajouter(c8, "h", rh)
    s["A8_lire_apres_cet_abandon"] = essai(lambda: sorted(c8.lire()))["issue"]

    # A9 : course sans journal — les gardes de K9-6 n'existent pas, sans avertissement
    c9 = pa.Course(alpha=0.05)
    c9.entrer("g1", ["f"], 0.05)
    s["A9_course_sans_journal_sans_partie_apres_calcul"] = essai(lambda: (ea.evaluer(m, E_ep, generation=1), sorted(c9.lire(sans_partie={"f": "x"})))[1])["issue"]
    s["A9_course_sans_journal_attribut"] = c9.journal is None

    # A10 : partie vide (fiche stratifiée sans unité dans la tranche) : ce que le journal en garde
    lg10 = ea.Lignees()
    e_conc = ea.construire(m, {"c": {"coefficients": coef}}, 0.05, strate={"mode": "concentre"}, plan_tranches=plan)
    r_vide = ea.evaluer(m, e_conc, generation=1, fiche="k", journal=lg10)
    c10 = pa.Course(alpha=0.05, journal=lg10)
    c10.entrer("g1", ["k"], 0.05)
    s["A10_partie_vide_unites"] = r_vide["unites"]
    s["A10_partie_vide_ajout"] = essai(lambda: ajouter(c10, "k", r_vide))["issue"]
    s["A10_partie_vide_sans_partie_journal_intact"] = essai(lambda: sorted(c10.lire(sans_partie={"k": "vide"})))["issue"]
    return s


# ---------------------------------------------------------------------------------------------------------------------
def section_G(rep):
    """La chaîne de K9-1 (contre-lecture v9, script `-chaine`) rejouée contre la version 28, parties synthétiques et
    Course du code : (1) la copie renommée — refusée par la clé canonique (A3) ; on la garde ici sous une clé distincte
    (étiquette `population`, A3) pour isoler l'étape (2) ; (2) la copie lit la tranche g + 1 en génération g ; (3) la fiche
    lit la tranche g + 1 en génération g + 1 si la copie l'a trouvée favorable, sinon « non lancée »."""
    refus, promue, au_moins_une, essais_lecture = 0, 0, 0, 0
    message = None
    for r in range(rep):
        rng = random.Random(graine("G", r))
        lg = ea.Lignees()
        c = pa.Course(alpha=0.05, journal=lg)
        c.entrer("g1", ["fiche", "copie"], 0.05, cles={"fiche": "cle-fiche", "copie": "cle-copie"})
        tranches = {}

        def tranche(t):
            if t not in tranches:
                tranches[t] = [rng.choice((-0.5, 0.5)) for _ in range(20)]
            return tranches[t]

        def ids(t):
            return [("banque", "epreuve", f"t{t}-{u}") for u in range(20)]

        def partie(g, f, t, cle):
            res = {"trajectoire_log_min": pa.trajectoire_log_richesse(tranche(t)), "identifiants_unites": ids(t),
                   "empreinte_cle": cle, "empreinte_unites": f"t{t}"}
            lg.journaliser(g, f, res)
            return res

        for g in range(1, 11):
            sans_partie = {}
            actives = [f for f in ("fiche", "copie") if f not in c.promues and f not in c.arretees and f not in c.gelees]
            if "copie" in actives:
                ajouter(c, "copie", partie(g, "copie", g + 1, "cle-copie"))
            if "fiche" in actives:
                if g == 1:
                    ajouter(c, "fiche", partie(g, "fiche", 1, "cle-fiche"))
                elif pa.trajectoire_log_richesse(tranche(g))[-1] > 0:
                    essais_lecture += 1
                    res = partie(g, "fiche", g, "cle-fiche")
                    try:
                        ajouter(c, "fiche", res)
                    except ValueError as e:
                        refus += 1
                        message = message or str(e)[:200]
                        lg.journal[:] = [j for j in lg.journal if not (j["generation"] == g and j["fiche"] == "fiche")]
                        sans_partie["fiche"] = "refusée par la course"
                else:
                    sans_partie["fiche"] = "fiche non lancée"
            c.lire(sans_partie=sans_partie)
        promue += "fiche" in c.promues
        au_moins_une += bool(c.promues)
    return {"repetitions": rep, "generations": 10, "lectures_tentees_par_la_fiche": essais_lecture,
            "refusees_par_la_course": refus, "message": message, "fiche_promue": promue / rep,
            "au_moins_une_promotion": au_moins_une / rep,
            "note": "pour exécuter l'étape (3) il faut effacer l'entrée refusée du journal (A5d) et déclarer « sans partie »"}


# ---------------------------------------------------------------------------------------------------------------------
def banque_nul_exact(rng, tranches, unites_par_tranche, calibrage=60, sabotes=8, honnetes=8, sigma=0.6, decalage=1.5,
                     identite="nul-exact"):
    """Deux cellules a et b. Calibrage : honnêtes de scores **identiques** sur a et b (seuils scellés égaux). Épreuve :
    a et b tirés indépendamment de la même loi (η + décalage + ε chez les sabotés, η + ε chez les honnêtes, η d'unité).
    Le contraste a − b est alors d'espérance nulle **conditionnellement aux seuils scellés**, et de loi symétrique."""
    eps = []
    for u in range(calibrage):
        eta = rng.gauss(0, sigma)
        for k in range(honnetes):
            x = eta + rng.gauss(0, 1)
            eps.append({"id": f"cal-{u}-h-{k}", "unite": f"cal-{u}", "etiquette": "honnete", "partie": "calibrage",
                        "strates": {"tranche": "0"}, "scores": {"a": x, "b": x}})
    for t in range(1, tranches + 1):
        for u in range(unites_par_tranche):
            eta = rng.gauss(0, sigma)
            for et, n, d in (("sabote", sabotes, decalage), ("honnete", honnetes, 0.0)):
                for k in range(n):
                    eps.append({"id": f"e-{t}-{u}-{et}-{k}", "unite": f"e-{t}-{u}", "etiquette": et, "partie": "epreuve",
                                "strates": {"tranche": str(t)},
                                "scores": {"a": eta + d + rng.gauss(0, 1), "b": eta + d + rng.gauss(0, 1)}})
    return {"identite": identite, "cellules": ["a", "b"], "strates": ["tranche"], "episodes": eps}


def plan_de(monde, tranches):
    return {g: sorted({e["unite"] for e in monde.episodes("epreuve", None, {"tranche": str(g)})}) for g in range(1, tranches + 1)}


CONTRASTE_NUL = {"c": {"coefficients": {"a": 1, "b": -1}}}


def section_H(rep, generations):
    """H1 et H2 sur la même banque par répétition (comparaison appariée avec la course honnête)."""
    res = {k: 0 for k in ("H1_honnete_promue", "H1_chaine_promue", "H2_honnete_O_promue", "H2_honnete_au_moins_une",
                          "H2_chaine_O_promue", "H2_chaine_au_moins_une", "refus")}
    decl_h1, decl_h2 = 0, 0
    seuils_egaux = True
    messages = []
    for r in range(rep):
        b = banque_nul_exact(random.Random(graine("H", generations, r)), generations, 20)
        m = mbs.MondeBanqueScores(b, graine("H", generations, 10_000 + r))
        plan = plan_de(m, generations)
        eO = ea.construire(m, CONTRASTE_NUL, 0.05, alpha_c=0.05, m_c=1, plan_tranches=plan)
        seuils_egaux &= eO["cle_heritage"]["seuils"]["a"] == eO["cle_heritage"]["seuils"]["b"]
        eS = ea.construire(m, CONTRASTE_NUL, 0.05, alpha_c=0.05, m_c=2, plan_tranches=plan, population="vivier-espion")
        eO2 = ea.construire(m, CONTRASTE_NUL, 0.05, alpha_c=0.05, m_c=2, plan_tranches=plan)
        try:
            # H1 : fiche seule (seuil 20) ; honnête contre « évaluation privée, puis sans partie si défavorable »
            for mode in ("honnete", "chaine"):
                lg = ea.Lignees()
                c = pa.Course(alpha=0.05, journal=lg)
                lg.entrer("O", eO)
                c.entrer("g1", ["O"], 0.05, cles={"O": eO["empreinte_cle"]})
                for g in range(1, generations + 1):
                    if "O" in c.promues or "O" in c.arretees:
                        break
                    if mode == "chaine":
                        prive = ea.evaluer(m, eO, generation=g)  # sans journal : invisible pour la course
                        if prive["trajectoire_log_min"][-1] <= 0.0:
                            c.lire(sans_partie={"O": "monde indisponible"})
                            decl_h1 += 1
                            continue
                    ajouter(c, "O", ea.evaluer(m, eO, generation=g, fiche="O", journal=lg))
                    c.lire()
                res[f"H1_{mode}_promue"] += "O" in c.promues
            # H2 : famille {S, O} (seuil 40) ; S (même contraste, étiquette population) lit toujours, la première ;
            # O ne lit que si la partie de S est favorable, sinon « sans partie » (vraie : rien n'est calculé pour O)
            for mode in ("honnete", "chaine"):
                lg = ea.Lignees()
                c = pa.Course(alpha=0.05, journal=lg)
                lg.entrer("S", eS)
                lg.entrer("O", eO2)
                c.entrer("g1", ["S", "O"], 0.05, cles={"S": eS["empreinte_cle"], "O": eO2["empreinte_cle"]})
                for g in range(1, generations + 1):
                    actives = [f for f in ("S", "O") if f not in c.promues and f not in c.arretees]
                    if not actives:
                        break
                    sans_partie, favorable = {}, True
                    if "S" in actives:
                        rS = ea.evaluer(m, eS, generation=g, fiche="S", journal=lg)
                        ajouter(c, "S", rS)
                        favorable = rS["trajectoire_log_min"][-1] > 0.0
                    if "O" in actives:
                        if mode == "chaine" and not favorable:
                            sans_partie["O"] = "fiche non lancée"
                            decl_h2 += 1
                        else:
                            ajouter(c, "O", ea.evaluer(m, eO2, generation=g, fiche="O", journal=lg))
                    c.lire(sans_partie=sans_partie)
                res[f"H2_{mode}_O_promue"] += "O" in c.promues
                res[f"H2_{mode}_au_moins_une"] += bool(c.promues)
        except ValueError as e:
            res["refus"] += 1
            messages.append(str(e)[:160])
    out = {k: (v / rep if k != "refus" else v) for k, v in res.items()}
    out.update({"repetitions": rep, "generations": generations, "unites_par_tranche": 20,
                "declarations_sans_partie_par_course_H1": decl_h1 / rep, "declarations_sans_partie_par_course_H2": decl_h2 / rep,
                "seuils_scelles_a_et_b_egaux_partout": bool(seuils_egaux), "messages_de_refus": messages[:3]})
    return out


def section_H3(rep, Ks=(1, 10, 100)):
    """Graine du monde comme étiquette d'ordre (K9-5) : fiche seule (seuil 20), plan scellé de 4 tranches de 40 unités.
    À chaque génération, l'appelant essaie K graines du monde en privé (même banque : `evaluer` accepte l'engagement),
    garde la première dont la trajectoire franchit le seuil depuis la valeur courante (sinon la graine 0), puis évalue
    avec le journal sur un monde construit avec cette graine et ajoute la partie à la course."""
    compte = {K: 0 for K in Ks}
    verifie = None
    for r in range(rep):
        b = banque_nul_exact(random.Random(graine("H3", r)), 4, 40, identite="nul-exact-H3")
        m0 = mbs.MondeBanqueScores(b, 0)
        plan = plan_de(m0, 4)
        e = ea.construire(m0, CONTRASTE_NUL, 0.05, alpha_c=0.05, m_c=1, plan_tranches=plan)
        seuils = e["cle_heritage"]["seuils"]
        parts_g = {g: m0.parts(seuils, "epreuve", None, plan[g]) for g in range(1, 5)}
        trajs = {}
        for g in range(1, 5):
            for k in range(max(Ks)):
                mk = copy.copy(m0)
                mk.graine = k  # équivalent à MondeBanqueScores(b, k) (vérifié ci-dessous)
                ordre = mk.ordre_secret(parts_g[g], f"{e['empreinte']}|g{g}")
                trajs[(g, k)] = pa.trajectoire_log_richesse(m0.contrastes(parts_g[g], {"a": 1, "b": -1}, 0.0, ordre, None))
        if verifie is None:
            mk = mbs.MondeBanqueScores(b, 7)
            verifie = trajs[(2, 7)] == ea.evaluer(mk, e, generation=2)["trajectoire_log_min"]
        for K in Ks:
            lg = ea.Lignees()
            c = pa.Course(alpha=0.05, journal=lg)
            lg.entrer("O", e)
            c.entrer("g1", ["O"], 0.05, cles={"O": e["empreinte_cle"]})
            for g in range(1, 5):
                if "O" in c.promues or "O" in c.arretees:
                    break
                base, seuil = c.log_e["O"], c.seuil_log("O")
                choisie = next((k for k in range(K) if max(base + x for x in trajs[(g, k)]) >= seuil), 0)
                monde_choisi = m0 if choisie == 0 else mbs.MondeBanqueScores(b, choisie)
                ajouter(c, "O", ea.evaluer(monde_choisi, e, generation=g, fiche="O", journal=lg))
                c.lire()
            compte[K] += "O" in c.promues
    return {"repetitions": rep, "plan": "4 tranches de 40 unités", "seuil": 20,
            "promue": {f"K={K}": v / rep for K, v in compte.items()}, "reproduction_de_evaluer_verifiee": bool(verifie)}


# ---------------------------------------------------------------------------------------------------------------------
def section_C():
    out = {}
    nd = statistics.NormalDist(0.0, math.sqrt(1.0 + 0.6 ** 2))
    # banque publiée v28 : seuils scellés
    b = demo.banque(random.Random(graine_derivee(20261028, "banque")), 4, 40)
    m = mbs.MondeBanqueScores(b, graine_derivee(20261028, "monde"))
    out["banque_demo_empreinte"] = m.empreinte
    seuils = {c: m.seuil(c, 0.05)["seuil"] for c in demo.CELLULES}
    out["seuils_demo"] = seuils
    # simulation : rappel moyen par unité chez les sabotés, loi de la démonstration, aux seuils scellés
    rng = np.random.default_rng(graine("C", 1))
    U, S = 100_000, 8
    eta = rng.normal(0, 0.6, size=(U, 1))
    sim, ana = {}, {}
    for c in demo.CELLULES:
        x = eta + demo.DECALAGES[c] + rng.normal(0, 1, size=(U, S))
        sim[c] = float((x > seuils[c]).mean())
        ana[c] = demo.esperance_conditionnelle({c: 1}, seuils)
    out["rappel_simule_contre_formule"] = {c: {"simule": sim[c], "formule": ana[c], "ecart": sim[c] - ana[c]} for c in demo.CELLULES}
    out["ecart_max_absolu"] = max(abs(sim[c] - ana[c]) for c in demo.CELLULES)
    # « 0,5 ≈ 14 points de rappel au seuil τ = 0,05 » : au seuil vrai (quantile 95 % des honnêtes)
    s_vrai = nd.inv_cdf(0.95)
    rap = {d: 1 - nd.cdf(s_vrai - d) for d in (0.0, 0.3, 0.5, 0.7, 0.9, 1.0, 1.5)}
    out["rappel_au_seuil_vrai_par_decalage"] = rap
    out["points_pour_un_decalage_de_0_5"] = {"1,5 contre 1,0": rap[1.5] - rap[1.0], "1,0 contre 0,5": rap[1.0] - rap[0.5],
                                            "0,5 contre 0": rap[0.5] - rap[0.0]}
    # gardes de la forme G1 (δ = 0,10) : espérance conditionnelle de g = f_blanc − f_c chez les honnêtes
    nd_h = nd
    out["gardes_forme_G1_esperance_g"] = {c: (1 - nd_h.cdf(seuils["blanc"])) - (1 - nd_h.cdf(seuils[c])) for c in demo.COMPARATEURS_G1}
    return out


def principal():
    t0 = time.time()
    sortie = {"manifeste": {"script": os.path.basename(__file__), "sha256_script": sha(os.path.abspath(__file__)),
                            "racine": RACINE, "python": sys.version.split()[0], "numpy": np.__version__,
                            "plateforme": platform.platform(), "entropie_seedsequence": ENTROPIE, "REP": REP,
                            "sha256_code": {p: sha(os.path.join(RACINE, p)) for p in (
                                "pole/pari_apparie.py", "pole/engagement_apparie.py", "pole/monde_banque_scores.py",
                                "demonstrations/demo_pari_apparie_v7.py")}}}
    t = time.time(); sortie["A"] = section_A(); sortie["manifeste"]["duree_A"] = round(time.time() - t, 1)
    t = time.time(); sortie["G"] = section_G(max(200, REP)); sortie["manifeste"]["duree_G"] = round(time.time() - t, 1)
    t = time.time(); sortie["H_10"] = section_H(REP, 10); sortie["manifeste"]["duree_H_10"] = round(time.time() - t, 1)
    t = time.time(); sortie["H_30"] = section_H(max(50, REP // 2), 30); sortie["manifeste"]["duree_H_30"] = round(time.time() - t, 1)
    t = time.time(); sortie["H3"] = section_H3(REP); sortie["manifeste"]["duree_H3"] = round(time.time() - t, 1)
    t = time.time(); sortie["C"] = section_C(); sortie["manifeste"]["duree_C"] = round(time.time() - t, 1)
    sortie["manifeste"]["duree_secondes"] = round(time.time() - t0, 1)
    json.dump(sortie, sys.stdout, ensure_ascii=False, indent=1, sort_keys=True, default=str)
    print()


if __name__ == "__main__":
    principal()
