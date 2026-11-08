"""Configuration de T0.6, v5 (E3 du 7 novembre ; nom neuf, R12 : `configuration_v4.py` reste tel quel).
Seule différence avec la v4 : le plafond d'une configuration d'ÉPREUVE (go_id `GO-2026-11-06-01`) n'est plus l'une des deux valeurs 1,5 (E2) ou 3,5 (E3) mais **un nombre fini strictement positif,
au plus 8 USD** (5 USD du GO de l'épreuve + 3 USD de GO-2026-11-07-08 pour E3 bis). Contrôle réel : la configuration d'E3 (plafond 4,27) était refusée par la v4 au démarrage du run
(« plafond 4.27 : (1.5, 3.5) USD attendus »), ce que la suite complète échouée avait masqué. Le plafond effectivement permis reste borné par le reste du GO au lanceur
(`session_v10.verifier_plafond_epreuve`) ; ici on ne fait que refuser un plafond illisible ou hors de toute proportion. Le reste (clé `egalite_jetons_reels`, validation de course) est celui de la v4.
"""
from __future__ import annotations

import math

from ..gardes import GardeArret
from ..sondes.familles_v2 import PAQUET_GELE
from .configuration_v3 import exiger_config_t06_v3
from .configuration_v4 import CLE_JETONS_REELS, GO_EPREUVE, est_epreuve, jetons_reels_voulus  # noqa: F401  (réexportés)

PLAFOND_EPREUVE_MAX_USD = 8.0


def exiger_config_t06_v5(config: dict) -> None:
    if CLE_JETONS_REELS not in config:
        raise GardeArret(f"configuration de T0.6 v5 incomplète : {[CLE_JETONS_REELS]} (C-V4-2 : booléen, aucune valeur implicite)")
    v = config[CLE_JETONS_REELS]
    if not isinstance(v, bool):
        raise GardeArret(f"{CLE_JETONS_REELS} : booléen attendu, pas {v!r}")
    reste = {k: x for k, x in config.items() if k != CLE_JETONS_REELS}
    if config.get("go_id") == GO_EPREUVE:
        p = config.get("plafond_usd")
        if isinstance(p, bool) or not isinstance(p, (int, float)) or not math.isfinite(p) or not (0 < p <= PLAFOND_EPREUVE_MAX_USD):
            raise GardeArret(f"plafond {p!r} : nombre fini de 0 (exclu) à {PLAFOND_EPREUVE_MAX_USD} USD attendu pour {GO_EPREUVE}")
        from .configuration import GO_ID, PLAFOND_USD
        reste.update(go_id=GO_ID, plafond_usd=PLAFOND_USD)       # le reste est validé comme une configuration de course
    exiger_config_t06_v3(reste)
    if v and config.get("mahalanobis_calcul") == PAQUET_GELE:
        raise GardeArret(f"{CLE_JETONS_REELS} vrai sous le paquet gelé : aucun essai d'égalité n'est joué sous le paquet gelé (refus, pas d'ignorance silencieuse)")
