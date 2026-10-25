"""Serveur d'appels du noyau : la seule porte de l'organisme vers les espèces.

Il tient les clés, le journal et le plafond (`appels.Appelant`) hors du bac à sable ; l'organisme ne voit qu'un
socket Unix et le module `noyau_client`. Un plafond atteint rend le statut `PLAFOND` et ne lève rien chez
l'organisme : c'est à lui de s'arrêter proprement ; le noyau, lui, ne sert plus rien.

Les appels sont servis en parallèle, au plus `parallele_max` à la fois (le moteur de Gemini en lançait 8 à 24 ;
un essaim qui veut des vagues parallèles doit pouvoir les faire) : le compteur d'appels est tenu sous verrou,
l'appel lui-même non ; le plafond en dollars est garanti par `Appelant` au pire cas sur les appels en vol.
"""
from __future__ import annotations

import json
import os
import socket
import threading

from .appels import Appelant, Arret, ESPECES

PARALLELE_MAX_DEFAUT = 8
ATTENTE_FILS_S = 900  # RV-08 : à la fin d'une génération, attente au plus de ce délai des appels encore en vol
MAX_TOKENS_DEFAUT_ORGANISME = 4096  # si l'organisme ne fixe pas max_tokens ; il peut demander plus, jusqu'au maximum du modèle


class ServeurAppels:
    def __init__(self, appelant: Appelant, chemin_socket: str, appels_max: int, parallele_max: int = PARALLELE_MAX_DEFAUT, rechercheur=None,
                 entraineur=None, telechargeur=None, max_tokens_appel: int | None = None):
        self.appelant = appelant
        # plafond de jetons de sortie par appel (budget `max_tokens_appel`, étape 1 « économe ») : le noyau rabat ce que
        # l'organisme demande ; None = aucun plafond (jusqu'au maximum du modèle, comme avant)
        self.max_tokens_appel = (None if max_tokens_appel is None else int(max_tokens_appel))
        if self.max_tokens_appel is not None and self.max_tokens_appel <= 0:
            raise ValueError("max_tokens_appel doit être strictement positif")
        self.rabattements = 0  # appels dont le max_tokens demandé a été rabattu au plafond (rapporté)
        self.rechercheur = rechercheur  # `recherche.Rechercheur` ou None (recherche non servie dans ce run)
        self.entraineur = entraineur    # `entrainement.Entraineur` ou None (apprentissage par gradient non servi)
        self.telechargeur = telechargeur  # `moisson.Telechargeur` ou None (téléchargement non servi)
        self.chemin = chemin_socket
        self.appels_max = int(appels_max)
        self.parallele_max = max(1, int(parallele_max))
        self.n_appels = 0
        self.non_conformes = 0   # appels dont le modèle servi n'est pas le modèle demandé (CR-02) : la génération est invalidée
        self.arret = None        # raison d'arrêt posée par le noyau : plus aucun appel servi
        self.en_vol_max = 0  # plus grand nombre d'appels simultanés observé (rapporté, pour l'audit)
        self._en_vol = 0
        self.refus: list[dict] = []
        self._verrou = threading.Lock()
        self._semaphore = threading.BoundedSemaphore(self.parallele_max)
        self._arret = threading.Event()
        self._fil = None
        self._sock = None
        self._fils: set = set()      # RV-08 : fils de service en cours, attendus à la sortie avant toute lecture du journal
        self.fils_non_finis = 0      # fils encore en vol après `ATTENTE_FILS_S` (consigné ; jamais attendu en silence)
        self.indisponibles: dict[str, int] = {}  # CE4-02 : demandes d'un service non servi dans ce run, par opération (rapport)

    # ---- cycle de vie ----
    def __enter__(self):
        if os.path.exists(self.chemin):
            os.unlink(self.chemin)
        self._sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        self._sock.bind(self.chemin)
        os.chmod(self.chemin, 0o666)  # l'organisme tourne sous un autre utilisateur (CR-01) ; le socket est local au conteneur
        self._sock.listen(16)
        self._sock.settimeout(0.5)
        self._fil = threading.Thread(target=self._boucle, daemon=True)
        self._fil.start()
        return self

    def __exit__(self, *exc):
        self._arret.set()  # plus aucune connexion acceptée
        if self._fil is not None:
            self._fil.join(timeout=5)
        if self._sock is not None:
            self._sock.close()
        if os.path.exists(self.chemin):
            os.unlink(self.chemin)
        # RV-08 : un appel servi mais non fini quand l'organisme s'arrête (délai dépassé, appels en parallèle) est attendu :
        # sa ligne entre au journal et son coût à la dépense avant que le noyau ne les lise et ne dépose la génération
        import time as _time
        limite = _time.monotonic() + ATTENTE_FILS_S
        with self._verrou:
            fils = list(self._fils)
        for f in fils:
            f.join(timeout=max(0.0, limite - _time.monotonic()))
        self.fils_non_finis = sum(1 for f in fils if f.is_alive())

    # ---- service ----
    def _boucle(self):
        while not self._arret.is_set():
            try:
                conn, _ = self._sock.accept()
            except socket.timeout:
                continue
            except OSError:
                break
            fil = threading.Thread(target=self._servir, args=(conn,), daemon=True)
            with self._verrou:
                self._fils.add(fil)
            fil.start()

    def _lire(self, conn) -> dict | None:
        tampon = b""
        conn.settimeout(30)
        while not tampon.endswith(b"\n"):
            try:
                morceau = conn.recv(1 << 20)
            except OSError:
                return None
            if not morceau:
                break
            tampon += morceau
        try:
            return json.loads(tampon.decode("utf-8"))
        except (json.JSONDecodeError, UnicodeDecodeError):
            return None

    def _servir(self, conn):
        try:
            with conn:
                req = self._lire(conn)
                rep = self.traiter(req)
                try:
                    conn.sendall((json.dumps(rep, ensure_ascii=False) + "\n").encode("utf-8"))
                except OSError:
                    pass
        finally:
            with self._verrou:
                self._fils.discard(threading.current_thread())

    def _noter_indisponible(self, op: str) -> None:
        with self._verrou:
            self.indisponibles[op] = self.indisponibles.get(op, 0) + 1

    def traiter(self, req) -> dict:
        if not isinstance(req, dict):
            return {"statut": "ANOMALIE", "texte": "", "echec": "requête illisible"}
        op = req.get("op")
        if op == "especes":
            return {"especes": sorted(ESPECES)}
        if op == "budget":
            with self._verrou:
                return {"appels_restants": max(0, self.appels_max - self.n_appels), "max_tokens_appel": self.max_tokens_appel,
                        "usd_restants": round(max(0.0, self.appelant.plafond_usd - self.appelant.depense_usd), 4),
                        "recherches_restantes": (max(0, self.rechercheur.recherches_max - self.rechercheur.compteur) if self.rechercheur is not None else 0),
                        "entrainements_restants": (max(0, self.entraineur.entrainements_max - self.entraineur.compteur) if self.entraineur is not None else 0),
                        "sources": (self.rechercheur.sources() if self.rechercheur is not None else []),
                        "telechargements_restants": (max(0, self.telechargeur.telechargements_max - self.telechargeur.compteur) if self.telechargeur is not None else 0),
                        "octets_restants": (max(0, self.telechargeur.octets_max_total - self.telechargeur.octets) if self.telechargeur is not None else 0)}
        if op == "entrainer":
            if self.entraineur is None:
                self._noter_indisponible(op)
                return {"statut": "INDISPONIBLE", "identifiant": None, "problemes": ["apprentissage par gradient non servi dans ce run"]}
            return self.entraineur.entrainer(req.get("spec"), role=str(req.get("role", ""))[:40])
        if op == "predire":
            if self.entraineur is None:
                self._noter_indisponible(op)
                return {"statut": "INDISPONIBLE", "probabilites": {}, "echec": "apprentissage par gradient non servi dans ce run"}
            return self.entraineur.predire(req.get("identifiant"), req.get("ids"), role=str(req.get("role", ""))[:40])
        if op == "rechercher":
            if self.rechercheur is None:
                self._noter_indisponible(op)
                return {"statut": "INDISPONIBLE", "source": None, "resultats": [], "identifiant": None, "echec": "recherche non servie dans ce run"}
            return self.rechercheur.rechercher(req.get("requete"), req.get("n", 5), role=str(req.get("role", ""))[:40], source=req.get("source"))
        if op == "telecharger":
            if self.telechargeur is None:
                self._noter_indisponible(op)
                return {"statut": "INDISPONIBLE", "identifiant": None, "texte": "", "echec": "téléchargement non servi dans ce run"}
            return self.telechargeur.telecharger(req.get("reference"), role=str(req.get("role", ""))[:40])
        if op != "appeler":
            return {"statut": "ANOMALIE", "texte": "", "echec": f"opération inconnue : {op!r}"}
        espece = req.get("espece")
        prompt = req.get("prompt")
        if espece not in ESPECES or not isinstance(prompt, str) or not prompt.strip():
            return {"statut": "ANOMALIE", "texte": "", "echec": "espèce inconnue ou consigne vide"}
        with self._verrou:
            if self.arret is not None:
                self.refus.append({"raison": "arret_noyau", "espece": espece, "detail": self.arret})
                return {"statut": "ARRET_NOYAU", "texte": "", "echec": self.arret}
            if self.n_appels >= self.appels_max:
                self.refus.append({"raison": "appels_max", "espece": espece})
                return {"statut": "PLAFOND", "texte": "", "echec": "nombre maximal d'appels atteint"}
            self.n_appels += 1
        with self._semaphore:
            with self._verrou:
                self._en_vol += 1
                self.en_vol_max = max(self.en_vol_max, self._en_vol)
            try:
                mt = req.get("max_tokens")
                mt = int(mt) if isinstance(mt, (int, float)) and not isinstance(mt, bool) and mt > 0 else MAX_TOKENS_DEFAUT_ORGANISME
                if self.max_tokens_appel is not None and mt > self.max_tokens_appel:
                    mt = self.max_tokens_appel
                    with self._verrou:
                        self.rabattements += 1
                res = self.appelant.appeler(espece, "organisme", prompt, max_tokens=mt,
                                            role=str(req.get("role", ""))[:40])
            except Arret as e:
                with self._verrou:
                    self.refus.append({"raison": "plafond_usd", "espece": espece, "detail": str(e)[:200]})
                return {"statut": "PLAFOND", "texte": "", "echec": str(e)[:200]}
            finally:
                with self._verrou:
                    self._en_vol -= 1
        if res.statut == "MODELE_NON_CONFORME":
            with self._verrou:
                self.non_conformes += 1
                self.arret = f"modèle servi non conforme ({res.modele_servi!r} pour {res.modele_demande!r}) : génération invalidée, plus aucun appel servi"
        return {"statut": res.statut, "texte": res.texte, "modele_servi": res.modele_servi, "fin": res.fin,
                "usage": res.usage, "cout_usd": res.cout_usd, "identifiant": res.identifiant, "max_tokens_servi": mt,
                "echec": (str(res.echec)[:200] if res.echec else None)}
