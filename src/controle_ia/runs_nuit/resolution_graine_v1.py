"""Rejeu à graine : retrouver les identifiants que l'agent de P3 a tirés, depuis le texte stocké, les graines du manifeste
de P3 et le modèle (relance de R1, demande de Lazar « résoudre les 7 épisodes avant la relance » ; addendum
`prereg/R1-addendum-relance-v2.md`, à sceller). Version 1, nom nouveau (R12) : `resolution_tokenisation_v1.py` n'est pas
modifié ; ses tables (versions 1 et 2) et leurs formes restent acceptées telles quelles.

**Mécanisme** (code de P3 : `premier_test_ia.run.jouer_p3`, `harnais.episode.generer_lot`). Chaque action (i, t) d'un
épisode a sa graine, `graines_des_actions(generateur(graine de la tâche), 1, T)` (générateur numpy de la tâche, clé
`tache/<identifiant>` du manifeste de P3 ; le tirage `g.random(T)` de l'échantillon d'équivalence vient après et ne la
change pas) ; P3 tirait chaque jeton par `torch.multinomial(softmax(logits / température), 1, generator=g)`, un
`torch.Generator('cpu')` par action, avancé d'un pas par jeton tant que la ligne est active ; logits en float32 sur
processeur ; température 1, ni top_p ni top_k ; au plus `max_nouveaux` jetons. Sur torch 2.14.1, ce tirage est
exactement `argmax(p / q)`, où `q` est le vecteur de tirages exponentiels `torch.empty_like(p).exponential_(1, generator=g)`
(taille = dimension des logits ; vérifié au lancement par `exiger_equivalence_tirage`). Donc, à chaque pas, le jeton
tiré est fixé par la graine, aux arrondis des logits près.

**Méthode** (`resoudre_action`, `rejouer_episode`, `resoudre_avec_repli`). Pour chaque action, dans l'ordre, dans le
contexte exact (jetons déjà retrouvés des actions précédentes, gabarit comme le harnais : ouverture, tour, clôture) :
passe avant forcée par l'enseignant sur le découpage courant (découpage canonique du texte restant, plus le jeton de fin
par défaut) ; à chaque pas, choix, parmi les **jetons compatibles avec les octets restants du texte stocké** (décodeur
au niveau de l'octet ; jetons spéciaux hors fins : zéro octet, effacés du texte par P3), de celui qui maximise `p / q` :
`p = softmax(logits / température)` en float32 sur processeur, ligne par ligne, comme P3, puis `log p − log q` en double
sur les candidats (`probabilites`, `scores_contraints` ; égalité exacte : plus petit identifiant) ; si le choix diffère
du découpage courant, le reste est redécoupé canoniquement et une nouvelle passe est faite. Le dernier jeton d'une
action est un jeton de fin (parmi `fmt.fins`, même règle) quand `jetons − jetons_notes = 1` (stocké par P3) ; sinon
l'action compte `max_nouveaux` jetons. Consigné par pas : choix contraint, choix non contraint (argmax de `p / q` sur
tout le vocabulaire, en float32 sur processeur : l'opération même de P3), nombre de candidats, écart en log entre le
premier et le second candidat compatibles, marge en log du choix non contraint, pas de recherche sur octets inconnus,
probabilité `p_k` du jeton retenu et argmax de `p` (`mesures_accord` : accord du choix non contraint avec le jeton
retenu, accord attendu sous une graine indépendante = moyenne des `p_k`, accord sur les pas informatifs, où le jeton
retenu n'est pas l'argmax de `p` ; calculés pour tout épisode, résolu ou non). **Arbitre unique : l'empreinte de
trajectoire de P3** (sha256 de l'épisode du harnais), recalculée sur l'épisode reconstruit.

**Repli écrit, itératif** (`resoudre_avec_repli`) : si l'empreinte n'est pas retrouvée, les quasi-égalités de l'essai
direct (écart sous `seuil_ecart`, au plus `quasi_egalites_max`, les plus fragiles d'abord) sont basculées vers leur
second candidat, une à la fois ; chaque rejeu basculé (arrêté ou non par une contradiction : son journal partiel compte)
apporte ses propres quasi-égalités, **après** sa dernière bascule (au plus `quasi_egalites_max`), qui forment la
frontière du niveau suivant (deux bascules, jusqu'à `bascules_max`) ; dans chaque niveau, les combinaisons de plus
faible écart cumulé d'abord ; au plus `combinaisons_max` rejeux en tout, chacun rejoué depuis l'action de sa première
bascule et arbitré par l'empreinte ; sinon « non résolu », avec sa cause. Une bascule change souvent le découpage, donc
la longueur des jetons qui suivent : la seconde erreur d'une paire n'apparaît que dans le rejeu de la première, d'où la
frontière enrichie. Caractère de remplacement U+FFFD dans le texte : **cas déclaré** (compté par épisode). Le jeton de
P3 reste dans l'ensemble contraint à chaque pas ; près d'un U+FFFD, la recherche couvre des octets inconnus
(`Cible.recherche` : jetons qui prolongent les octets connus au-delà, `commencant_par(E)` non vide). **Unité de
`balayages_max`** : un pas où cette recherche est faite avec un ensemble non vide ; plafond par essai = `balayages_max`
× nombre de U+FFFD de l'épisode. Au-delà : « non résolu », cause « caractère de remplacement : budget de balayages
dépassé » — un budget de recherche dépassé, non une preuve d'impossibilité ; il n'est déclaré « non inversible par la
méthode » (règle B) que sous la classe « graines validées » de la validation (`declarer`).

**Durées** : budget par épisode (`duree_max_episode_s`) et par étape (`duree_max_s`) ; un épisode dont le budget s'épuise
finit « non résolu : durée » sans arrêter l'étape ; une fois le budget de l'étape épuisé, les épisodes restants sont
consignés « non tenté : durée » ; le résultat est toujours écrit. Chaque épisode traité est consigné aussitôt dans un
fichier scellé (`diag/<run>/episodes-<étape>/NNN.json` : statut, cause, identifiants retrouvés, empreinte), cité dans
`arret.json` en cas d'arrêt (signal, erreur de chaîne).

**Validation : une mesure, pas un arrêt** (décision de session sur VG-03 ; n° 265). La résolution se lance quelle que
soit la lecture de la validation ; seule une erreur de chaîne (pièces, sceaux, graines illisibles) arrête avant la
résolution ; un « résolu » ne se lit que sur l'égalité de l'empreinte de P3, revérifiée à la construction de la table.
**Règle gelée de lecture** (`lire_validation`, seuils de la clé `regle_validation` de la configuration), appliquée par
le code et écrite au résultat de la validation avant toute lecture humaine : « graines validées » (toutes les empreintes
retrouvées, accord moyen par épisode, minimum par épisode et accord sur les pas informatifs aux seuils, assez de pas
informatifs), « méthode transposée, graines non validées » (toutes les empreintes, une condition d'accord manquée), «
méthode non transposée » (une empreinte au moins non retrouvée). La lecture est recopiée dans le résultat de la
résolution (avec la déclaration de chaque épisode) et dans la table v3. **Une seule exécution de chaque étape** sous une
même configuration et un même code (`exiger_execution_unique`, R3) ; tout essai de plus relève d'un texte neuf.

**Forme nouvelle d'entrée de table** (`METHODE_IDENTIFIANTS`, table version 3) : identifiants explicites des actions
corrigées (`actions` : pas, identifiants de la reconstruction de base, identifiants retrouvés), appliquée par
`appliquer_entree_v3` (transcription refaite comme le harnais ; gardes : longueur, jeton de fin, texte décodé) et
acceptée par `verifier_table_v3`, qui revérifie chaque correction par l'empreinte de P3 ; les formes des versions 1 et 2
passent par `resolution_tokenisation_v1.appliquer_entree`, inchangée.

Interdits respectés par construction : de `scores-p3.npz`, seuls les tableaux d'identité, `jetons` et `jetons_notes` sont
lus (`charger_identite_sans_scores`, clé par clé) ; le fichier des consignes n'est lu que par `charger_consignes`, qui en
vérifie l'empreinte ; aucune activation, aucune note, aucune étiquette.

    PYTHONPATH=src python -m controle_ia.runs_nuit.resolution_graine_v1 --etape validation --config CONFIG \\
        --run-id AAAAMMJJ-HHMMSS-r1-graine-validation --prereg prereg/R1-addendum-relance-v2.md
    PYTHONPATH=src python -m controle_ia.runs_nuit.resolution_graine_v1 --etape resolution --config CONFIG \\
        --run-id AAAAMMJJ-HHMMSS-r1-graine-resolution --prereg prereg/R1-addendum-relance-v2.md \\
        --validation diag/<run de validation>/resolution-graine-validation.json
    PYTHONPATH=src python -m controle_ia.runs_nuit.resolution_graine_v1 --etape table --config CONFIG \\
        --tokeniseur DOSSIER --resultat diag/<run de résolution>/resolution-graine-resolution.json \\
        --sortie prereg/R1-table-tokenisation-v3.json          (processeur seulement)
"""
from __future__ import annotations

import argparse
import bisect
import collections
import codecs
import hashlib
import json
import math
import signal
import sys
import time
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass, field, replace
from pathlib import Path

import numpy as np
import torch

from ..gardes import GardeArret, etat_git, exiger_sans_signal, lever_sur_term, motif_d_arret, relever_term_apres
from ..manifeste import config_canonique, creer_manifeste, ecrire_resultat, generateur, lire_manifeste, verifier_resultat
from ..scellement import sceller, verifier
from . import resolution_tokenisation_v1 as rt
from .alignement_v1 import CLES_IDENTITE, charger_textes_alignes, empreinte_identite
from .rejeu_activations_v1 import episode_harnais, empreinte_trajectoire, reconstruire_episode

VERSION = "resolution_graine_v1"
COMMANDE = "python -m controle_ia.runs_nuit.resolution_graine_v1"
CONFIG_CITEE = "Configuration de la résolution à graine (empreinte canonique) : `{}`"
FFFD = "�"
ETAPES = ("validation", "resolution")
METHODE_IDENTIFIANTS = "identifiants"
VERSION_TABLE_V3 = 3
METHODES_V3 = rt.METHODES + (METHODE_IDENTIFIANTS,)
CORRIGEES_V3 = rt.CORRIGEES + (METHODE_IDENTIFIANTS,)
SEUILS_ECART_COMPTES = (0.01, 0.05, 0.1, 0.25, 0.5, 1.0, 2.0)
CLES = ("agent", "mode", "T", "run_source", "chemin_textes", "textes_sha256", "chemin_scores", "scores_sha256",
        "identite_sha256", "chemin_fiches", "fiches_sha256", "chemin_taches", "taches_sha256", "chemin_consignes",
        "consignes_sha256", "chemin_manifeste_p3", "manifeste_p3_sha256", "chemin_table_tokenisation",
        "table_tokenisation_sha256", "episodes_resolution", "temperature", "max_nouveaux", "noyau_attention", "fils",
        "hors_ligne", "fils_tirages", "episodes_d_avance", "seuil_ecart", "quasi_egalites_max", "bascules_max",
        "combinaisons_max", "combinaisons_max_validation", "balayages_max", "seuil_validation", "duree_max_s")
# clés ajoutées par les corrections VG-01 à VG-09 : exigées par `exiger_reglages_execution` (étapes validation et
# resolution de ce module) ; `CLES` reste la liste des versions antérieures (modules qui l'importent)
CLES_EXECUTION = ("duree_max_episode_s", "regle_validation")
# règle gelée de lecture de la validation (C-3 et R-01 de la lecture neuve de conv-audit) : seuils de `regle_validation`
CLES_REGLE_VALIDATION = ("accord_moyen_min", "accord_episode_min", "accord_informatif_min", "pas_informatifs_min")
CLASSES_VALIDATION = ("graines validées", "méthode transposée, graines non validées", "méthode non transposée")
CAUSE_BUDGET_BALAYAGES = "caractère de remplacement : budget de balayages dépassé"
DECLARATIONS = {
    "resolu": "résolu (empreinte de P3 retrouvée)",
    "budget": ("budget de recherche dépassé (caractère de remplacement) : non inversible déclaré par la méthode, "
               "règle B pour cet épisode (non preuve d'impossibilité)"),
    "graines_non_validees": "non résolu, graines non validées : nœud porté à Lazar",
    "noeud": "non résolu par la méthode : nœud porté à Lazar"}
CLES_COMPLETES = CLES + CLES_EXECUTION
# répétition jouet du script d'instance seulement : épisodes que l'étape « resolution » laisse non tentés (artefact de
# répétition, pour que l'étape du lot tourne) ; clé refusée en mode réel, même vide (`episodes_laisses_par_repetition`)
CLE_REPETITION = "repetition_non_tentes"
NOYAUX = ("defaut", "math")
CLES_AGENT_P3 = ("modele", "revision", "variables_gabarit")
# environnement de P3 (`diag/20261019-230011-p3-reel/episodes-p3.json`, manifeste de P3) : un écart est une réserve
# écrite au résultat, pas un arrêt (la version de torch, elle, arrête dans le script d'instance)
ENVIRONNEMENT_P3 = {"torch": "2.14.1+cu130", "cuda": "13.0", "cudnn": 92400, "carte": "A100-SXM4-80GB"}
REGLE = ("rejeu à graine : graines des actions de P3 (manifeste, clé tache/<identifiant>, graines_des_actions) ; à chaque "
         "pas, parmi les jetons compatibles avec les octets restants du texte stocké (spéciaux hors fins : zéro octet ; "
         "dernier pas : jeton de fin si jetons − jetons_notes = 1), celui qui maximise p / q, q = tirages exponentiels de "
         "la graine (p = softmax(logits / T) en float32 sur processeur, comme P3, puis log p − log q en double) ; passe "
         "forcée par l'enseignant, redécoupage canonique du reste après chaque divergence ; arbitre "
         "unique : empreinte de trajectoire de P3 ; repli itératif : bascule des quasi-égalités (écart sous le seuil) "
         "de l'essai direct, puis de chaque rejeu basculé après sa dernière bascule, une puis deux, combinaisons bornées, "
         "arbitrées par l'empreinte ; budgets par épisode et par étape (non résolu : durée) ; recherche sur octets inconnus "
         "près d'un U+FFFD bornée à balayages_max pas par U+FFFD (au-delà : budget de balayages dépassé) ; sinon non "
         "résolu, cause écrite")


def horloge() -> float:
    """Horloge des échéances (remplacée dans les essais pour éprouver une échéance en milieu d'étape)."""
    return time.perf_counter()


class Contradiction(Exception):
    """Le texte stocké, les longueurs de P3 et les choix ne s'accordent pas (essai à rejeter, pas une garde du run)."""

    def __init__(self, t: int, s: int, motif: str):
        super().__init__(f"pas {t}, jeton {s} : {motif}")
        self.t, self.s, self.motif = t, s, motif


class NonResolu(Exception):
    """Budget de recherche près d'un caractère de remplacement dépassé (`CAUSE_BUDGET_BALAYAGES`) : l'essai finit
    « non résolu » ; ce n'est pas une preuve d'impossibilité (le jeton de P3 reste dans l'ensemble contraint)."""


class DureeEpuisee(Exception):
    """Budget de l'épisode (ou de l'étape) épuisé pendant un essai : l'épisode finit « non résolu : durée », l'étape
    continue (ce n'est pas une garde d'arrêt du run)."""


# --------------------------------------------------------------------------------------------------------------------
# Graines et tirages


def graines_p3(manifeste_p3: dict, tache: str, T: int) -> list[int]:
    """Graines des actions (agent 0, pas t) d'un épisode de P3, dérivées exactement comme `jouer_p3` : générateur neuf de
    la tâche (`generateur(graines['tache/<identifiant>'])`), puis `graines_des_actions(g, 1, T)` ; le `g.random(T)` qui
    suit dans P3 (échantillon d'équivalence) ne touche pas ces graines. Mêmes graines d'une condition à l'autre."""
    from ..environnements.pilote_a import graines_des_actions

    cle = f"tache/{tache}"
    if cle not in manifeste_p3["graines"]:
        raise GardeArret(f"manifeste de P3 : graine {cle} absente")
    d = graines_des_actions(generateur(manifeste_p3["graines"][cle]), 1, T)
    return [int(d[(0, t)]) for t in range(T)]


def tirages_exponentiels(graine: int, n: int, V: int) -> torch.Tensor:
    """(n, V) : tirages exponentiels des n pas d'une action, dans l'ordre où `torch.multinomial` les a pris au générateur
    de l'action (un vecteur de V valeurs par pas ; un appel unique de n × V valeurs donne les mêmes, vérifié par
    `exiger_equivalence_tirage`)."""
    g = torch.Generator(device="cpu").manual_seed(int(graine))
    return torch.empty((int(n), int(V)), dtype=torch.float32).exponential_(1, generator=g)


def exiger_equivalence_tirage(V: int, graines=(0, 1, 2026, 2 ** 31 - 2), pas: int = 3) -> dict:
    """Garde au lancement (R5) sur la bibliothèque installée : (1) `torch.multinomial(p, 1, generator=g)` = argmax de
    p / q, q tiré au même générateur, pas après pas ; (2) un appel unique de `pas × V` tirages = `pas` appels de V. Arrêt
    sinon : la méthode suppose ces deux faits."""
    egalites = 0
    for k, graine in enumerate(graines):
        logits = torch.randn(V, generator=torch.Generator().manual_seed(1000 + k)) * 4
        p = torch.softmax(logits, dim=-1)
        g1 = torch.Generator(device="cpu").manual_seed(int(graine))
        tires = [int(torch.multinomial(p, 1, generator=g1)) for _ in range(pas)]
        Q = tirages_exponentiels(graine, pas, V)
        g2 = torch.Generator(device="cpu").manual_seed(int(graine))
        un_par_un = torch.stack([torch.empty(V, dtype=torch.float32).exponential_(1, generator=g2) for _ in range(pas)])
        if not torch.equal(Q, un_par_un):
            raise GardeArret("tirages exponentiels : un appel de n × V ≠ n appels de V (générateur non séquentiel)")
        par_q = [int(torch.argmax(p / Q[s])) for s in range(pas)]
        if tires != par_q:
            raise GardeArret(f"torch.multinomial ≠ argmax(p / q) sur la graine {graine} : la méthode ne s'applique pas "
                             f"à torch {torch.__version__}")
        egalites += pas
    return {"egalites": egalites, "torch": torch.__version__}


class Tirages:
    """Tirages exponentiels calculés d'avance, en parallèle (fils Python : un générateur par action, aucun partage),
    pendant que la carte travaille. `demander(cle, graines, longueurs)` puis `prendre(cle)`."""

    def __init__(self, V: int, fils: int = 1):
        self.V = int(V)
        self.pool = ThreadPoolExecutor(max_workers=max(1, int(fils)))
        self.futurs: dict = {}

    def demander(self, cle, graines: list[int], longueurs: list[int]) -> None:
        if cle not in self.futurs:
            self.futurs[cle] = [self.pool.submit(tirages_exponentiels, g, n, self.V) for g, n in zip(graines, longueurs)]

    def prendre(self, cle) -> list[torch.Tensor]:
        return [f.result() for f in self.futurs.pop(cle)]

    def fermer(self) -> None:
        self.pool.shutdown(wait=True, cancel_futures=True)


# --------------------------------------------------------------------------------------------------------------------
# Vocabulaire et compatibilité avec le texte stocké


class Vocabulaire:
    """Octets de chaque jeton (décodeur au niveau de l'octet pour Llama 3 ; texte UTF-8 sinon), jetons spéciaux (zéro
    octet au décodage avec `skip_special_tokens=True`, vérifié jeton par jeton), fins. Gardes : dimension des logits =
    taille du tokeniseur, octets uniques par jeton ordinaire, fins parmi les spéciaux."""

    def __init__(self, tok, fins, V: int):
        if int(V) != len(tok):
            raise GardeArret(f"dimension des logits {V} ≠ taille du tokeniseur {len(tok)}")
        octets, par_octets = rt.table_des_octets(tok)
        self.V = int(V)
        self.octets = [octets(i) for i in range(self.V)]
        speciaux = sorted(rt.ids_speciaux(tok))
        for i in speciaux:
            if tok.decode([i], skip_special_tokens=True) != "":
                raise GardeArret(f"jeton spécial {i} non effacé au décodage : hypothèse « zéro octet » fausse")
        ordinaires = [i for i in range(self.V) if self.octets[i] is not None]
        if len(ordinaires) + len(speciaux) != self.V or any(self.octets[i] is not None for i in speciaux):
            raise GardeArret("vocabulaire : jetons ni ordinaires ni spéciaux")
        if len(par_octets) != len(ordinaires) or any(not self.octets[i] for i in ordinaires):
            raise GardeArret("vocabulaire : octets en double ou vides parmi les jetons ordinaires")
        self.par_octets = par_octets
        self.fins = sorted(int(x) for x in fins)
        if not set(self.fins) <= set(speciaux):
            raise GardeArret(f"fins {self.fins} hors des jetons spéciaux")
        self.speciaux_non_fins = [i for i in speciaux if i not in set(self.fins)]
        self.cles = sorted(par_octets)
        self.ids_tries = [par_octets[k] for k in self.cles]
        self.maxlen = max(len(b) for b in par_octets)

    def prefixes(self, E: bytes) -> list[int]:
        """Jetons dont les octets sont un préfixe non vide de E."""
        return [self.par_octets[E[:k]] for k in range(1, min(len(E), self.maxlen) + 1) if E[:k] in self.par_octets]

    def commencant_par(self, E: bytes) -> list[int]:
        """Jetons dont les octets commencent par E et sont plus longs que E (tous si E est vide)."""
        sortie = []
        for k in range(bisect.bisect_left(self.cles, E), len(self.cles)):
            b = self.cles[k]
            if not b.startswith(E):
                break
            if len(b) > len(E):
                sortie.append(self.ids_tries[k])
        return sortie


class Cible:
    """Texte stocké d'une action, comme contrainte sur les octets générés. État : (caractères déjà rendus, octets en
    attente d'un caractère incomplet). Décodage comme le harnais : octets concaténés, UTF-8 avec remplacement (U+FFFD)
    des sous-parties maximales invalides (`tok.decode` de Llama 3 = `bytes.decode('utf-8', 'replace')`, vérifié par les
    tests). Hors U+FFFD, les candidats sont les jetons préfixes des octets restants ; près d'un U+FFFD (octets
    inconnus), un balayage du vocabulaire est fait, compté."""

    def __init__(self, texte: str, voc: Vocabulaire):
        self.texte, self.voc = texte, voc
        self.fffd = texte.count(FFFD)

    @staticmethod
    def initial() -> tuple[int, bytes]:
        return (0, b"")

    def avancer(self, etat, i: int):
        """État après le jeton i, ou None s'il est incompatible avec le texte."""
        b = self.voc.octets[i]
        if b is None:
            return etat
        idx, P = etat
        dec = codecs.getincrementaldecoder("utf-8")("replace")
        sortie = dec.decode(P + b, final=False)
        P2 = dec.getstate()[0]
        t = self.texte
        if t[idx:idx + len(sortie)] != sortie:
            return None
        idx2 = idx + len(sortie)
        if P2:
            if idx2 >= len(t):
                return None
            c = t[idx2]
            ce = c.encode("utf-8")
            if c != FFFD and not (ce.startswith(P2) and len(ce) > len(P2)):
                return None
        return (idx2, P2)

    def fini(self, etat) -> bool:
        idx, P = etat
        if not P:
            return idx == len(self.texte)
        return P.decode("utf-8", "replace") == self.texte[idx:]

    def _attendu(self, etat):
        idx, P = etat
        t, m = self.texte, self.voc.maxlen
        j = t.find(FFFD, idx)
        if P:
            if idx >= len(t):
                return None
            if t[idx] == FFFD:
                return b"", True
        borne = len(t) if j < 0 else j
        seg = t[idx:min(borne, idx + m)].encode("utf-8")
        if P:
            if not seg.startswith(P):
                return None
            seg = seg[len(P):]
        atteint = j >= 0 and j <= idx + m and len(seg) < m
        return seg, atteint

    def recherche(self, etat) -> tuple[list[int], bool, bool]:
        """(jetons ordinaires compatibles, triés ; **pas compté** dans `balayages_max` ; balayage complet).

        Pas compté (unité de `balayages_max`, B-2 de la lecture neuve) : la recherche de candidats couvre des octets
        inconnus, c'est-à-dire que les octets connus E s'arrêtent sur un U+FFFD à portée et que `commencant_par(E)` (les
        jetons qui prolongent E au-delà, dans les octets que recouvre le U+FFFD) est non vide ; un pas simplement proche
        d'un U+FFFD, dont aucun jeton ne prolonge les octets connus, n'est pas compté. Balayage complet : E vide (le
        U+FFFD est le caractère courant), tout le vocabulaire est examiné ; c'est un cas particulier du pas compté,
        rapporté à part."""
        r = self._attendu(etat)
        if r is None:
            return [], False, False
        E, atteint = r
        c = self.voc.prefixes(E)
        etendus = self.voc.commencant_par(E) if atteint else []
        c = [i for i in set(c + etendus) if self.avancer(etat, i) is not None]
        return sorted(c), bool(etendus), bool(etendus) and not E

    def candidats(self, etat) -> tuple[list[int], bool]:
        """(jetons ordinaires compatibles, triés ; pas compté dans `balayages_max`) : voir `recherche`."""
        c, compte, _ = self.recherche(etat)
        return c, compte

    def reste(self, etat) -> tuple[bytes, str]:
        """(octets qui complètent le caractère en attente, texte qui suit) : base du découpage deviné."""
        idx, P = etat
        t = self.texte
        if P and idx < len(t) and t[idx] != FFFD:
            return t[idx].encode("utf-8")[len(P):], t[idx + 1:]
        if P and idx < len(t):
            return b"", t[idx + 1:]
        return b"", t[idx:]


def deviner(cible: Cible, etat, voc: Vocabulaire, tok, restants: int, a_fin: int, fin_defaut: int) -> list[int]:
    """Découpage courant du reste : octets du caractère en attente un par un, puis découpage canonique du texte restant
    (`tok`, sans jetons spéciaux), puis le jeton de fin par défaut ; tronqué pour que la dernière ligne de logits prédise
    au plus le dernier pas."""
    complete, suite = cible.reste(etat)
    ids = [voc.par_octets[bytes([x])] for x in complete if bytes([x]) in voc.par_octets]
    if suite:
        ids += [int(x) for x in tok(suite, add_special_tokens=False)["input_ids"]]
    if a_fin:
        ids.append(int(fin_defaut))
    return ids[:max(0, int(restants) - 1)]


# --------------------------------------------------------------------------------------------------------------------
# Passe forcée et choix contraint


class Moteur:
    """Passe avant sans cache sur une seule séquence (positions explicites, masque plein, sans remplissage) ; logits
    des k dernières positions, en float32 (comme P3, qui passait les logits du modèle en float32 avant le tirage).

    `passe` rend aussi, ligne par ligne, le choix non contraint (argmax de softmax(logits / température) / q) et sa marge
    en log, calculés sur l'appareil du modèle ; `resoudre_action` ne s'en sert pas : il refait, pour chaque ligne lue, le
    calcul de P3 tel quel sur processeur en float32 (`probabilites`), d'où il tire le choix contraint, le choix non
    contraint, la marge, `p_k` et l'argmax de p (C-7). Rendu gardé pour les modules qui l'appellent."""

    def __init__(self, modele):
        self.modele = modele
        self.appareil = next(modele.parameters()).device
        self.V = int(modele.config.vocab_size)
        self.passes = 0
        self.jetons = 0

    def logits(self, ids: list[int], k: int) -> torch.Tensor:
        """(k, V) en float32, sur l'appareil du modèle."""
        x = torch.tensor([ids], dtype=torch.long, device=self.appareil)
        with torch.no_grad():
            sortie = self.modele(input_ids=x, attention_mask=torch.ones_like(x),
                                 position_ids=torch.arange(len(ids), device=self.appareil)[None], use_cache=False,
                                 logits_to_keep=int(k))
        return sortie.logits[0].to(torch.float32)

    def passe(self, ids: list[int], k: int, Q: torch.Tensor, temperature: float):
        """(logits (k, V) float32 sur processeur, choix non contraints, marges en log) ; Q : (k, V), lignes des pas."""
        L = self.logits(ids, k)
        if tuple(L.shape) != (int(k), self.V) or tuple(Q.shape) != (int(k), self.V):
            raise GardeArret(f"logits de forme {tuple(L.shape)}, tirages {tuple(Q.shape)} ≠ ({k}, {self.V})")
        with torch.no_grad():
            R = torch.softmax(L / temperature, dim=-1) / Q.to(L.device)
            top = torch.topk(R, 2, dim=-1)
            nc = torch.argmax(R, dim=-1)
            v = top.values.double()
            marge = torch.where(v[:, 1] > 0, torch.log(v[:, 0]) - torch.log(v[:, 1]),
                                torch.full_like(v[:, 0], math.inf))
        self.passes += 1
        self.jetons += len(ids)
        return L.to("cpu"), [int(x) for x in nc.to("cpu")], [float(x) for x in marge.to("cpu")]


def probabilites(logits_ligne: torch.Tensor, temperature: float) -> torch.Tensor:
    """p = softmax(logits / température) d'une ligne (V,), en float32 sur processeur : l'opération même de P3
    (`generer_lot` : `torch.softmax(logits[r] / T, dim=-1)` sur une ligne de logits float32 sur processeur). Garde : une
    ligne (V,) float32 sur processeur, sinon arrêt (aucune conversion silencieuse)."""
    if logits_ligne.dim() != 1 or logits_ligne.dtype != torch.float32 or logits_ligne.device.type != "cpu":
        raise GardeArret(f"logits {tuple(logits_ligne.shape)} {logits_ligne.dtype} sur {logits_ligne.device} : une ligne "
                         "(V,) float32 sur processeur attendue, comme P3")
    with torch.no_grad():
        return torch.softmax(logits_ligne / temperature, dim=-1)


def scores_contraints(p: torch.Tensor, q_ligne: torch.Tensor, ordre: list[int]) -> torch.Tensor:
    """Score du choix contraint sur les candidats `ordre` (triés) : log p − log q en double, à partir de p en float32
    (`probabilites`) ; même ordre que p / q en arithmétique exacte ; argmax au premier maximum (plus petit identifiant à
    égalité exacte, y compris deux p arrondis au même float32). Un p nul en float32 donne −∞ (jamais tiré par P3)."""
    ct = torch.tensor(ordre, dtype=torch.long)
    with torch.no_grad():
        return torch.log(p[ct].double()) - torch.log(q_ligne[ct].double())


@dataclass
class Reglages:
    temperature: float = 1.0
    max_nouveaux: int = 400
    seuil_ecart: float = 0.5
    quasi_egalites_max: int = 12
    bascules_max: int = 2
    combinaisons_max: int = 80
    balayages_max: int = 64          # par U+FFFD de l'épisode (unité : `Cible.recherche`)
    echeance: float | None = None
    duree_episode_s: float | None = None


@dataclass
class Compteurs:
    """Compteurs d'un essai. `balayages` : pas comptés (`Cible.recherche`) ; `balayages_complets` : ceux où tout le
    vocabulaire est examiné ; `plafond_balayages` : plafond de l'essai (`balayages_max` × U+FFFD de l'épisode, posé par
    `resoudre_avec_repli`) ; None : plafond de l'action seule (`balayages_max` × U+FFFD de son texte)."""
    balayages: int = 0
    passes: int = 0
    balayages_complets: int = 0
    plafond_balayages: int | None = None


def compter_balayage(compteurs: Compteurs, reglages: Reglages, fffd_action: int, complet: bool, t: int, s: int) -> None:
    """Compte un pas de recherche sur octets inconnus ; au-delà du plafond, `NonResolu` (cause
    `CAUSE_BUDGET_BALAYAGES`)."""
    compteurs.balayages += 1
    compteurs.balayages_complets += int(bool(complet))
    plafond = compteurs.plafond_balayages
    if plafond is None:
        plafond = int(reglages.balayages_max) * int(fffd_action)
    if compteurs.balayages > plafond:
        raise NonResolu(f"{CAUSE_BUDGET_BALAYAGES} ({compteurs.balayages} pas de recherche sur octets inconnus > plafond "
                        f"{plafond} = {reglages.balayages_max} par U+FFFD ; pas {t}, jeton {s})")


def resoudre_action(moteur, voc: Vocabulaire, tok, ctx: list[int], texte: str, n: int, a_fin: int, Q: torch.Tensor,
                    fin_defaut: int, reglages: Reglages, t: int = 0, forcages: dict | None = None,
                    pas: list | None = None, compteurs: Compteurs | None = None) -> list[int]:
    """Identifiants d'une action : n jetons, le dernier parmi les fins si `a_fin`. `pas` reçoit, par jeton, (t, s, choix,
    non contraint, candidats, écart, second, marge, pas compté (recherche sur octets inconnus), p_k du choix, argmax de
    p). Lève `Contradiction` (essai à rejeter), `NonResolu` (budget de balayages dépassé) ou `DureeEpuisee` (échéance
    `reglages.echeance` passée)."""
    cible = Cible(texte, voc)
    forcages = forcages or {}
    compteurs = compteurs if compteurs is not None else Compteurs()
    if a_fin not in (0, 1) or n < a_fin or n > reglages.max_nouveaux:
        raise Contradiction(t, 0, f"longueurs incohérentes (jetons {n}, fin {a_fin}, max {reglages.max_nouveaux})")
    if a_fin == 0 and n != reglages.max_nouveaux:
        raise Contradiction(t, 0, f"action sans jeton de fin de {n} jetons ≠ max_nouveaux {reglages.max_nouveaux}")
    if tuple(Q.shape) != (n, voc.V):
        raise GardeArret(f"tirages de forme {tuple(Q.shape)} ≠ ({n}, {voc.V})")
    etat = cible.initial()
    choisis: list[int] = []
    while len(choisis) < n:
        exiger_sans_signal(f"résolution, pas {t}, jeton {len(choisis)}")
        if reglages.echeance is not None and horloge() > reglages.echeance:
            raise DureeEpuisee(f"budget épuisé (pas {t}, jeton {len(choisis)})")
        s0 = len(choisis)
        devine = deviner(cible, etat, voc, tok, n - s0, a_fin, fin_defaut)
        k_lignes = len(devine) + 1
        L, _nc, _marges = moteur.passe(ctx + choisis + devine, k_lignes, Q[s0:s0 + k_lignes], reglages.temperature)
        compteurs.passes += 1
        for j in range(len(devine) + 1):
            s = s0 + j
            if a_fin and s == n - 1:
                if not cible.fini(etat):
                    raise Contradiction(t, s, "octets du texte restants au jeton de fin")
                cands, balayage = voc.fins, False
            else:
                cands, balayage, complet = cible.recherche(etat)
                if balayage:
                    compter_balayage(compteurs, reglages, cible.fffd, complet, t, s)
                cands = cands + voc.speciaux_non_fins
            if not cands:
                raise Contradiction(t, s, "aucun jeton compatible avec le texte")
            # choix contraint (C-7) : p = softmax(logits / T) en float32 sur processeur, comme P3, puis argmax de
            # log p − log q en double sur les candidats (même ordre que p / q ; égalité exacte : plus petit identifiant)
            p = probabilites(L[j], reglages.temperature)
            ordre = sorted(cands)
            sc = scores_contraints(p, Q[s], ordre)
            k = int(torch.argmax(sc))
            choix = ordre[k]
            if (t, s) in forcages:
                choix = int(forcages[(t, s)])
                if choix not in set(ordre):
                    raise Contradiction(t, s, f"jeton forcé {choix} hors des candidats")
                k = ordre.index(choix)
            if not math.isfinite(float(sc[k])):
                raise Contradiction(t, s, f"jeton retenu {choix} de probabilité nulle en float32 (jamais tiré par P3)")
            ecart, second = math.inf, -1
            if len(ordre) > 1:
                autres = sc.clone()
                autres[k] = -math.inf
                k2 = int(torch.argmax(autres))
                ecart, second = float(sc[k] - autres[k2]), ordre[k2]
            # choix non contraint et marge : l'opération même de P3 (argmax de p / q en float32 sur processeur)
            with torch.no_grad():
                R = p / Q[s]
                non_contraint = int(torch.argmax(R))
                v2 = torch.topk(R, 2).values.double()
                marge = float(torch.log(v2[0]) - torch.log(v2[1])) if float(v2[1]) > 0 else math.inf
                p_k, argmax_p = float(p[choix]), int(torch.argmax(p))
            if pas is not None:
                pas.append((t, s, choix, non_contraint, len(ordre), ecart, second, marge, balayage, p_k, argmax_p))
            choisis.append(choix)
            if not (a_fin and s == n - 1):
                etat = cible.avancer(etat, choix)
                if etat is None:
                    raise Contradiction(t, s, "jeton choisi incompatible (état)")
            if s == n - 1 or j >= len(devine) or choix != devine[j]:
                break
    if not a_fin and not cible.fini(etat):
        raise Contradiction(t, n - 1, "octets du texte restants après le dernier jeton")
    return choisis


def transcription(fmt, env, T: int, textes: list[str], ids_par_action: list[list[int]], jetons=None, jetons_notes=None,
                  bornes: bool = False) -> dict:
    """Transcription de l'épisode refaite exactement comme le harnais (`jouer_episodes`, N = 1) à partir des identifiants
    de chaque action : ouverture au pas 0, puis contexte = transcription + tour ; transcription = contexte + action +
    clôture ; observations rejouées depuis le journal des textes. Forme de `reconstruire_episode` (actions : début,
    fin des jetons notés, identifiants, texte, pas, conforme, bornes)."""
    from ..premier_test_ia.conditions import bornes_champs

    ids: list[int] = []
    journal: list[tuple[int, int, str]] = []
    actions = []
    debut = None
    for t in range(T):
        obs = env.observation(0, t, journal)
        if t == 0:
            debut = (env.consigne_privee(0), obs)
            ctx = fmt.ouverture(*debut)
        else:
            ctx = ids + fmt.tour(debut, obs)
        nv = [int(x) for x in ids_par_action[t]]
        a_fin = (int(jetons[t]) - int(jetons_notes[t])) if jetons is not None else int(bool(nv) and nv[-1] in fmt.fins)
        notes = nv[:len(nv) - a_fin]
        a = {"debut": len(ctx), "fin": len(ctx) + len(notes), "conforme": True, "nv": nv, "texte": textes[t], "pas": t}
        if bornes:
            a["bornes"] = bornes_champs(fmt.tok, notes, textes[t]) if notes else {"lisibles": False}
        actions.append(a)
        ids = ctx + nv + fmt.cloture(debut, nv)
        journal.append((0, t, textes[t]))
    return {"ids": ids, "actions": actions}


def _contexte(fmt, env, journal, ids_tr, debut, t):
    obs = env.observation(0, t, journal)
    if t == 0:
        debut = (env.consigne_privee(0), obs)
        return fmt.ouverture(*debut), debut
    return ids_tr + fmt.tour(debut, obs), debut


def rejouer_episode(moteur, voc, fmt, env, identifiant: str, T: int, textes, jetons, jetons_notes, Qs, reglages,
                    forcages=None, prefixe=None, pas=None, compteurs=None) -> tuple[dict, list[list[int]]]:
    """Un essai : identifiants de chaque action dans l'ordre, chaque contexte construit sur les précédents ; `prefixe` :
    identifiants déjà retrouvés des premières actions (réutilisés tels quels, mêmes contextes). Rend (reconstruction,
    identifiants par action). Lève `Contradiction` ou `NonResolu`."""
    ids_tr: list[int] = []
    journal: list[tuple[int, int, str]] = []
    debut = None
    trouves: list[list[int]] = []
    fin_defaut = None
    for t in range(T):
        ctx, debut = _contexte(fmt, env, journal, ids_tr, debut, t)
        if fin_defaut is None:
            fin_defaut = fmt._pieces(debut)["cloture"][0] if fmt.nom == "chat" else min(fmt.fins)
        a_fin = int(jetons[t]) - int(jetons_notes[t])
        if prefixe is not None and t < len(prefixe):
            nv = list(prefixe[t])
        else:
            nv = resoudre_action(moteur, voc, fmt.tok, ctx, textes[t], int(jetons[t]), a_fin, Qs[t], fin_defaut,
                                 reglages, t, forcages, pas, compteurs)
        if fmt.tok.decode(nv, skip_special_tokens=True) != textes[t]:
            raise Contradiction(t, len(nv), "texte décodé ≠ texte stocké")
        if any(x in fmt.fins for x in nv[:len(nv) - 1]) or bool(nv and nv[-1] in fmt.fins) != bool(a_fin):
            raise Contradiction(t, len(nv), "jeton de fin mal placé")
        trouves.append(nv)
        ids_tr = ctx + nv + fmt.cloture(debut, nv)
        journal.append((0, t, textes[t]))
    return transcription(fmt, env, T, textes, trouves, jetons, jetons_notes), trouves


def echeance_episode(reglages: Reglages, depart: float) -> float | None:
    """Échéance d'un épisode : la plus proche de l'échéance de l'étape et de `depart + duree_episode_s`."""
    bornes = [x for x in (reglages.echeance,
                          None if reglages.duree_episode_s is None else depart + float(reglages.duree_episode_s))
              if x is not None]
    return min(bornes) if bornes else None


def quasi_egalites(journal: list, seuil: float, n_max: int, apres: tuple[int, int] = (-1, -1)) -> list:
    """Quasi-égalités d'un journal de pas : second candidat présent, écart sous `seuil`, position (pas, rang) strictement
    après `apres` ; les plus fragiles d'abord (écart, puis position), au plus `n_max`."""
    q = sorted((x for x in journal if x[6] >= 0 and x[5] < seuil and (x[0], x[1]) > tuple(apres)),
               key=lambda x: (x[5], x[0], x[1]))
    return q[:int(n_max)]


def resoudre_avec_repli(moteur, voc, fmt, fabrique_env, identifiant: str, T: int, textes, jetons, jetons_notes, Qs,
                        empreinte_cible: str, reglages: Reglages, combinaisons_max: int | None = None) -> dict:
    """Essai direct, puis repli écrit itératif (voir le module) ; arbitre : `empreinte_cible`. Budget de l'épisode
    (`echeance_episode`) : épuisé, l'épisode finit « non résolu », cause « durée : … », `duree_epuisee` vrai (jamais une
    exception : l'étape continue). Rend aussi `repli` : rejeux par niveau et par issue."""
    depart = horloge()
    cmax = reglages.combinaisons_max if combinaisons_max is None else int(combinaisons_max)
    reg = replace(reglages, echeance=echeance_episode(reglages, depart))
    sortie = {"episode": identifiant, "fffd": sum(x.count(FFFD) for x in textes), "statut": "non_resolu", "voie": None,
              "cause": None, "forcages": [], "combinaisons_essayees": 0, "ids": None, "ids_directs": None,
              "empreinte": None, "empreinte_cible": empreinte_cible, "duree_epuisee": False}
    pas: list = []
    plafond = int(reg.balayages_max) * int(sortie["fffd"])
    sortie["plafond_balayages"] = plafond
    compteurs = Compteurs(plafond_balayages=plafond)
    trouves_directs: list = []

    def essai(forcages, prefixe, journal_pas, cpt):
        rec, trouves = rejouer_episode(moteur, voc, fmt, fabrique_env(), identifiant, T, textes, jetons, jetons_notes,
                                       Qs, reg, forcages, prefixe, journal_pas, cpt)
        return rec, trouves, empreinte_trajectoire(episode_harnais(identifiant, T, rec))

    def finir(**k):
        sortie.update(k)
        sortie["duree_s"] = round(horloge() - depart, 2)
        return sortie

    try:
        rec, trouves, emp = essai(None, None, pas, compteurs)
        trouves_directs = trouves
        sortie["empreinte"] = emp
        if emp == empreinte_cible:
            sortie.update(statut="resolu", voie="directe", ids=trouves)
        else:
            sortie["cause"] = "empreinte de P3 non retrouvée à l'essai direct"
    except Contradiction as c:
        sortie["cause"] = f"contradiction à l'essai direct ({c})"
    except NonResolu as c:
        return finir(cause=str(c), pas=pas, balayages=compteurs.balayages, passes=compteurs.passes,
                     balayages_complets=compteurs.balayages_complets)
    except DureeEpuisee as c:
        sortie["duree_epuisee"] = True
        sortie["cause"] = f"durée : {c} à l'essai direct"
    # identifiants de l'essai direct, action par action (partiels en cas de contradiction) : pour la mesure à l'aveugle
    par_action: dict[int, list[int]] = {}
    for (t, s, c, *_r) in pas:
        par_action.setdefault(t, []).append(c)
    sortie["ids_directs"] = trouves_directs or [par_action[t] for t in sorted(par_action)]
    sortie.update(pas=pas, pas_direct=pas, balayages=compteurs.balayages, passes=compteurs.passes,
                  balayages_complets=compteurs.balayages_complets)
    if sortie["statut"] == "resolu" or sortie["duree_epuisee"]:
        return finir()
    quasi = quasi_egalites(pas, reg.seuil_ecart, reg.quasi_egalites_max)
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
            if reg.echeance is not None and horloge() > reg.echeance:
                sortie["duree_epuisee"] = True
                break
            essayees += 1
            par_niveau[str(taille)] = par_niveau.get(str(taille), 0) + 1
            forcages = {(x[0], x[1]): x[6] for x in combo}
            t0 = combo[0][0]
            prefixe = [par_action[t] for t in range(t0)]
            journal_pas: list = [x for x in pas if x[0] < t0]
            cpt = Compteurs(plafond_balayages=plafond)
            issue = "empreinte_differente"
            try:
                rec, trouves, emp = essai(forcages, prefixe, journal_pas, cpt)
            except Contradiction:
                issue = "contradiction"
            except NonResolu:
                issue = "non_resolu"
            except DureeEpuisee:
                sortie["duree_epuisee"] = True
                break
            if issue == "empreinte_differente" and emp == empreinte_cible:
                sortie["repli"] = {"par_niveau": par_niveau, "issues": issues}
                return finir(statut="resolu", voie="repli", ids=trouves, empreinte=emp, cause=None, pas=journal_pas,
                             forcages=[{"pas": x[0], "rang": x[1], "jeton": x[6], "ecart": x[5]} for x in combo],
                             combinaisons_essayees=essayees)
            issues[issue] = issues.get(issue, 0) + 1
            if taille < reg.bascules_max:
                # frontière enrichie : quasi-égalités du rejeu basculé (journal partiel compris), après sa dernière bascule
                for y in quasi_egalites(journal_pas, reg.seuil_ecart, reg.quasi_egalites_max, (combo[-1][0], combo[-1][1])):
                    suivante.append((cout + y[5], combo + (y,)))
        if sortie["duree_epuisee"] or essayees >= cmax:
            break
        frontiere = suivante
    sortie["repli"] = {"par_niveau": par_niveau, "issues": issues}
    sortie["combinaisons_essayees"] = essayees
    if sortie["duree_epuisee"]:
        return finir(cause=f"durée : budget de l'épisode épuisé pendant le repli ({sortie['cause']} ; {essayees} "
                           f"combinaison(s) essayée(s))")
    return finir(cause=f"{sortie['cause']} ; repli itératif : {len(quasi)} quasi-égalité(s) directe(s) sous "
                       f"{reg.seuil_ecart}, {essayees} combinaison(s) essayée(s) ({par_niveau}), aucune ne redonne "
                       f"l'empreinte")


def accord_non_contraint(pas: list, verite: list[list[int]] | None = None) -> float | None:
    """Part des pas où le choix non contraint égale le choix retenu (ou le jeton vrai, si `verite` est donnée)."""
    if not pas:
        return None
    if verite is None:
        return float(np.mean([x[3] == x[2] for x in pas]))
    n = ok = 0
    for x in pas:
        if x[0] < len(verite) and x[1] < len(verite[x[0]]):
            n += 1
            ok += x[3] == verite[x[0]][x[1]]
    return ok / n if n else None


def mesures_accord(pas: list) -> dict:
    """Mesures d'un épisode (résolu ou non : C-5, I-2, I-4, I-D), sur ses pas consignés (tuples de `resoudre_action`),
    contre le **jeton retenu** (le jeton de P3 quand l'épisode est résolu) : `accord` = part des pas où le choix non
    contraint (argmax de p / q sur tout le vocabulaire) égale le jeton retenu ; `attendu_graine_independante` = moyenne,
    sur les mêmes pas, de p_k, probabilité du jeton retenu sous la passe (pour un tirage exponentiel indépendant,
    P(argmax(p / q') = k) = p_k exactement) ; pas informatifs = pas où le jeton retenu n'est pas l'argmax de p (une
    graine indépendante y donne au plus 0,5) : leur nombre, l'accord et l'accord attendu sur eux. Calculé sur la même
    passe, sans dépense. Comptes entiers rendus pour l'agrégation."""
    n = len(pas)
    ok = sum(1 for x in pas if x[3] == x[2])
    somme_pk = float(sum(x[9] for x in pas))
    inf = [x for x in pas if x[2] != x[10]]
    ok_inf = sum(1 for x in inf if x[3] == x[2])
    somme_pk_inf = float(sum(x[9] for x in inf))
    return {"pas": n, "accords": ok, "accord": ok / n if n else None,
            "attendu_graine_independante": somme_pk / n if n else None, "somme_p_k": somme_pk,
            "pas_informatifs": len(inf), "accords_informatifs": ok_inf,
            "accord_informatif": ok_inf / len(inf) if inf else None,
            "attendu_informatif": somme_pk_inf / len(inf) if inf else None, "somme_p_k_informatifs": somme_pk_inf}


def agreger_accords(par_episode: dict) -> dict:
    """Agrégats sur les épisodes (`mesures_accord` de chacun) : accord moyen et minimum par épisode (épisodes à pas
    consignés), accord attendu sous graine indépendante moyen par épisode et sur les pas réunis, pas informatifs réunis
    et leur accord."""
    m = [x for x in par_episode.values() if x["pas"]]
    n = sum(x["pas"] for x in m)
    n_inf = sum(x["pas_informatifs"] for x in m)
    return {"episodes_mesures": len(m), "episodes_sans_pas": sorted(e for e, x in par_episode.items() if not x["pas"]),
            "pas": n, "accord_moyen_par_episode": float(np.mean([x["accord"] for x in m])) if m else None,
            "accord_min_par_episode": min((x["accord"] for x in m), default=None),
            "accord_sur_les_pas": sum(x["accords"] for x in m) / n if n else None,
            "attendu_graine_independante_moyen_par_episode":
                float(np.mean([x["attendu_graine_independante"] for x in m])) if m else None,
            "attendu_graine_independante_sur_les_pas": sum(x["somme_p_k"] for x in m) / n if n else None,
            "pas_informatifs": n_inf,
            "accord_informatif": sum(x["accords_informatifs"] for x in m) / n_inf if n_inf else None,
            "attendu_informatif": sum(x["somme_p_k_informatifs"] for x in m) / n_inf if n_inf else None}


def exiger_regle_validation(regle) -> dict:
    """Forme de `regle_validation` (configuration) : exactement les clés `CLES_REGLE_VALIDATION` ; trois seuils d'accord
    dans [0, 1], un nombre minimal de pas informatifs entier ≥ 0. Arrêt sinon (aucun défaut silencieux)."""
    if not isinstance(regle, dict) or set(regle) != set(CLES_REGLE_VALIDATION):
        raise GardeArret(f"regle_validation : clés {sorted(CLES_REGLE_VALIDATION)} exactement attendues, "
                         f"{sorted(regle) if isinstance(regle, dict) else regle!r} reçues")
    for k in ("accord_moyen_min", "accord_episode_min", "accord_informatif_min"):
        v = regle[k]
        if isinstance(v, bool) or not isinstance(v, (int, float)) or not 0 <= v <= 1:
            raise GardeArret(f"regle_validation.{k} = {v!r} : nombre dans [0, 1] attendu")
    v = regle["pas_informatifs_min"]
    if isinstance(v, bool) or not isinstance(v, int) or v < 0:
        raise GardeArret(f"regle_validation.pas_informatifs_min = {v!r} : entier ≥ 0 attendu")
    return regle


def lire_validation(empreintes_retrouvees: int, episodes: int, accords: dict, regle: dict) -> dict:
    """Règle gelée de lecture de la validation (C-3, R-01), appliquée par le code, écrite au résultat avant toute
    lecture humaine. `accords` : `agreger_accords` ; `regle` : `regle_validation` de la configuration.
    - « méthode non transposée » : moins de `episodes` empreintes de P3 retrouvées (ou aucun épisode) ;
    - « graines validées » : toutes retrouvées, et accord moyen par épisode ≥ `accord_moyen_min`, minimum par épisode
      ≥ `accord_episode_min`, au moins `pas_informatifs_min` pas informatifs, accord sur eux ≥ `accord_informatif_min` ;
    - « méthode transposée, graines non validées » : toutes retrouvées, une condition d'accord au moins manquée (une
      mesure absente compte comme manquée).
    Conséquences (`declarer`) : la résolution part sous les trois classes ; ses « résolus » sont des preuves sous les
    trois ; « non inversible » n'est déclarable que sous « graines validées »."""
    exiger_regle_validation(regle)

    def au_moins(x, seuil):
        return x is not None and x >= seuil

    conditions = {
        "accord_moyen": au_moins(accords.get("accord_moyen_par_episode"), regle["accord_moyen_min"]),
        "accord_episode": au_moins(accords.get("accord_min_par_episode"), regle["accord_episode_min"]),
        "pas_informatifs": au_moins(accords.get("pas_informatifs"), regle["pas_informatifs_min"]),
        "accord_informatif": au_moins(accords.get("accord_informatif"), regle["accord_informatif_min"])}
    transposee = int(episodes) > 0 and int(empreintes_retrouvees) == int(episodes)
    if not transposee:
        classe = CLASSES_VALIDATION[2]
    elif all(conditions.values()):
        classe = CLASSES_VALIDATION[0]
    else:
        classe = CLASSES_VALIDATION[1]
    return {"classe": classe, "empreintes_retrouvees": int(empreintes_retrouvees), "episodes": int(episodes),
            "conditions": conditions, "regle": dict(regle),
            "mesures": {k: accords.get(k) for k in ("accord_moyen_par_episode", "accord_min_par_episode",
                                                    "pas_informatifs", "accord_informatif",
                                                    "attendu_graine_independante_moyen_par_episode",
                                                    "attendu_informatif")}}


def declarer(statut: str, cause: str | None, classe: str) -> str:
    """Déclaration d'un épisode de la résolution, selon la classe de la validation (C-3 (4), I-3, R-09) : résolu (sous
    les trois classes) ; cause « budget de balayages dépassé » sous « graines validées » : non inversible déclaré par la
    méthode (budget de recherche dépassé, non preuve d'impossibilité ; règle B) ; tout autre non résolu sous « graines
    validées » : nœud ; tout non résolu sous une autre classe : « non résolu, graines non validées », nœud."""
    if classe not in CLASSES_VALIDATION:
        raise GardeArret(f"classe de validation {classe!r} inconnue : {CLASSES_VALIDATION} attendues")
    if statut == "resolu":
        return DECLARATIONS["resolu"]
    if classe != CLASSES_VALIDATION[0]:
        return DECLARATIONS["graines_non_validees"]
    if (cause or "").startswith(CAUSE_BUDGET_BALAYAGES):
        return DECLARATIONS["budget"]
    return DECLARATIONS["noeud"]


# --------------------------------------------------------------------------------------------------------------------
# Table version 3 : forme « identifiants »


def entree_identifiants(identifiant: str, empreinte_p3: str, base_nv: list[list[int]], trouves: list[list[int]],
                        resolution: dict | None = None) -> dict:
    """Entrée « identifiants » : les seules actions dont les identifiants retrouvés diffèrent de la reconstruction de
    base (texte retokenisé, fin par défaut), avec les deux suites."""
    actions = [{"pas": t, "canonique": [int(x) for x in b], "p3": [int(x) for x in v]}
               for t, (b, v) in enumerate(zip(base_nv, trouves)) if [int(x) for x in b] != [int(x) for x in v]]
    e = {"episode": identifiant, "methode": METHODE_IDENTIFIANTS, "trajectoire_p3": empreinte_p3, "fins": {},
         "paires": [], "actions": actions}
    if resolution is not None:
        e["resolution_graine"] = resolution
    verifier_forme_v3(e)
    return e


def verifier_forme_v3(e: dict) -> None:
    """Forme d'une entrée de table version 3 : « identifiants » (aucune fin, aucune paire ; au moins une action, pas
    distincts et croissants, deux suites d'entiers différentes) ; autres méthodes : `rt.verifier_forme`, inchangée."""
    if e.get("methode") not in METHODES_V3:
        raise GardeArret(f"table de tokenisation : méthode inconnue {e.get('methode')!r}")
    if e["methode"] != METHODE_IDENTIFIANTS:
        rt.verifier_forme(e)
        return
    acts = e.get("actions")
    if e.get("fins") or e.get("paires") or not isinstance(acts, list) or not acts:
        raise GardeArret(f"table de tokenisation : {e.get('episode')} : forme « identifiants » non conforme")
    pas = []
    for a in acts:
        if not isinstance(a, dict) or set(a) != {"pas", "canonique", "p3"} or isinstance(a["pas"], bool) \
                or not isinstance(a["pas"], int):
            raise GardeArret(f"table de tokenisation : {e.get('episode')} : action mal formée")
        for k in ("canonique", "p3"):
            if not isinstance(a[k], list) or not a[k] or any(isinstance(x, bool) or not isinstance(x, int) for x in a[k]):
                raise GardeArret(f"table de tokenisation : {e.get('episode')} : {k} n'est pas une suite d'entiers")
        if a["canonique"] == a["p3"]:
            raise GardeArret(f"table de tokenisation : {e.get('episode')} : action {a['pas']} sans changement")
        pas.append(a["pas"])
    if pas != sorted(set(pas)) or pas[0] < 0:
        raise GardeArret(f"table de tokenisation : {e.get('episode')} : pas en double ou non croissants")


def appliquer_entree_v3(fmt, env, T, lignes, jetons, jetons_notes, entree: dict, octets=None) -> dict:
    """Reconstruction corrigée selon une entrée de table version 3. Méthodes des versions 1 et 2 :
    `rt.appliquer_entree`, telle quelle. « identifiants » : reconstruction de base, puis, pour chaque action citée,
    identifiants de base = `canonique` (garde), remplacés par `p3` ; transcription refaite comme le harnais ; gardes par
    action : longueur = `jetons`, jeton de fin à la dernière place si et seulement si `jetons − jetons_notes = 1`, aucun
    autre jeton de fin, texte décodé = texte stocké. N'arbitre pas : l'appelant compare l'empreinte."""
    verifier_forme_v3(entree)
    if entree["methode"] != METHODE_IDENTIFIANTS:
        return rt.appliquer_entree(fmt, env, T, lignes, jetons, jetons_notes, entree, octets)
    base = reconstruire_episode(fmt, env, T, lignes, jetons, jetons_notes)
    nvs = [list(a["nv"]) for a in base["actions"]]
    for a in entree["actions"]:
        t = int(a["pas"])
        if not 0 <= t < T:
            raise GardeArret(f"{entree['episode']} : pas {t} hors de l'épisode")
        if [int(x) for x in nvs[t]] != [int(x) for x in a["canonique"]]:
            raise GardeArret(f"{entree['episode']} : identifiants de base du pas {t} ≠ `canonique` de la table")
        nvs[t] = [int(x) for x in a["p3"]]
    fins = {int(x) for x in fmt.fins}
    textes = [x["texte"] for x in lignes]
    for t in range(T):
        nv, a_fin = nvs[t], int(jetons[t]) - int(jetons_notes[t])
        if len(nv) != int(jetons[t]) or a_fin not in (0, 1) or any(x in fins for x in nv[:len(nv) - 1]) \
                or bool(nv and nv[-1] in fins) != bool(a_fin) \
                or fmt.tok.decode(nv, skip_special_tokens=True) != textes[t]:
            raise GardeArret(f"{entree['episode']} : action corrigée non conforme au pas {t} (longueur, fin ou texte)")
    return transcription(fmt, env, T, textes, nvs, jetons, jetons_notes, bornes=True)


def charger_table_v3(chemin, sha_attendue: str | None) -> dict:
    """Table version 3 scellée : empreinte citée, version, méthodes connues, formes conformes, aucun doublon."""
    sha = verifier(chemin)
    if sha_attendue is not None and sha != sha_attendue:
        raise GardeArret(f"table de tokenisation {chemin} : empreinte {sha[:12]} ≠ empreinte citée {sha_attendue[:12]}")
    t = json.loads(Path(chemin).read_text(encoding="utf-8"))
    if t.get("version") != VERSION_TABLE_V3:
        raise GardeArret(f"table de tokenisation : version {t.get('version')!r} ≠ {VERSION_TABLE_V3}")
    vus = set()
    for e in t["episodes"]:
        if e["episode"] in vus:
            raise GardeArret(f"table de tokenisation : épisode {e['episode']} en double")
        vus.add(e["episode"])
        verifier_forme_v3(e)
    return t


def verifier_entrees_v3(entrees, fmt, contexte, fiches: dict) -> int:
    """Chaque correction appliquée par `appliquer_entree_v3` redonne exactement l'empreinte de trajectoire de P3.
    `contexte(e)` rend (environnement neuf, lignes, jetons, jetons_notes, T). Rend le nombre de corrections vérifiées."""
    octets = rt.table_des_octets(fmt.tok)[0]
    n = 0
    for ent in entrees:
        verifier_forme_v3(ent)
        if ent["methode"] == "non_resolu":
            continue
        e = ent["episode"]
        env, L, J, JN, T = contexte(e)
        rec = appliquer_entree_v3(fmt, env, T, L, J, JN, ent, octets)
        if empreinte_trajectoire(episode_harnais(e, T, rec)) != fiches[e]["trajectoire"]:
            raise GardeArret(f"{e} : la correction de la table ({ent['methode']}) ne redonne pas l'empreinte de P3")
        n += 1
    return n


def construire_table_v3(table_v2: dict, sha_v2: str, resultat: dict, sha_resultat: str, base_nv: dict) -> dict:
    """Table version 3 : la table v2, dont chaque épisode « non résolu » que le rejeu à graine a résolu reçoit une entrée
    « identifiants » (`base_nv[e]` : identifiants de la reconstruction de base, par action) ; les entrées corrigées de la
    v2 restent telles quelles (contrôle croisé du rejeu consigné à part) ; les épisodes du résultat absents de la table v2
    sont cités (`resultat_hors_table`), non versés. Gardes : version 2, étape « resolution », mêmes empreintes de P3 ;
    contrôle croisé lu « conforme » (R-11 : une répétabilité en défaut s'audite avant la table) ; lecture de la
    validation présente dans le résultat, **recopiée** dans la table (`lecture_validation`) et, avec la déclaration de
    chaque épisode, dans les entrées nouvelles et dans `declarations` (C-3 (3), I-B)."""
    if table_v2.get("version") != rt.VERSION_TABLE:
        raise GardeArret(f"table v2 attendue, version {table_v2.get('version')!r}")
    if resultat.get("etape") != "resolution":
        raise GardeArret("résultat de l'étape « resolution » attendu")
    if resultat.get("controle_croise_lecture") != "conforme":
        raise GardeArret(f"contrôle croisé lu {resultat.get('controle_croise_lecture')!r}, « conforme » attendu : audit "
                         f"(R4) avant la table v3")
    lv = resultat.get("lecture_validation") or {}
    if lv.get("classe") not in CLASSES_VALIDATION:
        raise GardeArret("résultat de la résolution sans lecture de la validation : la table v3 doit porter sa classe")
    par_res = {x["episode"]: x for x in resultat["episodes"]}
    par_v2 = {x["episode"]: x for x in table_v2["episodes"]}
    episodes = []
    for x in table_v2["episodes"]:
        r = par_res.get(x["episode"])
        if x["methode"] != "non_resolu" or r is None or r["statut"] != "resolu":
            episodes.append(x)
            continue
        if r["empreinte_cible"] != x["trajectoire_p3"]:
            raise GardeArret(f"{x['episode']} : empreinte de P3 du résultat ≠ table v2")
        if r.get("empreinte") != x["trajectoire_p3"]:
            raise GardeArret(f"{x['episode']} : « résolu » sans l'empreinte de P3 recalculée égale (un résolu ne se lit "
                             f"que sur l'égalité d'empreinte)")
        res = {"voie": r["voie"], "forcages": r["forcages"], "resultat_sha256": sha_resultat,
               "classe_validation": lv["classe"], "declaration": r.get("declaration")}
        episodes.append({**entree_identifiants(x["episode"], x["trajectoire_p3"], base_nv[x["episode"]], r["ids"], res),
                         "essais": x.get("essais"), "essais_c6": x.get("essais_c6")})
    # épisodes résolus hors de la table v2 (contrôle croisé sur un épisode identique, par exemple) : consignés, non versés
    hors = sorted(set(par_res) - set(par_v2))
    comptes = {k: v for k, v in table_v2["comptes"].items() if k not in METHODES_V3 and k != "identiques_apres_table"}
    for m in METHODES_V3:
        comptes[m] = sum(1 for x in episodes if x["methode"] == m)
    comptes["identiques_apres_table"] = comptes["identiques_base"] + sum(comptes[m] for m in CORRIGEES_V3)
    meta = {k: v for k, v in table_v2.items() if k not in ("version", "comptes", "episodes")}
    return {**meta, "version": VERSION_TABLE_V3, "regle_graine": REGLE, "table_v2_sha256": sha_v2,
            "resultat_graine_sha256": sha_resultat, "resultat_hors_table": hors, "comptes": comptes,
            "lecture_validation": lv, "declarations": {x["episode"]: x.get("declaration") for x in resultat["episodes"]},
            "episodes": episodes}


# --------------------------------------------------------------------------------------------------------------------
# Pièces de P3, configuration, étapes


def empreinte_config(config: dict) -> str:
    return hashlib.sha256(config_canonique(config)).hexdigest()


def exiger_config(config: dict) -> None:
    manquantes = [k for k in CLES if k not in config]
    if manquantes:
        raise GardeArret(f"configuration de la résolution à graine incomplète : {manquantes}")
    if config["mode"] not in ("reel", "jouet"):
        raise GardeArret(f"mode {config['mode']!r} inconnu")
    entiers = ("T", "max_nouveaux", "fils", "fils_tirages", "episodes_d_avance", "quasi_egalites_max", "bascules_max",
               "combinaisons_max", "combinaisons_max_validation", "balayages_max", "seuil_validation")
    for k in entiers:
        if isinstance(config[k], bool) or not isinstance(config[k], int) or config[k] < 0:
            raise GardeArret(f"{k} = {config[k]!r} : entier positif ou nul attendu")
    if config["T"] < 1 or config["max_nouveaux"] < 1 or config["fils"] < 1 or config["fils_tirages"] < 1:
        raise GardeArret("T, max_nouveaux, fils et fils_tirages : au moins 1")
    if not float(config["temperature"]) > 0:
        raise GardeArret("température nulle : P3 tirait à température 1 (méthode sans objet en décodage glouton)")
    if not float(config["seuil_ecart"]) >= 0 or not float(config["duree_max_s"]) > 0:
        raise GardeArret("seuil_ecart ≥ 0 et duree_max_s > 0 attendus")
    if not isinstance(config["episodes_resolution"], list) or len(set(config["episodes_resolution"])) \
            != len(config["episodes_resolution"]):
        raise GardeArret("episodes_resolution : liste sans doublon attendue")
    if config["mode"] == "reel":
        for k in CLES:
            if k.endswith("_sha256") and not config[k]:
                raise GardeArret(f"mode réel : {k} obligatoire")


def exiger_reglages_execution(config: dict) -> None:
    """Gardes des étapes de ce module (VG-03, VG-04), avant tout chargement : `duree_max_episode_s` présent et positif,
    au plus `duree_max_s` ; `noyau_attention` parmi « defaut » et « math » (toute autre valeur tomberait en silence sur
    le noyau par défaut) ; paires permises en validation (`combinaisons_max_validation` = `combinaisons_max`) ;
    `regle_validation` conforme (`exiger_regle_validation`)."""
    manquantes = [k for k in CLES_EXECUTION if k not in config]
    if manquantes:
        raise GardeArret(f"configuration de la résolution à graine incomplète : {manquantes}")
    d = config["duree_max_episode_s"]
    if isinstance(d, bool) or not isinstance(d, (int, float)) or not d > 0 or d > float(config["duree_max_s"]):
        raise GardeArret(f"duree_max_episode_s = {d!r} : nombre > 0 et ≤ duree_max_s attendu")
    if config["noyau_attention"] not in NOYAUX:
        raise GardeArret(f"noyau_attention = {config['noyau_attention']!r} : {NOYAUX} attendus")
    if config["combinaisons_max_validation"] != config["combinaisons_max"]:
        raise GardeArret("combinaisons_max_validation ≠ combinaisons_max : la validation doit permettre les paires comme "
                         "la résolution")
    exiger_regle_validation(config["regle_validation"])
    episodes_laisses_par_repetition(config)


def episodes_laisses_par_repetition(config: dict) -> list[str]:
    """Répétition jouet du script d'instance seulement : épisodes de `episodes_resolution` que l'étape « resolution »
    laisse « non tentés » (cause « répétition jouet : … », jamais « durée »), pour que l'étape du lot ait une cible.
    Clé `CLE_REPETITION` absente : liste vide. Présente en mode réel (même vide) : arrêt ; en jouet : liste sans
    doublon, incluse dans `episodes_resolution`, sinon arrêt."""
    if CLE_REPETITION not in config:
        return []
    if config.get("mode") != "jouet":
        raise GardeArret(f"{CLE_REPETITION} : clé de la répétition jouet, interdite en mode {config.get('mode')!r}")
    v = config[CLE_REPETITION]
    if not isinstance(v, list) or len(set(v)) != len(v) or not set(v) <= set(config.get("episodes_resolution") or []):
        raise GardeArret(f"{CLE_REPETITION} : liste sans doublon, incluse dans episodes_resolution, attendue")
    return list(v)


def reglages_de(config: dict, echeance: float | None, duree_episode_s: float | None = None) -> Reglages:
    return Reglages(temperature=float(config["temperature"]), max_nouveaux=int(config["max_nouveaux"]),
                    seuil_ecart=float(config["seuil_ecart"]), quasi_egalites_max=int(config["quasi_egalites_max"]),
                    bascules_max=int(config["bascules_max"]), combinaisons_max=int(config["combinaisons_max"]),
                    balayages_max=int(config["balayages_max"]), echeance=echeance,
                    duree_episode_s=None if duree_episode_s is None else float(duree_episode_s))


def exiger_agent_de_p3(agent: dict, manifeste_p3: dict, reel: bool) -> None:
    """L'agent de la configuration est celui de P3 (`CLES_AGENT_P3` : modèle, révision, variables du gabarit, comparés au
    manifeste de P3) ; en mode réel, modèle et révision présents."""
    a3 = (manifeste_p3.get("config") or {}).get("agent") or {}
    differentes = [k for k in CLES_AGENT_P3 if agent.get(k) != a3.get(k)]
    if differentes:
        raise GardeArret(f"agent de la configuration ≠ agent de P3 ({differentes})")
    if reel and not (agent.get("modele") and agent.get("revision")):
        raise GardeArret("mode réel : agent sans modèle ou sans révision")


def exiger_seuil_atteignable(seuil: int, episodes: int) -> None:
    """Avant la boucle (VG-04) : le seuil de lecture de la validation ne dépasse pas le nombre d'épisodes à identifiants
    connus (sinon la configuration est fausse : arrêt avant tout calcul)."""
    if int(seuil) > int(episodes):
        raise GardeArret(f"seuil de validation {seuil} > {episodes} épisodes à identifiants connus")


def exiger_compte_validation(episodes: int, attendu: int) -> None:
    """Avant la boucle (m-3) : la validation porte sur exactement `seuil_validation` épisodes à identifiants connus (147
    en mode réel) ; un autre compte (classement changé, table autre) arrête avant tout calcul."""
    if int(episodes) != int(attendu):
        raise GardeArret(f"validation : {episodes} épisodes à identifiants connus ≠ {attendu} attendus (seuil_validation)")


def exiger_config_citee(texte: str, config: dict, prereg: str = "préenregistrement") -> None:
    """Le texte scellé cite l'empreinte canonique de la configuration (`CONFIG_CITEE`) ; arrêt sinon."""
    if CONFIG_CITEE.format(empreinte_config(config)) not in texte:
        raise GardeArret(f"{prereg} ne cite pas la configuration de la résolution {empreinte_config(config)[:12]}")


def exiger_ouverture(fmt, env, attendu: str | None, reel: bool) -> None:
    """Le texte attendu de l'ouverture (`agent.texte_attendu_ouverture`, obligatoire en mode réel) figure dans
    l'ouverture du gabarit de l'agent (variables du gabarit lues) ; arrêt sinon."""
    if reel and not attendu:
        raise GardeArret("agent : texte attendu dans l'ouverture absent de la configuration")
    if attendu and attendu not in fmt.tok.decode(fmt.ouverture(env.consigne_privee(0), env.observation(0, 0, []))):
        raise GardeArret(f"agent : ouverture sans {attendu!r} (variables du gabarit non lues)")


def _meme_code(racine: Path, commit: str) -> bool:
    import subprocess

    from ..harnais.validation_reelle import CHEMINS_GELES

    if etat_git(racine)["commit"] == commit:
        return True
    r = subprocess.run(["git", "-C", str(racine), "diff", "--quiet", commit, "HEAD", "--", *CHEMINS_GELES],
                       capture_output=True, text=True)
    if r.returncode not in (0, 1):
        raise GardeArret(f"comparaison au commit {commit[:12]} impossible : {r.stderr.strip()}")
    return r.returncode == 0


def executions_anterieures(racine: Path, config: dict, etape: str) -> list[str]:
    """Runs antérieurs du dépôt de la même étape (commande du manifeste), de la même configuration (empreinte canonique)
    et du même code (arbre gelé égal), qui ont laissé une sortie (`diag/<run>/` : résultat de l'étape, `arret.json` ou
    épisodes consignés). Un manifeste illisible arrête (VI-08, R5 : unicité non vérifiable, jamais sauté en silence)."""
    cible = empreinte_config(config)
    commande = f"{COMMANDE} --etape {etape}"
    sortie = []
    for chemin in sorted((Path(racine) / "runs").glob("*/manifeste.json")):
        try:
            brut = json.loads(chemin.read_text(encoding="utf-8"))
        except (OSError, ValueError) as e:
            raise GardeArret(f"R3 : manifeste illisible {chemin} ({e}) : unicité de l'étape non vérifiable")
        if brut.get("commande") != commande or brut.get("config_sha256") != cible:
            continue
        m, _ = lire_manifeste(chemin)
        d = Path(racine) / "diag" / m["run_id"]
        traces = [d / f"resolution-graine-{etape}.json", d / "arret.json", d / f"episodes-{etape}"]
        if any(x.exists() for x in traces) and _meme_code(Path(racine), m["commit"]):
            sortie.append(m["run_id"])
    return sortie


def exiger_execution_unique(racine: Path, config: dict, etape: str, reexecution_essai: bool = False) -> list[str]:
    """R3 (C-3 (5), I-A) : une seule exécution de chaque étape sous une même configuration et un même code ; une sortie
    antérieure de la même étape arrête avant tout calcul (tout essai de plus relève d'un texte neuf, donc d'une autre
    configuration ou d'un autre code). `reexecution_essai` : essais du code seulement, refusé en mode réel ; les runs
    antérieurs sont alors rendus et consignés au résultat."""
    if reexecution_essai and config.get("mode") == "reel":
        raise GardeArret("reexecution_essai interdit en mode réel (R3)")
    anterieurs = executions_anterieures(racine, config, etape)
    if anterieurs and not reexecution_essai:
        raise GardeArret(f"étape {etape} déjà exécutée sous cette configuration et ce code ({anterieurs}) : R3, une seule "
                         f"exécution par étape ; tout essai de plus sous un texte neuf")
    return anterieurs


def environnement_d_execution(reel: bool) -> dict:
    """Versions et carte de l'exécution, pour la comparaison à P3 (`ENVIRONNEMENT_P3`)."""
    env = {"torch": torch.__version__, "cuda": torch.version.cuda, "cudnn": None, "carte": None}
    if reel and torch.cuda.is_available():
        env["cudnn"] = torch.backends.cudnn.version()
        env["carte"] = torch.cuda.get_device_name(0)
    return env


def reserves_environnement(env: dict, reel: bool) -> list[str]:
    """Réserves écrites au résultat (VG-05), sans arrêt : construction de torch pour une autre version de CUDA que P3
    (13.0), autre cuDNN, autre carte. Rien en mode jouet (processeur)."""
    if not reel:
        return []
    r = []
    if env.get("cuda") != ENVIRONNEMENT_P3["cuda"]:
        r.append(f"torch construit pour CUDA {env.get('cuda')!r} ≠ {ENVIRONNEMENT_P3['cuda']} (P3, "
                 f"{ENVIRONNEMENT_P3['torch']}) : noyaux de la carte possiblement autres, arrondis des logits plus "
                 f"éloignés ; l'empreinte de P3 reste seule juge")
    if env.get("cudnn") != ENVIRONNEMENT_P3["cudnn"]:
        r.append(f"cuDNN {env.get('cudnn')!r} ≠ {ENVIRONNEMENT_P3['cudnn']} (P3)")
    if ENVIRONNEMENT_P3["carte"] not in str(env.get("carte") or ""):
        r.append(f"carte {env.get('carte')!r} ≠ {ENVIRONNEMENT_P3['carte']} (P3)")
    return r


def lecture_controle_croise(controle: list[dict]) -> str:
    """Lecture du contrôle croisé (épisodes de la résolution à identifiants déjà connus), à trois valeurs (VG-06) :
    « contraire » si un épisode résolu a des identifiants autres que ceux connus ; sinon « non résolu » si un épisode du
    contrôle n'est pas résolu ; sinon « conforme ». Sans épisode de contrôle : « sans objet »."""
    if not controle:
        return "sans objet"
    if any(c["statut"] == "resolu" and not c["identifiants_egaux"] for c in controle):
        return "contraire"
    if any(c["statut"] != "resolu" for c in controle):
        return "non résolu"
    return "conforme"


def charger_identite_sans_scores(chemin_scores, sha_attendue: str | None) -> dict:
    """Tableaux d'identité, `jetons` et `jetons_notes` du fichier des scores de P3, chargés **clé par clé** (aucun score,
    aucune note lus), avec son empreinte vérifiée."""
    sha = verifier(chemin_scores)
    if sha_attendue is not None and sha != sha_attendue:
        raise GardeArret(f"{chemin_scores} : empreinte {sha[:12]} ≠ empreinte citée {sha_attendue[:12]}")
    cles = (*CLES_IDENTITE, "jetons", "jetons_notes")
    with np.load(chemin_scores, allow_pickle=False) as z:
        manquantes = [k for k in cles if k not in z.files]
        if manquantes:
            raise GardeArret(f"{chemin_scores} : tableaux absents {manquantes}")
        sortie = {k: z[k] for k in cles}
    sortie["sha256"] = sha
    return sortie


@dataclass
class Pieces:
    lignes: list
    identite: dict
    fiches: dict
    taches: dict
    consignes: dict
    guide: str
    manifeste_p3: dict
    table: dict
    par_episode: dict = field(default_factory=dict)


def charger_pieces(config: dict, racine: Path) -> Pieces:
    """Pièces de P3, chacune vérifiée par son empreinte citée (aucun score lu)."""
    from ..environnements.invites import charger_invite
    from ..environnements.pilote_a import charger_taches
    from ..premier_test_ia.conditions import charger_consignes
    from .rejeu_activations_v1 import charger_fiches

    r = Path(racine)
    identite = charger_identite_sans_scores(r / config["chemin_scores"], config["scores_sha256"])
    sha_id = empreinte_identite(identite)
    if config["identite_sha256"] is not None and sha_id != config["identite_sha256"]:
        raise GardeArret(f"identité des actions {sha_id[:12]} ≠ identité citée {config['identite_sha256'][:12]}")
    lignes = charger_textes_alignes(r / config["chemin_textes"], identite, config["textes_sha256"])
    fiches = charger_fiches(r / config["chemin_fiches"], config["fiches_sha256"])
    chemin_t = r / config["chemin_taches"]
    if config["taches_sha256"] is not None and verifier(chemin_t) != config["taches_sha256"]:
        raise GardeArret("tâches : empreinte ≠ empreinte citée")
    taches = {t["identifiant"]: t for t in charger_taches(chemin_t)}
    consignes = charger_consignes(r / config["chemin_consignes"], config["consignes_sha256"])
    m, sha_m = lire_manifeste(r / config["chemin_manifeste_p3"])
    if config["manifeste_p3_sha256"] is not None and sha_m != config["manifeste_p3_sha256"]:
        raise GardeArret(f"manifeste de P3 : empreinte {sha_m[:12]} ≠ empreinte citée")
    if m["run_id"] != config["run_source"]:
        raise GardeArret(f"manifeste du run {m['run_id']} ≠ run source {config['run_source']}")
    exiger_agent_de_p3(config["agent"], m, config["mode"] == "reel")
    for k in ("T", "temperature", "max_nouveaux"):
        if m["config"].get(k) != config[k]:
            raise GardeArret(f"{k} = {config[k]!r} ≠ {m['config'].get(k)!r} dans la configuration de P3")
    if m["config"].get("N", 1) != 1:
        raise GardeArret("P3 à un seul agent (N = 1) attendu")
    table = rt.charger_table(r / config["chemin_table_tokenisation"], config["table_tokenisation_sha256"])
    for k in ("textes_sha256", "fiches_sha256", "scores_sha256"):
        if config[k] is not None and table.get(k) != config[k]:
            raise GardeArret(f"table de tokenisation calculée sur d'autres pièces ({k})")
    par_episode: dict[str, list[int]] = {}
    for i, x in enumerate(lignes):
        par_episode.setdefault(x["episode"], []).append(i)
    T = int(config["T"])
    for e, rs in par_episode.items():
        if len(rs) != T or rs != list(range(rs[0], rs[0] + T)) or [lignes[q]["pas"] for q in rs] != list(range(T)):
            raise GardeArret(f"épisode {e} : actions non contiguës ou pas désordonnés")
        if e not in fiches:
            raise GardeArret(f"épisode {e} absent des fiches de P3")
    return Pieces(lignes, identite, fiches, taches, consignes, charger_invite("H1-classification"), m, table, par_episode)


class EpisodeP3:
    """Accès aux données d'un épisode de P3 : textes, longueurs, graines, environnement neuf à chaque essai."""

    def __init__(self, pieces: Pieces, e: str, T: int):
        self.e, self.T = e, T
        rs = pieces.par_episode[e]
        x0 = pieces.lignes[rs[0]]
        self.lignes = [pieces.lignes[r] for r in rs]
        self.textes = [x["texte"] for x in self.lignes]
        self.jetons = [int(pieces.identite["jetons"][r]) for r in rs]
        self.jetons_notes = [int(pieces.identite["jetons_notes"][r]) for r in rs]
        self.condition, self.tache = x0["condition"], x0["tache"]
        self.graines = graines_p3(pieces.manifeste_p3, self.tache, T)
        self.empreinte = pieces.fiches[e]["trajectoire"]
        self._p = pieces

    def env(self):
        from ..environnements.pilote_a import tache_de
        from ..premier_test_ia.conditions import environnement

        return environnement(self.condition, tache_de(self._p.taches[self.tache]), self.T, self._p.guide,
                             self._p.consignes)


def classer(pieces: Pieces, fmt, T: int) -> dict:
    """Par épisode (processeur) : identifiants de la reconstruction de base, empreinte de base égale à celle de P3 ou
    non, entrée de la table. Sert à choisir les épisodes de l'étape et, après coup seulement, à la comparaison."""
    par_table = {x["episode"]: x for x in pieces.table["episodes"]}
    sortie = {}
    for e in pieces.par_episode:
        ep = EpisodeP3(pieces, e, T)
        rec = reconstruire_episode(fmt, ep.env(), T, ep.lignes, ep.jetons, ep.jetons_notes)
        ident = empreinte_trajectoire(episode_harnais(e, T, rec)) == ep.empreinte
        sortie[e] = {"base_nv": [list(a["nv"]) for a in rec["actions"]], "identique_base": ident,
                     "entree": par_table.get(e)}
    return sortie


def verite(pieces: Pieces, fmt, T: int, classement: dict, e: str) -> list[list[int]] | None:
    """Identifiants connus d'un épisode (reconstruction de base identique, ou correction de la table, revérifiée par
    l'empreinte) ; None si inconnus. Lu après la résolution seulement (mesure à l'aveugle)."""
    c = classement[e]
    if c["identique_base"]:
        return c["base_nv"]
    ent = c["entree"]
    if ent is None or ent["methode"] == "non_resolu":
        return None
    ep = EpisodeP3(pieces, e, T)
    rec = rt.appliquer_entree(fmt, ep.env(), T, ep.lignes, ep.jetons, ep.jetons_notes, ent)
    if empreinte_trajectoire(episode_harnais(e, T, rec)) != ep.empreinte:
        raise GardeArret(f"{e} : la correction de la table ne redonne pas l'empreinte de P3")
    return [list(a["nv"]) for a in rec["actions"]]


def episodes_de_l_etape(etape: str, config: dict, classement: dict) -> list[str]:
    """Validation : épisodes à identifiants connus (base identique ou corrigés par la table), dans l'ordre du run.
    Résolution : `episodes_resolution` de la configuration, chacun présent dans le run."""
    if etape == "validation":
        return [e for e, c in classement.items()
                if c["identique_base"] or (c["entree"] is not None and c["entree"]["methode"] != "non_resolu")]
    manquants = [e for e in config["episodes_resolution"] if e not in classement]
    if manquants or not config["episodes_resolution"]:
        raise GardeArret(f"episodes_resolution vide ou absents du run : {manquants[:3]}")
    return list(config["episodes_resolution"])


def exiger_seuil_validation(trouvees: int, seuil: int, episodes: int) -> None:
    """Garde : au moins `seuil` empreintes de P3 retrouvées sur `episodes` (arrêt sinon). Gardée pour les modules qui
    l'importent ; les étapes de ce module ne s'en servent plus après la boucle (VG-03 : la validation est une mesure
    rapportée) ; avant la boucle, `exiger_seuil_atteignable`."""
    if seuil > episodes:
        raise GardeArret(f"seuil de validation {seuil} > {episodes} épisodes à identifiants connus")
    if trouvees < seuil:
        raise GardeArret(f"validation : {trouvees} empreinte(s) de P3 retrouvée(s) sur {episodes}, sous le seuil de "
                         f"{seuil} : la méthode ne se transpose pas, résolution non lancée")


def exiger_validation(racine: Path, chemin, config: dict) -> dict:
    """Garde d'**ordre** (C-3 (2)) : la résolution exige une validation scellée, rattachée à son manifeste, sans
    `arret.json` dans son dossier, de même configuration et même code, **quelle que soit sa lecture** (la classe n'est
    exigée que présente, parmi les trois, pour être recopiée ; la validation est une mesure, pas un arrêt ; l'ordre
    « validation puis résolution » garde la validation à l'aveugle)."""
    if not chemin:
        raise GardeArret("étape « resolution » sans --validation : la validation à l'aveugle passe d'abord")
    corps = verifier_resultat(racine, chemin)
    m, _ = lire_manifeste(Path(racine) / "runs" / corps["run_id"] / "manifeste.json")
    r = corps["resultat"]
    classe = (r.get("lecture_validation") or {}).get("classe")
    if r.get("etape") != "validation" or r.get("version") != VERSION or classe not in CLASSES_VALIDATION:
        raise GardeArret(f"validation {chemin} : étape {r.get('etape')!r}, version {r.get('version')!r}, classe "
                         f"{classe!r}")
    if (Path(racine) / "diag" / corps["run_id"] / "arret.json").exists():
        raise GardeArret(f"validation {corps['run_id']} arrêtée (arret.json) : résolution non lancée")
    if m["config_sha256"] != empreinte_config(config):
        raise GardeArret("validation faite sous une autre configuration")
    exiger_meme_code(racine, m["commit"])
    return corps


def exiger_meme_code(racine: Path, commit: str) -> None:
    """L'arbre gelé (code, tests, scripts, dépendances ; hors sorties et documents) est, au commit courant, celui du
    commit de la validation (les résultats de la validation, committés entre-temps, sont hors de l'arbre gelé)."""
    import subprocess

    from ..harnais.validation_reelle import CHEMINS_GELES

    if etat_git(racine)["commit"] == commit:
        return
    r = subprocess.run(["git", "-C", str(racine), "diff", "--quiet", commit, "HEAD", "--", *CHEMINS_GELES],
                       capture_output=True, text=True)
    if r.returncode != 0:
        raise GardeArret(f"validation faite sur un autre code (commit {commit[:12]}) : "
                         f"{'arbre gelé modifié' if r.returncode == 1 else r.stderr.strip()}")


def _modele(config: dict, racine: Path, pieces: Pieces):
    from ..environnements.lancer_pilote_a import charger_modele_et_format
    from ..harnais.run_harnais_factice import graine_entiere

    if config["mode"] == "jouet":
        return charger_modele_et_format(config["agent"], "jouet", graine_entiere(pieces.manifeste_p3["graines"]
                                                                                  ["modele-jouet"]))
    return charger_modele_et_format(config["agent"], "reel", 0, hors_ligne=bool(config["hors_ligne"]))


def quantiles(x) -> dict:
    x = np.asarray([v for v in x if np.isfinite(v)], dtype=np.float64)
    if not len(x):
        return {"n": 0}
    q = (0.0, 0.001, 0.01, 0.05, 0.1, 0.5)
    return {"n": int(len(x)), **{f"q{v:g}": float(np.quantile(x, v)) for v in q},
            "sous": {f"{s:g}": int((x < s).sum()) for s in SEUILS_ECART_COMPTES}}


def premier_ecart(ids_directs, verite_ids, pas) -> dict | None:
    """Premier jeton de l'essai direct différent du jeton vrai, avec son écart et sa marge consignés."""
    for t, (a, b) in enumerate(zip(ids_directs or [], verite_ids)):
        for s, (x, y) in enumerate(zip(a, b)):
            if x != y:
                rec = next((p for p in pas if p[0] == t and p[1] == s), None)
                return {"pas": t, "rang": s, "trouve": int(x), "vrai": int(y),
                        "ecart": None if rec is None else rec[5], "marge": None if rec is None else rec[7]}
        if len(a) != len(b):
            return {"pas": t, "rang": min(len(a), len(b)), "longueur": [len(a), len(b)]}
    return None


def consigner_episode(dossier: Path, k: int, r: dict) -> dict:
    """Consigne un épisode traité, aussitôt (VG-01) : `dossier/NNN.json` scellé (statut, cause, identifiants retrouvés,
    empreinte, graines ; sans le journal des pas). Rend la référence citée par `arret.json` en cas d'arrêt."""
    dossier.mkdir(parents=True, exist_ok=True)
    chemin = dossier / f"{k:03d}.json"
    if chemin.exists():
        raise GardeArret(f"{chemin} existe déjà : R12 interdit d'écraser")
    corps = {k2: v for k2, v in r.items() if k2 not in ("pas", "pas_direct")}
    chemin.write_text(json.dumps(corps, indent=1, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")
    sha = sceller(chemin)
    return {"episode": r["episode"], "statut": r["statut"], "fichier": f"{dossier.name}/{chemin.name}", "sha256": sha}


def non_tente(ep: "EpisodeP3", motif: str) -> dict:
    """Épisode non tenté (budget de l'étape épuisé avant lui) : « non résolu », cause « durée : … »."""
    return {"episode": ep.e, "fffd": sum(x.count(FFFD) for x in ep.textes), "statut": "non_resolu", "voie": None,
            "cause": f"durée : {motif}", "forcages": [], "combinaisons_essayees": 0, "ids": None, "ids_directs": None,
            "empreinte": None, "empreinte_cible": ep.empreinte, "duree_epuisee": True, "non_tente": True,
            "balayages": 0, "passes": 0, "duree_s": 0.0}


def _executer(config, racine, run_id, chemin_m, manifeste, pieces, etape, etat, debut, validation=None) -> dict:
    from ..harnais.modeles import regler_determinisme
    from ..harnais.validation_reelle import noyau
    from .rejeu_activations_v1 import progres

    reel = config["mode"] == "reel"
    appareil = "cuda" if reel else "cpu"
    reglages_det = regler_determinisme(config["fils"], appareil)
    T = int(config["T"])
    echeance = debut + float(config["duree_max_s"])
    environnement = environnement_d_execution(reel)
    reserves = reserves_environnement(environnement, reel)
    etat["reserves"] = reserves
    modele, fmt = _modele(config, racine, pieces)
    attendu = config["agent"].get("texte_attendu_ouverture")
    if reel and not attendu:
        raise GardeArret("agent : texte attendu dans l'ouverture absent de la configuration")
    etat["etape"] = "classement"
    classement = classer(pieces, fmt, T)
    episodes = episodes_de_l_etape(etape, config, classement)
    if etape == "validation":
        exiger_seuil_atteignable(int(config["seuil_validation"]), len(episodes))
        exiger_compte_validation(len(episodes), int(config["seuil_validation"]))
    if not episodes:
        raise GardeArret(f"étape {etape} : aucun épisode")
    exiger_ouverture(fmt, EpisodeP3(pieces, episodes[0], T).env(), attendu, reel)
    voc = Vocabulaire(fmt.tok, fmt.fins, int(modele.config.vocab_size))
    etat["equivalence_tirage"] = exiger_equivalence_tirage(voc.V)
    moteur = Moteur(modele)
    reglages = reglages_de(config, echeance, float(config["duree_max_episode_s"]))
    cmax = int(config["combinaisons_max_validation" if etape == "validation" else "combinaisons_max"])
    tirages = Tirages(voc.V, int(config["fils_tirages"]))
    eps = {e: EpisodeP3(pieces, e, T) for e in episodes}
    laisses = set(episodes_laisses_par_repetition(config)) if etape == "resolution" else set()
    dossier = Path(racine) / "diag" / run_id
    dossier_eps = dossier / f"episodes-{etape}"
    resultats, pas_tous, pas_directs = [], [], []
    etat["episodes_consignes"] = []
    etat["etape"] = etape
    progres(etape=etape, episodes=len(episodes))
    try:
        with noyau(config["noyau_attention"]):
            for k, e in enumerate(episodes):
                exiger_sans_signal(f"résolution à graine, épisode {k}")
                ep = eps[e]
                if e in laisses:
                    r = {**non_tente(ep, "sans objet"), "duree_epuisee": False,
                         "cause": "répétition jouet : épisode laissé non tenté par le cœur (artefact de répétition, "
                                  "mode jouet seulement), pour l'étape du lot"}
                elif horloge() > echeance:
                    r = non_tente(ep, f"budget de l'étape ({config['duree_max_s']} s) épuisé avant l'épisode {k}")
                else:
                    for e2 in episodes[k:k + 1 + int(config["episodes_d_avance"])]:
                        tirages.demander(e2, eps[e2].graines, eps[e2].jetons)
                    Qs = tirages.prendre(e)
                    r = resoudre_avec_repli(moteur, voc, fmt, ep.env, e, T, ep.textes, ep.jetons, ep.jetons_notes, Qs,
                                            ep.empreinte, reglages, cmax)
                    del Qs
                r["graines"] = ep.graines
                pas_tous.append(r.pop("pas", []))
                pas_directs.append(r.pop("pas_direct", None) or pas_tous[-1])
                resultats.append(r)
                etat["episodes_consignes"].append(consigner_episode(dossier_eps, k, r))
                etat["episodes_traites"] = k + 1
                if (k + 1) % 10 == 0 or k + 1 == len(episodes):
                    progres(etape=etape, episodes=f"{k + 1}/{len(episodes)}",
                            resolus=sum(x["statut"] == "resolu" for x in resultats), passes=moteur.passes)
    finally:
        tirages.fermer()
    etat["etape"] = "mesures"
    # mesures, après la résolution seulement (à l'aveugle) : comparaison aux identifiants connus
    detail, ecarts, marges_desaccord, erreurs_directes = [], [], [], []
    accords, n_pas, egaux_ep, actions_egales, actions_tot, controle = [], 0, 0, 0, 0, []
    mesures_ep: dict[str, dict] = {}
    for r, pas, pas_d in zip(resultats, pas_tous, pas_directs):
        e = r["episode"]
        v = verite(pieces, fmt, T, classement, e)
        ecarts += [x[5] for x in pas if x[4] > 1]
        marges_desaccord += [x[7] for x in pas if x[3] != x[2]]
        n_pas += len(pas)
        # accord pour tout épisode à pas consignés, résolu ou non (I-4) : contre les identifiants connus s'il y en a,
        # sinon contre le jeton retenu
        acc_v = accord_non_contraint(pas, v) if v is not None else accord_non_contraint(pas)
        if acc_v is not None:
            accords.append(acc_v)
        mesures_ep[e] = mesures_accord(pas)
        d = {k2: r[k2] for k2 in ("episode", "statut", "voie", "cause", "forcages", "combinaisons_essayees", "passes",
                                  "balayages", "balayages_complets", "plafond_balayages", "fffd", "duree_s", "graines",
                                  "empreinte", "duree_epuisee", "repli", "non_tente") if k2 in r}
        d["empreinte_retrouvee"] = r["statut"] == "resolu" and r["empreinte"] == r["empreinte_cible"]
        d["accord_non_contraint"] = acc_v
        d["accord"] = {k2: v2 for k2, v2 in mesures_ep[e].items() if not k2.startswith("somme")}
        d["pas"] = len(pas)
        d["ecart_min"] = min((x[5] for x in pas if x[4] > 1), default=None)
        if v is not None:
            eg = r["ids"] == v
            egaux_ep += eg
            actions_tot += T
            actions_egales += sum(1 for a, b in zip(r["ids"] or [None] * T, v) if a == b)
            d["identifiants_egaux"] = eg
            pe = premier_ecart(r["ids_directs"], v, pas_d)
            if pe is not None:
                erreurs_directes.append({"episode": e, **pe})
            if etape == "resolution":
                controle.append({"episode": e, "methode_table": (classement[e]["entree"] or {}).get("methode")
                                 or "identique_base", "statut": r["statut"], "identifiants_egaux": eg})
        if etape == "resolution":
            d["declaration"] = declarer(r["statut"], r.get("cause"), validation["resultat"]["lecture_validation"]["classe"])
            d["ids"] = r["ids"]
            d["empreinte_cible"] = r["empreinte_cible"]
            d["quasi_egalites"] = r.get("quasi_egalites")
            d["base_nv"] = classement[e]["base_nv"]
        elif v is None or r["ids"] != v:
            d["ids"] = r["ids"]
            d["ids_directs"] = r["ids_directs"]
        detail.append(d)
    trouvees = sum(1 for x in detail if x["empreinte_retrouvee"])
    dossier.mkdir(parents=True, exist_ok=True)
    chemin_pas = dossier / f"pas-resolution-graine-{etape}.npz"
    lignes_pas = [(i, *x) for i, pas in enumerate(pas_tous) for x in pas]
    with open(chemin_pas, "wb") as f:
        col = list(zip(*lignes_pas)) if lignes_pas else [()] * 12
        np.savez_compressed(f, episodes=np.array([r["episode"] for r in resultats]),
                            episode=np.asarray(col[0], dtype=np.int32), pas=np.asarray(col[1], dtype=np.int16),
                            rang=np.asarray(col[2], dtype=np.int16), choix=np.asarray(col[3], dtype=np.int64),
                            non_contraint=np.asarray(col[4], dtype=np.int64),
                            candidats=np.asarray(col[5], dtype=np.int32), ecart=np.asarray(col[6], dtype=np.float64),
                            second=np.asarray(col[7], dtype=np.int64), marge=np.asarray(col[8], dtype=np.float64),
                            balayage=np.asarray(col[9], dtype=bool), p_k=np.asarray(col[10], dtype=np.float64),
                            argmax_p=np.asarray(col[11], dtype=np.int64))
    sha_pas = sceller(chemin_pas)
    accords_agreges = agreger_accords(mesures_ep)
    par_ep = {d["episode"]: d["accord_non_contraint"] for d in detail if d["accord_non_contraint"] is not None}
    resultat = {
        "etape": etape, "version": VERSION, "regle": REGLE, "run_source": config["run_source"],
        "episodes_etape": len(episodes), "empreintes_retrouvees": trouvees,
        "directes": sum(x["voie"] == "directe" for x in resultats),
        "par_repli": sum(x["voie"] == "repli" for x in resultats),
        "par_repli_bascules": {str(n): sum(1 for x in resultats if x["voie"] == "repli" and len(x["forcages"]) == n)
                               for n in range(1, int(config["bascules_max"]) + 1)},
        "non_resolus": [{"episode": x["episode"], "cause": x["cause"]} for x in resultats if x["statut"] != "resolu"],
        "non_resolus_duree": sum(1 for x in resultats if x["statut"] != "resolu" and x.get("duree_epuisee")),
        "non_tentes": sum(1 for x in resultats if x.get("non_tente")),
        "identifiants_egaux_episodes": egaux_ep, "actions_egales": actions_egales, "actions_comparees": actions_tot,
        "accord_non_contraint": {"pas": n_pas, "par_episode_min": min(accords) if accords else None,
                                 "moyenne_par_episode": float(np.mean(accords)) if accords else None,
                                 "par_episode": par_ep, "distribution_par_episode": quantiles(accords),
                                 "pas_en_desaccord": len(marges_desaccord)},
        "accord": accords_agreges,
        "ecarts_contraints": quantiles(ecarts), "marges_en_desaccord": quantiles(marges_desaccord),
        "erreurs_directes": erreurs_directes, "controle_croise": controle,
        "fffd_declares": {x["episode"]: x["fffd"] for x in resultats if x["fffd"]},
        "balayages": {"unite": "pas où la recherche couvre des octets inconnus (commencant_par(E) non vide)",
                      "par_episode": {x["episode"]: x.get("balayages", 0) for x in resultats if x["fffd"]},
                      "complets_par_episode": {x["episode"]: x.get("balayages_complets", 0) for x in resultats
                                               if x["fffd"]}},
        "passes": moteur.passes, "jetons_en_passe": moteur.jetons, "seuils": {
            k: config[k] for k in ("seuil_ecart", "quasi_egalites_max", "bascules_max", "combinaisons_max",
                                   "combinaisons_max_validation", "balayages_max", "seuil_validation", "duree_max_s",
                                   "duree_max_episode_s", "regle_validation")},
        "equivalence_tirage": etat["equivalence_tirage"], "reglages": reglages_det, "modele": config["agent"],
        "environnement": environnement, "environnement_p3": ENVIRONNEMENT_P3, "reserves": reserves,
        "episodes_consignes": etat["episodes_consignes"],
        "pas_fichier": chemin_pas.name, "pas_sha256": sha_pas, "episodes": detail,
        "executions_anterieures_essai": etat.get("executions_anterieures", []),
        "duree_s": round(horloge() - debut, 1)}
    if etape == "validation":
        # mesure rapportée, jamais un arrêt (VG-03) : la résolution se lance quelle que soit cette lecture ; la classe
        # (règle gelée, `lire_validation`) est écrite ici, avant toute lecture humaine (C-3 (1))
        resultat["seuil_validation"] = int(config["seuil_validation"])
        resultat["lecture"] = "atteint" if trouvees >= int(config["seuil_validation"]) else "sous le seuil"
        resultat["lecture_validation"] = lire_validation(trouvees, len(episodes), accords_agreges,
                                                         config["regle_validation"])
        # VI-10 : les épisodes corrigés par la table v2 (entrée autre que « non_resolu ») rapportés à part
        corr = [d for d in detail if ((classement[d["episode"]]["entree"] or {}).get("methode") or "non_resolu")
                != "non_resolu"]
        resultat["corriges_table_v2"] = {
            "episodes": len(corr), "empreintes_retrouvees": sum(1 for d in corr if d["empreinte_retrouvee"]),
            "identifiants_egaux": sum(1 for d in corr if d.get("identifiants_egaux")),
            "par_methode": dict(sorted(collections.Counter(classement[d["episode"]]["entree"]["methode"]
                                                           for d in corr).items()))}
    else:
        resultat["lecture"] = "complète" if trouvees == len(episodes) else "partielle"
        resultat["controle_croise_lecture"] = lecture_controle_croise(controle)
        # classe de la validation recopiée (C-3 (3)) : une résolution sous graines non validées se lit comme telle
        resultat["lecture_validation"] = {**validation["resultat"]["lecture_validation"],
                                          "run_validation": validation["run_id"],
                                          "manifeste_validation_sha256": validation["manifeste_sha256"]}
        resultat["declarations"] = {x["episode"]: x["declaration"] for x in detail}
    ecrire_resultat(racine, chemin_m, f"resolution-graine-{etape}", resultat)
    progres(etape="fin", resolus=f"{trouvees}/{len(episodes)}", lecture=resultat["lecture"].replace(" ", "_"))
    return resultat


def executer(config: dict, racine: Path, run_id: str, prereg: str | None, etape: str, validation: str | None = None,
             autoriser_depot_sale: bool = False, entropie_essai: int | None = None,
             reexecution_essai: bool = False) -> dict:
    """Étape « validation » ou « resolution ». `reexecution_essai` : essais du code seulement (refusé en mode réel) ;
    sinon une sortie antérieure de la même étape, même configuration, même code, arrête avant tout calcul (R3)."""
    racine = Path(racine)
    exiger_config(config)
    exiger_reglages_execution(config)
    if etape not in ETAPES:
        raise GardeArret(f"étape {etape!r} : {ETAPES} attendues")
    anterieurs = exiger_execution_unique(racine, config, etape, reexecution_essai)
    if config["mode"] == "reel" and prereg is None:
        raise GardeArret("résolution réelle sans préenregistrement : R1 interdit de lancer")
    entropie = entropie_essai
    if prereg is not None:
        from ..harnais.validation_reelle import ENTROPIE_CITEE, exiger_code_cite

        texte = Path(prereg).read_text(encoding="utf-8")
        exiger_config_citee(texte, config, str(prereg))
        e = ENTROPIE_CITEE.search(texte)
        if not e:
            raise GardeArret(f"{prereg} ne cite pas l'entropie")
        entropie = int(e.group(1))
        exiger_code_cite(racine, Path(prereg))
    pieces = charger_pieces(config, racine)
    corps_validation = exiger_validation(racine, validation, config) if etape == "resolution" else None
    chemin_m, manifeste = creer_manifeste(racine, run_id, config, ["aucun-tirage-propre"], entropie=entropie,
                                          decisif=prereg is not None, prereg=prereg,
                                          autoriser_depot_sale=autoriser_depot_sale, commande=f"{COMMANDE} --etape {etape}")
    etat = {"etape": "chargement", "executions_anterieures": anterieurs}
    debut = horloge()
    try:
        return _executer(config, racine, run_id, chemin_m, manifeste, pieces, etape, etat, debut, corps_validation)
    except Exception as e:
        # partiel : épisodes déjà consignés (fichiers scellés, identifiants retrouvés), réserves, garde du tirage
        ecrire_resultat(racine, chemin_m, "arret", {"etape": etat["etape"], "motif": motif_d_arret(e),
                                                     "partiel": {k: v for k, v in etat.items() if k != "etape"},
                                                     "duree_s": round(horloge() - debut, 1)})
        relever_term_apres(e)
        raise


def construire_et_verifier_table(config: dict, racine: Path, tokeniseur: str | None, chemin_resultat: str,
                                 fmt=None) -> dict:
    """Étape « table » (processeur) : table v3 depuis la table v2 et le résultat scellé de la résolution ; chaque
    correction, ancienne ou nouvelle, revérifiée par l'empreinte de P3 (`verifier_entrees_v3`). `fmt` : format déjà
    construit (essais en mode jouet) ; sinon tokeniseur lu dans `tokeniseur`, fins de la table v2 et premier jeton de
    clôture (comme `resolution_tokenisation_v1`)."""
    exiger_config(config)
    pieces = charger_pieces(config, racine)
    corps = verifier_resultat(racine, chemin_resultat)
    m, _ = lire_manifeste(Path(racine) / "runs" / corps["run_id"] / "manifeste.json")
    if m["config_sha256"] != empreinte_config(config):
        raise GardeArret("résultat de résolution fait sous une autre configuration")
    if fmt is None and config["mode"] == "jouet":
        _, fmt = _modele(config, racine, pieces)              # répétition jouet : format du modèle minuscule
    if fmt is None:
        from transformers import AutoTokenizer

        from ..harnais.formats import FormatChat

        tok = AutoTokenizer.from_pretrained(tokeniseur)
        fmt = FormatChat(tok, variables=config["agent"]["variables_gabarit"])
        fmt.fins = {int(x) for x in pieces.table["fins_du_format"]} | {fmt._pieces(("x", "y"))["cloture"][0]}
    T = int(config["T"])
    classement = classer(pieces, fmt, T)
    sha_v2 = verifier(Path(racine) / config["chemin_table_tokenisation"])
    table = construire_table_v3(pieces.table, sha_v2, corps["resultat"], verifier(chemin_resultat),
                                {e: c["base_nv"] for e, c in classement.items()})

    def contexte(e):
        ep = EpisodeP3(pieces, e, T)
        return ep.env(), ep.lignes, ep.jetons, ep.jetons_notes, T

    n = verifier_entrees_v3(table["episodes"], fmt, contexte, pieces.fiches)
    if n != table["comptes"]["identiques_apres_table"] - table["comptes"]["identiques_base"]:
        raise GardeArret("corrections vérifiées ≠ comptes de la table")
    table["corrections_verifiees"] = n
    return table


def ecrire_table_v3(table: dict, sortie) -> str:
    """Écrit la table version 3 (jamais par-dessus un fichier existant, R12) et la scelle (VG-08, R6) ; rend son
    empreinte, relue par `verifier`."""
    sortie = Path(sortie)
    if sortie.exists() or Path(f"{sortie}.sha256").exists():
        raise GardeArret(f"{sortie} (ou son sceau) existe déjà (R12 : on n'écrase jamais)")
    sortie.write_text(json.dumps(table, sort_keys=True, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    sha = sceller(sortie)
    if verifier(sortie) != sha:
        raise GardeArret(f"{sortie} : sceau non conforme après écriture")
    return sha


def _main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(prog=COMMANDE)
    ap.add_argument("--etape", required=True, choices=ETAPES + ("table",))
    ap.add_argument("--config", required=True)
    ap.add_argument("--run-id")
    ap.add_argument("--prereg", default=None)
    ap.add_argument("--validation", default=None, help="résultat scellé de l'étape validation (étape resolution)")
    ap.add_argument("--tokeniseur", help="dossier du tokeniseur à la révision de P3 (étape table)")
    ap.add_argument("--resultat", help="résultat scellé de l'étape resolution (étape table)")
    ap.add_argument("--sortie", help="table version 3 à écrire (étape table ; jamais écrasée)")
    a = ap.parse_args(argv)
    signal.signal(signal.SIGTERM, lever_sur_term)
    verifier(a.config)
    config = json.loads(Path(a.config).read_text(encoding="utf-8"))
    if a.etape == "table":
        if not (a.tokeniseur and a.resultat and a.sortie):
            raise GardeArret("étape table : --tokeniseur, --resultat et --sortie obligatoires")
        sortie = Path(a.sortie)
        if sortie.exists() or Path(f"{sortie}.sha256").exists():
            raise GardeArret(f"{sortie} existe déjà (R12 : on n'écrase jamais)")
        table = construire_et_verifier_table(config, Path("."), a.tokeniseur, a.resultat)
        sha = ecrire_table_v3(table, sortie)
        print(json.dumps({"comptes": table["comptes"], "corrections_verifiees": table["corrections_verifiees"],
                          "sha256": sha}, ensure_ascii=False))
        return 0
    if not a.run_id:
        raise GardeArret("--run-id obligatoire")
    r = executer(config, Path("."), a.run_id, a.prereg, a.etape, a.validation)
    print(json.dumps({"etape": r["etape"], "lecture": r["lecture"], "empreintes_retrouvees": r["empreintes_retrouvees"],
                      "episodes": r["episodes_etape"]}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    try:
        sys.exit(_main(sys.argv[1:]))
    except GardeArret as e:
        print(f"ARRÊT : {e}", file=sys.stderr)
        sys.exit(1)
