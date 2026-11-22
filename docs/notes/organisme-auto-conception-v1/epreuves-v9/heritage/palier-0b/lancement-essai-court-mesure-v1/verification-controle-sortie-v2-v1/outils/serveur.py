"""Serveur factice de la vérification. Emploi : serveur.py JOURNAL PRET ARRET
Route /rNNN (NNN = 301,302,303,307,308) : répond NNN avec Location vers /cible-NNN. Autre : 201 JSON.
Journal : méthode chemin taille jeton-présent(oui/non, sha court). Jamais le jeton."""
import hashlib, http.server, json, os, sys
J, PRET, ARRET = sys.argv[1:4]

class H(http.server.BaseHTTPRequestHandler):
    def go(self):
        n = int(self.headers.get("Content-Length", "0") or 0)
        c = self.rfile.read(n) if n else b""
        a = self.headers.get("Authorization", "")
        with open(J, "a") as f:
            f.write("%s %s corps=%d sha=%s jeton=%s\n" % (self.command, self.path, len(c), hashlib.sha256(c).hexdigest(),
                    hashlib.sha256(a.encode()).hexdigest()[:12] if a else "aucun"))
        p = self.path
        if p == "/lent":
            import time; time.sleep(2)
        if p.startswith("/r") and p[2:].isdigit():
            self.send_response(int(p[2:]))
            self.send_header("Location", "http://127.0.0.1:%d/cible-%s" % (self.server.server_address[1], p[2:]))
            self.send_header("Content-Length", "0")
            self.end_headers()
            return
        r = json.dumps({"server": {"id": 7, "status": "initializing", "created": "x", "user_data": "ECHO"},
                        "root_password": "MDPFACTICE"}).encode()
        self.send_response(201)
        self.send_header("Content-Length", str(len(r)))
        self.end_headers()
        self.wfile.write(r)
    do_POST = do_GET = go
    def log_message(self, *a): pass

s = http.server.HTTPServer(("127.0.0.1", 0), H)
s.timeout = 0.2
open(PRET + ".t", "w").write(str(s.server_address[1]))
os.rename(PRET + ".t", PRET)
while not os.path.exists(ARRET):
    s.handle_request()
