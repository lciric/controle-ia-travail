"""DOUBLURE D'ESSAI du module `requete_na_v3` (lot 3 v3), déclarée comme telle — ce n'est PAS le module du lot 3.

Seuls les noms que lisent `lecteur_fiches_na_v1`, `contrat_fiche_na_v1` et `portier_na_v1` dans les chemins que jouent les
essais du lot 5 v3. L'assemblage de la requête « fiche » du portier est réduit à ce que le portier vérifie : une composition
dont l'élément « fiche servie » porte l'empreinte des octets de la fiche (`json.dumps(contenu, ensure_ascii=False,
indent=1)`, forme que le portier v1 déclare, mot 8 de 07:46Z) ; aucun texte de requête n'est assemblé. L'ordre des douze
champs est celui de la fiche factice des aides du lot 5 v1, non celui, non lu, du lot 3. Les essais du lot 5 v3 doivent être
rejoués sur une copie où le lot 3 v3 est posé.
"""

import dataclasses
import hashlib
import json

CHAMPS_FICHE = ("case", "ce_que_le_moniteur_suppose", "menace_du_programme", "etage_de_lecture", "idee",
                "mesurable_sur_monde_plante", "ce_qui_la_refuterait", "issue_contraire", "voisin_le_plus_proche_connu",
                "ecart_au_voisin", "filiation", "piece_produite")
INDENTATION_JSON = 1
REGISTRE_SERVI = "registre servi"


@dataclasses.dataclass(frozen=True)
class Piece:
    nom: str
    octets: bytes
    sha256: str


@dataclasses.dataclass(frozen=True)
class CaseServie:
    triplet: tuple
    identifiant: str
    ligne: str


@dataclasses.dataclass(frozen=True)
class Element:
    nom: str
    sha256: str


@dataclasses.dataclass(frozen=True)
class RequeteDoublure:
    sorte: str
    identifiant_case: str
    generation: object
    composition: tuple


def assembler_portier_fiche(consigne, contenu, identifiant_case, generation):
    octets = json.dumps(contenu, ensure_ascii=False, indent=INDENTATION_JSON).encode("utf-8")
    return RequeteDoublure("fiche", identifiant_case, generation,
                           (Element("consigne", consigne.sha256), Element("fiche servie", hashlib.sha256(octets).hexdigest())))


def assembler_portier_reponse_sans_fiche(consigne, texte, identifiant_case, generation):
    return RequeteDoublure("réponse sans fiche", identifiant_case, generation, (Element("consigne", consigne.sha256),))
