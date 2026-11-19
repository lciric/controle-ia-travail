"""Garde statique du bras A des organismes discrets, version 6 du code (préenregistrement
`prereg/T0.7-organismes-discrets-v-a-v2-brouillon24.md`, 3.5 (b) ; 8.4, « fichier des scores par unité : cloisonnement » :
« fichier ouvert par un autre programme : refusé » ; 6.2, « tirage sans clé »).

Elle parcourt, par l'arbre syntaxique, les programmes des dossiers qu'on lui donne (l'enchaînement de l'analyse lui
donne `src` et `scripts`, depuis la racine du dépôt). Ce qui change depuis la version 5, d'après la contre-lecture du
code de la version 5 (défaut C-4, mineurs M-1 et M-8, essais d'attaque versés) :

- **autorisation par chemin exact et par empreinte** : le programme de l'aire conditionnelle est autorisé par son
  chemin relatif à la racine du dépôt, et seulement s'il répond à son empreinte compagnon ; un fichier du même nom
  rangé ailleurs (`scripts/analyse_bras_a_v3.py`) n'est plus autorisé ;
- **exclusion par préfixe de chemin exact** : le côté habilité, qui écrit le fichier, est exclu par le chemin de son
  dossier, non par un fragment de nom (`scripts/t07_lecture_rapide.py` n'est plus exclu) ;
- **noms recollés** : en plus de `+`, de la juxtaposition et des chaînes à trous, la garde remet bout à bout
  `"-".join([...])`, `"…%s…" % (...)`, `"…{}…".format(...)` et une chaîne retournée (`[::-1]`), pour le nom du fichier,
  pour les noms réservés et pour le nom du module de l'analyse ;
- **lecture d'un dossier** : un programme qui liste un dossier (`glob`, `rglob`, `iterdir`, `listdir`, `scandir`,
  `walk`) **et** nomme l'extension des fichiers de lignes JSON est le cas de mégarde le plus probable (un lanceur qui
  lit « tous les `.jsonl` d'une course »). **Ce n'est pas une garde** : sur le dépôt, huit programmes sans rapport avec
  le fichier des rangs le font à bon droit, et une garde qui les refuserait arrêterait à tort. `listages_a_relire`
  les **signale**, sans arrêter, pour qui contre-lit l'enchaînement ; la limite est écrite ci-dessous, en (e) ;
- **autres fichiers** : les fragments du nom sont cherchés aussi dans les fichiers de commandes et de réglages
  (`.sh`, `.bash`, `.zsh`, `.mk`, `Makefile`, `.ipynb`, `.yaml`, `.yml`, `.toml`, `.cfg`, `.ini`) ;
- **tirage à clé** (M-1) : hors du module des graines, dans tout programme qui importe ce module, toute mention du
  jeton, du constructeur du tirage à clé ou de son registre est refusée ;
- **porte de l'écart à R9** (M-8) : un programme qui importe une version des graines antérieure à la version 6 et
  nomme la porte de l'écart à R9 est refusé — la porte des versions 4 et 5, plus faible, ne s'emploie plus.

Ce qu'elle refuse, dans tout fichier qui n'est pas le programme de l'aire conditionnelle :
1. le nom du fichier des rangs, entier ou en morceaux remis bout à bout ;
2. les noms réservés du programme de l'aire conditionnelle (versions 4 à 6), comme nom, attribut, nom importé ou
   chaîne ;
3. dans un fichier qui importe le module de l'analyse (ou en écrit le nom dans une chaîne, hors de sa documentation) :
   `import *`, et tout accès indirect ;
4. dans un programme qui importe le module des graines : le jeton, le constructeur et le registre du tirage à clé ;
5. la porte de l'écart à R9 d'une version des graines antérieure à la version 6.
Un programme que l'analyseur ne lit pas est refusé lui aussi.

**Limites, écrites.** (a) La première barrière du cloisonnement est une règle de procédure — « aucun agent n'ouvre le
fichier des scores par unité » (3.5 (b)) — ; cette garde ne la remplace pas : elle voit le code des dossiers qu'on lui
donne, non ce qu'un agent fait à la main ni un programme rangé ailleurs. (b) Elle ne voit pas un nom **lu à
l'exécution** — dans la pièce scellée (`scores_par_unite.fichier`), dans un fichier, dans un argument — ni un nom
calculé autrement que par les six formes ci-dessus (essai : ce cas passe, et l'essai le dit). (c) Python ne cache
rien : l'objet qui porte les rangs et le registre des tirages restent atteignables à qui contourne tout cela exprès.
(d) Les essais touchent ces noms par nécessité ; `tests/` n'est pas un dossier gardé. (e) **Un programme qui lit tous
les fichiers d'un dossier lit aussi le fichier des rangs s'il s'y trouve, et la garde ne l'arrête pas** : elle le
signale seulement (`listages_a_relire`) quand l'extension est écrite, et ne le voit pas du tout sinon. Le fichier des
rangs doit donc être rangé dans un dossier qu'aucun lanceur ne parcourt : c'est une règle de procédure, à écrire par
qui écrit l'enchaînement.

Ce module ne lit que du code source ; il n'ouvre ni le fichier des rangs, ni aucun interne de moniteur.
"""
from __future__ import annotations

import ast
import re
from pathlib import Path
from typing import Iterable, Sequence

from ..gardes import GardeArret
from ..scellement import verifier

PAQUET = "src/controle_ia/organismes_discrets/"
# Le programme de l'aire conditionnelle et ses versions antérieures (laissées telles quelles, R12), par chemin exact.
PROGRAMMES_DE_L_AIRE_CONDITIONNELLE = tuple(PAQUET + f"analyse_bras_a_v{k}.py" for k in (3, 4, 5, 6))
GARDES_STATIQUES = tuple(PAQUET + f"cloisonnement_bras_a_v{k}.py" for k in (5, 6))
MODULES_DES_GRAINES = tuple(PAQUET + f"graines_bras_a_v{k}.py" for k in (5, 6))
# Le module des arrêts nomme la clé de la livraison qui décrit le fichier (liste fermée des noms qu'un arrêt peut dire).
AUTORISES_POUR_LES_RANGS = PROGRAMMES_DE_L_AIRE_CONDITIONNELLE + GARDES_STATIQUES + (PAQUET + "arrets_bras_a_v6.py",)
AUTORISES_POUR_LE_TIRAGE = MODULES_DES_GRAINES + GARDES_STATIQUES
# Le côté habilité écrit le fichier : son dossier est exclu, par son chemin exact, et rien n'en est lu.
EXCLUS_COTE_HABILITE = (PAQUET + "bras_a_v2_habilite/",)
DOSSIERS_GARDES = ("src", "scripts")
FRAGMENT_DU_NOM_DU_FICHIER = re.compile(r"(?:rangs|scores)[-_]par[-_]|par[-_]unite", re.I)
NOMS_RESERVES = ("lire_fichier_des_rangs", "_lire_les_rangs", "RangsScelles", "_pour_l_aire_conditionnelle",
                 "lire_fichier_des_scores", "ScoresScelles")
NOMS_DU_TIRAGE = ("_JETON", "TirageAClef", "_AUTHENTIQUES", "_SERVIS", "_inscrire")
PORTE_DE_L_ECART_A_R9 = "admettre_l_entropie_propre_de_la_table_des_identifiants"
GRAINES_ANTERIEURES = re.compile(r"graines_bras_a_v[1-5]\b")
MODULE_DE_L_ANALYSE = re.compile(r"analyse_bras_a_v")
MODULE_DES_GRAINES = re.compile(r"graines_bras_a_v")
ACCES_INDIRECTS = ("getattr", "setattr", "vars", "dir", "globals", "locals", "eval", "exec", "compile", "__import__",
                   "import_module", "__getattribute__", "__dict__", "attrgetter", "methodcaller")
LISTAGES = ("glob", "rglob", "iglob", "iterdir", "listdir", "scandir", "walk")
EXTENSION_DES_LIGNES_JSON = re.compile(r"jsonl", re.I)
SUFFIXES_DE_TEXTE = (".sh", ".bash", ".zsh", ".mk", ".ipynb", ".yaml", ".yml", ".toml", ".cfg", ".ini")
NOMS_DE_TEXTE = ("Makefile", "makefile", "GNUmakefile")


def _bout_a_bout(n: ast.AST) -> str | None:
    """Texte d'une expression faite de chaînes écrites : la chaîne elle-même ; les morceaux recollés par `+`, par une
    chaîne à trous, par `"…".join([...])`, par `%`, par `.format(...)` ; une chaîne retournée par `[::-1]`. Un morceau
    qui n'est pas écrit (une variable) compte pour rien. `None` si l'expression n'est pas de cette sorte."""
    if isinstance(n, ast.Constant):
        if isinstance(n.value, str):
            return n.value
        if isinstance(n.value, bytes):
            return n.value.decode("utf-8", "replace")
        return str(n.value) if isinstance(n.value, (int, float)) and not isinstance(n.value, bool) else None
    if isinstance(n, ast.JoinedStr):
        return "".join(_bout_a_bout(v) or "" for v in n.values)
    if isinstance(n, ast.FormattedValue):
        return _bout_a_bout(n.value) or ""
    if isinstance(n, ast.BinOp) and isinstance(n.op, ast.Add):
        g, d = _bout_a_bout(n.left), _bout_a_bout(n.right)
        return None if g is None and d is None else (g or "") + (d or "")
    if isinstance(n, ast.BinOp) and isinstance(n.op, ast.Mod):
        g = _bout_a_bout(n.left)
        if g is None:
            return None
        morceaux = [(_bout_a_bout(x) or "") for x in (n.right.elts if isinstance(n.right, ast.Tuple) else [n.right])]
        return _remplir(g, morceaux, r"%[sdirfg]")
    if isinstance(n, (ast.List, ast.Tuple)):
        return None
    if isinstance(n, ast.Call) and isinstance(n.func, ast.Attribute):
        base = _bout_a_bout(n.func.value)
        if base is not None and n.func.attr == "join" and len(n.args) == 1 and isinstance(n.args[0], (ast.List, ast.Tuple)):
            return base.join(_bout_a_bout(x) or "" for x in n.args[0].elts)
        if base is not None and n.func.attr == "format":
            return _remplir(base, [(_bout_a_bout(x) or "") for x in n.args], r"\{\d*\}")
        if base is not None and n.func.attr in ("lower", "upper", "strip", "casefold"):
            return base
    if isinstance(n, ast.Subscript) and isinstance(n.slice, ast.Slice) and n.slice.lower is None and n.slice.upper is None \
            and isinstance(n.slice.step, ast.UnaryOp) and isinstance(n.slice.step.op, ast.USub) \
            and isinstance(n.slice.step.operand, ast.Constant) and n.slice.step.operand.value == 1:
        base = _bout_a_bout(n.value)
        return None if base is None else base[::-1]
    return None


def _remplir(gabarit: str, morceaux: list[str], trou: str) -> str:
    suite = iter(morceaux)
    return re.sub(trou, lambda _: next(suite, ""), gabarit)


def _chaines(arbre: ast.AST) -> list[tuple[int, str]]:
    return [(getattr(n, "lineno", 0), t) for n in ast.walk(arbre) for t in [_bout_a_bout(n)] if t]


def _noms(arbre: ast.AST) -> list[tuple[int, str]]:
    """Tous les noms d'un programme : noms, attributs, noms importés, noms de fonctions, de classes, d'arguments."""
    noms: list[tuple[int, str]] = []
    for n in ast.walk(arbre):
        ligne = getattr(n, "lineno", 0)
        if isinstance(n, ast.Name):
            noms.append((ligne, n.id))
        elif isinstance(n, ast.Attribute):
            noms.append((ligne, n.attr))
        elif isinstance(n, (ast.Import, ast.ImportFrom)):
            for a in n.names:
                noms += [(ligne, a.name), (ligne, a.asname or "")]
            if getattr(n, "module", None):
                noms.append((ligne, n.module))
        elif isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            noms.append((ligne, n.name))
        elif isinstance(n, ast.arg):
            noms.append((ligne, n.arg))
        elif isinstance(n, ast.keyword) and n.arg:
            noms.append((ligne, n.arg))
    return noms


def violations_d_un_programme(source: str, nom: str, *, pour_les_rangs: bool = True, pour_le_tirage: bool = True) -> list[str]:
    """Violations dans le texte d'un programme Python. `pour_les_rangs` : règles 1 à 3 (fichier des rangs) ;
    `pour_le_tirage` : règles 4 et 5 (tirage à clé, porte de l'écart à R9)."""
    try:
        arbre = ast.parse(source)
    except SyntaxError as e:
        return [f"{nom} : programme illisible par l'analyseur (ligne {e.lineno}) — il ne peut pas être dit propre"]
    trouve: list[str] = []
    chaines, noms = _chaines(arbre), _noms(arbre)
    documentation = {id(n.body[0].value) for n in ast.walk(arbre)
                     if isinstance(n, (ast.Module, ast.ClassDef, ast.FunctionDef, ast.AsyncFunctionDef)) and n.body
                     and isinstance(n.body[0], ast.Expr) and isinstance(n.body[0].value, ast.Constant)
                     and isinstance(n.body[0].value.value, str)}
    hors_documentation = [(getattr(n, "lineno", 0), t) for n in ast.walk(arbre) if id(n) not in documentation
                          for t in [_bout_a_bout(n)] if t]
    if pour_les_rangs:
        for ligne, t in chaines:
            if FRAGMENT_DU_NOM_DU_FICHIER.search(t):
                trouve.append(f"{nom}, ligne {ligne} : fragment du nom du fichier des rangs par unité dans une chaîne")
            for r in NOMS_RESERVES:
                if r in t:
                    trouve.append(f"{nom}, ligne {ligne} : nom réservé `{r}` écrit dans une chaîne")
        for ligne, x in noms:
            for r in NOMS_RESERVES:
                if r in x:
                    trouve.append(f"{nom}, ligne {ligne} : nom réservé `{r}`")
        importe = any(MODULE_DE_L_ANALYSE.search(x) for _, x in noms) \
            or any(MODULE_DE_L_ANALYSE.search(t) for _, t in hors_documentation)
        if importe:
            for n in ast.walk(arbre):
                if isinstance(n, ast.ImportFrom) and any(a.name == "*" for a in n.names) \
                        and MODULE_DE_L_ANALYSE.search(n.module or ""):
                    trouve.append(f"{nom}, ligne {n.lineno} : `import *` depuis le module de l'analyse")
            for ligne, x in noms:
                if x in ACCES_INDIRECTS:
                    trouve.append(f"{nom}, ligne {ligne} : accès indirect `{x}` dans un programme qui importe le module "
                                  "de l'analyse")
    graines = any(MODULE_DES_GRAINES.search(x) for _, x in noms) or any(MODULE_DES_GRAINES.search(t) for _, t in hors_documentation)
    if pour_le_tirage and graines:
        for ligne, x in noms:
            if x in NOMS_DU_TIRAGE:
                trouve.append(f"{nom}, ligne {ligne} : `{x}` hors du module des graines — un tirage à clé ne se fabrique "
                              "que par ses fabriques")
        for ligne, t in hors_documentation:
            if any(r in t for r in ("_JETON", "TirageAClef")):
                trouve.append(f"{nom}, ligne {ligne} : nom du tirage à clé écrit dans une chaîne")
        if any(GRAINES_ANTERIEURES.search(x) for _, x in noms) and any(x == PORTE_DE_L_ECART_A_R9 for _, x in noms):
            trouve.append(f"{nom} : porte de l'écart à R9 d'une version des graines antérieure à la version 6")
    return trouve


def listages_d_un_programme(source: str, nom: str) -> list[str]:
    """**Signalement, non garde** : un programme qui liste un dossier et nomme l'extension des fichiers de lignes JSON.
    Il pourrait lire le fichier des rangs par mégarde s'il s'y trouvait ; à relire par qui contre-lit l'enchaînement."""
    try:
        arbre = ast.parse(source)
    except SyntaxError:
        return []
    listages = [(ligne, x) for ligne, x in _noms(arbre) if x in LISTAGES]
    if listages and any(EXTENSION_DES_LIGNES_JSON.search(t) for _, t in _chaines(arbre)):
        return [f"{nom}, ligne {listages[0][0]} : lecture d'un dossier (`{listages[0][1]}`) de fichiers de lignes JSON"]
    return []


def _relatif(f: Path, racine: Path) -> str:
    return f.resolve().relative_to(racine.resolve()).as_posix()


def violations_de_la_garde_statique(racine, dossiers: Iterable[str] = DOSSIERS_GARDES, *,
                                    exclus: Sequence[str] = EXCLUS_COTE_HABILITE) -> list[str]:
    """Parcourt, depuis la racine du dépôt, les dossiers donnés (chemins relatifs ; un fichier seul est admis) et rend
    les violations. `exclus` : préfixes de chemin exacts, relatifs à la racine, du côté habilité — jamais lus. Les
    programmes autorisés le sont **par leur chemin exact**, et doivent répondre à leur empreinte compagnon : sinon ils
    sont eux-mêmes une violation. Un dossier absent est refusé (une garde qui ne lit rien ne dit rien)."""
    racine = Path(racine)
    dossiers = list(dossiers)
    if not racine.is_dir() or not dossiers:
        raise GardeArret("garde statique : la racine du dépôt et au moins un dossier à parcourir sont exigés")
    if isinstance(exclus, (str, bytes)) or any(not isinstance(x, str) or not x for x in exclus):
        raise GardeArret("garde statique : exclusions par préfixes de chemin, relatifs à la racine, exigées")
    trouve: list[str] = []
    for d in dossiers:
        depart = racine / d
        if not depart.exists():
            raise GardeArret(f"garde statique : {d} absent sous la racine — une garde qui ne lit rien ne dit rien")
        fichiers = [depart] if depart.is_file() else sorted(p for p in depart.rglob("*") if p.is_file())
        for f in fichiers:
            chemin = _relatif(f, racine)
            if any(chemin.startswith(x) for x in exclus) or "/__pycache__/" in "/" + chemin:
                continue
            pour_les_rangs, pour_le_tirage = chemin not in AUTORISES_POUR_LES_RANGS, chemin not in AUTORISES_POUR_LE_TIRAGE
            if not (pour_les_rangs and pour_le_tirage):
                try:
                    verifier(f)
                except GardeArret:
                    trouve.append(f"{chemin} : programme autorisé par son chemin, mais qui ne répond pas à son empreinte "
                                  "compagnon — il n'est pas le programme scellé")
            if f.suffix == ".py":
                try:
                    source = f.read_text(encoding="utf-8")
                except UnicodeDecodeError:
                    trouve.append(f"{chemin} : programme illisible (encodage) — il ne peut pas être dit propre")
                    continue
                trouve += violations_d_un_programme(source, chemin, pour_les_rangs=pour_les_rangs, pour_le_tirage=pour_le_tirage)
            elif f.suffix in SUFFIXES_DE_TEXTE or f.name in NOMS_DE_TEXTE:
                for k, ligne in enumerate(f.read_text(encoding="utf-8", errors="replace").splitlines(), 1):
                    if FRAGMENT_DU_NOM_DU_FICHIER.search(ligne):
                        trouve.append(f"{chemin}, ligne {k} : fragment du nom du fichier des rangs par unité dans un "
                                      "fichier de commandes ou de réglages")
    return trouve


def exiger_garde_statique(racine, dossiers: Iterable[str] = DOSSIERS_GARDES, *,
                          exclus: Sequence[str] = EXCLUS_COTE_HABILITE) -> None:
    """Garde statique (3.5 (b) ; 8.4 ; 6.2) : arrêt si un programme autre que celui de l'aire conditionnelle nomme le
    fichier des rangs par unité, touche l'un des noms réservés, atteint le module de l'analyse par un détour ou lit un
    dossier de fichiers de lignes JSON ; ou si un programme autre que le module des graines touche au tirage à clé.
    Limites écrites en tête du module."""
    trouve = violations_de_la_garde_statique(racine, dossiers, exclus=exclus)
    if trouve:
        raise GardeArret("garde statique du bras A : " f"{len(trouve)} violation(s) : " + " | ".join(trouve[:8]))


def listages_a_relire(racine, dossiers: Iterable[str] = DOSSIERS_GARDES, *,
                      exclus: Sequence[str] = EXCLUS_COTE_HABILITE) -> list[str]:
    """Les programmes des dossiers donnés qui lisent un dossier de fichiers de lignes JSON (limite (e) de l'en-tête) :
    **liste à relire, sans arrêt**. Le programme de l'aire conditionnelle et les exclus n'y sont pas."""
    racine = Path(racine)
    signales: list[str] = []
    for d in dossiers:
        depart = racine / d
        if not depart.exists():
            raise GardeArret(f"garde statique : {d} absent sous la racine")
        for f in ([depart] if depart.is_file() else sorted(p for p in depart.rglob("*.py") if p.is_file())):
            chemin = _relatif(f, racine)
            if f.suffix != ".py" or any(chemin.startswith(x) for x in exclus) or chemin in AUTORISES_POUR_LES_RANGS:
                continue
            try:
                signales += listages_d_un_programme(f.read_text(encoding="utf-8"), chemin)
            except UnicodeDecodeError:
                continue
    return signales
