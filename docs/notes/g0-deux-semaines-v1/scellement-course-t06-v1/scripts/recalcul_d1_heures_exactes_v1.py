"""Recalcule les chiffres que le couple D1 inscrit au devis v3 (P4' à la borne, marge, seuils de durée de la H200 NVL pour P4'
et P3'), sous les deux conventions d'heures : celle du script cité par D1 (`recalcul_devis_v3_v1.py` de la contre-lecture :
hôte lent = 2 x 17,9 h, heures arrondies) et celle qu'écrit D1 (« heures exactes », 2 x 17,98 h). Mêmes formules et mêmes
grandeurs que ce script (lignes 39 à 63) ; n'écrit rien, imprime les deux variantes. Bibliothèque standard seule.

Usage : python -I -B recalcul_d1_heures_exactes_v1.py
"""
PLAFOND, BB, DISQUE, TEL = 200.0, 1.61, 72 * 0.08, 2
DIVERS = 0.10 + 0.02 + 67 / 60 * 1.02 + 20 / 60 + 0.25
H_MAX_EXACT = 3.57 + 6.43 + 6.14 + DIVERS
for nom, h_max in (("script cité (2 x 17,9 h)", 17.9), (f"heures exactes (2 x {H_MAX_EXACT:.3f} h)", H_MAX_EXACT)):
    lent = 2 * h_max
    calc_p3 = (lent + BB) * 4.70
    p3, p4 = calc_p3 + DISQUE + TEL, 9.1 * 1.30 + 2.3 + calc_p3 + DISQUE + TEL
    f_p4 = (PLAFOND - (9.1 * 1.30 + 2.3 + DISQUE + TEL)) / calc_p3
    f_p3 = (PLAFOND - DISQUE - TEL) / calc_p3
    print(f"{nom} : P3' borne {p3:.1f} USD ; P4' borne {p4:.1f} USD, marge {PLAFOND - p4:.1f} USD ; P4' > 200 USD dès "
          f"{100 * (f_p4 - 1):.1f} % de temps de plus sur H200 NVL ; P3' dès {100 * (f_p3 - 1):.1f} %")
