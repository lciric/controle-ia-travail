"""Gardes du module (instructions `raise` de GardeArret, NonCalculable, DefautDuModule) jamais exécutées par la suite de
tests (lignes relevées par le greffon `trace_lignes`, processus pytest seulement : la ligne de commande lancée dans un
processus séparé n'est pas tracée)."""
import ast
import json
import sys
from pathlib import Path

module = Path(sys.argv[1])
lignes = set(json.loads(Path(sys.argv[2]).read_text()))
arbre = ast.parse(module.read_text(encoding="utf-8"))
source = module.read_text(encoding="utf-8").splitlines()


class Visiteur(ast.NodeVisitor):
    def __init__(self):
        self.pile, self.gardes = [], []

    def visit_FunctionDef(self, n):
        self.pile.append(n.name)
        self.generic_visit(n)
        self.pile.pop()

    visit_ClassDef = visit_FunctionDef

    def visit_Raise(self, n):
        exc = n.exc
        nom = None
        if isinstance(exc, ast.Call) and isinstance(exc.func, ast.Name):
            nom = exc.func.id
        if nom in ("GardeArret", "NonCalculable", "DefautDuModule"):
            self.gardes.append((n.lineno, nom, ".".join(self.pile) or "<module>"))


v = Visiteur()
v.visit(arbre)
print(f"lignes exécutées relevées : {len(lignes)} ; gardes : {len(v.gardes)}")
non = [(l, nom, f) for l, nom, f in v.gardes if l not in lignes]
print(f"gardes jamais exécutées par les tests : {len(non)}")
for l, nom, f in non:
    print(f"  l. {l:4d} {nom:15s} {f:32s} {source[l - 1].strip()[:110]}")
