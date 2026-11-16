"""Coût de calcul par carte, bras par bras, sur le banc de l'angle « toute autre voie » — v1 (processeur, un cœur, numpy).
Mesure sur M mondes du cas 8 (composante neuve, dose 0,5) : temps mural médian et maximal par carte de chaque étape.
Usage : python essai_libre_cout_v1.py M SORTIE.json"""
import json
import os
import platform
import sys
import time

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import essai_libre_banc_v2 as b  # noqa: E402
from essai_libre_commun_v1 import (ALPHA, D, N, RACINE, T, archive, composantes, em_certifie, lois_connues, moitie,  # noqa: E402
                                   partitions_v9, plan, rng_de, tirer, tirer_lot)


def main():
    M, sortie = int(sys.argv[1]), sys.argv[2]
    temps = {k: [] for k in ("v9", "La", "Ld", "grille", "A1", "A2", "Mc", "Md")}
    for r in range(M):
        rng = rng_de(500 + 8, r)
        A = archive(rng); z, g = plan(rng); PL = lois_connues(A, z)
        P, _ = b.monde_du_cas(8, rng, A, z, g, PL); y = tirer(rng, P); Aj = composantes(PL, y)
        n = np.arange(N); logq = np.cumsum(np.log(P[n, y]))
        dec = {j: np.quantile(z[:, j], np.arange(0.1, 0.95, 0.1)) for j in range(D)}
        etat = {}
        for k in ("v9", "La", "Ld", "grille"):
            t0 = time.perf_counter()
            for t in T:
                zt, gt = z[:t], g[:t]; un = np.zeros(t, bool)
                Ms = {"v9": lambda: partitions_v9(z, g, t), "La": lambda: np.array([un, zt[:, A["jA"]] > A["sA"]]),
                      "Ld": lambda: np.array([un, zt[:, A["jA"]] > A["sA"], gt == 1, zt[:, 0] > 0, zt[:, 1] > 0]),
                      "grille": lambda: np.array([un, gt == 1] + [zt[:, j] > s for j in range(D) for s in dec[j]])}
                if k == "v9":
                    em_certifie(Aj[:t], y[:t], Ms[k]())
                elif k == "grille":
                    _, _, _, etat[k] = em_certifie(Aj[:t], y[:t], Ms[k](), maxit=600, tol=5e-3, depart=etat.get(k))
                else:
                    _, _, _, etat[k] = em_certifie(Aj[:t], y[:t], Ms[k](), maxit=1500, tol=2e-3, depart=etat.get(k))
            temps[k].append(time.perf_counter() - t0)
        m = z[:, A["jA"]] > A["sA"]; cel = m.astype(int)
        t0 = time.perf_counter(); b.stat_en_ligne(logq[None], PL, y[None], cel); temps["A1"].append(time.perf_counter() - t0)
        t0 = time.perf_counter(); moitie(PL, y, cel, 2); temps["A2"].append(time.perf_counter() - t0)
        t0 = time.perf_counter()
        for Pg in b.grille_La(rng, PL, m):
            Y = tirer_lot(rng, Pg, b.B_GRILLE); LQ = np.cumsum(np.log(np.maximum(P[n[None], Y], 1e-12)), 1)
            b.stat_en_ligne(LQ, PL, Y, cel)
        temps["Mc"].append(time.perf_counter() - t0)
        t0 = time.perf_counter()
        Y = tirer_lot(rng, P, b.B_BOOT); LQ = np.cumsum(np.log(np.maximum(P[n[None], Y], 1e-12)), 1)
        b.stat_en_ligne(LQ, PL, Y, cel)
        temps["Md"].append(time.perf_counter() - t0 + temps["La"][-1])  # ajustement La compris
    out = dict(version="essai_libre_cout_v1", mondes=M, cas=8,
               graines=dict(racine=RACINE, derivation="SeedSequence(entropy=racine, spawn_key=(508, r))"),
               secondes_par_carte={k: dict(mediane=round(float(np.median(v)), 4), maximum=round(float(np.max(v)), 4))
                                   for k, v in temps.items()},
               note="Mc et Md : temps des simulations seulement (plus l'ajustement La pour Md) ; un cœur partagé, nice 10",
               python=platform.python_version(), numpy=np.__version__)
    json.dump(out, open(sortie, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(out["secondes_par_carte"])


if __name__ == "__main__":
    main()
