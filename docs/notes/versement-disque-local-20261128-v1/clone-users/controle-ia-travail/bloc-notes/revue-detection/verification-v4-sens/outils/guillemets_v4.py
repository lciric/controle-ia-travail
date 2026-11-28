"""Toutes les phrases entre guillemets francais des lignes donnees de la v4, cherchees dans
toutes les pages de tous les PDF. Usage :
python3 -I -B guillemets_v4.py V4.md DEBUT-FIN [DEBUT-FIN ...]
Sortie : numero de ligne de la v4, phrase, cles et pages ou elle est trouvee.
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ch  # noqa: E402  (module voisin, ecrit pour cette verification)

CLES = sorted(os.listdir(ch.PAGES))


def main():
    v4 = open(sys.argv[1], encoding="utf-8").read().split("\n")
    plages = []
    for a in sys.argv[2:]:
        d, f = a.split("-")
        plages.append((int(d), int(f)))
    for d, f in plages:
        texte = "\n".join(v4[d - 1:f])
        for m in re.finditer(r"«\s*([^«»]+?)\s*»", texte):
            i = d + texte[:m.start()].count("\n")
            q = re.sub(r"\s+", " ", m.group(1))
            if True:
                if not re.search(r"[A-Za-z]{3}", q):
                    continue
                trouve = []
                for c in CLES:
                    r = ch.cherche(c, q)
                    pages = sorted(set([p for p, _ in r["r"]] + [p for p, _ in r["p"]]))
                    if pages:
                        trouve.append("%s p.%s" % (c, ",".join(map(str, pages))))
                print("v4 l.%d | %s | %s" % (i, q[:90], "; ".join(trouve) or "INTROUVABLE"))


if __name__ == "__main__":
    main()
