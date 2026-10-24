# -*- coding: utf-8 -*-
"""
m3_commun — module commun des trois scripts de brainstorm du « dossier 17 » (essaim M3), version déboguée v1.

Ce module remplace les parties fragiles des scripts d'origine (collés par Lazar le 24 octobre 2026) :

* un seul client d'appel aux modèles, qui n'échange jamais un modèle contre un autre : le modèle demandé est le
  seul appelé ; un échec est consigné comme un échec, jamais renvoyé comme un texte, jamais compté comme une
  réponse « sans refus » ;
* un journal par appel (une ligne JSON par appel) : lignée, modèle demandé, modèle servi, raison d'arrêt, code
  HTTP, jetons, durée, empreinte SHA-256 de l'invite et du texte ;
* aucun contenu de « réflexion » (blocs `thinking` d'Anthropic, parties `thought` de Gemini) n'est renvoyé
  comme texte ;
* une analyse spectrale réellement calculée, ou déclarée « non calculée » ; jamais une constante par défaut
  imprimée comme une mesure ;
* une extraction JSON dont le gabarit ne contient aucun nombre d'exemple ; un échec d'extraction est un échec,
  jamais le gabarit lui-même ;
* un substrat sauvegardé avec copie de secours horodatée ; la fonction de sauvegarde renvoie le dictionnaire ;
* un mode « à blanc » (aucun appel réseau, aucune dépense) pour vérifier toute la chaîne ;
* un plafond d'appels et de jetons de sortie qui arrête le script au lieu de continuer en silence.

Clés : lues dans les variables d'environnement `M3_ANTHROPIC_API_KEY` et `M3_GEMINI_API_KEY`, posées
explicitement par Lazar. Si la clé Anthropic est identique à `RR_ANTHROPIC_API_KEY` ou `RR_ANTHROPIC_API_KEY_2`
(clés d'un autre projet), le client refuse de démarrer. Aucune clé n'est jamais écrite dans un fichier.

Bibliothèques : Python 3.11 ou plus, numpy. Rien d'autre.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
import re
import sys
import threading
import time
import urllib.error
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Callable, Optional

try:
    import numpy as np
except ImportError as exc:  # pragma: no cover
    raise SystemExit("numpy est requis : `pip install numpy` (" + str(exc) + ")")

VERSION = "essaim-m3-debogage-v1"

# --------------------------------------------------------------------------------------------------------------
# Lignées : un seul modèle par lignée. Aucune rotation, aucun repli.
# --------------------------------------------------------------------------------------------------------------
LIGNEES = {
    "GEMINI_ARGON": {"fournisseur": "gemini", "modele": "gemini-4-argon"},
    "CLAUDE_FABLE_5_1": {"fournisseur": "anthropic", "modele": "claude-fable-5-1"},
    "CLAUDE_OPUS_5_5": {"fournisseur": "anthropic", "modele": "claude-opus-5-5"},
}
ALIAS_LIGNEES = {
    "GEMINI": "GEMINI_ARGON",
    "GEMINI_ARGON": "GEMINI_ARGON",
    "GEMINI_4_ARGON": "GEMINI_ARGON",
    "ARGON": "GEMINI_ARGON",
    "FABLE": "CLAUDE_FABLE_5_1",
    "CLAUDE_FABLE": "CLAUDE_FABLE_5_1",
    "CLAUDE_FABLE_5_1": "CLAUDE_FABLE_5_1",
    "OPUS": "CLAUDE_OPUS_5_5",
    "CLAUDE_OPUS": "CLAUDE_OPUS_5_5",
    "CLAUDE_OPUS_5_5": "CLAUDE_OPUS_5_5",
}
CYCLE_LIGNEES_PAR_DEFAUT = [["GEMINI_ARGON"], ["CLAUDE_FABLE_5_1"], ["CLAUDE_OPUS_5_5"],
                            ["CLAUDE_FABLE_5_1", "CLAUDE_OPUS_5_5"]]
SEUIL_TEXTE_VIDE = 20  # caractères ; en dessous, la réponse est « vide » (seuil des scripts d'origine)


class ErreurEssaim(Exception):
    """Erreur du module : jamais avalée, jamais remplacée par une valeur par défaut."""


class LigneeInconnue(ErreurEssaim):
    pass


class BudgetDepasse(ErreurEssaim):
    pass


class ClesRefusees(ErreurEssaim):
    pass


def normaliser_lignee(nom: str) -> str:
    """Renvoie le nom canonique d'une lignée ; lève `LigneeInconnue` sinon (pas de valeur par défaut)."""
    cle = str(nom).strip().upper().replace("-", "_").replace(".", "_").replace(" ", "_")
    if cle in ALIAS_LIGNEES:
        return ALIAS_LIGNEES[cle]
    raise LigneeInconnue(f"lignée inconnue : {nom!r} ; lignées connues : {sorted(LIGNEES)}")


def empreinte(texte: str) -> str:
    return hashlib.sha256(texte.encode("utf-8")).hexdigest()


def heure_utc() -> str:
    return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())


def horodatage_court() -> str:
    return time.strftime("%Y%m%d-%H%M%S", time.gmtime())


# --------------------------------------------------------------------------------------------------------------
# Configuration et arguments de ligne de commande
# --------------------------------------------------------------------------------------------------------------
@dataclass
class Config:
    dossier: Path
    a_blanc: bool = False
    graine: int = 20261024
    max_appels: int = 200
    max_jetons_sortie: int = 400_000
    max_tokens_par_appel: int = 6144
    parallelisme: int = 8
    delai_s: float = 105.0
    temperature_anthropic: bool = False  # les scripts d'origine omettaient le champ pour les modèles 5.x
    nom_run: str = ""
    arbitre: str = "CLAUDE_OPUS_5_5"  # lignée des étages M1 (extraction) et M0 (synthèse)

    @property
    def substrat(self) -> Path:
        return self.dossier / "SUBSTRAT_BRUT_CONNAISSANCES_INTER_GENERATIONS.json"

    @property
    def dossier_run(self) -> Path:
        return self.dossier / "runs_debogage" / self.nom_run

    @property
    def journal(self) -> Path:
        return self.dossier_run / "journal_appels.jsonl"


def analyseur_arguments(description: str) -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description=description)
    p.add_argument("--dossier", type=Path, default=None,
                   help="dossier 17 (contient le substrat) ; par défaut le dossier du script")
    p.add_argument("--a-blanc", action="store_true",
                   help="aucun appel réseau, aucune dépense : réponses factices déterministes")
    p.add_argument("--graine", type=int, default=20261024, help="graine du mode à blanc (R9)")
    p.add_argument("--max-appels", type=int, default=200, help="plafond d'appels de modèle, arrêt au-delà")
    p.add_argument("--max-jetons-sortie", type=int, default=400_000, help="plafond de jetons de sortie")
    p.add_argument("--parallelisme", type=int, default=8)
    p.add_argument("--nom-run", type=str, default="", help="nom du dossier de sortie (sinon horodaté)")
    p.add_argument("--arbitre", type=str, default="CLAUDE_OPUS_5_5",
                   help="lignée des étages M1 et M0 (extraction, synthèse)")
    p.add_argument("--temperature-anthropic", action="store_true",
                   help="envoyer le champ temperature aux modèles Anthropic (omis par défaut)")
    return p


def config_depuis_arguments(args: argparse.Namespace, prefixe: str, fichier_script: str) -> Config:
    dossier = args.dossier if args.dossier is not None else Path(fichier_script).resolve().parent
    nom_run = args.nom_run or f"{horodatage_court()}-{prefixe}" + ("-a-blanc" if args.a_blanc else "")
    return Config(dossier=dossier, a_blanc=args.a_blanc, graine=args.graine, max_appels=args.max_appels,
                  max_jetons_sortie=args.max_jetons_sortie, parallelisme=args.parallelisme, nom_run=nom_run,
                  arbitre=normaliser_lignee(args.arbitre), temperature_anthropic=args.temperature_anthropic)


# --------------------------------------------------------------------------------------------------------------
# Journal (une ligne JSON par appel) et budget
# --------------------------------------------------------------------------------------------------------------
class Journal:
    def __init__(self, chemin: Path):
        self.chemin = chemin
        self.chemin.parent.mkdir(parents=True, exist_ok=True)
        self._lock = threading.Lock()
        self.console = chemin.with_name("console.log")

    def ecrire(self, enregistrement: dict) -> None:
        ligne = json.dumps(enregistrement, ensure_ascii=False)
        with self._lock, open(self.chemin, "a", encoding="utf-8") as f:
            f.write(ligne + "\n")

    def dire(self, message: str) -> None:
        ligne = f"[{time.strftime('%H:%M:%S', time.gmtime())} UTC] {message}"
        with self._lock:
            print(ligne, flush=True)
            with open(self.console, "a", encoding="utf-8") as f:
                f.write(ligne + "\n")


class Budget:
    def __init__(self, max_appels: int, max_jetons_sortie: int):
        self.max_appels = int(max_appels)
        self.max_jetons_sortie = int(max_jetons_sortie)
        self.appels = 0
        self.jetons_sortie = 0
        self.jetons_entree = 0
        self._lock = threading.Lock()

    def reserver_appel(self) -> int:
        with self._lock:
            if self.appels >= self.max_appels:
                raise BudgetDepasse(f"plafond d'appels atteint : {self.appels} / {self.max_appels}")
            self.appels += 1
            return self.appels

    def ajouter_jetons(self, entree: Optional[int], sortie: Optional[int]) -> None:
        with self._lock:
            self.jetons_entree += int(entree or 0)
            self.jetons_sortie += int(sortie or 0)
            if self.jetons_sortie > self.max_jetons_sortie:
                raise BudgetDepasse(
                    f"plafond de jetons de sortie dépassé : {self.jetons_sortie} / {self.max_jetons_sortie}")

    def etat(self) -> dict:
        with self._lock:
            return {"appels": self.appels, "max_appels": self.max_appels, "jetons_entree": self.jetons_entree,
                    "jetons_sortie": self.jetons_sortie, "max_jetons_sortie": self.max_jetons_sortie}


# --------------------------------------------------------------------------------------------------------------
# Réponses et extraction de texte (jamais la réflexion)
# --------------------------------------------------------------------------------------------------------------
@dataclass
class Reponse:
    ok: bool
    statut: str  # "ok" | "vide" | "echec_api"
    lignee: str
    modele_demande: str
    modele_servi: Optional[str]
    texte: str
    raison_arret: Optional[str]
    http: Optional[int]
    erreur: Optional[str]
    jetons_entree: Optional[int]
    jetons_sortie: Optional[int]
    duree_s: float
    etiquette: str
    empreinte_invite: str
    empreinte_texte: str
    tentatives: int
    heure_utc: str
    a_blanc: bool
    temperature_envoyee: Optional[float]


def texte_anthropic(resp: dict) -> str:
    """Concatène les seuls blocs `text`. Les blocs `thinking` ne sont jamais renvoyés."""
    blocs = resp.get("content", []) or []
    textes = [b.get("text", "") for b in blocs if isinstance(b, dict) and b.get("type") == "text"]
    return "\n".join(t for t in textes if t).strip()


def texte_gemini(resp: dict) -> str:
    """Concatène les parties `text` du premier candidat, en ignorant les parties `thought`."""
    candidats = resp.get("candidates", []) or []
    if not candidats:
        return ""
    parties = (candidats[0].get("content", {}) or {}).get("parts", []) or []
    textes = [p.get("text", "") for p in parties
              if isinstance(p, dict) and p.get("text") and not p.get("thought")]
    return "\n".join(textes).strip()


# --------------------------------------------------------------------------------------------------------------
# Répondeur à blanc (déterministe, R9) : pour vérifier la chaîne sans réseau ni dépense
# --------------------------------------------------------------------------------------------------------------
class RepondeurABlanc:
    """Réponses factices déterministes. Mélange voulu pour éprouver la comptabilité : environ 70 % de textes
    avec 1 à 6 blocs LaTeX et une valeur de calibration, 10 % de refus de rôle, 10 % de textes vides,
    10 % d'échecs d'interface. Graines dérivées par `numpy.random.SeedSequence` (R9)."""

    def __init__(self, graine: int):
        self.graine = int(graine)
        self._compteur = 0
        self._lock = threading.Lock()

    def repondre(self, lignee: str, invite: str) -> dict:
        with self._lock:
            self._compteur += 1
            n = self._compteur
        rng = np.random.default_rng(np.random.SeedSequence([self.graine, n]))
        tirage = rng.random()
        modele = LIGNEES[lignee]["modele"] + "-a-blanc"
        if tirage < 0.10:
            return {"statut": "echec_api", "texte": "", "modele_servi": None, "raison": None, "http": 503,
                    "erreur": "à blanc : échec simulé HTTP 503"}
        if tirage < 0.20:
            return {"statut": "vide", "texte": "", "modele_servi": modele, "raison": "end_turn", "http": 200,
                    "erreur": None}
        if tirage < 0.30:
            texte = ("Je ne peux pas adopter l'identité d'un agent d'essaim fictif ni prétendre avoir accès à un "
                     "tableau partagé en direct. En tant que modèle de langage, je peux en revanche discuter la "
                     "question mathématique si vous la posez directement.")
            return {"statut": "ok", "texte": texte, "modele_servi": modele, "raison": "end_turn", "http": 200,
                    "erreur": None}
        k = int(rng.integers(1, 7))
        morceaux = [f"Contribution à blanc n° {n} ({lignee}). Invite de {len(invite)} caractères."]
        for i in range(k):
            a, b = rng.integers(1, 9, size=2)
            morceaux.append(f"$$D_\\Phi(u \\,\\|\\, q_{{{i}}}) = {a} \\cdot \\Phi(u) - {b} \\cdot \\Phi(q_{{{i}}})$$")
        q = float(np.round(0.5 + 0.49 * rng.random(), 3))
        morceaux.append(f"Confiance épistémique : $q^{{(T)}} = {q}$.")
        return {"statut": "ok", "texte": "\n".join(morceaux), "modele_servi": modele, "raison": "end_turn",
                "http": 200, "erreur": None}


# --------------------------------------------------------------------------------------------------------------
# Client d'appel : un modèle par lignée, échec = échec, journal par appel
# --------------------------------------------------------------------------------------------------------------
Transport = Callable[[str, bytes, dict, float], tuple]  # (url, data, headers, timeout) -> (code_http, corps)


def _transport_urllib(url: str, data: bytes, headers: dict, timeout: float) -> tuple:
    req = urllib.request.Request(url, data=data, headers=headers, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.status, r.read().decode("utf-8")
    except urllib.error.HTTPError as he:
        corps = ""
        try:
            corps = he.read().decode("utf-8", errors="replace")
        except Exception:  # pragma: no cover
            pass
        return he.code, corps


class Client:
    CODES_REESSAI = {429, 500, 502, 503, 529}

    def __init__(self, config: Config, journal: Journal, budget: Budget, transport: Optional[Transport] = None):
        self.config = config
        self.journal = journal
        self.budget = budget
        self.transport: Transport = transport or _transport_urllib
        self._semaphore = threading.BoundedSemaphore(max(1, config.parallelisme))
        self._a_blanc = RepondeurABlanc(config.graine) if config.a_blanc else None
        self._cles: dict = {}
        if not config.a_blanc:
            self._charger_cles()

    # -- clés -------------------------------------------------------------------------------------------------
    def _charger_cles(self) -> None:
        env = os.environ
        cle_a = env.get("M3_ANTHROPIC_API_KEY", "")
        cle_g = env.get("M3_GEMINI_API_KEY", "")
        if not cle_a or not cle_g:
            raise ClesRefusees("poser M3_ANTHROPIC_API_KEY et M3_GEMINI_API_KEY (clés du programme, jamais RR_*)")
        for nom in ("RR_ANTHROPIC_API_KEY", "RR_ANTHROPIC_API_KEY_2"):
            if env.get(nom) and env.get(nom) == cle_a:
                raise ClesRefusees(f"M3_ANTHROPIC_API_KEY est identique à {nom} (clé d'un autre projet) : refus")
        self._cles = {"anthropic": cle_a, "gemini": cle_g}

    # -- appel ------------------------------------------------------------------------------------------------
    def appeler(self, lignee: str, invite: str, temperature: Optional[float] = None, etiquette: str = "",
                outil_recherche: bool = False) -> Reponse:
        lignee = normaliser_lignee(lignee)
        spec = LIGNEES[lignee]
        self.budget.reserver_appel()
        debut = time.time()
        emp_invite = empreinte(invite)
        temp_envoyee: Optional[float] = None
        if temperature is not None and (spec["fournisseur"] == "gemini" or self.config.temperature_anthropic):
            temp_envoyee = float(max(0.0, min(1.0, temperature)))

        if self._a_blanc is not None:
            r = self._a_blanc.repondre(lignee, invite)
            rep = self._construire(lignee, spec["modele"], r["modele_servi"], r["texte"], r["raison"], r["http"],
                                   r["erreur"], 0, 0, debut, etiquette, emp_invite, 1, temp_envoyee, True)
            self._consigner(rep)
            return rep

        with self._semaphore:
            rep = self._appeler_reel(lignee, spec, invite, temp_envoyee, etiquette, emp_invite, debut,
                                     outil_recherche)
        self._consigner(rep)
        return rep

    def _consigner(self, rep: Reponse) -> None:
        self.journal.ecrire(asdict(rep))
        self.budget.ajouter_jetons(rep.jetons_entree, rep.jetons_sortie)

    def _construire(self, lignee, modele_demande, modele_servi, texte, raison, http, erreur, j_in, j_out, debut,
                    etiquette, emp_invite, tentatives, temp_envoyee, a_blanc) -> Reponse:
        texte = texte or ""
        if erreur is not None or (http is not None and http >= 400):
            statut, ok = "echec_api", False
        elif len(texte.strip()) < SEUIL_TEXTE_VIDE:
            statut, ok = "vide", False
        else:
            statut, ok = "ok", True
        return Reponse(ok=ok, statut=statut, lignee=lignee, modele_demande=modele_demande,
                       modele_servi=modele_servi, texte=texte, raison_arret=raison, http=http, erreur=erreur,
                       jetons_entree=j_in, jetons_sortie=j_out, duree_s=round(time.time() - debut, 3),
                       etiquette=etiquette, empreinte_invite=emp_invite, empreinte_texte=empreinte(texte),
                       tentatives=tentatives, heure_utc=heure_utc(), a_blanc=a_blanc,
                       temperature_envoyee=temp_envoyee)

    def _appeler_reel(self, lignee, spec, invite, temp_envoyee, etiquette, emp_invite, debut,
                      outil_recherche) -> Reponse:
        modele = spec["modele"]
        if spec["fournisseur"] == "anthropic":
            url = "https://api.anthropic.com/v1/messages"
            charge = {"model": modele, "max_tokens": self.config.max_tokens_par_appel,
                      "messages": [{"role": "user", "content": invite}]}
            if temp_envoyee is not None:
                charge["temperature"] = temp_envoyee
            en_tetes = {"x-api-key": self._cles["anthropic"], "anthropic-version": "2023-06-01",
                        "Content-Type": "application/json"}
        else:
            url = ("https://generativelanguage.googleapis.com/v1beta/models/"
                   f"{modele}:generateContent?key={urllib.parse.quote(self._cles['gemini'])}")
            gen = {"maxOutputTokens": self.config.max_tokens_par_appel}
            if temp_envoyee is not None:
                gen["temperature"] = temp_envoyee
            charge = {"contents": [{"parts": [{"text": invite}]}], "generationConfig": gen}
            if outil_recherche:
                charge["tools"] = [{"google_search": {}}]
            en_tetes = {"Content-Type": "application/json"}

        donnees = json.dumps(charge).encode("utf-8")
        derniere_erreur, dernier_code = None, None
        for tentative in range(1, 4):
            try:
                code, corps = self.transport(url, donnees, en_tetes, self.config.delai_s)
            except Exception as exc:  # réseau coupé, délai : on réessaie, puis on consigne l'échec
                derniere_erreur, dernier_code = f"{type(exc).__name__}: {exc}", None
                time.sleep(min(30.0, 2.0 ** tentative))
                continue
            if code in self.CODES_REESSAI:
                derniere_erreur, dernier_code = f"HTTP {code}", code
                time.sleep(min(60.0, 2.0 ** tentative + 1.0))
                continue
            if code >= 400:
                return self._construire(lignee, modele, None, "", None, code, f"HTTP {code} : {corps[:300]}",
                                        None, None, debut, etiquette, emp_invite, tentative, temp_envoyee, False)
            try:
                resp = json.loads(corps)
            except json.JSONDecodeError as exc:
                return self._construire(lignee, modele, None, "", None, code, f"corps non JSON : {exc}", None, None,
                                        debut, etiquette, emp_invite, tentative, temp_envoyee, False)
            if spec["fournisseur"] == "anthropic":
                texte = texte_anthropic(resp)
                servi = resp.get("model")
                raison = resp.get("stop_reason")
                usage = resp.get("usage", {}) or {}
                j_in, j_out = usage.get("input_tokens"), usage.get("output_tokens")
            else:
                texte = texte_gemini(resp)
                servi = resp.get("modelVersion")
                cands = resp.get("candidates", []) or []
                raison = cands[0].get("finishReason") if cands else None
                usage = resp.get("usageMetadata", {}) or {}
                j_in, j_out = usage.get("promptTokenCount"), usage.get("candidatesTokenCount")
            if servi and servi != modele and not str(servi).startswith(modele):
                # Le fournisseur annonce un autre modèle que celui demandé : consigné tel quel, jamais masqué.
                raison = f"{raison} | MODELE_SERVI_DIFFERENT"
            return self._construire(lignee, modele, servi, texte, raison, code, None, j_in, j_out, debut,
                                    etiquette, emp_invite, tentative, temp_envoyee, False)
        return self._construire(lignee, modele, None, "", None, dernier_code,
                                f"échec après 3 tentatives : {derniere_erreur}", None, None, debut, etiquette,
                                emp_invite, 3, temp_envoyee, False)


# --------------------------------------------------------------------------------------------------------------
# Blocs LaTeX, tableau partagé, résumé des réponses
# --------------------------------------------------------------------------------------------------------------
RE_BLOC_LATEX = re.compile(r"\$\$(.*?)\$\$", re.S)


def extraire_blocs_latex(texte: str, longueur_min: int = 7) -> list:
    """Blocs `$$…$$` d'au moins `longueur_min` caractères, dédoublonnés, dans l'ordre. Ce sont des blocs de
    texte entre deux doubles dollars : rien n'en garantit la validité mathématique."""
    vus, sortie = set(), []
    for bloc in RE_BLOC_LATEX.findall(texte or ""):
        b = bloc.strip()
        if len(b) >= longueur_min and b not in vus:
            vus.add(b)
            sortie.append(b)
    return sortie


def fusionner_uniques(base: list, ajouts: list) -> list:
    sortie = list(base or [])
    vus = set(str(x) for x in sortie)
    for x in ajouts or []:
        if str(x) not in vus:
            vus.add(str(x))
            sortie.append(x)
    return sortie


class Tableau:
    """Tableau partagé (posts et blocs LaTeX) d'une unité d'essaim."""

    def __init__(self):
        self.posts: list = []
        self.blocs: list = []
        self._lock = threading.Lock()

    def ajouter(self, etiquette: str, texte: str) -> None:
        with self._lock:
            self.posts.append({"author": etiquette, "content": texte})
            for b in extraire_blocs_latex(texte):
                if b not in self.blocs:
                    self.blocs.append(b)

    def contexte(self, n_blocs: int = 15, n_posts: int = 8) -> str:
        with self._lock:
            if not self.posts and not self.blocs:
                return "=== TABLEAU PARTAGÉ (VIERGE — INITIALISATION) ===\nAucun post précédent."
            lignes = ["=== ÉTAT DU TABLEAU PARTAGÉ ==="]
            if self.blocs:
                lignes.append(f"\n[ESPACE DE TRAVAIL — {len(self.blocs)} BLOCS LATEX ({n_blocs} DERNIERS)] :")
                for i, eq in enumerate(self.blocs[-n_blocs:], 1):
                    lignes.append(f"  Eq.{i:02d}: $${' '.join(str(eq).splitlines())[:240]}$$")
            if self.posts:
                lignes.append(f"\n[MESSAGES — {len(self.posts)} POSTS ({n_posts} DERNIERS)] :")
                for p in self.posts[-n_posts:]:
                    contenu = " ".join(str(p.get("content", "")).splitlines())[:380]
                    lignes.append(f"  * [{p.get('author', 'Agent')}] : {contenu}...")
            return "\n".join(lignes)


def resumer_reponses(reponses: list) -> dict:
    """Compte les réponses par statut, par lignée et par modèle servi. Les échecs restent des échecs."""
    r = {"n": len(reponses), "ok": 0, "vide": 0, "echec_api": 0, "par_lignee": {}, "par_modele_servi": {},
         "modele_servi_different": 0}
    for rep in reponses:
        r[rep.statut] = r.get(rep.statut, 0) + 1
        pl = r["par_lignee"].setdefault(rep.lignee, {"ok": 0, "vide": 0, "echec_api": 0})
        pl[rep.statut] = pl.get(rep.statut, 0) + 1
        cle = rep.modele_servi or "(aucun)"
        r["par_modele_servi"][cle] = r["par_modele_servi"].get(cle, 0) + 1
        if rep.raison_arret and "MODELE_SERVI_DIFFERENT" in str(rep.raison_arret):
            r["modele_servi_different"] += 1
    return r


# --------------------------------------------------------------------------------------------------------------
# Castes et unités d'essaim
# --------------------------------------------------------------------------------------------------------------
def castes_du_substrat(substrat: dict) -> list:
    """Castes mémorisées par les scripts d'origine (`PRIMORDIAL_MITOSIS_DONE_CACHE`). Une caste est un triplet
    (mode, lignées, température) ; rien de plus n'est garanti. Les castes mal formées sont écartées et comptées."""
    cache = substrat.get("PRIMORDIAL_MITOSIS_DONE_CACHE", {}) or {}
    brutes = cache.get("castes") or cache.get("differentiated_castes") or []
    castes, ecartees = [], 0
    for c in brutes:
        try:
            lignees = [normaliser_lignee(x) for x in (c.get("lineages") or [])]
            if not lignees:
                raise LigneeInconnue("aucune lignée")
            castes.append({"mode": str(c.get("mode", "MONOCULTURE")).upper(), "lineages": lignees,
                           "temp": float(c.get("temp", 0.45)), "focus": str(c.get("focus", ""))})
        except (LigneeInconnue, AttributeError, TypeError, ValueError):
            ecartees += 1
    if ecartees:
        castes.append({"_ecartees": ecartees})
    return castes


def selectionner_castes(castes: list, n: int) -> list:
    """`n` castes en cyclant sur la liste du substrat, ou sur le cycle par défaut si elle est vide."""
    propres = [c for c in castes if "lineages" in c]
    choisies = []
    for i in range(n):
        if propres:
            c = dict(propres[i % len(propres)])
        else:
            l_sel = CYCLE_LIGNEES_PAR_DEFAUT[i % len(CYCLE_LIGNEES_PAR_DEFAUT)]
            c = {"mode": "MONOCULTURE" if len(l_sel) == 1 else "HYBRIDE", "lineages": list(l_sel),
                 "temp": round(0.30 + 0.50 * (i % 7) / 6.0, 3), "focus": ""}
        c["slot"] = i + 1
        choisies.append(c)
    return choisies


def executer_vague(client: Client, tableau: Tableau, castes: list, construire_invite: Callable[[dict, str], str],
                   prefixe: str, journal: Journal, taille_lot: int = 12) -> list:
    """Déploie les castes par lots ; chaque lot voit l'état du tableau laissé par le lot précédent.
    Une cellule hybride enchaîne deux appels : la première lignée propose, la seconde critique."""
    reponses: list = []
    for i_lot, debut in enumerate(range(0, len(castes), taille_lot), start=1):
        lot = castes[debut:debut + taille_lot]
        contexte = tableau.contexte()
        with ThreadPoolExecutor(max_workers=max(1, min(client.config.parallelisme, len(lot)))) as ex:
            futurs = {}
            for c in lot:
                etiquette = f"{prefixe}_Caste_{c['slot']}_{c['mode']}_{'_x_'.join(c['lineages'])}_tau{c['temp']}"
                invite = construire_invite(c, contexte)
                if len(c["lineages"]) == 1:
                    futurs[ex.submit(client.appeler, c["lineages"][0], invite, c["temp"], etiquette)] = etiquette
                else:
                    futurs[ex.submit(_cellule_hybride, client, c["lineages"], invite, c["temp"], etiquette)] = etiquette
            for f in as_completed(futurs):
                try:
                    reps = f.result()
                except BudgetDepasse:
                    raise
                reps = reps if isinstance(reps, list) else [reps]
                for rep in reps:
                    reponses.append(rep)
                    if rep.ok:
                        tableau.ajouter(rep.etiquette, rep.texte)
        r = resumer_reponses(reponses)
        journal.dire(f"  * [{prefixe} | lot {i_lot}] réponses : {r['ok']} ok, {r['vide']} vides, "
                     f"{r['echec_api']} échecs sur {r['n']} appels ; {len(tableau.blocs)} blocs LaTeX")
    return reponses


def _cellule_hybride(client: Client, lignees: list, invite: str, temp: float, etiquette: str) -> list:
    rep1 = client.appeler(lignees[0], invite, temp, etiquette + "_1_" + lignees[0])
    if not rep1.ok:
        return [rep1]
    invite2 = (f"{invite}\n\n=== PROPOSITION DE {lignees[0]} ===\n{rep1.texte[:2500]}\n\n"
               "Critique rigoureusement cette analyse, corrige tout angle mort et démontre un énoncé plus fort.")
    rep2 = client.appeler(lignees[1], invite2, temp, etiquette + "_2_" + lignees[1])
    return [rep1, rep2]


def sondes_orthogonales(client: Client, tableau: Tableau, n: int, prefixe: str, consigne: str,
                        journal: Journal, structures_saturees: list) -> list:
    """Étage dit « M2 » : `n` appels supplémentaires, invités à s'écarter de ce qui est déjà au tableau.
    C'est une consigne d'écart, pas une projection sur un complément orthogonal."""
    cycle = ["CLAUDE_OPUS_5_5", "CLAUDE_FABLE_5_1", "GEMINI_ARGON"]
    contexte = tableau.contexte()
    reponses = []
    with ThreadPoolExecutor(max_workers=max(1, min(client.config.parallelisme, n))) as ex:
        futurs = {}
        for s in range(n):
            lignee = cycle[s % 3]
            etiquette = f"{prefixe}_M2_ecart_{s + 1}_{lignee}"
            invite = (f"SONDE D'ÉCART (`{prefixe}`).\nStructures déjà fréquentes au tableau : {structures_saturees}\n"
                      f"{contexte}\n\n{consigne}")
            futurs[ex.submit(client.appeler, lignee, invite, round(0.62 + 0.05 * s, 2), etiquette)] = etiquette
        for f in as_completed(futurs):
            rep = f.result()
            reponses.append(rep)
            if rep.ok:
                tableau.ajouter(rep.etiquette, rep.texte)
    r = resumer_reponses(reponses)
    journal.dire(f"  * [{prefixe} | sondes d'écart] {r['ok']} ok, {r['vide']} vides, {r['echec_api']} échecs sur {r['n']}")
    return reponses


# --------------------------------------------------------------------------------------------------------------
# Analyse spectrale réellement calculée (TF-IDF, matrice de Gram, valeurs propres)
# --------------------------------------------------------------------------------------------------------------
RE_JETON = re.compile(r"\\[a-zA-Z]+|[a-zA-Zàâäéèêëîïôöùûüç]{3,}")


def analyse_spectrale(textes: list) -> dict:
    """Indices descriptifs de diversité d'un ensemble de textes. Vecteurs TF-IDF normalisés, matrice de Gram
    G = X Xᵀ, valeurs propres λ. « capacité de Shannon-Gram » = Σ log₂(1 + λᵢ) : nom repris des scripts d'origine,
    défini ici explicitement ; indice descriptif, sans portée théorique. Moins de deux textes : non calculé."""
    textes = [t for t in (textes or []) if t and t.strip()]
    n = len(textes)
    if n < 2:
        return {"calcule": False, "raison": "moins de deux textes non vides", "n_textes": n}
    jetons = [RE_JETON.findall(t.lower()) for t in textes]
    vocab = sorted(set(j for js in jetons for j in js))
    if not vocab:
        return {"calcule": False, "raison": "aucun jeton", "n_textes": n}
    index = {v: i for i, v in enumerate(vocab)}
    X = np.zeros((n, len(vocab)))
    for i, js in enumerate(jetons):
        for j in js:
            X[i, index[j]] += 1.0
    df = (X > 0).sum(axis=0)
    idf = np.log((1.0 + n) / (1.0 + df)) + 1.0
    X = X * idf
    normes = np.linalg.norm(X, axis=1, keepdims=True)
    normes[normes == 0] = 1.0
    X = X / normes
    G = X @ X.T
    lam = np.clip(np.linalg.eigvalsh(G), 0.0, None)
    hors_diag = G[~np.eye(n, dtype=bool)]
    saturees = [vocab[i] for i in np.argsort(-df)[:10] if df[i] / n >= 0.75]
    return {"calcule": True, "n_textes": n, "taille_vocabulaire": len(vocab),
            "capacite_shannon_gram": float(np.sum(np.log2(1.0 + lam))),
            "lambda_min": float(lam.min()), "lambda_max": float(lam.max()),
            "similarite_moyenne_hors_diagonale": float(hors_diag.mean()) if hors_diag.size else 0.0,
            "structures_saturees": saturees}


# --------------------------------------------------------------------------------------------------------------
# Extraction JSON (étage dit « M1 ») : gabarit sans nombre d'exemple, échec = échec
# --------------------------------------------------------------------------------------------------------------
def _charger_json_tolerant(texte: str):
    t = (texte or "").strip()
    t = re.sub(r"^```(?:json)?\s*", "", t)
    t = re.sub(r"\s*```$", "", t)
    try:
        return json.loads(t)
    except json.JSONDecodeError:
        pass
    debut, fin = t.find("{"), t.rfind("}")
    if debut != -1 and fin > debut:
        try:
            return json.loads(t[debut:fin + 1])
        except json.JSONDecodeError:
            return None
    return None


def _liste_chaines(valeur) -> list:
    if isinstance(valeur, list):
        return [x if isinstance(x, str) else json.dumps(x, ensure_ascii=False) for x in valeur]
    if isinstance(valeur, str) and valeur.strip():
        return [valeur]
    return []


def extraire_json_structure(client: Client, invite: str, cles: list, etiquette: str) -> dict:
    """Demande à l'arbitre un objet JSON dont les valeurs sont des listes de chaînes, une par clé de `cles`.
    Chaque élément doit citer entre crochets l'étiquette de l'agent source (traçabilité). Deux tentatives.
    En cas d'échec : `ok=False`, listes vides, et le texte brut est conservé pour l'audit. Le gabarit ne contient
    aucun nombre : rien ne peut être recopié comme un comptage."""
    gabarit = {k: ["<chaîne : élément extrait, suivi de [étiquette de l'agent source]>"] for k in cles}
    consigne = (f"{invite}\n\nRéponds UNIQUEMENT par un objet JSON valide ayant exactement ces clés, chacune une "
                f"liste de chaînes (liste vide si rien n'est trouvé ; n'invente rien) :\n"
                f"{json.dumps(gabarit, ensure_ascii=False, indent=2)}")
    brut = []
    for tentative in (1, 2):
        texte_invite = consigne if tentative == 1 else consigne + \
            "\n\nTa réponse précédente n'était pas un objet JSON valide. Aucun texte hors du JSON."
        rep = client.appeler(client.config.arbitre, texte_invite, 0.2, f"{etiquette}_M1_tentative{tentative}")
        brut.append({"statut": rep.statut, "empreinte_texte": rep.empreinte_texte, "modele_servi": rep.modele_servi})
        if not rep.ok:
            continue
        obj = _charger_json_tolerant(rep.texte)
        if isinstance(obj, dict):
            return {"ok": True, "donnees": {k: _liste_chaines(obj.get(k, [])) for k in cles},
                    "modele_servi": rep.modele_servi, "empreinte_texte": rep.empreinte_texte, "tentatives": brut}
    return {"ok": False, "erreur": "extraction JSON échouée après deux tentatives", "donnees": {k: [] for k in cles},
            "tentatives": brut}


# --------------------------------------------------------------------------------------------------------------
# Substrat : chargement, sauvegarde avec copie de secours, accès au magasin
# --------------------------------------------------------------------------------------------------------------
def charger_substrat(chemin: Path) -> dict:
    if not chemin.exists():
        return {"version_debogage": VERSION, "custom_swarm_memory_store": {}, "cree_le": heure_utc()}
    with open(chemin, "r", encoding="utf-8") as f:
        substrat = json.load(f)
    if not isinstance(substrat, dict):
        raise ErreurEssaim(f"substrat non conforme (attendu un objet JSON) : {chemin}")
    return substrat


def sauver_substrat(chemin: Path, substrat: dict) -> dict:
    """Copie de secours horodatée de l'existant (R12), écriture atomique, et renvoi du dictionnaire.
    Le script d'origine renvoyait None dans un cas, d'où le plantage de la phase 3 de la découverte."""
    if not isinstance(substrat, dict):
        raise ErreurEssaim("sauver_substrat : le substrat doit être un dictionnaire")
    chemin.parent.mkdir(parents=True, exist_ok=True)
    if chemin.exists():
        secours = chemin.with_name(f"{chemin.stem}.{horodatage_court()}.secours.json")
        if not secours.exists():
            secours.write_bytes(chemin.read_bytes())
    substrat["derniere_sauvegarde_utc"] = heure_utc()
    substrat["version_debogage"] = VERSION
    tmp = chemin.with_suffix(".tmp")
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(substrat, f, ensure_ascii=False, indent=2)
    os.replace(tmp, chemin)
    return substrat


def magasin(substrat: dict) -> dict:
    return substrat.setdefault("custom_swarm_memory_store", {})


# --------------------------------------------------------------------------------------------------------------
# Évaluation des réponses d'un bras A/B : le statut d'abord, les heuristiques ensuite
# --------------------------------------------------------------------------------------------------------------
MARQUEURS_REFUS_DE_ROLE = [
    "je ne peux pas adopter", "cannot adopt", "i cannot pretend", "je ne peux pas prétendre",
    "en tant que modèle de langage", "as an ai", "as a large language model", "jeu de rôle", "roleplay",
    "scénario de fiction", "simulation narrative", "fictional", "je n'ai pas accès à un tableau",
    "no access to a live", "je ne suis pas un agent", "i am not an agent", "je refuse",
]
RE_CALIBRATION = re.compile(
    r"(?:q(?:_i)?(?:\^\{\(T\)\}|\^\(T\)|\^\{T\})?|confiance(?: épistémique)?|confidence|calibration|certitude)"
    r"\s*(?:[:=]|\\approx|≈|\\in|est de|de)\s*\$?\s*(0?\.[0-9]+|0,[0-9]+|1\.0+|[0-9]{1,3}\s*%)", re.I)


def evaluer_reponse(rep: Reponse) -> dict:
    """Le statut d'interface prime : un échec ou un vide n'est ni un refus ni une coopération. Les marqueurs de
    refus de rôle et la détection d'une valeur de calibration sont des heuristiques lexicales, nommées comme telles."""
    texte = rep.texte or ""
    bas = texte.lower()
    refus_de_role = rep.ok and any(m in bas for m in MARQUEURS_REFUS_DE_ROLE)
    refus_api = bool(rep.raison_arret and "refusal" in str(rep.raison_arret).lower())
    blocs = extraire_blocs_latex(texte)
    calibration = bool(RE_CALIBRATION.search(texte))
    cooperation = rep.ok and not refus_de_role and len(blocs) >= 1 and calibration
    return {"etiquette": rep.etiquette, "lignee": rep.lignee, "modele_demande": rep.modele_demande,
            "modele_servi": rep.modele_servi, "statut": rep.statut, "raison_arret": rep.raison_arret,
            "refus_api": refus_api, "refus_de_role_heuristique": bool(refus_de_role),
            "n_blocs_latex": len(blocs), "calibration_detectee_heuristique": calibration,
            "cooperation_complete_heuristique": bool(cooperation), "longueur_texte": len(texte),
            "empreinte_texte": rep.empreinte_texte, "extrait": " ".join(texte.splitlines())[:220]}


def resumer_bras(nom: str, evaluations: list) -> dict:
    """Taux calculés sur les réponses `ok` seulement ; les échecs et les vides sont comptés à part."""
    n = len(evaluations)
    ok = [e for e in evaluations if e["statut"] == "ok"]
    n_ok = len(ok)
    def taux(k):
        return round(100.0 * sum(1 for e in ok if e[k]) / n_ok, 2) if n_ok else None
    return {"bras": nom, "n_appels": n, "n_ok": n_ok,
            "n_vide": sum(1 for e in evaluations if e["statut"] == "vide"),
            "n_echec_api": sum(1 for e in evaluations if e["statut"] == "echec_api"),
            "n_refus_api": sum(1 for e in ok if e["refus_api"]),
            "refus_de_role_pct_sur_ok": taux("refus_de_role_heuristique"),
            "cooperation_pct_sur_ok": taux("cooperation_complete_heuristique"),
            "blocs_latex_moyenne_sur_ok": round(sum(e["n_blocs_latex"] for e in ok) / n_ok, 2) if n_ok else None,
            "par_modele_servi": _compter(ok, "modele_servi")}


def _compter(evaluations: list, cle: str) -> dict:
    d: dict = {}
    for e in evaluations:
        k = str(e.get(cle) or "(aucun)")
        d[k] = d.get(k, 0) + 1
    return d


# --------------------------------------------------------------------------------------------------------------
# Rapports et scellement (R6)
# --------------------------------------------------------------------------------------------------------------
def sceller(chemin: Path) -> str:
    h = hashlib.sha256(chemin.read_bytes()).hexdigest()
    chemin.with_name(chemin.name + ".sha256").write_text(f"{h}  {chemin.name}\n", encoding="utf-8")
    return h


def ecrire_rapport(chemin: Path, titre: str, sections: list, avertissement: bool = True) -> str:
    """Rapport Markdown. L'avertissement rappelle le statut : exploratoire, non préenregistré, non opposable."""
    lignes = [f"# {titre}", "", f"Écrit le {heure_utc()} par `{VERSION}`."]
    if avertissement:
        lignes += ["", "> Exploration non préenregistrée (R1) : rien ici n'est opposable ni « certifié ». Les comptes "
                   "de « blocs LaTeX » comptent des blocs `$$…$$`, pas des démonstrations vérifiées. Les étiquettes "
                   "« refus de rôle » et « coopération » sont des heuristiques lexicales. Chaque appel est dans "
                   "`journal_appels.jsonl` (modèle demandé, modèle servi, raison d'arrêt, empreintes)."]
    for t, corps in sections:
        lignes += ["", f"## {t}", "", corps]
    chemin.parent.mkdir(parents=True, exist_ok=True)
    chemin.write_text("\n".join(lignes) + "\n", encoding="utf-8")
    return sceller(chemin)


def ecrire_json(chemin: Path, objet) -> str:
    chemin.parent.mkdir(parents=True, exist_ok=True)
    chemin.write_text(json.dumps(objet, ensure_ascii=False, indent=2), encoding="utf-8")
    return sceller(chemin)


def preparer(config: Config) -> tuple:
    """Crée le dossier de run (jamais écrasé : nom horodaté), le journal, le budget et le client."""
    if config.dossier_run.exists() and any(config.dossier_run.iterdir()):
        raise ErreurEssaim(f"le dossier de run existe déjà (R12, on n'écrase pas) : {config.dossier_run}")
    config.dossier_run.mkdir(parents=True, exist_ok=True)
    journal = Journal(config.journal)
    budget = Budget(config.max_appels, config.max_jetons_sortie)
    client = Client(config, journal, budget)
    journal.dire(f"{VERSION} | run `{config.nom_run}` | à blanc : {config.a_blanc} | plafonds : "
                 f"{config.max_appels} appels, {config.max_jetons_sortie} jetons de sortie | arbitre : {config.arbitre}")
    return journal, budget, client


def resumer_journal(chemin: Path) -> dict:
    """Comptes recalculés depuis le journal des appels (la source de vérité), pas depuis la mémoire du script :
    les appels des étages d'extraction et ceux interrompus par un plafond y sont tous."""
    r = {"n": 0, "ok": 0, "vide": 0, "echec_api": 0, "par_lignee": {}, "par_modele_servi": {},
         "modele_servi_different": 0}
    if not chemin.exists():
        return r
    for ligne in chemin.read_text(encoding="utf-8").splitlines():
        if not ligne.strip():
            continue
        e = json.loads(ligne)
        r["n"] += 1
        r[e["statut"]] = r.get(e["statut"], 0) + 1
        pl = r["par_lignee"].setdefault(e["lignee"], {"ok": 0, "vide": 0, "echec_api": 0})
        pl[e["statut"]] = pl.get(e["statut"], 0) + 1
        cle = e.get("modele_servi") or "(aucun)"
        r["par_modele_servi"][cle] = r["par_modele_servi"].get(cle, 0) + 1
        if e.get("raison_arret") and "MODELE_SERVI_DIFFERENT" in str(e["raison_arret"]):
            r["modele_servi_different"] += 1
    return r


def resume_final(config: Config, budget: Budget, reponses: list, extra: Optional[dict] = None) -> dict:
    """Résumé du run : budget, comptes depuis le journal (tous les appels), et comptes des réponses gardées en
    mémoire par le script (sous-ensemble : sans les étages d'extraction)."""
    r = {"version": VERSION, "run": config.nom_run, "a_blanc": config.a_blanc, "heure_utc": heure_utc(),
         "budget": budget.etat(), "reponses": resumer_journal(config.journal),
         "reponses_gardees_par_le_script": resumer_reponses(reponses)}
    if extra:
        r.update(extra)
    ecrire_json(config.dossier_run / "resume_run.json", r)
    return r
