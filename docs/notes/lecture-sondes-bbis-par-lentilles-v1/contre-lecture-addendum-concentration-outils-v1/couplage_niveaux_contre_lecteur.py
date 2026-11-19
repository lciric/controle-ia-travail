"""Contre-lecteur Opus 5.5 : le terme de couplage grandit-il aux niveaux stricts ? Simulation jointe appariée (statistique corrigée
contre schéma échangeable exact) aux niveaux k/(M+1) pour k = 1 et k = (M+1)/20, T = 128 jetons, lois gaussiennes corrélées ;
et prédiction au premier ordre aux mêmes niveaux (M infini). Réemploie les fonctions de `couplage_contre_lecteur.py`.
Usage : python -I -B couplage_niveaux_contre_lecteur.py ENTROPIE"""
import os
import sys
import time
from multiprocessing import Pool

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np  # noqa: E402
import couplage_contre_lecteur as c  # noqa: E402


def bloc(tache):
    scenario, M, T, rep, entropie, i = tache
    g = np.random.Generator(np.random.PCG64(np.random.SeedSequence(entropy=entropie, spawn_key=(5 * 10**6 + i,))))
    ch = c.charge(scenario, T, np.random.Generator(np.random.PCG64(np.random.SeedSequence(entropy=entropie, spawn_key=(10**6,)))))
    ks = (1, (M + 1) // 20)
    lot = max(1, 1_000_000 // ((M + 1) * T))
    n = np.zeros((2, 4), dtype=np.int64)       # par k : plus, moins, corrigée, exacte
    fait = 0
    while fait < rep:
        b = min(lot, rep - fait)
        a = c.tirer(g, b * (M + 1), T, ch).reshape(b, M + 1, T)
        nul = a[:, 1:, :]
        m, s = nul.mean(1, keepdims=True), nul.std(1, keepdims=True)
        dmax = ((nul - m) / s).max(2)
        cv = ((a[:, 0, :] - m[:, 0, :]) / s[:, 0, :]).max(1)
        n_co = (c.sans_elle_meme(dmax, M) >= cv[:, None]).sum(1)
        mt, st = a.mean(1, keepdims=True), a.std(1, keepdims=True)
        dt = ((a - mt) / st).max(2)
        n_ex = (dt[:, 1:] >= dt[:, :1]).sum(1)
        for i_k, k in enumerate(ks):
            r_co, r_ex = n_co <= k - 1, n_ex <= k - 1
            n[i_k] += ((r_co & ~r_ex).sum(), (~r_co & r_ex).sum(), r_co.sum(), r_ex.sum())
        fait += b
    return scenario, M, rep, n


def prediction(entropie, T, sc, niveaux, n=600_000):
    g = np.random.Generator(np.random.PCG64(np.random.SeedSequence(entropy=entropie, spawn_key=(6 * 10**6,))))
    ch = c.charge(sc, T, np.random.Generator(np.random.PCG64(np.random.SeedSequence(entropy=entropie, spawn_key=(10**6,)))))
    a = c.tirer(g, n, T, ch)
    C = a.max(1)
    D = (C[:, None] * (a * a - 1) / 2 + a).mean(1)
    out = []
    for al in niveaux:
        q = np.quantile(C, 1 - al)
        lar = 0.05 * C.std()
        fen = np.abs(C - q) < lar
        h = fen.mean() / (2 * lar) / al
        out.append(-h * D[fen].mean())
    return out


if __name__ == "__main__":
    entropie = int(sys.argv[1])
    T = 128
    t0 = time.time()
    print(f"commande : couplage_niveaux_contre_lecteur.py {entropie} ; numpy {np.__version__} ; T = {T}")
    scenarios = ("equi-0.6", "blocs-0.3")
    plan = {79: 600_000, 159: 300_000}
    taches, i = [], 0
    for sc in scenarios:
        for M, N in plan.items():
            for j in range(4):
                taches.append((sc, M, T, N // 4, entropie, i)); i += 1
    cumul = {}
    with Pool(4) as p:
        for sc, M, r, n in p.imap(bloc, taches):
            x = cumul.setdefault((sc, M), [0, np.zeros((2, 4), dtype=np.int64)])
            x[0] += r; x[1] += n
    for sc in scenarios:
        for M in plan:
            N, n = cumul[(sc, M)]
            pred = prediction(entropie, T, sc, [1 / (M + 1), 0.05])
            for i_k, k in enumerate((1, (M + 1) // 20)):
                pl, mo, co, ex = (int(v) for v in n[i_k])
                niveau = k / (M + 1)
                d = (pl - mo) / N
                et = np.sqrt(pl + mo - (pl - mo) ** 2 / N) / N
                print(f"  {sc:<10} M = {M:>3}, niveau {niveau:.5f} ({N}) : corrigée {co / N:.5f} ; exacte {ex / N:.5f} ; "
                      f"différence relative × M {d / niveau * M:+.2f} ± {et / niveau * M:.2f} ; prédit au premier ordre "
                      f"{pred[i_k]:+.2f}")
    print(f"durée {time.time() - t0:.0f} s")
