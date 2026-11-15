"""Banc commun de l'angle « toute autre voie » (correction des poids du nul) — v1.

Mise au point exploratoire, aucune revendication. Processeur seul, numpy seul. Aucun fichier des dossiers de copie n'est
exécuté ni importé : la logique utile du juge est RECOPIÉE ici, simplifiée, et la simplification est dite :
- pari plein (numérateur = vraisemblance de la carte), comme une carte fraîche de `a_blanc_v59.juger_carte` ;
- n = 200 tirages frais, instants de lecture T = {25, 50, ..., 200}, alpha = 0,05, promotion si log W_t >= log(1/alpha)
  pour un t de T (règle de `nul_filles_v2.evaluer_v2`) ;
- membres du nul : seulement les mélanges de lois connues avec un bruit aveugle commun (famille de `nul_v9.py`, l. 19-25 :
  poids propres à chaque morceau, bruit aveugle commun, somme 1 par morceau) ; la partition « une seule cellule » tient lieu
  du membre linéaire du nul v8 ; les membres ordinaires et log-linéaires du v8 sont OMIS (le dénominateur est donc plus
  petit que celui du juge : la puissance de tous les bras est surestimée de la même façon, la validité n'en dépend pas) ;
- valeur d'un membre = valeur atteinte + écart de Frank-Wolfe (certificat de `nul_v9._certificats`), bornée par 0 ;
  optimiseur : espérance-maximisation (et non les points intérieurs du v9) ; arrêt quand le certificat est à TOL du meilleur
  atteint (élagage comme le v9) ou au plus MAXIT pas : un arrêt prématuré coûte en puissance, jamais en validité ;
- « maximum certifié façon v9 » : partitions = une cellule, sous-population, et toutes les coupes {z_j <= s} | {z_j > s} aux
  valeurs observées des deux traits (le sup sur un seuil réel est le maximum sur ces coupes, `nul_v9.py`, docstring).

Espace du banc (comme le banc B de `prereg-nul-par-morceaux-limite-v1.md`) : K = 3 issues, D = 2 traits gaussiens arrondis à
six décimales, G = 2 sous-populations ; lois softmax de force 1,5 (biais 0,3). Archive : S1, S2 softmax, S3 = si_sinon
({z_jA > s_A}, U1, U2) ; lois connues = (S1, S2, S3) ; coupure de l'archive C_arch = {z_jA > s_A}.
"""
import numpy as np

K, D, N, ALPHA = 3, 2, 200, 0.05
T = np.arange(25, N + 1, 25)
SEUIL = float(np.log(1 / ALPHA))
PLANCHER = 1e-12
TOL, MAXIT = 5e-3, 400
RACINE = 2026111501  # entropie racine des graines de l'angle libre (R9) ; chaque tâche dérive spawn_key=(cas, r)


def rng_de(cas, r):
    return np.random.default_rng(np.random.SeedSequence(entropy=RACINE, spawn_key=(cas, r)))


def soft(rng):
    return np.round(rng.normal(0, 1.5, (K, D)), 6), np.round(rng.normal(0, 0.3, K), 6)


def p_soft(Wb, z):
    s = z @ Wb[0].T + Wb[1]
    s -= s.max(1, keepdims=True)
    e = np.exp(s)
    return e / e.sum(1, keepdims=True)


def archive(rng):
    S1, S2, U1, U2 = soft(rng), soft(rng), soft(rng), soft(rng)
    jA = int(rng.integers(0, 2))
    while True:
        sA = round(float(rng.uniform(-1, 1)), 2)
        if abs(sA) >= 0.05:
            break
    return dict(S1=S1, S2=S2, U1=U1, U2=U2, jA=jA, sA=sA)


def plan(rng, n=N):
    z = np.round(rng.normal(size=(n, D)), 6)
    g = rng.integers(0, 2, n)
    return z, g


def lois_connues(A, z):
    """(n, J, K) : S1, S2, S3 sur le plan."""
    S3 = np.where((z[:, A["jA"]] > A["sA"])[:, None], p_soft(A["U1"], z), p_soft(A["U2"], z))
    return np.stack([p_soft(A["S1"], z), p_soft(A["S2"], z), S3], 1)


def tirer(rng, P):
    u = rng.random(P.shape[0])
    return np.minimum((u[:, None] > np.cumsum(P, 1)).sum(1), K - 1)


def tirer_lot(rng, P, B):
    u = rng.random((B, P.shape[0]))
    return np.minimum((u[:, :, None] > np.cumsum(P, 1)[None]).sum(2), K - 1)


# ---------------------------------------------------------------- partitions (masques « cellule gauche ») -----------
def masque_coupure(z, j, s):
    """cellule 1 = {z_j > s} (sens de `selection_pari._condition`), cellule 0 = le reste."""
    return z[:, j] > s


def partitions_v9(z, g, t):
    """Masques (P, t) des partitions du maximum façon v9 sur les t premières instances : une cellule, sous-population,
    toutes les coupes des deux traits aux valeurs observées. Rend aussi, pour chaque trait, les valeurs triées."""
    zt, gt = z[:t], g[:t]
    ms = [np.zeros(t, bool), gt == 1]
    for j in range(D):
        v = np.unique(zt[:, j])
        for s in v[:-1]:
            ms.append(zt[:, j] > s)
    return np.array(ms)


def em_certifie(Aj, y, M, tol=TOL, maxit=MAXIT, special=None, depart=None):
    """Maximum certifié, pour chaque partition (masque M de forme (P, t)), de f(mu, rho) = sum_s log(mu_{c(s)}.A_s + rho_{y_s})
    sur le polytope (poids propres à la cellule, bruit aveugle commun). Rend (UB, f_atteint, UB - f_atteint) par partition, où
    UB = min(0, min sur les pas de f + écart de Frank-Wolfe) >= sup f (certificat exact, sans hypothèse de convergence).
    Arrêt d'une partition : UB <= meilleur f atteint (toutes partitions) + tol, ou, si `special`, écart propre <= tol."""
    P, t = M.shape
    J = Aj.shape[1]
    Mf = M.astype(float)
    Yb = np.eye(K)[y]
    r = np.full(P, 0.5)
    beta = np.full((P, K), 1.0 / K)
    piL = np.full((P, J), 1.0 / J)
    piR = np.full((P, J), 1.0 / J)
    if depart is not None:  # départ chaud mêlé au centre (comme DEPART_CENTRE du v9) : aucun poids ne reste collé à 0
        r[:] = 0.9 * depart[0] + 0.1 * 0.5
        beta[:] = 0.9 * depart[1] + 0.1 / K
        piL[:] = 0.9 * depart[2] + 0.1 / J
        piR[:] = 0.9 * depart[3] + 0.1 / J
    UB = np.zeros(P)
    UB[:] = np.inf
    F = np.full(P, -np.inf)
    gapv = np.full(P, np.inf)
    actif = np.ones(P, bool)
    special = np.zeros(P, bool) if special is None else special
    for it in range(maxit):
        idx = np.where(actif)[0]
        if len(idx) == 0:
            break
        m = Mf[idx]
        kL = piL[idx] @ Aj.T
        kR = piR[idx] @ Aj.T
        known = m * kL + (1 - m) * kR
        rr = r[idx][:, None]
        blind = beta[idx][:, y]
        p = np.maximum((1 - rr) * known + rr * blind, PLANCHER)
        inv = 1.0 / p
        f = np.log(p).sum(1)
        gL = (m * inv) @ Aj
        gR = ((1 - m) * inv) @ Aj
        gr = inv @ Yb
        gap = np.maximum(gr.max(1), gL.max(1) + gR.max(1)) - t
        gap = np.maximum(gap, 0.0)
        UB[idx] = np.minimum(UB[idx], f + gap)
        F[idx] = np.maximum(F[idx], f)
        gapv[idx] = gap
        meilleur = F.max()
        fini = (UB[idx] <= meilleur + tol) & (~special[idx] | (gap <= tol))
        # pas d'espérance-maximisation (forme close, voir docstring)
        muL = (1 - rr) * piL[idx]
        muR = (1 - rr) * piR[idx]
        AL = muL * gL
        AR = muR * gR
        Bk = r[idx][:, None] * beta[idx] * gr
        Bs = Bk.sum(1)
        r[idx] = np.clip(Bs / t, 1e-300, 1.0)
        beta[idx] = np.where(Bs[:, None] > 0, Bk / np.maximum(Bs[:, None], 1e-300), beta[idx])
        sL, sR = AL.sum(1, keepdims=True), AR.sum(1, keepdims=True)
        piL[idx] = np.where(sL > 0, AL / np.maximum(sL, 1e-300), piL[idx])
        piR[idx] = np.where(sR > 0, AR / np.maximum(sR, 1e-300), piR[idx])
        # plancher numérique des poids (un poids exactement nul ne remonte jamais par ce pas) ; sans effet sur la validité :
        # le certificat vaut en tout point admissible
        r[idx] = np.clip(r[idx], 1e-10, 1 - 1e-10)
        for a in (beta, piL, piR):
            a[idx] = (a[idx] + 1e-10) / (a[idx] + 1e-10).sum(1, keepdims=True)
        actif[idx[fini]] = False
    UB = np.minimum(UB, 0.0)
    return UB, F, UB - np.minimum(F, 0.0), (r, beta, piL, piR)


def em_libre_cellules(Aj, y, cel, C, it=400):
    """Maximum de vraisemblance (sans certificat) d'un mélange PAR CELLULE des J lois connues et des K lois certaines,
    poids séparés par cellule (lettre des fiches argon-p1-01 et argon-p2-01). Rend w (C, J+K)."""
    G = np.concatenate([Aj, np.eye(K)[y]], 1)
    w = np.full((C, G.shape[1]), 1.0 / G.shape[1])
    for c in range(C):
        i = np.where(cel == c)[0]
        if len(i) == 0:
            continue
        Gc = G[i]
        v = w[c].copy()
        for _ in range(it):
            v = v * (Gc.T @ (1 / np.maximum(Gc @ v, PLANCHER))) / len(i)
            v /= v.sum()
        w[c] = v
    return w


def composantes(PL, y):
    n = np.arange(len(y))
    return PL[n, :, y]


# ---------------------------------------------------------------- statistiques des fiches --------------------------
def en_ligne_lot(PL, Y, cel, C, eta=0.2):
    """Nul appris en ligne par descente exponentielle (argon-p2-01), poids par cellule sur J lois + K lois certaines,
    départ uniforme ; Y (B, n) issues de B mondes simulés sur le même plan. Rend log p_enligne cumulé (B, n)."""
    B, n = Y.shape
    J = PL.shape[1]
    w = np.full((B, C, J + K), 1.0 / (J + K))
    out = np.empty((B, n))
    s = np.zeros(B)
    ar = np.arange(B)
    for t in range(n):
        c = cel[t]
        comp = np.concatenate([PL[t][:, Y[:, t]].T, np.eye(K)[Y[:, t]]], 1)  # (B, J+K)
        p = np.maximum((w[:, c] * comp).sum(1), PLANCHER)
        s += np.log(p)
        out[:, t] = s
        w[:, c] *= np.exp(np.minimum(eta * comp / p[:, None], 50.0))
        w[:, c] /= w[:, c].sum(1, keepdims=True)
    return out


def moitie(PL, y, cel, C):
    """argon-p1-01 : poids par cellule ajustés au maximum de vraisemblance sur les n/2 premiers tirages, log p du nul
    ajusté sur la seconde moitié (cumulé à partir de n/2 + 1)."""
    h = len(y) // 2
    Aj = composantes(PL, y)
    w = em_libre_cellules(Aj[:h], y[:h], cel[:h], C)
    G = np.concatenate([Aj, np.eye(K)[y]], 1)
    p2 = np.maximum((w[cel[h:]] * G[h:]).sum(1), PLANCHER)
    return np.cumsum(np.log(p2))


def clopper(k, n, niveau=0.95):
    from scipy.stats import beta
    a = (1 - niveau) / 2
    lo = 0.0 if k == 0 else float(beta.ppf(a, k, n - k + 1))
    hi = 1.0 if k == n else float(beta.ppf(1 - a, k + 1, n - k))
    return [round(lo, 4), round(hi, 4)]


def taux(v):
    v = np.asarray(v, bool)
    return dict(promues=int(v.sum()), mondes=int(len(v)), taux=round(float(v.mean()), 4), ic95=clopper(int(v.sum()), len(v)))
