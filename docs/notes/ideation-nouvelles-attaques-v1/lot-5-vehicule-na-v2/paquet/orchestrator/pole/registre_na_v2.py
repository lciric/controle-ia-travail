"""Véhicule NA-1, lot 5 v2 — registre des tentatives d'appel, aux champs de l'interface commune des lots 5 v2, 6 v4 et 7
et de son erratum 1 (`registre_na_v2`).

Lettre : interface commune des lots 5 v2, 6 v4 et 7 v1 (`interface-lots-5-6-7-repli-v1.md`, « à implanter telle quelle »)
et son erratum 1 (`erratum-1-interface-lots-5-6-7-repli-v1.md` : trois refus, rôle non proposeur servi par repli,
tentative sans réponse, champ fermé `type_ligne`) ; projet d'additif v2, § 5 (règle de repli, GO-2026-11-22-35 :
tentative, chaîne ; P1, P7 à P12) ; V9, l. 63 (registre servi), l. 92 à 101 (classes d'issue d'appel), l. 152 à 154 (M1,
M1 bis, M2), l. 160 (M6) ; conception du véhicule v5, § 2.6. Le lot 5 v1 (`registre_na_v1`) n'est pas modifié.

**Une ligne** porte les champs du lot 5 v1 (`identifiant`, `generation`, `case`, `classe`, les trois champs fermés, `nom`,
`enonce`), ceux de l'interface (`filiation`, `espece`, `rang_repli`, `modele_demande`, `modele_servi`, `raison_arret`,
`categorie_refus`, `cout_compte_usd`, `classe_issue`) et `type_ligne` (erratum, point 4), **tous présents dans chaque
ligne** ; une valeur sans objet est `null`, jamais omise. Deux types, champ fermé `type_ligne` :
- `tentative` : **une ligne par tentative**, et une seule ; `identifiant`, `classe` et champs de fiche à `null` ;
- `fiche` : une fiche rendue par la tentative qui la précède (classe d'issue « fiches rendues ») ; elle recopie les champs
  de sa tentative, et porte ses champs de fiche.
**Tout compte de fiches ne lit que les lignes `fiche` ; tout compte d'appels et de coût ne lit que les lignes
`tentative`** (erratum, point 4) : le coût d'une tentative n'est donc compté qu'une fois.

**Une chaîne** (additif v2, § 5) : une à trois tentatives, rangs 0, 1, 2, chacune refusée par un classifieur (raison
d'arrêt `refusal`) sauf la dernière. Trois formes de fin :
- *servie* : raison d'arrêt autre que `refusal` et `sans_reponse` ; les refus qui la précèdent ont la classe « refus par
  classifieur, servi par repli » ; la sienne est celle de sa réponse (pour un rôle autre qu'un proposeur, la classe du rôle :
  erratum, point 2) ;
- *sans réponse* (erratum, point 3) : `modele_servi` à `null`, raison d'arrêt `sans_reponse`, classe « réponse illisible » ;
- *trois refus* (erratum, point 1 ; arrêt n° 1) : la troisième a `rang_repli` 2, `refusal`, la classe « refus du modèle »
  de la V9, et aucune fiche.
Une chaîne s'écrit **en un appel** (`ajouter_chaine`), vérifiée entière avant toute écriture.

**Refusé** (`RegistreRefuse`, rien n'est écrit, rien n'est réparé, aucune valeur devinée) : un champ manquant ou en plus ;
une valeur hors des listes fermées (`type_ligne`, `espece`, `classe_issue`, `classe`, `rang_repli`, `case` hors des cases
servies données, `modele_demande` hors des identifiants par rôle donnés) ; une chaîne qui ne tient pas l'une des trois
formes. **Seul `categorie_refus` prend `null` quand il manque** ; elle n'est jamais devinée.

**Ancien format** (`RegistreAncienFormat`) : une ligne du lot 5 v1 (version `registre-tentatives-na-v1`, ou sans
`type_ligne`), l'appel `ajouter_fiche` du v1, l'écriture directe d'un dictionnaire : refusés, et le message le dit.

**Registre servi et garde du coffre** : calculés par le code du v1 sur les seules lignes `fiche`, ramenées à la forme du v1
(le v1 compte toutes ses lignes, `registre_na_v1`, l. 216 ; ici les lignes `tentative` n'y entrent jamais). Rien de
l'espèce, du modèle, du coût ni de la raison d'arrêt n'entre au registre servi. Les fiches servies par repli sont des fiches
rendues de la génération (P8, lecture scellée) : elles y entrent, et dans la garde.

Aucun message d'erreur ne recopie une valeur. Bibliothèque standard, et les modules des lots 1 et 5 v1.
"""

import dataclasses
import math

from pole import contrat_fiche_na_v1 as ct
from pole import identifiants_na_v1 as ident
from pole import portier_na_v1 as pt
from pole import registre_na_v1 as rg
from pole import tirage_na_v4 as tn

VERSION = "registre-na-v2"
VERSION_LIGNE = "registre-tentatives-na-v2"
VERSION_LIGNE_V1 = rg.RegistreTentatives.VERSION

TYPE_TENTATIVE, TYPE_FICHE = "tentative", "fiche"
TYPES_LIGNE = (TYPE_TENTATIVE, TYPE_FICHE)
ESPECES_PROPOSEURS = ("espece-1", "espece-2", "espece-3", "espece-4", "espece-5")
ESPECES = ESPECES_PROPOSEURS + ("aiguilleur", "portier", "juge-1", "juge-2", "passe-x")
RANGS_REPLI = (0, 1, 2)
RAISON_REFUS = "refusal"
RAISON_SANS_REPONSE = "sans_reponse"
REFUS_SERVI_PAR_REPLI = "refus par classifieur, servi par repli"
CLASSE_TROIS_REFUS = pt.REFUS_DU_MODELE      # erratum, point 1 : « la classe « refus » de la v9 »
CLASSE_SANS_REPONSE = pt.ILLISIBLE           # erratum, point 3 : la classe de défaut de la V9 (l. 99)
CLASSES_ISSUE = pt.CLASSES_APPEL + (REFUS_SERVI_PAR_REPLI,)
FILIATION_AUCUNE = "aucune"
CHAMP_FILIATION = "filiation"

CHAMPS_V1 = rg.RegistreTentatives.CHAMPS_PERMIS
CHAMPS_INTERFACE = ("generation", "filiation", "espece", "case", "rang_repli", "modele_demande", "modele_servi",
                    "raison_arret", "categorie_refus", "cout_compte_usd", "classe_issue")
CHAMPS_LIGNE = ("type_ligne",) + CHAMPS_V1 + tuple(c for c in CHAMPS_INTERFACE if c not in CHAMPS_V1)
CHAMPS_TENTATIVE = ("espece", "case", "rang_repli", "modele_demande", "modele_servi", "raison_arret", "categorie_refus",
                    "cout_compte_usd", "classe_issue")
CHAMPS_DE_FICHE = ("identifiant", "classe") + ct.CHAMPS_FERMES + ("nom", "enonce", "filiation")
CHAMPS_DU_FICHIER = ("rang", "precedente", "version")


class RegistreRefuse(RuntimeError):
    """Une ligne ou une chaîne que ce registre n'écrit pas, ou un registre qu'il ne relit pas ; rien n'est écrit, rien
    n'est réparé ; le message ne recopie aucune valeur."""


class RegistreAncienFormat(RegistreRefuse):
    """Un registre, une ligne ou un appel au format du lot 5 v1, donné au lot 5 v2."""

    def __init__(self, ou):
        super().__init__(f"ancien format (lot 5 v1, `{VERSION_LIGNE_V1}`) : {ou} ; le lot 5 v2 exige chaque ligne au "
                         f"format `{VERSION_LIGNE}`, avec `type_ligne` et les champs de l'interface des lots 5 v2, 6 v4 "
                         "et 7 et de son erratum 1 ; aucune conversion n'est faite")


# --- valeurs ------------------------------------------------------------------------------------------------------------

def _chaine_d_une_ligne(v):
    return type(v) is str and v != "" and v == v.strip() and "\n" not in v and "\r" not in v


def _entier(v):
    return type(v) is int


def _cout(v):
    return type(v) in (int, float) and math.isfinite(v) and v >= 0


def _est_v1(ligne):
    return isinstance(ligne, dict) and (ligne.get("version") == VERSION_LIGNE_V1
                                        or ("type_ligne" not in ligne and "classe" in ligne))


def filiation_de(contenu):
    """La filiation d'une fiche passée : `null` si son champ `filiation` est « aucune », la chaîne telle quelle sinon
    (sa validité contre le registre servi est l'affaire de M1 bis, au lot 7 : ni jugée ni réparée ici)."""
    v = contenu.get(CHAMP_FILIATION) if isinstance(contenu, dict) else None
    if type(v) is not str:
        raise RegistreRefuse("fiche passée sans champ `filiation` en chaîne")
    return None if v == FILIATION_AUCUNE else v


@dataclasses.dataclass(frozen=True)
class Contexte:
    """Les listes fermées d'une génération : son numéro, les cases servies, les identifiants par rôle des modèles
    demandés (de la configuration ; jamais un nom de modèle en clair)."""

    generation: int
    cases_servies: tuple
    modeles_demandes: tuple


def contexte_de(*, generation, cases_servies, modeles_demandes):
    if not _entier(generation) or generation not in (1, 2, 3):
        raise RegistreRefuse("génération hors de 1 à 3")
    if not isinstance(cases_servies, (list, tuple)) or not cases_servies:
        raise RegistreRefuse("les cases servies de la génération sont données, en liste")
    for c in cases_servies:
        try:
            ident.rang_du_mot_de_case(c)
        except ident.MotRefuse:
            raise RegistreRefuse("case servie qui n'est pas un mot de trois syllabes") from None
    if len(set(cases_servies)) != len(cases_servies):
        raise RegistreRefuse("case servie deux fois")
    if not isinstance(modeles_demandes, (list, tuple)) or not modeles_demandes \
            or not all(_chaine_d_une_ligne(m) for m in modeles_demandes) or len(set(modeles_demandes)) != len(modeles_demandes):
        raise RegistreRefuse("les identifiants par rôle des modèles demandés : une liste de chaînes d'une ligne, distinctes")
    return Contexte(generation, tuple(cases_servies), tuple(modeles_demandes))


def _verifier_tentative(l, contexte):
    """Les champs de tentative, communs aux deux types de ligne."""
    if not _entier(l["generation"]) or l["generation"] != contexte.generation:
        raise RegistreRefuse("génération autre que celle du registre")
    if l["espece"] not in ESPECES:
        raise RegistreRefuse("espèce hors de la liste fermée")
    if l["case"] is not None and l["case"] not in contexte.cases_servies:
        raise RegistreRefuse("case hors des cases servies")
    if l["espece"] in ESPECES_PROPOSEURS and l["case"] is None:
        raise RegistreRefuse("tentative de proposeur sans case")
    if not _entier(l["rang_repli"]) or l["rang_repli"] not in RANGS_REPLI:
        raise RegistreRefuse("rang de repli hors de 0, 1, 2")
    if l["modele_demande"] not in contexte.modeles_demandes:
        raise RegistreRefuse("modèle demandé hors des identifiants par rôle")
    if not _chaine_d_une_ligne(l["raison_arret"]):
        raise RegistreRefuse("raison d'arrêt : une chaîne d'une ligne, lue dans la réponse")
    sans_reponse = l["raison_arret"] == RAISON_SANS_REPONSE
    if sans_reponse:
        if l["modele_servi"] is not None:
            raise RegistreRefuse("tentative sans réponse : modèle servi null")
        if l["classe_issue"] != CLASSE_SANS_REPONSE:
            raise RegistreRefuse("tentative sans réponse : classe « réponse illisible »")
    elif not _chaine_d_une_ligne(l["modele_servi"]):
        raise RegistreRefuse("modèle servi : une chaîne d'une ligne, lue dans la réponse ; null pour la seule tentative "
                             "sans réponse")
    if l["categorie_refus"] is not None and not _chaine_d_une_ligne(l["categorie_refus"]):
        raise RegistreRefuse("catégorie de refus : une chaîne d'une ligne, ou null")
    if not _cout(l["cout_compte_usd"]):
        raise RegistreRefuse("coût compté : un nombre fini, positif ou nul")
    if l["classe_issue"] not in CLASSES_ISSUE:
        raise RegistreRefuse("classe d'issue hors de la liste fermée")
    if l["classe_issue"] == REFUS_SERVI_PAR_REPLI and l["raison_arret"] != RAISON_REFUS:
        raise RegistreRefuse("classe de repli sans raison d'arrêt `refusal`")
    if l["raison_arret"] == RAISON_REFUS and l["classe_issue"] not in (REFUS_SERVI_PAR_REPLI, CLASSE_TROIS_REFUS):
        raise RegistreRefuse("raison d'arrêt `refusal` : classe de repli, ou « refus du modèle » après trois refus")
    if l["classe_issue"] == REFUS_SERVI_PAR_REPLI and l["rang_repli"] == RANGS_REPLI[-1]:
        raise RegistreRefuse("troisième refus : aucun repli ne le sert ; classe « refus du modèle » (arrêt n° 1)")


def verifier_ligne(ligne, contexte):
    """Une ligne complète, aux valeurs dans les listes fermées, cohérente ; lève `RegistreRefuse`, ou
    `RegistreAncienFormat` pour une ligne du v1."""
    if not isinstance(contexte, Contexte):
        raise RegistreRefuse("le contexte est construit par `contexte_de`")
    if _est_v1(ligne):
        raise RegistreAncienFormat("une ligne du registre des tentatives")
    if not isinstance(ligne, dict):
        raise RegistreRefuse("une ligne est un dictionnaire")
    cles = set(ligne) - set(CHAMPS_DU_FICHIER)
    if cles - set(CHAMPS_LIGNE):
        raise RegistreRefuse("champ hors de la liste fermée")
    if set(CHAMPS_LIGNE) - cles:
        raise RegistreRefuse("ligne incomplète : un champ de l'interface manque")
    l = ligne
    if l["type_ligne"] not in TYPES_LIGNE:
        raise RegistreRefuse("type de ligne hors de la liste fermée")
    _verifier_tentative(l, contexte)
    if l["type_ligne"] == TYPE_TENTATIVE:
        if any(l[c] is not None for c in CHAMPS_DE_FICHE):
            raise RegistreRefuse("ligne de tentative : les champs de fiche sont null")
        return ligne
    if l["classe"] not in pt.CLASSES_FICHE:
        raise RegistreRefuse("classe de fiche hors de la liste fermée")
    if l["classe_issue"] != pt.FICHES_RENDUES:
        raise RegistreRefuse("une fiche n'est rendue que par une tentative « fiches rendues »")
    if l["espece"] not in ESPECES_PROPOSEURS:
        raise RegistreRefuse("une fiche n'est rendue que par une espèce de proposeur")
    try:
        if type(l["identifiant"]) is not str:
            raise ident.MotRefuse("un mot est une chaîne")
        ident.decoder_octets(l["identifiant"], pt.OCTETS_IDENTIFIANT)
    except (ident.MotRefuse, ident.EncodageRefuse):
        raise RegistreRefuse("identifiant de fiche : un mot réencodé de dix-huit lettres") from None
    if l["classe"] == pt.PASSEE:
        if not all(type(l[c]) is str for c in ct.CHAMPS_FERMES) or l["nom"] != l["identifiant"]:
            raise RegistreRefuse("fiche passée : trois champs fermés, le nom est l'identifiant")
        if type(l["enonce"]) is not str or l["enonce"] != rg.enonce_sur_une_ligne(l["enonce"]):
            raise RegistreRefuse("fiche passée : énoncé sur une ligne")
        if l["filiation"] is not None and type(l["filiation"]) is not str:
            raise RegistreRefuse("filiation : une chaîne, ou null")
    elif any(l[c] is not None for c in ct.CHAMPS_FERMES + ("nom", "enonce", "filiation")):
        raise RegistreRefuse("fiche non passée : ni champs fermés, ni nom, ni énoncé, ni filiation")
    return ligne


# --- chaînes ------------------------------------------------------------------------------------------------------------

@dataclasses.dataclass(frozen=True)
class Tentative:
    """Une tentative relue : sa ligne `tentative` (la seule qui compte un appel et un coût) et ses lignes `fiche`."""

    ligne: dict
    fiches: tuple

    def __getitem__(self, cle):
        return self.ligne[cle]


@dataclasses.dataclass(frozen=True)
class Chaine:
    tentatives: tuple

    @property
    def derniere(self):
        return self.tentatives[-1]

    @property
    def par_repli(self):
        return len(self.tentatives) > 1

    @property
    def fin(self):
        """« servie », « sans réponse » ou « trois refus »."""
        r = self.derniere["raison_arret"]
        return "trois refus" if r == RAISON_REFUS else ("sans réponse" if r == RAISON_SANS_REPONSE else "servie")


def _champs_tentative(ligne):
    return tuple((c, ligne[c]) for c in ("generation",) + CHAMPS_TENTATIVE)


def _clore(chaine):
    """Une chaîne finie : un refus à rang < 2 a son repli ; trois refus : tous « refus du modèle » ; sinon, les refus
    qui précèdent la dernière ont la classe de repli ; une tentative « fiches rendues » a au moins une fiche."""
    for t in chaine:
        if t["classe_issue"] == pt.FICHES_RENDUES and not t.fiches:
            raise RegistreRefuse("tentative « fiches rendues » sans ligne de fiche")
    derniere = chaine[-1]
    if derniere["raison_arret"] == RAISON_REFUS:
        if derniere["rang_repli"] != RANGS_REPLI[-1]:
            raise RegistreRefuse("chaîne non close : un refus sans la tentative de repli qui le suit")
        if any(t["classe_issue"] != CLASSE_TROIS_REFUS for t in chaine):
            raise RegistreRefuse("chaîne de trois refus : classe « refus du modèle » à chaque tentative (arrêt n° 1)")
    elif any(t["classe_issue"] != REFUS_SERVI_PAR_REPLI for t in chaine[:-1]):
        raise RegistreRefuse("refus suivi d'un repli : classe « refus par classifieur, servi par repli »")
    return Chaine(tuple(chaine))


def chaines_de(lignes, contexte):
    """Vérifie chaque ligne et la suite : une ligne `tentative` par tentative ; ses lignes `fiche` la suivent, aux mêmes
    champs de tentative ; rangs 0, 1, 2 sans trou ; un repli suit un refus de la même espèce et de la même case ; chaque
    chaîne finie sous l'une des trois formes ; identifiants de fiche distincts. Rend un tuple de `Chaine`."""
    chaines, courante, identifiants = [], None, set()
    for l in lignes:
        verifier_ligne(l, contexte)
        if l["type_ligne"] == TYPE_FICHE:
            t = courante[-1] if courante else None
            if t is None or t["classe_issue"] != pt.FICHES_RENDUES or _champs_tentative(t.ligne) != _champs_tentative(l):
                raise RegistreRefuse("ligne de fiche sans la ligne de sa tentative juste avant")
            if l["identifiant"] in identifiants:
                raise RegistreRefuse("identifiant de fiche écrit deux fois")
            identifiants.add(l["identifiant"])
            courante[-1] = Tentative(t.ligne, t.fiches + (l,))
            continue
        if l["rang_repli"] == 0:
            if courante is not None:
                chaines.append(_clore(courante))
            courante = [Tentative(l, ())]
            continue
        p = courante[-1] if courante else None
        if p is None or p["raison_arret"] != RAISON_REFUS or p["rang_repli"] != l["rang_repli"] - 1 \
                or p["espece"] != l["espece"] or p["case"] != l["case"]:
            raise RegistreRefuse("repli sans le refus qui le précède dans la même chaîne")
        courante.append(Tentative(l, ()))
    if courante is not None:
        chaines.append(_clore(courante))
    return tuple(chaines)


# --- le registre --------------------------------------------------------------------------------------------------------

class RegistreTentativesV2(pt.FichierAjoutSeul):
    """Le registre des tentatives d'appel d'une génération, en ajout seul, dans le dossier de sortie."""

    CHAMPS_PERMIS = CHAMPS_LIGNE
    VERSION = VERSION_LIGNE

    def __init__(self, dossier_sortie, nom_fichier, *, generation, cases_servies, modeles_demandes):
        self.contexte = contexte_de(generation=generation, cases_servies=cases_servies, modeles_demandes=modeles_demandes)
        super().__init__(dossier_sortie, nom_fichier)
        self._lignes = []

    def ajouter(self, champs):
        raise RegistreRefuse("écriture directe d'une ligne refusée : une chaîne s'écrit par `ajouter_chaine`")

    def ajouter_fiche(self, issue):
        raise RegistreAncienFormat("appel `ajouter_fiche` d'une fiche seule, sans sa tentative")

    def _ligne(self, t, issue):
        l = {c: None for c in CHAMPS_LIGNE}
        l["type_ligne"] = TYPE_TENTATIVE if issue is None else TYPE_FICHE
        l["generation"] = self.contexte.generation
        for c in CHAMPS_TENTATIVE:
            l[c] = t[c]
        if issue is None:
            return l
        if not isinstance(issue, pt.IssueFiche):
            raise RegistreRefuse("seule une fiche classée par le portier entre au registre")
        if issue.generation != self.contexte.generation or issue.identifiant_case != t["case"]:
            raise RegistreRefuse("fiche d'une autre génération ou d'une autre case que sa tentative")
        l["identifiant"], l["classe"] = issue.identifiant, issue.classe
        if issue.classe == pt.PASSEE:
            for c in ct.CHAMPS_FERMES:
                l[c] = issue.contenu[c]
            l["nom"] = issue.identifiant
            l["enonce"] = rg.enonce_sur_une_ligne(issue.contenu["idee"])
            l["filiation"] = filiation_de(issue.contenu)
        return l

    def ajouter_chaine(self, tentatives, fiches=()):
        """Écrit une chaîne entière : `tentatives`, une à trois, chacune un dictionnaire aux champs de
        `CHAMPS_TENTATIVE` (`categorie_refus` peut manquer : `null`) ; `fiches`, les `IssueFiche` de la dernière
        tentative. Une ligne `tentative` par tentative, puis une ligne `fiche` par fiche. Tout est vérifié avant la
        première écriture ; rend les lignes écrites."""
        if not isinstance(tentatives, (list, tuple)) or not 1 <= len(tentatives) <= len(RANGS_REPLI):
            raise RegistreRefuse("une chaîne compte une à trois tentatives")
        fiches = tuple(fiches)
        prets = []
        for t in tentatives:
            if not isinstance(t, dict):
                raise RegistreRefuse("une tentative est un dictionnaire")
            if set(t) - set(CHAMPS_TENTATIVE):
                raise RegistreRefuse("champ de tentative hors de la liste fermée")
            t = dict(t)
            t.setdefault("categorie_refus", None)
            if set(CHAMPS_TENTATIVE) - set(t):
                raise RegistreRefuse("tentative incomplète : un champ de l'interface manque")
            prets.append(t)
        if fiches and prets[-1]["classe_issue"] != pt.FICHES_RENDUES:
            raise RegistreRefuse("des fiches pour une tentative qui n'est pas « fiches rendues »")
        lignes = [self._ligne(t, None) for t in prets] + [self._ligne(prets[-1], f) for f in fiches]
        avant = len(chaines_de(self._lignes, self.contexte))
        if len(chaines_de(self._lignes + lignes, self.contexte)) != avant + 1:
            raise RegistreRefuse("une chaîne commence au rang 0")
        rendues = []
        for l in lignes:
            rendues.append(super().ajouter(l))
            self._lignes.append(l)
        return rendues


def lire_registre_tentatives_v2(chemin, *, generation, cases_servies, modeles_demandes, exiger_sceau=False):
    """Relit un registre v2 : rangs et chaînage du fichier, sceau s'il est exigé, chaque ligne et la suite des chaînes ;
    refuse un registre du v1 en le disant. Rend ses lignes."""
    contexte = contexte_de(generation=generation, cases_servies=cases_servies, modeles_demandes=modeles_demandes)
    lignes = pt.relire_ajout_seul(chemin, exiger_sceau=exiger_sceau)
    for l in lignes:
        if _est_v1(l):
            raise RegistreAncienFormat("un registre des tentatives relu")
        if l.get("version") != VERSION_LIGNE:
            raise RegistreRefuse("version de ligne inconnue")
    chaines_de(lignes, contexte)
    return lignes


# --- comptes : les fiches sur les lignes `fiche`, les appels sur les lignes `tentative` -----------------------------------

def _relues(lignes):
    for l in lignes:
        if _est_v1(l):
            raise RegistreAncienFormat("une ligne donnée au lot 5 v2")
        if not isinstance(l, dict) or l.get("version") != VERSION_LIGNE or set(CHAMPS_LIGNE) - set(l) \
                or l["type_ligne"] not in TYPES_LIGNE:
            raise RegistreRefuse("ligne qui n'est pas une ligne relue du registre v2")
    return lignes


def lignes_fiche(lignes):
    """Les seules lignes `fiche` (erratum, point 4)."""
    return [l for l in _relues(lignes) if l["type_ligne"] == TYPE_FICHE]


def lignes_tentative(lignes):
    """Les seules lignes `tentative` : un appel, un coût, chacune une fois."""
    return [l for l in _relues(lignes) if l["type_ligne"] == TYPE_TENTATIVE]


def lignes_v1_de(lignes):
    """Les lignes `fiche`, ramenées à la forme du lot 5 v1 (registre servi, garde du coffre)."""
    rendu = []
    for l in lignes_fiche(lignes):
        v1 = {"identifiant": l["identifiant"], "generation": l["generation"], "case": l["case"], "classe": l["classe"]}
        if l["classe"] == pt.PASSEE:
            for c in ct.CHAMPS_FERMES + ("nom", "enonce"):
                v1[c] = l[c]
        rendu.append(v1)
    return rendu


def fabriquer_registre_servi_v2(lignes, cases_servies, generation, *, permuter_comptes, racine=tn.RACINE_ECRITE,
                                racine_attendue=tn.RACINE_ECRITE):
    """Le registre servi des générations 2 et 3, par le code du v1, sur les lignes `fiche` des registres v2 relus."""
    return rg.fabriquer_registre_servi(lignes_v1_de(lignes), cases_servies, generation, permuter_comptes=permuter_comptes,
                                       racine=racine, racine_attendue=racine_attendue)


def garde_du_coffre_v2(lignes, generation):
    """Arrêt n° 5, par le code du v1, sur les seules lignes `fiche` (fiches servies par repli comprises, P8) : le
    dénominateur ne compte jamais une ligne `tentative`."""
    return rg.garde_du_coffre(lignes_v1_de(lignes), generation)


__all__ = ["RegistreTentativesV2", "RegistreRefuse", "RegistreAncienFormat", "Contexte", "contexte_de", "verifier_ligne",
           "Tentative", "Chaine", "chaines_de", "lire_registre_tentatives_v2", "lignes_fiche", "lignes_tentative",
           "lignes_v1_de", "filiation_de", "fabriquer_registre_servi_v2", "garde_du_coffre_v2", "CHAMPS_LIGNE",
           "CHAMPS_TENTATIVE", "TYPES_LIGNE", "ESPECES", "ESPECES_PROPOSEURS", "CLASSES_ISSUE", "REFUS_SERVI_PAR_REPLI",
           "RAISON_REFUS", "RAISON_SANS_REPONSE", "CLASSE_TROIS_REFUS", "VERSION", "VERSION_LIGNE"]
