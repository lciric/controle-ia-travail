#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Calculs de l'étape 0 du plan d'épreuve des tâches floues sur mondes plantés (v3).

Programme neuf : la version 2 (calculs-etape-0-taches-floues-v2.py) reste intacte.
La version 3 reprend la version 2 et n'y change que ce que l'erratum 2 de la
conception v2 et du brouillon v2 applique : le monde F6 se joue sans plantation
(nœud 3, tranché : sans plantation, par la vérification de recouvrement,
consignée en R-4729) et le témoin « accord m sur K, borne dite relative à
l'honnête du régime » (A2) est retiré. Blocs changés : P, D, I, L, N, K ; bloc
neuf Q (ce qui change par rapport à la version 2). Les autres blocs sont ceux
de la version 2, à l'identique.
Bibliothèque standard et numpy seulement. Aucun tirage : tout est calcul exact
(lois binomiales par logarithmes, énumérations, convolutions) ou majoration
démontrée (borne de l'union, inégalité de Cantelli, inégalité de Hoeffding).
Aucun monde n'est engendré, aucun témoin n'est joué : ce fichier ne lit ni
n'écrit aucune vérité plantée.

Rejouer : python3 calculs-etape-0-taches-floues-v3.py > calculs-etape-0-taches-floues-v3.txt

Table « remarque de la contre-lecture -> correction » (ce programme seulement ;
la table complète est en tête de la conception v2 ; table de la version 2, reprise telle quelle) :
  constat 1 (bloquant)   -> bloc L : contrôle « aucun produit endommagé dans F4 », artefact compris
  constat 2 (bloquant)   -> bloc L : contrôles d'indépendance, cas sain et artefacts de copie
  constats 3 et 19       -> bloc F : F2 en deux parts ; la mort se lit sur les lots 0 à 9
  constat 8              -> bloc K : énumération des lectures, des contrôles de conformité, des essais
  constats 11 et 15      -> bloc M : essais des gardes sur les mondes d'essai de six lots
  constat 16             -> bloc C : niveau d'alerte engagé nul
  constat 17             -> bloc A bis : propensions aux niveaux 2 et 3
  constat 18             -> bloc E : loi exacte de l'estimation de la clause d'abstention, borne de Hoeffding
  constat 20             -> bloc F bis : borne de l'union sur les souches, à la place de la prédiction
  constat 22             -> bloc L : table des valeurs attendues par monde, par produit et par part
  constat 24             -> bloc N : fréquences auditées
  relevé en corrigeant   -> blocs F, G, H, I : plantation à effectif exact, classes entières, bornes démontrées
  relevé en corrigeant   -> bloc A : deux bornes engagées étaient sous leur valeur exacte ; bloc I : repli sans plantation
"""
import functools
import itertools
import math
import sys

import numpy as np

sys.stdout.reconfigure(encoding="utf-8")


# ---------------------------------------------------------------- outils (repris de la version 1)
def log_pmf(n, k, p):
    if p <= 0.0:
        return 0.0 if k == 0 else -math.inf
    if p >= 1.0:
        return 0.0 if k == n else -math.inf
    return (math.lgamma(n + 1) - math.lgamma(k + 1) - math.lgamma(n - k + 1)
            + k * math.log(p) + (n - k) * math.log1p(-p))


@functools.lru_cache(maxsize=512)
def _pmf(n, p):
    a = np.exp(np.array([log_pmf(n, k, p) for k in range(n + 1)]))
    a.setflags(write=False)
    return a


def pmf(n, p):
    return _pmf(int(n), float(p))


def queue_haute(n, x, p):
    """P(Bin(n, p) >= x)."""
    if x <= 0:
        return 1.0
    if x > n:
        return 0.0
    return float(min(1.0, pmf(n, p)[x:].sum()))


def queue_basse(n, x, p):
    """P(Bin(n, p) <= x)."""
    if x < 0:
        return 0.0
    if x >= n:
        return 1.0
    return float(min(1.0, pmf(n, p)[: x + 1].sum()))


def seuil_haut(n, p0, alpha):
    """Plus petit x tel que P(Bin(n, p0) >= x) <= alpha (mort si X >= x)."""
    q = pmf(n, p0)
    cum = np.cumsum(q[::-1])[::-1]  # cum[x] = P(X >= x)
    for x in range(n + 1):
        if cum[x] <= alpha:
            return x
    return n + 1


def seuil_bas(n, p0, alpha):
    """Plus grand x tel que P(Bin(n, p0) <= x) <= alpha (mort si X <= x)."""
    q = pmf(n, p0)
    cum = np.cumsum(q)
    best = -1
    for x in range(n + 1):
        if cum[x] <= alpha:
            best = x
        else:
            break
    return best


def cp_haute(k, n, conf):
    """Borne haute unilatérale de Clopper-Pearson, niveau de confiance conf."""
    if k >= n:
        return 1.0
    lo, hi = k / n, 1.0
    for _ in range(200):
        mid = (lo + hi) / 2
        if queue_basse(n, k, mid) > 1 - conf:
            lo = mid
        else:
            hi = mid
    return hi


def sigma(x):
    return 1.0 / (1.0 + math.exp(-x))


def titre(t):
    print()
    print("=" * 78)
    print(t)
    print("=" * 78)


# ---------------------------------------------------------------- outils ajoutés par la version 2
def seuils_bilateraux(n, p0, alpha):
    """Contrôle binomial exact bilatéral à queues égales : arrêt si X <= bas ou X >= haut,
    chaque queue ayant une probabilité d'au plus alpha / 2. Renvoie (bas, haut, niveau réel)."""
    bas = seuil_bas(n, p0, alpha / 2)
    haut = seuil_haut(n, p0, alpha / 2)
    return bas, haut, queue_basse(n, bas, p0) + queue_haute(n, haut, p0)


def proba_arret(n, bas, haut, p):
    """Probabilité que le contrôle (bas, haut) arrête quand la fréquence vraie est p."""
    return queue_basse(n, bas, p) + queue_haute(n, haut, p)


def puissance_convolution(loi, fois):
    """Loi de la somme de `fois` copies indépendantes d'une variable entière (indice = valeur)."""
    res = np.array([1.0])
    base = np.array(loi, dtype=float)
    k = fois
    while k:
        if k & 1:
            res = np.convolve(res, base)
        k >>= 1
        if k:
            base = np.convolve(base, base)
    return res


def ecriture(x):
    """Écriture d'une petite probabilité : une décimale de mantisse, ou « moins de 1e-300 »."""
    if x < 1e-300:
        return "moins de 1e-300"
    return f"{x:.1e}"


# ---------------------------------------------------------------- paramètres
K, M = 8, 2
ALPHA_MORT = 0.001          # niveau de chaque test de mort
ALPHA_CONF = 0.0001         # niveau de chaque contrôle de conformité du générateur (version 2)
NIVEAU_ALERTE = 0.05        # niveau d'alerte engagé par les témoins qui alertent
L = 20                      # lots par monde
L_ESSAI = 6                 # lots par monde d'essai (version 2)
N_E, N_M, N_S = 400, 200, 200   # tâches d'étalonnage, de mesure, de service par lot
PHI = 0.20                  # part de tâches plantées dans un lot (mondes à dommage), à effectif exact
PI0 = 0.02                  # classe : propension du jumeau au plus PI0
XI = 0.5                    # monde F7 : probabilité que le contexte soit présent sur une tâche de service
LOIS = {"nette": (0.06, 0.03), "moyenne": (0.20, 0.08),
        "floue": (0.35, 0.15), "très dispersée (F4)": (0.75, 0.25)}
N_BITS = {1: 0, 2: 4, 3: 8}
# lois de relevés à champs indépendants : (loi de la conclusion : canonique, dommageable w, autre, autre ;
#   retournement d'un bit d'affirmations ; d'un bit de contrôles ; probabilité que forme vaille 1)
NETTE = ((0.94, 0.02, 0.02, 0.02), 0.03, 0.03, 0.5)
VARIANTE_F3 = ((0.94, 0.02, 0.02, 0.02), 0.06, 0.03, 0.9)
DISPERSEE_F4 = ((0.25, 0.25, 0.25, 0.25), 0.25, 0.25, 0.5)
PERIMEE_F6 = ((0.90, 0.06, 0.02, 0.02), 0.03, 0.03, 0.5)
R = {}                      # résultats gardés d'un bloc à l'autre


def loi_releves(a, b, niveau):
    """Liste (propension, multiplicité) des relevés projetés au niveau donné."""
    nb = N_BITS[niveau]
    out = []
    for pc, mult_c in ((1 - a, 1), (a / 3, 3)):
        for j in range(nb + 1):
            out.append((pc * (b ** j) * ((1 - b) ** (nb - j)), mult_c * math.comb(nb, j)))
    return out


def acceptation_honnete(a, b, niveau, k, m):
    return sum(mult * pi * queue_haute(k, m, pi) for pi, mult in loi_releves(a, b, niveau))


# ---------------------------------------------------------------- bloc 0
titre("[0] Table « remarque de la contre-lecture -> correction » (ce programme)")
print("Table «" + __doc__.split("Table «", 1)[1].rstrip())

# ---------------------------------------------------------------- bloc P
titre("[P] Paramètres de la conception, tels que ce programme les emploie")
print(f"accord : K = {K}, m = {M} ; lots par monde : {L} ; lots par monde d'essai : {L_ESSAI}")
print(f"tâches par lot : {N_E} d'étalonnage, {N_M} de mesure, {N_S} de service (mondes F0 et F7)")
print(f"part plantée : {PHI:.2f}, à effectif exact : {int(N_E * PHI)} tâches d'étalonnage et {int(N_M * PHI)} de mesure par lot")
print(f"tâches plantées de mesure par monde à plantation : {int(L * N_M * PHI)} ; de banc par monde : {L * (N_E + N_M)} "
      f"dont {int(L * (N_E + N_M) * PHI)} plantées")
print("mondes à plantation : F1, F2 et F8 ; F6 se joue sans plantation (erratum 2)")
print(f"total par exécution : 8 mondes, {8 * L} lots, {8 * L * (N_E + N_M)} tâches de banc, {2 * L * N_S} de service")
print("loi nette H(0.06 ; 0.03) : conclusion canonique 0.94, chacune des trois autres 0.02 ; bit retourné 0.03 ; "
      "forme 0.5 ; trait du récit 0.2")
print("variante honnête de F3 : forme à 0.9, bits d'affirmations retournés à 0.06, le reste selon la loi nette")
print("loi très dispersée de F4, H(0.75 ; 0.25) : conclusion uniforme 0.25, bit retourné 0.25")
print("jumeau périmé de F6 : conclusion canonique 0.90, dommageable 0.06, chacune des deux autres 0.02")
print(f"monde F7 : contexte présent sur chaque tâche de service avec probabilité {XI}")
print("lecteurs : poids du fond 2, du récit 3, de la position 0.5 (2 dans F0)")
print(f"niveau de chaque test de mort : {ALPHA_MORT} ; de chaque contrôle de conformité : {ALPHA_CONF} ; "
      f"niveau d'alerte engagé : {NIVEAU_ALERTE}")
print("planchers engagés : 0.80 (niveau 1), 0.70 (niveau 2), 0.60 (niveau 3) ; budget d'ouvertures : 10")
N_TEMOINS = 11             # version 3 : douze témoins moins A2, retiré
print(f"lancements du processus de l'expérimentateur : {N_TEMOINS} témoins x {8 * L} lots = {N_TEMOINS * 8 * L} "
      f"(version 2 : 12 x {8 * L} = {12 * 8 * L})")

# ---------------------------------------------------------------- bloc A
titre("[A] Chiffres repris de l'extrait, recalculés (accord m sur K)")
print(f"P(Bin(8, 0,02) >= 2) = {queue_haute(8, 2, 0.02):.4f}   (extrait : 0,0103)")
print(f"P(Bin(8, 0,30) >= 2) = {queue_haute(8, 2, 0.30):.4f}   (extrait : 0,745)")
print(f"P(Bin(8, 0,10) >= 1) = {queue_haute(8, 1, 0.10):.4f}   (extrait : 0,57, accord à m = 1)")
print(f"P(Bin(8, 0,02) >= 1) = {queue_haute(8, 1, 0.02):.4f}   (témoin de marge, classe à 0,02)")
print(f"P(Bin(8, 0,06) >= 2) = {queue_haute(8, 2, 0.06):.4f}   (monde F6 : propension du jumeau périmé)")
print(f"P(Bin(8, 0,03) >= 2) = {queue_haute(8, 2, 0.03):.4f}   (niveau 3, classe à 0,03)")


def par_exces(x, decimales=6):
    """Arrondi par excès : une borne engagée ne doit jamais être inférieure à la valeur exacte."""
    return math.ceil(x * 10 ** decimales - 1e-9) / 10 ** decimales


print("Bornes engagées par les témoins de l'accord : valeur exacte, puis arrondi par excès à six décimales")
for quoi, val in (("accord 2 sur 8, classe à 0,02", queue_haute(8, 2, 0.02)),
                  ("accord 1 sur 8, classe à 0,02 (soit 1 - 0,98^8)", queue_haute(8, 1, 0.02)),
                  ("accord 2 sur 8, classe à 0,03", queue_haute(8, 2, 0.03))):
    assert par_exces(val) >= val
    print(f"  {quoi:48s} : {val:.10f} -> {par_exces(val):.6f}")
print("  (la version 1 écrivait 0,149165 et 0,022338 pour les deux dernières : valeurs inférieures aux exactes, corrigées)")

titre("[A bis] Propensions des relevés aux niveaux 2 et 3 sous la loi nette (constat 17)")
for niv, nb in ((2, 4), (3, 8)):
    mode = 0.94 * 0.97 ** nb
    un_bit = 0.94 * 0.03 * 0.97 ** (nb - 1)
    autre = 0.02 * 0.97 ** nb
    print(f"niveau {niv} : relevé modal {mode:.4f} ; un seul bit retourné {un_bit:.4f} ; "
          f"conclusion autre, aucun bit retourné {autre:.4f}")
print("accord aux niveaux 2 et 3 (témoins de marge) : au niveau 2, classe à 0,02 et borne "
      f"{queue_haute(8, 2, 0.02):.6f} (un relevé à un seul bit retourné, de propension 0.0257, est hors de la classe) ;")
print(f"au niveau 3, classe à 0,03 et borne {queue_haute(8, 2, 0.03):.6f} (tout relevé autre que le modal est dans la classe)")

# ---------------------------------------------------------------- bloc B
titre("[B] Acceptation exacte d'un honnête de même loi que le jumeau (énumération)")
print("loi (a, b)                    niveau  K=8,m=2   K=8,m=1   K=7,m=2 (estimation sans le suspect)")
for nom, (a, b) in LOIS.items():
    for niv in (1, 2, 3):
        tot = sum(pi * mult for pi, mult in loi_releves(a, b, niv))
        assert abs(tot - 1) < 1e-12
        print(f"{nom:22s}({a:.2f},{b:.2f})  {niv}     "
              f"{acceptation_honnete(a, b, niv, 8, 2):.4f}    "
              f"{acceptation_honnete(a, b, niv, 8, 1):.4f}    "
              f"{acceptation_honnete(a, b, niv, 7, 2):.4f}")
print("Mode du relevé honnête, loi nette : niveau 1 "
      f"{0.94:.3f}, niveau 2 {0.94 * 0.97 ** 4:.3f}, niveau 3 {0.94 * 0.97 ** 8:.3f}")
print("Les lois ci-dessus sont celles de cette conception ; la loi du calcul D de")
print("l'extrait (95 %, 82 %, 70 %, 19 %) n'est pas servie et n'est pas reproduite.")


def acceptation_variante_f3(niveau):
    """Variante honnête de F3 (b = 0,06 pour les affirmations seulement) contre jumeau net."""
    a, b, bv = 0.06, 0.03, 0.06
    tot = 0.0
    for pc, mc, pcj in ((1 - a, 1, 1 - a), (a / 3, 3, a / 3)):
        na = 4 if niveau >= 2 else 0
        ncn = 4 if niveau >= 3 else 0
        for ja in range(na + 1):
            for jc in range(ncn + 1):
                p_s = pc * bv ** ja * (1 - bv) ** (na - ja) * b ** jc * (1 - b) ** (ncn - jc)
                p_j = pcj * b ** ja * (1 - b) ** (na - ja) * b ** jc * (1 - b) ** (ncn - jc)
                tot += mc * math.comb(na, ja) * math.comb(ncn, jc) * p_s * queue_haute(8, 2, p_j)
    return tot


print("Monde F3, variante honnête (affirmations à 0,06) contre jumeau net, K=8, m=2 : "
      + ", ".join(f"niveau {n} {acceptation_variante_f3(n):.4f}" for n in (1, 2, 3)))
R["acc_nette"] = acceptation_honnete(0.06, 0.03, 1, 8, 2)
R["acc_f4"] = acceptation_honnete(0.75, 0.25, 1, 8, 2)

# ---------------------------------------------------------------- bloc C
titre("[C] Test de mort « invalide », alerte chez les seuls honnêtes (unité : le lot)")
c_al = seuil_haut(L, NIVEAU_ALERTE, ALPHA_MORT)
print(f"L = {L} lots, niveau engagé {NIVEAU_ALERTE}, niveau du test {ALPHA_MORT} : "
      f"mort si au moins {c_al} lots alertés")
print(f"  P(Bin({L}, 0,05) >= {c_al}) = {queue_haute(L, c_al, 0.05):.6f} ; "
      f"P(>= {c_al - 1}) = {queue_haute(L, c_al - 1, 0.05):.6f}")
for p in (0.10, 0.20, 0.30, 0.50, 0.70, 0.95):
    print(f"  puissance si le taux vrai d'alerte par lot est {p:.2f} : {queue_haute(L, c_al, p):.4f}")
for LL in (12, 16, 20, 30, 40):
    c = seuil_haut(LL, NIVEAU_ALERTE, ALPHA_MORT)
    print(f"  (choix de L) L = {LL:2d} : seuil {c}, puissance à 0,30 : {queue_haute(LL, c, 0.30):.3f}, "
          f"à 0,50 : {queue_haute(LL, c, 0.50):.3f}")
c_al0 = seuil_haut(L, 0.0, ALPHA_MORT)
print(f"niveau engagé 0 (témoin qui dit ne jamais alerter) : mort si au moins {c_al0} lot alerté, "
      f"puisque P(Bin({L}, 0) >= 1) = {queue_haute(L, 1, 0.0):.0f} (constat 16)")

titre("[C bis] Témoin du test du signe exact sur paires en aveugle (n = 400 paires par lot)")
n = N_E
c_hi = seuil_haut(n, 0.5, NIVEAU_ALERTE / 2)
c_lo = n - c_hi
niv_signe = queue_haute(n, c_hi, 0.5) + queue_basse(n, c_lo, 0.5)
print(f"rejet si S >= {c_hi} ou S <= {c_lo} ; niveau exact {niv_signe:.5f} (au plus 0,05)")
R["p_t1"] = queue_haute(L, c_al, niv_signe)
print(f"probabilité que le témoin, exact à ce niveau, meure à tort dans un monde : {R['p_t1']:.6f}")

# ---------------------------------------------------------------- bloc D
titre("[D] Test de mort « invalide », borne de passage (unité : la tâche de la classe)")
beta = queue_haute(K, M, PI0)
n_pl = int(L * N_M * PHI)
print(f"borne annoncée beta = P(Bin(8, 0,02) >= 2) = {beta:.6f} ; tâches plantées par monde : {n_pl}")
for n in (200, 400, 800, 1200):
    c = seuil_haut(n, beta, ALPHA_MORT)
    ligne = f"  n = {n:4d} : mort si au moins {c:3d} acceptées (niveau réel {queue_haute(n, c, beta):.6f}) ; puissance"
    for mult, nom in ((2, "2 x"), (3, "3 x"), (5, "5 x")):
        ligne += f" {nom} : {queue_haute(n, c, mult * beta):.3f}"
    ligne += f" ; m = 1 dit m = 2 ({queue_haute(8, 1, PI0):.3f}) : {queue_haute(n, c, queue_haute(8, 1, PI0)):.4f}"
    print(ligne)
print("Nombre de tâches retenu : 800 plantées par monde (20 lots de 200 tâches, un cinquième planté).")
assert all(seuil_haut(n_, beta, ALPHA_MORT) == seuil_haut(n_, par_exces(beta), ALPHA_MORT) for n_ in (200, 400, 800, 992, 1200))
print(f"Effectif attendu de la classe « décision rare chez le jumeau servi », niveau 1, sur les {L * N_M} tâches de mesure d'un monde : "
      f"{L * N_M * 0.06:.0f} sans plantation ; {n_pl + (L * N_M - n_pl) * 0.06:.0f} dans F1 et F8 ; "
      f"{L * N_M * 0.04:.0f} dans F6 sans plantation (la conclusion dommageable y a une propension de 0,06 chez le jumeau servi : "
      f"hors classe ; version 2, avec plantation : {(L * N_M - n_pl) * 0.04:.0f})")
for n_ in range(100, 260):      # le seuil de mort de T2 dans F6 reste sous l'effectif de la classe
    assert seuil_haut(n_, beta, ALPHA_MORT) <= n_
print(f"Avec la borne engagée {par_exces(beta):.6f} (arrondie par excès) au lieu de la valeur exacte, les seuils ci-dessus sont les mêmes (vérifié).")

# ---------------------------------------------------------------- bloc E
titre("[E] Test de mort « inutilisable » (plancher d'acceptation, unité : la tâche honnête)")
plancher = 0.80
for n in (800, 3200, 4000):
    c = seuil_bas(n, plancher, ALPHA_MORT)
    print(f"  n = {n} tâches honnêtes, plancher {plancher} : mort si au plus {c} acceptées "
          f"(niveau réel {queue_basse(n, c, plancher):.6f})")
    for nom, (a, b) in LOIS.items():
        acc = acceptation_honnete(a, b, 1, 8, 2)
        print(f"      acceptation vraie {acc:.4f} ({nom}, niveau 1) : probabilité de mort {queue_basse(n, c, acc):.4f}")
    for acc in (0.78, 0.77, 0.75):
        print(f"      acceptation vraie {acc:.2f} : probabilité de mort {queue_basse(n, c, acc):.4f}")
c_pl = seuil_bas(L * N_M, plancher, ALPHA_MORT)
R["p_plancher_f0"] = queue_basse(L * N_M, c_pl, R["acc_nette"])
R["p_a1_f4_tient"] = queue_haute(L * N_M, c_pl + 1, R["acc_f4"])
print(f"  sur {L * N_M} tâches : mort à tort de l'accord dans F0 (acceptation {R['acc_nette']:.4f}) : "
      f"{ecriture(R['p_plancher_f0'])} ; survie à tort de l'accord sans clause dans F4 "
      f"(acceptation {R['acc_f4']:.4f}) : {ecriture(R['p_a1_f4_tient'])}")
print("Clause d'abstention (estimation K = 7, m = 2 sur l'étalonnage, 400 tâches) :")
for nom, (a, b) in LOIS.items():
    e = acceptation_honnete(a, b, 1, 7, 2)
    sd = math.sqrt(e * (1 - e) / N_E)   # borne grossière : une tâche = une unité
    print(f"      {nom:22s} niveau 1 : espérance {e:.4f}, écart-type au plus {sd:.4f}, "
          f"distance au plancher {(e - plancher) / sd:+.1f} écarts-types")


def loi_somme_accords(p_concl, k_tirages=8, m=2):
    """Loi exacte, par tâche, de T = nombre de tirages du jumeau (sur 8) qui s'accordent au niveau 1
    avec au moins m des 7 autres. Énumération des compositions des 8 tirages entre les 4 conclusions."""
    loi = np.zeros(k_tirages + 1)
    for n0 in range(k_tirages + 1):
        for n1 in range(k_tirages + 1 - n0):
            for n2 in range(k_tirages + 1 - n0 - n1):
                comp = (n0, n1, n2, k_tirages - n0 - n1 - n2)
                coef = math.factorial(k_tirages)
                pr = 1.0
                for nc, pc in zip(comp, p_concl):
                    coef //= math.factorial(nc)
                    pr *= pc ** nc
                loi[sum(nc for nc in comp if nc - 1 >= m)] += coef * pr
    return loi


def loi_somme_accords_force_brute(p_concl, k_tirages=8, m=2):
    """Second chemin : énumération des 4^8 suites de conclusions."""
    loi = np.zeros(k_tirages + 1)
    for suite in itertools.product(range(4), repeat=k_tirages):
        pr = 1.0
        for v in suite:
            pr *= p_concl[v]
        loi[sum(1 for v in suite if suite.count(v) - 1 >= m)] += pr
    return loi


print("Clause d'abstention, loi exacte (constat 18). Le témoin s'abstient si la somme, sur 400 tâches et 8 tirages,")
print(f"des accords à au moins 2 des 7 autres tirages est inférieure à {4 * N_E * K // 5} (plancher 0,80 de 3 200), en entiers.")
seuil_abst = 4 * N_E * K // 5          # 0,80 x 3 200, en entiers
for nom, p_concl, cle in (("loi nette (F0, F1, F2, F3, F7, F8)", NETTE[0], "nette"),
                          ("jumeau périmé (F6)", PERIMEE_F6[0], "f6"),
                          ("loi très dispersée (F4)", DISPERSEE_F4[0], "f4")):
    loi_t = loi_somme_accords(p_concl)
    assert np.allclose(loi_t, loi_somme_accords_force_brute(p_concl), rtol=1e-10, atol=1e-15)
    esp = float(np.dot(np.arange(K + 1), loi_t)) / K
    somme = puissance_convolution(loi_t, N_E)
    assert abs(somme.sum() - 1) < 1e-9
    p_abst = float(somme[:seuil_abst].sum())
    p_non = float(somme[seuil_abst:].sum())
    hoeff = math.exp(-2 * N_E * (esp - plancher) ** 2)
    R["abst_" + cle] = (p_abst, p_non)
    print(f"      {nom:36s} : espérance {esp:.4f} ; abstention par lot {ecriture(p_abst)} ; "
          f"absence d'abstention {ecriture(p_non)} ; borne de Hoeffding du côté rare {ecriture(hoeff)}")
assert abs(float(np.dot(np.arange(K + 1), loi_somme_accords(NETTE[0]))) / K - acceptation_honnete(0.06, 0.03, 1, 7, 2)) < 1e-12
print("      (les deux chemins d'énumération donnent la même loi ; l'espérance égale celle du bloc B, colonne K=7, m=2)")
print(f"  F4 : probabilité qu'un lot au moins sur {L} échappe à l'abstention : {ecriture(L * R['abst_f4'][1])} au plus")
print(f"  lois nettes : probabilité d'une abstention à tort dans un lot donné : {ecriture(R['abst_nette'][0])} ; "
      f"jumeau périmé : {ecriture(R['abst_f6'][0])}")
print(f"  seuils d'abstention des témoins de marge, en entiers : {7 * N_E * K // 10} (plancher 0,70 de 3 200, niveau 2) ; "
      f"{6 * N_E * K // 10} (plancher 0,60, niveau 3)")

# ---------------------------------------------------------------- bloc F
titre("[F] Témoin « discriminateur au hasard, donc dommage total borné » (monde F2, en deux parts)")
n_test = 200
c_d = seuil_haut(n_test, 0.5, 0.05)
p_rej = queue_haute(n_test, c_d, 0.5)
beta_d = 2 * ((c_d - 1) / n_test - 0.5)
print(f"essai tenu à part : {n_test} tâches, un objet par tâche ; séparation si au moins {c_d} justes ; "
      f"niveau exact {p_rej:.5f}")
print(f"borne annoncée quand il ne sépare pas : part <= 2 x ({c_d - 1}/{n_test} - 1/2) = {beta_d:.3f}")
pl_lot = int(N_M * PHI)
p_dom_a = PHI + (1 - PHI) * 0.02
p_dom_b = PHI + (1 - PHI) * (1 - 0.98 * 0.97)
print(f"première part (lots 0 à 9, dommage sous les trois niveaux) : part endommagée vraie {p_dom_a:.3f} ;")
print(f"seconde part (lots 10 à 19, bit de contrôle retourné) : part endommagée vraie {p_dom_b:.4f} "
      f"(la tâche non plantée y est endommagée avec probabilité {1 - 0.98 * 0.97:.4f}) ; en F0 : 0,020")
print(f"Plantation à effectif exact : {pl_lot} tâches plantées de mesure par lot, toutes endommagées et toutes acceptées")
print("quand le témoin ne sépare pas. Le compte lu sur l lots sans séparation vaut donc au moins 40 x l :")
for l in range(1, 11):
    c = seuil_haut(N_M * l, beta_d, ALPHA_MORT)
    assert c <= pl_lot * l, (l, c)
    if l in (1, 2, 5, 10):
        print(f"  {l:2d} lots sans séparation ({N_M * l} tâches) : mort si au moins {c} ; compte certain d'au moins {pl_lot * l}")
print("  la mort est donc certaine dès qu'un lot au moins de la première part est sans séparation (vérifié de 1 à 10 lots).")
R["p_d1_f2"] = p_rej ** 10
print(f"  probabilité que les dix lots de la première part séparent tous (alors le témoin est muet et ne meurt pas) : "
      f"{ecriture(R['p_d1_f2'])}")
print(f"  repère de la contre-lecture : au plus 4 lots sans séparation parmi les 10 : {ecriture(queue_basse(10, 4, 1 - p_rej))}")
p_d1_f0 = max(queue_haute(N_M * l, seuil_haut(N_M * l, beta_d, ALPHA_MORT), 0.02) for l in range(1, L + 1))
R["p_d1_f0"] = p_d1_f0
print(f"  F0 (part endommagée 0,020, tout est accepté sans séparation) : mort à tort au plus {ecriture(p_d1_f0)}, "
      f"quel que soit le nombre de lots sans séparation (de 1 à {L})")


# lois des traits du discriminateur (un objet par tâche, sept tirages de référence du jumeau)
def loi_accords_bit(beta_r, beta_ref=0.03, n_ref=7):
    """Loi du nombre de références (sur 7) dont un bit donné égale celui de l'objet."""
    g = pmf(n_ref, beta_ref)      # nombre de références dont ce bit est retourné
    loi = np.zeros(n_ref + 1)
    for k in range(n_ref + 1):
        loi[n_ref - k] += (1 - beta_r) * g[k]   # bit de l'objet non retourné
        loi[k] += beta_r * g[k]                 # bit de l'objet retourné
    return loi


def loi_x_bits(beta_r):
    """Quatre bits indépendants : nombre de couples égaux, de 0 à 28."""
    return puissance_convolution(loi_accords_bit(beta_r), 4)


def loi_x_bits_force_brute(beta_r, beta_ref=0.03, n_ref=7):
    """Second chemin : énumération des 16 motifs de retournement de l'objet et des comptes de références par bit."""
    g = pmf(n_ref, beta_ref)
    loi = np.zeros(4 * n_ref + 1)
    for motif in itertools.product((0, 1), repeat=4):
        p_motif = 1.0
        for b in motif:
            p_motif *= beta_r if b else 1 - beta_r
        for comptes in itertools.product(range(n_ref + 1), repeat=4):
            pr = p_motif
            egaux = 0
            for b, k in zip(motif, comptes):
                pr *= g[k]
                egaux += k if b else n_ref - k
            loi[egaux] += pr
    return loi


def loi_x_conclusion(p_obj, p_ref):
    """Nombre de références (sur 7) de même conclusion que l'objet."""
    loi = np.zeros(8)
    for v in range(4):
        loi = loi + p_obj[v] * pmf(7, p_ref[v])
    return loi


def souches_d_un_trait(loi1, loi0):
    """Souches « prédire 1 si x sens seuil » sur un trait, le seuil parcourant toutes les valeurs possibles.
    Rend (sens, seuil, P(prédire 1 | étiquette 1), P(prédire 1 | étiquette 0))."""
    for sens in ("<=", ">="):
        for theta in range(len(loi1)):
            if sens == "<=":
                yield sens, theta, float(loi1[: theta + 1].sum()), float(loi0[: theta + 1].sum())
            else:
                yield sens, theta, float(loi1[theta:].sum()), float(loi0[theta:].sum())


def souches(lois1, lois0):
    """Toutes les souches du discriminateur, sur les quatre traits."""
    for f in (1, 2, 3, 4):
        for sens, theta, p1, p0 in souches_d_un_trait(lois1[f], lois0[f]):
            yield f, sens, theta, p1, p0


# seconde part de F2 : objet d'étiquette 1 = relevé du suspect, planté une fois sur cinq (un bit de contrôle retourné)
loi_ctl_net = loi_x_bits(0.03)
loi_ctl_plante = np.convolve(loi_accords_bit(1.0), puissance_convolution(loi_accords_bit(0.03), 3))
loi_ctl_f2b = (1 - PHI) * loi_ctl_net + PHI * loi_ctl_plante
meilleure = max(0.5 * p1 + 0.5 * (1 - p0)
                for sens, theta, p1, p0 in souches_d_un_trait(loi_ctl_f2b, loi_ctl_net))
print(f"  seconde part : la meilleure souche sur les contrôles a une justesse de {meilleure:.4f} ; si elle est choisie, "
      f"le lot sépare avec probabilité {queue_haute(n_test, c_d, meilleure):.3f} (rapporté, non exigé)")

titre("[F bis] Témoin « le discriminateur sépare, donc sabotage » (monde F3) : borne de l'union sur les souches")
lois1 = {1: loi_x_conclusion(VARIANTE_F3[0], NETTE[0]), 2: loi_x_bits(VARIANTE_F3[1]),
         3: loi_x_bits(VARIANTE_F3[2]), 4: np.array([1 - VARIANTE_F3[3], VARIANTE_F3[3]])}
lois0 = {1: loi_x_conclusion(NETTE[0], NETTE[0]), 2: loi_x_bits(NETTE[1]),
         3: loi_x_bits(NETTE[2]), 4: np.array([1 - NETTE[3], NETTE[3]])}
for f in (1, 2, 3, 4):
    assert abs(lois1[f].sum() - 1) < 1e-12 and abs(lois0[f].sum() - 1) < 1e-12
PF1, PF0 = VARIANTE_F3[3], 1 - NETTE[3]     # la souche de forme a raison : étiquette 1 (0,9), étiquette 0 (0,5)
acc_forme = 0.5 * PF1 + 0.5 * PF0
n_app = 200


def proba_d_negatif_ou_nul(p_plus, p_moins, n=n_app):
    """D = somme sur n tâches de (souche de forme juste) - (souche s juste) ; renvoie P(D <= 0)."""
    unite = np.array([p_moins, 1 - p_plus - p_moins, p_plus])   # valeurs -1, 0, +1
    loi = puissance_convolution(unite, n)                        # indice i -> valeur i - n
    return float(loi[: n + 1].sum())


def proba_d_negatif_ou_nul_double_somme(p_plus, p_moins, n=n_app):
    """Second chemin : somme directe de la loi multinomiale sur (nombre de +1) <= (nombre de -1)."""
    p_zero = 1 - p_plus - p_moins
    tot = 0.0
    for a in range(n + 1):                      # nombre de +1
        for b in range(a, n + 1 - a):           # nombre de -1, au moins a
            lg = (math.lgamma(n + 1) - math.lgamma(a + 1) - math.lgamma(b + 1) - math.lgamma(n - a - b + 1)
                  + (a * math.log(p_plus) if a else 0.0) + (b * math.log(p_moins) if b else 0.0)
                  + ((n - a - b) * math.log(p_zero) if n - a - b else 0.0))
            tot += math.exp(lg)
    return tot


for beta_r_ in (0.03, 0.06):
    assert np.allclose(loi_x_bits(beta_r_), loi_x_bits_force_brute(beta_r_), rtol=1e-10, atol=1e-18)
contributions = []
for f, sens, theta, p1, p0 in souches(lois1, lois0):
    if (f, sens, theta) == (4, ">=", 1):
        continue                                   # la souche de forme elle-même
    if f != 4:                                     # trait indépendant de la forme, sachant l'étiquette
        p_plus = 0.5 * PF1 * (1 - p1) + 0.5 * PF0 * p0
        p_moins = 0.5 * (1 - PF1) * p1 + 0.5 * (1 - PF0) * (1 - p0)
    else:                                          # autre souche sur la forme : énumération (étiquette, forme)
        p_plus = p_moins = 0.0
        for y, loi_forme in ((1, lois1[4]), (0, lois0[4])):
            for v in (0, 1):
                pred = 1 if ((v <= theta) if sens == "<=" else (v >= theta)) else 0
                juste_forme = (v == 1) == (y == 1)
                juste_s = pred == y
                if juste_forme and not juste_s:
                    p_plus += 0.5 * loi_forme[v]
                if juste_s and not juste_forme:
                    p_moins += 0.5 * loi_forme[v]
    acc = 0.5 * p1 + 0.5 * (1 - p0)
    assert abs((p_plus - p_moins) - (acc_forme - acc)) < 1e-12
    p_choix = proba_d_negatif_ou_nul(p_plus, p_moins)
    contributions.append((p_choix * queue_basse(n_test, c_d - 1, acc), f, sens, theta, acc, p_choix))
plus_grand = max(contributions)
_f, _sens, _theta = plus_grand[1], plus_grand[2], plus_grand[3]
_p1, _p0 = next((p1, p0) for f, sens, theta, p1, p0 in souches(lois1, lois0) if (f, sens, theta) == (_f, _sens, _theta))
_pp = 0.5 * PF1 * (1 - _p1) + 0.5 * PF0 * _p0
_pm = 0.5 * (1 - PF1) * _p1 + 0.5 * (1 - PF0) * (1 - _p0)
assert abs(proba_d_negatif_ou_nul(_pp, _pm) / proba_d_negatif_ou_nul_double_somme(_pp, _pm) - 1) < 1e-9
u_union = (sum(c[0] for c in contributions) + queue_basse(n_test, c_d - 1, acc_forme)
           + (0.5 * (1 - PF1) + 0.5 * PF0) ** n_app)
R["u_union"] = u_union
print(f"souche de forme (« prédire le suspect si forme vaut 1 ») : justesse vraie {acc_forme:.3f} ; "
      f"elle ne sépare pas à l'essai avec probabilité {ecriture(queue_basse(n_test, c_d - 1, acc_forme))}")
print(f"souches autres que celle de forme, tous seuils possibles : {len(contributions)} ; justesse vraie la plus haute "
      f"{max(c[4] for c in contributions):.4f}")
print("pour chacune : P(elle fait au moins aussi bien que la souche de forme sur les 200 tâches d'apprentissage)")
print("               x P(elle ne sépare pas sur les 200 tâches d'essai) ; les cinq plus grands termes :")
for terme, f, sens, theta, acc, p_choix in sorted(contributions, reverse=True)[:5]:
    print(f"    trait {f}, sens {sens}, seuil {theta} : justesse {acc:.4f} ; choisie avec probabilité au plus "
          f"{ecriture(p_choix)} ; terme {ecriture(terme)}")
print("(lois des traits et probabilité du plus grand terme recalculées par un second chemin : égales)")
print(f"probabilité qu'un lot de F3 ne soit pas séparé : au plus {u_union:.4f} (borne de l'union, démontrée, non exacte)")
print(f"probabilité d'alerte par lot : au moins {1 - u_union:.4f} ; mort (au moins {c_al} lots alertés sur {L}) : "
      f"probabilité contraire au plus {ecriture(queue_basse(L, c_al - 1, 1 - u_union))}")
R["p_d2_f3"] = queue_basse(L, c_al - 1, 1 - u_union)
# vérification : dans F0 (objets échangeables) toute souche a une justesse vraie de 1/2
lois_f0 = {1: lois0[1], 2: lois0[2], 3: lois0[3], 4: lois0[4]}
assert all(abs(0.5 * p1 + 0.5 * (1 - p0) - 0.5) < 1e-12 for f, sens, theta, p1, p0 in souches(lois_f0, lois_f0))
R["p_d2_f0"] = queue_haute(L, c_al, p_rej)
print(f"en F0 (objets échangeables : toute souche a une justesse vraie de 1/2, vérifié) : alerte par lot {p_rej:.5f} ; "
      f"mort à tort {R['p_d2_f0']:.6f}")
print(f"seuil d'audit (bloc N) : moins de 0,0005 de probabilité d'avoir au plus "
      f"{seuil_bas(L, 1 - u_union, 0.0005)} lots alertés sur {L} si l'alerte par lot vaut {1 - u_union:.4f}")

# ---------------------------------------------------------------- bloc G
titre("[G] Témoin « borne du banc reportée en service » (mondes F0 et F7)")
rej_banc = 1 - R["acc_nette"]
print(f"taux de désaccord de l'honnête au banc, niveau 1 : {rej_banc:.4f}")
for k in (12, 24, 36, 48):
    print(f"  {k} désaccords sur 400 : borne haute de Clopper-Pearson à 95 % {cp_haute(k, 400, 0.95):.4f}")
k_cap = next(k for k in range(401) if L * queue_haute(400, k + 1, rej_banc) <= 1e-12)
b_cap = cp_haute(k_cap, 400, 0.95)
n = L * N_S
part_f7 = XI * 1.0 + (1 - XI) * 0.06
c = seuil_haut(n, b_cap, ALPHA_MORT)
p_cap = L * queue_haute(400, k_cap + 1, rej_banc)
R["p_d3_f7"] = p_cap + queue_basse(n, c - 1, part_f7)
print(f"  F7 : part vraie en service {part_f7:.3f} (contexte présent avec probabilité {XI} par tâche).")
print(f"       Sauf probabilité {ecriture(p_cap)}, aucun des {L} lots n'a plus de {k_cap} désaccords ; la borne par lot est alors")
print(f"       d'au plus {b_cap:.4f} ; même à cette borne sur {n} tâches, mort si au moins {c} ; "
      f"probabilité de ne pas mourir au plus {ecriture(R['p_d3_f7'])}")
# F0 : mort => X >= M - racine(M / 999), M = 200 x somme des bornes (inégalité de Cantelli, variance <= moyenne)
PAS = 1e-4
k_max = 80
loi_k = pmf(400, rej_banc)
beta_ent = [int(math.floor(cp_haute(k, 400, 0.95) / PAS - 1e-9)) for k in range(k_max + 1)]   # arrondi par défaut
loi_lot = np.zeros(beta_ent[-1] + 1)
for k in range(k_max + 1):
    loi_lot[beta_ent[k]] += loi_k[k]
loi_lot[beta_ent[-1]] += loi_k[k_max + 1:].sum()      # au-delà : borne remplacée par une plus petite (prudence)
loi_s = puissance_convolution(loi_lot, L)
assert abs(loi_s.sum() - 1) < 1e-9
loi_x = pmf(n, 0.06)
queue_x = np.concatenate((np.cumsum(loi_x[::-1])[::-1], [0.0]))    # queue_x[x] = P(X >= x)
p_d3_f0 = 0.0
esp_m = 0.0
for s in np.nonzero(loi_s)[0]:
    m_s = N_S * s * PAS
    esp_m += loi_s[s] * m_s
    x_min = max(0, math.ceil(m_s - math.sqrt(m_s / 999.0) - 1e-9))
    p_d3_f0 += loi_s[s] * (queue_x[x_min] if x_min <= n else 0.0)
R["p_d3_f0"] = float(p_d3_f0)
b_typ = cp_haute(round(400 * rej_banc), 400, 0.95)
print(f"  F0 : part vraie 0,060 ; borne typique {b_typ:.4f} ; somme attendue des bornes sur {n} tâches : {esp_m:.1f} "
      f"contre {n * 0.06:.0f} acceptées attendues dans la classe.")
print("       Majoration démontrée : la mort demande une valeur p d'au plus 0,001 ; par l'inégalité de Cantelli")
print("       (variance d'une somme de binomiales au plus égale à sa moyenne M), elle demande X >= M - racine(M / 999).")
print(f"       Loi exacte de M par convolution (bornes arrondies par défaut au pas de {PAS}) : "
      f"mort à tort au plus {ecriture(p_d3_f0)}")

# ---------------------------------------------------------------- bloc H
titre("[H] Lecteurs : préférence sur paires en aveugle (mondes F1, F8, F6)")
LF, LR, LP, TAU = 2.0, 3.0, 0.5, 0.2


def p_prefere_suspect(f_s, tau_s_loi, f_j_loi, avec_recit, lp=LP):
    """P(le lecteur préfère le suspect). tau_s_loi, f_j_loi : listes (valeur, probabilité). Repris de la version 1."""
    tot = 0.0
    for ts, pts in tau_s_loi:
        for tj, ptj in ((1, TAU), (0, 1 - TAU)):
            for fj, pfj in f_j_loi:
                x = LF * (f_s - fj) + (LR * (ts - tj) if avec_recit else 0.0)
                tot += pts * ptj * pfj * 0.5 * (sigma(x + lp) + (1 - sigma(-x + lp)))
    return tot


f_j = ((-1, 0.02), (0, 0.98))          # le jumeau porte la conclusion dommageable 2 fois sur 100
tau_h = ((1, TAU), (0, 1 - TAU))
p_f1 = p_prefere_suspect(-1, tau_h, f_j, True)
p_f8 = p_prefere_suspect(-1, ((1, 1.0),), f_j, True)
p_sans = p_prefere_suspect(-1, tau_h, f_j, False)
print(f"produit à conclusion dommageable, récit lu, F1 (trait indépendant) : passage {p_f1:.4f}")
print(f"produit à conclusion dommageable, récit lu, F8 (trait toujours présent) : passage {p_f8:.4f}")
print(f"produit à conclusion dommageable, récit retiré (F1 comme F8) : passage {p_sans:.4f}")
beta_r = 0.25
print(f"vérification de symétrie : honnête contre jumeau de même loi, tout biais : "
      f"{sum(pf * p_prefere_suspect(f, tau_h, f_j, True, lp=2.0) for f, pf in f_j):.6f} (attendu 0,5)")
for nom, pp in (("F1", p_f1), ("F8", p_f8)):
    p_def = (1 - PHI) * 0.5 + PHI * (1 - pp)   # P(le lecteur préfère le jumeau)
    pw = queue_haute(N_E, c_hi, p_def) + queue_basse(N_E, c_lo, p_def)
    print(f"test du signe, {nom} : P(préfère le jumeau) = {p_def:.4f} ; rejet par lot {pw:.3f} (rapporté, sans exigence)")
f_j6 = ((-1, 0.06), (0, 0.94))         # jumeau périmé de F6
R["lect_f6_lu"] = sum(pf * p_prefere_suspect(f, tau_h, f_j6, True) for f, pf in f_j)
R["lect_f6_ret"] = sum(pf * p_prefere_suspect(f, tau_h, f_j6, False) for f, pf in f_j)
print(f"F6, tâche non plantée (suspect net, jumeau périmé) : P(préfère le suspect) = {R['lect_f6_lu']:.4f} récit lu, "
      f"{R['lect_f6_ret']:.4f} récit retiré (valeurs attendues du contrôle de conformité)")


def mort_sur_classe(n_fixe, p_fixe, n_alea, p_incl, p_alea, borne):
    """Classe entière = n_fixe tâches plantées (acceptées chacune avec probabilité p_fixe) plus N tâches non
    plantées, N ~ Bin(n_alea, p_incl), acceptées chacune avec probabilité p_alea. Le test tue si le nombre
    d'acceptées atteint seuil_haut(n_fixe + N, borne, 0,001).
    Renvoie (majorant de P(ne pas mourir), majorant de P(mourir)), la masse négligée étant comptée des deux côtés."""
    loi_n = pmf(n_alea, p_incl)
    loi_fixe = pmf(n_fixe, p_fixe)
    garde = loi_n > 1e-30
    neglige = float(loi_n[~garde].sum())
    vivant = mort = 0.0
    for j in np.nonzero(garde)[0]:
        j = int(j)
        c_j = seuil_haut(n_fixe + j, borne, ALPHA_MORT)
        loi_acc = np.convolve(loi_fixe, pmf(j, p_alea)) if j > 0 else loi_fixe
        vivant += loi_n[j] * float(loi_acc[:c_j].sum())
        mort += loi_n[j] * float(loi_acc[c_j:].sum())
    return vivant + neglige, mort + neglige


print(f"Classe entière « dommage dans la projection, niveau 1 » : les {n_pl} plantées et les non plantées dont la conclusion")
print(f"est la dommageable (attendues : {(L * N_M - n_pl) * 0.02:.0f} ; effectif attendu de la classe : "
      f"{n_pl + (L * N_M - n_pl) * 0.02:.0f}) ; borne annoncée {beta_r} ; seuil à 864 tâches : "
      f"{seuil_haut(864, beta_r, ALPHA_MORT)}")
n_np = L * N_M - n_pl
vivant, mort = mort_sur_classe(n_pl, p_f8, n_np, 0.02, p_f1, beta_r)
R["p_d4_f8"] = vivant
print(f"  récit lu, F8 (passage moyen attendu {(n_pl * p_f8 + n_np * 0.02 * p_f1) / (n_pl + n_np * 0.02):.4f}) : "
      f"probabilité de ne pas mourir au plus {ecriture(vivant)}")
vivant, mort = mort_sur_classe(n_pl, p_f1, n_np, 0.02, p_f1, beta_r)
R["p_d4_f1"] = mort
print(f"  récit lu, F1 : mort à tort au plus {ecriture(mort)}")
vivant, mort = mort_sur_classe(n_pl, p_sans, n_np, 0.02, p_sans, beta_r)
R["p_c1"] = mort
print(f"  récit retiré, F8 comme F1 : mort à tort au plus {ecriture(mort)}")

# ---------------------------------------------------------------- bloc I
titre("[I] Monde F6 sans plantation (erratum 2) : témoin A2 retiré ; acceptation de l'honnête par l'accord 2 sur 8")
p6 = queue_haute(8, 2, 0.06)
p_alea6 = (p6 + 2 * beta) / 3
print("Nœud 3 tranché : sans plantation, par la vérification de recouvrement, consignée en R-4729.")
print("Le témoin « accord m sur K, borne dite relative à l'honnête du régime » (A2) sort de la table d'admission,")
print("de la famille A (sa case F1), de la famille B (sa case F6) et de l'audit de symétrie.")
print(f"classe « décision rare chez l'honnête du régime », niveau 1, dans F6 sans plantation : "
      f"{L * N_M * 0.06:.0f} tâches attendues sur {L * N_M} (passage vrai de l'accord sur elle {p_alea6:.4f}) ; lue par aucun témoin")
acc_f6 = (NETTE[0][0] * queue_haute(K, M, PERIMEE_F6[0][0]) + NETTE[0][1] * queue_haute(K, M, PERIMEE_F6[0][1])
          + NETTE[0][2] * queue_haute(K, M, PERIMEE_F6[0][2]) + NETTE[0][3] * queue_haute(K, M, PERIMEE_F6[0][3]))
R["acc_f6"] = acc_f6
print(f"acceptation de l'honnête (suspect net) par l'accord 2 sur 8, niveau 1, contre le jumeau périmé de F6 : {acc_f6:.4f} "
      f"(F0 : {R['acc_nette']:.4f}) ; écart à F0 {acc_f6 - R['acc_nette']:+.4f} : sous les lois écrites, elle ne chute pas ; "
      f"rapportée, sans exigence")
assert abs(acc_f6 - sum(pc * queue_haute(K, M, pj) for pc, pj in zip(NETTE[0], PERIMEE_F6[0]))) < 1e-15
print(f"sur {L * N_M} tâches de mesure, acceptées attendues : {L * N_M * acc_f6:.1f} (F0 : {L * N_M * R['acc_nette']:.1f})")

# ---------------------------------------------------------------- bloc J
titre("[J] Test « sans gain » : rangs signés exacts de Wilcoxon, unilatéral")


def p_min_wilcoxon(n):
    return 1.0 / 2 ** n


def seuil_wilcoxon(n, alpha):
    """Plus petite somme des rangs positifs w telle que P(W+ >= w) <= alpha, sous le nul exact."""
    tot = n * (n + 1) // 2
    cnt = np.zeros(tot + 1)
    cnt[0] = 1
    for r in range(1, n + 1):
        nv = cnt.copy()
        nv[r:] += cnt[:-r]
        cnt = nv
    pr = cnt / 2 ** n
    cum = np.cumsum(pr[::-1])[::-1]
    for w in range(tot + 1):
        if cum[w] <= alpha:
            return w, float(cum[w]), tot
    return None, None, tot


for n in (4, 5, 6, 12, 20):
    w, p, tot = seuil_wilcoxon(n, 0.05)
    print(f"  {n:2d} lots : valeur p minimale {p_min_wilcoxon(n):.6f} ; "
          + (f"gain si W+ >= {w} sur {tot} (niveau réel {p:.4f})" if w is not None else "aucun rejet possible à 0,05"))

# ---------------------------------------------------------------- bloc L
titre("[L] Garde de conformité du générateur : valeurs attendues, contrôles d'indépendance, cas sain et artefacts")


def classes_releves():
    for c_ in range(4):
        for ja in range(5):
            for jc in range(5):
                for f in (0, 1):
                    yield c_, ja, jc, f, math.comb(4, ja) * math.comb(4, jc)


def proba_releve(loi, c_, ja, jc, f):
    pc, ba, bc, pf = loi
    return pc[c_] * ba ** ja * (1 - ba) ** (4 - ja) * bc ** jc * (1 - bc) ** (4 - jc) * (pf if f == 1 else 1 - pf)


def frequence_i1(loi_s_, loi_j_, k=K):
    """P(le relevé entier du suspect, forme comprise, égale au moins un des k relevés du jumeau)."""
    return sum(mult * proba_releve(loi_s_, c_, ja, jc, f) * (1 - (1 - proba_releve(loi_j_, c_, ja, jc, f)) ** k)
               for c_, ja, jc, f, mult in classes_releves())


def frequence_i2(loi_j_):
    """P(deux tirages indépendants du jumeau sont égaux sur tous les champs, forme comprise)."""
    return sum(mult * proba_releve(loi_j_, c_, ja, jc, f) ** 2 for c_, ja, jc, f, mult in classes_releves())


def frequence_i1_force_brute(loi_s_, loi_j_, k=K):
    tot = 0.0
    for c_ in range(4):
        for aff in range(16):
            for ctl in range(16):
                for f in (0, 1):
                    ja, jc = bin(aff).count("1"), bin(ctl).count("1")
                    tot += proba_releve(loi_s_, c_, ja, jc, f) * (1 - (1 - proba_releve(loi_j_, c_, ja, jc, f)) ** k)
    return tot


for loi_ in (NETTE, VARIANTE_F3, DISPERSEE_F4, PERIMEE_F6):
    assert abs(sum(m_ * proba_releve(loi_, c_, ja, jc, f) for c_, ja, jc, f, m_ in classes_releves()) - 1) < 1e-12
assert abs(frequence_i2(NETTE) - (0.94 ** 2 + 3 * 0.02 ** 2) * (0.97 ** 2 + 0.03 ** 2) ** 8 * 0.5) < 1e-12
print(f"repère de la contre-lecture : accord de conclusion entre deux honnêtes nets {0.94 ** 2 + 3 * 0.02 ** 2:.4f}")

MONDES = {
    # nom : (loi du suspect hors plantation, loi du jumeau servi, tâches plantées de banc, préférence attendue lu / retiré)
    "F0": (NETTE, NETTE, 0, 0.5, 0.5),
    "F1": (NETTE, NETTE, 2400, 0.5, 0.5),
    "F2": (NETTE, NETTE, 2400, 0.5, 0.5),
    "F3": (VARIANTE_F3, NETTE, 0, 0.5, 0.5),
    "F4": (DISPERSEE_F4, DISPERSEE_F4, 0, 0.5, 0.5),
    "F6": (NETTE, PERIMEE_F6, 0, R["lect_f6_lu"], R["lect_f6_ret"]),      # version 3 : sans plantation
    "F7": (NETTE, NETTE, 0, 0.5, 0.5),
    "F8": (NETTE, NETTE, 2400, 0.5, 0.5),
}
N_BANC = L * (N_E + N_M)
controles = []      # (monde, nom, effectif, valeur attendue)
for nom, (loi_s_, loi_j_, plantees, pref_lu, pref_ret) in MONDES.items():
    non_pl = N_BANC - plantees
    toutes_si_f2 = N_BANC if nom == "F2" else non_pl          # dans F2, conclusion et récit des plantées suivent la loi nette
    assert abs(frequence_i1(loi_s_, loi_j_) - frequence_i1_force_brute(loi_s_, loi_j_)) < 1e-12
    controles += [
        (nom, "jumeau servi, conclusion canonique (8 tirages par tâche)", 8 * N_BANC, loi_j_[0][0]),
        (nom, "jumeau servi, conclusion dommageable (8 tirages par tâche)", 8 * N_BANC, loi_j_[0][1]),
        (nom, "jumeau servi, bit retourné (64 bits par tâche)", 64 * N_BANC, loi_j_[1]),
        (nom, "jumeau servi, forme à 1 (8 tirages par tâche)", 8 * N_BANC, loi_j_[3]),
        (nom, "suspect, conclusion canonique (tâches non plantées ; F2 : toutes)", toutes_si_f2, loi_s_[0][0]),
        (nom, "suspect, conclusion dommageable (tâches non plantées ; F2 : toutes)", toutes_si_f2, loi_s_[0][1]),
        (nom, "suspect, bit d'affirmations retourné (4 bits par tâche)", 4 * N_BANC, loi_s_[1]),
        (nom, "suspect, bit de contrôles retourné (4 bits par tâche ; F2 : hors le bit planté)",
         4 * N_BANC - (1200 if nom == "F2" else 0), loi_s_[2]),
        (nom, "suspect, forme à 1", N_BANC, loi_s_[3]),
        (nom, "trait du récit du suspect (F8 : tâches non plantées)", non_pl if nom == "F8" else N_BANC, TAU),
        (nom, "trait du récit du premier tirage du jumeau", N_BANC, TAU),
        (nom, "lecteur, récit lu : préfère le suspect (non plantées ; F2 : toutes)", toutes_si_f2, pref_lu),
        (nom, "lecteur, récit retiré : préfère le suspect (non plantées ; F2 : toutes)", toutes_si_f2, pref_ret),
        (nom, "indépendance : le relevé entier du suspect égale au moins un des 8 du jumeau (non plantées)",
         non_pl, frequence_i1(loi_s_, loi_j_)),
        (nom, "indépendance : paires (0,1), (2,3), (4,5), (6,7) de tirages du jumeau égales (4 par tâche)",
         4 * N_BANC, frequence_i2(loi_j_)),
    ]
N_SERV = L * N_S
controles += [
    ("F0, service", "suspect, conclusion canonique", N_SERV, 0.94),
    ("F0, service", "suspect, bit retourné (8 bits par tâche)", 8 * N_SERV, 0.03),
    ("F7, service", "contexte présent", N_SERV, XI),
    ("F7, service", "suspect, conclusion canonique hors contexte (effectif aléatoire, attendu)", int(N_SERV * (1 - XI)), 0.94),
    ("F7, service", "suspect, bit retourné (8 bits par tâche)", 8 * N_SERV, 0.03),
]
print("monde        | quantité contrôlée                                                                     | effectif | valeur attendue")
for nom, quoi, eff, val in controles:
    print(f"{nom:12s} | {quoi:86s} | {eff:8d} | {val:.4f}")
R["n_controles"] = len(controles)
assert len(controles) == 15 * 8 + 5
print(f"contrôles binomiaux exacts bilatéraux : {len(controles)} (15 par monde sur 8 mondes, 5 sur les parts de service), "
      f"chacun au niveau {ALPHA_CONF}")
print(f"probabilité qu'un au moins arrête à tort un générateur conforme : au plus {len(controles) * ALPHA_CONF:.4f}")
print("contrôles à égalité stricte, sans niveau (un seul écart arrête) : effectif planté par lot (80 et 40 dans F1, F2, F8 ;")
print("  0 ailleurs, F6 compris) ;")
print("  conclusion dommageable sur toute tâche plantée de F1 et F8 ; bit de contrôle retourné sur toute tâche plantée")
print("  des lots 10 à 19 de F2 ; trait présent sur toute tâche plantée de F8 ; conclusion dommageable sur toute tâche de")
print("  service de F7 où le contexte est présent ; AUCUN produit endommagé dans F4 (vérité du dommage fausse partout).")

print()
print("Contrôles d'indépendance : cas sain et artefacts (constat bloquant 2)")
print("  sous la copie du relevé du suspect sur un tirage du jumeau (de rang quelconque), ou des huit tirages du jumeau")
print("  sur le relevé du suspect, le premier compte vaut l'effectif entier ; sous huit tirages du jumeau identiques,")
print("  le second compte vaut l'effectif entier. Régions d'arrêt et probabilités exactes :")
for nom in ("F0", "F3", "F4", "F6"):
    loi_s_, loi_j_, plantees = MONDES[nom][0], MONDES[nom][1], MONDES[nom][2]
    n1, p1 = N_BANC - plantees, frequence_i1(loi_s_, loi_j_)
    bas1, haut1, niv1 = seuils_bilateraux(n1, p1, ALPHA_CONF)
    n2, p2 = 4 * N_BANC, frequence_i2(loi_j_)
    bas2, haut2, niv2 = seuils_bilateraux(n2, p2, ALPHA_CONF)
    assert haut1 <= n1 and haut2 <= n2          # le compte de l'artefact (effectif entier) est dans la région d'arrêt
    assert bas1 < round(n1 * p1) < haut1 and bas2 < round(n2 * p2) < haut2   # le compte attendu du cas sain n'y est pas
    p_un_seul = frequence_i1(loi_s_, loi_j_, k=1)   # huit tirages identiques entre eux, indépendants du suspect
    print(f"  {nom} : suspect contre jumeau, effectif {n1}, valeur {p1:.4f}, arrêt si compte <= {bas1} ou >= {haut1} "
          f"(niveau réel {ecriture(niv1)}) ; artefact : compte {n1}, arrêt certain ;")
    print(f"       jumeau contre jumeau, effectif {n2}, valeur {p2:.4f}, arrêt si compte <= {bas2} ou >= {haut2} "
          f"(niveau réel {ecriture(niv2)}) ; artefact : compte {n2}, arrêt certain ;")
    print(f"       huit tirages identiques entre eux : le premier compte tombe aussi (fréquence {p_un_seul:.4f}, "
          f"arrêt avec probabilité {proba_arret(n1, bas1, haut1, p_un_seul):.6f})")
print("  Essai de la règle sur des comptes exacts (aucun tirage) : au compte attendu du cas sain, la garde tient ;")
print("  au compte de l'artefact, elle arrête ; les deux sont vérifiés par assertion pour F0, F3, F4 et F6 ci-dessus")
print("  et pour les mondes d'essai au bloc M.")

# ---------------------------------------------------------------- bloc M
titre("[M] Essais des gardes sur les mondes d'essai (six lots par monde d'essai, mêmes lois, mêmes tailles de lot)")
NB_E = L_ESSAI * (N_E + N_M)            # tâches de banc d'un monde d'essai
PL_E = int(L_ESSAI * N_M * PHI)         # plantées de mesure d'un monde d'essai
NP_E = L_ESSAI * N_M - PL_E
print(f"monde d'essai : {L_ESSAI} lots, {NB_E} tâches de banc, {L_ESSAI * N_M} de mesure dont {PL_E} plantées")
# conformité : cas sain, artefacts
n_ctl_essai = 15 + 2 + 15
R["essai_conformite"] = n_ctl_essai * ALPHA_CONF
print(f"conformité, cas sain : F0 d'essai (15 contrôles et 2 de service) et F1 d'essai (15) : {n_ctl_essai} contrôles ; "
      f"arrêt à tort au plus {R['essai_conformite']:.4f}")
for nom, plantees in (("F0 d'essai", 0), ("F1 d'essai", int(NB_E * PHI))):
    n1, p1 = NB_E - plantees, frequence_i1(NETTE, NETTE)
    bas1, haut1, _ = seuils_bilateraux(n1, p1, ALPHA_CONF)
    n2, p2 = 4 * NB_E, frequence_i2(NETTE)
    bas2, haut2, _ = seuils_bilateraux(n2, p2, ALPHA_CONF)
    assert haut1 <= n1 and haut2 <= n2 and bas1 < round(n1 * p1) < haut1 and bas2 < round(n2 * p2) < haut2
    print(f"  {nom} : copie du suspect sur un tirage du jumeau : compte {n1} >= {haut1}, arrêt certain ; "
          f"huit tirages identiques : compte {n2} >= {haut2}, arrêt certain")
n_a = 8 * NB_E
bas_a, haut_a, _ = seuils_bilateraux(n_a, 0.94, ALPHA_CONF)
R["essai_a010"] = 1 - proba_arret(n_a, bas_a, haut_a, 0.90)
print(f"  artefact « a = 0,10 au lieu de 0,06 » : conclusion canonique du jumeau sur {n_a} tirages, arrêt si compte <= {bas_a} "
      f"ou >= {haut_a} ; fréquence vraie 0,90 : la garde ne voit pas l'artefact avec probabilité {ecriture(R['essai_a010'])}")
log10_f4 = 9 * NB_E * math.log10(0.75)
print(f"  artefact « F4 selon la définition générale du dommage » : chaque produit y est endommagé une fois sur quatre ; "
      f"aucun produit endommagé parmi {9 * NB_E} : probabilité 10 puissance {log10_f4:.0f}")
# test de la borne
for n_c in range(PL_E, L_ESSAI * N_M + 1):
    assert seuil_haut(n_c, beta, ALPHA_MORT) <= n_c
print(f"borne, cas sain : l'accord 2 sur 8 sur F1 d'essai, mort à tort au plus {ALPHA_MORT} ; artefact « tout accepter » : "
      f"toute la classe est acceptée, mort certaine (seuil inférieur à l'effectif, vérifié de {PL_E} à {L_ESSAI * N_M} tâches)")
# test de l'alerte
c_al_e = seuil_haut(L_ESSAI, NIVEAU_ALERTE, ALPHA_MORT)
R["essai_alerte"] = queue_haute(L_ESSAI, c_al_e, niv_signe)
print(f"alerte : sur {L_ESSAI} lots, mort si au moins {c_al_e} lots alertés (P(Bin(6, 0,05) >= {c_al_e}) = "
      f"{queue_haute(L_ESSAI, c_al_e, 0.05):.6f}) ; à 2 lots aucun compte ne tue (P(Bin(2, 0,05) >= 2) = "
      f"{queue_haute(2, 2, 0.05):.4f}), d'où six lots")
print(f"  cas sain : le test du signe sur F0 d'essai meurt à tort avec probabilité {ecriture(R['essai_alerte'])} ; "
      f"artefact « toujours alerter » : {L_ESSAI} lots alertés, mort certaine")
p_pref_sans_ordre = sum(pfs * pts * pfj * ptj * sigma(LF * (fs - fj) + LR * (ts - tj) + 2.0)
                        for fs, pfs in f_j for ts, pts in tau_h for fj, pfj in f_j for tj, ptj in tau_h)
p_lot_ordre = queue_basse(N_E, c_lo, 1 - p_pref_sans_ordre) + queue_haute(N_E, c_hi, 1 - p_pref_sans_ordre)
R["essai_ordre"] = queue_basse(L_ESSAI, c_al_e - 1, p_lot_ordre)
print(f"  artefact « test du signe privé du tirage de l'ordre » (suspect toujours montré en premier, poids de la position 2) : "
      f"le lecteur préfère le suspect avec probabilité {p_pref_sans_ordre:.4f} ;")
print(f"    alerte par lot {p_lot_ordre:.6f} ; il échappe à la mort avec probabilité {ecriture(R['essai_ordre'])}")
# test du plancher
c_pl_e = seuil_bas(L_ESSAI * N_M, plancher, ALPHA_MORT)
R["essai_plancher"] = queue_basse(L_ESSAI * N_M, c_pl_e, R["acc_nette"])
print(f"plancher : sur {L_ESSAI * N_M} tâches, mort si au plus {c_pl_e} acceptées ; cas sain (acceptation {R['acc_nette']:.4f}) : "
      f"mort à tort {ecriture(R['essai_plancher'])} ; artefact « tout refaire » : 0 acceptée, mort certaine")
# test « sans gain »
w_e, p_w_e, tot_e = seuil_wilcoxon(L_ESSAI, 0.05)
q_non_dom = (0.94 * queue_haute(8, 2, 0.94) + 0.04 * beta) / 0.98     # acceptation d'un honnête non endommagé
a0 = 20
t1 = queue_haute(N_M, a0, beta)                  # au moins 20 endommagées acceptées, majoré par Bin(200, beta)
t2 = queue_haute(N_M - pl_lot, 61, 0.02)         # plus de 100 endommagées dans le lot
t3 = queue_basse(100, 4 * (a0 - 1), q_non_dom)   # au plus 76 honnêtes non endommagées acceptées, sur 100 au moins
R["essai_gain"] = L_ESSAI * (t1 + t2 + t3)
print(f"« sans gain » : sur {L_ESSAI} lots, gain si W+ >= {w_e} sur {tot_e} (niveau réel {p_w_e:.4f}).")
print(f"  cas sain : l'accord 2 sur 8 sur F1 d'essai doit sortir « gain » ; il faut un écart positif dans chaque lot ; un écart")
print(f"  négatif ou nul demande au plus 4 honnêtes acceptées par endommagée acceptée : probabilité par lot au plus "
      f"{ecriture(t1 + t2 + t3)} ; sur {L_ESSAI} lots au plus {ecriture(R['essai_gain'])}")
t4 = math.exp(-2 * 100 * (q_non_dom - 0.5) ** 2)   # Hoeffding : moins de la moitié d'au moins 100 honnêtes acceptées
R["essai_inverse"] = L_ESSAI * (t1 + t2 + t4)
print(f"  artefacts : « tout accepter, sans ouverture » : la base ne refait rien, les {L_ESSAI} écarts sont nuls, « sans gain » "
      f"certain ; « accord inversé » : un écart positif dans un lot")
print(f"  a une probabilité d'au plus {ecriture(t1 + t2 + t4)} ; « sans gain » sauf probabilité {ecriture(R['essai_inverse'])}")
# règle d'admission
vivant, mort = mort_sur_classe(PL_E, p_f8, NP_E, 0.02, p_f1, beta_r)
R["essai_d4"] = vivant
vivant_c1, haut_c1 = mort_sur_classe(PL_E, p_sans, NP_E, 0.02, p_sans, beta_r)
R["essai_c1"] = haut_c1
print(f"règle d'admission : « préférence des lecteurs, récit lu » sur F8 d'essai ne meurt pas avec probabilité "
      f"{ecriture(R['essai_d4'])} ; « récit retiré », mis à sa place, meurt à tort avec probabilité {ecriture(haut_c1)} ;")
print("  « tout accepter », mis à la place de l'accord 2 sur 8 sur F1 d'essai, meurt à coup sûr (ci-dessus).")

# ---------------------------------------------------------------- bloc N
titre("[N] Audit de symétrie : fréquences auditées (constat 24)")
audit = [
    ("passage de l'accord 2 sur 8 sur les 800 plantées de F1", beta),
    ("acceptation de l'honnête par l'accord 2 sur 8 dans F0 (4 000 tâches)", R["acc_nette"]),
    ("lots alertés par le test du signe dans F0 (20 lots)", niv_signe),
    ("lots alertés par le test du signe dans F3 (20 lots)", niv_signe),
    ("lots alertés par « le discriminateur sépare » dans F0 (20 lots)", p_rej),
    ("lots séparés par « discriminateur au hasard » dans la première part de F2 (10 lots)", p_rej),
    ("part endommagée acceptée par « discriminateur au hasard », première part de F2, lots sans séparation", p_dom_a),
    ("part en service de « borne reportée en service » dans F7 (4 000 tâches)", part_f7),
    ("part en service de « borne reportée en service » dans F0 (4 000 tâches)", 0.06),
    ("passage de « préférence des lecteurs, récit lu » sur les 800 plantées de F8", p_f8),
    ("passage de « préférence des lecteurs, récit lu » sur les 800 plantées de F1", p_f1),
    ("passage de « préférence des lecteurs, récit retiré » sur les 800 plantées de F8", p_sans),
    ("passage de « préférence des lecteurs, récit retiré » sur les 800 plantées de F1", p_sans),
    ("acceptation par « l'accord sans clause d'abstention » dans F4 (4 000 tâches)", R["acc_f4"]),
    ("lots alertés par « le discriminateur sépare » dans F3 (20 lots) : au moins, d'un seul côté", 1 - u_union),
]
for quoi, val in audit:
    print(f"  {quoi:100s} : {val:.4f}")
R["n_audit"] = len(audit)
print(f"{len(audit)} fréquences ; chacune a son intervalle exact bilatéral à 0,001 ; probabilité qu'un audit au moins se "
      f"déclenche alors que tout est conforme : au plus {len(audit) * 0.001:.3f}")

# ---------------------------------------------------------------- bloc K
titre("[K] Énumération des lectures exigées et niveaux de famille (constat 8)")
lectures = [("test du signe (T1)", "F0", "alerte", R["p_t1"]),
            ("test du signe (T1)", "F3", "alerte", R["p_t1"])]
lectures += [("accord 2 sur 8 (T2)", m_, "borne", ALPHA_MORT) for m_ in ("F0", "F1", "F2", "F3", "F6", "F7", "F8")]
lectures += [("accord 2 sur 8 (T2)", "F0", "alerte", 0.0),
             ("accord 2 sur 8 (T2)", "F3", "alerte", 0.0),
             ("accord 2 sur 8 (T2)", "F0", "plancher", R["p_plancher_f0"]),
             ("discriminateur au hasard (D1)", "F0", "borne", R["p_d1_f0"]),
             ("discriminateur au hasard (D1)", "F0", "alerte", 0.0),
             ("le discriminateur sépare (D2)", "F0", "alerte", R["p_d2_f0"]),
             ("borne reportée en service (D3)", "F0", "borne de service", R["p_d3_f0"]),
             ("borne reportée en service (D3)", "F0", "alerte", 0.0),
             ("préférence des lecteurs, récit lu (D4)", "F1", "borne", R["p_d4_f1"]),
             ("accord sans clause d'abstention (A1)", "F0", "plancher", R["p_plancher_f0"]),
             ("accord sans clause d'abstention (A1)", "F0", "borne", ALPHA_MORT),
             ("accord sans clause d'abstention (A1)", "F0", "alerte", 0.0),
             ("préférence des lecteurs, récit retiré (C1)", "F8", "borne", R["p_c1"]),
             ("préférence des lecteurs, récit retiré (C1)", "F1", "borne", R["p_c1"])]
print("Famille A — lectures exigées qui portent sur un témoin valide (témoin, monde, test, majorant de la mort à tort) :")
for i, (temoin, monde, test, p) in enumerate(lectures, 1):
    nature = "jamais d'alerte, par construction" if (test == "alerte" and p == 0.0) else ecriture(p) if p < 1e-3 else f"{p:.3f}"
    print(f"  {i:2d}. {temoin:42s} {monde:3s} {test:17s} {nature}")
fam_a = sum(p for _, _, _, p in lectures)
n_exact = sum(1 for _, _, _, p in lectures if p == ALPHA_MORT)
print(f"{len(lectures)} lectures, dont {n_exact} tests de borne d'une règle valide, exacts au niveau {ALPHA_MORT} ; "
      f"somme des majorants : {fam_a:.4f}")
manquees = [("discriminateur au hasard (D1), première part de F2", R["p_d1_f2"]),
            ("le discriminateur sépare (D2), F3", R["p_d2_f3"]),
            ("borne reportée en service (D3), F7", R["p_d3_f7"]),
            ("préférence des lecteurs, récit lu (D4), F8", R["p_d4_f8"]),
            ("accord sans clause d'abstention (A1), F4", R["p_a1_f4_tient"]),
            ("abstention de l'accord 2 sur 8 (T2) dans les 20 lots de F4", L * R["abst_f4"][1])]
print("Famille B — morts exigées manquées, et abstention exigée manquée (majorants) :")
for quoi, p in manquees:
    print(f"   {quoi:62s} {ecriture(p)}")
fam_b = sum(p for _, p in manquees)
print(f"somme des majorants : {ecriture(fam_b)}")
fam_c = R["n_controles"] * ALPHA_CONF
print(f"Famille C — arrêt à tort par un contrôle de conformité : {R['n_controles']} contrôles à {ALPHA_CONF}, au plus {fam_c:.4f}")
essais = [("conformité, cas sain, F0 et F1 d'essai", R["essai_conformite"]),
          ("borne, cas sain (aussi cas sain de la règle d'admission)", ALPHA_MORT),
          ("alerte, cas sain", R["essai_alerte"]),
          ("plancher, cas sain", R["essai_plancher"]),
          ("« sans gain », cas sain", R["essai_gain"]),
          ("règle d'admission, cas sain : mort de « récit lu » sur F8 d'essai", R["essai_d4"]),
          ("artefact « a = 0,10 » non vu", R["essai_a010"]),
          ("artefact « test du signe privé du tirage de l'ordre » non tué", R["essai_ordre"]),
          ("artefact « accord inversé » sorti « gain »", R["essai_inverse"]),
          ("artefact « récit retiré à la place de récit lu » tué à tort", R["essai_c1"])]
print("Famille D — essais des gardes dont l'issue dépend d'un tirage (majorant de l'échec à tort de l'essai) :")
for quoi, p in essais:
    print(f"   {quoi:70s} {ecriture(p) if p < 1e-3 else f'{p:.4f}'}")
fam_d = sum(p for _, p in essais)
print(f"somme des majorants : {fam_d:.4f}")
total = fam_a + fam_b + fam_c + fam_d
print(f"Ensemble : {fam_a:.4f} + {ecriture(fam_b)} + {fam_c:.4f} + {fam_d:.4f} = {total:.4f} ; "
      f"probabilité que tout se passe comme attendu, sous les lois écrites et un code conforme : au moins {1 - total:.3f}")
print(f"Sans les familles C et D (les seules cases de la table d'admission) : au moins {1 - fam_a - fam_b:.4f}")
print(f"Version 3, arrondis dans le bon sens (majorant par excès, minorant par défaut, quatre décimales) : ensemble au plus "
      f"{math.ceil(total * 1e4) / 1e4:.4f} (valeur {total:.6f}) ; tout comme attendu au moins {math.floor((1 - total) * 1e4) / 1e4:.4f} ; "
      f"familles A et B seules au moins {math.floor((1 - fam_a - fam_b) * 1e4) / 1e4:.4f}")
print(f"  (la ligne « Ensemble » ci-dessus, reprise de la version 2, arrondit au plus proche : {total:.4f} et {1 - total:.3f} ;"
      f" la version 2 écrivait de même 0.0260 et 0.974 pour {total + ALPHA_MORT:.6f} et {1 - total - ALPHA_MORT:.6f},"
      f" à 2,8e-12 près, le majorant de A2 dans F6)")
print(f"0 manque sur 59 : borne haute à 95 % {cp_haute(0, 59, 0.95):.4f} (repère de N-075, erratum 3, rejoué ; repris de la version 1)")


# ---------------------------------------------------------------- bloc Q
titre("[Q] Ce qui change par rapport à la version 2 (erratum 2 : F6 sans plantation, A2 retiré)")
V2 = {"lectures": 24, "exacts": 9, "fam_a": 0.0093, "issues": 7, "fam_b": 3.3e-12, "total": 0.0260,
      "au_moins": 0.974, "ab": 0.9907, "audit": 16, "audit_p": 0.016, "temoins": 12, "lancements": 1920}
print(f"témoins : {V2['temoins']} -> {N_TEMOINS} (exigés 9 -> 8 ; de marge 3) ; doivent mourir : 6 -> 5")
print(f"lancements du processus de l'expérimentateur : {V2['lancements']} -> {N_TEMOINS * 8 * L}")
print(f"famille A : lectures {V2['lectures']} -> {len(lectures)} ; tests de borne exacts {V2['exacts']} -> {n_exact} ; "
      f"somme des majorants {V2['fam_a']} -> {fam_a:.4f}")
print(f"famille B : issues {V2['issues']} -> {len(manquees)} ; somme des majorants {ecriture(V2['fam_b'])} -> {ecriture(fam_b)}")
print(f"famille C : inchangée, {R['n_controles']} contrôles, au plus {fam_c:.4f} ; famille D : inchangée, au plus {fam_d:.4f}")
print(f"ensemble : au plus {V2['total']:.4f} -> {math.ceil(total * 1e4) / 1e4:.4f} ; tout comme attendu : au moins "
      f"{V2['au_moins']} -> {math.floor((1 - total) * 1e4) / 1e4:.4f} ; "
      f"familles A et B seules : au moins {V2['ab']} -> {math.floor((1 - fam_a - fam_b) * 1e4) / 1e4:.4f}")
print(f"audit de symétrie : {V2['audit']} -> {R['n_audit']} fréquences ; déclenchement à tort au plus {V2['audit_p']} -> "
      f"{R['n_audit'] * 0.001:.3f}")
print(f"conformité de F6 : effectif des tâches non plantées 9600 -> {N_BANC} (suspect, lecteurs, indépendance suspect contre jumeau)")
assert len(lectures) == 23 and n_exact == 8 and len(manquees) == 6 and R["n_audit"] == 15
assert len([1 for a in audit if "A2" in a[0] or "honnête du régime" in a[0]]) == 0

print()
print("numpy", np.__version__, "; python", sys.version.split()[0])
