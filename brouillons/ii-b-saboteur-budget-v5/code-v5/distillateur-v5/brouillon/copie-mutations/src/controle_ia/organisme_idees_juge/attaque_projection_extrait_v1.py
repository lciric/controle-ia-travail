"""Idée 1.1 (préenregistrement scellé `3ffe1739…`) : extraits **recopiés octet pour octet** (par analyse syntaxique) de
`docs/notes/organisme-idees-juge-v1/correction-poids-v1/projection/attaque_projection_v1.py` (`c6161399…`) : l'optimiseur
`em_commun` de ce fichier (distinct de celui de `projection_commun_v1`), `loi_commun`, `projeter_commun`,
`projection_globale` (monde de la ligne Q8 : projection d'information inverse de la carte sur la famille linéaire de
l'archive, 600 pas) et `carte_a_memoire` (carte de la ligne H7, genre « contre_exces_du_bloc », hors grammaire). Seul
ajout : l'en-tête d'import et les constantes `K` et `MINI` recopiées. L'égalité de chaque corps est éprouvée par un essai."""
import numpy as np


K = 3


MINI = 1e-300


def em_commun(a, bb, w, cel, C, iters):
    """Maximise Σ_i w_i·log((1 − τ)·Σ_j v[cel_i, j]·a[i, j] + τ·Σ_k u_k·bb[i, k]) pour F problèmes à la fois.
    a (F, N, J), bb (F, N, Kb), w (F, N), cel (F, N). Espérance-maximisation ; après chaque pas, un pas allongé dans
    la même direction (x·(x'/x)^α, renormalisé) est essayé et gardé seulement s'il fait mieux que le pas simple ;
    α double après un succès, se divise par deux après un échec. Rend (tau, v, u)."""
    F, N, J = a.shape
    Kb = bb.shape[2]
    lig = np.arange(F)[:, None]
    oh = np.zeros((F, N, C))
    oh[lig, np.arange(N)[None, :], cel] = 1.0
    wt = w.sum(1)

    def lois(tau, v, u):
        cj = v[lig, cel] * a
        ck = bb * u[:, None, :]
        return cj, ck, (1.0 - tau)[:, None] * cj.sum(2) + tau[:, None] * ck.sum(2)

    def valeur(p):
        return (w * np.log(np.maximum(p, MINI))).sum(1)

    def pas(tau, v, u, cj, ck, p):
        gr = w / np.maximum(p, MINI)
        rj = (1.0 - tau)[:, None, None] * cj * gr[:, :, None]
        rk = tau[:, None] * np.einsum("fn,fnk->fk", gr, ck)
        nv = np.einsum("fnc,fnj->fcj", oh, rj)
        sv = nv.sum(2, keepdims=True)
        v1 = np.where(sv > 0, nv / np.where(sv > 0, sv, 1.0), v)
        sk = rk.sum(1)
        u1 = np.where(sk[:, None] > 0, rk / np.where(sk[:, None] > 0, sk[:, None], 1.0), u)
        return np.clip(sk / wt, 1e-12, 1.0 - 1e-12), v1, u1

    def allonge(x, x1, al):
        with np.errstate(divide="ignore", invalid="ignore", over="ignore"):
            lx = np.log(np.maximum(x, MINI)) + al * (np.log(np.maximum(x1, MINI)) - np.log(np.maximum(x, MINI)))
            lx = lx - lx.max(-1, keepdims=True)
            ex = np.exp(lx)
            return ex / ex.sum(-1, keepdims=True)

    tau = np.full(F, 0.2)
    v = np.full((F, C, J), 1.0 / J)
    u = np.full((F, Kb), 1.0 / Kb)
    al = np.full(F, 2.0)
    cj, ck, p = lois(tau, v, u)
    for _ in range(iters):
        t1, v1, u1 = pas(tau, v, u, cj, ck, p)
        c1 = lois(t1, v1, u1)
        duo = allonge(np.stack([tau, 1.0 - tau], 1), np.stack([t1, 1.0 - t1], 1), al[:, None])
        te = np.clip(duo[:, 0], 1e-12, 1.0 - 1e-12)
        ve = allonge(v, v1, al[:, None, None])
        ue = allonge(u, u1, al[:, None])
        ce = lois(te, ve, ue)
        f1, fe = valeur(c1[2]), valeur(ce[2])
        ok = np.isfinite(fe) & (fe > f1)
        tau = np.where(ok, te, t1)
        v = np.where(ok[:, None, None], ve, v1)
        u = np.where(ok[:, None], ue, u1)
        cj = np.where(ok[:, None, None], ce[0], c1[0])
        ck = np.where(ok[:, None, None], ce[1], c1[1])
        p = np.where(ok[:, None], ce[2], c1[2])
        al = np.where(ok, np.minimum(2.0 * al, 64.0), np.maximum(0.5 * al, 1.5))
    return tau, v, u


def loi_commun(Lb, cel, tau, v, u):
    """Lb (F, S, J, K) ; rend P (F, S, K)."""
    F = Lb.shape[0]
    vs = v[np.arange(F)[:, None], cel]
    return (1.0 - tau)[:, None, None] * np.einsum("fsj,fsjk->fsk", vs, Lb) + (tau[:, None] * u)[:, None, :]


def projeter_commun(Lb, Qb, cel, C, iters):
    """Projection d'information inverse de la carte sur la famille, pour F questions (bloc, partition) : maximise
    Σ_s Σ_y Qb[s, y]·log P(y | x_s). Rend P (F, S, K)."""
    F, S, J, _ = Lb.shape
    a = np.transpose(Lb, (0, 1, 3, 2)).reshape(F, S * K, J)
    bb = np.broadcast_to(np.tile(np.eye(K), (S, 1))[None], (F, S * K, K))
    tau, v, u = em_commun(a, bb, Qb.reshape(F, S * K), np.repeat(cel, K, axis=1), C, iters)
    return loi_commun(Lb, cel, tau, v, u)


def projection_globale(e, Q, cel, C, it=600):
    """Membre de la famille le plus proche de la carte sur tout le plan (un point de la famille : le pire monde nul)."""
    L = e["L"]
    P = projeter_commun(L[None], Q[None], cel[None], C, it)[0]
    return P / P.sum(1, keepdims=True)


def carte_a_memoire(genre, param, part, M, y, b, gele):
    """Loi de la carte à chaque instance, sachant les issues passées. « sans_remise » : la loi de la grammaire du juge
    (p_k ∝ c − nombre de k déjà vus, c = param pour chaque issue), mêlée à la loi du monde avec le poids `part`.
    « contre_exces_du_bloc » : la loi du monde inclinée contre l'excès de chaque issue dans le bloc en cours,
    q(y) ∝ M(y)·exp(−param·(nombre de y dans le bloc − nombre attendu)). `gele` : l'historique n'est lu qu'au début de
    chaque bloc (hypothèse P4 rétablie)."""
    n = len(y)
    Q = np.empty((n, K))
    vus, exces = np.zeros(K), np.zeros(K)
    fige_vus = vus.copy()
    for t in range(n):
        if t % b == 0:
            exces[:] = 0.0
            fige_vus = vus.copy()
        if genre == "sans_remise":
            p = np.maximum(param - (fige_vus if gele else vus), 0.0)
            p = p / p.sum() if p.sum() > 0 else np.full(K, 1.0 / K)
            q = part * p + (1.0 - part) * M[t]
        else:
            q = M[t] * np.exp(-param * (0.0 if gele else exces))
        q = np.maximum(q, 1e-12)
        Q[t] = q / q.sum()
        vus[y[t]] += 1
        exces += np.eye(K)[y[t]] - M[t]
    return Q
