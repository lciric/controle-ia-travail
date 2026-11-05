"""Gardes de réception de la relance v4 de R1 (entrées, code v4), exigées par l'addendum v4 de R1 scellé
(`prereg/R1-addendum-relance-v4.md`, 0f10881b…, étape 4, « Analyses (inchangées) ») et rappelées par la fiche de
réception v4 (section 6). Elles s'ajoutent aux gardes de `entrees_v1.charger_r1`, reprises sans modification, et se
lisent sur le résultat scellé du rejeu que cite la fiche (`diag/<run>/rejeu-activations.json`, rattaché à son
manifeste `runs/<run>/manifeste.json`) :
- `texte` : le texte qui gouverne le rejeu, lu dans `preenregistrement` du manifeste du rejeu, est l'addendum v4 scellé
  (chemin et empreinte), non l'addendum v3 ;
- `table-comparee` : `tokenisation.table_sha256` est comparée au sceau de la table v4 versée avec le run
  (`prereg/R1-table-tokenisation-v4.json`, compagnon `.sha256` vérifié) **et** `resultat_reparation_sha256`, cité par la
  table, égale le sceau du résultat de la réparation versé (compagnon `.sha256` vérifié) : l'empreinte n'est pas connue
  d'avance (V4-E5), elle est fixée par la chaîne scellée ;
- `provenance` : `tokenisation.addendum` = `prereg/R1-addendum-relance-v4.md` à l'identique (V4-E14), et la commande du
  manifeste du rejeu est `rejeu_activations_v4`.
Du résultat de la réparation, seuls les octets sont hachés (rien n'en est lu) ; de la table, seule la clé
`resultat_reparation_sha256` est lue ; un message d'arrêt nomme la garde et la clé, jamais une valeur de couverture.
"""
from __future__ import annotations

from pathlib import Path

from ..analyse_blanche_noire.entrees import lire_json
from ..gardes import GardeArret
from ..manifeste import lire_manifeste, verifier_resultat
from ..scellement import verifier
from . import constantes_v6 as K6


def exiger_reception_v4(racine: Path, chemin_resultat: str) -> dict:
    """Les trois gardes, dans l'ordre de l'addendum v4 (`texte`, `table-comparee`, `provenance`) ; arrêt à la première
    qui manque (`GardeArret`, motif écrit, rien n'est lu) ; sinon, ce qui a été comparé (chemins et empreintes)."""
    racine = Path(racine)
    corps = verifier_resultat(racine, racine / chemin_resultat)
    run = corps["run_id"]
    m, sha_m = lire_manifeste(racine / "runs" / run / "manifeste.json")
    # texte : le texte qui gouverne le rejeu est l'addendum v4 scellé (chemin et empreinte)
    if m.get("preenregistrement") != K6.ADDENDUM_V4:
        raise GardeArret(f"garde texte : le texte qui gouverne le rejeu {run} (clé preenregistrement de son manifeste) "
                         f"≠ addendum v4 scellé ({K6.ADDENDUM_V4['chemin']}, {K6.ADDENDUM_V4['sha256'][:12]}…) : "
                         f"rien n'est lu")
    tk = (corps.get("resultat") or {}).get("tokenisation")
    if not isinstance(tk, dict):
        raise GardeArret(f"garde table-comparee : résultat du rejeu {run} sans clé tokenisation")
    # table-comparee : table versée (sceau) et résultat de la réparation versé (sceau cité par la table)
    sha_table = verifier(racine / K6.TABLE_V4)
    table = lire_json(racine / K6.TABLE_V4)
    sha_rep = verifier(racine / K6.RESULTAT_REPARATION_V4)
    if tk.get("table_sha256") != sha_table:
        raise GardeArret(f"garde table-comparee : tokenisation.table_sha256 du rejeu {run} ≠ sceau de la table v4 versée "
                         f"({K6.TABLE_V4})")
    if not isinstance(table, dict) or table.get("resultat_reparation_sha256") != sha_rep:
        raise GardeArret(f"garde table-comparee : resultat_reparation_sha256 cité par la table v4 ({K6.TABLE_V4}) ≠ sceau "
                         f"du résultat de la réparation versé ({K6.RESULTAT_REPARATION_V4})")
    # provenance : addendum de la table à l'identique (V4-E14) et commande du rejeu
    if tk.get("addendum") != K6.ADDENDUM_V4["chemin"]:
        raise GardeArret(f"garde provenance : tokenisation.addendum du rejeu {run} ≠ {K6.ADDENDUM_V4['chemin']} (V4-E14)")
    if m.get("commande") != K6.COMMANDE_REJEU_V4:
        raise GardeArret(f"garde provenance : commande du manifeste du rejeu {run} ≠ « {K6.COMMANDE_REJEU_V4} »")
    return {"run_rejeu": run, "manifeste_sha256": sha_m, "texte": m["preenregistrement"], "commande": m["commande"],
            "table": {"chemin": K6.TABLE_V4, "sha256": sha_table},
            "reparation": {"chemin": K6.RESULTAT_REPARATION_V4, "sha256": sha_rep},
            "tokenisation": {"addendum": tk["addendum"], "table_sha256": tk["table_sha256"]}}
