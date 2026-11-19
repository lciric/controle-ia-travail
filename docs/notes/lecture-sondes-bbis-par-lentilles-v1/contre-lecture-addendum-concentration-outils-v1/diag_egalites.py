"""Diagnostic des écarts de part en présence d'égalités : choix des vingt premiers (égalités au 20e rang) ou quantile sans soi ?"""
import sys
import numpy as np
import torch
sys.path.insert(0, sys.argv[1])
from controle_ia.lentilles_sondes_bbis import statistiques_v2 as s2
g = np.random.default_rng(int(sys.argv[2]))
for (T, M) in [(500, 101), (2000, 40)]:
    y = (np.round(g.standard_normal((T, M)) * 4) / 4).astype(np.float32)
    y[:, 1] = y[:, 0]
    t = torch.from_numpy(y)
    haut = t.topk(20, dim=0)
    q_dev = s2.quantiles_sans_soi(t, haut.indices, haut.values).numpy()
    idx = haut.indices.numpy()
    q_dir = np.empty_like(q_dev)
    for j in range(M):
        autres = np.delete(y, j, axis=1).astype(np.float64)
        q = np.quantile(autres, 0.99, axis=1)
        q_dir[:, j] = q[idx[:, j]]
    print(f"T={T} M={M} : |Δ quantile sans soi| max sur les mêmes (jeton, direction) = {np.abs(q_dev - q_dir).max():.2e} ; "
          f"parts égales avec les mêmes vingt premiers : {np.array_equal((haut.values.numpy() > q_dev).mean(0), (haut.values.numpy() > q_dir).mean(0))}")
