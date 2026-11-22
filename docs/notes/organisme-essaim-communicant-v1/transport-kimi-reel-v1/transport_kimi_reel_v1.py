#!/usr/bin/env python3
"""Transport réel vers Kimi (Moonshot, forme « Chat Completions ») pour `adaptateur_fournisseur_v1.AdaptateurChatCompletions`
— v1. Bibliothèque standard seule (`http.client`) : aucun kit client, donc **aucune relance cachée** par construction.
Écrit et éprouvé contre un faux serveur local seulement ; aucun appel réel n'a été fait avec ce fichier.

Contrat rempli (docstring de `adaptateur_fournisseur_v1.py`, exigences 1 à 5) :
- `relances_internes = 0`, `repli_modele = None` (attributs de classe, vrais : `http.client` ne relance jamais une requête,
  et `envoyer` ouvre une connexion neuve, fait **un seul** `request()`, puis la ferme) ;
- `envoyer(requete)` rend un dict `{"model": <modèle servi>, "usage": <usage du fournisseur ou None>, "choices": [...],
  "tentatives": n, "diagnostic": {...}}` ; `tentatives` est **mesuré**, jamais déclaré : chaque appel ouvre une connexion
  neuve d'une classe comptée (`ConnexionHTTPComptee` / `ConnexionHTTPSComptee`, qui comptent chaque `putrequest`) ;
  une connexion d'une autre classe est refusée sans envoi ; une mesure > 1 lève `AnomalieReponse` avec `envois` = mesure
  (le lanceur compte alors une réserve par envoi, arrêt 16) ; l'adaptateur exige 1 ;
- la classe exacte du transport et ses méthodes figées (`METHODES_FIGEES`) sont vérifiées par `adaptateur_kimi_strict_v1`,
  qui vérifie aussi l'empreinte du fichier de ce module ;
- modèle demandé = `kimi-k3.1-pro` seulement (constante `MODELE`) ; tout autre nom est refusé **sans envoi** ;
- `max_tokens` : celui de la requête de l'adaptateur (donc de la garde), entier dans 1..`PLAFOND_MAX_TOKENS` (24 000, le
  plafond absolu de `garde_pilote_essaim_v2`), envoyé tel quel dans le champ `max_tokens` (champ éprouvé par l'essai réel
  du 30 octobre 2026 : `completion_tokens` = 16 pour `max_tokens` = 16, réflexion comprise ; la documentation le dit
  « déprécié » au profit de `max_completion_tokens` : point à relever) ;
- corps envoyé = **liste blanche** : `model`, `messages` (un seul message `user`, texte en chaîne), `max_tokens`,
  `stream: true`, `stream_options: {"include_usage": true}`. Rien d'autre : ni `n` (absent du schéma de Kimi ; la requête
  de l'adaptateur doit porter `n == 1`, sinon refus), ni `user`, `safety_identifier`, `prompt_cache_key`,
  `prompt_cache_options` (le cache d'une heure est facturé 4 USD par million, au-dessus du prix d'entrée gelé),
  `reasoning_effort` (défaut du fournisseur), outils ; aucun identifiant de session ni nom de personne : le corps entier
  est passé aux motifs interdits (`MOTIFS_INTERDITS` et `noms_interdits`) avant l'envoi, refus sans envoi s'il y en a un ;
- **flux vers l'amont** (comme `relais_kimi_v3/v4` : une connexion muette est coupée par l'amont vers 300 s), réassemblé
  en une réponse entière ; `usage` = celui du dernier morceau qui en porte un (racine, sinon `choices[i].usage`) ;
- **réflexion** : rendue telle que le fournisseur la rend (`completion_tokens_details.reasoning_tokens`, ou
  `reasoning_tokens` au premier niveau) ; l'adaptateur l'ajoute à la sortie si elle est hors de `completion_tokens`.
  **Champ de réflexion exigé** : `completion_tokens_details.reasoning_tokens` (compris dans `completion_tokens` selon la
  documentation et l'essai réel du 30 octobre 2026), avec `prompt_tokens`, `completion_tokens`, `total_tokens` ; l'un
  d'eux absent ⇒ `usage = None` (réserve entière, arrêt 16), jamais zéro. Texte rendu (contenu + réflexion) de plus de
  12 octets par jeton de sortie déclaré ⇒ `usage = None` (sous-compte présumé).
  Complément du transport : si `total_tokens` dépasse `prompt_tokens + completion_tokens + reasoning_tokens` (premier
  niveau), l'excédent est **ajouté** à `reasoning_tokens` au premier niveau (donc compté en sortie, au prix fort) et noté
  au diagnostic (`excedent_total_tokens`) ;
- **modèle servi** : le `model` du premier morceau (et de tout morceau qui en porte un) est comparé au modèle demandé ; au
  premier écart (ou s'il manque au premier morceau), la lecture s'arrête, la connexion se ferme, et la réponse rendue
  porte le modèle servi avec `usage = None` : l'adaptateur lève `AnomalieReponse` (réserve, arrêt 16) ;
- **erreurs** (toutes après le début de l'envoi ; aucune n'est relancée ici) :
  - 408, 409, 425, 429, 500, 502, 503, 504, coupure de connexion, flux coupé avant `[DONE]`, événement `error` dans le
    flux, délai de silence ou délai total dépassé → `ErreurFournisseur` (échec compté à la réserve par le lanceur, qui
    seul décide d'une relance et la compte) ;
  - autre statut (400, 401, 402, 403, 404, 422…) → `ErreurTransportFatale` (comptée à la réserve, arrêt 17 : une clé
    refusée ne doit pas brûler le budget d'échecs) ;
  - 200 qui n'est pas un flux, réponse au-delà de `taille_max_octets`, morceau illisible → `AnomalieReponse` avec
    `envois = 1` (réserve, arrêt 16) ;
  - requête hors contrat (modèle, `max_tokens`, champs, motif interdit) → `ConfigurationRefusee` **sans envoi** (le lanceur
    la compte à la réserve, arrêt 17).
- **clé** : lue par son nom (`KIMI_API_KEY` par défaut) dans l'environnement à la construction, retirée de cet
  environnement (`effacer_variable=True`), gardée seulement dans un `bytearray` remis à zéro par `fermer()`. Jamais en
  argument, jamais dans un message d'erreur, un `repr`, un journal ou le diagnostic (tout message passe par `_masquer`).
  Limite de Python déclarée : l'en-tête est recopié en `bytes` immuables à chaque envoi (le ramasse-miettes les libère sans
  les effacer), et `/proc/<pid>/environ` garde le bloc initial de l'environnement tant que le processus vit (F-C7).
- délais : `delai_silence_s` (connexion et chaque lecture : délai de la prise) et `delai_total_s` (ouverture à `[DONE]`,
  vérifié entre deux lignes ; granularité : au plus `delai_silence_s` au-delà).
- mandataire : `HTTPS_PROXY` (ou `https_proxy`) par un tunnel `CONNECT` (un seul `CONNECT`, puis un seul `POST`) ;
  certificats : `SSL_CERT_FILE`. Amont : `https://` vers tout hôte, `http://` vers la boucle locale seulement (épreuves).
"""
import base64
import http.client
import json
import os
import re
import ssl
import time
import urllib.parse

import adaptateur_fournisseur_v1 as A

VERSION = "transport-kimi-reel-v1"
MODELE = "kimi-k3.1-pro"
AMONT_DEFAUT = "https://api.moonshot.ai"
CHEMIN = "/v1/chat/completions"
VARIABLE_CLE_DEFAUT = "KIMI_API_KEY"
PLAFOND_MAX_TOKENS = 24000
DELAI_SILENCE_DEFAUT_S = 600.0
DELAI_TOTAL_DEFAUT_S = 1800.0
TAILLE_MAX_DEFAUT = 32_000_000
STATUTS_RELANCABLES = {408, 409, 425, 429, 500, 502, 503, 504}
HOTES_LOCAUX = {"127.0.0.1", "localhost", "::1"}
AGENT = "transport-pilote/1"  # générique : ni nom, ni session, ni produit
MOTIFS_INTERDITS = (
    re.compile(r"session_[0-9A-Za-z]{8,}"),               # identifiant de session
    re.compile(r"claude\.ai/(code|chat|artifact)"),        # lien de session ou d'artefact
    re.compile(r"[A-Za-z0-9._%+-]{1,64}@[A-Za-z0-9-]{1,63}(\.[A-Za-z0-9-]{1,63}){0,8}\.[A-Za-z]{2,24}"),  # adresse (bornée : linéaire)
)
NOMS_INTERDITS_DEFAUT = ("Lazar", "lciric", "Ciric")


class _Compteur:
    """Compte les requêtes HTTP réellement commencées sur une connexion (chaque `putrequest`) : mesure, non déclaration."""

    def putrequest(self, *a, **kw):
        self._compteur_envois[0] += 1
        return super().putrequest(*a, **kw)


class ConnexionHTTPComptee(_Compteur, http.client.HTTPConnection):
    pass


class ConnexionHTTPSComptee(_Compteur, http.client.HTTPSConnection):
    pass


CLASSES_DE_CONNEXION = (ConnexionHTTPComptee, ConnexionHTTPSComptee)
OCTETS_PAR_JETON_SORTIE_MAX = 12  # texte rendu (contenu + réflexion) au-delà de 12 octets par jeton de sortie : usage suspect


class ErreurTransportFatale(Exception):
    """Réponse d'erreur non relançable (clé refusée, requête invalide) : comptée à la réserve, arrêt 17."""


def _entier(x):
    return isinstance(x, int) and not isinstance(x, bool)


def _court(texte, n=80):
    return re.sub(r"[^A-Za-z0-9_ .:/=-]", "?", str(texte))[:n]


class TransportKimiReel:
    relances_internes = 0
    repli_modele = None

    def __init__(self, amont=AMONT_DEFAUT, variable_cle=VARIABLE_CLE_DEFAUT, environ=None, effacer_variable=True,
                 delai_silence_s=DELAI_SILENCE_DEFAUT_S, delai_total_s=DELAI_TOTAL_DEFAUT_S, taille_max_octets=TAILLE_MAX_DEFAUT,
                 noms_interdits=NOMS_INTERDITS_DEFAUT, plafond_max_tokens=PLAFOND_MAX_TOKENS):
        env = os.environ if environ is None else environ
        p = urllib.parse.urlsplit(amont)
        if p.path not in ("", "/") or p.query or p.fragment or p.username or not p.hostname:
            raise A.ConfigurationRefusee("amont : schéma et hôte seulement")
        if not (p.scheme == "https" or (p.scheme == "http" and p.hostname in HOTES_LOCAUX)):
            raise A.ConfigurationRefusee("amont : https, ou http vers la boucle locale seulement")
        if not (0 < float(delai_silence_s) <= DELAI_TOTAL_DEFAUT_S and 0 < float(delai_total_s) <= 7200):
            raise A.ConfigurationRefusee("délais hors bornes")
        if not _entier(plafond_max_tokens) or not 0 < plafond_max_tokens <= PLAFOND_MAX_TOKENS:
            raise A.ConfigurationRefusee("plafond de max_tokens hors bornes")
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
        self.noms_interdits = tuple(noms_interdits)
        self._mandataire = self._lire_mandataire(env) if p.scheme == "https" else None
        self._tls = None
        if p.scheme == "https":
            ca = env.get("SSL_CERT_FILE")
            if ca and not os.path.isfile(ca):
                raise A.ConfigurationRefusee("SSL_CERT_FILE introuvable")
            self._tls = ssl.create_default_context(cafile=ca) if ca else ssl.create_default_context()
        self.envois = 0          # requêtes HTTP réellement commencées, toutes invocations confondues
        self.dernier_diagnostic = None
        self.derniere_reponse = None

    # --- garde de la clé -------------------------------------------------------------------------------------------
    def __repr__(self):
        return f"<TransportKimiReel {self.amont} envois={self.envois} clé=[masquée]>"

    __str__ = __repr__

    def __getstate__(self):
        raise TypeError("transport non sérialisable (clé)")

    def _masquer(self, texte):
        texte = str(texte)
        if self._cle:
            k = self._cle.decode("ascii")
            texte = texte.replace(k, "[clé]")
            del k
        return texte

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
        p, t = self._p, self.delai_silence_s
        if p.scheme == "https":
            if self._mandataire:
                h, port, en_tetes = self._mandataire
                c = ConnexionHTTPSComptee(h, port, context=self._tls, timeout=t)
                c.set_tunnel(p.hostname, p.port or 443, headers=en_tetes)  # CONNECT écrit hors de putrequest : non compté
                return c
            return ConnexionHTTPSComptee(p.hostname, p.port or 443, context=self._tls, timeout=t)
        return ConnexionHTTPComptee(p.hostname, p.port or 80, timeout=t)

    # --- contrôle de la requête, sans envoi ---------------------------------------------------------------------------
    def corps_fil(self, requete):
        """Corps exact qui partirait (octets), ou `ConfigurationRefusee` ; n'envoie rien."""
        if not isinstance(requete, dict):
            raise A.ConfigurationRefusee("requête non dict")
        cles = set(requete)
        if not cles <= {"model", "messages", "max_tokens", "stream", "n"} or not {"model", "messages", "max_tokens"} <= cles:
            raise A.ConfigurationRefusee(f"champs de requête hors contrat : {sorted(cles)}")
        if requete["model"] != MODELE:
            raise A.ConfigurationRefusee(f"modèle demandé {_court(requete['model'])!r} ≠ {MODELE}")
        if requete.get("stream", False) is not False or requete.get("n", 1) != 1 or isinstance(requete.get("n", 1), bool):
            raise A.ConfigurationRefusee("stream ou n hors contrat (stream faux, n = 1 exigés)")
        mt = requete["max_tokens"]
        if not _entier(mt) or not 0 < mt <= self.plafond_max_tokens:
            raise A.ConfigurationRefusee(f"max_tokens {mt!r} hors de 1..{self.plafond_max_tokens}")
        m = requete["messages"]
        if not (isinstance(m, list) and len(m) == 1 and isinstance(m[0], dict) and set(m[0]) == {"role", "content"}
                and m[0]["role"] == "user" and isinstance(m[0]["content"], str) and m[0]["content"]):
            raise A.ConfigurationRefusee("messages : un seul message user, texte non vide")
        corps = {"model": MODELE, "messages": [{"role": "user", "content": m[0]["content"]}], "max_tokens": mt,
                 "stream": True, "stream_options": {"include_usage": True}}
        brut = json.dumps(corps, ensure_ascii=False, separators=(",", ":"))
        for motif in MOTIFS_INTERDITS:
            if motif.search(brut):
                raise A.ConfigurationRefusee("motif interdit dans le corps (identifiant de session, lien ou adresse)")
        bas = brut.casefold()
        for nom in self.noms_interdits:
            if nom.casefold() in bas:
                raise A.ConfigurationRefusee("nom de personne interdit dans le corps")
        return brut.encode("utf-8")

    # --- envoi ----------------------------------------------------------------------------------------------------
    def envoyer(self, requete):
        """Un appel = une connexion neuve, comptée ; `tentatives` rendu = envois MESURÉS sur cette connexion. Si la mesure
        n'est pas 1 (relance cachée sous la connexion, connexion substituée), `AnomalieReponse` avec `envois` mesurés."""
        corps = self.corps_fil(requete)  # refus sans envoi
        if not self._cle:
            raise A.ConfigurationRefusee("transport fermé (clé effacée)")
        compteur = [0]
        self.derniere_reponse = None
        try:
            rep = self._envoyer_une_fois(corps, compteur)
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
        rep["tentatives"] = compteur[0]  # mesuré ; l'adaptateur exige 1
        self.dernier_diagnostic["envois_mesures"] = compteur[0]
        self.derniere_reponse = rep
        return rep

    def _envoyer_une_fois(self, corps, compteur):
        debut = time.monotonic()
        echeance = debut + self.delai_total_s
        diag = {"version": VERSION, "octets_corps": len(corps), "statut": None, "octets_reponse": 0, "morceaux": 0,
                "usage_place": None, "excedent_total_tokens": 0}
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
                raise A.ErreurFournisseur("délai de silence dépassé avant la réponse")
            except (OSError, http.client.HTTPException) as ex:
                raise A.ErreurFournisseur(self._masquer(f"coupure avant la réponse ({type(ex).__name__})"))
            except ValueError:  # en-tête refusé par http.client : son message recopierait la valeur, jamais relayé
                raise ErreurTransportFatale("en-tête refusé par http.client (message masqué)") from None
            diag["statut"] = rep.status
            if rep.status != 200:
                motif = self._motif_erreur(rep)
                if rep.status in STATUTS_RELANCABLES:
                    raise A.ErreurFournisseur(f"statut {rep.status} de l'amont ({motif})")
                raise ErreurTransportFatale(f"statut {rep.status} de l'amont ({motif})")
            if "text/event-stream" not in (rep.getheader("Content-Type") or ""):
                ex = A.AnomalieReponse("réponse 200 qui n'est pas un flux d'événements")
                ex.envois = 1
                raise ex
            return self._lire_flux(rep, echeance, diag)
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
            return self._masquer(_court(f"{e.get('type', '')} {e.get('code', '')}".strip() or "sans motif"))
        except (OSError, http.client.HTTPException, ValueError, AttributeError):
            return "corps illisible"

    def _lire_flux(self, rep, echeance, diag):
        contenu, raisonnement, fin, usage, servi, taille, fini, premier = [], [], None, None, None, 0, False, True
        ident = None
        while True:
            if time.monotonic() > echeance:
                raise A.ErreurFournisseur("délai total dépassé (coupé côté client)")
            try:
                ligne = rep.readline(1_000_000)
            except TimeoutError:
                raise A.ErreurFournisseur("délai de silence dépassé pendant le flux")
            except (OSError, http.client.HTTPException) as ex:
                raise A.ErreurFournisseur(self._masquer(f"coupure en plein flux ({type(ex).__name__})"))
            if not ligne:
                break
            taille += len(ligne)
            diag["octets_reponse"] = taille
            if taille > self.taille_max:
                ex = A.AnomalieReponse(f"réponse au-delà de {self.taille_max} octets")
                ex.envois = 1
                raise ex
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
                ex = A.AnomalieReponse("morceau de flux illisible")
                ex.envois = 1
                raise ex
            diag["morceaux"] += 1
            if morceau.get("error") is not None:
                e = morceau["error"] if isinstance(morceau["error"], dict) else {}
                raise A.ErreurFournisseur(self._masquer(f"événement d'erreur dans le flux ({_court(e.get('type', ''))})"))
            m = morceau.get("model")
            if premier or m is not None:
                if m != MODELE:  # barrière du modèle servi : lecture arrêtée, l'adaptateur lèvera AnomalieReponse
                    diag["modele_servi"] = _court(m)
                    return {"model": m, "usage": None, "choices": [{"message": {"content": ""}, "finish_reason": None}],
                            "tentatives": 1, "diagnostic": diag}
                servi = m
            premier = False
            if ident is None and isinstance(morceau.get("id"), str):
                ident = _court(morceau["id"], 120)  # identifiant de la réponse chez le fournisseur (rapprochement de facture)
            if isinstance(morceau.get("usage"), dict):
                usage, diag["usage_place"] = morceau["usage"], "racine"
            for ch in morceau.get("choices") or []:
                if not isinstance(ch, dict):
                    continue
                d = ch.get("delta") or {}
                if isinstance(d.get("content"), str):
                    contenu.append(d["content"])
                if isinstance(d.get("reasoning_content"), str):
                    raisonnement.append(d["reasoning_content"])
                if ch.get("finish_reason"):
                    fin = ch["finish_reason"]
                if isinstance(ch.get("usage"), dict):
                    usage, diag["usage_place"] = ch["usage"], "choix"
        if not fini:
            raise A.ErreurFournisseur("flux coupé avant [DONE]")
        usage = self._completer_usage(usage, diag)
        if usage is not None:
            octets_texte = sum(len(x.encode("utf-8")) for x in contenu + raisonnement)
            jetons = usage["completion_tokens"] + (usage.get("reasoning_tokens", 0) or 0)
            diag["octets_texte_rendu"] = octets_texte
            if octets_texte > OCTETS_PAR_JETON_SORTIE_MAX * max(jetons, 1):
                diag["usage_refuse"] = "texte rendu trop long pour la sortie déclarée (sous-compte présumé)"
                usage = None
        message = {"role": "assistant", "content": "".join(contenu)}
        if raisonnement:
            message["reasoning_content"] = "".join(raisonnement)
        diag["modele_servi"] = servi
        diag["fin"] = fin
        diag["id_reponse"] = ident
        return {"id": ident, "model": servi, "usage": usage, "choices": [{"message": message, "finish_reason": fin}],
                "tentatives": 1, "diagnostic": diag}

    @staticmethod
    def _completer_usage(usage, diag):
        """Copie de `usage`, ou None (réserve au pire, arrêt 16) si un champ exigé manque.
        Exigés (documentation lue le 30 octobre 2026, `api_chat.md` sha256 67b8b5fd…, exemples de réponse et de flux ; essai
        réel du 30 octobre : `completion_tokens` 16, `completion_tokens_details.reasoning_tokens` 13, `total_tokens` 105 =
        89 + 16) : `prompt_tokens`, `completion_tokens`, `total_tokens` et `completion_tokens_details.reasoning_tokens`,
        entiers. Le modèle raisonne toujours (`kimi-k3.1-pro`) : un champ de réflexion absent n'est jamais lu comme zéro.
        Excédent de `total_tokens` non expliqué : ajouté à `reasoning_tokens` (premier niveau), donc compté en sortie."""
        if not isinstance(usage, dict):
            diag["usage_refuse"] = "usage absent"
            return None
        u = json.loads(json.dumps(usage))
        det = u.get("completion_tokens_details")
        if not (_entier(u.get("prompt_tokens")) and _entier(u.get("completion_tokens")) and _entier(u.get("total_tokens"))
                and isinstance(det, dict) and _entier(det.get("reasoning_tokens"))):
            diag["usage_refuse"] = "champ exigé absent (prompt, completion, total ou completion_tokens_details.reasoning_tokens)"
            return None
        p, c, t, r = u.get("prompt_tokens"), u.get("completion_tokens"), u.get("total_tokens"), u.get("reasoning_tokens", 0) or 0
        if all(_entier(x) for x in (p, c, t, r)) and min(p, c, r) >= 0 and t > p + c + r:
            diag["excedent_total_tokens"] = t - p - c - r
            u["reasoning_tokens"] = r + (t - p - c - r)
        diag["usage_numerique"] = {k: v for k, v in u.items() if _entier(v)}
        return u


# Méthodes figées à l'import : `adaptateur_kimi_strict_v1` vérifie qu'aucune n'a été remplacée sur la classe ou l'instance.
METHODES_FIGEES = {n: TransportKimiReel.__dict__[n] for n in
                   ("envoyer", "_envoyer_une_fois", "_lire_flux", "_completer_usage", "_connexion", "corps_fil", "_motif_erreur",
                    "__init__", "fermer", "_masquer")}
PUTREQUEST_FIGE = _Compteur.__dict__["putrequest"]
