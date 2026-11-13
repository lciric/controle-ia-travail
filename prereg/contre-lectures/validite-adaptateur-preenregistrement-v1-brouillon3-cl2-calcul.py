# Contre-lecture 2 du brouillon 3 « validité de l'adaptateur » : arithmétique des 800 directions. Aucune donnée lue.
# Sources des constantes : T0.7 scellé (prereg/T0.7-sondes-v0-v1.md, d7d180ec…), configuration v8, journal du brouillon 3.
from math import sqrt
from statistics import NormalDist

N = NormalDist()
z80, z95u = N.inv_cdf(0.80), N.inv_cdf(0.95)


def zb(niv):
    return N.inv_cdf(1 - (1 - niv) / 2)


def sigma(n1, n0):
    return 1.188 * sqrt((n1 + n0 + 1) / (12 * n1 * n0))


print("== 1. formes (piece L)")
conditions, taches, T = 9, 64, 10
n_actions = conditions * taches * T
print("actions de 7b au plus : %d x %d x %d = %d" % (conditions, taches, T, n_actions))
for n in (200, 800):
    print("plancher_<k> : (%d, n_actions <= %d) ; rang du quantile 0,95 : %.2f sur %d aires" % (n, n_actions, 0.95 * (n - 1) + 1, n))

print("== 2. piece R : passes et directions")
series = {"R1": 64, "R2_d": 256, "R3_d": 256, "R4_d": 256, "R5": 64, "R6": 64, "R7": 64, "R8_d": 256, "R9": 64, "R10_d": 256, "R11_d": 256}
ep = sum(series.values())
print("episodes notes : %d (journal du brouillon 3 : 1024 + 832 = %d) ; rapport aux 576 de 7b : %.3f" % (ep, 1024 + 832, ep / 576))
for sondes in (4, 3, 2):
    print("directions notees, %d sondes : %d a 800 par sonde (%d a 200 par sonde)" % (sondes, sondes * 800, sondes * 200))
actions_r = ep * T
for n in (200, 800):
    octets = actions_r * 4 * (1 + n) * 8
    print("scores de R, 4 sondes, %d directions, double precision : %d x 4 x %d x 8 = %.1f Mo" % (n, actions_r, 1 + n, octets / 1e6))

print("== 3. piece R : temps de notation des directions (echelle de T0.7 scelle, l. 2086)")
f = (4 / 12) * (ep / 576)
print("facteur d'echelle (4 planchers sur une douzaine, %.3f fois les jetons) : %.3f" % (ep / 576, f))
print("par lots (plancher_v3) : %.2f h attendu, %.2f h au pire (T0.7 : 0,09 et 0,32 h pour l'etape A)" % (0.09 * f, 0.32 * f))
for n, h in ((200, 4.0), (800, 16.0)):
    hb = h * f
    print("par la boucle du harnais, %d directions : %.1f h, soit %.1f a %.1f USD (1,0889 a 1,30 USD/h)" % (n, hb, hb * 1.0889, hb * 1.30))

print("== 4. devis de R refait (formule du journal du brouillon 3, § 4)")
act = 0.45
for nom, passes in (("journal", 1024 + 832 + 512), ("corrige : recalcul des 576 episodes de 7b (+192), recherche de c_d a 12 pas (768 au lieu de 512)", 1024 + 832 + 192 + 768)):
    rel = passes * act / 3600
    lo = 1.0 + 0.3 + rel + 0.05 + 0.1 + 0.0 + 0.1
    hi = 1.0 + 0.3 + rel + 0.05 + 0.5 + 0.5 + 0.1
    pire = 2 * hi * 1.40 + 1
    print("%s : %d passes, %.3f h ; R %.2f a %.2f h ; pire %.2f USD ; ensemble pire %.1f USD (HD pire 24.56)" % (nom, passes, rel, lo, hi, pire, pire + 24.56))
print("poste notation du brouillon 3 : 0,1 a 0,5 h ; par lots a 3 200 directions : %.2f a %.2f h (tient) ; par la boucle : %.1f h (ne tient pas)" % (0.09 * f, 0.32 * f, 16.0 * f))

print("== 5. disque de R (T0.7 scelle, l. 2086 : 31,5 Go d'activations pour 576 episodes, trois couches)")
par_ep = 31.5 / 576
print("par episode : %.4f Go ; recalcul de T0.7 (576) : %.1f Go ; toutes les series de R gardees (%d) : %.1f Go ; avec modele 16 et paquets 10 : %.1f Go (disque exige : 150)" % (par_ep, 576 * par_ep, ep + 192, (ep + 192) * par_ep, (ep + 192) * par_ep + 26))

print("== 6. bruit d'echantillonnage du quantile 0,95 du plancher (aires nulles normales d'ecart type s)")
phi = N.pdf(z95u)
for n in (200, 800):
    print("n = %d : ecart type du quantile = %.4f s" % (n, sqrt(0.95 * 0.05 / n) / phi))
s = sigma(640, 640)
print("a 640 contre 640, s = %.5f : %.4f (200) et %.4f (800) en aire" % (s, s * sqrt(0.95 * 0.05 / 200) / phi, s * sqrt(0.95 * 0.05 / 800) / phi))

print("== 7. puissance des lignes de soutien : regle du brouillon 3 et regle (a) de T0.7")
print("(regle (a) : meme formule, ecart type de D = 1,10 fois celui de la sonde, rapport lu a l'audit de P3 cite par T0.7 l. 2030 ; suppose)")
for niv in (0.9875, 0.9833, 0.975):
    b3 = 0.5 + (z95u + zb(niv) + z80) * s
    ra = 0.5 + (z95u + 1.10 * (zb(niv) + z80)) * s
    print("640/640 niveau %.4f : brouillon 3 %.3f ; regle (a) %.3f (ecart %+.3f)" % (niv, b3, ra, ra - b3))
for n1, n0 in ((30, 100), (50, 200), (100, 300), (200, 300)):
    sg = sigma(n1, n0)
    b3 = 0.5 + (z95u + zb(0.9875) + z80) * sg
    ra = 0.5 + (z95u + 1.10 * (zb(0.9875) + z80)) * sg
    print("VA-1 (%d, %d) niveau 0.9875 : brouillon 3 %.3f ; regle (a) %.3f" % (n1, n0, b3, ra))
print("reserve 640/640 (borne basse > 0,5, 95 %%) : %.3f (inchangee : aucun plancher dans le critere)" % (0.5 + (zb(0.95) + z80) * s))
for n in (10, 8, 5):
    sd = sqrt(2 * (2 * n + 5) / (9 * n * (n - 1)) / 64)
    b3 = (z95u + zb(0.9875) + z80) * sd
    ra = (z95u + 1.10 * (zb(0.9875) + z80)) * sd
    print("VA-2 64x%d niveau 0.9875 : brouillon 3 %.3f ; analogue de la regle (a) %.3f" % (n, b3, ra))
print("T0.7 scelle, regle (a), 64 taches, 98,75 % (l. 2031) : 0,6408 ; 0,6058 ; 0,5815 a 0,6658 (planchers de P3, non nuls)")
