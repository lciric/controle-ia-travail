"""Serveur FACTICE de l'interface de création (banc du contrôle de sortie v1), sur 127.0.0.1, port choisi par le système.

Pour chaque POST : écrit dans JOURNAL une ligne « chemin, taille du corps, sha256 du corps, sha256 du jeton porté par
l'en-tête Authorization » (jamais le corps ni le jeton) ; répond 201 avec un corps JSON factice qui porte un identifiant,
un statut, un champ root_password et un champ user_data (pour éprouver l'expurgation). Écrit son port dans PRET ; s'arrête
quand le fichier ARRET existe.
Emploi : python -I serveur-hetzner-factice.py JOURNAL PRET ARRET
"""
import hashlib
import http.server
import json
import os
import sys

JOURNAL, PRET, ARRET = sys.argv[1:4]


class Gestion(http.server.BaseHTTPRequestHandler):
    def do_POST(self):
        n = int(self.headers.get("Content-Length", "0"))
        corps = self.rfile.read(n)
        auth = self.headers.get("Authorization", "")
        jet = auth[7:] if auth.startswith("Bearer ") else ""
        with open(JOURNAL, "a", encoding="utf-8") as f:
            f.write("POST %s ; corps %d octets, sha256 %s ; jeton sha256 %s ; type %s\n" % (
                self.path, len(corps), hashlib.sha256(corps).hexdigest(), hashlib.sha256(jet.encode()).hexdigest(),
                self.headers.get("Content-Type", "")))
        rep = json.dumps({"server": {"id": 424242, "name": "essai-3-palier-0b", "status": "initializing",
                                     "created": "2026-11-22T00:00:00+00:00", "user_data": "ECHO-USER-DATA-A-RETIRER"},
                          "root_password": "MOT-DE-PASSE-FACTICE-A-RETIRER", "action": {"id": 1, "status": "running"}}).encode()
        self.send_response(201)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(rep)))
        self.end_headers()
        self.wfile.write(rep)

    def log_message(self, *a):
        pass


s = http.server.HTTPServer(("127.0.0.1", 0), Gestion)
s.timeout = 0.2
with open(PRET + ".travail", "w") as f:
    f.write(str(s.server_address[1]))
os.rename(PRET + ".travail", PRET)
while not os.path.exists(ARRET):
    s.handle_request()
