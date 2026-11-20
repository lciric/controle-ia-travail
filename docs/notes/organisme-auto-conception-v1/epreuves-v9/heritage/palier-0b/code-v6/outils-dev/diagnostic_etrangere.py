"""Outil de développement : pourquoi la construction face à la source étrangère retire ses suites. Un monde cible de la source 0,
construit contre la source 1 ; affiche les manques de l'audit (graines « essai » ; aucune sortie versée)."""
import collections
import sys

sys.path.insert(0, sys.argv[1])
from controle_ia.heritage_etage_processeur_v1 import audit as AU
from controle_ia.heritage_etage_processeur_v1 import graines as GR
from controle_ia.heritage_etage_processeur_v1 import mondes as MO

g = GR.Graines()
bases = [dict(couche="essai", famille="etrangere", dose=0.5, source=k) for k in range(2)]
sources = [MO.generer_source(g, b, 0.5)[0] for b in bases]
paires = MO.tirer_paires(g.g(**bases[0], monde="paires", role="paires"), 0.5)
for essai_cible in range(3):
    m, essai, manques = MO.generer_cible(g, dict(bases[0], tour=essai_cible), sources[0], "cible-1", paires[0], 0.5,
                                         etrangere=sources[1])
    print("monde", "rendu" if m is not None else "None (suite à retirer)", "essai", essai, "manques", len(manques))
    genres = collections.Counter((x[0], "dependante") for x in manques)
    print(genres)
    for x in sorted(manques, key=lambda x: x[3])[:6]:
        print(x)
