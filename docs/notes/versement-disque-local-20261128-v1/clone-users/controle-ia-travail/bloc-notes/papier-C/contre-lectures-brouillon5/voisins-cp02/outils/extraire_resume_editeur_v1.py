"""Extrait d'une page d'article de l'éditeur (Nature) le résumé et les métadonnées « citation_* » seulement.

Usage : python3 -I -B extraire_resume_editeur_v1.py PAGE.html
Lecture seule. N'imprime ni le corps de l'article ni les sections autres que le résumé.
Signale aussi, sans les lire, la présence de sections de corps (indice d'accès libre).
"""
import hashlib
import html
import re
import sys


def texte(fragment):
    fragment = re.sub(r"<[^>]+>", " ", fragment)
    fragment = html.unescape(fragment)
    return re.sub(r"\s+", " ", fragment).strip()


def main(chemin):
    brut = open(chemin, "rb").read()
    print("fichier :", chemin)
    print("sha256  :", hashlib.sha256(brut).hexdigest())
    page = brut.decode("utf-8", "replace")
    titre = re.search(r"<title>(.*?)</title>", page, re.S)
    print("titre de la page :", texte(titre.group(1)) if titre else "<<ABSENT>>")
    noms = ("citation_title", "citation_journal_title", "citation_volume", "citation_issue",
            "citation_firstpage", "citation_lastpage", "citation_doi", "citation_publication_date",
            "citation_online_date", "dc.date", "dc.type", "citation_article_type", "citation_author",
            "WT.cg_s", "dc.rights", "access")
    for nom in noms:
        valeurs = re.findall(r'<meta\s+name="%s"\s+content="([^"]*)"' % re.escape(nom), page)
        if valeurs:
            print(f"{nom} :", " ; ".join(html.unescape(v) for v in valeurs))
    # Bloc du résumé : section Abs1 (gabarit Nature)
    resume = re.search(r'<div class="c-article-section__content" id="Abs1-content">(.*?)</div>', page, re.S)
    print("résumé (Abs1) :", texte(resume.group(1)) if resume else "<<ABSENT>>")
    # Indice d'accès : sections de corps présentes ? (titres seulement, sans contenu)
    sections = re.findall(r'<h2 class="c-article-section__title[^"]*"[^>]*id="([^"]+)"[^>]*>(.*?)</h2>', page, re.S)
    print("titres de section présents :", " | ".join(f"{i}: {texte(t)}" for i, t in sections))
    acces = re.findall(r'(Open access|Subscribe to this journal|Buy this article|Access through your institution)', page)
    print("mentions d'accès :", sorted(set(acces)))
    historique = re.findall(r'<li class="c-bibliographic-information__list-item[^"]*">(.*?)</li>', page, re.S)
    print("informations bibliographiques :", " | ".join(texte(h) for h in historique[:12]))


if __name__ == "__main__":
    main(sys.argv[1])
