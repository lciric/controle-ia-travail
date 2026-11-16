#!/usr/bin/env python3
"""Lanceur du jeu de l'idée 1.1 (préenregistrement scellé `prereg/organisme-idee-1-1-poids-du-nul-v2.md`, `3ffe1739…`).
Processeur seul, sans dépense, aucun appel réseau ni de modèle (R-2851).

    python -I -B scripts/jouer_idee_1_1_v1.py --addendum CHEMIN_ADDENDUM             # jeu décisif (processus : addendum)
    python -I -B scripts/jouer_idee_1_1_v1.py --addendum CHEMIN_ADDENDUM --reprendre RUN_ID
    python -I -B scripts/jouer_idee_1_1_v1.py --miniature --sortie DOSSIER_HORS_DU_DEPOT [--lignes 0,25 --repetitions 2]
    python -I -B scripts/jouer_idee_1_1_v1.py --lister-empreintes

Ordre des gardes du jeu décisif : préenregistrement scellé et égal au texte (`exiger_prereg_scelle`) ; arbre propre ;
aucune sortie ni manifeste antérieur de ce jeu (sauf reprise du même run, sans arrêt consigné) ; addendum d'empreintes
scellé couvrant les fichiers gelés, avec son bloc programme (processus, réductions rejouées sur le fichier d'étape 0) ;
copies du juge et du v9 ; essais ; mutations rejouées ; manifeste (graines `SeedSequence` : racine = entier de
l'empreinte du texte ; clés `(i_ligne, r, 0)`, `(i_ligne, r, 1)`, `(98, r)`, `(99, b)`, `(97, k)`) ; jeu ; sortie scellée.
Aucune lecture.
"""
from __future__ import annotations

import os
import sys

for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ[_v] = "1"
sys.dont_write_bytecode = True

import argparse  # noqa: E402
import hashlib  # noqa: E402
import json  # noqa: E402
import signal  # noqa: E402
import subprocess  # noqa: E402
import time  # noqa: E402
from datetime import datetime, timezone  # noqa: E402
from pathlib import Path  # noqa: E402

RACINE_DEPOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RACINE_DEPOT / "src"))

from controle_ia.gardes import GardeArret, exiger_depot_propre, lever_sur_term  # noqa: E402
from controle_ia.manifeste import creer_manifeste, lire_manifeste  # noqa: E402
from controle_ia.prereg import exiger_prereg_scelle  # noqa: E402
from controle_ia.scellement import empreinte, verifier  # noqa: E402
from controle_ia.organisme_idees_juge import banc_idee_1_1_v1 as B  # noqa: E402
from controle_ia.organisme_idees_juge import execution_idee_1_1_v1 as X  # noqa: E402
from controle_ia.organisme_idees_juge import juge_v1  # noqa: E402
from controle_ia.organisme_idees_juge import mutations_idee_1_1_v1 as MU  # noqa: E402
from controle_ia.organisme_idees_juge import vue_v9_v1 as VV  # noqa: E402

RACINE_MINIATURE = B.racine_de(hashlib.sha256(b"repetition miniature, idee 1.1, v1 (racine d'essai, jamais celle du jeu)").hexdigest())
CLES_DE_CONTROLE = ((0, 0, 0), (0, 0, 1), (29, 999, 1), (98, 0), (99, 0), (97, 40, 0, 0))


def exiger_prereg(racine_depot: Path) -> str:
    sha = exiger_prereg_scelle(Path(racine_depot) / B.CHEMIN_PREREG)
    if sha != B.EMPREINTE_PREREG:
        raise GardeArret(f"préenregistrement {sha[:12]}… ≠ texte scellé attendu {B.EMPREINTE_PREREG[:12]}…")
    return sha


def exiger_sortie_absente(racine_depot: Path) -> None:
    for dossier, quoi in ((racine_depot / X.DOSSIER_DIAG, "une sortie"), (racine_depot / "runs", "un manifeste")):
        if dossier.is_dir():
            anciens = sorted(p.name for p in dossier.iterdir() if p.name.endswith(X.NOM_RUN))
            if anciens:
                raise GardeArret(f"{quoi} de ce jeu existe déjà ({anciens}) : relance seulement sous un texte ou un addendum "
                                 "neuf, ou reprise du même run (--reprendre)")


def etats_de_controle(racine: int) -> dict:
    return {str(c): B.etat_graine(racine, *c) for c in CLES_DE_CONTROLE}


def lancer_essais(racine_depot: Path) -> dict:
    env = {"PATH": os.environ.get("PATH", "/usr/bin:/bin"), "HOME": os.environ.get("HOME", "/tmp"), "PYTHONPATH": "src",
           "LANG": "C.UTF-8", "OMP_NUM_THREADS": "1", "OPENBLAS_NUM_THREADS": "1", "MKL_NUM_THREADS": "1"}
    t0 = time.time()
    r = subprocess.run([sys.executable, "-B", "-m", "pytest", "-q", "-p", "no:cacheprovider", *X.ESSAIS], cwd=racine_depot,
                       env=env, capture_output=True, text=True)
    if r.returncode != 0:
        raise GardeArret(f"un essai échoue : pas de jeu\n{r.stdout[-3000:]}\n{r.stderr[-2000:]}")
    return {"code": r.returncode, "fin": r.stdout[-1500:], "duree_s": round(time.time() - t0, 1)}


def config_du_jeu(racine: int, add: dict | None, copie: dict, processus: int, reductions, miniature: bool) -> dict:
    return {"objet": "idée 1.1 : poids du nul (projection par blocs, nuls limités, règles de lecture), banc B v2",
            "version_lanceur": 1, "preenregistrement": {"chemin": B.CHEMIN_PREREG, "sha256": B.EMPREINTE_PREREG},
            "racine_graines": str(racine),
            "origine_racine": "racine d'essai (miniature)" if miniature else "entier de l'empreinte sha256 du texte scellé",
            "cles_graines": {"avant_gel": "(i_ligne, r, 0)", "issues_fraiches": "(i_ligne, r, 1)", "E0": "(98, r)",
                             "reechantillonnage": "(99, b)", "essais_mutations_chronometrage": "(97, k, …)",
                             "regle": "numpy.random.default_rng(numpy.random.SeedSequence(entropy=racine, spawn_key=clé))"},
            "etats_de_controle": etats_de_controle(racine), "lignes": list(B.NOMS), "repetitions": B.REPETITIONS,
            "alpha": B.ALPHA, "instants": list(B.T8), "instants_jumeau": list(B.T40), "tranche": X.TRANCHE,
            "processus": processus, "reductions": list(reductions), "nice": 10, "duree_max_s": X.DUREE_MAX_S,
            "addendum": add, "copies": copie, "miniature": miniature}


def _signal():
    signal.signal(signal.SIGTERM, lever_sur_term)


def jeu_decisif(args) -> int:
    _signal()
    os.nice(10)
    exiger_prereg(RACINE_DEPOT)
    exiger_depot_propre(RACINE_DEPOT)
    if not args.addendum:
        raise GardeArret("addendum d'empreintes scellé exigé (--addendum) : pas de jeu")
    chemin_add = (RACINE_DEPOT / args.addendum).resolve()
    add = X.lire_addendum(RACINE_DEPOT, chemin_add)
    processus, reductions = int(add["programme"]["processus"]), tuple(add["programme"]["reductions"])
    if not 1 <= processus <= X.PROCESSUS_MAX:
        raise GardeArret("trois processus au plus")
    copie = {**juge_v1.verifier_copie(), **VV.verifier_copie_v9()}
    V = VV.charger()
    VV.exiger_noms_empruntes(V.J)
    racine = B.racine_de(B.EMPREINTE_PREREG)
    if args.reprendre:
        run_id = args.reprendre
        if not run_id.endswith(X.NOM_RUN):
            raise GardeArret("reprise : identifiant de run de ce jeu exigé")
        m, sha_m = lire_manifeste(RACINE_DEPOT / "runs" / run_id / "manifeste.json")
        if m["config"]["reductions"] != list(reductions) or m["config"]["processus"] != processus:
            raise GardeArret("reprise : réductions ou processus différents du départ : interdit")
        dossier = RACINE_DEPOT / X.DOSSIER_DIAG / run_id
        depart = json.loads((dossier / "depart.json").read_text(encoding="utf-8"))
        verifier(dossier / "depart.json")
        debut, journal = float(depart["debut_epoch"]), {"run_id": run_id, "reprise": True}
    else:
        exiger_sortie_absente(RACINE_DEPOT)
        controles = {"essais": lancer_essais(RACINE_DEPOT)}
        mut = MU.jouer_banc(V, racine)
        if not (mut["toutes_tuees"] and mut["cas_sains_passes"]):
            raise GardeArret("une mutation survit ou un cas sain manque au contrôle avant jeu : pas de jeu")
        controles["mutations"] = {"toutes_tuees": True, "cas_sains_passes": True, "nombre": len(mut["mutations"])}
        run_id = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S") + "-" + X.NOM_RUN
        config = config_du_jeu(racine, {"chemin": str(chemin_add.relative_to(RACINE_DEPOT)), "sha256": empreinte(chemin_add),
                                        "programme": add["programme"]}, copie, processus, reductions, False)
        config["controles_avant_jeu"] = controles
        chemin_m, _ = creer_manifeste(RACINE_DEPOT, run_id, config, ["racine-du-texte"], entropie=racine, decisif=True,
                                      prereg=RACINE_DEPOT / B.CHEMIN_PREREG,
                                      commande="python -I -B scripts/jouer_idee_1_1_v1.py --addendum " + args.addendum)
        sha_m = empreinte(chemin_m)
        dossier = RACINE_DEPOT / X.DOSSIER_DIAG / run_id
        debut = time.time()
        X.ecrire_json_scelle(dossier / "depart.json", {"run_id": run_id, "debut_epoch": debut, "manifeste_sha256": sha_m,
                                                        "debut_utc": datetime.now(timezone.utc).isoformat(timespec="seconds")})
        journal = {"run_id": run_id}
    X.installer_garde_reseau()
    try:
        res = X.executer(racine=racine, dossier=dossier, run_id=run_id, manifeste_sha=sha_m, processus=processus,
                         reductions=reductions, debut=debut, journal=journal)
    except BaseException as e:
        print(f"ARRÊT : {X.consigner_arret(dossier, e, run_id, sha_m, journal)}", file=sys.stderr)
        raise
    print(json.dumps({"run_id": run_id, **res}, ensure_ascii=False, indent=1))
    return 0


def repetition_miniature(args) -> int:
    """Répétition du chemin du jeu, hors du dépôt, racine d'essai ; aucune lecture, aucun résultat opposable."""
    _signal()
    sortie = Path(args.sortie).resolve()
    if RACINE_DEPOT.resolve() in sortie.parents or sortie == RACINE_DEPOT.resolve():
        raise GardeArret("répétition miniature : sortie jetable hors du dépôt exigée")
    if sortie.exists():
        raise GardeArret(f"{sortie} existe déjà : R12 interdit d'écraser")
    exiger_prereg(RACINE_DEPOT)
    V = VV.charger()
    racine = RACINE_MINIATURE
    if racine == B.racine_de(B.EMPREINTE_PREREG):
        raise GardeArret("répétition miniature : la racine du texte est interdite")
    lignes = [int(x) for x in args.lignes.split(",")]
    liste = [(i, 0, args.repetitions) for i in lignes]
    run_id = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S") + "-miniature-" + X.NOM_RUN
    dossier = sortie / X.DOSSIER_DIAG / run_id
    debut = time.time()
    journal = {"run_id": run_id, "miniature": True}
    X.installer_garde_reseau()
    res = X.executer(racine=racine, dossier=dossier, run_id=run_id, manifeste_sha="miniature", processus=args.processus,
                     reductions=(), debut=debut, journal=journal, liste=liste)
    print(json.dumps({"run_id": run_id, **res, "copies_verifiees": len(V.empreintes)}, ensure_ascii=False, indent=1))
    return 0


def main(argv=None) -> int:
    a = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    a.add_argument("--addendum")
    a.add_argument("--reprendre")
    a.add_argument("--miniature", action="store_true")
    a.add_argument("--sortie")
    a.add_argument("--lignes", default="0,25")
    a.add_argument("--repetitions", type=int, default=2)
    a.add_argument("--processus", type=int, default=1)
    a.add_argument("--lister-empreintes", action="store_true")
    args = a.parse_args(argv)
    if args.lister_empreintes:
        print(X.lister_empreintes(RACINE_DEPOT), end="")
        return 0
    if args.miniature:
        if not args.sortie:
            raise GardeArret("--sortie exigée pour la répétition miniature")
        return repetition_miniature(args)
    return jeu_decisif(args)


if __name__ == "__main__":
    try:
        sys.exit(main())
    except GardeArret as e:
        print(f"ARRÊT : {e}", file=sys.stderr)
        sys.exit(1)
