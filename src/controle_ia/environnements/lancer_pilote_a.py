"""Lanceur du pilote 8B de l'environnement (a) (T0.5), côté machine de calcul.

Enchaîne, sous un manifeste de run décisif (préenregistrement scellé exigé, R1) :
1. épisodes honnêtes de l'agent (8B), un environnement par épisode, garde d'équivalence en ligne ;
2. notation des ensembles finaux par le juge 8B puis le juge 3B (invite b0) : épisodes e0 notés deux fois (runs A et B
   de la décomposition de l'annexe C.1), les autres une fois ;
3. appariement de chaque proposition finale à chaque cible semée de sa tâche, par le 8B (probabilité du jeton) ;
4. résultats scellés, rattachés au manifeste ; vecteurs par action sous `donnees/<run>/` (hors git), empreinte consignée.

Mode « jouet » (tests et répétitions sur processeur) : modèle jouet et tokeniseur par caractères à la place des
modèles réels ; même chaîne, mêmes gardes.
"""
from __future__ import annotations

import argparse
import json
import sys
import time
from pathlib import Path

import numpy as np

from ..gardes import GardeArret
from ..harnais.run_harnais_factice import graine_entiere
from ..manifeste import creer_manifeste, ecrire_resultat, generateur, lire_manifeste
from ..scellement import sceller
from .pilote_a import apparier, charger_taches, exiger_config, jouer_pilote, noter_ensembles, plan_des_episodes

CLES_LANCEMENT = ("agent", "juges", "episodes_notes_deux_fois", "lot_juge", "max_nouveaux_juge", "temperature_juge",
                  "variante_juge", "lot_appariement", "duree_max_s", "mode")


def cles_des_graines(plan, config) -> list[str]:
    """Une tâche du manifeste par épisode et par notation (R9)."""
    cles = [e for e, _ in plan]
    for j in config["juges"]:
        for e, _ in plan:
            for p in range(passes_de(e, config)):
                cles.append(f"juge-{j['nom']}/{e}/passe-{p}")
    return cles


def passes_de(episode: str, config: dict) -> int:
    return 2 if episode.rsplit("/e", 1)[1] in {str(k) for k in config["episodes_notes_deux_fois"]} else 1


def demandes_de_notation(fiches, taches_par_id, config, nom_juge: str) -> list[dict]:
    demandes = []
    for f in fiches:
        t = taches_par_id[f["tache"]]
        ensemble = f["bilan"]["ensemble"]
        if not ensemble.strip():
            continue  # ensemble vide (aucune action valide) : rien à noter, compté au bilan
        for p in range(passes_de(f["episode"], config)):
            demandes.append({"cle": f"juge-{nom_juge}/{f['episode']}/passe-{p}", "questions": t["questions"],
                             "ensemble": ensemble, "classification": None, "variante": config["variante_juge"]})
    return demandes


def paires_d_appariement(fiches, taches_par_id) -> list[dict]:
    paires = []
    for f in fiches:
        cibles = taches_par_id[f["tache"]].get("cibles") or {}
        for prop in f["bilan"]["propositions"]:
            texte = "\n".join(x for x in (prop["titre"], prop["texte"], prop.get("controles") or "") if x)
            for famille in ("controls", "fruitful_directions", "sterile_directions"):
                for c in cibles.get(famille, []):
                    paires.append({"cle": f"{f['episode']}/{prop['numero']}/{c['id']}", "proposition": texte,
                                   "cible": c["description"]})
    return paires


def charger_modele_et_format(spec: dict, mode: str, graine_jouet: int):
    """Modèle et format (réel : révision figée, date du gabarit figée ; jouet : modèle par caractères)."""
    from ..harnais.formats import FormatChat
    from ..harnais.modeles import fins_du_modele, modele_jouet, tokeniseur_caracteres_chat

    if mode == "jouet":
        tok = tokeniseur_caracteres_chat()
        m = modele_jouet(graine_jouet, len(tok), couches=4, largeur=32, tetes=4, tetes_cle_valeur=2, intermediaire=64)
        return m, FormatChat(tok, fins={tok.convert_tokens_to_ids("<|im_end|>"), tok.eos_token_id})
    from ..harnais.modeles import charger_modele

    m, tok = charger_modele(spec["modele"], spec["revision"], "bfloat16", "cuda", "sdpa")
    fmt = FormatChat(tok, variables=spec["variables_gabarit"])
    fmt.fins = fins_du_modele(m, tok) | {fmt._pieces(("x", "y"))["cloture"][0]}
    return m, fmt


def executer(config: dict, racine: Path, run_id: str, prereg: str | None, chemin_taches: str,
             autoriser_depot_sale: bool = False) -> dict:
    exiger_config(config)
    manquantes = [c for c in CLES_LANCEMENT if c not in config]
    if manquantes:
        raise GardeArret(f"configuration du lancement incomplète : {manquantes}")
    if config["mode"] not in ("reel", "jouet"):
        raise GardeArret(f"mode {config['mode']!r} inconnu")
    taches = charger_taches(chemin_taches)
    par_id = {t["identifiant"]: t for t in taches}
    plan = plan_des_episodes(taches, config["episodes_par_tache"])
    chemin_m, manifeste = creer_manifeste(racine, run_id, config, cles_des_graines(plan, config) + ["modele-jouet"],
                                          decisif=prereg is not None, prereg=prereg,
                                          autoriser_depot_sale=autoriser_depot_sale)
    g = manifeste["graines"]
    echeance = time.perf_counter() + float(config["duree_max_s"])
    debut = time.perf_counter()

    modele, fmt = charger_modele_et_format(config["agent"], config["mode"], graine_entiere(g["modele-jouet"]))
    generateurs = {e: generateur(g[e]) for e, _ in plan}
    fiches, vecteurs = jouer_pilote(modele, fmt, plan, generateurs, config, echeance=echeance)
    donnees = racine / "donnees" / run_id
    donnees.mkdir(parents=True, exist_ok=False)
    chemin_v = donnees / "vecteurs-par-action.npz"
    np.savez(chemin_v, **{k.replace("/", "__"): v for k, v in vecteurs.items()})
    sha_v = sceller(chemin_v)
    ecrire_resultat(racine, chemin_m, "episodes", {"fiches": fiches, "vecteurs": str(chemin_v.relative_to(racine)),
                                                   "vecteurs_sha256": sha_v,
                                                   "duree_s": round(time.perf_counter() - debut, 1)})

    notations = {}
    for j in config["juges"]:
        if time.perf_counter() > echeance:
            raise GardeArret("limite de durée dépassée avant les notations")
        m_j, fmt_j = (modele, fmt) if j["meme_modele_que_agent"] else charger_modele_et_format(
            j, config["mode"], graine_entiere(g["modele-jouet"]) + 1)
        demandes = demandes_de_notation(fiches, par_id, config, j["nom"])
        graines_j = {d["cle"]: graine_entiere(g[d["cle"]]) for d in demandes}
        notations[j["nom"]] = noter_ensembles(m_j, fmt_j, demandes, graines_j, config["lot_juge"],
                                              config["max_nouveaux_juge"], config["temperature_juge"])
        ecrire_resultat(racine, chemin_m, f"notations-{j['nom']}", {"notations": notations[j["nom"]]})
        if j["sert_a_l_appariement"]:
            paires = paires_d_appariement(fiches, par_id)
            app = apparier(m_j, fmt_j, paires, config["lot_appariement"]) if paires else []
            ecrire_resultat(racine, chemin_m, "appariements", {"juge": j["nom"], "appariements": app})
        if m_j is not modele:
            del m_j

    resume = {"episodes": len(fiches),
              "actions": sum(f["bilan"]["actions"] for f in fiches),
              "actions_valides": sum(f["bilan"]["actions_valides"] for f in fiches),
              "ensembles_vides": sum(1 for f in fiches if not f["bilan"]["ensemble"].strip()),
              "notations": {k: {"n": len(v), "completes": sum(1 for x in v if x["score"] is not None)}
                            for k, v in notations.items()},
              "duree_s": round(time.perf_counter() - debut, 1)}
    ecrire_resultat(racine, chemin_m, "resume", resume)
    lire_manifeste(chemin_m)
    return resume


def _main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(prog="python -m controle_ia.environnements.lancer_pilote_a")
    ap.add_argument("--config", required=True)
    ap.add_argument("--taches", required=True)
    ap.add_argument("--run-id", required=True)
    ap.add_argument("--prereg", default=None)
    a = ap.parse_args(argv)
    from ..scellement import verifier

    verifier(a.config)
    config = json.loads(Path(a.config).read_text(encoding="utf-8"))
    resume = executer(config, Path("."), a.run_id, a.prereg, a.taches)
    print(json.dumps(resume, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(_main(sys.argv[1:]))
