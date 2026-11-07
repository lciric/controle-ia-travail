"""Chaîne de session de T0.6, v8 (lanceur v9, R-1692 ; nom neuf, R12 : `session_v7.py` et les précédents restent tels quels).

Seule différence avec `session_v7.py` : **le stockage n'est plus compté deux fois** (défaut E2-2 de l'épreuve du 7 novembre). Avec
`vastai search offers … --storage <Go>`, la clé `dph_total` de l'offre INCLUT déjà le stockage demandé (`storage_total_cost`). Les v2 à v7
lisaient `prix_carte = dph_total` puis ajoutaient `prix_stockage = storage_total_cost` : 0,4034 USD/h estimés contre 0,362 facturés
(valeurs réelles : dph_total 0,3617, storage_total_cost 0,041667 ; carte seule 0,320 + disque 0,042). La v8 rend
`prix_carte = dph_total − storage_total_cost` et `prix_stockage = storage_total_cost` : la somme que lisent la garde de dépense et la
surveillance est exactement `dph_total`. Le tri des offres se fait aussi sur `dph_total` seul (avant : `dph_total + storage_total_cost`).
Le plafond horaire de la configuration (`prix_max_usd_h`) reste vérifié sur `dph_total`, comme avant (lecture prudente, inchangée).
Une offre dont `dph_total − storage_total_cost` n'est pas strictement positif est refusée (carte sans prix lisible).

    python -I -m controle_ia.t06.session_v8 choisir OFFRES.json CONFIG.json CARTE [MACHINES_EXCLUES]   (comme la v7, prix corrigés)
    autres sous-commandes : celles de `session_v7`.
"""
from __future__ import annotations

import sys

from . import session_v2 as s2
from . import session_v7 as s7
from .session import GardeSession

CUDA_MAX_GOOD_MIN = s7.CUDA_MAX_GOOD_MIN


def corriger_prix(r: dict) -> dict:
    """`dph_total` (lu dans `prix_carte` par `verifier_offre`) inclut déjà le stockage : on le sépare."""
    total, sto = float(r["prix_carte"]), float(r["prix_stockage"])
    carte = total - sto
    if not (carte > 0):
        raise GardeSession(f"offre {r['id']} : dph_total {total} − stockage {sto} = {carte} USD/h, carte sans prix lisible")
    r = dict(r)
    r["prix_carte"], r["dph_total"] = carte, total
    return r


def choisir_offre(offres, config: dict, carte: str, machines_exclues=()) -> dict:
    if isinstance(offres, dict) and "offers" in offres:
        offres = offres["offers"]
    if not isinstance(offres, list):
        raise GardeSession("liste d'offres illisible")
    if not offres:
        raise GardeSession("recherche filtrée : liste VIDE (aucune offre ne respecte le filtre)")
    exclues = {str(m) for m in machines_exclues}

    def cle(o):
        try:
            return (float(o.get("dph_total", 1e9)), int(o.get("id", 0)))
        except (TypeError, ValueError):
            return (1e18, 0)
    refus = []
    for rang, o in enumerate(sorted((o for o in offres if isinstance(o, dict)), key=cle), 1):
        if str(o.get("machine_id")) in exclues:
            refus.append(f"rang {rang} : machine {o.get('machine_id')} déjà refusée")
            continue
        try:
            cuda = float(o["cuda_max_good"])
        except (KeyError, TypeError, ValueError):
            refus.append(f"rang {rang} : cuda_max_good absent ou illisible (garde locale)")
            continue
        if cuda < CUDA_MAX_GOOD_MIN:
            refus.append(f"rang {rang} : cuda_max_good {cuda} < {CUDA_MAX_GOOD_MIN} (pilote trop ancien pour torch cu130)")
            continue
        try:
            r = corriger_prix(s2.verifier_offre([o], config, carte))
        except GardeSession as e:
            refus.append(f"rang {rang} : {e}")
            continue
        r["rang"] = rang
        r["cuda_max_good"] = cuda
        return r
    raise GardeSession(f"aucune offre conforme sur {len(offres)} : " + " ; ".join(refus[:3]))


def main(argv: list[str]) -> int:
    if len(argv) in (4, 5) and argv[0] == "choisir":
        try:
            r = choisir_offre(s2._lire_json(argv[1]), s2._lire_json(argv[2]), argv[3], argv[4].split(",") if len(argv) == 5 and argv[4] else ())
        except GardeSession as e:
            print(str(e))
            return 1
        print(f"id={r['id']} rang={r['rang']} machine={r['machine_id']} prix_carte={r['prix_carte']:.6f} prix_stockage={r['prix_stockage']:.6f} "
              f"dph_total={r['dph_total']:.6f} telechargement={r['telechargement']:.4f} telechargement_forfait={r['telechargement_forfait_usd']:.4f} "
              f"cuda_max_good={r['cuda_max_good']} carte={r['carte']}")
        return 0
    return s7.main(argv)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
