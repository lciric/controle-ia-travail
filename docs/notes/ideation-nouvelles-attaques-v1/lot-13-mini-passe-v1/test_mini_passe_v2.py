import json, os, sys
import pytest
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mini_passe_v2 as M
P = M.P
CLE = "sk-FAUSSE"; ENV = {"CLE_G": CLE, "CLE_K": CLE}; SECRET = "SECRETREPONSE"


def config():
    g = {"espece": "argon", "niveau": "high", "provision": 49152}
    return {"version": P.VERSION, "forme": "groupes_theme", "sous_parts": {"CLE_G": "12.10", "CLE_K": "12.10"},
            "proposeurs": [{"id": "argon", "fournisseur": "google", "cle_var": "CLE_G", "chaine": [
                {"modele": "gemini-4-argon", "tarif_entree": 4, "tarif_sortie": 20, "sortie_max": 65536, "google": g}]},
                {"id": "kimi", "fournisseur": "kimi", "cle_var": "CLE_K", "chaine": [
                    {"modele": "kimi-k3.1-pro", "tarif_entree": 2, "tarif_sortie": 10, "sortie_max": 96000}]}]}


def flux(f, m, texte, fin=None):
    if f == "kimi":
        return [{"model": m, "choices": [{"delta": {"content": texte}}]}, {"model": m, "choices": [{"delta": {}, "finish_reason": fin or "stop"}]},
                {"model": m, "choices": [], "usage": {"prompt_tokens": 800, "completion_tokens": 5000}}]
    return [{"modelVersion": m, "candidates": [{"finishReason": fin or "STOP", "content": {"parts": [{"text": texte}]}}],
             "usageMetadata": {"promptTokenCount": 800, "candidatesTokenCount": 3000, "thoughtsTokenCount": 9000}}]


class Faux:
    def __init__(self, regle=None):
        self.regle, self.appels = regle, []
    def __call__(self, url, h, corps, brut):
        b = json.loads(corps); m = b.get("model") or url.split("/models/")[1].split(":")[0]
        f = "google" if "googleapis" in url else "kimi"
        self.appels.append((f, m, b)); n = sum(1 for a in self.appels if a[1] == m)
        out = self.regle(f, m, n) if self.regle else None
        evs = out if out is not None else flux(f, m, SECRET)
        brut.write(b"x"); return 200, iter(evs)


def passe(tmp_path, t):
    q = tmp_path / "q"; q.mkdir()
    return M.MiniPasse(config(), {M.NOM_TEXTE: P.verifier_piece(M.TEXTE, M.NOM_TEXTE)}, ENV, t, str(q), str(tmp_path / "j")), tmp_path


def test_sain_texte_seul_servi(tmp_path):
    t = Faux(); p, tmp = passe(tmp_path, t); r = p.courir(False)
    assert r["unites"] == {"argon": "rendue", "kimi": "rendue"}
    servi = open(M.TEXTE).read()
    assert t.appels[0][2]["contents"][0]["parts"][0]["text"] == servi and t.appels[1][2]["messages"][0]["content"] == servi
    assert SECRET not in (tmp / "j").read_text()


def test_texte_coupe_relance_une_fois_puis_sans_reponse(tmp_path):
    t = Faux(lambda f, m, n: flux(f, m, "a", fin="length") if f == "kimi" else None)
    p, tmp = passe(tmp_path, t); r = p.courir(False)
    assert r["unites"]["kimi"] == "sans réponse" and sum(1 for a in t.appels if a[0] == "kimi") == 2


def test_relance_reussie(tmp_path):
    t = Faux(lambda f, m, n: flux(f, m, "", fin="MAX_TOKENS") if f == "google" and n == 1 else None)
    p, tmp = passe(tmp_path, t); r = p.courir(False)
    assert r["unites"]["argon"] == "rendue"


def test_garde_reduite():
    assert M.garde_reduite("x", "stop") is None and M.garde_reduite("", "stop") == "texte coupé"
    assert M.garde_reduite("", "max_tokens") == "réflexion épuisée" and M.garde_reduite("x", "length") == "texte coupé"


def test_texte_altere_refuse(tmp_path):
    f = tmp_path / "q.md"; f.write_bytes(open(M.TEXTE, "rb").read() + b"x")
    with pytest.raises(P.Refus):
        P.verifier_piece(str(f), M.NOM_TEXTE)


def test_go_exiges():
    assert M.P.GO_EXIGES == ("GO-2026-11-22-70", "GO-2026-11-22-54")


def test_v2_go_70_exige(tmp_path):
    r = tmp_path / "go.md"
    r.write_text("| GO-2026-11-22-46 | x |\n| GO-2026-11-22-48 | x |\n| GO-2026-11-22-54 | x |\n")
    with pytest.raises(P.Refus, match="GO-2026-11-22-70"):
        P.verifier_go(str(r), M.GO_EXIGES)
    r.write_text("| GO-2026-11-22-70 | x |\n| GO-2026-11-22-54 | x |\n")
    P.verifier_go(str(r), M.GO_EXIGES)


def test_v2_main_refuse_sans_go_70(tmp_path, monkeypatch, capsys):
    import hashlib
    for k, v in ENV.items():
        monkeypatch.setenv(k, v)
    c = config(); c["version"] = P.VERSION
    ch = tmp_path / "c.json"; b = json.dumps(c).encode(); ch.write_bytes(b)
    (tmp_path / "c.json.sha256").write_text(hashlib.sha256(b).hexdigest() + "  c.json\n")
    pl = tmp_path / "p.json"; pl.write_text(json.dumps([{"cle_var": "CLE_G", "fournisseur": "google", "modele": "gemini-4-argon",
        "tarif_entree_usd_par_million": 4, "tarif_sortie_usd_par_million": 20}, {"cle_var": "CLE_K", "fournisseur": "kimi",
        "modele": "kimi-k3.1-pro", "tarif_entree_usd_par_million": 2, "tarif_sortie_usd_par_million": 10}]))
    reg = tmp_path / "go.md"; reg.write_text("| GO-2026-11-22-46 | x |\n| GO-2026-11-22-48 | x |\n| GO-2026-11-22-54 | x |\n")
    arg = ["--configuration", str(ch), "--plan-garde", str(pl), "--quarantaine", str(tmp_path / "q"), "--journal", str(tmp_path / "j"),
           "--registre-go", str(reg)]
    assert M.main(arg) == 2
    reg.write_text("| GO-2026-11-22-70 | x |\n| GO-2026-11-22-54 | x |\n")
    assert M.main(arg) == 0


def test_v2_plafond_24_20():
    assert str(P.P_X) == "24.20"
    c = config(); c["sous_parts"] = {"CLE_G": "18.16", "CLE_K": "6.05"}
    import hashlib, tempfile
    d = tempfile.mkdtemp(); ch = os.path.join(d, "c.json"); b = json.dumps(c).encode(); open(ch, "wb").write(b)
    open(ch + ".sha256", "w").write(hashlib.sha256(b).hexdigest() + "  c.json\n")
    with pytest.raises(P.Refus, match="G7"):
        P.lire_configuration(ch)
