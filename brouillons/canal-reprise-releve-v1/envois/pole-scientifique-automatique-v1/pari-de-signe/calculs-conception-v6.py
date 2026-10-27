"""Calculs exacts cités par la conception v6 du pari apparié borné (aucun tirage, aucune graine).

1. Section 6 : nombre minimal d'unités à v = 1 pour atteindre le seuil m/α, à m = 1 (seuil 20) et m = 3 (seuil 60),
   mélange sur Λ = {0,1 ; 0,3 ; 0,6 ; 0,9}.
2. D-S24 : suite 6/(π²g²) contre l'uniforme α/G_max (G_max = 10 et 30) : première génération où l'uniforme donne plus.
3. Seuils des fiches nouvelles à m = 3 aux générations 1, 3, 10, 30 sous les deux suites.

Lancement : /opt/venv-essaim-sim-v1/bin/python -I -B calculs-conception-v6.py > calculs-conception-v6-sortie.json
"""

import json
import math
import platform
import sys

LAMBDAS = (0.1, 0.3, 0.6, 0.9)
ALPHA = 0.05


def richesse(n, v):
    return sum((1 + l * v) ** n for l in LAMBDAS) / len(LAMBDAS)


def alpha_g(g):
    return ALPHA * 6 / (math.pi ** 2 * g * g)


def main():
    sortie = {"manifeste": {"script": "calculs-conception-v6.py", "python": sys.version.split()[0],
                            "plateforme": platform.platform(), "grille": list(LAMBDAS), "alpha": ALPHA,
                            "tirages": "aucun"}}
    s6 = {}
    for m in (1, 3):
        seuil = m / ALPHA
        n = next(n for n in range(1, 1000) if richesse(n, 1.0) >= seuil)
        s6[f"m={m}"] = {"seuil": seuil, "unites_minimales_a_v=1": n,
                        "richesse_a_n-1": round(richesse(n - 1, 1.0), 2), "richesse_a_n": round(richesse(n, 1.0), 2)}
    sortie["section_6_unites_minimales"] = s6
    d24 = {"alpha_g_6/(pi2g2)": {str(g): round(alpha_g(g), 6) for g in (1, 2, 3, 4, 5, 10, 30)},
           "part_de_alpha_a_g=1": round(alpha_g(1) / ALPHA, 4)}
    for gmax in (10, 30):
        u = ALPHA / gmax
        premiere = next(g for g in range(1, gmax + 1) if u > alpha_g(g))
        d24[f"G_max={gmax}"] = {"uniforme": round(u, 6), "premiere_generation_ou_l_uniforme_donne_plus": premiere,
                                "alpha_g_a_cette_generation": round(alpha_g(premiere), 6)}
    d24["seuils_m=3"] = {str(g): {"6/(pi2g2)": round(3 / alpha_g(g), 1), "uniforme_G_max=10": (round(3 / (ALPHA / 10), 1) if g <= 10 else None),
                                   "uniforme_G_max=30": round(3 / (ALPHA / 30), 1)} for g in (1, 3, 10, 30)}
    sortie["D-S24_suites_de_depense"] = d24
    json.dump(sortie, sys.stdout, ensure_ascii=False, indent=1)
    print()


if __name__ == "__main__":
    main()
