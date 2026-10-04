"""Épisodes du harnais, indexés par (agent i, pas t) dès le premier jour.

Un épisode : à chaque pas t, chaque agent i (dans l'ordre « temps d'abord », comme les agrégateurs)
lit sa consigne privée, son historique et une observation, puis produit une action. La transcription
de chaque agent est tenue en identifiants de jetons, jamais retokenisée : l'empan de chaque action dans
la transcription est exact. Les activations viennent d'une passe avant unique sur la transcription
complète ; la génération, sur un échantillon d'actions, capture aussi ses activations pour la garde
d'équivalence.

Plusieurs épisodes se jouent en pas synchronisés (`jouer_episodes`) : à chaque (pas t, agent i), les
actions de tous les épisodes du lot sont générées ensemble, remplies à gauche, avec positions
explicites et une graine par action. Le rejeu au bit près suppose le même plan de lots.
"""
from __future__ import annotations

import hashlib
import json
import time
from dataclasses import asdict, dataclass, field

import numpy as np
import torch

from ..gardes import GardeArret
from .activations import (Crochets, agreger, ecart_equivalence, exiger_controle_negatif, exiger_equivalence,
                          passe_unique, profil_ecarts)
from .formats import FormatBrut


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


def generer_lot(modele, contextes: list[list[int]], max_nouveaux: int, temperature: float, graines: list[int],
                fins: set[int], pad_id: int) -> tuple[list[list[int]], dict]:
    """Échantillonnage jeton par jeton d'un lot, avec cache ; une graine et un générateur par ligne.

    Remplissage à gauche, masque d'attention et positions explicites (la position d'un jeton ne dépend pas
    du remplissage). Une ligne s'arrête à son premier jeton de `fins` (gardé dans l'action) ; les lignes
    finies reçoivent `pad_id`, sans effet sur les autres. Seuls les logits du dernier jeton sont calculés
    (mémoire : un vocabulaire de 128 000 jetons sur tout le contexte d'un lot pèserait des gigaoctets).
    Renvoie les jetons générés par ligne et le plan du lot (longueur remplie, nombre de passes de
    décodage), nécessaire pour relire les crochets."""
    if max_nouveaux < 1:
        raise GardeArret("max_nouveaux < 1")
    if not contextes or len(graines) != len(contextes) or any(len(c) == 0 for c in contextes):
        raise GardeArret("lot vide, contexte vide ou graines en nombre différent des contextes")
    B, L = len(contextes), max(len(c) for c in contextes)
    appareil = next(modele.parameters()).device
    ids = torch.full((B, L), int(pad_id), dtype=torch.long)
    masque = torch.zeros((B, L), dtype=torch.long)
    for r, c in enumerate(contextes):
        ids[r, L - len(c):] = torch.tensor(c, dtype=torch.long)
        masque[r, L - len(c):] = 1
    positions = (masque.cumsum(dim=1) - 1).clamp(min=0)
    generateurs = [torch.Generator(device="cpu").manual_seed(int(g)) for g in graines]
    nouveaux: list[list[int]] = [[] for _ in range(B)]
    actives = [True] * B
    passes = 0
    with torch.no_grad():
        sortie = modele(input_ids=ids.to(appareil), attention_mask=masque.to(appareil),
                        position_ids=positions.to(appareil), use_cache=True, logits_to_keep=1)
        suivante = positions[:, -1:] + 1
        for pas in range(max_nouveaux):
            logits = sortie.logits[:, -1].to("cpu", torch.float32)
            jetons = torch.full((B, 1), int(pad_id), dtype=torch.long)
            for r in range(B):
                if not actives[r]:
                    continue
                if temperature <= 0:
                    j = int(torch.argmax(logits[r]))
                else:
                    j = int(torch.multinomial(torch.softmax(logits[r] / temperature, dim=-1), 1, generator=generateurs[r]))
                nouveaux[r].append(j)
                jetons[r, 0] = j
                if j in fins:
                    actives[r] = False
            if not any(actives) or pas == max_nouveaux - 1:
                break
            masque = torch.cat([masque, torch.ones((B, 1), dtype=torch.long)], dim=1)
            sortie = modele(input_ids=jetons.to(appareil), attention_mask=masque.to(appareil),
                            position_ids=suivante.to(appareil), past_key_values=sortie.past_key_values, use_cache=True,
                            logits_to_keep=1)
            suivante = suivante + 1
            passes += 1
    return nouveaux, {"longueur_remplie": L, "passes_decodage": passes}


def generer(modele, contexte: list[int], max_nouveaux: int, temperature: float, graine: int, fin_id: int) -> list[int]:
    """Une seule séquence : cas particulier de `generer_lot`."""
    return generer_lot(modele, [contexte], max_nouveaux, temperature, [graine], {fin_id}, fin_id)[0][0]


def relire_crochets_lot(brut: dict[int, list[np.ndarray]], k: int, longueur_contexte: int, plan: dict,
                        n_generes: int) -> dict[int, np.ndarray]:
    """Activations de génération de la k-ième ligne capturée : positions du contexte (sans remplissage), puis
    un jeton par passe de décodage tant que la ligne recevait ses propres jetons."""
    L, passes = plan["longueur_remplie"], plan["passes_decodage"]
    sortie = {}
    for couche, morceaux in brut.items():
        if len(morceaux) != 1 + passes or morceaux[0].shape[1] != L:
            raise GardeArret(f"couche {couche} : {len(morceaux)} captures pour {1 + passes} passes, ou longueur ≠ {L}")
        utiles = [morceaux[0][k, L - longueur_contexte:]]
        utiles += [morceaux[j][k, :1] for j in range(1, 1 + min(passes, n_generes))]
        sortie[couche] = np.concatenate(utiles, axis=0)
    return sortie


def jouer_episodes(modele, fmt, environnement, identifiants: list[str], N: int, T: int, graines: list[dict],
                   couches, max_nouveaux: int = 24, temperature: float = 1.0, echantillon_equivalence=(),
                   tolerance_equivalence: float = 1e-4, pad_id: int | None = None, chrono: dict | None = None) -> list[tuple]:
    """Joue un lot d'épisodes en pas synchronisés ; renvoie, par épisode, (épisode, activations par agent et par
    couche, rapport d'équivalence).

    `graines[b][(i, t)]` : graine de l'action (i, t) de l'épisode b ; `echantillon_equivalence` : triplets
    (b, i, t) dont la génération capture aussi les activations. Pour chacun, deux gardes : génération =
    passe unique à la tolérance près ; décalée d'un jeton, la comparaison dépasse la tolérance.
    `chrono` (facultatif) cumule durées et nombres de jetons de la génération et de la passe unique."""
    B = len(identifiants)
    if N < 1 or T < 1 or B < 1:
        raise GardeArret(f"N = {N}, T = {T}, lot de {B} : au moins 1 attendu")
    if len(graines) != B:
        raise GardeArret(f"{len(graines)} jeux de graines pour {B} épisodes")
    for b in range(B):
        for t in range(T):
            for i in range(N):
                if (i, t) not in graines[b]:
                    raise GardeArret(f"graine absente pour l'action ({i}, {t}) de l'épisode {identifiants[b]}")
    pad = pad_id if pad_id is not None else (fmt.tok.pad_token_id if fmt.tok.pad_token_id is not None
                                             else min(fmt.fins))
    trs = [[Transcription(agent=i) for i in range(N)] for _ in range(B)]
    debuts = [[None] * N for _ in range(B)]
    journaux: list[list[tuple[int, int, str]]] = [[] for _ in range(B)]
    acts_generation = {}
    for t in range(T):
        for i in range(N):
            contextes = []
            for b in range(B):
                obs = environnement.observation(i, t, journaux[b])
                if t == 0:
                    debuts[b][i] = (environnement.consigne_privee(i), obs)
                    contextes.append(fmt.ouverture(*debuts[b][i]))
                else:
                    contextes.append(trs[b][i].ids + fmt.tour(debuts[b][i], obs))
            graines_lot = [graines[b][(i, t)] for b in range(B)]
            lignes = [b for b in range(B) if (b, i, t) in echantillon_equivalence]
            depart = time.perf_counter()
            if lignes:
                with Crochets(modele, couches, lignes=lignes) as c:
                    nouveaux, plan = generer_lot(modele, contextes, max_nouveaux, temperature, graines_lot, fmt.fins, pad)
                    brut = c.vider_lot()
                for k, b in enumerate(lignes):
                    acts_generation[(b, i, t)] = relire_crochets_lot(brut, k, len(contextes[b]), plan, len(nouveaux[b]))
            else:
                nouveaux, plan = generer_lot(modele, contextes, max_nouveaux, temperature, graines_lot, fmt.fins, pad)
            if chrono is not None:
                chrono["generation_s"] = chrono.get("generation_s", 0.0) + time.perf_counter() - depart
                chrono["jetons_generes"] = chrono.get("jetons_generes", 0) + sum(len(nv) for nv in nouveaux)
                chrono["jetons_contexte"] = chrono.get("jetons_contexte", 0) + sum(len(c) for c in contextes)
                chrono["jetons_contexte_remplis"] = chrono.get("jetons_contexte_remplis", 0) + B * plan["longueur_remplie"]
                chrono["passes_decodage"] = chrono.get("passes_decodage", 0) + plan["passes_decodage"]
            for b in range(B):
                ctx, nv = contextes[b], nouveaux[b]
                texte = fmt.tok.decode(nv, skip_special_tokens=True)
                trs[b][i].actions.append(Action(i, t, len(ctx), len(ctx) + len(nv), nv, texte))
                trs[b][i].ids = ctx + nv + fmt.cloture(debuts[b][i], nv)
                journaux[b].append((i, t, texte))
    sorties = []
    for b in range(B):
        episode = Episode(identifiants[b], N, T, trs[b])
        depart = time.perf_counter()
        acts = {tr.agent: passe_unique(modele, tr.ids, couches) for tr in trs[b]}
        if chrono is not None:
            chrono["passe_unique_s"] = chrono.get("passe_unique_s", 0.0) + time.perf_counter() - depart
            chrono["jetons_passe_unique"] = chrono.get("jetons_passe_unique", 0) + sum(len(tr.ids) for tr in trs[b])
        ecarts, decales, profils = {}, {}, {}
        for (bb, i, t), ag in sorted(acts_generation.items()):
            if bb != b:
                continue
            cle = f"{i},{t}"
            ecarts[cle] = ecart_equivalence(ag, acts[i])
            exiger_equivalence(ecarts[cle], tolerance_equivalence, f"{identifiants[b]}, action ({i}, {t})")
            decales[cle] = ecart_equivalence(ag, acts[i], decalage=1)
            exiger_controle_negatif(decales[cle], tolerance_equivalence, f"{identifiants[b]}, action ({i}, {t})")
            profils[cle] = profil_ecarts(ag, acts[i])
        sorties.append((episode, acts, {"tolerance": tolerance_equivalence, "ecarts": ecarts,
                                        "controle_negatif_decalage_1": decales, "profils": profils}))
    return sorties


def jouer_episode(modele, tokeniseur, environnement, identifiant: str, N: int, T: int, graines: dict,
                  couches, max_nouveaux: int = 24, temperature: float = 1.0, echantillon_equivalence=(),
                  tolerance_equivalence: float = 1e-4, fmt=None):
    """Un seul épisode : cas particulier de `jouer_episodes` (format brut par défaut).

    `graines[(i, t)]` : graine de l'action ; `echantillon_equivalence` : actions (i, t) dont la génération
    capture aussi les activations, comparées ensuite à la passe unique (garde d'arrêt)."""
    fmt = fmt or FormatBrut(tokeniseur)
    return jouer_episodes(modele, fmt, environnement, [identifiant], N, T, [graines], couches, max_nouveaux,
                          temperature, {(0, i, t) for (i, t) in echantillon_equivalence}, tolerance_equivalence)[0]


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
