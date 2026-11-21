"""Aides des essais du lot 3 du véhicule NA-1 (lisent `requete_na_v3` et `journal_na_v3`) : données factices seules.

v3 (remplace `aides_na_lot3_v2`, `757e2901…`, archivé sans modification) : des noms seuls changent, pour la v5 du lot 2.
Aucune liste réelle de motifs n'est lue ni copiée ici. La garde d'essai est celle de `aides_na_v4.garde_essai()`, qui la
construit ainsi :
`Normaliseur(charger_donnees_ignorables(chemin, empreinte))`, puis `charger_liste_motifs(chemin, empreinte, normaliseur)`,
puis `GardeMotifs(liste)`.

- Le gabarit factice, la synthèse factice, la racine factice et la liste de motifs d'essai sont ceux des lots 1 et 2
  (`aides_na_v4`) ; aucune pièce réelle n'est lue.
- Deux consignes factices (portier, juge), inertes, finies par des blancs pour éprouver la forme déclarée ; un registre
  servi factice, inerte ; une fiche factice aux douze champs, inerte.

Lancé comme programme (`python -B aides_na_lot3_v3.py SORTIE`), il écrit les octets de la requête d'un proposeur de la
génération 2 (première case de la génération, registre factice), pour l'essai « rejouée dans un autre processus ».
"""

import hashlib
import os
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
RACINE_ORCHESTRATEUR = os.path.dirname(ICI)
for _p in (ICI, RACINE_ORCHESTRATEUR):
    if _p not in sys.path:
        sys.path.insert(0, _p)

import aides_na_v4 as A  # noqa: E402
from pole import identifiants_na_v1 as ident  # noqa: E402
from pole import requete_na_v3 as rq  # noqa: E402

CONSIGNE_PORTIER_FACTICE = ("Consigne factice du portier, inerte : elle ne classe rien.\n"
                            "Deuxième ligne factice.\n\n  \n").encode("utf-8")
CONSIGNE_JUGE_FACTICE = "Consigne factice du juge, inerte : elle ne note rien.\n".encode("utf-8")
REGISTRE_FACTICE = ("ligne factice une du registre servi, inerte\n"
                    "ligne factice deux du registre servi, inerte\n").encode("utf-8")
TITRE_REGISTRE_FACTICE = "Titre factice de la section du registre"
OCTETS_JUGE_FACTICES = bytes([7, 0, 255, 128, 1])


def sha(octets):
    return hashlib.sha256(octets).hexdigest()


def gabarit():
    return rq.charger_gabarit(A.GABARIT_FACTICE, A.EMPREINTE_GABARIT_FACTICE)


def synthese(octets=A.SYNTHESE_FACTICE):
    return rq.charger_piece("synthèse servie", octets, sha(octets))


def consigne_portier(octets=CONSIGNE_PORTIER_FACTICE):
    return rq.charger_piece("consigne du portier", octets, sha(octets))


def consigne_juge(octets=CONSIGNE_JUGE_FACTICE):
    return rq.charger_piece("consigne des juges", octets, sha(octets))


def registre(octets=REGISTRE_FACTICE):
    return rq.charger_piece("registre servi", octets, sha(octets))


def cases():
    return rq.cases_du_tirage(A.sortie_factice(), gabarit())


def identifiant_juge():
    return ident.encoder_identifiant_juge(OCTETS_JUGE_FACTICES)


def contenu_fiche(case):
    """Une fiche factice, inerte, aux douze champs, dans l'ordre du contrat ; champs fermés égaux à ceux de la case."""
    g = gabarit()
    valeurs = [rq.tn.lire_legende(g.octets, g.sha256)["valeurs"][a][case.triplet[a]] for a in range(3)]
    return {
        "case": case.identifiant,
        "ce_que_le_moniteur_suppose": valeurs[0],
        "menace_du_programme": valeurs[1],
        "etage_de_lecture": valeurs[2],
        "idee": "Idée factice, inerte, sur deux lignes.\nSeconde ligne factice « entre guillemets ».",
        "mesurable_sur_monde_plante": "grandeur factice",
        "ce_qui_la_refuterait": "issue factice une",
        "issue_contraire": "issue factice deux",
        "voisin_le_plus_proche_connu": "aucun connu",
        "ecart_au_voisin": "écart factice",
        "filiation": "aucune",
        "piece_produite": "publique",
    }


def requete_generation_2():
    c = cases()["2"][0]
    return rq.assembler_proposeur(gabarit(), c, synthese(), 2, registre(), TITRE_REGISTRE_FACTICE)


if __name__ == "__main__":
    with open(sys.argv[1], "xb") as f:
        f.write(requete_generation_2().octets)
