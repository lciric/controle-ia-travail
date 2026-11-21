"""Faux fournisseur local pour les essais d'admission du bras A (Mistral en flux, Google sans flux) — version 8.

Devis : `docs/notes/relance-organismes-discrets-v1/devis-essais-admission-mistral-neon-bras-a-v1.md`
(`421ee2e6ec909c8b6261b3be39109aa5e76d6c275e79b4d7ec122816c83dd1bc`), section 10 et section 12, point 10.

Un serveur sur `127.0.0.1` seulement, dans un fil du processus d'essai. Il n'appelle personne. On lui **programme**
des réponses, servies dans l'ordre aux appels au modèle (`POST`) ; l'appel de liste (`GET`) rend `self.liste`.
Il garde ce qu'il a reçu (`recus`) et compte les connexions que le client a fermées en plein flux
(`fermees_par_le_client`), pour les gardes 1, 19 et « aucune reprise cachée ».

Réponses programmables (dictionnaires, fabriqués par les fonctions ci-dessous) :
- `json` : un code, un corps, des en-têtes, une attente avant de répondre (réponse sans flux, erreur, liste) ;
- `flux` : une suite d'événements `data:` (objets, `"[DONE]"`), de pauses `("pause", secondes)` et d'octets bruts ;
- `fermer` : la connexion est fermée sans réponse (connexion coupée en route) ;
- `muet` : la connexion reste ouverte sans un octet pendant une durée, puis se ferme.

`FauxMandataire` : un mandataire qui refuse toute demande de tunnel (code 403), pour la signature du devis (4.4).
Avec `repond=False`, il ferme la demande de tunnel sans répondre : une connexion non établie **hors** de la signature.
"""
from __future__ import annotations

import json
import socket
import threading
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

MISTRAL = "mistral-large-4-0"
NEON = "gemini-4-neon"


# --- fabriques de réponses ----------------------------------------------------------------------------------------------

def rep_json(code: int = 200, corps=None, en_tetes: dict | None = None, attente_s: float = 0.0) -> dict:
    return {"genre": "json", "code": code, "corps": {} if corps is None else corps, "en_tetes": en_tetes or {},
            "attente_s": attente_s}


def fermer() -> dict:
    return {"genre": "fermer"}


def muet(duree_s: float) -> dict:
    return {"genre": "muet", "duree_s": duree_s}


def _evenement(modele, delta=None, fin=None, usage=None) -> dict:
    o = {"id": "cmpl-faux", "object": "chat.completion.chunk"}
    if modele is not None:
        o["model"] = modele
    if delta is not None or fin is not None:
        o["choices"] = [{"index": 0, "delta": delta if delta is not None else {}, "finish_reason": fin}]
    if usage is not None:
        o["usage"] = usage
    return o


def flux_mistral(texte: str = '{"ok": true}', modele: str | None = MISTRAL, pensee: str | None = None,
                 usage=(40, 12, 52), fin: str | None = "stop", dernier_sans_modele: bool = True,
                 remplissage_octets: int = 0, sans_usage: bool = False, sans_total: bool = False,
                 sans_done: bool = False, autre_nom_au_dernier: str | None = None, type_pensee: str = "thinking",
                 sans_morceau_texte: bool = False, pause_entre_s: float = 0.0, contenu_en_chaine: bool = False,
                 sans_fin: bool = False) -> dict:
    """Flux de Mistral : un morceau de pensée (s'il y en a un), des morceaux `text`, la fin, puis un dernier événement
    qui ne porte que `usage` (sans champ `model` par défaut : devis, 4.3), puis `[DONE]`."""
    evenements = []
    if pensee is not None:
        evenements.append(_evenement(modele, {"content": [
            {"type": type_pensee, "thinking": [{"type": "text", "text": pensee}]}]}))
    reste = remplissage_octets
    while reste > 0:
        n = min(4096, reste)
        evenements.append(_evenement(modele, {"content": [{"type": "text", "text": "x" * n}]}))
        reste -= n
    if not sans_morceau_texte:
        evenements.append(_evenement(modele, {"content": texte if contenu_en_chaine else [{"type": "text", "text": texte}]}))
    if not sans_fin:
        evenements.append(_evenement(autre_nom_au_dernier or modele, {}, fin))
    if not sans_usage:
        u = {"prompt_tokens": usage[0], "completion_tokens": usage[1], "total_tokens": usage[2]}
        if sans_total:
            del u["total_tokens"]
        evenements.append(_evenement(None if dernier_sans_modele else modele, usage=u))
    suite = []
    for e in evenements:
        suite.append(e)
        if pause_entre_s:
            suite.append(("pause", pause_entre_s))
    if not sans_done:
        suite.append("[DONE]")
    return {"genre": "flux", "code": 200, "evenements": suite}


def flux_sans_fin(octets_par_morceau: int = 4096, pause_s: float = 0.0, modele: str = MISTRAL,
                  morceaux: int = 100000) -> dict:
    """Flux qui rend du contenu sans s'arrêter (pour la borne en octets), ou lentement (pour les délais)."""
    e = _evenement(modele, {"content": [{"type": "text", "text": "y" * octets_par_morceau}]})
    suite = []
    for _ in range(morceaux):
        suite.append(e)
        if pause_s:
            suite.append(("pause", pause_s))
    return {"genre": "flux", "code": 200, "evenements": suite}


def reponse_google(texte: str | None = '{"ok": true}', modele: str | None = NEON, usage=(30, 10, 5, 45),
                   fin: str | None = "STOP", attente_s: float = 0.0, sans_usage: bool = False,
                   sans_pensees: bool = False, blocage: str | None = None, avec_part_de_pensee: bool = False) -> dict:
    """Réponse de `generateContent`. `usage` : entrée, réponse seule, réflexion, total."""
    corps = {}
    if blocage is not None:
        corps["promptFeedback"] = {"blockReason": blocage}
    else:
        parts = []
        if avec_part_de_pensee:
            parts.append({"text": "réflexion du modèle, à écarter du texte jugé", "thought": True})
        if texte is not None:
            parts.append({"text": texte})
        candidat = {"content": {"role": "model", "parts": parts}, "index": 0}
        if fin is not None:
            candidat["finishReason"] = fin
        corps["candidates"] = [candidat]
    if modele is not None:
        corps["modelVersion"] = modele
    if not sans_usage:
        u = {"promptTokenCount": usage[0], "candidatesTokenCount": usage[1], "thoughtsTokenCount": usage[2],
             "totalTokenCount": usage[3]}
        if sans_pensees:
            del u["thoughtsTokenCount"]
        corps["usageMetadata"] = u
    return rep_json(200, corps, attente_s=attente_s)


def liste_mistral(identifiants=(MISTRAL,), forme: str = "objet", code: int = 200) -> dict:
    """L'appel de liste de Mistral, dans ses deux formes relevées : objet à champ `data`, ou tableau nu."""
    entrees = [{"id": i, "object": "model", "aliases": ["mistral-large-latest"]} for i in identifiants]
    if forme == "objet":
        return rep_json(code, {"object": "list", "data": entrees})
    if forme == "tableau":
        return rep_json(code, entrees)
    return rep_json(code, {"modeles": "forme illisible"})


def modele_google(identifiant: str = NEON, limite_sortie: int | None = 65536, code: int = 200) -> dict:
    corps = {"name": f"models/{identifiant}", "displayName": "faux"}
    if limite_sortie is not None:
        corps["outputTokenLimit"] = limite_sortie
    return rep_json(code, corps)


def erreur_mistral(code: int, type_: str | None = None, message: str | None = None, param: str | None = None,
                   detail=None, code_interne=None, en_tetes: dict | None = None) -> dict:
    corps = {"object": "error"}
    for k, v in (("type", type_), ("message", message), ("param", param), ("detail", detail), ("code", code_interne)):
        if v is not None:
            corps[k] = v
    return rep_json(code, corps, en_tetes)


def erreur_google(code: int, message: str = "erreur", champs=()) -> dict:
    erreur = {"code": code, "message": message, "status": "INVALID_ARGUMENT"}
    if champs:
        erreur["details"] = [{"@type": "type.googleapis.com/google.rpc.BadRequest",
                              "fieldViolations": [{"field": c, "description": "invalide"} for c in champs]}]
    return rep_json(code, {"error": erreur})


# --- le serveur ---------------------------------------------------------------------------------------------------------

class FauxFournisseur:
    def __init__(self, liste: dict | None = None):
        self.programme: list = []
        self.liste = liste if liste is not None else liste_mistral()
        self.recus: list = []
        self.fermees_par_le_client = 0
        self.imprevus = 0
        self.verrou = threading.Lock()
        faux = self

        class Gestionnaire(BaseHTTPRequestHandler):
            protocol_version = "HTTP/1.0"

            def log_message(self, format, *args):  # noqa: A002
                return

            def _noter(self, corps: bytes) -> None:
                with faux.verrou:
                    faux.recus.append({"methode": self.command, "chemin": self.path, "corps": corps,
                                       "en_tetes": {k.lower(): v for k, v in self.headers.items()}})

            def _servir(self, r: dict) -> None:
                genre = r["genre"]
                if genre == "fermer":
                    self.connection.shutdown(socket.SHUT_RDWR)
                    return
                if genre == "muet":
                    fin = time.monotonic() + r["duree_s"]
                    while time.monotonic() < fin:
                        time.sleep(0.02)
                    return
                if genre == "json":
                    if r["attente_s"]:
                        time.sleep(r["attente_s"])
                    corps = r["corps"] if isinstance(r["corps"], bytes) else json.dumps(r["corps"]).encode("utf-8")
                    try:
                        self.send_response(r["code"])
                        self.send_header("Content-Type", "application/json")
                        self.send_header("Content-Length", str(len(corps)))
                        for k, v in r["en_tetes"].items():
                            self.send_header(k, v)
                        self.end_headers()
                        self.wfile.write(corps)
                    except OSError:
                        with faux.verrou:
                            faux.fermees_par_le_client += 1
                    return
                try:
                    self.send_response(r["code"])
                    self.send_header("Content-Type", "text/event-stream")
                    self.end_headers()
                    for e in r["evenements"]:
                        if isinstance(e, tuple) and e[0] == "pause":
                            time.sleep(e[1])
                            continue
                        if isinstance(e, bytes):
                            self.wfile.write(e)
                        elif e == "[DONE]":
                            self.wfile.write(b"data: [DONE]\n\n")
                        else:
                            self.wfile.write(b"data: " + json.dumps(e).encode("utf-8") + b"\n\n")
                        self.wfile.flush()
                except OSError:
                    with faux.verrou:
                        faux.fermees_par_le_client += 1

            def do_GET(self):
                self._noter(b"")
                self._servir(faux.liste)

            def do_POST(self):
                corps = self.rfile.read(int(self.headers.get("Content-Length") or 0))
                self._noter(corps)
                with faux.verrou:
                    r = faux.programme.pop(0) if faux.programme else None
                    if r is None:
                        faux.imprevus += 1
                self._servir(r if r is not None else rep_json(599, {"faux": "aucune réponse programmée"}))

        self.serveur = ThreadingHTTPServer(("127.0.0.1", 0), Gestionnaire)
        self.serveur.daemon_threads = True
        self.fil = threading.Thread(target=self.serveur.serve_forever, daemon=True)

    @property
    def url(self) -> str:
        return f"http://127.0.0.1:{self.serveur.server_address[1]}"

    def programmer(self, *reponses) -> "FauxFournisseur":
        with self.verrou:
            self.programme.extend(reponses)
        return self

    def appels(self) -> list:
        """Les appels au modèle reçus (`POST`), dans l'ordre."""
        with self.verrou:
            return [r for r in self.recus if r["methode"] == "POST"]

    def demarrer(self) -> "FauxFournisseur":
        self.fil.start()
        return self

    def arreter(self) -> None:
        self.serveur.shutdown()
        self.serveur.server_close()


class FauxMandataire:
    """Mandataire local qui refuse toute demande de tunnel (code 403), sans rien relayer."""

    def __init__(self, repond: bool = True):
        self.repond = repond
        self.prise = socket.socket()
        self.prise.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.prise.bind(("127.0.0.1", 0))
        self.prise.listen(8)
        self.demandes = 0
        self.vivant = True
        self.fil = threading.Thread(target=self._tourner, daemon=True)

    @property
    def url(self) -> str:
        return f"http://127.0.0.1:{self.prise.getsockname()[1]}"

    def _tourner(self) -> None:
        while self.vivant:
            try:
                client, _ = self.prise.accept()
            except OSError:
                return
            with client:
                try:
                    client.settimeout(2)
                    client.recv(4096)
                    self.demandes += 1
                    if self.repond:
                        client.sendall(b"HTTP/1.1 403 Forbidden\r\nContent-Length: 0\r\n\r\n")
                except OSError:
                    pass

    def demarrer(self) -> "FauxMandataire":
        self.fil.start()
        return self

    def arreter(self) -> None:
        self.vivant = False
        self.prise.close()


def port_ferme() -> int:
    """Un port de la boucle locale où personne n'écoute (connexion refusée)."""
    s = socket.socket()
    s.bind(("127.0.0.1", 0))
    port = s.getsockname()[1]
    s.close()
    return port
