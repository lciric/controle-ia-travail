"""Fichier de stimuli figé du pilote : validation des règles de construction et paires de chaque direction.

Le fichier (`brouillons/pilote-exposant-p-v1/stimuli-pilote-exposant-p-v1.json`) porte ses règles (R-S1 à R-S7) et
ses listes de marqueurs. `problemes_stimuli` les vérifie mécaniquement ; une garde (`exiger_stimuli_conformes`) lève
sur tout écart, sans repli (R5). Le contrôle de sens (une phrase « évaluation » parle bien d'une évaluation de
l'assistant, une phrase « déploiement » d'un besoin réel) reste celui du contre-lecteur.

Signes : E = moyenne(évaluation − déploiement) ; R = moyenne(formel − familier) ; directions du papier : b − a.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

from ..gardes import GardeArret

ECART_FIN_E = 3        # R-S2 : écart de longueur des fins dans une paire E (mots)
ECART_PHRASE_R = 6     # R-S3 : écart de longueur des phrases dans une paire R (mots)
FENETRE_FIN = 6        # R-S4 : une racine d'évaluation parmi les 6 derniers mots des phrases E
MIN_PAIRES = 30


def charger(chemin: str | Path) -> dict:
    return json.loads(Path(chemin).read_text(encoding="utf-8"))


def mots(phrase: str) -> list[str]:
    """Mots en minuscules, apostrophes normalisées, ponctuation de bord retirée (traits d'union internes gardés)."""
    t = phrase.replace("’", "'").lower().split()
    return [m.strip(".,;:!?\"()[]") for m in t if m.strip(".,;:!?\"()[]")]


def a_racine(m: str, racines: list[str]) -> bool:
    return any(m.startswith(r) for r in racines)


def hachage_liste(lst: list[str]) -> str:
    """Empreinte d'une liste d'invites au format du code publié (`scripts/lib/directions.py::_hash_list`)."""
    h = hashlib.sha256()
    for s in lst:
        h.update(s.encode("utf-8"))
        h.update(b"\x00")
    return h.hexdigest()


def problemes_stimuli(stim: dict, hachages_publies: dict | None = None) -> list[str]:
    """Liste des écarts aux règles R-S1 à R-S7 (vide si conforme). `hachages_publies` : empreintes publiées des
    listes d'invites du papier (`references-publiees-v1.json`, clé `directions_hachages_invites`)."""
    pb: list[str] = []
    mk = stim["marqueurs"]
    racines = mk["racines_evaluation"]
    familiers = set(mk["contractions"]) | set(mk["marqueurs_familiers"])
    quads = stim["quadruplets"]
    vues: set[str] = set()
    for q in quads:
        i = q["id"]
        for cle, ouv, fin in (("FE", "ouverture_F", "fin_FE"), ("FD", "ouverture_F", "fin_FD"),
                              ("CE", "ouverture_C", "fin_CE"), ("CD", "ouverture_C", "fin_CD")):
            if q[cle] != f"{q[ouv]}, {q[fin]}":
                pb.append(f"{i} {cle} : la phrase n'est pas « ouverture, fin » (R-S1)")
            if not any(m.startswith(q["contenu"].lower()) for m in mots(q[cle])) and q["contenu"].lower() not in q[cle].lower():
                pb.append(f"{i} {cle} : contenu « {q['contenu']} » absent (R-S1)")
            if q[cle].rstrip()[-1:] in ".!?;:":
                pb.append(f"{i} {cle} : ponctuation finale (R-S6)")
            if q[cle] in vues:
                pb.append(f"{i} {cle} : phrase en double (R-S6)")
            vues.add(q[cle])
        for a, b in (("fin_FE", "fin_FD"), ("fin_CE", "fin_CD")):
            if abs(len(mots(q[a])) - len(mots(q[b]))) > ECART_FIN_E:
                pb.append(f"{i} {a}/{b} : écart de longueur des fins > {ECART_FIN_E} mots (R-S2)")
        for a, b in (("FE", "CE"), ("FD", "CD")):
            if abs(len(mots(q[a])) - len(mots(q[b]))) > ECART_PHRASE_R:
                pb.append(f"{i} {a}/{b} : écart de longueur > {ECART_PHRASE_R} mots (R-S3)")
        for cle in ("FE", "CE"):
            if not any(a_racine(m, racines) for m in mots(q[cle])[-FENETRE_FIN:]):
                pb.append(f"{i} {cle} : aucune racine d'évaluation parmi les {FENETRE_FIN} derniers mots (R-S4)")
        for cle in ("FD", "CD"):
            if any(a_racine(m, racines) for m in mots(q[cle])):
                pb.append(f"{i} {cle} : racine d'évaluation dans une phrase de déploiement (R-S4)")
        for cle in ("FE", "FD"):
            if set(mots(q[cle])) & familiers:
                pb.append(f"{i} {cle} : marqueur familier ou contraction en registre formel (R-S5)")
        for cle in ("CE", "CD"):
            if not set(mots(q[cle])) & familiers:
                pb.append(f"{i} {cle} : aucun marqueur familier en registre familier (R-S5)")
        attendu = "A" if int(i[1:]) <= len(quads) // 2 else "B"
        if q["moitie"] != attendu:
            pb.append(f"{i} : moitié {q['moitie']} au lieu de {attendu} (R-S7)")
    if 2 * len(quads) < MIN_PAIRES:
        pb.append(f"{2 * len(quads)} paires par direction < {MIN_PAIRES}")
    for nom, d in stim["papier"]["directions"].items():
        if len(d["a"]) != len(d["b"]) or len(d["a"]) < MIN_PAIRES:
            pb.append(f"papier {nom} : {len(d['a'])}/{len(d['b'])} invites (au moins {MIN_PAIRES} paires appariées)")
        if hachages_publies and nom in hachages_publies:
            m = min(len(d["a"]), len(d["b"]))
            if hachage_liste(d["a"][:m]) != hachages_publies[nom]["a_sha"] or hachage_liste(d["b"][:m]) != hachages_publies[nom]["b_sha"]:
                pb.append(f"papier {nom} : invites différentes de celles qui ont produit les directions publiées")
    return pb


def exiger_stimuli_conformes(chemin: str | Path, hachages_publies: dict | None = None) -> dict:
    stim = charger(chemin)
    pb = problemes_stimuli(stim, hachages_publies)
    if pb:
        raise GardeArret(f"{chemin} non conforme à ses règles de construction : " + " ; ".join(pb[:10]))
    return stim


def paires(stim: dict, direction: str, moitie: str | None = None) -> tuple[list[str], list[str]]:
    """Rend (côté a, côté b) ; la direction est moyenne(b − a).
    E : a = déploiement, b = évaluation (paires FD/FE et CD/CE) ; R : a = familier, b = formel (CE/FE et CD/FD) ;
    E_naif : a = CD, b = FE (paires confondues avec le registre, contrôle descriptif) ; E_naif_inverse : a = FD, b = CE ;
    papier : directions du papier (b − a) ; E_echelle : a = réel, b = évaluation (cadrages de l'échelle v2)."""
    quads = [q for q in stim["quadruplets"] if moitie is None or q["moitie"] == moitie]
    if direction == "E":
        return [q["FD"] for q in quads] + [q["CD"] for q in quads], [q["FE"] for q in quads] + [q["CE"] for q in quads]
    if direction == "R":
        return [q["CE"] for q in quads] + [q["CD"] for q in quads], [q["FE"] for q in quads] + [q["FD"] for q in quads]
    if direction == "E_naif":
        return [q["CD"] for q in quads], [q["FE"] for q in quads]
    if direction == "E_naif_inverse":
        return [q["FD"] for q in quads], [q["CE"] for q in quads]
    if direction == "E_echelle":
        c = stim["echelle_v2_cadrages"]["paires"]
        return [p[1] for p in c], [p[0] for p in c]
    if direction in stim["papier"]["directions"]:
        d = stim["papier"]["directions"][direction]
        m = min(len(d["a"]), len(d["b"]))
        return d["a"][:m], d["b"][:m]
    raise KeyError(direction)


def empreinte_canonique(stim: dict) -> str:
    return hashlib.sha256(json.dumps(stim, sort_keys=True, ensure_ascii=False, separators=(",", ":")).encode()).hexdigest()
