"""Garde de dépense d'une location pour « Neuron Lens » (volet A, puis tranche B-α) — v4 (v3 + destruction confirmée : l'outil du
loueur 1.11.0 demande une confirmation [y/N], abandonne sans entrée et rend le code 0 — constaté le 14 novembre 2026 sur l'instance
60669495, journal de la course du volet A ; `-y` passé, entrée fermée, sortie capturée et jamais imprimée ; une sortie vide de la
lecture du prix vaut un prix illisible, jamais une absence ; la destruction reste vérifiée par l'absence, réessayée). v3 : v2 + lecture du prix
protégée : une exception de la lecture vaut un prix illisible, le prix déclaré sert ; contre-lecture 4, remarque 5). La v2 remplaçait la v1 après la
contre-lecture 3, remarques 3 et 4 : destruction réessayée et vérifiée ; option « minuterie seulement », durée restante comptée depuis
la création).

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


def minuterie_restante_s(prix_h: float, plafond: float, debut: float, maintenant: float, frais_fixes: float = 0.0) -> int:
    """Durée restante de la minuterie, comptée depuis la création de l'instance (jamais négative)."""
    return max(0, minuterie_s(prix_h, plafond, frais_fixes) - int(max(0.0, maintenant - debut)))


def detruire_verifie(id_instance: int, detruire, lire_prix, essais: int = 5, dormir=time.sleep, pause: float = 20.0) -> bool:
    """Destruction par identifiant, réessayée jusqu'à `essais` fois, vérifiée par la lecture de l'instance (absente = détruite)."""
    for _ in range(essais):
        try:
            detruire(id_instance)
        except Exception:  # noqa: BLE001 — l'échec est retenté puis rendu, jamais tu
            pass
        try:
            absente = lire_prix(id_instance) is None
        except Exception:  # noqa: BLE001
            absente = False
        if absente:
            return True
        dormir(pause)
    return False


def surveiller(id_instance: int, prix_declare: float, plafond: float, debut: float, *, lire_prix, detruire, rapporter,
               horloge=time.time, dormir=time.sleep, periode: float = 60.0, frais_fixes: float = 0.0, tours_max=None) -> dict:
    """Boucle de garde. `lire_prix(id)` : prix horaire lu (ou None si l'instance n'existe plus) ; `detruire(id)` ; `rapporter(dict)`.
    Rend le dernier état. Le compte rendu à 60 % n'est envoyé qu'une fois."""
    rapporte, tours = False, 0
    while True:
        try:
            lu = lire_prix(id_instance)
        except Exception:  # noqa: BLE001 — délai dépassé, sortie illisible : prix déclaré, la boucle continue
            lu = float("nan")
        if lu is None:
            return {"etat": "instance_absente", "depense": depense(prix_declare, debut, horloge(), frais_fixes)}
        prix = max(prix_declare, lu) if (isinstance(lu, (int, float)) and math.isfinite(lu)) else prix_declare
        dep = depense(prix, debut, horloge(), frais_fixes)
        e = etat(dep, plafond)
        if e == "arret":
            ok = detruire_verifie(id_instance, detruire, lire_prix, dormir=dormir)
            r = {"etat": "arret" if ok else "arret_echec_destruction", "depense": dep, "prix_h": prix, "id": id_instance}
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
    if not p.stdout.strip():
        return float("nan")  # v4 : sortie vide = illisible, jamais une absence
    try:
        d = json.loads(p.stdout)
    except json.JSONDecodeError:
        return float("nan")
    if not d:
        return None
    return float(d.get("dph_total", float("nan")))


def _vast_detruire(id_instance: int):
    # v4 : `-y` (sans lui, l'outil 1.11.0 abandonne en silence, code 0) ; entrée fermée ; sortie capturée, jamais imprimée
    subprocess.run(["vastai", "destroy", "instance", str(int(id_instance)), "-y"], check=True, timeout=120,
                   stdin=subprocess.DEVNULL, capture_output=True, text=True)


def main(argv=None):
    p = argparse.ArgumentParser(description="Garde de dépense par identifiant d'instance")
    p.add_argument("--minuterie-seulement", action="store_true",
                   help="imprime la durée restante de la minuterie (secondes) depuis --debut et sort")
    p.add_argument("--instance", type=int)
    p.add_argument("--prix-h", type=float, required=True)
    p.add_argument("--plafond", type=float, required=True)
    p.add_argument("--debut", required=True, help="date de création ISO 8601 (UTC)")
    p.add_argument("--journal", type=Path)
    p.add_argument("--frais-fixes", type=float, default=0.0)
    a = p.parse_args(argv)
    debut = datetime.fromisoformat(a.debut).astimezone(timezone.utc).timestamp()
    if a.minuterie_seulement:
        print(minuterie_restante_s(a.prix_h, a.plafond, debut, time.time(), a.frais_fixes))
        return
    if a.instance is None or a.journal is None:
        p.error("--instance et --journal exigés pour la surveillance")

    def rapporter(r):
        r = r | {"heure": datetime.now(timezone.utc).isoformat(timespec="seconds")}
        with open(a.journal, "a", encoding="utf-8") as f:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
        print(json.dumps(r, ensure_ascii=False), flush=True)

    r = surveiller(a.instance, a.prix_h, a.plafond, debut, lire_prix=_vast_prix, detruire=_vast_detruire, rapporter=rapporter,
                   frais_fixes=a.frais_fixes)
    if not r["etat"].startswith("arret"):  # l'arrêt est déjà rapporté par `surveiller`
        rapporter(r)
    sys.exit({"arret": 3, "arret_echec_destruction": 4}.get(r["etat"], 0))


if __name__ == "__main__":
    main()
