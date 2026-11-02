"""Rejeu à graine, repli « lot fidèle » (étape 1 bis de l'addendum v2) : refaire la génération de P3 elle-même, dans son
lot, pour un épisode cible que la résolution du cœur (`resolution_graine_v1`, étape « resolution ») laisse non résolu.
Version 1, nom nouveau (R12) ; `resolution_graine_v1` n'est pas modifié, il est importé par ses fonctions publiques
(candidats, tirages exponentiels, repli : `quasi_egalites`, budgets : `echeance_episode`, `horloge`, `DureeEpuisee`,
consignation : `consigner_episode`, `non_tente`, empreinte, pièces de P3, table v3 : `construire_table_v3`,
`entree_identifiants`, `verifier_entrees_v3`, `ecrire_table_v3`).

**Pourquoi.** P3 (`premier_test_ia.run.jouer_p3` → `harnais.episode.jouer_episodes` → `generer_lot`) générait par lots de
`lot` épisodes (8 en réel : deux tâches × quatre conditions, plan `plan_p3`, lots consécutifs), remplis à gauche, avec une
passe de préremplissage puis une passe par jeton avec cache (`logits_to_keep=1`), positions explicites, modèle en bfloat16
sur la carte ; logits du dernier jeton ramenés sur processeur en float32, softmax, tirage multinomial à graine. Le cœur
fait une passe forcée pleine, sans lot ni cache : ses logits diffèrent aux arrondis près et, sur une quasi-égalité, le
vainqueur de la course exponentielle peut changer.

**Cibles** (décision écrite, texte et code alignés) : les épisodes que la résolution du cœur laisse non résolus **et**
dont l'entrée de la table v2 est « non_resolu » (au plus les 4 de la table v2) ; un épisode de C-6 (entrée corrigée de la
table v2, déjà prouvée par l'empreinte) non résolu par le cœur n'est **pas** une cible : il est cité dans
`hors_cibles` avec sa cause (aucun repli silencieux) ; demandé nommément au lot, il est refusé.

**Méthode** (`generer_lot_fidele`, `rejouer_episode_lot`, `resoudre_episode_lot`). Même lot que P3 (les autres lignes
reconstruites depuis leurs textes : identifiants exacts quand l'épisode est connu — base identique, table v2 revérifiée
par l'empreinte, résolu par le cœur ou plus tôt par cette étape, revérifiés par l'empreinte — sinon **approchées**,
déclarées ligne par ligne), même remplissage à gauche, même ordre d'appels, mêmes positions, mêmes conversions ; à chaque
pas de la ligne cible, le jeton retenu est le candidat compatible avec les octets restants du texte stocké qui maximise
p / q (`softmax(logits / température)` en float32 sur processeur, divisé par les tirages exponentiels de la graine :
l'opération même de P3, `argmax(p / q) = multinomial`, vérifiée au lancement). Les autres lignes reçoivent leurs jetons
connus et s'arrêtent au pas que donnent `jetons` ; les passes s'arrêtent dès que la ligne cible est finie (les passes
suivantes ne touchent pas à ses logits). Arbitre unique : l'empreinte de trajectoire de P3.

**Lignes approchées (B-L1)** : découpage canonique du texte, **tronqué ou complété** (jeton de remplissage) au nombre de
jetons notés par P3, **puis la fin par défaut à la dernière place** quand P3 a compté une fin (`LigneLot.forcee`) : le
nombre de jetons de chaque action est exact et la clôture du gabarit redevient celle de P3 (`c[1:]`), sauf si la vraie
fin de P3 n'était pas la fin par défaut (un jeton de plus chez P3 par telle action ; non connu pour une ligne
approchée). Les logits de la cible ne dépendent des autres lignes que par la forme du lot (taille, longueur remplie L) ;
**mesuré et rapporté** par action jouée : `pas_L_fixee_par_approchee` (une ligne approchée est strictement la plus longue :
L vient d'elle) et `pas_L_a_un_jeton_d_une_approchee` (une ligne approchée à un jeton ou moins de fixer L, ce qui couvre
la fin non par défaut) ; `forme_exacte_prouvee` = (premier compte nul).

**Repli écrit, itératif** (règle du cœur au commit 755959e1, recopiée : le cœur n'expose pas de fonction de repli
générique, seulement `quasi_egalites`) : bascule des quasi-égalités de l'essai direct, puis frontière enrichie par les
quasi-égalités de chaque rejeu basculé après sa dernière bascule, une puis deux, combinaisons de plus faible écart cumulé
d'abord, au plus `combinaisons_max_lot` rejeux, chacun rejoué depuis l'action de sa première bascule.

**Durées** : budget par épisode (`duree_max_episode_lot_s`) et par étape (`duree_max_lot_s`) ; un épisode dont le budget
s'épuise finit « non résolu : durée » sans arrêter l'étape ; ensuite « non tenté : durée » ; le résultat est toujours
écrit ; chaque épisode est consigné aussitôt dans un fichier scellé (`episodes-resolution-lot/NNN.json`), cité par
`arret.json` en cas d'arrêt.

**Validation du lot : une mesure, sans passe de plus ni seuil d'arrêt** (B-L2). Pendant les mêmes passes, chaque ligne
voisine **exacte** est mesurée à chaque pas joué avec les tirages exponentiels du générateur de **sa** propre action (une
graine par action, dérivée comme pour la cible, avancée d'un vecteur par jeton comme P3) : choix non contraint
(argmax p / q) contre son jeton connu (accord ; 1 exactement si les logits sont ceux de P3), probabilité du jeton connu
(accord attendu sous une graine indépendante), pas informatifs (jeton connu ≠ argmax des logits), choix contraint par le
texte contre le jeton connu (égalité). Lecture du lot (`lecture_lot`, jamais un arrêt) : « fidèle » si l'accord et
l'égalité des choix contraints atteignent `seuil_lecture_lot` et qu'aucun jeton connu n'est hors des candidats ;
« réserve lot non fidèle » sinon ; « sans mesure » si aucune ligne exacte n'a été mesurée. Les mesures retenues sont
celles de l'essai qui a produit chaque action de la cible (essai direct avant la première bascule, rejeu basculé
ensuite). Le choix contraint d'une ligne voisine n'est pas mesuré dans une action dont le texte contient U+FFFD
(compté `non_mesures_fffd`) : le balayage du vocabulaire y serait hors budget.

**Classe de la validation (I-B)** : lue dans le résultat scellé de la validation du cœur, clé `classe_validation` (la
lecture à trois classes du cœur, `lire_validation`) ; absente, l'étape refuse de partir (déclaré) ; recopiée, avec la
lecture du lot, dans le résultat du lot, dans chaque épisode et dans la table v3 (`lecture_validation`).

**R3** : une seule exécution de l'étape « resolution-lot » par configuration (`exiger_execution_unique` : tout manifeste
de `runs/` de même commande et de même empreinte de configuration arrête avant tout calcul).

**Table v3 (étape « table-lot », processeur)** : `construire_table_v3_lot` part du résultat scellé de la résolution du
cœur (table v3 du cœur, `construire_table_v3`), y verse les épisodes résolus par le lot, chacun revérifié par l'empreinte
de P3 avant écriture, refuse deux résultats différents pour un même épisode, exige le contrôle croisé du cœur
« conforme », revérifie toutes les entrées (`verifier_entrees_v3`) et écrit la table par `ecrire_table_v3` (scellée,
jamais écrasée).

**Non reproduit à l'identique, déclaré** : le type (bfloat16 sur A100 en réel : même carte et mêmes réglages exigés,
jamais garantis au bit près entre deux exécutions ; mesuré par l'accord des lignes voisines), les jetons des lignes
approchées (valeurs sans effet sur la cible ; forme mesurée), les passes après la fin de la ligne cible.

Interdits respectés par construction (comme le cœur) : aucun score, aucune note, aucune activation ; consignes lues par
`charger_consignes` seulement.

    PYTHONPATH=src python -m controle_ia.runs_nuit.resolution_graine_lot_v1 --etape resolution-lot --config CONFIG \\
        --run-id AAAAMMJJ-HHMMSS-r1-graine-lot-resolution --prereg prereg/R1-addendum-relance-v2.md \\
        --validation diag/<run de validation du cœur>/resolution-graine-validation.json \\
        --resolution diag/<run de résolution du cœur>/resolution-graine-resolution.json
    PYTHONPATH=src python -m controle_ia.runs_nuit.resolution_graine_lot_v1 --etape table-lot --config CONFIG \\
        --tokeniseur DOSSIER --resolution diag/<run de résolution du cœur>/resolution-graine-resolution.json \\
        --resultat-lot diag/<run du lot>/resolution-graine-resolution-lot.json \\
        --sortie prereg/R1-table-tokenisation-v3.json          (processeur seulement)
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import signal
import sys
from dataclasses import dataclass, replace
from pathlib import Path

import numpy as np
import torch

from ..gardes import GardeArret, exiger_sans_signal, lever_sur_term, motif_d_arret, relever_term_apres
from ..manifeste import creer_manifeste, ecrire_resultat, lire_manifeste, verifier_resultat
from ..scellement import sceller, verifier
from . import resolution_graine_v1 as rg
from .rejeu_activations_v1 import episode_harnais, empreinte_trajectoire
from .resolution_graine_v1 import Cible, Compteurs, Contradiction, DureeEpuisee, NonResolu, Reglages, Vocabulaire

VERSION = "resolution_graine_lot_v1"
COMMANDE = "python -m controle_ia.runs_nuit.resolution_graine_lot_v1"
CONFIG_CITEE = "Configuration de la résolution à graine, lot fidèle (empreinte canonique) : `{}`"
ETAPE_LOT = "resolution-lot"
ETAPE_TABLE = "table-lot"
ETAPES = (ETAPE_LOT,)
CLES_LOT = ("episodes_resolution_lot", "combinaisons_max_lot", "duree_max_episode_lot_s", "duree_max_lot_s",
            "seuil_lecture_lot")
CLES_COEUR = rg.CLES_COMPLETES
CLES = CLES_COEUR + CLES_LOT
CLE_CLASSE = "classe_validation"
SOURCE_CIBLE = "cible"
SOURCE_APPROCHEE = "canonique_approche"
LECTURE_FIDELE, LECTURE_RESERVE, LECTURE_SANS = "fidèle", "réserve lot non fidèle", "sans mesure"
CAUSE_BALAYAGES = "caractère de remplacement : budget de balayages dépassé"
REGLE = ("rejeu à graine, lot fidèle : la génération de P3 refaite dans son lot (plan_p3, lots consécutifs de `lot` "
         "épisodes), même remplissage à gauche, préremplissage puis une passe par jeton avec cache, logits du dernier "
         "jeton en float32 sur processeur ; ligne cible : à chaque pas, parmi les jetons compatibles avec les octets "
         "restants du texte stocké (dernier pas : jeton de fin si jetons − jetons_notes = 1), celui qui maximise "
         "softmax(logits / température) / q, q = tirages exponentiels de la graine ; autres lignes forcées à leurs jetons "
         "connus (exacts si connus, sinon découpage canonique tronqué ou complété au nombre de jetons notés puis la fin "
         "par défaut, déclaré ; pas où une ligne approchée fixe la longueur remplie comptés) ; lignes exactes mesurées "
         "pendant les mêmes passes avec les tirages de leur propre graine (accord, accord attendu, pas informatifs, "
         "égalité des choix contraints ; lecture sans arrêt) ; arbitre unique : empreinte de trajectoire de P3 ; repli "
         "itératif : bascule des quasi-égalités de l'essai direct puis de chaque rejeu basculé après sa dernière bascule, "
         "une puis deux, combinaisons bornées ; budgets par épisode et par étape (non résolu : durée) ; sinon non résolu, "
         "cause écrite")


# --------------------------------------------------------------------------------------------------------------------
# Choix contraint sur les logits du lot (ligne cible) et mesure des lignes voisines exactes


class ChoixCible:
    """Ligne cible d'un lot : à chaque pas, sur les logits (V,) float32 du pas (ceux de P3), choisit le candidat compatible
    avec le texte stocké qui maximise p / q, p = softmax(logits / température) en float32, q = tirages exponentiels du pas
    (l'opération de P3, à l'identique ; égalité exacte : plus petit identifiant, comme argmax). Journal `pas` : (t, s,
    choix, non contraint, candidats, écart, second, marge, balayage complet, p du jeton retenu, argmax des logits) — les
    neuf premiers champs au format du cœur. Lève `DureeEpuisee` à l'échéance de `reglages`."""

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
        if self.reglages.echeance is not None and rg.horloge() > self.reglages.echeance:
            raise DureeEpuisee(f"budget épuisé (pas {self.t}, jeton {s})")
        if tuple(logits.shape) != (self.voc.V,) or logits.dtype != torch.float32 or logits.device.type != "cpu":
            raise GardeArret(f"logits {tuple(logits.shape)} {logits.dtype} sur {logits.device} : (V,) float32 sur "
                             "processeur attendus, comme P3")
        with torch.no_grad():
            p = torch.softmax(logits / self.reglages.temperature, dim=-1)        # P3, à l'identique
            R = p / self.Q[s]
            non_contraint = int(torch.argmax(R))                                # = le tirage de P3 sur ces logits
            top = torch.topk(R, 2).values.double()
            marge = float(torch.log(top[0]) - torch.log(top[1])) if float(top[1]) > 0 else math.inf
            argmax_logits = int(torch.argmax(logits))
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
                    raise NonResolu(f"{CAUSE_BALAYAGES} ({self.compteurs.balayages} balayages complets du vocabulaire "
                                    f"> {self.reglages.balayages_max})")
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
            self.pas.append((self.t, s, choix, non_contraint, len(ordre), ecart, second, marge, balayage,
                             float(p[choix]), argmax_logits))
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


class MesureLigne:
    """Ligne voisine exacte d'une action : à chaque pas joué, avec les tirages du générateur de **son** action (graine de
    P3, un vecteur de V par jeton, dans l'ordre, comme `generer_lot`), choix non contraint (argmax de p / q, p en float32
    sur processeur comme P3) contre le jeton connu ; probabilité du jeton connu ; argmax des logits ; choix contraint par
    le texte stocké (non mesuré si le texte de l'action contient U+FFFD : compté). Ne change rien au lot : le jeton
    fourni est toujours le jeton connu. Enregistrement par pas : (s, connu, non contraint, p du connu, argmax des
    logits, contraint ou −1)."""

    def __init__(self, voc: Vocabulaire, texte: str, n: int, a_fin: int, graine: int, temperature: float):
        self.voc, self.n, self.a_fin, self.temperature = voc, int(n), int(a_fin), float(temperature)
        self.g = torch.Generator(device="cpu").manual_seed(int(graine))
        self.cible = None if rg.FFFD in texte else Cible(texte, voc)
        self.etat = Cible.initial()
        self.suivi = self.cible is not None
        self.pas: list[tuple] = []
        self.hors_candidats = 0
        self.non_mesures_fffd = 0

    def mesurer(self, s: int, logits: torch.Tensor, connu: int) -> None:
        if s != len(self.pas) or s >= self.n:
            raise GardeArret(f"mesure d'une ligne voisine : pas {s} demandé, {len(self.pas)} mesurés sur {self.n}")
        with torch.no_grad():
            q = torch.empty(self.voc.V, dtype=torch.float32).exponential_(1, generator=self.g)
            p = torch.softmax(logits / self.temperature, dim=-1)                 # P3, à l'identique
            R = p / q
            nc = int(torch.argmax(R))
            pk = float(p[int(connu)])
            am = int(torch.argmax(logits))
        contraint = -1
        if self.cible is None:
            self.non_mesures_fffd += 1
        elif self.suivi:
            dernier = bool(self.a_fin and s == self.n - 1)
            if dernier:
                cands = list(self.voc.fins)
            else:
                cands = self.cible.candidats(self.etat)[0] + self.voc.speciaux_non_fins
            if cands:
                ordre = sorted(cands)
                contraint = ordre[int(torch.argmax(R[torch.tensor(ordre, dtype=torch.long)]))]
            if int(connu) not in set(cands):
                self.hors_candidats += 1
                self.suivi = False
            elif not dernier:
                e2 = self.cible.avancer(self.etat, int(connu))
                if e2 is None:
                    self.hors_candidats += 1
                    self.suivi = False
                else:
                    self.etat = e2
        self.pas.append((s, int(connu), nc, pk, am, contraint))


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
                       t: int = 0, mesures: dict | None = None) -> tuple[list[list[int]], dict]:
    """`generer_lot` refait appel pour appel (remplissage à gauche, masque, positions explicites, préremplissage puis une
    passe par jeton avec cache, `logits_to_keep=1`, logits du dernier jeton en float32 sur processeur), sauf le tirage :
    la ligne `cible` choisit par `choix.choisir` (contrainte par le texte, p / q), les autres reçoivent `forces[r]`
    (jetons connus ; `pad_id` au-delà, compté) et s'arrêtent à leur premier jeton de `fins` ou à `longueurs[r]` jetons ;
    `mesures` ({ligne : MesureLigne}) : lignes voisines exactes mesurées à chaque pas joué (sans effet sur le lot).
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
    mesures = mesures or {}
    if cible is not None and cible in mesures:
        raise GardeArret("la ligne cible n'est pas une ligne voisine mesurée")
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
                    if r in mesures:
                        mesures[r].mesurer(pas, logits[r], j)
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
    par action (None pour la cible), la source de ces identifiants, si elle est exacte, et les graines de ses actions
    (graines de P3 ; None : ligne non mesurée)."""
    episode: str
    fabrique_env: object
    textes: list
    jetons: list
    jetons_notes: list
    ids: list | None
    source: str
    exacte: bool
    graines: list | None = None

    def forcee(self, t: int, pad_id: int, fin_defaut: int, fins) -> list[int]:
        """Jetons forcés de l'action t. Ligne exacte : ses identifiants (longueur = `jetons[t]`, garde). Ligne approchée
        (B-L1) : identifiants connus sans leur jeton de fin final, tronqués ou complétés par `pad_id` à `jetons_notes[t]`,
        puis la fin par défaut si P3 a compté une fin : nombre de jetons exact, clôture du gabarit comme chez P3."""
        n, jn = int(self.jetons[t]), int(self.jetons_notes[t])
        ids = [int(x) for x in self.ids[t]]
        if self.exacte:
            if len(ids) != n:
                raise GardeArret(f"{self.episode}, pas {t} : ligne exacte de {len(ids)} jetons ≠ {n} notés par P3")
            return ids
        a_fin = n - jn
        if a_fin not in (0, 1):
            raise GardeArret(f"{self.episode}, pas {t} : jetons − jetons notés = {a_fin}")
        notes = ids[:-1] if ids and ids[-1] in fins else ids
        notes = notes[:jn] + [int(pad_id)] * (jn - min(len(notes), jn))
        forcee = notes + ([int(fin_defaut)] if a_fin else [])
        if not a_fin and forcee and forcee[-1] == int(fin_defaut):
            raise GardeArret(f"{self.episode}, pas {t} : ligne approchée sans fin finissant par la fin par défaut "
                             "(clôture d'un jeton plus courte que chez P3)")
        return forcee


def pad_du_format(fmt) -> int:
    """Jeton de remplissage de P3 (`jouer_episodes`, `pad_id=None`)."""
    return fmt.tok.pad_token_id if fmt.tok.pad_token_id is not None else min(fmt.fins)


def fin_par_defaut(fmt, debut) -> int:
    """Fin par défaut d'une action : premier jeton de clôture du gabarit (comme `reconstruire_episode`)."""
    return int(fmt._pieces(debut)["cloture"][0]) if fmt.nom == "chat" else int(min(fmt.fins))


def forme_du_pas(longueurs: list[int], approchees: list[bool]) -> dict:
    """Longueur remplie d'une action et rôle des lignes approchées : `fixee` si L vient strictement d'une ligne approchée,
    `a_un_jeton` si une ligne approchée est à un jeton ou moins de la fixer."""
    exactes = [x for x, a in zip(longueurs, approchees) if not a]
    approx = [x for x, a in zip(longueurs, approchees) if a]
    if not approx:
        return {"L_fixee_par_approchee": False, "L_a_un_jeton_d_une_approchee": False}
    m_e = max(exactes) if exactes else -1
    m_a = max(approx)
    return {"L_fixee_par_approchee": m_a > m_e, "L_a_un_jeton_d_une_approchee": m_a + 1 > m_e}


def rejouer_episode_lot(moteur: MoteurLot, voc: Vocabulaire, fmt, lignes: list[LigneLot], cible: int | None, T: int,
                        Qs, reglages: Reglages, forcages=None, prefixe=None, pas=None, compteurs=None,
                        arreter_apres_cible: bool = True, plans: list | None = None,
                        mesurer: bool = True) -> tuple[dict | None, list, list[dict]]:
    """Un essai : les T pas du lot rejoués comme `jouer_episodes` (N = 1), contextes de chaque ligne construits sur ses
    identifiants (forcés, ou retrouvés pour la cible) ; `prefixe` : actions déjà retrouvées de la cible, reprises sans
    génération. `cible=None` : toutes les lignes forcées (contrôle des logits). `plans` : liste remplie action par action
    (gardée par l'appelant si l'essai s'arrête). `mesurer` : lignes voisines exactes munies de graines mesurées. Rend
    (reconstruction de la cible, identifiants par action de la cible, plans par pas). Lève `Contradiction`, `NonResolu`
    ou `DureeEpuisee`."""
    B = len(lignes)
    if cible is not None and not 0 <= cible < B:
        raise GardeArret(f"ligne cible {cible} hors du lot de {B}")
    for b, x in enumerate(lignes):
        if b != cible and x.ids is None:
            raise GardeArret(f"ligne {b} ({x.episode}) sans identifiants connus")
    envs = [x.fabrique_env() for x in lignes]
    pad = pad_du_format(fmt)
    fins = {int(x) for x in fmt.fins}
    trs: list[list[int]] = [[] for _ in range(B)]
    debuts: list = [None] * B
    fins_defaut: list = [None] * B
    journaux: list[list[tuple[int, int, str]]] = [[] for _ in range(B)]
    trouves: list[list[int]] = []
    plans = plans if plans is not None else []
    approchees = [b != cible and not x.exacte for b, x in enumerate(lignes)]
    compteurs = compteurs if compteurs is not None else Compteurs()
    for t in range(T):
        exiger_sans_signal(f"lot fidèle, pas {t}")
        contextes = []
        for b in range(B):
            obs = envs[b].observation(0, t, journaux[b])
            if t == 0:
                debuts[b] = (envs[b].consigne_privee(0), obs)
                fins_defaut[b] = fin_par_defaut(fmt, debuts[b])
                contextes.append(fmt.ouverture(*debuts[b]))
            else:
                contextes.append(trs[b] + fmt.tour(debuts[b], obs))
        nvs = [None if b == cible else lignes[b].forcee(t, pad, fins_defaut[b], fins) for b in range(B)]
        plan = None
        mes: dict[int, MesureLigne] = {}
        genere = not (cible is not None and prefixe is not None and t < len(prefixe))
        if mesurer and genere:
            for b, x in enumerate(lignes):
                if b != cible and x.exacte and x.graines is not None:
                    mes[b] = MesureLigne(voc, x.textes[t], int(x.jetons[t]), int(x.jetons[t]) - int(x.jetons_notes[t]),
                                         int(x.graines[t]), reglages.temperature)
        longueurs = [int(x.jetons[t]) for x in lignes]
        if not genere:
            nv = [int(x) for x in prefixe[t]]
        elif cible is not None:
            lc = lignes[cible]
            n, a_fin = int(lc.jetons[t]), int(lc.jetons[t]) - int(lc.jetons_notes[t])
            choix = ChoixCible(voc, lc.textes[t], n, a_fin, Qs[t], reglages, t, forcages, pas, compteurs)
            nouveaux, plan = generer_lot_fidele(moteur, contextes, reglages.max_nouveaux, reglages.temperature, fins,
                                                pad, nvs, longueurs, cible, choix, arreter_apres_cible, t, mes)
            compteurs.passes += 1
            nv = choix.terminer()
            if nouveaux[cible] != nv:
                raise GardeArret(f"pas {t} : jetons du lot ≠ jetons choisis")
            if fmt.tok.decode(nv, skip_special_tokens=True) != lc.textes[t]:
                raise Contradiction(t, len(nv), "texte décodé ≠ texte stocké")
            if any(x in fins for x in nv[:len(nv) - 1]) or bool(nv and nv[-1] in fins) != bool(a_fin):
                raise Contradiction(t, len(nv), "jeton de fin mal placé")
        else:
            nouveaux, plan = generer_lot_fidele(moteur, contextes, reglages.max_nouveaux, reglages.temperature, fins,
                                                pad, nvs, longueurs, None, None, False, t, mes)
            compteurs.passes += 1
            nv = None
        if cible is not None:
            nvs[cible] = nv
            trouves.append(nv)
        lc_ = [len(c) for c in contextes]
        plans.append({"pas": t, "longueur_remplie": None if plan is None else plan["longueur_remplie"],
                      "passes_decodage": None if plan is None else plan["passes_decodage"],
                      "remplissage_cible": None if plan is None or cible is None else plan["remplissage"][cible],
                      "jetons_manquants": None if plan is None else plan["jetons_manquants"],
                      "empreinte_logits_cible": None if plan is None or cible is None else plan["empreintes_logits"][cible],
                      "empreintes_logits": None if plan is None else plan["empreintes_logits"],
                      "longueurs_contextes": lc_, **forme_du_pas(lc_, approchees),
                      "mesure_voisines": [{"rang": b, "episode": lignes[b].episode, "pas": m.pas,
                                           "hors_candidats": m.hors_candidats, "non_mesures_fffd": m.non_mesures_fffd}
                                          for b, m in sorted(mes.items())] if plan is not None else []})
        for b in range(B):
            trs[b] = contextes[b] + nvs[b] + fmt.cloture(debuts[b], nvs[b])
            journaux[b].append((0, t, lignes[b].textes[t]))
    if cible is None:
        return None, [], plans
    lc = lignes[cible]
    rec = rg.transcription(fmt, envs[cible], T, lc.textes, trouves, lc.jetons, lc.jetons_notes)
    return rec, trouves, plans


# --------------------------------------------------------------------------------------------------------------------
# Mesures


def _moyenne(x) -> float | None:
    return float(np.mean(x)) if len(x) else None


def mesure_des_voisines(plans: list[dict], seuil: float) -> dict:
    """Validation du lot (B-L2), sur les pas joués des lignes voisines exactes : accord du choix non contraint avec le
    jeton connu, accord attendu sous une graine indépendante (moyenne de p du jeton connu), pas informatifs (jeton connu
    ≠ argmax des logits) et leur accord, égalité des choix contraints, jetons connus hors des candidats, pas non mesurés
    (U+FFFD) ; poolés et par ligne ; lecture (jamais un arrêt)."""
    par_ligne: dict[str, list] = {}
    hors = fffd = 0
    for p in plans:
        for m in p.get("mesure_voisines") or []:
            par_ligne.setdefault(m["episode"], []).extend(m["pas"])
            hors += int(m["hors_candidats"])
            fffd += int(m["non_mesures_fffd"])

    def resume(recs):
        inf = [x for x in recs if x[1] != x[4]]
        con = [x for x in recs if x[5] >= 0]
        return {"pas": len(recs), "accord": _moyenne([x[2] == x[1] for x in recs]),
                "accord_attendu_graine_independante": _moyenne([x[3] for x in recs]),
                "pas_informatifs": len(inf), "accord_informatifs": _moyenne([x[2] == x[1] for x in inf]),
                "contraints_mesures": len(con), "egalite_contraints": _moyenne([x[5] == x[1] for x in con])}

    tous = [x for v in par_ligne.values() for x in v]
    sortie = {**resume(tous), "hors_candidats": hors, "non_mesures_fffd": fffd,
              "par_ligne": {e: resume(v) for e, v in sorted(par_ligne.items())}, "seuil_lecture": float(seuil)}
    sortie["lecture"] = lecture_du_lot(sortie, seuil)
    return sortie


def lecture_du_lot(m: dict, seuil: float) -> str:
    """« fidèle » : accord ≥ seuil, égalité des choix contraints ≥ seuil (quand mesurés), aucun jeton connu hors des
    candidats ; « sans mesure » : aucun pas mesuré ; « réserve lot non fidèle » sinon."""
    if not m["pas"]:
        return LECTURE_SANS
    ok = m["accord"] >= seuil and (m["egalite_contraints"] is None or m["egalite_contraints"] >= seuil) \
        and m["hors_candidats"] == 0
    return LECTURE_FIDELE if ok else LECTURE_RESERVE


def forme_des_plans(plans: list[dict]) -> dict:
    """B-L1 : sur les actions jouées, pas où la longueur remplie vient d'une ligne approchée, et où une ligne approchée
    est à un jeton ou moins de la fixer ; `forme_exacte_prouvee` = premier compte nul."""
    joues = [p for p in plans if p.get("passes_decodage") is not None]
    f = sum(1 for p in joues if p["L_fixee_par_approchee"])
    u = sum(1 for p in joues if p["L_a_un_jeton_d_une_approchee"])
    return {"actions_jouees": len(joues), "pas_L_fixee_par_approchee": f, "pas_L_a_un_jeton_d_une_approchee": u,
            "forme_exacte_prouvee": f == 0}


def accords_cible(pas: list) -> dict:
    """Ligne cible (C-5, I-D), résolue ou non : accord du choix non contraint avec le jeton retenu, accord attendu sous
    une graine indépendante (moyenne de p du jeton retenu), pas informatifs (retenu ≠ argmax des logits) et leur
    accord."""
    inf = [x for x in pas if x[2] != x[10]]
    return {"pas": len(pas), "accord": _moyenne([x[3] == x[2] for x in pas]),
            "accord_attendu_graine_independante": _moyenne([x[9] for x in pas]),
            "pas_informatifs": len(inf), "accord_informatifs": _moyenne([x[3] == x[2] for x in inf])}


# --------------------------------------------------------------------------------------------------------------------
# Résolution d'un épisode cible


def resoudre_episode_lot(moteur: MoteurLot, voc: Vocabulaire, fmt, lignes: list[LigneLot], cible: int, T: int, Qs,
                         empreinte_cible: str, reglages: Reglages, combinaisons_max: int | None = None,
                         reference_logits: list | None = None, seuil_lecture: float = 0.99) -> dict:
    """Essai direct dans le lot fidèle, puis repli écrit itératif (règle du cœur) ; arbitre : `empreinte_cible`. Budget
    de l'épisode (`rg.echeance_episode`) : épuisé, l'épisode finit « non résolu », cause « durée : … » (jamais une
    exception : l'étape continue). `reference_logits` (essais) : empreintes des logits de la ligne cible par pas,
    comparées à celles des actions retenues (`logits_conformes`). Déclare le lot (source et exactitude de chaque ligne),
    la forme (B-L1), la mesure des voisines et sa lecture (B-L2), les accords de la cible."""
    depart = rg.horloge()
    lc = lignes[cible]
    if lc.ids is not None or lc.source != SOURCE_CIBLE:
        raise GardeArret(f"ligne cible {cible} : identifiants déjà connus ou source {lc.source!r}")
    cmax = reglages.combinaisons_max if combinaisons_max is None else int(combinaisons_max)
    reg = replace(reglages, echeance=rg.echeance_episode(reglages, depart))
    sortie = {"episode": lc.episode, "fffd": sum(x.count(rg.FFFD) for x in lc.textes), "statut": "non_resolu",
              "voie": None, "cause": None, "forcages": [], "combinaisons_essayees": 0, "ids": None, "ids_directs": None,
              "empreinte": None, "empreinte_cible": empreinte_cible, "duree_epuisee": False, "rang_dans_le_lot": cible,
              "lot": [{"episode": x.episode, "source": x.source, "exacte": bool(x.exacte)} for x in lignes],
              "lignes_approchees": sum(1 for b, x in enumerate(lignes) if b != cible and not x.exacte),
              "plans": None, "empreintes_logits": None, "logits_conformes": None}
    pas: list = []
    compteurs = Compteurs()
    plans_d: list = []

    def essai(forcages, prefixe, journal_pas, cpt, plans):
        rec, trouves, _ = rejouer_episode_lot(moteur, voc, fmt, lignes, cible, T, Qs, reg, forcages, prefixe,
                                              journal_pas, cpt, plans=plans)
        return rec, trouves, empreinte_trajectoire(episode_harnais(lc.episode, T, rec))

    def finir(plans, **k):
        sortie.update(k)
        sortie["plans"] = [{c: v for c, v in p.items() if c not in ("empreintes_logits", "mesure_voisines")}
                           for p in plans]
        sortie["empreintes_logits"] = [p["empreinte_logits_cible"] for p in plans]
        if reference_logits is not None:
            sortie["logits_conformes"] = len(reference_logits) == len(plans) and all(
                e is not None and e == r for e, r in zip(sortie["empreintes_logits"], reference_logits))
        sortie["forme"] = forme_des_plans(plans)
        sortie["mesure_voisines"] = mesure_des_voisines(plans, seuil_lecture)
        sortie["lecture_lot"] = sortie["mesure_voisines"]["lecture"]
        sortie["accord_cible"] = accords_cible(sortie.get("pas") or [])
        sortie["duree_s"] = round(rg.horloge() - depart, 2)
        return sortie

    try:
        rec, trouves, emp = essai(None, None, pas, compteurs, plans_d)
        sortie.update(empreinte=emp, ids_directs=trouves)
        if emp == empreinte_cible:
            sortie.update(statut="resolu", voie="directe", ids=trouves)
        else:
            sortie["cause"] = "empreinte de P3 non retrouvée à l'essai direct"
    except Contradiction as c:
        sortie["cause"] = f"contradiction à l'essai direct ({c})"
    except NonResolu as c:
        return finir(plans_d, cause=str(c), pas=pas, pas_direct=pas, balayages=compteurs.balayages,
                     passes=compteurs.passes)
    except DureeEpuisee as c:
        sortie["duree_epuisee"] = True
        sortie["cause"] = f"durée : {c} à l'essai direct"
    par_action: dict[int, list[int]] = {}
    for (t, s, c, *_r) in pas:
        par_action.setdefault(t, []).append(c)
    if not sortie["ids_directs"]:
        sortie["ids_directs"] = [par_action[t] for t in sorted(par_action)]
    sortie.update(pas=pas, pas_direct=pas, balayages=compteurs.balayages, passes=compteurs.passes)
    if sortie["statut"] == "resolu" or sortie["duree_epuisee"]:
        return finir(plans_d)
    quasi = rg.quasi_egalites(pas, reg.seuil_ecart, reg.quasi_egalites_max)
    sortie["quasi_egalites"] = [{"pas": x[0], "rang": x[1], "choix": x[2], "second": x[6], "ecart": x[5]} for x in quasi]
    essayees = 0
    issues: dict[str, int] = {}
    par_niveau: dict[str, int] = {}
    frontiere = [(x[5], (x,)) for x in quasi]
    for taille in range(1, reg.bascules_max + 1):
        suivante = []
        for cout, combo in sorted(frontiere, key=lambda c: (c[0], [(x[0], x[1]) for x in c[1]])):
            if essayees >= cmax:
                break
            if reg.echeance is not None and rg.horloge() > reg.echeance:
                sortie["duree_epuisee"] = True
                break
            essayees += 1
            par_niveau[str(taille)] = par_niveau.get(str(taille), 0) + 1
            forcages = {(x[0], x[1]): x[6] for x in combo}
            t0 = combo[0][0]
            prefixe = [par_action[t] for t in range(t0)]
            journal_pas: list = [x for x in pas if x[0] < t0]
            plans_r: list = []
            issue = "empreinte_differente"
            try:
                rec, trouves, emp = essai(forcages, prefixe, journal_pas, Compteurs(), plans_r)
            except Contradiction:
                issue = "contradiction"
            except NonResolu:
                issue = "non_resolu"
            except DureeEpuisee:
                sortie["duree_epuisee"] = True
                break
            if issue == "empreinte_differente" and emp == empreinte_cible:
                sortie["repli"] = {"par_niveau": par_niveau, "issues": issues}
                # actions retenues : celles de l'essai direct avant la première bascule, celles du rejeu ensuite
                retenus = plans_d[:t0] + [p for p in plans_r if p["pas"] >= t0]
                return finir(retenus, statut="resolu", voie="repli", ids=trouves, empreinte=emp, cause=None,
                             pas=journal_pas, combinaisons_essayees=essayees,
                             forcages=[{"pas": x[0], "rang": x[1], "jeton": x[6], "ecart": x[5]} for x in combo])
            issues[issue] = issues.get(issue, 0) + 1
            if taille < reg.bascules_max:
                # frontière enrichie : quasi-égalités du rejeu basculé (journal partiel compris), après sa dernière bascule
                for y in rg.quasi_egalites(journal_pas, reg.seuil_ecart, reg.quasi_egalites_max,
                                           (combo[-1][0], combo[-1][1])):
                    suivante.append((cout + y[5], combo + (y,)))
        if sortie["duree_epuisee"] or essayees >= cmax:
            break
        frontiere = suivante
    sortie["repli"] = {"par_niveau": par_niveau, "issues": issues}
    sortie["combinaisons_essayees"] = essayees
    if sortie["duree_epuisee"]:
        return finir(plans_d, cause=f"durée : budget de l'épisode épuisé pendant le repli ({sortie['cause']} ; "
                                    f"{essayees} combinaison(s) essayée(s))")
    return finir(plans_d, cause=f"{sortie['cause']} ; repli itératif : {len(quasi)} quasi-égalité(s) directe(s) sous "
                                f"{reg.seuil_ecart}, {essayees} combinaison(s) essayée(s) ({par_niveau}), aucune ne "
                                f"redonne l'empreinte")


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
    (identifiants, source)}, résolus par le cœur ou plus tôt par cette étape, revérifiés par l'empreinte de P3 ; base
    identique ; table v2 revérifiée par l'empreinte : exacts) ou, à défaut, la reconstruction de base (découpage
    canonique, fin par défaut), forcée par `LigneLot.forcee` : approchée, déclarée. Graines de P3 de chaque ligne."""
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
        sortie.append(LigneLot(e, ep.env, ep.textes, ep.jetons, ep.jetons_notes, ids, source, exacte, list(ep.graines)))
    return sortie


# --------------------------------------------------------------------------------------------------------------------
# Configuration, gardes, étapes


def exiger_config(config: dict) -> None:
    """Configuration du lot : celle du cœur (`rg.exiger_config` et `rg.exiger_reglages_execution` : noyau, paires,
    budgets du cœur), plus les clés du lot : `combinaisons_max_lot` entier ≥ 0, `duree_max_episode_lot_s` > 0 et ≤
    `duree_max_lot_s`, `seuil_lecture_lot` dans [0, 1], `episodes_resolution_lot` liste sans doublon."""
    rg.exiger_config({k: v for k, v in config.items() if k in rg.CLES})
    rg.exiger_reglages_execution(config)
    manquantes = [k for k in CLES_LOT if k not in config]
    if manquantes:
        raise GardeArret(f"configuration du lot fidèle incomplète : {manquantes}")
    c = config["combinaisons_max_lot"]
    if isinstance(c, bool) or not isinstance(c, int) or c < 0:
        raise GardeArret(f"combinaisons_max_lot = {c!r} : entier positif ou nul attendu")
    for k in ("duree_max_episode_lot_s", "duree_max_lot_s", "seuil_lecture_lot"):
        if isinstance(config[k], bool) or not isinstance(config[k], (int, float)):
            raise GardeArret(f"{k} = {config[k]!r} : nombre attendu")
    if not 0 < config["duree_max_episode_lot_s"] <= config["duree_max_lot_s"]:
        raise GardeArret("duree_max_episode_lot_s > 0 et ≤ duree_max_lot_s attendus")
    if not 0 <= config["seuil_lecture_lot"] <= 1:
        raise GardeArret(f"seuil_lecture_lot = {config['seuil_lecture_lot']!r} : dans [0, 1] attendu")
    e = config["episodes_resolution_lot"]
    if not isinstance(e, list) or len(set(e)) != len(e):
        raise GardeArret("episodes_resolution_lot : liste sans doublon attendue")


def exiger_meme_lot_que_p3(config: dict, manifeste_p3: dict) -> int:
    """Le noyau d'attention de la configuration est celui de P3 ; la taille de lot de P3 est lue dans son manifeste."""
    c3 = manifeste_p3["config"]
    if "lot" not in c3:
        raise GardeArret("manifeste de P3 sans taille de lot")
    if c3.get("noyau_attention", "defaut") != config["noyau_attention"]:
        raise GardeArret(f"noyau d'attention {config['noyau_attention']!r} ≠ {c3.get('noyau_attention')!r} dans P3 : "
                         "le lot fidèle exige le noyau de P3")
    return int(c3["lot"])


def _meme_config_coeur(m: dict, config: dict, quoi: str) -> None:
    differentes = [k for k in CLES_COEUR if m["config"].get(k) != config.get(k)]
    if differentes:
        raise GardeArret(f"{quoi} faite sous une autre configuration du cœur ({differentes})")


def exiger_validation_coeur(racine: Path, chemin, config: dict) -> dict:
    """Le résultat scellé de l'étape « validation » du cœur, rattaché à son manifeste, de même configuration du cœur et
    de même code, **quelle que soit sa lecture** ; sa classe (clé `classe_validation`, lecture à trois classes du cœur)
    est obligatoire : absente, refus (déclaré). Rend {classe, lecture, chemin, sha256}."""
    if not chemin:
        raise GardeArret("étape « resolution-lot » sans --validation : la validation du cœur est obligatoire")
    corps = verifier_resultat(racine, chemin)
    m, _ = lire_manifeste(Path(racine) / "runs" / corps["run_id"] / "manifeste.json")
    r = corps["resultat"]
    if r.get("etape") != "validation" or r.get("version") != rg.VERSION:
        raise GardeArret(f"validation {chemin} : étape {r.get('etape')!r}, version {r.get('version')!r}")
    _meme_config_coeur(m, config, "validation du cœur")
    rg.exiger_meme_code(racine, m["commit"])
    classe = r.get(CLE_CLASSE)
    if not isinstance(classe, str) or not classe:
        raise GardeArret(f"validation {chemin} sans « {CLE_CLASSE} » : la lecture à trois classes du cœur "
                         "(lire_validation) est exigée pour la recopier dans le lot et la table v3 (I-B) ; refus")
    return {CLE_CLASSE: classe, "lecture": r.get("lecture"), "chemin": str(chemin), "sha256": verifier(chemin)}


def exiger_resolution_v1(racine: Path, chemin, config: dict) -> tuple[list[str], dict, dict]:
    """Le résultat scellé de l'étape « resolution » du cœur, rattaché à son manifeste, de même configuration du cœur et
    de même code ; rend (ses épisodes non résolus, dans l'ordre ; {épisode : identifiants} de ses épisodes résolus, à
    revérifier par l'empreinte avant usage ; {chemin, sha256})."""
    if not chemin:
        raise GardeArret("étape « resolution-lot » sans --resolution : le résultat de la résolution du cœur est "
                         "obligatoire")
    corps = verifier_resultat(racine, chemin)
    m, _ = lire_manifeste(Path(racine) / "runs" / corps["run_id"] / "manifeste.json")
    r = corps["resultat"]
    if r.get("etape") != "resolution" or r.get("version") != rg.VERSION:
        raise GardeArret(f"résolution du cœur {chemin} : étape {r.get('etape')!r}, version {r.get('version')!r}")
    _meme_config_coeur(m, config, "résolution du cœur")
    rg.exiger_meme_code(racine, m["commit"])
    resolus = {x["episode"]: x["ids"] for x in r.get("episodes", []) if x.get("statut") == "resolu" and x.get("ids")}
    return [x["episode"] for x in r["non_resolus"]], resolus, {"chemin": str(chemin), "sha256": verifier(chemin)}


def cibles_du_lot(config: dict, pieces: rg.Pieces, non_resolus_v1: list[str]) -> tuple[list[str], list[dict]]:
    """Cibles (avant tout chargement) : non résolus du cœur dont l'entrée de la table v2 est « non_resolu »
    (`episodes_resolution_lot`, s'il est donné, en restreint la liste : chacun doit en être, sinon refus). Les autres
    non résolus du cœur sont rendus dans `hors_cibles`, cause écrite."""
    par_table = {x["episode"]: x for x in pieces.table["episodes"]}
    nr = list(non_resolus_v1 or [])

    def raison(e):
        if e not in pieces.par_episode:
            return "absent du run de P3"
        ent = par_table.get(e)
        if ent is None:
            return "absent de la table v2"
        if ent["methode"] != "non_resolu":
            return (f"entrée de la table v2 « {ent['methode']} », déjà prouvée par l'empreinte de P3 (C-6) : pas une "
                    "cible du lot")
        return None

    demandes = list(config["episodes_resolution_lot"])
    if demandes:
        hors = [e for e in demandes if e not in nr]
        if hors:
            raise GardeArret(f"resolution-lot : épisodes résolus par le cœur ou absents de son résultat : {hors[:3]}")
        refuses = [(e, raison(e)) for e in demandes if raison(e)]
        if refuses:
            raise GardeArret(f"resolution-lot : {refuses[0][0]} : {refuses[0][1]}")
        cibles = demandes
    else:
        cibles = [e for e in nr if raison(e) is None]
    hors_cibles = [{"episode": e, "cause": raison(e) or "hors de episodes_resolution_lot"} for e in nr if e not in cibles]
    if not cibles:
        raise GardeArret("resolution-lot : aucune cible (aucun non résolu du cœur à entrée « non_resolu » de la table v2) "
                         f"; hors cibles : {[x['episode'] for x in hors_cibles][:3]}")
    return cibles, hors_cibles


def exiger_execution_unique(racine: Path, config: dict, etape: str) -> None:
    """R3 : une seule exécution d'une étape par configuration ; tout manifeste de `runs/` de même commande et de même
    empreinte de configuration arrête avant tout calcul (toute reprise relève d'un texte neuf)."""
    commande, sha = f"{COMMANDE} --etape {etape}", rg.empreinte_config(config)
    for chemin in sorted((Path(racine) / "runs").glob("*/manifeste.json")):
        try:
            m = json.loads(chemin.read_text(encoding="utf-8"))
        except (OSError, ValueError) as e:
            raise GardeArret(f"R3 : manifeste illisible {chemin} ({e}) : unicité de l'étape non vérifiable")
        if m.get("commande") == commande and m.get("config_sha256") == sha:
            raise GardeArret(f"R3 : étape « {etape} » déjà exécutée sous cette configuration (run {m.get('run_id')}) ; "
                             "toute reprise relève d'un texte neuf")


def ecrire_pas(dossier: Path, etape: str, resultats: list, pas_tous: list) -> tuple[str, str]:
    """Journal des pas scellé, au format du cœur, plus deux colonnes : p du jeton retenu, argmax des logits."""
    chemin = dossier / f"pas-resolution-graine-{etape}.npz"
    if chemin.exists():
        raise GardeArret(f"{chemin} existe déjà : R12 interdit d'écraser")
    lignes_pas = [(i, *x) for i, pas in enumerate(pas_tous) for x in pas]
    with open(chemin, "wb") as f:
        col = list(zip(*lignes_pas)) if lignes_pas else [()] * 12
        np.savez_compressed(f, episodes=np.array([r["episode"] for r in resultats]),
                            episode=np.asarray(col[0], dtype=np.int32), pas=np.asarray(col[1], dtype=np.int16),
                            rang=np.asarray(col[2], dtype=np.int16), choix=np.asarray(col[3], dtype=np.int64),
                            non_contraint=np.asarray(col[4], dtype=np.int64),
                            candidats=np.asarray(col[5], dtype=np.int32), ecart=np.asarray(col[6], dtype=np.float64),
                            second=np.asarray(col[7], dtype=np.int64), marge=np.asarray(col[8], dtype=np.float64),
                            balayage=np.asarray(col[9], dtype=bool), p_choix=np.asarray(col[10], dtype=np.float64),
                            argmax_logits=np.asarray(col[11], dtype=np.int64))
    return chemin.name, sceller(chemin)


def _non_tente_lot(ep: rg.EpisodeP3, motif: str, rang: int, lot: list[str], k_lot: int, seuil: float) -> dict:
    r = rg.non_tente(ep, motif)
    r.update(rang_dans_le_lot=rang, numero_lot=k_lot, lot=[{"episode": e, "source": None, "exacte": None} for e in lot],
             lignes_approchees=None, plans=[], empreintes_logits=[], logits_conformes=None, forme=forme_des_plans([]),
             mesure_voisines=mesure_des_voisines([], seuil), lecture_lot=LECTURE_SANS, accord_cible=accords_cible([]))
    return r


def _executer(config, racine, run_id, chemin_m, pieces, etat, debut, cibles, hors_cibles, validation, resolution,
              resolus_v1, non_resolus_v1) -> dict:
    from ..harnais.modeles import regler_determinisme
    from ..harnais.validation_reelle import noyau
    from .rejeu_activations_v1 import progres

    etape = ETAPE_LOT
    reel = config["mode"] == "reel"
    appareil = "cuda" if reel else "cpu"
    reglages_det = regler_determinisme(config["fils"], appareil)
    T = int(config["T"])
    seuil = float(config["seuil_lecture_lot"])
    echeance = debut + float(config["duree_max_lot_s"])
    environnement = rg.environnement_d_execution(reel)
    reserves = rg.reserves_environnement(environnement, reel)
    etat["reserves"] = reserves
    modele, fmt = rg._modele(config, racine, pieces)
    attendu = config["agent"].get("texte_attendu_ouverture")
    if reel and not attendu:
        raise GardeArret("agent : texte attendu dans l'ouverture absent de la configuration")
    etat["etape"] = "classement"
    classement = rg.classer(pieces, fmt, T)
    taille = exiger_meme_lot_que_p3(config, pieces.manifeste_p3)
    from ..environnements.pilote_a import charger_taches

    lots = plan_des_lots(charger_taches(Path(racine) / config["chemin_taches"]), taille, pieces.lignes)
    ordre = {e: k for k, lot in enumerate(lots) for e in lot}
    episodes = sorted(cibles, key=lambda e: (ordre[e], lots[ordre[e]].index(e)))
    if attendu:
        e0 = rg.EpisodeP3(pieces, episodes[0], T).env()
        if attendu not in fmt.tok.decode(fmt.ouverture(e0.consigne_privee(0), e0.observation(0, 0, []))):
            raise GardeArret(f"agent : ouverture sans {attendu!r} (variables du gabarit non lues)")
    voc = Vocabulaire(fmt.tok, fmt.fins, int(modele.config.vocab_size))
    etat["equivalence_tirage"] = rg.exiger_equivalence_tirage(voc.V)
    moteur = MoteurLot(modele)
    reglages = rg.reglages_de(config, echeance, float(config["duree_max_episode_lot_s"]))
    cmax = int(config["combinaisons_max_lot"])
    tirages = rg.Tirages(voc.V, int(config["fils_tirages"]))
    eps = {e: rg.EpisodeP3(pieces, e, T) for e in episodes}
    connus: dict = connus_de_la_v1(pieces, fmt, T, resolus_v1 or {})
    dossier = Path(racine) / "diag" / run_id
    dossier_eps = dossier / f"episodes-{etape}"
    resultats, pas_tous = [], []
    etat["episodes_consignes"] = []
    etat["etape"] = etape
    progres(etape=etape, episodes=len(episodes), lots=len(lots), taille_lot=taille)
    try:
        with noyau(config["noyau_attention"]):
            for k, e in enumerate(episodes):
                exiger_sans_signal(f"lot fidèle, épisode {k}")
                ep = eps[e]
                k_lot, lot, rang = lot_de(lots, e)
                if rg.horloge() > echeance:
                    r = _non_tente_lot(ep, f"budget de l'étape ({config['duree_max_lot_s']} s) épuisé avant l'épisode "
                                           f"{k}", rang, lot, k_lot, seuil)
                else:
                    for e2 in episodes[k:k + 1 + int(config["episodes_d_avance"])]:
                        tirages.demander(e2, eps[e2].graines, eps[e2].jetons)
                    lignes = lignes_du_lot(pieces, fmt, T, classement, lot, e, connus)
                    Qs = tirages.prendre(e)
                    r = resoudre_episode_lot(moteur, voc, fmt, lignes, rang, T, Qs, ep.empreinte, reglages, cmax,
                                             seuil_lecture=seuil)
                    del Qs
                r.update(graines=ep.graines, numero_lot=k_lot, classe_validation=validation[CLE_CLASSE])
                if r["statut"] == "resolu":
                    connus[e] = (r["ids"], "lot_fidele")
                pas_tous.append(r.pop("pas", []))
                r.pop("pas_direct", None)
                resultats.append(r)
                etat["episodes_consignes"].append(rg.consigner_episode(dossier_eps, k, r))
                etat["episodes_traites"] = k + 1
                progres(etape=etape, episodes=f"{k + 1}/{len(episodes)}",
                        resolus=sum(x["statut"] == "resolu" for x in resultats), passes=moteur.passes)
    finally:
        tirages.fermer()
    etat["etape"] = "mesures"
    detail, ecarts, marges_desaccord = [], [], []
    for r, pas in zip(resultats, pas_tous):
        e = r["episode"]
        ecarts += [x[5] for x in pas if x[4] > 1]
        marges_desaccord += [x[7] for x in pas if x[3] != x[2]]
        d = {k2: r[k2] for k2 in ("episode", "statut", "voie", "cause", "forcages", "combinaisons_essayees", "passes",
                                  "balayages", "fffd", "duree_s", "graines", "numero_lot", "rang_dans_le_lot", "lot",
                                  "lignes_approchees", "plans", "empreintes_logits", "empreinte", "empreinte_cible",
                                  "quasi_egalites", "duree_epuisee", "non_tente", "repli", "forme", "mesure_voisines",
                                  "lecture_lot", "accord_cible", "classe_validation", "ids_directs") if k2 in r}
        d["empreinte_retrouvee"] = r["statut"] == "resolu" and r["empreinte"] == r["empreinte_cible"]
        d["pas"] = len(pas)
        d["ecart_min"] = min((x[5] for x in pas if x[4] > 1), default=None)
        d["ids"] = r["ids"]
        d["base_nv"] = classement[e]["base_nv"]
        detail.append(d)
    trouvees = sum(1 for x in detail if x["empreinte_retrouvee"])
    dossier.mkdir(parents=True, exist_ok=True)
    nom_pas, sha_pas = ecrire_pas(dossier, etape, resultats, pas_tous)
    # mesure des voisines poolée sur l'étape (épisodes tentés)
    pool = [x for d in detail for x in (d.get("mesure_voisines") or {}).get("par_ligne", {}).values()]
    n_pool = sum(x["pas"] for x in pool)
    lectures = [d["lecture_lot"] for d in detail if d["lecture_lot"] != LECTURE_SANS]
    lecture_lot = LECTURE_SANS if not lectures else (LECTURE_FIDELE if all(x == LECTURE_FIDELE for x in lectures)
                                                     else LECTURE_RESERVE)
    resultat = {
        "etape": etape, "version": VERSION, "regle": REGLE, "run_source": config["run_source"],
        "taille_lot": taille, "lots": len(lots), "episodes_etape": len(episodes), "cibles": episodes,
        "hors_cibles": hors_cibles, "empreintes_retrouvees": trouvees,
        "directes": sum(x["voie"] == "directe" for x in resultats),
        "par_repli": sum(x["voie"] == "repli" for x in resultats),
        "par_repli_bascules": {str(n): sum(1 for x in resultats if x["voie"] == "repli" and len(x["forcages"]) == n)
                               for n in range(1, int(config["bascules_max"]) + 1)},
        "non_resolus": [{"episode": x["episode"], "cause": x["cause"]} for x in resultats if x["statut"] != "resolu"],
        "non_resolus_duree": sum(1 for x in resultats if x["statut"] != "resolu" and x.get("duree_epuisee")),
        "non_tentes": sum(1 for x in resultats if x.get("non_tente")),
        "lignes_approchees": {d["episode"]: d["lignes_approchees"] for d in detail if d.get("lignes_approchees")},
        "forme": {d["episode"]: d["forme"] for d in detail},
        "accord_cible": {d["episode"]: d["accord_cible"] for d in detail},
        "mesure_voisines": {"pas": n_pool,
                            "accord": (sum(x["accord"] * x["pas"] for x in pool if x["pas"]) / n_pool) if n_pool
                            else None,
                            "accord_attendu_graine_independante":
                                (sum(x["accord_attendu_graine_independante"] * x["pas"] for x in pool if x["pas"])
                                 / n_pool) if n_pool else None,
                            "par_episode": {d["episode"]: {k2: d["mesure_voisines"][k2] for k2 in
                                                           ("pas", "accord", "accord_attendu_graine_independante",
                                                            "pas_informatifs", "accord_informatifs",
                                                            "contraints_mesures", "egalite_contraints",
                                                            "hors_candidats", "non_mesures_fffd", "lecture")}
                                            for d in detail}},
        "lecture_lot": lecture_lot, CLE_CLASSE: validation[CLE_CLASSE],
        "lecture_validation": {CLE_CLASSE: validation[CLE_CLASSE], "lecture_validation_coeur": validation["lecture"],
                               "lecture_lot": lecture_lot},
        "validation": validation, "resolution_v1": resolution, "non_resolus_v1": non_resolus_v1,
        "ecarts_contraints": rg.quantiles(ecarts), "marges_en_desaccord": rg.quantiles(marges_desaccord),
        "fffd_declares": {x["episode"]: x["fffd"] for x in resultats if x["fffd"]},
        "passes": moteur.passes, "jetons_en_passe": moteur.jetons, "seuils": {
            k: config[k] for k in ("seuil_ecart", "quasi_egalites_max", "bascules_max", "combinaisons_max_lot",
                                   "balayages_max", "duree_max_episode_lot_s", "duree_max_lot_s", "seuil_lecture_lot")},
        "equivalence_tirage": etat["equivalence_tirage"], "reglages": reglages_det, "modele": config["agent"],
        "noyau_attention": config["noyau_attention"], "environnement": environnement,
        "environnement_p3": rg.ENVIRONNEMENT_P3, "reserves": reserves, "episodes_consignes": etat["episodes_consignes"],
        "pas_fichier": nom_pas, "pas_sha256": sha_pas, "episodes": detail,
        "duree_s": round(rg.horloge() - debut, 1)}
    resultat["lecture"] = "complète" if trouvees == len(episodes) else ("partielle" if trouvees else "aucune")
    ecrire_resultat(racine, chemin_m, f"resolution-graine-{etape}", resultat)
    progres(etape="fin", resolus=f"{trouvees}/{len(episodes)}", lecture=resultat["lecture"].replace(" ", "_"),
            lecture_lot=lecture_lot.replace(" ", "_"))
    return resultat


def connus_de_la_v1(pieces: rg.Pieces, fmt, T: int, resolus: dict) -> dict:
    """Identifiants résolus par le cœur, chacun revérifié par l'empreinte de trajectoire de P3 (arrêt sinon) :
    {épisode : (identifiants, « resolution_v1 »)}, lignes exactes pour les lots de cette étape."""
    sortie = {}
    for e, ids in resolus.items():
        ep = rg.EpisodeP3(pieces, e, T)
        ids = [[int(x) for x in a] for a in ids]
        rec = rg.transcription(fmt, ep.env(), T, ep.textes, ids, ep.jetons, ep.jetons_notes)
        if empreinte_trajectoire(episode_harnais(e, T, rec)) != ep.empreinte:
            raise GardeArret(f"{e} : les identifiants résolus par le cœur ne redonnent pas l'empreinte de P3")
        sortie[e] = (ids, "resolution_v1")
    return sortie


def executer(config: dict, racine: Path, run_id: str, prereg: str | None, etape: str, validation: str | None = None,
             resolution: str | None = None, autoriser_depot_sale: bool = False,
             entropie_essai: int | None = None) -> dict:
    """Étape « resolution-lot ». Gardes avant tout chargement du modèle : configuration (cœur et lot), préenregistrement
    (configuration du lot citée, entropie, code), pièces de P3 et noyau de P3, validation du cœur (classe exigée),
    résolution du cœur, cibles, unicité de l'étape (R3) ; puis manifeste."""
    racine = Path(racine)
    exiger_config(config)
    if etape not in ETAPES:
        raise GardeArret(f"étape {etape!r} : {ETAPES} attendues (« {ETAPE_TABLE} » : construire_table_v3_lot)")
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
    val = exiger_validation_coeur(racine, validation, config)
    non_resolus_v1, resolus_v1, res = exiger_resolution_v1(racine, resolution, config)
    cibles, hors_cibles = cibles_du_lot(config, pieces, non_resolus_v1)
    exiger_execution_unique(racine, config, etape)
    chemin_m, _ = creer_manifeste(racine, run_id, config, ["aucun-tirage-propre"], entropie=entropie,
                                  decisif=prereg is not None, prereg=prereg, autoriser_depot_sale=autoriser_depot_sale,
                                  commande=f"{COMMANDE} --etape {etape}")
    etat = {"etape": "chargement"}
    debut = rg.horloge()
    try:
        return _executer(config, racine, run_id, chemin_m, pieces, etat, debut, cibles, hors_cibles, val, res,
                         resolus_v1, non_resolus_v1)
    except Exception as e:
        ecrire_resultat(racine, chemin_m, "arret", {"etape": etat["etape"], "motif": motif_d_arret(e),
                                                     "partiel": {k: v for k, v in etat.items() if k != "etape"},
                                                     "duree_s": round(rg.horloge() - debut, 1)})
        relever_term_apres(e)
        raise


# --------------------------------------------------------------------------------------------------------------------
# Étape « table-lot » : table v3 depuis la résolution du cœur et le lot


def construire_table_v3_lot(config: dict, racine: Path, tokeniseur: str | None, chemin_resolution: str,
                            chemin_lot: str, fmt=None) -> dict:
    """Table v3 (processeur) : table v3 du cœur (`rg.construire_table_v3` sur la table v2 et le résultat scellé de la
    résolution du cœur), puis les épisodes résolus par le lot (résultat scellé de « resolution-lot », fait sur **ce**
    résultat du cœur, même configuration), chacun revérifié par l'empreinte de P3 avant d'être versé ; refus : contrôle
    croisé du cœur autre que « conforme », deux résultats différents pour un même épisode, épisode du lot hors de la
    table v2 ou d'entrée autre que « non_resolu », classe de la validation absente. Toutes les entrées revérifiées
    (`rg.verifier_entrees_v3`) ; classe de la validation et lecture du lot recopiées (`lecture_validation`)."""
    exiger_config(config)
    racine = Path(racine)
    pieces = rg.charger_pieces(config, racine)
    corps_r = verifier_resultat(racine, chemin_resolution)
    m_r, _ = lire_manifeste(racine / "runs" / corps_r["run_id"] / "manifeste.json")
    _meme_config_coeur(m_r, config, "résolution du cœur")
    r = corps_r["resultat"]
    if r.get("etape") != "resolution" or r.get("version") != rg.VERSION:
        raise GardeArret(f"résolution du cœur {chemin_resolution} : étape {r.get('etape')!r}")
    if r.get("controle_croise_lecture") != "conforme":
        raise GardeArret(f"contrôle croisé du cœur « {r.get('controle_croise_lecture')} » ≠ « conforme » : audit (R4) "
                         "avant la table v3")
    sha_r = verifier(chemin_resolution)
    corps_l = verifier_resultat(racine, chemin_lot)
    m_l, _ = lire_manifeste(racine / "runs" / corps_l["run_id"] / "manifeste.json")
    if m_l["config_sha256"] != rg.empreinte_config(config):
        raise GardeArret("résultat du lot fait sous une autre configuration")
    lot = corps_l["resultat"]
    if lot.get("etape") != ETAPE_LOT or lot.get("version") != VERSION:
        raise GardeArret(f"résultat du lot {chemin_lot} : étape {lot.get('etape')!r}, version {lot.get('version')!r}")
    if (lot.get("resolution_v1") or {}).get("sha256") != sha_r:
        raise GardeArret("résultat du lot fait sur un autre résultat de la résolution du cœur")
    classe = lot.get(CLE_CLASSE)
    if not isinstance(classe, str) or not classe:
        raise GardeArret(f"résultat du lot sans « {CLE_CLASSE} » : refus (I-B)")
    sha_l = verifier(chemin_lot)
    if fmt is None:
        from transformers import AutoTokenizer

        from ..harnais.formats import FormatChat

        tok = AutoTokenizer.from_pretrained(tokeniseur)
        fmt = FormatChat(tok, variables=config["agent"]["variables_gabarit"])
        fmt.fins = {int(x) for x in pieces.table["fins_du_format"]} | {fmt._pieces(("x", "y"))["cloture"][0]}
    T = int(config["T"])
    classement = rg.classer(pieces, fmt, T)
    base_nv = {e: c["base_nv"] for e, c in classement.items()}
    sha_v2 = verifier(racine / config["chemin_table_tokenisation"])
    table = rg.construire_table_v3(pieces.table, sha_v2, r, sha_r, base_nv)
    ids_coeur = {x["episode"]: x.get("ids") for x in r["episodes"] if x.get("statut") == "resolu"}
    par_e = {x["episode"]: i for i, x in enumerate(table["episodes"])}
    vus: dict = {}
    verses = []
    for x in lot["episodes"]:
        if x.get("statut") != "resolu":
            continue
        e, ids = x["episode"], [[int(y) for y in a] for a in x["ids"]]
        if e in vus:
            if vus[e] != ids:
                raise GardeArret(f"{e} : deux résultats du lot différents pour un même épisode")
            continue
        vus[e] = ids
        if e in ids_coeur:
            if [[int(y) for y in a] for a in ids_coeur[e]] != ids:
                raise GardeArret(f"{e} : résultats du cœur et du lot différents pour un même épisode")
            continue
        if e not in par_e:
            raise GardeArret(f"{e} : résolu par le lot mais absent de la table v2")
        ent = table["episodes"][par_e[e]]
        if ent["methode"] != "non_resolu":
            raise GardeArret(f"{e} : entrée « {ent['methode']} » dans la table : le lot ne la remplace pas")
        traj = pieces.fiches[e]["trajectoire"]
        if x.get("empreinte_cible") != traj or x.get("empreinte") != traj or ent["trajectoire_p3"] != traj:
            raise GardeArret(f"{e} : « résolu » par le lot sans l'empreinte de P3 égale")
        ep = rg.EpisodeP3(pieces, e, T)
        rec = rg.transcription(fmt, ep.env(), T, ep.textes, ids, ep.jetons, ep.jetons_notes)
        if empreinte_trajectoire(episode_harnais(e, T, rec)) != traj:
            raise GardeArret(f"{e} : les identifiants du lot ne redonnent pas l'empreinte de P3 (revérification)")
        res = {"voie": f"lot_fidele:{x.get('voie')}", "forcages": x.get("forcages"), "resultat_sha256": sha_l,
               CLE_CLASSE: classe, "lecture_lot": x.get("lecture_lot"),
               "forme_exacte_prouvee": (x.get("forme") or {}).get("forme_exacte_prouvee")}
        table["episodes"][par_e[e]] = {**rg.entree_identifiants(e, traj, base_nv[e], ids, res),
                                       "essais": ent.get("essais"), "essais_c6": ent.get("essais_c6")}
        verses.append(e)
    comptes = {k: v for k, v in table["comptes"].items() if k not in rg.METHODES_V3 and k != "identiques_apres_table"}
    for m in rg.METHODES_V3:
        comptes[m] = sum(1 for x in table["episodes"] if x["methode"] == m)
    comptes["identiques_apres_table"] = comptes["identiques_base"] + sum(comptes[m] for m in rg.CORRIGEES_V3)
    table["comptes"] = comptes

    def contexte(e):
        ep = rg.EpisodeP3(pieces, e, T)
        return ep.env(), ep.lignes, ep.jetons, ep.jetons_notes, T

    n = rg.verifier_entrees_v3(table["episodes"], fmt, contexte, pieces.fiches)
    if n != comptes["identiques_apres_table"] - comptes["identiques_base"]:
        raise GardeArret("corrections vérifiées ≠ comptes de la table")
    table.update(corrections_verifiees=n, regle_lot=REGLE, resultat_lot_sha256=sha_l, episodes_verses_par_le_lot=verses,
                 non_resolus_apres_lot=[x["episode"] for x in table["episodes"] if x["methode"] == "non_resolu"],
                 lecture_validation={CLE_CLASSE: classe, "lecture_lot": lot.get("lecture_lot"),
                                     "validation": lot.get("validation"),
                                     "lectures_lot_par_episode": {x["episode"]: x.get("lecture_lot")
                                                                  for x in lot["episodes"]}})
    return table


def _main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(prog=COMMANDE)
    ap.add_argument("--etape", required=True, choices=ETAPES + (ETAPE_TABLE,))
    ap.add_argument("--config", required=True)
    ap.add_argument("--run-id")
    ap.add_argument("--prereg", default=None)
    ap.add_argument("--validation", default=None, help="résultat scellé de l'étape validation du cœur")
    ap.add_argument("--resolution", default=None, help="résultat scellé de l'étape resolution du cœur")
    ap.add_argument("--tokeniseur", help="dossier du tokeniseur à la révision de P3 (étape table-lot)")
    ap.add_argument("--resultat-lot", help="résultat scellé de l'étape resolution-lot (étape table-lot)")
    ap.add_argument("--sortie", help="table version 3 à écrire (étape table-lot ; jamais écrasée)")
    a = ap.parse_args(argv)
    signal.signal(signal.SIGTERM, lever_sur_term)
    verifier(a.config)
    config = json.loads(Path(a.config).read_text(encoding="utf-8"))
    if a.etape == ETAPE_TABLE:
        if not (a.tokeniseur and a.resolution and a.resultat_lot and a.sortie):
            raise GardeArret("étape table-lot : --tokeniseur, --resolution, --resultat-lot et --sortie obligatoires")
        sortie = Path(a.sortie)
        if sortie.exists() or Path(f"{sortie}.sha256").exists():
            raise GardeArret(f"{sortie} existe déjà (R12 : on n'écrase jamais)")
        table = construire_table_v3_lot(config, Path("."), a.tokeniseur, a.resolution, a.resultat_lot)
        sha = rg.ecrire_table_v3(table, sortie)
        print(json.dumps({"comptes": table["comptes"], "corrections_verifiees": table["corrections_verifiees"],
                          "lecture_validation": table["lecture_validation"][CLE_CLASSE], "sha256": sha},
                         ensure_ascii=False))
        return 0
    if not a.run_id:
        raise GardeArret("--run-id obligatoire")
    r = executer(config, Path("."), a.run_id, a.prereg, a.etape, a.validation, a.resolution)
    print(json.dumps({"etape": r["etape"], "lecture": r["lecture"], "lecture_lot": r["lecture_lot"],
                      "empreintes_retrouvees": r["empreintes_retrouvees"], "episodes": r["episodes_etape"]},
                     ensure_ascii=False))
    return 0


if __name__ == "__main__":
    try:
        sys.exit(_main(sys.argv[1:]))
    except GardeArret as e:
        print(f"ARRÊT : {e}", file=sys.stderr)
        sys.exit(1)
