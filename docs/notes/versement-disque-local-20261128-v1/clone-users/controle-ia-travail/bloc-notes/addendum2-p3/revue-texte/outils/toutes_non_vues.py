import ast, json, sys
from pathlib import Path
src = Path(sys.argv[1]).read_text(encoding="utf-8")
vues = {tuple(x) for x in json.load(open(sys.argv[2]))}
lignes = src.splitlines()
arbre = ast.parse(src)
fonctions = []
def visite(n, prefixe=""):
    for e in ast.iter_child_nodes(n):
        if isinstance(e, (ast.FunctionDef, ast.AsyncFunctionDef)):
            q = prefixe + e.name
            premiere = min([e.lineno] + [d.lineno for d in e.decorator_list])
            fonctions.append((q, premiere, e)); visite(e, q + ".<locals>.")
        elif isinstance(e, ast.ClassDef):
            visite(e, prefixe + e.name + ".")
visite(arbre)
for q, premiere, e in fonctions:
    # lignes de début des instructions du corps (hors def imbriquées)
    debuts = set()
    for n in ast.walk(e):
        if isinstance(n, ast.stmt) and n is not e and not isinstance(n, (ast.FunctionDef,)):
            debuts.add(n.lineno)
    # exclure les lignes des fonctions imbriquées
    for n in ast.walk(e):
        if isinstance(n, ast.FunctionDef) and n is not e:
            for m in ast.walk(n):
                if isinstance(m, ast.stmt):
                    debuts.discard(m.lineno)
    manquent = sorted(l for l in debuts if (q, l - premiere) not in vues)
    if manquent:
        print(f"{q}: " + ", ".join(f"{l}: {lignes[l-1].strip()[:60]}" for l in manquent))
