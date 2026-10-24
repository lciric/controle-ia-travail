"""Recherche documentaire servie par le noyau (décision de Lazar du 24 octobre 2026, 17:47, heure de Paris : nœud 1,
option (b) — « `rechercher()` servie par le noyau, journalisée »).

Le moissonneur de Gemini (dossier 17) faisait ses requêtes depuis le processus qui tenait les clés, avec une adresse
corrompue et des exceptions avalées. Ici :
- l'organisme ne touche jamais le réseau : il demande `rechercher(requete, n)` au noyau par le socket ;
- le noyau interroge un seul hôte (arXiv, interface Atom, lecture seule), avec délai, taille bornée, et refuse toute
  redirection hors de cet hôte ;
- chaque requête est journalisée (`journal-recherches.jsonl` : requête, empreintes de la requête et de la réponse
  brute, nombre de résultats, statut, heures) et la réponse brute est gardée (`recherches/<id>.brut`) pour l'audit ;
- un plafond par génération (`recherches_max`) : au-delà, statut `PLAFOND` ; une erreur réseau est un statut
  `ECHEC_RECHERCHE` avec une liste vide, jamais un texte d'erreur déguisé en résultat (B-03) ;
- les résultats sont des données rendues à l'organisme (titre, auteurs, date, résumé tronqué, lien) ; le noyau ne
  les exécute ni ne les interprète.
En simulation, un double (`recherche_simulee`) rend des notices déterministes sans réseau.
"""
from __future__ import annotations

import datetime as _dt
import hashlib
import json
import pathlib
import threading
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

HOTE_ARXIV = "export.arxiv.org"
N_MAX = 10
REQUETE_MAX = 300
RESUME_MAX = 1200
REPONSE_MAX_OCTETS = 2_000_000
DELAI_S = 25.0
NS_ATOM = {"a": "http://www.w3.org/2005/Atom"}


def _heure() -> str:
    return _dt.datetime.now(_dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%fZ")


def _empreinte(donnees: bytes | str) -> str:
    if isinstance(donnees, str):
        donnees = donnees.encode("utf-8")
    return hashlib.sha256(donnees).hexdigest()


def analyser_atom_arxiv(brut: bytes) -> list[dict]:
    """Notices d'une réponse Atom d'arXiv ; ne lève que sur un document illisible."""
    racine = ET.fromstring(brut)
    notices = []
    for e in racine.findall("a:entry", NS_ATOM):
        ident = (e.findtext("a:id", default="", namespaces=NS_ATOM) or "").strip()
        titre = " ".join((e.findtext("a:title", default="", namespaces=NS_ATOM) or "").split())
        resume = " ".join((e.findtext("a:summary", default="", namespaces=NS_ATOM) or "").split())
        auteurs = [" ".join((a.findtext("a:name", default="", namespaces=NS_ATOM) or "").split()) for a in e.findall("a:author", NS_ATOM)]
        date = (e.findtext("a:published", default="", namespaces=NS_ATOM) or "").strip()[:10]
        if titre or ident:
            notices.append({"source": "arxiv", "id": ident, "titre": titre, "auteurs": [a for a in auteurs if a][:8],
                            "date": date, "resume": resume[:RESUME_MAX], "lien": ident})
    return notices


def arxiv_rechercher(requete: str, n: int, delai_s: float = DELAI_S) -> tuple[list[dict], bytes]:
    """Interroge arXiv (lecture seule, un seul hôte, redirection hors hôte refusée) ; rend (notices, réponse brute)."""
    url = "https://" + HOTE_ARXIV + "/api/query?" + urllib.parse.urlencode(
        {"search_query": f"all:{requete}", "start": 0, "max_results": int(n), "sortBy": "relevance"})
    req = urllib.request.Request(url, headers={"User-Agent": "essaim-m3-noyau/1.0 (recherche journalisee, lecture seule)"})
    with urllib.request.urlopen(req, timeout=delai_s) as r:
        hote = urllib.parse.urlparse(r.geturl()).hostname
        if hote != HOTE_ARXIV:
            raise RuntimeError(f"redirection hors hôte refusée : {hote!r}")
        brut = r.read(REPONSE_MAX_OCTETS + 1)
    if len(brut) > REPONSE_MAX_OCTETS:
        raise RuntimeError("réponse trop volumineuse")
    return analyser_atom_arxiv(brut), brut


def recherche_simulee(rng=None):
    """Double sans réseau : notices déterministes tirées de la requête (par empreinte de la requête, pas du générateur ; `rng` est accepté pour la symétrie des fabriques). Quand la requête nomme
    une catégorie d'indice de la banque de simulation (ses mots séparés par des tirets), une notice en donne la phrase
    et la catégorie : c'est ainsi qu'une recherche peut « apprendre » quelque chose aux espèces simulées."""
    from .taches import CATEGORIES, PHRASES_INDICE

    def backend(requete: str, n: int) -> tuple[list[dict], bytes]:
        mots = [m for m in requete.lower().replace("-", " ").split() if len(m) >= 3]
        notices = []
        for fam, cats in CATEGORIES.items():
            for c in cats:
                if all(m in mots for m in c.split("-")):
                    notices.append({"source": "simulation", "id": f"sim:{c}", "titre": f"Note sur l'indice « {c} » ({fam})",
                                    "auteurs": ["Espèce simulée"], "date": "2026-01-01",
                                    "resume": f"Indice observé dans les cas positifs : « {PHRASES_INDICE[c]} » (catégorie {c}).",
                                    "lien": f"sim:{c}"})
        k = 0
        while len(notices) < n and k < n:
            graine = int(hashlib.sha256(f"{requete}|{k}".encode("utf-8")).hexdigest()[:8], 16)
            notices.append({"source": "simulation", "id": f"sim:{graine:08x}", "titre": f"Notice simulée {k + 1} pour « {requete[:40]} »",
                            "auteurs": ["Auteur simulé"], "date": "2025-06-01",
                            "resume": f"Résumé simulé n° {k + 1} : rien de vérifiable ici ; mots de la requête : {' '.join(mots[:6])}.",
                            "lien": f"sim:{graine:08x}"})
            k += 1
        brut = json.dumps(notices, ensure_ascii=False).encode("utf-8")
        return notices[:n], brut

    backend.source = "simulation"
    return backend


class Rechercheur:
    """Un rechercheur par génération : plafond, journal, réponses brutes. Sûr sous fils."""

    def __init__(self, dossier: str | pathlib.Path, recherches_max: int, backend=None, source: str = "arxiv", telechargeur=None):
        """`backend` : un double (simulation) qui sert toutes les sources ; sinon les sources réelles de `moisson.sources_disponibles()`
        (arXiv, OpenAlex, Semantic Scholar, web par clé). `telechargeur` : reçoit les liens rendus (chaîne de provenance)."""
        self.dossier = pathlib.Path(dossier)
        (self.dossier / "recherches").mkdir(parents=True, exist_ok=True)
        self.journal = self.dossier / "journal-recherches.jsonl"
        self.recherches_max = max(0, int(recherches_max))
        self.backend = backend
        self.source = source if backend is None else getattr(backend, "source", source)
        self.telechargeur = telechargeur
        self.compteur = 0
        self._verrou = threading.Lock()

    def sources(self) -> list[str]:
        if self.backend is not None:
            return ["arxiv", "openalex", "semanticscholar", "web", "simulation"]
        from .moisson import sources_disponibles
        import os
        return [n for n in sources_disponibles() if n != "web" or os.environ.get("BRAVE_API_KEY")]

    def _moteur(self, source: str):
        if self.backend is not None:
            return self.backend
        from .moisson import sources_disponibles
        return sources_disponibles()[source]

    def _journaliser(self, ligne: dict):
        with self.journal.open("a", encoding="utf-8") as fh:
            fh.write(json.dumps(ligne, ensure_ascii=False, sort_keys=True) + "\n")

    def rechercher(self, requete, n=5, role: str = "", source: str | None = None) -> dict:
        source = (source or self.source or "arxiv")
        if not isinstance(source, str) or source not in self.sources():
            return {"statut": "SOURCE_INCONNUE", "source": str(source)[:40], "resultats": [], "identifiant": None,
                    "echec": f"source inconnue ou non configurée ; sources : {self.sources()}"}
        if not isinstance(requete, str) or not requete.strip() or len(requete) > REQUETE_MAX:
            return {"statut": "ANOMALIE", "source": source, "resultats": [], "identifiant": None,
                    "echec": f"requête vide, non textuelle ou plus longue que {REQUETE_MAX} caractères"}
        try:
            n = max(1, min(N_MAX, int(n)))
        except (TypeError, ValueError):
            n = 5
        requete = requete.strip()
        with self._verrou:
            if self.compteur >= self.recherches_max:
                self._journaliser({"id": None, "role": role, "requete": requete, "sha256_requete": _empreinte(requete), "n_demande": n,
                                   "statut": "PLAFOND", "quand_utc": _heure(), "source": source})
                return {"statut": "PLAFOND", "source": source, "resultats": [], "identifiant": None,
                        "echec": f"plafond de {self.recherches_max} recherches atteint"}
            self.compteur += 1
            ident = f"recherche-{self.compteur:04d}"
        debut = _heure()
        try:
            resultats, brut = self._moteur(source)(requete, n)
            statut, echec = "OK", None
        except Exception as e:  # réseau, analyse, hôte : jamais un texte d'erreur en guise de résultat
            resultats, brut, statut, echec = [], b"", "ECHEC_RECHERCHE", f"{type(e).__name__}: {str(e)[:200]}"
        fin = _heure()
        if self.telechargeur is not None and resultats:
            self.telechargeur.noter_resultats(resultats)
        with self._verrou:
            (self.dossier / "recherches" / f"{ident}.brut").write_bytes(brut)
            self._journaliser({"id": ident, "role": str(role)[:40], "requete": requete, "sha256_requete": _empreinte(requete),
                               "n_demande": n, "n_rendus": len(resultats), "sha256_brut": _empreinte(brut), "octets_brut": len(brut),
                               "statut": statut, "echec": echec, "debut_utc": debut, "fin_utc": fin, "source": source})
        return {"statut": statut, "source": source, "resultats": resultats[:n], "identifiant": ident, "echec": echec}

    def lire_journal(self) -> list[dict]:
        if not self.journal.exists():
            return []
        return [json.loads(l) for l in self.journal.read_text(encoding="utf-8").splitlines() if l.strip()]
