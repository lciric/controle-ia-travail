"""Variantes « à la v67 » d'un même constat (effet de z1 au-delà de K1) dans le monde S-V1 : distances et groupes — v1.

Cartes écrites par programme (aucune carte réelle de la course v67 n'est lue ici). Concepteur neuf (Claude Opus 5.5),
12 novembre 2026. Lancement : `python3 -I -B variantes_v67_v1.py`."""
import os, sys, json, hashlib; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import monde_riche_outils_v1 as M
L = {"type": "softmax", "poids": [[0.833437, 0.861085], [-0.583145, 3.13424], [1.296203, -2.574519]], "biais": [-0.082681, 0.10575, -0.944897]}
K1 = {"type": "softmax", "poids": [[0.0, 0.0], [-0.834964, 0.0], [-0.242046, 0.0]], "biais": [0.0, 0.941698, 0.721847]}
rng = np.random.default_rng(np.random.SeedSequence(20261112, spawn_key=(67,)))
def bruit(l, s):
    W = np.asarray(l["poids"]) * np.exp(rng.normal(0, s, np.shape(l["poids"]))); b = np.asarray(l["biais"]) + rng.normal(0, s * 0.3, 3)
    return {"type": "softmax", "poids": W.round(3).tolist(), "biais": b.round(3).tolist()}
arrondie = {"type": "softmax", "poids": [[0.8, 0.9], [-0.6, 3.1], [1.3, -2.6]], "biais": [-0.1, 0.1, -0.9]}
cartes = {
 "L*-arrondie-1-decimale": arrondie,
 "L*-bruit-0.1": bruit(L, 0.1), "L*-bruit-0.2": bruit(L, 0.2),
 "z1-seul-plus-biais-de-K1": {"type": "softmax", "poids": [[0, 0.86], [-0.83, 3.13], [-0.24, -2.57]], "biais": [0, 0.94, 0.72]},
 "si-z0-positif-deux-softmax": {"type": "si_sinon", "condition": {"indice": 0, "seuil": 0.0}, "si": bruit(L, 0.15), "sinon": bruit(L, 0.15)},
 "par-sous-population": {"type": "par_sous_population", "lois": {"0": bruit(L, 0.15), "1": bruit(L, 0.15)}},
 "si-z1-positif-par-morceaux": {"type": "si_sinon", "condition": {"indice": 1, "seuil": 0.0},
                                "si": {"type": "softmax", "poids": [[0.8, 0.0], [-0.6, 0.0], [1.3, 0.0]], "biais": [0.5, 2.2, -2.5]},
                                "sinon": {"type": "softmax", "poids": [[0.8, 0.0], [-0.6, 0.0], [1.3, 0.0]], "biais": [-0.5, -2.0, 0.6]}},
 "L*-temperee-0.8": {"type": "transformee", "base": L, "puissance": 0.8},
}
noms = list(cartes)
Z, G = M.tirer_instances(np.random.default_rng(1), 2000, 2, 2)
o = M.Oracle(L, 2, 2, n=20000)
print("gains au-delà de K1 (oracle v60) :", {n: round(o.gain_au_dela(cartes[n], [K1]), 3) for n in noms})
gs = {}
for eps in (0.01, 0.02, 0.05):
    g, mats = M.grouper([cartes[n] for n in noms], Z, G, eps=eps)
    gs[eps] = [[noms[i] for i in x] for x in g]
    print("eps", eps, "groupes", len(g), gs[eps])
d = mats["d"]
print("distances d (min des deux projections, nat) :")
for i, n in enumerate(noms):
    print(f"  {n:32s}", " ".join(f"{d[i, j]:.3f}" for j in range(len(noms))))
