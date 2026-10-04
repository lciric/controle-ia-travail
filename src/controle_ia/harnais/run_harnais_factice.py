"""Harnais de T0.4 — run factice de bout en bout sur le modèle jouet (processeur, aucune mesure).

    PYTHONPATH=src python -m controle_ia.harnais.run_harnais_factice [--racine .] [--run-id …] [--entropie …]

Chaîne :
1. manifeste (R9) ;
2. modèle jouet (graine dérivée) ;
3. épisodes (N agents, T pas), une graine par action ;
4. passe avant unique et garde d'équivalence sur toutes les actions ;
5. politique de stockage par défaut (brief, T0.4) : vecteurs d'action par maximum et scores de sondes
   calculés en ligne pour tous les épisodes ; activations par jeton seulement pour les épisodes
   d'entraînement déclarés, dont scores et vecteurs se recalculent depuis le disque (garde au bit près) ;
6. trajectoires (JSON) et tableaux (npz) scellés dans diag/<run>/ ;
7. rejeu à graines identiques, comparé au bit près ; tout écart est une réserve (brief, T0.4).

Les sondes du run sont linéaires à poids aléatoires : elles éprouvent l'instrument, elles ne mesurent rien.
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
from .episode import EnvironnementJouet, empreinte_episode, empreinte_tableaux, jouer_episode, vecteurs_par_action
from .modeles import empreinte_poids, modele_jouet, regler_determinisme, tokeniseur_caracteres
from .sondes import AGREGATIONS_SONDE, exiger_identite, scores_en_ligne, sonde_lineaire_aleatoire
from .stockage import estimer

CONFIG = {
    "objet": "harnais T0.4, run factice sur modèle jouet à poids aléatoires (aucune mesure)",
    "episodes": 2, "N": 2, "T": 3, "max_nouveaux": 24, "temperature": 1.0,
    "modele": {"couches": 4, "largeur": 64, "tetes": 4, "tetes_cle_valeur": 2, "intermediaire": 128},
    "fils": 1, "tolerance_equivalence": 1e-4,
    "politique": {"episodes_par_jeton": [0],          # épisodes d'entraînement déclarés
                  "vecteurs_par_action": ["max"],
                  "sondes": [{"nom": "lineaire-max", "couche": "mediane", "agregation": "max"},
                             {"nom": "lineaire-attention", "couche": "mediane", "agregation": "attention"}]},
    "estimation_modele_reel": {"modele": "meta-llama/Llama-3.1-8B-Instruct", "couches": 3, "largeur": 4096,
                               "jetons_par_episode": 6000, "actions_par_episode": 20, "episodes": 2000,
                               "octets_par_valeur": 2, "fraction_par_jeton": 0.1, "agregations": 1},
}
POSITIONS_COUCHE = {"precoce": 0, "mediane": 1, "tardive": 2}


def taches(config: dict) -> list[str]:
    t = ["modele"] + [f"sonde-{d['nom']}" for d in config["politique"]["sondes"]]
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


def valider_config(config: dict) -> None:
    """Gardes sur la politique de stockage, avant tout manifeste (aucun run à moitié créé)."""
    politique = config["politique"]
    if not set(politique["episodes_par_jeton"]) <= set(range(config["episodes"])):
        raise GardeArret(f"épisodes d'entraînement {politique['episodes_par_jeton']} hors de [0, {config['episodes']}[")
    for methode in politique["vecteurs_par_action"]:
        if methode not in AGREGATIONS:
            raise GardeArret(f"vecteur d'action par {methode!r} refusé : seul {AGREGATIONS} (brief, T0.7)")
    couches = couches_par_defaut(config["modele"]["couches"])
    noms = [d["nom"] for d in politique["sondes"]]
    if len(set(noms)) != len(noms):
        raise GardeArret(f"noms de sondes en double : {noms}")
    for d in politique["sondes"]:
        pos = POSITIONS_COUCHE.get(d["couche"])
        if pos is None or pos >= len(couches):
            raise GardeArret(f"sonde {d['nom']} : couche {d['couche']!r} indisponible parmi {couches}")
        if d["agregation"] not in AGREGATIONS_SONDE:
            raise GardeArret(f"sonde {d['nom']} : agrégation {d['agregation']!r} refusée ; seulement {AGREGATIONS_SONDE} "
                             "(brief, T0.7)")


def construire_sondes(config: dict, couches: list[int], graines: dict) -> list:
    sondes = []
    for d in config["politique"]["sondes"]:
        pos = POSITIONS_COUCHE.get(d["couche"])
        if pos is None or pos >= len(couches):
            raise GardeArret(f"sonde {d['nom']} : couche {d['couche']!r} indisponible parmi {couches}")
        sondes.append(sonde_lineaire_aleatoire(d["nom"], couches[pos], config["modele"]["largeur"], d["agregation"],
                                               generateur(graines[f"sonde-{d['nom']}"])))
    return sondes


def calculer_en_ligne(config: dict, episode, acts: dict, couches: list[int], sondes: list) -> tuple[dict, dict]:
    """Vecteurs d'action (par couche et par agrégation) et scores de sondes, depuis la mémoire."""
    vecteurs = {f"couche{c}/{m}": vecteurs_par_action(episode, acts, c, m)
                for c in couches for m in config["politique"]["vecteurs_par_action"]}
    return vecteurs, scores_en_ligne(episode, acts, sondes)


def ecrire_tableaux(chemin: Path, acts: dict | None, vecteurs: dict, scores: dict) -> Path:
    """npz scellé : vecteurs d'action et scores toujours ; activations par jeton si `acts` est fourni."""
    if chemin.exists():
        raise GardeArret(f"{chemin} existe déjà : R12 interdit d'écraser")
    tableaux = {f"par_action/{k}": v for k, v in vecteurs.items()}
    tableaux.update({f"scores/{k}": v for k, v in scores.items()})
    for agent, par_couche in (acts or {}).items():
        for couche, a in par_couche.items():
            tableaux[f"par_jeton/agent{agent}/couche{couche}"] = a
    np.savez(chemin, **tableaux)
    sceller(chemin)
    return chemin


def relire_et_controler(chemin: Path, config: dict, episode, couches: list[int], sondes: list, vecteurs: dict,
                        scores: dict, par_jeton: bool) -> None:
    """Garde : le disque rend ce qui a été calculé en ligne ; pour un épisode d'entraînement, scores et vecteurs
    recalculés depuis les activations par jeton relues sont identiques au bit près."""
    verifier(chemin)
    with np.load(chemin) as z:
        exiger_identite(vecteurs, {k[len("par_action/"):]: z[k] for k in z.files if k.startswith("par_action/")},
                        f"{episode.identifiant}, vecteurs relus")
        exiger_identite(scores, {k[len("scores/"):]: z[k] for k in z.files if k.startswith("scores/")},
                        f"{episode.identifiant}, scores relus")
        cles = [k for k in z.files if k.startswith("par_jeton/")]
        if not par_jeton:
            if cles:
                raise GardeArret(f"{episode.identifiant} : activations par jeton conservées hors entraînement")
            return
        acts_disque: dict[int, dict[int, np.ndarray]] = {}
        for k in cles:
            _, agent, couche = k.split("/")
            acts_disque.setdefault(int(agent[len("agent"):]), {})[int(couche[len("couche"):])] = z[k]
    v2, s2 = calculer_en_ligne(config, episode, acts_disque, couches, sondes)
    exiger_identite(vecteurs, v2, f"{episode.identifiant}, vecteurs recalculés hors ligne")
    exiger_identite(scores, s2, f"{episode.identifiant}, scores recalculés hors ligne")


def executer(racine: str | Path, run_id: str, entropie: int | None = None, config: dict | None = None) -> dict:
    racine = Path(racine)
    config = config or CONFIG
    valider_config(config)
    chemin_m, m = creer_manifeste(racine, run_id, config, taches(config), entropie=entropie,
                                  commande="python -m controle_ia.harnais.run_harnais_factice")
    politique = config["politique"]
    reglages = regler_determinisme(config["fils"])
    modele, couches, sorties = jouer_tous(config, m["graines"])
    sondes = construire_sondes(config, couches, m["graines"])

    def empreintes(ep, acts):
        vecteurs, scores = calculer_en_ligne(config, ep, acts, couches, sondes)
        return {**empreinte_episode(ep, acts), "vecteurs": empreinte_tableaux(vecteurs),
                "scores": empreinte_tableaux(scores)}, vecteurs, scores

    episodes = []
    for k, (ep, acts, eq) in enumerate(sorties):
        par_jeton = k in politique["episodes_par_jeton"]
        emp, vecteurs, scores = empreintes(ep, acts)
        ecrire_resultat(racine, chemin_m, f"{ep.identifiant}-trajectoire", ep.en_dict())
        npz = ecrire_tableaux(racine / "diag" / run_id / f"{ep.identifiant}-tableaux.npz",
                              acts if par_jeton else None, vecteurs, scores)
        relire_et_controler(npz, config, ep, couches, sondes, vecteurs, scores, par_jeton)
        episodes.append({"episode": ep.identifiant, "par_jeton_conserve": par_jeton, "empreintes": emp,
                         "equivalence": eq, "tableaux": str(npz.relative_to(racine)),
                         "controle_disque": "scores et vecteurs relus et recalculés hors ligne : identiques"
                         if par_jeton else "scores et vecteurs relus : identiques",
                         "actions": [[a.agent, a.pas, a.debut, a.fin] for a in ep.actions_dans_l_ordre()]})
    _, _, rejeu = jouer_tous(config, m["graines"])
    comparaison = [empreintes(ep, acts)[0] == e["empreintes"] for (ep, acts, _), e in zip(rejeu, episodes)]
    identique = all(comparaison)
    reserves = [] if identique else ["rejeu non identique au bit près (brief, T0.4 : tout écart est une réserve)"]
    est = config["estimation_modele_reel"]
    resume = {"reglages": reglages, "couches": couches, "empreinte_poids": empreinte_poids(modele),
              "politique": politique,
              "sondes": [{"nom": s.nom, "couche": s.couche, "agregation": s.agregation, "empreinte": s.empreinte()}
                         for s in sondes],
              "episodes": episodes, "rejeu": {"identique": identique, "par_episode": comparaison},
              "stockage_modele_reel": {"modele": est["modele"],
                                       **estimer(est["episodes"], est["jetons_par_episode"], est["actions_par_episode"],
                                                 est["couches"], est["largeur"], est["octets_par_valeur"],
                                                 est["fraction_par_jeton"], est["agregations"])},
              "reserves": reserves}
    chemin_r = ecrire_resultat(racine, chemin_m, "resume", resume)
    verifier_resultat(racine, chemin_r)
    for e in episodes:
        verifier(racine / e["tableaux"])
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
