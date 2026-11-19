"""Contre-lecture de la grille (contre-lecteur). C-P3c sous les deux lectures du sort des tirages degeneres (ambiguite
A6 du rapport) : (i) on n'en tient pas compte ; (ii) une statistique dont une composante G-barre (familles 1 et 4, trois
lectures) a plus de 1 % de tirages degeneres n'est pas lue, donc jamais « etablie ». Reprend les fonctions du rapport
(grille_commun_v1.py, empreinte 6458120e...), avec un vrai reechantillonnage par grappes (B tirages) pour compter les
tirages degeneres, ce que grille_c_v1.py ne fait pas. Graine : SeedSequence(20261119, spawn_key = (7, case, 0)),
programme 7 propre a cette contre-lecture (aucune collision avec les programmes 1 et 2 du rapport).
Usage : python3 -B cp3c_lecture_ii_v1.py MODELE ATTAQUE k T R B SORTIE.json
"""
import json
import os
import sys
import time

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "programmes"))
import numpy as np  # noqa: E402

import grille_commun_v1 as G  # noqa: E402


def main():
    modele, attaque, k, T, R, B, sortie = (sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4]),
                                           int(sys.argv[5]), int(sys.argv[6]), sys.argv[7])
    cle = (7, G.identifiant_case(modele, attaque, k, T), 0)
    rng = np.random.default_rng(np.random.SeedSequence(G.RACINE, spawn_key=cle))
    juges, gj, doc = G.scenario(modele, attaque)
    pairs = G.appariement([1, 8, 16] if k == 3 else [1, 4, 8, 12, 16])
    gains = G.gains_vrais(gj, k)
    g_lie = np.array(gj, float)
    nb_s0_nul = sum(1 for (s0, sig, kap) in juges if s0 == 0)
    variantes = ["insertion"] + (["contenu"] if nb_s0_nul < 2 else [])
    acc = {(v, l): 0 for v in variantes for l in ("i", "ii")}
    n_lisible = 0
    t0 = time.time()
    for _ in range(R):
        cA = G.corpus_A(rng, T)
        oA, v0s = G.trois_lectures(rng, cA, juges, gains, 1.0, pairs, B, familles=(0, 3))
        deg = max(float(oA[r]["deg"][[0, 3], :].max()) for r in G.LECTURES)
        lisible = deg <= 0.01
        n_lisible += lisible
        for v in variantes:
            ec = G.gains_ecart(rng, cA, juges, v0s, g_lie, g_lie, 3, v)
            e = all(G.etablie_c(oA[r]["G"], ec) for r in G.LECTURES)
            acc[(v, "i")] += e
            acc[(v, "ii")] += e and lisible
    res = dict(modele=modele, attaque=attaque, k=k, T=T, R=R, B=B, graine=list(cle), doc=doc,
               seuil=G.seuil_clause(R), part_lisible=n_lisible / R, duree_s=round(time.time() - t0, 1),
               taux={f"{v}|{l}": acc[(v, l)] / R for (v, l) in acc},
               erreur={f"{v}|{l}": G.mc(acc[(v, l)] / R, R) for (v, l) in acc})
    json.dump(res, open(sortie, "w"), indent=1, ensure_ascii=False)


if __name__ == "__main__":
    main()
