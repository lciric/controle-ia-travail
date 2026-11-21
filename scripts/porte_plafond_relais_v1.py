#!/usr/bin/env python3
"""Porte de plafond d'un relais persistant (Claude, Kimi) — version 1, pour la course d'affinage des idées des mentors (v4).

Contrat de l'orchestrateur (`pole/adaptateurs_v56.py`, classe `PortePlafondCommande`) : au lancement de chaque étape, la
commande de la porte est lancée avec un environnement minimal **sans aucun nom de clé** (`PATH`, `HOME`, `LANG`, `LC_ALL`,
`TMPDIR`, plus `ETAPE_POLE` et `PLAFOND_ETAPE_USD`) ; elle doit rendre le code 0 et imprimer en dernière ligne
`{"etape": <ETAPE_POLE>, "plafond_usd": <PLAFOND_ETAPE_USD>}`, égal au centime ; sinon l'étape n'est pas lancée (A15).

Option appliquée : **relais de ligne entière** (procédure neutre `docs/procedures/relais-persistants-v1.md`, § 4, seconde
forme ; recommandation de la contre-lecture de la v3, constat 1) — le relais est lancé une fois, par le lanceur de relais de la
procédure, au plafond de la ligne (≤ plafond de la ligne de GO), sa clé lue **par son nom** dans son seul environnement au
démarrage (jamais sur une ligne de commande, jamais ici) ; l'étape est bornée par le plafond dur que l'orchestrateur tient
seul (cumul, règle d'A1) ; la porte **contrôle le relais vivant** et accuse le plafond de l'étape. Elle ne relance rien,
n'arrête rien, n'appelle aucun fournisseur.

Contrôles, sur `GET <url>/relais/etat` (boucle locale seulement, sans mandataire) :
- le relais répond, JSON lisible, `plafond_usd` > 0 et ≤ `--plafond-ligne` ;
- `modeles_permis` égal **exactement** (même ensemble) à `--modeles-permis` ;
- `depense_usd` ≤ `plafond_usd` ;
- étape « porte-a-blanc » (jouée par le lanceur de course avant son manifeste de départ) : en plus, `depense_usd` = 0 et
  `appels` = 0 (relais neuf, procédure § 3).

Usage : `python3 -I -B porte_plafond_relais_v1.py --url http://127.0.0.1:PORT --modeles-permis A,B --plafond-ligne 150`
Code 0 et l'accusé ; code 2 et un motif (sortie d'erreur) sur tout défaut. Bibliothèque standard seulement.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
import urllib.request

VERSION = "porte_plafond_relais_v1"
ETAPE_A_BLANC = "porte-a-blanc"
URL_LOCALE = re.compile(r"^http://(127\.0\.0\.1|localhost|\[::1\]):\d{2,5}$")


class Refus(RuntimeError):
    pass


def lire_etat(url: str, delai_s: float = 5.0) -> dict:
    ouvreur = urllib.request.build_opener(urllib.request.ProxyHandler({}))
    try:
        with ouvreur.open(url.rstrip("/") + "/relais/etat", timeout=delai_s) as rep:
            etat = json.loads(rep.read().decode("utf-8"))
    except Exception as e:  # noqa: BLE001
        raise Refus(f"relais injoignable ou réponse illisible ({type(e).__name__})") from None
    if not isinstance(etat, dict):
        raise Refus("état du relais : objet JSON attendu")
    return etat


def _nombre(v) -> bool:
    return isinstance(v, (int, float)) and not isinstance(v, bool)


def controler(etat: dict, modeles: list, plafond_ligne: float, etape: str) -> None:
    p, d = etat.get("plafond_usd"), etat.get("depense_usd")
    if not (_nombre(p) and p > 0):
        raise Refus(f"plafond du relais illisible ou nul : {p!r}")
    if p > plafond_ligne + 1e-9:
        raise Refus(f"plafond du relais {p} > plafond de la ligne {plafond_ligne}")
    if sorted(etat.get("modeles_permis") or []) != sorted(modeles):
        raise Refus(f"modèles permis du relais {etat.get('modeles_permis')!r} différents de ceux attendus")
    if not _nombre(d) or d < 0 or d > p + 1e-9:
        raise Refus(f"dépense du relais illisible ou au-delà de son plafond : {d!r}")
    if etape == ETAPE_A_BLANC and (d != 0 or etat.get("appels") not in (0, None)):
        raise Refus(f"porte à blanc : relais déjà employé (dépense {d}, appels {etat.get('appels')!r})")


def principal(argv: list | None = None, environnement=None) -> int:
    env = os.environ if environnement is None else environnement
    a = argparse.ArgumentParser(prog=VERSION)
    a.add_argument("--url", required=True)
    a.add_argument("--modeles-permis", required=True)
    a.add_argument("--plafond-ligne", type=float, required=True)
    try:
        args = a.parse_args(argv)
        if not URL_LOCALE.match(args.url):
            raise Refus(f"adresse hors boucle locale : {args.url!r}")
        etape, brut = env.get("ETAPE_POLE"), env.get("PLAFOND_ETAPE_USD")
        if not etape or brut is None:
            raise Refus("ETAPE_POLE et PLAFOND_ETAPE_USD exigés dans l'environnement")
        try:
            plafond_etape = float(brut)
        except ValueError:
            raise Refus(f"PLAFOND_ETAPE_USD illisible : {brut!r}") from None
        if plafond_etape < 0 or plafond_etape > args.plafond_ligne + 1e-9:
            raise Refus(f"plafond d'étape {plafond_etape} hors de [0 ; {args.plafond_ligne}]")
        modeles = [m.strip() for m in args.modeles_permis.split(",") if m.strip()]
        controler(lire_etat(args.url), modeles, args.plafond_ligne, etape)
    except SystemExit:
        return 2
    except Refus as e:
        print(json.dumps({"refus": str(e), "version": VERSION}, ensure_ascii=False), file=sys.stderr)
        return 2
    print(json.dumps({"etape": etape, "plafond_usd": round(plafond_etape, 2), "version": VERSION}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(principal())
