#!/usr/bin/env python3
"""Moisson OpenAlex v2 — bibliothèque standard seulement.

v2 : seul changement de fond, la pagination est ordonnée par
`sort=publication_date:asc` (ordre stable ; l'ordre par pertinence de la v1
sautait des œuvres). Fichiers, fiches et manifeste portent le suffixe v2.

Moissonne, pour chaque sous-domaine de la requête déclarée scellée
(`requete-declaree-v2.md`), les œuvres rendues par l'interface OpenAlex
(`/works`, curseur, 200 par page, champs choisis par `select=`), et les écrit
telles quelles dans un fichier JSON Lines compressé gzip par sous-domaine.

Aucune statistique n'est calculée sur les œuvres : seuls des comptes
(œuvres écrites, doublons écartés, compte annoncé, pages, coût) sont écrits.

Gardes :
- la requête déclarée doit correspondre à son empreinte compagnon, et chaque
  filtre de ce script doit y figurer mot pour mot (sinon arrêt) ;
- compte annoncé > 60 000 : le sous-domaine n'est pas moissonné (version 2 à déclarer) ;
- un fichier définitif existant n'est jamais écrasé (R12) : le sous-domaine est
  repris de sa fiche de moisson ;
- la clé ne passe que par OPENALEX_API_KEY et n'est jamais écrite ni affichée ;
- plancher d'allocation gratuite : sous le plancher, attente de la remise à zéro.

Usage (depuis n'importe quel dossier, en mode isolé) :
    python3 -I moissonner_openalex_v2.py --dossier DOSSIER [--sous-domaine NOM ...]
    python3 -I moissonner_openalex_v2.py --dossier DOSSIER --manifeste
"""
from __future__ import annotations

import argparse
import datetime as dt
import gzip
import hashlib
import json
import os
import platform
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

VERSION_SCRIPT = "moissonner_openalex_v2 2.0.0"
BASE = "https://api.openalex.org/works"
REQUETE_DECLAREE = "requete-declaree-v2.md"
MANIFESTE = "manifeste-moisson-v2.json"
TRI = "publication_date:asc"
SUFFIXE = "v2"
SELECT = "id,doi,title,publication_date,authorships,referenced_works,concepts,topics,primary_location,type"
PAR_PAGE = 200
PAUSE_S = 0.5
PLAFOND_OEUVRES = 60_000
PLANCHER_USD = 0.15
ESSAIS_MAX = 8

SOUS_DOMAINES = {
    "controle-alignement-ia": 'publication_year:2015-2026,title_and_abstract.search:("AI safety" OR "AI alignment" OR "value alignment" OR "reward hacking" OR "specification gaming" OR "reward tampering" OR "scalable oversight" OR "deceptive alignment" OR "goal misgeneralization" OR "corrigibility" OR "inner alignment" OR "superalignment" OR "sycophancy" OR "jailbreak" OR "red teaming" OR "reinforcement learning from human feedback" OR "RLHF" OR "constitutional AI" OR "mechanistic interpretability" OR "AI control" OR "AI risk" OR "safe reinforcement learning" OR "reward model" OR "preference alignment" OR "machine ethics" OR "AI deception" OR "alignment faking" OR "emergent misalignment" OR "trusted monitoring" OR "AI oversight" OR "chain-of-thought monitoring" OR "prompt injection" OR "frontier AI" OR "dangerous capabilities" OR ("existential risk" AND ("artificial intelligence" OR "AI")) OR ("sandbagging" AND ("language model" OR "artificial intelligence")) OR ("misalignment" AND ("artificial intelligence" OR "language model")))',
    "verification-formelle": 'publication_year:2015-2026,title_and_abstract.search:("formal verification" OR "model checking" OR "theorem proving" OR "proof assistant" OR "SMT solver" OR "program verification" OR "software verification" OR "separation logic" OR "abstract interpretation" OR "deductive verification")',
    "securite-systemes": 'publication_year:2015-2026,title_and_abstract.search:("malware detection" OR "vulnerability detection" OR "software vulnerability" OR "side-channel attack" OR "fuzzing" OR "ransomware" OR "memory safety" OR "control-flow integrity" OR "operating system security" OR "binary analysis" OR "return-oriented programming")',
    "statistique-sequentielle": 'publication_year:2015-2026,title_and_abstract.search:("sequential analysis" OR "sequential test" OR "sequential probability ratio test" OR "change-point detection" OR "changepoint" OR "sequential change detection" OR "quickest detection" OR "anytime-valid" OR "optional stopping" OR "CUSUM" OR "group sequential" OR "test martingale" OR "control chart")',
    "neurosciences-computationnelles": 'publication_year:2015-2026,title_and_abstract.search:("computational neuroscience" OR "neural coding" OR "neural population dynamics" OR "neural field" OR "attractor network" OR "Hodgkin-Huxley" OR "integrate-and-fire" OR "free energy principle" OR "neural mass model" OR "neural manifold" OR "Bayesian brain" OR "spiking network model" OR "dynamic causal modelling" OR "dynamic causal modeling" OR ("predictive coding" AND (brain OR neural OR cortex OR cortical)) OR ("biophysical model" AND (neuron OR neuronal OR neural)) OR ("spiking neural network" AND (brain OR cortex OR cortical OR neuroscience OR biological)) OR ("synaptic plasticity" AND (model OR simulation OR computational)))',
}


class Arret(Exception):
    """Arrêt explicite (aucun repli silencieux)."""


def maintenant() -> str:
    return dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def empreinte(chemin: str) -> str:
    h = hashlib.sha256()
    with open(chemin, "rb") as f:
        for bloc in iter(lambda: f.read(1 << 20), b""):
            h.update(bloc)
    return h.hexdigest()


def sceller(chemin: str) -> None:
    """Écrit le compagnon .sha256 au format sha256sum ; refuse d'écraser (R12)."""
    comp = chemin + ".sha256"
    if os.path.exists(comp):
        raise Arret(f"compagnon déjà présent, non écrasé : {os.path.basename(comp)}")
    with open(comp, "x", encoding="utf-8") as f:
        f.write(f"{empreinte(chemin)}  {os.path.basename(chemin)}\n")


def verifier_requete_declaree(dossier: str) -> str:
    chemin = os.path.join(dossier, REQUETE_DECLAREE)
    comp = chemin + ".sha256"
    if not (os.path.isfile(chemin) and os.path.isfile(comp)):
        raise Arret("requête déclarée ou son empreinte absente : moisson refusée")
    attendu = open(comp, encoding="utf-8").read().split()[0]
    reel = empreinte(chemin)
    if attendu != reel:
        raise Arret("requête déclarée modifiée depuis son scellement : moisson refusée")
    texte = open(chemin, encoding="utf-8").read()
    for nom, filtre in SOUS_DOMAINES.items():
        if filtre not in texte:
            raise Arret(f"filtre de {nom} absent mot pour mot de la requête déclarée")
    return reel


def cle() -> str:
    k = os.environ.get("OPENALEX_API_KEY", "")
    if not k:
        raise Arret("OPENALEX_API_KEY absente")
    return k


def url_publique(filtre: str, curseur: str) -> str:
    """URL sans clé, pour le manifeste et les messages."""
    q = urllib.parse.urlencode(
        {"filter": filtre, "per-page": PAR_PAGE, "sort": TRI, "cursor": curseur, "select": SELECT},
        quote_via=urllib.parse.quote,
    )
    return f"{BASE}?{q}"


def _sans_cle(texte: str, k: str) -> str:
    return texte.replace(k, "***") if k else texte


def obtenir(filtre: str, curseur: str, etat: dict) -> dict:
    k = cle()
    url = url_publique(filtre, curseur) + "&" + urllib.parse.urlencode({"api_key": k})
    for essai in range(1, ESSAIS_MAX + 1):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "moisson-openalex-v2 (research-bot@example.org)"})
            with urllib.request.urlopen(req, timeout=120) as rep:
                corps = rep.read()
                h = rep.headers
                cout = h.get("X-RateLimit-Cost-USD")
                if cout:
                    etat["cout_usd"] = round(etat.get("cout_usd", 0.0) + float(cout), 6)
                restant = h.get("X-RateLimit-Remaining-USD")
                reset = h.get("X-RateLimit-Reset")
                etat["requetes"] = etat.get("requetes", 0) + 1
                donnees = json.loads(corps)
                if restant is not None and float(restant) < PLANCHER_USD:
                    attente = int(reset or 3600) + 90
                    print(f"[{maintenant()}] plancher d'allocation atteint ; attente {attente} s", flush=True)
                    time.sleep(attente)
                else:
                    time.sleep(PAUSE_S)
                return donnees
        except urllib.error.HTTPError as e:
            code = e.code
            retry = e.headers.get("Retry-After") if e.headers else None
            reset = e.headers.get("X-RateLimit-Reset") if e.headers else None
            if code == 429:
                attente = int(float(retry)) if retry else int(reset or 60) + 60
                attente = max(attente, 30)
                print(f"[{maintenant()}] 429 (essai {essai}) ; attente {attente} s", flush=True)
                time.sleep(attente)
                continue
            if 500 <= code < 600:
                attente = min(300, 10 * 2 ** essai)
                print(f"[{maintenant()}] {code} (essai {essai}) ; attente {attente} s", flush=True)
                time.sleep(attente)
                continue
            raise Arret(_sans_cle(f"erreur HTTP {code} : {e.reason}", k)) from None
        except (urllib.error.URLError, TimeoutError, ConnectionError, json.JSONDecodeError) as e:
            attente = min(300, 10 * 2 ** essai)
            print(f"[{maintenant()}] {_sans_cle(type(e).__name__ + ' ' + str(e), k)} (essai {essai}) ; attente {attente} s", flush=True)
            time.sleep(attente)
    raise Arret(f"{ESSAIS_MAX} essais épuisés")


def moissonner(dossier: str, nom: str, empreinte_requete: str) -> dict:
    filtre = SOUS_DOMAINES[nom]
    final = os.path.join(dossier, f"{nom}-{SUFFIXE}.jsonl.gz")
    fiche = final + ".moisson.json"
    if os.path.exists(final):
        if not os.path.exists(fiche):
            raise Arret(f"{os.path.basename(final)} existe sans fiche de moisson : à examiner, non écrasé")
        print(f"[{maintenant()}] {nom} : déjà moissonné, repris de sa fiche", flush=True)
        return json.load(open(fiche, encoding="utf-8"))
    partiel = final + ".partiel"
    if os.path.exists(partiel):
        raise Arret(f"{os.path.basename(partiel)} existe (moisson interrompue) : à examiner, non écrasé")
    etat: dict = {}
    debut = maintenant()
    curseur = "*"
    vus: set = set()
    ecrites = doublons = sans_id = pages = 0
    compte_annonce = None
    with gzip.open(partiel, "xt", encoding="utf-8", compresslevel=6) as sortie:
        while curseur:
            d = obtenir(filtre, curseur, etat)
            pages += 1
            meta = d.get("meta") or {}
            if compte_annonce is None:
                compte_annonce = meta.get("count")
                if compte_annonce is None:
                    raise Arret(f"{nom} : réponse sans meta.count")
                if compte_annonce > PLAFOND_OEUVRES:
                    sortie.close()
                    os.rename(partiel, partiel + ".refuse")
                    raise Arret(f"{nom} : {compte_annonce} > {PLAFOND_OEUVRES} ; version 2 à déclarer")
                print(f"[{maintenant()}] {nom} : compte annoncé {compte_annonce}", flush=True)
            res = d.get("results")
            if res is None:
                raise Arret(f"{nom} : réponse sans results à la page {pages}")
            for oeuvre in res:
                ident = oeuvre.get("id")
                if not ident:
                    sans_id += 1
                    continue
                if ident in vus:
                    doublons += 1
                    continue
                vus.add(ident)
                sortie.write(json.dumps(oeuvre, ensure_ascii=False, separators=(",", ":")) + "\n")
                ecrites += 1
            curseur = meta.get("next_cursor")
            if not res:
                break
            if pages % 25 == 0:
                print(f"[{maintenant()}] {nom} : {pages} pages, {ecrites} œuvres", flush=True)
    os.rename(partiel, final)
    sceller(final)
    fiche_d = {
        "sous_domaine": nom,
        "fichier": os.path.basename(final),
        "sha256": empreinte(final),
        "octets": os.path.getsize(final),
        "filtre": filtre,
        "requete_premiere_page_sans_cle": url_publique(filtre, "*"),
        "debut_utc": debut,
        "fin_utc": maintenant(),
        "compte_annonce_premiere_page": compte_annonce,
        "oeuvres_ecrites": ecrites,
        "doublons_ecartes": doublons,
        "oeuvres_sans_id_ecartees": sans_id,
        "ecart_ecrites_moins_annonce": ecrites - compte_annonce,
        "pages": pages,
        "requetes_http_reussies": etat.get("requetes", 0),
        "cout_usd_allocation_gratuite": etat.get("cout_usd", 0.0),
        "empreinte_requete_declaree": empreinte_requete,
        "version_script": VERSION_SCRIPT,
    }
    with open(fiche, "x", encoding="utf-8") as f:
        json.dump(fiche_d, f, ensure_ascii=False, indent=2)
        f.write("\n")
    sceller(fiche)
    print(f"[{maintenant()}] {nom} : terminé, {ecrites} œuvres, {pages} pages", flush=True)
    return fiche_d


def ecrire_manifeste(dossier: str, empreinte_requete: str) -> None:
    chemin = os.path.join(dossier, MANIFESTE)
    if os.path.exists(chemin):
        raise Arret(f"{MANIFESTE} existe déjà : non écrasé")
    fiches = []
    for nom in SOUS_DOMAINES:
        fiche = os.path.join(dossier, f"{nom}-{SUFFIXE}.jsonl.gz.moisson.json")
        if not os.path.exists(fiche):
            raise Arret(f"fiche absente pour {nom} : manifeste refusé")
        fd = json.load(open(fiche, encoding="utf-8"))
        fichier = os.path.join(dossier, fd["fichier"])
        if empreinte(fichier) != fd["sha256"]:
            raise Arret(f"{fd['fichier']} ne correspond plus à son empreinte")
        fiches.append(fd)
    script = os.path.abspath(__file__)
    m = {
        "objet": "moisson OpenAlex v2 (message n° 265 de conv-audit, point 1 ; go R-633) ; remplace la v1 dont l'ordre par pertinence sautait des œuvres",
        "lignee": "session-depot",
        "remplace": {"requete_declaree_v1_sha256": "a29b09fb03ee85063e3049a92600dedf6c5f935916ba72728d5ec8a60f8f95dc", "script_v1_sha256": "356b378e0a6bb3005be67b8662050142c22b66585e978466fbdcf7148c92fd6a", "fichier_v1_garde_incomplet": "controle-alignement-ia-v1.jsonl.gz"},
        "requete_declaree": {"fichier": REQUETE_DECLAREE, "sha256": empreinte_requete},
        "script": {"fichier": os.path.basename(script), "version": VERSION_SCRIPT, "sha256": empreinte(script)},
        "python": sys.version.split()[0],
        "plateforme": platform.platform(),
        "interface": BASE,
        "parametres": {"per-page": PAR_PAGE, "sort": TRI, "select": SELECT, "pagination": "curseur", "pause_s": PAUSE_S,
                       "plafond_oeuvres": PLAFOND_OEUVRES, "plancher_allocation_usd": PLANCHER_USD,
                       "cle": "variable d'environnement OPENALEX_API_KEY, jamais écrite"},
        "moisson_debut_utc": min(f["debut_utc"] for f in fiches),
        "moisson_fin_utc": max(f["fin_utc"] for f in fiches),
        "fichiers": fiches,
        "total_oeuvres_ecrites": sum(f["oeuvres_ecrites"] for f in fiches),
        "total_octets": sum(f["octets"] for f in fiches),
        "total_cout_usd_allocation_gratuite": round(sum(f["cout_usd_allocation_gratuite"] for f in fiches), 6),
        "manifeste_ecrit_utc": maintenant(),
    }
    with open(chemin, "x", encoding="utf-8") as f:
        json.dump(m, f, ensure_ascii=False, indent=2)
        f.write("\n")
    sceller(chemin)
    print(f"[{maintenant()}] manifeste écrit", flush=True)


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--dossier", required=True)
    p.add_argument("--sous-domaine", action="append", choices=list(SOUS_DOMAINES))
    p.add_argument("--manifeste", action="store_true")
    a = p.parse_args()
    dossier = os.path.abspath(a.dossier)
    try:
        emp = verifier_requete_declaree(dossier)
        if a.manifeste:
            ecrire_manifeste(dossier, emp)
            return 0
        for nom in a.sous_domaine or list(SOUS_DOMAINES):
            moissonner(dossier, nom, emp)
        return 0
    except Arret as e:
        print(f"[{maintenant()}] ARRÊT : {e}", file=sys.stderr, flush=True)
        return 2


if __name__ == "__main__":
    sys.exit(main())
