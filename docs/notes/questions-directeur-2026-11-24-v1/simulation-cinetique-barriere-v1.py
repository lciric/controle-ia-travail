"""Simulation sur processeur pour la réponse à la question 3 (cinétique des collisions d'idées), v1.

Pièce de travail (classe C). Aucune dépense, aucun appel à un modèle. Deux calculs :

A. Course de dose-réponse décrite pour l'organisme d'idéation : avec quelle précision
   retrouve-t-on une barrière plantée E (en nats) en faisant varier la température
   d'échantillonnage T, à budget de collisions donné ? Et distingue-t-on un catalyseur
   (qui abaisse E, donc gain qui décroît quand T monte) d'un simple facteur de fréquence
   (qui multiplie le préfacteur, donc gain constant en T) ?
B. Corpus : si le taux suit la forme en série rencontre-barrière
   lambda = kD*kr/(kD+kr), une régression de Poisson log-linéaire (forme du taux fusionné)
   quel signe donne-t-elle à l'interaction entre contact et structure ?
   (Calcul : la dérivée croisée de log lambda en log kD et log kr vaut kD*kr/(kD+kr)^2 > 0.)

Graines par numpy.random.SeedSequence (règle R9), une graine fille par tâche.
Usage : python simulation-cinetique-barriere-v1.py  (numpy >= 1.25)
"""
import numpy as np

GRAINE_RACINE = 20261124  # graine du calcul, consignée ici
ss = np.random.SeedSequence(GRAINE_RACINE)
ss_a, ss_b, ss_c = ss.spawn(3)


def poisson_glm(X, y, offset=None, iters=50):
    """Régression de Poisson à lien logarithmique par moindres carrés repondérés."""
    n, p = X.shape
    off = np.zeros(n) if offset is None else offset
    beta = np.zeros(p)
    beta[0] = np.log(max(y.mean(), 1e-9)) - off.mean()
    for _ in range(iters):
        eta = X @ beta + off
        mu = np.exp(eta)
        W = mu
        z = eta - off + (y - mu) / np.maximum(mu, 1e-12)
        XtW = X.T * W
        H = XtW @ X + 1e-10 * np.eye(p)
        new = np.linalg.solve(H, XtW @ z)
        if np.max(np.abs(new - beta)) < 1e-10:
            beta = new
            break
        beta = new
    mu = np.exp(X @ beta + off)
    cov = np.linalg.inv((X.T * mu) @ X + 1e-10 * np.eye(p))
    return beta, np.sqrt(np.diag(cov))


# ---------- A. Barrière plantée et catalyseur dans l'organisme ----------
TEMPERATURES = np.array([0.4, 0.7, 1.0, 1.3])
A_PREF = 0.5  # probabilité de prise par collision à température infinie (vérité plantée)


def taux(E, T, A=A_PREF):
    return np.minimum(1.0, A * np.exp(-E / T))


def estime_barriere(E, budget, rng):
    n = np.full(len(TEMPERATURES), budget // len(TEMPERATURES))
    y = rng.binomial(n, taux(E, TEMPERATURES))
    X = np.column_stack([np.ones(len(TEMPERATURES)), -1.0 / TEMPERATURES])
    if y.sum() == 0:
        return np.nan
    b, _ = poisson_glm(X, y.astype(float), offset=np.log(n))
    return b[1]


rng_a = np.random.default_rng(ss_a)
print("A1. Barrière plantée E (nats) retrouvée par la pente du tracé d'Arrhenius")
print("    températures", TEMPERATURES.tolist(), "; 500 répétitions par case")
for E in (0.5, 1.5, 2.5, 3.5):
    for budget in (400, 1600, 6400):
        est = np.array([estime_barriere(E, budget, rng_a) for _ in range(500)])
        est = est[np.isfinite(est)]
        print(f"    E={E:3.1f}  budget={budget:5d} collisions : moyenne {est.mean():5.2f}, "
              f"écart type {est.std():4.2f}, rendements nuls exclus {500-len(est)}")

rng_c = np.random.default_rng(ss_c)
print("\nA2. Catalyseur (E abaissée de 1 nat) contre préfacteur (A multiplié par e) ;")
print("    même gain à T=1. Coefficient d'interaction (présence x 1/T) : vrai = -1 (catalyseur), 0 (préfacteur)")
E0 = 2.5
for budget in (800, 3200, 12800):
    res = {"catalyseur": [], "prefacteur": []}
    for _ in range(400):
        for nom in res:
            if nom == "catalyseur":
                p1 = taux(E0 - 1.0, TEMPERATURES)
            else:
                p1 = taux(E0, TEMPERATURES, A=A_PREF * np.e)
            p0 = taux(E0, TEMPERATURES)
            n = budget // (2 * len(TEMPERATURES))
            y0 = rng_c.binomial(n, p0)
            y1 = rng_c.binomial(n, p1)
            y = np.concatenate([y0, y1]).astype(float)
            invT = np.concatenate([1 / TEMPERATURES, 1 / TEMPERATURES])
            c = np.concatenate([np.zeros(4), np.ones(4)])
            X = np.column_stack([np.ones(8), -invT, c, -c * invT])
            b, se = poisson_glm(X, y, offset=np.full(8, np.log(n)))
            # dans ce paramétrage, le coefficient de -c/T vaut -1 pour un abaissement de 1 nat
            res[nom].append((b[3], b[3] / se[3]))
    for nom, v in res.items():
        v = np.array(v)
        print(f"    budget={budget:5d}  {nom:10s} : coefficient moyen {v[:,0].mean():5.2f}, "
              f"part |z|>1,96 : {np.mean(np.abs(v[:,1])>1.96):.2f}")

# ---------- B. Forme en série dans le corpus ----------
rng_b = np.random.default_rng(ss_b)
N = 20000
c = rng_b.normal(size=N)          # logarithme du contact (rencontres), centré réduit
Z = rng_b.normal(size=N)          # compatibilité de structure, centrée réduite
kD = np.exp(c - 3.0)
kr = np.exp(0.8 * Z - 3.0)
lam = kD * kr / (kD + kr)
dur = 50.0                        # durée d'exposition (unités arbitraires)
y = rng_b.poisson(lam * dur).astype(float)
X_add = np.column_stack([np.ones(N), c, Z])
X_int = np.column_stack([np.ones(N), c, Z, c * Z])
b_add, se_add = poisson_glm(X_add, y, offset=np.full(N, np.log(dur)))
b_int, se_int = poisson_glm(X_int, y, offset=np.full(N, np.log(dur)))
print("\nB. Forme en série rencontre-barrière, régression log-linéaire du taux")
print(f"    sans interaction : contact {b_add[1]:.2f}, structure {b_add[2]:.2f}")
print(f"    avec interaction : contact {b_int[1]:.2f}, structure {b_int[2]:.2f}, "
      f"interaction {b_int[3]:.3f} (écart type {se_int[3]:.3f})")
for lo, hi, nom in ((-9, -0.43, "tiers bas de Z"), (-0.43, 0.43, "tiers moyen"), (0.43, 9, "tiers haut")):
    m = (Z > lo) & (Z <= hi)
    bb, _ = poisson_glm(np.column_stack([np.ones(m.sum()), c[m]]), y[m], offset=np.full(m.sum(), np.log(dur)))
    print(f"    élasticité au contact, {nom:14s} : {bb[1]:.2f}")
print(f"    naissances simulées : {int(y.sum())} sur {N} paires")
