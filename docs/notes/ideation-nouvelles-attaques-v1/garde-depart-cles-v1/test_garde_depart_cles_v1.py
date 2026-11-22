import json, os, sys
import pytest
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import garde_depart_cles_v1 as g

CLE = "sk-FAUSSE-CLE-0123456789"
def couple(f="anthropic", m="claude-opus-4-6", **k):
    c = {"cle_var": "CLE_ESSAI", "fournisseur": f, "modele": m,
         "tarif_entree_usd_par_million": 5.0, "tarif_sortie_usd_par_million": 25.0}
    c.update(k); return c
ENV = {"CLE_ESSAI": CLE}

def faux(statut, corps, vus=None):
    def t(url, h, b):
        if vus is not None: vus.append((url, h, b))
        return statut, (corps if isinstance(corps, bytes) else json.dumps(corps).encode())
    return t

OK = {"anthropic": {"model": "claude-opus-4-6", "usage": {"input_tokens": 8, "output_tokens": 1}},
      "openai": {"model": "gpt-5", "usage": {"prompt_tokens": 8, "completion_tokens": 1}},
      "kimi": {"model": "kimi-k2", "usage": {"prompt_tokens": 8, "completion_tokens": 1}},
      "google": {"modelVersion": "gemini-3-pro", "usageMetadata": {"promptTokenCount": 2, "candidatesTokenCount": 1}}}
MODELES = {"anthropic": "claude-opus-4-6", "openai": "gpt-5", "kimi": "kimi-k2", "google": "gemini-3-pro"}

@pytest.mark.parametrize("f", list(OK))
def test_cas_sain_pret(f):
    vus = []
    l = g.essayer(couple(f, MODELES[f]), ENV, faux(200, OK[f], vus))
    assert l["verdict"] == "prêt" and l["raison"] == "prêt" and l["cout_usd"] > 0
    url, h, b = vus[0]
    assert url.startswith(g.HOTES[f].split("{")[0])
    assert json.loads(b).get("max_tokens", 1) == 1
    assert CLE not in json.dumps(l)

@pytest.mark.parametrize("statut,corps,raison", [
    (400, {"type": "error", "error": {"type": "invalid_request_error", "message": "Your credit balance is too low to access the Anthropic API."}}, "crédit épuisé"),
    (429, {"error": {"type": "insufficient_quota", "code": "insufficient_quota", "message": "You exceeded your current quota"}}, "crédit épuisé"),
    (429, {"error": {"type": "exceeded_current_quota_error", "message": "x"}}, "crédit épuisé"),
    (402, {"error": {"message": "pay"}}, "crédit épuisé"),
    (401, {"error": {"type": "authentication_error", "message": "Incorrect API key provided: sk-FA***789"}}, "accès refusé"),
    (403, {"error": {"type": "permission_error"}}, "accès refusé"),
    (404, {"error": {"type": "not_found_error", "message": "model: x"}}, "modèle inconnu"),
    (400, {"error": {"code": "model_not_found"}}, "modèle inconnu"),
    (429, {"error": {"type": "rate_limit_error"}}, "quota ou débit"),
    (500, {"error": {"type": "api_error"}}, "inconnu"),
    (529, b"<html>surcharge</html>", "inconnu"),
    (200, b"pas du json", "réponse illisible"),
    (200, {"model": "claude-opus-4-6"}, "réponse illisible"),
    (200, {"model": "claude-sonnet-4-6", "usage": {"input_tokens": 8, "output_tokens": 1}}, "modèle substitué"),
    (200, {"usage": {"input_tokens": 8, "output_tokens": 1}}, "modèle substitué"),
    (200, {"model": "claude-opus-4-6", "usage": {"input_tokens": 8, "output_tokens": 500}}, "sortie hors plafond"),
])
def test_artefacts_manque(statut, corps, raison):
    l = g.essayer(couple(), ENV, faux(statut, corps))
    assert l["verdict"] == "manque" and l["raison"] == raison
    s = json.dumps(l, ensure_ascii=False)
    assert "sk-FA" not in s and "Incorrect" not in s and "credit balance" not in s

def test_cle_absente_rien_ne_part():
    vus = []
    l = g.essayer(couple(), {}, faux(200, OK["anthropic"], vus))
    assert (l["verdict"], l["raison"]) == ("manque", "clé absente") and vus == []
    l = g.essayer(couple(), {"CLE_ESSAI": "  "}, faux(200, OK["anthropic"], vus))
    assert l["raison"] == "clé absente" and vus == []

def test_injoignable():
    def t(*a): raise TimeoutError("délai")
    l = g.essayer(couple(), ENV, t)
    assert (l["verdict"], l["raison"]) == ("manque", "injoignable")

def test_plafond_sans_envoi():
    vus = []
    l = g.essayer(couple(tarif_sortie_usd_par_million=1e6), ENV, faux(200, OK["anthropic"], vus))
    assert l["raison"] == "plafond" and vus == []
    l = g.essayer(couple(sortie_max=65), ENV, faux(200, OK["anthropic"], vus))
    assert l["raison"] == "plafond" and vus == []
    l = g.essayer(couple(sortie_max=0), ENV, faux(200, OK["anthropic"], vus))
    assert l["raison"] == "plafond" and vus == []

def test_fournisseur_hors_liste():
    l = g.essayer(couple(f="ailleurs"), ENV, faux(200, {}))
    assert l["verdict"] == "manque"

def test_par_cle_un_manque_suffit(tmp_path):
    plan = [couple(), couple(m="claude-sonnet-4-6")]
    rep = iter([(200, json.dumps(OK["anthropic"]).encode()),
                (400, json.dumps({"error": {"message": "credit balance is too low"}}).encode())])
    r = g.executer(plan, ENV, lambda *a: next(rep), str(tmp_path / "j.jsonl"))
    assert r["par_cle"] == {"CLE_ESSAI": "manque"} and r["tout_pret"] is False
    assert CLE not in (tmp_path / "j.jsonl").read_text()

def test_journal_jamais_ecrase(tmp_path):
    j = tmp_path / "j.jsonl"; j.write_text("x")
    with pytest.raises(FileExistsError):
        g.executer([couple()], ENV, faux(200, OK["anthropic"]), str(j))
    assert j.read_text() == "x"

def test_plan_mal_forme(tmp_path):
    for plan in ([], [{"cle_var": "X"}], [dict(couple(), cle_var="sk-valeur")]):
        p = tmp_path / "p.json"; p.write_text(json.dumps(plan))
        with pytest.raises(ValueError):
            g.lire_plan(str(p))

def test_reel_sans_go_refuse(tmp_path, monkeypatch):
    p = tmp_path / "p.json"; p.write_text(json.dumps([couple()]))
    reg = tmp_path / "go.md"; reg.write_text("| GO-2026-11-22-51 | x |\n")
    monkeypatch.setattr(g, "transport_reel", lambda *a: pytest.fail("envoi interdit"))
    assert g.main(["--plan", str(p), "--journal", str(tmp_path / "j"), "--reel", "--registre-go", str(reg)]) == 2
    assert g.main(["--plan", str(p), "--journal", str(tmp_path / "j"), "--reel", "--go", "GO-2026-11-22-99", "--registre-go", str(reg)]) == 2
    assert g.main(["--plan", str(p), "--journal", str(tmp_path / "j"), "--reel", "--go", "GO-2026-11-22-5", "--registre-go", str(reg)]) == 2

def test_reel_avec_go_cas_sain(tmp_path, monkeypatch):
    p = tmp_path / "p.json"; p.write_text(json.dumps([couple()]))
    reg = tmp_path / "go.md"; reg.write_text("| GO-2026-11-22-51 | x |\n")
    monkeypatch.setattr(g, "transport_reel", faux(200, OK["anthropic"]))
    monkeypatch.setenv("CLE_ESSAI", CLE)
    assert g.main(["--plan", str(p), "--journal", str(tmp_path / "j"), "--reel", "--go", "GO-2026-11-22-51", "--registre-go", str(reg)]) == 0

def test_a_blanc_rien_ne_part(tmp_path, monkeypatch, capsys):
    p = tmp_path / "p.json"; p.write_text(json.dumps([couple()]))
    monkeypatch.setattr(g, "transport_reel", lambda *a: pytest.fail("envoi interdit"))
    assert g.main(["--plan", str(p), "--journal", str(tmp_path / "j")]) == 0
    assert "a_blanc" in capsys.readouterr().out and not (tmp_path / "j").exists()

def test_invite_neutre():
    assert g.INVITE == "ok"
