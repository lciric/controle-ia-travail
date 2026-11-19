"""Diagnostic de faisabilité des marges (outil de développement, aucune sortie versée) : distribution de la divergence
(minimum des deux sens) entre lois aléatoires, et part des contraintes manquées, selon la force des softmax."""
import itertools
import random
import sys

import numpy as np

sys.path.insert(0, sys.argv[1])
from controle_ia.heritage_etage_processeur_v1 import comparateur as C
from controle_ia.heritage_etage_processeur_v1 import lois as L

Z, G = L.instances_oracle(12345, 4000)
o = C.Oracle(Z, G)
for force in (1.5, 2.0, 2.5, 3.0, 4.0):
    L.FORCE_SOFTMAX = force
    import controle_ia.heritage_etage_processeur_v1.lois as LL
    rng = np.random.default_rng(7)
    ok_source = 0
    essais = 200
    kl = []
    for e in range(essais):
        def sm(rng=rng, force=force):
            return {"type": "softmax", "poids": np.round(rng.normal(0, force, (3, 2)), 6).tolist(),
                    "biais": np.round(rng.normal(0, 0.3, 3), 6).tolist()}
        vraies = [L.loi_par_sous_population(sm(), sm()) for _ in range(8)]
        fausses = []
        for v in vraies:
            fausses.append(L.loi_par_sous_population(L.sous_loi(v, 0), sm()) if rng.integers(2) == 0
                           else L.loi_par_sous_population(sm(), L.sous_loi(v, 1)))
        lois = vraies + fausses
        manque = False
        for a, b in itertools.combinations(lois, 2):
            d = min(o.divergence(a, b), o.divergence(b, a))
            kl.append(d)
            if d < 0.25:
                manque = True
        for p, q in itertools.combinations(range(8), 2):
            c = L.composer(vraies[p], vraies[q])
            for r in range(8):
                if min(o.divergence(c, vraies[r]), o.divergence(vraies[r], c)) < 0.25:
                    manque = True
        ok_source += not manque
        if e >= 40:
            essais = e + 1
            break
    print("force", force, "sources qui passent", ok_source, "sur", essais, "quantiles divergence", np.round(np.quantile(kl, [0.01, 0.05, 0.5]), 3))
