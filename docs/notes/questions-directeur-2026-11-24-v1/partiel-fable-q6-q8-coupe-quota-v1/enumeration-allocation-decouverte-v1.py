"""Énumérations exhaustives et petits calculs sur processeur pour la partie I de la réponse aux
questions 6 et 8 (peut-on démontrer comment maximiser la probabilité d'une découverte), v1.

Pièce de travail (classe C). Aucune dépense, aucun appel à un modèle. Chaque partie éprouve un
énoncé de la réponse sur de petits paramètres, en arithmétique exacte (fractions) quand c'est
possible ; les paramètres sont tirés au hasard, ce ne sont pas des mesures.

A. Corollaire de la distance optimale du modèle de Fable, refait : condition d'existence d'un
   optimum intérieur, dérivées dS*/dZ = beta'·q*/rho et dS*/dW = -(1 - q*).
B. Trois objectifs, trois indices :
   B1. coût espéré jusqu'au premier succès : l'ordre p/c décroissant est optimal (toutes les
       permutations, n <= 7) ;
   B2. budget dur : « au moins une découverte » et « nombre espéré » ne choisissent pas le même
       ensemble (tous les sous-ensembles) ;
   B3. règle de Pandore de Weitzman : la politique d'indice (valeur de réserve) égale l'optimum
       de la programmation dynamique exhaustive ; l'indice q·V/c ne l'égale pas.
C. Allocation de Koopman en version discrète : le glouton marginal égale l'optimum exhaustif ;
   après échec, la masse restante se concentre dans les puits étroits.
D. Viser le maximum : étalement à moyenne constante et espérance du maximum ; seuil de
   croisement d'une famille position-échelle ; contre-exemple à « plus de variance, plus de queue ».
E. Diversité : écart de Jensen sous latent partagé ; la répartition égale entre proposeurs
   indépendants est optimale ; identité quand le latent est commun ; sous-modularité de la
   probabilité d'une union et de l'espérance d'un maximum ; contre-exemple des idées composites.
F. Filtre bon marché avant une épreuve chère : critère exact, plafond du gain, table de Carbon
   recalculée, contre-exemples (idées profondes sous-notées, candidats rares).
G. Criticalité : Galton-Watson, seuil biparti c_A·c_B = 1, opérateur sans retour sur un graphe
   à boucles courtes (réseau triangulaire) contre un graphe en arbre, vivier fini, condition
   de criticalité du cortège.

Graines par numpy.random.SeedSequence (règle R9) : une graine fille par partie.
Usage : python enumeration-allocation-decouverte-v1.py   (numpy >= 1.25, bibliothèque standard)
"""
import itertools
import math
from fractions import Fraction as Fr
from functools import lru_cache

import numpy as np

GRAINE_RACINE = 2026112406
ss = np.random.SeedSequence(GRAINE_RACINE)
ss_a, ss_b, ss_c, ss_d, ss_e, ss_f, ss_g = ss.spawn(7)


def sig(x):
    return 1.0 / (1.0 + math.exp(-x))


# =============================================================================================
print("=== A. Corollaire de la distance optimale : I(S) = q(S)·(S + W), q = sig(q0 + b·Z - rho·S) ===")
rng = np.random.default_rng(ss_a)


def interet(S, q0, b, rho, W, Z):
    return sig(q0 + b * Z - rho * S) * (S + W)


def g_cond(S, q0, b, rho, W, Z):
    return rho * (1.0 - sig(q0 + b * Z - rho * S)) * (S + W) - 1.0


def s_etoile(q0, b, rho, W, Z):
    """Racine de g sur S >= 0 par dichotomie ; None si g(0) >= 0 (optimum au bord S = 0)."""
    if g_cond(0.0, q0, b, rho, W, Z) >= 0.0:
        return None
    bas, haut = 0.0, 1.0
    while g_cond(haut, q0, b, rho, W, Z) < 0.0:
        haut *= 2.0
    for _ in range(200):
        mil = 0.5 * (bas + haut)
        if g_cond(mil, q0, b, rho, W, Z) < 0.0:
            bas = mil
        else:
            haut = mil
    return 0.5 * (bas + haut)


n_tir, n_int, n_bord = 800, 0, 0
err_grille = err_dz = err_dw = 0.0
desaccord_condition = 0
for _ in range(n_tir):
    q0 = rng.uniform(-2, 2)
    b = rng.uniform(0.2, 2.0)
    rho = rng.uniform(0.2, 2.0)
    W = rng.uniform(0.0, 4.0)
    Z = rng.uniform(-2, 3)
    s = s_etoile(q0, b, rho, W, Z)
    grille = np.linspace(0.0, 40.0, 400001)
    vals = 1.0 / (1.0 + np.exp(-(q0 + b * Z - rho * grille))) * (grille + W)
    s_brut = float(grille[int(np.argmax(vals))])
    cond = rho * W * (1.0 - sig(q0 + b * Z)) < 1.0
    if s is None:
        n_bord += 1
        if cond or s_brut > 1e-3:
            desaccord_condition += 1
        continue
    n_int += 1
    if not cond:
        desaccord_condition += 1
    err_grille = max(err_grille, abs(s - s_brut))
    qs = sig(q0 + b * Z - rho * s)
    eps = 1e-5
    sp, sm = s_etoile(q0, b, rho, W, Z + eps), s_etoile(q0, b, rho, W, Z - eps)
    if sp is not None and sm is not None:
        err_dz = max(err_dz, abs((sp - sm) / (2 * eps) - b * qs / rho))
    sp, sm = s_etoile(q0, b, rho, W + eps, Z), s_etoile(q0, b, rho, W - eps, Z)
    if sp is not None and sm is not None:
        err_dw = max(err_dw, abs((sp - sm) / (2 * eps) + (1.0 - qs)))
print(f"tirages de paramètres : {n_tir} ; optimum intérieur : {n_int} ; optimum au bord S = 0 : {n_bord}")
print(f"désaccords avec la condition rho·W·(1 - sig(q0 + b·Z)) < 1 : {desaccord_condition}")
print(f"écart maximal entre la racine de g et l'argmax sur grille (pas 1e-4) : {err_grille:.2e}")
print(f"écart maximal |dS*/dZ (différences finies) - b·q*/rho| : {err_dz:.2e}")
print(f"écart maximal |dS*/dW (différences finies) + (1 - q*)| : {err_dw:.2e}")
ex = dict(q0=0.0, b=1.0, rho=1.0, W=1.0)
for Z in (0.0, 1.0, 2.0, 3.0):
    s = s_etoile(Z=Z, **ex)
    qs = sig(ex["q0"] + ex["b"] * Z - ex["rho"] * s)
    print(f"  exemple q0=0, b=1, rho=1, W=1, Z={Z:.0f} : S* = {s:.4f}, crédibilité à l'optimum q* = {qs:.4f}")
for W in (0.5, 1.0, 2.0, 4.0):
    s = s_etoile(q0=0.0, b=1.0, rho=1.0, W=W, Z=1.0)
    txt = "bord (S* = 0)" if s is None else f"S* = {s:.4f}"
    print(f"  exemple q0=0, b=1, rho=1, Z=1, W={W:.1f} : {txt}")

# =============================================================================================
print()
print("=== B1. Ordre p/c décroissant et coût espéré jusqu'au premier succès (permutations exhaustives) ===")
rng = np.random.default_rng(ss_b)


def cout_espere(ordre, p, c):
    tot, survie = Fr(0), Fr(1)
    for i in ordre:
        tot += survie * c[i]
        survie *= (1 - p[i])
    return tot


n_inst, n_ok = 0, 0
for n in (3, 4, 5, 6, 7):
    for _ in range(60 if n < 7 else 20):
        p = [Fr(int(rng.integers(1, 20)), 20) for _ in range(n)]
        c = [Fr(int(rng.integers(1, 9)), 4) for _ in range(n)]
        meilleur = min(cout_espere(o, p, c) for o in itertools.permutations(range(n)))
        indice = sorted(range(n), key=lambda i: p[i] / c[i], reverse=True)
        n_inst += 1
        n_ok += (cout_espere(indice, p, c) == meilleur)
print(f"instances : {n_inst} (n de 3 à 7, probabilités et coûts rationnels) ; ordre p/c optimal : {n_ok}")

print()
print("=== B2. Budget dur : « au moins une » contre « nombre espéré » (sous-ensembles exhaustifs) ===")


def meilleurs_ensembles(p, c, B):
    n = len(p)
    best1 = best2 = None
    for r in range(n + 1):
        for S in itertools.combinations(range(n), r):
            if sum(c[i] for i in S) > B:
                continue
            echec = Fr(1)
            for i in S:
                echec *= (1 - p[i])
            v1, v2 = 1 - echec, sum((p[i] for i in S), Fr(0))
            if best1 is None or v1 > best1[0]:
                best1 = (v1, S)
            if best2 is None or v2 > best2[0]:
                best2 = (v2, S)
    return best1, best2


p_ex, c_ex = [Fr(9, 10), Fr(1, 2), Fr(1, 2)], [Fr(2), Fr(1), Fr(1)]
b1, b2 = meilleurs_ensembles(p_ex, c_ex, Fr(2))
print(f"exemple (p, c) = (0,9 ; 2), (0,5 ; 1), (0,5 ; 1), budget 2 : au moins une -> {b1[1]} "
      f"(P = {float(b1[0]):.2f}) ; nombre espéré -> {b2[1]} (E = {float(b2[0]):.2f})")
n_inst = n_diff = 0
perte_max = Fr(0)
for _ in range(400):
    n = 6
    p = [Fr(int(rng.integers(1, 20)), 20) for _ in range(n)]
    c = [Fr(int(rng.integers(1, 5))) for _ in range(n)]
    B = Fr(int(rng.integers(3, 9)))
    b1, b2 = meilleurs_ensembles(p, c, B)
    n_inst += 1
    echec = Fr(1)
    for i in b2[1]:
        echec *= (1 - p[i])
    if (1 - echec) < b1[0]:
        n_diff += 1
        perte_max = max(perte_max, b1[0] - (1 - echec))
print(f"instances : {n_inst} (n = 6) ; l'optimum du nombre espéré perd sur « au moins une » dans {n_diff} "
      f"cas, perte maximale {float(perte_max):.3f}")

print()
print("=== B3. Règle de Pandore (Weitzman) contre programmation dynamique exhaustive ===")


def valeur_reserve(xs, ps, c):
    """z tel que c = E[(X - z)^+], X discret (valeurs xs croissantes, probabilités ps)."""
    esp = sum(x * p for x, p in zip(xs, ps))
    z = esp - c
    if z <= xs[0]:
        return z
    for k in range(len(xs) - 1):
        A = sum(x * p for x, p in zip(xs[k + 1:], ps[k + 1:]))
        Bk = sum(ps[k + 1:])
        z = (A - c) / Bk
        if xs[k] <= z <= xs[k + 1]:
            return z
    raise RuntimeError("valeur de réserve introuvable")


def pandore(boites):
    """boites : liste de (xs, ps, c). Retourne (optimum exhaustif, politique de réserve,
    politique d'indice E[X]/c)."""
    n = len(boites)
    z = [valeur_reserve(*b) for b in boites]
    ratio = [sum(x * p for x, p in zip(b[0], b[1])) / b[2] for b in boites]

    @lru_cache(maxsize=None)
    def opt(U, y):
        best = y
        for i in U:
            xs, ps, c = boites[i]
            reste = tuple(j for j in U if j != i)
            v = -c + sum(p * opt(reste, max(y, x)) for x, p in zip(xs, ps))
            best = max(best, v)
        return best

    @lru_cache(maxsize=None)
    def reserve(U, y):
        if not U:
            return y
        i = max(U, key=lambda j: z[j])
        if z[i] <= y:
            return y
        xs, ps, c = boites[i]
        reste = tuple(j for j in U if j != i)
        return -c + sum(p * reserve(reste, max(y, x)) for x, p in zip(xs, ps))

    @lru_cache(maxsize=None)
    def naif(U, y):
        """Ouvre par E[X]/c décroissant ; s'arrête quand aucune boîte restante n'a de gain
        myope positif E[(X - y)^+] - c > 0 (règle d'arrêt myope, la plus favorable à l'indice)."""
        if not U:
            return y
        utiles = [j for j in U
                  if sum(p * max(x - y, 0) for x, p in zip(boites[j][0], boites[j][1])) > boites[j][2]]
        if not utiles:
            return y
        i = max(utiles, key=lambda j: ratio[j])
        xs, ps, c = boites[i]
        reste = tuple(j for j in U if j != i)
        return -c + sum(p * naif(reste, max(y, x)) for x, p in zip(xs, ps))

    tout = tuple(range(n))
    return opt(tout, Fr(0)), reserve(tout, Fr(0)), naif(tout, Fr(0))


n_inst = n_egal = n_naif_moins = 0
perte_naif = Fr(0)
for _ in range(300):
    n = int(rng.integers(3, 6))
    boites = []
    for _ in range(n):
        k = int(rng.integers(2, 4))
        xs = sorted(int(v) for v in rng.choice(np.arange(0, 13), size=k, replace=False))
        brut = [int(v) for v in rng.integers(1, 6, size=k)]
        ps = [Fr(b, sum(brut)) for b in brut]
        c = Fr(int(rng.integers(1, 9)), 4)
        boites.append((tuple(Fr(x) for x in xs), tuple(ps), c))
    v_opt, v_res, v_naif = pandore(boites)
    n_inst += 1
    n_egal += (v_opt == v_res)
    if v_naif < v_opt:
        n_naif_moins += 1
        perte_naif = max(perte_naif, (v_opt - v_naif) / v_opt if v_opt > 0 else Fr(0))
print(f"instances : {n_inst} (3 à 5 boîtes, lois à 2 ou 3 valeurs) ; politique de réserve = optimum : {n_egal}")
print(f"politique d'indice E[X]/c strictement sous l'optimum : {n_naif_moins} cas, perte relative maximale "
      f"{float(perte_naif):.3f}")
A = ((Fr(0), Fr(2)), (Fr(1, 10), Fr(9, 10)), Fr(1, 2))
Bb = ((Fr(0), Fr(10)), (Fr(9, 10), Fr(1, 10)), Fr(1, 2))
zA, zB = valeur_reserve(*A), valeur_reserve(*Bb)
print(f"exemple A (q=0,9 ; V=2 ; c=0,5) et B (q=0,1 ; V=10 ; c=0,5) : q·V/c = 3,6 et 2,0 ; "
      f"valeurs de réserve V - c/q = {float(zA):.3f} et {float(zB):.3f}")
v_opt, v_res, v_naif = pandore([A, Bb])
print(f"  gain espéré : optimum {float(v_opt):.4f}, réserve (B puis A) {float(v_res):.4f}, "
      f"q·V/c (A puis B) {float(v_naif):.4f}")

# =============================================================================================
print()
print("=== C. Allocation de Koopman discrète : P = somme_i pi_i·(1 - (1 - a_i)^n_i), somme n_i = B ===")
rng = np.random.default_rng(ss_c)


def compositions(B, m):
    if m == 1:
        yield (B,)
        return
    for k in range(B + 1):
        for reste in compositions(B - k, m - 1):
            yield (k,) + reste


def detection(n, pi, a):
    return sum(pi[i] * (1 - (1 - a[i]) ** n[i]) for i in range(len(pi)))


def glouton(B, pi, a):
    n = [0] * len(pi)
    for _ in range(B):
        i = max(range(len(pi)), key=lambda j: pi[j] * a[j] * (1 - a[j]) ** n[j])
        n[i] += 1
    return tuple(n)


n_inst = n_ok = 0
for _ in range(150):
    m = 4
    brut = [int(v) for v in rng.integers(1, 10, size=m)]
    pi = [Fr(b, sum(brut)) for b in brut]
    a = [Fr(int(rng.integers(1, 12)), 40) for _ in range(m)]
    B = int(rng.integers(5, 19))
    meilleur = max(detection(n, pi, a) for n in compositions(B, m))
    n_inst += 1
    n_ok += (detection(glouton(B, pi, a), pi, a) == meilleur)
print(f"instances : {n_inst} (4 cellules, budget de 5 à 18 tirages) ; glouton marginal = optimum exhaustif : {n_ok}")
pi = [0.40, 0.30, 0.20, 0.10]
a = [0.20, 0.05, 0.02, 0.20]
print("exemple : a priori pi = (0,40 ; 0,30 ; 0,20 ; 0,10), largeur des puits a = (0,20 ; 0,05 ; 0,02 ; 0,20)")
print("  (la cellule 3 est le puits étroit : pi·a = 0,004, le plus faible)")
for B in (10, 30, 100, 300, 1000):
    n = glouton(B, pi, a)
    reste = [pi[i] * (1 - a[i]) ** n[i] for i in range(4)]
    tot = sum(reste)
    post = [r / tot for r in reste]
    print(f"  budget {B:5d} : tirages {n} ; P(trouvé) = {1 - tot:.4f} ; a posteriori après échec = "
          + " ; ".join(f"{x:.3f}" for x in post))
print("  (limite continue : pi_i·a_i·exp(-a_i·z_i) égal entre cellules fouillées, donc masse restante en 1/a_i)")

# =============================================================================================
print()
print("=== D. Viser le maximum : étalement, seuil de croisement, contre-exemple ===")


def esp_max(xs, ps, n):
    """Espérance exacte du maximum de n tirages indépendants d'une loi discrète."""
    xs_ps = sorted(zip(xs, ps))
    tot, cdf_prec = Fr(0), Fr(0)
    for x, p in xs_ps:
        cdf = cdf_prec + p
        tot += x * (cdf ** n - cdf_prec ** n)
        cdf_prec = cdf
    return tot


X = ([Fr(4), Fr(6)], [Fr(1, 2), Fr(1, 2)])            # moyenne 5
Y2 = ([Fr(2), Fr(4), Fr(6), Fr(8)], [Fr(1, 4), Fr(1, 4), Fr(1, 4), Fr(1, 4)])  # X + bruit +-2 de moyenne nulle
print("X : 4 ou 6 (1/2, 1/2) ; Y2 = X + bruit indépendant de moyenne nulle (+2 ou -2) : étalement à moyenne constante")
for n in (1, 2, 3, 5, 10, 30):
    print(f"  n = {n:2d} : E[max] X = {float(esp_max(*X, n)):.4f} ; Y2 = {float(esp_max(*Y2, n)):.4f}")


def queue_normale(w, mu, sigma):
    return 0.5 * math.erfc((w - mu) / (sigma * math.sqrt(2)))


muA, sA, muB, sB = 0.0, 2.0, 1.0, 1.0
w_croise = (muB * sA - muA * sB) / (sA - sB)
print(f"famille normale : A (moyenne {muA}, écart type {sA}), B (moyenne {muB}, écart type {sB}) ; "
      f"seuil de croisement w* = {w_croise:.3f}")
for w in (0.0, 1.0, 1.9, 2.0, 2.1, 3.0, 5.0):
    pa, pb = queue_normale(w, muA, sA), queue_normale(w, muB, sB)
    print(f"  seuil {w:.1f} : P(A >= w) = {pa:.5f} ; P(B >= w) = {pb:.5f} ; A devant : {pa > pb}")
z = np.linspace(-10, 10, 400001)
dz = z[1] - z[0]
phi = np.exp(-z * z / 2) / math.sqrt(2 * math.pi)
Phi = np.cumsum(phi) * dz
m_n = {}
for n in range(1, 13):
    m_n[n] = float(np.sum(z * n * Phi ** (n - 1) * phi) * dz)
n_star = min(n for n in m_n if muA + sA * m_n[n] > muB + sB * m_n[n])
print("  espérance du maximum de n normales réduites : " + " ; ".join(f"m_{n} = {m_n[n]:.3f}" for n in (2, 3, 4, 5, 10)))
print(f"  E[max de n] : A dépasse B dès n = {n_star} (condition m_n > (muB - muA)/(sA - sB) = "
      f"{(muB - muA) / (sA - sB):.3f})")
print("contre-exemple : A = +3 ou -3 (1/2, 1/2), variance 9 ; B = 0 (0,98), +5 (0,01), -5 (0,01), variance 0,5")
print("  P(A >= 4) = 0 ; P(B >= 4) = 0,01 : la variance la plus forte a la queue la plus faible au-delà de 4")

# =============================================================================================
print()
print("=== E. Diversité et corrélation ===")
rng = np.random.default_rng(ss_e)


def moment_beta(alpha, beta, m):
    """E[(1 - A)^m] pour A de loi Beta(alpha, beta), exact (rationnel si alpha, beta rationnels)."""
    r = Fr(1)
    for j in range(m):
        r *= (beta + j) / (alpha + beta + j)
    return r


al, be = Fr(1, 2), Fr(9, 2)   # moyenne 0,1
print("E1. latent partagé A de loi Beta(0,5 ; 4,5), moyenne 0,1 : P(au moins un succès en n tirages)")
for n in (1, 5, 20, 100, 1000):
    melange = 1 - moment_beta(al, be, n)
    indep = 1 - Fr(9, 10) ** n
    print(f"  n = {n:4d} : tirages corrélés {float(melange):.4f} ; tirages indépendants de même taux {float(indep):.4f}")
print("  cas extrême A = 0 ou 1 (probabilité 0,1 d'être 1) : 0,1000 quel que soit n")

print("E2. n tirages répartis entre K proposeurs à latents indépendants de même loi (compositions exhaustives)")
n_inst = n_ok = n_pire = 0
for _ in range(200):
    alpha = Fr(int(rng.integers(1, 9)), 4)
    beta = Fr(int(rng.integers(4, 40)), 4)
    K = int(rng.integers(2, 5))
    n = int(rng.integers(K, 16))
    res = {}
    for comp in compositions(n, K):
        echec = Fr(1)
        for nk in comp:
            echec *= moment_beta(alpha, beta, nk)
        res[comp] = 1 - echec
    meilleur = max(res.values())
    pire = min(res.values())
    egal = tuple(n // K + (1 if i < n % K else 0) for i in range(K))
    n_inst += 1
    n_ok += (res[egal] == meilleur)
    tout_en_un = tuple([0] * (K - 1) + [n])
    n_pire += (res[tout_en_un] == pire)
print(f"  instances : {n_inst} ; la répartition la plus égale atteint l'optimum : {n_ok} ; "
      f"tout sur un seul proposeur est le pire : {n_pire}")
for comp in ((12, 0, 0), (6, 6, 0), (4, 4, 4)):
    echec = Fr(1)
    for nk in comp:
        echec *= moment_beta(al, be, nk)
    print(f"  Beta(0,5 ; 4,5), 12 tirages répartis {comp} : P(au moins un) = {float(1 - echec):.4f}")
print(f"  référence indépendante (aucun latent) : {1 - 0.9 ** 12:.4f}")
print("E3. latent commun aux K proposeurs : P = 1 - E[(1 - A)^n] pour toute répartition (identité) ;")
print(f"  ici {float(1 - moment_beta(al, be, 12)):.4f} pour (12,0,0), (6,6,0) et (4,4,4)")

print("E4. sous-modularité de f(S) = P(union des succès) et de E[max], dépendance quelconque (exhaustif)")
viol_union = viol_max = 0
ratio_union = ratio_max = 1.0
n_inst = 0
for _ in range(120):
    n_atomes, m = 8, 6
    brut = rng.integers(1, 10, size=n_atomes)
    prob = brut / brut.sum()
    E = rng.random((m, n_atomes)) < 0.3
    Xv = rng.integers(0, 10, size=(m, n_atomes)).astype(float) * (rng.random((m, n_atomes)) < 0.5)

    def f_union(S):
        if not S:
            return 0.0
        return float(prob[np.any(E[list(S)], axis=0)].sum())

    def f_max(S):
        if not S:
            return 0.0
        return float((prob * Xv[list(S)].max(axis=0)).sum())

    n_inst += 1
    for f, nom in ((f_union, "union"), (f_max, "max")):
        ens = [frozenset(c) for r in range(m + 1) for c in itertools.combinations(range(m), r)]
        val = {S: f(S) for S in ens}
        for S in ens:
            for T in ens:
                if S < T:
                    for i in range(m):
                        if i not in T:
                            if val[S | {i}] - val[S] < val[T | {i}] - val[T] - 1e-12:
                                if nom == "union":
                                    viol_union += 1
                                else:
                                    viol_max += 1
        for k in range(1, m):
            opt_k = max(val[S] for S in ens if len(S) == k)
            S = frozenset()
            for _ in range(k):
                i = max((j for j in range(m) if j not in S), key=lambda j: val[S | {j}])
                S = S | {i}
            if opt_k > 0:
                r = val[S] / opt_k
                if nom == "union":
                    ratio_union = min(ratio_union, r)
                else:
                    ratio_max = min(ratio_max, r)
print(f"  instances : {n_inst} (6 candidats, 8 états du monde) ; violations des rendements décroissants : "
      f"union {viol_union}, maximum {viol_max}")
print(f"  pire rapport glouton/optimum à cardinal fixé : union {ratio_union:.4f}, maximum {ratio_max:.4f} "
      f"(borne de Nemhauser, Wolsey et Fisher : {1 - 1 / math.e:.4f})")
print("  contre-exemple composite : découverte = pièce 1 ET pièce 2 ; f({1}) = f({2}) = 0, f({1,2}) = 1 ;")
print("  gain marginal de 2 : 0 seul, 1 après 1 : rendements croissants, le glouton ne voit rien (rapport 0)")

# =============================================================================================
print()
print("=== F. Filtre bon marché avant une épreuve chère ===")
rng = np.random.default_rng(ss_f)


def taux(pi, q, alpha, cg, cf, cv, filtre=True):
    """Vraies découvertes par unité de coût, candidats abondants, épreuve exacte."""
    if not filtre:
        return pi / (cg + cv)
    r = pi * q + (1 - pi) * alpha
    return pi * q / (cg + cf + r * cv)


n_inst = n_ok = 0
for _ in range(5000):
    pi = Fr(int(rng.integers(1, 50)), 100)
    q = Fr(int(rng.integers(1, 100)), 100)
    alpha = Fr(int(rng.integers(0, 100)), 100)
    cg, cf, cv = (Fr(int(rng.integers(1, 40)), 20), Fr(int(rng.integers(0, 40)), 20),
                  Fr(int(rng.integers(1, 400)), 20))
    gain = taux(pi, q, alpha, cg, cf, cv) - taux(pi, q, alpha, cg, cf, cv, filtre=False)
    critere = cv * (1 - pi) * (q - alpha) - (1 - q) * cg - cf
    n_inst += 1
    n_ok += ((gain > 0) == (critere > 0)) and ((gain == 0) == (critere == 0))
print(f"F1. instances : {n_inst} ; signe du gain = signe de c_v·(1 - pi)·(q - alpha) - (1 - q)·c_g - c_f : {n_ok}")

print("F2. table de Carbon recalculée (pi = 0,04 ; 500 candidats ; filtre 0,05 ; épreuve 8 ; budget 100)")
for nom, alpha, q in (("aucun filtre", 1.0, 1.0), ("faible", 0.25, 0.70), ("modéré", 0.08, 0.75),
                      ("rigoureux", 0.02, 0.80), ("strict", 0.005, 0.75), ("mort", 0.001, 0.0)):
    pi0, N, cf, cv, Bt = 0.04, 500, 0.05, 8.0, 100.0
    promus = N * (pi0 * q + (1 - pi0) * alpha)
    ppv = pi0 * q / (pi0 * q + (1 - pi0) * alpha) if promus > 0 else 0.0
    M = math.floor(max(0.0, Bt - N * cf) / cv)
    v = min(promus, M) * ppv
    print(f"  {nom:12s} : promus {promus:6.1f} ; précision {ppv:.4f} ; éprouvés {min(promus, M):5.1f} ; "
          f"vraies découvertes {v:.2f}")
print(f"  rapport strict/aucun : {(9 * 0.03 / 0.0348) / (9 * 0.04):.2f} = précision/pi ; plafond 1/pi = {1 / 0.04:.0f}")
print(f"  précision > 1/2 si et seulement si alpha < q·pi/(1 - pi) ; ici q = 0,75 : alpha < {0.75 * 0.04 / 0.96:.4f}")

print("F3. contre-exemple : idées profondes sous-notées par le filtre")
pi_s, pi_d, q_s, q_d, alpha = 0.04, 0.004, 0.90, 0.10, 0.02
cg, cf, cv = 0.05, 0.05, 8.0
r = pi_s * q_s + pi_d * q_d + (1 - pi_s - pi_d) * alpha
sans = (pi_s / (cg + cv), pi_d / (cg + cv))
avec = (pi_s * q_s / (cg + cf + r * cv), pi_d * q_d / (cg + cf + r * cv))
seuil = (cg + cf + r * cv) / (cg + cv)
print(f"  taux de passage du filtre r = {r:.4f} ; seuil de sensibilité utile (c_g + c_f + r·c_v)/(c_g + c_v) = {seuil:.4f}")
print(f"  pour 100 unités de coût, sans filtre : ordinaires {100 * sans[0]:.3f}, profondes {100 * sans[1]:.4f}")
print(f"  pour 100 unités de coût, avec filtre : ordinaires {100 * avec[0]:.3f}, profondes {100 * avec[1]:.4f}")
print(f"  le filtre multiplie les ordinaires par {avec[0] / sans[0]:.1f} et les profondes par {avec[1] / sans[1]:.2f} "
      f"(q_d = {q_d} contre seuil {seuil:.4f})")
q_d2 = 0.03
avec2 = pi_d * q_d2 / (cg + cf + (pi_s * q_s + pi_d * q_d2 + (1 - pi_s - pi_d) * alpha) * cv)
print(f"  si q_d = {q_d2} (sous le seuil) : profondes multipliées par {avec2 / sans[1]:.2f} : le filtre les détruit")

print("F4. contre-exemple : candidats rares (20 candidats, budget suffisant pour tout éprouver)")
print(f"  sans filtre : {20 * 0.04:.2f} vraies découvertes attendues ; avec filtre (q = 0,75) : {20 * 0.04 * 0.75:.2f}")

print("F5. vérification par tirage (pi = 0,04 ; q = 0,75 ; alpha = 0,02 ; c_g = 0,05 ; c_f = 0,05 ; c_v = 8)")
nb = 400000
vrai = rng.random(nb) < 0.04
passe = np.where(vrai, rng.random(nb) < 0.75, rng.random(nb) < 0.02)
cout_avec = nb * 0.10 + passe.sum() * 8.0
cout_sans = nb * 8.05
print(f"  taux simulé avec filtre {(vrai & passe).sum() / cout_avec:.5f} (formule {taux(0.04, 0.75, 0.02, 0.05, 0.05, 8.0):.5f}) ; "
      f"sans filtre {vrai.sum() / cout_sans:.5f} (formule {0.04 / 8.05:.5f})")

# =============================================================================================
print()
print("=== G. Criticalité de l'émergence ===")
rng = np.random.default_rng(ss_g)

print("G1. Galton-Watson à descendance de Poisson de moyenne n : extinction et descendance totale")
for n in (0.5, 0.9, 1.0, 1.1, 1.5, 2.0):
    eta = 0.0
    for _ in range(200000):
        eta = math.exp(n * (eta - 1.0))
    tot = []
    survie = 0
    for _ in range(4000):
        actifs, cumul = 1, 1
        while actifs > 0 and cumul < 5000:
            actifs = int(rng.poisson(n * actifs))
            cumul += actifs
        if cumul >= 5000:
            survie += 1
        else:
            tot.append(cumul)
    th = f"théorie 1/(1 - n) = {1 / (1 - n):.2f}" if n < 1 else "sans objet au-delà de n = 1"
    print(f"  n = {n:.1f} : P(extinction) théorique {eta:.4f} ; part simulée dépassant 5 000 naissances "
          f"{survie / 4000:.4f} ; descendance moyenne des lignées éteintes {np.mean(tot):.2f} ({th})")


def plus_grande_composante(n_noeuds, aretes):
    parent = list(range(n_noeuds))

    def trouve(x):
        racine = x
        while parent[racine] != racine:
            racine = parent[racine]
        while parent[x] != racine:
            parent[x], x = racine, parent[x]
        return racine

    for u, v in aretes:
        ru, rv = trouve(u), trouve(v)
        if ru != rv:
            parent[ru] = rv
    racines = np.array([trouve(i) for i in range(n_noeuds)])
    return np.bincount(racines).max()


print("G2. graphe biparti aléatoire (500 concepts d'un côté, 8 000 de l'autre) : seuil c_A·c_B = 1")
NA, NB = 500, 8000
for prod in (0.5, 0.8, 1.0, 1.5, 2.0, 4.0):
    p = math.sqrt(prod / (NA * NB))
    cA, cB = p * NB, p * NA
    x = y = 0.5
    for _ in range(20000):
        x = math.exp(-cA * (1 - y))
        y = math.exp(-cB * (1 - x))
    part_th = (NA * (1 - x) + NB * (1 - y)) / (NA + NB)
    parts = []
    for _ in range(12):
        nb_ar = rng.binomial(NA * NB, p)
        ua = rng.integers(0, NA, size=nb_ar)
        vb = NA + rng.integers(0, NB, size=nb_ar)
        parts.append(plus_grande_composante(NA + NB, zip(ua.tolist(), vb.tolist())) / (NA + NB))
    print(f"  c_A = {cA:.2f}, c_B = {cB:.3f}, produit {prod:.1f} : plus grande composante simulée {np.mean(parts):.4f} ; "
          f"théorie (taille infinie) {part_th:.4f}")

print("G3. opérateur sans retour : même rayon spectral, seuils différents (boucles courtes)")


def aretes_triangulaire(L):
    ar = set()
    for i in range(L):
        for j in range(L):
            u = i * L + j
            for di, dj in ((1, 0), (0, 1), (1, 1)):
                v = ((i + di) % L) * L + (j + dj) % L
                ar.add((min(u, v), max(u, v)))
    return sorted(ar)


def rayon_sans_retour(n_noeuds, aretes):
    orient = [(u, v) for u, v in aretes] + [(v, u) for u, v in aretes]
    idx = {e: k for k, e in enumerate(orient)}
    Bm = np.zeros((len(orient), len(orient)))
    sortants = {}
    for (u, v) in orient:
        sortants.setdefault(u, []).append((u, v))
    for (u, v) in orient:
        for (_, w) in sortants.get(v, []):
            if w != u:
                Bm[idx[(u, v)], idx[(v, w)]] = 1.0
    return float(np.max(np.abs(np.linalg.eigvals(Bm))))


def recable(aretes, rng, tours=10):
    """Recâblage de Maslov et Sneppen : échanges de doubles arêtes qui conservent tous les degrés,
    sans boucle ni arête multiple. Détruit les triangles du réseau, garde le degré 6."""
    ar = [tuple(e) for e in aretes]
    present = set(ar)
    m = len(ar)
    for _ in range(tours * m):
        i, j = int(rng.integers(0, m)), int(rng.integers(0, m))
        if i == j:
            continue
        (a, b), (c, d) = ar[i], ar[j]
        if rng.random() < 0.5:
            c, d = d, c
        if len({a, b, c, d}) < 4:
            continue
        n1, n2 = (min(a, d), max(a, d)), (min(c, b), max(c, b))
        if n1 in present or n2 in present:
            continue
        present.discard(ar[i])
        present.discard(ar[j])
        ar[i], ar[j] = n1, n2
        present.add(n1)
        present.add(n2)
    return sorted(ar)


petit_tri = aretes_triangulaire(6)
petit_reg = recable(petit_tri, rng)
print(f"  rayon spectral de l'opérateur sans retour : réseau triangulaire 6×6 (tore) {rayon_sans_retour(36, petit_tri):.4f} ; "
      f"le même recâblé à degrés constants {rayon_sans_retour(36, petit_reg):.4f} (degré - 1 = 5 ; seuil prédit 0,2)")
k47 = [(i, 4 + j) for i in range(4) for j in range(7)]
print(f"  biparti complet à 4 et 7 nœuds : rayon {rayon_sans_retour(11, k47):.4f} ; racine de (4 - 1)·(7 - 1) = "
      f"{math.sqrt(18):.4f} (d'où le seuil p²·(N_A - 1)·(N_B - 1) = 1, soit c_A·c_B = 1 en grande taille)")
L = 64
tri = aretes_triangulaire(L)
reg = recable(tri, rng)


def nb_triangles(n_noeuds, aretes):
    vois = [set() for _ in range(n_noeuds)]
    for u, v in aretes:
        vois[u].add(v)
        vois[v].add(u)
    return sum(len(vois[u] & vois[v]) for u, v in aretes) // 3


print(f"  réseau triangulaire {L}×{L} : {nb_triangles(L * L, tri)} triangles ; après recâblage : {nb_triangles(L * L, reg)}")
tri_a, reg_a = np.array(tri), np.array(reg)
for p in (0.15, 0.20, 0.25, 0.30, 0.3473, 0.40, 0.50):
    pt, pr = [], []
    for _ in range(8):
        garde = rng.random(len(tri_a)) < p
        pt.append(plus_grande_composante(L * L, tri_a[garde].tolist()) / (L * L))
        garde = rng.random(len(reg_a)) < p
        pr.append(plus_grande_composante(L * L, reg_a[garde].tolist()) / (L * L))
    print(f"  probabilité de lien {p:.4f} (p × rayon = {5 * p:.2f}) : plus grande composante, réseau triangulaire "
          f"{np.mean(pt):.4f} ; recâblé {np.mean(pr):.4f}")
print("  (seuil exact connu du réseau triangulaire : 2·sin(pi/18) = "
      f"{2 * math.sin(math.pi / 18):.4f} ; graphe en arbre de degré 6 : 1/5)")

print("G4. vivier fini : chaque naissance en induit n en moyenne parmi M = 2 000 paires encore à naître")
M = 2000
for n in (0.8, 1.5, 3.0):
    r = 0.5
    for _ in range(10000):
        r = 1 - math.exp(-n * r)
    finales = []
    for _ in range(200):
        ne = np.zeros(M, dtype=bool)
        ne[0] = True
        front = 1
        while front > 0:
            essais = rng.integers(0, M, size=rng.poisson(n * front))
            nouveaux = np.unique(essais[~ne[essais]])
            ne[nouveaux] = True
            front = len(nouveaux)
        finales.append(ne.sum() / M)
    finales = np.array(finales)
    grandes = finales[finales > 0.1]
    print(f"  n = {n:.1f} : part finale des avalanches étendues {grandes.mean() if len(grandes) else 0.0:.4f} "
          f"(théorie r = 1 - exp(-n·r) : {r:.4f}) ; part des amorces qui s'étendent {len(grandes) / 200:.3f}")

print("G5. cortège : rapport de branchement n = (exp(zeta) - 1)·m·(taux de base × durée)")
print("  (m paires alignées par la correspondance, taux de base × durée = 0,01 par paire)")
for mult in (1.5, 3.0, 6.0):
    ligne = []
    for m in (5, 20, 80, 320):
        ligne.append(f"m = {m:3d} : n = {(mult - 1) * m * 0.01:.2f}")
    print(f"  multiplicateur exp(zeta) = {mult:.1f} -> " + " ; ".join(ligne))
