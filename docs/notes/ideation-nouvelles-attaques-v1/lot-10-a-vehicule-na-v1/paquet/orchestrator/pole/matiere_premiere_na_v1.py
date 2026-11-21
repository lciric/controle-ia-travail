"""Véhicule NA-1, lot 10 a — colonne « matière première » : chargement et garde (`matiere_premiere_na_v1`).

Lettre : conception du véhicule v5 (`1b7f6822…`), § 0 bis (mots de 08:00Z, 2 et 3 ; 07:51Z), § 2.14 (interrupteur à trois
états, règle d'allumage, chargement en « garde seule », garde de la colonne, taux de faux refus), § 6.2 (trois lignes du
lot 10 a), § 7 (lot 10 a) ; contrôle de la conception v5 (`4b369004…`), point 4 (sixième ligne de la pièce de relevés) ;
V9 (`864f39a7…`), l. 83, l. 385 (arrêt n° 14), l. 387 (normalisation), l. 390 (forme de l'arrêt n° 19) ; erratum 1 du
mandat du lot 10 a (`61674e25…`), points E4 (manifeste de la lecture de fin) et E5 (identifiant de ligne).

**Ce que le module garde d'un registre, en état 1 : des empreintes d'énoncé, et rien d'autre.** Le chargeur vérifie
l'empreinte du fichier entier avant toute lecture (arrêt n° 14) ; de chaque entrée, il ne lit que le champ d'énoncé, le
passe à la forme de l'arrêt n° 19 (`verifier_registre_servi_na_v1.verifier_enonce`, défauts n° 19 seuls), le normalise
comme la garde de motifs (`garde_motifs_na_v4.Normaliseur`, bords retirés), en prend l'empreinte SHA-256 et ne garde que
cette empreinte, avec l'identifiant de la ligne. Un énoncé non conforme, une entrée d'une autre forme, un identifiant de
ligne refusé : la colonne n'est pas chargée, la course ne part pas, rien n'est retiré en silence.

**Identifiant de ligne (E5).** La source de ses octets n'est pas tranchée : elle est reçue par une fonction donnée au
chargeur, `octets_identifiant_ligne(rang, entree) -> six octets`, sans valeur par défaut ; le module encode ces octets par
`identifiants_na_v1` (dix-huit lettres) et n'en fixe aucune source.

**La garde de la colonne** (07:51Z) : une ligne mord si et seulement si son empreinte normalisée, ligne entière, est l'une
des empreintes gardées. Trois tenues : (i) le module `requete_na_v3` n'a aucune entrée par où la colonne arrive ; (ii) au
pas 3 de la surcharge d'`appel` du lot 4, par `JournalRequetesColonneNA`, qui examine chaque ligne d'une requête de
proposeur ou de sonde avant la garde de motifs : une égalité, une ligne « non envoyé » (coût nul, l'arrêt nommé), un
compte, puis `ArretColonneNA` ; (iii) au départ des générations 2 et 3, chaque énoncé du registre servi fabriqué
(`garder_registre_servi`) : une égalité, la génération ne part pas. **Au départ**, chaque ligne de chaque pièce fixe
(gabarit, synthèse, consignes, témoins) passe la garde sans un refus, sinon le départ est refusé (`controler_pieces_fixes`).
Ce que la garde ne tient pas : un énoncé repris en substance ; elle tient la copie, non le sens.

**L'interrupteur `colonne_matiere_premiere`** se lit à la sixième ligne de la pièce de relevés, sous un **libellé
d'essai**, déclaré comme tel (le libellé fixe viendra à l'additif du véhicule) ; une ligne absente, double, d'un autre
libellé, mal formée ou d'une autre empreinte de registre refuse le départ, par son nom. État 0 : rien n'est chargé. État 1 :
le chargement et la garde, sans autre condition que l'empreinte. État 2 : en plus, la règle d'allumage, toutes conditions
ensemble ; l'empreinte de l'additif se lit au **manifeste de la lecture de fin** (E4), jamais dans la configuration de la
course. Aucun état n'est pris d'une variable d'environnement, ni de la configuration seule. Ce module n'écrit rien en
décidant l'état. La lecture de fin elle-même est au lot 10 b.

**Aucun message, aucun `repr`, aucune ligne de journal de ce module ne recopie un nom, un énoncé ou un octet d'une
entrée** : rangs, identifiants, empreintes, comptes seulement.

Bibliothèque standard, et les modules des lots 1 à 3 et 5.
"""

import dataclasses
import hashlib
import json
import os
import re
import types

from pole import garde_motifs_na_v4 as gm
from pole import identifiants_na_v1 as ident
from pole import journal_na_v3 as jn
from pole import registre_na_v1 as rg
from pole import requete_na_v3 as rq
from pole import verifier_registre_servi_na_v1 as vr

VERSION = "matiere-premiere-na-v1"
INTERRUPTEUR = "colonne_matiere_premiere"
ETAT_ETEINTE, ETAT_GARDE_SEULE, ETAT_ALLUMEE = 0, 1, 2
NOMS_ETATS = {ETAT_ETEINTE: "éteinte", ETAT_GARDE_SEULE: "garde seule", ETAT_ALLUMEE: "allumée"}
ETAT_PAR_DEFAUT = ETAT_GARDE_SEULE  # mère, 07:46Z, mot 9 : c'est l'état que la pièce de relevés doit porter
ARRET_COLONNE = "garde de la colonne « matière première »"  # sans numéro dans la V9 : l'additif du véhicule le lui donne
NUMERO_ARRET_EMPREINTE = 14
NUMERO_ARRET_FORME = vr.ARRET_NON_CONFORME  # 19
OCTETS_IDENTIFIANT_LIGNE = 6
SORTES_GARDEES = ("proposeur", "sonde_refus")  # tenue (ii) : « pour tout rôle de proposeur et pour la sonde »

# Sixième ligne de la pièce de relevés : LIBELLÉ D'ESSAI, déclaré comme tel (contrôle v5, point 4). Le libellé fixe sera
# écrit à l'additif du véhicule ; la forme porte l'interrupteur, son état, l'empreinte du registre servi, la date.
STATUT_LIBELLE = "libellé d'essai, déclaré comme tel ; le libellé fixe viendra à l'additif du véhicule"
LIBELLE_ESSAI = "colonne « matière première » [libellé d'essai] :"
_LIGNE_ESSAI = re.compile(
    r"^" + re.escape(LIBELLE_ESSAI) + r" interrupteur " + INTERRUPTEUR
    + r" ; état (?P<etat>[012]) \((?P<nom>éteinte|garde seule|allumée)\) ; registre servi (?P<sha>[0-9a-f]{64})"
    + r" ; date (?P<date>[0-9]{4}-[0-9]{2}-[0-9]{2})$")

# Règle d'allumage (état 2) : formes d'essai, déclarées comme telles.
FORMAT_MANIFESTE_LECTURE_FIN = "manifeste-lecture-de-fin-na-v1 (forme d'essai)"
CLE_EMPREINTE_ADDITIF = "empreinte_additif"
JUGES_DE_FIN = ("lecteur d'antériorité 1", "lecteur d'antériorité 2", "juge de l'espèce 3", "juge de l'espèce 1")
LIGNE_DEVIS = "lecture de fin"
# Une variable d'environnement dont le nom porte l'un de ces fragments refuse toute décision d'état.
FRAGMENTS_ENV_INTERDITS = ("MATIERE_PREMIERE", "COLONNE_MATIERE")
CLE_CONFIGURATION = INTERRUPTEUR

_HEXA64 = re.compile(r"^[0-9a-f]{64}$")


# --- refus ---------------------------------------------------------------------------------------------------------------

class RefusColonneNA(RuntimeError):
    """Un refus de la colonne ; le message ne dit que la cause, des rangs, des identifiants, des empreintes, des comptes."""

    numero = None

    def __init__(self, cause):
        super().__init__(cause)
        self.cause = cause


class DepartRefuseColonneNA(RefusColonneNA):
    """Le départ est refusé : sixième ligne, registre, pièce fixe, interrupteur. `numero` vaut 14 pour une empreinte."""

    def __init__(self, cause, numero=None):
        super().__init__(f"colonne « matière première » : {cause} ; départ refusé")
        self.numero = numero


class ColonneNonChargee(DepartRefuseColonneNA):
    """Le registre ne se charge pas ; rien n'est retiré en silence. `defauts` : (rang d'entrée, cause), sans contenu."""

    def __init__(self, cause, defauts=(), numero=None):
        self.defauts = tuple(defauts)
        super().__init__(f"colonne non chargée ({cause} ; {len(self.defauts)} défaut(s))", numero)


class EtatRefuseNA(DepartRefuseColonneNA):
    """L'état demandé de l'interrupteur est refusé, avant toute écriture ; `manques` nomme les conditions manquantes."""

    def __init__(self, etat, manques):
        self.etat, self.manques = etat, tuple(manques)
        super().__init__(f"état {etat} de l'interrupteur refusé : " + " ; ".join(self.manques))


class ArretColonneNA(RefusColonneNA):
    """Arrêt nommé de la garde de la colonne, en course (tenue ii) : l'envoi est refusé, « non envoyé », coût nul.
    Numéro à l'additif du véhicule."""

    nom = ARRET_COLONNE

    def __init__(self, role, rang_ligne, identifiants):
        self.role, self.rang_ligne, self.identifiants = role, rang_ligne, tuple(identifiants)
        super().__init__(f"arrêt « {ARRET_COLONNE} » : rôle « {role} », ligne de rang {rang_ligne} de la requête égale à "
                         f"l'entrée {', '.join(self.identifiants)} ; envoi refusé, rien ne part")


class GenerationRefuseeColonneNA(RefusColonneNA):
    """Tenue (iii) : un énoncé du registre servi fabriqué est égal à une entrée de la colonne ; la génération ne part pas."""

    nom = ARRET_COLONNE

    def __init__(self, generation, constats):
        self.generation, self.constats = generation, tuple(constats)
        super().__init__(f"arrêt « {ARRET_COLONNE} » : génération {generation}, {len(self.constats)} ligne(s) du registre "
                         "servi égale(s) à une entrée de la colonne ; la génération ne part pas ; aucune ligne retirée")


# --- normalisation -------------------------------------------------------------------------------------------------------

def _forme(normaliseur, texte):
    """La forme comparée : la normalisation de la garde de motifs, puis les bords retirés."""
    return normaliseur.normaliser(texte).strip()


def _empreinte_forme(forme):
    return hashlib.sha256(forme.encode("utf-8")).hexdigest()


def _sans_double(paires):
    d = {}
    for k, v in paires:
        if k in d:
            raise ColonneNonChargee("clé en double dans le registre")
        d[k] = v
    return d


# --- la colonne chargée --------------------------------------------------------------------------------------------------

@dataclasses.dataclass(frozen=True)
class Constat:
    rang_ligne: int
    identifiants: tuple


class Colonne:
    """La colonne chargée en état 1 ou 2 : l'empreinte du registre, les empreintes d'énoncé et les identifiants de ligne.
    Ni nom, ni énoncé, ni autre champ n'y est gardé."""

    __slots__ = ("registre_sha256", "entrees", "_par_empreinte", "_normaliseur")

    def __init__(self, registre_sha256, couples, normaliseur):
        par = {}
        for identifiant, empreinte in couples:
            par.setdefault(empreinte, []).append(identifiant)
        object.__setattr__(self, "registre_sha256", registre_sha256)
        object.__setattr__(self, "entrees", len(couples))
        object.__setattr__(self, "_par_empreinte", types.MappingProxyType({k: tuple(v) for k, v in par.items()}))
        object.__setattr__(self, "_normaliseur", normaliseur)

    def __setattr__(self, *_):
        raise AttributeError("une colonne chargée ne change pas")

    def __repr__(self):
        return f"Colonne(registre={self.registre_sha256}, entrees={self.entrees}, empreintes={len(self._par_empreinte)})"

    @property
    def empreintes(self):
        return frozenset(self._par_empreinte)

    def identifiants(self):
        return tuple(sorted(i for ids in self._par_empreinte.values() for i in ids))

    def examiner_ligne(self, ligne):
        """Rend les identifiants des entrées égales à cette ligne entière (forme normalisée), ou ()."""
        if type(ligne) is not str:
            raise TypeError("la garde lit une ligne en chaîne")
        forme = _forme(self._normaliseur, ligne)
        if not forme:
            return ()
        return self._par_empreinte.get(_empreinte_forme(forme), ())

    def examiner_texte(self, texte):
        """Chaque ligne d'un texte (`str.splitlines`), comparée entière ; rend les constats (rang de ligne, identifiants)."""
        if type(texte) is not str:
            raise TypeError("la garde lit un texte en chaîne")
        rendu = []
        for i, ligne in enumerate(texte.splitlines(), start=1):
            ids = self.examiner_ligne(ligne)
            if ids:
                rendu.append(Constat(i, ids))
        return rendu

    def examiner_octets(self, octets):
        if not isinstance(octets, (bytes, bytearray)):
            raise TypeError("la garde lit des octets")
        try:
            texte = bytes(octets).decode("utf-8")
        except UnicodeDecodeError:
            raise RefusColonneNA("texte qui n'est pas en UTF-8 valide : refusé, jamais réparé") from None
        return self.examiner_texte(texte)

    def ligne_manifeste(self, etat):
        """Ce que le manifeste de départ porte de la colonne : comptes et empreintes."""
        return {"interrupteur": INTERRUPTEUR, "etat": etat, "nom_etat": NOMS_ETATS[etat],
                "registre_sha256": self.registre_sha256, "entrees": self.entrees,
                "empreintes_distinctes": len(self._par_empreinte), "libelle": STATUT_LIBELLE, "version": VERSION}


# --- le chargeur ---------------------------------------------------------------------------------------------------------

def lire_registre(octets, empreinte_attendue, *, normaliseur, octets_identifiant_ligne, champ_enonce, champs_entree,
                  borne_enonce_octets, cle_des_entrees=None, entrees_attendues=None):
    """Charge le registre de la colonne à son empreinte ; rend une `Colonne`.

    - L'empreinte des octets entiers est vérifiée **avant toute lecture** (arrêt n° 14).
    - Forme d'essai, déclarée : JSON ; la liste des entrées est la valeur entière (`cle_des_entrees=None`) ou la valeur de
      cette clé, seule clé de l'objet ; chaque entrée est un objet aux champs exactement `champs_entree`, dont
      `champ_enonce`, une chaîne. `entrees_attendues`, s'il est donné, est le nombre exact d'entrées.
    - Chaque énoncé passe la forme de l'arrêt n° 19, puis la normalisation ; vide après elle : refusé.
    - `octets_identifiant_ligne(rang, entree)` rend six octets (E5) ; identifiants distincts.
    Tous les défauts sont rassemblés ; un seul suffit : `ColonneNonChargee`, rien n'est chargé."""
    if not isinstance(normaliseur, gm.Normaliseur):
        raise ColonneNonChargee("la normalisation est celle de la garde de motifs (`Normaliseur` du lot 2)")
    if not callable(octets_identifiant_ligne):
        raise ColonneNonChargee("l'identifiant de ligne se reçoit par une fonction donnée au chargeur (E5)")
    if type(champ_enonce) is not str or not isinstance(champs_entree, (tuple, list)) or champ_enonce not in champs_entree \
            or len(set(champs_entree)) != len(champs_entree):
        raise ColonneNonChargee("forme déclarée des entrées : champs distincts, le champ d'énoncé parmi eux")
    if type(borne_enonce_octets) is not int or borne_enonce_octets <= 0:
        raise ColonneNonChargee("borne de l'énoncé : un entier positif")
    if not isinstance(octets, (bytes, bytearray)):
        raise ColonneNonChargee("le registre se lit en octets")
    octets = bytes(octets)
    sha = hashlib.sha256(octets).hexdigest()
    if type(empreinte_attendue) is not str or sha != empreinte_attendue:
        raise ColonneNonChargee("empreinte du registre servi de la matière différente de celle qui est écrite",
                                numero=NUMERO_ARRET_EMPREINTE)
    try:
        obj = json.loads(octets.decode("utf-8"), object_pairs_hook=_sans_double)
    except (UnicodeDecodeError, json.JSONDecodeError) as e:
        raise ColonneNonChargee(f"registre illisible ({type(e).__name__})") from None
    if cle_des_entrees is not None:
        if not isinstance(obj, dict) or set(obj) != {cle_des_entrees}:
            raise ColonneNonChargee("registre : un objet à une seule clé, celle des entrées")
        obj = obj[cle_des_entrees]
    if not isinstance(obj, list) or not obj:
        raise ColonneNonChargee("registre : une liste d'entrées non vide")
    if entrees_attendues is not None and len(obj) != entrees_attendues:
        raise ColonneNonChargee(f"registre : {len(obj)} entrées pour {entrees_attendues} attendues")
    defauts, couples, vus = [], [], set()
    attendus = set(champs_entree)
    for rang, entree in enumerate(obj, start=1):
        if not isinstance(entree, dict) or set(entree) != attendus:
            defauts.append((rang, "entrée d'une autre forme (champs)"))
            continue
        enonce = entree[champ_enonce]
        if type(enonce) is not str:
            defauts.append((rang, "énoncé qui n'est pas une chaîne"))
            continue
        forme_defauts = [c for n, c in vr.verifier_enonce(enonce, borne_enonce_octets) if n == NUMERO_ARRET_FORME]
        for cause in forme_defauts:
            defauts.append((rang, f"arrêt n° {NUMERO_ARRET_FORME} : {cause}"))
        forme = _forme(normaliseur, enonce)
        if not forme:
            defauts.append((rang, "énoncé vide après normalisation"))
        try:
            brut = octets_identifiant_ligne(rang, types.MappingProxyType(dict(entree)))
        except Exception as e:  # noqa: BLE001 — la fonction donnée échoue : refus nommé, jamais un repli
            defauts.append((rang, f"identifiant de ligne : la fonction donnée a échoué ({type(e).__name__})"))
            continue
        if type(brut) is not bytes or len(brut) != OCTETS_IDENTIFIANT_LIGNE:
            defauts.append((rang, f"identifiant de ligne : {OCTETS_IDENTIFIANT_LIGNE} octets attendus"))
            continue
        identifiant = ident.encoder_octets(brut)
        if identifiant in vus:
            defauts.append((rang, "identifiant de ligne déjà donné à une autre entrée"))
            continue
        vus.add(identifiant)
        if forme and not forme_defauts:
            couples.append((identifiant, _empreinte_forme(forme)))
    if defauts:
        raise ColonneNonChargee("registre non conforme", defauts, numero=NUMERO_ARRET_FORME)
    return Colonne(sha, tuple(couples), normaliseur)


def charger_registre(chemin, empreinte_attendue, **reglages):
    """Lit le fichier, puis `lire_registre` (l'empreinte est vérifiée avant toute lecture du contenu)."""
    with open(chemin, "rb") as f:
        octets = f.read()
    return lire_registre(octets, empreinte_attendue, **reglages)


# --- la sixième ligne de la pièce de relevés -----------------------------------------------------------------------------

@dataclasses.dataclass(frozen=True)
class LigneEtat:
    etat: int
    registre_sha256: str
    date: str
    rang: int


def lire_sixieme_ligne(piece_octets, empreinte_piece):
    """La ligne de l'interrupteur dans la pièce de relevés, lue à l'empreinte de la pièce (arrêt n° 14). Exactement une
    ligne au libellé d'essai ; absente, double, d'un autre libellé ou mal formée : départ refusé, par son nom."""
    if not isinstance(piece_octets, (bytes, bytearray)):
        raise DepartRefuseColonneNA("la pièce de relevés se lit en octets")
    piece_octets = bytes(piece_octets)
    if type(empreinte_piece) is not str or hashlib.sha256(piece_octets).hexdigest() != empreinte_piece:
        raise DepartRefuseColonneNA("empreinte de la pièce de relevés différente de celle qui est écrite",
                                    NUMERO_ARRET_EMPREINTE)
    try:
        texte = piece_octets.decode("utf-8")
    except UnicodeDecodeError:
        raise DepartRefuseColonneNA("pièce de relevés illisible") from None
    lignes = texte.split("\n")
    a_libelle = [(i, l) for i, l in enumerate(lignes, start=1) if l.startswith(LIBELLE_ESSAI)]
    autres = [i for i, l in enumerate(lignes, start=1) if INTERRUPTEUR in l and not l.startswith(LIBELLE_ESSAI)]
    if autres:
        raise DepartRefuseColonneNA(f"ligne de l'interrupteur d'un autre libellé (rang {autres[0]})")
    if not a_libelle:
        raise DepartRefuseColonneNA("ligne de l'état de l'interrupteur absente de la pièce de relevés")
    if len(a_libelle) > 1:
        raise DepartRefuseColonneNA("ligne de l'état de l'interrupteur en double dans la pièce de relevés")
    rang, ligne = a_libelle[0]
    m = _LIGNE_ESSAI.match(ligne)
    if m is None:
        raise DepartRefuseColonneNA(f"ligne de l'état de l'interrupteur mal formée (rang {rang})")
    etat = int(m.group("etat"))
    if NOMS_ETATS[etat] != m.group("nom"):
        raise DepartRefuseColonneNA(f"ligne de l'état de l'interrupteur : nom d'état qui n'est pas celui de l'état {etat}")
    return LigneEtat(etat, m.group("sha"), m.group("date"), rang)


# --- l'interrupteur et la règle d'allumage --------------------------------------------------------------------------------

@dataclasses.dataclass(frozen=True)
class ConditionsAllumage:
    """Ce que l'état 2 exige en plus de l'état 1 (§ 2.14, (a) à (e) ; E4). Formes d'essai, déclarées."""

    ligne_accord_lazar: object = None
    chemin_manifeste_lecture_fin: object = None
    empreinte_additif_attendue: object = None  # épinglée par le lanceur (lot 8), jamais lue dans la configuration
    devis_ligne_a_part: object = None
    lecteurs_inscrits: tuple = ()
    branche_orpheline: object = None


def _manques_allumage(c, registre_sha256):
    manques = []
    if not isinstance(c, ConditionsAllumage):
        return ["conditions d'allumage absentes"]
    a = c.ligne_accord_lazar
    if type(a) is not str or INTERRUPTEUR not in a or "état 2" not in a or registre_sha256 not in a:
        manques.append("(a) ligne d'accord de Lazar qui nomme l'interrupteur, l'état 2 et l'empreinte du registre")
    manques.extend(_manques_manifeste(c.chemin_manifeste_lecture_fin, c.empreinte_additif_attendue))
    d = c.devis_ligne_a_part
    if not (isinstance(d, dict) and d.get("ligne") == LIGNE_DEVIS and d.get("hors_parts_de_la_course") is True
            and type(d.get("plafond_usd")) in (int, float) and d["plafond_usd"] > 0):
        manques.append("(c) devis de la lecture de fin sur une ligne à part, hors des parts de la course")
    lec = c.lecteurs_inscrits
    if not isinstance(lec, tuple) or not lec or len(set(lec)) != len(lec) or not set(lec) <= set(JUGES_DE_FIN):
        manques.append("(d) lecteurs inscrits, parmi les juges de fin seuls")
    if c.branche_orpheline is not True:
        manques.append("(e) branche vérifiée orpheline")
    return manques


def _manques_manifeste(chemin, attendue):
    """E4 : le manifeste de la lecture de fin existe et porte l'empreinte de l'additif, égale à celle qui est épinglée."""
    if type(attendue) is not str or _HEXA64.match(attendue) is None:
        return ["(b) empreinte de l'additif épinglée absente"]
    if type(chemin) is not str or not os.path.isfile(chemin):
        return ["(b) manifeste de la lecture de fin absent"]
    try:
        with open(chemin, "rb") as f:
            obj = json.loads(f.read().decode("utf-8"))
    except (OSError, UnicodeDecodeError, json.JSONDecodeError):
        return ["(b) manifeste de la lecture de fin illisible"]
    if not isinstance(obj, dict) or obj.get("format") != FORMAT_MANIFESTE_LECTURE_FIN:
        return ["(b) manifeste de la lecture de fin d'une autre forme"]
    if CLE_EMPREINTE_ADDITIF not in obj:
        return ["(b) le manifeste de la lecture de fin ne porte pas l'empreinte de l'additif"]
    if obj[CLE_EMPREINTE_ADDITIF] != attendue:
        return ["(b) le manifeste de la lecture de fin porte une autre empreinte de l'additif"]
    return []


def decider_etat(ligne, *, configuration, environ=None, conditions_allumage=None):
    """L'état de l'interrupteur, lu à la sixième ligne seule ; rien n'est écrit. Refus, avant toute écriture : une
    variable d'environnement qui nomme la colonne ; une configuration qui porte un autre état ; l'état 2 sans toutes les
    conditions d'allumage. La configuration n'est jamais lue pour l'empreinte de l'additif."""
    if not isinstance(ligne, LigneEtat):
        raise EtatRefuseNA(None, ["l'état se lit à la sixième ligne de la pièce de relevés, et là seulement"])
    env = os.environ if environ is None else environ
    noms = sorted(k for k in env if any(f in k.upper() for f in FRAGMENTS_ENV_INTERDITS))
    if noms:
        raise EtatRefuseNA(ligne.etat, [f"variable d'environnement qui nomme la colonne ({len(noms)}) : aucun état ne "
                                        "se prend de l'environnement"])
    if not isinstance(configuration, dict):
        raise EtatRefuseNA(ligne.etat, ["configuration de la course absente"])
    if CLE_CONFIGURATION in configuration and configuration[CLE_CONFIGURATION] != ligne.etat:
        raise EtatRefuseNA(ligne.etat, ["la configuration porte un autre état que la pièce de relevés"])
    if ligne.etat == ETAT_ALLUMEE:
        manques = _manques_allumage(conditions_allumage, ligne.registre_sha256)
        if manques:
            raise EtatRefuseNA(ETAT_ALLUMEE, manques)
    return ligne.etat


# --- le départ -----------------------------------------------------------------------------------------------------------

@dataclasses.dataclass(frozen=True)
class DepartColonne:
    """Ce que rend le contrôle de départ : l'état, la colonne (None en état 0), la ligne du manifeste de départ."""

    etat: int
    colonne: object
    manifeste: dict


def controler_pieces_fixes(colonne, pieces):
    """Au départ : chaque ligne de chaque pièce fixe passe la garde sans un refus ; sinon départ refusé, en nommant la
    pièce, le rang de la ligne et l'identifiant de l'entrée (« c'est un point pour la mère »). `pieces` : {nom : octets}."""
    if not isinstance(colonne, Colonne):
        raise DepartRefuseColonneNA("contrôle des pièces fixes sans colonne chargée")
    if not isinstance(pieces, dict) or not pieces:
        raise DepartRefuseColonneNA("pièces fixes absentes du contrôle de départ")
    refus = []
    for nom in sorted(pieces):
        for c in colonne.examiner_octets(pieces[nom]):
            refus.append(f"pièce « {nom} », ligne de rang {c.rang_ligne}, entrée {', '.join(c.identifiants)}")
    if refus:
        raise DepartRefuseColonneNA("pièce fixe qui porte un énoncé entier de la colonne : " + " ; ".join(refus))
    return len(pieces)


def preparer_depart(*, piece_releves, empreinte_piece_releves, empreinte_registre_attendue, configuration, pieces_fixes,
                    charger, environ=None, conditions_allumage=None):
    """Le contrôle de départ de la colonne, pour le lanceur (lot 8) : la sixième ligne (arrêt n° 14 sur la pièce et sur
    l'empreinte du registre), l'état, puis, en état 1 ou 2, le chargement (`charger()` rend la `Colonne`, l'empreinte
    vérifiée avant toute lecture) et le contrôle des pièces fixes. En état 0, rien n'est chargé ni contrôlé."""
    ligne = lire_sixieme_ligne(piece_releves, empreinte_piece_releves)
    if type(empreinte_registre_attendue) is not str or ligne.registre_sha256 != empreinte_registre_attendue:
        raise DepartRefuseColonneNA("la ligne de l'état porte une autre empreinte du registre servi que celle qui est "
                                    "écrite", NUMERO_ARRET_EMPREINTE)
    etat = decider_etat(ligne, configuration=configuration, environ=environ, conditions_allumage=conditions_allumage)
    if etat == ETAT_ETEINTE:
        return DepartColonne(etat, None, {"interrupteur": INTERRUPTEUR, "etat": etat, "nom_etat": NOMS_ETATS[etat],
                                          "libelle": STATUT_LIBELLE, "version": VERSION})
    colonne = charger()
    if not isinstance(colonne, Colonne) or colonne.registre_sha256 != ligne.registre_sha256:
        raise DepartRefuseColonneNA("colonne chargée d'un autre registre que celui de la ligne", NUMERO_ARRET_EMPREINTE)
    controler_pieces_fixes(colonne, pieces_fixes)
    return DepartColonne(etat, colonne, colonne.ligne_manifeste(etat))


# --- tenue (ii) : au pas 3 de la surcharge d'`appel` (lot 4), par le journal --------------------------------------------

class JournalRequetesColonneNA(jn.JournalRequetes):
    """Le journal du lot 3, qui garde la colonne avant la garde de motifs. La surcharge d'`appel` du lot 4 appelle
    `journaliser_envoi` à son pas 3, après le routage et la part : une ligne de requête de proposeur ou de sonde égale à
    une entrée y écrit une ligne « non envoyé » (arrêt nommé, coût nul, sans contenu), compte le refus, et lève
    `ArretColonneNA`, que le lot 4 ne rattrape pas : rien ne part, le noyau n'est pas appelé, aucun coût n'est compté.
    Un journal en panne à cette ligne : `JournalRefuse`, que le lot 4 traite comme « requête journalisée »."""

    def __init__(self, dossier_sortie, nom_fichier, *, depart):
        if not isinstance(depart, DepartColonne):
            raise jn.JournalRefuse("le journal de la colonne exige le contrôle de départ (`DepartColonne`)")
        if depart.etat != ETAT_ETEINTE and not isinstance(depart.colonne, Colonne):
            raise jn.JournalRefuse("état 1 ou 2 sans colonne chargée")
        super().__init__(dossier_sortie, nom_fichier)
        self.depart = depart
        self.comptes_colonne = {}

    def journaliser_envoi(self, requete, garde, *, role, cle):
        colonne = self.depart.colonne
        if colonne is not None and isinstance(requete, rq.RequeteAssemblee) and requete.sorte in SORTES_GARDEES:
            constats = colonne.examiner_octets(requete.octets)
            if constats:
                c = constats[0]
                self.journaliser_non_envoye(arret=ARRET_COLONNE, role=role, generation=requete.generation,
                                            case=requete.identifiant_case, cle=cle,
                                            cause=f"ligne de rang {c.rang_ligne} égale à l'entrée "
                                                  f"{', '.join(c.identifiants)} ; {len(constats)} ligne(s) en tout",
                                            sorte=requete.sorte, sha256=requete.sha256, taille=requete.taille)
                self.comptes_colonne[role] = self.comptes_colonne.get(role, 0) + 1
                raise ArretColonneNA(role, c.rang_ligne, c.identifiants)
        return super().journaliser_envoi(requete, garde, role=role, cle=cle)


# --- tenue (iii) : le registre servi fabriqué, au départ des générations 2 et 3 ------------------------------------------

def enonces_du_registre_servi(octets):
    """Les énoncés des lignes de tentative d'un registre servi (forme de `registre_na_v1`) : (rang de ligne, énoncé).
    Une ligne de tentative illisible est refusée (elle est aussi refusée par l'arrêt n° 19)."""
    if not isinstance(octets, (bytes, bytearray)):
        raise RefusColonneNA("le registre servi se lit en octets")
    texte = bytes(octets).decode("utf-8")
    rendu = []
    for i, ligne in enumerate(texte.split("\n"), start=1):
        if not ligne.startswith(rg.TETE_TENTATIVE):
            continue
        parts = ligne[len(rg.TETE_TENTATIVE):].split(rg.SEPARATEUR, 5)
        try:
            if len(parts) != 6:
                raise ValueError
            enonce, fin = json.JSONDecoder().raw_decode(parts[5])
            if fin != len(parts[5]) or type(enonce) is not str:
                raise ValueError
        except ValueError:
            raise RefusColonneNA(f"ligne de tentative de rang {i} illisible pour la garde de la colonne") from None
        rendu.append((i, enonce))
    return rendu


def garder_registre_servi(depart, octets, generation):
    """Tenue (iii) : chaque énoncé du registre servi, et chaque ligne entière du fichier, comparés ; une égalité : la
    génération ne part pas, aucune ligne n'est retirée. En état 0 : rien."""
    if not isinstance(depart, DepartColonne):
        raise RefusColonneNA("la garde du registre servi exige le contrôle de départ")
    if generation not in (2, 3):
        raise RefusColonneNA("le registre servi se garde aux générations 2 et 3")
    if depart.colonne is None:
        return 0
    constats = []
    for rang, enonce in enonces_du_registre_servi(octets):
        ids = depart.colonne.examiner_ligne(enonce)
        if ids:
            constats.append(Constat(rang, ids))
    for c in depart.colonne.examiner_octets(octets):
        if all(c.rang_ligne != d.rang_ligne for d in constats):
            constats.append(c)
    if constats:
        raise GenerationRefuseeColonneNA(generation, sorted(constats, key=lambda c: c.rang_ligne))
    return len(enonces_du_registre_servi(octets))


# --- taux de faux refus --------------------------------------------------------------------------------------------------

def mesurer_faux_refus(colonne, requetes, registres_servis=()):
    """Sur des requêtes assemblées et des registres servis **où aucun énoncé de la colonne n'est planté**, chaque refus est
    un faux refus : rend les comptes et le taux (lignes refusées sur lignes examinées), rapportés, jamais corrigés."""
    if not isinstance(colonne, Colonne):
        raise RefusColonneNA("mesure sans colonne chargée")
    lignes = refusees = req_refusees = 0
    requetes = list(requetes)
    for r in requetes:
        if not isinstance(r, rq.RequeteAssemblee):
            raise RefusColonneNA("la mesure lit des requêtes assemblées")
        texte = r.octets.decode("utf-8")
        lignes += len(texte.splitlines())
        n = len(colonne.examiner_texte(texte))
        refusees += n
        req_refusees += 1 if n else 0
    reg_lignes = reg_refusees = 0
    registres_servis = list(registres_servis)
    for o in registres_servis:
        enonces = enonces_du_registre_servi(o)
        reg_lignes += len(enonces)
        reg_refusees += sum(1 for _, e in enonces if colonne.examiner_ligne(e))
    total = lignes + reg_lignes
    return {"requetes": len(requetes), "lignes_de_requete": lignes, "lignes_refusees": refusees,
            "requetes_refusees": req_refusees, "registres_servis": len(registres_servis),
            "enonces_du_registre_servi": reg_lignes, "enonces_refuses": reg_refusees,
            "taux_de_faux_refus": (refusees + reg_refusees) / total if total else None}


# --- recherche d'absence (essai à blanc, lot 9) --------------------------------------------------------------------------

def rechercher_textes(racines, textes):
    """Cherche, par programme, chacun des `textes` (octets UTF-8) dans tous les fichiers sous `racines` ; rend le nombre
    de fichiers où au moins un est trouvé et le nombre de trouvailles, sans dire ce qui est trouvé."""
    aiguilles = [t.encode("utf-8") for t in textes if t]
    fichiers = trouvailles = 0
    for racine in racines:
        for dossier, _, noms in os.walk(racine):
            for nom in noms:
                with open(os.path.join(dossier, nom), "rb") as f:
                    contenu = f.read()
                n = sum(contenu.count(a) for a in aiguilles)
                fichiers += 1 if n else 0
                trouvailles += n
    return {"fichiers_ou_trouve": fichiers, "trouvailles": trouvailles}
