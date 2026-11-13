"""Essai de bout en bout de T0.8 sur le modèle jouet et des épisodes factices (plan d'analyse, point 10 : « essai de bout
en bout sur le modèle jouet, sur processeur, sans réseau ni dépense, avant la course »).

    python -m controle_ia.t08.essai_jouet_v1 --racine essai/t08-jouet-compte4-v1/a --horodatage AAAAMMJJ-HHMMSS \
        --entropie N

Chaîne : entrées factices (`fabrique_jouet_v1`) → course en mode jouet (étalonnage par l'agent scripté, quatre lectures
de juges par les modèles jouets) → ligne `COURSE-T08` au registre factice → lecture complète (étapes (a) à (i), table D,
table F, lecture descriptive du témoin distillé honnête) → `lecture-t08.json` scellé. Deux essais de même entropie et de
même horodatage rendent les mêmes fichiers de données et les mêmes résultats (`resultat` des fichiers de diagnostic) à
l'octet ; seuls diffèrent les manifestes des runs de T0.8 (date de création, commit) et l'empreinte qui les rattache.
Mode jouet : arbre de travail non propre autorisé (entrées factices écrites dans l'arbre avant le manifeste), réserve
consignée au manifeste ; marqueurs absents ; longueur du raisonnement des juges réduite à 8 jetons (déclaré).
"""
from __future__ import annotations

import argparse
import json
import shutil
import sys
from pathlib import Path

import numpy as np

from ..gardes import GardeArret
from ..harnais.run_harnais_factice import graine_entiere
from ..manifeste import cle_de_tache
from ..scellement import empreinte, sceller
from ..t06.test_croise import partition_plis
from . import configuration_v1 as cf
from . import fabrique_jouet_v1 as fj
from .course_v1 import executer_course
from .lecture_v1 import executer_lecture

RACINE_DEPOT = Path(__file__).resolve().parents[3]
MAX_JETONS_JOUET = 8


def _copier(src_rel: str, racine: Path) -> str:
    src = RACINE_DEPOT / src_rel
    dst = racine / src_rel
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(src, dst)
    return sceller(dst)


def configs(racine: Path, runs: dict, s7b: dict, base_a: tuple, hd: dict, taches: tuple, entropie: int,
            course_run: str | None = None) -> tuple[dict, dict]:
    rel = lambda p: str(Path(p).relative_to(racine))        # noqa: E731
    entrees_course = {
        "taches": {"chemin": rel(taches[0]), "sha256": taches[1], "phase": "course"},
        "textes_7b": {"chemin": rel(s7b["textes"][0]), "sha256": s7b["textes"][1], "phase": "course"},
        "episodes_7b": {"chemin": rel(s7b["episodes"][0]), "sha256": s7b["episodes"][1], "phase": "course"},
        "manifeste_7b": {"chemin": rel(s7b["manifeste"][0]), "sha256": s7b["manifeste"][1], "phase": "course"},
        "invite": {"chemin": cf.INVITE_H12, "sha256": cf.INVITE_H12_SHA256, "phase": "course"},
    }
    course = {"mode": "jouet", "objet": "course de T0.8 (essai jouet)", "T": cf.T_PAS, "N": cf.N_AGENTS, "lot": 8,
              "max_nouveaux": 400, "temperature": 1.0, "noyau_attention": "defaut",
              "episodes_etalonnage_par_tache": cf.EPISODES_ETALONNAGE_PAR_TACHE,
              "max_jetons_raisonnement": MAX_JETONS_JOUET, "temperature_juge": cf.TEMPERATURE_JUGE,
              "lot_juge": cf.LOT_JUGE, "fils": 1, "couches": [7, 15, 23], "tolerance_equivalence": 0.2,
              "agent": {"modele": "meta-llama/Llama-3.1-8B-Instruct", "revision": cf.SPEC_JUGES["J8"]["revision"],
                        "nom": "8B", "variables_gabarit": {"date_string": "26 Jul 2024"},
                        "texte_attendu_ouverture": "Today Date: 26 Jul 2024"},
              "juges": cf.SPEC_JUGES, "entrees": entrees_course, "entropie": entropie, "marqueurs": None}
    lecture = None
    if course_run is not None:
        d = f"donnees/{course_run}"
        entrees = {
            "registre_scellements": {"chemin": "registres-factices/scellements-v1.md", "sha256": None, "scelle": False, "phase": "lecture"},
            "mesures_7b": {"chemin": rel(s7b["mesures"][0]), "sha256": s7b["mesures"][1], "phase": "lecture"},
            "textes_7b": {"chemin": rel(s7b["textes"][0]), "sha256": s7b["textes"][1], "phase": "lecture"},
            "episodes_7b": {"chemin": rel(s7b["episodes"][0]), "sha256": s7b["episodes"][1], "phase": "lecture"},
            "manifeste_7b": {"chemin": rel(s7b["manifeste"][0]), "sha256": s7b["manifeste"][1], "phase": "lecture"},
            "lecture_cout_7b": {"chemin": rel(s7b["lecture_cout"][0]), "sha256": s7b["lecture_cout"][1], "phase": "lecture"},
            "taches": {"chemin": rel(taches[0]), "sha256": taches[1], "phase": "lecture"},
            "base_a_texte": {"chemin": cf.BASE_A_TEXTE, "sha256": cf.BASE_A_SHA256, "phase": "lecture"},
            "base_a_json": {"chemin": rel(base_a[0]), "sha256": base_a[1], "phase": "lecture"},
            "course_t08": {"chemin": f"diag/{course_run}/course-t08.json", "sha256": None, "phase": "lecture"},
            "mesures_etalonnage": {"chemin": f"{d}/mesures-etalonnage-t08.npz", "sha256": None, "phase": "lecture"},
            "textes_etalonnage": {"chemin": f"{d}/textes-etalonnage-t08.jsonl", "sha256": None, "phase": "lecture"},
            "registre_vadapt": {"chemin": "registres-factices/validite-adaptateur-v1.md", "sha256": None, "scelle": False, "phase": "hd"},
            "index_hd": {"chemin": rel(hd["index"][0]), "sha256": None, "phase": "hd"},
            "mesures_hd": {"chemin": rel(hd["mesures"][0]), "sha256": None, "phase": "hd"},
            "textes_hd": {"chemin": rel(hd["textes"][0]), "sha256": None, "phase": "hd"},
            "manifeste_hd": {"chemin": rel(hd["manifeste"][0]), "sha256": None, "phase": "hd"},
        }
        for j in cf.JUGES:
            for l in ("une_passe", "raisonnement"):
                entrees[f"lectures_{j}_{l}"] = {"chemin": f"{d}/lectures-{j}-{l}-t08.jsonl", "sha256": None,
                                                "phase": "lecture"}
        lecture = {"mode": "jouet", "objet": "lecture de T0.8 (essai jouet)", **cf.VALEURS_GELEES_LECTURE,
                   "entrees": entrees, "hd": {}, "entropie": entropie, "marqueurs": None}
    return course, lecture


def fabriquer_entrees(racine, horodatage: str, entropie: int, retirer_hd: str | None = None) -> dict:
    """Entrées factices de la course et de la lecture (sans la course) ; registres factices sans `COURSE-T08`."""
    racine = Path(racine)
    if racine.exists():
        raise GardeArret(f"{racine} existe déjà (R12)")
    racine.mkdir(parents=True)
    _copier(cf.INVITE_H12, racine)
    _copier(cf.BASE_A_TEXTE, racine)
    rng = np.random.default_rng(np.random.SeedSequence(int(entropie), spawn_key=(cle_de_tache("jouet/fabrique"),)))
    taches = fj.taches_factices(racine, rng)
    runs = {k: f"{horodatage}-{k}" for k in ("t06-7b-jouet", "t06-mots-et-cout-jouet", "vadapt-hd-jouet", "t08-course-jouet",
                                             "t08-lecture-jouet")}
    s7b = fj.fabriquer_7b(racine, runs["t06-7b-jouet"], taches[2], entropie, fj.instant(horodatage))
    plis = partition_plis([l["tache"] for l in s7b["lignes"]], graine_entiere(s7b["graines"]["partition-taches"]))
    base_a = fj.fabriquer_base_a(racine, runs["t06-mots-et-cout-jouet"], s7b, plis, entropie, fj.instant(horodatage))
    hd = fj.fabriquer_hd(racine, runs["vadapt-hd-jouet"], taches[2], entropie, fj.instant(horodatage, 2), retirer_hd)
    rel = lambda p: str(Path(p).relative_to(racine))         # noqa: E731
    reg = racine / "registres-factices" / "scellements-v1.md"
    module_piece = RACINE_DEPOT / "src" / "controle_ia" / "t08" / "mots_et_cout_v1.py"
    fj.ecrire_registre(reg, [
        ("SCELLEMENT-T07", fj.instant(horodatage), "prereg/T0.7-factice.md", "0" * 64),
        ("RUN-CONFIRMATION-T06", fj.instant(horodatage), rel(s7b["manifeste"][0]), s7b["manifeste"][1]),
        ("CODE-MOTS-ET-COUT-T06", fj.instant(horodatage), "src/controle_ia/t08/mots_et_cout_v1.py (jouet)",
         empreinte(module_piece)),
        ("LECTURE-T08-BASE-A", fj.instant(horodatage), rel(base_a[0]), base_a[1]),
        ("GEL-T08", fj.instant(horodatage, 1), cf.TEXTE, cf.TEXTE_SHA256),
    ])
    fj.ecrire_registre(racine / "registres-factices" / "validite-adaptateur-v1.md", [
        ("VA-1", fj.instant(horodatage, 3), "diag/factice/va-1.json", "1" * 64),
        ("SORTIES-HD-VADAPT", fj.instant(horodatage, 3), rel(hd["index"][0]), hd["index"][1]),
    ])
    return {"racine": racine, "runs": runs, "s7b": s7b, "base_a": base_a, "hd": hd, "taches": taches, "registre": reg,
            "plis": plis}


def executer(racine, horodatage: str, entropie: int, retirer_hd: str | None = None) -> dict:
    e = fabriquer_entrees(racine, horodatage, entropie, retirer_hd)
    racine, runs, s7b, base_a, hd, taches, reg = (e[k] for k in ("racine", "runs", "s7b", "base_a", "hd", "taches",
                                                                 "registre"))
    rel = lambda p: str(Path(p).relative_to(racine))         # noqa: E731
    c_course, _ = configs(racine, runs, s7b, base_a, hd, taches, entropie)
    course = executer_course(c_course, racine, runs["t08-course-jouet"], autoriser_depot_sale=True)
    ch_course = Path(course["course"])
    fj.ecrire_registre(reg, [("COURSE-T08", fj.instant(horodatage, 4), rel(ch_course), empreinte(ch_course))])
    _, c_lecture = configs(racine, runs, s7b, base_a, hd, taches, entropie, runs["t08-course-jouet"])
    lecture = executer_lecture(c_lecture, racine, runs["t08-lecture-jouet"], autoriser_depot_sale=True)
    return {"racine": str(racine), "runs": runs, "course": course, "lecture": lecture, "ligne_A_factice": s7b["ligne_A"]}


def comparer(a, b) -> dict:
    """Fichiers de deux essais : données (`donnees/`) identiques à l'octet ; résultats (`diag/`) identiques sur leur
    clé `resultat` (ou l'objet entier pour les fichiers sans enveloppe) ; manifestes des runs de T0.8 exclus."""
    a, b = Path(a), Path(b)
    fa = sorted(str(p.relative_to(a)) for p in a.rglob("*") if p.is_file())
    fb = sorted(str(p.relative_to(b)) for p in b.rglob("*") if p.is_file())
    if fa != fb:
        raise GardeArret(f"listes de fichiers différentes : {sorted(set(fa) ^ set(fb))[:5]}")
    identiques, resultats, exclus, differents = [], [], [], []
    for f in fa:
        pa, pb = a / f, b / f
        t08 = ("-t08-course-jouet" in f or "-t08-lecture-jouet" in f)
        if f.startswith("runs/") and t08:
            exclus.append(f)
            continue
        if f.startswith("diag/") and t08 and f.endswith(".json"):
            ra, rb = json.loads(pa.read_text())["resultat"], json.loads(pb.read_text())["resultat"]
            ca, cb = (json.dumps(x, sort_keys=True, ensure_ascii=False).encode() for x in (ra, rb))
            (resultats if ca == cb else differents).append(f)
            continue
        if f.startswith("diag/") and t08 and f.endswith(".sha256"):
            exclus.append(f)
            continue
        if f.startswith("registres-factices/scellements-v1.md"):
            la = [l for l in pa.read_text().splitlines() if "COURSE-T08" not in l]
            lb = [l for l in pb.read_text().splitlines() if "COURSE-T08" not in l]
            (resultats if la == lb else differents).append(f)
            continue
        (identiques if pa.read_bytes() == pb.read_bytes() else differents).append(f)
    return {"fichiers": len(fa), "identiques_octet": len(identiques), "resultats_identiques": resultats,
            "exclus": exclus, "differents": differents, "deterministe": not differents}


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(prog="python -m controle_ia.t08.essai_jouet_v1")
    ap.add_argument("--racine", required=True)
    ap.add_argument("--horodatage", required=True)
    ap.add_argument("--entropie", type=int, required=True)
    ap.add_argument("--comparer", default=None, help="racine d'un premier essai à comparer")
    a = ap.parse_args(argv)
    r = executer(a.racine, a.horodatage, a.entropie)
    if a.comparer:
        r["comparaison"] = comparer(a.comparer, a.racine)
    print(json.dumps(r, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except GardeArret as e:
        print(f"ARRÊT : {e}", file=sys.stderr)
        sys.exit(1)
