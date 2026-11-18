"""Compte des marqueurs `<<NOM>>` dans des fichiers texte (ii-b) — v1.

Usage : python3 -I -B compter-marqueurs-ii-b-v1.py FICHIER...
Ne cherche que le motif des marqueurs, `<<[A-Z0-9_]+>>` ; rien d'autre n'est lu ni affiché.
Pour chaque fichier : son empreinte, le nombre d'occurrences, le nombre de marqueurs distincts et leur liste triée.
"""
from __future__ import annotations

import hashlib
import re
import sys
from collections import Counter
from pathlib import Path

MOTIF = re.compile(r"<<([A-Z0-9_]+)>>")


def main() -> None:
    for chemin in sys.argv[1:]:
        b = Path(chemin).read_bytes()
        c = Counter(MOTIF.findall(b.decode("utf-8")))
        print(f"{Path(chemin).name}  {hashlib.sha256(b).hexdigest()}")
        print(f"  occurrences {sum(c.values())} ; distincts {len(c)}")
        for nom in sorted(c):
            print(f"  {nom} {c[nom]}")


if __name__ == "__main__":
    main()
