"""Véhicule NA-1, lot 2 — garde de motifs (`garde_motifs_na_v1`) : programme, format de la liste, témoins positifs.

Lettre : V9, arrêt n° 16 (l. 387) ; conception du véhicule v4 (`3428dfb3…`), § 2.3 (pas 3), § 5.1 (ligne
`garde_motifs`), § 6.1 (ligne du n° 16), § 7 (lot 2).

- La garde lit la requête assemblée **au dernier point avant l'envoi** : elle copie les octets reçus, ne lit que cette
  copie, et rend cette copie, figée, avec son empreinte SHA-256 et sa taille. Après elle, plus aucun octet ne change :
  l'empreinte journalisée est celle de ce qu'elle a lu, et ce qui part est ce qu'elle a lu (`RequeteGardee`).
- Deux familles, gelées par l'empreinte de leur liste et de ce programme : « identité et dépôt », puis « composition et
  tenue », dans cet ordre (noms à la lettre de V9, l. 387).
- Normalisation avant la comparaison (V9, l. 387) : caractères invisibles retirés (catégorie Unicode « Cf »), forme de
  compatibilité (NFKC), casse repliée, puis NFKC de nouveau ; chaque tiret (catégorie « Pd », et le signe moins) ramené à
  « - » ; chaque suite d'espaces (tout blanc Unicode, fins de ligne comprises) ramenée à une espace.
- Chaque motif a un **témoin positif**, rejoué à chaque départ (`GardeMotifs.verifier_temoins`) : un motif qui ne mord
  pas sur son témoin refuse le départ.
- Un refus nomme la famille et le rang ; le texte trouvé ne va qu'au journal (`ArretMotifInterdit.texte_trouve`, jamais
  dans le message) ; rien n'est coupé, remplacé ni renvoyé.
- **La liste réelle des motifs n'est pas écrite ici** : elle est rédigée à part (modèle F) au format ci-dessous.

Format de la liste (`liste-motifs-na-v1`), un fichier JSON en UTF-8, clés exactement celles-ci, aucune clé en double :

    {"format": "liste-motifs-na-v1",
     "familles": [
       {"nom": "identité et dépôt",   "motifs": [{"rang": 1, "type": "litteral", "motif": "…", "temoin_positif": "…"}, …]},
       {"nom": "composition et tenue", "motifs": [{"rang": 1, "type": "expression_reguliere", "motif": "…",
                                                    "temoin_positif": "…"}, …]}]}

- `rang` : entiers 1, 2, 3… dans l'ordre, sans trou, par famille ; une famille vide est refusée.
- `type` « litteral » : le motif est normalisé comme le texte, puis cherché comme sous-chaîne ; vide après normalisation :
  refusé.
- `type` « expression_reguliere » : expression du module `re` de Python, appliquée telle quelle au texte **normalisé**
  (minuscules repliées, une seule espace, « - » seul tiret) ; une expression qui ne se compile pas, ou qui peut rendre un
  accord de longueur nulle, est refusée.
- `temoin_positif` : chaîne non vide ; normalisée, le motif doit y mordre.

Bibliothèque standard seule.
"""

import dataclasses
import hashlib
import json
import os
import re
import unicodedata

VERSION = "garde-motifs-na-v1"
FORMAT_LISTE = "liste-motifs-na-v1"
FAMILLES = ("identité et dépôt", "composition et tenue")
TYPES = ("litteral", "expression_reguliere")
NUMERO_ARRET = 16

_SONDES_ACCORD_VIDE = ("", " ", "x", "x y", "-", "xx-yy zz")
_ESPACES = re.compile(r"\s+")
_TIRETS_HORS_PD = {"−"}  # signe moins


class ListeMotifsRefusee(ValueError):
    """La liste des motifs ne tient pas son format ou son empreinte : la garde ne se construit pas."""


class TemoinPositifManque(RuntimeError):
    """Un motif ne mord pas sur son témoin positif : le départ est refusé (V9, l. 387)."""

    def __init__(self, famille, rang):
        super().__init__(f"arrêt n° {NUMERO_ARRET} au départ : le motif de rang {rang} de la famille « {famille} » "
                         "ne mord pas sur son témoin positif ; départ refusé")
        self.famille = famille
        self.rang = rang


class ArretMotifInterdit(RuntimeError):
    """Arrêt n° 16 : l'envoi est refusé ; le message dit la famille et le rang, jamais le texte trouvé."""

    numero = NUMERO_ARRET

    def __init__(self, famille, rang, texte_trouve):
        super().__init__(f"arrêt n° {NUMERO_ARRET}, motif interdit dans un texte à servir : famille « {famille} », "
                         f"rang {rang} ; envoi refusé")
        self.famille = famille
        self.rang = rang
        self.texte_trouve = texte_trouve  # pour le journal seulement


class RequeteIllisible(ValueError):
    """La requête n'est pas une suite d'octets en UTF-8 valide : refusée, jamais réparée."""


class EcartApresGarde(RuntimeError):
    """Les octets à envoyer ne sont pas ceux que la garde a lus : envoi refusé."""


def normaliser(texte):
    """La normalisation de la garde (V9, l. 387), appliquée au texte et aux motifs littéraux."""
    if type(texte) is not str:
        raise TypeError("la normalisation lit une chaîne")
    t = "".join(ch for ch in texte if unicodedata.category(ch) != "Cf")
    t = unicodedata.normalize("NFKC", t)
    t = t.casefold()
    t = unicodedata.normalize("NFKC", t)
    t = "".join(ch for ch in t if unicodedata.category(ch) != "Cf")
    t = "".join("-" if (unicodedata.category(ch) == "Pd" or ch in _TIRETS_HORS_PD) else ch for ch in t)
    t = _ESPACES.sub(" ", t)
    return t


@dataclasses.dataclass(frozen=True)
class Motif:
    famille: str
    rang: int
    type: str
    motif: str
    temoin_positif: str
    _forme: object = dataclasses.field(compare=False, repr=False)

    def chercher(self, texte_normalise):
        """Rend le texte trouvé, ou None."""
        if self.type == "litteral":
            i = texte_normalise.find(self._forme)
            return None if i < 0 else texte_normalise[i:i + len(self._forme)]
        m = self._forme.search(texte_normalise)
        return None if m is None else m.group(0)


@dataclasses.dataclass(frozen=True)
class ListeMotifs:
    sha256: str
    familles: tuple  # ((nom, (Motif, …)), …)


def _sans_double(paires):
    d = {}
    for k, v in paires:
        if k in d:
            raise ListeMotifsRefusee(f"clé en double : {k!r}")
        d[k] = v
    return d


def _compiler(famille, rang, type_, motif):
    if type_ == "litteral":
        forme = normaliser(motif)
        if not forme:
            raise ListeMotifsRefusee(f"famille « {famille} », rang {rang} : motif littéral vide après normalisation")
        return forme
    try:
        forme = re.compile(motif)
    except re.error as e:
        raise ListeMotifsRefusee(f"famille « {famille} », rang {rang} : expression invalide ({e})") from None
    for sonde in _SONDES_ACCORD_VIDE:
        for m in forme.finditer(sonde):
            if m.end() == m.start():
                raise ListeMotifsRefusee(f"famille « {famille} », rang {rang} : expression qui peut rendre un accord "
                                         "de longueur nulle")
    return forme


def lire_liste_motifs(octets, empreinte_attendue):
    """Lit une liste à son empreinte (arrêt n° 14 pour la liste) ; refuse tout écart de format."""
    if not isinstance(octets, (bytes, bytearray)):
        raise ListeMotifsRefusee("la liste se lit en octets")
    octets = bytes(octets)
    sha = hashlib.sha256(octets).hexdigest()
    if type(empreinte_attendue) is not str or sha != empreinte_attendue:
        raise ListeMotifsRefusee("empreinte de la liste des motifs différente de celle qui est écrite")
    try:
        texte = octets.decode("utf-8")
        obj = json.loads(texte, object_pairs_hook=_sans_double)
    except (UnicodeDecodeError, json.JSONDecodeError) as e:
        raise ListeMotifsRefusee(f"liste illisible ({type(e).__name__})") from None
    if not isinstance(obj, dict) or set(obj) != {"format", "familles"}:
        raise ListeMotifsRefusee("clés de tête : exactement « format » et « familles »")
    if obj["format"] != FORMAT_LISTE:
        raise ListeMotifsRefusee("format inconnu")
    familles = obj["familles"]
    if not isinstance(familles, list) or len(familles) != len(FAMILLES):
        raise ListeMotifsRefusee("exactement deux familles")
    rendu = []
    for attendu, fam in zip(FAMILLES, familles):
        if not isinstance(fam, dict) or set(fam) != {"nom", "motifs"}:
            raise ListeMotifsRefusee("une famille porte exactement « nom » et « motifs »")
        if fam["nom"] != attendu:
            raise ListeMotifsRefusee(f"famille attendue à ce rang : « {attendu} »")
        motifs = fam["motifs"]
        if not isinstance(motifs, list) or not motifs:
            raise ListeMotifsRefusee(f"famille « {attendu} » : liste de motifs vide ou invalide")
        rendus = []
        for i, m in enumerate(motifs, start=1):
            if not isinstance(m, dict) or set(m) != {"rang", "type", "motif", "temoin_positif"}:
                raise ListeMotifsRefusee(f"famille « {attendu} » : un motif porte exactement rang, type, motif, "
                                         "temoin_positif")
            if type(m["rang"]) is not int or m["rang"] != i:
                raise ListeMotifsRefusee(f"famille « {attendu} » : rangs 1, 2, 3… dans l'ordre, sans trou")
            if m["type"] not in TYPES:
                raise ListeMotifsRefusee(f"famille « {attendu} », rang {i} : type inconnu")
            if type(m["motif"]) is not str or not m["motif"]:
                raise ListeMotifsRefusee(f"famille « {attendu} », rang {i} : motif vide")
            if type(m["temoin_positif"]) is not str or not m["temoin_positif"]:
                raise ListeMotifsRefusee(f"famille « {attendu} », rang {i} : témoin positif vide")
            forme = _compiler(attendu, i, m["type"], m["motif"])
            rendus.append(Motif(attendu, i, m["type"], m["motif"], m["temoin_positif"], forme))
        rendu.append((attendu, tuple(rendus)))
    return ListeMotifs(sha, tuple(rendu))


def charger_liste_motifs(chemin, empreinte_attendue):
    with open(chemin, "rb") as f:
        return lire_liste_motifs(f.read(), empreinte_attendue)


@dataclasses.dataclass(frozen=True)
class Constat:
    famille: str
    rang: int
    texte_trouve: str


@dataclasses.dataclass(frozen=True)
class RequeteGardee:
    """Ce que la garde a lu : ces octets, et eux seuls, partent ; leur empreinte est celle du journal."""

    octets: bytes
    sha256: str
    taille: int

    def __post_init__(self):
        if type(self.octets) is not bytes:
            raise TypeError("une requête gardée porte des octets figés")


class GardeMotifs:
    """La garde, construite au départ sur une liste lue à son empreinte ; les témoins positifs sont rejoués."""

    def __init__(self, liste):
        if not isinstance(liste, ListeMotifs):
            raise TypeError("la garde se construit sur une liste lue par `lire_liste_motifs`")
        self.liste = liste
        self.verifier_temoins()

    def motifs(self):
        for _nom, motifs in self.liste.familles:
            yield from motifs

    def verifier_temoins(self):
        """Rejouée à chaque départ : chaque motif doit mordre sur son témoin positif."""
        for motif in self.motifs():
            if motif.chercher(normaliser(motif.temoin_positif)) is None:
                raise TemoinPositifManque(motif.famille, motif.rang)

    def examiner(self, texte):
        """Rend le premier constat (famille dans l'ordre, puis rang), ou None."""
        n = normaliser(texte)
        for motif in self.motifs():
            trouve = motif.chercher(n)
            if trouve is not None:
                return Constat(motif.famille, motif.rang, trouve)
        return None

    def garder_texte(self, texte):
        """Lève l'arrêt n° 16 si un motif mord ; sinon ne rend rien."""
        constat = self.examiner(texte)
        if constat is not None:
            raise ArretMotifInterdit(constat.famille, constat.rang, constat.texte_trouve)

    def garder_requete(self, requete):
        """Le dernier point avant l'envoi : copie, lecture de la copie seule, copie figée rendue avec son empreinte."""
        if not isinstance(requete, (bytes, bytearray, memoryview)):
            raise TypeError("la garde lit la requête assemblée en octets")
        octets = bytes(requete)
        try:
            texte = octets.decode("utf-8")
        except UnicodeDecodeError:
            raise RequeteIllisible("requête qui n'est pas en UTF-8 valide : refusée") from None
        self.garder_texte(texte)
        return RequeteGardee(octets, hashlib.sha256(octets).hexdigest(), len(octets))


def verifier_avant_envoi(requete_gardee, octets_a_envoyer):
    """Égalité : ce qui part a l'empreinte de ce que la garde a lu ; sinon refus."""
    if not isinstance(octets_a_envoyer, (bytes, bytearray, memoryview)):
        raise EcartApresGarde("rien d'autre que des octets ne part")
    if hashlib.sha256(bytes(octets_a_envoyer)).hexdigest() != requete_gardee.sha256:
        raise EcartApresGarde("les octets à envoyer diffèrent de ceux que la garde a lus : envoi refusé")


def envoyer_apres_garde(garde, requete, envoyer, journal, meta=None):
    """Garde, journal, envoi, dans cet ordre. Un refus : une ligne « non envoyé » (famille, rang, texte trouvé) au journal,
    puis l'arrêt n° 16 levé, sans envoi. Une ligne d'envoi qui ne s'écrit pas : rien ne part. `envoyer` reçoit les octets
    que la garde a lus, eux-mêmes."""
    meta = dict(meta or {})
    try:
        rg = garde.garder_requete(requete)
    except ArretMotifInterdit as arret:
        journal({**meta, "evenement": "non envoyé", "arret": NUMERO_ARRET, "famille": arret.famille,
                 "rang": arret.rang, "texte_trouve": arret.texte_trouve})
        raise
    journal({**meta, "evenement": "envoi", "taille": rg.taille, "sha256": rg.sha256})
    verifier_avant_envoi(rg, rg.octets)
    return envoyer(rg.octets)


def empreinte_programme():
    """L'empreinte de ce programme, que le lanceur épingle avec celle de la liste (arrêt n° 14)."""
    with open(os.path.abspath(__file__), "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()
