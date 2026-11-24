"""Épreuve, près de leur limite, de la garantie de seuil du théorème de mise en œuvre
aléatoire des audits (papier D, chantier 3) — instrument (classe B), version 3.

v3 = v2 + erratum 1 au préenregistrement (deux valeurs de conception exactes, GO-2026-11-24-21).

v2 = v1 + corrections de la contre-lecture du script (défauts 2 à 10 de
papiers/D/audits/contre-lecture-script-seuil-v1/contre-lecture-script-seuil-v1.md).

Préenregistrement scellé qui fait foi : papiers/D/prereg/prereg-seuil-chantier3-v3.md
(empreinte 4f3ee5c3a10b55d3a43a443b1418a006819d6e931f13247785b7afbf655b20e3).
Ce script suit ce texte à la lettre ; toute divergence est un défaut du script.

Modes :
  --gardes   : bancs témoins et essais des gardes (cas sain et artefact, R5), sans grille ;
  --course   : gardes, puis la grille complète ; écrit runs/<id>/manifeste.json et
               diag/<id>/*.json (scellés). Refuse un arbre git non propre et tout écrasement.
Aucune sortie de la grille n'est affichée à la console (lecture réservée au lecteur neuf).
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import sys
import time
from concurrent.futures import ProcessPoolExecutor, as_completed, TimeoutError as FuturTimeout
from pathlib import Path

import numpy as np
from scipy.stats import beta as beta_dist
from scipy.stats import binom, fisher_exact

RACINE = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(RACINE / "src"))

from controle_ia.gardes import GardeArret  # noqa: E402

PREREG = RACINE / "papiers/D/prereg/prereg-seuil-chantier3-v3.md"
PREREG_SHA = "4f3ee5c3a10b55d3a43a443b1418a006819d6e931f13247785b7afbf655b20e3"
ERRATUM = RACINE / "papiers/D/prereg/prereg-seuil-chantier3-v3-erratum-1.md"
ERRATUM_SHA = "411aba8156f166002c4ccb31337c9a36316326b04972e32214be64b092321f25"
ENTROPIE = 202611243003
DR = 1.0
LAMBDAS = (0.0, 0.1, 0.25, 0.5, 0.75, 1.0)
R_LOT = 10_000
N_LOTS = 10
R = R_LOT * N_LOTS
N_LOTS_PROLONG = 100
NIV = 1e-4  # niveau des bornes unilatérales de Clopper-Pearson


# ---------------------------------------------------------------- arithmétique du processus
def tau_de(c: float) -> float:
    return 1e-9 * max(1.0, c)


def a_de(gam: float, eta: float) -> float:
    return 1.0 if math.isinf(eta) else 1.0 - gam / eta


def G(k: int, gam: float, eta: float) -> float:
    a = a_de(gam, eta)
    return gam * sum(a**i for i in range(k))


def gamma_K_ferme(K: int, a: float) -> float:
    return float(K) if a == 1.0 else (1.0 - a ** (2 * K)) / (1.0 - a**2)


def epsilon(K: int, n: int, gam: float, eta: float, C: float, delta: float, gamma_K: float | None = None) -> float:
    W = DR + C
    rbar = DR / W
    a = a_de(gam, eta)
    GK = gamma_K_ferme(K, a) if gamma_K is None else gamma_K
    Lam = math.log(2 * K / delta)
    return gam * W * (math.sqrt(2 * rbar * GK * Lam / n) + 2 * Lam / (3 * n))


def plan_clos(K: int, gam: float, eta: float, C: float, c: float, m: float) -> tuple[np.ndarray, int]:
    """Plan « juste à temps » pour la marge de manœuvre c - m (forme close du texte)."""
    W = DR + C
    tau = tau_de(c)
    cc = c - m
    kap = None
    for k in range(K):
        if DR * G(k + 1, gam, eta) - cc > tau:
            kap = k
            break
    if kap is None:
        raise GardeArret(f"kappa indéfini (aucun tour ne dépasse c - m) : K={K}, c={c}, m={m}")
    rho = np.zeros(K)
    rho[kap] = (DR * G(kap + 1, gam, eta) - cc) / (gam * W)
    hold = (DR - (0.0 if math.isinf(eta) else cc / eta)) / W
    rho[kap + 1:] = hold
    return rho, kap


def plan_glouton(K: int, gam: float, eta: float, C: float, cc: float) -> np.ndarray:
    """Plan glouton de sim() (check_audit_v1.py), boucle ouverte, marge de manœuvre cc."""
    a = a_de(gam, eta)
    S = DR + C
    x = 0.0
    rho = []
    for _ in range(K):
        r = max(0.0, (a * x + gam * DR - cc) / (gam * S))
        rho.append(r)
        x = a * x + gam * DR - gam * S * r
    return np.array(rho)


def trajectoire_mf(K: int, gam: float, eta: float, C: float, rho: np.ndarray) -> np.ndarray:
    a = a_de(gam, eta)
    W = DR + C
    x = np.zeros(K + 1)
    for k in range(K):
        x[k + 1] = a * x[k] + gam * DR - gam * W * rho[k]
    return x


def closed_unif(K, gam, eta, dR, C, c):
    """Forme identité de B*_unif / n (check_audit_v1.py)."""
    a = 1 - gam / eta if np.isfinite(eta) else 1.0
    S = dR + C
    if dR * G(K, gam, eta) <= c:
        return 0.0
    xs = [min(c, dR * G(k, gam, eta)) for k in range(K + 1)]
    return (K * gam * dR - (1 - a) * sum(xs[1:K]) - xs[K]) / (gam * S)


def b_rand(Bm: float, delta: float) -> float:
    L = math.log(2 / delta)
    return Bm + math.sqrt(2 * Bm * L) + 2 * L / 3


# ---------------------------------------------------------------- statistique
def cp_haut(k: int, n: int, niv: float = NIV) -> float:
    return 1.0 if k >= n else float(beta_dist.ppf(1 - niv, k + 1, n - k))


def cp_bas(k: int, n: int, niv: float = NIV) -> float:
    return 0.0 if k <= 0 else float(beta_dist.ppf(niv, k, n - k + 1))


def cp95(k: int, n: int) -> list[float]:
    return [cp_bas(k, n, 0.025), cp_haut(k, n, 0.025)]


def classer(k: int, n: int, s: float) -> str:
    if cp_haut(k, n) <= s:
        return "sous"
    if cp_bas(k, n) > s:
        return "au-dessus"
    return "indetermine"


def tolerance_compte(R_: int, p: float) -> float:
    return 5 * math.sqrt(R_ * p * (1 - p)) + 3


# ---------------------------------------------------------------- graines
# Bancs témoins : le texte fixe i_point 1000-1002, i_bloc 0 (sain) / 1 (artefact), i_rang = indice de
# marge (0-2). Plusieurs essais portent sur la même marge : pour garder toutes les clés distinctes, les
# essais supplémentaires prennent i_rang >= 100 (artefacts du compteur : 100 + 10*variante + marge ;
# autres essais : 200-205) ; l'artefact de l'invariant tire ses audits plafonnés au bloc 2. Écart
# d'interprétation déclaré, consigné au manifeste avec toutes les clés.
class Cles:
    def __init__(self):
        self.vues: set = set()

    def rng(self, i_point: int, i_bloc: int, i_rang: int, i_lot: int) -> np.random.Generator:
        cle = (i_point, i_bloc, i_rang, i_lot)
        if cle in self.vues:
            raise GardeArret(f"clé de graine en double : {cle}")
        self.vues.add(cle)
        ss = np.random.SeedSequence(entropy=ENTROPIE, spawn_key=cle)
        return np.random.Generator(np.random.PCG64(ss))


# ---------------------------------------------------------------- simulateur
def simuler_lot(A: np.ndarray, *, K, n, gam, eta, C, c, rho, kap, x_mf, eps, cap, tau, tau2,
                variante: str = "saine", seuil_D: float | None = None, garder_max: bool = False,
                A_cap: np.ndarray | None = None) -> dict:
    """Récurrences sans plafond et plafonnée sur les mêmes tirages A (R_lot, K).

    `variante` sert aux essais des gardes (artefacts) ; la course n'emploie que « saine »."""
    a = a_de(gam, eta)
    if variante == "sans_memoire":
        a = 0.0
    W = DR + C
    Rl = A.shape[0]
    Ac_src = A if A_cap is None else A_cap
    x = np.zeros(Rl)
    xc = np.zeros(Rl)
    Ncap = np.zeros(Rl, dtype=np.int64)
    maxx = np.full(Rl, -np.inf)
    maxxc = np.full(Rl, -np.inf)
    dev_haut = np.zeros(Rl)
    dev_bas = np.zeros(Rl)
    premier = None
    for k in range(K):
        x = a * x + gam * DR - gam * W * A[:, k] / n
        if variante == "plafond_par_tour":
            Ak = np.minimum(Ac_src[:, k], cap)
        elif variante == "ignore_plafond":
            Ak = Ac_src[:, k]
        else:
            Ak = np.minimum(Ac_src[:, k], cap - Ncap)
        Ncap += Ak
        xc = a * xc + gam * DR - gam * W * Ak / n
        maxx = np.maximum(maxx, x)
        maxxc = np.maximum(maxxc, xc)
        d = x - x_mf[k + 1]
        dev_haut = np.maximum(dev_haut, d)
        dev_bas = np.maximum(dev_bas, -d)
        if k == kap:
            premier = x.copy()
    if not (np.all(np.isfinite(maxx)) and np.all(np.isfinite(maxxc))):
        raise GardeArret("valeur non finie dans la récurrence")
    N = A.sum(axis=1)
    seuil = c if variante != "seuil_c_moins_m" else None
    if variante == "dernier_tour":
        Vi = x - c > tau
    elif variante == "seuil_c_moins_m":
        raise RuntimeError("variante traitée par l'appelant")
    else:
        Vi = maxx - c > tau
    Vc = maxxc - c > tau
    sD = eps if seuil_D is None else seuil_D
    Di = np.maximum(dev_haut, dev_bas) - sD > tau
    Di_haut = dev_haut - sD > tau
    Di_bas = dev_bas - sD > tau
    out = {
        "V": int(Vi.sum()), "V_tau2": int((maxx - c > tau2).sum()), "Vc": int(Vc.sum()),
        "Vc_tau2": int((maxxc - c > tau2).sum()),
        "D": int(Di.sum()), "D_haut": int(Di_haut.sum()), "D_bas": int(Di_bas.sum()),
        "N_sum": float(N.sum()), "N_sumsq": float((N.astype(np.float64) ** 2).sum()),
        "xK_sum": float(x.sum()), "xK_sumsq": float((x**2).sum()),
        "premier": int((premier - c > tau).sum()) if premier is not None else -1,
        "_Vi": Vi, "_Vc": Vc, "_N": N, "_maxx": maxx if garder_max else None,
    }
    _ = seuil
    return out


def compter_seuil_variable(A, *, K, n, gam, eta, C, seuil, tau):
    a = a_de(gam, eta)
    W = DR + C
    x = np.zeros(A.shape[0])
    mx = np.full(A.shape[0], -np.inf)
    for k in range(K):
        x = a * x + gam * DR - gam * W * A[:, k] / n
        mx = np.maximum(mx, x)
    return int((mx - seuil > tau).sum())


# ---------------------------------------------------------------- contrôle 1 (plan)
def controle_plan(K, n, gam, eta, C, c, m, delta, rho, kap, x_mf, eps_annonce, gamma_K_force=None) -> list[str]:
    defauts = []
    tau = tau_de(c)
    if abs(x_mf.max() - (c - m)) > tau:
        defauts.append(f"plan : max x_k = {x_mf.max():.12g} au lieu de c - m = {c - m:.12g}")
    g = plan_glouton(K, gam, eta, C, c - m)
    if np.max(np.abs(g - rho)) > 1e-9:
        defauts.append(f"plan : écart clos/glouton {np.max(np.abs(g - rho)):.3g}")
    s = rho.sum()
    if abs(s - closed_unif(K, gam, eta, DR, C, c - m)) > 1e-9 * max(1.0, s):
        defauts.append("plan : somme des taux ≠ B*_unif(c - m)/n")
    eps_ref = epsilon(K, n, gam, eta, C, delta)
    eps_calc = epsilon(K, n, gam, eta, C, delta, gamma_K=gamma_K_force) if gamma_K_force is not None else eps_annonce
    # eps_annonce vient de la somme directe (grille) ; eps_ref, de la forme fermée de Γ_K
    if abs(eps_calc - eps_ref) > 1e-9 * eps_ref:
        defauts.append(f"epsilon recalculée {eps_ref:.12g} ≠ {eps_calc:.12g}")
    rbar = DR / (DR + C)
    if np.any(rho < 0) or np.any(rho > rbar + 1e-12) or not np.all(np.isfinite(rho)):
        raise GardeArret("arrêt 4 : taux hors de [0, rbar + 1e-12] ou non fini")
    return defauts


# ---------------------------------------------------------------- contrôle 2 (second chemin)
def second_chemin(rng, *, K, n, gam, eta, C, c, rho, reps) -> tuple[np.ndarray, np.ndarray, list[str]]:
    """Audits tirés épisode par épisode ; x̂ par récurrence et par somme explicite."""
    a = a_de(gam, eta)
    W = DR + C
    tau = tau_de(c)
    A = np.empty((reps, K), dtype=np.int64)
    for r in range(reps):
        U = rng.random(size=(K, n))
        A[r] = (U < rho[:, None]).sum(axis=1)
    x = np.zeros(reps)
    xr = np.empty((reps, K))
    for k in range(K):
        x = a * x + gam * DR - gam * W * A[:, k] / n
        xr[:, k] = x
    j = np.arange(K)
    kk = np.arange(1, K + 1)
    expo = (kk[:, None] - 1 - j[None, :]).astype(float)
    Mat = np.where(j[None, :] < kk[:, None], np.power(a, np.maximum(expo, 0)), 0.0)
    Gk = np.array([G(k, gam, eta) for k in range(1, K + 1)])
    xs = DR * Gk[None, :] - (gam * W / n) * (A @ Mat.T)
    defauts = []
    if np.max(np.abs(xs - xr)) > tau:
        defauts.append(f"second chemin : écart récurrence/somme {np.max(np.abs(xs - xr)):.3g}")
    mr = xr.max(axis=1)
    ms = xs.max(axis=1)
    Ir = mr - c > tau
    Is = ms - c > tau
    proches = np.abs(mr - c) <= 10 * tau
    if np.any((Ir != Is) & ~proches):
        defauts.append("second chemin : indicatrices différentes hors du voisinage du seuil")
    return Ir, proches, defauts


# ---------------------------------------------------------------- bancs témoins (vérités exactes)
BANCS = {
    0: dict(nom="sans_memoire", K=20, n=1000, gam=0.2, eta=0.2, C=4.0, c=0.1, delta=0.05),
    1: dict(nom="memoire_entiere", K=12, n=100, gam=0.2, eta=math.inf, C=4.0, c=1.2, delta=0.05),
    2: dict(nom="memoire_partielle", K=3, n=1000, gam=0.2, eta=0.4, C=4.0, c=0.175, delta=0.05),
}
VALEURS_CONCEPTION = {
    "eps": {0: 0.0562, 1: 0.5855, 2: 0.05333},
    "PV": {1: (0.751, 3.24e-3, 1.219e-7), 2: (0.799, 0.0162, 4.7e-6)},
    "PO": {1: (6.3e-4, 8.7e-4, 7.3e-4)},
    "D0": {"nominal": 2.668e-5, "epreuve": 0.255, "un_cote": (0.129, 0.144)},
}


def verite_sans_memoire(b, m, eps):
    K, n, gam, C, c = b["K"], b["n"], b["gam"], b["C"], b["c"]
    W = DR + C
    rho_m = (gam * DR - c + m) / (gam * W)
    nrho0 = round(n * (gam * DR - c) / (gam * W))
    F = binom.cdf(nrho0 - 1, n, rho_m)
    PV = 1 - (1 - F) ** K
    return PV, rho_m


def verite_D_sans_memoire(b, eps, s):
    K, n, gam, C = b["K"], b["n"], b["gam"], b["C"]
    W = DR + C
    rho_e = (gam * DR - b["c"] + eps) / (gam * W)
    mu = n * rho_e
    h = n * s / (gam * W)
    ks = np.arange(n + 1)
    pm = binom.pmf(ks, n, rho_e)
    tau = tau_de(b["c"])
    dev = gam * W * np.abs(ks - mu) / n
    p_in = pm[dev - s <= tau].sum()
    p_in_haut = pm[(gam * W * (mu - ks) / n) - s <= tau].sum()   # x̂ - x = γW(μ - A)/n
    p_in_bas = pm[(gam * W * (ks - mu) / n) - s <= tau].sum()
    _ = h
    return 1 - p_in**K, 1 - p_in_haut**K, 1 - p_in_bas**K


def verite_memoire_entiere(b, m, cap):
    """Programmation dynamique sur le compte cumulé (a = 1)."""
    K, n, gam, C, c, delta = b["K"], b["n"], b["gam"], b["C"], b["c"], b["delta"]
    W = DR + C
    tau = tau_de(c)
    rho, kap = plan_clos(K, gam, math.inf, C, c, m)
    Nmax = n * K
    vivant = np.zeros(Nmax + 1)
    vivant[0] = 1.0
    tot = np.zeros(Nmax + 1)
    tot[0] = 1.0
    vivc = np.zeros(cap + 1)
    vivc[0] = 1.0
    for k in range(K):
        pk = binom.pmf(np.arange(n + 1), n, rho[k])
        vivant = np.convolve(vivant, pk)[: Nmax + 1]
        tot = np.convolve(tot, pk)[: Nmax + 1]
        Ns = np.arange(Nmax + 1)
        xk = gam * DR * (k + 1) - gam * W * Ns / n
        vivant[xk - c > tau] = 0.0
        nv = np.zeros(cap + 1)
        for N0 in range(cap + 1):
            if vivc[N0] == 0:
                continue
            reste = cap - N0
            for A_ in range(n + 1):
                nv[N0 + min(A_, reste)] += vivc[N0] * pk[A_]
        Nc = np.arange(cap + 1)
        xck = gam * DR * (k + 1) - gam * W * Nc / n
        nv[xck - c > tau] = 0.0
        vivc = nv
    PV = 1 - vivant.sum()
    Bm = n * rho.sum()
    PO = tot[np.arange(Nmax + 1) > b_rand(Bm, delta)].sum()
    PVc = 1 - vivc.sum()
    return PV, PO, PVc


def verite_memoire_partielle(b, m):
    K, n, gam, eta, C, c = b["K"], b["n"], b["gam"], b["eta"], b["C"], b["c"]
    W = DR + C
    a = a_de(gam, eta)
    tau = tau_de(c)
    rho, kap = plan_clos(K, gam, eta, C, c, m)
    ks = np.arange(n + 1)
    p0 = binom.pmf(ks, n, rho[0])
    p1 = binom.pmf(ks, n, rho[1])
    x1 = gam * DR - gam * W * ks / n
    x2 = a * x1[:, None] + gam * DR - gam * W * ks[None, :] / n
    ok = (x1[:, None] - c <= tau) & (x2 - c <= tau)
    # x3 = a x2 + γΔR - γW A2/n ≤ c + τ  ⇔  A2 ≥ n (a x2 + γΔR - c - τ)/(γW)
    seuil = n * (a * x2 + gam * DR - c - tau) / (gam * W)
    kmin = np.ceil(seuil - 1e-12)
    p_ok3 = binom.sf(kmin - 1, n, rho[2])
    p_ok3 = np.where(kmin <= 0, 1.0, p_ok3)
    P_ok = (p0[:, None] * p1[None, :] * ok * p_ok3).sum()
    return 1 - P_ok


def tirer(rng, n, rho, reps):
    return rng.binomial(n, rho, size=(reps, rho.shape[0]))


def simuler_banc(cles, i_point, i_bloc, i_rang, b, rho, kap, x_mf, eps, cap, *, variante="saine",
                 seuil_D=None, decal=1.0, A_cap_bloc=None):
    tot = None
    for lot in range(N_LOTS):
        rng = cles.rng(i_point, i_bloc, i_rang, lot)
        A = tirer(rng, b["n"], np.clip(rho * decal, 0, 1), R_LOT)
        Acap = None
        if A_cap_bloc is not None:
            Acap = tirer(cles.rng(i_point, A_cap_bloc, i_rang, lot), b["n"], rho, R_LOT)
        o = simuler_lot(A, K=b["K"], n=b["n"], gam=b["gam"], eta=b["eta"], C=b["C"], c=b["c"], rho=rho, kap=kap,
                        x_mf=x_mf, eps=eps, cap=cap, tau=tau_de(b["c"]), tau2=1e-6 * max(1, b["c"]),
                        variante=variante, seuil_D=seuil_D, A_cap=Acap)
        o["inv"] = bool(np.all(~o["_Vi"] | o["_Vc"]) and np.all(~o["_Vc"] | o["_Vi"] | (o["_N"] > b_rand(b["n"] * rho.sum(), b["delta"]))))
        for kk in ("_Vi", "_Vc", "_N", "_maxx"):
            o.pop(kk)
        if tot is None:
            tot = o
        else:
            for kk, v in o.items():
                if kk == "inv":
                    tot[kk] = tot[kk] and v
                elif kk == "premier":
                    tot[kk] = tot[kk] + v
                else:
                    tot[kk] += v
    return tot


def gardes() -> dict:
    """Étape (1) : vérités exactes des bancs, recalcul des valeurs de conception, essais des gardes."""
    journal = {"valeurs": {}, "essais": [], "defauts": []}
    cles = Cles()

    def proche(v, ref, nom):
        if abs(v - ref) > 0.01 * abs(ref):
            journal["defauts"].append(f"valeur de conception {nom} : {v:.6g} contre {ref:.6g} (écart > 1 %)")

    def essai(nom, sain_passe, artefact_detecte):
        journal["essais"].append({"garde": nom, "sain_passe": bool(sain_passe), "artefact_detecte": bool(artefact_detecte)})
        if not (sain_passe and artefact_detecte):
            journal["defauts"].append(f"garde {nom} : sain_passe={sain_passe}, artefact_detecte={artefact_detecte}")

    def dans_tol(compte, p):
        return abs(compte - R * p) <= tolerance_compte(R, p)

    plans = {}
    for ib, b in BANCS.items():
        eps = epsilon(b["K"], b["n"], b["gam"], b["eta"], b["C"], b["delta"])
        proche(eps, VALEURS_CONCEPTION["eps"][ib], f"epsilon banc {b['nom']}")
        journal["valeurs"][f"eps_{b['nom']}"] = eps
        plans[ib] = (eps, {})
        for im, m in enumerate((0.0, eps / 2, eps)):
            rho, kap = plan_clos(b["K"], b["gam"], b["eta"], b["C"], b["c"], m)
            x_mf = trajectoire_mf(b["K"], b["gam"], b["eta"], b["C"], rho)
            cap = math.floor(b_rand(b["n"] * rho.sum(), b["delta"]))
            plans[ib][1][im] = (m, rho, kap, x_mf, cap)

    # vérités exactes
    ver = {}
    b0 = BANCS[0]
    eps0 = plans[0][0]
    for im in range(3):
        ver[(0, im)] = verite_sans_memoire(b0, plans[0][1][im][0], eps0)[0]
    Dn, Dn_h, Dn_b = verite_D_sans_memoire(b0, eps0, eps0)
    De, De_h, De_b = verite_D_sans_memoire(b0, eps0, eps0 / 2)
    proche(Dn, VALEURS_CONCEPTION["D0"]["nominal"], "D nominal sans mémoire")
    proche(De, VALEURS_CONCEPTION["D0"]["epreuve"], "D épreuve sans mémoire")
    un = sorted([De_h, De_b])
    proche(un[0], VALEURS_CONCEPTION["D0"]["un_cote"][0], "D un côté (petit)")
    proche(un[1], VALEURS_CONCEPTION["D0"]["un_cote"][1], "D un côté (grand)")
    b1 = BANCS[1]
    PO1 = {}
    PVc1 = {}
    for im in range(3):
        m, rho, kap, x_mf, cap = plans[1][1][im]
        PV, PO, PVc = verite_memoire_entiere(b1, m, cap)
        ver[(1, im)] = PV
        PO1[im] = PO
        PVc1[im] = PVc
        proche(PV, VALEURS_CONCEPTION["PV"][1][im], f"PV mémoire entière marge {im}")
        proche(PO, VALEURS_CONCEPTION["PO"][1][im], f"PO mémoire entière marge {im}")
    b2 = BANCS[2]
    for im in range(3):
        PV = verite_memoire_partielle(b2, plans[2][1][im][0])
        ver[(2, im)] = PV
        proche(PV, VALEURS_CONCEPTION["PV"][2][im], f"PV mémoire partielle marge {im}")
    journal["valeurs"]["verites_V"] = {f"{k[0]}_{k[1]}": v for k, v in ver.items()}
    journal["valeurs"]["verites_D_sans_memoire"] = {"nominal": Dn, "epreuve": De, "haut": De_h, "bas": De_b}
    journal["valeurs"]["verites_O_memoire_entiere"] = PO1
    journal["valeurs"]["verites_Vc_memoire_entiere"] = PVc1

    # simulations saines (bloc 0) et artefacts (bloc 1)
    sains = {}
    for ib, b in BANCS.items():
        eps = plans[ib][0]
        for im in range(3):
            m, rho, kap, x_mf, cap = plans[ib][1][im]
            sains[(ib, im)] = simuler_banc(cles, 1000 + ib, 0, im, b, rho, kap, x_mf, eps, cap,
                                           seuil_D=(eps / 2 if ib == 0 and im == 2 else None))

    # 1. plan
    sain_plan = all(not controle_plan(b["K"], b["n"], b["gam"], b["eta"], b["C"], b["c"], 0.0, b["delta"],
                                      plans[ib][1][0][1], plans[ib][1][0][2], plans[ib][1][0][3], plans[ib][0])
                    and dans_tol(sains[(ib, 0)]["V"], ver[(ib, 0)])
                    for ib, b in BANCS.items())
    b = BANCS[0]
    rho_f, kap_f = plan_clos(b["K"], b["gam"], b["eta"], b["C"], b["c"], plans[0][0])  # construit avec la marge
    xmf_f = trajectoire_mf(b["K"], b["gam"], b["eta"], b["C"], rho_f)
    art_a = bool(controle_plan(b["K"], b["n"], b["gam"], b["eta"], b["C"], b["c"], 0.0, b["delta"], rho_f, kap_f, xmf_f, plans[0][0]))
    b = BANCS[2]
    a2 = a_de(b["gam"], b["eta"])
    gam_faux = sum(a2**i for i in range(b["K"]))
    art_b = bool(controle_plan(b["K"], b["n"], b["gam"], b["eta"], b["C"], b["c"], 0.0, b["delta"],
                               plans[2][1][0][1], plans[2][1][0][2], plans[2][1][0][3], plans[2][0], gamma_K_force=gam_faux))
    essai("plan (controle 1)", sain_plan, art_a and art_b)

    # 2. compteur de V
    sain_V = all(dans_tol(sains[(ib, im)]["V"], ver[(ib, im)]) for ib in BANCS for im in range(3))
    detections = {}
    for variante in ("dernier_tour", "fusion_depassement", "seuil_c_moins_m", "sans_memoire"):
        det = False
        for ib, b in BANCS.items():
            if variante == "sans_memoire" and ib == 0:
                continue
            eps = plans[ib][0]
            for im in range(3):
                m, rho, kap, x_mf, cap = plans[ib][1][im]
                cnt = 0
                for lot in range(N_LOTS):
                    rng = cles.rng(1000 + ib, 1, 100 + 10 * ["dernier_tour", "fusion_depassement", "seuil_c_moins_m", "sans_memoire"].index(variante) + im, lot)
                    A = tirer(rng, b["n"], rho, R_LOT)
                    if variante == "seuil_c_moins_m":
                        cnt += compter_seuil_variable(A, K=b["K"], n=b["n"], gam=b["gam"], eta=b["eta"], C=b["C"],
                                                      seuil=b["c"] - m, tau=tau_de(b["c"]))
                        continue
                    o = simuler_lot(A, K=b["K"], n=b["n"], gam=b["gam"], eta=b["eta"], C=b["C"], c=b["c"], rho=rho,
                                    kap=kap, x_mf=x_mf, eps=eps, cap=cap, tau=tau_de(b["c"]), tau2=1e-6,
                                    variante=("saine" if variante == "fusion_depassement" else variante))
                    if variante == "fusion_depassement":
                        cnt += int((o["_Vi"] | (o["_N"] > b_rand(b["n"] * rho.sum(), b["delta"]))).sum())
                    else:
                        cnt += o["V"]
                if not dans_tol(cnt, ver[(ib, im)]):
                    det = True
        detections[variante] = det
    essai("compteur de la violation sans plafond", sain_V, all(detections.values()))
    journal["valeurs"]["detections_compteur_V"] = detections

    # 3. compteurs V' et D
    b = BANCS[1]
    sain_Vc = all(dans_tol(sains[(1, im)]["Vc"], PVc1[im]) for im in range(3))
    m, rho, kap, x_mf, cap = plans[1][1][0]
    eps1 = plans[1][0]
    epreuve = simuler_banc(cles, 1001, 0, 200, b, rho, kap, x_mf, eps1, 118)
    sain_Vc = sain_Vc and epreuve["Vc"] == R
    art_ignore = simuler_banc(cles, 1001, 1, 200, b, rho, kap, x_mf, eps1, 118, variante="ignore_plafond")
    art_tour = simuler_banc(cles, 1001, 1, 201, b, rho, kap, x_mf, eps1, 118, variante="plafond_par_tour")
    b0 = BANCS[0]
    m, rho0, kap0, xmf0, cap0 = plans[0][1][2]
    nominal = simuler_banc(cles, 1000, 0, 200, b0, rho0, kap0, xmf0, eps0, cap0, seuil_D=eps0)
    sain_D = dans_tol(nominal["D"], Dn) and dans_tol(sains[(0, 2)]["D"], De)
    art_D = simuler_banc(cles, 1000, 1, 202, b0, rho0, kap0, xmf0, eps0, cap0, seuil_D=eps0 / 2)
    det_un = (not dans_tol(art_D["D_haut"], De)) and (not dans_tol(art_D["D_bas"], De))
    essai("compteurs de la violation plafonnée et de l'écart bilatéral", sain_Vc and sain_D,
          (art_ignore["Vc"] != R) and (art_tour["Vc"] != R) and det_un)

    # 4. tirages
    def moyenne_ok(tot, n, rho):
        mu = n * rho.sum()
        var = n * (rho * (1 - rho)).sum()
        return abs(tot["N_sum"] / R - mu) <= 5 * math.sqrt(var / R)
    m, rho, kap, x_mf, cap = plans[0][1][1]
    sain_t = moyenne_ok(sains[(0, 1)], b0["n"], rho)
    art_t = simuler_banc(cles, 1000, 1, 203, b0, rho, kap, x_mf, eps0, cap, decal=1.1)
    essai("tirages (moyenne du nombre d'audits)", sain_t, not moyenne_ok(art_t, b0["n"], rho))

    # 5. valeurs finies, clés, écrasement
    try:
        simuler_lot(np.full((2, 3), 0), K=3, n=10, gam=0.2, eta=0.4, C=4.0, c=0.175, rho=np.full(3, 0.1), kap=0,
                    x_mf=np.zeros(4), eps=0.05, cap=10, tau=1e-9, tau2=1e-6)
        fini_sain = True
    except GardeArret:
        fini_sain = False
    try:
        simuler_lot(np.array([[0, 0, 0], [0, 0, 0]]), K=3, n=0, gam=0.2, eta=0.4, C=4.0, c=0.175, rho=np.full(3, 0.1),
                    kap=0, x_mf=np.zeros(4), eps=0.05, cap=10, tau=1e-9, tau2=1e-6)
        fini_art = False
    except GardeArret:
        fini_art = True
    # clés : cas sain = jeu de clés de la forme employée par la course (points, blocs 0-9), tous distincts
    k2 = Cles()
    try:
        for ip in range(144):
            for ib_ in range(10):
                for ir in range(11):
                    for il_ in range(100 if ib_ == 7 else 10):
                        k2.rng(ip, ib_, ir, il_) if (ib_ == 7 and ir <= 1) or (ib_ != 7 and ir <= 10) else None
        cle_sain = True
    except GardeArret:
        cle_sain = False
    try:
        k2.rng(0, 0, 0, 0)
        cle_art = False
    except GardeArret:
        cle_art = True
    ecr_sain, ecr_art = essai_ecrasement_resultat()
    essai("valeurs finies, clés distinctes, refus d'écraser", fini_sain and cle_sain and ecr_sain,
          fini_art and cle_art and ecr_art)
    # (10) recalcul des autres chiffres de conception
    b2c = BANCS[2]
    a2c = a_de(b2c["gam"], b2c["eta"])
    gK = gamma_K_ferme(b2c["K"], a2c)
    proche(gK, 1.3125, "Gamma_K mémoire partielle")
    proche(epsilon(b2c["K"], b2c["n"], b2c["gam"], b2c["eta"], b2c["C"], b2c["delta"],
                   gamma_K=sum(a2c**i for i in range(b2c["K"]))), 0.0611, "epsilon avec la mauvaise somme")
    b0c = BANCS[0]
    proche(b0c["n"] * plan_clos(b0c["K"], b0c["gam"], b0c["eta"], b0c["C"], b0c["c"], 0.0)[0][0], 100.0, "n rho_0 sans mémoire")
    b1c = BANCS[1]
    n_final = (b1c["gam"] * DR * b1c["K"] - b1c["c"]) * b1c["n"] / (b1c["gam"] * (DR + b1c["C"]))
    proche(n_final, 120.0, "audits exigés par la contrainte finale (mémoire entière)")

    # 6. sensibilité à la tolérance (banc sans mémoire, marge ε/2)
    m, rho, kap, x_mf, cap = plans[0][1][1]
    sain_s = abs(sains[(0, 1)]["V"] - sains[(0, 1)]["V_tau2"]) <= 10
    cnt_art = 0
    for lot in range(N_LOTS):
        A = tirer(cles.rng(1000, 1, 204, lot), b0["n"], rho, R_LOT)
        cnt_art_lot = compter_seuil_variable(A, K=b0["K"], n=b0["n"], gam=b0["gam"], eta=b0["eta"], C=b0["C"],
                                             seuil=b0["c"], tau=tau_de(b0["c"]))
        cnt_art_lot2 = compter_seuil_variable(A, K=b0["K"], n=b0["n"], gam=b0["gam"], eta=b0["eta"], C=b0["C"],
                                              seuil=b0["c"], tau=1.5 * b0["gam"] * (DR + b0["C"]) / b0["n"])
        cnt_art += abs(cnt_art_lot - cnt_art_lot2)
    essai("sensibilité à la tolérance", sain_s, cnt_art > 10)

    # 7. invariant entre violations
    m, rho, kap, x_mf, cap = plans[1][1][0]
    sain_i = all(sains[k]["inv"] for k in sains)
    art_i = simuler_banc(cles, 1001, 1, 205, b1, rho, kap, x_mf, eps1, cap, A_cap_bloc=2)
    essai("invariant entre violations", sain_i, not art_i["inv"])

    journal["cles_employees"] = [list(k) for k in sorted(cles.vues)]
    return journal


def refus_ecraser_essai() -> bool:
    import tempfile
    with tempfile.TemporaryDirectory() as d:
        p = Path(d) / "sortie.json"
        p.write_text("{}")
        try:
            ecrire_neuf(p, {})
            return False
        except GardeArret:
            return True


def essai_ecrasement_resultat() -> tuple[bool, bool]:
    """Éprouve ecrire_resultat (fonction de la course) dans une racine temporaire : écriture neuve, puis refus."""
    import tempfile
    from controle_ia.manifeste import config_canonique, ecrire_resultat
    from controle_ia.scellement import sceller
    with tempfile.TemporaryDirectory() as d:
        racine = Path(d)
        run = racine / "runs" / "20261124-000000-essai"
        run.mkdir(parents=True)
        cfg = {"essai": True}
        man = {"run_id": "20261124-000000-essai", "config": cfg,
               "config_sha256": hashlib.sha256(config_canonique(cfg)).hexdigest()}
        mp = run / "manifeste.json"
        mp.write_text(json.dumps(man))
        sceller(mp)
        try:
            ecrire_resultat(racine, mp, "sortie", {"x": 1})
            sain = True
        except GardeArret:
            sain = False
        try:
            ecrire_resultat(racine, mp, "sortie", {"x": 2})
            art = False
        except GardeArret:
            art = True
    return sain, art


def ecrire_neuf(p: Path, contenu: dict):
    if p.exists():
        raise GardeArret(f"fichier de sortie déjà présent : {p}")
    p.write_text(json.dumps(contenu, indent=2, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")


# ---------------------------------------------------------------- grille
def grille() -> list[dict]:
    pts = []
    i = 0
    for K in (50, 200, 500):
        for n in (100, 1000):
            for gam in (0.05, 0.2):
                for eta in (1.0, 10.0, math.inf):
                    for C in (4.0, 19.0):
                        for delta in (0.05, 0.1):
                            c = 0.5 * DR * G(K, gam, eta)
                            a_ = a_de(gam, eta)
                            eps = epsilon(K, n, gam, eta, C, delta, gamma_K=sum(a_ ** (2 * i) for i in range(K)))
                            pts.append(dict(i=i, K=K, n=n, gam=gam, eta=eta, C=C, delta=delta, c=c, eps=eps,
                                            admissible=eps <= c))
                            i += 1
    return pts


def verifier_admissibilite(pts) -> dict:
    adm = [p for p in pts if p["admissible"]]
    inad = [p for p in pts if not p["admissible"]]
    tenus = []
    audits_min = math.inf
    for p in adm:
        rho, kap = plan_clos(p["K"], p["gam"], p["eta"], p["C"], p["c"], 0.0)
        tenus.append(p["K"] - 1 - kap)
        audits_min = min(audits_min, p["n"] * rho[kap + 1:].min() if kap + 1 < p["K"] else math.inf)
    res = {"admissibles": len(adm), "inadmissibles": [dict(i=p["i"], K=p["K"], n=p["n"], gam=p["gam"],
                                                            eta=str(p["eta"]), C=p["C"], delta=p["delta"],
                                                            eps=p["eps"], c=p["c"]) for p in inad],
           "min_tours_tenus": min(tenus), "min_audits_par_tour_tenu": audits_min}
    if len(adm) != 138:
        raise GardeArret(f"arrêt 3 : {len(adm)} points admissibles au lieu de 138")
    if min(tenus) != 24:
        raise GardeArret(f"arrêt 3 : minimum de K-1-kappa(0) = {min(tenus)} au lieu de 24")
    return res


def lots_simulation(cles, p, i_bloc, i_rang, rho, kap, x_mf, m, n_lots, *, garder_max=False, seuil_D=None):
    K, n, gam, eta, C, c, delta = p["K"], p["n"], p["gam"], p["eta"], p["C"], p["c"], p["delta"]
    cap = math.floor(b_rand(n * rho.sum(), delta))
    Brand = b_rand(n * rho.sum(), delta)
    tot = {"V": 0, "V_tau2": 0, "Vc": 0, "Vc_tau2": 0, "D": 0, "O": 0, "N_sum": 0.0, "N_sumsq": 0.0, "xK_sum": 0.0,
           "xK_sumsq": 0.0, "premier": 0, "R": 0}
    maxs = []
    for lot in range(n_lots):
        rng = cles.rng(p["i"], i_bloc, i_rang, lot)
        A = tirer(rng, n, rho, R_LOT)
        o = simuler_lot(A, K=K, n=n, gam=gam, eta=eta, C=C, c=c, rho=rho, kap=kap, x_mf=x_mf, eps=p["eps"],
                        cap=cap, tau=tau_de(c), tau2=1e-6 * max(1, c), garder_max=garder_max, seuil_D=seuil_D)
        O = o["_N"] > Brand
        if not (np.all(~o["_Vi"] | o["_Vc"]) and np.all(~o["_Vc"] | o["_Vi"] | O)):
            raise GardeArret(f"arrêt 4 : invariant entre violations manqué au point {p['i']}")
        for k in ("V", "V_tau2", "Vc", "Vc_tau2", "D", "N_sum", "N_sumsq", "xK_sum", "xK_sumsq", "premier"):
            tot[k] += o[k]
        tot["O"] += int(O.sum())
        tot["R"] += A.shape[0]
        if garder_max:
            maxs.append(o["_maxx"] - c)
    return tot, (np.concatenate(maxs) if garder_max else None), Brand


def proba_depassement_exacte(n, rho, kap, Brand) -> float:
    K = rho.shape[0]
    k1 = np.arange(n + 1)
    p1 = binom.pmf(k1, n, rho[kap])
    n2 = n * (K - 1 - kap)
    hold = rho[kap + 1] if kap + 1 < K else 0.0
    # P(N1 + N2 > Brand) = Σ p1(a) P(N2 > Brand - a)
    return float((p1 * binom.sf(np.floor(Brand - k1), n2, hold)).sum()) if n2 > 0 else float(p1[k1 > Brand].sum())


def traiter_point(p: dict) -> dict:
    t0 = time.time()
    cles = Cles()
    K, n, gam, eta, C, c, delta, eps = p["K"], p["n"], p["gam"], p["eta"], p["C"], p["c"], p["delta"], p["eps"]
    a = a_de(gam, eta)
    W = DR + C
    tau = tau_de(c)
    defauts = []
    res = {"point": {k: (str(v) if isinstance(v, float) and math.isinf(v) else v) for k, v in p.items()},
           "marges": {}, "prolongations": {}, "controle2": {}, "audit_renforce": {}, "bissection": None,
           "boucle_fermee": {}, "non_concluant_sensibilite": []}
    plans = {}
    for il, lam in enumerate(LAMBDAS):
        m = lam * eps
        rho, kap = plan_clos(K, gam, eta, C, c, m)
        x_mf = trajectoire_mf(K, gam, eta, C, rho)
        d1 = controle_plan(K, n, gam, eta, C, c, m, delta, rho, kap, x_mf, eps)
        defauts += [f"lambda={lam} : {d}" for d in d1]
        plans[il] = (m, rho, kap, x_mf)
        tot, maxs, Brand = lots_simulation(cles, p, il, 0, rho, kap, x_mf, m, N_LOTS, garder_max=(lam == 1.0))
        # garde des tirages (arrêt 5)
        mu = n * rho.sum()
        varN = n * (rho * (1 - rho)).sum()
        if abs(tot["N_sum"] / R - mu) > 5 * math.sqrt(varN / R):
            defauts.append(f"lambda={lam} : garde des tirages hors tolérance")
        # contrôle 3 (moments)
        mean_x = tot["xK_sum"] / R
        var_x = tot["xK_sumsq"] / R - mean_x**2
        var_th = (gam * W) ** 2 / n * sum(a ** (2 * (K - 1 - j)) * rho[j] * (1 - rho[j]) for j in range(K))
        if abs(mean_x - x_mf[K]) > 5 * math.sqrt(max(var_x, 0) / R):
            defauts.append(f"lambda={lam} : contrôle 3 (moyenne de x_K)")
        if abs(var_x - var_th) > 0.03 * var_th:
            defauts.append(f"lambda={lam} : contrôle 3 (variance de x_K)")
        # contrôle 4 (premier tour audité)
        t1 = n * rho[kap] - n * (m + tau) / (gam * W)
        p1 = 0.0 if t1 <= 0 else float(binom.cdf(math.ceil(t1) - 1, n, rho[kap]))
        if abs(tot["premier"] - R * p1) > 5 * math.sqrt(R * p1 * (1 - p1)) + 3:
            defauts.append(f"lambda={lam} : contrôle 4 (premier tour audité)")
        # sensibilité (arrêt 6)
        if abs(tot["V"] - tot["V_tau2"]) > 10 or abs(tot["Vc"] - tot["Vc_tau2"]) > 10:
            res["non_concluant_sensibilite"].append(lam)
        entree = {"m": m, "kappa": kap, "B_m": mu, "B_rand": Brand, "V": tot["V"], "V_tau2": tot["V_tau2"],
                  "Vc": tot["Vc"], "Vc_tau2": tot["Vc_tau2"], "D": tot["D"], "D_ic95": cp95(tot["D"], R), "O": tot["O"], "O_exact": proba_depassement_exacte(n, rho, kap, Brand),
                  "R": tot["R"], "V_ic95": cp95(tot["V"], R), "Vc_ic95": cp95(tot["Vc"], R),
                  "O_ic95": cp95(tot["O"], R), "classe_V_premier": classer(tot["V"], R, delta / 2)}
        if lam == 1.0:
            entree.update({"classe_Vc_premier": classer(tot["Vc"], R, delta),
                           "classe_D_premier": classer(tot["D"], R, delta)})
            q = 1 - delta / 2
            srt = np.sort(maxs)
            iq = int(math.ceil(q * R)) - 1
            lo = int(binom.ppf(0.025, R, q)) - 1
            hi = int(binom.ppf(0.975, R, q))
            entree["distance_seuil"] = {"quantile_sur_eps": float(srt[iq] / eps),
                                        "ic95_sur_eps": [float(srt[max(lo, 0)] / eps), float(srt[min(hi, R - 1)] / eps)]}
        res["marges"][str(lam)] = entree
    # contrôle 2 systématique (λ = 0 et 1)
    for rang, il in ((0, 0), (1, 5)):
        m, rho, kap, x_mf = plans[il]
        Ir, proches, d2 = second_chemin(cles.rng(p["i"], 8, rang, 0), K=K, n=n, gam=gam, eta=eta, C=C, c=c,
                                        rho=rho, reps=1000)
        defauts += [f"contrôle 2 lambda={LAMBDAS[il]} : {d}" for d in d2]
        Vr = res["marges"][str(LAMBDAS[il])]["V"] / R
        f2 = float(Ir.mean())
        if abs(f2 - Vr) > 5 * math.sqrt(Vr * (1 - Vr) * (1e-3 + 1e-5)) + 0.003:
            defauts.append(f"contrôle 2 lambda={LAMBDAS[il]} : fréquence {f2:.4f} contre {Vr:.4f}")
        res["controle2"][str(LAMBDAS[il])] = {"frequence": f2, "repetitions_proches_du_seuil": int(proches.sum()),
                                              "indices_proches": [int(i) for i in np.flatnonzero(proches)]}
    if defauts:
        res["defauts_instrument"] = defauts
        res["duree_s"] = time.time() - t0
        return res
    # prolongations et classes finales
    m0 = res["marges"]["0.0"]
    m1 = res["marges"]["1.0"]
    classes = {"V0": m0["classe_V_premier"], "V1": m1["classe_V_premier"], "Vc1": m1["classe_Vc_premier"],
               "D1": m1["classe_D_premier"]}
    finales = {}
    if classes["V0"] == "indetermine":
        m, rho, kap, x_mf = plans[0]
        tot, _, _ = lots_simulation(cles, p, 7, 0, rho, kap, x_mf, m, N_LOTS_PROLONG)
        cl = classer(tot["V"], tot["R"], delta / 2)
        sens = abs(tot["V"] - tot["V_tau2"]) > 10
        res["prolongations"]["0.0"] = {"V": tot["V"], "V_tau2": tot["V_tau2"], "R": tot["R"], "classe_V": cl,
                                       "V_ic95": cp95(tot["V"], tot["R"]), "sensibilite_tau2": bool(sens)}
        finales["V0"] = "non concluant" if (cl == "indetermine" or sens) else cl
    else:
        finales["V0"] = classes["V0"]
    declenche = {k for k in ("V1", "Vc1", "D1") if classes[k] in ("au-dessus", "indetermine")}
    if declenche:
        m, rho, kap, x_mf = plans[5]
        tot, _, _ = lots_simulation(cles, p, 7, 1, rho, kap, x_mf, m, N_LOTS_PROLONG)
        cls_tous = {"V1": classer(tot["V"], tot["R"], delta / 2), "Vc1": classer(tot["Vc"], tot["R"], delta),
                    "D1": classer(tot["D"], tot["R"], delta)}
        sens1 = {"V1": abs(tot["V"] - tot["V_tau2"]) > 10, "Vc1": abs(tot["Vc"] - tot["Vc_tau2"]) > 10, "D1": False}
        # (8) seules les métriques déclenchantes sont lues sur la prolongation
        cls = {k: (cls_tous[k] if k in declenche else "non lue") for k in cls_tous}
        res["prolongations"]["1.0"] = {"V": tot["V"], "V_tau2": tot["V_tau2"], "Vc": tot["Vc"],
                                       "Vc_tau2": tot["Vc_tau2"], "D": tot["D"], "R": tot["R"],
                                       "V_ic95": cp95(tot["V"], tot["R"]), "Vc_ic95": cp95(tot["Vc"], tot["R"]),
                                       "D_ic95": cp95(tot["D"], tot["R"]), "declenchee_par": sorted(declenche),
                                       "classes": cls, "sensibilite_tau2": {k: bool(v) for k, v in sens1.items()}}
    for k in ("V1", "Vc1", "D1"):
        if k not in declenche:
            finales[k] = classes[k]
        else:
            cl = res["prolongations"]["1.0"]["classes"][k]
            if res["prolongations"]["1.0"]["sensibilite_tau2"][k]:
                finales[k] = "non concluant"
            elif classes[k] == "au-dessus":
                finales[k] = "au-dessus" if cl == "au-dessus" else "non concluant"
            else:
                finales[k] = cl if cl != "indetermine" else "non concluant"
    # (2) arrêt n° 6 : sensibilité à τ' sur le premier tirage, pour les classes qui en viennent
    if 0.0 in res["non_concluant_sensibilite"] and "0.0" not in res["prolongations"]:
        finales["V0"] = "non concluant"
    if 1.0 in res["non_concluant_sensibilite"]:
        for k in ("V1", "Vc1"):
            if k not in declenche:
                finales[k] = "non concluant"
    res["classes_premier_tirage"] = classes
    res["classes_finales"] = finales
    # audit renforcé : « trop propre » à λ = 0, ou toute réfutation (V, V' ou D au-dessus à λ = 1)
    cibles = []
    if finales["V0"] == "sous":
        cibles.append((0, 2, 0))
    if any(finales[k] == "au-dessus" for k in ("V1", "Vc1", "D1")):
        cibles.append((5, 3, 1))
    for il, rang, _ in cibles:
        m, rho, kap, x_mf = plans[il]
        Ir, proches, d2 = second_chemin(cles.rng(p["i"], 8, rang, 0), K=K, n=n, gam=gam, eta=eta, C=C, c=c,
                                        rho=rho, reps=10_000)
        lam = LAMBDAS[il]
        if il == 0 and "0.0" in res["prolongations"]:
            ref = res["prolongations"]["0.0"]["V"] / res["prolongations"]["0.0"]["R"]
            inv_ref = 1e-6
        elif il == 5 and "1.0" in res["prolongations"]:
            ref = res["prolongations"]["1.0"]["V"] / res["prolongations"]["1.0"]["R"]
            inv_ref = 1e-6
        else:
            ref = res["marges"][str(lam)]["V"] / R
            inv_ref = 1e-5
        f2 = float(Ir.mean())
        ok = (not d2) and abs(f2 - ref) <= 5 * math.sqrt(ref * (1 - ref) * (1e-4 + inv_ref)) + 0.0003
        res["audit_renforce"][str(lam)] = {"frequence": f2, "reference": ref, "sans_defaut": bool(ok),
                                           "defauts": d2}
        if not ok:
            defauts.append(f"audit renforcé lambda={lam} hors tolérance")
    if defauts:
        res["defauts_instrument"] = defauts
        res["duree_s"] = time.time() - t0
        return res
    # bissection
    if finales["V0"] == "au-dessus" and finales["V1"] == "sous":
        lo, hi = 0.0, eps
        hist = []
        for it in range(10):
            mm = 0.5 * (lo + hi)
            rho, kap = plan_clos(K, gam, eta, C, c, mm)
            x_mf = trajectoire_mf(K, gam, eta, C, rho)
            d1 = controle_plan(K, n, gam, eta, C, c, mm, delta, rho, kap, x_mf, eps)
            if d1:
                defauts += [f"bissection it={it} : {d}" for d in d1]
            tot, _, _ = lots_simulation(cles, p, 6, it, rho, kap, x_mf, mm, N_LOTS)
            hist.append({"m": mm, "V": tot["V"], "V_ic95": cp95(tot["V"], R)})
            if tot["V"] / R <= delta / 2:
                hi = mm
            else:
                lo = mm
        rho, kap = plan_clos(K, gam, eta, C, c, hi)
        x_mf = trajectoire_mf(K, gam, eta, C, rho)
        tot, _, _ = lots_simulation(cles, p, 6, 10, rho, kap, x_mf, hi, N_LOTS)
        conf = classer(tot["V"], R, delta / 2)
        # encadrement par la grille
        cl_grille = {}
        for il, lam in enumerate(LAMBDAS):
            if lam == 0.0:
                cl_grille[lam] = finales["V0"]
            elif lam == 1.0:
                cl_grille[lam] = finales["V1"]
            else:
                cl_grille[lam] = res["marges"][str(lam)]["classe_V_premier"]
        lam_moins = max([lam for lam, cl in cl_grille.items() if cl == "au-dessus"], default=None)
        lam_plus = min([lam for lam, cl in cl_grille.items() if cl == "sous"], default=None)
        valide = (conf != "au-dessus") and lam_moins is not None and lam_plus is not None and \
            (lam_moins * eps <= hi <= lam_plus * eps)
        res["bissection"] = {"historique": hist, "eps_emp": hi, "rapport": hi / eps, "confirmation": {"V": tot["V"], "classe": conf, "V_ic95": cp95(tot["V"], R)},
                             "lambda_moins": lam_moins, "lambda_plus": lam_plus, "valide": bool(valide),
                             "budget_epargne_sur_Bstar": (n * plans[5][1].sum() - n * rho.sum()) /
                             (n * closed_unif(K, gam, eta, DR, C, c))}
    # monotonie (Fisher unilatéral, 1e-5) sur les paires voisines, premiers tirages
    mono = []
    for il in range(len(LAMBDAS) - 1):
        k1 = res["marges"][str(LAMBDAS[il])]["V"]
        k2 = res["marges"][str(LAMBDAS[il + 1])]["V"]
        pv = fisher_exact([[k2, R - k2], [k1, R - k1]], alternative="greater")[1]
        mono.append({"paire": [LAMBDAS[il], LAMBDAS[il + 1]], "p": float(pv), "hausse_significative": bool(pv < 1e-5)})
    res["monotonie"] = mono
    # bras en boucle fermée (descriptif)
    for rang, lam in ((0, 0.0), (1, 1.0)):
        m = lam * eps
        Vt = 0
        Ot = 0
        Ns = 0.0
        Brand = res["marges"][str(lam)]["B_rand"]
        for lot in range(N_LOTS):
            rng = cles.rng(p["i"], 9, rang, lot)
            x = np.zeros(R_LOT)
            mx = np.full(R_LOT, -np.inf)
            N = np.zeros(R_LOT)
            for k in range(K):
                # bras descriptif : taux recalculés sur la trajectoire réalisée, bornés à [0, 1] (et non à rbar)
                r = np.clip((a * x + gam * DR - (c - m)) / (gam * W), 0.0, 1.0)
                if not np.all(np.isfinite(r)):
                    raise GardeArret("arrêt 4 : taux non fini en boucle fermée")
                Ak = rng.binomial(n, r)
                x = a * x + gam * DR - gam * W * Ak / n
                mx = np.maximum(mx, x)
                N += Ak
            Vt += int((mx - c > tau).sum())
            Ot += int((N > Brand).sum())
            Ns += float(N.sum())
        res["boucle_fermee"][str(lam)] = {"V": Vt, "V_ic95": cp95(Vt, R), "O_contre_B_rand_ouvert": Ot,
                                          "O_ic95": cp95(Ot, R), "audits_moyens": Ns / R, "R": R}
    if defauts:
        res["defauts_instrument"] = defauts
    res["cles"] = [list(k) for k in sorted(cles.vues)]
    res["duree_s"] = time.time() - t0
    return res


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--gardes", action="store_true")
    ap.add_argument("--course", action="store_true")
    ap.add_argument("--run-id")
    ap.add_argument("--processus", type=int, default=4)
    args = ap.parse_args()
    from controle_ia.prereg import exiger_prereg_scelle
    sha = exiger_prereg_scelle(PREREG)
    if sha != PREREG_SHA:
        raise GardeArret(f"arrêt 1 : empreinte du préenregistrement {sha} ≠ {PREREG_SHA}")
    from controle_ia.scellement import verifier as verifier_sceau
    if verifier_sceau(ERRATUM) != ERRATUM_SHA:
        raise GardeArret("arrêt 1 : erratum 1 non scellé ou altéré")
    if args.gardes and not args.course:
        j = gardes()
        print(json.dumps({"defauts": j["defauts"], "essais": j["essais"], "valeurs": j["valeurs"]}, indent=1, default=str))
        if j["defauts"]:
            raise SystemExit("arrêt 2 : garde ou valeur de conception en défaut")
        return
    if not args.course or not args.run_id:
        raise SystemExit("usage : --gardes | --course --run-id AAAAMMJJ-HHMMSS-nom")
    from controle_ia.manifeste import creer_manifeste, ecrire_resultat
    script_sha = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    config = {"script": str(Path(__file__).relative_to(RACINE)), "script_sha256": script_sha,
              "entropie": ENTROPIE, "R": R, "R_lot": R_LOT, "lots_prolongation": N_LOTS_PROLONG,
              "lambdas": list(LAMBDAS), "niveau_unilateral": NIV,
              "schema_graines": "SeedSequence(entropy=202611243003, spawn_key=(i_point, i_bloc, i_rang, i_lot)) ; PCG64 ;"
                                " toutes les clés employées sont consignées dans les sorties scellées",
              "champ_graines_du_manifeste": "la graine « non-employee » du manifeste ne sert à aucun tirage",
              "ecart_interpretation_rangs_bancs": "bancs témoins : essais supplémentaires sur une même marge aux rangs"
                                                  " >= 100 (compteur : 100 + 10*variante + marge ; autres : 200-205) ;"
                                                  " audits plafonnés de l'artefact de l'invariant au bloc 2",
              "audit_renforce_declenche_aussi_par_D": True,
              "reference_audit_renforce_lambda1": "prolongation dès qu'elle existe"}
    chemin_m, _ = creer_manifeste(RACINE, args.run_id, config, ["non-employee"], entropie=ENTROPIE, decisif=True,
                                  prereg=PREREG, commande=" ".join(sys.argv))
    t0 = time.time()

    def arret(n, motif, **extra):
        ecrire_resultat(RACINE, chemin_m, f"arret-{n}", {"arret": n, "motif": motif, **extra})
        raise SystemExit(f"arrêt {n} : {motif}")

    j = gardes()
    if j["defauts"]:
        arret(2, "garde ou valeur de conception en défaut ; rien de la grille n'est tiré", journal=j)
    pts = grille()
    try:
        adm = verifier_admissibilite(pts)
    except GardeArret as e:
        arret(3, str(e))
    print(f"gardes passées ; {adm['admissibles']} points admissibles ; course lancée", flush=True)
    a_traiter = [p for p in pts if p["admissible"]]
    resultats = []
    limite = 12 * 3600
    ex = ProcessPoolExecutor(max_workers=args.processus)
    try:
        futurs = [ex.submit(traiter_point, p) for p in a_traiter]
        try:
            for f in as_completed(futurs, timeout=max(1.0, limite - (time.time() - t0))):
                try:
                    resultats.append(f.result())
                except GardeArret as e:
                    ex.shutdown(wait=False, cancel_futures=True)
                    arret(4, str(e))
                print(f"point {len(resultats)}/{len(a_traiter)} traité", flush=True)
        except FuturTimeout:
            ex.shutdown(wait=False, cancel_futures=True)
            arret(7, "plus de 12 heures de calcul")
    finally:
        ex.shutdown(wait=False, cancel_futures=True)
    resultats.sort(key=lambda r: r["point"]["i"])
    toutes_cles = [tuple(k) for r in resultats for k in r.get("cles", [])]
    if len(set(toutes_cles)) != len(toutes_cles):
        arret(4, "clés de graines en double entre points")
    defauts = [(r["point"]["i"], r["defauts_instrument"]) for r in resultats if r.get("defauts_instrument")]
    sortie = {"gardes": j, "admissibilite": adm, "points": resultats, "defauts_instrument": defauts,
              "course_invalide": bool(defauts), "duree_s": time.time() - t0}
    chemin = ecrire_resultat(RACINE, chemin_m, "sorties-brutes", sortie)
    print(f"sorties scellées : {chemin.relative_to(RACINE)} ; course_invalide={bool(defauts)}", flush=True)

if __name__ == "__main__":
    main()
