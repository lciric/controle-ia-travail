#!/usr/bin/env python3
"""Barreau 5 : devis de la formation à trois membres par famille d'apprentissage (39 adaptateurs), et marché du 19 novembre (v1).

Écrit par le rédacteur du plan (Claude Fable 5.2), le 19 novembre 2026. Aucune donnée du programme : mêmes débits et prix
que le calcul v2 (`calcul-devis-adaptateurs-tenus-a-l-ecart-v2.py`, chargé tel quel) et que le calcul v3 pour la relecture.
Famille d'apprentissage à trois membres : 160 épisodes, trois distillations, 64 épisodes d'évaluation (saboteur) et 32 pour
chacun des deux autres. Coupure : quatre cinquièmes du pire cas, arrondis à l'entier supérieur (règle que suivent les trois
coupures du devis du brouillon 3 : 26, 24, 15).
"""
import math, os, runpy

ICI = os.path.dirname(os.path.abspath(__file__))
V2 = runpy.run_path(os.path.join(ICI, "calcul-devis-adaptateurs-tenus-a-l-ecart-v2.py"), run_name="v2")
famille, usd, FIXE = V2["famille"], V2["usd"], V2["H_FIXE_FORMATION"]
TELECH_GO, TELECH = V2["TELECH_GO"], V2["TELECH"]


def instance(nom, familles):
    b = FIXE + sum(f[0] for f in familles); h = FIXE + sum(f[1] for f in familles)
    u = usd(b, h, 1)
    c = math.ceil(0.8 * u[2])
    marge = c / 1.30 - 0.25 - h                      # garde du code : heures avant la coupure au prix plafond, moins l'attendu haut
    print(f"{nom} : {b:.2f} à {h:.2f} h ; {u[0]:.1f} à {u[1]:.1f} USD ; pire {u[2]:.1f} ; coupure {c} ; "
          f"heures avant la coupure à 1,30 USD de l'heure moins l'attendu haut : {marge:+.2f}")
    return b, h, u, c


def main():
    fe, fa2, fa3 = famille(3, 96), famille(2, 96), famille(3, 128)
    print(f"famille tenue à l'écart {fe[0]:.2f} à {fe[1]:.2f} h ; d'apprentissage à deux membres {fa2[0]:.2f} à {fa2[1]:.2f} ; à trois membres {fa3[0]:.2f} à {fa3[1]:.2f}")
    print("# contrôle : les trois coupures du brouillon 3 par la même règle")
    t = instance("instances 1 à 5 (deux familles tenues à l'écart)", [fe, fe])
    instance("instance 6, deux membres", [fa2, fa2]); instance("instance 7, deux membres", [fa2])
    print("# 39 adaptateurs")
    i6 = instance("instance 6, trois membres", [fa3, fa3]); i7 = instance("instance 7, trois membres", [fa3])
    b = 5 * t[0] + i6[0] + i7[0]; h = 5 * t[1] + i6[1] + i7[1]
    ub = 5 * t[2][0] + i6[2][0] + i7[2][0]; uh = 5 * t[2][1] + i6[2][1] + i7[2][1]; up = 5 * t[2][2] + i6[2][2] + i7[2][2]
    coup = 5 * t[3] + i6[3] + i7[3]
    print(f"formation à 39 : {b:.1f} à {h:.1f} h de carte ; horloge {max(t[0], i6[0]):.1f} à {max(t[1], i6[1]):.1f} h ; {ub:.1f} à {uh:.1f} USD ; pire {up:.1f} ; somme des coupures {coup}")
    print(f"écart à 36 : +{b - 58.0:.1f} à +{h - 66.3:.1f} h ; +{ub - 72.2:.1f} à +{uh - 105.5:.1f} USD ; pire +{up - 210.3:.1f}")
    # relecture à 39 (formules du calcul v3)
    GO = 1.06 * 640 / 576
    for n in (36, 39):
        go = (n * 3 + 3 + 9) * GO
        fixe = 1.3 + 64 * 40.2 / 3600 + n * 84 / 3600 + 0.29 + 0.03 + 0.17
        lb = fixe + 0.25 + go * 1e9 / 100e6 / 3600; lh = fixe + 0.60 + go * 1e9 / 30e6 / 3600
        print(f"relecture à {n} adaptateurs : {go:.1f} Go ; {lb:.2f} à {lh:.2f} h ; {lb * 1.1189 + 40 * .026 + go * .026:.1f} à {lh * 1.38 + 40 * .05 + go * .05:.1f} USD ; "
              f"pire {2 * lh * 1.48 + 40 * .05 + go * .05:.1f}")
    print(f"somme des coupures à 39 : formation {coup} + relecture 20 + répétition 8 = {coup + 28} (plafond 200)")
    print("# marché du 19 novembre à 20:02Z : trois offres acceptées, 1,12 à 1,19 USD de l'heure ; stockage vu ≈ 0,041 USD de l'heure")
    for nom, hb, hh in (("36", 58.0, 66.3), ("39", b, h)):
        print(f"formation à {nom}, aux prix vus : {hb * (1.12 + 0.041) + 7 * TELECH_GO * TELECH[0]:.1f} à {hh * (1.19 + 0.041) + 7 * TELECH_GO * TELECH[1]:.1f} USD")
    print("# vagues de trois cartes, dans l'ordre 6, 1, 2 ; 3, 4, 5 ; 7 (chaque vague part quand la plus longue de la précédente finit)")
    for nom, i6h, i7h in (("36", (8.44, 9.36), (5.12, 5.58)), ("39", (i6[0], i6[1]), (i7[0], i7[1]))):
        v = [max(t[k], i6h[k]) + t[k] + i7h[k] for k in (0, 1)]
        print(f"  à {nom} : horloge {v[0]:.1f} à {v[1]:.1f} h en trois vagues strictes ; avec quatre cartes (6, 1, 2, 3 ; 4, 5, 7) : {max(t[0], i6h[0]) + t[0]:.1f} à {max(t[1], i6h[1]) + t[1]:.1f} h")


if __name__ == "__main__":
    main()
