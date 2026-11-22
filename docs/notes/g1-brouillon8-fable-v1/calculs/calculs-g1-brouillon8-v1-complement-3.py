#!/usr/bin/env python3
"""Calculs de méthode du brouillon 8 de la porte G1 — complément 3 (fiche 6 : seuil du pari d'un cycle à l'autre).

Classe B (instrument de note). Aucune donnée du programme ; arithmétique exacte (fractions), aucun tirage.
À lancer depuis un dossier vide : python -I <ce fichier>.

Rappel de la règle (conception du pari apparié, § 2.2, 2.6 et 3.5 ; décision sur le seuil de promotion : 160) :
l'e-valeur arrêtée de la fiche d'un mode dépasse un seuil T avec une probabilité d'au plus 1/T quand le mode est
sous son nul. Avec M = 2 modes de porte et des cycles lus chacun sur des unités neuves :
  - une affirmation mode par mode est fausse, à un cycle au moins, avec une probabilité d'au plus  somme_k M / T_k ;
  - la porte (les deux modes promus) est franchie à tort, à un cycle au moins, avec une probabilité d'au plus
    somme_k 1 / T_k.
La borne d'union ne suppose aucune indépendance entre cycles ; elle suppose que le moniteur du cycle k est figé
avant la lecture des unités du cycle k.

Quatre suites de seuils :
  (a) 160 à chaque cycle ;
  (b) 160 x k(k+1)/2 : 160, 480, 960, 1 600, ... ;
  (c) 160 x k(k+1)   : 320, 960, 1 920, ... ;
  (d) 160 aux trois premiers cycles, puis doublé à chaque cycle : 160, 160, 160, 320, 640, 1 280, ...
"""
from __future__ import annotations

import math
from fractions import Fraction

M = 2
BASE = 160


def seuil(regle: str, k: int) -> int:
    if regle == "a":
        return BASE
    if regle == "b":
        return BASE * k * (k + 1) // 2
    if regle == "c":
        return BASE * k * (k + 1)
    if regle == "d":
        return BASE if k <= 3 else BASE * 2 ** (k - 3)
    raise ValueError(regle)


def main() -> None:
    print("Calculs de méthode, brouillon 8 de la porte G1 — complément 3 (seuil du pari d'un cycle à l'autre)")
    print("Arithmétique exacte ; aucune donnée du programme ; aucun tirage.")
    print()
    noms = {
        "a": "(a) 160 à chaque cycle",
        "b": "(b) 160 x k(k+1)/2",
        "c": "(c) 160 x k(k+1)",
        "d": "(d) 160 aux cycles 1 à 3, puis doublé à chaque cycle",
    }
    for regle in ("a", "b", "c", "d"):
        print(noms[regle])
        print("  cycle ; seuil ; borne cumulée de la porte ; borne cumulée des affirmations par mode ;"
              " évidence demandée par rapport au seuil 160 (log T / log 160)")
        cumul = Fraction(0)
        for k in range(1, 11):
            t = seuil(regle, k)
            cumul += Fraction(1, t)
            print(f"    {k:2d} ; {t:7d} ; {float(cumul):.5f} ; {float(M * cumul):.5f} ;"
                  f" {math.log(t) / math.log(BASE):.3f}")
        if regle == "a":
            print("  limite : aucune (la borne croît sans fin) ; 5 % atteints au 8e cycle pour la porte,"
                  " au 4e pour les affirmations par mode")
        elif regle == "b":
            lim = Fraction(2, BASE)
            print(f"  limite, cycles sans borne : porte {float(lim):.5f} ; par mode {float(M * lim):.5f}")
        elif regle == "c":
            lim = Fraction(1, BASE)
            print(f"  limite, cycles sans borne : porte {float(lim):.5f} ; par mode {float(M * lim):.5f}")
        else:
            lim = Fraction(3, BASE) + Fraction(1, BASE)
            print(f"  limite, cycles sans borne : porte {float(lim):.5f} ; par mode {float(M * lim):.5f}")
        print()
    print("Lecture de la dernière colonne : à effet égal, le nombre d'unités qu'il faut pour atteindre un seuil")
    print("croît à peu près comme son logarithme ; 1,137 se lit « environ 14 % d'unités de plus qu'au seuil 160 ».")
    print()
    print(f"versions : python {'.'.join(map(str, __import__('sys').version_info[:3]))}")


if __name__ == "__main__":
    main()
