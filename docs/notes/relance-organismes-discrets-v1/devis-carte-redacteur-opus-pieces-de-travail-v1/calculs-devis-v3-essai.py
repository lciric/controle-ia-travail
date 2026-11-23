# Calculs du devis de carte v3 du bras A (C). Entrées : devis v2 section 2-3 (M/S), texte v2 6.11 (M), config de référence (M).
import math
ep_haut, ep_bas = 42.8, 40.2          # s par épisode (devis v2, section 2 ; autre chaîne)
pas_dist_haut, pas_dist_bas = 3.0, 2.1  # s par pas de distillation (devis v2, section 2 ; S)
passe_prise = 0.45                    # s par passe sur texte imposé (devis v2, section 2 ; texte v2 6.11 : à mesurer)
mise_en_route = 1.0                   # h (S)
ident = 6 * 3 / 60                    # h, contrôle d'identité, 6 adaptateurs x 3 min (S)
prix_relu, prix_borne, stock = 1.1833, 1.30, 0.08
pire_prix = prix_borne + stock        # 1,38
tel_bas, tel_haut = 1.0, 2.0          # USD par mise en route (20 à 40 Go x 0,05)

def h(x): return x / 3600
print("=== Ligne 1 : 16 tâches de fabrication x 8 = 128 épisodes ===")
n1 = 16 * 8
e1_h, e1_b = h(n1 * ep_haut), h(n1 * ep_bas)
H1_h, H1_b = e1_h + mise_en_route, e1_b + mise_en_route
print(f"épisodes : {e1_b:.4f} à {e1_h:.4f} h ; total {H1_b:.4f} à {H1_h:.4f} h")
a1_b, a1_h = H1_b * prix_relu, H1_h * prix_borne
print(f"calcul attendu : {a1_b:.4f} à {a1_h:.4f} USD ; avec téléchargement {a1_b+tel_bas:.4f} à {a1_h+tel_haut:.4f}")
p1 = H1_h * 4 * pire_prix + 4
print(f"pire cas : {H1_h:.4f} x 4 = {H1_h*4:.4f} h x 1,38 = {H1_h*4*pire_prix:.4f} + 4 = {p1:.4f} -> plafond {math.ceil(p1)}")
print(f"pire cas sans relance (débit deux fois plus lent) : {2*H1_h:.4f} h")

print("=== Ligne 2 : distillation, identité, rejeu des sept conditions, prise ===")
n_pas = 6 * 384
d_h, d_b = h(n_pas * pas_dist_haut), h(n_pas * pas_dist_bas)
n2 = 7 * 128
r_h, r_b = h(n2 * ep_haut), h(n2 * ep_bas)
n_prise = 5 * 128 * 2
pr = h(n_prise * passe_prise)
H2_h = mise_en_route + d_h + ident + r_h + pr
H2_b = mise_en_route + d_b + ident + r_b + pr
print(f"distillation {n_pas} pas : {d_b:.4f} à {d_h:.4f} h ; identité {ident:.4f} h ; rejeu {n2} épisodes : {r_b:.4f} à {r_h:.4f} h ; prise {n_prise} passes : {pr:.4f} h")
print(f"total {H2_b:.4f} à {H2_h:.4f} h")
a2_b, a2_h = H2_b * prix_relu, H2_h * prix_borne
print(f"calcul attendu : {a2_b:.4f} à {a2_h:.4f} USD ; avec téléchargement {a2_b+tel_bas:.4f} à {a2_h+tel_haut:.4f}")
p2r = H2_h * 4 * pire_prix + 4
print(f"repli sans mesure : {H2_h:.4f} x 4 = {H2_h*4:.4f} h x 1,38 = {H2_h*4*pire_prix:.4f} + 4 = {p2r:.4f}")
# Plafond recalculé : d mesuré ; pas de distillation doublé 6,0 s ; passe de prise doublée 0,90 s ; m = max(1,0 ; mise en route mesurée)
const = ident + h(n_pas * 6.0) + h(n_prise * 0.90)
coef = n2 / 3600
print(f"H2(d, m) = m + {const:.4f} + {coef:.6f} x d  (avec m = 1,0 : {1.0+const:.4f} + {coef:.6f} d)")
for d in (40.0, 42.8, 45.0):
    H2 = 1.0 + const + coef * d
    P2 = 2 * pire_prix * H2 + 4
    print(f"  d = {d} s : H2 = {H2:.4f} h ; P2 = 2 x 1,38 x H2 + 4 = {P2:.4f} -> {math.ceil(P2)}")
# seuil de d au-delà duquel P2 dépasse le plafond de repli de 85
d_seuil = ((85 - 4) / (2 * pire_prix) - (1.0 + const)) / coef
print(f"d au-delà duquel P2(d, 1,0) > 85 : {d_seuil:.2f} s")
# v2, pour comparaison
H2v2 = lambda d: 1.0 + 0.30 + 768 * d / 3600 + 2304 * 6.0 / 3600
print(f"v2 : H2(40) = {H2v2(40):.4f}, P2 = {2*pire_prix*H2v2(40)+4:.4f} ; H2(45) = {H2v2(45):.4f}, P2 = {2*pire_prix*H2v2(45)+4:.4f}")

print("=== Totaux ===")
print(f"heures : {H1_b+H2_b:.4f} à {H1_h+H2_h:.4f}")
print(f"attendu avec téléchargement : {a1_b+tel_bas+a2_b+tel_bas:.4f} à {a1_h+tel_haut+a2_h+tel_haut:.4f}")
print(f"plafonds : sans mesure {math.ceil(p1)} + 85 = {math.ceil(p1)+85} ; avec mesure {math.ceil(p1)} + 47 à 50")

print("=== Écart à la v2 ===")
print(f"v2 ligne 1 : 256 épisodes -> {h(256*ep_bas)+1:.4f} à {h(256*ep_haut)+1:.4f} h")
print(f"v2 ligne 2 : {1.0 + h(n_pas*pas_dist_bas) + ident + h(768*ep_bas):.4f} à {1.0 + h(n_pas*pas_dist_haut) + ident + h(768*ep_haut):.4f} h")
print(f"128 épisodes déplacés de la ligne 1 à la ligne 2 : {h(128*ep_bas):.4f} à {h(128*ep_haut):.4f} h")

print("=== Ordre de grandeur, moniteurs à modèle de langue (S : une lecture = le temps d'une action de l'agent) ===")
t_lect = ep_haut / 10
for n in (6400, 12800):
    print(f"  {n} lectures x {t_lect:.2f} s = {h(n*t_lect):.4f} h")
Hm = h(12800 * t_lect) + mise_en_route
Hm_b = h(12800 * ep_bas / 10) + mise_en_route
print(f"  avec une mise en route : {Hm_b:.4f} à {Hm:.4f} h ; attendu {Hm_b*prix_relu+tel_bas:.4f} à {Hm*prix_borne+tel_haut:.4f} USD ; règle du pire cas : {Hm*4*pire_prix+4:.4f}")

print("=== Variantes de la décision sur les deux points appliqués par anticipation ===")
par_adapt_h = h(384 * pas_dist_haut) + 3/60 + h(128 * ep_haut) + h(128 * 2 * passe_prise)
par_adapt_b = h(384 * pas_dist_bas) + 3/60 + h(128 * ep_bas) + h(128 * 2 * passe_prise)
print(f"un adaptateur de plus (distillation, identité, rejeu, prise) : {par_adapt_b:.4f} à {par_adapt_h:.4f} h ; {par_adapt_b*prix_relu:.4f} à {par_adapt_h*prix_borne:.4f} USD")
print(f"trois de plus (témoin bénin à chaque dose) : {3*par_adapt_b:.4f} à {3*par_adapt_h:.4f} h ; {3*par_adapt_b*prix_relu:.4f} à {3*par_adapt_h*prix_borne:.4f} USD")

print("=== Total de la course, pour mémoire (hors carte cité seulement) ===")
lect = 255.0                # devis des lectures hors carte, brouillon 3, section 0, point 1 (avec la révision)
lect_sans = (218.0, 222.0)  # même endroit, sans la révision
carte_b, carte_h = a1_b + tel_bas + a2_b + tel_bas, a1_h + tel_haut + a2_h + tel_haut
mon_b, mon_h = Hm_b * prix_relu + tel_bas, Hm * prix_borne + tel_haut
print(f"carte : {carte_b:.2f} à {carte_h:.2f}")
print(f"carte + lectures (avec révision) : {carte_b+lect:.2f} à {carte_h+lect:.2f}")
print(f"carte + lectures (sans révision) : {carte_b+lect_sans[0]:.2f} à {carte_h+lect_sans[1]:.2f}")
print(f"+ moniteurs (S) : {carte_b+lect+mon_b:.2f} à {carte_h+lect+mon_h:.2f}")
print(f"plafonds carte + lectures : {18+47+670} à {18+50+670} (sur débit mesuré) ; {18+85+670} sans mesure")
print("=== Ce qu'épargne l'arrêt d'office (carte) ===")
print(f"ligne 2 : {H2_b:.2f} à {H2_h:.2f} h ; {a2_b+tel_bas:.2f} à {a2_h+tel_haut:.2f} USD")
print(f"plancher de 80 sur le cas complet de 640 : {80/640:.4f}")
