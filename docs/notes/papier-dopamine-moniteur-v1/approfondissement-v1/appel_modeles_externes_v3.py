"""Version 3 (21 novembre) : ajoute Argon, appelé comme Carbon (même interface, même fonction). Version 2 de l'appel aux modèles externes (GO-2026-11-20-37) : la v1 a été coupée par le relais réseau pendant la réflexion.

Astra : mode d'arrière-plan de l'interface Responses (background), puis relevés toutes les 20 s par requêtes courtes.
Carbon : flux continu (streamGenerateContent, alt=sse), pensées incluses pour garder la connexion vivante ; seules les
parties non « thought » forment la réponse.
Usage : python -I appel_modeles_externes_v2.py {carbon|argon|astra} ENONCE SORTIE_MD SORTIE_JSON
Clés lues par leur nom seulement ; jamais affichées.
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
PRIX = {"carbon": (4.0, 20.0), "astra": (10.0, 50.0), "argon": (10.0, 50.0)}
MODELE = {"carbon": "gemini-4-carbon", "astra": "gpt-6.2-astra", "argon": "gemini-4-argon"}


def requete(url, corps=None, entetes=None, methode="POST", delai=120):
    data = json.dumps(corps).encode("utf-8") if corps is not None else None
    req = urllib.request.Request(url, data=data, headers=entetes or {}, method=methode)
    try:
        with urllib.request.urlopen(req, timeout=delai) as r:
            return r.status, json.loads(r.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        return e.code, {"erreur": e.read().decode("utf-8", "replace")[:2000]}


def appeler_astra(enonce, journal):
    cle = os.environ["OPENAI_API_KEY"]
    ent = {"Content-Type": "application/json", "Authorization": f"Bearer {cle}"}
    for effort in ("xhigh", "high"):
        corps = {"model": MODELE["astra"], "input": enonce, "max_output_tokens": SORTIE_MAX,
                 "reasoning": {"effort": effort}, "background": True, "store": True}
        code, rep = requete("https://api.openai.com/v1/responses", corps, ent)
        journal.append({"reglage": effort, "code": code, "statut": rep.get("status")})
        if code == 400:
            continue
        if code != 200:
            return None, 0, 0, None, None
        rid = rep["id"]
        debut = time.time()
        while rep.get("status") in ("queued", "in_progress") and time.time() - debut < 3600:
            time.sleep(20)
            code, rep = requete(f"https://api.openai.com/v1/responses/{rid}", None, ent, "GET")
            if code != 200:
                journal.append({"releve": code})
                rep = {"status": "in_progress"}
        journal.append({"statut_final": rep.get("status")})
        texte = "".join(c.get("text", "") for o in rep.get("output", []) if o.get("type") == "message"
                        for c in o.get("content", []) if c.get("type") == "output_text")
        u = rep.get("usage") or {}
        return texte or None, u.get("input_tokens", 0), u.get("output_tokens", 0), rep.get("status"), rep.get("model")
    return None, 0, 0, None, None


def appeler_carbon(enonce, journal, espece="carbon"):
    cle = os.environ["GEMINI_API_KEY"]
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{MODELE[espece]}:streamGenerateContent?alt=sse"
    for pensee in ({"thinkingLevel": "high", "includeThoughts": True}, {"thinkingBudget": 32768, "includeThoughts": True}):
        corps = {"contents": [{"role": "user", "parts": [{"text": enonce}]}],
                 "generationConfig": {"maxOutputTokens": SORTIE_MAX, "thinkingConfig": pensee}}
        req = urllib.request.Request(url, data=json.dumps(corps).encode("utf-8"),
                                     headers={"Content-Type": "application/json", "x-goog-api-key": cle}, method="POST")
        try:
            r = urllib.request.urlopen(req, timeout=600)
        except urllib.error.HTTPError as e:
            journal.append({"reglage": pensee, "code": e.code, "erreur": e.read().decode("utf-8", "replace")[:500]})
            if e.code == 400:
                continue
            return None, 0, 0, None, None
        texte, usage, fin, servi, morceaux = [], {}, None, None, 0
        with r:
            for ligne in r:
                ligne = ligne.decode("utf-8").strip()
                if not ligne.startswith("data:"):
                    continue
                morceaux += 1
                d = json.loads(ligne[5:])
                for c in d.get("candidates", []):
                    for p in c.get("content", {}).get("parts", []):
                        if not p.get("thought") and "text" in p:
                            texte.append(p["text"])
                    fin = c.get("finishReason") or fin
                usage = d.get("usageMetadata") or usage
                servi = d.get("modelVersion") or servi
        journal.append({"reglage": pensee, "code": 200, "morceaux": morceaux})
        sortie = usage.get("candidatesTokenCount", 0) + usage.get("thoughtsTokenCount", 0)
        return "".join(texte) or None, usage.get("promptTokenCount", 0), sortie, fin, servi
    return None, 0, 0, None, None


def main(espece, chemin_enonce, sortie_md, sortie_json):
    enonce = open(chemin_enonce, encoding="utf-8").read()
    pe, ps = PRIX[espece]
    pire = (len(enonce) / 2) * pe / 1e6 + SORTIE_MAX * 1.5 * ps / 1e6
    if pire > PLAFOND_APPEL_USD:
        sys.exit(f"ARRET : pire cas {pire:.2f} USD > plafond {PLAFOND_APPEL_USD}")
    journal, t0 = [], time.time()
    texte, entree, sortie, fin, servi = (appeler_astra(enonce, journal) if espece == "astra" else appeler_carbon(enonce, journal, espece))
    meta = {"espece": espece, "modele_demande": MODELE[espece], "modele_servi": servi, "fin": fin,
            "jetons_entree": entree, "jetons_sortie_et_reflexion": sortie,
            "cout_usd_prix_haut": round(entree * pe / 1e6 + sortie * ps / 1e6, 4), "duree_s": round(time.time() - t0, 1),
            "essais": journal, "enonce_sha256": hashlib.sha256(enonce.encode("utf-8")).hexdigest(),
            "heure": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())}
    with open(sortie_json, "x", encoding="utf-8") as f:
        json.dump(meta, f, ensure_ascii=False, indent=1)
    if texte is None:
        sys.exit(f"ECHEC : {journal}")
    with open(sortie_md, "x", encoding="utf-8") as f:
        f.write(texte)
    print(json.dumps({k: meta[k] for k in ("modele_servi", "fin", "jetons_entree", "jetons_sortie_et_reflexion",
                                            "cout_usd_prix_haut", "duree_s")}))


if __name__ == "__main__":
    main(*sys.argv[1:5])
