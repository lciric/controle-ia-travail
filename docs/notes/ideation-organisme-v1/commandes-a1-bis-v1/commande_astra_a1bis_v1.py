#!/usr/bin/env python3
"""Commande externe Astra (gpt-6-astra, OpenAI) pour A1-bis (pôle v56), relais local sur le port 8807 — v1.

Écrit le 2 novembre 2026 (session fille de session-depot) ; aucun appel réel n'a été fait. Contrat commun :
`commande_pole_v56_commun_v1.py` (repris de `commande_argon_v56_nuit_v2.py`).

Appel : `appeler_openai(modele, prompt, max_tokens, attentes=(0,))` du collisionneur v8 (`collisionneur_v8.py`, 22e5ed8a…,
copie à côté, empreinte vérifiée au démarrage du relais) : chat/completions, `max_completion_tokens`, aucune reprise interne,
clé OPENAI_API_KEY dans le seul environnement du relais, OPENAI_BASE_URL acceptée seulement vers la boucle locale (essais).

CORRECTION du double compte relevé sur le v8 : le v8 ajoutait `completion_tokens_details.reasoning_tokens` à
`completion_tokens`, alors que `completion_tokens` les contient déjà (journaux des runs v8 : sortie = visible + raisonnement,
p. ex. 4 612 + 245 = 4 857). Ici la sortie facturée est `completion_tokens` SEUL (champ `sortie_visible` de l'usage du v8) ;
`raisonnement` reste consigné pour mémoire. Prix supposés hauts (10 / 50 USD par million, entrée / sortie), comme le v8.
Statut : celui du v8 pour « openai » (stop → OK, length → TRONQUE, content_filter ou refusal → REFUS, autre → ANOMALIE).
Modèle : `--modele` explicite à chaque appel ; le modèle servi doit être l'identifiant demandé, exactement (code 5 sinon).
Réglage annoncé et comparé par le relais : `compte_sortie` = "completion_tokens" (aucun effort de raisonnement n'est transmis :
l'interface garde le sien, comme dans le v8).

Usage :
  env -i PATH=… LANG=C.UTF-8 OPENAI_API_KEY="$OPENAI_API_KEY" HTTPS_PROXY=… SSL_CERT_FILE=… \\
      python3 -I -B commande_astra_a1bis_v1.py servir --port 8807 --plafond-usd P --max-appels N --journal J.jsonl \\
      --modeles-permis gpt-6-astra
  python3 -I -B commande_astra_a1bis_v1.py appeler --modele gpt-6-astra --max-sortie-proposeur 32000 --max-sortie-court 4000 \\
      --sortie-min-jetons 1000 --registre R.jsonl --plafond-cumule-usd P
"""

import argparse
import hashlib
import importlib.util
import os
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ICI)
import commande_pole_v56_commun_v1 as commun  # noqa: E402

VERSION = "commande-astra-a1bis-v1"
PORT = 8807
PRIX = {"gpt-6-astra": (10.0, 50.0)}  # SUPPOSÉ haut, comme le collisionneur v8
REGLAGES = {"compte_sortie": "completion_tokens"}
COLLISIONNEUR = os.path.join(ICI, "collisionneur_v8.py")
SHA_COLLISIONNEUR = "22e5ed8a64075f2f985755d9bff2c2336d8edc5f73cbc3b0511405fd8f43d264"


def charger_collisionneur(chemin=COLLISIONNEUR, sha=SHA_COLLISIONNEUR):
    with open(chemin, "rb") as f:
        vu = hashlib.sha256(f.read()).hexdigest()
    if vu != sha:
        raise SystemExit(f"collisionneur {chemin} : empreinte {vu[:12]}… différente de {sha[:12]}… : refus de servir")
    spec = importlib.util.spec_from_file_location("collisionneur_v8_a1bis", chemin)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def usage_corrige(u):
    """Sortie = completion_tokens seul (le raisonnement y est déjà) ; correction du double compte du v8."""
    u = dict(u or {})
    if "sortie_visible" in u:
        u["sortie_v8_double_compte"] = u.get("sortie")
        u["sortie"] = u["sortie_visible"]
    return u


class FournisseurAstra:
    nature = "collisionneur_v8.appeler_openai(attentes=(0,)), sortie = completion_tokens"

    def __init__(self, environ, cv):
        self.cle = environ.get("OPENAI_API_KEY") or ""
        self.cv = cv
        self.Reponse = cv.Reponse

    def cle_presente(self):
        return bool(self.cle)

    def masquer(self, texte):
        texte = str(texte)
        return texte.replace(self.cle, "[clé]") if len(self.cle) >= 8 else texte

    def prix(self, modele):
        return PRIX[modele]

    def appeler(self, modele, prompt, max_tokens, reglages):
        rep = self.cv.appeler_openai(modele, prompt, max_tokens, attentes=(0,))
        if not rep.echec:
            rep.usage = usage_corrige(rep.usage)
        return rep

    def statut(self, rep):
        return self.cv.statut_reponse("openai", rep)


def principal(argv=None, environ=None, entree=None):
    argv = list(sys.argv[1:] if argv is None else argv)
    if not argv or argv[0] not in ("servir", "appeler"):
        argv = ["appeler"] + argv
    environ = dict(os.environ) if environ is None else environ
    a = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sous = a.add_subparsers(dest="mode", required=True)
    s = sous.add_parser("servir")
    commun.ajouter_options_servir(s)
    p = sous.add_parser("appeler")
    commun.ajouter_options_appeler(p, PORT)
    args = a.parse_args(argv)
    if args.mode == "servir":
        if args.port <= 0 or args.plafond_usd <= 0 or args.max_appels <= 0:
            raise SystemExit("servir : --port, --plafond-usd, --max-appels strictement positifs")
        for m in [m.strip() for m in args.modeles_permis.split(",") if m.strip()]:
            if m not in PRIX:
                raise SystemExit(f"modèle {m!r} hors de {sorted(PRIX)} : refus")
        cv = charger_collisionneur()
        f = FournisseurAstra(environ, cv)
        if not f.cle_presente():
            raise SystemExit("OPENAI_API_KEY absente de l'environnement du relais : refus de servir")
        return commun.servir(args, f, VERSION, REGLAGES)

    def faire():
        if args.modele not in PRIX:
            commun.rendre(2, VERSION, erreur=f"--modele {args.modele!r} hors de {sorted(PRIX)}", envoye=False)
        commun.appeler(args, environ, sys.stdin if entree is None else entree, nom_fournisseur="astra", version=VERSION,
                       prix=PRIX[args.modele], reglages=REGLAGES)
    return commun.executer(faire)


if __name__ == "__main__":
    sys.exit(principal())
