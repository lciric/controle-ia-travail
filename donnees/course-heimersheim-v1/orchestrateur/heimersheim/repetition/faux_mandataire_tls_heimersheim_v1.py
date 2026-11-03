#!/usr/bin/env python3
"""Faux mandataire TLS de la répétition de la course Heimersheim (aucun réseau, aucune clé réelle, aucune dépense) — v1.

Rédigé le 3 novembre 2026 (sous-agent de session-depot), sur le modèle de `nuit/repetition/faux_mandataire_tls_v1.py` (inchangé)
de la mini-course. Les VRAIS relais (`commande_claude_a1bis_v1.py servir` par le SDK `anthropic`, `commande_astra_a1bis_v1.py
servir` par `collisionneur_v8.appeler_openai`, `relais_kimi_v3.py`, `commande_argon_v56_nuit_v2.py servir` par
`collisionneur_v7.appeler_gemini`) passent par `HTTPS_PROXY` = ce mandataire, qui accepte `CONNECT hôte:443` pour les quatre
hôtes, termine le TLS avec un certificat signé par l'**autorité factice** de répétition (que seul `SSL_CERT_FILE` de la
répétition reconnaît) et répond au format de chaque interface (Anthropic : flux SSE des messages ; OpenAI : chat completion
JSON ; Moonshot : flux SSE ; Gemini : JSON) avec le moteur simulé v56 de l'orchestrateur (8 fiches par proposeur). Tout autre
hôte, toute autre méthode : refus 403.

Options : `--pause-s` (attente avant chaque réponse : essai du `kill` en pleine course) ; `--controle-modele-faux MODELE`
(artefact : la réponse au contrôle d'avant course de ce modèle porte un autre modèle servi). Journal : hôte, chemin, modèle,
présence d'une clé (booléen), jamais de texte.
"""

import argparse
import json
import os
import ssl
import sys
import threading
import time
from socketserver import StreamRequestHandler, ThreadingTCPServer

ICI = os.path.dirname(os.path.abspath(__file__))
H = os.path.dirname(ICI)
sys.path.insert(0, os.path.dirname(H))
from pole.simulation_v56 import AdaptateurSimuleV56  # noqa: E402

HOTES = ("api.anthropic.com", "api.openai.com", "api.moonshot.ai", "generativelanguage.googleapis.com")
with open(os.path.join(H, "configuration-course-heimersheim-v1-avec-kimi.json"), encoding="utf-8") as _f:
    CONF = json.load(_f)


def simulateur():
    return AdaptateurSimuleV56(champs_fiche=CONF["champs_fiche"], items=CONF["items_juge"], champ_titre=CONF["champ_titre"],
                               cout_par_appel_usd=0.01, fiches_par_appel=8)


def texte_simule(sim, verrou, prompt, modele):
    if "seulement par le mot OK" in prompt:
        return "OK"
    with verrou:
        t = sim.reponse("inconnu", prompt, modele)
    return "Réponse simulée.\n```json\n" + t + "\n```\n"


def principal(argv=None):
    a = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    a.add_argument("--certificat", required=True)
    a.add_argument("--cle", required=True)
    a.add_argument("--port-fichier", required=True)
    a.add_argument("--journal", required=True)
    a.add_argument("--pause-s", type=float, default=0.0)
    a.add_argument("--controle-modele-faux", default=None)
    args = a.parse_args(argv)
    ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    ctx.load_cert_chain(args.certificat, args.cle)
    sim, verrou_sim, verrou = simulateur(), threading.Lock(), threading.Lock()

    def journal(**e):
        with verrou, open(args.journal, "a", encoding="utf-8") as f:
            f.write(json.dumps(dict(e, quand=time.time()), ensure_ascii=False) + "\n")

    def servi(modele, prompt):
        if args.controle_modele_faux and modele == args.controle_modele_faux and "seulement par le mot OK" in prompt:
            return modele + "-autre"
        return modele

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
            cle = bool(entetes.get("authorization") or entetes.get("x-api-key") or entetes.get("x-goog-api-key"))
            if args.pause_s:
                time.sleep(args.pause_s)
            chemin = requete.split()[1] if " " in requete else requete
            if hote == "api.anthropic.com":
                prompt = corps["messages"][-1]["content"]
                prompt = prompt if isinstance(prompt, str) else json.dumps(prompt)
                texte = texte_simule(sim, verrou_sim, prompt, corps["model"])
                mt = int(corps.get("max_tokens") or 1000)
                sortie = min(mt - 1, len(texte) // 3 + 40)
                evts = [("message_start", {"type": "message_start", "message": {
                    "id": "msg_repetition", "type": "message", "role": "assistant", "model": servi(corps["model"], prompt), "content": [],
                    "stop_reason": None, "stop_sequence": None, "usage": {"input_tokens": max(1, len(prompt) // 4), "output_tokens": 1}}}),
                    ("content_block_start", {"type": "content_block_start", "index": 0, "content_block": {"type": "text", "text": ""}})]
                evts += [("content_block_delta", {"type": "content_block_delta", "index": 0, "delta": {"type": "text_delta", "text": texte[i:i + 400]}})
                         for i in range(0, len(texte), 400)]
                evts += [("content_block_stop", {"type": "content_block_stop", "index": 0}),
                         ("message_delta", {"type": "message_delta", "delta": {"stop_reason": "end_turn", "stop_sequence": None},
                                            "usage": {"output_tokens": sortie}}),
                         ("message_stop", {"type": "message_stop"})]
                f.write(b"HTTP/1.1 200 OK\r\nContent-Type: text/event-stream\r\nCache-Control: no-cache\r\nConnection: close\r\n"
                        b"request-id: req_repetition\r\n\r\n")
                for nom, d in evts:
                    f.write(f"event: {nom}\ndata: {json.dumps(d, ensure_ascii=False)}\n\n".encode("utf-8"))
                journal(hote=hote, chemin=chemin, modele=corps.get("model"), cle=cle, flux=bool(corps.get("stream")))
            elif hote == "api.openai.com":
                prompt = corps["messages"][-1]["content"]
                texte = texte_simule(sim, verrou_sim, prompt, corps["model"])
                mt = int(corps.get("max_completion_tokens") or 1000)
                rep = {"id": "chatcmpl-repetition", "object": "chat.completion", "model": servi(corps["model"], prompt),
                       "choices": [{"index": 0, "message": {"role": "assistant", "content": texte}, "finish_reason": "stop"}],
                       "usage": {"prompt_tokens": max(1, len(prompt) // 4), "completion_tokens": min(mt - 1, len(texte) // 3 + 60),
                                 "completion_tokens_details": {"reasoning_tokens": 20}}}
                octets = json.dumps(rep, ensure_ascii=False).encode("utf-8")
                f.write(b"HTTP/1.1 200 OK\r\nContent-Type: application/json\r\nConnection: close\r\nContent-Length: "
                        + str(len(octets)).encode() + b"\r\n\r\n" + octets)
                journal(hote=hote, chemin=chemin, modele=corps.get("model"), cle=cle)
            elif hote == "api.moonshot.ai":
                prompt = corps["messages"][-1]["content"]
                texte = texte_simule(sim, verrou_sim, prompt, corps["model"])
                usage = {"prompt_tokens": len(prompt.encode("utf-8")) // 4, "completion_tokens": len(texte) // 3 + 300}
                usage["total_tokens"] = usage["prompt_tokens"] + usage["completion_tokens"]
                morceaux = [{"choices": [{"index": 0, "delta": {"reasoning_content": "raisonnement simulé. "}}]}]
                morceaux += [{"choices": [{"index": 0, "delta": {"content": texte[i:i + 400]}}]} for i in range(0, len(texte), 400)]
                morceaux.append({"choices": [{"index": 0, "delta": {}, "finish_reason": "stop"}], "usage": usage})
                f.write(b"HTTP/1.1 200 OK\r\nContent-Type: text/event-stream\r\nConnection: close\r\n\r\n")
                for m in morceaux:
                    m.update(id="chatcmpl-repetition", object="chat.completion.chunk", model=servi(corps["model"], prompt))
                    f.write(b"data: " + json.dumps(m, ensure_ascii=False).encode("utf-8") + b"\n\n")
                f.write(b"data: [DONE]\n\n")
                journal(hote=hote, chemin=chemin, modele=corps.get("model"), cle=cle, flux=bool(corps.get("stream")))
            else:
                modele = chemin.split("/models/")[1].split(":")[0]
                prompt = corps["contents"][0]["parts"][0]["text"]
                texte = texte_simule(sim, verrou_sim, prompt, modele)
                mt = int((corps.get("generationConfig") or {}).get("maxOutputTokens") or 1000)
                rep = {"candidates": [{"content": {"parts": [{"text": texte}], "role": "model"}, "finishReason": "STOP"}],
                       "usageMetadata": {"promptTokenCount": max(1, len(prompt) // 4),
                                         "candidatesTokenCount": min(mt - 20, len(texte) // 3 + 20), "thoughtsTokenCount": 10},
                       "modelVersion": servi(modele, prompt), "responseId": "repetition"}
                octets = json.dumps(rep, ensure_ascii=False).encode("utf-8")
                f.write(b"HTTP/1.1 200 OK\r\nContent-Type: application/json\r\nConnection: close\r\nContent-Length: "
                        + str(len(octets)).encode() + b"\r\n\r\n" + octets)
                journal(hote=hote, chemin=chemin, modele=modele, cle=cle)
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
    sys.exit(principal())
