"""Outil de développement : moyennes de M1 par bras, couche mécanique (n sources) contre couche statistique (S sources), sous
la couche « essai ». Aucune sortie versée ; ce n'est pas la garde S8 (celle-ci est dans `equivalence.py`)."""
import sys
import tempfile
import time

import numpy as np

sys.path.insert(0, sys.argv[1])
from controle_ia.heritage_etage_processeur_v1 import graines as GR
from controle_ia.heritage_etage_processeur_v1 import mecanique as MC
from controle_ia.heritage_etage_processeur_v1 import proposeurs as P
from controle_ia.heritage_etage_processeur_v1 import statistique as ST

g = GR.Graines()
racine = tempfile.mkdtemp(dir=sys.argv[2])
nom, K, dose, n = sys.argv[3], float(sys.argv[4]), float(sys.argv[5]), int(sys.argv[6])
prop = P.configuration(nom, K=K)
t = time.time()
freqs = MC.Frequences()
m1 = {b: [] for b in "123"}
for s in range(n):
    ctx = MC.ContexteSource(g, dict(couche="essai", famille="eq", proposeur=nom, source=s), prop, dose, 0.25, f"{racine}/{s}")
    out = MC.jouer_source(ctx)
    freqs.fusionner(out["frequences"])
    for b in "123":
        m1[b].append(out["bras"][b]["mesure"]["M1"])
f = MC.frequences_gelees(freqs.comptes())
print("mécanique", round(time.time() - t, 1), "s", {b: round(float(np.mean(v)), 3) for b, v in m1.items()}, f)
t = time.time()
S = 4000
res = ST.simuler({b: g.g(couche="essai", famille="eq-st", bras=b, role="echantillonnage") for b in "123"},
                 g.g(couche="essai", famille="eq-st", role="monde"), g.g(couche="essai", famille="eq-st", role="source"),
                 prop, dose, 0.25, f, S)
print("statistique", round(time.time() - t, 2), "s", {b: (round(float(v["M1"].mean()), 3), round(float(v["M1"].std() / np.sqrt(n)), 3))
                                                      for b, v in res["bras"].items()})
