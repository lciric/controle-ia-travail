"""Copie déclarée du code publié de Ferreira da Silva et Heimersheim (arXiv 2606.24964).

Dépôt amont : https://github.com/FranciscoHS/fsec-paper, commit a9355d4001500708a40a255bacfe559e6dc269c0 (branche
`main`, relevé le 2026-11-03). Licence MIT (`LICENSE-fsec-paper`, copie à l'identique, exigée par la licence).

Fichiers copiés à l'identique, sans aucune modification (empreintes dans `PROVENANCE.json`, vérifiées par les essais) :
- `parametrize.py` (amont `scripts/lib/parametrize.py`) : projection tangente, Gram-Schmidt, carte exponentielle ;
- `superellipse.py` (amont `scripts/lib/superellipse.py`) : contour d'iso-réponse, intercepts d'axe, ajustement de p.

Tout le reste du pilote est écrit ici ; il appelle ces deux fichiers sans les changer.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

DOSSIER = Path(__file__).resolve().parent
PROVENANCE = DOSSIER / "PROVENANCE.json"


def verifier_copie() -> dict:
    """Recalcule l'empreinte de chaque fichier copié et la compare à `PROVENANCE.json`. Lève sur tout écart."""
    from ...gardes import GardeArret

    prov = json.loads(PROVENANCE.read_text(encoding="utf-8"))
    for nom, info in prov["fichiers"].items():
        h = hashlib.sha256((DOSSIER / nom).read_bytes()).hexdigest()
        if h != info["sha256"]:
            raise GardeArret(f"copie amont altérée : {nom} {h[:12]}… ≠ {info['sha256'][:12]}…")
    return prov
