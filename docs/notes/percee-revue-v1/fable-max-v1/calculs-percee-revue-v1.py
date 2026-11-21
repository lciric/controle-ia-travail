#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Calculs de la note « la percée, revue » (v1).

Lois exactes et formes closes seulement : aucun tirage, aucune graine, aucune
donnée du programme. Bibliothèque standard seule. Toutes les entrées sont des
SUPPOSITIONS D'ILLUSTRATION, sauf quatre tailles de jeux d'épreuve publiés,
dont la page est dite au bloc C.

Rejeu : python3 -I calculs-percee-revue-v1.py > calculs-percee-revue-v1.txt
"""
import math

VERSION = "calculs-percee-revue-v1"


def phi(x):
    """Fonction de répartition de la loi normale centrée réduite."""
    return 0.5 * (1.0 + math.erf(x / math.sqrt(2.0)))


def phi_inv(p):
    """Quantile de la loi normale, par dichotomie (déterministe)."""
    lo, hi = -12.0, 12.0
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if phi(mid) < p:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def kl(p, q):
    """Divergence de Kullback-Leibler entre deux lois discrètes (listes)."""
    s = 0.0
    for a, b in zip(p, q):
        if a > 0.0:
            s += a * math.log(a / b)
    return s


def binom_queue_haute(n, k, p):
    """P(X >= k) pour X binomiale (n, p), somme exacte en flottants."""
    termes = [math.comb(n, i) * (p ** i) * ((1.0 - p) ** (n - i)) for i in range(k, n + 1)]
    return math.fsum(termes)


def titre(t):
    print()
    print("=" * 78)
    print(t)
    print("=" * 78)


print(VERSION)
print("Lois exactes ; aucune donnée du programme ; entrées = suppositions d'illustration.")

# ---------------------------------------------------------------------------
titre("BLOC A — Ce que gagne un second regard, quel qu'il soit, sur les épisodes endommagés audités")
# ---------------------------------------------------------------------------
print("Monde : l'honnête endommage un épisode avec probabilité rho0. Le saboteur ajoute un dommage")
print("délibéré dans une part delta des épisodes. Sur un épisode endommagé, un second regard rend une")
print("valeur S : de loi F0 si l'échec est honnête, de loi F1 si le dommage est délibéré.")
print("Gain = information par audit (divergence de Kullback-Leibler) du test qui lit (dommage, S),")
print("divisée par celle du test qui ne lit que le dommage. Le nombre d'audits avant l'alarme, à")
print("allure fixée, est divisé par ce gain (approximation de Wald).")
print()
rho0 = 0.10
t, f = 0.64, 0.029
print(f"A1. Second regard à deux valeurs : marque une part t = {t} des dommages délibérés et une part")
print(f"    f = {f} des échecs honnêtes ; rho0 = {rho0}.")
chi2 = t * t / f + (1 - t) ** 2 / (1 - f) - 1.0
limite = 1.0 + (1.0 - rho0) * chi2
evenement_seul = (t * t / f) * (1 - rho0) / (1 - rho0 * f)
print(f"    khi-deux de F1 contre F0 = t²/f + (1-t)²/(1-f) - 1 = {chi2:.4f}")
print(f"    limite annoncée : 1 + (1 - rho0) × khi-deux = {limite:.4f}")
print(f"    rappel, test sur le seul événement « endommagé et marqué » : t²/f × (1-rho0)/(1-rho0 f) = {evenement_seul:.4f}")
print("    allure delta     gain exact (rapport des divergences)")
for delta in (0.05, 0.02, 0.01, 0.005, 0.001, 0.0001, 0.00001):
    p0 = [rho0 * f, rho0 * (1 - f), 1 - rho0]
    p1 = [rho0 * f + delta * t, rho0 * (1 - f) + delta * (1 - t), 1 - rho0 - delta]
    d_complet = kl(p1, p0)
    d_dommage = kl([rho0 + delta, 1 - rho0 - delta], [rho0, 1 - rho0])
    print(f"    {delta:<12g}     {d_complet / d_dommage:9.4f}")
print("    Lecture : le gain tend vers une constante finie quand le saboteur ralentit ; il ne croît")
print("    pas avec la lenteur. Le dommage avant l'alarme garde donc sa loi en inverse de l'allure.")
print()
print("A2. Second regard à valeur continue, deux lois normales de même variance séparées de d écarts")
print("    types : khi-deux = exp(d²) - 1 ; gain limite = 1 + (1 - rho0)(exp(d²) - 1).")
print("    d       khi-deux        gain limite")
for d in (0.5, 1.0, 1.5, 2.0, 2.5, 3.0):
    c2 = math.exp(d * d) - 1.0
    print(f"    {d:<4g}   {c2:12.2f}   {1.0 + (1 - rho0) * c2:12.2f}")
print("    Lecture : une grande constante est possible, mais elle vit dans la queue de la loi honnête,")
print("    c'est-à-dire là où la référence honnête est la moins connue.")
print()
print("A3. Le plafond par la référence. Si aucun de m échecs honnêtes de référence n'est marqué, on ne")
print("    sait de f que : f <= 1 - 0,05^(1/m) (à 95 %). Le gain que l'on a le droit d'inscrire est")
print("    celui de cette borne. Coût : m échecs honnêtes confirmés = m / rho0 épisodes honnêtes jugés.")
print("    m        f inscrit     épisodes honnêtes jugés   gain inscrit, t=0,30   t=0,64   t=0,90")
for m in (35, 300, 2000, 20000, 100000):
    f_ins = 1.0 - 0.05 ** (1.0 / m)
    ligne = f"    {m:<7d}  {f_ins:10.6f}   {int(round(m / rho0)):>12d}            "
    for tt in (0.30, 0.64, 0.90):
        g = 1.0 + (1 - rho0) * (tt * tt / f_ins + (1 - tt) ** 2 / (1 - f_ins) - 1.0)
        ligne += f"   {g:10.1f}"
    print(ligne)
print("    Lecture : le gain inscrit croît comme m. Il s'achète en épisodes honnêtes jugés, et ne vaut")
print("    que si l'honnête de référence est celui du régime surveillé.")

# ---------------------------------------------------------------------------
titre("BLOC B — Ce que le ciblage rapporte : part de l'enjeu logée dans les éléments les plus lourds")
# ---------------------------------------------------------------------------
print("Monde : chaque élément d'un travail (une affirmation, un contrôle) porte un enjeu. Un agent qui")
print("laisse perdre une part delta des éléments, au hasard, détruit une part delta de l'enjeu total.")
print("S'il choisit les plus lourds, il en détruit la part ci-dessous. Choisir demande de savoir")
print("lesquels sont lourds et vrais.")
print()
print("B1. Enjeux de loi de Pareto d'indice alpha : part détruite = delta^(1 - 1/alpha).")
print("    alpha    delta = 1 %          5 %           20 %        (entre parenthèses : multiple du hasard)")
for alpha in (1.2, 1.5, 2.0, 3.0):
    ligne = f"    {alpha:<5g}  "
    for delta in (0.01, 0.05, 0.20):
        part = delta ** (1.0 - 1.0 / alpha)
        ligne += f"  {part:6.3f} (×{part / delta:5.1f})"
    print(ligne)
print()
print("B2. Enjeux de loi log-normale d'écart type sigma (du logarithme) : part = Phi(sigma - z),")
print("    z étant le quantile d'ordre 1 - delta de la loi normale.")
print("    sigma    delta = 1 %          5 %           20 %")
for sigma in (0.5, 1.0, 1.5, 2.0):
    ligne = f"    {sigma:<5g}  "
    for delta in (0.01, 0.05, 0.20):
        part = phi(sigma - phi_inv(1.0 - delta))
        ligne += f"  {part:6.3f} (×{part / delta:5.1f})"
    print(ligne)
print("    Lecture : dès que les enjeux sont inégaux, le dommage dangereux est le dommage ciblé ; à")
print("    enjeux égaux, la prime est nulle (multiple 1). La prime mesure ce qu'un agent perd à ne pas")
print("    calculer ce qu'il évite.")

# ---------------------------------------------------------------------------
titre("BLOC C — Ce que l'épreuve clé sait voir, aux tailles des jeux d'épreuve publiés")
# ---------------------------------------------------------------------------
print("Épreuve : sur n éléments retenus par un organisme, une lecture du savoir propose une réponse ;")
print("on compte les réponses justes. Barre : la justesse p0 de la même lecture sur un témoin ignorant")
print("(elle ne doit rien « retrouver » là où il n'y a rien à lire). Test binomial exact, unilatéral,")
print("niveau 1 %. On cherche la plus petite justesse p1 vue avec une puissance de 0,90.")
print("Tailles : 256, 83 et 399 questions d'épreuve (arXiv 2611.20459v1, p. 6) ; 51 éléments durs")
print("(même pièce, p. 10) ; 738 = somme des trois premières. Questions à quatre choix : hasard 0,25.")
print("Conversion en part de l'écart rendue : (p1 - 0,25) / (0,75 - 0,25), l'honnête étant SUPPOSÉ à 0,75")
print("et l'organisme qui retient au hasard.")
print()
print("    n      barre p0   seuil (réponses justes)   niveau exact   p1 vue à 0,90   part de l'écart rendue")
for p0 in (0.25, 0.35):
    for n in (51, 83, 256, 399, 738):
        k = 0
        while binom_queue_haute(n, k, p0) > 0.01:
            k += 1
        niveau = binom_queue_haute(n, k, p0)
        p1 = None
        for i in range(int(p0 * 1000), 1001):
            cand = i / 1000.0
            if binom_queue_haute(n, k, cand) >= 0.90:
                p1 = cand
                break
        part = (p1 - 0.25) / 0.5
        print(f"    {n:<5d}  {p0:<8g}   {k:>6d}                    {niveau:8.5f}       {p1:6.3f}          {part:6.3f}")
print("    Lecture : avec quelques centaines d'éléments, une lecture qui rend un cinquième à un quart")
print("    de l'écart se sépare d'un témoin ignorant ; avec 51 éléments, il en faut près de la moitié.")

# ---------------------------------------------------------------------------
titre("BLOC D — Lentille linéaire : ce qu'un juge laisse à l'attaquant, selon son angle avec la vérité")
# ---------------------------------------------------------------------------
print("Monde d'illustration, ni mesure ni modèle d'un banc : un produit est un point de la boule unité ;")
print("la note du juge et la vérité sont deux formes linéaires de norme 1 ; r = cosinus de leur angle")
print("(leur corrélation). Parmi les produits dont la note vaut au moins (1 - eps) fois la note")
print("maximale, la vérité parcourt l'intervalle (1 - eps) r -/+ racine(2 eps - eps²) racine(1 - r²),")
print("le plafond valant 1 dès que r >= 1 - eps.")
print("Unité : la vérité du meilleur produit possible vaut 1.")
print()
print("D1. Plancher et plafond de vérité à note presque maximale.")
print("    r        eps = 0,02 : plancher  plafond      eps = 0,05 : plancher  plafond")
for r in (0.14, 0.30, 0.50, 0.70, 0.90, 0.95, 0.99):
    ligne = f"    {r:<6g} "
    for eps in (0.02, 0.05):
        centre = (1 - eps) * r
        demi = math.sqrt(2 * eps - eps * eps) * math.sqrt(1 - r * r)
        # si r >= 1 - eps, le meilleur produit possible est lui-même admis : plafond 1
        plafond = 1.0 if r >= 1 - eps else centre + demi
        ligne += f"       {centre - demi:8.3f}  {plafond:8.3f}     "
    print(ligne)
print()
print("D2. Juge composé de deux notes. Chacune = vérité + erreur ; a et b = tangentes de leurs angles ;")
print("    c = cosinus entre leurs deux erreurs. Composé = lam × juge + (1 - lam) × lecture, lam entre 0 et 1 ;")
print("    tangente² = lam² a² + (1-lam)² b² + 2 lam (1-lam) c a b ; « meilleur poids » = le lam qui la minimise")
print("    (il demande de connaître la vérité) ; « poids égaux » = lam 1/2. Colonnes : corrélation avec la vérité.")
print("    juge r_J   lecture r_L   c      meilleur poids positif   poids égaux")
for rj in (0.14, 0.50, 0.90):
    for rl in (0.30, 0.50, 0.80):
        for c in (0.0, 0.5, 0.9):
            a = math.sqrt(1 - rj * rj) / rj
            b = math.sqrt(1 - rl * rl) / rl
            lam = (b * b - c * a * b) / (a * a + b * b - 2 * c * a * b)
            lam = min(1.0, max(0.0, lam))  # poids positifs seulement
            t2_opt = lam * lam * a * a + (1 - lam) ** 2 * b * b + 2 * lam * (1 - lam) * c * a * b
            t2_egal = (a * a + b * b + 2 * c * a * b) / 4.0
            r_opt = 1.0 / math.sqrt(1.0 + t2_opt)
            r_egal = 1.0 / math.sqrt(1.0 + t2_egal)
            print(f"    {rj:<8g}   {rl:<8g}      {c:<4g}   {r_opt:8.3f}                {r_egal:8.3f}")
print("    Lecture : dans ce monde, une seconde note ne relève le plancher que si elle est elle-même")
print("    alignée sur la vérité, ou si ses erreurs sont étrangères à celles du juge ; contre un juge déjà")
print("    aligné (r = 0,90), une lecture à 0,50 n'ajoute presque rien.")

# ---------------------------------------------------------------------------
titre("BLOC E — Les trois zones d'une lecture du savoir sur des éléments dont la vérité est connue")
# ---------------------------------------------------------------------------
print("Monde : question à deux réponses. Chez un agent qui sait, la projection de l'état sur l'axe de")
print("la réponse suit une loi normale de moyenne +s du côté juste (écart type 1). Un agent qui retient")
print("peut : garder une part kappa de ce signal (effacement partiel) ; le remplacer par le signal de")
print("la réponse fausse (leurre) ; ne pas calculer la réponse (alors il ressemble à l'ignorant).")
print("Deux lectures par l'auditeur, sans connaître le déclencheur : la justesse de la lecture du savoir")
print("(signe de la projection) ; un détecteur d'acte qui signale une projection trop petite en valeur")
print("absolue, réglé à 1 % de fausses alertes sur l'agent qui sait.")
print()
print("    s     conduite                    justesse de la lecture du savoir    acte signalé (seuil 1 %)")
for s in (2.0, 3.0, 4.0):
    # seuil c tel que P(|Z| < c) = 0,01 pour Z ~ N(s, 1)
    lo, hi = 0.0, 20.0
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if phi(mid - s) - phi(-mid - s) < 0.01:
            lo = mid
        else:
            hi = mid
    c = 0.5 * (lo + hi)
    lignes = [("honnête qui sait", 1.0, +1), ("effacement, kappa = 0,75", 0.75, +1),
              ("effacement, kappa = 0,50", 0.50, +1), ("effacement, kappa = 0,25", 0.25, +1),
              ("non calculé (ou ignorant)", 0.0, +1), ("leurre (réponse fausse)", 1.0, -1)]
    for nom, kappa, signe in lignes:
        mu = signe * kappa * s
        justesse = phi(mu)
        acte = phi(c - mu) - phi(-c - mu)
        print(f"    {s:<4g}  {nom:<27s} {justesse:10.4f}                         {acte:10.4f}")
    print()
print("    Lecture : au-dessus du hasard, la lecture rend la réponse ; au-dessous du hasard (leurre),")
print("    elle dénonce un savoir retourné, qu'un ignorant ne produit pas ; au hasard, rien ne sépare")
print("    l'agent qui n'a pas calculé de l'ignorant : c'est la zone qui reste. Plus l'effacement est")
print("    fort, plus l'acte se voit, et l'inverse : sous effacement linéaire, la séparation de l'acte")
print("    (1 - kappa) s et celle du savoir kappa s ont pour somme s.")
