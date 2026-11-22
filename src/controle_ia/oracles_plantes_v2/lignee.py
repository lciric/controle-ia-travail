"""Registre de lignée : en ajout seul, chaîné par empreintes, rejouable (D-M5 : une proposition morte reste morte).

Chaque ligne (JSON) : rang, empreinte de la forme normalisée, statut (« morte » ou « vivante »), test, motif, origine,
empreinte de la ligne précédente. Au chargement, la chaîne entière est revérifiée ; une ligne retirée, modifiée ou
réordonnée lève `GardeArret`. Inscrire « vivante » pour une empreinte déjà morte est refusé ; une reformulation de
même forme normalisée hérite de la mort (la batterie consulte `statut` avant tout test).

v2 (remarque 4 de la contre-lecture) : la tête de la chaîne (nombre de lignes, empreinte de la dernière ligne) est
écrite à chaque ajout dans `<registre>.tete.json` et revérifiée au chargement : une troncature, ou une modification de la
dernière ligne, lève `GardeArret`. La tête n'est qu'une preuve d'intégrité contre l'accident ou l'oubli, pas contre
qui réécrirait les deux fichiers : pour une course, la tête finale est aussi à consigner au manifeste.
v2 (remarque 10) : chaque ligne porte aussi le texte canonique de la proposition et l'empreinte de son monde, pour
que la batterie compare une proposition aux mortes du même monde par équivalence, et non par empreinte seule.
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
        self.chemin_tete = Path(str(self.chemin) + ".tete.json")
        self.lignes: list[dict] = []
        self.dernier = ZERO
        self.etat: dict[str, str] = {}
        if self.chemin.exists():
            self._recharger()
            self._verifier_tete()
        elif self.chemin_tete.exists():
            raise GardeArret(f"registre de lignée {self.chemin} absent alors que sa tête existe : registre supprimé")

    def _verifier_tete(self):
        if not self.chemin_tete.exists():
            if self.lignes:
                raise GardeArret(f"registre de lignée {self.chemin} : tête de chaîne absente")
            return
        tete = json.loads(self.chemin_tete.read_text(encoding="utf-8"))
        if tete.get("lignes") != len(self.lignes) or tete.get("derniere") != self.dernier:
            raise GardeArret(f"registre de lignée {self.chemin} : tête de chaîne différente (troncature ou dernière "
                             "ligne modifiée)")

    def _ecrire_tete(self):
        self.chemin_tete.write_text(json.dumps({"lignes": len(self.lignes), "derniere": self.dernier}) + "\n",
                                    encoding="utf-8")

    def tete(self) -> dict:
        return {"lignes": len(self.lignes), "derniere": self.dernier}

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

    def mortes_du_monde(self, empreinte_monde: str):
        """(empreinte, texte canonique) des propositions mortes inscrites pour ce monde, dans l'ordre d'inscription."""
        vus = set()
        for d in self.lignes:
            e = d["empreinte"]
            if d.get("monde") == empreinte_monde and d.get("texte") and self.etat.get(e) == "morte" and e not in vus:
                vus.add(e)
                yield e, d["texte"]

    def inscrire(self, empreinte: str, statut: str, test: str, motif: str, origine=None, texte: str | None = None,
                 monde: str | None = None) -> dict:
        d = {"rang": len(self.lignes), "empreinte": empreinte, "statut": statut, "test": test, "motif": motif,
             "origine": origine, "texte": texte, "monde": monde, "precedente": self.dernier}
        self._appliquer(d)
        brute = json.dumps(d, ensure_ascii=False, sort_keys=True)
        with open(self.chemin, "a", encoding="utf-8") as f:
            f.write(brute + "\n")
        self.lignes.append(d)
        self.dernier = _h(brute)
        self._ecrire_tete()
        return d


def rejouer(chemin: str | Path) -> dict:
    """Statut de chaque empreinte, reconstruit depuis le fichier seul (chaîne vérifiée)."""
    return dict(Registre(chemin).etat)
