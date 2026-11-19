import sys, time
sys.path[:0] = ["/home/user/controle-ia-travail/src"]
import numpy as np
from controle_ia.harnais.sondes import score_action
from controle_ia.sondes.familles import SondeLineaireJetons
rng = np.random.default_rng(0)
A = rng.standard_normal((400, 4096)).astype(np.float32).astype(np.float64)
dirs = [SondeLineaireJetons(f"p{k}", 15, "max", rng.standard_normal(4096), 0.1, None, "plancher") for k in range(200)]
t = time.time()
for s in dirs:
    score_action(s, A, 0, 400)
dt = (time.time() - t) / 200
W = np.stack([s.w for s in dirs] * 12, axis=1)[:, :2403]
t = time.time(); E = (np.abs(A) @ np.abs(W)).max(axis=0); M = (A @ W).mean(axis=0); dt2 = time.time() - t
print(f"score_action par direction (400 jetons) : {dt*1e3:.3f} ms ; par action, 2 403 directions : {dt*2403:.2f} s ; "
      f"161 actions : {dt*2403*161/60:.1f} min ; produits matriciels par action : {dt2:.3f} s")
