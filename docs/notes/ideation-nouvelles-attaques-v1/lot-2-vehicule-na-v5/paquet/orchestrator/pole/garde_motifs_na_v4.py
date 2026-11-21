"""Véhicule NA-1, lot 2 — garde de motifs (`garde_motifs_na_v4`) : programme, format de la liste, témoins positifs.

v4 (remplace `garde_motifs_na_v3`, `cea1e692…`, gardé tel quel dans le paquet pour les lots qui l'importent), sur les deux
décisions de la mère de 10:20Z, transmises par la coordination ; rien d'autre ne change :
- **la liste fermée d'apparence vide (`APPARENCE_VIDE`, U+2800) est ramenée à une espace**, et non plus retirée. Raison,
  pour l'additif : ces caractères s'affichent comme une espace ; c'est le plus souvent à la place d'une espace qu'ils
  coupent un motif (« graine⠀factice »), et les ramener à une espace lit ce texte comme on le voit. Le prix : inséré au
  milieu d'un mot, un tel caractère le coupe en deux, comme le font déjà un tiret ou un soulignement ;
- **les motifs passent par le même normaliseur que le texte.** Un motif « litteral » l'était déjà. Un motif
  « expression_reguliere » l'est désormais aussi, sur ses **littéraux seuls** (`Normaliseur.normaliser_expression`) : les
  métacaractères, les classes et les échappements de classe sont gardés tels quels ; chaque suite de caractères littéraux
  (échappements de ponctuation `\\-`, `\\_`, `\\.` et suites `\\xHH`, `\\uHHHH`, `\\t`, `\\n`… compris) est normalisée comme le
  texte, puis réécrite échappée. Une construction que cette lecture ne sait pas tenir est refusée au chargement, jamais
  laissée telle quelle. La liste scellée ne change pas : c'est la garde qui s'adapte.

v3 (remplace `garde_motifs_na_v2`, `1e4fe266…`, archivé sans modification), sur les décisions de la mère de 08:54Z, 08:55Z et
08:59Z, transmises par la coordination :
- **caractère invisible** : la catégorie Unicode « Cf », plus les points « Default_Ignorable_Code_Point », pris **par
  propriété**, dans un fichier de données tiré par programme de `DerivedCoreProperties.txt` d'Unicode 15.1.0 (voie (b) ;
  aucune dépendance au module `regex`), plus une **liste fermée et déclarée** de caractères d'apparence vide qui ne sont
  pas ignorables (`APPARENCE_VIDE`, qui commence par U+2800). Cette liste est un écart franc à « par propriété », écrit ici
  et dans le rapport, pour l'additif. Les trois ensembles sont retirés du texte ;
- **tiret, soulignement, espace : une seule forme**. Chaque caractère de la catégorie « Pd » (tirets, tiret long compris),
  le signe moins U+2212 (gardé de la v2) et chaque caractère de la catégorie « Pc » (soulignement et connecteurs) devient
  une espace ; puis tout caractère que `str.isspace()` accepte (catégories Zs, Zl, Zp, dont l'espace insécable ;
  tabulation, fins de ligne LF, CR, VT, FF, NEL, séparateurs U+001C à U+001F) devient une espace ; toute suite d'espaces
  devient une seule espace. La garde compare sur cette forme ; **les octets d'origine restent ceux qui partent et ceux
  dont l'empreinte et la taille sont journalisées** ;
- **le texte trouvé** ne va qu'à la ligne « non envoyé » du journal (et à l'attribut `texte_trouve` de l'arrêt, jamais à
  son message) : inchangé depuis la v1.

Les données des ignorables sont lues à leur empreinte (`lire_donnees_ignorables`) ; elles sont refusées si elles sont
vides (le fichier source n'est pas encore versé), si leur version d'Unicode diffère de `unicodedata.unidata_version` de
l'interpréteur qui joue, ou si leurs plages sont mal formées. Sans données acceptées, ni la liste ni la garde ne se
construisent : aucun repli silencieux (R5).

Le reste est celui de la v2 : copie au dernier point avant l'envoi, empreinte prise sur la copie, deux familles, témoins
positifs, refus qui nomme la famille et le rang ; la vraie égalité entre le journal et ce que reçoit le noyau est au lot 4
(`verifier_avant_envoi`).

Format de la liste (`liste-motifs-na-v1`), inchangé : JSON, `{"format", "familles": [{"nom", "motifs": [{"rang", "type",
"motif", "temoin_positif"}]}]}`, familles « identité et dépôt » puis « composition et tenue », rangs 1, 2, 3… sans trou,
types « litteral » (normalisé comme le texte, cherché comme sous-chaîne ; vide ou blanc après normalisation : refusé) et
« expression_reguliere » (module `re`, appliquée au texte normalisé : minuscules repliées, aucun tiret, aucun
soulignement, aucune tabulation ni fin de ligne, une seule espace ; une expression qui attend un de ces caractères ne mord
plus sur son témoin, et le départ est refusé).

Format des données (`ignorables-unicode-na-v1`) : JSON, `{"format", "propriete": "Default_Ignorable_Code_Point",
"version_unicode", "source": {"chemin", "sha256", "commit", "en_tete"}, "plages": [[debut, fin], …], "total"}`. Un fichier
« vide » porte `"source": null` et `"plages": null` : il est refusé au chargement.

Bibliothèque standard seule.
"""

import dataclasses
import hashlib
import json
import os
import re
import unicodedata

VERSION = "garde-motifs-na-v4"
FORMAT_LISTE = "liste-motifs-na-v1"
FORMAT_DONNEES = "ignorables-unicode-na-v1"
PROPRIETE = "Default_Ignorable_Code_Point"
VERSION_UNICODE_ATTENDUE = "15.1.0"  # mère, 08:55Z : la version de l'interpréteur de la course
FAMILLES = ("identité et dépôt", "composition et tenue")
TYPES = ("litteral", "expression_reguliere")
NUMERO_ARRET = 16

# Liste fermée et déclarée (mère, 08:59Z) : caractères d'apparence vide qui ne sont ni « Cf », ni ignorables par défaut,
# ni des espaces au sens de `str.isspace()`. Raison : ils s'affichent comme un blanc et coupent un motif sans le montrer ;
# aucune propriété d'Unicode ne les rassemble. C'est un écart franc à « par propriété », porté à l'additif ; tout ajout est
# une version neuve de ce programme. v4 (mère, 10:20Z) : ces caractères sont **ramenés à une espace**, non retirés, parce
# qu'ils se lisent comme une espace et prennent le plus souvent sa place (« graine⠀factice » se lit « graine factice »).
APPARENCE_VIDE = (
    0x2800,  # BRAILLE PATTERN BLANK (catégorie So) : relevé par la vérification du modèle S
)
SIGNE_MOINS = 0x2212  # tiret hors de la catégorie Pd, gardé de la v2

_SONDES_ACCORD_VIDE = ("", " ", "x", "x y", "xx yy zz")
_ESPACES_MULTIPLES = re.compile(" {2,}")


class DonneesIgnorablesRefusees(ValueError):
    """Les données des ignorables ne sont pas acceptées : ni la liste ni la garde ne se construisent."""


class ListeMotifsRefusee(ValueError):
    """La liste des motifs ne tient pas son format ou son empreinte : la garde ne se construit pas."""


class VersionUnicodeDifferente(RuntimeError):
    """La version d'Unicode des données diffère de celle de l'interpréteur : refus."""


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


def _sans_double(erreur):
    def crochet(paires):
        d = {}
        for k, v in paires:
            if k in d:
                raise erreur(f"clé en double : {k!r}")
            d[k] = v
        return d
    return crochet


def verifier_version_interprete(version_donnees, version_interprete=None):
    """Refuse si la version d'Unicode des données diffère de celle de l'interpréteur (par défaut, celui qui joue)."""
    v = unicodedata.unidata_version if version_interprete is None else version_interprete
    if type(version_donnees) is not str or version_donnees != v:
        raise VersionUnicodeDifferente(f"version d'Unicode des données {version_donnees!r} différente de celle de "
                                       f"l'interpréteur {v!r} : refus")
    return v


@dataclasses.dataclass(frozen=True)
class DonneesIgnorables:
    sha256: str
    version_unicode: str
    source: dict
    plages: tuple
    points: frozenset


def lire_donnees_ignorables(octets, empreinte_attendue):
    """Lit les données des ignorables à leur empreinte ; refuse un fichier vide, une autre version d'Unicode que celle de
    l'interpréteur, une plage mal formée, un total faux."""
    if not isinstance(octets, (bytes, bytearray)):
        raise DonneesIgnorablesRefusees("les données se lisent en octets")
    octets = bytes(octets)
    sha = hashlib.sha256(octets).hexdigest()
    if type(empreinte_attendue) is not str or sha != empreinte_attendue:
        raise DonneesIgnorablesRefusees("empreinte des données des ignorables différente de celle qui est écrite")
    try:
        obj = json.loads(octets.decode("utf-8"), object_pairs_hook=_sans_double(DonneesIgnorablesRefusees))
    except (UnicodeDecodeError, json.JSONDecodeError) as e:
        raise DonneesIgnorablesRefusees(f"données illisibles ({type(e).__name__})") from None
    cles = {"format", "propriete", "version_unicode", "source", "plages", "total"}
    if not isinstance(obj, dict) or set(obj) != cles:
        raise DonneesIgnorablesRefusees("clés des données : " + ", ".join(sorted(cles)))
    if obj["format"] != FORMAT_DONNEES or obj["propriete"] != PROPRIETE:
        raise DonneesIgnorablesRefusees("format ou propriété inconnus")
    if obj["source"] is None or obj["plages"] is None:
        raise DonneesIgnorablesRefusees("données vides : le fichier source n'est pas versé ; rien ne se charge")
    if obj["version_unicode"] != VERSION_UNICODE_ATTENDUE:
        raise DonneesIgnorablesRefusees(f"version d'Unicode des données autre que {VERSION_UNICODE_ATTENDUE}")
    verifier_version_interprete(obj["version_unicode"])
    source = obj["source"]
    if (not isinstance(source, dict) or set(source) != {"chemin", "sha256", "commit", "en_tete"}
            or not all(type(source[k]) is str and source[k] for k in source)
            or re.fullmatch(r"[0-9a-f]{64}", source["sha256"]) is None):
        raise DonneesIgnorablesRefusees("source des données : chemin, empreinte, commit et en-tête exigés")
    plages = obj["plages"]
    if not isinstance(plages, list) or not plages:
        raise DonneesIgnorablesRefusees("plages vides ou invalides")
    rendu, points, fin_prec = [], set(), -1
    for p in plages:
        if (not isinstance(p, list) or len(p) != 2 or not all(type(x) is int for x in p)
                or not 0 <= p[0] <= p[1] <= 0x10FFFF or p[0] <= fin_prec):
            raise DonneesIgnorablesRefusees("plage mal formée, hors d'Unicode, non triée ou chevauchante")
        fin_prec = p[1]
        rendu.append((p[0], p[1]))
        points.update(range(p[0], p[1] + 1))
    if type(obj["total"]) is not int or obj["total"] != len(points):
        raise DonneesIgnorablesRefusees("total des points différent de la somme des plages")
    return DonneesIgnorables(sha, obj["version_unicode"], dict(source), tuple(rendu), frozenset(points))


def charger_donnees_ignorables(chemin, empreinte_attendue):
    with open(chemin, "rb") as f:
        return lire_donnees_ignorables(f.read(), empreinte_attendue)


class Normaliseur:
    """La normalisation de la garde (V9, l. 387 ; mère, 08:54Z à 08:59Z), sur des données acceptées."""

    def __init__(self, donnees):
        if not isinstance(donnees, DonneesIgnorables):
            raise DonneesIgnorablesRefusees("le normaliseur se construit sur des données lues par "
                                            "`lire_donnees_ignorables`")
        verifier_version_interprete(donnees.version_unicode)
        self.donnees = donnees
        self._retires = donnees.points  # v4 : la liste d'apparence vide n'est plus retirée, elle devient une espace
        self._en_espace = frozenset(APPARENCE_VIDE) | {SIGNE_MOINS}

    def _retirer(self, t):
        return "".join(ch for ch in t if ord(ch) not in self._retires and unicodedata.category(ch) != "Cf")

    def normaliser(self, texte):
        if type(texte) is not str:
            raise TypeError("la normalisation lit une chaîne")
        t = self._retirer(texte)
        t = unicodedata.normalize("NFKC", t)
        t = t.casefold()
        t = unicodedata.normalize("NFKC", t)
        t = self._retirer(t)
        t = "".join(" " if (unicodedata.category(ch) in ("Pd", "Pc") or ord(ch) in self._en_espace) else ch for ch in t)
        t = "".join(" " if ch.isspace() else ch for ch in t)
        t = _ESPACES_MULTIPLES.sub(" ", t)
        return t

    def normaliser_expression(self, motif):
        """Normalise les **littéraux seuls** d'une expression régulière (mère, 10:20Z) : chaque suite de caractères
        littéraux passe par `normaliser`, puis est réécrite échappée (`re.escape`) ; les métacaractères, les classes
        `[…]`, les échappements de classe (`\\b \\B \\d \\D \\s \\S \\w \\W \\A \\Z`), les groupes `(` et `(?:` et les
        quantificateurs sont gardés tels quels. Un littéral suivi d'un quantificateur est normalisé à part ; s'il devient
        plusieurs caractères, il est mis dans un groupe `(?:…)` pour que le quantificateur porte sur lui entier ; s'il
        disparaît, l'expression est refusée. Toute autre construction (groupe spécial `(?…)` autre que `(?:`, renvoi,
        échappement alphanumérique inconnu, classe non fermée) est refusée : `ExpressionNonNormalisable`."""
        if type(motif) is not str:
            raise ExpressionNonNormalisable("une expression est une chaîne")
        jetons = _decouper_expression(motif)
        rendu, i = [], 0
        while i < len(jetons):
            genre, valeur = jetons[i]
            if genre != "lit":
                rendu.append(valeur)
                i += 1
                continue
            j = i
            while j < len(jetons) and jetons[j][0] == "lit":
                j += 1
            quantifie = j < len(jetons) and jetons[j][0] == "quant"
            corps = "".join(v for _, v in jetons[i:(j - 1 if quantifie else j)])
            if corps:
                rendu.append(re.escape(self.normaliser(corps)))
            if quantifie:
                dernier = self.normaliser(jetons[j - 1][1])
                if not dernier:
                    raise ExpressionNonNormalisable("un littéral quantifié disparaît à la normalisation")
                rendu.append(re.escape(dernier) if len(dernier) == 1 else "(?:" + re.escape(dernier) + ")")
            i = j
        return "".join(rendu)


class ExpressionNonNormalisable(ValueError):
    """Une expression régulière que la normalisation des littéraux ne sait pas tenir : refusée, jamais gardée telle quelle."""


_QUANTIFICATEUR_ACCOLADES = re.compile(r"\{\d+(?:,\d*)?\}\??")
_ECHAPPEMENTS_META = "bBdDsSwWAZ"
_ECHAPPEMENTS_LITTERAUX = {"t": "\t", "n": "\n", "r": "\r", "f": "\f", "v": "\v", "a": "\a"}


def _decouper_expression(p):
    """Découpe une expression en jetons : (« lit », caractère littéral), (« meta », texte gardé), (« quant », texte gardé)."""
    jetons, i, n = [], 0, len(p)
    while i < n:
        c = p[i]
        if c == "\\":
            if i + 1 >= n:
                raise ExpressionNonNormalisable("échappement final")
            d = p[i + 1]
            if d in _ECHAPPEMENTS_META:
                jetons.append(("meta", "\\" + d))
                i += 2
            elif d in "xuU":
                largeur = {"x": 2, "u": 4, "U": 8}[d]
                hexa = p[i + 2:i + 2 + largeur]
                if len(hexa) != largeur or re.fullmatch(r"[0-9A-Fa-f]+", hexa) is None:
                    raise ExpressionNonNormalisable("échappement hexadécimal mal formé")
                jetons.append(("lit", chr(int(hexa, 16))))
                i += 2 + largeur
            elif d in _ECHAPPEMENTS_LITTERAUX:
                jetons.append(("lit", _ECHAPPEMENTS_LITTERAUX[d]))
                i += 2
            elif d.isascii() and d.isalnum():
                raise ExpressionNonNormalisable("échappement non pris en charge (renvoi, nom, propriété…)")
            else:
                jetons.append(("lit", d))  # ponctuation échappée : un littéral
                i += 2
        elif c == "[":
            j = i + 1
            if j < n and p[j] == "^":
                j += 1
            if j < n and p[j] == "]":
                j += 1
            while j < n and p[j] != "]":
                j += 2 if p[j] == "\\" else 1
            if j >= n:
                raise ExpressionNonNormalisable("classe non fermée")
            jetons.append(("meta", p[i:j + 1]))
            i = j + 1
        elif c == "(":
            if p.startswith("(?:", i):
                jetons.append(("meta", "(?:"))
                i += 3
            elif p.startswith("(?", i):
                raise ExpressionNonNormalisable("groupe spécial non pris en charge")
            else:
                jetons.append(("meta", "("))
                i += 1
        elif c in "*+?":
            q = c
            i += 1
            if i < n and p[i] in "?+":
                q += p[i]
                i += 1
            jetons.append(("quant", q))
        elif c == "{":
            m = _QUANTIFICATEUR_ACCOLADES.match(p, i)
            if m is not None:
                jetons.append(("quant", m.group(0)))
                i = m.end()
            else:
                jetons.append(("lit", c))
                i += 1
        elif c in ".^$|)":
            jetons.append(("meta", c))
            i += 1
        else:
            jetons.append(("lit", c))
            i += 1
    return jetons


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
    normaliseur: Normaliseur


def _compiler(normaliseur, famille, rang, type_, motif):
    if type_ == "litteral":
        forme = normaliseur.normaliser(motif)
        if not forme.strip():
            raise ListeMotifsRefusee(f"famille « {famille} », rang {rang} : motif littéral vide ou blanc après "
                                     "normalisation")
        return forme
    try:
        re.compile(motif)  # l'expression écrite doit d'abord être valide telle quelle
        forme = re.compile(normaliseur.normaliser_expression(motif))  # v4 : ses littéraux normalisés comme le texte
    except re.error as e:
        raise ListeMotifsRefusee(f"famille « {famille} », rang {rang} : expression invalide ({e})") from None
    except ExpressionNonNormalisable as e:
        raise ListeMotifsRefusee(f"famille « {famille} », rang {rang} : {e}") from None
    for sonde in _SONDES_ACCORD_VIDE:
        for m in forme.finditer(sonde):
            if m.end() == m.start():
                raise ListeMotifsRefusee(f"famille « {famille} », rang {rang} : expression qui peut rendre un accord "
                                         "de longueur nulle")
    return forme


def lire_liste_motifs(octets, empreinte_attendue, normaliseur):
    """Lit une liste à son empreinte (arrêt n° 14 pour la liste), sur un normaliseur construit sur des données acceptées."""
    if not isinstance(normaliseur, Normaliseur):
        raise DonneesIgnorablesRefusees("la liste se lit avec un normaliseur construit sur des données acceptées")
    if not isinstance(octets, (bytes, bytearray)):
        raise ListeMotifsRefusee("la liste se lit en octets")
    octets = bytes(octets)
    sha = hashlib.sha256(octets).hexdigest()
    if type(empreinte_attendue) is not str or sha != empreinte_attendue:
        raise ListeMotifsRefusee("empreinte de la liste des motifs différente de celle qui est écrite")
    try:
        obj = json.loads(octets.decode("utf-8"), object_pairs_hook=_sans_double(ListeMotifsRefusee))
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
            forme = _compiler(normaliseur, attendu, i, m["type"], m["motif"])
            rendus.append(Motif(attendu, i, m["type"], m["motif"], m["temoin_positif"], forme))
        rendu.append((attendu, tuple(rendus)))
    return ListeMotifs(sha, tuple(rendu), normaliseur)


def charger_liste_motifs(chemin, empreinte_attendue, normaliseur):
    with open(chemin, "rb") as f:
        return lire_liste_motifs(f.read(), empreinte_attendue, normaliseur)


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

    def normaliser(self, texte):
        return self.liste.normaliseur.normaliser(texte)

    def motifs(self):
        for _nom, motifs in self.liste.familles:
            yield from motifs

    def verifier_temoins(self):
        """Rejouée à chaque départ : chaque motif doit mordre sur son témoin positif."""
        for motif in self.motifs():
            if motif.chercher(self.normaliser(motif.temoin_positif)) is None:
                raise TemoinPositifManque(motif.famille, motif.rang)

    def examiner(self, texte):
        """Rend le premier constat (famille dans l'ordre, puis rang), ou None."""
        n = self.normaliser(texte)
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
        octets = bytes(requete)  # une seule lecture du tampon de l'appelant
        empreinte = hashlib.sha256(octets).hexdigest()  # sur la copie, au moment de la copie
        try:
            texte = octets.decode("utf-8")
        except UnicodeDecodeError:
            raise RequeteIllisible("requête qui n'est pas en UTF-8 valide : refusée") from None
        self.garder_texte(texte)
        return RequeteGardee(octets, empreinte, len(octets))


def verifier_avant_envoi(requete_gardee, octets_a_envoyer):
    """Égalité : ce qui part a l'empreinte de ce que la garde a lu ; sinon refus. Pour le lot 4, qui l'appelle sur les
    octets qu'il remet à `super().appel` (conception v4, § 2.3, pas 5)."""
    if not isinstance(octets_a_envoyer, (bytes, bytearray, memoryview)):
        raise EcartApresGarde("rien d'autre que des octets ne part")
    if hashlib.sha256(bytes(octets_a_envoyer)).hexdigest() != requete_gardee.sha256:
        raise EcartApresGarde("les octets à envoyer diffèrent de ceux que la garde a lus : envoi refusé")


def envoyer_apres_garde(garde, requete, envoyer, journal, meta=None):
    """Garde, journal, envoi, dans cet ordre. Un refus : une ligne « non envoyé » (famille, rang, texte trouvé) au journal,
    puis l'arrêt n° 16 levé, sans envoi. Une ligne d'envoi qui ne s'écrit pas : rien ne part. `envoyer` reçoit les octets
    d'origine que la garde a lus (un objet `bytes`) ; la forme normalisée ne sert qu'à la comparaison. La vraie égalité
    avec ce que reçoit le noyau est au lot 4."""
    meta = dict(meta or {})
    try:
        rg = garde.garder_requete(requete)
    except ArretMotifInterdit as arret:
        journal({**meta, "evenement": "non envoyé", "arret": NUMERO_ARRET, "famille": arret.famille,
                 "rang": arret.rang, "texte_trouve": arret.texte_trouve})
        raise
    journal({**meta, "evenement": "envoi", "taille": rg.taille, "sha256": rg.sha256})
    return envoyer(rg.octets)


def empreinte_programme():
    """L'empreinte de ce programme, que le lanceur épingle avec celles de la liste et des données (arrêt n° 14)."""
    with open(os.path.abspath(__file__), "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()
