"""Arrêts nommés du bras A des organismes discrets, version 5 du code (préenregistrement
`prereg/T0.7-organismes-discrets-v-a-v2-brouillon20.md`, 6.9, 8.4 ; R5).

Deux sortes d'arrêt, toutes deux des `GardeArret` (jamais attrapées pour continuer, jamais de repli) :

- `ArretNomme` : une garde qui **refuse**, sous un nom que l'essai et le registre peuvent citer ;
- `EnAttenteDeDecision` : un cas que le texte **ne tranche pas encore**. La note du brouillon 20
  (`docs/notes/relance-organismes-discrets-v1/preenregistrement-v2-brouillon20-note-v1.md`, partie 5, seconde liste)
  nomme ce qui « attend un arbitrage et ne doit pas être codé avant » : dans chacun de ces cas, le code ne choisit
  pas — il s'arrête, et son message dit que le cas attend une décision. Régler le cas demandera une version nouvelle
  du code, après le mot de Lazar ou l'accord de la session principale ; aucune de ces gardes ne se lève par un réglage.

Les noms des cas en attente sont ici, en un seul endroit ; les essais (un cas sain et un artefact par garde) sont dans
`tests/test_analyse_bras_a_v5.py` et `tests/test_permutation_etiquettes_bras_a_v5.py`.
"""
from __future__ import annotations

from ..gardes import GardeArret

# --- Cas qui attendent une décision (note du brouillon 20, partie 3 ; partie 5, seconde liste) ----------------------------
# Points 1 et 2 : couple de tirages `null` sous le motif « plus de 1 % de permutations perdues ».
ATTENTE_TIRAGES_NULS_SOUS_PERMUTATIONS_PERDUES = "tirages nuls sous permutations perdues"
# Points 1 et 6 : couple de tirages `null` sous le motif « intervalle impossible faute de deux tâches ».
ATTENTE_TIRAGES_NULS_SOUS_INTERVALLE_IMPOSSIBLE = "tirages nuls sous intervalle impossible"
# Points 3 et 5 : `valeur_p_pour_la_famille` = 1 sous « plus de 1 % de tirages dégénérés » (contre GO-2026-11-19-70).
ATTENTE_FAMILLE_A_1_SOUS_TIRAGES_DEGENERES = "valeur p pour la famille égale à 1 sous tirages dégénérés"
# Point 4 : grandeurs rapportées à la dose ¼ quand le module rend tout nul.
ATTENTE_GRANDEURS_DE_LA_DOSE_QUART = "grandeurs rapportées à la dose un quart"
# Point 8 : liste à laquelle s'applique « un champ de plus ou de moins arrête la lecture ».
ATTENTE_LISTE_FERMEE = "liste fermée des noms rendus"
# Point 10 : contrôle des réglages de la livraison (dont les deux champs qui déclarent le schéma de permutation).
ATTENTE_CONTROLE_DES_REGLAGES = "contrôle des réglages"
CAS_EN_ATTENTE = (ATTENTE_TIRAGES_NULS_SOUS_PERMUTATIONS_PERDUES, ATTENTE_TIRAGES_NULS_SOUS_INTERVALLE_IMPOSSIBLE,
                  ATTENTE_FAMILLE_A_1_SOUS_TIRAGES_DEGENERES, ATTENTE_GRANDEURS_DE_LA_DOSE_QUART, ATTENTE_LISTE_FERMEE,
                  ATTENTE_CONTROLE_DES_REGLAGES)

# --- Gardes qui refusent, nommées (contre-lecture du code de la version 4) -------------------------------------------------
GARDE_VALEUR_P_ABSENTE = "valeur p haute absente alors qu'elle est calculable"                # B-1
GARDE_COMPTEE_POUR_1 = "valeur p comptée pour 1 ou retirée de la famille alors qu'elle est calculable"   # B-1, C-2 ; 8.4
GARDE_TOTAL_DES_TIRAGES = "total des tirages de l'intervalle différent du nombre demandé"     # C-1
GARDE_GRANDEUR_ABSENTE = "borne haute ou valeur p basse absente sans cause"                   # C-4
GARDE_VALEUR_P_ET_COMPTES = "valeur p qui ne répond pas à ses comptes"                        # M-4
GARDE_ETAPE_M_NON_JOUEE = "étape (m) non jouée"                                               # C-5
GARDE_DIXIEME_CHAMP = "dixième champ qui n'est pas un rang moyen dans le pli"                 # C-10
GARDE_DOSE_QUART_ABSENTE = "dose un quart absente de la livraison"                            # M-3
GARDES_NOMMEES = (GARDE_VALEUR_P_ABSENTE, GARDE_COMPTEE_POUR_1, GARDE_TOTAL_DES_TIRAGES, GARDE_GRANDEUR_ABSENTE,
                  GARDE_VALEUR_P_ET_COMPTES, GARDE_ETAPE_M_NON_JOUEE, GARDE_DIXIEME_CHAMP, GARDE_DOSE_QUART_ABSENTE)


class ArretNomme(GardeArret):
    """Arrêt commandé par une garde nommée ; `nom` est l'un de `GARDES_NOMMEES` ou de `CAS_EN_ATTENTE`."""

    def __init__(self, nom: str, message: str):
        if nom not in GARDES_NOMMEES + CAS_EN_ATTENTE:
            raise GardeArret(f"arrêt nommé {nom!r} hors de la liste des gardes")
        super().__init__(f"[{nom}] {message}")
        self.nom = nom


class EnAttenteDeDecision(ArretNomme):
    """Arrêt sur un cas que le texte ne tranche pas : il attend une décision. Aucun repli, aucun réglage ne le lève."""

    def __init__(self, nom: str, message: str):
        if nom not in CAS_EN_ATTENTE:
            raise GardeArret(f"cas en attente {nom!r} hors de {CAS_EN_ATTENTE}")
        super().__init__(nom, message + " — CE CAS ATTEND UNE DÉCISION (note du brouillon 20, parties 3 et 5) : le code "
                                        "ne choisit pas et ne continue pas")
