"""Consigne d'alignement v2, § 2 point 5 et § 4 : modules de `src/controle_ia/` importés, directement ou non, par le
code de T0.8 (`src/controle_ia/t08/*.py`) et par la pièce « mots et coût » (`scripts/mots_et_cout_t06_v3.py`, y compris
ses imports dynamiques par nom : `importlib.import_module("controle_ia....")`), au commit aligné ; pour chacun, égal à
l'octet à l'arbre du commit de départ, ou différent. Quatre chemins doivent être égaux à l'octet, sinon code 1.

Fermeture calculée sur l'arbre syntaxique (import, from-import absolus et relatifs, chaînes littérales passées à
`importlib.import_module`), fichiers lus par `git show` au commit aligné ; un import placé dans une fonction compte
(surestimation prudente). Aucun fichier de travail lu, rien d'écrit.

Usage : python modules-importes-t08-v1.py DEPART ALIGNE
"""
from __future__ import annotations

import ast
import subprocess
import sys

DEPART, ALIGNE = sys.argv[1], sys.argv[2]
QUATRE = ("src/controle_ia/bases/", "src/controle_ia/t06/cout.py", "src/controle_ia/t06/test_croise.py",
          "src/controle_ia/environnements/propositions.py")


def git(*a) -> bytes:
    return subprocess.run(["git", *a], check=True, capture_output=True).stdout


def arbre(c: str) -> dict[str, str]:
    d = {}
    for l in git("ls-tree", "-r", c, "--", "src/controle_ia", "scripts/mots_et_cout_t06_v3.py").decode().splitlines():
        meta, chemin = l.split("\t", 1)
        d[chemin] = meta.split()[2]
    return d


A, B = arbre(DEPART), arbre(ALIGNE)


def chemin_de(module: str) -> str | None:
    base = "src/" + module.replace(".", "/")
    for c in (base + ".py", base + "/__init__.py"):
        if c in B:
            return c
    return None


def paquet_de(chemin: str) -> str:
    parts = chemin[len("src/"):-len(".py")].split("/")
    return ".".join(parts[:-1] if parts[-1] == "__init__" else parts[:-1])


def imports(chemin: str) -> set[str]:
    t = ast.parse(git("show", f"{ALIGNE}:{chemin}"))
    pkg = paquet_de(chemin) if chemin.startswith("src/") else ""
    sortie = set()
    for n in ast.walk(t):
        if isinstance(n, ast.Import):
            sortie |= {a.name for a in n.names}
        elif isinstance(n, ast.ImportFrom):
            if n.level:
                parts = pkg.split(".")
                base = ".".join(parts[:len(parts) - n.level + 1])
                mod = base + ("." + n.module if n.module else "")
            else:
                mod = n.module or ""
            sortie.add(mod)
            sortie |= {f"{mod}.{a.name}" for a in n.names}
        elif (isinstance(n, ast.Call) and getattr(n.func, "attr", None) == "import_module" and n.args
              and isinstance(n.args[0], ast.Constant) and isinstance(n.args[0].value, str)):
            sortie.add(n.args[0].value)
    sortie = {m for m in sortie if m == "controle_ia" or m.startswith("controle_ia.")}
    # paquets parents (leur __init__ s'exécute à l'import)
    for m in list(sortie):
        p = m.split(".")
        sortie |= {".".join(p[:i]) for i in range(1, len(p))}
    return sortie


depart = sorted(c for c in B if c.startswith("src/controle_ia/t08/") and c.endswith(".py"))
depart.append("scripts/mots_et_cout_t06_v3.py")
vus, pile = set(), list(depart)
while pile:
    c = pile.pop()
    if c in vus:
        continue
    vus.add(c)
    for m in imports(c):
        p = chemin_de(m)
        if p and p not in vus:
            pile.append(p)
echecs = []
print(f"modules de src/controle_ia/ importés (fermeture, {len(vus) - 1} fichiers hors de la pièce) :")
for c in sorted(vus):
    if c.startswith("scripts/"):
        continue
    etat = "égal à l'octet" if A.get(c) == B.get(c) else ("ABSENT au départ" if c not in A else "DIFFÉRENT")
    print(f"  {c} : {etat}")
for q in QUATRE:
    ca = {k: v for k, v in A.items() if k.startswith(q)} if q.endswith("/") else {q: A.get(q)}
    cb = {k: v for k, v in B.items() if k.startswith(q)} if q.endswith("/") else {q: B.get(q)}
    ok = ca == cb and all(v is not None for v in cb.values())
    if not ok:
        echecs.append(q)
    print(f"chemin exigé égal : {q} ({len(cb)} fichier(s)) : {'égal à l\'octet' if ok else 'DIFFÉRENT : NŒUD'}")
print("BILAN : " + ("quatre chemins égaux à l'octet" if not echecs else f"ARRÊT, nœud : {echecs}"))
sys.exit(1 if echecs else 0)
