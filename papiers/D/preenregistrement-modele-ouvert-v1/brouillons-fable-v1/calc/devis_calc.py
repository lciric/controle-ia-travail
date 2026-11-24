#!/usr/bin/env python3
"""Recalcul des tables du devis v1 (aucune mesure : hypotheses du paragraphe 2 du devis).
Usage : python3 devis_calc.py"""
A_TR, A_TE, C_TR, C_TE, AMORCE = 150, 100, 75, 50, 100   # taches (preenregistrement)
G, E, K = 8, 16, 4                                        # episodes par tache (entrainement, evaluation), tours
TOK_GEN = (350, 550)        # jetons generes par episode
TOK_EX = (850, 1050)        # jetons par exemple d'affinage
MON_IN, AUD_IN = 700, 1000  # jetons lus par episode (moniteur en boucle, audit)
GEN = (800, 2500)           # jetons generes par seconde (lent, rapide)
RD = (8000, 25000)          # jetons lus par seconde
TR = (2000, 6000)           # jetons d'affinage par seconde
OVH = (4 / 60, 10 / 60)     # heures fixes par phase
PASSES, DEMOS = 2, 2000

ep_train = (A_TR + C_TR) * G
ep_eval = (A_TE + C_TE) * E
M = ep_train


def h(lo_tok, hi_tok, rate):  # heures (cas rapide, cas lent)
    return (lo_tok / rate[1] / 3600, hi_tok / rate[0] / 3600)


def add(*xs):
    return (sum(x[0] for x in xs), sum(x[1] for x in xs))


def mul(x, k):
    return (x[0] * k, x[1] * k)


def fmt(x, d=1):
    return f"{x[0]:.{d}f} a {x[1]:.{d}f}"


n_ep = (K - 1) * ep_train + ep_eval
gen = h(n_ep * TOK_GEN[0], n_ep * TOK_GEN[1], GEN)
mon_tok = n_ep * MON_IN + ep_eval * AUD_IN
mon = h(mon_tok, mon_tok, RD)
trn = h(K * M * TOK_EX[0] * PASSES, K * M * TOK_EX[1] * PASSES, TR)
fix = mul(OVH, K + 1)
bras = add(gen, mon, trn, fix)
print("bras-graine : episodes", n_ep, "| generation", fmt(gen), "| moniteurs", fmt(mon), f"({mon_tok/1e6:.1f} M lus)",
      "| affinage", fmt(trn), "| fixe", fmt(fix), "| total", fmt(bras))
print("   jetons generes (M)", n_ep * TOK_GEN[0] / 1e6, n_ep * TOK_GEN[1] / 1e6,
      "| jetons d'affinage (M)", K * M * TOK_EX[0] * PASSES / 1e6, K * M * TOK_EX[1] * PASSES / 1e6)

n0 = ep_train + ep_eval
dep = add(h(DEMOS * TOK_EX[0] * PASSES, DEMOS * TOK_EX[1] * PASSES, TR), h(n0 * TOK_GEN[0], n0 * TOK_GEN[1], GEN),
          h(n0 * MON_IN + ep_eval * AUD_IN, n0 * MON_IN + ep_eval * AUD_IN, RD), mul(OVH, 2))
print("depart graine-dose : episodes", n0, "| total", fmt(dep, 2))

sonde_tok = n0 * 950
sonde = h(sonde_tok, sonde_tok, RD)
print("passe d'activations :", fmt(sonde, 2), f"({sonde_tok/1e6:.1f} M lus)")

print("\nEtage 2 (heures de carte, hors marge puis avec 25 %)")
for n in (6, 9, 12):
    A = add(mul(bras, 4 * n), mul(dep, n), add(dep, (0.2, 0.5)))   # 4 bras, n departs, temoin positif
    B = mul(sonde, 4 * n)                                           # tour 0 + S, R, P au tour K
    C = add(mul(bras, n), mul(dep, n))                              # penalite a dose forte
    T = add(A, B, C)
    print(f"n={n:2d} | A {fmt(A,0)} | B {fmt(B,1)} | C {fmt(C,0)} | total {fmt(T,0)} | avec marge {fmt(mul(T,1.25),0)}")
print("episodes, n=9, trois tranches :", 45 * n_ep + 18 * n0)

print("\nEtage 1")
n_taches = A_TR + A_TE + C_TR + C_TE + AMORCE
base = add(h(n_taches * 8 * TOK_GEN[0], n_taches * 8 * TOK_GEN[1], GEN),
           h(n_taches * 8 * (MON_IN + AUD_IN), n_taches * 8 * (MON_IN + AUD_IN), RD))
demos = add(h(8000 * TOK_GEN[0], 8000 * TOK_GEN[1], GEN), h(8000 * MON_IN, 8000 * MON_IN, RD))
amorc = mul(dep, 6)   # jusqu'a 4 parts de triche a dose faible, dose forte, temoin positif
n2 = ep_train + ep_eval   # bras pilote : un tour de generation apres le tour 0, evaluation, deux affinages
bras2 = add(h(n2 * TOK_GEN[0], n2 * TOK_GEN[1], GEN), h(n2 * MON_IN, n2 * MON_IN, RD),
            h(2 * M * TOK_EX[0] * PASSES, 2 * M * TOK_EX[1] * PASSES, TR), mul(OVH, 3))
pilote = add(mul(bras2, 8), mul(dep, 4))
postes = {"debits": (1, 2), "masses du modele de base": base, "demonstrations": demos, "amorcages (6)": amorc,
          "pilote (4 graines, 2 bras, 2 tours)": pilote, "installation": (1, 3)}
for k, v in postes.items():
    print(f"  {k} : {fmt(v)}")
print("  total :", fmt(add(*postes.values())))
