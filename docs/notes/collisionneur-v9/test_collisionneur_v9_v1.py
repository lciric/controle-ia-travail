"""Essais du collisionneur v9-v1, hors réseau : transport, horloge et sommeil remplacés par des doublures. Chaque garde a un
cas sain et un artefact (R5) ; chaque motif de la garde de motifs a son témoin positif.

Lancement : PYTHONPATH=src .venv/bin/python -B -m pytest -q docs/notes/collisionneur-v9/test_collisionneur_v9_v1.py
"""
import importlib.util
import io
import json
import socket
import urllib.error
from pathlib import Path

import pytest

CHEMIN = Path(__file__).with_name("collisionneur_v9_v1.py")
CLE_GEMINI, CLE_OPENAI, CLE_ANTHROPIC = "cle-gemini-secrete-123", "cle-openai-secrete-456", "cle-anthropic-secrete-789"
SAIN = "mot " * 1000  # 4 000 caractères, aucun motif


def charger():
    spec = importlib.util.spec_from_file_location("collisionneur_v9_v1_essai", CHEMIN)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def reseau_interdit(*args, **kwargs):
    raise AssertionError("appel réseau réel interdit dans les essais")


@pytest.fixture
def c(monkeypatch):
    module = charger()  # module neuf à chaque essai : composition vide
    module.dormis = []
    monkeypatch.setattr(module, "TRANSPORT", reseau_interdit)
    monkeypatch.setattr(module, "DORMIR", lambda s: module.dormis.append(s))
    monkeypatch.setenv("GEMINI_API_KEY", CLE_GEMINI)
    monkeypatch.setenv("OPENAI_API_KEY", CLE_OPENAI)
    monkeypatch.setenv("MA_CLE", CLE_ANTHROPIC)
    monkeypatch.delenv("OPENAI_BASE_URL", raising=False)
    monkeypatch.delenv("ANTHROPIC_WORKSPACE_ID", raising=False)
    return module


# ---------- doublures ----------

class FauxFlux:
    """Réponse ouverte : itérable de lignes (flux) ou corps JSON (read). Coupure possible avant la ligne d'indice donné."""

    def __init__(self, lignes=(), corps=None, coupure_avant=None):
        self.lignes = [(l + "\r\n").encode("utf-8") for l in lignes]
        self.corps, self.coupure_avant = corps, coupure_avant

    def __iter__(self):
        for i, l in enumerate(self.lignes):
            if self.coupure_avant is not None and i == self.coupure_avant:
                raise ConnectionResetError("coupure du relais")
            yield l

    def read(self, *a):
        return json.dumps(self.corps).encode("utf-8")

    def __enter__(self):
        return self

    def __exit__(self, *a):
        return False


class FauxTransport:
    def __init__(self, *actions):
        self.actions, self.appels = list(actions), []

    def __call__(self, requete, delai, locale=False):
        corps = json.loads(requete.data) if requete.data else None
        self.appels.append({"url": requete.full_url, "methode": requete.get_method(), "corps": corps,
                            "entetes": {k.lower(): v for k, v in requete.header_items()}, "delai": delai,
                            "locale": locale})
        if not self.actions:
            raise AssertionError("appel de trop")
        a = self.actions.pop(0)
        if isinstance(a, BaseException):
            raise a
        return a


def http_erreur(code, corps=""):
    return urllib.error.HTTPError("https://exemple.invalid", code, "erreur", {}, io.BytesIO(corps.encode("utf-8")))


def flux_gemini(texte="Réponse. FIN-DE-CELLULE", entree=500, candidats=50, pensees=100, total="somme", fin="STOP",
                modele="gemini-4-carbon", coupure=False, sans_fin=False):
    usage = {"promptTokenCount": entree, "candidatesTokenCount": candidats, "thoughtsTokenCount": pensees}
    if total == "somme":
        usage["totalTokenCount"] = entree + candidats + pensees
    elif total is not None:
        usage["totalTokenCount"] = total
    m1 = {"candidates": [{"content": {"parts": [{"text": "je réfléchis", "thought": True}]}}], "modelVersion": modele,
          "responseId": "g1"}
    dernier = {"content": {"parts": [{"text": texte}]}}
    if not sans_fin:
        dernier["finishReason"] = fin
    m2 = {"candidates": [dernier], "usageMetadata": usage, "modelVersion": modele}
    return FauxFlux(["data: " + json.dumps(m1), "", "data: " + json.dumps(m2), ""], coupure_avant=2 if coupure else None)


def flux_anthropic(texte="Réponse. FIN-DE-CELLULE", fin="end_turn", entree=100, sortie=200, modele="claude-fable-5-2",
                   details=None, sans_stop=False, coupure=False, erreur=False):
    ev = [{"type": "message_start", "message": {"id": "msg_1", "model": modele,
                                                 "usage": {"input_tokens": entree, "output_tokens": 1}}},
          {"type": "content_block_start", "index": 0, "content_block": {"type": "thinking"}},
          {"type": "content_block_start", "index": 1, "content_block": {"type": "text", "text": ""}},
          {"type": "content_block_delta", "index": 1, "delta": {"type": "text_delta", "text": texte}}]
    if erreur:
        ev.append({"type": "error", "error": {"type": "overloaded_error"}})
    delta = {"stop_reason": fin}
    if details:
        delta["stop_details"] = details
    ev.append({"type": "message_delta", "delta": delta, "usage": {"output_tokens": sortie}})
    if not sans_stop:
        ev.append({"type": "message_stop"})
    lignes = []
    for e in ev:
        lignes += [f"event: {e['type']}", "data: " + json.dumps(e), ""]
    return FauxFlux(lignes, coupure_avant=6 if coupure else None)


def final_openai(statut="completed", texte="Réponse. FIN-DE-CELLULE", refus=None, raison=None):
    contenu = [{"type": "output_text", "text": texte}]
    if refus:
        contenu = [{"type": "refusal", "refusal": refus}]
    rep = {"id": "resp_1", "status": statut, "model": "gpt-6.2-astra",
           "output": [{"type": "reasoning"}, {"type": "message", "content": contenu}],
           "usage": {"input_tokens": 100, "output_tokens": 300, "output_tokens_details": {"reasoning_tokens": 200}}}
    if raison:
        rep["incomplete_details"] = {"reason": raison}
    return FauxFlux(corps=rep)


def cree_openai():
    return FauxFlux(corps={"id": "resp_1", "status": "queued", "model": "gpt-6.2-astra"})


def corps_kimi(fin="stop"):
    return FauxFlux(corps={"model": "kimi-k3.1-pro", "id": "k1", "usage": {"prompt_tokens": 10, "completion_tokens": 20},
                           "choices": [{"message": {"content": "Réponse. FIN-DE-CELLULE"}, "finish_reason": fin}]})


def executer(c, dossier, espece, prompt=SAIN, plafond=100.0):
    autre = "kimi" if espece != "kimi" else "astra"
    c.fixer_composition([espece, autre], nom_cle_anthropic="MA_CLE")
    lettre = next(l for l in c.LETTRES if c.MODELES[l]["espece"] == espece)
    return c.executer_cellule(dossier, "E1-T1", lettre, prompt, [], plafond, c.APPELANTS)


def journal(c, dossier):
    return c.essais_journal(dossier)


# ---------- 1. espèces ----------

def test_aucune_espece_implicite(c, tmp_path, capsys):
    faits = tmp_path / "faits.md"
    faits.write_text("Fait sain.\n", encoding="utf-8")
    assert c.principal(["devis", "--faits", str(faits)]) == c.CODE_USAGE
    assert c.principal(["devis", "--carbon", "--faits", str(faits)]) == c.CODE_USAGE
    assert c.LETTRES == ()
    assert c.principal(["devis", "--carbon", "--astra", "--faits", str(faits)]) == c.CODE_FINI
    assert [c.MODELES[l]["espece"] for l in c.LETTRES] == ["astra", "carbon"]


def test_lettres_dans_l_ordre_du_catalogue(c):
    c.fixer_composition(["carbon", "fable", "astra", "argon", "kimi"])
    assert {l: c.MODELES[l]["espece"] for l in c.LETTRES} == {"A": "fable", "B": "argon", "C": "kimi", "D": "astra",
                                                              "E": "carbon"}


def test_identifiants_et_table_des_prix(c):
    ids = {e: c.CATALOGUE[e]["id"] for e in c.CATALOGUE}
    assert ids == {"fable": "claude-fable-5-2", "opus": "claude-opus-5-5", "argon": "gemini-4-argon",
                   "kimi": "kimi-k3.1-pro", "astra": "gpt-6.2-astra", "carbon": "gemini-4-carbon"}
    for e, m in c.CATALOGUE.items():
        assert len(m["prix"]) == 2 and m["prix"][0] > 0 and m["prix"][1] > 0
        assert m["delai_s"] > 0 and m["max"] > 0 and m["max_relance"] >= m["max"]
        assert (m["provision"] > 0) == (m["fournisseur"] == "gemini")
        assert m["car_par_jeton"] == (2.5 if m["fournisseur"] == "gemini" else 3.0)
    texte = CHEMIN.read_text(encoding="utf-8")
    for source in ("R-2677", "R-3676", "R-1756", "R-1049", "plan-chiffre-credits-claude-v1.md"):
        assert source in texte


def test_cle_anthropic_obligatoire_et_cles_par_nom(c, tmp_path, capsys, monkeypatch):
    faits = tmp_path / "faits.md"
    faits.write_text("Fait sain.\n", encoding="utf-8")
    sortie = tmp_path / "run"
    assert c.principal(["etage1", "--fable", "--argon", "--faits", str(faits), "--sortie", str(sortie)]) == c.CODE_USAGE
    assert not sortie.exists()
    monkeypatch.delenv("GEMINI_API_KEY")
    assert c.principal(["etage1", "--fable", "--argon", "--cle-anthropic", "MA_CLE", "--faits", str(faits),
                        "--sortie", str(sortie)]) == c.CODE_USAGE
    err = capsys.readouterr().err
    assert "GEMINI_API_KEY" in err and CLE_ANTHROPIC not in err
    assert c.principal(["etage1", "--fable", "--argon", "--cle-anthropic", "mauvais nom", "--faits", str(faits),
                        "--sortie", str(sortie)]) == c.CODE_USAGE


def test_composition_scellee_dans_le_dossier(c, tmp_path):
    c.fixer_composition(["fable", "argon"], "MA_CLE")
    c.sceller_composition(tmp_path)
    c.sceller_composition(tmp_path)  # sain : même composition
    c.fixer_composition(["fable", "carbon"], "MA_CLE")
    with pytest.raises(c.Arret) as e:  # artefact : autre composition
        c.sceller_composition(tmp_path)
    assert e.value.code == c.CODE_USAGE


def test_cle_anthropic_lue_par_son_nom_jamais_affichee(c, tmp_path, monkeypatch):
    monkeypatch.setenv("MON_ESPACE", "espace-1")
    t = FauxTransport(flux_anthropic())
    c.TRANSPORT = t
    c.fixer_composition(["fable", "kimi"], nom_cle_anthropic="MA_CLE", nom_espace_anthropic="MON_ESPACE")
    rep = c.appeler_anthropic(c.MODELES["A"], SAIN, 100)
    assert rep.texte == "Réponse. FIN-DE-CELLULE" and rep.usage_lu
    entetes = t.appels[0]["entetes"]
    assert entetes["x-api-key"] == CLE_ANTHROPIC and entetes["anthropic-workspace-id"] == "espace-1"
    corps = t.appels[0]["corps"]
    assert corps["stream"] is True and corps["model"] == "claude-fable-5-2" and "thinking" not in corps
    assert "temperature" not in corps and corps["output_config"] == {"effort": "high"}
    c.TRANSPORT = FauxTransport(http_erreur(400, f"clé {CLE_ANTHROPIC} refusée"))
    rep = c.appeler_anthropic(c.MODELES["A"], SAIN, 100)
    assert rep.echec and CLE_ANTHROPIC not in rep.echec and "[clé]" in rep.echec and not rep.interrompue


# ---------- 2a. budget et provision de réflexion ----------

def test_garde_a_sain_budget_pose_et_reflexion_dans_la_provision(c, tmp_path):
    t = FauxTransport(flux_gemini(pensees=32768))
    c.TRANSPORT = t
    assert executer(c, tmp_path, "carbon") == "OK"
    corps = t.appels[0]["corps"]
    assert corps["generationConfig"]["thinkingConfig"] == {"thinkingBudget": 32768, "includeThoughts": True}
    assert corps["generationConfig"]["maxOutputTokens"] == 65536
    assert t.appels[0]["url"].endswith("gemini-4-carbon:streamGenerateContent?alt=sse")
    e = journal(c, tmp_path)[-1]
    assert e["statut"] == "OK" and e["cout_usd"] == round(500 * 4 / 1e6 + (50 + 32768) * 20 / 1e6, 4)


def test_garde_a_artefact_reflexion_au_dela_de_la_provision(c, tmp_path):
    c.TRANSPORT = FauxTransport(flux_gemini(modele="gemini-4-argon", pensees=8193))
    with pytest.raises(c.Arret) as e:
        executer(c, tmp_path, "argon")
    assert e.value.code == c.CODE_GARDE
    d = journal(c, tmp_path)[-1]
    assert d["statut"] == "REFLEXION_HORS_PROVISION"
    assert d["cout_usd"] == round(500 * 10 / 1e6 + (50 + 8193) * 50 / 1e6, 4)  # coût réel compté
    assert not c.chemin_cellule(tmp_path, d["cellule"]).exists()


def test_garde_a_provision_comptee_avant_l_envoi(c, tmp_path):
    c.fixer_composition(["carbon", "kimi"])
    m = c.MODELES["B"]
    assert c.cout_pire_cas(m, 0, 65536) == pytest.approx((65536 + 32768) * 20 / 1e6)
    pire = c.cout_pire_cas(m, len(SAIN), 65536)
    c.TRANSPORT = FauxTransport()  # artefact : plafond juste sous le pire cas, provision comprise → aucun envoi
    with pytest.raises(c.Arret) as e:
        executer(c, tmp_path, "carbon", plafond=pire - 0.001)
    assert e.value.code == c.CODE_PLAFOND and c.TRANSPORT.appels == []
    c.TRANSPORT = FauxTransport(flux_gemini())  # sain : plafond juste au-dessus
    assert executer(c, tmp_path, "carbon", plafond=pire + 0.001) == "OK"


# ---------- 2b. total des jetons de Google, entrée gardée ----------

def test_garde_b_sain_total_egal_aux_champs_lus(c, tmp_path):
    c.TRANSPORT = FauxTransport(flux_gemini(total="somme"))
    assert executer(c, tmp_path, "carbon") == "OK"
    assert journal(c, tmp_path)[-1]["usage"]["ecart_total"] == 0


def test_garde_b_artefact_ecart_compte_au_prix_de_sortie(c, tmp_path):
    c.TRANSPORT = FauxTransport(flux_gemini(total=500 + 50 + 100 + 1000))
    with pytest.raises(c.Arret) as e:
        executer(c, tmp_path, "carbon")
    assert e.value.code == c.CODE_GARDE
    d = journal(c, tmp_path)[-1]
    assert d["statut"] == "ECART_TOTAL_JETONS" and d["usage"]["ecart_total"] == 1000
    assert d["cout_usd"] == round(500 * 4 / 1e6 + (50 + 100 + 1000) * 20 / 1e6, 4)


def test_garde_b_artefact_total_absent_compte_au_pire(c, tmp_path):
    c.TRANSPORT = FauxTransport(flux_gemini(total=None))
    with pytest.raises(c.Arret) as e:
        executer(c, tmp_path, "carbon")
    d = journal(c, tmp_path)[-1]
    assert e.value.code == c.CODE_GARDE and d["statut"] == "USAGE_ABSENT"
    assert d["cout_usd"] == d["cout_pire_usd"] > 0


def test_garde_b_entree_gardee_a_deux_et_demi_caracteres(c, tmp_path):
    c.fixer_composition(["argon", "kimi"])
    m = c.MODELES["A"]
    assert c.entree_gardee(m, 2500) == 1000
    assert c.cout_pire_cas(m, 2500, 0) == pytest.approx(1000 * 10 / 1e6 + 8192 * 50 / 1e6)
    c.TRANSPORT = FauxTransport(flux_gemini(modele="gemini-4-argon", entree=1600))  # sain : 1 600 = 4 000 / 2,5
    assert executer(c, tmp_path, "argon") == "OK"


def test_garde_b_artefact_entree_au_dela_de_la_garde(c, tmp_path):
    c.TRANSPORT = FauxTransport(flux_gemini(modele="gemini-4-argon", entree=1601))
    with pytest.raises(c.Arret) as e:
        executer(c, tmp_path, "argon")
    assert e.value.code == c.CODE_GARDE and journal(c, tmp_path)[-1]["statut"] == "ENTREE_HORS_GARDE"


# ---------- 2c. aucun renvoi ; envoi interrompu compté au pire ----------

ARTEFACTS_ENVOI = {
    "délai": socket.timeout("délai dépassé"),
    "coupure": ConnectionResetError("coupure"),
    "502": "502", "503": "503", "504": "504",
}


@pytest.mark.parametrize("espece", ["carbon", "fable", "astra", "kimi"])
@pytest.mark.parametrize("cas", sorted(ARTEFACTS_ENVOI))
def test_garde_c_artefact_aucun_renvoi_compte_au_pire(c, tmp_path, espece, cas):
    a = ARTEFACTS_ENVOI[cas]
    action = http_erreur(int(a), "surcharge") if isinstance(a, str) else a
    t = FauxTransport(action, action, action)
    c.TRANSPORT = t
    with pytest.raises(c.Arret) as e:
        executer(c, tmp_path, espece)
    assert e.value.code == c.CODE_ECHEC
    assert len(t.appels) == 1  # aucun renvoi
    d = journal(c, tmp_path)[-1]
    assert d["statut"] == "INTERROMPU" and d["interrompue"] is True
    assert d["cout_usd"] == d["cout_pire_usd"] > 0
    assert len(journal(c, tmp_path)) == 1  # le passage s'arrête : pas de relance


@pytest.mark.parametrize("espece", ["carbon", "fable"])
def test_garde_c_artefact_coupure_dans_le_flux(c, tmp_path, espece):
    flux = flux_gemini(coupure=True) if espece == "carbon" else flux_anthropic(coupure=True)
    t = FauxTransport(flux)
    c.TRANSPORT = t
    with pytest.raises(c.Arret) as e:
        executer(c, tmp_path, espece)
    d = journal(c, tmp_path)[-1]
    assert e.value.code == c.CODE_ECHEC and d["statut"] == "INTERROMPU" and d["cout_usd"] == d["cout_pire_usd"]
    assert len(t.appels) == 1


@pytest.mark.parametrize("flux", [lambda: flux_gemini(sans_fin=True), lambda: flux_anthropic(sans_stop=True),
                                  lambda: flux_anthropic(erreur=True)])
def test_garde_c_artefact_flux_inacheve_ou_erreur_dans_le_flux(c, tmp_path, flux):
    f = flux()
    espece = "carbon" if b"gemini" in b"".join(f.lignes) else "fable"
    c.TRANSPORT = FauxTransport(f)
    with pytest.raises(c.Arret):
        executer(c, tmp_path, espece)
    d = journal(c, tmp_path)[-1]
    assert d["statut"] == "INTERROMPU" and d["cout_usd"] == d["cout_pire_usd"]


@pytest.mark.parametrize("espece", ["carbon", "fable", "astra"])
def test_garde_c_sain_seul_le_429_est_repris(c, tmp_path, espece):
    ok = {"carbon": flux_gemini, "fable": flux_anthropic}.get(espece)
    actions = [http_erreur(429, "trop de requêtes")] + ([ok()] if ok else [cree_openai(), final_openai()])
    t = FauxTransport(*actions)
    c.TRANSPORT = t
    assert executer(c, tmp_path, espece) == "OK"
    assert c.dormis[0] == 10
    assert sum(1 for a in t.appels if a["methode"] == "POST") == 2


@pytest.mark.parametrize("action", [http_erreur(400, "réglage refusé"),
                                    urllib.error.URLError(ConnectionRefusedError("refusée"))])
def test_garde_c_sain_refus_avant_traitement_compte_zero(c, tmp_path, action):
    t = FauxTransport(action)
    c.TRANSPORT = t
    with pytest.raises(c.Arret) as e:
        executer(c, tmp_path, "carbon")
    d = journal(c, tmp_path)[-1]
    assert e.value.code == c.CODE_ECHEC and d["statut"] == "ECHEC" and d["cout_usd"] == 0 and len(t.appels) == 1


def test_garde_c_jev_sans_renvoi_compte_au_pire_et_le_run_continue(c, tmp_path, monkeypatch):
    monkeypatch.setenv("TYPESAFE_API_KEY", "cle-jev")
    t = FauxTransport(http_erreur(503), http_erreur(503))
    c.TRANSPORT = t
    statut = c.auditer_jev(tmp_path, "E1-T1-meta-A", "Texte sain.", c.QUESTIONS_JEV, 10.0, c.APPELANTS)
    assert statut == "INTERROMPU" and len(t.appels) == 1
    e = c.audits_jev(tmp_path)[-1]
    assert e["cout_usd"] == round(len("Texte sain.") / 3 / 1e6 * c.JEV["prix_entree"], 4)


def test_garde_c_exception_imprevue_comptee_au_pire(c, tmp_path):
    def appelant_casse(m, prompt, max_tokens):
        raise RuntimeError("imprévu")
    c.fixer_composition(["carbon", "kimi"])
    with pytest.raises(c.Arret) as e:
        c.executer_cellule(tmp_path, "E1-T1", "B", SAIN, [], 100.0, dict(c.APPELANTS, gemini=appelant_casse))
    d = journal(c, tmp_path)[-1]
    assert e.value.code == c.CODE_ECHEC and d["statut"] == "INTERROMPU" and d["cout_usd"] == d["cout_pire_usd"]


# ---------- 2d. délai explicite par espèce ----------

@pytest.mark.parametrize("espece,flux,attendu", [("carbon", flux_gemini, 600), ("fable", flux_anthropic, 600)])
def test_garde_d_sain_delai_passe_au_transport(c, tmp_path, espece, flux, attendu):
    t = FauxTransport(flux())
    c.TRANSPORT = t
    assert executer(c, tmp_path, espece) == "OK"
    assert t.appels[0]["delai"] == attendu
    assert journal(c, tmp_path)[-1]["delai_s"] == c.CATALOGUE[espece]["delai_s"]


def test_garde_d_sain_kimi_garde_son_delai_et_la_boucle_locale(c, tmp_path):
    t = FauxTransport(corps_kimi())
    c.TRANSPORT = t
    assert executer(c, tmp_path, "kimi") == "OK"
    assert t.appels[0]["delai"] == 2000 and t.appels[0]["locale"] is True


@pytest.mark.parametrize("espece,flux", [("carbon", flux_gemini), ("fable", flux_anthropic)])
def test_garde_d_artefact_delai_de_l_espece_depasse_dans_le_flux(c, tmp_path, espece, flux):
    instants = iter([0.0] + [10_000.0] * 50)
    c.HORLOGE = lambda: next(instants)
    c.TRANSPORT = FauxTransport(flux())
    with pytest.raises(c.Arret) as e:
        executer(c, tmp_path, espece)
    d = journal(c, tmp_path)[-1]
    assert e.value.code == c.CODE_ECHEC and d["statut"] == "INTERROMPU" and "délai" in d["echec"]


def test_garde_d_artefact_astra_delai_depasse_annulation_sans_renvoi(c, tmp_path):
    instants = iter([0.0, 10.0, 10_000.0, 10_000.0])
    c.HORLOGE = lambda: next(instants)
    en_cours = FauxFlux(corps={"id": "resp_1", "status": "in_progress", "model": "gpt-6.2-astra"})
    t = FauxTransport(cree_openai(), en_cours, FauxFlux(corps={}))
    c.TRANSPORT = t
    with pytest.raises(c.Arret) as e:
        executer(c, tmp_path, "astra")
    d = journal(c, tmp_path)[-1]
    assert e.value.code == c.CODE_ECHEC and d["statut"] == "INTERROMPU" and d["cout_usd"] == d["cout_pire_usd"]
    assert [a["url"].rsplit("/", 1)[-1] for a in t.appels] == ["responses", "resp_1", "cancel"]
    assert "annulation demandée" in d["echec"]


def test_astra_sain_arriere_plan_et_releve_manque(c, tmp_path):
    t = FauxTransport(cree_openai(), socket.timeout("relevé lent"), final_openai())
    c.TRANSPORT = t
    assert executer(c, tmp_path, "astra") == "OK"
    cree = t.appels[0]
    assert cree["corps"]["background"] is True and cree["corps"]["store"] is True
    assert cree["corps"]["model"] == "gpt-6.2-astra" and cree["corps"]["max_output_tokens"] == 8000
    assert [a["methode"] for a in t.appels] == ["POST", "GET", "GET"]
    assert c.dormis == [20, 20]
    d = journal(c, tmp_path)[-1]
    assert d["cout_usd"] == round(100 * 10 / 1e6 + 500 * 50 / 1e6, 4)


# ---------- lecture des réponses (logique du v8 gardée) ----------

def test_anthropic_refus_et_troncature(c, tmp_path):
    c.TRANSPORT = FauxTransport(flux_anthropic(fin="refusal", texte="", details={"category": "cyber"}))
    assert executer(c, tmp_path, "fable") == "REFUS"
    assert journal(c, tmp_path)[-1]["categorie_refus"] == "cyber"


def test_anthropic_tronque_puis_relance_au_plafond_de_relance(c, tmp_path):
    t = FauxTransport(flux_anthropic(fin="max_tokens"), flux_anthropic())
    c.TRANSPORT = t
    assert executer(c, tmp_path, "fable") == "OK"
    assert [a["corps"]["max_tokens"] for a in t.appels] == [22000, 64000]


def test_anthropic_modele_different(c, tmp_path):
    c.TRANSPORT = FauxTransport(flux_anthropic(modele="claude-opus-4-6"))
    with pytest.raises(c.Arret) as e:
        executer(c, tmp_path, "fable")
    assert e.value.code == c.CODE_MODELE


@pytest.mark.parametrize("final,statut", [(lambda: final_openai(refus="non"), "REFUS"),
                                          (lambda: final_openai(statut="incomplete", raison="content_filter"), "REFUS"),
                                          (lambda: final_openai(statut="incomplete", raison="max_output_tokens"),
                                           "TRONQUE")])
def test_astra_refus_et_troncature(c, tmp_path, final, statut):
    actions = [cree_openai(), final()]
    if statut == "TRONQUE":
        actions += [cree_openai(), final_openai()]
    c.TRANSPORT = FauxTransport(*actions)
    assert executer(c, tmp_path, "astra") == ("OK" if statut == "TRONQUE" else statut)


def test_astra_echec_cote_serveur_compte_au_pire(c, tmp_path):
    c.TRANSPORT = FauxTransport(cree_openai(), final_openai(statut="failed"))
    with pytest.raises(c.Arret):
        executer(c, tmp_path, "astra")
    d = journal(c, tmp_path)[-1]
    assert d["statut"] == "INTERROMPU" and d["cout_usd"] == d["cout_pire_usd"]


def test_gemini_blocage_et_pensees_exclues_du_texte(c, tmp_path):
    c.TRANSPORT = FauxTransport(flux_gemini())
    assert executer(c, tmp_path, "carbon") == "OK"
    d = journal(c, tmp_path)[-1]
    assert d["types_blocs"] == ["thought", "text"]
    texte = (tmp_path / "cellules" / f"{d['cellule']}.md").read_text(encoding="utf-8")
    assert "je réfléchis" not in texte
    c.TRANSPORT = FauxTransport(flux_gemini(fin="SAFETY", texte=""))
    assert c.executer_cellule(tmp_path, "E1-T1", "B", SAIN, [], 100.0, c.APPELANTS) == "REFUS"


def test_kimi_usage_absent_compte_au_pire(c, tmp_path):
    c.TRANSPORT = FauxTransport(FauxFlux(corps={"model": "kimi-k3.1-pro", "choices": [
        {"message": {"content": "x"}, "finish_reason": "stop"}]}))
    with pytest.raises(c.Arret) as e:
        executer(c, tmp_path, "kimi")
    d = journal(c, tmp_path)[-1]
    assert e.value.code == c.CODE_GARDE and d["statut"] == "USAGE_ABSENT" and d["cout_usd"] == d["cout_pire_usd"]


# ---------- 4. garde de motifs ----------

TEMOINS = {
    "nom de personne": "L'arbitre est Lazar.",
    "identifiant de session": "Voir session_0123456789abcdefFAUX pour la suite.",
    "identifiant de session (forme UUID)": "Trace 123e4567-e89b-12d3-a456-426614174000.",
    "courriel": "Écrire à contact@exemple.org.",
    "chemin interne": "Le fichier est sous /home/quelqu-un/depot/.",
    "identifiant d'accord": "Accordé par GO-2026-11-20-31.",
    "identifiant de registre": "Consigné en R-3676.",
}


def test_chaque_motif_a_son_temoin(c):
    assert set(TEMOINS) == {nom for nom, _ in c.MOTIFS_INTERDITS}


@pytest.mark.parametrize("categorie", sorted(TEMOINS))
def test_garde_motifs_artefact_refus_nomme_rien_envoye(c, tmp_path, categorie):
    t = FauxTransport()
    c.TRANSPORT = t
    with pytest.raises(c.Arret) as e:
        executer(c, tmp_path, "carbon", prompt=SAIN + TEMOINS[categorie])
    assert e.value.code == c.CODE_MOTIF and categorie in str(e.value)
    assert t.appels == [] and not (tmp_path / "essais").exists()
    refus = [x for x in c.lire_journal(tmp_path) if "refus_motifs" in x]
    assert refus and categorie in refus[0]["categories"]
    assert TEMOINS[categorie] not in json.dumps(refus, ensure_ascii=False)  # jamais le texte trouvé


def test_garde_motifs_sain_textes_du_script(c):
    c.fixer_composition(["fable", "opus", "argon", "kimi", "astra", "carbon"])
    assert "Lazar" not in c.PREAMBULE_GABARIT and "arbitrée par un humain." in c.PREAMBULE_GABARIT
    assert c.motifs_trouves(c.preambule()) == []
    assert all(c.motifs_trouves(x) == [] for x in c.CONSIGNES.values())
    assert c.motifs_trouves(json.dumps(c.QUESTIONS_JEV, ensure_ascii=False)) == []
    sain = "Une empreinte sha256=" + "ab" * 32 + ", une règle R1, un tour E3-T2, une loi N(0, 1), 3/2 et a/b."
    assert c.motifs_trouves(sain) == []


def test_garde_motifs_artefact_jev_rien_envoye(c, tmp_path):
    appels = []
    with pytest.raises(c.Arret) as e:
        c.auditer_jev(tmp_path, "E1-T1-meta-A", "Texte de Lazar.", c.QUESTIONS_JEV, 10.0,
                      {"jev": lambda *a: appels.append(a)})
    assert e.value.code == c.CODE_MOTIF and appels == []


# ---------- de bout en bout, par doublures des appelants ----------

def doublures(c, prompts):
    fins = {"anthropic": "end_turn", "gemini": "STOP", "openai": "stop", "kimi": "stop"}

    def appelant(m, prompt, max_tokens):
        prompts.append(prompt)
        usage = {"entree": 100, "sortie": 200}
        if m["fournisseur"] == "gemini":
            usage.update(reflexion=10, ecart_total=0)
        return c.Reponse(texte="Proposition. FIN-DE-CELLULE", modele_servi=m["id"], fin=fins[m["fournisseur"]],
                         usage=usage, usage_lu=True)
    return {f: appelant for f in fins}




def test_etage1_de_bout_en_bout_et_verification(c, tmp_path, capsys):
    faits = tmp_path / "faits.md"
    faits.write_text("Fait 1 (HYPOTHÈSE) : texte sain.\n", encoding="utf-8")
    sortie = tmp_path / "run"
    prompts = []
    argv = ["etage1", "--fable", "--argon", "--astra", "--cle-anthropic", "MA_CLE", "--faits", str(faits),
            "--sortie", str(sortie), "--plafond-usd", "40"]
    assert c.principal(argv, appelants=doublures(c, prompts)) == c.CODE_FINI
    assert len(prompts) == 6
    assert all(c.motifs_trouves(p) == [] and "arbitrée par un humain." in p and "trois" in p for p in prompts)
    compo = json.loads((sortie / "especes.json").read_text(encoding="utf-8"))
    assert compo["especes"] == ["fable", "argon", "astra"]
    assert c.principal(["verifier", str(sortie)]) == c.CODE_FINI
    out = capsys.readouterr()
    assert "tout tient" in out.out and CLE_ANTHROPIC not in out.out + out.err
    autre = charger()
    autre.TRANSPORT = reseau_interdit
    argv_autre = ["etage1", "--fable", "--carbon", "--astra", "--cle-anthropic", "MA_CLE", "--sortie", str(sortie)]
    assert autre.principal(argv_autre, appelants=doublures(autre, [])) == c.CODE_USAGE  # artefact : autres espèces
