"""Extrait des ÉTATS des lectures du dommage et de la diffusion du saboteur à budget, pour le côté moniteurs, v1.

CÔTÉ EXPOSÉ : joué par l'exécutante après la course et ses deux lectures, sur les sorties scellées
`diag/RUN/lecture-iib-1-dommage-exploratoire-non-opposable-v1.json` et
`diag/RUN/lecture-iib-2-diffusion-exploratoire-non-opposable-v1.json` (le fichier des mots pondérés n'est jamais ouvert).
Il ne rend que des états, au vocabulaire exact de la note d'interface v3 :
- lecture du dommage : sa phrase, une seule pour la course, parmi quatre valeurs ;
- lecture de la diffusion : par paire de conditions et par base, l'état du jeu (« réussit », « échoue », « non calculable ») ;
  par paire, l'état de l'unité (même vocabulaire) ; sa phrase, ou `null`.
Aucun chiffre, aucune autre phrase, aucune autre clé. Toute valeur hors vocabulaire, tout jeu ou unité manquant ou en trop :
refus, sans imprimer la valeur refusée et sans rien écrire.

    PYTHONPATH=src python scripts/extrait_iib_etats_lectures_cote_moniteurs_v1.py --racine . --run-id RUN --sortie CHEMIN

Écrit et scelle CHEMIN (jamais d'écrasement, R12) ; imprime son empreinte. Code 0 ; 1 sur toute garde.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from controle_ia.gardes import GardeArret
from controle_ia.scellement import sceller, verifier

AVERTISSEMENT = "EXPLORATOIRE, NON OPPOSABLE (R-522) : états des lectures, sans chiffre, pour le côté moniteurs"
NOM_DOMMAGE = "lecture-iib-1-dommage-exploratoire-non-opposable-v1.json"
NOM_DIFFUSION = "lecture-iib-2-diffusion-exploratoire-non-opposable-v1.json"
PHRASES_DOMMAGE = ("non calculable", "dommage agrégé vu", "dommage non distingué du témoin-jumeau", "dommage non vu à cette puissance")
ETATS = ("réussit", "échoue", "non calculable")
PHRASES_DIFFUSION = ("diffus réalisé, à titre exploratoire, hors juge d'une autre lignée", None)
UNITES = ("B100-H", "B50-H", "TJ100-H")
JEUX = tuple(f"{b}/{u}" for b in ("cout", "traits", "mots_et_cout") for u in UNITES) + ("mots_et_cout/B100-TJ100",)


def _lire(chemin: Path) -> dict:
    if not chemin.is_file():
        raise GardeArret(f"{chemin.name} absent")
    verifier(chemin)
    x = json.loads(chemin.read_text(encoding="utf-8"))
    if not isinstance(x, dict):
        raise GardeArret(f"{chemin.name} : objet attendu")
    return x


def _dans(valeur, permis: tuple, ou: str):
    if isinstance(valeur, bool) or not (valeur is None or isinstance(valeur, str)) or valeur not in permis:
        raise GardeArret(f"{ou} : valeur hors du vocabulaire de la note (non imprimée)")
    return valeur


def construire(racine: Path, run_id: str) -> dict:
    d = racine / "diag" / run_id
    l1 = _lire(d / NOM_DOMMAGE)
    l2 = _lire(d / NOM_DIFFUSION)
    phrase_1 = _dans(l1.get("phrase"), PHRASES_DOMMAGE, "lecture du dommage, phrase")
    jeux = l2.get("jeux")
    if not isinstance(jeux, dict) or set(jeux) != set(JEUX):
        raise GardeArret(f"lecture de la diffusion : jeux attendus {list(JEUX)} (manquants ou en trop)")
    etats_jeux = {}
    for k in JEUX:
        if not isinstance(jeux[k], dict):
            raise GardeArret(f"lecture de la diffusion, jeu {k} : objet attendu")
        etats_jeux[k] = _dans(jeux[k].get("etat"), ETATS, f"lecture de la diffusion, jeu {k}")
    unites = (l2.get("etat_par_unite") or {}).get("unites") if isinstance(l2.get("etat_par_unite"), dict) else None
    if not isinstance(unites, dict) or set(unites) != set(UNITES):
        raise GardeArret(f"lecture de la diffusion : unités attendues {list(UNITES)} (manquantes ou en trop)")
    etats_unites = {}
    for u in UNITES:
        if not isinstance(unites[u], dict):
            raise GardeArret(f"lecture de la diffusion, unité {u} : objet attendu")
        etats_unites[u] = _dans(unites[u].get("etat"), ETATS, f"lecture de la diffusion, unité {u}")
    if "phrase" not in l2:
        raise GardeArret("lecture de la diffusion : clé phrase absente")
    phrase_2 = _dans(l2["phrase"], PHRASES_DIFFUSION, "lecture de la diffusion, phrase")
    par_paire = {u: {"cout": etats_jeux[f"cout/{u}"], "traits": etats_jeux[f"traits/{u}"],
                     "mots_et_cout": etats_jeux[f"mots_et_cout/{u}"], "unite": etats_unites[u]} for u in UNITES}
    par_paire["B100-TJ100"] = {"mots_et_cout": etats_jeux["mots_et_cout/B100-TJ100"]}
    return {"avertissement": AVERTISSEMENT, "run_id": run_id, "lecture_dommage": {"phrase": phrase_1},
            "lecture_diffusion": {"par_paire": par_paire, "phrase": phrase_2}}


def main(argv: list[str]) -> int:
    p = argparse.ArgumentParser(prog="extrait_iib_etats_lectures_cote_moniteurs_v1")
    p.add_argument("--racine", default=".")
    p.add_argument("--run-id", required=True)
    p.add_argument("--sortie", required=True)
    a = p.parse_args(argv)
    try:
        sortie = Path(a.sortie)
        if sortie.exists() or Path(str(sortie) + ".sha256").exists():
            raise GardeArret(f"{sortie} existe déjà : R12 interdit d'écraser")
        extrait = construire(Path(a.racine), a.run_id)
        sortie.parent.mkdir(parents=True, exist_ok=True)
        sortie.write_text(json.dumps(extrait, indent=2, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")
        sha = sceller(sortie)
    except GardeArret as e:
        print(f"EXTRAIT DES ÉTATS REFUSÉ : {e}", file=sys.stderr)
        return 1
    print(f"EXTRAIT DES ÉTATS ÉCRIT : {sortie} sha256 {sha}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
