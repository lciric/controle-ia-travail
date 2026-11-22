import sys, os, json, io, tempfile, importlib.util, urllib.error, contextlib, datetime as dt
P = "/home/user/controle-ia-travail/docs/notes/memoire-conception-v1/appel-google-garde-v3-v2/appel_google_garde_v3_v2.py"
spec = importlib.util.spec_from_file_location("s", P); s = importlib.util.module_from_spec(spec); spec.loader.exec_module(s)
os.environ["GEMINI_API_KEY"] = "CLE-FACTICE-123"
JOUR = dt.datetime(2026, 11, 22, 13, 0, tzinfo=dt.timezone.utc)
class R:
    def __init__(self, l): self.l, self.status = l, 200
    def __enter__(self): return self
    def __exit__(self, *a): return False
    def __iter__(self): return iter([x.encode() for x in self.l])
def flux(*c): return ["data: " + (x if isinstance(x, str) else json.dumps(x)) for x in c]
def ch(text=None, fin=None, thought=False, usage=None, model="gemini-4-argon"):
    c = {"content": {"parts": [{"text": text, "thought": thought}] if text is not None else []}}
    if fin: c["finishReason"] = fin
    d = {"modelVersion": model, "responseId": "r", "candidates": [c]}
    if usage: d["usageMetadata"] = usage
    return d
U = {"promptTokenCount": 100, "candidatesTokenCount": 50, "thoughtsTokenCount": 30}
E = "Question de test. Réponds en 400 mots au plus."
def run(nom, lignes=None, enonce=E, exc=None, extra=(), journal_txt=None, quand=JOUR, d=None):
    envoye = []
    def fake(req, timeout=None):
        envoye.append(1)
        if exc: raise exc
        return R(lignes)
    d = d or tempfile.mkdtemp(); e = os.path.join(d, "e.md"); open(e, "w").write(enonce)
    j = os.path.join(d, "j.jsonl")
    if journal_txt is not None: open(j, "w").write(journal_txt)
    k = len([x for x in os.listdir(d) if x.startswith("o")]) 
    out = os.path.join(d, f"o{k}")
    err = io.StringIO()
    try:
        with contextlib.redirect_stderr(err), contextlib.redirect_stdout(io.StringIO()):
            rc = s.main(["argon", e, out + ".md", out + ".json", "--journal", j, *extra], ouvrir=fake, maintenant=quand)
    except Exception as x:
        rc = f"EXC {type(x).__name__}: {x}"
    m = json.load(open(out + ".json")) if os.path.exists(out + ".json") else {}
    print(f"{nom:52s} rc={rc} envoye={bool(envoye)} defaut={m.get('defaut')} compte={m.get('cout_compte_usd')} {err.getvalue().strip()[:100]}")
    return d, m
run("M1 sain", flux(ch("pense", thought=True), ch("Réponse."), ch("", fin="STOP", usage=U)))
run("M2 MAX_TOKENS", flux(ch("x"), ch("", fin="MAX_TOKENS", usage=U)))
run("M3 zero pensee", flux(ch("x"), ch("", fin="STOP", usage={**U, "thoughtsTokenCount": 0})))
run("M3b usage absent", flux(ch("x"), ch("", fin="STOP")))
run("M4 JSON casse au milieu", flux(ch("Debut. "), '{"candidates": [{"content": {"parts": [{"text": "PERDU', ch("Fin.", fin="STOP", usage=U)))
run("M5 error en flux puis STOP", flux(ch("x"), {"error": {"code": 500}}, ch("y", fin="STOP", usage=U)))
run("M6 servi carbon", flux(ch("x", model="gemini-4-carbon"), ch("", fin="STOP", usage=U, model="gemini-4-carbon")))
run("M7 SAFETY", flux(ch("x"), ch("", fin="SAFETY", usage=U)))
run("M8 flux coupe sans fin (usage partiel)", flux(ch("x", usage={"promptTokenCount": 100, "candidatesTokenCount": 5, "thoughtsTokenCount": 10})))
run("M9 blocage invite", flux({"promptFeedback": {"blockReason": "SAFETY"}, "usageMetadata": U, "modelVersion": "gemini-4-argon"}))
run("M10 3300 mots", flux(ch("x", fin="STOP", usage=U)), enonce="En 3300 mots.")
run("M11 3212 mots", flux(ch("x", thought=False), ch("", fin="STOP", usage=U)), enonce="En 3212 mots.")
run("M12 --mots 0 / enonce 5000 mots", flux(ch("x", fin="STOP", usage=U)), enonce="Réponds en 5000 mots.", extra=["--mots", "0"])
run("M13 HTTP 400 cle masquee", exc=urllib.error.HTTPError("u", 400, "b", {}, io.BytesIO(b"thinkingLevel CLE-FACTICE-123")))
run("M14 URLError", exc=urllib.error.URLError("refus CLE-FACTICE-123"))
run("M15 enonce 3e6 signes", flux(ch("x", fin="STOP", usage=U)), enonce=("a" * 79 + "\n") * 30_000 + " 400 mots")
run("M16 courriel et session_", flux(ch("x", fin="STOP", usage=U)), enonce=E + " a@b.fr session_0123456789abcdefghijKLMN")
# nouvelles
run("N1 servi gemini-4-argon-lite (autre modele?)", flux(ch("x", model="gemini-4-argon-lite"), ch("", fin="STOP", usage=U, model="gemini-4-argon-lite")))
run("N2 journal NaN", flux(ch("x"), ch("", fin="STOP", usage=U)), journal_txt='{"cout_compte_usd": NaN}\n')
run("N3 journal valeur negative -100", flux(ch("x"), ch("", fin="STOP", usage=U)), journal_txt='{"cout_compte_usd": -100}\n{"cout_compte_usd": 2.9}\n')
run("N4 journal Infinity", flux(ch("x", fin="STOP", usage=U)), journal_txt='{"cout_compte_usd": Infinity}\n')
run("N5 limite en lettres + '3 mots-cles'", flux(ch("x"), ch("", fin="STOP", usage=U)), enonce="Réponds en dix mille mots ; garde les 3 mots-clés.")
run("N6 '2 000 mots' espace insecable", flux(ch("x"), ch("", fin="STOP", usage=U)), enonce="Réponds en 2 000 mots.")
run("N7 'fiche 12 2000 mots' (concatene)", flux(ch("x"), ch("", fin="STOP", usage=U)), enonce="Voir fiche 12 2000 mots au plus.")
run("N8 30 nov 20:00Z tarif", flux(ch("x"), ch("", fin="STOP", usage=U)), quand=dt.datetime(2026, 11, 30, 23, 0, tzinfo=dt.timezone.utc))
run("N9 candidates contient une chaine", flux({"candidates": ["x"], "modelVersion": "gemini-4-argon"}))
run("N10 part text None", flux(ch(None), {"candidates": [{"content": {"parts": [{"text": None}]}, "finishReason": "STOP"}], "usageMetadata": U, "modelVersion": "gemini-4-argon"}))
run("N11 --plafond-usd nan", flux(ch("x", fin="STOP", usage=U)), extra=["--plafond-usd", "nan"])
# cumul : 4 appels sequentiels sur le meme journal
d = tempfile.mkdtemp()
for i in range(4):
    run(f"N12 appel {i+1} meme journal", flux(ch("x"), ch("", fin="MAX_TOKENS")), d=d)
print(open(os.path.join(d, "j.jsonl")).read())
d2 = tempfile.mkdtemp()
for i in range(4):
    run(f"N13 apres bascule appel {i+1}", flux(ch("x")), d=d2, quand=dt.datetime(2026, 12, 2, tzinfo=dt.timezone.utc))
