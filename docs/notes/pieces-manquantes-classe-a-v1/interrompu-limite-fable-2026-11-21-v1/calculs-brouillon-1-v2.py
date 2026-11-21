"""Calculs cités par `brouillon-1-v2.md` (prévision chiffrée de la loi de la référence honnête, version 2).

Aucune donnée du programme n'est lue. Aucun tirage au hasard, aucune simulation : formes fermées,
intégrales à une dimension (règle de Simpson) et convolutions exactes de lois de rangs.
Tout chiffre vaut sous supposition (scores normaux, unités indépendantes, jumeau exact sauf mention,
approximation normale là où c'est dit) ; aucun n'est une mesure.

Blocs A à L : ceux de la version 1, recopiés à l'identique (le bloc L est gardé pour comparaison).
Blocs M à Z : ajouts de la version 2, un par correction (table en tête du brouillon).

Lancer : python3 calculs-brouillon-1-v2.py > calculs-brouillon-1-v2.txt
"""
import math
from statistics import NormalDist as N

import numpy as np

P = N().cdf
q = N().inv_cdf
phi = N().pdf
z = q(.99)
b = lambda x: round(100 * (1 - P(z - 1.645 / math.sqrt(x))), 1)

print("== Blocs de la version 1, recopiés à l'identique ==")
print("A", round(z, 4), round(math.sqrt(5 / 8), 4), round(math.sqrt(.5), 4), round(math.sqrt(1 / 4), 4))
print("B", round(math.sqrt(.75), 4), round(4 ** -.6, 4), round(4 ** -.4, 4))
print("C", round(math.sqrt(6 / 4) / math.sqrt(2), 4), round(math.sqrt(6 / 4) / math.sqrt(5), 4), round(2 / 4, 2))
print("D", [round(100 * P(z * (math.sqrt(r / (1 + r)) - 1)), 1) for r in (.5, 1, 2, 4)], [round(100 * P(z * (math.sqrt(r * 4 / 6) - 1)), 1) for r in (.5, 1, 2, 4)])
print("E", round(100 * P(z * (1 / .75 - 1)), 1), round(100 * P(z * (1 / math.sqrt(6 / 4 / 5) - 1)), 1))
print("F", [round(100 * (1 - P(z / math.sqrt(1 + r))), 1) for r in (.25, 1, 4)])
print("G", [round((1.645 / (z - q(1 - .01 * f))) ** 2, 1) for f in (2, 3, 5)])
print("H", [b(x) for x in (60, 15, 24, 6, 6, 1.5)])
print("I", round(1 + 1.645 / math.sqrt(24) / (z / 2), 3), round(1 + 1.645 / math.sqrt(60) / (z / 2), 3))
print("J", [round(z * math.sqrt(math.pi / 3) * math.sqrt(2) / math.sqrt(m), 2) for m in (40, 100, 400)])
print("K", round(math.sqrt(101) / math.sqrt(math.pi * 6 / 12), 2), round(math.sqrt(101) / math.sqrt(math.pi * 5 / 9), 2), round(100 * z / (0.5 * math.sqrt(400)), 1))
print("L", [round(math.sqrt(x) / z, 3) for x in (160 / 2400, 400 / 2400, 1600 / 2400)], [round(100 * P((.75 / math.sqrt(6 / 4 / 5) - 1) / (math.sqrt(x) / z) - 1.96)) for x in (160 / 2400, 400 / 2400, 1600 / 2400)])

# ---------------------------------------------------------------------------------------------
# Outils communs aux blocs de la version 2
# ---------------------------------------------------------------------------------------------
REGLAGES = (("A", 2400, 40), ("B", 2400, 100), ("C", 2400, 400))   # (nom, mondes W, référence m) ; n_max = 4 m
K = 4                                     # tirages du jumeau par unité
SIG = math.sqrt(K * (K + 2) / 12)         # écart type du rang d'une unité sous le nul


def simpson(f, a, c, pas=4000):
    h = (c - a) / pas
    s = f(a) + f(c)
    for i in range(1, pas):
        s += (4 if i % 2 else 2) * f(a + i * h)
    return s * h / 3


def loi_rang(mu, k=K):
    """Loi du nombre de tirages du jumeau dépassés (0 à k) : unité N(mu, 1), jumeaux N(0, 1), indépendants."""
    return [simpson(lambda x, j=j: phi(x - mu) * math.comb(k, j) * P(x) ** j * (1 - P(x)) ** (k - j), -10, 10 + mu) for j in range(k + 1)]


def conv_n(loi, n):
    """Loi exacte de la somme de n tirages indépendants de `loi` (convolution par carrés successifs)."""
    res, base = np.array([1.0]), np.array(loi, dtype=float)
    while n:
        if n & 1:
            res = np.convolve(res, base)
        n >>= 1
        if n:
            base = np.convolve(base, base)
    return res


def seuil_exact(n, k=K, alpha=0.01):
    """Seuil t tel que P(S + V > t) = alpha exactement sous le nul : S somme de n rangs uniformes sur 0..k,
    V tirage uniforme sur [0, 1) indépendant (c'est le tirage au sort à la valeur critique, écrit en continu)."""
    nul = conv_n([1 / (k + 1)] * (k + 1), n)
    queue = 0.0
    for c in range(len(nul) - 1, -1, -1):
        if queue + nul[c] > alpha:
            return c + 1 - (alpha - queue) / nul[c]
        queue += nul[c]


def depasse(loi, t):
    """P(S + V > t) pour S de loi `loi` sur 0..len-1 et V uniforme sur [0, 1) indépendant."""
    j = np.arange(len(loi))
    return float((loi * np.clip(j + 1 - t, 0, 1)).sum())


def rappel(pa, pb, n, s, t):
    """Rappel exact à l'horizon n d'un flux où chaque unité est sabotée avec probabilité s."""
    return depasse(conv_n([(1 - s) * u + s * v for u, v in zip(pa, pb)], n), t)


def part_cachee(pa, pb, n, t):
    """Dose à laquelle le rappel exact vaut 50 % (bissection) ; infini si la dose pleine ne l'atteint pas."""
    if rappel(pa, pb, n, 1.0, t) < 0.5:
        return float("inf")
    bas, haut = 0.0, 1.0
    for _ in range(50):
        mil = (bas + haut) / 2
        bas, haut = (mil, haut) if rappel(pa, pb, n, mil, t) < 0.5 else (bas, mil)
    return (bas + haut) / 2


def moyenne_centree(loi):
    return sum(j * v for j, v in enumerate(loi)) - (len(loi) - 1) / 2


def ecart_type(loi):
    mo = sum(j * v for j, v in enumerate(loi))
    return math.sqrt(sum((j - mo) ** 2 * v for j, v in enumerate(loi)))


def esperance_normale(f, bornes=8.0, pas=4000):
    """Espérance de f(xi) pour xi normale réduite."""
    return simpson(lambda x: phi(x) * f(x), -bornes, bornes, pas)


UNIF = [1 / (K + 1)] * (K + 1)

print()
print("== Blocs ajoutés par la version 2 ==")

# ---------------------------------------------------------------------------------------------
# M. Remarque 2 : « cesse de croître ». Rappel de la statistique étalonnée à dose fixe, entre m et 4 m.
#    R(r ; a) = Phi(z (a racine(r / (1 + r)) - 1)), r = n / m, a = dose / part cachée à horizon infini.
# ---------------------------------------------------------------------------------------------
ret = lambda a, r: P(z * (a * math.sqrt(r / (1 + r)) - 1))
gain, a_max = max((ret(a / 1000, 4) - ret(a / 1000, 1), a / 1000) for a in range(500, 3001))
print("M", "a = 1 :", round(100 * ret(1, 1), 1), "->", round(100 * ret(1, 4), 1), "plafond", round(100 * P(0), 1),
      "| gain le plus grand entre m et 4 m :", round(100 * gain, 1), "points, à a =", a_max,
      "(", round(100 * ret(a_max, 1), 1), "->", round(100 * ret(a_max, 4), 1), ", plafond", round(100 * P(z * (a_max - 1)), 1), ")")

# ---------------------------------------------------------------------------------------------
# N. Remarque 4 : doublons d'un flux tiré avec remise parmi les W - m autres mondes ; et ce que le tirage
#    sans remise fait au rang quand le vivier est fini (f = n_max / W).
# ---------------------------------------------------------------------------------------------
for nom, W, m in REGLAGES:
    n, autres = 4 * m, W - m
    p_doublon = 1 - math.exp(sum(math.log(1 - i / autres) for i in range(n)))
    part_doublons = 1 - autres * (1 - (1 - 1 / autres) ** n) / n
    f = n / W
    mediane_sans = 100 * (1 - P(z / math.sqrt(1 - f)))          # taux réalisé médian du seuil nominal, flux sans remise
    moyenne_avec = 100 * (1 - P(z / math.sqrt(1 + f)))          # taux réalisé moyen, loi empirique (avec remise)
    erreur_bord = 100 * P(q(0.97) * (1 - math.sqrt(1 - f)) / math.sqrt(f) - 1.645)   # attestation à tort « sous 3 % », au bord
    print("N", nom, "n_max =", n, "<= W - m =", autres, ":", n <= autres, "| au moins un doublon :", round(100 * p_doublon, 1), "% ; part de doublons :",
          round(100 * part_doublons, 1), "% | rang, sans remise : médiane", round(mediane_sans, 2), "% ; loi empirique : moyenne", round(moyenne_avec, 2),
          "% | attestation à tort au bord, sans remise :", round(erreur_bord, 1), "% (5 % visés)")

# ---------------------------------------------------------------------------------------------
# O. Remarque 8 : rangs simples ou scores normaux du rang rendu continu (statistique de la note « percée »).
#    Efficacité = écart réduit gagné par unité sabotée, divisé par mu (le test sur la moyenne à référence exacte vaut 1).
# ---------------------------------------------------------------------------------------------
def efficacite_rang_simple(mu, k):
    return k * (P(mu / math.sqrt(2)) - .5) / math.sqrt(k * (k + 2) / 12) / mu


def efficacite_score_normal(mu, k):
    a = [None] + [q(r / (k + 1)) for r in range(1, k + 1)] + [None]
    dens = [0.0] + [phi(v) for v in a[1:-1]] + [0.0]
    interieur = [(k + 1) * (dens[r] - dens[r + 1]) for r in range(k + 1)]
    return simpson(lambda x: phi(x - mu) * sum(math.comb(k, r) * P(x) ** r * (1 - P(x)) ** (k - r) * interieur[r] for r in range(k + 1)), -10, 10 + mu) / mu


es0, es5, en5 = math.sqrt(3 * 4 / (math.pi * 6)), efficacite_rang_simple(0.5, 4), efficacite_score_normal(0.5, 4)
print("O", "rang simple, K = 4 : petit écart", round(es0, 4), "; mu = 0,5 :", round(es5, 4), "| score normal du rang rendu continu, mu = 0,5 : K = 4 :", round(en5, 4),
      "; K = 19 :", round(efficacite_score_normal(0.5, 19), 4), "| rapport à 1 % de témoins :", round(math.sqrt(101) * es0, 2), round(math.sqrt(101) * es5, 2),
      round(math.sqrt(101) * en5, 2), "| kappa serait multiplié par", round(es5 / en5, 3), "avec le score normal")

# ---------------------------------------------------------------------------------------------
# P. Remarque 5 : erreur de l'écart kappa entre les deux courbes, selon la lecture du rang.
#    Modèle : par monde, un original honnête y ~ N(0,1), K jumeaux N(0,1), un épisode saboté x' ~ N(mu,1), indépendants.
#    a = rang centré de l'original, b = rang centré du saboté, psi = part du monde dans l'estimation de p_r.
#    Partie linéaire de ln(kappa estimé), par monde (c = part cachée nominale à l'horizon lu, tau = c b) :
#      lecture « flux au seuil nominal » (version 1)   : -(1 - c) a / tau - b / b_moyen + psi / delta
#      lecture « par construction » (jumeau supposé)   :                  - b / b_moyen + psi / delta
#      lecture attestée                                :        (a - b) / b_moyen + psi / delta
# ---------------------------------------------------------------------------------------------
def moments(mu, k=K):
    pj = P(mu / math.sqrt(2))
    e_phi2_x = simpson(lambda x: phi(x - mu) * P(x) ** 2, -10, 10 + mu)
    p_deux = simpson(lambda t: phi(t) * (1 - P(t)) * (1 - P(t - mu)), -10, 10)
    e_croise = simpson(lambda y: phi(y) * P(y) * P(y - mu), -10, 10)
    e_phi2_y = simpson(lambda y: phi(y) * P(y - mu) ** 2, -10, 10)
    return dict(pj=pj, var_a=k * (k + 2) / 12, var_b=k * pj * (1 - pj) + k * (k - 1) * (e_phi2_x - pj ** 2), cov_ab=k * (p_deux - .5 * pj),
                cov_a_psi=-k * (e_croise - .5 * (1 - pj)), cov_b_psi=k * (e_phi2_x - pj ** 2), var_psi=(e_phi2_x - pj ** 2) + (e_phi2_y - (1 - pj) ** 2))


def variance_par_monde(mu, c, lecture, k=K):
    M = moments(mu, k)
    delta = M["pj"] - .5
    bm = k * delta
    tau = c * bm
    if lecture == "attestee":
        return (M["var_a"] + M["var_b"] - 2 * M["cov_ab"]) / bm ** 2 + M["var_psi"] / delta ** 2 + 2 * (M["cov_a_psi"] - M["cov_b_psi"]) / (bm * delta)
    if lecture == "construction":
        return M["var_b"] / bm ** 2 + M["var_psi"] / delta ** 2 - 2 * M["cov_b_psi"] / (bm * delta)
    return ((1 - c) ** 2 * M["var_a"] / tau ** 2 + M["var_b"] / bm ** 2 + M["var_psi"] / delta ** 2 + 2 * (1 - c) * M["cov_ab"] / (tau * bm)
            - 2 * (1 - c) * M["cov_a_psi"] / (tau * delta) - 2 * M["cov_b_psi"] / (bm * delta))


def facteur(mu, c, lecture, k=K):
    """Écart type relatif de kappa estimé, en multiple de racine(n / W) / z, à l'horizon n où la part cachée nominale vaut c."""
    delta = P(mu / math.sqrt(2)) - .5
    n = z ** 2 * (k + 2) / (12 * k * c ** 2 * delta ** 2)
    return math.sqrt(variance_par_monde(mu, c, lecture, k)) / (math.sqrt(n) / z)


print("P1", "formes fermées (petit écart), en multiple de racine(n/W)/z : flux = racine((K + 2(1 - c + c²))/(K + 2)) ; construction = c ; attestée = c racine(2/(K + 2))")
for mu in (0.02, 0.5, 1.0):
    print("P1", "mu =", mu, [(c, round(facteur(mu, c, "flux"), 3), round(facteur(mu, c, "construction"), 3), round(facteur(mu, c, "attestee"), 3)) for c in (0.25, 0.5, 1.0)],
          "| formes fermées :", [(c, round(math.sqrt((K + 2 * (1 - c + c * c)) / (K + 2)), 3), c, round(c * math.sqrt(2 / (K + 2)), 3)) for c in (0.25, 0.5, 1.0)])

NH, ND = 20000, 2000                                           # configurations honnêtes (seuil recalé) et dosées, par lecture
ERR_SEUIL = math.sqrt(.01 * .99 / NH) / phi(z) / z              # erreur relative du seuil recalé (quantile empirique à 99 %)
ERR_RAPPEL = math.sqrt(.25 / ND) / phi(0) / z                   # erreur relative de la part cachée due au rappel estimé près de 50 %
ERR_C1 = math.hypot(ERR_SEUIL, ERR_RAPPEL)                      # erreur relative de tirage de c1 à un horizon
KAPPA = math.sqrt((K + 2) / K) / math.sqrt(5)                   # écart prédit par construction, E = 1, n_max = 4 m
print("P2", "erreur de tirage de c1 :", round(100 * ERR_SEUIL, 2), "% (seuil recalé,", NH, "configurations) et", round(100 * ERR_RAPPEL, 2), "% (rappel,", ND,
      "configurations) ; ensemble", round(100 * ERR_C1, 2), "%")


def chance(kappa, s, seuil=0.75):
    """Probabilité que la borne haute à 95 % de kappa passe sous le seuil : kappa estimé ~ N(kappa, (kappa s)²), borne = estimé (1 + 1,96 s)."""
    return P((seuil / (1 + 1.96 * s) - kappa) / (kappa * s))


for nom, W, m in REGLAGES:
    base = math.sqrt(4 * m / W) / z
    k_att = KAPPA * (1 + 1.645 * math.sqrt(4 * m / W) / z)
    lignes = []
    for c in (0.25, 0.5, 1.0):
        s_flux = math.hypot(base * math.sqrt((K + 2 * (1 - c + c * c)) / (K + 2)), ERR_C1)
        s_att = math.hypot(base * c * math.sqrt(2 / (K + 2)), ERR_C1)
        lignes.append((c, round(100 * s_flux, 1), round(100 * chance(KAPPA, s_flux)), round(100 * s_att, 1), round(100 * chance(k_att, s_att))))
    print("P3", nom, "W/m =", W // m, "racine(n_max/W)/z =", round(base, 3), "| kappa par construction", round(KAPPA, 4), "; attesté", round(k_att, 4),
          "| (c2 à n_max ; flux au seuil nominal : erreur %, chances % ; attestée : erreur %, chances %) :", lignes)
for wm, k in ((60, 9), (120, 4), (240, 4)):
    base = math.sqrt(4 / wm) / z
    kap = math.sqrt((k + 2) / k) / math.sqrt(5)
    k_att = kap * (1 + 1.645 * math.sqrt(4 / wm) / z)
    print("P4", "W/m =", wm, "K =", k, "| kappa attesté", round(k_att, 4), "| chances % pour c2(n_max) = 0,25 ; 0,5 ; 1 :",
          [round(100 * chance(k_att, math.hypot(base * c * math.sqrt(2 / (k + 2)), ERR_C1))) for c in (0.25, 0.5, 1.0)])

# ---------------------------------------------------------------------------------------------
# Q. Valeurs prédites de la lecture attestée (approximation normale, jumeau exact, E = 1, n_max = 4 m).
#    rho2 attesté = (z/2 + 1,645 racine(m/W)) / (z + 1,645 racine(m/W)) ; kappa attesté = kappa (1 + 1,645 racine(4m/W)/z).
# ---------------------------------------------------------------------------------------------
for wm in (15, 24, 60, 120, 240):
    v = 1.645 * math.sqrt(1 / wm)
    print("Q", "W/m =", wm, "| rho2 attesté", round((z / 2 + v) / (z + v), 4), "| kappa attesté : K = 4 :", round(KAPPA * (1 + 2 * v / z), 4),
          "; K = 9 :", round(math.sqrt(11 / 9) / math.sqrt(5) * (1 + 2 * v / z), 4),
          "| taux de fausses alertes du seuil relevé, jumeau exact : à m", round(100 * (1 - P(z + v)), 2), "% ; à 4 m", round(100 * (1 - P(z + 2 * v)), 2), "%",
          "| horizon où le relèvement d'attestation égale le seuil lui-même : n =", round((z / 1.645) ** 2, 2), "W")
print("Q", "W minimal pour que kappa attesté prédit passe sous 0,75 (K = 4, marge nulle) : W/m =", round(4 * (1.645 / (z * (0.75 / KAPPA - 1))) ** 2, 1),
      "; pour kappa attesté prédit = 0,65 : W/m =", round(4 * (1.645 / (z * (0.65 / KAPPA - 1))) ** 2, 1))

# ---------------------------------------------------------------------------------------------
# R. Les étiquettes de validité du seuil nominal du rang, jumeau exact : ce que valent leurs chances.
#    xi = dérive de tirage du vivier, normale réduite ; taux réalisé à l'horizon n = 1 - Phi(z - xi racine(n/W)).
# ---------------------------------------------------------------------------------------------
for wm in (60, 120, 173, 240):
    f1, f4 = 1 / wm, 4 / wm
    print("R", "W/m =", wm, "| borne haute médiane du taux réalisé : à m", round(100 * (1 - P(z - 1.645 * math.sqrt(f1))), 1), "% ; à 4 m", round(100 * (1 - P(z - 1.645 * math.sqrt(f4))), 1),
          "% | chances d'attester « au plus 3 % » à 4 m :", round(100 * P((z - q(.97)) / math.sqrt(f4) - 1.645), 1), "% ; « au plus 5 % » :", round(100 * P((z - q(.95)) / math.sqrt(f4) - 1.645), 1),
          "% | garde « démentie » (borne basse au-dessus de 2 %) levée à tort à m :", f"{1 - P(1.645 + (z - q(.98)) / math.sqrt(f1)):.1e}",
          "| levée si le nul est décalé de 0,68 écart type à m :", round(100 * P(0.68 / math.sqrt(f1) - 1.645 - (z - q(.98)) / math.sqrt(f1)), 1), "% ; d'un écart type :",
          round(100 * P(1 / math.sqrt(f1) - 1.645 - (z - q(.98)) / math.sqrt(f1)), 2), "%")

print("R", "unités honnêtes à vérifier, en multiple de l'horizon, pour attester « au plus 2, 3, 5 fois 1 % » : une fois sur deux", [round((1.645 / (z - q(1 - .01 * f))) ** 2, 1) for f in (2, 3, 5)],
      "; neuf fois sur dix", [round(((1.645 + q(.9)) / (z - q(1 - .01 * f))) ** 2, 1) for f in (2, 3, 5)])
print("R", "condition de lisibilité (écart par unité, en écart type) pour m = 20, 40, 100, 400 :", [round(z * math.sqrt(math.pi / 3) * math.sqrt(2) / math.sqrt(mm), 2) for mm in (20, 40, 100, 400)])

# ---------------------------------------------------------------------------------------------
# U. Remarque 6 : l'effet planté de l'étape 0 et les vérités exactes du rang (réglage A : m = 40, W = 2 400, K = 4).
#    Effet planté : le décalage mu0 pour lequel la formule donne c1(m) = 0,60.
# ---------------------------------------------------------------------------------------------
m, W = 40, 2400
GRILLE = (m // 4, m // 2, m, 2 * m, 4 * m)
delta0 = z * math.sqrt((2 * m + 1) / (12 * m * m)) / 0.6
mu0 = math.sqrt(2) * q(.5 + delta0)
pb0 = loi_rang(mu0)
c1 = {n: z * math.sqrt((n + m + 1) / (12 * n * m)) / delta0 for n in GRILLE}
rho1 = c1[4 * m] / c1[m]
seuils = {n: seuil_exact(n) for n in GRILLE}
c2 = {n: part_cachee(UNIF, pb0, n, seuils[n]) for n in GRILLE}
u0 = 1.645 * SIG / math.sqrt(W)
c2a = {n: part_cachee(UNIF, pb0, n, seuils[n] + n * u0) for n in GRILLE}
print("U", "contrôle : loi du rang sans décalage", [round(v, 6) for v in loi_rang(0.0)], "; taux exact du seuil à m :", round(100 * depasse(conv_n(UNIF, m), seuils[m]), 6), "%")
print("U", "delta0 =", round(delta0, 4), "mu0 =", round(mu0, 4), "| loi du rang saboté", [round(v, 4) for v in pb0], "moyenne centrée", round(moyenne_centree(pb0), 4), "écart type", round(ecart_type(pb0), 4))
print("U", "c1 (formule) sur la grille", [round(c1[n], 4) for n in GRILLE], "rho1 =", round(rho1, 4), "| taille utile attendue m + 1 =", m + 1)
print("U", "c2 exact, par construction", [round(c2[n], 4) for n in GRILLE], "rho2 =", round(c2[4 * m] / c2[m], 4), "| formule", [round(z * math.sqrt((K + 2) / (12 * K * n)) / delta0, 4) for n in GRILLE])
print("U", "c2 exact, attesté (W = 60 m)", [round(c2a[n], 4) for n in GRILLE], "rho2 =", round(c2a[4 * m] / c2a[m], 4), "| kappa : par construction", round(c2[4 * m] / c1[4 * m], 4),
      "; attesté", round(c2a[4 * m] / c1[4 * m], 4), "| dose cachée par l'écart du jumeau, à sa borne :", round(100 * u0 / moyenne_centree(pb0), 2), "% =", round(u0 / moyenne_centree(pb0) / c2[m], 4), "fois c2(m)")
print("U", "rappel du rang attesté à la dose où la statistique étalonnée rappelle 50 % à 4 m :", round(100 * rappel(UNIF, pb0, 4 * m, c1[4 * m], seuils[4 * m] + 4 * m * u0), 1),
      "% ; par construction :", round(100 * rappel(UNIF, pb0, 4 * m, c1[4 * m], seuils[4 * m]), 1), "%")

# ---------------------------------------------------------------------------------------------
# V. Objets plantés où le jumeau n'est pas un jumeau (vérités exactes par convolution, réglage A), et ce qu'y rendent
#    les trois lectures du rang. Les jumeaux sont décalés ; l'original honnête et la référence gardent leur loi (c1 inchangé).
# ---------------------------------------------------------------------------------------------
def trois_lectures(pa, pb):
    """kappa à 4 m et rho2 selon la lecture : par construction, flux au seuil nominal (version 1), attestée."""
    d, s_a = moyenne_centree(pa), ecart_type(pa)
    u = max(0.0, d + 1.645 * s_a / math.sqrt(W))
    sortie = {}
    for nom, loi_h, releve in (("construction", UNIF, 0.0), ("flux", pa, 0.0), ("attestee", pa, u)):
        cm, c4 = (part_cachee(loi_h, pb, n, seuils[n] + n * releve) for n in (m, 4 * m))
        sortie[nom] = (c4 / c1[4 * m], c4 / cm)
    return d, u, sortie


def affiche(nom, d, u, sortie):
    print(nom, "rang centré moyen de l'original", round(d, 4), "; relèvement", round(u, 4), "| (kappa, rho2) : par construction", tuple(round(v, 3) for v in sortie["construction"]),
          "; flux au seuil nominal", tuple(round(v, 3) for v in sortie["flux"]), "; attestée", tuple(round(v, 3) for v in sortie["attestee"]))


affiche("V0 jumeau exact :", *trois_lectures(UNIF, pb0))

# V1. Jumeau faussé vers le haut : l'original honnête dépasse ses jumeaux, de quoi décaler la somme de un écart type à n = m.
bas, haut = 0.0, 1.0
for _ in range(60):
    mil = (bas + haut) / 2
    bas, haut = (mil, haut) if K * (P(mil / math.sqrt(2)) - .5) < SIG / math.sqrt(m) else (bas, mil)
theta_haut = (bas + haut) / 2
pa_haut, pb_haut = loi_rang(theta_haut), loi_rang(mu0 + theta_haut)
fa_haut = {n: depasse(conv_n(pa_haut, n), seuils[n]) for n in GRILLE}
print("V1", "jumeaux décalés de", round(-theta_haut, 4), "| taux exact du seuil nominal sur la grille %", [round(100 * fa_haut[n], 2) for n in GRILLE],
      "| approximation normale à m :", round(100 * (1 - P(z - 1)), 2), "% ; moyenne sur les viviers :", round(100 * (1 - P((z - 1) / math.sqrt(1 + m / W))), 2), "%")
affiche("V1 jumeau faussé vers le haut :", *trois_lectures(pa_haut, pb_haut))
# V1 bis. Le même, plus faible : 0,3 écart type à n = m, que la garde « validité démentie » ne voit presque jamais.
bas, haut = 0.0, 1.0
for _ in range(60):
    mil = (bas + haut) / 2
    bas, haut = (mil, haut) if K * (P(mil / math.sqrt(2)) - .5) < 0.3 * SIG / math.sqrt(m) else (bas, mil)
theta_faible = (bas + haut) / 2
print("V1 bis", "jumeaux décalés de", round(-theta_faible, 4), "| garde levée, par vivier :", round(100 * P(0.3 / math.sqrt(m / W) - 1.645 - (z - q(.98)) / math.sqrt(m / W)), 1),
      "% | taux exact du seuil nominal à m et à 4 m %", [round(100 * depasse(conv_n(loi_rang(theta_faible), n), seuils[n]), 2) for n in (m, 4 * m)])
affiche("V1 bis jumeau faussé vers le haut, faible :", *trois_lectures(loi_rang(theta_faible), loi_rang(mu0 + theta_faible)))


# V2. Jumeau décalé vers le bas : l'original honnête est sous ses jumeaux ; la part cachée du rang reçoit un plancher.
CIBLE_BAS = 0.70


def rho2_bas(theta):
    r = trois_lectures(loi_rang(-theta), loi_rang(mu0 - theta))[2]["attestee"][1]
    return r if math.isfinite(r) else 1.0


bas, haut = 0.0, 0.6
for _ in range(40):
    mil = (bas + haut) / 2
    bas, haut = (mil, haut) if rho2_bas(mil) < CIBLE_BAS else (bas, mil)
theta_bas = (bas + haut) / 2
pa_bas, pb_bas = loi_rang(-theta_bas), loi_rang(mu0 - theta_bas)
d_bas, u_bas, lect_bas = trois_lectures(pa_bas, pb_bas)
b_bas = moyenne_centree(pb_bas)
rho2_cible = lect_bas["attestee"][1]
sd_rho2_bas = rho2_cible * abs(1 / (z * SIG / math.sqrt(4 * m) - d_bas) - 1 / (z * SIG / math.sqrt(m) - d_bas)) * ecart_type(pa_bas) / math.sqrt(W)
print("V2", "jumeaux décalés de", round(theta_bas, 4), "| rang centré moyen du saboté", round(b_bas, 4), "| plancher de la part cachée :", round(-d_bas / (b_bas - d_bas), 4),
      "| écart type de rho2 attesté d'un vivier à l'autre :", round(sd_rho2_bas, 4))
affiche("V2 jumeau décalé vers le bas :", d_bas, u_bas, lect_bas)

# ---------------------------------------------------------------------------------------------
# S. Remarque 6 : erreurs types et tolérances de l'étape 0 (réglage A ; G viviers plantés de la taille du banc par objet).
#    Tolérance = 4 erreurs types de la moyenne des G lectures, plus une marge d'approximation là où la vérité est une formule.
# ---------------------------------------------------------------------------------------------
G = 100
sd_rho1 = math.sqrt(2) * ERR_C1                                   # relatif ; horizons tenus pour indépendants (majorant)
print("S1", "rho1, par vivier : écart type relatif", round(100 * sd_rho1, 2), "% soit", round(rho1 * sd_rho1, 4), "| moyenne de", G, "viviers : erreur type", round(rho1 * sd_rho1 / math.sqrt(G), 4),
      "; quatre erreurs types", round(4 * rho1 * sd_rho1 / math.sqrt(G), 4))
for nom, valeur in (("référence de 100 m", math.sqrt((4 * m + 100 * m + 1) / (4 * (m + 100 * m + 1)))), ("référence d'un autre régime, taille utile m/2", math.sqrt((1 / (4 * m) + 2 / m) / (1 / m + 2 / m)))):
    print("S1", nom, ": rho1 attendu", round(valeur, 4), "; quatre erreurs types de la moyenne", round(4 * valeur * sd_rho1 / math.sqrt(G), 4))

f_att = math.sqrt(variance_par_monde(mu0, c2[4 * m], "attestee") / W)   # erreur relative de kappa attesté due au vivier
sd_kappa = math.hypot(f_att, ERR_C1)
k_att0 = c2a[4 * m] / c1[4 * m]
print("S2", "kappa attesté, par vivier : vivier", round(100 * f_att, 2), "% ; tirage", round(100 * ERR_C1, 2), "% ; ensemble", round(100 * sd_kappa, 2), "% soit", round(k_att0 * sd_kappa, 4),
      "| moyenne de", G, ": erreur type", round(k_att0 * sd_kappa / math.sqrt(G), 4), "; quatre erreurs types", round(4 * k_att0 * sd_kappa / math.sqrt(G), 4))

tau = {n: z * SIG / math.sqrt(n) for n in GRILLE}                 # seuil en unité de rang centré moyen (approximation normale)
pas_vivier = SIG / math.sqrt(W)                                   # écart type de la dérive de tirage d'un vivier


def rho2_att(xi):
    x = max(u0, -xi * pas_vivier)                                 # relèvement net du numérateur ; plancher à zéro actif si xi < -1,645
    return (tau[4 * m] + x) / (tau[m] + x)


e_rho2 = esperance_normale(rho2_att)
sd_rho2 = math.sqrt(esperance_normale(lambda x: rho2_att(x) ** 2) - e_rho2 ** 2)
print("S3", "rho2 attesté, jumeau exact : valeur centrale", round(rho2_att(0), 4), "; moyenne", round(e_rho2, 4), "; écart type par vivier", round(sd_rho2, 4), "; borne haute à 97,5 % :", round(rho2_att(-1.96), 4),
      "| quatre erreurs types de la moyenne de", G, ":", round(4 * sd_rho2 / math.sqrt(G), 4), "| écart de l'exact à la formule (bloc U) :", round(c2a[4 * m] / c2a[m] - rho2_att(0), 4))

for n in GRILLE:
    f = n / W
    fa = lambda xi, f=f: 1 - P(z - xi * math.sqrt(f))
    e_fa = esperance_normale(fa)
    sd_fa = math.sqrt(esperance_normale(lambda x: fa(x) ** 2) - e_fa ** 2)
    print("S4", "taux réalisé du seuil nominal du rang (loi empirique), n =", n, ": médiane 1,00 % ; moyenne", round(100 * e_fa, 3), "% ; écart type par vivier", round(100 * sd_fa, 3),
          "point | bande de la moyenne de", G, "à quatre erreurs types :", round(100 * (e_fa - 4 * sd_fa / math.sqrt(G)), 2), "à", round(100 * (e_fa + 4 * sd_fa / math.sqrt(G)), 2), "%")

sd_fa_haut = phi(z - 1) * math.sqrt(m / W)
print("S5", "jumeau faussé vers le haut, taux à m : exact au centre", round(100 * fa_haut[m], 2), "% ; écart type par vivier", round(100 * sd_fa_haut, 2), "points ; quatre erreurs types de la moyenne de", G, ":",
      round(100 * 4 * sd_fa_haut / math.sqrt(G), 2), "point ; la courbure relève la moyenne de", round(100 * ((1 - P((z - 1) / math.sqrt(1 + m / W))) - (1 - P(z - 1))), 2), "point")


def binomiale_type(p, n_conf):
    return 100 * math.sqrt(p * (1 - p) / n_conf)


naif = {n: 1 - P(z / math.sqrt((n + m + 1) / m)) for n in (m, 4 * m)}
autre = {n: 1 - P(z / math.sqrt((1 / n + 2 / m) / (1 / n + 1 / m))) for n in (m, 4 * m)}
rho_rang = 6 / math.pi * math.asin(0.2 / 2)
effet_plan = 1 + 4 * rho_rang
grappes = 1 - P(z / math.sqrt(effet_plan))
print("S6", "seuil recalé rejoué sur des configurations neuves : par vivier", round(binomiale_type(.01, NH) * math.sqrt(2), 3), "point ; quatre erreurs types de la moyenne de", G, ":",
      round(4 * binomiale_type(.01, NH) * math.sqrt(2) / math.sqrt(G), 3), "point")
print("S6", "étalonnage naïf : attendu", [round(100 * naif[n], 2) for n in (m, 4 * m)], "% ; quatre erreurs types de la moyenne :", [round(4 * binomiale_type(naif[n], NH) / math.sqrt(G), 3) for n in (m, 4 * m)], "point")
print("S6", "référence d'un autre régime, seuil nominal à deux échantillons : attendu", [round(100 * autre[n], 2) for n in (m, 4 * m)], "% ; quatre erreurs types :",
      [round(4 * binomiale_type(autre[n], NH) / math.sqrt(G), 3) for n in (m, 4 * m)], "point | variance du décalage de régime à planter :", round(math.pi / 3 * (2 * m + 1) / (2 * m * m), 5))
print("S6", "grappes de 5, corrélation 0,2 : corrélation de rang", round(rho_rang, 4), "; effet de plan", round(effet_plan, 4), "; seuil recalé par unités brassées : attendu", round(100 * grappes, 2),
      "% ; quatre erreurs types :", round(4 * binomiale_type(grappes, NH) / math.sqrt(G), 3), "point")
print("S6", "monde nul, rappel à une dose et un horizon : par vivier", round(math.hypot(binomiale_type(.01, ND), binomiale_type(.01, NH)), 3), "point ; quatre erreurs types de la moyenne :",
      round(4 * math.hypot(binomiale_type(.01, ND), binomiale_type(.01, NH)) / math.sqrt(G), 3), "point")

# Taille utile : pente sur ordonnée de la droite des moindres carrés de c1² contre 1/n ; propagation au premier ordre, erreurs indépendantes.
xs = [1 / n for n in GRILLE]
ys = [c1[n] ** 2 for n in GRILLE]
xm = sum(xs) / len(xs)
sxx = sum((x - xm) ** 2 for x in xs)
wp = [(x - xm) / sxx for x in xs]
wo = [1 / len(xs) - xm * w for w in wp]
pente, ordonnee = sum(w * y for w, y in zip(wp, ys)), sum(w * y for w, y in zip(wo, ys))
var_y = [(2 * ERR_C1 * y) ** 2 for y in ys]
vp, vo, cpo = sum(w * w * v for w, v in zip(wp, var_y)), sum(w * w * v for w, v in zip(wo, var_y)), sum(a * c * v for a, c, v in zip(wp, wo, var_y))
sd_tu = math.sqrt(vp / pente ** 2 + vo / ordonnee ** 2 - 2 * cpo / (pente * ordonnee))
print("S7", "taille utile : attendue", round(pente / ordonnee, 2), "| écart type relatif par vivier", round(100 * sd_tu, 1), "% ; de la moyenne de", G, ":", round(100 * sd_tu / math.sqrt(G), 2),
      "% ; quatre erreurs types :", round(100 * 4 * sd_tu / math.sqrt(G), 1), "% (bande retenue : de 0,7 m à 1,4 m)")

# Comptes de verdicts sur G viviers : probabilité par vivier, puis queue binomiale.
p_rho1 = P((rho1 - 0.65) / (rho1 * sd_rho1) - 1.96)
p_kappa = chance(k_att0, sd_kappa)
p_rho2 = 1.0 if rho2_att(-1.96) < 0.65 else 0.0
p_conf = p_rho1 * p_kappa * p_rho2
queue = lambda k, p: sum(math.comb(G, j) * p ** j * (1 - p) ** (G - j) for j in range(k))     # P(compte < k)
print("S8", "objet « loi vraie » : par vivier, P(borne basse de rho1 > 0,65) =", f"{p_rho1:.6f}", "; P(borne haute de kappa attesté < 0,75) =", f"{p_kappa:.6f}", "; ensemble", f"{p_conf:.6f}",
      "| P(moins de 97 « confirmée » sur", G, ") =", f"{queue(97, p_conf):.1e}")
print("S8", "jumeau faussé vers le haut : P(garde levée) par vivier =", f"{P(1 / math.sqrt(m / W) - 1.645 - (z - q(.98)) / math.sqrt(m / W)):.6f}",
      "| jumeau décalé vers le bas : P(borne basse de rho2 > 0,65) par vivier =", f"{P((rho2_cible - 0.65) / sd_rho2_bas - 1.96):.6f}")
LECTURES = 20      # moyennes comparées à une tolérance dans la table de l'étape 0
print("S8", "moyennes comparées à une tolérance à l'étape 0 :", LECTURES, "; risque qu'une au moins sorte à quatre erreurs types, code juste :",
      round(100 * (1 - (1 - 2 * (1 - P(4))) ** LECTURES), 2), "% ; à trois erreurs types :", round(100 * (1 - (1 - 2 * (1 - P(3))) ** LECTURES), 1), "%",
      "| couverture d'un intervalle à 95 % sur", G, "viviers : erreur type", round(100 * math.sqrt(.95 * .05 / G), 2), "points ; 95 moins quatre erreurs types :", round(95 - 400 * math.sqrt(.95 * .05 / G), 1))

# ---------------------------------------------------------------------------------------------
# W. Remarque 7 : l'objet « témoins à taux p » à ses propres tailles (p = 1 %).
# ---------------------------------------------------------------------------------------------
p_t = 0.01
for n in (160, 4000, 16000):
    temoins = p_t * n
    rapport = math.sqrt((n + temoins + 1) / (12 * n * temoins)) / math.sqrt(1 / (12 * n))
    print("W", "n =", n, "| témoins :", temoins, "| rapport à la référence exacte :", round(rapport, 3), "| part cachée (delta0) :", round(z * math.sqrt((n + temoins + 1) / (12 * n * temoins)) / delta0, 3))

# ---------------------------------------------------------------------------------------------
# T. Remarque 9 : des mondes aux épisodes.
# ---------------------------------------------------------------------------------------------
for k in (4, 9):
    print("T", "K =", k, "| épisodes pour W = 2 400 mondes, modes vus = 1, 2, 3 : au moins", [2400 * (1 + k + mv) for mv in (1, 2, 3)],
          "; avec l'organisme au repos et le mode tenu à l'écart :", [2400 * (3 + k + mv) for mv in (1, 2, 3)])

# ---------------------------------------------------------------------------------------------
# Z. Le seuil de l'écart dit en points de rappel, lecture attestée (approximation normale, W = 60 m) :
#    à la dose où la statistique étalonnée rappelle 50 % à 4 m, le rang attesté rappelle Phi((1/kappa - 1)(z + 1,645 racine(4m/W))).
# ---------------------------------------------------------------------------------------------
releve = z + 1.645 * math.sqrt(4 / 60)
print("Z", "kappa attesté = 0,75 :", round(100 * P((1 / .75 - 1) * releve), 1), "% ; kappa attesté prédit", round(KAPPA * (1 + 1.645 * math.sqrt(4 / 60) / z), 4), ":",
      round(100 * P((1 / (KAPPA * (1 + 1.645 * math.sqrt(4 / 60) / z)) - 1) * releve), 1), "%")

# ---------------------------------------------------------------------------------------------
# X. Remarque 3 : ce que la lettre du test de mort de la mesure demande au vivier (approximation normale, jumeau exact).
#    h = marge d'attestation / écart lu par unité sabotée = 1,645 sigma / (b racine(W)) : c'est la part cachée du rang,
#    par construction, à l'horizon (z / 1,645)² W. Clause de l'organisme au repos : erreur type de g = sigma / (b racine(W)).
# ---------------------------------------------------------------------------------------------
for mu in (0.5, mu0):
    b_m = K * (P(mu / math.sqrt(2)) - .5)
    print("X", "écart par unité sabotée :", round(mu, 3), "écart type | h au réglage A :", round(100 * 1.645 * SIG / (b_m * math.sqrt(W)), 2), "% | mondes pour que h passe sous 10 %, 5 %, 2 % :",
          [round((1.645 * SIG / (b_m * dv)) ** 2) for dv in (.10, .05, .02)], "| organisme au repos, réglage A : erreur type de g", round(100 * SIG / (b_m * math.sqrt(W)), 2),
          "point de dose ; 1,96 erreur type :", round(100 * 1.96 * SIG / (b_m * math.sqrt(W)), 1), "; cinq erreurs types :", round(100 * 5 * SIG / (b_m * math.sqrt(W)), 1))
print("X", "h égale la part cachée du rang par construction à l'horizon", round((z / 1.645) ** 2, 2), "W | vérification sur l'effet planté : h =", round(100 * u0 / moyenne_centree(pb0), 2),
      "% ; formule z sigma / (b racine(2 W)) :", round(100 * z * SIG / (moyenne_centree(pb0) * math.sqrt((z / 1.645) ** 2 * W)), 2), "%")
