import sys, os, json, io, tempfile, importlib.util, urllib.request, urllib.error
sys.path.insert(0, "/home/user/controle-ia-travail/src")
spec = importlib.util.spec_from_file_location("s", sys.argv[1]); s = importlib.util.module_from_spec(spec); spec.loader.exec_module(s)
os.environ["GEMINI_API_KEY"] = "CLE-FACTICE-123"
envoye = []
class R:
    def __init__(self, lignes, status=200): self.l, self.status = lignes, status
    def __enter__(self): return self
    def __exit__(self, *a): return False
    def __iter__(self): return iter([x.encode() for x in self.l])
def flux(*chunks): return ["data: " + (c if isinstance(c, str) else json.dumps(c)) for c in chunks]
def ch(text=None, fin=None, thought=False, usage=None, model="gemini-4-argon"):
    d = {"modelVersion": model, "responseId": "r"}
    parts = [{"text": text, "thought": thought}] if text is not None else []
    c = {"content": {"parts": parts}}
    if fin: c["finishReason"] = fin
    d["candidates"] = [c]
    if usage: d["usageMetadata"] = usage
    return d
U = {"promptTokenCount": 100, "candidatesTokenCount": 50, "thoughtsTokenCount": 30}
def run(nom, lignes=None, mots=400, enonce="Question de test. 400 mots au plus.", exc=None):
    def fake(req, timeout=None):
        envoye.append(req)
        if exc: raise exc
        return R(lignes)
    urllib.request.urlopen = fake
    d = tempfile.mkdtemp(); e = os.path.join(d, "e.md"); open(e, "w").write(enonce)
    n0 = len(envoye)
    import contextlib
    err = io.StringIO()
    with contextlib.redirect_stderr(err), contextlib.redirect_stdout(io.StringIO()):
        rc = s.main(["argon", e, d + "/o.md", d + "/o.json", "--mots", str(mots)])
    meta = json.load(open(d + "/o.json")) if os.path.exists(d + "/o.json") else {}
    print(f"{nom:45s} rc={rc} envoye={len(envoye)>n0} defaut={meta.get('defaut')} verdict={meta.get('verdict')} {err.getvalue().strip()[:110]}")
run("M1 sain STOP + pensees", flux(ch("pense", thought=True), ch("Réponse."), ch("", fin="STOP", usage=U)))
run("M2 MAX_TOKENS", flux(ch("x"), ch("", fin="MAX_TOKENS", usage=U)))
run("M3 zero pensee", flux(ch("x"), ch("", fin="STOP", usage={**U, "thoughtsTokenCount": 0})))
run("M3b usage absent", flux(ch("x"), ch("", fin="STOP")))
run("M4 morceau JSON casse au milieu (texte perdu)", flux(ch("Debut. "), '{"candidates": [{"content": {"parts": [{"text": "MILIEU PERDU', ch("Fin.", fin="STOP", usage=U)))
run("M5 objet error en flux puis STOP", flux(ch("x"), {"error": {"code": 500, "message": "interne"}}, ch("y", fin="STOP", usage=U)))
run("M6 modele servi different", flux(ch("x", model="gemini-4-carbon"), ch("", fin="STOP", usage=U, model="gemini-4-carbon")))
run("M7 SAFETY", flux(ch("x"), ch("", fin="SAFETY", usage=U)))
run("M8 flux coupe sans fin", flux(ch("x", usage=U)))
run("M9 blocage invite", flux({"promptFeedback": {"blockReason": "SAFETY"}, "usageMetadata": U}))
run("M10 mots 3300 (>16384/5.1)", flux(ch("x", fin="STOP", usage=U)), mots=3300)
run("M11 mots 3212 (limite)", flux(ch("x", fin="STOP", usage=U)), mots=3212)
run("M12 mots 0 alors que l'enonce dit 5000 mots", flux(ch("x"), ch("", fin="STOP", usage=U)), mots=0, enonce="Reponds en 5000 mots.")
run("M13 HTTP 400", exc=urllib.error.HTTPError("u", 400, "bad", {}, io.BytesIO(b'{"error":"thinkingLevel CLE-FACTICE-123"}')))
run("M14 URLError", exc=urllib.error.URLError("refus"))
run("M15 enonce 3e6 signes (pire cas)", flux(ch("x", fin="STOP", usage=U)), enonce="a"*3_000_000)
run("M16 enonce avec courriel et session_", flux(ch("x"), ch("", fin="STOP", usage=U)), enonce="contact a@b.fr session_0123456789abcdefghijKLMN")
del os.environ["GEMINI_API_KEY"]
run("M17 cle absente", flux(ch("x", fin="STOP", usage=U)))
r = envoye[0]; print("en-tetes:", sorted(r.headers), "corps:", json.loads(r.data)["generationConfig"])
