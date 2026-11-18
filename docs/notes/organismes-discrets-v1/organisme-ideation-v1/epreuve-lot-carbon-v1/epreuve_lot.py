"""Épreuve d'appel du mode par lot de Gemini pour Carbon (une requête, budget de pensée 8 192). Clé lue par son nom, jamais
affichée ; tout texte imprimé est passé au masque. Relève l'état toutes les 30 s pendant 30 min au plus, puis abandonne
(et annule le lot)."""
import json, os, ssl, sys, time, urllib.request, urllib.error
CLE = os.environ.get("GEMINI_API_KEY", "")
assert CLE, "GEMINI_API_KEY absente"
BASE = "https://generativelanguage.googleapis.com/v1beta"
ctx = ssl.create_default_context(cafile=os.environ.get("SSL_CERT_FILE") or None)
def m(t): return str(t).replace(CLE, "[clé]")
def appel(methode, url, corps=None):
    d = json.dumps(corps).encode() if corps is not None else None
    req = urllib.request.Request(url, data=d, method=methode, headers={"x-goog-api-key": CLE, "Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=60, context=ctx) as r:
            return r.status, json.loads(r.read() or b"{}")
    except urllib.error.HTTPError as e:
        return e.code, m(e.read()[:800].decode("utf-8", "replace"))
consigne = open(sys.argv[1], encoding="utf-8").read()
requete = {"contents": [{"role": "user", "parts": [{"text": consigne}]}],
           "generationConfig": {"maxOutputTokens": 1024, "thinkingConfig": {"thinkingBudget": 8192}}}
t0 = time.time()
st, rep = appel("POST", f"{BASE}/models/gemini-4-carbon:batchGenerateContent",
                {"batch": {"display_name": "epreuve-carbon-8192", "input_config": {"requests": {"requests": [
                    {"request": requete, "metadata": {"key": "epreuve-1"}}]}}}})
print("création :", st, m(json.dumps(rep, ensure_ascii=False))[:600], flush=True)
if st != 200: sys.exit(2)
nom = rep.get("name"); print("lot :", nom, flush=True)
fin = None
while time.time() - t0 < 1800:
    time.sleep(30)
    st, e = appel("GET", f"{BASE}/{nom}")
    etat = (e.get("metadata") or {}).get("state") or e.get("state") if isinstance(e, dict) else e
    print(f"{round(time.time()-t0)} s : {st} {etat} done={e.get('done') if isinstance(e, dict) else None}", flush=True)
    if isinstance(e, dict) and e.get("done"):
        fin = e; break
if fin is None:
    print("abandon après 30 min : annulation", appel("POST", f"{BASE}/{nom}:cancel")[0]); sys.exit(3)
texte = m(json.dumps(fin, ensure_ascii=False))
open("resultat-lot.json", "w", encoding="utf-8").write(texte)
def cherche(o):
    if isinstance(o, dict):
        if "usageMetadata" in o or "candidates" in o: yield o
        for v in o.values(): yield from cherche(v)
    elif isinstance(o, list):
        for v in o: yield from cherche(v)
for r in cherche(json.loads(texte)):
    c = (r.get("candidates") or [{}])[0]
    print("modèle servi :", r.get("modelVersion"), "| fin :", c.get("finishReason"), "| usage :", r.get("usageMetadata"))
    print("texte :", "".join(p.get("text", "") for p in (c.get("content") or {}).get("parts", []) if not p.get("thought"))[:300])
    break
print("durée totale :", round(time.time() - t0), "s")
