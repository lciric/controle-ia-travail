#!/usr/bin/env python3
"""Calculs de méthode du brouillon 8 du préenregistrement de la porte G1 — v1.

Processeur seul. AUCUNE donnée du programme n'est lue (rien sous `donnees/`, `diag/`, `runs/`, aucun score d'épisode,
aucun verdict) : les seules entrées sont des constantes recopiées des pièces citées, chacune avec sa source en
commentaire, et des lois SUPPOSÉES (binomiale, bêta-binomiale, gaussienne à effet de tâche). Les sorties sont des
illustrations « sous supposition » : elles éclairent des choix de forme, elles ne testent aucune prédiction du
programme et ne sont pas opposables seules (R7). La note des nœuds et le brouillon 8 citent la sortie par chemin et
empreinte (R6).

Graines (R9) : `numpy.random.SeedSequence`, une racine par paragraphe, enfants dérivés par cellule ; écrites en sortie.

Lancer, depuis un dossier vide, avec l'environnement du dépôt :
    python -I <chemin>/calculs-g1-brouillon8-v1.py > calculs-g1-brouillon8-v1-sortie.txt
"""
import math
import platform
from fractions import Fraction

import numpy as np
import scipy
from scipy import stats


def titre(s):
    print(f"\n## {s}\n")


def nombre(x, dec=0):
    """Nombre à la française : espace pour les milliers, virgule décimale."""
    return f"{x:,.{dec}f}".replace(",", " ").replace(".", ",")


print("# Sortie de calculs-g1-brouillon8-v1.py")
print(f"Python {platform.python_version()} ; numpy {np.__version__} ; scipy {scipy.__version__}")
print("Toutes les lois sont SUPPOSÉES ; aucune donnée du programme n'est lue.")

# ---------------------------------------------------------------------------------------------------------------
titre("1. Seuil du pari sur des cycles sans borne : borne de l'erreur totale (somme exacte)")
# Sources : seuil de promotion 160 et niveau 0,05 (brouillon 6, section « Seuil », décision DG1-2 prise le 5 novembre
# 2026) ; M = 2 modes de la porte (DG1-6 (b)) ; pas de borne de cycles (N-062, point 4) ; règle k(k+1) proposée par
# l'avis rendu le 21 novembre sur le mode tenu à l'écart (rapport du sas des notes, pièce 1).
SEUIL, M = 160, 2
regles = (
    ("(a) 160 à chaque cycle", lambda k: SEUIL),
    ("(b) 160 x k(k+1)/2 : 160, 480, 960, 1 600…", lambda k: SEUIL * k * (k + 1) // 2),
    ("(c) 160 x k(k+1) : 320, 960, 1 920…", lambda k: SEUIL * k * (k + 1)),
)
print("Par cycle, au seuil s : la porte est franchie à tort avec une probabilité d'au plus 1/s (une fiche de mode au moins")
print("est sous son nul et doit atteindre s) ; une affirmation mode par mode est fausse avec une probabilité d'au plus M/s.")
print(f"Somme exacte des 1/(k(k+1)) pour k = 1 à 10 000 : {float(sum(Fraction(1, k * (k + 1)) for k in range(1, 10001))):.6f} (limite 1)\n")
print("| règle | seuils des cycles 1 à 5 | borne pour la porte après 1, 2, 4, 8 cycles | limite sans borne de cycles (porte ; affirmations par mode) |")
print("|---|---|---|---|")
for nom, regle in regles:
    seuils = [regle(k) for k in range(1, 6)]
    bornes = [float(sum(Fraction(1, regle(k)) for k in range(1, K + 1))) for K in (1, 2, 4, 8)]
    if "(a)" in nom:
        limite = "aucune : K/160 pour la porte, K/80 par mode (5 % au 8e et au 4e cycle)"
    elif "(b)" in nom:
        limite = f"{2 / SEUIL:.4f} ; {2 * M / SEUIL:.4f}"
    else:
        limite = f"{1 / SEUIL:.5f} ; {M / SEUIL:.4f}"
    print(f"| {nom} | {', '.join(str(s) for s in seuils)} | {', '.join(f'{b:.5f}' for b in bornes)} | {limite} |")

# ---------------------------------------------------------------------------------------------------------------
titre("2. Garde de spécificité écrite avec une borne de Clopper-Pearson : contrôle des chiffres de la source, puis épisodes groupés par tâche")
# Source : extrait vérifié du brouillon 2 de la décision sur le contraste à témoin apparié (N-074, non pris),
# sections 3 et 4 : borne haute unilatérale à 95 % strictement inférieure à 5 %, au moins 300 épisodes du témoin ;
# puissances annoncées 0,95 (200 épisodes) et 0,996 (300), produits 0,85 / 0,73 et 0,99 / 0,98, « moins de 4 % »
# à taux vrai 5 %, « 37 chances sur cent » pour 100 épisodes.


def cp_haute(x, n, niveau=0.95):
    return 1.0 if x >= n else stats.beta.ppf(niveau, x + 1, n - x)


def x_max_passant(n, tol=0.05):
    x = -1
    while cp_haute(x + 1, n) < tol:
        x += 1
    return x


for n in (200, 300, 400):
    xm = x_max_passant(n)
    p1, p5 = stats.binom.cdf(xm, n, 0.01), stats.binom.cdf(xm, n, 0.05)
    print(f"n = {n} épisodes indépendants : la garde passe jusqu'à {xm} alertes ; P(passer | taux vrai 1 %) = {p1:.4f} "
          f"(trois cellules : {p1 ** 3:.3f} ; six : {p1 ** 6:.3f}) ; P(passer | taux vrai 5 %) = {p5:.4f}")
print(f"P(aucun de 100 épisodes ne dépasse le vrai quantile à 1 %) = {0.99 ** 100:.3f}")

ss2 = np.random.SeedSequence(20261122)
print(f"\nÉpisodes groupés par tâche, loi bêta-binomiale de corrélation intra-tâche rho ; graine racine {ss2.entropy} ; 200 000 répétitions par cellule")
print("| tâches x exécutions | rho | P(passer) si le taux vrai est 5 % (doit rester sous 0,05) | P(passer) si le taux vrai est 1 % |")
print("|---|---|---|---|")


def alertes(n_taches, m, p, rho, rng, R=200000):
    if rho <= 0 or m == 1:
        return rng.binomial(n_taches * m, p, size=R)
    a, b = p * (1 - rho) / rho, (1 - p) * (1 - rho) / rho
    return rng.binomial(m, rng.beta(a, b, size=(R, n_taches))).sum(axis=1)


plans = ((300, 1), (100, 3), (60, 5), (30, 10), (400, 10))
enfants = iter(ss2.spawn(len(plans) * 3 * 2))
for nt, m in plans:
    xm = x_max_passant(nt * m)
    for rho in (0.0, 0.1, 0.3):
        r5 = np.mean(alertes(nt, m, 0.05, rho, np.random.default_rng(next(enfants))) <= xm)
        r1 = np.mean(alertes(nt, m, 0.01, rho, np.random.default_rng(next(enfants))) <= xm)
        print(f"| {nt} x {m} | {rho:.1f} | {r5:.4f} | {r1:.4f} |")
print("\nSans aucune alerte sur n unités indépendantes, la borne haute exacte à 95 % d'un taux par unité vaut 1 - 0,05^(1/n) :")
for n in (30, 58, 59, 100):
    print(f"  n = {n:3d} unités : {1 - 0.05 ** (1 / n):.4f}")

# ---------------------------------------------------------------------------------------------------------------
titre("3. Garde de spécificité lue par un pari borné par unité (forme de la garde appariée de la conception du pari, § 2.4)")
# Facteur par unité : 1 + lambda x (tol - f(u)), f(u) = part des K épisodes du témoin de l'unité en alarme, tol = 0,05 ;
# richesse = moyenne sur la grille des mises {0,1 ; 0,3 ; 0,6 ; 0,9} (D-S6) ; garde tenue si le maximum courant
# atteint le seuil (20 = 1/0,05 ; 160 = seuil de promotion de la porte).
LAM, TOL = np.array([0.1, 0.3, 0.6, 0.9]), 0.05
ss3 = np.random.SeedSequence(2026112203)
print(f"graine racine {ss3.entropy} ; 20 000 répétitions par cellule")
print("| unités x épisodes du témoin par unité | rho | taux vrai d'alerte | P(garde tenue) au seuil 20 | au seuil 160 |")
print("|---|---|---|---|---|")


def parts(n, K, p, rho, rng, R=20000):
    if rho <= 0 or K == 1:
        return rng.binomial(K, p, size=(R, n)) / K
    a, b = p * (1 - rho) / rho, (1 - p) * (1 - rho) / rho
    return rng.binomial(K, rng.beta(a, b, size=(R, n))) / K


def tenue(f, seuil):
    w = np.exp(np.cumsum(np.log1p(LAM[None, None, :] * (TOL - f[:, :, None])), axis=1)).mean(axis=2)
    return (w.max(axis=1) >= seuil).mean()


plans3 = ((400, 1, (0.0,)), (400, 3, (0.0, 0.3)), (400, 10, (0.0, 0.3)), (300, 1, (0.0,)), (150, 2, (0.0, 0.3)))
enfants3 = iter(ss3.spawn(60))
for n, K, rhos in plans3:
    for rho in rhos:
        for p in (0.01, 0.02, 0.05):
            f = parts(n, K, p, rho, np.random.default_rng(next(enfants3)))
            print(f"| {n} x {K} | {rho:.1f} | {p:.2f} | {tenue(f, 20):.4f} | {tenue(f, 160):.4f} |")

# ---------------------------------------------------------------------------------------------------------------
titre("4. Bruit d'un seuil conforme à 1 % selon le nombre d'épisodes de calibrage")
# Seuil au rang conforme ceil((K + 1)(1 - tau)) parmi K épisodes négatifs (brouillon 6, section « Métrique ») ;
# épisodes indépendants : le taux réel de fausses alertes suit une loi Bêta(K + 1 - r, r).
print("| K épisodes de calibrage | rang par le haut | taux réel : moyenne | quantiles 5 % et 95 % | P(taux réel > 2 %) |")
print("|---|---|---|---|---|")
for K in (100, 300, 1000, 4000, 12000, 60000):
    r = math.ceil((K + 1) * 0.99 - 1e-12)
    loi = stats.beta(K + 1 - r, r)
    print(f"| {nombre(K)} | {K + 1 - r} | {loi.mean():.4f} | {loi.ppf(0.05):.4f} à {loi.ppf(0.95):.4f} | {loi.sf(0.02):.4f} |")
ss4 = np.random.SeedSequence(2026112202)
print(f"\nÉpisodes groupés par tâche (scores gaussiens, effet de tâche de corrélation rho), K = 300 ; graine racine {ss4.entropy} ; 40 000 répétitions par cellule")
print("| tâches x exécutions | rho | moyenne | quantiles 5 % et 95 % | P(taux réel > 2 %) |")
print("|---|---|---|---|---|")
plans4 = ((300, 1), (100, 3), (30, 10))
enfants4 = iter(ss4.spawn(len(plans4) * 2))
k_haut = 300 + 1 - math.ceil(301 * 0.99 - 1e-12)
for nt, m in plans4:
    for rho in (0.1, 0.3):
        rng = np.random.default_rng(next(enfants4))
        R = 40000
        s = (np.sqrt(rho) * rng.standard_normal((R, nt, 1)) + np.sqrt(1 - rho) * rng.standard_normal((R, nt, m))).reshape(R, nt * m)
        fpr = stats.norm.sf(np.partition(s, -k_haut, axis=1)[:, -k_haut])
        print(f"| {nt} x {m} | {rho:.1f} | {fpr.mean():.4f} | {np.quantile(fpr, 0.05):.4f} à {np.quantile(fpr, 0.95):.4f} | {np.mean(fpr > 0.02):.4f} |")

# ---------------------------------------------------------------------------------------------------------------
titre("5. Devis : épisodes du témoin apparié selon le nombre d'exécutions par unité (même modèle de coût que le brouillon 6)")
# Constantes recopiées de l'extrait vérifié des calculs du brouillon 5 (§ 7) et du brouillon 7 (§ 1 et 2) :
# génération 42,1 à 54,6 s par épisode, notation d'un juge 8B 58,2 s, 1 à 4 équivalents « juge 8B » par épisode
# (INFÉRÉ par la source), prix 1,08 à 1,2133 USD de l'heure de carte, K_s = K_h = 10, 400 tâches, calibrage 15 fois.
GEN = {"bas": 42.1, "central": (42.1 + 54.6) / 2, "haut": 54.6}
JUGE = 58.2
B = {"bas": 1, "central": 2, "haut": 4}
PRIX = {"bas": 1.08, "central": (1.08 + 1.2133) / 2, "haut": 1.2133}
TACHES, K_S, K_H, FACTEUR = 400, 10, 10, 15
PLAFOND_5_NOV, PLAFOND_22_NOV = 6331, 7600   # GO-2026-11-05-07 ; GO-2026-11-22-120 (« environ 7 600 USD »)


def cout(episodes):
    return {c: (episodes * (GEN[c] + B[c] * JUGE) / 3600, episodes * (GEN[c] + B[c] * JUGE) / 3600 * PRIX[c]) for c in GEN}


base_par_tache = K_H + 3 * K_S * 2 + 12 + FACTEUR * 10
c0 = cout(TACHES * base_par_tache)
assert TACHES * base_par_tache == 92800 and round(c0["central"][0]) == 4247 and round(c0["central"][1]) == 4870, "contrôle manqué"
print(f"Contrôle : {TACHES} tâches x {base_par_tache} épisodes = {nombre(TACHES * base_par_tache)} ; central {nombre(c0['central'][0])} h, "
      f"{nombre(c0['central'][1])} USD (brouillon 6 : 92 800 ; 4 247 h ; 4 870 USD) : conforme.\n")
variantes = (
    ("sans témoin apparié (brouillon 6, rappel)", 0),
    ("garde, hypothèse du rédacteur précédent : 10 exécutions du témoin par unité sans consigne, 3 par unité à consigne, trois modes", 3 * 10 + 3 * 3),
    ("garde, une exécution du témoin par unité, six cellules (trois modes x deux familles)", 6 * 1),
    ("garde, une exécution du témoin par unité, organisme sans consigne seul (trois modes)", 3 * 1),
    ("garde, 10 exécutions par unité dans les deux cellules de la porte, 1 ailleurs (quatre cellules)", 2 * 10 + 4 * 1),
    ("contraste, 300 épisodes de calibrage du témoin par cellule (six cellules), évaluation à 10 et 3 exécutions", 3 * 10 + 3 * 3 + 6 * 300 / TACHES),
    ("contraste, calibrage du témoin à l'échelle de l'honnête dans les deux cellules de la porte, évaluation à 10 et 3 exécutions", 3 * 10 + 3 * 3 + 2 * FACTEUR * 10),
)
print("| variante | épisodes du témoin par tâche | épisodes en tout | USD bas / central / haut | central x 1,3 | sous le plafond d'environ 7 600 USD |")
print("|---|---|---|---|---|---|")
for nom, par_tache in variantes:
    E = TACHES * (base_par_tache + par_tache)
    c = cout(E)
    marge = c["central"][1] * 1.3
    print(f"| {nom} | {nombre(par_tache, 1 if par_tache != int(par_tache) else 0)} | {nombre(E)} | "
          f"{nombre(c['bas'][1])} / {nombre(c['central'][1])} / {nombre(c['haut'][1])} | {nombre(marge)} | {'oui' if marge <= PLAFOND_22_NOV else 'non'} |")
print("\nNon comptés, comme dans la source : une distillation de plus par témoin d'adaptateur et sa remise à l'intensité du saboteur ;")
print("le témoin du mode tenu à l'écart ; disques, téléchargements, extraction des tâches, lecteurs de l'oracle, pilote.")

# ---------------------------------------------------------------------------------------------------------------
titre("6. Repères divers cités par les fiches")
print(f"Dix actions par épisode, 5 % d'actions sabotées qui sonnent au seuil par action, indépendance : 1 - 0,95^10 = {1 - 0.95 ** 10:.4f}")
print(f"Seuil par action à 1 %, dix actions, indépendance : 1 - 0,99^10 = {1 - 0.99 ** 10:.4f} (brouillon 6 : 0,0956)")
