"""Contrôle mécanique du second addendum de B bis (brouillon) : processeur seulement, aucun réseau, aucune donnée.

Lit le texte scellé T, le premier addendum A1 et le brouillon du second addendum ; construit T+1 (EC-1 à EC-8 de A1 appliqués à
T, chaque « ancien » unique dans T) ; pour chaque SA, vérifie que l'« ancien » figure une seule fois dans son document (T, T+1 ou
A1 ; pour un fragment de T, aussi une seule fois dans T+1) ; applique les remplacements ; écrit le texte en vigueur (T+2) ;
vérifie que la phrase de R-PILE et le point (7) du texte en vigueur sont égaux aux chaînes de `lecture_v3` (gras retiré).

Jouer depuis la racine du dépôt : `PYTHONPATH=<dossier>/code/src:src python <ce fichier> <dossier du second addendum>`.
Code 0 : tout est conforme ; code 1 : un écart (motif écrit)."""
from __future__ import annotations

import re
import sys
from pathlib import Path

RACINE = Path.cwd()
T_CHEMIN = RACINE / "prereg/T0.7-etape-B-bis-v1.md"
A1_CHEMIN = RACINE / "prereg/T0.7-etape-B-bis-v1-addendum-ecart-v1.md"
BLOC = re.compile(r"Ancien :\n\n```text\n(.*?)\n```\n\nNouveau, qui fait foi :\n\n```text\n(.*?)\n```", re.S)


def blocs(texte: str, prefixe: str) -> list[tuple[str, str, str, str]]:
    """(identifiant, document, ancien, nouveau) pour chaque section « ### <prefixe>-k — … »."""
    sortie = []
    parts = re.split(rf"^### ({prefixe}-\d+) — (.*)$", texte, flags=re.M)
    for i in range(1, len(parts), 3):
        ident, titre, corps = parts[i], parts[i + 1], parts[i + 2]
        m = BLOC.search(corps)
        if not m:
            raise SystemExit(f"{ident} : blocs « Ancien » et « Nouveau » introuvables")
        d = re.search(r"\(document : (T\+1|T|A1)\b", titre)
        sortie.append((ident, d.group(1) if d else "T", m.group(1), m.group(2)))
    return sortie


def remplacer_unique(texte: str, ancien: str, nouveau: str, quoi: str) -> str:
    n = texte.count(ancien)
    if n != 1:
        raise SystemExit(f"{quoi} : « ancien » trouvé {n} fois (une seule attendue) : {ancien[:90]!r}")
    return texte.replace(ancien, nouveau)


def main() -> int:
    dossier = Path(sys.argv[1])
    T = T_CHEMIN.read_text(encoding="utf-8")
    A1 = A1_CHEMIN.read_text(encoding="utf-8")
    SA = (dossier / "brouillon-second-addendum-bbis-v2.md").read_text(encoding="utf-8")
    ec = blocs(A1, "EC")
    print(f"A1 : {len(ec)} écarts EC lus")
    T1 = T
    for ident, _, ancien, nouveau in ec:
        T1 = remplacer_unique(T1, ancien, nouveau, f"A1 {ident} dans T")
    sa = blocs(SA, "SA")
    print(f"second addendum : {len(sa)} écarts SA lus")
    T2, A1b = T1, A1
    for ident, doc, ancien, nouveau in sa:
        if doc == "A1":
            A1b = remplacer_unique(A1b, ancien, nouveau, f"{ident} dans A1")
        else:
            if doc == "T" and T.count(ancien) != 1:
                raise SystemExit(f"{ident} : « ancien » trouvé {T.count(ancien)} fois dans T (une seule attendue)")
            if doc == "T+1" and T.count(ancien) != 0 and ident not in ("SA-5",):
                raise SystemExit(f"{ident} : fragment de T+1 attendu (« nouveau » de A1), trouvé tel quel dans T")
            T2 = remplacer_unique(T2, ancien, nouveau, f"{ident} dans T+1")
        print(f"{ident} ({doc}) : ancien unique, remplacé ({len(ancien)} → {len(nouveau)} caractères)")
    for ident, doc, ancien, nouveau in sa:
        cible = A1b if doc == "A1" else T2
        if nouveau not in cible:
            raise SystemExit(f"{ident} : « nouveau » absent du texte en vigueur")
    sortie = dossier / "pieces" / "texte-en-vigueur-apres-second-addendum-v2.md"
    if sortie.exists():
        raise SystemExit(f"{sortie} existe déjà (R12)")
    sortie.write_text("<!-- Texte scellé lu avec le premier addendum (EC-1 à EC-8) et le second addendum (SA-1 à SA-20), produit par "
                      "pieces/controle-fragments-second-addendum-v2.py ; pièce de travail, ne fait pas foi. -->\n" + T2,
                      encoding="utf-8")
    sortie_a1 = dossier / "pieces" / "premier-addendum-lu-avec-le-second-v2.md"
    if sortie_a1.exists():
        raise SystemExit(f"{sortie_a1} existe déjà (R12)")
    sortie_a1.write_text("<!-- Premier addendum lu avec SA-21 à SA-25 du second, produit par "
                         "pieces/controle-fragments-second-addendum-v2.py ; pièce de travail, ne fait pas foi. -->\n" + A1b,
                         encoding="utf-8")
    from controle_ia.t07bbis import lecture_v3 as lv3
    pile = lv3.RESERVES_FIXES["R-PILE"].split(" : ", 1)[1]
    if f"« {pile} »" not in T2:
        raise SystemExit("phrase de R-PILE du texte en vigueur ≠ RESERVES_FIXES['R-PILE'] de lecture_v3")
    sept = lv3.SECTION_D.split("(6) le libellé d'information ne dit pas « plafond tient » ; ", 1)[1]
    if sept not in T2.replace("**une**", "une"):
        raise SystemExit("point (7) du texte en vigueur ≠ SECTION_D de lecture_v3")
    print("R-PILE et point (7) : égaux aux chaînes de lecture_v3")
    print(f"écrit {sortie.relative_to(dossier)} et {sortie_a1.relative_to(dossier)}")
    print(f"T : {len(T)} caractères ; T+1 : {len(T1)} ; T+2 : {len(T2)} ; A1 lu : {len(A1b)}")
    print("CONFORME")
    return 0


if __name__ == "__main__":
    sys.exit(main())
