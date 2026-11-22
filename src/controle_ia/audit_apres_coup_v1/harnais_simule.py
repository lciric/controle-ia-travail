"""Le harnais simulé des épreuves de la boucle (rang 11 ; section 5), mondes plantés seulement.

Ce qui est écrit :
- **jeton de provenance** : toute entrée porte un jeton « monde planté » émis par `graines.py` avec l'empreinte du
  fichier de vérité plantée ; une entrée sans ce jeton (poids d'une sonde du programme, verdict d'un oracle réel, état
  d'un organisme) reçoit le refus nommé « hors monde planté » ; un contenu réel recopié sous un jeton valide est
  refusé aussi (re-dérivation depuis la graine) ;
- **interdit entier** : toute entrée de lignée est refusée, sans exception. Le mode « bras de flux » n'est pas écrit
  (nœud : mot du directeur sur la règle (b′)) ; aucune configuration ne l'ouvre ;
- versions nommées par empreinte, à lignée vide ;
- un rôle par épisode, écrit avant le verdict ;
- registres en ajout seul : témoins à deux usages disjoints (épreuve 6), plis tirés par le harnais et marqués
  « consommé » (épreuve 5), regards (épreuve 8).

Ce qui n'est pas écrit : l'enclave et ses jetons de capacité (épreuve 13), les cinq refus de lignée et de rôle
(épreuve 1), le mode « bras de flux ».

Les sondes de ces mondes sont des **directions plantées** dans un monde gaussien, instruites par des étiquettes de la
vérité plantée ; aucune sonde du programme n'est touchée, aucun verdict d'un oracle réel n'entre ; les gardes sont des
fonctions pures de ce que le harnais consigne. Elles ne couvrent pas une modification du harnais lui-même.
"""
from __future__ import annotations

import numpy as np

from ..gardes import GardeArret
from .graines import JetonProvenance, empreinte_octets, verifier_provenance

REFUS_LIGNEE = "interdit entier : toute entrée de lignée est refusée (le mode « bras de flux » n'est pas écrit)"
ROLES_ADMIS = ("verdict", "hors rôle")
REFUS_PLI_CONSOMME = "pli consommé : il a servi à choisir, il ne porte plus d'annonce"
REFUS_TEMOINS = "témoins : un même témoin sert à instruire et à calibrer"


class HarnaisSimule:
    def __init__(self):
        self._admis: list[str] = []
        self._versions: dict[str, tuple] = {}
        self._roles: dict[int, tuple[str, int]] = {}

    # --- provenance ------------------------------------------------------------------------------
    def admettre(self, contenu: bytes, jeton: JetonProvenance | None) -> bytes:
        verifier_provenance(contenu, jeton)
        self._admis.append(jeton.empreinte_contenu)
        return contenu

    # --- lignée et versions ----------------------------------------------------------------------
    def ajouter_lignee(self, *args, **kwargs):
        raise GardeArret(REFUS_LIGNEE)

    def sceller_version(self, octets_direction: bytes, lignee: tuple = ()) -> str:
        if lignee:
            raise GardeArret(REFUS_LIGNEE)
        nom = empreinte_octets(octets_direction)
        if nom in self._versions:
            raise GardeArret("version déjà scellée sous ce nom")
        self._versions[nom] = ()
        return nom

    def lignee(self, nom: str) -> tuple:
        if nom not in self._versions:
            raise GardeArret("version inconnue")
        return self._versions[nom]

    # --- rôles ----------------------------------------------------------------------------------
    def ecrire_role(self, episode: int, role: str, horloge: int) -> None:
        if role not in ROLES_ADMIS:
            raise GardeArret(f"rôle {role!r} refusé : seuls {ROLES_ADMIS} existent tant que le bras de flux n'est pas écrit")
        if episode in self._roles:
            raise GardeArret("rôle déjà écrit (ajout seul)")
        self._roles[episode] = (role, horloge)

    def verifier_roles_avant_verdict(self, journal) -> None:
        e = journal.colonne("v_episode")
        h = journal.colonne("v_h_verdict")
        for ep, hv in zip(e.tolist(), h.tolist()):
            if ep not in self._roles:
                raise GardeArret(f"épisode {ep} jugé sans rôle écrit")
            if self._roles[ep][1] >= hv:
                raise GardeArret(f"épisode {ep} : rôle écrit après le verdict")


class RegistreTemoins:
    """Témoins exogènes plantés à deux usages disjoints : « lecon » (négatifs qui donnent sa direction à la sonde) et
    « calibrage » (qui donnent son seuil)."""

    USAGES = ("lecon", "calibrage")

    def __init__(self):
        self._usage: dict[int, str] = {}

    def reserver(self, ids, usage: str) -> None:
        if usage not in self.USAGES:
            raise GardeArret(f"usage de témoin inconnu {usage!r}")
        ids = [int(i) for i in ids]
        for i in ids:
            if self._usage.get(i, usage) != usage:
                raise GardeArret(REFUS_TEMOINS)
        for i in ids:
            self._usage[i] = usage

    def exiger(self, ids, usage: str) -> None:
        for i in ids:
            if self._usage.get(int(i)) != usage:
                raise GardeArret(f"témoin {int(i)} non réservé à l'usage {usage!r}" +
                                 (f" (réservé à {self._usage[int(i)]!r} : {REFUS_TEMOINS})" if int(i) in self._usage else ""))


class RegistrePlis:
    """Plis retenus, tirés par le harnais ; un pli qui a servi à choisir est consommé."""

    def __init__(self):
        self._plis: dict[int, dict] = {}
        self._suivant = 0

    def tirer(self, ids: np.ndarray, taux: float, rng: np.random.Generator) -> int:
        ids = np.asarray(ids)
        sel = ids[rng.random(len(ids)) < taux]
        k = self._suivant
        self._plis[k] = {"ids": sel, "consomme": False}
        self._suivant += 1
        return k

    def ids(self, k: int) -> np.ndarray:
        return self._plis[k]["ids"]

    def utiliser_pour_choisir(self, k: int) -> np.ndarray:
        p = self._plis[k]
        if p["consomme"]:
            raise GardeArret(REFUS_PLI_CONSOMME)
        p["consomme"] = True
        return p["ids"]

    def annoncer(self, k: int) -> np.ndarray:
        p = self._plis[k]
        if p["consomme"]:
            raise GardeArret(REFUS_PLI_CONSOMME)
        return p["ids"]

    def consomme(self, k: int) -> bool:
        return self._plis[k]["consomme"]


class RegistreRegards:
    """On ajoute, on ne remplace pas : toute lecture d'un regard reste consignée."""

    def __init__(self):
        self._lectures: list[tuple[str, int, int]] = []

    def consigner(self, regard: str, episode: int, lecture: int) -> None:
        self._lectures.append((regard, int(episode), int(lecture)))

    def remplacer(self, *args, **kwargs):
        raise GardeArret("regards : on ajoute, on ne remplace pas")

    def lectures(self, regard: str) -> list[tuple[int, int]]:
        return [(e, l) for r, e, l in self._lectures if r == regard]
