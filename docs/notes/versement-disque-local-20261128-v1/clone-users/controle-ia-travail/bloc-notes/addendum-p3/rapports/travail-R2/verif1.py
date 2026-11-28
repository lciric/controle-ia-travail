"""Vérifications du contre-lecteur R2 (lecture seule du dépôt)."""
import numpy as np
from controle_ia.environnements.propositions import lire_action, heures_declarees
from controle_ia.premier_test_ia.conditions import cout_groupes_joints, _CLE_BRUTE
from controle_ia.premier_test_ia.statistiques import aire_stratifiee, strates_quantiles, etiquettes_gonflement, cout_de_tache

print("== 1. lire_action : puces et occurrences répétées")
t1 = "ACTION: ADD\nTITLE: t\nPROPOSAL: p\nCONTROLS: c\n- COST: 30 hours\nPREDICTION: x"
a = lire_action(t1); print("puce '- COST:' ->", a.valide, a.champs.get("COST"), a.motif)
t2 = "ACTION: ADD\nTITLE: t\nPROPOSAL: p\nCOST: 10 hours\nCONTROLS: c\nCOST: 99 hours\nPREDICTION: x"
a = lire_action(t2); print("deux COST ->", a.champs.get("COST"))
t3 = "ACTION: ADD\nTITLE: t\nPROPOSAL: p\nCONTROLS: c\n2. COST: 30\nPREDICTION: x"
a = lire_action(t3); print("numéro '2. COST:' ->", a.valide, a.champs.get("COST"), a.motif)
t4 = "ACTION: ADD\nTITLE: t\nPROPOSAL: p\nCONTROLS: c\n**Cost** breakdown: 40 hours\nCOST: 30\nPREDICTION: x"
a = lire_action(t4); print("'**Cost** breakdown:' ->", a.champs.get("COST"))
print("  _CLE_BRUTE trouve :", [(m['cle'], m.start()) for m in _CLE_BRUTE.finditer(t4)])
print("== coûts : '1 000', '1 000', '1 000.5', '1,000'")
for s in ["1 000 hours", "1 000 hours", "1 000.5 hours", "1,000 hours", "3 500-hour blocks"]:
    print(repr(s), heures_declarees(s), cout_groupes_joints(s))

print("== 2. aire_stratifiee, tâche pour tranche, tâche tirée deux fois")
s = np.array([0.9, 0.1, 0.8, 0.7, 0.2, 0.3, 0.6, 0.4])
y = np.array([1, 0, 1, 1, 0, 0, 1, 0])
st = np.array(["A", "A", "B", "B", "B", "B", "B", "B"])
print("observé  :", aire_stratifiee(s, y, st))
i = np.r_[0, 1, 0, 1, 2, 3, 4, 5, 6, 7]       # tâche A tirée deux fois, B une fois (même étiquette de tranche)
print("A doublée, même tranche :", aire_stratifiee(s[i], y[i], st[i]))
st2 = np.array(["A#0", "A#0", "A#1", "A#1", "B#0", "B#0", "B#0", "B#0", "B#0", "B#0"])
print("A doublée, tranche par copie :", aire_stratifiee(s[i], y[i], st2))
# poids attendu : A une fois (1 paire) + B (3*3=9) ; A deux fois en tranches séparées -> 2 paires ; même tranche -> 4 paires
print("== 3. tranches aux quintiles avec ex aequo")
v = np.log10(np.array([100]*30 + [200]*30 + [500]*10 + [1000]*5 + [50]*5, dtype=float))
print("tranches distinctes :", np.unique(strates_quantiles(v, 5)).size)
print("== 4. référence géométrique = cout_de_tache")
c = [100.0, 200.0, 400.0]
print(10 ** cout_de_tache(c)["valeur"], np.median(c))
