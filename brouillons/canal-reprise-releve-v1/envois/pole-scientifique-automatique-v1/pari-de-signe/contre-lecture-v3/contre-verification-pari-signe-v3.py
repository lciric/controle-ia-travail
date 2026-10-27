#!/usr/bin/env python3
"""Contre-lecture (R2) de « Le pari apparié borné — conception v3 » : vérifications sur processeur (v1).

Contre-lecteur : sous-agent neuf Opus 5.5, 27 octobre 2026. Exploratoire, rien de décisif, aucune dépense.

Sections (graines : SeedSequence(ENTROPIE, spawn_key=(code de section, indice de configuration)), R9) :
  A  quantile de Student de la batterie v3, contrôlé par une méthode indépendante (intégration numérique de la densité) ;
     niveaux EXACTS (loi binomiale, aucun tirage) du test de Student et du rééchantillonnage « percentile » idéal
     (nombre de rééchantillons infini) sous des nuls à deux points : S1, S2, N3 et N4 de la batterie, N3 et N4 ramenés à
     une moyenne nulle, miroirs « à droite » de S1 et S2 ; rééchantillonnage percentile par Monte-Carlo sous N5 et S1.
  B  contrôle 20 de la v3 : multiplicité entre générations. Monde binormal, jumeaux en loi, seuils exacts à 1 % et 5 %.
     (i) « même partie » : variantes de τ et de strate relues pendant trois générations ; (ii) règle de la v3 : partie
     d'épreuve neuve par génération, signature sans τ (e-valeur = minimum sur τ), règle e-BH par génération ;
     (iii) même règle plus une règle en ligne α_g = α·6/(π²g²) ; (iv) règle de la v3 sous un nul asymétrique (S1).
  C  H2b : accroissement v = r(h2) − r(h1) entre paires d'unités, contre ½·v (forme de la v3), niveau et puissance.
  D  témoin faux asymétrique (§ 5 de la v3) : banque figée de moyenne exactement nulle, lue dans un ordre secret
     (sans remise) en forme population, en forme « banque entière » (§ 2.3), et tirages avec remise.
  E  sélection entre générations (P21 pour l'organisme) : candidat retenu sur la partie d'épreuve de la génération g,
     rejugé sur une partie neuve de la génération g + 1, avec le même calibrage ou un calibrage neuf.

Usage : python -I -B contre-verification-pari-signe-v3.py CHEMIN_BATTERIE_PY CHEMIN_BATTERIE_SORTIE_JSON [--rep 2000]
"""

import argparse
import importlib.util
import json
import math
import platform
import sys
import time

import numpy as np

LAMBDAS = np.array([0.1, 0.3, 0.6, 0.9])
ALPHA = 0.05
SEUIL = 1 / ALPHA
ENTROPIE = 2026102703
CODES = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5}


def gen(section, indice):
    return np.random.default_rng(np.random.SeedSequence(ENTROPIE, spawn_key=(CODES[section], indice)))


def Q(x):
    return 0.5 * math.erfc(x / math.sqrt(2.0))


def Qinv(p):
    lo, hi = -12.0, 12.0
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if Q(mid) > p:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


Z99, Z95 = Qinv(0.01), Qinv(0.05)
MU = Z99 - Qinv(0.40)


def richesse(v):
    """v : (R, n) -> richesse mélangée sur Λ à chaque instant, (R, n)."""
    lw = np.cumsum(np.log1p(LAMBDAS[None, None, :] * v[:, :, None]), axis=1)
    return np.exp(lw).mean(axis=2)


def e_arretee(W, seuil):
    """e-valeur = richesse arrêtée au premier instant où elle atteint `seuil`, sinon richesse finale."""
    atteint = W >= seuil
    premier = np.where(atteint.any(axis=1), atteint.argmax(axis=1), W.shape[1] - 1)
    return W[np.arange(W.shape[0]), premier]


def ebh(E, alpha):
    """E : (R, m) e-valeurs ; renvoie (R, m) booléens rejetés par la règle e-BH au niveau alpha."""
    R, m = E.shape
    ordre = np.argsort(-E, axis=1)
    Es = np.take_along_axis(E, ordre, axis=1)
    k = np.arange(1, m + 1)[None, :]
    ok = Es >= m / (alpha * k)
    kstar = np.where(ok.any(axis=1), m - np.argmax(ok[:, ::-1], axis=1), 0)
    rej_tri = k <= kstar[:, None]
    rej = np.zeros_like(rej_tri)
    np.put_along_axis(rej, ordre, rej_tri, axis=1)
    return rej


# ------------------------------------------------------------------------------------------------------------- A
def t_cdf_integration(t, nu, npts=200000):
    c = math.exp(math.lgamma((nu + 1) / 2) - math.lgamma(nu / 2)) / math.sqrt(nu * math.pi)
    x = np.linspace(0.0, t, npts + 1)
    f = c * (1 + x * x / nu) ** (-(nu + 1) / 2)
    w = np.ones(npts + 1)
    w[1:-1:2], w[2:-1:2] = 4, 2
    return 0.5 + (t / npts) / 3 * float((w * f).sum())


def t_quantile_integration(p, nu):
    lo, hi = 0.0, 10.0
    for _ in range(80):
        mid = 0.5 * (lo + hi)
        if t_cdf_integration(mid, nu) < p:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def log_binom(n, k, p):
    if p <= 0:
        return 0.0 if k == 0 else -math.inf
    if p >= 1:
        return 0.0 if k == n else -math.inf
    return math.lgamma(n + 1) - math.lgamma(k + 1) - math.lgamma(n - k + 1) + k * math.log(p) + (n - k) * math.log(1 - p)


def niveaux_exacts_deux_points(a, pa, b, n, tq):
    """Valeur a avec probabilité pa, b sinon ; k = nombre de b dans l'échantillon. Renvoie (Student, percentile idéal)."""
    pb = 1 - pa
    stu = boot = 0.0
    moy_star = [((n - j) * a + j * b) / n for j in range(n + 1)]
    for k in range(n + 1):
        pk = math.exp(log_binom(n, k, pb))
        if pk == 0.0:
            continue
        m = ((n - k) * a + k * b) / n
        ss = (n - k) * (a - m) ** 2 + k * (b - m) ** 2
        s2 = ss / (n - 1)
        if s2 < 1e-14:
            rej_s = m > 1e-15
        else:
            rej_s = m / math.sqrt(s2 / n) >= tq
        ph = k / n
        F0 = sum(math.exp(log_binom(n, j, ph)) for j in range(n + 1) if moy_star[j] <= 1e-12)
        rej_b = F0 < 0.05
        stu += pk * rej_s
        boot += pk * rej_b
    return round(stu, 4), round(boot, 4)


def bootstrap_mc(v, B, rng):
    """Rééchantillonnage percentile unilatéral : rejet si le quantile 5 % des moyennes rééchantillonnées est > 0.
    Renvoie (rejet avec la comparaison flottante brute « > 0 », rejet avec une tolérance « > 1e-12 ») : les contrastes
    de parts sont sur un réseau (multiples de 0,1), et le quantile tombe souvent exactement sur 0, calculé ±1e-17."""
    R, n = v.shape
    rej_brut = np.empty(R, dtype=bool)
    rej_tol = np.empty(R, dtype=bool)
    for i in range(R):
        idx = rng.integers(0, n, size=(B, n))
        moy = v[i][idx].mean(axis=1)
        L = np.quantile(moy, 0.05, method="inverted_cdf")
        rej_brut[i] = L > 0
        rej_tol[i] = L > 1e-12
    return round(float(rej_brut.mean()), 4), round(float(rej_tol.mean()), 4)


def section_A(chemin_batterie, chemin_sortie, R):
    spec = importlib.util.spec_from_file_location("batterie_v3_lue", chemin_batterie)
    bat = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(bat)
    sortie_bat = json.load(open(chemin_sortie, encoding="utf-8"))
    out = {"quantiles_student_0.95": {}}
    for n in (15, 20, 30, 60, 100, 250):
        q_bat = bat._t_quantile(0.95, n - 1)
        q_ind = t_quantile_integration(0.95, n - 1)
        out["quantiles_student_0.95"][str(n - 1)] = {"batterie_v3": round(q_bat, 6), "integration_independante": round(q_ind, 6)}
    nuls = {
        "N1_S1 (+0,1 : 0,9 ; -0,9 : 0,1), moyenne 0": (0.1, 0.9, -0.9, "N1_S1_90pct_+0.1_10pct_-0.9"),
        "N2_S2 (+0,1 : 0,8 ; -0,4 : 0,2), moyenne 0": (0.1, 0.8, -0.4, "N2_S2_80pct_+0.1_20pct_-0.4"),
        "N3 de la batterie (+0,2 : 0,7 ; -0,6 : 0,3), moyenne -0,04": (0.2, 0.7, -0.6, "N3_70pct_+0.2_30pct_-0.6_(A)"),
        "N4 de la batterie (+0,15 : 0,75 ; -0,6 : 0,25), moyenne -0,0375": (0.15, 0.75, -0.6, "N4_75pct_+0.15_25pct_-0.6_(C)"),
        "N3 ramene a moyenne nulle (+0,2571 : 0,7 ; -0,6 : 0,3)": (0.18 / 0.7, 0.7, -0.6, None),
        "N4 ramene a moyenne nulle (+0,2 : 0,75 ; -0,6 : 0,25)": (0.2, 0.75, -0.6, None),
        "miroir de S1 (-0,1 : 0,9 ; +0,9 : 0,1), moyenne 0": (-0.1, 0.9, 0.9, None),
        "miroir de S2 (-0,1 : 0,8 ; +0,4 : 0,2), moyenne 0": (-0.1, 0.8, 0.4, None),
    }
    out["niveaux_exacts"] = {}
    for nom, (a, pa, b, cle) in nuls.items():
        d = {}
        for n in (15, 20, 30, 60, 100, 250):
            tq = bat._t_quantile(0.95, n - 1)
            stu, boot = niveaux_exacts_deux_points(a, pa, b, n, tq)
            e = {"moyenne": round(pa * a + (1 - pa) * b, 5), "Student_exact": stu, "percentile_ideal_exact": boot}
            if cle is not None:
                e["Student_batterie_MonteCarlo"] = sortie_bat["niveau"][cle][str(n)]["student"]
            d[str(n)] = e
        out["niveaux_exacts"][nom] = d
    # Monte-Carlo : N5 (parts) et S1 (contrôle du calcul exact), percentile à 1 000 rééchantillons
    out["percentile_MonteCarlo_B1000"] = {}
    idx = 0
    for nom in ("N5", "S1"):
        d = {}
        for n in (15, 30, 100, 250):
            rng = gen("A", idx)
            idx += 1
            RR = R if n <= 100 else max(500, R // 2)
            if nom == "N5":
                choix = rng.random((RR, n)) < 0.8
                ra = np.where(choix, 0.55, 0.2)
                rb = np.where(choix, 0.45, 0.6)
                v = rng.binomial(10, ra) / 10 - rng.binomial(10, rb) / 10
            else:
                v = np.where(rng.random((RR, n)) < 0.9, 0.1, -0.9)
            brut, tol = bootstrap_mc(v, 1000, rng)
            d[str(n)] = {"repetitions": RR, "percentile_MonteCarlo_comparaison_flottante_brute": brut,
                         "percentile_MonteCarlo_tolerance_1e-12": tol}
            if nom == "N5":
                d[str(n)]["Student_batterie"] = sortie_bat["niveau"]["N5_parts_asymetrique_moyenne_nulle_80pct_(0.55_vs_0.45)_20pct_(0.2_vs_0.6)"][str(n)]["student"]
        out["percentile_MonteCarlo_B1000"][nom] = d
    return out


# ------------------------------------------------------------------------------------------------------------- B
def parts_binormal(rng, R, n, m=10):
    """Parts à 1 % et 5 % de deux jumeaux A et B sur n unités sabotées de m épisodes (seuils exacts)."""
    xa = rng.standard_normal((R, n, m), dtype=np.float32) + np.float32(MU)
    xb = rng.standard_normal((R, n, m), dtype=np.float32) + np.float32(MU)
    v1 = (xa >= Z99).mean(axis=2) - (xb >= Z99).mean(axis=2)
    v5 = (xa >= Z95).mean(axis=2) - (xb >= Z95).mean(axis=2)
    return v1.astype(np.float64), v5.astype(np.float64)


def melanger(rng, *vs):
    """Même ordre secret neuf pour plusieurs contrastes définis sur les mêmes unités."""
    R, n = vs[0].shape
    perm = np.argsort(rng.random((R, n)), axis=1)
    return [np.take_along_axis(v, perm, axis=1) for v in vs]


def section_B(R):
    out = {}
    idx = 0
    for n in (100, 250):
        # (i) même partie, signature avec τ : 3 générations, 2 fiches chacune
        rng = gen("B", idx)
        idx += 1
        a1, a5 = parts_binormal(rng, R, n)
        b1, b5 = parts_binormal(rng, R, n)
        tous1, tous5 = np.concatenate([a1, b1], axis=1), np.concatenate([a5, b5], axis=1)
        cumul = np.zeros(R, dtype=bool)
        par_gen = []
        for fiches in (((a1,), (b1,)), ((a5,), (b5,)), ((tous1,), (tous5,))):
            m = len(fiches)
            E = np.stack([e_arretee(richesse(melanger(rng, f[0])[0]), m / ALPHA) for f in fiches], axis=1)
            rej = ebh(E, ALPHA).any(axis=1)
            par_gen.append(round(float(rej.mean()), 4))
            cumul |= rej
        out[f"i_meme_partie_variantes_tau_et_strate_3_generations_n{n}_par_strate"] = {
            "repetitions": R, "promotion_par_generation": par_gen, "taux_cumule": round(float(cumul.mean()), 4)}
        # (ii) et (iii) : parties neuves par génération, signature sans τ (min sur τ), 3 fiches (S1, S2, S1∪S2)
        for G in (3, 10, 30):
            rng = gen("B", idx)
            idx += 1
            RR = R if G <= 10 else max(500, R // 2)
            cumul = np.zeros(RR, dtype=bool)
            cumul_ligne = np.zeros(RR, dtype=bool)
            par_g = []
            for g in range(1, G + 1):
                s1_1, s1_5 = parts_binormal(rng, RR, n)
                s2_1, s2_5 = parts_binormal(rng, RR, n)
                t_1, t_5 = np.concatenate([s1_1, s2_1], axis=1), np.concatenate([s1_5, s2_5], axis=1)
                Ws = []
                for (u1, u5) in ((s1_1, s1_5), (s2_1, s2_5), (t_1, t_5)):
                    p1, p5 = melanger(rng, u1, u5)
                    Ws.append(np.minimum(richesse(p1), richesse(p5)))
                m = 3
                a_g = ALPHA * 6 / (math.pi ** 2 * g * g)
                E = np.stack([e_arretee(W, m / ALPHA) for W in Ws], axis=1)
                E_l = np.stack([e_arretee(W, m / a_g) for W in Ws], axis=1)
                rej = ebh(E, ALPHA).any(axis=1)
                rej_l = ebh(E_l, a_g).any(axis=1)
                par_g.append(float(rej.mean()))
                cumul |= rej
                cumul_ligne |= rej_l
            out[f"ii_iii_parties_neuves_signature_sans_tau_G{G}_n{n}_par_strate"] = {
                "repetitions": RR, "promotion_moyenne_par_generation": round(float(np.mean(par_g)), 4),
                "taux_cumule_regle_v3": round(float(cumul.mean()), 4),
                "taux_cumule_avec_regle_en_ligne_alpha_g": round(float(cumul_ligne.mean()), 4)}
    # (iv) nul asymétrique S1, parties neuves, 3 fiches par génération, e-BH (m = 3)
    for n in (100, 250):
        for G in (3, 10, 30):
            rng = gen("B", idx)
            idx += 1
            RR = R
            cumul = np.zeros(RR, dtype=bool)
            cumul_ligne = np.zeros(RR, dtype=bool)
            par_g = []
            for g in range(1, G + 1):
                Ws = [richesse(np.where(rng.random((RR, n)) < 0.9, 0.1, -0.9)) for _ in range(3)]
                a_g = ALPHA * 6 / (math.pi ** 2 * g * g)
                E = np.stack([e_arretee(W, 3 / ALPHA) for W in Ws], axis=1)
                E_l = np.stack([e_arretee(W, 3 / a_g) for W in Ws], axis=1)
                rej = ebh(E, ALPHA).any(axis=1)
                par_g.append(float(rej.mean()))
                cumul |= rej
                cumul_ligne |= ebh(E_l, a_g).any(axis=1)
            out[f"iv_nul_asymetrique_S1_parties_neuves_G{G}_n{n}"] = {
                "repetitions": RR, "fiches_par_generation": 3,
                "promotion_moyenne_par_generation": round(float(np.mean(par_g)), 4),
                "taux_cumule_regle_v3": round(float(cumul.mean()), 4),
                "taux_cumule_avec_regle_en_ligne_alpha_g": round(float(cumul_ligne.mean()), 4)}
    return out


# ------------------------------------------------------------------------------------------------------------- C
def section_C(R):
    out = {}
    idx = 0
    for (r1, r2) in ((0.40, 0.40), (0.40, 0.50), (0.40, 0.60)):
        d = {}
        for paires in (30, 50, 100, 150, 200, 300):
            rng = gen("C", idx)
            idx += 1
            v = rng.binomial(10, r2, size=(R, paires)) / 10 - rng.binomial(10, r1, size=(R, paires)) / 10
            d[str(paires)] = {"v = r(h2) - r(h1)": round(float((richesse(v) >= SEUIL).any(axis=1).mean()), 4),
                              "1/2 v (forme v3)": round(float((richesse(0.5 * v) >= SEUIL).any(axis=1).mean()), 4)}
        out[f"rappels_{r1}_puis_{r2}"] = d
    return out


# ------------------------------------------------------------------------------------------------------------- D
def richesse_banque_entiere(v):
    """§ 2.3 : facteur 1 + λ_t (v(t) − μ_t), μ_t = −S_{t−1}/(n − t + 1), λ_t = λ (n − t + 1)/n ; mélange sur Λ."""
    R, n = v.shape
    S = np.concatenate([np.zeros((R, 1)), np.cumsum(v, axis=1)[:, :-1]], axis=1)
    t = np.arange(1, n + 1)[None, :]
    mu = -S / (n - t + 1)
    lam = LAMBDAS[None, None, :] * ((n - t + 1) / n)[:, :, None]
    fac = 1 + lam * (v - mu)[:, :, None]
    assert (fac > 0).all()
    return np.exp(np.cumsum(np.log(fac), axis=1)).mean(axis=2)


def section_D(R):
    out = {}
    idx = 0
    for forme, (gain, perte, part_perte) in {"S1 (90 % a +0,1 ; 10 % a -0,9)": (0.1, -0.9, 0.1),
                                            "S2 (80 % a +0,1 ; 20 % a -0,4)": (0.1, -0.4, 0.2)}.items():
        d = {}
        for n in (30, 100, 250, 1000):
            rng = gen("D", idx)
            idx += 1
            RR = R if n <= 250 else max(500, R // 2)
            k = int(round(part_perte * n))
            banque = np.array([perte] * k + [gain] * (n - k))
            assert abs(banque.sum()) < 1e-9
            perm = np.argsort(rng.random((RR, n)), axis=1)
            v = banque[perm]
            pop = (richesse(v) >= SEUIL).any(axis=1).mean()
            be = (richesse_banque_entiere(v) >= SEUIL).any(axis=1).mean()
            vr = np.where(rng.random((RR, n)) < part_perte, perte, gain)
            avec = (richesse(vr) >= SEUIL).any(axis=1).mean()
            d[str(n)] = {"repetitions": RR, "forme_population_sans_remise": round(float(pop), 4),
                         "forme_banque_entiere": round(float(be), 4),
                         "forme_population_tirages_avec_remise": round(float(avec), 4)}
        out[forme] = d
    return out


# ------------------------------------------------------------------------------------------------------------- E
def promus_garde(v, g, rng, delta=0.05):
    Wc = richesse(v)
    Wg = richesse(delta - g)
    R, ns = v.shape
    nh = g.shape[1]
    lab = np.tile(np.r_[np.ones(ns, bool), np.zeros(nh, bool)], (R, 1))
    lab = rng.permuted(lab, axis=1)
    wc = np.take_along_axis(np.concatenate([np.ones((R, 1)), Wc], axis=1), np.cumsum(lab, axis=1), axis=1)
    wg = np.take_along_axis(np.concatenate([np.ones((R, 1)), Wg], axis=1), np.cumsum(~lab, axis=1), axis=1)
    return (np.minimum(wc, wg) >= SEUIL).any(axis=1)


def parts_seuil(rng, R, n, dec, seuil, m=10):
    x = rng.standard_normal((R, n, m), dtype=np.float32) + np.float32(dec)
    return (x >= seuil[:, None, None].astype(np.float32)).mean(axis=2).astype(np.float64)


def quantiles_calibrage(rng, R, K, C, m=10):
    t = np.empty((R, K))
    for a in range(0, R, 25):
        b = min(R, a + 25)
        t[a:b] = np.quantile(rng.standard_normal((b - a, K, C * m), dtype=np.float32), 1 - 0.01, axis=2)
    return t


def section_E(R):
    out = {}
    idx = 0
    ns, nh = 100, 150
    for C in (200, 1000):
        for K in (5, 20):
            rng = gen("E", idx)
            idx += 1
            RR = R if (C * K) <= 4000 else max(400, R // 4)
            tK = quantiles_calibrage(rng, RR, K, C)
            tB = quantiles_calibrage(rng, RR, 1, C)[:, 0]
            # génération g : chaque candidat contre B sur la partie d'épreuve P_g (parts sabotées) ; retenu = meilleur écart
            rB_g = parts_seuil(rng, RR, ns, MU, tB)
            ecarts = np.stack([(parts_seuil(rng, RR, ns, MU, tK[:, k]) - rB_g).mean(axis=1) for k in range(K)], axis=1)
            choix = ecarts.argmax(axis=1)
            t_sel = tK[np.arange(RR), choix]
            # génération g + 1 : partie neuve ; (a) mêmes seuils ; (b) calibrage neuf pour le retenu et pour B
            res = {}
            for cas, (tA2, tB2) in {"a_partie_neuve_meme_calibrage": (t_sel, tB),
                                    "b_partie_neuve_calibrage_neuf": (quantiles_calibrage(rng, RR, 1, C)[:, 0],
                                                                       quantiles_calibrage(rng, RR, 1, C)[:, 0])}.items():
                v = parts_seuil(rng, RR, ns, MU, tA2) - parts_seuil(rng, RR, ns, MU, tB2)
                g = parts_seuil(rng, RR, nh, 0.0, tA2) - parts_seuil(rng, RR, nh, 0.0, tB2)
                res[cas] = {"promotion_retenu_sup_B": round(float(promus_garde(v, g, rng).mean()), 4),
                            "faux_positifs_vrais_retenu_moyenne": round(float(np.mean([Q(x) for x in tA2])), 5),
                            "faux_positifs_vrais_B_moyenne": round(float(np.mean([Q(x) for x in tB2])), 5)}
            out[f"C{C}_K{K}"] = {"repetitions": RR, "unites_sabotees": ns, "unites_honnetes": nh, **res}
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("batterie_py")
    ap.add_argument("batterie_sortie")
    ap.add_argument("--rep", type=int, default=2000)
    args = ap.parse_args()
    t0 = time.time()
    sortie = {"manifeste": {"script": "contre-verification-pari-signe-v3.py", "entropie_SeedSequence": ENTROPIE,
                            "derivation": "SeedSequence(ENTROPIE, spawn_key=(code de section, indice de configuration))",
                            "codes_sections": CODES, "repetitions_de_base": args.rep, "python": sys.version.split()[0],
                            "numpy": np.__version__, "plateforme": platform.platform(),
                            "monde": {"MU": round(MU, 5), "z_0.99": round(Z99, 5), "z_0.95": round(Z95, 5),
                                      "grille": LAMBDAS.tolist(), "seuil": SEUIL, "alpha": ALPHA}}}
    sortie["A_student_et_reechantillonnage"] = section_A(args.batterie_py, args.batterie_sortie, args.rep)
    sortie["B_controle_20_generations"] = section_B(args.rep)
    sortie["C_H2b_facteur_un_demi"] = section_C(args.rep)
    sortie["D_temoin_faux_asymetrique"] = section_D(args.rep)
    sortie["E_selection_entre_generations"] = section_E(args.rep)
    sortie["manifeste"]["duree_secondes"] = round(time.time() - t0, 1)
    json.dump(sortie, sys.stdout, ensure_ascii=False, indent=1)
    sys.stdout.write("\n")


if __name__ == "__main__":
    main()
