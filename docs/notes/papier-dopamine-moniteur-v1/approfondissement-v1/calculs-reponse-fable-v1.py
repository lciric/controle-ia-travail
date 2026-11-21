"""Calculs cités par `reponse-fable-v1.md` (bras « papier dopamine », réglage du seuil à 1 %).

Aucune donnée du programme n'est lue : ce sont des lois exactes (statistiques d'ordre,
loi binomiale) et deux illustrations sous hypothèse écrite (modèle binormal à variances
égales ; taux d'alerte supposés). Aucun tirage aléatoire, donc aucune graine.

Lancer : python calculs-reponse-fable-v1.py > calculs-reponse-fable-v1.txt
"""
from math import ceil, exp, log, sqrt

from scipy.stats import beta, binom, norm

ALPHA = 0.01
DELTA = 0.05


def intervalle_taux_realise(n, k):
    """Seuil = k-ième plus grand de n scores honnêtes indépendants et continus.
    Son taux de fausses alertes réel suit Beta(k, n - k + 1)."""
    loi = beta(k, n - k + 1)
    return loi.mean(), loi.std(), loi.ppf(0.025), loi.ppf(0.975)


def rang_certifie(n, alpha=ALPHA, delta=DELTA):
    """Plus grand rang r tel que P(taux réel du r-ième plus grand <= alpha) >= 1 - delta."""
    meilleur = 0
    for r in range(1, n + 1):
        if beta(r, n - r + 1).cdf(alpha) >= 1 - delta:
            meilleur = r
        else:
            break
    return meilleur


print("A. Taux de fausses alertes réel d'un seuil pris au k-ième plus grand score honnête")
for n, k in ((300, 3), (1000, 10), (1600, 16), (5000, 50)):
    m, s, bas, haut = intervalle_taux_realise(n, k)
    print(f"   n={n:5d} k={k:3d} : moyenne {m:.4f}, écart type {s:.4f}, "
          f"95 % dans [{bas:.4f} ; {haut:.4f}]")

print("B. Plus petit lot honnête qui donne un seuil fini")
print(f"   validité en moyenne à 1 % (rang conforme) : n >= {ceil(1 / ALPHA) - 1}")
print(f"   validité à 95 % de confiance à 1 % (le maximum du lot) : "
      f"n >= {ceil(log(DELTA) / log(1 - ALPHA))}")
print(f"   contrôle de la formule sur l'exemple de Gao (alpha = delta = 0,05) : "
      f"n >= {ceil(log(0.05) / log(0.95))}")

print("C. Prix de la finesse : rang certifié à 95 % et taux réel moyen du seuil")
for n in (299, 500, 1000, 2000, 5000, 10000):
    r = rang_certifie(n)
    print(f"   n={n:5d} : rang {r:3d}, taux réel moyen {r / (n + 1):.4f}")

print("D. Bande uniforme de Dvoretzky-Kiefer-Wolfowitz à 95 %")
for n in (300, 5000):
    print(f"   n={n:5d} : demi-largeur {sqrt(log(2 / DELTA) / (2 * n)):.4f}")
print(f"   n pour une demi-largeur de 0,002 : {ceil(log(2 / DELTA) / (2 * 0.002 ** 2))}")

print("E. Règle des 50 dépassements : point de fonctionnement jugeable selon n")
for n in (300, 500, 1000, 5000):
    print(f"   n={n:5d} : alpha >= {50 / n:.3f}")

print("F. Illustration binormale à variances égales (hypothèse, pas une mesure)")
for aire in (0.69, 0.80, 0.95):
    d = sqrt(2) * norm.ppf(aire)
    z = norm.ppf(1 - ALPHA)
    rappel = norm.cdf(d - z)
    pente = exp(d * z - d * d / 2)
    ligne = f"   aire {aire:.2f} : rappel à 1 % {rappel:.3f}, pente {pente:5.1f}"
    for n in (300, 1600, 5000):
        ligne += f", écart type dû au seuil n={n} : {pente * sqrt(ALPHA * (1 - ALPHA) / n):.3f}"
    print(ligne)
    print(f"      n pour ramener cet écart type à 0,010 : "
          f"{ceil(pente ** 2 * ALPHA * (1 - ALPHA) / 0.010 ** 2)}")

print("G. Borne haute exacte (Clopper-Pearson, unilatérale à 95 %) d'un taux d'alerte honnête")
for x, n in ((0, 299), (45, 300), (60, 300)):
    haut = 1 - DELTA ** (1 / n) if x == 0 else beta(x + 1, n - x).ppf(1 - DELTA)
    print(f"   {x:3d} alertes sur {n} : borne haute {haut:.4f}")

print("H. Illustration : nombre d'épisodes pour une alerte au niveau du déploiement")
print("   (pari de Bernoulli contre un taux honnête borné q ; taux du saboteur p supposé)")
q = 0.20
for p in (0.25, 0.30, 0.40):
    kl = p * log(p / q) + (1 - p) * log((1 - p) / (1 - q))
    print(f"   q={q:.2f} p={p:.2f} : divergence {kl:.4f}, "
          f"épisodes pour un facteur 100 : {ceil(log(1 / ALPHA) / kl)}")

print("I. Contrôle de A par la loi binomiale : P(taux réel du 3e plus grand de 300 > 1 %)")
print(f"   {binom(300, ALPHA).cdf(2):.4f}")

print("J. Rangs que le lot ne sait pas distinguer du seuil à 1 % (1 % dans l'intervalle central à 95 %)")
for n in (300, 1000, 5000):
    rangs = [r for r in range(1, n // 10)
             if beta(r, n - r + 1).ppf(0.025) <= ALPHA <= beta(r, n - r + 1).ppf(0.975)]
    print(f"   n={n:5d} : rangs {rangs[0]} à {rangs[-1]}, "
          f"soit un taux réel moyen de {rangs[0] / (n + 1):.4f} à {rangs[-1] / (n + 1):.4f}")

print("K. Lot honnête pour un seuil certifié à 97,5 % (risque partagé avec la borne du rappel)")
print(f"   n >= {ceil(log(0.025) / log(1 - ALPHA))}")
