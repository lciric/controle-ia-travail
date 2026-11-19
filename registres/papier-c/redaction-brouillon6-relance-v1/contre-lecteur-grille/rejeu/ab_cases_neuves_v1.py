"""Contre-lecture de la grille (contre-lecteur). Cases de la grille non jouees par le rapport, pour C-P3a et C-P3b :
compression seule a d'autres ecarts types de l'erreur d'insertion (le texte ne le fixe pas, ambiguite A3) et
compression homogene intermediaire. Ajoute des modeles au dictionnaire MODELES du rapport, puis appelle grille_ab_v1.main
sans autre changement. Les nouveaux modeles prennent les rangs 8 a 11 (P3 et P6 passent a 12 et 13) ; joues seulement en g00, k = 3, T = 45 : aucune cle commune avec les cases P3 et P6 du rapport (g10, k = 5, T = 60) ; les
rangs des modeles du rapport ne changent pas pour E30 a M616 (P3 et P6 sont decales, non employes ici).
Usage : python3 -B ab_cases_neuves_v1.py MODELE ATTAQUE k T R B PASSE SORTIE.json
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "programmes"))
import grille_commun_v1 as G  # noqa: E402

NEUFS = {
    "K16s20": dict(juges=[(0.0, 0.2, 0.16)] * 3, doc="compression seule 0,16, erreur d'insertion 0,2"),
    "K16s60": dict(juges=[(0.0, 0.6, 0.16)] * 3, doc="compression seule 0,16, erreur d'insertion 0,6"),
    "K10": dict(juges=[(0.0, 0.4, 0.10)] * 3, doc="compression seule homogene 0,10"),
    "KHs60": dict(juges=[(0.0, 0.6, 0.04), (0.0, 0.6, 0.10), (0.0, 0.6, 0.16)],
                  doc="compression heterogene, erreur d'insertion 0,6"),
}
for nom, d in NEUFS.items():
    G.MODELES[nom] = d
# EFFETS doit rester apres MODELES pour identifiant_case : on le reconstruit dans le meme ordre
_eff = dict(G.EFFETS)
G.EFFETS.clear()
G.EFFETS.update(_eff)

import grille_ab_v1 as A  # noqa: E402

if __name__ == "__main__":
    sys.exit(A.main())
