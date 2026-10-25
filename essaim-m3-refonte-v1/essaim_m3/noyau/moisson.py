"""Moisson servie par le noyau — primitives seulement (décisions de Lazar du 24 octobre 2026, 20:32 à 20:35, heure de
Paris : « l'organisme doit lui-même concevoir le moissonneur » ; le noyau ne fournit que des tuyaux à portes).

- `SOURCES` : moteurs de recherche interrogeables par `rechercher(requete, n, source)` — `arxiv` (Atom, dans
  `recherche.py`), `openalex`, `semanticscholar` (interfaces ouvertes, sans clé), `web` (Brave Search, clé
  `BRAVE_API_KEY` lue par le noyau seul, jamais donnée à l'organisme). Chaque source rend des notices de même forme :
  {"source", "id", "titre", "auteurs", "date", "resume", "lien"} ; le noyau ne les interprète pas.
- `Telechargeur` : `telecharger(reference)` rapporte un document — une adresse https vue dans un résultat de recherche
  de la même génération, un identifiant arXiv, ou une adresse d'un hôte toujours permis — sous plafonds (nombre,
  octets par document, octets par génération) ; extrait le texte (HTML par analyse, PDF par `pdftotext`, texte et
  JSON tels quels), **empreinte** le document brut et le texte, les range dans `corpus/` (brut, texte, notice), tient
  `corpus/index.jsonl` (scellé en fin de génération). Le texte est rendu à l'organisme **comme donnée** (le contrat
  le dit : jamais une consigne). Aucune exécution, aucune redirection hors https, aucune erreur rendue comme texte.
- En simulation : `telechargement_simule` rend un texte déterministe pour les liens `sim:<catégorie>` du double de
  recherche (la phrase d'indice de la catégorie), ce qui permet à un organisme simulé d'« apprendre » en moissonnant.
"""
from __future__ import annotations

import datetime as _dt
import hashlib
import html.parser
import json
import os
import pathlib
import re
import shutil
import subprocess
import threading
import urllib.parse
import urllib.request

RESUME_MAX = 1200
REPONSE_MAX_OCTETS = 2_000_000
DELAI_S = 25.0
EXTRACTION_MAX_S = 120          # extraction d'un PDF (pdftotext) au plus ; compte dans la garde de temps CE-07 (CE3-11)
TEXTE_MAX_RENDU = 60_000            # caractères de texte rendus à l'organisme par document (le reste est dans corpus/)
OCTETS_MAX_DOC = 8_000_000
OCTETS_MAX_GENERATION = 40_000_000
TELECHARGEMENTS_MAX_DEFAUT = 20
HOTES_TOUJOURS_PERMIS = {"arxiv.org", "export.arxiv.org", "api.openalex.org", "openalex.org", "api.semanticscholar.org",
                         "www.semanticscholar.org", "www.alignmentforum.org", "alignmentforum.org", "www.lesswrong.com", "lesswrong.com"}
AGENT = "essaim-m3-noyau/1.0 (moisson journalisee, lecture seule)"


def _heure() -> str:
    return _dt.datetime.now(_dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%fZ")


def _empreinte(donnees: bytes | str) -> str:
    if isinstance(donnees, str):
        donnees = donnees.encode("utf-8")
    return hashlib.sha256(donnees).hexdigest()


def _lire_https(url: str, octets_max: int, delai_s: float = DELAI_S, entetes: dict | None = None,
                hotes_permis: set[str] | None = None) -> tuple[bytes, str, str]:
    """Lit une adresse https (redirections https seulement, hôte final vérifié) ; rend (octets, type de contenu, adresse finale)."""
    if not url.lower().startswith("https://"):
        raise RuntimeError("seules les adresses https sont lues")
    req = urllib.request.Request(url, headers={"User-Agent": AGENT, **(entetes or {})})
    with urllib.request.urlopen(req, timeout=delai_s) as r:
        finale = r.geturl()
        hote = (urllib.parse.urlparse(finale).hostname or "").lower()
        if not finale.lower().startswith("https://"):
            raise RuntimeError("redirection hors https refusée")
        if hotes_permis is not None and hote not in hotes_permis:
            raise RuntimeError(f"redirection vers un hôte non permis : {hote!r}")
        brut = r.read(octets_max + 1)
        type_contenu = (r.headers.get("Content-Type") or "").split(";")[0].strip().lower()
    if len(brut) > octets_max:
        raise RuntimeError(f"document plus grand que {octets_max} octets")
    return brut, type_contenu, finale


# ------------------------------------------------------------------ sources de recherche ----
def _abstract_openalex(inv: dict | None) -> str:
    if not isinstance(inv, dict) or not inv:
        return ""
    positions: dict[int, str] = {}
    for mot, idx in inv.items():
        for i in idx if isinstance(idx, list) else []:
            if isinstance(i, int):
                positions[i] = mot
    return " ".join(positions[i] for i in sorted(positions))


def openalex_rechercher(requete: str, n: int) -> tuple[list[dict], bytes]:
    """R-410 : clé OpenAlex lue par le noyau seul (`OPENALEX_API_KEY`, en-tête `Authorization: Bearer`, jamais dans
    l'adresse, jamais journalisée) ; sans clé, requête anonyme (budget quotidien partagé par l'adresse réseau)."""
    url = "https://api.openalex.org/works?" + urllib.parse.urlencode({"search": requete, "per-page": int(n)})
    cle = os.environ.get("OPENALEX_API_KEY")
    entetes = {"Authorization": "Bearer " + cle} if cle else None
    brut, _, _ = _lire_https(url, REPONSE_MAX_OCTETS, entetes=entetes, hotes_permis={"api.openalex.org"})
    d = json.loads(brut.decode("utf-8"))
    notices = []
    for w in d.get("results", []) or []:
        lieu = w.get("primary_location") or {}
        pdf = lieu.get("pdf_url") or (w.get("open_access") or {}).get("oa_url") or ""
        notices.append({"source": "openalex", "id": str(w.get("id") or ""), "titre": str(w.get("display_name") or ""),
                        "auteurs": [str(((a or {}).get("author") or {}).get("display_name") or "") for a in (w.get("authorships") or [])][:8],
                        "date": str(w.get("publication_date") or w.get("publication_year") or ""),
                        "resume": _abstract_openalex(w.get("abstract_inverted_index"))[:RESUME_MAX],
                        "lien": str(pdf or (lieu.get("landing_page_url") or "") or w.get("doi") or w.get("id") or "")})
    return notices, brut


def semanticscholar_rechercher(requete: str, n: int) -> tuple[list[dict], bytes]:
    """R-410 : clé Semantic Scholar lue par le noyau seul (`S2_API_KEY`, en-tête `x-api-key`, jamais journalisée) ;
    sans clé, requête anonyme (réserve commune des utilisateurs sans clé)."""
    url = "https://api.semanticscholar.org/graph/v1/paper/search?" + urllib.parse.urlencode(
        {"query": requete, "limit": int(n), "fields": "title,authors,year,abstract,openAccessPdf,externalIds,url,publicationDate"})
    cle = os.environ.get("S2_API_KEY")
    entetes = {"x-api-key": cle} if cle else None
    brut, _, _ = _lire_https(url, REPONSE_MAX_OCTETS, entetes=entetes, hotes_permis={"api.semanticscholar.org"})
    d = json.loads(brut.decode("utf-8"))
    notices = []
    for p in d.get("data", []) or []:
        pdf = ((p.get("openAccessPdf") or {}).get("url")) or ""
        arx = ((p.get("externalIds") or {}).get("ArXiv")) or ""
        notices.append({"source": "semanticscholar", "id": str(p.get("paperId") or ""), "titre": str(p.get("title") or ""),
                        "auteurs": [str((a or {}).get("name") or "") for a in (p.get("authors") or [])][:8],
                        "date": str(p.get("publicationDate") or p.get("year") or ""), "resume": str(p.get("abstract") or "")[:RESUME_MAX],
                        "lien": str(pdf or (f"https://arxiv.org/abs/{arx}" if arx else "") or p.get("url") or "")})
    return notices, brut


def brave_rechercher(requete: str, n: int) -> tuple[list[dict], bytes]:
    cle = os.environ.get("BRAVE_API_KEY")
    if not cle:
        raise RuntimeError("source web non configurée (BRAVE_API_KEY absente de l'environnement du noyau)")
    url = "https://api.search.brave.com/res/v1/web/search?" + urllib.parse.urlencode({"q": requete, "count": int(n)})
    brut, _, _ = _lire_https(url, REPONSE_MAX_OCTETS, entetes={"Accept": "application/json", "X-Subscription-Token": cle},
                             hotes_permis={"api.search.brave.com"})
    d = json.loads(brut.decode("utf-8"))
    notices = []
    for r in ((d.get("web") or {}).get("results") or []):
        notices.append({"source": "web", "id": str(r.get("url") or ""), "titre": str(r.get("title") or ""), "auteurs": [],
                        "date": str(r.get("age") or r.get("page_age") or ""), "resume": str(r.get("description") or "")[:RESUME_MAX],
                        "lien": str(r.get("url") or "")})
    return notices, brut


def sources_disponibles() -> dict:
    from .recherche import arxiv_rechercher
    return {"arxiv": arxiv_rechercher, "openalex": openalex_rechercher, "semanticscholar": semanticscholar_rechercher, "web": brave_rechercher}


# ------------------------------------------------------------------ extraction de texte ----
class _ExtracteurHTML(html.parser.HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.morceaux: list[str] = []
        self.titre: list[str] = []
        self._ignore = 0
        self._dans_titre = False

    def handle_starttag(self, tag, attrs):
        if tag in ("script", "style", "noscript", "svg"):
            self._ignore += 1
        if tag == "title":
            self._dans_titre = True
        if tag in ("p", "div", "br", "li", "h1", "h2", "h3", "h4", "tr", "section", "article"):
            self.morceaux.append("\n")

    def handle_endtag(self, tag):
        if tag in ("script", "style", "noscript", "svg") and self._ignore:
            self._ignore -= 1
        if tag == "title":
            self._dans_titre = False

    def handle_data(self, data):
        if self._dans_titre:
            self.titre.append(data)
        elif not self._ignore:
            self.morceaux.append(data)


def extraire_texte(brut: bytes, type_contenu: str, nom: str = "") -> tuple[str, str, str]:
    """Rend (texte, genre, titre) : genre ∈ {pdf, html, texte, json, inconnu}. Jamais d'exécution du contenu."""
    est_pdf = brut[:5] == b"%PDF-" or "pdf" in type_contenu or nom.lower().endswith(".pdf")
    if est_pdf:
        if shutil.which("pdftotext") is None:
            return "", "pdf", ""
        import tempfile
        with tempfile.TemporaryDirectory() as d:
            src = pathlib.Path(d) / "doc.pdf"
            src.write_bytes(brut)
            try:
                res = subprocess.run(["pdftotext", "-layout", "-enc", "UTF-8", str(src), "-"], capture_output=True, timeout=EXTRACTION_MAX_S)
                texte = res.stdout.decode("utf-8", errors="replace") if res.returncode == 0 else ""
            except (subprocess.TimeoutExpired, OSError):
                texte = ""
        return texte, "pdf", ""
    try:
        chaine = brut.decode("utf-8")
    except UnicodeDecodeError:
        chaine = brut.decode("latin-1", errors="replace")
    if "html" in type_contenu or re.search(r"<\s*html|<\s*body|<\s*div", chaine[:4000], flags=re.I):
        ex = _ExtracteurHTML()
        try:
            ex.feed(chaine)
        except Exception:  # analyse HTML tolérante : on garde ce qui a été lu
            pass
        texte = re.sub(r"[ \t\r\f\v]+", " ", "".join(ex.morceaux))
        texte = re.sub(r"\n\s*\n+", "\n\n", texte).strip()
        return texte, "html", " ".join("".join(ex.titre).split())[:300]
    if "json" in type_contenu:
        return chaine, "json", ""
    return chaine, "texte", ""


# ------------------------------------------------------------------ téléchargeur ----
def telechargement_simule(reference: str) -> tuple[bytes, str, str]:
    """Double sans réseau : pour un lien `sim:<catégorie>` du double de recherche, un texte qui contient la phrase
    d'indice de la catégorie ; pour toute autre référence, un texte neutre déterministe."""
    from .taches import PHRASES_INDICE
    cat = reference[4:] if reference.startswith("sim:") else ""
    if cat in PHRASES_INDICE:
        texte = (f"Document simulé sur l'indice « {cat} ».\n\nLes cas positifs de cette catégorie présentent le trait suivant : "
                 f"{PHRASES_INDICE[cat]}\n\nCe document n'a aucune valeur de preuve ; il sert au test du moissonneur.\n")
    else:
        texte = f"Document simulé pour la référence {reference!r} : aucun contenu vérifiable ({_empreinte(reference)[:12]}).\n"
    return texte.encode("utf-8"), "text/plain", reference


class _Quarantaine(Exception):
    """Lève la mise en quarantaine d'un document qui recoupe une tâche de test (CE3-04) ; porte l'empreinte du recoupement."""

    def __init__(self, empreinte: str):
        super().__init__(empreinte)
        self.empreinte = empreinte


class Telechargeur:
    """Un téléchargeur par génération : plafonds, provenance (adresses vues dans les résultats de recherche de la
    génération, identifiants arXiv, hôtes toujours permis), corpus empreinté, journal. Sûr sous fils."""

    def __init__(self, dossier_corpus: str | pathlib.Path, telechargements_max: int = TELECHARGEMENTS_MAX_DEFAUT,
                 octets_max_doc: int = OCTETS_MAX_DOC, octets_max_total: int = OCTETS_MAX_GENERATION, backend=None,
                 hotes_toujours_permis: set[str] | None = None, empreintes_fuite: set | None = None,
                 empreintes_courtes: set | None = None, journal_noyau: str | pathlib.Path | None = None):
        """`empreintes_fuite` (CE3-04) : un document qui contient un passage d'une tâche de test est mis en quarantaine ;
        `empreintes_courtes` (RV-07 ii) : recoupements courts comptés, jamais refusés ; `journal_noyau` (RV-07 iii) : journal
        du noyau, hors de la vue de la lignée, seul à recevoir les empreintes recoupées et les comptes courts (l'index du
        corpus, lisible par la lignée, ne porte que le statut)."""
        self.empreintes_fuite = empreintes_fuite or set()
        self.empreintes_courtes = empreintes_courtes or set()
        self.journal_noyau = pathlib.Path(journal_noyau) if journal_noyau is not None else None
        self.dossier = pathlib.Path(dossier_corpus)
        self.dossier.mkdir(parents=True, exist_ok=True)
        self.index = self.dossier / "index.jsonl"
        self.telechargements_max = max(0, int(telechargements_max))
        self.octets_max_doc = int(octets_max_doc)
        self.octets_max_total = int(octets_max_total)
        self.backend = backend  # None : réseau réel ; sinon fonction (référence) -> (octets, type, adresse finale)
        self.hotes_toujours_permis = set(HOTES_TOUJOURS_PERMIS if hotes_toujours_permis is None else hotes_toujours_permis)
        self.references_vues: set[str] = set()
        self.compteur = 0
        self.octets = 0
        self._verrou = threading.Lock()

    def noter_resultats(self, resultats: list[dict]) -> None:
        """Les liens rendus par une recherche de la génération deviennent téléchargeables (chaîne de provenance)."""
        with self._verrou:
            for r in resultats or []:
                for cle in ("lien", "id"):
                    v = r.get(cle)
                    if isinstance(v, str) and v:
                        self.references_vues.add(v)

    def _resoudre(self, reference: str) -> str:
        """Référence → adresse https lisible, ou RuntimeError si la provenance ne la permet pas."""
        ref = reference.strip()
        m = re.fullmatch(r"(?:arxiv:|https?://arxiv\.org/(?:abs|pdf)/)?(\d{4}\.\d{4,5}(?:v\d+)?)(?:\.pdf)?", ref)
        if m:
            return f"https://arxiv.org/pdf/{m.group(1)}"
        if self.backend is not None and ref.startswith("sim:"):
            return ref
        if not ref.lower().startswith("https://"):
            raise RuntimeError("référence non reconnue : adresse https, identifiant arXiv, ou lien d'un résultat de recherche attendu")
        hote = (urllib.parse.urlparse(ref).hostname or "").lower()
        if hote in self.hotes_toujours_permis or ref in self.references_vues:
            return ref
        raise RuntimeError(f"adresse hors provenance : {hote!r} n'est ni un hôte toujours permis ni un lien rendu par une recherche de cette génération")

    def _journaliser(self, ligne: dict) -> None:
        with self.index.open("a", encoding="utf-8") as fh:
            fh.write(json.dumps(ligne, ensure_ascii=False, sort_keys=True) + "\n")

    def telecharger(self, reference, role: str = "") -> dict:
        if not isinstance(reference, str) or not reference.strip() or len(reference) > 2000:
            return {"statut": "ANOMALIE", "identifiant": None, "echec": "référence vide, non textuelle ou trop longue"}
        with self._verrou:
            if self.compteur >= self.telechargements_max:
                self._journaliser({"id": None, "reference": reference[:500], "statut": "PLAFOND", "quand_utc": _heure(), "role": str(role)[:40]})
                return {"statut": "PLAFOND", "identifiant": None, "echec": f"plafond de {self.telechargements_max} téléchargements atteint"}
            self.compteur += 1
            ident = f"doc-{self.compteur:04d}"
        debut = _heure()
        recoupe_fuite = None
        try:
            adresse = self._resoudre(reference)
            reste = self.octets_max_total - self.octets
            if reste <= 0:
                raise RuntimeError("plafond d'octets de la génération atteint")
            if self.backend is not None:
                brut, type_contenu, finale = self.backend(adresse)
                if len(brut) > min(self.octets_max_doc, reste):
                    raise RuntimeError("document plus grand que le plafond")
            else:
                brut, type_contenu, finale = _lire_https(adresse, min(self.octets_max_doc, reste))
            texte, genre, titre = extraire_texte(brut, type_contenu, finale)
            statut, echec = ("OK" if texte.strip() else "SANS_TEXTE"), None
            from .garde_fuite import recoupement
            recoupe = recoupement(texte, self.empreintes_fuite)
            if recoupe is not None:  # CE3-04 : le document contient un passage d'une tâche de test ; quarantaine, rien n'est rendu
                raise _Quarantaine(recoupe)
        except _Quarantaine as q:
            brut, texte, genre, titre, finale, type_contenu = b"", "", "inconnu", "", reference, ""
            recoupe_fuite = q.empreinte
            statut, echec = "REFUSE_FUITE", "document en quarantaine : il contient un passage d'une tâche de test (CE3-04) ; rien n'est rendu"
        except Exception as e:  # réseau, provenance, taille, extraction : un statut, jamais un texte d'erreur en guise de document
            brut, texte, genre, titre, finale, type_contenu = b"", "", "inconnu", "", reference, ""
            statut, echec = "ECHEC_TELECHARGEMENT", f"{type(e).__name__}: {str(e)[:200]}"
        fin = _heure()
        sha_brut = _empreinte(brut) if brut else None
        sha_texte = _empreinte(texte) if texte else None
        with self._verrou:
            self.octets += len(brut)
            if brut:
                (self.dossier / f"{ident}.bin").write_bytes(brut)
                (self.dossier / f"{ident}.txt").write_text(texte, encoding="utf-8")
            notice = {"id": ident, "reference": reference[:500], "adresse": str(finale)[:1000], "type_contenu": type_contenu, "genre": genre,
                      "titre": titre, "octets": len(brut), "caracteres_texte": len(texte), "sha256_brut": sha_brut, "sha256_texte": sha_texte,
                      "statut": statut, "echec": echec, "debut_utc": debut, "fin_utc": fin, "role": str(role)[:40]}
            (self.dossier / f"{ident}.json").write_text(json.dumps(notice, ensure_ascii=False, indent=1), encoding="utf-8")
            self._journaliser(notice)
            if self.journal_noyau is not None:
                from .garde_fuite import compte_recoupements
                with self.journal_noyau.open("a", encoding="utf-8") as fh:
                    fh.write(json.dumps({"id": ident, "statut": statut, "sha256_recoupement": recoupe_fuite,
                                         "recoupements_courts": compte_recoupements(texte, self.empreintes_courtes),
                                         "quand_utc": fin}, ensure_ascii=False, sort_keys=True) + "\n")
        tronque = len(texte) > TEXTE_MAX_RENDU
        return {"statut": statut, "identifiant": ident, "adresse": str(finale)[:1000], "genre": genre, "titre": titre, "octets": len(brut),
                "sha256_brut": sha_brut, "sha256_texte": sha_texte, "texte": texte[:TEXTE_MAX_RENDU], "tronque": tronque,
                "caracteres_texte": len(texte), "fichier_texte": (str(self.dossier / f"{ident}.txt") if brut else None), "echec": echec}

    def lire_index(self) -> list[dict]:
        if not self.index.exists():
            return []
        return [json.loads(l) for l in self.index.read_text(encoding="utf-8").splitlines() if l.strip()]
