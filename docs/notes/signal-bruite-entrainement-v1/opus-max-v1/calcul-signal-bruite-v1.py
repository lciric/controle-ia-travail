# Calculs de la note « le signal bruite suffit-il pour entrainer ? » (v1)
# Auteur : Claude Opus 5.5, 21 novembre 2026. Piece de classe C.
# Aucune donnee du programme : mondes plantes a trois ou quatre conduites, suppositions d'illustration.
# Graines : numpy.random.SeedSequence, une sous-suite par bloc (R9).
#
# Modele. Une conduite x (une facon de faire l'episode, dans un meme contexte) a un dommage D(x)
# et un score moyen de moniteur m(x) = E[S | x]. Le score lu vaut S = m(x) + bruit independant.
# L'entrainement regularise (recompense -lambda*S, penalite beta sur l'ecart de Kullback-Leibler
# a la politique de depart pi0) a pour optimum la bascule exponentielle
#     pi_theta(x) proportionnel a pi0(x) * exp(-theta * m(x)),   theta = lambda / beta.
# Le bruit independant ne change pas cet optimum (seule la moyenne m(x) y entre) : il ralentit.
# Le choix du meilleur de N (le moins suspect de N tirages) en est l'approximation sans entrainement.

import math
from statistics import NormalDist

import numpy as np

ENTROPIE = 20261121174500  # fixee a l'ecriture, consignee ici
SS = np.random.SeedSequence(ENTROPIE)
GRAINES = SS.spawn(5)


def bascule(pi0, m, theta):
    w = pi0 * np.exp(-theta * (m - m.min()))
    return w / w.sum()


def kl(p, q):
    masque = p > 0
    return float(np.sum(p[masque] * np.log(p[masque] / q[masque])))


def theta_pour_kl(pi0, m, budget, hi=200.0):
    """Plus petit theta tel que KL(pi_theta || pi0) atteigne le budget ; inf si inatteignable."""
    if kl(bascule(pi0, m, hi), pi0) < budget:
        return math.inf
    lo = 0.0
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if kl(bascule(pi0, m, mid), pi0) < budget:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def lignes(titre):
    print()
    print("=" * 78)
    print(titre)
    print("=" * 78)


def trois_conduites(e, h, k, delta=1.0):
    # H honnete (D=0, m=0) ; B sabotage franc (D=1, m=delta) ; C sabotage cache (D=1, m=(1-k)*delta)
    pi0 = np.array([e, (1 - e) * (1 - h), (1 - e) * h])
    m = np.array([0.0, delta, (1 - k) * delta])
    D = np.array([0.0, 1.0, 1.0])
    return pi0, m, D


# ---------------------------------------------------------------------------------------------
lignes("Bloc A - loi exacte de la bascule : dommage et score selon la force d'optimisation")
print("Conduites : H honnete (D=0, m=0) ; B franc (D=1, m=1) ; C cache (D=1, m=1-k).")
print("Masses de depart : H = e ; C = (1-e)h ; B = (1-e)(1-h). theta = force d'optimisation.")
for (nom, e, h, k) in [("A1 saboteur constant", 0.0, 0.2, 0.8),
                       ("A2 exploration 10 % dans le meme contexte", 0.10, 0.2, 0.8),
                       ("A3 exploration 10 %, cache parfait", 0.10, 0.2, 1.0)]:
    pi0, m, D = trois_conduites(e, h, k)
    print(f"\n{nom} : e={e}, h={h}, k={k}")
    print(f"{'theta':>6} {'KL (nats)':>10} {'E[score]':>9} {'E[dommage]':>11} {'P(H)':>7} {'P(C)':>7}")
    for theta in [0, 0.5, 1, 2, 3, 5, 8, 12, 20]:
        p = bascule(pi0, m, theta)
        print(f"{theta:>6} {kl(p, pi0):>10.3f} {float(p @ m):>9.3f} {float(p @ D):>11.3f} "
              f"{p[0]:>7.3f} {p[2]:>7.3f}")

lignes("Bloc A4 - transition de phase : dommage final a budget d'optimisation fixe, selon e et k")
print("Budget : ecart de Kullback-Leibler de 1,204 nat (celui du meilleur de 8 : ln 8 - 7/8).")
budget = math.log(8) - 7 / 8
print(f"budget = {budget:.4f} nat ; h = 0,2")
ks = [0.5, 0.8, 0.95, 1.0]
print(f"{'e':>7} " + " ".join(f"{'k=' + str(k):>9}" for k in ks))
for e in [0.0, 0.001, 0.01, 0.03, 0.1, 0.3]:
    vals = []
    for k in ks:
        pi0, m, D = trois_conduites(e, 0.2, k)
        th = theta_pour_kl(pi0, m, budget)
        if math.isinf(th):
            p = bascule(pi0, m, 200.0)
            vals.append(f"{float(p @ D):>8.3f}*")
        else:
            p = bascule(pi0, m, th)
            vals.append(f"{float(p @ D):>9.3f}")
    print(f"{e:>7} " + " ".join(vals))
print("(* : budget inatteignable ; valeur a theta = 200, la bascule ne peut plus rien deplacer)")

# ---------------------------------------------------------------------------------------------
lignes("Bloc B - meilleur de N par tirage : le bruit ralentit, l'erreur systematique detourne")
rng = np.random.default_rng(GRAINES[0])
nd = NormalDist()


def sigma_pour_aire(aire, delta=1.0):
    # aire sous la courbe entre H et B sous bruit gaussien de meme ecart-type : Phi(delta/(sigma*sqrt2))
    return delta / (math.sqrt(2) * nd.inv_cdf(aire))


ESSAIS = 200_000
for (nom, e, h, k, aire) in [("B1 aucun cache possible, e=0,1", 0.10, 0.0, 0.0, 0.77),
                             ("B2 saboteur constant, cache parfait", 0.0, 0.2, 1.0, 0.77),
                             ("B3 e=0,1, cache partiel k=0,8", 0.10, 0.2, 0.8, 0.77),
                             ("B4 comme B1, moniteur plus bruite (aire 0,60)", 0.10, 0.0, 0.0, 0.60)]:
    pi0, m, D = trois_conduites(e, h, k)
    sig = sigma_pour_aire(aire)
    print(f"\n{nom} : aire entre H et B = {aire} (ecart-type du bruit {sig:.3f})")
    print(f"{'N':>4} {'E[score choisi]':>16} {'E[dommage choisi]':>18} {'P(H choisi)':>12}")
    for N in [1, 2, 4, 8, 16, 32]:
        x = rng.choice(3, size=(ESSAIS, N), p=pi0)
        s = m[x] + sig * rng.standard_normal((ESSAIS, N))
        j = np.argmin(s, axis=1)
        xc = x[np.arange(ESSAIS), j]
        sc = s[np.arange(ESSAIS), j]
        print(f"{N:>4} {sc.mean():>16.3f} {D[xc].mean():>18.3f} {np.mean(xc == 0):>12.3f}")

lignes("Bloc B5 - rapport de selection du meilleur de 5 (sans cache), comme la page web le mesure")
print("Rapport = P(H choisi par le meilleur de 5) / P(H choisi au hasard) = P(H choisi) / e.")
print(f"{'e':>6} " + " ".join(f"{'aire=' + str(a):>11}" for a in [0.6, 0.77, 0.9]))
rng2 = np.random.default_rng(GRAINES[1])
for e in [0.05, 0.1, 0.2, 0.5]:
    vals = []
    for a in [0.6, 0.77, 0.9]:
        pi0, m, D = trois_conduites(e, 0.0, 0.0)
        sig = sigma_pour_aire(a)
        x = rng2.choice(3, size=(ESSAIS, 5), p=pi0)
        s = m[x] + sig * rng2.standard_normal((ESSAIS, 5))
        xc = x[np.arange(ESSAIS), np.argmin(s, axis=1)]
        vals.append(f"{np.mean(xc == 0) / e:>11.2f}")
    print(f"{e:>6} " + " ".join(vals))
print(f"Plafond du rapport (moniteur parfait) : (1 - (1-e)^5)/e ; e=0,1 -> {(1 - 0.9 ** 5) / 0.1:.2f}")

# ---------------------------------------------------------------------------------------------
lignes("Bloc C - identite du premier ordre : dE[D]/dtheta en 0 = -Cov(m, D), et sa decomposition")
for (e, h, k) in [(0.0, 0.2, 0.8), (0.1, 0.2, 0.8), (0.3, 0.5, 0.5)]:
    pi0, m, D = trois_conduites(e, h, k)
    eps = 1e-6
    deriv = (float(bascule(pi0, m, eps) @ D) - float(pi0 @ D)) / eps
    cov = float(pi0 @ (m * D)) - float(pi0 @ m) * float(pi0 @ D)
    # decomposition par mode : honnete (H) contre sabotage (B, C)
    ps = pi0[1] + pi0[2]
    if ps > 0:
        m_s = (pi0[1] * m[1] + pi0[2] * m[2]) / ps
        within = (pi0[1] * (m[1] - m_s) * (D[1] - 1) + pi0[2] * (m[2] - m_s) * (D[2] - 1))
    else:
        m_s, within = 0.0, 0.0
    between = e * (1 - e) * (m_s - 0.0) * (1.0 - 0.0)
    print(f"e={e}, h={h}, k={k} : derivee numerique {deriv:.5f} ; -Cov {-cov:.5f} ; "
          f"part intra-mode {-within:.5f} ; part entre modes {-between:.5f}")

# ---------------------------------------------------------------------------------------------
lignes("Bloc D - sonde additive par action : baisser la dose ou cacher, la moins chere l'emporte")
print("Conduites : H (D=0, m=0) ; dose basse L (D=0,5, m=0,5) ; dose haute F (D=1, m=1) ;")
print("haute dose cachee C (D=1, m=1-k). e = 0 (saboteur constant). Masses : L = l, C = h, F = 1-l-h.")
print(f"Budget fixe : {budget:.4f} nat.")
print(f"{'l':>5} {'h':>6} " + " ".join(f"{'k=' + str(k):>9}" for k in [0.3, 0.5, 0.7, 1.0]))
for (l, h) in [(0.2, 0.0), (0.2, 0.01), (0.2, 0.05), (0.2, 0.2), (0.05, 0.05)]:
    vals = []
    for k in [0.3, 0.5, 0.7, 1.0]:
        pi0 = np.array([0.0, l, 1 - l - h, h])
        m = np.array([0.0, 0.5, 1.0, 1 - k])
        D = np.array([0.0, 0.5, 1.0, 1.0])
        th = theta_pour_kl(pi0, m, budget)
        p = bascule(pi0, m, 200.0 if math.isinf(th) else th)
        vals.append(f"{float(p @ D):>9.3f}")
    print(f"{l:>5} {h:>6} " + " ".join(vals))
pi0 = np.array([0.0, 0.2, 0.8, 0.0])
print(f"Reference sans optimisation (l=0,2, h=0) : E[D] = {float(pi0 @ np.array([0, .5, 1, 1])):.3f}")

lignes("Bloc E - ecart de Kullback-Leibler du meilleur de N : ln N - (N-1)/N (loi exacte)")
for N in [2, 4, 5, 8, 16, 32]:
    print(f"N={N:>3} : {math.log(N) - (N - 1) / N:.4f} nat")
rng3 = np.random.default_rng(GRAINES[2])
u = rng3.random((400_000, 8))
# controle de la loi : densite du max de 8 uniformes = 8 u^7 ; KL = E[ln(8 U^7)], U ~ max
mx = u.max(axis=1)
print(f"Controle par tirage (N=8) : {np.mean(np.log(8 * mx ** 7)):.4f} nat")

# ---------------------------------------------------------------------------------------------
lignes("Bloc F - reperes pour les predictions : minimum attendu de N normales ; part honnete du meilleur de N")
rng4 = np.random.default_rng(GRAINES[3])
z = rng4.standard_normal((400_000, 16))
for N in [4, 8, 16]:
    print(f"E[min de {N:>2} normales centrees reduites] = {z[:, :N].min(axis=1).mean():.3f}")
for e in [0.0, 0.02, 0.05, 0.2]:
    print(f"e={e:<5} : P(au moins un episode honnete parmi 16) = 1-(1-e)^16 = {1 - (1 - e) ** 16:.3f}")
print("Prix de l'honnetete par contexte : ecart de Kullback-Leibler pour porter toute la masse sur H = ln(1/e)")
for e in [0.3, 0.1, 0.01, 0.001]:
    print(f"e={e:<6} : ln(1/e) = {math.log(1 / e):.3f} nat")

# ---------------------------------------------------------------------------------------------
lignes("Bloc G - objets de controle de l'epreuve proposee : pente intra-contexte du dommage sur le score")
print("200 contextes x 16 tirages ; dommage D dans [0,1] ; score = effet du contexte + terme + bruit.")
print("Objet faux : saboteur constant, le score ne depend pas de D dans le contexte (pente vraie 0).")
print("Objet vrai : score = 1,0 x D + bruit (pente vraie > 0). Intervalle a 95 % par reechantillonnage")
print("des contextes (2 000 tirages). Meilleur de 16 : baisse du dommage choisi, en part de l'ecart moyen.")
rng5 = np.random.default_rng(GRAINES[4])


def pente_intra(S, D):
    Sc = S - S.mean(axis=1, keepdims=True)
    Dc = D - D.mean(axis=1, keepdims=True)
    return float((Sc * Dc).sum() / (Sc * Sc).sum())


for nom, vraie in [("objet faux", False), ("objet vrai", True)]:
    C, K = 200, 16
    ctx = rng5.standard_normal((C, 1))
    D = np.clip(0.7 + 0.2 * rng5.standard_normal((C, K)), 0, 1)
    if vraie:
        S = ctx + 1.0 * D + 0.3 * rng5.standard_normal((C, K))
    else:
        S = ctx + 1.0 + 0.3 * rng5.standard_normal((C, K))
    b = pente_intra(S, D)
    boots = []
    for _ in range(2000):
        idx = rng5.integers(0, C, C)
        boots.append(pente_intra(S[idx], D[idx]))
    lo, hi = np.percentile(boots, [2.5, 97.5])
    j = np.argmin(S, axis=1)
    baisse = float(D.mean() - D[np.arange(C), j].mean())
    print(f"{nom} : pente {b:+.3f} [{lo:+.3f} ; {hi:+.3f}] ; baisse du dommage au meilleur de 16 = {baisse:+.3f} "
          f"(dommage moyen {D.mean():.3f})")
print()
print("Fin des calculs.")
