"""Aides des essais des lots 1 et 2 du véhicule NA-1, v4 (lisent `tirage_na_v4` et `garde_motifs_na_v4`) : données factices
seules, plus les données des ignorables d'Unicode 15.1.0 (`pole/ignorables-unicode-15.1.0-na-v1.json`, tirées par
programme du fichier versé par la mère), qui ne sont pas des données de course, et la liste réelle des noms refusés
(`liste-reelle/motifs-noms-refuses-reels-v1.txt`, lue à son empreinte ; aucun nom n'est écrit dans ce fichier ni dans les
essais : ils sont lus dans la liste au moment où l'essai tourne).

- Un gabarit factice, de la forme du gabarit servi (une table de légende à trois axes, 6, 5 et 4 valeurs, un emplacement),
  aux valeurs inertes ; il n'est pas le gabarit servi et n'en a pas l'empreinte.
- Une racine factice : les essais ne jouent jamais le tirage réel (il est joué deux fois par la session de l'organisme,
  puis scellé par la mère : conception v4, § 4). La racine écrite n'est lue que pour être comparée à la lettre.
- La liste des motifs d'essai (`liste-motifs-essai-na-v1.json`), deux familles, motifs inertes, à son empreinte.

Lancé comme programme (`python -B aides_na_v4.py SORTIE`), il écrit le tirage factice, pour l'essai « rejoué dans deux
processus ».
"""

import hashlib
import os
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
RACINE_ORCHESTRATEUR = os.path.dirname(ICI)
if RACINE_ORCHESTRATEUR not in sys.path:
    sys.path.insert(0, RACINE_ORCHESTRATEUR)

from pole import garde_motifs_na_v4 as gm  # noqa: E402
from pole import tirage_na_v4 as tn  # noqa: E402

CHEMIN_LISTE_ESSAI = os.path.join(ICI, "liste-motifs-essai-na-v1.json")
EMPREINTE_LISTE_ESSAI = "41a50329f67c41d073115a75ae64981fd59a46b4663c269f42a32b4055c0508b"
CHEMIN_DONNEES = os.path.join(RACINE_ORCHESTRATEUR, "pole", "ignorables-unicode-15.1.0-na-v1.json")
EMPREINTE_DONNEES = "8e15ad688fbb298ade214fe19986e103e4302f0e67d169b7201f730e416699f7"
EMPREINTE_SOURCE_UNICODE = "f55d0db69123431a7317868725b1fcbf1eab6b265d756d1bd7f0f6d9f9ee108b"
COMMIT_SOURCE_UNICODE = "bed42d477a4894f56f280ce188d66bec1ba37503"
CHEMIN_DEPOT_SOURCE = "docs/sources/unicode/15.1.0/DerivedCoreProperties.txt"
INTERPRETE_COURSE = "/usr/local/bin/python3"
# Liste réelle des noms refusés (branche `verse/motifs-refuses-seuil-moniteurs-v1`, commit `d73f7ce3…`), copiée à l'octet.
CHEMIN_LISTE_REELLE = os.path.join(ICI, "liste-reelle", "motifs-noms-refuses-reels-v1.txt")
EMPREINTE_LISTE_REELLE = "583d428a89cbffe9d7167d9bfd4d4e0290a283ef2fbc825d4016afb6502c2813"
LIGNES_ATTENDUES_LISTE_REELLE = 34


def lire_liste_reelle():
    """Rend les expressions de la liste réelle (lignes de la forme `\\bnom\\b`), après vérification de l'empreinte ;
    les lignes vides et celles qui commencent par « # » sont des commentaires. Échoue (exception), jamais ne saute."""
    with open(CHEMIN_LISTE_REELLE, "rb") as f:
        octets = f.read()
    if hashlib.sha256(octets).hexdigest() != EMPREINTE_LISTE_REELLE:
        raise ValueError("empreinte de la liste réelle différente de celle qui est écrite")
    lignes = [l.strip() for l in octets.decode("utf-8").split("\n")]
    return [l for l in lignes if l and not l.startswith("#")]


def donnees():
    return gm.charger_donnees_ignorables(CHEMIN_DONNEES, EMPREINTE_DONNEES)


def normaliseur():
    return gm.Normaliseur(donnees())


def lire_liste(octets, sha):
    return gm.lire_liste_motifs(octets, sha, normaliseur())

RACINE_FACTICE = int.from_bytes(hashlib.sha256(b"racine factice du vehicule na, essais seulement").digest()[:16], "big")
ENTROPIE_ECHANTILLONS = int.from_bytes(hashlib.sha256(b"echantillons factices du vehicule na").digest()[:16], "big")

GABARIT_FACTICE = (
    "> Texte factice d'essai, inerte : il ne pose aucune question.\n"
    ">\n"
    "> Une case t'est servie ; rien d'autre n'est dit ici.\n"
    "\n"
    "{{CASE}}\n"
    "\n"
    "| axe | valeurs |\n"
    "|---|---|\n"
    "| ce que le moniteur suppose | trait factice un ; trait factice deux ; trait factice trois ; trait factice quatre ;"
    " trait factice cinq ; autre, à nommer |\n"
    "| menace du programme | sabotage factice ; menace factice deux ; menace factice trois (avec parenthèse) ;"
    " menace factice quatre, avec virgule ; menace factice cinq |\n"
    "| étage de lecture | étage factice un ; étage factice deux ; étage factice trois (a, b) ; étage factice quatre |\n"
    "\n"
    "**Champs factices** : `case` ; `idee`.\n"
).encode("utf-8")
EMPREINTE_GABARIT_FACTICE = hashlib.sha256(GABARIT_FACTICE).hexdigest()

SYNTHESE_FACTICE = ("Synthèse factice, inerte, pour les essais.\n" * 40).encode("utf-8")


def liste_essai():
    return gm.charger_liste_motifs(CHEMIN_LISTE_ESSAI, EMPREINTE_LISTE_ESSAI, normaliseur())


def garde_essai():
    return gm.GardeMotifs(liste_essai())


def tirage_factice(gabarit=GABARIT_FACTICE, empreinte=None):
    return tn.TirageNA(gabarit, empreinte_gabarit=empreinte or hashlib.sha256(gabarit).hexdigest(),
                       racine=RACINE_FACTICE, racine_attendue=RACINE_FACTICE)


def sortie_factice():
    return tirage_factice().jouer(garde_essai())


def requete_factice(ligne_de_case):
    """Une requête assemblée factice : le gabarit factice rempli d'une ligne de case, une ligne vide, la synthèse."""
    rempli = GABARIT_FACTICE.replace(b"{{CASE}}", ligne_de_case.encode("utf-8"))
    return rempli + b"\n" + SYNTHESE_FACTICE


def liste_octets(familles):
    """Une liste au format `liste-motifs-na-v1` en octets, pour les artefacts ; rend (octets, empreinte)."""
    import json
    octets = json.dumps({"format": gm.FORMAT_LISTE, "familles": familles}, ensure_ascii=False).encode("utf-8")
    return octets, hashlib.sha256(octets).hexdigest()


def familles_saines():
    return [
        {"nom": "identité et dépôt", "motifs": [
            {"rang": 1, "type": "litteral", "motif": "personne factice alpha", "temoin_positif": "personne factice alpha"}]},
        {"nom": "composition et tenue", "motifs": [
            {"rang": 1, "type": "litteral", "motif": "graine factice", "temoin_positif": "une graine factice"}]},
    ]


if __name__ == "__main__":
    with open(sys.argv[1], "xb") as f:
        f.write(tn.serialiser(sortie_factice()))
