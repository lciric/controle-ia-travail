"""Lots scellés et reprise après coupure ; graines dérivées (R9, R11, R12) — exploratoire.

Un lot s'écrit d'abord sous `<nom>.partiel`, puis il est renommé et scellé (compagnon `.sha256`). À la reprise :
- lot final scellé et intact : sauté ;
- lot absent : écrit ;
- lot final sans compagnon, ou compagnon qui ne correspond pas : arrêt (`GardeArret`), jamais deviné ni réécrit ;
- reste `.partiel` d'une coupure : renommé `.partiel.abandon-<n>` et gardé (rien n'est supprimé), puis le lot est réécrit.
"""
from __future__ import annotations

import json
import os
from pathlib import Path

import numpy as np

from ..gardes import GardeArret
from ..manifeste import cle_de_tache
from ..scellement import compagnon, sceller, verifier


def etat_lot(final: Path) -> str:
    """« scelle » (vérifié) ou « absent » ; lève sur un lot final non scellé ou altéré."""
    final = Path(final)
    if final.exists():
        if not compagnon(final).exists():
            raise GardeArret(f"{final} présent sans empreinte compagnon : coupure entre renommage et scellement, ou "
                             "écriture étrangère ; vérifier à la main (R11), rien n'est réécrit")
        verifier(final)
        return "scelle"
    return "absent"


def _mettre_de_cote(partiel: Path) -> Path | None:
    if not partiel.exists():
        return None
    n = 1
    while Path(f"{partiel}.abandon-{n}").exists():
        n += 1
    cible = Path(f"{partiel}.abandon-{n}")
    partiel.rename(cible)
    return cible


def ecrire_lot(final: Path, ecrire) -> str:
    """`ecrire(chemin_partiel)` écrit le contenu ; renommage atomique puis scellement. Rend l'empreinte."""
    final = Path(final)
    if etat_lot(final) == "scelle":
        raise GardeArret(f"{final} déjà scellé : R12 interdit de le réécrire")
    final.parent.mkdir(parents=True, exist_ok=True)
    partiel = Path(str(final) + ".partiel")
    _mettre_de_cote(partiel)
    ecrire(partiel)
    with open(partiel, "rb") as f:
        os.fsync(f.fileno())
    partiel.rename(final)
    return sceller(final)


def ecrire_jsonl(final: Path, lignes: list[dict]) -> str:
    def _e(p: Path):
        with open(p, "w", encoding="utf-8") as f:
            for x in lignes:
                f.write(json.dumps(x, ensure_ascii=False, sort_keys=True) + "\n")
    return ecrire_lot(final, _e)


def lire_jsonl(final: Path) -> list[dict]:
    verifier(final)
    return [json.loads(l) for l in Path(final).read_text(encoding="utf-8").splitlines() if l.strip()]


def nom_lot(i: int) -> str:
    return f"lot-{int(i):05d}"


def lots(elements: list, taille: int) -> list[list]:
    if isinstance(taille, bool) or not isinstance(taille, int) or taille < 1:
        raise GardeArret(f"taille de lot {taille!r} : entier positif attendu")
    return [elements[i:i + taille] for i in range(0, len(elements), taille)]


def graine_derivee(graine: dict, nom: str) -> int:
    """Entier de 32 bits dérivé d'une graine du manifeste (`manifeste.graines`) et d'un nom (question, pli, couche)."""
    cles = tuple(int(k) for k in graine["spawn_key"]) + (cle_de_tache(nom),)
    ss = np.random.SeedSequence(int(graine["entropie"]), spawn_key=cles)
    return int(ss.generate_state(1, dtype=np.uint32)[0])
