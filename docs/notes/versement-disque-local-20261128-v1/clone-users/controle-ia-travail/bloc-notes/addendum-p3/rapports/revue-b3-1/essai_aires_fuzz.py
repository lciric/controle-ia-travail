"""Essai : aire vectorisée par rangs contre `aire_sous_courbe` et `aire_stratifiee` (code gelé), sur 3 000 cas
aléatoires (ex aequo massifs, tranches à une seule classe, tranches d'une action, tailles 2 à 60)."""
import numpy as np

import complements_p3_v1 as cp
from controle_ia.premier_test_ia.statistiques import aire_stratifiee
from controle_ia.sondes.evaluation import aire_sous_courbe

g = np.random.default_rng(1)
pire, cas, none_ok = 0.0, 0, 0
for _ in range(3000):
    n = int(g.integers(2, 61))
    y = g.integers(0, 2, size=n)
    X = np.round(g.normal(size=(4, n)), int(g.integers(0, 3)))     # ex aequo fréquents
    st = g.integers(0, int(g.integers(1, 8)), size=n)
    a = cp.aires_par_rangs(X, y)
    if y.sum() in (0, n):
        assert a is None
        none_ok += 1
        continue
    ref = np.array([aire_sous_courbe(x, y) for x in X])
    pire = max(pire, float(np.max(np.abs(a - ref))))
    s = cp.aires_par_rangs(X, y, st)
    refs = [aire_stratifiee(x, y, st) for x in X]
    if refs[0] is None:
        assert s is None
    else:
        pire = max(pire, float(np.max(np.abs(s - np.array(refs)))))
    cas += 1
print(f"cas comparés {cas}, cas sans une classe {none_ok}, plus grand écart {pire:.3e}")
