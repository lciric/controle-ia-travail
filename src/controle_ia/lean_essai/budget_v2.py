"""Compteur de dépense A7 avec verrou — essai Lean, v2 (CLL-12 de la contre-lecture `2077ae26…`, R-2300).

« Contrôler puis inscrire » se fait sous un verrou : des fils lancés ensemble (trois processus Lean et quatre de la suite au
pilote) ne peuvent plus dépasser le plafond. Le reste (coût d'un appel, plafond par item, A8) est repris de `budget_v1`.
"""
from __future__ import annotations

import threading
from dataclasses import dataclass, field

from controle_ia.gardes import GardeArret

from .budget_v1 import (CACHE_ECRITURE, CACHE_LECTURE, GRAINES_ETALONNAGE, MAX_GRAINES, MIN_GRAINES,  # noqa: F401
                        PARALLELE_L, PARALLELE_S, PIRE_PROCHAIN, PLAFOND_ITEM, RESERVE_A7, RESERVE_A7_SERIE,
                        TAILLE_BLOC, cout_appel, decision_a8, graines_a8, lecture_si_coupure_a7, peut_appeler_item)


@dataclass
class CompteurPhase:
    plafond: float
    depense: float = 0.0
    en_vol: dict[str, float] = field(default_factory=dict)
    journal: list[tuple[str, str, float]] = field(default_factory=list)
    verrou: threading.Lock = field(default_factory=threading.Lock, repr=False, compare=False)

    def _peut_lancer(self, pire_prochain: float) -> bool:
        return self.depense + sum(self.en_vol.values()) + pire_prochain <= self.plafond

    def peut_lancer(self, pire_prochain: float) -> bool:
        with self.verrou:
            return self._peut_lancer(pire_prochain)

    def lancer(self, ident: str, pire: float) -> None:
        if pire <= 0:
            raise GardeArret(f"A7 : pire cas non positif pour {ident}")
        with self.verrou:
            if ident in self.en_vol:
                raise GardeArret(f"A7 : appel {ident} déjà en vol")
            if not self._peut_lancer(pire):
                raise GardeArret(f"A7 : dépense {self.depense:.2f} + en vol {sum(self.en_vol.values()):.2f} + prochain "
                                 f"{pire:.2f} > plafond {self.plafond:.2f} : plus aucun lancement")
            self.en_vol[ident] = pire
            self.journal.append(("lancé", ident, pire))

    def terminer(self, ident: str, cout_reel: float) -> None:
        with self.verrou:
            if ident not in self.en_vol:
                raise GardeArret(f"A7 : appel {ident} soldé sans avoir été lancé")
            pire = self.en_vol.pop(ident)
            if cout_reel < 0 or cout_reel > pire + 1e-9:
                raise GardeArret(f"A7 : coût réel {cout_reel:.4f} hors de [0 ; pire cas {pire:.4f}] pour {ident} : "
                                 "compteur faux")
            self.depense += cout_reel
            self.journal.append(("soldé", ident, cout_reel))

    def coupure(self, reserve: float = RESERVE_A7) -> bool:
        with self.verrou:
            return self.depense > self.plafond - reserve
