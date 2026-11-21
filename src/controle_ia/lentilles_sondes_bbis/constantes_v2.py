"""Constantes de la **seconde passe** : texte de lecture v2 scellé, clés de registre, nos lentilles, seuils.

Texte : `prereg/lecture-sondes-bbis-par-lentilles-v2.md` (`a2bbed7ac34180b69864f143d1a910c8c29687dc73cca359c85256b6d9b78d15`).
Tout ce qui vaut pour les deux passes reste dans `constantes_v1` (non réécrit, R12) ; ce module n'ajoute que ce que la seconde
passe a de neuf. Le texte décide, le code suit.
"""
from __future__ import annotations

from . import constantes_v1 as K
from .constantes_v1 import Arret, FormeMalComprise, Refus  # noqa: F401  (réexportés)

# --- texte et pièces qui font foi (« Documents ») -----------------------------------------------------------------------------------
TEXTE_V2 = "prereg/lecture-sondes-bbis-par-lentilles-v2.md"
EMPREINTE_TEXTE_V2 = "a2bbed7ac34180b69864f143d1a910c8c29687dc73cca359c85256b6d9b78d15"
ADDENDUM = "prereg/lecture-sondes-bbis-par-lentilles-v1-addendum-concentration-v1.md"
EMPREINTE_ADDENDUM = "7c7387088dd5956d3e75bd8e859346dd4db560582fd2f239d2c892b4d2c22970"
# Critère d'identité du réajustement, version 8, scellé (« CI »). La version du critère est celle-ci, par son chemin et son
# empreinte ; elle n'est jamais tirée d'une étiquette du programme de comparaison (champ `critere` de sa sortie).
CRITERE_IDENTITE = "docs/notes/neuron-lens-v1/devis-reajustement/critere-identite-reajustement-lentilles-v8.md"
EMPREINTE_CRITERE_IDENTITE = "541bb86b15088c5cea5a291a294cccdd1067fe39be995b7f9014661f96cb3940"
VERSION_CRITERE_IDENTITE = 8
# Pièce du 18 novembre dont le code lit le champ `meta` seul, pour notre S (CI, § 2).
PIECE_META_S = "diag/20261118-164930-neuron-lens-b-beta/b-beta-ajustement-S.json"
EMPREINTE_PIECE_META_S = "2dce646e32177941c02987a8ba3a0a67fd45d17f335e58ba9e321d3e0367c297"
VERDICT_TRANCHE = "docs/notes/neuron-lens-v1/lecture-b-beta/verdict-b-beta-v1.md"
EMPREINTE_VERDICT_TRANCHE = "3a9b947e0757dd7f5fe7ecb418b047b94fb274fed84672accabc48926660bb78"

# --- clés du registre propre (« Lignes de registre ») ---------------------------------------------------------------------------------
CLE_ADDENDUM = "ADDENDUM-CONCENTRATION-LENTILLES-BBIS"
CLE_SCELLEMENT_V2 = "SCELLEMENT-LENTILLES-BBIS-V2"
CLE_ABANDON_V2 = "ABANDON-LENTILLES-BBIS-V2"
CLE_GO_V2 = "GO-LENTILLES-BBIS-V2"
CLE_CODE_V2 = "CODE-LENTILLES-BBIS-V2"
CLE_RANGEMENT = "RANGEMENT-NOS-LENTILLES-BBIS"
CLE_AVERTISSEMENT = "AVERTISSEMENT-PALIER-2-LENTILLES-BBIS"
CLE_LECTURE_SECONDE_COURSE = "LECTURE-SECONDE-COURSE-NOS-LENTILLES-BBIS"
CLE_NOEUD_AJUSTEMENT_SEUL = "NOEUD-PALIER-2-AJUSTEMENT-SEUL-LENTILLES-BBIS"
CLE_MONTAGE_V2 = "MONTAGE-LENTILLES-BBIS-V2"
CLE_ENTREES_V2 = "ENTREES-LENTILLES-BBIS-V2"
CLE_TABLES_V2 = "TABLES-LENTILLES-BBIS-V2"
CLE_OUVERTURE_V2 = "OUVERTURE-LENTILLES-BBIS-V2"
CLE_LECTURE_V2 = "LECTURE-LENTILLES-BBIS-V2"
CLE_NON_LUES = "NON-LUES-NOS-LENTILLES-BBIS"
CLES_V2 = (CLE_SCELLEMENT_V2, CLE_ABANDON_V2, CLE_GO_V2, CLE_CODE_V2, CLE_RANGEMENT, CLE_AVERTISSEMENT,
           CLE_LECTURE_SECONDE_COURSE, CLE_NOEUD_AJUSTEMENT_SEUL, CLE_MONTAGE_V2, CLE_ENTREES_V2, CLE_TABLES_V2, CLE_OUVERTURE_V2,
           CLE_LECTURE_V2, CLE_NON_LUES)
CLES_EXIGEES_AVANT_TOUT_V2 = (CLE_SCELLEMENT_V2, CLE_GO_V2, CLE_CODE_V2)
# Clés de la première passe que la seconde lit (plan, point 11 ; « Liste d'arrêt »).
CLE_ENTREES_V1 = "ENTREES-LENTILLES-BBIS"
CLE_TABLES_V1 = "TABLES-LENTILLES-BBIS"
CLE_OUVERTURE_V1 = "OUVERTURE-LENTILLES-BBIS"
CLE_LECTURE_V1 = "LECTURE-LENTILLES-BBIS"
# Clé retirée au brouillon 6 (nœud N17, option (a) aux deux paliers) : le code ne l'exige ni ne la lit. Elle n'est nommée ici
# que pour que l'essai contrôle qu'elle n'est dans aucune liste de clés lues.
CLE_RETIREE_ADDENDUM_DE_RECOPIE = "ADDENDUM-RECOPIE-IDENTITE-LENTILLES-BBIS-V2"

# --- lentilles de la seconde passe ---------------------------------------------------------------------------------------------------------
LENTILLE_NOTRE_R, LENTILLE_NOTRE_S = "notre-R", "notre-S"
MOITIE_PAIRE, MOITIE_IMPAIRE = "notre-R-moitie-paire", "notre-R-moitie-impaire"
PLONGEMENTS_SEULS = "plongements-seuls"                 # référence, sans nul, sans p, sans libellé : ce n'est pas une lentille
LENTILLES_V2 = (K.LENTILLE_PUBLIQUE, K.LENTILLE_LOGITS, LENTILLE_NOTRE_R, LENTILLE_NOTRE_S)
LENTILLES_R = (K.LENTILLE_PUBLIQUE, K.LENTILLE_LOGITS, LENTILLE_NOTRE_R)          # celles que la garde du rapport à ε refait ensemble
MOITIES = (MOITIE_PAIRE, MOITIE_IMPAIRE)
NOS_LENTILLES = ("R", "S")
NOM_DE = {"R": LENTILLE_NOTRE_R, "S": LENTILLE_NOTRE_S}

FICHIER_AJUSTEMENT = {"R": "r-llama-3.1-8b-instruct-L32-dclm-T128.pt", "S": "s-llama-3.1-8b-instruct-L32-dclm-T128.pt"}
EMPREINTE_18_NOVEMBRE = {"R": "31061d6c6c4b521c43d4710f9b660184b285467a065dadb5fc48e48c6d48c64c",
                         "S": "aac70eef8f57b5d4423e5c8f8b2e77033b15077d95ef5a81894dbe3e0436e2b8"}
TAILLE_18_NOVEMBRE = {"R": 8_455_720_309, "S": 8_589_938_049}
N_COUCHES_OUT = {"R": 31, "S": 32}                      # `sums[("out", h)]` : [31, 4096, 4096] pour R, [32, 4096, 4096] pour S
N_DOCS = (466, 466)
NEXT_DOC = 932
CHAMPS_META = ("lens", "model", "layers", "model_layers", "targets", "rows_sha256", "docs", "seq_len", "full_length", "basis",
               "modality", "corpus_spec", "dtype")
META_R = {"lens": "R", "model": "meta-llama/Llama-3.1-8B-Instruct", "layers": 32, "model_layers": 32, "targets": ["out", "mid"],
          "rows_sha256": "a6afd972eeaa3566a28d07216efaf75624fda20293c5fab3b7af39277aaf93b3", "docs": 932, "seq_len": 128,
          "full_length": True, "basis": None, "modality": "text", "corpus_spec": "file:dclm.jsonl", "dtype": "bfloat16"}
CIBLES_S = ["mid", "out"]                               # `TARGETS` de `transport.py` pour S
CIBLE_LUE = "out"
TENSEUR_PLONGEMENTS = "model.embed_tokens.weight"
FORME_PLONGEMENTS = (128_256, 4_096)

# --- seuils et gardes neufs --------------------------------------------------------------------------------------------------------------
STABILITE_MAX = 0.10                                    # différence entre moitiés au plus 0,10 dans les deux ajustements
ECART_RELATIF_MATRICES = 1e-3                           # notre R contre l'identité et la lentille publique ; notre S contre R et Rᵀ
HORLOGE_S_V2 = 10 * 3600
DISQUE_DEPART_OCTETS_V2 = 8 * 10 ** 9                   # « au moins 8 Go libres au départ »
RECOUVREMENT_MAX = K.K_JETONS

# --- verdicts d'identité : libellés de CI, § 4, recopiés, jamais reformulés -------------------------------------------------------------
PALIER_1 = "palier 1 — même lentille, octets identiques"
SUITE_REPRISE = " ; reprise sur sauvegarde notée"
PALIER_2 = "palier 2 — différences entre moitiés concordantes à 10⁻³ près ; octets différents ; matrices non comparables"
DIFFERENTE = "différente"
NON_COMPARABLE = "non comparable (traitée comme différente)"
SUSPENDUE = "mention suspendue : anomalie (nœud de Lazar)"
NON_REAJUSTEE = {"R": "R non réajustée", "S": "S non réajustée"}
VARIANTE_AJUSTEMENT_SEUL, VARIANTE_COURSE_REJOUEE = "ajustement seul", "course rejouée"
SECONDE_COURSE_ENTIERE, SECONDE_COURSE_INCOMPLETE = "menée en entier", "incomplète"
AUCUNE = "aucune"
AUCUNE_LIMITE = "aucune limite écrite"
