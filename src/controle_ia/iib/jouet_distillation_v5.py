"""Monde jouet de la distillation de l'organisme retenu, v5 : entrées **factices** pour les essais (aucun torch, aucun poids).

- `MoteurJouet` : tient lieu de `distillation_v5.MoteurTorch`. Il ne distille rien : la « base » est une suite d'octets, un
  « adaptateur » un couple (A tirée d'une graine, B nul avant l'entraînement, fonction des exemples après), les « logits de
  contrôle » un couple (empreinte de la base et du contexte, dose × B). Il permet de jouer l'ordre des opérations et de planter
  les artefacts des gardes (`defaut`) : base touchée par l'entraînement, adaptateur actif à dose 0, adaptateur sans effet à
  dose 1, perte non finie, recharge infidèle.
- `ModeleJouetEleve` : le modèle jouet de langue, dont l'agent gonfle son coût de `dose × excès de l'adaptateur chargé` à
  partir de la deuxième action. **Il ne mesure rien et ne prouve aucun apprentissage** : il permet de jouer la chaîne
  (distillation, quatre conditions, deux oracles) de bout en bout.
"""
from __future__ import annotations

import hashlib
import json
import math
import re
from pathlib import Path

from ..gardes import GardeArret
from .jouet_v5 import SIGNAL_FLAGRANT, SIGNAL_MAITRE, ModeleJouetDeLangue

# Motifs de mention **factices** du monde jouet (aucun motif de T0.6 ni de la consigne) : ceux des essais du distillateur, pour
# le point d'entrée de la course en mode jouet (correctif 0015) ; en mode réel, `distillation_v5.motifs_de_la_course`.
MOTIFS_JOUET = {"t06:01": re.compile("private note", re.I), "t06:02": re.compile("three times", re.I), "iib:01": re.compile("FACTICE-MOTIF", re.I)}
DEFAUTS = (None, "base_touchee", "actif_a_dose_0", "sans_effet", "perte_non_finie", "recharge_infidele")


class ModeleJouetEleve(ModeleJouetDeLangue):
    def __init__(self, jouet: dict | None = None, tok=None, exces: dict | None = None):
        super().__init__(jouet, tok)
        self.adaptateur_charge = None
        self.exces = {"eleve": math.log10(2.0), "temoin-jumeau": 0.0, **(exces or {})}

    def _exces_de_politique(self, contexte: str, pas: int, rng) -> float:
        e = super()._exces_de_politique(contexte, pas, rng)
        if pas >= 1 and SIGNAL_FLAGRANT not in contexte and SIGNAL_MAITRE not in contexte:
            e += float(self.dose) * self.exces.get(self.adaptateur_charge, 0.0)
        return e


def _sha(*morceaux) -> str:
    return hashlib.sha256(json.dumps(morceaux, sort_keys=True).encode("utf-8")).hexdigest()


class MoteurJouet:
    reel = False

    def __init__(self, modele, defaut: str | None = None):
        if defaut not in DEFAUTS:
            raise GardeArret(f"moteur jouet : défaut {defaut!r} inconnu")
        self.modele, self.defaut = modele, defaut
        self.base = "poids-de-base-factices"
        self.courant: dict | None = None
        self.etats: dict[str, dict] = {}
        self.injecte = self.simple = False
        self.journal: list[str] = []

    def _b_actif(self) -> float:
        return 0.0 if self.courant is None else float(self.courant["B"])

    def logits_de_controle(self, ids):
        dose = float(self.modele.dose) if self.courant is not None else 0.0
        if self.defaut == "actif_a_dose_0" and self._b_actif() != 0.0:
            dose = max(dose, 0.5)
        return (_sha(self.base, list(ids)), round(dose * self._b_actif(), 12))

    def logits_egaux(self, a, b) -> bool:
        return a == b

    def ecart_max(self, a, b) -> float:
        return abs(a[1] - b[1])

    def empreinte_base(self) -> str:
        return _sha(self.base)

    def empreinte_adaptateurs(self) -> str:
        if self.courant is None:
            raise GardeArret("aucun adaptateur dans le modèle")
        return _sha(self.courant["A"], self.courant["B"])

    def vider_caches(self) -> None:
        self.journal.append("caches")

    def injecter(self, rang: int, alpha: float, graine: int, cibles: list) -> list:
        if self.injecte:
            raise GardeArret("le modèle porte déjà des adaptateurs : une seule injection")
        self.injecte = True
        self.courant = {"nom": None, "A": [int(graine), int(rang)], "B": 0.0}
        self.journal.append("injection")
        return [f"couche0.{c}" for c in cibles]

    def simple_precision(self) -> int:
        self.simple = True
        return 4

    def initialiser(self, nom: str, rang: int, alpha: float, graine: int) -> None:
        if not self.injecte or not self.simple:
            raise GardeArret("moteur jouet : état initial avant l'injection ou avant la simple précision")
        self.courant = {"nom": nom, "A": [int(graine), int(rang)], "B": 0.0}
        self.modele.adaptateur_charge = nom
        self.journal.append(f"initial:{nom}")

    def fixer_dose(self, dose: float) -> None:
        if not 0.0 <= float(dose) <= 1.0:
            raise GardeArret(f"dose {dose} hors de [0, 1]")
        self.modele.dose = float(dose)

    def dose(self):
        return float(self.modele.dose)

    def entrainer(self, exemples, epoques: int, pas: float, lot: int, graine: int, norme_max: float, progres) -> list:
        if not exemples:
            raise GardeArret("aucune transcription de distillation")
        for k, (i, e) in enumerate(exemples):
            if not i or len(i) != len(e) or all(x == -100 for x in e[1:]):
                raise GardeArret(f"transcription {k} : longueurs différentes, vide, ou sans jeton cible")
        if float(self.modele.dose) != 1.0:
            raise GardeArret("moteur jouet : entraînement hors de la dose 1")
        empreinte = _sha([list(e) for _, e in exemples], int(graine), self.courant["A"])
        self.courant["B"] = 0.0 if self.defaut == "sans_effet" else 0.25 + int(empreinte[:8], 16) / 2 ** 33
        if self.defaut == "base_touchee":
            self.base += "+"
        journal = [{"epoque": 0, "perte": 2.0}]
        for ep in range(1, int(epoques) + 1):
            perte = float("nan") if self.defaut == "perte_non_finie" else 2.0 / (1 + ep)
            journal.append({"epoque": ep, "perte": perte})
            if progres is not None:
                progres(ep, perte)
        self.journal.append(f"entrainement:{self.courant['nom']}:{len(exemples)}")
        return journal

    def sauver_et_recharger(self, nom: str, chemin, precision: str) -> None:
        etat = {"nom": nom, "A": list(self.courant["A"]), "B": round(float(self.courant["B"]), 4), "precision": precision}
        Path(chemin).write_text(json.dumps(etat, sort_keys=True) + "\n", encoding="utf-8")
        self.etats[nom] = json.loads(Path(chemin).read_text(encoding="utf-8"))
        self.charger(nom, fidele=True)

    def charger(self, nom: str, fidele: bool = False) -> None:
        if nom not in self.etats:
            raise GardeArret(f"adaptateur {nom!r} jamais sauvegardé : rien à charger (refus)")
        e = self.etats[nom]
        b = e["B"] + (0.125 if self.defaut == "recharge_infidele" and not fidele else 0.0)
        self.courant = {"nom": nom, "A": list(e["A"]), "B": b}
        self.modele.adaptateur_charge = nom
        self.journal.append(f"charge:{nom}")
