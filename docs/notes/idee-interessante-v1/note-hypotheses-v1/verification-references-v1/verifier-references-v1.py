"""Vérifie chaque référence en ligne : Crossref (DOI ou recherche), arXiv, OpenLibrary.
Écrit un JSON de résultats et un relevé lisible."""
import json, sys, time, urllib.parse, urllib.request, re, datetime
sys.path.insert(0, sys.argv[1])
import importlib, os; REFS = importlib.import_module(os.environ.get("REFMOD","refs")).REFS

UA = {"User-Agent": "verif-references/1.0 (note de travail)"}

def get(url, timeout=30):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read().decode("utf-8", "replace")

def crossref_doi(doi):
    j = json.loads(get("https://api.crossref.org/works/" + urllib.parse.quote(doi)))["message"]
    return summarize(j)

def summarize(j):
    t = (j.get("title") or [""])[0]
    c = (j.get("container-title") or [""])
    c = c[0] if c else ""
    y = None
    for k in ("published-print", "published-online", "issued", "published"):
        if j.get(k) and j[k].get("date-parts") and j[k]["date-parts"][0][0]:
            y = j[k]["date-parts"][0][0]; break
    au = [a.get("family", a.get("name", "")) for a in j.get("author", [])][:6]
    return {"doi": j.get("DOI"), "title": t, "container": c, "year": y, "authors": au,
            "volume": j.get("volume"), "issue": j.get("issue"), "page": j.get("page"),
            "article": j.get("article-number"), "type": j.get("type")}

def crossref_q(q):
    u = "https://api.crossref.org/works?rows=3&query.bibliographic=" + urllib.parse.quote(q)
    items = json.loads(get(u))["message"]["items"]
    return [summarize(i) for i in items]

def arxiv(aid):
    x = get("https://export.arxiv.org/api/query?id_list=" + aid)
    titles = re.findall(r"<title>(.*?)</title>", x, re.S)
    pub = re.findall(r"<published>(.*?)</published>", x)
    auth = re.findall(r"<name>(.*?)</name>", x)
    return {"arxiv": aid, "title": " ".join(titles[1].split()) if len(titles) > 1 else None,
            "published": pub[0] if pub else None, "authors": auth[:6]}

def openlib(title, author):
    u = ("https://openlibrary.org/search.json?limit=3&fields=title,author_name,first_publish_year,isbn,key&title="
         + urllib.parse.quote(title) + "&author=" + urllib.parse.quote(author))
    d = json.loads(get(u))["docs"]
    return [{"title": x.get("title"), "authors": x.get("author_name", [])[:3], "year": x.get("first_publish_year"),
             "isbn": (x.get("isbn") or [None])[:2], "key": x.get("key")} for x in d]

out = {"date_utc": datetime.datetime.utcnow().isoformat() + "Z", "resultats": {}}
for key, kind, ident in REFS:
    try:
        if kind == "doi":
            r = crossref_doi(ident)
        elif kind == "q":
            r = crossref_q(ident)
        elif kind == "arxiv":
            r = arxiv(ident)
        else:
            r = openlib(*ident)
        out["resultats"][key] = {"type": kind, "requete": ident, "ok": True, "reponse": r}
    except Exception as e:
        out["resultats"][key] = {"type": kind, "requete": ident, "ok": False, "erreur": repr(e)}
    time.sleep(0.3)
json.dump(out, open(sys.argv[2], "w"), ensure_ascii=False, indent=1)
for k, v in out["resultats"].items():
    if not v["ok"]:
        print(f"{k:22s} ÉCHEC {v['erreur'][:80]}"); continue
    r = v["reponse"]
    if isinstance(r, list):
        r0 = r[0] if r else {}
        print(f"{k:22s} [{v['type']}] {r0.get('doi') or r0.get('key')} | {str(r0.get('title'))[:80]} | {r0.get('year')} | {r0.get('authors')}")
    else:
        print(f"{k:22s} [{v['type']}] {r.get('doi') or r.get('arxiv')} | {str(r.get('title'))[:80]} | {r.get('year') or r.get('published')} | {r.get('container','')[:40]} {r.get('volume')}({r.get('issue')}) {r.get('page') or r.get('article')}")
