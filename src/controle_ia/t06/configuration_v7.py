"""Configuration de T0.6, v7 (chaîne v14 : lanceur `scripts/lancer_t06_v14.sh`, amorce `scripts/amorce_instance_t06_v12.sh` ; nom neuf, R12 : `configuration_v6.py`
reste tel quel). Seule différence avec la v6 : **la ligne de GO de la course n'est plus écrite en dur non plus**.
- La v6 reconnaissait la course à son `go_id` (le GO de la course, écrit en dur dans `configuration.py`) et validait sa configuration sans registre (GO exact, 200 USD
  exacts) ; toute autre ligne lisible était une épreuve à blanc. Une configuration de course sous une ligne neuve (`GO-2026-11-10-01`, prolongation au 23 novembre,
  R-2077) y serait donc lue comme une épreuve et refusée avec son préenregistrement par le lanceur v6.
- Ici **toute** configuration (course ou épreuve, réelle ou jouet) est validée contre le registre des GO, **obligatoire** (aucune validation sans lui : R5, pas de
  repli) : `session_v13.go_de_la_configuration` (ligne `go_id` présente, type « calcul », accordée par Lazar, non échue au jour donné, non révoquée ; plafond de la
  configuration fini, strictement positif, au plus égal au plafond de la ligne) ; le reste est validé comme en v6 (validation v3 aux valeurs de référence de
  `configuration.py`, clé `egalite_jetons_reels`).
- Course ou épreuve ne se lit plus dans la configuration : c'est le lanceur de run v7 qui le reçoit de l'amorce (`--epreuve`) ; `est_epreuve` n'existe plus ici.
"""
from __future__ import annotations

from datetime import date

from ..gardes import GardeArret
from ..sondes.familles_v2 import PAQUET_GELE
from .configuration import GO_ID as GO_REFERENCE_V3, PLAFOND_USD as PLAFOND_REFERENCE_V3
from .configuration_v3 import exiger_config_t06_v3
from .configuration_v4 import CLE_JETONS_REELS, jetons_reels_voulus  # noqa: F401  (réexporté)
from .session import GardeSession
from .session_v13 import go_de_la_configuration


def exiger_config_t06_v7(config: dict, registre_go=None, jour: date | None = None) -> dict:
    """Rend la ligne de GO de la configuration (`session_v13.go_de_la_configuration`) après toutes les vérifications ; lève `GardeArret` sinon."""
    if CLE_JETONS_REELS not in config:
        raise GardeArret(f"configuration de T0.6 v7 incomplète : {[CLE_JETONS_REELS]} (C-V4-2 : booléen, aucune valeur implicite)")
    v = config[CLE_JETONS_REELS]
    if not isinstance(v, bool):
        raise GardeArret(f"{CLE_JETONS_REELS} : booléen attendu, pas {v!r}")
    if registre_go is None:
        raise GardeArret(f"GO {config.get('go_id')!r} : registre des GO exigé pour lire la ligne de la configuration et borner son plafond (aucune validation sans lui)")
    try:
        ligne = go_de_la_configuration(config, registre_go, config.get("go_id"), jour)
    except GardeSession as e:
        raise GardeArret(f"GO {config.get('go_id')!r} : ligne de GO de la configuration non conforme : {e}") from None
    reste = {k: x for k, x in config.items() if k != CLE_JETONS_REELS}
    reste.update(go_id=GO_REFERENCE_V3, plafond_usd=PLAFOND_REFERENCE_V3)     # le reste est validé comme en v6 (les deux clés viennent d'être lues au registre)
    exiger_config_t06_v3(reste)
    if v and config.get("mahalanobis_calcul") == PAQUET_GELE:
        raise GardeArret(f"{CLE_JETONS_REELS} vrai sous le paquet gelé : aucun essai d'égalité n'est joué sous le paquet gelé (refus, pas d'ignorance silencieuse)")
    return ligne
