"""Lignes de la v6 où se trouve le texte neuf de chaque remplacement (correcteur v6). Lecture seule.
Usage : python3 -I -B localiser_v6.py V6.md
"""
import hashlib
import os
import re
import sys
from pathlib import Path

ICI = Path(os.path.abspath(__file__)).parent
sys.path.insert(0, str(ICI))
import appliquer_corrections_v6 as ap  # noqa: E402


def main():
    v6p = Path(sys.argv[1])
    b = v6p.read_bytes()
    print(f"# v6 {v6p.name} {hashlib.sha256(b).hexdigest()}")
    v6 = b.decode("utf-8")
    E = ap.entrees(ap.corrections(), ap.comptes())
    for etiq, a, nouveau in E:
        motif = r"\s+".join(re.escape(t) for t in nouveau.split())
        m = list(re.finditer(motif, v6))
        if len(m) != 1:
            print(f"FAUTE | {etiq} | texte neuf trouvé {len(m)} fois")
            continue
        d = v6.count("\n", 0, m[0].start()) + 1
        f = v6.count("\n", 0, m[0].end()) + 1
        print(f"{etiq} | l. {d}" + (f"-{f}" if f != d else ""))


if __name__ == "__main__":
    main()
