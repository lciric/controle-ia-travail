import http.server,sys
class H(http.server.BaseHTTPRequestHandler):
    def do_PUT(self): self.r()
    def do_DELETE(self): self.r()
    def r(self):
        n=int(self.headers.get("Content-Length") or 0); b=self.rfile.read(n)
        open(sys.argv[2],"a").write(f"{self.command} {self.path} auth={self.headers.get('Authorization')} body={b!r}\n")
        self.send_response(200); self.end_headers()
    def log_message(self,*a): pass
s=http.server.HTTPServer(("127.0.0.1",int(sys.argv[1])),H); s.handle_request(); s.handle_request()
