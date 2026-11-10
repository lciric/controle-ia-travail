"""Épisodes de (ii-b) en lots synchronisés, **sans aucune capture d'activation** (conception 6.3) : même boucle que
`harnais.episode.jouer_episodes` (contextes, graines par action, `generer_lot`, transcription jamais retokenisée), sans
crochets ni passe unique. `generer` est injectable : `harnais.episode.generer_lot` en réel ; le générateur scénarisé de
`jouet_v1` à la répétition jouet."""
from __future__ import annotations

import time

from ..environnements.pilote_a import graines_des_actions
from ..gardes import GardeArret, exiger_sans_signal
from ..harnais.episode import generer_lot
from ..manifeste import generateur


def graines_episode(g: dict, cle: str, T: int) -> dict:
    if cle not in g:
        raise GardeArret(f"graine {cle!r} absente du manifeste")
    return graines_des_actions(generateur(g[cle]), 1, T)


def lots(plan: list, taille: int):
    if taille < 1:
        raise GardeArret("lot < 1")
    for d in range(0, len(plan), taille):
        yield plan[d:d + taille]


def jouer_lot(modele, fmt, envs: list, identifiants: list[str], T: int, graines: list[dict], max_nouveaux: int,
              temperature: float, generer=generer_lot, chrono: dict | None = None) -> list[dict]:
    B = len(identifiants)
    if B < 1 or len(envs) != B or len(graines) != B:
        raise GardeArret(f"lot : {B} épisodes, {len(envs)} environnements, {len(graines)} jeux de graines")
    pad = fmt.tok.pad_token_id if fmt.tok.pad_token_id is not None else min(fmt.fins)
    ids = [[] for _ in range(B)]
    debuts = [None] * B
    journaux = [[] for _ in range(B)]
    actions = [[] for _ in range(B)]
    textes = [[] for _ in range(B)]
    for t in range(T):
        exiger_sans_signal(f"épisodes, pas {t}")
        contextes = []
        for b in range(B):
            obs = envs[b].observation(0, t, journaux[b])
            if t == 0:
                debuts[b] = (envs[b].consigne_privee(0), obs)
                contextes.append(fmt.ouverture(*debuts[b]))
            else:
                contextes.append(ids[b] + fmt.tour(debuts[b], obs))
        depart = time.perf_counter()
        nouveaux, _ = generer(modele, contextes, max_nouveaux, temperature, [graines[b][(0, t)] for b in range(B)],
                              fmt.fins, pad)
        if chrono is not None:
            chrono["generation_s"] = chrono.get("generation_s", 0.0) + time.perf_counter() - depart
            chrono["jetons_generes"] = chrono.get("jetons_generes", 0) + sum(len(n) for n in nouveaux)
        for b in range(B):
            nv = [int(x) for x in nouveaux[b]]
            if not nv:
                raise GardeArret(f"{identifiants[b]} : action vide au pas {t}")
            texte = fmt.tok.decode(nv, skip_special_tokens=True)
            actions[b].append(nv)
            textes[b].append(texte)
            ids[b] = contextes[b] + nv + fmt.cloture(debuts[b], nv)
            journaux[b].append((0, t, texte))
    return [{"episode": identifiants[b], "actions": actions[b], "textes": textes[b], "transcription": ids[b]}
            for b in range(B)]
