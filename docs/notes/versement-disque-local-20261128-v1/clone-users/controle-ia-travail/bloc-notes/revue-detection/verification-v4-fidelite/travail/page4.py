"""Une page d'un PDF empreinté, lue directement par pdftotext, en mémoire (vérification v4, angle fidélité).

Usage :
  python3 -I -B page4.py --page CLE PAGE [raw|layout]          imprime la page, lignes numérotées
  python3 -I -B page4.py CLE PAGE "phrase" [raw|layout]         phrase sur la page ? et sur quelles autres pages ?
L'empreinte complète du PDF est recalculée à chaque appel et comparée au préfixe de cles.txt ; écart : arrêt.
"""
import hashlib
import re
import subprocess
import sys
import unicodedata
from pathlib import Path

CLES = Path("/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/revue-detection/verification/cles.txt")


def pdf(cle):
    for ligne in CLES.read_text().splitlines():
        k, p, h = ligne.split()
        if k == cle:
            s = hashlib.sha256(Path(p).read_bytes()).hexdigest()
            if not s.startswith(h):
                sys.exit(f"empreinte en écart pour {cle} : {s}")
            return p
    sys.exit(f"clé inconnue : {cle}")


def texte(p, page, mode):
    opt = ["-raw"] if mode == "raw" else ["-layout"]
    r = subprocess.run(["pdftotext", *opt, "-f", str(page), "-l", str(page), p, "-"],
                       capture_output=True, text=True, check=True)
    return r.stdout


def nbpages(p):
    r = subprocess.run(["pdfinfo", p], capture_output=True, text=True, check=True)
    return int(re.search(r"Pages:\s+(\d+)", r.stdout).group(1))


def norm(s):
    s = unicodedata.normalize("NFKC", s)
    for a, b in [("’", "'"), ("‘", "'"), ("“", '"'), ("”", '"'), ("−", "-"), ("–", "-"), ("—", "-")]:
        s = s.replace(a, b)
    s = re.sub(r"-\s*\n\s*", "", s)
    s = re.sub(r"\s+", " ", s)
    return s.lower().strip()


def main():
    a = sys.argv[1:]
    if a[0] == "--page":
        cle, page = a[1], int(a[2])
        mode = a[3] if len(a) > 3 else "raw"
        for i, l in enumerate(texte(pdf(cle), page, mode).splitlines(), 1):
            print(f"{i:3d}: {l}")
        return
    cle, page, phrase = a[0], int(a[1]), a[2]
    mode = a[3] if len(a) > 3 else "raw"
    p = pdf(cle)
    f = norm(phrase)
    ici = f in norm(texte(p, page, mode))
    autres = []
    if not ici:
        for q in range(1, nbpages(p) + 1):
            if q != page and f in norm(texte(p, q, mode)):
                autres.append(q)
    print(f"{cle} p.{page} {mode} {'TROUVÉ' if ici else 'ABSENT'} {repr(phrase[:80])}"
          + ("" if ici else f" ; autres pages : {autres}"))
    sys.exit(0 if ici else 1)


if __name__ == "__main__":
    main()
