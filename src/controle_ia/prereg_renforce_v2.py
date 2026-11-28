"""Validateur renforcé des préenregistrements (v2) : les références citées doivent désigner le dépôt, et chacune le
bon fichier.

La v1 (`prereg_renforce_v1.py`, archivée sans modification) a été jugée « à corriger » par sa contre-lecture de classe B
(Sonnet 5.5, 28 novembre 2026) : 4 remarques majeures, 9 mineures. La v2 reprend ses cinq contrôles et ajoute
l'appariement d'une empreinte au chemin qui la précède, une garde de lecture normalisée et ancrée au dépôt, et le
signalement des empreintes de longueur fausse ou en majuscules.

Contrôles (chaque message commence par sa lettre ; les problèmes de `prereg.problemes` viennent d'abord) :

(a) Empreintes. Toute suite de 32 caractères hexadécimaux ou plus (au moins une lettre, non collée à une
    lettre ou un chiffre, non suivie d'une marque d'ellipse) est classée : 64 minuscules : empreinte ; 64 avec
    majuscules : problème ; 40 : identifiant de commit, avertissement s'il n'est pas un commit du dépôt ; 32 ou 128 :
    avertissement (longueur de MD5 ou de SHA-512) ; toute autre longueur : problème.
    Une empreinte **appariée** à un chemin (voir `paires`) est vérifiée pour ce chemin, dans l'ordre : (1) un compagnon
    `.sha256` porte cette empreinte pour ce chemin ; (2) l'empreinte du fichier sur disque est égale (jamais pour un
    fichier gardé, un lien ou ce qui sort de la racine) ; (3) une version de l'historique git du chemin a cette
    empreinte (au plus `PLAFOND_HISTORIQUE` révisions, plus la révision citée sur la ligne après « commit ») :
    avertissement. Sinon : problème, avec le fichier que l'empreinte désigne s'il y en a un.
    Une empreinte **non appariée** doit être connue du dépôt (compagnon dont le fichier existe, ou fichier suivi par git
    de même empreinte) ; une marque « hors dépôt » ou « hors du dépôt » sur la ligne en fait un avertissement.
    Avertissements aussi : compagnon périmé (le disque a changé), empreinte du fichier vide, empreintes non appariées.
(b) Préfixes. Une suite de 8 à 63 caractères hexadécimaux minuscules dont un chiffre, suivie de « … », « ... », « .. »,
    « ‥ » ou « ⋯ », ou de 8 à 31 caractères (un chiffre et une lettre) seule entre accents graves, commence au moins une
    empreinte connue ; sinon, si c'est un commit du dépôt, rien ; sinon problème. Plusieurs empreintes : avertissement.
    Les préfixes en forme de date (`20261128…`, jusqu'à 14 chiffres) sont ignorés.
(c) Chemins. Contenu entre accents graves commençant par l'un des dossiers de `RACINES_CHEMINS` : le contenu entier,
    sinon son premier mot, doit exister ; `::…` (essai pytest) et `#…` (ancre) sont coupés ; `:n`, `:Ln`, `:n-m`,
    `:n–m`, `:n,m` : chaque ligne tombe dans le fichier ; `:nom` après une extension : le fichier seul. Ignorés : `…`,
    `...`, `*`, `?`, `[`, `<`, `{`, `$`, et les gabarits `AAAA`, `JJ`, `HHMM`, `XXX`, `NNN`. Un chemin qui sort de la
    racine est un problème.
(d) Longueur. Chaque section compte au moins `mots_min` mots (défaut 30), dont au moins `mots_min // 2` distincts ;
    la section « Contre-lecture » au moins `mots_min_contre_lecture` (défaut 12), (e) la tenant entrée par entrée.
(e) Contre-lectures. Chaque entrée (ligne qui commence par une puce, un titre `###` à `######` ou du gras, puis
    « Contre-lecture k ») ou, à défaut d'entrée, la section entière, nomme un modèle (nom de `MODELES` avec sa
    majuscule, ou identifiant `claude-…`, `gemini-…`, `gpt-…`), hors des tournures d'auteur (« écrit par », « auteur »,
    « rédigé par »), et cite au moins une empreinte vérifiée par (a).

Garde de lecture (absolue). Un fichier est **ouvrable** seulement s'il n'est pas un lien symbolique, si son chemin
réel reste dans la racine passée et dans la racine du dépôt (`git rev-parse --show-toplevel`, sinon le premier dossier
parent qui contient `CLAUDE.md`, sinon la racine passée), et si ni son chemin lexical normalisé ni son chemin réel
relatif au dépôt ne tombent sous `est_garde`. Les motifs gardés sont testés à toute profondeur, sans tenir compte de la
casse. Seuls les compagnons `.sha256` (non liens, dans la racine) des fichiers gardés sont lus. Tout refus devient un
avertissement, jamais une ouverture. Le préenregistrement lui-même est refusé (`GardeArret`) s'il est gardé ou lien, et,
sauf `permettre_hors_racine`, s'il sort de la racine.

Ordre d'emploi : sceller (compagnon) ou suivre par git le rapport de contre-lecture et tout fichier cité, puis valider.

Ligne de commande : `python -m controle_ia.prereg_renforce_v2 [--racine R] [--mots-min N] [--mots-min-contre-lecture N]
[--permettre-hors-racine] FICHIER…` ; code de sortie 1 si un fichier a un problème ou est refusé, 0 sinon.
Bibliothèque standard seule.
"""
from __future__ import annotations

import argparse
import hashlib
import os
import posixpath
import re
import subprocess
import sys
from pathlib import Path

from .gardes import GardeArret
from .prereg import SECTIONS, problemes, sections

# ---------- garde de lecture ----------

MOTIFS_GARDES_NOM = (r"[^/]*\.npz", r"[^/]*\.npy", r"[^/]*\.safetensors")       # dernier segment
MOTIFS_GARDES_CHEMIN = (                                                         # à toute profondeur
    r"g0-criteres-2-3-v1/consignes-privees-[^/]*",
    r"ii-b-saboteur-budget-[^/]*",
    r"controle_ia/iib",
    r"p3-consignes-v1[^/]*",          # prereg/P3-consignes-v1.md, ses brouillons et candidats, fichier ou dossier
)
_GARDE = re.compile(r"(?:^|/)(?:" + "|".join(MOTIFS_GARDES_CHEMIN) + r")(?:/|$)"
                    r"|(?:^|/)(?:" + "|".join(MOTIFS_GARDES_NOM) + r")$")
DOSSIERS_IGNORES = {".git", ".venv", "venv", "node_modules", "__pycache__", ".pytest_cache", ".mypy_cache"}


def est_garde(chemin: str) -> bool:
    """Vrai si le chemin (relatif ou absolu) tombe sous la garde : normalisé, motifs à toute profondeur, casse
    indifférente. Un compagnon `.sha256` n'y tombe jamais."""
    c = posixpath.normpath(str(chemin).replace(os.sep, "/")).lower()
    if c.endswith(".sha256"):
        return False
    return bool(_GARDE.search(c))


def racine_du_depot(racine: str | Path) -> Path:
    r = Path(os.path.realpath(racine))
    try:
        sortie = subprocess.run(["git", "-C", str(r), "rev-parse", "--show-toplevel"],
                                capture_output=True, text=True, check=True).stdout.strip()
        if sortie:
            return Path(os.path.realpath(sortie))
    except (OSError, subprocess.CalledProcessError):
        pass
    for d in (r, *r.parents):
        if (d / "CLAUDE.md").is_file():
            return d
    return r


def _dedans(p: Path, base: Path) -> bool:
    try:
        p.relative_to(base)
        return True
    except ValueError:
        return False


# ---------- motifs du texte ----------

RACINES_CHEMINS = ("src", "docs", "prereg", "diag", "runs", "registres", "scripts", "tests", "brouillons", "livrables")
MODELES = ("Fable", "Opus", "Sonnet", "Haiku", "Gemini", "Carbon", "Argon", "Neon", "Astra", "GPT",
           "Llama", "Mistral", "Qwen", "DeepSeek", "Grok")
MOTS_MIN = 30
MOTS_MIN_CONTRE_LECTURE = 12
PLAFOND_HISTORIQUE = 50
EMPREINTE_VIDE = hashlib.sha256(b"").hexdigest()

ELLIPSE = r"(?:…|\.{2,3}|‥|⋯)"
HEXLONG = re.compile(r"(?<![0-9A-Za-z])[0-9a-fA-F]{32,}(?![0-9A-Za-z])(?!" + ELLIPSE + ")")
HEX64 = re.compile(r"(?<![0-9A-Za-z])[0-9a-f]{64}(?![0-9A-Za-z])")
PREFIXE = re.compile(r"(?<![0-9A-Za-z])([0-9a-f]{8,63})" + ELLIPSE)
PREFIXE_NU = re.compile(r"`([0-9a-f]{8,31})`")
DATE = re.compile(r"(?:19|20)\d{6}\d{0,6}")
CHEMIN = re.compile(r"`((?:" + "|".join(RACINES_CHEMINS) + r")/[^`\n]*)`")
LIGNES = re.compile(r"^(.*?):(L?\d+(?:[-–]L?\d+)?(?:,L?\d+(?:[-–]L?\d+)?)*)$")
NOM_APRES_EXTENSION = re.compile(r"^(.*?\.[A-Za-z0-9]+):[A-Za-z_][\w.]*$")
MOTIF_IGNORE = re.compile(r"…|\.\.\.|[*?\[<{$]|AAAA|JJ|HHMM|XXX|NNN")
INTERVALLE = re.compile(r"[\s(),;:|—–\-`]*(?:(?:empreinte|sha256|sha-256|SHA-256)\s*:?[\s(),;:|—–\-`]*)?")
COMMIT_CITE = re.compile(r"commit\s+`?([0-9a-f]{7,40})`?", re.I)
HORS_DEPOT = re.compile(r"hors (?:du )?dépôt", re.I)
MOT = re.compile(r"\S*\w\S*")
ENTREE = re.compile(r"^[ \t]*(?:#{3,6}[ \t]+\**|[-*+][ \t]+\**|\*\*)[ \t]*Contre-lecture[ \t]+(\d+)", re.M)
AUTEUR = re.compile(r"(?:écrite?s? par|rédigée?s? par|auteur|autrice)\W{0,3}(?:\w+\W+){0,2}$", re.I)
LIGNE_SHA = re.compile(r"^([0-9a-f]{64}) [ *](.+)$")


def _motif_modeles(modeles) -> re.Pattern:
    """Nom de modèle avec sa majuscule (« Fable », pas « une fable »), mot entier, ou identifiant en minuscules."""
    noms = "|".join(re.escape(m) for m in modeles)
    return re.compile(r"(?<![0-9A-Za-z])(?:" + noms + r")(?![A-Za-z])"
                      r"|(?<![0-9A-Za-z])(?i:claude|gemini|gpt)-[0-9a-z][\w.-]*")


def _hacher(chemin: Path) -> str:
    h = hashlib.sha256()
    with open(chemin, "rb") as f:
        for bloc in iter(lambda: f.read(1 << 20), b""):
            h.update(bloc)
    return h.hexdigest()


def _nb_lignes(chemin: Path) -> int:
    n, dernier = 0, b""
    with open(chemin, "rb") as f:
        for bloc in iter(lambda: f.read(1 << 20), b""):
            n += bloc.count(b"\n")
            dernier = bloc[-1:]
    return n + (1 if dernier and dernier != b"\n" else 0)


# ---------- index ----------

class Index:
    """Empreintes connues : compagnons (lus d'emblée), fichiers suivis par git (hachés à la première demande), empreintes
    sur disque des chemins cités (en cache), historique git (à la demande). Construit une fois par appel."""

    def __init__(self, racine: str | Path = "."):
        self.racine = Path(os.path.realpath(racine))
        self.depot = racine_du_depot(self.racine)
        self.compagnons: dict[str, set[str]] = {}
        self.par_chemin: dict[str, set[str]] = {}
        self._suivis: dict[str, set[str]] | None = None
        self._disque: dict[str, str | None] = {}
        self._commits: dict[str, bool] = {}
        self.gardes_sautes: list[str] = []
        self.avertissements: list[str] = []
        self.git_ok = True
        self._lire_compagnons()

    # garde
    def refus(self, p: Path) -> str | None:
        """Raison de ne pas ouvrir `p`, ou None s'il est ouvrable."""
        lexical = posixpath.normpath(str(p).replace(os.sep, "/"))
        if est_garde(lexical):
            return "fichier gardé"
        if p.is_symlink():
            return "lien symbolique"
        reel = Path(os.path.realpath(p))
        if not _dedans(reel, self.racine) or not _dedans(reel, self.depot):
            return "hors de la racine"
        if est_garde(str(reel.relative_to(self.depot))):
            return "fichier gardé"
        if not reel.is_file():
            return "pas un fichier ordinaire"
        return None

    def rel(self, p: Path) -> str:
        return posixpath.normpath(str(Path(os.path.realpath(p)).relative_to(self.racine)).replace(os.sep, "/"))

    def _lire_compagnons(self) -> None:
        for dossier, sous, fichiers in os.walk(self.racine):
            sous[:] = [d for d in sous if d not in DOSSIERS_IGNORES]
            for nom in fichiers:
                if not nom.endswith(".sha256"):
                    continue
                p = Path(dossier) / nom
                if p.is_symlink() or not _dedans(Path(os.path.realpath(p)), self.racine):
                    continue
                try:
                    lignes = [l.strip() for l in p.read_text(encoding="utf-8").splitlines() if l.strip()]
                except (OSError, UnicodeDecodeError):
                    self.avertissements.append(f"compagnon illisible : {p.relative_to(self.racine)}")
                    continue
                source = p.with_name(nom[: -len(".sha256")])
                for ligne in lignes:
                    m = LIGNE_SHA.match(ligne)
                    if not m:
                        continue
                    designe = p.parent / m.group(2).strip()
                    if not os.path.lexists(designe) and os.path.lexists(source) and len(lignes) == 1:
                        designe = source
                    if not os.path.lexists(designe):          # compagnon orphelin : ne désigne aucun fichier
                        continue
                    reel = Path(os.path.realpath(designe))
                    if not _dedans(reel, self.racine):
                        continue
                    rel = self.rel(designe)
                    self.compagnons.setdefault(m.group(1), set()).add(rel)
                    self.par_chemin.setdefault(rel, set()).add(m.group(1))

    def _git(self, *args, entree: bytes | None = None) -> bytes | None:
        try:
            return subprocess.run(["git", "-C", str(self.racine), *args], input=entree,
                                  capture_output=True, check=True).stdout
        except (OSError, subprocess.CalledProcessError):
            return None

    def suivis(self) -> dict[str, set[str]]:
        if self._suivis is None:
            self._suivis = {}
            sortie = self._git("ls-files", "-z", "--cached")
            if sortie is None:
                self.git_ok = False
                self.avertissements.append("index git indisponible : seuls les compagnons comptent")
                sortie = b""
            illisibles = 0
            for brut in sortie.split(b"\0"):
                if not brut:
                    continue
                rel = brut.decode("utf-8", "surrogateescape")
                if rel.endswith(".sha256"):
                    continue
                p = self.racine / rel
                raison = self.refus(p)
                if raison == "fichier gardé":
                    self.gardes_sautes.append(rel)
                    continue
                if raison:
                    continue
                try:
                    h = _hacher(p)
                except OSError:
                    illisibles += 1
                    continue
                self._suivis.setdefault(h, set()).add(posixpath.normpath(rel))
            if illisibles:
                self.avertissements.append(f"{illisibles} fichier(s) suivi(s) illisible(s), non hachés")
        return self._suivis

    def connue(self, h: str) -> bool:
        return h in self.compagnons or h in self.suivis()

    def chemins(self, h: str) -> set[str]:
        return self.compagnons.get(h, set()) | self.suivis().get(h, set())

    def prefixe(self, pre: str) -> set[str]:
        return {h for h in self.compagnons if h.startswith(pre)} | {h for h in self.suivis() if h.startswith(pre)}

    def disque(self, rel: str) -> str | None:
        """Empreinte sur disque d'un chemin relatif ouvrable ; None si refusé ou illisible."""
        if rel not in self._disque:
            p = self.racine / rel
            if self.refus(p):
                self._disque[rel] = None
            else:
                try:
                    self._disque[rel] = _hacher(p)
                except OSError:
                    self._disque[rel] = None
        return self._disque[rel]

    def est_commit(self, x: str) -> bool:
        if x not in self._commits:
            self._commits[x] = self._git("cat-file", "-e", f"{x}^{{commit}}") is not None
        return self._commits[x]

    def historique(self, rel: str, h: str, revisions=()) -> str | None:
        """Commit d'une version passée de `rel` dont l'empreinte vaut `h`, ou None. Jamais pour un chemin gardé."""
        if est_garde(rel):
            return None
        objets: list[tuple[str, str]] = []
        for rev in revisions:
            complet = self._git("rev-parse", "--verify", "--quiet", f"{rev}^{{commit}}")
            o = self._git("rev-parse", "--verify", "--quiet", f"{rev}:./{rel}") if complet else None
            if o:
                objets.append((complet.decode().strip(), o.decode().strip()))
        journal = self._git("log", "--all", f"-n{PLAFOND_HISTORIQUE}", "--format=C %H", "--raw", "--no-abbrev",
                            "--no-renames", "--", rel)
        if journal:
            commit = None
            for ligne in journal.decode("utf-8", "replace").splitlines():
                if ligne.startswith("C "):
                    commit = ligne[2:].strip()
                elif ligne.startswith(":") and commit:
                    champs = ligne.split()
                    if len(champs) >= 4 and set(champs[3]) != {"0"}:
                        objets.append((commit, champs[3]))
        vus = set()
        oids = []
        for c, o in objets:
            if o not in vus:
                vus.add(o)
                oids.append((c, o))
        if not oids:
            return None
        lot = self._git("cat-file", "--batch", entree="".join(o + "\n" for _, o in oids).encode())
        if not lot:
            return None
        pos = 0
        for c, o in oids:
            fin = lot.index(b"\n", pos)
            tete = lot[pos:fin].split()
            pos = fin + 1
            if len(tete) < 3 or tete[1] != b"blob":
                continue
            taille = int(tete[2])
            contenu = lot[pos:pos + taille]
            pos += taille + 1
            if hashlib.sha256(contenu).hexdigest() == h:
                return c
        return None


# ---------- appariement ----------

def _chemin_cite(contenu: str) -> str | None:
    """Chemin d'un contenu entre accents graves, sans suffixe de lignes ; None s'il est ignoré."""
    c = contenu.split()[0] if contenu.split() else contenu
    if MOTIF_IGNORE.search(c):
        return None
    c = c.split("::")[0].split("#")[0]
    m = LIGNES.match(c) or NOM_APRES_EXTENSION.match(c)
    return m.group(1) if m else c


def paires(texte: str) -> list[tuple[int, str, str | None]]:
    """[(position, empreinte, chemin ou None)] pour chaque empreinte de 64 minuscules. Par ligne : si la ligne a k ≥ 2
    chemins tous avant k empreintes, appariement par rang (k chemins et j ≠ k empreintes : aucun) ; sinon, une empreinte
    s'apparie au dernier chemin qui la précède sur la ligne si l'intervalle ne contient que des séparateurs, au plus un
    accent grave et, au plus, le mot « empreinte » ou « sha256 »."""
    sortie = []
    debut = 0
    for ligne in texte.split("\n"):
        chemins = [(m.start() + debut, m.end() + debut, _chemin_cite(m.group(1))) for m in CHEMIN.finditer(ligne)]
        hachages = [(m.start() + debut, m.group(0)) for m in HEX64.finditer(ligne)]
        rang = None
        if len(chemins) >= 2 and hachages and chemins[-1][1] <= hachages[0][0]:
            rang = [c for _, _, c in chemins] if len(chemins) == len(hachages) else []
        for i, (pos, h) in enumerate(hachages):
            chem = None
            if rang is not None:
                chem = rang[i] if rang else None
            else:
                avant = [(fin, c) for _, fin, c in chemins if fin <= pos]
                if avant:
                    fin, c = avant[-1]
                    inter = texte[fin:pos]
                    if INTERVALLE.fullmatch(inter) and inter.count("`") <= 1:
                        chem = c
            sortie.append((pos, h, chem))
        debut += len(ligne) + 1
    return sortie


# ---------- validation ----------

def _ligne(texte: str, pos: int) -> int:
    return texte.count("\n", 0, pos) + 1


def _texte_de_ligne(texte: str, pos: int) -> str:
    d = texte.rfind("\n", 0, pos) + 1
    f = texte.find("\n", pos)
    return texte[d:f if f >= 0 else len(texte)]


def _normaliser(racine: Path, chem: str) -> tuple[str | None, Path | None]:
    """(chemin relatif normalisé, chemin absolu) ou (None, None) s'il sort de la racine."""
    n = posixpath.normpath(chem)
    if n.startswith("../") or n == ".." or n.startswith("/"):
        return None, None
    return n, racine / n


def verifier_renforce(chemin: str | Path, racine: str | Path = ".", mots_min: int = MOTS_MIN,
                      mots_min_contre_lecture: int = MOTS_MIN_CONTRE_LECTURE, index: Index | None = None,
                      modeles=MODELES, permettre_hors_racine: bool = False) -> tuple[list[str], list[str]]:
    """Renvoie (problèmes, avertissements). Lève `GardeArret` si le préenregistrement ne peut pas être ouvert."""
    index = index or Index(racine)
    racine = index.racine
    p = Path(chemin)
    absolu = p if p.is_absolute() else Path.cwd() / p
    reel = Path(os.path.realpath(absolu))
    if est_garde(str(absolu)) or est_garde(str(reel)) or (
            _dedans(reel, index.depot) and est_garde(str(reel.relative_to(index.depot)))):
        raise GardeArret(f"{chemin} : fichier sous la garde de lecture, il n'est pas ouvert")
    if absolu.is_symlink():
        raise GardeArret(f"{chemin} : lien symbolique, il n'est pas ouvert")
    if not permettre_hors_racine and not _dedans(reel, racine):
        raise GardeArret(f"{chemin} : hors de la racine {racine}, il n'est pas ouvert")
    try:
        octets = reel.read_bytes()
    except OSError as e:
        return [f"(lecture) fichier illisible : {e.strerror or e}"], []
    try:
        texte = octets.decode("utf-8")
    except UnicodeDecodeError as e:
        return [f"(lecture) fichier non lisible en UTF-8 (octet {e.start})"], []
    sortie = list(problemes(reel))
    avert: list[str] = []
    if texte.startswith("\ufeff"):
        sortie.append("(lecture) octet d'ordre (BOM) en tête : à retirer, il masque le premier titre")

    # (a) suites hexadécimales longues : classement
    for m in HEXLONG.finditer(texte):
        s = m.group(0)
        if not re.search(r"[a-fA-F]", s):
            continue
        ln = _ligne(texte, m.start())
        if len(s) == 64 and s != s.lower():
            sortie.append(f"(a) empreinte en majuscules, ligne {ln} : {s} (écrire en minuscules)")
        elif len(s) == 40:
            if not index.est_commit(s.lower()):
                avert.append(f"(a) identifiant de 40 caractères qui n'est pas un commit du dépôt, ligne {ln} : {s}")
        elif len(s) in (32, 128):
            avert.append(f"(a) suite de {len(s)} caractères (MD5 ou SHA-512 ?), pas une empreinte SHA-256, "
                         f"ligne {ln} : {s[:16]}…")
        elif len(s) != 64:
            sortie.append(f"(a) longueur d'empreinte invalide ({len(s)} caractères), ligne {ln} : {s}")

    # (a) empreintes de 64 minuscules : appariées ou non
    verifiees: set[str] = set()
    deja: set[tuple[str, str | None]] = set()
    non_appariees: list[int] = []
    for pos, h, chem in paires(texte):
        if (h, chem) in deja:
            continue
        deja.add((h, chem))
        ln = _ligne(texte, pos)
        if h == EMPREINTE_VIDE:
            avert.append(f"(a) empreinte du fichier vide, ligne {ln}")
        if chem is None:
            if index.connue(h):
                verifiees.add(h)
            elif HORS_DEPOT.search(_texte_de_ligne(texte, pos)):
                avert.append(f"(a) empreinte déclarée hors dépôt, non vérifiée, ligne {ln} : {h}")
            else:
                sortie.append(f"(a) empreinte qui ne désigne aucun fichier du dépôt, ligne {ln} : {h}")
            non_appariees.append(ln)
            continue
        rel, cible = _normaliser(racine, chem)
        if rel is None:
            sortie.append(f"(a) empreinte appariée à un chemin qui sort de la racine, ligne {ln} : {chem}")
            continue
        if h in index.par_chemin.get(rel, set()):                  # (1) compagnon du chemin cité
            verifiees.add(h)
            d = index.disque(rel)
            if d is not None and d != h:
                avert.append(f"(a) compagnon périmé : le fichier {rel} a changé sur disque, ligne {ln}")
            continue
        if index.disque(rel) == h:                                  # (2) disque
            verifiees.add(h)
            continue
        revs = [m.group(1) for m in COMMIT_CITE.finditer(_texte_de_ligne(texte, pos))]
        c = index.historique(rel, h, revs)                          # (3) historique
        if c:
            verifiees.add(h)
            avert.append(f"(a) empreinte d'une version ancienne de {rel} (commit {c[:12]}), ligne {ln}")
            continue
        if est_garde(rel):
            sortie.append(f"(a) empreinte non vérifiable : {rel} est gardé et aucun compagnon ne la porte, ligne {ln}")
            continue
        ailleurs = sorted(index.chemins(h))
        if not os.path.lexists(cible):
            motif = "chemin absent"
        elif index.refus(cible):
            motif = f"chemin non ouvrable ({index.refus(cible)})"
        else:
            motif = "ce n'est pas l'empreinte de ce fichier"
        sortie.append(f"(a) empreinte appariée à {rel} non vérifiée ({motif}), ligne {ln} : {h}"
                      + (f" ; elle désigne {ailleurs[0]}" if ailleurs else ""))
    if non_appariees:
        avert.append(f"(a) {len(non_appariees)} empreinte(s) non appariée(s) à un chemin, lignes "
                     f"{', '.join(map(str, sorted(set(non_appariees))[:10]))}{' …' if len(set(non_appariees)) > 10 else ''}")

    # (b) préfixes
    vus: set[str] = set()
    candidats = [(m.start(), m.group(1)) for m in PREFIXE.finditer(texte)]
    candidats += [(m.start(), m.group(1)) for m in PREFIXE_NU.finditer(texte)
                  if re.search(r"\d", m.group(1)) and re.search(r"[a-f]", m.group(1))]
    for pos, pre in sorted(candidats):
        if pre in vus or not re.search(r"\d", pre) or DATE.fullmatch(pre):
            continue
        vus.add(pre)
        ln = _ligne(texte, pos)
        cibles = index.prefixe(pre)
        if not cibles:
            if not index.est_commit(pre):
                sortie.append(f"(b) préfixe d'empreinte sans empreinte connue ni commit, ligne {ln} : {pre}…")
        elif len(cibles) > 1:
            avert.append(f"(b) préfixe d'empreinte ambigu, ligne {ln} : {pre}… désigne {len(cibles)} empreintes")

    # (c) chemins
    vus = set()
    for m in CHEMIN.finditer(texte):
        contenu = m.group(1).strip()
        if contenu in vus:
            continue
        vus.add(contenu)
        ln = _ligne(texte, m.start())
        entier, _ = _normaliser(racine, contenu)
        if entier and " " in contenu and os.path.lexists(racine / entier):
            continue                                               # nom avec espaces, existant
        mot = contenu.split()[0]
        if MOTIF_IGNORE.search(mot):
            continue
        mot = mot.split("::")[0].split("#")[0]
        chem, intervalles = mot, []
        s = LIGNES.match(mot)
        if s:
            chem = s.group(1)
            for morceau in s.group(2).split(","):
                bornes = [int(x.lstrip("L")) for x in re.split(r"[-–]", morceau)]
                intervalles.append((bornes[0], bornes[-1]))
        else:
            e = NOM_APRES_EXTENSION.match(mot)
            if e:
                chem = e.group(1)
        rel, cible = _normaliser(racine, chem)
        if rel is None:
            sortie.append(f"(c) chemin qui sort de la racine, ligne {ln} : {chem}")
            continue
        if not os.path.lexists(cible):
            sortie.append(f"(c) chemin inexistant, ligne {ln} : {chem}")
            continue
        if not intervalles:
            continue
        if cible.is_dir() and not cible.is_symlink():
            sortie.append(f"(c) suffixe de lignes sur un dossier, ligne {ln} : {mot}")
            continue
        raison = index.refus(cible)
        if raison:
            avert.append(f"(c) lignes non vérifiées ({raison}), ligne {ln} : {mot}")
            continue
        n = _nb_lignes(cible)
        if not all(1 <= a <= b <= n for a, b in intervalles):
            sortie.append(f"(c) lignes hors du fichier ({n} lignes), ligne {ln} : {mot}")

    # (d) longueur des sections
    s = sections(texte)
    for nom in SECTIONS:
        if nom not in s:
            continue
        mots = MOT.findall(s[nom])
        seuil = mots_min_contre_lecture if nom == "Contre-lecture" else mots_min
        if len(mots) < seuil:
            sortie.append(f"(d) section trop courte : {nom} ({len(mots)} mots, au moins {seuil})")
        elif nom != "Contre-lecture" and len({x.lower() for x in mots}) < mots_min // 2:
            sortie.append(f"(d) section répétitive : {nom} ({len({x.lower() for x in mots})} mots distincts, "
                          f"au moins {mots_min // 2})")

    # (e) contre-lectures
    cl = s.get("Contre-lecture")
    if cl:
        motif = _motif_modeles(modeles)
        entrees = list(ENTREE.finditer(cl))
        morceaux = ([(f"contre-lecture {e.group(1)}",
                      cl[e.start():(entrees[k + 1].start() if k + 1 < len(entrees) else len(cl))])
                     for k, e in enumerate(entrees)] or [("section Contre-lecture", cl)])
        for nom, corps in morceaux:
            relecteur = [x for x in motif.finditer(corps) if not AUTEUR.search(corps[max(0, x.start() - 40):x.start()])]
            if not relecteur:
                sortie.append(f"(e) {nom} sans le modèle du relecteur (attendu : {', '.join(modeles)}, "
                              "ou un identifiant claude-…, gemini-…, gpt-…, hors « écrit par » et « auteur »)")
            if not any(h in verifiees for h in HEX64.findall(corps)):
                sortie.append(f"(e) {nom} sans empreinte vérifiée par (a)")
    avert = index.avertissements + avert
    return sortie, avert


def problemes_renforces(chemin: str | Path, racine: str | Path = ".", mots_min: int = MOTS_MIN,
                        index: Index | None = None, **kw) -> list[str]:
    return verifier_renforce(chemin, racine, mots_min=mots_min, index=index, **kw)[0]


def _main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(prog="python -m controle_ia.prereg_renforce_v2", description=__doc__.split("\n")[0])
    ap.add_argument("fichiers", nargs="+")
    ap.add_argument("--racine", default=".")
    ap.add_argument("--mots-min", type=int, default=MOTS_MIN)
    ap.add_argument("--mots-min-contre-lecture", type=int, default=MOTS_MIN_CONTRE_LECTURE)
    ap.add_argument("--permettre-hors-racine", action="store_true")
    a = ap.parse_args(argv)
    index = Index(a.racine)
    code = 0
    for f in a.fichiers:
        try:
            pb, av = verifier_renforce(f, a.racine, mots_min=a.mots_min, mots_min_contre_lecture=a.mots_min_contre_lecture,
                                       index=index, permettre_hors_racine=a.permettre_hors_racine)
        except GardeArret as e:
            print(f"{f} : REFUS — {e}")
            code = 1
            continue
        print(f"{f} : {'conforme' if not pb else f'{len(pb)} problème(s)'}"
              + (f", {len(av)} avertissement(s)" if av else ""))
        for x in pb:
            print(f"  PROBLÈME {x}")
        for x in av:
            print(f"  AVERTISSEMENT {x}")
        code = code or (1 if pb else 0)
    return code


if __name__ == "__main__":
    sys.exit(_main(sys.argv[1:]))
