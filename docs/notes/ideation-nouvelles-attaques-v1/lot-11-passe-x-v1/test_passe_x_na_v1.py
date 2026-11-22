import hashlib, json, os, sys
from decimal import Decimal as D
import pytest
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import passe_x_na_v1 as P

PIECE = "/home/user/controle-ia-travail/docs/notes/ideation-nouvelles-attaques-v1/passe-x-piece-fusionnee-v1/piece-fusionnee-passe-x-v1.md"
CLE = "sk-FAUSSE-0123456789abcdef"
ENV = {"CLE_LUC": CLE, "CLE_G": CLE, "CLE_O": CLE, "CLE_K": CLE}
TEXTE_SECRET = "TEXTE-DE-REPONSE-QUI-NE-DOIT-JAMAIS-SORTIR"


def maillon(m, te=5, ts=25, n=96000, **k):
    d = {"modele": m, "tarif_entree": te, "tarif_sortie": ts, "sortie_max": n}; d.update(k); return d


def config(**k):
    g = {"espece": "argon", "niveau": "high", "provision": 49152}
    c = {"version": P.VERSION, "sous_parts": {"CLE_LUC": "72.60", "CLE_G": "12.10", "CLE_O": "6.05", "CLE_K": "6.05"},
         "proposeurs": [
             {"id": "espece_1", "fournisseur": "google", "cle_var": "CLE_G", "chaine": [maillon("gemini-4-argon", 4, 20, 65536, google=g)]},
             {"id": "espece_2", "fournisseur": "openai", "cle_var": "CLE_O", "chaine": [maillon("gpt-6-astra", 10, 50, 96000)]},
             {"id": "espece_3", "fournisseur": "anthropic", "cle_var": "CLE_LUC", "chaine": [maillon("claude-x"), maillon("claude-opus-4-6"), maillon("claude-sonnet-4-6", 3, 15)]},
             {"id": "ajout_kimi", "fournisseur": "kimi", "cle_var": "CLE_K", "chaine": [maillon("kimi-k3.1-pro", 2, 10, 96000)]},
         ]}
    c.update(k); return c


def flux_sain(f, m):
    if f == "anthropic":
        return [{"type": "message_start", "message": {"model": m, "usage": {"input_tokens": 7000}}},
                {"type": "content_block_delta", "delta": {"type": "thinking_delta", "thinking": "x"}},
                {"type": "content_block_delta", "delta": {"type": "text_delta", "text": TEXTE_SECRET}},
                {"type": "message_delta", "delta": {"stop_reason": "end_turn"}, "usage": {"output_tokens": 20000}}]
    if f in ("openai", "kimi"):
        return [{"model": m, "choices": [{"delta": {"content": TEXTE_SECRET}}]},
                {"model": m, "choices": [{"delta": {}, "finish_reason": "stop"}]},
                {"model": m, "choices": [], "usage": {"prompt_tokens": 7000, "completion_tokens": 20000}}]
    return [{"modelVersion": m, "candidates": [{"content": {"parts": [{"text": "p", "thought": True}, {"text": TEXTE_SECRET}]}}]},
            {"modelVersion": m, "candidates": [{"finishReason": "STOP", "content": {"parts": []}}],
             "usageMetadata": {"promptTokenCount": 7000, "candidatesTokenCount": 9000, "thoughtsTokenCount": 11000}}]


class Faux:
    def __init__(self, regles=None):
        self.regles, self.appels = regles or {}, []

    def __call__(self, url, ent, corps, brut):
        b = json.loads(corps)
        m = b.get("model") or url.split("/models/")[1].split(":")[0]
        f = "anthropic" if "anthropic" in url else "google" if "googleapis" in url else "kimi" if "moonshot" in url else "openai"
        self.appels.append((f, m, url, ent, b))
        regle = self.regles.get(m)
        if callable(regle):
            return regle(f, m, brut)
        evs = flux_sain(f, m)
        brut.write(json.dumps(evs).encode())
        return 200, iter(evs)


def passe(tmp_path, transport, c=None, env=ENV):
    piece = P.verifier_piece(PIECE)
    q = tmp_path / "q"; q.mkdir()
    return P.Passe(c or config(), piece, env, transport, str(q), str(tmp_path / "j.jsonl")), tmp_path


def lignes(tmp):
    return [json.loads(l) for l in open(tmp / "j.jsonl")]


# ---- cas sain ----
def test_cas_sain_tous_rendus_sans_texte_qui_sorte(tmp_path):
    t = Faux(); p, tmp = passe(tmp_path, t)
    r = p.courir(en_parallele=True)
    assert all(v == ["réponse rendue"] for v in r["classes"].values())
    assert not r["arret_13"]
    j = (tmp / "j.jsonl").read_text()
    assert TEXTE_SECRET not in j and TEXTE_SECRET not in json.dumps(r) and CLE not in j
    assert len(os.listdir(tmp / "q")) == 8  # 4 flux et leurs compagnons
    for l in lignes(tmp):
        b = open(tmp / "q" / f"{l['proposeur']}-rang-{l['rang_repli']}-{l['modele_demande']}.flux", "rb").read()
        assert hashlib.sha256(b).hexdigest() == l["flux_sha256"]
    # Google : flux, réflexion explicite ; requête = pièce seule, sans champ système
    g = [a for a in t.appels if a[0] == "google"][0]
    assert g[2].endswith(":streamGenerateContent?alt=sse") and g[4]["generationConfig"]["thinkingConfig"]["includeThoughts"]
    a = [a for a in t.appels if a[0] == "anthropic"][0]
    assert "system" not in a[4] and a[4]["messages"][0]["content"] == open(PIECE).read()
    assert D(r["total_usd"]) > 0


def test_cout_au_tarif(tmp_path):
    p, tmp = passe(tmp_path, Faux()); p.courir(False)
    l = [x for x in lignes(tmp) if x["proposeur"] == "espece_3"][0]
    assert D(l["cout_usd"]) == (D(7000) * 5 + D(20000) * 25) / D(10**6)


# ---- repli G9 ----
def refus(f, m, brut):
    evs = [{"type": "message_start", "message": {"model": m, "usage": {"input_tokens": 7000}}},
           {"type": "message_delta", "delta": {"stop_reason": "refusal"}, "usage": {"output_tokens": 3}}]
    brut.write(b"x"); return 200, iter(evs)


def test_repli_marque_sur_refus_de_classifieur(tmp_path):
    p, tmp = passe(tmp_path, Faux({"claude-x": refus, "claude-opus-4-6": refus}))
    r = p.courir(False)
    assert r["classes"]["espece_3"] == ["refus du modèle (classifieur)", "refus du modèle (classifieur)", "réponse rendue"]
    l = [x for x in lignes(tmp) if x["proposeur"] == "espece_3"]
    assert [x["par_repli"] for x in l] == [False, True, True] and l[2]["modele_servi"] == "claude-sonnet-4-6"


def test_pas_de_repli_sur_reponse_illisible(tmp_path):
    def coupe(f, m, brut):
        brut.write(b"x"); return 200, iter([{"type": "message_start", "message": {"model": m, "usage": {"input_tokens": 1}}},
                                            {"type": "message_delta", "delta": {"stop_reason": "max_tokens"}, "usage": {"output_tokens": 96000}}])
    p, tmp = passe(tmp_path, Faux({"claude-x": coupe}))
    assert p.courir(False)["classes"]["espece_3"] == ["réponse illisible"]


def test_config_refuse_un_repli_hors_claude():
    c = config(); c["proposeurs"][1]["chaine"].append(maillon("gpt-autre"))
    with pytest.raises(P.Refus):
        P.lire_configuration_objet = None
        _ecrire_et_lire(c)


def _ecrire_et_lire(c, tmp=None):
    import tempfile
    d = tempfile.mkdtemp(); ch = os.path.join(d, "c.json")
    b = json.dumps(c).encode(); open(ch, "wb").write(b)
    open(ch + ".sha256", "w").write(hashlib.sha256(b).hexdigest() + "  c.json\n")
    return P.lire_configuration(ch)


def test_config_saine_lue():
    assert _ecrire_et_lire(config())["version"] == P.VERSION


@pytest.mark.parametrize("alterer", [
    lambda c: c.update(sous_parts=dict(c["sous_parts"], CLE_LUC="90")),
    lambda c: c["proposeurs"][0].update(fournisseur="ailleurs"),
    lambda c: c["proposeurs"][2]["chaine"][0].update(extras={"system": "x"}),
    lambda c: c["proposeurs"][1]["chaine"][0].update(google={"espece": "argon"}),
    lambda c: c["proposeurs"][0]["chaine"][0].pop("google"),
    lambda c: c["proposeurs"].append(dict(c["proposeurs"][0])),
    lambda c: c["proposeurs"][3].update(cle_var="CLE_INCONNUE"),
    lambda c: c.update(autre=1),
])
def test_config_artefacts_refuses(alterer):
    c = config(); alterer(c)
    with pytest.raises(P.Refus):
        _ecrire_et_lire(c)


def test_config_empreinte_alteree(tmp_path):
    ch = tmp_path / "c.json"; ch.write_text(json.dumps(config()))
    (tmp_path / "c.json.sha256").write_text("0" * 64 + "  c.json\n")
    with pytest.raises(P.Refus):
        P.lire_configuration(str(ch))


# ---- G1 pièce ----
def test_piece_alteree_refusee(tmp_path):
    b = open(PIECE, "rb").read(); f = tmp_path / "p.md"; f.write_bytes(b[:-1] + b"X")
    with pytest.raises(P.Refus):
        P.verifier_piece(str(f))


def test_piece_saine():
    assert hashlib.sha256(P.verifier_piece(PIECE)).hexdigest() == P.EMPREINTE_PIECE


def test_garde_motifs_mord(monkeypatch):
    monkeypatch.setattr(P, "garde_motifs_ligne", lambda l: ["motif"] if l else [])
    with pytest.raises(P.Refus):
        P.verifier_piece(PIECE)


# ---- G3 GO ----
def test_go(tmp_path):
    r = tmp_path / "go.md"
    r.write_text("".join(f"| {g} | x |\n" for g in P.GO_EXIGES))
    P.verifier_go(str(r))
    r.write_text("| GO-2026-11-22-46 | x |\n")
    with pytest.raises(P.Refus):
        P.verifier_go(str(r))


# ---- G5, G6, G11 ----
def test_pire_au_dela_de_6_05_refuse(tmp_path):
    c = config(); c["proposeurs"][2]["chaine"][0]["tarif_sortie"] = 75
    with pytest.raises(P.Refus):
        passe(tmp_path, Faux(), c)


def test_google_garde_refuse_96000(tmp_path):
    c = config(); c["proposeurs"][0]["chaine"][0]["sortie_max"] = 96000
    with pytest.raises(P.Refus, match="G6"):
        passe(tmp_path, Faux(), c)


def test_google_garde_refuse_niveau_bas(tmp_path):
    c = config(); c["proposeurs"][0]["chaine"][0]["google"]["niveau"] = "low"
    with pytest.raises(P.Refus, match="G6"):
        passe(tmp_path, Faux(), c)


def test_cle_absente_refuse(tmp_path):
    with pytest.raises(P.Refus, match="G11"):
        passe(tmp_path, Faux(), env={"CLE_LUC": CLE})


@pytest.mark.parametrize("evs", [
    [{"modelVersion": "gemini-4-argon", "candidates": [{"finishReason": "STOP", "content": {"parts": [{"text": "t"}]}}],
      "usageMetadata": {"promptTokenCount": 1, "candidatesTokenCount": 1, "thoughtsTokenCount": 0}}],
    [{"modelVersion": "gemini-4-argon", "candidates": [{"finishReason": "SAFETY"}]}],
    [{"modelVersion": "gemini-4-argon", "candidates": [{"finishReason": "MAX_TOKENS", "content": {"parts": [{"text": "t"}]}}]}],
    [{"promptFeedback": {"blockReason": "OTHER"}}],
])
def test_google_defauts_jamais_une_reponse(tmp_path, evs):
    def r(f, m, brut):
        brut.write(b"x"); return 200, iter(evs)
    p, tmp = passe(tmp_path, Faux({"gemini-4-argon": r}))
    assert p.courir(False)["classes"]["espece_1"] == ["défaut Google"]


# ---- G7 arrêt n° 12 ----
def test_arret_12_sous_part_trop_basse(tmp_path):
    c = config(); c["sous_parts"]["CLE_LUC"] = "1.00"
    t = Faux(); p, tmp = passe(tmp_path, t, c)
    r = p.courir(False)
    assert r["classes"]["espece_3"] == ["refusée avant envoi (arrêt n° 12)"]
    assert not any(a[1] == "claude-x" for a in t.appels)


def test_arret_12_compte_le_repli(tmp_path):
    c = config(); c["sous_parts"]["CLE_LUC"] = "1.00"
    c["proposeurs"][2]["chaine"] = [maillon("claude-x", 5, 25, 10000), maillon("claude-opus-4-6", 5, 25, 96000)]
    p, tmp = passe(tmp_path, Faux({"claude-x": refus}), c)
    assert p.courir(False)["classes"]["espece_3"] == ["refus du modèle (classifieur)", "refusée avant envoi (arrêt n° 12)"]


# ---- G8 arrêt n° 13 ----
def credit(f, m, brut):
    b = {"type": "error", "error": {"type": "invalid_request_error", "message": "Your credit balance is too low to access the Anthropic API. sk-FA"}}
    brut.write(json.dumps(b).encode()); return 400, iter([b])


def test_arret_13_arrete_la_passe(tmp_path):
    t = Faux({"claude-x": credit}); p, tmp = passe(tmp_path, t)
    r = p.courir(False)   # ordre : espece_1, espece_2, espece_3 (crédit), ajout_kimi
    assert r["arret_13"] and r["classes"]["espece_3"] == ["crédit épuisé"]
    assert r["classes"]["ajout_kimi"] == ["non partie (arrêt n° 13)"]
    assert not any(a[0] == "kimi" for a in t.appels)
    assert "credit balance" not in (tmp / "j.jsonl").read_text() and "sk-FA" not in (tmp / "j.jsonl").read_text()


@pytest.mark.parametrize("statut,corps", [
    (429, {"error": {"type": "exceeded_current_quota_error", "message": "x"}}),
    (429, {"error": {"type": "insufficient_quota", "code": "insufficient_quota"}}),
])
def test_credit_kimi_openai(tmp_path, statut, corps):
    def r(f, m, brut):
        brut.write(b"x"); return statut, iter([corps])
    p, tmp = passe(tmp_path, Faux({"kimi-k3.1-pro": r}))
    assert p.courir(False)["classes"]["ajout_kimi"] == ["crédit épuisé"]


def test_erreur_de_requete_cout_nul(tmp_path):
    def r(f, m, brut):
        brut.write(b"x"); return 400, iter([{"error": {"type": "invalid_request_error", "message": "bad"}}])
    p, tmp = passe(tmp_path, Faux({"gpt-6-astra": r}))
    p.courir(False)
    l = [x for x in lignes(tmp) if x["proposeur"] == "espece_2"][0]
    assert l["classe"] == "erreur de requête" and l["cout_usd"] == "0.000000"


# ---- G12, A3 ----
def test_modele_substitue(tmp_path):
    def r(f, m, brut):
        evs = flux_sain(f, "kimi-autre"); brut.write(b"x"); return 200, iter(evs)
    p, tmp = passe(tmp_path, Faux({"kimi-k3.1-pro": r}))
    assert p.courir(False)["classes"]["ajout_kimi"] == ["modèle substitué"]


def test_flux_coupe_cout_au_pire(tmp_path):
    def r(f, m, brut):
        def gen():
            yield {"model": m, "choices": [{"delta": {"content": "a"}}]}
            raise ConnectionResetError("coupé")
        brut.write(b"x"); return 200, gen()
    p, tmp = passe(tmp_path, Faux({"gpt-6-astra": r}))
    p.courir(False)
    l = [x for x in lignes(tmp) if x["proposeur"] == "espece_2"][0]
    assert l["classe"] == "injoignable" and l["cout_usd"] == l["pire_usd"]


def test_usage_absent_cout_au_pire(tmp_path):
    def r(f, m, brut):
        evs = flux_sain(f, m)[:2]; brut.write(b"x"); return 200, iter(evs)
    p, tmp = passe(tmp_path, Faux({"kimi-k3.1-pro": r}))
    p.courir(False)
    l = [x for x in lignes(tmp) if x["proposeur"] == "ajout_kimi"][0]
    assert l["cout_inconnu"] and l["cout_usd"] == l["pire_usd"]


# ---- G10 quarantaine, R12 ----
def test_quarantaine_jamais_ecrasee(tmp_path):
    p, tmp = passe(tmp_path, Faux())
    (tmp / "q" / "espece_2-rang-0-gpt-6-astra.flux").write_bytes(b"ancien")
    with pytest.raises(FileExistsError):
        p.tentative(p.c["proposeurs"][1], 0, p.c["proposeurs"][1]["chaine"][0])
    assert (tmp / "q" / "espece_2-rang-0-gpt-6-astra.flux").read_bytes() == b"ancien"


def test_main_a_blanc_et_refus_journal_present(tmp_path, monkeypatch, capsys):
    for k, v in ENV.items():
        monkeypatch.setenv(k, v)
    ch = tmp_path / "c.json"; b = json.dumps(config()).encode(); ch.write_bytes(b)
    (tmp_path / "c.json.sha256").write_text(hashlib.sha256(b).hexdigest() + "  c.json\n")
    reg = tmp_path / "go.md"; reg.write_text("".join(f"| {g} | x |\n" for g in P.GO_EXIGES))
    monkeypatch.setattr(P, "transport_reel", lambda *a: pytest.fail("aucun envoi à blanc"))
    monkeypatch.setattr(P.GD, "transport_reel", lambda *a: pytest.fail("aucun envoi à blanc"))
    arg = ["--piece", PIECE, "--configuration", str(ch), "--plan-garde", "x", "--quarantaine", str(tmp_path / "q"),
           "--journal", str(tmp_path / "j.jsonl"), "--registre-go", str(reg)]
    assert P.main(arg) == 0 and "conforme" in capsys.readouterr().out
    (tmp_path / "j.jsonl").write_text("x")
    assert P.main(arg) == 2


def test_main_garde_de_depart_manque_rien_ne_part(tmp_path, monkeypatch):
    for k, v in ENV.items():
        monkeypatch.setenv(k, v)
    ch = tmp_path / "c.json"; b = json.dumps(config()).encode(); ch.write_bytes(b)
    (tmp_path / "c.json.sha256").write_text(hashlib.sha256(b).hexdigest() + "  c.json\n")
    reg = tmp_path / "go.md"; reg.write_text("".join(f"| {g} | x |\n" for g in P.GO_EXIGES))
    plan = tmp_path / "plan.json"
    plan.write_text(json.dumps([{"cle_var": "CLE_LUC", "fournisseur": "anthropic", "modele": "claude-opus-4-6",
                                 "tarif_entree_usd_par_million": 5, "tarif_sortie_usd_par_million": 25}]))
    monkeypatch.setattr(P.GD, "transport_reel", lambda *a: (400, b'{"error":{"message":"credit balance is too low"}}'))
    monkeypatch.setattr(P, "transport_reel", lambda *a: pytest.fail("rien ne doit partir"))
    arg = ["--piece", PIECE, "--configuration", str(ch), "--plan-garde", str(plan), "--quarantaine", str(tmp_path / "q"),
           "--journal", str(tmp_path / "j.jsonl"), "--registre-go", str(reg), "--reel"]
    assert P.main(arg) == 2


# ---- transport réel contre un serveur local (flux SSE, erreur HTTP) ----
import http.server, threading, io


class _Serveur(http.server.BaseHTTPRequestHandler):
    def log_message(self, *a):
        pass

    def do_POST(self):
        self.rfile.read(int(self.headers["content-length"]))
        if self.path.startswith("/erreur"):
            b = json.dumps({"error": {"type": "invalid_request_error", "message": "credit balance is too low"}}).encode()
            self.send_response(400); self.send_header("content-length", str(len(b))); self.end_headers(); self.wfile.write(b)
            return
        self.send_response(200); self.send_header("content-type", "text/event-stream"); self.end_headers()
        for e in flux_sain("openai", "gpt-6-astra"):
            self.wfile.write(b"data: " + json.dumps(e).encode() + b"\n\n")
        self.wfile.write(b"data: [DONE]\n\n")


def test_transport_reel_local(monkeypatch):
    monkeypatch.setenv("no_proxy", "127.0.0.1"); monkeypatch.setenv("NO_PROXY", "127.0.0.1")
    s = http.server.ThreadingHTTPServer(("127.0.0.1", 0), _Serveur)
    threading.Thread(target=s.serve_forever, daemon=True).start()
    try:
        url = f"http://127.0.0.1:{s.server_port}"
        brut = io.BytesIO()
        st, evs = P.transport_reel(url + "/flux", {"content-type": "application/json"}, b"{}", brut)
        r = P.lire_flux("openai", evs)
        assert st == 200 and r["texte"] == TEXTE_SECRET and r["fin"] == "stop" and r["sortie"] == 20000
        assert b"[DONE]" in brut.getvalue()
        brut2 = io.BytesIO()
        st, evs = P.transport_reel(url + "/erreur", {"content-type": "application/json"}, b"{}", brut2)
        r = P.lire_flux("openai", evs)
        assert st == 400 and r["credit"] and "credit balance" not in json.dumps({k: v for k, v in r.items() if k != "texte"})
    finally:
        s.shutdown()
