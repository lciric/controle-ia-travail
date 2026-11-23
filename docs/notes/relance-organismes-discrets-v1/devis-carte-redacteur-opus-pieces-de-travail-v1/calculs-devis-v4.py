# Calculs du devis de carte v3 du bras A. Entrées : devis v2 (lignes citées), texte v2 brouillon 55 (6.11), configuration de référence.
import math
h = lambda s: s / 3600
ep_h, ep_b = 42.8, 40.2            # s par épisode (devis v2, lignes 42-43 ; autre chaîne)
dist_h, dist_b = 3.0, 2.1          # s par pas de distillation (devis v2, ligne 55 ; S)
prise = 0.45                       # s par passe sur texte imposé (devis v2, ligne 45 ; texte, ligne 959 : à mesurer)
mer = 1.0                          # h de mise en route (S)
ident = 6 * 3 / 60                 # h : 6 adaptateurs x 3 min (S)
relu, borne, stock = 1.1833, 1.30, 0.08   # USD/h (dépenses, ligne 515 ; configuration, lignes 41 et 115)
pire = borne + stock               # 1,38
tel_b, tel_h = 1.0, 2.0            # USD par mise en route (20 à 40 Go x 0,05)

# Ligne 1 : 16 x 8 = 128 épisodes des tâches de fabrication
H1_b, H1_h = h(128 * ep_b) + mer, h(128 * ep_h) + mer
A1_b, A1_h = H1_b * relu + tel_b, H1_h * borne + tel_h
P1 = H1_h * 4 * pire + 4
print(f"L1 : {H1_b:.4f} à {H1_h:.4f} h ; attendu {A1_b:.4f} à {A1_h:.4f} ; pire {P1:.4f} -> {math.ceil(P1)} ; sans relance {2*H1_h:.4f} h")

# Ligne 2 : 6 x 384 pas ; 6 contrôles ; 7 x 128 épisodes ; 5 x 128 x 2 passes
H2_b = mer + h(2304 * dist_b) + ident + h(896 * ep_b) + h(1280 * prise)
H2_h = mer + h(2304 * dist_h) + ident + h(896 * ep_h) + h(1280 * prise)
A2_b, A2_h = H2_b * relu + tel_b, H2_h * borne + tel_h
R2 = H2_h * 4 * pire + 4
print(f"L2 : {H2_b:.4f} à {H2_h:.4f} h ; attendu {A2_b:.4f} à {A2_h:.4f} ; repli {R2:.4f} -> 85")
k = ident + h(2304 * 6.0) + h(1280 * 0.90)          # pas et passe doublés
P2 = lambda d, m=1.0: 2 * pire * (max(1.0, m) + k + 896 * d / 3600) + 4
for d in (40.0, 42.8, 45.0):
    print(f"  d = {d} : H2 = {max(1.0,1.0)+k+896*d/3600:.4f} h ; P2 = {P2(d):.4f} -> {math.ceil(P2(d))}")
print(f"  constante {k:.4f} ; coefficient {896/3600:.6f} ; P2 = 85 pour d = {((85-4)/(2*pire)-1.0-k)/(896/3600):.2f} s")

# Totaux et comparaison à la v2
print(f"Deux lignes : {H1_b+H2_b:.4f} à {H1_h+H2_h:.4f} h ; attendu {A1_b+A2_b:.4f} à {A1_h+A2_h:.4f}")
print(f"v2, ligne 2 recalculée : P2(40) = {2*pire*(1.3+h(2304*6.0)+768*40/3600)+4:.4f} ; P2(45) = {2*pire*(1.3+h(2304*6.0)+768*45/3600)+4:.4f}")

# Hors de ce devis, ordre de grandeur (S) : deux moniteurs, 6 400 lectures chacun, une lecture = une action de l'agent
Hm_b, Hm_h = h(12800 * ep_b / 10) + mer, h(12800 * ep_h / 10) + mer
print(f"Moniteurs (S) : {Hm_b:.4f} à {Hm_h:.4f} h ; attendu {Hm_b*relu+tel_b:.4f} à {Hm_h*borne+tel_h:.4f}")
lect = 255.0                       # devis des lectures hors carte, brouillon 3, section 0, point 1
print(f"Carte + lectures : {A1_b+A2_b+lect:.2f} à {A1_h+A2_h+lect:.2f} ; avec les moniteurs (S) : {A1_b+A2_b+lect+Hm_b*relu+tel_b:.2f} à {A1_h+A2_h+lect+Hm_h*borne+tel_h:.2f}")

# Décision 4 : un adaptateur de plus (distillation, contrôle, rejeu de 128 épisodes)
un_b = h(384 * dist_b) + 3 / 60 + h(128 * ep_b)
un_h = h(384 * dist_h) + 3 / 60 + h(128 * ep_h)
print(f"Trois adaptateurs de plus : {3*un_b:.4f} à {3*un_h:.4f} h ; {3*un_b*relu:.4f} à {3*un_h*borne:.4f} USD")
