"""Garde statique du cloisonnement du fichier des rangs par unité des moniteurs, bras A des organismes discrets,
version 5 du code (préenregistrement `prereg/T0.7-organismes-discrets-v-a-v2-brouillon20.md`, 3.5 (b) ; 8.4, « fichier
des scores par unité : cloisonnement » : « fichier ouvert par un autre programme : refusé »).

D'où il vient : contre-lecture du code de la version 4, défaut C-6. La seule garde était un essai, qui cherchait cinq
chaînes dans sept fichiers nommés et se contournait par un import indirect (`getattr` sur un nom coupé en deux, nom
de fichier recollé, `import *`, `__getattribute__`). La garde est maintenant **une fonction du code**, qui parcourt par
l'arbre syntaxique tous les programmes des dossiers qu'on lui donne (l'enchaînement de l'analyse lui donnera `src/` et
`scripts/`), et elle est éprouvée sur des modules plantés dans un dossier temporaire.

Ce qu'elle refuse, dans tout fichier qui n'est pas le programme de l'aire conditionnelle :
1. **le nom du fichier**, entier ou en morceaux : toute chaîne de texte — les morceaux recollés par `+`, par
   juxtaposition ou dans une chaîne à trous étant d'abord remis bout à bout — où se lit un fragment du nom
   (`rangs-par-`, `scores-par-`, `par-unite`, avec tiret ou soulignement) ;
2. **les trois noms réservés** du programme de l'aire conditionnelle (la fonction qui lit le fichier, l'objet qui porte
   les rangs, sa méthode de lecture), et ceux de la version 4 : comme nom, comme attribut, comme nom importé, ou
   écrits dans une chaîne de texte (ce qui couvre `getattr(module, "nom")`), morceaux recollés compris ;
3. dans un fichier qui **importe le module de l'analyse** (ou qui en écrit le nom dans une chaîne, hors de sa
   documentation) : `import *`, et
   tout accès indirect — `getattr`, `setattr`, `vars`, `dir`, `globals`, `locals`, `eval`, `exec`, `compile`,
   `__import__`, `import_module`, `__getattribute__`, `__dict__`, `attrgetter`, `methodcaller` ;
4. dans un fichier de commandes (`.sh`, `.bash`) : un fragment du nom du fichier.
Un fichier Python que l'analyseur ne lit pas est refusé lui aussi (il ne peut pas être dit propre).

**Limites, écrites.** (a) La première barrière du cloisonnement est une règle de procédure — « aucun agent n'ouvre le
fichier des scores par unité » (3.5 (b)) — ; cette garde ne la remplace pas : elle voit le code des dossiers qu'on lui
donne, non ce qu'un agent fait à la main ni un programme rangé ailleurs. (b) Elle ne voit pas un nom fabriqué à
l'exécution (lu d'un fichier, décodé, calculé) dans un fichier qui n'importe pas le module de l'analyse et n'ouvre le
fichier que par un chemin reçu en argument. (c) Python ne cache rien : l'objet qui porte les rangs reste lisible à qui
contourne tout cela exprès ; la garde arrête la mégarde et les détours simples. (d) Les essais du programme de l'aire
conditionnelle le touchent par nécessité ; `tests/` n'est pas dans les dossiers gardés. (e) Le côté habilité écrit ce
fichier : ses modules sont **exclus par leur chemin** (`EXCLUS_COTE_HABILITE`), et cette garde ne les lit pas.

Ce module ne lit que du code source ; il n'ouvre ni le fichier des rangs, ni aucun interne de moniteur.
"""
from __future__ import annotations

import ast
import re
from pathlib import Path
from typing import Iterable, Sequence

from ..gardes import GardeArret

# Le programme de l'aire conditionnelle, et ses versions antérieures (laissées telles quelles, R12), et cette garde.
PROGRAMMES_DE_L_AIRE_CONDITIONNELLE = ("analyse_bras_a_v5.py", "analyse_bras_a_v4.py", "analyse_bras_a_v3.py")
AUTORISES = PROGRAMMES_DE_L_AIRE_CONDITIONNELLE + ("cloisonnement_bras_a_v5.py",)
# Chemins du côté habilité, qui écrit le fichier : jamais lus par cette garde (fragments du chemin, écrits avec « / »).
EXCLUS_COTE_HABILITE = ("bras_a_v2_habilite/", "autres_moniteurs_v", "/bases/", "/sondes/", "/t07", "mots_et_cout_",
                        "__pycache__/")
FRAGMENT_DU_NOM_DU_FICHIER = re.compile(r"(?:rangs|scores)[-_]par[-_]|par[-_]unite", re.I)
NOMS_RESERVES = ("lire_fichier_des_rangs", "RangsScelles", "_pour_l_aire_conditionnelle",
                 "lire_fichier_des_scores", "ScoresScelles")
MODULE_DE_L_ANALYSE = re.compile(r"analyse_bras_a_v\d+")
ACCES_INDIRECTS = ("getattr", "setattr", "vars", "dir", "globals", "locals", "eval", "exec", "compile", "__import__",
                   "import_module", "__getattribute__", "__dict__", "attrgetter", "methodcaller")
SUFFIXES_DE_COMMANDES = (".sh", ".bash")


def _chaines(arbre: ast.AST) -> list[tuple[int, str]]:
    """Toutes les chaînes de texte d'un arbre, avec leur ligne ; les morceaux recollés par `+` ou dans une chaîne à
    trous sont remis bout à bout (les trous comptant pour rien), en plus d'être rendus un à un."""
    sortie: list[tuple[int, str]] = []

    def bout_a_bout(n: ast.AST) -> str | None:
        if isinstance(n, ast.Constant) and isinstance(n.value, str):
            return n.value
        if isinstance(n, ast.Constant) and isinstance(n.value, bytes):
            return n.value.decode("utf-8", "replace")
        if isinstance(n, ast.BinOp) and isinstance(n.op, ast.Add):
            return (bout_a_bout(n.left) or "") + (bout_a_bout(n.right) or "")
        if isinstance(n, ast.JoinedStr):
            return "".join(bout_a_bout(v) or "" for v in n.values)
        if isinstance(n, ast.FormattedValue):
            return bout_a_bout(n.value) or ""
        return None

    for n in ast.walk(arbre):
        t = bout_a_bout(n)
        if t:
            sortie.append((getattr(n, "lineno", 0), t))
    return sortie


def violations_d_un_programme(source: str, nom: str) -> list[str]:
    """Violations du cloisonnement dans le texte d'un programme Python (règles 1 à 3 de l'en-tête)."""
    try:
        arbre = ast.parse(source)
    except SyntaxError as e:
        return [f"{nom} : programme illisible par l'analyseur (ligne {e.lineno}) — il ne peut pas être dit propre"]
    trouve: list[str] = []
    chaines = _chaines(arbre)
    for ligne, t in chaines:
        if FRAGMENT_DU_NOM_DU_FICHIER.search(t):
            trouve.append(f"{nom}, ligne {ligne} : fragment du nom du fichier des rangs par unité dans une chaîne")
        for r in NOMS_RESERVES:
            if r in t:
                trouve.append(f"{nom}, ligne {ligne} : nom réservé `{r}` écrit dans une chaîne")
    # le nom du module de l'analyse écrit dans une chaîne (pour un import par son nom) vaut import ; une chaîne de
    # documentation, qui ne s'exécute pas, ne compte pas pour cette seule règle
    documentation = {id(n.body[0].value) for n in ast.walk(arbre)
                     if isinstance(n, (ast.Module, ast.ClassDef, ast.FunctionDef, ast.AsyncFunctionDef)) and n.body
                     and isinstance(n.body[0], ast.Expr) and isinstance(n.body[0].value, ast.Constant)
                     and isinstance(n.body[0].value.value, str)}
    importe = any(isinstance(n, ast.Constant) and isinstance(n.value, str) and id(n) not in documentation
                  and MODULE_DE_L_ANALYSE.search(n.value) for n in ast.walk(arbre))
    etoile: list[int] = []
    for n in ast.walk(arbre):
        noms: list[str] = []
        if isinstance(n, ast.Name):
            noms.append(n.id)
        elif isinstance(n, ast.Attribute):
            noms.append(n.attr)
        elif isinstance(n, (ast.Import, ast.ImportFrom)):
            module = getattr(n, "module", None) or ""
            for a in n.names:
                noms += [a.name, a.asname or ""]
                if MODULE_DE_L_ANALYSE.search(module) or MODULE_DE_L_ANALYSE.search(a.name):
                    importe = True
                    if a.name == "*":
                        etoile.append(n.lineno)
        elif isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            noms.append(n.name)
        elif isinstance(n, ast.arg):
            noms.append(n.arg)
        elif isinstance(n, ast.keyword) and n.arg:
            noms.append(n.arg)
        for x in noms:
            for r in NOMS_RESERVES:
                if r in x:
                    trouve.append(f"{nom}, ligne {getattr(n, 'lineno', 0)} : nom réservé `{r}`")
    if importe:
        for ligne in etoile:
            trouve.append(f"{nom}, ligne {ligne} : `import *` depuis le module de l'analyse")
        for n in ast.walk(arbre):
            x = n.id if isinstance(n, ast.Name) else n.attr if isinstance(n, ast.Attribute) else None
            if x in ACCES_INDIRECTS:
                trouve.append(f"{nom}, ligne {n.lineno} : accès indirect `{x}` dans un programme qui importe le module "
                              "de l'analyse")
            if isinstance(n, (ast.Import, ast.ImportFrom)):
                for a in n.names:
                    if a.name in ACCES_INDIRECTS:
                        trouve.append(f"{nom}, ligne {n.lineno} : accès indirect `{a.name}` importé dans un programme "
                                      "qui importe le module de l'analyse")
    return trouve


def violations_du_cloisonnement(racines: Iterable, *, autorises: Sequence[str] = AUTORISES,
                                exclus: Sequence[str] = EXCLUS_COTE_HABILITE) -> list[str]:
    """Parcourt les dossiers (ou fichiers) donnés et rend les violations du cloisonnement. `autorises` : noms de
    fichier du programme de l'aire conditionnelle (et de cette garde) ; `exclus` : fragments de chemin du côté
    habilité, jamais lus. Une racine absente est refusée (une garde qui ne lit rien ne dit rien)."""
    trouve: list[str] = []
    racines = [Path(r) for r in racines]
    if not racines:
        raise GardeArret("garde du cloisonnement : au moins un dossier à parcourir exigé")
    for racine in racines:
        if not racine.exists():
            raise GardeArret(f"garde du cloisonnement : {racine} absent — une garde qui ne lit rien ne dit rien")
        fichiers = [racine] if racine.is_file() else sorted(p for p in racine.rglob("*") if p.is_file())
        for f in fichiers:
            chemin = f.as_posix()
            if any(x in chemin + ("/" if f.is_dir() else "") for x in exclus) or f.name in autorises:
                continue
            if f.suffix == ".py":
                try:
                    source = f.read_text(encoding="utf-8")
                except UnicodeDecodeError:
                    trouve.append(f"{chemin} : programme illisible (encodage) — il ne peut pas être dit propre")
                    continue
                trouve += violations_d_un_programme(source, chemin)
            elif f.suffix in SUFFIXES_DE_COMMANDES:
                for k, ligne in enumerate(f.read_text(encoding="utf-8", errors="replace").splitlines(), 1):
                    if FRAGMENT_DU_NOM_DU_FICHIER.search(ligne):
                        trouve.append(f"{chemin}, ligne {k} : fragment du nom du fichier des rangs par unité dans un "
                                      "fichier de commandes")
    return trouve


def exiger_cloisonnement_statique(racines: Iterable, *, autorises: Sequence[str] = AUTORISES,
                                  exclus: Sequence[str] = EXCLUS_COTE_HABILITE) -> None:
    """Garde statique du cloisonnement (3.5 (b) ; 8.4) : arrêt si un programme autre que celui de l'aire conditionnelle
    nomme le fichier des rangs par unité, touche l'un des noms réservés, ou atteint le module de l'analyse par un
    détour. Limites écrites en tête du module."""
    trouve = violations_du_cloisonnement(racines, autorises=autorises, exclus=exclus)
    if trouve:
        raise GardeArret("cloisonnement du fichier des rangs par unité : seul le programme de l'aire conditionnelle le "
                         f"lit (3.5 (b) ; 8.4) — {len(trouve)} violation(s) : " + " | ".join(trouve[:8]))
