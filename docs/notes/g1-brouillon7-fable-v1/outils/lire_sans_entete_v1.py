#!/usr/bin/env python3
"""Lecture d'un brouillon de décision sans son en-tête, pour un rédacteur tenu aveugle aux issues.

Usage : python3 lire_sans_entete_v1.py FICHIER [--journal JOURNAL] [--compter]

- L'en-tête (tout ce qui précède la première ligne de section « ## ») n'est jamais affiché.
- Dans le corps, toute ligne qui porte un mot d'issue (verdict, issue, résultat, aire, rappel mesuré…)
  ET un mot du premier cycle de l'accumulation des scores sur l'épisode est remplacée par une mention
  de masquage ; son contenu n'est pas affiché.
- Chaque appel écrit une ligne au journal : heure (UTC), fichier, empreinte, lignes d'en-tête écartées,
  lignes masquées (numéros seuls), mode.
- Aucun repli silencieux (R5) : sans ligne « ## », le programme s'arrête sans rien afficher.
"""
import datetime
import hashlib
import json
import re
import sys

MOTS_ISSUE = re.compile(
    r"verdict|issue|résultat|resultat|échou|echou|nul\b|négatif|negatif|positif|aire|rappel|"
    r"n'a pas|ne dépasse|ne depasse|au-dessus|au-dessous|sous le plancher|tenu\b|non tenu|réfut|refut",
    re.IGNORECASE,
)
MOTS_CYCLE = re.compile(
    r"premier cycle|cycle 1\b|barreau 6|accumulation|accb6|verdict-accb6|c78e35b5",
    re.IGNORECASE,
)


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        return 2
    chemin = argv[1]
    journal = None
    compter = "--compter" in argv
    if "--journal" in argv:
        journal = argv[argv.index("--journal") + 1]
    octets = open(chemin, "rb").read()
    empreinte = hashlib.sha256(octets).hexdigest()
    lignes = octets.decode("utf-8").splitlines()
    debut = None
    for i, ligne in enumerate(lignes):
        if ligne.startswith("## "):
            debut = i
            break
    if debut is None:
        print("ARRÊT : aucune ligne de section « ## » ; rien n'est affiché.")
        return 3
    masquees = []
    sortie = []
    for i in range(debut, len(lignes)):
        ligne = lignes[i]
        if MOTS_ISSUE.search(ligne) and MOTS_CYCLE.search(ligne):
            masquees.append(i + 1)
            sortie.append(f"{i + 1}: [ligne masquée par le programme : mot d'issue et mot du premier cycle]")
        else:
            sortie.append(f"{i + 1}: {ligne}")
    entree = {
        "heure_utc": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "fichier": chemin,
        "sha256": empreinte,
        "lignes_total": len(lignes),
        "lignes_entete_ecartees": debut,
        "lignes_masquees": masquees,
        "mode": "comptage seul" if compter else "affichage sans en-tête",
    }
    if journal:
        with open(journal, "a", encoding="utf-8") as f:
            f.write(json.dumps(entree, ensure_ascii=False) + "\n")
    if compter:
        print(json.dumps(entree, ensure_ascii=False))
        return 0
    print(f"[programme] {chemin} sha256 {empreinte[:16]}… : {debut} ligne(s) d'en-tête écartée(s), "
          f"{len(masquees)} ligne(s) masquée(s) dans le corps")
    print("\n".join(sortie))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
