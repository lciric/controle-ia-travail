"""Relance v4 de R1 : **garde de chaîne de la table v4** (point I1 de la contre-lecture R2 `contre-lecture-relance-v4-v1.md`,
`e224ae8a…` ; écart V4-E5 de l'addendum v4). Module neuf (R12) ; aucun fichier existant n'est modifié.

L'empreinte de la table v4 n'est pas citée d'avance : elle est la sortie d'un code scellé (`resolution_graine_lot_v3.
construire_table_v4`) appliqué à des pièces scellées. La seule liberté qui resterait à une table qui passe les gardes du
rejeu (chaque correction revérifiée par l'empreinte de P3) est **l'ensemble de ses entrées `non_resolu`** : une
retrouvée rétrogradée en `non_resolu` passerait le chargement du rejeu v4. Ce module ferme cette liberté.

- `exiger_chaine` (session 2, entre l'étape « table-v4 » et le rejeu, avant toute reconstruction ; et à la réception) :
  résultat de la réparation scellé, rattaché à son manifeste, même configuration, étape et version de
  `resolution_graine_lot_v3`, sans `arret.json` ; table v4 scellée (version 4, formes, aucun doublon :
  `resolution_graine_lot_v2.charger_table_v4`, chargeur du rejeu v4) ; `resultat_reparation_sha256` de la table = sceau
  du résultat ; table v3 citée la même ; entrées hors des cibles = les 22 entrées de la table v3 citée, à l'identique ;
  une entrée par cible ; entrées « identifiants » = **exactement** les retrouvées du résultat (`empreinte_retrouvee`),
  avec ses identifiants action par action et le sceau du résultat ; entrées `non_resolu` = **exactement** les non
  retrouvées ; `non_resolus_v4` et comptes égaux. Tout écart : `GardeArret` (le script arrête la session avant le
  rejeu : rien n'est lu).
- `recalculer_a_la_reception` (réception, processeur) : la chaîne, puis la table recalculée par `construire_table_v4`
  (même configuration, résultat versé) doit égaler **à l'octet** la table versée (`octets_de_table`, sérialisation de
  `ecrire_table_v4`).

    PYTHONPATH=src python -m controle_ia.runs_nuit.chaine_table_v4_v1 --config CONFIG_REPARATION \\
        --reparation diag/<run>/resolution-graine-lot-v3-reparation.json --table prereg/R1-table-tokenisation-v4.json
    … --reception --tokeniseur DOSSIER        (recalcul à l'octet, réception)

Aucun score, aucune activation, aucune sortie d'analyse n'est lu.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from ..gardes import GardeArret
from ..manifeste import lire_manifeste, verifier_resultat
from ..scellement import verifier
from . import resolution_graine_lot_v2 as rv2
from . import resolution_graine_lot_v3 as rv3
from . import resolution_graine_v1 as rg

VERSION = "chaine_table_v4_v1"
COMMANDE = "python -m controle_ia.runs_nuit.chaine_table_v4_v1"


def octets_de_table(table: dict) -> bytes:
    """Sérialisation exacte de `ecrire_table_v4` (clés triées, indentation 1, UTF-8, fin de ligne)."""
    return (json.dumps(table, sort_keys=True, ensure_ascii=False, indent=1) + "\n").encode("utf-8")


def exiger_chaine(racine, chemin_table, chemin_reparation, config: dict) -> dict:
    """Garde de chaîne (I1) ; rend un résumé (empreintes, comptes). Voir l'en-tête du module."""
    racine = Path(racine)
    rv3.exiger_config(config)
    corps = verifier_resultat(racine, chemin_reparation)
    m, _ = lire_manifeste(racine / "runs" / corps["run_id"] / "manifeste.json")
    if m["config_sha256"] != rv3.empreinte_config(config):
        raise GardeArret("chaîne : résultat de la réparation fait sous une autre configuration")
    if m.get("commande") != f"{rv3.COMMANDE} --etape {rv3.ETAPE_REPARATION}":
        raise GardeArret(f"chaîne : commande du manifeste {m.get('commande')!r} ≠ étape « reparation » de "
                         f"{rv3.VERSION}")
    r = corps["resultat"]
    if r.get("etape") != rv3.ETAPE_REPARATION or r.get("version") != rv3.VERSION:
        raise GardeArret(f"chaîne : résultat d'étape {r.get('etape')!r}, version {r.get('version')!r}")
    if (racine / "diag" / corps["run_id"] / "arret.json").exists():
        raise GardeArret(f"chaîne : réparation {corps['run_id']} arrêtée (arret.json)")
    sha_r = verifier(chemin_reparation)
    table_v3, sha_v3 = rv3.charger_table_v3_citee(config, racine)
    if r.get("table_v3_sha256") != sha_v3:
        raise GardeArret("chaîne : réparation faite sur une autre table v3 que celle de la configuration")
    table = rv2.charger_table_v4(chemin_table, None)
    sha_t = verifier(chemin_table)
    if table.get("resultat_reparation_sha256") != sha_r:
        raise GardeArret(f"chaîne : resultat_reparation_sha256 de la table "
                         f"{str(table.get('resultat_reparation_sha256'))[:12]} ≠ sceau du résultat de la réparation "
                         f"{sha_r[:12]}")
    if table.get("table_v3_sha256") != sha_v3:
        raise GardeArret("chaîne : table v4 bâtie sur une autre table v3")
    cibles = list(r.get("cibles") or [])
    par_r: dict = {}
    for x in r.get("episodes") or []:
        if x["episode"] in par_r:
            raise GardeArret(f"chaîne : {x['episode']} deux fois dans le résultat de la réparation")
        par_r[x["episode"]] = x
    if sorted(par_r) != sorted(cibles) or len(set(cibles)) != len(cibles):
        raise GardeArret("chaîne : épisodes du résultat de la réparation ≠ ses cibles")
    retrouvees = {e for e, x in par_r.items() if x.get("empreinte_retrouvee") is True}
    non_retrouvees = set(cibles) - retrouvees
    par_t = {x["episode"]: x for x in table["episodes"]}
    hors = [x for x in table["episodes"] if x["episode"] not in set(cibles)]
    if hors != list(table_v3["episodes"]):
        raise GardeArret("chaîne : entrées hors des cibles ≠ entrées de la table v3 citée (à l'identique, dans l'ordre)")
    manquantes = sorted(set(cibles) - set(par_t))
    if manquantes:
        raise GardeArret(f"chaîne : cibles sans entrée dans la table v4 : {manquantes[:3]}")
    ident = {e for e in cibles if par_t[e]["methode"] != "non_resolu"}
    nonr = {e for e in cibles if par_t[e]["methode"] == "non_resolu"}
    if ident != retrouvees:
        raise GardeArret(f"chaîne : entrées « identifiants » ≠ retrouvées du résultat (en moins : "
                         f"{sorted(retrouvees - ident)[:3]}, en trop : {sorted(ident - retrouvees)[:3]})")
    if nonr != non_retrouvees:
        raise GardeArret(f"chaîne : entrées « non_resolu » ≠ non retrouvées du résultat (en moins : "
                         f"{sorted(non_retrouvees - nonr)[:3]}, en trop : {sorted(nonr - non_retrouvees)[:3]})")
    for e in sorted(ident):
        ent, x = par_t[e], par_r[e]
        if ent["methode"] != rg.METHODE_IDENTIFIANTS:
            raise GardeArret(f"chaîne : {e} : méthode {ent['methode']!r} ≠ « {rg.METHODE_IDENTIFIANTS} »")
        if ent.get("trajectoire_p3") != x.get("empreinte_cible") or x.get("empreinte") != x.get("empreinte_cible"):
            raise GardeArret(f"chaîne : {e} : empreinte de l'entrée ≠ empreinte retrouvée du résultat")
        if (ent.get("resolution_graine") or {}).get("resultat_sha256") != sha_r:
            raise GardeArret(f"chaîne : {e} : entrée qui ne cite pas le sceau du résultat de la réparation")
        ids = [[int(y) for y in a] for a in x["ids"]]
        for a in ent["actions"]:
            if not 0 <= int(a["pas"]) < len(ids) or [int(y) for y in a["p3"]] != ids[int(a["pas"])]:
                raise GardeArret(f"chaîne : {e} : identifiants de l'entrée (pas {a['pas']}) ≠ identifiants du résultat")
    if sorted(table.get("non_resolus_v4") or []) != sorted(non_retrouvees):
        raise GardeArret("chaîne : non_resolus_v4 ≠ non retrouvées du résultat")
    c = table.get("comptes") or {}
    if c.get("cibles_v4") != len(cibles) or c.get("retrouvees_v4") != len(retrouvees):
        raise GardeArret("chaîne : comptes cibles_v4 / retrouvees_v4 ≠ résultat de la réparation")
    return {"version": VERSION, "table": str(chemin_table), "table_sha256": sha_t, "reparation": str(chemin_reparation),
            "resultat_reparation_sha256": sha_r, "run_reparation": corps["run_id"], "table_v3_sha256": sha_v3,
            "cibles": len(cibles), "retrouvees": len(retrouvees), "non_retrouvees": len(non_retrouvees),
            "entrees_v3": len(hors)}


def recalculer_a_la_reception(config: dict, racine, tokeniseur: str | None, chemin_reparation, chemin_table,
                              fmt=None) -> dict:
    """Réception (I1 (d)) : la chaîne, puis la table recalculée sur processeur depuis le résultat versé, égale à l'octet à
    la table versée."""
    resume = exiger_chaine(racine, chemin_table, chemin_reparation, config)
    table = rv3.construire_table_v4(config, Path(racine), tokeniseur, str(chemin_reparation), fmt=fmt)
    if octets_de_table(table) != Path(chemin_table).read_bytes():
        raise GardeArret("réception : table v4 recalculée ≠ table versée (à l'octet)")
    return {**resume, "recalcul_egal_a_l_octet": True}


def _main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(prog=COMMANDE)
    ap.add_argument("--config", required=True, help="configuration de la réparation (scellée)")
    ap.add_argument("--reparation", required=True, help="résultat scellé de l'étape reparation")
    ap.add_argument("--table", required=True, help="table version 4 scellée")
    ap.add_argument("--reception", action="store_true", help="recalcul de la table à l'octet (réception)")
    ap.add_argument("--tokeniseur", default=None, help="dossier du tokeniseur à la révision de P3 (réception, réel)")
    a = ap.parse_args(argv)
    verifier(a.config)
    config = json.loads(Path(a.config).read_text(encoding="utf-8"))
    if a.reception:
        if config.get("mode") != "jouet" and not a.tokeniseur:
            raise GardeArret("réception en mode réel sans --tokeniseur")
        r = recalculer_a_la_reception(config, Path("."), a.tokeniseur, a.reparation, a.table)
    else:
        r = exiger_chaine(Path("."), a.table, a.reparation, config)
    print(json.dumps(r, ensure_ascii=False, sort_keys=True))
    return 0


if __name__ == "__main__":
    try:
        sys.exit(_main(sys.argv[1:]))
    except GardeArret as e:
        print(f"ARRÊT : {e}", file=sys.stderr)
        sys.exit(1)
