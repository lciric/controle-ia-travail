"""Contre-vérification de la conception v11 du pari apparié borné et du code v7, version 29 (contre-lecture R2).

Usage (rien n'est écrit dans le dépôt ; sortie JSON sur la sortie standard) :
    REP=200 /opt/venv-essaim-sim-v1/bin/python -I -B contre-verification-pari-signe-v11.py RACINE_ORCHESTRATEUR > sortie.json

Sections :
  R  rejeu adapté à la version 29 des contrôles A1 à A10 de la contre-lecture v10 (cas sains et artefacts, R5), et
     contrôles nouveaux N1 à N10 sur `jouer_generation`, le journal, la `Course` publique ;
  H  chaînes mesurées sur une banque à nul exact (reprise de `banque_nul_exact` de la contre-lecture v10, seuils scellés
     égaux par construction), 20 unités par tranche, α = 0,05 :
       H1 fiche seule (seuil 20) : honnête par `jouer_generation` ; (a) chaîne v10 telle quelle (évaluation privée sans
          journal puis `Course.lire(sans_partie=…)`) ; (b) évaluation privée puis `jouer_generation(non_lancees=…)` ;
          (c) évaluation « fantôme » journalisée sous un autre nom de fiche, puis `jouer_generation(non_lancees=…)` ;
       H2 famille {A-espion, O} (seuil 40) : honnête par `jouer_generation` ; (a) chaîne v10 (espionne à autre étiquette
          `population`) — arrêtée par `Lignees` ; (b) espionne corrélée (τ = 0,051 : autre affirmation, mêmes seuils,
          même valeur finale) par l'interface publique de la `Course` ; (c) la même par `jouer_generation`, la règle
          `abandon_apres` voyant l'issue de l'espionne avant le calcul de O et interrompant la génération ;
  H3 graine du monde essayée K fois (canal d'ordre restant de K10-3), adapté de la contre-lecture v10 ;
  F  la forme G1 de la course publiée v29 : incréments de log e contre le processus minimal rapporté par partie.
Graines : numpy.random.SeedSequence(ENTROPIE, spawn_key=(section, indice)) (R9), converties en entiers pour `random`.
"""

import copy
import hashlib
import importlib.util
import json
import os
import platform
import random
import sys
import time
import types

import numpy as np

RACINE = os.path.abspath(sys.argv[1])
REP = int(os.environ.get("REP", "200"))
ENTROPIE = 2026102811
sys.path.insert(0, RACINE)

from pole import engagement_apparie as ea  # noqa: E402
from pole import monde_banque_scores as mbs  # noqa: E402
from pole import pari_apparie as pa  # noqa: E402
from pole.outils import graine_derivee  # noqa: E402

_spec = importlib.util.spec_from_file_location("demo_pari_apparie_v7",
                                               os.path.join(RACINE, "demonstrations", "demo_pari_apparie_v7.py"))
demo = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(demo)

SECTIONS = {"R": 1, "H": 2, "H3": 3, "F": 4}


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


def issue(f):
    return essai(f)["issue"]


def ajouter(c, fiche, r, **surcharge):
    kw = dict(unites=r["identifiants_unites"], empreinte_cle=r["empreinte_cle"], empreinte_unites=r["empreinte_unites"])
    kw.update(surcharge)
    return c.ajouter_trajectoire(fiche, r["trajectoire_log_min"], **kw)


def course_neuve(engagements):
    """Course de production (journal obligatoire, clés obligatoires), lignées entrées."""
    lg = ea.Lignees()
    for f, e in engagements.items():
        lg.entrer(f, e)
    c = pa.Course(alpha=0.05, journal=lg)
    c.entrer("g1", list(engagements), 0.05, cles={f: e["empreinte_cle"] for f, e in engagements.items()})
    return lg, c


class Interruption(Exception):
    pass


# ---------------------------------------------------------------------------------------------------------------------
def section_R():
    s = {}
    rng = random.Random(graine("R", 1))
    b = demo.banque(rng, 2, 20, developpement=20)
    m = mbs.MondeBanqueScores(b, 5)
    t1, t2 = demo.unites_de_tranche(m, 1), demo.unites_de_tranche(m, 2)
    plan = {1: t1, 2: t2}
    coef = {"blanc": 1, "juge": -1}
    E_ep = ea.construire(m, {"c": {"coefficients": coef}}, 0.05, alpha_c=0.05, m_c=1, partie="epreuve", plan_tranches=plan)
    E_tau = ea.construire(m, {"c": {"coefficients": coef}}, 0.10, alpha_c=0.05, m_c=1, partie="epreuve", plan_tranches=plan)
    E_pop = ea.construire(m, {"c": {"coefficients": coef}}, 0.05, plan_tranches=plan, population="vivier-espion")

    # A1 : clé en deux parties ; version de l'e-processus
    s["A1_champs_de_la_cle"] = sorted(E_ep["cle_heritage"])
    s["A1_affirmation"] = sorted(E_ep["cle_heritage"]["affirmation"])
    s["A1_lecture"] = sorted(E_ep["cle_heritage"]["lecture"])
    s["A1_e_processus_version"] = E_ep["cle_heritage"]["e_processus"]["version"]
    # A2 / A9 : course sans journal, entrée sans clés
    s["A9_course_sans_journal"] = issue(lambda: pa.Course(alpha=0.05))
    s["A2_entree_sans_cles"] = issue(lambda: pa.Course(alpha=0.05, journal=ea.Lignees()).entrer("g1", ["f"], 0.05))
    # A3 : même affirmation, autre population : Lignees la refuse ; la Course seule ?
    lg3 = ea.Lignees()
    lg3.entrer("O", E_ep)
    s["A3_population_lignees_seconde_fiche"] = issue(lambda: lg3.entrer("S", E_pop))
    s["A3_population_meme_affirmation"] = E_pop["empreinte_affirmation"] == E_ep["empreinte_affirmation"]
    s["A3_population_cle_differente"] = E_pop["empreinte_cle"] != E_ep["empreinte_cle"]
    lg3b = ea.Lignees()
    c3 = pa.Course(alpha=0.05, journal=lg3b)
    s["A3_course_sans_lignees_deux_fiches_meme_affirmation_entree"] = issue(
        lambda: c3.entrer("g1", ["O", "S"], 0.05, cles={"O": E_ep["empreinte_cle"], "S": E_pop["empreinte_cle"]}))
    s["A3_jouer_generation_deux_fiches_meme_affirmation_hors_lignees"] = essai(
        lambda: ea.jouer_generation(c3, m, {"O": E_ep, "S": E_pop})["parties"].keys().__len__())
    # ordre : même affirmation, autre population ou autre découpage du plan → autre ordre ?
    rA = ea.evaluer(m, E_ep, generation=1)
    rP = ea.evaluer(m, E_pop, generation=1)
    s["A3_population_change_l_ordre"] = rA["trajectoire_log_min"] != rP["trajectoire_log_min"]
    s["A3_population_finale_egale"] = abs(rA["trajectoire_log_min"][-1] - rP["trajectoire_log_min"][-1]) < 1e-9

    # A4 : banque sans identité déclarée
    b_sans = copy.deepcopy(b)
    b_sans.pop("identite")
    s["A4_banque_sans_identite_acceptee"] = issue(lambda: ea.construire(mbs.MondeBanqueScores(b_sans, 5), {"c": {"coefficients": coef}}, 0.05))
    s["A4_identite_de_repli"] = "empreinte de la banque" if mbs.MondeBanqueScores(b_sans, 5).identite == mbs.MondeBanqueScores(b_sans, 5).empreinte else "autre"

    # A5a : évaluation privée (sans journal) ; puis « sans partie » par la Course, puis par jouer_generation
    s["A5a_evaluer_sans_journal"] = issue(lambda: ea.evaluer(m, E_ep, generation=1)["unites"])
    lg, c = course_neuve({"f": E_ep})
    ea.evaluer(m, E_ep, generation=1)
    s["A5a_puis_sans_partie_par_course_lire"] = issue(lambda: c.lire(sans_partie={"f": "monde indisponible"}))
    lg, c = course_neuve({"f": E_ep})
    ea.evaluer(m, E_ep, generation=1)
    s["A5a_puis_non_lancee_par_jouer_generation"] = issue(lambda: ea.jouer_generation(c, m, {"f": E_ep}, non_lancees={"f": "x"}))
    # A5c : génération du journal choisie par l'appelant hors de jouer_generation (lecture d'avance)
    lg, c = course_neuve({"f": E_ep})
    avance = essai(lambda: ea.evaluer(m, E_ep, generation=2, fiche="f", journal=lg))
    s["A5c_tranche_2_journalisee_pendant_la_generation_1"] = avance["issue"]
    ea.jouer_generation(c, m, {"f": E_ep})
    if "f" in c.arretees or "f" in c.promues:
        s["A5c_suite"] = "fiche arrêtée en génération 1 : suite non testée"
    else:
        s["A5c_puis_jouer_generation_en_generation_2"] = essai(lambda: ea.jouer_generation(c, m, {"f": E_ep}))["issue"]
        s["A5c_puis_ajout_direct_de_la_partie_d_avance"] = issue(lambda: ajouter(c, "f", avance["valeur"]))
    # A5d : journal en lecture seule ; l'attribut privé
    lg = ea.Lignees()
    ea.evaluer(m, E_ep, generation=1, fiche="f", journal=lg)
    s["A5d_effacer_par_journal_public"] = issue(lambda: lg.journal.__setitem__(slice(None), []))
    s["A5d_effacer_par_attribut_prive"] = issue(lambda: lg._journal.clear())
    # A6 inchangé (rapporté) ; A7 : graine du monde
    m_autre = mbs.MondeBanqueScores(b, 6)
    tb = essai(lambda: ea.evaluer(m_autre, E_ep, generation=1)["trajectoire_log_min"])
    s["A7_meme_engagement_monde_d_autre_graine"] = tb["issue"]
    s["A7_trajectoire_differente"] = tb.get("valeur") != rA["trajectoire_log_min"]
    s["A7_graine_dans_l_engagement"] = any("graine" in str(k) for k in E_ep) or "graine" in json.dumps(E_ep["cle_heritage"])
    lg, c = course_neuve({"f": E_ep})
    s["A7_jouer_generation_sur_monde_d_autre_graine"] = issue(lambda: ea.jouer_generation(c, m_autre, {"f": E_ep}))
    # A8 : abandon « avant partie » alors que la partie de la fiche est au journal
    lg, c = course_neuve({"f": E_ep, "h": E_tau})
    ea.evaluer(m, E_ep, generation=1, fiche="f", journal=lg)
    s["A8_avant_partie_par_course_partie_au_journal"] = issue(lambda: c.abandonner("f", avant_partie=True, motif="x"))
    lg, c = course_neuve({"f": E_ep, "h": E_tau})
    ea.evaluer(m, E_ep, generation=1, fiche="f", journal=lg)
    s["A8_avant_partie_par_jouer_generation_partie_au_journal"] = issue(
        lambda: ea.jouer_generation(c, m, {"f": E_ep, "h": E_tau}, abandons_avant={"f": "retrait"}))
    # A10 : partie vide
    E_conc = ea.construire(m, {"c": {"coefficients": coef}}, 0.05, strate={"mode": "concentre"}, plan_tranches=plan)
    lg, c = course_neuve({"k": E_conc})
    cr = essai(lambda: ea.jouer_generation(c, m, {"k": E_conc}))
    s["A10_partie_vide_par_jouer_generation"] = cr["issue"]
    s["A10_vides"] = list(cr["valeur"]["vides"]) if cr["issue"] == "acceptée" else None

    # N1 : évaluation « fantôme » journalisée sous un nom de fiche non entré
    lg, c = course_neuve({"f": E_ep})
    s["N1_journal_accepte_un_nom_non_entre"] = issue(lambda: ea.evaluer(m, E_ep, generation=1, fiche="fantome", journal=lg))
    s["N1_puis_non_lancee_par_jouer_generation"] = issue(lambda: ea.jouer_generation(c, m, {"f": E_ep}, non_lancees={"f": "x"}))
    # N2 : trajectoire fabriquée, journal en ordre
    lg, c = course_neuve({"f": E_ep})
    r = ea.evaluer(m, E_ep, generation=1, fiche="f", journal=lg)
    s["N2_trajectoire_fabriquee_ajoutee"] = issue(lambda: c.ajouter_trajectoire("f", [10.0], unites=r["identifiants_unites"],
                                                                                empreinte_cle=r["empreinte_cle"], empreinte_unites=r["empreinte_unites"]))
    s["N2_puis_promue"] = "f" in c.lire()
    # N3 : partie d'une autre clé journalisée sous f, empreinte de clé déclarée par l'appelant
    lg, c = course_neuve({"f": E_ep})
    r_tau = ea.evaluer(m, E_tau, generation=1, fiche="f", journal=lg)
    s["N3_journal_autre_cle_sous_f"] = [j["empreinte_cle"] == E_tau["empreinte_cle"] for j in lg.journal]
    s["N3_ajout_avec_cle_declaree_fausse"] = issue(lambda: ajouter(c, "f", r_tau, empreinte_cle=E_ep["empreinte_cle"]))
    # N4 : la règle abandon_apres voit l'issue d'une fiche avant le calcul des suivantes, et peut interrompre
    E_tau51 = ea.construire(m, {"c": {"coefficients": coef}}, 0.051, alpha_c=0.05, m_c=2, plan_tranches=plan)
    E_O = ea.construire(m, {"c": {"coefficients": coef}}, 0.05, alpha_c=0.05, m_c=2, plan_tranches=plan)
    s["N4_espionne_tau_0_051_autre_affirmation"] = E_tau51["empreinte_affirmation"] != E_O["empreinte_affirmation"]
    s["N4_espionne_memes_seuils"] = E_tau51["cle_heritage"]["seuils"] == E_O["cle_heritage"]["seuils"]
    lg, c = course_neuve({"A-espion": E_tau51, "O": E_O})
    vu = {}

    def regle(f, valeur):
        vu[f] = [j["fiche"] for j in lg.journal]
        raise Interruption()

    s["N4_jouer_generation_interrompue"] = issue(lambda: ea.jouer_generation(c, m, {"A-espion": E_tau51, "O": E_O}, abandon_apres=regle))
    s["N4_journal_vu_par_la_regle"] = vu
    s["N4_puis_course_lire_sans_partie_O"] = issue(lambda: sorted(c.lire(sans_partie={"O": "fiche non lancée"})))
    # N5 : la règle gèle une autre fiche « avant partie » après l'issue de la première
    lg, c = course_neuve({"A-espion": E_tau51, "O": E_O})

    def regle2(f, valeur):
        if f == "A-espion":
            c.abandonner("O", avant_partie=True, motif="retrait")
        return None

    s["N5_jouer_generation"] = essai(lambda: ea.jouer_generation(c, m, {"A-espion": E_tau51, "O": E_O}, abandon_apres=regle2))["issue"]
    s["N5_O_gelee_avant_partie"] = c.abandons.get("O")
    s["N5_puis_course_lire"] = issue(lambda: sorted(c.lire()))
    # N6 : refus de fraîcheur dans jouer_generation (deux fiches, plans croisés) : sortie honnête ?
    E_x = ea.construire(m, {"c": {"coefficients": coef}}, 0.05, alpha_c=0.025, m_c=2, plan_tranches={1: t1, 2: t2})
    E_z = ea.construire(m, {"c": {"coefficients": {"blanc": 1, "cascade": -1}}}, 0.05, alpha_c=0.025, m_c=2, plan_tranches={1: t2, 2: t1})
    lg, c = course_neuve({"x": E_x, "z": E_z})
    s["N6_generation_1"] = issue(lambda: ea.jouer_generation(c, m, {"x": E_x, "z": E_z}))
    actives = [f for f in ("x", "z") if f not in c.promues | c.arretees]
    s["N6_actives_en_generation_2"] = actives
    g2 = essai(lambda: ea.jouer_generation(c, m, {"x": E_x, "z": E_z}))
    s["N6_generation_2"] = g2
    s["N6_relance_de_jouer_generation"] = essai(lambda: ea.jouer_generation(c, m, {"x": E_x, "z": E_z}))["issue"]
    s["N6_sans_partie_honnete_apres_refus"] = issue(lambda: c.lire(sans_partie={f: "partie refusée par la course" for f in actives}))
    s["N6_avant_partie_mensonger_apres_refus"] = issue(lambda: [c.abandonner(f, avant_partie=True, motif="x") for f in actives])
    # N7 : engagement sans plan dans jouer_generation
    E_np = ea.construire(m, {"c": {"coefficients": coef}}, 0.05)
    lg, c = course_neuve({"f": E_np})
    s["N7_sans_plan_generation_1"] = essai(lambda: ea.jouer_generation(c, m, {"f": E_np})["parties"]["f"]["unites"])["issue"]
    if "f" not in c.promues | c.arretees:
        s["N7_sans_plan_generation_2"] = essai(lambda: ea.jouer_generation(c, m, {"f": E_np}))
    # N8 : journal d'un autre type, clés quelconques
    faux = types.SimpleNamespace(journal=())
    s["N8_course_avec_journal_quelconque"] = issue(lambda: pa.Course(alpha=0.05, journal=faux))
    c8 = pa.Course(alpha=0.05, journal=faux)
    s["N8_cles_quelconques"] = issue(lambda: c8.entrer("g1", ["f"], 0.05, cles={"f": "n'importe quelle chaîne"}))
    ea.evaluer(m, E_ep, generation=1)
    s["N8_puis_sans_partie"] = issue(lambda: c8.lire(sans_partie={"f": "x"}))
    # N9 : premiere_lecture n'est remplie qu'à l'ajout : unités lues par un fantôme restent fraîches
    lg, c = course_neuve({"f": E_ep})
    ea.evaluer(m, E_ep, generation=1, fiche="fantome", journal=lg)
    s["N9_unites_du_fantome_dans_premiere_lecture"] = len(c.premiere_lecture)
    # N10 : génération entière par la course dans jouer_generation (cas sain) ; chaîne refusée ; bool
    lg = ea.Lignees()
    s["N10_generation_en_chaine"] = issue(lambda: ea.evaluer(m, E_ep, generation="1", fiche="f", journal=lg))
    s["N10_generation_5_hors_course"] = issue(lambda: ea.evaluer(m, ea.construire(m, {"c": {"coefficients": coef}}, 0.05), generation=5,
                                                                unites=t1, fiche="g", journal=lg))
    return s


# ---------------------------------------------------------------------------------------------------------------------
def banque_nul_exact(rng, tranches, unites_par_tranche, calibrage=60, sabotes=8, honnetes=8, sigma=0.6, decalage=1.5,
                     identite="nul-exact"):
    """Reprise à l'identique de la contre-lecture v10 : deux cellules a et b ; calibrage honnête de scores identiques sur a
    et b (seuils scellés égaux) ; épreuve : a et b de même loi ; a − b d'espérance nulle conditionnellement aux seuils."""
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


def actif(c, f):
    return f not in c.promues and f not in c.arretees and f not in c.gelees


def section_H(rep, generations):
    cles = ("H1_honnete", "H1a_chaine_v10", "H1b_prive_puis_non_lancee", "H1c_fantome_puis_non_lancee",
            "H2_honnete_O", "H2_honnete_une", "H2b_espionne_correlee_course_O", "H2b_une",
            "H2c_espionne_correlee_jouer_generation_O", "H2c_une")
    res = {k: 0 for k in cles}
    refus, messages, decl = {}, [], {k: 0 for k in ("H1a", "H1b", "H1c", "H2b", "H2c")}
    seuils_egaux, espionne_meme_finale, h2a = True, True, None
    for r in range(rep):
        b = banque_nul_exact(random.Random(graine("H", generations, r)), generations, 20)
        m = mbs.MondeBanqueScores(b, graine("H", generations, 10_000 + r))
        plan = plan_de(m, generations)
        eO = ea.construire(m, CONTRASTE_NUL, 0.05, alpha_c=0.05, m_c=1, plan_tranches=plan)
        seuils_egaux &= eO["cle_heritage"]["seuils"]["a"] == eO["cle_heritage"]["seuils"]["b"]
        eO2 = ea.construire(m, CONTRASTE_NUL, 0.05, alpha_c=0.05, m_c=2, plan_tranches=plan)
        eS = ea.construire(m, CONTRASTE_NUL, 0.051, alpha_c=0.05, m_c=2, plan_tranches=plan)  # autre affirmation, mêmes seuils
        if eS["cle_heritage"]["seuils"] != eO2["cle_heritage"]["seuils"]:
            espionne_meme_finale = False
        if h2a is None:  # H2a : l'espionne de la contre-lecture v10 (autre population) — la mémoire la refuse
            ePop = ea.construire(m, CONTRASTE_NUL, 0.05, alpha_c=0.05, m_c=2, plan_tranches=plan, population="vivier-espion")
            lg0 = ea.Lignees()
            lg0.entrer("O", eO2)
            h2a = essai(lambda: lg0.entrer("S", ePop))
        try:
            # --- H1 : fiche seule
            for mode in ("H1_honnete", "H1a_chaine_v10", "H1b_prive_puis_non_lancee", "H1c_fantome_puis_non_lancee"):
                lg, c = course_neuve({"O": eO})
                for g in range(1, generations + 1):
                    if not actif(c, "O"):
                        break
                    if mode == "H1_honnete":
                        ea.jouer_generation(c, m, {"O": eO})
                        continue
                    if mode == "H1c_fantome_puis_non_lancee":
                        vu = ea.evaluer(m, eO, generation=c.generation, fiche=f"fantome-{g}", journal=lg)
                    else:
                        vu = ea.evaluer(m, eO, generation=c.generation)  # sans journal
                    defavorable = vu["trajectoire_log_min"][-1] <= 0.0
                    if mode == "H1a_chaine_v10":
                        if defavorable:
                            c.lire(sans_partie={"O": "monde indisponible"})
                            decl["H1a"] += 1
                        else:
                            ajouter(c, "O", ea.evaluer(m, eO, generation=c.generation, fiche="O", journal=lg))
                            c.lire()
                    else:
                        ea.jouer_generation(c, m, {"O": eO}, non_lancees=({"O": "monde indisponible"} if defavorable else None))
                        decl["H1b" if mode.startswith("H1b") else "H1c"] += defavorable
                res[mode] += "O" in c.promues
            # --- H2 : famille {A-espion, O} ; l'espionne lit la première (ordre des noms dans jouer_generation)
            engs = {"A-espion": eS, "O": eO2}
            for mode in ("H2_honnete", "H2b", "H2c"):
                lg, c = course_neuve(engs)
                for g in range(1, generations + 1):
                    if not (actif(c, "A-espion") or actif(c, "O")):
                        break
                    if mode == "H2_honnete":
                        ea.jouer_generation(c, m, engs)
                        continue
                    if mode == "H2b":  # interface publique de la Course (chaîne v10, espionne corrélée)
                        sans_partie, favorable = {}, True
                        if actif(c, "A-espion"):
                            rS = ea.evaluer(m, eS, generation=c.generation, fiche="A-espion", journal=lg)
                            ajouter(c, "A-espion", rS)
                            favorable = rS["trajectoire_log_min"][-1] > 0.0
                            if g == 1 and actif(c, "O"):
                                rO_ = ea.evaluer(m, eO2, generation=1)  # contrôle : même valeur finale
                                if abs(rO_["trajectoire_log_min"][-1] - rS["trajectoire_log_min"][-1]) > 1e-9:
                                    espionne_meme_finale = False
                        if actif(c, "O"):
                            if not favorable:
                                sans_partie["O"] = "fiche non lancée"
                                decl["H2b"] += 1
                            else:
                                ajouter(c, "O", ea.evaluer(m, eO2, generation=c.generation, fiche="O", journal=lg))
                        c.lire(sans_partie=sans_partie)
                        continue
                    # H2c : par jouer_generation ; la règle d'abandon voit l'issue de l'espionne et interrompt
                    avant = c.log_e["A-espion"]

                    def regle(f, valeur, avant=avant, c=c):
                        if f == "A-espion" and actif(c, "O") and valeur - avant <= 0.0:
                            raise Interruption()
                        return None

                    try:
                        ea.jouer_generation(c, m, engs, abandon_apres=regle)
                    except Interruption:
                        c.lire(sans_partie={"O": "fiche non lancée"})
                        decl["H2c"] += 1
                promu_O, une = "O" in c.promues, bool(c.promues)
                if mode == "H2_honnete":
                    res["H2_honnete_O"] += promu_O
                    res["H2_honnete_une"] += une
                elif mode == "H2b":
                    res["H2b_espionne_correlee_course_O"] += promu_O
                    res["H2b_une"] += une
                else:
                    res["H2c_espionne_correlee_jouer_generation_O"] += promu_O
                    res["H2c_une"] += une
        except (ValueError, ea.EngagementInvalide) as e:
            refus[type(e).__name__] = refus.get(type(e).__name__, 0) + 1
            messages.append(str(e)[:160])
    out = {k: v / rep for k, v in res.items()}
    out.update({"repetitions": rep, "generations": generations, "unites_par_tranche": 20, "refus": refus,
                "messages_de_refus": messages[:3], "declarations_par_course": {k: v / rep for k, v in decl.items()},
                "seuils_scelles_a_et_b_egaux_partout": bool(seuils_egaux),
                "espionne_tau_0_051_memes_seuils_meme_finale": bool(espionne_meme_finale),
                "H2a_espionne_v10_autre_population": h2a})
    return out


def section_H3(rep, Ks=(1, 10, 100)):
    """Graine du monde comme étiquette d'ordre (canal restant de K10-3) : fiche seule (seuil 20), 4 tranches de 40 unités ;
    à chaque génération l'appelant essaie K graines en privé et garde la première qui franchit le seuil, puis joue la
    génération par jouer_generation sur un monde construit avec cette graine (même banque : engagement accepté)."""
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
                mk.graine = k
                ordre = mk.ordre_secret(parts_g[g], f"{e['empreinte_cle']}|g{g}")
                trajs[(g, k)] = pa.trajectoire_log_richesse(m0.contrastes(parts_g[g], {"a": 1, "b": -1}, 0.0, ordre, None))
        if verifie is None:
            verifie = trajs[(2, 7)] == ea.evaluer(mbs.MondeBanqueScores(b, 7), e, generation=2)["trajectoire_log_min"]
        mondes = {}
        for K in Ks:
            lg, c = course_neuve({"O": e})
            for g in range(1, 5):
                if not actif(c, "O"):
                    break
                base, seuil = c.log_e["O"], c.seuil_log("O")
                choisie = next((k for k in range(K) if max(base + x for x in trajs[(g, k)]) >= seuil), 0)
                if choisie not in mondes:
                    mondes[choisie] = m0 if choisie == 0 else mbs.MondeBanqueScores(b, choisie)
                ea.jouer_generation(c, mondes[choisie], {"O": e})
            compte[K] += "O" in c.promues
    return {"repetitions": rep, "plan": "4 tranches de 40 unités", "seuil": 20,
            "promue": {f"K={K}": v / rep for K, v in compte.items()}, "reproduction_de_evaluer_verifiee": bool(verifie)}


# ---------------------------------------------------------------------------------------------------------------------
def section_F():
    dossier = os.path.join(os.path.dirname(RACINE), "pari-de-signe", "demonstration-v29")
    with open(os.path.join(dossier, "course.json"), encoding="utf-8") as f:
        publie = json.load(f)
    with open(os.path.join(dossier, "lecture-pari-apparie.json"), encoding="utf-8") as f:
        lec = json.load(f)
    out = {"parties": {}}
    precedent = 0.0
    for x in publie["journal"]:
        p = x["parties"].get("forme-G1")
        if p is None:
            continue
        rap = next(q for q in lec["L3_forme_G1"]["parties"] if q["generation"] == x["generation"])
        tout = dict(p["log_richesse_finale_par_comparateur"])
        tout.update({f"garde:{k}": v for k, v in p["log_gardes_finales"].items()})
        out["parties"][x["generation"]] = {"increment": p["log_e_valeur"] - precedent, "processus_minimal_recalcule": min(tout, key=tout.get),
                                           "valeur_minimale": min(tout.values()), "processus_minimal_rapporte": rap["processus_minimal"],
                                           "valeur_rapportee": rap["valeur"], "arretee": p["arretee"]}
        precedent = p["log_e_valeur"]
    out["log_e_final"] = publie["log_e"]["forme-G1"]
    out["seuil_log"] = publie["seuils_log"]["forme-G1"]
    out["promue"] = "forme-G1" in publie["promues"]
    out["bonferroni"] = "forme-G1" in publie["bonferroni"]
    cumul = {}
    for x in publie["journal"]:
        p = x["parties"].get("forme-G1")
        if p:
            for k, v in list(p["log_richesse_finale_par_comparateur"].items()) + [(f"garde:{k}", v) for k, v in p["log_gardes_finales"].items()]:
                cumul[k] = cumul.get(k, 0.0) + v
    out["cumul_par_composante"] = cumul
    # le compte rendu de jouer_generation : champs par fiche
    out["champs_du_compte_rendu_par_fiche"] = sorted(next(iter(publie["journal"][0]["parties"].values())))
    return out


def principal():
    t0 = time.time()
    sortie = {"manifeste": {"script": os.path.basename(__file__), "sha256_script": sha(os.path.abspath(__file__)),
                            "racine": RACINE, "python": sys.version.split()[0], "numpy": np.__version__,
                            "plateforme": platform.platform(), "entropie_seedsequence": ENTROPIE, "REP": REP,
                            "sha256_code": {p: sha(os.path.join(RACINE, p)) for p in (
                                "pole/pari_apparie.py", "pole/engagement_apparie.py", "pole/monde_banque_scores.py",
                                "demonstrations/demo_pari_apparie_v7.py")}}}
    t = time.time(); sortie["R"] = section_R(); sortie["manifeste"]["duree_R"] = round(time.time() - t, 1)
    t = time.time(); sortie["F"] = section_F(); sortie["manifeste"]["duree_F"] = round(time.time() - t, 1)
    t = time.time(); sortie["H_10"] = section_H(REP, 10); sortie["manifeste"]["duree_H_10"] = round(time.time() - t, 1)
    t = time.time(); sortie["H_30"] = section_H(max(4, REP // 2), 30); sortie["manifeste"]["duree_H_30"] = round(time.time() - t, 1)
    t = time.time(); sortie["H3"] = section_H3(REP); sortie["manifeste"]["duree_H3"] = round(time.time() - t, 1)
    sortie["manifeste"]["duree_secondes"] = round(time.time() - t0, 1)
    json.dump(sortie, sys.stdout, ensure_ascii=False, indent=1, sort_keys=True, default=str)
    print()


if __name__ == "__main__":
    principal()
