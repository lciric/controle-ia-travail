"""Balayage statique (liste d'arrêt ; audit (i)) du code des bras et des noyaux.

Refuse : (1) toute instruction `try` munie d'un `except` (spécifique ou générique) — plus strict que la liste d'arrêt,
qui vise un `except` autour de `cholesky`, `glouton_paires` ou de la copie gardée : un `except` ailleurs dans le code
des bras est refusé aussi ; (2) toute mention d'un champ ou objet latent (`latent`, `Latent`, `JETON_MESURE`,
`vrais`, `plante`, `plantes`, `rares`, `info_paires`, `champ`, `arts`, `provenance`) comme nom ou attribut ;
(3) tout import de `monde_v2` ou de `mesures_v2` ; (4) tout accès dynamique qui contournerait (2) : appel de
`getattr`, `setattr`, `vars`, `eval`, `exec`, `globals`, `locals`, `__import__`, attribut `__dict__`, ou chaîne de
caractères égale à un nom interdit ; (5) (CLA-09) toute chaîne de caractères commençant par un préfixe d'étiquette
(`co:` ou `op:`, morceaux de f-chaîne compris) et tout appel de méthode `startswith`, `endswith`, `removeprefix`,
`removesuffix`, `partition`, `rpartition`, `split`, `rsplit` : un bras ne lit le nom d'une étiquette que comme une clé
opaque (égalité, appartenance, df), jamais par son préfixe (`co:R…` rare, `co:F…` fond, `op:h…` moyeu). Aucun bras
livré n'emploie ces chaînes ni ces méthodes (le préfixe est posé par monde_v2, hors balayage).
"""
import ast
from pathlib import Path

from controle_ia.gardes import GardeArret

INTERDITS = {"latent", "Latent", "_latent", "JETON_MESURE", "vrais", "plante", "plantes", "rares", "info_paires",
             "champ", "arts", "provenance", "verite"}
MODULES_INTERDITS = {"monde_v2", "mesures_v2"}
APPELS_DYNAMIQUES = {"getattr", "setattr", "vars", "eval", "exec", "globals", "locals", "__import__"}
APPELS_GARDES = {"cholesky", "glouton_paires", "ordre_glouton_garde"}
PREFIXES_ETIQUETTES = ("co:", "op:")
METHODES_DE_PREFIXE = {"startswith", "endswith", "removeprefix", "removesuffix", "partition", "rpartition", "split",
                       "rsplit"}


def problemes(source, nom="<module>"):
    arbre = ast.parse(source, filename=nom)
    out = []
    for n in ast.walk(arbre):
        if isinstance(n, ast.Try) and n.handlers:
            appels = {getattr(c.func, "id", getattr(c.func, "attr", None))
                      for t in n.body for c in ast.walk(t) if isinstance(c, ast.Call)}
            cible = sorted(appels & APPELS_GARDES)
            out.append(f"{nom}:{n.lineno} : except interdit" + (f" autour de {cible}" if cible else ""))
        if isinstance(n, ast.Name) and n.id in INTERDITS:
            out.append(f"{nom}:{n.lineno} : nom latent « {n.id} »")
        if isinstance(n, ast.Attribute) and n.attr in INTERDITS:
            out.append(f"{nom}:{n.lineno} : attribut latent « {n.attr} »")
        if isinstance(n, ast.Call) and isinstance(n.func, ast.Name) and n.func.id in APPELS_DYNAMIQUES:
            out.append(f"{nom}:{n.lineno} : accès dynamique « {n.func.id} »")
        if isinstance(n, ast.Attribute) and n.attr == "__dict__":
            out.append(f"{nom}:{n.lineno} : attribut « __dict__ »")
        if isinstance(n, ast.Constant) and isinstance(n.value, str) and n.value in INTERDITS:
            out.append(f"{nom}:{n.lineno} : chaîne latente « {n.value} »")
        if isinstance(n, ast.Constant) and isinstance(n.value, str) and n.value.startswith(PREFIXES_ETIQUETTES):
            out.append(f"{nom}:{n.lineno} : préfixe d'étiquette « {n.value[:6]} »")
        if isinstance(n, ast.Call) and isinstance(n.func, ast.Attribute) and n.func.attr in METHODES_DE_PREFIXE:
            out.append(f"{nom}:{n.lineno} : lecture de préfixe « .{n.func.attr} »")
        if isinstance(n, ast.Import):
            out += [f"{nom}:{n.lineno} : import {a.name}" for a in n.names if a.name in MODULES_INTERDITS]
        if isinstance(n, ast.ImportFrom) and n.module in MODULES_INTERDITS:
            out.append(f"{nom}:{n.lineno} : import depuis {n.module}")
    return out


def exiger_propre(chemins):
    tous = []
    for c in chemins:
        tous += problemes(Path(c).read_text(encoding="utf-8"), str(Path(c).name))
    if tous:
        raise GardeArret("balayage statique : code refusé\n" + "\n".join(tous))
    return True


MODULES_BRAS = ("bras_v2.py", "noyaux_v2.py")
