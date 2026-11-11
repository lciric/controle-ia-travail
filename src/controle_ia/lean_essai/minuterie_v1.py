"""Minuterie de destruction de la machine (A13, VL-02) — essai Lean, v1.

Brouillon 3, § 3.8 A13 : fournisseur et prix horaire consignés avant la location ; cumul « heures allumées × prix » ;
destruction **par identifiant** (R10) au plus tard à l'échéance du pas (48 heures pour D-1a, 26 pour D-1b, 70 pour la phase 2)
et plus tôt dès que le cumul atteint le plafond moins une heure. Les heures sont comptées **entamées** (facturation horaire).

La minuterie tourne hors de la machine (elle porte le jeton de l'API) ; si elle s'arrête, l'identifiant et l'échéance sont dans
son journal et le rapport, pour une destruction à la main par identifiant.
"""
from __future__ import annotations

import argparse
import json
import math
import sys
import time
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone

from controle_ia.gardes import GardeArret

ECHEANCES_H = {"D-1a": 48.0, "D-1b": 26.0, "phase-2": 70.0}
PLAFONDS_MACHINE = {"D-1a": 65.0, "D-1b": 35.0, "phase-2": 91.0}


@dataclass(frozen=True)
class Machine:
    identifiant: int
    nom: str
    cree_a: datetime
    prix_horaire_usd: float
    plafond_usd: float
    echeance_h: float

    def __post_init__(self):
        if self.cree_a.tzinfo is None:
            raise GardeArret("heure de création sans fuseau : UTC exigé")
        if self.prix_horaire_usd <= 0 or self.plafond_usd <= 0 or self.echeance_h <= 0:
            raise GardeArret("prix horaire, plafond et échéance doivent être positifs")


def verifier_devis(prix_horaire_usd: float, pas: str) -> None:
    """Avant la location : le type choisi tient le plafond du pas même allumé jusqu'à l'échéance."""
    if pas not in ECHEANCES_H:
        raise GardeArret(f"pas inconnu {pas!r}")
    if prix_horaire_usd * ECHEANCES_H[pas] > PLAFONDS_MACHINE[pas]:
        raise GardeArret(f"{prix_horaire_usd} USD/h × {ECHEANCES_H[pas]} h > plafond machine {PLAFONDS_MACHINE[pas]} USD")


def heures_entamees(m: Machine, maintenant: datetime) -> int:
    secondes = (maintenant - m.cree_a).total_seconds()
    return max(1, math.ceil(secondes / 3600.0))


def cout_cumule(m: Machine, maintenant: datetime) -> float:
    return heures_entamees(m, maintenant) * m.prix_horaire_usd


def decider(m: Machine, maintenant: datetime) -> tuple[bool, str]:
    if maintenant >= m.cree_a + timedelta(hours=m.echeance_h):
        return True, f"échéance de {m.echeance_h} h atteinte"
    cumul = cout_cumule(m, maintenant)
    if cumul >= m.plafond_usd - m.prix_horaire_usd:
        return True, f"cumul {cumul:.2f} USD ≥ plafond {m.plafond_usd:.2f} − une heure"
    return False, f"garder (cumul {cumul:.2f} USD)"


def veiller(m: Machine, client, horloge=lambda: datetime.now(timezone.utc), dormir=time.sleep, pas_s: float = 60.0,
            journal=None, tours_max: int | None = None) -> dict:
    """Boucle de la minuterie : à chaque pas, décision ; à la destruction, suppression par identifiant, puis attente de
    l'absence. Toute erreur de l'API remonte (aucun repli silencieux)."""
    tours = 0
    while True:
        maintenant = horloge()
        detruire, motif = decider(m, maintenant)
        if journal is not None:
            journal.write(json.dumps({"heure": maintenant.isoformat(), "detruire": detruire, "motif": motif}) + "\n")
            journal.flush()
        if detruire:
            etat = client.supprimer_serveur(m.identifiant, m.nom)
            absent = client.attendre_absence(m.identifiant)
            if not absent:
                raise GardeArret(f"serveur {m.identifiant} encore présent après la demande de suppression")
            return {"detruit": True, "motif": motif, "etat": etat, "heure": horloge().isoformat(),
                    "cout_cumule_usd": cout_cumule(m, maintenant)}
        tours += 1
        if tours_max is not None and tours >= tours_max:
            return {"detruit": False, "motif": motif}
        dormir(pas_s)


def main(argv=None) -> int:
    from .hetzner_v1 import ClientHetzner
    ap = argparse.ArgumentParser(description="Minuterie de destruction par identifiant (A13)")
    ap.add_argument("--identifiant", type=int, required=True)
    ap.add_argument("--nom", required=True)
    ap.add_argument("--cree-a", required=True, help="ISO 8601 avec fuseau")
    ap.add_argument("--prix-horaire-usd", type=float, required=True)
    ap.add_argument("--pas", choices=sorted(ECHEANCES_H), default="D-1a")
    ap.add_argument("--echeance-h", type=float, help="plus courte que celle du pas, jamais plus longue")
    ap.add_argument("--journal", required=True)
    a = ap.parse_args(argv)
    echeance = ECHEANCES_H[a.pas] if a.echeance_h is None else a.echeance_h
    if echeance > ECHEANCES_H[a.pas]:
        raise GardeArret("échéance plus longue que celle du pas")
    verifier_devis(a.prix_horaire_usd, a.pas)
    m = Machine(a.identifiant, a.nom, datetime.fromisoformat(a.cree_a), a.prix_horaire_usd, PLAFONDS_MACHINE[a.pas],
                echeance)
    with open(a.journal, "a", encoding="utf-8") as j:
        res = veiller(m, ClientHetzner(), journal=j)
        j.write(json.dumps(res) + "\n")
    print(json.dumps(res))
    return 0


if __name__ == "__main__":
    sys.exit(main())
