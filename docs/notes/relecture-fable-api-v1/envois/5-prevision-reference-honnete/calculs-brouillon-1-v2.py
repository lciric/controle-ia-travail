"""Calculs cités par `brouillon-1-v2.md` (prévision chiffrée de la loi de la référence honnête, version 2,
corrections de la contre-lecture portées par Opus 5.5).

Aucune donnée du programme n'est lue. Aucun tirage au hasard, aucune simulation : formes fermées et
une intégrale à une dimension (bloc R8). Tout chiffre vaut sous supposition : scores normaux, unités
indépendantes, pas d'effet de monde (gain d'appariement E = 1), bruit indépendant entre l'original
honnête et l'épisode saboté d'un monde, jumeau exact sauf mention, approximation normale des sommes
et méthode delta au premier ordre ; erreurs de tirage des configurations comptées comme indépendantes
entre horizons et entre statistiques (choix prudent : les nombres aléatoires communs les réduiraient).
Aucun chiffre n'est une mesure.

Blocs A à L : ceux de la version 1, recopiés à l'identique.
Blocs R4 à R9 : un par constat de la contre-lecture qui demande un calcul (numéro du constat).

Lancer : .venv/bin/python calculs-brouillon-1-v2.py > calculs-brouillon-1-v2.txt  (scipy pour R8 seulement)
"""
import math
from statistics import NormalDist as N

P = N().cdf
q = N().inv_cdf
phi = N().pdf
z = q(.99)

# ---------------------------------------------------------------- blocs de la version 1, à l'identique
print("== Blocs A à L de la version 1, rejoués à l'identique ==")
b = lambda x: round(100*(1-P(z-1.645/math.sqrt(x))),1)
print("A", round(z,4), round(math.sqrt(5/8),4), round(math.sqrt(.5),4), round(math.sqrt(1/4),4))
print("B", round(math.sqrt(.75),4), round(4**-.6,4), round(4**-.4,4))
print("C", round(math.sqrt(6/4)/math.sqrt(2),4), round(math.sqrt(6/4)/math.sqrt(5),4), round(2/4,2))
print("D", [round(100*P(z*(math.sqrt(r/(1+r))-1)),1) for r in (.5,1,2,4)], [round(100*P(z*(math.sqrt(r*4/6)-1)),1) for r in (.5,1,2,4)])
print("E", round(100*P(z*(1/.75-1)),1), round(100*P(z*(1/math.sqrt(6/4/5)-1)),1))
print("F", [round(100*(1-P(z/math.sqrt(1+r))),1) for r in (.25,1,4)])
print("G", [round((1.645/(z-q(1-.01*f)))**2,1) for f in (2,3,5)])
print("H", [b(x) for x in (60,15,24,6,6,1.5)])
print("I", round(1+1.645/math.sqrt(24)/(z/2),3), round(1+1.645/math.sqrt(60)/(z/2),3))
print("J", [round(z*math.sqrt(math.pi/3)*math.sqrt(2)/math.sqrt(m),2) for m in (40,100,400)])
print("K", round(math.sqrt(101)/math.sqrt(math.pi*6/12),2), round(math.sqrt(101)/math.sqrt(math.pi*5/9),2), round(100*z/(0.5*math.sqrt(400)),1))
print("L", [round(math.sqrt(x)/z,3) for x in (160/2400,400/2400,1600/2400)], [round(100*P((.75/math.sqrt(6/4/5)-1)/(math.sqrt(x)/z)-1.96)) for x in (160/2400,400/2400,1600/2400)])

# ---------------------------------------------------------------- réglages
W = 2400
K = 4
V = K * (K + 2) / 12                      # variance du rang centré parmi K + 1 valeurs échangeables
REGLAGES = {"A": 40, "B": 100, "C": 400}  # m ; n_max = 4 m
NCONF = 2000                              # configurations par horizon et par dose (version 1)


def tau_q(n_conf):
    """Erreur relative du seuil recalé (quantile à 99 % tiré de n_conf configurations honnêtes)."""
    return math.sqrt(.01 * .99 / n_conf) / phi(z) / z


def tau_r(n_conf):
    """Erreur relative de la dose de croisement à 50 % (rappel tiré de n_conf configurations)."""
    return math.sqrt(.25 / n_conf) / phi(0) / z


def binom(p, n_conf):
    return math.sqrt(p * (1 - p) / n_conf)


print()
print("== R4 (constat 4) : tirage du flux avec ou sans remise ==")
for nom, m in REGLAGES.items():
    nmax, Wp = 4 * m, W - m
    pas_de_double = math.exp(sum(math.log(1 - i / Wp) for i in range(nmax)))
    distincts = Wp * (1 - (1 - 1 / Wp) ** nmax)
    print(f"R4 {nom} m = {m} n_max = {nmax} W - m = {Wp} | condition n_max <= W - m : {nmax <= Wp}"
          f" | avec remise : au moins un doublon {100*(1-pas_de_double):.1f} % ; part de doublons {100*(1-distincts/nmax):.1f} %")
print("R4 effet du tirage sans remise sur le taux réalisé du seuil nominal du rang (jumeau exact, un vivier de W - m mondes) :")
for nom, m in REGLAGES.items():
    Wp = W - m
    lig = []
    for n in (m // 4, m // 2, m, 2 * m, 4 * m):
        f = (Wp - n) / (Wp - 1)
        mediane = 1 - P(z / math.sqrt(f))
        attendu = 1 - P(z / math.sqrt(f + n / Wp))
        lig.append(f"n = {n} : médiane {100*mediane:.2f} %, moyenne sur les viviers {100*attendu:.2f} %")
    print(f"R4 {nom} | " + " ; ".join(lig))

print()
print("== R5 (constat 5) : puissance de l'épreuve de l'écart, lecture principale et lecture attestée ==")
print("R5 formes : erreur relative de kappa, en multiple de racine(n_max/(W - m))/z ;"
      " principale : racine((K + 2(1 - c + c²))/(K + 2)) ; attestée : c racine(2/(K + 2)) ; c = c2(n_max) par construction")
KAPPA = math.sqrt(6 / 4) / math.sqrt(5)   # 0,5477, valeur prédite de la version 1 (bloc C)
for nom, m in REGLAGES.items():
    nmax, Wp = 4 * m, W - m
    base = math.sqrt(nmax / Wp) / z
    beta = 1.645 * math.sqrt(nmax / W) / z
    k_att = KAPPA * (1 + beta)
    mc = tau_q(NCONF) ** 2 + 2 * tau_r(NCONF) ** 2
    lig = []
    for c in (.25, .5, .75):
        e_p = math.sqrt(base ** 2 * (K + 2 * (1 - c + c * c)) / (K + 2) + mc)
        e_a = math.sqrt((base * c * math.sqrt(2 / (K + 2))) ** 2 + mc)
        ch_p = P((.75 / KAPPA - 1) / e_p - 1.96)
        ch_a = P((.75 / k_att - 1) / e_a - 1.96)
        hors = " (c attesté hors plage)" if c * (1 + beta) > 1 else ""
        lig.append(f"c = {c} : principale erreur {100*e_p:.1f} %, chances {100*ch_p:.0f} % ; attestée erreur {100*e_a:.1f} %, chances {100*ch_a:.0f} %{hors}")
    valid = P((z - q(.97)) / math.sqrt(nmax / W) - 1.645)
    print(f"R5 {nom} | terme dominant seul (bloc L) {100*math.sqrt(nmax/W)/z:.1f} % | kappa principal {KAPPA:.4f} ; attesté {k_att:.4f}"
          f" | erreur de tirage des configurations (N = {NCONF}) : seuil recalé {100*tau_q(NCONF):.2f} %, croisement {100*tau_r(NCONF):.2f} %")
    print(f"R5 {nom} | " + " | ".join(lig))
    print(f"R5 {nom} | validité attestée jusqu'à n_max (borne haute du taux au plus 3 %), jumeau exact : {100*valid:.1f} %")
    # autre supposition : l'épisode saboté a le même bruit que l'original honnête de son monde (décalage pur)
    e_p1 = math.sqrt(base ** 2 + mc)
    e_a1 = math.sqrt(mc)
    print(f"R5 {nom} | bruit identique entre original et saboté : principale erreur {100*e_p1:.1f} %, chances {100*P((.75/KAPPA-1)/e_p1-1.96):.0f} %"
          f" ; attestée erreur {100*e_a1:.1f} %, chances {100*P((.75/k_att-1)/e_a1-1.96):.0f} %")

print()
print("== R6 (constat 6) : étape 0, tailles d'effet, erreurs types et tolérances ==")
# vérification des chiffres de la contre-lecture
se1 = binom(.01, NCONF)
p_h = 2 * (1 - P(.003 / se1))
p_n = 2 * (1 - P(.005 / se1))
print(f"R6 contrôle de la contre-lecture : erreur type d'un taux de 1 % sur {NCONF} configurations {100*se1:.3f} point ;"
      f" sortie d'un horizon à ± 0,3 point {100*p_h:.1f} % ; d'au moins un sur cinq {100*(1-(1-p_h)**5):.1f} % ;"
      f" monde nul à ± 0,5 point, dix lectures {100*(1-(1-p_n)**10):.1f} %")


def table_etape0(m, n_conf, k_se):
    """Rend la liste (objet, grandeur, centre, erreur type, tolérance v1, tolérance retenue), réglage de taille m."""
    nmax, Wp = 4 * m, W - m
    grille = (m // 4, m // 2, m, 2 * m, 4 * m)
    D = z * math.sqrt((2 * m + 1) / (12 * m * m)) / 0.60          # effet planté : c1(m) = 0,60
    mu = math.sqrt(2) * q(.5 + D)
    c1 = lambda n, M=m: z * math.sqrt((n + M + 1) / (12 * n * M)) / D
    c2 = lambda n: z * math.sqrt((K + 2) / (12 * K * n)) / D
    tq, tr = tau_q(n_conf), tau_r(n_conf)
    rel_ratio = math.sqrt(2 * (tq ** 2 + tr ** 2))
    L = []

    def ajoute(obj, gr, centre, se, tol_v1):
        L.append((obj, gr, centre, se, tol_v1, max(tol_v1, k_se * se)))

    # 1. référence exacte, 1 000 m unités
    M = 1000 * m
    r1x = c1(nmax, M) / c1(m, M)
    ajoute("référence exacte", "rho1", r1x, r1x * rel_ratio, .05)
    # 2. référence fixe
    r1 = c1(nmax) / c1(m)
    ajoute("référence fixe", "rho1", r1, r1 * rel_ratio, .05)
    # taille utile : pente / ordonnée de c1² contre 1/n, moindres carrés, erreurs indépendantes par point
    xs = [1 / n for n in grille]
    ys = [c1(n) ** 2 for n in grille]
    sig = [2 * math.sqrt(tq ** 2 + tr ** 2) * y for y in ys]

    def rapport(yv):
        xb, yb = sum(xs) / len(xs), sum(yv) / len(yv)
        pente = sum((x - xb) * (y - yb) for x, y in zip(xs, yv)) / sum((x - xb) ** 2 for x in xs)
        return pente / (yb - pente * xb)
    t0 = rapport(ys)
    var = 0.0
    for i in range(len(ys)):
        h = 1e-7 * ys[i]
        yp = list(ys); yp[i] += h
        var += ((rapport(yp) - t0) / h * sig[i]) ** 2
    ajoute("référence fixe", "taille utile, en parts de m", t0 / m, math.sqrt(var) / m, .325)  # bande v1 : 0,7 à 1,4 m ; marge basse, la plus étroite
    # 3. nul par unité, effet planté
    r2 = c2(nmax) / c2(m)
    ajoute("nul par unité", "rho2", r2, r2 * math.sqrt(m / (z * z * Wp) + 2 * tr ** 2), .05)
    for n in grille:
        f = (Wp - n) / (Wp - 1)
        centre = 1 - P(z / math.sqrt(f + n / Wp))
        pool = phi(z / math.sqrt(f)) * math.sqrt(n / Wp) / math.sqrt(f)
        ajoute("nul par unité", f"taux réalisé à n = {n}", centre, math.sqrt(binom(.01, n_conf) ** 2 + pool ** 2), .003)
    c = c2(nmax)
    kap = c2(nmax) / c1(nmax)
    e_k = math.sqrt((nmax / (z * z * Wp)) * (K + 2 * (1 - c + c * c)) / (K + 2) + tq ** 2 + 2 * tr ** 2)
    ajoute("nul par unité et référence fixe (même vivier)", "kappa", kap, kap * e_k, .08)
    # 4. jumeau faussé : décalage de T2(m) de 0,68 écart type
    f = (Wp - m) / (Wp - 1)
    a = math.sqrt(m / Wp)
    centre = 1 - P((z - .68) / math.sqrt(f + a * a))
    pool = phi((z - .68) / math.sqrt(f)) * a / math.sqrt(f)
    ajoute("jumeau faussé", f"taux à n = {m}", centre, math.sqrt(binom(centre, n_conf) ** 2 + pool ** 2), .01)
    # 5. référence d'un autre régime, taille utile m/2
    for n, nom in ((m, "taux nominal à n = m"), (nmax, "taux nominal à n = 4m")):
        p_ = 1 - P(z * math.sqrt((1 / n + 1 / m) / (1 / n + 2 / m)))
        ajoute("autre régime", nom, p_, binom(p_, n_conf), .01)
    r1r = math.sqrt((1 / nmax + 2 / m) / (1 / m + 2 / m))
    ajoute("autre régime", "rho1 recalé", r1r, r1r * rel_ratio, .05)
    # 6. grappes de 5, corrélation 0,2 : effet de plan 1,8
    ajoute("grappes", "seuil recalé par grappes, configurations neuves", .01, math.sqrt(2) * binom(.01, n_conf), .003)
    p_b = 1 - P(z / math.sqrt(1.8))
    thr = math.sqrt(.0099 / n_conf) / phi(z)
    ajoute("grappes", "seuil recalé par unités brassées", p_b,
           math.sqrt(binom(p_b, n_conf) ** 2 + (phi(z / math.sqrt(1.8)) / math.sqrt(1.8) * thr) ** 2), .01)
    # 7. monde nul : dix lectures (cinq horizons, deux statistiques, dose pleine)
    for n in grille:
        ajoute("monde nul", f"statistique étalonnée, n = {n}", .01, math.sqrt(2) * binom(.01, n_conf), .005)
    for n in grille:
        f = (Wp - n) / (Wp - 1)
        centre = 1 - P(z / math.sqrt(f + n / Wp))
        pool = phi(z / math.sqrt(f)) * math.sqrt(n / Wp) / math.sqrt(f)
        ajoute("monde nul", f"rang, n = {n}", centre, math.sqrt(binom(.01, n_conf) ** 2 + pool ** 2), .005)
    # 8. étalonnage naïf
    for n, tol in ((m, .01), (nmax, .015)):
        p_ = 1 - P(z / math.sqrt(1 + n / m))
        ajoute("étalonnage naïf", f"taux à n = {n}", p_, binom(p_, n_conf), tol)
    return mu, D, L


def risque(L):
    pas = 1.0
    for (_, _, _, se, _, tol) in L:
        pas *= 1 - 2 * (1 - P(tol / se))
    return 1 - pas


for nom, m in REGLAGES.items():
    for n_conf in (NCONF, 20000):
        mu, D, L = table_etape0(m, n_conf, 3)
        print(f"R6 {nom} m = {m} | configurations {n_conf} | effet planté : c1(m) = 0,60, soit p - 1/2 = {D:.4f}, mu = {mu:.4f} écart type"
              f" | contrôles {len(L)} | risque qu'un code juste soit dit mort : tolérances v1 {100*risque([(a, b_, c_, s, t, t) for (a, b_, c_, s, t, _) in L]):.1f} %"
              f" ; tolérances retenues (au moins 3 erreurs types) {100*risque(L):.2f} %"
              f" ; à 4 erreurs types {100*risque(table_etape0(m, n_conf, 4)[2]):.3f} %")
        if n_conf == NCONF or nom == "A":
            for (obj, gr, centre, se, t1, t) in L:
                unite = 100 if ("taux" in gr or "seuil" in gr or "n =" in gr) and "rho" not in gr else 1
                fmt = (lambda v: f"{100*v:.2f} %") if unite == 100 else (lambda v: f"{v:.4f}")
                fmt_t = (lambda v: f"{100*v:.3f} point") if unite == 100 else (lambda v: f"{v:.4f}")
                print(f"R6 {nom} N={n_conf} | {obj} | {gr} | centre {fmt(centre)} | erreur type {fmt_t(se)}"
                      f" | tolérance v1 ± {fmt_t(t1)} ({t1/se:.2f} erreurs types) | retenue ± {fmt_t(t)}")

print()
print("== R7 (constat 7) : objet « témoins à taux p », p = 1 % ==")
m = 40
D = z * math.sqrt((2 * m + 1) / (12 * m * m)) / 0.60
for n in (160, 4000, 16000):
    mt = .01 * n
    c_t = z * math.sqrt((n + mt + 1) / (12 * n * mt)) / D
    c_x = z * math.sqrt(1 / (12 * n)) / D
    print(f"R7 n = {n} | témoins {mt:.1f} | part cachée {c_t:.3f}{' (hors plage)' if c_t > 1 else ''} | rapport à la référence exacte {c_t/c_x:.3f}"
          f" | erreur type du rapport (N = {NCONF}) {c_t/c_x*math.sqrt(2*(tau_q(NCONF)**2+tau_r(NCONF)**2)):.2f}")
print(f"R7 forme limite racine(1 + 1/p) = {math.sqrt(101):.3f}")

print()
print("== R8 (constat 8) : rangs simples contre scores normaux, rang parmi K tirages du jumeau ==")
from scipy import integrate  # noqa: E402


def score_normal_moyen(mu, k):
    """Espérance, sous un décalage mu, du score normal du rang rendu continu (variance 1 sous le nul)."""
    a = [q(r / (k + 1)) if 0 < r < k + 1 else (-math.inf if r == 0 else math.inf) for r in range(k + 2)]
    dens = [phi(v) if math.isfinite(v) else 0.0 for v in a]
    interieur = [(k + 1) * (dens[r] - dens[r + 1]) for r in range(k + 1)]

    def integrande(x):
        p = P(x)
        return phi(x - mu) * sum(math.comb(k, r) * p ** r * (1 - p) ** (k - r) * interieur[r] for r in range(k + 1))
    return integrate.quad(integrande, -10, 10 + mu, limit=400)[0]


for mu in (.02, .5):
    simple = K * (P(mu / math.sqrt(2)) - .5) / math.sqrt(V) / mu
    normal = score_normal_moyen(mu, K) / mu
    print(f"R8 mu = {mu} K = {K} | efficacité, rang simple {simple:.4f} ; score normal {normal:.4f}"
          f" | kappa multiplié par {simple/normal:.4f} si le score normal remplace le rang simple dans la seule statistique du rang"
          f" | rapport à 1 % de témoins : rang simple {math.sqrt(101)*simple:.2f} ; score normal {math.sqrt(101)*normal:.2f}")

print()
print("== R9 (constat 9) : mondes et épisodes ==")
for k in (4, 9):
    for modes in (1, 2, 3):
        print(f"R9 K = {k} modes vus {modes} | W = {W} mondes : au moins {(1+k+modes)*W} épisodes ;"
              f" avec l'organisme au repos et le mode tenu à l'écart : {(3+k+modes)*W}")

print()
print("== R12 d (constat 12 d) : bornes des bandes à quatre décimales ==")
print(f"R12d rho1 : {math.sqrt(.5):.4f} à {math.sqrt(.75):.4f} ; rho2 : {4**-.6:.4f} à {4**-.4:.4f}")
