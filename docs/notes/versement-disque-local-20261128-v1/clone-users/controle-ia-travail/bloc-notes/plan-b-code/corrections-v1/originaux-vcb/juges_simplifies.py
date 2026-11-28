"""Juges du plan B de T0.5 (préenregistrement `prereg/T0.5-plan-B-juges-v1.md`) : messages RS1 et adaptateur de notation
pour le harnais.

Messages RS1 : système = H.3, inchangé ; utilisateur = RS1 (sans espaces de bord), deux fins de ligne, puis le corps
assemblé exactement comme pour b0 (fonction gelée `juges._corps` : énoncé, classification si présente, ensemble). Seule
la rubrique change (annexe B).

Adaptateur : une notation est un épisode du harnais à un agent et un pas (N = 1, T = 1) ; la consigne privée est le
message système, l'observation le message utilisateur. `jouer_episodes` (gelé) génère alors la réponse par
`generer_lot`, avec le même contexte, la même graine et le même lot que `noter_ensembles` (gelé), et fait la passe
unique de chaque rangée : la garde d'équivalence en ligne porte sur les notations mêmes qui sont lues. Pour H.4 (b0),
les champs rendus sont exactement ceux de `noter_ensembles` (même lecture gelée, même règle de troncature) ; pour RS1,
la lecture est celle de `rubrique_simplifiee` (étapes 1 à 10 et R-225). Ce module n'appelle `generer_lot` qu'à travers
`jouer_episodes`.
"""
from __future__ import annotations

import hashlib

from ..gardes import GardeArret
from ..harnais.episode import jouer_episodes
from ..harnais.formats import verifier_format
from .invites import charger_invite
from .juges import _corps, messages_juge_ensemble
from .lancer_pilote_a import ENONCE_DE_CONTROLE
from .pilote_a import CLES_RAPPORT_GARDEES
from .rubrique import lire_notes
from .rubrique_simplifiee import (ANOMALIE_TRONQUEE, CRITERES_RS1, RACINE_INVITES_RS1, charger_invite_rs1,
                                  lire_reponse_rs1)

VARIANTES_ADAPTATEUR = ("RS1", "b0")
CLE_ACTION = "0,0"                  # clé de l'unique action (agent 0, pas 0) dans les rapports du harnais
ENSEMBLE_DE_CONTROLE = "PROPOSAL 1: Router ablation\nCompare top-1 and top-2."   # celui de `conversation_de_controle`


def messages_juge_rs1(questions: str, ensemble: str, classification: str | None = None,
                      racine=RACINE_INVITES_RS1) -> tuple[list[dict], tuple]:
    """Messages (système, utilisateur) du juge d'ensemble sous RS1 et la rubrique à lire dans sa réponse."""
    corps = _corps(questions, ensemble, classification)
    utilisateur = charger_invite_rs1(racine).strip() + "\n\n" + corps
    return [{"role": "system", "content": charger_invite("H3").strip()},
            {"role": "user", "content": utilisateur}], CRITERES_RS1


def messages_de_la_variante(demande: dict, variante: str) -> tuple[list[dict], tuple]:
    """Messages d'une demande de notation : RS1 (plan B) ou b0 (H.4, assemblage gelé de `juges.py`)."""
    if variante not in VARIANTES_ADAPTATEUR:
        raise GardeArret(f"variante de juge {variante!r} inconnue de l'adaptateur ({VARIANTES_ADAPTATEUR})")
    if variante == "RS1":
        return messages_juge_rs1(demande["questions"], demande["ensemble"], demande.get("classification"))
    return messages_juge_ensemble(demande["questions"], demande["ensemble"], "b0", demande.get("classification"))


# conversation de contrôle du format sous RS1 (contrôle (ii) du « Plan d'analyse ») : l'énoncé et l'ensemble de la
# conversation de contrôle de b0 (`lancer_pilote_a`), une réponse de juge au format de sortie de RS1
REPONSE_JUGE_DE_CONTROLE_RS1 = "SPECIFICITY: 3\nCOVERAGE: 3"


def conversation_de_controle_rs1() -> tuple[str, list[str], list[str]]:
    """Conversation de contrôle du format d'un juge sous RS1 : un tour de notation, faits des textes du run."""
    msgs, _ = messages_juge_rs1(ENONCE_DE_CONTROLE, ENSEMBLE_DE_CONTROLE, None)
    return msgs[0]["content"], [msgs[1]["content"]], [REPONSE_JUGE_DE_CONTROLE_RS1]


def controler_format_rs1(fmt, spec: dict, mode: str) -> dict:
    """Contrôle (ii) : sur la conversation de contrôle de RS1, transcription incrémentale = gabarit complet
    (`verifier_format`, gelée) ; en mode réel, texte attendu dans l'ouverture (variables du gabarit figées), exigé. Son
    format ne peut pas égaler celui, scellé, du pilote : la conversation porte une autre rubrique."""
    consigne, observations, reponses = conversation_de_controle_rs1()
    controle = verifier_format(fmt, consigne, observations, reponses)
    attendu = spec.get("texte_attendu_ouverture")
    if mode == "reel" and not attendu:
        raise GardeArret(f"{spec.get('nom')} : texte attendu dans l'ouverture absent de la configuration")
    if attendu and attendu not in fmt.tok.decode(fmt.ouverture(consigne, observations[0])):
        raise GardeArret(f"{spec.get('nom')} : ouverture sans {attendu!r} (variables du gabarit non lues)")
    return {**controle, "role": "juge", "variante": "RS1", "texte_attendu_ouverture": attendu}


class EnvironnementNotation:
    """Une demande de notation vue comme un environnement du harnais : un agent, un pas. Consigne privée = message
    système ; observation = message utilisateur. Tout autre agent ou pas, ou un journal non vide, arrête."""

    def __init__(self, demande: dict, variante: str):
        self.demande = demande
        self.variante = variante
        self.messages, self.criteres = messages_de_la_variante(demande, variante)

    def consigne_privee(self, agent: int) -> str:
        if agent != 0:
            raise GardeArret(f"notation : agent {agent}, un seul agent attendu (N = 1)")
        return self.messages[0]["content"]

    def observation(self, agent: int, pas: int, journal: list) -> str:
        if agent != 0 or pas != 0 or journal:
            raise GardeArret(f"notation : action ({agent}, {pas}) ou journal non vide ; une seule action (N = T = 1)")
        return self.messages[1]["content"]


def notation_de_l_episode(demande: dict, variante: str, criteres: tuple, episode, fins) -> dict:
    """Champs d'une notation, à partir de l'épisode joué : ceux de `noter_ensembles` (clé, variante, jetons de contexte,
    empreinte de l'ensemble, jetons et drapeau « tronquée », notes, anomalies, score, réponse). Sous RS1, en plus : la
    sensibilité « complète sans la règle de troncature » et les comptes de la lecture (descriptifs)."""
    if episode.N != 1 or episode.T != 1 or len(episode.transcriptions[0].actions) != 1:
        raise GardeArret(f"{demande['cle']} : épisode à une seule action attendu")
    action = episode.transcriptions[0].actions[0]
    nv, texte = list(action.ids), action.texte
    # une réponse sans jeton de fin est incomplète, sans score (CL-9 ; règle de `noter_ensembles`, gardée telle quelle)
    tronquee = not (nv and nv[-1] in fins)
    sortie = {"cle": demande["cle"], "variante": variante, "jetons_contexte": action.debut,
              "ensemble_sha256": hashlib.sha256(demande["ensemble"].encode("utf-8")).hexdigest(),
              "jetons_reponse": len(nv), "tronquee": tronquee}
    if variante == "b0":
        notes = lire_notes(texte, criteres)
        anomalies = notes.anomalies + ([ANOMALIE_TRONQUEE] if tronquee else [])
        sortie.update(notes=notes.notes, anomalies=anomalies,
                      score=notes.score_sur_100() if (notes.complete and not tronquee) else None, reponse=texte)
        return sortie
    if criteres != CRITERES_RS1:
        raise GardeArret(f"{demande['cle']} : critères {criteres} ≠ critères RS1")
    lu = lire_reponse_rs1(texte, tronquee)
    sortie.update(notes=lu["notes"], anomalies=lu["anomalies"], score=lu["score"], reponse=texte,
                  complete_sans_troncature=lu["complete_sans_troncature"], lecture_rs1=lu["lecture"])
    return sortie


def rapport_de_la_rangee(rapport: dict) -> dict:
    """Rapport d'équivalence d'une rangée, tel que le harnais le consigne pour son unique action (clés gardées par le
    pilote, CL-1), avec la tolérance et la statistique de la phase."""
    manquantes = [k for k in CLES_RAPPORT_GARDEES if CLE_ACTION not in rapport.get(k, {})]
    if manquantes:
        raise GardeArret(f"{rapport.get('episode')} : rapport d'équivalence sans l'action {CLE_ACTION} ({manquantes})")
    return {"tolerance": rapport["tolerance"], "statistique": rapport["statistique"],
            **{k: rapport[k][CLE_ACTION] for k in CLES_RAPPORT_GARDEES}}


def jouer_lot_de_notations(modele, fmt, demandes: list[dict], graines: dict[str, int], variante: str, couches,
                           max_nouveaux: int, temperature: float, tolerance: float, statistique: str,
                           decalage_positions: int = 0, garder_passes: bool = False) -> list[dict]:
    """Un lot de notations par `jouer_episodes` : toutes les rangées gardées (échantillon complet), garde différée.
    Rend, par rangée : la notation, le rapport d'équivalence, la longueur de la transcription et, sur demande
    (`garder_passes` : repère du rejeu), la transcription et les activations de sa passe unique. Sans cette demande,
    aucune activation ne sort de cette fonction : elles sont rendues avant le lot suivant (mémoire)."""
    if not demandes:
        raise GardeArret("lot de notations vide")
    envs = [EnvironnementNotation(d, variante) for d in demandes]
    manquantes = [d["cle"] for d in demandes if d["cle"] not in graines]
    if manquantes:
        raise GardeArret(f"graines absentes pour {manquantes[:3]}")
    sorties = jouer_episodes(modele, fmt, envs, [d["cle"] for d in demandes], 1, 1,
                             [{(0, 0): int(graines[d["cle"]])} for d in demandes], couches, max_nouveaux, temperature,
                             {(b, 0, 0) for b in range(len(demandes))}, tolerance, garde="differee",
                             decalage_positions=decalage_positions, statistique=statistique)
    lignes = []
    for d, env, (episode, acts, rapport) in zip(demandes, envs, sorties, strict=True):
        ligne = {"notation": notation_de_l_episode(d, variante, env.criteres, episode, fmt.fins),
                 "rapport": rapport_de_la_rangee(rapport),
                 "jetons_transcription": len(episode.transcriptions[0].ids)}
        if garder_passes:
            ligne["transcription"] = list(episode.transcriptions[0].ids)
            ligne["passe"] = acts[0]
        lignes.append(ligne)
    del sorties
    return lignes


def noter_par_episodes(modele, fmt, demandes: list[dict], graines: dict[str, int], lot: int, max_nouveaux: int,
                       temperature: float, couches, variante: str, tolerance: float = 0.2,
                       statistique: str = "q99") -> list[dict]:
    """Notations par lots consécutifs de `lot`, comme `noter_ensembles`, mais par `jouer_episodes` et l'adaptateur.
    Rend les seules notations (les rapports de garde sont rendus par `jouer_lot_de_notations`)."""
    sorties = []
    for debut in range(0, len(demandes), lot):
        sorties += [x["notation"] for x in jouer_lot_de_notations(
            modele, fmt, demandes[debut:debut + lot], graines, variante, couches, max_nouveaux, temperature,
            tolerance, statistique)]
    return sorties
