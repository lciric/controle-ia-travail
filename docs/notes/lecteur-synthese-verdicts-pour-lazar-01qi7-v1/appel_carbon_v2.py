"""[v2 : v1 plus le journal et le réessai borné des pannes avant traitement] Appel unique à Carbon (gemini-4-carbon) pour la question v1 du lecteur de synthèse. Sans l'option --envoyer, rien ne
part : seules la garde commune et l'estimation du pire cas sont jouées. Clé lue par son nom (GEMINI_API_KEY, sinon
GEMINI_API_KEY_2 ; jamais _3). Usage : python appel_carbon_v2.py DOSSIER [--envoyer GO-AAAA-MM-JJ-NN]"""
import json, os, sys, time, urllib.request
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "src"))
from controle_ia.garde_google_v3 import verifier_reglages_google, defaut_reponse_google, VERSION_GARDE

S = sys.argv[1]
q = open(f"{S}/question-carbon-v1.md", encoding="utf-8").read()
PROVISION, PLAFOND, MOTS = 49152, 65536, 1200
corps = {"contents": [{"role": "user", "parts": [{"text": q}]}],
         "generationConfig": {"maxOutputTokens": PLAFOND,
                              "thinkingConfig": {"thinkingLevel": "high", "includeThoughts": True}}}
prob = verifier_reglages_google("carbon", corps, provision=PROVISION, mots=MOTS, mode="flux")
if prob:
    print("REFUS AVANT ENVOI", prob); sys.exit(2)
PRIX_ENTREE, PRIX_SORTIE = 8.3e-6, 41.5e-6  # le plus haut des deux tarifs trouvés au dépôt (8,3 / 41,5 USD par million)
pire = PLAFOND * PRIX_SORTIE + (len(q) / 2) * PRIX_ENTREE
print(VERSION_GARDE, "réglages conformes ; pire cas USD", round(pire, 3))
assert pire < 5.0, "pire cas au-delà du plafond de 5 USD"
if len(sys.argv) < 4 or sys.argv[2] != "--envoyer" or not sys.argv[3].startswith("GO-"):
    print("RIEN N'EST PARTI : option --envoyer GO-… absente"); sys.exit(0)
if os.path.exists(f"{S}/reponse-carbon-v1-brute.jsonl"):
    print("REFUS : une réponse existe déjà ; aucune relance après dépense sans décision nommée"); sys.exit(3)
cle = os.environ.get("GEMINI_API_KEY") or os.environ["GEMINI_API_KEY_2"]
url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-4-carbon:streamGenerateContent?alt=sse"
req = urllib.request.Request(url, data=json.dumps(corps).encode(),
                             headers={"Content-Type": "application/json", "x-goog-api-key": cle})
t0, texte, fin, usage, blocage = time.time(), [], None, {}, None
# v2 (erratum du script v1) : une panne avant tout traitement (HTTP 429, 500, 502, 503, 504 : rien n'est facturé, rien
# n'est rendu) est journalisée avec son corps et réessayée au plus quatre fois (attentes 20, 60, 120, 240 s) ; tout autre
# échec arrête. Dès qu'une réponse commence, plus aucun réessai.
import urllib.error
r = None
for n, attente in enumerate((20, 60, 120, 240, None), 1):
    try:
        r = urllib.request.urlopen(req, timeout=1800); break
    except urllib.error.HTTPError as e:
        corps_erreur = e.read()[:800].decode("utf-8", "replace")
        with open(f"{S}/journal-appel-carbon-v1.txt", "a", encoding="utf-8") as j:
            j.write(f"{time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())} essai {n} HTTP {e.code} {corps_erreur!r}\n")
        print("essai", n, "HTTP", e.code, corps_erreur[:300], flush=True)
        if e.code not in (429, 500, 502, 503, 504) or attente is None:
            print("ARRÊT : panne technique avant tout traitement, rien n'est parti en réponse"); sys.exit(8)
        time.sleep(attente)
with r, open(f"{S}/reponse-carbon-v1-brute.jsonl", "w", encoding="utf-8") as brut:
    for ligne in r:
        ligne = ligne.decode("utf-8").strip()
        if not ligne.startswith("data:"):
            continue
        brut.write(ligne[5:].strip() + "\n")
        m = json.loads(ligne[5:])
        usage = m.get("usageMetadata", usage)
        blocage = m.get("promptFeedback", {}).get("blockReason", blocage)
        for c in m.get("candidates", []):
            fin = c.get("finishReason", fin)
            texte += [p.get("text", "") for p in c.get("content", {}).get("parts", []) if not p.get("thought")]
texte = "".join(texte)
d = defaut_reponse_google(fin, texte, usage.get("thoughtsTokenCount"), blocage)
cout = usage.get("promptTokenCount", 0) * PRIX_ENTREE + (usage.get("candidatesTokenCount", 0) + usage.get("thoughtsTokenCount", 0)) * PRIX_SORTIE
print("accord", sys.argv[3], "défaut", d, "fin", fin, "usage", usage, "coût USD (tarif haut)", round(cout, 4), "durée s", round(time.time() - t0))
open(f"{S}/reponse-carbon-v1.md", "w", encoding="utf-8").write(texte)
