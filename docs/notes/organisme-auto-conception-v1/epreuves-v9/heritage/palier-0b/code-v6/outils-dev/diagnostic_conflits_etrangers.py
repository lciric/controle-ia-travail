"""Outil de développement (graines « essai », aucune sortie versée) : fréquence des conflits entre les compositions d'une source
(candidates aux lois dépendantes, ordre des rangs) et les candidates de la source étrangère (lois vraies et compositions), au
seuil de 0,25 nat, sur les instances de l'oracle d'un monde ; deux lectures : compositions étrangères dans l'ordre des rangs seul,
ou dans les deux ordres. Rend, par tour, le nombre de compositions propres en conflit, et la part des tours où un tirage de
24 paires sur 28 (dose 0,5) évite tout conflit (probabilité exacte, combinatoire)."""
import itertools
import math
import sys

sys.path.insert(0, sys.argv[1])
from controle_ia.heritage_etage_processeur_v1 import audit as AU
from controle_ia.heritage_etage_processeur_v1 import graines as GR
from controle_ia.heritage_etage_processeur_v1 import lois as L
from controle_ia.heritage_etage_processeur_v1 import mondes as MO

g = GR.Graines()
tours = int(sys.argv[2])
famille = sys.argv[3] if len(sys.argv) > 3 else "conflits"
Z, G = L.instances_oracle(g.e(couche="essai", famille="conflits", role="oracle-instances"), 4000)
pr = AU.Probas(Z, G)
etr = MO.generer_source(g, dict(couche="essai", famille=famille, dose=0.5, source=1), 0.5)[0].vraies_par_rang()
for lecture in ("ordre-des-rangs", "deux-ordres"):
    cand = list(etr) + [AU._composer_audit(etr[p], etr[q]) for p in range(8) for q in range(8)
                        if p != q and (lecture == "deux-ordres" or p < q)]
    sans_conflit = []
    nombres = []
    for t in range(tours):
        v = MO.generer_source(g, dict(couche="essai", famille=famille, dose=0.5, source=0, tour=t + 1), 0.5)[0].vraies_par_rang()
        conflits = 0
        for p, q in itertools.combinations(range(8), 2):
            c = AU._composer_audit(v[p], v[q])
            if any(AU.separation(pr(c), pr(x)) < 0.25 for x in cand):
                conflits += 1
        nombres.append(conflits)
        # probabilité que 24 paires tirées sans remise parmi 28 évitent les `conflits` paires en conflit
        sans_conflit.append(math.comb(28 - conflits, 24) / math.comb(28, 24) if conflits <= 4 else 0.0)
    print(lecture, "conflits par tour", nombres, "probabilité moyenne d'un tour sans conflit à la dose 0,5",
          round(sum(sans_conflit) / len(sans_conflit), 4))
