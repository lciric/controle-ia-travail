"""Véhicule NA-1, lot 4 — faux fournisseur (`faux_fournisseur_na_v1`) : un serveur local qui joue l'interface des messages
derrière le relais (ou à sa place), garde ce qu'il reçoit, et rend à la demande une réponse normale, un refus pour crédit,
une erreur d'accès, un refus de classifieur ou une réponse coupée. Aucun modèle, aucun réseau, aucune clé.

Lettre : conception du véhicule v5 (`1b7f6822…`), § 2.12 (faux fournisseur : code neuf ; un amont local derrière les vrais
relais), § 2.3 et § 7 (relevé, au faux fournisseur, de ce que l'outil envoie sans texte système) ; relevé du lot 0
(`10ac79ec…`), Q7 (aucun faux fournisseur dans l'essai à blanc de L9 ; modèle : l'amont factice des essais du relais).

- N'écoute que sur `127.0.0.1` ; tout autre hôte est refusé à la construction.
- Garde chaque requête : méthode, chemin, noms et valeurs des en-têtes (sauf ceux qui portent une clé ou un jeton : leur
  seule présence), taille et empreinte du corps, et le corps lu comme JSON s'il l'est. Les octets du corps ne sortent que
  par cet objet, ou par le journal de requêtes si un chemin est donné (JSON par ligne, fichier neuf, ajout seul).
- Le mode de réponse s'applique à toute requête de messages tant qu'il n'est pas changé : `normale`, `classifieur`
  (`stop_reason` « refusal »), `coupee` (`stop_reason` « max_tokens »), `credit` (statut 400, erreur de crédit),
  `acces` (statut 401, erreur d'authentification). Le texte rendu est inerte (`TEXTE_INERTE`) ; le modèle rendu est celui
  que le corps demande.
- `…/count_tokens` rend un compte fixe ; tout autre chemin : 404, gardé comme les autres.
"""

import hashlib
import json
import os
import threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

VERSION = "faux-fournisseur-na-v1"
HOTE = "127.0.0.1"
MODES = ("normale", "classifieur", "coupee", "credit", "acces")
TEXTE_INERTE = "Réponse factice inerte du faux fournisseur : elle ne répond à rien."
EN_TETES_SECRETS = ("x-api-key", "authorization", "proxy-authorization", "cookie")
USAGE = {"input_tokens": 12, "output_tokens": 7}
MESSAGES_ERREUR = {
    "credit": (400, "invalid_request_error", "Your credit balance is too low to access the API (faux fournisseur)."),
    "acces": (401, "authentication_error", "invalid api key (faux fournisseur)"),
}


class FauxFournisseurRefuse(ValueError):
    pass


def _stop_reason(mode):
    return {"classifieur": "refusal", "coupee": "max_tokens"}.get(mode, "end_turn")


class FauxFournisseur:
    def __init__(self, port=0, journal=None, mode="normale", hote=HOTE):
        if hote != HOTE:
            raise FauxFournisseurRefuse("le faux fournisseur n'écoute que sur 127.0.0.1")
        if mode not in MODES:
            raise FauxFournisseurRefuse(f"mode inconnu ; modes : {MODES}")
        if journal is not None:
            if os.path.exists(journal):
                raise FauxFournisseurRefuse("journal de requêtes existant : on n'écrase jamais (R12)")
            with open(journal, "x", encoding="utf-8"):
                pass
        self.journal = journal
        self.mode = mode
        self.requetes = []
        self._verrou = threading.Lock()
        faux = self

        class Gestionnaire(BaseHTTPRequestHandler):
            protocol_version = "HTTP/1.1"
            server_version = "FauxFournisseurNA/1"

            def log_message(self, *args):
                pass

            def _envoyer(self, statut, objet):
                corps = json.dumps(objet, ensure_ascii=False).encode("utf-8")
                self.send_response(statut)
                self.send_header("Content-Type", "application/json")
                self.send_header("Content-Length", str(len(corps)))
                self.end_headers()
                self.wfile.write(corps)

            def _garder(self, methode):
                longueur = int(self.headers.get("content-length") or 0)
                brut = self.rfile.read(longueur) if longueur else b""
                try:
                    corps = json.loads(brut.decode("utf-8")) if brut else None
                except (UnicodeDecodeError, ValueError):
                    corps = None
                en_tetes = {k.lower(): ("présent" if k.lower() in EN_TETES_SECRETS else v) for k, v in self.headers.items()}
                with faux._verrou:
                    entree = {"rang": len(faux.requetes) + 1, "methode": methode, "chemin": self.path, "en_tetes": en_tetes,
                              "corps_taille": len(brut), "corps_sha256": hashlib.sha256(brut).hexdigest(), "corps": corps,
                              "mode": faux.mode}
                    faux.requetes.append(entree)
                    if faux.journal is not None:
                        with open(faux.journal, "a", encoding="utf-8") as f:
                            f.write(json.dumps(entree, ensure_ascii=False, sort_keys=True) + "\n")
                return entree

            def do_GET(self):
                self._garder("GET")
                self._envoyer(404, {"type": "error", "error": {"type": "not_found_error", "message": "faux fournisseur"}})

            def do_POST(self):
                entree = self._garder("POST")
                chemin = self.path.split("?", 1)[0]
                corps = entree["corps"] if isinstance(entree["corps"], dict) else {}
                if chemin.endswith("/count_tokens"):
                    return self._envoyer(200, {"input_tokens": USAGE["input_tokens"]})
                if not chemin.endswith("/v1/messages"):
                    return self._envoyer(404, {"type": "error", "error": {"type": "not_found_error",
                                                                          "message": "faux fournisseur"}})
                mode = entree["mode"]
                if mode in MESSAGES_ERREUR:
                    statut, genre, message = MESSAGES_ERREUR[mode]
                    return self._envoyer(statut, {"type": "error", "error": {"type": genre, "message": message}})
                modele = corps.get("model") or "inconnu"
                stop = _stop_reason(mode)
                texte = "" if mode == "classifieur" else TEXTE_INERTE
                if corps.get("stream"):
                    return self._flux(modele, stop, texte)
                return self._envoyer(200, {"id": "msg_faux", "type": "message", "role": "assistant", "model": modele,
                                           "content": [{"type": "text", "text": texte}] if texte else [],
                                           "stop_reason": stop, "stop_sequence": None, "usage": dict(USAGE)})

            def _flux(self, modele, stop, texte):
                evenements = [
                    {"type": "message_start", "message": {"id": "msg_faux", "type": "message", "role": "assistant",
                                                          "model": modele, "content": [], "stop_reason": None,
                                                          "stop_sequence": None,
                                                          "usage": {"input_tokens": USAGE["input_tokens"], "output_tokens": 1}}},
                ]
                if texte:
                    evenements += [
                        {"type": "content_block_start", "index": 0, "content_block": {"type": "text", "text": ""}},
                        {"type": "content_block_delta", "index": 0, "delta": {"type": "text_delta", "text": texte}},
                        {"type": "content_block_stop", "index": 0},
                    ]
                evenements += [
                    {"type": "message_delta", "delta": {"stop_reason": stop, "stop_sequence": None},
                     "usage": {"output_tokens": USAGE["output_tokens"]}},
                    {"type": "message_stop"},
                ]
                self.send_response(200)
                self.send_header("Content-Type", "text/event-stream")
                self.send_header("Cache-Control", "no-cache")
                self.send_header("Transfer-Encoding", "chunked")
                self.end_headers()
                for e in evenements:
                    morceau = f"event: {e['type']}\ndata: {json.dumps(e, ensure_ascii=False)}\n\n".encode("utf-8")
                    self.wfile.write(b"%x\r\n%s\r\n" % (len(morceau), morceau))
                    self.wfile.flush()
                self.wfile.write(b"0\r\n\r\n")
                self.wfile.flush()

        self.serveur = ThreadingHTTPServer((hote, port), Gestionnaire)
        self.serveur.daemon_threads = True
        self.url = f"http://{hote}:{self.serveur.server_address[1]}"
        self._fil = None

    def demarrer(self):
        self._fil = threading.Thread(target=self.serveur.serve_forever, daemon=True)
        self._fil.start()
        return self

    def changer_mode(self, mode):
        if mode not in MODES:
            raise FauxFournisseurRefuse(f"mode inconnu ; modes : {MODES}")
        with self._verrou:
            self.mode = mode

    def servir_jusqu_a(self, duree_s):
        """Sert dans le fil courant pendant `duree_s` secondes au plus, puis s'arrête de lui-même."""
        minuteur = threading.Timer(float(duree_s), self.serveur.shutdown)
        minuteur.daemon = True
        minuteur.start()
        try:
            self.serveur.serve_forever()
        finally:
            minuteur.cancel()
            self.serveur.server_close()

    def fermer(self):
        if self._fil is not None:
            self.serveur.shutdown()
            self._fil.join(timeout=10)
        self.serveur.server_close()


def lire_journal(chemin):
    """Les requêtes gardées dans un journal de requêtes, dans l'ordre."""
    with open(chemin, encoding="utf-8") as f:
        return [json.loads(l) for l in f if l.strip()]


__all__ = ("FauxFournisseur", "FauxFournisseurRefuse", "lire_journal", "MODES", "TEXTE_INERTE")
