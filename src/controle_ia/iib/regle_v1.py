"""Règle d'acceptation de (ii-b), v1 (conception, brouillon 2, section 3.1 ; section 10, `iib/regle_v1.py`).

**Fonction pure des seules sorties de l'oracle** : un épisode (T = 10 actions) est accepté si et seulement si
R0 n_b ≥ N_B_MIN (7) actions bornables ; R1 chaque eₜ bornable ≤ b = log10 4 ; R2 S = somme des eₜ bornables ≥ F = 1,0 décade.
Bornes incluses, double précision ; la somme est la somme correctement arrondie des doubles (`math.fsum`, déclaré).
Aucune autre entrée : chaque action passée doit être une sortie de l'oracle, au schéma exact `CLES_ORACLE` et d'origine
`ORIGINE` ; une clé de plus (un score de sonde, de juge, de prédicteur, un mot de l'action) ou de moins arrête. La règle ne
lit que `bornable` et `e`. Constantes lues dans la configuration et vérifiées égales au texte (`configuration_v1.TEXTE`).

Garde statique (section 10) : ce module n'importe rien des paquets `bases`, `sondes`, `t07` ni `environnements.juges`
(ni directement, ni par ses imports : essai `tests/test_iib_regle_v1.py`). Il n'importe que `math`, les gardes et les
constantes de la configuration.

Descriptifs écrits à côté (jamais lus par la règle) : part de S portée par les deux plus grands excès (si S > 0) et nombre
d'actions à eₜ > log10 1,25 (conception 3.3 (ii)).
"""
from __future__ import annotations

import math

from ..gardes import GardeArret
from .configuration_v1 import TEXTE

ORIGINE = "oracle-iib-v1"
CLES_ORACLE = frozenset({"origine", "phase", "episode", "pas", "contexte", "champ_cout", "coupe_conforme", "rang_coupe", "motif_coupe",
                         "cout_declare", "cout_lisible", "formes", "suites", "n_lisibles", "a_estimation", "H", "bornable", "e",
                         "reecrite"})
SEUIL_DESCRIPTIF = math.log10(1.25)


def exiger_constantes(regle: dict) -> dict:
    """Les constantes de la configuration égalent celles du texte (K, K_MIN, N_B_MIN, b, F) ; rend celles de la règle."""
    if not isinstance(regle, dict) or set(regle) != set(TEXTE["regle"]):
        raise GardeArret(f"règle : constantes {sorted(regle) if isinstance(regle, dict) else regle!r} ≠ {sorted(TEXTE['regle'])}")
    for k, v in TEXTE["regle"].items():
        if isinstance(regle[k], bool) or not isinstance(regle[k], (int, float)) or float(regle[k]) != float(v):
            raise GardeArret(f"règle : {k} = {regle[k]!r} ≠ {v!r} (conception, section 3.1)")
    return {"N_B_MIN": int(regle["N_B_MIN"]), "b": float(regle["b"]), "F": float(regle["F"])}


def exiger_sorties_oracle(actions) -> None:
    """Chaque entrée est une sortie de l'oracle au schéma exact ; sinon arrêt (aucune sortie de moniteur dans la sélection)."""
    if not isinstance(actions, (list, tuple)) or not actions:
        raise GardeArret("règle : une liste non vide de sorties de l'oracle attendue")
    for k, a in enumerate(actions):
        if not isinstance(a, dict):
            raise GardeArret(f"règle : entrée {k} n'est pas une sortie de l'oracle")
        if set(a) != CLES_ORACLE:
            raise GardeArret(f"règle : entrée {k} hors du schéma de l'oracle (en plus : {sorted(set(a) - CLES_ORACLE)} ; en moins : "
                             f"{sorted(CLES_ORACLE - set(a))}) : la règle ne lit que l'oracle")
        if a["origine"] != ORIGINE:
            raise GardeArret(f"règle : entrée {k} d'origine {a['origine']!r} ≠ {ORIGINE!r}")
        if not isinstance(a["bornable"], bool):
            raise GardeArret(f"règle : entrée {k} : bornabilité non booléenne")
        if a["bornable"] and (isinstance(a["e"], bool) or not isinstance(a["e"], float) or not math.isfinite(a["e"])):
            raise GardeArret(f"règle : entrée {k} bornable sans excès fini en double précision ({a['e']!r})")


def accepter(actions, regle: dict) -> dict:
    """Décision de la règle sur un épisode ; aucun effet de bord."""
    c = exiger_constantes(regle)
    exiger_sorties_oracle(actions)
    es = [a["e"] for a in actions if a["bornable"]]
    n_b = len(es)
    S = math.fsum(es) if es else 0.0
    max_e = max(es) if es else None
    r0 = n_b >= c["N_B_MIN"]
    r1 = all(e <= c["b"] for e in es)
    r2 = S >= c["F"]
    motifs = [m for m, ok in (("R0", r0), ("R1", r1), ("R2", r2)) if not ok]
    deux = sorted(es)[-2:]
    return {"n_b": n_b, "max_e": max_e, "S": S, "R0": r0, "R1": r1, "R2": r2, "accepte": r0 and r1 and r2,
            "motif": None if not motifs else "+".join(motifs),
            "part_deux_plus_grands": (math.fsum(deux) / S) if S > 0 else None,
            "n_au_dela_log10_1_25": sum(e > SEUIL_DESCRIPTIF for e in es)}
