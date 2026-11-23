#!/usr/bin/env python3
"""Commande externe Gemini **en flux, sous la garde des appels à Google** pour l'orchestrateur du pôle — version 2.

Version 2 (R12 ; la v1, `scripts/commande_gemini_flux_v1.py`, `6aaf235d…`, reste en place). Seul changement, sur le constat 12
de la contre-lecture du lanceur v11b (`contre-lecture-lanceur-v11b-v1.md`, `cd7e5455…`) : le pire cas avant l'envoi suppose
la réflexion **comprise** dans `maxOutputTokens` (page de Google versée sur `main`, `fe0b8d88…`, l. 914-916 et 1273-1274) ;
après la réponse, la commande vérifie cette hypothèse sur l'usage lu : `candidatesTokenCount + thoughtsTokenCount ≤
maxOutputTokens`. Le champ `hypothese_sortie_maximale_tenue` (vrai, faux, ou null si l'usage est illisible) est écrit dans
chaque ligne rendue après un envoi ; s'il est faux, la commande le signale sur sa sortie d'erreur (ligne
`commande-gemini-flux-v2 : HYPOTHESE_SORTIE_MAXIMALE_TOMBEE …`, journalisée avec la ligne rendue), sans changer le code : le
coût lu est compté tel quel et reste gardé par le plafond de session (code 7 au-delà). Texte de la v1 ci-dessous.

Commande externe Gemini en flux, sous la garde des appels à Google — version 1.

Écrite le 22 novembre 2026 (pièce de classe B, à contre-lire) pour le lanceur v11 de la course d'affinage des idées des
mentors, sur l'ordre de la mère : « Carbon par le relais en flux, sous la garde Google ». **Aucune clé ici** : elle parle au
relais Gemini v3 local (`docs/notes/ideation-organisme-v1/argon-recherche-v1/relais_gemini_v3.py` de `main`, `2cf6bc6d…`,
port d'usage 8791), qui tient la clé, la liste blanche des modèles, lit l'amont **en flux** (`streamGenerateContent`) et rend
une réponse `generateContent` entière (parties de pensée retirées, `usageMetadata` relayé tel quel).

Règle gelée de `CLAUDE.md`, « Appels aux modèles de Google » (GO-2026-11-21-71) : la commande **emploie la garde commune**
`src/controle_ia/garde_google_v3.py` (chemin passé par `--garde`, empreinte vérifiée contre `EMPREINTE_GARDE`, sinon code 2,
rien envoyé) :
- avant l'envoi, `verifier_reglages_google(espèce, corps, provision, mots, mode="flux")` sur le corps exact qui part ; un
  problème : code 2, rien envoyé ;
- après la réponse, `defaut_reponse_google(finishReason, texte, thoughtsTokenCount, blocage)` : zéro jeton de pensée (ou champ
  absent), fin MAX_TOKENS, SAFETY, RECITATION…, texte vide, invite bloquée : **défaut**, code 5, jamais une réponse ; le défaut
  est écrit dans la ligne rendue (`defaut_google`), que l'orchestrateur journalise.

Contrat (celui de `commande_gemini_lot_v1.py` pour `AdaptateurCommandeExterne`) : consigne sur l'entrée standard (UTF-8) ;
environnement minimal du noyau : `PLAFOND_SESSION_USD`, `ROLE_POLE` (dans `--roles`), `MODELE_DEMANDE_POLE` (s'il est posé,
égal à `--modele`) ; **la dernière ligne de la sortie standard est toujours un objet JSON** `{"texte", "cout_usd", …}`.

Déroulé :
1. compte de l'entrée par `countTokens` (gratuit, par le relais) ; entrée gardée = ⌈max(compte, caractères / 3) × 1,05⌉ ;
2. corps : `generationConfig` = {`maxOutputTokens`: `--max-sortie-jetons` (**jamais abaissé** : refus plutôt que
   troncature), `thinkingConfig`: {`thinkingLevel`: `--niveau-reflexion`, `includeThoughts`: vrai}} ; la sortie maximale
   compte la pensée (documentation du fournisseur) ;
3. garde avant envoi : réglages (garde commune) ; pire cas = entrée gardée × prix d'entrée + `maxOutputTokens` × prix de
   sortie ≤ plafond de session, sinon code 4, rien envoyé ;
4. `POST …:generateContent` au relais (qui lit l'amont en flux), délai `--delai-s` ;
5. lecture : modèle servi égal au modèle demandé (ou suffixé d'une date), sinon code 5 ; garde après réponse ; appel de
   fonction ou code refusés ; coût = entrée × prix d'entrée + (sortie + pensée) × prix de sortie ; coût lu au-delà du
   plafond de session : code 7 (garde du plafond compromise).
Coût rendu sur un échec : 1e-6 si rien n'est parti ; pire cas dès que la requête de génération est partie, sauf usage lu.

Codes : 0 conforme ; 2 réglage, garde ou entrée refusés (rien envoyé) ; 3 relais ou amont en échec ; 4 pire cas au-dessus du
plafond (rien envoyé) ; 5 réponse non conforme ou défaut Google ; 7 coût lu au-delà du plafond de session.
Bibliothèque standard seulement. Essais : `tests/test_commande_gemini_flux_v1.py`.
"""
import argparse
import hashlib
import importlib.util
import json
import math
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request

VERSION = "commande-gemini-flux-v2"
CLE_FACTICE = "factice-relais"
EMPREINTE_GARDE = "923679b51cfc84b65ff7cfc65296378d08e6d4e64f6b427823d23ba24f4afe91"  # garde_google_v3.py (main)
TEXTE_MIN_JETONS = 16000
CARACTERES_PAR_JETON = 3.0
MARGE_ENTREE = 0.05
HOTES_LOCAUX = ("127.0.0.1", "localhost", "::1")
PARTIES_INTERDITES = ("functionCall", "functionResponse", "executableCode", "codeExecutionResult")


class Erreur(Exception):
    def __init__(self, code, motif, **extra):
        super().__init__(motif)
        self.code, self.motif, self.extra = code, motif, extra


def analyseur():
    a = argparse.ArgumentParser(prog="commande_gemini_flux_v1")
    a.add_argument("--espece", required=True, help="espèce pour la garde (carbon, argon, neon)")
    a.add_argument("--modele", required=True)
    a.add_argument("--url-base", default="http://127.0.0.1:8791/v1beta")
    a.add_argument("--prix-entree", type=float, required=True, help="USD par million de jetons d'entrée")
    a.add_argument("--prix-sortie", type=float, required=True, help="USD par million de jetons de sortie (pensée comprise)")
    a.add_argument("--niveau-reflexion", required=True)
    a.add_argument("--provision-pensee-jetons", type=int, required=True)
    a.add_argument("--max-sortie-jetons", type=int, required=True)
    a.add_argument("--mots-invite", type=int, default=None, help="limite de mots demandée par l'invite, si elle en donne une")
    a.add_argument("--delai-s", type=float, default=1500.0)
    a.add_argument("--delai-requete-s", type=float, default=60.0, help="délai du compte de jetons")
    a.add_argument("--roles", default="proposeur_ideation")
    a.add_argument("--garde", required=True, help="chemin de src/controle_ia/garde_google_v3.py")
    return a


def charger_garde(chemin):
    try:
        octets = open(chemin, "rb").read()
    except OSError:
        raise Erreur(2, f"garde des appels à Google illisible : {chemin}") from None
    if hashlib.sha256(octets).hexdigest() != EMPREINTE_GARDE:
        raise Erreur(2, f"garde des appels à Google d'une autre empreinte que {EMPREINTE_GARDE[:12]}…")
    spec = importlib.util.spec_from_file_location("garde_google_pour_commande_flux_v1", chemin)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def modele_conforme(demande, servi):
    return isinstance(servi, str) and (servi == demande or re.fullmatch(re.escape(demande) + r"-\d{8}", servi) is not None)


def poster(ouvreur, url, corps, delai):
    req = urllib.request.Request(url, data=json.dumps(corps).encode("utf-8"), method="POST",
                                 headers={"x-goog-api-key": CLE_FACTICE, "Content-Type": "application/json"})
    with ouvreur.open(req, timeout=delai) as r:
        return json.loads(r.read() or b"{}")


def entier_positif(v):
    return isinstance(v, int) and not isinstance(v, bool) and v > 0


def executer(args, consigne, environ, ouvreur):
    etat = {"pire_cas": None, "envoye": False, "reglages": None, "hypothese": None, "sortie_lue": None}
    try:
        garde = charger_garde(args.garde)
        for nom, v in (("--prix-entree", args.prix_entree), ("--prix-sortie", args.prix_sortie), ("--delai-s", args.delai_s)):
            if not (math.isfinite(v) and v > 0):
                raise Erreur(2, f"{nom} : réel fini strictement positif exigé")
        if not (entier_positif(args.provision_pensee_jetons) and entier_positif(args.max_sortie_jetons)):
            raise Erreur(2, "--provision-pensee-jetons et --max-sortie-jetons : entiers > 0 exigés")
        p = urllib.parse.urlparse(args.url_base)
        if p.scheme != "http" or p.hostname not in HOTES_LOCAUX:
            raise Erreur(2, "--url-base : http vers la boucle locale seulement (le relais tient la clé)")
        roles = [x for x in args.roles.split(",") if x]
        if environ.get("ROLE_POLE") not in roles:
            raise Erreur(2, f"ROLE_POLE {environ.get('ROLE_POLE')!r} hors de {roles}")
        demande = environ.get("MODELE_DEMANDE_POLE")
        if demande and demande != args.modele:
            raise Erreur(2, f"MODELE_DEMANDE_POLE {demande!r} ≠ --modele {args.modele!r} : rien envoyé")
        try:
            plafond = float(environ.get("PLAFOND_SESSION_USD", ""))
            assert math.isfinite(plafond) and plafond > 0
        except (ValueError, AssertionError):
            raise Erreur(2, "PLAFOND_SESSION_USD absent ou invalide") from None
        if not consigne.strip():
            raise Erreur(2, "consigne vide")
        contenus = [{"role": "user", "parts": [{"text": consigne}]}]
        corps = {"contents": contenus, "generationConfig": {
            "maxOutputTokens": args.max_sortie_jetons,
            "thinkingConfig": {"thinkingLevel": args.niveau_reflexion, "includeThoughts": True}}}
        etat["reglages"] = {"niveau": args.niveau_reflexion, "provision": args.provision_pensee_jetons,
                            "maxOutputTokens": args.max_sortie_jetons, "mode": "flux"}
        problemes = garde.verifier_reglages_google(args.espece, corps, provision=args.provision_pensee_jetons,
                                                   mots=args.mots_invite, mode="flux", texte_min=TEXTE_MIN_JETONS)
        if problemes:
            raise Erreur(2, "garde des appels à Google : " + " ; ".join(problemes) + " : rien envoyé")
        base = args.url_base.rstrip("/")
        try:
            compte = poster(ouvreur, f"{base}/models/{args.modele}:countTokens", {"contents": contenus},
                            args.delai_requete_s).get("totalTokens")
        except (urllib.error.URLError, OSError, ValueError) as e:
            raise Erreur(3, f"countTokens : {type(e).__name__} : {e}"[:300]) from None
        if not entier_positif(compte):
            raise Erreur(5, f"countTokens : totalTokens invalide ({compte!r})")
        entree = math.ceil(max(compte, len(consigne) / CARACTERES_PAR_JETON) * (1 + MARGE_ENTREE))
        pe, ps = args.prix_entree / 1e6, args.prix_sortie / 1e6
        pire = entree * pe + args.max_sortie_jetons * ps
        if pire > plafond + 1e-12:
            raise Erreur(4, f"pire cas {pire:.6f} USD (entrée gardée {entree}, sortie {args.max_sortie_jetons} à {args.prix_sortie:g}) "
                            f"> plafond de session {plafond:g} USD : rien envoyé")
        etat["pire_cas"] = pire
        etat["envoye"] = True
        try:
            rep = poster(ouvreur, f"{base}/models/{args.modele}:generateContent", corps, args.delai_s)
        except urllib.error.HTTPError as e:
            raise Erreur(3, f"génération : HTTP {e.code} : " + e.read(300).decode("utf-8", "replace")) from None
        except (urllib.error.URLError, OSError, ValueError) as e:
            raise Erreur(3, f"génération : {type(e).__name__} : {e}"[:300]) from None
        servi = rep.get("modelVersion")
        usage = rep.get("usageMetadata") if isinstance(rep.get("usageMetadata"), dict) else None
        cout = None
        if usage is not None and isinstance(usage.get("promptTokenCount"), int):
            pensee = usage.get("thoughtsTokenCount")
            sortie = int(usage.get("candidatesTokenCount") or 0) + (pensee if isinstance(pensee, int) else 0)
            cout = int(usage["promptTokenCount"]) * pe + sortie * ps
            etat["sortie_lue"] = sortie
            etat["hypothese"] = sortie <= args.max_sortie_jetons  # v2, constat 12 : réflexion comprise dans la sortie maximale
        extra = {"usage": usage, "cout_reel": cout}
        if not modele_conforme(args.modele, servi):
            raise Erreur(5, f"modèle servi {servi!r} ≠ modèle demandé {args.modele!r}", **extra)
        extra["modele_servi"] = servi
        cands = rep.get("candidates") or []
        c = cands[0] if cands and isinstance(cands[0], dict) else {}
        parts = (c.get("content") or {}).get("parts") or []
        if any(isinstance(x, dict) and any(k in x for k in PARTIES_INTERDITES) for x in parts):
            raise Erreur(5, "appel de fonction ou code dans la réponse alors qu'aucun outil n'est déclaré", **extra)
        texte = "".join(x.get("text", "") for x in parts if isinstance(x, dict) and not x.get("thought"))
        blocage = (rep.get("promptFeedback") or {}).get("blockReason")
        defaut = garde.defaut_reponse_google(c.get("finishReason"), texte, (usage or {}).get("thoughtsTokenCount"), blocage=blocage)
        if defaut:
            raise Erreur(5, f"défaut Google : {defaut} (jamais une réponse)", defaut_google=defaut, **extra)
        if cout is None:
            raise Erreur(5, "usage absent de la réponse", **extra)
        if cout > plafond + 1e-9:
            raise Erreur(7, f"coût lu {cout:.6f} USD > plafond de session {plafond:g} USD : garde du plafond compromise", **extra)
        return 0, {"texte": texte, "cout_usd": max(cout, 1e-6), "modele_servi": servi, "modele_demande": args.modele,
                   "fin": c.get("finishReason"), "usage": usage, "version": VERSION, "reglages": etat["reglages"],
                   "pire_cas_usd": round(pire, 6), "prix": {"entree": args.prix_entree, "sortie": args.prix_sortie},
                   "defaut_google": None, "hypothese_sortie_maximale_tenue": etat["hypothese"]}
    except Exception as brute:  # noqa: BLE001 — toute exception donne une ligne au bon coût
        e = brute if isinstance(brute, Erreur) else Erreur(3, f"{type(brute).__name__} : {brute}"[:300])
        if etat["envoye"]:
            reel = e.extra.get("cout_reel")
            cout, origine = (reel, "usage") if isinstance(reel, float) else (etat["pire_cas"], "pire_cas")
        else:
            cout, origine = 1e-6, "plancher"
        ligne = {"texte": "", "cout_usd": max(cout or 1e-6, 1e-6), "cout_origine": origine, "erreur": f"{VERSION} : {e.motif}",
                 "modele_demande": args.modele, "version": VERSION, "reglages": etat["reglages"],
                 "defaut_google": e.extra.get("defaut_google")}
        if etat["envoye"]:
            ligne["hypothese_sortie_maximale_tenue"] = etat["hypothese"]
        if isinstance(e.extra.get("modele_servi"), str):
            ligne["modele_servi"] = e.extra["modele_servi"]
        if isinstance(e.extra.get("usage"), dict):
            ligne["usage"] = e.extra["usage"]
        return e.code, ligne


def principal(argv=None, environ=None, entree=None, ouvreur=None):
    environ = os.environ if environ is None else environ
    try:
        args = analyseur().parse_args(argv)
    except SystemExit:
        print(json.dumps({"texte": "", "cout_usd": 1e-6, "erreur": f"{VERSION} : arguments invalides"}))
        return 2
    try:
        consigne = (entree if entree is not None else sys.stdin.buffer.read()).decode("utf-8")
    except UnicodeDecodeError:
        print(json.dumps({"texte": "", "cout_usd": 1e-6, "erreur": f"{VERSION} : consigne non UTF-8"}))
        return 2
    ouvreur = ouvreur or urllib.request.build_opener(urllib.request.ProxyHandler({}))
    code, ligne = executer(args, consigne, environ, ouvreur)
    if ligne.get("hypothese_sortie_maximale_tenue") is False:  # v2 : signalé et journalisé, jamais tu
        u = ligne.get("usage") or {}
        print(f"{VERSION} : HYPOTHESE_SORTIE_MAXIMALE_TOMBEE : réflexion {u.get('thoughtsTokenCount')!r} + sortie "
              f"{u.get('candidatesTokenCount')!r} > maxOutputTokens {args.max_sortie_jetons} : le pire cas écrit avant l'envoi "
              "ne bornait pas cet appel", file=sys.stderr)
    if code != 0:
        print(f"{VERSION} : {ligne.get('erreur')}", file=sys.stderr)
    print(json.dumps(ligne, ensure_ascii=False))
    return code


if __name__ == "__main__":
    sys.exit(principal())
