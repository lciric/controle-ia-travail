"""Véhicule NA-1, lot 7 — les deux outils de la session à part et les recherches de la preuve de quarantaine
(`quarantaine_na_v1`).

Lettre : V9 (`864f39a7…`), l. 82, l. 119 (garde-fou 2), l. 125 (limite), l. 388 et 389 (arrêts n° 17 et 18) ; conception
du véhicule v5 (`1b7f6822…`), § 2.6 (« deux outils à part »), § 2.15 (branche orpheline, vérifiée par le graphe des
commits, sans l'ouvrir ; journal des lectures), § 6.1 (n° 17, n° 18), § 6.2 (branche orpheline, sans l'ouvrir ; M4 sans
cumul par clé) ; § 9, point 13.

**Outil 1, « branche orpheline »** (`verifier_branche_orpheline`) : il demande au dépôt l'ancêtre commun du commit donné et
de `main`, puis du même commit et de chaque branche liée à `main` (une référence qui a un ancêtre commun avec `main`). Il
ne passe que trois sous-commandes de `git`, en liste fermée : `rev-parse` (le commit existe et est un commit),
`for-each-ref` (les noms des références), `merge-base` (le graphe des commits). **Aucune ne lit un objet de fichier** ;
toute autre sous-commande est refusée par le programme avant d'être lancée (`CommandeGitRefusee`). Aucun ancêtre commun :
la branche est orpheline. Un ancêtre commun : `ArretQuarantaineRompueNA17` par `exiger_branche_orpheline`, et l'état 2 est
refusé ; c'est un point pour la mère avant toute lecture.

**Outil 2, « journal des lectures contre la liste »** : la liste nominative des lecteurs, scellée ; un journal des lectures
en ajout seul, scellé à la fin ; `ouvrir_en_quarantaine` refuse un lecteur absent de la liste (n° 18), consigne le refus,
et **écrit la ligne avant d'appeler l'ouverture** ; `controler_lectures` confronte le journal à des lectures constatées
(une ligne par ouverture, écrite avant elle, par un rôle inscrit) et rend ce qui est à porter à Lazar.

**Recherches** (preuve du n° 17 et garde « M4 sans cumul par clé ») : `rechercher_textes` cherche des chaînes données
(noms d'usage des clés, noms des champs du cumul par clé, empreintes) dans des fichiers et des dossiers ; `rechercher_empreintes`
cherche en plus les fichiers dont l'empreinte est l'une des empreintes données. Elles rendent des chemins et des comptes,
jamais un contenu.

**Limite, dite sans forcer** (V9, l. 125) : la règle d'ouverture se tient par procédure et par journal ; une lecture hors
règle se constate, elle ne s'empêche pas toujours. Bibliothèque standard, et `commun_na_lot7_v1`.
"""

import dataclasses
import datetime
import os
import re
import subprocess

from pole import commun_na_lot7_v1 as cm
from pole.export_na_v1 import ArretQuarantaineRompueNA17

VERSION = "quarantaine-na-v1"
SOUS_COMMANDES_GIT = ("rev-parse", "merge-base", "for-each-ref")
_HEX = re.compile(r"^[0-9a-f]{7,64}$")
_REF = re.compile(r"^[A-Za-z0-9._/-]{1,200}$")


class CommandeGitRefusee(RuntimeError):
    """Une sous-commande de `git` hors de la liste fermée : refusée avant d'être lancée."""


class BrancheRefusee(RuntimeError):
    """Une entrée que l'outil ne lit pas (commit inconnu, référence mal formée, sortie de `git` imprévue)."""


class ArretLectureHorsListeNA18(RuntimeError):
    """Arrêt n° 18 de la V9 : une lecture en quarantaine non consignée, ou par un lecteur absent de la liste nominative.
    L'ouverture est refusée là où un programme la tient ; constatée après coup, elle est consignée et portée à Lazar."""

    numero = 18
    nom = "lecture hors liste"

    def __init__(self, cause):
        super().__init__(f"arrêt n° 18, {self.nom} : {cause} ; consigné, porté à Lazar")
        self.cause = cause


# --- outil 1 : branche orpheline ----------------------------------------------------------------------------------------

class Git:
    """Lanceur de `git` à liste fermée ; garde chaque commande lancée (constat)."""

    def __init__(self, depot, executable="git"):
        if not os.path.isdir(depot):
            raise BrancheRefusee("dépôt absent")
        self.depot, self.executable, self.commandes = depot, executable, []

    def __call__(self, sous_commande, *args):
        if sous_commande not in SOUS_COMMANDES_GIT:
            raise CommandeGitRefusee(f"sous-commande hors de la liste fermée : {sous_commande}")
        for a in args:
            if type(a) is not str or a.startswith("-") and a not in ("--all", "--verify", "--quiet", "--format=%(refname)"):
                raise CommandeGitRefusee("argument hors de la liste fermée")
        argv = [self.executable, "-C", self.depot, sous_commande, *args]
        self.commandes.append((sous_commande,) + tuple(args))
        env = {k: v for k, v in os.environ.items() if not k.startswith("GIT_")}
        env.update(GIT_CONFIG_NOSYSTEM="1", GIT_TERMINAL_PROMPT="0", LC_ALL="C")
        p = subprocess.run(argv, capture_output=True, text=True, env=env, timeout=60)
        return p.returncode, p.stdout


def _commit(git, nom):
    if type(nom) is not str or not (_HEX.match(nom) or _REF.match(nom)):
        raise BrancheRefusee("nom de commit ou de référence mal formé")
    code, sortie = git("rev-parse", "--verify", "--quiet", nom + "^{commit}")
    ident = sortie.strip()
    if code != 0 or not re.fullmatch(r"[0-9a-f]{40}|[0-9a-f]{64}", ident):
        raise BrancheRefusee(f"pas un commit du dépôt : {nom}")
    return ident


def _ancetres_communs(git, a, b):
    code, sortie = git("merge-base", "--all", a, b)
    if code == 0:
        return tuple(sortie.split())
    if code == 1 and not sortie.strip():
        return ()
    raise BrancheRefusee("sortie de `merge-base` imprévue")


@dataclasses.dataclass(frozen=True)
class ConstatBranche:
    commit: str
    principale: str
    orpheline: bool
    ancetres_avec_principale: tuple
    branches_liees: tuple          # références qui ont un ancêtre commun avec la principale
    ancetres_avec_liees: tuple     # ((référence, (ancêtres…)), …), non vides seulement
    commandes: tuple               # constat : les seules commandes lancées


def verifier_branche_orpheline(depot, commit, principale="main", git=None):
    """Outil 1. Rend un `ConstatBranche` ; n'ouvre aucun fichier de la branche, n'en lit aucun objet de fichier."""
    git = git or Git(depot)
    c = _commit(git, commit)
    m = _commit(git, principale)
    avec_m = _ancetres_communs(git, c, m)
    code, sortie = git("for-each-ref", "--format=%(refname)")
    if code != 0:
        raise BrancheRefusee("sortie de `for-each-ref` imprévue")
    liees, avec_liees = [], []
    for ref in sorted(sortie.split()):
        if not _REF.match(ref) or ref.startswith("refs/tags/"):
            continue
        r = _commit(git, ref)
        if r == c:  # la référence de la branche elle-même : jugée par ses ancêtres avec la principale
            continue
        if _ancetres_communs(git, r, m):
            liees.append(ref)
            a = _ancetres_communs(git, c, r)
            if a:
                avec_liees.append((ref, a))
    orpheline = not avec_m and not avec_liees
    return ConstatBranche(c, m, orpheline, avec_m, tuple(liees), tuple(avec_liees), tuple(git.commandes))


def exiger_branche_orpheline(depot, commit, principale="main", git=None):
    """Arrêt n° 17 si la branche a un ancêtre commun avec `main` ou une branche liée : l'état 2 est refusé."""
    constat = verifier_branche_orpheline(depot, commit, principale, git)
    if not constat.orpheline:
        raise ArretQuarantaineRompueNA17("la branche de quarantaine a un ancêtre commun avec la branche principale ou une "
                                         "branche liée ; l'état 2 est refusé, point pour la mère")
    return constat


# --- outil 2 : journal des lectures contre la liste ---------------------------------------------------------------------

FORMAT_LISTE = "liste-nominative-lecteurs-na-v1"
_ROLE = re.compile(r"^[a-z0-9][a-z0-9 _-]{0,60}$")


def lire_liste_nominative(chemin, empreinte_attendue):
    """La liste nominative, scellée, à l'empreinte que la mère donne : {"format", "lecteurs": [rôle, …]}."""
    try:
        objet = cm.lire_json_scelle(chemin, empreinte_attendue)
    except cm.ScelleRefuse as e:
        raise ArretLectureHorsListeNA18(f"liste nominative absente, non scellée ou d'une autre empreinte ({e})") from None
    lecteurs = objet.get("lecteurs") if isinstance(objet, dict) else None
    if set(objet or {}) != {"format", "lecteurs"} or objet.get("format") != FORMAT_LISTE or not isinstance(lecteurs, list) \
            or not lecteurs or not all(type(r) is str and _ROLE.match(r) for r in lecteurs) \
            or len(set(lecteurs)) != len(lecteurs):
        raise ArretLectureHorsListeNA18("liste nominative hors de sa forme")
    return frozenset(lecteurs)


class JournalLectures(cm.FichierAjoutSeul):
    """Le journal des lectures en quarantaine : une ligne avant chaque ouverture ; les refus y sont consignés."""

    CHAMPS_PERMIS = ("evenement", "role", "heure", "commit", "empreintes", "cause")
    VERSION = "journal-lectures-quarantaine-na-v1"
    EVENEMENTS = ("ouverture", "refus")


def _heure(horloge):
    h = (horloge or (lambda: datetime.datetime.now(datetime.timezone.utc)))()
    return h.strftime("%Y-%m-%dT%H:%M:%S.%fZ")


def _verifier_ouverture(role, commit, empreintes):
    if type(role) is not str or not _ROLE.match(role):
        raise ArretLectureHorsListeNA18("rôle mal formé")
    if type(commit) is not str or not re.fullmatch(r"[0-9a-f]{7,64}", commit):
        raise ArretLectureHorsListeNA18("commit mal formé")
    if not isinstance(empreintes, (list, tuple)) or not empreintes \
            or not all(type(e) is str and re.fullmatch(r"[0-9a-f]{64}", e) for e in empreintes):
        raise ArretLectureHorsListeNA18("empreintes de ce qui est ouvert mal formées")


def ouvrir_en_quarantaine(journal, lecteurs, role, commit, empreintes, ouvrir, horloge=None):
    """Arrêt n° 18 là où le programme tient l'ouverture : un rôle hors de la liste est refusé (le refus est consigné) ; un
    rôle inscrit voit sa ligne écrite **avant** l'appel de `ouvrir()`, dont le résultat est rendu tel quel."""
    if not isinstance(journal, JournalLectures):
        raise ArretLectureHorsListeNA18("journal des lectures d'un autre type")
    _verifier_ouverture(role, commit, empreintes)
    if role not in lecteurs:
        journal.ajouter({"evenement": "refus", "role": role, "heure": _heure(horloge), "commit": commit,
                         "empreintes": list(empreintes), "cause": "lecteur absent de la liste nominative"})
        raise ArretLectureHorsListeNA18("lecteur absent de la liste nominative ; ouverture refusée")
    journal.ajouter({"evenement": "ouverture", "role": role, "heure": _heure(horloge), "commit": commit,
                     "empreintes": list(empreintes)})
    return ouvrir()


@dataclasses.dataclass(frozen=True)
class ConstatLectures:
    conformes: int
    sans_ligne: tuple          # indices des lectures constatées sans ligne écrite avant elles
    hors_liste: tuple          # indices des lectures constatées par un rôle absent de la liste
    lignes_hors_liste: tuple   # rangs des lignes « ouverture » d'un rôle absent de la liste
    refus_consignes: int

    @property
    def a_porter_a_lazar(self):
        return bool(self.sans_ligne or self.hors_liste or self.lignes_hors_liste)


def controler_lectures(chemin_journal, lecteurs, lectures_constatees):
    """Confronte le journal scellé à des lectures constatées [{role, heure, commit, empreinte}] : chaque lecture a sa ligne
    « ouverture », écrite avant elle (heure au plus égale), par le même rôle, au même commit, qui nomme l'empreinte ouverte.
    Rend un `ConstatLectures` ; ne recopie rien de ce qui a été lu."""
    lignes = cm.relire_ajout_seul(chemin_journal, exiger_sceau=True)
    ouvertures = [l for l in lignes if l.get("evenement") == "ouverture"]
    refus = sum(1 for l in lignes if l.get("evenement") == "refus")
    if any(l.get("evenement") not in JournalLectures.EVENEMENTS for l in lignes):
        raise ArretLectureHorsListeNA18("journal des lectures : événement hors de la liste fermée")
    lignes_hors = tuple(l["rang"] for l in ouvertures if l.get("role") not in lecteurs)
    sans, hors, ok = [], [], 0
    for i, lc in enumerate(lectures_constatees):
        if not isinstance(lc, dict) or set(lc) != {"role", "heure", "commit", "empreinte"}:
            raise ArretLectureHorsListeNA18("lecture constatée hors de sa forme")
        if lc["role"] not in lecteurs:
            hors.append(i)
            continue
        trouve = any(l["role"] == lc["role"] and l["commit"] == lc["commit"] and lc["empreinte"] in l["empreintes"]
                     and l["heure"] <= lc["heure"] for l in ouvertures)
        if trouve:
            ok += 1
        else:
            sans.append(i)
    return ConstatLectures(ok, tuple(sans), tuple(hors), lignes_hors, refus)


def exiger_lectures_conformes(chemin_journal, lecteurs, lectures_constatees):
    constat = controler_lectures(chemin_journal, lecteurs, lectures_constatees)
    if constat.a_porter_a_lazar:
        raise ArretLectureHorsListeNA18(f"{len(constat.sans_ligne)} lecture(s) sans ligne, {len(constat.hors_liste)} par un "
                                        f"lecteur absent de la liste, {len(constat.lignes_hors_liste)} ligne(s) d'un rôle "
                                        "absent de la liste")
    return constat


# --- recherches de la preuve de quarantaine -----------------------------------------------------------------------------

def _fichiers(chemins):
    for c in chemins:
        if os.path.isfile(c):
            yield c
        elif os.path.isdir(c):
            for racine, dossiers, fichiers in os.walk(c):
                dossiers.sort()
                for f in sorted(fichiers):
                    yield os.path.join(racine, f)
        else:
            raise FileNotFoundError(f"chemin de recherche absent : {os.path.basename(c)}")


def rechercher_textes(chemins, textes):
    """Les fichiers (sous `chemins`) qui contiennent l'une des chaînes `textes` (octets UTF-8 exacts) ; rend
    {chemin: nombre de chaînes trouvées}, jamais quelle chaîne ni un contenu."""
    aiguilles = [t.encode("utf-8") for t in textes if type(t) is str and t]
    if len(aiguilles) != len(textes):
        raise ValueError("des chaînes non vides à chercher")
    trouves = {}
    for f in _fichiers(chemins):
        with open(f, "rb") as h:
            o = h.read()
        n = sum(1 for a in aiguilles if a in o)
        if n:
            trouves[f] = n
    return trouves


def rechercher_empreintes(chemins, empreintes):
    """Preuve du n° 17 : les fichiers dont l'empreinte est l'une de `empreintes`, ou qui en portent une en clair."""
    if not all(type(e) is str and re.fullmatch(r"[0-9a-f]{64}", e) for e in empreintes):
        raise ValueError("des empreintes de 64 caractères hexadécimaux")
    cible = set(empreintes)
    trouves = {}
    for f in _fichiers(chemins):
        with open(f, "rb") as h:
            o = h.read()
        n = (1 if cm.sha256_octets(o) in cible else 0) + sum(1 for e in cible if e.encode("ascii") in o)
        if n:
            trouves[f] = n
    return trouves


def exiger_absence(chemins, textes=(), empreintes=(), quoi="quarantaine"):
    """Arrêt n° 17 si l'une des chaînes ou des empreintes se retrouve sous `chemins` ; ne recopie rien de ce qui a fui."""
    trouves = dict(rechercher_textes(chemins, list(textes))) if textes else {}
    if empreintes:
        for f, n in rechercher_empreintes(chemins, list(empreintes)).items():
            trouves[f] = trouves.get(f, 0) + n
    if trouves:
        raise ArretQuarantaineRompueNA17(f"{quoi} : {len(trouves)} fichier(s) portent ce qui ne doit pas sortir")
    return {}
