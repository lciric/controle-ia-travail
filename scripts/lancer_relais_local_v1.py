#!/usr/bin/env python3
"""Lanceur d'un relais local (clé par nom, environnement réduit à une liste de noms) — version 1.

Écrit le 18 novembre 2026 par la session de relance des organismes discrets ; remplace le lanceur hors dépôt des courses
de novembre (`/home/user/hors-depot/…/lancer_relais_v1.py`, `bf781533…`, disparu avec son conteneur), même contrat :

    python3 -I -B scripts/lancer_relais_local_v1.py CONSOLE NOM1,NOM2,… -- COMMANDE ARG…

- l'environnement du relais est **réduit aux noms listés** qui existent dans l'environnement courant (valeurs prises par
  nom, jamais lues ni écrites par ce script) ; `ANTHROPIC_BASE_URL`, `CLAUDE_CODE_REMOTE` et tout nom qui commence par
  `CLAUDE` ou `CCR` sont **refusés** (ils redirigeraient ou marqueraient l'appel) ;
- le relais part dans une **session de processus neuve** (`setsid`), dossier courant = dossier de CONSOLE, entrée standard
  fermée, sorties vers CONSOLE (créé, jamais écrasé) ;
- imprime une ligne JSON `{"pid", "console", "noms_transmis", "noms_absents"}` ; code 2 sur tout refus, rien lancé.

Bibliothèque standard seulement. Essais : `tests/test_lancer_relais_local_v1.py`.
"""
from __future__ import annotations

import json
import os
import subprocess
import sys

VERSION = "lancer_relais_local_v1"
NOMS_REFUSES = ("ANTHROPIC_BASE_URL", "CLAUDE_CODE_REMOTE")
PREFIXES_REFUSES = ("CLAUDE", "CCR")


class Refus(RuntimeError):
    pass


def environnement_reduit(noms: list, source) -> tuple:
    transmis, absents = {}, []
    for n in noms:
        if not n or n in NOMS_REFUSES or n.startswith(PREFIXES_REFUSES):
            raise Refus(f"nom refusé dans la liste : {n!r}")
        if n in source:
            transmis[n] = source[n]
        else:
            absents.append(n)
    if "PATH" not in transmis:
        transmis["PATH"] = os.defpath
    return transmis, absents


def lancer(console: str, noms: list, commande: list, source=None) -> dict:
    source = os.environ if source is None else source
    if not commande:
        raise Refus("aucune commande après « -- »")
    if os.path.exists(console):
        raise Refus(f"console déjà présente : {console} (R12 : jamais écrasée)")
    dossier = os.path.dirname(os.path.abspath(console))
    if not os.path.isdir(dossier):
        raise Refus(f"dossier de la console absent : {dossier}")
    env, absents = environnement_reduit(noms, source)
    with open(console, "xb") as f:
        p = subprocess.Popen(commande, cwd=dossier, env=env, stdin=subprocess.DEVNULL, stdout=f, stderr=subprocess.STDOUT,
                             start_new_session=True)
    return {"pid": p.pid, "console": os.path.abspath(console), "noms_transmis": sorted(env), "noms_absents": absents,
            "commande": commande, "version": VERSION}


def principal(argv: list | None = None) -> int:
    argv = sys.argv[1:] if argv is None else list(argv)
    try:
        if len(argv) < 4 or argv[2] != "--":
            raise Refus("usage : CONSOLE NOM1,NOM2,… -- COMMANDE ARG…")
        noms = [n.strip() for n in argv[1].split(",")]
        print(json.dumps(lancer(argv[0], noms, argv[3:]), ensure_ascii=False), flush=True)
        return 0
    except Refus as e:
        print(json.dumps({"refus": str(e)}, ensure_ascii=False), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(principal())
