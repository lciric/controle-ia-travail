"""Applique des couples « ancien » -> « nouveau » à un brouillon, sans jamais écraser (R12).

Usage : python3 -I appliquer-couples-vadapt-v1.py BASE SHA_BASE COUPLES SHA_COUPLES SORTIE

- BASE et COUPLES sont vérifiés contre les empreintes données (arrêt sinon, R11) ;
- COUPLES est un fichier JSON : liste de {"id", "ancien", "nouveau"} ;
- chaque « ancien » doit apparaître exactement une fois dans le texte courant au moment de son
  application, et différer de son « nouveau » (arrêt sinon : aucun repli silencieux, R5) ;
- SORTIE ne doit pas exister (R12) ;
- après application : aucun motif de marqueur `<<…>>` restant ; rapport JSON imprimé
  (empreintes, nombre de couples, empreinte de la sortie).
Aucune dépendance hors de la bibliothèque standard.
"""
from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path


class Arret(Exception):
    pass


def empreinte(chemin: Path) -> str:
    return hashlib.sha256(chemin.read_bytes()).hexdigest()


def appliquer(texte: str, couples: list[dict]) -> tuple[str, list[dict]]:
    journal = []
    vus = set()
    for c in couples:
        ident, ancien, nouveau = c.get("id"), c.get("ancien"), c.get("nouveau")
        if not ident or not isinstance(ancien, str) or not isinstance(nouveau, str):
            raise Arret(f"couple mal formé : {c!r}"[:300])
        if ident in vus:
            raise Arret(f"identifiant en double : {ident}")
        vus.add(ident)
        if ancien == nouveau:
            raise Arret(f"{ident} : « ancien » égal à « nouveau »")
        n = texte.count(ancien)
        if n != 1:
            raise Arret(f"{ident} : « ancien » trouvé {n} fois (exactement 1 exigé)")
        texte = texte.replace(ancien, nouveau, 1)
        journal.append({"id": ident, "longueur_ancien": len(ancien), "longueur_nouveau": len(nouveau)})
    return texte, journal


def principal(argv: list[str]) -> int:
    if len(argv) != 6:
        print(__doc__)
        return 2
    base, sha_base, couples_p, sha_couples, sortie = Path(argv[1]), argv[2], Path(argv[3]), argv[4], Path(argv[5])
    try:
        if empreinte(base) != sha_base:
            raise Arret(f"empreinte de la base différente : {empreinte(base)}")
        if empreinte(couples_p) != sha_couples:
            raise Arret(f"empreinte des couples différente : {empreinte(couples_p)}")
        if sortie.exists():
            raise Arret(f"{sortie} existe déjà (R12 : jamais d'écrasement)")
        couples = json.loads(couples_p.read_text(encoding="utf-8"))
        if not isinstance(couples, list) or not couples:
            raise Arret("le fichier des couples doit être une liste non vide")
        texte, journal = appliquer(base.read_text(encoding="utf-8"), couples)
        marqueurs = re.findall(r"<<[^<>\n]{1,80}>>", texte)
        if marqueurs:
            raise Arret(f"marqueurs restants : {marqueurs[:5]}")
        sortie.write_text(texte, encoding="utf-8")
    except Arret as e:
        print(f"ARRÊT : {e}", file=sys.stderr)
        return 2
    print(json.dumps({
        "base": str(base), "sha_base": sha_base,
        "couples": str(couples_p), "sha_couples": sha_couples,
        "nombre_couples": len(journal), "couples_appliques": journal,
        "sortie": str(sortie), "sha_sortie": empreinte(sortie),
    }, ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(principal(sys.argv))
