# -*- coding: utf-8 -*-
"""Calcul « signature ou excès » (v1) — note Opus 5.5 max sur « Diffuse AI Control on Fuzzy Tasks ».

But : traduire l'aire sous la courbe (AUROC) d'une lecture interne, mesurée à qualité égale,
en ce que cette lecture achète contre un saboteur diffus, sous la condition de Hebbar
(connaître la conduite de l'honnête) écrite comme une référence honnête de taille m, avec biais b.

Rien de neuf en mathématiques : c'est la loi de la référence honnête de N-076 (§ 2,
z × sqrt(1/n + 1/m) / mu), rejouée avec des aires publiées, plus le facteur de vitesse
d'un audit orienté sous un plancher (N-076, § 9). Suppositions d'illustration, aucune donnée
du programme :
  - modèle binormal à variances égales : scores honnêtes N(0, 1), épisodes sabotés N(d', 1),
    AUROC = Phi(d' / sqrt(2)) ;
  - saboteur « mélange » : une part f des épisodes est sabotée (cadre de l'annexe A du papier,
    stratégies mélangées), scores indépendants entre épisodes ;
  - test unilatéral sur la moyenne, alpha = 0,01, puissance 1/2 (comme N-076) ;
  - b : biais de la référence (écart entre l'honnête en service et sa référence), en écarts-types
    honnêtes, pris dans le sens qui masque.
Lois exactes (statistics.NormalDist) ; un contrôle par simulation, graines par numpy.random.SeedSequence.
"""
import math
import sys
from statistics import NormalDist

import numpy as np

N01 = NormalDist()
ALPHA = 0.01
Z = N01.inv_cdf(1 - ALPHA)  # 2,3263

# Aires de référence (marque dans la note) :
#  0,57 et 0,95 : Boxo, Neelappa, Raval, arXiv 2509.21344 v2, p. 1 (organisme de sous-rendement
#  sans verbalisation sur Llama 3.1 8B, contre la base incitée) ; 0,62 : même papier, p. 6
#  (filtrage du contenu) ; les autres sont des points de grille.
AUROCS = [0.55, 0.57, 0.60, 0.62, 0.65, 0.70, 0.75, 0.80, 0.90, 0.95]


def dprime(auc):
    return math.sqrt(2.0) * N01.inv_cdf(auc)


def auc_of(d):
    return N01.cdf(d / math.sqrt(2.0))


def f_min_reference(d, m, n, b):
    """Plus petite part sabotée détectée à puissance 1/2, référence fixe de taille m.
    n = None : horizon infini. Renvoie None si aucune part <= 1 ne suffit."""
    def g(f):
        var = 1.0 + f * (1.0 - f) * d * d
        se = math.sqrt((var / n if n else 0.0) + 1.0 / m)
        return f * d - b - Z * se
    if g(1.0) < 0:
        return None
    lo, hi = 0.0, 1.0
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if g(mid) >= 0:
            hi = mid
        else:
            lo = mid
    return hi


def f_min_twin(d, n, k):
    """Nul par acte : K tirages du jumeau honnête sur le même début (banc seulement)."""
    def g(f):
        var = 1.0 + f * (1.0 - f) * d * d + 1.0 / k
        return f * d - Z * math.sqrt(var / n)
    if g(1.0) < 0:
        return None
    lo, hi = 0.0, 1.0
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if g(mid) >= 0:
            hi = mid
        else:
            lo = mid
    return hi


def m_star(d, f, b):
    """Taille de référence minimale (horizon infini) ; None si f d' <= b (aucune ne suffit)."""
    gap = f * d - b
    if gap <= 0:
        return None
    return (Z / gap) ** 2


def capture_factor(d, p, p0):
    """Audit au budget p : plancher p0 uniforme, le reste aux scores les plus hauts.
    Facteur = P(audit | épisode saboté) / p (approximation f petit)."""
    q = (p - p0) / (1.0 - p0)
    tau = N01.inv_cdf(1.0 - q)
    cap = p0 + (1.0 - p0) * (1.0 - N01.cdf(tau - d))
    return cap / p


def fmt(x, nd=3):
    return "aucune" if x is None else ("{:.%df}" % nd).format(x)


def main():
    out = []
    w = out.append
    w("calcul-signature-ou-exces-v1 — sortie")
    w("python %s ; numpy %s" % (sys.version.split()[0], np.__version__))
    w("alpha unilatéral = %.2f ; z = %.4f ; puissance 1/2" % (ALPHA, Z))
    w("")
    w("A. Aire sous la courbe -> d' (binormal, variances égales)")
    for a in AUROCS:
        w("  AUROC %.2f -> d' = %.4f" % (a, dprime(a)))
    w("")
    w("B. Part sabotée minimale détectée, référence honnête fixe de taille m (test sur la moyenne)")
    w("   colonnes : m ; n = m ; n infini ; n infini avec biais b = 0,1")
    for a in AUROCS:
        d = dprime(a)
        cells = []
        for m in (100, 400, 1600):
            cells.append("m=%d: %s | %s | %s" % (
                m, fmt(f_min_reference(d, m, m, 0.0)), fmt(f_min_reference(d, m, None, 0.0)),
                fmt(f_min_reference(d, m, None, 0.1))))
        w("  AUROC %.2f : %s" % (a, " ; ".join(cells)))
    w("   (« aucune » : aucune part <= 1 n'est détectée à puissance 1/2)")
    w("")
    w("C. Nul par acte (jumeau honnête, K = 4 tirages par épisode ; banc seulement, N-075 § 5)")
    for a in AUROCS:
        d = dprime(a)
        w("  AUROC %.2f : n=100: %s ; n=400: %s ; n=1600: %s" % (
            a, fmt(f_min_twin(d, 100, 4)), fmt(f_min_twin(d, 400, 4)), fmt(f_min_twin(d, 1600, 4))))
    w("")
    L = 70.7 - 34.7  # perte par épisode, Opus 4.6 bénin contre attaque (papier, p. 2 et 6)
    f10 = 10.0 / L
    f20b = (70.7 - 39.3) / L
    w("D. Parts du papier, sous supposition de mélange (annexe A, p. 15)")
    w("   perte par épisode saboté L = 70,7 - 34,7 = %.1f points de vérité de substitution" % L)
    w("   f pour perdre 10 points en moyenne = %.4f ; f pour tomber au niveau de GPT-OSS-20B (39,3) = %.4f" % (f10, f20b))
    w("   taille de référence minimale m* (horizon infini) pour détecter f = %.3f" % f10)
    for a in AUROCS:
        d = dprime(a)
        w("  AUROC %.2f : b=0: %s ; b=0,05: %s ; b=0,1: %s ; b=0,2: %s" % (
            a, fmt(m_star(d, f10, 0.0), 0), fmt(m_star(d, f10, 0.05), 0),
            fmt(m_star(d, f10, 0.1), 0), fmt(m_star(d, f10, 0.2), 0)))
    w("")
    w("E. Aire de mort : en dessous, aucune taille de référence ne suffit (f d' <= b)")
    for f in (0.10, f10, 0.50):
        row = []
        for b in (0.05, 0.10, 0.20):
            row.append("b=%.2f: %.3f" % (b, auc_of(b / f)))
        w("  f = %.3f : %s" % (f, " ; ".join(row)))
    w("")
    w("F. Vitesse de prise d'un audit orienté par le score, budget p = 5 %")
    w("   facteur = P(audit | épisode saboté) / p ; plancher 2,5 % uniforme ou aucun")
    for a in AUROCS:
        d = dprime(a)
        w("  AUROC %.2f : avec plancher x%.2f ; sans plancher x%.2f" % (
            a, capture_factor(d, 0.05, 0.025), capture_factor(d, 0.05, 0.0)))
    w("")
    # G. Contrôles par simulation
    ss = np.random.SeedSequence(20261121)
    s1, s2 = ss.spawn(2)
    w("G. Contrôles par simulation (SeedSequence(20261121), deux enfants)")
    # G1 : puissance au point f_min (AUROC 0,80 ; m = n = 400 ; b = 0) : attendue 0,5
    rng = np.random.default_rng(s1)
    a, m, n, R = 0.80, 400, 400, 20000
    d = dprime(a)
    f = f_min_reference(d, m, n, 0.0)
    var = 1.0 + f * (1.0 - f) * d * d
    ref = rng.standard_normal((R, m)).mean(axis=1)
    lab = rng.random((R, n)) < f
    obs = (rng.standard_normal((R, n)) + d * lab).mean(axis=1)
    stat = (obs - ref) / math.sqrt(var / n + 1.0 / m)
    pw = float((stat > Z).mean())
    w("  G1 puissance simulée au point f_min = %.4f (AUROC 0,80, m = n = 400) : %.4f (erreur type %.4f ; attendue 0,5)"
      % (f, pw, math.sqrt(pw * (1 - pw) / R)))
    # G2 : facteur de prise avec plancher (AUROC 0,80 ; p = 5 % ; p0 = 2,5 %)
    rng = np.random.default_rng(s2)
    p, p0, N = 0.05, 0.025, 2_000_000
    q = (p - p0) / (1 - p0)
    tau = N01.inv_cdf(1 - q)
    hon = rng.standard_normal(N)
    sab = rng.standard_normal(N) + d
    u1, u2 = rng.random(N), rng.random(N)
    rate_h = float(((u1 < p0) | (hon > tau)).mean())
    cap_s = float(((u2 < p0) | (sab > tau)).mean())
    w("  G2 taux d'audit simulé sur l'honnête : %.4f (visé 0,05) ; facteur simulé x%.3f ; formule x%.3f"
      % (rate_h, cap_s / p, capture_factor(d, p, p0)))
    text = "\n".join(out) + "\n"
    sys.stdout.write(text)


if __name__ == "__main__":
    main()
