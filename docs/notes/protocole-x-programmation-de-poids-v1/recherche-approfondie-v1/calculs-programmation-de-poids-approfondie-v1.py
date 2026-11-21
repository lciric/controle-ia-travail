#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Calculs de la note « programmation de poids, recherche approfondie » (v1).

Pièce de travail (classe C), non contre-lue. Aucune donnée du programme : les seules entrées
sont (a) des chiffres publiés, recopiés avec leur page, et (b) des suppositions d'illustration,
marquées comme telles. Lois exactes pour les blocs A, C et D ; tirages à graines consignées
(numpy.random.SeedSequence) pour le bloc B.

Rejeu : python3 -B calculs-programmation-de-poids-approfondie-v1.py > sortie.txt
(Python 3.13.18, numpy 2.5.3 ; un autre numpy change la ligne qui imprime sa version et,
peut-être, les tirages du bloc B). Rejoué deux fois, sorties comparées à l'octet.

Les attentes (objets de contrôle) sont écrites dans le code, sous forme d'assertions,
avant toute exécution : un objet où la conclusion est fausse et un objet où elle est vraie
par bloc.
"""
import math
import sys
from statistics import NormalDist

import numpy as np

N01 = NormalDist()
GRAINE_MERE = 20261121  # consignée ; toutes les graines du bloc B en dérivent


def q(p):
    """Quantile de la loi normale centrée réduite."""
    return N01.inv_cdf(p)


def queue(x):
    """Probabilité de dépasser x pour une loi normale centrée réduite."""
    return 1.0 - N01.cdf(x)


def titre(t):
    print()
    print("=" * 100)
    print(t)
    print("=" * 100)


# ---------------------------------------------------------------------------------------------
# Bloc A — Du rapport des taux de fausses alertes, à seuil gelé, au déplacement du niveau
# ---------------------------------------------------------------------------------------------
def deplacement(r, alpha, echelle=1.0):
    """Déplacement d (en écarts types des scores bénins d'avant) tel qu'un seuil gelé au taux
    alpha passe au taux r*alpha, si les scores bénins restent normaux, translatés de d et
    d'écart type multiplié par `echelle`. Translation pure si echelle = 1."""
    if r * alpha >= 1:
        return float("nan")
    return q(1 - alpha) - echelle * q(1 - r * alpha)


def taux_apres(d, alpha, echelle=1.0):
    return queue((q(1 - alpha) - d) / echelle)


def bloc_a():
    titre("BLOC A — Rapport des taux de fausses alertes à seuil gelé  ->  déplacement du niveau, en écarts types")
    print("Modèle : scores bénins normaux ; la mise à jour les translate de d écarts types (échelle inchangée).")
    print("Entrées : rapports publiés (Shire et Kim, arXiv 2611.19216v1, p. 8, tableaux 3 et 4), recopiés.")
    print("Réserve : leur rapport est une moyenne de rapports par tirage, non un rapport de moyennes ;")
    print("          le modèle à deux moments des auteurs demande aussi le changement d'échelle (p. 9).")
    # Objets de contrôle
    assert abs(q(0.99) - 2.3263) < 1e-3                      # quantile connu
    assert abs(deplacement(1.0, 0.01)) < 1e-12               # objet faux : rapport 1 -> aucun déplacement
    d_max = deplacement(15.12 / 1.01, 0.01)                  # objet vrai : 1,01 % -> 15,12 % (p. 8)
    assert 1.2 < d_max < 1.4, d_max
    for r in (0.5, 2.0, 5.0):                                # aller et retour
        assert abs(taux_apres(deplacement(r, 0.01), 0.01) - r * 0.01) < 1e-9
    print()
    print("Contrôles : quantile 0,99 = %.4f ; rapport 1 -> %.3f ; de 1,01 %% à 15,12 %% -> %.3f écart type."
          % (q(0.99), deplacement(1.0, 0.01), d_max))
    print()
    cellules = [
        ("1a  base -> conversation (Mistral-7B), jeu Aegis", 17.377),
        ("1a  même paire, jeu WildGuardMix", 9.521),
        ("1b  base -> conversation (Gemma-2-9B)", 6.783),
        ("2e  base -> ajustement supervisé (OLMo-2), gabarit changé", 5.874),
        ("1g  version de base 3 -> 3.1 (Llama-3-8B)", 3.224),
        ("1f  base -> conversation (OLMo-2)", 3.146),
        ("1c  base -> conversation (Llama-3-8B)", 2.395),
        ("2b  conversation 3 -> 3.1 (Llama), gabarit changé", 2.254),
        ("1d  base -> conversation (Llama-3.1-8B)", 2.152),
        ("1e  base -> conversation (Qwen2.5-7B)", 1.577),
        ("2d  Phi-3-mini -> Phi-3.5-mini", 1.171),
        ("2g  étape d'après-entraînement (OLMo-2, préférences -> final)", 1.057),
        ("2f  étape d'après-entraînement (OLMo-2, supervisé -> préférences)", 1.050),
        ("2c  Qwen2 -> Qwen2.5 (conversation)", 1.028),
        ("2i  étape d'après-entraînement (Tulu-3, préférences -> final)", 0.905),
        ("2h  étape d'après-entraînement (Tulu-3, supervisé -> préférences)", 0.779),
        ("2a  Mistral conversation v0.1 -> v0.2 (seule cellule « ouverte »)", 0.055),
    ]
    print("%-70s %8s %12s %12s" % ("Cellule (cible 1 %)", "rapport", "taux après", "déplacement"))
    for nom, r in cellules:
        d = deplacement(r, 0.01)
        print("%-70s %8.3f %11.2f%% %+12.3f" % (nom, r, 100 * r * 0.01, d))
    print()
    print("Adaptateurs de rang 16 sur Mistral-7B (tableau 4, pire couche du balayage, FPR/cible) :")
    lora = [("corpus général (Alpaca), 25 pas", 1.60), ("corpus général, 100 pas", 1.44),
            ("corpus général, 400 pas", 1.58), ("corpus de sécurité (PKU-SafeRLHF), 25 pas", 21.33),
            ("corpus de sécurité, 100 pas", 10.49), ("corpus de sécurité, 400 pas", 12.27)]
    for nom, r in lora:
        print("  %-50s rapport %6.2f -> déplacement %+6.3f" % (nom, r, deplacement(r, 0.01)))
    print()
    print("Repères, cible 1 %% : la coupure « endommagé » des auteurs (rapport 2 ou 0,5) vaut %+.3f et %+.3f écart type ;"
          % (deplacement(2.0, 0.01), deplacement(0.5, 0.01)))
    print("un rapport de 1,5 vaut %+.3f ; de 1,2 : %+.3f ; de 1,1 : %+.3f."
          % (deplacement(1.5, 0.01), deplacement(1.2, 0.01), deplacement(1.1, 0.01)))
    print("Sensibilité à l'échelle : pour le rapport 2, si l'écart type des scores bénins croît de 10 %,")
    print("le même rapport s'obtient avec une translation de %+.3f seulement (au lieu de %+.3f)."
          % (deplacement(2.0, 0.01, 1.10), deplacement(2.0, 0.01)))
    return {nom: deplacement(r, 0.01) for nom, r in cellules}


# ---------------------------------------------------------------------------------------------
# Bloc B — Ce qu'un déplacement du niveau fait à une accumulation valide à tout instant
# ---------------------------------------------------------------------------------------------
LAMBDAS = np.array([0.05, 0.1, 0.2, 0.3, 0.5, 0.8, 1.2])
ALPHA = 0.01
HORIZON = 5000
N_TRAJ = 4000
LOT = 250


def temps_d_alerte(delta, graine):
    """Premier instant où le pari mélangé dépasse 1/ALPHA, pour des scores N(delta, 1).
    Pari : moyenne, sur la grille LAMBDAS, de exp(lambda * S_n - n * lambda^2 / 2) (unilatéral).
    Sous delta = 0 c'est une martingale positive de départ 1 : inégalité de Ville, niveau ALPHA.
    Rend un tableau de N_TRAJ entiers ; HORIZON + 1 veut dire : pas d'alerte sur l'horizon."""
    rng = np.random.default_rng(graine)
    n = np.arange(1, HORIZON + 1, dtype=np.float64)
    seuil = math.log(1.0 / ALPHA)
    out = np.empty(N_TRAJ, dtype=np.int64)
    for a in range(0, N_TRAJ, LOT):
        x = rng.standard_normal((LOT, HORIZON)) + delta
        s = np.cumsum(x, axis=1)
        # log du mélange, par log-somme-exponentielle sur la grille
        lg = LAMBDAS[:, None, None] * s[None, :, :] - (LAMBDAS[:, None, None] ** 2) * n[None, None, :] / 2.0
        m = lg.max(axis=0)
        logE = m + np.log(np.exp(lg - m[None, :, :]).mean(axis=0))
        franchi = logE >= seuil
        premier = np.where(franchi.any(axis=1), franchi.argmax(axis=1) + 1, HORIZON + 1)
        out[a:a + LOT] = premier
    return out


def resume(t):
    part = lambda k: float((t <= k).mean())
    med = float(np.median(t))
    return part(100), part(500), part(2000), part(5000), (med if med <= HORIZON else float("inf"))


def bloc_b(depl_a):
    titre("BLOC B — Honnête lu contre la référence d'avant l'écriture : part des trajectoires qui sonnent")
    print("Pari mélangé unilatéral sur la grille %s, niveau %.0f %%, %d trajectoires, horizon %d."
          % ([float(x) for x in LAMBDAS], 100 * ALPHA, N_TRAJ, HORIZON))
    print("Graine mère %d (SeedSequence) ; une graine fille par ligne, dans l'ordre d'impression." % GRAINE_MERE)
    filles = np.random.SeedSequence(GRAINE_MERE).spawn(64)
    k = 0
    # Objet faux : aucun déplacement -> au plus ALPHA (Ville), à l'erreur de tirage près
    t0 = temps_d_alerte(0.0, filles[k]); k += 1
    r0 = resume(t0)
    assert r0[3] <= 0.013 + 3 * math.sqrt(0.01 * 0.99 / N_TRAJ), r0
    # Objet vrai : déplacement de 0,5 -> délai médian entre 20 et 80 épisodes
    t5 = temps_d_alerte(0.5, filles[k]); k += 1
    r5 = resume(t5)
    assert 20 <= r5[4] <= 80, r5
    print()
    print("Contrôles : sans déplacement, %.4f des trajectoires sonnent en %d épisodes (attendu au plus 0,01, plus l'erreur de tirage) ;"
          % (r0[3], HORIZON))
    print("            déplacement de 0,5 : délai médian %.0f épisodes (attendu entre 20 et 80)." % r5[4])
    print()
    print("%-58s %8s | %7s %7s %7s %7s | %8s" % ("Écriture bénigne qui déplace le niveau de", "(é.-t.)", "100", "500", "2000", "5000", "médiane"))
    lignes = [
        ("rapport 1,1 à la cible 1 %", deplacement(1.1, 0.01)),
        ("rapport 1,2", deplacement(1.2, 0.01)),
        ("rapport 1,5 (adaptateur général, pire couche : 1,44 à 1,60)", deplacement(1.5, 0.01)),
        ("rapport 2 (coupure « endommagé » de la pièce publiée)", deplacement(2.0, 0.01)),
        ("rapport 3,2 (changement de version de la base)", deplacement(3.224, 0.01)),
        ("rapport 5,9", deplacement(5.874, 0.01)),
        ("rapport 17,4 (la plus forte hausse publiée)", deplacement(17.377, 0.01)),
    ]
    monotone = []
    for nom, d in lignes:
        t = temps_d_alerte(d, filles[k]); k += 1
        a, b, c, e, med = resume(t)
        monotone.append(e)
        print("%-58s %+8.3f | %7.3f %7.3f %7.3f %7.3f | %8s"
              % (nom, d, a, b, c, e, ("%.0f" % med) if math.isfinite(med) else "> 5000"))
    assert all(x <= y + 0.02 for x, y in zip(monotone, monotone[1:])), monotone  # monotonie en d
    print()
    print("Lecture : colonnes = part des agents honnêtes qui font sonner l'accumulation en 100, 500, 2 000, 5 000 épisodes.")
    print()
    print("Sens inverse (le seuil gelé « s'ouvre ») : un saboteur qui déplace le score de s, lu après une écriture")
    print("bénigne qui déplace le niveau de -g, est lu comme un déplacement de s - g. Délai médian de l'alerte :")
    print("%-10s %-10s %-12s %10s %10s" % ("s", "g", "s - g", "médiane", "pris/5000"))
    for s_, g_ in [(0.3, 0.0), (0.3, 0.1), (0.3, 0.2), (0.2, 0.0), (0.2, 0.05), (0.2, 0.1), (0.2, 0.15)]:
        t = temps_d_alerte(s_ - g_, filles[k]); k += 1
        a, b, c, e, med = resume(t)
        print("%-10.2f %-10.2f %-12.2f %10s %10.3f" % (s_, g_, s_ - g_, ("%.0f" % med) if math.isfinite(med) else "> 5000", e))
    print("(graines filles employées : %d)" % k)


# ---------------------------------------------------------------------------------------------
# Bloc C — Ce que coûte la mesure du glissement sur nos sondes
# ---------------------------------------------------------------------------------------------
def n_apparie(delta, rho, niveau=0.01, puissance=0.90):
    """Épisodes honnêtes rejoués sur deux états, pour voir un déplacement moyen de delta écarts
    types (test bilatéral, approximation normale). rho : corrélation, épisode par épisode, des
    scores des deux états."""
    z = q(1 - niveau / 2) + q(puissance)
    return math.ceil((z ** 2) * 2 * (1 - rho) / (delta ** 2))


def n_taux(r, alpha, niveau=0.01, puissance=0.90):
    """Épisodes honnêtes neufs pour voir un taux de dépassement passer de alpha à r*alpha
    (un échantillon, approximation normale ; le taux d'avant est supposé connu)."""
    p0, p1 = alpha, r * alpha
    num = q(1 - niveau / 2) * math.sqrt(p0 * (1 - p0)) + q(puissance) * math.sqrt(p1 * (1 - p1))
    return math.ceil((num / (p1 - p0)) ** 2)


def bloc_c():
    titre("BLOC C — Coût de la mesure du glissement : combien d'épisodes honnêtes, et quel calcul")
    # Objets de contrôle
    et = math.sqrt(0.01 * 0.99 / 1000)          # objet vrai : la résolution publiée (registre des auteurs, rang 48, p. 20)
    assert abs(et - 0.0031) < 2e-4, et
    assert n_apparie(0.1, 0.0) > n_apparie(0.1, 0.8) > n_apparie(0.2, 0.8)   # monotonie
    assert n_apparie(1e9, 0.0) == 1                                          # objet faux : effet énorme -> un épisode
    print("Contrôle : écart type d'un taux de 1 %% estimé sur 1 000 épisodes bénins = %.4f, soit %.0f %% de la cible"
          % (et, 100 * et / 0.01))
    print("           (la pièce publiée donne « about 0.0031, 31% of the target », p. 20).")
    print()
    print("C1. Mesure appariée du NIVEAU (mêmes épisodes honnêtes rejoués sur deux états ; niveau 1 %, puissance 90 %)")
    print("%-28s" % "déplacement à voir (é.-t.)" + "".join("%12s" % ("rho = %.2f" % r) for r in (0.0, 0.5, 0.8, 0.95)))
    for d in (0.05, 0.1, 0.2, 0.3):
        print("%-28.2f" % d + "".join("%12d" % n_apparie(d, r) for r in (0.0, 0.5, 0.8, 0.95)))
    print("  rho = corrélation des scores des deux états sur le même épisode : inconnue pour nos sondes ; 0 = aucune (pire cas).")
    print()
    print("C2. Mesure du TAUX de dépassement d'un seuil gelé (épisodes honnêtes neufs ; niveau 1 %, puissance 90 %)")
    print("%-28s %12s %12s" % ("rapport à voir", "cible 1 %", "cible 5 %"))
    for r in (1.5, 2.0, 3.0, 5.0):
        print("%-28.1f %12d %12d" % (r, n_taux(r, 0.01), n_taux(r, 0.05)))
    print("  À effet égal, le niveau apparié demande moins d'épisodes que le taux de queue :")
    print("  rapport 2 à la cible 1 %% = %.3f é.-t. ; niveau apparié à rho = 0,5 : %d épisodes ; taux : %d."
          % (deplacement(2.0, 0.01), n_apparie(deplacement(2.0, 0.01), 0.5), n_taux(2.0, 0.01)))
    print()
    print("C3. Calcul, pour n épisodes rejoués sur deux états (toutes les entrées sont SUPPOSÉES)")
    print("    jetons = n x longueur x 2 ; durée = jetons / débit ; coût = durée x prix horaire + coût fixe.")
    prix_h, fixe = 1.38, 6.90   # repères du registre des accords (GO-2026-11-21-70) pour une autre ligne de calcul
    print("    Repères de prix : %.2f USD l'heure et %.2f USD de coût fixe (registre des accords, ligne du saboteur à budget)." % (prix_h, fixe))
    print("%-10s %-12s %-14s %12s %10s %12s" % ("n", "longueur", "débit (j/s)", "jetons (M)", "heures", "coût (USD)"))
    for n in (300, 600, 1000, 3000):
        for longueur in (2000, 8000):
            for debit in (500, 2000):
                jetons = n * longueur * 2
                h = jetons / debit / 3600
                print("%-10d %-12d %-14d %12.1f %10.2f %12.2f" % (n, longueur, debit, jetons / 1e6, h, h * prix_h + fixe))
    print("    Si les activations des épisodes honnêtes sont déjà en cache pour deux états : calcul sur processeur, coût nul.")


# ---------------------------------------------------------------------------------------------
# Bloc D — Rappel de la recherche contre une liste tenue par un tiers
# ---------------------------------------------------------------------------------------------
def binom_cdf(k, n, p):
    return sum(math.comb(n, i) * p ** i * (1 - p) ** (n - i) for i in range(0, k + 1))


def clopper_pearson(k, n, conf=0.95):
    a = (1 - conf) / 2
    def racine(f, lo, hi):
        for _ in range(200):
            mid = (lo + hi) / 2
            if f(mid) > 0: lo = mid
            else: hi = mid
        return (lo + hi) / 2
    bas = 0.0 if k == 0 else racine(lambda p: a - (1 - binom_cdf(k - 1, n, p)), 0.0, 1.0)
    haut = 1.0 if k == n else racine(lambda p: binom_cdf(k, n, p) - a, 0.0, 1.0)
    return bas, haut


def bloc_d():
    titre("BLOC D — Rappel de mes requêtes d'arXiv, mesuré contre une liste publique tenue par un tiers")
    # Objets de contrôle : intervalles exacts connus
    b, h = clopper_pearson(0, 10)
    assert b == 0.0 and abs(h - 0.3085) < 1e-3, (b, h)        # 0 sur 10 -> [0 ; 0,3085]
    b, h = clopper_pearson(10, 10)
    assert h == 1.0 and abs(b - 0.6915) < 1e-3, (b, h)        # 10 sur 10 -> [0,6915 ; 1]
    trouves, total = 31, 33   # journal : liste-publique-principale.tsv contre ensemble-arxiv-avant-listes.txt
    b, h = clopper_pearson(trouves, total)
    print("Liste publique (664 entrées, relevée le 21 novembre 2026) : 180 entrées datées du 2 novembre ou après,")
    print("dont 33 portent un identifiant d'arXiv. Mes requêtes d'arXiv, figées avant lecture de la liste, en avaient 31.")
    print("Rappel sur les pièces d'arXiv de la vague : %d/%d = %.3f ; intervalle exact à 95 %% : [%.3f ; %.3f]." % (trouves, total, trouves / total, b, h))
    print("Part de la vague hors d'arXiv (billets, dépôts de code, archives) : %d/%d = %.3f." % (180 - 33, 180, (180 - 33) / 180))
    print("Limite : la liste recense mal les pièces de sécurité et de surveillance : sur douze pièces de ce côté rendues")
    print("par mes requêtes et contrôlées une à une, quatre y figurent. Le rappel ci-dessus ne vaut que pour la vague.")


def main():
    print("Calculs de la note « programmation de poids, recherche approfondie » (v1)")
    print("Python %s ; numpy %s" % (sys.version.split()[0], np.__version__))
    da = bloc_a()
    bloc_b(da)
    bloc_c()
    bloc_d()
    print()
    print("Fin. Toutes les assertions (objets de contrôle) tenues.")


if __name__ == "__main__":
    main()
