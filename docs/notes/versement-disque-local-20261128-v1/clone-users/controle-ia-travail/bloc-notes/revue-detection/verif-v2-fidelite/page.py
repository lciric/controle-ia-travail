"""Lit une page d'un PDF de la table des clés, directement par pdftotext (sans fichier intermédiaire).

Usage : python3 -I page.py CLE PAGE [PHRASE] [LARGEUR] [MODE]
- vérifie d'abord l'empreinte du PDF (préfixe de cles.txt ; RO : empreinte complète) ;
- MODE : def (défaut de pdftotext), layout, raw ; sans PHRASE : imprime la page ;
- avec PHRASE : normalise (NFKC, guillemets, tirets, ligatures, césures, espaces, casse) et imprime chaque occurrence
  avec LARGEUR signes de contexte (défaut 300), ou « INTROUVABLE ».
"""
import hashlib
import re
import subprocess
import sys
import unicodedata

CLES = "/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/revue-detection/verification/cles.txt"
RO = ("/home/user/controle-ia-travail/docs/sources/pdf/2604.01151v3.pdf",
      "bde99a620dbbb4064fcfd9a010ac4e92b17b619c5995ae0696911afdbed7686b")


def table():
    t = {"RO": RO}
    for ligne in open(CLES, encoding="utf-8"):
        k, p, h = ligne.split()
        t[k] = (p, h)
    return t


def norm(s):
    s = unicodedata.normalize("NFKC", s)
    for a, b in [("’", "'"), ("‘", "'"), ("“", '"'), ("”", '"'), ("−", "-"),
                 ("–", "-"), ("—", "-"), ("ﬁ", "fi"), ("ﬂ", "fl")]:
        s = s.replace(a, b)
    s = re.sub(r"-\s*\n\s*", "", s)
    s = re.sub(r"\s+", " ", s)
    return s


def texte(cle, page, mode="def"):
    p, h = table()[cle]
    e = hashlib.sha256(open(p, "rb").read()).hexdigest()
    if not e.startswith(h):
        sys.exit(f"EMPREINTE DIFFERENTE {cle} {e}")
    opts = {"def": [], "layout": ["-layout"], "raw": ["-raw"]}[mode]
    out = subprocess.run(["pdftotext", *opts, "-f", str(page), "-l", str(page), p, "-"],
                         capture_output=True, check=True).stdout.decode("utf-8", "replace")
    return out


def main():
    cle, page = sys.argv[1], int(sys.argv[2])
    phrase = sys.argv[3] if len(sys.argv) > 3 else None
    w = int(sys.argv[4]) if len(sys.argv) > 4 else 300
    mode = sys.argv[5] if len(sys.argv) > 5 else "def"
    t = texte(cle, page, mode)
    if phrase is None:
        print(t)
        return
    n = norm(t)
    nl, q = n.lower(), norm(phrase).lower()
    i = nl.find(q)
    if i < 0:
        print(f"INTROUVABLE {cle} p. {page} ({mode}) : {phrase!r}")
    while i >= 0:
        print(f"== {cle} p. {page} ({mode}) : ...{n[max(0, i - w):i + len(q) + w]}...\n")
        i = nl.find(q, i + 1)


if __name__ == "__main__":
    main()
