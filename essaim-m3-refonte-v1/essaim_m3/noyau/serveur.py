"""Serveur d'appels du noyau : la seule porte de l'organisme vers les espèces.

Il tient les clés, le journal et le plafond (`appels.Appelant`) hors du bac à sable ; l'organisme ne voit qu'un
socket Unix et le module `noyau_client`. Un plafond atteint rend le statut `PLAFOND` et ne lève rien chez
l'organisme : c'est à lui de s'arrêter proprement ; le noyau, lui, ne sert plus rien.
"""
from __future__ import annotations

import json
import os
import socket
import threading

from .appels import Appelant, Arret, ESPECES


class ServeurAppels:
    def __init__(self, appelant: Appelant, chemin_socket: str, appels_max: int):
        self.appelant = appelant
        self.chemin = chemin_socket
        self.appels_max = int(appels_max)
        self.n_appels = 0
        self.refus: list[dict] = []
        self._verrou = threading.Lock()
        self._arret = threading.Event()
        self._fil = None
        self._sock = None

    # ---- cycle de vie ----
    def __enter__(self):
        if os.path.exists(self.chemin):
            os.unlink(self.chemin)
        self._sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        self._sock.bind(self.chemin)
        os.chmod(self.chemin, 0o600)
        self._sock.listen(16)
        self._sock.settimeout(0.5)
        self._fil = threading.Thread(target=self._boucle, daemon=True)
        self._fil.start()
        return self

    def __exit__(self, *exc):
        self._arret.set()
        if self._fil is not None:
            self._fil.join(timeout=5)
        if self._sock is not None:
            self._sock.close()
        if os.path.exists(self.chemin):
            os.unlink(self.chemin)

    # ---- service ----
    def _boucle(self):
        while not self._arret.is_set():
            try:
                conn, _ = self._sock.accept()
            except socket.timeout:
                continue
            except OSError:
                break
            threading.Thread(target=self._servir, args=(conn,), daemon=True).start()

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
        with conn:
            req = self._lire(conn)
            rep = self.traiter(req)
            try:
                conn.sendall((json.dumps(rep, ensure_ascii=False) + "\n").encode("utf-8"))
            except OSError:
                pass

    def traiter(self, req) -> dict:
        if not isinstance(req, dict):
            return {"statut": "ANOMALIE", "texte": "", "echec": "requête illisible"}
        op = req.get("op")
        if op == "especes":
            return {"especes": sorted(ESPECES)}
        if op == "budget":
            with self._verrou:
                return {"appels_restants": max(0, self.appels_max - self.n_appels),
                        "usd_restants": round(max(0.0, self.appelant.plafond_usd - self.appelant.depense_usd), 4)}
        if op != "appeler":
            return {"statut": "ANOMALIE", "texte": "", "echec": f"opération inconnue : {op!r}"}
        espece = req.get("espece")
        prompt = req.get("prompt")
        if espece not in ESPECES or not isinstance(prompt, str) or not prompt.strip():
            return {"statut": "ANOMALIE", "texte": "", "echec": "espèce inconnue ou consigne vide"}
        with self._verrou:
            if self.n_appels >= self.appels_max:
                self.refus.append({"raison": "appels_max", "espece": espece})
                return {"statut": "PLAFOND", "texte": "", "echec": "nombre maximal d'appels atteint"}
            self.n_appels += 1
            try:
                res = self.appelant.appeler(espece, f"organisme", prompt, max_tokens=req.get("max_tokens"),
                                            role=str(req.get("role", ""))[:40])
            except Arret as e:
                self.refus.append({"raison": "plafond_usd", "espece": espece, "detail": str(e)[:200]})
                return {"statut": "PLAFOND", "texte": "", "echec": str(e)[:200]}
        return {"statut": res.statut, "texte": res.texte, "modele_servi": res.modele_servi, "fin": res.fin,
                "usage": res.usage, "cout_usd": res.cout_usd, "identifiant": res.identifiant,
                "echec": (str(res.echec)[:200] if res.echec else None)}
