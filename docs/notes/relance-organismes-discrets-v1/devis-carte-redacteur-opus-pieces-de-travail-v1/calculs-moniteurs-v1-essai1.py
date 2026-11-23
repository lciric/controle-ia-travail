# Calculs du devis de la carte des deux moniteurs à modèle de langue du bras A.
# Entrées : texte v2 brouillon 55 (6.10, 6.11, 13.2), devis v2 (débits de l'agent, prix), configuration de référence.
import math
h = lambda s: s / 3600
t_h, t_b = 42.8 / 10, 40.2 / 10   # s par lecture, S : le temps d'une action de l'agent en lots de 8 (devis v2, lignes 42-43)
n = 6400                          # lectures par moniteur, au plus (texte, lignes 918 et 960)
f_h, f_b = 1 + 102 / 400, 1.0     # juge, cas B : 102 points de lecture, au plus un pas chacun contre 400 jetons générés (S)
mer = 1.0                         # h de mise en route (S : devis v2, ligne 56)
L_max = 4.0                       # h de lecture commune sur la carte, borne choisie d'avance, sans donnée (S)
relu, borne, stock = 1.1833, 1.30, 0.08
pire = borne + stock
tel_b, tel_h = 1.0, 2.0

# Ligne A : moniteur boîte noire par action (mise en route comprise)
A_b, A_h = mer + h(n * t_b), mer + h(n * t_h)
EA_b, EA_h = A_b * relu + tel_b, A_h * borne + tel_h
PA = A_h * 4 * pire + 4
print(f"A : {A_b:.4f} à {A_h:.4f} h ; attendu {EA_b:.4f} à {EA_h:.4f} ; pire {PA:.4f} -> {5*math.ceil(PA/5)}")

# Ligne B : juge d'une autre lignée (102 points), ouvertures, lecture commune L
B_b, B_h = h(n * t_b * f_b), h(n * t_h * f_h)
EB_b, EB_h = B_b * relu, B_h * borne
PB0 = B_h * 4 * pire + 4
PB = (B_h + L_max) * 4 * pire + 4
print(f"B : {B_b:.4f} à {B_h:.4f} h hors lecture commune ; attendu {EB_b:.4f} à {EB_h:.4f} ; pire sans lecture commune {PB0:.4f} -> {5*math.ceil(PB0/5)} ; avec {L_max} h {PB:.4f} -> {5*math.ceil(PB/5)}")
print(f"Par heure de lecture commune : attendu {relu:.4f} à {borne:.2f} USD ; pire cas {4*pire:.2f} USD")
print(f"Ensemble : {A_b+B_b:.4f} à {A_h+B_h:.4f} h ; attendu {EA_b+EB_b:.4f} à {EA_h+EB_h:.4f} ; plafonds de repli {5*math.ceil(PA/5)} + {5*math.ceil(PB/5)} = {5*math.ceil(PA/5)+5*math.ceil(PB/5)}")

# Plafonds recalculés à l'étape (m) : t mesuré (non doublé), ou, à défaut, d de l'agent doublé
PA_m = lambda tA, m=1.0: 2 * pire * (max(1.0, m) + h(n * tA)) + 4
PB_m = lambda tB, L: 2 * pire * (h(n * tB) + L) + 4
for L in (1.0, 4.0):
    print(f"  L = {L} h ; t mesuré égal à la supposition : A {PA_m(t_h):.4f} -> {math.ceil(PA_m(t_h))} ; B {PB_m(t_h*f_h, L):.4f} -> {math.ceil(PB_m(t_h*f_h, L))}")
    d = 42.8
    print(f"  L = {L} h ; débit de l'agent d = {d} s doublé : A {PA_m(2*d/10):.4f} -> {math.ceil(PA_m(2*d/10))} ; B {PB_m(2*f_h*d/10, L):.4f} -> {math.ceil(PB_m(2*f_h*d/10, L))}")
