"""Entrée de commande du noyau.

- `simuler` : espèces simulées, organisme factice d'amorçage, juge en simulation ; aucun réseau, aucune clé.
- `lancer --reel` : espèces réelles ; exige un identifiant de GO (`registres/go.md`), les clés du programme dans
  l'environnement (`ANTHROPIC_API_KEY`, `GEMINI_API_KEY` : noms que le lanceur remplit, GO-2026-10-24-04), un plafond total, un fichier de tâches
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
            "recherches_max": args.recherches_max, "telechargements_max": args.telechargements_max, "octets_max": args.octets_max,
            "entrainements_max": args.entrainements_max, "pas_max": args.pas_max, "delai_entrainement_s": args.delai_entrainement,
            "max_tokens_appel": args.max_tokens_appel}


def _budget_conception(args) -> dict | None:
    """Budget d'une ronde de conception : celui d'une génération, sauf les plafonds donnés à part."""
    if not getattr(args, "rondes_conception_max", 0):
        return None
    b = _budget(args)
    if getattr(args, "usd_max_conception", None) is not None:
        b["usd_max"] = args.usd_max_conception
    if getattr(args, "appels_max_conception", None) is not None:
        b["appels_max"] = args.appels_max_conception
    if getattr(args, "temps_max_conception", None) is not None:
        b["temps_max_s"] = args.temps_max_conception
    return b


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
    """`--depuis COURSE` relance les organismes g000 de cette course (mêmes empreintes), sans amorçage. Avec `--gel` :
    bras gelé apparié (CR-08 : génération 0 relancée, sans mémoire). Sans `--gel` : bras apparié adaptatif (CE-06,
    étape 1) — même organisme de départ, boucle et mémoire ordinaires ; seul ce que la ligne de commande change (par
    exemple `--entrainements-max 0`) diffère de la course d'origine."""
    if args.depuis:
        if getattr(args, "rondes_conception_max", 0):
            raise SystemExit("--depuis : le bras apparié part de la génération 0 de la course d'origine, issue de sa phase de "
                             "conception ; pas de nouvelle conception (--rondes-conception-max doit valoir 0)")
        g000 = boucle.organismes_g000(args.depuis, pathlib.Path(args.sortie) / "g000-depuis")
        for nom, spec in g000.items():
            if nom in imposes:
                raise SystemExit(f"--depuis : la lignée {nom!r} est aussi donnée par --organisme-impose")
            imposes[nom] = spec
        return imposes, []  # aucune espèce n'amorce : les lignées sont celles de la course d'origine
    return imposes, args.especes


def _vivier(args, banque: dict):
    """Vivier de conception (`--pool-conception`) : refusé avec `--depuis` (le bras apparié n'a pas de rondes ; il importe
    la mémoire de conception de sa course d'origine, CE3-01) et sans phase de conception ; chargé et gardé par
    `vivier.charger_vivier` (compagnon, format, disjonction par le contenu)."""
    if not getattr(args, "pool_conception", None):
        return None
    if args.depuis:
        raise Arret("--pool-conception avec --depuis : refusé (le bras apparié n'a pas de phase de conception)")
    if not args.rondes_conception_max:
        raise Arret("--pool-conception sans --rondes-conception-max : refusé (le vivier ne sert qu'en conception)")
    from .vivier import VivierRefuse, charger_vivier
    try:
        return charger_vivier(args.pool_conception, banque)
    except VivierRefuse as e:
        raise Arret(f"vivier de conception : {e}")


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
    try:
        vivier = _vivier(args, banque)
    except Arret as e:
        print(f"refus : {e}", file=sys.stderr)
        return 7
    noyau = boucle.Noyau(args.sortie, _lire_mission(args.mission), banque, _budget(args), args.plafond_total,
                         args.generations, appelants=appelants, reel=False, entropie=int(ss.entropy), vivier=vivier,
                         especes_amorcage=especes, isoler_reseau=args.isoler_reseau, etiquette_run="simulation", gel=args.gel,
                         organismes_imposes=imposes, parallele_max=args.parallele_max,
                         recherche=recherche.recherche_simulee, relances_max=args.relances_max, memoire_partagee=args.memoire_partagee,
                         decalage_uid=args.decalage_uid,
                         rondes_conception_max=args.rondes_conception_max, budget_conception=_budget_conception(args))
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


def charger_traits(chemin, chemin_banque, banque: dict, vues_servies: list[str] | None = None) -> tuple[dict, str]:
    """Traits du mode réel. Un fichier `.npz` (ids, X) : une seule vue, « defaut ». Un dossier d'extraction
    (`extraire_activations_v2.py` : `manifeste-traits.json` et `traits-<vue>.npz`, chacun avec son `.sha256`) : une vue
    par fichier, chaque empreinte vérifiée contre le manifeste et le compagnon, la banque du manifeste égale à la banque
    de la course, toutes les tâches présentes, nombres finis ; `vues_servies` restreint la liste (le préenregistrement
    la fixe). Toute anomalie lève ValueError : aucun repli."""
    import hashlib as _h
    import numpy as _np

    def empreinte(f: pathlib.Path) -> str:
        return _h.sha256(f.read_bytes()).hexdigest()

    def compagnon(f: pathlib.Path) -> None:
        c = f.with_name(f.name + ".sha256")
        if not c.is_file() or c.read_text(encoding="utf-8").split()[:1] != [empreinte(f)]:
            raise ValueError(f"{f.name} : compagnon d'empreinte absent ou différent")

    attendus = {str(t["id"]) for n in ("train", "test", "test_final") for t in banque.get(n, [])}
    p = pathlib.Path(chemin)

    def lire(f: pathlib.Path, forme=None) -> dict:
        d = _np.load(f, allow_pickle=False)
        ids, X = [str(i) for i in d["ids"]], _np.asarray(d["X"], dtype=_np.float32)
        if len(set(ids)) != len(ids) or X.ndim != 2 or X.shape[0] != len(ids):
            raise ValueError(f"{f.name} : identifiants en double ou forme illisible")
        if forme is not None and list(X.shape) != list(forme):
            raise ValueError(f"{f.name} : forme {list(X.shape)} ≠ manifeste {list(forme)}")
        if not _np.all(_np.isfinite(X)):
            raise ValueError(f"{f.name} : traits non finis")
        manquants = attendus - set(ids)
        if manquants:
            raise ValueError(f"{f.name} : {len(manquants)} tâche(s) de la banque sans traits, dont {sorted(manquants)[:3]}")
        return dict(zip(ids, X))

    if p.is_file():
        traits = lire(p)
        return traits, f"traits chargés de {p.name} ({len(traits)} tâches, vue « defaut »)"
    if not p.is_dir():
        raise ValueError(f"{p} : ni fichier ni dossier")
    fm = p / "manifeste-traits.json"
    if not fm.is_file():
        raise ValueError("dossier sans manifeste-traits.json")
    compagnon(fm)
    m = json.loads(fm.read_text(encoding="utf-8"))
    if m.get("factice"):
        raise ValueError("traits factices (--factice) : refusés en réel")
    if m.get("sha256_banque") != empreinte(pathlib.Path(chemin_banque)):
        raise ValueError("la banque du manifeste n'est pas celle de la course (empreintes différentes)")
    fichiers = m.get("fichiers") or {}
    noms = sorted(fichiers) if vues_servies is None else list(vues_servies)
    inconnues = [v for v in noms if v not in fichiers]
    if not noms or inconnues:
        raise ValueError(f"vues demandées absentes du manifeste : {inconnues or 'aucune vue'} ; vues du manifeste : {sorted(fichiers)}")
    vues = {}
    for nom in noms:
        f = p / f"traits-{nom}.npz"
        if not f.is_file() or empreinte(f) != fichiers[nom].get("sha256"):
            raise ValueError(f"traits-{nom}.npz : absent ou empreinte différente du manifeste")
        compagnon(f)
        vues[nom] = lire(f, fichiers[nom].get("forme"))
    return vues, (f"activations de {m.get('modele')} (révision {m.get('revision')}), {len(noms)} vue(s), "
                  f"≤ {m.get('max_jetons')} jetons, {m.get('n_tronquees')} tâche(s) tronquée(s) ; manifeste {empreinte(fm)[:12]}…")


def conditions_moisson_differentes(course_origine: pathlib.Path, recherches_max: int) -> str | None:
    """CE3-05 : le bras apparié doit avoir les mêmes sources de moisson et la même présence de la clé Brave que sa course
    d'origine (consignées au manifeste) ; rend la différence, ou None."""
    m = json.loads((course_origine / "manifeste-run.json").read_text(encoding="utf-8"))
    brave = bool(os.environ.get("BRAVE_API_KEY"))
    if "cle_brave_presente" in m and bool(m["cle_brave_presente"]) != brave:
        return f"clé Brave {'présente' if brave else 'absente'} ici, {'présente' if m['cle_brave_presente'] else 'absente'} dans la course d'origine"
    if recherches_max > 0 and "sources_moisson" in m:
        from . import moisson as _moisson
        ici = sorted(n for n in _moisson.sources_disponibles() if n != "web" or brave)
        if sorted(m["sources_moisson"]) != ici:
            return f"sources de moisson {ici} ici, {sorted(m['sources_moisson'])} dans la course d'origine"
    return None


def lancer(args) -> int:
    if not args.reel:
        print("mode réel non demandé : utilise `simuler`, ou `lancer --reel --go …`", file=sys.stderr)
        return 2
    if not args.go:
        print("refus : mode réel sans identifiant de GO (nœud de dépense, registres/go.md)", file=sys.stderr)
        return 3
    manquantes = [k for k in ("ANTHROPIC_API_KEY", "GEMINI_API_KEY") if not os.environ.get(k)]
    if manquantes:
        print(f"refus : clés absentes de l'environnement : {manquantes} (le lanceur passe la clé des runs sous ces noms : GO-2026-10-24-04)", file=sys.stderr)
        return 4
    if os.environ.get("ANTHROPIC_BASE_URL") and not args.autoriser_base_url:
        print("refus : ANTHROPIC_BASE_URL est définie (les appels partiraient ailleurs que vers l'interface d'Anthropic) ; retire-la de l'environnement du run, ou --autoriser-base-url en connaissance de cause", file=sys.stderr)
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
    if args.depuis:  # bras apparié : la banque de la course d'origine doit être la même (CE-06)
        origine = pathlib.Path(args.depuis) / "banque.json"
        if not origine.is_file() or json.loads(origine.read_text(encoding="utf-8")) != banque:
            print("refus : --depuis : la banque de la course d'origine n'est pas celle de --taches", file=sys.stderr)
            return 6
        refus_conditions = conditions_moisson_differentes(pathlib.Path(args.depuis), int(args.recherches_max))
        if refus_conditions:  # CE3-05 : conditions extérieures appariées entre les bras
            print(f"refus : --depuis : {refus_conditions}", file=sys.stderr)
            return 6
    traits, description = None, ""
    if args.traits:
        try:
            traits, description = charger_traits(args.traits, args.taches, banque, args.vues)
        except ValueError as e:
            print(f"refus : traits : {e}", file=sys.stderr)
            return 6
    try:
        imposes, especes = _imposes_et_especes(args, _organismes_imposes(args))
        vivier = _vivier(args, banque)
        noyau = boucle.Noyau(args.sortie, _lire_mission(args.mission), banque, _budget(args), args.plafond_total,
                             args.generations, appelants=None, reel=True, go_id=args.go, isoler_reseau=args.isoler_reseau, vivier=vivier,
                             entropie=args.graine, especes_amorcage=especes, etiquette_run="reel", gel=args.gel,
                             organismes_imposes=imposes, parallele_max=args.parallele_max,
                             recherche=None, relances_max=args.relances_max, traits=traits, description_traits=description,
                             registre_go=args.registre_go, memoire_partagee=args.memoire_partagee, decalage_uid=args.decalage_uid,
                             rondes_conception_max=args.rondes_conception_max, budget_conception=_budget_conception(args))
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
        q.add_argument("--depuis", default=None, metavar="COURSE", help="relance les organismes g000 archivés de cette course, même banque : avec --gel, bras gelé apparié (CR-08) ; sans --gel, bras apparié adaptatif (CE-06)")
        q.add_argument("--confronter", action="store_true", help="après la boucle : métriques croisées et attaques entre lignées de familles différentes")
        q.add_argument("--organisme-impose", action="append", default=None, metavar="NOM=CHEMIN@FAMILLE",
                       help="lignée dont la génération 0 est fournie (dossier organisme/) ; famille de fournisseur déclarée (anthropic|gemini) ; répétable")
        q.add_argument("--parallele-max", type=int, default=8, help="appels aux espèces servis en parallèle au plus (défaut 8)")
        q.add_argument("--recherches-max", type=int, default=20, help="recherches documentaires servies par le noyau, par génération (0 : aucune) ; arXiv en réel, double en simulation")
        q.add_argument("--telechargements-max", type=int, default=0, help="documents que le noyau rapporte à l'organisme par génération (moisson) ; 0 : non servi")
        q.add_argument("--octets-max", type=int, default=40_000_000, help="octets téléchargés au plus par génération")
        q.add_argument("--relances-max", type=int, default=1, help="relances consécutives de la dernière génération valide quand le successeur est invalide (0 : lignée arrêtée)")
        q.add_argument("--entrainements-max", type=int, default=10, help="entraînements par gradient servis par le noyau, par génération (0 : aucun)")
        q.add_argument("--pas-max", type=int, default=5000, help="pas de gradient au plus par entraînement")
        q.add_argument("--delai-entrainement", type=int, default=120, help="secondes au plus par entraînement (sous-processus isolé)")
        q.add_argument("--max-tokens-appel", type=int, default=None, help="plafond de jetons de sortie par appel d'organisme (le noyau rabat ce qui est demandé au-delà ; l'amorçage garde le maximum du modèle) ; défaut : aucun")
        q.add_argument("--traits", default=None, help="réel : dossier d'extraction (manifeste-traits.json, traits-<vue>.npz) ou fichier .npz (ids, X) — activations extraites sous GO ; simulation : traits de hachage calculés")
        q.add_argument("--vues", nargs="+", default=None, help="réel : vues servies (noms du manifeste, par exemple couche16-dernier) ; défaut : toutes")
        q.add_argument("--rondes-conception-max", type=int, default=0, help="phase de conception avant la génération 0 notée : borne dure du nombre de rondes (l'organisme déclare lui-même la fin par fin_conception.json) ; 0 : pas de phase")
        q.add_argument("--usd-max-conception", type=float, default=None, help="dollars par ronde de conception (défaut : --usd-max)")
        q.add_argument("--appels-max-conception", type=int, default=None, help="appels par ronde de conception (défaut : --appels-max)")
        q.add_argument("--temps-max-conception", type=int, default=None, help="secondes par ronde de conception (défaut : --temps-max)")
        q.add_argument("--autoriser-base-url", action="store_true", help="réel : accepte une ANTHROPIC_BASE_URL définie (sinon refus)")
        q.add_argument("--decalage-uid", type=int, default=0, help="décalage des utilisateurs des organismes (multiple de 100, 0 à 900) : distinct pour chaque course qui tourne en même temps qu'une autre (CE3-06)")
        q.add_argument("--pool-conception", default=None, metavar="FICHIER", help="vivier de conception : tâches à vérité connue (JSON du sous-ensemble, avec compagnon .sha256) servies en plus des tâches d'entraînement pendant la phase de conception seulement, jamais en génération notée ; identifiants opaques, textes bornés, items qui recoupent un texte de la banque écartés et comptés")
        q.add_argument("--memoire-partagee", action="store_true", help="les lignées lisent la vue de toutes les lignées, figée au début de chaque ronde (défaut : chaque lignée ne lit que la sienne, CR-15)")
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
