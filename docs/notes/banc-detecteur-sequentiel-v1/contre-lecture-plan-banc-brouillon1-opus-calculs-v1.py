"""Calculs refaits par le contre-lecteur (Claude Opus 5.5) du brouillon 1 du préenregistrement
prereg/banc-detecteur-sequentiel-reference-contaminee-v1-brouillon1.md (c10e3fa8…).

Aucun tirage au hasard : formes fermées, quadratures déterministes, propagation de densité sur grille.
Aucune cellule de la grille n'est simulée. Dépendances : numpy, scipy, et le code du dépôt (PYTHONPATH=src).
Lancement : PYTHONPATH=src python contre-lecture-plan-banc-brouillon1-opus-calculs-v1.py [--sans-passage]
Partie 1 : rayons, bornes de la construction naïve à l'instant n (indépendamment de l'annexe A, par calibrage.py).
Partie 2 : Bêta(1 ; 4), sous-gaussianité de l'échelle « écart type », correction d'Edgeworth de G1, multiplicité,
           rapport G5 dans la couche « enveloppe », duel refait (population et taille finie, pente contre r et contre ε).
Partie 3 : taux de premier passage exacts (à la discrétisation près) de la construction naïve et de la construction
           bien spécifiée sur la loi normale du contrôle (A-artefact, A-sain-1, A-i2, A-i3, A-i4) ; environ 4 minutes.
"""
import sys
# ===================== Partie 1
import math
import numpy as np
from statistics import NormalDist
from scipy import stats, optimize, special
from controle_ia.simulation_t03.calibrage import rho_optimal, frontiere
from controle_ia.agregateurs.processus_e import log_e_unilateral

# 1. rayons
def r(m, e, a=0.025, unil=False):
    mh = math.floor((1-e)*m+1e-9); c = math.log((1 if unil else 2)/a)
    return e + math.sqrt(c/(2*mh))
for m in (100,400,1600):
    print(m, [round(r(m,e),4) for e in (0,0.02,0.10)], "unilat", [round(r(m,e,unil=True),4) for e in (0,.02,.1)])
print("reduction unilaterale du rayon d'echantillonnage", 1-math.sqrt(math.log(40)/math.log(80)))
print("condition Massart unilaterale exp(-2 m g^2)<=1/2 :", 0.025<=0.5)
# 2. bornes naive instant n (independant, scipy)
for m in (100,400):
    rho,_ = rho_optimal(m,0.05,"unilateral")
    for k in (0.25,1,4,16,64):
        n=int(k*m); s=frontiere(n,rho,0.05,"unilateral")
        print(m,k, round(rho,5), round(s,2), round(stats.norm.sf(s/math.sqrt(n*(1+n/m))),4))
# ===================== Partie 2
from scipy import stats, integrate, optimize
from controle_ia.simulation_t03.calibrage import rho_optimal, frontiere  # noqa

# ---------- Bêta(1;4) : nœuds, moments du gain, sous-gaussianité
Fb = lambda x: 1 - (1 - x) ** 4
Qb = lambda u: 1 - (1 - u) ** 0.25
a, c = Qb(0.5), Qb(0.9)
u = (np.arange(4_000_000) + 0.5) / 4_000_000
g = np.clip((Qb(u) - a) / (c - a), 0, 1)
mu, sd = g.mean(), g.std()
sk = ((g - mu) ** 3).mean() / sd ** 3
print(f"Bêta(1;4) : a = {a:.4f} c = {c:.4f} moyenne du gain {mu:.4f} écart type {sd:.4f} asymétrie {sk:.3f}")
lam = np.linspace(0.02, 3, 150)
z = (g - mu) / sd
psi = np.array([math.log(np.mean(np.exp(l * z))) - l * l / 2 for l in lam])
print(f"  z = (g − μ)/écart type exact : max_λ∈]0,3] [log E e^(λz) − λ²/2] = {psi.max():.4f} à λ = {lam[psi.argmax()]:.2f} (positif = pas 1-sous-gaussien)")
psih = np.array([math.log(np.mean(np.exp(l * (g - mu)))) - l * l / 8 for l in lam * 2])
print(f"  Hoeffding : max [log E e^(λ(g−μ)) − λ²/8] = {psih.max():.2e} (doit être ≤ 0)")
rho400, _ = rho_optimal(400, 0.05, "unilateral")
print(f"  ρ*(400 ; 0,05) = {rho400:.4f} : λ effectifs du mélange de l'ordre de ρ à quelques ρ")
# Edgeworth pour G1 : P(S_400/√400 ≥ 1,959964) pour le gain standardisé
zq = 1.959964; n = 400
edg = stats.norm.sf(zq) + sk / (6 * math.sqrt(n)) * (zq ** 2 - 1) * stats.norm.pdf(zq)
print(f"  G1 : taux de la somme à horizon fixe, correction d'Edgeworth : {edg:.4f} (contre 0,025)")

# ---------- multiplicité
print(f"150 comparaisons, Z = 4 unilatéral : {1 - (1 - stats.norm.sf(4)) ** 150:.4f}")

# ---------- G5 dans la couche « enveloppe » (population, sans bruit de référence)
from statistics import NormalDist
N01 = NormalDist()
ZG = stats.norm.ppf((np.arange(200_000) + 0.5) / 200_000)
def hausse(d):
    xs = Qb(stats.norm.cdf(ZG + d)); return np.clip((xs - a) / (c - a), 0, 1).mean() - mu
rho_e, s_e = rho_optimal(400, 0.025, "unilateral")
s400 = frontiere(400, rho_e, 0.025, "unilateral")
for r in (0.0, 0.0948):
    cible_somme = r + 1.959964 * sd / 20
    cible_e = r + 0.5 * s400 / 400
    d1 = optimize.brentq(lambda d: hausse(d) - cible_somme, 0, 3)
    d2 = optimize.brentq(lambda d: hausse(d) - cible_e, 0, 3)
    print(f"G5, marge {r} : décalage latent détectable somme {d1:.3f}, processus-e (instant n) {d2:.3f}, rapport {d2/d1:.2f}")

# ---------- duel, mise en œuvre indépendante (lois uniformes, formes fermées en s)
def rayon(m, e, a_=0.025):
    return e + math.sqrt(math.log(2 / a_) / (2 * math.floor((1 - e) * m + 1e-9)))
def duel(lo, hi, eps, regle, n_seq=None, m=1_000_000):
    r = rayon(m, eps)
    w = hi - lo
    q = lambda p: lo + w * p / (1 - eps) if p <= 1 - eps else 1.0   # quantile du mélange
    med = q(0.5)
    if regle == "support":
        A, C = 0.0, 1.0
    elif regle == "quantiles":
        A, C = q(0.5), q(0.9)
    else:
        st = (q(0.75) - q(0.25)) / 1.349
        A, C = max(0.0, med - st / math.sqrt(r)), min(1.0, med + st / math.sqrt(r))
    gfun = lambda x: np.clip((x - A) / (C - A), 0, 1)
    # survie du gain sous la référence : P(g > s) = (1−ε) P_U(X > A + s(C−A)) + ε·1[g(1) > s]
    def surv(s):
        t = A + s * (C - A)
        pu = np.clip((hi - t) / w, 0, 1)
        return (1 - eps) * pu + eps * (gfun(1.0) > s)
    S = (np.arange(400_000) + 0.5) / 400_000
    borne = float(np.mean(np.minimum(1.0, surv(S) + r)))
    if n_seq:
        rho_d, _ = rho_optimal(n_seq, 0.025, "unilateral")
        borne += 0.5 * frontiere(n_seq, rho_d, 0.025, "unilateral") / n_seq
    X = lo + w * (np.arange(200_000) + 0.5) / 200_000
    f = lambda D: float(gfun(np.minimum(X + D, 1.0)).mean()) - borne
    return optimize.brentq(f, 0, 1, xtol=1e-12) if f(1) > 0 else float("nan"), r
EPS = (0.01, 0.02, 0.04, 0.08)
for nom, lo, hi in (("étalé", 0.0, 1.0), ("concentré", 0.2 - 0.02 * math.sqrt(3), 0.2 + 0.02 * math.sqrt(3))):
    for regle in ("variance", "support", "quantiles"):
        for nseq in (None, 1_000_000):
            res = [duel(lo, hi, e, regle, nseq) for e in EPS]
            pl = np.array([p for p, _ in res]); rs = np.array([r for _, r in res])
            pr = np.polyfit(np.log(rs), np.log(pl), 1)[0]; pe = np.polyfit(np.log(EPS), np.log(pl), 1)[0]
            print(f"duel {nom:9} {regle:9} {'fini n=10^6' if nseq else 'population '} : planchers {np.round(pl,5)} ; pente contre r {pr:.3f} ; contre ε {pe:.3f}")
# ===================== Partie 3
if "--sans-passage" in sys.argv:
    sys.exit(0)
H = 0.25
XMAX = 640.0
GRID = np.arange(-XMAX, XMAX + H / 2, H)
KX = np.arange(-7.0, 7.0 + H / 2, H)
KER = stats.norm.pdf(KX) * H
KER /= KER.sum()

def frontiere_vec(nmax, rho, alpha):
    t = np.arange(1, nmax + 1, dtype=float)
    lo, hi = np.zeros_like(t), 60 * np.sqrt(t) + 60
    h = math.log(1 / alpha)
    for _ in range(80):
        mi = 0.5 * (lo + hi)
        f = log_e_unilateral(mi, t, 1.0, rho) < h
        lo = np.where(f, mi, lo); hi = np.where(f, hi, mi)
    return 0.5 * (lo + hi)

def passage(c, horizons):
    """Probabilité cumulée d'avoir W_t >= c_t pour un t <= horizon, aux horizons demandés."""
    nmax = len(c)
    dens = stats.norm.pdf(GRID) * H
    out, cum = {}, 0.0
    hs = set(horizons)
    for t in range(1, nmax + 1):
        if t > 1:
            dens = np.convolve(dens, KER, mode="same")
        ct = c[t - 1]
        # masse au-dessus de c_t (cellule de largeur H centrée sur chaque point)
        haut = GRID + H / 2
        frac = np.clip((haut - ct) / H, 0.0, 1.0)
        absorb = float((dens * frac).sum())
        cum += absorb
        dens = dens * (1 - frac)
        if t in hs:
            out[t] = cum
    return out

def controle_propagateur():
    # frontière constante b : P(max W_t >= b, t<=n) ~ 2 Φ̄((b + 0.5826)/√n) (correction de Siegmund)
    n, b = 400, 40.0
    p = passage(np.full(n, b), [n])[n]
    print(f"contrôle du propagateur : frontière constante {b}, n = {n} : {p:.5f} ; Siegmund {2*stats.norm.sf((b+0.5826)/math.sqrt(n)):.5f}")

if True:
    controle_propagateur()
    alpha = 0.05
    for m, mult in ((400, (0.25, 1, 4, 16)), (100, (0.25, 1, 4, 16, 64))):
        rho, _ = rho_optimal(m, alpha, "unilateral")
        hz = [int(k * m) for k in mult]
        nmax = max(hz)
        b = frontiere_vec(nmax, rho, alpha)
        t = np.arange(1, nmax + 1, dtype=float)
        # bien spécifiée
        pc = passage(b, hz)
        print(f"m = {m} bien spécifiée (connue_normale) : " + " ; ".join(f"n = {h} : {pc[h]:.5f}" for h in hz))
        # naïve : quadrature de Gauss-Hermite sur δ, et sur u (7 nœuds, approximation normale de σ̂/σ)
        xd, wd = np.polynomial.hermite_e.hermegauss(48); wd = wd / wd.sum()
        xu, wu = np.polynomial.hermite_e.hermegauss(3); wu = wu / wu.sum()
        su = math.sqrt(1 / (2 * (m - 1)))
        mu_u = math.exp(special_lgamma := 0) if False else math.sqrt(2/(m-1)) * math.exp(math.lgamma(m/2) - math.lgamma((m-1)/2))
        for avec_sigma in (False, True):
            res = {h: [] for h in hz}
            poids = []
            for xi, wi in zip(xd, wd):
                d = xi / math.sqrt(m)
                for uj, wj in (zip(xu, wu) if avec_sigma else [(0.0, 1.0)]):
                    u = (mu_u + su * uj) if avec_sigma else 1.0
                    p = passage(u * b + d * t, hz)
                    for h in hz:
                        res[h].append(p[h])
                    poids.append(wi * wj)
            poids = np.array(poids)
            lib = "centre et échelle estimés" if avec_sigma else "centre seul estimé"
            ligne = []
            for h in hz:
                pj = np.array(res[h]); moy = float((poids * pj).sum()); sd = math.sqrt(float((poids * (pj - moy) ** 2).sum()))
                part10 = float(poids[pj > 0.10].sum()); part128 = float(poids[pj > 0.10 + 3*math.sqrt(0.09/1000)].sum())
                ligne.append(f"n = {h} : taux {moy:.4f} (é.t. des taux conditionnels {sd:.3f} ; part > 2α {part10:.3f}, part nette > 0,1285 {part128:.3f})")
            print(f"m = {m} naïve ({lib}) : " + " ; ".join(ligne))
            sys.stdout.flush()
