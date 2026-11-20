#!/usr/bin/env python3
"""Recalcul indépendant du devis « collisionneur, modes de sabotage et attaques » v1 — outil du contre-lecteur.

Écrit le 20 novembre 2026 par le contre-lecteur neuf (Opus 5.5). Aucun appel réseau, aucune dépense.
Rejoue la formule du script `collisionneur_v8_plafonds_bas_v1.py` (fonctions `devis` et `cout_pire_cas`) :
  coût d'un appel = (caractères d'entrée / 3) x prix d'entrée + (plafond de sortie + provision) x prix de sortie,
  caractères d'entrée = faits + 6 000 + question + pièces reçues x mots permis du tour x 7 (borne large du script),
avec les réglages de la section 3 du devis (Carbon à 4 / 20, plafond 65 536, provision 32 768 ; Argon provision 8 192).
Ajoute deux variantes que le devis ne calcule pas :
  (1) pièces reçues à la longueur la plus grande déjà relevée pour une cellule du collisionneur (49 389 caractères,
      `registres/depenses.md`, 25 octobre, Argon) au lieu de mots x 7 ;
  (2) entrée à 2,5 caractères par jeton (rapport le plus bas relevé pour une interface de Google, CL11, cité dans
      l'en-tête de `commande_argon_v3e.py`) au lieu de 3.
Usage : python3 -I -B recalcul_devis_v1.py QUESTION_MODES.md QUESTION_ATTAQUES.md
"""
import sys
from pathlib import Path

ESPECES = {
    # nom: (prix entrée, prix sortie, plafond premier essai, plafond relance, provision de réflexion)
    "Fable 5.1": (10.0, 50.0, 22000, 64000, 0),
    "Carbon": (4.0, 20.0, 65536, 65536, 32768),
    "Argon": (10.0, 50.0, 18000, 32000, 8192),
    "Astra": (10.0, 50.0, 8000, 32000, 0),
    "Kimi": (2.0, 10.0, 32000, 65536, 0),
}
MOTS = {"E3-T1": 3500, "E3-T2": 3000, "E3-T3": 3500}
CAS_BAS = {"Fable 5.1": 3.00, "Argon": 1.57, "Astra": 1.33, "Kimi": 0.61}
PIECE_MAX_RELEVEE = 49389


def caracteres(n_texte, tour, n_especes, piece=None):
    pieces = {"E3-T1": 0, "E3-T2": n_especes - 1, "E3-T3": n_especes}[tour]
    longueur = MOTS[tour] * 7 if piece is None else piece
    return n_texte + 6000 + n_texte + pieces * longueur


def appel(nom, chars, plafond_sortie, cpj=3.0):
    pe, ps, _, _, prov = ESPECES[nom]
    return chars / cpj / 1e6 * pe + (plafond_sortie + prov) / 1e6 * ps


def par_espece(nom, n_texte, n_especes, piece=None, cpj=3.0):
    _, _, m, mr, _ = ESPECES[nom]
    haut = pire = 0.0
    for tour in MOTS:
        c = caracteres(n_texte, tour, n_especes, piece)
        haut += appel(nom, c, m, cpj)
        pire += appel(nom, c, m, cpj) + appel(nom, c, mr, cpj)
    return haut, pire


def tableau(n_texte, noms, piece=None, cpj=3.0):
    lignes, th, tp, tb = [], 0.0, 0.0, 0.0
    for nom in noms:
        h, p = par_espece(nom, n_texte, len(noms), piece, cpj)
        b = CAS_BAS.get(nom, h / 2)
        lignes.append(f"  {nom:10s} bas {b:6.2f}  haut {h:6.2f}  pire {p:6.2f}")
        th, tp, tb = th + h, tp + p, tb + b
    lignes.append(f"  {'total':10s} bas {tb:6.2f}  haut {th:6.2f}  pire {tp:6.2f}")
    return lignes, tb, th, tp


def main(chemins):
    tailles = [len(Path(c).read_bytes().decode("utf-8-sig").replace("\r\n", "\n")) for c in chemins]
    for c, n in zip(chemins, tailles):
        print(f"{Path(c).name} : {n} caractères")
    base = ["Fable 5.1", "Carbon", "Argon", "Astra"]
    for titre, noms in (("BASE, quatre espèces", base), ("AVEC KIMI, cinq espèces", base + ["Kimi"])):
        print(f"\n=== {titre} ===")
        totaux = []
        for c, n in zip(chemins, tailles):
            print(f"-- {Path(c).name}")
            lignes, tb, th, tp = tableau(n, noms)
            print("\n".join(lignes))
            totaux.append((tb, th, tp))
        relances = (64000 / 1e6 * 50) + ((65536 + 32768) / 1e6 * 20)
        n_max = max(tailles)
        c_long = caracteres(n_max, "E3-T3", len(noms))
        epreuve = appel("Carbon", c_long, 65536)
        print(f"  relances ajoutées au plafond (sorties seules) : {relances:.3f}")
        for i, (tb, th, tp) in enumerate(totaux):
            print(f"  question {i + 1} : haut + relances = {th + relances:.2f}")
        print(f"  épreuve de Carbon (plus long tour) : {epreuve:.3f}")
        sb = sum(t[0] for t in totaux)
        sh = sum(t[1] for t in totaux)
        sp = sum(t[2] for t in totaux)
        print(f"  deux questions : bas {sb:.2f}  haut {sh:.2f}  pire sans plafond {sp + epreuve:.2f}")
        print("  variante (1), pièces à la plus grande longueur relevée :")
        for c, n in zip(chemins, tailles):
            _, _, th1, tp1 = tableau(n, noms, piece=PIECE_MAX_RELEVEE)
            print(f"    {Path(c).name} : haut {th1:.2f}  pire {tp1:.2f}")
        print("  variante (1) + (2), et 2,5 caractères par jeton :")
        for c, n in zip(chemins, tailles):
            _, _, th2, tp2 = tableau(n, noms, piece=PIECE_MAX_RELEVEE, cpj=2.5)
            print(f"    {Path(c).name} : haut {th2:.2f}  pire {tp2:.2f}")
    print("\nCarbon, un appel au bout du plafond, sorties seules : "
          f"{(65536 + 32768) / 1e6 * 20:.3f} USD ; Fable, une relance au bout : {64000 / 1e6 * 50:.3f} USD")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    main(sys.argv[1:])
