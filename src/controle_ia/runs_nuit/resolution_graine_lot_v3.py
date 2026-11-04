"""Relance v4 de R1 : retrouver les identifiants des épisodes de P3 dont la reconstruction de base n'est pas celle de P3
et que la table v3 ne couvre pas (les 89 épisodes non entièrement conformes en longueur), par le **lot fidèle à
plusieurs cibles**, précédé d'un **témoin** ; construire la **table v4**. Version 3 du lot fidèle, nom nouveau (R12) :
copie de `resolution_graine_lot_v2` (non modifié) dont chaque écart est marqué `# v3` : (a) arbitrage de la mère sur la
contre-lecture R2 (`contre-lecture-relance-v4-v1.md`, `e224ae8a…`, M7) : **témoin « non exact » → même voie que
« exact »** (lot à plusieurs cibles, puis lot à une cible avec repli écrit, puis passe forcée du cœur), la lecture du
témoin étant rapportée telle quelle ; (b) point I5 : **mesure de l'indépendance des lignes** dans `lots_rapport`
(`mesure_independance` : accord des lignes connues et captures, avant et après la première action en échec d'une cible ;
deux réserves descriptives, sans effet sur aucune entrée, aucune classe, aucune voie). `resolution_graine_lot_v1` et
`resolution_graine_v1` ne sont pas modifiés, ils sont importés par leurs fonctions
publiques (`ChoixCible`, `MesureLigne`, `MoteurLot`, `LigneLot`, `resoudre_episode_lot`, `mesure_des_voisines`,
`plan_des_lots`, `pad_du_format`, `fin_par_defaut` ; `Vocabulaire`, `tirages_exponentiels`, `resoudre_avec_repli`,
`transcription`, `classer`, `charger_pieces`, `EpisodeP3`, `entree_identifiants`, `appliquer_entree_v3`,
`verifier_entrees_v3`, `charger_table_v3`, `consigner_episode`).

Pourquoi (diagnostic `rapport-diagnostic-r1-v4-v1.md`, `1c2dd25f…`) : les 89 épisodes cassés sont exactement ceux qui ne
sont pas entièrement conformes en longueur ; cause : le texte stocké, retokenisé, ne redonne pas les jetons tirés par P3
(redécoupages, chaînes de jeton spécial réservé épelées puis fondues, un U+FFFD) ; aucun n'est dans la table v3, et le
code de la v3 les excluait en amont (`cibles_du_lot` : « absent de la table v2 ») et en aval (`construire_table_v3_lot`,
`charger_table_v3`, règle A du rejeu v3).

**Étape « temoin »** (lots 2 et 13 de P3, aucun épisode cassé) : chaque lot rejoué en entier, toutes ses lignes forcées à
leurs identifiants connus (base identique ou table v3, revérifiés par l'empreinte de P3), même composition, mêmes
graines, même ordre, même remplissage à gauche, préremplissage puis une passe par jeton avec cache, logits du dernier
jeton en float32 sur processeur, jusqu'à la fin de la dernière ligne (la forme exacte de `generer_lot`) ; chaque ligne
mesurée à chaque pas avec les tirages de **sa** graine (`MesureLigne`) ; activations des actions d'équivalence de P3
recapturées pendant les mêmes passes, avec les crochets de P3 (`Crochets`, `relire_crochets_lot`), et comparées à
`empreintes_capture` des fiches de P3. **Lecture gelée d'avance** (`lire_temoin`) : « exact » si, sur chaque lot, l'accord
du choix non contraint avec le jeton de P3 vaut 1 exactement sur tous les pas mesurés, l'égalité des choix contraints
vaut 1, aucun jeton connu n'est hors des candidats, toutes les empreintes de capture sont égales à celles de P3, aucun
jeton manquant et les passes égales à celles qu'impose la forme de P3 ; « non exact » sinon ; « sans mesure » si aucun
pas n'est mesuré (refusé : le témoin doit mesurer).

**Étape « reparation »** : lit le résultat scellé du témoin. **Témoin « exact » ou « non exact » → voie « lot fidèle »**
(v3 ; « sans mesure » : arrêt) : pour chacun des
lots qui contiennent une cible, un essai à plusieurs cibles (toutes les lignes cassées du lot choisissent en même temps,
chacune contrainte par son texte stocké et sa graine, `argmax(p / q)` parmi les jetons compatibles ; les longueurs de
chaque action sont imposées par P3, donc la forme du lot est exacte à chaque pas quels que soient les choix) ; une cible
en contradiction (aucun jeton compatible) est remplie, pour la suite de l'essai, de jetons ordinaires au nombre de P3
(forme gardée), et déclarée ; puis, pour chaque cible non retrouvée, le lot fidèle à une cible avec son repli écrit
(`resolution_graine_lot_v1.resoudre_episode_lot`, frontière entière), puis la passe forcée du cœur à frontière entière
(`resolution_graine_v1.resoudre_avec_repli`). (La v2 écrivait : témoin « non exact » → passe forcée seule ; la v3 garde
le lot, qui contient la passe forcée et la domine en couverture, contre-lecture M7.) Arbitre unique : égalité
de l'empreinte de trajectoire de P3 (sha256). Chaque épisode est consigné aussitôt (`episodes-reparation/NNN.json`).

**Étape « table-v4 »** (processeur) : table v3 inchangée (ses 22 entrées) plus une entrée par cible : « identifiants »
si retrouvée, « non_resolu » sinon ; chaque correction revérifiée par l'empreinte de P3 (`verifier_entrees_v3`) ; la
table couvre exactement les épisodes dont la trajectoire de base diffère de P3 ; version 4 ; scellée, jamais écrasée.

Durées : gardes contre une boucle folle seulement (C2 du complément : 14 400 s par épisode, 259 200 s par étape), jamais
un couperet attendu ; repli à sa frontière écrite entière (C1 : 16 + 16 × 16 = 272 combinaisons).

Interdits respectés par construction : aucun score, aucune note, aucune activation de rejeu ; des fiches de P3, seules les
empreintes et, sous `equivalence`, les clés `actions`, `empreintes_capture`, `longueurs_contexte`, `positions_capturees`
et `lignes` sont lues (`captures_de_p3`).

    PYTHONPATH=src python -m controle_ia.runs_nuit.resolution_graine_lot_v3 --etape temoin --config CONFIG \\
        --run-id AAAAMMJJ-HHMMSS-r1-v4-temoin --prereg prereg/R1-addendum-relance-v4.md
    PYTHONPATH=src python -m controle_ia.runs_nuit.resolution_graine_lot_v3 --etape reparation --config CONFIG \\
        --run-id AAAAMMJJ-HHMMSS-r1-v4-reparation --prereg prereg/R1-addendum-relance-v4.md \\
        --temoin diag/<run du témoin>/resolution-graine-lot-v3-temoin.json
    PYTHONPATH=src python -m controle_ia.runs_nuit.resolution_graine_lot_v3 --etape table-v4 --config CONFIG \\
        --tokeniseur DOSSIER --reparation diag/<run>/resolution-graine-lot-v3-reparation.json \\
        --sortie prereg/R1-table-tokenisation-v4.json          (processeur seulement)
"""
from __future__ import annotations

import argparse
import contextlib
import hashlib
import json
import signal
import sys
from dataclasses import dataclass
from pathlib import Path

import torch

from ..gardes import GardeArret, exiger_sans_signal, lever_sur_term, motif_d_arret, relever_term_apres
from ..manifeste import creer_manifeste, ecrire_resultat, generateur, lire_manifeste, verifier_resultat
from ..scellement import sceller, verifier
from . import resolution_graine_lot_v1 as rl
from . import resolution_graine_v1 as rg
from .rejeu_activations_v1 import episode_harnais, empreinte_trajectoire

VERSION = "resolution_graine_lot_v3"                                                                         # v3
COMMANDE = "python -m controle_ia.runs_nuit.resolution_graine_lot_v3"                                       # v3
CONFIG_CITEE = "Configuration de la réparation v4 (lot fidèle à plusieurs cibles, empreinte canonique) : `{}`"
ETAPE_TEMOIN, ETAPE_REPARATION, ETAPE_TABLE = "temoin", "reparation", "table-v4"
ETAPES = (ETAPE_TEMOIN, ETAPE_REPARATION)
LECTURE_EXACT, LECTURE_NON_EXACT, LECTURE_SANS = "exact", "non exact", "sans mesure"
VOIE_LOT, VOIE_PASSE = "lot_fidele", "passe_forcee"
VOIE_SI_NON_EXACT = VOIE_LOT     # v3 : écrit d'avance (arbitrage de la mère, M7) : témoin non exact → lot puis repli
VERSION_TABLE_V4 = 4
SOURCE_CIBLE, SOURCE_APPROCHEE = rl.SOURCE_CIBLE, rl.SOURCE_APPROCHEE
CLES_V2 = ("chemin_table_v3", "table_v3_sha256", "lots_temoin", "lots_d_abord", "cibles_attendues",
           "lots_cibles_attendus", "combinaisons_max_lot", "duree_max_episode_lot_s", "duree_max_lot_s",
           "seuil_lecture_lot", "capture_equivalence", "voie_si_temoin_non_exact")
CLES = rg.CLES_COMPLETES + CLES_V2
REGLE = ("lot fidèle à plusieurs cibles (relance v4 de R1) : témoin d'abord (lots sans épisode cassé, toutes lignes "
         "forcées à leurs identifiants connus, chaque ligne mesurée avec sa graine, captures d'équivalence de P3 "
         "recapturées ; « exact » si accord 1 exactement, choix contraints égaux, aucun jeton hors des candidats, toutes "
         "les captures égales, forme égale) ; témoin exact : chaque lot qui contient une cible rejoué en entier, toutes "
         "ses cibles choisissant ensemble (argmax de p / q parmi les jetons compatibles avec le texte stocké, longueurs "
         "imposées par P3, forme exacte à chaque pas), puis lot fidèle à une cible avec repli écrit, puis passe forcée du "
         "cœur, frontière entière ; témoin non exact (v3) : même voie (lot, puis repli, puis passe forcée), lecture du témoin "
         "rapportée ; indépendance des lignes mesurée par lot réparé, avant et après le premier échec d'une cible, "
         "rapportée sans effet ; arbitre unique : "
         "empreinte de trajectoire de P3 ; table v4 = table v3 inchangée plus une entrée par cible (identifiants si "
         "retrouvée, non_resolu sinon), chaque correction revérifiée par l'empreinte de P3")


# --------------------------------------------------------------------------------------------------------------------
# Lignes du lot


def remplissage_ordinaire(voc: rg.Vocabulaire) -> int:
    """Jeton de remplissage **ordinaire** (le plus petit identifiant à octets non vides), jamais un jeton de fin : le
    remplissage de P3 (`pad_du_format`) est une fin chez Llama 3 (128001), qui arrêterait la ligne avant sa longueur."""
    for i in range(voc.V):
        if voc.octets[i]:
            return int(i)
    raise GardeArret("vocabulaire sans jeton ordinaire")


def forcee_approchee(base: list[int], n: int, jn: int, remplissage: int, fin_defaut: int, fins) -> list[int]:
    """Action approchée au nombre de jetons de P3 : découpage de base sans sa fin, tout jeton de fin interne remplacé
    par `remplissage` (ordinaire), tronqué ou complété à `jn`, puis `fin_defaut` si P3 a compté une fin (`n − jn = 1`).
    La forme (longueur, clôture) est celle de P3 ; le contenu ne l'est pas (ligne déclarée approchée)."""
    a_fin = int(n) - int(jn)
    if a_fin not in (0, 1):
        raise GardeArret(f"jetons − jetons notés = {a_fin}")
    fins = {int(x) for x in fins}
    if int(remplissage) in fins:
        raise GardeArret("remplissage d'une ligne approchée parmi les fins : la ligne s'arrêterait avant sa longueur")
    notes = [int(x) for x in base]
    if notes and notes[-1] in fins:
        notes = notes[:-1]
    notes = [int(remplissage) if x in fins else x for x in notes][:int(jn)]
    notes += [int(remplissage)] * (int(jn) - len(notes))
    return notes + ([int(fin_defaut)] if a_fin else [])


@dataclass
class LigneLotV2(rl.LigneLot):
    """`LigneLot` de la v1, dont la ligne approchée est remplie d'un jeton **ordinaire** (`forcee_approchee`) au lieu du
    remplissage de P3 (une fin chez Llama 3) ; `ids` d'une ligne approchée = découpage de base."""
    remplissage: int = -1
    base_nv: list | None = None

    def forcee(self, t: int, pad_id: int, fin_defaut: int, fins) -> list[int]:
        if self.exacte:
            return super().forcee(t, pad_id, fin_defaut, fins)
        return forcee_approchee(self.ids[t], self.jetons[t], self.jetons_notes[t], self.remplissage, fin_defaut, fins)


# --------------------------------------------------------------------------------------------------------------------
# Génération en lot à plusieurs cibles, à la forme exacte de P3


def generer_lot_multi(moteur: rl.MoteurLot, contextes: list[list[int]], max_nouveaux: int, fins: set[int], pad_id: int,
                      forces: list, longueurs: list[int], choix: dict, t: int = 0, mesures: dict | None = None,
                      capture: dict | None = None, remplissage: int | None = None,
                      fins_defaut: list | None = None) -> tuple[list[list[int]], dict]:
    """`generer_lot` refait appel pour appel (remplissage à gauche, masque, positions explicites, préremplissage puis une
    passe par jeton avec cache, `logits_to_keep=1`, logits du dernier jeton en float32 sur processeur), **jusqu'à la fin
    de la dernière ligne** ; les lignes de `choix` ({ligne : ChoixCible}) choisissent sous contrainte du texte, les autres
    reçoivent `forces[r]` ; chaque ligne s'arrête à `longueurs[r]` jetons ou à son premier jeton de fin. Une cible en
    contradiction (`Contradiction`, `NonResolu`, `DureeEpuisee`) est déclarée dans `plan["echecs"]` et reçoit, jusqu'à sa
    longueur, `remplissage` (ordinaire) puis, à la dernière place si P3 a compté une fin, `fins_defaut[r]` : la forme du
    lot reste celle de P3. `mesures` ({ligne : MesureLigne}) : lignes exactes mesurées. `capture` ({"lignes", "couches"})
    : activations de génération de ces lignes recapturées avec les crochets de P3 ; leurs empreintes (`empreinte_tableaux`)
    sont rendues par ligne dans `plan["captures"]`."""
    from ..harnais.activations import Crochets
    from ..harnais.episode import empreinte_tableaux, relire_crochets_lot

    if max_nouveaux < 1:
        raise GardeArret("max_nouveaux < 1")
    if not contextes or any(len(c) == 0 for c in contextes):
        raise GardeArret("lot vide ou contexte vide")
    B, L = len(contextes), max(len(c) for c in contextes)
    if len(forces) != B or len(longueurs) != B:
        raise GardeArret(f"{len(forces)} forçages et {len(longueurs)} longueurs pour {B} lignes")
    for r in range(B):
        if r in choix:
            if int(choix[r].n) != int(longueurs[r]):
                raise GardeArret(f"ligne cible {r} : longueur {longueurs[r]} ≠ {choix[r].n} du choix contraint")
        elif forces[r] is None:
            raise GardeArret(f"ligne {r} : jetons forcés obligatoires hors des cibles")
    mesures = mesures or {}
    if set(mesures) & set(choix):
        raise GardeArret("une ligne cible n'est pas une ligne mesurée")
    if choix and (remplissage is None or fins_defaut is None or int(remplissage) in fins):
        raise GardeArret("cibles sans remplissage ordinaire ni fins par défaut (forme d'une cible en échec)")
    lignes_cap = sorted({int(x) for x in (capture or {}).get("lignes") or []})
    ids = torch.full((B, L), int(pad_id), dtype=torch.long)
    masque = torch.zeros((B, L), dtype=torch.long)
    for r, c in enumerate(contextes):
        ids[r, L - len(c):] = torch.tensor(c, dtype=torch.long)
        masque[r, L - len(c):] = 1
    positions = (masque.cumsum(dim=1) - 1).clamp(min=0)
    empreintes = [hashlib.sha256() for _ in range(B)]
    nouveaux: list[list[int]] = [[] for _ in range(B)]
    actives = [True] * B
    echecs: dict[int, str] = {}
    passes = manquants = 0
    poignee = Crochets(moteur.modele, capture["couches"], lignes=lignes_cap) if lignes_cap else contextlib.nullcontext()
    with torch.no_grad(), poignee as crochets:
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
                empreintes[r].update(logits[r].contiguous().numpy().tobytes())
                if r in choix:
                    c = choix[r]
                    j = None
                    if r not in echecs:
                        try:
                            j = int(c.choisir(pas, logits[r]))
                        except (rg.Contradiction, rg.NonResolu, rg.DureeEpuisee) as x:
                            echecs[r] = f"{type(x).__name__} : {x}"
                    if j is None:
                        j = int(fins_defaut[r]) if (c.a_fin and pas == c.n - 1) else int(remplissage)
                elif pas < len(forces[r]):
                    j = int(forces[r][pas])
                    if r in mesures:
                        mesures[r].mesurer(pas, logits[r], j)
                else:
                    j, manquants = int(pad_id), manquants + 1
                nouveaux[r].append(j)
                jetons[r, 0] = j
                if j in fins or len(nouveaux[r]) >= int(longueurs[r]):
                    actives[r] = False
            if not any(actives) or pas == max_nouveaux - 1:
                break
            masque = torch.cat([masque, torch.ones((B, 1), dtype=torch.long)], dim=1)
            sortie = moteur.pas(jetons, masque, suivante, sortie)
            suivante = suivante + 1
            passes += 1
        brut = crochets.vider_lot() if lignes_cap else None
    plan = {"longueur_remplie": L, "passes_decodage": passes, "remplissage": [L - len(c) for c in contextes],
            "empreintes_logits": [h.hexdigest() for h in empreintes], "jetons_manquants": manquants, "echecs": echecs,
            "captures": {}}
    for k, b in enumerate(lignes_cap):
        acts = relire_crochets_lot(brut, k, len(contextes[b]), plan, len(nouveaux[b]))
        plan["captures"][b] = empreinte_tableaux(acts)
    return nouveaux, plan


def passes_de_la_forme(longueurs: list[int], max_nouveaux: int) -> int:
    """Passes de décodage de `generer_lot` quand chaque ligne a exactement `longueurs[r]` jetons : la plus longue moins
    un (la dernière passe n'est pas faite)."""
    return min(max(int(x) for x in longueurs), int(max_nouveaux)) - 1


def rejouer_lot_multi(moteur: rl.MoteurLot, voc: rg.Vocabulaire, fmt, lignes: list, T: int, tirages,
                      reglages: rg.Reglages, mesurer: bool = True, captures_voulues=(), couches=None) -> dict:
    """Les T pas d'un lot de P3 rejoués comme `jouer_episodes` (N = 1). Lignes à `ids` None : cibles (choix contraint ;
    `tirages(b, t)` rend les tirages exponentiels (n, V) de l'action t de la ligne b) ; autres lignes : forcées (exactes :
    leurs identifiants ; approchées : `forcee_approchee`). Une cible en échec à l'action t est approchée pour les actions
    suivantes (forme gardée). `captures_voulues` : couples (ligne, pas) recapturés. Rend, par cible, les identifiants
    retrouvés et l'empreinte de trajectoire (ou l'échec et sa cause), les plans par pas (format de `resolution_graine_lot_v1`
    pour `mesure_des_voisines`), les empreintes de capture {(ligne, pas) : empreinte} et les journaux de pas des cibles."""
    B = len(lignes)
    pad = rl.pad_du_format(fmt)
    fins = {int(x) for x in fmt.fins}
    remp = remplissage_ordinaire(voc)
    cibles = [b for b, x in enumerate(lignes) if x.ids is None]
    for b, x in enumerate(lignes):
        if x.ids is None and x.source != SOURCE_CIBLE:
            raise GardeArret(f"ligne {b} ({x.episode}) sans identifiants hors des cibles")
        if x.ids is not None and not x.exacte and (not isinstance(x, LigneLotV2) or x.remplissage != remp):
            raise GardeArret(f"ligne approchée {b} ({x.episode}) sans le remplissage ordinaire")
    captures_voulues = {(int(b), int(t)) for b, t in captures_voulues}
    if captures_voulues and not couches:
        raise GardeArret("captures demandées sans couches")
    envs = [x.fabrique_env() for x in lignes]
    trs: list[list[int]] = [[] for _ in range(B)]
    debuts: list = [None] * B
    fins_defaut: list = [None] * B
    journaux: list[list] = [[] for _ in range(B)]
    trouves: dict[int, list] = {b: [] for b in cibles}
    echecs: dict[int, dict] = {}
    pas_journal: dict[int, list] = {b: [] for b in cibles}
    compteurs = {b: rg.Compteurs(plafond_balayages=int(reglages.balayages_max)
                                 * sum(y.count(rg.FFFD) for y in lignes[b].textes)) for b in cibles}
    plans, captures = [], {}
    for t in range(T):
        exiger_sans_signal(f"lot fidèle à plusieurs cibles, pas {t}")
        contextes = []
        for b in range(B):
            obs = envs[b].observation(0, t, journaux[b])
            if t == 0:
                debuts[b] = (envs[b].consigne_privee(0), obs)
                fins_defaut[b] = rl.fin_par_defaut(fmt, debuts[b])
                contextes.append(fmt.ouverture(*debuts[b]))
            else:
                contextes.append(trs[b] + fmt.tour(debuts[b], obs))
        longueurs = [int(x.jetons[t]) for x in lignes]
        forces: list = [None] * B
        choix: dict = {}
        for b, x in enumerate(lignes):
            if b in cibles and b not in echecs:
                n, a_fin = int(x.jetons[t]), int(x.jetons[t]) - int(x.jetons_notes[t])
                choix[b] = rl.ChoixCible(voc, x.textes[t], n, a_fin, tirages(b, t), reglages, t, None, pas_journal[b],
                                         compteurs[b])
            elif b in cibles:
                if x.base_nv is None:
                    raise GardeArret(f"cible {b} ({x.episode}) en échec sans découpage de base (forme non gardable)")
                forces[b] = forcee_approchee(x.base_nv[t], x.jetons[t], x.jetons_notes[t], remp, fins_defaut[b], fins)
            else:
                forces[b] = x.forcee(t, pad, fins_defaut[b], fins)
        mes = {}
        if mesurer:
            for b, x in enumerate(lignes):
                if b not in cibles and x.exacte and x.graines is not None:
                    mes[b] = rl.MesureLigne(voc, x.textes[t], int(x.jetons[t]), int(x.jetons[t]) - int(x.jetons_notes[t]),
                                            int(x.graines[t]), reglages.temperature)
        cap = {"lignes": [b for b in range(B) if (b, t) in captures_voulues], "couches": couches}
        nouveaux, plan = generer_lot_multi(moteur, contextes, reglages.max_nouveaux, fins, pad, forces, longueurs, choix,
                                           t, mes, cap, remp, fins_defaut)
        for b, emp in plan["captures"].items():
            captures[(b, t)] = emp
        for b in list(choix):
            if b in plan["echecs"]:
                echecs[b] = {"pas": t, "cause": plan["echecs"][b]}
                continue
            try:
                nv = choix[b].terminer()
                if nouveaux[b] != nv:
                    raise GardeArret(f"pas {t} : jetons du lot ≠ jetons choisis (ligne {b})")
                if fmt.tok.decode(nv, skip_special_tokens=True) != lignes[b].textes[t]:
                    raise rg.Contradiction(t, len(nv), "texte décodé ≠ texte stocké")
                a_fin = int(lignes[b].jetons[t]) - int(lignes[b].jetons_notes[t])
                if any(x in fins for x in nv[:len(nv) - 1]) or bool(nv and nv[-1] in fins) != bool(a_fin):
                    raise rg.Contradiction(t, len(nv), "jeton de fin mal placé")
            except rg.Contradiction as c:
                echecs[b] = {"pas": t, "cause": f"Contradiction : {c}"}
                continue
            trouves[b].append(nv)
        lc_ = [len(c) for c in contextes]
        plans.append({"pas": t, "longueur_remplie": plan["longueur_remplie"], "passes_decodage": plan["passes_decodage"],
                      "passes_de_la_forme": passes_de_la_forme(longueurs, reglages.max_nouveaux),
                      "jetons_manquants": plan["jetons_manquants"], "empreintes_logits": plan["empreintes_logits"],
                      "longueurs_contextes": lc_, "echecs": {str(b): v for b, v in plan["echecs"].items()},
                      "mesure_voisines": [{"rang": b, "episode": lignes[b].episode, "pas": m.pas,
                                           "hors_candidats": m.hors_candidats, "non_mesures_fffd": m.non_mesures_fffd}
                                          for b, m in sorted(mes.items())]})
        for b in range(B):
            trs[b] = contextes[b] + nouveaux[b] + fmt.cloture(debuts[b], nouveaux[b])
            journaux[b].append((0, t, lignes[b].textes[t]))
    sortie = {}
    for b in cibles:
        x = lignes[b]
        d = {"rang": b, "episode": x.episode, "ids": None, "empreinte": None, "echec": echecs.get(b),
             "pas": pas_journal[b], "balayages": compteurs[b].balayages}
        if b not in echecs:
            rec = rg.transcription(fmt, x.fabrique_env(), T, x.textes, trouves[b], x.jetons, x.jetons_notes)
            d.update(ids=trouves[b], empreinte=empreinte_trajectoire(episode_harnais(x.episode, T, rec)))
        sortie[b] = d
    return {"cibles": sortie, "plans": plans, "captures": captures}


# --------------------------------------------------------------------------------------------------------------------
# Lecture du témoin (gelée)


def lire_temoin(plans: list[dict], captures: dict, captures_p3: dict) -> dict:
    """Lecture gelée d'un lot témoin : mesure des voisines (`mesure_des_voisines`, seuil 1) ; captures recapturées contre
    celles de P3 (`captures_p3` : {(ligne, pas) : empreinte}) ; forme (passes égales à celles de la forme de P3, aucun
    jeton manquant). « exact » si accord = 1 et égalité des choix contraints = 1 (quand mesurés) exactement, aucun jeton
    connu hors des candidats, toutes les captures égales (chacune présente), forme égale ; « sans mesure » si aucun pas
    n'est mesuré ; « non exact » sinon."""
    m = rl.mesure_des_voisines(plans, 1.0)
    differentes = sorted(f"{b},{t}" for (b, t), e in captures_p3.items() if captures.get((b, t)) != e)
    en_trop = sorted(f"{b},{t}" for (b, t) in captures if (b, t) not in captures_p3)
    forme = all(p["passes_decodage"] == p["passes_de_la_forme"] and p["jetons_manquants"] == 0 for p in plans)
    sortie = {"mesure": {k: m[k] for k in ("pas", "accord", "accord_attendu_graine_independante", "pas_informatifs",
                                           "accord_informatifs", "contraints_mesures", "egalite_contraints",
                                           "hors_candidats", "non_mesures_fffd")},
              "par_ligne": m["par_ligne"], "captures": {"attendues": len(captures_p3),
                                                        "egales": len(captures_p3) - len(differentes),
                                                        "differentes": differentes, "en_trop": en_trop},
              "forme_egale": forme}
    if not m["pas"]:
        sortie["lecture"] = LECTURE_SANS
    elif (m["accord"] == 1.0 and m["egalite_contraints"] in (None, 1.0) and m["hors_candidats"] == 0
          and not differentes and not en_trop and forme):
        sortie["lecture"] = LECTURE_EXACT
    else:
        sortie["lecture"] = LECTURE_NON_EXACT
    return sortie


def lecture_globale_temoin(lectures: list[str]) -> str:
    """« exact » seulement si chaque lot témoin est « exact » ; aucun lot, ou un lot « sans mesure » : « sans mesure »."""
    if not lectures or any(x == LECTURE_SANS for x in lectures):
        return LECTURE_SANS
    return LECTURE_EXACT if all(x == LECTURE_EXACT for x in lectures) else LECTURE_NON_EXACT


def voie_de_reparation(lecture_temoin: str) -> str:
    """Écrit d'avance (v3, arbitrage M7) : témoin « exact » → lot fidèle ; « non exact » → lot fidèle aussi (lot, repli,
    passe forcée) ; « sans mesure » : arrêt."""
    if lecture_temoin == LECTURE_EXACT:
        return VOIE_LOT
    if lecture_temoin == LECTURE_NON_EXACT:
        return VOIE_SI_NON_EXACT
    raise GardeArret(f"lecture du témoin {lecture_temoin!r} : « {LECTURE_EXACT} » ou « {LECTURE_NON_EXACT} » attendue")


# --------------------------------------------------------------------------------------------------------------------
# v3, I5 : indépendance des lignes d'un lot réparé (mesure rapportée, sans effet)


def _propre(m: dict, differentes: list) -> bool | None:
    """Bloc « propre » : accord 1 et choix contraints égaux (quand mesurés), aucun jeton connu hors des candidats,
    aucune capture différente ; None si rien n'est mesuré (ni pas ni capture)."""
    if not m["pas"] and m["captures"] == 0:
        return None
    return (m["accord"] in (None, 1.0) and m["egalite_contraints"] in (None, 1.0) and m["hors_candidats"] == 0
            and not differentes)


def mesure_independance(plans: list[dict], captures: dict, cap_p3: dict, cibles: dict, empreintes_p3: dict) -> dict:
    """Point I5 de la contre-lecture R2 (v3) : dans l'essai à plusieurs cibles d'un lot réparé, accord des lignes
    connues (mesure des voisines, seuil 1) et captures d'équivalence recapturées contre celles de P3, **séparés avant
    et après la première action en échec d'une cible** (`t_e` = plus petit pas d'échec localisé ; « après » = pas
    ≥ `t_e`). `cibles` : sortie `cibles` de `rejouer_lot_multi` ; `empreintes_p3` : {rang : empreinte de P3}. Une cible
    sans échec localisé mais d'empreinte non retrouvée est déclarée par son rang (`non_retrouvees_sans_echec`) :
    son premier écart n'est pas localisable. Deux réserves **descriptives** (critères gelés de l'addendum) :
    `reserve_independance` (avant propre, après non propre) et `reserve_lecture_exact` (aucune cible non retrouvée
    dans le lot et lignes connues non propres). Aucune entrée, aucune classe, aucune voie ne dépend de cette mesure."""
    pas_echec = sorted(int(d["echec"]["pas"]) for d in cibles.values() if d.get("echec"))
    t_e = pas_echec[0] if pas_echec else None
    sans_echec = sorted(int(b) for b, d in cibles.items() if not d.get("echec")
                        and d.get("empreinte") != empreintes_p3[b])

    def bloc(ps: list, dedans) -> dict:
        m = rl.mesure_des_voisines(ps, 1.0)
        caps = {k: v for k, v in captures.items() if dedans(k[1])}
        diff = sorted(f"{b},{t}" for (b, t), v in caps.items() if cap_p3.get((b, t)) != v)
        s = {"pas_mesures": m["pas"], "accord": m["accord"], "egalite_contraints": m["egalite_contraints"],
             "hors_candidats": m["hors_candidats"], "captures": len(caps), "captures_differentes": diff}
        s["propre"] = _propre({"pas": m["pas"], "captures": len(caps), "accord": m["accord"],
                               "egalite_contraints": m["egalite_contraints"], "hors_candidats": m["hors_candidats"]},
                              diff)
        return s

    tout = bloc(plans, lambda t: True)
    if t_e is None:
        avant, apres = tout, None
    else:
        avant = bloc([p for p in plans if p["pas"] < t_e], lambda t: t < t_e)
        apres = bloc([p for p in plans if p["pas"] >= t_e], lambda t: t >= t_e)
    en_echec = bool(pas_echec) or bool(sans_echec)
    return {"premier_echec_pas": t_e, "cibles_en_echec_localise": len(pas_echec),
            "non_retrouvees_sans_echec": sans_echec, "tout": tout, "avant": avant, "apres": apres,
            "reserve_independance": bool(t_e is not None and avant["propre"] is not False
                                         and apres["propre"] is False),
            "reserve_lecture_exact": bool(not en_echec and tout["propre"] is False)}


# --------------------------------------------------------------------------------------------------------------------
# Pièces : captures de P3, épisodes connus, cibles


def captures_de_p3(chemin_fiches, sha_attendue: str | None, pieces: rg.Pieces, T: int, fraction: float) -> dict:
    """{épisode : {pas : empreinte de capture}} lus dans les fiches de P3 (clés permises seulement : `actions` et
    `empreintes_capture` d'`equivalence`) ; l'échantillon de chaque épisode est **recalculé** depuis les graines de P3
    (`g.random(T) < fraction_equivalence`, après `graines_des_actions`, comme `jouer_p3`) et doit égaler `actions` (R5)."""
    from ..environnements.pilote_a import graines_des_actions

    sha = verifier(chemin_fiches)
    if sha_attendue is not None and sha != sha_attendue:
        raise GardeArret(f"{chemin_fiches} : empreinte {sha[:12]} ≠ empreinte citée {sha_attendue[:12]}")
    fiches = json.loads(Path(chemin_fiches).read_text(encoding="utf-8"))["resultat"]["fiches"]
    sortie = {}
    for f in fiches:
        e = f["episode"]
        eq = f.get("equivalence") or {}
        actions = list(eq.get("actions") or [])
        emp = eq.get("empreintes_capture") or {}
        if sorted(emp) != sorted(actions):
            raise GardeArret(f"{e} : empreintes de capture ≠ actions d'équivalence dans les fiches de P3")
        g = generateur(pieces.manifeste_p3["graines"][f"tache/{f['tache']}"])
        graines_des_actions(g, 1, T)
        tirages = g.random(T)
        attendues = sorted(f"0,{s}" for s in range(T) if tirages[s] < float(fraction))
        if attendues != sorted(actions):
            raise GardeArret(f"{e} : échantillon d'équivalence recalculé {attendues} ≠ fiches {sorted(actions)}")
        sortie[e] = {int(k.split(",")[1]): str(v) for k, v in emp.items()}
    return sortie


def charger_table_v3_citee(config: dict, racine: Path) -> tuple[dict, str]:
    chemin = Path(racine) / config["chemin_table_v3"]
    t = rg.charger_table_v3(chemin, config["table_v3_sha256"])
    return t, verifier(chemin)


def connus_v4(pieces: rg.Pieces, fmt, T: int, classement: dict, table_v3: dict) -> dict:
    """Épisodes à identifiants connus : base identique, ou entrée corrigée de la table v3 appliquée
    (`appliquer_entree_v3`) et revérifiée par l'empreinte de P3 (arrêt sinon). {épisode : (identifiants, source)}."""
    sortie = {e: ([list(a) for a in c["base_nv"]], "identique_base") for e, c in classement.items() if c["identique_base"]}
    for ent in table_v3["episodes"]:
        if ent["methode"] == "non_resolu":
            continue
        e = ent["episode"]
        ep = rg.EpisodeP3(pieces, e, T)
        rec = rg.appliquer_entree_v3(fmt, ep.env(), T, ep.lignes, ep.jetons, ep.jetons_notes, ent)
        if empreinte_trajectoire(episode_harnais(e, T, rec)) != ep.empreinte:
            raise GardeArret(f"{e} : l'entrée de la table v3 ne redonne pas l'empreinte de P3")
        sortie[e] = ([list(a["nv"]) for a in rec["actions"]], f"table_v3:{ent['methode']}")
    return sortie


def cibles_v4(classement: dict, table_v3: dict) -> list[str]:
    """Cibles : épisodes dont la trajectoire de base diffère de P3 et absents de la table v3 (les non entièrement
    conformes en longueur), dans l'ordre du run."""
    dans_v3 = {x["episode"] for x in table_v3["episodes"]}
    return [e for e, c in classement.items() if not c["identique_base"] and e not in dans_v3]


def lignes_du_lot_v2(pieces: rg.Pieces, T: int, lot: list[str], connus: dict, cibles: set, base_nv: dict,
                     remplissage: int) -> list[LigneLotV2]:
    """Lignes d'un lot : connues (exactes, avec leurs graines) ; cibles (sans identifiants) ; toute autre ligne : refus."""
    sortie = []
    for e in lot:
        ep = rg.EpisodeP3(pieces, e, T)
        if e in cibles:
            ids, source, exacte = None, SOURCE_CIBLE, True
        elif e in connus:
            ids, source, exacte = [list(x) for x in connus[e][0]], str(connus[e][1]), True
        else:
            raise GardeArret(f"{e} : ni connu ni cible dans le lot")
        sortie.append(LigneLotV2(e, ep.env, ep.textes, ep.jetons, ep.jetons_notes, ids, source, exacte,
                                 list(ep.graines), remplissage, [list(a) for a in base_nv[e]]))
    return sortie


# --------------------------------------------------------------------------------------------------------------------
# Configuration et gardes


def empreinte_config(config: dict) -> str:
    return rg.empreinte_config(config)


def exiger_config(config: dict) -> None:
    """Configuration : celle du cœur (`rg.exiger_config`, `rg.exiger_reglages_execution`), plus les clés v2 :
    table v3 citée (chemin, empreinte en mode réel), lots témoins (entiers distincts, au moins un), lots d'abord,
    comptes attendus (entiers ou null en jouet seulement), bornes du lot, `capture_equivalence` booléen,
    `voie_si_temoin_non_exact` = « lot_fidele » exactement (règle écrite d'avance ; v3, arbitrage M7)."""
    rg.exiger_config({k: v for k, v in config.items() if k in rg.CLES})
    rg.exiger_reglages_execution(config)
    manquantes = [k for k in CLES_V2 if k not in config]
    if manquantes:
        raise GardeArret(f"configuration de la réparation v4 incomplète : {manquantes}")
    reel = config["mode"] == "reel"
    if not config["chemin_table_v3"] or (reel and not config["table_v3_sha256"]):
        raise GardeArret("table v3 : chemin (et empreinte en mode réel) obligatoires")
    for k in ("lots_temoin", "lots_d_abord"):
        v = config[k]
        if not isinstance(v, list) or len(set(v)) != len(v) or any(isinstance(x, bool) or not isinstance(x, int)
                                                                    or x < 0 for x in v):
            raise GardeArret(f"{k} : liste d'entiers ≥ 0 sans doublon attendue")
    if not config["lots_temoin"]:
        raise GardeArret("lots_temoin : au moins un lot")
    for k in ("cibles_attendues", "lots_cibles_attendus"):
        v = config[k]
        if v is None and not reel:
            continue
        if isinstance(v, bool) or not isinstance(v, int) or v < 1:
            raise GardeArret(f"{k} = {v!r} : entier ≥ 1 attendu (null en jouet seulement)")
    c = config["combinaisons_max_lot"]
    if isinstance(c, bool) or not isinstance(c, int) or c < 0:
        raise GardeArret(f"combinaisons_max_lot = {c!r} : entier ≥ 0 attendu")
    for k in ("duree_max_episode_lot_s", "duree_max_lot_s", "seuil_lecture_lot"):
        if isinstance(config[k], bool) or not isinstance(config[k], (int, float)):
            raise GardeArret(f"{k} = {config[k]!r} : nombre attendu")
    if not 0 < config["duree_max_episode_lot_s"] <= config["duree_max_lot_s"]:
        raise GardeArret("duree_max_episode_lot_s > 0 et ≤ duree_max_lot_s attendus")
    if not 0 <= config["seuil_lecture_lot"] <= 1:
        raise GardeArret("seuil_lecture_lot dans [0, 1] attendu")
    if not isinstance(config["capture_equivalence"], bool):
        raise GardeArret("capture_equivalence : booléen attendu")
    if config["voie_si_temoin_non_exact"] != VOIE_SI_NON_EXACT:
        raise GardeArret(f"voie_si_temoin_non_exact = {config['voie_si_temoin_non_exact']!r} : « {VOIE_SI_NON_EXACT} » "
                         "exactement (règle écrite d'avance)")


def exiger_execution_unique(racine: Path, config: dict, etape: str) -> None:
    """R3 : une seule exécution de chaque étape par configuration (tout manifeste de même commande et même empreinte de
    configuration arrête avant tout calcul)."""
    commande, sha = f"{COMMANDE} --etape {etape}", empreinte_config(config)
    for chemin in sorted((Path(racine) / "runs").glob("*/manifeste.json")):
        try:
            m = json.loads(chemin.read_text(encoding="utf-8"))
        except (OSError, ValueError) as e:
            raise GardeArret(f"R3 : manifeste illisible {chemin} ({e}) : unicité de l'étape non vérifiable")
        if m.get("commande") == commande and m.get("config_sha256") == sha:
            raise GardeArret(f"R3 : étape « {etape} » déjà exécutée sous cette configuration (run {m.get('run_id')})")


def exiger_temoin(racine: Path, chemin, config: dict) -> dict:
    """Résultat scellé de l'étape « temoin », rattaché à son manifeste, même configuration, même code (arbre gelé), sans
    `arret.json` ; sa lecture doit être « exact » ou « non exact ». Rend {lecture, voie, chemin, sha256}."""
    if not chemin:
        raise GardeArret("étape « reparation » sans --temoin : le résultat scellé du témoin est obligatoire")
    corps = verifier_resultat(racine, chemin)
    m, _ = lire_manifeste(Path(racine) / "runs" / corps["run_id"] / "manifeste.json")
    r = corps["resultat"]
    if r.get("etape") != ETAPE_TEMOIN or r.get("version") != VERSION:
        raise GardeArret(f"témoin {chemin} : étape {r.get('etape')!r}, version {r.get('version')!r}")
    if (Path(racine) / "diag" / corps["run_id"] / "arret.json").exists():
        raise GardeArret(f"témoin {corps['run_id']} arrêté (arret.json) : réparation non lancée")
    if m["config_sha256"] != empreinte_config(config):
        raise GardeArret("témoin fait sous une autre configuration")
    rg.exiger_meme_code(racine, m["commit"])
    lecture = r.get("lecture")
    return {"lecture": lecture, "voie": voie_de_reparation(lecture), "chemin": str(chemin), "sha256": verifier(chemin)}


def exiger_comptes_attendus(config: dict, cibles: list, lots_a_cible: list) -> None:
    """Avant tout calcul de la réparation : cibles et lots à cible recalculés (classement de base, table v3) égaux aux
    comptes de la configuration (89 et 28 en réel ; null en jouet : non vérifiés) ; aucune cible : arrêt (déclaré)."""
    for k, attendu in (("cibles_attendues", len(cibles)), ("lots_cibles_attendus", len(lots_a_cible))):
        if config[k] is not None and int(config[k]) != attendu:
            raise GardeArret(f"{k} = {config[k]} ≠ {attendu} trouvés (classement de base et table v3) : arrêt avant "
                             "tout calcul")
    if not cibles:
        raise GardeArret("aucune cible : réparation sans objet (arrêt, déclaré)")


def _prereg(config: dict, racine: Path, prereg: str | None, entropie_essai: int | None) -> int | None:
    if config["mode"] == "reel" and prereg is None:
        raise GardeArret("réparation réelle sans préenregistrement : R1 interdit de lancer")
    if prereg is None:
        return entropie_essai
    from ..harnais.validation_reelle import ENTROPIE_CITEE, exiger_code_cite

    texte = Path(prereg).read_text(encoding="utf-8")
    if CONFIG_CITEE.format(empreinte_config(config)) not in texte:
        raise GardeArret(f"{prereg} ne cite pas la configuration de la réparation {empreinte_config(config)[:12]}")
    e = ENTROPIE_CITEE.search(texte)
    if not e:
        raise GardeArret(f"{prereg} ne cite pas l'entropie")
    exiger_code_cite(racine, Path(prereg))
    return int(e.group(1))


# --------------------------------------------------------------------------------------------------------------------
# Étapes


@dataclass
class Contexte:
    pieces: rg.Pieces
    fmt: object
    modele: object
    voc: rg.Vocabulaire
    T: int
    classement: dict
    table_v3: dict
    table_v3_sha: str
    connus: dict
    cibles: list
    lots: list
    captures_p3: dict
    remplissage: int


def _contexte(config: dict, racine: Path, etat: dict) -> Contexte:
    from ..environnements.pilote_a import charger_taches

    T = int(config["T"])
    pieces = rg.charger_pieces(config, racine)
    rl.exiger_meme_lot_que_p3(config, pieces.manifeste_p3)
    etat["etape"] = "modèle"
    modele, fmt = rg._modele(config, racine, pieces)
    e0 = rg.EpisodeP3(pieces, next(iter(pieces.par_episode)), T).env()
    rg.exiger_ouverture(fmt, e0, config["agent"].get("texte_attendu_ouverture"), config["mode"] == "reel")
    voc = rg.Vocabulaire(fmt.tok, fmt.fins, int(modele.config.vocab_size))
    etat["etape"] = "classement"
    classement = rg.classer(pieces, fmt, T)
    table_v3, sha_v3 = charger_table_v3_citee(config, racine)
    for k in ("textes_sha256", "fiches_sha256", "scores_sha256"):
        if config[k] is not None and table_v3.get(k) != config[k]:
            raise GardeArret(f"table v3 calculée sur d'autres pièces ({k})")
    connus = connus_v4(pieces, fmt, T, classement, table_v3)
    cibles = cibles_v4(classement, table_v3)
    inconnus = [e for e in classement if e not in connus and e not in cibles]
    if inconnus:
        raise GardeArret(f"épisodes ni connus ni cibles (entrée non_resolu de la table v3 ?) : {inconnus[:3]}")
    taille = int(pieces.manifeste_p3["config"]["lot"])
    lots = rl.plan_des_lots(charger_taches(Path(racine) / config["chemin_taches"]), taille, pieces.lignes)
    fraction = float(pieces.manifeste_p3["config"].get("fraction_equivalence", 0.0))
    captures = captures_de_p3(Path(racine) / config["chemin_fiches"], config["fiches_sha256"], pieces, T, fraction) \
        if config["capture_equivalence"] else {}
    return Contexte(pieces, fmt, modele, voc, T, classement, table_v3, sha_v3, connus, cibles, lots, captures,
                    remplissage_ordinaire(voc))


def _couches_p3(ctx: Contexte) -> list[int]:
    return [int(c) for c in ctx.pieces.manifeste_p3["config"]["couches"]]


def _captures_du_lot(ctx: Contexte, lot: list[str]) -> dict:
    return {(b, t): emp for b, e in enumerate(lot) for t, emp in (ctx.captures_p3.get(e) or {}).items()}


def _executer_temoin(config, racine, run_id, chemin_m, etat, debut) -> dict:
    from ..harnais.modeles import regler_determinisme
    from ..harnais.validation_reelle import noyau
    from .rejeu_activations_v1 import progres

    reel = config["mode"] == "reel"
    reglages_det = regler_determinisme(config["fils"], "cuda" if reel else "cpu")
    environnement = rg.environnement_d_execution(reel)
    reserves = rg.reserves_environnement(environnement, reel)
    ctx = _contexte(config, racine, etat)
    etat["equivalence_tirage"] = rg.exiger_equivalence_tirage(ctx.voc.V)
    reglages = rg.reglages_de(config, None)
    moteur = rl.MoteurLot(ctx.modele)
    par_lot = []
    etat["etape"] = ETAPE_TEMOIN
    with noyau(config["noyau_attention"]):
        for k in config["lots_temoin"]:
            if not 0 <= k < len(ctx.lots):
                raise GardeArret(f"lot témoin {k} hors du plan ({len(ctx.lots)} lots)")
            lot = ctx.lots[k]
            pas_connus = [e for e in lot if e not in ctx.connus]
            if pas_connus:
                raise GardeArret(f"lot témoin {k} : épisodes sans identifiants connus {pas_connus[:3]} : refus")
            lignes = lignes_du_lot_v2(ctx.pieces, ctx.T, lot, ctx.connus, set(), {e: ctx.classement[e]["base_nv"]
                                                                                  for e in lot}, ctx.remplissage)
            cap_p3 = _captures_du_lot(ctx, lot)
            passes0 = moteur.passes
            r = rejouer_lot_multi(moteur, ctx.voc, ctx.fmt, lignes, ctx.T, None, reglages, True, set(cap_p3),
                                  _couches_p3(ctx))
            lec = lire_temoin(r["plans"], r["captures"], cap_p3)
            par_lot.append({"lot": k, "episodes": lot, "sources": [x.source for x in lignes],
                            "passes": moteur.passes - passes0, **lec,
                            "plans": [{c: v for c, v in p.items() if c != "mesure_voisines"} for p in r["plans"]]})
            progres(etape=ETAPE_TEMOIN, lot=k, lecture=lec["lecture"].replace(" ", "_"), pas=lec["mesure"]["pas"],
                    accord=lec["mesure"]["accord"], captures=f"{lec['captures']['egales']}/{lec['captures']['attendues']}")
    lecture = lecture_globale_temoin([x["lecture"] for x in par_lot])
    if lecture == LECTURE_SANS:
        raise GardeArret("témoin sans mesure : aucun pas mesuré (refus, le témoin doit mesurer)")
    resultat = {"etape": ETAPE_TEMOIN, "version": VERSION, "regle": REGLE, "run_source": config["run_source"],
                "lots_temoin": config["lots_temoin"], "lots": par_lot, "lecture": lecture,
                "voie_ecrite_d_avance": voie_de_reparation(lecture), "passes": moteur.passes,
                "jetons_en_passe": moteur.jetons, "table_v3_sha256": ctx.table_v3_sha,
                "equivalence_tirage": etat["equivalence_tirage"], "reglages": reglages_det, "modele": config["agent"],
                "noyau_attention": config["noyau_attention"], "environnement": environnement,
                "environnement_p3": rg.ENVIRONNEMENT_P3, "reserves": reserves,
                "duree_s": round(rg.horloge() - debut, 1)}
    ecrire_resultat(racine, chemin_m, f"resolution-graine-lot-v3-{ETAPE_TEMOIN}", resultat)
    progres(etape="fin", lecture=lecture.replace(" ", "_"), voie=resultat["voie_ecrite_d_avance"])
    return resultat


def _ordre_des_lots(lots_a_cible: list[int], d_abord: list[int]) -> list[int]:
    return [k for k in d_abord if k in lots_a_cible] + [k for k in lots_a_cible if k not in d_abord]


def _par_condition(episodes: list[str], pieces: rg.Pieces) -> dict:
    sortie: dict = {}
    for e in episodes:
        c = pieces.lignes[pieces.par_episode[e][0]]["condition"]
        sortie[c] = sortie.get(c, 0) + 1
    return dict(sorted(sortie.items()))


def _executer_reparation(config, racine, run_id, chemin_m, etat, debut, temoin) -> dict:
    from ..harnais.modeles import regler_determinisme
    from ..harnais.validation_reelle import noyau
    from .rejeu_activations_v1 import progres

    reel = config["mode"] == "reel"
    reglages_det = regler_determinisme(config["fils"], "cuda" if reel else "cpu")
    environnement = rg.environnement_d_execution(reel)
    reserves = rg.reserves_environnement(environnement, reel)
    ctx = _contexte(config, racine, etat)
    T, voc = ctx.T, ctx.voc
    etat["equivalence_tirage"] = rg.exiger_equivalence_tirage(voc.V)
    ordre = {e: (k, lot.index(e)) for k, lot in enumerate(ctx.lots) for e in lot}
    cibles = sorted(ctx.cibles, key=lambda e: ordre[e])
    lots_a_cible = sorted({ordre[e][0] for e in cibles})
    exiger_comptes_attendus(config, cibles, lots_a_cible)
    voie = temoin["voie"]
    if voie != VOIE_LOT:                                                                                         # v3
        raise GardeArret(f"voie {voie!r} : « {VOIE_LOT} » seule voie de la réparation v3 (arbitrage M7)")
    echeance = debut + float(config["duree_max_lot_s"])
    reglages = rg.reglages_de(config, echeance, float(config["duree_max_episode_lot_s"]))
    cmax = int(config["combinaisons_max_lot"])
    moteur_lot = rl.MoteurLot(ctx.modele)
    moteur_passe = rg.Moteur(ctx.modele)
    connus = dict(ctx.connus)
    base_nv = {e: c["base_nv"] for e, c in ctx.classement.items()}
    dossier = Path(racine) / "diag" / run_id
    dossier_eps = dossier / f"episodes-{ETAPE_REPARATION}"
    resultats: dict[str, dict] = {}
    lots_rapport = []
    etat["episodes_consignes"] = []
    etat["etape"] = ETAPE_REPARATION
    progres(etape=ETAPE_REPARATION, voie=voie, cibles=len(cibles), lots=len(lots_a_cible))

    def consigner(e, r):
        r.update(numero_lot=ordre[e][0], rang_dans_le_lot=ordre[e][1], voie_de_l_etape=voie)
        resultats[e] = r
        etat["episodes_consignes"].append(rg.consigner_episode(dossier_eps, len(etat["episodes_consignes"]), r))
        progres(etape=ETAPE_REPARATION, episodes=f"{len(resultats)}/{len(cibles)}",
                retrouves=sum(x["statut"] == "resolu" for x in resultats.values()))

    def passe_forcee(e, essais):
        ep = rg.EpisodeP3(ctx.pieces, e, T)
        Qs = [rg.tirages_exponentiels(g, n, voc.V) for g, n in zip(ep.graines, ep.jetons)]
        r = rg.resoudre_avec_repli(moteur_passe, voc, ctx.fmt, ep.env, e, T, ep.textes, ep.jetons, ep.jetons_notes, Qs,
                                   ep.empreinte, reglages, cmax)
        del Qs
        essais.append({"voie": f"passe_forcee:{r.get('voie')}", "statut": r["statut"], "cause": r.get("cause"),
                       "combinaisons_essayees": r.get("combinaisons_essayees")})
        return r

    with noyau(config["noyau_attention"]):
        for k in _ordre_des_lots(lots_a_cible, config["lots_d_abord"]):
            exiger_sans_signal(f"réparation, lot {k}")
            lot = ctx.lots[k]
            cib = [e for e in lot if e in set(cibles)]
            essais: dict[str, list] = {e: [] for e in cib}
            # v3 : une seule voie (lot, repli, passe forcée) ; la passe forcée seule de la v2 est retirée
            lignes = lignes_du_lot_v2(ctx.pieces, T, lot, connus, set(cib), base_nv, ctx.remplissage)
            graines = {b: x.graines for b, x in enumerate(lignes)}

            def tirages(b, t, _g=graines, _l=lignes):
                return rg.tirages_exponentiels(_g[b][t], int(_l[b].jetons[t]), voc.V)

            cap = set(_captures_du_lot(ctx, lot)) if config["capture_equivalence"] else set()
            passes0 = moteur_lot.passes
            r = rejouer_lot_multi(moteur_lot, voc, ctx.fmt, lignes, T, tirages, reglages, True, cap,
                                  _couches_p3(ctx) if cap else None)
            m = rl.mesure_des_voisines(r["plans"], float(config["seuil_lecture_lot"]))
            cap_p3 = _captures_du_lot(ctx, lot)
            lots_rapport.append({"lot": k, "cibles": cib, "passes": moteur_lot.passes - passes0,
                                 "forme_egale": all(p["passes_decodage"] == p["passes_de_la_forme"]
                                                    for p in r["plans"]),
                                 "mesure_voisines": {c: m[c] for c in ("pas", "accord", "egalite_contraints",
                                                                       "hors_candidats", "lecture")},
                                 "captures_egales": sorted(f"{b},{t}" for (b, t), x in r["captures"].items()
                                                           if cap_p3.get((b, t)) == x),
                                 "captures_differentes": sorted(f"{b},{t}" for (b, t), x in r["captures"].items()
                                                                if cap_p3.get((b, t)) != x),
                                 "independance_des_lignes": mesure_independance(                         # v3, I5
                                     r["plans"], r["captures"], cap_p3, r["cibles"],
                                     {b: rg.EpisodeP3(ctx.pieces, lot[b], T).empreinte for b in r["cibles"]})})
            non_retrouvees = []
            for b, d in sorted(r["cibles"].items()):
                e = lot[b]
                ep = rg.EpisodeP3(ctx.pieces, e, T)
                ok = d["empreinte"] is not None and d["empreinte"] == ep.empreinte
                essais[e].append({"voie": "lot_multi:directe", "statut": "resolu" if ok else "non_resolu",
                                  "cause": None if ok else (d["echec"] or {"cause": "empreinte de P3 non "
                                                                                   "retrouvée"})["cause"]})
                if ok:
                    connus[e] = (d["ids"], "lot_multi")
                    consigner(e, {"episode": e, "statut": "resolu", "voie": "lot_multi:directe", "ids": d["ids"],
                                  "empreinte": d["empreinte"], "empreinte_cible": ep.empreinte, "cause": None,
                                  "essais": essais[e], "fffd": sum(x.count(rg.FFFD) for x in ep.textes)})
                else:
                    non_retrouvees.append(e)
            for e in non_retrouvees:
                ep = rg.EpisodeP3(ctx.pieces, e, T)
                autres = set(non_retrouvees) - {e} - set(connus)
                lignes1 = []
                for e2 in lot:
                    ep2 = rg.EpisodeP3(ctx.pieces, e2, T)
                    if e2 == e:
                        ids, src, ex = None, SOURCE_CIBLE, True
                    elif e2 in connus:
                        ids, src, ex = [list(a) for a in connus[e2][0]], str(connus[e2][1]), True
                    elif e2 in autres:
                        ids, src, ex = [list(a) for a in base_nv[e2]], SOURCE_APPROCHEE, False
                    else:
                        raise GardeArret(f"{e2} : ligne sans statut dans le lot {k}")
                    lignes1.append(LigneLotV2(e2, ep2.env, ep2.textes, ep2.jetons, ep2.jetons_notes, ids, src, ex,
                                              list(ep2.graines), ctx.remplissage))
                Qs = [rg.tirages_exponentiels(g, n, voc.V) for g, n in zip(ep.graines, ep.jetons)]
                r1 = rl.resoudre_episode_lot(moteur_lot, voc, ctx.fmt, lignes1, lot.index(e), T, Qs, ep.empreinte,
                                             reglages, cmax, seuil_lecture=float(config["seuil_lecture_lot"]))
                del Qs
                essais[e].append({"voie": f"lot_une_cible:{r1.get('voie')}", "statut": r1["statut"],
                                  "cause": r1.get("cause"), "combinaisons_essayees": r1.get("combinaisons_essayees"),
                                  "lignes_approchees": r1.get("lignes_approchees")})
                if r1["statut"] == "resolu":
                    connus[e] = (r1["ids"], "lot_une_cible")
                    consigner(e, {"episode": e, "statut": "resolu", "voie": f"lot_une_cible:{r1['voie']}",
                                  "ids": r1["ids"], "empreinte": r1["empreinte"], "empreinte_cible": ep.empreinte,
                                  "cause": None, "essais": essais[e], "forcages": r1.get("forcages"),
                                  "fffd": r1.get("fffd")})
                    continue
                r2 = passe_forcee(e, essais[e])
                if r2["statut"] == "resolu":
                    connus[e] = (r2["ids"], "passe_forcee")
                consigner(e, {"episode": e, "statut": r2["statut"], "voie": f"passe_forcee:{r2.get('voie')}",
                              "ids": r2.get("ids"), "empreinte": r2.get("empreinte"),
                              "empreinte_cible": ep.empreinte, "cause": r2.get("cause"), "essais": essais[e],
                              "forcages": r2.get("forcages"), "fffd": r2.get("fffd"),
                              "duree_epuisee": r2.get("duree_epuisee")})
    etat["etape"] = "mesures"
    episodes = [resultats[e] for e in cibles]
    for x in episodes:
        x["empreinte_retrouvee"] = x["statut"] == "resolu" and x["empreinte"] == x["empreinte_cible"]
    retrouves = [x["episode"] for x in episodes if x["empreinte_retrouvee"]]
    resultat = {"etape": ETAPE_REPARATION, "version": VERSION, "regle": REGLE, "run_source": config["run_source"],
                "temoin": temoin, "voie": voie, "cibles": cibles, "lots_a_cible": lots_a_cible,
                "ordre_des_lots": _ordre_des_lots(lots_a_cible, config["lots_d_abord"]),
                "cibles_par_condition": _par_condition(cibles, ctx.pieces),
                "retrouves_par_condition": _par_condition(retrouves, ctx.pieces),
                "empreintes_retrouvees": len(retrouves),
                "non_resolus": [{"episode": x["episode"], "cause": x["cause"]} for x in episodes
                                if not x["empreinte_retrouvee"]],
                "par_voie": {v: sum(1 for x in episodes if x["empreinte_retrouvee"] and x["voie"].startswith(v))
                             for v in ("lot_multi", "lot_une_cible", "passe_forcee")},
                "lots_rapport": lots_rapport, "table_v3_sha256": ctx.table_v3_sha,
                "passes_lot": moteur_lot.passes, "passes_forcees": moteur_passe.passes,
                "seuils": {k: config[k] for k in ("seuil_ecart", "quasi_egalites_max", "bascules_max",
                                                  "combinaisons_max_lot", "balayages_max", "duree_max_episode_lot_s",
                                                  "duree_max_lot_s", "seuil_lecture_lot")},
                "equivalence_tirage": etat["equivalence_tirage"], "reglages": reglages_det, "modele": config["agent"],
                "noyau_attention": config["noyau_attention"], "environnement": environnement,
                "environnement_p3": rg.ENVIRONNEMENT_P3, "reserves": reserves,
                "episodes_consignes": etat["episodes_consignes"], "episodes": episodes,
                "duree_s": round(rg.horloge() - debut, 1)}
    resultat["lecture"] = ("complète" if len(retrouves) == len(cibles) else ("partielle" if retrouves else "aucune"))
    ecrire_resultat(racine, chemin_m, f"resolution-graine-lot-v3-{ETAPE_REPARATION}", resultat)
    progres(etape="fin", retrouves=f"{len(retrouves)}/{len(cibles)}", lecture=resultat["lecture"], voie=voie)
    return resultat


def executer(config: dict, racine: Path, run_id: str, prereg: str | None, etape: str, temoin: str | None = None,
             autoriser_depot_sale: bool = False, entropie_essai: int | None = None) -> dict:
    """Étapes « temoin » et « reparation ». Gardes avant tout chargement du modèle : configuration, préenregistrement
    (configuration citée, entropie, code), pièces de P3 et noyau de P3, table v3 citée, témoin scellé (réparation),
    unicité de l'étape (R3) ; puis manifeste. Tout arrêt après le manifeste écrit `arret.json` (épisodes consignés)."""
    racine = Path(racine)
    exiger_config(config)
    if etape not in ETAPES:
        raise GardeArret(f"étape {etape!r} : {ETAPES} attendues (« {ETAPE_TABLE} » : construire_table_v4)")
    entropie = _prereg(config, racine, prereg, entropie_essai)
    pieces = rg.charger_pieces(config, racine)
    rl.exiger_meme_lot_que_p3(config, pieces.manifeste_p3)
    charger_table_v3_citee(config, racine)
    tem = exiger_temoin(racine, temoin, config) if etape == ETAPE_REPARATION else None
    exiger_execution_unique(racine, config, etape)
    chemin_m, _ = creer_manifeste(racine, run_id, config, ["aucun-tirage-propre"], entropie=entropie,
                                  decisif=prereg is not None, prereg=prereg, autoriser_depot_sale=autoriser_depot_sale,
                                  commande=f"{COMMANDE} --etape {etape}")
    etat = {"etape": "chargement"}
    debut = rg.horloge()
    try:
        if etape == ETAPE_TEMOIN:
            return _executer_temoin(config, racine, run_id, chemin_m, etat, debut)
        return _executer_reparation(config, racine, run_id, chemin_m, etat, debut, tem)
    except Exception as e:
        ecrire_resultat(racine, chemin_m, "arret", {"etape": etat["etape"], "motif": motif_d_arret(e),
                                                     "partiel": {k: v for k, v in etat.items() if k != "etape"},
                                                     "duree_s": round(rg.horloge() - debut, 1)})
        relever_term_apres(e)
        raise


# --------------------------------------------------------------------------------------------------------------------
# Table v4


def entree_non_resolue(e: str, trajectoire: str, cause: str | None) -> dict:
    """Entrée « non_resolu » d'une cible non retrouvée (forme de la table v2 : aucune fin, aucune paire)."""
    ent = {"episode": e, "methode": "non_resolu", "trajectoire_p3": trajectoire, "fins": {}, "paires": [],
           "cause_v4": cause}
    rg.verifier_forme_v3(ent)
    return ent


def verifier_forme_v4(e: dict) -> None:
    """Forme d'une entrée de table version 4 : celle de la version 3 (`verifier_forme_v3`)."""
    rg.verifier_forme_v3(e)


def charger_table_v4(chemin, sha_attendue: str | None) -> dict:
    """Table version 4 scellée : empreinte du fichier = empreinte citée (si citée), version 4, méthodes connues, formes
    conformes, aucun doublon. Une table de version 1, 2 ou 3 est refusée, sa version dans le motif."""
    sha = verifier(chemin)
    if sha_attendue is not None and sha != sha_attendue:
        raise GardeArret(f"table de tokenisation {chemin} : empreinte {sha[:12]} ≠ empreinte citée {sha_attendue[:12]}")
    t = json.loads(Path(chemin).read_text(encoding="utf-8"))
    if t.get("version") != VERSION_TABLE_V4:
        raise GardeArret(f"table de tokenisation : version {t.get('version')!r} ≠ {VERSION_TABLE_V4}")
    vus = set()
    for e in t["episodes"]:
        if e["episode"] in vus:
            raise GardeArret(f"table de tokenisation : épisode {e['episode']} en double")
        vus.add(e["episode"])
        verifier_forme_v4(e)
    return t


def construire_table_v4(config: dict, racine: Path, tokeniseur: str | None, chemin_reparation: str, fmt=None) -> dict:
    """Table v4 (processeur) : table v3 citée (entrées inchangées), plus une entrée par cible du résultat scellé de la
    réparation (même configuration) : « identifiants » si l'empreinte de P3 est retrouvée (revérifiée ici avant tout
    versement), « non_resolu » sinon (cause recopiée). Refus : cibles du résultat ≠ cibles recalculées, cible résolue
    sans l'empreinte, identifiants qui ne redonnent pas l'empreinte, doublon. Toutes les corrections revérifiées
    (`verifier_entrees_v3`) ; comptes : ceux de la v3, plus `non_conformes`, `cibles_v4`, `retrouvees_v4`."""
    exiger_config(config)
    racine = Path(racine)
    pieces = rg.charger_pieces(config, racine)
    table_v3, sha_v3 = charger_table_v3_citee(config, racine)
    corps = verifier_resultat(racine, chemin_reparation)
    m, _ = lire_manifeste(racine / "runs" / corps["run_id"] / "manifeste.json")
    if m["config_sha256"] != empreinte_config(config):
        raise GardeArret("résultat de la réparation fait sous une autre configuration")
    r = corps["resultat"]
    if r.get("etape") != ETAPE_REPARATION or r.get("version") != VERSION:
        raise GardeArret(f"réparation {chemin_reparation} : étape {r.get('etape')!r}, version {r.get('version')!r}")
    if r.get("table_v3_sha256") != sha_v3:
        raise GardeArret("réparation faite sur une autre table v3")
    sha_r = verifier(chemin_reparation)
    if fmt is None and config["mode"] == "jouet":
        _, fmt = rg._modele(config, racine, pieces)
    if fmt is None:
        from transformers import AutoTokenizer

        from ..harnais.formats import FormatChat

        tok = AutoTokenizer.from_pretrained(tokeniseur)
        fmt = FormatChat(tok, variables=config["agent"]["variables_gabarit"])
        fmt.fins = {int(x) for x in table_v3["fins_du_format"]} | {fmt._pieces(("x", "y"))["cloture"][0]}
    T = int(config["T"])
    classement = rg.classer(pieces, fmt, T)
    cibles = cibles_v4(classement, table_v3)
    if sorted(r.get("cibles") or []) != sorted(cibles):
        raise GardeArret("cibles du résultat de la réparation ≠ cibles recalculées (classement de base, table v3)")
    par_e: dict = {}
    for x in r["episodes"]:
        if x["episode"] in par_e:
            raise GardeArret(f"{x['episode']} : deux entrées dans le résultat de la réparation")
        par_e[x["episode"]] = x
    if sorted(par_e) != sorted(cibles):
        raise GardeArret("épisodes du résultat de la réparation ≠ cibles")
    nouvelles = []
    for e in cibles:
        x = par_e[e]
        traj = pieces.fiches[e]["trajectoire"]
        if x.get("empreinte_cible") != traj:
            raise GardeArret(f"{e} : empreinte cible du résultat ≠ fiches de P3")
        if x.get("statut") == "resolu":
            if x.get("empreinte") != traj:
                raise GardeArret(f"{e} : « résolu » sans l'empreinte de P3 égale")
            ids = [[int(y) for y in a] for a in x["ids"]]
            ep = rg.EpisodeP3(pieces, e, T)
            rec = rg.transcription(fmt, ep.env(), T, ep.textes, ids, ep.jetons, ep.jetons_notes)
            if empreinte_trajectoire(episode_harnais(e, T, rec)) != traj:
                raise GardeArret(f"{e} : les identifiants de la réparation ne redonnent pas l'empreinte de P3 "
                                 "(revérification)")
            res = {"voie": x.get("voie"), "resultat_sha256": sha_r, "voie_de_l_etape": r.get("voie"),
                   "lecture_temoin": (r.get("temoin") or {}).get("lecture")}
            nouvelles.append(rg.entree_identifiants(e, traj, classement[e]["base_nv"], ids, res))
        else:
            nouvelles.append(entree_non_resolue(e, traj, x.get("cause")))
    episodes = list(table_v3["episodes"]) + nouvelles
    comptes = {k: v for k, v in table_v3["comptes"].items() if k not in rg.METHODES_V3 and k != "identiques_apres_table"}
    for meth in rg.METHODES_V3:
        comptes[meth] = sum(1 for x in episodes if x["methode"] == meth)
    comptes["identiques_apres_table"] = comptes["identiques_base"] + sum(comptes[meth] for meth in rg.CORRIGEES_V3)
    comptes.update(non_conformes=len(cibles), cibles_v4=len(cibles),
                   retrouvees_v4=sum(1 for x in nouvelles if x["methode"] != "non_resolu"))

    def contexte(e):
        ep = rg.EpisodeP3(pieces, e, T)
        return ep.env(), ep.lignes, ep.jetons, ep.jetons_notes, T

    n = rg.verifier_entrees_v3(episodes, fmt, contexte, pieces.fiches)
    if n != comptes["identiques_apres_table"] - comptes["identiques_base"]:
        raise GardeArret("corrections vérifiées ≠ comptes de la table v4")
    meta = {k: v for k, v in table_v3.items() if k not in ("version", "comptes", "episodes")}
    return {**meta, "version": VERSION_TABLE_V4, "regle_v4": REGLE, "table_v3_sha256": sha_v3,
            "resultat_reparation_sha256": sha_r, "voie": r.get("voie"), "temoin": r.get("temoin"),
            "comptes": comptes, "corrections_verifiees": n,
            "non_resolus_v4": [x["episode"] for x in nouvelles if x["methode"] == "non_resolu"],
            "episodes": episodes}


def ecrire_table_v4(table: dict, sortie) -> str:
    """Écrit la table version 4 (jamais par-dessus un fichier existant, R12) et la scelle ; rend son empreinte."""
    if table.get("version") != VERSION_TABLE_V4:
        raise GardeArret(f"table de version {table.get('version')!r} : 4 attendue")
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
    ap.add_argument("--etape", required=True, choices=ETAPES + (ETAPE_TABLE,))
    ap.add_argument("--config", required=True)
    ap.add_argument("--run-id")
    ap.add_argument("--prereg", default=None)
    ap.add_argument("--temoin", default=None, help="résultat scellé de l'étape temoin (étape reparation)")
    ap.add_argument("--reparation", default=None, help="résultat scellé de l'étape reparation (étape table-v4)")
    ap.add_argument("--tokeniseur", help="dossier du tokeniseur à la révision de P3 (étape table-v4)")
    ap.add_argument("--sortie", help="table version 4 à écrire (étape table-v4 ; jamais écrasée)")
    a = ap.parse_args(argv)
    signal.signal(signal.SIGTERM, lever_sur_term)
    verifier(a.config)
    config = json.loads(Path(a.config).read_text(encoding="utf-8"))
    if a.etape == ETAPE_TABLE:
        if not (a.reparation and a.sortie and (a.tokeniseur or config.get("mode") == "jouet")):
            raise GardeArret("étape table-v4 : --reparation, --sortie et --tokeniseur (mode réel) obligatoires")
        sortie = Path(a.sortie)
        if sortie.exists() or Path(f"{sortie}.sha256").exists():
            raise GardeArret(f"{sortie} existe déjà (R12 : on n'écrase jamais)")
        table = construire_table_v4(config, Path("."), a.tokeniseur, a.reparation)
        sha = ecrire_table_v4(table, sortie)
        print(json.dumps({"comptes": table["comptes"], "corrections_verifiees": table["corrections_verifiees"],
                          "voie": table["voie"], "sha256": sha}, ensure_ascii=False))
        return 0
    if not a.run_id:
        raise GardeArret("--run-id obligatoire")
    r = executer(config, Path("."), a.run_id, a.prereg, a.etape, a.temoin)
    resume = {"etape": r["etape"], "lecture": r["lecture"]}
    if r["etape"] == ETAPE_TEMOIN:
        resume["voie_ecrite_d_avance"] = r["voie_ecrite_d_avance"]
    else:
        resume.update(voie=r["voie"], empreintes_retrouvees=r["empreintes_retrouvees"], cibles=len(r["cibles"]))
    print(json.dumps(resume, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    try:
        sys.exit(_main(sys.argv[1:]))
    except GardeArret as e:
        print(f"ARRÊT : {e}", file=sys.stderr)
        sys.exit(1)
