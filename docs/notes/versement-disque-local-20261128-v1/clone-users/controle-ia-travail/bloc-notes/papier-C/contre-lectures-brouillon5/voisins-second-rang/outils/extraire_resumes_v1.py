"""Extrait titre, auteurs, résumé, historique, commentaires et référence de revue
des pages de résumé arXiv (export.arxiv.org/abs/...) passées en argument.
Usage : python3 -I -B extraire_resumes_v1.py FICHIER.html ...
"""
import html
import re
import sys


def texte(fragment):
    fragment = re.sub(r"<[^>]+>", " ", fragment)
    fragment = html.unescape(fragment)
    return re.sub(r"\s+", " ", fragment).strip()


def champ(motif, page):
    m = re.search(motif, page, re.S)
    return texte(m.group(1)) if m else "(absent)"


for chemin in sys.argv[1:]:
    with open(chemin, encoding="utf-8") as f:
        page = f.read()
    print("=" * 100)
    print("FICHIER :", chemin)
    print("TITRE :", champ(r'<h1 class="title mathjax">(.*?)</h1>', page))
    print("AUTEURS :", champ(r'<div class="authors">(.*?)</div>', page))
    print("COMMENTAIRES :", champ(r'<td class="tablecell comments mathjax">(.*?)</td>', page))
    print("REVUE :", champ(r'<td class="tablecell jref">(.*?)</td>', page))
    print("DOI :", champ(r'<td class="tablecell doi">(.*?)</td>', page))
    print("SUJETS :", champ(r'<td class="tablecell subjects">(.*?)</td>', page))
    print("HISTORIQUE :", champ(r'<div class="submission-history">(.*?)</div>', page))
    print("RESUME :", champ(r'<blockquote class="abstract mathjax">(.*?)</blockquote>', page))
