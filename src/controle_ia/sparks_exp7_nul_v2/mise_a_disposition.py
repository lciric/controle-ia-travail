"""Mise à disposition pour l'addendum n° 1 : celle de la v1 (secret, clé au coffre, ordres, service cas par cas,
contrôle de fuite), plus :

- **B3 et B4 sur chaque cas servi, avant qu'il ne soit lu** (`bases_poids_cas`) : la fonction ne reçoit que le
  dossier servi du cas et les couches du départ ; elle **ne lit pas la clé**, n'imprime ni ne journalise aucun score ;
  les scores vont au coffre seul (`aveugle.ajouter_bases_coffre`) ;
- **couches du départ** reçues de l'instance avec le premier lot (`recevoir_couches_depart`) : empreinte contrôlée
  contre le manifeste ; rangées hors de tout dossier servi, de toute session de lecteur et du dépôt (jamais montées
  dans le bac) ;
- **service par lots** de 4 cas, 3 si moins de 10 Go sont libres (`taille_lot`, `lots`).

    python -m controle_ia.sparks_exp7_nul_v2.mise_a_disposition servir --nom cas_<hex> --modeles M --depart D \
        --servi S --coffre C --engagement E.json --depart-couches F --sha-depart H [--sessions SS]
    python -m controle_ia.sparks_exp7_nul_v2.mise_a_disposition lots --libres OCTETS --noms cas_a,cas_b,…
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

from ..sparks_exp7_nul_v1.mise_a_disposition import (cas_a_servir, config_servie, lire_cle_preparation,  # noqa: F401
                                                     mettre_a_disposition, servir_un)
from . import aveugle, bases

LOT, LOT_REDUIT, SEUIL_LIBRE = 4, 3, 10 * 10 ** 9


def taille_lot(octets_libres: int) -> int:
    if octets_libres < 0:
        raise ValueError("place libre négative")
    return LOT if octets_libres >= SEUIL_LIBRE else LOT_REDUIT


def lots(noms: list[str], taille: int) -> list[list[str]]:
    if taille not in (LOT, LOT_REDUIT):
        raise ValueError(f"taille de lot {taille} : 4 ou 3")
    return [noms[i:i + taille] for i in range(0, len(noms), taille)]


def recevoir_couches_depart(fichier: Path, sha_attendu: str, *, interdits: list[Path]) -> dict:
    """Couches du départ (bf16) : empreinte = manifeste, emplacement hors du servi, des sessions et du dépôt."""
    f = Path(fichier)
    aveugle.verifier_emplacement_coffre(f.parent, interdits)
    if aveugle.sha256_fichier(f) != sha_attendu:
        raise aveugle.GardeFuite("couches du départ : empreinte ≠ manifeste")
    return bases.lire_safetensors(f)


def bases_poids_cas(dossier_cas: Path, etat_depart: dict, coffre: Path, n_couches: int, *, interdits: list[Path],
                    suffixes=bases.SUFFIXES_GEMMA) -> None:
    """B3 et B4 des deux copies servies d'un cas, au coffre seul ; rien n'est rendu ni imprimé."""
    d = Path(dossier_cas)
    if not aveugle.NOM_CAS.match(d.name):
        raise aveugle.GardeFuite(f"nom de cas {d.name!r}")
    sc = {X: bases.scores_poids(bases.lire_safetensors(d / X / "model.safetensors"), etat_depart, n_couches,
                                suffixes=suffixes) for X in ("A", "B")}
    aveugle.ajouter_bases_coffre(coffre, d.name, sc, interdits=interdits + [d.parent])


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(prog="mise_a_disposition_v2")
    sp = ap.add_subparsers(dest="cmd", required=True)
    u = sp.add_parser("servir", help="sert un cas, contrôle de fuite, puis B3 et B4 au coffre")
    for k in ("nom", "modeles", "depart", "servi", "coffre", "engagement", "depart-couches", "sha-depart"):
        u.add_argument(f"--{k}", required=True)
    u.add_argument("--sessions", default=None)
    u.add_argument("--depot", default=str(Path(__file__).resolve().parents[3]))
    u.add_argument("--suffixes-du-depart", action="store_true", help="secours : tenseurs de couche relevés sur le départ")
    lo = sp.add_parser("lots")
    lo.add_argument("--libres", type=int, required=True)
    lo.add_argument("--noms", required=True)
    a = ap.parse_args(argv)
    if a.cmd == "servir":
        import torch
        from transformers import AutoModelForCausalLM

        if not aveugle.NOM_CAS.match(a.nom):
            raise SystemExit("nom de cas invalide")
        interdits = [Path(a.servi), Path(a.depot)] + ([Path(a.sessions)] if a.sessions else [])
        dep = recevoir_couches_depart(Path(a.depart_couches), a.sha_depart, interdits=interdits)
        eng = json.loads(Path(a.engagement).read_text(encoding="utf-8"))
        cle = lire_cle_preparation(Path(a.coffre), eng["sha256_cle"])
        depart = AutoModelForCausalLM.from_pretrained(a.depart, dtype=torch.float32)
        servir_un(a.nom, cle[a.nom], Path(a.modeles), depart, Path(a.depart), Path(a.servi), Path(a.coffre))
        del cle
        bases_poids_cas(Path(a.servi) / a.nom, dep, Path(a.coffre), depart.config.num_hidden_layers,
                        interdits=interdits, suffixes=None if a.suffixes_du_depart else bases.SUFFIXES_GEMMA)
        print(f"SERVI {a.nom} : contrôle de fuite passé ; B3 et B4 au coffre")
    else:
        noms = [x for x in a.noms.split(",") if x]
        for i, l in enumerate(lots(noms, taille_lot(a.libres)), 1):
            print(f"LOT {i} : {' '.join(l)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
