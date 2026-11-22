"""Véhicule NA-1, lot 11 — exécutant de la passe X — v4.

v4 (remplace `passe_x_na_v3.py`, archivé sans changement) : forme de la réponse 36 de Fable (C.3, B.3, B.4), décidée
par la mère à 12:46Z, écart à X-2 accordé. Neuf modèles ; trois groupes thématiques de six pièces, avec un préambule
fixe ; une unité par (modèle, groupe). Le groupe 1 part d'abord pour les neuf modèles ; une barrière lit les issues ;
les groupes 2 et 3 partent si sept modèles au moins sont sans défaut de réglage. Après chaque réponse rendue, la garde
de coupure (cinq contrôles de B.4, par programme, sans rien afficher) ; un défaut ouvre une seule relance par unité,
selon la cause : transport (la même requête), réflexion épuisée (un cran d'effort en moins), texte coupé ou couverture
incomplète (le groupe scindé en deux moitiés de trois). Second défaut : « sans réponse ». P_X = 199,65 USD (33
tentatives au pire de 6,05).

v3 (remplace `passe_x_na_v2.py`, archivé sans changement ; vérification de la v2 « Conforme avec réserves ») :
pièce fusionnée v2 à dix-huit pièces (13928f87…, GO-2026-11-22-57) et ses trois morceaux de six pièces ; neuvième
proposeur Neon (GO-2026-11-22-33, accordé par la mère) ; deux formes accordables, écrites dans la configuration :
« sans découpe » (P_X = 102,85) ou « découpe Google » (chaque espèce Google reçoit les trois morceaux, une tentative
chacun ; P_X = 139,15). Les envois de la garde de départ et de l'essai de réglages ne suivent plus de redirection
(réserve de la vérification v2). Rien d'autre ne change.

v2 (remplace `passe_x_na_v1.py`, archivé sans changement) : porte la vérification `lot-11-passe-x-v1/verification-v1/`
(« À corriger ») : B1 (la garde de départ couvre chaque couple clé et modèle de la configuration), B2 (flux coupé ou en
erreur sous un statut 200 : coût au pire), B3 (raison d'arrêt et modèle servi en liste fermée au journal), B4 (toute
exception de transport classée « injoignable », ligne et compagnon toujours écrits), R1 (crédit lu sur le corps brut,
sans le garder), R2 (suffixe du modèle servi : date ou numéro seulement), R3 (ligne « envoi » avant l'envoi, P6), R4
(quarantaine neuve hors des dépôts ; journal de la garde absent), R5 (réservation à 6,05 par tentative, P4 « jamais
baissé » ; coût déclaré brut gardé), R6 (arrêt n° 13 relu sous le verrou), R7 (aucune redirection suivie), R8 (usage de
Kimi lu aux deux emplacements). Ajout : G4b, l'essai de réglages, qui retient pour chaque modèle le plus haut niveau
d'effort admis, par ordre décroissant, sur une requête de quelques jetons (consigne de la mère, effort maximal partout
où le modèle l'admet).

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
      ≤ sous-part de la clé, sinon refus nommé, sans bascule ; et somme ≤ P_X de la forme (102,85 ou 139,15) ;
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

VERSION = "passe-x-na-v4"
EMPREINTES_TEXTES = {
    "groupe-1": "b824df08208fcc53636fb6c71d23a89f47f2e98525f496341a5496df5692e531",
    "groupe-1-moitie-a": "f503f550c61188e918f2c72412c7b72923065085b5418155863261717f8d914c",
    "groupe-1-moitie-b": "d44033469620fc89534e3abcbd07927d90ca5f61a2e3284ac79e4c4a31adf654",
    "groupe-2": "fc9bed7ffdadca5f2a8d288d2cacece0953c8e8f95671b7ddc3f8cf36ab153c9",
    "groupe-2-moitie-a": "f179039e77d45b620a141b5ac9fac1b533bd69fea14d2b9f5b61baff53e32106",
    "groupe-2-moitie-b": "8ca599c1366291b13757838124cbec7f62355b7261321aedd668e4176a81fcac",
    "groupe-3": "61fceb5ecf19d5b86d08bd213416ac66b327f3f98d7e113cebed3d1889bb4289",
    "groupe-3-moitie-a": "6e07440af900dbb44c96e5d0f0b7a78b2ed262db7a3b3746aca6ddc4b485c770",
    "groupe-3-moitie-b": "9b96216aab49c15e2e99250c657af3572007f4d22a8bca47d4bd913e9a2e7e49",
}
RANGS_TEXTES = {
    "groupe-1": (1, 2, 3, 9, 15, 18),
    "groupe-1-moitie-a": (1, 2, 3),
    "groupe-1-moitie-b": (9, 15, 18),
    "groupe-2": (4, 5, 6, 7, 8, 17),
    "groupe-2-moitie-a": (4, 5, 6),
    "groupe-2-moitie-b": (7, 8, 17),
    "groupe-3": (10, 11, 12, 13, 14, 16),
    "groupe-3-moitie-a": (10, 11, 12),
    "groupe-3-moitie-b": (13, 14, 16),
}
FICHIERS_TEXTES = {k: k + ".md" for k in EMPREINTES_TEXTES}
GROUPES = (1, 2, 3)
P_X = D("199.65")
MOTS_CIBLE = 600
FRACTION_MIN = D("0.4")
LIGNE_FINALE = "FIN DES RÉPONSES"
DEFAUTS_ADMIS_BARRIERE = 2  # sept modèles sur neuf
PIRE_TENTATIVE = D("6.05")
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
CLES_MAILLON = {"modele", "tarif_entree", "tarif_sortie", "sortie_max", "extras", "google", "efforts"}
CLASSES = ("réponse rendue", "refus du modèle (classifieur)", "réponse illisible", "défaut Google", "modèle substitué",
           "crédit épuisé", "erreur de requête", "injoignable", "refusée avant envoi (arrêt n° 12)",
           "non partie (arrêt n° 13)")
MOTIFS_CREDIT = re.compile(r"credit balance is too low|insufficient_quota|exceeded_current_quota|insufficient balance|"
                           r"billing|suspended|depleted|prepayment", re.I)
FINS = ("end_turn", "stop", "refusal", "max_tokens", "pause_turn", "tool_use", "stop_sequence", "length",
        "content_filter", "STOP", "MAX_TOKENS", "SAFETY", "RECITATION", "PROHIBITED_CONTENT", "BLOCKLIST", "SPII",
        "OTHER", "FINISH_REASON_UNSPECIFIED")
SUFFIXE_MODELE = r"-(\d{8}|\d{4}-\d{2}-\d{2}|v?\d{1,3})"
EFFORTS_PERMIS = {"anthropic": ("max", "xhigh", "high", "medium", "low"), "openai": ("xhigh", "high", "medium", "low")}
ESSAI_REGLAGES_SORTIE = 16
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
def verifier_piece(chemin: str, nom: str = "piece") -> bytes:
    b = open(chemin, "rb").read()
    if sha(b) != EMPREINTES_TEXTES[nom]:
        raise Refus(f"G1 : empreinte de « {nom} » différente de celle qui est scellée")
    for n, ligne in enumerate(b.decode("utf-8").split("\n"), 1):
        if garde_motifs_ligne(ligne):
            raise Refus(f"G1 : la garde de motifs mord à la ligne {n} de « {nom} »")
    return b


def lire_textes(dossier: str) -> dict:
    return {nom: verifier_piece(os.path.join(dossier, f), nom) for nom, f in FICHIERS_TEXTES.items()}


TITRE = re.compile(r"(?m)^[ \t#*_>]*Réponse[ \t]+(\d+)\b")


def mots(t: str) -> int:
    return len(re.findall(r"\w+", t))


def garde_coupure(texte: str, rangs: tuple, fin, sortie_jetons, sortie_max: int):
    """Cinq contrôles de B.4 (le 4e, modèle servi, est tenu par la classe). Rend (cause ou None, alertes, comptes) ;
    n'affiche ni ne rend aucun texte."""
    comptes = {"titres": 0, "dans_l_ordre": False, "sections_courtes": None, "ligne_finale": 0}
    if fin not in ("end_turn", "stop", "STOP"):
        return ("réflexion épuisée" if mots(texte or "") < FRACTION_MIN * MOTS_CIBLE * len(rangs) else "texte coupé"), [], comptes
    lignes = [l.strip(" \t*_#>") for l in (texte or "").strip().split("\n") if l.strip()]
    comptes["ligne_finale"] = sum(1 for l in lignes if l == LIGNE_FINALE)
    if not lignes or lignes[-1] != LIGNE_FINALE or comptes["ligne_finale"] != 1:
        return "texte coupé", [], comptes
    titres = [(int(m.group(1)), m.start(), m.end()) for m in TITRE.finditer(texte)]
    comptes["titres"] = len(titres)
    comptes["dans_l_ordre"] = [t[0] for t in titres] == list(rangs)
    if not comptes["dans_l_ordre"]:
        return "couverture incomplète", [], comptes
    fin_txt = texte.rfind(LIGNE_FINALE)
    longueurs = [mots(texte[t[2]:(titres[i + 1][1] if i + 1 < len(titres) else fin_txt)]) for i, t in enumerate(titres)]
    comptes["sections_courtes"] = sum(1 for n in longueurs if n < FRACTION_MIN * MOTS_CIBLE)
    if comptes["sections_courtes"]:
        return "couverture incomplète", [], comptes
    alertes = []
    if isinstance(sortie_jetons, int) and sortie_jetons > 0.9 * sortie_max:
        alertes.append("sortie au-delà de 90 % du plafond")
    tiers = max(1, len(longueurs) // 3)
    if sum(longueurs[-tiers:]) * 2 < sum(longueurs[:tiers]):
        alertes.append("dernier tiers deux fois plus court que le premier")
    return None, alertes, comptes


def lire_configuration(chemin: str) -> dict:
    b = open(chemin, "rb").read()
    comp = chemin + ".sha256"
    if not os.path.exists(comp) or open(comp).read().split()[0] != sha(b):
        raise Refus("G2 : configuration sans compagnon, ou empreinte différente")
    c = json.loads(b)
    if set(c) != {"version", "forme", "proposeurs", "sous_parts"} or c["version"] != VERSION \
            or c["forme"] != "groupes_theme":
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
            if "efforts" in m:
                ef = m["efforts"]
                if p["fournisseur"] not in EFFORTS_PERMIS or not ef or not set(ef) <= set(EFFORTS_PERMIS[p["fournisseur"]]) \
                        or list(ef) != sorted(ef, key=EFFORTS_PERMIS[p["fournisseur"]].index):
                    raise Refus("G4b : niveaux d'effort hors liste ou hors de l'ordre décroissant")
                if "reasoning_effort" in m.get("extras", {}) or "effort" in m.get("extras", {}).get("output_config", {}):
                    raise Refus("G4b : effort à la fois fixé et à essayer")
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
            r["credit"] = r["credit"] or bool(MOTIFS_CREDIT.search(r["erreur"] + " " + str(err.get("message", ""))))
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
                if isinstance(ch.get("usage"), dict):  # R8 : Kimi peut porter l'usage dans le choix
                    r["entree"], r["sortie"] = ch["usage"].get("prompt_tokens"), ch["usage"].get("completion_tokens")
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
    if not modele_conforme(m, servi):
        return "modèle substitué"
    return "réponse rendue"


def modele_conforme(m, servi) -> bool:
    return isinstance(servi, str) and (servi == m or re.fullmatch(re.escape(m) + SUFFIXE_MODELE, servi) is not None)


def cout(maillon: dict, r: dict, pire_t: D):
    e, s = r.get("entree"), r.get("sortie")
    if not isinstance(e, int) or not isinstance(s, int) or isinstance(e, bool) or isinstance(s, bool):
        return pire_t, True
    c = (D(e) * D(str(maillon["tarif_entree"])) + D(s) * D(str(maillon["tarif_sortie"]))) / D(10**6)
    return (c if s <= maillon["sortie_max"] else max(c, pire_t)), False  # R5 : coût déclaré brut, jamais borné


# ---------- transport réel (urllib : honore le mandataire du conteneur) ----------
class _SansRedirection(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, *a, **k):  # R7 : une redirection renverrait la clé ailleurs
        raise urllib.error.URLError("redirection refusée")


_OUVREUR = urllib.request.build_opener(_SansRedirection)

def transport_reel(url: str, ent: dict, corps: bytes, brut):
    """Rend (statut, générateur d'objets JSON). Écrit chaque octet reçu dans `brut` (quarantaine)."""
    req = urllib.request.Request(url, data=corps, headers=ent, method="POST")
    try:
        rep = _OUVREUR.open(req, timeout=DELAI_SILENCE_S)
    except urllib.error.HTTPError as e:
        b = e.read()
        brut.write(b)
        texte = b.decode("utf-8", "replace")
        try:
            d = json.loads(b)
        except ValueError:
            d = None
        err = d.get("error") if isinstance(d, dict) else None
        typ = " ".join(str(err.get(k, "")) for k in ("type", "code", "status")).strip() if isinstance(err, dict) else ""
        # R1 : le corps brut sert au seul constat « crédit » ; il n'est gardé qu'en quarantaine
        return e.code, iter([{"error": {"type": typ or "erreur", "message": texte[:8000]}}])

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
    def __init__(self, config, textes: dict, environ, transport, quarantaine: str, journal: str):
        self.c, self.textes, self.env, self.transport = config, textes, environ, transport
        self.p_x = P_X
        self.unites = []
        self.q, self.journal = quarantaine, journal
        self.verrou = threading.Lock()
        self.cumul = {k: D(0) for k in config["sous_parts"]}
        self.en_vol = {k: D(0) for k in config["sous_parts"]}
        self.arret_13 = threading.Event()
        self.lignes = []
        for p in config["proposeurs"]:
            for nom_t, b in textes.items():
                for m in p["chaine"]:
                    if pire(m, len(b)) > PIRE_TENTATIVE:
                        raise Refus(f"G5 : pire d'une tentative de {p['id']} au-delà de 6,05")
                    if p["fournisseur"] == "google":
                        verifier_google(m, corps_requete("google", m, b.decode("utf-8")))
            if not (environ.get(p["cle_var"]) or "").strip():
                raise Refus(f"G11 : clé {p['cle_var']} absente")

    def _ecrire(self, ligne: dict):
        with self.verrou:
            self.lignes.append(ligne)
            with open(self.journal, "a", encoding="utf-8") as f:
                f.write(json.dumps(ligne, ensure_ascii=False, sort_keys=True) + "\n")

    def _reserver(self, cle: str, p_t: D) -> str:
        with self.verrou:
            if self.arret_13.is_set():  # R6 : relu sous le verrou
                return "13"
            total = sum(self.cumul.values()) + sum(self.en_vol.values())
            if self.cumul[cle] + self.en_vol[cle] + p_t > D(str(self.c["sous_parts"][cle])) or total + p_t > self.p_x:
                return "12"
            self.en_vol[cle] += p_t
            return "ok"

    def tentative(self, p: dict, rang: int, maillon: dict, nom_texte: str = "groupe-1", relance: str = None):
        cle, f = p["cle_var"], p["fournisseur"]
        p_t = PIRE_TENTATIVE  # R5, P4 : chaque tentative est réservée et comptée au pire de 6,05, jamais baissé
        piece = self.textes[nom_texte]
        base = {"version": VERSION, "proposeur": p["id"], "fournisseur": f, "cle_var": cle, "rang_repli": rang,
                "texte_servi": nom_texte, "texte_sha256": EMPREINTES_TEXTES[nom_texte], "relance": relance,
                "par_repli": rang > 0, "modele_demande": maillon["modele"], "pire_usd": usd(p_t), "heure": heure()}
        base["pire_calcule_usd"] = usd(pire(maillon, len(piece)))
        etat = self._reserver(cle, p_t)
        if etat != "ok":
            base.update(type_ligne="tentative", cout_usd="0.000000",
                        classe="non partie (arrêt n° 13)" if etat == "13" else "refusée avant envoi (arrêt n° 12)")
            self._ecrire(base)
            return base["classe"], None
        nom = f"{p['id']}-{nom_texte}-rang-{rang}-{maillon['modele']}" + (f"-relance-{relance}" if relance else "") + ".flux"
        nom = re.sub(r"[^A-Za-z0-9._-]", "_", nom)
        chemin = os.path.join(self.q, nom)
        corps = json.dumps(corps_requete(f, maillon, piece.decode("utf-8"))).encode()
        url = HOTES[f].format(modele=maillon["modele"])
        self._ecrire(dict(base, type_ligne="envoi", requete_sha256=sha(corps), reglages=reglages_journal(f, maillon)))
        r, c, inconnu, statut, classe = None, p_t, True, None, "injoignable"
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
                    elif r["erreur"] or r["fin"] is None:
                        c, inconnu = p_t, True  # B2 : flux en erreur ou sans fin : coût au pire
                    else:
                        c, inconnu = cout(maillon, r, p_t)
                except Exception as e:  # B4 : toute exception de transport ; la ligne et le compagnon suivent toujours
                    classe, base["exception"], c, inconnu = "injoignable", type(e).__name__, p_t, True
        finally:
            with self.verrou:
                self.en_vol[cle] -= p_t
                self.cumul[cle] += c
        if classe == "crédit épuisé":
            self.arret_13.set()
        b = open(chemin, "rb").read()
        with open(chemin + ".sha256", "x") as fc:
            fc.write(f"{sha(b)}  {nom}\n")
        fin, servi = (r or {}).get("fin"), (r or {}).get("modele")
        base.update(type_ligne="tentative", classe=classe, http=statut, cout_usd=usd(c), cout_inconnu=inconnu,
                    flux_sha256=sha(b), flux_octets=len(b),
                    fin=fin if fin in FINS else ("absente" if fin is None else "autre"),
                    modele_servi=servi if modele_conforme(maillon["modele"], servi) else
                    ("absent" if servi is None else "autre"),
                    entree_jetons=(r or {}).get("entree"), sortie_jetons=(r or {}).get("sortie"),
                    texte_signes=len((r or {}).get("texte") or ""), heure_fin=heure())
        self._ecrire(base)
        return classe, r

    def chaine(self, p: dict, nom_texte: str = "groupe-1"):
        """Chaîne de repli (G9) sur un texte ; rend (classe, r, maillon servi, rang)."""
        for rang, m in enumerate(p["chaine"]):
            classe, r = self.tentative(p, rang, m, nom_texte)
            if classe != "refus du modèle (classifieur)":
                return classe, r, m, rang
        return classe, r, m, rang

    def _juger(self, p, nom_texte, classe, r, maillon):
        """Rend (issue, cause) : issue ∈ {« rendue », « défaut », « fermée »} ; cause de la relance éventuelle."""
        if classe == "réponse rendue":
            cause, alertes, comptes = garde_coupure(r["texte"], RANGS_TEXTES[nom_texte], r["fin"], r.get("sortie"),
                                                    maillon["sortie_max"])
            self._ecrire({"type_ligne": "garde de coupure", "proposeur": p["id"], "texte_servi": nom_texte,
                          "cause": cause, "alertes": alertes, "comptes": comptes, "heure": heure()})
            return ("rendue", None) if cause is None else ("défaut", cause)
        if classe == "injoignable":
            return "défaut", "transport"
        if classe == "réponse illisible" and r and r.get("fin") in ("max_tokens", "length"):
            return "défaut", "réflexion épuisée" if mots(r.get("texte") or "") < FRACTION_MIN * MOTS_CIBLE * \
                len(RANGS_TEXTES[nom_texte]) else "texte coupé"
        if classe == "défaut Google" and r and r.get("fin") == "MAX_TOKENS":
            return "défaut", "texte coupé"
        return "fermée", None

    def unite(self, p: dict, g: int):
        nom_texte = f"groupe-{g}"
        classe, r, maillon, rang = self.chaine(p, nom_texte)
        issue, cause = self._juger(p, nom_texte, classe, r, maillon)
        bilan = {"type_ligne": "unité", "proposeur": p["id"], "groupe": g, "classe": classe, "issue": issue,
                 "cause": cause, "relance": None, "heure": heure()}
        if issue == "défaut" and not self.arret_13.is_set():
            bilan["relance"] = cause
            if cause in ("texte coupé", "couverture incomplète"):
                issues = []
                for moitie in ("a", "b"):
                    t = f"{nom_texte}-moitie-{moitie}"
                    c2, r2 = self.tentative(p, rang, maillon, t, relance="moitié " + moitie)
                    issues.append(self._juger(p, t, c2, r2, maillon)[0])
                bilan["issue_relance"] = "rendue" if all(x == "rendue" for x in issues) else "sans réponse"
                bilan["moities"] = issues
            else:
                m2 = maillon
                if cause == "réflexion épuisée":
                    m2 = cran_en_moins(p["fournisseur"], maillon)
                c2, r2 = self.tentative(p, rang, m2, nom_texte, relance=cause)
                i2 = self._juger(p, nom_texte, c2, r2, m2)[0]
                bilan["issue_relance"] = "rendue" if i2 == "rendue" else "sans réponse"
        self._ecrire(bilan)
        self.unites.append(bilan)
        return bilan

    def _phase(self, groupes, en_parallele):
        travaux = [(p, g) for g in groupes for p in self.c["proposeurs"]]
        if en_parallele:
            fils = [threading.Thread(target=self.unite, args=t) for t in travaux]
            for t in fils:
                t.start()
            for t in fils:
                t.join()
        else:
            for t in travaux:
                self.unite(*t)

    def barriere(self) -> bool:
        """Après le groupe 1 : au plus deux modèles en défaut de réglage (erreur de requête, modèle substitué), soit sept
        sur neuf."""
        mauvais = {u["proposeur"] for u in self.unites if u["groupe"] == 1
                   and u["classe"] in ("erreur de requête", "modèle substitué")}
        bons = len(self.c["proposeurs"]) - len(mauvais)
        ok = len(mauvais) <= DEFAUTS_ADMIS_BARRIERE and not self.arret_13.is_set()
        self._ecrire({"type_ligne": "barrière", "modeles_sans_defaut_de_reglage": bons, "passe": ok, "heure": heure()})
        return ok

    def courir(self, en_parallele=True):
        self._phase((1,), en_parallele)
        if self.barriere():
            self._phase((2, 3), en_parallele)
        par_cle = {k: usd(v) for k, v in self.cumul.items()}
        return {"version": VERSION, "par_cle_usd": par_cle, "total_usd": usd(sum(self.cumul.values())),
                "arret_13": self.arret_13.is_set(),
                "classes": {p["id"]: [l["classe"] for l in self.lignes
                                      if l.get("proposeur") == p["id"] and l.get("type_ligne") == "tentative"]
                            for p in self.c["proposeurs"]},
                "unites": {f"{u['proposeur']}/groupe-{u['groupe']}": u.get("issue_relance") or u["issue"]
                           for u in self.unites}}


def cran_en_moins(f: str, maillon: dict) -> dict:
    """Un cran d'effort en moins (relance « réflexion épuisée ») ; sans effort réglable, le même maillon."""
    m = json.loads(json.dumps(maillon))
    ex = m.setdefault("extras", {})
    if f == "anthropic" and (ex.get("output_config") or {}).get("effort") in EFFORTS_PERMIS["anthropic"][:-1]:
        niv = EFFORTS_PERMIS["anthropic"]
        ex["output_config"]["effort"] = niv[niv.index(ex["output_config"]["effort"]) + 1]
    elif f == "openai" and ex.get("reasoning_effort") in EFFORTS_PERMIS["openai"][:-1]:
        niv = EFFORTS_PERMIS["openai"]
        ex["reasoning_effort"] = niv[niv.index(ex["reasoning_effort"]) + 1]
    return m


def reglages_journal(f: str, maillon: dict) -> dict:
    """Réglages non textuels tels qu'ils partent (A7), pour le journal : aucun texte."""
    d = {"sortie_max": maillon["sortie_max"]}
    ex = maillon.get("extras", {})
    if f == "anthropic":
        d["effort"] = (ex.get("output_config") or {}).get("effort")
        d["thinking"] = (ex.get("thinking") or {}).get("type")
    elif f == "openai":
        d["effort"] = ex.get("reasoning_effort")
    elif f == "google":
        d["niveau"], d["provision"] = maillon["google"]["niveau"], maillon["google"]["provision"]
    return d


def couples_de_la_configuration(c: dict) -> set:
    return {(p["cle_var"], m["modele"]) for p in c["proposeurs"] for m in p["chaine"]}


def verifier_garde_couvre(c: dict, plan: list, rendu: dict):
    """B1 : chaque couple (clé, modèle) des chaînes est au plan, et rendu « prêt »."""
    au_plan = {(x["cle_var"], x["modele"]) for x in plan}
    manque = couples_de_la_configuration(c) - au_plan
    if manque:
        raise Refus("G4 : couple non éprouvé par la garde de départ : " + ", ".join(sorted(f"{k}/{m}" for k, m in manque)))
    for l in rendu["lignes"]:
        if (l["cle_var"], l["modele"]) in couples_de_la_configuration(c) and l["verdict"] != "prêt":
            raise Refus(f"G4 : {l['cle_var']}/{l['modele']} : {l['raison']}")


def corps_essai_reglages(f: str, maillon: dict, effort: str) -> dict:
    msg = [{"role": "user", "content": GD.INVITE}]
    if f == "anthropic":
        ex = dict(maillon.get("extras", {}))
        ex["output_config"] = dict(ex.get("output_config", {}), effort=effort)
        return dict({"model": maillon["modele"], "max_tokens": ESSAI_REGLAGES_SORTIE, "messages": msg}, **ex)
    return {"model": maillon["modele"], "max_completion_tokens": ESSAI_REGLAGES_SORTIE, "messages": msg,
            "reasoning_effort": effort}


def essayer_reglages(c: dict, environ, transport, journal: str) -> dict:
    """G4b : pour chaque maillon qui porte `efforts`, essaie les niveaux dans l'ordre décroissant, sur quelques jetons ;
    retient le premier rendu 200 ; un 400 passe au niveau suivant ; tout autre statut, ou aucun niveau admis, refuse.
    Rend la configuration réglée (copie). Coût : quelques jetons par essai, journalisé, sans aucun texte."""
    if os.path.exists(journal):
        raise Refus("G4b : journal de l'essai de réglages déjà présent")
    c = json.loads(json.dumps(c))
    with open(journal, "x", encoding="utf-8") as fj:
        for p in c["proposeurs"]:
            f = p["fournisseur"]
            for m in p["chaine"]:
                if "efforts" not in m:
                    continue
                retenu = None
                for e in m["efforts"]:
                    corps = json.dumps(corps_essai_reglages(f, m, e)).encode()
                    url = HOTES[f].split("{")[0] if f != "google" else None
                    try:
                        statut, octets = transport(url, entetes(f, environ[p["cle_var"]]), corps)
                    except Exception as x:
                        raise Refus(f"G4b : {p['id']}/{m['modele']} : essai injoignable ({type(x).__name__})")
                    fj.write(json.dumps({"heure": heure(), "proposeur": p["id"], "cle_var": p["cle_var"],
                                         "modele": m["modele"], "effort": e, "http": statut}, ensure_ascii=False) + "\n")
                    if statut == 200:
                        retenu = e
                        break
                    if statut != 400:
                        raise Refus(f"G4b : {p['id']}/{m['modele']} : statut {statut} à l'essai de réglages")
                if retenu is None:
                    raise Refus(f"G4b : {p['id']}/{m['modele']} : aucun niveau d'effort admis")
                ex = m.setdefault("extras", {})
                if f == "anthropic":
                    ex["output_config"] = dict(ex.get("output_config", {}), effort=retenu)
                else:
                    ex["reasoning_effort"] = retenu
                del m["efforts"]
    return c


def transport_simple(url: str, entetes_: dict, corps: bytes, delai: float = 60.0):
    """Envoi sans flux, sans redirection (garde de départ et essai de réglages) ; rend (statut, octets)."""
    req = urllib.request.Request(url, data=corps, headers=entetes_, method="POST")
    try:
        with _OUVREUR.open(req, timeout=delai) as rep:
            return rep.status, rep.read()
    except urllib.error.HTTPError as e:
        return e.code, e.read()


def hors_des_depots(chemin: str) -> bool:
    r = os.path.realpath(chemin)
    return not any(r == d or r.startswith(d + os.sep) for d in (os.path.realpath(RACINE), "/home/user/main-lecture"))


def main(argv=None) -> int:
    a = argparse.ArgumentParser(description="Exécutant de la passe X, v2")
    a.add_argument("--textes", required=True, help="dossier des neuf textes scellés des groupes")
    a.add_argument("--configuration", required=True)
    a.add_argument("--plan-garde", required=True)
    a.add_argument("--quarantaine", required=True)
    a.add_argument("--journal", required=True)
    a.add_argument("--registre-go", default="/home/user/main-lecture/registres/go.md")
    a.add_argument("--reel", action="store_true")
    o = a.parse_args(argv)
    garde_j, reglages_j = o.journal + ".garde-depart.jsonl", o.journal + ".essai-reglages.jsonl"
    try:
        textes = lire_textes(o.textes)
        c = lire_configuration(o.configuration)
        verifier_go(o.registre_go)
        plan = GD.lire_plan(o.plan_garde)
        if couples_de_la_configuration(c) - {(x["cle_var"], x["modele"]) for x in plan}:
            verifier_garde_couvre(c, plan, {"lignes": []})
        for j in (o.journal, garde_j, reglages_j):
            if os.path.exists(j):
                raise Refus("journal déjà présent : on n'écrase jamais (" + os.path.basename(j) + ")")
        if os.path.exists(o.quarantaine) or not hors_des_depots(o.quarantaine):
            raise Refus("R4 : la quarantaine doit être un dossier neuf, hors des dépôts")
        Passe(c, textes, os.environ, transport_reel, o.quarantaine, o.journal)  # contrôles G5, G6, G11 à blanc
        if not o.reel:
            print(json.dumps({"a_blanc": "conforme", "forme": c["forme"], "p_x": str(P_X),
                              "pires": {p["id"]: [usd(max(pire(m, len(b)) for b in textes.values())) for m in p["chaine"]]
                                        for p in c["proposeurs"]}}, ensure_ascii=False))
            return 0
        g = GD.executer(plan, os.environ, transport_simple, garde_j)
        verifier_garde_couvre(c, plan, g)
        c = essayer_reglages(c, os.environ, transport_simple, reglages_j)
        os.makedirs(o.quarantaine)
        passe = Passe(c, textes, os.environ, transport_reel, o.quarantaine, o.journal)
        passe._ecrire({"type_ligne": "ouverture", "version": VERSION, "heure": heure(),
                       "ecart_google": "sortie 65 536 jetons, dont 49 152 de réflexion comptée, sous la garde v3 ; "
                                       "écart accordé par la mère le 2026-11-22 (message de 12:31Z), aucun chiffre changé",
                       "go": list(GO_EXIGES), "textes_sha256": EMPREINTES_TEXTES, "forme": c["forme"],
                       "p_x": str(P_X),
                       "ecarts": ["Neon en neuvième proposeur (GO-2026-11-22-33)", "18e pièce (GO-2026-11-22-57)",
                                  "groupes thématiques, préambule et garde de coupure (réponse 36 de Fable, écart à X-2 "
                                  "accordé par la mère à 12:46Z)"],
                       "configuration_sha256": sha(open(o.configuration, "rb").read())})
        rapport = passe.courir()
    except Refus as e:
        print("REFUS :", e, file=sys.stderr)
        return 2
    print(json.dumps(rapport, ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main())
