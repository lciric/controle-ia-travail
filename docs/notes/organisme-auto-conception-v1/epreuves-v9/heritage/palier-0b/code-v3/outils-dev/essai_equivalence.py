"""Outil de développement : moyennes de M1 par bras, couche mécanique (n sources, fréquences mesurées sur d'autres graines)
contre couche statistique, sous la couche « essai ». Aucune sortie versée ; ce n'est pas la garde S8 de l'étape 7.
Arguments : src, dossier neuf, proposeur, dose, n sources mécaniques."""
import os
import sys
import time

import numpy as np

sys.path.insert(0, sys.argv[1])
from controle_ia.heritage_etage_processeur_v1 import equivalence as EQ
from controle_ia.heritage_etage_processeur_v1 import frequences as FR
from controle_ia.heritage_etage_processeur_v1 import graines as GR
from controle_ia.heritage_etage_processeur_v1 import mecanique as MC
from controle_ia.heritage_etage_processeur_v1 import proposeurs as P
from controle_ia.heritage_etage_processeur_v1 import statistique as ST
from controle_ia.heritage_etage_processeur_v1.constantes import REGLAGES_ETAPE_4

g = GR.Graines()
nom, dose, n = sys.argv[3], float(sys.argv[4]), int(sys.argv[5])
prop = P.configuration(nom, **REGLAGES_ETAPE_4)


def couche(famille, n):
    freqs = MC.Frequences()
    m1 = {b: [] for b in "123"}
    for s in range(n):
        ctx = MC.ContexteSource(g, dict(couche="essai", famille=famille, proposeur=nom, dose=dose, source=s), prop, dose, 0.25,
                                os.path.join(sys.argv[2], famille, str(s)))
        out = MC.jouer_source(ctx)
        freqs.fusionner(out["frequences"])
        for b in "123":
            m1[b].append(out["bras"][b]["mesure"]["M1"])
    return freqs, m1


t = time.time()
freqs, _ = couche("eq-frequences", n)
f = FR.frequences_gelees(freqs.comptes())
print("fréquences", round(time.time() - t, 1), "s", f)
t = time.time()
_, m1 = couche("eq-reprise", n)
print("reprise", round(time.time() - t, 1), "s", {b: float(np.mean(v)) for b, v in m1.items()})
S = 20000
res = ST.simuler({b: g.g(couche="essai", famille="eq-st", bras=b, role="echantillonnage") for b in "123"},
                 g.g(couche="essai", famille="eq-st", role="monde"), g.g(couche="essai", famille="eq-st", role="source"),
                 prop, dose, 0.25, f, S)
rng = g.g(couche="essai", famille="eq-st", role="intervalle")
for b in "123":
    v = res["bras"][b]["M1"]
    print(b, "statistique", round(float(v.mean()), 3), "mécanique", round(float(np.mean(m1[b])), 3),
          "intervalle", [round(x, 3) for x in EQ.intervalle_de_prediction(v, n, rng)])
