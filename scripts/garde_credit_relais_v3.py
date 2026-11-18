#!/usr/bin/env python3
"""Garde de crédit d'un relais à solde illisible (Argon, Astra, Carbon) — version 3 de la course d'affinage des idées des mentors.

Décision de la mère R-3237, point (2) : pour les clés dont aucune session ne lit le solde (R-3222), départ permis sous
dispense écrite, **arrêt de la course au premier refus pour crédit**, coût compté au prix des fichiers (celui que la commande
du relais rend dans `cout_usd`). Cette enveloppe est mise par le lanceur v3 devant la commande déclarée du relais :

    python3 -I -B garde_credit_relais_v3.py DOSSIER_DES_ARRETS ETIQUETTE -- COMMANDE ARGS…

Elle passe l'entrée standard à la commande, renvoie sa sortie standard et sa sortie d'erreur **telles quelles** et son code ;
elle lit seulement la dernière ligne JSON de la sortie (contrat de la commande externe : `{"texte", "cout_usd", …}`). Si cette
ligne, ou la sortie d'erreur, porte un motif de refus pour crédit, elle écrit (une fois) `DOSSIER_DES_ARRETS/arret-credit-
ETIQUETTE.json` (motif, code ; jamais le texte ni une clé), que le lanceur surveille : il arrête alors l'orchestrateur par
son PID (signal SIGTERM, arrêt propre, manifestes écrits). Aucune valeur de clé n'est lue ; l'environnement est passé tel quel.

Bibliothèque standard seulement.
"""
from __future__ import annotations

import json
import os
import re
import subprocess
import sys

VERSION = "garde_credit_relais_v3"
MOTIFS_CREDIT = re.compile(r"(insufficient[_ ]?(funds|quota|balance|credit)|exceeded your current quota|quota exceeded|"
                           r"billing|payment required|credit balance|out of credits?|resource_exhausted|\b402\b|"
                           r"cr[ée]dit (insuffisant|épuisé|epuise)|solde (insuffisant|épuisé|epuise))", re.I)


def derniere_ligne_json(texte: str):
    for ligne in reversed([l for l in texte.splitlines() if l.strip()]):
        try:
            o = json.loads(ligne)
        except ValueError:
            return None
        return o if isinstance(o, dict) else None
    return None


def motif_credit(sortie: str, erreur: str) -> str | None:
    o = derniere_ligne_json(sortie)
    morceaux = [erreur or ""]
    if o is not None:
        morceaux += [str(o.get(k) or "") for k in ("erreur", "motif", "statut", "code_http", "message")]
    m = MOTIFS_CREDIT.search(" ".join(morceaux))
    return m.group(0) if m else None


def principal(argv: list) -> int:
    if len(argv) < 4 or argv[2] != "--":
        print(json.dumps({"texte": "", "cout_usd": 1e-06, "erreur": "garde de crédit : usage DOSSIER ETIQUETTE -- COMMANDE"}))
        return 2
    dossier, etiquette, commande = argv[0], argv[1], argv[3:]
    entree = sys.stdin.buffer.read()
    p = subprocess.run(commande, input=entree, capture_output=True)
    sortie, erreur = p.stdout.decode("utf-8", "replace"), p.stderr.decode("utf-8", "replace")
    sys.stdout.buffer.write(p.stdout)
    sys.stdout.flush()
    sys.stderr.buffer.write(p.stderr)
    sys.stderr.flush()
    motif = motif_credit(sortie, erreur)
    if motif:
        os.makedirs(dossier, exist_ok=True)
        chemin = os.path.join(dossier, f"arret-credit-{re.sub(r'[^a-z0-9-]', '-', etiquette.lower())}.json")
        try:
            with open(chemin, "x", encoding="utf-8") as f:
                json.dump({"version": VERSION, "relais": etiquette, "motif": motif, "code_commande": p.returncode}, f)
        except FileExistsError:
            pass
    return p.returncode


if __name__ == "__main__":
    raise SystemExit(principal(sys.argv[1:]))
