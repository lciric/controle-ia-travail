"""Oracle des fausses promotions ([CL] M1 ; section « Métrique » du texte scellé), calculé **avant** le rejeu des bras.

Par génération : 20 000 instances et leurs issues tirées du monde (graine `(f, g, 2000)`) ; log-vraisemblance moyenne
de chaque carte ; maximum de vraisemblance du nul v8 de l'archive : bibliothèque standard et
`nul_v8.membres_archive_v8`, membres ordinaires lus par `selection_pari.trajectoire_membre`, membres ajustés par
`nul_filles_v2.valeurs_ajustees` à l'instant 20 000 (marge de certificat comprise) ; gain d'oracle = log-vraisemblance
moyenne de la carte moins celle du meilleur membre. La marginale d'entraînement, propre à chaque carte, n'entre pas :
le meilleur membre est le même pour les 24 cartes (section « Coût ») et la marginale ajustée (`marginale_empirique`)
domine toute loi fixe de la marginale.

Les probabilités par instance sont calculées par l'évaluateur vectorisé (`lois_v1.probas_np`, égal à
`selection_pari.proba` à 10⁻¹² près, essais) servi aux routines du juge par un cache de même interface que
`selection_pari.Cache`.

Classes : porteuse = porteuse construite et gain > 0 ; porteuse sans gain = porteuse construite et gain ≤ 0 ;
fausse = non porteuse et gain ≤ 0 ; partiellement vraie = non porteuse et gain > 0.
"""
from __future__ import annotations

import numpy as np

from ..gardes import GardeArret
from . import banc_tirages_repartis_v1 as B
from . import lois_v1 as L

CLASSES = ("porteuse", "porteuse sans gain", "fausse", "partiellement vraie")


class CacheNumpy:
    """Même interface que `selection_pari.Cache` (méthode `probas(loi)`), calculée par l'évaluateur vectorisé."""

    def __init__(self, J, Z: np.ndarray, G: np.ndarray):
        self.J, self.Z, self.G, self._lois = J, Z, G, {}

    def probas(self, loi):
        cle = self.J.outils.empreinte_objet(loi)
        if cle not in self._lois:
            self._lois[cle] = L.probas_np(loi, self.Z, self.G).tolist()
        return self._lois[cle]


def classe(porteuse_construite: bool, gain: float) -> str:
    if porteuse_construite:
        return "porteuse" if gain > 0 else "porteuse sans gain"
    return "partiellement vraie" if gain > 0 else "fausse"


def table_oracle(J, gen: "B.Generation") -> dict:
    """Table de l'oracle d'une génération. Gardes : appelée avant toute issue fraîche de la génération ; échantillon
    retiré de sa propre graine et comparé (jamais les issues jugées)."""
    if gen.etat != "construite" or gen.flux_ouverts or gen.issues is not None:
        raise GardeArret(f"{gen.nom} : oracle demandé après l'ouverture d'un flux d'issues fraîches")
    ech = gen.echantillon
    refait = B.echantillon_oracle(gen.racine, gen.f, gen.g, gen.monde.loi)
    if ech.cle != (gen.f, gen.g, 2000) or refait.empreinte != ech.empreinte or len(ech.y) != B.ORACLE_N:
        raise GardeArret(f"{gen.nom} : échantillon de l'oracle non tiré de sa graine (f, g, 2000)")
    cache = CacheNumpy(J, ech.Z, ech.G)
    issues = [int(v) for v in ech.y]
    n = len(issues)
    biblio = list(J.sp.BIBLIOTHEQUE_STANDARD) + J.nul_v8.membres_archive_v8(dict(B.lois_archive(gen.archive)), None, B.K, B.D)
    valeurs = {}
    for m in biblio:
        if m["type"] in J.nf.TYPES_AJUSTES:
            valeurs[m["nom"]] = float(J.nf.valeurs_ajustees(m, cache, issues, B.K, [n])[n])
        else:
            valeurs[m["nom"]] = float(J.sp.trajectoire_membre(m, issues, None, B.K, cache)[-1])
    meilleur_nom = max(valeurs, key=lambda k: (valeurs[k], k))
    meilleur = valeurs[meilleur_nom]
    cartes = []
    porteuse = B.SORTE_PORTEUSE[gen.famille]
    for c in gen.cartes:
        ll = float(J.sp.trajectoire_loi(c.loi, issues, None, cache)[-1])
        gain = (ll - meilleur) / n
        cartes.append({"indice": c.indice, "sorte": c.sorte, "empreinte_loi": c.empreinte,
                       "log_vraisemblance_moyenne": ll / n, "gain": gain,
                       "classe": classe(c.sorte == porteuse, gain)})
    return {"generation": gen.nom, "famille": gen.famille, "g": gen.g, "n": n, "echantillon": ech.empreinte,
            "meilleur_membre": meilleur_nom, "log_vraisemblance_moyenne_meilleur": meilleur / n,
            "membres": {k: v / n for k, v in sorted(valeurs.items())}, "cartes": cartes}
