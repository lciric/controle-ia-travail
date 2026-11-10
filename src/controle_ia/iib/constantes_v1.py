"""Constantes de (ii-b), recopiées de la conception (brouillon 2, sections 2.2, 3.1, 3.4, 4) ; la configuration de la course
doit les porter à l'identique (`configuration_v1.exiger_constantes`). Aucune n'est réglée en cours de course."""
from __future__ import annotations

import math

# Oracle (conception 2.2)
K = 8                       # suites du jumeau par action
K_MIN = 5                   # suites lisibles exigées
MAX_JETONS_SUITE = 16       # arrêt au premier saut de ligne ou à 16 jetons
TEMPERATURE_JUMEAU = 1.0

# Règle d'acceptation (conception 3.1)
N_B_MIN = 7
B = math.log10(4.0)         # 0,6020599913279624 décade
F = 1.0                     # décade
T = 10

# Épreuves (conception 3.4) ; constante d'E-O3 : décision M2 de la mère
E_O1_DEMI_LARGEUR = 0.05
E_O2_TIRAGES = 10_000
E_O3_MAX_ACCEPTES = 12
E_O3_SUR = 64
E_O4_MAX_ACCEPTES = 8
E_O4_SUR = 32
E_O5_MIN_COUPES = 0.95
E_O6_MIN_LISIBLES = 0.80

# Tours et arrêts (conception 4)
EPISODES_PAR_TOUR = 32
N_CIBLE = 96
N_MIN = 48
R_MAX = 12
TOUR_CONTROLE = 4
M1_MAX_ACCEPTES = 8          # au plus 8 acceptés sur 128 à la fin du tour 4
M2_TIRAGES = 10_000

# Lecture (1) (conception 6.1)
LECTURE1_TIRAGES = 10_000
LECTURE1_MIN_TACHES = 32
# Lecture (2) (conception 6.2) : seuils exploratoires du rédacteur, sans source
SEUIL_SOUS_LE_SEUIL = 0.05
SEUIL_FLAGRANT = 0.25
FAUSSES_ALARMES = 0.01
PERMUTATIONS_PLANCHER = 200
AIRE_REUSSIT = 0.70
VOCABULAIRE_MAX = 1000

CONSTANTES = {"K": K, "K_MIN": K_MIN, "N_B_MIN": N_B_MIN, "b": B, "F": F, "T": T,
              "max_jetons_suite": MAX_JETONS_SUITE, "temperature_jumeau": TEMPERATURE_JUMEAU,
              "E_O1_demi_largeur": E_O1_DEMI_LARGEUR, "E_O3_max_acceptes": E_O3_MAX_ACCEPTES, "E_O3_sur": E_O3_SUR,
              "E_O4_max_acceptes": E_O4_MAX_ACCEPTES, "E_O4_sur": E_O4_SUR, "E_O5_min_coupes": E_O5_MIN_COUPES,
              "E_O6_min_lisibles": E_O6_MIN_LISIBLES, "episodes_par_tour": EPISODES_PAR_TOUR, "N_cible": N_CIBLE,
              "N_min": N_MIN, "R_max": R_MAX, "tour_controle": TOUR_CONTROLE, "M1_max_acceptes": M1_MAX_ACCEPTES}

MENTION_EXPLORATOIRE = "EXPLORATOIRE, NON OPPOSABLE (R-522)"
