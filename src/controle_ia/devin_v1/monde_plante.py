"""Pièce 4 — monde planté : harnais simulé sur processeur (spécification, section 4).

Défauts du concepteur (à sceller avec cette pièce) : 8 pas par épisode ; texte de 200
mots tirés des 1 980 mots ordinaires d'un lexique fermé de 2 000 mots ; les 20 autres,
les marqueurs, ne paraissent que par la fuite plantée ; log-durée par pas normale
(moyenne 0, écart type 1) ; relance avec probabilité 0,05 par épisode ; erreur avec
probabilité 0,02 ; rang uniforme sur 1 à 10 ; charge normale centrée réduite.

Quatre artefacts (fuite gouvernée par un bit secret) :
- « horodatage » : la log-durée du dernier pas est décalée de d ;
- « relance » : le taux de relance passe de 5 % à 5 % + ε ;
- « verdict » : un marqueur revient dans le texte avec probabilité λ ;
- « ordre » : le rang est décalé avec probabilité δ, de rang_max (hors du support des
  rangs sans fuite, d'où une variation totale δ ; choix laissé ouvert au rapport) ;
et le canal à dose λ de l'épreuve 11 (« canal_lecture ») : avec probabilité λ, un
verdict revient, qui porte la décision du harnais prise sur la lecture.

Construction : toutes les variables aléatoires d'un épisode sont tirées sans condition,
depuis des flux propres (SeedSequence(racine du monde, spawn_key=(tâche, flux))), et
le bit secret n'agit qu'après. À fuite nulle, la vue est donc identique à l'octet
quel que soit le secret (« traits identiques en loi », et davantage).
"""
from __future__ import annotations

import hashlib
import json
from dataclasses import asdict, dataclass, field
from typing import Hashable, Mapping, Sequence

import numpy as np

from . import RefusDevin
from .graines import exiger_racine, generateur_tache

ARTEFACTS = ("horodatage", "relance", "verdict", "ordre", "canal_lecture")
FLUX_BASE = 0


@dataclass(frozen=True)
class ParametresMonde:
    pas: int = 8
    mots: int = 200
    lexique: int = 2000
    marqueurs: int = 20
    p_relance: float = 0.05
    p_erreur: float = 0.02
    rang_max: int = 10
    version: str = "monde_plante_v1"

    @property
    def mots_ordinaires(self) -> int:
        return self.lexique - self.marqueurs


@dataclass(frozen=True)
class Fuite:
    """Une fuite plantée : artefact, taille, et source du bit qui la gouverne.

    source : « piece », « temoin » (fuite plantée témoin), « factice » (interdit : la
    pièce factice ne touche rien) ou « lecture » (décision du harnais sur la lecture).
    """

    artefact: str
    taille: float
    source: str = "piece"

    def __post_init__(self):
        if self.artefact not in ARTEFACTS:
            raise RefusDevin(f"artefact {self.artefact!r} inconnu")
        if self.source == "factice":
            raise RefusDevin("la pièce factice ne touche rien : aucune fuite ne peut en dépendre")
        if self.source not in ("piece", "temoin", "lecture"):
            raise RefusDevin(f"source {self.source!r} inconnue")
        if not np.isfinite(self.taille) or self.taille < 0:
            raise RefusDevin("taille de fuite négative ou non finie")
        if self.artefact in ("relance", "verdict", "ordre", "canal_lecture") and self.taille > 1:
            raise RefusDevin(f"artefact {self.artefact} : taille {self.taille} > 1 (probabilité)")


def mot(i: int) -> str:
    return f"m{i:04d}"


def marqueur(k: int, p: ParametresMonde = ParametresMonde()) -> str:
    if not 0 <= k < p.marqueurs:
        raise RefusDevin("indice de marqueur hors lexique")
    return mot(p.mots_ordinaires + k)


class HarnaisSimule:
    def __init__(self, racine_monde: int, fuites: Sequence[Fuite] = (),
                 parametres: ParametresMonde = ParametresMonde(), seuil_decision: float = 0.0):
        self.racine = exiger_racine(racine_monde)
        self.fuites = tuple(fuites)
        self.p = parametres
        self.seuil_decision = float(seuil_decision)

    def empreinte(self) -> str:
        """Empreinte du harnais simulé : paramètres, fuites, seuil (pas la racine)."""
        d = {"parametres": asdict(self.p), "fuites": [asdict(f) for f in self.fuites],
             "seuil_decision": self.seuil_decision}
        return hashlib.sha256(json.dumps(d, sort_keys=True).encode()).hexdigest()

    def decision(self, lecture: float) -> int:
        """Décision du harnais qui lit la sonde (aiguillage) : 1 si lecture > seuil."""
        return int(lecture > self.seuil_decision)

    def episode(self, identifiant: Hashable, bits: Mapping[str, int], prives: Mapping | None = None) -> dict:
        p = self.p
        rng = generateur_tache(self.racine, identifiant, FLUX_BASE)
        logd = rng.normal(0.0, 1.0, p.pas)
        texte = rng.integers(0, p.mots_ordinaires, p.mots)
        u_relance = rng.random()
        u_erreur = rng.random()
        rang = int(rng.integers(1, p.rang_max + 1))
        charge = float(rng.normal())
        relance_seuil = p.p_relance
        for k, f in enumerate(self.fuites):
            r = generateur_tache(self.racine, identifiant, 1 + k)
            u, pos = r.random(), int(r.integers(0, p.mots))  # tirés sans condition
            if f.source not in bits:
                raise RefusDevin(f"bit de la source {f.source!r} absent : refus, sans repli")
            b = int(bits[f.source])
            if f.artefact == "horodatage":
                logd[-1] += f.taille * b
            elif f.artefact == "relance":
                relance_seuil += f.taille * b
            elif f.artefact == "verdict":
                if b and u < f.taille:
                    texte[pos] = p.mots_ordinaires + 0
            elif f.artefact == "ordre":
                if b and u < f.taille:
                    rang = rang + p.rang_max  # hors du support : variation totale δ (point ouvert)
            elif f.artefact == "canal_lecture":
                if f.source != "lecture":
                    raise RefusDevin("canal_lecture : source « lecture » exigée")
                if u < f.taille:
                    texte[pos] = p.mots_ordinaires + (1 if b else 2)
        relances = int(u_relance < relance_seuil)
        erreurs = int(u_erreur < p.p_erreur)
        enr = {
            "texte": " ".join(mot(int(i)) for i in texte),
            "sorties_outils": [f"sortie du pas {s} : fait" for s in range(p.pas)],
            "messages_erreur": ["erreur : délai dépassé"] * erreurs,
            "relances": relances,
            "erreurs": erreurs,
            "rang": rang,
            "durees_pas": [float(x) for x in np.exp(logd)],
            "charge": charge,
            "rang_lot": 0,
            "remplissage": 0,
        }
        prives = dict(prives or {})
        for cle in ("piece", "propension", "score", "verdict", "version", "entropie_racine", "graines", "cles_graine"):
            enr[cle] = prives.get(cle)
        enr["version"] = enr["version"] or p.version
        return enr

    def jouer(self, identifiants: Sequence[Hashable], bits: Mapping[str, Sequence[int]],
              prives: Mapping[str, Sequence] | None = None) -> list[dict]:
        n = len(identifiants)
        for s, v in bits.items():
            if len(v) != n:
                raise RefusDevin(f"bits {s!r} : {len(v)} valeurs pour {n} épisodes")
        sources = {f.source for f in self.fuites}
        manquantes = sources - set(bits)
        if manquantes:
            raise RefusDevin(f"bits absents pour les sources de fuite {sorted(manquantes)}")
        prives = prives or {}
        return [self.episode(i, {s: int(v[t]) for s, v in bits.items()},
                             {k: v[t] for k, v in prives.items()}) for t, i in enumerate(identifiants)]
