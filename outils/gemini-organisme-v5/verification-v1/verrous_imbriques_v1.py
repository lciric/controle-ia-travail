"""Liste, dans un principal.py, les appels faits en tenant _VERROU à une fonction du module qui le reprend.
Usage : python -I verrous_imbriques_v1.py FICHIER"""
import ast, sys
arbre = ast.parse(open(sys.argv[1], encoding="utf-8").read())
def blocs(f):
    return [n for n in ast.walk(f) if isinstance(n, ast.With)
            and any(isinstance(i.context_expr, ast.Name) and i.context_expr.id == "_VERROU" for i in n.items)]
fonctions = [f for f in ast.walk(arbre) if isinstance(f, ast.FunctionDef)]
prennent = {f.name for f in fonctions if blocs(f)}
trouves = 0
for f in fonctions:
    for b in blocs(f):
        for c in ast.walk(b):
            if isinstance(c, ast.Call) and isinstance(c.func, ast.Name) and c.func.id in prennent:
                trouves += 1
                print(f"BLOCAGE : {f.name} (ligne {b.lineno}) appelle {c.func.id} (ligne {c.lineno}) en tenant _VERROU")
print(f"{trouves} appel(s) imbriqué(s) ; fonctions qui prennent _VERROU : {sorted(prennent)}")
