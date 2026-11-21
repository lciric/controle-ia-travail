"""Envoi unique de la question servie (famille réservée, dommage mis de côté) à trois modèles externes.

Accord : GO-2026-11-21-68 (consultations, petites, sur les clés existantes). Opérateur d'envoi, rien de conçu ici.
Clés lues par leur nom dans l'environnement, jamais écrites. Une seule fois par modèle ; seule relance permise :
une réponse Gemini qui finit en MAX_TOKENS sans texte (défaut de réglage), une fois.
Usage : python envoi_v1.py carbon|neon|opus46
"""
import datetime
import hashlib
import json
import os
import ssl
import subprocess
import sys
import urllib.error
import urllib.request

ICI = os.path.dirname(os.path.abspath(__file__))
QUESTION = os.path.join(ICI, "question-servie-v1.md")
EMPREINTE_ATTENDUE_FICHIER = QUESTION + ".sha256"
PREAMBULE = "Réponds en français.\n\n"
URL_GEMINI = "https://generativelanguage.googleapis.com/v1beta/models"
URL_ANTHROPIC = "https://api.anthropic.com/v1/messages"
MODELES = {
    # prix en dollars par million de jetons (entrée, sortie, réflexion comprise en sortie)
    "carbon": {"id": "gemini-4-carbon", "fournisseur": "gemini", "cles": ["GEMINI_API_KEY", "GEMINI_API_KEY_2"],
               "max": 65536, "reflexion": 32768, "prix": (4.0, 20.0)},
    "neon": {"id": "gemini-4-neon", "fournisseur": "gemini", "cles": ["GEMINI_API_KEY", "GEMINI_API_KEY_2"],
             "max": 65536, "reflexion": 32768, "prix": (3.0, 15.0)},
    "opus46": {"id": "claude-opus-4-6", "fournisseur": "anthropic",
               "cles": ["RR_ANTHROPIC_API_KEY_LUC", "RR_ANTHROPIC_API_KEY_MINUIT"],
               "max": 32000, "reflexion": "adaptative", "prix": (5.0, 25.0)},
}
MOTIFS_INTERDITS = ["lazar", "session_", "controle-ia", "@"]


def date_u():
    return subprocess.run(["date", "-u"], capture_output=True, text=True, check=True).stdout.strip()


def contexte_tls():
    ca = os.environ.get("SSL_CERT_FILE") or os.environ.get("REQUESTS_CA_BUNDLE")
    return ssl.create_default_context(cafile=ca) if ca else ssl.create_default_context()


def question():
    brut = open(QUESTION, "rb").read()
    attendu = open(EMPREINTE_ATTENDUE_FICHIER).read().split()[0]
    if hashlib.sha256(brut).hexdigest() != attendu:
        sys.exit("empreinte de la question non conforme : arrêt")
    texte = PREAMBULE + brut.decode("utf-8")
    bas = texte.lower()
    sortis = [m for m in MOTIFS_INTERDITS if m in bas]
    if sortis:
        sys.exit(f"garde de motifs : {sortis} : arrêt")
    return texte


def sse(flux):
    for ligne in flux:
        ligne = ligne.decode("utf-8", "replace").strip()
        if ligne.startswith("data:"):
            charge = ligne[5:].strip()
            if charge and charge != "[DONE]":
                yield json.loads(charge)


def gemini(m, prompt, cle):
    corps = {"contents": [{"role": "user", "parts": [{"text": prompt}]}],
             "generationConfig": {"maxOutputTokens": m["max"],
                                  "thinkingConfig": {"thinkingBudget": m["reflexion"], "includeThoughts": True}}}
    req = urllib.request.Request(f"{URL_GEMINI}/{m['id']}:streamGenerateContent?alt=sse",
                                 data=json.dumps(corps, ensure_ascii=False).encode(), method="POST",
                                 headers={"Content-Type": "application/json", "x-goog-api-key": cle})
    texte, fin, usage, servi = [], None, {}, None
    with urllib.request.urlopen(req, timeout=900, context=contexte_tls()) as flux:
        for d in sse(flux):
            if "error" in d:
                raise RuntimeError(json.dumps(d["error"])[:500])
            for c in (d.get("candidates") or [])[:1]:
                for p in (c.get("content") or {}).get("parts") or []:
                    if not p.get("thought"):
                        texte.append(p.get("text", ""))
                fin = c.get("finishReason") or fin
            fin = (d.get("promptFeedback") or {}).get("blockReason") or fin
            usage = d.get("usageMetadata") or usage
            servi = d.get("modelVersion") or servi
    e, s, r = usage.get("promptTokenCount", 0), usage.get("candidatesTokenCount", 0), usage.get("thoughtsTokenCount", 0)
    total = usage.get("totalTokenCount")
    ecart = max((total or 0) - (e + s + r), 0)
    return {"texte": "".join(texte), "fin": fin, "servi": servi, "entree": e, "sortie": s + r + ecart,
            "detail": f"entrée {e}, texte {s}, réflexion {r}, total déclaré {total}"}


def anthropic(m, prompt, cle):
    corps = {"model": m["id"], "max_tokens": m["max"], "stream": True, "thinking": {"type": "adaptive"},
             "messages": [{"role": "user", "content": prompt}]}
    req = urllib.request.Request(URL_ANTHROPIC, data=json.dumps(corps, ensure_ascii=False).encode(), method="POST",
                                 headers={"Content-Type": "application/json", "x-api-key": cle,
                                          "anthropic-version": "2023-06-01"})
    texte, fin, e, s, servi = [], None, 0, 0, None
    with urllib.request.urlopen(req, timeout=900, context=contexte_tls()) as flux:
        for d in sse(flux):
            t = d.get("type")
            if t == "message_start":
                msg = d.get("message") or {}
                servi = msg.get("model")
                e = (msg.get("usage") or {}).get("input_tokens", 0)
            elif t == "content_block_delta" and (d.get("delta") or {}).get("type") == "text_delta":
                texte.append(d["delta"].get("text", ""))
            elif t == "message_delta":
                fin = (d.get("delta") or {}).get("stop_reason") or fin
                s = (d.get("usage") or {}).get("output_tokens", s)
            elif t == "error":
                raise RuntimeError(json.dumps(d.get("error"))[:500])
    return {"texte": "".join(texte), "fin": fin, "servi": servi, "entree": e, "sortie": s,
            "detail": f"entrée {e}, sortie {s} (réflexion comprise)"}


def envoyer(nom):
    m = MODELES[nom]
    prompt = question()
    appel = gemini if m["fournisseur"] == "gemini" else anthropic
    journal = []
    for i, nom_cle in enumerate(m["cles"]):
        cle = os.environ.get(nom_cle)
        if not cle:
            journal.append(f"{nom_cle} absente")
            continue
        try:
            rep = appel(m, prompt, cle)
        except urllib.error.HTTPError as err:
            corps = err.read().decode("utf-8", "replace").replace(cle, "***")[:800]
            journal.append(f"{nom_cle} : HTTP {err.code} : {corps}")
            # repli sur la seconde clé seulement si la première est refusée avant tout service (crédit, quota, clé)
            if err.code in (400, 401, 402, 403, 429) and i + 1 < len(m["cles"]) and \
                    any(k in corps.lower() for k in ("credit", "quota", "billing", "api key", "permission", "exhaust")):
                continue
            return ecrire(nom, m, None, journal)
        relance = None
        if m["fournisseur"] == "gemini" and rep["fin"] == "MAX_TOKENS" and not rep["texte"].strip():
            journal.append(f"première réponse MAX_TOKENS sans texte ({rep['detail']}) : relance unique")
            relance = rep
            rep = appel(m, prompt, cle)
        rep["cle"] = nom_cle
        rep["relance"] = relance
        return ecrire(nom, m, rep, journal)
    return ecrire(nom, m, None, journal)


def ecrire(nom, m, rep, journal):
    chemin = os.path.join(ICI, f"reponse-{nom}-v1.md")
    if os.path.exists(chemin):
        sys.exit(f"{chemin} existe déjà : on n'écrase jamais")
    pe, ps = m["prix"]
    lignes = [f"# Réponse brute — {m['id']}", "", f"- Modèle demandé : {m['id']}", f"- Heure (date -u) : {date_u()}",
              f"- Réglages : plafond de sortie {m['max']}, réflexion {m['reflexion']}",
              "- Question : question-servie-v1.md, précédée de « Réponds en français. »"]
    if rep is None:
        lignes += ["- Statut : échec, aucune réponse", "- Journal :"] + [f"  - {j}" for j in journal]
    else:
        cout = rep["entree"] * pe / 1e6 + rep["sortie"] * ps / 1e6
        if rep.get("relance"):
            r0 = rep["relance"]
            cout += r0["entree"] * pe / 1e6 + r0["sortie"] * ps / 1e6
        lignes += [f"- Modèle servi : {rep['servi']}", f"- Clé (nom) : {rep['cle']}",
                   f"- Jetons facturés : {rep['detail']}",
                   f"- Coût estimé : {cout:.4f} dollars (tarif {pe} / {ps} dollars par million, relance comprise)",
                   f"- Motif d'arrêt : {rep['fin']}", "- Journal :"] + [f"  - {j}" for j in journal or ["envoi unique"]]
        lignes += ["", "---", "", rep["texte"]]
    with open(chemin, "w", encoding="utf-8") as f:
        f.write("\n".join(lignes) + "\n")
    print(chemin, "|", "échec" if rep is None else f"{rep['fin']} | {len(rep['texte'])} car.")


if __name__ == "__main__":
    envoyer(sys.argv[1])
