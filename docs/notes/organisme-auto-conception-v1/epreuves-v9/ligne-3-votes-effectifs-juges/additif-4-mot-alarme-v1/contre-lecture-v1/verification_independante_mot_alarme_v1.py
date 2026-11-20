"""Contre-lecture de l'additif 4 de la ligne 3 (mot de la carte de l'alarme) : calcul indépendant — v1.

Contre-lecteur neuf, modèle O. Ce programme ne lance ni n'importe le banc v3. Il réécrit, depuis la lecture de
`cellule_alarme` (banc v3, lignes 1287 à 1342), les lois du bras de l'alarme, par deux voies distinctes de celles
du rédacteur :
  1. une voie exacte (lois binomiales de scipy, p-valeurs recodées) pour les valeurs de population ;
  2. une simulation directe de la mécanique du banc (référence, ancres, production, cartes de plus, tests), par
     passages entiers de 2 000 suites, à laquelle la règle de mot du § 2 est appliquée sur comptes entiers.
Il ajoute des bornes de Chernoff (voie sans convolution) pour la clause du délai, et des points des courbes
génériques. En fin, il compare aux valeurs de la sortie du rédacteur (fichier lu en argument, données seules).

Graines de la simulation : SeedSequence(551177, spawn_key=(1,)), racine de contre-lecture, hors de toute racine du
projet ; un enfant par cellule m.

Usage : python3 -B verification_independante_mot_alarme_v1.py SORTIE_DU_REDACTEUR.json CHEMIN_DE_SORTIE.json PASSAGES
"""
import functools
import json
import math
import sys
from fractions import Fraction

import numpy as np
from scipy import stats

G = 12
NIV = 0.05 / 11
GCH = list(range(4, 11))
MS = (10, 20, 40)
ZC = float(stats.norm.ppf(1 - NIV / 2))
# (vr0, fa0, vr1, fa1) par groupe
EFFET = (0.10, 0.10, 0.25, 0.25)
SANS_EFFET = (0.05, 0.15, 0.15, 0.05)


def pmf(n, p):
    return stats.binom.pmf(np.arange(n + 1), n, p)


def somme(n1, p1, n2, p2):
    return np.convolve(pmf(n1, p1), pmf(n2, p2))


def pvaleurs(m, p0):
    f = pmf(m, p0)
    return np.array([min(1.0, f[f <= f[x] * (1 + 1e-7)].sum()) for x in range(m + 1)])


# ------------------------------------------------------------------ voie exacte
def hasard_B(m, grp):
    vr0, fa0, vr1, fa1 = grp
    ref = somme(50, vr0, 50, fa0)
    av = somme(m // 2, vr0, m - m // 2, fa0)
    ap = somme(m // 2, vr1, m - m // 2, fa1)
    a0 = np.empty(101)
    a1 = np.empty(101)
    for k in range(101):
        s = pvaleurs(m, k / 100.0) <= NIV
        a0[k] = av[s].sum()
        a1[k] = ap[s].sum()
    return ref, a0, a1


def hasard_D(extra_m, grp):
    vr0, fa0, vr1, fa1 = grp
    be = int(round(0.7 * extra_m))
    nb, nm = 70 + be, 30 + extra_m - be
    M = 100 + extra_m
    av = somme(nb, 1 - vr0, nm, fa0)
    ap = somme(nb, 1 - vr1, nm, fa1)
    c = np.arange(M + 1)
    a0 = np.empty(M + 1)
    a1 = np.empty(M + 1)
    for c1 in range(M + 1):
        pool = (c1 + c) / (2.0 * M)
        se = np.sqrt(pool * (1 - pool) * 2.0 / M)
        z = np.zeros(M + 1)
        ok = se > 0
        z[ok] = (c[ok] / M - c1 / M) / se[ok]
        s = ok & (np.abs(z) >= ZC)
        a0[c1] = av[s].sum()
        a1[c1] = ap[s].sum()
    return av, a0, a1


def population(h):
    w, a0, a1 = h
    fa = float((w * (1 - (1 - a0) ** 11)).sum())
    det = 0.0
    dsum = 0.0
    alarme = 0.0
    loi_d = np.zeros(9)
    for g in GCH:
        n_ap = 13 - g
        det += float((w * (1 - (1 - a1) ** n_ap)).sum()) / 7
        for d in range(n_ap):
            p = float((w * (1 - a1) ** d * a1).sum()) / 7
            loi_d[d] += p
            dsum += d * p
        alarme += float((w * (1 - (1 - a0) ** (g - 2) * (1 - a1) ** n_ap)).sum()) / 7
    return {"fa": fa, "det": det, "delai": dsum / det if det > 0 else None, "alarme_suite_qui_change": alarme,
            "loi_delai": loi_d}


def chernoff_somme_le_zero(valeurs_probas, n):
    """Borne P(somme de n tirages <= 0) <= min_t E[exp(-t Y)]^n, t >= 0 (Chernoff)."""
    meilleur = 0.0
    for t in np.linspace(0.0, 5.0, 5001)[1:]:
        e = sum(p * math.exp(-t * v) for v, p in valeurs_probas)
        meilleur = min(meilleur, n * math.log(e))
    return math.exp(meilleur)


def chernoff_somme_ge_zero(valeurs_probas, n):
    meilleur = 0.0
    for t in np.linspace(0.0, 5.0, 5001)[1:]:
        e = sum(p * math.exp(t * v) for v, p in valeurs_probas)
        meilleur = min(meilleur, n * math.log(e))
    return math.exp(meilleur)


def voie_exacte():
    sortie = {}
    for m in MS:
        bE, bS = hasard_B(m, EFFET), hasard_B(m, SANS_EFFET)
        dE, dS = hasard_D(m, EFFET), hasard_D(m, SANS_EFFET)
        pbE, pbS, pdE, pdS = population(bE), population(bS), population(dE), population(dS)
        fa_B = (pbE["fa"] + pbS["fa"]) / 2
        en_alarme = (pbE["alarme_suite_qui_change"] + pbS["alarme_suite_qui_change"] + pbE["fa"] + pbS["fa"]) / 4
        part_b = (pbE["det"] / 4) / en_alarme
        # Clause 1 exacte : F = Bin(500, fa_A) + Bin(500, fa_B) ; et à 1 000 + 1 000.
        lf = np.convolve(pmf(500, pbE["fa"]), pmf(500, pbS["fa"]))
        c1_2000 = float(lf[np.arange(len(lf)) * 100 > 8 * 1000].sum())
        lf4 = np.convolve(pmf(1000, pbE["fa"]), pmf(1000, pbS["fa"]))
        c1_4000 = float(lf4[np.arange(len(lf4)) * 100 > 8 * 2000].sum())
        moyF = 500 * (pbE["fa"] + pbS["fa"])
        varF = 500 * (pbE["fa"] * (1 - pbE["fa"]) + pbS["fa"] * (1 - pbS["fa"]))
        # Clause 3 par Chernoff (NE = 500) : S <= EB  <=>  somme (d - 1) <= 0 ; 6 S >= 17 EB <=> somme (6 d - 17) >= 0.
        nd = 1 - pbE["det"]
        y_t = [(0, nd)] + [(d - 1, float(pbE["loi_delai"][d])) for d in range(9)]
        y_a = [(0, nd)] + [(6 * d - 17, float(pbE["loi_delai"][d])) for d in range(9)]
        c3_tenue_borne = chernoff_somme_le_zero(y_t, 500)
        c3_atteinte_borne = chernoff_somme_ge_zero(y_a, 500)
        sortie[str(m)] = {
            "B": {"fausse_alarme": fa_B, "fausse_alarme_depart_effet": pbE["fa"],
                  "fausse_alarme_depart_sans_effet": pbS["fa"], "detection_a_effet": pbE["det"],
                  "detection_sans_effet": pbS["det"], "delai_moyen_a_effet": pbE["delai"], "part_b": part_b},
            "D": {"fausse_alarme": (pdE["fa"] + pdS["fa"]) / 2, "detection_a_effet": pdE["det"],
                  "detection_sans_effet": pdS["det"]},
            "clause_1_atteinte_exacte_2000_suites": c1_2000,
            "clause_1_atteinte_exacte_4000_suites": c1_4000,
            "F_moyenne": moyF, "F_ecart_type": math.sqrt(varF),
            "borne_chernoff_clause_3_tenue_2000_suites": c3_tenue_borne,
            "borne_chernoff_clause_3_atteinte_2000_suites": c3_atteinte_borne,
        }
        # Fourchettes de l'audit : moyenne +- 4 écarts types, arrondies vers l'extérieur.
        eb_m, eb_s = 500 * pbE["det"], math.sqrt(500 * pbE["det"] * (1 - pbE["det"]))
        ed_m, ed_s = 500 * pdE["det"], math.sqrt(500 * pdE["det"] * (1 - pdE["det"]))
        sortie[str(m)]["fourchettes_audit"] = {
            "F": [max(0, math.floor(moyF - 4 * math.sqrt(varF))), math.ceil(moyF + 4 * math.sqrt(varF))],
            "EB": [max(0, math.floor(eb_m - 4 * eb_s)), math.ceil(eb_m + 4 * eb_s)],
            "ED": [max(0, math.floor(ed_m - 4 * ed_s)), math.ceil(ed_m + 4 * ed_s)]}
        # Référence connue 0,10 : fausse alarme par départ.
        s = pvaleurs(m, 0.10) <= NIV
        connue = {}
        for nom, grp in (("depart_effet", EFFET), ("depart_sans_effet", SANS_EFFET)):
            av = somme(m // 2, grp[0], m - m // 2, grp[1])
            a = float(av[s].sum())
            connue[nom] = {"chance_par_test": a, "fausse_alarme_suite": 1 - (1 - a) ** 11}
        sortie[str(m)]["reference_connue_0_10"] = connue
    return sortie


# ------------------------------------------------------------------ simulation directe
def tirer_groupe(rng, P, n, m, grp, change, tables):
    vr0, fa0, vr1, fa1 = grp
    gens = np.arange(1, G + 1)
    if change:
        g = rng.integers(4, 11, size=(P, n))
        apres = gens[None, None, :] >= g[:, :, None]
    else:
        g = np.full((P, n), 99)
        apres = np.zeros((P, n, G), dtype=bool)
    vr = np.where(apres, vr1, vr0)
    fa = np.where(apres, fa1, fa0)
    k = rng.binomial(50, vr0, size=(P, n)) + rng.binomial(50, fa0, size=(P, n))
    anc = rng.binomial(m // 2, vr) + rng.binomial(m - m // 2, fa)
    prod = rng.binomial(70, 1 - vr) + rng.binomial(30, fa)
    be = int(round(0.7 * m))
    ext = rng.binomial(be, 1 - vr) + rng.binomial(m - be, fa)
    pv = tables[k[:, :, None], anc]
    aB = pv[:, :, 1:] <= NIV
    cD = prod + ext
    M = 100 + m
    pool = (cD[:, :, :1] + cD[:, :, 1:]) / (2.0 * M)
    se = np.sqrt(pool * (1 - pool) * 2.0 / M)
    z = np.zeros_like(se)
    ok = se > 0
    diff = cD[:, :, 1:] / M - cD[:, :, :1] / M
    z[ok] = diff[ok] / se[ok]
    aD = ok & (np.abs(z) >= ZC)
    gt = gens[1:]
    apres_t = gt[None, None, :] >= g[:, :, None]
    detB = (aB & apres_t).any(axis=2)
    detD = (aD & apres_t).any(axis=2)
    masque = aB & apres_t
    premiere = np.where(detB, gt[np.argmax(masque, axis=2)], 0)
    delai = np.where(detB, premiere - g, 0)
    alarmeB = aB.any(axis=2)
    return detB, detD, delai, alarmeB


@functools.lru_cache(maxsize=None)
def signe_ok(n10, n01):
    n = n10 + n01
    return 40 * sum(math.comb(n, k) for k in range(n10, n + 1)) <= 2 ** n


@functools.lru_cache(maxsize=None)
def seuil_signe(n):
    """Plus petit n10 tel que signe_ok(n10, n - n10) ; n + 1 si aucun (recherche par dichotomie, la condition
    étant monotone en n10)."""
    if not signe_ok(n, 0):
        return n + 1
    bas, haut = 0, n
    while bas < haut:
        mil = (bas + haut) // 2
        if signe_ok(mil, n - mil):
            haut = mil
        else:
            bas = mil + 1
    return bas


def mot_cellule(N0, NE, F, EB, ED, n10, n01, S, A):
    c1 = "atteinte" if 100 * F > 8 * N0 else "tenue"
    if 100 * ED >= 98 * NE or (100 * EB <= 2 * NE and 100 * ED <= 2 * NE):
        c2 = "sans prise"
    elif 100 * (EB - ED) >= 5 * NE and signe_ok(n10, n01):
        c2 = "tenue"
    elif EB <= ED:
        c2 = "atteinte"
    else:
        c2 = "indecise"
    if EB == 0:
        c3 = "indefinie"
    elif S <= EB:
        c3 = "tenue"
    elif 6 * S >= 17 * EB:
        c3 = "atteinte"
    else:
        c3 = "indecise"
    if A == 0:
        c4 = "indefinie"
    elif 2 * EB > A:
        c4 = "tenue"
    elif 4 * EB <= A:
        c4 = "atteinte"
    else:
        c4 = "indecise"
    if c1 == "atteinte":
        mot = "refute"
    elif c2 == "sans prise":
        mot = "sans prise"
    elif "atteinte" in (c2, c3, c4):
        mot = "refute"
    elif (c1, c2, c3, c4) == ("tenue",) * 4:
        mot = "tient"
    else:
        mot = "sans prise"
    return mot, (c1, c2, c3, c4)


def simulation(P, bloc=50):
    parent = np.random.SeedSequence(551177, spawn_key=(1,))
    enfants = parent.spawn(len(MS))
    res = {}
    mots_par_m = {}
    for i, m in enumerate(MS):
        rng = np.random.default_rng(enfants[i])
        tables = np.stack([pvaleurs(m, kk / 100.0) for kk in range(101)])
        mots = []
        clauses = {j: {} for j in range(4)}
        cumul = {"F": 0, "EB": 0, "ED": 0, "S": 0, "A": 0, "detB_sans": 0, "detD_sans": 0}
        faits = 0
        while faits < P:
            p = min(bloc, P - faits)
            dE, dDE, delE, alE = tirer_groupe(rng, p, 500, m, EFFET, True, tables)
            dS, dDS, _, alS = tirer_groupe(rng, p, 500, m, SANS_EFFET, True, tables)
            _, _, _, al0a = tirer_groupe(rng, p, 500, m, EFFET, False, tables)
            _, _, _, al0b = tirer_groupe(rng, p, 500, m, SANS_EFFET, False, tables)
            F = al0a.sum(axis=1) + al0b.sum(axis=1)
            EB = dE.sum(axis=1)
            ED = dDE.sum(axis=1)
            n10 = (dE & ~dDE).sum(axis=1)
            n01 = (~dE & dDE).sum(axis=1)
            S = delE.sum(axis=1)
            A = alE.sum(axis=1) + alS.sum(axis=1) + al0a.sum(axis=1) + al0b.sum(axis=1)
            for j in range(p):
                mot, cl = mot_cellule(1000, 500, int(F[j]), int(EB[j]), int(ED[j]), int(n10[j]), int(n01[j]),
                                      int(S[j]), int(A[j]))
                mots.append(mot)
                for q in range(4):
                    clauses[q][cl[q]] = clauses[q].get(cl[q], 0) + 1
            cumul["F"] += int(F.sum())
            cumul["EB"] += int(EB.sum())
            cumul["ED"] += int(ED.sum())
            cumul["S"] += int(S.sum())
            cumul["A"] += int(A.sum())
            cumul["detB_sans"] += int(dS.sum())
            cumul["detD_sans"] += int(dDS.sum())
            faits += p
        mots_par_m[m] = mots
        res[str(m)] = {
            "passages": P,
            "mots": {w: mots.count(w) for w in ("tient", "refute", "sans prise")},
            "clauses": {str(q + 1): clauses[q] for q in range(4)},
            "population_simulee": {
                "fausse_alarme_B": cumul["F"] / (1000 * P),
                "detection_a_effet_B": cumul["EB"] / (500 * P),
                "detection_a_effet_D": cumul["ED"] / (500 * P),
                "detection_sans_effet_B": cumul["detB_sans"] / (500 * P),
                "detection_sans_effet_D": cumul["detD_sans"] / (500 * P),
                "delai_moyen_B": cumul["S"] / cumul["EB"],
                "part_b_B": cumul["EB"] / cumul["A"]},
        }
    carte = {"tient": 0, "refute": 0, "sans prise": 0}
    for a, b in zip(mots_par_m[20], mots_par_m[40]):
        if "refute" in (a, b):
            carte["refute"] += 1
        elif a == b == "tient":
            carte["tient"] += 1
        else:
            carte["sans prise"] += 1
    res["carte_sur_les_passages_apparies_20_40"] = carte
    return res


# ------------------------------------------------------------------ points des courbes génériques
def clause2_generique(p10, p01, NE=500):
    q = p10 + p01
    tenue = atteinte = 0.0
    for n in range(NE + 1):
        pn = stats.binom.pmf(n, NE, q)
        if pn == 0:
            continue
        k10 = np.arange(n + 1)
        pk = stats.binom.pmf(k10, n, p10 / q)
        ecart = 2 * k10 - n
        t = (100 * ecart >= 5 * NE) & (k10 >= seuil_signe(n))
        tenue += pn * pk[t].sum()
        atteinte += pn * pk[(ecart <= 0) & ~t].sum()
    return {"tenue": tenue, "atteinte": atteinte}


def generiques():
    c1 = {str(t): float(stats.binom.sf(80, 1000, t)) for t in (0.05, 0.065, 0.07, 0.08, 0.09, 0.10, 0.12)}
    c2 = {}
    for ecart in (-0.05, 0.0, 0.05, 0.10, 0.15):
        for disc in (0.2, 0.6):
            c2[f"ecart={ecart};discordance={disc}"] = clause2_generique((disc + ecart) / 2, (disc - ecart) / 2)
    return {"clause_1_N0_1000": c1, "clause_2_NE_500": c2}


def arithmetique():
    num = Fraction(0)
    den = Fraction(0)
    for g in GCH:
        fen = 13 - g
        num += Fraction(fen * (fen - 1), 2)
        den += fen
    m10 = pvaleurs(10, 0.10) <= NIV
    seuil = int(np.argmax(m10[2:])) + 2
    return {"delai_sans_information": str(num / den), "egal_17_sur_6": num / den == Fraction(17, 6),
            "m10_erreurs_qui_font_sonner": [int(x) for x in np.nonzero(m10)[0]],
            "m10_premier_x_haut": seuil,
            "m10_chance_par_generation_juge_0_25": float(stats.binom.sf(seuil - 1, 10, 0.25))}


def comparer(red, ex):
    cmp = {}
    t = red["par_taille"]["taille_jouee_2000_suites"]
    for m in MS:
        c = t["cellules"][str(m)]
        pb = c["population_par_bras"]["B"]
        pd = c["population_par_bras"]["D"]
        e = ex[str(m)]
        cmp[str(m)] = {
            "fa_B": [pb["fausse_alarme_suites_sans_changement"], e["B"]["fausse_alarme"]],
            "det_effet_B": [pb["detection_changement_a_effet"], e["B"]["detection_a_effet"]],
            "det_sans_effet_B": [pb["detection_changement_sans_effet"], e["B"]["detection_sans_effet"]],
            "delai_B": [pb["delai_moyen_changement_a_effet_rapport_des_esperances"], e["B"]["delai_moyen_a_effet"]],
            "part_b_B": [pb["part_b_rapport_des_esperances"], e["B"]["part_b"]],
            "fa_D": [pd["fausse_alarme_suites_sans_changement"], e["D"]["fausse_alarme"]],
            "det_effet_D": [pd["detection_changement_a_effet"], e["D"]["detection_a_effet"]],
            "det_sans_effet_D": [pd["detection_changement_sans_effet"], e["D"]["detection_sans_effet"]],
            "clause_1_atteinte": [c["clauses_bras_B"]["1_fausse_alarme"]["atteinte"],
                                  e["clause_1_atteinte_exacte_2000_suites"]],
            "clause_3_tenue_redacteur_vs_borne_chernoff": [c["clauses_bras_B"]["3_delai"]["tenue"],
                                                           e["borne_chernoff_clause_3_tenue_2000_suites"]],
            "mot_cellule_bornes_redacteur": c["mot_de_la_cellule_bornes"],
        }
        cles = ("fa_B", "det_effet_B", "det_sans_effet_B", "delai_B", "part_b_B", "fa_D", "det_effet_D",
                "det_sans_effet_D")
        cmp[str(m)]["ecart_max_population"] = max(abs(cmp[str(m)][kk][0] - cmp[str(m)][kk][1]) for kk in cles)
    cmp["carte_redacteur"] = t["mot_de_la_carte_bornes"]
    t4 = red["par_taille"]["taille_4000_suites"]["cellules"]["20"]["clauses_bras_B"]["1_fausse_alarme"]["atteinte"]
    cmp["clause_1_m20_4000_suites"] = [t4, ex["20"]["clause_1_atteinte_exacte_4000_suites"]]
    return cmp


def main(argv):
    if len(argv) != 4:
        raise SystemExit(__doc__)
    with open(argv[1], encoding="utf-8") as f:
        red = json.load(f)
    P = int(argv[3])
    ex = voie_exacte()
    sim = simulation(P)
    sortie = {"version": "verification-independante-mot-alarme-v1", "z_critique": ZC, "voie_exacte": ex,
              "simulation_directe": sim, "generiques": generiques(), "arithmetique": arithmetique(),
              "comparaison_au_redacteur": comparer(red, ex)}
    with open(argv[2], "x", encoding="utf-8") as f:
        json.dump(sortie, f, ensure_ascii=False, indent=1, sort_keys=True, default=float)
        f.write("\n")


if __name__ == "__main__":
    main(sys.argv)
