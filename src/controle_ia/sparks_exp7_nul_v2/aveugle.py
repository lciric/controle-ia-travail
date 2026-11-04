"""Aveuglement pour l'addendum n° 1 : celui de la v1 (tirage secret, coffre, copies servies, contrôle de fuite),
plus le fichier des scores de B3 et B4 du bras principal, **au coffre seul** (« Bases et plafond », « Quand ») :

- `ajouter_bases_coffre` : ajout seul, par nom servi (`cas_<hex>` → {"A": {"d", "n"}, "B": {"d", "n"}}), dans
  `coffre/bases-poids-principal-v1.json` (droits 600) ; refus si le dossier n'est pas un coffre (clé absente, droits
  autres que 700) ou s'il est mêlé au dossier servi, au dépôt ou au bac ; refus d'une seconde valeur différente pour
  un même nom ; rien n'est imprimé ni journalisé, sauf le nom du cas dans le journal du coffre ;
- `engager_bases` : empreinte du fichier, pour le manifeste, après le dernier cas servi ;
- `ouvrir_coffre` : ouverture unique de la v1, qui exige en plus l'empreinte engagée du fichier des bases et en écrit
  une copie scellée à côté de la copie de la clé (`bases-poids-principal-ouvert-v1.json`).
"""
from __future__ import annotations

import json
import os
import stat
from datetime import datetime, timezone
from pathlib import Path

from ..sparks_exp7_nul_v1.aveugle import (CHAINES_INTERDITES, DATE_NORMALISEE, FICHIERS_SERVIS,  # noqa: F401
                                          FICHIERS_TOKENISEUR, NOM_CAS, GardeCoffre, GardeFuite, controle_fuite,
                                          ecrire_coffre, ecrire_safetensors, engagement, entete_safetensors,
                                          normaliser_dates, ordre_lecteur, servir_cas, sha256_fichier, tirer_attribution,
                                          tirer_secret, verifier_emplacement_coffre)
from ..sparks_exp7_nul_v1.aveugle import ouvrir_coffre as ouvrir_coffre_v1

FICHIER_BASES = "bases-poids-principal-v1.json"
COPIE_BASES = "bases-poids-principal-ouvert-v1.json"


def exiger_coffre(coffre: Path, interdits: list[Path]) -> Path:
    c = Path(coffre)
    if not (c / "cle-v1.json").is_file():
        raise GardeCoffre(f"{c} n'est pas un coffre (clé absente) : scores de base refusés hors du coffre")
    if stat.S_IMODE(c.stat().st_mode) != 0o700:
        raise GardeCoffre(f"{c} : droits {oct(stat.S_IMODE(c.stat().st_mode))}, 0o700 attendus")
    verifier_emplacement_coffre(c, interdits)
    return c


def ajouter_bases_coffre(coffre: Path, nom: str, scores: dict, *, interdits: list[Path]) -> None:
    c = exiger_coffre(coffre, interdits)
    if not NOM_CAS.match(nom):
        raise GardeCoffre(f"nom de cas {nom!r}")
    if set(scores) != {"A", "B"} or any(set(v) != {"d", "n"} for v in scores.values()):
        raise GardeCoffre("scores attendus : {A: {d, n}, B: {d, n}}")
    f = c / FICHIER_BASES
    tout = json.loads(f.read_text(encoding="utf-8")) if f.exists() else {}
    if nom in tout:
        if tout[nom] != scores:
            raise GardeCoffre(f"{nom} : scores différents de la première mise à disposition (ajout seul)")
        return
    tout[nom] = scores
    tmp = c / (FICHIER_BASES + ".tmp")
    tmp.write_text(json.dumps(tout, indent=1, sort_keys=True), encoding="utf-8")
    os.chmod(tmp, 0o600)
    tmp.replace(f)
    with open(c / "journal-v1.txt", "a", encoding="utf-8") as j:
        j.write(f"{datetime.now(timezone.utc).isoformat(timespec='seconds')} bases B3 et B4 de {nom} écrites "
                "(scores non journalisés)\n")


def engager_bases(coffre: Path, attendus: int) -> str:
    f = Path(coffre) / FICHIER_BASES
    n = len(json.loads(f.read_text(encoding="utf-8"))) if f.exists() else 0
    if n != attendus:
        raise GardeCoffre(f"{n} cas aux bases du coffre, {attendus} attendus")
    return sha256_fichier(f)


def ouvrir_coffre(coffre: Path, sortie: Path, *, sha256_cle: str, sha256_bases: str, reponses_scellees: list[Path],
                  sha256_script_analyse: str, attendues: int) -> dict:
    from ..scellement import sceller

    f = Path(coffre) / FICHIER_BASES
    if not f.is_file() or sha256_fichier(f) != sha256_bases:
        raise GardeCoffre("bases du coffre absentes ou altérées (empreinte ≠ manifeste)")
    copie = Path(sortie) / COPIE_BASES
    if copie.exists():
        raise GardeCoffre(f"{copie} existe déjà (R12)")
    corps = ouvrir_coffre_v1(coffre, sortie, sha256_cle=sha256_cle, reponses_scellees=reponses_scellees,
                             sha256_script_analyse=sha256_script_analyse, attendues=attendues)
    copie.write_bytes(f.read_bytes())
    sceller(copie)
    return {**corps, "bases_poids": json.loads(f.read_text(encoding="utf-8"))}
