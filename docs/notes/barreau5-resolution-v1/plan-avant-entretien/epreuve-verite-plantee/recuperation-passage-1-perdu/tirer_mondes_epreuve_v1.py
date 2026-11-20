"""Tireur de l'épreuve à vérité plantée (barreau 5), rôle 1 — v1.

Mandat `mandats-epreuve-verite-plantee-v1.md` (`2dce334d…`), section « Rôle 1 ». Tire une entropie neuve de 128 bits
(`secrets.randbits(128)`), qui n'est écrite que dans le fichier des vérités et n'est jamais affichée ; écrit les vérités
(`ecrire_verites`), puis tous les mondes (`fabriquer`, pour chaque identifiant de `liste_mondes`), sous les paramètres de
l'essai de raccord (seul `empreinte_lecture` réglé, à l'empreinte du programme gelé) ; écrit l'inventaire des mondes (chemins
relatifs triés, chacun avec son sha256). N'affiche que : empreinte des vérités, empreinte de l'inventaire, nombre de mondes.
Aucune donnée lue. Rien n'est supprimé.

Usage : `PYTHONPATH=src .venv/bin/python -B <ce fichier> --racine /dev/shm/b5f-epreuve-v1`.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import secrets
import shutil
import sys
from pathlib import Path

from controle_ia.barreau5_familles import epreuve_verite_plantee_v1 as fab

LECTURE_SHA256 = "ed0999df49aedb52099bb848803c3049a8ba09db2a46ce3df9230d3e7b25626f"
BORNE_OCTETS = 12 * 1024 ** 3


def sha_fichier(p: Path) -> str:
    h = hashlib.sha256()
    with open(p, "rb") as fh:
        for bloc in iter(lambda: fh.read(1 << 20), b""):
            h.update(bloc)
    return h.hexdigest()


def taille(d: Path) -> int:
    return sum(f.stat().st_size for f in d.rglob("*") if f.is_file())


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--racine", required=True)
    a = ap.parse_args()
    racine = Path(a.racine)
    racine.mkdir(parents=False, exist_ok=False)
    mondes_d = racine / "mondes"
    verites_d = racine / "verites"
    mondes_d.mkdir()
    verites_d.mkdir()

    params_f = racine / "parametres-epreuve-v1.json"
    with open(params_f, "x", encoding="utf-8") as fh:
        fh.write(json.dumps({"empreinte_lecture": LECTURE_SHA256}))
    params = fab.Parametres.depuis_fichier(params_f)

    entropie = 0
    while entropie == 0:
        entropie = secrets.randbits(128)

    verites_f = verites_d / "verites-epreuve-v1.json"
    sha_rendu = fab.ecrire_verites(entropie, verites_f, params)
    sha_disque = sha_fichier(verites_f)
    if sha_rendu != sha_disque or verites_f.stat().st_size == 0:
        print("vérités : empreinte rendue différente de celle du disque, ou fichier vide : arrêt", file=sys.stderr)
        return 3

    liste = fab.liste_mondes()
    for k, m in enumerate(liste):
        fab.fabriquer(entropie, m, mondes_d / m, params)
        if k == 0:
            projete = taille(mondes_d) * len(liste)
            if projete > BORNE_OCTETS or projete > shutil.disk_usage(racine).free:
                print(f"taille projetée {projete} octets : arrêt", file=sys.stderr)
                return 5
    del entropie

    lignes = []
    for f in sorted(p for p in mondes_d.rglob("*") if p.is_file()):
        lignes.append(f"{sha_fichier(f)}  {f.relative_to(mondes_d).as_posix()}")
    lignes.sort(key=lambda x: x.split("  ", 1)[1])
    inv_f = racine / "inventaire-mondes-v1.txt"
    with open(inv_f, "x", encoding="utf-8") as fh:
        fh.write("\n".join(lignes) + "\n")

    n_dossiers = sum(1 for p in mondes_d.iterdir() if p.is_dir())
    print(json.dumps({"verites_sha256": sha_disque, "inventaire_sha256": sha_fichier(inv_f),
                      "mondes": len(liste), "dossiers_de_mondes": n_dossiers, "fichiers_inventories": len(lignes)},
                     ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
