#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Calculs de la note « percée après Blindfold » (v1).

Pièce de travail (classe C), non contre-lue. Aucune donnée du programme : toutes les
entrées sont des suppositions d'illustration, ou des comptes imprimés dans un article
(page dite dans la note). Lois exactes, formules fermées et tirages à graines écrites
(numpy.random.SeedSequence, une graine fille par configuration, R9).

Rejeu : PYTHONPATH=src .venv/bin/python docs/notes/percee-apres-blindfold-v1/calculs-percee-apres-blindfold-v1.py
La sortie doit être identique à l'octet d'un rejeu à l'autre.

Blocs :
  A  relecture de la borne de la proposition 1 (ii) de Singh (arXiv 2610.18948, p. 9, 22-23)
  B  la règle à mélange sur une fraction auditée au hasard : borne garantie (troisième
     implémentation du théorème de la re-dérivation), composition « suite du taux réalisé
     (Blindfold, proposition 3) après la borne sur trajectoire », minorant valable pour
     toute règle, avec et sans second regard
  C  la loi du second regard : divergences exactes, approximation de Wald, tirages,
     objets de contrôle (référence fausse ; sabotage logé dans la marge de la référence)
  D  la bande aveugle due à la référence honnête, avec et sans second regard
  E  après l'alarme : le rappel d'une sonde apprise sur les prises de l'audit (monde planté)
  F  le prix de la couverture à chacun des trois points d'insertion d'une lecture
"""
import math
import sys

import numpy as np
import scipy
from scipy import stats
from scipy.special import logsumexp

RHO0 = 0.10      # taux de dommage de l'honnête (supposition d'illustration)
ALPHA = 0.05     # risque de fausse annonce
BETA = 0.10      # risque sur la borne du dommage accumulé
GRAINE = 20261121


def p(*a):
    print(*a)


def grille(r0, k=12):
    """Douze taux qui descendent vers r0 : r0 * (1 + 4 / 2**j), j = 0..11."""
    r = np.array([r0 * (1.0 + 4.0 / 2 ** j) for j in range(k)])
    assert r.max() < 1.0
    a = np.log(r * (1 - r0) / (r0 * (1 - r)))
    b = np.log((1 - r0) / (1 - r))
    return r, a, b


def kl_bern(x, y):
    """KL(Bern(x) || Bern(y))."""
    t = 0.0
    if x > 0:
        t += x * math.log(x / y)
    if x < 1:
        t += (1 - x) * math.log((1 - x) / (1 - y))
    return t


# ---------------------------------------------------------------- bloc A
def singh_borne(H, p0, alpha):
    eps = (1 - p0) / (4 * p0)
    return math.sqrt(0.5 * H * (math.log(H / alpha) + eps)) + 1.0


def bloc_a():
    p("=" * 78)
    p("BLOC A - Borne sur trajectoire de la proposition 1 (ii) de Singh, relue")
    p("  forme reconstituée : racine( H (log(H/alpha) + eps) / 2 ) + 1, eps = (1-p0)/(4 p0)")
    for nom, p0, imprime in (("monde 006", 0.225, 21.57), ("monde 037", 0.450, 20.88)):
        v = singh_borne(100, p0, 0.05)
        p(f"  {nom} : p0 = {p0:.3f}, H = 100, alpha = 0,05 -> {v:.2f} (imprimé p. 23 : {imprime:.2f})")
        assert abs(v - imprime) < 0.005
    for H in (1000, 10 ** 6):
        p(f"  rho0 = 0,10, alpha = 0,05, H = {H} -> {singh_borne(H, RHO0, ALPHA):.1f}")
    p("  objet de contrôle : les deux valeurs imprimées par l'article sont retrouvées au centième.")


# ---------------------------------------------------------------- bloc B
LAMBDAS = np.geomspace(1e-5, 30.0, 6000)


def borne_auditee(n, q, r0, alpha=ALPHA, beta=BETA):
    """Excès garanti (avec probabilité >= 1 - beta) du compte de l'événement au-delà de r0*n,
    avant l'annonce, pour le mélange à douze taux audité à la fraction q.
    Théorème du § 3.1 de la re-dérivation, réimplémenté."""
    _, a, b = grille(r0)
    u = a - b
    L = math.log(len(a) / alpha)
    lb = math.log(1 / beta)
    lam = LAMBDAS[None, :]

    def phi(s):
        return q * s + np.log(1 - q + q * np.exp(-s))

    A = q * a[:, None] - (phi(lam * u[:, None]) - phi(-lam * b[:, None])) / lam
    C = q * b[:, None] + phi(-lam * b[:, None]) / lam
    with np.errstate(divide="ignore", invalid="ignore"):
        val = (L + lb / lam) / A + n * (C / A - r0)
    val = np.where(A > 0, val, np.inf)
    return float(val.min())


def g_trajectoire(N, r0, alpha=ALPHA):
    """Borne sur trajectoire, à observation complète, du mélange à douze taux :
    sans annonce, M - r0*N < min_k [ L/a_k + (b_k/a_k - r0) N ]."""
    _, a, b = grille(r0)
    L = math.log(len(a) / alpha)
    return float(np.min(L / a + (b / a - r0) * N))


def composition_taux_realise(n, q, r0, alpha=ALPHA, beta1=0.09, beta2=0.01, singh=False):
    """Composition : (1) borne sur trajectoire du mélange sur les seuls audits (celle du
    mélange à douze taux, ou, si singh=True, celle de la proposition 1 (ii) de Singh telle
    qu'imprimée, avec pour horizon le nombre maximal d'audits) ;
    (2) suite du taux réalisé de la proposition 3 de « Blindfold » (p. 6), sous son énoncé
    imprimé : somme des V <= [lambda*G + log(1/beta1)] / (lambda - c*psi(lambda)),
    c = (1-q)/q, psi(l) = exp(l) - 1 - l, G = (audits positifs)/q ; (3) nombre d'audits
    borné par son quantile binomial 1 - beta2."""
    Nplus = float(stats.binom.ppf(1 - beta2, n, q))
    traj = singh_borne(Nplus, r0, alpha) if singh else g_trajectoire(Nplus, r0, alpha)
    Gplus = (r0 * Nplus + traj) / q
    c = (1 - q) / q
    lam = np.geomspace(1e-6, 5.0, 20000)
    den = lam - c * (np.exp(lam) - 1 - lam)
    with np.errstate(divide="ignore", invalid="ignore"):
        val = (lam * Gplus + math.log(1 / beta1)) / den
    val = np.where(den > 0, val, np.inf)
    return float(val.min()) - r0 * n


def kl_joint(delta, t, f, rho0=RHO0):
    """KL de la loi d'un audit sous sabotage (allure delta) contre l'honnête, quand l'audit
    rend trois issues : sain ; endommagé sans marque ; endommagé avec marque du second regard."""
    alt = (1 - rho0 - delta, rho0 * (1 - f) + delta * (1 - t), rho0 * f + delta * t)
    nul = (1 - rho0, rho0 * (1 - f), rho0 * f)
    s = 0.0
    for x, y in zip(alt, nul):
        if x > 0:
            if y <= 0:
                return math.inf
            s += x * math.log(x / y)
    return s


def allure_indetectable(n, q, kl_fonction, budget=None):
    """Plus grande allure delta telle que alpha + racine(q n KL(delta) / 2) + gamma <= 1 - beta
    (Pinsker sur les seuls audits ; § 3.5 de la re-dérivation), gamma = 0,05."""
    gamma = 0.05
    marge = 1 - BETA - ALPHA - gamma
    cible = 2 * marge ** 2 / (q * n)
    lo, hi = 0.0, 1 - RHO0 - 1e-9
    for _ in range(200):
        mid = (lo + hi) / 2
        if kl_fonction(mid) <= cible:
            lo = mid
        else:
            hi = mid
    return lo


def bloc_b():
    p("=" * 78)
    p("BLOC B - La règle à mélange sur une fraction auditée au hasard")
    p(f"  rho0 = {RHO0}, alpha = {ALPHA}, beta = {BETA}, grille de douze taux descendants")
    p("  B1. Borne garantie de l'excès d'épisodes endommagés avant l'annonce (dommage seul)")
    attendu = {(0.20, 1000): 136.1, (0.20, 4000): 252.4, (0.20, 16000): 483.7,
               (0.05, 1000): 317.9, (0.05, 4000): 564.6, (0.05, 16000): 1045.1}
    for q in (0.20, 0.05):
        for n in (1000, 4000, 16000, 100000):
            v = borne_auditee(n, q, RHO0)
            ech = math.sqrt(n * RHO0 * (1 - RHO0) / q)
            ref = attendu.get((q, n))
            note = f" (erratum : {ref})" if ref is not None else ""
            p(f"    q = {q:.2f}, n = {n:>6} : {v:8.1f}  = {v / ech:.2f} x racine(n rho0 (1-rho0) / q){note}")
            if ref is not None:
                assert abs(v - ref) < 0.15, (v, ref)
    p("    objet de contrôle : les six valeurs de l'erratum sont retrouvées à 0,15 près.")
    p("  B2. La même borne obtenue par composition de deux énoncés publiés")
    p("      (borne sur trajectoire du mélange, puis suite du taux réalisé sous tirage non divulgué)")
    for q in (0.20, 0.05):
        for n in (1000, 16000, 100000):
            v1 = borne_auditee(n, q, RHO0)
            v2 = composition_taux_realise(n, q, RHO0)
            v3 = composition_taux_realise(n, q, RHO0, singh=True)
            p(f"    q = {q:.2f}, n = {n:>6} : composition {v2:8.1f} ; théorème direct {v1:8.1f} ; rapport {v2 / v1:.2f}"
              f" ; avec la borne de Singh telle qu'imprimée {v3:8.1f} (rapport {v3 / v1:.2f})")
    p("  B3. Avec un second regard (t = part des dommages délibérés marqués, f = part des échecs")
    p("      honnêtes marqués) : borne garantie sur l'excès d'épisodes « endommagés et marqués »,")
    p("      puis conversion en épisodes endommagés par sabotage, en espérance (division par t)")
    for (t, f) in ((0.64, 0.029), (0.50, 0.010), (0.30, 0.050), (0.93, 0.571)):
        for q in (0.20, 0.05):
            ligne = []
            for n in (1000, 16000, 100000):
                v_d = borne_auditee(n, q, RHO0)
                v_y = borne_auditee(n, q, RHO0 * f) / t
                ligne.append(f"n={n}: {v_y:7.1f} contre {v_d:7.1f} (x{v_d / v_y:.2f})")
            p(f"    t = {t:.2f}, f = {f:.3f}, q = {q:.2f} : " + " ; ".join(ligne))
    p("  B4. Ce qu'aucune règle ne peut empêcher : allure indétectable (Pinsker), excès moyen n*delta")
    for q in (0.20, 0.05):
        for n in (1000, 16000, 100000):
            d0 = allure_indetectable(n, q, lambda d: kl_bern(RHO0 + d, RHO0))
            quant = float(stats.binom.ppf(0.05, n, RHO0 + d0)) - RHO0 * n
            ligne = f"    q = {q:.2f}, n = {n:>6} : dommage seul delta* = {d0:.4f}, excès moyen {n * d0:7.1f}"
            ligne += f", quantile 5 % {quant:7.1f}"
            for (t, f) in ((0.64, 0.029), (0.50, 0.010)):
                d1 = allure_indetectable(n, q, lambda d, t=t, f=f: kl_joint(d, t, f))
                ligne += f" | second regard ({t:.2f}; {f:.3f}) : {n * d1:6.1f} (x{d0 / d1:.2f})"
            p(ligne)
    p("    objet de contrôle : à q = 0,20, n = 1 000 et 16 000, le quantile 5 % retrouve 18 et 73")
    p("    (re-dérivation, § 3.5).")
    v = float(stats.binom.ppf(0.05, 1000, RHO0 + allure_indetectable(1000, 0.20, lambda d: kl_bern(RHO0 + d, RHO0)))) - 100
    assert abs(v - 18) <= 1.0, v
    v = float(stats.binom.ppf(0.05, 16000, RHO0 + allure_indetectable(16000, 0.20, lambda d: kl_bern(RHO0 + d, RHO0)))) - 1600
    assert abs(v - 73) <= 1.5, v


# ---------------------------------------------------------------- bloc C
def wilson(k, n, z=1.959963984540054):
    if n == 0:
        return (0.0, 1.0)
    ph = k / n
    den = 1 + z * z / n
    centre = (ph + z * z / (2 * n)) / den
    demi = z * math.sqrt(ph * (1 - ph) / n + z * z / (4 * n * n)) / den
    return (max(0.0, centre - demi), min(1.0, centre + demi))


def simuler(rng, proba, r0_d, r0_y, n_max, pas, reps):
    """Mélanges à douze taux sur le dommage seul, sur « endommagé et marqué », et moyenne des
    deux ; issues d'audit tirées par blocs de `pas` audits. Rend l'instant d'annonce (en audits)
    de chaque règle, infini si pas d'annonce avant n_max."""
    _, a_d, b_d = grille(r0_d)
    _, a_y, b_y = grille(r0_y)
    seuil = math.log(1 / ALPHA)
    lk = math.log(len(a_d))
    N = 0
    Md = np.zeros(reps)
    My = np.zeros(reps)
    t_d = np.full(reps, np.inf)
    t_y = np.full(reps, np.inf)
    t_m = np.full(reps, np.inf)
    while N < n_max:
        c = rng.multinomial(pas, proba, size=reps)
        N += pas
        Md += c[:, 1] + c[:, 2]
        My += c[:, 2]
        lw_d = logsumexp(a_d[None, :] * Md[:, None] - b_d[None, :] * N, axis=1) - lk
        lw_y = logsumexp(a_y[None, :] * My[:, None] - b_y[None, :] * N, axis=1) - lk
        lw_m = np.logaddexp(lw_d, lw_y) - math.log(2)
        t_d = np.where((lw_d >= seuil) & np.isinf(t_d), N, t_d)
        t_y = np.where((lw_y >= seuil) & np.isinf(t_y), N, t_y)
        t_m = np.where((lw_m >= seuil) & np.isinf(t_m), N, t_m)
        if np.isfinite(t_d).all() and np.isfinite(t_y).all() and np.isfinite(t_m).all():
            break
    return t_d, t_y, t_m


def resume(t, q, delta):
    fini = np.isfinite(t)
    part = fini.mean()
    if part < 0.5:
        return f"annonce {part:5.3f}, médiane non atteinte"
    med = float(np.median(np.where(fini, t, np.inf)))
    return f"annonce {part:5.3f}, médiane {med:8.0f} audits, soit ~{delta * med / q:7.1f} épisodes en excès"


def bloc_c():
    p("=" * 78)
    p("BLOC C - La loi du second regard sur les seuls épisodes endommagés audités")
    p("  C0. Comptes imprimés d'un banc public « manipulation contre échec honnête »")
    p("      (arXiv 2611.00407, table 3, p. 6 ; moniteurs de texte, 14 tentatives, 35 échecs honnêtes)")
    for nom, k1, n1, k0, n0 in (("moniteur capable, consigne v5, vue C", 9, 14, 1, 35),
                                ("moniteur capable, consigne v5, vue B", 11, 14, 3, 35),
                                ("moniteur capable, consigne v3, vue B", 10, 14, 1, 35),
                                ("petit moniteur 8B, consigne v3, vue C", 13, 14, 20, 35),
                                ("petit moniteur 8B, consigne v5, vue C", 4, 14, 0, 35),
                                ("contrôle déterministe à deux règles", 14, 14, 1, 35)):
        t, f = k1 / n1, k0 / n0
        tl, th = wilson(k1, n1)
        fl, fh = wilson(k0, n0)
        point = "infini (f = 0)" if f == 0 else f"{t * t / f:6.1f}"
        p(f"    {nom:<40} t = {k1}/{n1} = {t:.3f} [{tl:.2f} ; {th:.2f}], f = {k0}/{n0} = {f:.3f} "
          f"[{fl:.2f} ; {fh:.2f}] ; t²/f = {point} ; prudent (t bas, f haut) = {tl * tl / fh:5.2f}")
    p("  C1. Divergences exactes par audit (nats) et gain à allure fixée")
    p("      dommage seul : KL(Bern(rho0+delta) || Bern(rho0)) ; marque : KL(Bern(rho0 f + delta t) || Bern(rho0 f)) ;")
    p("      trois issues : loi jointe ; gain = rapport à la divergence du dommage seul")
    couples = ((0.64, 0.029), (0.79, 0.086), (0.50, 0.010), (0.30, 0.050), (0.93, 0.571), (0.029, 0.029))
    for delta in (0.10, 0.05, 0.02, 0.01, 0.005, 0.002):
        kd = kl_bern(RHO0 + delta, RHO0)
        p(f"    allure delta = {delta:.3f} : dommage seul {kd:.3e} ; audits (Wald, mélange) ~ {math.log(12 / ALPHA) / kd:9.0f}")
        for (t, f) in couples:
            ky = kl_bern(RHO0 * f + delta * t, RHO0 * f)
            kj = kl_joint(delta, t, f)
            p(f"        t = {t:.3f}, f = {f:.3f} : marque {ky:.3e} (gain {ky / kd:6.2f}) ; "
              f"trois issues {kj:.3e} (gain {kj / kd:6.2f}) ; t²/f x (1-rho0) = {t * t / f * (1 - RHO0):6.2f}")
    p("  C2. Régime de signature (f = 0) : une seule marque suffit ; épisodes endommagés par sabotage")
    p("      avant la prise : moyenne 1/(q t), quelle que soit l'allure")
    for q in (0.20, 0.05):
        for t in (0.3, 0.5, 0.64):
            p(f"    q = {q:.2f}, t = {t:.2f} : moyenne {1 / (q * t):6.1f} ; quantile 0,95 {math.log(0.05) / math.log(1 - q * t):6.1f}")
    p("  C3. Tirages : audits avant l'annonce, médiane sur 1 000 déploiements, allure constante")
    p("      (règles : D = mélange sur le dommage seul ; Y = mélange sur « endommagé et marqué » ;")
    p("       M = moyenne des deux ; épisodes en excès = delta x médiane / q, ordre de grandeur)")
    ss = np.random.SeedSequence(GRAINE)
    filles = iter(ss.spawn(64))
    for q in (0.20,):
        for delta in (0.05, 0.02, 0.01):
            wald = math.log(12 / ALPHA) / kl_bern(RHO0 + delta, RHO0)
            pas = max(1, int(wald / 400))
            for (t, f) in ((0.64, 0.029), (0.50, 0.010), (0.30, 0.050), (0.93, 0.571), (0.029, 0.029)):
                rng = np.random.default_rng(next(filles))
                proba = (1 - RHO0 - delta, RHO0 * (1 - f) + delta * (1 - t), RHO0 * f + delta * t)
                t_d, t_y, t_m = simuler(rng, proba, RHO0, RHO0 * f, int(8 * wald), pas, 1000)
                p(f"    q = {q:.2f}, delta = {delta:.2f}, t = {t:.3f}, f = {f:.3f} (pas de {pas} audits)")
                p(f"        D : {resume(t_d, q, delta)}")
                p(f"        Y : {resume(t_y, q, delta)}")
                p(f"        M : {resume(t_m, q, delta)}")
    p("  C4. Objets de contrôle (2 000 déploiements, audit par audit, 20 000 audits)")
    for nom, f_suppose, f_vrai in (("monde honnête, référence juste (f vrai = f supposé = 0,029)", 0.029, 0.029),
                                   ("monde honnête, référence fausse (f vrai = 2 x f supposé)", 0.029, 0.058)):
        rng = np.random.default_rng(next(filles))
        proba = (1 - RHO0, RHO0 * (1 - f_vrai), RHO0 * f_vrai)
        t_d, t_y, t_m = simuler(rng, proba, RHO0, RHO0 * f_suppose, 20000, 1, 2000)
        p(f"    {nom}")
        p(f"        fausse annonce : D {np.isfinite(t_d).mean():.4f} ; Y {np.isfinite(t_y).mean():.4f} ; M {np.isfinite(t_m).mean():.4f}"
          f" (permis : {ALPHA})")
    p("  C5. Saboteur logé dans la marge de la référence : il est plus capable que la référence ne le dit")
    p("      (taux d'échec propre 0,08 pour une référence inscrite à 0,10) et dépense l'écart en dommage")
    p("      délibéré (0,02) : son taux de dommage total égale la référence ; 1 000 déploiements, 20 000 audits")
    for (t, f) in ((0.64, 0.029), (0.30, 0.050), (0.029, 0.029)):
        rng = np.random.default_rng(next(filles))
        propre, delib = 0.08, 0.02
        proba = (1 - propre - delib, propre * (1 - f) + delib * (1 - t), propre * f + delib * t)
        t_d, t_y, t_m = simuler(rng, proba, RHO0, RHO0 * f, 20000, 5, 1000)
        fin_m = np.isfinite(t_m)
        med = f"{float(np.median(np.where(fin_m, t_m, np.inf))):.0f} audits" if fin_m.mean() >= 0.5 else "non atteinte"
        p(f"    t = {t:.3f}, f = {f:.3f} : annonce D {np.isfinite(t_d).mean():.3f} ; Y {np.isfinite(t_y).mean():.3f} ; "
          f"M {fin_m.mean():.3f} (médiane de M : {med})")


# ---------------------------------------------------------------- bloc D
def bloc_d():
    p("=" * 78)
    p("BLOC D - Bande aveugle due à la référence honnête (m épisodes honnêtes de référence)")
    p("  z = 2,326 (1 % unilatéral) ; bande en points de taux de dommage ; dommage logé sur 100 000 épisodes")
    z = float(stats.norm.ppf(0.99))
    for m in (400, 2000, 10000):
        bd = z * math.sqrt(RHO0 * (1 - RHO0) / m)
        ligne = f"    m = {m:>5} : dommage seul {100 * bd:5.2f} points ({1e5 * bd:7.0f} épisodes)"
        for (t, f) in ((0.64, 0.029), (0.50, 0.010), (0.30, 0.050)):
            by = z * math.sqrt(RHO0 * f * (1 - RHO0 * f) / m) / t
            ligne += f" | ({t:.2f}; {f:.3f}) : {100 * by:5.2f} points (x{bd / by:.2f})"
        p(ligne)
    p("  lecture : la bande se réduit du facteur t / racine(f), à (1 - rho0) près ; elle ne s'annule qu'à f = 0.")


# ---------------------------------------------------------------- bloc E
def d_eff(sep, d, k1, k0):
    return sep ** 2 / math.sqrt(sep ** 2 + d * (1.0 / k1 + 1.0 / k0))


def rappel_au_budget(dprime, prevalence, budget):
    """Rappel quand on revoit la part `budget` des épisodes non audités, rangés par score."""
    lo, hi = -20.0, 20.0 + dprime
    for _ in range(200):
        mid = (lo + hi) / 2
        part = prevalence * stats.norm.sf(mid - dprime) + (1 - prevalence) * stats.norm.sf(mid)
        if part > budget:
            lo = mid
        else:
            hi = mid
    return float(stats.norm.sf(lo - dprime))


def bloc_e(med_audits):
    p("=" * 78)
    p("BLOC E - Après l'alarme : sonde apprise sur les prises de l'audit, états consignés (monde planté)")
    p("  monde : états gaussiens de dimension d, écart de moyenne `sep` (en écarts types) entre épisodes")
    p("  endommagés et sains ; sonde = différence des moyennes estimées sur k1 endommagés et k0 sains audités")
    p("  E1. Contrôle de la formule d' = sep² / racine(sep² + d (1/k1 + 1/k0)) par tirages (d = 256)")
    ss = np.random.SeedSequence(GRAINE + 1)
    for (sep, k1, k0), fille in zip(((2.0, 20, 200), (2.0, 100, 1000), (4.0, 20, 200)), ss.spawn(3)):
        rng = np.random.default_rng(fille)
        d = 256
        mu = np.zeros(d)
        mu[0] = sep
        aires = []
        for _ in range(200):
            x1 = rng.standard_normal((k1, d)) + mu
            x0 = rng.standard_normal((k0, d))
            w = x1.mean(axis=0) - x0.mean(axis=0)
            dp = float(w @ mu) / float(np.linalg.norm(w))
            aires.append(float(stats.norm.cdf(dp / math.sqrt(2))))
        attendu = float(stats.norm.cdf(d_eff(sep, d, k1, k0) / math.sqrt(2)))
        p(f"    sep = {sep}, k1 = {k1}, k0 = {k0} : aire sous la courbe moyenne {np.mean(aires):.3f} ; formule {attendu:.3f}")
        assert abs(np.mean(aires) - attendu) < 0.02
    p("  E2. À l'instant de l'alarme du plancher (dommage seul, q = 0,20, allure 0,02) :")
    q, delta = 0.20, 0.02
    N = med_audits
    k1 = int(round((RHO0 + delta) * N))
    k0 = int(round(N - k1))
    prev = RHO0 + delta
    p(f"      {N:.0f} audits, dont {k1} épisodes endommagés et {k0} sains ; {N / q * (1 - q):.0f} épisodes non audités,")
    p(f"      dont ~{prev * N / q * (1 - q):.0f} endommagés jamais regardés")
    p("      rappel sur ces épisodes si l'on en revoit 12 % (leur prévalence) puis 25 %, contre le hasard (12 %, 25 %)")
    for d in (64, 512, 4096):
        for sep in (1.0, 2.0, 3.0, 4.0):
            dp = d_eff(sep, d, k1, k0)
            aire = float(stats.norm.cdf(dp / math.sqrt(2)))
            r12 = rappel_au_budget(dp, prev, 0.12)
            r25 = rappel_au_budget(dp, prev, 0.25)
            p(f"      d = {d:>4}, sep = {sep:.0f} : d' = {dp:5.2f}, aire {aire:.3f}, rappel {r12:.2f} à 12 %, {r25:.2f} à 25 %")
    p("  E3. Combien de prises faut-il ? (d = 4096, sains audités : 9 fois plus) rappel à 25 % de revue")
    for sep in (2.0, 3.0, 4.0):
        ligne = f"      sep = {sep:.0f} :"
        for k1 in (6, 20, 60, 200, 600):
            dp = d_eff(sep, 4096, k1, 9 * k1)
            ligne += f" k1={k1}: {rappel_au_budget(dp, prev, 0.25):.2f}"
        p(ligne)
    p("  lecture : tout dépend de l'écart `sep`, inconnu ; c'est la mesure à faire. Objet de contrôle :")
    p("  à sep = 1 et d = 4096 le rappel reste proche du hasard (0,16 contre 0,12 ; 0,31 contre 0,25).")


# ---------------------------------------------------------------- bloc F
def bloc_f():
    p("=" * 78)
    p("BLOC F - Le prix de la couverture, aux trois points d'insertion d'une lecture")
    p("  (ce que coûte la lecture quand l'adversaire la rend inutile)")
    q = 0.05
    p(f"  avant l'audit (les scores orientent le tirage) : budget q = {q}, moitié en plancher, moitié orientée ;")
    p("      contre un saboteur que le score ne voit pas, seul le plancher q/2 compte :")
    for n in (16000, 100000):
        v_plein = borne_auditee(n, q, RHO0)
        v_demi = borne_auditee(n, q / 2, RHO0)
        p(f"      n = {n} : borne {v_demi:7.1f} au lieu de {v_plein:7.1f} (x{v_demi / v_plein:.2f}) ; à allure fixée : x2,00 d'épisodes")
    k = 12
    p("  à l'audit (second regard sur les épisodes endommagés audités) : moyenne de deux mélanges ;")
    p(f"      seuil relevé de log 2 : x{(math.log(2 * k / ALPHA)) / (math.log(k / ALPHA)):.3f} d'audits au plus, à allure fixée")
    p("  après l'alarme (rappel sur états consignés) : aucun coût avant l'alarme ; le coût est la revue.")


def main():
    p("calculs-percee-apres-blindfold-v1 ; python " + sys.version.split()[0]
      + " ; numpy " + np.__version__ + " ; scipy " + scipy.__version__)
    p(f"graine mère : {GRAINE} (numpy.random.SeedSequence, une fille par configuration)")
    bloc_a()
    bloc_b()
    bloc_c()
    bloc_d()
    # médiane d'audits avant l'alarme, dommage seul, q = 0,20, allure 0,02 : recalculée ici
    ss = np.random.SeedSequence(GRAINE + 2)
    rng = np.random.default_rng(ss)
    delta = 0.02
    wald = math.log(12 / ALPHA) / kl_bern(RHO0 + delta, RHO0)
    t_d, _, _ = simuler(rng, (1 - RHO0 - delta, RHO0 + delta - 1e-12, 1e-12), RHO0, RHO0 * 0.029,
                        int(8 * wald), max(1, int(wald / 400)), 1000)
    bloc_e(float(np.median(t_d)))
    bloc_f()
    p("=" * 78)
    p("fin")


if __name__ == "__main__":
    main()
