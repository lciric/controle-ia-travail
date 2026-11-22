"""Véhicule NA-1, lot 5 v3 — registre des tentatives d'appel, aux champs de l'interface commune des lots 5, 6 et 7 et de
ses errata 1 et 2 (`registre_na_v3`) ; registre servi marqué `par_repli`.

Lettre : interface commune (`interface-lots-5-6-7-repli-v1.md`, « à implanter telle quelle ») ; erratum 1
(`erratum-1-interface-lots-5-6-7-repli-v1.md` : trois refus, rôle non proposeur servi par repli, tentative sans réponse,
champ fermé `type_ligne`) ; **erratum 2** (`erratum-2-interface-lots-5-6-7-repli-v1.md`, décisions de la mère : (a) classe
« refus » aux trois tentatives d'une chaîne de trois refus ; (b) refus puis tentative sans réponse : classe de défaut
« sans réponse », jamais « servi par repli » ; (d) fiches servies par repli au registre servi, **marquées** `par_repli`,
décision de fond provisoire) ; projet d'additif v2, § 5 ; V9, l. 63, l. 92 à 101, l. 152 à 154, l. 160 ; conception v5,
§ 2.6 (écart (c), déclaré à l'additif). Les lots 5 v1 et 5 v2 ne sont pas modifiés ; ce module remplace le v2.

**Une ligne** porte `type_ligne`, les champs du lot 5 v1 et ceux de l'interface, **tous présents** ; `null` si sans objet.
Deux types : `tentative` (une par tentative, la seule qui compte un appel et un coût) et `fiche` (une fiche rendue par la
tentative qui la précède, dont elle recopie les champs). **Tout compte de fiches ne lit que les lignes `fiche`.**

**Une chaîne** : une à trois tentatives, rangs 0, 1, 2, chacune refusée par un classifieur (`refusal`) sauf la dernière.
Trois fins, et la classe des refus qui précèdent la dernière :
- *servie* : « refus par classifieur, servi par repli » ; la dernière, la classe de sa réponse (rôle non proposeur : la
  classe de son rôle) ;
- *sans réponse* (erratum 1, point 3 ; **erratum 2, (b)**) : la dernière a `modele_servi` à `null`, `sans_reponse` et la
  classe de défaut de l'appel sans réponse (« réponse illisible », V9 l. 99) ; **les refus qui la précèdent prennent cette
  même classe de défaut, jamais la classe de repli**, puisque rien n'a été servi ;
- *trois refus* (erratum 1, point 1 ; erratum 2, (a)) : la classe « refus du modèle » aux trois ; aucune fiche ; arrêt n° 1.
Une chaîne s'écrit en un appel (`ajouter_chaine`), vérifiée entière avant toute écriture.

**Refusé** (`RegistreRefuse`, rien n'est écrit, rien n'est réparé, aucune valeur devinée) : champ manquant ou en plus ;
valeur hors des listes fermées ; chaîne qui ne tient aucune des trois formes. **Seul `categorie_refus` prend `null` quand
elle manque.** **Ancien format** (`RegistreAncienFormat`) : une ligne du lot 5 v1 ou du lot 5 v2, l'appel `ajouter_fiche`
du v1, l'écriture directe d'un dictionnaire ; le message le dit.

**Registre servi** (`fabriquer_registre_servi_v3`) : celui du v1, sur les seules lignes `fiche`, même ordre, mêmes lignes de
compte, **plus un champ fermé `par_repli` sur chaque ligne de tentative passée** (erratum 2, (d)) : `par_repli : vrai` pour
une fiche rendue par une tentative de rang 1 ou 2, `par_repli : faux` sinon, placé entre la classe et l'énoncé :
`tentative : <nom> ; <fermé 1> ; <fermé 2> ; <fermé 3> ; passée ; par_repli : vrai|faux ; <énoncé en chaîne JSON>`.
Retirer ce champ rend le registre servi du v1, octet pour octet. La vérification est `verifier_registre_servi_na_v3`.
**Garde du coffre** : celle du v1, sur les seules lignes `fiche` (fiches servies par repli comprises, P8).

Aucun message d'erreur ne recopie une valeur. Bibliothèque standard, et les modules des lots 1 et 5 v1.
"""

import dataclasses
import hashlib
import math

from pole import contrat_fiche_na_v1 as ct
from pole import identifiants_na_v1 as ident
from pole import portier_na_v1 as pt
from pole import registre_na_v1 as rg
from pole import tirage_na_v4 as tn

VERSION = "registre-na-v3"
VERSION_LIGNE = "registre-tentatives-na-v3"
VERSION_LIGNE_V1 = rg.RegistreTentatives.VERSION
VERSION_LIGNE_V2 = "registre-tentatives-na-v2"
MARQUE_PAR_REPLI = "par_repli : "
PAR_REPLI = {True: "par_repli : vrai", False: "par_repli : faux"}

TYPE_TENTATIVE, TYPE_FICHE = "tentative", "fiche"
TYPES_LIGNE = (TYPE_TENTATIVE, TYPE_FICHE)
ESPECES_PROPOSEURS = ("espece-1", "espece-2", "espece-3", "espece-4", "espece-5")
ESPECES = ESPECES_PROPOSEURS + ("aiguilleur", "portier", "juge-1", "juge-2", "passe-x")
RANGS_REPLI = (0, 1, 2)
RAISON_REFUS = "refusal"
RAISON_SANS_REPONSE = "sans_reponse"
REFUS_SERVI_PAR_REPLI = "refus par classifieur, servi par repli"
CLASSE_TROIS_REFUS = pt.REFUS_DU_MODELE      # erratum, point 1 : « la classe « refus » de la v9 »
CLASSE_SANS_REPONSE = pt.ILLISIBLE           # erratum 1, point 3 ; erratum 2, (b) : la classe de défaut (V9, l. 99)
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
    """Un registre, une ligne ou un appel au format du lot 5 v1 ou du lot 5 v2, donné au lot 5 v3."""

    def __init__(self, ou):
        super().__init__(f"ancien format (lot 5 v1, `{VERSION_LIGNE_V1}`, ou lot 5 v2, `{VERSION_LIGNE_V2}`) : {ou} ; "
                         f"le lot 5 v3 exige chaque ligne au format `{VERSION_LIGNE}`, avec `type_ligne` et les champs de "
                         "l'interface des lots 5, 6 et 7 et de ses errata 1 et 2 ; aucune conversion n'est faite")


# --- valeurs ------------------------------------------------------------------------------------------------------------

def _chaine_d_une_ligne(v):
    return type(v) is str and v != "" and v == v.strip() and "\n" not in v and "\r" not in v


def _entier(v):
    return type(v) is int


def _cout(v):
    return type(v) in (int, float) and math.isfinite(v) and v >= 0


def _est_v1(ligne):
    return isinstance(ligne, dict) and (ligne.get("version") in (VERSION_LIGNE_V1, VERSION_LIGNE_V2)
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
    if l["raison_arret"] == RAISON_REFUS and l["classe_issue"] not in (REFUS_SERVI_PAR_REPLI, CLASSE_TROIS_REFUS,
                                                                       CLASSE_SANS_REPONSE):
        raise RegistreRefuse("raison d'arrêt `refusal` : classe de repli, « refus du modèle » après trois refus, ou la "
                             "classe de défaut avant une tentative sans réponse")
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
    elif derniere["raison_arret"] == RAISON_SANS_REPONSE:
        if any(t["classe_issue"] != CLASSE_SANS_REPONSE for t in chaine[:-1]):
            raise RegistreRefuse("refus suivi d'une tentative sans réponse : classe de défaut, jamais « servi par repli »")
    elif any(t["classe_issue"] != REFUS_SERVI_PAR_REPLI for t in chaine[:-1]):
        raise RegistreRefuse("refus suivi d'un repli servi : classe « refus par classifieur, servi par repli »")
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

class RegistreTentativesV3(pt.FichierAjoutSeul):
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


def lire_registre_tentatives_v3(chemin, *, generation, cases_servies, modeles_demandes, exiger_sceau=False):
    """Relit un registre v3 : rangs et chaînage du fichier, sceau s'il est exigé, chaque ligne et la suite des chaînes ;
    refuse un registre du v1 ou du v2 en le disant. Rend ses lignes."""
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
            raise RegistreAncienFormat("une ligne donnée au lot 5 v3")
        if not isinstance(l, dict) or l.get("version") != VERSION_LIGNE or set(CHAMPS_LIGNE) - set(l) \
                or l["type_ligne"] not in TYPES_LIGNE:
            raise RegistreRefuse("ligne qui n'est pas une ligne relue du registre v3")
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


def _marquer(ligne_v1, par_repli):
    """Insère le champ `par_repli` entre la classe et l'énoncé d'une ligne de tentative du v1."""
    parts = ligne_v1[len(rg.TETE_TENTATIVE):].split(rg.SEPARATEUR, 5)
    if len(parts) != 6 or parts[4] != pt.PASSEE:
        raise RegistreRefuse("ligne de tentative du registre servi mal formée")
    nom = parts[0]
    if nom not in par_repli:
        raise RegistreRefuse("ligne de tentative du registre servi sans fiche relue")
    return rg.TETE_TENTATIVE + rg.SEPARATEUR.join(parts[:5] + [PAR_REPLI[par_repli[nom]], parts[5]])


def fabriquer_registre_servi_v3(lignes, cases_servies, generation, *, permuter_comptes, racine=tn.RACINE_ECRITE,
                                racine_attendue=tn.RACINE_ECRITE):
    """Le registre servi des générations 2 et 3 : celui du v1 sur les lignes `fiche` (même ordre, mêmes comptes), chaque
    ligne de tentative marquée `par_repli` (erratum 2, (d)). Rend un `registre_na_v1.RegistreServi`."""
    fiches = lignes_fiche(lignes)
    par_repli = {l["identifiant"]: l["rang_repli"] > 0 for l in fiches if l["classe"] == pt.PASSEE}
    v1 = rg.fabriquer_registre_servi(lignes_v1_de(lignes), cases_servies, generation, permuter_comptes=permuter_comptes,
                                     racine=racine, racine_attendue=racine_attendue)
    if not v1.octets:
        return v1
    sortie = [_marquer(t, par_repli) if t.startswith(rg.TETE_TENTATIVE) else t
              for t in v1.octets.decode("utf-8").split("\n")[:-1]]
    octets = ("\n".join(sortie) + "\n").encode("utf-8")
    return dataclasses.replace(v1, octets=octets, sha256=hashlib.sha256(octets).hexdigest(), taille=len(octets))


def marques_par_repli(registre_servi):
    """Les noms des tentatives du registre servi marquées `par_repli : vrai` (pour une lecture qui les retire après
    coup)."""
    noms = []
    for t in registre_servi.octets.decode("utf-8").split("\n"):
        if t.startswith(rg.TETE_TENTATIVE):
            parts = t[len(rg.TETE_TENTATIVE):].split(rg.SEPARATEUR, 6)
            if len(parts) == 7 and parts[5] == PAR_REPLI[True]:
                noms.append(parts[0])
    return tuple(noms)


def garde_du_coffre_v3(lignes, generation):
    """Arrêt n° 5, par le code du v1, sur les seules lignes `fiche` (fiches servies par repli comprises, P8) : le
    dénominateur ne compte jamais une ligne `tentative`."""
    return rg.garde_du_coffre(lignes_v1_de(lignes), generation)


__all__ = ["RegistreTentativesV3", "RegistreRefuse", "RegistreAncienFormat", "Contexte", "contexte_de", "verifier_ligne",
           "Tentative", "Chaine", "chaines_de", "lire_registre_tentatives_v3", "lignes_fiche", "lignes_tentative",
           "lignes_v1_de", "filiation_de", "fabriquer_registre_servi_v3", "garde_du_coffre_v3", "marques_par_repli", "CHAMPS_LIGNE",
           "CHAMPS_TENTATIVE", "TYPES_LIGNE", "ESPECES", "ESPECES_PROPOSEURS", "CLASSES_ISSUE", "REFUS_SERVI_PAR_REPLI",
           "RAISON_REFUS", "RAISON_SANS_REPONSE", "CLASSE_TROIS_REFUS", "VERSION", "VERSION_LIGNE", "PAR_REPLI"]
