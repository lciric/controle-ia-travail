#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Calculs de la note « famille réservée » (v1).

Lois exactes, aucun tirage, aucune donnée du programme, bibliothèque standard seule.
Toutes les entrées sont des suppositions d'illustration, sauf les deux tailles de banque
(288 et 400 unités par mode), reprises de l'avis d'Opus sur le mode tenu à l'écart.

Blocs :
  A. Ce qu'une réponse publique apprend à qui connaît la demande (oui/non, compte par lot),
     avec et sans retrait du juge.
  B. Le prix d'un recouvrement partiel non vu : probabilité exacte de franchir à tort une
     porte « borne basse du gain au-dessus de zéro ».
  C. Le taux de recouvrements manqués par le lecteur, borné par des paires plantées.
  D. Le stock de réserve : probabilité que toutes les familles du coffre soient écartées,
     auteurs indépendants ou corrélés.
  E. L'engagement public d'un verdict court : attaque par dictionnaire, taille du fichier.

Usage : python3 calculs-famille-reservee-v1.py > calculs-famille-reservee-v1.txt
"""
import hashlib
import math
from fractions import Fraction


def titre(t):
    print()
    print("=" * 78)
    print(t)
    print("=" * 78)


# ----------------------------------------------------------------------------
# Bloc A
# ----------------------------------------------------------------------------
def bloc_a():
    titre("BLOC A — Ce qu'une réponse publique apprend à qui connaît la demande")
    print("Monde d'illustration : la famille secrète occupe une case parmi M, a priori")
    print("uniforme ; le côté des concepteurs déclare des familles, une case chacune,")
    print("ou des ensembles de cases (familles larges).")
    print()
    print("A1. Réponse oui/non publique, juge gardé quoi qu'il arrive.")
    print("    Probabilité que les concepteurs connaissent le juge après k déclarations")
    print("    d'une case : k/M. Nombre de déclarations larges (moitié des cases restantes)")
    print("    qui suffisent à coup sûr : plafond(log2 M).")
    print("    M    k=1     k=3     k=5     déclarations larges suffisantes")
    for m in (8, 20, 64):
        ligne = "    %-4d" % m
        for k in (1, 3, 5):
            ligne += " %.4f " % (k / m)
        ligne += "  %d" % math.ceil(math.log2(m))
        print(ligne)
    assert math.ceil(math.log2(8)) == 3 and math.ceil(math.log2(64)) == 6

    print()
    print("A2. Même réponse, mais un juge recouvert est écarté et remplacé par une famille")
    print("    tirée hors des cases déclarées. Probabilité que les concepteurs connaissent")
    print("    le juge en service : 0 tant qu'il reste deux cases non déclarées. Ce qu'ils")
    print("    apprennent : le juge n'est dans aucune case déclarée ; leur meilleur pari")
    print("    sur le juge passe de 1/M à 1/(M-k).")
    print("    M    k=0     k=1     k=3     k=5")
    for m in (8, 20, 64):
        ligne = "    %-4d" % m
        for k in (0, 1, 3, 5):
            ligne += " %.4f " % (1 / (m - k))
        print(ligne)
    assert abs(1 / (20 - 0) - 0.05) < 1e-12

    print()
    print("A3. Une seule famille candidate, de probabilité a priori p de recouvrir le juge.")
    print("    Colonne 1 : probabilité que les concepteurs connaissent le juge en service,")
    print("    sous « oui/non public, juge gardé » (= p). Colonne 2 : sous « juge écarté")
    print("    si oui » (= 0). Colonne 3 : facteur par lequel un « non » public multiplie")
    print("    leur meilleur pari sur le juge (= 1/(1-p)).")
    print("    p      juge gardé   juge écarté   facteur après un non")
    for p in (0.05, 0.10, 0.20, 0.30):
        print("    %.2f   %.2f         %.2f          %.3f" % (p, p, 0.0, 1 / (1 - p)))

    print()
    print("A4. Réponse par compte sur un lot : « j familles du lot recouvrent », sans dire")
    print("    lesquelles. Lot de n familles disjointes, chacune de probabilité a priori p.")
    print("    Si le compte vaut 1, la probabilité qu'une famille donnée du lot soit le")
    print("    juge passe de p à 1/n ; la probabilité que le juge soit dans le lot, de n*p à 1.")
    print("    n    p      avant (une famille)   après (une famille)   juge dans le lot : avant -> après")
    for n, p in ((5, 0.04), (5, 0.10), (10, 0.03)):
        print("    %-4d %.2f   %.2f                  %.2f                  %.2f -> 1.00"
              % (n, p, p, 1 / n, n * p))
    print()
    print("Lecture : une réponse oui/non, ou un compte, n'est « sans contenu » que pour")
    print("qui ignore la demande. Pour qui l'a écrite, un oui vaut la description du juge.")
    print("Écarter le juge recouvert annule ce que le oui apprend sur le juge en service.")


# ----------------------------------------------------------------------------
# Bloc B
# ----------------------------------------------------------------------------
def pmf_binomiale(n, p):
    q = 1.0 - p
    if p == 0.0:
        return [1.0] + [0.0] * n
    if p == 1.0:
        return [0.0] * n + [1.0]
    return [math.comb(n, k) * (p ** k) * (q ** (n - k)) for k in range(n + 1)]


def proba_franchir(n, r_blanc, r_base, z=1.959963984540054):
    """Probabilité exacte que la borne basse de Wald à 95 % de (x/n - y/n) soit > 0,
    X ~ Bin(n, r_blanc), Y ~ Bin(n, r_base), indépendantes."""
    px = pmf_binomiale(n, r_blanc)
    py = pmf_binomiale(n, r_base)
    # cumul de Y pour accélérer : pour chaque x, on cherche les y qui franchissent.
    termes = []
    for x in range(n + 1):
        if px[x] == 0.0:
            continue
        a = x / n
        somme_y = []
        for y in range(0, x):  # il faut x > y pour une borne basse > 0
            b = y / n
            se = math.sqrt(a * (1 - a) / n + b * (1 - b) / n)
            if (a - b) - z * se > 0:
                somme_y.append(py[y])
        if somme_y:
            termes.append(px[x] * math.fsum(somme_y))
    return math.fsum(termes)


def bloc_b():
    titre("BLOC B — Le prix d'un recouvrement partiel non vu")
    print("Porte d'illustration (ce n'est pas le critère de la porte du programme, que je")
    print("n'ai pas lu) : on franchit si la borne basse de Wald à 95 % de la différence des")
    print("rappels (bras boîte blanche moins base) est au-dessus de zéro ; n unités sabotées")
    print("par bras, bras indépendants. Vérité : aucun gain, les deux bras ont le rappel r0")
    print("sur la famille juge. Recouvrement : une part c des unités de la famille juge")
    print("relève d'une famille que les concepteurs connaissent, et le bras qui la connaît")
    print("y a le rappel r_s au lieu de r0. Son rappel sur le juge devient (1-c) r0 + c r_s.")
    print("n = 288 et 400 : tailles de banque par mode reprises de l'avis d'Opus.")
    print()
    r0 = 0.30
    for r_s in (0.90, 0.60):
        print("r0 = %.2f, r_s = %.2f : probabilité de franchir à tort" % (r0, r_s))
        print("    c       n=288     n=400")
        for c in (0.00, 0.02, 0.05, 0.10, 0.20, 0.50, 1.00):
            r_blanc = (1 - c) * r0 + c * r_s
            p288 = proba_franchir(288, r_blanc, r0)
            p400 = proba_franchir(400, r_blanc, r0)
            print("    %.2f    %.4f    %.4f" % (c, p288, p400))
        print()
    # objets de contrôle
    nul_288 = proba_franchir(288, r0, r0)
    nul_400 = proba_franchir(400, r0, r0)
    assert nul_288 < 0.03 and nul_400 < 0.03, (nul_288, nul_400)
    meme = proba_franchir(288, (1 - 0.5) * r0 + 0.5 * r0, r0)
    assert abs(meme - nul_288) < 1e-12
    plein = proba_franchir(400, 0.90, r0)
    assert plein > 0.999999
    print("Objets de contrôle : sans recouvrement (c = 0), %.4f et %.4f, près du niveau"
          % (nul_288, nul_400))
    print("nominal 0,025 ; bras spécialisé sans avantage (r_s = r0) : même valeur ;")
    print("famille entièrement connue (c = 1, r_s = 0,90) : %.6f." % plein)
    print()
    # plus petite part c (au centième) qui double le niveau nominal
    print("Plus petite part c, au centième, pour laquelle la probabilité de franchir à")
    print("tort dépasse 0,05 (le double du niveau nominal) :")
    for r_s in (0.90, 0.60):
        for n in (288, 400):
            trouve = None
            for i in range(0, 101):
                c = i / 100
                if proba_franchir(n, (1 - c) * r0 + c * r_s, r0) > 0.05:
                    trouve = c
                    break
            print("    r_s = %.2f, n = %d : c = %.2f" % (r_s, n, trouve))
    print()
    rapports = []
    for r_s in (0.90, 0.60):
        for n in (288, 400):
            nul = proba_franchir(n, r0, r0)
            dix = proba_franchir(n, (1 - 0.10) * r0 + 0.10 * r_s, r0)
            rapports.append(dix / nul)
    print("À c = 0,10, le risque de franchir à tort est multiplié par %.1f à %.1f selon"
          % (min(rapports), max(rapports)))
    print("r_s et n (rapport à la valeur sans recouvrement).")
    assert min(rapports) > 4 and max(rapports) < 20
    print()
    print("Lecture : deux à quatre centièmes d'unités recouvertes suffisent à doubler le")
    print("risque de franchir à tort. Le seuil d'action ne peut donc pas être « recouvre en")
    print("majorité » : c'est « une unité au moins ». Des bras appariés, à erreur type plus")
    print("petite, seraient plus sensibles encore au même biais (raisonnement, non calcul).")


# ----------------------------------------------------------------------------
# Bloc C
# ----------------------------------------------------------------------------
def queue_basse(m, x, beta):
    return math.fsum(math.comb(m, i) * beta ** i * (1 - beta) ** (m - i) for i in range(x + 1))


def borne_haute(m, x, niveau=0.05):
    """Borne haute exacte (Clopper-Pearson, unilatérale) du taux de manqués."""
    bas, haut = 0.0, 1.0
    for _ in range(200):
        mil = (bas + haut) / 2
        if queue_basse(m, x, mil) > niveau:
            bas = mil
        else:
            haut = mil
    return haut


def bloc_c():
    titre("BLOC C — Le taux de recouvrements manqués, borné par des paires plantées")
    print("Le lecteur habilité est éprouvé sur m paires où le recouvrement est vrai par")
    print("construction (coffre factice). Avec x manqués sur m, borne haute exacte à 95 %")
    print("du taux de manqués b. Deux lecteurs, règle « le plus sévère l'emporte » : un")
    print("recouvrement n'est manqué que si les deux le manquent ; b*b s'ils sont")
    print("indépendants, b s'ils se trompent ensemble.")
    print()
    print("    m     x   borne de b   deux lecteurs indépendants   deux lecteurs liés")
    for m in (10, 20, 30, 60, 100):
        for x in (0, 1):
            b = borne_haute(m, x)
            print("    %-5d %d   %.4f       %.4f                       %.4f" % (m, x, b, b * b, b))
    # objet de contrôle : forme close pour x = 0
    for m in (10, 30, 60):
        clos = 1 - 0.05 ** (1 / m)
        assert abs(borne_haute(m, 0) - clos) < 1e-9, (m, borne_haute(m, 0), clos)
    print()
    print("Objet de contrôle : pour x = 0 la bissection retrouve 1 - 0,05^(1/m)")
    print("(m = 30 : %.4f ; règle de trois : 3/30 = 0,1000)." % (1 - 0.05 ** (1 / 30)))
    print()
    print("Risque restant qu'un juge recouvert serve quand même : q * b, q étant la")
    print("probabilité a priori que la famille déclarée recouvre le juge.")
    print("    q      b=0,0950 (30 paires, un lecteur)   b=0,0090 (deux, indépendants)")
    b1 = borne_haute(30, 0)
    for q in (0.05, 0.10, 0.20, 0.30):
        print("    %.2f   %.4f                             %.4f" % (q, q * b1, q * b1 * b1))
    print()
    print("Familles écartées à tort par vérification, a = taux de fausses alertes d'un")
    print("lecteur, deux lecteurs : 1 - (1-a)^2.")
    for a in (0.02, 0.05, 0.10):
        print("    a = %.2f : %.4f" % (a, 1 - (1 - a) ** 2))


# ----------------------------------------------------------------------------
# Bloc D
# ----------------------------------------------------------------------------
def tout_ecarte(n, q, rho):
    """Probabilité que les n familles du coffre recouvrent toutes la liste déclarée.
    q : probabilité marginale ; rho : corrélation entre familles (loi bêta-binomiale).
    rho = 0 : indépendance."""
    q = Fraction(q)
    rho = Fraction(rho)
    if rho == 0:
        return q ** n
    a = q * (1 - rho) / rho
    b = (1 - q) * (1 - rho) / rho
    prod = Fraction(1)
    for i in range(n):
        prod *= (a + i) / (a + b + i)
    return prod


def bloc_d():
    titre("BLOC D — Le stock de réserve")
    print("Le coffre tient n familles ; chacune recouvre la liste des familles déclarées")
    print("avec la probabilité q. Si toutes recouvrent, il n'y a plus de juge : il faut en")
    print("écrire une, et ce délai se voit du dehors. Corrélation rho entre familles :")
    print("0 si les auteurs sont indépendants ; plus haute s'ils sont des instances d'un")
    print("même modèle, sur la même consigne.")
    print()
    for rho in (Fraction(0), Fraction(1, 5), Fraction(1, 2)):
        print("rho = %s" % (float(rho),))
        print("    q      n=1      n=2      n=3      n=4      n=6")
        for q in (Fraction(1, 20), Fraction(1, 10), Fraction(1, 5), Fraction(3, 10)):
            ligne = "    %.2f " % float(q)
            for n in (1, 2, 3, 4, 6):
                ligne += "  %.4f " % float(tout_ecarte(n, q, rho))
            print(ligne)
        print()
    # objets de contrôle
    assert tout_ecarte(3, Fraction(1, 5), 0) == Fraction(1, 125)
    for rho in (Fraction(1, 5), Fraction(1, 2)):
        assert tout_ecarte(1, Fraction(1, 5), rho) == Fraction(1, 5)
    assert tout_ecarte(2, Fraction(1, 5), Fraction(1, 2)) == Fraction(3, 25)
    print("Objets de contrôle : rho = 0, q = 0,2, n = 3 : 1/125 exactement ; n = 1 rend q")
    print("pour toute corrélation ; rho = 0,5, q = 0,2, n = 2 : 3/25 exactement.")
    print()
    print("Plus petit n pour que la probabilité d'un coffre vide passe sous 0,05, puis 0,01 :")
    print("    rho    q      n (0,05)   n (0,01)")
    for rho in (Fraction(0), Fraction(1, 5), Fraction(1, 2)):
        for q in (Fraction(1, 10), Fraction(1, 5), Fraction(3, 10)):
            n05 = next((n for n in range(1, 2001) if tout_ecarte(n, q, rho) <= Fraction(5, 100)), None)
            n01 = next((n for n in range(1, 2001) if tout_ecarte(n, q, rho) <= Fraction(1, 100)), None)
            print("    %.1f    %.2f   %-9s  %s" % (float(rho), float(q),
                                                  n05 if n05 is not None else "> 2000",
                                                  n01 if n01 is not None else "> 2000"))
    print()
    rap = [float(tout_ecarte(2, q, Fraction(1, 2)) / tout_ecarte(6, q, Fraction(1, 2)))
           for q in (Fraction(1, 20), Fraction(1, 10), Fraction(1, 5), Fraction(3, 10))]
    rap0 = [float(tout_ecarte(2, q, Fraction(0)) / tout_ecarte(6, q, Fraction(0)))
            for q in (Fraction(1, 20), Fraction(1, 10), Fraction(1, 5), Fraction(3, 10))]
    print("Passer de deux à six familles divise le risque d'un coffre vide par %.1f à %.1f"
          % (min(rap), max(rap)))
    print("à corrélation 0,5, et par %.0f à %.0f sans corrélation." % (min(rap0), max(rap0)))
    assert max(rap) < 3 and min(rap0) > 100
    print()
    print("Lecture : une réserve n'achète de la sûreté que si ses auteurs sont indépendants.")
    print("La diversité des auteurs compte plus que leur nombre.")


# ----------------------------------------------------------------------------
# Bloc E
# ----------------------------------------------------------------------------
def bloc_e():
    titre("BLOC E — L'engagement public d'un verdict court")
    print("Le verdict du lecteur est consigné dans le coffre ; une empreinte en est posée")
    print("du côté public pour qu'on ne puisse pas le changer après coup. Si le fichier ne")
    print("contient que le verdict, quiconque voit l'empreinte retrouve le verdict en")
    print("calculant l'empreinte de chaque verdict possible.")
    print()
    verdicts_mots = ["étranger\n", "voisin\n", "recouvrement partiel\n", "recouvrement\n"]
    verdicts_codes = ["0\n", "1\n", "2\n", "3\n"]

    def empreinte(octets):
        return hashlib.sha256(octets).hexdigest()

    def attaque(empreinte_vue, candidats, prefixes=(b"",)):
        for pre in prefixes:
            for cand in candidats:
                if empreinte(pre + cand.encode("utf-8")) == empreinte_vue:
                    return cand
        return None

    # E1 : sans sel
    retrouves = 0
    for v in verdicts_mots:
        vue = empreinte(v.encode("utf-8"))
        if attaque(vue, verdicts_mots) == v:
            retrouves += 1
    print("E1. Fichier sans sel : verdicts retrouvés par dictionnaire : %d sur %d."
          % (retrouves, len(verdicts_mots)))
    assert retrouves == len(verdicts_mots)

    # E2 : avec sel de 32 octets tenu dans le coffre. Sel de démonstration, dérivé
    # d'une étiquette fixe : il est public par construction, il ne sert qu'à montrer
    # la forme ; un vrai sel est tiré dans le coffre et n'en sort qu'à l'évaluation.
    sel = hashlib.sha256("sel de démonstration, public par construction".encode("utf-8")).digest()
    assert len(sel) == 32
    retrouves_sel = 0
    faux_sels = [b"", b"\x00" * 32, hashlib.sha256(b"autre").digest()]
    for v in verdicts_codes:
        vue = empreinte(sel + v.encode("utf-8"))
        if attaque(vue, verdicts_codes, prefixes=faux_sels) == v:
            retrouves_sel += 1
    print("E2. Fichier avec sel de 32 octets inconnu de l'observateur : verdicts retrouvés")
    print("    par dictionnaire (sans le sel, trois sels devinés) : %d sur %d."
          % (retrouves_sel, len(verdicts_codes)))
    assert retrouves_sel == 0
    # et avec le sel, à l'ouverture, chacun vérifie
    ouverts = sum(1 for v in verdicts_codes
                  if attaque(empreinte(sel + v.encode("utf-8")), verdicts_codes, prefixes=[sel]) == v)
    print("    À l'évaluation, le sel révélé, verdicts vérifiés par tous : %d sur %d."
          % (ouverts, len(verdicts_codes)))
    assert ouverts == len(verdicts_codes)

    # E3 : taille
    tailles_mots = sorted({len(v.encode("utf-8")) for v in verdicts_mots})
    tailles_codes = sorted({len(sel) + len(v.encode("utf-8")) for v in verdicts_codes})
    print()
    print("E3. Un inventaire public qui donne les tailles trahit le verdict s'il est écrit")
    print("    en mots : tailles distinctes %s octets (%d valeurs pour %d verdicts)."
          % (tailles_mots, len(tailles_mots), len(verdicts_mots)))
    print("    En code de largeur fixe, avec sel : tailles distinctes %s octets (%d valeur)."
          % (tailles_codes, len(tailles_codes)))
    assert len(tailles_mots) == len(verdicts_mots)
    assert len(tailles_codes) == 1
    print()
    print("Lecture : l'empreinte compagnon d'un verdict court est le verdict. Il faut un sel")
    print("tenu dans le coffre, un code de largeur fixe, et aucune taille variable du côté public.")


def main():
    print("Calculs de la note « famille réservée » (v1) — lois exactes, aucun tirage.")
    bloc_a()
    bloc_b()
    bloc_c()
    bloc_d()
    bloc_e()
    print()
    print("Fin. Toutes les assertions sont passées.")


if __name__ == "__main__":
    main()
