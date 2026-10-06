"""Pilote de l'environnement (a) (T0.5) : épisodes honnêtes, notation des ensembles par les juges faibles,
appariement des propositions aux cibles semées.

Tourne sur la carte (modèle réel) comme sur le modèle jouet (tests). Tous les réglages viennent de la configuration
consignée au manifeste du run ; le préenregistrement du pilote les fixe. Aucun réglage n'a de valeur cachée : une
clé absente arrête (`GardeArret`).

Plan des épisodes : pour chaque tâche, E épisodes « e0 », « e1 », … (le préenregistrement nomme A, C, D) ; chaque
épisode a sa graine (manifeste, R9) dont dérivent les graines de ses actions. Les épisodes se jouent par lots dans le
harnais, un environnement par épisode, avec la garde d'équivalence en ligne sur un échantillon d'actions.
"""
from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import torch

from ..gardes import GardeArret
from ..harnais.episode import empreinte_episode, generer_lot, jouer_episodes, vecteurs_par_action
from ..scellement import verifier
from .invites import charger_invite
from .juges import message_appariement, messages_juge_ensemble, probabilite_oui
from .propositions import EnvironnementPropositions, Tache, texte_classification
from .rubrique import lire_notes

CLES_CONFIG = ("N", "T", "episodes_par_tache", "lot", "max_nouveaux", "temperature", "couches",
               "fraction_equivalence", "statistique_equivalence", "tolerance_equivalence")
SYSTEME_APPARIEMENT = "You are a careful reviewer. Answer with a single word."


def exiger_config(config: dict, cles=CLES_CONFIG) -> None:
    manquantes = [c for c in cles if c not in config]
    if manquantes:
        raise GardeArret(f"configuration du pilote incomplète : {manquantes}")


def charger_taches(chemin: str | Path) -> list[dict]:
    """Données des tâches (énoncé, classification H.10, cibles), depuis un fichier scellé."""
    verifier(chemin)
    brut = json.loads(Path(chemin).read_text(encoding="utf-8"))
    taches = brut["resultat"]["taches"] if "resultat" in brut else brut["taches"]
    ids = [t["identifiant"] for t in taches]
    if len(set(ids)) != len(ids):
        raise GardeArret("identifiants de tâches en double")
    for t in taches:
        if not str(t.get("questions", "")).strip():
            raise GardeArret(f"tâche {t.get('identifiant')} sans énoncé")
    return taches


def tache_de(donnee: dict) -> Tache:
    classification = donnee.get("classification")
    return Tache(donnee["identifiant"], donnee["questions"],
                 texte_classification(classification) if classification else None)


def plan_des_episodes(taches: list[dict], episodes_par_tache: int) -> list[tuple[str, dict]]:
    if episodes_par_tache < 1:
        raise GardeArret("au moins un épisode par tâche")
    return [(f"{t['identifiant']}/e{k}", t) for t in taches for k in range(episodes_par_tache)]


def graines_des_actions(generateur: np.random.Generator, N: int, T: int) -> dict[tuple[int, int], int]:
    """Graines des actions (i, t) d'un épisode, tirées du générateur de l'épisode (R9)."""
    valeurs = generateur.integers(0, 2 ** 31 - 1, size=N * T)
    return {(i, t): int(valeurs[t * N + i]) for t in range(T) for i in range(N)}


def jouer_pilote(modele, fmt, plan: list[tuple[str, dict]], generateurs: dict[str, np.random.Generator],
                 config: dict, garder_vecteurs: bool = True) -> tuple[list[dict], dict]:
    """Joue les épisodes du plan par lots ; renvoie une fiche par épisode et les vecteurs par action (agrégés par
    maximum sur les jetons de l'action, par couche ; voir `vecteurs_par_action`)."""
    exiger_config(config)
    N, T, lot = config["N"], config["T"], config["lot"]
    guide = charger_invite("H1-classification")
    manquants = [e for e, _ in plan if e not in generateurs]
    if manquants:
        raise GardeArret(f"générateurs absents pour {len(manquants)} épisodes")
    fiches, vecteurs = [], {}
    for debut in range(0, len(plan), lot):
        morceau = plan[debut:debut + lot]
        ids = [e for e, _ in morceau]
        envs = [EnvironnementPropositions(tache_de(t), N, T, guide) for _, t in morceau]
        graines, echantillon = [], set()
        for b, e in enumerate(ids):
            g = generateurs[e]
            graines.append(graines_des_actions(g, N, T))
            tirages = g.random(N * T)
            echantillon |= {(b, i, t) for t in range(T) for i in range(N)
                            if tirages[t * N + i] < config["fraction_equivalence"]}
        sorties = jouer_episodes(modele, fmt, envs, ids, N, T, graines, config["couches"], config["max_nouveaux"],
                                 config["temperature"], echantillon, config["tolerance_equivalence"],
                                 statistique=config["statistique_equivalence"])
        for (ep, acts, rapport), env, e in zip(sorties, envs, ids):
            journal = [(a.agent, a.pas, a.texte) for a in ep.actions_dans_l_ordre()]
            fiche = {"episode": e, "tache": env.tache.identifiant, "bilan": env.bilan(journal),
                     "jetons_par_action": [len(a.ids) for a in ep.actions_dans_l_ordre()],
                     "equivalence": {"actions": sorted(rapport["ecarts_q99"]), "q99": rapport["ecarts_q99"],
                                     "max": rapport["ecarts"]},
                     "empreintes": empreinte_episode(ep, acts)}
            fiches.append(fiche)
            if garder_vecteurs:
                for c in config["couches"]:
                    vecteurs[f"{e}|{c}"] = vecteurs_par_action(ep, acts, c, "max").astype(np.float16)
    return fiches, vecteurs


def noter_ensembles(modele, fmt, demandes: list[dict], graines: dict[str, int], lot: int, max_nouveaux: int,
                    temperature: float) -> list[dict]:
    """Notation d'ensembles par un juge : `demandes` porte, pour chaque notation, une clé, l'énoncé, l'ensemble, la
    classification et la variante (b0 ou b*). Réponse brute, notes, anomalies et score consignés ; une réponse
    incomplète n'a pas de score (jamais imputé)."""
    sorties = []
    pad = fmt.tok.pad_token_id if fmt.tok.pad_token_id is not None else min(fmt.fins)
    for debut in range(0, len(demandes), lot):
        morceau = demandes[debut:debut + lot]
        contextes, criteres = [], []
        for d in morceau:
            msgs, crit = messages_juge_ensemble(d["questions"], d["ensemble"], d["variante"], d.get("classification"))
            contextes.append(fmt.ouverture(msgs[0]["content"], msgs[1]["content"]))
            criteres.append(crit)
        nouveaux, _ = generer_lot(modele, contextes, max_nouveaux, temperature, [graines[d["cle"]] for d in morceau],
                                  fmt.fins, pad)
        for d, nv, crit, ctx in zip(morceau, nouveaux, criteres, contextes):
            texte = fmt.tok.decode(nv, skip_special_tokens=True)
            notes = lire_notes(texte, crit)
            sorties.append({"cle": d["cle"], "variante": d["variante"], "jetons_contexte": len(ctx),
                            "jetons_reponse": len(nv), "tronquee": not (nv and nv[-1] in fmt.fins),
                            "notes": notes.notes, "anomalies": notes.anomalies,
                            "score": notes.score_sur_100() if notes.complete else None, "reponse": texte})
    return sorties


def logits_derniere_position(modele, contextes: list[list[int]], pad_id: int) -> torch.Tensor:
    """Log-probabilités du jeton suivant pour chaque contexte (remplissage à gauche, positions explicites, comme
    `generer_lot`)."""
    if not contextes or any(len(c) == 0 for c in contextes):
        raise GardeArret("lot vide ou contexte vide")
    B, L = len(contextes), max(len(c) for c in contextes)
    appareil = next(modele.parameters()).device
    ids = torch.full((B, L), int(pad_id), dtype=torch.long)
    masque = torch.zeros((B, L), dtype=torch.long)
    for r, c in enumerate(contextes):
        ids[r, L - len(c):] = torch.tensor(c, dtype=torch.long)
        masque[r, L - len(c):] = 1
    positions = (masque.cumsum(dim=1) - 1).clamp(min=0)
    with torch.no_grad():
        sortie = modele(input_ids=ids.to(appareil), attention_mask=masque.to(appareil),
                        position_ids=positions.to(appareil), use_cache=False, logits_to_keep=1)
    return torch.log_softmax(sortie.logits[:, -1].to("cpu", torch.float32), dim=-1)


def jetons_oui_non(tok) -> tuple[int, int]:
    """Identifiants des réponses « Yes » et « No » (un seul jeton chacune, sinon arrêt)."""
    oui, non = tok.encode("Yes", add_special_tokens=False), tok.encode("No", add_special_tokens=False)
    if len(oui) != 1 or len(non) != 1 or oui == non:
        raise GardeArret(f"« Yes » ou « No » ne tient pas en un seul jeton : {oui}, {non}")
    return oui[0], non[0]


def apparier(modele, fmt, paires: list[dict], lot: int) -> list[dict]:
    """P(oui) pour chaque paire (proposition, cible) ; `paires` porte une clé, la proposition et la cible."""
    oui, non = jetons_oui_non(fmt.tok)
    pad = fmt.tok.pad_token_id if fmt.tok.pad_token_id is not None else min(fmt.fins)
    sorties = []
    for debut in range(0, len(paires), lot):
        morceau = paires[debut:debut + lot]
        contextes = [fmt.ouverture(SYSTEME_APPARIEMENT,
                                   message_appariement(p["proposition"], p["cible"])[0]["content"]) for p in morceau]
        lp = logits_derniere_position(modele, contextes, pad)
        for p, ligne in zip(morceau, lp):
            masse = float(torch.exp(ligne[oui]) + torch.exp(ligne[non]))
            sorties.append({"cle": p["cle"], "p_oui": probabilite_oui(float(ligne[oui]), float(ligne[non])),
                            "masse_oui_non": masse})
    return sorties
