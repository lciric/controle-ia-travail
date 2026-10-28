"""Extrait le texte visible d'une page HTML (bibliothèque standard seule) et l'écrit dans un fichier texte, avec les titres
marqués et les liens listés à part. Usage : python -I html_vers_texte_v1.py PAGE.html SORTIE.txt LIENS.txt"""
import html, pathlib, re, sys
from html.parser import HTMLParser

class Extracteur(HTMLParser):
    def __init__(self):
        super().__init__()
        self.morceaux, self.liens, self.pile = [], [], []
        self.ignore = 0
    def handle_starttag(self, tag, attrs):
        if tag in ("script", "style", "svg", "noscript"):
            self.ignore += 1
        if tag in ("h1", "h2", "h3", "h4"):
            self.morceaux.append(f"\n\n[{tag.upper()}] ")
        elif tag in ("p", "li", "div", "section", "figcaption", "blockquote", "tr", "br"):
            self.morceaux.append("\n")
        if tag == "a":
            for k, v in attrs:
                if k == "href" and v:
                    self.liens.append(v)
    def handle_endtag(self, tag):
        if tag in ("script", "style", "svg", "noscript") and self.ignore:
            self.ignore -= 1
    def handle_data(self, data):
        if not self.ignore:
            self.morceaux.append(data)

page, sortie, liens = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2]), pathlib.Path(sys.argv[3])
e = Extracteur()
e.feed(page.read_text(encoding="utf-8", errors="replace"))
texte = html.unescape("".join(e.morceaux))
texte = re.sub(r"[ \t]+", " ", texte)
texte = re.sub(r"\n\s*\n\s*\n+", "\n\n", texte)
sortie.write_text(texte, encoding="utf-8")
liens.write_text("\n".join(dict.fromkeys(e.liens)) + "\n", encoding="utf-8")
print(f"texte : {len(texte)} caractères ; liens : {len(dict.fromkeys(e.liens))}")
