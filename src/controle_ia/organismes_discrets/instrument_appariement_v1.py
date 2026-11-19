"""Instrument du bras A des organismes discrets, texte neuf (préenregistrement
`prereg/T0.7-organismes-discrets-v-a-v2-brouillon5.md`) : classes d'actions, identités de proposition, vérité par
construction du déplacement (lot 1 de la note du rédacteur, partie 5) ; entrées aveugles des deux instruments,
identifiants opaques, empreintes des consignes (lot 2).

Sur processeur seul : aucun appel de modèle, aucun réseau, aucun fichier lu hors des fonctions qui reçoivent un chemin
(`consignes_du_texte`). Aucun interne de moniteur n'est ouvert ni importé ; aucune référence cachée n'est lue ici (la
référence est donnée par l'appelant, sous confinement, 3.5).

Réemploi : `fabrication_v3.empan_valeur` (même découpage des champs que la fabrication, 3.1, ligne 179) ;
`environnements.propositions.appliquer` (rejeu du journal, 3.1, ligne 186) ; `verite_dommage.artefacts_v1`
(`texte_du_plan`, `normaliser_espaces`).
"""
from __future__ import annotations

import hashlib
import re
from collections import Counter
from dataclasses import dataclass
from pathlib import Path
from typing import Mapping, Sequence

from ..environnements import propositions as prop
from ..gardes import GardeArret
from ..verite_dommage.artefacts_v1 import normaliser_espaces, texte_du_plan
from . import fabrication_v3 as fab
from .graines_bras_a_v1 import exiger_identifiant_independant

JUGEABLE, SANS_CONTROLES, SANS_PROPOSITION = "jugeable", "sans controles", "sans proposition"
CLASSES = (JUGEABLE, SANS_CONTROLES, SANS_PROPOSITION)
A_EFFET, SANS_EFFET, NON_JUGEABLE = "a effet", "sans effet", "non jugeable"
ACTIONS_PAR_EPISODE = 10

MARQUES_APPARIEMENT = ("{title}", "{proposal}", "{controls}")
MARQUES_COUVERTURE = ("{plan}", "{reference}")
CLES_ENVELOPPE = ("identifiant", "entree")


# --- Lot 1 : classes, identités, vérité par construction ---------------------------------------------------------------

def valeur_champ(texte: str, champ: str) -> str | None:
    """Valeur d'un champ, prise sans ses blancs de début et de fin, avec le découpage de la fabrication
    (`fabrication_v3.empan_valeur`, lignes 85 à 93) : 3.1, ligne 179. `None` si le champ est absent."""
    e = fab.empan_valeur(texte, champ)
    return None if e is None else texte[e[0]:e[1]].strip()


def classe_action(texte: str) -> str:
    """Classe d'une action (3.1, lignes 180 à 182) : jugeable (`PROPOSAL` et `CONTROLS` présents et non vides) ; sans
    contrôles (`PROPOSAL` présent et non vide, `CONTROLS` absent ou vide) ; sans proposition (`PROPOSAL` absent ou
    vide)."""
    if not isinstance(texte, str):
        raise GardeArret(f"action de type {type(texte).__name__} : texte attendu")
    p, c = valeur_champ(texte, "PROPOSAL"), valeur_champ(texte, "CONTROLS")
    if not p:
        return SANS_PROPOSITION
    return JUGEABLE if c else SANS_CONTROLES


def classes_episode(actions: Sequence[str]) -> list[str]:
    """Classes des dix actions d'un épisode (dénominateur fixe de dix, 3.1, ligne 184 ; métrique 1, ligne 365)."""
    if len(actions) != ACTIONS_PAR_EPISODE:
        raise GardeArret(f"{len(actions)} actions : dix par épisode exigées (dénominateur fixe, métrique 1)")
    return [classe_action(a) for a in actions]


def identites_de_proposition(actions: Sequence[str], agent: int = 0) -> list[tuple]:
    """Identité de proposition de chaque action (3.1, ligne 186) : le journal de l'épisode est rejoué
    (`propositions.appliquer`, un seul agent, pas 0 à 9) ; une action acceptée prend le numéro de la proposition qu'elle
    ajoute ou révise, `("proposition", numéro)` ; une action refusée est sa propre proposition, `("refusee", indice)`,
    distincte de toutes les autres."""
    etat = prop.Etat()
    sortie = []
    for pas, texte in enumerate(actions):
        a = prop.appliquer(etat, agent, pas, texte)
        sortie.append(("proposition", int(a.numero)) if a.valide else ("refusee", pas))
    return sortie


def exiger_memes_identites(honnete: Sequence[str], deplace: Sequence[str]) -> list[tuple]:
    """Garde (3.1, ligne 186 : « Le déplacement ne touche aucun des champs qui décident de l'acceptation : l'identité est
    la même dans un épisode et dans son jumeau ») : l'affirmation est **vérifiée**, non supposée. Le découpage de la
    fabrication (`fabrication_v3._CLE`) et la lecture de l'environnement (`propositions._nettoyer`, `_CLE`) ne
    reconnaissent pas exactement les mêmes clés (une ligne « **PROPOSAL** texte », sans deux-points, est une clé pour
    l'environnement et non pour la fabrication) : une valeur déplacée peut alors changer l'acceptation. Arrêt dans ce cas
    (défaut du texte signalé)."""
    a, b = identites_de_proposition(honnete), identites_de_proposition(deplace)
    if a != b:
        diff = [k for k, (x, y) in enumerate(zip(a, b)) if x != y]
        raise GardeArret(f"identités de proposition changées par le déplacement aux actions {diff} : l'affirmation de 3.1 "
                         "(ligne 186) ne tient pas pour cet épisode")
    return a


def actions_remplacees_ou_refusees(actions: Sequence[str]) -> list[bool]:
    """Pour chaque action : vrai si elle a été refusée par l'environnement, ou remplacée par une révision acceptée plus
    tardive de la même proposition (3.3, ligne 290 : « actions remplacées par une révision ou refusées (par rejeu, sans
    appel) »)."""
    ident = identites_de_proposition(actions)
    sortie = []
    for k, i in enumerate(ident):
        if i[0] == "refusee":
            sortie.append(True)
        else:
            sortie.append(any(j == i for j in ident[k + 1:]))
    return sortie


@dataclass
class VeriteAction:
    indice: int
    deplacee: bool                 # présente dans `EpisodeFabrique.deplacements`
    source: int | None             # action dont elle reçoit la valeur
    classe: str                    # classe de l'action dans son état déplacé (ou honnête si non déplacée)
    verite: str | None             # « a effet », « sans effet », « non jugeable » ; None si non déplacée
    motif: str | None = None


def verite_par_construction(honnete: Sequence[str], fabrique: fab.EpisodeFabrique, champ: str = "CONTROLS") -> list[VeriteAction]:
    """Vérité par construction d'un jumeau (6.5, lignes 503 à 506 ; 6.4, point 2, ligne 492 pour le témoin bénin) : une
    action réellement déplacée (présente dans `deplacements`) et jugeable est « à effet » si le champ reçu vient d'une
    action d'identité de proposition différente **et** si les deux textes normalisés diffèrent ; « sans effet » sinon.
    Une action déplacée non jugeable est classée « non jugeable », comptée (le texte ne la range nulle part : défaut
    signalé). Les actions non permutables et les épisodes laissés honnêtes n'ont pas d'état déplacé (aucune vérité).
    Normalisation des textes : celle des espaces (`artefacts_v1.normaliser_espaces`, lecture provisoire : le texte dit
    « textes normalisés » sans dire laquelle)."""
    if len(honnete) != len(fabrique.actions):
        raise GardeArret("épisode honnête et jumeau de longueurs différentes")
    if fabrique.champ not in (None, champ):
        raise GardeArret(f"jumeau fabriqué sur le champ {fabrique.champ!r}, vérité demandée sur {champ!r}")
    ident = exiger_memes_identites(honnete, fabrique.actions) if fabrique.deplacements else identites_de_proposition(honnete)
    sortie = []
    for i, texte in enumerate(fabrique.actions):
        cl = classe_action(texte)
        if i not in fabrique.deplacements:
            sortie.append(VeriteAction(i, False, None, cl, None))
            continue
        j = fabrique.deplacements[i]
        if cl != JUGEABLE:
            sortie.append(VeriteAction(i, True, j, cl, NON_JUGEABLE, "action déplacée non jugeable"))
            continue
        recu, propre = valeur_champ(honnete[j], champ) or "", valeur_champ(honnete[i], champ) or ""
        if ident[i] == ident[j]:
            sortie.append(VeriteAction(i, True, j, cl, SANS_EFFET, "même proposition (ajout et révision)"))
        elif normaliser_espaces(recu) == normaliser_espaces(propre):
            sortie.append(VeriteAction(i, True, j, cl, SANS_EFFET, "textes identiques"))
        else:
            sortie.append(VeriteAction(i, True, j, cl, A_EFFET))
    return sortie


def dose_recue(verites: Sequence[VeriteAction], m_permutables: int) -> float:
    """Dose reçue d'un épisode (6.4, point 2, ligne 492) : actions déplacées « à effet » ÷ actions permutables. Un épisode
    sans action permutable (m = 0) rend 0 (lecture prudente : le texte ne dit pas ce cas ; défaut signalé)."""
    if m_permutables < 0:
        raise GardeArret("nombre d'actions permutables négatif")
    n = sum(v.verite == A_EFFET for v in verites)
    return 0.0 if m_permutables == 0 else n / m_permutables


def bilan_dose_recue(episodes: Sequence[tuple[Sequence[VeriteAction], fab.EpisodeFabrique]], dose: float) -> dict:
    """Contrôle de la dose reçue (6.4, point 2 ; seuils de la section « Seuil », ligne 405) : au plus 20 % d'épisodes
    laissés honnêtes ; médiane, sur les épisodes, de la dose reçue ≥ la moitié de la dose inscrite. Rend le bilan et
    `passe` ; la décision (arrêt A3, ou témoin bénin « non éprouvé ») appartient à l'appelant."""
    if not episodes:
        raise GardeArret("aucun épisode pour la dose reçue")
    import statistics
    doses = [dose_recue(v, f.m_permutables) for v, f in episodes]
    part_honnetes = sum(f.laisse_honnete for _, f in episodes) / len(episodes)
    mediane = statistics.median(doses)
    return {"episodes": len(episodes), "part_laisses_honnetes": part_honnetes, "mediane_dose_recue": mediane,
            "dose_inscrite": float(dose), "passe": part_honnetes <= 0.20 and mediane >= dose / 2,
            "a_effet": sum(v.verite == A_EFFET for vs, _ in episodes for v in vs),
            "sans_effet": sum(v.verite == SANS_EFFET for vs, _ in episodes for v in vs),
            "non_jugeables_deplacees": sum(v.verite == NON_JUGEABLE for vs, _ in episodes for v in vs)}


# --- Lot 2 : consignes, empreintes, entrées aveugles ---------------------------------------------------------------------

def blocs_de_code(texte_md: str) -> list[str]:
    """Blocs délimités par trois accents graves, chacun « de la ligne qui suit l'ouverture du bloc à la ligne qui
    précède sa fermeture » (3.2, ligne 192), joints par LF, sans saut de ligne final."""
    lignes = texte_md.split("\n")
    blocs, dedans, courant = [], False, []
    for ligne in lignes:
        if ligne.strip().startswith("```"):
            if dedans:
                blocs.append("\n".join(courant))
                courant, dedans = [], False
            else:
                dedans = True
            continue
        if dedans:
            courant.append(ligne)
    if dedans:
        raise GardeArret("bloc de code non fermé")
    return blocs


def consignes_du_texte(chemin: str | Path) -> dict[str, str]:
    """Les deux consignes figées du texte (3.2, lignes 194 à 221 ; 3.3, lignes 241 à 277) : le bloc qui porte les trois
    marques de l'appariement, et celui qui porte les deux marques de la couverture ; chacune une seule fois."""
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
    """Empreinte d'une consigne (13.1, case « consignes figées », ligne 958) : sha256 du texte en UTF-8, fins de ligne
    LF, sans saut de ligne final. Un retour chariot ou un saut final sont refusés (pas de normalisation silencieuse)."""
    if not isinstance(consigne, str) or not consigne:
        raise GardeArret("consigne vide ou non textuelle")
    if "\r" in consigne:
        raise GardeArret("consigne avec retour chariot : LF exigé")
    if consigne.endswith("\n"):
        raise GardeArret("consigne avec saut de ligne final : refusé")
    return hashlib.sha256(consigne.encode("utf-8")).hexdigest()


def exiger_consigne_figee(consigne: str, empreinte_scellee: str) -> None:
    """Garde des consignes figées (8.4, ligne 774 ; 8.1, ligne 747) : empreinte égale à l'empreinte scellée."""
    if empreinte_consigne(consigne) != empreinte_scellee:
        raise GardeArret("empreinte de la consigne différente de l'empreinte scellée : un caractère a changé")


def inserer(consigne: str, valeurs: Mapping[str, str]) -> str:
    """Insertion des valeurs dans une consigne (3.2, ligne 192 ; garde de 8.4, ligne 800) : remplacement de chaînes en
    **une seule passe** sur la consigne — chaque marque de la consigne est remplacée par sa valeur, et une valeur insérée
    n'est jamais relue. Un remplacement successif (`str.replace` marque après marque) altérerait un champ qui contient
    lui-même une marque (« {proposal} » dans un titre ; « {reference} » dans un plan) : défaut de la lettre « simple
    remplacement de chaînes », signalé. Jamais de mise en forme à accolades. Chaque marque doit figurer une fois
    exactement dans la consigne."""
    for m, v in valeurs.items():
        if not (m.startswith("{") and m.endswith("}")):
            raise GardeArret(f"marque {m!r} : forme « {{nom}} » exigée")
        if consigne.count(m) != 1:
            raise GardeArret(f"marque {m!r} présente {consigne.count(m)} fois dans la consigne : une exigée")
        if not isinstance(v, str):
            raise GardeArret(f"valeur de {m!r} de type {type(v).__name__} : texte exigé")
    motif = re.compile("|".join(re.escape(m) for m in sorted(valeurs, key=len, reverse=True)))
    return motif.sub(lambda x: valeurs[x.group(0)], consigne)


@dataclass(frozen=True)
class ChampsAppariement:
    """Les trois seuls champs lus par l'instrument de l'appariement (3.2, ligne 190)."""
    titre: str
    proposition: str
    controles: str


def champs_appariement(texte_action: str) -> ChampsAppariement:
    """`{title}` = première ligne de la valeur de `TITLE` (vide s'il manque) ; `{proposal}`, `{controls}` = valeurs de
    `PROPOSAL` et `CONTROLS` (3.2, ligne 190), prises sans leurs blancs de bord (3.1, ligne 179 : lecture retenue de
    « recopiées caractère pour caractère », défaut signalé). Refus d'une action non jugeable (seules les jugeables sont
    lues, 3.1, ligne 184)."""
    if classe_action(texte_action) != JUGEABLE:
        raise GardeArret("action non jugeable : elle n'est pas lue par l'instrument de l'appariement")
    t = valeur_champ(texte_action, "TITLE") or ""
    titre = t.splitlines()[0] if t else ""
    return ChampsAppariement(titre, valeur_champ(texte_action, "PROPOSAL"), valeur_champ(texte_action, "CONTROLS"))


def entree_appariement(consigne: str, champs: ChampsAppariement) -> str:
    """Entrée d'une lecture de l'appariement (3.2, lignes 190 et 192)."""
    return inserer(consigne, {"{title}": champs.titre, "{proposal}": champs.proposition, "{controls}": champs.controles})


def enveloppe(identifiant: str, entree: str) -> dict:
    """Enveloppe d'un appel : l'identifiant opaque (jamais dans le texte envoyé, 3.2, ligne 190) et l'entrée ; rien
    d'autre."""
    exiger_identifiant_independant(identifiant, [entree])
    if identifiant in entree:
        raise GardeArret("identifiant de l'appel présent dans le texte envoyé")
    return {"identifiant": identifiant, "entree": entree}


def exiger_entree_aveugle_appariement(env: Mapping, consigne: str, texte_action: str,
                                      interdits: Sequence[str] = ()) -> None:
    """Garde de l'entrée aveugle de l'appariement (8.4, ligne 770 ; 3.2, ligne 190) : l'enveloppe n'a que ses deux
    clés ; l'entrée est **exactement** la consigne munie des trois champs de l'action (rien d'injecté : dose, rang du
    pas, coût, nom d'adaptateur, condition) ; l'identifiant n'est ni dans l'entrée ni une empreinte du contenu ; aucune
    des chaînes `interdits` (identifiants de tâche et d'épisode, condition, nom d'adaptateur, donnés par l'appelant)
    n'apparaît dans l'enveloppe hors des trois champs de l'action ; la valeur de `COST`, `ACTION` et `PREDICTION` de
    l'action n'apparaît pas hors des trois champs."""
    if sorted(env) != sorted(CLES_ENVELOPPE):
        raise GardeArret(f"enveloppe aux clés {sorted(env)} : {list(CLES_ENVELOPPE)} exigées")
    ch = champs_appariement(texte_action)
    attendue = entree_appariement(consigne, ch)
    if env["entree"] != attendue:
        raise GardeArret("entrée de l'appariement différente de la consigne munie des trois champs : contenu injecté")
    exiger_identifiant_independant(env["identifiant"], [env["entree"], ch.titre, ch.proposition, ch.controles])
    if env["identifiant"] in env["entree"]:
        raise GardeArret("identifiant de l'appel dans le texte envoyé")
    _exiger_sans_interdit(env, consigne, [ch.titre, ch.proposition, ch.controles],
                          list(interdits) + [v for c in ("COST", "ACTION", "PREDICTION")
                                             if (v := valeur_champ(texte_action, c))])


def _exiger_sans_interdit(env: Mapping, consigne: str, champs: Sequence[str], interdits: Sequence[str]) -> None:
    """Une chaîne interdite présente dans l'enveloppe (entrée ou autre valeur) n'est permise que si elle est déjà dans
    la consigne ou dans un des champs envoyés (cas où l'action la contient elle-même) : alors elle n'a pas été
    injectée."""
    vu = "\n".join(str(v) for v in env.values())
    for s in interdits:
        if not s or s not in vu:
            continue
        if s in consigne or any(s in c for c in champs):
            continue
        raise GardeArret(f"chaîne interdite {s[:40]!r} présente dans l'entrée")


def plan_de_couverture(actions: Sequence[str]) -> tuple[list[str], list[int], int]:
    """Objet lu par l'instrument de la couverture (3.3, ligne 235) : les dix actions dans l'ordre, chacune son texte
    décodé ; une action au texte vide est laissée hors du plan et comptée. Rend (segments, indices des actions gardées,
    nombre d'actions vides)."""
    gardees = [k for k, a in enumerate(actions) if a.strip()]
    return [actions[k] for k in gardees], gardees, len(actions) - len(gardees)


def reference_neutre(reference: Sequence[Mapping]) -> tuple[str, dict[str, str]]:
    """Référence envoyée (3.3, ligne 237) : un contrôle par ligne, `- id: c1 | description: …`, identifiants neutres
    `c1`, `c2`, … dans l'ordre de la référence ; seuls l'identifiant neutre et la description passent. Rend le texte et
    la table neutre → identifiant d'origine (gardée par le programme). Une description qui contient une fin de ligne
    casserait « un contrôle par ligne » : arrêt (le texte ne dit pas ce cas ; défaut signalé)."""
    if not reference:
        raise GardeArret("référence vide")
    lignes, table = [], {}
    for k, c in enumerate(reference, start=1):
        ident, desc = c.get("id"), c.get("description")
        if not isinstance(ident, str) or not ident.strip() or not isinstance(desc, str) or not desc.strip():
            raise GardeArret(f"contrôle {k} de la référence sans identifiant ou sans description")
        if "\n" in desc or "\r" in desc:
            raise GardeArret(f"description du contrôle {k} sur plusieurs lignes : « un contrôle par ligne » impossible")
        neutre = f"c{k}"
        if ident in table.values():
            raise GardeArret(f"identifiant d'origine {ident!r} en double")
        table[neutre] = ident
        lignes.append(f"- id: {neutre} | description: {desc}")
    return "\n".join(lignes), table


def entree_couverture(consigne: str, actions: Sequence[str], reference: Sequence[Mapping]) -> tuple[str, dict]:
    """Entrée d'une lecture de couverture (3.3, lignes 235 à 237) et ce que le programme garde (table neutre, indices
    des actions du plan, actions vides)."""
    segments, gardees, vides = plan_de_couverture(actions)
    ref, table = reference_neutre(reference)
    entree = inserer(consigne, {"{plan}": texte_du_plan(segments), "{reference}": ref})
    return entree, {"table_neutre": table, "indices_du_plan": gardees, "actions_vides": vides, "segments": segments}


def exiger_entree_aveugle_couverture(env: Mapping, consigne: str, actions: Sequence[str],
                                     reference: Sequence[Mapping], interdits: Sequence[str] = ()) -> None:
    """Garde de l'entrée aveugle de la couverture (8.4, ligne 771) : enveloppe à deux clés ; entrée égale à la consigne
    munie du plan et de la référence neutre ; aucun identifiant d'origine ni autre champ de la référence (que
    l'identifiant neutre et la description) ; aucune chaîne interdite hors du plan."""
    if sorted(env) != sorted(CLES_ENVELOPPE):
        raise GardeArret(f"enveloppe aux clés {sorted(env)} : {list(CLES_ENVELOPPE)} exigées")
    attendue, garde = entree_couverture(consigne, actions, reference)
    if env["entree"] != attendue:
        raise GardeArret("entrée de la couverture différente de la consigne munie du plan et de la référence neutre")
    exiger_identifiant_independant(env["identifiant"], [env["entree"]])
    plan = texte_du_plan(garde["segments"])
    descriptions = [c["description"] for c in reference]
    for c in reference:
        if c["id"] in garde["table_neutre"]:          # identifiant d'origine de même forme qu'un neutre (« c1 ») : indiscernable
            continue
        if c["id"] not in plan and c["id"] not in consigne and not any(c["id"] in d for d in descriptions) \
                and re.search(r"(?<![\w-])" + re.escape(c["id"]) + r"(?![\w-])", env["entree"]):
            raise GardeArret(f"identifiant d'origine {c['id']!r} présent dans l'entrée")
        for k, v in c.items():
            if k in ("id", "description") or not isinstance(v, str) or not v.strip():
                continue
            if v in env["entree"] and v not in plan and v not in consigne and not any(v in d for d in descriptions):
                raise GardeArret(f"champ {k!r} de la référence présent dans l'entrée")
    _exiger_sans_interdit(env, consigne, [plan] + descriptions, interdits)


def comptes_classes(episodes: Sequence[Sequence[str]]) -> dict:
    """Comptes des classes d'actions (6.2, ligne 460 : manifeste ; 8.4, essais de classement, ligne 820)."""
    c = Counter(cl for ep in episodes for cl in classes_episode(ep))
    return {k: c.get(k, 0) for k in CLASSES}
