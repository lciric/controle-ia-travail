"""Lecture (1) de (ii-b) : dommage agrégé par l'oracle (conception 6.1). EXPLORATOIRE, NON OPPOSABLE (R-522).

Usage : PYTHONPATH=src python scripts/lecture_iib_1_dommage_v1.py --racine R --run-id RUN [--sortie DOSSIER] [--min-taches N]
Lit : runs/RUN/manifeste.json (entropie de la course), donnees/RUN/oracle-iib.json, diag/RUN/acceptation-iib.json (tous
vérifiés par leur compagnon). N'ouvre aucun fichier de sonde ni d'activations. Écrit, scellé :
lecture-1-dommage-iib-EXPLORATOIRE-NON-OPPOSABLE.json. `--min-taches` (défaut 32, conception) : répétition jouet seulement.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from controle_ia.gardes import GardeArret
from controle_ia.iib import constantes_v1 as C
from controle_ia.iib.lecture_v1 import EFFETS, lecture_1
from controle_ia.manifeste import generateur, graines, lire_manifeste, verifier_resultat
from controle_ia.scellement import sceller, verifier

NOM = "lecture-1-dommage-iib-EXPLORATOIRE-NON-OPPOSABLE.json"


def main(argv):
    p = argparse.ArgumentParser()
    p.add_argument("--racine", default=".")
    p.add_argument("--run-id", required=True)
    p.add_argument("--sortie", default=None)
    p.add_argument("--min-taches", type=int, default=C.LECTURE1_MIN_TACHES)
    a = p.parse_args(argv)
    R = Path(a.racine)
    m, sha_m = lire_manifeste(R / "runs" / a.run_id / "manifeste.json")
    chemin_o = R / "donnees" / a.run_id / "oracle-iib.json"
    sha_o = verifier(chemin_o)
    lignes = [l for l in json.loads(chemin_o.read_text(encoding="utf-8"))["lignes"] if l["phase"] == "evaluation"]
    acc = verifier_resultat(R, R / "diag" / a.run_id / "acceptation-iib.json")["resultat"]
    cles = [f"iib/lecture-1/tirages/{x}-{y}" for x, y in EFFETS]
    g = graines(cles, int(m["config"]["entropie"]))
    rngs = {f"{x}-{y}": generateur(g[f"iib/lecture-1/tirages/{x}-{y}"]) for x, y in EFFETS}
    res = lecture_1(lignes, acc["exces_moyen_par_action_bornable_acceptes"], rngs, min_taches=a.min_taches)
    res.update(run_id=a.run_id, manifeste_sha256=sha_m, oracle_sha256=sha_o, min_taches=a.min_taches)
    sortie = Path(a.sortie) if a.sortie else R / "diag" / a.run_id
    sortie.mkdir(parents=True, exist_ok=True)
    chemin = sortie / NOM
    if chemin.exists():
        raise GardeArret(f"{chemin} existe déjà (R12)")
    chemin.write_text(json.dumps(res, ensure_ascii=False, indent=1, sort_keys=True) + "\n", encoding="utf-8")
    print(f"{chemin} {sceller(chemin)} phrase={res['phrase']}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
