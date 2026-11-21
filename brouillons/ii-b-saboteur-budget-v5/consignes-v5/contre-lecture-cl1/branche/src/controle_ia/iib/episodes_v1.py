"""Épisodes de (ii-b) sans aucune activation, v1.

`jouer_lot` joue un lot d'épisodes de l'environnement (a) (N = 1) en pas synchronisés, comme `harnais.episode.jouer_episodes`
(même ordre des contextes : ouverture au pas 0, puis transcription + nouveau tour ; même clôture des tours ; une graine par
action ; génération par le modèle de l'interface `modele_v1`), **sans** crochet de capture, **sans** passe unique et **sans**
garde d'équivalence : la conception (6.3) interdit toute activation dans cette course, même en mémoire ; `jouer_episodes`
calcule toujours une passe unique des activations à la fin de chaque épisode, il n'est donc pas repris (choix déclaré).
Rend, par épisode, ses actions (identifiants générés, jamais retokenisés, et texte décodé).
"""
from __future__ import annotations

from ..gardes import GardeArret, exiger_sans_signal


def jouer_lot(modele, environnements: list, identifiants: list[str], T: int, graines: list[dict], max_nouveaux: int,
              temperature: float) -> list[dict]:
    B = len(identifiants)
    if B < 1 or len(environnements) != B or len(graines) != B:
        raise GardeArret(f"lot : {B} épisodes, {len(environnements)} environnements, {len(graines)} jeux de graines")
    for b in range(B):
        if environnements[b].N != 1 or environnements[b].T != T:
            raise GardeArret(f"épisode {identifiants[b]} : N = 1 et T = {T} attendus")
        manquantes = [t for t in range(T) if (0, t) not in graines[b]]
        if manquantes:
            raise GardeArret(f"épisode {identifiants[b]} : graines absentes aux pas {manquantes}")
    fmt = modele.fmt
    transcriptions, debuts = [[] for _ in range(B)], [None] * B
    journaux: list[list[tuple[int, int, str]]] = [[] for _ in range(B)]
    actions: list[list[dict]] = [[] for _ in range(B)]
    for t in range(T):
        exiger_sans_signal(f"au pas {t}")
        contextes = []
        for b in range(B):
            obs = environnements[b].observation(0, t, journaux[b])
            if t == 0:
                debuts[b] = (environnements[b].consigne_privee(0), obs)
                contextes.append(fmt.ouverture(*debuts[b]))
            else:
                contextes.append(transcriptions[b] + fmt.tour(debuts[b], obs))
        nouveaux = modele.generer_actions(contextes, [graines[b][(0, t)] for b in range(B)], max_nouveaux, temperature)
        if len(nouveaux) != B or any(not nv for nv in nouveaux):
            raise GardeArret(f"pas {t} : génération vide ou incomplète")
        for b in range(B):
            nv = list(nouveaux[b])
            texte = fmt.tok.decode(nv, skip_special_tokens=True)
            actions[b].append({"ids": nv, "texte": texte})
            transcriptions[b] = contextes[b] + nv + fmt.cloture(debuts[b], nv)
            journaux[b].append((0, t, texte))
    return [{"episode": identifiants[b], "actions": actions[b]} for b in range(B)]
