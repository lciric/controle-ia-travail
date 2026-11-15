"""Épreuve des trois clés du pilote MR-2, juste avant le lancement unique — v1 (option (b) de Lazar).

Un appel minimal par clé (« Réponds par le seul mot OK. », 16 jetons de sortie au plus), aux fournisseurs et aux modèles de la
configuration v12 : `opus55` pour la clé de Claude (la même clé sert à `fable52`), `argon`, `astra`. Rien d'autre : ni monde, ni texte
servi, ni consigne du pilote. Imprime seulement, par clé : code HTTP, modèle servi conforme (vrai ou faux, jamais l'identifiant),
jetons d'entrée et de sortie, coût aux prix de la configuration ; jamais une clé, jamais le corps. Refuse avant tout appel si le pire
cas dépasse le montant de la ligne. Clés lues par leur nom (`variable_cle` de la configuration), sous `env -i` (aucune
`ANTHROPIC_BASE_URL`). Aucune reprise.

Usage : python3 -I -B epreuve_cles_pilote_v1.py CONFIGURATION MONTANT_USD SORTIE.json [--amont-essai http://127.0.0.1:PORT]
(`--amont-essai` : doublure locale des essais seulement ; refuse toute autre adresse que la boucle locale.)
"""
import json
import os
import ssl
import sys
import urllib.request

CONSIGNE = "Réponds par le seul mot OK."
BORNE = 16
CLES = ("opus55", "argon", "astra")  # une par clé : RR_ANTHROPIC_API_KEY_RIGAUD, GEMINI_API_KEY, OPENAI_API_KEY


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
        sortie = (u.get("candidatesTokenCount") or 0) + (u.get("thoughtsTokenCount") or 0)
        return r.get("modelVersion"), u.get("promptTokenCount"), sortie
    u = r.get("usage") or {}
    return r.get("model"), u.get("prompt_tokens"), u.get("completion_tokens")


def main():
    a = sys.argv[1:]
    essai = None
    if "--amont-essai" in a:
        i = a.index("--amont-essai"); essai = a[i + 1]; del a[i:i + 2]
        if not essai.startswith("http://127.0.0.1:"):
            sys.exit("REFUS : --amont-essai n'admet que la boucle locale")
    conf_chemin, montant, sortie = a[0], float(a[1]), a[2]
    if os.path.exists(sortie):
        sys.exit("REFUS : sortie existante")
    conf = json.load(open(conf_chemin, encoding="utf-8"))
    octets = len(CONSIGNE.encode("utf-8"))
    pire = {n: ((octets + 1024) * conf["proposeurs"][n]["prix_entree_usd_par_million"]
                + BORNE * conf["proposeurs"][n]["prix_sortie_usd_par_million"]) / 1e6 for n in CLES}
    if sum(pire.values()) > montant:
        sys.exit(f"REFUS : pire cas {sum(pire.values()):.6f} > ligne {montant}")
    for n in CLES:  # toutes les clés présentes avant tout appel
        if not os.environ.get(conf["proposeurs"][n]["variable_cle"]):
            sys.exit(f"REFUS : clé {conf['proposeurs'][n]['variable_cle']} absente (nom seul)")
    ca = os.environ.get("SSL_CERT_FILE")
    ctx = ssl.create_default_context(cafile=ca) if ca else ssl.create_default_context()
    res = {"version": "epreuve-cles-pilote-v1", "consigne_octets": octets, "borne": BORNE, "pire_cas_usd": round(sum(pire.values()), 6),
           "montant_ligne_usd": montant, "essai_local": essai is not None, "cles": {}}
    for n in CLES:
        p = conf["proposeurs"][n]
        url = p["url_amont"] if essai is None else essai + "/" + p["dialecte"]
        corps, ent = corps_et_entetes(p["dialecte"], p["modele"], os.environ[p["variable_cle"]])
        ligne = {"variable": p["variable_cle"], "statut": None, "modele_servi_conforme": None, "entree": None, "sortie": None, "cout_usd": None}
        try:
            with urllib.request.urlopen(urllib.request.Request(url, data=corps, headers=ent, method="POST"), timeout=120,
                                        context=None if essai else ctx) as rep:
                ligne["statut"] = rep.status
                servi, ei, so = lire_usage(p["dialecte"], json.loads(rep.read().decode("utf-8")))
        except urllib.error.HTTPError as e:
            ligne["statut"] = e.code
            servi = ei = so = None
        except Exception as e:  # noqa: BLE001 — réseau : dit, sans corps
            ligne["statut"] = "erreur:" + type(e).__name__
            servi = ei = so = None
        if servi is not None:
            ligne["modele_servi_conforme"] = str(servi).startswith(p["modele"])
        if isinstance(ei, int) and isinstance(so, int):
            ligne.update(entree=ei, sortie=so,
                         cout_usd=round((ei * p["prix_entree_usd_par_million"] + so * p["prix_sortie_usd_par_million"]) / 1e6, 8))
        res["cles"][p["variable_cle"]] = ligne
    res["toutes_valides"] = all(l["statut"] == 200 and l["modele_servi_conforme"] for l in res["cles"].values())
    res["depense_usd"] = round(sum(l["cout_usd"] or 0 for l in res["cles"].values()), 8)
    with open(sortie, "x", encoding="utf-8") as f:
        json.dump(res, f, ensure_ascii=False, indent=1, sort_keys=True)
    print(json.dumps({k: res[k] for k in ("toutes_valides", "depense_usd", "pire_cas_usd")}, ensure_ascii=False))
    sys.exit(0 if res["toutes_valides"] else 4)


if __name__ == "__main__":
    main()
