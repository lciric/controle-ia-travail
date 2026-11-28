"""Differentiel par l'arbre syntaxique (sans rien executer) entre deux versions d'un fichier Python :
definitions de haut niveau (fonctions, classes, affectations) ajoutees, retirees, changees ; ordre."""
import ast
import json
import sys
from pathlib import Path


def defs(chemin):
    arbre = ast.parse(Path(chemin).read_text(encoding="utf-8"))
    sortie, ordre = {}, []
    for n in arbre.body:
        if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            nom = n.name
        elif isinstance(n, (ast.Assign, ast.AnnAssign)):
            cibles = n.targets if isinstance(n, ast.Assign) else [n.target]
            nom = "=" + ",".join(ast.unparse(c) for c in cibles)
        elif isinstance(n, (ast.Import, ast.ImportFrom)):
            nom = "import:" + ast.unparse(n)
        elif isinstance(n, ast.Expr) and isinstance(getattr(n, "value", None), ast.Constant) and isinstance(n.value.value, str):
            nom = "docstring-module"
        else:
            nom = "stmt:" + ast.unparse(n)[:80]
        k, base = 1, nom
        while nom in sortie:
            k += 1
            nom = f"{base}#{k}"
        sortie[nom] = ast.dump(n, include_attributes=False)
        ordre.append(nom)
    return sortie, ordre


def sans_docstring(dump_src):
    return dump_src


def code_sans_docstrings(chemin):
    arbre = ast.parse(Path(chemin).read_text(encoding="utf-8"))
    for n in ast.walk(arbre):
        if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef, ast.Module)):
            b = n.body
            if b and isinstance(b[0], ast.Expr) and isinstance(getattr(b[0], "value", None), ast.Constant) \
                    and isinstance(b[0].value.value, str):
                n.body = b[1:] or [ast.Pass()]
    return arbre


def defs_code(chemin):
    arbre = code_sans_docstrings(chemin)
    sortie = {}
    for n in arbre.body:
        if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            sortie[n.name] = ast.dump(n, include_attributes=False)
    return sortie


a, b = sys.argv[1], sys.argv[2]
da, oa = defs(a)
db, ob = defs(b)
ca, cb = defs_code(a), defs_code(b)
res = {
    "ancien": a, "nouveau": b,
    "retirees": [k for k in oa if k not in db],
    "ajoutees": [k for k in ob if k not in da],
    "changees": [k for k in oa if k in db and da[k] != db[k]],
    "changees_code_hors_docstrings": [k for k in ca if k in cb and ca[k] != cb[k]],
    "changees_docstring_seule": [k for k in ca if k in cb and ca[k] == cb[k] and da.get(k) != db.get(k)],
    "ordre_commun_garde": [k for k in oa if k in db] == [k for k in ob if k in da],
}
print(json.dumps(res, ensure_ascii=False, indent=1))
