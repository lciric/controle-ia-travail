"""Appel unique à Neon ou à Carbon, en flux, sous la garde des appels à Google (garde_google_v3), version 2.

v2 : copie de appel_neon_v1.py ; l'espèce devient un argument (neon : xhigh, provision 32 768 ; carbon : high,
provision 49 152, comme leurs passages précédents au collisionneur) ; limite 3 500 mots ; noms de sortie par espèce.

Usage : python3 -I appel_google_v2.py DEPOT ESPECE QUESTION.md SORTIE_DIR
Réglages : niveau de réflexion xhigh (le plus haut admis), provision 32 768, plafond 65 536, limite 4 500 mots,
comme le passage précédent de Neon au collisionneur. Plafond de dépense déclaré : 2 USD. Une seule tentative ;
toute réponse en défaut est journalisée comme défaut, jamais comme réponse.
"""
import hashlib
import json
import os
import sys
import time
import urllib.request

depot, espece, chemin_q, sortie = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
sys.path.insert(0, os.path.join(depot, "src"))
from controle_ia.garde_google_v3 import (VERSION_GARDE, defaut_reponse_google,  # noqa: E402
                                         verifier_reglages_google)

REGLAGES = {"neon": ("gemini-4-neon", "xhigh", 32768), "carbon": ("gemini-4-carbon", "high", 49152)}
MODELE, NIVEAU, PROVISION = REGLAGES[espece]
PLAFOND, MOTS = 65536, 3500
question = open(chemin_q, encoding="utf-8").read()
corps = {"contents": [{"role": "user", "parts": [{"text": question}]}],
         "generationConfig": {"maxOutputTokens": PLAFOND,
                              "thinkingConfig": {"thinkingLevel": NIVEAU, "includeThoughts": True}}}
os.makedirs(sortie, exist_ok=True)
journal = open(os.path.join(sortie, f"journal-appel-{espece}-v2.txt"), "a", encoding="utf-8")


def j(msg):
    ligne = f"[{time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}] {msg}"
    print(ligne)
    journal.write(ligne + "\n")
    journal.flush()


problemes = verifier_reglages_google(espece, corps, provision=PROVISION, mots=MOTS, mode="flux")
j(f"garde {VERSION_GARDE} avant envoi : {problemes or 'aucun problème'}")
if problemes:
    j("ARRÊT : rien ne part")
    sys.exit(2)
j(f"question sha256 {hashlib.sha256(question.encode('utf-8')).hexdigest()} ; modèle {MODELE} ; niveau {NIVEAU} ; "
  f"provision {PROVISION} ; plafond {PLAFOND} ; limite {MOTS} mots ; envoi flux")
url = f"https://generativelanguage.googleapis.com/v1beta/models/{MODELE}:streamGenerateContent?alt=sse"
req = urllib.request.Request(url, data=json.dumps(corps).encode("utf-8"), method="POST",
                             headers={"Content-Type": "application/json",
                                      "x-goog-api-key": os.environ["GEMINI_API_KEY"]})
texte, pensees_txt, fin, usage, blocage = [], [], None, {}, None
t0 = time.time()
try:
    with urllib.request.urlopen(req, timeout=5400) as r:
        for brut in r:
            ligne = brut.decode("utf-8").strip()
            if not ligne.startswith("data:"):
                continue
            ev = json.loads(ligne[5:].strip())
            if ev.get("promptFeedback", {}).get("blockReason"):
                blocage = ev["promptFeedback"]["blockReason"]
            for c in ev.get("candidates", []):
                for p in c.get("content", {}).get("parts", []):
                    (pensees_txt if p.get("thought") else texte).append(p.get("text", ""))
                fin = c.get("finishReason") or fin
            usage = ev.get("usageMetadata", usage) or usage
except urllib.error.HTTPError as e:
    j(f"ERREUR HTTP {e.code} : {e.read().decode('utf-8', 'replace')[:600]}")
    sys.exit(3)
texte = "".join(texte)
pensees = usage.get("thoughtsTokenCount")
defaut = defaut_reponse_google(fin, texte, pensees, blocage=blocage)
j(f"fin {fin} ; durée {time.time() - t0:.0f} s ; jetons : entrée {usage.get('promptTokenCount')}, "
  f"pensée {pensees}, texte {usage.get('candidatesTokenCount')} ; signes de texte {len(texte)} ; "
  f"marque de fin {'oui' if 'FIN-DE-REPONSE' in texte else 'non'} ; défaut : {defaut or 'aucun'}")
nom = f"reponse-{espece}-modes-exploitables-v2.md" if not defaut else f"defaut-{espece}-modes-exploitables-v2.md"
with open(os.path.join(sortie, nom), "w", encoding="utf-8") as f:
    f.write(texte)
with open(os.path.join(sortie, f"usage-{espece}-v2.json"), "w", encoding="utf-8") as f:
    json.dump({"modele": MODELE, "fin": fin, "usage": usage, "defaut": defaut, "blocage": blocage,
               "garde": VERSION_GARDE}, f, ensure_ascii=False, indent=1)
j(f"écrit : {nom}")
sys.exit(0 if not defaut else 4)
