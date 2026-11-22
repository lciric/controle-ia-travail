"""Véhicule NA-1, lot 11 — exécutant de la passe X — v1.

Sert la pièce fusionnée scellée (39fb4e93…) aux huit proposeurs de la passe X, une requête par proposeur, en flux,
selon le devis v3 scellé (83a3f035…) et l'additif du véhicule v2 (X-1 à X-11), sous GO-2026-11-22-46, -48 et -54.

Gardes, toutes avant tout envoi sauf mention :
- G1  pièce : empreinte égale à 39fb4e93… (n° 14, X-4) ; zéro motif à la garde de motifs de l'outil de relecture
      (`relecture_fable_api_v3.garde_motifs_ligne`, n° 38) ;
- G2  configuration scellée : empreinte de son fichier égale à son compagnon `.sha256` ; champs en liste fermée ;
- G3  lignes de GO présentes au registre (chaque identifiant donné) ;
- G4  garde de départ « prêt / manque » v2 rejouée juste avant l'envoi : toutes les clés « prêt », sinon rien ne part ;
- G5  pire d'une tentative ≤ 6,05 USD (P4) : entrée bornée (octets de la pièce + 512) et sortie maximale, au tarif ;
- G6  Google : `garde_google_v3.verifier_reglages_google` sur le corps tel qu'il part (mode « flux ») ; après la
      réponse, `defaut_reponse_google` (un défaut n'est jamais une réponse) ;
- G7  arrêt n° 12 par clé : avant chaque tentative, cumul compté + pire des tentatives en vol + pire de celle-ci
      ≤ sous-part de la clé, sinon refus nommé, sans bascule ; et somme ≤ P_X (96,80) ;
- G8  arrêt n° 13 : un refus pour crédit arrête la passe : aucune tentative neuve ne part ensuite ;
- G9  repli de GO-35 (Opus 4.6 puis Sonnet 4.6), sur le seul refus de classifieur d'un modèle Claude, selon la chaîne
      du devis ; chaque tentative servie par repli est marquée `par_repli` et attribuée au modèle servi ;
- G10 quarantaine (X-5) : le flux brut de chaque tentative est écrit tel quel dans un fichier neuf de la quarantaine,
      avec son compagnon ; aucun texte de réponse n'est affiché, journalisé ni rendu ; seuls des comptes, des classes,
      des empreintes et des coûts sortent ;
- G11 clés lues par le nom de leur variable, jamais affichées ; aucun texte d'erreur de fournisseur gardé hors de la
      quarantaine ;
- G12 modèle servi comparé au modèle demandé (n° 31) : un écart classe la tentative « modèle substitué ».
Coût : usage déclaré × tarif ; usage illisible ou flux coupé après le début : coût inconnu, compté au pire (A3).
"""
from __future__ import annotations

import argparse
import datetime as _dt
import hashlib
import json
import os
import re
import sys
import threading
import time
import urllib.error
import urllib.request
from decimal import Decimal as D, ROUND_CEILING

RACINE = "/home/user/controle-ia-travail"
sys.path.insert(0, RACINE + "/src")
sys.path.insert(0, RACINE + "/docs/notes/ideation-nouvelles-attaques-v1/garde-depart-cles-v2")
from controle_ia.relecture_fable_api_v3 import garde_motifs_ligne  # noqa: E402
import garde_depart_cles_v2 as GD  # noqa: E402
import importlib.util  # noqa: E402


def _charger_scelle(nom, chemin):
    """Charge un module par son chemin, après contrôle de son empreinte contre son compagnon `.sha256`."""
    octets = open(chemin, "rb").read()
    if open(chemin + ".sha256").read().split()[0] != hashlib.sha256(octets).hexdigest():
        raise ImportError(f"{chemin} : empreinte différente de son compagnon")
    spec = importlib.util.spec_from_file_location(nom, chemin)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


GG = _charger_scelle("garde_google_v3", "/home/user/main-lecture/src/controle_ia/garde_google_v3.py")

VERSION = "passe-x-na-v1"
EMPREINTE_PIECE = "39fb4e93f26f6447822a9f548053b1ca8f8156d714d3d55bb8c0369a11b9db2a"
PIRE_TENTATIVE = D("6.05")
P_X = D("96.80")
ENVELOPPE = 512
GO_EXIGES = ("GO-2026-11-22-46", "GO-2026-11-22-48", "GO-2026-11-22-54")
FOURNISSEURS = ("anthropic", "openai", "kimi", "google")
HOTES = {
    "anthropic": "https://api.anthropic.com/v1/messages",
    "openai": "https://api.openai.com/v1/chat/completions",
    "kimi": "https://api.moonshot.ai/v1/chat/completions",
    "google": "https://generativelanguage.googleapis.com/v1beta/models/{modele}:streamGenerateContent?alt=sse",
}
EXTRAS_PERMIS = {"anthropic": {"thinking", "output_config"}, "openai": {"reasoning_effort"}, "kimi": set(),
                 "google": set()}
CLES_PROPOSEUR = {"id", "fournisseur", "cle_var", "chaine"}
CLES_MAILLON = {"modele", "tarif_entree", "tarif_sortie", "sortie_max", "extras", "google"}
CLASSES = ("réponse rendue", "refus du modèle (classifieur)", "réponse illisible", "défaut Google", "modèle substitué",
           "crédit épuisé", "erreur de requête", "injoignable", "refusée avant envoi (arrêt n° 12)",
           "non partie (arrêt n° 13)")
MOTIFS_CREDIT = re.compile(r"credit balance is too low|insufficient_quota|exceeded_current_quota|insufficient balance|"
                           r"billing|suspended", re.I)
DELAI_SILENCE_S = 900
DELAI_TOTAL_S = 5400


class Refus(Exception):
    """Refus avant tout envoi : rien ne part."""


def heure() -> str:
    return _dt.datetime.now(_dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def sha(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def usd(x) -> str:
    return str(D(x).quantize(D("0.000001")))


# ---------- G1, G2, G3 ----------
def verifier_piece(chemin: str) -> bytes:
    b = open(chemin, "rb").read()
    if sha(b) != EMPREINTE_PIECE:
        raise Refus("G1 : empreinte de la pièce différente de 39fb4e93…")
    for n, ligne in enumerate(b.decode("utf-8").split("\n"), 1):
        if garde_motifs_ligne(ligne):
            raise Refus(f"G1 : la garde de motifs mord à la ligne {n} de la pièce")
    return b


def lire_configuration(chemin: str) -> dict:
    b = open(chemin, "rb").read()
    comp = chemin + ".sha256"
    if not os.path.exists(comp) or open(comp).read().split()[0] != sha(b):
        raise Refus("G2 : configuration sans compagnon, ou empreinte différente")
    c = json.loads(b)
    if set(c) != {"version", "proposeurs", "sous_parts"} or c["version"] != VERSION:
        raise Refus("G2 : clés de la configuration hors liste")
    ids = set()
    for p in c["proposeurs"]:
        if set(p) != CLES_PROPOSEUR or p["fournisseur"] not in FOURNISSEURS or p["id"] in ids:
            raise Refus("G2 : proposeur mal formé")
        ids.add(p["id"])
        if not re.fullmatch(r"[A-Z][A-Z0-9_]{2,63}", p["cle_var"]) or not p["chaine"]:
            raise Refus("G2 : proposeur mal formé")
        if p["fournisseur"] != "anthropic" and len(p["chaine"]) != 1:
            raise Refus("G9 : seule une chaîne Claude a un repli")
        for m in p["chaine"]:
            if not set(m) <= CLES_MAILLON or not {"modele", "tarif_entree", "tarif_sortie", "sortie_max"} <= set(m):
                raise Refus("G2 : maillon mal formé")
            if not set(m.get("extras", {})) <= EXTRAS_PERMIS[p["fournisseur"]]:
                raise Refus("G2 : réglage non admis pour ce fournisseur")
            if (p["fournisseur"] == "google") != ("google" in m):
                raise Refus("G6 : réglages Google absents ou en trop")
    for p in c["proposeurs"]:
        if p["cle_var"] not in c["sous_parts"]:
            raise Refus("G7 : clé sans sous-part")
    if sum(D(str(v)) for v in c["sous_parts"].values()) > P_X:
        raise Refus("G7 : somme des sous-parts au-delà de P_X")
    return c


def verifier_go(registre: str, ids=GO_EXIGES):
    lignes = open(registre, encoding="utf-8").read().split("\n")
    for g in ids:
        if not any(l.startswith("| " + g + " |") for l in lignes):
            raise Refus(f"G3 : {g} absent du registre")


# ---------- G5, G6 : requêtes ----------
def pire(maillon: dict, octets_piece: int) -> D:
    return ((D(octets_piece + ENVELOPPE) * D(str(maillon["tarif_entree"])) +
             D(maillon["sortie_max"]) * D(str(maillon["tarif_sortie"]))) / D(10**6)).quantize(D("0.000001"), ROUND_CEILING)


def corps_requete(fournisseur: str, maillon: dict, texte: str) -> dict:
    m, n, ex = maillon["modele"], maillon["sortie_max"], maillon.get("extras", {})
    msg = [{"role": "user", "content": texte}]
    if fournisseur == "anthropic":
        return dict({"model": m, "max_tokens": n, "messages": msg, "stream": True}, **ex)
    if fournisseur == "openai":
        return dict({"model": m, "max_completion_tokens": n, "messages": msg, "stream": True,
                     "stream_options": {"include_usage": True}}, **ex)
    if fournisseur == "kimi":
        return {"model": m, "max_tokens": n, "messages": msg, "stream": True, "stream_options": {"include_usage": True}}
    g = maillon["google"]
    return {"contents": [{"role": "user", "parts": [{"text": texte}]}],
            "generationConfig": {"maxOutputTokens": n,
                                 "thinkingConfig": {"thinkingLevel": g["niveau"], "includeThoughts": True}}}


def verifier_google(maillon: dict, corps: dict):
    g = maillon["google"]
    pb = GG.verifier_reglages_google(g["espece"], corps, provision=g["provision"], mots=None, mode="flux")
    if pb:
        raise Refus("G6 : " + " ; ".join(pb))


def entetes(fournisseur: str, cle: str) -> dict:
    if fournisseur == "anthropic":
        return {"x-api-key": cle, "anthropic-version": "2023-06-01", "content-type": "application/json"}
    if fournisseur == "google":
        return {"x-goog-api-key": cle, "content-type": "application/json"}
    return {"authorization": "Bearer " + cle, "content-type": "application/json"}


# ---------- lecture des flux ----------
def lire_flux(fournisseur: str, evenements) -> dict:
    """`evenements` : objets JSON des lignes `data:` du flux. Rend texte (pour le compte seulement), usage, fin, modèle."""
    r = {"texte": [], "pensee_jetons": None, "entree": None, "sortie": None, "fin": None, "modele": None,
         "blocage": None, "erreur": None, "credit": False}
    for e in evenements:
        if not isinstance(e, dict):
            continue
        if "error" in e and isinstance(e["error"], dict):
            err = e["error"]
            r["erreur"] = " ".join(str(err.get(k, "")) for k in ("type", "code", "status")).strip() or "erreur"
            # le message n'est jamais gardé (il peut contenir un fragment de clé) : seul le constat « crédit » en sort
            r["credit"] = bool(MOTIFS_CREDIT.search(r["erreur"] + " " + str(err.get("message", ""))))
            continue
        if fournisseur == "anthropic":
            t = e.get("type")
            if t == "message_start":
                msg = e.get("message", {})
                r["modele"] = msg.get("model")
                r["entree"] = (msg.get("usage") or {}).get("input_tokens")
            elif t == "content_block_delta" and (e.get("delta") or {}).get("type") == "text_delta":
                r["texte"].append(e["delta"].get("text", ""))
            elif t == "message_delta":
                r["fin"] = (e.get("delta") or {}).get("stop_reason")
                r["sortie"] = (e.get("usage") or {}).get("output_tokens")
        elif fournisseur in ("openai", "kimi"):
            r["modele"] = e.get("model", r["modele"])
            for ch in e.get("choices") or []:
                d = ch.get("delta") or {}
                if d.get("content"):
                    r["texte"].append(d["content"])
                if ch.get("finish_reason"):
                    r["fin"] = ch["finish_reason"]
            u = e.get("usage")
            if isinstance(u, dict):
                r["entree"], r["sortie"] = u.get("prompt_tokens"), u.get("completion_tokens")
        else:
            r["modele"] = e.get("modelVersion", r["modele"])
            pf = e.get("promptFeedback") or {}
            if pf.get("blockReason"):
                r["blocage"] = pf["blockReason"]
            for c in e.get("candidates") or []:
                for part in (c.get("content") or {}).get("parts") or []:
                    if part.get("text") and not part.get("thought"):
                        r["texte"].append(part["text"])
                if c.get("finishReason"):
                    r["fin"] = c["finishReason"]
            u = e.get("usageMetadata")
            if isinstance(u, dict):
                r["entree"] = u.get("promptTokenCount")
                r["sortie"] = (u.get("candidatesTokenCount") or 0) + (u.get("thoughtsTokenCount") or 0)
                r["pensee_jetons"] = u.get("thoughtsTokenCount")
    r["texte"] = "".join(r["texte"])
    return r


def classer(fournisseur: str, maillon: dict, r: dict) -> str:
    if r["erreur"]:
        return "crédit épuisé" if r["credit"] else "erreur de requête"
    servi, m = r["modele"], maillon["modele"]
    if fournisseur == "google":
        if GG.defaut_reponse_google(r["fin"], r["texte"], r["pensee_jetons"], blocage=r["blocage"]):
            return "défaut Google"
    elif fournisseur == "anthropic" and r["fin"] == "refusal":
        return "refus du modèle (classifieur)"
    elif r["fin"] not in ("end_turn", "stop") or not r["texte"].strip():
        return "réponse illisible"
    if servi is None or not (servi == m or servi.startswith(m + "-")):
        return "modèle substitué"
    return "réponse rendue"


def cout(maillon: dict, r: dict, pire_t: D):
    e, s = r.get("entree"), r.get("sortie")
    if not isinstance(e, int) or not isinstance(s, int) or isinstance(e, bool) or isinstance(s, bool):
        return pire_t, True
    c = (D(e) * D(str(maillon["tarif_entree"])) + D(s) * D(str(maillon["tarif_sortie"]))) / D(10**6)
    return min(c, pire_t) if s <= maillon["sortie_max"] else pire_t, s > maillon["sortie_max"]


# ---------- transport réel (urllib : honore le mandataire du conteneur) ----------
def transport_reel(url: str, ent: dict, corps: bytes, brut):
    """Rend (statut, générateur d'objets JSON). Écrit chaque octet reçu dans `brut` (quarantaine)."""
    req = urllib.request.Request(url, data=corps, headers=ent, method="POST")
    try:
        rep = urllib.request.urlopen(req, timeout=DELAI_SILENCE_S)
    except urllib.error.HTTPError as e:
        b = e.read()
        brut.write(b)
        try:
            return e.code, iter([json.loads(b)])
        except ValueError:
            return e.code, iter([{"error": {"type": "corps illisible"}}])

    def gen():
        debut = time.monotonic()
        for ligne in rep:
            brut.write(ligne)
            if time.monotonic() - debut > DELAI_TOTAL_S:
                raise TimeoutError("délai total")
            l = ligne.strip()
            if l.startswith(b"data:"):
                charge = l[5:].strip()
                if charge == b"[DONE]":
                    continue
                try:
                    yield json.loads(charge)
                except ValueError:
                    yield {"error": {"type": "ligne illisible"}}
    return rep.status, gen()


# ---------- course de la passe X ----------
class Passe:
    def __init__(self, config, piece: bytes, environ, transport, quarantaine: str, journal: str):
        self.c, self.piece, self.env, self.transport = config, piece, environ, transport
        self.texte = piece.decode("utf-8")
        self.q, self.journal = quarantaine, journal
        self.verrou = threading.Lock()
        self.cumul = {k: D(0) for k in config["sous_parts"]}
        self.en_vol = {k: D(0) for k in config["sous_parts"]}
        self.arret_13 = threading.Event()
        self.lignes = []
        for p in config["proposeurs"]:
            for m in p["chaine"]:
                if pire(m, len(piece)) > PIRE_TENTATIVE:
                    raise Refus(f"G5 : pire d'une tentative de {p['id']} au-delà de 6,05")
                if p["fournisseur"] == "google":
                    verifier_google(m, corps_requete("google", m, self.texte))
            if not (environ.get(p["cle_var"]) or "").strip():
                raise Refus(f"G11 : clé {p['cle_var']} absente")

    def _ecrire(self, ligne: dict):
        with self.verrou:
            self.lignes.append(ligne)
            with open(self.journal, "a", encoding="utf-8") as f:
                f.write(json.dumps(ligne, ensure_ascii=False, sort_keys=True) + "\n")

    def _reserver(self, cle: str, p_t: D) -> bool:
        with self.verrou:
            total = sum(self.cumul.values()) + sum(self.en_vol.values())
            if self.cumul[cle] + self.en_vol[cle] + p_t > D(str(self.c["sous_parts"][cle])) or total + p_t > P_X:
                return False
            self.en_vol[cle] += p_t
            return True

    def tentative(self, p: dict, rang: int, maillon: dict) -> str:
        cle, f = p["cle_var"], p["fournisseur"]
        p_t = pire(maillon, len(self.piece))
        base = {"version": VERSION, "proposeur": p["id"], "fournisseur": f, "cle_var": cle, "rang_repli": rang,
                "par_repli": rang > 0, "modele_demande": maillon["modele"], "pire_usd": usd(p_t), "heure": heure()}
        if self.arret_13.is_set():
            base.update(classe="non partie (arrêt n° 13)", cout_usd="0.000000")
            self._ecrire(base)
            return base["classe"]
        if not self._reserver(cle, p_t):
            base.update(classe="refusée avant envoi (arrêt n° 12)", cout_usd="0.000000")
            self._ecrire(base)
            return base["classe"]
        nom = f"{p['id']}-rang-{rang}-{maillon['modele']}.flux"
        chemin = os.path.join(self.q, nom)
        corps = json.dumps(corps_requete(f, maillon, self.texte)).encode()
        url = HOTES[f].format(modele=maillon["modele"])
        r, c, inconnu, statut = None, p_t, True, None
        try:
            with open(chemin, "xb") as brut:
                try:
                    statut, evs = self.transport(url, entetes(f, self.env[cle]), corps, brut)
                    r = lire_flux(f, evs)
                    classe = classer(f, maillon, r)
                    if statut != 200 and classe not in ("crédit épuisé",):
                        classe = "crédit épuisé" if statut == 402 else "erreur de requête"
                    if statut != 200:
                        c, inconnu = D(0), False  # erreur rendue par un statut avant tout octet de réponse : coût nul
                    else:
                        c, inconnu = cout(maillon, r, p_t)
                except (OSError, TimeoutError, ValueError) as e:
                    classe, base["exception"] = "injoignable", type(e).__name__
        finally:
            with self.verrou:
                self.en_vol[cle] -= p_t
                self.cumul[cle] += c
        if classe == "crédit épuisé":
            self.arret_13.set()
        b = open(chemin, "rb").read()
        with open(chemin + ".sha256", "x") as fc:
            fc.write(f"{sha(b)}  {nom}\n")
        base.update(classe=classe, http=statut, cout_usd=usd(c), cout_inconnu=inconnu, flux_sha256=sha(b),
                    flux_octets=len(b), fin=(r or {}).get("fin"), modele_servi=(r or {}).get("modele"),
                    entree_jetons=(r or {}).get("entree"), sortie_jetons=(r or {}).get("sortie"),
                    texte_signes=len((r or {}).get("texte") or ""), heure_fin=heure())
        self._ecrire(base)
        return classe

    def chaine(self, p: dict):
        for rang, m in enumerate(p["chaine"]):
            classe = self.tentative(p, rang, m)
            if classe != "refus du modèle (classifieur)":
                return

    def courir(self, en_parallele=True):
        fils = [threading.Thread(target=self.chaine, args=(p,)) for p in self.c["proposeurs"]]
        if en_parallele:
            for t in fils:
                t.start()
            for t in fils:
                t.join()
        else:
            for t in fils:
                t.run()
        par_cle = {k: usd(v) for k, v in self.cumul.items()}
        return {"version": VERSION, "par_cle_usd": par_cle, "total_usd": usd(sum(self.cumul.values())),
                "arret_13": self.arret_13.is_set(),
                "classes": {p["id"]: [l["classe"] for l in self.lignes if l["proposeur"] == p["id"]]
                            for p in self.c["proposeurs"]}}


def main(argv=None) -> int:
    a = argparse.ArgumentParser(description="Exécutant de la passe X, v1")
    a.add_argument("--piece", required=True)
    a.add_argument("--configuration", required=True)
    a.add_argument("--plan-garde", required=True)
    a.add_argument("--quarantaine", required=True)
    a.add_argument("--journal", required=True)
    a.add_argument("--registre-go", default="/home/user/main-lecture/registres/go.md")
    a.add_argument("--reel", action="store_true")
    o = a.parse_args(argv)
    try:
        piece = verifier_piece(o.piece)
        c = lire_configuration(o.configuration)
        verifier_go(o.registre_go)
        if os.path.exists(o.journal) or (os.path.exists(o.quarantaine) and os.listdir(o.quarantaine)):
            raise Refus("journal ou quarantaine déjà présents : on n'écrase jamais")
        passe = Passe(c, piece, os.environ, transport_reel, o.quarantaine, o.journal)
        if not o.reel:
            print(json.dumps({"a_blanc": "conforme", "pires": {p["id"]: [usd(pire(m, len(piece))) for m in p["chaine"]]
                                                               for p in c["proposeurs"]}}, ensure_ascii=False))
            return 0
        g = GD.executer(GD.lire_plan(o.plan_garde), os.environ, GD.transport_reel, o.journal + ".garde-depart.jsonl")
        if not g["tout_pret"]:
            raise Refus("G4 : garde de départ : " + json.dumps(g["par_cle"], ensure_ascii=False))
        os.makedirs(o.quarantaine, exist_ok=True)
        rapport = passe.courir()
    except Refus as e:
        print("REFUS :", e, file=sys.stderr)
        return 2
    print(json.dumps(rapport, ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main())
