"""Entrée de commande du noyau.

- `simuler` : espèces simulées, organisme factice d'amorçage, juge en simulation ; aucun réseau, aucune clé.
- `lancer --reel` : espèces réelles ; exige un identifiant de GO (`registres/go.md`), les clés du programme dans
  l'environnement (`ANTHROPIC_API_KEY`, `GEMINI_API_KEY` ; jamais `RR_*`), un plafond total, un fichier de tâches
  préenregistré, et refuse de tourner en tant que root sans accord explicite (le bac à sable repose sur les
  permissions du système de fichiers).
"""
from __future__ import annotations

import argparse
import json
import os
import pathlib
import sys

import numpy as np

from . import boucle, contrat, taches
from .appels import Arret

MISSION_DEFAUT = pathlib.Path(__file__).resolve().parent.parent.parent / "MISSION-v1.md"


def _lire_mission(chemin: str | None) -> str:
    p = pathlib.Path(chemin) if chemin else MISSION_DEFAUT
    return p.read_text(encoding="utf-8")


def _budget(args) -> dict:
    return {"appels_max": args.appels_max, "usd_max": args.usd_par_generation, "temps_max_s": args.temps_max}


def simuler(args) -> int:
    from ..simulateur import appelants_simules
    ss = np.random.SeedSequence(args.graine)
    rng_banque, rng_especes = (np.random.default_rng(s) for s in ss.spawn(2))
    banque = taches.banque_simulation(rng_banque, args.n_train, args.n_test)
    options = {"commun": {"organisme_amorcage": args.organisme_amorcage} if args.organisme_amorcage else {}}
    appelants, _ = appelants_simules(rng_especes, **options)
    noyau = boucle.Noyau(args.sortie, _lire_mission(args.mission), banque, _budget(args), args.plafond_total,
                         args.generations, appelants=appelants, reel=False, entropie=int(ss.entropy),
                         especes_amorcage=args.especes, isoler_reseau=args.isoler_reseau, etiquette_run="simulation")
    amorcage = noyau.amorcer()
    rapport = noyau.boucler()
    print(json.dumps({"amorcage": {k: v["statut"] for k, v in amorcage.items()}, "courbes": rapport["courbes"],
                      "depense_usd": rapport["depense_totale_usd"], "n_appels": rapport["n_appels_total"]}, ensure_ascii=False, indent=1))
    return 0


def lancer(args) -> int:
    if not args.reel:
        print("mode réel non demandé : utilise `simuler`, ou `lancer --reel --go …`", file=sys.stderr)
        return 2
    if not args.go:
        print("refus : mode réel sans identifiant de GO (nœud de dépense, registres/go.md)", file=sys.stderr)
        return 3
    manquantes = [k for k in ("ANTHROPIC_API_KEY", "GEMINI_API_KEY") if not os.environ.get(k)]
    if manquantes:
        print(f"refus : clés absentes de l'environnement : {manquantes} (jamais de clé RR_*)", file=sys.stderr)
        return 4
    if hasattr(os, "geteuid") and os.geteuid() == 0 and not args.accepter_root:
        print("refus : exécution en root ; le bac à sable repose sur les permissions (relance avec --accepter-root en connaissance de cause)", file=sys.stderr)
        return 5
    banque = json.loads(pathlib.Path(args.taches).read_text(encoding="utf-8"))
    if not isinstance(banque, dict) or "train" not in banque or "test" not in banque:
        print("refus : le fichier de tâches doit contenir `train` et `test`", file=sys.stderr)
        return 6
    try:
        noyau = boucle.Noyau(args.sortie, _lire_mission(args.mission), banque, _budget(args), args.plafond_total,
                             args.generations, appelants=None, reel=True, go_id=args.go, isoler_reseau=args.isoler_reseau,
                             entropie=args.graine, especes_amorcage=args.especes, etiquette_run="reel")
    except Arret as e:
        print(f"refus : {e}", file=sys.stderr)
        return 7
    noyau.amorcer()
    rapport = noyau.boucler()
    print(json.dumps({"courbes": rapport["courbes"], "depense_usd": rapport["depense_totale_usd"]}, ensure_ascii=False, indent=1))
    return 0


def principal(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(prog="essaim_m3", description="Noyau de l'essaim autonome (refonte v1)")
    sp = p.add_subparsers(dest="commande", required=True)
    for nom in ("simuler", "lancer"):
        q = sp.add_parser(nom)
        q.add_argument("--sortie", required=True)
        q.add_argument("--mission", default=None)
        q.add_argument("--generations", type=int, default=3)
        q.add_argument("--appels-max", type=int, default=60)
        q.add_argument("--usd-par-generation", type=float, default=5.0)
        q.add_argument("--temps-max", type=int, default=600)
        q.add_argument("--plafond-total", type=float, default=10.0)
        q.add_argument("--graine", type=int, default=None)
        q.add_argument("--especes", nargs="*", default=None, help="espèces d'amorçage (défaut : les trois)")
        q.add_argument("--isoler-reseau", action="store_true")
        if nom == "simuler":
            q.add_argument("--n-train", type=int, default=24)
            q.add_argument("--n-test", type=int, default=24)
            q.add_argument("--organisme-amorcage", default=None, help="dossier contenant organisme/ servi par les espèces simulées")
            q.set_defaults(fonction=simuler)
        else:
            q.add_argument("--reel", action="store_true")
            q.add_argument("--go", default=None)
            q.add_argument("--taches", required=True, help="fichier JSON préenregistré {train, test}")
            q.add_argument("--accepter-root", action="store_true")
            q.set_defaults(fonction=lancer)
    args = p.parse_args(argv)
    for e in args.especes or []:
        if e not in contrat.ESPECES_DISPONIBLES:
            print(f"espèce inconnue : {e}", file=sys.stderr)
            return 2
    return args.fonction(args)
