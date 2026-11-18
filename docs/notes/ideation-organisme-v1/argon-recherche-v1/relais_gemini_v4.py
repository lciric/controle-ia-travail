#!/usr/bin/env python3
"""Relais Gemini local, version 4 : la v2, plus les **trois chemins du mode par lot** (pièce neutre, réutilisable).

Session de relance des organismes discrets, 18 novembre 2026, sur la décision de la session mère (07:29Z, R-3241) : la lignée
Carbon passe par le mode par lot (« Batch API » de Gemini), parce qu'en appel synchrone à budget de pensée élevé le modèle
reste muet au-delà de la coupure à 300 s des connexions muettes de ces conteneurs, alors qu'un lot rend en quelques minutes
(épreuve du 18 novembre, 430 s, 844 jetons de pensée). Copie de `relais_gemini_v2.py` (`2b0043bc…`, inchangée, R12) ; ce
qui change, et rien d'autre :

1. `POST /v1beta/models/<modèle>:batchGenerateContent` est relayé (modèle dans la liste blanche, borne `--max-lots`, comptée
   avant l'envoi) ; le nom du lot rendu par l'amont (`batches/…`) est **retenu** par le relais.
2. `GET /v1beta/batches/<identifiant>` (état et résultat) et `POST /v1beta/batches/<identifiant>:cancel` ne sont relayés que
   pour un lot **créé par ce relais** ; tout autre identifiant : 403, rien n'est envoyé. Les relevés sont bornés par
   `--max-releves` (défaut 2 000) ; ils ne comptent pas dans `--max-appels`.
3. Journal : `action` = `batchGenerateContent`, `releve_lot` ou `annule_lot`, nom du lot, état (`metadata.state`), `done`,
   et `usageMetadata` de chaque réponse du lot quand il est fini — jamais le texte, jamais la clé.
4. `/relais/etat` : lots créés, relevés faits et restants, annulations.
5. Corrigé avant tout scellement après la contre-lecture des commandes neutres (`contre-lecture-commandes-neutres-lot-et-
   astra-v1.md`) : **l'annulation a sa propre borne** (`--max-annulations`, défaut 16), jamais mangée par les relevés ;
   **le contenu d'un lot est borné avant l'envoi** : au plus `--max-requetes-par-lot` requêtes (défaut 1), aucune requête
   qui nomme un autre modèle (`model`) ni qui déclare des outils (`tools`, `toolConfig`) ; sinon 403, rien n'est envoyé.

Tout le reste — clé lue puis effacée, clé du client retirée, liste blanche des modèles, bornes d'appels et d'octets, masquage
de la clé dans le corps relayé, `generateContent` et `countTokens` sans flux — est celui de la v2.

## En-tête de la v2 (inchangé)

Relais Gemini local, version 2 : la v1, plus le **masquage de la vraie clé dans le corps relayé**.

Lignée session-depot, 30 octobre 2026. Copie de `lancement-v2/relais_gemini_v1.py` (inchangée, R12). Seul changement :
avant d'écrire la réponse de l'amont au client, chaque occurrence de la vraie clé (octets UTF-8) dans le corps est
remplacée par `[clé]`, et `Content-Length` est recalculé sur le corps relayé. Pourquoi : sous l'enveloppe v4 ou v4b, la
commande d'Argon ne détient que la clé factice `factice-relais` ; son masquage ne vise qu'elle. Le relais v1 ne masquait
la vraie clé que dans les en-têtes : un amont qui la recopie dans le corps (titre ou adresse d'une source de recherche,
message d'erreur) la faisait passer jusqu'à la sortie de la commande (vérifié hors réseau, contre-lecture de la v3).
Le journal dit le nombre de remplacements (`cle_masquee_dans_reponse`, seulement s'il est non nul) et lit le corps masqué
(en v1, un `modelVersion` qui portait la clé faisait échouer le garde-fou du journal : entrée perdue, sans fuite) ;
`octets_reponse` reste la taille reçue de l'amont. Limite : une clé encodée autrement (échappement `\\uXXXX`, encodage d'adresse, corps
compressé malgré `Accept-Encoding: identity`) n'est pas reconnue. Tout le reste est celui de la v1.

## En-tête de la v1 (inchangé)

Relais Gemini local, version 1 : la commande d'Argon n'a plus **aucune clé** (ni fichier, ni variable réelle).

Lignée session-depot, 29 octobre 2026. Même modèle que le relais Claude du pôle (`orchestrateur-v45/pole/relais_reel.py`) :
un petit serveur HTTP dans **son propre processus**, sur la boucle locale seulement, lancé par le noyau sous `env -i` avec la
vraie clé dans **son seul environnement** (variable `--variable-cle`, `GEMINI_API_KEY` par défaut) ; la clé est lue au
démarrage, effacée de `os.environ`, gardée en mémoire, jamais journalisée ni affichée. La commande `commande_argon_v2.py`
(inchangée, R12) reçoit de l'enveloppe v3 `--url-base http://127.0.0.1:8788/v1beta` et une clé **factice**
(`GEMINI_API_KEY=factice-relais`) qu'elle pose dans l'en-tête `x-goog-api-key` ; le relais **retire** toute clé reçue du client
(en-tête `x-goog-api-key`, en-tête `Authorization`, paramètre `?key=`) et pose la vraie, puis transmet à l'amont
(`https://generativelanguage.googleapis.com`) par le mandataire `HTTPS_PROXY` et les certificats `SSL_CERT_FILE` de son
environnement. Corps relayé tel quel ; réponse relayée telle quelle (code, corps, type de contenu).

Ce que le relais refuse **sans rien envoyer** :
- tout chemin autre que `POST /v1beta/models/<modèle>:generateContent` et `POST /v1beta/models/<modèle>:countTokens`, et
  tout modèle hors de la liste blanche (`--modele`, répétable, défaut `gemini-4-argon`) : 403 ;
- au-delà de `--max-appels` (défaut 64) appels relayés, ou un corps de plus de `--max-octets-corps` (défaut 8 000 000) octets :
  429 ;
- une requête sans `Content-Length` : 411 ; une méthode autre que GET (`/relais/etat` seulement) et POST : 403.

Journal (`--journal`, JSON par ligne) par appel : heure UTC, méthode, chemin (sans paramètre de clé), modèle, taille du
corps, code amont, `usageMetadata` (ou `totalTokens` pour `countTokens`) si présent, durée — **jamais le texte, jamais la
clé**. Route `GET /relais/etat` : appels, refus, octets, bornes, liste blanche, et la preuve que la variable de clé n'est plus
dans l'environnement du processus.

Limite connue (reprise de `relais_reel.py`, contre-lecture F-C7) : effacer la variable de `os.environ` n'efface pas le bloc
initial que `/proc/<pid>/environ` expose ; tout processus du même utilisateur (ou root) peut l'y lire tant que le relais vit.
L'utilisateur distinct `argon`, qui exécute la commande, n'est pas cet utilisateur : c'est tout l'objet du montage.

Ce fichier n'est jamais exécuté avec une vraie clé dans ce dépôt : ses essais (`test_relais_gemini_v1.py`) le lancent avec une
clé factice devant un faux amont local. Aucune dépendance hors bibliothèque standard.

Lancement (noyau, clé par variable sous `env -i`, jamais en argument ni en fichier) :

    setsid nohup env -i PATH=/usr/bin:/bin LANG=C.UTF-8 GEMINI_API_KEY="$CLE" HTTPS_PROXY=http://127.0.0.1:40191 \\
        SSL_CERT_FILE=/root/.ccr/ca-bundle.crt python3 -I -B relais_gemini_v1.py --port 8788 --max-appels 64 \\
        --journal $DOS/relais-gemini-journal-v1.jsonl > $DOS/relais-gemini-v1.log 2>&1 & echo $! > $DOS/relais-gemini.pid
"""

import argparse
import datetime
import http.client
import json
import os
import re
import ssl
import sys
import threading
import time
import urllib.parse
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

VERSION = "relais-gemini-v4"
HOTE = "127.0.0.1"  # jamais une autre interface : aucune option ne le change
PORT_DEFAUT = 8788
AMONT_DEFAUT = "https://generativelanguage.googleapis.com"
VARIABLE_CLE_DEFAUT = "GEMINI_API_KEY"
MODELES_DEFAUT = ("gemini-4-argon",)
MAX_APPELS_DEFAUT = 64
MAX_OCTETS_CORPS_DEFAUT = 8_000_000
TAILLE_MAX_REPONSE = 50_000_000  # au-delà : 502 (la commande refuse elle-même au-delà de cette taille)
DELAI_AMONT_DEFAUT_S = 1800.0    # ≥ délai de la commande (1 500 s) : c'est elle qui coupe en premier
HOTES_LOCAUX = {"127.0.0.1", "localhost", "::1"}
ACTIONS_PERMISES = ("generateContent", "countTokens", "batchGenerateContent")
MOTIF_CHEMIN = re.compile(r"^/v1beta/models/([A-Za-z0-9._-]+):(generateContent|countTokens|batchGenerateContent)$")
MOTIF_LOT = re.compile(r"^/v1beta/(batches/[A-Za-z0-9_-]+)(:cancel)?$")  # v4 : relevé (GET) et annulation (POST :cancel)
MAX_LOTS_DEFAUT = 8
MAX_RELEVES_DEFAUT = 2000
MAX_ANNULATIONS_DEFAUT = 16
MAX_REQUETES_PAR_LOT_DEFAUT = 1
EN_TETES_DE_CLE = {"x-goog-api-key", "authorization", "proxy-authorization"}
EN_TETES_NON_RELAYES = EN_TETES_DE_CLE | {"host", "connection", "content-length", "transfer-encoding", "keep-alive", "te",
                                          "trailer", "upgrade", "accept-encoding", "expect"}
PARAMETRES_DE_CLE = {"key", "access_token"}


class RelaisInvalide(Exception):
    """Réglage impossible : le relais ne démarre pas."""


def masquer(texte, cle):
    """Ne laisse jamais passer la clé dans un message, un journal ou une réponse."""
    texte = str(texte)
    return texte.replace(cle, "[clé]") if cle else texte


def lire_cle(environnement, variable):
    """Lit la clé dans l'environnement donné et l'en efface ; ne la rend qu'à l'appelant (jamais journalisée)."""
    cle = (environnement.get(variable) or "").strip()
    if not cle:
        raise RelaisInvalide(f"aucune clé dans la variable {variable} de l'environnement du relais")
    environnement.pop(variable, None)
    return cle


def valider_amont(amont):
    """`https://` vers n'importe quel hôte, ou `http://` vers la boucle locale seulement (essais)."""
    p = urllib.parse.urlsplit(amont)
    if p.scheme == "https" and p.hostname:
        return p
    if p.scheme == "http" and p.hostname in HOTES_LOCAUX:
        return p
    raise RelaisInvalide(f"--amont : https, ou http vers la boucle locale seulement (reçu {amont!r})")


def mandataire_de(environnement):
    """Mandataire HTTPS de l'environnement (`HTTPS_PROXY`, puis `https_proxy`) : (hôte, port, en-têtes du tunnel) ou None."""
    brut = environnement.get("HTTPS_PROXY") or environnement.get("https_proxy")
    if not brut:
        return None
    p = urllib.parse.urlsplit(brut if "://" in brut else "http://" + brut)
    if p.scheme != "http" or not p.hostname or not p.port:
        raise RelaisInvalide("HTTPS_PROXY : http://hôte:port attendu")
    en_tetes = {}
    if p.username is not None:
        import base64
        jeton = base64.b64encode(f"{urllib.parse.unquote(p.username)}:{urllib.parse.unquote(p.password or '')}"
                                 .encode("utf-8")).decode("ascii")
        en_tetes["Proxy-Authorization"] = "Basic " + jeton
    return p.hostname, p.port, en_tetes


def chemin_sans_cle(chemin):
    """Rend (chemin nettoyé, modèle, action) ; (None, None, None) si le chemin n'est pas permis. Retire tout paramètre de
    clé de la chaîne de requête ; garde les autres paramètres tels quels."""
    p = urllib.parse.urlsplit(chemin)
    m = MOTIF_CHEMIN.match(p.path)
    if not m:
        lot = MOTIF_LOT.match(p.path)
        if not lot:
            return None, None, None
        return p.path, lot.group(1), ("annule_lot" if lot.group(2) else "releve_lot")
    parametres = [(k, v) for k, v in urllib.parse.parse_qsl(p.query, keep_blank_values=True)
                  if k.lower() not in PARAMETRES_DE_CLE]
    propre = p.path + ("?" + urllib.parse.urlencode(parametres) if parametres else "")
    return propre, m.group(1), m.group(2)


def usage_d_une_reponse(corps):
    """Ce que le journal garde d'une réponse : `usageMetadata`, `totalTokens`, `modelVersion` s'ils sont présents, et c'est
    tout — jamais les candidats, jamais le texte."""
    try:
        objet = json.loads(corps.decode("utf-8"))
    except (UnicodeDecodeError, ValueError):
        return {}
    if not isinstance(objet, dict):
        return {}
    garde = {}
    if isinstance(objet.get("usageMetadata"), dict):
        garde["usageMetadata"] = {k: v for k, v in objet["usageMetadata"].items() if isinstance(v, (int, float))}
    if isinstance(objet.get("totalTokens"), int):
        garde["totalTokens"] = objet["totalTokens"]
    if isinstance(objet.get("modelVersion"), str):
        garde["modele_servi"] = objet["modelVersion"][:80]
    if isinstance(objet.get("error"), dict) and isinstance(objet["error"].get("status"), str):
        garde["statut_erreur_amont"] = objet["error"]["status"][:40]
    return garde


class Compteur:
    """Bornes du relais : nombre d'appels relayés et taille du corps par appel. Un appel est **compté avant de partir**
    (sous verrou) : des appels simultanés ne peuvent pas franchir la borne ensemble."""

    def __init__(self, max_appels, max_octets_corps, max_lots=MAX_LOTS_DEFAUT, max_releves=MAX_RELEVES_DEFAUT,
                 max_annulations=MAX_ANNULATIONS_DEFAUT):
        self.max_appels, self.max_octets_corps = int(max_appels), int(max_octets_corps)
        self.appels, self.refus, self.octets_envoyes, self.octets_recus = 0, 0, 0, 0
        self.par_statut = {}
        self.max_lots, self.max_releves = int(max_lots), int(max_releves)  # v4
        self.lots_crees, self.releves, self.lots = 0, 0, set()
        self.max_annulations, self.annulations = int(max_annulations), 0
        self._verrou = threading.Lock()

    def admettre_lot(self):
        """v4 : compte une création de lot avant l'envoi, ou rend le motif du refus."""
        with self._verrou:
            if self.lots_crees >= self.max_lots:
                self.refus += 1
                return f"--max-lots ({self.max_lots}) atteint"
            self.lots_crees += 1
            return None

    def retenir_lot(self, nom):
        with self._verrou:
            self.lots.add(nom)

    def admettre_releve(self, nom, annulation=False):
        """v4 : relevé ou annulation, seulement d'un lot créé par ce relais ; chacun dans sa propre borne."""
        with self._verrou:
            if nom not in self.lots:
                self.refus += 1
                return (403, "lot inconnu de ce relais : seuls les lots qu'il a créés sont relevés ou annulés")
            if annulation:
                if self.annulations >= self.max_annulations:
                    self.refus += 1
                    return (429, f"--max-annulations ({self.max_annulations}) atteint")
                self.annulations += 1
                return None
            if self.releves >= self.max_releves:
                self.refus += 1
                return (429, f"--max-releves ({self.max_releves}) atteint")
            self.releves += 1
            return None

    def admettre(self, longueur_corps):
        """Admet (compte) un appel ou rend le motif du refus."""
        with self._verrou:
            if longueur_corps > self.max_octets_corps:
                self.refus += 1
                return f"corps de {longueur_corps} octets au-dessus de --max-octets-corps ({self.max_octets_corps})"
            if self.appels >= self.max_appels:
                self.refus += 1
                return f"--max-appels ({self.max_appels}) atteint"
            self.appels += 1
            self.octets_envoyes += longueur_corps
            return None

    def refuser(self):
        with self._verrou:
            self.refus += 1

    def conclure(self, statut, octets_recus):
        with self._verrou:
            self.octets_recus += octets_recus
            self.par_statut[str(statut)] = self.par_statut.get(str(statut), 0) + 1

    def etat(self):
        with self._verrou:
            return {"appels": self.appels, "refus": self.refus, "octets_envoyes": self.octets_envoyes,
                    "octets_recus": self.octets_recus, "max_appels": self.max_appels,
                    "max_octets_corps": self.max_octets_corps, "appels_restants": max(0, self.max_appels - self.appels),
                    "reponses_par_statut": dict(self.par_statut), "lots_crees": self.lots_crees, "max_lots": self.max_lots,
                    "releves": self.releves, "releves_restants": max(0, self.max_releves - self.releves),
                    "annulations": self.annulations, "max_annulations": self.max_annulations}


def appel_amont(parties, mandataire, contexte_tls, delai_s, methode, chemin, corps, en_tetes):
    """v4 : un appel à l'amont ; rend (statut, en-têtes, octets lus) ; lève OSError, HTTPException, SSLError."""
    if parties.scheme == "https":
        if mandataire:
            hote_m, port_m, en_tetes_tunnel = mandataire
            connexion = http.client.HTTPSConnection(hote_m, port_m, context=contexte_tls, timeout=delai_s)
            connexion.set_tunnel(parties.hostname, parties.port or 443, headers=en_tetes_tunnel)
        else:
            connexion = http.client.HTTPSConnection(parties.hostname, parties.port or 443, context=contexte_tls, timeout=delai_s)
    else:
        connexion = http.client.HTTPConnection(parties.hostname, parties.port or 80, timeout=delai_s)
    try:
        connexion.request(methode, chemin, body=corps if methode == "POST" else None, headers=en_tetes)
        reponse = connexion.getresponse()
        return reponse.status, reponse.getheaders(), reponse.read(TAILLE_MAX_REPONSE + 1)
    finally:
        connexion.close()


def motif_contenu_lot(corps, modele, max_requetes):
    """v4 (corrigé) : rend le motif d'un refus du contenu d'un lot, ou None. Le corps doit être un objet JSON portant au
    plus `max_requetes` requêtes en ligne, sans modèle étranger ni outil."""
    try:
        o = json.loads(corps.decode("utf-8"))
        reqs = o["batch"]["input_config"]["requests"]["requests"]
    except (UnicodeDecodeError, ValueError, KeyError, TypeError):
        return "corps de lot illisible (batch.input_config.requests.requests attendu, requêtes en ligne seulement)"
    if not isinstance(reqs, list) or not reqs:
        return "lot sans requête"
    if len(reqs) > max_requetes:
        return f"{len(reqs)} requêtes dans le lot > --max-requetes-par-lot ({max_requetes})"
    for x in reqs:
        req = x.get("request") if isinstance(x, dict) else None
        if not isinstance(req, dict):
            return "requête du lot illisible"
        if "model" in req and str(req["model"]).split("/")[-1] != modele:
            return "requête du lot qui nomme un autre modèle"
        if "tools" in req or "toolConfig" in req or "tool_config" in req:
            return "requête du lot qui déclare des outils"
    return None


def resume_lot(brut):
    """v4 : ce que le journal garde d'une réponse de lot : nom, état, fini, usages des réponses — jamais le texte."""
    try:
        o = json.loads(brut.decode("utf-8"))
    except (UnicodeDecodeError, ValueError):
        return {}
    if not isinstance(o, dict):
        return {}
    meta = o.get("metadata") if isinstance(o.get("metadata"), dict) else {}
    garde = {"lot": (o.get("name") or meta.get("name")), "etat_lot": meta.get("state") or o.get("state"), "done": o.get("done")}
    reponses = (((o.get("response") or {}).get("inlinedResponses") or {}).get("inlinedResponses") or []) if isinstance(o.get("response"), dict) else []
    usages = []
    for x in reponses if isinstance(reponses, list) else []:
        rep = x.get("response") if isinstance(x, dict) else None
        if isinstance(rep, dict):
            u = rep.get("usageMetadata") if isinstance(rep.get("usageMetadata"), dict) else {}
            usages.append({"modele_servi": rep.get("modelVersion"),
                           **{k: v for k, v in u.items() if isinstance(v, (int, float))}})
        elif isinstance(x, dict) and "error" in x:
            usages.append({"erreur": str(x.get("error"))[:200]})
    if usages:
        garde["reponses"] = usages
    return {k: v for k, v in garde.items() if v is not None}


def fabriquer_gestionnaire(cle, amont, modeles, compteur, journal, verrou_journal, mandataire, contexte_tls, delai_amont_s,
                           variable_cle, max_requetes_par_lot=MAX_REQUETES_PAR_LOT_DEFAUT):
    parties = valider_amont(amont)
    modeles = frozenset(modeles)
    etat_fixe = {"version": VERSION, "amont": amont, "modeles": sorted(modeles), "mandataire": bool(mandataire),
                 "variable_cle_encore_presente": None}

    def ecrire_journal(entree):
        if journal is None:
            return
        ligne = json.dumps(entree, ensure_ascii=False, sort_keys=True)
        assert cle not in ligne, "la clé ne s'écrit jamais"  # garde-fou ; le texte est exclu par construction
        with verrou_journal:
            with open(journal, "a", encoding="utf-8") as f:
                f.write(ligne + "\n")

    def maintenant():
        return datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="milliseconds")

    class Gestionnaire(BaseHTTPRequestHandler):
        protocol_version = "HTTP/1.1"
        server_version = "RelaisGemini/4"
        sys_version = ""

        def log_message(self, format, *args):  # noqa: A002 — signature imposée par la bibliothèque standard
            pass  # aucun journal implicite : il porterait les chemins (donc un éventuel ?key=) sur un terminal partagé

        def _repondre_json(self, statut, objet):
            corps = json.dumps(objet, ensure_ascii=False).encode("utf-8")
            self.send_response(statut)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(corps)))
            self.send_header("Connection", "close")
            self.end_headers()
            self.wfile.write(corps)
            self.close_connection = True

        def _refuser(self, statut, motif, methode, chemin_propre, modele=None):
            compteur.refuser()
            ecrire_journal({"quand_utc": maintenant(), "methode": methode, "chemin": chemin_propre, "modele": modele,
                            "statut": statut, "motif": motif})
            return self._repondre_json(statut, {"erreur": motif, "relais": VERSION})

        def do_GET(self):
            if urllib.parse.urlsplit(self.path).path == "/relais/etat":
                etat = dict(etat_fixe, variable_cle_encore_presente=variable_cle in os.environ, **compteur.etat())
                return self._repondre_json(200, etat)
            chemin_propre, lot, action = chemin_sans_cle(self.path)
            if action == "releve_lot":
                return self._relayer_lot("GET", chemin_propre, lot, action)
            return self._refuser(403, "chemin non relayé", "GET", chemin_propre or "[chemin refusé]")

        def _relayer_lot(self, methode, chemin_propre, lot, action):
            """v4 : relevé (GET) ou annulation (POST :cancel) d'un lot créé par ce relais ; corps vide vers l'amont."""
            debut = time.time()
            motif = compteur.admettre_releve(lot, annulation=(action == "annule_lot"))
            if motif:
                ecrire_journal({"quand_utc": maintenant(), "methode": methode, "chemin": chemin_propre, "action": action,
                                "statut": motif[0], "motif": motif[1]})
                return self._repondre_json(motif[0], {"erreur": motif[1], "relais": VERSION})
            if methode == "POST" and self.headers.get("content-length"):
                self.rfile.read(int(self.headers["content-length"] or 0))
            en_tetes = {"x-goog-api-key": cle, "Accept-Encoding": "identity", "Host": parties.netloc, "Connection": "close",
                        "Content-Length": "0" if methode == "POST" else None}
            en_tetes = {k: v for k, v in en_tetes.items() if v is not None}
            try:
                statut, entetes_amont, brut = appel_amont(parties, mandataire, contexte_tls, delai_amont_s, methode,
                                                          chemin_propre, b"" if methode == "POST" else None, en_tetes)
            except (OSError, http.client.HTTPException, ssl.SSLError) as erreur:
                compteur.conclure(502, 0)
                motif = "amont injoignable : " + masquer(type(erreur).__name__, cle)
                ecrire_journal({"quand_utc": maintenant(), "duree_s": round(time.time() - debut, 3), "methode": methode,
                                "chemin": chemin_propre, "action": action, "statut": 502, "motif": motif})
                return self._repondre_json(502, {"erreur": motif, "relais": VERSION})
            if len(brut) > TAILLE_MAX_REPONSE:
                compteur.conclure(502, len(brut))
                return self._repondre_json(502, {"erreur": "réponse de l'amont trop grande", "relais": VERSION})
            octets_recus = len(brut)
            masquees = brut.count(cle.encode("utf-8"))
            if masquees:
                brut = brut.replace(cle.encode("utf-8"), "[clé]".encode("utf-8"))
            compteur.conclure(statut, octets_recus)
            ecrire_journal({"quand_utc": maintenant(), "duree_s": round(time.time() - debut, 3), "methode": methode,
                            "chemin": chemin_propre, "action": action, "statut_amont": statut, "octets_reponse": octets_recus,
                            **resume_lot(brut), **({"cle_masquee_dans_reponse": masquees} if masquees else {})})
            self.send_response(statut)
            self.send_header("Content-Type", "application/json; charset=UTF-8")
            self.send_header("Content-Length", str(len(brut)))
            self.send_header("Connection", "close")
            self.end_headers()
            try:
                self.wfile.write(brut)
                self.wfile.flush()
            except OSError:
                pass
            self.close_connection = True

        def do_POST(self):
            return self._relayer()

        def _autre_methode(self):
            return self._refuser(403, f"méthode {self.command} non relayée", self.command, "[chemin refusé]")

        do_PUT = do_DELETE = do_PATCH = do_HEAD = do_OPTIONS = _autre_methode

        def _relayer(self):
            debut = time.time()
            chemin_propre, modele, action = chemin_sans_cle(self.path)
            if chemin_propre is None or action == "releve_lot":
                return self._refuser(403, "chemin non relayé (generateContent, countTokens, batchGenerateContent de "
                                     "/v1beta/models, annulation d'un lot du relais seulement)", "POST", "[chemin refusé]")
            if action == "annule_lot":
                return self._relayer_lot("POST", chemin_propre, modele, action)
            if modele not in modeles:
                return self._refuser(403, "modèle hors de la liste blanche du relais", "POST", chemin_propre, modele)
            if "content-length" not in self.headers or self.headers.get("transfer-encoding"):
                return self._refuser(411, "Content-Length requis (aucun corps en morceaux)", "POST", chemin_propre, modele)
            try:
                longueur = int(self.headers["content-length"])
                if longueur < 0:
                    raise ValueError
            except ValueError:
                return self._refuser(411, "Content-Length invalide", "POST", chemin_propre, modele)
            corps_lu = None
            if action == "batchGenerateContent":  # v4 : contenu du lot borné avant tout compte et tout envoi
                if longueur > compteur.max_octets_corps:  # taille vérifiée avant de lire le corps
                    return self._refuser(429, f"corps de {longueur} octets au-dessus de --max-octets-corps", "POST",
                                         chemin_propre, modele)
                corps_lu = self.rfile.read(longueur) if longueur else b""
                refus_contenu = motif_contenu_lot(corps_lu, modele, max_requetes_par_lot)
                if refus_contenu:
                    return self._refuser(403, refus_contenu, "POST", chemin_propre, modele)
            motif = compteur.admettre_lot() if action == "batchGenerateContent" else None  # v4
            motif = motif or compteur.admettre(longueur)
            if motif:
                ecrire_journal({"quand_utc": maintenant(), "methode": "POST", "chemin": chemin_propre, "modele": modele,
                                "octets_corps": longueur, "statut": 429, "motif": motif})
                return self._repondre_json(429, {"erreur": motif, "relais": VERSION, **compteur.etat()})
            corps = corps_lu if corps_lu is not None else (self.rfile.read(longueur) if longueur else b"")
            en_tetes = {k: v for k, v in self.headers.items() if k.lower() not in EN_TETES_NON_RELAYES}
            en_tetes["x-goog-api-key"] = cle
            en_tetes["Accept-Encoding"] = "identity"
            en_tetes["Host"] = parties.netloc
            en_tetes["Content-Length"] = str(len(corps))
            en_tetes["Connection"] = "close"
            statut, octets_recus, garde = None, 0, {}
            try:
                if parties.scheme == "https":
                    if mandataire:
                        hote_m, port_m, en_tetes_tunnel = mandataire
                        connexion = http.client.HTTPSConnection(hote_m, port_m, context=contexte_tls, timeout=delai_amont_s)
                        connexion.set_tunnel(parties.hostname, parties.port or 443, headers=en_tetes_tunnel)
                    else:
                        connexion = http.client.HTTPSConnection(parties.hostname, parties.port or 443, context=contexte_tls,
                                                                timeout=delai_amont_s)
                else:
                    connexion = http.client.HTTPConnection(parties.hostname, parties.port or 80, timeout=delai_amont_s)
                try:
                    connexion.request("POST", chemin_propre, body=corps, headers=en_tetes)
                    reponse = connexion.getresponse()
                    brut = reponse.read(TAILLE_MAX_REPONSE + 1)
                finally:
                    connexion.close()
            except (OSError, http.client.HTTPException, ssl.SSLError) as erreur:
                compteur.conclure(502, 0)
                motif = "amont injoignable : " + masquer(type(erreur).__name__, cle)
                ecrire_journal({"quand_utc": maintenant(), "duree_s": round(time.time() - debut, 3), "methode": "POST",
                                "chemin": chemin_propre, "modele": modele, "octets_corps": len(corps), "statut": 502,
                                "motif": motif})
                return self._repondre_json(502, {"erreur": motif, "relais": VERSION})
            if len(brut) > TAILLE_MAX_REPONSE:
                compteur.conclure(502, len(brut))
                motif = f"réponse de l'amont au-dessus de {TAILLE_MAX_REPONSE} octets : non relayée"
                ecrire_journal({"quand_utc": maintenant(), "duree_s": round(time.time() - debut, 3), "methode": "POST",
                                "chemin": chemin_propre, "modele": modele, "octets_corps": len(corps), "statut": 502,
                                "statut_amont": reponse.status, "motif": motif})
                return self._repondre_json(502, {"erreur": motif, "relais": VERSION})
            statut, octets_recus = reponse.status, len(brut)
            # v2 : la vraie clé ne sort jamais dans le corps relayé ; Content-Length recalculé sur ce corps ; le journal lit
            # le corps masqué (en v1, un `modelVersion` qui portait la clé faisait échouer le garde-fou du journal)
            masquees = brut.count(cle.encode("utf-8"))
            if masquees:
                brut = brut.replace(cle.encode("utf-8"), "[clé]".encode("utf-8"))
            garde = usage_d_une_reponse(brut)
            if action == "batchGenerateContent":  # v4 : le lot créé est retenu ; seuls ses relevés seront relayés
                garde.update(resume_lot(brut))
                if statut == 200 and isinstance(garde.get("lot"), str) and MOTIF_LOT.match("/v1beta/" + garde["lot"]):
                    compteur.retenir_lot(garde["lot"])
            if masquees:
                garde["cle_masquee_dans_reponse"] = masquees
            self.send_response(statut)
            for k, v in reponse.getheaders():
                if k.lower() in EN_TETES_NON_RELAYES or k.lower() in ("content-length", "transfer-encoding",
                                                                      "content-encoding"):
                    continue
                self.send_header(k, masquer(v, cle))
            self.send_header("Content-Length", str(len(brut)))
            self.send_header("Connection", "close")
            self.end_headers()
            try:
                self.wfile.write(brut)
                self.wfile.flush()
            except OSError:
                pass  # client parti : l'appel est compté quand même (l'amont l'a servi)
            self.close_connection = True
            compteur.conclure(statut, octets_recus)
            ecrire_journal({"quand_utc": maintenant(), "duree_s": round(time.time() - debut, 3), "methode": "POST",
                            "chemin": chemin_propre, "modele": modele, "action": action, "octets_corps": len(corps),
                            "statut_amont": statut, "octets_reponse": octets_recus, **garde})

    return Gestionnaire


def contexte_tls_de(environnement):
    """Certificats : `SSL_CERT_FILE` de l'environnement s'il est posé, sinon ceux du système."""
    ca = environnement.get("SSL_CERT_FILE")
    if ca and not os.path.isfile(ca):
        raise RelaisInvalide(f"SSL_CERT_FILE introuvable : {ca}")
    return ssl.create_default_context(cafile=ca) if ca else ssl.create_default_context()


def servir(port, cle, amont, modeles, max_appels, max_octets_corps, journal=None, pret=None, environnement=None,
           delai_amont_s=DELAI_AMONT_DEFAUT_S, variable_cle=VARIABLE_CLE_DEFAUT, max_lots=MAX_LOTS_DEFAUT,
           max_releves=MAX_RELEVES_DEFAUT, max_annulations=MAX_ANNULATIONS_DEFAUT,
           max_requetes_par_lot=MAX_REQUETES_PAR_LOT_DEFAUT):
    """Sert jusqu'à l'arrêt du processus ; `pret` (événement) est levé avec l'adresse effective dans `pret.url`."""
    environnement = os.environ if environnement is None else environnement
    if variable_cle in environnement:
        raise RelaisInvalide(f"la variable {variable_cle} doit être effacée avant de servir")
    parties = valider_amont(amont)
    mandataire = mandataire_de(environnement) if parties.scheme == "https" else None
    contexte = contexte_tls_de(environnement) if parties.scheme == "https" else None
    compteur = Compteur(max_appels, max_octets_corps, max_lots, max_releves, max_annulations)
    gestionnaire = fabriquer_gestionnaire(cle, amont, modeles, compteur, journal, threading.Lock(), mandataire, contexte,
                                          delai_amont_s, variable_cle, max_requetes_par_lot)
    serveur = ThreadingHTTPServer((HOTE, port), gestionnaire)
    serveur.daemon_threads = True
    url = f"http://{HOTE}:{serveur.server_address[1]}"
    if pret is not None:
        pret.url = url
        pret.set()
    print(f"relais prêt sur {url} (amont {amont}, modèles {','.join(sorted(modeles))}, max-appels {max_appels}, "
          f"max-octets-corps {max_octets_corps}, mandataire {'oui' if mandataire else 'non'}, max-lots {max_lots}, "
          f"max-releves {max_releves})", flush=True)
    try:
        serveur.serve_forever()
    finally:
        serveur.server_close()
    return url


def analyseur():
    a = argparse.ArgumentParser(prog="relais_gemini_v4",
                                description="Relais Gemini local : la commande d'Argon n'a aucune clé.")
    a.add_argument("--port", type=int, default=PORT_DEFAUT, help="0 : port libre choisi par le système (essais)")
    a.add_argument("--amont", default=AMONT_DEFAUT, help="https, ou http vers la boucle locale (essais)")
    a.add_argument("--variable-cle", default=VARIABLE_CLE_DEFAUT,
                   help="variable de l'environnement du relais qui porte la clé ; effacée après lecture")
    a.add_argument("--modele", action="append", default=None, help="modèle permis (répétable) ; défaut gemini-4-argon")
    a.add_argument("--max-appels", type=int, default=MAX_APPELS_DEFAUT, help="appels relayés au plus ; au-delà : 429")
    a.add_argument("--max-octets-corps", type=int, default=MAX_OCTETS_CORPS_DEFAUT,
                   help="taille maximale du corps d'un appel ; au-delà : 429 sans envoi")
    a.add_argument("--delai-amont-s", type=float, default=DELAI_AMONT_DEFAUT_S, help="délai d'un appel à l'amont")
    a.add_argument("--max-lots", type=int, default=MAX_LOTS_DEFAUT, help="v4 : créations de lot au plus")
    a.add_argument("--max-releves", type=int, default=MAX_RELEVES_DEFAUT, help="v4 : relevés de lot au plus")
    a.add_argument("--max-annulations", type=int, default=MAX_ANNULATIONS_DEFAUT, help="v4 : annulations de lot au plus")
    a.add_argument("--max-requetes-par-lot", type=int, default=MAX_REQUETES_PAR_LOT_DEFAUT,
                   help="v4 : requêtes en ligne au plus dans un lot (1 par défaut)")
    a.add_argument("--journal", help="journal des appels (JSON par ligne : jamais la clé, jamais le texte)")
    return a


def principal(argv=None):
    args = analyseur().parse_args(argv)
    try:
        cle = lire_cle(os.environ, args.variable_cle)
        if args.max_appels < 0 or args.max_octets_corps < 0 or args.max_lots < 0 or args.max_releves < 0 \
                or args.max_annulations < 0 or args.max_requetes_par_lot < 1:
            raise RelaisInvalide("--max-appels et --max-octets-corps : entiers positifs ou nuls requis")
        if not (args.delai_amont_s > 0):
            raise RelaisInvalide("--delai-amont-s : strictement positif requis")
        modeles = args.modele or list(MODELES_DEFAUT)
        for m in modeles:
            if not re.fullmatch(r"[A-Za-z0-9._-]+", m):
                raise RelaisInvalide(f"--modele : nom invalide {m!r}")
        servir(args.port, cle, args.amont, modeles, args.max_appels, args.max_octets_corps, args.journal,
               delai_amont_s=args.delai_amont_s, variable_cle=args.variable_cle, max_lots=args.max_lots,
               max_releves=args.max_releves, max_annulations=args.max_annulations,
               max_requetes_par_lot=args.max_requetes_par_lot)
    except RelaisInvalide as erreur:
        print(f"erreur : {erreur}", file=sys.stderr)
        return 2
    except KeyboardInterrupt:
        return 0
    return 0


if __name__ == "__main__":
    sys.exit(principal())
