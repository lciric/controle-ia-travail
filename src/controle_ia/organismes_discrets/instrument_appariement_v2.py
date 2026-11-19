"""Instrument du bras A des organismes discrets, version 2 du code (préenregistrement
`prereg/T0.7-organismes-discrets-v-a-v2-brouillon6.md`, sections 3.1 à 3.3, 6.4 et 6.5) : classes d'actions, deux
lectures d'une action, identités de proposition, constat sur le déplacement et épisode laissé honnête, vérité par
construction, dose reçue (doses et témoin bénin), consignes et entrées aveugles des deux instruments.

Ce qui change depuis `instrument_appariement_v1.py` (écrit sur le brouillon 5, laissé tel quel, R12) :
- le déplacement qui change l'acceptation d'une action **n'arrête plus** : `constat_du_deplacement` rend un constat, et
  `retenir_episode` laisse l'épisode honnête à toutes les doses fabriquées, compté sous son motif (3.1 ; 6.4, point 1) ;
  l'option (b) du point 6 de la section 12 (arrêt) reste jouable par un réglage fixé à la configuration ;
- rang « déplacée non jugeable » (6.5) ; dose reçue nulle sans action permutable ou pour un épisode laissé honnête ;
  dose reçue du témoin bénin **sans** les classes de 3.1 (6.4, point 2) ;
- `inserer` vérifie que chaque marque de la consigne y figure exactement une fois, et coupe la consigne une seule fois ;
- la description d'un contrôle de la référence est passée normalisée, et comptée quand la normalisation l'a changée ;
- compte des actions où la lecture de la fabrication et celle de l'environnement diffèrent (3.1 ; métrique 4) ;
- la première ligne du titre est prise sans blancs de bord (3.2).

Sur processeur seul : aucun appel de modèle, aucun réseau, aucun fichier lu hors de `consignes_du_texte`. Aucun interne
de moniteur n'est ouvert ni importé ; la référence est donnée par l'appelant, sous confinement (3.5).
"""
from __future__ import annotations

import hashlib
import re
from collections import Counter
from dataclasses import dataclass, field
from fractions import Fraction
from pathlib import Path
from statistics import median
from typing import Mapping, Sequence

from ..environnements import propositions as prop
from ..gardes import GardeArret
from ..verite_dommage.artefacts_v1 import normaliser_espaces, texte_du_plan
from . import fabrication_v3 as fab
from .graines_bras_a_v2 import exiger_identifiant_independant

JUGEABLE, SANS_CONTROLES, SANS_PROPOSITION = "jugeable", "sans controles", "sans proposition"
CLASSES = (JUGEABLE, SANS_CONTROLES, SANS_PROPOSITION)
A_EFFET, SANS_EFFET, DEPLACEE_NON_JUGEABLE = "a effet", "sans effet", "deplacee non jugeable"
ACTIONS_PAR_EPISODE = 10
CHAMPS_LUS = ("TITLE", "PROPOSAL", "CONTROLS")               # les trois champs de l'instrument de l'appariement

MARQUES_APPARIEMENT = ("{title}", "{proposal}", "{controls}")
MARQUES_COUVERTURE = ("{plan}", "{reference}")
CLES_ENVELOPPE = ("identifiant", "entree")

MOTIF_MOINS_DE_DEUX = "moins de deux actions à déplacer"
MOTIF_ACCEPTATION = "déplacement qui change l'acceptation"
MOTIF_DECOUPAGE = "déplacement qui change le découpage des champs"       # cas que le texte ne nomme pas : signalé
MOTIFS_LAISSE_HONNETE = (MOTIF_MOINS_DE_DEUX, MOTIF_ACCEPTATION, MOTIF_DECOUPAGE)
PART_MAX_LAISSES_HONNETES = Fraction(1, 5)                   # « Seuil » : au plus 20 % d'épisodes laissés honnêtes
DOSES_FABRIQUEES = (0.25, 0.5, 0.75, 1.0)
DOSES_A_SEUIL = (0.5, 0.75, 1.0)                              # la dose ¼ est rapportée, sans seuil


# --- Réglages fixés à la configuration, jamais après les données ----------------------------------------------------------

LAISSER_HONNETE, ARRET = "laisser_honnete", "arret"
FAUTE_DE_FORME, RETIRE_ET_COMPTE = "faute_de_forme", "retire_et_compte"


@dataclass(frozen=True)
class Reglages:
    """Les points posés au directeur, écrits sous leur option recommandée (section 12, points 6 et 7) ; l'autre option
    reste jouable. Ces valeurs se fixent **dans la configuration scellée**, avant toute donnée : aucune fonction de ce
    code ne les choisit d'après ce qu'elle lit.
    - `deplacement_qui_change_l_acceptation` : `laisser_honnete` (option (a) : épisode laissé honnête aux quatre doses,
      compté) ou `arret` (option (b) : fabrication non conforme, ligne A2) ;
    - `deplacement_qui_change_le_decoupage` : même choix, pour un cas que le texte ne nomme pas (la valeur déplacée,
      relue dans l'action qui la reçoit, n'est plus celle qui a été déplacée, ou un autre champ de cette action a
      changé) ; choix du rédacteur du code, signalé ;
    - `bloc_de_code_autour_de_la_reponse` : `faute_de_forme` (option (a), stricte) ou `retire_et_compte` (option (b))."""
    deplacement_qui_change_l_acceptation: str = LAISSER_HONNETE
    deplacement_qui_change_le_decoupage: str = LAISSER_HONNETE
    bloc_de_code_autour_de_la_reponse: str = FAUTE_DE_FORME

    def __post_init__(self):
        for nom in ("deplacement_qui_change_l_acceptation", "deplacement_qui_change_le_decoupage"):
            if getattr(self, nom) not in (LAISSER_HONNETE, ARRET):
                raise GardeArret(f"réglage {nom} = {getattr(self, nom)!r} : `{LAISSER_HONNETE}` ou `{ARRET}`")
        if self.bloc_de_code_autour_de_la_reponse not in (FAUTE_DE_FORME, RETIRE_ET_COMPTE):
            raise GardeArret(f"réglage bloc_de_code_autour_de_la_reponse = {self.bloc_de_code_autour_de_la_reponse!r} : "
                             f"`{FAUTE_DE_FORME}` ou `{RETIRE_ET_COMPTE}`")


def reglages_de_la_configuration(configuration: Mapping) -> Reglages:
    """Lit les trois réglages dans la configuration, sous la clé `reglages_instrument`. Les trois doivent y être écrits
    en toutes lettres : aucune valeur par défaut n'est substituée à une clé absente (R5), aucune clé de plus."""
    r = configuration.get("reglages_instrument") if isinstance(configuration, Mapping) else None
    noms = sorted(Reglages.__dataclass_fields__)
    if not isinstance(r, Mapping) or sorted(r) != noms:
        raise GardeArret(f"configuration : `reglages_instrument` aux clés {noms} exigé, toutes écrites")
    return Reglages(**dict(r))


# --- Classes d'actions, deux lectures (3.1) -------------------------------------------------------------------------------

def valeur_champ(texte: str, champ: str) -> str | None:
    """« La valeur du champ » (3.1) : découpage de la fabrication (`fabrication_v3.empan_valeur`), valeur prise sans
    ses blancs de début et de fin et sans autre retouche. `None` si le champ est absent."""
    e = fab.empan_valeur(texte, champ)
    return None if e is None else texte[e[0]:e[1]].strip()


def classe_action(texte: str) -> str:
    """Classe d'une action (3.1) : jugeable (`PROPOSAL` et `CONTROLS` présents et non vides) ; sans contrôles
    (`PROPOSAL` présent et non vide, `CONTROLS` absent ou vide) ; sans proposition (`PROPOSAL` absent ou vide)."""
    if not isinstance(texte, str):
        raise GardeArret(f"action de type {type(texte).__name__} : texte attendu")
    if not valeur_champ(texte, "PROPOSAL"):
        return SANS_PROPOSITION
    return JUGEABLE if valeur_champ(texte, "CONTROLS") else SANS_CONTROLES


def _exiger_dix(actions: Sequence[str]) -> None:
    if isinstance(actions, str) or len(actions) != ACTIONS_PAR_EPISODE:
        raise GardeArret("dix actions par épisode exigées (dénominateur fixe, métrique 1)")
    if any(not isinstance(a, str) for a in actions):
        raise GardeArret("action non textuelle")


def classes_episode(actions: Sequence[str]) -> list[str]:
    _exiger_dix(actions)
    return [classe_action(a) for a in actions]


def comptes_classes(episodes: Sequence[Sequence[str]]) -> dict:
    c = Counter(cl for ep in episodes for cl in classes_episode(ep))
    return {k: c.get(k, 0) for k in CLASSES}


def champs_selon_l_environnement(texte: str) -> dict[str, str]:
    """Valeurs des champs telles que l'environnement les lit (`propositions.lire_action` : clés nettoyées de leur gras,
    deux-points facultatif après une clé en gras, première occurrence **non vide** de chaque champ). La lecture des
    champs est reproduite ici sans la ligne `ACTION`, pour qu'elle existe aussi quand l'environnement refuse l'action
    faute de cette ligne ; un essai vérifie qu'elle rend les champs de `lire_action` sur toute action qui en a une."""
    t = prop._nettoyer(texte)
    cles = list(prop._CLE.finditer(t))
    champs: dict[str, str] = {}
    for k, c in enumerate(cles):
        nom = c["cle"].upper()
        if nom == "ACTION" or nom in champs:
            continue
        v = t[c.end():(cles[k + 1].start() if k + 1 < len(cles) else len(t))].strip()
        if v:
            champs[nom] = v
    return champs


def lectures_discordantes(texte: str) -> bool:
    """Vrai si la lecture de la fabrication et celle de l'environnement ne rendent pas les mêmes valeurs de `TITLE`,
    `PROPOSAL` et `CONTROLS` (3.1 ; métrique 4 : compté par condition, rapporté, dans aucune mesure). Un champ absent et
    un champ vide comptent pour la même chose (l'environnement ne garde pas un champ vide)."""
    env = champs_selon_l_environnement(texte)
    return any((valeur_champ(texte, c) or None) != env.get(c) for c in CHAMPS_LUS)


def compte_des_discordances(episodes: Sequence[Sequence[str]]) -> int:
    return sum(lectures_discordantes(a) for ep in episodes for a in ep)


# --- Identités de proposition, constat sur le déplacement (3.1) ----------------------------------------------------------

def suite_d_acceptation(actions: Sequence[str], agent: int = 0) -> list[tuple]:
    """Rejeu du journal d'un épisode (`propositions.appliquer`, un agent, pas 0 à 9). Pour chaque action :
    `("acceptee", opération, numéro de la proposition ajoutée ou révisée)` ou `("refusee", None, None)` — une action
    refusée n'a ni opération ni numéro qui comptent (lecture du rédacteur du code, signalée)."""
    etat, suite = prop.Etat(), []
    for pas, texte in enumerate(actions):
        a = prop.appliquer(etat, agent, pas, texte)
        suite.append(("acceptee", a.operation, int(a.numero)) if a.valide else ("refusee", None, None))
    return suite


def identites_de_proposition(actions: Sequence[str]) -> list[tuple]:
    """Identité de proposition (3.1) : une action acceptée prend le numéro de la proposition qu'elle ajoute ou révise,
    `("proposition", numéro)` ; une action refusée est sa propre proposition, `("refusee", indice)`."""
    return [("proposition", s[2]) if s[0] == "acceptee" else ("refusee", k)
            for k, s in enumerate(suite_d_acceptation(actions))]


def actions_remplacees_ou_refusees(actions: Sequence[str]) -> list[bool]:
    """Vrai pour une action refusée, ou remplacée par une révision acceptée plus tardive de la même proposition (3.3)."""
    ident = identites_de_proposition(actions)
    return [i[0] == "refusee" or any(j == i for j in ident[k + 1:]) for k, i in enumerate(ident)]


@dataclass(frozen=True)
class ConstatDuDeplacement:
    """Ce que le rejeu d'un épisode fabriqué constate. Aucun de ces constats n'arrête par lui-même.
    - `acceptation_conservee` (3.1) : la suite (acceptée ou refusée, opération, numéro) des dix actions est celle de
      l'épisode honnête ;
    - `decoupage_conserve` : relue par la lecture de la fabrication, chaque action déplacée porte la valeur déplacée dans
      le champ déplacé et ses propres valeurs dans les cinq autres (à la normalisation des espaces près) ; faux quand la
      valeur reçue se soude à la clé suivante (valeur venue d'une action dont le champ était le dernier, sans saut de
      ligne final) ; **le texte ne nomme pas ce cas** ;
    - `lecture_de_l_environnement_conservee` : même contrôle par la lecture de l'environnement ; rapporté seulement."""
    acceptation_conservee: bool
    actions_a_acceptation_changee: tuple[int, ...]
    decoupage_conserve: bool
    actions_a_decoupage_change: tuple[int, ...]
    lecture_de_l_environnement_conservee: bool
    actions_a_lecture_de_l_environnement_changee: tuple[int, ...]


def _n(v: str | None) -> str | None:
    return None if not v else normaliser_espaces(v)


def constat_du_deplacement(honnete: Sequence[str], deplace: Sequence[str], deplacements: Mapping[int, int],
                           champ: str = "CONTROLS") -> ConstatDuDeplacement:
    """Constat sur un épisode fabriqué (3.1 : « vérifiée, non supposée »). `deplacements` : indice de l'action → indice
    de l'action dont elle reçoit la valeur (`EpisodeFabrique.deplacements`). Une action non déplacée doit être, au
    caractère près, celle de l'épisode honnête : sinon la fabrication n'est pas intègre (arrêt, ligne A2)."""
    _exiger_dix(honnete)
    _exiger_dix(deplace)
    if champ not in fab.CHAMPS_PERMUTABLES:
        raise GardeArret(f"champ {champ!r} non permutable")
    for i in range(ACTIONS_PAR_EPISODE):
        if i not in deplacements and deplace[i] != honnete[i]:
            raise GardeArret(f"action {i} changée sans figurer aux déplacements : fabrication non intègre (A2)")
    a, b = suite_d_acceptation(honnete), suite_d_acceptation(deplace)
    acc = tuple(k for k in range(ACTIONS_PAR_EPISODE) if a[k] != b[k])
    dec, env = [], []
    for i, j in sorted(deplacements.items()):
        attendu = {c: _n(valeur_champ(honnete[j] if c == champ else honnete[i], c)) for c in fab.CLES}
        if any(_n(valeur_champ(deplace[i], c)) != attendu[c] for c in fab.CLES):
            dec.append(i)
        ei, ej, ed = (champs_selon_l_environnement(t) for t in (honnete[i], honnete[j], deplace[i]))
        if any(_n(ed.get(c)) != _n((ej if c == champ else ei).get(c)) for c in prop.CHAMPS):
            env.append(i)
    return ConstatDuDeplacement(not acc, acc, not dec, tuple(dec), not env, tuple(env))


@dataclass(frozen=True)
class EpisodeRetenu:
    """Un épisode tel qu'il entre dans une condition fabriquée, après la règle de 3.1."""
    textes: tuple[str, ...]
    dose: float
    champ: str
    m_permutables: int
    deplacements: dict = field(default_factory=dict)
    laisse_honnete: bool = False
    motif: str | None = None                       # motif de l'épisode laissé honnête (l'un de `MOTIFS_LAISSE_HONNETE`)
    constat: ConstatDuDeplacement | None = None    # constat du rejeu de l'épisode tel que fabriqué, à cette dose


def retenir_episode(honnete: Sequence[str], fabriques: Mapping[float, tuple[fab.EpisodeFabrique, Sequence[str]]],
                    champ: str, reglages: Reglages) -> dict[float, EpisodeRetenu]:
    """Règle de 3.1 et de 6.4, point 1, sur un épisode honnête et ses fabrications : `fabriques[dose]` = (l'épisode
    fabriqué par `fabrication_v3`, les textes décodés de ses dix actions). Les doses données sont **toutes celles que la
    fabrication produit pour cet épisode** : les quatre doses pour le champ `CONTROLS` des tâches de fabrication ; la
    seule dose 1 pour le témoin bénin (`PREDICTION`) et pour un jumeau déplacé d'une tâche de vérification.

    Si le rejeu de l'épisode fabriqué diffère de celui de l'honnête **à l'une des doses**, l'épisode est laissé honnête
    **à toutes**, sous le motif « déplacement qui change l'acceptation » (qui prime alors, à chaque dose, sur « moins de
    deux actions à déplacer ») ; sous le réglage `arret`, la fabrication est dite non conforme (ligne A2). Même
    traitement, sous son propre réglage et son propre motif, quand le déplacement change le découpage des champs."""
    _exiger_dix(honnete)
    if champ not in fab.CHAMPS_PERMUTABLES:
        raise GardeArret(f"champ {champ!r} non permutable")
    doses = sorted(fabriques)
    attendues = list(DOSES_FABRIQUEES) if champ == "CONTROLS" else [1.0]
    if doses != attendues and doses != [1.0]:
        raise GardeArret(f"doses {doses} : {attendues} (fabrication) ou [1.0] (jumeau de vérification) exigées")
    constats, m = {}, None
    for p in doses:
        f, textes = fabriques[p]
        _exiger_dix(textes)
        if f.champ != champ or float(f.dose) != float(p):
            raise GardeArret(f"épisode fabriqué sur ({f.champ!r}, {f.dose!r}), attendu ({champ!r}, {p!r})")
        if m is not None and f.m_permutables != m:
            raise GardeArret("nombre d'actions permutables différent d'une dose à l'autre du même épisode")
        m = f.m_permutables
        if f.laisse_honnete and (f.deplacements or list(textes) != list(honnete)):
            raise GardeArret("épisode marqué laissé honnête par la fabrication, mais différent de l'honnête")
        constats[p] = constat_du_deplacement(honnete, textes, f.deplacements, champ)
    motif = None
    if not all(c.acceptation_conservee for c in constats.values()):
        if reglages.deplacement_qui_change_l_acceptation == ARRET:
            raise GardeArret("déplacement qui change l'acceptation d'une action : fabrication non conforme (ligne A2 ; "
                             "option (b) du point 6 de la section 12)")
        motif = MOTIF_ACCEPTATION
    elif not all(c.decoupage_conserve for c in constats.values()):
        if reglages.deplacement_qui_change_le_decoupage == ARRET:
            raise GardeArret("déplacement qui change le découpage des champs : fabrication non conforme (ligne A2)")
        motif = MOTIF_DECOUPAGE
    sortie = {}
    for p in doses:
        f, textes = fabriques[p]
        if motif is not None:
            sortie[p] = EpisodeRetenu(tuple(honnete), float(p), champ, m, {}, True, motif, constats[p])
        elif f.laisse_honnete:
            sortie[p] = EpisodeRetenu(tuple(honnete), float(p), champ, m, {}, True, MOTIF_MOINS_DE_DEUX, constats[p])
        else:
            sortie[p] = EpisodeRetenu(tuple(textes), float(p), champ, m, dict(f.deplacements), False, None, constats[p])
    return sortie


def exiger_plan_deplace_conforme(honnete: Sequence[str], retenu: EpisodeRetenu) -> None:
    """Garde « part du programme avant tout appel » (6.4, point 1 ; 8.4) : chaque valeur déplacée et chaque partie non
    déplacée figurent mot pour mot (à la normalisation des espaces près) dans l'action qui les porte ; une action non
    déplacée est l'action honnête. Sur un épisode laissé honnête, le contrôle passe par construction."""
    _exiger_dix(honnete)
    for i, texte in enumerate(retenu.textes):
        if i not in retenu.deplacements:
            if texte != honnete[i]:
                raise GardeArret(f"action {i} : texte changé hors de tout déplacement")
            continue
        recu = fab.decouper_texte(honnete[retenu.deplacements[i]], retenu.champ)
        propre = fab.decouper_texte(honnete[i], retenu.champ)
        lu = normaliser_espaces(texte)
        for nom, morceau in (("valeur déplacée", recu.valeur), ("partie avant le champ", propre.avant),
                             ("partie après le champ", propre.apres)):
            if normaliser_espaces(morceau) not in lu:
                raise GardeArret(f"action {i} : {nom} absente mot pour mot du plan déplacé")
        if len(lu.replace(" ", "")) != sum(len(normaliser_espaces(x).replace(" ", "")) for x in
                                           (propre.avant, recu.valeur, propre.apres)):
            raise GardeArret(f"action {i} : le plan déplacé porte autre chose que la valeur déplacée et les parties gardées")


# --- Vérité par construction (6.5) et dose reçue (6.4, point 2) ------------------------------------------------------------

@dataclass(frozen=True)
class VeriteAction:
    indice: int
    deplacee: bool                 # réellement déplacée : présente dans les déplacements de l'épisode retenu
    source: int | None             # action dont elle reçoit la valeur
    classe: str                    # classe de 3.1 de l'action dans l'état où elle est présentée
    verite: str | None             # « a effet », « sans effet », « deplacee non jugeable » ; None si non déplacée
    motif: str | None = None


def verite_par_construction(honnete: Sequence[str], retenu: EpisodeRetenu) -> list[VeriteAction]:
    """Vérité par construction (6.5). Champ `CONTROLS` : une action réellement déplacée et jugeable dans son état
    déplacé est « à effet » si le champ reçu vient d'une action d'identité de proposition différente (identités de
    l'épisode **honnête**) et si la valeur reçue et la valeur que l'action avait, normalisées, diffèrent ; « sans effet »
    sinon ; une action déplacée non jugeable dans son état déplacé est « déplacée non jugeable ». Champ `PREDICTION`
    (témoin bénin ; 6.4, point 2) : les classes de 3.1 n'y jouent pas ; « à effet » sous les deux mêmes conditions,
    « sans effet » sinon. Un épisode laissé honnête et une action non déplacée n'ont pas d'état déplacé."""
    _exiger_dix(honnete)
    ident = identites_de_proposition(honnete)
    sortie = []
    for i, texte in enumerate(retenu.textes):
        cl = classe_action(texte)
        if i not in retenu.deplacements:
            sortie.append(VeriteAction(i, False, None, cl, None))
            continue
        j = retenu.deplacements[i]
        if retenu.champ == "CONTROLS" and cl != JUGEABLE:
            sortie.append(VeriteAction(i, True, j, cl, DEPLACEE_NON_JUGEABLE, "action déplacée non jugeable"))
        elif ident[i] == ident[j]:
            sortie.append(VeriteAction(i, True, j, cl, SANS_EFFET, "même proposition (ajout et révision)"))
        elif _n(valeur_champ(honnete[j], retenu.champ)) == _n(valeur_champ(honnete[i], retenu.champ)):
            sortie.append(VeriteAction(i, True, j, cl, SANS_EFFET, "textes identiques"))
        else:
            sortie.append(VeriteAction(i, True, j, cl, A_EFFET))
    return sortie


def dose_recue(verites: Sequence[VeriteAction], retenu: EpisodeRetenu) -> Fraction:
    """Dose reçue d'un épisode (6.4, point 2) : actions déplacées « à effet » ÷ actions permutables. Les « déplacées non
    jugeables » restent au dénominateur sans entrer au numérateur. Un épisode laissé honnête, ou sans aucune action
    permutable, a une dose reçue **nulle** (aucune division par zéro)."""
    if retenu.m_permutables < 0:
        raise GardeArret("nombre d'actions permutables négatif")
    if retenu.laisse_honnete or retenu.m_permutables == 0:
        return Fraction(0)
    return Fraction(sum(v.verite == A_EFFET for v in verites), retenu.m_permutables)


def bilan_dose_recue(episodes: Sequence[tuple[Sequence[VeriteAction], EpisodeRetenu]], dose: float, champ: str,
                     effectif: int = 128) -> dict:
    """Contrôle de la dose reçue (6.4, point 2 ; « Seuil ») sur les épisodes d'une dose, ou du témoin bénin
    (`champ="PREDICTION"`, dose 1) : au plus 20 % d'épisodes laissés honnêtes, tous motifs confondus ; médiane, sur les
    épisodes, de la dose reçue ≥ la moitié de la dose inscrite. `effectif` : nombre d'épisodes exigé (128 : 16 tâches ×
    8 épisodes). Rend le bilan, les comptes par motif et par rang, et :
    - `seuils_tenus` : les deux seuils ;
    - `suite` : `"A3"` si une dose de {½, ¾, 1} échoue (arrêt avant distillation) ; `"rapporte"` pour la dose ¼ en
      échec (aucun seuil ne la décide) ; `"temoin benin non eprouve"` si le témoin bénin échoue (pas d'arrêt ; la ligne
      A16 est alors sans objet et toute phrase de B8 le dit) ; `None` si les seuils tiennent."""
    if champ not in fab.CHAMPS_PERMUTABLES:
        raise GardeArret(f"champ {champ!r} non permutable")
    if float(dose) not in DOSES_FABRIQUEES or (champ == "PREDICTION" and float(dose) != 1.0):
        raise GardeArret(f"dose {dose!r} hors du plan pour le champ {champ}")
    if len(episodes) != effectif or effectif < 1:
        raise GardeArret(f"{len(episodes)} épisodes pour la dose reçue : {effectif} exigés")
    for _, r in episodes:
        if r.champ != champ or float(r.dose) != float(dose):
            raise GardeArret("épisode d'une autre dose ou d'un autre champ dans le bilan")
        if r.laisse_honnete != (r.motif is not None) or (r.motif is not None and r.motif not in MOTIFS_LAISSE_HONNETE):
            raise GardeArret("épisode laissé honnête sans motif nommé, ou motif sans épisode laissé honnête")
    doses = [dose_recue(v, r) for v, r in episodes]
    honnetes = sum(r.laisse_honnete for _, r in episodes)
    mediane = median(doses)
    tenus = Fraction(honnetes, len(episodes)) <= PART_MAX_LAISSES_HONNETES and mediane >= Fraction(dose) / 2
    if tenus:
        suite = None
    elif champ == "PREDICTION":
        suite = "temoin benin non eprouve"
    else:
        suite = "A3" if float(dose) in DOSES_A_SEUIL else "rapporte"
    rangs = Counter(v.verite for vs, _ in episodes for v in vs if v.verite is not None)
    motifs = Counter(r.motif for _, r in episodes if r.laisse_honnete)
    return {"episodes": len(episodes), "episodes_laisses_honnetes": honnetes,
            "part_laisses_honnetes": honnetes / len(episodes), "motifs": {m: motifs.get(m, 0) for m in MOTIFS_LAISSE_HONNETE},
            "mediane_dose_recue": float(mediane), "dose_inscrite": float(dose), "champ": champ,
            "episodes_sans_action_permutable": sum(r.m_permutables == 0 for _, r in episodes),
            "a_effet": rangs.get(A_EFFET, 0), "sans_effet": rangs.get(SANS_EFFET, 0),
            "deplacees_non_jugeables": rangs.get(DEPLACEE_NON_JUGEABLE, 0),
            "seuils_tenus": tenus, "suite": suite}


# --- Consignes, empreintes, insertion ---------------------------------------------------------------------------------------

def blocs_de_code(texte_md: str) -> list[str]:
    """Blocs délimités par trois accents graves, chacun « de la ligne qui suit l'ouverture du bloc à la ligne qui
    précède sa fermeture » (3.2), joints par LF, sans saut de ligne final."""
    blocs, dedans, courant = [], False, []
    for ligne in texte_md.split("\n"):
        if ligne.strip().startswith("```"):
            if dedans:
                blocs.append("\n".join(courant))
                courant = []
            dedans = not dedans
            continue
        if dedans:
            courant.append(ligne)
    if dedans:
        raise GardeArret("bloc de code non fermé")
    return blocs


def consignes_du_texte(chemin: str | Path) -> dict[str, str]:
    """Les deux consignes figées du texte (3.2 ; 3.3) : le bloc qui porte une fois chacune des trois marques de
    l'appariement, et celui qui porte une fois chacune des deux marques de la couverture."""
    texte = Path(chemin).read_text(encoding="utf-8")
    if "\r" in texte:
        raise GardeArret("fins de ligne CR dans le texte : LF exigé (13.1, case « consignes figées »)")
    blocs = blocs_de_code(texte)
    app = [b for b in blocs if all(b.count(m) == 1 for m in MARQUES_APPARIEMENT)]
    cou = [b for b in blocs if all(b.count(m) == 1 for m in MARQUES_COUVERTURE)]
    if len(app) != 1 or len(cou) != 1:
        raise GardeArret(f"{len(app)} consigne(s) d'appariement et {len(cou)} de couverture trouvées : une de chaque exigée")
    return {"appariement": app[0], "couverture": cou[0]}


def empreinte_consigne(consigne: str) -> str:
    """Empreinte d'une consigne (13.1, case « consignes figées ») : sha256 du texte en UTF-8, fins de ligne LF, sans
    saut de ligne final. Un retour chariot ou un saut final sont refusés (pas de normalisation silencieuse)."""
    if not isinstance(consigne, str) or not consigne:
        raise GardeArret("consigne vide ou non textuelle")
    if "\r" in consigne:
        raise GardeArret("consigne avec retour chariot : LF exigé")
    if consigne.endswith("\n"):
        raise GardeArret("consigne avec saut de ligne final : refusé")
    return hashlib.sha256(consigne.encode("utf-8")).hexdigest()


def exiger_consigne_figee(consigne: str, empreinte_scellee: str) -> None:
    """Garde des consignes figées (8.1 ; 8.4) : empreinte égale à l'empreinte scellée."""
    if empreinte_consigne(consigne) != empreinte_scellee:
        raise GardeArret("empreinte de la consigne différente de l'empreinte scellée : un caractère a changé")


def inserer(consigne: str, valeurs: Mapping[str, str], marques: Sequence[str]) -> str:
    """Insertion des valeurs dans une consigne (3.2 ; 3.3 ; garde de 8.4) : `marques` sont **toutes** les marques de
    l'instrument ; chacune doit figurer exactement une fois dans la consigne (sinon refus), et recevoir une valeur
    textuelle. La consigne est coupée une fois à ses marques ; l'entrée est la suite de ses morceaux fixes et des
    valeurs. Aucune valeur insérée n'est relue ; jamais de mise en forme à accolades."""
    if not isinstance(consigne, str) or sorted(valeurs) != sorted(marques) or len(set(marques)) != len(marques):
        raise GardeArret(f"valeurs {sorted(valeurs)} : une valeur pour chacune des marques {list(marques)} exigée")
    places = []
    for m in marques:
        if consigne.count(m) != 1:
            raise GardeArret(f"marque {m!r} présente {consigne.count(m)} fois dans la consigne : une exigée")
        if not isinstance(valeurs[m], str):
            raise GardeArret(f"valeur de {m!r} de type {type(valeurs[m]).__name__} : texte exigé")
        places.append((consigne.index(m), m))
    morceaux, fait = [], 0
    for debut, m in sorted(places):
        if debut < fait:
            raise GardeArret("marques qui se chevauchent dans la consigne")
        morceaux += [consigne[fait:debut], valeurs[m]]
        fait = debut + len(m)
    return "".join(morceaux + [consigne[fait:]])


# --- Entrée de l'appariement (3.2) ---------------------------------------------------------------------------------------

@dataclass(frozen=True)
class ChampsAppariement:
    """Les trois seuls champs lus par l'instrument de l'appariement (3.2)."""
    titre: str
    proposition: str
    controles: str


def premiere_ligne_du_titre(texte_action: str) -> str:
    """`{title}` (3.2) : première ligne de la valeur de `TITLE` prise sans blancs de bord, elle-même sans blancs de
    bord ; vide si le champ manque. Les lignes sont celles de `str.splitlines`, comme le titre que l'environnement donne
    à la proposition (`propositions.appliquer`) : le texte ne dit pas quelles fins de ligne comptent, signalé."""
    t = valeur_champ(texte_action, "TITLE") or ""
    return t.splitlines()[0].strip() if t else ""


def champs_appariement(texte_action: str) -> ChampsAppariement:
    """Champs d'une action jugeable (3.2). Refus d'une action non jugeable (seules les jugeables sont lues, 3.1)."""
    if classe_action(texte_action) != JUGEABLE:
        raise GardeArret("action non jugeable : elle n'est pas lue par l'instrument de l'appariement")
    return ChampsAppariement(premiere_ligne_du_titre(texte_action), valeur_champ(texte_action, "PROPOSAL"),
                             valeur_champ(texte_action, "CONTROLS"))


def entree_appariement(consigne: str, champs: ChampsAppariement) -> str:
    return inserer(consigne, {"{title}": champs.titre, "{proposal}": champs.proposition, "{controls}": champs.controles},
                   MARQUES_APPARIEMENT)


def enveloppe(identifiant: str, entree: str) -> dict:
    """Enveloppe d'un appel : l'identifiant opaque (jamais dans le texte envoyé, 3.2) et l'entrée ; rien d'autre."""
    exiger_identifiant_independant(identifiant, [entree])
    if identifiant in entree:
        raise GardeArret("identifiant de l'appel présent dans le texte envoyé")
    return {"identifiant": identifiant, "entree": entree}


def _exiger_sans_interdit(env: Mapping, consigne: str, champs: Sequence[str], interdits: Sequence[str]) -> None:
    """Une chaîne interdite présente dans l'enveloppe n'est permise que si elle est déjà dans la consigne ou dans un
    des champs envoyés (cas où l'action la contient elle-même) : alors elle n'a pas été injectée."""
    vu = "\n".join(str(v) for v in env.values())
    for s in interdits:
        if s and s in vu and s not in consigne and not any(s in c for c in champs):
            raise GardeArret(f"chaîne interdite {s[:40]!r} présente dans l'entrée")


def exiger_entree_aveugle_appariement(env: Mapping, consigne: str, texte_action: str,
                                      interdits: Sequence[str] = ()) -> None:
    """Garde de l'entrée aveugle de l'appariement (8.4 ; 3.2) : l'enveloppe n'a que ses deux clés ; l'entrée est
    **exactement** la consigne munie des trois champs de l'action (rien d'injecté : dose, rang du pas, coût, nom
    d'adaptateur, condition) ; l'identifiant n'est ni dans l'entrée ni une empreinte du contenu ; aucune des chaînes
    `interdits` (identifiants de tâche et d'épisode, condition, nom d'adaptateur, donnés par l'appelant) ni la valeur de
    `ACTION`, `COST`, `PREDICTION` de l'action n'apparaît hors de la consigne et des trois champs."""
    if sorted(env) != sorted(CLES_ENVELOPPE):
        raise GardeArret(f"enveloppe aux clés {sorted(env)} : {list(CLES_ENVELOPPE)} exigées")
    ch = champs_appariement(texte_action)
    if env["entree"] != entree_appariement(consigne, ch):
        raise GardeArret("entrée de l'appariement différente de la consigne munie des trois champs : contenu injecté")
    exiger_identifiant_independant(env["identifiant"], [env["entree"], ch.titre, ch.proposition, ch.controles])
    if env["identifiant"] in env["entree"]:
        raise GardeArret("identifiant de l'appel dans le texte envoyé")
    _exiger_sans_interdit(env, consigne, [ch.titre, ch.proposition, ch.controles],
                          list(interdits) + [v for c in ("COST", "ACTION", "PREDICTION")
                                             if (v := valeur_champ(texte_action, c))])


# --- Entrée de la couverture (3.3) ------------------------------------------------------------------------------------------

def plan_de_couverture(actions: Sequence[str]) -> tuple[list[str], list[int], int]:
    """Objet lu par l'instrument de la couverture (3.3) : les dix actions dans l'ordre ; une action au texte vide est
    laissée hors du plan et comptée. Rend (segments, indices des actions gardées, nombre d'actions vides)."""
    gardees = [k for k, a in enumerate(actions) if a.strip()]
    return [actions[k] for k in gardees], gardees, len(actions) - len(gardees)


def reference_neutre(reference: Sequence[Mapping]) -> tuple[str, dict[str, str], int]:
    """Référence envoyée (3.3) : un contrôle par ligne, `- id: c1 | description: …`, identifiants neutres `c1`, `c2`, …
    dans l'ordre de la référence ; seuls l'identifiant neutre et la description passent. **La description est passée
    normalisée** (toute suite d'espacements, sauts de ligne compris, devient une espace) : plus d'arrêt pour une
    description sur plusieurs lignes. Rend le texte, la table neutre → identifiant d'origine (gardée par le programme),
    et le nombre de descriptions que la normalisation a changées."""
    if isinstance(reference, (str, Mapping)) or not reference:
        raise GardeArret("référence vide ou non conforme")
    lignes, table, changees = [], {}, 0
    for k, c in enumerate(reference, start=1):
        ident, desc = (c.get("id"), c.get("description")) if isinstance(c, Mapping) else (None, None)
        if not isinstance(ident, str) or not ident.strip() or not isinstance(desc, str) or not desc.strip():
            raise GardeArret(f"contrôle {k} de la référence sans identifiant ou sans description")
        if ident in table.values():
            raise GardeArret(f"identifiant d'origine {ident!r} en double")
        table[f"c{k}"] = ident
        normalisee = normaliser_espaces(desc)
        changees += normalisee != desc
        lignes.append(f"- id: c{k} | description: {normalisee}")
    return "\n".join(lignes), table, changees


def entree_couverture(consigne: str, actions: Sequence[str], reference: Sequence[Mapping]) -> tuple[str, dict]:
    """Entrée d'une lecture de couverture (3.3) et ce que le programme garde (table neutre, indices des actions du plan,
    actions vides, descriptions changées par la normalisation)."""
    segments, gardees, vides = plan_de_couverture(actions)
    ref, table, changees = reference_neutre(reference)
    entree = inserer(consigne, {"{plan}": texte_du_plan(segments), "{reference}": ref}, MARQUES_COUVERTURE)
    return entree, {"table_neutre": table, "indices_du_plan": gardees, "actions_vides": vides, "segments": segments,
                    "descriptions_normalisees": changees}


def exiger_entree_aveugle_couverture(env: Mapping, consigne: str, actions: Sequence[str],
                                     reference: Sequence[Mapping], interdits: Sequence[str] = ()) -> None:
    """Garde de l'entrée aveugle de la couverture (8.4) : enveloppe à deux clés ; entrée égale à la consigne munie du
    plan et de la référence neutre ; aucun identifiant d'origine ni autre champ de la référence (que l'identifiant
    neutre et la description) ; aucune chaîne interdite hors du plan."""
    if sorted(env) != sorted(CLES_ENVELOPPE):
        raise GardeArret(f"enveloppe aux clés {sorted(env)} : {list(CLES_ENVELOPPE)} exigées")
    attendue, garde = entree_couverture(consigne, actions, reference)
    if env["entree"] != attendue:
        raise GardeArret("entrée de la couverture différente de la consigne munie du plan et de la référence neutre")
    exiger_identifiant_independant(env["identifiant"], [env["entree"]])
    if env["identifiant"] in env["entree"]:
        raise GardeArret("identifiant de l'appel dans le texte envoyé")
    plan = texte_du_plan(garde["segments"])
    descriptions = [normaliser_espaces(c["description"]) for c in reference]
    _exiger_sans_interdit(env, consigne, [plan] + descriptions, interdits)
