"""Assemble les faits du tour du collisionneur v9 sur la conception de l'organisme d'idéation (spécification de conv-audit
`specification-collisionneur-conception-organisme-v1.md`, 7de4cb16…, § 2). Copie adaptée de assembler_faits_kirchner_v1.py
(branche donnees/collisionneur-v9-kirchner-q2-v1, 16ec2e5a) : mêmes blocs (« DÉBUT FICHIER … sha256=… » / « FIN FICHIER … »),
même écriture en mode « x » ; seuls changent les cinq pièces, leur ordre (README, état réel, Kirchner, lecture de 2608.28945,
nos résultats) et les noms de blocs (provenance). Chaque pièce est recopiée à l'octet entre ses deux balises ; empreintes exigées
avant toute écriture.
Usage : python3 -I assembler_faits_conception_organisme_v1.py DOSSIER_PIECES SORTIE
(DOSSIER_PIECES contient README.md = `git show 4848ad9:README.md` du dépôt public ideation-organism, et les quatre pièces du canal.)"""
import hashlib, os, sys
pieces_dir, sortie = sys.argv[1:3]
PIECES = (("README.md", "ideation-organism@4848ad9:README.md",
           "bdd6516f18ec0cf44ba7fa173df519d8f88b3ee89ab8892454822babbe05b1df"),
          ("piece-etat-reel-organisme-v1.md", "piece-etat-reel-organisme-v1.md",
           "09a4a028388fb33e314488a26ee71bb10dca2a99ec354c128919dd9908ba9c07"),
          ("piece-kirchner-v2.md", "piece-kirchner-v2.md",
           "6e7fb1c56cb292aa97667f11093959f775f940b06dc85d8038e728813e4203f5"),
          ("piece-lecture-2608-28945-parties-factuelles-v1.md", "piece-lecture-2608-28945-parties-factuelles-v1.md",
           "4ab6c9d780ac3ae9f44b70ff97e785c77d973d178a7aec3d027f8e06e584026b"),
          ("piece-nos-resultats-v1.md", "piece-nos-resultats-v1.md",
           "d6fa8011d9b5680d4ec58b262b6440e0e61e9c9987f0ac79a51cb5bca7b27e3c"))
blocs = []
for fichier, nom, attendu in PIECES:
    octets = open(os.path.join(pieces_dir, fichier), "rb").read()
    h = hashlib.sha256(octets).hexdigest()
    if h != attendu:
        sys.exit(f"{fichier} : empreinte {h} au lieu de {attendu} ; rien n'est écrit")
    blocs.append(f"<<<DÉBUT FICHIER {nom} sha256={h}>>>\n{octets.decode('utf-8')}\n<<<FIN FICHIER {nom}>>>")
entete = "pas de web, pas d'exécution de code ; nouveauté : non cherchée\n\n"
open(sortie, "x", encoding="utf-8").write(entete + "\n\n".join(blocs) + "\n")
print(len(blocs), "pièces")
