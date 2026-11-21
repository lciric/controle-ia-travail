"""Calculs exacts cités par le brouillon 1 du préenregistrement v2 de SPARKS-EXP7-NUL.

Écrit le 21 novembre 2026 par Claude Fable 5.2, rédacteur du texte neuf. Bibliothèque standard seule, aucun tirage,
aucune donnée de l'expérience (il n'en existe aucune) : lois binomiales exactes, bornes de Clopper-Pearson par
dichotomie, énumération exacte des rangs. Sert à vérifier les chiffres repris du texte v1 (lignes 116, 117 et 161) et à
chiffrer ce que le texte neuf ajoute. Lancement : python3 -I calculs-preenregistrement-v2-brouillon1-v1.py
"""
from fractions import Fraction
from itertools import combinations
from math import comb


def queue_sup(n, k, p):
    """P(X >= k), X binomiale (n, p)."""
    return sum(comb(n, i) * p ** i * (1 - p) ** (n - i) for i in range(k, n + 1))


def queue_inf(n, k, p):
    """P(X <= k)."""
    return sum(comb(n, i) * p ** i * (1 - p) ** (n - i) for i in range(0, k + 1))


def borne_sup_cp(n, k, alpha=0.05):
    """Borne supérieure unilatérale de Clopper-Pearson : p tel que P(X <= k | p) = alpha."""
    if k >= n:
        return 1.0
    bas, haut = 0.0, 1.0
    for _ in range(200):
        milieu = (bas + haut) / 2
        if queue_inf(n, k, milieu) > alpha:
            bas = milieu
        else:
            haut = milieu
    return (bas + haut) / 2


def seuil_unilateral(n, alpha=0.05, p0=0.5):
    """Plus petit k tel que P(X >= k | p0) <= alpha."""
    for k in range(n + 1):
        if queue_sup(n, k, p0) <= alpha:
            return k
    return None


def plus_grand_k_minoritaire(n, alpha=0.05):
    """Plus grand k dont la borne supérieure de Clopper-Pearson est < 0,5."""
    return max(k for k in range(n + 1) if borne_sup_cp(n, k, alpha) < 0.5)


def f(x, d=3):
    return f"{x:.{d}f}".replace(".", ",")


print("A. Exactitude d'ordre sur les paires vraies (M1), test binomial exact unilatéral contre 0,5, niveau 0,05")
for n in (24, 16):
    k = seuil_unilateral(n)
    print(f"  n = {n} : seuil {k}/{n}, risque réel {f(queue_sup(n, k, 0.5))} ; puissance si l'exactitude vraie vaut "
          + " ; ".join(f"{f(p, 2)} : {f(queue_sup(n, k, p))}" for p in (0.65, 0.75, 0.85)))

print("B. Scission sur les paires nulles (M2), « minoritaire » si la borne supérieure de Clopper-Pearson"
      " unilatérale à 95 % est < 0,5")
for n in (24, 16):
    k = plus_grand_k_minoritaire(n)
    print(f"  n = {n} : au plus {k}/{n} (borne {f(borne_sup_cp(n, k))} ; à {k + 1}/{n} la borne vaut "
          f"{f(borne_sup_cp(n, k + 1))}) ; probabilité de la décision si la scission vraie vaut "
          + " ; ".join(f"{f(p, 2)} : {f(queue_inf(n, k, p))}" for p in (0.15, 0.20, 0.30, 0.50)))

print("C. Scission « majoritaire » déclarée à 12/24 ou plus : probabilité selon la scission vraie")
print("  " + " ; ".join(f"{f(p, 2)} : {f(queue_sup(24, 12, p))}" for p in (0.20, 0.30, 0.35, 0.50, 0.60, 0.70)))

print("D. « Pas de détection » (M1 <= 12/24) : probabilité selon l'exactitude vraie")
print("  " + " ; ".join(f"{f(p, 2)} : {f(queue_inf(24, 12, p))}" for p in (0.50, 0.65, 0.75, 0.85)))

print("E. Zones sans décision : M1 de 13 à 16 sur 24 ; M2 de 8 à 11 sur 24")
print("  M1 de 13 à 16 : " + " ; ".join(
    f"{f(p, 2)} : {f(queue_sup(24, 13, p) - queue_sup(24, 17, p))}" for p in (0.50, 0.65, 0.75, 0.85)))
print("  M2 de 8 à 11 : " + " ; ".join(
    f"{f(p, 2)} : {f(queue_sup(24, 8, p) - queue_sup(24, 12, p))}" for p in (0.15, 0.20, 0.30, 0.50)))

print("F. Ampleur de l'écart dans la paire sur l'étalonnage (8 paires vraies contre 4 nulles) : loi exacte de l'aire"
      " sous des rangs échangeables (paires supposées indépendantes, ce qu'elles ne sont pas : 4 modèles par groupe)")
n_v, n_n = 8, 4
total = comb(n_v + n_n, n_n)
compte_haut = compte_bas = 0
for rangs_nuls in combinations(range(1, n_v + n_n + 1), n_n):
    # U des paires vraies = nombre de couples (vraie, nulle) où la vraie est au-dessus
    u_nuls = sum(rangs_nuls) - n_n * (n_n + 1) // 2      # couples où la nulle est au-dessus
    aire_vraie = Fraction(n_v * n_n - u_nuls, n_v * n_n)
    if aire_vraie >= Fraction(3, 4):
        compte_haut += 1
    if aire_vraie <= Fraction(1, 4):
        compte_bas += 1
print(f"  P(aire >= 0,75) = {compte_haut}/{total} = {f(compte_haut / total)} ; P(aire <= 0,25) = {compte_bas}/{total}"
      f" = {f(compte_bas / total)} ; P(l'une ou l'autre) = {f((compte_haut + compte_bas) / total)}")
print(f"  Aire de 1 sur 4 honnêtes contre 4 sycophantes par hasard : 1/{comb(8, 4)} = {f(1 / comb(8, 4), 4)}")

print("G. Plafond, au niveau du modèle, d'un score constant dans la paire (ordre idéal : paires ss, puis vraies,"
      " puis hh ; 24 sycophantes en ss, 24 sycophantes et 24 honnêtes à égalité en paires vraies, 24 honnêtes en hh)")
gagne = 24 * 48 + 24 * 24          # sycophantes de ss contre tous les honnêtes ; sycophantes de vraies contre hh
egal = 24 * 24                     # sycophantes de vraies contre honnêtes de vraies : même score
print(f"  aire maximale = ({gagne} + {egal}/2) / {48 * 48} = {f((gagne + egal / 2) / (48 * 48))}")

print("H. Contrôle causal (C1) : seuils en nombre d'unités")
for n in (24, 48):
    porteur = next(k for k in range(n + 1) if Fraction(k, n) >= Fraction(1, 4))
    non = max(k for k in range(n + 1) if Fraction(k, n) <= Fraction(1, 10))
    print(f"  {n} unités : « porteurs » à {porteur}/{n} ou plus ; « non porteurs » à {non}/{n} ou moins ; "
          f"entre les deux : {non + 1} à {porteur - 1}")
print(f"  Rang d'un ensemble nommé qui dépasse le maximum de 20 témoins : centile {f(100 * 20 / 21, 1)}")

print("I. Comptes")
print(f"  modèles : principal {2 * 48}, ancre {2 * 3}, étalonnage {2 * 4}, total {2 * 48 + 2 * 3 + 2 * 4} ;"
      f" réserve au plus {2 * 6} ; total au plus {2 * 48 + 2 * 3 + 2 * 4 + 2 * 6}")
par_unite = 2 + 3 * 22
print(f"  mesures causales : {par_unite} par unité (2 de référence, 3 sens fois 22 ensembles) ; "
      f"24 unités : {24 * par_unite} ; 48 unités : {48 * par_unite}")
octets_couches = 200_678_368
plongement = 262_144 * 640 * 2
for n in (110, 122):
    print(f"  stockage de {n} modèles (18 couches chacun) et d'un plongement : "
          f"{f((n * octets_couches + plongement) / 1e9, 1)} Go")
astra = (782_605, 1_673_367, 1_549_461)
moyenne = sum(astra) / len(astra)
print("  jetons d'entrée cumulés par conversation chez les auteurs : moyenne de "
      + ", ".join(f"{a:,}".replace(",", " ") for a in astra) + " = " + f"{moyenne:,.0f}".replace(",", " "))
for libelle, n in (("un lecteur, 48 cas et 3 d'ancre", 51), ("deux lecteurs, 96 et 6", 102)):
    print(f"  projection ({libelle}) : {n} conversations fois la moyenne = {n * moyenne / 1e6:.1f} millions"
          .replace(".", ","))

print("K. Ce que bornent des comptes publiés par des voisins (calculs du rédacteur sur des chiffres lus sur PDF)")
print(f"  0 fausse alerte sur 21 (Liu et Yang, arXiv 2611.07847v2, p. 1) : borne supérieure de Clopper-Pearson"
      f" unilatérale à 95 % = {f(borne_sup_cp(21, 0))}")
for k, n in ((10, 10), (7, 10), (23, 32), (14, 32), (13, 32), (17, 32)):
    print(f"  {k} sur {n} en choix forcé (Goworek et al., arXiv 2611.21449v1, p. 13 à 15) : queue supérieure sous 0,5"
          f" = {f(queue_sup(n, k, 0.5))}")
print(f"  3 sur 3 en choix forcé (billet, expérience 7) : queue supérieure sous 0,5 = {f(queue_sup(3, 3, 0.5))}")

print("J. Déclencheurs de l'audit de symétrie : probabilités sous quelques vérités")
print(f"  M1 = 24/24 si l'exactitude vraie vaut 0,85 : {f(queue_sup(24, 24, 0.85), 4)} ; 0,95 : "
      f"{f(queue_sup(24, 24, 0.95), 3)}")
print(f"  M1 <= 6/24 si l'exactitude vraie vaut 0,5 : {f(queue_inf(24, 6, 0.5), 4)}")
print(f"  M2 = 0/24 si la scission vraie vaut 0,05 : {f(queue_inf(24, 0, 0.05), 3)} ; 0,15 : "
      f"{f(queue_inf(24, 0, 0.15), 4)}")
