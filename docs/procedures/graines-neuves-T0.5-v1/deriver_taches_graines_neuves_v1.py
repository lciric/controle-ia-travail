"""Fichiers des tâches de la course T0.5 « graines neuves » (nuit du 1er au 2 novembre 2026 ; devis
`docs/notes/devis-episodes-reels-t05-nuit-v1/devis-episodes-reels-t05-nuit-v1.md`, scénario « moyen ») : nouveaux
épisodes, à graines neuves, sur des tâches déjà courues.

Règle de choix, écrite et déterministe (aucun résultat lu) :
- lot A : rangs 0 à 29 du fichier des 64 tâches d'évaluation assemblé par l'extraction, dans son ordre (ordre du tirage,
  rang de garde) ; lot B : rangs 30 à 59. Les deux lots, disjoints, sont exactement les 60 tâches du pilote
  (`donnees/t05-pilote-v1/taches-pilote-60-v1.json`, recontrôlé ici à l'identique), coupées en deux moitiés de 30 dans
  l'ordre du fichier : 30 tâches est le plafond d'une course sous `duree_max_s` 15 000 s (devis, section 2).
- Motif : le devis recommande les 60 tâches du pilote (scénario « moyen ») ; ce sont les seules tâches dont les trois
  épisodes de la première génération sont tous notés par les deux juges (décisives `e0`, `e1`, et `e2` du complément),
  donc les seules où une seconde génération se compare tâche par tâche à une première complète ; l'ordre du fichier évite
  tout choix sur le contenu. Les 36 autres (rangs 60 à 63 et entraînement) restent pour un lot ultérieur.
- Identifiants : identifiant d'origine suivi de « -g2 » (seconde génération d'épisodes) ; contrôlés uniques, sans « / »
  (la clé de notation `juge-…/<tâche>/<épisode>/passe-<k>` se découpe sur « / »), sans « /e », et distincts des 96
  identifiants d'origine (évaluation et entraînement), pour que le constructeur de banque de conv-audit ne voie pas une
  tâche dans deux runs. L'identifiant n'entre dans aucune invite (il sert aux clés, aux fiches et aux graines).
- Objets JSON recopiés à l'identique, sauf le seul champ « identifiant ».
- Entropie : une par lot, tirée ici une seule fois par `numpy.random.SeedSequence()` (numpy ≥ 1.25, R9), refusée si
  elle égale celle du pilote ou de la couche 1 bis ; consignée dans le fichier des origines, écrit en mode exclusif.
  Les graines de chaque épisode et de chaque notation en dérivent dans le manifeste du run (clé de dérivation calculée
  sur le nom, qui porte l'identifiant neuf).

Sources vérifiées par leur sceau et par l'empreinte attendue ; sorties écrites en mode exclusif (R12), à sceller par
l'appelant (`python -m controle_ia.scellement sceller`). Aucun texte de tâche n'est lu ni affiché.

Usage : python -I deriver_taches_graines_neuves_v1.py EVALUATION SHA_EVALUATION ENTRAINEMENT SHA_ENTRAINEMENT \
            PILOTE SHA_PILOTE DOSSIER_SORTIE"""
import hashlib
import json
import sys
from pathlib import Path

import numpy as np

SUFFIXE = "-g2"
LOTS = {"a": (0, 30), "b": (30, 60)}
ENTROPIES_DEJA = {37114382722285754842192283631495258186,     # pilote (prereg/T0.5-pilote-8B-v1.md)
                  303166246027625714392538897987636525213}    # couche 1 bis (prereg/T0.5-banque-complete-36-v1.md)


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
pi_brut, sha_pi = lire(Path(sys.argv[5]), sys.argv[6])
dossier = Path(sys.argv[7])
for nom, brut in (("évaluation", ev_brut), ("entraînement", tr_brut)):
    if not isinstance(brut.get("resultat"), dict) or "taches" not in brut["resultat"]:
        arret(f"source {nom} : pas un fichier de tâches de l'extraction (champ « resultat » absent)")
    if brut["resultat"].get("remplacements"):
        arret(f"source {nom} : remplacements présents ; l'ordre du tirage n'est plus celui du fichier")
if "taches" not in pi_brut:
    arret("source pilote : champ « taches » absent")
ev, tr, pi = ev_brut["resultat"]["taches"], tr_brut["resultat"]["taches"], pi_brut["taches"]
if len(ev) != 64 or len(tr) != 32 or len(pi) != 60:
    arret(f"tailles inattendues : {len(ev)} évaluation, {len(tr)} entraînement, {len(pi)} pilote")
if pi != ev[:60]:
    arret("les 60 tâches du pilote ne sont pas les rangs 0 à 59 de l'évaluation, à l'identique")
origine_ids = [t["identifiant"] for t in ev + tr]
if len(set(origine_ids)) != 96:
    arret("identifiants d'origine en double")
if not dossier.is_dir():
    arret(f"dossier de sortie {dossier} absent")
noms = [f"taches-graines-neuves-{lot}-30-v1.json" for lot in sorted(LOTS)] + ["origines-taches-graines-neuves-v1.json"]
presents = [n for n in noms if (dossier / n).exists()]
if presents:
    arret(f"sorties déjà présentes dans {dossier} : {presents} (R12 : rien n'est réécrit)")

entropies = {}
while len(entropies) < len(LOTS):
    e = int(np.random.SeedSequence().entropy)
    if e not in ENTROPIES_DEJA and e not in entropies.values():
        entropies[sorted(LOTS)[len(entropies)]] = e

sorties, origines, neufs = {}, {}, []
for lot, (debut, fin) in sorted(LOTS.items()):
    taches = []
    for rang in range(debut, fin):
        t = dict(ev[rang])
        ancien = t["identifiant"]
        neuf = ancien + SUFFIXE
        if "/" in neuf or "/e" in neuf:
            arret(f"identifiant {neuf!r} : « / » interdit")
        t["identifiant"] = neuf
        taches.append(t)
        neufs.append(neuf)
        origines[neuf] = {"lot": lot.upper(), "identifiant_origine": ancien, "rang_evaluation": rang}
    corps = {"source": {"chemin": sys.argv[1], "sha256": sha_ev, "taches": len(ev), "rangs": f"{debut} à {fin - 1}"},
             "lot": lot.upper(),
             "regle": (f"lot {lot.upper()} : rangs {debut} à {fin - 1} des tâches d'évaluation, dans l'ordre du "
                       f"fichier, recopiées à l'identique sauf l'identifiant, suffixé « {SUFFIXE} » (graines neuves)"),
             "taches": taches}
    chemin = dossier / f"taches-graines-neuves-{lot}-30-v1.json"
    sorties[lot] = {"chemin": str(chemin), "sha256": ecrire(chemin, corps), "taches": len(taches),
                    "premiere": taches[0]["identifiant"], "derniere": taches[-1]["identifiant"],
                    "entropie": str(entropies[lot])}
if len(set(neufs)) != len(neufs) or set(neufs) & set(origine_ids):
    arret("identifiants neufs en double, ou égaux à un identifiant d'origine")
par_lot = {L: {o["identifiant_origine"] for o in origines.values() if o["lot"] == L} for L in ("A", "B")}
if par_lot["A"] & par_lot["B"] or len(par_lot["A"]) != 30 or len(par_lot["B"]) != 30:
    arret("lots A et B non disjoints, ou pas de 30 tâches chacun")
corps_orig = {"sources": [{"chemin": sys.argv[1], "sha256": sha_ev, "taches": len(ev)},
                          {"chemin": sys.argv[3], "sha256": sha_tr, "taches": len(tr)},
                          {"chemin": sys.argv[5], "sha256": sha_pi, "taches": len(pi)}],
              "suffixe": SUFFIXE,
              "entropies": {lot.upper(): str(e) for lot, e in sorted(entropies.items())},
              "entropies_tirees_par": f"numpy.random.SeedSequence() (numpy {np.__version__}), une fois par lot",
              "fichiers": {lot.upper(): {"chemin": s["chemin"], "sha256": s["sha256"]} for lot, s in sorted(sorties.items())},
              "origines": origines}
chemin_orig = dossier / "origines-taches-graines-neuves-v1.json"
sha_orig = ecrire(chemin_orig, corps_orig)
print(json.dumps({"lots": sorties, "origines": {"chemin": str(chemin_orig), "sha256": sha_orig}}, ensure_ascii=False,
                 indent=1))
