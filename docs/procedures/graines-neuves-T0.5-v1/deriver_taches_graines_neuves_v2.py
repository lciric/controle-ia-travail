"""Lots C et D de la course T0.5 « graines neuves » (v2 de la dérivation ; périmètre élargi aux 96 tâches sur le mot de
Lazar « lance tout », GO-2026-11-01-11). La v1 (`deriver_taches_graines_neuves_v1.py`) a écrit les lots A et B et
leurs entropies ; ils ne sont ni réécrits ni retirés (R12) : la v2 les relit, les contrôle et ajoute C et D.

Règle d'ensemble, écrite et déterministe (aucun résultat lu) : la liste ordonnée des 96 tâches de l'environnement est
le fichier des 64 tâches d'évaluation, dans son ordre, suivi du fichier des 32 tâches d'entraînement, dans son ordre ;
lot A = rangs 0 à 29, lot B = 30 à 59 (v1, inchangés : rangs 0 à 59 de l'évaluation), **lot C = rangs 60 à 89** (rangs
60 à 63 de l'évaluation, puis rangs 0 à 25 de l'entraînement), **lot D = rangs 90 à 95** (rangs 26 à 31 de
l'entraînement). Les quatre lots sont disjoints et couvrent les 96 tâches ; C et D sont exactement les 36 tâches de la
couche 1 bis (`donnees/t05-banque-complete-v1/taches-banque-36-v1.json`, même ordre), dont la première génération est
notée en entier (décisives de la course de la couche 1 bis, `e2` du complément, R-591 et R-596). 30 tâches au plus
par course (plafond de 15 000 s).
Identifiants : identifiant d'origine suivi de « -g2 », contrôlés uniques, sans « / », distincts des 96 identifiants
d'origine et des 60 identifiants neufs de A et B. Objets JSON recopiés à l'identique, sauf l'identifiant.
Entropie : une par lot neuf, tirée une seule fois par `numpy.random.SeedSequence()` (numpy ≥ 1.25, R9), refusée si elle
égale celle du pilote, de la couche 1 bis, de A ou de B.
Le fichier des origines v2 reprend A et B de la v1 (relus et contrôlés) et ajoute C et D, avec les quatre entropies.

Usage : python -I deriver_taches_graines_neuves_v2.py EVALUATION SHA_EVALUATION ENTRAINEMENT SHA_ENTRAINEMENT \
            ORIGINES_V1 SHA_ORIGINES_V1 DOSSIER_SORTIE"""
import hashlib
import json
import sys
from pathlib import Path

import numpy as np

SUFFIXE = "-g2"
LOTS_NEUFS = {"c": (60, 90), "d": (90, 96)}
ENTROPIES_DEJA = {37114382722285754842192283631495258186,     # pilote
                  303166246027625714392538897987636525213}    # couche 1 bis


def arret(msg: str) -> None:
    sys.exit(f"ARRÊT de la dérivation : {msg}")


def lire(source: Path, attendue: str) -> tuple[dict, str]:
    octets = source.read_bytes()
    sha = hashlib.sha256(octets).hexdigest()
    if sha != attendue:
        arret(f"source {source} : empreinte {sha} ≠ {attendue}")
    sceau = Path(str(source) + ".sha256")
    if not sceau.is_file() or sceau.read_text(encoding="utf-8").split()[0] != sha:
        arret(f"source {source} : sceau absent ou différent")
    return json.loads(octets), sha


def ecrire(chemin: Path, corps: dict) -> str:
    with open(chemin, "x", encoding="utf-8") as f:
        json.dump(corps, f, ensure_ascii=False, indent=1)
        f.write("\n")
    return hashlib.sha256(chemin.read_bytes()).hexdigest()


if len(sys.argv) != 8:
    arret("sept arguments attendus")
majeur, mineur = (int(x) for x in np.__version__.split(".")[:2])
if (majeur, mineur) < (1, 25):
    arret(f"numpy {np.__version__} : 1.25 ou plus exigé (R9)")
ev_brut, sha_ev = lire(Path(sys.argv[1]), sys.argv[2])
tr_brut, sha_tr = lire(Path(sys.argv[3]), sys.argv[4])
o1, sha_o1 = lire(Path(sys.argv[5]), sys.argv[6])
dossier = Path(sys.argv[7])
for nom, brut in (("évaluation", ev_brut), ("entraînement", tr_brut)):
    if not isinstance(brut.get("resultat"), dict) or "taches" not in brut["resultat"]:
        arret(f"source {nom} : pas un fichier de tâches de l'extraction (champ « resultat » absent)")
    if brut["resultat"].get("remplacements"):
        arret(f"source {nom} : remplacements présents ; l'ordre du tirage n'est plus celui du fichier")
if "origines" not in o1 or "entropies" not in o1 or set(o1["entropies"]) != {"A", "B"}:
    arret("origines v1 : champs « origines » ou « entropies » (A, B) absents")
ev, tr = ev_brut["resultat"]["taches"], tr_brut["resultat"]["taches"]
if len(ev) != 64 or len(tr) != 32:
    arret(f"tailles inattendues : {len(ev)} évaluation, {len(tr)} entraînement")
tout = ev + tr
origine_ids = [t["identifiant"] for t in tout]
if len(set(origine_ids)) != 96:
    arret("identifiants d'origine en double")
# A et B de la v1 : rangs 0 à 59 de la liste ordonnée, identifiants « -g2 »
attendu_ab = {tout[r]["identifiant"] + SUFFIXE: ("A" if r < 30 else "B", tout[r]["identifiant"], r) for r in range(60)}
lu_ab = {i: (o["lot"], o["identifiant_origine"], o["rang_evaluation"]) for i, o in o1["origines"].items()}
if lu_ab != attendu_ab:
    arret("origines v1 : lots A et B différents des rangs 0 à 59 suffixés")
for nom, f in o1["fichiers"].items():
    fichier = Path(f["chemin"])
    if not fichier.is_file() or hashlib.sha256(fichier.read_bytes()).hexdigest() != f["sha256"]:
        arret(f"fichier du lot {nom} de la v1 absent ou modifié")
if not dossier.is_dir():
    arret(f"dossier de sortie {dossier} absent")
noms = ["taches-graines-neuves-c-30-v1.json", "taches-graines-neuves-d-6-v1.json", "origines-taches-graines-neuves-v2.json"]
presents = [n for n in noms if (dossier / n).exists()]
if presents:
    arret(f"sorties déjà présentes dans {dossier} : {presents} (R12 : rien n'est réécrit)")

deja = ENTROPIES_DEJA | {int(e) for e in o1["entropies"].values()}
entropies = {}
while len(entropies) < len(LOTS_NEUFS):
    e = int(np.random.SeedSequence().entropy)
    if e not in deja and e not in entropies.values():
        entropies[sorted(LOTS_NEUFS)[len(entropies)]] = e

origines = {i: dict(lot=v[0], identifiant_origine=v[1], rang_evaluation=v[2]) for i, v in attendu_ab.items()}
sorties, neufs = {}, []
for lot, (debut, fin) in sorted(LOTS_NEUFS.items()):
    taches = []
    for rang in range(debut, fin):
        t = dict(tout[rang])
        ancien = t["identifiant"]
        neuf = ancien + SUFFIXE
        if "/" in neuf:
            arret(f"identifiant {neuf!r} : « / » interdit")
        t["identifiant"] = neuf
        taches.append(t)
        neufs.append(neuf)
        src = ("evaluation", rang) if rang < 64 else ("entrainement", rang - 64)
        origines[neuf] = {"lot": lot.upper(), "identifiant_origine": ancien, "rang_liste_96": rang,
                          "fichier_origine": src[0], "rang_fichier_origine": src[1]}
    corps = {"sources": [{"chemin": sys.argv[1], "sha256": sha_ev, "taches": len(ev)},
                         {"chemin": sys.argv[3], "sha256": sha_tr, "taches": len(tr)}],
             "lot": lot.upper(),
             "regle": (f"lot {lot.upper()} : rangs {debut} à {fin - 1} de la liste ordonnée des 96 tâches (évaluation "
                       f"puis entraînement, chacune dans l'ordre de son fichier), recopiées à l'identique sauf "
                       f"l'identifiant, suffixé « {SUFFIXE} » (graines neuves)"),
             "taches": taches}
    chemin = dossier / f"taches-graines-neuves-{lot}-{fin - debut}-v1.json"
    sorties[lot] = {"chemin": str(chemin), "sha256": ecrire(chemin, corps), "taches": len(taches),
                    "premiere": taches[0]["identifiant"], "derniere": taches[-1]["identifiant"],
                    "entropie": str(entropies[lot])}
tous_neufs = list(attendu_ab) + neufs
if len(set(tous_neufs)) != 96 or set(tous_neufs) & set(origine_ids):
    arret("identifiants neufs en double, ou égaux à un identifiant d'origine")
if sorted(o["identifiant_origine"] for o in origines.values()) != sorted(origine_ids):
    arret("les quatre lots ne couvrent pas exactement les 96 tâches")
corps_orig = {"sources": [{"chemin": sys.argv[1], "sha256": sha_ev, "taches": len(ev)},
                          {"chemin": sys.argv[3], "sha256": sha_tr, "taches": len(tr)},
                          {"chemin": sys.argv[5], "sha256": sha_o1, "role": "origines v1 (lots A et B, inchangés)"}],
              "suffixe": SUFFIXE,
              "entropies": {**o1["entropies"], **{lot.upper(): str(e) for lot, e in sorted(entropies.items())}},
              "entropies_tirees_par": (f"A et B : v1 ; C et D : numpy.random.SeedSequence() (numpy {np.__version__}), "
                                       "une fois par lot"),
              "fichiers": {**o1["fichiers"],
                           **{lot.upper(): {"chemin": s["chemin"], "sha256": s["sha256"]} for lot, s in sorted(sorties.items())}},
              "origines": origines}
chemin_orig = dossier / "origines-taches-graines-neuves-v2.json"
sha_orig = ecrire(chemin_orig, corps_orig)
print(json.dumps({"lots": sorties, "origines": {"chemin": str(chemin_orig), "sha256": sha_orig}}, ensure_ascii=False,
                 indent=1))
