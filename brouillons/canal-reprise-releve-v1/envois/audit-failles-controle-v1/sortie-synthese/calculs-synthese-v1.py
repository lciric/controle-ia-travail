# Calculs de la synthese de l'audit des failles - v1
# Illustrations analytiques ou synthetiques ; aucune donnee du programme ni des pilotes.
# Lance par : python3 -I calculs-synthese-v1.py > calculs-synthese-v1.sortie.txt
# Graines : numpy.random.SeedSequence, entropie 20261026 fixee avant toute execution (R9).

import numpy as np

print("numpy", np.__version__)
ss = np.random.SeedSequence(20261026)
rng = np.random.default_rng(ss.spawn(1)[0])

# Bloc 1 - rapport consolide, section 2.1 : invariance du spectre sous rotation orthogonale.
# Valeurs singulieres d'une matrice d'etats H (n x d) et de H Q, Q orthogonale ;
# puis du dictionnaire applique coordonnee par coordonnee [v, sin v, v^2].
n, d = 200, 8
H = rng.standard_normal((n, d))
Q, _ = np.linalg.qr(rng.standard_normal((d, d)))
def releve(V):
    return np.hstack([V, np.sin(V), V ** 2])
sv = lambda X: np.round(np.linalg.svd(X, compute_uv=False)[:4], 4)
print("bloc 1 : etat brut, 4 premieres valeurs singulieres :", sv(H))
print("bloc 1 : etat brut tourne                        :", sv(H @ Q))
print("bloc 1 : dictionnaire [v, sin v, v^2]            :", sv(releve(H)))
print("bloc 1 : meme dictionnaire, etat tourne          :", sv(releve(H @ Q)))
print("bloc 1 : ecart relatif max (dictionnaire)        :",
      round(float(np.max(np.abs(sv(releve(H)) - sv(releve(H @ Q))) / sv(releve(H)))), 4))

# Bloc 2 - section 2.4 : regle 1 - Brier + 0,02 (q - 1/2)^2, optimum et condition de Savage.
p = 0.97
q = np.linspace(0.0, 1.0, 2000001)
g = p * (1 - (1 - q) ** 2 + 0.02 * (q - 0.5) ** 2) + (1 - p) * (1 - q ** 2 + 0.02 * (q - 0.5) ** 2)
print("bloc 2 : optimum numerique q* pour p = 0,97 :", round(float(q[np.argmax(g)]), 5),
      "; forme close (2p - 0,02) / 1,96 :", round((2 * p - 0.02) / 1.96, 5))
print("bloc 2 : derivee de l'esperance en q = p : 0,04 p - 0,02 =", round(0.04 * p - 0.02, 5),
      "(seuil du rapport : 1,5e-4) ; elle s'annule seulement en p = 0,5")
print("bloc 2 : transformation affine 0,82 x 0,745 + 0,18 =", round(0.82 * 0.745 + 0.18, 4))
# Score de competence relatif a une reference gelee : invariant par aR + b, a > 0.
S, S_ref, S_opt = 0.745, 0.70, 1.0
ss_avant = (S - S_ref) / (S_opt - S_ref)
a, b = 0.82, 0.18
ss_apres = ((a * S + b) - (a * S_ref + b)) / ((a * S_opt + b) - (a * S_ref + b))
print("bloc 2 : score de competence avant / apres transformation affine :", round(ss_avant, 6), round(ss_apres, 6))

# Bloc 3 - section 2.2 : divergence de Bregman engendree par Phi_alpha, alpha = 4/3.
al = 4.0 / 3.0
Phi = lambda x: (x ** al + (1 - x) ** al - 1) / (al - 1)
dPhi = lambda x: al * (x ** (al - 1) - (1 - x) ** (al - 1)) / (al - 1)
dv = lambda y, x: -Phi(x) - dPhi(x) * (y - x)
print("bloc 3 : d(1, 0) =", round(dv(1, 0.0), 4), "; d(0, 1) =", round(dv(0, 1.0), 4),
      "; d(y, 0,5) =", round(dv(1, 0.5), 4))
x = 0.3
brier2 = -((x ** 2 + (1 - x) ** 2 - 1)) - (4 * x - 2) * (1 - x)
print("bloc 3 : alpha = 2 redonne deux fois le score de Brier :", round(brier2, 4), round(2 * (1 - x) ** 2, 4))
# Proprete : l'esperance p d(1, x) + (1 - p) d(0, x) est minimale en x = p.
xs = np.linspace(0.001, 0.999, 99901)
for pp in (0.1, 0.5, 0.97):
    e = pp * dv(1, xs) + (1 - pp) * dv(0, xs)
    print("bloc 3 : p =", pp, "argmin de l'esperance =", round(float(xs[np.argmin(e)]), 4))
# Dilution : une prediction critique fausse parmi m predictions bien calibrees.
for m in (10, 100, 1000):
    moyenne = (dv(1, 0.0) + (m - 1) * (0.75 * dv(1, 0.75) + 0.25 * dv(0, 0.75))) / m
    reference = 0.75 * dv(1, 0.75) + 0.25 * dv(0, 0.75)
    print("bloc 3 : m =", m, "score moyen", round(moyenne, 4), "contre", round(reference, 4), "sans l'action critique")

# Bloc 4 - section 1.1 : couverture marginale conforme au rang ceil((K + 1)(1 - alpha)).
for K, alpha in ((1000, 0.05), (1000, 0.01), (499, 0.01), (99, 0.01)):
    r = int(np.ceil((K + 1) * (1 - alpha)))
    print("bloc 4 : K = %d, alpha = %.2f : rang %d, taux marginal %.4f %%" % (K, alpha, r, 100 * (1 - r / (K + 1))))

# Bloc 5 - section 1.3 : rapport signal sur bruit de la somme terminale B / (sigma racine(n0)).
for B, sigma, n0 in ((20, 10, 100), (20, 10, 400)):
    print("bloc 5 : B = %d, sigma = %d, n0 = %d : decalage standardise %.2f" % (B, sigma, n0, B / (sigma * np.sqrt(n0))))
print("bloc 5 : seuil extreme sigma racine(2 ln n0), sigma = 1 : n0 = 100 ->", round(float(np.sqrt(2 * np.log(100))), 3),
      "; n0 = 400 ->", round(float(np.sqrt(2 * np.log(400))), 3))

# Bloc 6 - section 1.2 : une variance plus grande de la somme ne suffit pas en general.
# Exemple : meme moyenne, variance plus grande, et probabilite de depasser un seuil fixe plus petite.
# Loi A : normale centree d'ecart type 1. Loi B : melange 0,999 en 0 (ecart type 0,5) et 0,001 en +/- 40 (ecart type 0,5).
t = 2.3263  # quantile 0,99 de la loi A
rngB = np.random.default_rng(ss.spawn(2)[1])
nB = 4_000_000
comp = rngB.random(nB) < 0.001
signe = np.where(rngB.random(nB) < 0.5, -1.0, 1.0)
xB = np.where(comp, 40.0 * signe, 0.0) + 0.5 * rngB.standard_normal(nB)
print("bloc 6 : variance A = 1 ; variance B =", round(float(xB.var()), 3),
      "; P(A > t) = 0,0100 ; P(B > t) =", round(float((xB > t).mean()), 4))
