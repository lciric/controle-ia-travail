"""Contre-lecteur : bruit de l'exactitude equilibree du plus proche centre (forme, 65 traits) sous le nul, aux tailles de l'audit
des doses par paires a pleine taille (50 suites par dose, 4 mondes cibles ou finaux par suite = 200 mondes par dose ; paire de
doses = 200 contre 200). Traits gaussiens independants (nul), graines locales sans rapport avec le dispositif. Aucun tirage
decisif, aucun appel au code de calcul des couches ; seule la fonction d'exactitude de l'audit est reprise."""
import sys

import numpy as np

sys.path.insert(0, sys.argv[1])
from controle_ia.heritage_etage_processeur_v1 import audit as AU

rng = np.random.default_rng(424242)
reps = int(sys.argv[2])
for n_par_classe in (200, 400):
    acc = []
    for _ in range(reps):
        X = rng.normal(size=(2 * n_par_classe, 65))
        y = np.array([0] * n_par_classe + [1] * n_par_classe)
        acc.append(AU.exactitude_equilibree(X, y, rng))
    a = np.array(acc)
    print("n par classe", n_par_classe, "moyenne", round(float(a.mean()), 4), "ecart-type", round(float(a.std()), 4),
          "part au-dessus de 0,55", round(float(np.mean(a > 0.55)), 4))
