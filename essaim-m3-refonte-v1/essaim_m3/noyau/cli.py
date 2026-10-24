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

from . import boucle, confrontation, contrat, recherche, taches
from .appels import Arret

MISSION_DEFAUT = pathlib.Path(__file__).resolve().parent.parent.parent / "MISSION-v1.md"


def _lire_mission(chemin: str | None) -> str:
    p = pathlib.Path(chemin) if chemin else MISSION_DEFAUT
    return p.read_text(encoding="utf-8")


def _budget(args) -> dict:
    return {"appels_max": args.appels_max, "usd_max": args.usd_par_generation, "temps_max_s": args.temps_max,
            "recherches_max": args.recherches_max}


def _organismes_imposes(args) -> dict:
    """`--organisme-impose NOM=CHEMIN@FAMILLE` (répétable) : lignées dont la génération 0 est fournie, pas écrite
    par une espèce (par exemple l'essaim de Gemini corrigé, ou l'organisme écrit par Gemini sous contrat)."""
    sortie = {}
    for spec in args.organisme_impose or []:
        if "=" not in spec or "@" not in spec.split("=", 1)[1]:
            raise SystemExit(f"--organisme-impose attend NOM=CHEMIN@FAMILLE, reçu : {spec!r}")
        nom, reste = spec.split("=", 1)
        chemin, famille = reste.rsplit("@", 1)
        nom = nom.strip().lower()
        if not nom or not pathlib.Path(chemin).is_dir():
            raise SystemExit(f"--organisme-impose : nom vide ou dossier introuvable : {spec!r}")
        if nom in sortie:
            raise SystemExit(f"--organisme-impose : nom en double : {nom!r}")
        sortie[nom] = {"organisme": str(pathlib.Path(chemin).resolve()), "famille": famille.strip().lower()}
    return sortie


def _imposes_et_especes(args, imposes: dict) -> tuple[dict, list | None]:
    """Bras gelé apparié (CR-08) : `--gel --depuis COURSE` relance les organismes g000 de cette course, sans amorçage."""
    if args.depuis:
        if not args.gel:
            raise SystemExit("--depuis exige --gel (bras gelé apparié à une course adaptative)")
        g000 = boucle.organismes_g000(args.depuis, pathlib.Path(args.sortie) / "g000-depuis")
        for nom, spec in g000.items():
            if nom in imposes:
                raise SystemExit(f"--depuis : la lignée {nom!r} est aussi donnée par --organisme-impose")
            imposes[nom] = spec
        return imposes, []  # aucune espèce n'amorce : les lignées sont celles de la course d'origine
    return imposes, args.especes


def simuler(args) -> int:
    from ..simulateur import appelants_simules
    ss = np.random.SeedSequence(args.graine)
    rng_banque, rng_especes = (np.random.default_rng(s) for s in ss.spawn(2))
    if args.depuis:
        banque = json.loads((pathlib.Path(args.depuis) / "banque.json").read_text(encoding="utf-8"))  # même banque que la course d'origine
    else:
        banque = taches.banque_simulation(rng_banque, args.n_train, args.n_test, args.n_final)
    options = {"commun": {"organisme_amorcage": args.organisme_amorcage} if args.organisme_amorcage else {}}
    appelants, _ = appelants_simules(rng_especes, **options)
    imposes, especes = _imposes_et_especes(args, _organismes_imposes(args))
    noyau = boucle.Noyau(args.sortie, _lire_mission(args.mission), banque, _budget(args), args.plafond_total,
                         args.generations, appelants=appelants, reel=False, entropie=int(ss.entropy),
                         especes_amorcage=especes, isoler_reseau=args.isoler_reseau, etiquette_run="simulation", gel=args.gel,
                         organismes_imposes=imposes, parallele_max=args.parallele_max,
                         recherche=recherche.recherche_simulee, relances_max=args.relances_max)
    amorcage = noyau.amorcer()
    rapport = noyau.boucler()
    if args.confronter:
        conf = confrontation.Confrontation(noyau, pathlib.Path(args.sortie) / "confrontation").confronter()
        rapport["confrontation"] = {"paires": [{k: p.get(k) for k in ("attaquant", "defendeur", "applicable", "n_attaques", "score_attaques", "metrique")} for p in conf["paires"]]}
    print(json.dumps({"amorcage": {k: v["statut"] for k, v in amorcage.items()}, "lignees": {l: {"famille": e.get("famille"), "impose": e.get("impose")} for l, e in noyau.lignees.items()},
                      "courbes": rapport["courbes"],
                      "scores_finaux": rapport["scores_finaux"], "depense_usd": rapport["depense_totale_usd"],
                      "n_appels": rapport["n_appels_total"]}, ensure_ascii=False, indent=1))
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
    if not (hasattr(os, "geteuid") and os.geteuid() == 0):
        print("refus : le mode réel exige d'être root pour faire tourner chaque organisme sous un utilisateur non privilégié distinct (CR-01)", file=sys.stderr)
        return 5
    try:
        os.chmod(args.taches, 0o600)  # la banque (avec ses vérités) n'est lisible que par le noyau
    except OSError as e:
        print(f"refus : impossible de protéger le fichier de tâches : {e}", file=sys.stderr)
        return 5
    from ..banque import verifier_banque
    problemes = verifier_banque(pathlib.Path(args.taches))
    if problemes:
        print("refus : banque de tâches non conforme :\n  - " + "\n  - ".join(problemes), file=sys.stderr)
        return 6
    banque = json.loads(pathlib.Path(args.taches).read_text(encoding="utf-8"))
    try:
        imposes, especes = _imposes_et_especes(args, _organismes_imposes(args))
        noyau = boucle.Noyau(args.sortie, _lire_mission(args.mission), banque, _budget(args), args.plafond_total,
                             args.generations, appelants=None, reel=True, go_id=args.go, isoler_reseau=args.isoler_reseau,
                             entropie=args.graine, especes_amorcage=especes, etiquette_run="reel", gel=args.gel,
                             organismes_imposes=imposes, parallele_max=args.parallele_max,
                             recherche=None, relances_max=args.relances_max, registre_go=args.registre_go)
    except Arret as e:
        print(f"refus : {e}", file=sys.stderr)
        return 7
    noyau.amorcer()
    rapport = noyau.boucler()
    if args.confronter:
        confrontation.Confrontation(noyau, pathlib.Path(args.sortie) / "confrontation").confronter()
    print(json.dumps({"courbes": rapport["courbes"], "scores_finaux": rapport["scores_finaux"], "depense_usd": rapport["depense_totale_usd"]}, ensure_ascii=False, indent=1))
    return 0


def extraire_metriques(args) -> int:
    """Relevé des métriques d'une course finie, sans lecture de score ; à geler (compagnon .sha256, contre-lecture)."""
    noyau = boucle.Noyau.recharger(args.course, appelants={}, reel=False)
    r = confrontation.relever_metriques(noyau, pathlib.Path(args.course) / "confrontation")
    print(json.dumps({k: v for k, v in r.items() if k != "course"}, ensure_ascii=False, indent=1))
    return 0


def confronter(args) -> int:
    """Confrontation d'une course finie, avec un relevé gelé : une métrique qui a changé depuis le relevé n'est ni
    exécutée ni attaquée."""
    addendum = json.loads(pathlib.Path(args.metriques_gelees).read_text(encoding="utf-8"))
    compagnon = pathlib.Path(args.metriques_gelees + ".sha256")
    if not compagnon.exists():
        print("refus : l'addendum gelé doit avoir son compagnon .sha256", file=sys.stderr)
        return 3
    import hashlib
    if compagnon.read_text(encoding="utf-8").split()[0] != hashlib.sha256(pathlib.Path(args.metriques_gelees).read_bytes()).hexdigest():
        print("refus : l'addendum ne correspond pas à son empreinte", file=sys.stderr)
        return 3
    if args.reel:
        if not args.go or not args.registre_go:
            print("refus : confrontation réelle sans GO ou sans extrait du registre des GO", file=sys.stderr)
            return 3
        noyau = boucle.Noyau.recharger(args.course, appelants=None, reel=True, go_id=args.go, registre_go=args.registre_go, isoler_reseau=True)
    else:
        from ..simulateur import appelants_simules
        appelants, _ = appelants_simules(np.random.default_rng(args.graine), **({"commun": {"organisme_amorcage": args.organisme_amorcage}} if args.organisme_amorcage else {}))
        noyau = boucle.Noyau.recharger(args.course, appelants=appelants, reel=False)
    rapport = confrontation.Confrontation(noyau, pathlib.Path(args.course) / "confrontation", addendum=addendum).confronter()
    print(json.dumps({"addendum_gele": rapport["addendum_gele"], "paires": [{k: p.get(k) for k in ("attaquant", "defendeur", "applicable", "n_attaques", "score_attaques", "metrique")} for p in rapport["paires"]]},
                     ensure_ascii=False, indent=1, default=str))
    return 0


def principal(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(prog="essaim_m3", description="Noyau de l'essaim autonome (refonte v1)")
    sp = p.add_subparsers(dest="commande", required=True)
    e = sp.add_parser("extraire-metriques", help="relevé des métriques d'une course finie, sans lecture de score (à geler)")
    e.add_argument("--course", required=True)
    e.set_defaults(fonction=extraire_metriques)
    c = sp.add_parser("confronter", help="confrontation d'une course finie avec un relevé gelé")
    c.add_argument("--course", required=True)
    c.add_argument("--metriques-gelees", required=True, help="relevé gelé (JSON + .sha256)")
    c.add_argument("--reel", action="store_true")
    c.add_argument("--go", default=None)
    c.add_argument("--registre-go", default=None)
    c.add_argument("--graine", type=int, default=None)
    c.add_argument("--organisme-amorcage", default=None)
    c.set_defaults(fonction=confronter)
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
        q.add_argument("--gel", action="store_true", help="bras témoin : relance la génération 0, ignore les successeurs")
        q.add_argument("--depuis", default=None, metavar="COURSE", help="avec --gel : relance les organismes g000 archivés de cette course (bras gelé apparié, CR-08) ; même banque")
        q.add_argument("--confronter", action="store_true", help="après la boucle : métriques croisées et attaques entre lignées de familles différentes")
        q.add_argument("--organisme-impose", action="append", default=None, metavar="NOM=CHEMIN@FAMILLE",
                       help="lignée dont la génération 0 est fournie (dossier organisme/) ; famille de fournisseur déclarée (anthropic|gemini) ; répétable")
        q.add_argument("--parallele-max", type=int, default=8, help="appels aux espèces servis en parallèle au plus (défaut 8)")
        q.add_argument("--recherches-max", type=int, default=20, help="recherches documentaires servies par le noyau, par génération (0 : aucune) ; arXiv en réel, double en simulation")
        q.add_argument("--relances-max", type=int, default=1, help="relances consécutives de la dernière génération valide quand le successeur est invalide (0 : lignée arrêtée)")
        if nom == "simuler":
            q.add_argument("--n-train", type=int, default=24)
            q.add_argument("--n-test", type=int, default=24)
            q.add_argument("--n-final", type=int, default=0, help="tâches du test final (jamais rendu aux organismes)")
            q.add_argument("--organisme-amorcage", default=None, help="dossier contenant organisme/ servi par les espèces simulées")
            q.set_defaults(fonction=simuler)
        else:
            q.add_argument("--reel", action="store_true")
            q.add_argument("--go", default=None)
            q.add_argument("--taches", required=True, help="fichier JSON préenregistré {train, test, test_final}")
            q.add_argument("--registre-go", default=None, help="extrait de registres/go.md contenant la ligne du GO (type « calcul ») ; exigé en réel")
            q.set_defaults(fonction=lancer)
    args = p.parse_args(argv)
    for e in getattr(args, "especes", None) or []:
        if e not in contrat.ESPECES_DISPONIBLES:
            print(f"espèce inconnue : {e}", file=sys.stderr)
            return 2
    return args.fonction(args)
