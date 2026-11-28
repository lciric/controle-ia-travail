"""Validateur renforcé des préenregistrements (v1) : les références citées doivent désigner le dépôt.

`controle_ia.prereg.problemes` ne vérifie que la structure (huit titres non vides, aucun marqueur, deux chaînes de
64 caractères hexadécimaux par contre-lecture). Ce module reprend ses problèmes, puis ajoute cinq contrôles :

(a) toute empreinte complète (64 caractères hexadécimaux) citée n'importe où désigne un fichier du dépôt : soit un
    compagnon `*.sha256` (une ligne au format de `sha256sum`) la porte et le fichier qu'il désigne existe, soit un
    fichier suivi par git a cette empreinte ;
(b) tout préfixe d'empreinte cité sous la forme `0065065b…` (8 à 63 caractères hexadécimaux dont au moins un chiffre,
    suivis de « … » ou de « ... ») correspond à au moins une empreinte connue ; plusieurs : avertissement seulement ;
(c) tout chemin du dépôt cité entre accents graves et commençant par l'un des dossiers de `RACINES_CHEMINS` existe ;
    seul le premier mot du contenu est lu (les noms de fichiers du dépôt n'ont pas d'espace) ;
    un suffixe `:ligne` ou `:l1-l2` tombe dans le fichier ; un chemin qui porte `…`, `...` ou un motif
    (`*`, `?`, `[`, `<`, `{`, `$`) est ignoré ;
(d) chacune des huit sections de `prereg.SECTIONS` compte au moins `mots_min` mots (défaut 30 ; un mot est un
    morceau sans espace qui contient au moins une lettre ou un chiffre) ;
(e) chaque entrée « Contre-lecture k » (à défaut d'entrée, la section entière) nomme le modèle du relecteur (un nom
    de `MODELES`, casse indifférente, mot entier) et cite au moins une empreinte qui se résout par (a).

Garde de lecture (absolue) : aucun fichier qui répond à `est_garde` n'est ouvert, ni pour son empreinte, ni pour compter
ses lignes, ni comme préenregistrement à valider ; seuls les compagnons `.sha256` de ces fichiers sont lus. L'index des
empreintes est construit une fois par appel (une fois pour tous les fichiers en ligne de commande) ; les fichiers suivis
par git ne sont hachés que si une empreinte ou un préfixe cité n'est pas porté par un compagnon. Bibliothèque standard.

Ligne de commande : `python -m controle_ia.prereg_renforce_v1 [--racine R] [--mots-min N] FICHIER…` ; code de sortie 1
si un fichier a un problème (les avertissements ne comptent pas), 0 sinon.
"""
from __future__ import annotations

import argparse
import fnmatch
import hashlib
import os
import re
import subprocess
import sys
from pathlib import Path, PurePosixPath

from .gardes import GardeArret
from .prereg import SECTIONS, problemes, sections

# Garde de lecture : motifs sur le chemin relatif à la racine (séparateur « / »).
MOTIFS_GARDES_NOM = ("*.npz", "*.npy", "*.safetensors")
MOTIFS_GARDES_CHEMIN = (
    "brouillons/g0-criteres-2-3-v1/consignes-privees-*",      # fichier ou dossier, et tout ce qui est dessous
    "brouillons/ii-b-saboteur-budget-*",                      # tout ce qui est sous ces dossiers
    "src/controle_ia/iib",
)
PREFIXE_GARDE_NOM = "P3-consignes-v1"   # prereg/P3-consignes-v1.md et ses brouillons et candidats, où qu'ils soient
DOSSIERS_IGNORES = {".git", ".venv", "venv", "node_modules", "__pycache__", ".pytest_cache", ".mypy_cache"}

RACINES_CHEMINS = ("src", "docs", "prereg", "diag", "runs", "registres", "scripts", "tests", "brouillons", "livrables")
MODELES = ("Fable", "Opus", "Sonnet", "Haiku", "Gemini", "Carbon", "Argon", "Neon", "Astra", "GPT",
           "Llama", "Mistral", "Qwen", "DeepSeek", "Grok")
MOTS_MIN = 30

HEX64 = re.compile(r"(?<![0-9A-Za-z])[0-9a-f]{64}(?![0-9A-Za-z])")
PREFIXE = re.compile(r"(?<![0-9A-Za-z])([0-9a-f]{8,63})(?:…|\.\.\.)")
CHEMIN = re.compile(r"`((?:" + "|".join(RACINES_CHEMINS) + r")/[^`\n]*)`")
SUFFIXE_LIGNES = re.compile(r"^(.*?):(\d+)(?:-(\d+))?$")
MOTIF_IGNORE = re.compile(r"…|\.\.\.|[*?\[<{$]")
MOT = re.compile(r"\S*\w\S*")
ENTREE = re.compile(r"^[ \t]*(?:#{3,6}[ \t]+)?(?:[-*+][ \t]+)?\**[ \t]*Contre-lecture[ \t]+(\d+)", re.M)
LIGNE_SHA = re.compile(r"^([0-9a-f]{64}) [ *](.+)$")


def _modeles_motif(modeles) -> re.Pattern:
    return re.compile(r"(?<![0-9A-Za-z])(" + "|".join(re.escape(m) for m in modeles) + r")(?![A-Za-z])", re.I)


def est_garde(rel: str) -> bool:
    """Vrai si le chemin relatif (« / ») tombe sous la garde de lecture. Les compagnons `.sha256` n'y tombent jamais."""
    rel = rel.replace(os.sep, "/")
    while rel.startswith("./"):
        rel = rel[2:]
    if rel.endswith(".sha256"):
        return False
    nom = PurePosixPath(rel).name
    if any(fnmatch.fnmatch(nom, m) for m in MOTIFS_GARDES_NOM) or nom.startswith(PREFIXE_GARDE_NOM):
        return True
    parties = rel.split("/")
    for i in range(1, len(parties) + 1):
        tete = "/".join(parties[:i])
        if any(fnmatch.fnmatch(tete, m) for m in MOTIFS_GARDES_CHEMIN):
            return True
        if parties[i - 1].startswith(PREFIXE_GARDE_NOM):
            return True
    return False


def _hacher(chemin: Path) -> str:
    h = hashlib.sha256()
    with open(chemin, "rb") as f:
        for bloc in iter(lambda: f.read(1 << 20), b""):
            h.update(bloc)
    return h.hexdigest()


class Index:
    """Empreintes connues du dépôt : celles des compagnons (lus d'emblée), puis celles des fichiers suivis par git
    (hachés à la première demande seulement, en sautant les fichiers gardés)."""

    def __init__(self, racine: str | Path = "."):
        self.racine = Path(racine).resolve()
        self.compagnons: dict[str, set[str]] = {}
        self._suivis: dict[str, set[str]] | None = None
        self.gardes_sautes: list[str] = []
        self._lire_compagnons()

    def _lire_compagnons(self) -> None:
        for dossier, sous, fichiers in os.walk(self.racine):
            sous[:] = [d for d in sous if d not in DOSSIERS_IGNORES]
            for nom in fichiers:
                if not nom.endswith(".sha256"):
                    continue
                p = Path(dossier) / nom
                try:
                    lignes = p.read_text(encoding="utf-8").splitlines()
                except (OSError, UnicodeDecodeError):
                    continue
                source = p.with_name(nom[: -len(".sha256")])
                for ligne in lignes:
                    m = LIGNE_SHA.match(ligne.strip())
                    if not m:
                        continue
                    designe = p.parent / m.group(2).strip()
                    if not designe.exists() and source.exists() and len(lignes) == 1:
                        designe = source
                    if designe.exists():       # un compagnon orphelin ne désigne aucun fichier
                        self.compagnons.setdefault(m.group(1), set()).add(self._rel(designe))

    def _rel(self, p: Path) -> str:
        try:
            return str(p.resolve().relative_to(self.racine)).replace(os.sep, "/")
        except ValueError:
            return str(p)

    def suivis(self) -> dict[str, set[str]]:
        if self._suivis is None:
            self._suivis = {}
            try:
                sortie = subprocess.run(["git", "-C", str(self.racine), "ls-files", "-z", "--cached"],
                                        capture_output=True, check=True).stdout
            except (OSError, subprocess.CalledProcessError):
                sortie = b""                    # pas de dépôt git : seuls les compagnons comptent
            for brut in sortie.split(b"\0"):
                if not brut:
                    continue
                rel = brut.decode("utf-8", "surrogateescape")
                if rel.endswith(".sha256"):
                    continue
                if est_garde(rel):
                    self.gardes_sautes.append(rel)
                    continue
                p = self.racine / rel
                if not p.is_file():
                    continue
                self._suivis.setdefault(_hacher(p), set()).add(rel)
        return self._suivis

    def resoudre(self, h: str) -> set[str]:
        if h in self.compagnons:
            return self.compagnons[h]
        return self.suivis().get(h, set())

    def prefixe(self, pre: str) -> set[str]:
        """Empreintes complètes connues qui commencent par `pre`."""
        trouve = {h for h in self.compagnons if h.startswith(pre)}
        trouve |= {h for h in self.suivis() if h.startswith(pre)}
        return trouve


def _ligne(texte: str, pos: int) -> int:
    return texte.count("\n", 0, pos) + 1


def _nb_lignes(p: Path) -> int:
    with open(p, "rb") as f:
        donnees = f.read()
    return donnees.count(b"\n") + (1 if donnees and not donnees.endswith(b"\n") else 0)


def verifier_renforce(chemin: str | Path, racine: str | Path = ".", mots_min: int = MOTS_MIN,
                      index: Index | None = None, modeles=MODELES) -> tuple[list[str], list[str]]:
    """Renvoie (problèmes, avertissements). Les problèmes commencent par ceux de `prereg.problemes`."""
    index = index or Index(racine)
    racine = index.racine
    p = Path(chemin)
    rel_p = index._rel(p if p.is_absolute() else Path.cwd() / p)
    if est_garde(rel_p) or est_garde(p.name):
        raise GardeArret(f"{chemin} : fichier sous la garde de lecture, il n'est pas ouvert")
    sortie = list(problemes(p))
    avert: list[str] = []
    texte = p.read_text(encoding="utf-8")

    # (a) empreintes complètes
    resolues: set[str] = set()
    vues: set[str] = set()
    for m in HEX64.finditer(texte):
        h = m.group(0)
        if h in vues:
            continue
        vues.add(h)
        if index.resoudre(h):
            resolues.add(h)
        else:
            sortie.append(f"(a) empreinte qui ne désigne aucun fichier du dépôt, ligne {_ligne(texte, m.start())} : {h}")

    # (b) préfixes d'empreinte
    vus: set[str] = set()
    for m in PREFIXE.finditer(texte):
        pre = m.group(1)
        if pre in vus or not re.search(r"\d", pre):
            continue
        vus.add(pre)
        cibles = index.prefixe(pre)
        if not cibles:
            sortie.append(f"(b) préfixe d'empreinte sans empreinte connue, ligne {_ligne(texte, m.start())} : {pre}…")
        elif len(cibles) > 1:
            avert.append(f"(b) préfixe d'empreinte ambigu, ligne {_ligne(texte, m.start())} : {pre}… "
                         f"désigne {len(cibles)} empreintes")

    # (c) chemins cités entre accents graves
    vus = set()
    for m in CHEMIN.finditer(texte):
        cite = m.group(1).split()[0]   # une commande ou une liste entre accents graves : le premier mot seul
        if cite in vus or MOTIF_IGNORE.search(cite):
            continue
        vus.add(cite)
        ln = _ligne(texte, m.start())
        chem, l1, l2 = cite, None, None
        s = SUFFIXE_LIGNES.match(cite)
        if s:
            chem, l1 = s.group(1), int(s.group(2))
            l2 = int(s.group(3)) if s.group(3) else l1
        cible = racine / chem
        if not cible.exists():
            sortie.append(f"(c) chemin inexistant, ligne {ln} : {chem}")
            continue
        if l1 is None:
            continue
        if not cible.is_file():
            sortie.append(f"(c) suffixe de lignes sur un dossier, ligne {ln} : {cite}")
        elif est_garde(chem):
            avert.append(f"(c) lignes non vérifiées (fichier sous la garde de lecture), ligne {ln} : {cite}")
        else:
            n = _nb_lignes(cible)
            if not (1 <= l1 <= l2 <= n):
                sortie.append(f"(c) lignes hors du fichier ({n} lignes), ligne {ln} : {cite}")

    # (d) sections trop courtes
    s = sections(texte)
    for nom in SECTIONS:
        if nom in s:
            n = len(MOT.findall(s[nom]))
            if n < mots_min:
                sortie.append(f"(d) section trop courte : {nom} ({n} mots, au moins {mots_min})")

    # (e) contre-lectures : modèle nommé et empreinte résolue
    cl = s.get("Contre-lecture")
    if cl:
        motif = _modeles_motif(modeles)
        entrees = list(ENTREE.finditer(cl))
        morceaux = ([(f"contre-lecture {e.group(1)}",
                      cl[e.start():(entrees[k + 1].start() if k + 1 < len(entrees) else len(cl))])
                     for k, e in enumerate(entrees)] or [("section Contre-lecture", cl)])
        for nom, corps in morceaux:
            if not motif.search(corps):
                sortie.append(f"(e) {nom} sans le modèle du relecteur (attendu : {', '.join(modeles)})")
            if not any(h in resolues for h in HEX64.findall(corps)):
                sortie.append(f"(e) {nom} sans empreinte qui désigne un fichier du dépôt")
    return sortie, avert


def problemes_renforces(chemin: str | Path, racine: str | Path = ".", mots_min: int = MOTS_MIN,
                        index: Index | None = None) -> list[str]:
    return verifier_renforce(chemin, racine, mots_min=mots_min, index=index)[0]


def _main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(prog="python -m controle_ia.prereg_renforce_v1", description=__doc__.split("\n")[0])
    ap.add_argument("fichiers", nargs="+")
    ap.add_argument("--racine", default=".")
    ap.add_argument("--mots-min", type=int, default=MOTS_MIN)
    a = ap.parse_args(argv)
    index = Index(a.racine)
    code = 0
    for f in a.fichiers:
        try:
            pb, av = verifier_renforce(f, a.racine, mots_min=a.mots_min, index=index)
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
