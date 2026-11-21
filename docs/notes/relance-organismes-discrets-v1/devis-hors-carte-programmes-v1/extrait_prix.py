# Extraction de texte des pages de prix versees (lecture seule, hors reseau).
import html, re, sys
from html.parser import HTMLParser

class T(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.out = []
        self.skip = 0
    def handle_starttag(self, tag, attrs):
        if tag in ("script", "style", "noscript", "svg"):
            self.skip += 1
        if tag in ("p", "div", "tr", "li", "h1", "h2", "h3", "h4", "table", "section", "br", "td", "th"):
            self.out.append("\n")
    def handle_endtag(self, tag):
        if tag in ("script", "style", "noscript", "svg") and self.skip:
            self.skip -= 1
    def handle_data(self, d):
        if not self.skip:
            self.out.append(d)

def texte(path):
    raw = open(path, "rb").read().decode("utf-8", "replace")
    p = T()
    p.feed(raw)
    t = "".join(p.out)
    t = re.sub(r"[ \t\r\f\v]+", " ", t)
    t = re.sub(r"\n\s*\n+", "\n", t)
    return raw, t

if __name__ == "__main__":
    path = sys.argv[1]
    motifs = sys.argv[2:]
    raw, t = texte(path)
    lignes = t.split("\n")
    print("octets:", len(raw.encode("utf-8")), "lignes de texte:", len(lignes))
    for m in motifs:
        print("=== motif:", m)
        rx = re.compile(m, re.I)
        n = 0
        for i, l in enumerate(lignes):
            if rx.search(l):
                n += 1
                a, b = max(0, i - 2), min(len(lignes), i + 6)
                print("--- ligne", i)
                for j in range(a, b):
                    s = lignes[j].strip()
                    if s:
                        print("   ", s[:300])
                if n >= 12:
                    print("   (coupé à 12 occurrences)")
                    break
        print("occurrences vues:", n)
