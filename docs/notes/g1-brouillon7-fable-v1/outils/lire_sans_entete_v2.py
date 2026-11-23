#!/usr/bin/env python3
"""Lecture d'un brouillon de décision sans son en-tête, masquage phrase par phrase (v2).

Usage : python3 lire_sans_entete_v2.py FICHIER [--journal JOURNAL] [--compter]

Ce qui change de la v1 (gardée telle quelle, R12) : le masquage se fait phrase par phrase et non
ligne par ligne, pour ne pas cacher un énoncé de critère qui partage sa ligne avec une mention d'issue.

- L'en-tête (tout ce qui précède la première ligne de section « ## ») n'est jamais affiché.
- Une phrase du corps est masquée si :
    (1) elle porte un mot propre au premier cycle (premier cycle, barreau 6, nom ou empreinte du verdict)
        et un mot d'issue de la liste large ; ou
    (2) elle porte « accumulation » et un mot d'issue de la liste forte (verdict, issue, échec, nul,
        négatif, positif, « n'a pas », « ne dépasse », réfuté, artefact…).
- Chaque appel écrit une ligne au journal : heure (UTC), fichier, empreinte, lignes d'en-tête écartées,
  nombre de phrases masquées et leurs lignes, mode.
- Aucun repli silencieux (R5) : sans ligne « ## », le programme s'arrête sans rien afficher.
"""
import datetime
import hashlib
import json
import re
import sys

ISSUE_LARGE = re.compile(
    r"verdict|issue|résultat|resultat|échou|echou|échec|echec|\bnul\b|\bnuls\b|\bnulle\b|négatif|negatif|"
    r"positif|\baire|rappel|n'a pas|n’a pas|ne dépasse|ne depasse|au-dessus|au-dessous|sous le plancher|"
    r"\btenu\b|non tenu|réfut|refut|artefact|montr|trouv|conclu|constat|observ",
    re.IGNORECASE,
)
ISSUE_FORTE = re.compile(
    r"verdict|issue|échou|echou|échec|echec|\bnul\b|\bnuls\b|\bnulle\b|négatif|negatif|positif|n'a pas|n’a pas|"
    r"ne dépasse|ne depasse|au-dessous|sous le plancher|non tenu|réfut|refut|artefact|conclu|constat",
    re.IGNORECASE,
)
CYCLE_PROPRE = re.compile(
    r"premier cycle|cycle 1\b|barreau 6|accb6|verdict-accb6|c78e35b5|sixième barreau|sixieme barreau",
    re.IGNORECASE,
)
ACCUMULATION = re.compile(r"accumulation", re.IGNORECASE)
COUPE = re.compile(r"(?<=[.;:!?])\s+")


def masquer(phrase):
    if CYCLE_PROPRE.search(phrase) and ISSUE_LARGE.search(phrase):
        return True
    if ACCUMULATION.search(phrase) and ISSUE_FORTE.search(phrase):
        return True
    return False


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
    lignes_touchees = []
    n_phrases = 0
    sortie = []
    for i in range(debut, len(lignes)):
        phrases = COUPE.split(lignes[i])
        rendu = []
        touche = False
        for p in phrases:
            if masquer(p):
                rendu.append("[phrase masquée]")
                n_phrases += 1
                touche = True
            else:
                rendu.append(p)
        if touche:
            lignes_touchees.append(i + 1)
        sortie.append(f"{i + 1}: " + " ".join(rendu))
    entree = {
        "heure_utc": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "outil": "lire_sans_entete_v2.py",
        "fichier": chemin,
        "sha256": empreinte,
        "lignes_total": len(lignes),
        "lignes_entete_ecartees": debut,
        "phrases_masquees": n_phrases,
        "lignes_touchees": lignes_touchees,
        "mode": "comptage seul" if compter else "affichage sans en-tête",
    }
    if journal:
        with open(journal, "a", encoding="utf-8") as f:
            f.write(json.dumps(entree, ensure_ascii=False) + "\n")
    if compter:
        print(json.dumps(entree, ensure_ascii=False))
        return 0
    print(f"[programme v2] {chemin} sha256 {empreinte[:16]}… : {debut} ligne(s) d'en-tête écartée(s), "
          f"{n_phrases} phrase(s) masquée(s) sur {len(lignes_touchees)} ligne(s)")
    print("\n".join(sortie))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
