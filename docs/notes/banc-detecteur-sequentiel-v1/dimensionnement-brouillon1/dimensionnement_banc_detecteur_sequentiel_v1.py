"""Calculs de principe, sous supposition, pour dimensionner le banc de validité du détecteur séquentiel
(préenregistrement prereg/banc-detecteur-sequentiel-reference-contaminee-v1.md, annexe A).

Aucun tirage au hasard : formes fermées, lois normales exactes, quadratures sur grilles déterministes.
Dépendances : numpy et la bibliothèque standard (statistics.NormalDist). Aucune cellule de la grille n'est simulée.
"""
from __future__ import annotations

import math
from statistics import NormalDist

import numpy as np

N01 = NormalDist()
ALPHA, A_CAL, A_ARRET = 0.05, 0.025, 0.025


# ---------- processus e unilatéral de mélange normal (mêmes formules que agregateurs/processus_e.py, σ = 1)
def log_e_unilateral(S: float, n: float, rho: float) -> float:
    a = 1.0 + rho * rho * n
    x = rho * S / math.sqrt(a)
    return math.log(2.0) - 0.5 * math.log(a) + rho * rho * S * S / (2.0 * a) + math.log(max(N01.cdf(x), 1e-300))


def frontiere(n: float, rho: float, alpha: float) -> float:
    """s* > 0 tel que log E_n(s*) = log(1/alpha) ; dichotomie."""
    h, lo, hi = math.log(1.0 / alpha), 0.0, 50.0 * math.sqrt(n) + 50.0
    for _ in range(200):
        mi = 0.5 * (lo + hi)
        if log_e_unilateral(mi, n, rho) < h:
            lo = mi
        else:
            hi = mi
    return 0.5 * (lo + hi)


def rho_optimal(n0: int, alpha: float) -> float:
    """ρ minimisant la frontière à l'horizon n0 (section dorée sur log ρ, bornes 1e-3 et 10)."""
    g = (math.sqrt(5.0) - 1.0) / 2.0
    lo, hi = math.log(1e-3), math.log(10.0)
    c, d = hi - g * (hi - lo), lo + g * (hi - lo)
    fc, fd = frontiere(n0, math.exp(c), alpha), frontiere(n0, math.exp(d), alpha)
    for _ in range(120):
        if fc < fd:
            hi, d, fd = d, c, fc
            c = hi - g * (hi - lo)
            fc = frontiere(n0, math.exp(c), alpha)
        else:
            lo, c, fc = c, d, fd
            d = lo + g * (hi - lo)
            fd = frontiere(n0, math.exp(d), alpha)
    return math.exp(0.5 * (lo + hi))


def rayon_dkw(m: int, eps_d: float, a_cal: float = A_CAL) -> float:
    """Rayon total : fraction déclarée + rayon bilatéral de Dvoretzky-Kiefer-Wolfowitz sur ⌊(1 − ε)m⌋ honnêtes."""
    mh = math.floor((1.0 - eps_d) * m + 1e-9)
    return eps_d + math.sqrt(math.log(2.0 / a_cal) / (2.0 * mh))


print("=== 1. Rayons (alpha_etalonnage = 0,025 ; forme bilatérale, constante 2)")
for m in (32, 100, 400, 1600, 6400, 1_000_000):
    print(f"  m = {m:>7} : " + " | ".join(f"eps_d = {e:.2f} : r = {rayon_dkw(m, e):.4f}" for e in (0.0, 0.02, 0.05, 0.10)))

print("=== 2. Contrôle de banc : construction naïve, loi normale, centre estimé sur m (échelle supposée connue)")
print("    borne inférieure exacte du taux de fausses alertes : P(E_n >= 1/alpha) à l'instant n seul,")
print("    S_n ~ N(0, n(1 + n/m)) en moyenne sur la référence ; bien spécifiée : S_n ~ N(0, n)")
for m in (100, 400):
    rho = rho_optimal(m, ALPHA)
    print(f"  m = {m}, rho*(m, alpha = 0,05) = {rho:.5f}")
    for k in (0.25, 1, 4, 16, 64):
        n = int(k * m)
        s = frontiere(n, rho, ALPHA)
        naive = 1.0 - N01.cdf(s / math.sqrt(n * (1.0 + n / m)))
        sain = 1.0 - N01.cdf(s / math.sqrt(n))
        # part des références où le taux conditionnel terminal dépasse 2 alpha : P(Phi_bar((s - n d)/sqrt n) > 0.10), d ~ N(0, 1/m)
        d_crit = (s - math.sqrt(n) * N01.inv_cdf(1.0 - 2 * ALPHA)) / n
        part = 1.0 - N01.cdf(d_crit * math.sqrt(m))
        print(f"    n/m = {k:>5} (n = {n:>5}) : frontière s* = {s:8.2f} ; naïve >= {naive:.4f} ; bien spécifiée (instant n) = {sain:.5f} ;"
              f" part des références à taux conditionnel terminal > 2 alpha = {part:.4f}")

# ---------- loi honnête principale : Beta(1, 4), Q(u) = 1 − (1 − u)^(1/4)
U = (np.arange(2_000_000) + 0.5) / 2_000_000   # grille déterministe de quadrature sur ]0, 1[


def q_beta14(u):
    return 1.0 - (1.0 - u) ** 0.25


def phi_inv(u):
    return np.array([N01.inv_cdf(float(x)) for x in u])


def gain(x, a, c):
    return np.clip((x - a) / (c - a), 0.0, 1.0)


def borne_enveloppe(valeurs_g_triees: np.ndarray, r: float) -> float:
    """Moyenne de g après déplacement de la masse r la plus basse vers 1 (grille uniforme de masses égales)."""
    k = r * valeurs_g_triees.size
    kf = int(math.floor(k))
    bas = valeurs_g_triees[:kf].sum() + (k - kf) * valeurs_g_triees[min(kf, valeurs_g_triees.size - 1)]
    return float((valeurs_g_triees.sum() - bas) / valeurs_g_triees.size + r)


X_H = q_beta14(U)                      # population honnête (triée)
A0, C0 = q_beta14(0.50), q_beta14(0.90)
G_H = gain(X_H, A0, C0)
MU_G, SD_G = float(G_H.mean()), float(G_H.std())
print("=== 3. Loi honnête Beta(1, 4) ; gain écrêté entre les quantiles 0,50 et 0,90")
print(f"  a = {A0:.4f}, c = {C0:.4f} ; moyenne du gain = {MU_G:.4f} ; écart type du gain = {SD_G:.4f} ; moyenne du score = {X_H.mean():.4f}")

# décalage diffus sur l'échelle latente : X = Q(Phi(Phi^-1(U) + d))
UG = (np.arange(200_000) + 0.5) / 200_000
ZG = phi_inv(UG)
PHI = np.vectorize(N01.cdf)
print("  décalage diffus latent d -> hausse de la moyenne du gain (a, c de la population honnête) ; distance de Kolmogorov")
for d in (0.05, 0.10, 0.15, 0.20, 0.30, 0.40, 0.50, 0.75, 1.00):
    xs = q_beta14(np.clip(PHI(ZG + d), 0.0, 1.0 - 1e-16))
    ks = float(np.max(np.abs(PHI(ZG + d) - UG)))
    print(f"    d = {d:.2f} : hausse = {gain(xs, A0, C0).mean() - gain(q_beta14(UG), A0, C0).mean():.4f} ; Kolmogorov = {ks:.4f}")

print("=== 4. Marge de population de l'enveloppe : borne − moyenne honnête du gain (référence contaminée infinie + rayon de m)")
print("    marge > 0 : dérive négative, tenue attendue ; marge < 0 : dérive positive, chute attendue aux longs horizons")


def reference_contaminee(eps: float, placement: str) -> np.ndarray:
    """Population de référence triée : mélange (1 − eps) honnête + eps contaminant, par grille de masses égales."""
    if eps == 0.0:
        return X_H
    n_c = int(round(eps * X_H.size / (1.0 - eps)))
    uc = (np.arange(n_c) + 0.5) / n_c
    if placement == "haut":            # sabotage visible : Beta(4, 1), Q(u) = u^(1/4)
        xc = uc ** 0.25
    elif placement == "seuil":         # dans la queue qui fixe le plafond : uniforme entre les quantiles honnêtes 0,90 et 0,97
        xc = q_beta14(0.90) + uc * (q_beta14(0.97) - q_beta14(0.90))
    elif placement == "bas":           # score minimal
        xc = np.zeros(n_c)
    else:
        raise ValueError(placement)
    return np.sort(np.concatenate([X_H, xc]))


for m in (400, 1600):
    for eps_d in (0.02, 0.10):
        r = rayon_dkw(m, eps_d)
        for eps in (0.0, eps_d, 2 * eps_d):
            for pl in (("-",) if eps == 0.0 else ("haut", "seuil", "bas")):
                ref = reference_contaminee(eps, pl if pl != "-" else "haut")
                a, c = np.quantile(ref, 0.50), np.quantile(ref, 0.90)
                borne = borne_enveloppe(np.sort(gain(ref, a, c)), r)
                vrai = float(gain(X_H, a, c).mean())
                naive = float(gain(ref, a, c).mean())
                # horizon où la dérive positive atteint la frontière (échelle de Hoeffding 1/2), si marge < 0
                marge = borne - vrai
                print(f"  m = {m:>4} eps_d = {eps_d:.2f} r = {r:.4f} eps_réel = {eps:.2f} placement = {pl:<5} :"
                      f" marge enveloppe = {marge:+.4f} ; marge naïve (rayon nul) = {naive - vrai:+.4f} ; a = {a:.3f} c = {c:.3f}")

print("=== 4 bis. Rognage haut naïf (retirer la fraction eps_d la plus haute de la référence, rayon nul) : marge de population")
for eps_d, reels in ((0.02, (0.0, 0.02, 0.04)), (0.10, (0.0, 0.02, 0.10, 0.20))):
    for eps in reels:
        for pl in (("-",) if eps == 0.0 else ("haut", "seuil", "bas")):
            ref = reference_contaminee(eps, pl if pl != "-" else "haut")
            garde = ref[: int(round((1.0 - eps_d) * ref.size))]
            a, c = np.quantile(garde, 0.50), np.quantile(garde, 0.90)
            marge = gain(garde, a, c).mean() - gain(X_H, a, c).mean()
            et = float(gain(garde, a, c).std())
            print(f"  eps_d = {eps_d:.2f} eps_réel = {eps:.2f} placement = {pl:<5} : marge = {marge:+.4f} ; écart type du gain rogné = {et:.3f} ;"
                  f" dérive standardisée × 400 = {-marge / et * 400:+.1f} (frontière à n = 400, alpha = 0,05 : 55,3)")
print("=== 4 quater. Construction naïve sous contamination : dérive standardisée cumulée à n = m = 400 et à 4m (frontières 55,3 et 114,8)")
for eps, pl in ((0.02, "bas"), (0.04, "bas"), (0.10, "bas"), (0.20, "bas")):
    ref = reference_contaminee(eps, pl)
    a, c = np.quantile(ref, 0.50), np.quantile(ref, 0.90)
    marge = gain(ref, a, c).mean() - gain(X_H, a, c).mean()
    et = float(gain(ref, a, c).std())
    print(f"  eps_réel = {eps:.2f} placement bas : marge = {marge:+.4f} ; à n = 400 : {-marge / et * 400:+.1f} ; à n = 1600 : {-marge / et * 1600:+.1f}")
print("=== 4 quinquies. Vivacité : sabotage massif (décalage latent 2) contre la plus grande marge de l'enveloppe (m = 100, eps_d = 0,10)")
xs = q_beta14(np.clip(PHI(ZG + 2.0), 0.0, 1.0 - 1e-16))
hausse = gain(xs, A0, C0).mean() - MU_G
r_max = rayon_dkw(100, 0.10)
rho_v = rho_optimal(100, A_ARRET)
print(f"  hausse du gain = {hausse:.4f} ; rayon maximal = {r_max:.4f} ; dérive nette × n / 0,5 à n = 100 : {(hausse - r_max) * 100 / 0.5:.1f} ; frontière à n = 100 : {frontiere(100, rho_v, A_ARRET):.1f}")

print("=== 4 ter. Dérive bénigne latente d du déploiement (référence propre) : marge de l'enveloppe")
for m in (400, 1600):
    for eps_d in (0.02, 0.10):
        r = rayon_dkw(m, eps_d)
        borne = borne_enveloppe(np.sort(G_H), r)
        for d in (0.05, 0.10, 0.20, 0.40, 0.80):
            xs = q_beta14(np.clip(PHI(ZG + d), 0.0, 1.0 - 1e-16))
            print(f"  m = {m:>4} eps_d = {eps_d:.2f} r = {r:.4f} d = {d:.2f} : marge = {borne - gain(xs, A0, C0).mean():+.4f}")

print("=== 5. Horizon de chute sous dérive positive : plus petit n tel que n × dérive >= frontière (échelle 1/2, alpha_arrêt = 0,025, rho*(400))")
RHO_E = rho_optimal(400, A_ARRET)
print(f"  rho*(400 ; 0,025) = {RHO_E:.5f}")
for derive in (0.005, 0.01, 0.02, 0.03, 0.05):
    n = 10
    while n * derive / 0.5 < frontiere(n, RHO_E, A_ARRET) and n < 10_000_000:
        n = int(n * 1.02) + 1
    print(f"  dérive du gain = {derive:.3f} par épisode : n ≈ {n}")

print("=== 6. Prix de la garantie : décalage standardisé détecté à puissance un demi (médiane de S_n à la frontière), loi connue")
for (m, alpha) in ((400, A_ARRET), (400, ALPHA)):
    rho = rho_optimal(m, alpha)
    z = N01.inv_cdf(1.0 - alpha)
    for n in (100, 400, 1600, 6400):
        s = frontiere(n, rho, alpha)
        print(f"  alpha = {alpha:.3f} rho*({m}) n = {n:>5} : processus e (instant n) = {s / n:.4f} ; somme à horizon fixe = {z / math.sqrt(n):.4f} ; rapport = {s / (z * math.sqrt(n)):.2f}")

print("=== 7. Duel sur la pente : planchers de population (décalage additif diffus), référence contaminée au plafond du support")


def plancher(loi: str, eps: float, r: float, regle: str) -> float:
    """Plus petit décalage additif D tel que E g(X + D) >= borne de l'enveloppe (population ; contamination réelle eps placée à 1)."""
    if loi == "etale":
        xh = UG.copy()
    else:
        xh = 0.2 + 0.02 * math.sqrt(3.0) * (2.0 * UG - 1.0)
    n_c = int(round(eps * xh.size / (1.0 - eps)))
    ref = np.sort(np.concatenate([xh, np.ones(n_c)]))
    med = float(np.quantile(ref, 0.5))
    s0 = float((np.quantile(ref, 0.75) - np.quantile(ref, 0.25)) / 1.349)
    if regle == "variance":
        a, c = max(0.0, med - s0 / math.sqrt(r)), min(1.0, med + s0 / math.sqrt(r))
    elif regle == "support":
        a, c = 0.0, 1.0
    else:                               # quantiles de la référence
        a, c = float(np.quantile(ref, 0.50)), float(np.quantile(ref, 0.90))
    borne = borne_enveloppe(np.sort(gain(ref, a, c)), r)
    lo, hi = 0.0, 1.0
    if gain(np.minimum(xh + hi, 1.0), a, c).mean() < borne:
        return float("nan")
    for _ in range(60):
        mi = 0.5 * (lo + hi)
        if gain(np.minimum(xh + mi, 1.0), a, c).mean() < borne:
            lo = mi
        else:
            hi = mi
    return hi


EPS = (0.01, 0.02, 0.04, 0.08)
M_DUEL = 1_000_000
for loi, s0_vrai, portee in (("etale", 1.0 / math.sqrt(12.0), 0.5), ("concentre", 0.02, 0.8)):
    print(f"  loi {loi} : écart type {s0_vrai:.4f}, portée au plafond {portee:.2f}, bascule (sigma0/portée)^2 = {(s0_vrai / portee) ** 2:.5f}")
    for regle in ("variance", "support", "quantiles"):
        rs = [rayon_dkw(M_DUEL, e) for e in EPS]
        pl = [plancher(loi, e, r, regle) for e, r in zip(EPS, rs)]
        pente = np.polyfit(np.log(rs), np.log(pl), 1)[0]
        pente_bas = math.log(pl[1] / pl[0]) / math.log(rs[1] / rs[0])
        pente_haut = math.log(pl[3] / pl[2]) / math.log(rs[3] / rs[2])
        print(f"    règle {regle:<9} : planchers = " + ", ".join(f"{p:.5f}" for p in pl)
              + f" ; pente = {pente:.3f} (bas {pente_bas:.3f}, haut {pente_haut:.3f})"
              + " ; rapports à sigma0·racine(r) = " + ", ".join(f"{p / (s0_vrai * math.sqrt(r)):.2f}" for p, r in zip(pl, rs))
              + " ; rapports à r = " + ", ".join(f"{p / r:.2f}" for p, r in zip(pl, rs)))
    # terme séquentiel à n = 10^6 (frontière / n, échelle de Hoeffding 1/2 sur le gain, ramenée à l'échelle du score)
rho_d = rho_optimal(M_DUEL, A_ARRET)
s_d = frontiere(M_DUEL, rho_d, A_ARRET)
print(f"  terme séquentiel à n = 10^6 : frontière/n = {s_d / M_DUEL:.6f} en unités de Hoeffding, soit {0.5 * s_d / M_DUEL:.6f} sur le gain")
