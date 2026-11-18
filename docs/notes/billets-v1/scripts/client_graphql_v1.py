"""Client minimal de l'interface de données de LessWrong (requêtes POST).

Une requête par seconde au plus, agent utilisateur générique, aucune information
personnelle. Chaque requête est consignée (texte, variables, date) dans un journal
hors du dépôt, sous /home/user/billets-corpus-v1/journal-requetes.jsonl.
Arrêt au premier refus : toute réponse non 200 ou porteuse d'erreurs lève.
"""
import json
import time
import datetime
import requests

URL = "https://www.lesswrong.com/graphql"
ENTETES = {"User-Agent": "Mozilla/5.0 (compatible; research-client/1.0)",
           "Content-Type": "application/json"}
JOURNAL = "/home/user/billets-corpus-v1/journal-requetes.jsonl"
_dernier = [0.0]


class Refus(RuntimeError):
    pass


def requete(texte, variables=None):
    attente = 1.05 - (time.time() - _dernier[0])
    if attente > 0:
        time.sleep(attente)
    _dernier[0] = time.time()
    r = requests.post(URL, headers=ENTETES,
                      data=json.dumps({"query": texte, "variables": variables or {}}),
                      timeout=60)
    with open(JOURNAL, "a") as f:
        f.write(json.dumps({"date": datetime.datetime.utcnow().isoformat() + "Z",
                            "statut": r.status_code, "requete": texte,
                            "variables": variables or {}}) + "\n")
    if r.status_code != 200:
        raise Refus(f"HTTP {r.status_code} : {r.text[:300]}")
    d = r.json()
    if d.get("errors"):
        raise Refus(f"erreurs : {json.dumps(d['errors'])[:500]}")
    return d["data"]
