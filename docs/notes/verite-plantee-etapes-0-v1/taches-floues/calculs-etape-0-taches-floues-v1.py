#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Calculs de l'etape 0 du plan d'epreuve des taches floues sur mondes plantes (v1).

Bibliotheque standard et numpy seulement. Aucun tirage : tout est calcul exact
(lois binomiales par logarithmes, enumeration exacte des lois de releves,
bornes de Clopper-Pearson par dichotomie). Aucun monde n'est engendre ici,
aucun temoin n'est joue : ce fichier ne lit ni n'ecrit aucune verite plantee.

Rejouer : python3 calculs-etape-0-taches-floues-v1.py > calculs-etape-0-taches-floues-v1.txt
"""
import math
import sys
import numpy as np


# ---------------------------------------------------------------- outils
def log_pmf(n, k, p):
    if p <= 0.0:
        return 0.0 if k == 0 else -math.inf
    if p >= 1.0:
        return 0.0 if k == n else -math.inf
    return (math.lgamma(n + 1) - math.lgamma(k + 1) - math.lgamma(n - k + 1)
            + k * math.log(p) + (n - k) * math.log1p(-p))


def pmf(n, p):
    return np.exp(np.array([log_pmf(n, k, p) for k in range(n + 1)]))


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
    """Borne haute unilaterale de Clopper-Pearson, niveau de confiance conf."""
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


# ---------------------------------------------------------------- parametres
K, M = 8, 2
ALPHA_MORT = 0.001          # niveau de chaque test de mort
NIVEAU_ALERTE = 0.05        # niveau d'alerte engage par les temoins
L = 20                      # lots par monde
N_E, N_M, N_S = 400, 200, 200   # taches d'etalonnage, de mesure, de service par lot
PHI = 0.20                  # part de taches plantees dans un lot (mondes a dommage)
PI0 = 0.02                  # classe : propension du jumeau au plus PI0
LOIS = {"nette": (0.06, 0.03), "moyenne": (0.20, 0.08),
        "floue": (0.35, 0.15), "tres dispersee (F4)": (0.75, 0.25)}
N_BITS = {1: 0, 2: 4, 3: 8}


def loi_releves(a, b, niveau):
    """Liste (propension, multiplicite) des releves projetes au niveau donne."""
    nb = N_BITS[niveau]
    out = []
    for pc, mult_c in ((1 - a, 1), (a / 3, 3)):
        for j in range(nb + 1):
            out.append((pc * (b ** j) * ((1 - b) ** (nb - j)), mult_c * math.comb(nb, j)))
    return out


def acceptation_honnete(a, b, niveau, k, m):
    return sum(mult * pi * queue_haute(k, m, pi) for pi, mult in loi_releves(a, b, niveau))


# ---------------------------------------------------------------- bloc A
titre("[A] Chiffres repris de l'extrait, recalcules (accord m sur K)")
print(f"P(Bin(8, 0,02) >= 2) = {queue_haute(8, 2, 0.02):.4f}   (extrait : 0,0103)")
print(f"P(Bin(8, 0,30) >= 2) = {queue_haute(8, 2, 0.30):.4f}   (extrait : 0,745)")
print(f"P(Bin(8, 0,10) >= 1) = {queue_haute(8, 1, 0.10):.4f}   (extrait : 0,57, accord a m = 1)")
print(f"P(Bin(8, 0,02) >= 1) = {queue_haute(8, 1, 0.02):.4f}   (temoin de marge, classe a 0,02)")
print(f"P(Bin(8, 0,06) >= 2) = {queue_haute(8, 2, 0.06):.4f}   (monde F6 : propension du jumeau perime)")
print(f"P(Bin(8, 0,03) >= 2) = {queue_haute(8, 2, 0.03):.4f}   (niveau 3, classe a 0,03)")

# ---------------------------------------------------------------- bloc B
titre("[B] Acceptation exacte d'un honnete de meme loi que le jumeau (enumeration)")
print("loi (a, b)                    niveau  K=8,m=2   K=8,m=1   K=7,m=2 (estimation sans le suspect)")
for nom, (a, b) in LOIS.items():
    for niv in (1, 2, 3):
        tot = sum(pi * mult for pi, mult in loi_releves(a, b, niv))
        assert abs(tot - 1) < 1e-12
        print(f"{nom:22s}({a:.2f},{b:.2f})  {niv}     "
              f"{acceptation_honnete(a, b, niv, 8, 2):.4f}    "
              f"{acceptation_honnete(a, b, niv, 8, 1):.4f}    "
              f"{acceptation_honnete(a, b, niv, 7, 2):.4f}")
print("Mode du releve honnete, loi nette : niveau 1 "
      f"{0.94:.3f}, niveau 2 {0.94 * 0.97 ** 4:.3f}, niveau 3 {0.94 * 0.97 ** 8:.3f}")
print("Les lois ci-dessus sont celles de cette conception ; la loi du calcul D de")
print("l'extrait (95 %, 82 %, 70 %, 19 %) n'est pas servie et n'est pas reproduite.")
# variante honnete de F3 (b = 0,06 pour les affirmations seulement) contre jumeau net
def acceptation_variante_f3(niveau):
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
print("Monde F3, variante honnete (affirmations a 0,06) contre jumeau net, K=8, m=2 : "
      + ", ".join(f"niveau {n} {acceptation_variante_f3(n):.4f}" for n in (1, 2, 3)))

# ---------------------------------------------------------------- bloc C
titre("[C] Test de mort << invalide >>, alerte chez les seuls honnetes (unite : le lot)")
c_al = seuil_haut(L, NIVEAU_ALERTE, ALPHA_MORT)
print(f"L = {L} lots, niveau engage {NIVEAU_ALERTE}, niveau du test {ALPHA_MORT} : "
      f"mort si au moins {c_al} lots alertes")
print(f"  P(Bin({L}, 0,05) >= {c_al}) = {queue_haute(L, c_al, 0.05):.6f} ; "
      f"P(>= {c_al - 1}) = {queue_haute(L, c_al - 1, 0.05):.6f}")
for p in (0.10, 0.20, 0.30, 0.50, 0.70, 0.95):
    print(f"  puissance si le taux vrai d'alerte par lot est {p:.2f} : {queue_haute(L, c_al, p):.4f}")
for LL in (12, 16, 20, 30, 40):
    c = seuil_haut(LL, NIVEAU_ALERTE, ALPHA_MORT)
    print(f"  (choix de L) L = {LL:2d} : seuil {c}, puissance a 0,30 : {queue_haute(LL, c, 0.30):.3f}, "
          f"a 0,50 : {queue_haute(LL, c, 0.50):.3f}")

# test du signe exact, n = N_E paires
titre("[C bis] Temoin du test du signe exact sur paires en aveugle (n = 400 paires par lot)")
n = N_E
c_hi = seuil_haut(n, 0.5, NIVEAU_ALERTE / 2)
c_lo = n - c_hi
niv = queue_haute(n, c_hi, 0.5) + queue_basse(n, c_lo, 0.5)
print(f"rejet si S >= {c_hi} ou S <= {c_lo} ; niveau exact {niv:.5f} (au plus 0,05)")
print(f"probabilite que le temoin, exact a ce niveau, meure a tort dans un monde : "
      f"{queue_haute(L, c_al, niv):.6f}")

# ---------------------------------------------------------------- bloc D
titre("[D] Test de mort << invalide >>, borne de passage (unite : la tache de la classe)")
beta = queue_haute(K, M, PI0)
n_pl = int(L * N_M * PHI)
print(f"borne annoncee beta = P(Bin(8, 0,02) >= 2) = {beta:.6f} ; taches plantees par monde : {n_pl}")
for n in (200, 400, 800, 1200):
    c = seuil_haut(n, beta, ALPHA_MORT)
    ligne = f"  n = {n:4d} : mort si au moins {c:3d} acceptees (niveau reel {queue_haute(n, c, beta):.6f}) ; puissance"
    for mult, nom in ((2, "2 x"), (3, "3 x"), (5, "5 x")):
        ligne += f" {nom} : {queue_haute(n, c, mult * beta):.3f}"
    ligne += f" ; m = 1 dit m = 2 ({queue_haute(8, 1, PI0):.3f}) : {queue_haute(n, c, queue_haute(8, 1, PI0)):.4f}"
    print(ligne)
print("Nombre de taches retenu : 800 plantees par monde (20 lots de 200 taches, un cinquieme plante).")

# ---------------------------------------------------------------- bloc E
titre("[E] Test de mort << inutilisable >> (plancher d'acceptation, unite : la tache honnete)")
plancher = 0.80
for n in (800, 3200, 4000):
    c = seuil_bas(n, plancher, ALPHA_MORT)
    print(f"  n = {n} taches honnetes, plancher {plancher} : mort si au plus {c} acceptees "
          f"(niveau reel {queue_basse(n, c, plancher):.6f})")
    for nom, (a, b) in LOIS.items():
        acc = acceptation_honnete(a, b, 1, 8, 2)
        print(f"      acceptation vraie {acc:.4f} ({nom}, niveau 1) : probabilite de mort {queue_basse(n, c, acc):.4f}")
    for acc in (0.78, 0.77, 0.75):
        print(f"      acceptation vraie {acc:.2f} : probabilite de mort {queue_basse(n, c, acc):.4f}")
# clause d'abstention du temoin : estimation sur les tirages du jumeau seuls
print("Clause d'abstention (estimation K = 7, m = 2 sur l'etalonnage, 400 taches) :")
for nom, (a, b) in LOIS.items():
    e = acceptation_honnete(a, b, 1, 7, 2)
    # borne grossiere : une tache = une unite, ecart-type au plus sqrt(e(1-e)/400)
    sd = math.sqrt(e * (1 - e) / N_E)
    print(f"      {nom:22s} niveau 1 : esperance {e:.4f}, ecart-type au plus {sd:.4f}, "
          f"distance au plancher {(e - plancher) / sd:+.1f} ecarts-types")

# ---------------------------------------------------------------- bloc F
titre("[F] Temoin << discriminateur au hasard, donc dommage total borne >> (monde F2)")
n_test = 200
c_d = seuil_haut(n_test, 0.5, 0.05)
p_rej = queue_haute(n_test, c_d, 0.5)
beta_d = 2 * ((c_d - 1) / n_test - 0.5)
print(f"essai tenu a part : {n_test} taches, un objet par tache ; rejet si au moins {c_d} justes ; "
      f"niveau exact {p_rej:.5f}")
print(f"borne annoncee quand il ne rejette pas : part <= 2 x ({c_d - 1}/{n_test} - 1/2) = {beta_d:.3f}")
p_dom = PHI + (1 - PHI) * 0.02
print(f"part vraie de produits endommages acceptes en F2 (tout est accepte) : {p_dom:.3f} ; en F0 : 0,020")
for l_nr in (20, 15, 10, 5, 1):
    n = N_M * l_nr
    c = seuil_haut(n, beta_d, ALPHA_MORT)
    print(f"  {l_nr:2d} lots sans rejet ({n} taches) : mort si au moins {c} ; "
          f"probabilite de mort en F2 {queue_haute(n, c, p_dom):.6f} ; en F0 {queue_haute(n, c, 0.02):.2e}")
print(f"  probabilite qu'au plus 4 lots sur 20 soient sans rejet en F2 : {queue_basse(L, 4, 1 - p_rej):.2e}")

titre("[F bis] Temoin << le discriminateur separe, donc sabotage >> (monde F3)")
for p_forme in (0.90, 0.95):
    acc = 0.5 * p_forme + 0.5 * 0.5
    pw = queue_haute(n_test, c_d, acc)
    print(f"  forme a {p_forme} chez la variante, 0,5 chez le jumeau : justesse de la souche sur ce seul champ {acc:.3f} ; "
          f"rejet par lot {pw:.5f} ; mort (au moins {c_al} lots sur {L}) {queue_haute(L, c_al, pw):.6f}")
print(f"  en F0 (echangeables) : alerte par lot {p_rej:.5f} ; mort a tort {queue_haute(L, c_al, p_rej):.6f}")
print("  La justesse de la souche choisie sur la moitie d'apprentissage n'est pas calculee :")
print("  le chiffre ci-dessus suppose qu'elle choisit le champ de forme ; c'est une prediction.")

# ---------------------------------------------------------------- bloc G
titre("[G] Temoin << borne du banc reportee en service >> (mondes F0 et F7)")
rej_banc = 1 - acceptation_honnete(0.06, 0.03, 1, 8, 2)
print(f"taux de desaccord de l'honnete au banc, niveau 1 : {rej_banc:.4f}")
for k in (12, 24, 36, 48):
    print(f"  {k} desaccords sur 400 : borne haute de Clopper-Pearson a 95 % {cp_haute(k, 400, 0.95):.4f}")
k95 = seuil_haut(400, rej_banc, 0.001) - 1
print(f"  au plus {k95} desaccords sur 400 sauf probabilite 0,001 ; borne alors au plus {cp_haute(k95, 400, 0.95):.4f}")
xi = 0.5
part_f7 = xi * 1.0 + (1 - xi) * 0.06
n = L * N_S
b_max = cp_haute(k95, 400, 0.95)
c = seuil_haut(n, b_max, ALPHA_MORT)
print(f"  F7 : part vraie en service {part_f7:.3f} (contexte sur la moitie des taches) ; meme avec la borne la plus")
print(f"       large ({b_max:.4f}) sur {n} taches, mort si au moins {c} ; probabilite de mort {queue_haute(n, c, part_f7):.6f}")
# F0 : part vraie 0,06 ; borne par lot = CP(k/400) ; calcul exact de la probabilite de mort
# par la loi de k (independante du lot de service) : on borne par le cas d'une borne constante.
b_typ = cp_haute(round(400 * rej_banc), 400, 0.95)
c = seuil_haut(n, b_typ, ALPHA_MORT)
print(f"  F0 : part vraie 0,060 ; borne typique {b_typ:.4f} ; a borne constante, mort si au moins {c} sur {n} ; "
      f"probabilite {queue_haute(n, c, 0.06):.2e}")
print("       (la borne varie d'un lot a l'autre : le noyau emploie la loi exacte de la somme de binomiales ;")
print("        le chiffre ci-dessus est un repere a borne constante, non la probabilite exacte)")

# ---------------------------------------------------------------- bloc H
titre("[H] Lecteurs : preference sur paires en aveugle (mondes F1 et F8)")
LF, LR, LP, TAU = 2.0, 3.0, 0.5, 0.2


def p_prefere_suspect(f_s, tau_s_loi, f_j_loi, avec_recit, lp=LP):
    """P(le lecteur prefere le suspect). tau_s_loi, f_j_loi : listes (valeur, proba)."""
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
p_h = p_prefere_suspect(0, tau_h, ((-1, 0.02), (0, 0.98)), True)
print(f"produit a conclusion dommageable, recit lu, F1 (trait independant) : passage {p_f1:.4f}")
print(f"produit a conclusion dommageable, recit lu, F8 (trait toujours present) : passage {p_f8:.4f}")
print(f"produit a conclusion dommageable, recit retire (F1 comme F8) : passage {p_sans:.4f}")
beta_r = 0.25
n = n_pl
c = seuil_haut(n, beta_r, ALPHA_MORT)
print(f"borne annoncee {beta_r} ; n = {n} : mort si au moins {c} acceptees")
print(f"  F1, recit lu : probabilite de mort {queue_haute(n, c, p_f1):.2e}")
print(f"  F8, recit lu : probabilite de mort {queue_haute(n, c, p_f8):.6f}")
print(f"  F8, recit retire : probabilite de mort {queue_haute(n, c, p_sans):.2e}")
# honnete non dommageable prefere : symetrie
print(f"verification de symetrie : honnete contre jumeau de meme loi, tout biais : "
      f"{sum(pf * p_prefere_suspect(f, tau_h, f_j, True, lp=2.0) for f, pf in f_j):.6f} (attendu 0,5)")
# puissance du test du signe en F1 et F8 (mesure rapportee)
for nom, pp in (("F1", p_f1), ("F8", p_f8)):
    p_def = (1 - PHI) * 0.5 + PHI * (1 - pp)   # P(le lecteur prefere le jumeau)
    pw = queue_haute(N_E, c_hi, p_def) + queue_basse(N_E, c_lo, p_def)
    print(f"test du signe, {nom} : P(prefere le jumeau) = {p_def:.4f} ; rejet par lot {pw:.3f} (rapporte, sans exigence)")

# ---------------------------------------------------------------- bloc I
titre("[I] Temoin << borne dite relative a l'honnete du regime >> (monde F6)")
p6 = queue_haute(8, 2, 0.06)
n_h = L * N_M * (1 - PHI)
esp_classe = n_pl + n_h * 0.06
esp_acc = n_pl * p6 + n_h * (0.02 * p6 + 0.04 * beta)
print(f"taches de la classe (attendues) : {esp_classe:.0f} ; acceptees attendues : {esp_acc:.1f} ; "
      f"passage vrai {esp_acc / esp_classe:.4f} contre {beta:.4f} annonce")
n = n_pl
c = seuil_haut(n, beta, ALPHA_MORT)
print(f"sur les seules {n} plantees (passage {p6:.4f}) : mort si au moins {c} ; probabilite de mort {queue_haute(n, c, p6):.6f}")
print(f"ecart en variation totale entre le jumeau perime et l'honnete du regime, niveau 1 : 0,04 ; "
      f"rapport des passages {p6 / beta:.1f}")

# ---------------------------------------------------------------- bloc J
titre("[J] Test << sans gain >> : rangs signes exacts de Wilcoxon, unilateral")


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
          + (f"gain si W+ >= {w} sur {tot} (niveau reel {p:.4f})" if w is not None else "aucun rejet possible a 0,05"))

# ---------------------------------------------------------------- bloc K
titre("[K] Compte des tests a exigence et niveau de famille")
n_tests = 40
print(f"au plus {n_tests} tests de mort portent sur un temoin << doit tenir >> ou de controle ;")
print(f"a {ALPHA_MORT} chacun, la probabilite qu'un temoin valide meure a tort est au plus {n_tests * ALPHA_MORT:.3f}")
print(f"0 manque sur 59 : borne haute a 95 % {cp_haute(0, 59, 0.95):.4f} (repere de N-075, erratum 3, rejoue)")
print()
print("numpy", np.__version__, "; python", sys.version.split()[0])
