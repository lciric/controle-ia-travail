"""Véhicule NA-1, lot 6 v4 — la course alimente le registre des tentatives (filiation, espèce, case, repli) et rend les
comptes de M6, de M3, de M4 et des replis ; garde du coffre (arrêt n° 5) sur les fiches rendues, servies par repli
comprises ; contrôle d'empreinte du code chargé (C-1 à C-4) (`course_na_v4`).

Lettre : interface commune des lots 5 v2, 6 v4 et 7 v1 (`interface-lots-5-6-7-repli-v1.md`) ; V9 (`864f39a7…`), l. 92 à
101 (classes d'issue), l. 148 à 161 (M3, M4, M6), l. 372 (n° 1), l. 376 (n° 5) ; projet d'additif v2 du véhicule, § 3 (C-1
à C-4, arrêt n° 33), § 5 (P1, P4, P7 à P10, P12, P16, P17 ; définitions de « tentative », « servie », « chaîne ») et § 10
(n° 31, n° 34) ; nœuds ouverts v2, § 3 (N3) et § 5.2, point 6 (lot 6 v4) ; conception v5, § 2.6, § 2.8, § 2.13.

**Ce module ne change rien au v3** (`course_na_v3.py`, `7c154a89…`) : il s'ajoute à côté, sans importer le v3 ni aucun
module des lots 1 à 5, du lot 10 a ou de la v68, que ce développement n'a pas le droit de lire. Il code contre l'interface :
le registre est reçu (toute classe qui offre `ajouter(champs)` et `lignes()`), la chaîne d'un appel est lue par
`tentatives_de_l_appel` sur la forme écrite plus bas (lot 4 v2 : « le repli comme des tentatives successives de
`rang_repli` 0, 1, 2 rendues par l'appel »). Le branchement dans `GenerationNA` (proposition, aiguillage, ligne de la
génération, l. 774 du v3) est décrit au rapport, non fait ici.

**Une chaîne** compte une à trois tentatives (modèle du rôle, premier repli, second repli). Une tentative est **servie** si
la raison d'arrêt lue n'est pas « refusal » ; **refusée** si elle l'est ; **en erreur** si aucune réponse n'est rendue
(raison absente). Seule une tentative refusée est suivie d'une autre (A6). Le registre reçoit **une ligne par tentative**
(`classe` nulle) et **une ligne par fiche rendue** (`classe` du portier), qui porte les champs de la tentative servie qui
l'a rendue, coût mis à zéro pour qu'une somme naïve ne compte pas deux fois (le coût vit à la ligne de la tentative).

**Classe d'issue écrite** (`classe_issue`) :
- tentative de rang 0 : la classe **de la chaîne à l'espèce demandée** (P12) : la classe de la V9 si elle est servie au
  rang 0 ; « refus par classifieur, servi par repli » si une tentative de repli est servie ; « réponse illisible » si la
  chaîne finit en erreur (sous-compte « cause non établie, en repli » si l'erreur suit un refus) ;
- tentative de rang 1 ou 2 servie : la classe de la V9 de sa réponse (rubrique « servies par repli ») ;
- tentative refusée suivie d'une servie : « refus par classifieur, servi par repli » ;
- **deux valeurs hors de la liste fermée de l'interface, déclarées au rapport** (l'interface ne dit rien pour ces cas) :
  `CLASSE_ARRET_1` pour une chaîne qui finit sur un refus (trois refus : n° 1 ; aucune classe de M6, P12), et
  `CLASSE_HORS_M6` pour une tentative servie d'un rôle qui n'est pas un proposeur (portier, juges, aiguilleur).

**Comptes** (lus sur les lignes du registre, jamais sur un état en mémoire) : M6 par génération, par rôle, par espèce
demandée, par case, et par (case, espèce), sur les **seules tentatives de rang 0** des proposeurs ; replis par espèce
demandée et par modèle servi (nombre, coût), et par modèle demandé ; servies par repli, à part, au nom du modèle servi ; M3
en lecture scellée (fiches de repli comprises) et en lecture « espèces seules » ; M4 : la première tentative seule à
l'espèce, une ligne « replis » ; garde du coffre sur les fiches rendues de la génération, servies par repli comprises.

**Contrôle du code chargé** (C-1) : l'empreinte du fichier source de chaque module chargé qui vit sous la racine du paquet,
ou dont le nom est dans un espace protégé, est comparée à la table d'empreintes du paquet ; hors table ou autre empreinte :
arrêt n° 33. Réserve déclarée (C-3) : une modification en mémoire (classe vidée, `__code__` échangé) n'est pas vue.

Aucun message d'erreur ne recopie un énoncé, une idée, un nom de fiche ni un identifiant de modèle servi. Bibliothèque
standard seule.
"""

import dataclasses
import decimal
import hashlib
import json
import os
import re
import sys

VERSION = "course-na-v4"
NOM_COMPTES = "comptes-tentatives-et-replis-na-v4.json"

ESPECES_PROPOSEUSES = ("espece-1", "espece-2", "espece-3", "espece-4", "espece-5")
ESPECES = ESPECES_PROPOSEUSES + ("aiguilleur", "portier", "juge-1", "juge-2", "passe-x")
ESPECE_SANS_CASE = "passe-x"

FICHES_RENDUES = "fiches rendues"
VIDE_MOTIVEE = "réponse vide motivée"
REFUS_DU_MODELE = "refus du modèle"
ILLISIBLE = "réponse illisible"
CLASSES_V9 = (FICHES_RENDUES, VIDE_MOTIVEE, REFUS_DU_MODELE, ILLISIBLE)
SERVI_PAR_REPLI = "refus par classifieur, servi par repli"
CLASSES_INTERFACE = CLASSES_V9 + (SERVI_PAR_REPLI,)
CLASSES_M6 = (VIDE_MOTIVEE, REFUS_DU_MODELE, ILLISIBLE, SERVI_PAR_REPLI)
# Hors de la liste fermée de l'interface : déclarées au rapport, à trancher par la coordination.
CLASSE_ARRET_1 = "arrêt n° 1, consigné, non relancé"
CLASSE_HORS_M6 = "servie, rôle sans classe d'issue d'appel"
CLASSES_ECRITES = CLASSES_INTERFACE + (CLASSE_ARRET_1, CLASSE_HORS_M6)
SOUS_COMPTE_EN_REPLI = "cause non établie, en repli"

PASSEE, AU_COFFRE, HORS_CASE = "passée", "au coffre", "hors case"
CLASSES_FICHE = (PASSEE, AU_COFFRE, HORS_CASE)

RAISON_REFUS = "refusal"
SANS_REPONSE = "sans réponse"  # modèle servi d'une tentative en erreur (aucune réponse) : déclaré au rapport
RANGS = (0, 1, 2)

CHAMPS_LOT_5_V1 = ("identifiant", "generation", "case", "classe", "nom", "enonce")
CHAMPS_INTERFACE = ("generation", "filiation", "espece", "case", "rang_repli", "modele_demande", "modele_servi",
                    "raison_arret", "categorie_refus", "cout_compte_usd", "classe_issue")

NUMERO_ARRET_COFFRE = 5
NUMERO_ARRET_MODELE_SERVI = 31
NUMERO_ARRET_PIRE = 34
NUMERO_ARRET_CODE_CHARGE = 33

_IDENTIFIANT_ROLE = re.compile(r"^[a-z][a-z0-9-]{1,62}$")
_HEX64 = re.compile(r"^[0-9a-f]{64}$")


# --- erreurs et arrêts ---------------------------------------------------------------------------------------------------

class DefautLot6V4(RuntimeError):
    """Une entrée qui ne tient pas sa forme : rien n'est écrit, rien n'est réparé ; le message ne recopie aucun contenu."""


class ArretNommeV4(RuntimeError):
    numero = None
    nom = None


class ArretModeleServiNA(ArretNommeV4):
    """N° 31 : modèle servi absent, ou autre que celui que la tentative demande."""

    numero = NUMERO_ARRET_MODELE_SERVI
    nom = "modèle servi absent ou différent du modèle demandé de la tentative"

    def __init__(self, espece, rang, cause):
        super().__init__(f"arrêt n° {self.numero}, {self.nom} : espèce « {espece} », rang {rang} ; {cause}")
        self.espece, self.rang, self.cause = espece, rang, cause


class ArretRepliNonPermisNA(ArretNommeV4):
    """A6 : une tentative de plus après une tentative qui n'est pas refusée, ou un repli sur une espèce sans repli."""

    numero = None
    nom = "repli hors de la liste fermée"

    def __init__(self, espece, rang, cause):
        super().__init__(f"{self.nom} : espèce « {espece} », rang {rang} ; {cause}")
        self.espece, self.rang, self.cause = espece, rang, cause


class ArretPireManquantNA(ArretNommeV4):
    """N° 34 : un (rôle, modèle) sans pire écrit ; départ refusé."""

    numero = NUMERO_ARRET_PIRE
    nom = "pire manquant pour un (rôle, modèle)"

    def __init__(self, espece, modele):
        super().__init__(f"arrêt n° {self.numero}, {self.nom} : espèce « {espece} », modèle « {modele} »")


class ArretGardeCoffreV4(ArretNommeV4):
    """N° 5 : strictement plus d'un quart des fiches rendues d'une génération au coffre, servies par repli comprises."""

    numero = NUMERO_ARRET_COFFRE
    nom = "garde du coffre"

    def __init__(self, generation, au_coffre, rendues, dont_repli):
        super().__init__(f"arrêt n° {self.numero}, {self.nom} : génération {generation}, {au_coffre} au coffre sur "
                         f"{rendues} fiches rendues (dont {dont_repli} servies par repli) ; la génération suivante ne part pas")
        self.generation, self.au_coffre, self.rendues, self.dont_repli = generation, au_coffre, rendues, dont_repli


class ArretCodeChargeNA(ArretNommeV4):
    """N° 33 : module chargé hors table, ou d'une autre empreinte, ou sans source lisible ; départ ou génération refusé."""

    numero = NUMERO_ARRET_CODE_CHARGE
    nom = "code chargé hors table ou d'une autre empreinte"

    def __init__(self, moment, module, cause):
        super().__init__(f"arrêt n° {self.numero}, {self.nom} ({moment}) : module « {module} » ; {cause}")
        self.moment, self.module, self.cause = moment, module, cause


# --- montants ------------------------------------------------------------------------------------------------------------

def montant(x):
    """Un coût en dollars, décimal exact, positif ou nul ; refuse booléen, NaN, infini, négatif, texte non décimal."""
    if isinstance(x, bool) or x is None:
        raise DefautLot6V4("coût : un nombre positif ou nul")
    try:
        d = x if isinstance(x, decimal.Decimal) else decimal.Decimal(str(x))
    except (decimal.InvalidOperation, ValueError, TypeError):
        raise DefautLot6V4("coût : un nombre décimal") from None
    if not d.is_finite() or d < 0:
        raise DefautLot6V4("coût : un nombre fini, positif ou nul")
    return d


def texte_montant(d):
    return format(montant(d), "f")


# --- configuration des replis (champ distinct de `a11_modeles`, P16) ---------------------------------------------------

@dataclasses.dataclass(frozen=True)
class ConfigurationReplisNA:
    """Ce que la course lit de la configuration pour les replis : le modèle de chaque espèce (identifiant par rôle), les
    deux modèles de repli (premier, second), les espèces sur clé Claude (seules à avoir un repli), l'identifiant lu dans la
    réponse attendu pour chaque identifiant par rôle, le pire de chaque (espèce, modèle) et l'étiquette de rôle de chaque
    espèce proposeuse. `a11_modeles` reste vide et n'est pas lu ici."""

    modele_du_role: dict
    modeles_de_repli: tuple
    especes_avec_repli: frozenset
    modele_reel: dict
    pires: dict
    role_de_l_espece: dict

    def __post_init__(self):
        if not isinstance(self.modele_du_role, dict) or set(self.modele_du_role) != set(ESPECES):
            raise DefautLot6V4("modèle du rôle : une entrée par espèce de la liste fermée")
        if not isinstance(self.modeles_de_repli, tuple) or len(self.modeles_de_repli) != 2 \
                or self.modeles_de_repli[0] == self.modeles_de_repli[1]:
            raise DefautLot6V4("modèles de repli : deux, distincts (premier, second)")
        ids = set(self.modele_du_role.values()) | set(self.modeles_de_repli)
        for m in ids:
            if type(m) is not str or not _IDENTIFIANT_ROLE.match(m):
                raise DefautLot6V4("identifiant par rôle : minuscules, chiffres et traits")
        if set(self.modeles_de_repli) & set(self.modele_du_role.values()):
            raise DefautLot6V4("un modèle de repli n'est le modèle d'aucune espèce")
        if not isinstance(self.especes_avec_repli, frozenset) or not self.especes_avec_repli <= set(ESPECES):
            raise DefautLot6V4("espèces avec repli : une partie de la liste fermée")
        if not isinstance(self.modele_reel, dict) or set(self.modele_reel) != ids \
                or any(type(v) is not str or not v for v in self.modele_reel.values()):
            raise DefautLot6V4("identifiant attendu dans la réponse : un par identifiant par rôle")
        if not isinstance(self.role_de_l_espece, dict) or set(self.role_de_l_espece) != set(ESPECES_PROPOSEUSES) \
                or len(set(self.role_de_l_espece.values())) != len(ESPECES_PROPOSEUSES):
            raise DefautLot6V4("étiquette de rôle : une, distincte, par espèce proposeuse")
        if not isinstance(self.pires, dict):
            raise DefautLot6V4("pires : un dictionnaire (espèce, modèle) -> dollars")

    def suite(self, espece):
        """La suite fermée des modèles demandés d'une chaîne de l'espèce."""
        if espece in self.especes_avec_repli:
            return (self.modele_du_role[espece],) + self.modeles_de_repli
        return (self.modele_du_role[espece],)

    def verifier_pires(self):
        """N° 34 : chaque (espèce, modèle) de chaque suite a son pire ; rend le nombre de couples vérifiés."""
        n = 0
        for e in ESPECES:
            for m in self.suite(e):
                if (e, m) not in self.pires:
                    raise ArretPireManquantNA(e, m)
                montant(self.pires[(e, m)])
                n += 1
        return n


# --- une tentative, une chaîne -------------------------------------------------------------------------------------------

@dataclasses.dataclass(frozen=True)
class TentativeNA:
    rang_repli: int
    modele_demande: str
    modele_servi: str  # lu dans la réponse ; `SANS_REPONSE` pour une tentative en erreur
    raison_arret: object  # chaîne, ou None si aucune réponse
    categorie_refus: object  # chaîne ou None, jamais devinée
    cout_compte_usd: decimal.Decimal

    @property
    def refusee(self):
        return self.raison_arret == RAISON_REFUS

    @property
    def en_erreur(self):
        return self.raison_arret is None

    @property
    def servie(self):
        return not self.refusee and not self.en_erreur


def tentatives_de_l_appel(a, espece, config):
    """Lit et vérifie la chaîne qu'un appel rend (`a["tentatives_na"]`, une liste de dictionnaires : `rang_repli`,
    `modele_demande`, `modele_servi`, `raison_arret`, `categorie_refus`, `cout_compte_usd`, `usage_manquant`). Forme
    attendue du lot 4 v2, déclarée au rapport. Rien n'est réparé : une chaîne hors forme est refusée, jamais lue à moitié."""
    if espece not in ESPECES:
        raise DefautLot6V4("espèce hors de la liste fermée")
    if not isinstance(a, dict) or "tentatives_na" not in a:
        raise DefautLot6V4("l'appel ne rend pas ses tentatives (`tentatives_na`) : aucune lecture sans elles")
    brutes = a["tentatives_na"]
    if not isinstance(brutes, list) or not 1 <= len(brutes) <= len(RANGS):
        raise DefautLot6V4("une chaîne compte une à trois tentatives")
    suite = config.suite(espece)
    if len(brutes) > len(suite):
        raise ArretRepliNonPermisNA(espece, len(brutes) - 1, "repli sur une espèce sans repli (clé hors Claude)")
    rendu = []
    for i, t in enumerate(brutes):
        if not isinstance(t, dict) or t.get("rang_repli") != i or type(t.get("rang_repli")) is not int:
            raise DefautLot6V4("rangs de repli : 0, 1, 2, dans l'ordre")
        demande = t.get("modele_demande")
        if demande != suite[i]:
            raise ArretRepliNonPermisNA(espece, i, "modèle demandé hors de la suite fermée de l'espèce")
        raison = t.get("raison_arret")
        if raison is not None and (type(raison) is not str or not raison):
            raise DefautLot6V4("raison d'arrêt : une chaîne lue, ou absente si aucune réponse")
        categorie = t.get("categorie_refus")
        if categorie is not None and (type(categorie) is not str or not categorie):
            raise DefautLot6V4("catégorie : une chaîne lue, ou nulle")
        if categorie is not None and raison != RAISON_REFUS:
            raise DefautLot6V4("une catégorie n'accompagne qu'un refus par classifieur")
        servi = t.get("modele_servi")
        if raison is None:
            if servi is not None:
                raise DefautLot6V4("une tentative sans réponse n'a pas de modèle servi")
            servi = SANS_REPONSE
        else:
            if type(servi) is not str or not servi:
                raise ArretModeleServiNA(espece, i, "modèle servi absent")
            if servi != config.modele_reel[demande]:
                raise ArretModeleServiNA(espece, i, "modèle servi différent du modèle demandé de la tentative")
        if "cout_compte_usd" not in t or type(t.get("usage_manquant")) is not bool:
            raise DefautLot6V4("coût compté et drapeau d'usage manquant : dits")
        cout = montant(t["cout_compte_usd"])
        if t["usage_manquant"]:
            if (espece, demande) not in config.pires:
                raise ArretPireManquantNA(espece, demande)
            if cout != montant(config.pires[(espece, demande)]):
                raise DefautLot6V4("usage manquant : le coût compté est le pire de la tentative, jamais moins")
        rendu.append(TentativeNA(i, demande, servi, raison, categorie, cout))
    for t in rendu[:-1]:
        if not t.refusee:
            raise ArretRepliNonPermisNA(espece, t.rang_repli + 1, "repli après une tentative qui n'est pas refusée")
    return tuple(rendu)


def classe_de_la_chaine(tentatives, classe_servie, proposeur):
    """La classe de la chaîne à l'espèce demandée (P12), et son sous-compte de M6 ou None."""
    der = tentatives[-1]
    if der.servie:
        if der.rang_repli > 0:
            return SERVI_PAR_REPLI, None
        return (classe_servie if proposeur else CLASSE_HORS_M6), None
    if der.en_erreur:
        return ILLISIBLE, (SOUS_COMPTE_EN_REPLI if der.rang_repli > 0 else None)
    return CLASSE_ARRET_1, None


def classe_de_la_tentative(tentatives, i, classe_servie, proposeur):
    """La classe écrite à la ligne de la tentative de rang `i` (voir l'en-tête)."""
    if i == 0:
        return classe_de_la_chaine(tentatives, classe_servie, proposeur)[0]
    t, der = tentatives[i], tentatives[-1]
    if t.servie:
        return classe_servie if proposeur else CLASSE_HORS_M6
    if t.en_erreur:
        return ILLISIBLE
    if der.servie:
        return SERVI_PAR_REPLI
    if der.en_erreur:
        return ILLISIBLE
    return CLASSE_ARRET_1


# --- l'alimentation du registre ------------------------------------------------------------------------------------------

def _filiation(f):
    v = f.get("filiation")
    if v is None or v == "aucune":
        return None
    if type(v) is not str or not v:
        raise DefautLot6V4("filiation : un identifiant de fiche, « aucune » ou nulle")
    return v


class AlimentationRegistreNA:
    """Écrit au registre des tentatives, par l'interface `ajouter(champs)`, une ligne par tentative et une ligne par fiche
    rendue. `champs_fermes` : les trois champs fermés du contrat de fiche (lot 5), lus dans la configuration."""

    def __init__(self, registre, config, champs_fermes):
        if not callable(getattr(registre, "ajouter", None)):
            raise DefautLot6V4("le registre offre `ajouter(champs)` (interface du lot 5 v2)")
        if not isinstance(config, ConfigurationReplisNA):
            raise DefautLot6V4("la configuration des replis est une `ConfigurationReplisNA`")
        if not isinstance(champs_fermes, tuple) or len(champs_fermes) != 3:
            raise DefautLot6V4("trois champs fermés")
        self.registre, self.config, self.champs_fermes = registre, config, champs_fermes
        self.chaines = 0

    def consigner_chaine(self, *, identifiant_chaine, generation, espece, case, a, classe_servie=None, fiches=()):
        """Une chaîne d'appel, une fois sa classe connue (le portier a classé la réponse servie d'un proposeur). Rend les
        tentatives lues. Toutes les vérifications ont lieu avant la première écriture."""
        if type(generation) is not int or generation < 1:
            raise DefautLot6V4("génération : un entier, 1, 2, 3…")
        if type(identifiant_chaine) is not str or not identifiant_chaine:
            raise DefautLot6V4("identifiant de chaîne : une chaîne")
        tentatives = tentatives_de_l_appel(a, espece, self.config)
        if espece == ESPECE_SANS_CASE:
            if case is not None:
                raise DefautLot6V4("la passe X n'a pas de case")
        elif type(case) is not str or not case:
            raise DefautLot6V4("une requête de l'espèce a sa case servie")
        proposeur = espece in ESPECES_PROPOSEUSES
        servie = tentatives[-1].servie
        if proposeur and servie:
            if classe_servie not in CLASSES_V9:
                raise DefautLot6V4("classe de la réponse servie : une des quatre de la V9, rendue par le portier")
        elif classe_servie is not None:
            raise DefautLot6V4("classe servie dite pour une chaîne sans réponse servie, ou pour un rôle non proposeur")
        fiches = list(fiches)
        if (classe_servie == FICHES_RENDUES) != bool(fiches):
            raise DefautLot6V4("des fiches si et seulement si la classe est « fiches rendues »")
        lignes_fiche = []
        t_servie = tentatives[-1]
        for f in fiches:
            if not isinstance(f, dict) or f.get("classe") not in CLASSES_FICHE or type(f.get("identifiant")) is not str:
                raise DefautLot6V4("fiche : identifiant et classe du portier")
            ligne = self._champs_tentative(generation, espece, case, t_servie, FICHES_RENDUES, cout_zero=True)
            ligne.update(identifiant=f["identifiant"], classe=f["classe"], filiation=_filiation(f))
            if f["classe"] == PASSEE:
                fermes = f.get("fermes")
                if not isinstance(fermes, dict) or set(fermes) != set(self.champs_fermes) \
                        or any(type(v) is not str for v in fermes.values()) or type(f.get("idee")) is not str:
                    raise DefautLot6V4("fiche passée : trois champs fermés et une idée")
                ligne.update(fermes)
                ligne.update(nom=f["identifiant"], enonce=" ".join(f["idee"].split()))
            lignes_fiche.append(ligne)
        lignes = []
        for i, t in enumerate(tentatives):
            ligne = self._champs_tentative(generation, espece, case, t,
                                           classe_de_la_tentative(tentatives, i, classe_servie, proposeur))
            ligne.update(identifiant=f"{identifiant_chaine}.t{i}", classe=None, filiation=None)
            lignes.append(ligne)
        for ligne in lignes + lignes_fiche:
            self.registre.ajouter(ligne)
        self.chaines += 1
        return tentatives

    @staticmethod
    def _champs_tentative(generation, espece, case, t, classe_issue, cout_zero=False):
        return {"generation": generation, "espece": espece, "case": case, "rang_repli": t.rang_repli,
                "modele_demande": t.modele_demande, "modele_servi": t.modele_servi, "raison_arret": t.raison_arret,
                "categorie_refus": t.categorie_refus,
                "cout_compte_usd": "0" if cout_zero else texte_montant(t.cout_compte_usd), "classe_issue": classe_issue}


# --- lecture des lignes --------------------------------------------------------------------------------------------------

def _verifier_ligne(l):
    if not isinstance(l, dict):
        raise DefautLot6V4("ligne du registre : un dictionnaire")
    for k in CHAMPS_INTERFACE:
        if k not in l:
            raise DefautLot6V4("ligne du registre sans un champ de l'interface")
    if l["espece"] not in ESPECES or l["rang_repli"] not in RANGS or type(l["rang_repli"]) is not int:
        raise DefautLot6V4("espèce ou rang hors de la liste fermée")
    if l["classe_issue"] not in CLASSES_ECRITES:
        raise DefautLot6V4("classe d'issue hors de la liste")
    if l.get("classe") is not None and l["classe"] not in CLASSES_FICHE:
        raise DefautLot6V4("classe de fiche hors de la liste")
    montant(l["cout_compte_usd"])


def lignes_tentatives(lignes):
    return [l for l in lignes if l.get("classe") is None]


def lignes_fiches(lignes):
    return [l for l in lignes if l.get("classe") is not None]


def _plus(d, k, n=1):
    d[k] = d.get(k, 0) + n


def _ajouter_cout(d, k, c):
    d[k] = d.get(k, decimal.Decimal(0)) + c


# --- comptes -------------------------------------------------------------------------------------------------------------

def comptes_m6(lignes, config):
    """M6 par génération : par rôle, par espèce demandée, par case, par (case, espèce) ; sous-compte « cause non établie,
    en repli » ; sur les seules tentatives de rang 0 des espèces proposeuses (une chaîne, un appel, à l'espèce demandée)."""
    rendu = {}
    for l in lignes_tentatives(lignes):
        _verifier_ligne(l)
        if l["rang_repli"] != 0 or l["espece"] not in ESPECES_PROPOSEUSES or l["classe_issue"] not in CLASSES_M6:
            continue
        g = rendu.setdefault(str(l["generation"]), {"par_role": {}, "par_espece": {}, "par_case": {},
                                                     "par_case_et_espece": {}, "sous_comptes": {}})
        k = l["classe_issue"]
        _plus(g["par_role"].setdefault(config.role_de_l_espece[l["espece"]], {}), k)
        _plus(g["par_espece"].setdefault(l["espece"], {}), k)
        _plus(g["par_case"].setdefault(l["case"], {}), k)
        _plus(g["par_case_et_espece"].setdefault(l["case"], {}).setdefault(l["espece"], {}), k)
    # sous-compte : chaîne refusée au rang 0 puis en erreur
    for l in lignes_tentatives(lignes):
        if l["rang_repli"] > 0 and l["raison_arret"] is None and l["espece"] in ESPECES_PROPOSEUSES:
            g = rendu.setdefault(str(l["generation"]), {"par_role": {}, "par_espece": {}, "par_case": {},
                                                         "par_case_et_espece": {}, "sous_comptes": {}})
            _plus(g["sous_comptes"].setdefault(l["espece"], {}), SOUS_COMPTE_EN_REPLI)
    return rendu


def comptes_replis(lignes):
    """Replis (tentatives de rang 1 et 2, refusées, servies ou en erreur) : par génération, par espèce demandée et par
    modèle servi (nombre, coût), et par modèle demandé ; servies par repli, à part, au nom du modèle servi."""
    rendu = {}
    for l in lignes_tentatives(lignes):
        _verifier_ligne(l)
        if l["rang_repli"] == 0:
            continue
        g = rendu.setdefault(str(l["generation"]), {"par_espece_et_modele_servi": {}, "par_modele_demande": {},
                                                     "servies_par_repli": {}})
        c = montant(l["cout_compte_usd"])
        e = g["par_espece_et_modele_servi"].setdefault(l["espece"], {}).setdefault(
            l["modele_servi"], {"nombre": 0, "cout_usd": decimal.Decimal(0)})
        e["nombre"] += 1
        e["cout_usd"] += c
        d = g["par_modele_demande"].setdefault(l["modele_demande"], {"nombre": 0, "cout_usd": decimal.Decimal(0)})
        d["nombre"] += 1
        d["cout_usd"] += c
        if l["raison_arret"] is not None and l["raison_arret"] != RAISON_REFUS:
            s = g["servies_par_repli"].setdefault(l["modele_servi"], {"tentatives": {}, "fiches": {}})
            _plus(s["tentatives"], l["classe_issue"])
    for l in lignes_fiches(lignes):
        _verifier_ligne(l)
        if l["rang_repli"] == 0:
            continue
        g = rendu.setdefault(str(l["generation"]), {"par_espece_et_modele_servi": {}, "par_modele_demande": {},
                                                     "servies_par_repli": {}})
        s = g["servies_par_repli"].setdefault(l["modele_servi"], {"tentatives": {}, "fiches": {}})
        _plus(s["fiches"], l["classe"])
    return rendu


def comptes_m3(lignes):
    """M3 par génération et par case : au coffre, hors case, rendues ; lecture scellée (fiches de repli comprises) et
    lecture « espèces seules » (sans elles) ; les fiches servies par repli à part, par modèle servi."""
    rendu = {}
    for l in lignes_fiches(lignes):
        _verifier_ligne(l)
        g = rendu.setdefault(str(l["generation"]), {"scellee": {}, "especes_seules": {}, "servies_par_repli": {}})
        lectures = ["scellee"] + (["especes_seules"] if l["rang_repli"] == 0 else [])
        for lec in lectures:
            c = g[lec].setdefault(l["case"], {"rendues": 0, AU_COFFRE: 0, HORS_CASE: 0})
            c["rendues"] += 1
            if l["classe"] in (AU_COFFRE, HORS_CASE):
                c[l["classe"]] += 1
        if l["rang_repli"] > 0:
            _plus(g["servies_par_repli"].setdefault(l["modele_servi"], {}), l["classe"])
    return rendu


def comptes_m4(lignes):
    """M4 par génération : coût et fiches passées par espèce, **première tentative seule** ; une ligne « replis » (coût des
    tentatives de rang 1 et 2, fiches passées servies par repli), par modèle demandé ; jamais rendue à l'espèce."""
    rendu = {}
    for l in lignes:
        _verifier_ligne(l)
        g = rendu.setdefault(str(l["generation"]), {"par_espece": {}, "replis": {"cout_usd": decimal.Decimal(0),
                                                                                  "par_modele_demande": {},
                                                                                  "fiches_passees": 0}})
        c = montant(l["cout_compte_usd"])
        passee = 1 if l.get("classe") == PASSEE else 0
        if l["rang_repli"] == 0:
            e = g["par_espece"].setdefault(l["espece"], {"cout_usd": decimal.Decimal(0), "fiches_passees": 0})
            e["cout_usd"] += c
            e["fiches_passees"] += passee
        else:
            g["replis"]["cout_usd"] += c
            _ajouter_cout(g["replis"]["par_modele_demande"], l["modele_demande"], c)
            g["replis"]["fiches_passees"] += passee
    return rendu


# --- garde du coffre (arrêt n° 5) ----------------------------------------------------------------------------------------

@dataclasses.dataclass(frozen=True)
class ConstatCoffreV4:
    generation: int
    au_coffre: int
    rendues: int
    dont_repli_rendues: int
    dont_repli_au_coffre: int
    depasse: bool
    consigne: bool


def garde_du_coffre_v4(lignes, generation, derniere_generation=3):
    """N° 5 : sur les **lignes de fiche** de la génération (servies par repli comprises, P8) ; jamais sur les lignes de
    tentative, qui ne sont pas des fiches rendues. Générations avant la dernière : arrêt ; dernière : consigné."""
    if type(generation) is not int or not 1 <= generation <= derniere_generation:
        raise DefautLot6V4("génération hors de la course")
    de_g = [l for l in lignes_fiches(lignes) if l.get("generation") == generation]
    for l in de_g:
        _verifier_ligne(l)
    rendues = len(de_g)
    au_coffre = sum(1 for l in de_g if l["classe"] == AU_COFFRE)
    dr = sum(1 for l in de_g if l["rang_repli"] > 0)
    drc = sum(1 for l in de_g if l["rang_repli"] > 0 and l["classe"] == AU_COFFRE)
    depasse = 4 * au_coffre > rendues
    if depasse and generation < derniere_generation:
        raise ArretGardeCoffreV4(generation, au_coffre, rendues, dr)
    return ConstatCoffreV4(generation, au_coffre, rendues, dr, drc, depasse, depasse and generation == derniere_generation)


# --- tout, pour la ligne de la génération et pour le lot 7 ----------------------------------------------------------------

def _json(x):
    if isinstance(x, decimal.Decimal):
        return format(x, "f")
    if isinstance(x, dict):
        return {k: _json(v) for k, v in x.items()}
    if isinstance(x, (list, tuple)):
        return [_json(v) for v in x]
    return x


def comptes_v4(lignes, config):
    """Tous les comptes du lot 6 v4, sérialisables (montants en chaîne décimale)."""
    lignes = list(lignes)
    return _json({"version": VERSION, "m6": comptes_m6(lignes, config), "replis": comptes_replis(lignes),
                  "m3": comptes_m3(lignes), "m4": comptes_m4(lignes)})


def ecrire_comptes(dossier, comptes):
    """Écrit les comptes dans un fichier neuf (jamais écrasé) et son compagnon ; rend le chemin."""
    octets = (json.dumps(comptes, ensure_ascii=False, sort_keys=True, indent=1) + "\n").encode("utf-8")
    chemin = os.path.join(dossier, NOM_COMPTES)
    with open(chemin, "xb") as f:
        f.write(octets)
    with open(chemin + ".sha256", "x", encoding="utf-8") as f:
        f.write(f"{hashlib.sha256(octets).hexdigest()}  {NOM_COMPTES}\n")
    return chemin


# --- contrôle d'empreinte du code chargé (C-1 à C-4) --------------------------------------------------------------------

def lire_table_empreintes(chemin, sha256_attendu):
    """La table d'empreintes du paquet (`<sha256>  <chemin relatif>` par ligne), vérifiée à son empreinte ; rend
    {chemin relatif normalisé : sha256}."""
    with open(chemin, "rb") as f:
        octets = f.read()
    if hashlib.sha256(octets).hexdigest() != sha256_attendu:
        raise ArretCodeChargeNA("lecture de la table", os.path.basename(chemin), "table d'une autre empreinte")
    table = {}
    for ligne in octets.decode("utf-8").splitlines():
        if not ligne.strip():
            continue
        h, _, rel = ligne.partition("  ")
        if not _HEX64.match(h) or not rel or os.path.isabs(rel) or ".." in rel.split("/"):
            raise ArretCodeChargeNA("lecture de la table", os.path.basename(chemin), "ligne hors forme")
        if rel in table:
            raise ArretCodeChargeNA("lecture de la table", rel, "chemin deux fois")
        table[os.path.normpath(rel)] = h
    return table


def verifier_code_charge(table, racine, moment, *, espaces_proteges=("pole",), modules=None):
    """C-1 : pour chaque module de `sys.modules` (ou `modules`) dont le fichier vit sous `racine`, ou dont le nom est dans
    un espace protégé, l'empreinte du fichier source est celle de la table. Refus (n° 33) : module protégé sans fichier
    source `.py`, fichier hors de la racine, fichier hors table, autre empreinte. Rend la liste triée des chemins vérifiés.
    C-3 : ne voit pas une modification en mémoire (ce n'est pas le fichier qui change)."""
    racine = os.path.realpath(racine)
    modules = sys.modules if modules is None else modules
    vus = []
    for nom, m in sorted(list(modules.items()), key=lambda e: e[0]):
        if m is None:
            continue
        fichier = getattr(m, "__file__", None)
        protege = any(nom == p or nom.startswith(p + ".") for p in espaces_proteges)
        reel = os.path.realpath(fichier) if isinstance(fichier, str) else None
        sous_racine = reel is not None and (reel == racine or reel.startswith(racine + os.sep))
        if not protege and not sous_racine:
            continue
        chemins = getattr(m, "__path__", None)
        if fichier is None and chemins is not None and getattr(getattr(m, "__spec__", None), "origin", None) is None:
            # paquet d'espace de noms : aucun fichier ; chacun de ses dossiers doit être sous la racine
            if not all(os.path.realpath(c).startswith(racine + os.sep) for c in list(chemins)):
                raise ArretCodeChargeNA(moment, nom, "paquet d'espace de noms hors de la racine du paquet")
            continue
        if reel is None or not reel.endswith(".py"):
            raise ArretCodeChargeNA(moment, nom, "aucun fichier source lisible")
        if not sous_racine:
            raise ArretCodeChargeNA(moment, nom, "fichier hors de la racine du paquet")
        rel = os.path.normpath(os.path.relpath(reel, racine))
        if rel not in table:
            raise ArretCodeChargeNA(moment, nom, "module hors table")
        try:
            with open(reel, "rb") as f:
                h = hashlib.sha256(f.read()).hexdigest()
        except OSError:
            raise ArretCodeChargeNA(moment, nom, "fichier source illisible") from None
        if h != table[rel]:
            raise ArretCodeChargeNA(moment, nom, "autre empreinte que celle de la table")
        vus.append(rel)
    return sorted(vus)


RESERVE_C3 = ("C-3, réserve déclarée : le contrôle compare les fichiers sources aux empreintes de la table ; il ne voit "
              "pas une modification en mémoire (méthode vidée sur une classe, `__code__` échangé, objet remplacé après "
              "le contrôle).")

__all__ = ("AlimentationRegistreNA", "ConfigurationReplisNA", "TentativeNA", "tentatives_de_l_appel", "comptes_v4",
           "comptes_m6", "comptes_replis", "comptes_m3", "comptes_m4", "garde_du_coffre_v4", "verifier_code_charge",
           "lire_table_empreintes", "ecrire_comptes", "ArretModeleServiNA", "ArretRepliNonPermisNA",
           "ArretPireManquantNA", "ArretGardeCoffreV4", "ArretCodeChargeNA", "DefautLot6V4")
