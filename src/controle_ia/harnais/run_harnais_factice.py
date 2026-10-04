"""Harnais de T0.4 — run factice de bout en bout sur le modèle jouet (processeur, aucune mesure).

    PYTHONPATH=src python -m controle_ia.harnais.run_harnais_factice [--racine .] [--run-id …] [--entropie …]

Chaîne :
1. manifeste (R9) ;
2. modèle jouet (graine dérivée) ;
3. épisodes (N agents, T pas), une graine par action ;
4. passe avant unique et garde d'équivalence sur toutes les actions ;
5. trajectoires (JSON) et activations (npz) scellées dans diag/<run>/ ;
6. rejeu à graines identiques, comparé au bit près ; tout écart est une réserve (brief, T0.4).
"""
from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import numpy as np

from ..gardes import GardeArret
from ..manifeste import creer_manifeste, ecrire_resultat, generateur, verifier_resultat
from ..scellement import sceller, verifier
from .activations import AGREGATIONS, couches_par_defaut
from .episode import EnvironnementJouet, empreinte_episode, jouer_episode, vecteurs_par_action
from .modeles import empreinte_poids, modele_jouet, regler_determinisme, tokeniseur_caracteres
from .stockage import estimer

CONFIG = {
    "objet": "harnais T0.4, run factice sur modèle jouet à poids aléatoires (aucune mesure)",
    "episodes": 2, "N": 2, "T": 3, "max_nouveaux": 24, "temperature": 1.0,
    "modele": {"couches": 4, "largeur": 64, "tetes": 4, "tetes_cle_valeur": 2, "intermediaire": 128},
    "fils": 1, "tolerance_equivalence": 1e-4,
    "estimation_modele_reel": {"modele": "meta-llama/Llama-3.1-8B-Instruct", "couches": 3, "largeur": 4096,
                               "jetons_par_episode": 6000, "actions_par_episode": 20, "episodes": 2000,
                               "octets_par_valeur": 2, "fraction_par_jeton": 0.1},
}


def taches(config: dict) -> list[str]:
    t = ["modele"]
    for k in range(config["episodes"]):
        t += [f"episode-{k}/action-{i}-{p}" for p in range(config["T"]) for i in range(config["N"])]
    return t


def graine_entiere(graine: dict) -> int:
    return int(generateur(graine).integers(0, 2 ** 63 - 1))


def jouer_tous(config: dict, graines: dict):
    tok = tokeniseur_caracteres()
    modele = modele_jouet(graine_entiere(graines["modele"]), len(tok), **config["modele"])
    couches = couches_par_defaut(config["modele"]["couches"])
    sorties = []
    for k in range(config["episodes"]):
        g = {(i, p): graine_entiere(graines[f"episode-{k}/action-{i}-{p}"])
             for p in range(config["T"]) for i in range(config["N"])}
        ep, acts, eq = jouer_episode(modele, tok, EnvironnementJouet(), f"episode-{k}", config["N"], config["T"], g,
                                     couches, config["max_nouveaux"], config["temperature"],
                                     echantillon_equivalence=set(g), tolerance_equivalence=config["tolerance_equivalence"])
        sorties.append((ep, acts, eq))
    return modele, couches, sorties


def ecrire_activations(chemin: Path, episode, acts: dict, couches: list[int]) -> Path:
    if chemin.exists():
        raise GardeArret(f"{chemin} existe déjà : R12 interdit d'écraser")
    tableaux = {}
    for agent, par_couche in acts.items():
        for couche, a in par_couche.items():
            tableaux[f"par_jeton/agent{agent}/couche{couche}"] = a
    for couche in couches:
        for m in AGREGATIONS:
            tableaux[f"par_action/couche{couche}/{m}"] = vecteurs_par_action(episode, acts, couche, m)
    np.savez(chemin, **tableaux)
    sceller(chemin)
    return chemin


def executer(racine: str | Path, run_id: str, entropie: int | None = None, config: dict | None = None) -> dict:
    racine = Path(racine)
    config = config or CONFIG
    chemin_m, m = creer_manifeste(racine, run_id, config, taches(config), entropie=entropie,
                                  commande="python -m controle_ia.harnais.run_harnais_factice")
    reglages = regler_determinisme(config["fils"])
    modele, couches, sorties = jouer_tous(config, m["graines"])
    episodes = []
    for ep, acts, eq in sorties:
        ecrire_resultat(racine, chemin_m, f"{ep.identifiant}-trajectoire", ep.en_dict())
        npz = ecrire_activations(racine / "diag" / run_id / f"{ep.identifiant}-activations.npz", ep, acts, couches)
        episodes.append({"episode": ep.identifiant, "empreintes": empreinte_episode(ep, acts), "equivalence": eq,
                         "activations": str(npz.relative_to(racine)),
                         "actions": [[a.agent, a.pas, a.debut, a.fin] for a in ep.actions_dans_l_ordre()]})
    _, _, rejeu = jouer_tous(config, m["graines"])
    comparaison = [empreinte_episode(ep, acts) == e["empreintes"] for (ep, acts, _), e in zip(rejeu, episodes)]
    identique = all(comparaison)
    reserves = [] if identique else ["rejeu non identique au bit près (brief, T0.4 : tout écart est une réserve)"]
    est = config["estimation_modele_reel"]
    resume = {"reglages": reglages, "couches": couches, "empreinte_poids": empreinte_poids(modele),
              "episodes": episodes, "rejeu": {"identique": identique, "par_episode": comparaison},
              "stockage_modele_reel": {"modele": est["modele"],
                                       **estimer(est["episodes"], est["jetons_par_episode"], est["actions_par_episode"],
                                                 est["couches"], est["largeur"], est["octets_par_valeur"],
                                                 est["fraction_par_jeton"])},
              "reserves": reserves}
    chemin_r = ecrire_resultat(racine, chemin_m, "resume", resume)
    verifier_resultat(racine, chemin_r)
    for e in episodes:
        verifier(racine / e["activations"])
    return {"manifeste": str(chemin_m), "resume": str(chemin_r), "rejeu_identique": identique, "reserves": reserves}


def main(argv=None) -> int:
    a = argparse.ArgumentParser()
    a.add_argument("--racine", default=".")
    a.add_argument("--run-id", default=None)
    a.add_argument("--entropie", type=int, default=None)
    args = a.parse_args(argv)
    run_id = args.run_id or datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S") + "-harnais-factice"
    print(json.dumps(executer(args.racine, run_id, args.entropie), indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except GardeArret as e:
        print(f"ARRÊT : {e}", file=sys.stderr)
        sys.exit(1)
