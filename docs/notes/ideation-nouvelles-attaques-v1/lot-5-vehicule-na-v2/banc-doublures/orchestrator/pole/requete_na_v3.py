"""DOUBLURE D'ESSAI du module `requete_na_v3` (lot 3 v3), déclarée comme telle — ce n'est PAS le module du lot 3.

Seuls les noms que lisent `lecteur_fiches_na_v1`, `contrat_fiche_na_v1` et `portier_na_v1` à l'import et dans les chemins
que jouent les essais du lot 5 v2 (aucun assemblage de requête n'y est joué). L'ordre des douze champs est celui de la
fiche factice des aides du lot 5 v1, non celui, non lu, du lot 3. Les essais du lot 5 v2 doivent être rejoués sur une copie
où le lot 3 v3 est posé.
"""

import dataclasses

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


def assembler_portier_fiche(*a, **k):
    raise NotImplementedError("doublure : aucun assemblage n'est joué au banc du lot 5 v2")


def assembler_portier_reponse_sans_fiche(*a, **k):
    raise NotImplementedError("doublure : aucun assemblage n'est joué au banc du lot 5 v2")
