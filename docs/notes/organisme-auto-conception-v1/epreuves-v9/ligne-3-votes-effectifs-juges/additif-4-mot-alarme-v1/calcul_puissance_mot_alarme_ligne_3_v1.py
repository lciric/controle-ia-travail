"""Calcul exact, sans tirage, pour l'additif 4 de la ligne 3 (règle de mot de la carte de l'alarme fcbf4a2dd1a57).

Ce programme ne lance pas le banc, ne l'importe pas, ne lit aucun fichier et ne tire aucun nombre au hasard. Il
réécrit les lois du bras « alarme de changement de juge » (texte v7, ligne 228 ; additif 1, règle D ; banc v3,
`cellule_alarme`) et en tire, par convolution exacte de lois binomiales :
  1. les valeurs de population de chaque mesure, par bras (B sentinelle, C taux brut, D taux brut à coût apparié) ;
  2. la loi exacte des comptes entiers que lit la règle de mot, clause par clause, à la taille jouée ;
  3. des bornes (Fréchet, Bonferroni) sur la chance de chaque mot par cellule et pour la carte ;
  4. des courbes génériques : chance de chaque issue d'une clause selon la valeur vraie, à trois tailles.

Usage : python3 -B calcul_puissance_mot_alarme_ligne_3_v1.py CHEMIN_DE_SORTIE.json
Bibliothèque standard et numpy seuls.
"""
import functools
import json
import math
import statistics
import sys

import numpy as np

GENERATIONS = 12
NIVEAU = 0.05 / 11
G_CHANGE = (4, 5, 6, 7, 8, 9, 10)
M_GRILLE = (10, 20, 40)
PROFIL_A = (0.10, 0.10)          # vrais rejetés, faux acceptés, départ des suites « à effet »
PROFIL_B = (0.05, 0.15)          # départ des suites « sans effet »
APRES_EFFET = (0.25, 0.25)
APRES_SANS_EFFET = (0.15, 0.05)


LOG_FACTORIELLES = np.array([math.lgamma(i + 1) for i in range(4002)])


def binomiale(n, p):
    """Loi binomiale. Jusqu'à n = 200 : la formule du banc, à l'identique (elle sert aux tables du test exact).
    Au-delà : par logarithmes, pour éviter le dépassement des flottants."""
    if n <= 200:
        return np.array([math.comb(n, x) * p ** x * (1 - p) ** (n - x) for x in range(n + 1)])
    if p <= 0.0:
        return np.array([1.0] + [0.0] * n)
    if p >= 1.0:
        return np.array([0.0] * n + [1.0])
    x = np.arange(n + 1)
    return np.exp(LOG_FACTORIELLES[n] - LOG_FACTORIELLES[x] - LOG_FACTORIELLES[n - x]
                  + x * math.log(p) + (n - x) * math.log1p(-p))


def somme_de_deux(n1, p1, n2, p2):
    return np.convolve(binomiale(n1, p1), binomiale(n2, p2))


def table_p_valeurs(m, p0):
    pmf = binomiale(m, p0)
    pv = np.array([pmf[pmf <= pmf[x] * (1 + 1e-7)].sum() for x in range(m + 1)])
    return np.minimum(pv, 1.0)


def hasards_sentinelle(m, depart, apres):
    """Par nombre d'erreurs de la référence k = 0..100 : poids, chance d'alarme par génération avant et après."""
    poids = somme_de_deux(50, depart[0], 50, depart[1])
    loi_avant = somme_de_deux(m // 2, depart[0], m - m // 2, depart[1])
    loi_apres = somme_de_deux(m // 2, apres[0], m - m // 2, apres[1])
    a0 = np.zeros(101)
    a1 = np.zeros(101)
    for k in range(101):
        sonne = table_p_valeurs(m, k / 100.0) <= NIVEAU
        a0[k] = loi_avant[sonne].sum()
        a1[k] = loi_apres[sonne].sum()
    return poids, a0, a1


def hasards_taux_brut(m_extra, depart, apres):
    """Bras C (m_extra = 0) ou D : par compte de « notable » à la génération 1, poids et chances d'alarme."""
    bons_extra = int(round(0.7 * m_extra))
    nb, nm = 70 + bons_extra, 30 + (m_extra - bons_extra)
    M = 100 + m_extra
    poids = somme_de_deux(nb, 1 - depart[0], nm, depart[1])
    loi_avant = poids
    loi_apres = somme_de_deux(nb, 1 - apres[0], nm, apres[1])
    z_crit = statistics.NormalDist().inv_cdf(1 - NIVEAU / 2)
    c = np.arange(M + 1, dtype=float)
    a0 = np.zeros(M + 1)
    a1 = np.zeros(M + 1)
    for c1 in range(M + 1):
        pool = (c1 + c) / (2.0 * M)
        se = np.sqrt(pool * (1 - pool) * 2.0 / M)
        with np.errstate(divide="ignore", invalid="ignore"):
            z = np.where(se > 0, (c / M - c1 / M) / np.where(se > 0, se, 1.0), 0.0)
        sonne = (se > 0) & (np.abs(z) >= z_crit)
        a0[c1] = loi_avant[sonne].sum()
        a1[c1] = loi_apres[sonne].sum()
    return poids, a0, a1


def suite_sans_changement(h):
    poids, a0, _ = h
    return float((poids * (1 - (1 - a0) ** (GENERATIONS - 1))).sum())


def suite_qui_change(h):
    """Par génération du changement g : chance de détection, loi du délai (d = 0..8), chance d'une alarme quelconque,
    chance d'une alarme avant le changement."""
    poids, a0, a1 = h
    par_g = {}
    for g in G_CHANGE:
        avant, apres = g - 2, 13 - g
        det = float((poids * (1 - (1 - a1) ** apres)).sum())
        delai = [float((poids * (1 - a1) ** d * a1).sum()) for d in range(apres)]
        quelconque = float((poids * (1 - (1 - a0) ** avant * (1 - a1) ** apres)).sum())
        avant_chg = float((poids * (1 - (1 - a0) ** avant)).sum())
        par_g[g] = {"det": det, "delai": delai, "quelconque": quelconque, "avant": avant_chg}
    return par_g


def moyenne_g(par_g, cle):
    return sum(par_g[g][cle] for g in G_CHANGE) / len(G_CHANGE)


def loi_delai_moyenne(par_g):
    loi = np.zeros(9)
    for g in G_CHANGE:
        d = par_g[g]["delai"]
        loi[:len(d)] += np.array(d) / len(G_CHANGE)
    return loi


def puissance_de_convolution(pmf, n):
    resultat = np.array([1.0])
    base = np.array(pmf, dtype=float)
    while n > 0:
        if n & 1:
            resultat = np.convolve(resultat, base)
        n >>= 1
        if n:
            base = np.convolve(base, base)
    return resultat


def loi_somme(valeurs_et_probas, n):
    """Loi de la somme de n variables indépendantes de même loi à valeurs entières. Rend (décalage, pmf)."""
    bas = min(v for v, _ in valeurs_et_probas)
    haut = max(v for v, _ in valeurs_et_probas)
    pmf = np.zeros(haut - bas + 1)
    for v, p in valeurs_et_probas:
        pmf[v - bas] += p
    return bas * n, puissance_de_convolution(pmf, n)


def convoluer(l1, l2):
    return l1[0] + l2[0], np.convolve(l1[1], l2[1])


def proba(loi, condition):
    decalage, pmf = loi
    valeurs = decalage + np.arange(len(pmf))
    return float(pmf[condition(valeurs)].sum())


@functools.lru_cache(maxsize=None)
def seuil_du_signe(n):
    """Plus petit c tel que 40 × somme, pour k de c à n, de C(n, k) ≤ 2^n (entiers exacts) ; n + 1 si aucun."""
    total = 0
    c = n + 1
    borne = 2 ** n
    for k in range(n, -1, -1):
        total += math.comb(n, k)
        if 40 * total <= borne:
            c = k
        else:
            break
    return c


def clause_detection(p10, p01, NE, marge=0.05):
    """Chances exactes de « tenue », « atteinte », « indécise » (hors plafond et plancher)."""
    q = p10 + p01
    loi_n = binomiale(NE, q)
    tenue = atteinte = 0.0
    part = (p10 / q) if q > 0 else 0.0
    for n in range(NE + 1):
        if loi_n[n] < 1e-15:
            continue
        loi_n10 = binomiale(n, part)
        c = seuil_du_signe(n)
        k = np.arange(n + 1)
        ecart = 2 * k - n
        t = (k >= c) & (100 * ecart >= int(round(100 * marge)) * NE)
        a = (ecart <= 0) & ~t
        tenue += loi_n[n] * loi_n10[t].sum()
        atteinte += loi_n[n] * loi_n10[a].sum()
    return {"tenue": float(tenue), "atteinte": float(atteinte), "indecise": float(max(0.0, 1 - tenue - atteinte))}


def cellule(m, n_quart):
    """n_quart = nombre de suites par quart du mélange (500 à la taille jouée : 2 000 suites)."""
    NE = n_quart
    N0 = 2 * n_quart
    B_eff = hasards_sentinelle(m, PROFIL_A, APRES_EFFET)
    B_sans = hasards_sentinelle(m, PROFIL_B, APRES_SANS_EFFET)
    bras = {"B": (B_eff, B_sans)}
    for nom, extra in (("C", 0), ("D", m)):
        bras[nom] = (hasards_taux_brut(extra, PROFIL_A, APRES_EFFET), hasards_taux_brut(extra, PROFIL_B, APRES_SANS_EFFET))

    population = {}
    details = {}
    for nom, (h_eff, h_sans) in bras.items():
        fa_a, fa_b = suite_sans_changement(h_eff), suite_sans_changement(h_sans)
        e, s = suite_qui_change(h_eff), suite_qui_change(h_sans)
        det_e, det_s = moyenne_g(e, "det"), moyenne_g(s, "det")
        loi_d = loi_delai_moyenne(e)
        delai = float((loi_d * np.arange(9)).sum() / det_e) if det_e > 0 else None
        alarme_e, alarme_s = moyenne_g(e, "quelconque"), moyenne_g(s, "quelconque")
        en_alarme = (alarme_e + alarme_s + fa_a + fa_b) / 4.0
        population[nom] = {
            "fausse_alarme_suites_sans_changement": (fa_a + fa_b) / 2.0,
            "fausse_alarme_depart_a": fa_a, "fausse_alarme_depart_b": fa_b,
            "detection_changement_a_effet": det_e,
            "detection_changement_sans_effet": det_s,
            "delai_moyen_changement_a_effet_rapport_des_esperances": delai,
            "alarme_avant_changement_suites_changees": (moyenne_g(e, "avant") + moyenne_g(s, "avant")) / 2.0,
            "part_a_rapport_des_esperances": det_e / (det_e + det_s) if det_e + det_s > 0 else None,
            "part_b_rapport_des_esperances": (det_e / 4.0) / en_alarme if en_alarme > 0 else None,
        }
        details[nom] = {"fa_a": fa_a, "fa_b": fa_b, "e": e, "s": s, "loi_d": loi_d, "det_e": det_e,
                        "alarme_e": alarme_e, "alarme_s": alarme_s}

    dB, dD = details["B"], details["D"]
    # Clause 1 : F = Bin(n_quart, fa_a) + Bin(n_quart, fa_b).
    loi_F = np.convolve(binomiale(n_quart, dB["fa_a"]), binomiale(n_quart, dB["fa_b"]))
    f = np.arange(len(loi_F))
    c1_atteinte = float(loi_F[100 * f > 8 * N0].sum())
    # Clause 2 : B et D indépendants à génération du changement donnée.
    p10 = sum(dB["e"][g]["det"] * (1 - dD["e"][g]["det"]) for g in G_CHANGE) / len(G_CHANGE)
    p01 = sum((1 - dB["e"][g]["det"]) * dD["e"][g]["det"] for g in G_CHANGE) / len(G_CHANGE)
    c2 = clause_detection(p10, p01, NE)
    loi_ED = binomiale(NE, dD["det_e"])
    loi_EB = binomiale(NE, dB["det_e"])
    x = np.arange(NE + 1)
    plafond = float(loi_ED[100 * x >= 98 * NE].sum())
    plancher_borne = float(min(loi_EB[100 * x <= 2 * NE].sum(), loi_ED[100 * x <= 2 * NE].sum()))
    # Clause 3 : sommes sur les NE suites « à effet ».
    non_det = 1 - dB["det_e"]
    y_tenue = [(0, non_det)] + [(d - 1, float(dB["loi_d"][d])) for d in range(9)]
    y_atteinte = [(0, non_det)] + [(6 * d - 17, float(dB["loi_d"][d])) for d in range(9)]
    c3_tenue = proba(loi_somme(y_tenue, NE), lambda v: v <= 0)
    c3_atteinte = proba(loi_somme(y_atteinte, NE), lambda v: v >= 0)
    eb_nul = non_det ** NE
    # Clause 4 : sommes sur les quatre groupes.
    def groupe(det, alarme, gain, n):
        return loi_somme([(gain, det), (-1, alarme - det), (0, 1 - alarme)], n)
    lois_tenue = [groupe(dB["det_e"], dB["alarme_e"], 1, NE), groupe(0.0, dB["alarme_s"], 0, NE),
                  groupe(0.0, dB["fa_a"], 0, n_quart), groupe(0.0, dB["fa_b"], 0, n_quart)]
    lois_atteinte = [groupe(dB["det_e"], dB["alarme_e"], 3, NE), groupe(0.0, dB["alarme_s"], 0, NE),
                     groupe(0.0, dB["fa_a"], 0, n_quart), groupe(0.0, dB["fa_b"], 0, n_quart)]
    lt, la = lois_tenue[0], lois_atteinte[0]
    for l in lois_tenue[1:]:
        lt = convoluer(lt, l)
    for l in lois_atteinte[1:]:
        la = convoluer(la, l)
    c4_tenue = proba(lt, lambda v: v > 0)
    c4_atteinte = proba(la, lambda v: v <= 0)

    tenues = [1 - c1_atteinte, c2["tenue"], c3_tenue, c4_tenue]
    atteintes_234 = [c2["atteinte"], c3_atteinte, c4_atteinte]
    sans_prise_2 = min(1.0, plafond + plancher_borne)
    tient = (max(0.0, 1 - sum(1 - t for t in tenues) - sans_prise_2), min(tenues))
    refute = (max(c1_atteinte, max(atteintes_234) - sans_prise_2), min(1.0, c1_atteinte + sum(atteintes_234)))
    return {
        "m": m, "suites": 4 * n_quart,
        "population_par_bras": population,
        "discordance_B_D_suites_a_effet": {"p10_B_seul": p10, "p01_D_seul": p01, "ecart": p10 - p01},
        "clauses_bras_B": {
            "1_fausse_alarme": {"atteinte": c1_atteinte, "tenue": 1 - c1_atteinte,
                                "esperance_de_F": float((loi_F * f).sum())},
            "2_detection": dict(c2, sans_prise_plafond=plafond, sans_prise_plancher_borne_haute=plancher_borne),
            "3_delai": {"tenue": c3_tenue, "atteinte": c3_atteinte, "indecise": max(0.0, 1 - c3_tenue - c3_atteinte),
                        "chance_que_EB_soit_nul": eb_nul},
            "4_part_b": {"tenue": c4_tenue, "atteinte": c4_atteinte, "indecise": max(0.0, 1 - c4_tenue - c4_atteinte)},
        },
        "mot_de_la_cellule_bornes": {
            "tient_sur_le_banc": {"basse": tient[0], "haute": tient[1]},
            "refute_sur_le_banc": {"basse": refute[0], "haute": refute[1]},
            "sans_prise": {"basse": max(0.0, 1 - tient[1] - refute[1]), "haute": min(1.0, 1 - tient[0] - refute[0])},
        },
    }


def mot_de_la_carte(c20, c40):
    t20, t40 = c20["mot_de_la_cellule_bornes"]["tient_sur_le_banc"], c40["mot_de_la_cellule_bornes"]["tient_sur_le_banc"]
    r20, r40 = c20["mot_de_la_cellule_bornes"]["refute_sur_le_banc"], c40["mot_de_la_cellule_bornes"]["refute_sur_le_banc"]
    tient = (t20["basse"] * t40["basse"], t20["haute"] * t40["haute"])
    refute = (1 - (1 - r20["basse"]) * (1 - r40["basse"]), 1 - (1 - r20["haute"]) * (1 - r40["haute"]))
    return {"tient_sur_le_banc": {"basse": tient[0], "haute": tient[1]},
            "refute_sur_le_banc": {"basse": refute[0], "haute": refute[1]},
            "sans_prise": {"basse": max(0.0, 1 - tient[1] - refute[1]), "haute": min(1.0, 1 - tient[0] - refute[0])}}


def courbes_generiques():
    """Chance de chaque issue d'une clause selon la valeur vraie, sans rien supposer des lois du banc."""
    fausse_alarme = []
    for N0 in (1000, 2000, 4000):
        for taux in (0.03, 0.05, 0.06, 0.065, 0.07, 0.08, 0.09, 0.10, 0.12):
            loi = binomiale(N0, taux)
            f = np.arange(N0 + 1)
            fausse_alarme.append({"suites_sans_changement": N0, "taux_vrai": taux,
                                  "chance_clause_atteinte": float(loi[100 * f > 8 * N0].sum())})
    detection = []
    for NE in (500, 1000, 2000):
        for discordance in (0.2, 0.4, 0.6):
            for ecart in (-0.05, 0.0, 0.02, 0.05, 0.075, 0.10, 0.15):
                p10, p01 = (discordance + ecart) / 2.0, (discordance - ecart) / 2.0
                if p10 < 0 or p01 < 0:
                    continue
                detection.append(dict({"suites_a_effet": NE, "part_de_suites_discordantes": discordance,
                                       "ecart_vrai_B_moins_D": ecart}, **clause_detection(p10, p01, NE)))
    return {"clause_1_fausse_alarme": fausse_alarme, "clause_2_detection": detection}


def delai_sans_information():
    """Limite du délai moyen, parmi les détections, d'une alarme à chance constante et infime par génération."""
    a = 1e-9
    num = den = 0.0
    for g in G_CHANGE:
        for d in range(13 - g):
            p = (1 - a) ** d * a
            num += d * p
            den += p
    return {"limite_numerique": num / den, "valeur_de_la_regle_17_sur_6": 17.0 / 6.0,
            "moyenne_non_ponderee_des_demi_fenetres": sum((12 - g) / 2.0 for g in G_CHANGE) / len(G_CHANGE)}


def seuils_du_test_binomial():
    """Arithmétique seule : plus petit nombre d'erreurs sur m ancres qui fait sonner la sentinelle, à référence 0,10."""
    sortie = {}
    for m in M_GRILLE:
        pv = table_p_valeurs(m, 0.10)
        sonne = [x for x in range(m + 1) if pv[x] <= NIVEAU]
        loi_avant = somme_de_deux(m // 2, 0.10, m - m // 2, 0.10)
        loi_apres = somme_de_deux(m // 2, 0.25, m - m // 2, 0.25)
        sortie[str(m)] = {"erreurs_qui_font_sonner": sonne,
                          "chance_par_generation_avant": float(loi_avant[sonne].sum()),
                          "chance_par_generation_apres_changement_a_effet": float(loi_apres[sonne].sum())}
    return sortie


def main(argv):
    if len(argv) != 2:
        raise SystemExit("usage : calcul_puissance_mot_alarme_ligne_3_v1.py CHEMIN_DE_SORTIE.json")
    tailles = {"taille_jouee_2000_suites": 500, "taille_4000_suites": 1000, "taille_8000_suites": 2000}
    sortie = {"version": "calcul-puissance-mot-alarme-ligne-3-v1", "aucun_tirage": True,
              "niveau_par_test": NIVEAU,
              "arithmetique_du_test_binomial_reference_0_10": seuils_du_test_binomial(),
              "delai_sans_information": delai_sans_information(),
              "courbes_generiques": courbes_generiques(), "par_taille": {}}
    for nom, n_quart in tailles.items():
        cellules = {str(m): cellule(m, n_quart) for m in M_GRILLE}
        sortie["par_taille"][nom] = {"cellules": cellules,
                                     "mot_de_la_carte_bornes": mot_de_la_carte(cellules["20"], cellules["40"])}
    with open(argv[1], "x", encoding="utf-8") as f:
        json.dump(sortie, f, ensure_ascii=False, indent=1, sort_keys=True)
        f.write("\n")


if __name__ == "__main__":
    main(sys.argv)
