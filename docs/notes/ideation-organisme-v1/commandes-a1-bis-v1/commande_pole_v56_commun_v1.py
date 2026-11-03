#!/usr/bin/env python3
"""Partie commune des commandes externes d'A1-bis (Claude, port 8806 ; Astra, port 8807), au contrat du pôle v56 — v1.

Écrit le 2 novembre 2026 par la session fille de session-depot, sur demande de la session mère (A1-bis, GO-2026-11-02-11 à -13,
rien de lancé). Le contrat est celui de `commande_argon_v56_nuit_v2.py` (221df610…), repris ici à l'identique dans sa
logique, rendu générique par fournisseur :

- `servir` : relais local (boucle locale seulement), clé dans le SEUL environnement du relais, jamais en argument ni en
  fichier ; `POST /appel` {modele, prompt, max_tokens, pire_cas_usd, reglages} ; `GET /relais/etat`. Second barrage : plafond
  propre (réserve au pire cas sous verrou), nombre d'appels borné, modèles permis, réglages du relais exigés à l'identique
  de ceux que la commande annonce (sinon refus 409, rien n'est envoyé). Journal JSON par ligne : jamais le texte, jamais la clé.
  Aucune reprise interne : un échec est rendu tel quel (l'orchestrateur décide).
- `appeler` : consigne sur l'entrée standard ; garde du pire cas sur PLAFOND_SESSION_USD ; garde cumulée du registre partagé
  (`registre_depense_cumulee_v1.py`, 8ba92066…) avec la porte « environnement » (ETAPE_POLE, PLAFOND_ETAPE_USD) ; ROLE_POLE
  permis ; MODELE_DEMANDE_POLE égal à --modele ; modèle demandé passé EXPLICITEMENT au relais ; modèle servi contrôlé
  (identifiant exact) ; dernière ligne JSON {texte, cout_usd > 0, modele_servi, …}.
- Le modèle n'est JAMAIS changé par la commande ni par le relais : pas de repli, pas de bascule ; un modèle servi différent
  est un refus (code 5).

Codes (`appeler`) : 0 conforme ; 2 réglage ou entrée refusés ; 3 relais ou interface (HTTP, connexion) ; 4 pire cas au-dessus
d'un plafond (session, étape, cumulé, relais) ou registre illisible ; 5 réponse non conforme (vide, tronquée, refus du modèle,
anomalie, modèle servi différent, coût au-dessus du pire cas réservé) ; 6 délai dépassé ou interruption.
"""

import datetime
import json
import math
import os
import signal
import sys
import threading
import time
import urllib.error
import urllib.parse
import urllib.request
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

ICI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ICI)
import registre_depense_cumulee_v1 as reg  # noqa: E402

ROLES = ("proposeur_ideation", "juge_ideation")
PLANCHER = 1e-6
HOTE = "127.0.0.1"
MAX_OCTETS_CORPS = 4_000_000


def maintenant():
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def pire_cas(caracteres, max_tokens, prix):
    """Formule du collisionneur (`cout_pire_cas`) : caractères / 3 à l'entrée, max_tokens à la sortie."""
    return caracteres / 3 / 1e6 * prix[0] + max_tokens / 1e6 * prix[1]


def cout_usage(prix, usage):
    return usage["entree"] / 1e6 * prix[0] + usage["sortie"] / 1e6 * prix[1]


# --- relais ----------------------------------------------------------------------------------------------------------------


class EtatRelais:
    def __init__(self, plafond, max_appels, modeles, journal, reglages, version):
        self.plafond, self.max_appels, self.modeles, self.journal = float(plafond), int(max_appels), set(modeles), journal
        self.reglages, self.version = dict(reglages), version
        self.depense, self.engage, self.appels, self.refus = 0.0, 0.0, 0, {}
        self.verrou = threading.Lock()

    def noter_refus(self, motif):
        with self.verrou:
            self.refus[motif] = self.refus.get(motif, 0) + 1

    def ecrire_journal(self, entree):
        if not self.journal:
            return
        with self.verrou, open(self.journal, "a", encoding="utf-8") as f:
            f.write(json.dumps(dict(entree, quand_utc=maintenant()), ensure_ascii=False, sort_keys=True) + "\n")


def fabriquer_gestion(etat, fournisseur):
    """`fournisseur` : objet avec .appeler(modele, prompt, max_tokens, reglages) -> Reponse, .prix(modele),
    .statut(rep), .masquer(texte), .cle_presente(), .nature."""
    class Gestion(BaseHTTPRequestHandler):
        server_version = etat.version

        def log_message(self, *a):
            pass

        def _json(self, code, objet):
            corps = json.dumps(objet, ensure_ascii=False).encode("utf-8")
            self.send_response(code)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(corps)))
            self.end_headers()
            self.wfile.write(corps)

        def do_GET(self):
            if self.path != "/relais/etat":
                return self._json(403, {"erreur": "chemin refusé"})
            with etat.verrou:
                d = {"version": etat.version, "pid": os.getpid(), "appels": etat.appels, "max_appels": etat.max_appels,
                     "depense_usd": round(etat.depense, 6), "engage_usd": round(etat.engage, 6), "plafond_usd": etat.plafond,
                     "restant_usd": round(etat.plafond - etat.depense - etat.engage, 6), "refus": dict(etat.refus),
                     "modeles_permis": sorted(etat.modeles), "reglages": etat.reglages,
                     "cle_presente": fournisseur.cle_presente(), "appelant": fournisseur.nature,
                     "reprise_interne": "aucune"}
            return self._json(200, d)

        def do_POST(self):
            if self.path != "/appel":
                return self._json(403, {"erreur": "chemin refusé"})
            longueur = self.headers.get("Content-Length")
            if longueur is None:
                return self._json(411, {"erreur": "Content-Length exigé"})
            if int(longueur) > MAX_OCTETS_CORPS:
                return self._json(413, {"erreur": "corps trop grand"})
            try:
                d = json.loads(self.rfile.read(int(longueur)))
                modele, prompt, mt, pire = d["modele"], d["prompt"], int(d["max_tokens"]), float(d["pire_cas_usd"])
                reglages = d.get("reglages") or {}
                if not (isinstance(prompt, str) and prompt.strip() and mt > 0 and math.isfinite(pire) and pire >= 0
                        and isinstance(reglages, dict)):
                    raise ValueError
            except (ValueError, KeyError, TypeError):
                etat.noter_refus("requete_illisible")
                return self._json(400, {"erreur": "requête illisible"})
            if modele not in etat.modeles:
                etat.noter_refus("modele_non_permis")
                return self._json(403, {"erreur": f"modèle {modele!r} non permis"})
            if reglages != etat.reglages:
                etat.noter_refus("reglages_differents")
                return self._json(409, {"erreur": f"réglages annoncés {reglages!r} ≠ réglages du relais {etat.reglages!r}"})
            pire_relais = max(pire, pire_cas(len(prompt), mt, fournisseur.prix(modele)))
            with etat.verrou:
                if etat.appels >= etat.max_appels:
                    etat.refus["max_appels"] = etat.refus.get("max_appels", 0) + 1
                    return self._json(429, {"erreur": "max-appels atteint (relais)"})
                if etat.depense + etat.engage + pire_relais > etat.plafond + 1e-9:
                    etat.refus["plafond"] = etat.refus.get("plafond", 0) + 1
                    return self._json(402, {"erreur": f"plafond du relais : {etat.depense:.4f} + engagé {etat.engage:.4f} + "
                                                      f"pire cas {pire_relais:.4f} > {etat.plafond:g} USD"})
                etat.appels += 1
                etat.engage += pire_relais
                numero = etat.appels
            t0 = time.time()
            try:
                rep = fournisseur.appeler(modele, prompt, mt, etat.reglages)
            except Exception as e:  # noqa: BLE001 — exception de l'appel : échec consigné, au pire cas
                rep = fournisseur.Reponse(echec=f"exception : {type(e).__name__} : {fournisseur.masquer(str(e))[:300]}")
            duree = round(time.time() - t0, 1)
            if rep.echec:
                statut, cout, origine = "ECHEC", pire_relais, "pire_cas"
            else:
                statut = fournisseur.statut(rep)
                u = rep.usage or {}
                if not isinstance(u.get("entree"), int) or u.get("entree", 0) <= 0 or not isinstance(u.get("sortie"), int):
                    cout, origine = pire_relais, "pire_cas"
                else:
                    cout, origine = cout_usage(fournisseur.prix(modele), u), "usage"
            with etat.verrou:
                etat.engage -= pire_relais
                etat.depense += cout
                cumul = etat.depense
            echec = fournisseur.masquer(rep.echec)[:300] if rep.echec else None
            etat.ecrire_journal({"appel": numero, "modele_demande": modele, "modele_servi": rep.modele_servi, "statut": statut,
                                 "fin": rep.fin, "usage": rep.usage, "cout_usd": round(cout, 6), "cout_origine": origine,
                                 "pire_cas_usd": round(pire_relais, 6), "max_tokens": mt, "caracteres": len(prompt),
                                 "reglages": etat.reglages, "duree_s": duree, "echec": echec,
                                 "depense_cumulee_usd": round(cumul, 6)})
            return self._json(200, {"texte": rep.texte or "", "modele_servi": rep.modele_servi, "fin": rep.fin,
                                    "categorie": rep.categorie, "statut": statut, "usage": rep.usage, "cout_usd": round(cout, 8),
                                    "cout_origine": origine, "pire_cas_relais_usd": round(pire_relais, 8),
                                    "reglages": etat.reglages, "echec": echec, "duree_s": duree})
    return Gestion


def servir(args, fournisseur, version, reglages):
    modeles = [m.strip() for m in args.modeles_permis.split(",") if m.strip()]
    if not modeles:
        raise SystemExit("--modeles-permis vide")
    etat = EtatRelais(args.plafond_usd, args.max_appels, modeles, args.journal, reglages, version)
    serveur = ThreadingHTTPServer((HOTE, args.port), fabriquer_gestion(etat, fournisseur))
    print(f"relais {version} prêt sur http://{HOTE}:{serveur.server_address[1]} (PID {os.getpid()}, plafond {etat.plafond:g} USD, "
          f"modèles {sorted(etat.modeles)}, réglages {reglages})", flush=True)

    def arreter(signum, _frame):
        raise KeyboardInterrupt
    if threading.current_thread() is threading.main_thread():  # arrêt par PID (R10)
        signal.signal(signal.SIGTERM, arreter)
    try:
        serveur.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        serveur.server_close()
    return 0


# --- commande --------------------------------------------------------------------------------------------------------------


class Sortie(Exception):
    def __init__(self, code):
        self.code = code


def rendre(code, version, texte="", cout=PLANCHER, **diag):
    cout = cout if (isinstance(cout, (int, float)) and math.isfinite(cout) and cout > 0) else PLANCHER
    print(json.dumps({"texte": texte, "cout_usd": round(float(cout), 8), "version": version, **diag}, ensure_ascii=False))
    sys.stdout.flush()
    raise Sortie(code)


def verifier_url(url):
    u = urllib.parse.urlsplit(url)
    if u.scheme != "http" or u.hostname not in ("127.0.0.1", "localhost") or u.path not in ("", "/"):
        raise ValueError("--url-relais : http://127.0.0.1:PORT seulement (le relais local tient la clé)")
    return url.rstrip("/") + "/appel"


def plafond_etape(environ):
    etape, brut = environ.get("ETAPE_POLE"), environ.get("PLAFOND_ETAPE_USD")
    if etape is None and brut is None:
        return None, None
    if etape is None or brut is None or not etape.strip():
        raise ValueError("porte « environnement » incomplète : ETAPE_POLE et PLAFOND_ETAPE_USD vont ensemble")
    p = float(brut)
    if not (math.isfinite(p) and p >= 0):
        raise ValueError("PLAFOND_ETAPE_USD invalide")
    return etape, p


def appeler(args, environ, entree, *, nom_fournisseur, version, prix, reglages):
    """`prix` : (entrée, sortie) USD par million pour args.modele ; `reglages` : dict annoncé au relais (doit être identique)."""
    def r(code, **kw):
        rendre(code, version, **kw)
    try:
        cible = verifier_url(args.url_relais)
        plafond = float(environ.get("PLAFOND_SESSION_USD", "nan"))
        if not (math.isfinite(plafond) and plafond > 0):
            raise ValueError("PLAFOND_SESSION_USD absent ou invalide")
        role = environ.get("ROLE_POLE")
        if role not in ROLES:
            raise ValueError(f"ROLE_POLE {role!r} refusé (permis : {ROLES})")
        demande = environ.get("MODELE_DEMANDE_POLE")
        if demande is not None and demande != args.modele:
            raise ValueError(f"MODELE_DEMANDE_POLE {demande!r} ≠ --modele {args.modele!r}")
        etape, plafond_dur = plafond_etape(environ)
        prompt = entree.read()
        if not prompt.strip():
            raise ValueError("consigne vide")
    except (ValueError, SystemExit) as e:
        r(2, erreur=str(e)[:300], envoye=False)
    maxi = args.max_sortie_proposeur if role == "proposeur_ideation" else args.max_sortie_court
    entree_usd = pire_cas(len(prompt), 0, prix)
    mt = min(maxi, int((plafond - entree_usd) * 1e6 / prix[1])) if plafond > entree_usd else 0
    if mt < args.sortie_min_jetons:
        r(4, erreur=f"pire cas au-dessus du plafond de session {plafond} USD ({len(prompt)} caractères)", envoye=False)
    pire = pire_cas(len(prompt), mt, prix)
    if pire > plafond + 1e-12:
        r(4, erreur="pire cas au-dessus du plafond de session", envoye=False)
    diag = {"max_tokens": mt, "caracteres": len(prompt), "pire_cas_usd": round(pire, 8), "modele_demande": args.modele,
            "role": role, "etape": etape, "reglages": reglages}
    try:
        ident = reg.reserver(args.registre, plafond_cumule_usd=args.plafond_cumule_usd, pire_cas_usd=pire,
                             fournisseur=nom_fournisseur, role=role, modele=args.modele, etape=etape,
                             plafond_etape_usd=plafond_dur)
    except (reg.PlafondCumule, reg.RegistreIllisible, OSError) as e:
        r(4, erreur=str(e)[:300], envoye=False, **diag)

    def fin(code, texte="", cout=PLANCHER, origine="plancher", statut="echec", **extra):
        envoye = extra.pop("envoye", True)
        depasse = reg.regler(args.registre, ident, cout_usd=cout, pire_cas_usd=pire, statut=statut, code=code,
                             cout_origine=origine)
        if depasse and code == 0:
            extra.pop("erreur", None)
            r(5, cout=cout, erreur="coût lu au-dessus du pire cas réservé (liste d'arrêt)", envoye=True,
              cout_origine=origine, depassement_reserve=True, **dict(diag, **extra))
        r(code, texte=texte, cout=cout, envoye=envoye, cout_origine=origine, **dict(diag, **extra))

    def interrompu(signum, _frame):
        fin(6, cout=pire, origine="pire_cas", erreur=f"signal {signum}")
    if threading.current_thread() is threading.main_thread():
        signal.signal(signal.SIGTERM, interrompu)
        signal.signal(signal.SIGINT, interrompu)

    corps = json.dumps({"modele": args.modele, "prompt": prompt, "max_tokens": mt, "pire_cas_usd": pire,
                        "reglages": reglages}, ensure_ascii=False).encode("utf-8")
    ouvreur = urllib.request.build_opener(urllib.request.ProxyHandler({}))  # boucle locale : jamais de mandataire
    requete = urllib.request.Request(cible, data=corps, method="POST",
                                     headers={"Content-Type": "application/json", "Content-Length": str(len(corps))})
    try:
        with ouvreur.open(requete, timeout=args.delai_s) as rr:
            brut = rr.read()
    except urllib.error.HTTPError as e:
        motif = e.read()[:300].decode("utf-8", "replace")
        avant = e.code in (400, 402, 403, 409, 411, 413, 429)  # refus du relais : rien n'est parti vers l'interface
        fin(4 if e.code in (402, 429) else 3, cout=PLANCHER if avant else pire, origine="plancher" if avant else "pire_cas",
            erreur=f"HTTP {e.code} : {motif}", envoye=not avant)
    except urllib.error.URLError as e:
        if isinstance(e.reason, ConnectionRefusedError):
            fin(3, erreur="relais injoignable (connexion refusée)", envoye=False)
        fin(3, cout=pire, origine="pire_cas", erreur="URLError : " + str(e.reason)[:200])
    except (TimeoutError, OSError) as e:
        fin(6 if isinstance(e, TimeoutError) else 3, cout=pire, origine="pire_cas", erreur=type(e).__name__ + " : " + str(e)[:200])
    try:
        o = json.loads(brut)
        texte, statut, cout, origine = o["texte"], o["statut"], float(o["cout_usd"]), o["cout_origine"]
    except (ValueError, KeyError, TypeError):
        fin(5, cout=pire, origine="pire_cas", erreur="réponse du relais illisible")
    if origine == "pire_cas":
        cout = pire  # le pire cas réservé, exactement (correction v2 de la commande Argon)
    servi = o.get("modele_servi")
    extra = {"modele_servi": servi, "fin_interface": o.get("fin"), "usage": o.get("usage"), "statut_interface": statut,
             "reglages_relais": o.get("reglages")}
    if o.get("echec"):
        extra.pop("modele_servi")  # échec de transport : aucun modèle n'a répondu
        fin(3, cout=cout, origine=origine, erreur="interface : " + str(o["echec"])[:300], **extra)
    if servi != args.modele:  # identifiant exact : aucune bascule de modèle n'est acceptée
        fin(5, cout=cout, origine=origine, erreur=f"modèle servi {servi!r} ≠ {args.modele!r}", **extra)
    if statut == "REFUS":
        fin(5, cout=cout, origine=origine, statut="refus", refus=True,
            erreur=f"refus du modèle ({o.get('categorie') or o.get('fin')})", **extra)
    if statut in ("TRONQUE", "VIDE", "ANOMALIE"):
        fin(5, cout=cout, origine=origine, statut=statut.lower(),
            erreur=f"réponse non conforme ({statut}, fin {o.get('fin')!r})", **extra)
    if origine != "usage":
        fin(5, cout=cout, origine=origine, erreur="usage absent", **extra)
    fin(0, texte=texte, cout=cout, origine=origine, statut="ok", **extra)


def ajouter_options_appeler(p, port, modele_obligatoire=True):
    p.add_argument("--url-relais", default=f"http://127.0.0.1:{port}")
    p.add_argument("--modele", required=modele_obligatoire)
    p.add_argument("--max-sortie-proposeur", type=int, required=True)
    p.add_argument("--max-sortie-court", type=int, required=True)
    p.add_argument("--sortie-min-jetons", type=int, required=True)
    p.add_argument("--delai-s", type=float, default=1750.0)
    p.add_argument("--registre", required=True)
    p.add_argument("--plafond-cumule-usd", type=float, required=True)


def ajouter_options_servir(s):
    s.add_argument("--port", type=int, required=True)
    s.add_argument("--plafond-usd", type=float, required=True)
    s.add_argument("--max-appels", type=int, required=True)
    s.add_argument("--journal", required=True)
    s.add_argument("--modeles-permis", required=True)


def executer(fonction):
    try:
        return fonction()
    except Sortie as s:
        return s.code
