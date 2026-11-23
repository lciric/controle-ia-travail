"""Outil de la revue bibliographique v1 (classe B, outil de travail ; sans dépense).

Résout des identifiants (DOI, arXiv) et cherche par mots-clés sur trois
interfaces gratuites : OpenAlex, Semantic Scholar, arXiv ; Crossref en appoint
pour les DOI. Chaque requête et sa réponse brute sont journalisées en JSON
Lines dans le fichier nommé par la variable BIBLIO_JOURNAL (une ligne par
requête). Les clés (OPENALEX_API_KEY, SEMANTIC_SCHOLAR_API_KEY) sont lues par
leur nom et retirées des adresses journalisées.

Usage :
    BIBLIO_JOURNAL=journal.jsonl python -I biblio_v1.py resoudre doi:10.1126/science.1240474 arxiv:2409.04109
    BIBLIO_JOURNAL=journal.jsonl python -I biblio_v1.py chercher "atypical combinations novelty" --depuis 2024 --n 10
La sortie standard est un résumé lisible (JSON) ; le brut est dans le journal.
"""
from __future__ import annotations

import argparse
import datetime as _dt
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

OA = "https://api.openalex.org"
S2 = "https://api.semanticscholar.org/graph/v1"
AX = "https://export.arxiv.org/api/query"
CR = "https://api.crossref.org/works/"
CHAMPS_S2 = "title,year,authors,venue,externalIds,publicationDate,citationCount,abstract"
_DERNIER_S2 = [0.0]


def _journal(entree: dict) -> None:
    chemin = os.environ.get("BIBLIO_JOURNAL")
    if not chemin:
        return
    with open(chemin, "a", encoding="utf-8") as f:
        f.write(json.dumps(entree, ensure_ascii=False) + "\n")


def _get(url: str, entetes: dict | None = None, interface: str = "", essais: int = 4) -> tuple[int, str]:
    url_publique = re.sub(r"([?&])api_key=[^&]*&?", r"\1", url).rstrip("?&")
    attente = 2.0
    statut, corps = 0, ""
    for essai in range(essais):
        if interface == "semanticscholar":
            delta = time.time() - _DERNIER_S2[0]
            if delta < 1.2:
                time.sleep(1.2 - delta)
            _DERNIER_S2[0] = time.time()
        req = urllib.request.Request(url, headers={"User-Agent": "revue-bibliographique/1.0", **(entetes or {})})
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                statut, corps = r.status, r.read().decode("utf-8", "replace")
        except urllib.error.HTTPError as e:
            statut, corps = e.code, e.read().decode("utf-8", "replace")
        except Exception as e:  # réseau
            statut, corps = -1, f"{type(e).__name__}: {e}"
        _journal({
            "horodatage_utc": _dt.datetime.now(_dt.timezone.utc).isoformat(timespec="seconds"),
            "interface": interface, "url": url_publique, "essai": essai + 1,
            "statut": statut, "reponse": corps,
        })
        if statut in (429, 500, 502, 503, 504, -1) and essai + 1 < essais:
            time.sleep(attente)
            attente *= 2
            continue
        break
    return statut, corps


def _oa_cle() -> str:
    k = os.environ.get("OPENALEX_API_KEY", "")
    return f"&api_key={k}" if k else ""


def _s2_entetes() -> dict:
    k = os.environ.get("SEMANTIC_SCHOLAR_API_KEY", "")
    return {"x-api-key": k} if k else {}


def _resume_oa(w: dict) -> dict:
    auteurs = [a.get("author", {}).get("display_name") for a in w.get("authorships", [])][:6]
    loc = (w.get("primary_location") or {}).get("source") or {}
    return {"interface": "openalex", "titre": w.get("title"), "annee": w.get("publication_year"),
            "date": w.get("publication_date"), "auteurs": auteurs, "lieu": loc.get("display_name"),
            "doi": w.get("doi"), "openalex": w.get("id"), "citations": w.get("cited_by_count"),
            "type": w.get("type")}


def _resume_s2(p: dict) -> dict:
    return {"interface": "semanticscholar", "titre": p.get("title"), "annee": p.get("year"),
            "date": p.get("publicationDate"), "auteurs": [a.get("name") for a in (p.get("authors") or [])][:6],
            "lieu": p.get("venue"), "ids": p.get("externalIds"), "citations": p.get("citationCount")}


def _arxiv_entrees(xml: str) -> list[dict]:
    ns = {"a": "http://www.w3.org/2005/Atom"}
    out = []
    try:
        racine = ET.fromstring(xml)
    except ET.ParseError:
        return out
    for e in racine.findall("a:entry", ns):
        titre = (e.findtext("a:title", default="", namespaces=ns) or "").strip()
        if not titre or titre == "Error":
            continue
        out.append({"interface": "arxiv", "titre": " ".join(titre.split()),
                    "date": e.findtext("a:published", default="", namespaces=ns),
                    "auteurs": [a.findtext("a:name", default="", namespaces=ns) for a in e.findall("a:author", ns)][:6],
                    "id": e.findtext("a:id", default="", namespaces=ns),
                    "resume": " ".join((e.findtext("a:summary", default="", namespaces=ns) or "").split())[:600]})
    return out


def resoudre(ident: str) -> dict:
    """Résout `doi:…` ou `arxiv:…` sur toutes les interfaces ; rend les fiches trouvées."""
    ident = ident.strip()
    genre, _, val = ident.partition(":")
    genre = genre.lower()
    fiches = []
    if genre == "doi":
        s, c = _get(f"{OA}/works/doi:{urllib.parse.quote(val, safe='/')}?x=1{_oa_cle()}", interface="openalex")
        if s == 200:
            fiches.append(_resume_oa(json.loads(c)))
        s, c = _get(f"{S2}/paper/DOI:{urllib.parse.quote(val, safe='/')}?fields={CHAMPS_S2}", _s2_entetes(), "semanticscholar")
        if s == 200:
            fiches.append(_resume_s2(json.loads(c)))
        s, c = _get(CR + urllib.parse.quote(val, safe="/"), interface="crossref")
        if s == 200:
            m = json.loads(c).get("message", {})
            fiches.append({"interface": "crossref", "titre": (m.get("title") or [None])[0],
                           "annee": ((m.get("issued") or {}).get("date-parts") or [[None]])[0][0],
                           "lieu": (m.get("container-title") or [None])[0],
                           "auteurs": [f"{a.get('given','')} {a.get('family','')}".strip() for a in m.get("author", [])][:6]})
    elif genre == "arxiv":
        val = re.sub(r"v\d+$", "", val)
        s, c = _get(f"{AX}?id_list={val}", interface="arxiv")
        if s == 200:
            fiches += _arxiv_entrees(c)
        s, c = _get(f"{OA}/works/doi:10.48550/arXiv.{val}?x=1{_oa_cle()}", interface="openalex")
        if s == 200:
            fiches.append(_resume_oa(json.loads(c)))
        s, c = _get(f"{S2}/paper/arXiv:{val}?fields={CHAMPS_S2}", _s2_entetes(), "semanticscholar")
        if s == 200:
            fiches.append(_resume_s2(json.loads(c)))
    else:
        raise SystemExit(f"identifiant inconnu : {ident!r} (attendu doi:… ou arxiv:…)")
    return {"identifiant": ident, "resolu": bool(fiches), "interfaces": sorted({f["interface"] for f in fiches}), "fiches": fiches}


def chercher(requete: str, depuis: int | None = None, n: int = 10, interfaces: str = "openalex,semanticscholar,arxiv") -> dict:
    out = {"requete": requete, "depuis": depuis, "resultats": {}}
    q = urllib.parse.quote(requete)
    if "openalex" in interfaces:
        filtre = f"&filter=from_publication_date:{depuis}-01-01" if depuis else ""
        s, c = _get(f"{OA}/works?search={q}{filtre}&per-page={n}{_oa_cle()}", interface="openalex")
        out["resultats"]["openalex"] = [_resume_oa(w) for w in json.loads(c).get("results", [])] if s == 200 else f"statut {s}"
    if "semanticscholar" in interfaces:
        an = f"&year={depuis}-" if depuis else ""
        s, c = _get(f"{S2}/paper/search?query={q}{an}&limit={n}&fields={CHAMPS_S2}", _s2_entetes(), "semanticscholar")
        out["resultats"]["semanticscholar"] = [_resume_s2(p) for p in json.loads(c).get("data", []) or []] if s == 200 else f"statut {s}"
    if "arxiv" in interfaces:
        s, c = _get(f"{AX}?search_query=all:{urllib.parse.quote(requete)}&max_results={n}&sortBy=relevance", interface="arxiv")
        res = _arxiv_entrees(c) if s == 200 else f"statut {s}"
        if depuis and isinstance(res, list):
            res = [r for r in res if r["date"][:4] >= str(depuis)]
        out["resultats"]["arxiv"] = res
    return out


def main(argv=None) -> None:
    ap = argparse.ArgumentParser()
    sp = ap.add_subparsers(dest="cmd", required=True)
    r = sp.add_parser("resoudre"); r.add_argument("ids", nargs="+")
    c = sp.add_parser("chercher"); c.add_argument("requete"); c.add_argument("--depuis", type=int); c.add_argument("--n", type=int, default=10)
    c.add_argument("--interfaces", default="openalex,semanticscholar,arxiv")
    a = ap.parse_args(argv)
    if a.cmd == "resoudre":
        res = [resoudre(i) for i in a.ids]
    else:
        res = chercher(a.requete, a.depuis, a.n, a.interfaces)
    json.dump(res, sys.stdout, ensure_ascii=False, indent=1)
    print()


if __name__ == "__main__":
    main()
