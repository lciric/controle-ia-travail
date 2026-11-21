"""Véhicule NA-1, lot 2 v3 — extraction des plages « Default_Ignorable_Code_Point » de `DerivedCoreProperties.txt`.

Décision de la mère (08:55Z, 08:59Z) : voie (b). Les plages viennent du seul fichier versé par la mère, lu à son empreinte,
à la version d'Unicode de l'interpréteur de la course (15.1.0). Ce programme :
- vérifie l'empreinte du fichier source ;
- lit la version dans sa première ligne (`# DerivedCoreProperties-X.Y.Z.txt`) et refuse si elle diffère de 15.1.0 ou de
  `unicodedata.unidata_version` de l'interpréteur qui joue ;
- prend, dans l'ordre du fichier, chaque ligne de données dont le second champ est exactement
  `Default_Ignorable_Code_Point` (un point ou une plage `XXXX..YYYY`) ; refuse une plage non triée ou chevauchante ;
- relit le total écrit par le fichier (`# Total code points: N`, première ligne de ce type après la dernière ligne de la
  propriété) et refuse s'il diffère du compte des plages ;
- écrit le fichier de données (`ignorables-unicode-na-v1`), clés triées, sans heure, et refuse une sortie existante (R12).

Usage : `python -B -m pole.extraire_ignorables_unicode_na_v1 --source F --empreinte-source H --chemin-depot C --commit K
--sortie S`. Bibliothèque standard seule.
"""

import argparse
import hashlib
import json
import os
import re
import sys
import unicodedata

from pole import garde_motifs_na_v3 as gm

_ENTETE = re.compile(r"^# DerivedCoreProperties-(\d+\.\d+\.\d+)\.txt$")
_DONNEE = re.compile(r"^([0-9A-F]{4,6})(?:\.\.([0-9A-F]{4,6}))?\s*;\s*([A-Za-z_]+)\s*(?:#.*)?$")
_TOTAL = re.compile(r"^# Total code points: (\d+)$")


class ExtractionRefusee(ValueError):
    pass


def extraire(octets, empreinte_attendue, chemin_depot, commit, version_interprete=None):
    """Rend l'objet des données ; refuse tout écart à l'empreinte, à la version, à l'ordre ou au total."""
    sha = hashlib.sha256(octets).hexdigest()
    if sha != empreinte_attendue:
        raise ExtractionRefusee("empreinte du fichier source différente de celle qui est donnée")
    lignes = octets.decode("utf-8").split("\n")
    m = _ENTETE.match(lignes[0].rstrip("\r")) if lignes else None
    if m is None:
        raise ExtractionRefusee("première ligne : « # DerivedCoreProperties-X.Y.Z.txt » attendue")
    version = m.group(1)
    if version != gm.VERSION_UNICODE_ATTENDUE:
        raise ExtractionRefusee(f"version du fichier {version} différente de {gm.VERSION_UNICODE_ATTENDUE}")
    try:
        gm.verifier_version_interprete(version, version_interprete)
    except gm.VersionUnicodeDifferente as e:
        raise ExtractionRefusee(str(e)) from None
    en_tete = lignes[0].lstrip("# ").rstrip("\r")
    if len(lignes) > 1 and lignes[1].startswith("# Date:"):
        en_tete += " ; " + lignes[1].lstrip("# ").rstrip("\r")
    plages, derniere, fin_prec = [], None, -1
    for i, brute in enumerate(lignes):
        ligne = brute.rstrip("\r")
        d = _DONNEE.match(ligne)
        if d is None or d.group(3) != gm.PROPRIETE:
            continue
        debut = int(d.group(1), 16)
        fin = int(d.group(2), 16) if d.group(2) else debut
        if not 0 <= debut <= fin <= 0x10FFFF or debut <= fin_prec:
            raise ExtractionRefusee(f"ligne {i + 1} : plage non triée, chevauchante ou hors d'Unicode")
        fin_prec = fin
        plages.append([debut, fin])
        derniere = i
    if not plages:
        raise ExtractionRefusee("aucune ligne de la propriété")
    total_ecrit = None
    for ligne in lignes[derniere + 1:]:
        t = _TOTAL.match(ligne.rstrip("\r"))
        if t is not None:
            total_ecrit = int(t.group(1))
            break
    total = sum(f - d + 1 for d, f in plages)
    if total_ecrit is None or total_ecrit != total:
        raise ExtractionRefusee(f"total écrit {total_ecrit} différent du compte des plages {total}")
    return {
        "format": gm.FORMAT_DONNEES,
        "propriete": gm.PROPRIETE,
        "version_unicode": version,
        "source": {"chemin": chemin_depot, "sha256": sha, "commit": commit, "en_tete": en_tete},
        "plages": plages,
        "total": total,
    }


def serialiser(donnees):
    return (json.dumps(donnees, ensure_ascii=False, sort_keys=True, indent=1) + "\n").encode("utf-8")


def main(argv=None):
    p = argparse.ArgumentParser(description="extraction des ignorables par défaut d'Unicode, véhicule NA-1")
    for nom in ("--source", "--empreinte-source", "--chemin-depot", "--commit", "--sortie"):
        p.add_argument(nom, required=True)
    a = p.parse_args(argv)
    if os.path.exists(a.sortie):
        raise ExtractionRefusee("sortie existante : on n'écrase jamais (R12)")
    with open(a.source, "rb") as f:
        octets = serialiser(extraire(f.read(), a.empreinte_source, a.chemin_depot, a.commit))
    with open(a.sortie, "xb") as f:
        f.write(octets)
    print(json.dumps({"sortie_sha256": hashlib.sha256(octets).hexdigest(), "octets": len(octets),
                      "unicodedata": unicodedata.unidata_version}))
    return 0


if __name__ == "__main__":
    sys.exit(main())
