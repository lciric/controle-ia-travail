import json, os, sys, urllib.request, time
sys.path.insert(0, "/home/user/controle-ia-travail/src")
from controle_ia.garde_google_v3 import verifier_reglages_google, defaut_reponse_google, VERSION_GARDE
S = sys.argv[1]
q = open(f"{S}/question-neon-v1.md", encoding="utf-8").read()
corps = {"contents": [{"role": "user", "parts": [{"text": q}]}],
         "generationConfig": {"maxOutputTokens": 65536,
                              "thinkingConfig": {"thinkingLevel": "xhigh", "includeThoughts": True}}}
prob = verifier_reglages_google("neon", corps, provision=32768, mots=1200, mode="non_diffuse")
if prob:
    print("REFUS AVANT ENVOI", prob); sys.exit(2)
pire = 65536 * 15e-6 + (len(q) / 2) * 3e-6
print("pire cas USD", round(pire, 3)); assert pire < 3.0
cle = os.environ["GEMINI_API_KEY"]
url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-4-neon:generateContent"
req = urllib.request.Request(url, data=json.dumps(corps).encode(), headers={"Content-Type": "application/json", "x-goog-api-key": cle})
t0 = time.time()
with urllib.request.urlopen(req, timeout=900) as r:
    rep = json.load(r)
json.dump(rep, open(f"{S}/reponse-neon-v1.json", "w"), ensure_ascii=False, indent=1)
c = rep["candidates"][0]; u = rep.get("usageMetadata", {})
texte = "".join(p.get("text", "") for p in c["content"]["parts"] if not p.get("thought"))
d = defaut_reponse_google(c.get("finishReason"), texte, u.get("thoughtsTokenCount"), rep.get("promptFeedback", {}).get("blockReason"))
cout = u.get("promptTokenCount", 0) * 3e-6 + (u.get("candidatesTokenCount", 0) + u.get("thoughtsTokenCount", 0)) * 15e-6
print(VERSION_GARDE, "defaut", d, "usage", u, "cout USD", round(cout, 4), "duree", round(time.time() - t0))
open(f"{S}/reponse-neon-v1-texte.md", "w").write(texte)
