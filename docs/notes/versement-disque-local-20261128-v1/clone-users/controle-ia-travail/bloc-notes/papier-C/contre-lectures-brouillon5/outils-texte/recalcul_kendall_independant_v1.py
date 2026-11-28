"""Recalcul indépendant (entiers) des queues du W de Kendall pour 3 objets classés par m évaluateurs.
W = 12 S / (m^2 (k^3 - k)) ; avec k = 3 : W = S / (2 m^2), S = somme des (R_j - 2m)^2.
Usage : python3 -I -B recalcul_kendall_independant_v1.py"""
from itertools import permutations, product
ordres = list(permutations((1, 2, 3)))
for m, w0 in ((3, 1.0), (4, 0.8125), (5, 0.64)):
    n = tot = bas = 0
    for aff in product(ordres, repeat=m):
        r = [sum(o[j] for o in aff) for j in range(3)]
        s = sum((x - 2 * m) ** 2 for x in r)
        # W >= w0  <=>  s >= w0 * 2 m^2 (comparaison en entiers via 10000)
        tot += 1
        n += s * 10000 >= round(w0 * 10000) * 2 * m * m
        bas += s * m <= 2 * m * m  # W <= 1/m  <=>  s/(2m^2) <= 1/m  <=>  s*m <= 2m^2
    print(f"m={m} : P(W >= {w0}) = {n}/{tot} = {n/tot:.4f} ; P(W <= 1/m, espérance sous le nul) = {bas}/{tot} = {bas/tot:.4f}")
