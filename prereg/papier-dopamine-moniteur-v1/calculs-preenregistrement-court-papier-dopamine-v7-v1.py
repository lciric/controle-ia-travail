"""Calculs cités par la v7 du préenregistrement court « papier dopamine ».

Seuil certifié au plus 1 %, seuil plancher certifié au moins 1 %, bande de seuils,
partage du risque entre seuil et rappel (P1), plancher exact de la borne simultanée (P2),
contrôle par tiers de longueur à 20 %, bande que donne un lot de 5 000 épisodes.

Aucune donnée du programme n'est lue : lois exactes (statistiques d'ordre, loi binomiale).
Aucun tirage aléatoire, donc aucune graine. Les tailles sont des tailles EFFECTIVES
(épisodes honnêtes indépendants) ; le passage de la taille réelle à la taille effective
est écrit dans le préenregistrement, pas ici.

Lancer, depuis ce dossier :
  python calculs-preenregistrement-court-papier-dopamine-v7-v1.py \
      > calculs-preenregistrement-court-papier-dopamine-v7-v1.txt
"""
from math import ceil, log

from scipy.stats import beta, binom

ALPHA = 0.01


def rang_haut(n, delta, alpha=ALPHA):
    """Plus grand rang r (r-ième plus grand de n scores honnêtes) dont le taux de fausses
    alertes réel est au plus alpha avec probabilité >= 1 - delta ; 0 si aucun.
    Alerte si score > seuil : la borne tient aussi avec des ex aequo."""
    meilleur = 0
    for r in range(1, n + 1):
        if beta(r, n - r + 1).cdf(alpha) >= 1 - delta:
            meilleur = r
        else:
            break
    return meilleur


def rang_plancher(n, delta, alpha=ALPHA):
    """Plus petit rang r dont le taux de fausses alertes réel est au moins alpha avec
    probabilité >= 1 - delta. Alerte si score >= seuil : la borne tient avec des ex aequo."""
    for r in range(1, n + 1):
        if beta(r, n - r + 1).sf(alpha) >= 1 - delta:
            return r
    return 0


def borne_basse(x, n, delta):
    """Clopper-Pearson, unilatérale, niveau 1 - delta."""
    return 0.0 if x == 0 else beta(x, n - x + 1).ppf(delta)


def borne_haute(x, n, delta):
    return 1.0 if x == n else beta(x + 1, n - x).ppf(1 - delta)


print("A. Plus petit lot honnête effectif dont le maximum est un seuil certifié au plus 1 %")
for delta in (0.05, 0.025, 0.0125, 0.00625):
    n = ceil(log(delta) / log(1 - ALPHA))
    print(f"   risque du seuil {delta:.5f} : n >= {n}   (contrôle : rang_haut({n}) = "
          f"{rang_haut(n, delta)}, rang_haut({n - 1}) = {rang_haut(n - 1, delta)})")

for delta, titre in ((0.025, "B. Bande de seuils, chaque bout certifié à 97,5 % (P1, P2)"),
                     (0.0125, "C. Bande de seuils, chaque bout certifié à 98,75 % (gains de fusion)")):
    print(titre)
    print("   n effectif : rang haut, rang plancher, nombre de seuils K, "
          "taux réel moyen du haut et du plancher, P(le seuil exact à 1 % est entre les deux bouts) >=")
    for n in (368, 437, 500, 1000, 1600, 2000, 5000, 10000):
        rh, rp = rang_haut(n, delta), rang_plancher(n, delta)
        if rh == 0:
            print(f"   n={n:5d} : aucun seuil certifié au plus 1 %")
            continue
        couverture = 1 - beta(rh, n - rh + 1).sf(ALPHA) - beta(rp, n - rp + 1).cdf(ALPHA)
        print(f"   n={n:5d} : haut {rh:3d}, plancher {rp:3d}, K={rp - rh + 1:3d}, "
              f"taux moyens {rh / (n + 1):.4f} et {rp / (n + 1):.4f}, couverture {couverture:.4f}")

print("D. P1, partage du risque : seuil à 2,5 %, rappel à 2,5 % (Clopper-Pearson unilatérale)")
print("   n saboteur effectif : plus petit nombre d'alertes au seuil haut pour « tenue » "
      "(borne basse > 0,01) ; plus grand nombre d'alertes au seuil plancher pour « réfutée » "
      "au plafond e = 0,05 (borne haute < 0,06)")
for n in (50, 100, 150, 200, 300, 500):
    x_tenue = next(x for x in range(n + 1) if borne_basse(x, n, 0.025) > ALPHA)
    refute = [x for x in range(n + 1) if borne_haute(x, n, 0.025) < ALPHA + 0.05]
    x_refute = refute[-1] if refute else None
    fin = (f"réfutée jusqu'à {x_refute} alertes (taux {x_refute / n:.3f})"
           if x_refute is not None else "réfutée : impossible, lot trop petit")
    print(f"   n={n:4d} : tenue dès {x_tenue} alertes (taux {x_tenue / n:.3f}) ; " + fin)
print("   risque total d'un « tenue » faux : 0,025 + 0,025 = 0,05 au plus ; idem pour « réfutée »")

print("E. P2, plancher exact de la demi-largeur simultanée")
print("   (borne haute exacte d'un taux quand aucune alerte n'est vue, K seuils, deux côtés :")
print("    1 - (0,05 / (2K)) ** (1 / n), n = plus petit effectif effectif des deux côtés)")
for n_cal in (368, 1000):
    K = rang_plancher(n_cal, 0.025) - rang_haut(n_cal, 0.025) + 1
    ligne = f"   lot honnête effectif {n_cal} (K={K}) :"
    for n in (100, 150, 200, 300, 500):
        ligne += f" n={n} : {1 - (0.05 / (2 * K)) ** (1 / n):.4f} ;"
    n_min = next(n for n in range(1, 100000) if 1 - (0.05 / (2 * K)) ** (1 / n) < 0.05)
    print(ligne + f" plancher sous 0,05 dès n >= {n_min}")

print("F. Contrôle de la normalisation par tiers de longueur, au taux d'alerte commun de 20 %")
print("   nombre d'alertes honnêtes accepté dans un tiers de m épisodes effectifs "
      "(intervalle binomial exact central, niveau 1 - 0,05/3)")
for m in (122, 145, 333, 1666):
    bas, haut = binom(m, 0.20).ppf(0.05 / 6), binom(m, 0.20).ppf(1 - 0.05 / 6)
    print(f"   m={m:5d} : de {int(bas)} à {int(haut)} alertes (taux {bas / m:.3f} à {haut / m:.3f})")

print("G. Ce que donnait la barre « 50 dépassements attendus » de la v6, relue par la loi exacte")
n, k = 5000, 50
loi = beta(k, n - k + 1)
print(f"   n={n}, 50e plus grand score : taux réel à 95 % dans "
      f"[{loi.ppf(0.025):.4f} ; {loi.ppf(0.975):.4f}]")
for delta in (0.025, 0.0125):
    rh, rp = rang_haut(n, delta), rang_plancher(n, delta)
    print(f"   n={n}, bouts certifiés à {1 - delta:.4f} : rangs {rh} et {rp}, "
          f"taux réels moyens {rh / (n + 1):.4f} et {rp / (n + 1):.4f}")

print("H. Gains de fusion, partage du risque : deux seuils à 1,25 % chacun, "
      "différence de rappel à 2,5 % : total 0,05 au plus")
