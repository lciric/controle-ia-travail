"""Contre-vérification de la conception v6 du pari apparié borné et du code `pole/pari_apparie.py` (v7, version 21).

Contre-lecteur neuf (Fable 5.1). Processeur seul ; aucun fichier du dépôt modifié ; graines par numpy.random.SeedSequence
(entropie 2026102721, clé de dérivation (section, indice)), consignées dans la sortie.

Sections :
  U  — les essais du dépôt (`essais/test_v7_pari_apparie.py`) lancés tels quels, sans écrire de bytecode ;
  E  — cas limites de `ebh_pondere` : ex æquo au bord, somme des budgets entre α et 1 acceptée, course vide ;
  C  — cas limites de `Course` : abandonnée gelée promue plus tard quand k* grandit ; fiche arrêtée non promue puis lue ;
       ordre des appels « abandonner avant ajouter_trajectoire » (la partie est jetée, silencieusement) ;
  H  — D-S25 bis sous nul complet, familles entrées à des générations différentes avec des budgets différents (suite
       6/(π²g²) et uniforme α/G_max), monde A′ ; P(au moins une fausse promotion) et nombre moyen de promotions ;
  N  — nuls partiels : taux de fausses découvertes de l'union contre Σ_{i nulle} b_i ; puissance (vraies promues) ;
  S  — D-S24 : arrêt de la course avant G_max sur une règle qui dépend des issues (uniforme α/G_max) ;
  T  — tricherie d'ordre : abandonner **avant** d'ajouter la partie quand elle baisse la valeur (nul complet) ;
  P  — D-S27 : `contraste_plafonne` contre le calcul direct ; bornes.
"""

import json
import math
import os
import sys
import time
import unittest

import numpy as np

DOSSIER = ("/home/claude/canal-conv-audit-n04/brouillons/canal-reprise-releve-v1/envois/"
           "pole-scientifique-automatique-v1/orchestrateur-pole-v7")
sys.path.insert(0, DOSSIER)
sys.dont_write_bytecode = True
from pole import pari_apparie as pa  # noqa: E402

ENTROPIE = 2026102721
ALPHA = 0.05
REP = int(os.environ.get("REP", "2000"))


def rng_de(section, indice):
    return np.random.default_rng(np.random.SeedSequence(ENTROPIE, spawn_key=(section, indice)))


def marche_a_prime(rng, pas, p_haut=0.5):
    """Monde A′ : ×1,5 avec probabilité p_haut, ×0,5 sinon ; martingale si p_haut = 0,5 ; trajectoire du log, cumulée."""
    pas_log = np.where(rng.random(pas) < p_haut, math.log(1.5), math.log(0.5))
    return np.cumsum(pas_log).tolist()


# --- U : essais du dépôt --------------------------------------------------------------------------------------------

def section_U():
    sys.path.insert(0, DOSSIER)
    import importlib
    mod = importlib.import_module("essais.test_v7_pari_apparie")
    suite = unittest.defaultTestLoader.loadTestsFromModule(mod)
    res = unittest.TextTestRunner(stream=open(os.devnull, "w"), verbosity=0).run(suite)
    return {"essais_lances": res.testsRun, "echecs": len(res.failures), "erreurs": len(res.errors),
            "tout_passe": res.wasSuccessful()}


# --- E : ebh_pondere ------------------------------------------------------------------------------------------------

def section_E():
    s = {}
    # ex æquo au bord : trois fiches à b·E = 1/3 exactement, une quatrième en dessous
    b = 0.05 / 4
    log_e = {"a": math.log(1 / (3 * b)), "b": math.log(1 / (3 * b)), "c": math.log(1 / (3 * b)), "d": math.log(1.0)}
    s["ex_aequo_au_bord_trois_a_1_sur_3"] = sorted(pa.ebh_pondere(log_e, {k: b for k in log_e}))
    # ex æquo : deux fiches à 1/2 exactement et une troisième à 1/2 aussi → k* = 3 ? (1/2 ≥ 1/3 oui) ; toutes promues
    log_e2 = {"a": math.log(0.5 / b), "b": math.log(0.5 / b), "c": math.log(0.5 / b)}
    s["trois_a_1_sur_2"] = sorted(pa.ebh_pondere(log_e2, {k: b for k in log_e2}))
    # somme des budgets entre α et 1 : acceptée par ebh_pondere seule (le contrôle ≤ α est dans Course)
    try:
        pa.ebh_pondere({"a": math.log(3.0)}, {"a": 0.5})
        s["somme_0.5_acceptee_par_ebh_pondere_seule"] = True
    except ValueError:
        s["somme_0.5_acceptee_par_ebh_pondere_seule"] = False
    s["course_vide_lire"] = sorted(pa.Course().lire())
    # une seule famille : e-BH ordinaire (tolérance 1e-12 : b·E = (1/k)·e^{-1e-12} est promue)
    k = 2
    log_e3 = {"a": math.log(2.0 / b), "b": -math.log(k) - math.log(b) - 0.5e-12}
    s["tolerance_1e-12_promeut_juste_sous_1_sur_k"] = "b" in pa.ebh_pondere(log_e3, {"a": b, "b": b})
    return s


# --- C : Course, cas limites ----------------------------------------------------------------------------------------

def section_C():
    s = {}
    # (1) abandonnée, gelée en dessous de son seuil, promue plus tard quand k* grandit
    c = pa.Course(alpha=0.05)
    c.entrer("g1", ["a", "b", "c", "d"], 0.04)  # b = 0,01, seuil 100
    c.ajouter_trajectoire("a", [math.log(40)])  # b·E = 0,4 < 1
    c.abandonner("a")
    s["lecture_1_a_seule_a_0.4"] = sorted(c.lire())
    c.ajouter_trajectoire("b", [math.log(100)])  # arrêtée : b·E = 1
    c.ajouter_trajectoire("c", [math.log(100)])
    c.ajouter_trajectoire("d", [math.log(100)])
    s["lecture_2_k_etoile_4_promeut_l_abandonnee_a_0.4"] = sorted(c.lire())
    s["a_abandonnee_promue"] = "a" in c.promues
    # (2) fiche arrêtée puis abandonnée avant lecture : lue à sa valeur gelée ≥ 1/b → promue
    c2 = pa.Course(alpha=0.05)
    c2.entrer("g1", ["a"], 0.05)
    c2.ajouter_trajectoire("a", [math.log(10), math.log(25), math.log(0.1)])  # arrêt à 25 ≥ 20, le reste ignoré
    s["arret_valeur_gelee_log"] = round(c2.log_e["a"], 6)
    s["arret_valeur_attendue_log25"] = round(math.log(25), 6)
    c2.abandonner("a")
    s["arretee_puis_abandonnee_promue_a_la_lecture"] = sorted(c2.lire())
    # (3) ordre : abandonner avant ajouter_trajectoire → la partie est ignorée sans erreur
    c3 = pa.Course(alpha=0.05)
    c3.entrer("g1", ["a"], 0.05)
    c3.ajouter_trajectoire("a", [math.log(15)])
    c3.abandonner("a")
    r = c3.ajouter_trajectoire("a", [math.log(0.01)])
    s["abandon_puis_partie_basse_ignoree_valeur_log"] = round(r, 6)
    s["abandon_puis_partie_basse_ignoree_sans_erreur"] = abs(r - math.log(15)) < 1e-12
    # (4) abandonner une fiche inconnue → KeyError ; lire deux fois de suite → même ensemble, aucune nouvelle
    try:
        c3.abandonner("zz")
        s["abandonner_inconnue"] = "accepté"
    except KeyError:
        s["abandonner_inconnue"] = "KeyError"
    c4 = pa.Course(alpha=0.05)
    c4.entrer("g1", ["a"], 0.05)
    c4.ajouter_trajectoire("a", [math.log(30)])
    s["lire_1"] = sorted(c4.lire())
    s["lire_2_sans_nouvelle_partie"] = sorted(c4.lire())
    s["promues_apres_deux_lectures"] = sorted(c4.promues)
    # (5) promue puis abandonnée : reste promue, valeur inchangée
    c4.abandonner("a")
    s["promue_puis_abandonnee_reste_promue"] = "a" in c4.promues
    # (6) somme des α_c : une famille après abandon de toutes les précédentes n'est pas « rendue »
    c5 = pa.Course(alpha=0.05)
    c5.entrer("g1", ["a", "b"], 0.03)
    c5.abandonner("a")
    c5.abandonner("b")
    try:
        c5.entrer("g2", ["c"], 0.03)
        s["budget_des_abandonnees_rendu"] = True
    except ValueError:
        s["budget_des_abandonnees_rendu"] = False
    # (7) domaine logarithmique : une partie énorme (log 1e300·10) ne déborde pas
    c6 = pa.Course(alpha=0.05)
    c6.entrer("g1", ["a"], 0.05)
    c6.ajouter_trajectoire("a", [3000.0])
    s["log_tres_grand_sans_debordement"] = sorted(c6.lire()) == ["a"] and math.isfinite(c6.log_e["a"])
    return s


# --- H : D-S25 bis, nul complet, familles à budgets différents -----------------------------------------------------

def course_nul_complet(rng, suite, generations, pas, cohorte=4, nouvelles=3, p_haut=0.5, arret_sur_issue=False):
    c = pa.Course(alpha=ALPHA)
    c.entrer("c1", [f"c{i}" for i in range(cohorte)], suite[0])
    nb_gen = 0
    for g in range(generations):
        if g > 0:
            c.entrer(f"g{g + 1}", [f"n{g}-{j}" for j in range(nouvelles)], suite[g])
        for i in range(cohorte):
            c.ajouter_trajectoire(f"c{i}", marche_a_prime(rng, pas, p_haut))
        if g > 0:
            for j in range(nouvelles):
                c.ajouter_trajectoire(f"n{g}-{j}", marche_a_prime(rng, pas, p_haut))
        c.lire()
        nb_gen = g + 1
        if g > 0:
            for j in range(nouvelles):
                c.abandonner(f"n{g}-{j}")
        if arret_sur_issue:
            # règle qui dépend des issues : on arrête la course dès qu'une promotion existe, ou dès que la cohorte
            # entière est au-dessous de 1/10 de sa valeur de départ (log < −log 10)
            if c.promues or all(c.log_e[f"c{i}"] < -math.log(10) for i in range(cohorte)):
                break
    return c, nb_gen


def section_H(rep):
    s = {}
    G = 10
    suites = {"6/(pi2g2)": [ALPHA * 6 / (math.pi ** 2 * g * g) for g in range(1, G + 1)],
              "uniforme_alpha_sur_G_max=10": [ALPHA / G] * G}
    for nom, suite in suites.items():
        for pas in (20, 200):
            rng = rng_de(1, pas + (0 if nom.startswith("6") else 1))
            au_moins_une = 0
            nb_promues = 0
            for _ in range(rep):
                c, _ = course_nul_complet(rng, suite, G, pas)
                au_moins_une += bool(c.promues)
                nb_promues += len(c.promues)
            s[f"{nom}_A_prime_{pas}_pas"] = {"repetitions": rep, "somme_alpha_c": round(sum(suite), 5),
                                            "P(au_moins_une_fausse_promotion)": au_moins_une / rep,
                                            "nombre_moyen_de_fausses_promotions": nb_promues / rep}
    return s


# --- N : nuls partiels, taux de fausses découvertes de l'union -----------------------------------------------------

def section_N(rep):
    s = {}
    G, pas = 10, 20
    suite = [ALPHA * 6 / (math.pi ** 2 * g * g) for g in range(1, G + 1)]
    rng = rng_de(2, 0)
    fdp, vraies, au_moins_une = 0.0, 0, 0
    budgets_nulles = None
    for _ in range(rep):
        c = pa.Course(alpha=ALPHA)
        # cohorte : 2 vraies (p_haut = 0,7 : E[facteur] = 1,2) + 2 nulles ; nouvelles : 1 vraie + 2 nulles
        c.entrer("c1", ["v0", "v1", "z0", "z1"], suite[0])
        nulles = {"z0", "z1"}
        for g in range(G):
            if g > 0:
                c.entrer(f"g{g + 1}", [f"v{g}-0", f"z{g}-1", f"z{g}-2"], suite[g])
                nulles |= {f"z{g}-1", f"z{g}-2"}
            for f in ("v0", "v1"):
                c.ajouter_trajectoire(f, marche_a_prime(rng, pas, 0.7))
            for f in ("z0", "z1"):
                c.ajouter_trajectoire(f, marche_a_prime(rng, pas, 0.5))
            if g > 0:
                c.ajouter_trajectoire(f"v{g}-0", marche_a_prime(rng, pas, 0.7))
                for f in (f"z{g}-1", f"z{g}-2"):
                    c.ajouter_trajectoire(f, marche_a_prime(rng, pas, 0.5))
            c.lire()
            if g > 0:
                for f in (f"v{g}-0", f"z{g}-1", f"z{g}-2"):
                    c.abandonner(f)
        if budgets_nulles is None:
            budgets_nulles = sum(c.budgets[f] for f in nulles)
        fausses = len(c.promues & nulles)
        fdp += fausses / max(1, len(c.promues))
        au_moins_une += fausses > 0
        vraies += len(c.promues - nulles)
    s["nuls_partiels_A_prime_20_pas"] = {"repetitions": rep, "borne_somme_budgets_des_nulles": round(budgets_nulles, 5),
                                         "taux_de_fausses_decouvertes_de_l_union": fdp / rep,
                                         "P(au_moins_une_fausse_promotion)": au_moins_une / rep,
                                         "vraies_promues_moyenne_sur_11": vraies / rep}
    return s


# --- S : D-S24, arrêt avant G_max sur une règle qui dépend des issues ----------------------------------------------

def section_S(rep):
    G = 10
    suite = [ALPHA / G] * G
    rng = rng_de(3, 0)
    au_moins_une, gens = 0, 0
    for _ in range(rep):
        c, nb = course_nul_complet(rng, suite, G, 20, arret_sur_issue=True)
        au_moins_une += bool(c.promues)
        gens += nb
    return {"uniforme_G_max=10_arret_sur_issue_A_prime_20_pas": {"repetitions": rep,
                                                                 "P(au_moins_une_fausse_promotion)": au_moins_une / rep,
                                                                 "generations_faites_en_moyenne": gens / rep}}


# --- T : tricherie d'ordre (abandonner avant d'ajouter la partie qui baisse) ---------------------------------------

def section_T(rep):
    s = {}
    G, pas = 10, 20
    for ordre in ("juste", "abandon_avant_partie_basse"):
        rng = rng_de(4, 0 if ordre == "juste" else 1)
        au_moins_une = 0
        for _ in range(rep):
            c = pa.Course(alpha=ALPHA)
            c.entrer("c1", ["a"], ALPHA)  # une fiche, seuil 20
            for g in range(G):
                traj = marche_a_prime(rng, pas)
                if ordre == "abandon_avant_partie_basse" and traj[-1] < 0 and "a" not in c.gelees:
                    c.abandonner("a")       # on « décide » d'abandonner en ayant vu la partie, avant de l'ajouter
                c.ajouter_trajectoire("a", traj)  # ignorée si gelée
                c.lire()
            au_moins_une += bool(c.promues)
        s[ordre] = {"repetitions": rep, "P(fausse_promotion)": au_moins_une / rep}
    return s


# --- P : D-S27 ------------------------------------------------------------------------------------------------------

def section_P():
    s = {}
    rng = rng_de(5, 0)
    ecarts = 0.0
    pire = 0.0
    for _ in range(2000):
        m_t, m_max = int(rng.integers(0, 200)), int(rng.integers(1, 100))
        rA, rB = float(rng.random()), float(rng.random())
        v = pa.contraste({"A": rA, "B": rB}, {"A": 1, "B": -1})
        vp = pa.contraste_plafonne({"A": rA, "B": rB}, {"A": 1, "B": -1}, 0.0, m_t, m_max)
        attendu = min(m_t, m_max) / m_max * v
        ecarts = max(ecarts, abs(vp - attendu))
        pire = max(pire, abs(vp))
    s["ecart_max_contre_calcul_direct"] = ecarts
    s["max_abs_v_prime_sur_2000_tirages"] = pire
    s["m_t=0_poids"] = pa.ponderation_plafonnee(0, 20)
    return s


def main():
    debut = time.time()
    sortie = {"manifeste": {"script": "contre-verification-pari-signe-v6.py", "entropie_SeedSequence": ENTROPIE,
                            "derivation": "SeedSequence(ENTROPIE, spawn_key=(section, indice))",
                            "codes_sections": {"H": 1, "N": 2, "S": 3, "T": 4, "P": 5}, "repetitions": REP,
                            "python": sys.version.split()[0], "numpy": np.__version__, "alpha": ALPHA,
                            "module_teste": os.path.join(DOSSIER, "pole/pari_apparie.py")}}
    sortie["U_essais_du_depot"] = section_U()
    sortie["E_ebh_pondere"] = section_E()
    sortie["C_course_cas_limites"] = section_C()
    sortie["H_nul_complet_familles_a_budgets_differents"] = section_H(REP)
    sortie["N_nuls_partiels"] = section_N(REP)
    sortie["S_arret_avant_G_max_sur_issue"] = section_S(REP)
    sortie["T_tricherie_d_ordre"] = section_T(REP)
    sortie["P_plafond"] = section_P()
    sortie["manifeste"]["duree_secondes"] = round(time.time() - debut, 1)
    json.dump(sortie, sys.stdout, ensure_ascii=False, indent=1)
    print()


if __name__ == "__main__":
    main()
