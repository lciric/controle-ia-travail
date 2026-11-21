"""Tirer les huit suites d'une action dans un contexte donné, v5 (texte scellé, section 3.2 point 3 ; section 13 ; section 14).

`tirer_suites` : K = 8 suites du modèle de base à partir d'un préfixe en jetons (contexte honnête jusqu'à la coupe), arrêtées au
premier saut de ligne, à la fin de tour ou à 16 jetons ; rend les suites en jetons, leur lecture par `lecture_cout_v5` et
l'empreinte du préfixe. Gardes (un cas sain et un artefact chacune, `tests/test_iib_jumeau_v5.py`) :
- **dose 0 exigée et relue sur le modèle chargé**, avant chaque tirage (`exiger_dose_nulle`) ;
- **aucun texte privé dans le préfixe** : recherche des marqueurs de la consigne, fournis par leur empreinte et leur longueur,
  jamais par leur texte (`exiger_sans_texte_prive`) ;
- **réglages de tirage égaux à ceux de l'agent**, champ par champ (`exiger_reglages_egaux`).

Graines : `Graines` dérive chaque clé de l'entropie de la course comme `manifeste.graines` (même dérivation, donc rejouable par
`manifeste.generateur`), à la demande, et garde la liste des clés employées pour le manifeste.
"""
from __future__ import annotations

import hashlib

import numpy as np

from ..gardes import GardeArret
from ..manifeste import cle_de_tache
from .lecture_cout_v5 import FENETRE, lire_fenetre

CHAMPS_TIRAGE = ("temperature", "coupe_probabilite_cumulee", "jetons_gardes", "penalite_repetition", "penalite_presence",
                 "penalite_frequence")
K_SUITES = 8


class Graines:
    """Graines dérivées par clé d'une entropie (R9) ; `prefixe` : préfixe propre de la course (section 14)."""

    def __init__(self, entropie: int, prefixe: str = ""):
        if isinstance(entropie, bool) or not isinstance(entropie, int) or entropie < 0:
            raise GardeArret(f"entropie {entropie!r} : entier positif attendu (R9 ; champ à remplir par la mère)")
        self.entropie, self.prefixe = int(entropie), str(prefixe)
        self.employees: dict[str, dict] = {}

    def _sequence(self, cle: str) -> np.random.SeedSequence:
        return np.random.SeedSequence(self.entropie, spawn_key=(cle_de_tache(self.prefixe + cle),))

    def generateur(self, cle: str) -> np.random.Generator:
        ss = self._sequence(cle)
        self.employees.setdefault(self.prefixe + cle, {"entropie": str(self.entropie), "spawn_key": [str(cle_de_tache(self.prefixe + cle))],
                                                       "etat_controle": [int(x) for x in ss.generate_state(2)]})
        return np.random.default_rng(ss)

    def entiers(self, cle: str, n: int) -> list[int]:
        return [int(x) for x in self.generateur(cle).integers(0, 2 ** 31 - 1, size=n)]


def cle_du_jumeau(oracle: str, phase: str, episode: str, pas: int) -> str:
    """Clé des suites : `iib/jumeau/<oracle>/<phase>/<episode>/pas<t>`. Aux deux premières actions (pas 0 et 1), les contextes
    des deux oracles sont égaux : les suites y sont tirées une fois, sous la clé de l'oracle au contexte de l'agent."""
    if oracle not in ("N", "P"):
        raise GardeArret(f"oracle {oracle!r} : N ou P")
    return f"iib/jumeau/{'P' if pas <= 1 else oracle}/{phase}/{episode}/pas{pas}"


def empreinte_de_prefixe(ids) -> str:
    return hashlib.sha256(",".join(str(int(i)) for i in ids).encode("ascii")).hexdigest()


def lire_doses(modele) -> list[float]:
    """Doses lues sur le modèle chargé : `modele.doses_lues()` s'il l'offre (modèles jouets) ; sinon sur chaque module
    d'adaptation de `modele.torch` (`organismes.lora`), une liste vide voulant dire « aucun adaptateur injecté »."""
    if hasattr(modele, "doses_lues"):
        return sorted({float(d) for d in modele.doses_lues()})
    if not hasattr(modele, "torch"):
        raise GardeArret("jumeau : la dose ne peut pas être relue sur ce modèle (ni `doses_lues`, ni module PyTorch)")
    from ..organismes.lora import modules_lora

    return sorted({float(m.dose) for m in modules_lora(modele.torch).values()})


def exiger_dose_nulle(modele) -> float:
    doses = lire_doses(modele)
    if doses and doses != [0.0]:
        raise GardeArret(f"jumeau honnête à dose {doses} ≠ 0 : l'oracle exige le modèle de base (refus)")
    return 0.0


def exiger_reglages_egaux(agent: dict, jumeau: dict) -> None:
    for d, nom in ((agent, "de l'agent"), (jumeau, "du jumeau")):
        if not isinstance(d, dict) or set(d) != set(CHAMPS_TIRAGE):
            raise GardeArret(f"réglages de tirage {nom} : champs {sorted(d) if isinstance(d, dict) else d!r} ≠ {sorted(CHAMPS_TIRAGE)}")
    for c in CHAMPS_TIRAGE:
        a, j = agent[c], jumeau[c]
        if isinstance(a, bool) or isinstance(j, bool) or not isinstance(a, (int, float)) or not isinstance(j, (int, float)) or float(a) != float(j):
            raise GardeArret(f"réglages de tirage différents : {c} = {a!r} chez l'agent, {j!r} chez le jumeau (refus)")


def exiger_marqueurs(marqueurs) -> list[tuple[str, int]]:
    sortie = []
    for m in marqueurs or []:
        if not isinstance(m, dict) or set(m) != {"sha256", "longueur"} or not isinstance(m["longueur"], int) or m["longueur"] < 8 \
                or not isinstance(m["sha256"], str) or len(m["sha256"]) != 64:
            raise GardeArret("marqueur de consigne mal formé : {sha256 (64 caractères), longueur (au moins 8 caractères)} attendu, jamais un texte")
        sortie.append((m["sha256"], int(m["longueur"])))
    return sortie


def marqueur_de(texte: str) -> dict:
    """Empreinte et longueur d'un fragment de consigne : fait par l'agent qui a le droit de lire la consigne, jamais ici."""
    return {"sha256": hashlib.sha256(texte.encode("utf-8")).hexdigest(), "longueur": len(texte)}


def exiger_sans_texte_prive(texte: str, marqueurs, deja_verifie: int = 0) -> int:
    """Aucun marqueur de la consigne dans `texte` ; ne relit que les fenêtres qui finissent après `deja_verifie` caractères.
    Rend la longueur vérifiée. Un marqueur trouvé arrête."""
    for sha, n in exiger_marqueurs(marqueurs):
        for i in range(max(0, deja_verifie - n + 1), len(texte) - n + 1):
            if hashlib.sha256(texte[i:i + n].encode("utf-8")).hexdigest() == sha:
                raise GardeArret(f"texte privé dans un préfixe du jumeau (marqueur {sha[:12]}…, position {i}) : arrêt")
    return len(texte)


def tirer_suites(modele, prefixe, reglages_jumeau: dict, reglages_agent: dict, graines: list[int], marqueurs=(),
                 max_jetons: int = FENETRE, K: int = K_SUITES, texte_deja_verifie: int = 0) -> dict:
    """Huit suites du modèle de base à partir de `prefixe` ; les gardes passent avant le tirage."""
    prefixe = list(prefixe)
    if not prefixe or len(graines) != K:
        raise GardeArret(f"jumeau : préfixe vide ou {len(graines)} graines pour {K} suites")
    exiger_reglages_egaux(reglages_agent, reglages_jumeau)
    exiger_dose_nulle(modele)
    tok = modele.fmt.tok
    verifie = texte_deja_verifie
    if marqueurs:
        verifie = exiger_sans_texte_prive(tok.decode(prefixe, skip_special_tokens=False), marqueurs, texte_deja_verifie)
    suites = modele.suites(prefixe, list(graines), int(max_jetons), float(reglages_jumeau["temperature"]))
    if len(suites) != K or any(len(s) > max_jetons for s in suites):
        raise GardeArret(f"jumeau : {len(suites)} suites rendues pour {K} demandées, ou une suite de plus de {max_jetons} jetons")
    fins = frozenset(modele.fmt.fins)
    return {"suites": [list(s) for s in suites], "lectures": [lire_fenetre(tok, s, fins, max_jetons) for s in suites],
            "empreinte": empreinte_de_prefixe(prefixe), "texte_verifie": verifie}
