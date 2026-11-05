"""Applique dans l'ordre des couples (ancien → nouveau) à un texte : chaque « ancien » doit apparaître **exactement une
fois** dans le texte au moment de son application (sauf un compte `occurrences` déclaré par le couple, alors exactement
ce compte, toutes remplacées) ; sinon arrêt sans rien écrire. Écrit le texte résultant et un journal (un couple par
ligne : identifiant, occurrences remplacées). Lancement :
    python brouillons/etape-F-r1-v4-v1/appliquer-couples-v2.py <entree.md> <couples.json> <sortie.md> <journal.md>
Le fichier de couples porte la clé `couples` (liste de {id, motif, ancien, nouveau[, occurrences]}) ; il peut aussi
porter `blocs` (liste de {id, motif, debut, fin, fichier}) : le texte de la ligne `debut` (incluse) à la ligne `fin`
(exclue), chacune unique, est remplacé par le contenu du `fichier` (chemin relatif à la racine de l'arbre), avant les
couples.
"""
import json
import sys
from pathlib import Path


def appliquer(texte: str, spec: dict, racine: Path) -> tuple[str, list[str]]:
    journal = []
    for b in spec.get("blocs", []):
        d, f = texte.count(b["debut"]), texte.count(b["fin"])
        if d != 1 or f != 1:
            raise SystemExit(f"bloc {b['id']} : début trouvé {d} fois, fin trouvée {f} fois (1 attendu)")
        i, j = texte.index(b["debut"]), texte.index(b["fin"])
        if j <= i:
            raise SystemExit(f"bloc {b['id']} : fin avant début")
        contenu = (racine / b["fichier"]).read_text(encoding="utf-8")
        texte = texte[:i] + contenu + texte[j:]
        journal.append(f"- {b['id']} : bloc remplacé par `{b['fichier']}` ({contenu.count(chr(10))} lignes) — {b['motif']}")
    for c in spec["couples"]:
        attendu = int(c.get("occurrences", 1))
        n = texte.count(c["ancien"])
        if n != attendu:
            raise SystemExit(f"couple {c['id']} : « ancien » trouvé {n} fois ({attendu} attendu) : {c['ancien'][:80]!r}")
        texte = texte.replace(c["ancien"], c["nouveau"])
        journal.append(f"- {c['id']} : {n} occurrence(s) remplacée(s) — {c['motif']}")
    return texte, journal


def main(argv):
    entree, couples, sortie, journal = (Path(a) for a in argv)
    spec = json.loads(couples.read_text(encoding="utf-8"))
    texte, lignes = appliquer(entree.read_text(encoding="utf-8"), spec, Path("."))
    for p in (sortie, journal):
        if p.exists():
            raise SystemExit(f"{p} existe déjà (R12)")
    sortie.write_text(texte, encoding="utf-8")
    journal.write_text("\n".join([f"# Journal — couples `{couples}` appliqués à `{entree}` → `{sortie}`", "", *lignes, ""]),
                       encoding="utf-8")
    print(f"{len(lignes)} opérations ; {sortie}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
