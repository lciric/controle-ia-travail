"""Essai : A4 (b) avec quatre tâches mixtes et 24 paires intra-tâche (la règle propre de A4 (b), « au moins deux tâches
mixtes et dix paires », est remplie) mais 11 actions qui gonflent et 9 qui ne gonflent pas : le module rend « non
calculable » par l'effectif minimal général (10 de chaque côté), règle que le texte de A4 (b) ne cite pas."""
import numpy as np

import complements_p3_v1 as cp

g = np.random.default_rng(12345)
ys = np.array([1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0])
ts = np.repeat([f"t{k}" for k in range(6)], 5)
mixtes = [t for t in np.unique(ts) if 0 < ys[ts == t].sum() < (ts == t).sum()]
paires = sum(int(ys[ts == t].sum()) * int((ts == t).sum() - ys[ts == t].sum()) for t in mixtes)
m = np.isin(ts, mixtes)
print(f"tâches mixtes {len(mixtes)}, paires intra-tâche {paires}, dans les tâches mixtes : {int(ys[m].sum())} positifs, "
      f"{int((1 - ys[m]).sum())} négatifs")
try:
    cp.t1_intra_tache(g.normal(size=30), g.normal(size=(30, 5)), ys, ts, np.random.default_rng(3), 100, 0.95)
except cp.NonCalculable as e:
    print("NonCalculable :", e)
