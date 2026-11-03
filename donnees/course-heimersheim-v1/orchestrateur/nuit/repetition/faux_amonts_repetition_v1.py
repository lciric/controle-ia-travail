#!/usr/bin/env python3
"""Faux amonts de la répétition de la mini-course (aucun réseau, aucune clé réelle, aucune dépense) — version 1.

Rédigé le 1er novembre 2026 (sous-agent de session-depot), pour la répétition complète en « moteur réel » sans réseau :
les vraies commandes (`commande_kimi_v2.py`, `commande_argon_v56_nuit_v1.py appeler`), le vrai relais Kimi
(`relais_kimi_v3.py`, empreinte vérifiée, clé **factice**, `--amont` vers la boucle locale), le vrai serveur du relais Argon
(fonction `servir` de `commande_argon_v56_nuit_v1.py`), le vrai registre cumulé et le vrai lanceur ; **seul l'amont est
remplacé**, par des réponses déterministes au format attendu (moteur simulé v56 de l'orchestrateur,
`pole/simulation_v56.AdaptateurSimuleV56`, six fiches par proposeur).

Sous-commandes :
  kimi  --port-fichier F [--fiche-factice CHAINE]   faux amont Kimi, compatible OpenAI, en flux SSE (comme Moonshot, supposé)
  argon --port P --journal J [--fiche-factice CHAINE] relais Argon réel (`servir`) dont l'appelant est remplacé (aucun réseau)

`--fiche-factice` : la première fiche de chaque proposeur porte la chaîne canari (fiche factice du préenregistrement).
"""

import argparse
import json
import os
import sys
import threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

ICI = os.path.dirname(os.path.abspath(__file__))
NUIT = os.path.dirname(ICI)
RACINE = os.path.dirname(NUIT)
sys.path.insert(0, RACINE)
sys.path.insert(0, NUIT)

from pole.simulation_v56 import AdaptateurSimuleV56  # noqa: E402

with open(os.path.join(NUIT, "configuration-mini-course-kimi-argon-v1.json"), encoding="utf-8") as _f:
    CONF = json.load(_f)


def simulateur():
    return AdaptateurSimuleV56(champs_fiche=CONF["champs_fiche"], items=CONF["items_juge"], champ_titre=CONF["champ_titre"],
                               cout_par_appel_usd=0.01, fiches_par_appel=6)


def texte_simule(sim, prompt, modele, fiche_factice):
    t = sim.reponse("inconnu", prompt, modele)
    if fiche_factice and "## Case" in prompt and "## Les deux fiches" not in prompt:
        o = json.loads(t)
        o["fiches"][0]["hypothese"] += " " + fiche_factice
        t = json.dumps(o, ensure_ascii=False)
    if "seulement par le mot OK" in prompt:
        t = "OK"
    return "Réponse simulée.\n```json\n" + t + "\n```\n" if t != "OK" else t


def faux_kimi(args):
    sim, verrou, compte = simulateur(), threading.Lock(), {"n": 0}

    class Gestion(BaseHTTPRequestHandler):
        def log_message(self, *a):
            pass

        def do_POST(self):
            corps = json.loads(self.rfile.read(int(self.headers.get("Content-Length") or 0)) or b"{}")
            if self.path != "/v1/chat/completions" or not corps.get("stream"):
                self.send_response(400)
                self.end_headers()
                return
            with verrou:
                compte["n"] += 1
            prompt = corps["messages"][-1]["content"]
            texte = texte_simule(sim, prompt, corps["model"], args.fiche_factice)
            usage = {"prompt_tokens": len(prompt.encode("utf-8")) // 4, "completion_tokens": len(texte) // 3 + 300}
            usage["total_tokens"] = usage["prompt_tokens"] + usage["completion_tokens"]
            morceaux = [{"choices": [{"index": 0, "delta": {"reasoning_content": "raisonnement simulé. "}}]}]
            for i in range(0, len(texte), 400):
                morceaux.append({"choices": [{"index": 0, "delta": {"content": texte[i:i + 400]}}]})
            morceaux.append({"choices": [{"index": 0, "delta": {}, "finish_reason": "stop"}], "usage": usage})
            self.send_response(200)
            self.send_header("Content-Type", "text/event-stream")
            self.send_header("Connection", "close")
            self.end_headers()
            for m in morceaux:
                m.update(id="chatcmpl-repetition", object="chat.completion.chunk", model=corps["model"])
                self.wfile.write(b"data: " + json.dumps(m, ensure_ascii=False).encode("utf-8") + b"\n\n")
            self.wfile.write(b"data: [DONE]\n\n")
            self.wfile.flush()
            self.close_connection = True

    serveur = ThreadingHTTPServer(("127.0.0.1", 0), Gestion)
    with open(args.port_fichier, "w", encoding="utf-8") as f:
        f.write(str(serveur.server_address[1]))
    print(f"faux amont Kimi prêt sur http://127.0.0.1:{serveur.server_address[1]}", flush=True)
    try:
        serveur.serve_forever()
    except KeyboardInterrupt:
        pass
    return 0


def faux_argon(args):
    import commande_argon_v56_nuit_v1 as cmd
    c = cmd.charger_collisionneur(cmd.COLLISIONNEUR_DEFAUT, cmd.SHA_COLLISIONNEUR)
    sim = simulateur()

    def appelant(modele, prompt, max_tokens):
        texte = texte_simule(sim, prompt, modele, args.fiche_factice)
        return c.Reponse(texte=texte, modele_servi=modele, identifiant="repetition", fin="STOP",
                         usage={"entree": max(1, len(prompt) // 4), "sortie": min(max_tokens, len(texte) // 3 + 50)},
                         types_blocs=["text"])

    a = argparse.Namespace(port=args.port, plafond_usd=10.0, max_appels=60, journal=args.journal, modeles_permis="gemini-4-argon",
                           collisionneur=cmd.COLLISIONNEUR_DEFAUT, sha_collisionneur=cmd.SHA_COLLISIONNEUR)
    return cmd.servir(a, appelant=appelant, c=c, environ={}, nature_appelant="faux amont de répétition (aucun réseau)")


def principal(argv=None):
    a = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    s = a.add_subparsers(dest="mode", required=True)
    k = s.add_parser("kimi")
    k.add_argument("--port-fichier", required=True)
    k.add_argument("--fiche-factice", default=None)
    g = s.add_parser("argon")
    g.add_argument("--port", type=int, required=True)
    g.add_argument("--journal", required=True)
    g.add_argument("--fiche-factice", default=None)
    args = a.parse_args(argv)
    return faux_kimi(args) if args.mode == "kimi" else faux_argon(args)


if __name__ == "__main__":
    sys.exit(principal())
