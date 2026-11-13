# Puissance (règle (a) de T0.7) et devis refaits pour le brouillon 4 « validité de l'adaptateur » ; aucune donnée lue.
# Formules : journal du brouillon 3, § 4, et contre-lecture 2, § 2 bis (écart type de D = 1,10 fois celui de la sonde, supposé).
from math import sqrt
from statistics import NormalDist
N = NormalDist(); G = 1.188; z80 = N.inv_cdf(0.80); z95u = N.inv_cdf(0.95); RAPPORT_D = 1.10
def zb(niv): return N.inv_cdf(1 - (1 - niv) / 2)
def sigma(n1, n0): return G * sqrt((n1 + n0 + 1) / (12 * n1 * n0))
def soutien_regle_a(s, niv): return 0.5 + (z95u + RAPPORT_D * (zb(niv) + z80)) * s
print("== puissance, lignes de soutien, regle (a)")
s = sigma(640, 640)
for niv in (0.9875, 0.9833, 0.975):
    print("640/640 niveau %.4f : aire min %.3f" % (niv, soutien_regle_a(s, niv)))
for n1, n0 in ((30, 100), (50, 200), (100, 300), (200, 300), (20, 20)):
    sg = sigma(n1, n0)
    print("VA-1 (%d, %d) sigma %.4f : aire min %.3f" % (n1, n0, sg, soutien_regle_a(sg, 0.9875)))
print("seuil non informative sigma = 0,060 : aire min %.3f (regle (a), 98,75 %%) ; %.3f (regle du brouillon 3)"
      % (soutien_regle_a(0.060, 0.9875), 0.5 + (z95u + zb(0.9875) + z80) * 0.060))
for n in (10, 8, 5):
    sd = sqrt(2 * (2 * n + 5) / (9 * n * (n - 1)) / 64)
    print("VA-2 64x%d : tau min %.3f (analogue de la regle (a))" % (n, (z95u + RAPPORT_D * (zb(0.9875) + z80)) * sd))
print("reserve 640/640 (borne basse > 0,5, 95 %%) : aire min %.3f (inchangee)" % (0.5 + (zb(0.95) + z80) * s))
print("== devis")
ep, act = 40.2, 0.45
gen = 160 * ep / 3600; ev = 320 * ep / 3600
hd_lo = 1.0 + 0.6 + gen + 0.23 + ev + 0.2; hd_hi = 1.0 + 0.6 + gen + 0.46 + ev + 0.2
hd_att_lo = hd_lo * 1.0889 + 0.5; hd_att_hi = hd_hi * 1.30 + 0.08 * hd_hi + 2
hd_pire = 2 * hd_hi * 1.40 + 0.08 * 2 * hd_hi + 2
print("HD heures %.2f a %.2f ; attendu %.1f a %.1f ; pire %.2f (inchange)" % (hd_lo, hd_hi, hd_att_lo, hd_att_hi, hd_pire))
passes = 1856 + 192 + 768; rel = passes * act / 3600
r_lo = 1.0 + 0.3 + rel + 0.05 + 0.1 + 0.0 + 0.1; r_hi = 1.0 + 0.3 + rel + 0.05 + 0.5 + 0.5 + 0.1
r_att_lo = r_lo * 1.0889 + 0.4; r_att_hi = r_hi * 1.30 + 1
r_pire = 2 * r_hi * 1.40 + 1
print("R passes %d (series 1856, recalcul de 7b +192, recherche de c_d 768), relecture %.3f h ; heures %.2f a %.2f"
      % (passes, rel, r_lo, r_hi))
print("R attendu %.2f a %.2f ; pire %.2f h x 1,40 + 1 = %.2f" % (r_att_lo, r_att_hi, 2 * r_hi, r_pire))
print("ensemble heures %.2f a %.2f ; attendu %.2f a %.2f ; pire %.2f" % (hd_lo + r_lo, hd_hi + r_hi, hd_att_lo + r_att_lo, hd_att_hi + r_att_hi, hd_pire + r_pire))
print("coupures 21,0 + 8,5 + reserve 0,5 = %.1f ; pire de R au-dessus de sa coupure de %.2f USD" % (21.0 + 8.5 + 0.5, r_pire - 8.5))
