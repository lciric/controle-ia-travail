"""Cherche une phrase dans les pages extraites d'un PDF (verification v4, angle sens).

Usage : python3 -I -B ch.py CLE "phrase" [page]
Sortie : pages ou la phrase est trouvee (texte brut rNNN, mise en page pNNN), avec la
premiere ligne du fichier brut ou elle commence. Normalisation : NFKC, guillemets et
tirets ramenes a l'ASCII, cesures recollees, espaces reduits, minuscules.
"""
import os
import re
import sys
import unicodedata

ICI = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAGES = os.path.join(ICI, "pages")

REMPL = [("’", "'"), ("‘", "'"), ("“", '"'), ("”", '"'),
         ("−", "-"), ("–", "-"), ("—", "-"), ("ﬁ", "fi"),
         ("ﬂ", "fl"), (" ", " ")]


def norm(s):
    s = unicodedata.normalize("NFKC", s)
    for a, b in REMPL:
        s = s.replace(a, b)
    s = re.sub(r"-\s*\n\s*", "", s)
    s = re.sub(r"\s+", " ", s)
    return s.lower().strip()


def ligne_de(texte, phrase_n):
    """Premiere ligne (1-indexee) du fichier ou commence la phrase normalisee."""
    lignes = texte.split("\n")
    for i in range(len(lignes)):
        bloc = norm("\n".join(lignes[i:i + 12]))
        if bloc.startswith(phrase_n[:40]) or phrase_n in bloc and phrase_n not in norm("\n".join(lignes[i + 1:i + 12])):
            return i + 1
    return None


def cherche(cle, phrase, page=None):
    d = os.path.join(PAGES, cle)
    pn = norm(phrase)
    res = {"r": [], "p": []}
    for f in sorted(os.listdir(d)):
        typ = f[0]
        num = int(f[1:4])
        if page is not None and num != page:
            continue
        t = open(os.path.join(d, f), encoding="utf-8", errors="ignore").read()
        if pn in norm(t):
            res[typ].append((num, ligne_de(t, pn)))
    return res


if __name__ == "__main__":
    cle = sys.argv[1]
    phrase = sys.argv[2]
    page = int(sys.argv[3]) if len(sys.argv) > 3 else None
    r = cherche(cle, phrase, page)
    print(cle, repr(phrase[:80]), "brut:", r["r"], "mise en page:", r["p"])
