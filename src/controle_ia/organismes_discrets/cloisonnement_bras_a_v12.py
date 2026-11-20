"""Garde statique du bras A des organismes discrets, version 12 du code (préenregistrement
`prereg/T0.7-organismes-discrets-v-a-v2-brouillon35.md`, 3.5 (b) ; conventions, « Qui en lit le contenu » ; 8.4,
« fichier des scores par unité : cloisonnement » ; 6.2, « tirage sans clé »).

Elle parcourt, par l'arbre syntaxique, les programmes des dossiers qu'on lui donne (l'enchaînement de l'analyse lui
donne `src` et `scripts`, depuis la racine du dépôt). `cloisonnement_bras_a_v11.py` n'est pas modifié (R12). **Ce qui
change à la version 12** : les programmes autorisés sont ceux des versions 3 à 12 ; rien d'autre — la porte de
l'écart à R9 de la version 11 des graines, que sa vérification tient pour sûre, reste admise. **Ce qui avait changé à
la version 11** (vérification du code de la version 10, M-1) : les programmes autorisés étaient ceux des versions 3
à 11 ; la porte de l'écart à R9 de la version 10 des graines, qui s'ouvrait sur une ligne où la phrase
d'accord n'était qu'une partie de l'objet — « aucun écart à R9 accordé… » —, rejoint les portes refusées. **Ce qui
avait changé à la version 10** : la porte de la version 9 des graines, qui ne voyait ni un identifiant sans tiret ni
une empreinte abrégée, avait rejoint les portes refusées. **Ce qui avait changé à la version 9** (vérification du code de la version 8, M-5) : **un lien physique n'est plus ouvert** — un
fichier qui porte plusieurs noms pourrait être un fichier cloisonné sous un autre nom ; la garde ne l'ouvre pas et le
dit par une violation, comme un lien symbolique. Les programmes autorisés sont ceux des versions 3 à 9 ; la porte de
l'écart à R9 de la version 8 des graines, qui ne voyait une révocation qu'à l'orthographe de son type, rejoint les
portes refusées. **Ce qui avait changé à la version 8** (vérification du code de la version 7, M-4) : **les motifs des chemins cloisonnés sont
jugés sans égard à la casse**, tous — un dossier `T07/` ou `Bases/` était lu, alors que la marque de T0.8 était déjà
jugée sans la casse ; dans le doute, la garde n'entre pas. Et la porte de l'écart à R9 de la version 7 des graines,
qui lisait le registre du dépôt, rejoint les portes refusées. Le reste est celui de la version 7, d'après la
vérification du code de la version 6 (C-3, M-8) :

- **l'élagage des chemins cloisonnés est le défaut du module, et il ne se retire pas** (C-3). La version 6 n'écartait
  par défaut que le dossier du côté habilité : appelée telle quelle, elle faisait ouvrir par programme les dossiers
  d'internes des moniteurs, que la relance ne doit pas ouvrir, et pouvait y arrêter à tort. Ici, `est_cloisonne` est
  jugé **avant tout parcours** : un dossier cloisonné n'est jamais listé, un fichier cloisonné jamais ouvert, quel que
  soit l'appelant. L'appelant peut **ajouter** des chemins à élaguer (`cloisonnes_de_plus`), jamais en retirer. Un
  dossier de départ lui-même cloisonné est refusé. Ce qui est élagué est rendu, par son nom seul
  (`chemins_elagues`), pour que l'enchaînement dise ce que la garde n'a pas regardé : aucun repli silencieux ;
- **le parcours ne suit aucun lien symbolique** : un lien mènerait dans un chemin cloisonné sans le nommer ; un lien
  rencontré est une violation (« il ne peut pas être dit propre ») ;
- **noms recollés, deux formes de plus** (M-8) : `"-".join(x for x in [...])`, et une chaîne faite de variables
  affectées une fois d'une chaîne écrite (`a = "rangs"` … `f"{a}-par-…"`) ;
- **tirage à clé** (M-8) : le générateur d'un tirage (`_generateur`) entre dans les noms refusés hors du module des
  graines.

**Ce qui est cloisonné, par défaut** (liste à confirmer par la session principale : demande 17 de la note du brouillon
25) :
- tout **dossier** nommé `t07…`, `bases`, `sondes`, ou dont le nom porte `bras_a_v2_habilite`, à quelque profondeur
  que ce soit ;
- tout **dossier ou fichier** dont le nom porte `mots_et_cout_`, `autres_moniteurs_v` ou `bras_a_v2_habilite`, ou une
  marque de T0.8 (`t08`, `t0.8`, `t0_8`, `t0-8`, sans égard à la casse) ;
- les chemins `prereg/T0.6-organismes-v0-v1.md` (et son compagnon), et, sous `docs/notes/bras-a-moniteurs-v1/`, les
  notices (`notice-…`), les contre-lectures du code (`contre-lecture-code-…`) et les vérifications des lots
  (`verification-lots-…`).
C'est plus large que les seuls préfixes de la vérification (`scripts/mots_et_cout_…` devient « tout nom qui porte
`mots_et_cout_` ») : dans le doute, la garde n'entre pas. Le prix : un programme rangé sous un de ces noms n'est pas
regardé — c'est le côté habilité, qui écrit le fichier et le nomme à bon droit.

Ce qu'elle refuse, dans tout fichier qui n'est pas le programme de l'aire conditionnelle :
1. le nom du fichier des rangs, entier ou en morceaux remis bout à bout ;
2. les noms réservés du programme de l'aire conditionnelle (versions 4 à 11), comme nom, attribut, nom importé ou
   chaîne ;
3. dans un fichier qui importe le module de l'analyse (ou en écrit le nom dans une chaîne, hors de sa documentation) :
   `import *`, et tout accès indirect ;
4. dans un programme qui importe le module des graines : le jeton, le constructeur, le registre et le générateur du
   tirage à clé ;
5. la porte de l'écart à R9 d'une version des graines antérieure à la version 11 (les versions 1 à 7 lisaient le
   registre du dépôt ; la version 8 ne voyait une révocation qu'à l'orthographe de son type ; la version 9 ne voyait
   pas un identifiant écrit sans tiret ; la version 10 cherchait la phrase d'accord comme une partie de la ligne).
Un programme que l'analyseur ne lit pas, un lien symbolique ou un lien physique est refusé lui aussi.

**Lecture d'un dossier : signalement, non garde.** Un programme qui liste un dossier et nomme l'extension des fichiers
de lignes JSON est signalé par `listages_a_relire`, sans arrêt (sur le dépôt, des programmes sans rapport le font à
bon droit). Le texte porte la règle, bornée au contenu (conventions, « Qui en lit le contenu ») : aucun programme ne
lit ni n'affiche le contenu du fichier des scores par unité, hors le programme de l'aire conditionnelle, qui l'ouvre
par son chemin exact ; les outils de scellement et de version n'en prennent que l'empreinte.

**Limites, écrites.** (a) La première barrière du cloisonnement est une règle de procédure — « aucun agent n'ouvre le
fichier des scores par unité » (3.5 (b)) — ; cette garde ne la remplace pas. (b) Elle ne voit pas un nom **lu à
l'exécution** — dans la pièce scellée, dans un fichier, dans un argument — ni un nom calculé autrement que par les
formes ci-dessus ; une variable affectée plusieurs fois compte pour sa première valeur. (c) Python ne cache rien :
l'objet qui porte les rangs et le registre des tirages restent atteignables à qui contourne tout cela exprès. (d) Les
essais touchent ces noms par nécessité ; `tests/` n'est pas un dossier gardé. (e) Un programme qui lit tous les
fichiers d'un dossier sans écrire l'extension n'est ni refusé ni signalé : c'est la règle du dossier qui tient là.
(f) Un programme rangé dans un chemin cloisonné n'est pas regardé. (g) **Le cloisonnement tient aux noms** : un
programme de T0.8, ou un interne de moniteur, rangé sous un nom qui ne porte aucune des marques ci-dessus serait
ouvert et lu comme un programme ordinaire (vérification du code de la version 8, M-5) ; la liste est à confirmer par
le lecteur habilité.

Ce module ne lit que du code source ; il n'ouvre ni le fichier des rangs, ni aucun interne de moniteur.
"""
from __future__ import annotations

import ast
import fnmatch
import os
import re
from pathlib import Path
from typing import Iterable, Iterator, Sequence

from ..gardes import GardeArret
from ..scellement import verifier

PAQUET = "src/controle_ia/organismes_discrets/"
# Le programme de l'aire conditionnelle et ses versions antérieures (laissées telles quelles, R12), par chemin exact.
PROGRAMMES_DE_L_AIRE_CONDITIONNELLE = tuple(PAQUET + f"analyse_bras_a_v{k}.py" for k in (3, 4, 5, 6, 7, 8, 9, 10, 11, 12))
GARDES_STATIQUES = tuple(PAQUET + f"cloisonnement_bras_a_v{k}.py" for k in (5, 6, 7, 8, 9, 10, 11, 12))
MODULES_DES_GRAINES = tuple(PAQUET + f"graines_bras_a_v{k}.py" for k in (5, 6, 7, 8, 9, 10, 11, 12))
# Les modules des arrêts nomment la clé de la livraison qui décrit le fichier (liste fermée des noms qu'un arrêt peut dire).
MODULES_DES_ARRETS = tuple(PAQUET + f"arrets_bras_a_v{k}.py" for k in (6, 7, 8, 9, 10, 11, 12))
AUTORISES_POUR_LES_RANGS = PROGRAMMES_DE_L_AIRE_CONDITIONNELLE + GARDES_STATIQUES + MODULES_DES_ARRETS
AUTORISES_POUR_LE_TIRAGE = MODULES_DES_GRAINES + GARDES_STATIQUES
DOSSIERS_GARDES = ("src", "scripts")

# --- Chemins cloisonnés : élagués avant tout parcours, par défaut, sans moyen de les retirer (C-3) -------------------------
DOSSIERS_CLOISONNES = ("t07*", "bases", "sondes")                     # nom d'un dossier, à toute profondeur
NOMS_CLOISONNES = ("*mots_et_cout_*", "*autres_moniteurs_v*", "*bras_a_v2_habilite*")   # nom d'un dossier ou d'un fichier
MARQUE_DE_T0_8 = re.compile(r"(?<![a-z0-9])t0[._-]?8(?![0-9])", re.I)  # nom d'un dossier ou d'un fichier
CHEMINS_CLOISONNES = ("prereg/T0.6-organismes-v0-v1.md*",             # chemin relatif à la racine, composante par composante
                      "docs/notes/bras-a-moniteurs-v1/notice-*",
                      "docs/notes/bras-a-moniteurs-v1/contre-lecture-code-*",
                      "docs/notes/bras-a-moniteurs-v1/verification-lots-*")

FRAGMENT_DU_NOM_DU_FICHIER = re.compile(r"(?:rangs|scores)[-_]par[-_]|par[-_]unite", re.I)
NOMS_RESERVES = ("lire_fichier_des_rangs", "_lire_les_rangs", "RangsScelles", "_pour_l_aire_conditionnelle",
                 "lire_fichier_des_scores", "ScoresScelles")
NOMS_DU_TIRAGE = ("_JETON", "TirageAClef", "_AUTHENTIQUES", "_SERVIS", "_inscrire", "_generateur")
PORTE_DE_L_ECART_A_R9 = "admettre_l_entropie_propre_de_la_table_des_identifiants"
# registre du dépôt (1 à 7) ; révocation vue au type (8), au tiret (9) ; phrase d'accord cherchée comme une partie (10)
GRAINES_ANTERIEURES = re.compile(r"graines_bras_a_v(?:[1-9]|10)\b")
MODULE_DE_L_ANALYSE = re.compile(r"analyse_bras_a_v")
MODULE_DES_GRAINES = re.compile(r"graines_bras_a_v")
ACCES_INDIRECTS = ("getattr", "setattr", "vars", "dir", "globals", "locals", "eval", "exec", "compile", "__import__",
                   "import_module", "__getattribute__", "__dict__", "attrgetter", "methodcaller")
LISTAGES = ("glob", "rglob", "iglob", "iterdir", "listdir", "scandir", "walk")
EXTENSION_DES_LIGNES_JSON = re.compile(r"jsonl", re.I)
SUFFIXES_DE_TEXTE = (".sh", ".bash", ".zsh", ".mk", ".ipynb", ".yaml", ".yml", ".toml", ".cfg", ".ini")
NOMS_DE_TEXTE = ("Makefile", "makefile", "GNUmakefile")


def _motifs(cloisonnes_de_plus) -> tuple[str, ...]:
    if isinstance(cloisonnes_de_plus, (str, bytes)) or any(not isinstance(x, str) or not x.strip("/") for x in cloisonnes_de_plus):
        raise GardeArret("garde statique : chemins à élaguer en plus — motifs de chemin relatifs à la racine, non vides")
    return CHEMINS_CLOISONNES + tuple(x.strip("/") for x in cloisonnes_de_plus)


def _repond(nom: str, motif: str) -> bool:
    """Un nom répond à un motif **sans égard à la casse** (vérification du code de la version 7, M-4)."""
    return fnmatch.fnmatchcase(nom.casefold(), motif.casefold())


def est_cloisonne(chemin_relatif: str, est_un_dossier: bool, cloisonnes_de_plus: Sequence[str] = ()) -> bool:
    """Vrai si ce chemin, relatif à la racine du dépôt, est cloisonné : la garde n'y entre pas. Jugé sur les **noms
    seuls**, composante par composante, sans rien ouvrir ni lister :
    - une composante qui est un dossier et répond à `DOSSIERS_CLOISONNES` ;
    - une composante quelconque qui répond à `NOMS_CLOISONNES` ou porte la marque de T0.8 ;
    - un chemin dont les premières composantes répondent à un motif de `CHEMINS_CLOISONNES` ou à un motif ajouté par
      l'appelant.
    La liste par défaut ne se retire pas. Tous les motifs sont jugés sans égard à la casse."""
    parties = [p for p in str(chemin_relatif).split("/") if p not in ("", ".")]
    if ".." in parties:
        raise GardeArret("garde statique : chemin qui remonte (`..`) refusé")
    for k, nom in enumerate(parties):
        dossier = k < len(parties) - 1 or est_un_dossier
        if dossier and any(_repond(nom, m) for m in DOSSIERS_CLOISONNES):
            return True
        if any(_repond(nom, m) for m in NOMS_CLOISONNES) or MARQUE_DE_T0_8.search(nom):
            return True
    for motif in _motifs(cloisonnes_de_plus):
        m = motif.split("/")
        if len(parties) >= len(m) and all(_repond(p, x) for p, x in zip(parties, m)):
            return True
    return False


def _plusieurs_noms(fichier: Path) -> bool:
    """Vrai si ce fichier ordinaire porte plusieurs noms (lien physique). Lu sur ses seules métadonnées : il n'est
    pas ouvert."""
    return os.lstat(fichier).st_nlink > 1


def _parcourir(racine: Path, depart: str, cloisonnes_de_plus: Sequence[str], elagues: list[str], liens: list[str],
               physiques: list[str], suffixe: str | None = None) -> Iterator[tuple[Path, str]]:
    """Les fichiers sous `racine/depart`, avec leur chemin relatif, dans l'ordre des noms. **Élagage avant tout
    parcours** : `est_cloisonne` est jugé sur le nom d'une entrée avant de la lister ou de la rendre ; un dossier
    cloisonné n'est jamais listé. Aucun lien symbolique n'est suivi ni ouvert. **Un fichier qui porte plusieurs noms
    (lien physique) n'est pas rendu** : il n'est pas ouvert, et son chemin est noté (`physiques`). Les dossiers
    `__pycache__` sont sautés."""
    relatif = depart.strip("/")
    if est_cloisonne(relatif, (racine / relatif).is_dir(), cloisonnes_de_plus):
        raise GardeArret(f"garde statique : `{relatif}` est un chemin cloisonné — la garde n'y entre pas, et ne dit donc "
                         "rien de lui ; le retirer des dossiers à parcourir")
    premier = racine / relatif
    if premier.is_symlink():
        liens.append(relatif)
        return
    if premier.is_file():
        if _plusieurs_noms(premier):
            physiques.append(relatif)
        else:
            yield premier, relatif
        return
    pile = [relatif]
    while pile:
        d = pile.pop()
        with os.scandir(racine / d) as entrees:
            noms = sorted((e.name, e.is_symlink(), e.is_dir(follow_symlinks=False)) for e in entrees)
        sous = []
        for nom, lien, dossier in noms:
            chemin = f"{d}/{nom}"
            if est_cloisonne(chemin, dossier, cloisonnes_de_plus):
                elagues.append(chemin + ("/" if dossier else ""))
            elif lien:
                liens.append(chemin)
            elif dossier:
                if nom != "__pycache__":
                    sous.append(chemin)
            elif suffixe is None or nom.endswith(suffixe):
                if _plusieurs_noms(racine / chemin):
                    physiques.append(chemin)
                else:
                    yield racine / chemin, chemin
        pile.extend(reversed(sous))


def _bout_a_bout(n: ast.AST, env: dict | None = None) -> str | None:
    """Texte d'une expression faite de chaînes écrites : la chaîne elle-même ; les morceaux recollés par `+`, par une
    chaîne à trous, par `"…".join([...])` ou `"…".join(x for x in [...])`, par `%`, par `.format(...)` ; une chaîne
    retournée par `[::-1]` ; une variable de `env` (affectée d'une chaîne écrite). Un morceau qui n'est pas écrit
    compte pour rien. `None` si l'expression n'est pas de cette sorte."""
    env = env or {}
    _b = lambda x: _bout_a_bout(x, env)  # noqa: E731
    if isinstance(n, ast.Name):
        return env.get(n.id)
    if isinstance(n, ast.Constant):
        if isinstance(n.value, str):
            return n.value
        if isinstance(n.value, bytes):
            return n.value.decode("utf-8", "replace")
        return str(n.value) if isinstance(n.value, (int, float)) and not isinstance(n.value, bool) else None
    if isinstance(n, ast.JoinedStr):
        return "".join(_b(v) or "" for v in n.values)
    if isinstance(n, ast.FormattedValue):
        return _b(n.value) or ""
    if isinstance(n, ast.BinOp) and isinstance(n.op, ast.Add):
        g, d = _b(n.left), _b(n.right)
        return None if g is None and d is None else (g or "") + (d or "")
    if isinstance(n, ast.BinOp) and isinstance(n.op, ast.Mod):
        g = _b(n.left)
        if g is None:
            return None
        morceaux = [(_b(x) or "") for x in (n.right.elts if isinstance(n.right, ast.Tuple) else [n.right])]
        return _remplir(g, morceaux, r"%[sdirfg]")
    if isinstance(n, (ast.List, ast.Tuple)):
        return None
    if isinstance(n, ast.Call) and isinstance(n.func, ast.Attribute):
        base = _b(n.func.value)
        if base is not None and n.func.attr == "join" and len(n.args) == 1:
            elts = _elements_joints(n.args[0])
            if elts is not None:
                return base.join(_b(x) or "" for x in elts)
        if base is not None and n.func.attr == "format":
            return _remplir(base, [(_b(x) or "") for x in n.args], r"\{\d*\}")
        if base is not None and n.func.attr in ("lower", "upper", "strip", "casefold"):
            return base
    if isinstance(n, ast.Subscript) and isinstance(n.slice, ast.Slice) and n.slice.lower is None and n.slice.upper is None \
            and isinstance(n.slice.step, ast.UnaryOp) and isinstance(n.slice.step.op, ast.USub) \
            and isinstance(n.slice.step.operand, ast.Constant) and n.slice.step.operand.value == 1:
        base = _b(n.value)
        return None if base is None else base[::-1]
    return None


def _elements_joints(arg: ast.AST):
    """Éléments d'un `join` : ceux d'une liste écrite, ou d'une compréhension qui parcourt une liste écrite sans la
    filtrer ni la transformer (`x for x in [...]`). `None` sinon."""
    if isinstance(arg, (ast.List, ast.Tuple)):
        return arg.elts
    if isinstance(arg, (ast.GeneratorExp, ast.ListComp)) and len(arg.generators) == 1:
        g = arg.generators[0]
        if not g.ifs and isinstance(g.iter, (ast.List, ast.Tuple)) and isinstance(g.target, ast.Name) \
                and isinstance(arg.elt, ast.Name) and arg.elt.id == g.target.id:
            return g.iter.elts
    return None


def _variables(arbre: ast.AST) -> dict:
    """Variables affectées d'une chaîne écrite (`a = "rangs"` ; `a, b = "rangs", "unite"`), pour recoller une chaîne
    faite de variables. Une variable affectée plusieurs fois garde sa première valeur (limite (b))."""
    env: dict = {}
    for _ in range(3):                                     # quelques passes : une variable faite d'une autre
        for n in ast.walk(arbre):
            if not isinstance(n, ast.Assign):
                continue
            for cible in n.targets:
                paires = [(cible, n.value)]
                if isinstance(cible, (ast.Tuple, ast.List)) and isinstance(n.value, (ast.Tuple, ast.List)) \
                        and len(cible.elts) == len(n.value.elts):
                    paires = list(zip(cible.elts, n.value.elts))
                for c, v in paires:
                    if isinstance(c, ast.Name) and c.id not in env:
                        t = _bout_a_bout(v, env)
                        if t:
                            env[c.id] = t
    return env


def _remplir(gabarit: str, morceaux: list[str], trou: str) -> str:
    suite = iter(morceaux)
    return re.sub(trou, lambda _: next(suite, ""), gabarit)


def _chaines(arbre: ast.AST, env: dict | None = None) -> list[tuple[int, str]]:
    return [(getattr(n, "lineno", 0), t) for n in ast.walk(arbre) if not isinstance(n, ast.Name)
            for t in [_bout_a_bout(n, env)] if t]


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
    env = _variables(arbre)
    chaines, noms = _chaines(arbre, env), _noms(arbre)
    documentation = {id(n.body[0].value) for n in ast.walk(arbre)
                     if isinstance(n, (ast.Module, ast.ClassDef, ast.FunctionDef, ast.AsyncFunctionDef)) and n.body
                     and isinstance(n.body[0], ast.Expr) and isinstance(n.body[0].value, ast.Constant)
                     and isinstance(n.body[0].value.value, str)}
    hors_documentation = [(getattr(n, "lineno", 0), t) for n in ast.walk(arbre)
                          if id(n) not in documentation and not isinstance(n, ast.Name) for t in [_bout_a_bout(n, env)] if t]
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
            if any(r in t for r in NOMS_DU_TIRAGE):
                trouve.append(f"{nom}, ligne {ligne} : nom du tirage à clé écrit dans une chaîne")
        if any(GRAINES_ANTERIEURES.search(x) for _, x in noms) and any(x == PORTE_DE_L_ECART_A_R9 for _, x in noms):
            trouve.append(f"{nom} : porte de l'écart à R9 d'une version des graines antérieure à la version 11")
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


def _lire_les_dossiers(racine, dossiers, cloisonnes_de_plus, suffixe=None):
    racine = Path(racine)
    dossiers = list(dossiers) if not isinstance(dossiers, (str, bytes)) else []
    if not racine.is_dir() or not dossiers or any(not isinstance(d, str) or not d.strip("/") for d in dossiers):
        raise GardeArret("garde statique : la racine du dépôt et au moins un dossier à parcourir (chemins relatifs) sont exigés")
    _motifs(cloisonnes_de_plus)
    racine = racine.resolve()
    elagues: list[str] = []
    liens: list[str] = []
    physiques: list[str] = []
    fichiers: list[tuple[Path, str]] = []
    for d in dossiers:
        d = d.strip("/")
        if ".." in d.split("/") or os.path.isabs(d):
            raise GardeArret(f"garde statique : dossier {d!r} — chemin relatif à la racine, qui ne remonte pas, exigé")
        if not os.path.lexists(racine / d):
            raise GardeArret(f"garde statique : {d} absent sous la racine — une garde qui ne lit rien ne dit rien")
        fichiers += list(_parcourir(racine, d, cloisonnes_de_plus, elagues, liens, physiques, suffixe))
    return fichiers, elagues, liens, physiques


def violations_de_la_garde_statique(racine, dossiers: Iterable[str] = DOSSIERS_GARDES, *,
                                    cloisonnes_de_plus: Sequence[str] = ()) -> list[str]:
    """Parcourt, depuis la racine du dépôt, les dossiers donnés (chemins relatifs ; un fichier seul est admis) et rend
    les violations. **Les chemins cloisonnés sont élagués avant tout parcours, par défaut** (`est_cloisonne`) ;
    `cloisonnes_de_plus` en ajoute, sans pouvoir en retirer. Les programmes autorisés le sont **par leur chemin exact**,
    et doivent répondre à leur empreinte compagnon : sinon ils sont eux-mêmes une violation. Un dossier absent ou
    cloisonné est refusé (une garde qui ne lit rien ne dit rien) ; un lien symbolique est une violation, **un lien
    physique aussi** (un fichier qui porte plusieurs noms : non ouvert)."""
    fichiers, _, liens, physiques = _lire_les_dossiers(racine, dossiers, cloisonnes_de_plus)
    trouve = [f"{chemin} : lien symbolique — non suivi, non ouvert ; il ne peut pas être dit propre" for chemin in liens]
    trouve += [f"{chemin} : lien physique (ce fichier porte plusieurs noms) — non ouvert ; il ne peut pas être dit propre"
               for chemin in physiques]
    for f, chemin in fichiers:
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
                          cloisonnes_de_plus: Sequence[str] = ()) -> None:
    """Garde statique (3.5 (b) ; 8.4 ; 6.2) : arrêt si un programme autre que celui de l'aire conditionnelle nomme le
    fichier des rangs par unité, touche l'un des noms réservés ou atteint le module de l'analyse par un détour ; ou si
    un programme autre que le module des graines touche au tirage à clé. Les chemins cloisonnés ne sont pas
    parcourus. Limites écrites en tête du module."""
    trouve = violations_de_la_garde_statique(racine, dossiers, cloisonnes_de_plus=cloisonnes_de_plus)
    if trouve:
        raise GardeArret("garde statique du bras A : " f"{len(trouve)} violation(s) : " + " | ".join(trouve[:8]))


def chemins_elagues(racine, dossiers: Iterable[str] = DOSSIERS_GARDES, *, cloisonnes_de_plus: Sequence[str] = ()) -> list[str]:
    """Les chemins cloisonnés rencontrés sous les dossiers donnés, **par leur nom seul** (un dossier finit par `/`) :
    ce que la garde n'a pas regardé. Rien n'y est listé ni ouvert. À joindre au rapport de l'enchaînement."""
    return _lire_les_dossiers(racine, dossiers, cloisonnes_de_plus)[1]


def listages_a_relire(racine, dossiers: Iterable[str] = DOSSIERS_GARDES, *, cloisonnes_de_plus: Sequence[str] = ()) -> list[str]:
    """Les programmes des dossiers donnés qui lisent un dossier de fichiers de lignes JSON : **liste à relire, sans
    arrêt**, à remettre à qui contre-lit l'enchaînement. Le programme de l'aire conditionnelle et les chemins
    cloisonnés n'y sont pas."""
    signales: list[str] = []
    for f, chemin in _lire_les_dossiers(racine, dossiers, cloisonnes_de_plus, ".py")[0]:
        if f.suffix != ".py" or chemin in AUTORISES_POUR_LES_RANGS:
            continue
        try:
            signales += listages_d_un_programme(f.read_text(encoding="utf-8"), chemin)
        except UnicodeDecodeError:
            continue
    return signales
