"""Récupère titre, revue et résumé (Crossref ; arXiv) pour ancrer les affirmations du cours accéléré."""
import json, re, sys, time, urllib.parse, urllib.request
UA = {"User-Agent": "verif-references/1.0 (note de travail)"}
def get(u):
    with urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=40) as r:
        return r.read().decode("utf-8", "replace")
DOIS = sys.argv[2].split(",") if len(sys.argv) > 2 else []
ARX = sys.argv[3].split(",") if len(sys.argv) > 3 else []
out = {}
for d in DOIS:
    if not d: continue
    try:
        m = json.loads(get("https://api.crossref.org/works/" + urllib.parse.quote(d)))["message"]
        a = m.get("abstract")
        out[d] = {"title": (m.get("title") or [""])[0], "container": (m.get("container-title") or [""])[0],
                  "volume": m.get("volume"), "page": m.get("page") or m.get("article-number"),
                  "authors": [x.get("family") for x in m.get("author", [])],
                  "abstract": re.sub(r"<[^>]+>", " ", a) if a else None}
    except Exception as e:
        out[d] = {"erreur": repr(e)}
    time.sleep(0.3)
for a in ARX:
    if not a: continue
    try:
        x = get("https://export.arxiv.org/api/query?id_list=" + a)
        t = re.findall(r"<title>(.*?)</title>", x, re.S); s = re.findall(r"<summary>(.*?)</summary>", x, re.S)
        out["arXiv:" + a] = {"title": " ".join(t[1].split()), "abstract": " ".join(s[0].split()) if s else None}
    except Exception as e:
        out["arXiv:" + a] = {"erreur": repr(e)}
json.dump(out, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
for k, v in out.items():
    print("===", k, "|", v.get("title"), "|", v.get("container"), v.get("volume"), v.get("page"), (v.get("authors") or [])[:4])
    print((v.get("abstract") or v.get("erreur") or "PAS DE RÉSUMÉ")[:1400])
