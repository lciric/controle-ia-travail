"""Oracle v2 (mineur 1 de la contre-lecture du code `36ecc4a4…`) : la table de `oracle_v1.table_oracle`, inchangée,
plus le champ `membres_a_la_borne_triviale` — membres ajustés du nul que le juge rend à la borne triviale 0 (ajustement
logarithmique non convergé à 20 000 issues, `nul_filles_v2._logit`). Une telle valeur serait prise pour le meilleur
membre et toute la génération serait sans « porteuse » : elle est désormais signalée, rapportée par la lecture v2 dans
l'audit (R4), sans toucher un critère du texte."""
from __future__ import annotations

from . import oracle_v1 as O1


def membres_a_la_borne_triviale(J, table: dict) -> list[str]:
    ajustes = {"ajuste_lineaire:archive"} | {k for k in table["membres"] if k.startswith("ajuste_log:")}
    return sorted(k for k, v in table["membres"].items() if k in ajustes and v == 0.0)


def table_oracle(J, gen) -> dict:
    t = O1.table_oracle(J, gen)
    t["membres_a_la_borne_triviale"] = membres_a_la_borne_triviale(J, t)
    return t
