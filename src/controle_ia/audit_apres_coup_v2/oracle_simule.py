"""L'oracle simulé (rang 4 ; section 1, « Oracle »).

Couverture q (probabilité de dire « endommagé » un épisode endommagé qu'il regarde), taux de faux « endommagé » f (nul
en régime de signature), délai L compté en épisodes endommagés : le verdict de l'épisode i se lit à la fin du premier
épisode j ≥ i tel que L épisodes endommagés soient survenus dans (i, j] (j = i si L = 0). Un verdict dont le délai ne
s'achève pas dans le monde n'est pas rendu (aucun événement, jamais une valeur par défaut).

L'oracle ne lit que ce que `entrees_oracle` sérialise : l'identifiant de l'épisode, l'empreinte de son enregistrement
et l'ordre de présentation tiré par le harnais. Ni score, ni version, ni source du tirage (épreuve 9, clause 8).
"""
from __future__ import annotations

from dataclasses import dataclass

import numpy as np

from ..gardes import GardeArret
from .journal import DECALAGES, PAS

REFUS_AVANT_DELAI = "verdict lu avant son délai"


@dataclass(frozen=True)
class OracleSimule:
    q: float
    f: float
    L: int
    regime: str  # « signature » ou « exces »

    def __post_init__(self):
        if not (0 < self.q <= 1):
            raise GardeArret("oracle : couverture q hors de ]0, 1] (q = 0 se déclare par sorte de dommage, épreuve 12)")
        if not (0 <= self.f < 1):
            raise GardeArret("oracle : f hors de [0, 1[")
        if self.regime not in ("signature", "exces"):
            raise GardeArret(f"oracle : régime inconnu {self.regime!r}")
        if self.regime == "signature" and self.f != 0:
            raise GardeArret("oracle : en régime de signature, f = 0 (oracle à faux positifs non traité)")
        if int(self.L) != self.L or self.L < 0:
            raise GardeArret("oracle : délai L entier positif ou nul")

    def verdicts(self, dommage: np.ndarray, u_oracle: np.ndarray, q_par_episode: np.ndarray | None = None) -> np.ndarray:
        """Verdict qu'il rendrait sur chaque épisode s'il le regardait (1 endommagé, 0 sain).
        `q_par_episode` permet une couverture par sorte de dommage (q = 0 sur une sorte : épreuve 12)."""
        d = np.asarray(dommage, dtype=bool)
        u = np.asarray(u_oracle, dtype=float)
        q = self.q if q_par_episode is None else np.asarray(q_par_episode, dtype=float)
        return np.where(d, u < q, u < self.f).astype(np.int8)

    def episode_de_lecture(self, dommage: np.ndarray) -> np.ndarray:
        """Indice de l'épisode à la fin duquel le verdict de chaque épisode se lit ; -1 si le délai déborde le monde."""
        d = np.asarray(dommage, dtype=np.int64)
        n = len(d)
        idx = np.arange(n)
        if self.L == 0:
            return idx
        cum = np.cumsum(d)
        j = np.searchsorted(cum, cum + self.L, side="left")
        return np.where(j < n, j, -1)


def heure_de_lecture(episode_lecture: np.ndarray) -> np.ndarray:
    e = np.asarray(episode_lecture, dtype=np.int64)
    return np.where(e >= 0, PAS * e + DECALAGES["h_verdict"], -1)


def lire_verdict(journal, episode: int, horloge: int) -> int:
    """Lecture d'un verdict à l'instant `horloge` ; refus nommé s'il n'est pas encore lisible."""
    v, h = journal.verdicts_par_episode()
    if episode < 0 or episode >= len(v):
        raise GardeArret("épisode inconnu du journal")
    if h[episode] < 0:
        raise GardeArret(f"{REFUS_AVANT_DELAI} : aucun verdict rendu pour l'épisode {episode}")
    if horloge < h[episode]:
        raise GardeArret(f"{REFUS_AVANT_DELAI} : épisode {episode}, heure {h[episode]}, lu à {horloge}")
    return int(v[episode])


def entrees_oracle(episodes: np.ndarray, empreintes_enregistrement: list[str], ordre: np.ndarray,
                   champs_en_plus: dict | None = None) -> bytes:
    """Sérialise ce que lit l'oracle. `champs_en_plus` n'existe que pour l'artefact de l'épreuve 9 (« source du
    tirage ») : un oracle qui les lit n'est plus aveugle, et l'épreuve doit échouer."""
    e = np.asarray(episodes, dtype=np.int64)
    o = np.asarray(ordre, dtype=np.int64)
    if len(e) != len(empreintes_enregistrement) or sorted(o.tolist()) != list(range(len(e))):
        raise GardeArret("entrées de l'oracle : ordre de présentation invalide")
    lignes = []
    for k in o:
        ligne = f"{int(e[k])}|{empreintes_enregistrement[k]}"
        if champs_en_plus:
            ligne += "|" + "|".join(f"{c}={champs_en_plus[c][k]}" for c in sorted(champs_en_plus))
        lignes.append(ligne)
    return ("\n".join(lignes)).encode()
