# -*- coding: utf-8 -*-
"""Calculs de la note « dommage » (Opus 5.5, effort maximal) — v1.

Pièce de travail. Aucune donnée du programme : toutes les entrées sont des
suppositions d'illustration, écrites ici. Lois exactes (binomiale, normale)
et tirages à graines dérivées de numpy.random.SeedSequence (racine écrite).

Blocs :
  A0  borne à deux points, régime d'excès homogène : ce qu'aucun test de
      niveau alpha ne voit, selon le taux honnête f de « reconnu endommagé »
      (f = 0 : régime de signature).
  A1  la cachette est la variance honnête : dommage d'excès invisible
      D* = z * sqrt(V (1 + 1/K) / p) / q, avec V = somme des a_i (1 - a_i)
      sur les tâches confiées ; vérification par tirages ; budget de
      variance et seuil fixe par construction.
  B   dommage concentré (transposition de la condition de 2606.09931, p. 5) :
      à masse lue bornée, le dommage atteignable suit les plus grands enjeux ;
      retirer la sélection aux points de plus fort enjeu.
  C   indiscernabilité certifiée pour une classe finie d'observateurs :
      coût en paires, monde planté (dommage lu, dommage non lu, variante
      honnête), borne cumulée sur un flux d'audit.
  D   épreuve du devin : paires nécessaires ; biais d'un tirage qui fuit.
  E   prix du déplacement : épisodes par bras pour voir une perte de réussite.
"""
import math
import sys

import numpy as np
from scipy import stats

RACINE = 20261121
SS = np.random.SeedSequence(RACINE)
ENFANTS = SS.spawn(8)  # une graine par bloc à tirages, dérivée de la racine

Z = stats.norm.ppf
ALPHA = 0.01


def titre(s):
    print()
    print("=" * 78)
    print(s)
    print("=" * 78)


print("calculs-dommage-opus-max-v1.py ; numpy", np.__version__, "; scipy",
      __import__("scipy").__version__, "; python", sys.version.split()[0])
print("graine racine SeedSequence :", RACINE)

# ---------------------------------------------------------------------------
titre("A0  Borne à deux points, régime d'excès homogène (test le plus puissant)")
# N audits ~ p T (conditionné) ; sous l'honnête, chaque audit dit « endommagé »
# avec probabilité f ; sous le saboteur, f + q*delta. Test de Neyman-Pearson
# randomisé de niveau exact alpha (le plus puissant pour cette alternative) :
# tout autre test de niveau alpha fait moins bien. D = delta * T est l'excès
# cumulé que le saboteur peut laisser sans être vu avec la puissance visée.


def np_test(N, f, alpha=ALPHA):
    """Seuil c et randomisation g du test le plus puissant de niveau alpha."""
    c = 0
    while stats.binom.sf(c, N, f) > alpha:
        c += 1
    pc = stats.binom.pmf(c, N, f)
    g = (alpha - stats.binom.sf(c, N, f)) / pc if pc > 0 else 0.0
    return c, g


def puissance(N, f, f1, c, g):
    return stats.binom.sf(c, N, f1) + g * stats.binom.pmf(c, N, f1)


def excess_invisible(T, f, p=0.05, q=1.0, cible=0.5):
    N = int(round(p * T))
    c, g = np_test(N, f)
    lo, hi = 0.0, (1.0 - f) / q
    for _ in range(80):
        mid = 0.5 * (lo + hi)
        if puissance(N, f, f + q * mid, c, g) < cible:
            lo = mid
        else:
            hi = mid
    return hi * T, N, c


p, q = 0.05, 1.0
print(f"entrées : p = {p} (part auditée), q = {q} (reconnaissance), alpha = {ALPHA}")
for cible in (0.5, 0.95):
    zb = Z(cible) if cible > 0.5 else 0.0
    print(f"\npuissance visée {cible} : excès cumulé invisible D (épisodes) ; "
          f"en tête de ligne f ; entre crochets, seuil c du test")
    Ts = [1e3, 1e4, 1e5, 1e6]
    print("   f        " + "".join(f"T={int(t):>9d}      " for t in Ts))
    for f in (0.0, 1e-4, 1e-3, 1e-2, 1e-1):
        cells = []
        for T in Ts:
            D, N, c = excess_invisible(T, f, p, q, cible)
            cells.append(f"{D:9.1f} [c={c:>3d}]")
        print(f"  {f:<8g} " + "  ".join(cells))
    # contrôles : f = 0 -> D p q = ln((1-alpha)/(1-cible)) ; f > 0, grand T ->
    # D ~ (z_{1-alpha} + z_cible) sqrt(f (1-f) T / p) / q
    D0, _, _ = excess_invisible(1e6, 0.0, p, q, cible)
    print(f"  contrôle f = 0 : D p q = {D0 * p * q:.4f} ; prévu "
          f"ln((1-alpha)/(1-puissance)) = {math.log((1 - ALPHA) / (1 - cible)):.4f}")
    for f in (1e-2, 1e-1):
        D, _, _ = excess_invisible(1e6, f, p, q, cible)
        prev = (Z(1 - ALPHA) + zb) * math.sqrt(f * (1 - f) * 1e6 / p) / q
        print(f"  contrôle f = {f:g}, T = 1e6 : D = {D:.1f} ; approximation normale {prev:.1f}")

print("\nhorizon du seuil fixe : plus grand T (grille) où D(T) <= 2 x D(f = 0), puissance 0,5")
Tgrid = np.unique(np.round(np.logspace(2, 7, 61)).astype(int))
Dsig, _, _ = excess_invisible(1e4, 0.0, p, q, 0.5)
for f in (1e-4, 1e-3, 1e-2):
    best = None
    for T in Tgrid:
        D, _, _ = excess_invisible(float(T), f, p, q, 0.5)
        if D <= 2 * Dsig:
            best = int(T)
    print(f"  f = {f:g} : T_max ~ {best} épisodes, soit {best * p:.0f} audits ; "
          f"alpha/(p f) = {ALPHA / (p * f):.0f} épisodes ; 1/(p f) = {1 / (p * f):.0f}")

# ---------------------------------------------------------------------------
titre("A1  La cachette est la variance honnête : D* = z sqrt(V (1+1/K) / p) / q")
# Tâches hétérogènes : a_i = probabilité qu'un audit dise « endommagé » chez
# l'honnête sur la tâche i (échec honnête ou fausse reconnaissance). Le
# saboteur répartit son excès delta_i ; contre l'allocation delta_i ~ a_i(1-a_i),
# le test le plus puissant est la somme (issue - référence) : le bilan.
# Le plus grand excès que ce test ne voit qu'une fois sur deux, à niveau alpha :
# D* = z_{1-alpha} sqrt(V / p) / q ; avec une référence par K tirages du jumeau
# sur la même tâche, V est multiplié par (1 + 1/K).
classes = {"facile": (0.60, 0.002), "moyenne": (0.30, 0.05), "dure": (0.10, 0.30)}
z = Z(1 - ALPHA)
print("mélange supposé (part des tâches, taux honnête a) :",
      ", ".join(f"{k} ({w:.2f}, {a})" for k, (w, a) in classes.items()))
for T in (1e4, 1e5):
    print(f"\nT = {int(T)} tâches, p = {p}, q = {q}")
    for nom, garder in (("tout confié", ("facile", "moyenne", "dure")),
                        ("dures confiées ailleurs", ("facile", "moyenne")),
                        ("seules les faciles", ("facile",))):
        V = sum(w * T * a * (1 - a) for k, (w, a) in classes.items() if k in garder)
        F = sum(w * T * a for k, (w, a) in classes.items() if k in garder)
        parts = sum(w for k, (w, a) in classes.items() if k in garder)
        D = z * math.sqrt(V / p) / q
        print(f"  {nom:<26s} part confiée {parts:4.2f} ; échecs honnêtes attendus F = {F:8.1f} ; "
              f"V = {V:8.1f} ; D* = {D:7.1f} épisodes")
print("\nréférence par K tirages du jumeau : facteur sqrt(1 + 1/K) sur D*")
for K in (1, 4, 16, 64):
    print(f"  K = {K:>2d} : x {math.sqrt(1 + 1 / K):.3f}")

print("\nseuil fixe par construction : budget F_max = p (K_seuil q / z)^2 d'échecs honnêtes "
      "attendus sur les tâches confiées")
for Ks in (30, 100, 300):
    Fmax = p * (Ks * q / z) ** 2
    print(f"  seuil K = {Ks:>3d} épisodes d'excès, p = {p} : F_max = {Fmax:7.1f} ; "
          f"soit {Fmax / 0.002:9.0f} tâches à a = 0,002, {Fmax / 0.05:7.0f} à a = 0,05, "
          f"{Fmax / 0.30:6.0f} à a = 0,30")

# vérification par tirages (approximation normale du seuil, conditionnée aux audits)
rng = np.random.default_rng(ENFANTS[0])
T = 20000
w = np.array([v[0] for v in classes.values()])
av = np.array([v[1] for v in classes.values()])
cls = rng.choice(3, size=T, p=w)
a = av[cls]
v = a * (1 - a)
V = v.sum()
Dstar = z * math.sqrt(V / p) / q
lam = Dstar / V
delta = np.minimum(lam * v, 1 - a)
R = 4000
rej0 = rej1 = 0
for r in range(R):
    aud = rng.random(T) < p
    va = v[aud].sum()
    seuil = z * math.sqrt(va)
    x0 = rng.random(T) < a
    x1 = rng.random(T) < (a + q * delta)
    s0 = (x0[aud] - a[aud]).sum()
    s1 = (x1[aud] - a[aud]).sum()
    rej0 += s0 > seuil
    rej1 += s1 > seuil
print(f"\ntirages (T = {T}, R = {R}, mélange ci-dessus) : D* = {Dstar:.1f} ; "
      f"niveau observé {rej0 / R:.4f} (visé {ALPHA}) ; puissance observée {rej1 / R:.4f} (prévue 0,5)")

# ---------------------------------------------------------------------------
titre("B  Dommage concentré : la masse lue ne borne le dommage qu'au plus grand enjeu près")
# J décisions ; enjeu I_j (Pareto, x_m = 1) ; l'honnête choisit l'option
# nuisible plausible avec probabilité h_j (sa liberté légitime).
# Cas 1, choix observés en entier : le saboteur déplace Delta_j sous un budget
# de masse lue sum Delta_j^2 / (h_j (1-h_j)) <= Bm (au plus une chance sur deux
# d'être vu à 1 %) ; dommage atteignable sum Delta_j I_j (remplissage exact).
# Cas 2, choix non lus (M3) : tout écart passe ; dommage sum (1 - h_j) I_j.
# Défense : le hasard du défenseur ou le jumeau décide aux phi % de points de
# plus fort enjeu (Delta_j = 0 forcé).
rng = np.random.default_rng(ENFANTS[1])
J = 10000
Bm = z ** 2
h = rng.uniform(0.05, 0.5, size=J)
vh = h * (1 - h)


def dommage_sous_budget(I, mask):
    """max sum Delta I  s.c.  sum Delta^2/vh <= Bm, 0 <= Delta <= 1-h, Delta=0 hors mask."""
    cap = np.where(mask, 1 - h, 0.0)
    lo, hi = 0.0, 1e6
    for _ in range(200):
        lam = 0.5 * (lo + hi)
        d = np.minimum(lam * I * vh, cap)
        if (d ** 2 / vh).sum() > Bm:
            hi = lam
        else:
            lo = lam
    d = np.minimum(lo * I * vh, cap)
    return (d * I).sum()


for alpha_tail in (1.2, 1.5, 2.5):
    I = rng.pareto(alpha_tail, size=J) + 1.0
    order = np.argsort(-I)
    Ibar = np.full(J, I.mean())
    tout = np.ones(J, bool)
    Hobs = dommage_sous_budget(I, tout)
    Hdiff = dommage_sous_budget(Ibar, tout)
    Hm3 = ((1 - h) * I).sum()
    print(f"\nqueue de Pareto {alpha_tail} : enjeu total {I.sum():.0f}, plus grand {I.max():.0f}, "
          f"part des 1 % les plus forts {I[order[:J // 100]].sum() / I.sum():.3f}")
    print(f"  choix lus, même masse : dommage atteignable {Hobs:8.1f} ; à enjeux égaux "
          f"(même total) {Hdiff:6.1f} ; rapport {Hobs / Hdiff:5.1f}")
    for phi in (0.0, 0.001, 0.01, 0.05, 0.10):
        mask = np.ones(J, bool)
        k = int(round(phi * J))
        mask[order[:k]] = False
        Ho = dommage_sous_budget(I, mask)
        Hu = ((1 - h) * I)[mask].sum()
        print(f"  sélection retirée aux {phi * 100:5.1f} % de plus fort enjeu : "
              f"choix lus {Ho:8.1f} ({Ho / Hobs:5.3f}) ; choix non lus, M3 {Hu:9.1f} ({Hu / Hm3:5.3f})")

# ---------------------------------------------------------------------------
titre("C  Indiscernabilité certifiée pour une classe finie de k observateurs")
# Paires (suspect, jumeau) sur les mêmes tâches ; observateur j binaire ;
# avantage A_j = |P_S(g_j = 1) - P_J(g_j = 1)|. Certificat : max_j |Â_j| + largeur.
# Largeur de Hoeffding avec union sur 2k côtés : sqrt(2 ln(2k/eta) / n).
# Largeur de Bernstein empirique (Maurer et Pontil, étendue à [-1, 1]) :
# sqrt(2 Vn ln(4k/eta) / n) + 14 ln(4k/eta) / (3 (n - 1)), Vn ~ taux de discordance r.
k, eta = 10, 0.05
print(f"k = {k} observateurs, risque eta = {eta}")
print("  n paires   Hoeffding   Bernstein r=0,02   r=0,10   r=0,50")
for n in (100, 1000, 10000, 100000):
    hw = math.sqrt(2 * math.log(2 * k / eta) / n)
    bw = [math.sqrt(2 * r * math.log(4 * k / eta) / n) + 14 * math.log(4 * k / eta) / (3 * (n - 1))
          for r in (0.02, 0.10, 0.50)]
    print(f"  {n:>8d}   {hw:9.4f}   {bw[0]:16.4f}   {bw[1]:6.4f}   {bw[2]:6.4f}")
print("paires pour certifier une largeur de 0,01 :")
for r in (None, 0.02, 0.10):
    n = 10
    while True:
        if r is None:
            wdt = math.sqrt(2 * math.log(2 * k / eta) / n)
        else:
            wdt = math.sqrt(2 * r * math.log(4 * k / eta) / n) + 14 * math.log(4 * k / eta) / (3 * (n - 1))
        if wdt <= 0.01:
            break
        n = int(n * 1.01) + 1
    print(f"  {'Hoeffding' if r is None else f'Bernstein, r = {r}':<20s} : n ~ {n}")

# monde planté : 6 traits par produit ; les observateurs lisent les traits 1 à 5
# (g_j = 1[x_j > 1]) ; le trait 6 n'est lu par personne.
rng = np.random.default_rng(ENFANTS[2])
n = 2000
kk = 5
wdt = math.sqrt(2 * math.log(2 * kk / eta) / n)
print(f"\nmonde planté : n = {n} paires, {kk} observateurs à seuil, largeur de Hoeffding {wdt:.4f}")


def certificat(dx):
    J0 = rng.standard_normal((n, 6))
    S0 = rng.standard_normal((n, 6)) + dx
    adv = [abs((S0[:, j] > 1).mean() - (J0[:, j] > 1).mean()) for j in range(kk)]
    return max(adv) + wdt


def vrai_avantage(shift):
    return abs(stats.norm.sf(1 - shift) - stats.norm.sf(1))


cas = [("jumeau contre jumeau", np.zeros(6), 0.0),
       ("dommage dans le trait 6, non lu (dose 1,0)", np.array([0, 0, 0, 0, 0, 1.0]), 1.0),
       ("dommage dans le trait 1, lu (dose 0,1)", np.array([0.1, 0, 0, 0, 0, 0]), 0.1),
       ("dommage dans le trait 1, lu (dose 0,3)", np.array([0.3, 0, 0, 0, 0, 0]), 0.3),
       ("variante honnête : décalage bénin du trait 2 (0,3)", np.array([0, 0.3, 0, 0, 0, 0]), 0.0)]
for nom, dx, dose in cas:
    eps = certificat(dx)
    va = max(vrai_avantage(s) for s in dx[:kk])
    print(f"  {nom:<52s} certificat eps = {eps:.4f} ; avantage vrai max {va:.4f} ; "
          f"dommage vrai {dose:.1f}")

print("\nborne cumulée sur un flux d'audit (certificat refait sur n = p T paires, plafond 1 par épisode) :")
for T in (1e3, 1e4, 1e5, 1e6):
    nn = p * T
    bound = T * math.sqrt(2 * math.log(2 * k / eta) / nn)
    print(f"  T = {int(T):>8d} : borne T x largeur = {bound:10.1f} ; rapport à sqrt(T / p) = "
          f"{bound / math.sqrt(T / p):.3f}")

# ---------------------------------------------------------------------------
titre("D  Épreuve du devin : épisodes pour voir une fuite ; biais d'une pièce qui fuit")
zb = Z(0.95)
print("épisodes pour voir, à 1 % et puissance 0,95, une précision de devin 1/2 + e (secret binaire équilibré)")
for e in (0.05, 0.02, 0.01, 0.005):
    nn = ((z + zb) / (2 * e)) ** 2
    print(f"  e = {e:<6g} : n ~ {nn:9.0f}")
print("biais au pire d'un taux certifié quand la pièce d'audit fuit : (1 - p) x d (« Blindfold », repris)")
for pp in (0.01, 0.05, 0.20):
    print("  p = %-5g : " % pp + " ; ".join(f"d = {d:g} -> {(1 - pp) * d:.4f}" for d in (0.005, 0.02, 0.05)))

# ---------------------------------------------------------------------------
titre("E  Prix du déplacement : épisodes honnêtes par bras pour voir une perte de réussite")
# deux proportions, unilatéral, alpha = 0,01, puissance 0,95 ; réussite sous
# direction au hasard p0, sous la direction lue p0 - Delta.
p0 = 0.60
for dlt in (0.02, 0.05, 0.10):
    p1 = p0 - dlt
    pb = 0.5 * (p0 + p1)
    nn = (z * math.sqrt(2 * pb * (1 - pb)) + zb * math.sqrt(p0 * (1 - p0) + p1 * (1 - p1))) ** 2 / dlt ** 2
    print(f"  perte {dlt:.2f} sur une réussite de {p0:.2f} : n ~ {nn:7.0f} épisodes par bras")

print("\nfin des calculs")
