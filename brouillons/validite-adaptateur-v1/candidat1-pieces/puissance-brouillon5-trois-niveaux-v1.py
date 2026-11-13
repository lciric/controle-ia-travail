# Puissance sous la règle (a) aux trois niveaux de Bonferroni de T0.7 (quatre, trois, deux sondes lues) — brouillon 5 ;
# même formule que puissance-devis-brouillon4-v1.py (écart type de D = 1,10 fois celui de la sonde, supposé) ; aucune donnée lue.
from math import sqrt
from statistics import NormalDist
N = NormalDist(); G = 1.188; z80 = N.inv_cdf(0.80); z95u = N.inv_cdf(0.95); RAPPORT_D = 1.10
NIVEAUX = (0.9875, 0.9833, 0.975)
def zb(niv): return N.inv_cdf(1 - (1 - niv) / 2)
def sigma(n1, n0): return G * sqrt((n1 + n0 + 1) / (12 * n1 * n0))
def soutien(s, niv): return 0.5 + (z95u + RAPPORT_D * (zb(niv) + z80)) * s
def sd_tau(n): return sqrt(2 * (2 * n + 5) / (9 * n * (n - 1)) / 64)
f = lambda xs: " / ".join("%.3f" % x for x in xs)
print("niveaux : 98,75 % / 98,33 % / 97,5 %")
print("VA-3, VA-5b, VA-6 (640/640) : " + f([soutien(sigma(640, 640), n) for n in NIVEAUX]))
for n1, n0 in ((30, 100), (50, 200), (100, 300), (200, 300)):
    print("VA-1 (%d, %d) : %s" % (n1, n0, f([soutien(sigma(n1, n0), n) for n in NIVEAUX])))
for k in (10, 8, 5):
    print("VA-2 64x%d (tau, analogue de la regle (a)) : %s" % (k, f([(z95u + RAPPORT_D * (zb(n) + z80)) * sd_tau(k) for n in NIVEAUX])))
for k in (10, 8):
    print("VA-4b 64x%d (ecart de tau, sans plancher) : %s" % (k, f([(zb(n) + z80) * sqrt(2) * sd_tau(k) for n in NIVEAUX])))
print("seuil non informative sigma = 0,060 : " + f([soutien(0.060, n) for n in NIVEAUX]))
print("reserve 640/640 (95 %%, borne basse > 0,5) : %.3f" % (0.5 + (zb(0.95) + z80) * sigma(640, 640)))
rel = (1856 + 192 + 768) * 0.45 / 3600
r4 = 1.0 + 0.3 + rel + 0.05 + 0.5 + 2.0 + 0.1
print("R pire sur 4 coeurs : %.3f h x 2 x 1,40 + 1 = %.2f USD" % (r4, 2 * r4 * 1.40 + 1))
