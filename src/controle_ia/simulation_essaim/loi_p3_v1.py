"""Loi honnête réelle de P3 pour la simulation d'essaim — v1 (préenregistrement hors échantillon).

Source : `donnees/20261019-230011-p3-reel/scores-p3.npz` (sha256 `SHA256`), colonnes `scores` (actions × sondes),
`noms_sondes`, `episode`, `condition`, `pas`. Seules les actions de condition « honnete » sont lues : 60 épisodes de
10 actions (pas 0 à 9), un épisode par tâche.

Construction d'un essaim (K agents × T pas, T = 10) :
- un agent = un épisode honnête entier, rééchantillonné **par épisode entier** (ses 10 scores dans l'ordre des pas) ;
- les K épisodes d'un essaim sont tirés uniformément **sans remise** parmi les 60 (pas deux copies du même épisode dans
  un essaim) ; les essaims sont tirés indépendamment les uns des autres (avec remise entre essaims) ;
- un pas = une action : le pas t de l'essaim aligne l'action t de chacun des K épisodes ;
- scores réduits par la moyenne et l'écart-type regroupés des 600 actions honnêtes de la sonde ; seuil par case
  u = quantile empirique 1 − q de ces 600 scores réduits (méthode « inverted_cdf », valeur observée).

Ce que la construction garde : la marginale de chaque pas, le profil moyen par pas commun à tous les épisodes, l'effet
d'épisode et toute dépendance intra-épisode. Ce qu'elle ne garde pas : aucune corrélation entre agents d'un vrai essaim
(les épisodes de P3 sont indépendants, chacun sur sa tâche ; aucune communication) ; au-delà de 60 épisodes, la
diversité est celle de l'échantillon (un essaim de 10 agents tire 10 des 60 mêmes épisodes).

`charger` vérifie l'empreinte avant toute lecture et refuse un épisode non honnête (`matrice_episodes`).
"""
from __future__ import annotations

import hashlib
from dataclasses import dataclass
from pathlib import Path

import numpy as np

from ..gardes import GardeArret

CHEMIN = "donnees/20261019-230011-p3-reel/scores-p3.npz"
SHA256 = "968414fc7ce7db935c2c4a390a13e2eceebe2fd722628cccb52caf27128004cf"
SONDES = ("tromperie-difference_moyennes-c15", "enjeux-lineaire-c15")   # principale de tromperie, puis enjeux
CONDITION = "honnete"
T_P3 = 10


def empreinte_fichier(chemin: str | Path) -> str:
    h = hashlib.sha256()
    with open(chemin, "rb") as f:
        for bloc in iter(lambda: f.read(1 << 20), b""):
            h.update(bloc)
    return h.hexdigest()


def matrice_episodes(scores, episodes, conditions, pas, ids, T: int = T_P3) -> np.ndarray:
    """(len(ids), T) : scores des épisodes demandés, dans l'ordre des pas. Refuse (liste d'arrêt) un épisode absent,
    un épisode dont une action n'est pas de condition « honnete », ou des pas autres que 0…T − 1."""
    scores, episodes = np.asarray(scores, dtype=float), np.asarray(episodes)
    conditions, pas = np.asarray(conditions), np.asarray(pas)
    sortie = np.empty((len(ids), T))
    for k, e in enumerate(ids):
        lignes = np.flatnonzero(episodes == e)
        if lignes.size == 0:
            raise GardeArret(f"épisode {e!r} absent des données P3")
        if not np.all(conditions[lignes] == CONDITION):
            raise GardeArret(f"épisode {e!r} non honnête ({sorted(set(conditions[lignes].tolist()))}) : refusé")
        o = lignes[np.argsort(pas[lignes], kind="stable")]
        if not np.array_equal(pas[o], np.arange(T)):
            raise GardeArret(f"épisode {e!r} : pas {pas[o].tolist()} ≠ 0…{T - 1}")
        sortie[k] = scores[o]
    if not np.all(np.isfinite(sortie)):
        raise GardeArret("scores P3 non finis (liste d'arrêt)")
    return sortie


@dataclass(frozen=True)
class LoiP3:
    sonde: str
    episodes: tuple
    matrice: np.ndarray            # (n_ep, T), réduite
    moyenne: float                 # moyenne et écart-type regroupés des actions honnêtes, avant réduction
    ecart_type: float
    sha256: str

    @property
    def n_episodes(self) -> int:
        return self.matrice.shape[0]

    @property
    def T(self) -> int:
        return self.matrice.shape[1]

    def seuil_par_case(self, q: float) -> float:
        if not (0.0 < q < 1.0):
            raise GardeArret(f"q = {q} hors de ]0, 1[")
        return float(np.quantile(self.matrice.ravel(), 1.0 - q, method="inverted_cdf"))

    def indices(self, g: np.random.Generator, r: int, K: int) -> np.ndarray:
        """(r, K) : K épisodes distincts par essaim, tirés uniformément sans remise ; essaims indépendants."""
        if not (2 <= K <= self.n_episodes):
            raise GardeArret(f"K = {K} hors de [2, {self.n_episodes}] (épisodes honnêtes disponibles)")
        return np.argsort(g.random((r, self.n_episodes)), axis=1)[:, :K]

    def tirer(self, g: np.random.Generator, r: int, K: int) -> tuple[np.ndarray, np.ndarray]:
        """Scores (r, K, T) puis uniformes de départage (r,), dans cet ordre (R9)."""
        Y = self.matrice[self.indices(g, r, K)]
        return Y, g.random(r)


def charger(chemin: str | Path | None = None, sonde: str = SONDES[0], sha_attendu: str = SHA256,
            racine: str | Path | None = None) -> LoiP3:
    """Vérifie l'empreinte du fichier, puis construit la loi honnête de la sonde (épisodes honnêtes seuls)."""
    p = Path(chemin) if chemin is not None else Path(CHEMIN)
    if racine is not None and not p.is_absolute():
        p = Path(racine) / p
    if not p.is_file():
        raise GardeArret(f"données P3 absentes : {p} (R11 : vérifier sur disque)")
    sha = empreinte_fichier(p)
    if sha != sha_attendu:
        raise GardeArret(f"empreinte de {p} = {sha} ≠ {sha_attendu} attendue (liste d'arrêt)")
    with np.load(p, allow_pickle=False) as d:
        noms = [str(x) for x in d["noms_sondes"]]
        if sonde not in noms:
            raise GardeArret(f"sonde {sonde!r} absente de {p}")
        scores = d["scores"][:, noms.index(sonde)]
        episodes, conditions, pas = d["episode"], d["condition"], d["pas"]
        ids = tuple(sorted(set(episodes[conditions == CONDITION].tolist())))
        brute = matrice_episodes(scores, episodes, conditions, pas, ids)
    mu, sd = float(brute.mean()), float(brute.std())
    if not (sd > 0):
        raise GardeArret(f"sonde {sonde!r} : écart-type nul")
    return LoiP3(sonde=sonde, episodes=ids, matrice=(brute - mu) / sd, moyenne=mu, ecart_type=sd, sha256=sha)
