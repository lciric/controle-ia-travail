"""Vérifications par énumération exacte des suites d'issues, pour la preuve, version 2, de l'idée 1.1 (poids du nul).
Processeur seul ; numpy et scipy ; aucun code du juge n'est importé ni exécuté (la logique des deux lois de la grammaire
qui lisent l'historique, « sans_remise » et « moyenne_glissante », est recopiée de selection_pari.proba, copie 94bfd92).

Parties :
 A. lemme 1 (projection par blocs, certificat exact) : sup sur θ de E_θ[e_B] ≤ 1, par énumération des K^b suites ;
    nécessité de la division par le certificat.
 B. théorème 4 (minimum de processus par blocs, Ville aux fins de bloc) : P(promotion) exacte ≤ α.
 C. contre-exemple sans P4 : cartes de la grammaire qui lisent l'historique du bloc ; forme « gel » ; maximum certifié.
 D. théorème 1 (nul limité, maximum certifié sur les tirages mêmes), lecture à tous les instants, rejet par famille,
    réunion J9 ∪ J9-D40 ∪ (par membre) ; statistique min_m max_t (pas une valeur e) ; forme arrêtée membre par membre.
 E. lois connues seulement par tirages : certificat « comme si exact » non valide (probabilité exacte).
Graines : numpy.random.SeedSequence(20261115_2), dérivées par partie (spawn_key).
"""
import itertools
import math
import sys

import numpy as np
from scipy.optimize import minimize

PLANCHER = 1e-12
RACINE = 202611152


def rng_de(cle):
    return np.random.default_rng(np.random.SeedSequence(entropy=RACINE, spawn_key=(cle,)))


def normaliser(p):
    p = np.maximum(PLANCHER, np.asarray(p, dtype=float))
    return p / p.sum()


# ---------------------------------------------------------------------------------------------------------------------
# Famille « poids des lois connues propres à la cellule, bruit aveugle commun » (forme du v9 et du membre linéaire du v8).
# Paramètre linéaire x = (μ_{c,j} pour c < C, j < J ; ρ_k pour k < K), Σ_j μ_{c,j} + Σ_k ρ_k = 1 pour chaque c.
# L : (n, J, K) lois connues aux instances ; cel : (n,) cellule de chaque instance.
# ---------------------------------------------------------------------------------------------------------------------
def probas_famille(x, L, cel, C):
    n, J, K = L.shape
    mu = x[:C * J].reshape(C, J)
    rho = x[C * J:]
    return np.einsum("nj,njk->nk", mu[cel], L) + rho[None, :]


def em_famille(Y, L, cel, C, iterations=2000):
    """EM sur la forme « mélange à deux niveaux » (bruit avec probabilité r, sinon loi j de la cellule) ; Y (n, K) poids
    des issues : une indicatrice (maximum de vraisemblance) ou q_s (projection d'information inverse). Rend x."""
    n, J, K = L.shape
    r, rt, w = 0.5, np.full(K, 1.0 / K), np.full((C, J), 1.0 / J)
    tot = Y.sum()
    for _ in range(iterations):
        bruit = r * rt[None, :]                                          # (n, K)
        lois = (1 - r) * w[cel][:, :, None] * L                          # (n, J, K)
        p = np.maximum(bruit + lois.sum(1), 1e-300)
        rb = (Y * bruit / p)                                             # (n, K)
        rl = (Y[:, None, :] * lois / p[:, None, :]).sum(2)               # (n, J)
        nb = rb.sum()
        r = nb / tot
        rt = rb.sum(0) / max(nb, 1e-300)
        for c in range(C):
            s = rl[cel == c].sum(0)
            if s.sum() > 0:
                w[c] = s / s.sum()
    return np.concatenate([((1 - r) * w).ravel(), r * rt])


def gradient_sommets(Y, L, cel, C, x):
    """Plus grande valeur, sur les sommets du polytope, de la forme linéaire ∇f(x) où f(x) = Σ_s Σ_y Y_sy log p_x(y|x_s)."""
    n, J, K = L.shape
    p = np.maximum(probas_famille(x, L, cel, C), 1e-300)
    R = Y / p                                                            # (n, K)
    g_rho = R.sum(0)                                                     # sommet ρ = e_k
    g_mu = np.einsum("nk,njk->nj", R, L)                                 # (n, J)
    tot_mu = sum(g_mu[cel == c].sum(0).max() for c in range(C) if (cel == c).any())
    return max(g_rho.max(), tot_mu)


def max_certifie(y, L, cel, C, iterations=2000):
    """Borne haute certifiée (valeur atteinte + écart de Frank-Wolfe, bornée par 0) du maximum de vraisemblance de la
    famille sur les issues y (n,)."""
    n, J, K = L.shape
    Y = np.eye(K)[y]
    x = em_famille(Y, L, cel, C, iterations)
    f = float(np.log(np.maximum(probas_famille(x, L, cel, C)[np.arange(n), y], 1e-300)).sum())
    ecart = max(0.0, gradient_sommets(Y, L, cel, C, x) - n)
    return min(0.0, f + ecart)


def em_lot(Y, L, cel, C, iterations=400):
    """EM par lots : Y (S, n, K) poids des issues (indicatrices, comptes ou q_s) ; L (S ou 1, n, J, K) ; cel (n,)."""
    S, n, K = Y.shape
    J = L.shape[2]
    r = np.full(S, 0.5); rt = np.full((S, K), 1.0 / K); w = np.full((S, C, J), 1.0 / J)
    tot = Y.sum((1, 2))
    masques = [cel == c for c in range(C)]
    for _ in range(iterations):
        bruit = r[:, None, None] * rt[:, None, :]
        lois = (1 - r)[:, None, None, None] * w[:, cel][:, :, :, None] * L
        p = np.maximum(bruit + lois.sum(2), 1e-300)
        rb = Y * bruit / p
        rl = (Y[:, :, None, :] * lois / p[:, :, None, :]).sum(3)
        nb = rb.sum((1, 2))
        r = nb / tot
        rt = rb.sum(1) / np.maximum(nb, 1e-300)[:, None]
        for c in range(C):
            if masques[c].any():
                sc = rl[:, masques[c]].sum(1)
                w[:, c] = sc / np.maximum(sc.sum(1, keepdims=True), 1e-300)
    return r, rt, w


def max_certifie_lot(Y, L, cel, C, iterations=400):
    """Borne haute certifiée du maximum de Σ Y log p_x sur la famille, par lots (valeur atteinte + écart de Frank-Wolfe,
    bornée par 0)."""
    r, rt, w = em_lot(Y, L, cel, C, iterations)
    bruit = r[:, None, None] * rt[:, None, :]
    p = np.maximum(bruit + ((1 - r)[:, None, None, None] * w[:, cel][:, :, :, None] * L).sum(2), 1e-300)
    f = (Y * np.log(p)).sum((1, 2))
    R = Y / p
    g_rho = R.sum(1).max(1)
    g_mu = np.einsum("snk,snjk->snj", R, np.broadcast_to(L, (Y.shape[0],) + L.shape[1:]))
    tot_mu = np.zeros(Y.shape[0])
    for c in range(C):
        if (cel == c).any():
            tot_mu += g_mu[:, cel == c].sum(1).max(1)
    ecart = np.maximum(0.0, np.maximum(g_rho, tot_mu) - Y.sum((1, 2)))
    return np.minimum(0.0, f + ecart)


def certificat_bloc(q, L, cel, C, phi):
    """c_B(φ) = max_v (1/b) Σ_s Σ_y P_v(y|x_s) q_s(y) / P_φ(y|x_s) (lemme 1)."""
    return gradient_sommets(q, L, cel, C, phi) / q.shape[0]


def sommets(C, J, K):
    out = []
    for k in range(K):
        x = np.zeros(C * J + K); x[C * J + k] = 1.0; out.append(x)
    for choix in itertools.product(range(J), repeat=C):
        x = np.zeros(C * J + K)
        for c, j in enumerate(choix):
            x[c * J + j] = 1.0
        out.append(x)
    return out


def point_au_hasard(rng, C, J, K):
    r = rng.uniform()
    rho = rng.dirichlet(np.ones(K)) * r
    mu = rng.dirichlet(np.ones(J), size=C) * (1 - r)
    return np.concatenate([mu.ravel(), rho])


def point_de_parametres(z, C, J, K):
    """Paramétrage libre → point du polytope (pour la recherche du pire θ)."""
    z = np.clip(z, -30.0, 30.0)
    r = 1 / (1 + math.exp(-z[0]))
    rt = np.exp(z[1:1 + K] - z[1:1 + K].max()); rt /= rt.sum()
    zw = z[1 + K:].reshape(C, J)
    w = np.exp(zw - zw.max(1, keepdims=True)); w /= w.sum(1, keepdims=True)
    return np.concatenate([((1 - r) * w).ravel(), r * rt])


def toutes_suites(K, n):
    return np.array(list(itertools.product(range(K), repeat=n)), dtype=int)


# ---------------------------------------------------------------------------------------------------------------------
def partie_A(repetitions=200):
    """Lemme 1 : pour une carte sans mémoire et φ quelconque fixé avant le bloc, sup_θ E_θ[e_B] ≤ 1 ; espérance calculée
    par la somme sur les K^b suites (pas par la formule produit, pour éprouver le pas 1)."""
    K, J, C, b = 3, 2, 2, 3
    rng = rng_de(1)
    suites = toutes_suites(K, b)
    pire = {"projection": -np.inf, "phi au hasard": -np.inf}
    pire_sans_division = -np.inf
    cert_projection = []
    for _ in range(repetitions):
        L = rng.dirichlet(np.ones(K), size=(b, J))
        cel = np.array([0, 1, rng.integers(0, 2)])
        q = rng.dirichlet(np.ones(K) * 0.7, size=b)
        phis = {"projection": em_famille(q, L, cel, C, 3000), "phi au hasard": point_au_hasard(rng, C, J, K)}
        for nom, phi in phis.items():
            Pphi = np.maximum(probas_famille(phi, L, cel, C), 1e-300)
            r = q / Pphi                                                  # (b, K)
            c = certificat_bloc(q, L, cel, C, phi)
            if nom == "projection":
                cert_projection.append(c)
            num = np.prod(r[np.arange(b)[None, :], suites], axis=1)       # (K^b,)
            e = num / max(1.0, c) ** b

            def esperance(theta, e=e):
                Pt = probas_famille(theta, L, cel, C)
                return float((np.prod(Pt[np.arange(b)[None, :], suites], axis=1) * e).sum())

            cands = sommets(C, J, K) + [point_au_hasard(rng, C, J, K) for _ in range(100)]
            meilleur = max(esperance(t) for t in cands)
            for _ in range(3):
                z0 = rng.normal(size=1 + K + C * J)
                res = minimize(lambda z: -esperance(point_de_parametres(z, C, J, K)), z0, method="Nelder-Mead",
                               options={"maxiter": 3000, "xatol": 1e-10, "fatol": 1e-14})
                meilleur = max(meilleur, -res.fun)
            pire[nom] = max(pire[nom], math.log(meilleur))
            if nom == "phi au hasard":
                ns = max(float((np.prod(probas_famille(t, L, cel, C)[np.arange(b)[None, :], suites], axis=1) * num).sum())
                         for t in sommets(C, J, K))
                pire_sans_division = max(pire_sans_division, math.log(ns))
    cp = np.array(cert_projection)
    print(f"A. lemme 1, {repetitions} jeux (K=3, b=3, 2 cellules, 2 lois connues) : plus grand log sup_θ E_θ[e_B] "
          f"projection {pire['projection']:.3e} ; φ au hasard {pire['phi au hasard']:.3e}")
    print(f"A. sans division par le certificat (φ au hasard) : plus grand log max_sommets E_θ[Π r] {pire_sans_division:.3f}")
    print(f"A. lemme 2 : certificat de la projection (3000 pas d'EM) entre {cp.min():.6f} et {cp.max():.6f}")


# ---------------------------------------------------------------------------------------------------------------------
def processus_blocs(q, L, cel_list, C_list, b, suites):
    """log W aux fins de bloc pour chaque famille (carte sans mémoire : projections et certificats au gel) ; rend
    (S, nb_blocs) = minimum sur les familles."""
    n = q.shape[0]
    nb = n // b
    logW = None
    for cel, C in zip(cel_list, C_list):
        lw = np.zeros((len(suites), nb))
        acc = np.zeros(len(suites))
        for B in range(nb):
            idx = np.arange(B * b, (B + 1) * b)
            phi = em_famille(q[idx], L[idx], cel[idx], C, 1500)
            Pphi = np.maximum(probas_famille(phi, L[idx], cel[idx], C), 1e-300)
            r = q[idx] / Pphi
            c = certificat_bloc(q[idx], L[idx], cel[idx], C, phi)
            acc = acc + np.log(r[np.arange(b)[None, :], suites[:, idx]]).sum(1) - b * math.log(max(1.0, c))
            lw[:, B] = acc
        logW = lw if logW is None else np.minimum(logW, lw)
    return logW


def partie_B(repetitions=40):
    K, J, n, b = 2, 2, 8, 2
    rng = rng_de(2)
    suites = toutes_suites(K, n)
    alphas = (0.5, 0.25, 0.1, 0.05)
    pire_rapport = {a: 0.0 for a in alphas}
    for i in range(repetitions):
        L = rng.dirichlet(np.ones(K), size=(n, J))
        celA = rng.integers(0, 2, size=n)
        cel1 = np.zeros(n, dtype=int)
        q = rng.dirichlet(np.ones(K) * 0.6, size=n)
        logW = processus_blocs(q, L, [celA, cel1], [2, 1], b, suites)
        mondes = [em_famille(q, L, celA, 2, 3000)] + [point_au_hasard(rng, 2, J, K) for _ in range(3)] + sommets(2, J, K)
        for theta in mondes:
            P = probas_famille(theta, L, celA, 2)
            prob = np.prod(P[np.arange(n)[None, :], suites], axis=1)
            for a in alphas:
                pa = float(prob[(logW >= math.log(1 / a)).any(1)].sum())
                pire_rapport[a] = max(pire_rapport[a], pa / a)
    print(f"B. théorème 4, {repetitions} plans (K=2, n=8, blocs de 2, familles {{cellules A, linéaire}}), mondes de la "
          f"famille A (projection de la carte, 3 au hasard, 6 sommets) : plus grand P(promotion)/α "
          + " ; ".join(f"α={a} : {v:.4f}" for a, v in pire_rapport.items()))


# ---------------------------------------------------------------------------------------------------------------------
# Lois de la grammaire qui lisent l'historique (recopie de selection_pari.proba, copie 94bfd92, l. 131-134 et 156-159).
def sans_remise(composition, historique, t):
    vus = np.bincount(np.asarray(historique[:t], dtype=int), minlength=len(composition)) if t else np.zeros(len(composition))
    return normaliser([max(0, c - v) for c, v in zip(composition, vus)])


def moyenne_glissante(k, fenetre, lissage, historique, t):
    recents = list(historique[max(0, t - fenetre):t])
    compte = np.bincount(np.asarray(recents, dtype=int), minlength=k) if recents else np.zeros(k)
    return normaliser([(compte[i] + lissage) / (len(recents) + k * lissage) for i in range(k)])


def lois_realisees(carte, y, b, forme):
    """q_s pour s = 0..n−1 : « nu » = historique complet (y[:s]) ; « gel » = historique arrêté au début du bloc de s."""
    out = []
    for s in range(len(y)):
        h = y[:s] if forme == "nu" else y[:(s // b) * b]
        out.append(carte(h, s))
    return np.array(out)


def partie_C():
    K = 2
    # (C1) exemple exact : sans_remise [1, 1], un bloc de 2, famille des lois constantes (sommets δ_0, δ_1), projection =
    # moyenne des lois réalisées (minimise Σ KL(q_s ‖ φ) sur les lois constantes), certificat exact.
    def e_bloc(Q, yb):
        phi = Q.mean(0)
        c = max((Q[:, k] / phi[k]).mean() for k in range(Q.shape[1]))
        return float(np.prod(Q[np.arange(len(yb)), yb] / phi[yb]) / max(1.0, c) ** len(yb)), c

    print("C1. sans_remise [1, 1], un bloc de 2, nul = lois constantes :")
    for p in (0.5, 0.3, 0.1):
        for forme in ("nu", "gel"):
            E, cmax = 0.0, 0.0
            for yb in itertools.product(range(K), repeat=2):
                yb = np.array(yb)
                Q = lois_realisees(lambda h, s: sans_remise([1, 1], h, s), yb, 2, forme)
                e, c = e_bloc(Q, yb)
                pr = np.prod(np.where(yb == 0, p, 1 - p))
                E += pr * e
                cmax = max(cmax, c)
            print(f"    p = {p} ({forme}) : E[e_B] = {E:.6f} (16/3·p(1−p) = {16 / 3 * p * (1 - p):.6f}) ; plus grand certificat {cmax:.6f}")

    # (C2) recherche, parmi des cartes de la grammaire, de violations exactes de Ville (monde p = 1/2, constant, membre de
    # tout nul qui contient les lois constantes) ; lecture aux fins de bloc ; blocs de b ; n tirages.
    cartes = {}
    for a in (1, 2, 3, 6):
        cartes[f"sans_remise [{a}, {a}]"] = (lambda a: (lambda h, s: sans_remise([a, a], h, s)))(a)
    for f in (1, 2):
        for lam in (1e-3, 0.5):
            cartes[f"moyenne_glissante fenêtre {f}, lissage {lam}"] = (lambda f, lam: (lambda h, s: moyenne_glissante(2, f, lam, h, s)))(f, lam)
    print("C2. monde constant p = 1/2 ; par carte : E[e_B1] (nu / gel) ; P(∃ fin de bloc : W ≥ 1/α) exacte (nu / gel / maximum certifié sur les tirages mêmes / rapport au monde)")
    resultats = []
    for nom, carte in cartes.items():
        for b, n in ((2, 2), (2, 8), (2, 12), (3, 12), (4, 12), (6, 12)):
            suites = toutes_suites(K, n)
            lw = {"nu": np.zeros((len(suites), n // b)), "gel": np.zeros((len(suites), n // b))}
            lmax = np.zeros((len(suites), n // b))
            lvrai = np.zeros((len(suites), n // b))
            e1 = {"nu": 0.0, "gel": 0.0}
            for i, y in enumerate(suites):
                for forme in ("nu", "gel"):
                    Q = lois_realisees(carte, y, b, forme)
                    acc = 0.0
                    for B in range(n // b):
                        idx = np.arange(B * b, (B + 1) * b)
                        e, _ = e_bloc(Q[idx], y[idx])
                        acc += math.log(max(e, 1e-300))
                        lw[forme][i, B] = acc
                        if B == 0:
                            e1[forme] += e * 0.5 ** n
                Qn = lois_realisees(carte, y, b, "nu")
                lq = np.cumsum(np.log(Qn[np.arange(n), y]))
                for B in range(n // b):
                    t = (B + 1) * b
                    k1 = int(y[:t].sum())
                    ph = k1 / t
                    lm = (k1 * math.log(ph) if k1 else 0.0) + ((t - k1) * math.log(1 - ph) if t - k1 else 0.0)
                    lmax[i, B] = lq[t - 1] - lm                                 # carte réelle, maximum exact des lois constantes
                    lvrai[i, B] = lq[t - 1] - t * math.log(0.5)
            def pire_rapport(M):
                """sup sur α ∈ ]0, 1[ de P(max_B log W ≥ log 1/α)/α = max_v P(M ≥ v)·e^v, v > 0 (monde uniforme : poids égaux)."""
                m = np.sort(M.max(1))[::-1]
                meilleur, a_pire = 0.0, None
                for i_v, v in enumerate(m):
                    if v <= 1e-12:
                        break
                    r = float((m >= v - 1e-12).mean()) * math.exp(v)
                    if r > meilleur:
                        meilleur, a_pire = r, math.exp(-v)
                return meilleur, a_pire
            rn, an = pire_rapport(lw["nu"]); rg, _ = pire_rapport(lw["gel"]); rm, _ = pire_rapport(lmax); rv, _ = pire_rapport(lvrai)
            p05 = float((lw["nu"] >= math.log(20) - 1e-12).any(1).mean())
            resultats.append((nom, b, n, e1["nu"], e1["gel"], rn, an, rg, rm, rv, p05))
    for nom, b, n, en, eg, rn, an, rg, rm, rv, p05 in resultats:
        marque = "  <-- Ville violée" if rn > 1 + 1e-9 else ""
        a_txt = f"{an:.4f}" if an is not None else "—"
        print(f"    {nom:42s} b={b} n={n:2d} E[e_B1] {en:.4f} / {eg:.4f} ; sup_α P/α : nu {rn:.4f} (α = {a_txt}) ; gel {rg:.4f} ; "
              f"maximum {rm:.4f} ; rapport au monde {rv:.4f} ; P(nu, α = 0,05) {p05:.4f}{marque}")
    print(f"C2. configurations où Ville est violée (sup_α P/α > 1) : nu {sum(r[5] > 1 + 1e-9 for r in resultats)} sur "
          f"{len(resultats)} ; gel {sum(r[7] > 1 + 1e-9 for r in resultats)} ; maximum certifié {sum(r[8] > 1 + 1e-9 for r in resultats)} ; "
          f"rapport au monde {sum(r[9] > 1 + 1e-9 for r in resultats)} ; plus grand E[e_B1] sous gel {max(r[4] for r in resultats):.6f}")


# ---------------------------------------------------------------------------------------------------------------------
def partie_D(repetitions=12):
    """Théorème 1 (maximum certifié sur les tirages mêmes) avec trois membres (cellules A, cellules B, linéaire) ; monde
    dans A ; lectures : T8 = {5, 10} (« éparse »), T40 = {1..10} (« dense ») ; règles : J9 (∃t∈T8 ∀m), J9-D40
    (J9 ou ∃t∈T40 ∀m), par membre (∀m ∃t_m∈T40), réunion ; statistiques : S = min_m max_t W^m_t, E' = min_m W^m_{τ_m}."""
    K, J, n = 2, 2, 10
    T8 = [4, 9]                           # indices 0..n−1 des instants 5 et 10
    rng = rng_de(4)
    suites = toutes_suites(K, n)
    alphas = (0.5, 0.25, 0.1)
    pire = {(r, a): 0.0 for r in ("J9", "J9-D40", "par membre", "réunion", "Ville du monde") for a in alphas}
    ES_max, EE_max, Emax_lambda = 0.0, 0.0, 0.0
    gain = {a: [0, 0, 0] for a in alphas}
    for i in range(repetitions):
        L = rng.dirichlet(np.ones(K), size=(n, J))
        celA = rng.integers(0, 2, size=n)
        celB = rng.integers(0, 2, size=n)
        cel1 = np.zeros(n, dtype=int)
        q = rng.dirichlet(np.ones(K) * 0.6, size=n)
        membres = [(celA, 2), (celB, 2), (cel1, 1)]
        lq = np.cumsum(np.log(q[np.arange(n)[None, :], suites]), axis=1)       # (S, n)
        V = np.zeros((3, len(suites), n))
        Yall = np.eye(K)[suites]                                              # (S, n, K)
        for m, (cel, C) in enumerate(membres):
            for t in range(1, n + 1):
                V[m, :, t - 1] = max_certifie_lot(Yall[:, :t], L[None, :t], cel[:t], C, 600)
        lW = lq[None, :, :] - V                                               # (3, S, n)
        lmin = lW.min(0)                                                      # dénominateur = maximum des membres
        mondes = [em_famille(q, L, celA, 2, 3000)] + [point_au_hasard(rng, 2, J, K) for _ in range(2)]
        for theta in mondes:
            P = probas_famille(theta, L, celA, 2)
            lP = np.cumsum(np.log(P[np.arange(n)[None, :], suites]), axis=1)
            prob = np.exp(lP[:, -1])
            lam = lq - lP
            for a in alphas:
                s = math.log(1 / a)
                r_j9 = (lmin[:, T8] >= s).any(1)
                r_d40 = r_j9 | (lmin >= s).any(1)
                r_mem = (lW >= s).any(2).all(0)
                r_un = r_j9 | r_d40 | r_mem
                r_v = (lam >= s).any(1)
                assert not np.any(r_un & ~r_v), "réunion hors de l'événement de Ville du monde"
                for nom, ev in (("J9", r_j9), ("J9-D40", r_d40), ("par membre", r_mem), ("réunion", r_un), ("Ville du monde", r_v)):
                    pire[(nom, a)] = max(pire[(nom, a)], float(prob[ev].sum()) / a)
                gain[a][0] += int(r_j9.sum()); gain[a][1] += int(r_d40.sum()); gain[a][2] += int(r_mem.sum())
            S = np.exp(lW.max(2).min(0))                                       # min_m max_t W^m_t
            ES_max = max(ES_max, float((prob * S).sum()))
            Emax_lambda = max(Emax_lambda, float((prob * np.exp(lam.max(1))).sum()))
            c = 1 / 0.25                                                       # seuil fixé d'avance
            Ep = np.full(len(suites), np.inf)
            for m in range(3):
                franchit = lW[m] >= math.log(c)
                tau = np.where(franchit.any(1), franchit.argmax(1), n - 1)
                Ep = np.minimum(Ep, np.exp(lW[m][np.arange(len(suites)), tau]))
            EE_max = max(EE_max, float((prob * Ep).sum()))
    print(f"D. {repetitions} plans (K=2, n=10, membres {{cellules A, cellules B, linéaire}}, monde dans A ; projection de la "
          f"carte et deux mondes au hasard) — plus grand P(règle)/α :")
    for nom in ("J9", "J9-D40", "par membre", "réunion", "Ville du monde"):
        print(f"    {nom:15s} " + " ; ".join(f"α={a} : {pire[(nom, a)]:.4f}" for a in alphas))
    print("D. suites promues, sommées sur les plans et les mondes (J9 / J9-D40 / par membre) : "
          + " ; ".join(f"α={a} : {g[0]}/{g[1]}/{g[2]}" for a, g in gain.items()))
    print(f"D. statistique S = min_m max_t W^m_t : plus grande espérance {ES_max:.4f} ; E[max_t Λ_t] la plus grande {Emax_lambda:.4f}")
    print(f"D. forme arrêtée membre par membre E' (seuil c = 4 fixé d'avance) : plus grande espérance {EE_max:.4f}")
    # exemple à la main : S n'est pas une valeur e (un membre fixe P* = (1/2, 1/2), carte (0,9 ; 0,1), lu à t = 1 et 2)
    lam = [max(1.8 ** (2 - k) * 0.2 ** k, (1.8 if y1 == 0 else 0.2)) for y1 in (0, 1) for k in ([0, 1] if y1 == 0 else [1, 2])]
    print(f"D. exemple à la main : E[max(Λ_1, Λ_2)] = {np.mean(lam):.4f}")


# ---------------------------------------------------------------------------------------------------------------------
def partie_E():
    """Lois connues par tirages. Deux cellules g ∈ {0, 1}, deux issues ; loi connue L(1|g) = (0,1 ; 0,9) ; famille
    « loi connue plus bruit aveugle commun » (membre linéaire à une loi connue : sommets L, δ_0, δ_1) ; carte = monde = L
    (copie exacte, membre du vrai nul). Estimation L̂ sur N tirages par cellule ; m tirages frais par cellule ; lecture à
    la fin seulement (borne basse du taux à plusieurs instants). Probabilité exacte (somme sur tous les comptes)."""
    from scipy.stats import binom
    alpha = 0.05
    s = math.log(1 / alpha)

    def bornes(k0, k1, a0, a1, m):
        """Comptes en quatre pseudo-instances (g, y) pondérées ; L (S, 4, 1, 2) ; une seule cellule de poids (C = 1)."""
        S = len(k0)
        Y = np.zeros((S, 4, 2))
        Y[:, 0, 1] = k0; Y[:, 1, 0] = m - k0; Y[:, 2, 1] = k1; Y[:, 3, 0] = m - k1
        L = np.zeros((S, 4, 1, 2))
        for i, a in ((0, a0), (1, a0), (2, a1), (3, a1)):
            L[:, i, 0, 1] = a; L[:, i, 0, 0] = 1 - a
        return max_certifie_lot(Y, L, np.zeros(4, dtype=int), 1, 400)

    for N, m in ((10, 20), (20, 20), (50, 20), (10, 100), (20, 100)):
        K0, K1 = np.meshgrid(np.arange(m + 1), np.arange(m + 1), indexing="ij")
        K0, K1 = K0.ravel(), K1.ravel()
        pk = binom.pmf(K0, m, 0.1) * binom.pmf(K1, m, 0.9)
        lq = K0 * math.log(0.1) + (m - K0) * math.log(0.9) + K1 * math.log(0.9) + (m - K1) * math.log(0.1)
        v = bornes(K0.astype(float), K1.astype(float), np.full(len(K0), 0.1), np.full(len(K0), 0.9), m)
        p_vrai = float(pk[lq - v >= s].sum())
        p_plug = 0.0
        for h0 in range(N + 1):
            for h1 in range(N + 1):
                ph = binom.pmf(h0, N, 0.1) * binom.pmf(h1, N, 0.9)
                if ph < 1e-14:
                    continue
                v = bornes(K0.astype(float), K1.astype(float), np.full(len(K0), h0 / N), np.full(len(K0), h1 / N), m)
                p_plug += ph * float(pk[lq - v >= s].sum())
        print(f"E. N = {N} tirages par cellule pour estimer L, m = {m} tirages frais par cellule, lecture à la fin : "
              f"P(copie promue) certificat « comme si exact » {p_plug:.4f} ; vraies lois {p_vrai:.4f} (α = {alpha})")


if __name__ == "__main__":
    parties = sys.argv[1:] or ["A", "B", "C", "D", "E"]
    for p in parties:
        {"A": partie_A, "B": partie_B, "C": partie_C, "D": partie_D, "E": partie_E}[p]()
        sys.stdout.flush()
