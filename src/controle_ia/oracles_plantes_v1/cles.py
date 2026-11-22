"""Définition servie et clé d'un monde : deux fichiers distincts ; la clé est scellée (compagnon `.sha256`, R6).

- La définition servie est ce qu'un proposeur verra : paramètres, vocabulaire, domaines, axiomes, borne N.
- La clé : étiquette de chaque énoncé planté, instance certifiant chaque faux tôt et chaque piège.
- Avant toute écriture, aucun fragment de la clé (texte d'un énoncé planté, étiquette, instance) ne doit apparaître
  dans les octets de la définition servie (préfigure A8) ; sinon `GardeArret`.
- Au chargement, la clé est vérifiée contre son empreinte compagnon : un octet altéré est refusé.
"""
from __future__ import annotations

import json
from pathlib import Path

from ..gardes import GardeArret
from ..scellement import sceller, verifier
from . import VERSION
from .banque import ETIQUETTES


def octets_json(obj) -> bytes:
    return (json.dumps(obj, ensure_ascii=False, sort_keys=True, indent=1) + "\n").encode("utf-8")


def fragments_de_cle(cle: dict) -> list[str]:
    fr = list(ETIQUETTES.values())
    for p in cle["plantes"]:
        fr.append(p["texte"])
        if p.get("instance"):  # une instance vide (énoncé clos) ne porte aucune information
            fr.append(json.dumps(p["instance"], ensure_ascii=False, sort_keys=True))
    return fr


def verifier_absence_fuite(octets_servis: bytes, fragments: list[str], quoi: str = "définition servie"):
    for f in fragments:
        if f and f.encode("utf-8") in octets_servis:
            raise GardeArret(f"fuite : un fragment de la clé apparaît dans la {quoi} ({f[:40]!r}…)")


def cle_du_monde(monde, identifiant: str, plantes: list) -> dict:
    internes = {k: (str(v) if not isinstance(v, (int, list, dict)) else v)
                for k, v in monde.p.items() if k != "cfg"}
    return {"version": VERSION, "identifiant_monde": identifiant, "famille": monde.famille, "borne_N": monde.N,
            "indice_monde": monde.indice, "parametres_internes": internes,
            "plantes": [p.en_dict() for p in plantes]}


def ecrire_monde(dossier: str | Path, monde, identifiant: str, plantes: list, statut_parametres: str):
    dossier = Path(dossier)
    dossier.mkdir(parents=True, exist_ok=False)
    definition = monde.definition_servie(identifiant)
    definition["version"] = VERSION
    definition["statut_parametres"] = statut_parametres
    cle = cle_du_monde(monde, identifiant, plantes)
    o_def, o_cle = octets_json(definition), octets_json(cle)
    verifier_absence_fuite(o_def, fragments_de_cle(cle))
    ch_def, ch_cle = dossier / "definition-servie-v1.json", dossier / "cle-v1.json"
    for ch, o in ((ch_def, o_def), (ch_cle, o_cle)):
        if ch.exists():
            raise GardeArret(f"{ch} existe déjà : R12 interdit d'écraser")
        ch.write_bytes(o)
        sceller(ch)
    return ch_def, ch_cle


def charger_cle(chemin: str | Path) -> dict:
    """Vérifie l'empreinte compagnon, puis lit la clé ; lève `GardeArret` si un octet a changé."""
    verifier(chemin)
    cle = json.loads(Path(chemin).read_text(encoding="utf-8"))
    if cle.get("version") != VERSION:
        raise GardeArret(f"{chemin} : version {cle.get('version')!r} ≠ {VERSION}")
    return cle


def charger_definition(chemin: str | Path) -> dict:
    verifier(chemin)
    return json.loads(Path(chemin).read_text(encoding="utf-8"))
