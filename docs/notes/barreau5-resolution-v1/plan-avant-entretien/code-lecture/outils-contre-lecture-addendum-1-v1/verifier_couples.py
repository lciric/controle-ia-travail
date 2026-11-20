"""Verifie les couples (fichier, avant, apres) d'une contre-lecture, par programme.

Usage : verifier_couples.py CONTRE_LECTURE RACINE_DEPOT SORTIE
  CONTRE_LECTURE : la piece qui porte les couples. Chaque couple y est ecrit ainsi :
      - Fichier : `chemin/relatif/au/depot`
      - Avant :
      ````text
      ...
      ````
      - Après :
      ````text
      ...
      ````
  SORTIE : chemin ou ecrire le fichier vise apres application de tous les couples
           (une copie de travail ; le fichier du depot n'est jamais touche).
Pour chaque couple : compte de « avant » dans le fichier d'origine et dans le texte
en cours d'application (les deux doivent valoir 1), puis compte de « apres » dans le
resultat final. Sortie non nulle si une regle manque. Un seul fichier vise par appel.
Outil du contre-lecteur de l'addendum 1 (barreau 5).
"""
import hashlib
import os
import re
import sys

MOTIF = re.compile(
    r"- Fichier : `(?P<fichier>[^`]+)`\n"
    r"- Avant :\n````text\n(?P<avant>.*?)\n````\n"
    r"- Après :\n````text\n(?P<apres>.*?)\n````",
    re.S,
)


def main() -> int:
    piece, racine, sortie = sys.argv[1], sys.argv[2], sys.argv[3]
    with open(piece, encoding="utf-8") as f:
        texte_piece = f.read()
    couples = [m.groupdict() for m in MOTIF.finditer(texte_piece)]
    if not couples:
        print("aucun couple trouve : refus")
        return 2
    fichiers = sorted({c["fichier"] for c in couples})
    if len(fichiers) != 1:
        print(f"plusieurs fichiers vises {fichiers} : un seul par appel")
        return 2
    chemin = os.path.join(racine, fichiers[0])
    with open(chemin, encoding="utf-8") as f:
        origine = f.read()
    print(f"fichier vise : {fichiers[0]}")
    print(f"sha256 d'origine : {hashlib.sha256(origine.encode('utf-8')).hexdigest()}")
    print(f"couples trouves : {len(couples)}")
    ok = True
    courant = origine
    for i, c in enumerate(couples, 1):
        n_origine = origine.count(c["avant"])
        n_courant = courant.count(c["avant"])
        bon = n_origine == 1 and n_courant == 1
        ok = ok and bon
        print(f"couple {i:2d} : avant dans l'origine {n_origine} ; dans le texte en cours {n_courant} ; "
              f"{'bon' if bon else 'MANQUE'}")
        if n_courant == 1:
            courant = courant.replace(c["avant"], c["apres"], 1)
    for i, c in enumerate(couples, 1):
        n = courant.count(c["apres"])
        bon = n >= 1
        ok = ok and bon
        print(f"couple {i:2d} : apres dans le resultat {n} ; {'bon' if bon else 'MANQUE'}")
    with open(sortie, "w", encoding="utf-8") as f:
        f.write(courant)
    print(f"sha256 du resultat (copie de travail) : {hashlib.sha256(courant.encode('utf-8')).hexdigest()}")
    print("tous les couples s'appliquent" if ok else "AU MOINS UN COUPLE NE S'APPLIQUE PAS")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
