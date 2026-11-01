#!/usr/bin/env python3
"""Assemble le pilote v4 complet (racine d'essai gelée 20264201 / 20264202) à partir des deux lancements disjoints du
même code (`…-instances-00-05.json`, `…-instances-05-24.json`) en un seul fichier JSON NOUVEAU (R12), avec l'analyse
recalculée sur l'union par `analyser` du code v4. Aucune tâche n'est recalculée : chaque tâche ne dépend que de
(racine, δ, instance) ; l'union est identique au bit à un lancement unique.

Gardes : les deux parties sont chargées par `charger_tous` de `calcul-puissance-arene-melange-v4.py` (racines d'essai
permises, configuration et empreinte du code identiques à celles du code v4 remis, instances disjointes) ; on exige en
plus 24 instances × 2 δ, sans trou ; la sortie ne doit pas exister.

    PYTHONPATH=src python3 assembler-pilote-arene-melange-v4.py SORTIE.json PARTIE1.json PARTIE2.json

Rédacteur de reprise (Opus, lignée conv-audit), 1er novembre 2026.
"""
from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path

ICI = Path(__file__).resolve().parent
sys.path.insert(0, str(ICI))
import arene_melange_v4 as am  # noqa: E402
from controle_ia.gardes import GardeArret  # noqa: E402

_spec = importlib.util.spec_from_file_location("puissance_v4", ICI / "calcul-puissance-arene-melange-v4.py")
puissance = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(puissance)


def main(argv: list[str]) -> int:
    if len(argv) < 3:
        raise GardeArret("usage : SORTIE.json PARTIE1.json PARTIE2.json …")
    sortie = am._exiger_absent(Path(argv[0]))
    corps = puissance.charger_tous(argv[1:])
    res = corps["resultats"]
    attendu = {(i, cd) for i in range(24) for cd in (1, 2)}
    if {(r["instance"], r["code_delta"]) for r in res} != attendu:
        raise GardeArret("pilote v4 incomplet : 24 instances × 2 δ exigées")
    man = dict(corps["manifeste"])
    man["commande_assemblage"] = " ".join(sys.argv)
    man["code_assemblage_sha256"] = am.empreinte_fichier(__file__)
    res = sorted(res, key=lambda r: (r["code_delta"], r["instance"]))
    sortie_corps = {"mode": "essai", "oracle": "detection", "assemblage": True, "manifeste": man,
                    "parties": corps["parties"], "temps": corps["temps"],
                    "analyse": am.analyser(res, man["racine"]), "resultats": res}
    am._ecrire_nouveau(sortie, sortie_corps)
    print(f"pilote assemblé écrit : {sortie} ; {len(res)} tâches ; {am.empreinte_fichier(sortie)}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
