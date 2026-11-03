"""Assemble les faits du tour du collisionneur v9 sur la question 1 de Lujain Ibrahim (conv-audit n° 416, e5d2f7af… ; empreinte de la
pièce du mentor au n° 417). Copie adaptée de assembler_faits_kirchner_v1.py (branche donnees/collisionneur-v9-kirchner-q2-v1,
16ec2e5a) : mêmes blocs (« DÉBUT FICHIER … sha256=… » / « FIN FICHIER … »), même en-tête, même écriture en mode « x » ; seule change
les premières pièces (piece-ibrahim-v1.md puis piece-sycophancie-publique-v1.md, au lieu de la pièce Kirchner v2). Chaque pièce est recopiée à l'octet entre ses deux balises ;
empreintes exigées avant toute écriture.
Usage : python3 -I assembler_faits_ibrahim_q1_v1.py DOSSIER_PIECES SORTIE"""
import hashlib, os, sys
pieces_dir, sortie = sys.argv[1:3]
PIECES = (("piece-ibrahim-v1.md", "4e3851e3816fc3afaa573693f8f3d0aa2b9fc6c0e726ae54bab8cd4a248d6149"),
          ("piece-sycophancie-publique-v1.md", "9e424a025280908baf5e2eec65f285a746f92ce14991cdc5d7d80cb5978716b8"),
          ("piece-nos-resultats-v1.md", "d6fa8011d9b5680d4ec58b262b6440e0e61e9c9987f0ac79a51cb5bca7b27e3c"))
blocs = []
for nom, attendu in PIECES:
    octets = open(os.path.join(pieces_dir, nom), "rb").read()
    h = hashlib.sha256(octets).hexdigest()
    if h != attendu:
        sys.exit(f"{nom} : empreinte {h} au lieu de {attendu} ; rien n'est écrit")
    blocs.append(f"<<<DÉBUT FICHIER {nom} sha256={h}>>>\n{octets.decode('utf-8')}\n<<<FIN FICHIER {nom}>>>")
entete = "pas de web, pas d'exécution de code ; nouveauté : non cherchée\n\n"
open(sortie, "x", encoding="utf-8").write(entete + "\n\n".join(blocs) + "\n")
print(len(blocs), "pièces")
