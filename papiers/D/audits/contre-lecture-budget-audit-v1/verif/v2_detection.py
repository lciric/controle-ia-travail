# Contre-lecture independante : theoreme de detection minimax (thm:audit-detection).
import math, itertools
from fractions import Fraction as Fr
from math import comb
import numpy as np
from scipy.optimize import linprog

def q(T, k, B):
    return Fr(comb(T - k, B), comb(T, B)) if B <= T - k else Fr(0)

# (a) valeur du jeu par programme lineaire sur toutes les strategies mixtes d'audit (sous-ensembles de taille B)
print("(a) valeur minimax par programme lineaire contre 1 - q :")
for (T, k, B) in [(5, 1, 2), (5, 2, 2), (6, 2, 3), (6, 3, 1), (7, 2, 2), (7, 3, 3)]:
    Qs = list(itertools.combinations(range(T), B)); Fs = list(itertools.combinations(range(T), k))
    # variables : p_Q (>=0, somme 1), v ; max v s.c. pour tout F : sum_Q p_Q 1[F inter Q non vide] >= v
    nQ = len(Qs)
    c = np.zeros(nQ + 1); c[-1] = -1
    A = []; b = []
    for F in Fs:
        row = np.zeros(nQ + 1)
        for i, Q in enumerate(Qs):
            row[i] = -1.0 if set(F) & set(Q) else 0.0
        row[-1] = 1.0; A.append(row); b.append(0.0)
    Aeq = [np.r_[np.ones(nQ), 0.0]]
    r = linprog(c, A_ub=np.array(A), b_ub=b, A_eq=np.array(Aeq), b_eq=[1.0], bounds=[(0, None)] * nQ + [(None, None)], method="highs")
    print(f"  T={T} k={k} B={B} : LP {-r.fun:.10f}  1-q {float(1 - q(T, k, B)):.10f}")

# (b) bornes, exactes en rationnels sauf racines ; B*_det ; borne inferieure de l'enonce de mission
bad = 0; tot = 0
claim_viol = 0; claim_tot = 0; exemples = []
rem_rel = []
for T in [1, 2, 3, 10, 33, 100, 257]:
    for k in range(1, T + 1):
        for B in range(0, T - k + 1):
            qq = q(T, k, B)
            lo = Fr(T - k + 1 - B, T - k + 1) ** k; hi = Fr(T - B, T) ** k
            tot += 1
            if not (lo <= qq <= hi and float(hi) <= math.exp(-k * B / T) * (1 + 1e-12)): bad += 1
            if not (1 - qq >= 0 and qq >= 1 - Fr(k * B, T - k + 1)): bad += 1
        for delta in [0.5, 0.2, 0.1, 0.05, 0.01, 1e-3, 1e-6]:
            Bs = min(B for B in range(T + 1) if q(T, k, B) <= Fr(delta))
            y = math.log(1 / delta) / k
            chain = [(T - k + 1) * y / (1 + y), (T - k + 1) * (1 - delta ** (1 / k)), Bs,
                     math.ceil(T * (1 - delta ** (1 / k)) - 1e-12), math.ceil(T / k * math.log(1 / delta))]
            tot += 1
            if not all(chain[i] <= chain[i + 1] + 1e-9 for i in range(4)): bad += 1; print("viol", T, k, delta, chain)
            claimed = (T - k + 1) / k * math.log(1 / delta)
            claim_tot += 1
            if Bs < claimed - 1e-9:
                claim_viol += 1
                if len(exemples) < 4 and T >= 100: exemples.append((T, k, delta, Bs, round(claimed, 2)))
            if T == 257 and k in (1, 3, 10, 30, 100):
                rem_rel.append((k, delta, Bs, round(T / k * math.log(1 / delta), 1)))
print(f"(b) chaine de bornes : {tot} cas, violations {bad}")
print(f"    borne (T-k+1)/k log(1/delta) annoncee dans la mission : fausse dans {claim_viol}/{claim_tot} cas ; exemples {exemples}")
print("    T=257 : (k, delta, B*_det, (T/k)log(1/delta) de la remarque rem:audit-detect-deter)")
for r_ in rem_rel:
    if r_[1] in (0.05, 1e-3): print("     ", r_)
# contre-exemple de la note : T=100, k=1, delta=0.01
print("    note : T=100 k=1 delta=0.01 -> B* =", min(B for B in range(101) if q(100, 1, B) <= Fr(1, 100)), "; borne annoncee", 100 * math.log(100))
# la borne annoncee est-elle jamais vraie pour k >= log(1/delta) a grand T ?
for (T, k, d) in [(10**4, 50, 0.05), (10**4, 500, 0.05), (10**5, 1000, 0.01)]:
    Bs_cont = T * (1 - d ** (1 / k))  # minorant serre a 1 pres pour T >> k
    print(f"    T={T} k={k} delta={d} : T(1-delta^(1/k)) = {Bs_cont:.1f} ; (T-k+1)/k log(1/delta) = {(T-k+1)/k*math.log(1/d):.1f}")

# (c) test d'un taux : programme lineaire sur les tests randomises phi(s), s = nombre de 1
print("(c) min max(alpha, beta) par programme lineaire, alternative eps' dans une grille >= eps :")
for (B, eps) in [(3, 0.2), (10, 0.1), (25, 0.05)]:
    grid = np.linspace(eps, 1, 400)
    # variables phi_0..phi_B in [0,1], t ; min t ; alpha = phi_0 <= t ; beta(e) = sum_s binom (1-phi_s) <= t
    nv = B + 2; cvec = np.zeros(nv); cvec[-1] = 1
    A = []; b = []
    row = np.zeros(nv); row[0] = 1; row[-1] = -1; A.append(row); b.append(0)
    for e in grid:
        pm = np.array([comb(B, s) * e ** s * (1 - e) ** (B - s) for s in range(B + 1)])
        row = np.zeros(nv); row[:B + 1] = -pm; row[-1] = -1; A.append(row); b.append(-pm.sum())
    r = linprog(cvec, A_ub=np.array(A), b_ub=b, bounds=[(0, 1)] * (B + 1) + [(0, None)], method="highs")
    mu = (1 - eps) ** B
    print(f"  B={B} eps={eps}: LP {r.fun:.10f}  mu/(1+mu) {mu/(1+mu):.10f}")
