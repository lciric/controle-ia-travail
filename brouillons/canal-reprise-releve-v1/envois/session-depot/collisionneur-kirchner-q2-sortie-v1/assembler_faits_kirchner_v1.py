"""Assemble les faits du tour du collisionneur v9 sur la question 2 du mentor Kirchner (spécification de conv-audit
`specification-kirchner-q2-v1.md`, 934f5dcb…, § 2). Copie adaptée de assembler_faits_brainstorm_v1.py (branche 9edaeb26) :
même forme de blocs (« DÉBUT FICHIER … sha256=… » / « FIN FICHIER … »), même écriture en mode « x » (on n'écrase jamais) ;
seuls changent les sources (deux pièces servies, empreintes exigées avant toute écriture), l'en-tête et l'ordre (Kirchner, puis
nos résultats). Le contenu de chaque pièce est recopié à l'octet entre ses deux balises.
Usage : python3 -I assembler_faits_kirchner_v1.py DOSSIER_PIECES SORTIE"""
import hashlib, os, sys
pieces_dir, sortie = sys.argv[1:3]
PIECES = (("piece-kirchner-v2.md", "6e7fb1c56cb292aa97667f11093959f775f940b06dc85d8038e728813e4203f5"),
          ("piece-nos-resultats-v1.md", "d6fa8011d9b5680d4ec58b262b6440e0e61e9c9987f0ac79a51cb5bca7b27e3c"))
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
