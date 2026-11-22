"""v2 : relance unique en FLUX (streamGenerateContent, SSE) après la panne de transport de la v1.
Un appel à Neon (gemini-4-neon) sur le point 2 du bras A (épreuves sans plancher), GO-2026-11-22-100.
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
pb = g.verifier_reglages_google("neon", corps, provision=PROVISION, mots=MOTS, mode="flux")
journal = {"go": "GO-2026-11-22-100", "question": os.path.basename(Q),
           "question_sha256": hashlib.sha256(question.encode()).hexdigest(), "garde": g.VERSION_GARDE,
           "problemes_avant": pb, "debut": datetime.datetime.utcnow().isoformat() + "Z"}
pire = 65536 * 15 / 1e6 + (len(question) / 2.5) * 3 / 1e6
journal["pire_cas_usd"] = round(pire, 4)
def ecrire():
    json.dump(journal, open(os.path.join(ICI, "journal-v2.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
if pb or pire > 1.00:
    journal["statut"] = "refusé avant envoi"; ecrire(); print(journal); sys.exit(2)
json.dump(corps, open(os.path.join(ICI, "corps-envoye-v2.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-4-neon:streamGenerateContent?alt=sse"
req = urllib.request.Request(url, data=json.dumps(corps).encode(), method="POST",
      headers={"Content-Type": "application/json", "x-goog-api-key": os.environ["GEMINI_API_KEY"]})
try:
    morceaux = []
    with urllib.request.urlopen(req, timeout=600) as r:
        for ligne in r:
            ligne = ligne.decode().strip()
            if ligne.startswith("data:"):
                morceaux.append(json.loads(ligne[5:]))
    brut = "\n".join(json.dumps(m, ensure_ascii=False) for m in morceaux)
except urllib.error.HTTPError as e:
    journal["statut"] = f"HTTP {e.code}"; journal["erreur"] = e.read().decode()[:2000]; ecrire(); print(journal); sys.exit(3)
except Exception as e:  # panne de transport : journalisée, jamais une réponse, aucune relance
    journal["statut"] = f"panne de transport : {type(e).__name__} {e}"[:500]; journal["morceaux_recus"] = len(locals().get("morceaux", []))
    ecrire(); print(journal); sys.exit(4)
open(os.path.join(ICI, "reponse-brute-v2.jsonl"), "w", encoding="utf-8").write(brut)
parts, fin, u, rep = [], None, {}, {}
for m in morceaux:
    c = (m.get("candidates") or [{}])[0]
    parts += (c.get("content") or {}).get("parts") or []
    fin = c.get("finishReason") or fin
    u = m.get("usageMetadata") or u
    rep = {**rep, **{k: v for k, v in m.items() if k in ("modelVersion", "promptFeedback")}}
cand = {"finishReason": fin}
texte = "".join(p.get("text", "") for p in parts if not p.get("thought"))
pensees = u.get("thoughtsTokenCount")
defaut = g.defaut_reponse_google(cand.get("finishReason"), texte, pensees, blocage=(rep.get("promptFeedback") or {}).get("blockReason"))
cout = u.get("promptTokenCount", 0) * 3 / 1e6 + (u.get("candidatesTokenCount", 0) + (pensees or 0)) * 15 / 1e6
journal.update({"fin": datetime.datetime.utcnow().isoformat() + "Z", "modele": rep.get("modelVersion"),
                "finishReason": cand.get("finishReason"), "usage": u, "cout_usd": round(cout, 4),
                "defaut": defaut, "statut": "réponse" if defaut is None else "défaut journalisé"})
open(os.path.join(ICI, "reponse-texte-v2.md"), "w", encoding="utf-8").write(texte)
ecrire(); print(json.dumps({k: journal[k] for k in ("statut", "defaut", "cout_usd", "finishReason", "modele")}, ensure_ascii=False))
