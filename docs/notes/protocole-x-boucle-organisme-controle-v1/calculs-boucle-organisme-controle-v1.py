"""Calculs formels et simulations exactes pour la boucle de rétroaction
« Organisme d'idéation <-> Programme de contrôle de l'intelligence artificielle ».

Ce script exécute quatre blocs analytiques et numériques :
[A] Modèle mathématique de la boucle fermée : taux de découverte valide en fonction du budget
    de cartes graphiques et de l'efficacité de filtrage sur mondes plantés (sensibilité et spécificité).
[B] Modèle de contamination et de sur-ajustement adaptatif (effet « Ladder ») quand des familles
    de mondes plantés fuient entre l'entraînement de l'organisme et l'évaluation du contrôle,
    et démonstration numérique de l'élimination de cette fuite par séparation stricte
    entre familles d'entraînement de l'organisme, familles tenues à l'écart du banc de contrôle
    et familles de validation finale lues une seule fois.
[C] Théorème de rendement décroissant lorsque la couverture q des mondes plantés manque
    une fraction (1 - c) des classes d'invariants réels du domaine cible (plancher asymptotique
    irréductible malgré l'augmentation de la taille ou du budget de l'organisme).
[D] Classement quantitatif des chantiers et actions prioritaires de la boucle fermée selon :
    score = (gain_informatif * facilite * portee * potentiel_de_decouverte_majeure) / cout
    avec vérification explicite des objets de contrôle (« doit mourir ») et analyse de sensibilité
    aux perturbations de pondération (exposants de poids +/- 50 %).

Toutes les valeurs d'entrée sont des suppositions d'illustration explicitement marquées comme telles ;
aucune donnée privée ni aucun résultat de course réelle du dépôt n'est lu.
Bibliothèque standard Python seule ; graine déterministe documentée si tirage (ici lois fermées exactes).
"""

import math
from pathlib import Path


def titre(texte: str) -> None:
    print()
    print("=" * 100)
    print(texte)
    print("=" * 100)


def phi(z: float) -> float:
    """Fonction de répartition de la loi normale centrée réduite."""
    return 0.5 * (1.0 + math.erf(z / math.sqrt(2.0)))


def inv_phi(p: float) -> float:
    """Inverse approché de la fonction de répartition normale par bissection exacte."""
    bas, haut = -10.0, 10.0
    for _ in range(100):
        mil = 0.5 * (bas + haut)
        if phi(mil) < p:
            bas = mil
        else:
            haut = mil
    return 0.5 * (bas + haut)


# ===================================================================================================
# BLOC [A] : Équation de bilan de la boucle fermée et effet filtre sur mondes plantés vs GPU
# ===================================================================================================
titre("[A] Bilan de la boucle fermée : taux de découverte exploitable contre coût sur cartes graphiques")

# Hypothèses d'illustration :
# N_cand : nombre de fiches ou candidats produits par l'organisme par cycle (sur processeur ou API légère)
# pi_0   : taux de base de candidats véritablement féconds et non redondants parmi les propositions brutes
# alpha_o: taux de faux positifs du filtre de l'oracle sur mondes plantés (laisse passer une fausse idée)
# q_o    : sensibilité (rappel) de l'oracle sur mondes plantés sur la strate couverte
# c_f    : coût unitaire de production + filtrage sur mondes plantés (USD par candidat brut)
# c_gpu  : coût unitaire d'une épreuve complète sur modèle ouvert (8 milliards de paramètres, USD par candidat promu)
# Budget total B_cycle = 100 USD par cycle d'interaction avec le programme de contrôle.

N_CAND = 500
PI_0 = 0.04  # 4 % de candidats intrinsèquement valides avant filtrage (20 candidats vrais sur 500)
C_FILTRE_UNIT = 0.05  # 5 cents par candidat (processeur + appel léger éventuel)
C_GPU_UNIT = 8.00     # 8 USD par épreuve préenregistrée sur carte graphique (illustrative)
BUDGET_TOTAL = 100.0

print(f"Paramètres d'illustration : candidats bruts={N_CAND}, taux de base pi_0={PI_0:.2%}, "
      f"coût filtre={C_FILTRE_UNIT:.2f} USD/cand., coût épreuve GPU={C_GPU_UNIT:.2f} USD/cand., budget={BUDGET_TOTAL:.2f} USD.")
print()
print(f"{'Régime du filtre (mondes plantés)':<40} | {'alpha_o':>7} | {'q_o':>5} | {'Promus':>7} | {'Budget GPU':>10} | {'Vrais épr.':>10} | {'Rendement/100$':>14}")

regimes = [
    ("Objet faux (aucun filtre, tirage brut)", 1.00, 1.00),
    ("Filtre faible (bricolé, haute fausse adm.)", 0.25, 0.70),
    ("Filtre modéré (sans audit de générateur)", 0.08, 0.75),
    ("Filtre rigoureux (scission + compression)", 0.02, 0.80),
    ("Filtre strict (e-valeurs + nul d'archive)", 0.005, 0.75),
    ("Objet mort (filtre trop dur, q_o = 0)", 0.001, 0.00),
]

for nom, alpha_o, q_o in regimes:
    cout_filtre = N_CAND * C_FILTRE_UNIT
    budget_gpu_dispo = max(0.0, BUDGET_TOTAL - cout_filtre)
    max_eprouves_gpu = int(budget_gpu_dispo // C_GPU_UNIT)

    esp_vrais_promus = N_CAND * PI_0 * q_o
    esp_faux_promus = N_CAND * (1.0 - PI_0) * alpha_o
    total_promus = esp_vrais_promus + esp_faux_promus

    if total_promus <= 0:
        precision = 0.0
        nb_eprouves = 0
        vrais_decouverts = 0.0
    else:
        precision = esp_vrais_promus / total_promus
        nb_eprouves = min(total_promus, float(max_eprouves_gpu))
        vrais_decouverts = nb_eprouves * precision

    rendement_par_100 = vrais_decouverts / BUDGET_TOTAL * 100.0
    print(f"{nom:<40} | {alpha_o:>7.3f} | {q_o:>5.2f} | {total_promus:>7.1f} | {budget_gpu_dispo:>10.2f} | {vrais_decouverts:>10.2f} | {rendement_par_100:>14.2f}")

print()
print("Objets de contrôle [A] : (1) sans filtre (alpha_o = 1,00), la précision reste pi_0 = 4,0 %, "
      "et avec 9 candidats éprouvés on obtient exactement 9 * 0,04 = 0,36 vraie découverte ; "
      "(2) lorsque q_o = 0,00 (filtre mort), les vraies découvertes valent exactement 0,00.")


# ===================================================================================================
# BLOC [B] : Modèle de sur-ajustement adaptatif (Ladder) et séparation stricte des familles
# ===================================================================================================
titre("[B] Contamination par fuite sur bancs partagés et élimination par séparation des familles")

# Modèle mathématique de l'attaque adaptative par lecture répétée (Blum et Hardt 2015 / Dwork et al. 2015) :
# Un organisme qui sélectionne la meilleure de M modifications ou réécritures à partir du score observé
# sur un banc partagé de taille n (taux d'erreur standard sigma / sqrt(n)) gonfle son score observé
# de l'espérance du maximum de M gaussiennes corrélées ou indépendantes :
#   biais_optimisme(M, n) ≈ sigma * sqrt(2 * ln(M) / n)   (borne supérieure exacte pour M indépendantes).
# Si l'organisme partage une fraction rho in [0, 1] de ses familles de mondes plantés (ou de ses tâches
# de contrôle) avec le banc d'évaluation du programme de contrôle, le transfert apparent est :
#   gain_apparent = gain_reel + rho * biais_optimisme(M, n)
# tandis que sur une famille tenue à l'écart (rho_ecart = 0), le gain réel hors-famille est mesuré sans biais
# (au bruit d'échantillonnage près), à condition qu'aucune fuite de générateur ni de verdict ne traverse.

SIGMA_SCORE = 0.35   # écart type par tâche sur une métrique normalisée (par ex. score centré ou différence de rappel)
N_BAN = 60           # taille d'un petit banc fixe partagé (à l'image de 60 tâches)
GAIN_REEL_NUL = 0.0  # objet de contrôle « doit mourir » : mécanisme qui n'apporte aucun vrai progrès (Delta = 0)
GAIN_REEL_VRAI = 0.18

print(f"Hypothèses d'illustration : sigma={SIGMA_SCORE}, taille du banc partagé n={N_BAN} tâches.")
print("Sous nul vrai (mécanisme sans gain réel, Delta = 0) : un biais d'optimisme > 0,10 crée une fausse percée.")
print()
print(f"{'Sélection M (cycles x variantes)':>32} | {'Part fuite rho':>14} | {'Biais opt.':>10} | {'Gain apparent (nul)':>19} | {'Gain apparent (vrai=0,18)':>25}")

for M in (1, 10, 50, 200):
    biais_max = SIGMA_SCORE * math.sqrt(2.0 * math.log(max(M, 1)) / N_BAN) if M > 1 else 0.0
    for rho in (1.0, 0.5, 0.0):
        apparent_nul = GAIN_REEL_NUL + rho * biais_max
        apparent_vrai = GAIN_REEL_VRAI + rho * biais_max
        print(f"{M:>32d} | {rho:>14.2f} | {biais_max:>10.4f} | {apparent_nul:>19.4f} | {apparent_vrai:>25.4f}")

print()
print("Interprétation et preuve d'élimination :")
print("1. À M = 200 sélections cumulées sur un banc de n = 60 tâches non séparé (rho = 1,0), "
      f"un mécanisme nul (gain réel = 0) affiche un gain illusoire de +{SIGMA_SCORE * math.sqrt(2.0 * math.log(200) / N_BAN):.3f}, "
      "indiscernable d'un gain réel de 0,15.")
print("2. L'élimination mathématique exige rho = 0 exactement, soit trois cloisons disjointes :")
print("   (C1) Familles de mondes plantés F_org : entraînement et conception interne de l'organisme seul ;")
print("   (C2) Familles tenues à l'écart F_ecart : un tirage unique par cycle de reconception du contrôle ;")
print("   (C3) Familles de validation finale F_final : générateur distinct (anti-raccourci de générateur), lues 1 seule fois.")


# ===================================================================================================
# BLOC [C] : Théorème de rendement décroissant quand les mondes plantés manquent une classe d'invariants
# ===================================================================================================
titre("[C] Rendement décroissant lorsque les mondes plantés manquent une classe d'invariants réels")

# Soit U l'espace des classes d'invariants ou d'attaques réelles en contrôle boîte blanche.
# Supposons que les mondes plantés de l'organisme couvrent une fraction kappa in [0, 1] de ces classes
# (avec efficacité asymtotique plafonnée à P_max sur la fraction couverte kappa), et ne modélisent pas
# du tout la fraction complémentaire (1 - kappa) — par exemple des invariants d'auto-incrimination sous
# poids modifiés, de collusion multi-agents ou de censure du canal de retour.
# Quand l'organisme investit un effort E (nombre d'évaluations / cycles d'optimisation sur mondes plantés),
# le taux de découverte valide sur la fraction couverte suit une courbe saturante :
#   P_couverte(E) = P_max * (1 - exp(-lambda_o * E))
# Mais si l'amélioration sur les mondes plantés entraîne une spécialisation ou un décalage (taxe de sur-spécialisation
# tau_s >= 0) sur les classes non représentées (1 - kappa) de probabilité de base p_residuelle(E) = p_base * exp(-tau_s * E),
# la valeur totale sur l'espace réel U vaut :
#   V_reel(E) = kappa * P_max * (1 - exp(-lambda_o * E)) + (1 - kappa) * p_base * exp(-tau_s * E).
#
# Conséquence analytique :
# 1) Dès que kappa < 1, lim_{E -> +inf} V_reel(E) <= kappa * P_max < P_max (plafond infranchissable).
# 2) Si tau_s > 0 et (1 - kappa) * p_base * tau_s > kappa * P_max * lambda_o * exp(-lambda_o * E),
#    la dérivée dV_reel / dE devient NÉGATIVE : pousser l'organisme davantage détruit la performance réelle !
#    L'effort optimal E* est fini : E* = (1 / (lambda_o - tau_s)) * ln( (kappa*P_max*lambda_o) / ((1-kappa)*p_base*tau_s) )
#    (quand lambda_o != tau_s).

P_MAX = 0.85
LAMBDA_O = 0.04
P_BASE = 0.15
TAU_S = 0.015  # taxe de spécialisation sur les invariants non modélisés dans les mondes plantés

print(f"Modèle saturant avec dérive : P_max={P_MAX}, lambda_o={LAMBDA_O}, p_base={P_BASE}, tau_s={TAU_S}.")
print()
print(f"{'Couverture kappa':>16} | {'E = 10':>9} | {'E = 30':>9} | {'E = 60':>9} | {'E = 150':>9} | {'E = 500':>9} | {'E* optimal':>11} | {'V_reel(E*)':>10}")

for kappa in (1.0, 0.80, 0.50, 0.25, 0.00):
    vals = []
    for E in (10, 30, 60, 150, 500):
        v = kappa * P_MAX * (1.0 - math.exp(-LAMBDA_O * E)) + (1.0 - kappa) * P_BASE * math.exp(-TAU_S * E)
        vals.append(v)
    if kappa == 1.0:
        e_opt_str = "+inf"
        v_opt = P_MAX
    elif kappa == 0.0:
        e_opt_str = "0"
        v_opt = P_BASE
    else:
        ratio = (kappa * P_MAX * LAMBDA_O) / ((1.0 - kappa) * P_BASE * TAU_S)
        if ratio <= 1.0:
            e_opt = 0.0
        else:
            e_opt = math.log(ratio) / (LAMBDA_O - TAU_S)
        v_opt = kappa * P_MAX * (1.0 - math.exp(-LAMBDA_O * e_opt)) + (1.0 - kappa) * P_BASE * math.exp(-TAU_S * e_opt)
        e_opt_str = f"{e_opt:.1f}"
    print(f"{kappa:>16.2f} | " + " | ".join(f"{v:>9.4f}" for v in vals) + f" | {e_opt_str:>11} | {v_opt:>10.4f}")

print()
print("Objets de contrôle [C] :")
print("1. Si kappa = 1,00 (couverture totale), V_reel croît monotonement vers P_max = 0,8500.")
print("2. Si kappa = 0,00 (objet « doit mourir » : les mondes plantés manquent tous les invariants réels), "
      "l'optimisation réduit V_reel de 0,1500 (E=0) à 0,0001 (E=500), confirmant E* = 0.")
print("3. Si kappa = 0,50 (moitié des classes manquantes), V_reel culmine à E* = 108,6 (0,4342) puis baisse à 0,4250 asymptotiquement, "
      "confirmant que l'optimisation au-delà de E* détruit la généralisation hors des strates modélisées.")


# ===================================================================================================
# BLOC [D] : Classement quantitatif des priorités et analyse de sensibilité aux poids
# ===================================================================================================
titre("[D] Classement des priorités selon score = (gain * facilite * portee * decouverte) / cout et sensibilité")

# Liste des chantiers / leviers candidats de la boucle « Organisme d'idéation <-> Programme de contrôle IA »
# Chaque entrée : (code, libelle_en_clair, gain_informatif, facilite, cout, portee, decouverte_majeure, role_boucle)
candidats = [
    ("C1", "Cloisonnement strict à trois strates (entraînement organisme / mode tenu à l'écart / validation finale) et audit du générateur avant tout banc partagé",
     5, 5, 1, 5, 4, "Garde anti-contamination (boucle entière)"),
    ("C2", "Branchement de l'opérateur de scission conceptuelle (faisceaux cellulaires et personas) sur les faux amalgames de contrôle (conscience d'évaluation contre intention)",
     5, 4, 1, 5, 5, "Organisme -> Programme contrôle (H8, HC2, passage obligé)"),
    ("C3", "Détecteurs sémantiques des cinq signaux ex ante appliqués au corpus d'alignement et de contrôle boîte blanche (repérage des zones d'objets manquants)",
     5, 4, 1, 5, 5, "Corpus contrôle -> Organisme (orientation de recherche)"),
    ("C4", "Banc de recherche à vérité plantée (lois statistiques et dommages exacts hors machine) servant d'environnement exécutable flou-à-la-relecture pour les papiers A et B",
     5, 4, 2, 5, 5, "Organisme <-> Programme contrôle (N-076 point 3 / N-065 rôle 3)"),
    ("C5", "Validation empirique en 3 à 5 jours sur processeur des briques de l'organisme (test sur données publiques datées et graphes sans fuite temporelle avant dégel)",
     5, 5, 1, 5, 4, "Assise empirique de l'organisme avant couplage"),
    ("C6", "Cycle Éveil-Sommeil hybride (proposition par modèle de langage + compression inter-bassins par longueur de description minimale) pour inventer des invariants de contrôle hors alphabet",
     5, 3, 2, 5, 5, "Organisme avancé -> Nouveaux objets pour le contrôle"),
    ("C7", "Chaîne d'épreuves et objets « doit mourir » avant tout réapprentissage ou toute promesse (séparation des jumeaux, épreuve du devin, calibration sur référence honnête)",
     5, 4, 1, 4, 3, "Garde d'oracle et d'audit dans la boucle (N-075, N-076)"),
    ("C8", "Boucle de génération de modes de sabotage inédits par l'organisme (rôle 3 : proposeurs hors alphabet de sabotage puis sélection par mode tenu à l'écart)",
     4, 3, 2, 4, 5, "Organisme -> Équipe rouge du contrôle (N-065 rôle 3)"),
    ("C9", "Sondes internes de surprise / erreur de prédiction (observation passive au dernier jeton sans optimisation directe) appliquées aux trajectoires d'idéation et de contrôle",
     3, 3, 2, 4, 4, "Programme contrôle -> Organisme (mesure exploratoire N-076 § 10)"),
    ("C10", "Réécriture éditoriale ou mise en forme de vulgarisation / subvention (effet nul sur la boucle technique)",
     2, 4, 1, 2, 1, "Hors boucle technique (témoin bas)"),
    ("C11", "[OBJET DOIT MOURIR] Sélection directe des proposeurs ou sondes de l'organisme par les verdicts des juges ou des moniteurs du programme",
     1, 5, 1, 1, 1, "Interdit par N-053 / N-058 (contamination circulaire)"),
]

def calcul_score(g, f, c, p, d, exposants=(1.0, 1.0, 1.0, 1.0, 1.0)):
    eg, ef, ec, ep, ed = exposants
    return ((g ** eg) * (f ** ef) * (p ** ep) * (d ** ed)) / (c ** ec)

# Calcul principal (exposants unitaires = formule demandée)
resultats = []
for code, lib, g, f, c, p, d, role in candidats:
    s = calcul_score(g, f, c, p, d)
    resultats.append((s, code, lib, g, f, c, p, d, role))

resultats.sort(key=lambda x: (-x[0], x[1]))

print("Classement nominal (formule exacte : (gain * facilite * portee * decouverte) / cout) :")
print(f"{'Rang':>4} | {'Code':>4} | {'G':>2} | {'F':>2} | {'C':>2} | {'P':>2} | {'D':>2} | {'Score':>7} | {'Rôle / Libellé'}")
for idx, (s, code, lib, g, f, c, p, d, role) in enumerate(resultats, 1):
    print(f"{idx:>4} | {code:>4} | {g:>2} | {f:>2} | {c:>2} | {p:>2} | {d:>2} | {s:>7.1f} | {lib[:68]}")

# Analyse de sensibilité aux exposants de poids (variation bilatérale +/- 50 % : exposant à 0,5 ou 1,5)
print()
print("Analyse de sensibilité aux pondérations (variation bilatérale des exposants : 0,5 ou 1,5) :")
schemas = [
    ("Nominal (1,1,1,1,1)", (1.0, 1.0, 1.0, 1.0, 1.0)),
    ("Priorité Découverte (D^1,5)", (1.0, 1.0, 1.0, 1.0, 1.5)),
    ("Découverte atténuée (D^0,5)", (1.0, 1.0, 1.0, 1.0, 0.5)),
    ("Priorité Coût strict (C^1,5)", (1.0, 1.0, 1.5, 1.0, 1.0)),
    ("Coût atténué (C^0,5)", (1.0, 1.0, 0.5, 1.0, 1.0)),
    ("Priorité Facilité (F^1,5)", (1.0, 1.5, 1.0, 1.0, 1.0)),
    ("Facilité atténuée (F^0,5)", (1.0, 0.5, 1.0, 1.0, 1.0)),
    ("Priorité Gain info (G^1,5)", (1.5, 1.0, 1.0, 1.0, 1.0)),
    ("Priorité Portée (P^1,5)", (1.0, 1.0, 1.0, 1.5, 1.0)),
]

top_codes = {}
for nom_s, exp in schemas:
    classement = sorted(
        [(calcul_score(g, f, c, p, d, exp), code) for code, _, g, f, c, p, d, _ in candidats],
        key=lambda x: (-x[0], x[1])
    )
    ordre = [code for _, code in classement]
    top_codes[nom_s] = ordre[:5]
    print(f"  {nom_s:<30} -> Top 6 : {' > '.join(ordre[:6])} | Bas : {' > '.join(ordre[-3:])}")

# Vérification de stabilité : combien de candidats dans le top 5 restent stables ?
intersection_top5 = set.intersection(*(set(v) for v in top_codes.values()))
print(f"Invariants du Top 5 sur les 9 schémas de sensibilité : {sorted(intersection_top5)}")
print(f"Invariants de queue (toujours dans les 2 derniers : C10 et C11) : "
      f"{all(set(sorted([(calcul_score(g, f, c, p, d, exp), code) for code, _, g, f, c, p, d, _ in candidats])[:2][i][1] for i in range(2)) == {'C10', 'C11'} for _, exp in schemas)}")
