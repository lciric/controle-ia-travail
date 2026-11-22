"""Un appel à Neon (gemini-4-neon) sur le point 2 du bras A (épreuves sans plancher), GO-2026-11-22-100.
Plafond 1,00 USD : pire cas 3 USD/M en entrée, 15 USD/M en sortie, sortie bornée à 65 536 jetons (≈ 0,99 USD).
Garde des réglages de Google v3 (copie de src/controle_ia/garde_google_v3.py de main) avant et après. Un seul envoi, aucune relance.
Clé lue par son nom (GEMINI_API_KEY). Écrit : corps envoyé, réponse brute, texte, journal."""
import hashlib, json, os, sys, time, urllib.request, datetime
ICI = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, ICI)
import garde_google_v3 as g
Q = sys.argv[1]
question = open(Q, encoding="utf-8").read()
corps = {"contents": [{"role": "user", "parts": [{"text": question}]}],
         "generationConfig": {"maxOutputTokens": 65536,
                              "thinkingConfig": {"thinkingLevel": "xhigh", "includeThoughts": True}}}
PROVISION, MOTS = 32768, 1200
pb = g.verifier_reglages_google("neon", corps, provision=PROVISION, mots=MOTS, mode="non_diffuse")
journal = {"go": "GO-2026-11-22-100", "question": os.path.basename(Q),
           "question_sha256": hashlib.sha256(question.encode()).hexdigest(), "garde": g.VERSION_GARDE,
           "problemes_avant": pb, "debut": datetime.datetime.utcnow().isoformat() + "Z"}
pire = 65536 * 15 / 1e6 + (len(question) / 2.5) * 3 / 1e6
journal["pire_cas_usd"] = round(pire, 4)
def ecrire():
    json.dump(journal, open(os.path.join(ICI, "journal-v1.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
if pb or pire > 1.00:
    journal["statut"] = "refusé avant envoi"; ecrire(); print(journal); sys.exit(2)
json.dump(corps, open(os.path.join(ICI, "corps-envoye-v1.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-4-neon:generateContent"
req = urllib.request.Request(url, data=json.dumps(corps).encode(), method="POST",
      headers={"Content-Type": "application/json", "x-goog-api-key": os.environ["GEMINI_API_KEY"]})
try:
    with urllib.request.urlopen(req, timeout=5400) as r:
        brut = r.read().decode()
except urllib.error.HTTPError as e:
    journal["statut"] = f"HTTP {e.code}"; journal["erreur"] = e.read().decode()[:2000]; ecrire(); print(journal); sys.exit(3)
open(os.path.join(ICI, "reponse-brute-v1.json"), "w", encoding="utf-8").write(brut)
rep = json.loads(brut); cand = (rep.get("candidates") or [{}])[0]
parts = (cand.get("content") or {}).get("parts") or []
texte = "".join(p.get("text", "") for p in parts if not p.get("thought"))
u = rep.get("usageMetadata", {})
pensees = u.get("thoughtsTokenCount")
defaut = g.defaut_reponse_google(cand.get("finishReason"), texte, pensees, blocage=(rep.get("promptFeedback") or {}).get("blockReason"))
cout = u.get("promptTokenCount", 0) * 3 / 1e6 + (u.get("candidatesTokenCount", 0) + (pensees or 0)) * 15 / 1e6
journal.update({"fin": datetime.datetime.utcnow().isoformat() + "Z", "modele": rep.get("modelVersion"),
                "finishReason": cand.get("finishReason"), "usage": u, "cout_usd": round(cout, 4),
                "defaut": defaut, "statut": "réponse" if defaut is None else "défaut journalisé"})
open(os.path.join(ICI, "reponse-texte-v1.md"), "w", encoding="utf-8").write(texte)
ecrire(); print(json.dumps({k: journal[k] for k in ("statut", "defaut", "cout_usd", "finishReason", "modele")}, ensure_ascii=False))
