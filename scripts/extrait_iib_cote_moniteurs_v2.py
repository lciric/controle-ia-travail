"""Extrait de la course du saboteur à budget pour le côté moniteurs, v2 (v1 + couples E-01 à E-09 de la vérification de la note v2).

CÔTÉ EXPOSÉ : joué par l'exécutante après le rapatriement vérifié, sur l'arbre de la branche du run. L'extrait ne porte que :
- les versions relevées au manifeste (clé `versions`, réduite aux clés de `manifeste.versions()` ; toute autre clé : refus) ;
- le commit de lancement (égal au commit du manifeste, sinon refus) ;
- les empreintes des quatre fichiers de la passe (identifiants et textes de l'évaluation, deux adaptateurs), tirées de
  `resultat.empreintes` du résumé et recalculées sur disque ;
- les lignes `etats_par_lot` de l'évaluation, réduites à six clés permises, chaque valeur de type et de valeur permis
  (adaptateur et dose de la condition, lot entier, empreinte hexadécimale ; toute autre clé ou valeur : refus).
Il remplace, pour le côté moniteurs, tout accès au manifeste, au résumé et aux fiches d'épisodes.

    PYTHONPATH=src python scripts/extrait_iib_cote_moniteurs_v2.py --racine . --run-id RUN --commit-lancement SHA --sortie CHEMIN

Écrit et scelle CHEMIN (jamais d'écrasement, R12) ; imprime son empreinte. Code 0 ; 1 sur toute garde (motif sur la sortie
d'erreur), sans rien écrire.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path

from controle_ia.gardes import GardeArret
from controle_ia.manifeste import BIBLIOTHEQUES
from controle_ia.scellement import sceller, verifier

AVERTISSEMENT = "EXPLORATOIRE, NON OPPOSABLE (R-522) : extrait sans mécanisme pour le côté moniteurs"
FICHIERS_PASSE = ("ids-actions-iib-evaluation.npz", "textes-actions-iib-evaluation.jsonl", "adaptateur-eleve.pt",
                  "adaptateur-temoin-jumeau.pt")
CONDITIONS = ("H", "B50", "B100", "TJ100")
CLES_ETAT = ("adaptateur", "condition", "dose_apres", "dose_avant", "empreinte", "lot")
CLES_VERSIONS = frozenset(("python", "plateforme") + tuple(BIBLIOTHEQUES))
ADAPTATEUR_ET_DOSE = {"H": ("eleve", 0.0), "B50": ("eleve", 0.5), "B100": ("eleve", 1.0), "TJ100": ("temoin-jumeau", 1.0)}


def _sha(chemin: Path) -> str:
    h = hashlib.sha256()
    with open(chemin, "rb") as f:
        for bloc in iter(lambda: f.read(1 << 20), b""):
            h.update(bloc)
    return h.hexdigest()


def _lire_scelle(chemin: Path) -> dict:
    if not chemin.is_file():
        raise GardeArret(f"{chemin} absent")
    verifier(chemin)
    return json.loads(chemin.read_text(encoding="utf-8"))


def construire(racine: Path, run_id: str, commit_lancement: str) -> dict:
    if not re.fullmatch(r"[0-9a-f]{40}", commit_lancement):
        raise GardeArret(f"commit de lancement {commit_lancement!r} : 40 caractères hexadécimaux attendus")
    m = _lire_scelle(racine / "runs" / run_id / "manifeste.json")
    if m.get("run_id") != run_id:
        raise GardeArret(f"manifeste : run_id {m.get('run_id')!r} ≠ {run_id!r}")
    if m.get("commit") != commit_lancement:
        raise GardeArret(f"manifeste : commit {str(m.get('commit'))[:12]} ≠ commit de lancement {commit_lancement[:12]}")
    versions = m.get("versions")
    if not isinstance(versions, dict) or not versions or not all(isinstance(k, str) and isinstance(v, str) for k, v in versions.items()):
        raise GardeArret("manifeste : versions absentes ou mal formées")
    if not set(versions) <= CLES_VERSIONS:
        raise GardeArret(f"manifeste : versions, {len(set(versions) - CLES_VERSIONS)} clé(s) hors de manifeste.versions()")
    resume = _lire_scelle(racine / "diag" / run_id / "resume.json")
    empreintes = (resume.get("resultat") or {}).get("empreintes")
    if not isinstance(empreintes, dict):
        raise GardeArret("résumé : resultat.empreintes absent")
    fichiers = {}
    for nom in FICHIERS_PASSE:
        rel = f"donnees/{run_id}/{nom}"
        if rel not in empreintes:
            raise GardeArret(f"{rel} absent de resultat.empreintes du résumé")
        chemin = racine / rel
        if not chemin.is_file():
            raise GardeArret(f"{rel} absent sur disque")
        sur_disque = _sha(chemin)
        if sur_disque != empreintes[rel]:
            raise GardeArret(f"{rel} : empreinte sur disque {sur_disque[:12]} ≠ résumé {str(empreintes[rel])[:12]}")
        if verifier(chemin) != sur_disque:
            raise GardeArret(f"{rel} : compagnon .sha256 non conforme")
        fichiers[rel] = sur_disque
    fiches = _lire_scelle(racine / "diag" / run_id / "episodes-iib.json")
    lignes = fiches.get("etats_par_lot")
    if not isinstance(lignes, list) or not lignes:
        raise GardeArret("fiches d'épisodes : etats_par_lot absent ou vide")
    etats = []
    for i, l in enumerate(lignes):
        if not isinstance(l, dict) or tuple(sorted(l)) != CLES_ETAT:
            raise GardeArret(f"etats_par_lot[{i}] : clés {sorted(l) if isinstance(l, dict) else type(l).__name__} ≠ {list(CLES_ETAT)}")
        if l["condition"] not in CONDITIONS:
            raise GardeArret(f"etats_par_lot[{i}] : condition {l['condition']!r} hors de l'évaluation")
        adaptateur, dose = ADAPTATEUR_ET_DOSE[l["condition"]]
        if (l["adaptateur"] != adaptateur or type(l["lot"]) is not int or l["lot"] < 1
                or any(type(l[k]) is not float or l[k] != dose for k in ("dose_avant", "dose_apres"))
                or not isinstance(l["empreinte"], str) or not re.fullmatch(r"[0-9a-f]{64}", l["empreinte"])):
            raise GardeArret(f"etats_par_lot[{i}] : valeur hors permis (adaptateur et dose de la condition, lot entier, empreinte)")
        etats.append({k: l[k] for k in CLES_ETAT})
    return {"avertissement": AVERTISSEMENT, "run_id": run_id, "commit_lancement": commit_lancement, "versions": dict(sorted(versions.items())),
            "fichiers_de_la_passe": fichiers, "etats_par_lot_evaluation": etats}


def main(argv: list[str]) -> int:
    p = argparse.ArgumentParser(prog="extrait_iib_cote_moniteurs_v2")
    p.add_argument("--racine", default=".")
    p.add_argument("--run-id", required=True)
    p.add_argument("--commit-lancement", required=True)
    p.add_argument("--sortie", required=True)
    a = p.parse_args(argv)
    try:
        sortie = Path(a.sortie)
        if sortie.exists() or Path(str(sortie) + ".sha256").exists():
            raise GardeArret(f"{sortie} existe déjà : R12 interdit d'écraser")
        extrait = construire(Path(a.racine), a.run_id, a.commit_lancement)
        sortie.parent.mkdir(parents=True, exist_ok=True)
        sortie.write_text(json.dumps(extrait, indent=2, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")
        sha = sceller(sortie)
    except GardeArret as e:
        print(f"EXTRAIT REFUSÉ : {e}", file=sys.stderr)
        return 1
    print(f"EXTRAIT ÉCRIT : {sortie} sha256 {sha}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
