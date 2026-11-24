"""Dénombrement exact pour l'épreuve des rangs signés, sans ex aequo (aucune donnée, aucun résultat).

Pour n familles, nombre de sous-ensembles de {1, …, n} dont la somme vaut au plus w : la valeur p bilatérale exacte
d'une somme des rangs contraires égale à w est 2 × ce nombre / 2^n. Le programme rend, pour chaque n, la plus grande
somme des rangs contraires qui passe à 99 % et à 95 % bilatéral, et la borne (1/2)^n.
Emploi : python3 denombrement-rangs-signes-v1.py SORTIE.json
"""
import json
import sys


def comptes(n):
    c = [0] * (n * (n + 1) // 2 + 1)
    c[0] = 1
    for r in range(1, n + 1):
        for s in range(len(c) - 1, r - 1, -1):
            c[s] += c[s - r]
    return c


def seuil(n, alpha):
    """Plus grande somme des rangs contraires w telle que la valeur p bilatérale exacte soit au plus alpha."""
    cumul, meilleur = 0, None
    for w, k in enumerate(comptes(n)):
        cumul += k
        if 2 * cumul / 2 ** n <= alpha:
            meilleur = {"somme_des_rangs_contraires_max": w, "p_bilaterale": 2 * cumul / 2 ** n}
    return meilleur


sortie = {str(n): {"p_bilaterale_minimale": 2 / 2 ** n, "niveau_99": seuil(n, 0.01), "niveau_95": seuil(n, 0.05),
                   "un_demi_puissance_n": 0.5 ** n} for n in range(5, 11)}
json.dump(sortie, open(sys.argv[1], "w"), indent=1, sort_keys=True)
for n, v in sortie.items():
    print(n, v)
