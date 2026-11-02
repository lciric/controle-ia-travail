"""Rejeu à graine, repli « lot fidèle » : refaire la génération de P3 elle-même, dans son lot, pour un épisode cible que
`resolution_graine_v1` et son repli laissent non résolus. Version 1, nom nouveau (R12) ; `resolution_graine_v1` n'est pas
modifié, il est importé (candidats, tirages exponentiels, empreinte, pièces de P3, table).

**Pourquoi.** P3 (`premier_test_ia.run.jouer_p3` → `harnais.episode.jouer_episodes` → `generer_lot`) générait par lots de
`lot` épisodes (8 en réel : deux tâches × quatre conditions, plan `plan_p3`, lots consécutifs), remplis à gauche, avec une
passe de préremplissage puis une passe par jeton avec cache (`logits_to_keep=1`), positions explicites, modèle en bfloat16
sur la carte ; logits du dernier jeton ramenés sur processeur en float32, softmax, tirage multinomial à graine. La v1 fait
une passe forcée pleine, sans lot ni cache : ses logits diffèrent aux arrondis près (vérifié sur processeur : un lot de 1
ou un remplissage différent change les bits ; l'ordre des lignes et une ligne en moins sans effet sur le remplissage,
non) et, sur une quasi-égalité, le vainqueur de la course exponentielle peut changer.

**Méthode** (`generer_lot_fidele`, `rejouer_episode_lot`, `resoudre_episode_lot`). Même lot que P3 (les sept autres lignes
reconstruites depuis leurs textes : identifiants exacts quand l'épisode est résolu — base identique, table v2 revérifiée
par l'empreinte, résolu par la v1 ou plus tôt par cette étape, revérifiés par l'empreinte — sinon découpage canonique à
longueur forcée, **déclaré** ligne par ligne ; sur les pièces réelles, les quatre non résolus de la table v2 ont une à
trois lignes approchées dans leur lot, toutes à un ou quelques jetons d'écart canonique, longueur forcée exacte), même
remplissage à gauche, même ordre d'appels, mêmes positions, mêmes conversions ; à chaque pas de la ligne
cible, le jeton retenu est le candidat compatible avec les octets restants du texte stocké qui maximise p / q
(`softmax(logits / température)` en float32 sur processeur, divisé par les tirages exponentiels de la graine : l'opération
même de P3, `argmax(p / q) = multinomial`, fait établi dans `resolution_graine_v1`, vérifié au lancement). Les autres
lignes reçoivent leurs jetons connus (forçage) et s'arrêtent au pas que donnent `jetons` ; les passes s'arrêtent dès que
la ligne cible est finie (les passes suivantes ne touchent pas à ses logits : chaque ligne d'un lot ne dépend des autres
que par la forme du lot, taille et longueur remplie). Arbitre unique : l'empreinte de trajectoire de P3. Repli écrit comme
la v1 : bascule des quasi-égalités (une, puis deux ; combinaisons bornées par `combinaisons_max_lot`), chaque essai rejoué
depuis l'action basculée. Consigné par pas comme la v1 (choix contraint, choix non contraint = le tirage même de P3 si les
logits sont les siens, candidats, écart, marge) ; par pas de l'épisode, l'empreinte sha256 des logits de la ligne cible
(même calcul que `generer_lot(empreinte_logits=True)`), comparée à une référence quand elle existe (essais).

**Non reproduit à l'identique, déclaré** : le type (bfloat16 sur A100 en réel : même carte et mêmes réglages exigés par la
configuration, jamais garantis au bit près entre deux exécutions), le noyau d'attention (celui de la configuration de
P3, exigé égal), les jetons des lignes non résolues (découpage canonique, jeton de fin par défaut : longueur du contexte
juste à un jeton de clôture près), les passes après la fin de la ligne cible.

Interdits respectés par construction (comme la v1) : aucun score, aucune note, aucune activation ; consignes lues par
`charger_consignes` seulement.

    PYTHONPATH=src python -m controle_ia.runs_nuit.resolution_graine_lot_v1 --etape validation-lot --config CONFIG \\
        --run-id AAAAMMJJ-HHMMSS-r1-graine-lot-validation --prereg prereg/R1-addendum-relance-v2.md
    PYTHONPATH=src python -m controle_ia.runs_nuit.resolution_graine_lot_v1 --etape resolution-lot --config CONFIG \\
        --run-id AAAAMMJJ-HHMMSS-r1-graine-lot-resolution --prereg prereg/R1-addendum-relance-v2.md \\
        --validation diag/<run de validation-lot>/resolution-graine-validation-lot.json \\
        --resolution diag/<run de résolution v1>/resolution-graine-resolution.json
"""
from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import math
import signal
import sys
import time
from dataclasses import dataclass
from pathlib import Path

import numpy as np
import torch

from ..gardes import GardeArret, exiger_sans_signal, lever_sur_term, motif_d_arret, relever_term_apres
from ..manifeste import creer_manifeste, ecrire_resultat, lire_manifeste, verifier_resultat
from ..scellement import sceller
from . import resolution_graine_v1 as rg
from .rejeu_activations_v1 import episode_harnais, empreinte_trajectoire
from .resolution_graine_v1 import Cible, Compteurs, Contradiction, NonResolu, Reglages, Vocabulaire

VERSION = "resolution_graine_lot_v1"
COMMANDE = "python -m controle_ia.runs_nuit.resolution_graine_lot_v1"
CONFIG_CITEE = "Configuration de la résolution à graine, lot fidèle (empreinte canonique) : `{}`"
ETAPES = ("validation-lot", "resolution-lot")
CLES_LOT = ("episodes_validation_lot", "episodes_resolution_lot", "combinaisons_max_lot", "seuil_validation_lot")
CLES = rg.CLES + CLES_LOT
SOURCE_CIBLE = "cible"
SOURCE_APPROCHEE = "canonique_approche"
REGLE = ("rejeu à graine, lot fidèle : la génération de P3 refaite dans son lot (plan_p3, lots consécutifs de `lot` "
         "épisodes), même remplissage à gauche, préremplissage puis une passe par jeton avec cache, logits du dernier "
         "jeton en float32 sur processeur ; ligne cible : à chaque pas, parmi les jetons compatibles avec les octets "
         "restants du texte stocké (dernier pas : jeton de fin si jetons − jetons_notes = 1), celui qui maximise "
         "softmax(logits / température) / q, q = tirages exponentiels de la graine ; autres lignes forcées à leurs jetons "
         "connus (exacts si résolus, sinon découpage canonique à longueur forcée, déclaré) ; arbitre unique : empreinte "
         "de trajectoire de P3 ; repli : bascule des quasi-égalités, combinaisons bornées ; sinon non résolu, cause écrite")


# --------------------------------------------------------------------------------------------------------------------
# Choix contraint sur les logits du lot


class ChoixCible:
    """Ligne cible d'un lot : à chaque pas, sur les logits (V,) float32 du pas (ceux de P3), choisit le candidat compatible
    avec le texte stocké qui maximise p / q, p = softmax(logits / température) en float32, q = tirages exponentiels du pas
    (l'opération de P3, à l'identique ; égalité exacte : plus petit identifiant, comme argmax). Journal `pas` au format
    de la v1 : (t, s, choix, non contraint, candidats, écart, second, marge, balayage)."""

    def __init__(self, voc: Vocabulaire, texte: str, n: int, a_fin: int, Q: torch.Tensor, reglages: Reglages, t: int,
                 forcages: dict | None = None, pas: list | None = None, compteurs: Compteurs | None = None):
        if a_fin not in (0, 1) or n < a_fin or n > reglages.max_nouveaux:
            raise Contradiction(t, 0, f"longueurs incohérentes (jetons {n}, fin {a_fin}, max {reglages.max_nouveaux})")
        if a_fin == 0 and n != reglages.max_nouveaux:
            raise Contradiction(t, 0, f"action sans jeton de fin de {n} jetons ≠ max_nouveaux {reglages.max_nouveaux}")
        if tuple(Q.shape) != (n, voc.V):
            raise GardeArret(f"tirages de forme {tuple(Q.shape)} ≠ ({n}, {voc.V})")
        self.voc, self.cible, self.n, self.a_fin, self.Q, self.reglages, self.t = voc, Cible(texte, voc), n, a_fin, Q, \
            reglages, t
        self.forcages = forcages or {}
        self.pas = pas
        self.compteurs = compteurs if compteurs is not None else Compteurs()
        self.etat = self.cible.initial()
        self.choisis: list[int] = []

    def choisir(self, s: int, logits: torch.Tensor) -> int:
        if s != len(self.choisis) or s >= self.n:
            raise GardeArret(f"pas {self.t} : jeton {s} demandé, {len(self.choisis)} choisis sur {self.n}")
        exiger_sans_signal(f"résolution en lot, pas {self.t}, jeton {s}")
        if self.reglages.echeance is not None and time.perf_counter() > self.reglages.echeance:
            raise GardeArret(f"limite de durée dépassée (pas {self.t}, jeton {s})")
        if tuple(logits.shape) != (self.voc.V,) or logits.dtype != torch.float32 or logits.device.type != "cpu":
            raise GardeArret(f"logits {tuple(logits.shape)} {logits.dtype} sur {logits.device} : (V,) float32 sur "
                             "processeur attendus, comme P3")
        with torch.no_grad():
            p = torch.softmax(logits / self.reglages.temperature, dim=-1)        # P3, à l'identique
            R = p / self.Q[s]
            non_contraint = int(torch.argmax(R))                                # = le tirage de P3 sur ces logits
            top = torch.topk(R, 2).values.double()
            marge = float(torch.log(top[0]) - torch.log(top[1])) if float(top[1]) > 0 else math.inf
        dernier = bool(self.a_fin and s == self.n - 1)
        balayage = False
        if dernier:
            if not self.cible.fini(self.etat):
                raise Contradiction(self.t, s, "octets du texte restants au jeton de fin")
            cands = list(self.voc.fins)
        else:
            cands, balayage = self.cible.candidats(self.etat)
            if balayage:
                self.compteurs.balayages += 1
                if self.compteurs.balayages > self.reglages.balayages_max:
                    raise NonResolu(f"caractère de remplacement : cas non simple ({self.compteurs.balayages} balayages "
                                    f"du vocabulaire > {self.reglages.balayages_max})")
            cands = cands + self.voc.speciaux_non_fins
        if not cands:
            raise Contradiction(self.t, s, "aucun jeton compatible avec le texte")
        ordre = sorted(cands)
        vals = R[torch.tensor(ordre, dtype=torch.long)]
        k = int(torch.argmax(vals))                     # premier maximum : plus petit identifiant à égalité exacte
        choix = ordre[k]
        if (self.t, s) in self.forcages:
            choix = int(self.forcages[(self.t, s)])
            if choix not in set(ordre):
                raise Contradiction(self.t, s, f"jeton forcé {choix} hors des candidats")
            k = ordre.index(choix)
        ecart, second = math.inf, -1
        if len(ordre) > 1:
            autres = vals.double().clone()
            autres[k] = -math.inf
            k2 = int(torch.argmax(autres))
            second = ordre[k2]
            vk, v2 = float(vals[k]), float(vals[k2])
            ecart = 0.0 if vk <= 0 else (math.inf if v2 <= 0 else math.log(vk) - math.log(v2))
        if self.pas is not None:
            self.pas.append((self.t, s, choix, non_contraint, len(ordre), ecart, second, marge, balayage))
        self.choisis.append(choix)
        if not dernier:
            self.etat = self.cible.avancer(self.etat, choix)
            if self.etat is None:
                raise Contradiction(self.t, s, "jeton choisi incompatible (état)")
        return choix

    def terminer(self) -> list[int]:
        if len(self.choisis) != self.n:
            raise Contradiction(self.t, len(self.choisis), f"{len(self.choisis)} jetons générés pour {self.n}")
        if not self.a_fin and not self.cible.fini(self.etat):
            raise Contradiction(self.t, self.n - 1, "octets du texte restants après le dernier jeton")
        return list(self.choisis)


# --------------------------------------------------------------------------------------------------------------------
# Génération en lot, à l'identique de P3


class MoteurLot:
    """Le modèle et ses appels, exactement ceux de `generer_lot` ; compteurs de passes et de jetons. `etiquette` : (pas t,
    jeton s) du dernier appel (essais : perturbation ciblée)."""

    def __init__(self, modele):
        self.modele = modele
        self.appareil = next(modele.parameters()).device
        self.V = int(modele.config.vocab_size)
        self.passes = 0
        self.jetons = 0
        self.etiquette = None

    def preremplir(self, ids, masque, positions):
        self.passes += 1
        self.jetons += int(ids.numel())
        return self.modele(input_ids=ids.to(self.appareil), attention_mask=masque.to(self.appareil),
                           position_ids=positions.to(self.appareil), use_cache=True, logits_to_keep=1)

    def pas(self, jetons, masque, positions, sortie):
        self.passes += 1
        self.jetons += int(jetons.numel())
        return self.modele(input_ids=jetons.to(self.appareil), attention_mask=masque.to(self.appareil),
                           position_ids=positions.to(self.appareil), past_key_values=sortie.past_key_values,
                           use_cache=True, logits_to_keep=1)

    def logits_cpu(self, sortie) -> torch.Tensor:
        """(B, V) float32 sur processeur : la conversion même de P3."""
        return sortie.logits[:, -1].to("cpu", torch.float32)


def generer_lot_fidele(moteur: MoteurLot, contextes: list[list[int]], max_nouveaux: int, temperature: float,
                       fins: set[int], pad_id: int, forces: list, longueurs: list, cible: int | None = None,
                       choix: ChoixCible | None = None, arreter_apres_cible: bool = True,
                       t: int = 0) -> tuple[list[list[int]], dict]:
    """`generer_lot` refait appel pour appel (remplissage à gauche, masque, positions explicites, préremplissage puis une
    passe par jeton avec cache, `logits_to_keep=1`, logits du dernier jeton en float32 sur processeur), sauf le tirage :
    la ligne `cible` choisit par `choix.choisir` (contrainte par le texte, p / q), les autres reçoivent `forces[r]`
    (jetons connus ; `pad_id` au-delà, compté) et s'arrêtent à leur premier jeton de `fins` ou à `longueurs[r]` jetons.
    `arreter_apres_cible` : plus aucune passe quand la ligne cible est finie (ses logits n'en dépendent pas). Rend les
    jetons par ligne et le plan (longueur remplie, passes, remplissage, empreintes sha256 des logits par ligne sur ses
    pas actifs — même calcul que `generer_lot(empreinte_logits=True)` —, empreintes par pas de la ligne cible)."""
    if max_nouveaux < 1:
        raise GardeArret("max_nouveaux < 1")
    if not contextes or any(len(c) == 0 for c in contextes):
        raise GardeArret("lot vide ou contexte vide")
    B, L = len(contextes), max(len(c) for c in contextes)
    if len(forces) != B or len(longueurs) != B:
        raise GardeArret(f"{len(forces)} forçages et {len(longueurs)} longueurs pour {B} lignes")
    if (cible is None) != (choix is None) or (cible is not None and not 0 <= cible < B):
        raise GardeArret("ligne cible et choix contraint vont ensemble (ou ni l'un ni l'autre)")
    for r in range(B):
        if r != cible and (forces[r] is None or longueurs[r] is None):
            raise GardeArret(f"ligne {r} : jetons forcés et longueur obligatoires hors de la cible")
    ids = torch.full((B, L), int(pad_id), dtype=torch.long)
    masque = torch.zeros((B, L), dtype=torch.long)
    for r, c in enumerate(contextes):
        ids[r, L - len(c):] = torch.tensor(c, dtype=torch.long)
        masque[r, L - len(c):] = 1
    positions = (masque.cumsum(dim=1) - 1).clamp(min=0)
    empreintes = [hashlib.sha256() for _ in range(B)]
    par_pas_cible: list[str] = []
    nouveaux: list[list[int]] = [[] for _ in range(B)]
    actives = [True] * B
    passes = manquants = 0
    with torch.no_grad():
        sortie = moteur.preremplir(ids, masque, positions)
        suivante = positions[:, -1:] + 1
        for pas in range(max_nouveaux):
            moteur.etiquette = (t, pas)
            logits = moteur.logits_cpu(sortie)
            if tuple(logits.shape) != (B, moteur.V):
                raise GardeArret(f"logits de forme {tuple(logits.shape)} ≠ ({B}, {moteur.V})")
            jetons = torch.full((B, 1), int(pad_id), dtype=torch.long)
            for r in range(B):
                if not actives[r]:
                    continue
                octets = logits[r].contiguous().numpy().tobytes()
                empreintes[r].update(octets)
                if r == cible:
                    par_pas_cible.append(hashlib.sha256(octets).hexdigest())
                    j = int(choix.choisir(pas, logits[r]))
                elif pas < len(forces[r]):
                    j = int(forces[r][pas])
                else:
                    j, manquants = int(pad_id), manquants + 1
                nouveaux[r].append(j)
                jetons[r, 0] = j
                if j in fins or (r != cible and len(nouveaux[r]) >= int(longueurs[r])) \
                        or (r == cible and len(nouveaux[r]) >= choix.n):
                    actives[r] = False
            if not any(actives) or pas == max_nouveaux - 1:
                break
            if arreter_apres_cible and cible is not None and not actives[cible]:
                break
            masque = torch.cat([masque, torch.ones((B, 1), dtype=torch.long)], dim=1)
            sortie = moteur.pas(jetons, masque, suivante, sortie)
            suivante = suivante + 1
            passes += 1
    plan = {"longueur_remplie": L, "passes_decodage": passes, "remplissage": [L - len(c) for c in contextes],
            "empreintes_logits": [h.hexdigest() for h in empreintes], "jetons_manquants": manquants,
            "empreintes_cible_par_pas": par_pas_cible}
    return nouveaux, plan


# --------------------------------------------------------------------------------------------------------------------
# Lignes d'un lot et rejeu d'un épisode cible


@dataclass
class LigneLot:
    """Une ligne du lot de P3 : son épisode, un environnement neuf par essai, ses textes et longueurs, ses identifiants
    par action (None pour la cible), la source de ces identifiants et si elle est exacte."""
    episode: str
    fabrique_env: object
    textes: list
    jetons: list
    jetons_notes: list
    ids: list | None
    source: str
    exacte: bool

    def forcee(self, t: int, pad_id: int) -> list[int]:
        """Jetons forcés de l'action t : identifiants connus, tronqués ou complétés par `pad_id` à `jetons[t]`."""
        nv = [int(x) for x in self.ids[t]][:int(self.jetons[t])]
        return nv + [int(pad_id)] * (int(self.jetons[t]) - len(nv))


def pad_du_format(fmt) -> int:
    """Jeton de remplissage de P3 (`jouer_episodes`, `pad_id=None`)."""
    return fmt.tok.pad_token_id if fmt.tok.pad_token_id is not None else min(fmt.fins)


def rejouer_episode_lot(moteur: MoteurLot, voc: Vocabulaire, fmt, lignes: list[LigneLot], cible: int | None, T: int,
                        Qs, reglages: Reglages, forcages=None, prefixe=None, pas=None, compteurs=None,
                        arreter_apres_cible: bool = True) -> tuple[dict | None, list, list[dict]]:
    """Un essai : les T pas du lot rejoués comme `jouer_episodes` (N = 1), contextes de chaque ligne construits sur ses
    identifiants (forcés, ou retrouvés pour la cible) ; `prefixe` : actions déjà retrouvées de la cible, reprises sans
    génération. `cible=None` : toutes les lignes forcées (contrôle des logits). Rend (reconstruction de la cible,
    identifiants par action de la cible, plans par pas). Lève `Contradiction` ou `NonResolu`."""
    B = len(lignes)
    if cible is not None and not 0 <= cible < B:
        raise GardeArret(f"ligne cible {cible} hors du lot de {B}")
    for b, x in enumerate(lignes):
        if b != cible and x.ids is None:
            raise GardeArret(f"ligne {b} ({x.episode}) sans identifiants connus")
    envs = [x.fabrique_env() for x in lignes]
    pad = pad_du_format(fmt)
    trs: list[list[int]] = [[] for _ in range(B)]
    debuts: list = [None] * B
    journaux: list[list[tuple[int, int, str]]] = [[] for _ in range(B)]
    trouves: list[list[int]] = []
    plans: list[dict] = []
    compteurs = compteurs if compteurs is not None else Compteurs()
    for t in range(T):
        exiger_sans_signal(f"lot fidèle, pas {t}")
        contextes = []
        for b in range(B):
            obs = envs[b].observation(0, t, journaux[b])
            if t == 0:
                debuts[b] = (envs[b].consigne_privee(0), obs)
                contextes.append(fmt.ouverture(*debuts[b]))
            else:
                contextes.append(trs[b] + fmt.tour(debuts[b], obs))
        nvs = [None if b == cible else lignes[b].forcee(t, pad) for b in range(B)]
        plan = None
        if cible is not None and prefixe is not None and t < len(prefixe):
            nv = [int(x) for x in prefixe[t]]
        elif cible is not None:
            lc = lignes[cible]
            n, a_fin = int(lc.jetons[t]), int(lc.jetons[t]) - int(lc.jetons_notes[t])
            choix = ChoixCible(voc, lc.textes[t], n, a_fin, Qs[t], reglages, t, forcages, pas, compteurs)
            nouveaux, plan = generer_lot_fidele(moteur, contextes, reglages.max_nouveaux, reglages.temperature, fmt.fins,
                                                pad, nvs, [int(x.jetons[t]) for x in lignes], cible, choix,
                                                arreter_apres_cible, t)
            compteurs.passes += 1
            nv = choix.terminer()
            if nouveaux[cible] != nv:
                raise GardeArret(f"pas {t} : jetons du lot ≠ jetons choisis")
            if fmt.tok.decode(nv, skip_special_tokens=True) != lc.textes[t]:
                raise Contradiction(t, len(nv), "texte décodé ≠ texte stocké")
            if any(x in fmt.fins for x in nv[:len(nv) - 1]) or bool(nv and nv[-1] in fmt.fins) != bool(a_fin):
                raise Contradiction(t, len(nv), "jeton de fin mal placé")
        else:
            nouveaux, plan = generer_lot_fidele(moteur, contextes, reglages.max_nouveaux, reglages.temperature, fmt.fins,
                                                pad, nvs, [int(x.jetons[t]) for x in lignes], None, None, False, t)
            compteurs.passes += 1
            nv = None
        if cible is not None:
            nvs[cible] = nv
            trouves.append(nv)
        plans.append({"pas": t, "longueur_remplie": None if plan is None else plan["longueur_remplie"],
                      "passes_decodage": None if plan is None else plan["passes_decodage"],
                      "remplissage_cible": None if plan is None or cible is None else plan["remplissage"][cible],
                      "jetons_manquants": None if plan is None else plan["jetons_manquants"],
                      "empreinte_logits_cible": None if plan is None or cible is None else plan["empreintes_logits"][cible],
                      "empreintes_logits": None if plan is None else plan["empreintes_logits"],
                      "longueurs_contextes": [len(c) for c in contextes]})
        for b in range(B):
            trs[b] = contextes[b] + nvs[b] + fmt.cloture(debuts[b], nvs[b])
            journaux[b].append((0, t, lignes[b].textes[t]))
    if cible is None:
        return None, [], plans
    lc = lignes[cible]
    rec = rg.transcription(fmt, envs[cible], T, lc.textes, trouves, lc.jetons, lc.jetons_notes)
    return rec, trouves, plans


def resoudre_episode_lot(moteur: MoteurLot, voc: Vocabulaire, fmt, lignes: list[LigneLot], cible: int, T: int, Qs,
                         empreinte_cible: str, reglages: Reglages, combinaisons_max: int | None = None,
                         reference_logits: list | None = None) -> dict:
    """Essai direct dans le lot fidèle, puis repli écrit (bascule des quasi-égalités, comme la v1) ; arbitre :
    `empreinte_cible`. `reference_logits` (essais) : empreintes des logits de la ligne cible par pas, comparées à celles
    de l'essai retenu (`logits_conformes`). Déclare le lot : source et exactitude de chaque ligne."""
    depart = time.perf_counter()
    lc = lignes[cible]
    if lc.ids is not None or lc.source != SOURCE_CIBLE:
        raise GardeArret(f"ligne cible {cible} : identifiants déjà connus ou source {lc.source!r}")
    cmax = reglages.combinaisons_max if combinaisons_max is None else int(combinaisons_max)
    sortie = {"episode": lc.episode, "fffd": sum(x.count(rg.FFFD) for x in lc.textes), "statut": "non_resolu",
              "voie": None, "cause": None, "forcages": [], "combinaisons_essayees": 0, "ids": None, "ids_directs": None,
              "empreinte": None, "empreinte_cible": empreinte_cible, "rang_dans_le_lot": cible,
              "lot": [{"episode": x.episode, "source": x.source, "exacte": bool(x.exacte)} for x in lignes],
              "lignes_approchees": sum(1 for x in lignes if not x.exacte), "plans": None, "empreintes_logits": None,
              "logits_conformes": None}
    pas: list = []
    compteurs = Compteurs()
    trouves_directs: list = []

    def essai(forcages, prefixe, journal_pas, cpt):
        rec, trouves, plans = rejouer_episode_lot(moteur, voc, fmt, lignes, cible, T, Qs, reglages, forcages, prefixe,
                                                  journal_pas, cpt)
        return rec, trouves, plans, empreinte_trajectoire(episode_harnais(lc.episode, T, rec))

    def retenir(plans):
        sortie["plans"] = [{k: v for k, v in p.items() if k != "empreintes_logits"} for p in plans]
        sortie["empreintes_logits"] = [p["empreinte_logits_cible"] for p in plans]
        if reference_logits is not None:
            sortie["logits_conformes"] = all(e is not None and e == r for e, r in zip(sortie["empreintes_logits"],
                                                                                      reference_logits)) \
                and len(reference_logits) == len(plans)

    try:
        rec, trouves, plans, emp = essai(None, None, pas, compteurs)
        trouves_directs = trouves
        sortie["empreinte"] = emp
        retenir(plans)
        if emp == empreinte_cible:
            sortie.update(statut="resolu", voie="directe", ids=trouves)
        else:
            sortie["cause"] = "empreinte de P3 non retrouvée à l'essai direct"
    except Contradiction as c:
        sortie["cause"] = f"contradiction à l'essai direct ({c})"
    except NonResolu as c:
        sortie.update(cause=str(c), pas=pas, balayages=compteurs.balayages, passes=compteurs.passes,
                      duree_s=round(time.perf_counter() - depart, 2))
        return sortie
    par_action: dict[int, list[int]] = {}
    for (t, s, c, *_r) in pas:
        par_action.setdefault(t, []).append(c)
    sortie["ids_directs"] = trouves_directs or [par_action[t] for t in sorted(par_action)]
    sortie.update(pas=pas, pas_direct=pas, balayages=compteurs.balayages, passes=compteurs.passes)
    if sortie["statut"] == "resolu":
        sortie["duree_s"] = round(time.perf_counter() - depart, 2)
        return sortie
    quasi = sorted((x for x in pas if x[6] >= 0 and x[5] < reglages.seuil_ecart), key=lambda x: (x[5], x[0], x[1]))
    quasi = quasi[:reglages.quasi_egalites_max]
    sortie["quasi_egalites"] = [{"pas": x[0], "rang": x[1], "choix": x[2], "second": x[6], "ecart": x[5]} for x in quasi]
    essayees = 0
    for taille in range(1, reglages.bascules_max + 1):
        for combo in itertools.combinations(quasi, taille):
            if essayees >= cmax:
                break
            essayees += 1
            forcages = {(x[0], x[1]): x[6] for x in combo}
            t0 = min(x[0] for x in combo)
            prefixe = [par_action[t] for t in range(t0)]
            journal_pas: list = [x for x in pas if x[0] < t0]
            cpt = Compteurs()
            try:
                rec, trouves, plans, emp = essai(forcages, prefixe, journal_pas, cpt)
            except (Contradiction, NonResolu):
                continue
            if emp == empreinte_cible:
                sortie.update(statut="resolu", voie="repli", ids=trouves, empreinte=emp, cause=None, pas=journal_pas,
                              forcages=[{"pas": x[0], "rang": x[1], "jeton": x[6], "ecart": x[5]} for x in combo])
                # empreintes des logits : celles de l'essai direct pour les pas repris, celles du repli ensuite
                directs = sortie["empreintes_logits"] or []
                for p in plans:
                    if p["empreinte_logits_cible"] is None and p["pas"] < len(directs):
                        p["empreinte_logits_cible"] = directs[p["pas"]]
                retenir(plans)
                sortie["combinaisons_essayees"] = essayees
                sortie["duree_s"] = round(time.perf_counter() - depart, 2)
                return sortie
    sortie["combinaisons_essayees"] = essayees
    sortie["cause"] = (f"{sortie['cause']} ; repli : {len(quasi)} quasi-égalité(s) sous {reglages.seuil_ecart}, "
                       f"{essayees} combinaison(s) essayée(s), aucune ne redonne l'empreinte")
    sortie["duree_s"] = round(time.perf_counter() - depart, 2)
    return sortie


# --------------------------------------------------------------------------------------------------------------------
# Plan des lots de P3 et lignes connues


def plan_des_lots(taches: list[dict], taille: int, lignes: list[dict]) -> list[list[str]]:
    """Lots de P3 reconstruits depuis son code (`plan_p3` : un épisode par tâche et par condition, conditions
    entremêlées ; lots consécutifs de `taille`), vérifiés contre l'ordre d'apparition des épisodes dans les textes
    stockés (écrits lot par lot, épisode par épisode) : arrêt au premier écart."""
    from ..premier_test_ia.run import plan_p3

    if isinstance(taille, bool) or not isinstance(taille, int) or taille < 1:
        raise GardeArret(f"taille de lot {taille!r} : entier ≥ 1 attendu")
    plan = [e for e, _, _ in plan_p3(taches)]
    vus: list[str] = []
    for x in lignes:
        if not vus or vus[-1] != x["episode"]:
            if x["episode"] in vus:
                raise GardeArret(f"textes de P3 : épisode {x['episode']} en plusieurs morceaux")
            vus.append(x["episode"])
    if vus != plan:
        k = next((i for i, (a, b) in enumerate(zip(vus, plan)) if a != b), min(len(vus), len(plan)))
        raise GardeArret(f"plan des lots ≠ ordre des textes de P3 (premier écart au rang {k} : "
                         f"{vus[k] if k < len(vus) else None!r} dans les textes, {plan[k] if k < len(plan) else None!r} "
                         "dans le plan)")
    return [plan[d:d + taille] for d in range(0, len(plan), taille)]


def lot_de(lots: list[list[str]], episode: str) -> tuple[int, list[str], int]:
    """(numéro du lot, épisodes du lot, rang de l'épisode dans le lot)."""
    for k, lot in enumerate(lots):
        if episode in lot:
            return k, list(lot), lot.index(episode)
    raise GardeArret(f"épisode {episode} absent du plan des lots")


def lignes_du_lot(pieces: rg.Pieces, fmt, T: int, classement: dict, lot: list[str], cible: str,
                  connus: dict | None = None) -> list[LigneLot]:
    """Lignes du lot : la cible sans identifiants ; les autres avec leurs identifiants connus (`connus` : {épisode :
    (identifiants, source)}, résolus par la v1 ou plus tôt par cette étape, revérifiés par l'empreinte de P3 ; base
    identique ; table v2 revérifiée par l'empreinte : exacts) ou, à défaut, la reconstruction de base (découpage
    canonique, fin par défaut), à longueur forcée au rejeu : approchée, déclarée."""
    connus = connus or {}
    sortie = []
    for e in lot:
        ep = rg.EpisodeP3(pieces, e, T)
        if e == cible:
            ids, source, exacte = None, SOURCE_CIBLE, True
        elif e in connus:
            ids, source, exacte = [list(x) for x in connus[e][0]], str(connus[e][1]), True
        else:
            v = rg.verite(pieces, fmt, T, classement, e)
            if v is not None:
                ent = classement[e]["entree"]
                ids, exacte = [list(x) for x in v], True
                source = "identique_base" if classement[e]["identique_base"] else f"table:{ent['methode']}"
            else:
                ids, source, exacte = [list(x) for x in classement[e]["base_nv"]], SOURCE_APPROCHEE, False
        sortie.append(LigneLot(e, ep.env, ep.textes, ep.jetons, ep.jetons_notes, ids, source, exacte))
    return sortie


# --------------------------------------------------------------------------------------------------------------------
# Configuration, gardes, étapes


def exiger_config(config: dict) -> None:
    rg.exiger_config({k: v for k, v in config.items() if k in rg.CLES})
    manquantes = [k for k in CLES_LOT if k not in config]
    if manquantes:
        raise GardeArret(f"configuration du lot fidèle incomplète : {manquantes}")
    for k in ("combinaisons_max_lot", "seuil_validation_lot"):
        if isinstance(config[k], bool) or not isinstance(config[k], int) or config[k] < 0:
            raise GardeArret(f"{k} = {config[k]!r} : entier positif ou nul attendu")
    for k in ("episodes_validation_lot", "episodes_resolution_lot"):
        if not isinstance(config[k], list) or len(set(config[k])) != len(config[k]):
            raise GardeArret(f"{k} : liste sans doublon attendue")


def exiger_meme_lot_que_p3(config: dict, manifeste_p3: dict) -> int:
    """Le noyau d'attention de la configuration est celui de P3 ; la taille de lot de P3 est lue dans son manifeste."""
    c3 = manifeste_p3["config"]
    if "lot" not in c3:
        raise GardeArret("manifeste de P3 sans taille de lot")
    if c3.get("noyau_attention", "defaut") != config["noyau_attention"]:
        raise GardeArret(f"noyau d'attention {config['noyau_attention']!r} ≠ {c3.get('noyau_attention')!r} dans P3 : "
                         "le lot fidèle exige le noyau de P3")
    return int(c3["lot"])


def exiger_resolution_v1(racine: Path, chemin, config: dict) -> tuple[list[str], dict]:
    """Le résultat scellé de l'étape « resolution » de la v1, rattaché à son manifeste, de même configuration sur les clés
    de la v1 ; rend (ses épisodes non résolus, dans l'ordre ; {épisode : identifiants} de ses épisodes résolus, à
    revérifier par l'empreinte avant usage)."""
    if not chemin:
        raise GardeArret("étape « resolution-lot » sans --resolution : le résultat de la résolution v1 est obligatoire")
    corps = verifier_resultat(racine, chemin)
    m, _ = lire_manifeste(Path(racine) / "runs" / corps["run_id"] / "manifeste.json")
    r = corps["resultat"]
    if r.get("etape") != "resolution" or r.get("version") != rg.VERSION:
        raise GardeArret(f"résolution v1 {chemin} : étape {r.get('etape')!r}, version {r.get('version')!r}")
    differentes = [k for k in rg.CLES if m["config"].get(k) != config.get(k)]
    if differentes:
        raise GardeArret(f"résolution v1 faite sous une autre configuration ({differentes})")
    resolus = {x["episode"]: x["ids"] for x in r.get("episodes", []) if x.get("statut") == "resolu" and x.get("ids")}
    return [x["episode"] for x in r["non_resolus"]], resolus


def connus_de_la_v1(pieces: rg.Pieces, fmt, T: int, resolus: dict) -> dict:
    """Identifiants résolus par la v1, chacun revérifié par l'empreinte de trajectoire de P3 (arrêt sinon) :
    {épisode : (identifiants, « resolution_v1 »)}, lignes exactes pour les lots de cette étape."""
    sortie = {}
    for e, ids in resolus.items():
        ep = rg.EpisodeP3(pieces, e, T)
        ids = [[int(x) for x in a] for a in ids]
        rec = rg.transcription(fmt, ep.env(), T, ep.textes, ids, ep.jetons, ep.jetons_notes)
        if empreinte_trajectoire(episode_harnais(e, T, rec)) != ep.empreinte:
            raise GardeArret(f"{e} : les identifiants résolus par la v1 ne redonnent pas l'empreinte de P3")
        sortie[e] = (ids, "resolution_v1")
    return sortie


def exiger_validation_lot(racine: Path, chemin, config: dict) -> dict:
    if not chemin:
        raise GardeArret("étape « resolution-lot » sans --validation : la validation-lot à l'aveugle passe d'abord")
    corps = verifier_resultat(racine, chemin)
    m, _ = lire_manifeste(Path(racine) / "runs" / corps["run_id"] / "manifeste.json")
    r = corps["resultat"]
    if r.get("etape") != "validation-lot" or r.get("lecture") != "atteint":
        raise GardeArret(f"validation-lot {chemin} : étape {r.get('etape')!r}, lecture {r.get('lecture')!r}")
    if m["config_sha256"] != rg.empreinte_config(config):
        raise GardeArret("validation-lot faite sous une autre configuration")
    rg.exiger_meme_code(racine, m["commit"])
    return corps


def episodes_de_l_etape(etape: str, config: dict, classement: dict, non_resolus_v1: list[str] | None) -> list[str]:
    """Validation-lot : `episodes_validation_lot`, chacun à identifiants connus. Résolution-lot : les non résolus de la
    v1, restreints à `episodes_resolution_lot` s'il est donné (chacun non résolu par la v1)."""
    if etape == "validation-lot":
        eps = list(config["episodes_validation_lot"])
        for e in eps:
            c = classement.get(e)
            if c is None or not (c["identique_base"] or (c["entree"] and c["entree"]["methode"] != "non_resolu")):
                raise GardeArret(f"validation-lot : épisode {e!r} absent du run ou sans identifiants connus")
        if not eps:
            raise GardeArret("episodes_validation_lot vide")
        return eps
    eps = list(config["episodes_resolution_lot"]) or list(non_resolus_v1 or [])
    hors = [e for e in eps if e not in (non_resolus_v1 or [])]
    if hors:
        raise GardeArret(f"resolution-lot : épisodes résolus par la v1 ou absents de son résultat : {hors[:3]}")
    if not eps:
        raise GardeArret("resolution-lot : aucun épisode non résolu par la v1, rien à faire")
    manquants = [e for e in eps if e not in classement]
    if manquants:
        raise GardeArret(f"resolution-lot : épisodes absents du run : {manquants[:3]}")
    return eps


def ecrire_pas(dossier: Path, etape: str, resultats: list, pas_tous: list) -> tuple[str, str]:
    """Journal des pas scellé, au format de la v1."""
    chemin = dossier / f"pas-resolution-graine-{etape}.npz"
    lignes_pas = [(i, *x) for i, pas in enumerate(pas_tous) for x in pas]
    with open(chemin, "wb") as f:
        col = list(zip(*lignes_pas)) if lignes_pas else [()] * 10
        np.savez_compressed(f, episodes=np.array([r["episode"] for r in resultats]),
                            episode=np.asarray(col[0], dtype=np.int32), pas=np.asarray(col[1], dtype=np.int16),
                            rang=np.asarray(col[2], dtype=np.int16), choix=np.asarray(col[3], dtype=np.int64),
                            non_contraint=np.asarray(col[4], dtype=np.int64),
                            candidats=np.asarray(col[5], dtype=np.int32), ecart=np.asarray(col[6], dtype=np.float64),
                            second=np.asarray(col[7], dtype=np.int64), marge=np.asarray(col[8], dtype=np.float64),
                            balayage=np.asarray(col[9], dtype=bool))
    return chemin.name, sceller(chemin)


def _executer(config, racine, run_id, chemin_m, pieces, etape, etat, debut, non_resolus_v1, resolus_v1=None) -> dict:
    from ..harnais.modeles import regler_determinisme
    from ..harnais.validation_reelle import noyau
    from .rejeu_activations_v1 import progres

    reel = config["mode"] == "reel"
    appareil = "cuda" if reel else "cpu"
    reglages_det = regler_determinisme(config["fils"], appareil)
    T = int(config["T"])
    echeance = debut + float(config["duree_max_s"])
    modele, fmt = rg._modele(config, racine, pieces)
    attendu = config["agent"].get("texte_attendu_ouverture")
    if reel and not attendu:
        raise GardeArret("agent : texte attendu dans l'ouverture absent de la configuration")
    etat["etape"] = "classement"
    classement = rg.classer(pieces, fmt, T)
    episodes = episodes_de_l_etape(etape, config, classement, non_resolus_v1)
    taille = exiger_meme_lot_que_p3(config, pieces.manifeste_p3)
    from ..environnements.pilote_a import charger_taches

    lots = plan_des_lots(charger_taches(Path(racine) / config["chemin_taches"]), taille, pieces.lignes)
    ordre = {e: k for k, lot in enumerate(lots) for e in lot}
    episodes = sorted(episodes, key=lambda e: (ordre[e], lots[ordre[e]].index(e)))
    if attendu:
        e0 = rg.EpisodeP3(pieces, episodes[0], T).env()
        if attendu not in fmt.tok.decode(fmt.ouverture(e0.consigne_privee(0), e0.observation(0, 0, []))):
            raise GardeArret(f"agent : ouverture sans {attendu!r} (variables du gabarit non lues)")
    voc = Vocabulaire(fmt.tok, fmt.fins, int(modele.config.vocab_size))
    etat["equivalence_tirage"] = rg.exiger_equivalence_tirage(voc.V)
    moteur = MoteurLot(modele)
    reglages = rg.reglages_de(config, echeance)
    cmax = int(config["combinaisons_max_lot"])
    tirages = rg.Tirages(voc.V, int(config["fils_tirages"]))
    eps = {e: rg.EpisodeP3(pieces, e, T) for e in episodes}
    connus: dict = connus_de_la_v1(pieces, fmt, T, resolus_v1 or {}) if etape == "resolution-lot" else {}
    resultats, pas_tous, pas_directs = [], [], []
    etat["etape"] = etape
    progres(etape=etape, episodes=len(episodes), lots=len(lots), taille_lot=taille)
    try:
        with noyau(config["noyau_attention"]):
            for k, e in enumerate(episodes):
                exiger_sans_signal(f"lot fidèle, épisode {k}")
                if time.perf_counter() > echeance:
                    raise GardeArret(f"limite de durée dépassée avant l'épisode {k}")
                for e2 in episodes[k:k + 1 + int(config["episodes_d_avance"])]:
                    tirages.demander(e2, eps[e2].graines, eps[e2].jetons)
                ep = eps[e]
                k_lot, lot, rang = lot_de(lots, e)
                lignes = lignes_du_lot(pieces, fmt, T, classement, lot, e, connus if etape == "resolution-lot" else None)
                Qs = tirages.prendre(e)
                r = resoudre_episode_lot(moteur, voc, fmt, lignes, rang, T, Qs, ep.empreinte, reglages, cmax)
                del Qs
                r.update(graines=ep.graines, numero_lot=k_lot)
                if r["statut"] == "resolu" and etape == "resolution-lot":
                    connus[e] = (r["ids"], "lot_fidele")
                pas_tous.append(r.pop("pas", []))
                pas_directs.append(r.pop("pas_direct", None) or pas_tous[-1])
                resultats.append(r)
                etat["episodes_traites"] = k + 1
                progres(etape=etape, episodes=f"{k + 1}/{len(episodes)}",
                        resolus=sum(x["statut"] == "resolu" for x in resultats), passes=moteur.passes)
    finally:
        tirages.fermer()
    etat["etape"] = "mesures"
    detail, ecarts, marges_desaccord, erreurs_directes = [], [], [], []
    accords, n_pas, egaux_ep, actions_egales, actions_tot = [], 0, 0, 0, 0
    for r, pas, pas_d in zip(resultats, pas_tous, pas_directs):
        e = r["episode"]
        v = rg.verite(pieces, fmt, T, classement, e) if etape == "validation-lot" else None
        ecarts += [x[5] for x in pas if x[4] > 1]
        marges_desaccord += [x[7] for x in pas if x[3] != x[2]]
        n_pas += len(pas)
        acc_v = rg.accord_non_contraint(pas, v if v is not None else r["ids"]) if (v or r["ids"]) else None
        if acc_v is not None:
            accords.append(acc_v)
        d = {k2: r[k2] for k2 in ("episode", "statut", "voie", "cause", "forcages", "combinaisons_essayees", "passes",
                                  "balayages", "fffd", "duree_s", "graines", "numero_lot", "rang_dans_le_lot", "lot",
                                  "lignes_approchees", "plans", "empreintes_logits", "empreinte_cible", "quasi_egalites")
             if k2 in r}
        d["empreinte_retrouvee"] = r["statut"] == "resolu"
        d["accord_non_contraint"] = acc_v
        d["pas"] = len(pas)
        d["ecart_min"] = min((x[5] for x in pas if x[4] > 1), default=None)
        d["ids"] = r["ids"]
        if v is not None:
            eg = r["ids"] == v
            egaux_ep += eg
            actions_tot += T
            actions_egales += sum(1 for a, b in zip(r["ids"] or [None] * T, v) if a == b)
            d["identifiants_egaux"] = eg
            pe = rg.premier_ecart(r["ids_directs"], v, pas_d)
            if pe is not None:
                erreurs_directes.append({"episode": e, **pe})
        else:
            d["base_nv"] = classement[e]["base_nv"]
        detail.append(d)
    trouvees = sum(x["statut"] == "resolu" for x in resultats)
    dossier = Path(racine) / "diag" / run_id
    dossier.mkdir(parents=True, exist_ok=True)
    nom_pas, sha_pas = ecrire_pas(dossier, etape, resultats, pas_tous)
    resultat = {
        "etape": etape, "version": VERSION, "regle": REGLE, "run_source": config["run_source"],
        "taille_lot": taille, "lots": len(lots),
        "episodes_etape": len(episodes), "empreintes_retrouvees": trouvees,
        "directes": sum(x["voie"] == "directe" for x in resultats),
        "par_repli": sum(x["voie"] == "repli" for x in resultats),
        "non_resolus": [{"episode": x["episode"], "cause": x["cause"]} for x in resultats if x["statut"] != "resolu"],
        "lignes_approchees": {x["episode"]: x["lignes_approchees"] for x in resultats if x["lignes_approchees"]},
        "identifiants_egaux_episodes": egaux_ep, "actions_egales": actions_egales, "actions_comparees": actions_tot,
        "accord_non_contraint": {"pas": n_pas, "par_episode_min": min(accords) if accords else None,
                                 "moyenne_par_episode": float(np.mean(accords)) if accords else None,
                                 "pas_en_desaccord": len(marges_desaccord)},
        "ecarts_contraints": rg.quantiles(ecarts), "marges_en_desaccord": rg.quantiles(marges_desaccord),
        "erreurs_directes": erreurs_directes,
        "fffd_declares": {x["episode"]: x["fffd"] for x in resultats if x["fffd"]},
        "passes": moteur.passes, "jetons_en_passe": moteur.jetons, "seuils": {
            k: config[k] for k in ("seuil_ecart", "quasi_egalites_max", "bascules_max", "combinaisons_max_lot",
                                   "balayages_max", "seuil_validation_lot")},
        "equivalence_tirage": etat["equivalence_tirage"], "reglages": reglages_det, "modele": config["agent"],
        "noyau_attention": config["noyau_attention"], "non_resolus_v1": non_resolus_v1,
        "pas_fichier": nom_pas, "pas_sha256": sha_pas, "episodes": detail,
        "duree_s": round(time.perf_counter() - debut, 1)}
    if etape == "validation-lot":
        resultat["seuil_validation"] = int(config["seuil_validation_lot"])
        resultat["lecture"] = "atteint" if trouvees >= int(config["seuil_validation_lot"]) else "sous le seuil"
    else:
        resultat["lecture"] = "complète" if trouvees == len(episodes) else ("partielle" if trouvees else "aucune")
    ecrire_resultat(racine, chemin_m, f"resolution-graine-{etape}", resultat)
    progres(etape="fin", resolus=f"{trouvees}/{len(episodes)}", lecture=resultat["lecture"].replace(" ", "_"))
    if etape == "validation-lot":
        rg.exiger_seuil_validation(trouvees, int(config["seuil_validation_lot"]), len(episodes))
    return resultat


def executer(config: dict, racine: Path, run_id: str, prereg: str | None, etape: str, validation: str | None = None,
             resolution: str | None = None, autoriser_depot_sale: bool = False,
             entropie_essai: int | None = None) -> dict:
    racine = Path(racine)
    exiger_config(config)
    if etape not in ETAPES:
        raise GardeArret(f"étape {etape!r} : {ETAPES} attendues")
    if config["mode"] == "reel" and prereg is None:
        raise GardeArret("résolution réelle sans préenregistrement : R1 interdit de lancer")
    entropie = entropie_essai
    if prereg is not None:
        from ..harnais.validation_reelle import ENTROPIE_CITEE, exiger_code_cite

        texte = Path(prereg).read_text(encoding="utf-8")
        if CONFIG_CITEE.format(rg.empreinte_config(config)) not in texte:
            raise GardeArret(f"{prereg} ne cite pas la configuration du lot fidèle {rg.empreinte_config(config)[:12]}")
        e = ENTROPIE_CITEE.search(texte)
        if not e:
            raise GardeArret(f"{prereg} ne cite pas l'entropie")
        entropie = int(e.group(1))
        exiger_code_cite(racine, Path(prereg))
    pieces = rg.charger_pieces(config, racine)
    exiger_meme_lot_que_p3(config, pieces.manifeste_p3)
    non_resolus_v1, resolus_v1 = None, None
    if etape == "resolution-lot":
        exiger_validation_lot(racine, validation, config)
        non_resolus_v1, resolus_v1 = exiger_resolution_v1(racine, resolution, config)
    chemin_m, _ = creer_manifeste(racine, run_id, config, ["aucun-tirage-propre"], entropie=entropie,
                                  decisif=prereg is not None, prereg=prereg, autoriser_depot_sale=autoriser_depot_sale,
                                  commande=f"{COMMANDE} --etape {etape}")
    etat = {"etape": "chargement"}
    debut = time.perf_counter()
    try:
        return _executer(config, racine, run_id, chemin_m, pieces, etape, etat, debut, non_resolus_v1, resolus_v1)
    except Exception as e:
        ecrire_resultat(racine, chemin_m, "arret", {"etape": etat["etape"], "motif": motif_d_arret(e),
                                                     "partiel": {k: v for k, v in etat.items() if k != "etape"},
                                                     "duree_s": round(time.perf_counter() - debut, 1)})
        relever_term_apres(e)
        raise


def _main(argv: list[str]) -> int:
    from ..scellement import verifier

    ap = argparse.ArgumentParser(prog=COMMANDE)
    ap.add_argument("--etape", required=True, choices=ETAPES)
    ap.add_argument("--config", required=True)
    ap.add_argument("--run-id", required=True)
    ap.add_argument("--prereg", default=None)
    ap.add_argument("--validation", default=None, help="résultat scellé de l'étape validation-lot (étape resolution-lot)")
    ap.add_argument("--resolution", default=None,
                    help="résultat scellé de l'étape resolution de la v1 (étape resolution-lot) : ses non résolus")
    a = ap.parse_args(argv)
    signal.signal(signal.SIGTERM, lever_sur_term)
    verifier(a.config)
    config = json.loads(Path(a.config).read_text(encoding="utf-8"))
    r = executer(config, Path("."), a.run_id, a.prereg, a.etape, a.validation, a.resolution)
    print(json.dumps({"etape": r["etape"], "lecture": r["lecture"], "empreintes_retrouvees": r["empreintes_retrouvees"],
                      "episodes": r["episodes_etape"]}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    try:
        sys.exit(_main(sys.argv[1:]))
    except GardeArret as e:
        print(f"ARRÊT : {e}", file=sys.stderr)
        sys.exit(1)
