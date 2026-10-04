"""Épisodes du harnais, indexés par (agent i, pas t) dès le premier jour.

Un épisode : à chaque pas t, chaque agent i (dans l'ordre « temps d'abord », comme les agrégateurs)
lit sa consigne privée, son historique et une observation, puis produit une action. La transcription
de chaque agent est tenue en identifiants de jetons, jamais retokenisée : l'empan de chaque action dans
la transcription est exact. Les activations viennent d'une passe avant unique sur la transcription
complète ; la génération, sur un échantillon d'actions, capture aussi ses activations pour la garde
d'équivalence.
"""
from __future__ import annotations

import hashlib
import json
from dataclasses import asdict, dataclass, field

import numpy as np
import torch

from ..gardes import GardeArret
from .activations import Crochets, agreger, ecart_equivalence, exiger_equivalence, passe_unique


@dataclass
class Action:
    agent: int
    pas: int
    debut: int          # empan [début, fin[ dans la transcription de l'agent
    fin: int
    ids: list[int]
    texte: str


@dataclass
class Transcription:
    agent: int
    ids: list[int] = field(default_factory=list)
    actions: list[Action] = field(default_factory=list)


@dataclass
class Episode:
    identifiant: str
    N: int
    T: int
    transcriptions: list[Transcription]

    def actions_dans_l_ordre(self) -> list[Action]:
        """Ordre de lecture « temps d'abord » : (agent 0, pas 0), (agent 1, pas 0), …, (agent 0, pas 1), …"""
        par_cle = {(a.agent, a.pas): a for tr in self.transcriptions for a in tr.actions}
        return [par_cle[(i, t)] for t in range(self.T) for i in range(self.N)]

    def en_dict(self) -> dict:
        return asdict(self)


class EnvironnementJouet:
    """Environnement minimal pour développer le harnais (aucune tâche réelle : voir T0.5)."""

    def consigne_privee(self, agent: int) -> str:
        return f"Tu es l'agent {agent}. Propose une étape d'expérience, en une phrase.\n"

    def observation(self, agent: int, pas: int, journal: list[tuple[int, int, str]]) -> str:
        derniers = " | ".join(f"{i}@{t}: {texte[:20]}" for i, t, texte in journal[-3:])
        return f"Pas {pas}. Journal : {derniers}\nAgent {agent} :"


def generer(modele, contexte: list[int], max_nouveaux: int, temperature: float, graine: int, fin_id: int) -> list[int]:
    """Échantillonnage jeton par jeton avec cache, générateur à graine explicite (rejeu au bit près)."""
    if max_nouveaux < 1:
        raise GardeArret("max_nouveaux < 1")
    appareil = next(modele.parameters()).device
    g = torch.Generator(device="cpu").manual_seed(int(graine))
    nouveaux: list[int] = []
    with torch.no_grad():
        sortie = modele(torch.tensor([contexte], device=appareil), use_cache=True)
        for _ in range(max_nouveaux):
            logits = sortie.logits[0, -1].to("cpu", torch.float32)
            if temperature <= 0:
                jeton = int(torch.argmax(logits))
            else:
                proba = torch.softmax(logits / temperature, dim=-1)
                jeton = int(torch.multinomial(proba, 1, generator=g))
            nouveaux.append(jeton)
            if jeton == fin_id:
                break
            sortie = modele(torch.tensor([[jeton]], device=appareil), past_key_values=sortie.past_key_values,
                            use_cache=True)
    return nouveaux


def jouer_episode(modele, tokeniseur, environnement, identifiant: str, N: int, T: int, graines: dict,
                  couches, max_nouveaux: int = 24, temperature: float = 1.0, echantillon_equivalence=(),
                  tolerance_equivalence: float = 1e-4):
    """Joue un épisode ; renvoie (épisode, activations par agent et par couche, rapport d'équivalence).

    `graines[(i, t)]` : graine de l'action ; `echantillon_equivalence` : actions (i, t) dont la génération
    capture aussi les activations, comparées ensuite à la passe unique (garde d'arrêt)."""
    if N < 1 or T < 1:
        raise GardeArret(f"N = {N}, T = {T} : au moins 1 attendu")
    bos, fin_id = tokeniseur.bos_token_id, tokeniseur.eos_token_id
    trs = [Transcription(agent=i, ids=[bos] + tokeniseur(environnement.consigne_privee(i),
                                                         add_special_tokens=False)["input_ids"]) for i in range(N)]
    journal: list[tuple[int, int, str]] = []
    acts_generation = {}
    for t in range(T):
        for i in range(N):
            if (i, t) not in graines:
                raise GardeArret(f"graine absente pour l'action ({i}, {t})")
            obs = tokeniseur(environnement.observation(i, t, journal), add_special_tokens=False)["input_ids"]
            contexte = trs[i].ids + obs
            if (i, t) in echantillon_equivalence:
                with Crochets(modele, couches) as c:
                    nouveaux = generer(modele, contexte, max_nouveaux, temperature, graines[(i, t)], fin_id)
                    acts_generation[(i, t)] = c.vider()
            else:
                nouveaux = generer(modele, contexte, max_nouveaux, temperature, graines[(i, t)], fin_id)
            texte = tokeniseur.decode(nouveaux, skip_special_tokens=True)
            trs[i].actions.append(Action(i, t, len(contexte), len(contexte) + len(nouveaux), nouveaux, texte))
            trs[i].ids = contexte + nouveaux
            journal.append((i, t, texte))
    episode = Episode(identifiant, N, T, trs)
    acts = {tr.agent: passe_unique(modele, tr.ids, couches) for tr in trs}
    rapport = {}
    for (i, t), ag in acts_generation.items():
        ecarts = ecart_equivalence(ag, acts[i])
        exiger_equivalence(ecarts, tolerance_equivalence, f"action ({i}, {t})")
        rapport[f"{i},{t}"] = ecarts
    return episode, acts, {"tolerance": tolerance_equivalence, "ecarts": rapport}


def vecteurs_par_action(episode: Episode, acts: dict[int, dict[int, np.ndarray]], couche: int, methode: str) -> np.ndarray:
    """Tableau (N, T, largeur) des vecteurs agrégés par action, prêt pour les sondes et les agrégateurs."""
    largeur = next(iter(acts.values()))[couche].shape[1]
    sortie = np.zeros((episode.N, episode.T, largeur), dtype=np.float32)
    for a in episode.actions_dans_l_ordre():
        sortie[a.agent, a.pas] = agreger(acts[a.agent][couche], a.debut, a.fin, methode)
    return sortie


def empreinte_episode(episode: Episode, acts: dict[int, dict[int, np.ndarray]]) -> dict:
    """Empreintes de la trajectoire (identifiants et empans) et des activations, pour le rejeu au bit près."""
    traj = hashlib.sha256(json.dumps(episode.en_dict(), sort_keys=True, ensure_ascii=False).encode("utf-8")).hexdigest()
    h = hashlib.sha256()
    for agent in sorted(acts):
        for couche in sorted(acts[agent]):
            a = np.ascontiguousarray(acts[agent][couche])
            h.update(f"{agent}/{couche}/{a.shape}/{a.dtype}".encode("utf-8"))
            h.update(a.tobytes())
    return {"trajectoire": traj, "activations": h.hexdigest()}


def empreinte_tableaux(tableaux: dict) -> str:
    """Empreinte d'un dictionnaire de tableaux (clé, forme, type, octets), indépendante de l'ordre d'insertion."""
    h = hashlib.sha256()
    for cle in sorted(tableaux, key=str):
        a = np.ascontiguousarray(tableaux[cle])
        h.update(f"{cle}/{a.shape}/{a.dtype}".encode("utf-8"))
        h.update(a.tobytes())
    return h.hexdigest()
