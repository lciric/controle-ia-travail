"""Illustration (flottants, non contre-lue) : aires atteignables par une loi normale arrondie, et issue de trois conduites
d'auteur sous la tolérance proposée. Aucune donnée du programme : lois et nombres choisis ici."""
import math
from statistics import NormalDist

def reseau(mu, sigma, h, k=14):
    nd = NormalDist(mu, sigma)
    n0 = round(mu / h)
    pts = range(n0 - int(k * sigma / h) - 2, n0 + int(k * sigma / h) + 3)
    return {i: nd.cdf((i + 0.5) * h) - nd.cdf((i - 0.5) * h) for i in pts}

def loi_diff(m):  # D = Y - X
    d = {}
    for i, p in m.items():
        for j, q in m.items():
            d[j - i] = d.get(j - i, 0.0) + p * q
    return d

def aire(dd, h, dec):
    # P(X + dec > Y) + 0,5 P(X + dec = Y) = P(D < dec) + 0,5 P(D = dec)
    a = 0.0
    for k, p in dd.items():
        v = k * h
        if v < dec - 1e-12: a += p
        elif abs(v - dec) <= 1e-12: a += 0.5 * p
    return a

def atteignables(dd, h):
    ks = sorted(dd)
    cum, out = 0.0, []
    for k in ks:
        avant = cum; cum += dd[k]
        out.append(((avant + cum) / 2, "saut", k * h))        # décalage = k h exactement
        out.append((cum, "palier", (k + 0.5) * h))            # décalage dans ]k h, (k+1) h[
    return out

def ecart_type(m, h):
    mu = sum(i * h * p for i, p in m.items())
    return math.sqrt(sum((i * h - mu) ** 2 * p for i, p in m.items()))

CIBLES = (0.69, 0.80, 0.95)
PLAFOND = 0.02
for sigma, h in ((1, 0.001), (1, 0.1), (1, 0.25), (1, 0.5), (1, 1.0), (1, 2.0), (2, 1.0), (2, 0.5)):
    m = reseau(0, sigma, h, 10); dd = loi_diff(m); s = ecart_type(m, h); S = atteignables(dd, h)
    print(f"\nnormale(0,{sigma}) arrondie au pas {h} ; écart type {s:.4f}")
    for a in CIBLES:
        bas = max((v for v in S if v[0] <= a), key=lambda v: v[0]); haut = min((v for v in S if v[0] >= a), key=lambda v: v[0])
        proche = min((bas, haut), key=lambda v: abs(v[0] - a))
        # conduite iii : décalage de la loi continue, en écarts types de la loi continue, lu en écarts types de la loi arrondie
        d_cont = NormalDist().inv_cdf(a) * math.sqrt(2)  # en écarts types (sigma continu)
        a_iii = aire(dd, h, d_cont * s)
        # artefact : le même nombre écrit en unité brute par un auteur (d_cont * sigma), lu en écarts types
        a_brut = aire(dd, h, d_cont * sigma * s)
        def issue(x):
            dans = any(abs(x - v[0]) < 1e-9 for v in (bas, haut))
            if abs(x - a) <= 0.005: return "a"
            return "a-réseau" if dans and abs(x - a) <= PLAFOND else "hors"
        print(f"  aire dite {a:.2f} : sous {bas[0]:.4f} ({bas[1]}), sur {haut[0]:.4f} ({haut[1]}), saut d'un palier à l'autre "
              f"{2*(haut[0]-bas[0]):.4f} ; plus proche {proche[0]:.4f} -> {issue(proche[0])} ; sur -> {issue(haut[0])} ; "
              f"loi continue {a_iii:.4f} -> {issue(a_iii)} ; nombre brut lu en écarts types {a_brut:.4f} -> {issue(a_brut)}")
