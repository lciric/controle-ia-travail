# Calculs du devis de la carte des deux moniteurs à modèle de langue du bras A.
# Entrées : texte v2 brouillon 55 (6.10, 6.11, 13.2) ; devis v2 (débits de l'agent, prix) ; configuration de référence ;
# réponses du lecteur habilité transmises par la session mère (2026-11-22, 22:33Z), sans interne.
import math
h = lambda s: s / 3600
n = 6400                                # lectures par moniteur, au plus (texte, lignes 918 et 960)
t_b, t_h = 40.2 / 10, 42.8 / 10         # S1 : s par lecture du moniteur boîte noire = une action de l'agent en lots de 8 (devis v2, lignes 42-43)
passe = 0.45                            # S2 : passe de contexte refaite une fois par action (devis v2, ligne 45 : une passe sur texte imposé)
courtes = 11 / 400                      # S2 : onze passes courtes, chacune au plus un pas contre 400 pas de génération
tJ = lambda t: t * (1 + courtes) + passe   # s par lecture du juge
L_b, L_h = 0.1, 1.0                     # S3 : lecture commune sur la carte, « quelques minutes à moins d'une heure »
mer = 1.0                               # S5 : mise en route, les deux modèles (devis v2, ligne 56)
relu, borne, stock = 1.1833, 1.30, 0.08
pire = borne + stock
tel_b, tel_h = 1.0, 2.0
c5 = lambda x: 5 * math.ceil(x / 5)

print(f"s par lecture : boîte noire {t_b:.4f} à {t_h:.4f} (borne haute {2*t_h:.4f}) ; juge {tJ(t_b):.4f} à {tJ(t_h):.4f} (borne haute {2*tJ(t_h):.4f})")
# Ligne A : moniteur boîte noire, mise en route comprise
A_b, A_h = mer + h(n * t_b), mer + h(n * t_h)
EA_b, EA_h = A_b * relu + tel_b, A_h * borne + tel_h
PA = A_h * 4 * pire + 4
print(f"A : {A_b:.4f} à {A_h:.4f} h ; attendu {EA_b:.4f} à {EA_h:.4f} ; pire {PA:.4f} -> {c5(PA)}")
# Ligne B : juge (102 points), ouvertures, lecture commune
Bl_b, Bl_h = h(n * tJ(t_b)), h(n * tJ(t_h))
B_b, B_h = Bl_b + L_b, Bl_h + L_h
EB_b, EB_h = B_b * relu, B_h * borne
PB = B_h * 4 * pire + 4
print(f"B : lectures {Bl_b:.4f} à {Bl_h:.4f} h ; avec la lecture commune {B_b:.4f} à {B_h:.4f} h ; attendu {EB_b:.4f} à {EB_h:.4f} ; pire {PB:.4f} -> {c5(PB)}")
print(f"Ensemble : {A_b+B_b:.4f} à {A_h+B_h:.4f} h ; attendu {EA_b+EB_b:.4f} à {EA_h+EB_h:.4f} ; plafonds de repli {c5(PA)} + {c5(PB)} = {c5(PA)+c5(PB)}")
# Plafonds recalculés à l'étape (m) : débits mesurés pris tels quels ; à défaut, d de l'agent, doublé
PA_m = lambda tA, m=1.0: 2 * pire * (max(1.0, m) + h(n * tA)) + 4
PB_m = lambda tB, L: 2 * pire * (h(n * tB) + L) + 4
print(f"  débits mesurés égaux aux hypothèses hautes, L = {L_h} : A {PA_m(t_h):.4f} -> {math.ceil(PA_m(t_h))} ; B {PB_m(tJ(t_h), L_h):.4f} -> {math.ceil(PB_m(tJ(t_h), L_h))}")
for d in (40.0, 42.8, 45.0):
    print(f"  d = {d} s, doublé, L = {L_h} : A {PA_m(2*d/10):.4f} -> {math.ceil(PA_m(2*d/10))} ; B {PB_m(2*tJ(d/10), L_h):.4f} -> {math.ceil(PB_m(2*tJ(d/10), L_h))}")
