"""Mini-course d'idéation, Kimi et Argon seuls (GO-2026-11-01-12) — version 2, au-dessus de `course2_nuit_v1` (inchangé, R12).

Rédigé le 1er novembre 2026 (sous-agent de session-depot) après la contre-lecture
`docs/notes/mini-course-kimi-argon-v1/contre-lecture-mini-course-kimi-argon-v1.md` (« scellable après corrections ») :

- **CLM-02** : un coût lu au-dessus du pire cas réservé (`depassement_reserve: true` sur la dernière ligne d'une commande)
  **arrête la course** (`ArretDepassementReserve`) : la garde cumulée ne tient plus ; en v1, l'appel n'était qu'inexploitable.
- **CLM-09** : un refus de plafond tenu hors du noyau arrête la course sous un motif distinct, au lieu d'apparaître comme
  « trois échecs consécutifs » ou comme nœud : garde cumulée des commandes (`ArretPlafondCumule`), garde du plafond dur de
  l'étape dans le registre (`ArretPlafondEtapeCommande`), plafond propre d'un relais (`ArretPlafondRelais`, HTTP 402 ou 429).
- Le refus « modèle servi » (v1) reste un arrêt.

La génération (`GenerationNuitV1`), la course à une génération (`executer_mini_course_v1`) et les contrôles du scénario B
(`verifier_configuration_nuit`) sont ceux de la v1, inchangés : seul l'adaptateur des commandes change.
"""

from .adaptateurs_v56 import AdaptateurCommandeExterneV56
from .course2_nuit_v1 import (EVENEMENTS_MODELE, SCENARIO, ArretDebordementKimi, ArretModeleServiDifferent, ArretTroisEchecs,
                              GenerationNuitV1, executer_mini_course_v1, verifier_configuration_nuit)

VERSION = "course-2-nuit-v2 (mini-course Kimi et Argon, scénario B, au-dessus de la v1)"


class ArretDepassementReserve(RuntimeError):
    """CLM-02 : coût lu au-dessus du pire cas réservé ; la garantie de la garde cumulée ne tient plus."""


class ArretPlafondCumule(RuntimeError):
    """CLM-09 : la garde cumulée des commandes (10 USD) refuse un appel : plus rien ne peut partir."""


class ArretPlafondEtapeCommande(RuntimeError):
    """CLM-09 : la garde du plafond dur de l'étape, tenue par le registre des commandes, refuse un appel."""


class ArretPlafondRelais(RuntimeError):
    """CLM-09 : le plafond propre d'un relais (ou son nombre d'appels) est atteint (HTTP 402 ou 429)."""


def motif_de_ligne(objet):
    """Exception à lever pour la dernière ligne d'une commande, ou None."""
    if not isinstance(objet, dict):
        return None
    if objet.get("depassement_reserve") is True:
        return ArretDepassementReserve
    erreur = str(objet.get("erreur") or "")
    if erreur.startswith("garde cumulée"):
        return ArretPlafondCumule
    if erreur.startswith("garde d'étape"):
        return ArretPlafondEtapeCommande
    if erreur.startswith(("HTTP 402", "HTTP 429")):
        return ArretPlafondRelais
    return None


class AdaptateurCommandeExterneNuitV2(AdaptateurCommandeExterneV56):
    """Commande externe v56 ; arrêts de la course : modèle servi (v1), dépassement de réserve, plafonds hors noyau (v2)."""

    nom = "commande-externe-nuit-v2"

    def lire_derniere_ligne(self, sortie_octets):
        objet, motif = super().lire_derniere_ligne(sortie_octets)
        self._derniere_nuit = objet
        return objet, motif

    def lancer(self, role, consigne, dossier, budget_usd, max_tours, modele=None):
        self._derniere_nuit = None
        r = super().lancer(role, consigne, dossier, budget_usd, max_tours, modele=modele)
        objet, self._derniere_nuit = self._derniere_nuit, None
        if r.statut == "refus" and isinstance(r.refus, dict) and r.refus.get("evenement") in EVENEMENTS_MODELE:
            raise ArretModeleServiDifferent(f"modèle servi {r.refus.get('modele_servi')!r} ≠ modèle demandé {modele!r} "
                                            "(refus R-764) : arrêt de la course (liste d'arrêt)")
        classe = motif_de_ligne(objet)
        if classe is not None:
            raise classe(f"{classe.__name__} : {str(objet.get('erreur') or 'dépassement de réserve')[:200]} — arrêt de la "
                         "course (liste d'arrêt) ; coût compté au plafond de session par le noyau, réel au registre cumulé")
        return r

    def description(self):
        d = super().description()
        d["nuit"] = ("arrêts de la course : modèle servi différent, dépassement de réserve, garde cumulée, garde d'étape des "
                     "commandes, plafond d'un relais (v2, CLM-02, CLM-09)")
        return d


__all__ = ("AdaptateurCommandeExterneNuitV2", "ArretDepassementReserve", "ArretPlafondCumule", "ArretPlafondEtapeCommande",
           "ArretPlafondRelais", "ArretModeleServiDifferent", "ArretTroisEchecs", "ArretDebordementKimi", "GenerationNuitV1",
           "executer_mini_course_v1", "verifier_configuration_nuit", "motif_de_ligne", "SCENARIO", "VERSION")
