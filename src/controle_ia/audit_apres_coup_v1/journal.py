"""Journal en ajout seul, à horloge logique (rang 2 ; section 1, « Journal »).

Par épisode : enjeu (écrit avant le début), fin, score, les trois parts et π_i, U_i, audité, source ; puis, par un
événement à part ajouté plus tard, le verdict et son heure. Rien ne se réécrit : un verdict est un événement neuf, non
une ligne modifiée. Les colonnes rendues sont en lecture seule, et une empreinte chaînée par lot détecte toute
modification faite par-dessous l'interface (`verifier`).

Horloge logique : l'épisode i occupe les instants 8i (enjeu écrit), 8i+1 (début), 8i+2 (fin), 8i+3 (score consigné),
8i+4 (uniforme de la pièce tiré) ; un verdict rendu à la fin de l'épisode j porte l'heure 8j+5 ; une vue de l'agent
est servie au début de l'épisode (8i+1). L'heure d'écriture de l'enjeu est consignée telle qu'elle a eu lieu (la garde 3
des invariants refuse un enjeu écrit après le début). La vérité plantée ne vit pas ici (`simulateur.VeritePlantee`).

Codes de source : 0 non audité, 1 plancher, 2 enjeu, 3 soupçon.
"""
from __future__ import annotations

import numpy as np

from ..gardes import GardeArret
from .graines import empreinte_octets, empreinte_tableaux

PAS = 8
DECALAGES = {"h_enjeu": 0, "h_debut": 1, "h_fin": 2, "h_score": 3, "h_piece": 4, "h_verdict": 5}
SOURCES = {0: "non audité", 1: "plancher", 2: "enjeu", 3: "soupçon"}
CODE_SOURCE = {v: k for k, v in SOURCES.items()}

COLONNES_EPISODE = {
    "episode": np.int64, "enjeu": np.float64, "h_enjeu": np.int64, "h_debut": np.int64, "h_fin": np.int64,
    "score": np.float64, "g_force": np.bool_, "h_score": np.int64,
    "part_plancher": np.float64, "part_enjeu": np.float64, "part_soupcon": np.float64, "pi": np.float64,
    "ecrete": np.bool_, "u_piece": np.float64, "h_piece": np.int64, "audite": np.bool_, "source": np.int8,
}
COLONNES_VERDICT = {"episode": np.int64, "verdict": np.int8, "h_verdict": np.int64}


def heures(episodes: np.ndarray) -> dict[str, np.ndarray]:
    e = np.asarray(episodes, dtype=np.int64)
    return {k: PAS * e + d for k, d in DECALAGES.items() if k != "h_verdict"}


class Journal:
    """Journal d'un monde : deux tables en ajout seul (épisodes, verdicts)."""

    def __init__(self, etiquette: str = "", chaine: bool = True):
        """`chaine=False` (boucles statistiques longues) n'écrit pas l'empreinte chaînée : `verifier` et `empreinte`
        rendent alors un refus nommé, jamais une empreinte de remplacement."""
        self.etiquette = etiquette
        self.chaine = chaine
        self._ep: dict[str, list[np.ndarray]] = {k: [] for k in COLONNES_EPISODE}
        self._ve: dict[str, list[np.ndarray]] = {k: [] for k in COLONNES_VERDICT}
        self._chaine: list[str] = []
        self._lots: list[tuple[str, int]] = []
        self._n_ep = 0
        self._n_ve = 0
        self._cache: dict[str, np.ndarray] = {}
        self._dernier_h_verdict = -1

    # --------------------------------------------------------------------------------------------
    def _chainer(self, table: str, lot: dict[str, np.ndarray]) -> None:
        self._lots.append((table, len(next(iter(lot.values())))))
        if not self.chaine:
            return
        prec = self._chaine[-1] if self._chaine else "0" * 64
        self._chaine.append(empreinte_octets(prec.encode(), table.encode(), empreinte_tableaux(**lot).encode()))

    def _figer(self, cols: dict, schema: dict) -> dict[str, np.ndarray]:
        manquantes = set(schema) - set(cols)
        if manquantes:
            raise GardeArret(f"journal : colonnes absentes {sorted(manquantes)} (refus, jamais de valeur par défaut)")
        en_trop = set(cols) - set(schema)
        if en_trop:
            raise GardeArret(f"journal : colonnes inconnues {sorted(en_trop)}")
        lot = {}
        n = None
        for k, t in schema.items():
            a = np.array(cols[k], dtype=t, copy=True)
            if a.ndim != 1:
                raise GardeArret(f"journal : colonne {k} non plate")
            if n is None:
                n = len(a)
            elif len(a) != n:
                raise GardeArret(f"journal : colonnes de longueurs différentes ({k})")
            a.setflags(write=False)
            lot[k] = a
        return lot

    def ajouter_episodes(self, **cols) -> None:
        lot = self._figer(cols, COLONNES_EPISODE)
        n = len(lot["episode"])
        if n == 0:
            return
        if np.any(~np.isfinite(lot["pi"])):
            raise GardeArret("journal : probabilité d'audit absente (refus, jamais de valeur par défaut)")
        attendu = np.arange(self._n_ep, self._n_ep + n)
        if not np.array_equal(lot["episode"], attendu):
            raise GardeArret("journal : épisodes hors de l'ordre d'ajout (ajout seul, à horloge logique)")
        h = heures(lot["episode"])
        for k, v in h.items():
            if k == "h_enjeu":
                continue  # l'heure d'écriture de l'enjeu est consignée telle quelle ; la garde 3 la juge
            if not np.array_equal(lot[k], v):
                raise GardeArret(f"journal : horloge {k} incohérente (enjeu avant le début, fin, score, puis pièce)")
        if np.any(lot["u_piece"] < 0) or np.any(lot["u_piece"] >= 1):
            raise GardeArret("journal : uniforme de la pièce hors de [0, 1)")
        if not np.array_equal(lot["audite"], lot["u_piece"] < lot["pi"]):
            raise GardeArret("journal : « audité » ne suit pas U_i < π_i")
        if not np.array_equal(lot["audite"], lot["source"] > 0):
            raise GardeArret("journal : source incohérente avec « audité »")
        self._chainer("episodes", lot)
        for k in COLONNES_EPISODE:
            self._ep[k].append(lot[k])
        self._n_ep += n
        self._cache.clear()

    def ajouter_verdicts(self, **cols) -> None:
        lot = self._figer(cols, COLONNES_VERDICT)
        n = len(lot["episode"])
        if n == 0:
            return
        if np.any(np.diff(lot["h_verdict"]) < 0) or lot["h_verdict"][0] < self._dernier_h_verdict:
            raise GardeArret("journal : verdicts hors de l'ordre de leurs heures (ajout seul)")
        if np.any(lot["episode"] >= self._n_ep):
            raise GardeArret("journal : verdict d'un épisode non encore journalisé")
        audite = self.colonne("audite")
        if not np.all(audite[lot["episode"]]):
            raise GardeArret("journal : verdict d'un épisode non audité")
        hp = PAS * lot["episode"] + DECALAGES["h_piece"]
        if np.any(lot["h_verdict"] <= hp):
            raise GardeArret("journal : verdict d'heure antérieure à la pièce (l'audit vient après coup)")
        if np.any(lot["h_verdict"] % PAS != DECALAGES["h_verdict"]):
            raise GardeArret("journal : heure de verdict hors de la grille de l'horloge")
        deja = set(np.concatenate(self._ve["episode"]).tolist()) if self._ve["episode"] else set()
        if deja & set(lot["episode"].tolist()) or len(set(lot["episode"].tolist())) != n:
            raise GardeArret("journal : second verdict pour un épisode (réécriture interdite)")
        self._chainer("verdicts", lot)
        for k in COLONNES_VERDICT:
            self._ve[k].append(lot[k])
        self._n_ve += n
        self._dernier_h_verdict = int(lot["h_verdict"][-1])
        self._cache.clear()

    def reecrire(self, *args, **kwargs):
        raise GardeArret("journal en ajout seul : réécriture d'une ligne refusée")

    # --------------------------------------------------------------------------------------------
    def __len__(self) -> int:
        return self._n_ep

    def colonne(self, nom: str) -> np.ndarray:
        if nom in self._cache:
            return self._cache[nom]
        if nom in COLONNES_EPISODE:
            parts, t = self._ep[nom], COLONNES_EPISODE[nom]
        elif nom.startswith("v_") and nom[2:] in COLONNES_VERDICT:
            parts, t = self._ve[nom[2:]], COLONNES_VERDICT[nom[2:]]
        else:
            raise GardeArret(f"journal : colonne inconnue {nom!r}")
        a = np.concatenate(parts) if parts else np.zeros(0, dtype=t)
        a.setflags(write=False)
        self._cache[nom] = a
        return a

    def verdicts_par_episode(self) -> tuple[np.ndarray, np.ndarray]:
        """(verdict, heure) par épisode ; -1 et -1 sans verdict journalisé."""
        v = np.full(self._n_ep, -1, dtype=np.int8)
        h = np.full(self._n_ep, -1, dtype=np.int64)
        e = self.colonne("v_episode")
        v[e] = self.colonne("v_verdict")
        h[e] = self.colonne("v_h_verdict")
        return v, h

    def _exiger_chaine(self) -> None:
        if not self.chaine:
            raise GardeArret("journal non chaîné (boucle statistique) : empreinte et vérification refusées")

    def empreinte(self) -> str:
        self._exiger_chaine()
        return self._chaine[-1] if self._chaine else "0" * 64

    def verifier(self) -> str:
        """Recalcule l'empreinte chaînée depuis les colonnes ; lève si une ligne a été modifiée par-dessous."""
        self._exiger_chaine()
        prec = "0" * 64
        i_ep = {k: 0 for k in ("episodes", "verdicts")}
        for j, (table, n) in enumerate(self._lots):
            src, schema = (self._ep, COLONNES_EPISODE) if table == "episodes" else (self._ve, COLONNES_VERDICT)
            lot = {k: src[k][i_ep[table]] for k in schema}
            if len(lot[next(iter(schema))]) != n:
                raise GardeArret("journal : longueur d'un lot modifiée")
            h = empreinte_octets(prec.encode(), table.encode(), empreinte_tableaux(**lot).encode())
            if h != self._chaine[j]:
                raise GardeArret(f"journal : lot {j} ({table}) modifié après ajout (réécriture détectée)")
            prec = h
            i_ep[table] += 1
        return prec
