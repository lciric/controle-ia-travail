#!/usr/bin/env python3
"""Faux serveur Kimi local (http.server sur 127.0.0.1, port libre) pour éprouver `transport_kimi_reel_v2` — v2
(la v1 plus : `usage_intermediaire`, `deux_usages`, `ignore_max_tokens`, `en_tete_id`).
Bibliothèque standard seule ; aucun réseau sortant. Il **compte** chaque requête reçue (toutes méthodes, tous chemins) et
tient **sa propre facture** (2 / 10 USD par million par défaut, prix gelés du pilote) : ce qu'un fournisseur facturerait,
y compris ce qu'il ne rendrait pas dans `usage` (réflexion cachée, requête coupée facturée).

Comportement par requête : `regle(k, corps)` rend un dict (k = rang de la requête, corps = JSON reçu). Clés reconnues :
- `statut` (200), `corps_erreur` (dict) ; `facture` : (entrée, sortie) facturés, sinon tirés de l'usage rendu (200 seulement) ;
- `modele` (modèle servi, défaut : celui demandé), `modele_apres` (modèle d'un morceau suivant) ;
- `prompt`, `completion`, `raisonnement` (dans `completion_tokens_details`, compris dans `completion`),
  `reflexion_hors` (au premier niveau, hors de `completion`), `detail_hors` (détail > completion), `cache_lu` ;
  `total_en_plus` (excédent de `total_tokens`) ; `usage` (remplace tout) ou `usage_absent` ; `usage_dans_choix` ;
- `coupure_apres` (n morceaux, puis fermeture brutale, sans [DONE]) ; `sans_done` ; `attente_s` (avant l'en-tête) ;
  `maintien` (n commentaires « : » espacés de `pas_s`) ; `non_flux` ; `evenement_erreur` ; `remplissage` (octets de contenu) ;
  `fermer_sans_reponse` ; `reflexion_texte` (octets de réflexion rendus en texte) ;
- v2 : `usage_intermediaire` (l'usage part dans un morceau de contenu, puis du contenu suit), `deux_usages` (usage d'abord
  grand, puis le vrai), `ignore_max_tokens` (n morceaux de contenu, quel que soit `max_tokens`), `en_tete_id` (valeur d'un
  en-tête `x-request-id`), `ident` (identifiant des morceaux).
"""
import json
import math
import socket
import threading
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer


def defaut(k, corps):
    return {}


class FauxServeurKimi:
    def __init__(self, regle=defaut, prix=(2.0, 10.0)):
        self.regle, self.prix = regle, prix
        self.requetes = []        # (méthode, chemin, en-têtes, corps)
        self.facture_usd = 0.0
        self.verrou = threading.Lock()
        serveur = self

        class Gestionnaire(BaseHTTPRequestHandler):
            protocol_version = "HTTP/1.1"

            def log_message(self, *a):
                pass

            def do_GET(self):
                self._noter(b"")
                self.send_error(404)

            def do_POST(self):
                n = int(self.headers.get("Content-Length") or 0)
                brut = self.rfile.read(n)
                k = self._noter(brut)
                try:
                    corps = json.loads(brut)
                except ValueError:
                    corps = {}
                serveur._servir(self, k, corps, len(brut))

            def _noter(self, brut):
                with serveur.verrou:
                    serveur.requetes.append((self.command, self.path, dict(self.headers), brut))
                    return len(serveur.requetes) - 1

        self.httpd = ThreadingHTTPServer(("127.0.0.1", 0), Gestionnaire)
        self.httpd.daemon_threads = True
        self.url = f"http://127.0.0.1:{self.httpd.server_address[1]}"
        self.fil = threading.Thread(target=self.httpd.serve_forever, daemon=True)

    def __enter__(self):
        self.fil.start()
        return self

    def __exit__(self, *a):
        self.httpd.shutdown()
        self.httpd.server_close()

    @property
    def nombre(self):
        return len(self.requetes)

    def facturer(self, e, s):
        with self.verrou:
            self.facture_usd += (e * self.prix[0] + s * self.prix[1]) / 1e6

    # --- service -------------------------------------------------------------------------------------------------
    def _servir(self, h, k, corps, octets):
        r = dict(self.regle(k, corps) or {})
        demande = corps.get("model")
        mt = corps.get("max_tokens") or 0
        texte = ((corps.get("messages") or [{}])[0] or {}).get("content", "") or ""
        if r.get("fermer_sans_reponse"):
            if "facture" in r:
                self.facturer(*r["facture"])
            h.connection.shutdown(socket.SHUT_RDWR)
            h.close_connection = True
            return
        if r.get("attente_s"):
            time.sleep(r["attente_s"])
        statut = r.get("statut", 200)
        if statut != 200:
            if "facture" in r:
                self.facturer(*r["facture"])
            b = json.dumps(r.get("corps_erreur", {"error": {"type": "faux", "code": statut}})).encode()
            h.send_response(statut)
            h.send_header("Content-Type", "application/json")
            h.send_header("Content-Length", str(len(b)))
            h.send_header("Connection", "close")
            h.end_headers()
            h.wfile.write(b)
            h.close_connection = True
            return
        p = r.get("prompt", math.ceil(len(texte.encode()) / 3.3) + 12)
        c = r.get("completion", min(mt, 300))
        rais = r.get("raisonnement", min(c, c * 2 // 3))
        usage = {"prompt_tokens": p, "completion_tokens": c, "total_tokens": p + c,
                 "completion_tokens_details": {"reasoning_tokens": rais}, "prompt_tokens_details": {"cache_write_tokens": 0}}
        if r.get("reflexion_hors"):
            usage["reasoning_tokens"] = r["reflexion_hors"]
            usage["total_tokens"] += r["reflexion_hors"]
        if r.get("detail_hors"):
            usage["completion_tokens_details"]["reasoning_tokens"] = c + r["detail_hors"]
            usage["total_tokens"] += r["detail_hors"]
        if r.get("total_en_plus"):
            usage["total_tokens"] += r["total_en_plus"]
        if r.get("cache_lu"):
            usage["prompt_tokens_details"]["cached_tokens"] = r["cache_lu"]
        if "usage" in r:
            usage = r["usage"]
        if r.get("usage_absent"):
            usage = None
        # facture : ce que le fournisseur compterait (réflexion cachée et excédent compris)
        if "facture" in r:
            self.facturer(*r["facture"])
        else:
            cache = r.get("cache_lu", 0)
            fe = (p - cache) * self.prix[0] + cache * self.prix[0] / 10
            fs = (c + r.get("reflexion_hors", 0) + r.get("detail_hors", 0) + r.get("total_en_plus", 0)) * self.prix[1]
            with self.verrou:
                self.facture_usd += (fe + fs) / 1e6
        if r.get("non_flux"):
            b = json.dumps({"model": r.get("modele", demande), "choices": [{"message": {"content": "x"}, "finish_reason": "stop"}],
                            "usage": usage}).encode()
            h.send_response(200)
            h.send_header("Content-Type", "application/json")
            h.send_header("Content-Length", str(len(b)))
            h.end_headers()
            h.wfile.write(b)
            return
        h.send_response(200)
        h.send_header("Content-Type", "text/event-stream")
        if r.get("en_tete_id"):
            h.send_header("x-request-id", r["en_tete_id"])
        h.send_header("Transfer-Encoding", "chunked")
        h.send_header("Connection", "close")
        h.end_headers()
        h.close_connection = True

        def envoyer(octets_):
            h.wfile.write(b"%x\r\n" % len(octets_) + octets_ + b"\r\n")
            h.wfile.flush()

        def ev(obj):
            envoyer(b"data: " + json.dumps(obj).encode() + b"\n\n")

        modele = r.get("modele", demande)
        base = {"id": r.get("ident", "chatcmpl-faux"), "object": "chat.completion.chunk", "created": 0}
        morceaux = [{"choices": [{"index": 0, "delta": {"role": "assistant",
                                                         "reasoning_content": "r" * r["reflexion_texte"] if r.get("reflexion_texte") else "je réfléchis"}}]},
                    {"choices": [{"index": 0, "delta": {"content": "OK"}}]}]
        if r.get("remplissage"):
            morceaux.append({"choices": [{"index": 0, "delta": {"content": "y" * r["remplissage"]}}]})
        for i in range(r.get("ignore_max_tokens", 0)):
            morceaux.append({"choices": [{"index": 0, "delta": {"content": "abcd "}}]})
        if r.get("usage_intermediaire"):
            morceaux.insert(1, dict(morceaux[1], usage=usage))
            morceaux.insert(2, {"choices": [{"index": 0, "delta": {"content": "suite " * 20}}]})
        morceaux.append({"choices": [{"index": 0, "delta": {}, "finish_reason": "length" if c >= mt else "stop"}]})
        try:
            for i in range(r.get("maintien", 0)):
                envoyer(b": maintien\n\n")
                time.sleep(r.get("pas_s", 0.1))
            for i, m in enumerate(morceaux):
                if r.get("coupure_apres") is not None and i >= r["coupure_apres"]:
                    h.wfile.flush()
                    h.connection.shutdown(socket.SHUT_RDWR)
                    return
                if r.get("evenement_erreur") and i == 1:
                    ev({"error": {"type": "server_error", "message": "faux"}})
                    break
                mod = modele if i == 0 else r.get("modele_apres", modele)
                ev(dict(base, model=mod, **m))
            if usage is not None or not r.get("usage_absent"):
                if r.get("deux_usages"):
                    grand = dict(usage, completion_tokens=usage["completion_tokens"] + 1900,
                                 total_tokens=usage["total_tokens"] + 1900)
                    ev(dict(base, model=modele, choices=[], usage=grand))
                if r.get("usage_intermediaire"):
                    pass
                elif r.get("usage_dans_choix"):
                    ev(dict(base, model=modele, choices=[{"index": 0, "delta": {}, "usage": usage}]))
                elif usage is not None:
                    ev(dict(base, model=modele, choices=[], usage=usage))
            if r.get("coupure_apres") is not None:  # au-delà des morceaux : coupure après l'usage, avant [DONE]
                h.wfile.flush()
                h.connection.shutdown(socket.SHUT_RDWR)
                return
            if not r.get("sans_done"):
                envoyer(b"data: [DONE]\n\n")
            envoyer(b"")
        except (BrokenPipeError, ConnectionResetError):
            pass
