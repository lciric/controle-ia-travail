"""Pièce 1 — graines : dérivation par tâche (spécification, section 3, « Unité et tirages »).

Règles appliquées :
- toute graine est `numpy.random.SeedSequence(racine, spawn_key=(identifiant de tâche,))` ;
  les flux secondaires d'un même monde (vue, artefact…) ajoutent des clés après
  l'identifiant de tâche (point laissé ouvert dans le rapport) ;
- une racine a au moins 128 bits et vient de la source d'entropie du système ;
- seule l'empreinte d'une racine est consignée avant ses épisodes ; la racine n'est
  révélée qu'après la fin déclarée des épisodes qu'elle sert ;
- une racine qui figure en clair dans un texte lisible avant cette fin : refus ;
- une dérivation qui dépend de l'ordre des tâches (graine globale) : refus.
"""
from __future__ import annotations

import hashlib
import os
from typing import Callable, Hashable, Iterable, Sequence

import numpy as np

from . import RefusDevin

BITS_MIN_RACINE = 128


def exiger_numpy() -> None:
    """R9 : numpy ≥ 1.25 (SeedSequence avec spawn_key)."""
    majeur, mineur = (int(x) for x in np.__version__.split(".")[:2])
    if (majeur, mineur) < (1, 25):
        raise RefusDevin(f"numpy {np.__version__} < 1.25")


def cle_tache(identifiant: Hashable) -> int:
    """Convertit un identifiant de tâche en entier de clé de graine.

    Un entier positif est gardé tel quel ; toute autre valeur passe par sha256
    de sa représentation textuelle (64 bits). Un entier négatif ou un booléen : refus.
    """
    if isinstance(identifiant, bool):
        raise RefusDevin("identifiant de tâche booléen refusé")
    if isinstance(identifiant, (int, np.integer)):
        if identifiant < 0:
            raise RefusDevin(f"identifiant de tâche négatif : {identifiant}")
        return int(identifiant)
    if isinstance(identifiant, str):
        return int.from_bytes(hashlib.sha256(identifiant.encode("utf-8")).digest()[:8], "big")
    raise RefusDevin(f"identifiant de tâche de type {type(identifiant).__name__} refusé")


def exiger_racine(racine: int) -> int:
    if isinstance(racine, bool) or not isinstance(racine, (int, np.integer)):
        raise RefusDevin(f"racine de type {type(racine).__name__} : un entier est exigé")
    racine = int(racine)
    if racine < 0 or racine.bit_length() < BITS_MIN_RACINE - 8:
        # Une racine tirée sur 128 bits a sa longueur ≥ 120 bits sauf avec
        # probabilité 2^-8 · … négligeable ; plus courte = racine choisie à la main.
        raise RefusDevin(f"racine de {racine.bit_length()} bits : au moins {BITS_MIN_RACINE} bits tirés exigés")
    return racine


def graine_tache(racine: int, identifiant: Hashable, *sous_cles: int) -> np.random.SeedSequence:
    """SeedSequence(racine, spawn_key=(identifiant de tâche, *sous_clés))."""
    exiger_numpy()
    racine = exiger_racine(racine)
    cles = (cle_tache(identifiant),) + tuple(int(c) for c in sous_cles)
    return np.random.SeedSequence(racine, spawn_key=cles)


def generateur_tache(racine: int, identifiant: Hashable, *sous_cles: int) -> np.random.Generator:
    return np.random.default_rng(graine_tache(racine, identifiant, *sous_cles))


def tirer_racine() -> int:
    """Racine de 128 bits tirée de la source d'entropie du système (os.urandom)."""
    while True:
        r = int.from_bytes(os.urandom(BITS_MIN_RACINE // 8), "big")
        if r.bit_length() >= BITS_MIN_RACINE - 8:
            return r


def empreinte_racine(racine: int) -> str:
    """sha256 de l'écriture hexadécimale minuscule de la racine."""
    return hashlib.sha256(format(int(racine), "x").encode("ascii")).hexdigest()


class RacineScellee:
    """Racine dont seule l'empreinte est publique jusqu'à la fin déclarée.

    `racine_interne()` sert au tireur du harnais (seul). `reveler()` n'est permis
    qu'après `declarer_fin()` ; avant, refus.
    """

    def __init__(self, nom: str, racine: int | None = None):
        self.nom = nom
        self._racine = exiger_racine(tirer_racine() if racine is None else racine)
        self.empreinte = empreinte_racine(self._racine)
        self._fin = False

    def racine_interne(self) -> int:
        return self._racine

    def declarer_fin(self) -> None:
        self._fin = True

    @property
    def fin_declaree(self) -> bool:
        return self._fin

    def reveler(self) -> int:
        if not self._fin:
            raise RefusDevin(f"racine {self.nom!r} : révélation avant la fin déclarée de ses épisodes")
        return self._racine

    def __repr__(self) -> str:  # jamais la racine en clair
        return f"RacineScellee({self.nom!r}, empreinte={self.empreinte[:12]}…, fin={self._fin})"


def verifier_racine_revelee(racine: int, empreinte: str) -> None:
    if empreinte_racine(racine) != empreinte:
        raise RefusDevin("racine révélée : empreinte différente de celle consignée")


def formes_en_clair(racine: int) -> list[str]:
    r = int(racine)
    return [str(r), format(r, "x"), format(r, "X"), hex(r)]


def verifier_racine_absente(racine: int, textes: Iterable[str | bytes]) -> None:
    """Refus si la racine figure en clair (décimale ou hexadécimale) dans un texte."""
    formes = formes_en_clair(racine)
    for i, t in enumerate(textes):
        s = t.decode("utf-8", errors="replace") if isinstance(t, (bytes, bytearray)) else str(t)
        for f in formes:
            if f in s:
                raise RefusDevin(f"racine en clair dans le texte n° {i} (forme {f[:6]}…)")


def verifier_invariance_ordre(
    tirage: Callable[[Sequence[Hashable]], dict], identifiants: Sequence[Hashable], graine_permutation: np.random.SeedSequence
) -> None:
    """Garde contre la graine globale : les tirages d'une tâche ne dépendent pas de l'ordre.

    `tirage(ids)` rend {identifiant: valeur} en tirant les tâches dans l'ordre donné.
    On compare l'ordre donné, l'ordre renversé et un ordre permuté.
    """
    ids = list(identifiants)
    if len(ids) < 2:
        raise RefusDevin("invariance d'ordre : au moins deux tâches exigées")
    perm = np.random.default_rng(graine_permutation).permutation(len(ids))
    ordres = [ids, ids[::-1], [ids[k] for k in perm]]
    ref = tirage(ordres[0])
    for o in ordres[1:]:
        autre = tirage(o)
        for i in ids:
            if not np.array_equal(np.asarray(ref[i]), np.asarray(autre[i])):
                raise RefusDevin(f"tirage de la tâche {i!r} change avec l'ordre des tâches : graine globale")
