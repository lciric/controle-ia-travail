"""Papier C — erreurs nommées de la liste d'arrêt (v1).

Texte de référence : préenregistrement du papier C, brouillon 6 de relance, version r1
(`e12f16fa1460149344cd5d68b614294ea502c4c7fc24bc86970cafcfbaafc8b2`), section « Liste d'arrêt » (lignes 1467 à 1522).
Chaque garde de la liste lève une erreur de ce fichier, jamais une valeur de repli (R5). Deux familles :
`ArretPapierC` (arrêt du run ou de la lecture concernée) et `NoeudPapierC` (arrêt, et décision de Lazar exigée,
quand le texte écrit « nœud »). Toutes héritent de `controle_ia.gardes.GardeArret`, importée sans modification.

Le numéro porté par chaque classe (`garde`) est celui de la liste d'arrêt du texte ; il ne vient qu'en appui du nom.
"""
from __future__ import annotations

from controle_ia.gardes import GardeArret


class ArretPapierC(GardeArret):
    """Arrêt commandé par une garde de la liste d'arrêt du papier C."""

    garde: int | None = None


class NoeudPapierC(ArretPapierC):
    """Arrêt qui est aussi un nœud de décision : rien ne reprend sans le mot de Lazar."""


# --- configuration (hors liste d'arrêt : lecture et validation de la configuration) -------------------------------
class ConfigurationInvalide(ArretPapierC):
    """Champ inconnu, champ manquant, type faux ou constante différente de celle du texte."""


# --- garde 1 ------------------------------------------------------------------------------------------------------
class EmpreinteNonConforme(ArretPapierC):
    """Empreinte d'une pièce (texte, configuration, addendum, juge, items, contenus, tâches, sondes) non conforme."""
    garde = 1


class ModuleNonConforme(ArretPapierC):
    """Ligne « Module du papier C » non conforme, ou fichier du module sans ligne."""
    garde = 1


class ArbreGeleModifie(ArretPapierC):
    """Arbre gelé du commit 7a54d43 modifié sous `src/` ou `tests/`."""
    garde = 1


class MarqueurRestant(ArretPapierC):
    """Marqueur `<<…>>` restant dans la configuration."""
    garde = 1


# --- garde 2 ------------------------------------------------------------------------------------------------------
class PrealableAbsent(ArretPapierC):
    """Préalable du pilote ou de l'étape 2 absent ou non scellé."""
    garde = 2


class AccordDuJourAbsent(ArretPapierC):
    """Lancement payant sans ligne d'accord du jour consignée."""
    garde = 2


class AccordDeDepenseInvalide(ArretPapierC):
    """Aucun accord de dépense valide au jour du lancement dans le registre des accords."""
    garde = 2


# --- garde 3 ------------------------------------------------------------------------------------------------------
class BudgetDepasse(ArretPapierC):
    """Lancement estimé à 10 USD ou plus, ou pilote au-delà de 4 heures de carte cumulées."""
    garde = 3


class ArretInstanceNonConsigne(ArretPapierC):
    """Instance non arrêtée par son identifiant, ou arrêt non consigné."""
    garde = 3


# --- garde 4 ------------------------------------------------------------------------------------------------------
class BancProcesseurNonReproduit(ArretPapierC):
    """Banc sur processeur non reproduit : arrêt avant toute carte."""
    garde = 4


class DefautDeChaineAuBanc(NoeudPapierC):
    """Ordre contraire chez les trois juges au banc sur carte et défaut de la chaîne trouvé à l'audit A6."""
    garde = 4


# --- garde 5 ------------------------------------------------------------------------------------------------------
class VarianteRefusee(ArretPapierC):
    """Une valeur ne tient pas en un jeton en contexte, ou deux valeurs partagent un jeton."""
    garde = 5


class AucuneVariantePourUnJuge(NoeudPapierC):
    """Aucune variante de réponse imposée ne passe pour un juge."""
    garde = 5


# --- garde 6 ------------------------------------------------------------------------------------------------------
class LisibiliteNonTenue(NoeudPapierC):
    """Critère de lisibilité du pilote non tenu après le choix de la variante."""
    garde = 6


class AnomaliesDeMasse(NoeudPapierC):
    """Étape 2 : plus de 5 % de lectures de masse sous 0,50 pour un juge et une consigne."""
    garde = 6


# --- garde 7 ------------------------------------------------------------------------------------------------------
class LectureTronquee(ArretPapierC):
    """Lecture sur un contenu tronqué, ou contexte au-delà de la longueur du juge."""
    garde = 7


# --- garde 8 ------------------------------------------------------------------------------------------------------
class InstrumentVariable(ArretPapierC):
    """Consigne, variante, mode ou juge différents selon l'intensité au sein d'une loi."""
    garde = 8


# --- garde 9 ------------------------------------------------------------------------------------------------------
class FuiteDeLaCible(ArretPapierC):
    """Consigne d'un juge différente de la configuration, variable selon la condition, ou porteuse d'une
    formulation du vivier ou d'un témoin."""
    garde = 9


# --- garde 10 -----------------------------------------------------------------------------------------------------
class InsertionAbsente(ArretPapierC):
    """Insertion absente du rendu complet, ou placée hors de la règle."""
    garde = 10


# --- garde 11 -----------------------------------------------------------------------------------------------------
class GardeLexicaleEnEchec(ArretPapierC):
    """Motif interdit dans une formulation, un témoin, le constat nu ou un paragraphe de bras."""
    garde = 11


# --- garde 12 -----------------------------------------------------------------------------------------------------
class RecouvrementCalibrageEtape2(ArretPapierC):
    """Contenu ou tâche commun au lot de calibrage et à l'étape 2."""
    garde = 12


class FichierDuBancRefuse(ArretPapierC):
    """La dérivation a reçu en entrée un fichier du banc."""
    garde = 12


# --- garde 13 -----------------------------------------------------------------------------------------------------
class EntropieNonConforme(ArretPapierC):
    """Entropie absente ou différente de celle du scellement."""
    garde = 13


class CleDeGraineNonDeclaree(ArretPapierC):
    """Clé de graine absente de la configuration."""
    garde = 13


# --- garde 14 -----------------------------------------------------------------------------------------------------
class RegleDeLAddendumInapplicable(NoeudPapierC):
    """Une règle de l'addendum de dérivation ne peut pas s'appliquer."""
    garde = 14


# --- garde 15 -----------------------------------------------------------------------------------------------------
class AucuneSondeDesignee(NoeudPapierC):
    """Aucune sonde désignée par le verdict de la porte de sortie de la phase 0."""
    garde = 15


# --- garde 16 -----------------------------------------------------------------------------------------------------
class TachesNonConformes(ArretPapierC):
    """Fichier de tâches d'empreinte non conforme, partage non tiré par sa clé, listes absentes du manifeste,
    ou tâche commune au lot de calibrage et au bassin de l'étape 2."""
    garde = 16


class BassinTropPetit(NoeudPapierC):
    """Bassin de l'étape 2 de moins de n_min / 2 tâches à son ouverture, ou aucun effectif permis."""
    garde = 16


# --- garde 18 -----------------------------------------------------------------------------------------------------
class TexteDansLeDepotPublic(ArretPapierC):
    """Texte de contenu, d'item ou du gabarit trouvé dans un fichier destiné au dépôt public."""
    garde = 18


# --- garde 19 -----------------------------------------------------------------------------------------------------
class EcartAuPreenregistrement(NoeudPapierC):
    """Écart au préenregistrement constaté en cours de run."""
    garde = 19


# --- garde 20 -----------------------------------------------------------------------------------------------------
class LectureForceeInfidele(ArretPapierC):
    """Suite de jetons relue différente de celle de l'épisode, message système qui n'est pas celui de la relecture
    annoncée, ou témoin de l'instrument hors de la tolérance : lignes du témoin lexical « non mesurées »."""
    garde = 20


# --- garde 21 -----------------------------------------------------------------------------------------------------
class ScoreDansLaGeneration(NoeudPapierC):
    """Score de sonde ou de juge trouvé dans la génération, le choix, le filtrage ou la régénération d'un épisode."""
    garde = 21


# --- garde 22 -----------------------------------------------------------------------------------------------------
class BancDeControlabiliteIndisponible(NoeudPapierC):
    """Banc publié indisponible, licence non vérifiée, ou version et empreinte absentes du manifeste."""
    garde = 22


# --- garde 23 -----------------------------------------------------------------------------------------------------
class ParagraphesDePlaidoyerNonConformes(ArretPapierC):
    """Paragraphes de plaidoyer en nombre différent de k_P, ou dans un autre ordre que la configuration scellée."""
    garde = 23


# --- interdit de CLAUDE.md et décision N-026 ----------------------------------------------------------------------
class MoyenneEnProduction(ArretPapierC):
    """Une agrégation à moyenne (bras de diagnostic, jamais en production) est présentée à une règle de décision."""


__all__ = [n for n, o in dict(globals()).items() if isinstance(o, type) and issubclass(o, GardeArret) and o is not GardeArret]
