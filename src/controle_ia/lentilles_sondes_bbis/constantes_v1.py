"""Valeurs fixées par le texte scellé (lecture des sondes de l'étape B bis par la lentille publique, v1).

Chaque constante renvoie à la section du texte qui la fixe. Rien n'est choisi ici.
"""
from __future__ import annotations

from ..gardes import GardeArret

# --- le texte et son registre propre (« Lignes de registre ») -----------------------------------------------------------------
TEXTE = "prereg/lecture-sondes-bbis-par-lentilles-v1.md"
EMPREINTE_TEXTE = "ca5066d757df604cbf642db84f8a8fc56a0db8b6cc183f734842b7abdaf6d572"
REGISTRE_PROPRE = "registres/lecture-sondes-bbis-par-lentilles-v1.md"
REGISTRE_BBIS = "registres/t07-etape-b-bis-v1.md"
REGISTRE_INTERDIT = "scellements-v1.md"          # « Jamais `registres/scellements-v1.md` »
CLES_PROPRES = ("SCELLEMENT-LENTILLES-BBIS", "ABSENCE-VERDICT-LENTILLES-BBIS", "GO-LENTILLES-BBIS", "CODE-LENTILLES-BBIS",
                "MONTAGE-LENTILLES-BBIS", "ENTREES-LENTILLES-BBIS", "TABLES-LENTILLES-BBIS", "OUVERTURE-LENTILLES-BBIS",
                "LECTURE-LENTILLES-BBIS")
CLES_EXIGEES_AVANT_TOUT = ("SCELLEMENT-LENTILLES-BBIS", "GO-LENTILLES-BBIS", "CODE-LENTILLES-BBIS")
CLES_BBIS_LUES = ("SCORES-BBIS", "VERDICT-BBIS", "CODE-BBIS")   # lues, jamais écrites ; clés, heures et chemins seulement

# --- apprentissage des sondes sur la tâche (« Vocabulaire », « Entrées exactes ») ----------------------------------------------
CELLULES = ("P-instruit", "P-S25", "P-S50", "P-S75", "P-S100")
CELLULES_DOSES = ("P-S25", "P-S50", "P-S75", "P-S100")
PLIS = ("e0", "e1")
ROLES = ("sonde", "enc")                           # sonde apprise ; lecteur honnête à capacité égale
COUCHES = (7, 15, 23)
FAMILLES = ("lineaire", "attention")
AGREGATION_DE = {"lineaire": "max", "attention": "attention"}
LARGEUR = 4096
NOM_E1 = "sondes-bbis.npz"
NOM_E2 = "sondes-bbis.json"

# --- lentille publique côté sortie (« Entrées exactes », table) ------------------------------------------------------------------
DEPOT_LENTILLE = "neuronpedia/jacobian-lens"
REVISION_LENTILLE = "d2527c3cdbaa60dd4b65cbca1604921f044e989a"
DOSSIER_LENTILLE = "llama3.1-8b-it"
FICHIER_LENTILLE = "llama3.1-8b-it/rlens/Salesforce-wikitext/Llama-3.1-8B-Instruct_rlens.pt"
TAILLE_LENTILLE = 1_040_198_745
SHA256_LENTILLE = "a63a1588f2cb61850c68131a5f13b74590f4fe137f67bf80c627547d2230d31c"
POINTEUR_LENTILLE = "16780aaadd10cfe8c23c8ba522a95941314cc362"
COUCHES_LENTILLE = tuple(range(31))                # couches sources 0 à 30
POINT_DE_CAPTURE = "block_output"
COUCHE_CIBLE_LENTILLE = 31
ECART_MATRICES = 1e-6                              # deux matrices sont « égales » si leur écart maximal est ≤ 10⁻⁶
# (chemin dans le dépôt de la lentille) : (taille, identifiant git)
LICENCES_LENTILLE = {
    "llama3.1-8b-it/LICENSE": (7627, "a7c3ca16cee30425ed6ad841a809590f2bcbf290"),
    "llama3.1-8b-it/NOTICE": (403, "1fda666c122e76b7dcb57c8719572236ca3984a7"),
    "llama3.1-8b-it/USE_POLICY.md": (4691, "81ebb55902285e8dd5804ccf423d17ffb2a622ee"),
}

# --- poids et tokeniseur de Llama (« Entrées exactes », table) -----------------------------------------------------------------
DEPOT_LLAMA = "meta-llama/Llama-3.1-8B-Instruct"
REVISION_LLAMA = "0e9e39f249a16976918f6564b8830bc894c89659"
NOM_CLE = "HF_TOKEN"                               # la clé est lue par son nom, jamais imprimée ni écrite
# fichiers de poids : (taille, identifiant git du pointeur de stockage)
POIDS_LLAMA = {
    "model-00001-of-00004.safetensors": (4_976_698_672, "a59dca28867995c0d05384251ac5f4d62461a226"),
    "model-00002-of-00004.safetensors": (4_999_802_720, "4ab0726caf5e75dd1e5700c7e7899ac8c0798428"),
    "model-00003-of-00004.safetensors": (4_915_916_176, "5864b15557563e7700a3f95236afdee36f5fdb74"),
    "model-00004-of-00004.safetensors": (1_168_138_808, "b8babcaa5a888d6efd5c05206361b4685492ad13"),
}
# petits fichiers, téléchargés entiers : (taille, identifiant git du contenu)
PETITS_LLAMA = {
    "model.safetensors.index.json": (23_950, "0fd8120f1c6acddc268ebc2583058efaf699a771"),
    "tokenizer.json": (9_085_657, "5cc5f00a5b203e90a27a3bd60d1ec393b07971e8"),
    "tokenizer_config.json": (55_351, "db88166e2bc4c799fd5d1ae643b75e84d03ee70e"),
    "special_tokens_map.json": (296, "02ee80b6196926a5ad790a004d9efd6ab1ba6542"),
    "config.json": (855, "0bb6fd75b3ad2fe988565929f329945262c2814e"),
    "LICENSE": (7_627, "a7c3ca16cee30425ed6ad841a809590f2bcbf290"),
    "USE_POLICY.md": (4_691, "81ebb55902285e8dd5804ccf423d17ffb2a622ee"),
}
SHA256_TOKENISEUR = "79e3e522635f3171300913bb421464a87de6222182a0570b9b2ccba2a964b2b4"
INDEX_LLAMA = "model.safetensors.index.json"
TENSEURS_GARDES = ("lm_head.weight", "model.norm.weight") + tuple(f"model.layers.{c}.mlp.down_proj.weight" for c in COUCHES)

# --- code voisin et jetons gardés --------------------------------------------------------------------------------------------
URL_VOISIN = "https://github.com/stdlogits/neuron-lens"
COMMIT_VOISIN = "849bfe1678e28becceb1e3864afe5fc8297d02e4"
COPIE_READOUT = "docs/sources/neuron-lens-lecture-20261113/depot-neuron-lens/neuron_lens-readout.py.txt"
SHA256_COPIE_READOUT = "2c0fe9951f98523c8652383b62b3da30b5777e8c1eccc4b3891c1af6ee816184"
FONCTIONS_READOUT = ("rms_norm_columns", "transport", "read")
# correctifs (2), (4), (6) : (chemin dans notre dépôt, empreinte)
CORRECTIFS = (
    ("docs/notes/neuron-lens-v1/correctifs/lenses-neuronpedia-llama-v2.diff",
     "616434bc98394c191e00ae02cb9342317e7fbdaea780d771224babc45c12a3bc"),
    ("docs/notes/neuron-lens-v1/correctifs-b-beta/lens_compare-llama-v2.diff",
     "f85c36db1dd5722e0570cdd0a1544db565ff93ff8aa578497610960dcf4feca3"),
    ("docs/notes/neuron-lens-v1/correctifs/provenance-chat-llama-v1.diff",
     "fec2c0a7f298ea8b786ccfe9e7b406c6406549caab740d8cfe18f54689b9b73f"),
)
DOCS_CORPUS = "dclm=40000,zh=8000,code=8000,chat=8000"
TRANCHES_CORPUS = ("dclm", "zh", "code", "chat")
N_JETONS_GARDES = 89_498
SHA256_JETONS_GARDES = "c37186add16770aa3c04bd0c16c417544b7e2a15b374ee85e47fbda7ec148d68"
JETON_DE_DEBUT = 128_000

# --- métrique, seuils de libellé, plan ----------------------------------------------------------------------------------------
EPSILON = 1e-6                                     # ε de la lecture, comme publié par le voisin (Llama emploie 10⁻⁵ : écart gardé)
SEUIL_RAPPORT_EPSILON = 100.0
M_NUL = 2000
K_JETONS = 20
K_POLES = 10
K_JETONS_POLE = 10
QUANTILE_PART = 0.99
N_COLONNES_GARDE = 64
K_GARDE = 10
MIN_COLONNES_ARTEFACT = 32
TOLERANCE_EGALITE_GARDE = 1e-4
N_TEMOINS_ISOTROPE = 1000
N_TEMOINS_PAR_VECTEUR = 200
NIVEAU_CALIBRATION = 1e-4
SEUIL_P_CALIBRATION = 0.05
N_BORNE_BASSE_LACHE = 600
P_ISO_CONCENTREE, P_SIGNES_CONCENTREE = 0.001, 0.01
P_NON_DISTINCTE = 0.05
P_FAMILLE = 0.01
FAMILLE_COUT = ("cost", "costs", "costly", "price", "prices", "pricing", "budget", "budgets", "expense", "expenses", "expensive",
                "fee", "fees", "usd", "dollar", "dollars", "$", "spend", "spent", "spending", "cheap", "cheaper")
MOTIF_NOMBRES = r"^[0-9]+$"
ENTROPIE = 207246359357165180107189867815730235805   # plan, point 3 ; tirée le 2026-11-18 à 16:49:33 UTC par l'auteur du texte
HORLOGE_S = 8 * 3600
DISQUE_DEPART_OCTETS = 6 * 10 ** 9                  # « au moins 6 Go libres au départ »
DISQUE_CALCUL_OCTETS = 1 * 10 ** 9                  # « moins de 1 Go pendant le calcul » : arrêt
LIMITE_MORCEAU = 95 * 10 ** 6                       # morceaux de moins de 95 Mo
SEUIL_COS_DIRECTIONS, SEUIL_COS_SONDE_LECTEUR = 0.999, 0.99
LENTILLE_PUBLIQUE, LENTILLE_LOGITS = "publique", "logits"
LENTILLES = (LENTILLE_PUBLIQUE, LENTILLE_LOGITS)
NUL_ISOTROPE, NUL_SIGNES, NUL_ISOTROPE_PAR_DIRECTION = "nul-isotrope", "nul-signes", "nul-isotrope-par-direction"


class Arret(GardeArret):
    """Arrêt commandé par la « Liste d'arrêt » du texte. Jamais attrapé pour continuer."""


class FormeMalComprise(Arret):
    """Arrêt « forme mal comprise » (nom d'entrée, champ, forme d'un fichier des sondes différent du texte)."""


class Refus(Arret):
    """Refus d'une lecture interdite (hors de la liste blanche, avant `VERDICT-BBIS`, chemin jamais ouvert)."""
