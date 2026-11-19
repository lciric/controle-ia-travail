"""Vérification exacte des lois nulles du W de Kendall citées par le brouillon 5 (bloc P-019) — v1.

Trois juges (k = 3) classés par m évaluateurs ; sous le nul, chaque évaluateur tire un des six ordres au hasard.
W = 12 S / (m^2 (k^3 - k)), S = somme sur les juges des carrés des écarts des sommes de rangs à m(k+1)/2.
Énumération complète des 6^m affectations, fractions exactes. Aucun tirage, aucune donnée lue.
Lancement : python3 -I -B verifier_kendall_C_P3_v1.py > verifier_kendall_C_P3_v1.txt
"""
from fractions import Fraction
from itertools import permutations, product
import sys

K = 3
ORDRES = list(permutations(range(1, K + 1)))


def loi_w(m):
    compte = {}
    for aff in product(ORDRES, repeat=m):
        sommes = [sum(o[j] for o in aff) for j in range(K)]
        centre = Fraction(m * (K + 1), 2)
        s = sum((Fraction(r) - centre) ** 2 for r in sommes)
        w = Fraction(12) * s / (m * m * (K ** 3 - K))
        compte[w] = compte.get(w, 0) + 1
    return compte, len(ORDRES) ** m


def queue_haute(compte, total, w0):
    return Fraction(sum(c for w, c in compte.items() if w >= w0), total)


def queue_basse(compte, total, w0):
    return Fraction(sum(c for w, c in compte.items() if w <= w0), total)


print(f"python {sys.version.split()[0]} ; fractions exactes ; k = {K} juges")
for m in (3, 4, 5):
    compte, total = loi_w(m)
    esp = sum(w * c for w, c in compte.items()) / total
    print(f"\nm = {m} évaluateurs : {total} affectations ; espérance de W sous le nul = {esp} = {float(esp):.4f}")
    for w in sorted(compte):
        p = queue_haute(compte, total, w)
        print(f"  W = {str(w):>6} ({float(w):.4f}) : effectif {compte[w]:>5} ; P(W >= w) = {float(p):.4f}")
    seuil = min(w for w in compte if queue_haute(compte, total, w) <= Fraction(5, 100))
    print(f"  plus petit W de valeur p exacte <= 0,05 : {seuil} ({float(seuil):.4f}) ; p = "
          f"{float(queue_haute(compte, total, seuil)):.4f}")
    print(f"  P(W <= espérance) sous le nul = {float(queue_basse(compte, total, esp)):.4f}")
