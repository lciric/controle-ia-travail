"""Différentiel par l'arbre syntaxique, module v1 → module v2 (vérificateur neuf ; rien n'est exécuté).

Pour chaque fichier Python : nœuds de premier niveau (fonctions, classes, affectations, imports) ajoutés, retirés,
changés ; docstring du module changée ou non ; pour les fichiers de tests, noms des tests (fonctions `test_*`) et
paramétrages. Sortie : JSON sur la sortie standard.

Usage : python -I -B differentiel_ast_v1.py <dossier v1> <dossier v2>
"""
import ast
import json
import sys
from pathlib import Path

FICHIERS = ("mesures_conception_p4_v1.py", "instrument_p4_v1.py", "lecture_p4_v1.py", "test_instrument_p4_v1.py",
            "test_lecture_p4_v1.py", "test_gardes_p4_v1.py")


def cle(n, i):
    if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
        return f"def {n.name}"
    if isinstance(n, ast.Assign):
        return "= " + ",".join(ast.unparse(t) for t in n.targets)
    if isinstance(n, ast.AnnAssign):
        return "= " + ast.unparse(n.target)
    if isinstance(n, (ast.Import, ast.ImportFrom)):
        return "import " + ast.unparse(n)
    if isinstance(n, ast.Expr) and isinstance(getattr(n, "value", None), ast.Constant) and i == 0:
        return "docstring"
    return f"autre {type(n).__name__} {ast.unparse(n)[:60]}"


def noeuds(chemin):
    a = ast.parse(Path(chemin).read_text(encoding="utf-8"))
    out = {}
    for i, n in enumerate(a.body):
        k = cle(n, i)
        while k in out:
            k += "'"
        out[k] = ast.dump(n, include_attributes=False)
    return out


def sans_docstring(dump_src):
    return dump_src


def corps_sans_docstring(chemin, nom):
    a = ast.parse(Path(chemin).read_text(encoding="utf-8"))
    for n in a.body:
        if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef)) and n.name == nom:
            corps = n.body[1:] if (n.body and isinstance(n.body[0], ast.Expr)
                                   and isinstance(n.body[0].value, ast.Constant)) else n.body
            return ast.dump(ast.Module(body=corps, type_ignores=[])) + ast.dump(n.args) + "".join(
                ast.dump(d) for d in n.decorator_list)
    return None


def main(d1, d2):
    rapport = {}
    for f in FICHIERS:
        a, b = noeuds(Path(d1) / f), noeuds(Path(d2) / f)
        changes = [k for k in a if k in b and a[k] != b[k]]
        changes_hors_docstring = [k for k in changes if k.startswith("def ")
                                  and corps_sans_docstring(Path(d1) / f, k[4:]) != corps_sans_docstring(Path(d2) / f, k[4:])]
        r = {"ajoutes": [k for k in b if k not in a], "retires": [k for k in a if k not in b], "changes": changes,
             "fonctions_changees_hors_docstring": changes_hors_docstring,
             "ordre_des_noeuds_communs_garde": [k for k in a if k in b] == [k for k in b if k in a]}
        if f.startswith("test_"):
            ta = [k[4:] for k in a if k.startswith("def test_")]
            tb = [k[4:] for k in b if k.startswith("def test_")]
            r["tests_v1"] = len(ta)
            r["tests_v2"] = len(tb)
            r["tests_v1_absents_du_v2"] = [t for t in ta if t not in tb]
            r["tests_v1_changes_dans_v2"] = [t for t in ta if t in tb and a["def " + t] != b["def " + t]]
            r["tests_neufs"] = [t for t in tb if t not in ta]
        rapport[f] = r
    print(json.dumps(rapport, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main(*sys.argv[1:3])
