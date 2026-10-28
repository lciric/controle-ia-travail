"""Contre-vérification de la conception v9 du pari apparié borné et du code v7, versions 26 et 27 (contre-lecture R2).

Usage (depuis n'importe où ; rien n'est écrit dans le dépôt, sortie JSON sur la sortie standard) :
    REP=200 /opt/venv-essaim-sim-v1/bin/python -I -B contre-verification-pari-signe-v9.py RACINE_ORCHESTRATEUR > sortie.json

Sections :
  A  contrôles du code (clé, lignées, identifiants, journal, traces) — cas sains et artefacts (R5) ;
  B  étiquette d'ordre libre : « choisir l'ordre après coup » sous le nul (B1 pur, B2 par l'interface du code) ;
  C  « signe connu » des contrastes de la démonstration, conditionnellement aux seuils scellés ;
  D  la course de la démonstration répétée sur des banques neuves (fausses promotions, taux par fiche) ;
  E  rembourrage par des fiches vraies faciles (k* grandit, la barre des nulles baisse) ;
  F  G1 de la démonstration : composantes cumulées sur les tranches, règle de sortie (e-Bonferroni).
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
import sys
import time

import numpy as np

RACINE = os.path.abspath(sys.argv[1])
REP = int(os.environ.get("REP", "200"))
ENTROPIE = 2026102809
sys.path.insert(0, RACINE)

from pole import engagement_apparie as ea  # noqa: E402
from pole import monde_banque_scores as mbs  # noqa: E402
from pole import pari_apparie as pa  # noqa: E402
from pole.outils import graine_derivee  # noqa: E402

_spec = importlib.util.spec_from_file_location("demo_pari_apparie_v7",
                                               os.path.join(RACINE, "demonstrations", "demo_pari_apparie_v7.py"))
demo = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(demo)

SECTIONS = {"A": 1, "B1": 2, "B2": 3, "C": 4, "D": 5, "E": 6, "F": 7, "D10": 8}


def graine(section, i=0):
    s = np.random.SeedSequence(ENTROPIE, spawn_key=(SECTIONS[section], i))
    return int(s.generate_state(1, dtype=np.uint64)[0])


def sha(chemin):
    with open(chemin, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


def Phi(x):
    return 0.5 * (1.0 + math.erf(x / math.sqrt(2.0)))


SD_SABOTE = math.sqrt(1.0 + 0.6 ** 2)  # effet d'unité N(0 ; 0,6²) + bruit N(0 ; 1), démonstration


def rappel_population(seuil, decalage):
    return 1.0 - Phi((seuil - decalage) / SD_SABOTE)


def essai(f):
    try:
        return {"issue": "acceptée", "valeur": f()}
    except Exception as e:  # noqa: BLE001
        return {"issue": "refusée", "erreur": f"{type(e).__name__}: {str(e)[:160]}"}


# ---------------------------------------------------------------------------------------------------------------------
def section_A():
    s = {}
    rng = random.Random(graine("A", 1))
    b = demo.banque(rng, 2, 20, developpement=20)
    m = mbs.MondeBanqueScores(b, 5)
    coef = {"blanc": 1, "juge": -1}
    E_ep = ea.construire(m, {"c": {"coefficients": coef}}, 0.05, alpha_c=0.05, m_c=1, partie="epreuve")
    E_dev = ea.construire(m, {"c": {"coefficients": coef}}, 0.05, alpha_c=0.05, m_c=1, partie="developpement")
    E_tau = ea.construire(m, {"c": {"coefficients": coef}}, 0.10, alpha_c=0.05, m_c=1, partie="epreuve")
    champs = sorted(E_ep["cle_heritage"])
    s["A1_champs_de_la_cle"] = champs
    s["A1_champ_version_e_processus_present"] = any("version" in k or "processus" in k for k in champs)

    # A2 : une fiche, deux clés (développement puis épreuve ; puis τ changé) — Lignees et Course
    lg = ea.Lignees()
    lg.entrer("f", E_dev)
    s["A2_lignees_meme_fiche_seconde_cle"] = essai(lambda: lg.entrer("f", E_ep))["issue"]
    c = pa.Course(alpha=0.05)
    c.entrer("g1", ["f"], 0.05)
    r_dev = ea.evaluer(m, E_dev)
    r_ep = ea.evaluer(m, E_ep, unites=demo.unites_de_tranche(m, 1))
    r_tau = ea.evaluer(m, E_tau, unites=demo.unites_de_tranche(m, 2))
    s["A2_course_partie_developpement"] = essai(lambda: c.ajouter_trajectoire("f", r_dev["trajectoire_log_min"],
                                                                                unites=r_dev["identifiants_unites"]))["issue"]
    c.lire()
    s["A2_course_partie_epreuve_meme_fiche"] = essai(lambda: c.ajouter_trajectoire("f", r_ep["trajectoire_log_min"],
                                                                                     unites=r_ep["identifiants_unites"]))["issue"]
    c.lire()
    s["A2_course_partie_tau_change_meme_fiche"] = essai(lambda: c.ajouter_trajectoire("f", r_tau["trajectoire_log_min"],
                                                                                        unites=r_tau["identifiants_unites"]))["issue"]
    s["A2_cles_distinctes"] = len({E_dev["empreinte_cle"], E_ep["empreinte_cle"], E_tau["empreinte_cle"]}) == 3

    # A3 : même affirmation (mêmes coefficients), autre nom de contraste → autre clé → autre fiche acceptée
    E_x = ea.construire(m, {"x": {"coefficients": coef}}, 0.05)
    E_y = ea.construire(m, {"y": {"coefficients": coef}}, 0.05)
    lg3 = ea.Lignees()
    lg3.entrer("fx", E_x)
    s["A3_cles_x_y_identiques"] = E_x["empreinte_cle"] == E_y["empreinte_cle"]
    s["A3_relance_sous_autre_nom_avec_engagement_neuf"] = essai(lambda: lg3.entrer("fy", E_y))["issue"]
    s["A3_relance_meme_engagement_autre_fiche"] = essai(lambda: lg3.entrer("fz", E_x))["issue"]

    # A3b : doublons d'affirmation dans la démonstration publiée (proposeur reconstruit à l'identique)
    rngp = random.Random(graine_derivee(graine_derivee(20261028, "course"), "proposeur"))
    par_coef = {}
    for g in range(1, 5):
        for nom, fiche in demo.propositions(rngp, g, 6).items():
            cle = json.dumps(sorted(fiche["coefficients"].items())) + json.dumps(fiche.get("strate"))
            par_coef.setdefault(cle, []).append(nom)
    s["A3b_affirmations_portees_par_plusieurs_fiches"] = {k: v for k, v in par_coef.items() if len(v) > 1}

    # A4 : banque grandie d'une unité — identifiants (banque, partie, unité) disjoints, unités physiques communes
    rng4 = random.Random(graine("A", 4))
    b1 = demo.banque(rng4, 1, 40)
    b2 = copy.deepcopy(b1)
    extra = [dict(e, id=e["id"].replace("epr-1-0-", "epr-1-extra-"), unite="epr-1-extra")
             for e in b1["episodes"] if e["unite"] == "epr-1-0"]
    b2["episodes"] += copy.deepcopy(extra)
    m1, m2 = mbs.MondeBanqueScores(b1, 9), mbs.MondeBanqueScores(b2, 9)
    e1 = ea.construire(m1, {"c": {"coefficients": coef}}, 0.05)
    e2 = ea.construire(m2, {"c": {"coefficients": coef}}, 0.05)
    r1, r2 = ea.evaluer(m1, e1), ea.evaluer(m2, e2)
    phys = {u for _, _, u in r1["identifiants_unites"]} & {u for _, _, u in r2["identifiants_unites"]}
    ids = set(r1["identifiants_unites"]) & set(r2["identifiants_unites"])
    c4 = pa.Course(alpha=0.05)
    c4.entrer("g1", ["f"], 0.05)
    c4.ajouter_trajectoire("f", r1["trajectoire_log_min"], unites=r1["identifiants_unites"])
    c4.lire()
    s["A4_unites_physiques_communes"] = len(phys)
    s["A4_identifiants_communs"] = len(ids)
    s["A4_cles_identiques"] = e1["empreinte_cle"] == e2["empreinte_cle"]
    s["A4_seconde_partie_meme_fiche"] = essai(lambda: c4.ajouter_trajectoire("f", r2["trajectoire_log_min"],
                                                                              unites=r2["identifiants_unites"]))["issue"]
    s["A4_evaluer_engagement_1_sur_banque_2"] = essai(lambda: ea.evaluer(m2, e1))["issue"]

    # A5 : le journal est volontaire ; plusieurs évaluations d'une même fiche dans une génération ne sont pas vues
    lg5 = ea.Lignees()
    lg5.entrer("f", E_ep)
    c5 = pa.Course(alpha=0.05)
    c5.entrer("g1", ["f"], 0.05)
    _ = ea.evaluer(m, E_ep, unites=demo.unites_de_tranche(m, 1))  # partie calculée, non journalisée
    s["A5_sans_partie_mensonger_non_journalise_lignees"] = essai(lambda: lg5.verifier_sans_partie(1, {"f": "monde indisponible"}))["issue"]
    s["A5_sans_partie_mensonger_non_journalise_course"] = essai(lambda: sorted(c5.lire(sans_partie={"f": "monde indisponible"})))["issue"]
    lg5b = ea.Lignees()
    tr = demo.unites_de_tranche(m, 1)
    for k in range(5):
        lg5b.journaliser(1, "f", ea.evaluer(m, E_ep, unites=tr, etiquette_ordre=f"essai-{k}"))
    s["A5_cinq_evaluations_journalisees_meme_fiche_meme_generation"] = len([j for j in lg5b.journal if j["fiche"] == "f"])
    s["A5_une_garde_refuse_les_evaluations_multiples"] = any(hasattr(lg5b, n) for n in ("verifier_une_partie", "verifier_journal"))
    lg5c = ea.Lignees()
    lg5c.journaliser(7, "f", ea.evaluer(m, E_ep, unites=tr))  # numéro de génération libre, non lié à la Course
    s["A5_generation_du_journal_libre"] = essai(lambda: lg5c.verifier_sans_partie(1, {"f": "x"}))["issue"]

    # A6 : traces (K8-3) ; déclaration « sans partie » d'une fiche non active
    c6 = pa.Course(alpha=0.05)
    c6.entrer("g1", ["a", "b"], 0.04)
    c6.abandonner("a", avant_partie=True, motif="m1")
    c6.abandonner("a", motif="m2")
    s["A6_redite_tracee"] = c6.abandons.get(("redite", "a"))
    c6.ajouter_trajectoire("b", [0.1], unites={("x", "b", 1)})
    c6.lire(sans_partie={"a": "gelée", "b": "déclarée alors qu'elle a sa partie"})
    s["A6_sans_partie_enregistree_pour_gelee_et_pour_fiche_avec_partie"] = {str(k): v for k, v in c6.sans_partie.items()}

    # A7 : étiquette et tranche libres — l'interface accepte n'importe quel choix, sans trace
    t_a = ea.evaluer(m, E_ep, unites=tr, etiquette_ordre="a")["trajectoire_log_min"]
    t_b = ea.evaluer(m, E_ep, unites=tr, etiquette_ordre="b")["trajectoire_log_min"]
    s["A7_etiquettes_libres_trajectoires_differentes"] = t_a != t_b
    s["A7_finale_identique_a_l_ordre_pres"] = abs(t_a[-1] - t_b[-1]) < 1e-9
    s["A7_tranche_libre_sous_ensemble_quelconque"] = essai(lambda: ea.evaluer(m, E_ep, unites=tr[::3])["unites"])["issue"]
    return s


# ---------------------------------------------------------------------------------------------------------------------
LAM = np.array(pa.LAMBDAS)


def max_log_melange(v):
    """v : tableau (K, n) ; max sur t du log de la richesse mélangée, pour chaque ligne."""
    logs = np.cumsum(np.log1p(LAM[:, None, None] * v[None, :, :]), axis=2)  # (L, K, n)
    mx = logs.max(axis=0)
    mel = mx + np.log(np.exp(logs - mx[None]).mean(axis=0))
    return mel.max(axis=1)


def section_B1(rep):
    out = {}
    seuil = math.log(20)
    # contrôle : le calcul vectorisé égale `pa.trajectoire_log_richesse`
    rng = np.random.default_rng(graine("B1", 0))
    v = rng.choice([-0.25, 0.0, 0.25], size=40)
    assert abs(max(pa.trajectoire_log_richesse(list(v))) - max_log_melange(v[None, :])[0]) < 1e-9
    for nom_loi, loi in (("v_dans_{-0,25;0;0,25}", [-0.25, 0.0, 0.25]), ("v_dans_{-0,5;0,5}", [-0.5, 0.5])):
        for n in (40, 160):
            compte = {1: 0, 10: 0, 100: 0, 1000: 0}
            for r in range(rep):
                g = np.random.default_rng(graine("B1", 1000 * n + r + (500_000 if len(loi) == 2 else 0)))
                v = g.choice(loi, size=n)
                perms = np.array([g.permutation(v) for _ in range(1000)])
                croise = max_log_melange(perms) >= seuil
                for K in compte:
                    compte[K] += bool(croise[:K].any())
            out[f"{nom_loi}_n={n}"] = {f"K={K}": c / rep for K, c in compte.items()}
    out["monde"] = "v i.i.d. équiprobable sur la loi nommée (espérance nulle), seuil 20 (fiche seule, α = 0,05), K ordres essayés"
    out["repetitions"] = rep
    return out


def section_B2(rep):
    """Par l'interface du code : contraste « nul exact » blanc − blanc_jumeau de la démonstration, fiche seule (seuil 20),
    tranche de 40 unités (tranche 1) et partie entière (160 unités) ; K étiquettes essayées."""
    out = {"K=1": {}, "K=10": {}, "K=100": {}}
    seuil = math.log(20)
    verifie = False
    coef = {"blanc": 1, "blanc_jumeau": -1}
    comptes = {"tranche_40": {1: 0, 10: 0, 100: 0}, "partie_160": {1: 0, 10: 0, 100: 0}}
    for r in range(rep):
        b = demo.banque(random.Random(graine("B2", r)), 4, 40)
        m = mbs.MondeBanqueScores(b, graine("B2", 10_000 + r))
        E = ea.construire(m, {"nul": {"coefficients": coef}}, 0.05, alpha_c=0.05, m_c=1)
        for nom, unites in (("tranche_40", demo.unites_de_tranche(m, 1)), ("partie_160", None)):
            parts = m.parts(E["cle_heritage"]["seuils"], "epreuve", None, unites)
            croise = []
            for k in range(100):
                ordre = m.ordre_secret(parts, f"etiquette-{k}")
                vals = m.contrastes(parts, coef, 0.0, ordre, None)
                traj = pa.trajectoire_log_richesse(vals)
                croise.append(max(traj) >= seuil)
                if not verifie:
                    ref = ea.evaluer(m, E, unites=unites, etiquette_ordre=f"etiquette-{k}")["trajectoire_log_min"]
                    assert all(abs(x - y) < 1e-12 for x, y in zip(ref, traj)) and len(ref) == len(traj)
                    verifie = True
            for K in (1, 10, 100):
                comptes[nom][K] += any(croise[:K])
    return {nom: {f"K={K}": c / rep for K, c in d.items()} for nom, d in comptes.items()} | {
        "reproduction_de_evaluer_verifiee": verifie, "repetitions": rep}


# ---------------------------------------------------------------------------------------------------------------------
TEMOINS = {"temoin-vrai-fort": ({"blanc": 1, "juge": -1}, None), "temoin-vrai-moyen": ({"blanc": 1, "noir_action": -1}, None),
           "temoin-vrai-faible": ({"blanc": 1, "cascade": -1}, None), "temoin-vrai-tenu": ({"cascade": 1, "dernier_etat": -1}, None),
           "temoin-faux-nul": ({"blanc": 1, "blanc_jumeau": -1}, None), "temoin-faux-inverse": ({"juge": 1, "blanc": -1}, None),
           "temoin-vrai-concentre": ({"blanc": 1, "noir_sequentiel": -1}, {"mode": "concentre"})}


def esperance_conditionnelle(m, coefficients, strate=None, tau=0.05, decalages=None):
    decalages = decalages or demo.DECALAGES
    tot = 0.0
    for c, a in coefficients.items():
        s = m.seuil(c, tau, strate)["seuil"]
        tot += a * rappel_population(s, decalages[c])
    return tot


def section_C(rep):
    out = {}
    b = demo.banque(random.Random(graine_derivee(20261028, "banque")), 4, 40)
    m = mbs.MondeBanqueScores(b, graine_derivee(20261028, "monde"))
    out["banque_demo_empreinte"] = m.empreinte
    out["seuils_demo"] = {c: m.seuil(c, 0.05)["seuil"] for c in demo.CELLULES}
    out["rappel_population_au_seuil_scelle"] = {c: rappel_population(out["seuils_demo"][c], demo.DECALAGES[c]) for c in demo.CELLULES}
    out["rappel_population_au_seuil_vrai"] = {}
    s_vrai = 1.6448536269514722 * SD_SABOTE  # quantile 95 % des honnêtes : N(0 ; 1,36)
    for c in demo.CELLULES:
        out["rappel_population_au_seuil_vrai"][c] = rappel_population(s_vrai, demo.DECALAGES[c])
    out["temoins_demo"] = {}
    for nom, (coef, strate) in TEMOINS.items():
        out["temoins_demo"][nom] = {"esperance_connue_demo": demo.esperance_connue(coef),
                                    "esperance_conditionnelle_aux_seuils_scelles": esperance_conditionnelle(m, coef, strate)}
    out["G1_composantes_demo"] = {k: esperance_conditionnelle(m, {"blanc": 1, k: -1}) for k in demo.COMPARATEURS_G1}
    # sur des banques neuves (calibrage seul) : distribution de l'espérance conditionnelle
    nul_exact, tenu, tenu_neg, toutes_paires = [], [], 0, []
    for r in range(rep):
        bc = demo.banque(random.Random(graine("C", r)), 0, 0)
        mc = mbs.MondeBanqueScores(bc, 3)
        nul_exact.append(esperance_conditionnelle(mc, {"blanc": 1, "blanc_jumeau": -1}))
        t = esperance_conditionnelle(mc, {"cascade": 1, "dernier_etat": -1})
        tenu.append(t)
        tenu_neg += t <= 0
        bn = demo.banque(random.Random(graine("C", 100_000 + r)), 0, 0, nul=True)
        mn = mbs.MondeBanqueScores(bn, 3)
        zero = {c: 0.0 for c in demo.CELLULES}
        rs = {c: rappel_population(mn.seuil(c, 0.05)["seuil"], 0.0) for c in demo.CELLULES}
        toutes_paires += [rs[a] - rs[bb] for a in demo.CELLULES for bb in demo.CELLULES if a < bb]
        del zero
    a = np.abs(np.array(nul_exact))
    out["nul_exact_blanc_moins_jumeau"] = {"repetitions": rep, "part_positive": float(np.mean(np.array(nul_exact) > 0)),
                                           "moyenne_valeur_absolue": float(a.mean()), "quantile_90_valeur_absolue": float(np.quantile(a, 0.9)),
                                           "max_valeur_absolue": float(a.max())}
    out["tenu_cascade_moins_dernier_etat"] = {"esperance_au_seuil_vrai": out["rappel_population_au_seuil_vrai"]["cascade"]
                                              - out["rappel_population_au_seuil_vrai"]["dernier_etat"],
                                              "part_de_signe_conditionnel_negatif_ou_nul": tenu_neg / rep,
                                              "moyenne": float(np.mean(tenu))}
    tp = np.abs(np.array(toutes_paires))
    out["banques_nulles_toutes_paires"] = {"paires": len(toutes_paires), "moyenne_valeur_absolue": float(tp.mean()),
                                           "quantile_90_valeur_absolue": float(np.quantile(tp, 0.9))}
    return out


# ---------------------------------------------------------------------------------------------------------------------
def coefficients_de_la_course(graine_course, generations, n_hasard=6):
    rngp = random.Random(graine_derivee(graine_course, "proposeur"))
    coefs = {}
    for g in range(1, generations + 1):
        for nom, f in demo.propositions(rngp, g, n_hasard).items():
            coefs[nom] = (f["coefficients"], f.get("strate"))
    return coefs


def section_D(rep, generations, cle):
    res = {"repetitions": rep, "generations": generations, "au_moins_une_fausse_population": 0,
           "au_moins_une_fausse_conditionnelle": 0, "temoin_faux_nul_promu": 0, "fdp_population": [], "promues": [],
           "G1_promue": 0, "G1_bonferroni": 0, "temoin_vrai_faible_promu": 0, "temoin_vrai_faible_bonferroni": 0}
    for r in range(rep):
        b = demo.banque(random.Random(graine(cle, r)), generations, 40)
        m = mbs.MondeBanqueScores(b, graine(cle, 50_000 + r))
        gc = graine(cle, 90_000 + r)
        etat = demo.course(m, generations, 0.05, 0.05, gc)
        coefs = coefficients_de_la_course(gc, generations)
        promues = etat["promues"]
        fausses = [f for f in promues if etat["verites"][f] <= 1e-12]
        fausses_cond = []
        for f in promues:
            if f == "G1":
                ec = min(esperance_conditionnelle(m, {"blanc": 1, k: -1}) for k in demo.COMPARATEURS_G1)
            else:
                cf, st = coefs[f]
                ec = esperance_conditionnelle(m, cf, st)
            if ec <= 0:
                fausses_cond.append(f)
        res["au_moins_une_fausse_population"] += bool(fausses)
        res["au_moins_une_fausse_conditionnelle"] += bool(fausses_cond)
        res["temoin_faux_nul_promu"] += "temoin-faux-nul" in promues
        res["fdp_population"].append(len(fausses) / max(1, len(promues)))
        res["promues"].append(len(promues))
        res["G1_promue"] += "G1" in promues
        res["G1_bonferroni"] += "G1" in etat["bonferroni"]
        res["temoin_vrai_faible_promu"] += "temoin-vrai-faible" in promues
        res["temoin_vrai_faible_bonferroni"] += "temoin-vrai-faible" in etat["bonferroni"]
    res["fdr_population_moyen"] = float(np.mean(res["fdp_population"]))
    res["promues_moyenne"] = float(np.mean(res["promues"]))
    del res["fdp_population"], res["promues"]
    for k in ("au_moins_une_fausse_population", "au_moins_une_fausse_conditionnelle", "temoin_faux_nul_promu", "G1_promue",
              "G1_bonferroni", "temoin_vrai_faible_promu", "temoin_vrai_faible_bonferroni"):
        res[k + "_part"] = res[k] / rep
    return res


# ---------------------------------------------------------------------------------------------------------------------
def section_E(rep):
    """Course synthétique, G_max = 4, α = 0,05 : 14 fiches nulles en génération 1 (budget α/4/14 chacune), parties de
    20 unités v ∈ {−0,5 ; +0,5} équiprobables ; à partir de la génération 2, n fiches vraies « faciles » entrent par
    génération (log e = 50 : arrêtées au seuil dès leur partie)."""
    out = {}
    for n in (0, 6, 30, 200, 1000):
        une, fdp, fdp_aff = 0, [], []
        for r in range(rep):
            rng = random.Random(graine("E", 10_000 * n + r))
            c = pa.Course(alpha=0.05)
            nulles = [f"n{i}" for i in range(14)]
            c.entrer("g1", nulles, 0.0125)
            for g in range(1, 5):
                if g >= 2 and n:
                    vraies = [f"t{g}-{j}" for j in range(n)]
                    c.entrer(f"g{g}", vraies, 0.0125)
                    for f in vraies:
                        c.ajouter_trajectoire(f, [50.0], unites={(g, f, 0)})
                for f in nulles:
                    if f in c.gelees or f in c.promues or f in c.arretees:
                        continue
                    v = [rng.choice((-0.5, 0.5)) for _ in range(20)]
                    c.ajouter_trajectoire(f, pa.trajectoire_log_richesse(v), unites={(g, f, i) for i in range(20)})
                c.lire()
            fausses = [f for f in c.promues if f.startswith("n")]
            une += bool(fausses)
            fdp.append(len(fausses) / max(1, len(c.promues)))
            vraies_promues = any(f.startswith("t") for f in c.promues)  # les vraies : copies d'une seule affirmation
            fdp_aff.append(len(fausses) / max(1, len(fausses) + int(vraies_promues)))
        out[f"n_vraies_par_generation={n}"] = {"au_moins_une_nulle_promue": une / rep, "fdr_par_fiche": float(np.mean(fdp)),
                                               "fdr_par_affirmation_si_les_vraies_sont_des_copies": float(np.mean(fdp_aff))}
    out["repetitions"] = rep
    return out


# ---------------------------------------------------------------------------------------------------------------------
def section_F(dossier_demo):
    with open(os.path.join(dossier_demo, "course.json"), encoding="utf-8") as f:
        c = json.load(f)
    cumul, par_g = {}, {}
    for g in c["journal"]:
        p = g["parties"].get("G1")
        if not p:
            continue
        par_g[g["generation"]] = p["log_richesse_finale_par_comparateur"]
        for k, v in p["log_richesse_finale_par_comparateur"].items():
            cumul[k] = cumul.get(k, 0.0) + v
    return {"par_generation": par_g, "cumul_par_comparateur": cumul,
            "plus_faible_cumule": min(cumul, key=cumul.get), "plus_faible_derniere_partie": min(par_g[max(par_g)], key=par_g[max(par_g)].get),
            "log_e_G1": c["log_e"]["G1"], "seuil_log_G1": c["seuils_log"]["G1"], "G1_bonferroni": "G1" in c["bonferroni"],
            "bonferroni": c["bonferroni"], "promues": c["promues"]}


def principal():
    t0 = time.time()
    dossier_demo = os.path.join(os.path.dirname(RACINE), "pari-de-signe", "demonstration-v27")
    sortie = {"manifeste": {"script": os.path.basename(__file__), "sha256_script": sha(os.path.abspath(__file__)),
                            "racine": RACINE, "python": sys.version.split()[0], "numpy": np.__version__,
                            "plateforme": platform.platform(), "entropie_seedsequence": ENTROPIE, "REP": REP,
                            "sha256_code": {p: sha(os.path.join(RACINE, p)) for p in (
                                "pole/pari_apparie.py", "pole/engagement_apparie.py", "pole/monde_banque_scores.py",
                                "demonstrations/demo_pari_apparie_v7.py")},
                            "sha256_course_json_publie": sha(os.path.join(dossier_demo, "course.json"))}}
    sortie["A"] = section_A()
    sortie["B1"] = section_B1(REP)
    sortie["B2"] = section_B2(max(50, REP // 2))
    sortie["C"] = section_C(REP)
    sortie["D"] = section_D(REP, 4, "D")
    sortie["D10"] = section_D(max(30, REP // 4), 10, "D10")
    sortie["E"] = section_E(max(200, REP))
    sortie["F"] = section_F(dossier_demo)
    sortie["manifeste"]["duree_secondes"] = round(time.time() - t0, 1)
    json.dump(sortie, sys.stdout, ensure_ascii=False, indent=1, sort_keys=True, default=str)
    print()


if __name__ == "__main__":
    principal()
