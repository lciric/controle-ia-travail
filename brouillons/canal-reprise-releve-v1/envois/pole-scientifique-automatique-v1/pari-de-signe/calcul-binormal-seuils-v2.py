"""Bruit de calibrage des seuils, calcul binormal (pas de simulation) — pièce jointe de la conception v2 du pari apparié
borné (constat C2 de la contre-lecture). Scores honnêtes N(0, 1), sabotés N(d', 1) ; seuil = quantile empirique (1 − τ)
de N = C·m scores honnêtes ; écart-type asymptotique du quantile : sqrt(τ(1 − τ)/N)/φ(z_τ) ; pente du rappel par unité
de seuil : φ(z_τ − d') ; écart vrai de rappel entre deux moniteurs de même loi calibrés séparément : × sqrt(2).

Usage : python -I -B calcul-binormal-seuils-v2.py
"""

import math


def phi(x):
    return math.exp(-x * x / 2) / math.sqrt(2 * math.pi)


def quantile_normal(p):
    """Inverse de Φ par bissection (sans scipy)."""
    lo, hi = -10.0, 10.0
    for _ in range(200):
        mid = (lo + hi) / 2
        if 0.5 * math.erfc(-mid / math.sqrt(2)) < p:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def principal():
    m = 10
    print("tau ; rappel vrai ; d' ; pente rappel/faux positifs ; C (tâches honnêtes de 10 épisodes) ; écart-type de l'écart "
          "vrai de rappel entre jumeaux (points) ; écart-type de l'asymétrie vraie de faux positifs (points)")
    for tau in (0.01, 0.05):
        z = quantile_normal(1 - tau)
        for rappel in (0.40, 0.80):
            d = z - quantile_normal(1 - rappel)
            pente_roc = phi(z - d) / phi(z)
            for C in (45, 200, 500, 1000, 4000):
                N = C * m
                et_seuil = math.sqrt(tau * (1 - tau) / N) / phi(z)
                et_rappel = math.sqrt(2) * phi(z - d) * et_seuil
                et_fp = math.sqrt(2) * phi(z) * et_seuil
                print(f"{tau:.2f} ; {rappel:.2f} ; {d:.2f} ; {pente_roc:.1f} ; {C} ; {100 * et_rappel:.1f} ; {100 * et_fp:.2f}")


if __name__ == "__main__":
    principal()
