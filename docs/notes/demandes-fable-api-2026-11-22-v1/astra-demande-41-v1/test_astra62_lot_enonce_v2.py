import hashlib, json, os, sys
import pytest
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import astra62_lot_enonce_v2 as A

TEXTE = "Question neutre de test.\nRéponds en 100 mots au plus.\n"


def enonce(tmp_path, texte=TEXTE):
    p = tmp_path / "e.md"
    p.write_text(texte, encoding="utf-8")
    h = hashlib.sha256(p.read_bytes()).hexdigest()
    (tmp_path / "e.md.sha256").write_text(f"{h}  e.md\n")
    return str(p), h


def registre(tmp_path, go="GO-2026-11-22-74"):
    r = tmp_path / "go.md"
    r.write_text(f"| {go} | 2026-11-22 | calcul |\n")
    return str(r)


class Faux:
    def __init__(self, sortie=b"", statut="completed", total=1):
        self.appels, self.sortie, self.statut, self.total = [], sortie, statut, total

    def __call__(self, m, chemin, cle, corps=None, ent=None):
        self.appels.append((m, chemin, corps))
        if chemin == "/v1/files":
            return 200, b'{"id":"file-in"}'
        if chemin == "/v1/batches":
            return 200, b'{"id":"batch_1","status":"validating"}'
        if chemin.startswith("/v1/batches/"):
            return 200, json.dumps({"id": "batch_1", "status": self.statut, "output_file_id": "file-out",
                                    "request_counts": {"total": self.total}}).encode()
        if chemin == "/v1/files/file-out/content":
            return 200, self.sortie
        return 404, b"{}"


def sortie(ids=("astra62-enonce",), fin="stop", modele="gpt-6.2-astra", texte="RÉPONSE"):
    return "\n".join(json.dumps({"custom_id": i, "response": {"status_code": 200, "body": {
        "model": modele, "choices": [{"finish_reason": fin, "message": {"content": texte}}],
        "usage": {"prompt_tokens": 3000, "completion_tokens": 20000}}}}) for i in ids).encode()


def test_reglages_et_pire(tmp_path):
    e, h = enonce(tmp_path)
    l = A.ligne_du_lot(A.lire_enonce(e, h))
    b = l["body"]
    assert b["reasoning_effort"] == "high" and b["max_completion_tokens"] == 96000 and b["model"] == "gpt-6.2-astra"
    assert [m["role"] for m in b["messages"]] == ["user"] and b["messages"][0]["content"] == TEXTE
    assert A.pire(l) <= A.PLAFOND_LOT


def test_empreinte_fausse_refusee(tmp_path):
    e, h = enonce(tmp_path)
    with pytest.raises(A.Refus):
        A.lire_enonce(e, "0" * 64)
    os.remove(e + ".sha256")
    with pytest.raises(A.Refus):
        A.lire_enonce(e, h)


def test_garde_de_motifs(tmp_path):
    e, h = enonce(tmp_path, "Question.\nsession_01ABCDEFGHIJKLMNOPQRSTUV\n")
    with pytest.raises(A.Refus, match="garde de motifs"):
        A.lire_enonce(e, h)


def test_pire_au_dela_refuse(tmp_path, monkeypatch):
    e, h = enonce(tmp_path)
    monkeypatch.setattr(A, "PLAFOND_LOT", A.D("0.5"))
    with pytest.raises(A.Refus, match="pire"):
        A.soumettre("k", str(tmp_path / "j.jsonl"), Faux(), A.lire_enonce(e, h))


def test_go_absent(tmp_path, monkeypatch):
    e, h = enonce(tmp_path)
    monkeypatch.setenv("OPENAI_API_KEY_2", "k")
    t = Faux()
    assert A.main(["soumettre", "--enonce", e, "--empreinte", h, "--journal", str(tmp_path / "j.jsonl"),
                   "--registre-go", registre(tmp_path, "GO-2026-11-22-01")], transport=t) == 2
    assert t.appels == []


def test_soumettre(tmp_path, monkeypatch):
    e, h = enonce(tmp_path)
    monkeypatch.setenv("OPENAI_API_KEY_2", "CLESECRETE")
    t = Faux(); j = tmp_path / "j.jsonl"
    assert A.main(["soumettre", "--enonce", e, "--empreinte", h, "--journal", str(j),
                   "--registre-go", registre(tmp_path)], transport=t) == 0
    assert [a[1] for a in t.appels] == ["/v1/files", "/v1/batches"]
    assert b'name="purpose"\r\n\r\nbatch' in t.appels[0][2]
    assert json.loads(t.appels[1][2])["completion_window"] == "24h"
    assert "CLESECRETE" not in j.read_text()  # la clé n'est pas journalisée


def test_releve_saine(tmp_path):
    j = tmp_path / "j.jsonl"; s = tmp_path / "s"
    assert A.relever("k", "batch_1", str(j), str(s), Faux(sortie())) == "completed"
    assert (s / "reponse-astra62-v1.md").read_text() == "RÉPONSE"
    assert (s / "reponse-astra62-v1.md.sha256").exists() and (s / "astra62-lot-output_file_id.jsonl.sha256").exists()
    r = [json.loads(x) for x in j.read_text().split("\n") if x]
    assert r[0]["verdict"] == "reponse" and r[-1]["cout_total_usd"] == "0.415000"
    assert "RÉPONSE" not in j.read_text()


@pytest.mark.parametrize("kw", [{"fin": "length"}, {"modele": "gpt-5"}, {"texte": ""}, {"texte": "   \n "}])
def test_releve_defaut(tmp_path, kw):
    j = tmp_path / "j.jsonl"; s = tmp_path / "s"
    assert A.relever("k", "batch_1", str(j), str(s), Faux(sortie(**kw))) == "defaut"
    assert not (s / "reponse-astra62-v1.md").exists()
    r = [json.loads(x) for x in j.read_text().split("\n") if x]
    assert r[0]["verdict"] == "defaut"
    if kw.get("texte", "x"):
        assert (s / "defaut-astra62-v1.md").exists()


@pytest.mark.parametrize("brut,total", [(sortie(ids=("astra62-enonce", "astra62-enonce")), 2),
                                        (sortie(), 2), (sortie(ids=("autre",)), 1), (b"pas du json", 1)])
def test_releve_incoherente_refusee(tmp_path, brut, total):
    j = tmp_path / "j.jsonl"; s = tmp_path / "s"
    with pytest.raises(A.Refus):
        A.relever("k", "batch_1", str(j), str(s), Faux(brut, total=total))
    assert not j.exists() and not (s / "reponse-astra62-v1.md").exists()


def test_releve_repetee_refusee(tmp_path):
    j = tmp_path / "j.jsonl"; s = tmp_path / "s"
    A.relever("k", "batch_1", str(j), str(s), Faux(sortie()))
    with pytest.raises(A.Refus, match="neuf"):
        A.relever("k", "batch_1", str(j), str(s), Faux(sortie()))


def test_lot_en_cours(tmp_path):
    j = tmp_path / "j.jsonl"
    assert A.relever("k", "batch_1", str(j), str(tmp_path / "s"), Faux(statut="in_progress")) == "in_progress"
    assert not (tmp_path / "s").exists()


def test_reseau_nomme(monkeypatch):
    def coupe(*a, **k):
        raise A.urllib.error.URLError("x")
    monkeypatch.setattr(A._OUVREUR, "open", coupe)
    with pytest.raises(A.Refus, match="réseau"):
        A.transport_reel("GET", "/v1/batches/x", "k")


def soumis(tmp_path, monkeypatch, cle="CLESECRETE"):
    e, h = enonce(tmp_path)
    monkeypatch.setenv("OPENAI_API_KEY_2", cle)
    j = tmp_path / "j.jsonl"; g = registre(tmp_path)
    assert A.main(["soumettre", "--enonce", e, "--empreinte", h, "--journal", str(j), "--registre-go", g],
                  transport=Faux()) == 0
    return e, h, j, g


def test_soumission_unique(tmp_path, monkeypatch):
    e, h, j, g = soumis(tmp_path, monkeypatch)
    t = Faux()
    assert A.main(["soumettre", "--enonce", e, "--empreinte", h, "--journal", str(tmp_path / "j2.jsonl"),
                   "--registre-go", g], transport=t) == 2
    assert t.appels == []


def test_releve_liee_au_lot_soumis(tmp_path, monkeypatch):
    e, h, j, g = soumis(tmp_path, monkeypatch)
    base = ["relever", "--enonce", e, "--empreinte", h, "--journal", str(j), "--registre-go", g]
    assert A.main(base + ["--lot", "batch_autre", "--sortie", str(tmp_path / "s1")], transport=Faux(sortie())) == 2
    assert not (tmp_path / "s1").exists()
    assert A.main(base + ["--lot", "batch_1", "--sortie", str(tmp_path / "s2")], transport=Faux(sortie())) == 0
    assert (tmp_path / "s2" / "reponse-astra62-v1.md").exists()


def test_releve_enonce_change(tmp_path, monkeypatch):
    e, h, j, g = soumis(tmp_path, monkeypatch)
    autre = tmp_path / "autre"; autre.mkdir()
    e2, h2 = enonce(autre, "Autre énoncé.\n")
    assert A.main(["relever", "--enonce", e2, "--empreinte", h2, "--journal", str(j), "--registre-go", g,
                   "--lot", "batch_1", "--sortie", str(tmp_path / "s")], transport=Faux(sortie())) == 2


def test_cle_jamais_affichee(tmp_path, monkeypatch, capsys):
    e, h, j, g = soumis(tmp_path, monkeypatch)
    A.main(["relever", "--enonce", e, "--empreinte", h, "--journal", str(j), "--registre-go", g,
            "--lot", "batch_1", "--sortie", str(tmp_path / "s")], transport=Faux(sortie()))
    o = capsys.readouterr()
    assert "CLESECRETE" not in o.out + o.err and "CLESECRETE" not in j.read_text()


def test_empreinte_seule_fausse(tmp_path):
    e, h = enonce(tmp_path)
    open(e, "a").write("x")
    with pytest.raises(A.Refus, match="--empreinte"):
        A.lire_enonce(e, h)


@pytest.mark.parametrize("cas", ["compagnon_vide", "absent", "registre_absent"])
def test_refus_nommes(tmp_path, monkeypatch, cas):
    e, h = enonce(tmp_path)
    monkeypatch.setenv("OPENAI_API_KEY_2", "k")
    g = registre(tmp_path)
    if cas == "compagnon_vide":
        open(e + ".sha256", "w").close()
    if cas == "absent":
        e = str(tmp_path / "nul.md")
    if cas == "registre_absent":
        g = str(tmp_path / "nul-go.md")
    assert A.main(["soumettre", "--enonce", e, "--empreinte", h, "--journal", str(tmp_path / "j.jsonl"),
                   "--registre-go", g], transport=Faux()) == 2


@pytest.mark.parametrize("brut", [b"pas du json", b"[1, 2]"])
def test_lot_non_objet(tmp_path, brut):
    class F(Faux):
        def __call__(self, m, chemin, cle, corps=None, ent=None):
            if chemin.startswith("/v1/batches/"):
                return 200, brut
            return super().__call__(m, chemin, cle, corps, ent)
    with pytest.raises(A.Refus):
        A.relever("k", "batch_1", str(tmp_path / "j.jsonl"), str(tmp_path / "s"), F())


def test_identifiant_manquant(tmp_path):
    class F(Faux):
        def __call__(self, m, chemin, cle, corps=None, ent=None):
            self.appels.append((m, chemin, corps))
            if chemin == "/v1/files":
                return 200, b"{}"
            return 200, b'{"id":"batch_1"}'
    t = F()
    with pytest.raises(A.Refus, match="identifiant"):
        A.soumettre("k", str(tmp_path / "j.jsonl"), t, TEXTE)
    assert [a[1] for a in t.appels] == ["/v1/files"]


@pytest.mark.parametrize("statut,erreur", [(500, None), (200, {"code": "x"})])
def test_ligne_en_erreur_pas_reponse(tmp_path, statut, erreur):
    l = json.loads(sortie())
    l["response"]["status_code"] = statut
    if erreur:
        l["error"] = erreur
    j = tmp_path / "j.jsonl"; s = tmp_path / "s"
    assert A.relever("k", "batch_1", str(j), str(s), Faux(json.dumps(l).encode())) == "defaut"
    assert not (s / "reponse-astra62-v1.md").exists()


def test_brut_en_mode_neuf(tmp_path):
    s = tmp_path / "s"; s.mkdir()
    A.ecrire_neuf(str(s / "f"), b"a")
    with pytest.raises(FileExistsError):
        A.ecrire_neuf(str(s / "f"), b"b")


def test_redirection_refusee():
    with pytest.raises(A.urllib.error.URLError):
        A._SansRedirection().redirect_request(None, None, 302, "x", {}, "https://ailleurs")


def test_incompleteread_nomme(monkeypatch):
    def coupe(*a, **k):
        raise A.http.client.IncompleteRead(b"")
    monkeypatch.setattr(A._OUVREUR, "open", coupe)
    with pytest.raises(A.Refus, match="réseau"):
        A.transport_reel("GET", "/v1/batches/x", "k")
