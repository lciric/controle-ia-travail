"""Comparaison indépendante (vérificateur neuf) : table « Critères de lecture gelés » du texte contre `LIGNES` du module.

Aucun import du module : `LIGNES` est extraite du source par l'arbre syntaxique (`ast.literal_eval`), sans rien exécuter.
Le texte est découpé caractère par caractère (barre échappée « \\| » gardée comme « | »), sans expression régulière et
sans `controle_ia.prereg.sections`. Sortie : un JSON sur la sortie standard.

Usage : python -I -B comparer_table_independant_v1.py <texte.md> <lecture_p4_v1.py> [<lecture_p4_v1.py> ...]
"""
import ast
import json
import sys
import unicodedata
from pathlib import Path


def cellules(ligne: str) -> list[str]:
    s = ligne.strip()
    assert s.startswith("|") and s.endswith("|"), ligne[:60]
    s = s[1:-1]
    out, cur, i = [], [], 0
    while i < len(s):
        if s[i] == "\\" and i + 1 < len(s) and s[i + 1] == "|":
            cur.append("|")
            i += 2
            continue
        if s[i] == "|":
            out.append("".join(cur).strip())
            cur = []
        else:
            cur.append(s[i])
        i += 1
    out.append("".join(cur).strip())
    return out


def table_du_texte(texte: str):
    lignes = texte.split("\n")
    titres = [i for i, x in enumerate(lignes) if x.rstrip() == "## Critères de lecture gelés"]
    assert len(titres) == 1, titres
    debut = titres[0] + 1
    fin = next((i for i in range(debut, len(lignes)) if lignes[i].startswith("## ")), len(lignes))
    rangees = [x for x in lignes[debut:fin] if x.lstrip().startswith("|")]
    entete, separateur, corps = rangees[0], rangees[1], rangees[2:]
    autres_avec_barre = [x for x in lignes[debut:fin] if "|" in x and not x.lstrip().startswith("|")]
    table = []
    for x in corps:
        c = cellules(x)
        table.append(c)
    return {"entete": cellules(entete), "separateur": separateur.strip(), "rangees": table,
            "lignes_avec_barre_hors_rangee": autres_avec_barre, "ligne_du_titre": titres[0] + 1,
            "lignes_du_texte": [debut + 1, fin]}


def lignes_du_source(chemin: Path) -> dict:
    arbre = ast.parse(chemin.read_text(encoding="utf-8"))
    for n in arbre.body:
        if isinstance(n, ast.Assign) and any(isinstance(t, ast.Name) and t.id == "LIGNES" for t in n.targets):
            return ast.literal_eval(n.value)
    raise SystemExit(f"LIGNES absente de {chemin}")


def inventaire_caracteres(s: str) -> list:
    return sorted({f"U+{ord(ch):04X} {unicodedata.name(ch, '?')}" for ch in s if ord(ch) > 127})


def main(argv):
    texte = Path(argv[0]).read_text(encoding="utf-8")
    t = table_du_texte(texte)
    rapport = {"texte": argv[0], "entete": t["entete"], "ligne_du_titre": t["ligne_du_titre"],
               "lignes_avec_barre_hors_rangee": t["lignes_avec_barre_hors_rangee"],
               "nombre_de_rangees": len(t["rangees"]), "rangees_a_trois_cellules": all(len(r) == 3 for r in t["rangees"]),
               "cles_du_texte": [r[0] for r in t["rangees"]],
               "caracteres_non_ascii_de_la_table": inventaire_caracteres("".join("".join(r) for r in t["rangees"])),
               "modules": {}}
    for chemin in argv[1:]:
        L = lignes_du_source(Path(chemin))
        cmp = []
        for r in t["rangees"]:
            k = r[0]
            if k not in L:
                cmp.append({"ligne": k, "etat": "absente du module"})
                continue
            for j, nom in ((1, "issue"), (2, "lecture")):
                eg = r[j] == L[k][j - 1]
                cmp.append({"ligne": k, "cellule": nom, "egale": eg, **({} if eg else {"texte": r[j], "module": L[k][j - 1]})})
        rapport["modules"][chemin] = {
            "cles_du_module": list(L), "meme_ordre": [r[0] for r in t["rangees"]] == list(L),
            "cellules_egales": sum(1 for c in cmp if c.get("egale")),
            "cellules_differentes": [(c["ligne"], c.get("cellule"), c.get("etat")) for c in cmp if not c.get("egale")],
            "detail_des_differences": [c for c in cmp if not c.get("egale")]}
    print(json.dumps(rapport, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main(sys.argv[1:])
