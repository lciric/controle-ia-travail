"""Fichier des 36 tâches de la « couche 1 bis » (banque T0.5 complète ; GO-2026-10-27-07, R-564) : les tâches de T0.5
que le pilote n'a pas courues — les rangs 60 à 63 du fichier des tâches d'évaluation (retirées par N-019) puis les 32
tâches d'entraînement, dans l'ordre de leurs fichiers —, recopiées à l'identique (objets JSON inchangés), avec un fichier
à part qui donne l'origine de chaque tâche (« evaluation-retiree » ou « entrainement »). Sources vérifiées par leur sceau
et par l'empreinte attendue ; sorties écrites en mode exclusif (R12), puis scellées par l'appelant. Aucun texte de tâche
n'est lu ni affiché. Copie de `deriver_taches_pilote_v1.py` sous un nom nouveau, étendue à deux sources.

Usage : python -I deriver_taches_banque_v1.py EVALUATION SHA_EVALUATION ENTRAINEMENT SHA_ENTRAINEMENT SORTIE ORIGINES"""
import hashlib
import json
import sys
from pathlib import Path


def arret(msg: str) -> None:
    sys.exit(f"ARRÊT de la dérivation : {msg}")


def lire(source: Path, attendue: str) -> list:
    octets = source.read_bytes()
    sha = hashlib.sha256(octets).hexdigest()
    if sha != attendue:
        arret(f"source {source} : empreinte {sha} ≠ {attendue}")
    sceau = Path(str(source) + ".sha256")
    if not sceau.is_file() or sceau.read_text(encoding="utf-8").split()[0] != sha:
        arret(f"source {source} : sceau absent ou différent")
    brut = json.loads(octets)
    if brut["resultat"].get("remplacements"):
        arret(f"source {source} : remplacements présents")
    return brut["resultat"]["taches"], sha


if len(sys.argv) != 7:
    arret("six arguments attendus")
ev, sha_ev = lire(Path(sys.argv[1]), sys.argv[2])
tr, sha_tr = lire(Path(sys.argv[3]), sys.argv[4])
sortie, origines = Path(sys.argv[5]), Path(sys.argv[6])
if len(ev) != 64 or len(tr) != 32:
    arret(f"tailles inattendues : {len(ev)} tâches d'évaluation, {len(tr)} d'entraînement")
taches = ev[60:64] + tr
ids = [t["identifiant"] for t in taches]
if len(set(ids)) != len(ids) or set(ids) & {t["identifiant"] for t in ev[:60]}:
    arret("identifiants en double, ou communs avec le pilote")
corps = {"sources": [{"chemin": sys.argv[1], "sha256": sha_ev, "taches": len(ev), "rangs": "60 à 63"},
                     {"chemin": sys.argv[3], "sha256": sha_tr, "taches": len(tr), "rangs": "0 à 31"}],
         "regle": ("les rangs 60 à 63 des tâches d'évaluation (retirées du pilote par N-019), puis les 32 tâches "
                   "d'entraînement, dans l'ordre de leurs fichiers, recopiées à l'identique"),
         "taches": taches}
with open(sortie, "x", encoding="utf-8") as f:
    json.dump(corps, f, ensure_ascii=False, indent=1)
    f.write("\n")
orig = {"origines": {i: ("evaluation-retiree" if k < 4 else "entrainement") for k, i in enumerate(ids)},
        "pilote": {"fichier": "donnees/t05-pilote-v1/taches-pilote-60-v1.json", "origine": "evaluation"}}
with open(origines, "x", encoding="utf-8") as f:
    json.dump(orig, f, ensure_ascii=False, indent=1)
    f.write("\n")
print(json.dumps({"sortie": str(sortie), "sha256": hashlib.sha256(sortie.read_bytes()).hexdigest(), "taches": len(ids),
                  "origines": str(origines)}, ensure_ascii=False))
