"""Doublure locale de l'interface du loueur pour les essais de l'amorce — v1 : consigne chaque requête (méthode, chemin, présence
d'un en-tête d'autorisation, jamais sa valeur) dans JOURNAL, rend 200. Usage : python3 doublure_vast_v1.py PORT JOURNAL"""
import http.server
import json
import sys

PORT, JOURNAL = int(sys.argv[1]), sys.argv[2]


class G(http.server.BaseHTTPRequestHandler):
    def _r(self):
        n = int(self.headers.get("Content-Length") or 0)
        corps = self.rfile.read(n).decode() if n else ""
        with open(JOURNAL, "a") as f:
            f.write(json.dumps({"methode": self.command, "chemin": self.path, "autorisation": bool(self.headers.get("Authorization")),
                                "corps": corps}) + "\n")
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"{}")

    do_DELETE = do_PUT = do_GET = do_POST = _r

    def log_message(self, *a):
        pass


http.server.HTTPServer(("127.0.0.1", PORT), G).serve_forever()
