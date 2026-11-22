import json, threading, sys, os, tempfile
from http.server import BaseHTTPRequestHandler, HTTPServer
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "copie", "orchestrator"))
from pole import adaptateur_claude_direct_na_v1 as ad
VUS = []
CAS = {}
class H(BaseHTTPRequestHandler):
    def log_message(self, *a): pass
    def do_POST(self):
        n = int(self.headers.get("content-length", 0)); self.rfile.read(n)
        VUS.append({k.lower(): ("<jeton>" if k.lower() in ("x-api-key","authorization") else v) for k, v in self.headers.items() if k.lower() in ("x-api-key","authorization","anthropic-beta")}|{"_cles":sorted(k.lower() for k in self.headers.keys() if k.lower() in ("x-api-key","authorization"))} | {"_x_val_eq_jeton": self.headers.get("x-api-key")==ad.JETON_FACTICE, "_auth": self.headers.get("authorization"), "_nb_xkey": len(self.headers.get_all("x-api-key") or [])})
        st, corps = CAS["cas"]
        b = json.dumps(corps).encode()
        self.send_response(st); self.send_header("content-type","application/json"); self.send_header("content-length", str(len(b))); self.end_headers(); self.wfile.write(b)
srv = HTTPServer(("127.0.0.1", 0), H); threading.Thread(target=srv.serve_forever, daemon=True).start()
url = f"http://127.0.0.1:{srv.server_port}"
M = ["m-role", "m-r1", "m-r2"]
reg = {r: {m: {"max_tokens": 100, "effort": None, "reflexion": "omise", "flux": False} for m in M} for r in ad.ROLES_NA}
adm = {m: {"max_tokens_max": 1000, "efforts": [], "reflexions": ["omise"]} for m in M}
bar = {m: [1, 1, 1, 1] for m in M}
d = tempfile.mkdtemp(); sess = tempfile.mkdtemp(dir=d)
a = ad.AdaptateurClaudeDirectNA(url, d, modeles_admis=M, reglages=reg, admis=adm, bareme=bar, environnement={}, arme=True)
msg = "Your credit balance is too low to access the Anthropic API. Please go to Plans & Billing to upgrade or purchase credits."
cas = {
 "400 invalid_request_error credit too low": (400, {"type":"error","error":{"type":"invalid_request_error","message":msg}}),
 "402 billing_error (controle)": (402, {"type":"error","error":{"type":"billing_error","message":msg}}),
 "429 rate_limit spend (controle)": (429, {"type":"error","error":{"type":"rate_limit_error","message":"spend limit"}}),
}
for nom, c in cas.items():
    CAS["cas"] = c; VUS.clear()
    r = a.lancer("proposeur_ideation", "bonjour", sess, 1.0, 1, modele="m-role")
    t = r.tentative
    print(nom, "->", t["classe_erreur"], t["statut_http"], t["type_erreur"], "| credit?", t["classe_erreur"] in (ad.ERREUR_CREDIT_AMONT, ad.ERREUR_PLAFOND_RELAIS), "| requetes:", len(VUS))
print("entetes vus:", VUS[0])
