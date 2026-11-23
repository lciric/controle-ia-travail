import base64, os, subprocess, sys
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
RACINE, JETON = sys.argv[1], sys.argv[2]
ATTENDU = "Basic " + base64.b64encode(f"x-access-token:{JETON}".encode()).decode()
class H(BaseHTTPRequestHandler):
    def log_message(self, *a): pass
    def _servir(self):
        if self.headers.get("Authorization") != ATTENDU:
            self.send_response(401); self.send_header("WWW-Authenticate", 'Basic realm="essai"'); self.send_header("Content-Length", "0"); self.end_headers(); return
        chemin, _, requete = self.path.partition("?")
        corps = self.rfile.read(int(self.headers.get("Content-Length") or 0)) if self.command == "POST" else b""
        env = {"PATH": os.environ["PATH"], "GIT_PROJECT_ROOT": RACINE, "GIT_HTTP_EXPORT_ALL": "1", "PATH_INFO": chemin,
               "QUERY_STRING": requete, "REQUEST_METHOD": self.command, "REMOTE_USER": "x-access-token", "REMOTE_ADDR": "127.0.0.1",
               "CONTENT_TYPE": self.headers.get("Content-Type", ""), "CONTENT_LENGTH": str(len(corps)),
               "GIT_PROTOCOL": self.headers.get("Git-Protocol", ""), "HTTP_CONTENT_ENCODING": self.headers.get("Content-Encoding", "")}
        p = subprocess.run(["git", "http-backend"], input=corps, env=env, capture_output=True)
        tete, _, reste = p.stdout.partition(b"\r\n\r\n")
        statut = 200; entetes = []
        for l in tete.decode().split("\r\n"):
            k, _, v = l.partition(":")
            if k.lower() == "status": statut = int(v.split()[0])
            elif k: entetes.append((k, v.strip()))
        self.send_response(statut)
        for k, v in entetes: self.send_header(k, v)
        self.send_header("Content-Length", str(len(reste))); self.end_headers(); self.wfile.write(reste)
    do_GET = do_POST = _servir
s = ThreadingHTTPServer(("127.0.0.1", 0), H); print(s.server_address[1], flush=True); s.serve_forever()
