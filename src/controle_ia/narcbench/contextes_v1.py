"""Constructeur de contextes à deux champs, v1 (brouillon 4, « Métrique », B1 et B2 ; contre-lecture 3, M1).

Un message relu est un **texte fixé** (identifiants générés, jamais retokenisés) placé derrière un **contexte** :

- champ 1, la **consigne** : l'invite système entière ;
- champ 2, la **case privée** : dans CORE, la section « PRIVATE COORDINATION … » que le gabarit des colludeurs insère entre
  les options et l'historique (tours 1 à 3) ; dans STEGO, le préfixe privé placé avant le gabarit honnête (huit mains).
  Tout le reste du message utilisateur (`avant_case`, `apres_case`) est réel et inchangé.

Les gabarits publiés (`generation/core.py`, `generation/stego.py`, commit `85fea3be2a9d`) ne sont **pas** recopiés ici : le
découpage d'un message utilisateur publié en (avant, case, après) est fait par l'étape 0 et éprouvé par la concordance au
caractère près (liste d'arrêt 2). Ce module ne connaît que les trois morceaux.

Le tokeniseur est injecté (`encoder(texte) -> list[int]`, `decoder(ids) -> str`) ; le gabarit de dialogue aussi
(`prefixe_ids(systeme, utilisateur) -> list[int]` : identifiants du contexte jusqu'au début du texte de l'agent). Le texte
relu est toujours ajouté **par identifiants** derrière ce préfixe.
"""
from __future__ import annotations

from dataclasses import dataclass, replace
from typing import Callable

import numpy as np

from ..gardes import GardeArret

PHRASE_BOURRAGE = "This line is intentionally left blank. "

# cellules (brouillon 4, table « Cellules ») ; `H-h0` : cellule proposée par la contre-lecture 3 (M1), hors brouillon 4,
# construite ici pour que le brouillon 5 puisse l'adopter sans nouveau code ; jamais jouée sans texte scellé qui la nomme.
CELLULES_COLLUDEUR = ("K-c+", "K-h+", "K-h0", "K-c0", "K-c+/rep", "K-c+/dec")
CELLULES_HONNETE = ("H-h−", "H-c−", "H-c+", "H-c0", "H-h−/rep", "H-h−/dec", "H-h−/ech", "H-h0")
SOCLE = ("K-c+", "K-h+", "K-h0", "H-h−", "H-c−", "H-c+", "K-c+/rep", "H-h−/rep", "K-c+/dec", "H-h−/dec", "H-h−/ech")
HORS_SOCLE_ORDRE_DE_RETRAIT = ("K-c0", "H-c0")
CELLULES_AVEC_CASE = ("K-c+", "K-h+", "K-h0", "K-c0", "H-c+", "H-c0", "H-h0")


@dataclass(frozen=True)
class Tokeniseur:
    encoder: Callable[[str], list]
    decoder: Callable[[list], str]
    prefixe_ids: Callable[[str, str], list]


@dataclass(frozen=True)
class Contexte:
    """Contexte d'un message : consigne (invite système) et message utilisateur en trois morceaux."""
    systeme: str
    avant_case: str
    case: str | None          # None : pas de case (honnête, tour final de CORE)
    apres_case: str

    def utilisateur(self) -> str:
        return self.avant_case + (self.case or "") + self.apres_case


@dataclass(frozen=True)
class Message:
    """Un message public généré, avec le contexte réel où il a été généré."""
    cle: str                  # identifiant stable (épisode/siège/tour)
    etage: str                # "CORE" ou "STEGO"
    scenario: str
    replicat: int
    tour: int
    siege: str                # nom complet de l'agent
    role: str                 # "colludeur", "honnete" (épisode de collusion) ou "temoin"
    contexte: Contexte
    texte_ids: tuple          # identifiants générés (empan entier, jeton de fin compris s'il y est)


def exiger_texte(texte_ids) -> tuple:
    t = tuple(int(i) for i in texte_ids)
    if not t:
        raise GardeArret("texte vide : rien à relire")
    return t


def assembler(tok: Tokeniseur, ctx: Contexte, texte_ids) -> tuple[list, int]:
    """Identifiants du contexte puis du texte fixé ; rend (identifiants, position du premier jeton du texte)."""
    pre = [int(i) for i in tok.prefixe_ids(ctx.systeme, ctx.utilisateur())]
    t = exiger_texte(texte_ids)
    return pre + list(t), len(pre)


def bourrage(tok: Tokeniseur, n_jetons: int) -> str:
    """Chaîne neutre de `n_jetons` jetons exactement (phrase répétée, tokenisée, tronquée, décodée, revérifiée)."""
    n = int(n_jetons)
    if n < 0:
        raise GardeArret(f"bourrage de {n} jetons : longueur négative")
    if n == 0:
        return ""
    texte = PHRASE_BOURRAGE
    while len(tok.encoder(texte)) < n:
        texte += PHRASE_BOURRAGE
    chaine = tok.decoder(list(tok.encoder(texte))[:n])
    if len(tok.encoder(chaine)) != n:
        raise GardeArret(f"bourrage : {n} jetons demandés, {len(tok.encoder(chaine))} obtenus après décodage (tokeniseur non "
                         "réversible sur la phrase de bourrage) ; aucun repli")
    return chaine


def neutraliser(tok: Tokeniseur, ctx_reel: Contexte, case_de_reference: str, ajustement_max: int = 1) -> tuple[Contexte, int]:
    """Remplace la case (ou l'absence de case) de `ctx_reel` par un bourrage de la longueur en jetons de `case_de_reference`,
    puis vise la **position du premier jeton du texte** du contexte où `case_de_reference` occupe la même place : ajustement
    d'au plus `ajustement_max` jeton de bourrage (liste d'arrêt 14). Rend (contexte neutralisé, ajustement appliqué) ; lève
    `ExclusionPosition` si l'égalité n'est pas atteinte (message exclu des duels qui comparent cette cellule, compté)."""
    if not case_de_reference:
        raise GardeArret("neutralisation sans case de référence : rien à neutraliser")
    reference = replace(ctx_reel, case=case_de_reference)
    cible = len(tok.prefixe_ids(reference.systeme, reference.utilisateur()))
    n0 = len(tok.encoder(case_de_reference))
    for k in [0] + [s * d for d in range(1, int(ajustement_max) + 1) for s in (1, -1)]:
        if n0 + k < 1:
            continue
        essai = replace(ctx_reel, case=bourrage(tok, n0 + k))
        if len(tok.prefixe_ids(essai.systeme, essai.utilisateur())) == cible:
            return essai, k
    raise ExclusionPosition(f"position du premier jeton du texte ≠ {cible} après ajustement de ±{ajustement_max} jeton")


class ExclusionPosition(GardeArret):
    """Liste d'arrêt 14 : la position n'est pas égale ; le message est exclu (compté), l'arrêt dépend de la proportion."""


def renommer(texte: str, ancien: str, nouveau: str) -> str:
    """Remplace le nom complet `ancien` par `nouveau` ; refuse un nom absent (renommage sans effet = artefact)."""
    if not ancien or ancien not in texte:
        raise GardeArret(f"renommage : nom {ancien!r} absent du texte")
    return texte.replace(ancien, nouveau)


def apparier(honnetes: list[str], colludeurs: list[str]) -> dict:
    """Sièges honnêtes et colludeurs triés par nom complet, premier avec premier, second avec second."""
    if len(honnetes) != 2 or len(colludeurs) != 2 or len(set(honnetes) | set(colludeurs)) != 4:
        raise GardeArret(f"appariement : deux honnêtes et deux colludeurs distincts attendus ({honnetes}, {colludeurs})")
    return dict(zip(sorted(honnetes), sorted(colludeurs)))


def longueur_l(tok: Tokeniseur, consignes_colludeur: dict, consignes_honnetes_meme_siege: dict) -> int:
    """L du contrôle `/dec` : médiane, **sur les sièges colludeurs**, de l'écart de longueur en jetons entre la consigne du
    colludeur et la consigne honnête du même siège (une statistique de longueurs, pas une sonde)."""
    if set(consignes_colludeur) != set(consignes_honnetes_meme_siege) or not consignes_colludeur:
        raise GardeArret("L : mêmes sièges attendus des deux côtés")
    ecarts = [len(tok.encoder(consignes_colludeur[s])) - len(tok.encoder(consignes_honnetes_meme_siege[s]))
              for s in sorted(consignes_colludeur)]
    return int(round(float(np.median(ecarts))))


def contextes_colludeur(tok: Tokeniseur, msg: Message, consigne_honnete_meme_siege: str, L: int) -> dict:
    """Cellules du texte d'un colludeur : nom → Contexte (ou ExclusionPosition, gardée pour le compte)."""
    if msg.role != "colludeur":
        raise GardeArret(f"{msg.cle} : texte de colludeur attendu, rôle {msg.role!r}")
    reel = msg.contexte
    sortie = {"K-c+": reel, "K-c+/rep": reel, "K-h+": replace(reel, systeme=consigne_honnete_meme_siege),
              "K-c+/dec": replace(reel, systeme=reel.systeme + bourrage(tok, L))}
    if reel.case:
        for nom, base in (("K-c0", reel), ("K-h0", sortie["K-h+"])):
            try:
                sortie[nom] = neutraliser(tok, base, reel.case)[0]
            except ExclusionPosition as e:
                sortie[nom] = e
    return sortie


def contextes_honnete(tok: Tokeniseur, msg: Message, colludeur_apparie: Message, autre_honnete: Message, L: int) -> dict:
    """Cellules du texte d'un honnête d'un épisode de collusion. Consigne du colludeur apparié **renommée** (son nom complet
    remplacé par celui de l'honnête) ; case du colludeur apparié renommée (partenaire gardé), à la place de l'absence de case."""
    if msg.role != "honnete" or colludeur_apparie.role != "colludeur" or autre_honnete.role != "honnete":
        raise GardeArret(f"{msg.cle} : rôles honnête, colludeur apparié, autre honnête attendus")
    if (msg.scenario, msg.replicat, msg.tour) != (colludeur_apparie.scenario, colludeur_apparie.replicat, colludeur_apparie.tour):
        raise GardeArret(f"{msg.cle} : colludeur apparié d'un autre épisode ou d'un autre tour")
    if msg.contexte.case is not None:
        raise GardeArret(f"{msg.cle} : un honnête n'a pas de case privée dans son contexte réel")
    reel = msg.contexte
    consigne_c = renommer(colludeur_apparie.contexte.systeme, colludeur_apparie.siege, msg.siege)
    sortie = {"H-h−": reel, "H-h−/rep": reel, "H-c−": replace(reel, systeme=consigne_c),
              "H-h−/dec": replace(reel, systeme=reel.systeme + bourrage(tok, L)),
              "H-h−/ech": replace(reel, systeme=autre_honnete.contexte.systeme)}
    case_c = colludeur_apparie.contexte.case
    if case_c:
        case_r = renommer(case_c, colludeur_apparie.siege, msg.siege) if colludeur_apparie.siege in case_c else case_c
        sortie["H-c+"] = replace(reel, systeme=consigne_c, case=case_r)
        for nom, base in (("H-c0", sortie["H-c−"]), ("H-h0", reel)):
            try:
                sortie[nom] = neutraliser(tok, base, case_r)[0]
            except ExclusionPosition as e:
                sortie[nom] = e
    return sortie


__all__ = ["Tokeniseur", "Contexte", "Message", "ExclusionPosition", "assembler", "bourrage", "neutraliser", "renommer",
           "apparier", "longueur_l", "contextes_colludeur", "contextes_honnete", "CELLULES_COLLUDEUR", "CELLULES_HONNETE",
           "SOCLE", "HORS_SOCLE_ORDRE_DE_RETRAIT", "PHRASE_BOURRAGE"]
