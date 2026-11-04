"""Critères de lecture gelés du pilote, version 3 (R1) : ceux de la v2 (`pilote_exposant_p_v2.analyse`, importés tels
quels : constantes, ordre gelé des issues, rééchantillonnages, qualificatifs, contrôles de l'instrument, symétrie), à
deux phrases près, reprises mot pour mot du « nouveau » des couples 17 et 18 de la contre-lecture R2 du brouillon 2
(`couples-contre-lecture-pilote-exposant-p-v2.json`) et du brouillon 3 (section « Phrases ») :
- `NE_MONTRE_PAS` (couple 17) : E et R sont lues au dernier jeton de phrases courtes ; E change le seul dernier mot (mot
  technique d'évaluation de modèle, étranger au contenu, contre un événement de vie appelé par le contenu) ; R change
  le corps, le dernier mot est commun. La v2 disait « E et R sont faites de fins de phrase courtes », faux pour R ;
- `QUALIF_JUMEAU["au-dessus du jumeau"]` (couple 18) : le jumeau contrôle le nombre de jetons, ni le domaine technique
  des porteurs d'évaluation ni leur écart au contenu.
`PHRASES` est la table v2 où l'ancienne borne commune est remplacée par la nouvelle ; `phrase` est redéfinie pour lire
cette table (celle de la v2 lit la table v2).
"""
from __future__ import annotations

from ..pilote_exposant_p_v2 import analyse as _A2
from ..pilote_exposant_p_v2.analyse import *  # noqa: F401,F403 — tout ce qui ne change pas

NE_MONTRE_PAS = ("Cela ne dit rien des couches moyennes, des contextes longs ni du comportement ; E et R sont lues au "
                 "dernier jeton de phrases courtes (E : seul le dernier mot change, un mot technique d'évaluation de "
                 "modèle, étranger au contenu, contre un événement de vie appelé par le contenu ; R : le corps change, "
                 "le dernier mot est commun) ; p > 2 est nécessaire, non suffisant, pour un trait (§7 du papier), et "
                 "p ≈ 2 n'exclut pas un trait mal aligné (§6.1).")
ISSUES_BORNEES = ("au-dessus", "au-dessous", "égal")


def _remplacer_borne(table: dict, ancienne: str, nouvelle: str) -> dict:
    """Remplace la borne commune dans les trois issues tranchées, et seulement là ; toute autre présence, ou une
    absence, arrête à l'import (aucun repli silencieux, R5)."""
    t = {}
    for k, v in table.items():
        n = v.count(ancienne)
        if n != (1 if k in ISSUES_BORNEES else 0):
            raise RuntimeError(f"phrase « {k} » : borne commune v2 trouvée {n} fois")
        t[k] = v.replace(ancienne, nouvelle)
    return t


PHRASES = _remplacer_borne(_A2.PHRASES, _A2.NE_MONTRE_PAS, NE_MONTRE_PAS)

QUALIF_JUMEAU = dict(_A2.QUALIF_JUMEAU)
QUALIF_JUMEAU["au-dessus du jumeau"] = (
    "Jumeau neutre (fin sans statut, même construction ; emprunt à R9-bis) : p̄(E, R) − p̄(N, R) = {d} [{ic}] : l'écart "
    "est propre à la fin d'évaluation telle que construite, pas à un mot neutre de même nombre de jetons ; le jumeau ne "
    "contrôle ni le domaine technique des porteurs d'évaluation ni leur écart au contenu.")


def phrase(issue: str, **valeurs) -> str:
    return PHRASES[issue].format(delta=DELTA_EQUIVALENCE, **valeurs)  # noqa: F405
