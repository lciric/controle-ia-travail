"""Essai réel minuscule de la réflexion des modèles de Google, version 1 (21 novembre 2026, Claude Opus 5.5, opérateur).

Accords : GO-2026-11-21-69 (dépenses sur devis ; plafond 0,50 USD pour l'ensemble) et GO-2026-11-21-71 (vérifier les
réglages). Identifiants et prix : catalogue du collisionneur, docs/notes/collisionneur-v9/collisionneur_v9_v8b.py.
Un envoi generateContent non diffusé par modèle, corps fixé par l'ordre de la mère ; chaque corps passe d'abord par la
garde commune src/controle_ia/garde_google_v2.py (mode « non_diffuse ») et par une garde de motifs ; s'il est refusé,
rien ne part. Clé GEMINI_API_KEY lue par son nom, jamais affichée ni écrite. Seuls les compteurs et le motif de fin sont
gardés ; aucune réponse brute n'est versée. Sortie : JSON des relevés sur la sortie standard.
"""
import json
import os
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "src"))
from controle_ia import garde_google_v2 as garde  # noqa: E402

VERSION = "essai-reel-reflexion-google-v1"
PLAFOND_USD = 0.50
QUESTION = "Combien de nombres premiers y a-t-il entre 100 et 150 ? Donne seulement le nombre."
# Catalogue du collisionneur v9-v8b (identifiant, prix entrée/sortie en USD par million, provision comptée).
ESPECES = {
    "argon": {"id": "gemini-4-argon", "prix": (4.0, 20.0), "niveau": "high", "provision": 16384},
    "carbon": {"id": "gemini-4-carbon", "prix": (4.0, 20.0), "niveau": "high", "provision": 49152},
    "neon": {"id": "gemini-4-neon", "prix": (3.0, 15.0), "niveau": "xhigh", "provision": 32768},
}
MAX_SORTIE = 65536
MOTIFS_INTERDITS = re.compile(r"lazar|ciric|session|controle-ia|github|claude", re.I)
URL = "https://generativelanguage.googleapis.com/v1beta/models/{m}:generateContent"


def corps_pour(niveau):
    return {"contents": [{"role": "user", "parts": [{"text": QUESTION}]}],
            "generationConfig": {"maxOutputTokens": MAX_SORTIE,
                                 "thinkingConfig": {"thinkingLevel": niveau, "includeThoughts": False}}}


def niveau_dessous(espece, niveau):
    niveaux = garde.NIVEAUX_REFLEXION[espece]
    i = niveaux.index(niveau)
    return niveaux[i - 1] if i > 0 else None


def cout_pire(e):
    entree, sortie = ESPECES[e]["prix"]
    return (200 * entree + MAX_SORTIE * sortie) / 1e6


def envoyer(modele, corps, cle):
    requete = urllib.request.Request(URL.format(m=modele), data=json.dumps(corps).encode(),
                                     headers={"Content-Type": "application/json", "x-goog-api-key": cle})
    try:
        with urllib.request.urlopen(requete, timeout=1800) as r:
            return r.status, json.loads(r.read().decode())
    except urllib.error.HTTPError as err:
        try:
            message = json.loads(err.read().decode()).get("error", {}).get("message", "")
        except Exception:
            message = ""
        return err.code, {"_message_erreur": message}


def essai(espece, niveau, cle, depense):
    info = ESPECES[espece]
    corps = corps_pour(niveau)
    rel = {"espece": espece, "modele": info["id"], "niveau": niveau, "maxOutputTokens": MAX_SORTIE,
           "includeThoughts": False}
    problemes = garde.verifier_reglages_google(espece, corps, provision=info["provision"], mode="non_diffuse",
                                               niveau_attendu=niveau)
    if MOTIFS_INTERDITS.search(json.dumps(corps)):
        problemes.append("garde de motifs : nom de personne, de session ou de dépôt dans le corps")
    if problemes:
        rel.update(envoye=False, refus_garde=problemes, verdict="défaut : refusé par la garde, non envoyé")
        return rel, depense
    if depense + cout_pire(espece) > PLAFOND_USD:
        rel.update(envoye=False, verdict="défaut : plafond de dépense au pire cas atteint, non envoyé")
        return rel, depense
    code, rep = envoyer(info["id"], corps, cle)
    rel.update(envoye=True, code_http=code)
    if code != 200:
        rel["niveau_refuse"] = garde.niveau_refuse(f"{code} {rep.get('_message_erreur', '')}")
        rel["verdict"] = f"défaut : code HTTP {code}"
        return rel, depense
    usage = rep.get("usageMetadata", {})
    cand = (rep.get("candidates") or [{}])[0]
    fin = cand.get("finishReason", "absent")
    pensees = usage.get("thoughtsTokenCount", "absent")
    sortie, entree = usage.get("candidatesTokenCount", 0), usage.get("promptTokenCount", 0)
    texte = "".join(p.get("text", "") for p in cand.get("content", {}).get("parts", []) if not p.get("thought"))
    pe, ps = info["prix"]
    cout = (entree * pe + (sortie + (pensees if isinstance(pensees, int) else 0)) * ps) / 1e6
    rel.update(finishReason=fin, thoughtsTokenCount=pensees, candidatesTokenCount=usage.get("candidatesTokenCount", "absent"),
               promptTokenCount=usage.get("promptTokenCount", "absent"), cout_usd=round(cout, 6),
               texte_non_vide=bool(texte.strip()))
    defaut = garde.defaut_reponse_google(fin, texte, pensees if isinstance(pensees, int) else None)
    ok = isinstance(pensees, int) and pensees > 0 and fin == "STOP"
    rel["verdict"] = "réfléchit" if ok else f"défaut : {defaut or 'pensées ou fin hors critère'}"
    return rel, depense + cout


def main():
    releves, depense, cle = [], 0.0, None
    for espece in ESPECES:
        niveau = ESPECES[espece]["niveau"]
        if cle is None and not garde.verifier_reglages_google(espece, corps_pour(niveau), ESPECES[espece]["provision"],
                                                              mode="non_diffuse", niveau_attendu=niveau):
            cle = os.environ.get("GEMINI_API_KEY")
            if not cle:
                print(json.dumps({"erreur": "GEMINI_API_KEY absente"}))
                return 2
        rel, depense = essai(espece, niveau, cle, depense)
        releves.append(rel)
        if rel.get("code_http") == 400 and rel.get("niveau_refuse"):
            dessous = niveau_dessous(espece, niveau)
            if dessous:
                rel2, depense = essai(espece, dessous, cle, depense)
                rel2["repli_declare"] = f"niveau {niveau} refusé (400), une seule reprise au niveau {dessous}"
                releves.append(rel2)
    print(json.dumps({"version": VERSION, "releves": releves, "cout_total_usd": round(depense, 6)},
                     ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main())
