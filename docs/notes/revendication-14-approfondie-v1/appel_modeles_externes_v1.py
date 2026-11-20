"""Sert l'énoncé neutre de la revendication 14 à un modèle externe, une fois, raisonnement au plus haut (GO-2026-11-20-37).

Usage : python -I appel_modeles_externes_v1.py {carbon|astra} ENONCE SORTIE_MD SORTIE_JSON
Clés lues par leur nom seulement (GEMINI_API_KEY, OPENAI_API_KEY) ; jamais affichées.
Un réglage refusé par l'interface (erreur 400, rien de facturé) fait essayer le réglage suivant, dit au journal.
Coût calculé sur l'usage rendu, au prix haut connu du programme ; arrêt si le pire cas dépasse le plafond.
"""
import hashlib
import json
import os
import sys
import time
import urllib.error
import urllib.request

PLAFOND_APPEL_USD = 4.0
SORTIE_MAX = 32000
PRIX = {"carbon": (4.0, 20.0), "astra": (10.0, 50.0)}  # USD par million de jetons, entrée et sortie (réflexion au prix de sortie)
MODELE = {"carbon": "gemini-4-carbon", "astra": "gpt-6.2-astra"}


def poster(url, corps, entetes):
    req = urllib.request.Request(url, data=json.dumps(corps).encode("utf-8"), headers=entetes, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=1800) as r:
            return r.status, json.loads(r.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        return e.code, {"erreur": e.read().decode("utf-8", "replace")[:2000]}


def appeler_carbon(enonce, journal):
    cle = os.environ["GEMINI_API_KEY"]
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{MODELE['carbon']}:generateContent"
    for pensee in ({"thinkingLevel": "high"}, {"thinkingBudget": 32768}):
        corps = {"contents": [{"role": "user", "parts": [{"text": enonce}]}],
                 "generationConfig": {"maxOutputTokens": SORTIE_MAX, "thinkingConfig": pensee}}
        code, rep = poster(url, corps, {"Content-Type": "application/json", "x-goog-api-key": cle})
        journal.append({"reglage": pensee, "code": code})
        if code == 200:
            texte = "".join(p.get("text", "") for c in rep.get("candidates", []) for p in c.get("content", {}).get("parts", [])
                            if not p.get("thought"))
            u = rep.get("usageMetadata", {})
            entree = u.get("promptTokenCount", 0)
            sortie = u.get("candidatesTokenCount", 0) + u.get("thoughtsTokenCount", 0)
            fin = rep.get("candidates", [{}])[0].get("finishReason")
            return texte, entree, sortie, fin, rep.get("modelVersion")
        if code != 400:
            break
    return None, 0, 0, None, None


def appeler_astra(enonce, journal):
    cle = os.environ["OPENAI_API_KEY"]
    for effort in ("xhigh", "high"):
        corps = {"model": MODELE["astra"], "input": enonce, "max_output_tokens": SORTIE_MAX, "reasoning": {"effort": effort}}
        code, rep = poster("https://api.openai.com/v1/responses", corps,
                           {"Content-Type": "application/json", "Authorization": f"Bearer {cle}"})
        journal.append({"reglage": effort, "code": code})
        if code == 200:
            texte = "".join(c.get("text", "") for o in rep.get("output", []) if o.get("type") == "message"
                            for c in o.get("content", []) if c.get("type") == "output_text")
            u = rep.get("usage", {})
            return texte, u.get("input_tokens", 0), u.get("output_tokens", 0), rep.get("status"), rep.get("model")
        if code != 400:
            break
    return None, 0, 0, None, None


def main(espece, chemin_enonce, sortie_md, sortie_json):
    enonce = open(chemin_enonce, encoding="utf-8").read()
    pe, ps = PRIX[espece]
    pire = (len(enonce) / 2) * pe / 1e6 + SORTIE_MAX * 1.5 * ps / 1e6
    if pire > PLAFOND_APPEL_USD:
        sys.exit(f"ARRET : pire cas {pire:.2f} USD > plafond {PLAFOND_APPEL_USD}")
    journal = []
    t0 = time.time()
    texte, entree, sortie, fin, servi = (appeler_carbon if espece == "carbon" else appeler_astra)(enonce, journal)
    cout = entree * pe / 1e6 + sortie * ps / 1e6
    meta = {"espece": espece, "modele_demande": MODELE[espece], "modele_servi": servi, "fin": fin,
            "jetons_entree": entree, "jetons_sortie_et_reflexion": sortie, "cout_usd_prix_haut": round(cout, 4),
            "duree_s": round(time.time() - t0, 1), "essais": journal,
            "enonce_sha256": hashlib.sha256(enonce.encode("utf-8")).hexdigest(),
            "heure": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())}
    with open(sortie_json, "x", encoding="utf-8") as f:
        json.dump(meta, f, ensure_ascii=False, indent=1)
    if texte is None:
        sys.exit(f"ECHEC : {journal}")
    with open(sortie_md, "x", encoding="utf-8") as f:
        f.write(texte)
    print(json.dumps({k: meta[k] for k in ("modele_servi", "fin", "jetons_entree", "jetons_sortie_et_reflexion", "cout_usd_prix_haut")}))


if __name__ == "__main__":
    main(*sys.argv[1:5])
