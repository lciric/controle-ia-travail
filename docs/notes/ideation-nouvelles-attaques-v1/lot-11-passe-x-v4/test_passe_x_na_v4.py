import hashlib, http.server, io, json, os, re, shutil, sys, threading
from decimal import Decimal as D
import pytest
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import passe_x_na_v4 as P

TEXTES = "/home/user/controle-ia-travail/docs/notes/ideation-nouvelles-attaques-v1/passe-x-textes-groupes-v1/textes"
CLE = "sk-FAUSSE-0123456789abcdef"
ENV = {"CLE_LUC": CLE, "CLE_G": CLE, "CLE_O": CLE, "CLE_K": CLE}
SECRET = "SECRETDEREPONSE"


def maillon(m, te=5, ts=25, n=96000, **k):
    d = {"modele": m, "tarif_entree": te, "tarif_sortie": ts, "sortie_max": n}; d.update(k); return d


def config():
    g = {"espece": "argon", "niveau": "high", "provision": 49152}
    return {"version": P.VERSION, "forme": "groupes_theme",
            "sous_parts": {"CLE_LUC": "90.75", "CLE_G": "66.55", "CLE_O": "24.20", "CLE_K": "18.15"},
            "proposeurs": [
                {"id": "espece_1", "fournisseur": "google", "cle_var": "CLE_G", "chaine": [maillon("gemini-4-argon", 4, 20, 65536, google=g)]},
                {"id": "espece_2", "fournisseur": "openai", "cle_var": "CLE_O", "chaine": [maillon("gpt-6-astra", 10, 50, 96000, extras={"reasoning_effort": "xhigh"})]},
                {"id": "espece_3", "fournisseur": "anthropic", "cle_var": "CLE_LUC", "chaine": [maillon("claude-x", extras={"output_config": {"effort": "max"}}), maillon("claude-opus-4-6"), maillon("claude-sonnet-4-6", 3, 15)]},
                {"id": "ajout_kimi", "fournisseur": "kimi", "cle_var": "CLE_K", "chaine": [maillon("kimi-k3.1-pro", 2, 10, 96000)]},
            ]}


def rangs_de(texte):
    return [int(x) for x in re.findall(r"\[Pièce (\d+) sur 18\]", texte)]


def reponse(rangs, mots_par=300, finale=True, ordre=None, court=None):
    parts = []
    for i, k in enumerate(ordre or rangs):
        n = court if (court is not None and i == len(rangs) - 1) else mots_par
        parts.append(f"## Réponse {k}\n\n" + " ".join([SECRET.lower()] * n))
    return "\n\n".join(parts) + ("\n\nFIN DES RÉPONSES\n" if finale else "\n")


def flux(f, m, texte, fin=None, sortie=20000):
    if f == "anthropic":
        return [{"type": "message_start", "message": {"model": m, "usage": {"input_tokens": 3000}}},
                {"type": "content_block_delta", "delta": {"type": "text_delta", "text": texte}},
                {"type": "message_delta", "delta": {"stop_reason": fin or "end_turn"}, "usage": {"output_tokens": sortie}}]
    if f in ("openai", "kimi"):
        return [{"model": m, "choices": [{"delta": {"content": texte}}]},
                {"model": m, "choices": [{"delta": {}, "finish_reason": fin or "stop"}]},
                {"model": m, "choices": [], "usage": {"prompt_tokens": 3000, "completion_tokens": sortie}}]
    return [{"modelVersion": m, "candidates": [{"content": {"parts": [{"text": "p", "thought": True}, {"text": texte}]}}]},
            {"modelVersion": m, "candidates": [{"finishReason": fin or "STOP", "content": {"parts": []}}],
             "usageMetadata": {"promptTokenCount": 3000, "candidatesTokenCount": 9000, "thoughtsTokenCount": 11000}}]


def texte_de(f, b):
    return b["contents"][0]["parts"][0]["text"] if f == "google" else b["messages"][0]["content"]


class Faux:
    def __init__(self, regle=None):
        self.regle, self.appels, self.verrou = regle, [], threading.Lock()

    def __call__(self, url, ent, corps, brut):
        b = json.loads(corps)
        m = b.get("model") or url.split("/models/")[1].split(":")[0]
        f = "anthropic" if "anthropic" in url else "google" if "googleapis" in url else "kimi" if "moonshot" in url else "openai"
        rangs = rangs_de(texte_de(f, b))
        with self.verrou:
            self.appels.append((f, m, tuple(rangs), b))
            n = sum(1 for a in self.appels if a[1] == m and a[2] == tuple(rangs))
        out = self.regle(f, m, rangs, n, b) if self.regle else None
        if out is None:
            evs = flux(f, m, reponse(rangs))
            st = 200
        else:
            st, evs = out
        brut.write(json.dumps(evs).encode())
        return st, iter(evs)


def passe(tmp_path, transport, c=None, env=ENV):
    textes = P.lire_textes(TEXTES)
    q = tmp_path / "q"; q.mkdir()
    return P.Passe(c or config(), textes, env, transport, str(q), str(tmp_path / "j.jsonl")), tmp_path


def lignes(tmp, t="tentative"):
    return [x for x in (json.loads(l) for l in open(tmp / "j.jsonl")) if x.get("type_ligne") == t]


def ecrire_lire(c):
    import tempfile
    d = tempfile.mkdtemp(); ch = os.path.join(d, "c.json"); b = json.dumps(c).encode(); open(ch, "wb").write(b)
    open(ch + ".sha256", "w").write(hashlib.sha256(b).hexdigest() + "  c.json\n")
    return P.lire_configuration(ch)


# ---- cas sain ----
def test_sain_douze_unites_rendues_sans_texte_qui_sorte(tmp_path):
    t = Faux(); p, tmp = passe(tmp_path, t)
    r = p.courir(True)
    assert len(r["unites"]) == 12 and set(r["unites"].values()) == {"rendue"}
    j = (tmp / "j.jsonl").read_text()
    assert SECRET.lower() not in j and SECRET not in json.dumps(r) and CLE not in j
    assert len(lignes(tmp, "barrière")) == 1 and lignes(tmp, "barrière")[0]["passe"]
    assert {a[2] for a in t.appels} == {tuple(P.RANGS_TEXTES[f"groupe-{g}"]) for g in (1, 2, 3)}
    assert all(texte_de(a[0], a[3]).startswith("Voici six questions de recherche") for a in t.appels)
    assert len(os.listdir(tmp / "q")) == 24


def test_groupe_1_part_avant_les_autres(tmp_path):
    t = Faux(); p, tmp = passe(tmp_path, t); p.courir(True)
    ordre = [a[2] for a in t.appels]
    g1 = tuple(P.RANGS_TEXTES["groupe-1"])
    assert all(x == g1 for x in ordre[:4]) and g1 not in ordre[4:]


# ---- garde de coupure : banc de coupures plantées ----
R6 = (1, 2, 3, 9, 15, 18)
BANC = {
    "sans ligne finale": (reponse(R6, finale=False), "stop"),
    "ligne finale en double": (reponse(R6) + "FIN DES RÉPONSES\n", "stop"),
    "ligne finale pas en dernier": (reponse(R6).replace("FIN DES RÉPONSES\n", "FIN DES RÉPONSES\nencore\n"), "stop"),
    "titre manquant": (reponse(R6, ordre=(1, 2, 3, 9, 15)), "stop"),
    "titres dans le désordre": (reponse(R6, ordre=(1, 3, 2, 9, 15, 18)), "stop"),
    "dernière réponse trop courte": (reponse(R6, court=100), "stop"),
    "coupé sur max_tokens": (reponse(R6, finale=False), "max_tokens"),
    "coupé sur length": (reponse(R6, finale=False), "length"),
    "réflexion épuisée, texte vide": ("", "max_tokens"),
    "fin absente": (reponse(R6), None),
    "titre de trop": (reponse(R6, ordre=(1, 2, 3, 9, 15, 18, 19)), "stop"),
    "réponse vide": ("", "stop"),
}


@pytest.mark.parametrize("nom", sorted(BANC))
def test_banc_de_coupures_plantees_toutes_rejetees(nom):
    texte, fin = BANC[nom]
    cause, _, _ = P.garde_coupure(texte, R6, fin, 1000, 96000)
    assert cause is not None, nom


def test_garde_reponse_saine_acceptee_et_alertes():
    assert P.garde_coupure(reponse(R6), R6, "end_turn", 1000, 96000)[0] is None
    cause, alertes, _ = P.garde_coupure(reponse(R6), R6, "stop", 95000, 96000)
    assert cause is None and alertes == ["sortie au-delà de 90 % du plafond"]
    t = reponse(R6).replace("## Réponse 18\n\n" + " ".join([SECRET.lower()] * 300), "## Réponse 18\n\n" + " ".join([SECRET.lower()] * 250))
    t = t.replace("## Réponse 15\n\n" + " ".join([SECRET.lower()] * 300), "## Réponse 15\n\n" + " ".join([SECRET.lower()] * 250))
    t = t.replace("## Réponse 1\n\n" + " ".join([SECRET.lower()] * 300), "## Réponse 1\n\n" + " ".join([SECRET.lower()] * 800), 1)
    assert P.garde_coupure(t, R6, "stop", 1, 96000)[1] == ["dernier tiers deux fois plus court que le premier"]


def test_garde_causes():
    assert P.garde_coupure("", R6, "max_tokens", 1, 96000)[0] == "réflexion épuisée"
    assert P.garde_coupure(reponse(R6, finale=False), R6, "max_tokens", 1, 96000)[0] == "texte coupé"
    assert P.garde_coupure(reponse(R6, ordre=(1, 2, 3, 9, 15)), R6, "stop", 1, 96000)[0] == "couverture incomplète"


# ---- relances ----
def test_relance_texte_coupe_scinde_en_deux_moities(tmp_path):
    def regle(f, m, rangs, n, b):
        if f == "kimi" and len(rangs) == 6 and rangs[0] == 1:
            return 200, flux(f, m, reponse(rangs, finale=False))
    t = Faux(regle); p, tmp = passe(tmp_path, t); r = p.courir(False)
    assert r["unites"]["ajout_kimi/groupe-1"] == "rendue"
    k = [a[2] for a in t.appels if a[0] == "kimi"]
    assert (1, 2, 3) in k and (9, 15, 18) in k
    l = [x for x in lignes(tmp) if x["proposeur"] == "ajout_kimi" and x["relance"]]
    assert sorted(x["relance"] for x in l) == ["moitié a", "moitié b"]
    assert all(texte_de(a[0], a[3]).startswith("Voici trois questions") for a in t.appels if len(a[2]) == 3)


def test_relance_reflexion_epuisee_cran_en_moins(tmp_path):
    def regle(f, m, rangs, n, b):
        if m == "claude-x" and rangs[0] == 1 and b["output_config"]["effort"] == "max":
            return 200, flux(f, m, "", fin="max_tokens", sortie=96000)
    t = Faux(regle); p, tmp = passe(tmp_path, t); r = p.courir(False)
    assert r["unites"]["espece_3/groupe-1"] == "rendue"
    efforts = [a[3]["output_config"]["effort"] for a in t.appels if a[1] == "claude-x" and a[2][0] == 1]
    assert efforts == ["max", "xhigh"]


def test_relance_transport_meme_requete(tmp_path):
    def regle(f, m, rangs, n, b):
        if f == "openai" and rangs[0] == 4 and n == 1:
            def g():
                yield {"model": m, "choices": [{"delta": {"content": "a"}}]}
                raise ConnectionResetError()
            return 200, g()
    t = Faux(regle); p, tmp = passe(tmp_path, t); r = p.courir(False)
    assert r["unites"]["espece_2/groupe-2"] == "rendue"
    l = [x for x in lignes(tmp) if x["proposeur"] == "espece_2" and x["texte_servi"] == "groupe-2"]
    assert [x["relance"] for x in l] == [None, "transport"] and l[0]["cout_usd"] == "6.050000"


def test_second_defaut_sans_reponse_une_seule_relance(tmp_path):
    def regle(f, m, rangs, n, b):
        if f == "kimi" and rangs[0] == 10:
            def g():
                raise ConnectionResetError()
                yield
            return 200, g()
    t = Faux(regle); p, tmp = passe(tmp_path, t); r = p.courir(False)
    assert r["unites"]["ajout_kimi/groupe-3"] == "sans réponse"
    assert sum(1 for a in t.appels if a[0] == "kimi" and a[2][0] == 10) == 2


def test_google_max_tokens_scinde(tmp_path):
    def regle(f, m, rangs, n, b):
        if f == "google" and len(rangs) == 6 and rangs[0] == 4:
            return 200, flux(f, m, reponse(rangs, finale=False), fin="MAX_TOKENS")
    t = Faux(regle); p, tmp = passe(tmp_path, t); r = p.courir(False)
    assert r["unites"]["espece_1/groupe-2"] == "rendue"
    assert sorted(a[2] for a in t.appels if a[0] == "google" and len(a[2]) == 3 and a[2][0] in (4, 7)) == [(4, 5, 6), (7, 8, 17)]


def test_refus_de_classifieur_garde_le_repli(tmp_path):
    def regle(f, m, rangs, n, b):
        if m == "claude-x":
            return 200, [{"type": "message_start", "message": {"model": m, "usage": {"input_tokens": 1}}},
                         {"type": "message_delta", "delta": {"stop_reason": "refusal"}, "usage": {"output_tokens": 1}}]
    t = Faux(regle); p, tmp = passe(tmp_path, t); r = p.courir(False)
    assert all(r["unites"][f"espece_3/groupe-{g}"] == "rendue" for g in (1, 2, 3))
    l = [x for x in lignes(tmp) if x["proposeur"] == "espece_3" and x["modele_demande"] == "claude-opus-4-6"]
    assert len(l) == 3 and all(x["par_repli"] for x in l)


def test_refus_final_pas_de_relance(tmp_path):
    def regle(f, m, rangs, n, b):
        if f == "anthropic":
            return 200, [{"type": "message_start", "message": {"model": m, "usage": {"input_tokens": 1}}},
                         {"type": "message_delta", "delta": {"stop_reason": "refusal"}, "usage": {"output_tokens": 1}}]
    t = Faux(regle); p, tmp = passe(tmp_path, t); r = p.courir(False)
    assert r["unites"]["espece_3/groupe-1"] == "fermée"
    assert not any(x["relance"] for x in lignes(tmp) if x["proposeur"] == "espece_3")


# ---- barrière ----
def test_barriere_arrete_si_moins_de_sept_sur_neuf(tmp_path):
    c = config()
    base = c["proposeurs"]
    c["proposeurs"] = base + [dict(base[3], id=f"kimi_{i}") for i in range(5)]  # 9 proposeurs
    c["sous_parts"]["CLE_K"] = "18.15"
    def regle(f, m, rangs, n, b):
        if f in ("openai", "google", "anthropic"):
            return 400, [{"error": {"type": "invalid_request_error", "message": "mauvais réglage"}}]
    t = Faux(regle); p, tmp = passe(tmp_path, t, c); p.courir(False)
    assert not lignes(tmp, "barrière")[0]["passe"]
    assert all(a[2][0] == 1 for a in t.appels)


def test_barriere_passe_a_sept(tmp_path):
    c = config(); base = c["proposeurs"]
    c["proposeurs"] = base + [dict(base[3], id=f"kimi_{i}") for i in range(5)]
    c["sous_parts"]["CLE_K"] = "200"
    c["sous_parts"] = {"CLE_LUC": "40", "CLE_G": "40", "CLE_O": "20", "CLE_K": "99.65"}
    def regle(f, m, rangs, n, b):
        if f in ("openai", "google"):
            return 400, [{"error": {"type": "invalid_request_error", "message": "x"}}]
    t = Faux(regle); p, tmp = passe(tmp_path, t, c); p.courir(False)
    assert lignes(tmp, "barrière")[0]["passe"] and lignes(tmp, "barrière")[0]["modeles_sans_defaut_de_reglage"] == 7


# ---- arrêts n° 12 et 13, crédit ----
def test_arret_12_par_cle(tmp_path):
    c = config(); c["sous_parts"]["CLE_O"] = "6.10"   # une tentative réservée à 6,05, puis le coût réel (1,03) compté
    t = Faux(); p, tmp = passe(tmp_path, t, c); p.courir(False)
    l = [x for x in lignes(tmp) if x["proposeur"] == "espece_2"]
    assert [x["classe"] for x in l] == ["réponse rendue", "refusée avant envoi (arrêt n° 12)",
                                        "refusée avant envoi (arrêt n° 12)"]
    assert sum(1 for a in t.appels if a[0] == "openai") == 1


def test_arret_13(tmp_path):
    def regle(f, m, rangs, n, b):
        if f == "anthropic":
            return 400, [{"error": {"type": "invalid_request_error", "message": "Your credit balance is too low"}}]
    t = Faux(regle); p, tmp = passe(tmp_path, t); r = p.courir(False)
    assert r["arret_13"] and not lignes(tmp, "barrière")[0]["passe"]
    assert "credit balance" not in (tmp / "j.jsonl").read_text()


# ---- configuration, textes ----
def test_config_saine():
    assert ecrire_lire(config())["forme"] == "groupes_theme"


@pytest.mark.parametrize("alterer", [
    lambda c: c.update(forme="sans_decoupe"),
    lambda c: c["proposeurs"][0].update(texte="groupe-1"),
    lambda c: c["sous_parts"].update(CLE_LUC="91.00"),
    lambda c: c["proposeurs"][2]["chaine"][0].update(extras={"system": "x"}),
    lambda c: c["proposeurs"][1]["chaine"].append(maillon("gpt-autre")),
])
def test_config_artefacts(alterer):
    c = config(); alterer(c)
    with pytest.raises(P.Refus):
        ecrire_lire(c)


def test_texte_altere_refuse(tmp_path):
    d = tmp_path / "t"; shutil.copytree(TEXTES, d)
    f = d / "groupe-2-moitie-b.md"; b = f.read_bytes(); f.write_bytes(b[:-1] + b"Z")
    with pytest.raises(P.Refus, match="groupe-2-moitie-b"):
        P.lire_textes(str(d))


def test_textes_sains_neuf():
    assert len(P.lire_textes(TEXTES)) == 9


def test_cran_en_moins():
    m = maillon("claude-x", extras={"output_config": {"effort": "max"}})
    assert P.cran_en_moins("anthropic", m)["extras"]["output_config"]["effort"] == "xhigh"
    assert P.cran_en_moins("openai", maillon("g", extras={"reasoning_effort": "xhigh"}))["extras"]["reasoning_effort"] == "high"
    assert P.cran_en_moins("kimi", maillon("k")) == maillon("k") | {"extras": {}}


# ---- main ----
def plan_complet(c):
    return [{"cle_var": k, "fournisseur": next(p["fournisseur"] for p in c["proposeurs"] if p["cle_var"] == k),
             "modele": m, "tarif_entree_usd_par_million": 5, "tarif_sortie_usd_par_million": 25}
            for k, m in sorted(P.couples_de_la_configuration(c))]


def preparer(tmp_path, monkeypatch, plan=None):
    for k, v in ENV.items():
        monkeypatch.setenv(k, v)
    c = config(); ch = tmp_path / "c.json"; b = json.dumps(c).encode(); ch.write_bytes(b)
    (tmp_path / "c.json.sha256").write_text(hashlib.sha256(b).hexdigest() + "  c.json\n")
    reg = tmp_path / "go.md"; reg.write_text("".join(f"| {g} | x |\n" for g in P.GO_EXIGES))
    pl = tmp_path / "plan.json"; pl.write_text(json.dumps(plan if plan is not None else plan_complet(c)))
    return ["--textes", TEXTES, "--configuration", str(ch), "--plan-garde", str(pl), "--quarantaine", str(tmp_path / "q"),
            "--journal", str(tmp_path / "j.jsonl"), "--registre-go", str(reg)]


def test_main_a_blanc(tmp_path, monkeypatch, capsys):
    arg = preparer(tmp_path, monkeypatch)
    monkeypatch.setattr(P, "transport_reel", lambda *a: pytest.fail("rien"))
    monkeypatch.setattr(P, "transport_simple", lambda *a: pytest.fail("rien"))
    assert P.main(arg) == 0 and '"p_x": "199.65"' in capsys.readouterr().out


def test_main_reel_sain(tmp_path, monkeypatch):
    arg = preparer(tmp_path, monkeypatch)
    def simple(url, h, b):
        m = json.loads(b).get("model") or url.split("/models/")[1].split(":")[0]
        return 200, json.dumps({"model": m, "totalTokens": 2, "usage": {"input_tokens": 1, "output_tokens": 1,
                                                                        "prompt_tokens": 1, "completion_tokens": 1}}).encode()
    monkeypatch.setattr(P, "transport_simple", simple)
    monkeypatch.setattr(P, "transport_reel", Faux())
    assert P.main(arg + ["--reel"]) == 0
    l = [json.loads(x) for x in open(tmp_path / "j.jsonl")]
    assert l[0]["type_ligne"] == "ouverture" and any("groupes thématiques" in e for e in l[0]["ecarts"])


def test_main_plan_partiel(tmp_path, monkeypatch):
    c = config()
    arg = preparer(tmp_path, monkeypatch, plan=plan_complet(c)[:2])
    monkeypatch.setattr(P, "transport_reel", lambda *a: pytest.fail("rien"))
    monkeypatch.setattr(P, "transport_simple", lambda *a: pytest.fail("rien"))
    assert P.main(arg + ["--reel"]) == 2


def test_main_quarantaine_dans_un_depot(tmp_path, monkeypatch):
    arg = preparer(tmp_path, monkeypatch)
    q = "/home/user/controle-ia-travail/docs/notes/ideation-nouvelles-attaques-v1/lot-11-passe-x-v4/q-interdit"
    arg[arg.index("--quarantaine") + 1] = q
    assert P.main(arg) == 2 and not os.path.exists(q)


# ---- héritage : quelques gardes de la v3, rejouées ----
def test_credit_hors_forme(tmp_path):
    def regle(f, m, rangs, n, b):
        if f == "kimi":
            return 429, [{"error": {"type": "erreur", "message": "insufficient balance"}}]
    p, tmp = passe(tmp_path, Faux(regle)); r = p.courir(False)
    assert r["arret_13"]


def test_modele_substitue(tmp_path):
    def regle(f, m, rangs, n, b):
        if f == "kimi":
            return 200, flux(f, "kimi-k3.1-pro-mini", reponse(rangs))
    p, tmp = passe(tmp_path, Faux(regle)); r = p.courir(False)
    assert r["unites"]["ajout_kimi/groupe-1"] == "fermée"


# ================= essais hérités de la v3 (chemins inchangés) =================
class _Serveur(http.server.BaseHTTPRequestHandler):
    def log_message(self, *a):
        pass

    def do_POST(self):
        self.rfile.read(int(self.headers["content-length"]))
        if self.path.startswith("/erreur"):
            b = json.dumps({"error": {"type": "invalid_request_error", "message": "credit balance is too low"}}).encode()
            self.send_response(400); self.send_header("content-length", str(len(b))); self.end_headers(); self.wfile.write(b)
            return
        if self.path.startswith("/redirige"):
            self.send_response(307); self.send_header("location", "http://127.0.0.1:9/ailleurs")
            self.send_header("content-length", "0"); self.end_headers(); return
        self.send_response(200); self.send_header("content-type", "text/event-stream"); self.end_headers()
        for e in flux("openai", "gpt-6-astra", reponse((4, 5, 6))):
            self.wfile.write(b"data: " + json.dumps(e).encode() + b"\n\n")
        self.wfile.write(b"data: [DONE]\n\n")


@pytest.fixture
def serveur(monkeypatch):
    monkeypatch.setenv("no_proxy", "127.0.0.1"); monkeypatch.setenv("NO_PROXY", "127.0.0.1")
    s = http.server.ThreadingHTTPServer(("127.0.0.1", 0), _Serveur)
    threading.Thread(target=s.serve_forever, daemon=True).start()
    yield f"http://127.0.0.1:{s.server_port}"
    s.shutdown()


def test_transport_reel_local(serveur):
    brut = io.BytesIO()
    st, evs = P.transport_reel(serveur + "/flux", {}, b"{}", brut)
    r = P.lire_flux("openai", evs)
    assert st == 200 and r["fin"] == "stop" and r["sortie"] == 20000 and b"[DONE]" in brut.getvalue()
    st, evs = P.transport_reel(serveur + "/erreur", {}, b"{}", io.BytesIO())
    r = P.lire_flux("openai", evs)
    assert st == 400 and r["credit"] and "credit" not in r["erreur"]


def test_redirections_refusees(serveur):
    with pytest.raises(Exception):
        st, evs = P.transport_reel(serveur + "/redirige", {"x-api-key": CLE}, b"{}", io.BytesIO())
        list(evs)
        raise RuntimeError
    st, b = None, None
    try:
        st, b = P.transport_simple(serveur + "/redirige", {"x-api-key": CLE}, b"{}")
    except Exception:
        st = "refus"
    assert st in (307, "refus")


def test_r1_corps_non_json(monkeypatch):
    err = P.urllib.error.HTTPError("u", 403, "x", {}, io.BytesIO(b"credit balance is too low"))
    monkeypatch.setattr(P._OUVREUR, "open", lambda *a, **k: (_ for _ in ()).throw(err))
    st, evs = P.transport_reel("http://127.0.0.1:1/", {}, b"{}", io.BytesIO())
    r = P.lire_flux("anthropic", evs)
    assert st == 403 and r["credit"]


@pytest.mark.parametrize("servi,ok", [("gpt-6-astra-mini", False), ("gpt-6-astra-2026-11-01", True), (None, False),
                                      ("gpt-6-astra", True)])
def test_r2_suffixe(servi, ok):
    assert P.modele_conforme("gpt-6-astra", servi) is ok


def test_r6_arret_13_sous_verrou(tmp_path):
    p, tmp = passe(tmp_path, Faux()); p.arret_13.set()
    assert p._reserver("CLE_LUC", D("6.05")) == "13"


class _Coupe(http.server.BaseHTTPRequestHandler):
    protocol_version = "HTTP/1.1"
    def log_message(self, *a):
        pass
    def do_POST(self):
        self.rfile.read(int(self.headers["content-length"]))
        self.send_response(200); self.send_header("content-type", "text/event-stream")
        self.send_header("transfer-encoding", "chunked"); self.end_headers()
        self.wfile.write(b"ff\r\ndata: {}\n\n"); self.wfile.flush()
        self.close_connection = True


def test_b4_coupure_reelle(tmp_path, monkeypatch):
    monkeypatch.setenv("no_proxy", "127.0.0.1"); monkeypatch.setenv("NO_PROXY", "127.0.0.1")
    s = http.server.ThreadingHTTPServer(("127.0.0.1", 0), _Coupe)
    threading.Thread(target=s.serve_forever, daemon=True).start()
    try:
        monkeypatch.setitem(P.HOTES, "openai", f"http://127.0.0.1:{s.server_port}/v1/chat/completions")
        p, tmp = passe(tmp_path, P.transport_reel)
        c, r = p.tentative(p.c["proposeurs"][1], 0, p.c["proposeurs"][1]["chaine"][0], "groupe-2")
        assert c == "injoignable"
        l = [x for x in lignes(tmp) if x["proposeur"] == "espece_2"][0]
        assert l["cout_usd"] == "6.050000" and "exception" in l
    finally:
        s.shutdown()


def test_quarantaine_jamais_ecrasee(tmp_path):
    p, tmp = passe(tmp_path, Faux())
    pr = p.c["proposeurs"][1]
    (tmp / "q" / "espece_2-groupe-1-rang-0-gpt-6-astra.flux").write_bytes(b"ancien")
    with pytest.raises(FileExistsError):
        p.tentative(pr, 0, pr["chaine"][0], "groupe-1")
    assert (tmp / "q" / "espece_2-groupe-1-rang-0-gpt-6-astra.flux").read_bytes() == b"ancien"


def config_efforts():
    c = config()
    c["proposeurs"][2]["chaine"][0] = maillon("claude-x", efforts=["max", "xhigh", "high"])
    c["proposeurs"][1]["chaine"][0] = maillon("gpt-6-astra", 10, 50, 96000, efforts=["xhigh", "high"])
    return c


def test_g4b_retient_le_premier_admis(tmp_path):
    def t(url, h, b):
        d = json.loads(b); e = (d.get("output_config") or {}).get("effort") or d.get("reasoning_effort")
        assert d.get("max_tokens", d.get("max_completion_tokens")) == 16 and d["messages"][0]["content"] == "ok"
        return (400, b"{}") if e in ("max", "xhigh") else (200, b"{}")
    c = P.essayer_reglages(config_efforts(), ENV, t, str(tmp_path / "r.jsonl"))
    assert c["proposeurs"][2]["chaine"][0]["extras"]["output_config"]["effort"] == "high"
    assert c["proposeurs"][1]["chaine"][0]["extras"]["reasoning_effort"] == "high"


@pytest.mark.parametrize("rep", [(500, b"{}"), (401, b"{}")])
def test_g4b_autre_statut(tmp_path, rep):
    vus = []
    def t(*a):
        vus.append(1); return rep
    with pytest.raises(P.Refus, match=f"statut {rep[0]}"):
        P.essayer_reglages(config_efforts(), ENV, t, str(tmp_path / "r.jsonl"))
    assert len(vus) == 1


def test_g4b_aucun_niveau(tmp_path):
    with pytest.raises(P.Refus, match="aucun niveau"):
        P.essayer_reglages(config_efforts(), ENV, lambda *a: (400, b"{}"), str(tmp_path / "r.jsonl"))


@pytest.mark.parametrize("alterer", [
    lambda c: c["proposeurs"][2]["chaine"][0].update(efforts=["high", "max"]),
    lambda c: c["proposeurs"][3]["chaine"][0].update(efforts=["high"]),
    lambda c: c["proposeurs"][2]["chaine"][0].update(extras={"output_config": {"effort": "max"}}),
])
def test_g4b_config(alterer):
    c = config_efforts(); alterer(c)
    with pytest.raises(P.Refus):
        ecrire_lire(c)


def test_go_et_piece(tmp_path):
    r = tmp_path / "go.md"; r.write_text("| GO-2026-11-22-46 | x |\n")
    with pytest.raises(P.Refus):
        P.verifier_go(str(r))
    r.write_text("".join(f"| {g} | x |\n" for g in P.GO_EXIGES)); P.verifier_go(str(r))


def test_garde_motifs_mord(monkeypatch):
    monkeypatch.setattr(P, "garde_motifs_ligne", lambda l: ["m"] if l else [])
    with pytest.raises(P.Refus):
        P.lire_textes(TEXTES)


def test_google_defauts(tmp_path):
    def regle(f, m, rangs, n, b):
        if f == "google":
            return 200, [{"modelVersion": m, "candidates": [{"finishReason": "STOP", "content": {"parts": [{"text": reponse(rangs)}]}}],
                          "usageMetadata": {"promptTokenCount": 1, "candidatesTokenCount": 1, "thoughtsTokenCount": 0}}]
    p, tmp = passe(tmp_path, Faux(regle)); r = p.courir(False)
    assert r["unites"]["espece_1/groupe-1"] == "fermée"


def test_google_garde_v3_refuse_96000(tmp_path):
    c = config(); c["proposeurs"][0]["chaine"][0]["sortie_max"] = 96000
    with pytest.raises(P.Refus, match="G6"):
        passe(tmp_path, Faux(), c)


def test_pire_au_dela_refuse(tmp_path):
    c = config(); c["proposeurs"][2]["chaine"][0]["tarif_sortie"] = 75
    with pytest.raises(P.Refus, match="G5"):
        passe(tmp_path, Faux(), c)


def test_cle_absente(tmp_path):
    with pytest.raises(P.Refus, match="G11"):
        passe(tmp_path, Faux(), env={"CLE_LUC": CLE})


def test_usage_absent_au_pire(tmp_path):
    def regle(f, m, rangs, n, b):
        if f == "kimi":
            return 200, flux(f, m, reponse(rangs))[:2]
    p, tmp = passe(tmp_path, Faux(regle)); p.courir(False)
    l = [x for x in lignes(tmp) if x["proposeur"] == "ajout_kimi"][0]
    assert l["cout_inconnu"] and l["cout_usd"] == "6.050000"


def test_b3_fin_et_modele_en_liste_fermee(tmp_path):
    def regle(f, m, rangs, n, b):
        if f == "openai":
            return 200, [{"model": SECRET, "choices": [{"delta": {"content": "a"}, "finish_reason": SECRET}],
                          "usage": {"prompt_tokens": 1, "completion_tokens": 1}}]
    p, tmp = passe(tmp_path, Faux(regle)); p.courir(False)
    assert SECRET not in (tmp / "j.jsonl").read_text()


def test_b2_google_erreur_apres_usage(tmp_path):
    def regle(f, m, rangs, n, b):
        if f == "google" and n == 1:
            return 200, [{"modelVersion": m, "candidates": [{"content": {"parts": [{"text": "t"}]}}],
                          "usageMetadata": {"promptTokenCount": 7000, "candidatesTokenCount": 5, "thoughtsTokenCount": 5}},
                         {"error": {"code": 500, "status": "INTERNAL"}}]
    p, tmp = passe(tmp_path, Faux(regle)); p.courir(False)
    l = [x for x in lignes(tmp) if x["proposeur"] == "espece_1"][0]
    assert l["cout_usd"] == "6.050000" and l["cout_inconnu"]


# ================= essais ajoutés après les mutations =================
def test_g2_compagnon_faux(tmp_path):
    ch = tmp_path / "c.json"; ch.write_text(json.dumps(config()))
    (tmp_path / "c.json.sha256").write_text("0" * 64 + "  c.json\n")
    with pytest.raises(P.Refus, match="G2"):
        P.lire_configuration(str(ch))


def test_classe_illisible_sur_length():
    r = {"erreur": None, "credit": False, "modele": "gpt-6-astra", "fin": "length", "texte": "abc", "pensee_jetons": None,
         "blocage": None}
    assert P.classer("openai", maillon("gpt-6-astra"), r) == "réponse illisible"
    r["fin"] = "stop"; r["texte"] = "  "
    assert P.classer("openai", maillon("gpt-6-astra"), r) == "réponse illisible"


def test_b1_un_couple_manque_au_releve(tmp_path, monkeypatch):
    arg = preparer(tmp_path, monkeypatch)
    def simple(url, h, b):
        m = json.loads(b).get("model") or url.split("/models/")[1].split(":")[0]
        if m == "claude-opus-4-6":
            return 400, b'{"error":{"message":"credit balance is too low"}}'
        return 200, json.dumps({"model": m, "totalTokens": 2, "usage": {"input_tokens": 1, "output_tokens": 1,
                                                                        "prompt_tokens": 1, "completion_tokens": 1}}).encode()
    monkeypatch.setattr(P, "transport_simple", simple)
    monkeypatch.setattr(P, "transport_reel", lambda *a: pytest.fail("rien ne part"))
    assert P.main(arg + ["--reel"]) == 2


def test_r3_une_ligne_envoi_par_tentative_partie(tmp_path):
    p, tmp = passe(tmp_path, Faux()); p.courir(False)
    envois = lignes(tmp, "envoi"); tent = [x for x in lignes(tmp) if x.get("flux_sha256")]
    assert len(envois) == len(tent) == 12 and all(e["requete_sha256"] for e in envois)


class _Compteur(http.server.BaseHTTPRequestHandler):
    coups = []
    def log_message(self, *a):
        pass
    def do_POST(self):
        n = int(self.headers.get("content-length") or 0); self.rfile.read(n)
        if self.path == "/depart":
            self.send_response(302); self.send_header("location", self.headers["x-cible"])
            self.send_header("content-length", "0"); self.end_headers(); return
        self.do_GET()

    def do_GET(self):
        _Compteur.coups.append(self.headers.get("x-api-key"))
        self.send_response(200); self.send_header("content-length", "2"); self.end_headers(); self.wfile.write(b"{}")


def test_r7_redirection_jamais_suivie(monkeypatch):
    monkeypatch.setenv("no_proxy", "127.0.0.1"); monkeypatch.setenv("NO_PROXY", "127.0.0.1")
    s = http.server.ThreadingHTTPServer(("127.0.0.1", 0), _Compteur)
    threading.Thread(target=s.serve_forever, daemon=True).start()
    try:
        u = f"http://127.0.0.1:{s.server_port}"
        _Compteur.coups.clear()
        for f in (lambda: list(P.transport_reel(u + "/depart", {"x-api-key": CLE, "x-cible": u + "/ailleurs"}, b"{}", io.BytesIO())[1]),
                  lambda: P.transport_simple(u + "/depart", {"x-api-key": CLE, "x-cible": u + "/ailleurs"}, b"{}")):
            try:
                f()
            except Exception:
                pass
        assert _Compteur.coups == []
    finally:
        s.shutdown()


def test_r8_usage_kimi_dans_le_choix(tmp_path):
    def regle(f, m, rangs, n, b):
        if f == "kimi":
            return 200, [{"model": m, "choices": [{"delta": {"content": reponse(rangs)}, "finish_reason": "stop",
                                                   "usage": {"prompt_tokens": 3000, "completion_tokens": 100}}]}]
    p, tmp = passe(tmp_path, Faux(regle)); p.courir(False)
    l = [x for x in lignes(tmp) if x["proposeur"] == "ajout_kimi"][0]
    assert not l["cout_inconnu"] and D(l["cout_usd"]) == (D(3000) * 2 + D(100) * 10) / D(10**6)
