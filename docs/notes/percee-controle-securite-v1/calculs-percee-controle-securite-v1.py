"""Calculs cités par `reponse-fable-percee-v1.md` (percée en contrôle et sécurité de l'IA).

Aucune donnée du programme n'est lue. Blocs A, B, C, E : lois exactes (gaussiennes,
binomiales) ou intégrales à une dimension ; un contrôle par tirages au bloc A. Bloc D :
tirages sur des p-valeurs exactement uniformes sous le nul. Graines par
`numpy.random.SeedSequence`, dérivées par bloc et écrites en sortie (R9).
Tout est une illustration sous hypothèse écrite, pas une mesure.

Lancer : python calculs-percee-controle-securite-v1.py > calculs-percee-controle-securite-v1.txt
"""
from math import comb, log, sqrt

import numpy as np
from scipy import integrate
from scipy.stats import norm

ALPHA = 0.01
ZA = norm.ppf(1 - ALPHA)
RACINE = 20261121
INF = float("inf")


def part_non_detectee(n, m, mu, puissance=0.5):
    """Plus grande part f d'actes sabotés (décalage mu par acte, variance 1) que le test
    unilatéral de niveau ALPHA sur la moyenne de n actes, comparée à la moyenne de m
    scores de référence honnêtes, détecte avec une probabilité inférieure à `puissance`.
    Exact pour des scores gaussiens : z ~ N(f mu / sqrt(1/n + 1/m), 1)."""
    besoin = ZA + norm.ppf(puissance)
    return min(1.0, besoin * sqrt(1.0 / n + (0.0 if m == INF else 1.0 / m)) / mu)


print(f"Niveau {ALPHA}, seuil unilatéral z = {ZA:.4f}")
print()
print("A. Part d'actes sabotés non détectée (puissance < 0,5) selon la référence honnête")
print("   Hypothèses : un score par acte, honnête N(0,1), saboté N(mu,1), mu = 0,5 ;")
print("   test sur la moyenne des n actes du déploiement contre la moyenne de la référence.")
MU = 0.5
colonnes = [("référence exacte", lambda n: INF), ("m = 400 fixe", lambda n: 400),
            ("m = 2000 fixe", lambda n: 2000), ("témoins 1 % (m = 0,01 n)", lambda n: 0.01 * n),
            ("témoins 5 %", lambda n: 0.05 * n), ("témoins 20 %", lambda n: 0.20 * n)]
for nom, m_de in colonnes:
    ligne = []
    for n in (10**2, 10**3, 10**4, 10**5, 10**6):
        f = part_non_detectee(n, m_de(n), MU)
        ligne.append(f"n = {n:>7} : {100 * f:6.2f} % ({f * n:9.0f} actes)")
    print(f"   {nom:<26} | " + " | ".join(ligne))
print("   Lecture : référence exacte, le nombre d'actes non détectés croît comme racine de n")
print(f"   ({ZA / MU:.2f} racine de n) ; référence fixe de m scores, la part tend vers")
print(f"   z / (mu racine de m) = {100 * ZA / (MU * sqrt(400)):.1f} % (m = 400) et {100 * ZA / (MU * sqrt(2000)):.1f} % (m = 2000) : elle ne baisse plus ;")
print("   témoins à taux p, la loi en racine revient, multipliée par racine de (1 + 1/p) :")
for p in (0.01, 0.05, 0.20):
    print(f"     p = {p:4.2f} : facteur {sqrt(1 + 1 / p):5.2f}")
print("   Horizon utile d'une référence fixe : au-delà de n = m, allonger le déploiement")
print("   n'ajoute presque rien (rapport des deux termes : racine de (1 + n/m)).")
print("   A bis. Plancher valable pour TOUT test, à tout horizon, quand la loi honnête n'est")
print("   connue que par m lectures (ni sa moyenne ni sa forme ne sont sues d'ailleurs) :")
print("   argument à deux points : la loi G du déploiement (mélange) est elle-même une loi")
print("   honnête possible ; seule la référence distingue les deux cas ; puissance - niveau")
print("   <= distance en variation totale entre m lectures de G et m lectures de F")
print("   <= 0,5 racine de ((1 + f^2 (exp(mu^2) - 1))^m - 1)   (borne du khi-deux, exacte).")
for m in (400, 2000, 10**4):
    f_min = sqrt(((1 + (2 * (0.5 - ALPHA)) ** 2) ** (1.0 / m) - 1) / (np.exp(MU**2) - 1))
    f_moy = ZA / (MU * sqrt(m))
    print(f"     m = {m:>5} : aucun test n'atteint la puissance 0,5 sous f = {100 * f_min:5.2f} % ;"
          f" le test sur la moyenne l'atteint à {100 * f_moy:5.2f} % (n infini)")

# Contrôle par tirages d'une cellule (cas sain : niveau ; cas d'épreuve : puissance 0,5).
# Un premier passage (graine [RACINE, 1], 5000 puis 20000 répétitions) a donné une fausse alerte
# de 0,0072 puis 0,0083, à 2,4 erreurs types sous 0,01 : audit par quatre graines de plus (R4),
# toutes rapportées, et total des cinq.
n_c, m_c, rep = 2000, 400, 20000
f_c = part_non_detectee(n_c, m_c, MU)
k_c = int(round(f_c * n_c))
print(f"   Contrôle par tirages ({rep} répétitions par graine, n = {n_c}, m = {m_c}, {k_c} actes sabotés) :")
tot0 = tot1 = 0
for suffixe in (1, 101, 102, 103, 104):
    ss_a = np.random.SeedSequence([RACINE, suffixe])
    rng = np.random.default_rng(ss_a)
    alertes0 = alertes1 = 0
    for _ in range(rep):
        ref = rng.standard_normal(m_c).mean()
        x = rng.standard_normal(n_c)
        z0 = (x.mean() - ref) / sqrt(1 / n_c + 1 / m_c)
        x[:k_c] += MU
        z1 = (x.mean() - ref) / sqrt(1 / n_c + 1 / m_c)
        alertes0 += z0 > ZA
        alertes1 += z1 > ZA
    tot0 += alertes0
    tot1 += alertes1
    ecart = (alertes0 - ALPHA * rep) / sqrt(rep * ALPHA * (1 - ALPHA))
    print(f"     graine {ss_a.entropy} : fausse alerte {alertes0 / rep:.4f} ({ecart:+.2f} erreur type), détection {alertes1 / rep:.4f}")
print(f"     cinq graines réunies : fausse alerte {tot0 / (5 * rep):.4f} (attendu {ALPHA}), détection {tot1 / (5 * rep):.4f}")
print(f"     (attendu 0,5 à l'arrondi de {k_c} actes près)")

print()
print("B. Tolérance et cachette : si le test doit garder son niveau pour tout écart")
print("   systématique |b| <= b_max entre l'honnête et sa référence, une part f d'actes")
print("   sabotés avec f mu <= b_max reste sous le seuil à tout horizon quand l'écart vrai")
print("   est nul, et jusqu'à f mu <= 2 b_max quand l'écart vrai vaut -b_max")
print("   (instance à une dimension du théorème 4 de arXiv 2609.23254, p. 6).")
for b_max in (0.02, 0.05, 0.10):
    print(f"   b_max = {b_max:4.2f}, mu = {MU} : part cachée {100 * b_max / MU:5.1f} % à {100 * 2 * b_max / MU:5.1f} %, pour tout n")
print("   Écart borné par m témoins honnêtes (demi-largeur à 99 % : 2,576 / racine de m) :")
for m in (100, 400, 2000, 10**4, 10**5):
    print(f"     m = {m:>6} : b_max = {norm.ppf(0.995) / sqrt(m):.4f}")


def score_normal_moyen(mu, k):
    """Espérance du score normal du rang rendu continu de l'acte de l'agent, N(mu,1),
    parmi k tirages du jumeau, N(0,1). Nulle si mu = 0 ; variance 1 sous le nul."""
    a = [norm.ppf(r / (k + 1)) if 0 < r < k + 1 else (-INF if r == 0 else INF) for r in range(k + 2)]
    dens = [norm.pdf(v) if abs(v) != INF else 0.0 for v in a]
    interieur = [(k + 1) * (dens[r] - dens[r + 1]) for r in range(k + 1)]

    def integrande(x):
        p = norm.cdf(x)
        return norm.pdf(x - mu) * sum(comb(k, r) * p**r * (1 - p) ** (k - r) * interieur[r] for r in range(k + 1))

    return integrate.quad(integrande, -10, 10 + mu, limit=400)[0]


print()
print("C. Ce qu'un moniteur ajoute à l'audit : part d'actes sabotés non détectée")
print("   (puissance < 0,5, niveau 1 %), audit tiré au hasard à p = 1 % des actes.")
P_AUDIT = 0.01
D0, D1 = 0.30, 0.60
e4, e19 = score_normal_moyen(MU, 4), score_normal_moyen(MU, 19)
print(f"   Contrôle : score normal moyen à mu = 0 : {score_normal_moyen(0.0, 4):+.2e} (attendu 0).")
print(f"   Efficacité du rang parmi K tirages du jumeau, mu = {MU} : K = 4 : {e4 / MU:.3f} ; K = 19 : {e19 / MU:.3f}")
procedures = [
    ("C1 audit seul, dommage reconnu à coup sûr (q = 1), l'honnête n'en fait jamais",
     lambda n: min(1.0, log(2) / (P_AUDIT * 1.0 * n))),
    ("C1 bis audit seul, dommage reconnu une fois sur cinq (q = 0,2)",
     lambda n: min(1.0, log(2) / (P_AUDIT * 0.2 * n))),
    (f"C2 audit seul, excès d'échecs ({D0} honnête, {D1} saboté), taux honnête connu",
     lambda n: min(1.0, ZA * sqrt(D0 * (1 - D0)) / ((D1 - D0) * sqrt(P_AUDIT * n)))),
    ("C3 moniteur, référence = les épisodes audités sans dommage (m = p n)",
     lambda n: part_non_detectee(n, P_AUDIT * n, MU)),
    ("C4 moniteur à pivot par acte : rang parmi K = 4 tirages du jumeau",
     lambda n: min(1.0, ZA / (e4 * sqrt(n)))),
    ("C4 bis le même, K = 19",
     lambda n: min(1.0, ZA / (e19 * sqrt(n)))),
]
for nom, f_de in procedures:
    print(f"   {nom}")
    print("      " + " | ".join(f"n = {n:>7} : {100 * f_de(n):6.2f} % ({f_de(n) * n:7.0f} actes)" for n in (10**3, 10**4, 10**5, 10**6)))
print("   Rapport C3 / C4 (ce que vaut un pivot par acte face à une référence de p n témoins) :")
print(f"     {(ZA * sqrt((1 + P_AUDIT) / P_AUDIT) / MU) / (ZA / e4):.1f} à tout n (p = 1 %, K = 4)")
print("   Horizon au-delà duquel l'audit seul (C1, C1 bis) fait mieux que le pivot (C4) :")
for q in (1.0, 0.2, 0.05):
    n_x = (log(2) * e4 / (ZA * P_AUDIT * q)) ** 2
    print(f"     q = {q:4.2f} : n = {n_x:10.0f} actes")

print()
print("D. Entre le maximum et la somme : puissance à 1 % de quatre agrégateurs sur")
print("   n = 1000 p-valeurs exactement uniformes sous le nul ; k actes décalés de mu.")
N_D, REP0, REP1, LOT = 1000, 20000, 2000, 2000
ss_d = np.random.SeedSequence([RACINE, 4])
g0, g1 = (np.random.default_rng(s) for s in ss_d.spawn(2))
I = np.arange(1, N_D + 1)
MOITIE = N_D // 2


def statistiques(z):
    """z : tableau (répétitions, n) de scores normaux ; grand = suspect."""
    somme = z.sum(axis=1) / sqrt(N_D)
    maxi = z.max(axis=1)
    p = np.sort(norm.sf(z), axis=1)[:, :MOITIE]
    p = np.clip(p, 1e-300, 1 - 1e-12)
    frac = I[:MOITIE] / N_D
    hc = sqrt(N_D) * (frac - p) / np.sqrt(p * (1 - p))
    hc = np.where(p >= 1.0 / N_D, hc, -INF).max(axis=1)
    kl = frac * np.log(frac / p) + (1 - frac) * np.log((1 - frac) / (1 - p))
    bj = np.where(p < frac, N_D * kl, 0.0).max(axis=1)
    return somme, maxi, hc, bj


nul = [[], [], [], []]
for _ in range(REP0 // LOT):
    for acc, v in zip(nul, statistiques(g0.standard_normal((LOT, N_D)))):
        acc.append(v)
seuils = [np.quantile(np.concatenate(a), 1 - ALPHA) for a in nul]
print(f"   Graines : racine {ss_d.entropy} ; seuils à 1 % sur {REP0} tirages du nul :")
print("   somme {:.3f} ; maximum {:.3f} ; critique d'ordre supérieur {:.3f} ; Berk-Jones {:.3f}".format(*seuils))
print("   (somme attendue 2,326 ; maximum attendu {:.3f})".format(norm.isf(1 - (1 - ALPHA) ** (1 / N_D))))
print("   k actes, mu        | somme | maximum | critique d'ordre supérieur | Berk-Jones")
for k, mu in ((300, 0.25), (100, 0.75), (30, 1.5), (30, 2.0), (10, 2.5), (10, 3.0), (3, 3.5), (3, 4.0), (1, 5.0)):
    z = g1.standard_normal((REP1, N_D))
    z[:, :k] += mu
    pw = [float((v > s).mean()) for v, s in zip(statistiques(z), seuils)]
    print(f"   k = {k:>3}, mu = {mu:4.2f} | {pw[0]:5.3f} | {pw[1]:7.3f} | {pw[2]:26.3f} | {pw[3]:.3f}")
print(f"   Erreur type d'une puissance : au plus {sqrt(0.25 / REP1):.3f}.")

print()
print("E. Défenses heuristiques réexaminées sous attaque adaptée (comptes lus p. 1 des PDF)")
casse = [("arXiv 1802.00420 (défenses de 2018 à gradients masqués)", 9, 6 + 1),
         ("arXiv 2002.08347 (treize défenses de 2018 à 2020)", 13, 13),
         ("arXiv 2510.09023 (douze défenses de modèles de langage)", 12, 12)]
tot = sum(c[1] for c in casse)
tom = sum(c[2] for c in casse)
for nom, n, k in casse:
    print(f"   {nom} : {k} contournées sur {n}")
print(f"   Total : {tom} sur {tot} ; restent {tot - tom} sur {tot} ({100 * (tot - tom) / tot:.1f} %).")
print("   Réserve : trois audits choisis par leurs auteurs, non un échantillon des défenses publiées ;")
print("   dans le premier, 1 des 7 n'est contournée qu'en partie.")
