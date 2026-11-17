"""Calculs du brouillon 4 du préenregistrement de la course à plusieurs générations (MR-2) — v1.

Aucun tirage, aucun monde, aucun appel : arithmétique sur des nombres cités de pièces scellées.
(1) Table des minimums de la ligne FD à la tolérance indicative de la v4 (36 fausses sur 204 retenues,
    conception v7 §4.4) : plus petit nombre de fausses découvertes k sur n retenues dont la borne basse
    de Wilson à 95 % dépasse tau (z = 1,959964), pour n dans {3, 5, 8, 10, 15, 20, 30}.
(2) Même table à la tolérance de la v3b (28 sur 181), pour mémoire (brouillon 3 §4.2).
(3) Coût par appel du proposeur le plus coûteux au pilote (verdict v2 du pilote, « Dépense rapprochée »
    et « Nœuds de Lazar ») : 10,019552 USD au total sur 4 appels, dont 5,585992 sur les 2 appels tronqués.
(4) Garde 30 au tiers (Q-12 (ii)) : seuil d'arrêt en entiers, « 3 x coupés > lancés », pour 1 à 37 tests lancés.
(5) Chance qu'au moins un des deux mondes de test porte une chaîne, part 2 sur 12 (conception v7 §4.4).
"""
import json
import math
import sys

Z = 1.959964


def wilson_basse(k, n, z=Z):
    if n == 0:
        return None
    p = k / n
    d = 1 + z * z / n
    c = p + z * z / (2 * n)
    r = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n))
    return (c - r) / d


def minimum_fd(tau, ns):
    sortie = {}
    for n in ns:
        k_min = None
        for k in range(0, n + 1):
            if wilson_basse(k, n) > tau:
                k_min = k
                break
        sortie[str(n)] = k_min
    return sortie


def essais():
    assert abs(wilson_basse(7, 16) - 0.2309) < 5e-4      # brouillon 3 §4.2 : monde 1, 7 sur 16, borne basse 0,23
    t = minimum_fd(28 / 181, [5, 10, 15, 20, 30])
    assert t == {"5": 3, "10": 4, "15": 6, "20": 7, "30": 9}, t   # table du brouillon 3 §4.2
    assert 3 * 12 <= 37 and 3 * 13 > 37                  # au-delà de 12 coupés sur 37 : arrêt


def main():
    essais()
    ns = [3, 5, 8, 10, 15, 20, 30]
    tau_v4 = 36 / 204
    tau_v3b = 28 / 181
    total, tronques = 10.019552, 5.585992
    sortie = {
        "tau_v4": round(tau_v4, 6),
        "minimum_fd_tau_v4": minimum_fd(tau_v4, ns),
        "tau_v3b": round(tau_v3b, 6),
        "minimum_fd_tau_v3b": minimum_fd(tau_v3b, ns),
        "cout_appel_proposeur_le_plus_couteux": {
            "complet_moyen_usd": round((total - tronques) / 2, 6),
            "tronque_moyen_usd": round(tronques / 2, 6),
        },
        "garde30_tiers": {str(t): next(c for c in range(0, t + 2) if 3 * c > t) for t in range(1, 38)},
        "chance_chaine_deux_mondes": round(1 - (10 / 12) ** 2, 4),
        "python": sys.version.split()[0],
    }
    print(json.dumps(sortie, ensure_ascii=False, indent=1, sort_keys=True))


if __name__ == "__main__":
    main()
