"""Lecture des pages des PDF de la revue, pour la vérification de la v3 (angle fidélité, tour 2).

Indépendant des outils du correcteur : empreinte complète contrôlée, puis texte extrait directement
par pdftotext (modes défaut, -raw, -layout), en mémoire, découpé par saut de page. Rien n'est écrit.

Usage :
  python3 -I -B page3.py CLE PAGE "phrase" [largeur] [mode]   # phrase en contexte, à la page exacte
  python3 -I -B page3.py --ou CLE "phrase"                     # toutes les pages où la phrase se trouve
  python3 -I -B page3.py --page CLE PAGE [mode]                # texte brut de la page
"""
import hashlib
import json
import re
import subprocess
import sys
import unicodedata

CITATIONS = ("/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/revue-detection/"
             "redaction/citations-synthese-v1.json")
MODES = ("defaut", "raw", "layout")
_cache = {}
_pdfs = None


def pdfs():
    global _pdfs
    if _pdfs is None:
        d = json.load(open(CITATIONS))["pdfs"]
        _pdfs = {k: (v["chemin"], v["sha256"]) for k, v in d.items()}
        # RO : absent du JSON ; empreinte complète donnée par la synthèse (section 6).
        _pdfs["RO"] = ("/home/user/controle-ia-travail/docs/sources/pdf/2604.01151v3.pdf",
                       "bde99a620dbbb4064fcfd9a010ac4e92b17b619c5995ae0696911afdbed7686b")
    return _pdfs


def empreinte(chemin):
    h = hashlib.sha256()
    with open(chemin, "rb") as f:
        for bloc in iter(lambda: f.read(1 << 20), b""):
            h.update(bloc)
    return h.hexdigest()


def controle(cle):
    chemin, attendu = pdfs()[cle]
    vu = empreinte(chemin)
    if vu != attendu:
        raise SystemExit("EMPREINTE DIFFERENTE %s : %s contre %s" % (cle, vu, attendu))
    return chemin, vu


def pages(cle, mode="defaut"):
    if (cle, mode) in _cache:
        return _cache[(cle, mode)]
    chemin, _ = controle(cle)
    args = ["pdftotext", "-enc", "UTF-8"]
    if mode == "raw":
        args.append("-raw")
    elif mode == "layout":
        args.append("-layout")
    args += [chemin, "-"]
    sortie = subprocess.run(args, check=True, capture_output=True).stdout.decode("utf-8", "replace")
    morceaux = sortie.split("\f")
    if morceaux and morceaux[-1].strip() == "":
        morceaux = morceaux[:-1]
    _cache[(cle, mode)] = morceaux
    return morceaux


REMPL = [("’", "'"), ("‘", "'"), ("“", '"'), ("”", '"'), ("−", "-"), ("–", "-"),
         ("—", "-"), ("ﬁ", "fi"), ("ﬂ", "fl"), (" ", " "), (" ", " ")]


def norm(s, coupure="colle"):
    s = unicodedata.normalize("NFKC", s)
    for a, b in REMPL:
        s = s.replace(a, b)
    if coupure == "colle":
        s = re.sub(r"-\s*\n\s*", "", s)
    else:
        s = re.sub(r"-\s*\n\s*", "-", s)
    s = re.sub(r"\s+", " ", s)
    return s.lower().strip()


_ncache = {}


def page_norm(cle, page, mode, coupure):
    k = (cle, page, mode, coupure)
    if k not in _ncache:
        ps = pages(cle, mode)
        _ncache[k] = norm(ps[page - 1], coupure) if 1 <= page <= len(ps) else ""
    return _ncache[k]


def present(cle, page, phrase):
    """Vrai si la phrase est sur la page (1 = première page du fichier), dans un des modes."""
    q = {c: norm(phrase, c) for c in ("colle", "garde")}
    for mode in MODES:
        for c in ("colle", "garde"):
            t = page_norm(cle, page, mode, c)
            if t and (q[c] in t or q["colle"] in t):
                return mode
    return None


def ou(cle, phrase):
    res = []
    n = len(pages(cle, "defaut"))
    for p in range(1, n + 1):
        if present(cle, p, phrase):
            res.append(p)
    return res


def contexte(cle, page, phrase, largeur=300, mode="defaut"):
    t = norm(pages(cle, mode)[page - 1])
    q = norm(phrase)
    i = t.find(q)
    if i < 0:
        t = norm(pages(cle, mode)[page - 1], "garde")
        i = t.find(q)
    if i < 0:
        return None
    return t[max(0, i - largeur):i + len(q) + largeur]


def lignes_avec(cle, page, mots, mode="layout"):
    """Lignes de la page (mise en page) qui contiennent tous les mots donnés."""
    out = []
    for n, l in enumerate(pages(cle, mode)[page - 1].split("\n"), 1):
        ln = norm(l)
        if all(norm(m) in ln for m in mots):
            out.append((n, l.rstrip()))
    return out


def ligne_de(cle, page, debut, mode="raw"):
    """Numéro (1 = première ligne) de la ligne de la page où commence le fragment donné (mode raw ou layout)."""
    q = norm(debut)
    for n, l in enumerate(pages(cle, mode)[page - 1].split("\n"), 1):
        if q in norm(l):
            return n
    return None


if __name__ == "__main__":
    a = sys.argv[1:]
    if a and a[0] == "--ligne":
        mode = a[4] if len(a) > 4 else "raw"
        print(a[1], "p.", a[2], "mode", mode, "l.", ligne_de(a[1], int(a[2]), a[3], mode), "|", a[3])
    elif a and a[0] == "--ou":
        print(a[1], repr(a[2]), "pages :", ou(a[1], a[2]))
    elif a and a[0] == "--page":
        mode = a[3] if len(a) > 3 else "defaut"
        print(pages(a[1], mode)[int(a[2]) - 1])
    else:
        cle, page, phrase = a[0], int(a[1]), a[2]
        largeur = int(a[3]) if len(a) > 3 else 300
        mode = a[4] if len(a) > 4 else "defaut"
        m = present(cle, page, phrase)
        print(cle, "p.", page, "présent" if m else "ABSENT", "(mode %s)" % m if m else "")
        if m:
            print(contexte(cle, page, phrase, largeur, m if m in MODES else mode))
