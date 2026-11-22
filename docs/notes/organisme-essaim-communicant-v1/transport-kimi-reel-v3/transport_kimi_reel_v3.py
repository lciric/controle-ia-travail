#!/usr/bin/env python3
"""Transport réel vers Kimi (Moonshot, « Chat Completions » en flux) pour `adaptateur_fournisseur_v1` — v3.
Bibliothèque standard seule (`http.client`). Écrit et éprouvé contre des serveurs locaux seulement ; aucun appel réel.

v3 = v2 (`transport_kimi_reel_v2.py`, gardée sans modification) avec un seul changement, demandé par la vérification de la
v2 (`transport-kimi-reel-v2/verification-v1/`) : la coupure par le nombre de morceaux prend une marge, **au-delà de
2 × `max_tokens` + 8 morceaux non vides** (au lieu de `max_tokens`), pour qu'un découpage sous le jeton par Kimi ne coupe
pas à tort avant la lecture de l'usage (H2 perdue) ; la limite en octets (12 × `max_tokens`) reste la garde principale.
Le texte ci-dessous est celui de la v2, sauf ce point.

La v2 reprend la v1 (`transport_kimi_reel_v1.py`, gardée sans modification) et ferme les points de sa contre-lecture
(`transport-kimi-reel-v1/contre-lecture-v1/`, N1 à N20) :

Envoi
- une connexion neuve par appel, d'une classe qui compte chaque `putrequest` (mesure, jamais déclaration) ; une connexion
  d'une autre classe est refusée sans envoi ; mesure > 1 ⇒ `AnomalieReponse` avec `envois` = mesure ;
- `set_debuglevel(0)` sur chaque connexion, et refus avant l'envoi si `http.client.HTTPConnection.debuglevel` ≠ 0 (N12) ;
- refus avant l'envoi si une méthode de `http.client.HTTPConnection`, `HTTPSConnection`, `HTTPResponse` ou de
  `ssl.SSLSocket` n'a plus son code d'origine (fichier de la bibliothèque), ou si `socket.socket` porte un `send`/`sendall`
  remplacé (N15, en partie : un envoi doublé plus bas que ces couches reste visible au seul serveur) ;
- **configuration figée** à la construction : toute affectation d'attribut ensuite est refusée (sauf compteurs et
  diagnostic, et les délais par `regler_delais`, validés) ; empreinte de la configuration vérifiée avant chaque appel ;
  amont revalidé dans `_connexion` ; contexte TLS vérifié (`CERT_REQUIRED`, nom d'hôte) (N13) ;
- constantes du module comparées à leurs valeurs littérales avant chaque appel (N14) ; l'adaptateur strict v2 compare en
  plus le code de chaque fonction et méthode du module à celui de son fichier, empreinté ;
- corps en liste blanche : `model`, un message `user`, `max_tokens` **et** `max_completion_tokens` (même valeur ; la
  documentation donne le premier « deprecated, please refer to max_completion_tokens », `api_chat.md` l. 1077-1081 ; le
  premier a été honoré à l'essai du 30 octobre), `stream`, `stream_options.include_usage` ; `champs_max` permet de n'en
  garder qu'un (réglage figé) ;
- filtre du corps : identifiant de session, UUID, lien de session ou d'artefact, adresse électronique, noms interdits
  après normalisation (NFKD sans diacritiques, pliage de casse, homoglyphes cyrilliques et grecs courants, caractères
  invisibles retirés) (N16) ;
- 407 du mandataire (tunnel refusé) : fatal (N18).

Lecture du flux
- **usage** : un seul `usage` non nul est admis, et seulement **au dernier morceau avant `[DONE]`, à `choices` vide**
  (forme documentée, `api_chat.md` l. 216 et 1176-1184) ; un `usage` non nul ailleurs, deux `usage`, ou un `usage` dans un
  choix ⇒ `usage = None` (réserve entière, arrêt 16) avec le motif (N5, N6) ;
- champs exigés : `prompt_tokens`, `completion_tokens`, `total_tokens`, `completion_tokens_details.reasoning_tokens`
  (entiers ≥ 0) ; absent ⇒ `usage = None`, jamais zéro ; excédent de `total_tokens` ajouté à la sortie ;
- **coupure côté client** dès que la sortie lue dépasse `max_tokens` (au cas où l'amont l'ignore) : plus de 2 × `max_tokens`
  + 8 morceaux non vides (v3 : marge contre un découpage sous le jeton), ou plus de 12 × `max_tokens` octets de texte ⇒
  connexion fermée, `AnomalieReponse` (réserve, arrêt 16) (N10) ;
- texte rendu de plus de 12 octets par jeton de sortie déclaré ⇒ `usage = None` ;
- modèle servi comparé à chaque morceau qui en porte un ; écart ⇒ lecture arrêtée, l'adaptateur arrête la course ;
- **masque d'abord** : la clé est retirée de tout champ rendu par l'amont (identifiant, modèle, motif d'erreur, en-têtes,
  contenu, réflexion, chaînes de l'usage) **avant** toute troncature (N11) ;
- diagnostic (pour le journal de la fumée, B1) : `usage_brut` (chaque `usage` non nul reçu, entier, imbriqué compris,
  masqué), `usage_refuse` (motif), `en_tetes_id` (en-têtes d'identifiant de requête de l'amont, s'il en rend), `id_reponse`.

Erreurs : 408, 409, 425, 429, 5xx, coupure, flux sans `[DONE]`, événement d'erreur, délais ⇒ `ErreurFournisseur` ;
autre statut (dont 3xx, 4xx, 407 du mandataire) ⇒ `ErreurTransportFatale` ; requête hors contrat ⇒ `ConfigurationRefusee`
sans envoi. Clé : lue par son nom, retirée de l'environnement, gardée dans un `bytearray` remis à zéro par `fermer()`.
Limites déclarées (code hostile dans le même processus) : `object.__setattr__`, `ctypes`, un `socket` remplacé en C, une
réécriture conjointe du fichier et de son empreinte ; seul le budget du projet chez Kimi les borne.
"""
import base64
import hashlib
import http.client
import json
import os
import re
import socket
import ssl
import time
import unicodedata
import urllib.parse

import adaptateur_fournisseur_v1 as A

VERSION = "transport-kimi-reel-v3"
MODELE = "kimi-k3.1-pro"
AMONT_DEFAUT = "https://api.moonshot.ai"
CHEMIN = "/v1/chat/completions"
VARIABLE_CLE_DEFAUT = "KIMI_API_KEY"
PLAFOND_MAX_TOKENS = 24000
DELAI_SILENCE_DEFAUT_S = 600.0
DELAI_TOTAL_DEFAUT_S = 1800.0
TAILLE_MAX_DEFAUT = 32_000_000
STATUTS_RELANCABLES = (408, 409, 425, 429, 500, 502, 503, 504)
HOTES_LOCAUX = ("127.0.0.1", "localhost", "::1")
AGENT = "transport-pilote/2"
OCTETS_PAR_JETON_SORTIE_MAX = 12
CHAMPS_MAX_PERMIS = ("max_tokens", "max_completion_tokens")
MOTIFS_SOURCES = (
    r"session_[0-9A-Za-z]{8,}",
    r"[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}",
    r"claude\.ai/(code|chat|artifact)",
    r"[A-Za-z0-9._%+-]{1,64}@[A-Za-z0-9-]{1,63}(\.[A-Za-z0-9-]{1,63}){0,8}\.[A-Za-z]{2,24}",
)
NOMS_INTERDITS_DEFAUT = ("lazar", "lciric", "ciric")
HOMOGLYPHES = {"а": "a", "е": "e", "о": "o", "р": "p", "с": "c", "у": "y", "х": "x", "і": "i", "ј": "j", "ѕ": "s",
               "ԁ": "d", "ӏ": "l", "к": "k", "м": "m", "н": "h", "т": "t", "в": "b", "ı": "i", "α": "a", "ο": "o",
               "ρ": "p", "ε": "e", "κ": "k", "ν": "v", "τ": "t", "ι": "i", "ζ": "z", "ɡ": "g", "ⅼ": "l", "ł": "l",
               "đ": "d", "ø": "o"}
INVISIBLES = ("​", "‌", "‍", "⁠", "﻿", "­")
EN_TETES_ID = ("x-request-id", "request-id", "msh-request-id", "x-msh-request-id", "x-trace-id", "msh-trace-id",
               "msh-request-timestamp", "msh-request-signature")
FRAGMENT_CLE = 8
MODIFIABLES = ("envois", "dernier_diagnostic", "derniere_reponse", "_cle")


def _constantes_intactes():
    """Valeurs littérales (dans le code, non dans les globales) : une globale réécrite est vue avant l'envoi."""
    return (MODELE == "kimi-k3.1-pro" and CHEMIN == "/v1/chat/completions" and PLAFOND_MAX_TOKENS == 24000
            and STATUTS_RELANCABLES == (408, 409, 425, 429, 500, 502, 503, 504) and HOTES_LOCAUX == ("127.0.0.1", "localhost", "::1")
            and OCTETS_PAR_JETON_SORTIE_MAX == 12 and CHAMPS_MAX_PERMIS == ("max_tokens", "max_completion_tokens")
            and AGENT == "transport-pilote/2" and FRAGMENT_CLE == 8 and len(MOTIFS_SOURCES) == 4 and MOTIFS_SOURCES[0] == r"session_[0-9A-Za-z]{8,}")


def _code_d_origine(cls, module):
    for n, f in vars(cls).items():
        f = getattr(f, "__func__", f)
        code = getattr(f, "__code__", None)
        if code is not None and os.path.realpath(code.co_filename) != os.path.realpath(module.__file__):
            return n
    return None


def http_client_intact():
    """Rend None si `http.client`, `ssl.SSLSocket` et `socket.socket` ont leur code d'origine, sinon le motif."""
    if http.client.HTTPConnection.debuglevel != 0 or http.client.HTTPSConnection.debuglevel != 0:
        return "debuglevel de http.client non nul"
    for cls in (http.client.HTTPConnection, http.client.HTTPSConnection, http.client.HTTPResponse):
        n = _code_d_origine(cls, http.client)
        if n:
            return f"http.client.{cls.__name__}.{n} remplacé"
    n = _code_d_origine(ssl.SSLSocket, ssl)
    if n:
        return f"ssl.SSLSocket.{n} remplacé"
    if any(n in vars(socket.socket) for n in ("send", "sendall", "sendto", "connect")) or _code_d_origine(socket.socket, socket):
        return "socket.socket remplacé"
    return None


class ErreurTransportFatale(Exception):
    """Réponse d'erreur non relançable : comptée à la réserve, arrêt 17."""


def _entier(x):
    return isinstance(x, int) and not isinstance(x, bool)


def _court(texte, n=80):
    return re.sub(r"[^A-Za-z0-9_ .:/=-]", "?", str(texte))[:n]


def normaliser(texte):
    t = unicodedata.normalize("NFKD", str(texte))
    t = "".join(c for c in t if not unicodedata.combining(c) and c not in INVISIBLES)
    return t.casefold().translate(str.maketrans(HOMOGLYPHES))


class _Compteur:
    def putrequest(self, *a, **kw):
        self._compteur_envois[0] += 1
        return super().putrequest(*a, **kw)


class ConnexionHTTPComptee(_Compteur, http.client.HTTPConnection):
    pass


class ConnexionHTTPSComptee(_Compteur, http.client.HTTPSConnection):
    pass


CLASSES_DE_CONNEXION = (ConnexionHTTPComptee, ConnexionHTTPSComptee)


def _valider_amont(amont):
    p = urllib.parse.urlsplit(amont)
    if p.path not in ("", "/") or p.query or p.fragment or p.username or p.password or not p.hostname:
        raise A.ConfigurationRefusee("amont : schéma et hôte seulement")
    if not (p.scheme == "https" or (p.scheme == "http" and p.hostname in HOTES_LOCAUX)):
        raise A.ConfigurationRefusee("amont : https, ou http vers la boucle locale seulement")
    return p


class TransportKimiReel:
    relances_internes = 0
    repli_modele = None

    def __init__(self, amont=AMONT_DEFAUT, variable_cle=VARIABLE_CLE_DEFAUT, environ=None, effacer_variable=True,
                 delai_silence_s=DELAI_SILENCE_DEFAUT_S, delai_total_s=DELAI_TOTAL_DEFAUT_S, taille_max_octets=TAILLE_MAX_DEFAUT,
                 noms_interdits=NOMS_INTERDITS_DEFAUT, plafond_max_tokens=PLAFOND_MAX_TOKENS, champs_max=CHAMPS_MAX_PERMIS):
        env = os.environ if environ is None else environ
        p = _valider_amont(amont)
        self._valider_delais(delai_silence_s, delai_total_s)
        if not _entier(plafond_max_tokens) or not 0 < plafond_max_tokens <= PLAFOND_MAX_TOKENS:
            raise A.ConfigurationRefusee("plafond de max_tokens hors bornes")
        champs_max = tuple(champs_max)
        if not champs_max or len(set(champs_max)) != len(champs_max) or not set(champs_max) <= set(CHAMPS_MAX_PERMIS):
            raise A.ConfigurationRefusee("champs_max : max_tokens et/ou max_completion_tokens")
        cle = env.get(variable_cle) or ""
        if effacer_variable:
            env.pop(variable_cle, None)
        cle = cle.strip()
        if not cle or any(c in cle for c in "\r\n\t ") or not cle.isascii() or not cle.isprintable():
            del cle
            raise A.ConfigurationRefusee(f"clé absente ou mal formée dans la variable {variable_cle}")
        self._cle = bytearray(cle.encode("ascii"))
        del cle
        self.amont, self._p = amont, p
        self.delai_silence_s, self.delai_total_s = float(delai_silence_s), float(delai_total_s)
        self.taille_max = int(taille_max_octets)
        self.plafond_max_tokens = plafond_max_tokens
        self.champs_max = champs_max
        self.noms_interdits = tuple(normaliser(n) for n in noms_interdits)
        self._mandataire = self._lire_mandataire(env) if p.scheme == "https" else None
        self._tls = None
        if p.scheme == "https":
            ca = env.get("SSL_CERT_FILE")
            if ca and not os.path.isfile(ca):
                raise A.ConfigurationRefusee("SSL_CERT_FILE introuvable")
            self._tls = ssl.create_default_context(cafile=ca) if ca else ssl.create_default_context()
        self.envois = 0
        self.dernier_diagnostic = None
        self.derniere_reponse = None
        self._empreinte = self._empreinte_config()
        self._fige = True

    # --- configuration figée --------------------------------------------------------------------------------------
    def __setattr__(self, nom, valeur):
        if self.__dict__.get("_fige") and nom not in MODIFIABLES:
            raise A.ConfigurationRefusee(f"attribut {nom} figé après la construction")
        object.__setattr__(self, nom, valeur)

    def __delattr__(self, nom):
        raise A.ConfigurationRefusee(f"attribut {nom} figé")

    @staticmethod
    def _valider_delais(silence, total):
        if not (0 < float(silence) <= 600 and 0 < float(total) <= 7200 and float(silence) <= float(total)):
            raise A.ConfigurationRefusee("délais hors bornes")

    def regler_delais(self, delai_silence_s, delai_total_s):
        """Seul changement permis après la construction : les délais, validés ; l'empreinte est recalculée."""
        self._valider_integrite()
        self._valider_delais(delai_silence_s, delai_total_s)
        object.__setattr__(self, "delai_silence_s", float(delai_silence_s))
        object.__setattr__(self, "delai_total_s", float(delai_total_s))
        object.__setattr__(self, "_empreinte", self._empreinte_config())

    def _empreinte_config(self):
        m = None
        if self._mandataire:
            h, port, en_tetes = self._mandataire
            m = [h, port, hashlib.sha256(json.dumps(en_tetes, sort_keys=True).encode()).hexdigest()]
        cfg = [self.amont, list(self._p), self.delai_silence_s, self.delai_total_s, self.taille_max, self.plafond_max_tokens,
               list(self.champs_max), list(self.noms_interdits), m, self._tls is None, type(self).__qualname__]
        return hashlib.sha256(json.dumps(cfg, sort_keys=True).encode()).hexdigest()

    def _valider_integrite(self):
        """Avant chaque envoi : constantes, configuration, attributs, TLS, http.client. Refus sans envoi."""
        if not _constantes_intactes():
            raise A.ConfigurationRefusee("constante du module réécrite")
        attendus = {"_cle", "amont", "_p", "delai_silence_s", "delai_total_s", "taille_max", "plafond_max_tokens", "champs_max",
                    "noms_interdits", "_mandataire", "_tls", "envois", "dernier_diagnostic", "derniere_reponse", "_empreinte", "_fige"}
        if set(vars(self)) != attendus:
            raise A.ConfigurationRefusee("attributs d'instance ajoutés ou retirés")
        if _valider_amont(self.amont) != self._p or self._empreinte_config() != self._empreinte:
            raise A.ConfigurationRefusee("configuration du transport modifiée après la construction")
        if self._tls is not None and (self._tls.verify_mode != ssl.CERT_REQUIRED or not self._tls.check_hostname):
            raise A.ConfigurationRefusee("contexte TLS affaibli")
        motif = http_client_intact()
        if motif:
            raise A.ConfigurationRefusee(f"pile HTTP altérée : {motif}")

    # --- garde de la clé -------------------------------------------------------------------------------------------
    def __repr__(self):
        return f"<TransportKimiReel v2 {self.amont} envois={self.envois} clé=[masquée]>"

    __str__ = __repr__

    def __getstate__(self):
        raise TypeError("transport non sérialisable (clé)")

    def _masquer(self, texte):
        """Retire la clé entière, puis tout fragment d'au moins `FRAGMENT_CLE` caractères consécutifs de la clé (une clé
        tronquée ou coupée par l'amont reste masquée)."""
        texte = str(texte)
        if not self._cle:
            return texte
        k = self._cle.decode("ascii")
        texte = texte.replace(k, "[clé]")
        n = FRAGMENT_CLE
        if len(k) >= n and len(texte) >= n:
            grammes = {k[i:i + n] for i in range(len(k) - n + 1)}
            marque = bytearray(len(texte))
            for j in range(len(texte) - n + 1):
                if texte[j:j + n] in grammes:
                    marque[j:j + n] = b"\x01" * n
            if any(marque):
                morceaux, j = [], 0
                while j < len(texte):
                    if marque[j]:
                        while j < len(texte) and marque[j]:
                            j += 1
                        morceaux.append("[clé]")
                    else:
                        morceaux.append(texte[j])
                        j += 1
                texte = "".join(morceaux)
        del k
        return texte

    def _propre(self, texte, n=80):
        """Masque D'ABORD, puis tronque et filtre les caractères (N11)."""
        return _court(self._masquer(texte), n)

    def _masquer_arbre(self, x):
        if isinstance(x, str):
            return self._masquer(x)
        if isinstance(x, dict):
            return {self._masquer(k): self._masquer_arbre(v) for k, v in x.items()}
        if isinstance(x, list):
            return [self._masquer_arbre(v) for v in x]
        return x

    def fermer(self):
        for i in range(len(self._cle)):
            self._cle[i] = 0
        self._cle = bytearray()

    @staticmethod
    def _lire_mandataire(env):
        brut = env.get("HTTPS_PROXY") or env.get("https_proxy")
        if not brut:
            return None
        q = urllib.parse.urlsplit(brut if "://" in brut else "http://" + brut)
        if q.scheme != "http" or not q.hostname or not q.port:
            raise A.ConfigurationRefusee("HTTPS_PROXY : http://hôte:port attendu")
        en_tetes = {}
        if q.username is not None:
            jeton = base64.b64encode(f"{urllib.parse.unquote(q.username)}:{urllib.parse.unquote(q.password or '')}".encode()).decode()
            en_tetes["Proxy-Authorization"] = "Basic " + jeton
        return q.hostname, q.port, en_tetes

    def _connexion(self):
        p = _valider_amont(self.amont)
        if p != self._p:
            raise A.ConfigurationRefusee("amont modifié")
        t = self.delai_silence_s
        if p.scheme == "https":
            if self._mandataire:
                h, port, en_tetes = self._mandataire
                c = ConnexionHTTPSComptee(h, port, context=self._tls, timeout=t)
                c.set_tunnel(p.hostname, p.port or 443, headers=dict(en_tetes))
            else:
                c = ConnexionHTTPSComptee(p.hostname, p.port or 443, context=self._tls, timeout=t)
        else:
            c = ConnexionHTTPComptee(p.hostname, p.port or 80, timeout=t)
        c.set_debuglevel(0)
        return c

    # --- contrôle de la requête, sans envoi ---------------------------------------------------------------------------
    def corps_fil(self, requete):
        if not isinstance(requete, dict):
            raise A.ConfigurationRefusee("requête non dict")
        cles = set(requete)
        if not cles <= {"model", "messages", "max_tokens", "stream", "n"} or not {"model", "messages", "max_tokens"} <= cles:
            raise A.ConfigurationRefusee(f"champs de requête hors contrat : {_court(sorted(cles), 120)}")
        if requete["model"] != MODELE:
            raise A.ConfigurationRefusee(f"modèle demandé {self._propre(requete['model'])!r} ≠ {MODELE}")
        if requete.get("stream", False) is not False or requete.get("n", 1) != 1 or isinstance(requete.get("n", 1), bool):
            raise A.ConfigurationRefusee("stream ou n hors contrat (stream faux, n = 1 exigés)")
        mt = requete["max_tokens"]
        if not _entier(mt) or not 0 < mt <= self.plafond_max_tokens:
            raise A.ConfigurationRefusee(f"max_tokens {_court(mt)} hors de 1..{self.plafond_max_tokens}")
        m = requete["messages"]
        if not (isinstance(m, list) and len(m) == 1 and isinstance(m[0], dict) and set(m[0]) == {"role", "content"}
                and m[0]["role"] == "user" and isinstance(m[0]["content"], str) and m[0]["content"]):
            raise A.ConfigurationRefusee("messages : un seul message user, texte non vide")
        corps = {"model": MODELE, "messages": [{"role": "user", "content": m[0]["content"]}]}
        for champ in self.champs_max:
            corps[champ] = mt
        corps["stream"] = True
        corps["stream_options"] = {"include_usage": True}
        brut = json.dumps(corps, ensure_ascii=False, separators=(",", ":"))
        norme = normaliser(brut)
        for source in MOTIFS_SOURCES:
            if re.search(source, brut) or re.search(source, norme):
                raise A.ConfigurationRefusee("motif interdit dans le corps (session, UUID, lien ou adresse)")
        for nom in self.noms_interdits:
            if nom in norme:
                raise A.ConfigurationRefusee("nom de personne interdit dans le corps")
        return brut.encode("utf-8")

    # --- envoi ----------------------------------------------------------------------------------------------------
    def envoyer(self, requete):
        self._valider_integrite()
        corps = self.corps_fil(requete)
        if not self._cle:
            raise A.ConfigurationRefusee("transport fermé (clé effacée)")
        compteur = [0]
        self.derniere_reponse = None
        try:
            rep = self._envoyer_une_fois(corps, compteur, requete["max_tokens"])
        except BaseException as ex:
            self.envois += compteur[0]
            if compteur[0] > 1:
                an = A.AnomalieReponse(f"{compteur[0]} envois mesurés pour un appel (1 exigé)")
                an.envois = compteur[0]
                raise an from None
            if isinstance(ex, A.AnomalieReponse):
                ex.envois = max(1, compteur[0])
            raise
        self.envois += compteur[0]
        rep["tentatives"] = compteur[0]
        self.dernier_diagnostic["envois_mesures"] = compteur[0]
        self.derniere_reponse = rep
        return rep

    def _envoyer_une_fois(self, corps, compteur, mt):
        debut = time.monotonic()
        echeance = debut + self.delai_total_s
        diag = {"version": VERSION, "octets_corps": len(corps), "statut": None, "octets_reponse": 0, "morceaux": 0,
                "usage_place": None, "excedent_total_tokens": 0, "usage_brut": [], "usage_refuse": None, "en_tetes_id": {}}
        self.dernier_diagnostic = diag
        c = self._connexion()
        if type(c) not in CLASSES_DE_CONNEXION:
            raise A.ConfigurationRefusee("connexion d'une classe non comptée : refus sans envoi")
        c._compteur_envois = compteur
        try:
            try:
                c.putrequest("POST", CHEMIN, skip_accept_encoding=True)
                c.putheader("Content-Type", "application/json")
                c.putheader("Accept", "text/event-stream")
                c.putheader("Accept-Encoding", "identity")
                c.putheader("User-Agent", AGENT)
                c.putheader("Content-Length", str(len(corps)))
                c.putheader("Authorization", b"Bearer " + bytes(self._cle))
                c.endheaders(corps)
                rep = c.getresponse()
            except TimeoutError:
                raise A.ErreurFournisseur("délai de silence dépassé avant la réponse") from None
            except OSError as ex:
                m = self._masquer(str(ex))
                if "Tunnel connection failed" in m:
                    raise ErreurTransportFatale(f"mandataire : tunnel refusé ({_court(m.split(':', 1)[-1], 40)})") from None
                raise A.ErreurFournisseur(f"coupure avant la réponse ({type(ex).__name__})") from None
            except http.client.HTTPException as ex:
                raise A.ErreurFournisseur(f"coupure avant la réponse ({type(ex).__name__})") from None
            except ValueError:
                raise ErreurTransportFatale("en-tête refusé par http.client (message masqué)") from None
            diag["statut"] = rep.status
            for k, v in rep.getheaders():
                if k.lower() in EN_TETES_ID or "request-id" in k.lower():
                    diag["en_tetes_id"][self._propre(k.lower(), 40)] = self._propre(v, 120)
            if rep.status != 200:
                motif = self._motif_erreur(rep)
                if rep.status in STATUTS_RELANCABLES:
                    raise A.ErreurFournisseur(f"statut {rep.status} de l'amont ({motif})")
                raise ErreurTransportFatale(f"statut {rep.status} de l'amont ({motif})")
            if "text/event-stream" not in (rep.getheader("Content-Type") or ""):
                ex = A.AnomalieReponse("réponse 200 qui n'est pas un flux d'événements")
                ex.envois = 1
                raise ex
            return self._lire_flux(rep, echeance, diag, mt)
        finally:
            diag["duree_s"] = round(time.monotonic() - debut, 3)
            try:
                c.close()
            except OSError:
                pass

    def _motif_erreur(self, rep):
        try:
            brut = rep.read(65536)
            e = json.loads(brut.decode("utf-8", "replace")).get("error") or {}
            return self._propre(f"{e.get('type', '')} {e.get('code', '')}".strip() or "sans motif")
        except (OSError, http.client.HTTPException, ValueError, AttributeError):
            return "corps illisible"

    def _anomalie(self, motif):
        ex = A.AnomalieReponse(motif)
        ex.envois = 1
        return ex

    def _lire_flux(self, rep, echeance, diag, mt):
        contenu, raisonnement, fin, servi, taille, fini, premier, ident = [], [], None, None, 0, False, True, None
        usages = []          # (rang du morceau, usage, place)
        rang, non_vides, octets_texte = -1, 0, 0
        while True:
            if time.monotonic() > echeance:
                raise A.ErreurFournisseur("délai total dépassé (coupé côté client)")
            try:
                ligne = rep.readline(1_000_000)
            except TimeoutError:
                raise A.ErreurFournisseur("délai de silence dépassé pendant le flux") from None
            except (OSError, http.client.HTTPException) as ex:
                raise A.ErreurFournisseur(f"coupure en plein flux ({type(ex).__name__})") from None
            if not ligne:
                break
            taille += len(ligne)
            diag["octets_reponse"] = taille
            if taille > self.taille_max:
                raise self._anomalie(f"réponse au-delà de {self.taille_max} octets")
            ligne = ligne.strip()
            if not ligne.startswith(b"data:"):
                continue
            charge = ligne[5:].strip()
            if charge == b"[DONE]":
                fini = True
                break
            try:
                morceau = json.loads(charge.decode("utf-8"))
                if not isinstance(morceau, dict):
                    raise ValueError
            except (ValueError, UnicodeDecodeError):
                raise self._anomalie("morceau de flux illisible") from None
            rang += 1
            diag["morceaux"] += 1
            if morceau.get("error") is not None:
                e = morceau["error"] if isinstance(morceau["error"], dict) else {}
                raise A.ErreurFournisseur(f"événement d'erreur dans le flux ({self._propre(e.get('type', ''))})")
            m = morceau.get("model")
            if premier or m is not None:
                if m != MODELE:
                    diag["modele_servi"] = self._propre(m)
                    return {"model": self._propre(m), "usage": None, "choices": [{"message": {"content": ""}, "finish_reason": None}],
                            "diagnostic": diag}
                servi = m
            premier = False
            if ident is None and isinstance(morceau.get("id"), str):
                ident = self._propre(morceau["id"], 120)
            choix = morceau.get("choices")
            if morceau.get("usage") is not None:
                usages.append((rang, morceau["usage"], "racine" if choix == [] else "racine-avec-choix"))
            for ch in choix or []:
                if not isinstance(ch, dict):
                    continue
                d = ch.get("delta") or {}
                for champ, puits in (("content", contenu), ("reasoning_content", raisonnement)):
                    v = d.get(champ)
                    if isinstance(v, str) and v:
                        puits.append(v)
                        non_vides += 1
                        octets_texte += len(v.encode("utf-8"))
                if ch.get("finish_reason"):
                    fin = ch["finish_reason"]
                if ch.get("usage") is not None:
                    usages.append((rang, ch["usage"], "choix"))
            if non_vides > 2 * mt + 8 or octets_texte > OCTETS_PAR_JETON_SORTIE_MAX * mt:  # v3 : marge de morceaux
                diag["coupure_sortie"] = {"morceaux_non_vides": non_vides, "octets_texte": octets_texte, "max_tokens": mt}
                raise self._anomalie("sortie lue au-delà de max_tokens : coupure côté client (l'amont l'ignore)")
        if not fini:
            raise A.ErreurFournisseur("flux coupé avant [DONE]")
        diag["usage_brut"] = [{"rang": r, "place": p, "usage": self._masquer_arbre(u)} for r, u, p in usages]
        usage = None
        if not usages:
            diag["usage_refuse"] = "usage absent"
        elif len(usages) > 1:
            diag["usage_refuse"] = f"{len(usages)} usages non nuls dans le flux (un seul admis)"
        elif usages[0][2] != "racine" or usages[0][0] != rang:
            diag["usage_refuse"] = "usage hors du dernier morceau à choices vide"
        else:
            usage = self._completer_usage(usages[0][1], diag)
        if usage is not None:
            jetons = usage["completion_tokens"] + (usage.get("reasoning_tokens", 0) or 0)
            if octets_texte > OCTETS_PAR_JETON_SORTIE_MAX * max(jetons, 1):
                diag["usage_refuse"] = "texte rendu trop long pour la sortie déclarée (sous-compte présumé)"
                usage = None
        diag["octets_texte_rendu"] = octets_texte
        diag["morceaux_non_vides"] = non_vides
        message = {"role": "assistant", "content": self._masquer("".join(contenu))}
        if raisonnement:
            message["reasoning_content"] = self._masquer("".join(raisonnement))
        diag["modele_servi"] = servi
        diag["fin"] = self._propre(fin) if fin is not None else None
        diag["id_reponse"] = ident
        return {"id": ident, "model": servi, "usage": usage, "choices": [{"message": message, "finish_reason": fin}],
                "diagnostic": diag}

    @staticmethod
    def _completer_usage(usage, diag):
        """Copie, ou None si un champ exigé manque ou est négatif ; excédent de `total_tokens` ajouté en sortie."""
        if not isinstance(usage, dict):
            diag["usage_refuse"] = "usage non objet"
            return None
        u = json.loads(json.dumps(usage))
        det = u.get("completion_tokens_details")
        p, c, t = u.get("prompt_tokens"), u.get("completion_tokens"), u.get("total_tokens")
        r = u.get("reasoning_tokens", 0)
        if not (_entier(p) and _entier(c) and _entier(t) and isinstance(det, dict) and _entier(det.get("reasoning_tokens"))
                and (r is None or _entier(r))):
            diag["usage_refuse"] = "champ exigé absent (prompt, completion, total ou completion_tokens_details.reasoning_tokens)"
            return None
        r = r or 0
        if min(p, c, t, r, det["reasoning_tokens"]) < 0:
            diag["usage_refuse"] = "compte négatif"
            return None
        if t > p + c + r:
            diag["excedent_total_tokens"] = t - p - c - r
            u["reasoning_tokens"] = r + (t - p - c - r)
        diag["usage_numerique"] = {k: v for k, v in u.items() if _entier(v)}
        return u
