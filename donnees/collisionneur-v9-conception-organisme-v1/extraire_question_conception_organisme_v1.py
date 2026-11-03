"""Extrait la question servie du tour du collisionneur v9 sur la conception de l'organisme d'idéation (spécification de conv-audit
`specification-collisionneur-conception-organisme-v1.md`, 7de4cb16…, § 2 : « --question = les trois sections servies de la
question »). Source : `question-collisionneur-conception-organisme-v1.md` (b7420561…, empreinte exigée). Sections servies, à
l'octet, dans l'ordre du fichier : de la ligne « ## La demande, telle que Lazar l'a écrite … » jusqu'à la ligne qui précède
« ## Lecture prévue de la sortie » (non servie, comme le titre et la provenance) ; seules les lignes vides de fin sont réduites à
un saut de ligne final. Écriture en mode « x » (on n'écrase jamais).
Usage : python3 -I extraire_question_conception_organisme_v1.py QUESTION_SOURCE SORTIE"""
import hashlib, sys
src, sortie = sys.argv[1:3]
ATTENDU = "b742056195097bf4cf383b31b6ecfe99effb0ca1cb5ddfed6701af17333279b9"
octets = open(src, "rb").read()
h = hashlib.sha256(octets).hexdigest()
if h != ATTENDU:
    sys.exit(f"question source : empreinte {h} au lieu de {ATTENDU} ; rien n'est écrit")
texte = octets.decode("utf-8")
DEBUT, FIN = "\n## La demande, telle que Lazar l'a écrite", "\n## Lecture prévue de la sortie\n"
assert texte.count(DEBUT) == 1 and texte.count(FIN) == 1 and texte.index(DEBUT) < texte.index(FIN)
servie = texte[texte.index(DEBUT) + 1:texte.index(FIN)].rstrip("\n") + "\n"
titres = [l for l in servie.splitlines() if l.startswith("## ")]
assert titres == ["## La demande, telle que Lazar l'a écrite (texte exact, fautes de frappe d'origine)",
                  "## Ce qu'on attend de chaque espèce", "## Règles d'intégrité (reprises dans la consigne)"], titres
open(sortie, "x", encoding="utf-8").write(servie)
print(len(titres), "sections,", len(servie.encode()), "octets")
