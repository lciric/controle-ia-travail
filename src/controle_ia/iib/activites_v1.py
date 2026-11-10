"""Activité interne enregistrée de (ii-b) (GO-2026-11-10-08, R-2175, D-4 (a) : « avec l'activité interne enregistrée »),
ajout au code v1 sur mot de la mère ; **aucune sonde n'est apprise, appliquée ni lue** par ce code : l'enregistrement sert
une lecture ultérieure sous préenregistrement scellé à part, après le verdict scellé de P3-bis (DT-4, R-2044).

Choix déclaré du développeur : l'extracteur de T0.7 n'a pas été lu (tout fichier de T0.7 est interdit à ce développeur) ;
couches et format sont donc ceux de T0.6 (configuration du candidat 12, brouillon 5 : couches 7, 15 et 23 ; `ActivationsDemi`
de `t06.lanceur_v2` : jetons des actions, une matrice (jetons, largeur) par action et par couche, demi-précision, aucun
arrondi silencieux hors de la demi-précision). Une concordance avec l'extracteur de T0.7 reste à faire par la mère ou un
lecteur autorisé.

Ce qui est enregistré : pour chaque épisode d'évaluation (conditions H, B50, B100, TJ100), une passe avant unique sur sa
transcription (`harnais.activations.passe_unique`), **dans l'état d'adaptateur et à la dose qui l'ont généré** (état relu
avant et après) ; tous les jetons de chaque action (empan exact de la transcription, jamais retokenisé). Aucune réduction sur
les jetons (ni moyenne, ni médiane, ni maximum). Écrit en morceaux npz (≤ 90 Mo par fichier, borne du dépôt distant de
T0.6), chacun scellé, et un index scellé (clé, morceau, couche, forme).
"""
from __future__ import annotations

import io
import json
from pathlib import Path

import numpy as np

from ..gardes import GardeArret
from ..scellement import sceller

FLOAT16_MAX = float(np.finfo(np.float16).max)
MORCEAU_MAX_OCTETS = 90_000_000
REMPLISSAGE_MAX_OCTETS = 85_000_000
COUCHES_T06 = (7, 15, 23)


class ActivitesIib:
    def __init__(self, dossier: Path, couches, prefixe: str = "activations-iib"):
        self.dossier = Path(dossier)
        if self.dossier.exists():
            raise GardeArret(f"{self.dossier} existe déjà (R12)")
        self.dossier.mkdir(parents=True)
        self.couches = [int(c) for c in couches]
        if not self.couches:
            raise GardeArret("activité interne : aucune couche")
        self.prefixe = prefixe
        self.tampon: dict[str, np.ndarray] = {}
        self.octets = 0
        self.morceaux: list[dict] = []
        self.index: list[dict] = []
        self.noms: set[str] = set()

    def ajouter(self, cle: str, segments: dict[int, np.ndarray]) -> None:
        prets = {}
        for c in self.couches:
            if c not in segments:
                raise GardeArret(f"activité interne : couche {c} absente pour {cle}")
            a = np.asarray(segments[c], dtype=np.float32)
            if a.ndim != 2 or a.shape[0] < 1:
                raise GardeArret(f"activité interne : forme {a.shape} pour {cle}, couche {c}")
            if not np.all(np.isfinite(a)) or float(np.abs(a).max(initial=0.0)) > FLOAT16_MAX:
                raise GardeArret(f"activation non finie ou hors de la demi-précision ({cle}, couche {c}) : aucun arrondi silencieux")
            nom = f"{cle}|c{c}"
            if nom in self.noms:
                raise GardeArret(f"activité interne : {nom} déjà écrite (R12)")
            h = a.astype(np.float16)
            if h.nbytes > REMPLISSAGE_MAX_OCTETS:
                raise GardeArret(f"activité interne : {nom} seule dépasse un morceau")
            prets[nom] = h
        for nom, h in prets.items():                      # rien n'est ajouté tant qu'une couche est en défaut
            if self.octets + h.nbytes > REMPLISSAGE_MAX_OCTETS:
                self.vider()
            self.tampon[nom] = h
            self.noms.add(nom)
            self.octets += h.nbytes

    def vider(self) -> None:
        if not self.tampon:
            return
        n = len(self.morceaux)
        chemin = self.dossier / f"{self.prefixe}-{n:04d}.npz"
        if chemin.exists():
            raise GardeArret(f"{chemin} existe déjà (R12)")
        noms = sorted(self.tampon)
        tampon = io.BytesIO()
        np.savez(tampon, **{f"a{k}": self.tampon[x] for k, x in enumerate(noms)})
        if tampon.getbuffer().nbytes > MORCEAU_MAX_OCTETS:
            raise GardeArret(f"morceau {n} : {tampon.getbuffer().nbytes} octets > {MORCEAU_MAX_OCTETS}")
        chemin.write_bytes(tampon.getvalue())
        sha = sceller(chemin)
        self.morceaux.append({"fichier": chemin.name, "sha256": sha, "tableaux": len(noms)})
        for k, x in enumerate(noms):
            cle, _, c = x.rpartition("|c")
            self.index.append({"nom": x, "cle": cle, "couche": int(c), "morceau": chemin.name, "tableau": f"a{k}",
                               "forme": list(self.tampon[x].shape)})
        self.tampon, self.octets = {}, 0

    def clore(self) -> dict:
        self.vider()
        chemin = self.dossier / f"index-{self.prefixe}.json"
        corps = {"couches": self.couches, "format": "float16, (jetons, largeur) par action et par couche",
                 "morceaux": self.morceaux, "tableaux": self.index}
        chemin.write_text(json.dumps(corps, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")
        return {"index": chemin.name, "sha256_index": sceller(chemin), "morceaux": len(self.morceaux),
                "tableaux": len(self.index), "octets": int(sum((self.dossier / m["fichier"]).stat().st_size for m in self.morceaux))}
