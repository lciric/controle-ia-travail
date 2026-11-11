"""Compteur de dépense, coupure A7, plafond par item et étalonnage A8 de l'essai Lean — v1 (écrits et éprouvés en D-1a).

Brouillon 3, § 3.3 (plafond de 4 USD par item, parallélisme 3 processus Lean et 4 de la suite), § 3.8 A7 et A8 ;
`calculs-v3/calculs_devis_essai_v5.py` (`85a8fad1…`), bloc 1 (mêmes formules). Aucun appel de modèle ici : le compteur reçoit
des coûts, il n'en produit pas.
"""
from __future__ import annotations

import math
from dataclasses import dataclass, field

from controle_ia.gardes import GardeArret

PLAFOND_ITEM = 4.0
PARALLELE_L, PARALLELE_S = 3, 4
PIRE_PROCHAIN = 4.0  # le plus cher des appels suivants (paire, planteur, contrôle, lecture nue, audit, adjudication)
RESERVE_A7 = PARALLELE_L * PLAFOND_ITEM + PARALLELE_S * PLAFOND_ITEM + PIRE_PROCHAIN   # 32
RESERVE_A7_SERIE = PLAFOND_ITEM + PLAFOND_ITEM + PIRE_PROCHAIN                           # 12 : fin sans parallélisme
CACHE_LECTURE, CACHE_ECRITURE = 0.10, 1.25
GRAINES_ETALONNAGE, TAILLE_BLOC, MIN_GRAINES, MAX_GRAINES = 10, 5, 40, 60


def cout_appel(prix_entree: float, prix_sortie: float, entree: int, sortie: int, lus_cache: int = 0,
               ecrits_cache: int = 0, f_lecture: float = CACHE_LECTURE, f_ecriture: float = CACHE_ECRITURE) -> float:
    """Coût d'un appel en USD (prix par million de jetons ; `entree` compte tous les jetons d'entrée, dont ceux lus et écrits
    en cache ; le raisonnement est compté en sortie)."""
    for v in (entree, sortie, lus_cache, ecrits_cache):
        if v < 0:
            raise GardeArret("compteur de jetons négatif")
    if lus_cache + ecrits_cache > entree:
        raise GardeArret("jetons en cache plus nombreux que les jetons d'entrée : compteur faux")
    ordinaires = entree - lus_cache - ecrits_cache
    return (ordinaires * prix_entree + lus_cache * prix_entree * f_lecture + ecrits_cache * prix_entree * f_ecriture
            + sortie * prix_sortie) / 1e6


def peut_appeler_item(depense_item: float, pire_appel: float, plafond_item: float = PLAFOND_ITEM) -> bool:
    """Plafond par item (§ 3.3) : aucun appel dont le pire cas ferait passer l'item au-dessus de 4 USD (motif « plafond »)."""
    return depense_item + pire_appel <= plafond_item


@dataclass
class CompteurPhase:
    """A7 : dépense de la phase + pire cas de tous les appels en cours + pire cas du prochain appel > plafond ⇒ aucun
    lancement. Chaque appel est déclaré avec son pire cas avant d'être lancé, puis soldé à son coût réel."""
    plafond: float
    depense: float = 0.0
    en_vol: dict[str, float] = field(default_factory=dict)
    journal: list[tuple[str, str, float]] = field(default_factory=list)

    def peut_lancer(self, pire_prochain: float) -> bool:
        return self.depense + sum(self.en_vol.values()) + pire_prochain <= self.plafond

    def lancer(self, ident: str, pire: float) -> None:
        if pire <= 0:
            raise GardeArret(f"A7 : pire cas non positif pour {ident}")
        if ident in self.en_vol:
            raise GardeArret(f"A7 : appel {ident} déjà en vol")
        if not self.peut_lancer(pire):
            raise GardeArret(f"A7 : dépense {self.depense:.2f} + en vol {sum(self.en_vol.values()):.2f} + prochain "
                             f"{pire:.2f} > plafond {self.plafond:.2f} : plus aucun lancement")
        self.en_vol[ident] = pire
        self.journal.append(("lancé", ident, pire))

    def terminer(self, ident: str, cout_reel: float) -> None:
        if ident not in self.en_vol:
            raise GardeArret(f"A7 : appel {ident} soldé sans avoir été lancé")
        pire = self.en_vol.pop(ident)
        if cout_reel < 0 or cout_reel > pire + 1e-9:
            raise GardeArret(f"A7 : coût réel {cout_reel:.4f} hors de [0 ; pire cas {pire:.4f}] pour {ident} : compteur faux")
        self.depense += cout_reel
        self.journal.append(("soldé", ident, cout_reel))

    def coupure(self, reserve: float = RESERVE_A7) -> bool:
        """Forme chiffrée de A7 à parallélisme plein : la coupure se déclenche dès que la dépense dépasse plafond − réserve."""
        return self.depense > self.plafond - reserve


def graines_a8(plafond: float, depense: float, charges_restantes: float, cout_graine: float,
               reserve: float = RESERVE_A7) -> int:
    """A8 : G = 10 + ⌊(P − D − R − H) / c⌋, borné à 60 et arrondi au bloc de 5 inférieur."""
    if cout_graine <= 0:
        raise GardeArret("A8 : coût mesuré d'une graine non positif")
    if min(plafond, depense, charges_restantes, reserve) < 0:
        raise GardeArret("A8 : montant négatif")
    g = GRAINES_ETALONNAGE + math.floor((plafond - depense - reserve - charges_restantes) / cout_graine)
    g = min(g, MAX_GRAINES)
    return max(0, (g // TAILLE_BLOC) * TAILLE_BLOC)


def decision_a8(plafond: float, depense: float, charges_restantes: float, cout_graine: float,
                reserve: float = RESERVE_A7) -> dict:
    """G < 40 ⇒ arrêt avant toute autre graine (« pilote non payable au plafond »)."""
    g = graines_a8(plafond, depense, charges_restantes, cout_graine, reserve)
    arret = g < MIN_GRAINES
    return {"graines": g, "arret": arret,
            "motif": "pilote non payable au plafond : arrêt, devis refait, nouveau GO" if arret else
                     ("pilote ramené sous 60 graines : choix des classes « fragile »" if g < MAX_GRAINES else "pilote complet")}


def lecture_si_coupure_a7(graines_faites: int) -> str:
    """A8 : si A7 coupe en cours de route sous 40 graines, le pilote est lu en description seulement."""
    return "descriptive seulement (aucun choix de classes, aucune fiche de passage)" if graines_faites < MIN_GRAINES \
        else "ordinaire"
