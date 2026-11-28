"""Différentiel strict brouillon 6 -> brouillon 7 : jetons = mots et blancs (chaque blanc gardé tel quel).

Rend chaque changement (remplacement, insertion, suppression), avec ce qui change dans les blancs seuls,
et vérifie que les caractères non ASCII du texte inchangé sont identiques.
Usage : python -B diff_strict.py b6 b7
"""
import difflib
import re
import sys
import unicodedata
from pathlib import Path


def jetons(t: str) -> list[str]:
    return re.findall(r"\s+|[^\s]+", t)


def main(a: str, b: str) -> None:
    ta, tb = Path(a).read_text(encoding="utf-8"), Path(b).read_text(encoding="utf-8")
    ja, jb = jetons(ta), jetons(tb)
    assert "".join(ja) == ta and "".join(jb) == tb
    sm = difflib.SequenceMatcher(None, ja, jb, autojunk=False)
    n = 0
    blancs_seuls = 0
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op == "equal":
            continue
        avant, apres = "".join(ja[i1:i2]), "".join(jb[j1:j2])
        if avant.split() == apres.split():
            blancs_seuls += 1
            print(f"[blancs seuls] {op} {avant!r} -> {apres!r}")
            continue
        n += 1
        ligne_a = ta.count("\n", 0, len("".join(ja[:i1]))) + 1
        ligne_b = tb.count("\n", 0, len("".join(jb[:j1]))) + 1
        print(f"--- changement {n} ({op}) b6 l. {ligne_a} / b7 l. {ligne_b}")
        print(f"    b6 : {' '.join(avant.split())!r}")
        print(f"    b7 : {' '.join(apres.split())!r}")
    print(f"\nchangements de mots : {n} ; changements de blancs seuls : {blancs_seuls}")
    # caractères non ASCII et de contrôle, comptés dans chaque texte
    def inventaire(t):
        d = {}
        for ch in t:
            if ord(ch) > 126 or (ord(ch) < 32 and ch != "\n"):
                d[ch] = d.get(ch, 0) + 1
        return d
    ia, ib = inventaire(ta), inventaire(tb)
    for ch in sorted(set(ia) | set(ib)):
        if ia.get(ch, 0) != ib.get(ch, 0):
            print(f"caractère U+{ord(ch):04X} {unicodedata.name(ch, '?')} : b6 {ia.get(ch, 0)}, b7 {ib.get(ch, 0)}")
    print("fins de ligne CR : b6", ta.count("\r"), "b7", tb.count("\r"),
          "; tabulations : b6", ta.count("\t"), "b7", tb.count("\t"),
          "; espaces en fin de ligne : b6", len(re.findall(r" +\n", ta)), "b7", len(re.findall(r" +\n", tb)),
          "; fin de fichier par saut de ligne : b6", ta.endswith("\n"), "b7", tb.endswith("\n"))


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
