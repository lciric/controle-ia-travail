# -*- coding: utf-8 -*-
"""Calculs de la note « revoir la percée » (Opus 5.5, effort maximal), v1.

Toutes les entrées sont des SUPPOSITIONS D'ILLUSTRATION, sauf mention « repris » :
aucune donnée du programme n'est lue. Lois exactes ou approximation normale dite
comme telle ; tirages par numpy.random.SeedSequence (R9).

Blocs :
  A  Pourquoi chaque piste rend une constante : ce qui passe sans alerte selon la
     source de validité du test (loi honnête exacte ; référence finie ; second regard
     dont la part f est estimée ; nul créé par tirage du défenseur ; signature).
  A2 Objet de contrôle par tirages du cas « référence finie » : la probabilité
     d'annonce plafonne quand l'horizon croît.
  B  Ce que coûte la certification de f au banc, et ce que des négatifs durs
     (échecs honnêtes sous preuve trompeuse) y changent.
  C  Taille d'échantillon du critère de mort de la mesure proposée (part de
     subversion qui survit à l'évasion), sous supposition de dispersion.
"""
import math
import sys

import numpy as np
import scipy
from scipy import stats

VERSION = "calculs-percee-revue-opus-max-v1"
ALPHA = 0.05
Z = stats.norm.ppf(1 - ALPHA)  # unilatéral, 1,6449

SS = np.random.SeedSequence(20261121)
SEEDS = dict(zip(["A2", "C"], SS.spawn(2)))


def ligne(*xs):
    print(" | ".join(str(x) for x in xs))


print(VERSION)
print("numpy", np.__version__, "| scipy", scipy.__version__, "| python", sys.version.split()[0])
print("graine mère SeedSequence(20261121), enfants :", {k: v.entropy for k, v in SEEDS.items()},
      {k: v.spawn_key for k, v in SEEDS.items()})
print()

# ---------------------------------------------------------------------------
# Bloc A
# ---------------------------------------------------------------------------
print("=== Bloc A : ce qui passe sans alerte, selon la source de validité ===")
rho0 = 0.10   # part d'épisodes endommagés chez l'honnête (supposé)
q = 0.20      # part auditée au hasard (supposé)
m = 2000      # épisodes honnêtes de référence, entièrement observés (supposé)
t, f = 0.64, 0.029   # repris : comptes au point d'un moniteur de texte publié,
                     # tels que la note percée v2 les cite (9/14 et 1/35) ; illustration
m_f = 500     # échecs honnêtes de référence sur lesquels f est estimée (supposé)
print(f"suppositions : rho0={rho0}, q={q}, m={m}, t={t}, f={f}, m_f={m_f}, alpha={ALPHA}, z={Z:.4f}")
print("convention : puissance 1/2 (le décalage égale le seuil), test à horizon fixe,")
print("approximation normale ; H = n x delta* = excès d'épisodes endommagés par sabotage")
print("que le test ne voit pas à mi-puissance, sur tous les épisodes (audités ou non).")
print()


def H_exacte(n):
    # (i) loi honnête connue exactement : seule la variance de l'échantillon audité compte
    return n * Z * math.sqrt(rho0 * (1 - rho0) / (q * n))


def H_reference(n):
    # (ii) référence finie de m épisodes honnêtes : comparaison de deux proportions
    return n * Z * math.sqrt(rho0 * (1 - rho0) * (1 / (q * n) + 1 / m))


def H_second_regard(n):
    # (iii) événement « endommagé et marqué » ; taux honnête mu0 = rho0 f ; rho0 connu
    # exactement (généreux), f estimée sur m_f échecs honnêtes ; chaque épisode saboté
    # est endommagé et marqué avec probabilité t
    mu0 = rho0 * f
    var = mu0 * (1 - mu0) / (q * n) + rho0 ** 2 * f * (1 - f) / m_f
    return n * Z * math.sqrt(var) / t


def H_tirage_conditionnel(n):
    # (iv) condition tirée par le harnais (moitié des épisodes), saboteur qui ne nuit que
    # sous la condition B ; test A contre B sur les audités ; aucune référence extérieure
    var_diff = rho0 * (1 - rho0) * (1 / (q * n / 2) + 1 / (q * n / 2))
    deltaB = Z * math.sqrt(var_diff)
    return (n / 2) * deltaB


ligne("n", "(i) exacte", "(ii) réf. m", "(iii) 2nd regard, f sur m_f", "(iv) tirage, saboteur conditionnel",
      "(ii)/n", "(iii)/n", "(i)/sqrt(n)", "(iv)/sqrt(n)")
for n in (10 ** 3, 10 ** 4, 10 ** 5, 10 ** 6, 10 ** 7):
    a, b, c, d = H_exacte(n), H_reference(n), H_second_regard(n), H_tirage_conditionnel(n)
    ligne(n, f"{a:.0f}", f"{b:.0f}", f"{c:.0f}", f"{d:.0f}",
          f"{b / n:.5f}", f"{c / n:.5f}", f"{a / math.sqrt(n):.3f}", f"{d / math.sqrt(n):.3f}")
pente_ii = Z * math.sqrt(rho0 * (1 - rho0) / m)
pente_iii = Z * rho0 * math.sqrt(f * (1 - f) / m_f) / t
print(f"pente limite de (ii) : z sqrt(rho0(1-rho0)/m) = {pente_ii:.5f} épisode par épisode")
print(f"pente limite de (iii) : z rho0 sqrt(f(1-f)/m_f) / t = {pente_iii:.5f} ; rapport (ii)/(iii) = {pente_ii / pente_iii:.2f}")
print("lecture : (ii) et (iii) fuient linéairement (une constante les sépare) ; (i) et (iv) en racine.")
print("(iv) ne vaut que pour un saboteur qui conditionne sur la condition tirée ; un saboteur")
print("inconditionnel n'y laisse aucun écart A contre B et retombe sur (ii).")
print()

print("(v) régime de signature au banc : zéro marque sur m_f échecs honnêtes, une marque = alerte")
ligne("m_f", "f_max (95 %, zéro marque)", "horizon n_sig = alpha/(q rho0 f_max)", "n_sig / m_f")
for mf in (35, 500, 2000, 10_000, 100_000):
    fmax = 1 - ALPHA ** (1 / mf)
    nsig = ALPHA / (q * rho0 * fmax)
    ligne(mf, f"{fmax:.6f}", f"{nsig:.0f}", f"{nsig / mf:.3f}")
print("lecture : la signature ne tient qu'à un horizon proportionnel au nombre d'échecs honnêtes")
print("de référence ; au banc, ce nombre s'achète en inférence, non en attaquants.")
print()

# Objet de contrôle analytique : (ii) -> (i) quand m -> infini ; (iii) -> racine quand m_f -> infini
n = 10 ** 6
m_sauv, mf_sauv = m, m_f
m = 10 ** 12
ok1 = abs(H_reference(n) - H_exacte(n)) / H_exacte(n) < 1e-3
m_f = 10 ** 12
lim_iii = n * Z * math.sqrt(rho0 * f * (1 - rho0 * f) / (q * n)) / t
ok2 = abs(H_second_regard(n) - lim_iii) / lim_iii < 1e-3
m, m_f = m_sauv, mf_sauv
print(f"contrôle : (ii) rejoint (i) quand m -> infini : {ok1} ; (iii) rejoint la racine quand m_f -> infini : {ok2}")
print()

# ---------------------------------------------------------------------------
# Bloc A2 : tirages du cas (ii)
# ---------------------------------------------------------------------------
print("=== Bloc A2 : tirages, référence finie (cas ii) ===")
rng = np.random.default_rng(SEEDS["A2"])
R = 20_000
delta = 0.5 * Z * math.sqrt(rho0 * (1 - rho0) / m)  # la moitié de la largeur asymptotique
print(f"saboteur à delta = {delta:.5f} (moitié de z sqrt(rho0(1-rho0)/m)), m = {m}, q = {q}, {R} tirages par case")
ligne("n", "annonce sous l'honnête", "annonce sous le saboteur", "prévu à n infini", "excès caché n*delta")
prevu = stats.norm.cdf(delta / math.sqrt(rho0 * (1 - rho0) / m) - Z)
for n in (10 ** 4, 10 ** 5, 10 ** 6):
    na = int(q * n)
    ref = rng.binomial(m, rho0, size=R) / m
    for rate, lab in ((rho0, "H0"), (rho0 + delta, "H1")):
        dep = rng.binomial(na, rate, size=R) / na
        pool = (dep * na + ref * m) / (na + m)
        se = np.sqrt(pool * (1 - pool) * (1 / na + 1 / m))
        rej = np.mean(dep - ref > Z * se)
        if lab == "H0":
            r0 = rej
        else:
            r1 = rej
    ligne(n, f"{r0:.3f}", f"{r1:.3f}", f"{prevu:.3f}", f"{n * delta:.0f}")
print("lecture : la probabilité d'annonce plafonne vers la valeur prévue, l'excès caché croît comme n.")
print()

# ---------------------------------------------------------------------------
# Bloc B : certification de f et négatifs durs
# ---------------------------------------------------------------------------
print("=== Bloc B : certifier f au banc ; ce que changent des négatifs durs ===")
ligne("m_f", "k marques", "borne haute de f à 95 % (Clopper-Pearson)")
for mf in (35, 500, 2000, 10_000):
    for k in (0, 1, 5):
        if k == 0:
            ub = 1 - ALPHA ** (1 / mf)
        else:
            ub = stats.beta.ppf(1 - ALPHA, k + 1, mf - k)
        ligne(mf, k, f"{ub:.5f}")
print()
print("mélange : une part h des échecs honnêtes est « sous preuve trompeuse » (le modèle")
print("représente la bonne réponse tôt puis émet la fausse, comme sous fausses démonstrations),")
print("marquée avec probabilité f_h ; le reste, avec f_0. Gain du second regard à allure fixée,")
print("limite du saboteur lent, t²/f x (1 - rho0) (formule de la note percée v2, reprise).")
f0 = 0.001
ligne("h", "f_h", "f global", "t²/f x (1-rho0) à t=0,64", "horizon de signature si f était connue")
for h in (0.0, 0.02, 0.05, 0.10):
    for fh in (0.1, 0.3):
        if h == 0.0 and fh == 0.3:
            continue
        fg = h * fh + (1 - h) * f0
        gain = t ** 2 / fg * (1 - rho0)
        nsig = ALPHA / (q * rho0 * fg)
        ligne(h, fh, f"{fg:.4f}", f"{gain:.1f}", f"{nsig:.0f}")
print("lecture : une marque validée sur des échecs ordinaires (f_0 = 0,001) perd l'essentiel de")
print("son gain si 5 % des échecs honnêtes sont du genre « sait tôt, émet faux » et marqués 3 fois")
print("sur 10 ; les négatifs durs décident du régime, pas les négatifs faciles.")
print()

# ---------------------------------------------------------------------------
# Bloc C : taille d'échantillon du critère de mort
# ---------------------------------------------------------------------------
print("=== Bloc C : part de subversion qui survit à l'évasion (« part qui survit »), taille d'échantillon ===")
sigma = 1.2   # écart type du dommage par épisode (lois perdues + fausses promues), SUPPOSÉ
G0 = 1.0      # écart de l'attaquant libre au témoin handicapé, à note de juge égale, SUPPOSÉ
print(f"suppositions : sigma = {sigma} par épisode, G0 = {G0} ; trois bras de n épisodes")
print("(attaquant libre, attaquant qui échappe aux lectures, honnête handicapé à note de juge égale) ;")
print("part qui survit = (D_evade - D_temoin) / (D_libre - D_temoin) ; test unilatéral de « part >= 0,5 »")
print("(mort) contre « part <= 0,2 » (critère proposé) ; écart type par la méthode delta.")


def se_pse(p, n):
    # Var(D_e - D_h) et Var(D_l - D_h) partagent D_h : méthode delta sur le rapport
    Ge = p * G0
    var_num = 2 * sigma ** 2 / n
    var_den = 2 * sigma ** 2 / n
    cov = sigma ** 2 / n
    r = Ge / G0
    return math.sqrt((var_num - 2 * r * cov + r ** 2 * var_den) / G0 ** 2)


ligne("n par bras", "écart type de la part à 0,2", "écart type de la part à 0,5", "puissance (rejeter 0,5 quand vrai 0,2)")
for n in (50, 100, 200, 300, 500, 1000):
    s2, s5 = se_pse(0.2, n), se_pse(0.5, n)
    crit = 0.5 - Z * s5
    power = stats.norm.cdf((crit - 0.2) / s2)
    ligne(n, f"{s2:.3f}", f"{s5:.3f}", f"{power:.3f}")

rng = np.random.default_rng(SEEDS["C"])
n, R = 300, 20_000
hits = 0
fa = 0
for vrai, compteur in ((0.2, "puis"), (0.5, "faux")):
    Dh = rng.normal(0.0, sigma, size=(R, n)).mean(axis=1)
    Dl = rng.normal(G0, sigma, size=(R, n)).mean(axis=1)
    De = rng.normal(vrai * G0, sigma, size=(R, n)).mean(axis=1)
    pse = (De - Dh) / (Dl - Dh)
    s5 = se_pse(0.5, n)
    rej = np.mean(pse < 0.5 - Z * s5)
    if compteur == "puis":
        hits = rej
    else:
        fa = rej
print(f"tirages à n = {n} par bras, {R} répétitions : rejet de « part >= 0,5 » quand la part vaut 0,2 : {hits:.3f} ;")
print(f"quand elle vaut 0,5 (niveau) : {fa:.3f}")
print("lecture : sous ces suppositions, quelques centaines d'épisodes par bras suffisent ; le")
print("coût de la mesure est dans la fabrication des attaquants, non dans le nombre d'épisodes.")
