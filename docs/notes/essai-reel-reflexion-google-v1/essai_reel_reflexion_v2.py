"""Essai réel minuscule de la réflexion des modèles de Google, version 2 (21 novembre 2026, Claude Opus 5.5, opérateur).

v2 : copie de essai_reel_reflexion_v1.py (inchangée, R12), après les deux refus de la garde relevés par la v1, tranchés
par la mère : (1) includeThoughts vrai ; on ne verse que les compteurs, jamais le texte des pensées ni la réponse ;
(2) envoi en flux (streamGenerateContent, alt=sse), comme le collisionneur, maxOutputTokens 65 536 pour les trois
modèles, garde en mode « flux ». Réglage inchangé : thinkingLevel « high » (Argon, Carbon), « xhigh » (Neon), aucun
thinkingBudget. Un seul envoi par modèle ; sur un 400 qui nomme le niveau, une seule reprise déclarée au niveau
documenté juste en dessous.
Ajout de l'opérateur (déclaré, jamais silencieux) : le pire cas d'un envoi à 65 536 jetons de sortie (1,31 USD pour
Argon et Carbon, 0,98 pour Neon) dépasse à lui seul le plafond de 0,50 USD de GO-2026-11-21-69 ; le flux est donc lu
avec une coupure de dépense : chaque modèle reçoit une part (reste du plafond × 0,9 / modèles restants) ; si le coût
estimé en cours de flux (compteurs cumulés de usageMetadata, sinon caractères reçus / 3) l'atteint, la connexion est
fermée et la coupure est relevée (la facturation de ce qui suit la coupure n'est pas connue).
Accords : GO-2026-11-21-69 (dépenses sur devis ; plafond 0,50 USD pour l'ensemble) et GO-2026-11-21-71 (vérifier les
réglages). Identifiants et prix : catalogue du collisionneur, docs/notes/collisionneur-v9/collisionneur_v9_v8b.py.
Clé GEMINI_API_KEY lue par son nom, jamais affichée ni écrite. Sortie : JSON des relevés (compteurs seulement).
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

VERSION = "essai-reel-reflexion-google-v2"
PLAFOND_USD = 0.50
MARGE = 0.9
QUESTION = "Combien de nombres premiers y a-t-il entre 100 et 150 ? Donne seulement le nombre."
ESPECES = {
    "argon": {"id": "gemini-4-argon", "prix": (4.0, 20.0), "niveau": "high", "provision": 16384},
    "carbon": {"id": "gemini-4-carbon", "prix": (4.0, 20.0), "niveau": "high", "provision": 49152},
    "neon": {"id": "gemini-4-neon", "prix": (3.0, 15.0), "niveau": "xhigh", "provision": 32768},
}
MAX_SORTIE = 65536
MODE = "flux"
MOTIFS_INTERDITS = re.compile(r"lazar|ciric|session|controle-ia|github|claude", re.I)
URL = "https://generativelanguage.googleapis.com/v1beta/models/{m}:streamGenerateContent?alt=sse"
DELAI_S = 900


def corps_pour(niveau):
    return {"contents": [{"role": "user", "parts": [{"text": QUESTION}]}],
            "generationConfig": {"maxOutputTokens": MAX_SORTIE,
                                 "thinkingConfig": {"thinkingLevel": niveau, "includeThoughts": True}}}


def niveau_dessous(espece, niveau):
    niveaux = garde.NIVEAUX_REFLEXION[espece]
    i = niveaux.index(niveau)
    return niveaux[i - 1] if i > 0 else None


def masquer(texte, cle):
    texte = str(texte)
    return texte.replace(cle, "<clé masquée>") if cle else texte


def cout(info, entree, sortie, pensees):
    pe, ps = info["prix"]
    return (entree * pe + (sortie + pensees) * ps) / 1e6


def envoyer_flux(info, corps, cle, part_usd):
    """Envoie en flux ; agrège le dernier morceau. Ne garde que des compteurs (caractères reçus, pas le texte)."""
    requete = urllib.request.Request(URL.format(m=info["id"]), data=json.dumps(corps).encode(), method="POST",
                                     headers={"Content-Type": "application/json", "x-goog-api-key": cle})
    agr = {"finishReason": None, "usage": {}, "blockReason": None, "car_pensee": 0, "car_texte": 0, "coupe": None,
           "morceaux": 0, "erreur_flux": None}
    try:
        flux = urllib.request.urlopen(requete, timeout=DELAI_S)
    except urllib.error.HTTPError as err:
        try:
            message = json.loads(err.read().decode()).get("error", {}).get("message", "")
        except Exception:
            message = ""
        return err.code, {"_message_erreur": masquer(message, cle)[:400]}
    except OSError as e:
        return None, {"_message_erreur": f"échec sans réponse : {type(e).__name__} : {masquer(e, cle)[:300]}"}
    with flux:
        try:
            for brute in flux:
                ligne = brute.decode("utf-8", "replace").strip()
                if not ligne.startswith("data:"):
                    continue
                charge = ligne[5:].strip()
                if not charge or charge == "[DONE]":
                    continue
                d = json.loads(charge)
                agr["morceaux"] += 1
                if "error" in d:
                    agr["erreur_flux"] = masquer(json.dumps(d["error"]), cle)[:300]
                    break
                agr["blockReason"] = (d.get("promptFeedback") or {}).get("blockReason") or agr["blockReason"]
                for c in (d.get("candidates") or [])[:1]:
                    for p in (c.get("content") or {}).get("parts") or []:
                        cle_car = "car_pensee" if p.get("thought") else "car_texte"
                        agr[cle_car] += len(p.get("text", ""))
                    agr["finishReason"] = c.get("finishReason") or agr["finishReason"]
                agr["usage"] = d.get("usageMetadata") or agr["usage"]
                u = agr["usage"]
                sortie_cumul = (u.get("candidatesTokenCount") or 0) + (u.get("thoughtsTokenCount") or 0)
                estime_car = (agr["car_pensee"] + agr["car_texte"]) / 3
                estime = cout(info, u.get("promptTokenCount") or 0, max(sortie_cumul, estime_car), 0)
                if estime >= part_usd and not agr["finishReason"]:
                    agr["coupe"] = f"coupure de dépense : coût estimé {estime:.4f} USD ≥ part {part_usd:.4f} USD"
                    break
        except (OSError, ValueError) as e:
            agr["erreur_flux"] = f"flux coupé : {type(e).__name__} : {masquer(e, cle)[:300]}"
    return 200, agr


def essai(espece, niveau, cle, depense, restants):
    info = ESPECES[espece]
    corps = corps_pour(niveau)
    rel = {"espece": espece, "modele": info["id"], "niveau": niveau, "maxOutputTokens": MAX_SORTIE,
           "includeThoughts": True, "mode": MODE}
    problemes = garde.verifier_reglages_google(espece, corps, provision=info["provision"], mode=MODE,
                                               niveau_attendu=niveau)
    if MOTIFS_INTERDITS.search(json.dumps(corps)):
        problemes.append("garde de motifs : nom de personne, de session ou de dépôt dans le corps")
    if problemes:
        rel.update(envoye=False, refus_garde=problemes, verdict="défaut : refusé par la garde, non envoyé")
        return rel, depense
    part = (PLAFOND_USD * MARGE - depense) / max(restants, 1)
    rel["part_usd"] = round(part, 4)
    if part <= 0.01:
        rel.update(envoye=False, verdict="défaut : plafond de dépense épuisé, non envoyé")
        return rel, depense
    code, rep = envoyer_flux(info, corps, cle, part)
    rel.update(envoye=True, code_http=code if code is not None else "aucun")
    if code != 200:
        rel["message_erreur"] = rep.get("_message_erreur", "")
        rel["niveau_refuse"] = code == 400 and garde.niveau_refuse(f"{code} {rep.get('_message_erreur', '')}")
        rel["verdict"] = f"défaut : code HTTP {code}"
        return rel, depense
    u = rep["usage"]
    fin = rep["finishReason"] or "absent"
    pensees = u.get("thoughtsTokenCount", "absent")
    p_int = pensees if isinstance(pensees, int) else 0
    sortie, entree = u.get("candidatesTokenCount", 0) or 0, u.get("promptTokenCount", 0) or 0
    c = cout(info, entree, sortie, p_int)
    if rep["coupe"]:  # facturation après coupure inconnue : on compte au moins la part
        c = max(c, part)
    rel.update(finishReason=fin, thoughtsTokenCount=pensees,
               candidatesTokenCount=u.get("candidatesTokenCount", "absent"),
               promptTokenCount=u.get("promptTokenCount", "absent"), cout_usd=round(c, 6),
               morceaux=rep["morceaux"], caracteres_pensee=rep["car_pensee"], caracteres_texte=rep["car_texte"],
               texte_non_vide=rep["car_texte"] > 0, blockReason=rep["blockReason"], coupure=rep["coupe"],
               erreur_flux=rep["erreur_flux"])
    defaut = garde.defaut_reponse_google(fin, "x" if rep["car_texte"] > 0 else "",
                                         pensees if isinstance(pensees, int) else None, blocage=rep["blockReason"])
    ok = isinstance(pensees, int) and pensees > 0 and fin == "STOP" and not rep["coupe"] and not rep["erreur_flux"]
    rel["verdict"] = "réfléchit" if ok else f"défaut : {defaut or rep['coupe'] or rep['erreur_flux'] or 'hors critère'}"
    return rel, depense + c


def main():
    releves, depense = [], 0.0
    cle = os.environ.get("GEMINI_API_KEY")
    if not cle:
        print(json.dumps({"erreur": "GEMINI_API_KEY absente"}))
        return 2
    especes = list(ESPECES)
    for i, espece in enumerate(especes):
        niveau = ESPECES[espece]["niveau"]
        rel, depense = essai(espece, niveau, cle, depense, len(especes) - i)
        releves.append(rel)
        if rel.get("code_http") == 400 and rel.get("niveau_refuse"):
            dessous = niveau_dessous(espece, niveau)
            if dessous:
                rel2, depense = essai(espece, dessous, cle, depense, len(especes) - i)
                rel2["repli_declare"] = f"niveau {niveau} refusé (400), une seule reprise au niveau {dessous}"
                releves.append(rel2)
    print(json.dumps({"version": VERSION, "releves": releves, "cout_total_usd": round(depense, 6)},
                     ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main())
