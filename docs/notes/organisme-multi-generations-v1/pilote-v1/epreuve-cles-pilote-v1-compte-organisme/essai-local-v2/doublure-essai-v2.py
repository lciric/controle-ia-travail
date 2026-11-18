"""Doublure locale des essais de l'épreuve v2 : le scénario est lu dans le fichier SCENARIO ; compte les requêtes reçues."""
import json, http.server, sys
C = json.load(open(sys.argv[1]))["proposeurs"]; S = sys.argv[2]; N = sys.argv[3]
def scen(): return open(S).read().strip()
class H(http.server.BaseHTTPRequestHandler):
    def _compte(self):
        open(N, "a").write(self.command + " " + self.path + "\n")
    def do_GET(self):
        self._compte(); self.send_response(200); self.end_headers(); self.wfile.write(b"{}")
    def do_POST(self):
        self._compte(); n = int(self.headers["Content-Length"]); self.rfile.read(n)
        d = self.path.strip("/"); s = scen()
        if s == "401" and d == "astra": self.send_response(401); self.end_headers(); self.wfile.write(b'{"secret":"CORPS-ERREUR"}'); return
        if s == "302" and d == "gemini": self.send_response(302); self.send_header("Location", "/ailleurs"); self.end_headers(); return
        if s == "illisible" and d == "gemini": self.send_response(200); self.end_headers(); self.wfile.write(b"pas du json"); return
        mo = {"claude": C["opus55"]["modele"], "gemini": C["argon"]["modele"], "astra": C["astra"]["modele"] + "-2026-05-01"}[d]
        if s == "mini" and d == "astra": mo = C["astra"]["modele"] + "-mini"
        if d == "claude": r = {"model": mo, "usage": {"input_tokens": 15, "output_tokens": 3}}
        elif d == "gemini":
            u = {"promptTokenCount": 9, "candidatesTokenCount": 2}
            if s == "reflexion": u["thoughtsTokenCount"] = 32000
            r = {"modelVersion": mo, "usageMetadata": u}
            if s == "sansusage": r = {"modelVersion": mo}
        else: r = {"model": mo, "usage": {"prompt_tokens": 12, "completion_tokens": 5}}
        b = json.dumps(r).encode(); self.send_response(200); self.send_header("Content-Length", str(len(b))); self.end_headers(); self.wfile.write(b)
    def log_message(self, *a): pass
http.server.HTTPServer(("127.0.0.1", 8898), H).serve_forever()
