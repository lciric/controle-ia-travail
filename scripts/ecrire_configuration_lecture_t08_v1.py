#!/usr/bin/env python3
"""Configuration réelle de la lecture de T0.8 — programme qui l'écrit (consigne de la chaîne de lancement, `722ceb5e…`, tenue en v3 `6f52c4db…` ; texte au brouillon 15 `8d68b7a0…`,
§ 3.3). v1.

Aucune règle de lecture n'est écrite ici : elles sont dans `lecture_v1.py`, contre-lu. Ce programme ne fait qu'assembler la
liste blanche de la lecture (`lecture_v1.ENTREES_LECTURE_REQUISES`, plus les entrées de la pièce HD si elles sont données),
chaque entrée à son chemin et à son empreinte **inscrite** :

- registre des scellements (`registres/scellements-v1.md`, registre vivant, sans empreinte) ;
- de 7b : `mesures-t06.npz`, `textes-actions-t06.jsonl`, `episodes-t06.json`, `manifeste.json`, `lecture-cout-t06.json` aux
  chemins du run `RUN_7B` (plan, point 1) et aux empreintes du marqueur `EMPREINTES_ENTREES_7B` ;
- tâches et texte scellé de la base (A) : chemins et empreintes du texte (`configuration_v1.ENTREES_CONSTANTES`) ;
- `base-a-t08.json` : chemin et empreinte de la ligne `LECTURE-T08-BASE-A` du registre ;
- `course-t08.json` : chemin et empreinte de la ligne `COURSE-T08` ; de son enveloppe, **seuls** `run_id`, `manifeste_sha256`
  et la liste `resultat.fichiers` (chemins et empreintes des six fichiers de la course) sont lus, après vérification de son
  empreinte contre la ligne et contre son compagnon ; rien d'autre n'en est gardé (aucun compte, aucun score) ;
- manifeste de la course : `runs/<run de la course>/manifeste.json`, à l'empreinte de l'enveloppe ;
- **empreinte exigée de chaque fichier de la course** (r-9 ; mot de Lazar `GO-2026-11-22-134`) : chaque fichier que lit la
  lecture entre à l'empreinte que lui donne `course-t08.json` (64 caractères hexadécimaux), jamais au seul compagnon ; un
  fichier sans empreinte dans `course-t08.json` n'entre pas (arrêt, rien d'écrit). Un fichier de plus de 90 Mo versé en
  morceaux et recomposé entre donc à son chemin d'origine si, et seulement si, il est égal à l'octet à la sortie scellée :
  la liste blanche compare son empreinte à celle-ci (`differe_de_la_consignee` sinon, entrée manquante, ligne D1) ;
- pièce HD (facultatif, `--hd` : fichier JSON `{"index": …, "mesures": …, "textes": …, "manifeste": …}`) : registre du texte de
  validité (`registres/validite-adaptateur-v1.md`, vivant) et les quatre fichiers, phase `hd`, sans empreinte consignée (le
  code les contrôle contre la ligne `SORTIES-HD-VADAPT` et l'index, à l'étape (h bis)) ; sans `--hd`, la lecture écrit
  « non lue (entrées absentes) ».

Marqueurs : ceux de la configuration scellée de la course (`--config-course`), qui doivent égaler ceux que porte le texte.
Contrôles avant l'écriture : `exiger_marqueurs`, `exiger_valeurs_gelees` (lecture), `exiger_entrees_reelles`,
`exiger_marqueurs_au_texte` ; puis écriture (refus d'écraser, R12) et compagnon `.sha256` (R6).

    PYTHONPATH=src python3 -B scripts/ecrire_configuration_lecture_t08_v1.py --texte prereg/T0.8-bases-boite-noire-v0-v1.md \
        --config-course prereg/T0.8-configuration-course-v1.json --registre registres/scellements-v1.md \
        [--hd <chemins-hd.json>] --sortie prereg/T0.8-configuration-lecture-v1.json

Codes : 0 écrit ; 1 arrêt (rien d'écrit) ; 2 usage.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parents[1]
if str(RACINE / "src") not in sys.path:
    sys.path.insert(0, str(RACINE / "src"))

from controle_ia.gardes import GardeArret  # noqa: E402
from controle_ia.scellement import empreinte, sceller, verifier  # noqa: E402
from controle_ia.t08 import configuration_v1 as cf  # noqa: E402
from controle_ia.t08 import entrees_v1 as en  # noqa: E402

VERSION = "ecrire_configuration_lecture_t08_v1"
REGISTRE_VADAPT = "registres/validite-adaptateur-v1.md"
FICHIERS_COURSE = {"mesures_etalonnage": "mesures_etalonnage", "textes_etalonnage": "textes_etalonnage",
                   **{f"lectures_{j}_{l}": f"lectures_{j}_{l}" for j in cf.JUGES for l in ("une_passe", "raisonnement")}}


def _rel(racine: Path, chemin: str) -> str:
    p = Path(chemin)
    if p.is_absolute() or ".." in p.parts:
        raise GardeArret(f"chemin {chemin!r} : relatif à la racine, sans « .. », attendu")
    return chemin


def entrees_lecture(racine: Path, marqueurs: dict, registre_rel: str, hd: dict | None) -> dict:
    run = marqueurs["RUN_7B"]["run_id"]
    emp = marqueurs["EMPREINTES_ENTREES_7B"]
    reg = en.lire_registre_scellements(racine / registre_rel)
    if reg["mal_formees_lues"]:
        raise GardeArret(f"registre : lignes lues d'une autre forme {reg['mal_formees_lues']} : arrêt")
    base_a = en.exiger_ligne(reg, "LECTURE-T08-BASE-A")
    course = en.exiger_ligne(reg, "COURSE-T08")
    ch_course = _rel(racine, course["chemin"])
    p = racine / ch_course
    if Path(ch_course).name != "course-t08.json" or Path(ch_course).parts[0] != "diag":
        raise GardeArret(f"ligne COURSE-T08 : {ch_course} n'est pas diag/<run>/course-t08.json")
    if verifier(p) != course["sha256"]:
        raise GardeArret("course-t08.json : empreinte ≠ ligne COURSE-T08 (R11)")
    corps = json.loads(p.read_text(encoding="utf-8"))
    run_c, sha_m = corps["run_id"], corps["manifeste_sha256"]
    if Path(ch_course).parent.name != run_c:
        raise GardeArret(f"course-t08.json : run {run_c} ≠ dossier {Path(ch_course).parent.name}")
    fichiers = corps["resultat"]["fichiers"]
    if not isinstance(fichiers, dict):
        raise GardeArret("course-t08.json : resultat.fichiers attendu (chemin et empreinte de chaque fichier)")
    e = {"registre_scellements": {"chemin": registre_rel, "sha256": None, "scelle": False, "phase": "lecture"},
         "mesures_7b": {"chemin": f"donnees/{run}/mesures-t06.npz", "sha256": emp["mesures-t06.npz"]},
         "textes_7b": {"chemin": f"donnees/{run}/textes-actions-t06.jsonl", "sha256": emp["textes-actions-t06.jsonl"]},
         "episodes_7b": {"chemin": f"diag/{run}/episodes-t06.json", "sha256": emp["episodes-t06.json"]},
         "manifeste_7b": {"chemin": f"runs/{run}/manifeste.json", "sha256": emp["manifeste.json"]},
         "lecture_cout_7b": {"chemin": f"diag/{run}/lecture-cout-t06.json", "sha256": emp["lecture-cout-t06.json"]},
         "taches": {"chemin": cf.TACHES_EVALUATION, "sha256": cf.TACHES_EVALUATION_SHA256},
         "base_a_texte": {"chemin": cf.BASE_A_TEXTE, "sha256": cf.BASE_A_SHA256},
         "base_a_json": {"chemin": _rel(racine, base_a["chemin"]), "sha256": base_a["sha256"]},
         "course_t08": {"chemin": ch_course, "sha256": course["sha256"]},
         "manifeste_course": {"chemin": f"runs/{run_c}/manifeste.json", "sha256": sha_m}}
    for nom, cle in FICHIERS_COURSE.items():
        f = fichiers.get(cle)
        if not isinstance(f, dict) or not re.fullmatch(r"[0-9a-f]{64}", str(f.get("sha256") or "")):
            raise GardeArret(f"course-t08.json : {cle} sans empreinte de 64 caractères : il n'entre pas dans la lecture "
                             "(r-9, GO-2026-11-22-134)")
        if not str(f["chemin"]).startswith(f"donnees/{run_c}/"):
            raise GardeArret(f"course-t08.json : {cle} hors de donnees/{run_c}/")
        e[nom] = {"chemin": _rel(racine, f["chemin"]), "sha256": f["sha256"]}
    for x in e.values():
        x.setdefault("phase", "lecture")
    if hd is not None:
        if sorted(hd) != ["index", "manifeste", "mesures", "textes"]:
            raise GardeArret("--hd : clés index, mesures, textes, manifeste attendues")
        e["registre_vadapt"] = {"chemin": REGISTRE_VADAPT, "sha256": None, "scelle": False, "phase": "hd"}
        for k in ("index", "mesures", "textes", "manifeste"):
            e[f"{k}_hd"] = {"chemin": _rel(racine, hd[k]), "sha256": None, "phase": "hd"}
    en.ListeBlanche(racine, e)                 # motifs interdits, forme des entrées : arrêt dès ici
    return dict(sorted(e.items()))


def construire(racine: Path, texte: str, config_course: str, registre: str, hd: dict | None) -> dict:
    verifier(racine / config_course)
    cc = json.loads((racine / config_course).read_text(encoding="utf-8"))
    mq = cf.exiger_marqueurs(cc.get("marqueurs"))
    cf.exiger_marqueurs_au_texte(racine / texte, mq)
    entrees = entrees_lecture(racine, mq, registre, hd)
    config = {"mode": "reel", "objet": "lecture de T0.8 (étapes (a) à (i), processeur)", "version_programme": VERSION,
              **cf.VALEURS_GELEES_LECTURE, "entrees": entrees, "hd": {}, "marqueurs": mq,
              "configuration_course": {"chemin": config_course, "sha256": empreinte(racine / config_course)}}
    cf.exiger_valeurs_gelees(config, cf.VALEURS_GELEES_LECTURE)
    from controle_ia.t08.lecture_v1 import ENTREES_LECTURE_REQUISES

    cf.exiger_entrees_reelles(config["entrees"], mq, ENTREES_LECTURE_REQUISES)
    return config


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(prog="ecrire_configuration_lecture_t08_v1.py")
    ap.add_argument("--racine", default=".")
    ap.add_argument("--texte", required=True)
    ap.add_argument("--config-course", required=True)
    ap.add_argument("--registre", default="registres/scellements-v1.md")
    ap.add_argument("--hd", default=None)
    ap.add_argument("--sortie", required=True)
    a = ap.parse_args(argv)
    racine, sortie = Path(a.racine), Path(a.racine) / a.sortie
    try:
        if sortie.exists() or Path(str(sortie) + ".sha256").exists():
            raise GardeArret(f"{sortie} existe déjà : nouvelle version = nouveau nom (R12)")
        hd = json.loads(Path(a.hd).read_text(encoding="utf-8")) if a.hd else None
        config = construire(racine, a.texte, a.config_course, a.registre, hd)
        sortie.parent.mkdir(parents=True, exist_ok=True)
        sortie.write_text(json.dumps(config, ensure_ascii=False, indent=1, sort_keys=True) + "\n", encoding="utf-8")
        sha = sceller(sortie)
    except (GardeArret, json.JSONDecodeError, KeyError, TypeError) as e:
        print(f"ARRÊT ({VERSION}) : {type(e).__name__} : {e}", file=sys.stderr)
        return 1
    print(json.dumps({"version": VERSION, "sortie": str(a.sortie), "sha256": sha}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
