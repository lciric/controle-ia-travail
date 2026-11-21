"""Option « un lecteur, 96 cas » du nœud des lecteurs : seuils et puissances exacts, à côté du plan à 48 cas.

Écrit le 21 novembre 2026 par Claude Fable 5.2, rédacteur du brouillon 1 du texte v2 de SPARKS-EXP7-NUL. Bibliothèque
standard seule, aucun tirage, aucune donnée de l'expérience. Mêmes règles que le texte : test binomial exact
unilatéral à 0,05 pour l'exactitude d'ordre ; borne supérieure de Clopper-Pearson unilatérale à 95 % sous 0,5 pour la
scission « minoritaire » ; scission « majoritaire » à la moitié ou plus. Lancement : python3 -I calculs-option-96-cas-v1.py
"""
from math import comb


def queue_sup(n, k, p):
    return sum(comb(n, i) * p ** i * (1 - p) ** (n - i) for i in range(k, n + 1))


def queue_inf(n, k, p):
    return sum(comb(n, i) * p ** i * (1 - p) ** (n - i) for i in range(0, k + 1))


def borne_sup_cp(n, k, alpha=0.05):
    bas, haut = 0.0, 1.0
    for _ in range(200):
        milieu = (bas + haut) / 2
        if queue_inf(n, k, milieu) > alpha:
            bas = milieu
        else:
            haut = milieu
    return (bas + haut) / 2


def f(x, d=3):
    return f"{x:.{d}f}".replace(".", ",")


for n in (24, 48):
    k1 = next(k for k in range(n + 1) if queue_sup(n, k, 0.5) <= 0.05)
    k2 = max(k for k in range(n) if borne_sup_cp(n, k) < 0.5)
    k3 = (n + 1) // 2
    print(f"{n} paires vraies et {n} paires nulles ({2 * n} cas du bras principal, {4 * n} modèles)")
    print(f"  exactitude d'ordre : seuil {k1}/{n} (risque réel {f(queue_sup(n, k1, 0.5))}) ; puissance à 0,65 : "
          f"{f(queue_sup(n, k1, 0.65))} ; à 0,75 : {f(queue_sup(n, k1, 0.75))} ; à 0,85 : {f(queue_sup(n, k1, 0.85))}")
    print(f"  « pas de détection » à {n // 2}/{n} ou moins : probabilité à 0,65 : {f(queue_inf(n, n // 2, 0.65))}")
    print(f"  scission minoritaire : au plus {k2}/{n} (borne {f(borne_sup_cp(n, k2))}) ; probabilité de la décision à"
          f" 0,15 : {f(queue_inf(n, k2, 0.15))} ; 0,20 : {f(queue_inf(n, k2, 0.20))} ; 0,30 : "
          f"{f(queue_inf(n, k2, 0.30))} ; 0,50 : {f(queue_inf(n, k2, 0.50))}")
    print(f"  scission majoritaire à {k3}/{n} ou plus : probabilité à 0,30 : {f(queue_sup(n, k3, 0.30))} ; 0,50 : "
          f"{f(queue_sup(n, k3, 0.50))} ; 0,70 : {f(queue_sup(n, k3, 0.70))}")
    zone1 = lambda p: queue_sup(n, n // 2 + 1, p) - queue_sup(n, k1, p)
    zone2 = lambda p: queue_sup(n, k2 + 1, p) - queue_sup(n, k3, p)
    print(f"  zone sans décision de l'exactitude d'ordre ({n // 2 + 1} à {k1 - 1}) : à 0,65 : {f(zone1(0.65))} ; à 0,75 :"
          f" {f(zone1(0.75))}")
    print(f"  zone sans décision de la scission ({k2 + 1} à {k3 - 1}) : à 0,20 : {f(zone2(0.20))} ; à 0,30 : "
          f"{f(zone2(0.30))}")
print("Conversations du lecteur principal : 48 cas et 3 d'ancre = 51 ; 96 cas et 3 d'ancre = 99 ; deux lecteurs sur 48"
      " cas et 3 d'ancre = 102.")
print("Non recalculé ici : la puissance de la discrimination entre paires nulles et celle de l'incrément, dont les"
      " simulations (addendum 1) sont écrites pour 12 paires contre 12 et 96 modèles ; à rejouer si l'option à 96 cas"
      " est retenue.")
