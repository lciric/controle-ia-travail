"""Extrait le texte du corps d'une page d'article de l'éditeur (HTML), section par section.

Usage : python3 -I -B extraire_corps_editeur_v1.py PAGE.html EMPREINTE_ATTENDUE SORTIE.txt
Refuse si l'empreinte de la page diffère (R5). Écrit une ligne « ### <titre> » par titre h1 à h4,
puis les paragraphes, légendes et éléments de liste. Rien n'est réécrit : texte brut, entités décodées.
"""
import hashlib
import html
import re
import sys
from html.parser import HTMLParser


class Extracteur(HTMLParser):
    BLOCS = {"p", "h1", "h2", "h3", "h4", "figcaption", "li", "td", "th", "caption"}
    IGNORES = {"script", "style", "noscript", "svg", "nav", "footer", "header", "button"}

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.lignes = []
        self.pile_ignore = 0
        self.courant = None
        self.balise = None

    def handle_starttag(self, tag, attrs):
        if tag in self.IGNORES:
            self.pile_ignore += 1
            return
        if self.pile_ignore:
            return
        if tag in self.BLOCS:
            self._vider()
            self.courant = []
            self.balise = tag
        elif tag == "br" and self.courant is not None:
            self.courant.append(" ")

    def handle_endtag(self, tag):
        if tag in self.IGNORES:
            self.pile_ignore = max(0, self.pile_ignore - 1)
            return
        if self.pile_ignore:
            return
        if tag in self.BLOCS and self.balise == tag:
            self._vider()

    def handle_data(self, data):
        if self.pile_ignore:
            return
        if self.courant is not None:
            self.courant.append(data)

    def _vider(self):
        if self.courant is not None:
            texte = re.sub(r"\s+", " ", "".join(self.courant)).strip()
            if texte:
                if self.balise in {"h1", "h2", "h3", "h4"}:
                    self.lignes.append("### " + texte)
                else:
                    self.lignes.append(texte)
        self.courant = None
        self.balise = None


def main():
    page, attendue, sortie = sys.argv[1], sys.argv[2], sys.argv[3]
    donnees = open(page, "rb").read()
    obtenue = hashlib.sha256(donnees).hexdigest()
    if obtenue != attendue:
        print(f"REFUS empreinte : attendue {attendue}, obtenue {obtenue}")
        sys.exit(2)
    ex = Extracteur()
    ex.feed(donnees.decode("utf-8"))
    ex._vider()
    with open(sortie, "w", encoding="utf-8") as f:
        f.write(f"# source {page}\n# sha256 {obtenue}\n")
        for ligne in ex.lignes:
            f.write(html.unescape(ligne) + "\n")
    print(f"OK {len(ex.lignes)} lignes -> {sortie}")


if __name__ == "__main__":
    main()
