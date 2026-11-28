# Essai minimal des deux points d'appel (AI Studio, Vertex AI express), clé dans l'en-tête, jamais affichée.
import json, os, sys, urllib.request, urllib.error
cle = os.environ.get("GEMINI_API_KEY", "")
if not cle:
    print("aucune clé dans l'environnement"); sys.exit(2)
modeles = sys.argv[1:] or ["gemini-4-argon"]
points = {
    "vertex": "https://aiplatform.googleapis.com/v1/publishers/google/models/{m}:generateContent",
    "studio": "https://generativelanguage.googleapis.com/v1beta/models/{m}:generateContent",
}
corps = json.dumps({"contents": [{"role": "user", "parts": [{"text": "Réponds seulement : OK"}]}],
                    "generationConfig": {"maxOutputTokens": 64}}).encode()
for m in modeles:
    for nom, url in points.items():
        req = urllib.request.Request(url.format(m=m), data=corps, method="POST",
                                     headers={"Content-Type": "application/json", "x-goog-api-key": cle})
        try:
            with urllib.request.urlopen(req, timeout=120) as r:
                d = json.loads(r.read().decode())
            t = "".join(p.get("text", "") for p in d["candidates"][0]["content"]["parts"] if not p.get("thought"))
            print(f"{nom} {m} : OK ({t.strip()[:20]!r})")
        except urllib.error.HTTPError as e:
            msg = e.read().decode(errors="replace").replace(cle, "<clé>")[:300].replace("\n", " ")
            print(f"{nom} {m} : HTTP {e.code} : {msg}")
        except Exception as e:
            print(f"{nom} {m} : {type(e).__name__} : {str(e).replace(cle, '<clé>')[:200]}")
