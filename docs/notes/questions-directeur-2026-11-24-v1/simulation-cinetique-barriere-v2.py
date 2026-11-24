"""Simulation sur processeur pour l'erratum 1 de la réponse à la question 3 (cinétique des
collisions d'idées), v2. Remplace la partie A de la v1, qui reste archivée sans modification.

Pièce de travail (classe C). Aucune dépense, aucun appel à un modèle.

Correction visée (contre-lecture du 24 novembre, majeur de la question 3) : la section 3 de la
réponse pose pour l'organisme un préfacteur qui dépend de la température,
    ln k = ln A + m ln T - E/T,
mais la partie A de la v1 ajustait ln A - E/T sans le terme m ln T. On refait :

A0. Colinéarité de ln T et de 1/T dans chaque plan de températures.
A1. Barrière plantée E retrouvée par la pente, quatre ajustements croisés :
    vérité m = 0 ou m = 1 ; ajustement sans ou avec le terme m ln T ;
    deux plans : l'ancien (0,4 à 1,3, quatre températures) et un plan plus large (0,25 à 2,0,
    six températures, posé ; la borne haute est limitée par la réaction parasite, réponse,
    section 4). Écart type de Monte-Carlo, écart type robuste (écart interquartile / 1,349),
    biais, et écart type asymptotique tiré de l'information de Fisher du modèle de Poisson
    évaluée à la vérité.
A2. Test du catalyseur (E abaissée de 1 nat) contre un préfacteur de même gain à T = 1
    (A multiplié par e), avec le terme m ln T commun aux deux bras dans l'ajustement.

Graines par numpy.random.SeedSequence (règle R9) : une graine fille par cellule.
Usage : python simulation-cinetique-barriere-v2.py  (numpy >= 1.25)
"""
import numpy as np

GRAINE_RACINE = 20261124  # même racine que la v1 ; arbre de graines distinct (spawn_key 2)
ss = np.random.SeedSequence(GRAINE_RACINE, spawn_key=(2,))

PLANS = {
    "ancien 0,4-1,3 (4 T)": np.array([0.4, 0.7, 1.0, 1.3]),
    "large 0,25-2,0 (6 T)": np.array([0.25, 0.4, 0.7, 1.0, 1.4, 2.0]),
}
A_PREF = 0.5
REPET = 500


def poisson_glm(X, y, offset, iters=100):
    n, p = X.shape
    beta = np.zeros(p)
    beta[0] = np.log(max(y.sum() / np.exp(offset).sum(), 1e-9))
    for _ in range(iters):
        eta = X @ beta + offset
        mu = np.exp(np.clip(eta, -50, 50))
        z = eta - offset + (y - mu) / np.maximum(mu, 1e-12)
        XtW = X.T * mu
        new = np.linalg.solve(XtW @ X + 1e-10 * np.eye(p), XtW @ z)
        if not np.all(np.isfinite(new)):
            return None, None
        if np.max(np.abs(new - beta)) < 1e-10:
            beta = new
            break
        beta = new
    mu = np.exp(np.clip(X @ beta + offset, -50, 50))
    cov = np.linalg.inv((X.T * mu) @ X + 1e-10 * np.eye(p))
    return beta, np.sqrt(np.diag(cov))


def taux(E, T, m, A=A_PREF):
    return np.minimum(1.0, A * T**m * np.exp(-E / T))


def plan_X(T, avec_lnT):
    cols = [np.ones(len(T))]
    if avec_lnT:
        cols.append(np.log(T))
    cols.append(-1.0 / T)
    return np.column_stack(cols)


def sd_asymptotique(E, T, m, budget, avec_lnT):
    n = budget // len(T)
    mu = n * taux(E, T, m)
    X = plan_X(T, avec_lnT)
    cov = np.linalg.inv((X.T * mu) @ X)
    return float(np.sqrt(cov[-1, -1]))


print("A0. Corrélation de ln T et de 1/T dans chaque plan")
for nom, T in PLANS.items():
    r = np.corrcoef(np.log(T), 1.0 / T)[0, 1]
    print(f"    {nom} : températures {T.tolist()} ; corrélation(ln T, -1/T) = {-r:.3f}")

print("\nA1. Barrière plantée E (nats) retrouvée par la pente ; "
      f"{REPET} répétitions par case ; A = {A_PREF}")
print("    plan | m vrai | ajustement | E | budget | moyenne | écart type MC | écart type robuste | "
      "écart type asymptotique | échecs")
cellules = iter(ss.spawn(2 * 2 * 2 * 3 * 3))
for nom, T in PLANS.items():
    for m_vrai in (0, 1):
        for avec in (False, True):
            for E in (1.5, 2.5, 3.5):
                for budget in (1600, 6400, 25600):
                    rng = np.random.default_rng(next(cellules))
                    n = np.full(len(T), budget // len(T))
                    X = plan_X(T, avec)
                    est, echec = [], 0
                    for _ in range(REPET):
                        y = rng.binomial(n, taux(E, T, m_vrai)).astype(float)
                        if y.sum() == 0:
                            echec += 1
                            continue
                        b, _ = poisson_glm(X, y, np.log(n))
                        if b is None:
                            echec += 1
                            continue
                        est.append(b[-1])
                    est = np.array(est)
                    q1, q3 = np.quantile(est, [0.25, 0.75])
                    sda = sd_asymptotique(E, T, m_vrai, budget, avec)
                    print(f"    {nom} | m={m_vrai} | {'avec m ln T' if avec else 'sans m ln T'} | "
                          f"E={E:3.1f} | {budget:5d} | {est.mean():6.2f} | {est.std():6.2f} | "
                          f"{(q3 - q1) / 1.349:5.2f} | {sda:5.2f} | {echec}")

print("\nA2. Catalyseur (E abaissée de 1 nat) contre préfacteur (A multiplié par e), même gain à T = 1 ;")
print("    E0 = 2,5 ; ajustement avec m ln T commun aux deux bras ; coefficient de -c/T : "
      "vrai -1 (catalyseur), 0 (préfacteur) ; 400 répétitions")
print("    plan | m vrai | budget | bras | coefficient moyen | part |z|>1,96")
E0 = 2.5
cellules2 = iter(ss.spawn(2 * 2 * 3 * 2))
for nom, T in PLANS.items():
    k = len(T)
    for m_vrai in (0, 1):
        for budget in (3200, 12800, 51200):
            for bras in ("catalyseur", "prefacteur"):
                rng = np.random.default_rng(next(cellules2))
                n = budget // (2 * k)
                coefs, sig = [], []
                for _ in range(400):
                    p0 = taux(E0, T, m_vrai)
                    p1 = taux(E0 - 1.0, T, m_vrai) if bras == "catalyseur" else \
                        taux(E0, T, m_vrai, A=A_PREF * np.e)
                    y = np.concatenate([rng.binomial(n, p0), rng.binomial(n, p1)]).astype(float)
                    TT = np.concatenate([T, T])
                    c = np.concatenate([np.zeros(k), np.ones(k)])
                    X = np.column_stack([np.ones(2 * k), np.log(TT), -1.0 / TT, c, -c / TT])
                    b, se = poisson_glm(X, y, np.full(2 * k, np.log(n)))
                    if b is None:
                        continue
                    coefs.append(b[4])
                    sig.append(abs(b[4] / se[4]) > 1.96)
                print(f"    {nom} | m={m_vrai} | {budget:5d} | {bras:10s} | {np.mean(coefs):6.2f} | "
                      f"{np.mean(sig):.2f}")
