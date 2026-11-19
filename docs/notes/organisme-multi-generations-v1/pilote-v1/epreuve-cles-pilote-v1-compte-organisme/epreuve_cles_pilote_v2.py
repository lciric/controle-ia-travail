"""Épreuve des trois clés du pilote MR-2, juste avant toute location — v2 (R12 ; la v1 reste en place).

Un appel minimal par clé (« Réponds par le seul mot OK. », 16 jetons de sortie au plus), aux fournisseurs et aux modèles de la
configuration v12 : `opus55` pour la clé de Claude (la même clé sert à `fable52`), `argon`, `astra`. Rien d'autre : ni monde, ni texte
servi, ni consigne du pilote. Clés lues par leur nom (`variable_cle` de la configuration), sous `env -i` (aucune
`ANTHROPIC_BASE_URL`). Un seul envoi par clé : aucune reprise, aucune redirection suivie.

Portée (dite) : l'épreuve prouve, par clé, que la clé est acceptée et qu'un modèle de la configuration est servi selon la règle du
pilote. Elle ne prouve pas l'accès au modèle de `fable52` (même clé, autre modèle), ni le réglage `output_config` que le pilote
envoie aux deux proposeurs de Claude, ni un quota suffisant pour un appel du pilote, ni le chemin de réseau de la machine louée.

Sortie (fichier réservé **avant** tout appel, écrit d'abord « appels en cours », puis complet) : par clé, le nom de la variable, le
code HTTP, l'identifiant **servi** (jamais une clé ni un corps ; ce fichier reste hors de `main`, R-2731), « modèle servi conforme »
selon la règle du pilote, les jetons, le coût (pire cas de la clé si un appel est parti sans usage lu). Écran : quatre champs.

Codes : 0 les trois clés passent et la dépense tient sous la ligne ; 4 une clé au moins ne passe pas ; 5 la dépense lue dépasse la
ligne ; 2 refus avant tout appel (sortie existante, montant illisible, pire cas au-dessus de la ligne, clé absente, adresse d'essai
non locale) ; 1 erreur non rattrapée.

Usage : python3 -I -B epreuve_cles_pilote_v2.py CONFIGURATION MONTANT_USD SORTIE.json [--amont-essai http://127.0.0.1:PORT]
(`--amont-essai` : doublure locale des essais seulement.)
"""
import datetime
import json
import math
import os
import re
import ssl
import sys
import urllib.error
import urllib.request

VERSION = "epreuve-cles-pilote-v2"
CONSIGNE = "Réponds par le seul mot OK."
BORNE = 16
DELAI_S = 60
CLES = ("opus55", "argon", "astra")  # une par clé : RR_ANTHROPIC_API_KEY_RIGAUD, GEMINI_API_KEY, OPENAI_API_KEY
SUFFIXE = re.compile(r"-(?:(\d{4})(\d{2})(\d{2})|(\d{4})-(\d{2})-(\d{2}))")


def refus(texte):
    print("REFUS : " + texte, file=sys.stderr)
    sys.exit(2)


def conforme(demande, servi):
    """Règle du pilote (`commande_pilote_v70.py`) : identifiant exact, ou suivi d'un suffixe de date réelle (2000 à 2099)."""
    if not isinstance(servi, str):
        return False
    if servi == demande:
        return True
    m = SUFFIXE.fullmatch(servi[len(demande):]) if servi.startswith(demande) else None
    if m is None:
        return False
    a, mo, j = [int(x) for x in m.groups() if x is not None]
    try:
        datetime.date(a, mo, j)
    except ValueError:
        return False
    return 2000 <= a <= 2099


class SansRedirection(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, *a, **k):  # un 3xx devient un statut rendu, aucune seconde requête
        return None


def corps_et_entetes(dialecte, modele, cle):
    e = {"Content-Type": "application/json"}
    if dialecte == "claude":
        c = {"model": modele, "max_tokens": BORNE, "messages": [{"role": "user", "content": CONSIGNE}]}
        e.update({"x-api-key": cle, "anthropic-version": "2023-06-01"})
    elif dialecte == "gemini":
        c = {"contents": [{"role": "user", "parts": [{"text": CONSIGNE}]}], "generationConfig": {"maxOutputTokens": BORNE}}
        e["x-goog-api-key"] = cle
    else:
        c = {"model": modele, "messages": [{"role": "user", "content": CONSIGNE}], "max_completion_tokens": BORNE}
        e["Authorization"] = "Bearer " + cle
    return json.dumps(c).encode("utf-8"), e


def lire_usage(dialecte, r):
    if dialecte == "claude":
        u = r.get("usage") or {}
        return r.get("model"), u.get("input_tokens"), u.get("output_tokens")
    if dialecte == "gemini":
        u = r.get("usageMetadata") or {}
        c, t = u.get("candidatesTokenCount"), u.get("thoughtsTokenCount")
        sortie = None if c is None and t is None else (c or 0) + (t or 0)
        return r.get("modelVersion"), u.get("promptTokenCount"), sortie
    u = r.get("usage") or {}
    return r.get("model"), u.get("prompt_tokens"), u.get("completion_tokens")


def main():
    a = sys.argv[1:]
    essai = None
    if "--amont-essai" in a:
        i = a.index("--amont-essai"); essai = a[i + 1]; del a[i:i + 2]
        if not re.fullmatch(r"http://127\.0\.0\.1:\d{1,5}", essai):
            refus("--amont-essai n'admet que la boucle locale")
    if len(a) != 3:
        refus("arguments : CONFIGURATION MONTANT_USD SORTIE.json")
    conf_chemin, montant_txt, sortie = a
    try:
        montant = float(montant_txt)
    except ValueError:
        refus("montant illisible")
    if not (math.isfinite(montant) and montant > 0):
        refus("montant illisible")
    conf = json.load(open(conf_chemin, encoding="utf-8"))
    octets = len(CONSIGNE.encode("utf-8"))
    pire = {n: ((octets + 1024) * conf["proposeurs"][n]["prix_entree_usd_par_million"]
                + BORNE * conf["proposeurs"][n]["prix_sortie_usd_par_million"]) / 1e6 for n in CLES}
    if sum(pire.values()) > montant:
        refus(f"pire cas {sum(pire.values()):.6f} > ligne {montant}")
    for n in CLES:  # toutes les clés présentes avant tout appel
        if not os.environ.get(conf["proposeurs"][n]["variable_cle"]):
            refus(f"clé {conf['proposeurs'][n]['variable_cle']} absente (nom seul)")
    try:
        f = open(sortie, "x", encoding="utf-8")  # réservée avant tout appel : une seconde exécution est refusée
    except FileExistsError:
        refus("sortie existante")
    except OSError as e:
        refus(f"sortie non inscriptible ({type(e).__name__})")
    res = {"version": VERSION, "etat": "appels en cours", "consigne_octets": octets, "borne": BORNE, "delai_s": DELAI_S,
           "pire_cas_usd": round(sum(pire.values()), 6), "montant_ligne_usd": montant, "essai_local": essai is not None, "cles": {}}
    f.write(json.dumps(res, ensure_ascii=False, sort_keys=True)); f.flush(); os.fsync(f.fileno())
    ca = os.environ.get("SSL_CERT_FILE")
    ctx = ssl.create_default_context(cafile=ca) if ca else ssl.create_default_context()
    ouvreur = urllib.request.build_opener(SansRedirection, urllib.request.HTTPSHandler(context=ctx))
    for n in CLES:
        p = conf["proposeurs"][n]
        url = p["url_amont"] if essai is None else essai + "/" + p["dialecte"]
        corps, ent = corps_et_entetes(p["dialecte"], p["modele"], os.environ[p["variable_cle"]])
        ligne = {"variable": p["variable_cle"], "statut": None, "modele_servi": None, "modele_servi_conforme": False,
                 "entree": None, "sortie": None, "cout_usd": None, "cout_origine": None}
        parti = False
        servi = ei = so = None
        cle = os.environ[p["variable_cle"]]
        if not re.fullmatch(r"[\x21-\x7e]+", cle):  # clé illisible (espace, saut de ligne, non latin) : rien n'est envoyé
            ligne["statut"] = "erreur:cle_illisible"
        else:
            try:
                req = urllib.request.Request(url, data=corps, headers=ent, method="POST")
                parti = True
                with ouvreur.open(req, timeout=DELAI_S) as rep:
                    ligne["statut"] = rep.status
                    servi, ei, so = lire_usage(p["dialecte"], json.loads(rep.read().decode("utf-8")))
            except urllib.error.HTTPError as e:
                ligne["statut"] = e.code  # le corps n'est pas lu ; refusé par le fournisseur : rien de facturé à compter ici
                parti = False
            except Exception as e:  # noqa: BLE001 — réseau, délai, corps illisible : compté au pire cas
                ligne["statut"] = "erreur:" + type(e).__name__
        if isinstance(servi, str):
            ligne["modele_servi"] = servi
        ligne["modele_servi_conforme"] = conforme(p["modele"], servi)
        if isinstance(ei, int) and isinstance(so, int):
            ligne.update(entree=ei, sortie=so, cout_origine="usage",
                         cout_usd=round((ei * p["prix_entree_usd_par_million"] + so * p["prix_sortie_usd_par_million"]) / 1e6, 8))
        elif parti:
            ligne.update(cout_usd=round(pire[n], 8), cout_origine="pire_cas")
        res["cles"][p["variable_cle"]] = ligne
    res["toutes_valides"] = all(l["statut"] == 200 and l["modele_servi_conforme"] and l["cout_origine"] == "usage"
                                for l in res["cles"].values())
    res["depense_usd"] = round(sum(l["cout_usd"] or 0 for l in res["cles"].values()), 8)
    res["depassement"] = res["depense_usd"] > montant
    res["etat"] = "fini"
    f.seek(0); f.truncate()
    json.dump(res, f, ensure_ascii=False, indent=1, sort_keys=True); f.close()
    print(json.dumps({k: res[k] for k in ("toutes_valides", "depense_usd", "pire_cas_usd", "depassement")}, ensure_ascii=False))
    sys.exit(5 if res["depassement"] else 0 if res["toutes_valides"] else 4)


if __name__ == "__main__":
    main()
