"""Valeurs gelées de l'étage sur processeur du palier 0b de l'héritage (préenregistrement v3, `a4535a67…`).

Chaque valeur renvoie à la section du texte qui la fixe. Les valeurs marquées « SILENCE » ne sont pas écrites dans le texte :
elles sont le choix le plus étroit du développeur et sont déclarées au rapport (section « Silences comblés »).
"""

VERSION = "heritage-etage-processeur-v1"

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
TAUX_ECHEC_SENSIBILITE = (0.0, 0.5)
TAUX_ECHEC_TOUS = (0.0, 0.25, 0.5)
TAILLES = (0.5, 0.75, 1.0, 1.5)
TAILLE_REFERENCE = 1.0
DOSES = (0.0, 0.25, 0.5)
DOSES_NON_NULLES = (0.25, 0.5)
FORCES_SUIVEUR = (0.5, 1.0, 1.5)
FORCES_GENERALISTE = (0.25, 0.5, 1.0, 1.5)
PROPORTION_TRANCHE = 0.5

# B1 — mondes
DOMAINES_PAR_MONDE = 16
DOMAINES_A_LOI_CIBLE = 12
DOMAINES_A_LOI_SOURCE = 8
MONDES_CIBLES_D_EVOLUTION = 3
EPISODES_PAR_DOMAINE = 400  # SILENCE : le texte ne le dit pas ; 400 est la tranche du tour fermé (A.EPISODES_TRANCHE)
NOMBRE_ISSUES = 3
DIMENSION = 2
SOUS_POPULATIONS = 2
FORCE_SOFTMAX = 1.5  # SILENCE : celle de `selection_pari.loi_softmax_aleatoire` de l'organisme
ECART_TYPE_BIAIS = 0.3  # SILENCE : idem
MARGE_NAT = 0.25
EXACTITUDE_EQUILIBREE_MAX = 0.55
INSTANCES_ORACLE = 4000  # rapport du palier 0a, § 1 (oracle v60, N_ORACLE)
SEUIL_APPARIEMENT_NAT = 0.05  # B3
PLANCHER = 1e-12

# B4 — forme imposée des engagements (tour fermé de l'organisme, rapport du palier 0a, § 1)
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
TAILLE_LOT = 12  # plafond de l'étage v5 (rapport du palier 0a, § 3.1, point 3)

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
PROBA_DEUX_TENTATIVES = 0.71  # devis, § 2 (94 tentatives pour 55 appels)
COUT_EPREUVE_USD = 0.18  # devis, § 5
EPREUVES_PROVISIONNEES_PAR_APPEL = 2
REPERE_LECTURE = 0.141  # devis v3, § 2 bis
REPERES_LECTURE_SENSIBILITE = (0.05, 0.25)
TAILLE_REGISTRE_PLEIN = 282
ENTREES_DE_SATURATION = 564

# B7 — proposeurs
P_VRAIE_BASE = 0.10
P_FAUSSE_BASE = 0.10
GENERATIONS_COURSE_SOURCE = 3
JUSTIFICATION_FIXE = "Tentative écrite par programme ; justification fixe."
PREDICTION_FIXE = (0.3, 0.5, 0.2)  # SILENCE : un vecteur fixe en dixièmes, dans l'ordre de CLASSES

# B7 — étalonnage
SOURCES_ETALONNAGE = 200_000
TOLERANCE_ETALONNAGE = 0.02
SOURCES_FAMILLES_GRANDES = 200_000  # familles D, E, H (écarts)
LOT_DE_SOURCES = 2_000  # SILENCE : taille d'un lot vectorisé (ne change aucune loi : un lot = une étiquette de graine)

# B2 — couche mécanique
SOURCES_COUCHE_MECANIQUE = 24
SOURCES_SOUS_ENSEMBLE_ORGANISME = 2
NIVEAU_PREDICTION_S8 = 0.999

# Estimateurs
REECHANTILLONS = 2_000
TOLERANCE_TAILLE_REALISEE = 0.05

# Annexe C — essai de forme
ESSAI_DE_FORME_MAX_TIRAGES = 200
ESSAI_DE_FORME_MAX_NOMBRES_DE_SOURCES = 2

BRAS_DU_CRITERE = ("1", "2", "3")
BRAS_DE_DIAGNOSTIC = ("4a", "4b")
