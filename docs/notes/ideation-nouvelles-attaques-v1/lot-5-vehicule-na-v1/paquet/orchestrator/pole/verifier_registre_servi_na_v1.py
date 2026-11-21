"""Véhicule NA-1, lot 5 — vérification du registre servi, avant tout envoi (`verifier_registre_servi_na_v1`) : arrêts
n° 8, n° 9 et n° 19.

Lettre : V9 (`864f39a7…`), l. 63, l. 120 (garde-fou 3), l. 379 (arrêt n° 8), l. 380 (arrêt n° 9), l. 390 (arrêt n° 19) ;
conception du véhicule v5 (`1b7f6822…`), § 2.6 (vérification, avant tout envoi, sur le fichier entier), § 2.14 et § 2.15
(la forme de l'arrêt n° 19 sert aussi au chargement de la colonne « matière première », lot 10 a : `verifier_enonce`),
§ 6.1 (arrêts n° 8, n° 9, n° 19).

Le programme lit le **fichier entier**, à la forme de `registre_na_v1` (brouillon d'essai), et rend « conforme », ou lève
`RegistreServiNonConforme` avec **tous** les défauts trouvés (numéro d'arrêt, rang de ligne, cause ; jamais un contenu).
**Aucune ligne n'est retirée** : un défaut, la génération ne part pas. Les arrêts s'ajoutent les uns aux autres (l'arrêt
n° 19 s'ajoute aux arrêts n° 9 et n° 16, sans les remplacer ; l'arrêt n° 16 est au point d'envoi, lot 4).

- **Arrêt n° 8** : le registre plus long que sa borne en octets.
- **Arrêt n° 9** : une ligne qui porte une étiquette interdite : note, rang, verdict de juge, étiquette d'antériorité,
  coût (motifs ci-dessous, sur la ligne brute et sur chaque champ lu).
- **Arrêt n° 19** : une ligne d'une autre forme ; un champ de plus ; une classe autre que « passée » sur une ligne de
  tentative ; deux lignes pour une tentative ou pour un compte ; un énoncé sur plusieurs lignes, ou au-dessus de sa borne ;
  une marque de code, d'étape numérotée ou de consigne ; et, si l'appelant donne ce qu'il attend, une ligne manquante ou
  inattendue.

**Les listes de marques et d'étiquettes ci-dessous sont un brouillon d'essai** (valeurs du développeur) ; la lettre en
nomme les sortes, non les motifs ; elles sont à fixer à l'additif, et leur taux de faux refus à mesurer à l'essai à blanc.
Bibliothèque standard, et les modules des lots 1 et 5.
"""

import dataclasses
import json
import re

from pole import identifiants_na_v1 as ident
from pole import portier_na_v1 as pt
from pole import registre_na_v1 as rg

VERSION = "verifier-registre-servi-na-v1"
STATUT_DES_LISTES = "brouillon d'essai, valeurs du développeur, à fixer à l'additif"
ARRET_TAILLE, ARRET_ETIQUETTE, ARRET_NON_CONFORME = 8, 9, 19

# Arrêt n° 9 : les cinq étiquettes interdites (V9, l. 380), en motifs (brouillon).
ETIQUETTES_INTERDITES = (
    ("note", re.compile(r"(?i)(?<!\w)note\s*[:=]")),
    ("rang", re.compile(r"(?i)(?<!\w)rang\s*[:=]")),
    ("verdict de juge", re.compile(r"(?i)(?<!\w)verdict(?:\s+de\s+juge)?\s*[:=]")),
    ("étiquette d'antériorité", re.compile(r"(?i)(?<!\w)(?:aucune\s+)?antériorité\s+(?:trouvée|partielle)|(?<!\w)non\s+"
                                           r"tranchée(?!\w)|(?<!\w)antériorité\s*[:=]")),
    ("coût", re.compile(r"(?i)(?<!\w)(?:coût|cout|prix)\s*[:=]|\d(?:[.,]\d+)?\s*(?:usd|dollars?|\$)(?!\w)|\$\s*\d")),
)
# Arrêt n° 19 : marques de code, d'étape numérotée, de consigne (brouillon).
MARQUES_DE_CODE = re.compile(r"[`{}\\]|#!|\$\(|=>|&&|\|\||</|/>|\);|(?<!\w)(?:def|import|lambda|return)\s")
MARQUES_D_ETAPE = re.compile(r"(?i)(?:^|\s)\d{1,3}\s*[.)](?:\s|$)|(?<!\w)(?:étape|step)\s*\d|(?<!\w)(?:premièrement|"
                             r"deuxièmement|troisièmement)(?!\w)")
MARQUES_DE_CONSIGNE = re.compile(r"(?i)(?<!\w)(?:ignore[rz]?|tu\s+dois|vous\s+devez|you\s+must|réponds|répondez|"
                                 r"instructions?|consignes?|system\s*:|assistant\s*:|user\s*:)(?!\w)")
_ENTIER = re.compile(r"^(?:0|[1-9][0-9]*)$")


@dataclasses.dataclass(frozen=True)
class Defaut:
    numero: int
    rang: object  # rang de ligne (1, 2, …), ou None pour le fichier entier
    cause: str


class RegistreServiNonConforme(RuntimeError):
    """Le registre servi n'est pas conforme : la génération ne part pas ; aucune ligne n'est retirée."""

    def __init__(self, defauts):
        self.defauts = tuple(defauts)
        self.numeros = tuple(sorted({d.numero for d in self.defauts}))
        super().__init__(f"registre servi non conforme : arrêts n° {', '.join(str(n) for n in self.numeros)} ; "
                         f"{len(self.defauts)} défaut(s) ; la génération ne part pas ; aucune ligne n'est retirée")


@dataclasses.dataclass(frozen=True)
class ConstatConforme:
    taille: int
    lignes: int
    lignes_tentative: int
    lignes_compte: int


def _sur_une_ligne(t):
    return len(t.splitlines()) <= 1 and t == t.strip("\r\n\x0b\x0c\x1c\x1d\x1e\x85  ") and "\r" not in t \
        and "\n" not in t


def verifier_enonce(enonce, borne_octets):
    """La forme de l'arrêt n° 19 pour un énoncé : une ligne, sous sa borne, aucune marque de code, d'étape numérotée ni de
    consigne ; et l'arrêt n° 9 (étiquettes interdites). Rend la liste des défauts (numéro, cause), vide si conforme.
    Sert aussi au lot 10 a (chargement de la colonne)."""
    if type(borne_octets) is not int or borne_octets <= 0:
        raise ValueError("borne de l'énoncé : un entier positif")
    if type(enonce) is not str:
        return [(ARRET_NON_CONFORME, "énoncé qui n'est pas une chaîne")]
    d = []
    if not _sur_une_ligne(enonce):
        d.append((ARRET_NON_CONFORME, "énoncé sur plusieurs lignes"))
    if len(enonce.encode("utf-8")) > borne_octets:
        d.append((ARRET_NON_CONFORME, "énoncé au-dessus de sa borne"))
    d.extend(_marques(enonce))
    return d


def _marques(texte):
    d = []
    if MARQUES_DE_CODE.search(texte):
        d.append((ARRET_NON_CONFORME, "marque de code"))
    if MARQUES_D_ETAPE.search(texte):
        d.append((ARRET_NON_CONFORME, "marque d'étape numérotée"))
    if MARQUES_DE_CONSIGNE.search(texte):
        d.append((ARRET_NON_CONFORME, "marque de consigne"))
    d.extend(_etiquettes(texte))
    return d


def _etiquettes(texte):
    return [(ARRET_ETIQUETTE, f"étiquette interdite : {nom}") for nom, m in ETIQUETTES_INTERDITES if m.search(texte)]


def _lire_tentative(reste):
    """Rend (nom, fermes, enonce) ou une cause."""
    parts = reste.split(rg.SEPARATEUR, 5)
    if len(parts) != 6:
        return "ligne de tentative : champs manquants"
    nom, f1, f2, f3, classe, brut = parts
    if classe != pt.PASSEE:
        return "ligne de tentative : classe autre que « passée », ou champ de plus"
    try:
        enonce, fin = json.JSONDecoder().raw_decode(brut)
    except ValueError:
        return "ligne de tentative : énoncé mal formé, ou champ de plus"
    if fin != len(brut) or type(enonce) is not str:
        return "ligne de tentative : champ de plus après l'énoncé"
    return nom, (f1, f2, f3), enonce


def verifier_registre_servi(octets, *, borne_registre_octets, borne_enonce_octets, noms_attendus=None,
                            cases_attendues=None):
    """Vérifie le fichier entier du registre servi ; rend `ConstatConforme`, ou lève `RegistreServiNonConforme` avec tous
    les défauts. `noms_attendus` (les tentatives passées) et `cases_attendues` (les cases servies), s'ils sont donnés,
    font refuser une ligne manquante ou inattendue."""
    if not isinstance(octets, (bytes, bytearray)):
        raise TypeError("le registre servi se vérifie en octets")
    if type(borne_registre_octets) is not int or borne_registre_octets <= 0:
        raise ValueError("borne du registre : un entier positif")
    octets = bytes(octets)
    defauts = []
    if len(octets) > borne_registre_octets:
        defauts.append(Defaut(ARRET_TAILLE, None, "registre plus long que sa borne"))
    try:
        texte = octets.decode("utf-8")
    except UnicodeDecodeError:
        raise RegistreServiNonConforme(defauts + [Defaut(ARRET_NON_CONFORME, None, "registre qui n'est pas en UTF-8")]) \
            from None
    if texte and not texte.endswith("\n"):
        defauts.append(Defaut(ARRET_NON_CONFORME, None, "registre sans fin de ligne finale"))
    lignes = texte.split("\n")
    if lignes and lignes[-1] == "":
        lignes = lignes[:-1]
    noms, comptes, n_t, n_c = {}, {}, 0, 0
    for i, ligne in enumerate(lignes, start=1):
        for num, cause in _etiquettes(ligne):
            defauts.append(Defaut(num, i, cause))
        if ligne == "":
            defauts.append(Defaut(ARRET_NON_CONFORME, i, "ligne vide"))
            continue
        if "\r" in ligne or len(ligne.splitlines()) != 1:
            defauts.append(Defaut(ARRET_NON_CONFORME, i, "ligne coupée en deux"))
        if ligne.startswith(rg.TETE_TENTATIVE):
            lu = _lire_tentative(ligne[len(rg.TETE_TENTATIVE):])
            if isinstance(lu, str):
                defauts.append(Defaut(ARRET_NON_CONFORME, i, lu))
                continue
            nom, fermes, enonce = lu
            n_t += 1
            try:
                ident.decoder_octets(nom, pt.OCTETS_IDENTIFIANT)
            except (ident.MotRefuse, ident.EncodageRefuse):
                defauts.append(Defaut(ARRET_NON_CONFORME, i, "nom qui n'est pas un identifiant réencodé"))
            if nom in noms:
                defauts.append(Defaut(ARRET_NON_CONFORME, i, "deux lignes pour une tentative"))
            noms.setdefault(nom, i)
            for v in (nom, *fermes):
                if v == "" or v != v.strip():
                    defauts.append(Defaut(ARRET_NON_CONFORME, i, "champ fermé vide ou entouré de blancs"))
                for num, cause in _marques(v):
                    if num != ARRET_ETIQUETTE:
                        defauts.append(Defaut(num, i, cause))
            for num, cause in verifier_enonce(enonce, borne_enonce_octets):
                if num != ARRET_ETIQUETTE or not any(d.rang == i and d.cause == cause for d in defauts):
                    defauts.append(Defaut(num, i, cause))
        elif ligne.startswith(rg.TETE_COMPTE):
            parts = ligne[len(rg.TETE_COMPTE):].split(rg.SEPARATEUR)
            if len(parts) != 3:
                defauts.append(Defaut(ARRET_NON_CONFORME, i, "ligne de compte : champs manquants ou en plus"))
                continue
            case, classe, n = parts
            n_c += 1
            try:
                ident.rang_du_mot_de_case(case)
            except ident.MotRefuse:
                defauts.append(Defaut(ARRET_NON_CONFORME, i, "ligne de compte : identifiant de case mal formé"))
            if classe not in rg.CLASSES_COMPTEES:
                defauts.append(Defaut(ARRET_NON_CONFORME, i, "ligne de compte : classe qui n'est pas comptée"))
            if _ENTIER.match(n) is None:
                defauts.append(Defaut(ARRET_NON_CONFORME, i, "ligne de compte : compte qui n'est pas un entier"))
            if (case, classe) in comptes:
                defauts.append(Defaut(ARRET_NON_CONFORME, i, "deux lignes de compte pour une case et une classe"))
            comptes.setdefault((case, classe), i)
        else:
            defauts.append(Defaut(ARRET_NON_CONFORME, i, "ligne d'une autre forme"))
    if noms_attendus is not None:
        attendus = set(noms_attendus)
        if set(noms) - attendus:
            defauts.append(Defaut(ARRET_NON_CONFORME, None, "tentative inattendue"))
        if attendus - set(noms):
            defauts.append(Defaut(ARRET_NON_CONFORME, None, "tentative manquante"))
    if cases_attendues is not None:
        attendues = {(c, k) for c in cases_attendues for k in rg.CLASSES_COMPTEES}
        if set(comptes) - attendues:
            defauts.append(Defaut(ARRET_NON_CONFORME, None, "ligne de compte inattendue"))
        if attendues - set(comptes):
            defauts.append(Defaut(ARRET_NON_CONFORME, None, "ligne de compte manquante"))
    if defauts:
        raise RegistreServiNonConforme(defauts)
    return ConstatConforme(len(octets), len(lignes), n_t, n_c)
