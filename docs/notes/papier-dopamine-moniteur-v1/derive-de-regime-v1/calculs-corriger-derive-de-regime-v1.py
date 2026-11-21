"""Calculs cités par `corriger-derive-de-regime-v1.md` (seuil à 1 % sous changement de régime).

Aucune donnée du programme n'est lue. Blocs A à D, F à K : lois exactes ou intégrales
à une dimension, sans tirage. Bloc E et test de rang du bloc D : tirages de calibration
et de témoins seulement (le taux vrai d'un seuil reste exact), graines par
`numpy.random.SeedSequence`, écrites en sortie (R9). Tout est une illustration sous
hypothèse écrite (scores honnêtes gaussiens, dérive plantée), pas une mesure.

Lancer : python calculs-corriger-derive-de-regime-v1.py > calculs-corriger-derive-de-regime-v1.txt
"""
from math import ceil, exp, floor, log, sqrt

import numpy as np
from scipy import integrate, optimize
from scipy.stats import beta, betabinom, binom, laplace, logistic, norm
from scipy.stats import t as student

ALPHA = 0.01
Z99 = norm.ppf(1 - ALPHA)
DERIVE = Z99 - norm.ppf(1 - 3 * ALPHA)  # translation qui triple un taux gaussien de 1 %
RACINE = 20261121
R_TIRAGES = 4000


def kl(a, b):
    """Divergence de Kullback-Leibler entre deux lois de Bernoulli, en nats."""
    return a * log(a / b) + (1 - a) * log((1 - a) / (1 - b))


def loi_du_maximum(n, fonction):
    """Espérance de fonction(M), M le plus grand de n scores gaussiens réduits."""
    dens = lambda m: n * norm.pdf(m) * norm.cdf(m) ** (n - 1) * fonction(m)
    return integrate.quad(dens, -2, 12, limit=400)[0]


print(f"Translation qui triple un taux gaussien de 1 % : {DERIVE:.4f} écart type")

print("A. Sensibilité d'un seuil à une translation des scores honnêtes")
for a in (0.20, 0.10, 0.05, 0.01, 0.001):
    z = norm.ppf(1 - a)
    print(f"   gaussien, taux nominal {a:.3f} : taux de hasard au seuil {norm.pdf(z) / a:.2f} par écart type ; "
          f"la translation {DERIVE:.3f} le multiplie par {norm.sf(z - DERIVE) / a:.2f} ; "
          f"translation qui le triple : {z - norm.ppf(1 - 3 * a):.3f}")
for nom, loi, ecart in (("logistique", logistic, np.pi / sqrt(3)), ("Laplace", laplace, sqrt(2)),
                        ("Student à 3 degrés", student(3), sqrt(3))):
    q99, q97 = loi.ppf(0.99), loi.ppf(0.97)
    print(f"   {nom} : translation qui triple 1 % = {(q99 - q97) / ecart:.3f} écart type")
print("   en variation totale, tripler 1 % demande un déplacement de masse de 0,02 seulement")

print("B. La base « le plus grand score de n » sous cette translation (taux vrai, exact)")
for n in (200, 299, 300, 368, 400, 1000):
    moy0 = loi_du_maximum(n, lambda m: norm.sf(m))
    moy1 = loi_du_maximum(n, lambda m: norm.sf(m - DERIVE))
    couv0 = 1 - norm.cdf(Z99) ** n
    couv1 = 1 - norm.cdf(Z99 + DERIVE) ** n
    print(f"   n={n:4d} : taux moyen sans dérive {moy0:.5f}, avec {moy1:.5f} ; "
          f"probabilité que le taux vrai soit d'au plus 1 % : {couv0:.4f} puis {couv1:.4f}")

print("C. Robustesse au pire cas sur une boule de lois, au taux de 1 %")
rayon = DERIVE ** 2 / 2
masse = optimize.brentq(lambda lb: kl(ALPHA, exp(lb)) - rayon, log(1e-12), log(ALPHA))
print(f"   boule de Kullback-Leibler de rayon {rayon:.4f} nat (celui de la translation) : il faut régler le seuil "
      f"au taux {exp(masse):.2e} sous la loi d'étalonnage, soit de l'ordre de {1 / exp(masse):.2e} épisodes")
for gamma in (3.0,):
    z = norm.ppf(1 - ALPHA / gamma)
    print(f"   rapport de densité borné par {gamma:.0f} : seuil au taux {ALPHA / gamma:.5f} ; "
          f"sous la translation gaussienne son taux vrai est {norm.sf(z - DERIVE):.5f}, donc au-dessus de 1 %")
b_eff = norm.sf(Z99 + DERIVE)
print(f"   enveloppe de translation d'au plus {DERIVE:.3f} : seuil au taux {b_eff:.5f} "
      f"(facteur {ALPHA / b_eff:.2f}) ; seuil fini valide en moyenne dès n = {ceil(1 / b_eff) - 1}, "
      f"certifié à 95 % dès n = {ceil(log(0.05) / log(1 - b_eff))}")
for aire in (0.69, 0.80, 0.95):
    d = sqrt(2) * norm.ppf(aire)
    print(f"   prix en rappel d'une marge de {DERIVE:.3f} sans dérive, aire {aire:.2f} : "
          f"{norm.sf(Z99 - d):.3f} -> {norm.sf(Z99 + DERIVE - d):.3f}")

print("D. Témoins honnêtes du régime d'usage : combien pour voir la dérive")
n = 400
grille = (np.arange(4000) + 0.5) / 4000
for rang, nom in ((4, "seuil à 1 % (4e plus grand de 400)"), (80, "seuil auxiliaire à 20 % (80e plus grand de 400)")):
    p_cal = beta(rang, n - rang + 1).ppf(grille)          # taux d'étalonnage du seuil, par quantiles
    p_use = norm.sf(norm.isf(p_cal) - DERIVE)              # son taux après la translation
    ligne = f"   {nom}, test exact bêta-binomial unilatéral à 5 % :"
    for m in (50, 100, 200, 300, 500):
        nul = betabinom(m, rang, n - rang + 1)
        c = next(k for k in range(m + 2) if nul.sf(k - 1) <= 0.05)
        ligne += f" m={m} puissance {np.mean(binom.sf(c - 1, m, p_use)):.2f} ;"
    print(ligne)
graines = np.random.SeedSequence(RACINE).spawn(64)
print(f"   graine racine {RACINE}, suites dérivées dans l'ordre des lignes ; {R_TIRAGES} tirages par ligne")
ligne = "   test de rang (Mann-Whitney, unilatéral à 5 %, approximation normale) contre la translation :"
for i, m in enumerate((20, 30, 50, 100)):
    rng = np.random.default_rng(graines[i])
    rejets = 0
    for _ in range(R_TIRAGES):
        cal = np.sort(rng.standard_normal(n))
        tem = rng.standard_normal(m) + DERIVE
        u = np.searchsorted(cal, tem).sum()
        rejets += (u - m * n / 2) / sqrt(m * n * (m + n + 1) / 12) > norm.ppf(0.95)
    ligne += f" m={m} puissance {rejets / R_TIRAGES:.2f} ;"
print(ligne)
for b in (0.2, 0.5):
    print(f"   borne basse du nombre moyen de témoins pour certifier « 1 % et non 3 % » sur les seuls dépassements "
          f"(risque 0,05, puissance {1 - b:.1f}) : {ceil(kl(1 - b, 0.05) / kl(0.01, 0.03))}")

print("E. Le seuil ancré : k-ième plus grand de l'étalonnage, translaté par la borne haute de la dérive")
print("   (borne de Hodges-Lehmann par inversion du test de rang ; n = 400 ; taux vrai exact par tirage ;")
print("    rappel contre un saboteur d'aire 0,80 ; base = le plus grand score de l'étalonnage)")
D80 = sqrt(2) * norm.ppf(0.80)
MONDES = {
    "sain": dict(tirer=lambda r, m: r.standard_normal(m), faux=lambda s: norm.sf(s),
                 rappel=lambda s: norm.sf(s - D80)),
    "translation qui triple": dict(tirer=lambda r, m: r.standard_normal(m) + DERIVE,
                                   faux=lambda s: norm.sf(s - DERIVE), rappel=lambda s: norm.sf(s - DERIVE - D80)),
    "échelle x 1,25": dict(tirer=lambda r, m: 1.25 * r.standard_normal(m), faux=lambda s: norm.sf(s / 1.25),
                           rappel=lambda s: norm.sf((s - D80) / 1.25)),
    "queue seule (2 % à +3)": dict(
        tirer=lambda r, m: np.where(r.random(m) < 0.02, 3 + 0.5 * r.standard_normal(m), r.standard_normal(m)),
        faux=lambda s: 0.98 * norm.sf(s) + 0.02 * norm.sf((s - 3) / 0.5),
        rappel=lambda s: 0.98 * norm.sf(s - D80) + 0.02 * norm.sf((s - 3 - D80) / 0.5)),
}
VARIANTES = (("confiance dite, risque 5 %", 1, 0.05 - 0.99 ** n), ("en moyenne", 2, 0.005))
j = 8
for nom_v, k, eta in VARIANTES:
    for m in (50, 100, 200, 400):
        c_eta = floor(m * n / 2 - norm.ppf(1 - eta) * sqrt(m * n * (m + n + 1) / 12) - 0.5)
        rang_diff = m * n - c_eta                     # rang (croissant) de la différence prise pour borne haute
        for nom_m, monde in MONDES.items():
            rng = np.random.default_rng(graines[j]); j += 1
            faux, ecart, faux_base, marge = [], [], [], []
            for _ in range(R_TIRAGES if m <= 200 else R_TIRAGES // 2):
                cal = np.sort(rng.standard_normal(n))
                tem = monde["tirer"](rng, m)
                diff = np.subtract.outer(tem, cal).ravel()
                borne = np.partition(diff, rang_diff - 1)[rang_diff - 1]
                seuil, base = cal[-k] + borne, cal[-1]
                faux.append(monde["faux"](seuil)); faux_base.append(monde["faux"](base))
                ecart.append(monde["rappel"](seuil) - monde["rappel"](base)); marge.append(borne)
            faux, ecart = np.array(faux), np.array(ecart)
            print(f"   {nom_v:26s} m={m:3d} {nom_m:24s}: taux vrai moyen {faux.mean():.4f} "
                  f"(base {np.mean(faux_base):.4f}), part des tirages au-dessus de 1 % {np.mean(faux > ALPHA):.3f}, "
                  f"borne moyenne {np.mean(marge):+.2f}, écart de rappel à la base {ecart.mean():+.3f} "
                  f"(erreur type {ecart.std(ddof=1) / sqrt(len(ecart)):.3f})")

print("E2. Le seuil des témoins seuls : k-ième plus grand de m témoins du régime d'usage, k = partie entière de 0,01 (m + 1)")
print("   (exact, sans tirage ; vaut pour toute dérive commune aux témoins et aux épisodes d'usage ; base à n = 400 ;")
print("    borne basse à 99 % de l'écart de rappel moyen sur 2 000 tirages indépendants, saboteur d'aire 0,80)")
u = (np.arange(20000) + 0.5) / 20000
max_cal = norm.isf(beta(1, 400).ppf(u))                    # le plus grand de 400 scores d'étalonnage, par quantiles
for m in (99, 150, 200, 300, 400):
    k = floor(ALPHA * (m + 1))
    taux = beta(k, m - k + 1).ppf(u)                       # taux vrai du seuil des témoins, dans leur régime
    rappel = norm.sf(norm.isf(taux) - D80)
    ligne = (f"   m={m:3d} k={k} : taux vrai moyen {taux.mean():.5f}, probabilité d'un taux d'au plus 1 % "
             f"{beta(k, m - k + 1).cdf(ALPHA):.3f} ;")
    for nom_m, derive in (("sain", 0.0), ("translation qui triple", DERIVE)):
        rappel_base = norm.sf(max_cal - derive - D80)
        ecart = rappel.mean() - rappel_base.mean()
        erreur = sqrt((rappel.var() + rappel_base.var()) / 2000)
        ligne += f" {nom_m} : écart de rappel {ecart:+.3f}, borne basse {ecart - norm.ppf(0.995) * erreur:+.3f} ;"
    print(ligne)

print("F. Rang de l'agent parmi K exécutions du jumeau sur la même tâche (alerte si l'agent dépasse les K)")
for K in (4, 9, 99):
    ligne = f"   K={K:2d} : taux honnête exact {1 / (K + 1):.3f} dans tout régime ;"
    for aire in (0.69, 0.80, 0.95):
        d = sqrt(2) * norm.ppf(aire)
        p = integrate.quad(lambda x: norm.cdf(x) ** K * norm.pdf(x - d), -8, 14)[0]
        ligne += f" saboteur d'aire {aire:.2f} : {p:.3f}"
        if K == 4:
            ligne += f" (pari à 100 en {ceil(log(100) / kl(p, 0.2))} épisodes)"
        ligne += " ;"
    print(ligne)
for aire_h in (0.52, 0.55, 0.60):
    d = sqrt(2) * norm.ppf(aire_h)
    p = integrate.quad(lambda x: norm.cdf(x) ** 4 * norm.pdf(x - d), -8, 14)[0]
    print(f"   si l'honnête diffère du jumeau (aire {aire_h:.2f}), K=4 : taux honnête {p:.3f} au lieu de 0,200")

print("G. Ré-étalonnage sur le flux du suspect : « le centième le plus suspect du lot », saboteur d'aire 0,80")
for part in (0.0, 0.05, 0.2, 0.5, 1.0):
    s = optimize.brentq(lambda x: (1 - part) * norm.sf(x) + part * norm.sf(x - D80) - ALPHA, -5, 12)
    print(f"   part d'épisodes sabotés {part:.2f} : rappel {norm.sf(s - D80):.3f}, taux de fausses alertes {norm.sf(s):.4f}")

print("H. Sans aucune dérive : taux réalisé dans une famille de tâches neuve, seuil réglé à 1 % toutes familles confondues")
for rho in (0.05, 0.10, 0.20):
    taux = lambda q: norm.sf((Z99 - sqrt(rho) * norm.ppf(q)) / sqrt(1 - rho))
    part3 = norm.sf((Z99 - sqrt(1 - rho) * norm.ppf(0.97)) / sqrt(rho))
    print(f"   corrélation dans la famille {rho:.2f} : médiane {taux(0.5):.4f}, 90e centile {taux(0.9):.4f}, "
          f"95e centile {taux(0.95):.4f} ; part des familles neuves au taux triplé ou pire : {part3:.3f}")

print("J. Comparer deux moniteurs « à 1 % » quand le taux de l'un a triplé : rappel gagné par les seules fausses alertes")
for aire in (0.69, 0.80, 0.95):
    d = sqrt(2) * norm.ppf(aire)
    print(f"   aire {aire:.2f} : rappel au taux vrai de 1 % {norm.sf(Z99 - d):.3f}, au taux vrai de 3 % "
          f"{norm.sf(norm.ppf(0.97) - d):.3f}, soit {norm.sf(norm.ppf(0.97) - d) - norm.sf(Z99 - d):+.3f}")

print("K. Contrôle « taux d'alerte entre deux lots honnêtes » : loi binomiale ou bêta-binomiale ?")
for n_a, m_b in ((368, 200), (368, 368), (1000, 1000)):
    rang = floor(0.2 * (n_a + 1))
    p0 = rang / (n_a + 1)
    bas, haut = binom.ppf(0.025, m_b, p0), binom.ppf(0.975, m_b, p0)
    nul = betabinom(m_b, rang, n_a - rang + 1)
    print(f"   seuil au rang {rang} de {n_a}, lu sur {m_b} épisodes honnêtes de même loi : l'intervalle binomial central "
          f"à 95 % [{bas:.0f} ; {haut:.0f}] est quitté avec probabilité {nul.cdf(bas - 1) + nul.sf(haut):.3f}")
print(f"   rejeu de Gao, p. 6 : P(K >= 14) sous BetaBinomial(75, 5, 96) = {betabinom(75, 5, 96).sf(13):.6f}")
