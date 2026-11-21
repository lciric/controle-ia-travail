"""Précondition P1, première moitié (côté agent) : l'agent ne voit pas la référence cachée — v1.

Au coffre. Monteur de l'oracle du cycle 1. Processeur seul. Ne lit aucun moniteur : la seconde moitié de P1 (« aucun
moniteur ne lit la référence ») revient à une autre main (pièce 3 du dossier, section 6).

Trois contrôles :
  (a) la tâche passée à l'environnement (`Tache` de `environnements/propositions.py`) n'a aucun champ de référence ;
  (b) pour chaque tâche, tout texte que l'environnement montre à un agent (consigne privée de chaque agent,
      observation au premier pas) ne contient aucune suite de LONGUEUR mots consécutifs d'un élément de la
      référence (description et extrait d'appui de chaque direction fructueuse et stérile), après normalisation ;
  (c) la tâche agent se construit par `tache_agent`, qui ne copie que l'identifiant, l'énoncé et la classification.
Le lanceur des épisodes doit construire ses tâches par `tache_agent` ; sa contre-lecture (classe B) le vérifie.

Le programme ne rend que des comptes et des identifiants de tâches, jamais un texte de la référence.
"""
from __future__ import annotations

import dataclasses
import re
import sys
import unicodedata
from pathlib import Path

RACINE = Path(__file__).resolve().parents[2]
if str(RACINE / "src") not in sys.path:
    sys.path.insert(0, str(RACINE / "src"))

from controle_ia.environnements.propositions import EnvironnementPropositions, Tache, texte_classification  # noqa: E402

LONGUEUR = 8
CHAMPS_PERMIS = {"identifiant", "questions", "classification"}
TYPES_REFERENCE = ("fruitful_directions", "sterile_directions")


def mots(s: str) -> list[str]:
    s = unicodedata.normalize("NFC", s).lower()
    return re.findall(r"\w+", s)


def suites(s: str, n: int = LONGUEUR) -> set[tuple[str, ...]]:
    m = mots(s)
    return {tuple(m[i:i + n]) for i in range(len(m) - n + 1)}


def tache_agent(t: dict) -> Tache:
    """Seule voie permise de la tâche du banc vers l'agent."""
    classification = None
    if t.get("classification"):
        classification = texte_classification(t["classification"])
    return Tache(identifiant=t["identifiant"], questions=t["questions"], classification=classification)


def controle_a() -> dict:
    champs = {f.name for f in dataclasses.fields(Tache)}
    return {"champs": sorted(champs), "passe": champs <= CHAMPS_PERMIS}


def textes_vus(t: dict, N: int = 2, T: int = 3) -> list[str]:
    env = EnvironnementPropositions(tache_agent(t), N=N, T=T)
    return [env.consigne_privee(i) for i in range(N)] + [env.observation(i, 0, []) for i in range(N)]


def controle_b(taches: list[dict]) -> dict:
    touchees = []
    for t in taches:
        ref = set()
        for cle in TYPES_REFERENCE:
            for d in t["cibles"][cle]:
                ref |= suites(d.get("description", "")) | suites(d.get("evidence", ""))
        vu = set()
        for x in textes_vus(t):
            vu |= suites(x)
        n = len(ref & vu)
        if n:
            touchees.append((t["identifiant"], n))
    return {"taches": len(taches), "taches_touchees": touchees, "passe": not touchees}


def controle_c(taches: list[dict]) -> dict:
    ok = all(set(vars(tache_agent(t))) <= CHAMPS_PERMIS for t in taches)
    return {"passe": ok}


def controler(taches: list[dict]) -> dict:
    r = {"a": controle_a(), "b": controle_b(taches), "c": controle_c(taches)}
    r["passe"] = all(v["passe"] for v in r.values())
    return r


if __name__ == "__main__":  # pragma: no cover — exécution au moment des épreuves, pas à la rédaction
    import json
    taches = []
    for f in sys.argv[1:]:
        d = json.load(open(f))
        r = d.get("resultat", d) if isinstance(d, dict) else d
        taches += r["taches"] if isinstance(r, dict) else r
    res = controler(taches)
    print(json.dumps({"passe": res["passe"], "a": res["a"]["passe"], "c": res["c"]["passe"],
                      "taches": res["b"]["taches"], "taches_touchees": res["b"]["taches_touchees"]}, indent=1))
