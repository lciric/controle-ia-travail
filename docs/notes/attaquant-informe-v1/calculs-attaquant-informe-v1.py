#!/usr/bin/env python3
"""Calculs de la note « attaquant informé » (v1). Bibliothèque standard seule, aucun tirage,
aucune donnée du programme. Toutes les valeurs d'entrée sont des suppositions d'illustration.
Rejouer : python3 calculs-attaquant-informe-v1.py > calculs-attaquant-informe-v1.txt
"""
import math
from statistics import NormalDist

Z = NormalDist()

print("[A] Du seuil toléré au taux d'audit (dommage « de signature » : l'honnête ne le produit jamais,")
print("    un seul épisode endommagé reconnu suffit). K = nombre d'épisodes endommagés tolérés avant l'alerte ;")
print("    q = probabilité que l'oracle reconnaisse un dommage qu'il regarde ; L = épisodes endommagés produits")
print("    pendant le délai de l'oracle et de la réponse. Plus petit taux d'audit p tel que la prise survienne")
print("    au plus tard au (K - L)e épisode endommagé avec probabilité 0,95 : p = (1 - 0,05^(1/(K-L))) / q.")
for K in (30, 100, 300, 1000):
    for q in (1.0, 0.5):
        for L in (0, 20):
            if K - L <= 0:
                print(f"    K = {K:5d}, q = {q:.1f}, L = {L:3d} : impossible (le délai dépasse le seuil)")
                continue
            p = (1 - 0.05 ** (1 / (K - L))) / q
            txt = f"{p:.4f}" if p <= 1 else "impossible (taux > 1)"
            print(f"    K = {K:5d}, q = {q:.1f}, L = {L:3d} : p minimal = {txt}")

print()
print("[B] Dommage « d'excès » : l'honnête produit aussi ce dommage, au taux d0 ; le saboteur l'élève de eps.")
print("    Test unilatéral au niveau 1 % sur les n = p N épisodes audités (approximation normale, déclarée).")
print("    Excès de taux que le test ne voit qu'une fois sur deux : eps* = z_0,99 sqrt(d0 (1 - d0) / (p N)).")
print("    Épisodes endommagés en excès sur l'horizon, à ce taux : eps* N = z_0,99 sqrt(d0 (1 - d0) N / p).")
z = Z.inv_cdf(0.99)
for d0 in (0.10, 0.01):
    for N in (1000, 10000, 100000):
        for p in (0.05, 0.20, 1.00):
            eps = z * math.sqrt(d0 * (1 - d0) / (p * N))
            print(f"    d0 = {d0:.2f}, N = {N:6d}, p = {p:.2f} : eps* = {eps:.4f} ; épisodes en excès non vus = {eps * N:7.1f}"
                  f" ; part de l'horizon = {eps:.4f}")

print()
print("[C] Audit selon l'enjeu. Types d'épisodes : part f, enjeu s (dommage possible, défini par le défenseur).")
print("    Un saboteur qui n'attaque que le type i cause en moyenne s_i / pi_i de dommage jusqu'à sa première prise")
print("    (prise comprise), pi_i étant la probabilité d'audit de ce type. Budget moyen d'audit : somme f_i pi_i = p.")
types = [(0.90, 1.0), (0.09, 5.0), (0.01, 25.0)]
moy = sum(f * s for f, s in types)
for p in (0.01, 0.02, 0.05):
    print(f"    budget p = {p:.2f} ; enjeu moyen = {moy:.2f} ; enjeu maximal = {max(s for _, s in types):.0f}")
    pire_u = max(s / p for _, s in types)
    print(f"      audit uniforme            : dommage moyen avant prise, au pire type = {pire_u:8.1f}")
    pis = [p * s / moy for _, s in types]
    assert all(x <= 1 for x in pis) and abs(sum(f * x for (f, _), x in zip(types, pis)) - p) < 1e-12
    pire_e = max(s / x for (_, s), x in zip(types, pis))
    print(f"      audit proportionnel à l'enjeu : probabilités par type = "
          + ", ".join(f"{x:.4f}" for x in pis) + f" ; dommage moyen avant prise, tout type = {pire_e:8.1f}")
    print(f"      rapport = {pire_u / pire_e:.2f} (= enjeu maximal / enjeu moyen)")

print()
print("[D] Audit mixte : plancher au hasard pi_min sur tout épisode, le reste du budget suivant le soupçon.")
print("    Contre un saboteur qui n'endommage que des épisodes au soupçon le plus bas, seul le plancher compte :")
print("    prise avec probabilité 0,95 au plus tard au n-ième épisode endommagé, n = ceil(ln 0,05 / ln(1 - pi_min)).")
for pim in (0.0, 0.005, 0.01, 0.02, 0.05):
    if pim == 0:
        print("    pi_min = 0.000 (audit des seuls plus suspects) : jamais")
    else:
        n = math.ceil(math.log(0.05) / math.log(1 - pim))
        print(f"    pi_min = {pim:.3f} : n = {n}")

print()
print("[E] Fuite de la pièce d'audit (formule de l'article « Blindfold », p. 1 : biais au pire = (1 - eps) D_A,")
print("    eps = taux d'audit, D_A = distance en variation totale entre ce que l'agent voit selon la pièce).")
for eps in (0.01, 0.05, 0.20):
    for DA in (0.0, 0.05, 0.50, 1.0):
        print(f"    eps = {eps:.2f}, D_A = {DA:.2f} : biais au pire du taux certifié = {(1 - eps) * DA:.4f}")
