#!/usr/bin/env python3
"""Relais local de Google (`generateContent`, sans flux) pour les essais d'admission du bras A (juge des deux ancres)
— version 1.

Devis joué : `docs/notes/relance-organismes-discrets-v1/devis-essais-admission-mistral-neon-bras-a-v1.md`
(`421ee2e6ec909c8b6261b3be39109aa5e76d6c275e79b4d7ec122816c83dd1bc`), sections 4.4, 5.3, 5.5, 5.6, 6.4 et 12 (point 7).
Formes des appels : relevé `releve-api-mistral-gemini-essais-admission-v1.md` (non opposable).

Un petit serveur dans son propre processus, sur la boucle locale seulement. Le programme qui conduit les essais n'a
aucune clé : le relais tient la clé, l'amont fixe et la borne d'appels. **Il n'a pas de plafond en dollars** (devis,
6.4) : celui de la ligne est tenu par le programme, entre les envois ; pendant un envoi, rien ne le tient que le délai.

Ce qu'il sert, et rien d'autre (le modèle de la ligne est dans le chemin, à la lettre) :
- `GET /relais/etat` ;
- `GET /v1beta/models/<modèle>` : l'appel de liste, gratuit, relayé tel quel ; non compté parmi les appels ;
- `POST /v1beta/models/<modèle>:generateContent` : **sans flux**. Le corps part tel quel, octet pour octet : le relais
  ne touche ni à `thinkingLevel` ni à rien d'autre ; la réponse entière est rendue telle quelle (code et corps).

Clé : lue une seule fois dans la variable `--variable-cle`, effacée de `os.environ`, posée dans l'en-tête
`x-goog-api-key` ; jamais dans l'adresse, jamais journalisée. Toute clé reçue du client est retirée.

Amont : `--amont` vaut `generativelanguage.googleapis.com`, joint en `https`. `--adresse-d-essai
http://127.0.0.1:PORT` le remplace pour les essais sans réseau (boucle locale seulement) ; l'état le dit.

Signature du refus du mandataire (devis, 4.4, ligne 1) : code 502, origine `mandataire`, **seulement** si la connexion
vers l'amont n'a pas été établie avant tout octet de la requête — connexion refusée, ou tunnel refusé par le
mandataire — ; le journal porte alors `octets_envoyes_amont` à zéro. Toute autre panne porte l'origine `relais`.

Délai : `--delai-total-s`, un seul (2 690 secondes à la file, 890 à la vérification : dix secondes sous celui du
programme). Dépassé : code 502, origine `relais`, motif `delai_total` ; la connexion vers l'amont est fermée.
Connexion coupée par l'amont : code 502, origine `relais`, motif `coupure_amont`. Si le client ferme sa connexion,
le relais ferme celle de l'amont.

Journal (`--journal`) : heure, chemin, identifiant d'envoi (`X-Envoi`, non relayé), code, origine, motif, octets
envoyés à l'amont, octets reçus, durée — **jamais un texte, jamais la clé**.

Bibliothèque standard seulement. Essais : `tests/test_chef_essais_admission_bras_a_v1.py` (faux fournisseur local).
"""
from __future__ import annotations

import argparse
import base64
import datetime
import http.client
import json
import os
import socket
import ssl
import sys
import threading
import time
import urllib.parse
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

VERSION = "relais_google_essais_admission_v1"
HOTE = "127.0.0.1"
HOTES_LOCAUX = ("127.0.0.1", "localhost", "::1")
HOTES_PERMIS = ("generativelanguage.googleapis.com",)
CHEMIN_ETAT = "/relais/etat"
MAX_OCTETS_CORPS = 4_000_000
MAX_OCTETS_REPONSE = 50_000_000


class RelaisInvalide(Exception):
    """Réglage impossible : le relais ne démarre pas."""


class RefusMandataire(Exception):
    """Connexion vers l'amont non établie, avant tout octet de la requête, à la signature du devis (4.4)."""


class PanneConnexion(Exception):
    """Connexion vers l'amont non établie, hors de la signature du mandataire."""


def heure() -> str:
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def lire_cle(environnement, variable: str) -> str:
    cle = (environnement.get(variable) or "").strip()
    environnement.pop(variable, None)
    if not cle or any(c in cle for c in "\r\n"):
        raise RelaisInvalide(f"aucune clé lisible dans la variable {variable} de l'environnement du relais")
    return cle


def mandataire_de(environnement):
    brut = environnement.get("HTTPS_PROXY") or environnement.get("https_proxy")
    if not brut:
        return None
    p = urllib.parse.urlsplit(brut if "://" in brut else "http://" + brut)
    if p.scheme != "http" or not p.hostname or not p.port:
        raise RelaisInvalide("HTTPS_PROXY : http://hôte:port attendu")
    en_tetes = {}
    if p.username is not None:
        jeton = base64.b64encode(f"{urllib.parse.unquote(p.username)}:{urllib.parse.unquote(p.password or '')}"
                                 .encode("utf-8")).decode("ascii")
        en_tetes["Proxy-Authorization"] = "Basic " + jeton
    return p.hostname, p.port, en_tetes


def cible_de(amont: str, adresse_d_essai: str | None):
    if amont not in HOTES_PERMIS:
        raise RelaisInvalide(f"--amont : {HOTES_PERMIS[0]} attendu, reçu {amont!r}")
    if adresse_d_essai is None:
        return urllib.parse.urlsplit(f"https://{amont}")
    p = urllib.parse.urlsplit(adresse_d_essai)
    if p.scheme != "http" or p.hostname not in HOTES_LOCAUX or not p.port or p.path not in ("", "/"):
        raise RelaisInvalide("--adresse-d-essai : http vers la boucle locale seulement, avec un port, sans chemin")
    return p


def ouvrir_amont(cible, mandataire, contexte_tls, delai_s: float):
    """Établit la connexion vers l'amont, sans rien envoyer de la requête. Lève `RefusMandataire` à la signature du
    devis (connexion refusée ; tunnel refusé par le mandataire), `PanneConnexion` pour toute autre panne."""
    port = cible.port or (443 if cible.scheme == "https" else 80)
    classe = http.client.HTTPSConnection if cible.scheme == "https" else http.client.HTTPConnection
    plus = {"context": contexte_tls} if cible.scheme == "https" else {}
    try:
        if mandataire:
            hote_m, port_m, en_tetes = mandataire
            connexion = classe(hote_m, port_m, timeout=delai_s, **plus)
            connexion.set_tunnel(cible.hostname, port, headers=en_tetes)
        else:
            connexion = classe(cible.hostname, port, timeout=delai_s, **plus)
        connexion.connect()
        return connexion
    except ConnectionRefusedError:
        raise RefusMandataire("connexion refusée") from None
    except OSError as erreur:
        if str(erreur).startswith("Tunnel connection failed"):
            raise RefusMandataire("tunnel refusé par le mandataire") from None
        raise PanneConnexion(type(erreur).__name__) from None


def fabriquer_gestionnaire(cle, amont, cible, modele, etat, journal, mandataire, contexte_tls, delai_total_s,
                           variable_cle):
    verrou = threading.Lock()
    chemin_liste = f"/v1beta/models/{modele}"
    chemin_appel = f"/v1beta/models/{modele}:generateContent"

    def ecrire_journal(**champs):
        if not journal:
            return
        ligne = json.dumps({"quand": heure(), "relais": VERSION, **champs}, ensure_ascii=False, sort_keys=True) + "\n"
        with verrou, open(journal, "a", encoding="utf-8") as f:
            f.write(ligne)
            f.flush()
            os.fsync(f.fileno())

    class Gestionnaire(BaseHTTPRequestHandler):
        protocol_version = "HTTP/1.0"
        server_version = "relais"
        sys_version = ""

        def log_message(self, format, *args):  # noqa: A002 — signature imposée par la bibliothèque standard
            return

        def _json(self, code: int, objet: dict) -> None:
            corps = json.dumps(objet, ensure_ascii=False).encode("utf-8")
            self.send_response(code)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(corps)))
            self.end_headers()
            self.wfile.write(corps)

        def _refus(self, code: int, origine: str, motif: str, **plus) -> None:
            ecrire_journal(chemin=self.path, envoi=self.headers.get("X-Envoi"), code=code, origine=origine, motif=motif,
                           **plus)
            try:
                self._json(code, {"erreur": {"origine": origine, "motif": motif, "relais": VERSION}})
            except OSError:
                pass

        def do_GET(self):
            if self.path == CHEMIN_ETAT:
                self._json(200, {
                    "version": VERSION, "pid": os.getpid(), "amont": amont, "modele": modele,
                    "adresse_d_essai": None if cible.scheme == "https" else f"http://{cible.hostname}:{cible.port}",
                    "appels": etat["appels"], "max_appels": etat["max_appels"], "refus": etat["refus"],
                    "listes": etat["listes"], "delai_total_s": delai_total_s, "plafond_usd": None,
                    "variable_cle": variable_cle, "cle_dans_l_environnement": variable_cle in os.environ})
                return
            if self.path != chemin_liste:
                self._refus(403, "relais", "chemin non servi")
                return
            etat["listes"] += 1
            self._relayer("GET", chemin_liste, None, min(60.0, delai_total_s))

        def do_POST(self):
            if self.path != chemin_appel:
                self._refus(403, "relais", "chemin non servi : le modèle de la ligne, sans flux, et rien d'autre")
                return
            try:
                longueur = int(self.headers.get("Content-Length", ""))
            except ValueError:
                self._refus(411, "relais", "longueur du corps exigée")
                return
            if not 0 < longueur <= MAX_OCTETS_CORPS:
                self._refus(413, "relais", "corps vide ou trop long")
                return
            corps = self.rfile.read(longueur)
            try:
                objet = json.loads(corps.decode("utf-8"))
            except ValueError:
                objet = None
            if not isinstance(objet, dict):
                self._refus(400, "relais", "corps refusé : objet JSON exigé")
                return
            with verrou:
                if etat["appels"] >= etat["max_appels"]:
                    etat["refus"] += 1
                    plein = True
                else:
                    etat["appels"] += 1
                    plein = False
            if plein:
                self._refus(429, "relais", f"borne d'appels atteinte ({etat['max_appels']})")
                return
            self._relayer("POST", chemin_appel, corps, delai_total_s)

        def _relayer(self, methode: str, chemin: str, corps, delai_s: float):
            envoi, debut, compte = self.headers.get("X-Envoi"), time.monotonic(), corps is not None
            try:
                connexion = ouvrir_amont(cible, mandataire, contexte_tls, delai_s)
            except RefusMandataire as refus:
                if compte:
                    with verrou:
                        etat["appels"] -= 1   # rien n'a atteint le fournisseur
                self._refus(502, "mandataire", str(refus), octets_envoyes_amont=0)
                return
            except PanneConnexion as panne:
                self._refus(502, "relais", "connexion", genre=str(panne), octets_envoyes_amont=0)
                return
            # La prise de l'amont est doublée : `http.client` détache la sienne dès que la réponse annonce la fermeture
            # (toute réponse HTTP/1.0), et une prise détachée ne se règle ni ne se ferme plus. Le double vit jusqu'au bout.
            try:
                garde_prise = socket.socket(fileno=os.dup(connexion.sock.fileno()))
            except OSError as erreur:
                connexion.close()
                self._refus(502, "relais", "connexion", genre=type(erreur).__name__, octets_envoyes_amont=0)
                return
            fin = {"fini": False, "client_ferme": False, "delai": False}

            def couper_l_amont():
                try:
                    garde_prise.shutdown(socket.SHUT_RDWR)
                except OSError:
                    pass

            def guetter_le_client():
                try:
                    while not fin["fini"]:
                        if self.connection.recv(1, socket.MSG_PEEK) == b"":
                            break
                except OSError:
                    pass
                if not fin["fini"]:
                    fin["client_ferme"] = True
                    couper_l_amont()

            def au_delai():
                """Le délai total, tenu par une minuterie : il coupe l'amont même pendant un silence (devis, 5.6)."""
                if not fin["fini"]:
                    fin["delai"] = True
                    couper_l_amont()

            minuterie = threading.Timer(max(0.0, delai_s - (time.monotonic() - debut)), au_delai)
            minuterie.daemon = True
            envoyes, reponse = None, None

            def tout_fermer():
                fin["fini"] = True
                minuterie.cancel()
                for a_fermer in (reponse, connexion, garde_prise):
                    try:
                        if a_fermer is not None:
                            a_fermer.close()
                    except OSError:
                        pass

            try:
                en_tetes = {"x-goog-api-key": cle, "Accept": "application/json",
                            "User-Agent": self.headers.get("User-Agent") or "client-http/1.0"}
                if compte:
                    en_tetes["Content-Type"] = "application/json"
                threading.Thread(target=guetter_le_client, daemon=True).start()
                minuterie.start()
                connexion.request(methode, chemin, body=corps, headers=en_tetes)
                envoyes = len(corps) if compte else 0
                reponse = connexion.getresponse()
                morceaux, total = [], 0
                while True:
                    morceau = reponse.read1(65536)
                    if not morceau:
                        break
                    morceaux.append(morceau)
                    total += len(morceau)
                    if total > MAX_OCTETS_REPONSE:
                        raise http.client.HTTPException("réponse trop longue")
                if fin["delai"] or fin["client_ferme"]:   # une réponse sans longueur annoncée finit sans erreur
                    raise http.client.IncompleteRead(b"")
                recu = b"".join(morceaux)
            except (OSError, http.client.HTTPException) as erreur:
                tout_fermer()
                if fin["client_ferme"]:
                    ecrire_journal(chemin=chemin, envoi=envoi, code=None, origine="relais", motif="client_ferme",
                                   octets_envoyes_amont=envoyes, client_ferme=True,
                                   duree_s=round(time.monotonic() - debut, 3))
                    return
                delai = fin["delai"] or isinstance(erreur, (socket.timeout, TimeoutError))
                self._refus(502, "relais", "delai_total" if delai else "coupure_amont", octets_envoyes_amont=envoyes,
                            duree_s=round(time.monotonic() - debut, 3))
                return
            tout_fermer()
            ecrire_journal(chemin=chemin, envoi=envoi, code=reponse.status, origine="amont", motif=None,
                           octets_envoyes_amont=envoyes, octets_recus=len(recu), client_ferme=False,
                           duree_s=round(time.monotonic() - debut, 3))
            try:
                self.send_response(reponse.status)
                self.send_header("Content-Type", reponse.getheader("Content-Type") or "application/json")
                self.send_header("Content-Length", str(len(recu)))
                if reponse.getheader("Retry-After"):
                    self.send_header("Retry-After", reponse.getheader("Retry-After"))
                self.end_headers()
                self.wfile.write(recu)
            except OSError:
                pass

    return Gestionnaire


def servir(port: int, environnement, variable_cle: str, amont: str, modele: str, max_appels: int, delai_total_s: float,
           journal=None, adresse_d_essai=None):
    """Monte le serveur et le rend, sans le faire tourner (les essais le font tourner dans un fil)."""
    if not (max_appels >= 0 and delai_total_s > 0):
        raise RelaisInvalide("borne d'appels et délai : nombres positifs exigés")
    if not modele or "/" in modele or ":" in modele or "?" in modele:
        raise RelaisInvalide("--modele : identifiant exact, sans chemin")
    cible = cible_de(amont, adresse_d_essai)
    cle = lire_cle(environnement, variable_cle)
    mandataire = mandataire_de(environnement)
    contexte = None
    if cible.scheme == "https":
        ca = environnement.get("SSL_CERT_FILE")
        contexte = ssl.create_default_context(cafile=ca) if ca else ssl.create_default_context()
    etat = {"appels": 0, "max_appels": max_appels, "refus": 0, "listes": 0}
    gestionnaire = fabriquer_gestionnaire(cle, amont, cible, modele, etat, journal, mandataire, contexte, delai_total_s,
                                          variable_cle)
    serveur = ThreadingHTTPServer((HOTE, port), gestionnaire)
    serveur.daemon_threads = True
    return serveur


def analyseur() -> argparse.ArgumentParser:
    a = argparse.ArgumentParser(description="Relais local de Google (generateContent, sans flux), essais d'admission")
    a.add_argument("--variable-cle", required=True)
    a.add_argument("--port", type=int, default=0)
    a.add_argument("--amont", required=True)
    a.add_argument("--adresse-d-essai", default=None, help="http://127.0.0.1:PORT, essais sans réseau seulement")
    a.add_argument("--modele", required=True)
    a.add_argument("--max-appels", type=int, required=True)
    a.add_argument("--delai-total-s", type=float, required=True)
    a.add_argument("--journal", default=None)
    return a


def principal(argv=None) -> int:
    args = analyseur().parse_args(argv)
    try:
        serveur = servir(args.port, os.environ, args.variable_cle, args.amont, args.modele, args.max_appels,
                         args.delai_total_s, args.journal, args.adresse_d_essai)
    except RelaisInvalide as refus:
        print(f"relais non lancé : {refus}", file=sys.stderr)
        return 2
    print(f"relais prêt sur http://{HOTE}:{serveur.server_address[1]} (pid {os.getpid()}, amont {args.amont}, "
          f"modèle {args.modele}, {args.max_appels} appels au plus, sans plafond en dollars)", flush=True)
    try:
        serveur.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        serveur.server_close()
    return 0


if __name__ == "__main__":
    raise SystemExit(principal())
