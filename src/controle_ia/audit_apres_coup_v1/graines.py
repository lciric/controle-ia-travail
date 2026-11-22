"""Graines et flux de tirage séparés par canal (rang 1), jeton de provenance « monde planté » (section 5).

Spécification, section 1 : « La graine est `SeedSequence(entropie déclarée, spawn_key=(monde, tâche, épisode, canal))`,
avec un canal par grandeur » ; six canaux : enjeu, dommage, score, pièce, oracle, lisibilité. « Les flux sont séparés :
permuter les scores ne change donc aucun octet de la pièce. »

Deux modes, tous deux par `numpy.random.SeedSequence` (R9) :
- `generateur_episode` : la clé exacte de la spécification, (monde, tâche, épisode, canal) ; un générateur par épisode ;
- `flux_tache` : un flux par (monde, tâche, canal), dont l'épisode est le rang du tirage dans le flux (un uniforme par
  épisode et par canal). C'est le mode du simulateur vectorisé : la clé par épisode coûte un `SeedSequence` par
  épisode et par canal, hors de portée pour R = 2 000 répétitions de 10 000 épisodes. L'écart est un point laissé
  ouvert du rapport ; les deux modes gardent la séparation des flux, seule propriété dont dépendent les épreuves.

Chaque canal consomme exactement un uniforme par épisode, quel que soit ce qui se passe dans l'épisode : aucun tirage
d'un canal ne dépend d'un autre canal.
"""
from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass
from typing import Callable

import numpy as np

from ..gardes import GardeArret

CANAUX = ("enjeu", "dommage", "score", "piece", "oracle", "lisibilite")
PROVENANCE_MONDE_PLANTE = "monde planté"
REFUS_HORS_MONDE = "hors monde planté"


def _verifier_numpy() -> None:
    major, minor = (int(x) for x in np.__version__.split(".")[:2])
    if (major, minor) < (1, 25):
        raise GardeArret(f"numpy {np.__version__} < 1.25 : R9 exige numpy >= 1.25")


def indice_canal(canal: str) -> int:
    if canal not in CANAUX:
        raise GardeArret(f"canal inconnu {canal!r} ; canaux déclarés : {CANAUX}")
    return CANAUX.index(canal)


def _cle(*parties: int) -> tuple[int, ...]:
    out = []
    for p in parties:
        if isinstance(p, bool) or not isinstance(p, (int, np.integer)) or int(p) < 0:
            raise GardeArret(f"clé de graine invalide {p!r} : entiers positifs ou nuls seulement")
        out.append(int(p))
    return tuple(out)


def generateur_episode(entropie: int, monde: int, tache: int, episode: int, canal: str) -> np.random.Generator:
    """Générateur à la clé exacte de la spécification (monde, tâche, épisode, canal)."""
    _verifier_numpy()
    ss = np.random.SeedSequence(int(entropie), spawn_key=_cle(monde, tache, episode, indice_canal(canal)))
    return np.random.default_rng(ss)


def flux_tache(entropie: int, monde: int, tache: int, canal: str) -> np.random.Generator:
    """Flux d'un canal pour une tâche : l'épisode i y lit son i-ième uniforme."""
    _verifier_numpy()
    ss = np.random.SeedSequence(int(entropie), spawn_key=_cle(monde, tache, indice_canal(canal)))
    return np.random.default_rng(ss)


def generateur_auxiliaire(entropie: int, *cle: int) -> np.random.Generator:
    """Générateur d'un monde gaussien des épreuves (clé déclarée par l'épreuve, préfixée de 1 000 pour ne jamais
    coïncider avec un flux de canal)."""
    _verifier_numpy()
    return np.random.default_rng(np.random.SeedSequence(int(entropie), spawn_key=_cle(1000, *cle)))


class Flux:
    """Les six flux d'une tâche ; `tirer(canal, n)` rend les n uniformes suivants du canal, dans l'ordre."""

    def __init__(self, entropie: int, monde: int, tache: int):
        self.entropie, self.monde, self.tache = int(entropie), int(monde), int(tache)
        self._gen = {c: flux_tache(entropie, monde, tache, c) for c in CANAUX}
        self._lus = {c: 0 for c in CANAUX}

    def tirer(self, canal: str, n: int) -> np.ndarray:
        indice_canal(canal)
        if n < 0:
            raise GardeArret("nombre de tirages négatif")
        self._lus[canal] += int(n)
        return self._gen[canal].random(int(n))

    def lus(self, canal: str) -> int:
        return self._lus[canal]


def empreinte_octets(*morceaux: bytes) -> str:
    h = hashlib.sha256()
    for m in morceaux:
        h.update(len(m).to_bytes(8, "little"))
        h.update(m)
    return h.hexdigest()


def empreinte_tableaux(**tableaux: np.ndarray) -> str:
    """Empreinte stable de tableaux nommés (nom, type, forme, octets)."""
    morceaux = []
    for nom in sorted(tableaux):
        a = np.ascontiguousarray(tableaux[nom])
        morceaux += [nom.encode(), str(a.dtype).encode(), json.dumps(a.shape).encode(), a.tobytes()]
    return empreinte_octets(*morceaux)


# ------------------------------------------------------------------------------------------------
# Jeton de provenance « monde planté » (section 5)
# ------------------------------------------------------------------------------------------------
@dataclass(frozen=True)
class JetonProvenance:
    """Lie l'empreinte du contenu d'une entrée à sa graine et à l'empreinte du fichier de vérité plantée."""

    provenance: str
    entropie: int
    cle: tuple[int, ...]
    derivation: str
    empreinte_contenu: str
    empreinte_verite: str


# Registre des fonctions de dérivation : nom -> f(entropie, cle) -> octets du contenu. Le harnais re-dérive l'entrée
# depuis sa graine par ce registre, et refuse si l'empreinte diffère.
DERIVATIONS: dict[str, Callable[[int, tuple[int, ...]], bytes]] = {}


def enregistrer_derivation(nom: str, fonction: Callable[[int, tuple[int, ...]], bytes]) -> None:
    if nom in DERIVATIONS and DERIVATIONS[nom] is not fonction:
        raise GardeArret(f"dérivation {nom!r} déjà enregistrée avec une autre fonction")
    DERIVATIONS[nom] = fonction


def emettre_jeton(entropie: int, cle: tuple[int, ...], derivation: str, empreinte_verite: str) -> tuple[bytes, JetonProvenance]:
    """Dérive le contenu depuis la graine et émet son jeton. Seul `graines.py` émet des jetons."""
    if derivation not in DERIVATIONS:
        raise GardeArret(f"dérivation inconnue {derivation!r} : aucun jeton émis")
    if not (isinstance(empreinte_verite, str) and len(empreinte_verite) == 64):
        raise GardeArret("empreinte de la vérité plantée absente ou mal formée : aucun jeton émis")
    contenu = DERIVATIONS[derivation](int(entropie), _cle(*cle))
    jeton = JetonProvenance(PROVENANCE_MONDE_PLANTE, int(entropie), _cle(*cle), derivation,
                            empreinte_octets(contenu), empreinte_verite)
    return contenu, jeton


def verifier_provenance(contenu: bytes, jeton: JetonProvenance | None) -> None:
    """Refus nommé « hors monde planté » : jeton absent, provenance autre, contenu qui ne correspond pas au jeton, ou
    contenu re-dérivé de la graine qui diffère (un contenu réel recopié sous un jeton valide est refusé aussi)."""
    if not isinstance(jeton, JetonProvenance):
        raise GardeArret(f"{REFUS_HORS_MONDE} : entrée sans jeton de provenance")
    if jeton.provenance != PROVENANCE_MONDE_PLANTE:
        raise GardeArret(f"{REFUS_HORS_MONDE} : provenance {jeton.provenance!r}")
    if not isinstance(contenu, (bytes, bytearray)):
        raise GardeArret(f"{REFUS_HORS_MONDE} : contenu non sérialisé")
    if empreinte_octets(bytes(contenu)) != jeton.empreinte_contenu:
        raise GardeArret(f"{REFUS_HORS_MONDE} : le contenu ne correspond pas à l'empreinte du jeton")
    if jeton.derivation not in DERIVATIONS:
        raise GardeArret(f"{REFUS_HORS_MONDE} : dérivation {jeton.derivation!r} inconnue")
    rederive = DERIVATIONS[jeton.derivation](jeton.entropie, jeton.cle)
    if empreinte_octets(rederive) != jeton.empreinte_contenu:
        raise GardeArret(f"{REFUS_HORS_MONDE} : le contenu re-dérivé de la graine diffère")
