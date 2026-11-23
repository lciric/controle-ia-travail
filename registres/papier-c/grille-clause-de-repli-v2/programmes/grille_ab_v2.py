"""VERSION v2 (2026-11-22, agent de la grille, rapport v2). Copie de grille_ab_v1.py
(7df353b10eb88e2be7e0a25ae37e00bf142e882a9001415ca5bb779a70b84a94). Differences, aucune ne touche au flux de hasard
ni a un taux :
  (1) importe grille_commun_v2 (graine propre aux cases a T = 30) ; champ « programme » = grille_ab_v2.py ;
  (2) compteurs de controle ecrits dans la sortie (Plan, section 8, precisions 5 et 8) : essais ou une composante G-barre
      observee ou tiree est non finie ; essais ou deux juges d'une meme famille ont un G-barre observe exactement egal,
      ou un ecart G* - G exactement egal dans un tirage. S'ils valent 0, la lecture des programmes (rangs ordinaux,
      tau-a, aucun traitement des valeurs non finies) coincide avec celle du texte (rangs moyens, tau-b, tirage non
      fini au numerateur).

Grille de la clause de repli pour C-P3a et C-P3b (programme 1). Une case par appel.

Case = modele d'erreur des trois juges x attaque x k x T (voir grille_commun_v1.py). Pour chaque essai : corpus A
(T taches) et corpus B (30 items), trois juges, cinq familles, k rangs (indices 1, 8, 16 ou 1, 4, 8, 12, 16 du vivier
pour la regle des temoins), vrai reechantillonnage par grappes (B tirages, memes comptes pour les trois juges et les
cinq familles d'un corpus, tirages independants entre corpus), trois lectures.

Sorties par case : taux de « etablie » par lecture (cal, brut, rr), aux deux premieres jointes (conj2) et aux trois
jointes (conj3, la regle du texte), pour C-P3a et C-P3b.
Deux lectures du sort des tirages degeneres (le texte ne dit pas comment une composante « non identifiable », point 11,
lignes 758 a 759, entre dans une statistique de rang) :
  (i)  on n'en tient pas compte (ce que font les programmes de l'archive) : taux « conj3 » ;
  (ii) une statistique dont une composante G-barre a plus de 1 % de tirages degeneres dans une lecture n'est pas lue,
       donc jamais « etablie » : taux « conj3_ii ». (ii) <= (i) par construction ; (i) est la lecture qui charge la clause.

Regle de la seconde passe, ecrite avant tout resultat : toute case dont un taux conj3 (C-P3a ou C-P3b) de la premiere
passe (passe 0, R = 1000) n'est pas sous le seuil de la clause d'au moins deux erreurs de Monte-Carlo est rejouee sur
une graine neuve (passe 1) avec R = 4000 ; les deux passes sont rapportees, sans mise en commun.

Usage : python3 -B grille_ab_v1.py MODELE ATTAQUE k T R B PASSE SORTIE.json
"""
import json
import sys
import time

import numpy as np

from grille_commun_v2 import (appariement, corpus_A, corpus_B, etablie_a, etablie_b, gains_vrais, generateur, mc,
                              scenario, seuil_clause, trois_lectures, versions, LECTURES)

PROGRAMME = 1


def controles(o):
    """(non fini, egalite) pour les sorties d'un corpus, toutes lectures : bool, bool. Aucun tirage aleatoire."""
    nf, eg = False, False
    for r in LECTURES:
        G, Gb = o[r]["G"], o[r]["Gb"]
        nf = nf or (not np.isfinite(G).all()) or (not np.isfinite(Gb).all())
        sG = np.sort(G, -1)
        sD = np.sort(Gb - G[None], -1)
        eg = eg or bool((np.diff(sG, axis=-1) == 0).any()) or bool((np.diff(sD, axis=-1) == 0).any())
    return nf, eg


def main():
    modele, attaque, k, T, R, B, passe, sortie = (sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4]),
                                                  int(sys.argv[5]), int(sys.argv[6]), int(sys.argv[7]), sys.argv[8])
    rng, graine = generateur(PROGRAMME, modele, attaque, k, T, passe)
    juges, g_juges, doc = scenario(modele, attaque)
    pairs = appariement([1, 8, 16] if k == 3 else [1, 4, 8, 12, 16])
    gains = gains_vrais(g_juges, k)
    cles = [(r, s) for r in LECTURES + ("conj2", "conj3", "conj3_ii") for s in ("a", "b")]
    acc = {c: 0 for c in cles}
    acc_detail = {(r, x): 0 for r in LECTURES for x in ("a_exact", "a_centre")}
    deg_max = {"A": 0.0, "B": 0.0}
    n_deg = {"a": 0, "b": 0}
    n_ctl = {"non_fini_A": 0, "non_fini_B": 0, "egalite_A": 0, "egalite_B": 0}
    t0 = time.time()
    for _ in range(R):
        oA, _v = trois_lectures(rng, corpus_A(rng, T), juges, gains, 1.0, pairs, B)
        oB, _v = trois_lectures(rng, corpus_B(rng), juges, gains, 1.0, pairs, B)
        for nom, o in (("A", oA), ("B", oB)):
            nf, eg = controles(o)
            n_ctl[f"non_fini_{nom}"] += nf
            n_ctl[f"egalite_{nom}"] += eg
        v = {}
        for r in LECTURES:
            ea, pe, pc = etablie_a(oA[r]["G"], oA[r]["Gb"])
            eb = etablie_b(oA[r]["G"], oA[r]["Gb"], oB[r]["G"], oB[r]["Gb"])
            v[r] = dict(a=ea, b=eb)
            acc_detail[(r, "a_exact")] += pe
            acc_detail[(r, "a_centre")] += pc
        dA = max(float(oA[r]["deg"].max()) for r in LECTURES)
        dB = max(float(oB[r]["deg"].max()) for r in LECTURES)
        deg_max["A"] = max(deg_max["A"], dA)
        deg_max["B"] = max(deg_max["B"], dB)
        lisible = dict(a=dA <= 0.01, b=(dA <= 0.01) and (dB <= 0.01))
        n_deg["a"] += not lisible["a"]
        n_deg["b"] += not lisible["b"]
        v["conj2"] = {s: v["cal"][s] and v["brut"][s] for s in ("a", "b")}
        v["conj3"] = {s: v["conj2"][s] and v["rr"][s] for s in ("a", "b")}
        v["conj3_ii"] = {s: v["conj3"][s] and lisible[s] for s in ("a", "b")}
        for (r, s) in cles:
            acc[(r, s)] += bool(v[r][s])
    seuil = seuil_clause(R)
    res = dict(programme="grille_ab_v2.py", essais_controles=n_ctl, modele=modele, attaque=attaque, k=k, T=T, R=R, B=B, passe=passe,
               description=doc, juges=[list(j) for j in juges], g=g_juges, graine=graine, versions=versions(),
               seuil_clause=seuil, duree_s=round(time.time() - t0, 1),
               taux={f"{r}_{s}": acc[(r, s)] / R for (r, s) in cles},
               erreur_mc={f"{r}_{s}": mc(acc[(r, s)] / R, R) for (r, s) in cles},
               detail_a={f"{r}_{x}": acc_detail[(r, x)] / R for (r, x) in acc_detail},
               part_essais_non_lisibles_ii={s: n_deg[s] / R for s in n_deg},
               part_max_tirages_degeneres=deg_max)
    with open(sortie, "w", encoding="utf-8") as f:
        json.dump(res, f, ensure_ascii=False, indent=1, sort_keys=True)
        f.write("\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
