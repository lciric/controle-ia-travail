"""Grille de la clause de repli pour C-P3c, trois lectures jointes (programme 2). Une case par appel.

C-P3c n'emploie aucun reechantillonnage (valeur p exacte seulement) : aucun tirage par grappes n'est fait ici, ce qui
permet un grand nombre d'essais. Les G-barre nets des familles 1 et 4 viennent du meme modele de TC.1 que la grille de
C-P3a et C-P3b (grille_commun_v1.trois_lectures, B = 0) ; les deux gains d'ecart bruts viennent du modele
`gains_ecart` de grille_commun_v1.py (hypotheses G1 a G5), sur les memes contenus H et S que TC.1.

Bras joues dans les memes essais (memes corpus, memes lectures de TC.1) :
  « bruit »      : les deux gains d'ecart sont six tirages N(0, 1) independants (aucun lien entre evaluateurs ni entre
                   juges) : cas ideal ou la loi exacte du W vaut pour ces deux evaluateurs ; sert de cas sain ;
  « insertion »  : variante « insertion » de G4, kP = 3 (decision D-2, trois niveaux) et kP = 1 ;
  « contenu »    : variante « contenu » de G4, kP = 3 et kP = 1 ; non definie (taux « null ») si deux juges au moins
                   ont s0 = 0 et le meme gain ;
  « insertion_S_separe » (diagnostic, hors du texte) : comme « insertion », kP = 3, mais le gain sous l'usurpation est
                   calcule sur une lecture independante des cellules S et H (memes lectures vraies, erreurs e0
                   retirees) : mesure la part du taux due au partage de S et de D0 entre les deux gains d'ecart.
Gain du plaidoyer et de l'usurpation sous le nul : le texte ne lie pas ces gains au g de la grille ; deux lectures :
  « lie »  : gp_j = gu_j = g_j (le g de la case, 0 sans attaque) ;
  « fort » : gp_j = gu_j = 0,30 pour les trois juges, quel que soit g.
Pour les scenarios d'effet (P3, P6) : « lie » = memes gains ordonnes que TC.1 ; « fort » remplace par « inverse »
(gp_j = gu_j = gains de TC.1 dans l'ordre inverse des juges : l'invariance a l'attaquant est fausse).

Usage : python3 -B grille_c_v1.py MODELE ATTAQUE k T R PASSE SORTIE.json
"""
import json
import sys
import time

import numpy as np

from grille_commun_v1 import (EFFETS, LECTURES, appariement, corpus_A, etablie_c, ex_aequo, gains_ecart, gains_vrais,
                              generateur, mc, scenario, seuil_clause, trois_lectures, versions)

PROGRAMME = 2
BRAS = ["bruit", "insertion_kP3_lie", "insertion_kP1_lie", "contenu_kP3_lie", "contenu_kP1_lie",
        "insertion_kP3_fort", "contenu_kP3_fort", "insertion_S_separe_kP3_lie"]


def main():
    modele, attaque, k, T, R, passe, sortie = (sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4]),
                                               int(sys.argv[5]), int(sys.argv[6]), sys.argv[7])
    rng, graine = generateur(PROGRAMME, modele, attaque, k, T, passe)
    juges, g_juges, doc = scenario(modele, attaque)
    pairs = appariement([1, 8, 16] if k == 3 else [1, 4, 8, 12, 16])
    gains = gains_vrais(g_juges, k)
    g_lie = np.array(g_juges, float)
    effet = modele in EFFETS
    g_fort = g_lie[::-1].copy() if effet else np.full(3, 0.30)
    nb_s0_nul = sum(1 for (s0, sig, kap) in juges if s0 == 0)
    contenu_defini = not (nb_s0_nul >= 2 and not effet)
    acc = {(b, r): 0 for b in BRAS for r in LECTURES + ("conj2", "conj3")}
    n_ex = 0
    t0 = time.time()
    for _ in range(R):
        cA = corpus_A(rng, T)
        oA, v0s = trois_lectures(rng, cA, juges, gains, 1.0, pairs, 0, familles=(0, 3))
        ec = {"bruit": rng.normal(0, 1, (2, 3))}
        for var in ("insertion", "contenu"):
            for kP in (3, 1):
                ec[f"{var}_kP{kP}_lie"] = gains_ecart(rng, cA, juges, v0s, g_lie, g_lie, kP, var)
            ec[f"{var}_kP3_fort"] = gains_ecart(rng, cA, juges, v0s, g_fort, g_fort, 3, var)
        # diagnostic : cellules S et H relues a part pour l'usurpation (erreurs e0 neuves, memes lectures vraies)
        v0_bis = [cA["vrai"] + (rng.normal(0, s0, len(cA["vrai"])) if s0 > 0 else 0.0) for (s0, sig, kap) in juges]
        sep = gains_ecart(rng, cA, juges, v0_bis, g_lie, g_lie, 3, "insertion")
        ec["insertion_S_separe_kP3_lie"] = np.vstack([ec["insertion_kP3_lie"][0], sep[1]])
        for b in BRAS:
            if b.startswith("contenu") and not contenu_defini:
                continue
            if ex_aequo(ec[b]):
                n_ex += 1
            v = {r: etablie_c(oA[r]["G"], ec[b]) for r in LECTURES}
            v["conj2"] = v["cal"] and v["brut"]
            v["conj3"] = v["conj2"] and v["rr"]
            for r in v:
                acc[(b, r)] += bool(v[r])
    seuil = seuil_clause(R)
    taux, err = {}, {}
    for b in BRAS:
        defini = contenu_defini or not b.startswith("contenu")
        for r in LECTURES + ("conj2", "conj3"):
            p = acc[(b, r)] / R
            taux[f"{b}|{r}"] = p if defini else None
            err[f"{b}|{r}"] = mc(p, R) if defini else None
    res = dict(programme="grille_c_v1.py", modele=modele, attaque=attaque, k=k, T=T, R=R, passe=passe,
               description=doc, juges=[list(j) for j in juges], g=g_juges, g_fort_ou_inverse=list(map(float, g_fort)),
               graine=graine, versions=versions(), seuil_clause=seuil, duree_s=round(time.time() - t0, 1),
               contenu_defini=contenu_defini, essais_avec_ex_aequo=n_ex, taux=taux, erreur_mc=err)
    with open(sortie, "w", encoding="utf-8") as f:
        json.dump(res, f, ensure_ascii=False, indent=1, sort_keys=True)
        f.write("\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
