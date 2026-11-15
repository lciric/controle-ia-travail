import json, http.server, sys
C=json.load(open(sys.argv[1]))["proposeurs"]
class H(http.server.BaseHTTPRequestHandler):
    def do_POST(self):
        n=int(self.headers["Content-Length"]); self.rfile.read(n)
        d=self.path.strip("/")
        if d=="claude": r={"model":C["opus55"]["modele"],"usage":{"input_tokens":15,"output_tokens":3}}
        elif d=="gemini": r={"modelVersion":C["argon"]["modele"],"usageMetadata":{"promptTokenCount":9,"candidatesTokenCount":2}}
        else: r={"model":C["astra"]["modele"]+"-2026","usage":{"prompt_tokens":12,"completion_tokens":5}}
        b=json.dumps(r).encode(); self.send_response(200); self.send_header("Content-Length",str(len(b))); self.end_headers(); self.wfile.write(b)
    def log_message(self,*a): pass
http.server.HTTPServer(("127.0.0.1",8899),H).serve_forever()
