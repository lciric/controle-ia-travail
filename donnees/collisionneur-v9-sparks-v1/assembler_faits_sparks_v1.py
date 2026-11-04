"""Assemble les faits du tour du collisionneur v9 sur la question Sparks (billet « Sparks of Weight-Space Programming » du
2 novembre 2026 ; question `question-collisionneur-sparks-v1.md`, 69d05369…). Copie adaptée de assembler_faits_kirchner_v1.py
(branche donnees/collisionneur-v9-kirchner-q2-v1, 16ec2e5a) : même forme de blocs (« DÉBUT FICHIER … sha256=… » / « FIN FICHIER … »),
même écriture en mode « x » (on n'écrase jamais), mêmes empreintes exigées avant toute écriture, même en-tête ; seuls changent les
sources (trois pièces servies) et l'ordre (lecture factuelle, billet, nos résultats). Le contenu de chaque pièce est recopié à
l'octet entre ses deux balises.
Usage : python3 -I assembler_faits_sparks_v1.py DOSSIER_PIECES SORTIE"""
import hashlib, os, sys
pieces_dir, sortie = sys.argv[1:3]
PIECES = (("piece-3-lecture-factuelle.md", "fff05896def645d0ff1a22b86ddfaaeb3ed2e9e3ccba9a5dc47e1d69cdaaac55"),
          ("piece-1-billet.txt", "49b2db7e7744a7263a887e06ff507953a24b8915ba314840266156094f851f2d"),
          ("piece-2-nos-resultats.md", "d6fa8011d9b5680d4ec58b262b6440e0e61e9c9987f0ac79a51cb5bca7b27e3c"))
blocs = []
for nom, attendu in PIECES:
    octets = open(os.path.join(pieces_dir, nom), "rb").read()
    h = hashlib.sha256(octets).hexdigest()
    if h != attendu:
        sys.exit(f"{nom} : empreinte {h} au lieu de {attendu} ; rien n'est écrit")
    texte = octets.decode("utf-8")
    blocs.append(f"<<<DÉBUT FICHIER {nom} sha256={h}>>>\n{texte}\n<<<FIN FICHIER {nom}>>>")
entete = "pas de web, pas d'exécution de code ; nouveauté : non cherchée\n\n"
open(sortie, "x", encoding="utf-8").write(entete + "\n\n".join(blocs) + "\n")
print(len(blocs), "pièces")
