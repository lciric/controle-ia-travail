"""Véhicule NA-1, lot 5 — lecteur de fiches neuf (`lecteur_fiches_na_v1`) : syntaxes déclarées, grammaire par étiquettes
ancrées, sans ordre exigé.

Lettre : V9 (`864f39a7…`), l. 92 à 101 (classes d'issue d'appel ; « fiches rendues » par programme) ; conception du véhicule
v5 (`1b7f6822…`), § 0 bis (07:46Z, mot 3 : grammaire par étiquettes ancrées ; « dans l'ordre » retiré, 07:51Z), § 2.4
(lecteur neuf ; ni `preparer`, ni `valider_contenu`, ni `fiches_du_texte`), § 2.13 (la lecture rend un objet dès qu'un texte
est rendu), § 5.4, § 6.2 (grammaire par étiquettes ancrées), § 9, point 20 ; relevé du lot 0 (`10ac79ec…`), Q6.

**Syntaxes déclarées** (forme proposée ici, à écrire à l'additif ; la lettre ne fixe que leur existence) :

1. *Objet structuré* : un objet JSON par fiche, dans un bloc clôturé (```` ```json ```` ou ```` ``` ```` sans langue) ou nu,
   en tête de ligne. Un objet qui porte une clé `fiches` (une liste) sans porter aucun des douze noms est une enveloppe :
   ses éléments sont lus. Une liste d'objets aussi. Les valeurs sont gardées telles que le JSON les donne (le type est
   vérifié par `contrat_fiche_na_v1`).
2. *Étiquettes ancrées* : une ligne dont le début, après une parure de tête facultative (titre `#` à `######`, puce `-`,
   `*`, `+`, numéro `1.` ou `1)`, citation `>`), porte un nom en minuscules ASCII (lettres, chiffres, soulignements, sans
   soulignement final), entouré ou non
   d'une même parure (`**`, `__`, `*`, `` ` ``), puis deux-points suivis d'un blanc ou de la fin de ligne ; ou une ligne de
   titre qui ne porte que ce nom. Les lignes « champ : valeur » sont la parure nue de cette grammaire. L'ordre des
   étiquettes n'est pas exigé (mot 3 ; la partie servie nomme les champs sans en imposer un).

**Valeur d'une étiquette** : le reste de la ligne après les deux-points (et la parure fermante, si elle les suit), puis les
lignes suivantes jusqu'à l'étiquette suivante ou la fin du morceau, jointes par une fin de ligne ; les blancs de tête et de
queue de la valeur entière sont retirés (et rien d'autre). Aucun caviardage, aucune correction, aucun complément. Les
lignes qui suivent la dernière étiquette d'un morceau appartiennent à sa valeur : une prose finale ne s'en sépare que par
une règle ou un titre ; rien n'est retiré. Les fins de ligne `\\r\\n` et `\\r` sont lues comme `\\n`.

**Morceaux** : un bloc clôturé, un objet JSON nu, ou un passage de texte entre deux séparateurs (ligne de règle `---`,
`***`, `___`, ou ligne de titre qui n'est pas une étiquette). Une fiche est reconnue dans un morceau quand les douze noms
du contrat y figurent **chacun une fois exactement**. Un nom en double, ou un nom manquant : le morceau n'est pas une
fiche ; il est compté (« morceau non reconnu », avec sa cause), jamais complété ni réparé. Une étiquette dont le nom
n'est pas l'un des douze est un **champ en plus** de la fiche du morceau (il l'enverra au coffre, § 2.4). Une valeur
libre qui porte le nom d'un autre champ ailleurs qu'en tête de ligne n'est pas une étiquette ; en tête de ligne, elle en
est une, et le morceau porte alors un nom en double : refusé, jamais lu faux.

Le lecteur rend **toujours** un objet `Lecture` pour un texte rendu, avec ou sans fiche (§ 2.13). Aucun message d'erreur ne
recopie un octet du texte. Bibliothèque standard, et `requete_na_v3` (les douze champs, une seule source).
"""

import dataclasses
import json
import re

from pole import requete_na_v3 as rq

VERSION = "lecteur-fiches-na-v1"
CHAMPS = rq.CHAMPS_FICHE
SYNTAXE_OBJET = "objet structuré"
SYNTAXE_ETIQUETTES = "étiquettes ancrées"
CAUSE_MANQUANT = "champ manquant"
CAUSE_DOUBLE = "champ en double"
CLE_ENVELOPPE = "fiches"

_FINS_DE_LIGNE = re.compile(r"\r\n|\n|\r")
_PARURES = ("**", "__", "*", "`")
_ETIQUETTE = re.compile(
    r"^[ \t]*(?:(?P<titre>#{1,6})[ \t]+|(?:[-*+]|\d{1,2}[.)])[ \t]+|>[ \t]*)?"
    r"(?P<ouv>\*\*|__|\*|`)?(?P<nom>[a-z](?:[a-z0-9_]*[a-z0-9])?)(?P<ferm1>\*\*|__|\*|`)?"
    r"[ \t]*(?:(?P<deux>:)(?=[ \t]|$|\*\*|__|\*|`)(?P<ferm2>\*\*|__|\*|`)?)?(?P<reste>.*)$")
_REGLE = re.compile(r"^[ \t]*([-*_])(?:[ \t]*\1){2,}[ \t]*$")
_TITRE = re.compile(r"^[ \t]*#{1,6}(?:[ \t]|$)")
_CLOTURE = re.compile(r"^ {0,3}```(?P<info>[^`]*)$")


class LectureRefusee(TypeError):
    """Le lecteur ne lit qu'un texte (une chaîne) ; le message ne recopie rien."""


@dataclasses.dataclass(frozen=True)
class FicheLue:
    """Une fiche reconnue : ses douze valeurs telles que lues, dans l'ordre du contrat, et les noms de ses champs en plus."""

    rang: int
    syntaxe: str
    champs: tuple  # ((nom, valeur), …), les douze, dans l'ordre du contrat
    extras: tuple  # noms des champs en plus, dans l'ordre de lecture

    def contenu(self):
        return dict(self.champs)

    def valeur(self, nom):
        return dict(self.champs)[nom]


@dataclasses.dataclass(frozen=True)
class Lecture:
    """Ce que rend le lecteur pour un texte rendu : les fiches reconnues (peut-être aucune) et les morceaux non reconnus
    (leurs causes seules)."""

    texte_rendu: bool
    fiches: tuple
    non_reconnus: tuple  # causes, une par morceau non reconnu

    @property
    def a_des_fiches(self):
        return len(self.fiches) > 0


class _ObjetJSON(dict):
    """Un objet JSON qui garde la trace de ses clés en double (au lieu de garder la dernière en silence)."""

    doubles = ()


def _paires(paires):
    o = _ObjetJSON()
    doubles = []
    for k, v in paires:
        if k in o:
            doubles.append(k)
        o[k] = v
    o.doubles = tuple(doubles)
    return o


def _charger_json(texte):
    return json.loads(texte, object_pairs_hook=_paires)


def _etiquette(ligne):
    """Rend (nom, valeur en ligne) si la ligne est une étiquette ancrée, sinon None."""
    m = _ETIQUETTE.match(ligne)
    if m is None:
        return None
    ouv, f1, f2 = m.group("ouv"), m.group("ferm1"), m.group("ferm2")
    if ouv is None:
        if f1 is not None or f2 is not None:
            return None
    else:
        if (f1 is None) == (f2 is None) or (f1 or f2) != ouv:
            return None
    reste = m.group("reste")
    if m.group("deux") is not None:
        return m.group("nom"), reste.strip(" \t")
    if m.group("titre") is not None and f2 is None and reste.strip(" \t") == "":
        return m.group("nom"), ""
    return None


def _separateur(ligne):
    return _REGLE.match(ligne) is not None or (_TITRE.match(ligne) is not None and _etiquette(ligne) is None)


def _lire_morceau_etiquettes(lignes):
    """Rend ("fiche", champs, extras), ("non", cause) ou None (aucune étiquette des douze : de la prose)."""
    entrees = []  # [nom, [lignes de valeur]]
    for ligne in lignes:
        e = _etiquette(ligne)
        if e is not None:
            entrees.append([e[0], [e[1]]])
        elif entrees:
            entrees[-1][1].append(ligne)
    noms = [n for n, _ in entrees]
    if not any(n in CHAMPS for n in noms):
        return None
    vus = [n for n in noms if n in CHAMPS]
    if len(vus) != len(set(vus)):
        return ("non", CAUSE_DOUBLE)
    if set(vus) != set(CHAMPS):
        return ("non", CAUSE_MANQUANT)
    valeurs = {n: "\n".join(v).strip(" \t\n") for n, v in entrees if n in CHAMPS}
    extras = tuple(n for n in noms if n not in CHAMPS)
    return ("fiche", tuple((c, valeurs[c]) for c in CHAMPS), extras)


def _candidats_json(valeur):
    if isinstance(valeur, dict) and CLE_ENVELOPPE in valeur and isinstance(valeur[CLE_ENVELOPPE], list) \
            and not any(c in valeur for c in CHAMPS):
        return [v for v in valeur[CLE_ENVELOPPE] if isinstance(v, dict)]
    if isinstance(valeur, dict):
        return [valeur]
    if isinstance(valeur, list):
        return [v for v in valeur if isinstance(v, dict)]
    return []


def _lire_objet(o):
    if not any(c in o for c in CHAMPS):
        return None
    if any(d in CHAMPS for d in getattr(o, "doubles", ())):
        return ("non", CAUSE_DOUBLE)
    if not all(c in o for c in CHAMPS):
        return ("non", CAUSE_MANQUANT)
    extras = tuple(k for k in o if k not in CHAMPS) + tuple(d for d in getattr(o, "doubles", ()) if d not in CHAMPS)
    return ("fiche", tuple((c, o[c]) for c in CHAMPS), extras)


def _morceaux(lignes):
    """Découpe le texte en morceaux : ("json", valeur) ou ("texte", [lignes])."""
    rendu, courant, i, n = [], [], 0, len(lignes)
    decodeur = json.JSONDecoder(object_pairs_hook=_paires)

    def clore():
        if courant:
            rendu.append(("texte", list(courant)))
            courant.clear()

    while i < n:
        ligne = lignes[i]
        m = _CLOTURE.match(ligne)
        if m is not None:
            fin = next((j for j in range(i + 1, n) if re.match(r"^ {0,3}```[ \t]*$", lignes[j])), None)
            if fin is not None:
                clore()
                corps = "\n".join(lignes[i + 1:fin])
                info = m.group("info").strip().lower()
                valeur, lu = None, False
                if info in ("json", ""):
                    try:
                        valeur, lu = _charger_json(corps), True
                    except ValueError:
                        lu = False
                rendu.append(("json", valeur) if lu else ("texte", lignes[i + 1:fin]))
                i = fin + 1
                continue
        if ligne.lstrip(" \t")[:1] in ("{", "["):
            reste = "\n".join(lignes[i:])
            debut = len(ligne) - len(ligne.lstrip(" \t"))
            try:
                valeur, fin_car = decodeur.raw_decode(reste, debut)
            except ValueError:
                valeur = None
            else:
                apres = reste[fin_car:]
                coupure = apres.find("\n")
                queue = apres if coupure < 0 else apres[:coupure]
                if queue.strip(" \t") == "":
                    clore()
                    rendu.append(("json", valeur))
                    i += reste[:fin_car].count("\n") + 1
                    continue
        if _separateur(ligne):
            clore()
        else:
            courant.append(ligne)
        i += 1
    clore()
    return rendu


def lire_fiches(texte):
    """Lit les fiches d'une réponse ; rend toujours une `Lecture` pour un texte (une chaîne), vide comprise."""
    if type(texte) is not str:
        raise LectureRefusee("le lecteur ne lit qu'un texte rendu (une chaîne)")
    lignes = _FINS_DE_LIGNE.split(texte)
    fiches, non = [], []
    for sorte, contenu in _morceaux(lignes):
        if sorte == "json":
            issues = [_lire_objet(o) for o in _candidats_json(contenu)]
            syntaxe = SYNTAXE_OBJET
        else:
            issues = [_lire_morceau_etiquettes(contenu)]
            syntaxe = SYNTAXE_ETIQUETTES
        for issue in issues:
            if issue is None:
                continue
            if issue[0] == "non":
                non.append(issue[1])
            else:
                fiches.append(FicheLue(len(fiches) + 1, syntaxe, issue[1], issue[2]))
    return Lecture(True, tuple(fiches), tuple(non))
