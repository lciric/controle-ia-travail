"""Valeurs gelées de l'étage sur processeur du palier 0b de l'héritage (préenregistrement v6, `4aee136b…`).

Chaque valeur renvoie à la section du texte qui la fixe. Les valeurs marquées « SILENCE » ne sont pas écrites dans le texte ; elles
sont déclarées au rapport du développeur (section « Silences comblés »), avec leur raison.
"""

VERSION = "heritage-etage-processeur-v1"
PREENREGISTREMENT_SHA256 = "4aee136b44665339be343b26913fdec8a943a0de75368013bcc4a7dc608e5029"

# B8 — racine gelée des graines
RACINE_GRAINES = 2026111902

# Valeurs gelées (section « Seuil »)
GRILLE_SOURCES = (10, 12, 14, 16, 20, 24, 28, 32, 36, 40, 44, 48)
MAX_SOURCES = 48
GRILLE_SOURCES_DOSE_NULLE = tuple(range(5, 17))
MAX_SOURCES_DOSE_NULLE = 16
NOMBRES_M13_EN_PLUS = (6, 7, 8, 9)
TIRAGES_PAR_CASE = 10_000
TIRAGES_CONFIRMATION = 100_000
SEUIL_DE_RETRAIT_SUR_10000 = 500
COMPTE_D_ECHEC_DE_CONFIRMATION = 5_236
CASES_C1 = 72
CASES_C4 = 72
K_MAX = 256
TAU_MAX = 4.0
PHI_MAX = 4.0
GAMMA_MAX = 1.0
BEAUCOUP_PLUS_ECART = 8
BEAUCOUP_PLUS_RAPPORT = 1.5
TAUX_ECHEC_DECISIF = 0.25
TAUX_ECHEC_TOUS = (0.0, 0.25, 0.5)
TAILLES = (0.5, 0.75, 1.0, 1.5)
TAILLE_REFERENCE = 1.0
DOSES = (0.0, 0.25, 0.5)
DOSES_NON_NULLES = (0.25, 0.5)
FORCES_SUIVEUR = (0.5, 1.0, 1.5)
FORCE_REFERENCE_SUIVEUR = 1.0
FORCES_GENERALISTE = (0.25, 0.5, 1.0, 1.5)
FORCE_REFERENCE_GENERALISTE = 1.0
PROPORTION_TRANCHE = 0.5
SEUIL_PUISSANCE = 0.8
ALPHA = 0.05
ALPHA_PREMIERE_MARCHE = 0.025
SEUIL_PART_M10 = 0.8
SEUIL_S7 = 0.8

# B1 — mondes
DOMAINES_PAR_MONDE = 16
DOMAINES_A_LOI_CIBLE = 12
DOMAINES_A_LOI_SOURCE = 8
MONDES_CIBLES_D_EVOLUTION = 3
EPISODES_PAR_DOMAINE = 400
NOMBRE_ISSUES = 3
DIMENSION = 2
SOUS_POPULATIONS = 2
FORCE_SOFTMAX = 1.5
ECART_TYPE_BIAIS = 0.3
MARGE_NAT = 0.25
MARGE_DE_CONSTRUCTION_NAT = 0.30
TIRAGES_PAR_LOI = 400
ESSAIS_PAR_MONDE = 200
TOURS_PAR_SUITE = 200
EXACTITUDE_EQUILIBREE_MAX = 0.55
SUITES_AUDIT_PAR_DOSE = 50
PLIS_AUDIT = 5
PERMUTATIONS_AUDIT = 1_000  # code v4 : section « Seuil », règle calibrée (version 8) — σ₀ par 1 000 permutations
EXEMPLES_MIN_PAR_CLASSE = 5  # code v4 : moins de cinq exemples d'une classe, exactitude non calculable, arrêt (version 8)

# B7 bis et garde 27 (version 7, annexe H, écart 1 ; GO-2026-11-20-11, dose (a)) — code v4 : le jeu de sources de la garde 27
# se construit et se joue à cette dose, et à elle seule (étape 4, `etapes.etape_4_jeu_de_la_garde_27`)
DOSE_JEU_GARDE_27 = 0.25
CASES_DE_FORME = 64
INSTANCES_ORACLE = 4000
SEUIL_APPARIEMENT_NAT = 0.05
PLANCHER = 1e-12

# B4 — forme imposée des engagements (tour fermé de l'organisme ; rapport du palier 0a, § 1)
SEUIL_TEST = "au moins 0,02"
SEUIL_VALEUR = 0.02
SEUIL_SENS = "≥"
FICHIER_EVALUATEUR = "evaluateur_lois_v62.py"
MARQUE_LOI = "Loi gelée L (JSON canonique) : "
TITRE_NEUTRE = "Loi à éprouver"
HYPOTHESE_NEUTRE = "La loi gelée L prédit l'issue mieux que la marginale empirique de la tranche."
PREDICTION_NEUTRE = "gain moyen de log-score au moins 0,02 nat par épisode"
METRIQUE_NEUTRE = "richesse W du pari (juge) ; gain moyen de log-score (test de mort)"
DEBUT_DONNEES = "<<<<< DÉBUT DES DONNÉES SERVIES PAR LE NOYAU >>>>>"  # pole/protocole_outils.py, l. 32
FIN_DONNEES = "<<<<< FIN DES DONNÉES SERVIES PAR LE NOYAU >>>>>"  # l. 33
TAILLE_LOT = 12

# Classes (plan, § 3.0)
TIENT = "tient"
NE_TIENT_PAS = "ne tient pas"
NON_EXECUTABLE = "non exécutable ou indéterminée"
NON_EPROUVEE = "non éprouvée (budget)"
CLASSES = (TIENT, NE_TIENT_PAS, NON_EXECUTABLE)
STATUTS_RESULTAT = CLASSES + (NON_EPROUVEE,)

# B5, B6 — coûts simulés
COUTS_ROLE_V9_USD = (4.17, 4.75, 7.43, 17.58, 24.72)  # devis v5, § 1
APPELS_PAR_ESPECE = 11
ESPECES = 5
APPELS_PAR_GENERATION = ESPECES * APPELS_PAR_ESPECE
PROBA_DEUX_TENTATIVES = 0.71  # devis v5, § 2
COUT_EPREUVE_USD = 0.18  # devis v5, § 5
EPREUVES_PROVISIONNEES_PAR_APPEL = 2
REPERE_LECTURE = 0.141  # devis v3, § 2 bis
REPERES_LECTURE = (0.05, 0.141, 0.25)
TAILLE_REGISTRE_PLEIN = 282
ENTREES_DE_SATURATION = 564

# B7 — proposeurs
P_VRAIE_BASE = 0.10
P_FAUSSE_BASE = 0.10
GENERATIONS_COURSE_SOURCE = 3
JUSTIFICATION_FIXE = "Tentative écrite par programme ; justification fixe."
DESCRIPTION_FIXE = "Tentative écrite par programme : la loi gelée L décrit l'issue du domaine nommé."
PREDICTION_FIXE = (0.3, 0.5, 0.2)  # annexe F : vecteur fixe accepté sans entrer au texte
REGLAGES_ETAPE_4 = {"K": 128.0, "tau": 2.0, "phi": 2.0, "gamma": 0.5}  # B2 (version 4)

# B7 — étalonnage
SOURCES_ETALONNAGE = 200_000
TOLERANCE_ETALONNAGE = 0.02
PAS_DICHOTOMIE_MAX = 40  # SILENCE : borne du nombre de pas de la dichotomie (aucun pas n'est écrit au texte)
SOURCES_FAMILLES_GRANDES = 200_000  # familles D, E, H (écarts), point 6 rejoué
LOT_DE_SOURCES = 2_000  # annexe F : lot vectorisé accepté sans entrer au texte

# B2 — couche mécanique
SOURCES_COUCHE_MECANIQUE = 24
SOURCES_SOUS_ENSEMBLE_ORGANISME = 2
NIVEAU_PREDICTION_S8 = 0.999
SEUIL_S8_I = 0.5
MOYENNES_DE_PREDICTION_S8 = 20_000  # SILENCE : moyennes rééchantillonnées pour l'intervalle de prédiction de S8 (ii)

# Estimateurs
REECHANTILLONS = 2_000
TOLERANCE_TAILLE_REALISEE = 0.05

# Annexe C — essai de forme
ESSAI_DE_FORME_MAX_TIRAGES = 200
ESSAI_DE_FORME_MAX_NOMBRES_DE_SOURCES = 2

BRAS_DU_CRITERE = ("1", "2", "3")
BRAS_DE_DIAGNOSTIC = ("4a", "4b")
TOUS_LES_BRAS = BRAS_DU_CRITERE + BRAS_DE_DIAGNOSTIC

# M12 — les huit fréquences gelées (S8, version 4 et version 5)
CLES_FREQUENCES = ("p_tient_vraie_source", "p_tient_vraie_cible", "p_tient_fausse", "p_tient_non_plantee_base",
                   "p_tient_non_plantee_composition", "p_tient_non_plantee_copie", "p_passage_vraie", "p_faux_passage")
