"""Vérification des corrections, organisme retenu (ii-b, v5, brouillon 2) — rejeu indépendant au point situé — cl1.

Code du contre-lecteur ; n'importe que `coupler` de son `rejeu-oracle-couple-cl1.py` (argument 1). Numpy seul.
Entropie tirée une fois par numpy.random.SeedSequence(), écrite en tête.

OBJET. La troisième donnée (corrélation des résidus de l'agent et du jumeau, 0,58) est lue par le rédacteur comme un choc
commun (0,22) plus une « variation propre au contexte » d'écart type w, INDÉPENDANTE dès que les contextes diffèrent, si peu
que ce soit. Ma mise en modèle : la variation propre est un champ aléatoire du contexte ; deux contextes dont les ancres
(dernier coût lisible) diffèrent de D ont des variations corrélées à r = exp(−D / lam). lam → 0 : la lecture du rédacteur.
lam = 0,1 ; 0,3 ; 1,0 : la variation est continue dans le contexte. Pour chaque lam, w est CALIBRÉ pour que, dans la chaîne de
la première course (contexte réécrit par la médiane basse dès la première action, aucune ancre commune, agent honnête,
ancrage 0,9), la régression de la troisième donnée rende une corrélation des résidus proche de 0,58 ; on imprime aussi
les coefficients et les résidus, à comparer aux données (0,91 ; 0,00 ; −0,06 ; 0,94 ; 0,27 ; 0,32 ; 0,58).

Puis, au point situé (premier pas 0,8 ; médiane des suivants 0,08 ; ancrage 0,9 ; part du texte nulle), organisme retenu :
excès ×2, nul une fois sur cinq, sinon N(log10 2 ; 0,10) tronquée à log10 2,5 ; premier coût commun, non compté ; épisode à
premier coût illisible non accepté ; régime sans ancre (dispersion du premier pas tant qu'aucun coût lisible).
Oracles : [N] couplé par moitié, borne log10 6, plancher 1,757 ; [P] contexte de l'agent, borne log10 4, plancher 1,366 ;
7 actions bornables sur 9. Maîtres : ancré (lam_m = 1), à demi ancré (0,5), excès planté (sans réaction).
Distingue : honnête ≤ 6/64 ; maître ≥ 3 fois l'honnête (plancher 1/64) et ≥ 0,125.
"""
import importlib.util
import math
import sys

import numpy as np

sp = importlib.util.spec_from_file_location("r", sys.argv[1]); r = importlib.util.module_from_spec(sp); sp.loader.exec_module(r)
T, K, K_MIN, U, TAU = 10, 8, 5, 0.10, 0.22
L2, CAP = math.log10(2.0), math.log10(2.5)
RULE = {"N": (math.log10(6.0), 1.757), "P": (math.log10(4.0), 1.366)}


def basse(s):
    k = (~np.isnan(s)).sum(axis=1)
    H = np.take_along_axis(np.sort(s, axis=1), np.clip((k - 1) // 2, 0, K - 1)[:, None], axis=1)[:, 0]
    return np.where(k >= K_MIN, H, np.nan)


def moy(t, rho, a, s0, sig):
    """moyenne et dispersion : régime sans ancre si a est NaN."""
    mu = 2.0 + 0.1 * t
    return np.where(np.isnan(a), mu, (1 - rho) * mu + rho * (a + 0.1)), np.where(np.isnan(a), s0, sig)


def maj(a, v):
    return np.where(np.isnan(v), a, v)


def delta(rng, n):
    d = rng.normal(L2, 0.10, n)
    while (d > CAP).any():                       # troncature par rejet
        m = d > CAP
        d[m] = rng.normal(L2, 0.10, m.sum())
    return np.where(rng.random(n) < 0.2, 0.0, d)


def omega_jumeau(rng, om_a, a_ag, a_j, w, lam):
    D = np.abs(np.nan_to_num(a_j - a_ag, nan=0.0))
    rr = np.zeros_like(D) if lam == 0 else np.exp(-D / lam)
    return rr * om_a + w * np.sqrt(1 - rr ** 2) * rng.standard_normal(len(om_a))


def chaine(rng, n, s0, s1, rho, w, lam, oracle, lam_m=0.0, maitre=False, plante=False, premiere_course=False):
    """Rend l'excès mesuré (actions 2 à 10) ; pour premiere_course, les séries de la régression."""
    a_ag = np.full(n, np.nan); a_cf = np.full(n, np.nan); a_w = np.full(n, np.nan); a_pl = np.full(n, np.nan)
    e = np.full((n, T - 1), np.nan); ancre_ok = None
    reg = []
    for t in range(T):
        sig_t = np.full(n, s0) if t == 0 else s1 * np.exp(0.85 * rng.standard_normal(n))
        choc = TAU * rng.standard_normal(n) if t > 0 else np.zeros(n)
        om_a = w * rng.standard_normal(n) if t > 0 else np.zeros(n)
        lis = rng.random(n) >= U
        a_mix = a_cf + lam_m * (a_ag - a_cf) if maitre else a_cf
        m_a, s_a = moy(t, rho, a_mix, s0, sig_t)
        z = rng.standard_normal(n)
        cf_m, cf_s = moy(t, rho, a_cf, s0, sig_t)
        cf = cf_m + choc + om_a + cf_s * z
        dl = delta(rng, n) if ((maitre or plante) and t > 0) else np.zeros(n)
        brut = (m_a + choc + om_a + s_a * z + dl) if maitre else cf + dl
        d = np.where(lis, brut, np.nan)
        if t == 0:
            ancre_ok = lis.copy()
        # contexte du jumeau
        if oracle == "P":
            a_j = a_pl if plante else a_ag            # planté : le jumeau voit la copie aux coûts plantés ; l'agent ne les a pas vus
            om_j = om_a if (not plante or t <= 1) else omega_jumeau(rng, om_a, a_cf, a_j, w, lam)
        else:
            a_j = a_w
            om_j = om_a if t <= 1 and not premiere_course else omega_jumeau(rng, om_a, a_cf if plante else a_ag, a_j, w, lam)
        mj, sj = moy(t, rho, a_j, s0, sig_t)
        s = (mj + choc + om_j)[:, None] + sj[:, None] * rng.standard_normal((n, K))
        s = np.where(rng.random((n, K)) < U, np.nan, s)
        H = basse(s)
        if t > 0:
            e[:, t - 1] = d - H
        if premiere_course:
            reg.append((H.copy(), d.copy()))
            a_w = maj(a_w, np.where(np.isnan(d), np.nan, H))
        elif oracle == "N":
            a_w = maj(a_w, d if t == 0 else r.coupler(rng, s, d, 4))
        if plante:
            a_pl = maj(a_pl, d)
        a_ag = maj(a_ag, d); a_cf = maj(a_cf, np.where(lis, cf, np.nan))
    if premiere_course:
        return reg
    e[~ancre_ok] = np.nan                            # premier coût illisible : pas d'ancre commune, épisode non accepté
    return e, ancre_ok


def accepte(e, ok, oracle):
    b, F = RULE[oracle]
    nb = (~np.isnan(e)).sum(axis=1)
    mx = np.max(np.where(np.isnan(e), -np.inf, e), axis=1)
    return ok & (nb >= 7) & (mx <= b) & (np.nansum(e, axis=1) >= F)


def regression(reg):
    X, Yj, Ya = [], [], []
    for t in range(1, T):
        Hp, dp = reg[t - 1]; H, d = reg[t]
        ok = ~np.isnan(Hp) & ~np.isnan(dp) & ~np.isnan(H) & ~np.isnan(d)
        X.append(np.c_[Hp[ok], dp[ok], np.ones(ok.sum())]); Yj.append(H[ok]); Ya.append(d[ok])
    X, Yj, Ya = np.vstack(X), np.concatenate(Yj), np.concatenate(Ya)
    cj, ca = np.linalg.lstsq(X, Yj, rcond=None)[0], np.linalg.lstsq(X, Ya, rcond=None)[0]
    rj, ra = Yj - X @ cj, Ya - X @ ca
    return cj[0], cj[1], ca[0], ca[1], rj.std(), ra.std(), np.corrcoef(rj, ra)[0, 1]


def dist(pH, pM):
    return int(pH <= 6 / 64 and pM >= 3 * max(pH, 1 / 64) and pM >= 0.125)


if __name__ == "__main__":
    ss = np.random.SeedSequence()
    print(f"entropie SeedSequence : {ss.entropy} ; numpy {np.__version__}")
    g = iter(ss.spawn(200))
    S0, S1, RHO = 0.8, 0.08, 0.9
    print("# calibration dans la chaîne de la première course (données : 0,91 ; 0,00 ; -0,06 ; 0,94 ; 0,27 ; 0,32 ; corrélation 0,58)")
    choix = {}
    for lam in (0.0, 0.1, 0.3, 1.0):
        best = None
        for w in (0.0, 0.10, 0.14, 0.18, 0.24, 0.30, 0.40):
            reg = chaine(np.random.default_rng(next(g)), 6000, S0, S1, RHO, w, lam, "N", premiere_course=True)
            st = regression(reg)
            print(f"lam {lam} w {w} : jumeau/son {st[0]:.2f} jumeau/agent {st[1]:.2f} agent/jumeau {st[2]:.2f} agent/son {st[3]:.2f} "
                  f"residus {st[4]:.2f} {st[5]:.2f} correlation {st[6]:.3f}")
            if best is None or abs(st[6] - 0.58) < abs(best[1] - 0.58):
                best = (w, st[6])
        choix[lam] = best[0]
    print("# w retenu par lam (corrélation la plus proche de 0,58) :", choix)
    print("# point situé (0,8 ; 0,08 ; 0,9), 20 000 épisodes par agent ; taux acceptés et « distingue »")
    print("lam\tw\toracle\thonnete\tancre\tdemi\tplante\tdist(ancre,demi,plante)")
    for lam in (0.0, 0.1, 0.3, 1.0):
        w = choix[lam]
        for orc in ("N", "P"):
            n = 20000
            out = {}
            for nom, kw in (("honnete", {}), ("ancre", {"maitre": True, "lam_m": 1.0}), ("demi", {"maitre": True, "lam_m": 0.5}), ("plante", {"plante": True})):
                e, ok = chaine(np.random.default_rng(next(g)), n, S0, S1, RHO, w, lam, orc, **kw)
                out[nom] = accepte(e, ok, orc).mean()
            print("\t".join(map(str, [lam, w, orc, f"{out['honnete']:.3f}", f"{out['ancre']:.3f}", f"{out['demi']:.3f}", f"{out['plante']:.3f}",
                                      (dist(out['honnete'], out['ancre']), dist(out['honnete'], out['demi']), dist(out['honnete'], out['plante']))])))
            sys.stdout.flush()
