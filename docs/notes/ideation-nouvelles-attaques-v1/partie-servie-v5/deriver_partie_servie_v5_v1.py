"""Dérivation de la partie servie de la question v5 (course « nouvelles attaques ») — v1.

Lit la question v5, vérifie son empreinte, extrait des zones données par leurs
lignes, les met bout à bout dans l'ordre, insère l'unique emplacement de case,
écrit le gabarit et le journal. Aucune autre opération.

Seul écart à « sans transformation » : la zone de la table des axes perd sa
colonne « source » (chaque ligne est gardée jusqu'à sa troisième barre
verticale comprise, puis le saut de ligne). À trancher par la mère.

Bibliothèque standard seule. Aucun argument. Signé : dériveur neuf, modèle F.
"""

import hashlib
import json
import platform
import sys

SOURCE = (
    "/tmp/claude-0/-home-user-controle-ia-travail/"
    "16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/"
    "derivation-partie-servie-v5-sources/question-v5.md"
)
SOURCE_ORIGINE = (
    "origin/main:prereg/ideation-nouvelles-attaques-v1/"
    "question-course-nouvelles-attaques-v5.md"
)
SOURCE_SHA256 = "eaf5db8a558547aa8f5df45008a34eebf4cb7a163e12ca400176401de6f5ce0f"
SOURCE_LIGNES = 74

DOSSIER = (
    "/tmp/claude-0/-home-user-controle-ia-travail/"
    "16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/"
    "derivation-partie-servie-v5/"
)
SORTIE = DOSSIER + "partie-servie-question-v5-v1.md"
JOURNAL = DOSSIER + "journal-derivation-partie-servie-v5-v1.json"

COMMANDE = (
    "env -C /home/user/controle-ia-travail python3 -I -B "
    + DOSSIER
    + "deriver_partie_servie_v5_v1.py"
)

EMPLACEMENT = b"{{CASE}}\n"
MARQUES_INTERDITES_DANS_LA_SOURCE = (b"{{", b"}}", b"{", b"}")

SANS = "aucune"
RETRAIT = "retrait de la colonne « source »"

# Suite ordonnée des pièces du gabarit. Lignes de la source, numérotées à
# partir de 1, bornes comprises.
PIECES = (
    {
        "nature": "zone",
        "nom": "question servie (§ 4, citation entière) et la ligne vide qui la suit",
        "debut": 42,
        "fin": 51,
        "operation": SANS,
    },
    {"nature": "emplacement", "nom": "emplacement de case"},
    {
        "nature": "zone",
        "nom": "ligne vide avant la légende des axes",
        "debut": 55,
        "fin": 55,
        "operation": SANS,
    },
    {
        "nature": "zone",
        "nom": "légende des axes (§ 5, table : noms des trois axes et leurs valeurs)",
        "debut": 56,
        "fin": 60,
        "operation": RETRAIT,
    },
    {
        "nature": "zone",
        "nom": "ligne vide après la légende des axes",
        "debut": 61,
        "fin": 61,
        "operation": SANS,
    },
    {
        "nature": "zone",
        "nom": "champs d'une fiche (§ 5, contrat de sortie, deux alinéas)",
        "debut": 64,
        "fin": 66,
        "operation": SANS,
    },
)

BARRE = b"|"
COLONNE_RETIREE_EN_TETE = b" source |\n"


def empreinte(octets):
    return hashlib.sha256(octets).hexdigest()


def arret(message):
    sys.stderr.write("ARRÊT : " + message + "\n")
    sys.exit(1)


def retirer_colonne_source(lignes):
    """Garde chaque ligne jusqu'à sa troisième barre verticale comprise."""
    sorties = []
    for rang, ligne in enumerate(lignes):
        if ligne.count(BARRE) != 4 or not ligne.endswith(b"|\n"):
            arret("ligne de table inattendue dans la zone de la légende")
        position = -1
        for _ in range(3):
            position = ligne.index(BARRE, position + 1)
        garde = ligne[: position + 1] + b"\n"
        retire = ligne[position + 1 :]
        if rang == 0 and retire != COLONNE_RETIREE_EN_TETE:
            arret("la colonne retirée ne s'appelle pas « source »")
        sorties.append(garde)
    return sorties


def main():
    with open(SOURCE, "rb") as flux:
        source = flux.read()
    if empreinte(source) != SOURCE_SHA256:
        arret("empreinte de la source différente de l'empreinte attendue")
    if not source.endswith(b"\n"):
        arret("la source ne finit pas par un saut de ligne")
    lignes = [morceau + b"\n" for morceau in source[:-1].split(b"\n")]
    if len(lignes) != SOURCE_LIGNES:
        arret("nombre de lignes de la source inattendu")
    for marque in MARQUES_INTERDITES_DANS_LA_SOURCE:
        if marque in source:
            arret("la source porte une accolade : l'emplacement ne serait pas unique")

    morceaux = []
    journal_pieces = []
    for piece in PIECES:
        if piece["nature"] == "emplacement":
            morceaux.append(EMPLACEMENT)
            journal_pieces.append(
                {
                    "nature": "emplacement",
                    "nom": piece["nom"],
                    "octets_inseres": EMPLACEMENT.decode("ascii"),
                    "taille_octets": len(EMPLACEMENT),
                    "sha256": empreinte(EMPLACEMENT),
                }
            )
            continue
        extrait = lignes[piece["debut"] - 1 : piece["fin"]]
        brut = b"".join(extrait)
        if piece["operation"] == RETRAIT:
            servi = b"".join(retirer_colonne_source(extrait))
        elif piece["operation"] == SANS:
            servi = brut
        else:
            arret("opération inconnue")
        morceaux.append(servi)
        journal_pieces.append(
            {
                "nature": "zone",
                "nom": piece["nom"],
                "ligne_debut": piece["debut"],
                "ligne_fin": piece["fin"],
                "operation": piece["operation"],
                "taille_octets_extraits": len(brut),
                "sha256_extrait": empreinte(brut),
                "taille_octets_servis": len(servi),
                "sha256_servi": empreinte(servi),
                "egal_a_l_octet": servi == brut,
            }
        )

    sortie = b"".join(morceaux)
    if sortie.count(b"{{CASE}}") != 1 or sortie.count(b"{") != 2 or sortie.count(b"}") != 2:
        arret("l'emplacement de case n'est pas unique dans le gabarit")
    if sortie.count(EMPLACEMENT) != 1 or (b"\n" + EMPLACEMENT) not in sortie:
        arret("l'emplacement de case n'est pas sur une ligne propre")

    with open(SORTIE, "wb") as flux:
        flux.write(sortie)

    journal = {
        "piece": "journal de dérivation de la partie servie de la question v5 — v1",
        "signe": "dériveur neuf, modèle F",
        "source": {
            "origine": SOURCE_ORIGINE,
            "copie_lue": SOURCE,
            "sha256": SOURCE_SHA256,
            "taille_octets": len(source),
            "lignes": len(lignes),
        },
        "pieces_dans_l_ordre": journal_pieces,
        "emplacement_de_case": {
            "octets": "{{CASE}}",
            "forme": "une ligne propre, entre la question servie et la légende des axes",
            "ligne_du_gabarit": sortie[: sortie.index(EMPLACEMENT)].count(b"\n") + 1,
            "occurrences_dans_le_gabarit": sortie.count(b"{{CASE}}"),
            "accolades_dans_la_source": 0,
        },
        "ecart_a_sans_transformation": {
            "zone": "lignes 56 à 60",
            "operation": RETRAIT,
            "regle": (
                "chaque ligne de la zone est gardée jusqu'à sa troisième barre "
                "verticale comprise, puis le saut de ligne ; arrêt si une ligne "
                "n'a pas quatre barres ou si la partie retirée de la première "
                "ligne n'est pas « source »"
            ),
            "statut": "seul écart, à trancher par la mère",
        },
        "sortie": {
            "chemin": SORTIE,
            "sha256": empreinte(sortie),
            "taille_octets": len(sortie),
            "lignes": sortie.count(b"\n"),
        },
        "commande": COMMANDE,
        "python": platform.python_version(),
    }
    texte = json.dumps(journal, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    with open(JOURNAL, "wb") as flux:
        flux.write(texte.encode("utf-8"))


if __name__ == "__main__":
    main()
