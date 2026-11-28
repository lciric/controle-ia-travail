"""Extrait titre, auteurs, résumé, commentaire et historique des versions d'une page de résumé arXiv.

Usage : python3 -I -B extraire_resumes_cp02_v1.py PAGE.html [PAGE.html ...]
Lecture seule des pages passées en argument ; aucune écriture.
"""
import hashlib
import html
import re
import sys


def texte(fragment):
    fragment = re.sub(r"<[^>]+>", " ", fragment)
    fragment = html.unescape(fragment)
    return re.sub(r"\s+", " ", fragment).strip()


def extraire(chemin):
    brut = open(chemin, "rb").read()
    empreinte = hashlib.sha256(brut).hexdigest()
    page = brut.decode("utf-8", "replace")
    titre = re.search(r'<h1 class="title mathjax">(.*?)</h1>', page, re.S)
    auteurs = re.search(r'<div class="authors">(.*?)</div>', page, re.S)
    resume = re.search(r'<blockquote class="abstract mathjax">(.*?)</blockquote>', page, re.S)
    commentaire = re.search(r'<td class="tablecell comments mathjax">(.*?)</td>', page, re.S)
    historique = re.search(r'<div class="submission-history">(.*?)</div>', page, re.S)
    print("=" * 100)
    print("fichier :", chemin)
    print("sha256  :", empreinte)
    for nom, m in (("titre", titre), ("auteurs", auteurs), ("commentaire", commentaire),
                   ("historique", historique), ("résumé", resume)):
        print(f"{nom} :", texte(m.group(1)) if m else "<<ABSENT>>")


if __name__ == "__main__":
    for chemin in sys.argv[1:]:
        extraire(chemin)
