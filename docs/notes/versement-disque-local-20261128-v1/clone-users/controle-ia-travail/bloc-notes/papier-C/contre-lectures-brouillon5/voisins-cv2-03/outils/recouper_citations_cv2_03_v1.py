"""Recoupe tous les segments entre guillemets francais de la note avec le texte entier des deux PDF empreintes.
Usage : python3 -I -B recouper_citations_cv2_03_v1.py NOTE PDF1 SHA1 PDF2 SHA2
Affiche, pour chaque segment, TROUVE (dans quel PDF) ou INTROUVABLE ; les introuvables sont a justifier a la main
(phrases francaises, corrections proposees, citations d'autres notes). Empreinte differente : arret, code 1."""
import hashlib, re, subprocess, sys, unicodedata

PAIRES = [("’", "'"), ("‘", "'"), ("“", '"'), ("”", '"'), ("–", "-"), ("—", "-"),
          ("−", "-"), (" ", " "), (" ", " ")]

def norm(s):
    s = unicodedata.normalize("NFKC", s)
    for a, b in PAIRES:
        s = s.replace(a, b)
    return s

def sha(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()

def texte(pdf):
    t = norm(subprocess.run(["pdftotext", "-raw", pdf, "-"], capture_output=True, text=True, check=True).stdout)
    return [re.sub(r"\s+", " ", re.sub(r"-\s*\n\s*", r, t)) for r in ("-", "")] + [re.sub(r"\s+", " ", t)]

def main():
    note, p1, s1, p2, s2 = sys.argv[1:6]
    sources = {}
    for p, s, nom in ((p1, s1, "PDF1"), (p2, s2, "PDF2")):
        if sha(p) != s:
            print("ARRET : empreinte differente " + p)
            sys.exit(1)
        sources[nom] = texte(p)
    n = re.sub(r"\s+", " ", norm(open(note, encoding="utf-8").read()))
    segs = re.findall(r"« ([^«»]+?) »", n)
    trouves = introuvables = 0
    for s in segs:
        ou = [k for k, v in sources.items() if any(s in x for x in v)]
        if ou:
            trouves += 1
            print("TROUVE (%s) | %s" % (",".join(ou), s[:100]))
        else:
            introuvables += 1
            print("INTROUVABLE | %s" % s[:100])
    print("BILAN : %d segments, %d trouves, %d introuvables" % (len(segs), trouves, introuvables))

if __name__ == "__main__":
    main()
