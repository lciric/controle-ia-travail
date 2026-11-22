"""Preuve de la différence entre la garde statique version 13 et version 14 du bras A (cloisonnement).

Compare `src/controle_ia/organismes_discrets/cloisonnement_bras_a_v13.py` et `..._v14.py` :
1. par l'arbre syntaxique, docstring du module retirée : toute instruction de haut niveau est identique, sauf les deux
   affectations déclarées `PROGRAMMES_DE_L_AIRE_CONDITIONNELLE` et `GARDES_STATIQUES` ;
2. ces deux listes, évaluées : la version 14 est la version 13, dans le même ordre, plus **un seul** chemin chacune —
   `aire_conditionnelle_bras_a_v1.py` pour la première, `cloisonnement_bras_a_v14.py` pour la seconde (différence
   nécessaire : sans elle, la garde version 14 se refuserait elle-même, puisqu'elle écrit les noms réservés) ;
3. la docstring du module, ligne à ligne (difflib) : toute ligne changée tombe dans les lignes d'en-tête déclarées
   nommément — ligne 1 (titre, numéro de version) et lignes 6 à 10 de la version 14 (paragraphe « Ce qui change à la
   version 14 », remplaçant les lignes 6 et 7 de la version 13 qui ouvraient celui de la version 13).
Sort sur le code 1 et dit pourquoi à la première différence hors de ce périmètre ; sinon imprime la différence et
« PREUVE TENUE ». Ne lit que ces deux fichiers (ou, pour l'éprouver sur un artefact, les deux chemins donnés en
arguments : version 13, puis version 14).
"""
from __future__ import annotations

import ast
import difflib
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parents[3]
PAQUET = "src/controle_ia/organismes_discrets/"
V13, V14 = RACINE / PAQUET / "cloisonnement_bras_a_v13.py", RACINE / PAQUET / "cloisonnement_bras_a_v14.py"
LISTES_DECLAREES = {"PROGRAMMES_DE_L_AIRE_CONDITIONNELLE": PAQUET + "aire_conditionnelle_bras_a_v1.py",
                    "GARDES_STATIQUES": PAQUET + "cloisonnement_bras_a_v14.py"}
LIGNES_D_EN_TETE_V14 = {1, 6, 7, 8, 9, 10}      # numéros de ligne (fichier version 14), docstring du module
LIGNES_D_EN_TETE_V13 = {1, 6, 7}                # leurs correspondantes dans la version 13


def echec(motif: str) -> None:
    print(f"PREUVE EN ÉCHEC : {motif}")
    sys.exit(1)


def corps_sans_docstring(arbre: ast.Module) -> list[ast.stmt]:
    corps = list(arbre.body)
    if corps and isinstance(corps[0], ast.Expr) and isinstance(corps[0].value, ast.Constant) \
            and isinstance(corps[0].value.value, str):
        corps = corps[1:]
    return corps


def nom_affecte(n: ast.stmt) -> str | None:
    if isinstance(n, ast.Assign) and len(n.targets) == 1 and isinstance(n.targets[0], ast.Name):
        return n.targets[0].id
    return None


def valeur(n: ast.Assign):
    return eval(compile(ast.Expression(n.value), "<liste>", "eval"), {"PAQUET": PAQUET, "tuple": tuple})  # noqa: S307


def main(argv: list[str]) -> int:
    v13, v14 = (Path(argv[0]), Path(argv[1])) if len(argv) == 2 else (V13, V14)
    t13, t14 = v13.read_text(encoding="utf-8"), v14.read_text(encoding="utf-8")
    a13, a14 = ast.parse(t13), ast.parse(t14)
    c13, c14 = corps_sans_docstring(a13), corps_sans_docstring(a14)
    if len(c13) != len(c14):
        echec(f"nombre d'instructions de haut niveau différent ({len(c13)} contre {len(c14)})")
    vues = set()
    for i, (x, y) in enumerate(zip(c13, c14)):
        if ast.dump(x) == ast.dump(y):
            continue
        nom = nom_affecte(x)
        if nom is None or nom != nom_affecte(y) or nom not in LISTES_DECLAREES:
            echec(f"instruction {i} (ligne {y.lineno} de la version 14) différente, hors des listes déclarées")
        l13, l14 = valeur(x), valeur(y)
        if tuple(l14) != tuple(l13) + (LISTES_DECLAREES[nom],):
            echec(f"{nom} : la version 14 n'est pas la version 13 plus le seul chemin {LISTES_DECLAREES[nom]}")
        vues.add(nom)
        print(f"{nom} : version 13 + {LISTES_DECLAREES[nom]!r} ({len(l13)} → {len(l14)} chemins)")
    if vues != set(LISTES_DECLAREES):
        echec(f"listes déclarées non changées : {sorted(set(LISTES_DECLAREES) - vues)}")
    d13, d14 = ast.get_docstring(a13, clean=False).splitlines(), ast.get_docstring(a14, clean=False).splitlines()
    for op, i1, i2, j1, j2 in difflib.SequenceMatcher(a=d13, b=d14, autojunk=False).get_opcodes():
        if op == "equal":
            continue
        hors = [k + 1 for k in range(j1, j2) if k + 1 not in LIGNES_D_EN_TETE_V14] \
            + [k + 1 for k in range(i1, i2) if k + 1 not in LIGNES_D_EN_TETE_V13]
        if hors:
            echec(f"docstring : ligne(s) changée(s) hors de l'en-tête déclaré ({op}, lignes {hors})")
    print("".join(difflib.unified_diff(t13.splitlines(True), t14.splitlines(True), "cloisonnement_bras_a_v13.py",
                                       "cloisonnement_bras_a_v14.py", n=0)), end="")
    print("PREUVE TENUE : seules différences — en-tête déclaré (lignes 1, 6 à 10 de la version 14) et un chemin ajouté à "
          "chacune des deux listes déclarées")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
