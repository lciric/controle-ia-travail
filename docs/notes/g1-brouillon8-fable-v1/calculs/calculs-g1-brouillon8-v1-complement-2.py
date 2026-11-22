#!/usr/bin/env python3
"""Calculs de méthode du brouillon 8 de la porte G1 — complément 2 (fiches sur le critère contre le véhicule).

Classe B (instrument de note). Aucune donnée du programme : lois supposées, écrites ici.
Tout est analytique (aucun tirage). À lancer depuis un dossier vide : python -I <ce fichier>.

Supposition commune des paragraphes 1 et 2 : modèle binormal à variances égales. La statistique d'un moniteur
suit une loi normale réduite sur la classe négative (épisodes du témoin apparié) et la même loi décalée de d
sur les épisodes sabotés. Le rappel à un taux d'alerte a sur la classe négative vaut Phi(d - z(1 - a)).
C'est le modèle du calcul de la conception du pari apparié, § 2.4 (rappel 0,40 à 1 %, pente 14,5).

§ 1 — Ce qu'une tolérance sur le taux d'alerte du témoin laisse passer : rappel d'un même moniteur
       selon qu'il sonne sur 1 %, 2 %, 3 % ou 5 % des épisodes du témoin.
§ 2 — Bruit d'un seuil recalibré à 1 % sur K épisodes du témoin, traduit en bruit de rappel.
§ 3 — Devis : calibrage du témoin à 10 et 15 fois les unités sabotées, même modèle de coût que le brouillon 6.
"""
from __future__ import annotations

import math

from scipy.stats import norm

TAU = 0.01


def decalage_pour_rappel(rappel: float, a: float = TAU) -> float:
    return float(norm.ppf(1.0 - a) + norm.ppf(rappel))


def rappel(d: float, a: float) -> float:
    return float(norm.cdf(d - norm.ppf(1.0 - a)))


def pente(d: float, a: float = TAU) -> float:
    """Dérivée du rappel par rapport au taux d'alerte sur la classe négative, au point a."""
    z = float(norm.ppf(1.0 - a))
    return float(norm.pdf(d - z) / norm.pdf(z))


def main() -> None:
    print("Calculs de méthode, brouillon 8 de la porte G1 — complément 2 (critère contre le véhicule)")
    print("Lois supposées (modèle binormal à variances égales) ; aucune donnée du programme ; aucun tirage.")
    print()
    print("§ 1 — Rappel d'un même moniteur selon son taux d'alerte sur le témoin")
    print("  rappel à 1 % ; décalage d ; rappel à 2 % ; à 3 % ; à 5 % ; gain de rappel de 1 % à 5 % ;"
          " dont au-delà des alertes en plus (gain moins 0,04)")
    for r1 in (0.10, 0.20, 0.30, 0.40, 0.50, 0.60, 0.80):
        d = decalage_pour_rappel(r1)
        r2, r3, r5 = rappel(d, 0.02), rappel(d, 0.03), rappel(d, 0.05)
        print(f"    {r1:.2f} ; {d:.3f} ; {r2:.3f} ; {r3:.3f} ; {r5:.3f} ; {r5 - r1:+.3f} ; {r5 - r1 - 0.04:+.3f}")
    print("  lecture : un moniteur qui sonne sur 5 % des épisodes du témoin au lieu de 1 % affiche, à pouvoir de")
    print("  détection égal, le rappel de la colonne « à 5 % » ; l'écart de planification du texte de la porte est 0,10.")
    print()
    print("§ 2 — Bruit d'un seuil recalibré à 1 % sur K épisodes indépendants, traduit en rappel")
    d40 = decalage_pour_rappel(0.40)
    p40 = pente(d40)
    print(f"  cas de la conception du pari : rappel 0,40 à 1 %, décalage {d40:.3f}, pente {p40:.2f}"
          " (conception : 14,5)")
    print("  K ; écart-type du taux d'alerte réel (points) ; écart-type du rappel d'un moniteur (points) ;"
          " écart-type de l'écart de rappel entre deux moniteurs de même loi, seuils indépendants (points)")
    for k in (300, 450, 1000, 2000, 4000, 10000, 40000, 60000):
        sd_a = math.sqrt(TAU * (1.0 - TAU) / k)
        sd_r = p40 * sd_a
        print(f"    {k:6d} ; {100 * sd_a:.3f} ; {100 * sd_r:.2f} ; {100 * sd_r * math.sqrt(2.0):.2f}")
    print("  contrôle : à K = 450 (45 unités de dix épisodes), la conception écrit 9,6 points pour l'écart entre"
          " deux moniteurs.")
    print("  même calcul pour d'autres rappels à 1 % (pente ; écart-type de l'écart entre deux moniteurs à K = 300,"
          " puis à K = 60 000, en points) :")
    for r1 in (0.10, 0.20, 0.40, 0.60):
        d = decalage_pour_rappel(r1)
        p = pente(d)
        e300 = 100 * p * math.sqrt(TAU * (1 - TAU) / 300) * math.sqrt(2.0)
        e60k = 100 * p * math.sqrt(TAU * (1 - TAU) / 60000) * math.sqrt(2.0)
        print(f"    rappel {r1:.2f} : pente {p:.2f} ; {e300:.2f} ; {e60k:.2f}")
    print()
    print("§ 3 — Devis du calibrage sur le témoin (modèle de coût du brouillon 6, estimation centrale)")
    secondes = 48.35 + 2 * 58.2      # génération et notation, par épisode (central)
    usd_h = 1.1467
    taches = 400

    def cout(episodes: int) -> float:
        return episodes * secondes / 3600.0 * usd_h

    base = taches * 232
    print(f"  contrôle : {base} épisodes sans témoin ; {cout(base):.0f} USD (brouillon 6 : 92 800 ; 4 870)")
    print("  variante ; épisodes du témoin par tâche ; épisodes en tout ; USD central ; central x 1,3 ;"
          " sous un plafond de 7 600")
    variantes = [
        ("évaluation seule : 10 exécutions dans les deux cellules de la porte, 1 dans les quatre autres", 24),
        ("300 épisodes de calibrage par cellule (six cellules) + évaluation 10 et 1", None),
        ("calibrage à 10 fois les unités sabotées (100 par tâche) dans les deux cellules de la porte"
         " + évaluation 10 et 1", 2 * 100 + 24),
        ("calibrage à 15 fois (150 par tâche, échelle de l'honnête) dans les deux cellules de la porte"
         " + évaluation 10 et 1", 2 * 150 + 24),
        ("calibrage à 15 fois dans les deux cellules de la porte + évaluation 10 et 3"
         " (hypothèse du rédacteur précédent ; calcul v1, § 5)", 2 * 150 + 39),
    ]
    for nom, par_tache in variantes:
        if par_tache is None:
            total = base + taches * 24 + 6 * 300
            par = (taches * 24 + 6 * 300) / taches
        else:
            total = base + taches * par_tache
            par = par_tache
        c = cout(total)
        print(f"    {nom} ; {par:g} ; {total} ; {c:.0f} ; {1.3 * c:.0f} ; {'oui' if 1.3 * c <= 7600 else 'non'}")
    print()
    print(f"versions : python {'.'.join(map(str, __import__('sys').version_info[:3]))} ;"
          f" scipy {__import__('scipy').__version__}")


if __name__ == "__main__":
    main()
