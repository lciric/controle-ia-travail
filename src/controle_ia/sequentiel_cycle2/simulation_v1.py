"""Lancement de la simulation du plan séquentiel : configuration scellée → manifeste (R9) → résultats scellés.

    PYTHONPATH=src python3 -B -m controle_ia.sequentiel_cycle2.simulation_v1 --config CONFIG.json \
        --run-id AAAAMMJJ-HHMMSS-nom [--mondes nom1,nom2] [--essai-a-blanc]

Gardes : la configuration doit être scellée ; un run existant n'est jamais écrasé ; l'essai à blanc ne joue que
quelques répliques et n'écrit QUE des durées — aucun état, aucun compte.
"""
from __future__ import annotations

import argparse
import json
import sys
import time
from pathlib import Path

import numpy as np

from ..gardes import GardeArret
from ..manifeste import cle_de_tache, creer_manifeste, ecrire_resultat
from ..scellement import verifier
from . import criteres_v1 as criteres
from . import monde_gaussien_v1 as gaussien
from . import monde_scores_v1 as scores

GENRES = ("gaussien", "scores")
REPLIQUES_A_BLANC = 3


def lire_configuration(chemin: str | Path) -> dict:
    sha = verifier(chemin)     # lève si le compagnon manque ou diffère
    config = json.loads(Path(chemin).read_text(encoding="utf-8"))
    noms = [m.get("nom") for m in config.get("mondes", [])]
    if not noms or len(set(noms)) != len(noms):
        raise GardeArret("configuration : liste « mondes » absente, vide ou à noms en double")
    for m in config["mondes"]:
        if m.get("genre") not in GENRES or "config" not in m or not m.get("criteres"):
            raise GardeArret(f"monde {m.get('nom')!r} : genre, config et liste non vide de criteres attendus")
        if any(k.get("genre") not in criteres.GENRES or not k.get("etats") for k in m["criteres"]):
            raise GardeArret(f"monde {m['nom']!r} : critère de genre inconnu ou sans états")
        if m["genre"] == "scores" and not (isinstance(m.get("n_repliques"), int) and m["n_repliques"] > 0):
            raise GardeArret(f"monde {m['nom']!r} : n_repliques entier positif attendu")
    config["_sha256"] = sha
    return config


def _graine(entropie: int, nom: str, *suite: int) -> np.random.SeedSequence:
    return np.random.SeedSequence(entropie, spawn_key=(cle_de_tache(nom), *suite))


def jouer_monde(monde: dict, entropie: int, repliques: int | None = None) -> dict:
    """Comptes d'un monde. `repliques` : nombre réduit (essai à blanc) ; None : celui de la configuration."""
    nom, c = monde["nom"], dict(monde["config"])
    if monde["genre"] == "gaussien":
        if repliques is not None:
            c["n_repliques"] = repliques
        sortie = gaussien.jouer(c, _graine(entropie, nom, 0))
        return {"repliques": sortie["n_repliques"], "comptes": sortie["comptes"], "bornes_z": sortie["bornes_z"]}
    n = monde["n_repliques"] if repliques is None else repliques
    reglage = None
    if isinstance(c["amplitude"], dict):
        # {"cible": 0.05, "facteur": 1.0} : plus petite amplitude dense donnant l'écart de population visé
        reglage = scores.regler_amplitude(dict(c, amplitude=0.0), c["amplitude"]["cible"], _graine(entropie, nom, 1))
        c["amplitude"] = reglage * c["amplitude"].get("facteur", 1.0)
    comptes = {p: {"intermediaire": {}, "finale": {}, "couple": {}} for p in ("unique", "reparti", "naif")}
    for r in range(n):
        etats = scores.jouer_replique(c, _graine(entropie, nom, 2, r))
        for plan, e in etats.items():
            for cle in (("intermediaire", e["intermediaire"]), ("finale", e["finale"]),
                        ("couple", f"{e['intermediaire']}>{e['finale']}")):
                comptes[plan][cle[0]][cle[1]] = comptes[plan][cle[0]].get(cle[1], 0) + 1
    return {"repliques": n, "comptes": comptes, "amplitude_reglee": reglage}


def lancer(racine: str | Path, chemin_config: str | Path, run_id: str, mondes: list[str] | None = None,
           essai_a_blanc: bool = False, entropie: int | None = None) -> list[Path]:
    config = lire_configuration(chemin_config)
    choisis = [m for m in config["mondes"] if mondes is None or m["nom"] in mondes]
    if mondes is not None and len(choisis) != len(set(mondes)):
        raise GardeArret(f"mondes demandés absents de la configuration : {sorted(set(mondes) - {m['nom'] for m in choisis})}")
    consigne = {"configuration": str(chemin_config), "configuration_sha256": config["_sha256"],
                "mondes": [m["nom"] for m in choisis], "essai_a_blanc": essai_a_blanc}
    chemin_m, manifeste = creer_manifeste(racine, run_id, consigne, [m["nom"] for m in choisis], entropie=entropie,
                                          commande=" ".join(sys.argv))
    racine_entropie = int(next(iter(manifeste["graines"].values()))["entropie"])
    ecrits = []
    for monde in choisis:
        debut = time.monotonic()
        sortie = jouer_monde(monde, racine_entropie, REPLIQUES_A_BLANC if essai_a_blanc else None)
        duree = time.monotonic() - debut
        if essai_a_blanc:
            contenu = {"essai_a_blanc": True, "monde": monde["nom"], "repliques_jouees": sortie["repliques"],
                       "secondes": round(duree, 3)}     # ni état ni compte : rien à lire
            nom = f"essai-a-blanc-{monde['nom']}"
        else:
            contenu = {"monde": monde["nom"], "genre": monde["genre"], "config": monde["config"], **sortie,
                       "criteres": [criteres.juger(k, sortie["comptes"], sortie["repliques"])
                                    for k in monde["criteres"]],
                       "secondes": round(duree, 3)}
            nom = f"simulation-{monde['nom']}"
        ecrits.append(ecrire_resultat(racine, chemin_m, nom, contenu))
    return ecrits


def _main(argv: list[str]) -> int:
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("--config", required=True)
    p.add_argument("--run-id", required=True)
    p.add_argument("--mondes", default=None)
    p.add_argument("--essai-a-blanc", action="store_true")
    p.add_argument("--racine", default=".")
    a = p.parse_args(argv)
    ecrits = lancer(a.racine, a.config, a.run_id, a.mondes.split(",") if a.mondes else None, a.essai_a_blanc)
    print(f"{len(ecrits)} fichier(s) écrit(s) et scellé(s) ; aucun contenu affiché")
    return 0


if __name__ == "__main__":
    sys.exit(_main(sys.argv[1:]))
