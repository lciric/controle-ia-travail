"""Serveur factice de la vérification (127.0.0.1 seulement). Emploi : python -I serveur-verif.py DOSSIER
DOSSIER/pret reçoit le port ; l'arrêt se fait par la création de DOSSIER/arret.
Routes : POST /v1/servers -> 201 (corps conservé dans DOSSIER/corps-N.bin ; réponse avec root_password et user_data imbriqués) ;
POST /err -> 403 (même charge) ; POST /redir -> 302 vers /cible ; GET|POST /cible ; CONNECT -> 502 (puits de mandataire).
Journal : DOSSIER/journal.txt, une ligne par requête : méthode, chemin, taille, sha256 du corps, sha256 de l'en-tête Authorization
(jamais le jeton, jamais le corps)."""
import hashlib
import http.server
import json
import os
import sys

D = sys.argv[1]
N = [0]


def sha(b):
    return hashlib.sha256(b).hexdigest()


class H(http.server.BaseHTTPRequestHandler):
    def _journal(self, corps):
        a = self.headers.get("Authorization", "")
        with open(os.path.join(D, "journal.txt"), "a") as f:
            f.write("%s %s corps=%d sha=%s auth=%s\n" % (self.command, self.path, len(corps), sha(corps), sha(a.encode())))

    def _rep(self, code, obj, extra=None):
        b = json.dumps(obj).encode()
        self.send_response(code)
        if extra:
            for k, v in extra.items():
                self.send_header(k, v)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(b)))
        self.end_headers()
        self.wfile.write(b)

    def do_POST(self):
        n = int(self.headers.get("Content-Length", "0"))
        corps = self.rfile.read(n)
        self._journal(corps)
        if self.path == "/redir":
            self._rep(302, {}, {"Location": "/cible"})
            return
        N[0] += 1
        with open(os.path.join(D, "corps-%d.bin" % N[0]), "wb") as f:
            f.write(corps)
        charge = {"server": {"id": 424242, "status": "initializing", "created": "2026-11-22T00:00:00+00:00",
                             "user_data": "ECHO-USER-DATA-RETIRER", "meta": [{"root_password": "MDP-IMBRIQUE-LISTE"}]},
                  "root_password": "MDP-RACINE-FACTICE", "action": {"id": 1, "status": "running", "root_password": "MDP-ACTION"}}
        self._rep(403 if self.path == "/err" else 201, charge)

    def do_GET(self):
        self._journal(b"")
        self._rep(200, {"cible": True})

    def do_CONNECT(self):
        self._journal(b"")
        self.send_response(502)
        self.send_header("Content-Length", "0")
        self.end_headers()

    def log_message(self, *a):
        pass


s = http.server.HTTPServer(("127.0.0.1", 0), H)
s.timeout = 0.1
with open(os.path.join(D, "pret.tmp"), "w") as f:
    f.write(str(s.server_address[1]))
os.rename(os.path.join(D, "pret.tmp"), os.path.join(D, "pret"))
while not os.path.exists(os.path.join(D, "arret")):
    s.handle_request()
