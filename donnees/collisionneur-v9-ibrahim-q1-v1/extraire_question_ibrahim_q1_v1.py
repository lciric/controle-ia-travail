"""Extrait la question servie du tour du collisionneur v9 sur la question 1 de Lujain Ibrahim (conv-audit n° 416 (e5d2f7af…, canal/conv-audit-n04)). Source : `question-collisionneur-ibrahim-v1.md`
(5e905798…, empreinte exigée). Sections servies, à l'octet, dans l'ordre du fichier : de la ligne « ## La question, telle que … »
jusqu'à la ligne qui précède « ## Lecture prévue de la sortie » (non servie, comme le titre et la provenance) ; seules les lignes
vides de fin sont réduites à un saut de ligne final. Copie adaptée de extraire_question_conception_organisme_v1.py (branche
donnees/collisionneur-v9-conception-organisme-v1, 676495c9) ; seuls changent la source, son empreinte et le premier titre.
Écriture en mode « x » (on n'écrase jamais).
Usage : python3 -I extraire_question_ibrahim_q1_v1.py QUESTION_SOURCE SORTIE"""
import hashlib, sys
src, sortie = sys.argv[1:3]
ATTENDU = "5e905798a512db9fb9c607be0fbe74972d7df618cf8b9026c23eb0bc8ed6d9c0"
octets = open(src, "rb").read()
h = hashlib.sha256(octets).hexdigest()
if h != ATTENDU:
    sys.exit(f"question source : empreinte {h} au lieu de {ATTENDU} ; rien n'est écrit")
texte = octets.decode("utf-8")
DEBUT, FIN = "\n## La question, telle que ", "\n## Lecture prévue de la sortie\n"
assert texte.count(DEBUT) == 1 and texte.count(FIN) == 1 and texte.index(DEBUT) < texte.index(FIN)
servie = texte[texte.index(DEBUT) + 1:texte.index(FIN)].rstrip("\n") + "\n"
titres = [l for l in servie.splitlines() if l.startswith("## ")]
assert len(titres) == 3 and titres[0].startswith("## La question, telle que ") and titres[1:] == [
    "## Ce qu'on attend de chaque espèce", "## Règles d'intégrité (reprises dans la consigne)"], titres
open(sortie, "x", encoding="utf-8").write(servie)
print(len(titres), "sections,", len(servie.encode()), "octets")
