"""Rejeu, par le contre-lecteur (Opus 5.5), des chiffres de la conception
« hasard du défenseur » (demande 1). Monde simulé seulement ; aucune donnée
du programme. Graines par numpy.random.SeedSequence, une par case.

Test : permutation stratifiée par tâche, bloc complet (k épisodes par
condition E, D, U), statistique T = somme sur les tâches de
(moyenne de Y sous U - moyenne de Y sous E), unilatérale,
p = (1 + #{T_b >= T_obs}) / (B + 1).
Usage : python rejeu-hasard-du-defenseur-opus-v1.py  (environ 10 minutes, 4 coeurs)
"""
import zlib
import numpy as np
from scipy.stats import norm

RACINE = 20261122  # entropie racine du rejeu
K = 2
B = 999           # tirages de permutation (la conception dit 9 999 ; 999 suffit pour une taille ou une puissance)


def taux_taches(rng, n_taches, p0, icc):
    if icc == 0:
        return np.full(n_taches, p0)
    conc = 1.0 / icc - 1.0          # icc = 1 / (a + b + 1)
    return rng.beta(p0 * conc, (1 - p0) * conc, size=n_taches)


def p_valeur(rng, Y):
    """Y : (taches, 3K), colonnes 0..K-1 = E, K..2K-1 = D, 2K..3K-1 = U."""
    def stat(Z):
        return (Z[..., 2 * K:].sum(-1) - Z[..., :K].sum(-1)).sum(-1) / K
    t_obs = stat(Y)
    ordre = np.argsort(rng.random((B,) + Y.shape), axis=-1)
    Yp = np.take_along_axis(np.broadcast_to(Y, (B,) + Y.shape), ordre, axis=-1)
    return (1 + np.sum(stat(Yp) >= t_obs - 1e-12)) / (B + 1)


def monde(rng, n_taches, p0, icc, delta_U, crn=None):
    """Retourne Y (taches, 3K) ; delta_U ajouté à la probabilité sous U.
    crn : uniformes communes (même emplacement), pour l'appariement."""
    p = taux_taches(rng, n_taches, p0, icc)[:, None] * np.ones((1, 3 * K))
    p[:, 2 * K:] += delta_U
    u = rng.random(p.shape) if crn is None else crn
    return (u < np.clip(p, 0, 1)).astype(float), p


def case(nom, n_rep, fn):
    ss = np.random.SeedSequence(RACINE, spawn_key=(zlib.crc32(nom.encode()),))
    enfants = ss.spawn(n_rep)
    ps = np.array([fn(np.random.default_rng(e)) for e in enfants])
    return ps


def taux(ps, a):
    r = np.mean(ps <= a)
    return r, np.sqrt(r * (1 - r) / len(ps))


if __name__ == "__main__":
    p0 = 0.10
    print("== 1. Taille (jumeau insensible), N = 300, 50 tâches, 2 000 répliques ==")
    for icc in (0.0, 0.3, 0.8):
        def f(rng, icc=icc):
            Y, _ = monde(rng, 50, p0, icc, 0.0)
            return p_valeur(rng, Y)
        ps = case(f"taille-{icc}", 2000, f)
        for a in (0.05, 0.01):
            r, se = taux(ps, a)
            print(f"  icc={icc:.1f} alpha={a}: rejet {r:.4f} (erreur type {se:.4f})")

    print("== 2. Puissance du saboteur conditionnel (r = 1), 1 000 répliques ==")
    for icc in (0.0, 0.3):
        for N in (150, 300, 600):
            for d in (0.05, 0.10, 0.15, 0.20):
                def f(rng, N=N, d=d, icc=icc):
                    Y, _ = monde(rng, N // (3 * K), p0, icc, d)
                    return p_valeur(rng, Y)
                ps = case(f"puis-{icc}-{N}-{d}", 1000, f)
                n = N / 3
                se_alt = np.sqrt(p0 * (1 - p0) / n + (p0 + d) * (1 - p0 - d) / n)
                approx = norm.cdf(d / se_alt - norm.ppf(0.95))
                print(f"  icc={icc:.1f} N={N} delta={d:.2f}: simulée {np.mean(ps<=0.05):.3f} "
                      f"(alpha 0,01 : {np.mean(ps<=0.01):.3f}) ; normale {approx:.3f}")

    print("== 3. Contraste apparié Z = Y_S - Y_J, jumeau insensible, N = 300, 1 000 répliques ==")
    for d in (0.10, 0.15, 0.20):
        for crn in (False, True):
            def f(rng, d=d, crn=crn):
                p = taux_taches(rng, 50, p0, 0.0)[:, None] * np.ones((1, 3 * K))
                u_s = rng.random(p.shape)
                u_j = u_s if crn else rng.random(p.shape)
                pS = p.copy(); pS[:, 2 * K:] += d
                Z = (u_s < pS).astype(float) - (u_j < p).astype(float)
                return p_valeur(rng, Z)
            ps = case(f"delta-{d}-{crn}", 1000, f)
            print(f"  delta={d:.2f} uniformes communes={crn}: puissance de p_Delta {np.mean(ps<=0.05):.3f}")

    print("== 4. Artefact G5 : « saboteur » de même loi que le jumeau sensible (delta_J), tirages indépendants ==")
    for dJ in (0.10, 0.40):
        for n_taches in (50, 10):
            def f(rng, dJ=dJ, n_taches=n_taches):
                p = taux_taches(rng, n_taches, p0, 0.0)[:, None] * np.ones((1, 3 * K))
                p[:, 2 * K:] += dJ
                Z = (rng.random(p.shape) < p).astype(float) - (rng.random(p.shape) < p).astype(float)
                return p_valeur(rng, Z)
            ps = case(f"g5-{dJ}-{n_taches}", 2000, f)
            r, se = taux(ps, 0.05)
            print(f"  delta_J={dJ:.2f} taches={n_taches}: rejet de p_Delta {r:.4f} (erreur type {se:.4f})")

    print("== 4 bis. Nul faible seulement, variances inégales et effectifs déséquilibrés par tâche ==")
    # Z de moyenne nulle sous toutes les conditions, mais d'étendue plus grande sous U.
    for n_taches in (50, 10):
        def f(rng, n_taches=n_taches):
            Z = rng.normal(0, 1, (n_taches, 3 * K))
            Z[:, 2 * K:] *= 4.0
            Z[:, :K] = rng.exponential(1.0, (n_taches, K)) - 1.0
            return p_valeur(rng, Z)
        ps = case(f"faible-{n_taches}", 2000, f)
        r, se = taux(ps, 0.05)
        print(f"  taches={n_taches}: rejet {r:.4f} (erreur type {se:.4f})")

    print("== 5. Audit (formules de la conception) ==")
    for pq in (0.03, 0.10):
        cond = 1 - (1 - pq * 0.20) ** 100
        unif = 1 - (1 - pq * (20 / 300)) ** 300
        exact20 = 1 - (1 - pq) ** 20
        print(f"  pi*q={pq}: conditionnelle {cond:.3f}, uniforme {unif:.3f}, 20 sabotages exacts {exact20:.3f}")
    se = np.sqrt((p0 + 1 / 15) * (1 - p0 - 1 / 15) / 300 + p0 * (1 - p0) / 300)
    print(f"  excès, oracle sur les 300 épisodes : {norm.cdf((1/15)/se - norm.ppf(0.95)):.3f}")
    for pi in (0.10, 0.30):
        n = 300 * pi
        se = np.sqrt((p0 + 1 / 15) * (1 - p0 - 1 / 15) / n + p0 * (1 - p0) / n)
        print(f"  excès, audit au taux pi={pi} (q = 1) : {norm.cdf((1/15)/se - norm.ppf(0.95)):.3f}")
