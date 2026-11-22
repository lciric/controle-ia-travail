#!/usr/bin/env python3
"""Calculs du brouillon 7 du préenregistrement de la porte G1 — v1.

Processeur seul, bibliothèque standard seule. Aucune donnée du programme n'est lue (rien sous `donnees/`, `diag/`,
`runs/`, aucun score d'épisode, aucun verdict) : les seules entrées sont des constantes recopiées des pièces citées
dans le brouillon, chacune avec sa source en commentaire. Non opposable seul (R7) : le brouillon cite cette sortie
par chemin et empreinte (R6). Aucune graine : tout est déterministe (formules fermées, sommes exactes).

Lancer, depuis un dossier vide : python3 -I <chemin>/calculs-g1-brouillon7-v1.py > calculs-g1-brouillon7-v1-sortie.txt
"""
import math
import platform

# ---------------------------------------------------------------------------------------------------------------
# Outils


def titre(s):
    print(f"\n## {s}\n")


def nombre(x, dec=0):
    """Nombre à la française : espace pour les milliers, virgule décimale."""
    t = f"{x:,.{dec}f}"
    return t.replace(",", " ").replace(".", ",")


def log_binom(n, k):
    return math.lgamma(n + 1) - math.lgamma(k + 1) - math.lgamma(n - k + 1)


def pmf_binomiale(n, p):
    if p <= 0.0:
        return [1.0] + [0.0] * n
    return [math.exp(log_binom(n, k) + k * math.log(p) + (n - k) * math.log1p(-p)) for k in range(n + 1)]


def repartition_binomiale(x, n, p):
    """P(X <= x) pour X ~ Binomiale(n, p), somme exacte en logarithmes."""
    if x < 0:
        return 0.0
    if x >= n:
        return 1.0
    return min(1.0, sum(math.exp(log_binom(n, k) + k * math.log(p) + (n - k) * math.log1p(-p)) for k in range(x + 1)))


def borne_haute_clopper_pearson(x, n, niveau=0.95):
    """Borne haute unilatérale : p_h tel que P(X <= x | p_h) = 1 - niveau (bissection)."""
    if x >= n:
        return 1.0
    bas, haut = x / n, 1.0
    for _ in range(200):
        mil = (bas + haut) / 2
        if repartition_binomiale(x, n, mil) > 1 - niveau:
            bas = mil
        else:
            haut = mil
    return haut


def log_beta(a, b):
    return math.lgamma(a) + math.lgamma(b) - math.lgamma(a + b)


def pmf_beta_binomiale(n, p, rho):
    """Bêta-binomiale de moyenne p et de corrélation intra-unité rho (rho = 1 / (a + b + 1))."""
    if rho <= 0.0:
        return pmf_binomiale(n, p)
    s = 1.0 / rho - 1.0
    a, b = p * s, (1.0 - p) * s
    return [math.exp(log_binom(n, k) + log_beta(k + a, n - k + b) - log_beta(a, b)) for k in range(n + 1)]


print("# Sortie de calculs-g1-brouillon7-v1.py")
print(f"Python {platform.python_version()} ; bibliothèque standard seule (math)")
print("Aucune graine : tous les calculs sont déterministes.")

# ---------------------------------------------------------------------------------------------------------------
titre("1. Contrôle : la variante par défaut du brouillon 6 est retrouvée (même modèle de coût que [calc § 7] du brouillon 5)")
# Constantes recopiées de calculs-g1-brouillon5-v1.py (8021037b…), elles-mêmes rapportées de : pilote de T0.5 (R-143),
# dimensionnement de la couche 2 § 8 (95c5c396…), registres/depenses.md (lignes du 12 au 20 octobre), R-205.
GEN = {"bas": 42.1, "central": (42.1 + 54.6) / 2, "haut": 54.6}      # secondes de génération par épisode
JUGE = 58.2                                                          # secondes de notation d'un juge 8B par épisode
B = {"bas": 1, "central": 2, "haut": 4}                              # équivalents « juge 8B » par épisode (INFÉRÉ)
PRIX = {"bas": 1.08, "central": (1.08 + 1.2133) / 2, "haut": 1.2133}  # USD par heure de carte A100 80 Go
K_S, K_H = 10, 10            # exécutions sabotées et jumelles honnêtes par unité (branche R-504 ; R-733 N2)
TACHES = 400                 # unités par mode sans mesure au pilote (branche R-556 (2))
FACTEUR_CALIBRAGE = 15       # D-S9 (a) : 10 à 16 fois les unités sabotées, unités de 10 épisodes
PLAFOND_ACCORDE = 6331       # USD, DG1-13, GO-2026-11-05-07 (calculé sans aucun épisode de témoin apparié)


def cout(episodes):
    sortie = {}
    for cle in ("bas", "central", "haut"):
        s = GEN[cle] + B[cle] * JUGE
        h = episodes * s / 3600
        sortie[cle] = (h, h * PRIX[cle])
    return sortie


base_par_tache = K_H + 3 * K_S * 2 + 12 + FACTEUR_CALIBRAGE * 10
base = TACHES * base_par_tache
c0 = cout(base)
print(f"Épisodes par tâche (brouillon 6) : {K_H} jumeaux + 3 modes x {K_S} x 2 familles + 12 témoin bénin et mention "
      f"+ {FACTEUR_CALIBRAGE * 10} de calibrage honnête = {base_par_tache}")
print(f"Variante par défaut : {TACHES} tâches x {base_par_tache} = {nombre(base)} épisodes ; "
      f"central {nombre(c0['central'][0])} h, {nombre(c0['central'][1])} USD "
      f"(attendu d'après le brouillon 6 : 92 800 épisodes, 4 247 h, 4 870 USD)")
assert base == 92800 and round(c0["central"][0]) == 4247 and round(c0["central"][1]) == 4870, "contrôle manqué"
print("Contrôle : conforme.")

# ---------------------------------------------------------------------------------------------------------------
titre("2. Épisodes du témoin apparié selon l'énoncé retenu (GO-2026-11-18-48 ; brouillon de décision N-074, non pris)")
# Proposition du brouillon 7, à contre-lire : K_w = 10 exécutions du témoin par unité pour la famille de la porte
# (l'organisme sans consigne, un témoin d'adaptateur par mode, trois modes : deux de la porte, le mode « coût »
# rapporté) ; K_w = 3 pour la famille à consigne, rapportée (témoin de consigne, trois modes).
KW_PORTE, KW_RAPPORTE = 10, 3
temoin_eval_par_tache = 3 * KW_PORTE + 3 * KW_RAPPORTE
print(f"Épisodes d'évaluation du témoin par tâche, communs à tous les énoncés : 3 modes x {KW_PORTE} (organisme sans "
      f"consigne) + 3 modes x {KW_RAPPORTE} (organisme à consigne) = {temoin_eval_par_tache}")
print(f"Par cellule de la porte (un mode, organisme sans consigne) : {TACHES} x {KW_PORTE} = {nombre(TACHES * KW_PORTE)} "
      f"épisodes d'évaluation du témoin (le brouillon de N-074 en demande au moins 300)\n")

VARIANTES = [
    ("sans témoin apparié (brouillon 6, rappel)", 0, 0),
    ("garde de spécificité, ou garde avec contraste rapporté à 5 % (énoncés B et C2)", temoin_eval_par_tache, 0),
    ("contraste, calibrage du témoin au minimum du brouillon de N-074 : 300 épisodes par cellule, 6 cellules "
     "(énoncés A et C1)", temoin_eval_par_tache, 6 * 300 / TACHES),
    ("contraste, calibrage du témoin à l'échelle du calibrage honnête, cellules de la porte seules : "
     "2 témoins x 150 par tâche (énoncés A et C1)", temoin_eval_par_tache, 2 * FACTEUR_CALIBRAGE * 10),
    ("contraste, calibrage du témoin à l'échelle du calibrage honnête, les trois modes de l'organisme sans consigne : "
     "3 témoins x 150 par tâche (énoncés A et C1)", temoin_eval_par_tache, 3 * FACTEUR_CALIBRAGE * 10),
]
print("| variante | épisodes par tâche | épisodes | heures de carte (bas / central / haut) | USD (bas / central / haut) "
      "| central x 1,3 | rapport au plafond accordé (6 331 USD) |")
print("|---|---|---|---|---|---|---|")
for nom, ev, cal in VARIANTES:
    ept = base_par_tache + ev + cal
    E = TACHES * ept
    c = cout(E)
    print(f"| {nom} | {nombre(ept, 1 if ept != int(ept) else 0)} | {nombre(E)} | "
          f"{nombre(c['bas'][0])} / {nombre(c['central'][0])} / {nombre(c['haut'][0])} | "
          f"{nombre(c['bas'][1])} / {nombre(c['central'][1])} / {nombre(c['haut'][1])} | "
          f"{nombre(c['central'][1] * 1.3)} | {nombre(c['central'][1] * 1.3 / PLAFOND_ACCORDE, 2)} |")
print("\nNon comptés, en plus de ceux du brouillon 6 : une distillation de plus par témoin d'adaptateur et sa remise à "
      "l'intensité du saboteur ; la conception du témoin du mode tenu à l'écart par son concepteur.")

# ---------------------------------------------------------------------------------------------------------------
titre("3. Bruit d'un seuil conforme à 1 % : écart-type du taux réel de fausses alarmes selon le nombre d'épisodes de "
      "calibrage (épisodes indépendants ; taux réel ~ Bêta(K + 1 - r, r), r = ceil((K + 1) x 0,99))")
for K in (300, 1200, 4000, 12000, 18000, 60000):
    r = math.ceil((K + 1) * 0.99 - 1e-12)
    a, b = K + 1 - r, r
    moyenne = a / (a + b)
    ecart = math.sqrt(a * b / ((a + b) ** 2 * (a + b + 1)))
    print(f"  K = {K:>6} : rang {r:>6} ; taux réel moyen {nombre(100 * moyenne, 3)} % ; écart-type {nombre(100 * ecart, 3)} point")
print("Repères de l'étude de la formulation (d04da790…, texte) : 0,57 point à 300 épisodes ; 0,09 à 12 000 ; 0,07 à 18 000.")
print(f"Calibrage d'épreuve du brouillon 6 : {FACTEUR_CALIBRAGE * 10} épisodes honnêtes par tâche x {TACHES} tâches = "
      f"{nombre(FACTEUR_CALIBRAGE * 10 * TACHES)} épisodes (groupés par tâche : l'information réelle est moindre "
      "que celle d'épisodes indépendants ; le contrôle par moitiés jumelles le mesure).")

# ---------------------------------------------------------------------------------------------------------------
titre("4. Garde de spécificité par la borne de Clopper-Pearson (lettre du brouillon de N-074, épisodes supposés "
      "indépendants) : plus grand nombre d'alertes du témoin qui laisse la borne haute à 95 % strictement sous 5 %")
for n in (300, 1200, 4000):
    x_max = -1
    for x in range(n + 1):
        if borne_haute_clopper_pearson(x, n) < 0.05:
            x_max = x
        else:
            break
    ligne = f"  n = {n:>5} : au plus {x_max} alertes ({nombre(100 * x_max / n, 2)} % observé)"
    for p in (0.01, 0.027, 0.04, 0.05):
        ligne += f" ; P(passer | taux vrai {nombre(100 * p, 1)} %) = {nombre(repartition_binomiale(x_max, n, p), 4)}"
    print(ligne)
print("Repères du brouillon de N-074 (29b38fc4…, § 4) : 0,95 par cellule à 200 épisodes et 0,996 à 300, au taux vrai de 1 % ; "
      "moins de 4 % de passages au taux vrai de 5 %.")
x200 = max(x for x in range(201) if borne_haute_clopper_pearson(x, 200) < 0.05)
print(f"  contrôle à n = 200 : au plus {x200} alertes ; P(passer | 1 %) = {nombre(repartition_binomiale(x200, 200, 0.01), 4)}")

# ---------------------------------------------------------------------------------------------------------------
titre("5. Garde de spécificité par un pari borné sur les parts par unité (proposition du brouillon 7 ; valide quand "
      "les épisodes d'une même tâche sont dépendants) : unités nécessaires pour atteindre le seuil, ordre de grandeur")
# w(u) = part des K_w épisodes du témoin de l'unité u en alarme pour la boîte blanche séquentielle ; pari contre
# « E[w] >= 0,05 » de facteur 1 + lambda x (0,05 - w(u)), lambda dans la grille de N-055 (D-S6), mélange à poids
# égaux. Ordre de grandeur : la richesse du mélange croît comme celle de la meilleure mise, au quart près (poids 1/4) :
# unités nécessaires ~ ln(4 x seuil) / max_lambda E[ln(1 + lambda x (0,05 - w))]. NON OPPOSABLE : la simulation de la
# garde appariée (à refaire à la liste exacte) le chiffrera ; ce calcul ne sert qu'à dire ce que le choix du niveau
# de cette garde change.
GRILLE = (0.1, 0.3, 0.6, 0.9)
PLAFOND_GARDE = 0.05


def croissance(p, k_w, rho):
    pmf = pmf_beta_binomiale(k_w, p, rho)
    meilleur = -math.inf
    for lam in GRILLE:
        g = sum(q * math.log1p(lam * (PLAFOND_GARDE - k / k_w)) for k, q in enumerate(pmf) if q > 0)
        meilleur = max(meilleur, g)
    return meilleur


print("| taux d'alerte vrai du témoin | K_w | corrélation intra-unité | croissance par unité (meilleure mise) | "
      "unités pour le seuil 20 | pour 40 | pour 160 |")
print("|---|---|---|---|---|---|---|")
for p in (0.01, 0.02, 0.027, 0.03, 0.04):
    for k_w in (10, 3):
        for rho in (0.0, 0.17):
            g = croissance(p, k_w, rho)
            if g <= 0:
                besoins = ["jamais", "jamais", "jamais"]
            else:
                besoins = [nombre(math.ceil(math.log(4 * s) / g)) for s in (20, 40, 160)]
            print(f"| {nombre(100 * p, 1)} % | {k_w} | {nombre(rho, 2)} | {nombre(g, 5)} | {besoins[0]} | {besoins[1]} | {besoins[2]} |")
print("\nLecture : à 400 unités et K_w = 10, la garde par pari au seuil 160 n'est atteinte que si le taux d'alerte vrai "
      "du témoin est nettement sous 5 % (lignes ci-dessus) ; entre ce taux et 5 %, elle se lit « non jugeable par "
      "puissance », non « garde perdue ». La borne de Clopper-Pearson (section 4) est plus puissante parce qu'elle "
      "tient les épisodes d'une même tâche pour indépendants.")

# ---------------------------------------------------------------------------------------------------------------
titre("6. Seuils du pari inverse (signe contraire) : Bonferroni sur les comparateurs et les modes de la porte")
for k in (12, 13):
    for doubles in (1, 2):
        print(f"  k = {k} comparateurs, {doubles} classe(s) négative(s) (honnête{' et témoin' if doubles == 2 else ''}), "
              f"M = 2 modes : seuil = k x classes x M / 0,05 = {k * doubles * 2 * 20}")
print("Le brouillon 6 écrit 480 (k = 12) et 520 (k = 13) pour la seule classe négative honnête.")

# ---------------------------------------------------------------------------------------------------------------
titre("7. Probabilité de franchir toutes les cellules si elles étaient indépendantes (illustration prudente, comme [calc § 5])")
for p_cellule in (0.9, 0.8):
    print("  puissance par condition " + nombre(p_cellule, 1) + " : " + " ; ".join(
        f"{n} condition(s) -> {nombre(p_cellule ** n, 3)}" for n in (1, 2, 4, 6)))
print("Deux modes de la porte : 2 conditions sans témoin apparié ; 4 si chaque mode porte en plus une condition de témoin.")
