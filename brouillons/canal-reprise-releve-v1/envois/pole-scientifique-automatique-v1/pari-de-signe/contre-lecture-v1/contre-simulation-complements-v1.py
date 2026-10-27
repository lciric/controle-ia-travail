"""Compléments à contre-simulation-pari-signe-v1.py (mêmes fonctions, chargées par chemin) : héritage relu sur k
générations ; sélection sur les scores du comparateur à 100 et 150 tâches ; jumeaux en loi à 500 tâches de calibrage."""
import importlib.util
import json
import math
import sys

import numpy as np

chemin = sys.argv[1]
spec = importlib.util.spec_from_file_location("cs", chemin)
cs = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cs)

racine = np.random.SeedSequence(16180339887)
g1, g2, g3 = (np.random.default_rng(s) for s in racine.spawn(3))
out = {"entropie_SeedSequence": 16180339887}

# 1. Héritage : même banque relue k fois (ordres secrets différents) contre k banques disjointes, nul 0,5 contre 0,5
R, n = 4000, 100
v = cs.parts(g1, R, n, 10, 0.5, 0.5)
res = {}
for forme in ("parts", "melange"):
    def lw(x):
        return cs.logw([x], [1.0]) if forme == "parts" else cs.logw([x, np.sign(x)], [0.5, 0.5])
    lectures_meme = [cs.e_arretee(lw(v[np.arange(R)[:, None], np.array([g1.permutation(n) for _ in range(R)])]), cs.S20)
                     for _ in range(10)]
    lectures_disj = [cs.e_arretee(lw(cs.parts(g1, R, n, 10, 0.5, 0.5)), cs.S20) for _ in range(10)]
    res[forme] = {f"k_{k}": {"meme_banque": float((np.sum(lectures_meme[:k], 0) >= cs.S20 - cs.TOL).mean()),
                             "banques_disjointes": float((np.sum(lectures_disj[:k], 0) >= cs.S20 - cs.TOL).mean())}
                  for k in (1, 2, 3, 5, 10)}
out["heritage_k_lectures_P(produit>=20)_4000_rep"] = res

# 2. Sélection sur les scores du comparateur (jumeaux en loi), forme parts seule, plus de tâches
out["selection_comparateur_jumeaux"] = {n_t: cs.section_L(g2, 1000, n=n_t) for n_t in (100, 150)}

# 3. Jumeaux en loi : 500 tâches de calibrage
out["jumeaux_cal_500"] = {f"icc_{icc}": cs.jumeaux(g3, 500, 500, 100, 150, 0.05, icc=icc) for icc in (0.0, 0.3)}
print(json.dumps(out, ensure_ascii=False, indent=1))
