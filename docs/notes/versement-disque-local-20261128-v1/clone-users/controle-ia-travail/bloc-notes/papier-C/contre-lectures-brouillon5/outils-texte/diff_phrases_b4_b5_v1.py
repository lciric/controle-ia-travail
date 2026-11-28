"""Différentiel brouillon 4 -> brouillon 5 du préenregistrement du papier C, par phrase normalisée.

Lecture seule. Usage : python3 -I -B diff_phrases_b4_b5_v1.py B4 B5 > sortie
Normalisation : lignes d'un même paragraphe ou d'une même puce recollées, blancs réduits.
Découpe : par section de niveau 2 ou 3, puis par phrase (point, point-virgule suivis d'un blanc).
Sortie : phrases retirées (-) et ajoutées (+), section par section, avec leur rang.
"""
import difflib
import re
import sys
from pathlib import Path


def blocs(texte):
    """Recolle les lignes de suite (indentées) d'une puce ou d'un paragraphe."""
    sortie, courant = [], []
    for ligne in texte.splitlines():
        if not ligne.strip():
            if courant:
                sortie.append(" ".join(courant))
                courant = []
            continue
        debut_bloc = bool(re.match(r"^(#|\s*[-|]|\s*\d+(\.\d+)?\.? |\s*\d+ bis\.|\*\*\[)", ligne)) and not ligne.startswith("   ")
        if re.match(r"^\s*- ", ligne) or re.match(r"^#", ligne) or re.match(r"^\|", ligne) or re.match(r"^\d+(\.\d+)? ", ligne) or re.match(r"^\d+\. ", ligne) or re.match(r"^\d+ bis\. ", ligne):
            debut_bloc = True
        if debut_bloc and courant:
            sortie.append(" ".join(courant))
            courant = []
        courant.append(ligne.strip())
    if courant:
        sortie.append(" ".join(courant))
    return [re.sub(r"\s+", " ", b) for b in sortie]


def phrases(texte):
    res = []
    section = "(en-tête)"
    for b in blocs(texte):
        if b.startswith("#"):
            section = b
            res.append((section, b))
            continue
        for p in re.split(r"(?<=[.;])\s+(?=[A-ZÀ-Ü«(\-*0-9λĉĝḠΔ])", b):
            p = p.strip()
            if p:
                res.append((section, p))
    return res


def main():
    a = phrases(Path(sys.argv[1]).read_text(encoding="utf-8"))
    b = phrases(Path(sys.argv[2]).read_text(encoding="utf-8"))
    ta = [p for _, p in a]
    tb = [p for _, p in b]
    sm = difflib.SequenceMatcher(a=ta, b=tb, autojunk=False)
    n_moins = n_plus = 0
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op == "equal":
            continue
        print(f"=== {op} b4[{i1}:{i2}] b5[{j1}:{j2}] ; section b5 : {b[j1][0] if j1 < len(b) else '(fin)'}")
        for i in range(i1, i2):
            print(f"- [{i}] {ta[i]}")
            n_moins += 1
        for j in range(j1, j2):
            print(f"+ [{j}] {tb[j]}")
            n_plus += 1
    print(f"# phrases : b4 {len(ta)} ; b5 {len(tb)} ; retirées {n_moins} ; ajoutées {n_plus}")


if __name__ == "__main__":
    main()
