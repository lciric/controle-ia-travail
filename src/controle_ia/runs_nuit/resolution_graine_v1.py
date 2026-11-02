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
au niveau de l'octet ; jetons spéciaux hors fins : zéro octet, effacés du texte par P3), de celui qui maximise `p / q` ;
si le choix diffère du découpage courant, le reste est redécoupé canoniquement et une nouvelle passe est faite. Le
dernier jeton d'une action est un jeton de fin (parmi `fmt.fins`, même règle) quand `jetons − jetons_notes = 1`
(stocké par P3) ; sinon l'action compte `max_nouveaux` jetons. Consigné par pas : choix contraint, choix non contraint
(argmax de `p / q` sur tout le vocabulaire, comme P3), nombre de candidats, écart en log entre le premier et le second
candidat compatibles, marge en log du choix non contraint. **Arbitre unique : l'empreinte de trajectoire de P3**
(sha256 de l'épisode du harnais), recalculée sur l'épisode reconstruit.

**Repli écrit** (`resoudre_avec_repli`) : si l'empreinte n'est pas retrouvée, les quasi-égalités du premier essai (écart
sous `seuil_ecart`, au plus `quasi_egalites_max`, les plus fragiles d'abord) sont basculées vers leur second candidat,
une, puis deux à la fois (`bascules_max`), dans l'ordre de `itertools.combinations`, au plus `combinaisons_max`
combinaisons, chacune rejouée depuis l'action basculée et arbitrée par l'empreinte ; sinon « non résolu », avec sa
cause. Caractère de remplacement U+FFFD dans le texte : **cas déclaré** (compté par épisode) ; les octets inconnus qu'il
recouvre sont traités par un balayage du vocabulaire seulement si c'est simple (au plus `balayages_max` balayages par
épisode), sinon « non résolu » déclaré.

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
import codecs
import hashlib
import itertools
import json
import math
import signal
import sys
import time
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass, field
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
REGLE = ("rejeu à graine : graines des actions de P3 (manifeste, clé tache/<identifiant>, graines_des_actions) ; à chaque "
         "pas, parmi les jetons compatibles avec les octets restants du texte stocké (spéciaux hors fins : zéro octet ; "
         "dernier pas : jeton de fin si jetons − jetons_notes = 1), celui qui maximise p / q, q = tirages exponentiels de "
         "la graine ; passe forcée par l'enseignant, redécoupage canonique du reste après chaque divergence ; arbitre "
         "unique : empreinte de trajectoire de P3 ; repli : bascule des quasi-égalités (écart sous le seuil), une puis "
         "deux, combinaisons bornées, arbitrées par l'empreinte ; sinon non résolu, cause écrite")


class Contradiction(Exception):
    """Le texte stocké, les longueurs de P3 et les choix ne s'accordent pas (essai à rejeter, pas une garde du run)."""

    def __init__(self, t: int, s: int, motif: str):
        super().__init__(f"pas {t}, jeton {s} : {motif}")
        self.t, self.s, self.motif = t, s, motif


class NonResolu(Exception):
    """Cas déclaré hors de la méthode (caractère de remplacement non simple) : l'épisode est « non résolu »."""


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

    def candidats(self, etat) -> tuple[list[int], bool]:
        """(jetons ordinaires compatibles, triés ; vrai si un balayage du vocabulaire a été nécessaire)."""
        r = self._attendu(etat)
        if r is None:
            return [], False
        E, atteint = r
        c = self.voc.prefixes(E)
        if atteint:
            c += self.voc.commencant_par(E)
        c = [i for i in set(c) if self.avancer(etat, i) is not None]
        return sorted(c), bool(atteint)

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

    `passe` rend aussi, ligne par ligne, le choix non contraint (argmax de softmax(logits / température) / q, l'opération
    même de P3) et sa marge en log (premier contre second) : calcul groupé sur l'appareil du modèle (la carte en mode
    réel ; les mêmes opérations que P3, qui les faisait sur processeur : écarts d'arrondi en float32 seulement,
    négligeables devant le bruit des logits en bfloat16)."""

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


@dataclass
class Reglages:
    temperature: float = 1.0
    max_nouveaux: int = 400
    seuil_ecart: float = 0.5
    quasi_egalites_max: int = 12
    bascules_max: int = 2
    combinaisons_max: int = 80
    balayages_max: int = 64
    echeance: float | None = None


@dataclass
class Compteurs:
    balayages: int = 0
    passes: int = 0


def resoudre_action(moteur, voc: Vocabulaire, tok, ctx: list[int], texte: str, n: int, a_fin: int, Q: torch.Tensor,
                    fin_defaut: int, reglages: Reglages, t: int = 0, forcages: dict | None = None,
                    pas: list | None = None, compteurs: Compteurs | None = None) -> list[int]:
    """Identifiants d'une action : n jetons, le dernier parmi les fins si `a_fin`. `pas` reçoit, par jeton, (t, s, choix,
    non contraint, candidats, écart, second, marge, balayage). Lève `Contradiction` (essai à rejeter) ou `NonResolu`."""
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
        if reglages.echeance is not None and time.perf_counter() > reglages.echeance:
            raise GardeArret(f"limite de durée dépassée (pas {t}, jeton {len(choisis)})")
        s0 = len(choisis)
        devine = deviner(cible, etat, voc, tok, n - s0, a_fin, fin_defaut)
        k_lignes = len(devine) + 1
        L, non_contraints, marges = moteur.passe(ctx + choisis + devine, k_lignes, Q[s0:s0 + k_lignes],
                                                 reglages.temperature)
        compteurs.passes += 1
        for j in range(len(devine) + 1):
            s = s0 + j
            if a_fin and s == n - 1:
                if not cible.fini(etat):
                    raise Contradiction(t, s, "octets du texte restants au jeton de fin")
                cands, balayage = voc.fins, False
            else:
                cands, balayage = cible.candidats(etat)
                if balayage:
                    compteurs.balayages += 1
                    if compteurs.balayages > reglages.balayages_max:
                        raise NonResolu(f"caractère de remplacement : cas non simple ({compteurs.balayages} balayages du "
                                        f"vocabulaire > {reglages.balayages_max})")
                cands = cands + voc.speciaux_non_fins
            if not cands:
                raise Contradiction(t, s, "aucun jeton compatible avec le texte")
            # choix contraint : argmax de p / q parmi les candidats, soit de log p − log q (même ordre ; calcul en
            # double précision sur les seuls candidats ; égalité exacte : plus petit identifiant, comme argmax)
            ordre = sorted(cands)
            ct = torch.tensor(ordre, dtype=torch.long)
            sc = (L[j, ct] / reglages.temperature).double() - torch.log(Q[s, ct].double())
            k = int(torch.argmax(sc))
            choix = ordre[k]
            if (t, s) in forcages:
                choix = int(forcages[(t, s)])
                if choix not in set(ordre):
                    raise Contradiction(t, s, f"jeton forcé {choix} hors des candidats")
                k = ordre.index(choix)
            ecart, second = math.inf, -1
            if len(ordre) > 1:
                autres = sc.clone()
                autres[k] = -math.inf
                k2 = int(torch.argmax(autres))
                ecart, second = float(sc[k] - autres[k2]), ordre[k2]
            non_contraint, marge = non_contraints[j], marges[j]
            if pas is not None:
                pas.append((t, s, choix, non_contraint, len(ordre), ecart, second, marge, balayage))
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


def resoudre_avec_repli(moteur, voc, fmt, fabrique_env, identifiant: str, T: int, textes, jetons, jetons_notes, Qs,
                        empreinte_cible: str, reglages: Reglages, combinaisons_max: int | None = None) -> dict:
    """Essai direct, puis repli écrit (bascule des quasi-égalités, voir le module) ; arbitre : `empreinte_cible`."""
    depart = time.perf_counter()
    cmax = reglages.combinaisons_max if combinaisons_max is None else int(combinaisons_max)
    sortie = {"episode": identifiant, "fffd": sum(x.count(FFFD) for x in textes), "statut": "non_resolu", "voie": None,
              "cause": None, "forcages": [], "combinaisons_essayees": 0, "ids": None, "ids_directs": None,
              "empreinte": None, "empreinte_cible": empreinte_cible}
    pas: list = []
    compteurs = Compteurs()
    trouves_directs: list = []

    def essai(forcages, prefixe, journal_pas, cpt):
        rec, trouves = rejouer_episode(moteur, voc, fmt, fabrique_env(), identifiant, T, textes, jetons, jetons_notes,
                                       Qs, reglages, forcages, prefixe, journal_pas, cpt)
        return rec, trouves, empreinte_trajectoire(episode_harnais(identifiant, T, rec))

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
        sortie.update(cause=str(c), pas=pas, balayages=compteurs.balayages, passes=compteurs.passes,
                      duree_s=round(time.perf_counter() - depart, 2))
        return sortie
    # identifiants de l'essai direct, action par action (partiels en cas de contradiction) : pour la mesure à l'aveugle
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
                rec, trouves, emp = essai(forcages, prefixe, journal_pas, cpt)
            except (Contradiction, NonResolu):
                continue
            if emp == empreinte_cible:
                sortie.update(statut="resolu", voie="repli", ids=trouves, empreinte=emp, cause=None, pas=journal_pas,
                              forcages=[{"pas": x[0], "rang": x[1], "jeton": x[6], "ecart": x[5]} for x in combo])
                sortie["combinaisons_essayees"] = essayees
                sortie["duree_s"] = round(time.perf_counter() - depart, 2)
                return sortie
    sortie["combinaisons_essayees"] = essayees
    sortie["cause"] = (f"{sortie['cause']} ; repli : {len(quasi)} quasi-égalité(s) sous {reglages.seuil_ecart}, "
                       f"{essayees} combinaison(s) essayée(s), aucune ne redonne l'empreinte")
    sortie["duree_s"] = round(time.perf_counter() - depart, 2)
    return sortie


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
    sont cités (`resultat_hors_table`), non versés. Gardes : version 2, étape « resolution », mêmes empreintes de P3."""
    if table_v2.get("version") != rt.VERSION_TABLE:
        raise GardeArret(f"table v2 attendue, version {table_v2.get('version')!r}")
    if resultat.get("etape") != "resolution":
        raise GardeArret("résultat de l'étape « resolution » attendu")
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
        res = {"voie": r["voie"], "forcages": r["forcages"], "resultat_sha256": sha_resultat}
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


def reglages_de(config: dict, echeance: float | None) -> Reglages:
    return Reglages(temperature=float(config["temperature"]), max_nouveaux=int(config["max_nouveaux"]),
                    seuil_ecart=float(config["seuil_ecart"]), quasi_egalites_max=int(config["quasi_egalites_max"]),
                    bascules_max=int(config["bascules_max"]), combinaisons_max=int(config["combinaisons_max"]),
                    balayages_max=int(config["balayages_max"]), echeance=echeance)


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
    """Garde de la validation : au moins `seuil` empreintes de P3 retrouvées sur `episodes` (arrêt sinon)."""
    if seuil > episodes:
        raise GardeArret(f"seuil de validation {seuil} > {episodes} épisodes à identifiants connus")
    if trouvees < seuil:
        raise GardeArret(f"validation : {trouvees} empreinte(s) de P3 retrouvée(s) sur {episodes}, sous le seuil de "
                         f"{seuil} : la méthode ne se transpose pas, résolution non lancée")


def exiger_validation(racine: Path, chemin, config: dict) -> dict:
    """La résolution exige une validation scellée, rattachée à son manifeste, de même configuration et même commit, de
    lecture « atteint »."""
    if not chemin:
        raise GardeArret("étape « resolution » sans --validation : la validation à l'aveugle passe d'abord")
    corps = verifier_resultat(racine, chemin)
    m, _ = lire_manifeste(Path(racine) / "runs" / corps["run_id"] / "manifeste.json")
    r = corps["resultat"]
    if r.get("etape") != "validation" or r.get("lecture") != "atteint":
        raise GardeArret(f"validation {chemin} : étape {r.get('etape')!r}, lecture {r.get('lecture')!r}")
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


def _executer(config, racine, run_id, chemin_m, manifeste, pieces, etape, etat, debut) -> dict:
    from ..harnais.modeles import regler_determinisme
    from ..harnais.validation_reelle import noyau
    from .rejeu_activations_v1 import progres

    reel = config["mode"] == "reel"
    appareil = "cuda" if reel else "cpu"
    reglages_det = regler_determinisme(config["fils"], appareil)
    T = int(config["T"])
    echeance = debut + float(config["duree_max_s"])
    modele, fmt = _modele(config, racine, pieces)
    attendu = config["agent"].get("texte_attendu_ouverture")
    if reel and not attendu:
        raise GardeArret("agent : texte attendu dans l'ouverture absent de la configuration")
    etat["etape"] = "classement"
    classement = classer(pieces, fmt, T)
    episodes = episodes_de_l_etape(etape, config, classement)
    if attendu:
        ep0 = EpisodeP3(pieces, episodes[0], T)
        e0 = ep0.env()
        if attendu not in fmt.tok.decode(fmt.ouverture(e0.consigne_privee(0), e0.observation(0, 0, []))):
            raise GardeArret(f"agent : ouverture sans {attendu!r} (variables du gabarit non lues)")
    voc = Vocabulaire(fmt.tok, fmt.fins, int(modele.config.vocab_size))
    etat["equivalence_tirage"] = exiger_equivalence_tirage(voc.V)
    moteur = Moteur(modele)
    reglages = reglages_de(config, echeance)
    cmax = int(config["combinaisons_max_validation" if etape == "validation" else "combinaisons_max"])
    tirages = Tirages(voc.V, int(config["fils_tirages"]))
    eps = {e: EpisodeP3(pieces, e, T) for e in episodes}
    resultats, pas_tous, pas_directs = [], [], []
    etat["etape"] = etape
    progres(etape=etape, episodes=len(episodes))
    try:
        with noyau(config["noyau_attention"]):
            for k, e in enumerate(episodes):
                exiger_sans_signal(f"résolution à graine, épisode {k}")
                if time.perf_counter() > echeance:
                    raise GardeArret(f"limite de durée dépassée avant l'épisode {k}")
                for e2 in episodes[k:k + 1 + int(config["episodes_d_avance"])]:
                    tirages.demander(e2, eps[e2].graines, eps[e2].jetons)
                ep = eps[e]
                Qs = tirages.prendre(e)
                r = resoudre_avec_repli(moteur, voc, fmt, ep.env, e, T, ep.textes, ep.jetons, ep.jetons_notes, Qs,
                                        ep.empreinte, reglages, cmax)
                del Qs
                r["graines"] = ep.graines
                pas_tous.append(r.pop("pas", []))
                pas_directs.append(r.pop("pas_direct", None) or pas_tous[-1])
                resultats.append(r)
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
    for r, pas, pas_d in zip(resultats, pas_tous, pas_directs):
        e = r["episode"]
        v = verite(pieces, fmt, T, classement, e)
        ecarts += [x[5] for x in pas if x[4] > 1]
        marges_desaccord += [x[7] for x in pas if x[3] != x[2]]
        n_pas += len(pas)
        acc_v = accord_non_contraint(pas, v if v is not None else r["ids"]) if (v or r["ids"]) else None
        if acc_v is not None:
            accords.append(acc_v)
        d = {k2: r[k2] for k2 in ("episode", "statut", "voie", "cause", "forcages", "combinaisons_essayees", "passes",
                                  "balayages", "fffd", "duree_s", "graines") if k2 in r}
        d["empreinte_retrouvee"] = r["statut"] == "resolu"
        d["accord_non_contraint"] = acc_v
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
                                 or "identique_base", "identifiants_egaux": eg})
        if etape == "resolution":
            d["ids"] = r["ids"]
            d["empreinte_cible"] = r["empreinte_cible"]
            d["quasi_egalites"] = r.get("quasi_egalites")
            d["base_nv"] = classement[e]["base_nv"]
        elif v is None or r["ids"] != v:
            d["ids"] = r["ids"]
            d["ids_directs"] = r["ids_directs"]
        detail.append(d)
    trouvees = sum(x["statut"] == "resolu" for x in resultats)
    dossier = Path(racine) / "diag" / run_id
    dossier.mkdir(parents=True, exist_ok=True)
    chemin_pas = dossier / f"pas-resolution-graine-{etape}.npz"
    lignes_pas = [(i, *x) for i, pas in enumerate(pas_tous) for x in pas]
    with open(chemin_pas, "wb") as f:
        col = list(zip(*lignes_pas)) if lignes_pas else [()] * 10
        np.savez_compressed(f, episodes=np.array([r["episode"] for r in resultats]),
                            episode=np.asarray(col[0], dtype=np.int32), pas=np.asarray(col[1], dtype=np.int16),
                            rang=np.asarray(col[2], dtype=np.int16), choix=np.asarray(col[3], dtype=np.int64),
                            non_contraint=np.asarray(col[4], dtype=np.int64),
                            candidats=np.asarray(col[5], dtype=np.int32), ecart=np.asarray(col[6], dtype=np.float64),
                            second=np.asarray(col[7], dtype=np.int64), marge=np.asarray(col[8], dtype=np.float64),
                            balayage=np.asarray(col[9], dtype=bool))
    sha_pas = sceller(chemin_pas)
    resultat = {
        "etape": etape, "version": VERSION, "regle": REGLE, "run_source": config["run_source"],
        "episodes_etape": len(episodes), "empreintes_retrouvees": trouvees,
        "directes": sum(x["voie"] == "directe" for x in resultats),
        "par_repli": sum(x["voie"] == "repli" for x in resultats),
        "non_resolus": [{"episode": x["episode"], "cause": x["cause"]} for x in resultats if x["statut"] != "resolu"],
        "identifiants_egaux_episodes": egaux_ep, "actions_egales": actions_egales, "actions_comparees": actions_tot,
        "accord_non_contraint": {"pas": n_pas, "par_episode_min": min(accords) if accords else None,
                                 "moyenne_par_episode": float(np.mean(accords)) if accords else None,
                                 "pas_en_desaccord": len(marges_desaccord)},
        "ecarts_contraints": quantiles(ecarts), "marges_en_desaccord": quantiles(marges_desaccord),
        "erreurs_directes": erreurs_directes, "controle_croise": controle,
        "fffd_declares": {x["episode"]: x["fffd"] for x in resultats if x["fffd"]},
        "passes": moteur.passes, "jetons_en_passe": moteur.jetons, "seuils": {
            k: config[k] for k in ("seuil_ecart", "quasi_egalites_max", "bascules_max", "combinaisons_max",
                                   "combinaisons_max_validation", "balayages_max", "seuil_validation")},
        "equivalence_tirage": etat["equivalence_tirage"], "reglages": reglages_det, "modele": config["agent"],
        "pas_fichier": chemin_pas.name, "pas_sha256": sha_pas, "episodes": detail,
        "duree_s": round(time.perf_counter() - debut, 1)}
    if etape == "validation":
        resultat["seuil_validation"] = int(config["seuil_validation"])
        resultat["lecture"] = "atteint" if trouvees >= int(config["seuil_validation"]) else "sous le seuil"
    else:
        resultat["lecture"] = "complète" if trouvees == len(episodes) else "partielle"
        resultat["controle_croise_lecture"] = ("conforme" if all(c["identifiants_egaux"] for c in controle)
                                               else "contraire")
    ecrire_resultat(racine, chemin_m, f"resolution-graine-{etape}", resultat)
    progres(etape="fin", resolus=f"{trouvees}/{len(episodes)}", lecture=resultat["lecture"].replace(" ", "_"))
    if etape == "validation":
        exiger_seuil_validation(trouvees, int(config["seuil_validation"]), len(episodes))
    return resultat


def executer(config: dict, racine: Path, run_id: str, prereg: str | None, etape: str, validation: str | None = None,
             autoriser_depot_sale: bool = False, entropie_essai: int | None = None) -> dict:
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
        if CONFIG_CITEE.format(empreinte_config(config)) not in texte:
            raise GardeArret(f"{prereg} ne cite pas la configuration de la résolution {empreinte_config(config)[:12]}")
        e = ENTROPIE_CITEE.search(texte)
        if not e:
            raise GardeArret(f"{prereg} ne cite pas l'entropie")
        entropie = int(e.group(1))
        exiger_code_cite(racine, Path(prereg))
    pieces = charger_pieces(config, racine)
    if etape == "resolution":
        exiger_validation(racine, validation, config)
    chemin_m, manifeste = creer_manifeste(racine, run_id, config, ["aucun-tirage-propre"], entropie=entropie,
                                          decisif=prereg is not None, prereg=prereg,
                                          autoriser_depot_sale=autoriser_depot_sale, commande=f"{COMMANDE} --etape {etape}")
    etat = {"etape": "chargement"}
    debut = time.perf_counter()
    try:
        return _executer(config, racine, run_id, chemin_m, manifeste, pieces, etape, etat, debut)
    except Exception as e:
        ecrire_resultat(racine, chemin_m, "arret", {"etape": etat["etape"], "motif": motif_d_arret(e),
                                                     "partiel": {k: v for k, v in etat.items() if k != "etape"},
                                                     "duree_s": round(time.perf_counter() - debut, 1)})
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
        if sortie.exists():
            raise GardeArret(f"{sortie} existe déjà (R12 : on n'écrase jamais)")
        table = construire_et_verifier_table(config, Path("."), a.tokeniseur, a.resultat)
        sortie.write_text(json.dumps(table, sort_keys=True, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
        print(json.dumps({"comptes": table["comptes"], "corrections_verifiees": table["corrections_verifiees"],
                          "sha256": hashlib.sha256(sortie.read_bytes()).hexdigest()}, ensure_ascii=False))
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
