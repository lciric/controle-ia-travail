"""Gardes de réception de la relance v4 de R1 (entrées, version 4 de l'analyse secondaire), exigées par l'addendum v4
de R1 scellé (`prereg/R1-addendum-relance-v4.md`, 0f10881b…, étape 4, « Analyses (inchangées) ») et rappelées par la
fiche de réception v4 (section 6). Elles s'ajoutent aux gardes de `entrees_v3.charger_activations_v3`, reprises sans
modification, et se lisent sur le « manifeste » de R1 que cite la fiche v3 (`diag/<run>/rejeu-activations.json`,
résultat scellé du rejeu, rattaché à son manifeste `runs/<run>/manifeste.json`) :
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
Même règle que `analyse_principale_r1_r2.entrees_v4`, recopiée (le paquet secondaire ne charge aucun module du paquet
principal).
"""
from __future__ import annotations

from pathlib import Path

from ..gardes import GardeArret
from ..manifeste import lire_manifeste, verifier_resultat
from ..scellement import verifier
from . import constantes_v4 as C4
from .entrees import lire_json


def exiger_reception_v4(racine: Path, chemin_resultat: str) -> dict:
    """Les trois gardes, dans l'ordre de l'addendum v4 (`texte`, `table-comparee`, `provenance`) ; arrêt à la première
    qui manque (`GardeArret`, motif écrit, rien n'est lu) ; sinon, ce qui a été comparé (chemins et empreintes)."""
    racine = Path(racine)
    corps = verifier_resultat(racine, racine / chemin_resultat)
    run = corps["run_id"]
    m, sha_m = lire_manifeste(racine / "runs" / run / "manifeste.json")
    # texte : le texte qui gouverne le rejeu est l'addendum v4 scellé (chemin et empreinte)
    if m.get("preenregistrement") != C4.ADDENDUM_V4:
        raise GardeArret(f"garde texte : le texte qui gouverne le rejeu {run} (clé preenregistrement de son manifeste) "
                         f"≠ addendum v4 scellé ({C4.ADDENDUM_V4['chemin']}, {C4.ADDENDUM_V4['sha256'][:12]}…) : "
                         f"rien n'est lu")
    tk = (corps.get("resultat") or {}).get("tokenisation")
    if not isinstance(tk, dict):
        raise GardeArret(f"garde table-comparee : résultat du rejeu {run} sans clé tokenisation")
    # table-comparee : table versée (sceau) et résultat de la réparation versé (sceau cité par la table)
    sha_table = verifier(racine / C4.TABLE_V4)
    table = lire_json(racine / C4.TABLE_V4)
    sha_rep = verifier(racine / C4.RESULTAT_REPARATION_V4)
    if tk.get("table_sha256") != sha_table:
        raise GardeArret(f"garde table-comparee : tokenisation.table_sha256 du rejeu {run} ≠ sceau de la table v4 versée "
                         f"({C4.TABLE_V4})")
    if not isinstance(table, dict) or table.get("resultat_reparation_sha256") != sha_rep:
        raise GardeArret(f"garde table-comparee : resultat_reparation_sha256 cité par la table v4 ({C4.TABLE_V4}) ≠ sceau "
                         f"du résultat de la réparation versé ({C4.RESULTAT_REPARATION_V4})")
    # provenance : addendum de la table à l'identique (V4-E14) et commande du rejeu
    if tk.get("addendum") != C4.ADDENDUM_V4["chemin"]:
        raise GardeArret(f"garde provenance : tokenisation.addendum du rejeu {run} ≠ {C4.ADDENDUM_V4['chemin']} (V4-E14)")
    if m.get("commande") != C4.COMMANDE_REJEU_V4:
        raise GardeArret(f"garde provenance : commande du manifeste du rejeu {run} ≠ « {C4.COMMANDE_REJEU_V4} »")
    return {"run_rejeu": run, "manifeste_sha256": sha_m, "texte": m["preenregistrement"], "commande": m["commande"],
            "table": {"chemin": C4.TABLE_V4, "sha256": sha_table},
            "reparation": {"chemin": C4.RESULTAT_REPARATION_V4, "sha256": sha_rep},
            "tokenisation": {"addendum": tk["addendum"], "table_sha256": tk["table_sha256"]}}
