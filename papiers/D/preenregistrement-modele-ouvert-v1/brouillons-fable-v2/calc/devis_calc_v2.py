#!/usr/bin/env python3
"""Recalcul des tables du devis v2 (aucune mesure : hypotheses du paragraphe 2 du devis v2).
Usage : python3 devis_calc_v2.py"""
A_TR, A_TE, C_TR, C_TE, AMORCE = 150, 100, 75, 50, 100   # taches (preenregistrement v2)
BANQUE = 542                                              # taches EvalPlus (164 + 378)
G, E, K = 8, 16, 4                                        # episodes par tache (entrainement, evaluation), tours
TOK_GEN = (350, 550)        # jetons generes par episode
TOK_EX = (850, 1050)        # jetons par exemple d'affinage
MON_IN, AUD_IN = 700, 1000  # jetons lus par episode (moniteur en boucle, audit)
SONDE_IN = 950              # jetons lus par episode reencode pour les sondes
GEN = (800, 2500)           # jetons generes par seconde (lent, rapide)
RD = (8000, 25000)          # jetons lus par seconde
TR = (1200, 5000)           # jetons d'affinage par seconde
BAC = (5, 30)               # episodes testes par seconde dans le bac a sable (sans recouvrement compte)
OVH = (4 / 60, 10 / 60)     # heures fixes par phase
PASSES, DEMOS = 2, 2000
MARGE = 1.25

ep_train = (A_TR + C_TR) * G
ep_eval = (A_TE + C_TE) * E
M = ep_train


def h(lo, hi, rate):        # heures (cas rapide, cas lent) pour un volume (lo, hi)
    return (lo / rate[1] / 3600, hi / rate[0] / 3600)


def add(*xs):
    return (sum(x[0] for x in xs), sum(x[1] for x in xs))


def mul(x, k):
    return (x[0] * k, x[1] * k)


def fmt(x, d=1):
    return f"{x[0]:.{d}f} a {x[1]:.{d}f}"


def gen_h(n):
    return h(n * TOK_GEN[0], n * TOK_GEN[1], GEN)


def bac_h(n):
    return h(n, n, BAC)


# --- un bras pour une graine (K tours ; le tour 0 est partage)
n_ep = (K - 1) * ep_train + ep_eval
gen = gen_h(n_ep)
tests = bac_h(n_ep)
mon_tok = n_ep * MON_IN + ep_eval * AUD_IN
mon = h(mon_tok, mon_tok, RD)
trn = h(K * M * TOK_EX[0] * PASSES, K * M * TOK_EX[1] * PASSES, TR)
fix = mul(OVH, K + 1)
bras = add(gen, tests, mon, trn, fix)
print("bras-graine : episodes", n_ep, "| generation", fmt(gen), "| tests", fmt(tests, 2), "| moniteurs", fmt(mon),
      f"({mon_tok/1e6:.1f} M lus)", "| affinage", fmt(trn), "| fixe", fmt(fix), "| total", fmt(bras))
print("   jetons generes (M)", n_ep * TOK_GEN[0] / 1e6, n_ep * TOK_GEN[1] / 1e6,
      "| jetons d'affinage (M)", K * M * TOK_EX[0] * PASSES / 1e6, K * M * TOK_EX[1] * PASSES / 1e6)

# --- un depart (amorcage, tour 0 : generation d'entrainement et d'evaluation, tests, moniteurs)
n0 = ep_train + ep_eval
dep = add(h(DEMOS * TOK_EX[0] * PASSES, DEMOS * TOK_EX[1] * PASSES, TR), gen_h(n0), bac_h(n0),
          h(n0 * MON_IN + ep_eval * AUD_IN, n0 * MON_IN + ep_eval * AUD_IN, RD), mul(OVH, 2))
print("depart graine-dose : episodes", n0, "| total", fmt(dep, 2))

sonde_tok = n0 * SONDE_IN
sonde = h(sonde_tok, sonde_tok, RD)
print("passe d'activations :", fmt(sonde, 2), f"({sonde_tok/1e6:.1f} M lus)")

print("\nEtage 2 (heures de carte)")
INSTALL2 = (0.5, 4.0)       # une a quatre machines, 0,5 a 1 heure chacune
for n in (8, 9, 12):
    A = add(mul(bras, 4 * n), mul(dep, n), dep, (0.0, 3 * dep[1]), INSTALL2)   # 4 bras, departs, temoin positif, remplacements, installation
    B = mul(sonde, 4 * n)                                                        # tour 0 et bras S, R, P au tour K
    C = add(mul(bras, n), mul(dep, n), (0.0, 3 * dep[1]))                        # penalite a dose forte, departs, remplacements
    T = add(A, B, C)
    print(f"n={n:2d} | A {fmt(A,0)} | B {fmt(B,1)} | C {fmt(C,0)} | total {fmt(T,0)} | A marge {fmt(mul(A,MARGE),0)}"
          f" | A+B marge {fmt(mul(add(A,B),MARGE),0)} | total marge {fmt(mul(T,MARGE),0)}")
print("episodes, n=9, trois tranches, temoin positif compris :", 45 * n_ep + 19 * n0)

print("\nEtage 1 (dans l'ordre d'execution)")
bras2 = add(gen_h(ep_train + ep_eval), bac_h(ep_train + ep_eval), h((ep_train + ep_eval) * MON_IN, (ep_train + ep_eval) * MON_IN, RD),
            h(2 * M * TOK_EX[0] * PASSES, 2 * M * TOK_EX[1] * PASSES, TR), mul(OVH, 3))
postes = [
    ("1 installation (une a deux machines)", (0.5, 2.0)),
    ("2 debits et bac a sable", (1.0, 2.0)),
    ("3 modele de base, 10 episodes sur 542 taches non mutees", add(gen_h(BANQUE * 10), bac_h(BANQUE * 10), OVH)),
    ("4 negatifs frais, 4 episodes sur 250 taches", add(gen_h(1000), bac_h(1000), OVH)),
    ("5 departs d'etalonnage a dose faible (2 a 5)", (2 * dep[0], 5 * dep[1])),
    ("6 temoin positif", dep),
    ("7 departs du pilote (4, et jusqu'a 3 remplacements)", (4 * dep[0], 7 * dep[1])),
    ("8 bras du pilote (4 graines, 2 bras, 2 tours)", mul(bras2, 8)),
    ("9 depart a dose forte", dep),
]
for k, v in postes:
    print(f"  {k} : {fmt(v)}")
tot = add(*[v for _, v in postes])
print("  total :", fmt(tot), "| avec marge de 25 % :", fmt(mul(tot, MARGE)))
avant_pilote = add(*[v for _, v in postes[:7]])
print("  cumul avant les bras du pilote :", fmt(avant_pilote))
