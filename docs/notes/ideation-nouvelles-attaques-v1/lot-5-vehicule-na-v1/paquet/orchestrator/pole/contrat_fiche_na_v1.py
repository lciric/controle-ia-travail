"""Véhicule NA-1, lot 5 — validateur neuf du contrat d'une fiche (`contrat_fiche_na_v1`), sans caviardage ; comparaison
« hors case » à l'octet (arrêt n° 4) ; champ `case` comparé à l'identifiant servi.

Lettre : V9 (`864f39a7…`), l. 75 (le portier compare les champs fermés à ces chaînes), l. 110 (« autre, à nommer »),
l. 148 (classes d'issue), l. 375 (arrêt n° 4) ; conception du véhicule v5 (`1b7f6822…`), § 0 bis (D13, 07:10Z ; 07:21Z,
règle 1 ; 07:46Z, mot 2), § 2.4 (validateur neuf : présence, type de chaîne, borne en octets ; tout champ en plus ; aucun
caviardage avant la classification ; garde « hors case »), § 5.4, § 6.2 (champ `case` et validateur neuf ; fiche hors
contrat de longueur ; case « autre, à nommer ») ; relevé du lot 0 (`10ac79ec…`), Q6.

- **Présence** : tenue par le lecteur (`lecteur_fiches_na_v1`), qui ne reconnaît une fiche qu'avec les douze noms.
- **Type** : chaque valeur des douze est une chaîne ; sinon la fiche est hors contrat (cause « champ qui n'est pas une
  chaîne »), donc « au coffre » par le programme de forme. *La lettre ne nomme pas ce cas ; il est rangé avec les fiches
  hors contrat (D13), en remarque au rapport.*
- **Borne en octets** (D13) : chaque valeur, encodée en UTF-8, au plus à sa borne ; un octet de plus, la fiche est « hors
  contrat de longueur » : traitée comme illisible, donc « au coffre », comptée, **jamais réparée** (aucune coupe). Les bornes
  sont une valeur de l'additif, sur la mesure ; ce module les reçoit, une par champ, les douze exactement.
- **Champ en plus** : il envoie la fiche au coffre.
- **Hors case** (arrêt n° 4) : les trois champs fermés comparés **à l'octet** (UTF-8) aux trois chaînes de la ligne de case,
  sur le texte rendu, sans normalisation. À la case « autre, à nommer », la valeur attendue du champ fermé est cette chaîne
  même : la règle n'a rien de particulier, la ligne de case la porte.
- **Champ `case`** (07:46Z, mot 2) : comparé à l'identifiant servi ; une différence est consignée et comptée à part ; elle
  ne change pas la classe.

Aucun caviardage, aucune normalisation, aucune réparation : ce module ne modifie rien de ce qu'il lit. Aucun message
d'erreur ne recopie une valeur. Bibliothèque standard, et les modules des lots 1, 3 et 5.
"""

import dataclasses

from pole import lecteur_fiches_na_v1 as lf
from pole import requete_na_v3 as rq
from pole import tirage_na_v4 as tn

VERSION = "contrat-fiche-na-v1"
CHAMPS = rq.CHAMPS_FICHE
CHAMPS_FERMES = ("ce_que_le_moniteur_suppose", "menace_du_programme", "etage_de_lecture")
CHAMP_CASE = "case"
CAUSE_CHAMP_EN_PLUS = "champ en plus"
CAUSE_TYPE = "champ qui n'est pas une chaîne"
CAUSE_LONGUEUR = "hors contrat de longueur"
ORDRE_DES_CAUSES = (CAUSE_CHAMP_EN_PLUS, CAUSE_TYPE, CAUSE_LONGUEUR)


class ContratRefuse(ValueError):
    """Une entrée que le validateur ne lit pas (bornes mal formées, objet d'un autre type) ; rien n'est réparé."""


@dataclasses.dataclass(frozen=True)
class BornesFiche:
    """Une borne en octets par champ, les douze exactement, entiers strictement positifs (valeurs de l'additif)."""

    bornes: tuple  # ((nom, octets), …), dans l'ordre du contrat
    statut: str = "non dit"

    def borne(self, nom):
        return dict(self.bornes)[nom]


def bornes_de(dictionnaire, statut):
    """Construit les bornes depuis un dictionnaire {champ: octets} ; refuse un champ manquant, en plus, ou mal chiffré.
    `statut` dit d'où viennent les valeurs (« brouillon d'essai factice » tant que l'additif n'est pas scellé)."""
    if not isinstance(dictionnaire, dict) or set(dictionnaire) != set(CHAMPS):
        raise ContratRefuse("bornes : les douze champs du contrat, exactement")
    for nom in CHAMPS:
        v = dictionnaire[nom]
        if type(v) is not int or v <= 0:
            raise ContratRefuse("bornes : un entier strictement positif par champ")
    if type(statut) is not str or not statut:
        raise ContratRefuse("bornes : leur statut est dit")
    return BornesFiche(tuple((c, dictionnaire[c]) for c in CHAMPS), statut)


@dataclasses.dataclass(frozen=True)
class VerdictContrat:
    """Le verdict du programme de forme : au contrat, ou la liste de ce qui l'en sort (noms seuls, aucune valeur)."""

    au_contrat: bool
    champs_en_plus: tuple
    types_faux: tuple
    hors_longueur: tuple

    @property
    def cause(self):
        """La première cause, dans l'ordre fixe : champ en plus, type, longueur ; None au contrat."""
        if self.champs_en_plus:
            return CAUSE_CHAMP_EN_PLUS
        if self.types_faux:
            return CAUSE_TYPE
        if self.hors_longueur:
            return CAUSE_LONGUEUR
        return None


def verifier(fiche, bornes):
    """Le programme de forme (étape (i) du portier) : type de chaîne, borne en octets, champ en plus."""
    if not isinstance(fiche, lf.FicheLue):
        raise ContratRefuse("seule une fiche lue par `lecteur_fiches_na_v1` se vérifie")
    if not isinstance(bornes, BornesFiche):
        raise ContratRefuse("les bornes sont construites par `bornes_de`")
    contenu = fiche.contenu()
    types_faux = tuple(c for c in CHAMPS if type(contenu[c]) is not str)
    hors = tuple(c for c in CHAMPS if type(contenu[c]) is str and len(contenu[c].encode("utf-8")) > bornes.borne(c))
    en_plus = tuple(fiche.extras)
    return VerdictContrat(not (en_plus or types_faux or hors), en_plus, types_faux, hors)


def valeurs_de_la_case(case):
    """Les trois chaînes de la ligne de case, dans l'ordre des axes (forme du lot 1 : `case : id ; v1 ; v2 ; v3`)."""
    if not isinstance(case, rq.CaseServie):
        raise ContratRefuse("la case est une case du tirage (`requete_na_v3.CaseServie`)")
    ligne = case.ligne
    if type(ligne) is not str or not ligne.startswith(tn.PREFIXE_LIGNE):
        raise ContratRefuse("ligne de case mal formée")
    parts = ligne[len(tn.PREFIXE_LIGNE):].split(tn.SEPARATEUR_LIGNE)
    if len(parts) != 4 or parts[0] != case.identifiant:
        raise ContratRefuse("ligne de case mal formée")
    return tuple(parts[1:])


def champs_fermes_differents(contenu, case):
    """Arrêt n° 4 : les champs fermés dont la valeur diffère **à l'octet** de la chaîne de la ligne de case."""
    attendues = valeurs_de_la_case(case)
    rendu = []
    for nom, attendue in zip(CHAMPS_FERMES, attendues):
        v = contenu.get(nom)
        if type(v) is not str or v.encode("utf-8") != attendue.encode("utf-8"):
            rendu.append(nom)
    return tuple(rendu)


def case_differe(contenu, identifiant_case):
    """07:46Z, mot 2 : vrai si le champ `case` diffère de l'identifiant servi (consigné, compté, classe inchangée)."""
    v = contenu.get(CHAMP_CASE)
    return type(v) is not str or v.encode("utf-8") != identifiant_case.encode("utf-8")
