"""Banc commun des essais « inférence universelle » (correction des poids du nul) — v1.

Mise au point exploratoire, aucune revendication. Processeur seul. Aucun code du dépôt de l'organisme n'est exécuté :
la logique utile du juge est **recopiée** ici, simplifiée, d'après la lecture de
`copie-nul-v9-a41b7b5/orchestrator/pole/nul_v9.py` (famille par morceaux à bruit aveugle commun, certificat de
Frank-Wolfe, lecture aux instants fixés, promotion si log W_t ≥ log(1/α) à un instant lu) et de
`code-organisme-94bfd92/orchestrator/pole/nul_filles_v2.py` (`_lineaire` : membre linéaire certifié).

Simplifications déclarées (le banc n'est pas le juge) :
- K = 3 issues, 2 traits z ~ N(0, 1), une sous-population g ∈ {0, 1}, n = 200 tirages frais, instants 25, 50, …, 200,
  α = 0,05, pari plein (numérateur = loi de la carte, sans « fractions ») ;
- lois connues : S1, S2 (softmax aléatoires) et S3 = si_sinon(z_jA > s_A, U1, U2) (loi d'archive qui porte une coupure) ;
- membres du nul : seulement les membres **linéaires** (mélange des lois connues et des lois certaines δ_k) et leurs
  versions **par morceaux à un niveau** (poids propres à chaque morceau, bruit aveugle commun) ; les membres ordinaires du
  juge (uniforme, marginales) sont des cas particuliers du bruit aveugle ; les membres log-linéaires du v8 sont absents ;
- « v9 du banc » : partitions = aucune (membre linéaire, le v8 du banc), sous-population, coupure de l'archive, et coupures
  sur une **grille fixe** de seuils par trait (quantiles de N(0, 1)), non pas sur tout seuil réel comme le v9 ; la preuve ne
  dépend pas du nombre de coupures ; le prix en puissance du vrai v9 (toutes les coupures) est au moins celui du banc ;
- « limité » : partitions = aucune et coupure de l'archive.
"""

import math

import numpy as np

K, D, N = 3, 2, 200
ALPHA = 0.05
SEUIL = math.log(1.0 / ALPHA)
INSTANTS = tuple(range(25, N + 1, 25))
PLANCHER = 1e-12
NORMALE_QUANTILES = (-1.2816, -0.8416, -0.5244, -0.2533, 0.0, 0.2533, 0.5244, 0.8416, 1.2816)  # déciles de N(0, 1)
GRILLE = NORMALE_QUANTILES
TOL_GROUPE = 1e-3     # même précision visée que TOLERANCE_GROUPE du v9 (nul_v9.py)
ITER_BLOC = 20
ITER_MAX = 400


# --- lois -------------------------------------------------------------------------------------------------------------
def softmax_aleatoire(rng):
    return rng.normal(0.0, 1.5, size=(K, D)), rng.normal(0.0, 0.3, size=K)


def probas_softmax(par, z):
    W, b = par
    s = z @ W.T + b
    s -= s.max(axis=1, keepdims=True)
    e = np.exp(s)
    return e / e.sum(axis=1, keepdims=True)


def tirer_archive(rng):
    """S1, S2 softmax ; S3 = si_sinon(z_jA > s_A, U1, U2) ; |s_A| ≥ 0,05 et s_A hors de la grille (à 0,05 près)."""
    S1, S2, U1, U2 = (softmax_aleatoire(rng) for _ in range(4))
    jA = int(rng.integers(0, D))
    while True:
        sA = round(float(rng.uniform(-1.0, 1.0)), 2)
        if abs(sA) >= 0.05 and min(abs(sA - c) for c in GRILLE) >= 0.05:
            break
    return {"S1": S1, "S2": S2, "U1": U1, "U2": U2, "jA": jA, "sA": sA}


def lois_connues(arch, z):
    """(n, J=3, K) : S1, S2, S3 aux instances z."""
    p1, p2 = probas_softmax(arch["S1"], z), probas_softmax(arch["S2"], z)
    haut = z[:, arch["jA"]] > arch["sA"]
    p3 = np.where(haut[:, None], probas_softmax(arch["U1"], z), probas_softmax(arch["U2"], z))
    return np.stack([p1, p2, p3], axis=1)


def tirer_plan(rng, n=N):
    return np.round(rng.normal(size=(n, D)), 6), rng.integers(0, 2, size=n)


def tirer_issues(rng, P):
    u = rng.random(P.shape[0])
    return np.minimum((u[:, None] > np.cumsum(P, axis=1)).sum(axis=1), K - 1)


# --- partitions (masque booléen « morceau 1 ») ------------------------------------------------------------------------
def masques(z, g, arch, sorte):
    """Liste de masques (n,) ; chaque masque définit deux morceaux {faux, vrai}. Masque tout faux = membre linéaire."""
    n = z.shape[0]
    m = [np.zeros(n, dtype=bool)]
    if sorte in ("limite", "v9"):
        m.append(z[:, arch["jA"]] > arch["sA"])
    if sorte == "v9":
        m.append(g == 1)
        for j in range(D):
            for c in GRILLE:
                m.append(z[:, j] > c)
    if sorte not in ("v8", "limite", "v9"):
        raise ValueError(sorte)
    return np.array(m)


# --- maximum certifié d'une famille par morceaux (copie de la logique de nul_v9 : certificat de Frank-Wolfe) ------------
class Solveur:
    """Maxima certifiés de familles par morceaux, **par lots** (comme `nul_v9.maximiser_par_lots`).

    Une « question » q porte une partition (masque M_q, deux morceaux) et des poids de tirages w_q (0/1 pour « les t premiers
    tirages de la part jugée », λ pour une part pondérée). Elle demande
        sup f_q,  f_q(μ, ρ) = Σ_s w_{q,s} log( Σ_j μ_{c(s), j} A_{s, j} + ρ_{y_s} ),
    sur le polytope {μ ≥ 0, ρ ≥ 0, Σ_j μ_{c, j} + Σ_k ρ_k = 1 pour chaque morceau c} (poids propres au morceau, bruit aveugle
    commun : la famille de `nul_v9`). Paramétrage μ_c = (1 − r)·a_c, ρ = r·β ; montée par espérance-maximisation (a_c ∝ a_c ⊙
    ∂f/∂μ_c, β ∝ β ⊙ ∂f/∂ρ, r ← r·(β·∂f/∂ρ)/Σw), plus un pas de Frank-Wolfe à pas cherché tous les trois pas (sortie des
    poids presque nuls). Valeur rendue : min(0, f(x) + écart de Frank-Wolfe), où l'écart = max_sommet ∇f·v − Σ_s w_s ; c'est
    une **borne haute exacte** du maximum (concavité ; ∇f·x = Σ w par homogénéité), sans hypothèse de convergence.
    Élagage par groupe (une valeur demandée = le maximum sur les questions d'un groupe) : une question s'arrête quand sa
    borne est à moins de `tol` de la meilleure valeur atteinte de son groupe ; sa borne reste dans le maximum rendu."""

    def __init__(self, Ak, y, M, Wt, groupes):
        self.Ak, self.y = Ak, y
        self.Y1 = np.eye(K)[y]
        self.M, self.Wt = M.astype(bool), np.asarray(Wt, dtype=float)
        self.groupes = np.asarray(groupes)
        Q, J = M.shape[0], Ak.shape[1]
        self.J = J
        self.a = np.full((Q, 2, J), 1.0 / J)
        self.r = np.full(Q, 0.1)
        self.beta = np.full((Q, K), 1.0 / K)
        self.tot = self.Wt.sum(1)
        self.vide1 = ~((self.M) & (self.Wt > 0)).any(1)
        self.vide0 = ~((~self.M) & (self.Wt > 0)).any(1)

    def _p(self, idx):
        a, r, beta = self.a[idx], self.r[idx], self.beta[idx]
        m0 = a[:, 0] @ self.Ak.T                      # (q, n)
        m1 = a[:, 1] @ self.Ak.T
        known = np.where(self.M[idx], m1, m0)
        blind = beta @ self.Y1.T
        return np.maximum((1.0 - r)[:, None] * known + r[:, None] * blind, PLANCHER), known, blind

    def _gradients(self, idx):
        p, _, _ = self._p(idx)
        W = self.Wt[idx]
        inv = W / p                                    # (q, n)
        Mf = self.M[idx]
        g1 = (inv * Mf) @ self.Ak                      # (q, J)
        g0 = (inv * ~Mf) @ self.Ak
        gr = inv @ self.Y1                             # (q, K)
        f = (W * np.log(p)).sum(1)
        sommet = np.maximum(gr.max(1), np.where(self.vide0[idx], 0.0, g0.max(1)) + np.where(self.vide1[idx], 0.0, g1.max(1)))
        ecart = np.maximum(0.0, sommet - self.tot[idx])
        return f, ecart, g0, g1, gr, p

    def _pas_frank_wolfe(self, idx, g0, g1, gr, p):
        W = self.Wt[idx]
        s_mu = np.where(self.vide0[idx], 0.0, g0.max(1)) + np.where(self.vide1[idx], 0.0, g1.max(1))
        aveugle = gr.max(1) > s_mu
        k = gr.argmax(1); j0 = g0.argmax(1); j1 = g1.argmax(1)
        v_mu = np.where(self.M[idx], self.Ak[:, j1].T, self.Ak[:, j0].T)   # (q, n)
        v_bl = self.Y1[:, k].T
        v = np.where(aveugle[:, None], v_bl, v_mu)
        d = v - p
        lo = np.zeros(len(idx)); hi = np.ones(len(idx))
        plein = (W * d / np.maximum(p + d, PLANCHER)).sum(1) >= 0
        for _ in range(10):
            mid = 0.5 * (lo + hi)
            der = (W * d / np.maximum(p + mid[:, None] * d, PLANCHER)).sum(1)
            lo = np.where(der > 0, mid, lo); hi = np.where(der > 0, hi, mid)
        gam = np.clip(np.where(plein, 1.0 - 1e-9, lo), 0.0, 1.0 - 1e-9)[:, None]
        a, r, beta = self.a[idx], self.r[idx], self.beta[idx]
        mu0 = (1 - r)[:, None] * a[:, 0]; mu1 = (1 - r)[:, None] * a[:, 1]; rho = r[:, None] * beta
        e0 = np.eye(self.J)[j0]; e1 = np.eye(self.J)[j1]; ek = np.eye(K)[k]
        av = aveugle[:, None]
        mu0 = (1 - gam) * mu0 + np.where(av, 0.0, gam * e0)
        mu1 = (1 - gam) * mu1 + np.where(av, 0.0, gam * e1)
        rho = (1 - gam) * rho + np.where(av, gam * ek, 0.0)
        self.r[idx] = np.clip(rho.sum(1), 1e-12, 1 - 1e-12)
        self.beta[idx] = (rho + 1e-300) / (rho + 1e-300).sum(1, keepdims=True)
        self.a[idx, 0] = (mu0 + 1e-300) / (mu0 + 1e-300).sum(1, keepdims=True)
        self.a[idx, 1] = (mu1 + 1e-300) / (mu1 + 1e-300).sum(1, keepdims=True)

    def resoudre(self, tol=None, iter_max=None):
        """Rend (bornes certifiées par question (Q,), valeurs atteintes (Q,), maximum certifié par groupe {groupe: valeur})."""
        tol = TOL_GROUPE if tol is None else tol
        iter_max = ITER_MAX if iter_max is None else iter_max
        Q = self.M.shape[0]
        actifs = np.arange(Q)
        f_all = np.full(Q, -np.inf); cert = np.full(Q, np.inf)
        it = 0
        while True:
            f, ecart, g0, g1, gr, p = self._gradients(actifs)
            f_all[actifs] = f
            cert[actifs] = np.minimum(0.0, f + ecart)
            if it % ITER_BLOC == 0 or it >= iter_max:
                meilleur = np.full(self.groupes.max() + 1, -np.inf)
                np.maximum.at(meilleur, self.groupes, f_all)
                garder = cert[actifs] - meilleur[self.groupes[actifs]] > tol
                if it >= iter_max or not garder.any():
                    break
                if not garder.all():
                    actifs = actifs[garder]
                    g0, g1, gr, p = g0[garder], g1[garder], gr[garder], p[garder]
            a, r, beta = self.a[actifs], self.r[actifs], self.beta[actifs]
            a0 = a[:, 0] * g0 + 1e-300; a1 = a[:, 1] * g1 + 1e-300
            self.a[actifs, 0] = a0 / a0.sum(1, keepdims=True)
            self.a[actifs, 1] = a1 / a1.sum(1, keepdims=True)
            bg = beta * gr
            self.r[actifs] = np.clip(r * bg.sum(1) / self.tot[actifs], 1e-12, 1 - 1e-12)
            self.beta[actifs] = (bg + 1e-300) / (bg + 1e-300).sum(1, keepdims=True)
            if it % 3 == 0:
                _, _, g0, g1, gr, p = self._gradients(actifs)
                self._pas_frank_wolfe(actifs, g0, g1, gr, p)
            it += 1
        par_groupe = {}
        for gq in np.unique(self.groupes):
            par_groupe[int(gq)] = float(cert[self.groupes == gq].max())
        self.iterations = it
        return cert, f_all, par_groupe


def matrice_connues(Lc, y):
    """A (n, J) : probabilité de chaque loi connue à l'issue observée."""
    return Lc[np.arange(len(y)), :, y]


def questions(Mpart, poids_list):
    """Produit (partitions × vecteurs de poids) : rend M (Q, n), Wt (Q, n), groupes (Q,) — un groupe par vecteur de poids."""
    P = Mpart.shape[0]
    M = np.concatenate([Mpart for _ in poids_list])
    Wt = np.concatenate([np.tile(w, (P, 1)) for w in poids_list])
    gr = np.repeat(np.arange(len(poids_list)), P)
    return M, Wt, gr


def promue(log_w, seuil=SEUIL):
    return bool(np.max(log_w) >= seuil)


def clopper_pearson(k, n, niveau=0.95):
    from scipy.stats import beta as B
    a = (1 - niveau) / 2
    bas = 0.0 if k == 0 else float(B.ppf(a, k, n - k + 1))
    haut = 1.0 if k == n else float(B.ppf(1 - a, k + 1, n - k))
    return [round(bas, 4), round(haut, 4)]


# --- mondes ------------------------------------------------------------------------------------------------------------
def poids_membre(rng, sorte):
    """Poids (μ_0, μ_1, ρ) d'un membre du nul limité (coupure de l'archive, bruit commun)."""
    J = 3
    if sorte == "interieur":
        r = float(rng.uniform(0.05, 0.4))
        a0, a1, be = rng.dirichlet(np.ones(J)), rng.dirichlet(np.ones(J)), rng.dirichlet(np.ones(K))
    elif sorte == "sommet":            # bord du simplexe : une loi connue par morceau, aucun bruit
        r = 0.0
        j0, j1 = rng.choice(J, size=2, replace=False)
        a0, a1, be = np.eye(J)[j0], np.eye(J)[j1], np.full(K, 1.0 / K)
    elif sorte == "extreme":           # poids extrêmes : presque un sommet, un peu de bruit concentré sur une issue
        r = 0.01
        j0, j1 = rng.choice(J, size=2, replace=False)
        a0 = np.full(J, 0.005); a0[j0] = 1 - 0.005 * (J - 1)
        a1 = np.full(J, 0.005); a1[j1] = 1 - 0.005 * (J - 1)
        be = np.full(K, 0.01); be[int(rng.integers(0, K))] = 1 - 0.01 * (K - 1)
    elif sorte == "bruite":            # copie par morceaux sur la coupure de l'archive avec fort bruit aveugle
        r = 0.4
        j0, j1 = rng.choice(J, size=2, replace=False)
        a0, a1, be = np.eye(J)[j0], np.eye(J)[j1], rng.dirichlet(np.ones(K))
    else:
        raise ValueError(sorte)
    return a0, a1, r, be


def loi_membre(Lc, haut, a0, a1, r, be):
    mix = np.where(haut[:, None], np.einsum("njk,j->nk", Lc, a1), np.einsum("njk,j->nk", Lc, a0))
    return (1 - r) * mix + r * be[None, :]


def monde(cas, ss):
    """Un monde du banc : rend un dictionnaire (z, g, Lc, P loi du monde, Q loi de la carte, y, archive).
    Cas de taille (Q = P, P membre d'un nul) : 'interieur', 'sommet', 'extreme', 'bruite' (coupure de l'archive),
    'sous_population' (copie par sous-population, classe v9 du banc seulement), 'grille' (coupure d'un seuil de la grille,
    classe v9 du banc seulement), 'v8' (mélange sans coupure, toutes les classes).
    Cas de puissance : ('neuve', λ) : P = (1 − λ)·membre intérieur + λ·N, N softmax neuve hors de l'archive ; Q = P."""
    rng = np.random.default_rng(ss)
    arch = tirer_archive(rng)
    z, g = tirer_plan(rng)
    Lc = lois_connues(arch, z)
    haut_arch = z[:, arch["jA"]] > arch["sA"]
    if isinstance(cas, tuple) and cas[0] == "neuve":
        lam = cas[1]
        a0, a1, r, be = poids_membre(rng, "interieur")
        base = loi_membre(Lc, haut_arch, a0, a1, r, be)
        Nn = probas_softmax(softmax_aleatoire(rng), z)
        P = (1 - lam) * base + lam * Nn
    elif cas in ("interieur", "sommet", "extreme", "bruite"):
        P = loi_membre(Lc, haut_arch, *poids_membre(rng, cas))
    elif cas == "v8":
        a0, a1, r, be = poids_membre(rng, "interieur")
        P = loi_membre(Lc, haut_arch, a0, a0, r, be)
    elif cas == "sous_population":
        j0, j1 = rng.choice(3, size=2, replace=False)
        P = loi_membre(Lc, g == 1, np.eye(3)[j0], np.eye(3)[j1], 0.0, np.full(K, 1 / K))
    elif cas == "grille":
        j = int(rng.integers(0, D)); c = GRILLE[int(rng.integers(0, len(GRILLE)))]
        j0, j1 = rng.choice(3, size=2, replace=False)
        P = loi_membre(Lc, z[:, j] > c, np.eye(3)[j0], np.eye(3)[j1], 0.0, np.full(K, 1 / K))
    else:
        raise ValueError(cas)
    P = np.maximum(P, 0.0); P /= P.sum(1, keepdims=True)
    y = tirer_issues(rng, P)
    return {"arch": arch, "z": z, "g": g, "Lc": Lc, "P": P, "Q": P.copy(), "y": y}


# --- méthodes ----------------------------------------------------------------------------------------------------------
BETA_CONFIANCE = 0.025          # part de α dépensée par la région de confiance (Berger et Boos, à vérifier sur pièce)
LAMBDAS = (0.0, 0.25, 1.0, 4.0, 16.0)
INSTANTS_DENSES = tuple(range(10, N + 1, 10))
B_SOUS = 4
D_LIBRES = 7                    # paramètres libres d'un membre à deux morceaux : 2·(J − 1) + 1 + (K − 1)
ETAS = (0.05, 0.2)


def _prefixe(t, debut=0):
    w = np.zeros(N); w[debut:debut + t] = 1.0
    return w


def _resoudre(Ak, y, Mp, poids):
    M, Wt, gr = questions(Mp, poids)
    S = Solveur(Ak, y, M, Wt, gr)
    cert, f, pg = S.resoudre()
    return cert.reshape(len(poids), Mp.shape[0]), f.reshape(len(poids), Mp.shape[0]), np.array([pg[i] for i in range(len(poids))]), S


def lw_classe(w, sorte, instants=INSTANTS):
    """log W_t de l'inférence universelle pleine (numérateur gelé, maximum certifié sur les t premiers tirages) ;
    rend aussi les bornes par partition (pour le mélange a priori)."""
    y, Ak, cum = w["y"], w["Ak"], w["cum"]
    Mp = masques(w["z"], w["g"], w["arch"], sorte)
    cert, _, pg, _ = _resoudre(Ak, y, Mp, [_prefixe(t) for t in instants])
    return np.array([cum[t - 1] for t in instants]) - pg, cert


def lw_part(w, sorte, poids_list):
    """log W sur des parts jugées données (vecteurs 0/1) : Σ_part log q − maximum certifié du nul **sur cette part**."""
    y, Ak, lq = w["y"], w["Ak"], w["lq"]
    Mp = masques(w["z"], w["g"], w["arch"], sorte)
    _, _, pg, _ = _resoudre(Ak, y, Mp, poids_list)
    return np.array([float(p @ lq) for p in poids_list]) - pg


def methode_moitie_jugee(w, sorte="v9"):
    """Découpe correcte : le nul est maximisé sur la seconde moitié, celle où W est évalué (la première est perdue,
    le numérateur étant gelé)."""
    t0s = [25, 50, 75, 100]
    return lw_part(w, sorte, [_prefixe(t, 100) for t in t0s])


def methode_croisee(w, sorte="v9"):
    """Découpes croisées paire / impaire : e_t = ½(W^A_t + W^B_t), chaque W calculé sur sa part, à l'instant t."""
    imp = (np.arange(N) % 2 == 0).astype(float)
    pai = 1.0 - imp
    pl = []
    for t in INSTANTS:
        pre = _prefixe(t)
        pl += [pre * imp, pre * pai]
    lw = lw_part(w, sorte, pl).reshape(len(INSTANTS), 2)
    m = lw.max(1)
    return m + np.log(0.5 * np.exp(lw - m[:, None]).sum(1))


def methode_sous_echantillons(w, sous, sorte="v9"):
    """Sous-échantillonnage : B moitiés tirées avant les issues (graine propre) ; e_t = moyenne des W^b_t."""
    pl = []
    for t in INSTANTS:
        pre = _prefixe(t)
        for S_b in sous:
            pl.append(pre * S_b)
    lw = lw_part(w, sorte, pl).reshape(len(INSTANTS), len(sous))
    m = lw.max(1)
    return m + np.log(np.exp(lw - m[:, None]).mean(1))


def methode_confiance(w, sorte="v9", beta=BETA_CONFIANCE, lambdas=LAMBDAS):
    """Région de confiance apprise sur la première moitié D1, maximum du nul pris sur la seconde D0 et restreint à
    C = {θ : log L_θ(D1) > log q(D1) − log(1/β)} ; borne par dualité faible : pour tout λ ≥ 0,
    sup_C log L_θ(D0_t) ≤ sup_θ [log L_θ(D0_t) + λ log L_θ(D1)] − λ (log q(D1) − log(1/β)) ; seuil log(1/(α − β))."""
    y, Ak, lq = w["y"], w["Ak"], w["lq"]
    Mp = masques(w["z"], w["g"], w["arch"], sorte)
    d1 = _prefixe(100)
    lq1 = float(d1 @ lq)
    pl, meta = [], []
    for t0 in (25, 50, 75, 100):
        for lam in lambdas:
            pl.append(_prefixe(t0, 100) + lam * d1)
            meta.append((t0, lam))
    _, _, pg, _ = _resoudre(Ak, y, Mp, pl)
    sortie = []
    for i, t0 in enumerate((25, 50, 75, 100)):
        bornes = [pg[i * len(lambdas) + k] - lam * (lq1 - math.log(1 / beta)) for k, lam in enumerate(lambdas)]
        sortie.append(float(_prefixe(t0, 100) @ lq) - min(bornes))
    return np.array(sortie)


def methode_en_ligne(w, eta):
    """Fiche argon-p2-01 : poids par cellule de la partition de l'archive, sur J lois connues et K lois certaines,
    appris en ligne par descente exponentielle ; dénominateur = produit des prédictions p_{w_{s−1}}(y_s)."""
    y, Lc, lq = w["y"], w["Lc"], w["lq"]
    cel = (w["z"][:, w["arch"]["jA"]] > w["arch"]["sA"]).astype(int)
    J = Lc.shape[1]
    poids = np.full((2, J + K), 1.0 / (J + K))
    s, lw = 0.0, np.empty(N)
    for t in range(N):
        comp = np.concatenate([Lc[t, :, y[t]], np.eye(K)[y[t]]])
        c = cel[t]
        p = max(PLANCHER, float(poids[c] @ comp))
        s += lq[t] - math.log(p)
        lw[t] = s
        poids[c] *= np.exp(np.minimum(eta * comp / p, 50.0))
        poids[c] /= poids[c].sum()
    return lw[np.array(INSTANTS) - 1]


def methode_moitie_fiche(w):
    """Fiche argon-p1-01 : poids du nul limité ajustés (maximum de vraisemblance) sur la première moitié, valeur e sur la
    seconde avec ces poids fixés ; lecture aux instants 25 à 100 de la seconde moitié."""
    y, Ak, lq = w["y"], w["Ak"], w["lq"]
    Mp = masques(w["z"], w["g"], w["arch"], "limite")
    M, Wt, gr = questions(Mp, [_prefixe(100)])
    S = Solveur(Ak, y, M, Wt, gr)
    cert, f, _ = S.resoudre(tol=1e-4, iter_max=1000)
    q = int(np.argmax(f))
    p, _, _ = S._p(np.array([q]))
    p = p[0]
    d = np.cumsum((lq - np.log(p))[100:])
    return d[np.array([25, 50, 75, 100]) - 1]


def preparer(w):
    y = w["y"]
    w["Ak"] = matrice_connues(w["Lc"], y)
    w["lq"] = np.log(np.maximum(w["Q"][np.arange(N), y], PLANCHER))
    w["cum"] = np.cumsum(w["lq"])
    return w


def sous_ensembles(ss_sous, B=B_SOUS):
    rng = np.random.default_rng(ss_sous)
    out = []
    for _ in range(B):
        v = np.zeros(N); v[rng.choice(N, size=N // 2, replace=False)] = 1.0
        out.append(v)
    return out


def melange_a_priori(cert, cum, instants=INSTANTS):
    """Fiche fable-p1-05 et point 5 de nul_v9 : dénominateur log Σ_F π_F exp(v_F), π uniforme sur les partitions (bornes
    certifiées par partition : le dénominateur calculé majore le vrai, la richesse calculée est donc minorée)."""
    m = cert.max(1)
    den = m + np.log(np.exp(cert - m[:, None]).mean(1))
    return np.array([cum[t - 1] for t in instants]) - den


# --- jeu ---------------------------------------------------------------------------------------------------------------
SEUIL_CONFIANCE = math.log(1.0 / (ALPHA - BETA_CONFIANCE))
METHODES = ("v8", "limite", "v9", "v9_dense", "penalise_1nat", "penalise_bic", "melange_a_priori",
            "moitie_jugee", "croisee", "sous_echantillons", "confiance", "fiche_en_ligne_0.05", "fiche_en_ligne_0.2",
            "fiche_moitie")
VALIDES_ATTENDUES = ("v8", "limite", "v9", "v9_dense", "moitie_jugee", "croisee", "sous_echantillons", "confiance")


def evaluer(w, sous, methodes):
    """Rend {méthode: (log W par instant lu, seuil)} pour un monde."""
    out = {}
    lw9 = cert9 = None
    if any(m in methodes for m in ("v9", "penalise_1nat", "penalise_bic", "melange_a_priori")):
        lw9, cert9 = lw_classe(w, "v9")
    for m in methodes:
        if m == "v8":
            out[m] = (lw_classe(w, "v8")[0], SEUIL)
        elif m == "limite":
            out[m] = (lw_classe(w, "limite")[0], SEUIL)
        elif m == "v9":
            out[m] = (lw9, SEUIL)
        elif m == "v9_dense":
            out[m] = (lw_classe(w, "v9", INSTANTS_DENSES)[0], SEUIL)
        elif m == "penalise_1nat":
            out[m] = (lw9 + 1.0, SEUIL)
        elif m == "penalise_bic":
            out[m] = (lw9 + 0.5 * D_LIBRES * np.log(np.array(INSTANTS, dtype=float)), SEUIL)
        elif m == "melange_a_priori":
            out[m] = (melange_a_priori(cert9, w["cum"]), SEUIL)
        elif m == "moitie_jugee":
            out[m] = (methode_moitie_jugee(w), SEUIL)
        elif m == "croisee":
            out[m] = (methode_croisee(w), SEUIL)
        elif m == "sous_echantillons":
            out[m] = (methode_sous_echantillons(w, sous), SEUIL)
        elif m == "confiance":
            out[m] = (methode_confiance(w), SEUIL_CONFIANCE)
        elif m.startswith("fiche_en_ligne_"):
            out[m] = (methode_en_ligne(w, float(m.rsplit("_", 1)[1])), SEUIL)
        elif m == "fiche_moitie":
            out[m] = (methode_moitie_fiche(w), SEUIL)
        else:
            raise ValueError(m)
    return out


def _un_monde(args):
    cas, entropie, cle, methodes = args
    ss = np.random.SeedSequence(entropy=entropie, spawn_key=cle)
    s_monde, s_sous = ss.spawn(2)
    w = preparer(monde(cas, s_monde))
    res = evaluer(w, sous_ensembles(s_sous), methodes)
    return {m: (bool(np.max(lw) >= sl), float(np.max(lw))) for m, (lw, sl) in res.items()}, \
        {m: [round(float(v), 6) for v in lw] for m, (lw, sl) in res.items() if m in ("v8", "limite", "v9")}


def jouer(cas, R, methodes, entropie, i_cas, processus=3):
    """R mondes du cas ; graine du monde r : SeedSequence(entropy=entropie, spawn_key=(i_cas, r)), scindée en (monde,
    sous-ensembles). Rend le résumé par méthode et les comptes de contrôle (monotonie v9 ≤ limité ≤ v8)."""
    import multiprocessing as mp
    taches = [(cas, entropie, (i_cas, r), methodes) for r in range(R)]
    with mp.get_context("fork").Pool(processus) as pool:
        sorties = pool.map(_un_monde, taches, chunksize=8)
    resume = {}
    for m in methodes:
        pro = [s[0][m][0] for s in sorties]
        mx = np.array([s[0][m][1] for s in sorties])
        k = int(sum(pro))
        resume[m] = {"mondes": R, "promotions": k, "taux": round(k / R, 4), "intervalle_clopper_pearson_95": clopper_pearson(k, R),
                     "log_w_max_plus_grand": round(float(mx.max()), 4), "log_w_max_median": round(float(np.median(mx)), 4)}
    controles = {}
    if all(m in methodes for m in ("v8", "limite", "v9")):
        viol = 0
        for s in sorties:
            a, b_, c = (np.array(s[1][m]) for m in ("v8", "limite", "v9"))
            viol += int((c > b_ + 1e-2).any() or (b_ > a + 1e-2).any())
        controles["mondes_avec_monotonie_violee_au_dela_de_0.01_nat"] = viol
    apparies = {}
    for ref in ("v9", "limite"):
        if ref in methodes:
            for m in methodes:
                if m != ref:
                    a = np.array([s[0][m][0] for s in sorties]); b_ = np.array([s[0][ref][0] for s in sorties])
                    apparies[f"{m}_contre_{ref}"] = {"seule_la_methode": int((a & ~b_).sum()), "seule_la_reference": int((~a & b_).sum()),
                                                     "ecart_de_taux": round(float(a.mean() - b_.mean()), 4)}
    return resume, controles, apparies
