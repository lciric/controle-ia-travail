"""Essai ciblé (demande 6 a) : l'ajustement des deux moniteurs appris rend-il « non calculable » sous séparation
parfaite des deux classes ? Données construites à la main, aucun épisode, aucun moniteur réel. Sortie : un motif ou
« calculable » par cas, rien d'autre (aucun coefficient)."""
import sys

import numpy as np

from controle_ia.organismes_discrets.bras_a_v2_habilite import autres_moniteurs_v8 as am

RACINE = sys.argv[1]
v3, _ = am.charger_piece_source(RACINE)
rng = np.random.default_rng(20261120)
n = 1280                                  # actions d'apprentissage d'un pli à une dose (8 tâches x 8 x 10 x 2)
y = np.array([0, 1] * (n // 2), dtype=np.int64)

cas = {}
# lexical : présence binaire, 1 000 colonnes ; un mot présent exactement dans la classe 1 (séparation parfaite)
Xl = (rng.random((n, 1000)) < 0.05).astype(np.float64)
Xl[:, 0] = y
cas["lexical, un mot séparateur"] = (Xl, v3.REGLAGES_B)
# lexical : séparation par de nombreux mots (chaque classe a ses mots propres)
Xl2 = np.zeros((n, 1000))
Xl2[y == 1, :500] = (rng.random(((y == 1).sum(), 500)) < 0.2)
Xl2[y == 0, 500:] = (rng.random(((y == 0).sum(), 500)) < 0.2)
Xl2[y == 1, 0] = 1.0
Xl2[y == 0, 500] = 1.0
cas["lexical, classes à mots disjoints"] = (Xl2, v3.REGLAGES_B)
# surface : 21 colonnes, une colonne séparatrice à grande marge
Xs = rng.normal(size=(n, 21))
Xs[:, 0] = np.where(y == 1, 100.0, -100.0) + rng.normal(size=n)
cas["surface, une colonne séparatrice"] = (Xs, v3.REGLAGES_A)
# surface : séparation par une combinaison de colonnes
Xs2 = rng.normal(size=(n, 21))
Xs2[:, :3] += np.where(y[:, None] == 1, 5.0, -5.0)
cas["surface, séparation par plusieurs colonnes"] = (Xs2, v3.REGLAGES_A)

for nom, (X, reglages) in cas.items():
    noms = tuple(f"c{j}" for j in range(X.shape[1]))
    m = v3.ajuster(X, y, noms, reglages)
    print(f"{nom} : {'calculable' if m['calculable'] else 'NON CALCULABLE : ' + str(m['motif'])} ; "
          f"convergé : {m['convergence']['converge']}")
