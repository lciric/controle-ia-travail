#!/usr/bin/env python3
"""Commande externe Claude pour A1-bis (pôle v56), relais local sur le port 8806 — v1.

Écrit le 2 novembre 2026 (session fille de session-depot) ; aucun appel réel n'a été fait. Contrat commun :
`commande_pole_v56_commun_v1.py` (repris de `commande_argon_v56_nuit_v2.py`).

Modèles : tout identifiant Anthropic de `PRIX` (claude-fable-5-1, claude-opus-5-5, claude-opus-4-6), passé EXPLICITEMENT par
`--modele` à chaque appel et permis par `--modeles-permis` au relais. La commande ne bascule jamais : pas de paramètre
`fallbacks`, pas de repli ; le modèle servi doit être l'identifiant demandé, exactement (sinon code 5). C'est le lanceur qui
choisit le modèle au début de l'unité.

Réglages explicites, obligatoires aux deux bouts et comparés par le relais (refus 409 s'ils diffèrent) : `--effort`
(output_config.effort : low, medium, high, xhigh, max ; xhigh n'existe pas sur claude-opus-4-6) et `--reflexion`
(`adaptative` → thinking {"type": "adaptive"} ; `omise` → paramètre absent : Fable 5.1 et Opus 5.5 réfléchissent quand même,
Opus 4.6 ne réfléchit pas). Les deux figurent dans la ligne de commande de la configuration, donc au manifeste du lanceur, et
dans chaque dernière ligne rendue (`reglages`). Sortie maximale : `--max-sortie-proposeur`, `--max-sortie-court` (obligatoires).
L'effort par défaut d'Opus 5.5 est `medium` : il n'y a ici aucun défaut, la valeur est toujours écrite.

Appel : SDK `anthropic`, `messages.stream(...).get_final_message()`, `max_retries=0` (aucune reprise interne), délai 1 800 s.
Prix (USD par million, entrée / sortie), relevés le 2 novembre 2026 dans la documentation de l'interface (table des modèles,
cache du 6 octobre 2026) : Fable 5.1 10 / 50 ; Opus 5.5 4 / 20 ; Opus 4.6 5 / 25. Coût : input_tokens et output_tokens de
`usage` (la sortie compte la réflexion). Statut : end_turn → OK (VIDE si aucun texte) ; max_tokens → TRONQUE ; refusal → REFUS
(catégorie de stop_details) ; autre → ANOMALIE.
ANTHROPIC_BASE_URL n'est acceptée que vers la boucle locale (essais hors réseau) ; toute autre adresse est refusée au
démarrage du relais. Clé : ANTHROPIC_API_KEY dans le seul environnement du relais (valeur prise de RR_ANTHROPIC_API_KEY_LUC
par le lanceur, sous env -i) ; ANTHROPIC_WORKSPACE_ID facultatif (en-tête), jamais affiché.

Usage :
  env -i PATH=… LANG=C.UTF-8 ANTHROPIC_API_KEY="$RR_ANTHROPIC_API_KEY_LUC" HTTPS_PROXY=… SSL_CERT_FILE=… \\
      <python avec anthropic> -I -B commande_claude_a1bis_v1.py servir --port 8806 --plafond-usd P --max-appels N \\
      --journal J.jsonl --modeles-permis claude-opus-5-5 --effort high --reflexion adaptative
  python3 -I -B commande_claude_a1bis_v1.py appeler --modele claude-opus-5-5 --effort high --reflexion adaptative \\
      --max-sortie-proposeur 32000 --max-sortie-court 4000 --sortie-min-jetons 1000 --registre R.jsonl --plafond-cumule-usd P
"""

import argparse
import os
import sys
from dataclasses import dataclass, field

ICI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ICI)
import commande_pole_v56_commun_v1 as commun  # noqa: E402

VERSION = "commande-claude-a1bis-v1"
PORT = 8806
PRIX = {"claude-fable-5-1": (10.0, 50.0), "claude-opus-5-5": (4.0, 20.0), "claude-opus-4-6": (5.0, 25.0)}
EFFORTS = {"claude-fable-5-1": ("low", "medium", "high", "xhigh", "max"),
           "claude-opus-5-5": ("low", "medium", "high", "xhigh", "max"),
           "claude-opus-4-6": ("low", "medium", "high", "max")}
REFLEXIONS = ("adaptative", "omise")
DELAI_S = 1800.0


@dataclass
class Reponse:
    texte: str = ""
    modele_servi: str = None
    fin: str = None
    categorie: str = None
    usage: dict = field(default_factory=dict)
    echec: str = None


class FournisseurClaude:
    Reponse = Reponse
    nature = "anthropic.Anthropic(max_retries=0).messages.stream(...).get_final_message()"

    def __init__(self, environ, client=None):
        self.cle = environ.get("ANTHROPIC_API_KEY") or ""
        self._client = client

    def cle_presente(self):
        return bool(self.cle)

    def masquer(self, texte):
        texte = str(texte)
        return texte.replace(self.cle, "[clé]") if len(self.cle) >= 8 else texte

    def prix(self, modele):
        return PRIX[modele]

    def client(self):
        if self._client is None:
            import anthropic
            espace = os.environ.get("ANTHROPIC_WORKSPACE_ID")
            self._client = anthropic.Anthropic(max_retries=0, timeout=DELAI_S,
                                               default_headers={"anthropic-workspace-id": espace} if espace else None)
        return self._client

    def appeler(self, modele, prompt, max_tokens, reglages):
        import anthropic
        params = {"model": modele, "max_tokens": max_tokens, "output_config": {"effort": reglages["effort"]},
                  "messages": [{"role": "user", "content": prompt}]}
        if reglages["reflexion"] == "adaptative":
            params["thinking"] = {"type": "adaptive"}
        try:
            with self.client().messages.stream(**params) as flux:
                msg = flux.get_final_message()
        except anthropic.APIStatusError as e:
            return Reponse(echec=f"HTTP {e.status_code} {type(e).__name__} : {self.masquer(str(e))[:300]}")
        except anthropic.APIError as e:
            return Reponse(echec=f"{type(e).__name__} : {self.masquer(str(e))[:300]}")
        details = getattr(msg, "stop_details", None)
        return Reponse(texte="".join(b.text for b in msg.content if b.type == "text"), modele_servi=msg.model,
                       fin=msg.stop_reason,
                       categorie=getattr(details, "category", None) if msg.stop_reason == "refusal" else None,
                       usage={"entree": msg.usage.input_tokens, "sortie": msg.usage.output_tokens})

    @staticmethod
    def statut(rep):
        plein = bool((rep.texte or "").strip())
        if rep.fin == "refusal":
            return "REFUS"
        if rep.fin == "max_tokens":
            return "TRONQUE" if plein else "VIDE"
        if rep.fin == "end_turn":
            return "OK" if plein else "VIDE"
        return "ANOMALIE"


def verifier_reglages(modeles, effort, reflexion):
    for m in modeles:
        if m not in PRIX:
            raise SystemExit(f"modèle {m!r} hors de la table des prix {sorted(PRIX)} : refus")
        if effort not in EFFORTS[m]:
            raise SystemExit(f"effort {effort!r} non permis pour {m} (permis : {EFFORTS[m]})")
    if reflexion not in REFLEXIONS:
        raise SystemExit(f"--reflexion {reflexion!r} : {REFLEXIONS}")


def verifier_base_url(environ):
    base = environ.get("ANTHROPIC_BASE_URL")
    if base and not base.startswith(("http://127.0.0.1:", "http://localhost:")) and base.rstrip("/") != "https://api.anthropic.com":
        raise SystemExit("ANTHROPIC_BASE_URL : boucle locale (essais hors réseau) ou adresse d'Anthropic seulement")


def principal(argv=None, environ=None, entree=None, client=None):
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
    for x in (s, p):
        x.add_argument("--effort", required=True)
        x.add_argument("--reflexion", required=True)
    args = a.parse_args(argv)
    reglages = {"effort": args.effort, "reflexion": args.reflexion}
    if args.mode == "servir":
        if args.port <= 0 or args.plafond_usd <= 0 or args.max_appels <= 0:
            raise SystemExit("servir : --port, --plafond-usd, --max-appels strictement positifs")
        modeles = [m.strip() for m in args.modeles_permis.split(",") if m.strip()]
        verifier_reglages(modeles, args.effort, args.reflexion)
        verifier_base_url(environ)
        f = FournisseurClaude(environ, client)
        if client is None and not f.cle_presente():
            raise SystemExit("ANTHROPIC_API_KEY absente de l'environnement du relais : refus de servir")
        return commun.servir(args, f, VERSION, reglages)

    def faire():
        if args.modele not in PRIX:
            commun.rendre(2, VERSION, erreur=f"--modele {args.modele!r} hors de {sorted(PRIX)}", envoye=False)
        try:
            verifier_reglages([args.modele], args.effort, args.reflexion)
        except SystemExit as e:
            commun.rendre(2, VERSION, erreur=str(e), envoye=False)
        commun.appeler(args, environ, sys.stdin if entree is None else entree, nom_fournisseur="claude", version=VERSION,
                       prix=PRIX[args.modele], reglages=reglages)
    return commun.executer(faire)


if __name__ == "__main__":
    sys.exit(principal())
