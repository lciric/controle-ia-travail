"""Version 6 (21 novembre) de l'appel aux modèles externes : nom de la clé d'OpenAI restreint à OPENAI_API_KEY….
Remplace le v5 (4c44b89e…, gardé sans modification, R12). Un seul changement, décidé par la mère après la contre-lecture
contre-lecture-collisionneur-v9-v5-v1.md (77041a13…, remarque 1) : --cle-openai n'accepte qu'un nom qui commence par
OPENAI_API_KEY (par exemple OPENAI_API_KEY_2) ; tout autre nom (GEMINI_API_KEY, par exemple) est refusé sans être répété,
pour qu'une clé ne parte jamais vers un autre fournisseur que le sien. Essais : essais_appel_modeles_externes_v6.py.

Ce qui suit est l'en-tête du v5, inchangé.
Version 5 (21 novembre, GO-2026-11-21-57) de l'appel aux modèles externes : Neon, et clé d'OpenAI nommée.
Remplace le v4 (b31fecf2…, gardé sans modification, R12). Changements, et seulement ceux-là :
- espèce Neon (gemini-4-neon, flux continu Gemini, clé GEMINI_API_KEY par son nom) : prix 3 / 15 USD par million (palier
  « Standard » de la page publique de Google lue le 21 novembre 2026 à 13:49Z, versée :
  docs/sources/prix/page-prix-gemini-api-20261121T134918Z.html, 40202cdd…) ; identifiant vérifié par la liste des modèles de
  l'interface (docs/notes/collisionneur-v9/liste-modeles-gemini-20261121T134904Z.json, eeec19e8… : outputTokenLimit 65 536,
  thinking vrai) ; défaut 32 768 de réflexion + 32 768 de texte = 65 536, le plafond synchrone documenté ;
- règle du plafond large de Carbon (CLAUDE.md, GO-2026-11-21-47) appliquée à Neon, qui réfléchit : réflexion bornée par
  `thinkingBudget` et au moins 16 000 jetons de texte au-delà (refus en dessous), comme Carbon et Argon dans le v4 ; un arrêt
  en « MAX_TOKENS » sans texte chez Carbon ou Neon est dit « défaut de réglage, pas une réponse » (code 3 inchangé) ;
- option --cle-openai NOM (défaut OPENAI_API_KEY) : nom de la variable qui porte la clé d'OpenAI (Astra) ; nom mal formé
  refusé sans être répété ; la valeur n'est jamais affichée ni écrite ; le NOM de la variable lue est écrit dans le JSON.
Essais hors réseau : essais_appel_modeles_externes_v5.py (les dix essais du v4, rejoués tels quels, et ceux du v5).

Ce qui suit est l'en-tête du v4, inchangé.
Version 4 (21 novembre) de l'appel aux modèles externes. Remplace le v3 (8aee878d…, gardé sans modification, R12).

Pourquoi : le v3 a perdu deux échecs d'Astra (« failed » sans motif : il ne gardait ni l'identifiant de la réponse ni son
objet d'erreur) et un échec de Carbon (« MAX_TOKENS » : la réflexion « high », non bornée, a mangé les 32 000 jetons de
sortie avant tout texte).

Ce que fait le v4 :
- garde l'identifiant de la réponse (Astra : `id` ; Carbon : `responseId`) et le message d'erreur complet du fournisseur
  (corps HTTP entier, objet `error`, `incomplete_details`, `promptFeedback`, `finishMessage`), clés masquées ;
- plafond de sortie = provision de réflexion + texte, réglables. Carbon : réflexion bornée par `thinkingBudget`
  (défaut 24 000) et 16 000 jetons de texte au moins au-delà (refus en dessous) ; Astra : l'interface ne borne la réflexion
  que par l'effort et le plafond commun, défaut 32 000 + 16 000 ;
- garde de dépense : pire cas (entrée estimée à 1 jeton pour 2 signes, sortie au plafond × 1,5) contre le plafond par appel
  (défaut 4 USD, jamais au-dessus) ;
- aucun renvoi silencieux : tout échec est écrit dans le JSON et rend un code non nul (1 échec ou refus, 3 réponse
  tronquée ou incomplète — texte partiel écrit à part, en `.partiel.md`, jamais sous le nom de la réponse) ;
- essais hors réseau : `essais_appel_modeles_externes_v4.py` (transport simulé).
Usage (v6) : python -I appel_modeles_externes_v6.py {argon|astra|carbon|neon} ENONCE SORTIE_MD SORTIE_JSON
        [--reflexion N] [--texte N] [--efforts xhigh,high] [--plafond-usd X] [--cle-openai NOM]
Clés lues par leur nom seulement (celle d'OpenAI dans la variable nommée par --cle-openai, défaut OPENAI_API_KEY ;
GEMINI_API_KEY) ; jamais affichées ni écrites.
"""
import argparse
import hashlib
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request

PLAFOND_APPEL_USD = 4.0
PRIX = {"carbon": (4.0, 20.0), "astra": (10.0, 50.0), "argon": (10.0, 50.0), "neon": (3.0, 15.0)}  # v5 : Neon
MODELE = {"carbon": "gemini-4-carbon", "astra": "gpt-6.2-astra", "argon": "gemini-4-argon", "neon": "gemini-4-neon"}
CLE = {"carbon": "GEMINI_API_KEY", "argon": "GEMINI_API_KEY", "astra": "OPENAI_API_KEY", "neon": "GEMINI_API_KEY"}
DEFAUTS = {"carbon": (24000, 16000), "argon": (24000, 16000), "astra": (32000, 16000),
           "neon": (32768, 32768)}  # (réflexion, texte) ; v5 : Neon, 65 536 au total, plafond synchrone documenté
TEXTE_MIN_GEMINI = 16000
ESPECES_GEMINI = ("carbon", "argon", "neon")  # v5 : espèces servies par le flux Gemini, sous le plancher de texte
REGLE_PLAFOND_LARGE = ("carbon", "neon")  # v5 : règle de CLAUDE.md (GO-2026-11-21-47), étendue à Neon (GO-2026-11-21-57)
MOTIF_NOM_VARIABLE = re.compile(r"^[A-Z_][A-Z0-9_]{0,99}$")  # v5 : --cle-openai, comme le collisionneur
PREFIXE_CLE_OPENAI = "OPENAI_API_KEY"  # v6 : tout nom donné à --cle-openai commence par ce préfixe
URL_OPENAI = "https://api.openai.com/v1/responses"
URL_GEMINI = "https://generativelanguage.googleapis.com/v1beta/models/{}:streamGenerateContent?alt=sse"
RELEVE_S = 20
DELAI_MAX_S = 3600
RELEVES_RATES_MAX = 5

CODE_OK, CODE_ECHEC, CODE_TRONQUE = 0, 1, 3


class Masque:
    """Remplace toute occurrence des clés (valeurs lues par nom) dans un texte ou un objet avant écriture."""

    def __init__(self, valeurs):
        self.valeurs = [v for v in valeurs if v and len(v) >= 8]

    def __call__(self, x):
        if isinstance(x, str):
            for v in self.valeurs:
                x = x.replace(v, "[clé masquée]")
            return x
        if isinstance(x, dict):
            return {k: self(v) for k, v in x.items()}
        if isinstance(x, list):
            return [self(v) for v in x]
        return x


# --- transport réel (remplacé par un simulé dans les essais) -----------------------------------------------------------
def http_json(url, corps, entetes, methode="POST", delai=120):
    """Rend (code, objet JSON ou None, corps brut complet)."""
    data = json.dumps(corps).encode("utf-8") if corps is not None else None
    req = urllib.request.Request(url, data=data, headers=entetes, method=methode)
    try:
        with urllib.request.urlopen(req, timeout=delai) as r:
            brut = r.read().decode("utf-8", "replace")
            code = r.status
    except urllib.error.HTTPError as e:
        brut, code = e.read().decode("utf-8", "replace"), e.code
    except (urllib.error.URLError, TimeoutError, OSError) as e:
        return None, None, f"{type(e).__name__}: {e}"
    try:
        return code, json.loads(brut), brut
    except json.JSONDecodeError:
        return code, None, brut


def http_flux(url, corps, entetes, delai=600):
    """Rend (code, itérateur de lignes décodées ou None, corps d'erreur complet ou None)."""
    req = urllib.request.Request(url, data=json.dumps(corps).encode("utf-8"), headers=entetes, method="POST")
    try:
        r = urllib.request.urlopen(req, timeout=delai)
    except urllib.error.HTTPError as e:
        return e.code, None, e.read().decode("utf-8", "replace")
    except (urllib.error.URLError, TimeoutError, OSError) as e:
        return None, None, f"{type(e).__name__}: {e}"

    def lignes():
        with r:
            for ligne in r:
                yield ligne.decode("utf-8", "replace")
    return r.status, lignes(), None


def attendre(s):
    time.sleep(s)


# --- Astra (interface Responses, arrière-plan) ---------------------------------------------------------------------------
def appeler_astra(enonce, cle, reglage, journal, transport=http_json, dormir=attendre):
    ent = {"Content-Type": "application/json", "Authorization": f"Bearer {cle}"}
    res = {"texte": None, "statut": None, "id_reponse": None, "modele_servi": None, "erreur_fournisseur": None,
           "details_incomplet": None, "jetons_entree": 0, "jetons_sortie": 0, "jetons_reflexion": 0, "effort": None}
    for effort in reglage["efforts"]:
        corps = {"model": MODELE["astra"], "input": enonce, "max_output_tokens": reglage["plafond_sortie"],
                 "reasoning": {"effort": effort}, "background": True, "store": True}
        code, rep, brut = transport(URL_OPENAI, corps, ent, "POST")
        rep = rep or {}
        journal.append({"etape": "creation", "effort": effort, "code_http": code, "statut": rep.get("status"),
                        "id_reponse": rep.get("id"), **({} if code == 200 else {"corps_erreur": brut})})
        res["effort"] = effort
        if code == 400:  # réglage refusé : essai suivant, consigné ci-dessus avec le corps complet
            res["statut"], res["erreur_fournisseur"] = "refus_requete_400", rep.get("error") or brut
            continue
        if code != 200:
            res["statut"], res["erreur_fournisseur"] = f"http_{code}", rep.get("error") or brut
            return res
        rid = rep.get("id")
        res["id_reponse"] = rid
        debut, rates = time.monotonic(), 0
        while rep.get("status") in ("queued", "in_progress"):
            if time.monotonic() - debut > DELAI_MAX_S:
                res["statut"] = "delai_depasse"
                journal.append({"etape": "abandon", "motif": f"plus de {DELAI_MAX_S} s", "id_reponse": rid})
                return res
            dormir(RELEVE_S)
            code, nouveau, brut = transport(f"{URL_OPENAI}/{rid}", None, ent, "GET")
            if code != 200 or nouveau is None:
                rates += 1
                journal.append({"etape": "releve_rate", "code_http": code, "corps_erreur": brut})
                if rates >= RELEVES_RATES_MAX:
                    res["statut"] = "releves_rates"
                    res["erreur_fournisseur"] = brut
                    return res
                continue
            rates, rep = 0, nouveau
        res["statut"] = rep.get("status")
        res["modele_servi"] = rep.get("model")
        res["erreur_fournisseur"] = rep.get("error")
        res["details_incomplet"] = rep.get("incomplete_details")
        u = rep.get("usage") or {}
        res["jetons_entree"] = u.get("input_tokens", 0) or 0
        res["jetons_sortie"] = u.get("output_tokens", 0) or 0
        res["jetons_reflexion"] = (u.get("output_tokens_details") or {}).get("reasoning_tokens", 0) or 0
        journal.append({"etape": "fin", "statut": res["statut"], "id_reponse": rid, "erreur": res["erreur_fournisseur"],
                        "details_incomplet": res["details_incomplet"]})
        texte = "".join(c.get("text", "") for o in rep.get("output", []) or [] if o.get("type") == "message"
                        for c in o.get("content", []) or [] if c.get("type") == "output_text")
        res["texte"] = texte or None
        return res
    return res


# --- Carbon et Argon (flux continu Gemini) -------------------------------------------------------------------------------
def appeler_gemini(enonce, cle, reglage, journal, espece="carbon", transport=http_flux):
    res = {"texte": None, "statut": None, "id_reponse": None, "modele_servi": None, "erreur_fournisseur": None,
           "details_incomplet": None, "jetons_entree": 0, "jetons_sortie": 0, "jetons_reflexion": 0,
           "budget_reflexion": reglage["reflexion"]}
    pensee = {"thinkingBudget": reglage["reflexion"], "includeThoughts": True}
    corps = {"contents": [{"role": "user", "parts": [{"text": enonce}]}],
             "generationConfig": {"maxOutputTokens": reglage["plafond_sortie"], "thinkingConfig": pensee}}
    code, lignes, brut = transport(URL_GEMINI.format(MODELE[espece]), corps,
                                   {"Content-Type": "application/json", "x-goog-api-key": cle})
    if code != 200 or lignes is None:
        try:
            obj = json.loads(brut)
        except (TypeError, json.JSONDecodeError):
            obj = None
        res["statut"] = f"http_{code}"
        res["erreur_fournisseur"] = (obj or {}).get("error") if isinstance(obj, dict) else None
        res["erreur_fournisseur"] = res["erreur_fournisseur"] or brut
        journal.append({"etape": "creation", "reglage": pensee, "code_http": code, "corps_erreur": brut})
        return res
    texte, usage, fin, morceaux, retour, message_fin = [], {}, None, 0, None, None
    for ligne in lignes:
        ligne = ligne.strip()
        if not ligne.startswith("data:"):
            continue
        morceaux += 1
        try:
            d = json.loads(ligne[5:])
        except json.JSONDecodeError:
            journal.append({"etape": "morceau_illisible", "contenu": ligne[:2000]})
            continue
        if "error" in d:  # erreur au milieu du flux
            res["erreur_fournisseur"] = d["error"]
        for c in d.get("candidates", []) or []:
            for p in (c.get("content") or {}).get("parts", []) or []:
                if not p.get("thought") and "text" in p:
                    texte.append(p["text"])
            fin = c.get("finishReason") or fin
            message_fin = c.get("finishMessage") or message_fin
        if d.get("promptFeedback"):
            retour = d["promptFeedback"]
        usage = d.get("usageMetadata") or usage
        res["modele_servi"] = d.get("modelVersion") or res["modele_servi"]
        res["id_reponse"] = d.get("responseId") or res["id_reponse"]
    res["statut"] = fin or ("erreur_dans_le_flux" if res["erreur_fournisseur"] else "flux_sans_fin")
    if retour or message_fin:
        res["details_incomplet"] = {"promptFeedback": retour, "finishMessage": message_fin}
    res["jetons_entree"] = usage.get("promptTokenCount", 0) or 0
    res["jetons_reflexion"] = usage.get("thoughtsTokenCount", 0) or 0
    res["jetons_sortie"] = (usage.get("candidatesTokenCount", 0) or 0) + res["jetons_reflexion"]
    res["texte"] = "".join(texte) or None
    journal.append({"etape": "fin", "reglage": pensee, "code_http": 200, "morceaux": morceaux, "statut": res["statut"],
                    "id_reponse": res["id_reponse"]})
    return res


# --- verdict, garde de dépense, écriture ---------------------------------------------------------------------------------
def verdict(espece, res):
    """Rend (code de sortie, motif). Seul un texte complet et une fin normale donnent 0."""
    statut = res["statut"]
    if espece == "astra":
        if statut == "completed" and res["texte"]:
            return CODE_OK, "complet"
        if statut == "incomplete":
            return CODE_TRONQUE, f"incomplet : {res['details_incomplet']}"
        return CODE_ECHEC, f"statut {statut} ; erreur du fournisseur : {res['erreur_fournisseur']}"
    if statut == "STOP" and res["texte"] and not res["erreur_fournisseur"]:
        return CODE_OK, "complet"
    if statut == "MAX_TOKENS":
        reglage = (" ; défaut de réglage, pas une réponse (règle du plafond large)"
                   if espece in REGLE_PLAFOND_LARGE and not res["texte"] else "")  # v5
        return CODE_TRONQUE, (f"MAX_TOKENS : plafond de sortie atteint ({res['jetons_reflexion']} jetons de réflexion, "
                              f"texte {'partiel' if res['texte'] else 'absent'}){reglage}")
    return CODE_ECHEC, (f"statut {statut} ; erreur du fournisseur : {res['erreur_fournisseur']} ; "
                        f"détails : {res['details_incomplet']}")


def reglage_depuis(espece, reflexion, texte, efforts):
    r0, t0 = DEFAUTS[espece]
    reflexion = r0 if reflexion is None else reflexion
    texte = t0 if texte is None else texte
    if espece in ESPECES_GEMINI and texte < TEXTE_MIN_GEMINI:  # v5 : Neon compris
        raise ValueError(f"texte {texte} < {TEXTE_MIN_GEMINI} jetons au-delà de la réflexion : refusé pour {espece}")
    if reflexion < 0 or texte <= 0:
        raise ValueError("réflexion et texte doivent être positifs")
    return {"reflexion": reflexion, "texte": texte, "plafond_sortie": reflexion + texte,
            "efforts": tuple(efforts or ("xhigh", "high"))}


def pire_cas_usd(espece, enonce, plafond_sortie):
    pe, ps = PRIX[espece]
    return (len(enonce) / 2) * pe / 1e6 + plafond_sortie * 1.5 * ps / 1e6


def executer(espece, chemin_enonce, sortie_md, sortie_json, reflexion=None, texte=None, efforts=None,
             plafond_usd=PLAFOND_APPEL_USD, environ=None, transport_json=http_json, transport_flux=http_flux,
             dormir=attendre, nom_cle_openai=CLE["astra"]):
    environ = os.environ if environ is None else environ
    if plafond_usd > PLAFOND_APPEL_USD:
        print(f"ARRET : plafond demandé {plafond_usd} > {PLAFOND_APPEL_USD} USD", file=sys.stderr)
        return CODE_ECHEC
    if not isinstance(nom_cle_openai, str) or not MOTIF_NOM_VARIABLE.match(nom_cle_openai):  # v5 : nom jamais répété
        print("ARRET : --cle-openai : nom de variable d'environnement mal formé (lettres majuscules, chiffres, « _ »)",
              file=sys.stderr)
        return CODE_ECHEC
    if not nom_cle_openai.startswith(PREFIXE_CLE_OPENAI):  # v6 : une clé ne part jamais vers un autre fournisseur
        print(f"ARRET : --cle-openai : le nom doit commencer par {PREFIXE_CLE_OPENAI}", file=sys.stderr)
        return CODE_ECHEC
    for chemin in (sortie_md, sortie_json, sortie_md + ".partiel.md"):
        if os.path.exists(chemin):
            print(f"ARRET : {chemin} existe déjà (on n'écrase jamais, R12)", file=sys.stderr)
            return CODE_ECHEC
    try:
        reglage = reglage_depuis(espece, reflexion, texte, efforts)
    except ValueError as e:
        print(f"ARRET : {e}", file=sys.stderr)
        return CODE_ECHEC
    enonce = open(chemin_enonce, encoding="utf-8").read()
    pire = pire_cas_usd(espece, enonce, reglage["plafond_sortie"])
    if pire > plafond_usd:
        print(f"ARRET : pire cas {pire:.4f} USD > plafond {plafond_usd} USD", file=sys.stderr)
        return CODE_ECHEC
    nom_cle = nom_cle_openai if espece == "astra" else CLE[espece]  # v5 : --cle-openai
    cle = environ.get(nom_cle)
    if not cle:
        print(f"ARRET : variable {nom_cle} absente", file=sys.stderr)
        return CODE_ECHEC
    masque = Masque([cle])
    journal, t0 = [], time.time()
    if espece == "astra":
        res = appeler_astra(enonce, cle, reglage, journal, transport_json, dormir)
    else:
        res = appeler_gemini(enonce, cle, reglage, journal, espece, transport_flux)
    code, motif = verdict(espece, res)
    pe, ps = PRIX[espece]
    meta = {"version_script": "v6", "espece": espece, "modele_demande": MODELE[espece], "variable_cle": nom_cle,
            "modele_servi": res["modele_servi"], "id_reponse": res["id_reponse"], "fin": res["statut"],
            "verdict": "ok" if code == CODE_OK else ("tronque" if code == CODE_TRONQUE else "echec"),
            "motif": motif, "erreur_fournisseur": res["erreur_fournisseur"],
            "details_incomplet": res["details_incomplet"], "effort": res.get("effort"),
            "provision_reflexion": reglage["reflexion"], "texte_reserve": reglage["texte"],
            "plafond_sortie": reglage["plafond_sortie"], "plafond_usd": plafond_usd, "pire_cas_usd": round(pire, 4),
            "jetons_entree": res["jetons_entree"], "jetons_sortie_et_reflexion": res["jetons_sortie"],
            "jetons_reflexion": res["jetons_reflexion"],
            "cout_usd_prix_haut": round(res["jetons_entree"] * pe / 1e6 + res["jetons_sortie"] * ps / 1e6, 4),
            "duree_s": round(time.time() - t0, 1), "essais": journal,
            "enonce_sha256": hashlib.sha256(enonce.encode("utf-8")).hexdigest(),
            "heure": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            "sortie_texte": None}
    if res["texte"]:
        cible = sortie_md if code == CODE_OK else sortie_md + ".partiel.md"
        with open(cible, "x", encoding="utf-8") as f:
            f.write(masque(res["texte"]))
        meta["sortie_texte"] = os.path.basename(cible)
    with open(sortie_json, "x", encoding="utf-8") as f:
        json.dump(masque(meta), f, ensure_ascii=False, indent=1)
    resume = {k: meta[k] for k in ("verdict", "fin", "id_reponse", "modele_servi", "jetons_entree",
                                    "jetons_sortie_et_reflexion", "jetons_reflexion", "cout_usd_prix_haut", "duree_s")}
    print(json.dumps(masque(resume), ensure_ascii=False))
    if code != CODE_OK:
        print(masque(f"{'TRONQUE' if code == CODE_TRONQUE else 'ECHEC'} : {motif}"), file=sys.stderr)
    return code


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("espece", choices=sorted(MODELE))
    p.add_argument("enonce")
    p.add_argument("sortie_md")
    p.add_argument("sortie_json")
    p.add_argument("--reflexion", type=int, default=None, help="provision de réflexion en jetons")
    p.add_argument("--texte", type=int, default=None, help="jetons de texte au-delà de la réflexion")
    p.add_argument("--efforts", default=None, help="Astra : efforts essayés dans l'ordre sur refus 400, ex. xhigh,high")
    p.add_argument("--plafond-usd", type=float, default=PLAFOND_APPEL_USD)
    p.add_argument("--cle-openai", default=CLE["astra"],  # v5
                   help="NOM de la variable d'environnement qui porte la clé d'OpenAI (défaut OPENAI_API_KEY ; v6 : "
                        "commence par OPENAI_API_KEY)")
    a = p.parse_args(argv)
    efforts = tuple(x.strip() for x in a.efforts.split(",") if x.strip()) if a.efforts else None
    return executer(a.espece, a.enonce, a.sortie_md, a.sortie_json, a.reflexion, a.texte, efforts, a.plafond_usd,
                    nom_cle_openai=a.cle_openai)


if __name__ == "__main__":
    sys.exit(main())
