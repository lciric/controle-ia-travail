"""Lecture des notations décisives refaites du pilote de T0.5 (N-021, option (a), GO-2026-10-12-02).

Écart de procédure déclaré au préenregistrement du pilote : le code de lecture gelé (`lire_pilote`, commit cité par le
pilote) ne lit les notations que dans le dossier du pilote, par un seul run d'analyse. Les notations refaites
(`noter_pilote_a`) vivent dans un run distinct. Ce module mince les lit **sans rien recalculer lui-même** : il
n'appelle que les fonctions gelées (`_ouvrir_analyse`, `charger_pilote`, `mesures_format`, `empreintes_des_ensembles`,
`notes_alignees`, `lecture_juge`, `decomposition_complete`, `difference_appariee`, `predictions`,
`declencheurs_audit`, `tirer_relectures`), avec les graines de la première analyse, dans l'ordre d'`analyser`. Son
équivalence avec `analyser` est éprouvée par un test (même pilote, notations dans le dossier du pilote ou dans un run
distinct : mêmes juges, même différence appariée, mêmes P2 et P3, mêmes réponses tirées pour l'audit).

Gardes : celles d'`_ouvrir_analyse` (préenregistrement du pilote intact, modules de lecture égaux au commit cité,
constantes et version de numpy du manifeste d'analyse) ; run des notations rattaché au même pilote ; modules de ce
module et du lanceur des notations égaux au commit du run des notations ; aucune notation dans le dossier du pilote ;
format recalculé égal à la première lecture ; P1 et P4 à P7 recalculés avec les grandeurs scellées de la première
lecture, égaux à elles. Sortie : `diag/<run de lecture>/lecture-juges.json`, sous son propre manifeste.
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

from ..gardes import GardeArret
from ..manifeste import creer_manifeste, ecrire_resultat, generateur, lire_manifeste, verifier_resultat
from ..scellement import empreinte
from .lire_pilote import (NIVEAU, TIRAGES, _familles_vides, _ouvrir_analyse, _serialisable, charger_pilote,
                          declencheurs_audit, decomposition_complete, difference_appariee, empreintes_des_ensembles,
                          lecture_juge, mesures_format, notes_alignees, predictions, tirer_relectures)

COMMANDE = "python -m controle_ia.environnements.lire_notations_pilote"
MODULES_NOTATIONS = ("src/controle_ia/environnements/noter_pilote_a.py",
                     "src/controle_ia/environnements/lire_notations_pilote.py")
PREDICTIONS_DE_LA_PREMIERE_LECTURE = ("P1", "P4", "P5", "P6", "P7")


def exiger_modules_notations(racine: Path, commit: str) -> None:
    """Le lanceur et ce lecteur sont ceux du commit du run des notations (modifications non commitées comprises)."""
    absents = [x for x in MODULES_NOTATIONS if not (Path(racine) / x).is_file()]
    if absents:
        raise GardeArret(f"modules des notations absents du dépôt : {absents}")
    r = subprocess.run(["git", "-C", str(racine), "diff", "--quiet", commit, "--", *MODULES_NOTATIONS],
                       capture_output=True, text=True)
    if r.returncode == 1:
        raise GardeArret(f"modules des notations modifiés depuis le commit du run des notations {commit[:12]}")
    if r.returncode != 0:
        raise GardeArret(f"comparaison au commit {commit[:12]} impossible : {r.stderr.strip()}")


def charger_notations(racine: Path, run_notations: str, run_pilote: str, juges: list[str]) -> tuple[dict, str, dict]:
    """Manifeste du run des notations, rattaché au pilote ; notations décisives de chaque juge (None si son fichier
    n'est pas écrit : juge échu ou arrêt)."""
    chemin_m = Path(racine) / "runs" / run_notations / "manifeste.json"
    if not chemin_m.exists():
        raise GardeArret(f"manifeste du run des notations absent : {chemin_m}")
    m, sha_m = lire_manifeste(chemin_m)
    if m["config"].get("run_pilote") != run_pilote:
        raise GardeArret(f"run des notations rattaché au pilote {m['config'].get('run_pilote')!r}, non à {run_pilote}")
    notations = {}
    for j in juges:
        f = Path(racine) / "diag" / run_notations / f"notations-{j}-decisives.json"
        if not f.exists():
            notations[j] = None
            continue
        c = verifier_resultat(racine, f)
        if c["run_id"] != run_notations:
            raise GardeArret(f"{f.name} rattaché au run {c['run_id']}, non à {run_notations}")
        notations[j] = c["resultat"]["notations"]
    return m, sha_m, notations


def lire_notations(racine: Path, run_pilote: str, run_notations: str, run_analyse: str, chemin_taches: str | Path,
                   run_lecture: str, prereg: str | None = None, autoriser_depot_sale: bool = False) -> dict:
    racine = Path(racine)
    # gardes gelées de la première analyse (préenregistrement du pilote, modules, constantes, numpy, état de l'arbre)
    chemin_a, m_a, etat = _ouvrir_analyse(racine, run_analyse)
    if m_a["config"]["run_pilote"] != run_pilote:
        raise GardeArret(f"run du pilote {run_pilote} ≠ run du manifeste d'analyse {m_a['config']['run_pilote']}")
    p = charger_pilote(racine, run_pilote, chemin_taches)
    if p["manifeste_sha256"] != m_a["config"]["manifeste_pilote_sha256"]:
        raise GardeArret("manifeste du pilote différent de celui de l'analyse")
    if any(v is not None for (j, etape), v in p["notations"].items() if etape == "decisives"):
        raise GardeArret("le dossier du pilote porte des notations décisives : lecture par `analyser`, pas ici")
    m_n, sha_n, notations = charger_notations(racine, run_notations, run_pilote, p["juges"])
    exiger_modules_notations(racine, m_n["commit"])
    chemin_l1 = racine / "diag" / run_analyse / "lecture.json"
    l1 = verifier_resultat(racine, chemin_l1)["resultat"]
    if l1.get("run_pilote") != run_pilote:
        raise GardeArret("première lecture d'un autre pilote")
    g = m_a["graines"]
    fiches, taches_ids = p["episodes"]["fiches"], sorted(p["taches"])
    fmt = mesures_format(fiches, p["config"]["max_nouveaux"])
    if _serialisable(fmt) != l1["format"]:
        raise GardeArret("format recalculé ≠ format de la première lecture")
    ensembles = empreintes_des_ensembles(fiches)
    # juges et différence appariée : mêmes fonctions, mêmes graines, même ordre qu'`analyser`
    juges, alignes = {}, {}
    for j in p["juges"]:
        if notations[j] is None:
            juges[j] = {"lecture": "notations décisives refaites absentes (juge échu ou arrêt) : nœud",
                        "plan_b": "nœud"}
            continue
        alignes[j] = notes_alignees(notations[j], j, taches_ids, ensembles)
        juges[j] = lecture_juge(alignes[j], generateur(g[f"analyse/bootstrap-parts-{j}"]))
        sensib = notes_alignees(notations[j], j, taches_ids, ensembles, mesure=lambda n: n["score"])
        try:
            juges[j]["sensibilite_sur_100"] = decomposition_complete(sensib["sA"], sensib["sB"], sensib["sC"])[
                "parts_tronquees"]
        except GardeArret as e:
            juges[j]["sensibilite_sur_100"] = f"impossible : {e}"
    diff = None
    if len(alignes) == 2:
        a8, a3 = (alignes[j] for j in p["juges"])
        try:
            diff = difference_appariee((a8["sA"], a8["sB"], a8["sC"]), (a3["sA"], a3["sB"], a3["sC"]), TIRAGES,
                                       generateur(g["analyse/bootstrap-difference"]), NIVEAU)
        except GardeArret as e:
            diff = {"impossible": str(e), "borne": None}
    # prédictions : P2 et P3 nouvelles ; les autres, recalculées sur les grandeurs scellées de la première lecture,
    # doivent lui être égales
    fam = l1["familles"] if isinstance(l1.get("familles"), dict) else _familles_vides()
    cout = l1.get("cout") or {"mediane_log10": None}
    preds = predictions(fmt, juges, diff, fam, cout, l1.get("kappas"), l1.get("difference_kappas"))
    ecarts = [k for k in PREDICTIONS_DE_LA_PREMIERE_LECTURE if preds[k] != l1["predictions"][k]]
    if ecarts:
        raise GardeArret(f"prédictions {ecarts} recalculées ≠ celles de la première lecture")
    p_oui = [a["p_oui"] for a in p["appariements"]["appariements"]] if p["appariements"] else []
    audit = declencheurs_audit(fmt, juges, fam if isinstance(l1.get("familles"), dict) else {}, l1.get("kappas"),
                               p_oui)
    p_notes = {**p, "notations": {(j, "decisives"): notations[j] for j in p["juges"]}}
    lecture = {"run_pilote": run_pilote, "run_notations": run_notations, "run_analyse": run_analyse,
               "commit_lecture_cite": m_a["config"]["commit_lecture_cite"], "commit_notations": m_n["commit"], **etat,
               "juges": juges, "difference_appariee": diff,
               "predictions": {"P2": preds["P2"], "P3": preds["P3"],
                               **{k: preds[k] for k in PREDICTIONS_DE_LA_PREMIERE_LECTURE}},
               "audit_r4_juges": audit, "lecture_suspendue": audit["declenche"],
               "relectures_audit": tirer_relectures(p_notes, generateur(g["analyse/audit"]))}
    config = {"run_pilote": run_pilote, "run_notations": run_notations, "manifeste_notations_sha256": sha_n,
              "run_analyse": run_analyse, "manifeste_analyse_sha256": empreinte(chemin_a),
              "premiere_lecture_sha256": empreinte(chemin_l1), "commit_lecture_cite": lecture["commit_lecture_cite"]}
    chemin_m, _ = creer_manifeste(racine, run_lecture, config, [], decisif=prereg is not None, prereg=prereg,
                                  autoriser_depot_sale=autoriser_depot_sale, commande=COMMANDE)
    ecrire_resultat(racine, chemin_m, "lecture-juges", _serialisable(lecture))
    return lecture


def _main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(prog=COMMANDE)
    for k in ("--run-pilote", "--run-notations", "--run-analyse", "--taches", "--run-lecture", "--prereg"):
        ap.add_argument(k, required=True)
    x = ap.parse_args(argv)
    lecture = lire_notations(Path("."), x.run_pilote, x.run_notations, x.run_analyse, x.taches, x.run_lecture,
                             x.prereg)
    print(json.dumps(_serialisable({k: lecture[k] for k in ("predictions", "audit_r4_juges", "lecture_suspendue")}),
                     ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    try:
        sys.exit(_main(sys.argv[1:]))
    except GardeArret as e:
        print(f"ARRÊT : {e}", file=sys.stderr)
        sys.exit(1)
