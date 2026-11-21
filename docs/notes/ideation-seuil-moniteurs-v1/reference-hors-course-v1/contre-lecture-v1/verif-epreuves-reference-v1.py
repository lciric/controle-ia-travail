#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Vérification du relecteur affecté (mode « épreuve qui ne peut pas échouer,
ou pas réussir ») — section « Référence hors course » et critères de lecture.

Usage : python3 -I -B verif-epreuves-reference-v1.py

Parties exactes (sans tirage) : couverture exacte de l'intervalle de
Clopper-Pearson à 99 % ; puissance des morts « invalide » par approximation
normale du t de Student ; borne c(W) sous dépendance.
Parties par tirage (numpy, graine SeedSequence fixée ci-dessous, règle R9) :
taux de rouge de la garde de l'objet vrai sur un générateur sain ;
puissance de la mort de l'objet faux sous loi normale.
"""
import math
from statistics import NormalDist

import numpy as np

N01 = NormalDist()
R = 2000                      # tirages de calibration, unité des intervalles
ALPHA2 = 0.005                # demi-risque d'un intervalle à 99 %
Z995 = N01.inv_cdf(0.995)
RACINE = 20261121


def binom_logpmf(n, j, p):
    return (math.lgamma(n + 1) - math.lgamma(j + 1) - math.lgamma(n - j + 1)
            + j * math.log(p) + (n - j) * math.log1p(-p))


def table_binom(n, p):
    pmf = [math.exp(binom_logpmf(n, j, p)) for j in range(n + 1)]
    cdf = []
    s = 0.0
    for v in pmf:
        s += v
        cdf.append(s)
    sf = [1.0 - (cdf[j - 1] if j > 0 else 0.0) for j in range(n + 1)]  # P(X >= j)
    return pmf, cdf, sf


def ensemble_accepte_cp(n, p0):
    """x tels que p0 est dans l'intervalle de Clopper-Pearson à 99 % de x.
    p0 > borne basse(x) ssi P_p0(X >= x) > 0,005 ; p0 < borne haute(x) ssi
    P_p0(X <= x) > 0,005."""
    pmf, cdf, sf = table_binom(n, p0)
    acc = [(sf[x] > ALPHA2) and (cdf[x] > ALPHA2) for x in range(n + 1)]
    couverture = sum(pmf[x] for x in range(n + 1) if acc[x])
    return acc, couverture


def t_quantile_995(df):
    # Pour df = 1999 le quantile de Student à 0,995 vaut z + (z^3 + z)/(4 df) au premier ordre.
    z = Z995
    return z + (z ** 3 + z) / (4.0 * df) + (5 * z ** 5 + 16 * z ** 3 + 3 * z) / (96.0 * df * df)


T995 = t_quantile_995(R - 1)


def ligne(*m):
    print(" ".join(str(x) for x in m))


def partie_1_garde_objet_vrai(rng, repliques=20000):
    ligne("[1] Garde de la référence (§ 9, objet vrai ; arrêt n° 20) sur un générateur SAIN")
    ligne("    V1* de la référence = Beta(k, m + 1 - k) exactement pour une loi continue")
    ligne("    t de Student à 0,995, df = 1999 :", f"{T995:.4f}")
    rouges_cellule = {}
    for m in (200, 400):
        k = int(math.floor(0.01 * (m + 1) + 1e-12))
        moy = k / (m + 1)
        p0 = sum(math.exp(binom_logpmf(m, j, 0.01)) for j in range(k, m + 1))
        acc, couv_cp = ensemble_accepte_cp(R, p0)
        ligne(f"    m = {m}, k = {k} : moyenne vraie {moy:.6f} ; part vraie V1* <= 1 % = {p0:.4f}")
        ligne(f"      couverture exacte de Clopper-Pearson 99 % à {R} tirages : {couv_cp:.5f}"
              f" (rouge {1 - couv_cp:.5f})")
        rouge_moy = 0
        rouge_cp = 0
        rouge_un = 0
        for _ in range(repliques):
            v = rng.beta(k, m + 1 - k, size=R)
            mu = v.mean()
            se = v.std(ddof=1) / math.sqrt(R)
            miss_m = not (mu - T995 * se <= moy <= mu + T995 * se)
            x = int((v <= 0.01).sum())
            miss_c = not acc[x]
            rouge_moy += miss_m
            rouge_cp += miss_c
            rouge_un += (miss_m or miss_c)
        q = rouge_un / repliques
        rouges_cellule[m] = q
        ligne(f"      sur {repliques} répliques : rouge par la moyenne {rouge_moy / repliques:.4f} ;"
              f" par la part {rouge_cp / repliques:.4f} ; par l'une ou l'autre {q:.4f}")
    q_paire = 1 - (1 - rouges_cellule[200]) * (1 - rouges_cellule[400])
    ligne(f"    rouge d'un couple (monde, tranche), m = 200 et 400 joués : {q_paire:.4f}")
    ligne("    P(garde rouge au moins une fois | générateur sain), cellules indépendantes :")
    for familles in (1, 3, 4, 5, 6, 8, 10):
        cellules = 3 * familles
        ligne(f"      {familles} famille(s) continue(s) x 3 tranches = {cellules} couples :"
              f" {1 - (1 - q_paire) ** cellules:.3f}")


def partie_2_objet_faux(rng, repliques=2000):
    ligne("[2] Objet faux (§ 9) : témoins de la loi de calibration, usage sous dérive, loi normale")
    z99 = N01.inv_cdf(0.99)
    d = z99 - N01.inv_cdf(0.97)
    for m in (200, 400):
        k = int(math.floor(0.01 * (m + 1) + 1e-12))
        tues = 0
        moyennes = []
        sds = []
        for _ in range(repliques):
            u = rng.beta(k, m + 1 - k, size=R)            # 1 - F(seuil) sous la loi de calibration
            s = np.array([N01.inv_cdf(1.0 - x) for x in u])
            v = 0.5 * np.array([math.erfc((si - d) / math.sqrt(2.0)) for si in s])
            mu = v.mean()
            se = v.std(ddof=1) / math.sqrt(R)
            moyennes.append(mu)
            sds.append(v.std(ddof=1))
            tues += (mu - T995 * se > 0.01)
        ligne(f"    m = {m} : moyenne de V1* {np.mean(moyennes):.5f} ; écart type par tirage {np.mean(sds):.5f} ;"
              f" part des répliques où la mort « invalide, en moyenne » tombe : {tues / repliques:.4f}")
        # garde de l'arrêt n° 20 sur l'artefact : la moyenne vraie k/(m+1) hors de l'intervalle ?
        ligne(f"      écart à k/(m+1) en erreurs types : {(np.mean(moyennes) - k / (m + 1)) / (np.mean(sds) / math.sqrt(R)):.1f}")


def puissance_mort_moyenne(mu, sd):
    se = sd / math.sqrt(R)
    return 1.0 - N01.cdf(T995 - (mu - 0.01) / se)


def puissance_mort_confiance(p_vrai, risque):
    """P(borne basse CP 99 % de la part > risque) ssi P_risque(X >= x) <= 0,005."""
    pmf_r, cdf_r, sf_r = table_binom(R, risque)
    pmf_v, _, _ = table_binom(R, p_vrai)
    return sum(pmf_v[x] for x in range(R + 1) if sf_r[x] <= ALPHA2)


def partie_3_puissance_doit_mourir():
    ligne("[3] Puissance de mort d'un témoin « doit mourir » selon sa distance au seuil (2 000 tirages, 99 %)")
    ligne("    (a) garantie « en moyenne », écart type par tirage pris à 0,0060 (ordre de Beta(3, 298))")
    sd = math.sqrt(3 * 298 / (301 ** 2 * 302))
    ligne(f"        écart type de Beta(3, 298) : {sd:.5f}")
    for mu in (0.0100, 0.0102, 0.0104, 0.0105, 0.0106, 0.0108, 0.0110, 0.0120):
        ligne(f"        taux vrai moyen {mu:.4f} : P(mort) = {puissance_mort_moyenne(mu, sd):.4f}")
    ligne("    (b) garantie « avec une confiance dite », risque 0,05 : part vraie des tirages où V1* > 1 %")
    for p in (0.050, 0.055, 0.060, 0.065, 0.070, 0.080):
        ligne(f"        part vraie {p:.3f} : P(mort) = {puissance_mort_confiance(p, 0.05):.4f}")
    ligne("    (c) témoin « doit tenir » au bord exact (T02, part 0,0495 ; T03, moyenne 0,00997)")
    ligne(f"        T02 : P(mort) = {puissance_mort_confiance(1 - 0.9505, 0.05):.5f}")
    ligne(f"        T03 : P(mort) = {puissance_mort_moyenne(3 / 301, sd):.5f}")


def partie_4_cw_dependance():
    ligne("[4] Borne c(W) (critères, § 4, point 2) si les morts de témoins « doit tenir » sont liées")
    ligne("    exemple : W témoins en W/2 paires de règles identiques jouées sur les mêmes tirages")
    for w in (4, 10, 20, 30):
        paires = w // 2
        p_sup1 = 1 - (1 - 0.005) ** paires   # au moins une paire meurt -> 2 morts > c = 1
        ligne(f"      W = {w}, c = 1 : P(plus de c morts) = {p_sup1:.4f} (borne visée 0,01)")


def main():
    ss = np.random.SeedSequence(RACINE)
    e1, e2 = ss.spawn(2)
    ligne("Vérification du relecteur affecté, épreuve qui ne peut pas échouer ou pas réussir — v1")
    ligne("numpy", np.__version__, "; racine", RACINE)
    partie_1_garde_objet_vrai(np.random.default_rng(e1))
    partie_2_objet_faux(np.random.default_rng(e2))
    partie_3_puissance_doit_mourir()
    partie_4_cw_dependance()


if __name__ == "__main__":
    main()
