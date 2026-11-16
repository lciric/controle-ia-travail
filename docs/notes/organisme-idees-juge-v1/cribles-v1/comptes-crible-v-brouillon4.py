"""Comptes exacts du crible (v), brouillon 4 : chiffres que le tour 3 de contre-lecture demande « à refaire par programme et à
recopier en annexe » (aucune donnée, aucun tirage, aucun appel, aucune lecture du pilote).

1. Seuil W_min(n) : plus petit W dont la borne basse de Clopper-Pearson à 95 % bilatéral (W sur n) dépasse 0,05, n = 16 à 24.
2. Puissance : probabilité d'une « perte établie » (au moins W_min pertes) quand m mondes sont à risque, chacun perdant avec la
   probabilité p (loi binomiale exacte) : N = 20 (W_min = 4 ; m = 20 et m = 17) et N = 24 (W_min = 5 ; m = 24 et m = 21).
3. Épargne : S(k) = f × (N − k) / N, f = part de la moitié chère dans le coût des proposeurs (0,71 et 0,75, valeurs de la section
   « Seuil »), calcul en fractions exactes ; plus grand k avec S(k) ≥ 0,25.
4. Monde complet (au moins un appel répondu dans chaque moitié de deux appels) et monde à quatre appels, pour un taux d'appels
   répondus r d'une grille écrite d'avance (aucun taux du pilote) ; probabilité d'atteindre le minimum 0,8 × N (16 sur 20 ; 20 sur 24).
5. Devis au pire à N = 24 (plafonds de session du bloc gelé du pilote : Pr-1 2,34 ; Pr-2 2,00 ; Pr-3 2,34 ; Pr-4 3,00 ; machine 3,00).
Bibliothèque standard seule. Usage : python3 -I comptes-crible-v-brouillon4.py
"""
from fractions import Fraction as F
from math import comb


def queue_haute(n, p, w):
    """P(Bin(n, p) >= w)."""
    return sum(comb(n, i) * p ** i * (1 - p) ** (n - i) for i in range(w, n + 1))


def borne_basse_cp(x, n, alpha=0.05):
    """Borne basse de Clopper-Pearson : p tel que P(Bin(n, p) >= x) = alpha / 2 (bissection, 200 itérations)."""
    if x == 0:
        return 0.0
    bas, haut = 0.0, 1.0
    for _ in range(200):
        mil = (bas + haut) / 2
        if queue_haute(n, mil, x) < alpha / 2:
            bas = mil
        else:
            haut = mil
    return (bas + haut) / 2


print("1. W_min(n) : plus petit W dont la borne basse de Clopper-Pearson (95 % bilatéral) dépasse 0,05")
wmin = {}
for n in range(16, 25):
    w = next(w for w in range(0, n + 1) if borne_basse_cp(w, n) > 0.05)
    wmin[n] = w
    print(f"  n = {n} : W >= {w} (borne basse {borne_basse_cp(w, n):.4f} ; à W - 1 : {borne_basse_cp(w - 1, n):.4f})")

print("2. Probabilité d'une perte établie (loi binomiale exacte)")
for N, risque in ((20, (20, 17)), (24, (24, 21))):
    W = wmin[N]
    for m in risque:
        ligne = " ; ".join(f"p = {p:.2f} : {queue_haute(m, p, W):.4f}" for p in (0.10, 0.15, 0.20, 0.26, 0.35))
        print(f"  N = {N}, W >= {W}, {m} mondes à risque : {ligne}")

print("3. Épargne S(k) = f (N - k) / N, fractions exactes ; plus grand k avec S(k) >= 0,25")
for N in (20, 24):
    for f in (F(71, 100), F(75, 100)):
        kmax = max(k for k in range(0, N + 1) if f * (N - k) / N >= F(1, 4))
        s1 = f * (N - kmax) / N
        s2 = f * (N - kmax - 1) / N
        print(f"  N = {N}, f = {float(f):.2f} : S >= 0,25 ssi k <= {kmax} (S({kmax}) = {float(s1):.4f} ; "
              f"S({kmax + 1}) = {float(s2):.4f}) ; « pas d'épargne notable » ssi k >= {kmax + 1}")

print("4. Monde complet et minimum de mondes complets, grille de taux d'appels répondus r (aucun taux du pilote)")
for r in (0.70, 0.75, 0.80, 0.85, 0.90, 0.95, 1.00):
    q = (1 - (1 - r) ** 2) ** 2
    q4 = r ** 4
    print(f"  r = {r:.2f} : P(monde complet) = {q:.4f} ; P(monde à quatre appels) = {q4:.4f} ; "
          f"P(n_c >= 16 sur 20) = {queue_haute(20, q, 16):.4f} ; P(n_c >= 20 sur 24) = {queue_haute(24, q, 20):.4f}")

print("5. Devis au pire (plafonds de session du bloc gelé), USD")
plafonds = {"Pr-1": F("2.34"), "Pr-2": F("2.00"), "Pr-3": F("2.34"), "Pr-4": F("3.00")}
machine = F("3.00")
for N in (20, 24):
    parts = {k: v * N for k, v in plafonds.items()}
    credits = parts["Pr-2"] + parts["Pr-4"]
    hors = parts["Pr-1"] + parts["Pr-3"] + machine
    total = credits + hors
    detail = " ; ".join(f"{k} {float(v):.2f}" for k, v in parts.items())
    print(f"  N = {N} : {4 * N} appels ; {detail} ; machine {float(machine):.2f} ; crédits {float(credits):.2f} ; "
          f"hors crédits {float(hors):.2f} ; total {float(total):.2f} ; part sur crédits {float(credits / total):.4f}")
