"""Compare le brouillon 2 au brouillon 1 auquel on applique les couples d'une contre-lecture.

Usage : comparer_brouillon2.py CONTRE_LECTURE RACINE_DEPOT BROUILLON2
  Les couples sont lus dans CONTRE_LECTURE (meme forme que pour verifier_couples.py) ;
  le fichier vise par les couples (brouillon 1) est lu sous RACINE_DEPOT.
Affiche : l'empreinte du brouillon 1, celle du texte attendu (brouillon 1 + couples),
celle du brouillon 2, puis chaque ecart ligne a ligne entre attendu et brouillon 2
(numero de ligne de chaque cote, texte entier des deux cotes), et le nombre d'ecarts.
Aucun fichier n'est ecrit. Outil du contre-lecteur de l'addendum 1 (barreau 5).
"""
import difflib
import hashlib
import os
import re
import sys

MOTIF = re.compile(
    r"- Fichier : `(?P<fichier>[^`]+)`\n"
    r"- Avant :\n````text\n(?P<avant>.*?)\n````\n"
    r"- Après :\n````text\n(?P<apres>.*?)\n````",
    re.S,
)


def empreinte(texte: str) -> str:
    return hashlib.sha256(texte.encode("utf-8")).hexdigest()


def main() -> int:
    piece, racine, chemin_b2 = sys.argv[1], sys.argv[2], sys.argv[3]
    with open(piece, encoding="utf-8") as f:
        couples = [m.groupdict() for m in MOTIF.finditer(f.read())]
    fichiers = {c["fichier"] for c in couples}
    if len(fichiers) != 1:
        print(f"fichiers vises {sorted(fichiers)} : un seul attendu ; refus")
        return 2
    with open(os.path.join(racine, fichiers.pop()), encoding="utf-8") as f:
        b1 = f.read()
    attendu = b1
    for i, c in enumerate(couples, 1):
        if attendu.count(c["avant"]) != 1:
            print(f"couple {i} : avant non unique dans le texte en cours ; refus")
            return 2
        attendu = attendu.replace(c["avant"], c["apres"], 1)
    with open(chemin_b2, encoding="utf-8") as f:
        b2 = f.read()
    print(f"couples appliques : {len(couples)}")
    print(f"sha256 brouillon 1 : {empreinte(b1)}")
    print(f"sha256 attendu (brouillon 1 + couples) : {empreinte(attendu)}")
    print(f"sha256 brouillon 2 : {empreinte(b2)}")
    la, lb = attendu.splitlines(), b2.splitlines()
    n = 0
    sm = difflib.SequenceMatcher(a=la, b=lb, autojunk=False)
    for op, a1, a2, b1_, b2_ in sm.get_opcodes():
        if op == "equal":
            continue
        n += 1
        print(f"--- ecart {n} : {op} ; attendu l. {a1 + 1} a {a2} ; brouillon 2 l. {b1_ + 1} a {b2_}")
        for k in range(a1, a2):
            print(f"  attendu  {k + 1:4d} | {la[k]}")
        for k in range(b1_, b2_):
            print(f"  brouil.2 {k + 1:4d} | {lb[k]}")
    print(f"ecarts : {n}")
    print(f"fin de fichier : attendu {'avec' if attendu.endswith(chr(10)) else 'sans'} saut final ; "
          f"brouillon 2 {'avec' if b2.endswith(chr(10)) else 'sans'} saut final")
    return 0


if __name__ == "__main__":
    sys.exit(main())
