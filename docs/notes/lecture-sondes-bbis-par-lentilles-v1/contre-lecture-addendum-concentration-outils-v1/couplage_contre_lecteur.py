"""Contre-lecture (Opus 5.5) du terme de couplage de l'addendum « concentration », § 6 (d) et (e).
Lois inventées, scores gaussiens corrélés entre jetons ; aucune donnée, aucun code du paquet.

Partie J (simulation jointe appariée) : par réplique, M directions nulles et une direction lue ; valeur p de concentration au
niveau 0,05 (k = (M+1)/20) sous la statistique corrigée (nulles jugées sur les M − 1 autres) et sous le schéma échangeable exact
(nulles jugées sur les M autres, la lue comprise) ; différence appariée, relative au niveau, multipliée par M.
Partie P (prédiction au premier ordre, M → ∞) : variation relative du taux ≈ −h(q)·E[M·δ | C(v) = q], δ = moyenne sur le jeton
de culmination t d'une nulle (uniforme, indépendant de v par symétrie des jetons) de [q(ζ_t² − 1)/2 + ζ_t]/M, ζ_t = z de v au jeton t ;
h = hasard de C au quantile 0,95 q. Estimée par Monte-Carlo sur la loi de C(v) (z = score, M infini).

Scénarios (corrélation entre jetons) :
  ind        : indépendants ;
  equi-<r>   : équicorrélés, a_t = √r f + √(1−r) e_t ;
  blocs-<r>  : deux moitiés de signes opposés, a_t = s_t √r f + √(1−r) e_t (corrélations ±r) ;
  facteurs-K : a_t = L_t·f + √(1−h) e_t, L_t aléatoire de norme² h = 0,5, K = 8 facteurs (corrélations de signes mêlés).
Graines : numpy.random.SeedSequence(entropy=E_CL, spawn_key=(i,)), E_CL tiré par le contre-lecteur.
Usage : python -I -B couplage_contre_lecteur.py J|P ENTROPIE [T]
"""
import sys
import time
from multiprocessing import Pool

import numpy as np


def charge(scenario, T, g_monde):
    if scenario == "ind":
        return None
    if scenario.startswith("equi"):
        r = float(scenario.split("-")[1])
        return np.full((T, 1), np.sqrt(r)), 1 - r
    if scenario.startswith("blocs"):
        r = float(scenario.split("-")[1])
        s = np.where(np.arange(T) < T // 2, 1.0, -1.0)
        return (s * np.sqrt(r))[:, None], 1 - r
    if scenario.startswith("facteurs"):
        K = int(scenario.split("-")[1])
        L = g_monde.standard_normal((T, K))
        L *= np.sqrt(0.5) / np.linalg.norm(L, axis=1, keepdims=True)
        return L, 0.5
    raise ValueError(scenario)


def tirer(g, n, T, ch):
    e = g.standard_normal((n, T))
    if ch is None:
        return e
    L, res = ch
    f = g.standard_normal((n, L.shape[1]))
    return f @ L.T + np.sqrt(res) * e


def sans_elle_meme(d, M):
    return d * np.sqrt(M / (M - 1)) / np.sqrt(np.maximum(1 - d * d / (M - 1), 1e-300))


def bloc_j(tache):
    scenario, M, T, rep, entropie, i = tache
    g = np.random.Generator(np.random.PCG64(np.random.SeedSequence(entropy=entropie, spawn_key=(i,))))
    ch = charge(scenario, T, np.random.Generator(np.random.PCG64(np.random.SeedSequence(entropy=entropie, spawn_key=(10**6,)))))
    k = (M + 1) // 20
    lot = max(1, 1_000_000 // ((M + 1) * T))
    plus = moins = co_n = ex_n = 0
    fait = 0
    while fait < rep:
        b = min(lot, rep - fait)
        a = tirer(g, b * (M + 1), T, ch).reshape(b, M + 1, T)
        nul = a[:, 1:, :]
        m, s = nul.mean(1, keepdims=True), nul.std(1, keepdims=True)
        dmax = ((nul - m) / s).max(2)
        cv = ((a[:, 0, :] - m[:, 0, :]) / s[:, 0, :]).max(1)
        r_co = (sans_elle_meme(dmax, M) >= cv[:, None]).sum(1) <= k - 1
        mt, st = a.mean(1, keepdims=True), a.std(1, keepdims=True)
        dt = ((a - mt) / st).max(2)
        r_ex = (dt[:, 1:] >= dt[:, :1]).sum(1) <= k - 1
        plus += int((r_co & ~r_ex).sum()); moins += int((~r_co & r_ex).sum())
        co_n += int(r_co.sum()); ex_n += int(r_ex.sum())
        fait += b
    return scenario, M, rep, plus, moins, co_n, ex_n


def partie_j(entropie, T):
    scenarios = ("ind", "equi-0.3", "equi-0.6", "blocs-0.3", "facteurs-8")
    plan = {39: 400_000, 79: 200_000, 159: 100_000}
    taches, i = [], 0
    for sc in scenarios:
        for M, N in plan.items():
            for j in range(4):
                taches.append((sc, M, T, N // 4, entropie, i)); i += 1
    cumul = {}
    with Pool(4) as p:
        for sc, M, r, pl, mo, co, ex in p.imap(bloc_j, taches):
            c = cumul.setdefault((sc, M), np.zeros(5))
            c += (r, pl, mo, co, ex)
    print(f"J. simulation jointe appariée, T = {T}, niveau 0,05 ; colonnes : corrigée, exacte, corrigée − exacte ± erreur type, "
          f"relatif × M ± erreur type")
    for sc in scenarios:
        for M in plan:
            N, pl, mo, co, ex = cumul[(sc, M)]
            d = (pl - mo) / N
            et = np.sqrt(pl + mo - (pl - mo) ** 2 / N) / N
            print(f"  {sc:<11} M = {M:>3} ({int(N)}) : {co / N:.5f} ; {ex / N:.5f} ; {d:+.2e} ± {et:.1e} ; "
                  f"{d / 0.05 * M:+.2f} ± {et / 0.05 * M:.2f} / M")


def partie_p(entropie, T, scenarios=("ind", "equi-0.1", "equi-0.3", "equi-0.6", "blocs-0.3", "facteurs-8"), n=400_000):
    print(f"P. prédiction au premier ordre (M infini), T = {T} : quantile 0,95 q de C, hasard h(q), E[M·δ | C ≈ q], "
          f"variation relative prédite × M = −h·E[M·δ]")
    for idx, sc in enumerate(scenarios):
        g = np.random.Generator(np.random.PCG64(np.random.SeedSequence(entropy=entropie, spawn_key=(2 * 10**6 + idx,))))
        ch = charge(sc, T, np.random.Generator(np.random.PCG64(np.random.SeedSequence(entropy=entropie, spawn_key=(10**6,)))))
        Cs, Ds = [], []
        lot = max(1, 4_000_000 // T)
        fait = 0
        while fait < n:
            b = min(lot, n - fait)
            a = tirer(g, b, T, ch)
            # standardisation exacte de la loi (M infini) : variance 1 par jeton dans tous les scénarios
            C = a.max(1)
            D = (C[:, None] * (a * a - 1) / 2 + a).mean(1)      # E_t[q(ζ²−1)/2 + ζ] avec q ≈ C(v)
            Cs.append(C); Ds.append(D); fait += b
        C, D = np.concatenate(Cs), np.concatenate(Ds)
        q = np.quantile(C, 0.95)
        lar = 0.05 * C.std()
        fen = np.abs(C - q) < lar
        dens = fen.mean() / (2 * lar)
        h = dens / 0.05
        ed = D[fen].mean()
        et = D[fen].std() / np.sqrt(fen.sum())
        print(f"  {sc:<11} : q = {q:.3f} ; h = {h:.3f} ; E[M·δ | C ≈ q] = {ed:+.3f} ± {et:.3f} ; prédit {-h * ed:+.2f} / M "
              f"(à M = 2 000 : {-h * ed / 2000 * 100:+.3f} %)")


if __name__ == "__main__":
    quoi, entropie = sys.argv[1], int(sys.argv[2])
    T = int(sys.argv[3]) if len(sys.argv) > 3 else 128
    t0 = time.time()
    print(f"commande : couplage_contre_lecteur.py {quoi} {entropie} {T} ; numpy {np.__version__}")
    if quoi == "J":
        partie_j(entropie, T)
    else:
        partie_p(entropie, T)
    print(f"durée {time.time() - t0:.0f} s")
