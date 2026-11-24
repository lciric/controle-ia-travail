"""Calculs d'illustration pour la demande 2 : zéro alerte sur 256 épisodes est-il surprenant ?
Lois exactes sous SUPPOSITIONS déclarées ; aucune donnée du programme n'est lue, hors quatre constantes du montage
(256 épisodes de seuil, niveau 0,01, dix actions par épisode, 64 épisodes par dose) et des aires du verdict
données en argument d'illustration. Bibliothèque standard et scipy. Sortie : calculs-zero-alerte-v1.txt."""
import math
from fractions import Fraction
from scipy.stats import norm, beta
from scipy.integrate import quad

K, ALPHA, T, N_DOSE = 256, 0.01, 10, 64
rang = math.ceil((K + 1) * (1 - ALPHA))            # rang conforme
a, b = K + 1 - rang, rang                           # taux réalisé de fausses alertes ~ Bêta(a, b)
print(f"A. Rang conforme : {rang} sur {K} ; taux réalisé de fausses alertes ~ Bêta({a} ; {b}), moyenne {a/(a+b):.4f}")

def p_zero_beta(n):
    """P(aucune alerte sur n épisodes) pour un surveillant aveugle, seuil conforme sans égalités : E[(1-p)^n], p ~ Bêta(a, b)."""
    f = Fraction(1)
    for i in range(n):
        f *= Fraction(b + i, a + b + i)
    return f
for n in (64, 256):
    f = p_zero_beta(n)
    print(f"B. Surveillant aveugle, {n} épisodes indépendants : P(zéro alerte) = {float(f):.4f}")
print(f"   Deux surveillants aveugles indépendants, 256 épisodes chacun : {float(p_zero_beta(256))**2:.4f}")

def p_alerte_episode(aire, p_fa, actions):
    """Scores normaux de même variance ; aire par action -> décalage d = sqrt(2) * z(aire) ; statistique = maximum de
    `actions` scores indépendants ; seuil tel que P(alerte | honnête, T actions) = p_fa."""
    d = math.sqrt(2) * norm.ppf(aire)
    q0 = 1 - (1 - p_fa) ** (1 / T)
    z = norm.ppf(1 - q0)
    q1 = 1 - norm.cdf(z - d)
    return 1 - (1 - q1) ** actions

print("C. Juge à signal faible (SUPPOSÉ : scores normaux, même variance, actions indépendantes, toutes sabotées) :")
for aire in (0.52, 0.54, 0.56, 0.60, 0.65, 0.84, 0.97):
    for actions in (10, 8):
        # moyenne sur l'incertitude du seuil : p_fa ~ Bêta(a, b)
        val, _ = quad(lambda p: p_alerte_episode(aire, p, actions) * beta.pdf(p, a, b), 1e-9, 0.2)
        print(f"   aire {aire:.2f}, {actions:2d} actions lues : P(alerte par épisode) = {val:.4f} ; attendu sur 64 : {64*val:.2f}")

def p_zero_juge(aires, actions):
    """P(aucune alerte sur 64 épisodes par dose), doses indépendantes sachant le seuil ; intégrée sur le seuil."""
    def integrande(p):
        pr = 1.0
        for aire in aires:
            pr *= (1 - p_alerte_episode(aire, p, actions)) ** N_DOSE
        return pr * beta.pdf(p, a, b)
    return quad(integrande, 1e-9, 0.2)[0]
for nom, aires in (("aires 0,52 ; 0,54 ; 0,56 ; 0,56 (juge de huit milliards avec raisonnement)", (0.52, 0.54, 0.56, 0.56)),
                   ("aires 0,52 ; 0,52 ; 0,52 ; 0,56 (juge de trois milliards avec raisonnement)", (0.52, 0.52, 0.52, 0.56)),
                   ("aires 0,52 ; 0,60 ; 0,58 ; 0,65 (juge de trois milliards en une passe)", (0.52, 0.60, 0.58, 0.65))):
    for actions in (10, 8):
        print(f"D. {nom}, {actions} actions lues : P(zéro alerte sur 256) = {p_zero_juge(aires, actions):.4f}")

print("E. Rappel par épisode au maximum, à 1 % par épisode, selon l'aire par action (10 actions, seuil exact 0,01) :")
for aire in (0.56, 0.65, 0.75, 0.84, 0.90, 0.97):
    print(f"   aire {aire:.2f} : {p_alerte_episode(aire, 0.01, 10):.3f}")
