"""Calculs cités par `conception-branchement-experimentateurs-tests-de-mort-v1.md` (même dossier).

Ce que c'est : des lois exactes (statistiques d'ordre, loi binomiale, loi normale, programmation dynamique
sur une suite de Bernoulli) et des intégrales numériques à une dimension. Aucune donnée du programme n'est
lue. Aucun tirage aléatoire, donc aucune graine. Ce n'est pas une expérience : c'est la vérité plantée de
quatre mondes d'illustration (blocs A à C, D, E, F), telle qu'un test de mort devrait la retrouver ; le bloc G
reprend les mêmes lois aux valeurs que propose la conception de la course « seuil et moniteurs ».

Les valeurs marquées « proposition » (nombre de lots R, niveau de mort, horizon T, corrélation par famille)
sont des valeurs d'illustration du concepteur, à geler ou à changer au préenregistrement court ; elles ne
sont tirées d'aucune mesure.

Lancer : python calculs-conception-tests-de-mort-v1.py > calculs-conception-tests-de-mort-v1.txt
"""
from math import log, sqrt

from scipy.integrate import quad
from scipy.stats import beta, binom, norm

ALPHA = 0.01      # taux de fausses alertes visé (faits de la question)
DELTA = 0.05      # un certificat « à 95 % »
R_LOTS = 400      # proposition : nombre de lots d'étalonnage tirés par monde
NIVEAU_MORT = 0.001  # proposition : niveau du test exact qui tue un engagement


def couverture(n, k, alpha=ALPHA):
    """P(taux réel du k-ième plus grand de n scores honnêtes indépendants et continus <= alpha).
    Le taux réel suit Beta(k, n - k + 1)."""
    return beta(k, n - k + 1).cdf(alpha)


def seuil_de_mort(r, p0, niveau=NIVEAU_MORT):
    """Plus grand c tel que P(Bin(r, p0) <= c) <= niveau : l'engagement « couverture >= p0 » meurt si le
    nombre de lots conformes est <= c."""
    c = -1
    while binom(r, p0).cdf(c + 1) <= niveau:
        c += 1
    return c


def p_tue(r, c, p):
    return binom(r, p).cdf(c)


print("A. Monde 1, unités indépendantes : couverture exacte P(taux réel <= 1 %) des règles témoins")
temoins = (("3e plus grand de 300", 300, 3), ("plus grand de 299", 299, 1), ("plus grand de 300", 300, 1),
           ("plus grand de 368", 368, 1), ("5e plus grand de 1000", 1000, 5), ("6e plus grand de 1000", 1000, 6),
           ("10e plus grand de 1000", 1000, 10))
for nom, n, k in temoins:
    print(f"   {nom:24s} : couverture {couverture(n, k):.4f}, taux réel moyen {k / (n + 1):.5f}")

print("A bis. Monde 1 : la même règle sous l'engagement « valide en moyenne » (taux réel moyen <= 1 %)")
for nom, n, k in (("3e plus grand de 300", 300, 3), ("4e plus grand de 300", 300, 4)):
    loi = beta(k, n - k + 1)
    print(f"   {nom:24s} : taux réel moyen {loi.mean():.5f} ; écart type de la moyenne sur {R_LOTS} lots "
          f"{loi.std() / sqrt(R_LOTS):.5f} ; écart à 1 % en écarts types {(loi.mean() - ALPHA) / (loi.std() / sqrt(R_LOTS)):+.1f}")

print(f"B. Le test de mort d'un engagement « certifié à 95 % », R = {R_LOTS} lots, niveau de mort {NIVEAU_MORT} (propositions)")
for r in (200, R_LOTS, 1000):
    c = seuil_de_mort(r, 1 - DELTA)
    ligne = f"   R={r:4d} : meurt si lots conformes <= {c} ; niveau réalisé {p_tue(r, c, 1 - DELTA):.5f}"
    for nom, n, k in (temoins[0], temoins[1], temoins[5]):
        ligne += f" ; P(tue « {nom} ») = {p_tue(r, c, couverture(n, k)):.4f}"
    print(ligne)
    # angle mort : plus grande couverture vraie encore tuée neuf fois sur dix
    bas, haut = 0.5, 1 - DELTA
    for _ in range(60):
        milieu = (bas + haut) / 2
        if p_tue(r, c, milieu) >= 0.9:
            bas = milieu
        else:
            haut = milieu
    print(f"            angle mort : une couverture vraie au-dessus de {bas:.4f} est tuée moins de neuf fois sur dix")

print("C. Monde 1, puissance contre le signal planté (binormal à variances égales ; aire sous la courbe plantée)")


def rappel_moyen(d, n, k):
    """Espérance du rappel au seuil pris au k-ième plus grand de n : le taux réel a suit Beta(k, n-k+1),
    le rappel vaut Phi(d - z_{1-a})."""
    loi = beta(k, n - k + 1)
    valeur, _ = quad(lambda a: norm.cdf(d - norm.isf(a)) * loi.pdf(a), 0.0, 1.0, limit=400)
    return valeur


for aire in (0.69, 0.80, 0.95):
    d = sqrt(2) * norm.ppf(aire)
    exact = norm.cdf(d - norm.isf(ALPHA))
    print(f"   aire {aire:.2f} : rappel au taux réel de 1 % exactement {exact:.3f} ; plus grand de 299 : "
          f"{rappel_moyen(d, 299, 1):.3f} ; plus grand de 368 : {rappel_moyen(d, 368, 1):.3f} ; "
          f"3e plus grand de 300 : {rappel_moyen(d, 300, 3):.3f} ; ne jamais alerter : 0.000")

print("D. Monde 2, changement de régime (scores honnêtes gaussiens, décalage de la moyenne au service)")
z99 = norm.isf(ALPHA)
decalage = z99 - norm.isf(3 * ALPHA)
print(f"   décalage qui triple un taux réel de 1 % : {decalage:.4f} écart type")
for nom, n, k in (temoins[1], temoins[3], temoins[4]):
    a_limite = norm.sf(z99 + decalage)  # le seuil doit dépasser z99 + décalage pour rester à 1 % au service
    c_mort = seuil_de_mort(R_LOTS, 1 - DELTA)
    print(f"   {nom:24s} : couverture à l'étalonnage {couverture(n, k):.4f} ; au service, après décalage, "
          f"{couverture(n, k, a_limite):.4f} ; P(tue, R = {R_LOTS}) = {p_tue(R_LOTS, c_mort, couverture(n, k, a_limite)):.4f}")

print("E. Monde 3, grappes par famille (score = effet de famille + bruit, variance totale 1 ; proposition : corrélation 0,2)")


def couverture_grappes(familles, par_famille, rho):
    """P(le plus grand des scores du lot >= z99), familles neuves au service (loi marginale normale réduite).
    Intégrale exacte à une dimension sur l'effet de famille."""
    if rho == 0:
        return 1 - norm.cdf(z99) ** (familles * par_famille)
    s_u, s_e = sqrt(rho), sqrt(1 - rho)
    moyenne, _ = quad(lambda u: norm.cdf((z99 - s_u * u) / s_e) ** par_famille * norm.pdf(u), -10, 10, limit=400)
    return 1 - moyenne ** familles


for familles, par_famille in ((300, 1), (30, 10), (10, 30), (3, 100)):
    n = familles * par_famille
    cg = couverture_grappes(familles, par_famille, 0.2)
    print(f"   {familles:3d} familles x {par_famille:3d} épisodes (n = {n}) : couverture du « plus grand du lot » "
          f"{cg:.4f} ; P(tue, R = {R_LOTS}) = {p_tue(R_LOTS, seuil_de_mort(R_LOTS, 1 - DELTA), cg):.4f} ; "
          f"taille effective n / (1 + (m - 1) rho) = {n / (1 + (par_famille - 1) * 0.2):.1f}")

print("F. Monde de déploiement : alerte entre épisodes sur une suite de Bernoulli (taux d'alerte honnête q = 0,20 ; horizon T = 300 ; propositions)")


def suite(q, p_vrai, horizon, regle):
    """Programmation dynamique exacte sur (épisode t, nombre d'alertes k). `regle(t, k)` dit si la procédure
    sonne. Rend (probabilité de sonner avant l'horizon, épisode moyen de la sonnerie quand elle a lieu)."""
    masse = {0: 1.0}
    sonne, somme_t = 0.0, 0.0
    for t in range(1, horizon + 1):
        suivante = {}
        for k, m in masse.items():
            for x, px in ((1, p_vrai), (0, 1 - p_vrai)):
                kk = k + x
                if regle(t, kk):
                    sonne += m * px
                    somme_t += m * px * t
                else:
                    suivante[kk] = suivante.get(kk, 0.0) + m * px
        masse = suivante
    return sonne, (somme_t / sonne if sonne > 0 else float("nan"))


Q, P1, T = 0.20, 0.30, 300
_valeurs_p = {}


def test_repete(t, k):
    """Témoin faux : test binomial exact unilatéral à 1 %, rejoué à chaque épisode, sans correction."""
    if (t, k) not in _valeurs_p:
        _valeurs_p[(t, k)] = binom(t, Q).sf(k - 1)
    return _valeurs_p[(t, k)] < ALPHA


def pari(t, k):
    """Témoin vrai : rapport de vraisemblance de Bernoulli (q contre p1), sonne quand il passe 1 / alpha."""
    return k * log(P1 / Q) + (t - k) * log((1 - P1) / (1 - Q)) >= log(1 / ALPHA)


for nom, regle in (("test répété sans correction", test_repete), ("pari de Bernoulli, seuil 100", pari)):
    fausse, _ = suite(Q, Q, T, regle)
    ligne = f"   {nom:28s} : fausse alerte par déploiement {fausse:.4f}"
    for p in (0.25, 0.30, 0.40):
        puissance, delai = suite(Q, p, T, regle)
        ligne += f" ; saboteur à {p:.2f} : sonne {puissance:.3f}, épisode moyen {delai:.0f}"
    print(ligne)
c_haut = 0
while binom(R_LOTS, ALPHA).sf(c_haut - 1) > NIVEAU_MORT:
    c_haut += 1
print(f"   règle de mort de l'engagement « fausse alerte par déploiement <= 1 % », {R_LOTS} suites honnêtes : meurt si "
      f"au moins {c_haut} suites sonnent (niveau réalisé {binom(R_LOTS, ALPHA).sf(c_haut - 1):.5f})")
for nom, regle in (("test répété sans correction", test_repete), ("pari de Bernoulli, seuil 100", pari)):
    fausse, _ = suite(Q, Q, T, regle)
    print(f"      P(tue « {nom} ») = {binom(R_LOTS, fausse).sf(c_haut - 1):.4f}")
derive, _ = suite(Q, 0.25, T, pari)
print(f"   changement de régime : si le taux d'alerte honnête dérive de 0,20 à 0,25, le pari sonne à tort {derive:.3f}")

print("G. Aux valeurs proposées par la conception de la course « seuil et moniteurs » (n = 200 et 400 ; R = 2 000 tirages ; mort si la borne exacte à 99 % sort de la garantie)")
for nom, n, k in (("plus grand de 200", 200, 1), ("2e plus grand de 200", 200, 2), ("plus grand de 400", 400, 1),
                  ("4e plus grand de 400", 400, 4)):
    print(f"   {nom:24s} : couverture {couverture(n, k):.4f}, taux réel moyen {k / (n + 1):.5f}")
r_course, niveau_course = 2000, 0.005
c = seuil_de_mort(r_course, 1 - DELTA, niveau_course)
print(f"   engagement « certifié à 95 % », R = {r_course}, niveau unilatéral {niveau_course} : meurt si lots conformes <= {c} ; "
      f"niveau réalisé {p_tue(r_course, c, 1 - DELTA):.5f}")
for nom, n, k in (("plus grand de 200", 200, 1), ("plus grand de 400", 400, 1), ("6e plus grand de 1000", 1000, 6)):
    print(f"      P(tue « {nom} ») = {p_tue(r_course, c, couverture(n, k)):.4f}")
bas, haut = 0.5, 1 - DELTA
for _ in range(60):
    milieu = (bas + haut) / 2
    if p_tue(r_course, c, milieu) >= 0.9:
        bas = milieu
    else:
        haut = milieu
print(f"      angle mort : une couverture vraie au-dessus de {bas:.4f} est tuée moins de neuf fois sur dix")
