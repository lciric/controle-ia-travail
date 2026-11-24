#!/usr/bin/env python3
"""Vérification des références du papier D contre la source qui fait foi (R7).

Pour chaque entrée de references-a-verifier-v1.json :
  - arXiv : notice de l'interface d'arXiv (titre, auteurs, date, version) ; PDF versionné téléchargé
    dans --pdf (hors dépôt), empreinte SHA-256, nombre de pages, titre lu sur la page 1 (pdftotext) ;
  - DOI : notice de l'éditeur via Crossref (titre, premier auteur, année, revue, volume, pages) ;
  - requête : recherche bibliographique Crossref puis arXiv ; la meilleure notice est proposée,
    jamais acceptée d'office : le verdict exige titre et premier auteur concordants ;
  - web : page récupérée, statut HTTP et présence du titre.
Verdicts : CONCORDE (titre et premier auteur concordent, année à un an près),
ECART (notice trouvée, au moins un champ diffère : à corriger dans nos textes),
INTROUVABLE (aucune notice fiable), PDF_NON_ACCESSIBLE est noté à part.
Usage : PYTHONDONTWRITEBYTECODE=1 python3 verifier_references_v1.py --pdf DOSSIER_HORS_DEPOT --out DOSSIER
"""
from __future__ import annotations
import argparse, hashlib, json, re, subprocess, sys, time, unicodedata, urllib.parse, urllib.request
import xml.etree.ElementTree as ET
from difflib import SequenceMatcher
from pathlib import Path

UA = {"User-Agent": "reference-checker/1.0 (research verification script)"}

def get(url, binary=False, tries=3):
    for k in range(tries):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60) as r:
                data = r.read(); return r.status, (data if binary else data.decode("utf-8", "replace"))
        except urllib.error.HTTPError as e:
            if e.code in (404, 410): return e.code, None
            time.sleep(3 * (k + 1))
        except Exception:  # noqa: BLE001
            time.sleep(3 * (k + 1))
    return None, None

def norm(s):
    s = unicodedata.normalize("NFKD", s or "").encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]+", " ", s).strip()

def sim(a, b): return SequenceMatcher(None, norm(a), norm(b)).ratio()

def surname_ok(claimed, authors):
    c = norm(claimed).split()
    return bool(authors) and any(w in norm(authors[0]) for w in c if len(w) > 2)

ATOM = {"a": "http://www.w3.org/2005/Atom", "arxiv": "http://arxiv.org/schemas/atom"}

def arxiv_meta(aid):
    st, txt = get(f"https://export.arxiv.org/api/query?id_list={aid}")
    if not txt: return None
    e = ET.fromstring(txt).find("a:entry", ATOM)
    if e is None or e.find("a:title", ATOM) is None: return None
    idv = e.find("a:id", ATOM).text.rsplit("/", 1)[-1]
    return {"titre": " ".join(e.find("a:title", ATOM).text.split()),
            "auteurs": [a.find("a:name", ATOM).text for a in e.findall("a:author", ATOM)],
            "annee_premiere_version": int(e.find("a:published", ATOM).text[:4]),
            "annee_derniere_version": int(e.find("a:updated", ATOM).text[:4]),
            "version": idv, "doi_journal": (e.find("arxiv:doi", ATOM).text if e.find("arxiv:doi", ATOM) is not None else None),
            "revue": (e.find("arxiv:journal_ref", ATOM).text if e.find("arxiv:journal_ref", ATOM) is not None else None)}

def arxiv_search(q):
    st, txt = get("https://export.arxiv.org/api/query?" + urllib.parse.urlencode({"search_query": f'ti:"{q}"', "max_results": 3}))
    if not txt: return None
    for e in ET.fromstring(txt).findall("a:entry", ATOM):
        aid = e.find("a:id", ATOM).text.rsplit("/abs/", 1)[-1]
        return re.sub(r"v\d+$", "", aid)
    return None

def crossref_doi(doi):
    st, txt = get("https://api.crossref.org/works/" + urllib.parse.quote(doi))
    return parse_cr(json.loads(txt)["message"]) if txt else None

def crossref_query(q):
    st, txt = get("https://api.crossref.org/works?" + urllib.parse.urlencode({"query.bibliographic": q, "rows": 3}))
    if not txt: return []
    return [parse_cr(m) for m in json.loads(txt)["message"]["items"]]

def parse_cr(m):
    au = [(" ".join(filter(None, [a.get("given"), a.get("family")])) or a.get("name", "")) for a in m.get("author", [])]
    if not au and m.get("editor"): au = [" ".join(filter(None, [a.get("given"), a.get("family")])) for a in m["editor"]]
    y = None
    for k in ("published-print", "issued", "published-online", "created"):
        if m.get(k, {}).get("date-parts") and m[k]["date-parts"][0][0]: y = m[k]["date-parts"][0][0]; break
    return {"titre": " ".join((m.get("title") or [""])[0].split()), "auteurs": au, "annee": y, "doi": m.get("DOI"),
            "revue": (m.get("container-title") or [None])[0], "volume": m.get("volume"), "pages": m.get("page"),
            "type": m.get("type"), "editeur": m.get("publisher")}

def pdf_check(aid_v, pdfdir):
    st, data = get(f"https://arxiv.org/pdf/{aid_v}", binary=True)
    if not data or not data.startswith(b"%PDF"): return {"pdf": "PDF_NON_ACCESSIBLE"}
    f = pdfdir / f"{aid_v}.pdf"; f.write_bytes(data)
    txt = subprocess.run(["pdftotext", "-f", "1", "-l", "1", str(f), "-"], capture_output=True, text=True).stdout
    pages = re.search(r"Pages:\s+(\d+)", subprocess.run(["pdfinfo", str(f)], capture_output=True, text=True).stdout)
    return {"pdf": "OK", "url_pdf": f"https://arxiv.org/pdf/{aid_v}", "sha256_pdf": hashlib.sha256(data).hexdigest(),
            "pages": int(pages.group(1)) if pages else None, "page1_debut": " ".join(txt.split())[:300]}

def verdict(ref, titre, auteurs, annee):
    t = sim(ref["titre"], titre); a = surname_ok(ref["auteur"], auteurs)
    y = annee is None or abs(int(annee) - int(ref["annee"])) <= 1
    return ("CONCORDE" if (t >= 0.9 and a and y) else "ECART"), round(t, 3), a, y

def main(argv=None):
    ap = argparse.ArgumentParser(); ap.add_argument("--pdf", required=True); ap.add_argument("--out", required=True)
    ap.add_argument("--entree", default=str(Path(__file__).with_name("references-a-verifier-v1.json")))
    a = ap.parse_args(argv)
    pdfdir = Path(a.pdf); pdfdir.mkdir(parents=True, exist_ok=True)
    out = Path(a.out); out.mkdir(parents=True, exist_ok=True)
    refs = json.loads(Path(a.entree).read_text()); res = []
    for r in refs:
        row = {"cle": r["cle"], "revendique": {k: r[k] for k in ("titre", "auteur", "annee")}}
        try:
            aid = r.get("arxiv")
            if not aid and r.get("requete") and not r.get("doi"):
                cands = [c for c in crossref_query(r["requete"]) if c["titre"]]
                best = max(cands, key=lambda c: sim(r["titre"], c["titre"]), default=None)
                if best and verdict(r, best["titre"], best["auteurs"], best["annee"])[0] == "CONCORDE":
                    row["source"] = "crossref (recherche)"; row["notice"] = best
                else:
                    time.sleep(3); aid = arxiv_search(r["titre"])
                    if not aid:
                        row["source"] = "crossref (recherche)" if best else None; row["notice"] = best
            if aid:
                time.sleep(3); m = arxiv_meta(aid)
                if m:
                    row["source"] = "arxiv"; row["notice"] = m; row["arxiv"] = aid
                    time.sleep(3); row.update(pdf_check(m["version"], pdfdir))
            elif r.get("doi"):
                m = crossref_doi(r["doi"]); row["source"] = "crossref (doi)"; row["notice"] = m
            elif r.get("web"):
                st, txt = get(r["web"]); row["source"] = "web"
                row["notice"] = {"statut_http": st, "titre_present": bool(txt and norm(r["titre"]) in norm(txt))}
            n = row.get("notice")
            if not n: row["verdict"] = "INTROUVABLE"
            elif row["source"] == "web":
                row["verdict"] = "CONCORDE" if n["titre_present"] else "ECART"
            else:
                ann = n.get("annee") or n.get("annee_premiere_version")
                v, t, au, y = verdict(r, n["titre"], n["auteurs"], ann)
                if row["source"] == "arxiv" and not y:
                    y2 = abs(n["annee_derniere_version"] - r["annee"]) <= 1
                    if y2 and t >= 0.9 and au: v = "CONCORDE"
                row.update({"verdict": v, "similarite_titre": t, "premier_auteur_ok": au, "annee_ok": y})
        except Exception as e:  # noqa: BLE001 — journalisé, jamais un résultat silencieux
            row["verdict"] = "ERREUR_TECHNIQUE"; row["erreur"] = repr(e)
        res.append(row); print(r["cle"], row.get("verdict"), row.get("similarite_titre"), flush=True)
    fn = out / "verification-references-v1.json"
    fn.write_text(json.dumps(res, indent=1, ensure_ascii=False) + "\n")
    Path(str(fn) + ".sha256").write_text(f"{hashlib.sha256(fn.read_bytes()).hexdigest()}  {fn.name}\n")

if __name__ == "__main__":
    main()
