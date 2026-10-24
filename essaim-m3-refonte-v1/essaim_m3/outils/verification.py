"""Étage M1 : le « collisionneur byzantin de Dolev », rendu réel.

Principe gardé de Gemini : découverte et vérification sont découplées (un seul attaquant suffit à découvrir une
faille ; un vérificateur isolé tranche, avec des leurres).

Corrections :
- B-06/B-07 : canaris aveugles et verdicts lus item par item (`canaris.py`) ; aucun compteur auto-déclaré (constat 32) ;
- B-08/B-33 (constats 14, 40, 41) : la convergence n'est plus « zéro survivant à un tour », ni des incréments additifs
  appelés Wald-Ville : c'est un processus de e-valeurs. Sous l'hypothèse H0 « au moins une faille subsiste et chaque
  attaquant indépendant la trouve avec probabilité ≥ ρ », un tour sans faille confirmée a probabilité ≤ (1 − ρ)^m
  (m familles d'attaquants indépendantes) ; e_t = 1[aucune faille confirmée] / (1 − ρ̂_t)^m, avec ρ̂_t la borne
  inférieure de Wilson mesurée sur les canaris du tour, est une e-valeur ; le produit est une surmartingale et
  l'inégalité de Ville permet de déclarer la convergence quand le produit atteint 1/α. Une faille confirmée remet le
  produit à 1 (le texte défendu a changé). Un tour non lisible (canaris non valides, appel en échec) vaut e_t = 1 :
  il n'avance pas la convergence, et ne la déclare jamais ;
- B-17 : la gravité et la nouveauté ne sont plus auto-déclarées par le découvreur : un candidat compte quand le
  vérificateur (d'une autre famille de fournisseur quand c'est possible, constat 39) le dit VALIDE, et il est « déjà
  couvert » quand la mémoire M0 le dit (résidu faible), pas quand le modèle le dit ;
- B-26 : plus de variable non liée ; chaque tour rend un statut.
"""
from __future__ import annotations

import json
import math
import re

import numpy as np

from . import canaris as _canaris
from .especes import famille_de

MOTIF_BLOC_JSON = re.compile(r"```json\s*(\{.*?\})\s*```", re.S)


def extraire_json(texte: str):
    """Premier bloc ```json … ``` ; sinon l'objet entre la première `{` et la dernière `}`. None si illisible."""
    if not texte:
        return None
    m = MOTIF_BLOC_JSON.search(texte)
    brut = m.group(1) if m else None
    if brut is None and "{" in texte and "}" in texte:
        brut = texte[texte.find("{"):texte.rfind("}") + 1]
    if brut is None:
        return None
    try:
        return json.loads(brut)
    except json.JSONDecodeError:
        return None


# ---------- consignes ----------

def prompt_decouverte(cible: str, contexte: str, deja_fermes: list[str], connaissances: list[str]) -> str:
    fermes = "\n".join(f"- {x}" for x in deja_fermes) or "- (aucune encore)"
    conn = "\n".join(f"- {x}" for x in connaissances) or "- (aucune encore)"
    return (
        "Tu es un attaquant de l'étage M1 (découverte). Lis le contexte, puis propose les failles, angles morts ou "
        "affirmations fausses que tu trouves, en français simple, une par candidat, chacune vérifiable par un "
        "raisonnement court. N'invente pas de références : si tu cites un travail, écris « (à vérifier) ».\n\n"
        f"CIBLE : {cible}\n\nCONTEXTE :\n{contexte}\n\n"
        f"DÉJÀ FERMÉ (ne répète pas) :\n{fermes}\n\nCONNAISSANCES ACQUISES PAR L'ESSAIM :\n{conn}\n\n"
        "Termine par un bloc ```json {\"candidats\": [{\"enonce\": \"…\", \"mecanisme\": \"…\", \"confiance\": 0.0}]} ```"
        " (confiance entre 0 et 1 que le candidat sera confirmé par un vérificateur indépendant)."
    )


def prompt_verification(presentes: list[dict], contexte: str) -> str:
    lignes = "\n".join(f"[{it['id']}] {it['enonce']}" for it in presentes)
    return (
        "Tu es un vérificateur isolé de l'étage M1. Pour chaque item ci-dessous, décide s'il est VALIDE (l'énoncé est "
        "vrai, ou la faille décrite est réelle dans le contexte) ou INVALIDE (faux, ou faille inexistante). Chaque item "
        "se juge seul, par un raisonnement court ; certains items sont vrais, d'autres faux, dans un ordre quelconque. "
        "Réponds pour tous les items.\n\n"
        f"CONTEXTE :\n{contexte}\n\nITEMS :\n{lignes}\n\n"
        "Termine par un bloc ```json {\"verdicts\": {\"item-01\": \"VALIDE\", \"item-02\": \"INVALIDE\"}, "
        "\"justifications\": {\"item-01\": \"…\"}} ``` couvrant tous les identifiants."
    )


def parser_candidats(texte: str) -> list[dict]:
    d = extraire_json(texte)
    if not isinstance(d, dict) or not isinstance(d.get("candidats"), list):
        return []
    sortie = []
    for c in d["candidats"]:
        if not isinstance(c, dict):
            continue
        e = str(c.get("enonce", "")).strip()
        if not e:
            continue
        try:
            conf = float(c.get("confiance", 0.5))
        except (TypeError, ValueError):
            conf = 0.5
        sortie.append({"enonce": e, "mecanisme": str(c.get("mecanisme", "")).strip(), "confiance": min(1.0, max(0.0, conf))})
    return sortie


def parser_verdicts(texte: str) -> dict[str, str]:
    d = extraire_json(texte)
    if not isinstance(d, dict) or not isinstance(d.get("verdicts"), dict):
        return {}
    return {str(k): str(v).strip().upper() for k, v in d["verdicts"].items()}


# ---------- processus de e-valeurs ----------

class EProcessus:
    def __init__(self, alpha: float = 0.05):
        self.alpha = float(alpha)
        self.produit = 1.0
        self.trace: list[dict] = []

    def observer(self, failles_confirmees: int, lisible: bool, puissance: float, m_familles: int) -> dict:
        if not lisible or m_familles <= 0:
            e = 1.0
            raison = "tour non lisible : e = 1"
        elif failles_confirmees > 0:
            e = 0.0
            raison = "faille confirmée : produit remis à 1 (texte défendu modifié)"
        else:
            rho = min(0.999, max(0.0, float(puissance)))
            e = 1.0 / ((1.0 - rho) ** int(m_familles)) if rho > 0 else 1.0
            raison = "tour propre"
        if failles_confirmees > 0 and lisible:
            self.produit = 1.0
        else:
            self.produit *= e
        etat = {"e": round(e, 4), "produit": round(self.produit, 4), "seuil": round(1.0 / self.alpha, 2),
                "converge": self.produit >= 1.0 / self.alpha, "raison": raison, "m_familles": m_familles,
                "puissance": round(float(puissance), 4), "failles_confirmees": failles_confirmees}
        self.trace.append(etat)
        return etat

    @property
    def converge(self) -> bool:
        return self.produit >= 1.0 / self.alpha


# ---------- un tour de collisionneur ----------

def tour_collisionneur(appeler, etape: str, cible: str, contexte: str, attaquants: list[str],
                       verificateurs: list[str], rng: np.random.Generator, deja_fermes: list[str],
                       connaissances: list[str], memoire=None, seuil_couvert: float = 0.35,
                       puissance_min: float = 0.6, n_canaris: int = 12) -> dict:
    """Découverte par chaque attaquant, puis vérification isolée des candidats mêlés à des canaris.

    `appeler(espece, etape, prompt, role=…)` rend un objet avec `ok`, `statut`, `texte`, `identifiant` (la couche
    d'appel du noyau, ou un double). Rend un dictionnaire sans valeur par défaut déguisée : `lisible` dit si le tour compte."""
    candidats, decouvertes = [], []
    familles_actives = set()
    for a in attaquants:
        res = appeler(a, etape, prompt_decouverte(cible, contexte, deja_fermes, connaissances), role="decouverte")
        cs = parser_candidats(res.texte) if res.ok else []
        decouvertes.append({"espece": a, "statut": res.statut, "n_candidats": len(cs), "id_appel": res.identifiant})
        if res.ok:
            familles_actives.add(famille_de(a))
        for c in cs:
            c["attaquant"] = a
            candidats.append(c)

    # déjà couvert, selon la mémoire (jamais selon le modèle)
    nouveaux = []
    for c in candidats:
        if memoire is not None and memoire.deja_couvert(c["enonce"], seuil_couvert):
            c["deja_couvert_memoire"] = True
        else:
            nouveaux.append(c)

    canaris = _canaris.tirer_canaris(rng, n_canaris)
    presentes, engagement = _canaris.meler([c["enonce"] for c in nouveaux], canaris, rng)
    verdicts_par_verif, mesures = {}, {}
    for v in verificateurs:
        res_v = appeler(v, etape, prompt_verification(presentes, contexte), role="verification")
        verdicts = parser_verdicts(res_v.texte) if res_v.ok else {}
        verdicts_par_verif[v] = {"statut": res_v.statut, "verdicts": verdicts, "id_appel": res_v.identifiant}
        mesures[v] = _canaris.mesurer(presentes, verdicts) if verdicts else {"valide": False, "non_lus": len(presentes), "puissance_wilson_inf": 0.0}

    # un tour est lisible si au moins un vérificateur a des canaris valides et une puissance suffisante
    verifs_fiables = [v for v, m in mesures.items() if m.get("valide") and m.get("puissance_wilson_inf", 0.0) >= puissance_min]
    confirmes, rejetes = [], []
    if verifs_fiables:
        for it in presentes:
            if it["type"] != "candidat":
                continue
            votes = [verdicts_par_verif[v]["verdicts"].get(it["id"]) for v in verifs_fiables]
            c = dict(nouveaux[it["indice_source"]])
            c["id_item"] = it["id"]
            c["verdicts"] = {v: verdicts_par_verif[v]["verdicts"].get(it["id"]) for v in verifs_fiables}
            if votes and all(x == "VALIDE" for x in votes):
                confirmes.append(c)
            else:
                rejetes.append(c)
    puissance = max([mesures[v]["puissance_wilson_inf"] for v in verifs_fiables], default=0.0)
    return {
        "etape": etape, "lisible": bool(verifs_fiables), "decouvertes": decouvertes,
        "n_candidats": len(candidats), "n_nouveaux": len(nouveaux), "confirmes": confirmes, "rejetes": rejetes,
        "canaris": {"engagement": engagement, "engagement_verifie": _canaris.verifier_engagement(engagement, presentes),
                    "mesures": mesures, "n": n_canaris},
        "familles_attaquantes_actives": sorted(familles_actives), "m_familles": len(familles_actives),
        "puissance": puissance, "verificateurs_fiables": verifs_fiables,
    }


def choisir_verificateurs(attaquants: list[str], especes: list[str]) -> list[str]:
    """Priorité aux espèces d'une autre famille que les attaquants (constat 39) ; sinon toutes les autres espèces."""
    fam_att = {famille_de(a) for a in attaquants}
    autres_familles = [e for e in especes if famille_de(e) not in fam_att]
    if autres_familles:
        return autres_familles
    return [e for e in especes if e not in attaquants] or list(especes)
