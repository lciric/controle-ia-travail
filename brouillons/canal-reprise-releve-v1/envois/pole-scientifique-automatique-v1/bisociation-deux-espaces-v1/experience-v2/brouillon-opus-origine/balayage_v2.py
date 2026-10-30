"""Balayage statique (liste d'arrêt ; audit (i)) du code des bras et des noyaux.

Refuse : (1) toute instruction `try` munie d'un `except` (spécifique ou générique) — plus strict que la liste d'arrêt,
qui vise un `except` autour de `cholesky`, `glouton_paires` ou de la copie gardée : un `except` ailleurs dans le code
des bras est refusé aussi ; (2) toute mention d'un champ ou objet latent (`latent`, `Latent`, `JETON_MESURE`,
`vrais`, `plante`, `plantes`, `rares`, `info_paires`, `champ`, `arts`, `provenance`) comme nom ou attribut ;
(3) tout import de `monde_v2` ou de `mesures_v2`.
"""
import ast
from pathlib import Path

from controle_ia.gardes import GardeArret

INTERDITS = {"latent", "Latent", "_latent", "JETON_MESURE", "vrais", "plante", "plantes", "rares", "info_paires",
             "champ", "arts", "provenance", "verite"}
MODULES_INTERDITS = {"monde_v2", "mesures_v2"}
APPELS_GARDES = {"cholesky", "glouton_paires", "ordre_glouton_garde"}


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
