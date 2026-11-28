import ast, json, sys
from pathlib import Path

src = Path(sys.argv[1]).read_text(encoding="utf-8")
vues = {tuple(x) for x in json.load(open(sys.argv[2]))}
arbre = ast.parse(src)
lignes = src.splitlines()

# qualname et première ligne (celle du `def`, ou du premier décorateur : co_firstlineno) de chaque fonction
fonctions = []
def visite(n, prefixe=""):
    for e in ast.iter_child_nodes(n):
        if isinstance(e, (ast.FunctionDef, ast.AsyncFunctionDef)):
            q = prefixe + e.name
            premiere = min([e.lineno] + [d.lineno for d in e.decorator_list])
            fonctions.append((q, premiere, e))
            visite(e, q + ".<locals>.")
        elif isinstance(e, ast.ClassDef):
            visite(e, prefixe + e.name + ".")
visite(arbre)
non_vues = []
for q, premiere, e in fonctions:
    for n in ast.walk(e):
        if isinstance(n, ast.Raise):
            if (q, n.lineno - premiere) not in vues:
                non_vues.append((n.lineno, q, lignes[n.lineno - 1].strip()[:110]))
for x in sorted(set(non_vues)):
    print(f"{x[0]:5d}  {x[1]:32s} {x[2]}")
# fonctions jamais appelées
print("fonctions jamais appelées :", [q for q, p, e in fonctions if not any(v[0] == q for v in vues)])
