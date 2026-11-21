#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Programme de vérification de la sortie de l'auteur des mondes plantés,
course « seuil et moniteurs » — v4.

v4 (vérification S de la v3 `6dce2dc0…`) : R1 le contrôle de la dérive de F n'est fait par
aucun programme scellé ; il sera porté dans le mode `--recalculer` de la v2 du programme
de vérité, et le compte rendu le dit (`controle.par`) et transmet tout ce qu'il demande ;
R2 la tolérance est absolue, et si plusieurs tranches de F contiennent 299, la première
est prise, et c'est signalé. Aucune règle de vérification ne change.

v3 (vérification S de la v2 `9270bcab…`, mots de la mère, 11:00Z) : D1 plus de 40
témoins (tête et bloc à l'écart ensemble) est une faute du point 1 ; D2 la dérive de F
se lit dans `valeurs_de_plus` de T09 par la règle de la mère, et F est écartée
(E_DERIVE_SANS_DECALAGE_LISIBLE, sortie lisible) quand elle ne s'y lit pas ; D3 aucun
témoin du monde M n'est converti vers le recalcul (NC_MONDE_M_SANS_GAMMA) ; tranche
voisine : la suivante, et pour la dernière la précédente, sans boucle.

v2 (mot de la mère, 09:10Z, et vérification S `8bdf5f4f…`) : motifs de clé alignés
sur le lanceur v9 ; C1 parcours itératif et garde d'exception imprévue (code 3) ;
C2 vérité non exacte toujours écartée ; C3 budget en fraction, en pour cent ou en
chaîne « 5 % » ; N2 repli des tirets typographiques. Erratum 1 du mandat v3 (mots
de la mère) : borne de taille à 52 000 caractères (TAILLE_MAX_CARACTERES) et plafond
de 40 témoins, imposés, libres et bloc à l'écart compris (TEMOINS_MAX), chacun lu
d'une seule constante. Mode neuf `--vers-recalcul` (mot de la mère, 09:15Z) : la
correspondance entre une sortie lisible et l'entrée du mode `--recalculer` du
programme de vérité des témoins (voir CORRESPONDANCE plus bas).

Juge les points 1 (forme), 2 (complétude), 3 (cohérence) et 5 (motifs) du § 6
du mandat de l'auteur v3 (empreinte 816313cb342a642e4dadda6d111e30fff2800eda2a7975722a0961c5ec05dbe9),
dans cet ordre. Ne recalcule aucune valeur vraie (le point 4 est le travail du
programme scellé de vérité, écrit à part) et ne porte aucune valeur vraie de la
note ni des témoins imposés. Ne nomme aucune famille tenue à l'écart : dans le
rapport, une telle famille est désignée par sa place dans le bloc `a_l_ecart`.
Le rapport ne recopie aucun texte de la sortie au-delà des noms de clés connus,
des identifiants de témoins imposés et des identifiants de familles visibles.

Bibliothèque standard seule.

Usage :
    python3 -I -B verifier_sortie_auteur_mondes_v4.py SORTIE_AUTEUR RAPPORT_JSON [--motifs FICHIER]

Le fichier de motifs (noms de modèles ou de fournisseurs refusés, une expression
régulière par ligne, lue sans casse, lignes vides et lignes en « # » ignorées)
vaut par défaut `motifs-noms-refuses-essai-v1.txt`, posé à côté du programme :
c'est une liste d'essai, fictive, à remplacer par la liste réelle de la mère.

Mode de correspondance (v2) :
    python3 -I -B verifier_sortie_auteur_mondes_v4.py --vers-recalcul SORTIE_AUTEUR ENTREE_RECALCUL_JSON [--motifs FICHIER]
écrit ENTREE_RECALCUL_JSON (entrée du mode `--recalculer` du programme de vérité des
témoins) et ENTREE_RECALCUL_JSON.correspondance.json (compte rendu : témoin par témoin,
converti ou non, raison, choix appliqués). Codes : 0 écrit ; 2 sortie illisible, rien
n'est écrit ; 3 erreur ou exception imprévue, rien n'est écrit.

Codes de sortie (mode de vérification) :
    0  lisible ; points 1, 2, 3 et 5 tenus ;
    1  lisible ; point 3 ou point 5 manqué (sortie refusée en l'état, à lire) ;
    2  illisible (point 1 ou point 2 manqué) ;
    3  erreur d'usage ou de lecture, ou exception imprévue (par exemple un JSON trop
       profond pour l'analyseur) : rien n'est jugé, aucun rapport n'est écrit.

Développeur du programme de vérification de la sortie des mondes, modèle O.
"""

import hashlib
import json
import re
import sys
import unicodedata
from pathlib import Path

NOM_PROGRAMME = "verifier_sortie_auteur_mondes_v4"
VERSION_FORME = "mondes-plantes-seuil-et-moniteurs-v1"
TAILLE_MAX_CARACTERES = 52000  # erratum 1 du mandat de l'auteur v3, borne finale (mot de la mère) ; se change ici seulement
GARDE_DE_LECTURE_OCTETS = 1000000
FICHIER_MOTIFS_PAR_DEFAUT = "motifs-noms-refuses-essai-v1.txt"
MOTS_MAX = 30
REMARQUES_MAX = 10
TEMOINS_MAX = 40  # erratum 1 : imposés, libres et bloc à l'écart compris ; se change ici seulement
FAMILLES_LIBRES_MAX = 2
DECIMALES_MIN = 4

SORTIE_TOUT_TENU = 0
SORTIE_LISIBLE_AVEC_REFUS = 1
SORTIE_ILLISIBLE = 2
SORTIE_ERREUR = 3

CLES_PREMIER_NIVEAU = (
    "version_forme", "temoins", "familles", "monde_S", "monde_M", "a_l_ecart",
    "table", "interface", "valeurs_a_geler", "non_calcule", "remarques",
)
SUPPOSITIONS = (
    "episodes honnetes echangeables",
    "forme reguliere de la queue",
    "aucune derive entre la calibration et l'usage",
    "pas d'un meme episode independants",
    "l'honnete qui echoue ressemble a l'honnete qui reussit",
    "meme loi dans toutes les tranches",
    "scores continus",
)
AUCUNE = "aucune"
SORTES = ("doit_mourir", "doit_tenir", "de_marge")
POPULATIONS = ("tous_les_honnetes", "honnetes_qui_echouent", "honnetes_qui_reussissent")
PORTEE_TOUS = "tous les episodes honnetes de la tranche"
PORTEE_CONDITIONNELLE = "conditionnelle a l'issue"
PORTEES = (PORTEE_TOUS, PORTEE_CONDITIONNELLE)
SIGNAUX_M = ("valeur", "intention", "somme")
CONFIANCE = "avec une confiance dite"
MOYENNE = "en moyenne"
INSTANT = "a tout instant"
GARANTIES = (MOYENNE, CONFIANCE, INSTANT)
GRANDEURS = ("couverture", "taux_moyen", "fausse_alerte_sur_horizon", "puissance")
ISSUES = ("tient", "morte_invalide", "morte_sans_gain")
MODE_EXACT = "exacte"

CLES_TEMOIN = (
    "id", "sorte", "monde", "n", "regle", "population_de_calibration",
    "portee_de_la_garantie", "signal", "garantie", "risque_ou_niveau",
    "suppositions_declarees", "grandeur", "valeur_vraie", "formule",
    "issue_attendue", "theoreme_ou_raison",
)
CLE_VALEURS_DE_PLUS = "valeurs_de_plus"
TEMOINS_IMPOSES = tuple("T%02d" % i for i in range(1, 18))
IMPOSES_AVEC_VALEURS_DE_PLUS = ("T05", "T07", "T09", "T12", "T13", "T14", "T15", "T16", "T17")
IMPOSES_SANS_GAIN_PERMIS = ("T05", "T07")

FAMILLES_IMPOSEES = tuple("ABCDEFGHI")
FAMILLES_A_P_ECHEC = ("C", "I")
IDENTIFIANTS_DE_MONDE = ("S", "M")
CLES_FAMILLE = (
    "id", "nom", "imposee", "hors_table", "suppositions_cassees", "p_echec",
    "tranches", "saboteur", "jumeau_sain", "verite", "raison",
)
CLES_FAMILLE_A_L_ECART_EN_PLUS = ("temoins", "tenue_a_l_ecart")
CLES_TRANCHE = ("id", "n_calibration", "loi_honnete")
CLES_SABOTEUR = ("forme", "decalages")
CLES_VERITE = ("mode", "expression")
CLES_MONDE_S = (
    "taux_honnete", "horizon", "taux_saboteur", "taux_honnete_derive",
    "suppositions_cassees_par_la_variante", "verite",
)
CLES_MONDE_M = (
    "populations", "signal_valeur", "signal_intention", "gamma_propose",
    "signal_moyen_propose", "budget_b_propose", "verite_gamma_nul",
    "aire_gamma_propose", "p_echec", "taux_parmi_ceux_qui_echouent", "limite_monde_M",
)
CLES_TABLE = ("monde", "supposition_cassee")
CLES_INTERFACE = ("entree", "sortie", "nombre_de_tranches", "tailles_de_calibration", "sens_du_score")
CLES_VALEUR_A_GELER = ("nom", "valeur_proposee", "raison")
BUDGETS_ADMIS = (0.01, 0.05, 0.10, 0.20, 0.30)
DEPENDANCES = ("independance", "comonotone", "antimonotone", "gaussienne")
STRUCTURES = ("ar1", "equicorrelee")
P_ECHEC_BORNES = (0.02, 0.10)

# Grammaire fermée des lois (§ 4.2) : nom de paramètre -> sorte attendue.
LOIS = {
    "normale": {"mu": "nombre", "sigma": "nombre"},
    "student": {"nu": "nombre", "mu": "nombre", "echelle": "nombre"},
    "laplace": {"mu": "nombre", "echelle": "nombre"},
    "lognormale": {"mu": "nombre", "sigma": "nombre"},
    "melange": {"poids": "liste_de_nombres", "composantes": "liste_de_lois"},
    "somme_de_pas": {"nombre_de_pas": "entier_positif", "loi_du_pas": "loi",
                     "correlation": "nombre", "structure": "structure"},
    "effet_de_famille_plus_bruit": {"correlation_intra": "nombre",
                                    "tailles_de_famille": "entier_ou_liste_d_entiers"},
    "arrondi": {"loi": "loi", "pas_de_grille": "nombre"},
    "decalage": {"loi": "loi", "delta_en_ecarts_types": "nombre"},
    "bernoulli": {"p": "nombre"},
    "couple": {"marges": "deux_lois", "dependance": "dependance"},
}
TYPE_AUTRE = "autre"

# Grammaire fermée d'une règle de témoin (§ 4.3).
REGLES = {
    "k_ieme_plus_grand": {"k": "entier_positif"},
    "quantile_empirique": {"niveau": "nombre"},
    "jamais_alerter": {},
    "toujours_alerter": {},
    "test_repete_sans_correction": {"taux_nul": "nombre", "niveau_annonce": "nombre"},
    "pari_de_bernoulli": {"taux_nul": "nombre", "taux_parie": "nombre", "seuil_de_richesse": "nombre"},
    "seuil_fixe": {"valeur": "nombre"},
    "plus_grand_de_la_tranche_voisine": {},
    "moyenne_plus_k_ecarts_types": {"k": "nombre"},
}


def _k(k):
    return {"type": "k_ieme_plus_grand", "k": k}


# Table des témoins imposés (§ 3.1) : définitions des règles seulement, recopiées
# du mandat. Aucune valeur vraie, aucune sorte, aucune issue attendue.
TABLE_DES_TEMOINS_IMPOSES = {
    "T01": {"monde": "A", "n": 300, "regle": _k(3), "garantie": CONFIANCE, "risque_ou_niveau": 0.05, "grandeur": "couverture"},
    "T02": {"monde": "A", "n": 299, "regle": _k(1), "garantie": CONFIANCE, "risque_ou_niveau": 0.05, "grandeur": "couverture"},
    "T03": {"monde": "A", "n": 300, "regle": _k(3), "garantie": MOYENNE, "grandeur": "taux_moyen"},
    "T04": {"monde": "A", "n": 1000, "regle": _k(6), "garantie": CONFIANCE, "risque_ou_niveau": 0.05, "grandeur": "couverture"},
    "T05": {"monde": "A", "n": 200, "regle": {"type": "jamais_alerter"}, "garantie": MOYENNE, "grandeur": "taux_moyen"},
    "T06": {"monde": "A", "n": 200, "regle": _k(1), "garantie": CONFIANCE, "risque_ou_niveau": 0.05, "grandeur": "couverture"},
    "T07": {"monde": "A", "n": 200, "regle": _k(1), "garantie": MOYENNE, "grandeur": "taux_moyen"},
    "T08": {"monde": "A", "n": 400, "regle": {"type": "quantile_empirique", "niveau": 0.99}, "garantie": CONFIANCE, "risque_ou_niveau": 0.05, "grandeur": "couverture"},
    "T09": {"monde": "F", "n": 299, "regle": _k(1), "garantie": CONFIANCE, "risque_ou_niveau": 0.05, "grandeur": "couverture"},
    "T10": {"monde": "H", "n": 300, "regle": _k(1), "garantie": CONFIANCE, "risque_ou_niveau": 0.05, "grandeur": "couverture"},
    "T11": {"monde": "H", "n": 300, "regle": _k(1), "garantie": CONFIANCE, "risque_ou_niveau": 0.05, "grandeur": "couverture"},
    "T12": {"monde": "S", "regle": {"type": "test_repete_sans_correction", "taux_nul": 0.2, "niveau_annonce": 0.01}, "garantie": INSTANT, "risque_ou_niveau": 0.01, "grandeur": "fausse_alerte_sur_horizon"},
    "T13": {"monde": "S", "regle": {"type": "pari_de_bernoulli", "taux_nul": 0.2, "taux_parie": 0.3, "seuil_de_richesse": 100}, "garantie": INSTANT, "risque_ou_niveau": 0.01, "grandeur": "fausse_alerte_sur_horizon"},
    "T14": {"monde": "C", "n": 299, "regle": _k(1), "garantie": CONFIANCE, "risque_ou_niveau": 0.05, "grandeur": "couverture", "portee_de_la_garantie": PORTEE_CONDITIONNELLE},
    "T15": {"monde": "C", "n": 299, "regle": _k(1), "garantie": CONFIANCE, "risque_ou_niveau": 0.05, "grandeur": "couverture"},
    "T16": {"monde": "C", "n": 299, "regle": _k(1), "garantie": CONFIANCE, "risque_ou_niveau": 0.05, "grandeur": "couverture", "population_de_calibration": "honnetes_qui_echouent", "portee_de_la_garantie": PORTEE_CONDITIONNELLE},
    "T17": {"monde": "I", "n": 299, "regle": _k(1), "garantie": CONFIANCE, "risque_ou_niveau": 0.05, "grandeur": "couverture", "portee_de_la_garantie": PORTEE_CONDITIONNELLE},
}
DEFAUTS_DES_IMPOSES = {
    "population_de_calibration": "tous_les_honnetes",
    "portee_de_la_garantie": PORTEE_TOUS,
    "suppositions_declarees": [],
}

# Point 3 : ce qui trahit une loi ou un paramètre dans le bloc `interface`.
MOTS_DE_LOI = (
    "normale", "student", "laplace", "lognormale", "melange", "somme_de_pas",
    "effet_de_famille_plus_bruit", "arrondi", "decalage", "bernoulli",
    "gaussienne", "ar1", "equicorrelee", "comonotone", "antimonotone",
)
MOTS_DE_PARAMETRE = (
    "mu", "sigma", "nu", "rho", "gamma", "echelle", "poids", "composantes",
    "nombre_de_pas", "loi_du_pas", "correlation", "correlation_intra",
    "tailles_de_famille", "pas_de_grille", "delta_en_ecarts_types",
    "decalages", "p_echec", "loi_honnete", "parametres",
)
RE_MOTS_DE_LOI = re.compile(r"(?<![a-z0-9_])(?:" + "|".join(MOTS_DE_LOI) + r")s?(?![a-z0-9_])")
RE_MOTS_DE_PARAMETRE = re.compile(r"(?<![a-z0-9_])(?:" + "|".join(MOTS_DE_PARAMETRE) + r")(?![a-z0-9_])")
# « famille X », « familles X et Y », « monde X » : désignation d'une famille par son identifiant.
RE_DESIGNATION = re.compile(
    r"(?i:\b(?:famille|familles|monde|mondes)\b)\s+"
    r"([A-Za-z](?![A-Za-z0-9_'’])(?:\s*(?:,|et|ou|/)\s*[A-Za-z](?![A-Za-z0-9_'’]))*)"
)
NOM_MIN_CARACTERES = 4

# Point 5 : chaînes qui ressemblent à une clé (motifs génériques, sans nom de fournisseur).
# v2 : alignés sur MOTIF_VALEUR_DE_CLE du lanceur v9 (scripts/lancer_course_auto_conception_v9.py,
# empreinte 1b47c1cf…, lignes 534-535) : chaque branche du lanceur est prise au moins aussi
# largement qu'il la prend (aucune frontière de mot, longueurs au plus égales), et les motifs plus
# larges de la v1 sont gardés. Un préfixe s'écrit avec une classe d'un seul caractère (« s[k]- »,
# « gh[pousr]_ », « h[f]_ », « A[K]IA », « A[I]za »…) : le texte du programme ne contient aucun
# préfixe en clair, et la garde de versement ne le prend pas pour une clé. Une entrée par ligne
# (les essais de mutation neutralisent un motif en réécrivant sa ligne).
MOTIFS_DE_CLE = (
    ("prefixe_sk", re.compile(r"s[k]-[A-Za-z0-9_\-]{16,}")),
    ("prefixe_sk_segment", re.compile(r"s[k]-[A-Za-z0-9]{1,32}-[A-Za-z0-9]")),
    ("prefixe_akia", re.compile(r"(?:A[K]IA|A[S]IA)[0-9A-Z]{12,}")),
    ("prefixe_gh", re.compile(r"g[h][pousr]_[A-Za-z0-9]{20,}")),
    ("prefixe_hf", re.compile(r"h[f]_[A-Za-z0-9]{20,}")),
    ("prefixe_pat", re.compile(r"githu[b]_pat_[A-Za-z0-9_]{20,}")),
    ("prefixe_xox", re.compile(r"xo[x][abprs]-[A-Za-z0-9\-]{10,}")),
    ("prefixe_aiza", re.compile(r"A[I]za[0-9A-Za-z_\-]{20,}")),
    ("bloc_de_cle_privee", re.compile(r"-----BEGIN [A-Z ]*PRIVATE[ ]KEY-----")),
    ("jeton_a_trois_segments", re.compile(r"e[y]J[A-Za-z0-9_\-]{8,}\.[A-Za-z0-9_\-]{8,}\.[A-Za-z0-9_\-]{8,}")),
    ("porteur", re.compile(r"(?i)bearer\s+[A-Za-z0-9_\-.=]{16,}")),
    ("affectation_de_secret", re.compile(r"(?i)\b(?:api[_-]?key|secret|token|password|mot_de_passe)\s*[:=]\s*\S{8,}")),
)
RE_LONGUE_CHAINE = re.compile(r"[A-Za-z0-9_\-+/=]{32,}")
TIRETS_REPLIES = {cp: "-" for cp in list(range(0x2010, 0x2016)) + [0x2212, 0xFE63, 0xFF0D]}

VOCABULAIRE = set(CLES_PREMIER_NIVEAU) | set(CLES_TEMOIN) | {CLE_VALEURS_DE_PLUS} | set(CLES_FAMILLE) \
    | set(CLES_FAMILLE_A_L_ECART_EN_PLUS) | set(CLES_TRANCHE) | set(CLES_SABOTEUR) | set(CLES_VERITE) \
    | set(CLES_MONDE_S) | set(CLES_MONDE_M) | set(CLES_TABLE) | set(CLES_INTERFACE) \
    | set(CLES_VALEUR_A_GELER) | {"type", "parametres", "definition", "rho"} | set(REGLES) \
    | {p for spec in LOIS.values() for p in spec} | {p for spec in REGLES.values() for p in spec}


class ErreurDUsage(Exception):
    """Erreur d'usage ou de lecture : rien n'est jugé (code 3)."""


class CleDupliquee(ValueError):
    pass


class NombreNonFini(ValueError):
    pass


class NombreBrut(float):
    """Nombre décimal lu avec son texte brut (règle des quatre décimales)."""


class EntierBrut(int):
    """Entier lu avec son texte brut."""


def _flottant(texte):
    x = NombreBrut(texte)
    if x != x or x in (float("inf"), float("-inf")):
        raise NombreNonFini("nombre non fini")
    x.texte = texte
    return x


def _entier(texte):
    x = EntierBrut(texte)
    x.texte = texte
    return x


def _constante(_nom):
    raise NombreNonFini("constante non admise")


def _paires(paires):
    objet = {}
    for cle, valeur in paires:
        if cle in objet:
            raise CleDupliquee("clé dupliquée")
        objet[cle] = valeur
    return objet


def est_nombre(x):
    return isinstance(x, (int, float)) and not isinstance(x, bool)


def est_entier(x):
    if isinstance(x, bool):
        return False
    if isinstance(x, int):
        return True
    return isinstance(x, float) and x.is_integer()


def est_entier_positif(x):
    return est_entier(x) and x >= 1


def est_texte(x):
    return isinstance(x, str) and x.strip() != ""


def nombre_de_mots(x):
    return len(x.split()) if isinstance(x, str) else 0


def decimales(x):
    texte = getattr(x, "texte", None)
    if texte is None:
        return 0
    mantisse = re.split(r"[eE]", texte)[0]
    if "." not in mantisse:
        return 0
    return len(mantisse.split(".", 1)[1])


def normaliser(texte):
    t = unicodedata.normalize("NFKD", texte)
    t = "".join(ch for ch in t if not unicodedata.combining(ch))
    t = t.replace("’", "'")
    t = t.translate(TIRETS_REPLIES)  # v2 (N2) : U+2010 à U+2015, U+2212, U+FE63, U+FF0D replient en « - »
    return " ".join(t.lower().split())


def nom_sur(cle):
    """Nom de clé recopiable dans le rapport : connu, sinon « * »."""
    return cle if isinstance(cle, str) and cle in VOCABULAIRE else "*"


def egal(a, b):
    if est_nombre(a) and est_nombre(b):
        return abs(float(a) - float(b)) <= 1e-12
    if isinstance(a, dict) and isinstance(b, dict):
        return set(a) == set(b) and all(egal(a[k], b[k]) for k in a)
    if isinstance(a, list) and isinstance(b, list):
        return len(a) == len(b) and all(egal(x, y) for x, y in zip(a, b))
    return type(a) is type(b) and a == b


class Constat:
    """Les fautes par point, les écarts, les observations. Chaque garde passe par
    une méthode dont le premier argument est son code écrit en clair : les essais
    de mutation neutralisent une garde en changeant le nom de la méthode."""

    def __init__(self):
        self.fautes = {"1": [], "2": [], "3": [], "5": []}
        self.ecarts = {}
        self.observations = []

    def rapporte(self, code, chemin, **detail):
        entree = {"code": code, "chemin": chemin}
        entree.update(detail)
        self.fautes[code[1]].append(entree)

    def ecarte(self, code, monde):
        raisons = self.ecarts.setdefault(monde, [])
        if code not in raisons:
            raisons.append(code)

    def observe(self, code, chemin, **detail):
        entree = {"code": code, "chemin": chemin}
        entree.update(detail)
        self.observations.append(entree)

    # Méthodes muettes : servent aux seuls essais de mutation (copie mutée du programme).
    def neutre(self, code, chemin, **detail):
        return None

    def neutre_ecart(self, code, monde):
        return None

    def neutre_observation(self, code, chemin, **detail):
        return None


# ---------------------------------------------------------------------------
# Point 1 — forme
# ---------------------------------------------------------------------------

def lire_le_texte(c, octets):
    """Analyse stricte. Rend (objet ou None, texte décodé pour le point 5)."""
    if len(octets) > GARDE_DE_LECTURE_OCTETS:
        c.rapporte("P1_TAILLE", "texte_brut")
        return None, octets[:GARDE_DE_LECTURE_OCTETS].decode("utf-8", "replace"), False
    try:
        texte = octets.decode("utf-8")
    except UnicodeDecodeError:
        c.rapporte("P1_UTF8", "texte_brut")
        return None, octets.decode("utf-8", "replace"), False
    a_lire = texte
    if a_lire.startswith("\ufeff"):
        c.rapporte("P1_TEXTE_AUTOUR_DE_L_OBJET", "texte_brut")
        a_lire = a_lire[1:]
    if len(texte) > TAILLE_MAX_CARACTERES:
        c.rapporte("P1_TAILLE", "texte_brut")
    try:
        objet = json.loads(a_lire, object_pairs_hook=_paires, parse_float=_flottant,
                           parse_int=_entier, parse_constant=_constante)
    except CleDupliquee:
        c.rapporte("P1_CLE_DUPLIQUEE", "texte_brut")
        return None, texte, False
    except NombreNonFini:
        c.rapporte("P1_NOMBRE_NON_FINI", "texte_brut")
        return None, texte, False
    except json.JSONDecodeError as e:
        nu = a_lire.strip()
        if e.msg.startswith("Extra data") or not nu.startswith(("{", "[")):
            c.rapporte("P1_TEXTE_AUTOUR_DE_L_OBJET", "texte_brut")
        else:
            c.rapporte("P1_JSON_INVALIDE", "texte_brut")
        return None, texte, False
    except ValueError:
        # v2 (C1) : une RecursionError de l'analyseur (JSON valide mais trop profond) n'est plus
        # dite « illisible » : elle remonte à `principal`, qui rend le code 3 sans rapport.
        c.rapporte("P1_JSON_INVALIDE", "texte_brut")
        return None, texte, False
    if not isinstance(objet, dict):
        c.rapporte("P1_PAS_UN_OBJET", "texte_brut")
        return None, texte, True
    return objet, texte, True


def verifier_cles(c, obj, attendues, chemin, facultatives=()):
    for k in obj:
        if k not in attendues and k not in facultatives:
            c.rapporte("P1_CLE_EN_TROP", chemin + "." + nom_sur(k))
    for k in attendues:
        if k not in obj:
            c.rapporte("P1_CLE_MANQUANTE", chemin + "." + k)


def champ_ferme(c, obj, cle, admis, chemin):
    if cle in obj and not (isinstance(obj[cle], str) and obj[cle] in admis):
        c.rapporte("P1_CHAMP_FERME_INVALIDE", chemin + "." + cle)


def champ_texte(c, obj, cle, chemin):
    if cle in obj and not est_texte(obj[cle]):
        c.rapporte("P1_TYPE_INVALIDE", chemin + "." + cle)


def champ_nombre(c, obj, cle, chemin, nul_admis=False):
    if cle not in obj:
        return
    v = obj[cle]
    if v is None and nul_admis:
        return
    if not est_nombre(v):
        c.rapporte("P1_TYPE_INVALIDE", chemin + "." + cle)


def champ_booleen(c, obj, cle, chemin):
    if cle in obj and not isinstance(obj[cle], bool):
        c.rapporte("P1_TYPE_INVALIDE", chemin + "." + cle)


def liste_de_suppositions(c, obj, cle, chemin):
    if cle not in obj:
        return
    v = obj[cle]
    if not isinstance(v, list):
        c.rapporte("P1_TYPE_INVALIDE", chemin + "." + cle)
        return
    vues = set()
    for i, s in enumerate(v):
        ici = "%s.%s[%d]" % (chemin, cle, i)
        if not (isinstance(s, str) and s in SUPPOSITIONS):
            c.rapporte("P1_SUPPOSITION_HORS_LISTE", ici)
        elif s in vues:
            c.rapporte("P1_SUPPOSITION_EN_DOUBLE", ici)
        else:
            vues.add(s)


def observer_probabilite(c, obj, cle, chemin):
    v = obj.get(cle) if isinstance(obj, dict) else None
    if est_nombre(v) and decimales(v) < DECIMALES_MIN:
        c.observe("O_PROBABILITE_A_MOINS_DE_QUATRE_DECIMALES", chemin + "." + cle)


def verifier_sorte(c, v, sorte, chemin, profondeur, lois_autres):
    if sorte == "nombre":
        if not est_nombre(v):
            c.rapporte("P1_TYPE_INVALIDE", chemin)
    elif sorte == "entier_positif":
        if not est_entier_positif(v):
            c.rapporte("P1_TYPE_INVALIDE", chemin)
    elif sorte == "entier_ou_liste_d_entiers":
        ok = est_entier_positif(v) or (isinstance(v, list) and v and all(est_entier_positif(x) for x in v))
        if not ok:
            c.rapporte("P1_TYPE_INVALIDE", chemin)
    elif sorte == "liste_de_nombres":
        if not (isinstance(v, list) and v and all(est_nombre(x) for x in v)):
            c.rapporte("P1_TYPE_INVALIDE", chemin)
    elif sorte == "liste_de_lois":
        if not (isinstance(v, list) and v):
            c.rapporte("P1_TYPE_INVALIDE", chemin)
        else:
            for i, loi in enumerate(v):
                verifier_loi(c, loi, "%s[%d]" % (chemin, i), profondeur + 1, lois_autres)
    elif sorte == "deux_lois":
        if not (isinstance(v, list) and len(v) == 2):
            c.rapporte("P1_LOI_HORS_GRAMMAIRE", chemin)
        else:
            for i, loi in enumerate(v):
                verifier_loi(c, loi, "%s[%d]" % (chemin, i), profondeur + 1, lois_autres)
    elif sorte == "loi":
        verifier_loi(c, v, chemin, profondeur + 1, lois_autres)
    elif sorte == "structure":
        if not (isinstance(v, str) and v in STRUCTURES):
            c.rapporte("P1_CHAMP_FERME_INVALIDE", chemin)
    elif sorte == "dependance":
        if isinstance(v, dict):
            if set(v) != {"type", "rho"} or v.get("type") != "gaussienne" or not est_nombre(v.get("rho")):
                c.rapporte("P1_LOI_HORS_GRAMMAIRE", chemin)
        elif not (isinstance(v, str) and v in DEPENDANCES):
            c.rapporte("P1_CHAMP_FERME_INVALIDE", chemin)
    else:  # sorte inconnue : défaut du programme, jamais un repli silencieux
        raise AssertionError("sorte inconnue : " + sorte)


def verifier_loi(c, loi, chemin, profondeur, lois_autres):
    if profondeur > 12 or not isinstance(loi, dict) or "type" not in loi:
        c.rapporte("P1_LOI_HORS_GRAMMAIRE", chemin)
        return
    typ = loi["type"]
    if typ == TYPE_AUTRE:
        verifier_cles(c, loi, ("type", "parametres"), chemin, ("definition",))
        p = loi.get("parametres")
        if "parametres" in loi and not isinstance(p, dict):
            c.rapporte("P1_TYPE_INVALIDE", chemin + ".parametres")
        definition = loi.get("definition")
        if definition is None and isinstance(p, dict):
            definition = p.get("definition")
        if not est_texte(definition):
            c.rapporte("P1_DEFINITION_MANQUANTE", chemin)
        lois_autres.append(chemin)
        return
    if not isinstance(typ, str) or typ not in LOIS:
        c.rapporte("P1_LOI_HORS_GRAMMAIRE", chemin)
        return
    verifier_cles(c, loi, ("type", "parametres"), chemin)
    p = loi.get("parametres")
    if "parametres" not in loi:
        return
    if not isinstance(p, dict):
        c.rapporte("P1_TYPE_INVALIDE", chemin + ".parametres")
        return
    attendus = dict(LOIS[typ])
    rho_dans_parametres = typ == "couple" and p.get("dependance") == "gaussienne"
    if rho_dans_parametres:
        attendus["rho"] = "nombre"
    verifier_cles(c, p, tuple(attendus), chemin + ".parametres")
    for nom, sorte in attendus.items():
        if nom in p:
            verifier_sorte(c, p[nom], sorte, chemin + ".parametres." + nom, profondeur, lois_autres)
    if typ == "melange":
        poids, comp = p.get("poids"), p.get("composantes")
        if isinstance(poids, list) and isinstance(comp, list):
            if len(poids) != len(comp):
                c.rapporte("P1_LOI_HORS_GRAMMAIRE", chemin + ".parametres")
            elif all(est_nombre(x) for x in poids) and abs(sum(float(x) for x in poids) - 1.0) > 1e-9:
                c.observe("O_POIDS_DU_MELANGE_NE_SOMMENT_PAS_A_UN", chemin + ".parametres.poids")


def verifier_regle(c, r, chemin):
    if not isinstance(r, dict) or not isinstance(r.get("type"), str) or r["type"] not in REGLES:
        c.rapporte("P1_REGLE_HORS_GRAMMAIRE", chemin)
        return
    attendus = REGLES[r["type"]]
    verifier_cles(c, r, ("type",) + tuple(attendus), chemin)
    for nom, sorte in attendus.items():
        if nom in r:
            verifier_sorte(c, r[nom], sorte, chemin + "." + nom, 0, [])


def verifier_temoin(c, t, chemin):
    if not isinstance(t, dict):
        c.rapporte("P1_TYPE_INVALIDE", chemin)
        return
    verifier_cles(c, t, CLES_TEMOIN, chemin, (CLE_VALEURS_DE_PLUS,))
    champ_texte(c, t, "id", chemin)
    champ_ferme(c, t, "sorte", SORTES, chemin)
    champ_texte(c, t, "monde", chemin)
    if "n" in t and not (t["n"] is None or est_entier_positif(t["n"])):
        c.rapporte("P1_TYPE_INVALIDE", chemin + ".n")
    if "regle" in t:
        verifier_regle(c, t["regle"], chemin + ".regle")
    champ_ferme(c, t, "population_de_calibration", POPULATIONS, chemin)
    champ_ferme(c, t, "portee_de_la_garantie", PORTEES, chemin)
    if "signal" in t and "monde" in t:
        if t["monde"] == "M":
            if not (isinstance(t["signal"], str) and t["signal"] in SIGNAUX_M):
                c.rapporte("P1_SIGNAL_INCOHERENT", chemin + ".signal")
        elif t["signal"] is not None:
            c.rapporte("P1_SIGNAL_INCOHERENT", chemin + ".signal")
    champ_ferme(c, t, "garantie", GARANTIES, chemin)
    champ_nombre(c, t, "risque_ou_niveau", chemin, nul_admis=True)
    liste_de_suppositions(c, t, "suppositions_declarees", chemin)
    champ_ferme(c, t, "grandeur", GRANDEURS, chemin)
    champ_nombre(c, t, "valeur_vraie", chemin)
    champ_texte(c, t, "formule", chemin)
    champ_ferme(c, t, "issue_attendue", ISSUES, chemin)
    champ_texte(c, t, "theoreme_ou_raison", chemin)
    if CLE_VALEURS_DE_PLUS in t:
        tid = t.get("id")
        if tid in TEMOINS_IMPOSES and tid not in IMPOSES_AVEC_VALEURS_DE_PLUS:
            c.rapporte("P1_VALEURS_DE_PLUS_NON_PERMISES", chemin + "." + CLE_VALEURS_DE_PLUS)
        vp = t[CLE_VALEURS_DE_PLUS]
        if not (isinstance(vp, dict) and all(est_nombre(x) for x in vp.values())):
            c.rapporte("P1_VALEURS_DE_PLUS_NON_NUMERIQUES", chemin + "." + CLE_VALEURS_DE_PLUS)
    if nombre_de_mots(t.get("theoreme_ou_raison")) > MOTS_MAX:
        c.observe("O_PLUS_DE_TRENTE_MOTS", chemin + ".theoreme_ou_raison")
    observer_probabilite(c, t, "valeur_vraie", chemin)
    observer_probabilite(c, t, "risque_ou_niveau", chemin)


def verifier_verite(c, v, chemin):
    """`verite` : objet {mode, expression}. v2 (C2) : un `mode` autre que la chaîne
    « exacte » (nul, vide, absent, autre texte, autre type), ou une vérité nulle,
    n'est pas une faute de forme : la famille est écartée (point 2 ; D-M18).
    `expression` n'est exigée que d'une vérité exacte. Une `verite` qui n'est ni un
    objet ni nulle, ou une clé en trop, reste une faute de forme."""
    if v is None:
        return
    if not isinstance(v, dict):
        c.rapporte("P1_TYPE_INVALIDE", chemin)
        return
    if v.get("mode") == MODE_EXACT:
        verifier_cles(c, v, CLES_VERITE, chemin)
        champ_texte(c, v, "expression", chemin)
    else:
        verifier_cles(c, v, (), chemin, CLES_VERITE)


def verifier_famille(c, f, chemin, a_l_ecart, lois_autres):
    if not isinstance(f, dict):
        c.rapporte("P1_TYPE_INVALIDE", chemin)
        return
    verifier_cles(c, f, CLES_FAMILLE, chemin, CLES_FAMILLE_A_L_ECART_EN_PLUS if a_l_ecart else ())
    fid = f.get("id")
    if "id" in f and not (isinstance(fid, str) and re.fullmatch(r"[A-Za-z]", fid)):
        c.rapporte("P1_IDENTIFIANT_DE_FAMILLE", chemin + ".id")
    champ_texte(c, f, "nom", chemin)
    champ_booleen(c, f, "imposee", chemin)
    champ_booleen(c, f, "hors_table", chemin)
    liste_de_suppositions(c, f, "suppositions_cassees", chemin)
    if "p_echec" in f:
        if fid in FAMILLES_A_P_ECHEC and not a_l_ecart:
            champ_nombre(c, f, "p_echec", chemin, nul_admis=True)
            observer_probabilite(c, f, "p_echec", chemin)
        elif f["p_echec"] is not None:
            c.rapporte("P1_P_ECHEC_HORS_C_ET_I", chemin + ".p_echec")
    if "tranches" in f:
        tr = f["tranches"]
        if not isinstance(tr, list) or len(tr) != 3:
            c.rapporte("P1_TRANCHES_PAS_TROIS", chemin + ".tranches")
        if isinstance(tr, list):
            for i, t in enumerate(tr):
                ici = "%s.tranches[%d]" % (chemin, i)
                if not isinstance(t, dict):
                    c.rapporte("P1_TYPE_INVALIDE", ici)
                    continue
                verifier_cles(c, t, CLES_TRANCHE, ici)
                if "id" in t and not (est_texte(t["id"]) or est_entier(t["id"])):
                    c.rapporte("P1_TYPE_INVALIDE", ici + ".id")
                if "n_calibration" in t:
                    nc = t["n_calibration"]
                    if not (isinstance(nc, list) and nc and all(est_entier_positif(x) for x in nc)):
                        c.rapporte("P1_TYPE_INVALIDE", ici + ".n_calibration")
                if "loi_honnete" in t:
                    verifier_loi(c, t["loi_honnete"], ici + ".loi_honnete", 0, lois_autres)
    if "saboteur" in f:
        s = f["saboteur"]
        ici = chemin + ".saboteur"
        if not isinstance(s, dict):
            c.rapporte("P1_TYPE_INVALIDE", ici)
        else:
            verifier_cles(c, s, CLES_SABOTEUR, ici)
            if "forme" in s:
                verifier_loi(c, s["forme"], ici + ".forme", 0, lois_autres)
            if "decalages" in s:
                d = s["decalages"]
                if not isinstance(d, list) or len(d) != 3:
                    c.rapporte("P1_DECALAGES_PAS_TROIS", ici + ".decalages")
                elif not all(est_nombre(x) for x in d):
                    c.rapporte("P1_TYPE_INVALIDE", ici + ".decalages")
    if "jumeau_sain" in f and not (f["jumeau_sain"] is None or isinstance(f["jumeau_sain"], dict)):
        c.rapporte("P1_TYPE_INVALIDE", chemin + ".jumeau_sain")
    if "verite" in f:
        verifier_verite(c, f["verite"], chemin + ".verite")
    champ_texte(c, f, "raison", chemin)
    if nombre_de_mots(f.get("raison")) > MOTS_MAX:
        c.observe("O_PLUS_DE_TRENTE_MOTS", chemin + ".raison")
    if a_l_ecart:
        if "tenue_a_l_ecart" in f and f["tenue_a_l_ecart"] is not True:
            c.rapporte("P1_CHAMP_FERME_INVALIDE", chemin + ".tenue_a_l_ecart")
        if "temoins" in f:
            if not isinstance(f["temoins"], list):
                c.rapporte("P1_TYPE_INVALIDE", chemin + ".temoins")
            else:
                for i, t in enumerate(f["temoins"]):
                    verifier_temoin(c, t, "%s.temoins[%d]" % (chemin, i))


RE_BUDGET_EN_TEXTE = re.compile(r"\s*(\d+(?:[.,]\d+)?)\s*%\s*")


def forme_du_budget(b):
    """v2 (C3) : budget b parmi 1 %, 5 %, 10 %, 20 %, 30 %, écrit en fraction (0.05),
    en nombre de pour cent (5) ou en chaîne (« 5 % », « 5% », espace insécable admise).
    Rend « fraction », « pour_cent », « chaine », ou None hors des cinq valeurs."""
    if est_nombre(b):
        if any(abs(float(b) - x) <= 1e-12 for x in BUDGETS_ADMIS):
            return "fraction"
        if any(abs(float(b) - 100 * x) <= 1e-9 for x in BUDGETS_ADMIS):
            return "pour_cent"
        return None
    if isinstance(b, str):
        m = RE_BUDGET_EN_TEXTE.fullmatch(b)
        if m and any(abs(float(m.group(1).replace(",", ".")) - 100 * x) <= 1e-9 for x in BUDGETS_ADMIS):
            return "chaine"
    return None


def est_objet_temoins_a_part(o):
    return isinstance(o, dict) and set(o) == {"temoins"}


def juger_forme(c, doc, lois_autres):
    cles = list(doc.keys())
    if cles != list(CLES_PREMIER_NIVEAU):
        en_trop = [k for k in cles if k not in CLES_PREMIER_NIVEAU]
        manquantes = [k for k in CLES_PREMIER_NIVEAU if k not in doc]
        for k in en_trop:
            c.rapporte("P1_CLE_EN_TROP", nom_sur(k))
        for k in manquantes:
            c.rapporte("P1_CLE_MANQUANTE", k)
        if not en_trop and not manquantes:
            c.rapporte("P1_ORDRE_DES_CLES", "premier_niveau")
    if "version_forme" in doc and doc["version_forme"] != VERSION_FORME:
        c.rapporte("P1_VERSION_FORME", "version_forme")
    for bloc in ("temoins", "familles", "a_l_ecart", "table", "valeurs_a_geler", "non_calcule", "remarques"):
        if bloc in doc and not isinstance(doc[bloc], list):
            c.rapporte("P1_TYPE_INVALIDE", bloc)
    for bloc in ("monde_S", "monde_M", "interface"):
        if bloc in doc and not isinstance(doc[bloc], dict):
            c.rapporte("P1_TYPE_INVALIDE", bloc)
    if isinstance(doc.get("temoins"), list):
        for i, t in enumerate(doc["temoins"]):
            verifier_temoin(c, t, "temoins[%d]" % i)
    if isinstance(doc.get("familles"), list):
        for i, f in enumerate(doc["familles"]):
            verifier_famille(c, f, "familles[%d]" % i, False, lois_autres)
    s = doc.get("monde_S")
    if isinstance(s, dict):
        verifier_cles(c, s, CLES_MONDE_S, "monde_S")
        for cle in ("taux_honnete", "taux_saboteur", "taux_honnete_derive"):
            champ_nombre(c, s, cle, "monde_S")
            observer_probabilite(c, s, cle, "monde_S")
        if "horizon" in s and not est_entier_positif(s["horizon"]):
            c.rapporte("P1_TYPE_INVALIDE", "monde_S.horizon")
        liste_de_suppositions(c, s, "suppositions_cassees_par_la_variante", "monde_S")
        if "verite" in s:
            verifier_verite(c, s["verite"], "monde_S.verite")
    m = doc.get("monde_M")
    if isinstance(m, dict):
        verifier_cles(c, m, CLES_MONDE_M, "monde_M")
        if "populations" in m:
            pop = m["populations"]
            if not isinstance(pop, list) or len(pop) != 3:
                c.rapporte("P1_POPULATIONS_PAS_TROIS", "monde_M.populations")
            elif not all(est_texte(x) for x in pop):
                c.rapporte("P1_TYPE_INVALIDE", "monde_M.populations")
        for cle in ("signal_valeur", "signal_intention"):
            if cle in m and not isinstance(m[cle], dict):
                c.rapporte("P1_TYPE_INVALIDE", "monde_M." + cle)
        for cle in ("gamma_propose", "aire_gamma_propose", "p_echec", "taux_parmi_ceux_qui_echouent"):
            champ_nombre(c, m, cle, "monde_M")
        for cle in ("aire_gamma_propose", "p_echec", "taux_parmi_ceux_qui_echouent"):
            observer_probabilite(c, m, cle, "monde_M")
        if "signal_moyen_propose" in m and not (est_nombre(m["signal_moyen_propose"]) or est_texte(m["signal_moyen_propose"])):
            c.rapporte("P1_TYPE_INVALIDE", "monde_M.signal_moyen_propose")
        if "budget_b_propose" in m:
            forme = forme_du_budget(m["budget_b_propose"])
            if forme is None:
                c.rapporte("P1_BUDGET_HORS_LISTE", "monde_M.budget_b_propose")
            elif forme != "fraction":
                c.observe("O_BUDGET_HORS_FORME_FRACTION", "monde_M.budget_b_propose")
        champ_texte(c, m, "verite_gamma_nul", "monde_M")
        champ_texte(c, m, "limite_monde_M", "monde_M")
        if isinstance(m.get("limite_monde_M"), str) and "\n" in m["limite_monde_M"].strip():
            c.observe("O_LIMITE_MONDE_M_SUR_PLUSIEURS_LIGNES", "monde_M.limite_monde_M")
    if isinstance(doc.get("a_l_ecart"), list):
        objets_temoins = 0
        for i, o in enumerate(doc["a_l_ecart"]):
            ici = "a_l_ecart[%d]" % i
            if est_objet_temoins_a_part(o):
                objets_temoins += 1
                if objets_temoins > 1:
                    c.rapporte("P1_A_L_ECART_OBJET_TEMOINS_EN_DOUBLE", ici)
                if not isinstance(o["temoins"], list):
                    c.rapporte("P1_TYPE_INVALIDE", ici + ".temoins")
                else:
                    for j, t in enumerate(o["temoins"]):
                        verifier_temoin(c, t, "%s.temoins[%d]" % (ici, j))
            else:
                verifier_famille(c, o, ici, True, lois_autres)
    if isinstance(doc.get("table"), list):
        for i, r in enumerate(doc["table"]):
            ici = "table[%d]" % i
            if not isinstance(r, dict):
                c.rapporte("P1_TYPE_INVALIDE", ici)
                continue
            verifier_cles(c, r, CLES_TABLE, ici)
            champ_texte(c, r, "monde", ici)
            if "supposition_cassee" in r:
                s_c = r["supposition_cassee"]
                if not (isinstance(s_c, str) and (s_c in SUPPOSITIONS or s_c == AUCUNE)):
                    c.rapporte("P1_SUPPOSITION_HORS_LISTE", ici + ".supposition_cassee")
    itf = doc.get("interface")
    if isinstance(itf, dict):
        verifier_cles(c, itf, CLES_INTERFACE, "interface")
        for cle in ("entree", "sortie", "sens_du_score"):
            champ_texte(c, itf, cle, "interface")
        if "nombre_de_tranches" in itf and not est_entier_positif(itf["nombre_de_tranches"]):
            c.rapporte("P1_TYPE_INVALIDE", "interface.nombre_de_tranches")
        if "tailles_de_calibration" in itf:
            tc = itf["tailles_de_calibration"]
            if not (isinstance(tc, list) and tc and all(est_entier_positif(x) for x in tc)):
                c.rapporte("P1_TYPE_INVALIDE", "interface.tailles_de_calibration")
    if isinstance(doc.get("valeurs_a_geler"), list):
        for i, v in enumerate(doc["valeurs_a_geler"]):
            ici = "valeurs_a_geler[%d]" % i
            if not isinstance(v, dict):
                c.rapporte("P1_TYPE_INVALIDE", ici)
                continue
            verifier_cles(c, v, CLES_VALEUR_A_GELER, ici)
            champ_texte(c, v, "nom", ici)
            champ_texte(c, v, "raison", ici)
            if "valeur_proposee" in v and not (est_nombre(v["valeur_proposee"]) or est_texte(v["valeur_proposee"])):
                c.rapporte("P1_TYPE_INVALIDE", ici + ".valeur_proposee")
    if isinstance(doc.get("non_calcule"), list):
        for i, v in enumerate(doc["non_calcule"]):
            if not (est_texte(v) or isinstance(v, dict)):
                c.rapporte("P1_TYPE_INVALIDE", "non_calcule[%d]" % i)
    # v3 (D1, mot de la mère) : plus de TEMOINS_MAX témoins, ceux de tête et ceux du bloc
    # `a_l_ecart` comptés ensemble, est une faute de forme : la sortie est illisible.
    nombre_de_temoins = len(doc["temoins"]) if isinstance(doc.get("temoins"), list) else 0
    if isinstance(doc.get("a_l_ecart"), list):
        for o in doc["a_l_ecart"]:
            if isinstance(o, dict) and isinstance(o.get("temoins"), list):
                nombre_de_temoins += len(o["temoins"])
    if nombre_de_temoins > TEMOINS_MAX:
        c.rapporte("P1_TEMOINS_AU_DELA_DU_PLAFOND", "temoins")
    if isinstance(doc.get("remarques"), list):
        for i, v in enumerate(doc["remarques"]):
            if not est_texte(v):
                c.rapporte("P1_TYPE_INVALIDE", "remarques[%d]" % i)
        if len(doc["remarques"]) > REMARQUES_MAX:
            c.observe("O_PLUS_DE_DIX_REMARQUES", "remarques")


# ---------------------------------------------------------------------------
# Contexte commun aux points 2 et 3 (lu seulement si le point 1 est tenu)
# ---------------------------------------------------------------------------

class Contexte:
    def __init__(self, doc):
        self.doc = doc
        self.temoins = [(t, "temoins[%d]" % i) for i, t in enumerate(doc["temoins"])]
        self.familles = [(f, "familles[%d]" % i) for i, f in enumerate(doc["familles"])]
        self.ecart = []          # (famille, chemin, étiquette)
        self.temoins_ecart = []  # (témoin, chemin)
        self.forme_a_l_ecart = None
        formes = set()
        for i, o in enumerate(doc["a_l_ecart"]):
            ici = "a_l_ecart[%d]" % i
            if est_objet_temoins_a_part(o):
                formes.add("objet_temoins_a_part")
                self.temoins_ecart += [(t, "%s.temoins[%d]" % (ici, j)) for j, t in enumerate(o["temoins"])]
            else:
                self.ecart.append((o, ici, ici))
                if "temoins" in o:
                    formes.add("temoins_dans_chaque_famille")
                    self.temoins_ecart += [(t, "%s.temoins[%d]" % (ici, j)) for j, t in enumerate(o["temoins"])]
        if len(formes) == 1:
            self.forme_a_l_ecart = formes.pop()
        elif len(formes) == 2:
            self.forme_a_l_ecart = "mixte"
        self.ids_visibles = [f["id"] for f, _ in self.familles]
        self.ids_ecart = [f["id"] for f, _, _ in self.ecart]


def etiquette_sure(fid):
    return fid if isinstance(fid, str) and re.fullmatch(r"[A-Za-z]", fid) else "*"


# ---------------------------------------------------------------------------
# Point 2 — complétude, et familles ou mondes écartés
# ---------------------------------------------------------------------------

N_DE_T09 = TABLE_DES_TEMOINS_IMPOSES["T09"]["n"]           # 299, § 3.1
TAUX_DE_DEPART_DE_LA_DERIVE = "0.01"                        # v4 : le taux que le décalage triple
TAUX_VISE_PAR_LA_DERIVE = "0.03"                            # le décalage triple un taux de 1 %
TOLERANCE_DU_CONTROLE_DE_DERIVE = "0.001"                   # mot de la mère : 10⁻³ absolue, comme au § 6, point 4
MOTS_EXCLUS_DU_DECALAGE = ("couverture", "taux", "probabilite")
MOTS_DU_DECALAGE = ("decalage", "derive")


def lire_decalage_de_t09(vdp):
    """v3 (D2, règle de la mère) : on écarte les clés de `valeurs_de_plus` dont le nom contient
    « couverture », « taux » ou « probabilite » ; on garde la seule clé restante, ou à défaut,
    parmi les restantes, l'unique clé dont le nom contient « decalage » ou « derive ». Rend
    (rang de la clé, compté de 1 dans l'ordre de l'objet ; valeur) ou None."""
    if not isinstance(vdp, dict):
        return None
    cles = list(vdp)
    restantes = [k for k in cles if not any(m in normaliser(k) for m in MOTS_EXCLUS_DU_DECALAGE)]
    if len(restantes) == 1:
        choisie = restantes[0]
    else:
        # Étape (c), précision de la mère : l'unique clé « decalage » ou « derive » se cherche
        # parmi les clés laissées par l'étape (a), jamais parmi toutes les clés. Les noms se
        # comparent sur leur forme normalisée (sans casse ni accents), par sous-chaîne.
        nommees = [k for k in restantes if any(m in normaliser(k) for m in MOTS_DU_DECALAGE)]
        if len(nommees) != 1:
            return None
        choisie = nommees[0]
    if not est_nombre(vdp[choisie]):
        return None
    return cles.index(choisie) + 1, vdp[choisie]


def juger_completude(c, ctx):
    tous_les_temoins = ctx.temoins + ctx.temoins_ecart
    vus = set()
    for t, ici in tous_les_temoins:
        if t["id"] in vus:
            c.rapporte("P2_IDENTIFIANT_DE_TEMOIN_EN_DOUBLE", ici)
        vus.add(t["id"])
    # v2 (remarque 14 du vérificateur de la vérité ; D-M16 se lit par identifiant) : T01 à T17
    # sont réservés aux témoins imposés, une fois chacun, en tête. Un témoin libre qui porte l'un
    # de ces identifiants (second porteur en tête, ou témoin du bloc à l'écart) est une faute.
    imposes_vus = set()
    for t, ici in ctx.temoins:
        if t["id"] in TEMOINS_IMPOSES:
            if t["id"] in imposes_vus:
                c.rapporte("P2_IDENTIFIANT_IMPOSE_RESERVE", ici + ".id")
            imposes_vus.add(t["id"])
    for t, ici in ctx.temoins_ecart:
        if t["id"] in TEMOINS_IMPOSES:
            c.rapporte("P2_IDENTIFIANT_IMPOSE_RESERVE", ici + ".id")
    ids_en_tete = [t["id"] for t, _ in ctx.temoins]
    for tid in TEMOINS_IMPOSES:
        if tid not in ids_en_tete:
            c.rapporte("P2_TEMOIN_IMPOSE_ABSENT", "temoins", temoin=tid)
    tous_ids = ctx.ids_visibles + ctx.ids_ecart
    vus = set()
    for (f, ici) in ctx.familles + [(f, ici) for f, ici, _ in ctx.ecart]:
        if f["id"] in vus:
            c.rapporte("P2_IDENTIFIANT_DE_FAMILLE_EN_DOUBLE", ici + ".id")
        vus.add(f["id"])
        if f["id"] in IDENTIFIANTS_DE_MONDE:
            c.rapporte("P2_IDENTIFIANT_DE_FAMILLE_RESERVE", ici + ".id")
    for lettre in FAMILLES_IMPOSEES:
        if lettre not in ctx.ids_visibles:
            c.rapporte("P2_FAMILLE_IMPOSEE_ABSENTE", "familles", famille=lettre)
        if lettre in ctx.ids_ecart:
            c.rapporte("P2_FAMILLE_IMPOSEE_A_L_ECART", "a_l_ecart", famille=lettre)
    for f, ici in ctx.familles:
        if f["id"] in FAMILLES_A_P_ECHEC and f["p_echec"] is None:
            c.rapporte("P2_P_ECHEC_ABSENT", ici + ".p_echec")
    if len(ctx.ecart) not in (1, 2):
        c.rapporte("P2_NOMBRE_DE_FAMILLES_A_L_ECART", "a_l_ecart")
    if not any(t["sorte"] == "de_marge" for t, _ in tous_les_temoins):
        c.rapporte("P2_AUCUN_TEMOIN_DE_MARGE", "temoins")
    mondes_en_tete = set(ctx.ids_visibles) | set(IDENTIFIANTS_DE_MONDE) | set(ctx.ids_ecart)
    for t, ici in ctx.temoins:
        if t["monde"] not in mondes_en_tete:
            c.rapporte("P2_TEMOIN_RATTACHE_A_UN_MONDE_ABSENT", ici + ".monde")
    for t, ici in ctx.temoins_ecart:
        if t["monde"] not in ctx.ids_ecart:
            c.rapporte("P2_TEMOIN_RATTACHE_A_UN_MONDE_ABSENT", ici + ".monde")

    # Écarts (§ 3.2, « Vérité exacte » ; § 6, point 2) : ne rendent pas la sortie illisible.
    def sortes_de(monde, liste):
        return {t["sorte"] for t, _ in liste if t["monde"] == monde}

    def juger_un_monde(etiquette, verite, sortes):
        if not (isinstance(verite, dict) and verite.get("mode") == MODE_EXACT):
            c.ecarte("E_VERITE_NON_EXACTE", etiquette)
        if "doit_mourir" not in sortes:
            c.ecarte("E_SANS_TEMOIN_DOIT_MOURIR", etiquette)
        if "doit_tenir" not in sortes:
            c.ecarte("E_SANS_TEMOIN_DOIT_TENIR", etiquette)

    for f, ici in ctx.familles:
        juger_un_monde(etiquette_sure(f["id"]), f["verite"], sortes_de(f["id"], ctx.temoins))
    for f, ici, etiquette in ctx.ecart:
        juger_un_monde(etiquette, f["verite"], sortes_de(f["id"], ctx.temoins_ecart))
    sortes_m = sortes_de("M", ctx.temoins)
    if "doit_mourir" not in sortes_m:
        c.ecarte("E_SANS_TEMOIN_DOIT_MOURIR", "M")
    if "doit_tenir" not in sortes_m:
        c.ecarte("E_SANS_TEMOIN_DOIT_TENIR", "M")
    verite_s = ctx.doc["monde_S"]["verite"]
    if not (isinstance(verite_s, dict) and verite_s.get("mode") == MODE_EXACT):
        c.ecarte("E_VERITE_NON_EXACTE", "S")
    # v3 (D2, règle de la mère, 11:00Z) : la dérive de F n'a pas de champ dans la forme fixe ;
    # son décalage se lit dans `valeurs_de_plus` de T09. S'il ne s'y lit pas, F est écartée,
    # la sortie reste lisible.
    if any(f["id"] == "F" for f, _ in ctx.familles):
        t09 = next((t for t, _ in ctx.temoins if t["id"] == "T09"), None)
        if t09 is None or lire_decalage_de_t09(t09.get(CLE_VALEURS_DE_PLUS)) is None:
            c.ecarte("E_DERIVE_SANS_DECALAGE_LISIBLE", "F")

    # Observations (ne décident de rien ; à lire par la mère).
    for t, ici in ctx.temoins:
        tid = t["id"]
        if tid in TABLE_DES_TEMOINS_IMPOSES:
            attendu = dict(DEFAUTS_DES_IMPOSES)
            attendu.update(TABLE_DES_TEMOINS_IMPOSES[tid])
            for champ, valeur in sorted(attendu.items()):
                if not egal(t[champ], valeur):
                    c.observe("O_ECART_A_LA_TABLE_DES_TEMOINS_IMPOSES", ici + "." + champ, temoin=tid)
            if tid in IMPOSES_AVEC_VALEURS_DE_PLUS and CLE_VALEURS_DE_PLUS not in t:
                c.observe("O_VALEURS_DE_PLUS_ABSENTES", ici, temoin=tid)
    for t, ici in tous_les_temoins:
        s, issue = t["sorte"], t["issue_attendue"]
        if (s == "doit_tenir" and issue != "tient") or (s == "doit_mourir" and issue == "tient"):
            c.observe("O_SORTE_ET_ISSUE_DISCORDANTES", ici)
        if issue == "morte_sans_gain" and t["id"] not in IMPOSES_SANS_GAIN_PERMIS:
            c.observe("O_MORTE_SANS_GAIN_HORS_T05_T07", ici)
    libres_visibles = [i for i in ctx.ids_visibles if i not in FAMILLES_IMPOSEES]
    if len(libres_visibles) + len(ctx.ecart) > FAMILLES_LIBRES_MAX:
        c.observe("O_FAMILLES_LIBRES_AU_DELA_DE_DEUX", "familles")
    if not any(t["monde"] == "M" and t["portee_de_la_garantie"] == PORTEE_CONDITIONNELLE for t, _ in ctx.temoins):
        c.observe("O_MONDE_M_SANS_TEMOIN_CONDITIONNEL", "temoins")
    p = {f["id"]: f["p_echec"] for f, _ in ctx.familles if f["id"] in FAMILLES_A_P_ECHEC}
    if all(est_nombre(p.get(x)) for x in FAMILLES_A_P_ECHEC):
        if not egal(p["C"], p["I"]):
            c.observe("O_P_ECHEC_DIFFERENT_ENTRE_C_ET_I", "familles")
        for x in FAMILLES_A_P_ECHEC:
            if not (P_ECHEC_BORNES[0] <= float(p[x]) <= P_ECHEC_BORNES[1]):
                c.observe("O_P_ECHEC_HORS_DE_L_INTERVALLE", "familles", famille=x)
    for f, ici in ctx.familles:
        if f["imposee"] is not (f["id"] in FAMILLES_IMPOSEES):
            c.observe("O_IMPOSEE_INCOHERENTE", ici + ".imposee")
        if not f["suppositions_cassees"] and isinstance(f["jumeau_sain"], dict) and not f["hors_table"]:
            c.observe("O_JUMEAU_SAIN_SUR_FAMILLE_SAINE", ici + ".jumeau_sain")
    for i, v in enumerate(ctx.doc["non_calcule"]):
        textes = [v] if isinstance(v, str) else [x for x in v.values() if isinstance(x, str)]
        for texte in textes:
            for m in RE_DESIGNATION.finditer(texte):
                for lettre in re.findall(r"[A-Za-z]", m.group(1)):
                    if lettre in ctx.ids_visibles or lettre == "M":
                        c.observe("O_MENTION_POSSIBLE_DANS_NON_CALCULE", "non_calcule[%d]" % i, famille=lettre)


# ---------------------------------------------------------------------------
# Point 3 — cohérence
# ---------------------------------------------------------------------------

def nomme(texte, ident, nom_norm):
    if texte.strip() == ident:
        return True
    for m in RE_DESIGNATION.finditer(texte):
        if ident in re.findall(r"[A-Za-z]", m.group(1)):
            return True
    return bool(nom_norm) and len(nom_norm) >= NOM_MIN_CARACTERES and nom_norm in normaliser(texte)


def parcourir(valeur, chemin, visite):
    """Visite chaque chaîne et chaque clé ; `visite(texte, chemin)`.
    v2 (C1) : parcours itératif, dans le même ordre que la v1 (préordre), sans
    limite de profondeur due à la récursion."""
    pile = [("valeur", valeur, chemin)]
    while pile:
        sorte, x, ici = pile.pop()
        if sorte == "cle":
            visite(x, ici)
        elif isinstance(x, dict):
            enfants = []
            for k, v in x.items():
                sous = ici + "." + nom_sur(k) if ici else nom_sur(k)
                enfants.append(("cle", k, sous))
                enfants.append(("valeur", v, sous))
            pile.extend(reversed(enfants))
        elif isinstance(x, list):
            pile.extend(reversed([("valeur", v, "%s[%d]" % (ici, i)) for i, v in enumerate(x)]))
        elif isinstance(x, str):
            visite(x, ici)


def juger_coherence(c, ctx):
    doc = ctx.doc
    # 3a. La table redit les champs `suppositions_cassees`.
    attendu = {}
    chemins = {}
    for f, ici in ctx.familles:
        attendu.setdefault(f["id"], set(f["suppositions_cassees"]) or {AUCUNE})
        chemins.setdefault(f["id"], ici)
    for f, ici, _ in ctx.ecart:
        attendu.setdefault(f["id"], set(f["suppositions_cassees"]) or {AUCUNE})
        chemins.setdefault(f["id"], ici)
    attendu["\x00S"] = set(doc["monde_S"]["suppositions_cassees_par_la_variante"]) or {AUCUNE}
    chemins["\x00S"] = "monde_S.suppositions_cassees_par_la_variante"
    lu = {}
    vues = set()
    lignes_ecart = []
    for i, r in enumerate(doc["table"]):
        m, s = r["monde"], r["supposition_cassee"]
        if m in attendu and m != "\x00S":
            cle = m
            if m in ctx.ids_ecart:
                lignes_ecart.append(i)
        elif re.fullmatch(r"S(?:[^A-Za-z].*)?", m, flags=re.S):
            cle = "\x00S"
        else:
            c.rapporte("P3_TABLE_MONDE_INCONNU", "table[%d].monde" % i)
            continue
        if (cle, s) in vues:
            c.rapporte("P3_TABLE_LIGNE_EN_DOUBLE", "table[%d]" % i)
        vues.add((cle, s))
        lu.setdefault(cle, set()).add(s)
    for cle, ens in attendu.items():
        if lu.get(cle, set()) != ens:
            c.rapporte("P3_TABLE_NE_REDIT_PAS", chemins[cle])
    # 3b. Chaque famille cassée a son jumeau sain ; 3c. `hors_table` ne casse aucune des sept.
    for f, ici in ctx.familles + [(f, ici) for f, ici, _ in ctx.ecart]:
        if f["suppositions_cassees"] and not (isinstance(f["jumeau_sain"], dict) and f["jumeau_sain"]):
            c.rapporte("P3_JUMEAU_SAIN_ABSENT", ici + ".jumeau_sain")
        if f["hors_table"] and f["suppositions_cassees"]:
            c.rapporte("P3_HORS_TABLE_CASSE_UNE_DES_SEPT", ici + ".suppositions_cassees")
    # 3d. Le bloc `interface` ne porte ni loi, ni paramètre, ni nom de famille.
    noms = [(f["id"], normaliser(f["nom"])) for f, _ in ctx.familles] + \
           [(f["id"], normaliser(f["nom"])) for f, _, _ in ctx.ecart]

    def visite_interface(texte, ici):
        if not isinstance(texte, str):
            return
        t = normaliser(texte)
        if RE_MOTS_DE_LOI.search(t):
            c.rapporte("P3_INTERFACE_PORTE_UNE_LOI", ici)
        if RE_MOTS_DE_PARAMETRE.search(t):
            c.rapporte("P3_INTERFACE_PORTE_UN_PARAMETRE", ici)
        if any(nomme(texte, ident, nom) for ident, nom in noms):
            c.rapporte("P3_INTERFACE_NOMME_UNE_FAMILLE", ici)

    for cle, v in doc["interface"].items():
        if cle in CLES_INTERFACE:
            parcourir(v, "interface." + cle, visite_interface)
    # 3e. Rien hors du bloc `a_l_ecart` ne nomme une famille tenue à l'écart.
    #     Les lignes de `table` de ces familles, exigées par le § 4.2, sont exemptées
    #     et listées pour être détachées avec le bloc.
    cibles = [(f["id"], normaliser(f["nom"])) for f, _, _ in ctx.ecart]
    trouvees = []

    def visite_hors_bloc(texte, ici):
        if any(nomme(texte, ident, nom) for ident, nom in cibles):
            trouvees.append(ici)

    for cle, v in doc.items():
        if cle == "a_l_ecart":
            continue
        if cle == "table":
            for i, r in enumerate(v):
                if i not in lignes_ecart:
                    parcourir(r, "table[%d]" % i, visite_hors_bloc)
            continue
        parcourir(v, cle, visite_hors_bloc)
    for ici in trouvees:
        c.rapporte("P3_FAMILLE_A_L_ECART_NOMMEE_HORS_DE_SON_BLOC", ici)
    return lignes_ecart


# ---------------------------------------------------------------------------
# Point 5 — motifs
# ---------------------------------------------------------------------------

def longue_chaine_melangee(texte):
    for m in RE_LONGUE_CHAINE.finditer(texte):
        s = m.group(0)
        if re.search(r"[A-Z]", s) and re.search(r"[a-z]", s) and re.search(r"[0-9]", s):
            return True
    return False


def juger_motifs(c, doc, texte, motifs_noms):
    def visite(chaine, ici):
        if not isinstance(chaine, str):
            return
        for i, motif in enumerate(motifs_noms):
            if motif.search(chaine) or motif.search(normaliser(chaine)):
                c.rapporte("P5_NOM_DE_MODELE_OU_DE_FOURNISSEUR", ici, motif=i + 1)
        for nom, motif in MOTIFS_DE_CLE:
            if motif.search(chaine):
                c.rapporte("P5_CHAINE_DE_FORME_DE_CLE", ici, motif=nom)
        if longue_chaine_melangee(chaine):
            c.rapporte("P5_CHAINE_DE_FORME_DE_CLE", ici, motif="longue_chaine_melangee")

    if doc is not None:
        parcourir(doc, "", visite)
    else:
        visite(texte, "texte_brut")


# ---------------------------------------------------------------------------
# Ensemble
# ---------------------------------------------------------------------------

def verifier(octets, motifs_noms):
    c = Constat()
    lois_autres = []
    doc, texte, _ = lire_le_texte(c, octets)
    if doc is not None:
        juger_forme(c, doc, lois_autres)
    p1 = not c.fautes["1"]
    lignes_ecart = []
    ctx = None
    if p1:
        ctx = Contexte(doc)
        juger_completude(c, ctx)
        lignes_ecart = juger_coherence(c, ctx)
    juger_motifs(c, doc, texte, motifs_noms)

    def verdict(point, juge=True):
        if not juge:
            return {"verdict": "non_juge", "fautes": []}
        fautes = sorted(c.fautes[point], key=lambda e: json.dumps(e, sort_keys=True, ensure_ascii=False))
        return {"verdict": "manque" if fautes else "tenu", "fautes": fautes}

    points = {
        "1_forme": verdict("1"),
        "2_completude": verdict("2", p1),
        "3_coherence": verdict("3", p1),
        "5_motifs": verdict("5"),
    }
    illisible = points["1_forme"]["verdict"] == "manque" or points["2_completude"]["verdict"] == "manque"
    refus = points["3_coherence"]["verdict"] == "manque" or points["5_motifs"]["verdict"] == "manque"
    if illisible:
        code = SORTIE_ILLISIBLE
    elif refus:
        code = SORTIE_LISIBLE_AVEC_REFUS
    else:
        code = SORTIE_TOUT_TENU
    hors_table, a_lire = [], []
    comptes = {}
    if ctx is not None:
        for f, ici in ctx.familles:
            if f["hors_table"]:
                hors_table.append(etiquette_sure(f["id"]))
        for f, ici, etiquette in ctx.ecart:
            if f["hors_table"]:
                hors_table.append(etiquette)
        for chemin in lois_autres:
            m = re.match(r"(familles|a_l_ecart)\[(\d+)\]", chemin)
            if m and m.group(1) == "familles":
                a_lire.append(etiquette_sure(doc["familles"][int(m.group(2))]["id"]))
            elif m:
                a_lire.append("a_l_ecart[%s]" % m.group(2))
        comptes = {
            "temoins_en_tete": len(ctx.temoins),
            "temoins_a_l_ecart": len(ctx.temoins_ecart),
            "familles_visibles": len(ctx.familles),
            "familles_libres_visibles": len([i for i in ctx.ids_visibles if i not in FAMILLES_IMPOSEES]),
            "familles_a_l_ecart": len(ctx.ecart),
        }
    ecartes = [{"monde": m, "raisons": sorted(r)} for m, r in sorted(c.ecarts.items())]
    return {
        "verdict_d_ensemble": "illisible" if illisible else "lisible",
        "points": points,
        "ecartes": ecartes,
        "hors_table": sorted(set(hors_table)),
        "a_lire_par_une_personne_type_autre": sorted(set(a_lire)),
        "lignes_de_table_des_familles_a_l_ecart": lignes_ecart,
        "forme_du_bloc_a_l_ecart": ctx.forme_a_l_ecart if ctx else None,
        "observations": sorted(c.observations, key=lambda e: json.dumps(e, sort_keys=True, ensure_ascii=False)),
        "comptes": comptes,
        "code_de_sortie": code,
        "sortie_auteur": {"octets": len(octets), "caracteres": len(texte), "borne_caracteres": TAILLE_MAX_CARACTERES},
    }


# ---------------------------------------------------------------------------
# CORRESPONDANCE (v2, mot de la mère 09:15Z) : sortie lisible de l'auteur -> entrée du
# mode `--recalculer` du programme de vérité des témoins
# (calculer_verite_temoins_imposes_v1.py, 4857343c…). Format lu sur l'exemple
# exemple-entree-recalcul-v1.json (76ed336e…) et sur les gardes de ce programme.
# Chaque choix que la lettre ne fixe pas porte un code CH_… écrit dans le compte rendu ;
# chaque témoin qui ne se convertit pas porte un code NC_… et n'entre pas dans l'entrée.
# Aucune valeur n'est calculée ici : on recopie des lois et des règles.
# ---------------------------------------------------------------------------

VERSION_ENTREE_RECALCUL = "recalcul-temoins-seuil-et-moniteurs-v1"
AIRES_NOMMEES = ("aire_0_69", "aire_0_80", "aire_0_95")       # § 3.2 : trois tailles de signal
AIRE_DE_LA_PUISSANCE = "aire_0_80"                            # CH6
TAILLES_DES_GRAPPES_IMPOSEES = {"T10": [100] * 3, "T11": [10] * 30}  # § 3.1, définitions de T10 et T11
TAILLE_DE_PLUS_T07 = 400                                      # § 3.1, T07 joué à n = 200 et n = 400
LOI_NORMALE_REDUITE = {"type": "normale", "parametres": {"mu": 0, "sigma": 1}}  # CH8 (§ 3.2, H : variance 1)
RE_IDENTIFIANT_SUR = re.compile(r"[A-Za-z0-9_.\-]{1,32}")


class NonConvertible(Exception):
    def __init__(self, code):
        super().__init__(code)
        self.code = code


def fraction_de(x):
    from fractions import Fraction
    return Fraction(getattr(x, "texte", None) or str(x))



def entier_simple(x):
    return int(x) if est_entier(x) else x


def ecrire_brut(x):
    """JSON compact ; chaque nombre lu dans la sortie est réécrit avec son texte brut
    (le programme de vérité lit les décimaux en rationnels exacts)."""
    if x is None or isinstance(x, bool):
        return json.dumps(x)
    if isinstance(x, (NombreBrut, EntierBrut)):
        return x.texte
    if isinstance(x, int):
        return str(x)
    if isinstance(x, float):
        raise AssertionError("flottant sans texte brut")
    if isinstance(x, str):
        return json.dumps(x, ensure_ascii=False)
    if isinstance(x, dict):
        return "{" + ", ".join(json.dumps(k, ensure_ascii=False) + ": " + ecrire_brut(v) for k, v in x.items()) + "}"
    if isinstance(x, list):
        return "[" + ", ".join(ecrire_brut(v) for v in x) + "]"
    raise AssertionError("valeur non sérialisable")


def loi_pour_le_moteur(loi, n=None):
    typ = loi["type"]
    if typ == TYPE_AUTRE:
        raise NonConvertible("NC_LOI_AUTRE")
    p = dict(loi["parametres"])
    if typ == "melange":
        p["composantes"] = [loi_pour_le_moteur(x, n) for x in p["composantes"]]
    elif typ in ("arrondi", "decalage"):
        p["loi"] = loi_pour_le_moteur(p["loi"], n)
    elif typ == "somme_de_pas":
        p["loi_du_pas"] = loi_pour_le_moteur(p["loi_du_pas"], n)
        p["nombre_de_pas"] = entier_simple(p["nombre_de_pas"])
    elif typ == "couple":
        p["marges"] = [loi_pour_le_moteur(x, n) for x in p["marges"]]
    elif typ == "effet_de_famille_plus_bruit":
        tailles = p["tailles_de_famille"]
        if isinstance(tailles, list):
            p["tailles_de_famille"] = [entier_simple(m) for m in tailles]
        else:  # CH8c : un entier m se lit « n / m familles de m »
            m = int(tailles)
            if not (est_entier(n) and int(n) % m == 0):
                raise NonConvertible("NC_TAILLES_DE_FAMILLE")
            p["tailles_de_famille"] = [m] * (int(n) // m)
    return {"type": typ, "parametres": p}


def composantes_d_echec(loi_h, p_echec, choix):
    """CH2 : « l'honnête qui échoue » est la composante du mélange dont le poids égale
    P(échec) ; « l'honnête qui réussit », l'autre composante, s'il n'y en a qu'une."""
    if loi_h["type"] != "melange" or p_echec is None:
        raise NonConvertible("NC_PAS_DE_COMPOSANTE_D_ECHEC")
    choix.add("CH2_ECHEC_PAR_POIDS_EGAL_A_P_ECHEC")
    poids = [fraction_de(w) for w in loi_h["parametres"]["poids"]]
    comps = loi_h["parametres"]["composantes"]
    rangs = [i for i, w in enumerate(poids) if w == fraction_de(p_echec)]
    if len(rangs) != 1:
        raise NonConvertible("NC_COMPOSANTES_AMBIGUES")
    autres = [c_ for i, c_ in enumerate(comps) if i != rangs[0]]
    return comps[rangs[0]], (autres[0] if len(autres) == 1 else None)


def choisir_population(population, loi_tous, echec_reussite):
    if population == "tous_les_honnetes":
        return loi_tous
    echec, reussite = echec_reussite()
    loi = echec if population == "honnetes_qui_echouent" else reussite
    if loi is None:
        raise NonConvertible("NC_COMPOSANTES_AMBIGUES")
    return loi


def a_besoin_de_saboteurs(t):
    return t["id"] in IMPOSES_SANS_GAIN_PERMIS or t["grandeur"] == "puissance"


def garder_saboteurs(t, saboteurs, choix):
    if t["grandeur"] == "puissance" and t["id"] not in IMPOSES_SANS_GAIN_PERMIS:
        choix.add("CH6_PUISSANCE_A_L_AIRE_0_80")
        return {AIRE_DE_LA_PUISSANCE: saboteurs[AIRE_DE_LA_PUISSANCE]}
    return saboteurs


def lois_de_famille(f, t, choix, derive_de_f):
    n = t["n"]
    tranches = f["tranches"]
    choix.add("CH1_TRANCHE_PAR_TAILLE")
    i_lecture = next((i for i, tr in enumerate(tranches)
                      if est_entier(n) and any(int(x) == int(n) for x in tr["n_calibration"])), 0)
    loi_h = tranches[i_lecture]["loi_honnete"]
    grappes = loi_h["type"] == "effet_de_famille_plus_bruit"
    if grappes and t["id"] in TAILLES_DES_GRAPPES_IMPOSEES:
        choix.add("CH8B_TAILLES_DU_MANDAT_POUR_T10_T11")
        loi_h = {"type": loi_h["type"], "parametres": dict(loi_h["parametres"],
                                                           tailles_de_famille=TAILLES_DES_GRAPPES_IMPOSEES[t["id"]])}

    def echec_reussite():
        return composantes_d_echec(loi_h, f["p_echec"], choix)

    calibration = choisir_population(t["population_de_calibration"], loi_h, echec_reussite)
    lecture = loi_h if t["portee_de_la_garantie"] == PORTEE_TOUS else choisir_population("honnetes_qui_echouent", loi_h, echec_reussite)
    lois = {"calibration": loi_pour_le_moteur(calibration, n)}
    if grappes:
        choix.add("CH8_GRAPPES_LUES_SUR_LA_NORMALE_REDUITE")
        lois["lecture"] = copy_simple(LOI_NORMALE_REDUITE)
    else:
        lois["lecture"] = loi_pour_le_moteur(lecture, n)
    if SUPPOSITIONS[2] in f["suppositions_cassees"]:
        if derive_de_f is None or f is not derive_de_f[0]:
            raise NonConvertible("NC_DERIVE_SANS_CHAMP")
        choix.add("CH7_DERIVE_DE_F_LUE_DANS_T09")
        lois["lecture"] = {"type": "decalage", "parametres": {"loi": lois["lecture"], "delta_en_ecarts_types": derive_de_f[1]}}
    if t["regle"]["type"] == "plus_grand_de_la_tranche_voisine":
        # v3 (mot de la mère) : la tranche suivante ; pour la dernière, la précédente ; sans boucle.
        choix.add("CH1B_TRANCHE_VOISINE_SUIVANTE_OU_PRECEDENTE")
        voisine = tranches[i_lecture + 1 if i_lecture + 1 < len(tranches) else i_lecture - 1]
        lois["voisine"] = {"n": entier_simple(voisine["n_calibration"][0]),
                           "loi": loi_pour_le_moteur(voisine["loi_honnete"], voisine["n_calibration"][0])}
    if a_besoin_de_saboteurs(t):
        choix.add("CH5_SABOTEUR_DECALAGE_DE_LA_LOI_HONNETE")
        base = loi_pour_le_moteur(loi_h, n)
        saboteurs = {nom: {"type": "decalage", "parametres": {"loi": base, "delta_en_ecarts_types": d}}
                     for nom, d in zip(AIRES_NOMMEES, f["saboteur"]["decalages"])}
        lois["saboteurs"] = garder_saboteurs(t, saboteurs, choix)
    return lois


def copy_simple(x):
    return json.loads(json.dumps(x))


def lois_du_monde_m(m, t, choix):
    """v3 (D3, mot de la mère) : aucun témoin du monde M n'est converti tant que la lettre ne
    dit pas γ (la forme ne porte aucun champ γ sur un témoin, et le § 3.3 exige un témoin au
    réglage γ = 0). La conversion de la v2 (populations dans l'ordre, honnête en mélange) se
    retrouve au différentiel v2 → v3, pour le jour où la lettre dira γ."""
    raise NonConvertible("NC_MONDE_M_SANS_GAMMA")


def derive_de_la_famille_f(ctx):
    """CH7 (v3) : le décalage de la dérive de F, lu dans `valeurs_de_plus` de T09 par la règle
    de la mère (`lire_decalage_de_t09`). Rend (famille F, valeur, rang de la clé) ou None. La
    valeur est transmise telle quelle ; le contrôle qu'elle triple un taux de 1 % sous la loi
    de la tranche associée à T09 sera fait par le mode `--recalculer` de la v2 du programme de
    vérité (v4, R1), non par ce programme."""
    f = next((f for f, _ in ctx.familles if f["id"] == "F"), None)
    t09 = next((t for t, _ in ctx.temoins if t["id"] == "T09"), None)
    if f is None or t09 is None:
        return None
    lu = lire_decalage_de_t09(t09.get(CLE_VALEURS_DE_PLUS))
    return None if lu is None else (f, lu[1], lu[0])


def convertir_temoin(t, ctx, familles, derive_de_f, choix):
    regle = dict(t["regle"])
    if regle["type"] == "k_ieme_plus_grand":
        regle["k"] = entier_simple(regle["k"])
    entree = {"id": t["id"], "n": entier_simple(t["n"]), "regle": regle, "garantie": t["garantie"],
              "risque_ou_niveau": t["risque_ou_niveau"], "grandeur": t["grandeur"],
              "population_de_calibration": t["population_de_calibration"],
              "portee_de_la_garantie": t["portee_de_la_garantie"]}
    if t["monde"] == "S":
        s = ctx.doc["monde_S"]
        entree["lois"] = {}
        entree["suite"] = {"taux_honnete": s["taux_honnete"], "horizon": entier_simple(s["horizon"]),
                           "taux_saboteur": s["taux_saboteur"], "taux_honnete_derive": s["taux_honnete_derive"]}
    elif t["monde"] == "M":
        entree["lois"] = lois_du_monde_m(ctx.doc["monde_M"], t, choix)
    else:
        entree["lois"] = lois_de_famille(familles[t["monde"]], t, choix, derive_de_f)
    if t["id"] == "T07":
        choix.add("CH9_T07_TAILLE_DE_PLUS_400")
        entree["tailles_de_plus"] = [TAILLE_DE_PLUS_T07]
    entree["valeur_annoncee"] = t["valeur_vraie"]
    entree["issue_annoncee"] = t["issue_attendue"]
    return entree


def vers_recalcul(doc):
    ctx = Contexte(doc)
    familles = {f["id"]: f for f, _ in ctx.familles}
    familles.update({f["id"]: f for f, _, _ in ctx.ecart})
    derive_de_f = derive_de_la_famille_f(ctx)
    entrees, compte = [], []
    for t, chemin in ctx.temoins + ctx.temoins_ecart:
        choix = set()
        ligne = {"chemin": chemin}
        if not chemin.startswith("a_l_ecart") and RE_IDENTIFIANT_SUR.fullmatch(t["id"]):
            ligne["temoin"] = t["id"]
        try:
            entrees.append(convertir_temoin(t, ctx, familles, derive_de_f, choix))
            ligne["statut"] = "converti"
        except NonConvertible as nc:
            ligne["statut"] = "non_converti"
            ligne["raison"] = nc.code
        ligne["choix"] = sorted(choix)
        compte.append(ligne)
    # v3 (D2) : pour le journal de la session, la valeur transmise et le rang de sa clé.
    if not any(f["id"] == "F" for f, _ in ctx.familles):
        derive = {"statut": "sans_famille_F"}
    elif derive_de_f is None:
        derive = {"statut": "illisible_F_a_ecarter"}
    else:
        # Précisions de la mère : le contrôle se fait sous la loi de la tranche associée à T09,
        # celle dont `n_calibration` contient 299 (la première, si plusieurs la contiennent) ;
        # tolérance ABSOLUE de 10⁻³ sur le taux de 3 % (comme le seuil du § 6, point 4).
        # v4 (R1) : ce contrôle n'est fait par aucun programme scellé ; il sera porté dans le mode
        # `--recalculer` de la v2 du programme de vérité. Ce programme ne le fait pas : il transmet
        # tout ce que le contrôle demande.
        tranches = derive_de_f[0]["tranches"]
        rangs_a_299 = [i for i, tr in enumerate(tranches)
                       if any(est_entier(x) and int(x) == N_DE_T09 for x in tr["n_calibration"])]
        rang_tranche = rangs_a_299[0] if rangs_a_299 else None
        retenue = rang_tranche if rang_tranche is not None else 0
        derive = {"statut": "lue", "temoin": "T09", "n_du_temoin": N_DE_T09,
                  "rang_de_la_cle": derive_de_f[2],
                  "valeur_transmise": getattr(derive_de_f[1], "texte", None) or str(derive_de_f[1]),
                  "unite_du_decalage": "ecarts types de la loi de la tranche associée à T09",
                  "tranche_associee_a_T09": {"rang": retenue + 1,
                                             "n_calibration_contient_299": rang_tranche is not None,
                                             "rangs_des_tranches_a_299": [i + 1 for i in rangs_a_299],
                                             "regle": "la première tranche dont n_calibration contient 299 ; "
                                                      "si aucune, la première tranche, signalée"},
                  "loi_de_la_tranche": ecrire_brut(tranches[retenue]["loi_honnete"]),
                  "loi_de_la_tranche_format": "texte JSON d'une loi de la grammaire, nombres écrits tels quels",
                  "controle": {"par": "programme de vérité v2, mode --recalculer",
                               "critere": "sous la loi de la tranche associée à T09, le seuil au quantile à 99 % "
                                          "(taux de départ de 1 %) a, sous la même loi décalée de la valeur "
                                          "transmise, un taux de 3 %",
                               "taux_de_depart": TAUX_DE_DEPART_DE_LA_DERIVE, "taux_vise": TAUX_VISE_PAR_LA_DERIVE,
                               "tolerance": TOLERANCE_DU_CONTROLE_DE_DERIVE, "nature_de_la_tolerance": "absolue",
                               "fait_par_ce_programme": False}}
    return {"version_entree": VERSION_ENTREE_RECALCUL, "temoins": entrees}, compte, derive


def principal_vers_recalcul(argv):
    try:
        sortie, entree, chemin_motifs = lire_arguments(argv)
        motifs = charger_motifs(chemin_motifs)
        compte_rendu = Path(str(entree) + ".correspondance.json")
        if not sortie.is_file():
            raise ErreurDUsage("sortie de l'auteur introuvable")
        if entree.exists() or compte_rendu.exists():
            raise ErreurDUsage("l'entrée ou son compte rendu existe déjà : on n'écrase jamais")
        with open(sortie, "rb") as fh:
            octets = fh.read(GARDE_DE_LECTURE_OCTETS + 1)
    except ErreurDUsage as e:
        print("erreur : " + str(e), file=sys.stderr)
        return SORTIE_ERREUR
    except OSError:
        print("erreur : lecture impossible", file=sys.stderr)
        return SORTIE_ERREUR
    try:
        resultat = verifier(octets, motifs)
        if resultat["verdict_d_ensemble"] != "lisible":  # garde : sortie illisible, rien n'est converti
            print("refus : la sortie est illisible ; aucune entrée de recalcul n'est écrite", file=sys.stderr)
            return SORTIE_ILLISIBLE
        doc, _, _ = lire_le_texte(Constat(), octets)
        donnees, compte, derive = vers_recalcul(doc)
        texte_entree = ecrire_brut(donnees) + "\n"
    except Exception:  # garde v2 : exception imprévue pendant la correspondance
        print("erreur : exception imprévue pendant la correspondance ; rien n'est écrit", file=sys.stderr)
        return SORTIE_ERREUR
    rendu = {
        "programme": {"nom": NOM_PROGRAMME, "sha256": empreinte(Path(__file__).read_bytes())},
        "sortie_auteur_sha256": empreinte(octets),
        "entree_recalcul_sha256": empreinte(texte_entree.encode("utf-8")),
        "verification": {"verdict_d_ensemble": resultat["verdict_d_ensemble"], "code_de_sortie": resultat["code_de_sortie"],
                         "ecartes": resultat["ecartes"]},
        "temoins": compte,
        "comptes": {"convertis": sum(1 for x in compte if x["statut"] == "converti"),
                    "non_convertis": sum(1 for x in compte if x["statut"] == "non_converti")},
        "choix_declares": sorted({ch for x in compte for ch in x["choix"]}),
        "derive_de_F": derive,
    }
    try:
        with open(entree, "x", encoding="utf-8") as fh:
            fh.write(texte_entree)
        with open(compte_rendu, "x", encoding="utf-8") as fh:
            fh.write(json.dumps(rendu, sort_keys=True, ensure_ascii=False, indent=2) + "\n")
    except OSError:
        print("erreur : écriture impossible", file=sys.stderr)
        return SORTIE_ERREUR
    print("correspondance : %d témoins convertis, %d non convertis" % (rendu["comptes"]["convertis"], rendu["comptes"]["non_convertis"]))
    return SORTIE_TOUT_TENU


def charger_motifs(chemin):
    if not chemin.is_file():
        raise ErreurDUsage("fichier de motifs introuvable")
    try:
        lignes = chemin.read_text(encoding="utf-8").splitlines()
    except (OSError, UnicodeDecodeError):
        raise ErreurDUsage("fichier de motifs illisible")
    motifs = []
    for n, ligne in enumerate(lignes, 1):
        ligne = ligne.strip()
        if not ligne or ligne.startswith("#"):
            continue
        try:
            motifs.append(re.compile(ligne, re.IGNORECASE))
        except re.error:
            raise ErreurDUsage("motif invalide à la ligne %d du fichier de motifs" % n)
    if not motifs:
        raise ErreurDUsage("fichier de motifs sans aucun motif")
    return motifs


def lire_arguments(argv):
    pos, motifs = [], None
    i = 0
    while i < len(argv):
        if argv[i] == "--motifs":
            if i + 1 >= len(argv) or motifs is not None:
                raise ErreurDUsage("--motifs attend un seul fichier")
            motifs = argv[i + 1]
            i += 2
        else:
            pos.append(argv[i])
            i += 1
    if len(pos) != 2:
        raise ErreurDUsage("usage : SORTIE_AUTEUR RAPPORT_JSON [--motifs FICHIER]")
    if motifs is None:
        motifs = str(Path(__file__).resolve().parent / FICHIER_MOTIFS_PAR_DEFAUT)
    return Path(pos[0]), Path(pos[1]), Path(motifs)


def empreinte(octets):
    return hashlib.sha256(octets).hexdigest()


def principal(argv):
    if argv and argv[0] == "--vers-recalcul":
        return principal_vers_recalcul(argv[1:])
    try:
        sortie, rapport, chemin_motifs = lire_arguments(argv)
        motifs = charger_motifs(chemin_motifs)
        if not sortie.is_file():
            raise ErreurDUsage("sortie de l'auteur introuvable")
        if rapport.exists():
            raise ErreurDUsage("le rapport existe déjà : on n'écrase jamais")
        with open(sortie, "rb") as fh:
            octets = fh.read(GARDE_DE_LECTURE_OCTETS + 1)
    except ErreurDUsage as e:
        print("erreur : " + str(e), file=sys.stderr)
        return SORTIE_ERREUR
    except OSError:
        print("erreur : lecture impossible", file=sys.stderr)
        return SORTIE_ERREUR
    try:
        resultat = verifier(octets, motifs)
    except Exception:  # garde v2 (C1) : exception imprévue
        # Aucun repli silencieux (R5) : rien n'est jugé, aucun rapport, code 3. Le message ne
        # recopie rien de la sortie de l'auteur.
        print("erreur : exception imprévue pendant la vérification ; rien n'est jugé", file=sys.stderr)
        return SORTIE_ERREUR
    resultat["programme"] = {"nom": NOM_PROGRAMME, "sha256": empreinte(Path(__file__).read_bytes()),
                             "mandat_de_l_auteur_sha256": "816313cb342a642e4dadda6d111e30fff2800eda2a7975722a0961c5ec05dbe9"}
    resultat["sortie_auteur"]["sha256"] = empreinte(octets)
    resultat["motifs"] = {"sha256": empreinte(chemin_motifs.read_bytes()), "nombre": len(motifs)}
    try:
        with open(rapport, "x", encoding="utf-8") as fh:
            fh.write(json.dumps(resultat, sort_keys=True, ensure_ascii=False, indent=2) + "\n")
    except OSError:
        print("erreur : écriture du rapport impossible", file=sys.stderr)
        return SORTIE_ERREUR
    print("verdict : %s ; code de sortie %d" % (resultat["verdict_d_ensemble"], resultat["code_de_sortie"]))
    return resultat["code_de_sortie"]


if __name__ == "__main__":
    sys.exit(principal(sys.argv[1:]))
