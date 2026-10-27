"""Vérifications analytiques (contre-lecture R2) : espérance du signe sous un nul de moyenne nulle ; dérive des
composantes du mélange ; pentes de la courbe de détection au point de fonctionnement 1 %."""
import math
from math import comb

def binom_pmf(n, p):
    return [comb(n, k) * p**k * (1-p)**(n-k) for k in range(n+1)]

def esperance_signe_et_v(types, m=10):
    """types : (poids, pA, pB). Renvoie E[v], E[signe(v)], E[v^2] pour v = rA - rB, parts binomiales de m épisodes."""
    Ev = Es = Ev2 = 0.0
    for w, a, b in types:
        pa, pb = binom_pmf(m, a), binom_pmf(m, b)
        for i in range(m+1):
            for j in range(m+1):
                v = (i - j) / m
                pr = w * pa[i] * pb[j]
                Ev += pr * v; Es += pr * (v > 0) - pr * (v < 0); Ev2 += pr * v * v
    return Ev, Es, Ev2

def derive(types, lam, forme, m=10):
    """E[log(1 + lam * x)] par tâche, x = v ou signe(v)."""
    tot = 0.0
    for w, a, b in types:
        pa, pb = binom_pmf(m, a), binom_pmf(m, b)
        for i in range(m+1):
            for j in range(m+1):
                v = (i - j) / m
                x = v if forme == "parts" else (1.0 if v > 0 else (-1.0 if v < 0 else 0.0))
                tot += w * pa[i] * pb[j] * math.log(1 + lam * x)
    return tot

scen = {"S1 (90 % : +0,10 ; 10 % : -0,90)": [(0.9, 0.55, 0.45), (0.1, 0.05, 0.95)],
        "S2 (80 % : +0,10 ; 20 % : -0,40, mode écarté)": [(0.8, 0.6, 0.5), (0.2, 0.2, 0.6)],
        "alternative 20 points (0,6 contre 0,4)": [(1.0, 0.6, 0.4)]}
for nom, t in scen.items():
    Ev, Es, Ev2 = esperance_signe_et_v(t)
    print(f"{nom} : E[v] = {Ev:+.4f} ; E[signe] = {Es:+.4f}")
    for lam in (0.1, 0.3, 0.6, 0.9):
        print(f"   lambda {lam} : dérive parts {derive(t, lam, 'parts'):+.4f} nat/tâche ; dérive signe {derive(t, lam, 'signe'):+.4f}")
# borne de croissance de toute mise valide pour le nul E[v] <= 0 sur [-1, 1] : max_lambda E log(1 + lambda v), lambda <= 1
t = [(1.0, 0.6, 0.4)]
best = max((derive(t, l/100, 'parts'), l/100) for l in range(1, 100))
print(f"alternative 20 points : meilleure dérive valide (lambda <= 0,99) = {best[0]:.4f} nat/tâche à lambda = {best[1]} ; "
      f"log 20 / dérive = {math.log(20)/best[0]:.1f} tâches en moyenne, sans prix de mélange")
# pente de la courbe de détection binormale au point 1 % (rappel 0,40 puis 0,80)
def phi(x): return math.exp(-x*x/2)/math.sqrt(2*math.pi)
z99 = 2.3263478740408408
for rappel, zr in ((0.40, 0.2533471031357997), (0.80, -0.8416212335729143)):
    d = z99 - zr
    pente = phi(z99 - d) / phi(z99)
    print(f"courbe binormale, rappel {rappel} à 1 % : pente d(rappel)/d(taux de faux positifs) = {pente:.1f} ; "
          f"0,5 point de faux positifs achète ≈ {pente*0.005*100:.0f} points de rappel")
# contre-exemple exact sur deux points
print("contre-exemple deux points : v = +0,1 (proba 0,9), v = -0,9 (proba 0,1) : E[v] =", 0.9*0.1 + 0.1*(-0.9),
      "; E[signe] =", 0.9 - 0.1, "; dérive du signe à lambda 0,6 =", round(0.9*math.log(1.6) + 0.1*math.log(0.4), 4), "nat/tâche")
