#!/usr/bin/env python3
"""Relecture de la v3 du script de lecture du pilote 4 : comparaison des fonctions et constantes de la v2 et de la v3,
par leurs arbres syntaxiques sans les chaînes de documentation (aucun code des scripts n'est exécuté).

Usage : python -I comparer_fonctions_v2_v3.py SCRIPT_V2 SCRIPT_V3
"""
import ast
import difflib
import sys


def sans_doc(noeud):
    """Copie de l'arbre d'une fonction, chaînes de documentation retirées (fonction et fonctions imbriquées)."""
    n = ast.parse(ast.unparse(noeud))
    for x in ast.walk(n):
        if isinstance(x, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)) and x.body:
            premier = x.body[0]
            if isinstance(premier, ast.Expr) and isinstance(getattr(premier, "value", None), ast.Constant) \
                    and isinstance(premier.value.value, str):
                x.body = x.body[1:] or [ast.Pass()]
    return n


def elements(chemin):
    arbre = ast.parse(open(chemin, encoding="utf-8").read())
    fonctions, constantes = {}, {}
    for x in arbre.body:
        if isinstance(x, ast.FunctionDef):
            fonctions[x.name] = x
        elif isinstance(x, ast.Assign) and len(x.targets) == 1 and isinstance(x.targets[0], ast.Name):
            constantes[x.targets[0].id] = x.value
    return fonctions, constantes


def principal():
    f2, c2 = elements(sys.argv[1])
    f3, c3 = elements(sys.argv[2])
    print("# fonctions présentes dans les deux versions")
    for nom in sorted(set(f2) & set(f3)):
        a, b = ast.dump(sans_doc(f2[nom])), ast.dump(sans_doc(f3[nom]))
        print(f"{nom:32s} {'identique' if a == b else 'DIFFÉRENTE'}")
    print("# fonctions de la v2 seule :", ", ".join(sorted(set(f2) - set(f3))) or "aucune")
    print("# fonctions de la v3 seule :", ", ".join(sorted(set(f3) - set(f2))) or "aucune")
    print("# constantes présentes dans les deux versions")
    for nom in sorted(set(c2) & set(c3)):
        a, b = ast.dump(c2[nom]), ast.dump(c3[nom])
        print(f"{nom:32s} {'identique' if a == b else 'DIFFÉRENTE'}")
    print("# constantes de la v2 seule :", ", ".join(sorted(set(c2) - set(c3))) or "aucune")
    print("# constantes de la v3 seule :", ", ".join(sorted(set(c3) - set(c2))) or "aucune")
    for nom in sorted(set(f2) & set(f3)):
        a, b = ast.unparse(sans_doc(f2[nom])), ast.unparse(sans_doc(f3[nom]))
        if a != b:
            print(f"===== {nom}")
            for ligne in difflib.unified_diff(a.splitlines(), b.splitlines(), lineterm="", n=1):
                if not ligne.startswith(("---", "+++")):
                    print(ligne)


if __name__ == "__main__":
    principal()
