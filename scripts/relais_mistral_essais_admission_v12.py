#!/usr/bin/env python3
"""Relais local de Mistral pour les essais d'admission du bras A (second lecteur) — version 12.

Devis joué : `docs/notes/relance-organismes-discrets-v1/devis-essais-admission-mistral-neon-bras-a-v1.md`
(`421ee2e6ec909c8b6261b3be39109aa5e76d6c275e79b4d7ec122816c83dd1bc`), sections 4.4, 5.2, 5.5, 5.6, 6.4 et 12 (point 7).
Formes des appels : relevés `releve-api-mistral-gemini-essais-admission-v1.md` et `…-complement-v1.md` (non opposables).

Un petit serveur dans son propre processus, sur la boucle locale seulement (`127.0.0.1`, aucune option ne le change).
Le programme qui conduit les essais n'a aucune clé : le relais tient la clé, l'amont fixe, la borne d'appels et un
plafond en dollars. **Un relais est lancé par ligne de calcul**, et arrêté par son identifiant de processus (R10).

Ce qu'il sert, et rien d'autre :
- `GET /relais/etat` : compteurs, bornes, amont, identifiant de processus ; jamais la clé ;
- `GET /v1/models` : l'appel de liste, gratuit, relayé tel quel (code et corps) ; il n'est pas compté parmi les appels ;
- `POST /v1/chat/completions` : **le flux de l'amont passe tel quel**, octet pour octet. Le corps doit être un objet
  JSON dont `model` est le modèle de la ligne et `stream` vaut vrai ; sinon 400, rien n'est envoyé.

Clé : lue une seule fois dans la variable `--variable-cle` de l'environnement du relais, puis effacée de
`os.environ` ; jamais en argument, jamais journalisée ni affichée. Toute clé reçue du client est retirée.

Amont : `--amont` est un nom d'hôte, l'un des deux permis (`api.eu.mistral.ai`, `api.mistral.ai`), joint en `https`.
Pour les essais sans réseau, `--adresse-d-essai http://127.0.0.1:PORT` remplace l'adresse jointe (boucle locale
seulement) ; l'état le dit (`adresse_d_essai`), et le programme des essais refuse une ligne réelle sur un tel relais.

Signature du refus du mandataire (devis, 4.4, ligne 1) : le relais rend le code 502 avec l'origine `mandataire`
**seulement** si l'établissement de la connexion vers l'amont a échoué avant tout octet de la requête — connexion
refusée, ou réponse du mandataire à la demande de tunnel d'un code autre que 200 —, et son journal porte, pour cet
envoi, `octets_envoyes_amont` à zéro. Toute autre panne porte l'origine `relais`.

Fermeture (garde 19) : dès que le client ferme sa connexion, le relais ferme la connexion vers l'amont (un fil
guette la fermeture du client, même pendant un silence de l'amont).

Délais : `--delai-silence-s` (aucun octet de l'amont) et `--delai-total-s`, réglés dix secondes sous ceux du
programme, pour que la coupure vienne du relais. Le délai total est tenu par une minuterie (m-11). Avant le premier octet relayé : code 502, origine `relais`, motif
`delai_silence` ou `delai_total`. Après : le relais ajoute au flux l'événement `event: relais` qui porte le motif, puis
ferme.

Plafond (seconde barrière, devis 6.4) : un appel n'est admis que si la dépense comptée plus la réserve
(`octets du corps × prix d'entrée + --reserve-sortie-jetons × prix de sortie`) tient sous `--plafond-usd` ; sinon 402,
origine `relais`. Un envoi fini est compté sur le bloc `usage` vu passer (la plus grande des deux lectures de la
sortie) ; un envoi sans `usage` est compté à l'entrée de son corps plus les octets de contenu vus plus 64, au prix de
sortie : c'est un compte bas, jamais au-dessus de celui du programme, pour que le relais ne refuse pas avant lui.
Au-delà de `--max-appels` : 429, origine `relais`.

Clé dans une réponse (garde 7, m-4) : le relais cherche la valeur exacte de sa clé dans tout corps reçu de l'amont,
la masque avant de relayer, et journalise le booléen `cle_vue_dans_la_reponse`.

Journal (`--journal`, une ligne JSON par événement) : heure, chemin, identifiant d'envoi (`X-Envoi`, non relayé),
code, origine, motif, octets envoyés à l'amont, octets reçus, octets de contenu, nombres du bloc `usage`, coût,
client fermé ou non — **jamais un texte, jamais la clé**.

Bibliothèque standard seulement. Essais : `tests/test_chef_essais_admission_bras_a_v12.py` (faux fournisseur local).
"""
from __future__ import annotations

import argparse
import base64
import datetime
import fcntl
import http.client
import json
import os
import socket
import ssl
import struct
import sys
import threading
import time
import urllib.parse
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

VERSION = "relais_mistral_essais_admission_v12"
HOTE = "127.0.0.1"
HOTES_LOCAUX = ("127.0.0.1", "localhost", "::1")
HOTES_PERMIS = ("api.eu.mistral.ai", "api.mistral.ai")
CHEMIN_APPEL = "/v1/chat/completions"
CHEMIN_LISTE = "/v1/models"
CHEMIN_ETAT = "/relais/etat"
MARGE_JETONS = 64
MAX_OCTETS_CORPS = 4_000_000
MAX_OCTETS_ERREUR = 1_000_000
EN_TETES_DE_CLE = ("authorization", "x-api-key", "proxy-authorization", "api-key", "x-goog-api-key")


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
    """Rend l'adresse jointe. `amont` est l'un des hôtes permis ; l'adresse d'essai ne vise que la boucle locale."""
    if amont not in HOTES_PERMIS:
        raise RelaisInvalide(f"--amont : l'un de {HOTES_PERMIS} attendu, reçu {amont!r}")
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


def _entier(x) -> bool:
    return isinstance(x, int) and not isinstance(x, bool) and x >= 0


def octets_des_chaines(objet) -> int:
    """Somme des longueurs en octets UTF-8 de toutes les chaînes d'un contenu, hors les valeurs des champs `type`."""
    if isinstance(objet, str):
        return len(objet.encode("utf-8"))
    if isinstance(objet, list):
        return sum(octets_des_chaines(x) for x in objet)
    if isinstance(objet, dict):
        return sum(octets_des_chaines(v) for k, v in objet.items() if k != "type")
    return 0


class SuiviDuFlux:
    """Lit le flux qui passe, sans le changer : octets de contenu et bloc `usage`. Rien n'est gardé du texte."""

    def __init__(self):
        self.reste, self.octets_contenu, self.usage = b"", 0, None

    def nourrir(self, octets: bytes) -> None:
        self.reste += octets
        *lignes, self.reste = self.reste.split(b"\n")
        for ligne in lignes:
            ligne = ligne.strip()
            if not ligne.startswith(b"data:"):
                continue
            try:
                o = json.loads(ligne[5:].strip().decode("utf-8"))
            except ValueError:
                continue
            if not isinstance(o, dict):
                continue
            if isinstance(o.get("usage"), dict):
                self.usage = o["usage"]
            choix = o.get("choices")
            if isinstance(choix, list) and choix and isinstance(choix[0], dict) and isinstance(choix[0].get("delta"), dict):
                self.octets_contenu += octets_des_chaines(choix[0]["delta"].get("content"))


def coupure_brutale(prise) -> None:
    """m-b : avant de fermer une prise de l'amont **coupée** (client parti, délai), la fermeture est rendue brutale
    (`SO_LINGER` à zéro) : l'amont reçoit la remise à zéro tout de suite, sans attendre que sa file d'émission se vide."""
    try:
        prise.setsockopt(socket.SOL_SOCKET, socket.SO_LINGER, struct.pack("ii", 1, 0))
    except OSError:
        pass


class Masque:
    """m-4 (garde 7) : le relais tient la clé ; il cherche sa **valeur exacte** dans tout ce que rend l'amont avant de
    le relayer, la remplace, et retient qu'il l'a vue (`vue`). Une clé à cheval sur deux morceaux est vue aussi : la
    fin d'un morceau n'est retenue que si elle peut être un début de clé. La valeur n'est ni journalisée ni rendue."""
    REMPLACEMENT = b"[cle-du-relais-masquee]"

    def __init__(self, cle: str):
        self.cle, self.reste, self.vue = cle.encode("utf-8"), b"", False

    def passer(self, octets: bytes, fin: bool = False) -> bytes:
        donnees = self.reste + octets
        if self.cle in donnees:
            self.vue = True
            donnees = donnees.replace(self.cle, self.REMPLACEMENT)
        retenu = 0
        if not fin:
            for k in range(min(len(self.cle) - 1, len(donnees)), 0, -1):
                if donnees.endswith(self.cle[:k]):
                    retenu = k
                    break
        self.reste = donnees[len(donnees) - retenu:] if retenu else b""
        return donnees[:len(donnees) - retenu] if retenu else donnees

    def en_tete(self, valeur):
        """Un en-tête relayé qui porterait la clé n'est pas relayé."""
        if valeur is not None and self.cle.decode("utf-8") in valeur:
            self.vue = True
            return None
        return valeur


class Compte:
    def __init__(self, plafond_usd, prix, reserve_sortie_jetons, max_appels):
        self.plafond, self.prix, self.reserve_sortie, self.max_appels = plafond_usd, prix, reserve_sortie_jetons, max_appels
        self.depense, self.appels, self.refus, self.listes = 0.0, 0, 0, 0
        self.verrou = threading.Lock()

    def reserve(self, octets_corps: int) -> float:
        return (octets_corps * self.prix[0] + self.reserve_sortie * self.prix[1]) / 1e6

    def admettre(self, octets_corps: int):
        with self.verrou:
            if self.appels >= self.max_appels:
                self.refus += 1
                return 429, f"borne d'appels atteinte ({self.max_appels})"
            if self.depense + self.reserve(octets_corps) > self.plafond + 1e-9:
                self.refus += 1
                return 402, f"plafond du relais ({self.plafond} USD) : dépense comptée plus réserve au-dessus"
            self.appels += 1
            return None

    def rendre_l_appel(self) -> None:
        with self.verrou:
            self.appels -= 1

    def regler(self, octets_corps: int, suivi: SuiviDuFlux | None) -> float:
        usage = suivi.usage if suivi else None
        if isinstance(usage, dict) and _entier(usage.get("prompt_tokens")) and _entier(usage.get("completion_tokens")):
            entree, sortie = usage["prompt_tokens"], usage["completion_tokens"]
            if _entier(usage.get("total_tokens")):
                sortie = max(sortie, usage["total_tokens"] - entree)
        else:
            entree, sortie = octets_corps, (suivi.octets_contenu if suivi else 0) + MARGE_JETONS
        cout = (entree * self.prix[0] + sortie * self.prix[1]) / 1e6
        with self.verrou:
            self.depense += cout
        return cout


def fabriquer_gestionnaire(cle, amont, cible, modele, compte, journal, mandataire, contexte_tls, delai_silence_s,
                           delai_total_s, variable_cle):
    verrou_journal = threading.Lock()

    def ecrire_journal(**champs):
        if not journal:
            return
        ligne = json.dumps({"quand": heure(), "relais": VERSION, **champs}, ensure_ascii=False, sort_keys=True) + "\n"
        with verrou_journal, open(journal, "a", encoding="utf-8") as f:
            f.write(ligne)
            f.flush()
            os.fsync(f.fileno())

    class Gestionnaire(BaseHTTPRequestHandler):
        protocol_version = "HTTP/1.0"
        server_version = "relais"
        sys_version = ""

        def log_message(self, format, *args):  # noqa: A002 — signature imposée par la bibliothèque standard
            return

        def _json(self, code: int, objet: dict, en_tetes: dict | None = None) -> None:
            corps = json.dumps(objet, ensure_ascii=False).encode("utf-8")
            self.send_response(code)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(corps)))
            for k, v in (en_tetes or {}).items():
                self.send_header(k, v)
            self.end_headers()
            self.wfile.write(corps)

        def _refus(self, code: int, origine: str, motif: str, **plus) -> None:
            ecrire_journal(chemin=self.path, envoi=self.headers.get("X-Envoi"), code=code, origine=origine, motif=motif,
                           **plus)
            try:
                self._json(code, {"erreur": {"origine": origine, "motif": motif, "relais": VERSION}})
            except OSError:
                pass

        def _en_tetes_amont(self, avec_corps: bool) -> dict:
            en_tetes = {"Authorization": "Bearer " + cle, "Accept": "*/*",
                        "User-Agent": self.headers.get("User-Agent") or "client-http/1.0"}
            if avec_corps:
                en_tetes["Content-Type"] = "application/json"
            return en_tetes

        def do_GET(self):
            if self.path == CHEMIN_ETAT:
                self._json(200, {
                    "version": VERSION, "pid": os.getpid(), "amont": amont, "modele": modele,
                    "adresse_d_essai": None if cible.scheme == "https" else f"http://{cible.hostname}:{cible.port}",
                    "appels": compte.appels, "max_appels": compte.max_appels, "refus": compte.refus,
                    "listes": compte.listes, "depense_usd": round(compte.depense, 6), "plafond_usd": compte.plafond,
                    "prix": list(compte.prix), "reserve_sortie_jetons": compte.reserve_sortie,
                    "delai_silence_s": delai_silence_s, "delai_total_s": delai_total_s,
                    "variable_cle": variable_cle, "cle_dans_l_environnement": variable_cle in os.environ})
                return
            if self.path != CHEMIN_LISTE:
                self._refus(403, "relais", "chemin non servi")
                return
            self._relayer_entier("GET", CHEMIN_LISTE, None)

        def do_POST(self):
            if self.path != CHEMIN_APPEL:
                self._refus(403, "relais", "chemin non servi")
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
                demande = json.loads(corps.decode("utf-8"))
            except ValueError:
                demande = None
            if not isinstance(demande, dict) or demande.get("model") != modele or demande.get("stream") is not True:
                self._refus(400, "relais", "corps refusé : objet JSON, modèle de la ligne et flux exigés")
                return
            refus = compte.admettre(len(corps))
            if refus:
                self._refus(refus[0], "relais", refus[1])
                return
            self._relayer_flux(corps)

        def _ouvrir(self, delai_s):
            """Rend la connexion, ou None après avoir répondu (signature du mandataire, ou panne de connexion)."""
            try:
                return ouvrir_amont(cible, mandataire, contexte_tls, delai_s)
            except RefusMandataire as refus:
                self._refus(502, "mandataire", str(refus), octets_envoyes_amont=0)
            except PanneConnexion as panne:
                self._refus(502, "relais", "connexion", genre=str(panne), octets_envoyes_amont=0)
            return None

        def _relayer_entier(self, methode: str, chemin: str, corps):
            compte.listes += 1
            connexion = self._ouvrir(min(60.0, delai_total_s))
            if connexion is None:
                return
            try:
                connexion.request(methode, chemin, body=corps, headers=self._en_tetes_amont(corps is not None))
                reponse = connexion.getresponse()
                masque = Masque(cle)
                recu = masque.passer(reponse.read(MAX_OCTETS_ERREUR), fin=True)
            except (OSError, http.client.HTTPException) as erreur:
                delai = isinstance(erreur, (socket.timeout, TimeoutError))
                self._refus(502, "relais", "delai_total" if delai else "coupure_amont", octets_envoyes_amont=None)
                return
            finally:
                connexion.close()
            type_du_contenu = masque.en_tete(reponse.getheader("Content-Type"))
            ecrire_journal(chemin=chemin, envoi=self.headers.get("X-Envoi"), code=reponse.status, origine="amont",
                           octets_recus=len(recu), cle_vue_dans_la_reponse=masque.vue)
            self.send_response(reponse.status)
            self.send_header("Content-Type", type_du_contenu or "application/json")
            self.send_header("Content-Length", str(len(recu)))
            self.end_headers()
            self.wfile.write(recu)

        def _relayer_flux(self, corps: bytes):
            envoi, debut = self.headers.get("X-Envoi"), time.monotonic()
            connexion = self._ouvrir(delai_silence_s)
            if connexion is None:
                compte.rendre_l_appel()   # rien n'a atteint le fournisseur
                return
            # La prise de l'amont est doublée : `http.client` détache la sienne dès que la réponse annonce la fermeture
            # (toute réponse HTTP/1.0), et une prise détachée ne se ferme plus. Le double vit jusqu'au bout (garde 19).
            try:
                prise_amont = socket.socket(fileno=os.dup(connexion.sock.fileno()))
            except OSError as erreur:
                connexion.close()
                compte.rendre_l_appel()
                self._refus(502, "relais", "connexion", genre=type(erreur).__name__, octets_envoyes_amont=0)
                return
            suivi, etat = SuiviDuFlux(), {"client_ferme": False, "fini": False, "delai_total": False}
            masque = Masque(cle)

            def au_delai_total():
                """m-11 : le délai total est tenu par une minuterie, qui coupe l'amont même au milieu d'un silence
                (il n'était contrôlé qu'entre deux morceaux, et pouvait être dépassé d'un délai de silence)."""
                if not etat["fini"]:
                    etat["delai_total"] = True
                    try:
                        prise_amont.shutdown(socket.SHUT_RDWR)
                    except OSError:
                        pass

            minuterie = threading.Timer(max(0.0, delai_total_s - (time.monotonic() - debut)), au_delai_total)
            minuterie.daemon = True
            minuterie.start()
            bilan = {"chemin": CHEMIN_APPEL, "envoi": envoi, "octets_corps": len(corps), "octets_envoyes_amont": None,
                     "octets_recus": 0, "origine": "amont", "motif": None, "code": None}

            def guetter_le_client():
                """Garde 19 : la fermeture du client ferme l'amont, même pendant un silence de l'amont."""
                try:
                    while not etat["fini"]:
                        if self.connection.recv(1, socket.MSG_PEEK) == b"":
                            break
                except OSError:
                    pass
                if not etat["fini"]:
                    etat["client_ferme"] = True
                    try:
                        prise_amont.shutdown(socket.SHUT_RDWR)
                    except (OSError, AttributeError):
                        pass

            entame, reponse = False, None
            try:
                connexion.request("POST", CHEMIN_APPEL, body=corps, headers=self._en_tetes_amont(True))
                bilan["octets_envoyes_amont"] = len(corps)
                reponse = connexion.getresponse()
                bilan["code"] = reponse.status
                if reponse.status != 200:
                    recu = masque.passer(reponse.read(MAX_OCTETS_ERREUR), fin=True)
                    bilan["octets_recus"] = len(recu)
                    attente = masque.en_tete(reponse.getheader("Retry-After"))
                    plus = {"Retry-After": attente} if attente else {}
                    self.send_response(reponse.status)
                    self.send_header("Content-Type", masque.en_tete(reponse.getheader("Content-Type")) or "application/json")
                    self.send_header("Content-Length", str(len(recu)))
                    for k, v in plus.items():
                        self.send_header(k, v)
                    self.end_headers()
                    self.wfile.write(recu)
                    return
                threading.Thread(target=guetter_le_client, daemon=True).start()
                while True:
                    if time.monotonic() - debut > delai_total_s:
                        raise TimeoutError("delai_total")
                    morceau = reponse.read1(65536)
                    if etat["delai_total"]:
                        raise TimeoutError("delai_total")
                    if etat["client_ferme"]:
                        break
                    if not morceau:
                        morceau = masque.passer(b"", fin=True)      # ce que le masque retenait encore
                        if morceau and entame:
                            try:
                                self.wfile.write(morceau)
                                self.wfile.flush()
                            except OSError:
                                etat["client_ferme"] = True
                        break
                    if not entame:
                        self.send_response(200)
                        self.send_header("Content-Type", masque.en_tete(reponse.getheader("Content-Type")) or "text/event-stream")
                        self.send_header("Connection", "close")
                        self.end_headers()
                        entame = True
                    suivi.nourrir(morceau)
                    bilan["octets_recus"] += len(morceau)
                    try:
                        self.wfile.write(masque.passer(morceau))
                        self.wfile.flush()
                    except OSError:
                        etat["client_ferme"] = True
                        break
                if not entame and not etat["client_ferme"]:
                    raise http.client.IncompleteRead(b"")
            except (OSError, http.client.HTTPException) as erreur:
                if not etat["client_ferme"]:
                    if str(erreur) == "delai_total" or etat["delai_total"]:
                        motif = "delai_total"
                    elif isinstance(erreur, (socket.timeout, TimeoutError)):
                        motif = "delai_silence"
                    else:
                        motif = "coupure_amont"
                    bilan["origine"], bilan["motif"] = "relais", motif
                    objet = {"erreur": {"origine": "relais", "motif": motif, "relais": VERSION}}
                    try:
                        if entame:
                            self.wfile.write(b"\nevent: relais\ndata: " + json.dumps(objet).encode("utf-8") + b"\n\n")
                            self.wfile.flush()
                        else:
                            bilan["code"] = 502
                            self._json(502, objet)
                    except OSError:
                        etat["client_ferme"] = True
            finally:
                etat["fini"] = True
                minuterie.cancel()
                bilan["cle_vue_dans_la_reponse"] = masque.vue
                # Fermeture explicite de tout ce qui tient la prise de l'amont : la réponse (à qui `http.client` passe
                # la prise quand l'amont annonce la fermeture), la connexion, et le double.
                if etat["client_ferme"] or etat["delai_total"]:
                    coupure_brutale(prise_amont)
                for a_fermer in (reponse, connexion, prise_amont):
                    try:
                        if a_fermer is not None:
                            a_fermer.close()
                    except OSError:
                        pass
                cout = compte.regler(len(corps), suivi)
                usage = suivi.usage if isinstance(suivi.usage, dict) else {}
                ecrire_journal(**bilan, client_ferme=etat["client_ferme"], octets_contenu=suivi.octets_contenu,
                               usage={k: v for k, v in usage.items() if _entier(v)}, cout_usd=round(cout, 6),
                               depense_usd=round(compte.depense, 6), duree_s=round(time.monotonic() - debut, 3))

    return Gestionnaire


def servir(port: int, environnement, variable_cle: str, amont: str, modele: str, max_appels: int, plafond_usd: float,
           prix, reserve_sortie_jetons: int, delai_silence_s: float, delai_total_s: float, journal=None,
           adresse_d_essai=None):
    """Monte le serveur et le rend, sans le faire tourner (les essais le font tourner dans un fil)."""
    if not (max_appels >= 0 and plafond_usd >= 0 and reserve_sortie_jetons > 0 and delai_silence_s > 0
            and delai_total_s > 0 and len(prix) == 2 and min(prix) >= 0):
        raise RelaisInvalide("bornes, prix et délais : nombres positifs exigés")
    cible = cible_de(amont, adresse_d_essai)
    cle = lire_cle(environnement, variable_cle)
    mandataire = mandataire_de(environnement)
    contexte = None
    if cible.scheme == "https":
        ca = environnement.get("SSL_CERT_FILE")
        contexte = ssl.create_default_context(cafile=ca) if ca else ssl.create_default_context()
    compte = Compte(plafond_usd, tuple(prix), reserve_sortie_jetons, max_appels)
    gestionnaire = fabriquer_gestionnaire(cle, amont, cible, modele, compte, journal, mandataire, contexte,
                                          delai_silence_s, delai_total_s, variable_cle)
    serveur = ThreadingHTTPServer((HOTE, port), gestionnaire)
    serveur.daemon_threads = True
    return serveur


def analyseur() -> argparse.ArgumentParser:
    a = argparse.ArgumentParser(description="Relais local de Mistral, essais d'admission du bras A")
    a.add_argument("--variable-cle", required=True)
    a.add_argument("--port", type=int, default=0)
    a.add_argument("--amont", required=True, help="nom d'hôte de l'amont, l'un des deux permis")
    a.add_argument("--adresse-d-essai", default=None, help="http://127.0.0.1:PORT, essais sans réseau seulement")
    a.add_argument("--modele", required=True)
    a.add_argument("--max-appels", type=int, required=True)
    a.add_argument("--plafond-usd", type=float, required=True)
    a.add_argument("--prix-entree", type=float, required=True)
    a.add_argument("--prix-sortie", type=float, required=True)
    a.add_argument("--reserve-sortie-jetons", type=int, required=True)
    a.add_argument("--delai-silence-s", type=float, required=True)
    a.add_argument("--delai-total-s", type=float, required=True)
    a.add_argument("--journal", default=None)
    a.add_argument("--verrou-des-vivants", default=None,
                   help="fichier de verrou que le relais tient en partage tant qu'il vit (une amorce neuve le voit)")
    return a


def tenir_le_verrou_des_vivants(chemin):
    """Tant que le relais vit, il tient ce verrou en partage : une amorce neuve du même fournisseur ne part pas tant
    qu'un relais d'un lancement antérieur vit encore. Rend le descripteur, à garder ouvert."""
    if not chemin:
        return None
    descripteur = os.open(chemin, os.O_CREAT | os.O_RDWR, 0o644)
    fcntl.flock(descripteur, fcntl.LOCK_SH)
    return descripteur


def principal(argv=None) -> int:
    args = analyseur().parse_args(argv)
    try:
        verrou_tenu = tenir_le_verrou_des_vivants(args.verrou_des_vivants)   # noqa: F841 — gardé ouvert jusqu'à la fin
        serveur = servir(args.port, os.environ, args.variable_cle, args.amont, args.modele, args.max_appels,
                         args.plafond_usd, (args.prix_entree, args.prix_sortie), args.reserve_sortie_jetons,
                         args.delai_silence_s, args.delai_total_s, args.journal, args.adresse_d_essai)
    except RelaisInvalide as refus:
        print(f"relais non lancé : {refus}", file=sys.stderr)
        return 2
    print(f"relais prêt sur http://{HOTE}:{serveur.server_address[1]} (pid {os.getpid()}, amont {args.amont}, "
          f"modèle {args.modele}, {args.max_appels} appels au plus, plafond {args.plafond_usd} USD)", flush=True)
    try:
        serveur.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        serveur.server_close()
    return 0


if __name__ == "__main__":
    raise SystemExit(principal())
