"""Appel d'une question à Argon ou Carbon (Google), sous la garde commune garde_google_v3, version 1 (22 novembre 2026).

Écrit par Claude Opus 5.5 pour la demande 33. Pourquoi un appel neuf : appel_modeles_externes_v6.py n'appelle pas la garde
et envoie un thinkingBudget, que la garde v3 refuse (déprécié chez Gemini 4). La lecture du flux reprend celle du v6.
Avant l'envoi : verifier_reglages_google (niveau le plus haut admis, includeThoughts, plafond ≥ provision + 16 000, limite
de mots) ; un problème = rien ne part. Après : defaut_reponse_google ; un défaut n'est jamais une réponse (écrit en
.defaut.md à part). Clé GEMINI_API_KEY lue par son nom ; jamais affichée ni écrite. Pièce d'instrument (classe B).
Usage : python -I appel_google_garde_v3_v1.py {argon|carbon} ENONCE SORTIE_MD SORTIE_JSON --mots N
"""
import argparse
import hashlib
import json
import os
import sys
import time
import urllib.error
import urllib.request

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "src"))
from controle_ia import garde_google_v3 as garde  # noqa: E402

MODELE = {"argon": "gemini-4-argon", "carbon": "gemini-4-carbon"}
PRIX = {"argon": (10.0, 50.0), "carbon": (4.0, 20.0)}  # USD par million, entrée / sortie, repris du v6 (prix haut)
URL = "https://generativelanguage.googleapis.com/v1beta/models/{}:streamGenerateContent?alt=sse"
PLAFOND = 65536          # limite en flux de la garde v3 (Argon et Carbon)
PROVISION = 49152        # réflexion comptée ; texte réservé : 16 384 ≥ 16 000
PLAFOND_USD = 4.0


def main(argv=None):
    p = argparse.ArgumentParser()
    p.add_argument("espece", choices=sorted(MODELE))
    p.add_argument("enonce")
    p.add_argument("sortie_md")
    p.add_argument("sortie_json")
    p.add_argument("--mots", type=int, required=True)
    a = p.parse_args(argv)
    for c in (a.sortie_md, a.sortie_json, a.sortie_md + ".defaut.md"):
        if os.path.exists(c):
            print(f"ARRET : {c} existe déjà (R12)", file=sys.stderr)
            return 1
    enonce = open(a.enonce, encoding="utf-8").read()
    niveau = garde.NIVEAU_MAX_REFLEXION[a.espece]
    corps = {"contents": [{"role": "user", "parts": [{"text": enonce}]}],
             "generationConfig": {"maxOutputTokens": PLAFOND,
                                  "thinkingConfig": {"thinkingLevel": niveau, "includeThoughts": True}}}
    problemes = garde.verifier_reglages_google(a.espece, corps, provision=PROVISION, mots=a.mots, mode="flux")
    if problemes:
        print("ARRET (garde) : " + " ; ".join(problemes), file=sys.stderr)
        return 1
    pe, ps = PRIX[a.espece]
    pire = len(enonce) / 2 * pe / 1e6 + PLAFOND * ps / 1e6
    if pire > PLAFOND_USD:
        print(f"ARRET : pire cas {pire:.4f} USD > {PLAFOND_USD}", file=sys.stderr)
        return 1
    cle = os.environ.get("GEMINI_API_KEY")
    if not cle:
        print("ARRET : variable GEMINI_API_KEY absente", file=sys.stderr)
        return 1
    t0 = time.time()
    req = urllib.request.Request(URL.format(MODELE[a.espece]), data=json.dumps(corps).encode("utf-8"), method="POST",
                                 headers={"Content-Type": "application/json", "x-goog-api-key": cle})
    texte, usage, fin, retour, message_fin, erreur, servi, rid, code = [], {}, None, None, None, None, None, None, None
    try:
        with urllib.request.urlopen(req, timeout=900) as r:
            code = r.status
            for ligne in r:
                ligne = ligne.decode("utf-8", "replace").strip()
                if not ligne.startswith("data:"):
                    continue
                try:
                    d = json.loads(ligne[5:])
                except json.JSONDecodeError:
                    continue
                erreur = d.get("error") or erreur
                for c in d.get("candidates", []) or []:
                    for part in (c.get("content") or {}).get("parts", []) or []:
                        if not part.get("thought") and "text" in part:
                            texte.append(part["text"])
                    fin = c.get("finishReason") or fin
                    message_fin = c.get("finishMessage") or message_fin
                retour = d.get("promptFeedback") or retour
                usage = d.get("usageMetadata") or usage
                servi = d.get("modelVersion") or servi
                rid = d.get("responseId") or rid
    except urllib.error.HTTPError as e:
        code, erreur = e.code, e.read().decode("utf-8", "replace").replace(cle, "[clé masquée]")
    except (urllib.error.URLError, TimeoutError, OSError) as e:
        erreur = f"{type(e).__name__}: {e}"
    texte = "".join(texte)
    pensees = usage.get("thoughtsTokenCount")
    jetons_texte = usage.get("candidatesTokenCount", 0) or 0
    entree = usage.get("promptTokenCount", 0) or 0
    defaut = (f"HTTP_{code}" if code != 200 else None) or garde.defaut_reponse_google(
        fin, texte, pensees, blocage=(retour or {}).get("blockReason"))
    cout = entree * pe / 1e6 + (jetons_texte + (pensees or 0)) * ps / 1e6
    meta = {"script": "appel_google_garde_v3_v1.py", "garde": garde.VERSION_GARDE, "espece": a.espece,
            "modele_demande": MODELE[a.espece], "modele_servi": servi, "id_reponse": rid, "code_http": code,
            "raison_arret": fin, "defaut": defaut, "verdict": "reponse" if defaut is None else "defaut",
            "reglage": corps["generationConfig"], "provision_reflexion": PROVISION, "mots_demandes": a.mots,
            "jetons_entree": entree, "jetons_reflexion": pensees, "jetons_texte": jetons_texte,
            "prix_usd_par_million": {"entree": pe, "sortie": ps}, "cout_estime_usd": round(cout, 4),
            "pire_cas_usd": round(pire, 4), "erreur_fournisseur": erreur,
            "details": {"promptFeedback": retour, "finishMessage": message_fin}, "duree_s": round(time.time() - t0, 1),
            "enonce_sha256": hashlib.sha256(enonce.encode("utf-8")).hexdigest(),
            "heure": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), "variable_cle": "GEMINI_API_KEY"}
    if texte:
        with open(a.sortie_md if defaut is None else a.sortie_md + ".defaut.md", "x", encoding="utf-8") as f:
            f.write(texte.replace(cle, "[clé masquée]"))
    with open(a.sortie_json, "x", encoding="utf-8") as f:
        json.dump(meta, f, ensure_ascii=False, indent=1)
    print(json.dumps({k: meta[k] for k in ("verdict", "defaut", "raison_arret", "modele_servi", "jetons_entree",
                                            "jetons_reflexion", "jetons_texte", "cout_estime_usd", "duree_s")},
                     ensure_ascii=False))
    return 0 if defaut is None else 3


if __name__ == "__main__":
    sys.exit(main())
