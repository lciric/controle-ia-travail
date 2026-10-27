"""Relais de clé réel (version 0.6.0, pièce 2 du premier lancement réel) : un petit serveur local tenu par le noyau.

Il tourne dans **son propre processus** (`python -I -m pole.relais_reel …`), lit la vraie clé dans **son seul
environnement** au démarrage (variable `--variable-cle`, `ANTHROPIC_API_KEY` par défaut), l'efface de cet environnement,
et la garde en mémoire. Les agents ne reçoivent que le point d'accès local et le jeton factice (`relais.variables_agent`) ;
à chaque requête, le relais exige ce jeton factice, le remplace par la clé, transmet à l'amont (`https://api.anthropic.com`
par défaut), et renvoie la réponse telle quelle, en flux (les réponses en flux d'événements sont relayées morceau par
morceau). Il tient un **plafond de dépense indépendant de l'orchestrateur** : il lit l'usage dans les réponses (JSON ou
flux d'événements), le convertit en dollars avec un barème officiel lu le 27 octobre 2026, et refuse (statut 402) toute
requête une fois le plafond atteint. Journal des appels en JSON par ligne : jamais la clé, jamais le corps des messages.

Ce que le relais ne garantit pas : qu'un agent ne puisse pas lui parler avec le jeton factice depuis son bac à sable (c'est
le rôle du bac à sable réseau du moteur et de la garde des outils) ; le plafond borne alors la dépense, pas l'usage.

Ce fichier n'est jamais exécuté avec une vraie clé dans ce dépôt : ses essais le lancent avec une clé factice et un amont
factice (`essais/test_v6_relais_reel.py`).
"""

if __name__ == "__main__" and not __package__:  # `python -I pole/relais_reel.py …` : le paquet n'est pas sur le chemin
    import os as _os
    import runpy as _runpy
    import sys as _sys
    _ICI = _os.path.dirname(_os.path.abspath(__file__))
    _sys.path[:] = [p for p in _sys.path if _os.path.abspath(p or _os.curdir) != _ICI]
    _sys.path.insert(0, _os.path.dirname(_ICI))
    _runpy.run_module("pole.relais_reel", run_name="__main__", alter_sys=True)
    raise SystemExit(0)

import argparse
import http.client
import json
import os
import socket
import sys
import threading
import time
import urllib.parse
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

from .relais import HOTES_LOCAUX, JETON_FACTICE, RelaisInvalide

# Barème officiel, dollars par million de jetons, lu le 27 octobre 2026 sur
# https://platform.claude.com/docs/en/about-claude/pricing (entrée, sortie, écriture de cache 5 min, lecture de cache).
BAREME_USD_PAR_MILLION = {
    "claude-opus-5-5": (4.0, 20.0, 5.0, 0.20),
    "claude-sonnet-5-5": (2.0, 10.0, 2.5, 0.10),
    "claude-haiku-5-5": (0.10, 0.50, 0.125, 0.01),
    "claude-fable-5-1": (10.0, 50.0, 12.5, 0.25),
    "claude-mythos-5-1": (10.0, 50.0, 12.5, 0.25),
}
BAREME_INCONNU = (10.0, 50.0, 12.5, 0.25)  # modèle inconnu : le plus cher du barème (borne haute, jamais basse)
# v11 (contre-lecture C10) : seuls les messages ; `/v1/messages/batches` (dont la création ne porte pas d'usage, donc
# une dépense que le plafond ne verrait pas) et tout autre point d'entrée sont refusés.
CHEMINS_PERMIS = ("/v1/messages",)
CHEMINS_REFUSES = ("/v1/messages/batches",)
EN_TETES_NON_RELAYES = {"host", "connection", "content-length", "transfer-encoding", "keep-alive", "proxy-authorization",
                        "te", "trailer", "upgrade", "accept-encoding", "x-api-key", "authorization"}
TAILLE_MAX_CORPS = 20_000_000


def tarif_du_modele(modele):
    """Barème du modèle (préfixe reconnu), sinon le plus cher."""
    nom = (modele or "").lower()
    for prefixe, tarif in BAREME_USD_PAR_MILLION.items():
        if nom.startswith(prefixe):
            return tarif
    return BAREME_INCONNU


def cout_usd(modele, usage):
    """Coût d'un appel d'après son usage {input_tokens, output_tokens, cache_creation_input_tokens,
    cache_read_input_tokens} ; un champ absent vaut zéro."""
    entree, sortie, ecriture, lecture = tarif_du_modele(modele)
    u = usage or {}
    return (int(u.get("input_tokens") or 0) * entree + int(u.get("output_tokens") or 0) * sortie
            + int(u.get("cache_creation_input_tokens") or 0) * ecriture
            + int(u.get("cache_read_input_tokens") or 0) * lecture) / 1_000_000


def usage_d_une_reponse_json(corps):
    """(modèle, usage) d'une réponse non relayée en flux ; (None, None) si illisible."""
    try:
        objet = json.loads(corps.decode("utf-8"))
    except (UnicodeDecodeError, ValueError):
        return None, None
    if not isinstance(objet, dict):
        return None, None
    return objet.get("model"), objet.get("usage")


class LecteurUsageFlux:
    """Lit l'usage dans un flux d'événements (`message_start` : modèle et jetons d'entrée ; `message_delta` : jetons de
    sortie cumulés), morceau par morceau, sans garder les contenus."""

    def __init__(self):
        self.modele, self.usage, self._reste = None, {}, b""

    def avaler(self, morceau):
        self._reste += morceau
        while b"\n" in self._reste:
            ligne, self._reste = self._reste.split(b"\n", 1)
            ligne = ligne.strip()
            if not ligne.startswith(b"data:"):
                continue
            try:
                evenement = json.loads(ligne[5:].decode("utf-8"))
            except (UnicodeDecodeError, ValueError):
                continue
            if not isinstance(evenement, dict):
                continue
            if evenement.get("type") == "message_start":
                message = evenement.get("message") or {}
                self.modele = message.get("model") or self.modele
                for cle, valeur in (message.get("usage") or {}).items():
                    if isinstance(valeur, int):
                        self.usage[cle] = valeur
            elif evenement.get("type") == "message_delta":
                for cle, valeur in (evenement.get("usage") or {}).items():
                    if isinstance(valeur, int):
                        self.usage[cle] = valeur


def valider_hote(hote):
    if hote not in HOTES_LOCAUX:
        raise RelaisInvalide(f"le relais n'écoute que sur la boucle locale (127.0.0.1, localhost, ::1), reçu {hote!r}")
    return hote


RESERVE_PAR_APPEL_DEFAUT = 0.40  # v7, version 5 : au-dessus du coût maximal d'un appel vu en (a), 0,266 USD (défaut 8)


class Compteur:
    """Plafond de dépense du relais. Chaque appel **réserve** `reserve_par_appel` avant de partir (des appels simultanés ne
    peuvent pas franchir le plafond ensemble : défaut vu par la répétition générale, corrigé ici), puis règle au coût lu.

    Garantie : la dépense ne dépasse le plafond que d'au plus (coût maximal d'un appel − réserve) × appels simultanés.
    v7, version 5 (défaut 8 du premier lancement réel : un appel à 0,266 USD pour une réserve de 0,25) : réserve par défaut
    0,40 USD, et tout dépassement de la réserve par un appel est compté et journalisé (`depassement_max_usd`)."""

    def __init__(self, plafond_usd, reserve_par_appel=RESERVE_PAR_APPEL_DEFAUT):
        self.plafond, self.reserve, self.depense = float(plafond_usd), float(reserve_par_appel), 0.0
        self.engage, self.appels, self.refus = 0.0, 0, 0
        self.depassements, self.depassement_max = 0, 0.0
        self._verrou = threading.Lock()

    def reserver(self):
        with self._verrou:
            if self.depense + self.engage + self.reserve > self.plafond + 1e-12:
                return False
            self.engage += self.reserve
            return True

    def regler(self, cout):
        with self._verrou:
            self.engage -= self.reserve
            self.depense += cout
            self.appels += 1
            if cout > self.reserve:
                self.depassements += 1
                self.depassement_max = max(self.depassement_max, cout - self.reserve)
            return self.depense

    def etat(self):
        with self._verrou:
            return {"plafond_usd": self.plafond, "reserve_par_appel_usd": self.reserve, "depense_usd": round(self.depense, 6),
                    "engage_usd": round(self.engage, 6), "appels": self.appels, "refus": self.refus,
                    "restant_usd": round(self.plafond - self.depense, 6),
                    "appels_au_dessus_de_la_reserve": self.depassements,
                    "depassement_max_usd": round(self.depassement_max, 6)}


def fabriquer_gestionnaire(cle, amont, compteur, journal, verrou_journal):
    """Gestionnaire des requêtes ; `compteur` est un `Compteur` (plafond et réserve par appel)."""
    parties = urllib.parse.urlsplit(amont)
    if parties.scheme not in ("http", "https") or not parties.hostname:
        raise RelaisInvalide(f"adresse d'amont invalide : {amont!r}")

    def ecrire_journal(entree):
        if journal is None:
            return
        with verrou_journal:
            with open(journal, "a", encoding="utf-8") as f:
                f.write(json.dumps(entree, ensure_ascii=False, sort_keys=True) + "\n")

    class Gestionnaire(BaseHTTPRequestHandler):
        protocol_version = "HTTP/1.1"
        server_version = "RelaisNoyau/0.6"

        def log_message(self, format, *args):  # noqa: A002 — signature imposée par la bibliothèque standard
            pass  # aucun journal implicite (il contiendrait les chemins et pourrait finir sur un terminal partagé)

        def _repondre_json(self, statut, objet):
            corps = json.dumps(objet, ensure_ascii=False).encode("utf-8")
            self.send_response(statut)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(corps)))
            self.end_headers()
            self.wfile.write(corps)

        def do_GET(self):
            if self.path == "/relais/etat":
                return self._repondre_json(200, compteur.etat())
            return self._relayer("GET")

        def do_POST(self):
            return self._relayer("POST")

        def _relayer(self, methode):
            debut = time.time()
            chemin = self.path
            if not chemin.startswith(CHEMINS_PERMIS) or chemin.startswith(CHEMINS_REFUSES):
                compteur.refus += 1
                return self._repondre_json(404, {"erreur": "chemin non relayé"})
            recu = self.headers.get("x-api-key") or ""
            if recu != JETON_FACTICE:
                compteur.refus += 1
                ecrire_journal({"quand": debut, "methode": methode, "chemin": chemin, "statut": 401,
                                "motif": "jeton différent du jeton factice"})
                return self._repondre_json(401, {"erreur": "le relais n'accepte que le jeton factice du pôle"})
            if not compteur.reserver():
                compteur.refus += 1
                ecrire_journal({"quand": debut, "methode": methode, "chemin": chemin, "statut": 402,
                                "motif": "plafond de dépense du relais atteint (réserve par appel comprise)", **compteur.etat()})
                return self._repondre_json(402, {"erreur": "plafond de dépense du relais atteint", **compteur.etat()})
            longueur = int(self.headers.get("content-length") or 0)
            if longueur > TAILLE_MAX_CORPS:
                compteur.refus += 1
                compteur.regler(0.0)
                return self._repondre_json(413, {"erreur": "corps trop volumineux"})
            corps = self.rfile.read(longueur) if longueur else b""
            en_tetes = {k: v for k, v in self.headers.items() if k.lower() not in EN_TETES_NON_RELAYES}
            en_tetes["x-api-key"] = cle
            en_tetes["Accept-Encoding"] = "identity"
            en_tetes["Host"] = parties.netloc
            if corps:
                en_tetes["Content-Length"] = str(len(corps))
            connexion = (http.client.HTTPSConnection if parties.scheme == "https" else http.client.HTTPConnection)(
                parties.hostname, parties.port, timeout=600)
            try:
                connexion.request(methode, chemin, body=corps or None, headers=en_tetes)
                reponse = connexion.getresponse()
            except (OSError, http.client.HTTPException) as erreur:
                connexion.close()
                compteur.regler(0.0)
                ecrire_journal({"quand": debut, "methode": methode, "chemin": chemin, "statut": 502,
                                "motif": type(erreur).__name__})
                return self._repondre_json(502, {"erreur": "amont injoignable : " + type(erreur).__name__})
            type_contenu = reponse.getheader("Content-Type") or ""
            en_flux = "text/event-stream" in type_contenu
            self.send_response(reponse.status)
            for k, v in reponse.getheaders():
                if k.lower() in EN_TETES_NON_RELAYES or k.lower() in ("content-length", "transfer-encoding"):
                    continue
                self.send_header(k, v)
            self.send_header("Transfer-Encoding", "chunked")
            self.send_header("Connection", "close")
            self.end_headers()
            lecteur, accumule, octets = LecteurUsageFlux(), bytearray(), 0
            try:
                while True:
                    morceau = reponse.read(4096)
                    if not morceau:
                        break
                    octets += len(morceau)
                    if en_flux:
                        lecteur.avaler(morceau)
                    elif len(accumule) <= TAILLE_MAX_CORPS:
                        accumule.extend(morceau)
                    self.wfile.write(b"%x\r\n%s\r\n" % (len(morceau), morceau))
                    self.wfile.flush()
                self.wfile.write(b"0\r\n\r\n")
                self.wfile.flush()
            except OSError:
                pass  # client parti : on comptabilise ce qui a été lu
            finally:
                connexion.close()
            if en_flux:
                modele, usage = lecteur.modele, lecteur.usage
            else:
                modele, usage = usage_d_une_reponse_json(bytes(accumule))
            cout = cout_usd(modele, usage) if usage else 0.0
            cumul = compteur.regler(cout)
            ecrire_journal({"quand": debut, "duree_s": round(time.time() - debut, 3), "methode": methode, "chemin": chemin,
                            "statut": reponse.status, "en_flux": en_flux, "octets": octets, "modele": modele,
                            "usage": usage or {}, "cout_usd": round(cout, 6), "depense_cumulee_usd": round(cumul, 6),
                            "depassement_de_reserve_usd": round(max(0.0, cout - compteur.reserve), 6)})
            self.close_connection = True

    return Gestionnaire


def lire_cle(environnement, variable):
    """Lit la clé dans l'environnement donné et l'en efface ; ne la rend qu'à l'appelant (jamais journalisée)."""
    cle = environnement.get(variable)
    if not cle:
        raise RelaisInvalide(f"aucune clé dans la variable {variable} de l'environnement du relais")
    environnement.pop(variable, None)
    return cle


def servir(hote, port, cle, amont, plafond_usd, journal=None, pret=None, reserve_par_appel=RESERVE_PAR_APPEL_DEFAUT):
    """Sert jusqu'à l'arrêt du processus ; `pret` (événement) est levé avec l'adresse effective dans `pret.url`."""
    valider_hote(hote)
    compteur = Compteur(plafond_usd, reserve_par_appel)
    gestionnaire = fabriquer_gestionnaire(cle, amont, compteur, journal, threading.Lock())
    serveur = ThreadingHTTPServer((hote, port), gestionnaire)
    serveur.daemon_threads = True
    url = f"http://{hote}:{serveur.server_address[1]}"
    if pret is not None:
        pret.url = url
        pret.set()
    print(f"relais prêt sur {url} (amont {amont}, plafond {plafond_usd} USD, réserve par appel {reserve_par_appel} USD)",
          flush=True)
    try:
        serveur.serve_forever()
    finally:
        serveur.server_close()
    return url


def analyseur():
    a = argparse.ArgumentParser(prog="relais_reel", description="Relais de clé local tenu par le noyau.")
    a.add_argument("--hote", default="127.0.0.1")
    a.add_argument("--port", type=int, default=8787, help="0 : port libre choisi par le système")
    a.add_argument("--amont", default="https://api.anthropic.com")
    a.add_argument("--variable-cle", default="ANTHROPIC_API_KEY",
                   help="variable de l'environnement du relais qui porte la clé (effacée après lecture)")
    a.add_argument("--plafond-usd", type=float, required=True, help="plafond de dépense tenu par le relais")
    a.add_argument("--journal", help="journal des appels (JSON par ligne, sans clé ni corps)")
    a.add_argument("--reserve-par-appel", type=float, default=RESERVE_PAR_APPEL_DEFAUT,
                   help="montant réservé avant chaque appel, réglé au coût lu après (borne les appels simultanés)")
    return a


def principal(argv=None):
    args = analyseur().parse_args(argv)
    try:
        cle = lire_cle(os.environ, args.variable_cle)
        if not (args.plafond_usd > 0):
            raise RelaisInvalide("plafond strictement positif requis")
        if not (args.reserve_par_appel >= 0):
            raise RelaisInvalide("réserve par appel positive ou nulle requise")
        servir(args.hote, args.port, cle, args.amont, args.plafond_usd, args.journal, reserve_par_appel=args.reserve_par_appel)
    except RelaisInvalide as erreur:
        print(f"erreur : {erreur}", file=sys.stderr)
        return 2
    except KeyboardInterrupt:
        return 0
    return 0


if __name__ == "__main__":
    sys.exit(principal())
