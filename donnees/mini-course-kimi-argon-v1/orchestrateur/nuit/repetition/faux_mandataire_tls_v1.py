#!/usr/bin/env python3
"""Faux mandataire TLS de la répétition v2 de la mini-course (aucun réseau, aucune clé réelle, aucune dépense) — version 1.

Rédigé le 1er novembre 2026 (sous-agent de session-depot), pour faire tourner le **vrai** `lancer-mini-course-v2.sh` (mode
`repeter`) et les **vrais** chemins réseau des relais — `relais_kimi_v3.py` vers `https://api.moonshot.ai` et
`commande_argon_v56_nuit_v1.py servir`, donc `collisionneur_v7.appeler_gemini` vers
`https://generativelanguage.googleapis.com` — sans quitter la machine : les deux relais passent par `HTTPS_PROXY` ; ce
mandataire accepte `CONNECT hôte:443`, termine le TLS avec un certificat signé par une **autorité factice** de répétition
(que seul `SSL_CERT_FILE` de la répétition reconnaît), et répond au format de chaque interface (Moonshot en flux SSE,
Gemini en JSON) avec le moteur simulé v56 (six fiches par proposeur). Tout autre hôte, toute autre méthode : refus.

Options : `--pause-s` (attente avant chaque réponse, pour l'essai du `kill` en pleine course) ; `--fiche-factice` (canari
planté dans la première fiche de chaque proposeur) ; `--controle-modele-faux` (artefact : la réponse au contrôle d'Argon
porte un autre modèle servi). Journal (`--journal`) : hôte, chemin, modèle, présence d'une clé (booléen), jamais de texte.
"""

import argparse
import json
import os
import socket
import ssl
import sys
import threading
import time
from socketserver import ThreadingTCPServer, StreamRequestHandler

ICI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ICI)
import faux_amonts_repetition_v1 as fa  # noqa: E402  (moteur simulé v56 et texte factice, déjà employés en v1)

HOTES = ("api.moonshot.ai", "generativelanguage.googleapis.com")


def principal(argv=None):
    a = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    a.add_argument("--certificat", required=True)
    a.add_argument("--cle", required=True)
    a.add_argument("--port-fichier", required=True)
    a.add_argument("--journal", required=True)
    a.add_argument("--pause-s", type=float, default=0.0)
    a.add_argument("--fiche-factice", default=None)
    a.add_argument("--controle-modele-faux", action="store_true")
    args = a.parse_args(argv)
    ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    ctx.load_cert_chain(args.certificat, args.cle)
    sim, verrou = fa.simulateur(), threading.Lock()

    def journal(**e):
        with verrou, open(args.journal, "a", encoding="utf-8") as f:
            f.write(json.dumps(dict(e, quand=time.time()), ensure_ascii=False) + "\n")

    class Gestion(StreamRequestHandler):
        def handle(self):
            ligne = self.rfile.readline().decode("latin-1").strip()
            while self.rfile.readline() not in (b"\r\n", b"\n", b""):
                pass
            parties = ligne.split()
            if len(parties) < 2 or parties[0] != "CONNECT" or parties[1].rsplit(":", 1)[0] not in HOTES:
                self.wfile.write(b"HTTP/1.1 403 Forbidden\r\nContent-Length: 0\r\n\r\n")
                journal(refus=ligne[:120])
                return
            hote = parties[1].rsplit(":", 1)[0]
            self.wfile.write(b"HTTP/1.1 200 Connection established\r\n\r\n")
            self.wfile.flush()
            try:
                tls = ctx.wrap_socket(self.connection, server_side=True)
            except (ssl.SSLError, OSError) as e:
                journal(hote=hote, tls="échec", motif=type(e).__name__)
                return
            f = tls.makefile("rwb")
            requete = f.readline().decode("latin-1").strip()
            entetes = {}
            while True:
                l = f.readline().decode("latin-1")
                if l in ("\r\n", "\n", ""):
                    break
                k, _, v = l.partition(":")
                entetes[k.strip().lower()] = v.strip()
            corps = json.loads(f.read(int(entetes.get("content-length", "0"))) or b"{}")
            cle = bool(entetes.get("authorization") or entetes.get("x-goog-api-key"))
            if args.pause_s:
                time.sleep(args.pause_s)
            if hote == "api.moonshot.ai":
                prompt = corps["messages"][-1]["content"]
                texte = fa.texte_simule(sim, prompt, corps["model"], args.fiche_factice)
                usage = {"prompt_tokens": len(prompt.encode("utf-8")) // 4, "completion_tokens": len(texte) // 3 + 300}
                usage["total_tokens"] = usage["prompt_tokens"] + usage["completion_tokens"]
                morceaux = [{"choices": [{"index": 0, "delta": {"reasoning_content": "raisonnement simulé. "}}]}]
                morceaux += [{"choices": [{"index": 0, "delta": {"content": texte[i:i + 400]}}]} for i in range(0, len(texte), 400)]
                morceaux.append({"choices": [{"index": 0, "delta": {}, "finish_reason": "stop"}], "usage": usage})
                f.write(b"HTTP/1.1 200 OK\r\nContent-Type: text/event-stream\r\nConnection: close\r\n\r\n")
                for m in morceaux:
                    m.update(id="chatcmpl-repetition", object="chat.completion.chunk", model=corps["model"])
                    f.write(b"data: " + json.dumps(m, ensure_ascii=False).encode("utf-8") + b"\n\n")
                f.write(b"data: [DONE]\n\n")
                journal(hote=hote, chemin=requete.split()[1] if " " in requete else requete, modele=corps.get("model"), cle=cle,
                        flux=bool(corps.get("stream")))
            else:
                modele = requete.split()[1].split("/models/")[1].split(":")[0]
                prompt = corps["contents"][0]["parts"][0]["text"]
                texte = fa.texte_simule(sim, prompt, modele, args.fiche_factice)
                servi = modele + "-autre" if (args.controle_modele_faux and "seulement par le mot OK" in prompt) else modele
                mt = int((corps.get("generationConfig") or {}).get("maxOutputTokens") or 1000)
                rep = {"candidates": [{"content": {"parts": [{"text": texte}], "role": "model"}, "finishReason": "STOP"}],
                       "usageMetadata": {"promptTokenCount": max(1, len(prompt) // 4),
                                         "candidatesTokenCount": min(mt - 20, len(texte) // 3 + 20), "thoughtsTokenCount": 10},
                       "modelVersion": servi, "responseId": "repetition"}
                octets = json.dumps(rep, ensure_ascii=False).encode("utf-8")
                f.write(b"HTTP/1.1 200 OK\r\nContent-Type: application/json\r\nConnection: close\r\nContent-Length: "
                        + str(len(octets)).encode() + b"\r\n\r\n" + octets)
                journal(hote=hote, chemin=requete.split()[1] if " " in requete else requete, modele=modele, cle=cle)
            f.flush()
            try:
                tls.unwrap()
            except (ssl.SSLError, OSError):
                pass

    ThreadingTCPServer.allow_reuse_address = True
    ThreadingTCPServer.daemon_threads = True
    serveur = ThreadingTCPServer(("127.0.0.1", 0), Gestion)
    with open(args.port_fichier, "w", encoding="utf-8") as f:
        f.write(str(serveur.server_address[1]))
    print(f"faux mandataire TLS prêt sur 127.0.0.1:{serveur.server_address[1]}", flush=True)
    try:
        serveur.serve_forever()
    except KeyboardInterrupt:
        pass
    return 0


if __name__ == "__main__":
    _ = socket
    sys.exit(principal())
