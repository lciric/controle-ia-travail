"""Garde de départ « prêt / manque » par clé et par modèle — v2.

v2 : pour Google, aucun appel qui génère (consigne de la mère, GO-2026-11-22-54) : l'essai est
`countTokens`, gratuit ; il prouve l'accès au modèle, pas le crédit (« prêt, accès seul »).

Avant toute course et toute passe : un essai par couple (clé, modèle), au plus bas
coût (sortie d'un jeton par défaut), qui vérifie l'accès et le crédit. Rend « prêt »
ou « manque » par couple, avec une raison en liste fermée. Tout ce qui n'est pas
reconnu comme un succès complet est « manque » : aucun repli silencieux (R5).

Règles :
- la clé est lue par le nom de sa variable d'environnement, jamais affichée ni écrite ;
- aucun texte d'erreur du fournisseur n'est gardé (il peut contenir un fragment de clé) :
  seuls le code HTTP, le type ou code d'erreur et la raison classée sont journalisés ;
- l'invite servie est fixe et neutre (« ok ») : aucun nom, identifiant ni courriel ;
- l'hôte est fixé par fournisseur, jamais lu du plan ;
- un envoi réel exige --reel et --go GO-AAAA-MM-JJ-NN présent dans le registre des GO
  donné ; sans cela, rien ne part ;
- chaque appel a un pire calculé (entrée bornée + sortie maximale, au tarif du plan) ;
  au-delà du plafond par appel, le couple est « manque (plafond) » sans envoi.
"""
from __future__ import annotations

import argparse
import datetime as _dt
import json
import os
import re
import sys
import urllib.error
import urllib.request

INVITE = "ok"
ENTREE_MAX_JETONS = 32  # borne prudente de l'entrée servie, pour le pire
PLAFOND_APPEL_USD = 0.02
SORTIE_MAX_PERMISE = 64

HOTES = {
    "anthropic": "https://api.anthropic.com/v1/messages",
    "openai": "https://api.openai.com/v1/chat/completions",
    "kimi": "https://api.moonshot.ai/v1/chat/completions",
    "google": "https://generativelanguage.googleapis.com/v1beta/models/{modele}:countTokens",
}

RAISONS = (
    "prêt", "prêt, accès seul", "clé absente", "accès refusé", "crédit épuisé", "quota ou débit",
    "modèle inconnu", "modèle substitué", "réponse illisible", "injoignable",
    "plafond", "sortie hors plafond", "inconnu",
)

MOTIFS_CREDIT = re.compile(
    r"credit balance is too low|insufficient_quota|exceeded_current_quota|"
    r"billing|payment|insufficient balance|suspended", re.I)
MOTIFS_MODELE = re.compile(r"model_not_found|not_found_error|does not exist|"
                           r"no such model|is not found|unknown model", re.I)


def heure_utc() -> str:
    return _dt.datetime.now(_dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def pire_appel_usd(couple: dict) -> float:
    e = couple["tarif_entree_usd_par_million"]
    s = couple["tarif_sortie_usd_par_million"]
    return (ENTREE_MAX_JETONS * e + couple.get("sortie_max", 1) * s) / 1e6


def requete(couple: dict, cle: str) -> tuple[str, dict, bytes]:
    f, m, n = couple["fournisseur"], couple["modele"], couple.get("sortie_max", 1)
    if f == "anthropic":
        h = {"x-api-key": cle, "anthropic-version": "2023-06-01",
             "content-type": "application/json"}
        b = {"model": m, "max_tokens": n, "messages": [{"role": "user", "content": INVITE}]}
        return HOTES[f], h, json.dumps(b).encode()
    if f in ("openai", "kimi"):
        h = {"authorization": "Bearer " + cle, "content-type": "application/json"}
        champ = "max_completion_tokens" if f == "openai" else "max_tokens"
        b = {"model": m, champ: n, "messages": [{"role": "user", "content": INVITE}]}
        return HOTES[f], h, json.dumps(b).encode()
    if f == "google":
        h = {"x-goog-api-key": cle, "content-type": "application/json"}
        b = {"contents": [{"role": "user", "parts": [{"text": INVITE}]}]}  # countTokens : rien n'est généré
        return HOTES[f].format(modele=m), h, json.dumps(b).encode()
    raise ValueError("fournisseur hors liste")


def transport_reel(url: str, entetes: dict, corps: bytes, delai: float = 60.0):
    req = urllib.request.Request(url, data=corps, headers=entetes, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=delai) as r:
            return r.status, r.read()
    except urllib.error.HTTPError as e:
        return e.code, e.read()


def _code_erreur(d: dict) -> str:
    err = d.get("error") if isinstance(d, dict) else None
    if isinstance(err, dict):
        return " ".join(str(err.get(k, "")) for k in ("type", "code", "status")).strip()
    return ""


def _modele_servi(f: str, d: dict) -> str | None:
    if f == "google":
        return d.get("modelVersion")
    return d.get("model")


def _usage(f: str, d: dict) -> tuple[int, int] | None:
    try:
        if f == "anthropic":
            u = d["usage"]; return int(u["input_tokens"]), int(u["output_tokens"])
        if f == "google":
            u = d["usageMetadata"]
            sortie = int(u.get("candidatesTokenCount", 0)) + int(u.get("thoughtsTokenCount", 0))
            return int(u["promptTokenCount"]), sortie
        u = d["usage"]; return int(u["prompt_tokens"]), int(u["completion_tokens"])
    except (KeyError, TypeError, ValueError):
        return None


def classer(couple: dict, statut: int, octets: bytes) -> tuple[str, dict]:
    """Rend (raison, détails sûrs). Ne garde jamais le texte d'erreur."""
    f, m = couple["fournisseur"], couple["modele"]
    texte = octets.decode("utf-8", "replace")
    try:
        d = json.loads(texte)
    except ValueError:
        d = None
    code = _code_erreur(d) if isinstance(d, dict) else ""
    details = {"http": statut, "code_erreur": code[:80]}
    if statut == 200 and f == "google":
        if not isinstance(d, dict) or not isinstance(d.get("totalTokens"), int) or d["totalTokens"] < 1:
            return "réponse illisible", details
        details.update({"entree_jetons": d["totalTokens"], "sortie_jetons": 0, "cout_usd": 0.0,
                        "credit_prouve": False})
        return "prêt, accès seul", details
    if statut == 200:
        if not isinstance(d, dict):
            return "réponse illisible", details
        u = _usage(f, d)
        if u is None:
            return "réponse illisible", details
        servi = _modele_servi(f, d)
        details.update({"entree_jetons": u[0], "sortie_jetons": u[1], "modele_servi": servi})
        if servi is None or not (servi == m or servi.startswith(m + "-")):
            return "modèle substitué", details
        if u[1] > couple.get("sortie_max", 1):
            return "sortie hors plafond", details
        cout = (u[0] * couple["tarif_entree_usd_par_million"] +
                u[1] * couple["tarif_sortie_usd_par_million"]) / 1e6
        details["cout_usd"] = round(cout, 6)
        details["credit_prouve"] = True
        return "prêt", details
    if MOTIFS_CREDIT.search(texte) or statut == 402:
        return "crédit épuisé", details
    if statut in (401, 403):
        return "accès refusé", details
    if statut == 404 or MOTIFS_MODELE.search(texte):
        return "modèle inconnu", details
    if statut == 429:
        return "quota ou débit", details
    return "inconnu", details


def essayer(couple: dict, environ: dict, transport) -> dict:
    ligne = {"heure": heure_utc(), "cle_var": couple["cle_var"],
             "fournisseur": couple["fournisseur"], "modele": couple["modele"]}
    if couple["fournisseur"] not in HOTES:
        ligne.update(verdict="manque", raison="inconnu"); return ligne
    n = couple.get("sortie_max", 1)
    if not isinstance(n, int) or not 1 <= n <= SORTIE_MAX_PERMISE:
        ligne.update(verdict="manque", raison="plafond"); return ligne
    pire = pire_appel_usd(couple)
    ligne["pire_usd"] = round(pire, 6)
    if pire > couple.get("plafond_appel_usd", PLAFOND_APPEL_USD) or pire > PLAFOND_APPEL_USD:
        ligne.update(verdict="manque", raison="plafond"); return ligne
    cle = environ.get(couple["cle_var"], "")
    if not cle.strip():
        ligne.update(verdict="manque", raison="clé absente"); return ligne
    url, h, corps = requete(couple, cle)
    try:
        statut, octets = transport(url, h, corps)
    except Exception as e:  # réseau, délai : jamais un succès
        ligne.update(verdict="manque", raison="injoignable", exception=type(e).__name__)
        return ligne
    raison, details = classer(couple, statut, octets)
    ligne.update(details)
    ligne.update(verdict="prêt" if raison in ("prêt", "prêt, accès seul") else "manque", raison=raison)
    return ligne


def lire_plan(chemin: str) -> list[dict]:
    with open(chemin, encoding="utf-8") as fh:
        plan = json.load(fh)
    requis = {"cle_var", "fournisseur", "modele",
              "tarif_entree_usd_par_million", "tarif_sortie_usd_par_million"}
    if not isinstance(plan, list) or not plan:
        raise ValueError("plan vide ou mal formé")
    for c in plan:
        if not isinstance(c, dict) or not requis <= set(c):
            raise ValueError("couple incomplet dans le plan")
        if not re.fullmatch(r"[A-Z][A-Z0-9_]{2,63}", c["cle_var"]):
            raise ValueError("nom de variable de clé hors forme")
    return plan


def go_present(go_id: str, registre: str) -> bool:
    if not re.fullmatch(r"GO-\d{4}-\d{2}-\d{2}-\d{2}", go_id or ""):
        return False
    with open(registre, encoding="utf-8") as fh:
        return any(l.startswith("| " + go_id + " |") for l in fh)


def executer(plan, environ, transport, journal: str | None) -> dict:
    lignes = [essayer(c, environ, transport) for c in plan]
    if journal:
        if os.path.exists(journal):
            raise FileExistsError("journal déjà présent : on n'écrase jamais")
        with open(journal, "w", encoding="utf-8") as fh:
            for l in lignes:
                fh.write(json.dumps(l, ensure_ascii=False, sort_keys=True) + "\n")
    par_cle: dict[str, str] = {}
    for l in lignes:
        par_cle[l["cle_var"]] = "prêt" if (par_cle.get(l["cle_var"], "prêt") == "prêt"
                                           and l["verdict"] == "prêt") else "manque"
    sans_credit = sorted({l["cle_var"] for l in lignes if l.get("raison") == "prêt, accès seul"})
    return {"lignes": lignes, "par_cle": par_cle, "credit_non_prouve": sans_credit,
            "tout_pret": all(v == "prêt" for v in par_cle.values()),
            "cout_total_usd": round(sum(l.get("cout_usd", 0) for l in lignes), 6)}


def main(argv=None) -> int:
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("--plan", required=True)
    p.add_argument("--journal", required=True)
    p.add_argument("--reel", action="store_true")
    p.add_argument("--go")
    p.add_argument("--registre-go", default="/home/user/main-lecture/registres/go.md")
    a = p.parse_args(argv)
    plan = lire_plan(a.plan)
    if not a.reel:
        print(json.dumps({"a_blanc": [{"cle_var": c["cle_var"], "modele": c["modele"],
                                       "pire_usd": round(pire_appel_usd(c), 6)} for c in plan]},
                         ensure_ascii=False, indent=1))
        return 0
    if not go_present(a.go, a.registre_go):
        print("REFUS : envoi réel sans ligne de GO présente au registre", file=sys.stderr)
        return 2
    r = executer(plan, os.environ, transport_reel, a.journal)
    print(json.dumps({"par_cle": r["par_cle"], "tout_pret": r["tout_pret"],
                      "credit_non_prouve": r["credit_non_prouve"],
                      "cout_total_usd": r["cout_total_usd"]}, ensure_ascii=False, indent=1))
    return 0 if r["tout_pret"] else 1


if __name__ == "__main__":
    sys.exit(main())
