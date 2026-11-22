"""Modèle de (ii-b) qui tire ses jetons sur l'appareil du modèle, v1 (correctif 0020) : chemin NEUF, choisi explicitement.

`ModeleTorchTirageCarte` est `modele_v1.ModeleTorch` (inchangé, toujours le défaut), dont les trois tirages passent par
`harnais.tirage_carte_v1` : actions (`generer_lot_carte`), suites du jumeau en « cache_duplique »
(`suites_cache_duplique_carte`) et en « prerempli_par_suite » (`generer_lot_carte` sur K copies du préfixe). L'agent et le jumeau
tirent donc sous la **même** méthode (égalité des réglages de tirage, texte scellé, section 13, `jumeau_v5`). Le repli de la
forme du lot des suites est le même, consigné de même dans `replis`. Choisi par `modele_v5.construire_modele(config,
tirage="carte")` ou `lanceur_v5 --tirage carte` ; jamais par défaut.
"""
from __future__ import annotations

from ..gardes import GardeArret
from ..harnais.tirage_carte_v1 import METHODE, generer_lot_carte, suites_cache_duplique_carte
from .modele_v1 import _EXCEPTIONS_DU_CACHE, ModeleTorch


class ModeleTorchTirageCarte(ModeleTorch):
    tirage = METHODE

    def generer_actions(self, contextes, graines, max_nouveaux: int, temperature: float) -> list[list[int]]:
        nouveaux, _ = generer_lot_carte(self.torch, [list(c) for c in contextes], max_nouveaux, temperature, list(graines), self.fmt.fins, self.pad)
        return nouveaux

    def _suites_cache_duplique(self, prefixe, graines, max_jetons: int, temperature: float) -> list[list[int]]:
        return suites_cache_duplique_carte(self.torch, list(prefixe), list(graines), int(max_jetons), temperature, self.fins_suites(), self.pad)

    def suites(self, prefixe, graines, max_jetons: int, temperature: float) -> list[list[int]]:
        if not prefixe or not graines:
            raise GardeArret("suites du jumeau : préfixe ou graines vides")
        if self.forme == "cache_duplique":
            try:
                return self._suites_cache_duplique(prefixe, graines, max_jetons, temperature)
            except GardeArret:
                raise
            except _EXCEPTIONS_DU_CACHE as e:
                self.replis.append({"de": "cache_duplique", "vers": "prerempli_par_suite", "motif": f"{type(e).__name__}: {e}"[:300]})
                self.forme = "prerempli_par_suite"
        nouveaux, _ = generer_lot_carte(self.torch, [list(prefixe)] * len(graines), int(max_jetons), temperature, list(graines),
                                        self.fins_suites(), self.pad)
        return nouveaux
