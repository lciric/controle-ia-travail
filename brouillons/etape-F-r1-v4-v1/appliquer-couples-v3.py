"""Applique dans l'ordre des couples (ancien → nouveau) à un texte : chaque « ancien » doit apparaître **exactement une
fois** dans le texte au moment de son application (sauf un compte `occurrences` déclaré par le couple, alors exactement
ce compte, toutes remplacées) ; sinon arrêt sans rien écrire. Même méthode que `appliquer-couples-v2.py` ; en plus :
- le fichier de couples peut être une **liste nue** de {ancien, nouveau} (forme de la contre-lecture 2) ; les
  identifiants sont alors K-1, K-2, … ; la forme v2 ({couples: [...], blocs: [...]}) reste acceptée ;
- le journal porte les empreintes sha256 des entrées (texte, couples), pour chaque couple la ligne (1-indexée) où
  commence l'« ancien » au moment de son application et le nombre d'occurrences remplacées, l'empreinte sha256 de la
  sortie et le compte des marqueurs de gabarit (motif `<<[A-Z0-9_]+>>`) dans la sortie.
Lancement :
    python3 -I brouillons/etape-F-r1-v4-v1/appliquer-couples-v3.py <entree.md> <couples.json> <sortie.md> <journal.md>
Rien d'existant n'est écrasé (R12).
"""
import hashlib
import json
import re
import sys
from collections import Counter
from pathlib import Path

MARQUEUR = re.compile(r"<<[A-Z0-9_]+>>")


def sha256_fichier(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def normaliser(spec) -> dict:
    if isinstance(spec, list):
        return {"couples": [{"id": f"K-{i}", "motif": "contre-lecture 2", **c} for i, c in enumerate(spec, 1)]}
    return spec


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
        ligne = texte[: texte.index(c["ancien"])].count("\n") + 1
        texte = texte.replace(c["ancien"], c["nouveau"])
        journal.append(f"- {c['id']} : {n} occurrence(s) remplacée(s), ligne {ligne} de l'entrée au moment de "
                       f"l'application — {c['motif']}")
    return texte, journal


def main(argv):
    entree, couples, sortie, journal = (Path(a) for a in argv)
    spec = normaliser(json.loads(couples.read_text(encoding="utf-8")))
    for p in (sortie, journal):
        if p.exists():
            raise SystemExit(f"{p} existe déjà (R12)")
    texte, lignes = appliquer(entree.read_text(encoding="utf-8"), spec, Path("."))
    sortie.write_text(texte, encoding="utf-8")
    marqueurs = Counter(MARQUEUR.findall(texte))
    lignes_marqueurs = [f"- `{m}` : {k} fois" for m, k in sorted(marqueurs.items())] or ["- aucun"]
    journal.write_text("\n".join([
        f"# Journal — couples `{couples}` appliqués à `{entree}` → `{sortie}`", "",
        "## Entrées (sha256)", "",
        f"- `{entree}` : `{sha256_fichier(entree)}`",
        f"- `{couples}` : `{sha256_fichier(couples)}`", "",
        "## Opérations, dans l'ordre", "", *lignes, "",
        "## Sortie", "",
        f"- `{sortie}` : `{sha256_fichier(sortie)}`",
        f"- marqueurs de gabarit (motif `<<[A-Z0-9_]+>>`) : {sum(marqueurs.values())} occurrence(s), "
        f"{len(marqueurs)} marqueur(s) distinct(s)",
        *lignes_marqueurs, "",
    ]), encoding="utf-8")
    print(f"{len(lignes)} opérations ; {sortie} ; marqueurs : {dict(marqueurs)}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
