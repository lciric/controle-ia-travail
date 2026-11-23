#!/usr/bin/env python3
"""Complément 4 : porte au moindre coût (coût par variante, puissance du pari à deux seuils).
Classe B. Lois supposées, aucune donnée du programme. Lancer depuis un dossier vide : python -I <ce fichier>.
Coût : même modèle que le brouillon 6 (48,35 s de génération + 2 x 58,2 s de notation par épisode, 1,1467 USD/h, marge 1,3).
Puissance : une seule comparaison (A contre un comparateur), unités de 10 épisodes sabotés, parts binomiales
indépendantes, richesse mélangée sur Lambda = {0,1 ; 0,3 ; 0,6 ; 0,9}, promotion si la richesse atteint le seuil à
un instant quelconque. Le minimum sur douze comparateurs ne peut que baisser ces puissances. Graine racine 20261123.
"""
import numpy as np

SEC, USD_H, MARGE = 48.35 + 2 * 58.2, 1.1467, 1.3
LAMBDAS = (0.1, 0.3, 0.6, 0.9)

def usd(ep): return ep * SEC / 3600 * USD_H

def puissance(n, pa, pb, seuil, reps, rng):
    ra = rng.binomial(10, pa, (reps, n)) / 10
    rb = rng.binomial(10, pb, (reps, n)) / 10
    v = ra - rb
    w = np.zeros((reps, n))
    for lam in LAMBDAS:
        w += np.exp(np.cumsum(np.log1p(lam * v), axis=1)) / len(LAMBDAS)
    return float((w.max(axis=1) >= seuil).mean())

def main():
    print("Complément 4 — porte au moindre coût ; lois supposées ; aucune donnée du programme\n")
    print("§ 1 Coût (400 tâches sauf mention ; épisodes par tâche = jumeaux + sabotés + témoin/mention + calibrage + témoin apparié)")
    print("variante ; tâches ; épisodes/tâche ; épisodes ; USD central ; x1,3")
    V = [
     ("défaut accordé (brouillon 6)", 400, 10, 60, 12, 150, 0),
     ("garde, 10 exécutions du témoin dans les 2 cellules de la porte, 1 ailleurs", 400, 10, 60, 12, 150, 24),
     ("garde, 1 exécution du témoin par unité, 6 cellules", 400, 10, 60, 12, 150, 6),
     ("contraste minimal : 300 épisodes de calibrage du témoin x 6 cellules + évaluation 10/1", 400, 10, 60, 12, 150, 24 + 4.5),
     ("A. porte seule : 2 modes de la porte x famille sans consigne ; mode coût et famille à consigne retirés ; témoin/mention gardés", 400, 10, 20, 12, 150, 0),
     ("B. = A, calibrage à 10 fois (100/tâche)", 400, 10, 20, 12, 100, 0),
     ("C. = B, 288 tâches", 288, 10, 20, 12, 100, 0),
     ("D. = C, sans témoin ni mention (rapportés seulement ailleurs)", 288, 10, 20, 0, 100, 0),
     ("D + témoin apparié, 1 exécution par unité dans les 2 cellules", 288, 10, 20, 0, 100, 2),
     ("D + témoin apparié, 10 exécutions par unité dans les 2 cellules", 288, 10, 20, 0, 100, 20),
    ]
    for nom, n, tw, sab, tm, cal, ap in V:
        par = tw + sab + tm + cal + ap
        ep = n * par
        c = usd(ep)
        print(f"{nom} ; {n} ; {par:g} ; {ep:g} ; {c:.0f} ; {c*MARGE:.0f}")
    print("\nSensibilité : si la notation par les moniteurs coûtait moitié moins (non sourcé), le coût par épisode passe de",
          f"{SEC:.1f} s à {48.35 + 58.2:.1f} s, soit x{(48.35+58.2)/SEC:.2f}.\n")
    print("§ 2 Puissance du pari (une comparaison), 2000 répétitions par cellule, graine racine 20261123")
    print("unités ; écart (rappels) ; seuil 20 ; seuil 160")
    ss = np.random.SeedSequence(20261123)
    cells = [(n, pa, pb) for pa, pb in ((0.5, 0.4), (0.6, 0.4), (0.7, 0.4)) for n in (100, 150, 200, 288, 400)]
    for (n, pa, pb), s in zip(cells, ss.spawn(len(cells))):
        r1 = puissance(n, pa, pb, 20, 2000, np.random.default_rng(s))
        r2 = puissance(n, pa, pb, 160, 2000, np.random.default_rng(s))
        print(f"{n} ; {pa-pb:.2f} ; {r1:.3f} ; {r2:.3f}")

main()
