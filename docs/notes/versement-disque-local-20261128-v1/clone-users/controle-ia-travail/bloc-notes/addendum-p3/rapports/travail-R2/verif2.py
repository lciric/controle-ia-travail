import numpy as np
from controle_ia.premier_test_ia.statistiques import aire_stratifiee
# tâche A : aire 0 (1 positif, 1 négatif inversés) ; tâche B : aire 1 (2 positifs, 2 négatifs)
s = np.array([0.1, 0.9, 0.8, 0.7, 0.2, 0.3]); y = np.array([1, 0, 1, 1, 0, 0])
st = np.array(["A", "A", "B", "B", "B", "B"])
print("observé (A:1 paire, B:4 paires) :", aire_stratifiee(s, y, st))
i = np.r_[0, 1, 0, 1, 2, 3, 4, 5]   # tirage : A deux fois, B une fois
print("A tirée deux fois, même tranche (4 paires A, dont 2 croisées) :", aire_stratifiee(s[i], y[i], st[i]))
st2 = np.array(["A0", "A0", "A1", "A1", "B0", "B0", "B0", "B0"])
print("A tirée deux fois, une tranche par copie (2 paires A) :", aire_stratifiee(s[i], y[i], st2))
