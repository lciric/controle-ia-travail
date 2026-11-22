"""Registre de lignée : en ajout seul, chaîné par empreintes, rejouable (D-M5 : une proposition morte reste morte).

Chaque ligne (JSON) : rang, empreinte de la forme normalisée, statut (« morte » ou « vivante »), test, motif, origine,
empreinte de la ligne précédente. Au chargement, la chaîne entière est revérifiée ; une ligne retirée, modifiée ou
réordonnée lève `GardeArret`. Inscrire « vivante » pour une empreinte déjà morte est refusé ; une reformulation de
même forme normalisée hérite de la mort (la batterie consulte `statut` avant tout test).
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

from ..gardes import GardeArret

ZERO = "0" * 64
STATUTS = ("morte", "vivante")


def _h(ligne: str) -> str:
    return hashlib.sha256(ligne.encode("utf-8")).hexdigest()


class Registre:
    def __init__(self, chemin: str | Path):
        self.chemin = Path(chemin)
        self.lignes: list[dict] = []
        self.dernier = ZERO
        self.etat: dict[str, str] = {}
        if self.chemin.exists():
            self._recharger()

    def _recharger(self):
        precedente = ZERO
        for rang, brute in enumerate(self.chemin.read_text(encoding="utf-8").splitlines()):
            d = json.loads(brute)
            if d.get("rang") != rang or d.get("precedente") != precedente:
                raise GardeArret(f"registre de lignée {self.chemin} : chaîne rompue à la ligne {rang}")
            self._appliquer(d)
            self.lignes.append(d)
            precedente = _h(brute)
        self.dernier = precedente

    def _appliquer(self, d):
        e, s = d["empreinte"], d["statut"]
        if s not in STATUTS:
            raise GardeArret(f"statut inconnu {s!r}")
        if self.etat.get(e) == "morte" and s == "vivante":
            raise GardeArret(f"empreinte {e[:12]}… : une proposition morte reste morte (D-M5)")
        if s == "morte" or e not in self.etat:
            self.etat[e] = s

    def statut(self, empreinte: str):
        return self.etat.get(empreinte)

    def inscrire(self, empreinte: str, statut: str, test: str, motif: str, origine=None) -> dict:
        d = {"rang": len(self.lignes), "empreinte": empreinte, "statut": statut, "test": test, "motif": motif,
             "origine": origine, "precedente": self.dernier}
        self._appliquer(d)
        brute = json.dumps(d, ensure_ascii=False, sort_keys=True)
        with open(self.chemin, "a", encoding="utf-8") as f:
            f.write(brute + "\n")
        self.lignes.append(d)
        self.dernier = _h(brute)
        return d


def rejouer(chemin: str | Path) -> dict:
    """Statut de chaque empreinte, reconstruit depuis le fichier seul (chaîne vérifiée)."""
    return dict(Registre(chemin).etat)
