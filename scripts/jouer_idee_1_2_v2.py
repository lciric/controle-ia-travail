#!/usr/bin/env python3
"""Lanceur du jeu de l'idée 1.2, version 2 (préenregistrement scellé
`prereg/organisme-idee-1-2-tirages-repartis-arret-anticipe-v4.md`, `bdabf2bc…`, R-2886 ; corrections de la contre-lecture
du code `36ecc4a4…`, R-2899). Processeur seul, sans dépense, aucun appel réseau ni de modèle (R-2851).

    python -I -B scripts/jouer_idee_1_2_v2.py --addendum CHEMIN_ADDENDUM [--processus 2]     # jeu décisif
    python -I -B scripts/jouer_idee_1_2_v2.py --miniature --sortie DOSSIER_HORS_DU_DEPOT [--n-T 5 --n-N 5]
    python -I -B scripts/jouer_idee_1_2_v2.py --lister-empreintes                            # lignes de l'addendum

Différences avec la v1 : la garde du préenregistrement reçoit toujours la racine du dépôt vérifiée (majeur 2) et passe
la première ; le signal TERM est consigné (`arret.json`) ; un manifeste antérieur de ce jeu sous `runs/` bloque la
relance comme une sortie sous `diag/` (mineur 3) ; le champ `graines` du manifeste porte la racine et la configuration
des états de contrôle de clés du texte, que le lecteur revérifie (mineur 4) ; enchaînement `execution_v2` (attente
bornée sur les fils, constantes et troisième écriture du texte) ; banc de mutations v2 ; essais v1 et v2.

Ordre des gardes du jeu décisif : préenregistrement scellé et égal au texte ; arbre propre ; aucune sortie ni manifeste
antérieur de ce jeu ; addendum d'empreintes scellé couvrant les fichiers gelés ; copie du juge ; constantes du texte ;
essais ; mutations ; manifeste ; jeu (E1, oracle scellé, rejeu, sortie scellée). Aucune lecture.
"""
from __future__ import annotations

import os
import sys

for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ[_v] = "1"     # une file de calcul par processus (deux processus au plus)
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

from controle_ia.gardes import GardeArret, etat_git, exiger_depot_propre, lever_sur_term  # noqa: E402
from controle_ia.manifeste import config_canonique, creer_manifeste, graines, versions  # noqa: E402
from controle_ia.prereg import exiger_prereg_scelle  # noqa: E402
from controle_ia.scellement import empreinte, sceller  # noqa: E402
from controle_ia.organisme_idees_juge import banc_tirages_repartis_v1 as B  # noqa: E402
from controle_ia.organisme_idees_juge import execution_v2 as X  # noqa: E402
from controle_ia.organisme_idees_juge import juge_v1  # noqa: E402
from controle_ia.organisme_idees_juge import lire_banc_tirages_repartis_v2 as LB  # noqa: E402
from controle_ia.organisme_idees_juge import mutations_v2 as MU  # noqa: E402
from controle_ia.organisme_idees_juge import rejeu_v1 as R  # noqa: E402
from controle_ia.organisme_idees_juge import verificateur_texte_v2 as VT  # noqa: E402

RACINE_MINIATURE = B.racine_de(hashlib.sha256(b"repetition miniature, idee 1.2, v1 (racine d'essai, jamais celle du jeu)").hexdigest())
ESSAIS = list(X.ESSAIS)
CLES_DE_CONTROLE = ((1, 0, 24), (1, 0, 25), (0, 0, 0, 2), (1, 749, 23, 2), (1, 0, 1000), (1, 0, 1001), (1, 0, 2000),
                    (99, 0), (97, 0))


def exiger_prereg(racine_depot: Path) -> str:
    sha = exiger_prereg_scelle(Path(racine_depot) / B.CHEMIN_PREREG)
    if sha != B.EMPREINTE_PREREG:
        raise GardeArret(f"préenregistrement {sha[:12]}… ≠ texte scellé attendu {B.EMPREINTE_PREREG[:12]}…")
    return sha


def exiger_sortie_absente(racine_depot: Path, run_id: str) -> None:
    diag, runs = racine_depot / X.DOSSIER_DIAG, racine_depot / "runs"
    if (runs / run_id).exists() or (diag / run_id).exists():
        raise GardeArret(f"sortie du run {run_id} déjà présente : R12 interdit d'écraser")
    for dossier, quoi in ((diag, "une sortie"), (runs, "un manifeste")):
        if dossier.is_dir():
            anciens = sorted(p.name for p in dossier.iterdir() if p.name.endswith(X.NOM_RUN))
            if anciens:
                raise GardeArret(f"{quoi} de ce jeu existe déjà ({anciens}) : relance seulement sous un texte ou un addendum neuf")


def installer_signaux():
    """Le signal TERM lève `GardeArret` dans le parent (consigné dans `arret.json`) ; les fils le rétablissent au défaut."""
    return signal.signal(signal.SIGTERM, lever_sur_term)


def abaisser_priorite() -> None:
    os.nice(10)


def etats_de_controle(racine: int) -> dict:
    return {str(cle): B.etat_graine(racine, *cle) for cle in CLES_DE_CONTROLE}


def lancer_essais(racine_depot: Path) -> dict:
    env = {"PATH": os.environ.get("PATH", "/usr/bin:/bin"), "HOME": os.environ.get("HOME", "/tmp"), "PYTHONPATH": "src",
           "LANG": "C.UTF-8", "OMP_NUM_THREADS": "1", "OPENBLAS_NUM_THREADS": "1", "MKL_NUM_THREADS": "1"}
    t0 = time.time()
    r = subprocess.run([sys.executable, "-B", "-m", "pytest", "-q", "-p", "no:cacheprovider", *ESSAIS], cwd=racine_depot,
                       env=env, capture_output=True, text=True)
    sortie = {"code": r.returncode, "fin": r.stdout[-2000:], "duree_s": round(time.time() - t0, 1)}
    if r.returncode != 0:
        raise GardeArret(f"un essai échoue : pas de jeu\n{r.stdout[-3000:]}\n{r.stderr[-2000:]}")
    return sortie


def config_du_jeu(racine: int, generations: dict, fichiers: dict, addendum: dict | None, copie: dict, processus: int,
                  miniature: bool) -> dict:
    return {"objet": "idée 1.2 : tirages frais répartis par blocs avec arrêt anticipé contre la part fixe (banc B v2)",
            "version_lanceur": 2,
            "preenregistrement": {"chemin": B.CHEMIN_PREREG, "sha256": B.EMPREINTE_PREREG},
            "racine_graines": str(racine),
            "origine_racine": "répétition miniature : racine d'essai" if miniature else "entier de l'empreinte sha256 du texte scellé",
            "cles_graines": {"monde": "(f, g, 24)", "archive": "(f, g, 25)", "carte": "(f, g, i, 0)",
                             "plan_entrainement": "(f, g, i, 1)", "issues_fraiches": "(f, g, i, 2)",
                             "positions": "(f, g, 1001)", "placebo": "(f, g, 1000)", "oracle": "(f, g, 2000)",
                             "reechantillonnage": "(99, b)", "jeu_synthetique": "(97, g)", "familles": {"N": 0, "T": 1},
                             "regle": "numpy.random.SeedSequence(entropy=racine_graines, spawn_key=clé)"},
            "etats_de_controle": etats_de_controle(racine),
            "generations": {f: len(v) for f, v in generations.items()},
            "indices_generations": generations if miniature else "N : 0..499 ; T : 0..749",
            "bras": {"T": list(R.BRAS_T), "N": list(R.BRAS_N)},
            "parametres": {"alpha": B.ALPHA, "m": B.M, "bloc": B.BLOC, "plafond": B.N_MAX, "part_fixe": B.PART,
                           "budget": B.M * B.PART, "budget_F125": 6000, "entrainement": B.ENTRAINEMENT,
                           "instances_oracle": B.ORACLE_N, "plafond_cosinus": B.PLAFOND_COSINUS,
                           "reechantillons": VT.REECHANTILLONS_TEXTE, "seuil_haut": "log(m/alpha)",
                           "seuil_bas": "log(1/20), t >= 50", "intervalle": "percentile 95 % (2,5 % ; 97,5 %)",
                           "attente_bornee_s": X.PAS_ATTENTE_S},
            "fichiers_geles": fichiers, "addendum": addendum, "copie_juge": copie,
            "processus": processus, "nice": 10, "miniature": miniature}


def jeu_decisif(args) -> int:
    installer_signaux()
    garde = X.GardeDuree(horloge=time.time)
    abaisser_priorite()
    run_id = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S") + "-" + X.NOM_RUN
    exiger_prereg(RACINE_DEPOT)
    exiger_depot_propre(RACINE_DEPOT)
    exiger_sortie_absente(RACINE_DEPOT, run_id)
    if not args.addendum:
        raise GardeArret("addendum d'empreintes scellé exigé (--addendum) : pas de jeu")
    chemin_add = (RACINE_DEPOT / args.addendum).resolve()
    liste = X.verifier_addendum(RACINE_DEPOT, chemin_add)
    copie = juge_v1.verifier_copie()
    VT.exiger_constantes_du_texte()
    controles = {"preenregistrement": B.EMPREINTE_PREREG, "addendum": {"chemin": str(chemin_add.relative_to(RACINE_DEPOT)),
                 "sha256": empreinte(chemin_add)}, "copie_juge": copie}
    controles["essais"] = lancer_essais(RACINE_DEPOT)
    racine = B.racine_de(B.EMPREINTE_PREREG)
    rapport_mut = MU.banc(racine)
    MU.exiger_toutes_tuees(rapport_mut)
    controles["mutations"] = rapport_mut
    generations = X.generations_du_texte()
    config = config_du_jeu(racine, generations, {f: liste[f] for f in X.FICHIERS_GELES}, controles["addendum"], copie,
                           args.processus, False)
    chemin_m, _ = creer_manifeste(RACINE_DEPOT, run_id, config, ["racine-du-texte"], entropie=racine, decisif=True,
                                  prereg=RACINE_DEPOT / B.CHEMIN_PREREG,
                                  commande="python -I -B scripts/jouer_idee_1_2_v2.py --addendum " + args.addendum)
    sha_m = empreinte(chemin_m)
    dossier = RACINE_DEPOT / X.DOSSIER_DIAG / run_id
    journal = {"run_id": run_id, "debut_utc": datetime.now(timezone.utc).isoformat(timespec="seconds")}
    X.installer_garde_reseau()
    try:
        res = X.executer(racine=racine, generations=generations, dossier_sortie=dossier, run_id=run_id, manifeste_sha=sha_m,
                         processus=args.processus, controles=controles, garde=garde, journal=journal)
    except BaseException as e:
        print(f"ARRÊT : {X.consigner_arret(dossier, e, run_id, sha_m, journal)}", file=sys.stderr)
        raise
    print(json.dumps({"manifeste": str(chemin_m.relative_to(RACINE_DEPOT)), **res}, ensure_ascii=False, indent=1))
    return 0


def repetition_miniature(args) -> int:
    installer_signaux()
    garde = X.GardeDuree(horloge=time.time)
    abaisser_priorite()
    sortie = Path(args.sortie).resolve()
    if RACINE_DEPOT.resolve() in sortie.parents or sortie == RACINE_DEPOT.resolve():
        raise GardeArret("répétition miniature : sortie jetable hors du dépôt exigée")
    if sortie.exists():
        raise GardeArret(f"{sortie} existe déjà : R12 interdit d'écraser")
    racine = args.racine_essai or RACINE_MINIATURE
    if racine == B.racine_de(B.EMPREINTE_PREREG):
        raise GardeArret("répétition miniature : la racine du texte est interdite (graine d'essai distincte)")
    exiger_prereg(RACINE_DEPOT)
    copie = juge_v1.verifier_copie()
    VT.exiger_constantes_du_texte()
    run_id = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S") + "-miniature-" + X.NOM_RUN
    controles = {"miniature": True, "copie_juge": copie, "essais": "non lancés (répétition miniature)",
                 "addendum": "non exigé (répétition miniature)"}
    t0 = time.time()
    rapport_mut = MU.banc(racine, args.synthetique, args.reechantillons_synthetiques)
    MU.exiger_toutes_tuees(rapport_mut)
    controles["mutations"] = rapport_mut
    controles["duree_mutations_s"] = round(time.time() - t0, 1)
    generations = X.generations_miniature(args.n_T, args.n_N)
    fichiers = {f: empreinte(RACINE_DEPOT / f) for f in X.FICHIERS_GELES if (RACINE_DEPOT / f).is_file()}
    config = config_du_jeu(racine, generations, fichiers, None, copie, args.processus, True)
    git = etat_git(RACINE_DEPOT)
    manifeste = {"run_id": run_id, "cree_le": datetime.now(timezone.utc).isoformat(timespec="seconds"), "commit": git["commit"],
                 "depot_propre": git["propre"], "decisif": False, "config": config,
                 "config_sha256": hashlib.sha256(config_canonique(config)).hexdigest(), "versions": versions(),
                 "graines": graines(["racine-d-essai"], racine),
                 "commande": " ".join(sys.argv), "reserves": ["répétition miniature : racine d'essai, aucun résultat opposable"]}
    (sortie / "runs" / run_id).mkdir(parents=True)
    chemin_m = sortie / "runs" / run_id / "manifeste.json"
    chemin_m.write_text(json.dumps(manifeste, indent=2, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")
    sha_m = sceller(chemin_m)
    dossier = sortie / X.DOSSIER_DIAG / run_id
    cartes_E1 = (("T", 0, 0), ("N", 0, 8))
    journal = {"run_id": run_id, "miniature": True}
    X.installer_garde_reseau()
    try:
        res = X.executer(racine=racine, generations=generations, dossier_sortie=dossier, run_id=run_id, manifeste_sha=sha_m,
                         processus=args.processus, cartes_E1=cartes_E1, controles=controles, garde=garde, journal=journal)
    except BaseException as e:
        print(f"ARRÊT : {X.consigner_arret(dossier, e, run_id, sha_m, journal)}", file=sys.stderr)
        raise
    t1 = time.time()
    lecture = LB.ecrire_lecture(dossier, racine, reechantillons=args.reechantillons_lecture, manifeste_sha=sha_m)
    corps = json.loads(lecture.read_text(encoding="utf-8"))["resultat"]
    structure = {"etages": sorted(k for k in corps if k.startswith("etage")), "cles": sorted(corps)}
    print(json.dumps({"manifeste": str(chemin_m), **res, "lecture": str(lecture), "duree_lecture_s": round(time.time() - t1, 1),
                      "structure_de_la_lecture (chiffres non affichés)": structure}, ensure_ascii=False, indent=1))
    return 0


def main(argv=None) -> int:
    a = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    a.add_argument("--addendum")
    a.add_argument("--processus", type=int, default=X.PROCESSUS_MAX)
    a.add_argument("--miniature", action="store_true")
    a.add_argument("--sortie")
    a.add_argument("--n-T", dest="n_T", type=int, default=5)
    a.add_argument("--n-N", dest="n_N", type=int, default=5)
    a.add_argument("--racine-essai", type=int, default=None)
    a.add_argument("--synthetique", type=int, default=1000)
    a.add_argument("--reechantillons-synthetiques", type=int, default=1000)
    a.add_argument("--reechantillons-lecture", type=int, default=1000)
    a.add_argument("--lister-empreintes", action="store_true")
    args = a.parse_args(argv)
    if args.lister_empreintes:
        print(X.lister_empreintes(RACINE_DEPOT), end="")
        return 0
    if not 1 <= args.processus <= X.PROCESSUS_MAX:
        raise GardeArret("deux processus au plus")
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
