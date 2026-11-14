"""Garde de dépense d'une location pour « Neuron Lens » (volet A, puis tranche B-α) — v1.

Côté commande (le conteneur de la session), jamais sur la machine louée (aucune clé du loueur n'y va). Liste d'arrêt du texte gelé v6 :
« dépense à 60 % du plafond de la ligne ou de la tranche → compte rendu à la mère ; à 90 %, arrêt dur » ; « minuterie de destruction
par identifiant non posée à la création → destruction par identifiant avant toute passe (R10) ».

Dépense estimée = prix horaire **lu sur l'instance** (`dph_total` de `vastai show instance <id> --raw`, stockage compris) × durée
depuis la création, plus les frais fixes déclarés ; si le prix lu manque ou n'est pas fini, le prix déclaré à la location sert, et
le plus grand des deux est toujours pris. Arrêt dur = destruction **par identifiant** (`vastai destroy instance <id>`), jamais par
motif. La minuterie est la durée au bout de laquelle la dépense atteint 90 % du plafond au prix déclaré ; elle est posée à la
création, avant toute passe.
"""
from __future__ import annotations

import argparse
import json
import math
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

SEUIL_COMPTE_RENDU = 0.60
SEUIL_ARRET = 0.90


def etat(depense: float, plafond: float) -> str:
    if not (math.isfinite(depense) and math.isfinite(plafond) and plafond > 0 and depense >= 0):
        return "arret"  # valeur illisible : arrêt (aucun repli)
    if depense >= SEUIL_ARRET * plafond:
        return "arret"
    if depense >= SEUIL_COMPTE_RENDU * plafond:
        return "compte_rendu"
    return "ok"


def depense(prix_h: float, debut: float, maintenant: float, frais_fixes: float = 0.0) -> float:
    return max(0.0, maintenant - debut) / 3600.0 * prix_h + frais_fixes


def minuterie_s(prix_h: float, plafond: float, frais_fixes: float = 0.0) -> int:
    if not (prix_h > 0 and plafond > frais_fixes):
        raise ValueError("prix ou plafond illisible")
    return int((SEUIL_ARRET * plafond - frais_fixes) / prix_h * 3600)


def surveiller(id_instance: int, prix_declare: float, plafond: float, debut: float, *, lire_prix, detruire, rapporter,
               horloge=time.time, dormir=time.sleep, periode: float = 60.0, frais_fixes: float = 0.0, tours_max=None) -> dict:
    """Boucle de garde. `lire_prix(id)` : prix horaire lu (ou None si l'instance n'existe plus) ; `detruire(id)` ; `rapporter(dict)`.
    Rend le dernier état. Le compte rendu à 60 % n'est envoyé qu'une fois."""
    rapporte, tours = False, 0
    while True:
        lu = lire_prix(id_instance)
        if lu is None:
            return {"etat": "instance_absente", "depense": depense(prix_declare, debut, horloge(), frais_fixes)}
        prix = max(prix_declare, lu) if (isinstance(lu, (int, float)) and math.isfinite(lu)) else prix_declare
        dep = depense(prix, debut, horloge(), frais_fixes)
        e = etat(dep, plafond)
        if e == "arret":
            detruire(id_instance)
            r = {"etat": "arret", "depense": dep, "prix_h": prix, "id": id_instance}
            rapporter(r)
            return r
        if e == "compte_rendu" and not rapporte:
            rapporter({"etat": "compte_rendu", "depense": dep, "prix_h": prix, "id": id_instance})
            rapporte = True
        tours += 1
        if tours_max is not None and tours >= tours_max:
            return {"etat": e, "depense": dep}
        dormir(periode)


# ---------------------------------------------------------------- loueur (Vast.ai), par identifiant seulement
def _vast_prix(id_instance: int):
    p = subprocess.run(["vastai", "show", "instance", str(int(id_instance)), "--raw"], capture_output=True, text=True, timeout=120)
    if p.returncode != 0:
        if "not found" in (p.stdout + p.stderr).lower():
            return None
        return float("nan")  # illisible : le prix déclaré sert
    try:
        d = json.loads(p.stdout)
    except json.JSONDecodeError:
        return float("nan")
    if not d:
        return None
    return float(d.get("dph_total", float("nan")))


def _vast_detruire(id_instance: int):
    subprocess.run(["vastai", "destroy", "instance", str(int(id_instance))], check=True, timeout=120)


def main(argv=None):
    p = argparse.ArgumentParser(description="Garde de dépense par identifiant d'instance")
    p.add_argument("--instance", type=int, required=True)
    p.add_argument("--prix-h", type=float, required=True)
    p.add_argument("--plafond", type=float, required=True)
    p.add_argument("--debut", required=True, help="date de création ISO 8601 (UTC)")
    p.add_argument("--journal", type=Path, required=True)
    p.add_argument("--frais-fixes", type=float, default=0.0)
    a = p.parse_args(argv)
    debut = datetime.fromisoformat(a.debut).astimezone(timezone.utc).timestamp()

    def rapporter(r):
        r = r | {"heure": datetime.now(timezone.utc).isoformat(timespec="seconds")}
        with open(a.journal, "a", encoding="utf-8") as f:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
        print(json.dumps(r, ensure_ascii=False), flush=True)

    r = surveiller(a.instance, a.prix_h, a.plafond, debut, lire_prix=_vast_prix, detruire=_vast_detruire, rapporter=rapporter,
                   frais_fixes=a.frais_fixes)
    rapporter(r)
    sys.exit(0 if r["etat"] != "arret" else 3)


if __name__ == "__main__":
    main()
