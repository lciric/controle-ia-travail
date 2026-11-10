"""Télécharge la dernière version de PDF d'arXiv (client générique) ; une ligne JSON par identifiant."""
import hashlib, json, re, subprocess, sys, time, urllib.parse, urllib.request
from pathlib import Path
UA = {"User-Agent": "Mozilla/5.0 (compatible; generic-fetch/1.0)"}
def lire(url):
    for attente in (0, 5, 15, 45):
        time.sleep(attente)
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=120) as f:
                return f.read()
        except Exception as e:
            err = e
    raise err
cible = Path(sys.argv[1]); ids = sys.argv[2:]; cible.mkdir(parents=True, exist_ok=True)
api = lire("https://export.arxiv.org/api/query?" + urllib.parse.urlencode({"id_list": ",".join(ids), "max_results": len(ids)})).decode()
(cible / "api.xml").write_text(api)
info = {}
for e in re.findall(r"<entry>.*?</entry>", api, flags=re.S):
    g = lambda k: [" ".join(x.split()) for x in re.findall(r"<%s[^>]*>(.*?)</%s>" % (k, k), e, flags=re.S)]
    if not g("id") or "/abs/" not in g("id")[0]: continue
    brut = g("id")[0].rsplit("/abs/", 1)[1]; pid, v = brut.rsplit("v", 1)
    info[pid] = dict(v=int(v), titre=g("title")[0], publie=g("published")[0][:10], maj=g("updated")[0][:10], auteurs=g("name"))
for pid in ids:
    if pid not in info:
        print(json.dumps({"id": pid, "erreur": "absent de la réponse de l'interface"})); continue
    i = info[pid]; nom = f"{pid}v{i['v']}.pdf"; time.sleep(3)
    try:
        o = lire(f"https://export.arxiv.org/pdf/{pid}v{i['v']}")
    except Exception as e:
        print(json.dumps({"id": pid, "erreur": repr(e)})); continue
    if o[:4] != b"%PDF":
        print(json.dumps({"id": pid, "erreur": "pas un PDF"})); continue
    (cible / nom).write_bytes(o)
    n = next((l.split()[-1] for l in subprocess.run(["pdfinfo", str(cible / nom)], capture_output=True, text=True).stdout.splitlines() if l.startswith("Pages:")), "?")
    p1 = " ".join(subprocess.run(["pdftotext", "-f", "1", "-l", "1", str(cible / nom), "-"], capture_output=True, text=True).stdout.split())[:110]
    time.sleep(3)
    try:
        lic = sorted(set(re.findall(r'href="(https?://(?:creativecommons|arxiv)\.org/licenses[^"]*)"', lire(f"https://arxiv.org/abs/{pid}v{i['v']}").decode(errors="replace"))))
    except Exception as e:
        lic = ["non relevée: " + repr(e)]
    print(json.dumps({"id": pid, "fichier": nom, "pages": n, "octets": len(o), "sha256": hashlib.sha256(o).hexdigest(), "titre": i["titre"], "auteurs": i["auteurs"][:4], "n_auteurs": len(i["auteurs"]), "publie": i["publie"], "maj": i["maj"], "licence": lic, "page1": p1, "heure": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())}, ensure_ascii=False), flush=True)
