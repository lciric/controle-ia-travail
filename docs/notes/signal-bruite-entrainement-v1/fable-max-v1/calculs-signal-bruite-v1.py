#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Calculs de la note « le signal bruité pourrait suffire pour entraîner » (v1).

Lois exactes et intégration numérique déterministe (règle de Simpson, grille fixe).
Aucun tirage au hasard, aucune donnée du programme, aucune donnée d'un article :
toutes les entrées sont des SUPPOSITIONS D'ILLUSTRATION, dites en tête de chaque bloc.
Seule la bibliothèque standard est employée. Rejouer : python3 -I calculs-signal-bruite-v1.py
"""
import math

RACINE2 = math.sqrt(2.0)


def Phi(x):
    """Fonction de répartition de la loi normale centrée réduite."""
    return 0.5 * math.erfc(-x / RACINE2)


def phi(x):
    """Densité de la loi normale centrée réduite."""
    return math.exp(-0.5 * x * x) / math.sqrt(2.0 * math.pi)


def Phi_inverse(p):
    """Quantile de la loi normale, par dichotomie (déterministe)."""
    bas, haut = -12.0, 12.0
    for _ in range(200):
        milieu = 0.5 * (bas + haut)
        if Phi(milieu) < p:
            bas = milieu
        else:
            haut = milieu
    return 0.5 * (bas + haut)


def grille(a, b, pas):
    """Points et poids de Simpson sur [a, b] ; le nombre d'intervalles est rendu pair."""
    n = int(round((b - a) / pas))
    if n % 2 == 1:
        n += 1
    h = (b - a) / n
    xs = [a + i * h for i in range(n + 1)]
    ws = []
    for i in range(n + 1):
        if i == 0 or i == n:
            ws.append(h / 3.0)
        elif i % 2 == 1:
            ws.append(4.0 * h / 3.0)
        else:
            ws.append(2.0 * h / 3.0)
    return xs, ws


XS, WS = grille(-12.0, 16.0, 0.004)


def tables(moyennes):
    """Pour chaque comportement de soupçon moyen m (écart type 1) : densité et survie sur la grille."""
    dens = [[phi(x - m) for x in XS] for m in moyennes]
    surv = [[1.0 - Phi(x - m) for x in XS] for m in moyennes]
    return dens, surv


def meilleur_de_n(parts, dens, surv, n):
    """Parts des comportements parmi les épisodes retenus quand on garde le MOINS suspect de n tirages
    indépendants de la politique courante. Loi exacte du minimum d'un mélange."""
    k = len(parts)
    nouvelles = [0.0] * k
    for i, w in enumerate(WS):
        s = 0.0
        for j in range(k):
            s += parts[j] * surv[j][i]
        puissance = s ** (n - 1)
        for j in range(k):
            nouvelles[j] += w * dens[j][i] * puissance
    nouvelles = [n * parts[j] * nouvelles[j] for j in range(k)]
    total = sum(nouvelles)
    return [v / total for v in nouvelles], total


def auroc_de(d):
    """Aire sous la courbe pour deux lois normales de même variance séparées de d écarts types."""
    return Phi(d / RACINE2)


def d_de_auroc(a):
    return RACINE2 * Phi_inverse(a)


def ligne(texte=""):
    print(texte)


def bloc_a():
    ligne("=" * 100)
    ligne("BLOC A — Le « meilleur de cinq » de la source est une fonction de la séparation des scores")
    ligne("Supposition : soupçon normal, écart type 1 ; honnête centré en 0, sous-rendement centré en d.")
    ligne("Lot : part f d'épisodes honnêtes. On retient le moins suspect de 5 tirages.")
    ligne("rapport = P(l'épisode retenu est honnête) / f ; plafond = (1 - (1-f)^5) / f (moniteur parfait).")
    ligne("-" * 100)
    ligne(f"{'d':>6} {'aire':>7} | {'f=0,10 P':>9} {'rapport':>8} | {'f=0,20 P':>9} {'rapport':>8} | {'f=0,50 P':>9} {'rapport':>8}")
    for d in (0.0, 0.25, 0.36, 0.50, 0.74, 1.00, 1.045, 1.50, 2.00, 3.00):
        dens, surv = tables([0.0, d])
        cellules = []
        for f in (0.10, 0.20, 0.50):
            p, _ = meilleur_de_n([f, 1.0 - f], dens, surv, 5)
            cellules.append((p[0], p[0] / f))
        ligne(f"{d:6.3f} {auroc_de(d):7.4f} | {cellules[0][0]:9.4f} {cellules[0][1]:8.3f} | "
              f"{cellules[1][0]:9.4f} {cellules[1][1]:8.3f} | {cellules[2][0]:9.4f} {cellules[2][1]:8.3f}")
    for f in (0.10, 0.20, 0.50):
        ligne(f"plafond du rapport à f = {f:.2f} : {(1.0 - (1.0 - f) ** 5) / f:.4f}")
    ligne("-" * 100)
    ligne("Inversion à f = 0,20 : quelle séparation d (et quelle aire) rend un rapport donné ?")
    for cible in (1.5, 2.0, 3.0):
        bas, haut = 0.0, 8.0
        for _ in range(60):
            milieu = 0.5 * (bas + haut)
            dens, surv = tables([0.0, milieu])
            p, _ = meilleur_de_n([0.20, 0.80], dens, surv, 5)
            if p[0] / 0.20 < cible:
                bas = milieu
            else:
                haut = milieu
        d = 0.5 * (bas + haut)
        ligne(f"rapport {cible:.1f} -> d = {d:.4f}, aire sous la courbe = {auroc_de(d):.4f}")
    ligne("Repère : aire de 0,77 (meilleur auditeur d'une des deux sources) -> d = "
          f"{d_de_auroc(0.77):.4f} dans ce modèle.")
    ligne()


def generations_jusqua(parts0, dens, surv, condition, maximum=400):
    parts = list(parts0)
    for g in range(1, maximum + 1):
        parts, _ = meilleur_de_n(parts, dens, surv, 5)
        if condition(parts):
            return g, parts
    return None, parts


def bloc_b():
    ligne("=" * 100)
    ligne("BLOC B — Deux comportements seulement : un signal faible suffit, il coûte des générations")
    ligne("Supposition : la politique suivante imite exactement les épisodes retenus (meilleur de 5 par le")
    ligne("soupçon), population infinie. Deux comportements : honnête (0) et sous-rendement visible (d).")
    ligne("Nombre de générations pour passer d'une part honnête f0 à 0,95 au moins.")
    ligne("-" * 100)
    ligne(f"{'d':>6} {'aire':>7} | {'f0=0,10':>8} {'f0=0,01':>8} {'f0=0,001':>9}")
    for d in (0.10, 0.25, 0.36, 0.50, 1.045, 2.00):
        dens, surv = tables([0.0, d])
        cellules = []
        for f0 in (0.10, 0.01, 0.001):
            g, _ = generations_jusqua([f0, 1.0 - f0], dens, surv, lambda p: p[0] >= 0.95, 5000)
            cellules.append(g)
        ligne(f"{d:6.3f} {auroc_de(d):7.4f} | {str(cellules[0]):>8} {str(cellules[1]):>8} {str(cellules[2]):>9}")
    dens, surv = tables([0.0, 0.5])
    g, parts = generations_jusqua([0.0, 1.0], dens, surv, lambda p: p[0] >= 0.95, 50)
    ligne(f"Témoin : f0 = 0 exactement, d = 0,5 -> part honnête après 50 générations = {parts[0]:.6f} "
          "(rien à renforcer : la sélection ne crée pas un comportement absent).")
    ligne()


def rappel_restant(parts, moyennes, seuil):
    """Rappel du moniteur, au seuil donné, sur ce qui reste de sous-rendement (comportements d'indice >= 1)."""
    masse = sum(parts[1:])
    if masse <= 0.0:
        return float("nan")
    return sum(parts[j] * (1.0 - Phi(seuil - moyennes[j])) for j in range(1, len(parts))) / masse


def bloc_c():
    ligne("=" * 100)
    ligne("BLOC C — Trois comportements : honnête, sous-rendement visible, sous-rendement discret")
    ligne("Supposition : soupçons moyens (0 ; 1,045 ; eps), écart type 1 ; même règle que le bloc B.")
    ligne("Le visible est séparé comme une aire de 0,77 ; le discret est séparé de eps seulement.")
    ligne("dommage = part des deux comportements de sous-rendement ; rappel = rappel du même moniteur,")
    ligne("à 5 % de fausses alertes, sur le sous-rendement qui reste.")
    ligne("-" * 100)
    seuil = Phi_inverse(0.95)
    cas = [
        ("C1 angle mort (eps = 0), mélange", 0.0, (0.10, 0.80, 0.10)),
        ("C2 angle mort, honnête rare au départ", 0.0, (0.001, 0.949, 0.05)),
        ("C3 angle mort, après rupture du pli", 0.0, (0.60, 0.35, 0.05)),
        ("C4 signal faible mais juste (eps = +0,2)", 0.2, (0.10, 0.80, 0.10)),
        ("C5 signal faible mais juste (eps = +0,2), honnête rare", 0.2, (0.001, 0.949, 0.05)),
        ("C6 signal qui préfère le discret (eps = -0,2)", -0.2, (0.89, 0.10, 0.01)),
    ]
    for nom, eps, depart in cas:
        moyennes = [0.0, 1.045, eps]
        dens, surv = tables(moyennes)
        parts = list(depart)
        ligne(nom)
        ligne(f"  {'génération':>10} {'honnête':>9} {'visible':>9} {'discret':>9} {'dommage':>9} "
              f"{'soupçon moyen':>14} {'rappel':>8}")
        for g in range(0, 201):
            if g in (0, 1, 2, 3, 5, 10, 20, 30, 50, 100, 200):
                moyen = sum(parts[j] * moyennes[j] for j in range(3))
                ligne(f"  {g:10d} {parts[0]:9.4f} {parts[1]:9.4f} {parts[2]:9.4f} {parts[1] + parts[2]:9.4f} "
                      f"{moyen:14.4f} {rappel_restant(parts, moyennes, seuil):8.4f}")
            parts, _ = meilleur_de_n(parts, dens, surv, 5)
        ligne(f"  rapport discret/(honnête+discret) au départ : {depart[2] / (depart[0] + depart[2]):.4f}")
    ligne("Lecture : avec eps = 0 le rapport discret/(honnête+discret) ne bouge pas ; le soupçon moyen")
    ligne("retombe au niveau honnête alors que le dommage reste à ce rapport, et le rappel tombe à 5 %.")
    ligne("Quand le dommage tend vers zéro, la colonne « rappel » est celle du dernier comportement de")
    ligne("sous-rendement, de masse presque nulle. Cas C6 : le dommage baisse d'abord (le visible part),")
    ligne("puis remonte jusqu'à 1 (le discret, mieux vu que l'honnête, prend toute la place).")
    ligne()


def bloc_d():
    ligne("=" * 100)
    ligne("BLOC D — Seuil de paiement : à partir de quel taux de détection le signal pousse du bon côté")
    ligne("Supposition : récompense R_h pour l'honnête, R_n pour un sous-rendement non détecté, R_d pour un")
    ligne("sous-rendement détecté ; détection indépendante de tout le reste, de probabilité t.")
    ligne("Le sous-rendement paie si t < t* = (R_n - R_h) / (R_n - R_d).")
    ligne("-" * 100)
    ligne(f"{'R_h':>6} {'R_n':>6} {'R_d':>6} {'t*':>8}   remarque")
    for rh, rn, rd, remarque in (
        (1.0, 2.0, -1.0, "valeurs publiées par un des voisins : seuil attendu 1/3"),
        (1.0, 1.0, -1.0, "aucun gain à tromper : tout taux positif suffit"),
        (1.0, 1.5, 0.0, "pénalité faible"),
        (1.0, 3.0, -1.0, "gain fort à tromper"),
        (0.0, 1.0, -9.0, "pénalité dix fois le gain"),
    ):
        t = (rn - rh) / (rn - rd)
        ligne(f"{rh:6.2f} {rn:6.2f} {rd:6.2f} {t:8.4f}   {remarque}")
    ligne("Témoin de la formule : à t = t* les deux espérances sont égales.")
    rh, rn, rd = 1.0, 2.0, -1.0
    t = (rn - rh) / (rn - rd)
    ligne(f"  espérance du sous-rendement à t* : {(1 - t) * rn + t * rd:.10f} ; honnête : {rh:.10f}")
    ligne()


def bloc_e():
    ligne("=" * 100)
    ligne("BLOC E — Le bruit se paie en épisodes, pas en signe")
    ligne("Supposition : deux groupes d'épisodes de même taille, écart type 1, différence de moyenne d.")
    ligne("Taille par groupe pour voir la différence (bilatéral 5 %, puissance 80 %) : 2 * ((1,96 + 0,8416)/d)^2.")
    ligne("-" * 100)
    z = Phi_inverse(0.975) + Phi_inverse(0.80)
    ligne(f"{'aire':>6} {'d':>8} {'épisodes par groupe':>20}")
    for a in (0.55, 0.60, 0.65, 0.70, 0.77, 0.90):
        d = d_de_auroc(a)
        ligne(f"{a:6.2f} {d:8.4f} {math.ceil(2.0 * (z / d) ** 2):20d}")
    ligne()


def bloc_f():
    ligne("=" * 100)
    ligne("BLOC F — Puissance de la lecture proposée (corrélation entre score et dommage)")
    ligne("Transformation de Fisher : n = ((1,96 + 0,8416) / atanh(rho))^2 + 3 épisodes pour distinguer")
    ligne("une corrélation rho de zéro (bilatéral 5 %, puissance 80 %).")
    ligne("-" * 100)
    z = Phi_inverse(0.975) + Phi_inverse(0.80)
    ligne(f"{'rho':>6} {'épisodes':>10}")
    for rho in (0.10, 0.14, 0.15, 0.20, 0.30, 0.46, 0.55):
        ligne(f"{rho:6.2f} {math.ceil((z / math.atanh(rho)) ** 2 + 3):10d}")
    ligne("Intervalle à 95 % autour de rho = 0,15 selon le nombre n d'épisodes :")
    for n in (50, 100, 200, 400, 800):
        centre = math.atanh(0.15)
        demi = Phi_inverse(0.975) / math.sqrt(n - 3)
        ligne(f"  n = {n:4d} : [{math.tanh(centre - demi):+.3f} ; {math.tanh(centre + demi):+.3f}]")
    ligne("Même intervalle autour de rho = 0,30 (ce qui réfuterait la prédiction « au plus 0,15 ») :")
    for n in (100, 200, 400, 800):
        centre = math.atanh(0.30)
        demi = Phi_inverse(0.975) / math.sqrt(n - 3)
        ligne(f"  n = {n:4d} : [{math.tanh(centre - demi):+.3f} ; {math.tanh(centre + demi):+.3f}]")
    ligne()


def bloc_g():
    ligne("=" * 100)
    ligne("BLOC G — De la corrélation au « gain du meilleur de cinq » sur le dommage")
    ligne("Supposition : score et dommage de loi normale jointe, corrélation rho ; dommage de moyenne mu et")
    ligne("d'écart type sigma (cv = sigma/mu). On retient le moins suspect de 5 : le dommage moyen du retenu")
    ligne("vaut mu - rho * sigma * E[max de 5 normales]. gain = baisse relative du dommage = rho * cv * E[max].")
    ligne("-" * 100)
    emax = sum(w * x * 5.0 * phi(x) * Phi(x) ** 4 for x, w in zip(XS, WS))
    ligne(f"E[max de 5 normales centrées réduites] = {emax:.6f}")
    ligne(f"{'rho':>6} | {'gain, cv = 0,5':>15} {'gain, cv = 1,0':>15}")
    for rho in (0.00, 0.14, 0.15, 0.30, 0.46, 0.55):
        ligne(f"{rho:6.2f} | {rho * 0.5 * emax:15.4f} {rho * 1.0 * emax:15.4f}")
    ligne()


def bloc_h():
    ligne("=" * 100)
    ligne("BLOC H — Témoins de l'identité centrale : la réponse au premier ordre est la covariance")
    ligne("Politique à comportements discrets k, de parts p_k, score moyen s_k (grand = bien vu), dommage D_k.")
    ligne("Entraînement idéalisé : p_k devient proportionnel à p_k * exp(eta * s_k).")
    ligne("Identité : la dérivée en eta = 0 du dommage moyen vaut Cov(s, D).")
    ligne("-" * 100)

    def dommage_moyen(parts, scores, dommages, eta):
        poids = [p * math.exp(eta * s) for p, s in zip(parts, scores)]
        total = sum(poids)
        return sum(w * d for w, d in zip(poids, dommages)) / total

    def covariance(parts, scores, dommages):
        ms = sum(p * s for p, s in zip(parts, scores))
        md = sum(p * d for p, d in zip(parts, dommages))
        return sum(p * (s - ms) * (d - md) for p, s, d in zip(parts, scores, dommages))

    objets = [
        ("vrai par construction : le score baisse quand le dommage monte",
         [0.2, 0.5, 0.3], [0.0, -1.0, -0.3], [0.0, 1.0, 1.0]),
        ("faux par construction : saboteur constant, même dommage partout, scores variés",
         [0.3, 0.4, 0.3], [-1.5, -0.5, 0.0], [1.0, 1.0, 1.0]),
        ("faux à terme : le score préfère le dommage discret à l'honnête, un visible est là au départ",
         [0.89, 0.10, 0.01], [0.0, -1.0, 0.2], [0.0, 1.0, 1.0]),
        ("faux par construction : le score préfère le dommage discret à l'honnête, sans visible",
         [0.90, 0.10], [0.0, 0.2], [0.0, 1.0]),
    ]
    eta = 1e-6
    for nom, parts, scores, dommages in objets:
        d0 = dommage_moyen(parts, scores, dommages, 0.0)
        derivee = (dommage_moyen(parts, scores, dommages, eta) - dommage_moyen(parts, scores, dommages, -eta)) / (2 * eta)
        cov = covariance(parts, scores, dommages)
        d5 = dommage_moyen(parts, scores, dommages, 5.0)
        ligne(nom)
        ligne(f"  dommage moyen au départ : {d0:.6f} ; dérivée numérique : {derivee:+.6f} ; covariance : {cov:+.6f} ; "
              f"dommage moyen à eta = 5 : {d5:.6f}")
    ligne("Chemin du troisième témoin (dommage moyen selon eta) :")
    parts, scores, dommages = objets[2][1], objets[2][2], objets[2][3]
    ligne("  " + " ; ".join(f"eta = {e:g} : {dommage_moyen(parts, scores, dommages, float(e)):.4f}"
                            for e in (0, 1, 2, 5, 10, 15, 20, 25, 30, 40)))
    ligne("Constat : dérivée = covariance dans les quatre cas. Négative au premier, nulle au deuxième,")
    ligne("positive au quatrième. Au troisième elle est NÉGATIVE alors que le dommage finit par monter :")
    ligne("avant le calcul, l'auteur l'attendait positive. La lecture au premier ordre ne voit pas un")
    ligne("comportement discret encore rare ; elle peut réfuter, elle ne peut pas confirmer.")
    ligne()


def principal():
    ligne("Calculs de la note « le signal bruité pourrait suffire pour entraîner » (v1)")
    ligne("Lois exactes, intégration de Simpson sur grille fixe de -12 à 16 au pas de 0,004 ; aucun tirage.")
    ligne("Toutes les entrées sont des suppositions d'illustration ; aucun chiffre n'est une mesure.")
    ligne()
    bloc_a()
    bloc_b()
    bloc_c()
    bloc_d()
    bloc_e()
    bloc_f()
    bloc_g()
    bloc_h()
    ligne("Fin.")


if __name__ == "__main__":
    principal()
