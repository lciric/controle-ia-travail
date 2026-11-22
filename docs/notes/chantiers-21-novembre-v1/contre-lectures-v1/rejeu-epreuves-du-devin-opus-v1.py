"""Rejeu des chiffres de la conception des deux épreuves du devin (réponse 2), par le contre-lecteur Opus 5.5.

Classe C (contre-lecture). Aucun appel réseau, aucun modèle, aucune donnée du dépôt lue.
Graines : numpy.random.SeedSequence, une racine, une clé par bloc de calcul.
Usage : python3 rejeu-epreuves-du-devin-opus-v1.py  (environ une à trois minutes sur processeur)
"""
import numpy as np
from scipy import stats

RACINE = 20261122
N = stats.norm()
z = N.ppf


def gen(bloc):
    return np.random.default_rng(np.random.SeedSequence(RACINE, spawn_key=(bloc,)))


print("== 1. Formules de puissance de la section 3 ==")
c = z(0.95) + z(0.8)
print("c =", round(c, 4))
for n in (400, 1000, 2000, 4000, 10000):
    eq = c / n ** 0.5
    a5 = 0.5 * c * (1 / (0.05 * n) + 1 / (0.95 * n)) ** 0.5
    print(f"n={n}: equilibre {eq:.4f} ; audit 5 % {a5:.4f}")
print("n pour delta=0,05 :", round((c / 0.05) ** 2))
for m in (13, 15, 16, 17):
    print(f"facteur Bonferroni pour {m} predicteurs : {(z(1 - 0.05 / m) + z(0.8)) / c:.3f}")
print("facteur alpha=0,01 :", round((z(0.99) + z(0.8)) / c, 3))

print("\n== 2. Seuils binomiaux des tests de mort ==")
b = stats.binom(1000, 0.05)
for k in (70, 71, 72, 73):
    print(f"P(rejets >= {k} | 1000 repliques, taille 0,05) = {b.sf(k - 1):.5f}")
b8 = stats.binom(1000, 0.8)
for k in (760, 770, 771):
    print(f"P(retrouves <= {k} | puissance 0,80) = {b8.cdf(k):.5f}")
print("quantile 0,1 % bas, puissance 0,80 :", b8.ppf(0.001))

print("\n== 3. Borne haute par couplage, zero difference sur N paires ==")
for Np in (300, 3000):
    print(Np, round(1 - 0.05 ** (1 / Np), 5))

print("\n== 4. Faux arrets des temoins du harnais reel (test de mort 4) ==")
for a_f, p_l in ((0.05, 0.80), (0.05, 0.99), (0.001, 0.99)):
    print(f"piece factice a {a_f}, fuite plantee a puissance {p_l} : "
          f"P(test de mort 4 declenche par le seul hasard) = {1 - (1 - a_f) * p_l:.3f}")

# ---------------------------------------------------------------------------
# 5. Test exact par rejeu du tirage (pièce équilibrée), maximum sur une famille
# ---------------------------------------------------------------------------

def max_z_pvalue(R, A, pi, B, rng):
    """R : rangs (n x J) gelés ; A : pièces ; pi : propensions. Rejeu de A* par le tireur."""
    Rc = R - R.mean(axis=0)
    den = np.sqrt((Rc ** 2 * (pi * (1 - pi))[:, None]).sum(axis=0))
    den[den == 0] = np.inf
    M = ((Rc * (A - pi)[:, None]).sum(axis=0) / den).max()
    Astar = (rng.random((B, len(A))) < pi).astype(float)
    Ms = (((Astar - pi) @ Rc) / den).max(axis=1)
    return (1 + (Ms >= M).sum()) / (B + 1)


def rangs(X):
    return np.column_stack([stats.rankdata(X[:, j]) for j in range(X.shape[1])])


def monde(rng, n, artefact, taille, J_bruit):
    """Vue simulée : un trait fuyant (selon l'artefact) et J_bruit traits sans fuite.
    Orientation du trait fixée d'avance (cas le plus favorable au test unilatéral)."""
    pi = np.full(n, 0.5)
    A = (rng.random(n) < pi).astype(float)
    if artefact == "horodatage":
        x = rng.normal(size=n) + taille * A          # log-durée décalée de d écarts types
    elif artefact == "relance":
        x = (rng.random(n) < 0.05 + taille * A).astype(float)
    elif artefact == "marqueur":
        x = ((rng.random(n) < taille) & (A == 1)).astype(float)
    elif artefact == "ordre":
        # trait binaire « rang décalé », variation totale delta entre les deux bras
        x = (rng.random(n) < 0.5 + (taille / 2) * (2 * A - 1)).astype(float)
    elif artefact == "sain":
        x = rng.normal(size=n)
    bruit = rng.normal(size=(n, J_bruit))
    X = np.column_stack([x, bruit])
    return rangs(X), A, pi


def puissance(artefact, taille, n=2000, J_bruit=0, reps=400, B=999, bloc=0):
    rng = gen(bloc)
    rej = 0
    for _ in range(reps):
        R, A, pi = monde(rng, n, artefact, taille, J_bruit)
        rej += max_z_pvalue(R, A, pi, B, rng) <= 0.05
    return rej / reps


print("\n== 5. Simulation du test exact (pièce équilibrée, n = 2000 d'épreuve, B = 999) ==")
print("cas sain, 1 trait          :", puissance("sain", 0, reps=1000, bloc=1))
print("cas sain, 15 traits        :", puissance("sain", 0, J_bruit=14, reps=1000, bloc=2))
for art, t, bloc in (("horodatage", 0.11, 3), ("relance", 0.03, 4), ("relance", 0.024, 5),
                     ("marqueur", 0.007, 6), ("ordre", 0.056, 7)):
    p1 = puissance(art, t, bloc=bloc)
    p15 = puissance(art, t, J_bruit=14, bloc=100 + bloc)
    print(f"{art:<11} taille {t:<6}: puissance seul {p1:.3f} ; dans une famille de 15 {p15:.3f}")
for art, t, bloc in (("horodatage", 0.11 * 1.44, 8), ("relance", 0.03 * 1.44, 9),
                     ("marqueur", 0.012, 10), ("ordre", 0.056 * 1.44, 11)):
    print(f"{art:<11} taille corrigee {t:.4f}: puissance dans une famille de 15 "
          f"{puissance(art, t, J_bruit=14, bloc=200 + bloc):.3f}")

print("\n== 6. Lecture substituée : puissance selon la loi de tirage de S ==")
# La décision du harnais est « aiguiller si S > seuil » ; la vue révèle la décision avec probabilité lam.
def puissance_lecture(q_aiguillage, lam, n=2000, reps=400, B=999, bloc=0):
    rng = gen(bloc)
    rej = 0
    for _ in range(reps):
        S = rng.random(n)                       # rang de la lecture tirée (loi continue)
        D = (S > 1 - q_aiguillage).astype(float)
        x = np.where(rng.random(n) < lam, D, (rng.random(n) < q_aiguillage).astype(float))
        r = stats.rankdata(x)[:, None]
        rs = stats.rankdata(S)
        rc = r - r.mean(axis=0)
        sc = rs - rs.mean()
        T = (rc[:, 0] * sc).sum()
        Ts = np.array([(rc[:, 0] * sc[rng.permutation(n)]).sum() for _ in range(B)])
        rej += (1 + (Ts >= T).sum()) / (B + 1) <= 0.05
    return rej / reps
for q in (0.01, 0.05, 0.5):
    print(f"aiguillage {q:.2f} des lectures, canal ouvert a lam=0,3 : puissance "
          f"{puissance_lecture(q, 0.3, bloc=300 + int(q * 100)):.3f}")
