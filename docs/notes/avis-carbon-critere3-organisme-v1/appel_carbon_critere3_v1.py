"""Appel unique à Carbon (gemini-4-carbon) pour la question « critère 3 et organisme » (GO-2026-11-24-22, plafond 3 USD).
Repris de appel_carbon_v2.py (branche lecture/synthese-verdicts-pour-lazar-01qi7-v1, f37e4a10…), avec trois changements :
une seule relance, sur refus HTTP 503 avant traitement ; toute coupure pendant la réponse arrête sans relance (faux échec,
flux partiel gardé) ; plafond de 3 USD. Sans l'option --envoyer, rien ne part. Clé lue par son nom (GEMINI_API_KEY, sinon
GEMINI_API_KEY_2 ; jamais _3). Usage : python appel_carbon_critere3_v1.py DOSSIER [--envoyer GO-AAAA-MM-JJ-NN]"""
import json, os, sys, time, urllib.error, urllib.request
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "src"))
from controle_ia.garde_google_v3 import verifier_reglages_google, defaut_reponse_google, VERSION_GARDE

S = sys.argv[1]
NOM = "carbon-critere3-organisme-v1"
q = open(f"{S}/question-{NOM}.md", encoding="utf-8").read()
PROVISION, PLAFOND = 49152, 65536
corps = {"contents": [{"role": "user", "parts": [{"text": q}]}],
         "generationConfig": {"maxOutputTokens": PLAFOND,
                              "thinkingConfig": {"thinkingLevel": "high", "includeThoughts": True}}}
prob = verifier_reglages_google("carbon", corps, provision=PROVISION, mode="flux")
if prob:
    print("REFUS AVANT ENVOI", prob); sys.exit(2)
PRIX_ENTREE, PRIX_SORTIE = 8.3e-6, 41.5e-6  # le plus haut des deux tarifs trouvés au dépôt (8,3 / 41,5 USD par million)
pire = PLAFOND * PRIX_SORTIE + (len(q) / 2) * PRIX_ENTREE
print(VERSION_GARDE, "réglages conformes ; pire cas USD", round(pire, 3))
assert pire < 3.0, "pire cas au-delà du plafond de 3 USD"
if len(sys.argv) < 4 or sys.argv[2] != "--envoyer" or not sys.argv[3].startswith("GO-"):
    print("RIEN N'EST PARTI : option --envoyer GO-… absente"); sys.exit(0)
if os.path.exists(f"{S}/reponse-{NOM}-brute.jsonl"):
    print("REFUS : une réponse ou un flux partiel existe déjà ; aucune relance après dépense"); sys.exit(3)
cle = os.environ.get("GEMINI_API_KEY") or os.environ["GEMINI_API_KEY_2"]
url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-4-carbon:streamGenerateContent?alt=sse"
req = urllib.request.Request(url, data=json.dumps(corps).encode(),
                             headers={"Content-Type": "application/json", "x-goog-api-key": cle})
def journal(ligne):
    with open(f"{S}/journal-appel-{NOM}.txt", "a", encoding="utf-8") as j:
        j.write(f"{time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())} {ligne}\n")
    print(ligne, flush=True)
journal(f"accord {sys.argv[3]} ; {VERSION_GARDE} ; plafond de sortie {PLAFOND}, provision de réflexion {PROVISION}, niveau high")
r = None
for n in (1, 2):
    try:
        r = urllib.request.urlopen(req, timeout=1800); break
    except urllib.error.HTTPError as e:
        corps_erreur = e.read()[:800].decode("utf-8", "replace")
        journal(f"essai {n} HTTP {e.code} {corps_erreur!r}")
        if e.code != 503 or n == 2:
            journal("ARRÊT : panne avant tout traitement, rien n'est parti en réponse (faux échec, jamais parti)"); sys.exit(8)
        time.sleep(30)
t0, texte, fin, usage, blocage = time.time(), [], None, {}, None
try:
    with r, open(f"{S}/reponse-{NOM}-brute.jsonl", "w", encoding="utf-8") as brut:
        for ligne in r:
            ligne = ligne.decode("utf-8").strip()
            if not ligne.startswith("data:"):
                continue
            brut.write(ligne[5:].strip() + "\n"); brut.flush()
            m = json.loads(ligne[5:])
            usage = m.get("usageMetadata", usage)
            blocage = m.get("promptFeedback", {}).get("blockReason", blocage)
            for c in m.get("candidates", []):
                fin = c.get("finishReason", fin)
                texte += [p.get("text", "") for p in c.get("content", {}).get("parts", []) if not p.get("thought")]
except Exception as e:  # coupure pendant la réponse : arrêt, aucune relance
    journal(f"COUPURE après {round(time.time() - t0)} s : {e!r} ; usage partiel {usage} ; faux échec, flux partiel gardé, aucune relance")
    sys.exit(9)
texte = "".join(texte)
d = defaut_reponse_google(fin, texte, usage.get("thoughtsTokenCount"), blocage)
cout = usage.get("promptTokenCount", 0) * PRIX_ENTREE + (usage.get("candidatesTokenCount", 0) + usage.get("thoughtsTokenCount", 0)) * PRIX_SORTIE
journal(f"défaut {d} ; fin {fin} ; usage {usage} ; coût USD (tarif haut) {round(cout, 4)} ; durée s {round(time.time() - t0)}")
open(f"{S}/reponse-{NOM}.md", "w", encoding="utf-8").write(texte)
