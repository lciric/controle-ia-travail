"""Essais du collisionneur v9-v7 : copie des essais v9-v6 (cd4c1337…), rejoués sur le v9-v7, adaptés là où le v9-v7 change
(réglages d'Argon, d'Opus et budget de Carbon ; V-1 au texte exact de la vérification de Fable, 523dda37…, section 6 ; leur
remarque 1), marqués « v9-v7 », plus la section v9-v7 en fin de fichier (corrections 1 à 9 de la réflexion d'Opus,
28ce8440…, section 8). Les essais des copies des quatre dossiers à reprendre lisent, par git, les seuls journaux et
compositions de la branche des versements (REF_RUNS_COLLISIONNEURS, DEPOT_COLLISIONNEURS), jamais une réponse de modèle ;
absente : essais sautés. En-tête des essais v9-v6, inchangé :

Essais du collisionneur v9-v6 : copie des essais v9-v5 (624b5229…), rejoués sur le v9-v6, adaptés là où le v9-v6 change
(provision de Carbon à 49 152, marqués « v9-v6 »), plus la section v9-v6 en fin de fichier (CO-1 à CO-3 de la contre-lecture
du v9-v5, préfixe de --cle-openai, réglages de Carbon). En-tête des essais v9-v5, inchangé :

Essais du collisionneur v9-v5 (GO-2026-11-21-57). Partie reprise : les essais v9-v3 (8c38dc2f…) et leur complément 1
(58ddaa24…), rejoués sur le v9-v5, avec trois écarts seulement : (1) le chemin du script (collisionneur_v9_v5.py) et le nom
du module chargé ; (2) l'essai qui lisait le run réel sous runs/ ne lit plus qu'une copie désignée par COPIE_RUN_DOPAMINE
(absente : essai sauté), comme dans les essais v9-v4 ; (3) test_identifiants_et_table_des_prix attend Neon (écart voulu).
Partie neuve : section v9-v5, en fin de fichier (Neon, règle du plafond large, --cle-openai). Hors réseau : transport,
transport des comptages, horloge et sommeil remplacés par des doublures ; toute ouverture de connexion lève une erreur.
Chaque garde a un cas sain et un artefact (R5) ; chaque motif de la garde de motifs a son témoin positif.

Lancement : PYTHONPATH=src .venv/bin/python -B -m pytest -q docs/notes/collisionneur-v9/test_collisionneur_v9_v7.py
"""
import importlib.util
import io
import json
import os
import socket
import urllib.error
from pathlib import Path

import pytest

CHEMIN = Path(__file__).with_name("collisionneur_v9_v7.py")
CLE_GEMINI, CLE_OPENAI, CLE_ANTHROPIC = "cle-gemini-secrete-123", "cle-openai-secrete-456", "cle-anthropic-secrete-789"
SAIN = "mot " * 1000  # 4 000 caractères, aucun motif
TEXTE_JEV = "mot " * 1000  # v9-v2 (C3, point 4) : pire cas de Jev non nul


def charger():
    spec = importlib.util.spec_from_file_location("collisionneur_v9_v7_essai", CHEMIN)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def reseau_interdit(*args, **kwargs):
    raise AssertionError("appel réseau réel interdit dans les essais")


class FauxCompteur:
    """v9-v3 : doublure du transport des comptages. Reconnaît l'interface par l'adresse, lit le texte envoyé et rend un
    compte de ⌊caractères / 2,5⌋ (la garde du v9-v2), ou le compte forcé par `compte`, ou lève l'erreur `erreur`."""

    def __init__(self, compte=None, erreur=None, corps=None):
        self.compte, self.erreur, self.corps, self.appels = compte, erreur, corps, []

    def __call__(self, requete, delai, locale=False):
        corps = json.loads(requete.data)
        url = requete.full_url
        self.appels.append({"url": url, "corps": corps, "delai": delai, "locale": locale,
                            "entetes": {k.lower(): v for k, v in requete.header_items()}})
        if self.erreur is not None:
            raise self.erreur
        if url.endswith("/v1/messages/count_tokens"):
            texte, champ = corps["messages"][0]["content"], "input_tokens"
        elif url.endswith(":countTokens"):
            texte, champ = corps["contents"][0]["parts"][0]["text"], "totalTokens"
        elif url.endswith("/responses/input_tokens"):
            texte, champ = corps["input"], "input_tokens"
        else:
            raise AssertionError(f"adresse de comptage inattendue : {url}")
        n = self.compte if self.compte is not None else int(len(texte) / 2.5)
        reponse = self.corps if self.corps is not None else {champ: n}
        return FauxFlux(corps=reponse)


@pytest.fixture
def c(monkeypatch):
    module = charger()  # module neuf à chaque essai : composition vide
    module.dormis = []
    monkeypatch.setattr(module, "TRANSPORT", reseau_interdit)
    module.compteur = FauxCompteur()
    monkeypatch.setattr(module, "TRANSPORT_COMPTE", module.compteur)
    monkeypatch.setattr(socket, "create_connection", reseau_interdit)  # v9-v3 : aucune connexion, pas même un comptage
    monkeypatch.setattr(socket.socket, "connect", reseau_interdit)
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
                   "kimi": "kimi-k3.1-pro", "astra": "gpt-6.2-astra", "carbon": "gemini-4-carbon",
                   "neon": "gemini-4-neon"}  # v9-v5 : Neon (écart voulu)
    for e, m in c.CATALOGUE.items():
        assert len(m["prix"]) == 2 and m["prix"][0] > 0 and m["prix"][1] > 0
        assert m["delai_s"] > 0 and m["max"] > 0 and m["max_relance"] >= m["max"]
        assert (m["provision"] > 0) == (m["fournisseur"] == "gemini")
        assert m["car_par_jeton"] == (2.0 if e == "kimi" else 2.5)  # v9-v2 (C4) ; v9-v3 : Kimi, sans comptage, à 2
    texte = CHEMIN.read_text(encoding="utf-8")
    for source in ("R-2677", "R-3676", "R-1756", "R-1049", "plan-chiffre-credits-claude-v1.md",
                   "page-prix-gemini-api-20261121T134918Z.html"):  # v9-v5 : source du prix de Neon
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
    t = FauxTransport(flux_gemini(pensees=49152))  # v9-v6 : provision de Carbon 49 152 (v9-v5 : 32 768)
    c.TRANSPORT = t
    assert executer(c, tmp_path, "carbon") == "OK"
    corps = t.appels[0]["corps"]
    # v9-v7 (correction 2) : budget envoyé 32 768, séparé de la provision comptée (49 152)
    assert corps["generationConfig"]["thinkingConfig"] == {"thinkingBudget": 32768, "includeThoughts": True}
    assert corps["generationConfig"]["maxOutputTokens"] == 65536
    assert t.appels[0]["url"].endswith("gemini-4-carbon:streamGenerateContent?alt=sse")
    e = journal(c, tmp_path)[-1]
    assert e["statut"] == "OK" and e["cout_usd"] == round(500 * 4 / 1e6 + (50 + 49152) * 20 / 1e6, 4)  # v9-v6


def test_garde_a_artefact_sortie_au_dela_de_la_sortie_comptee(c, tmp_path):  # v9-v7 (V-1)
    m = c.CATALOGUE["argon"]
    comptee = m["max"] + m["provision"]  # sortie comptée au pire cas du premier envoi
    c.TRANSPORT = FauxTransport(flux_gemini(modele="gemini-4-argon", pensees=comptee - 50 + 1))
    with pytest.raises(c.Arret) as e:
        executer(c, tmp_path, "argon")
    assert e.value.code == c.CODE_GARDE and len(c.TRANSPORT.appels) == 1
    d = journal(c, tmp_path)[-1]
    assert d["statut"] == "REFLEXION_HORS_PROVISION"
    assert d["cout_usd"] == round(500 * m["prix"][0] / 1e6 + (comptee + 1) * m["prix"][1] / 1e6, 4)  # coût réel compté
    assert not c.chemin_cellule(tmp_path, d["cellule"]).exists()


def test_garde_a_sain_reflexion_au_dela_du_budget_sous_la_sortie_comptee(c, tmp_path):  # v9-v7 (V-1)
    """Le budget de réflexion est une limite souple chez Google : une réponse complète dont les pensées dépassent le budget
    envoyé, et dont la sortie facturée tient sous la sortie comptée au pire cas, est gardée, au coût réel."""
    m = c.CATALOGUE["argon"]
    c.TRANSPORT = FauxTransport(flux_gemini(modele="gemini-4-argon", pensees=m["provision"] + 1))
    assert executer(c, tmp_path, "argon") == "OK"
    d = journal(c, tmp_path)[-1]
    assert d["cout_usd"] == round(500 * m["prix"][0] / 1e6 + (50 + m["provision"] + 1) * m["prix"][1] / 1e6, 4)
    assert d["cout_usd"] <= d["cout_pire_usd"] and c.chemin_cellule(tmp_path, d["cellule"]).exists()
    c.TRANSPORT = FauxTransport(flux_gemini(modele="gemini-4-argon", pensees=m["max"] + m["provision"] - 50))  # bord
    assert executer(c, tmp_path / "bord", "argon") == "OK"


def test_garde_a_provision_comptee_avant_l_envoi(c, tmp_path):
    c.fixer_composition(["carbon", "kimi"])
    m = c.MODELES["B"]
    assert c.cout_pire_cas(m, 0, 65536) == pytest.approx((65536 + 49152) * 20 / 1e6)  # v9-v6
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
    assert c.cout_pire_cas(m, 2500, 0) == pytest.approx(1000 * 4 / 1e6 + 16384 * 20 / 1e6)  # v9-v7 : Argon 4 / 20, 16 384
    c.TRANSPORT = FauxTransport(flux_gemini(modele="gemini-4-argon", entree=1600))  # sain : 1 600 = 4 000 / 2,5
    assert executer(c, tmp_path, "argon") == "OK"


def test_garde_b_artefact_entree_au_dela_de_la_garde(c, tmp_path):
    # v9-v3 : la garde est le compte (1 600, doublure à 2,5 caractères) plus la tolérance : 1 648 ; artefact juste au-delà
    assert c.garde_entree(1600) == 1648
    c.TRANSPORT = FauxTransport(flux_gemini(modele="gemini-4-argon", entree=c.garde_entree(1600) + 1))
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
    statut = c.auditer_jev(tmp_path, "E1-T1-meta-A", TEXTE_JEV, c.QUESTIONS_JEV, 10.0, c.APPELANTS)
    assert statut == "INTERROMPU" and len(t.appels) == 1
    e = c.audits_jev(tmp_path)[-1]
    assert e["cout_usd"] == round(len(TEXTE_JEV) / 3 / 1e6 * c.JEV["prix_entree"], 4) > 0


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
    assert [a["corps"]["max_tokens"] for a in t.appels] == [c.MAX_FABLE_V3, 64000]  # v9-v3 : plafond de Fable relevé
    assert c.MAX_FABLE_V3 == 49000


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


# ======================================================================================================================
# v9-v2 : un essai (au moins) par trou fermé après la contre-lecture contre-lecture-collisionneur-v9-v1.md
# ======================================================================================================================

# ---------- B1 : sortie d'Anthropic non lue ----------

def flux_anthropic_sans_usage_final():
    f = flux_anthropic()
    lignes = []
    for brute in f.lignes:
        l = brute.decode("utf-8").rstrip("\r\n")
        if l.startswith("data: ") and '"message_delta"' in l:
            d = json.loads(l[6:])
            d.pop("usage")
            l = "data: " + json.dumps(d)
        lignes.append(l)
    return FauxFlux(lignes)


def test_b1_artefact_message_delta_sans_usage_compte_au_pire(c, tmp_path):
    c.TRANSPORT = FauxTransport(flux_anthropic_sans_usage_final())
    with pytest.raises(c.Arret) as e:
        executer(c, tmp_path, "fable")
    d = journal(c, tmp_path)[-1]
    assert e.value.code == c.CODE_GARDE and d["statut"] == "USAGE_ABSENT"
    assert d["cout_usd"] == d["cout_pire_usd"] > 0


def test_b1_sain_message_delta_avec_usage(c, tmp_path):
    c.TRANSPORT = FauxTransport(flux_anthropic(sortie=200))
    assert executer(c, tmp_path, "fable") == "OK"
    assert journal(c, tmp_path)[-1]["usage"]["sortie"] == 200


# ---------- B2 : formes du nom et chemins du dépôt ----------

TEMOINS_B2 = {
    "nom collé": "LazarCiric",
    "nom au tiret bas": "lazar_ciric",
    "un seul accent (1)": "Ćiric",
    "un seul accent (2)": "Cirić",
    "accents décomposés": "C\u0301iric\u0301",
    "cyrillique": "Лазар Ћирић",
    "docs/sources": "voir docs/sources/x",
    "docs/ racine": "voir docs/sha256sums-lancement-v2.txt",
    "runs/": "voir runs/x",
    "scripts/": "voir scripts/x",
    "CLAUDE.md": "voir CLAUDE.md",
}


@pytest.mark.parametrize("nom", sorted(TEMOINS_B2))
def test_b2_artefact_forme_refusee(c, nom):
    assert c.motifs_trouves(TEMOINS_B2[nom]) != []


@pytest.mark.parametrize("texte", ["Lazarsfeld (1944) sur la décision de vote.",
                                   "Documentation publique : https://exemple.org/docs/guide et https://exemple.org/runs/1"])
def test_b2_sain_pas_de_refus(c, texte):
    assert c.motifs_trouves(texte) == []


# ---------- B3 : écriture mathématique ----------

@pytest.mark.parametrize("texte", [r"Soit $f:\mathbb{R}^d\to\mathbb{R}$ mesurable.", r"et $T:\Omega\to\Omega$ ergodique."])
def test_b3_sain_ecriture_mathematique(c, texte):
    assert c.motifs_trouves(texte) == []


def test_b3_artefact_chemin_windows_toujours_refuse(c):
    assert [n for n, _ in c.motifs_trouves(r"C:\Users\quelqu-un\depot")] == ["chemin interne"]


# ---------- B4 : interruption ou usage incomplet comptés au plus grand du pire cas et de l'usage lu ----------

def test_b4_artefact_flux_inacheve_usage_partiel_plus_cher_que_le_pire(c, tmp_path):
    c.TRANSPORT = FauxTransport(flux_gemini(modele="gemini-4-argon", pensees=60000, sans_fin=True))
    with pytest.raises(c.Arret) as e:
        executer(c, tmp_path, "argon")
    d = journal(c, tmp_path)[-1]
    attendu = round(500 * 4 / 1e6 + (50 + 60000) * 20 / 1e6, 4)  # v9-v7 : Argon compté 4 / 20
    assert e.value.code == c.CODE_ECHEC and d["statut"] == "INTERROMPU"
    assert d["cout_usd"] == attendu > d["cout_pire_usd"]


def test_b4_artefact_total_absent_usage_partiel_plus_cher_que_le_pire(c, tmp_path):
    c.TRANSPORT = FauxTransport(flux_gemini(modele="gemini-4-argon", pensees=60000, total=None))
    with pytest.raises(c.Arret):
        executer(c, tmp_path, "argon")
    d = journal(c, tmp_path)[-1]
    assert d["statut"] == "USAGE_ABSENT" and d["cout_usd"] > d["cout_pire_usd"]


# ---------- C1 : Jev sans usage compté au pire ----------

def test_c1_artefact_jev_ok_sans_usage_compte_au_pire(c, tmp_path):
    reponse = {"model": c.JEV["id"], "answers": {q: {"type": "noul", "noul": 0.5} for q in c.QUESTIONS_JEV}}
    statut = c.auditer_jev(tmp_path, "E1-T1-meta-A", TEXTE_JEV, c.QUESTIONS_JEV, 10.0,
                           {"jev": lambda *a: {"reponse": reponse}})
    e = c.audits_jev(tmp_path)[-1]
    assert statut == "OK" and e["cout_usd"] == round(len(TEXTE_JEV) / 3 / 1e6 * c.JEV["prix_entree"], 4) > 0


def test_c1_sain_jev_avec_usage_compte_reel(c, tmp_path):
    reponse = {"model": c.JEV["id"], "answers": {q: {"type": "noul", "noul": 0.5} for q in c.QUESTIONS_JEV},
               "usage": {"input_tokens": 1000}}
    c.auditer_jev(tmp_path, "E1-T1-meta-A", TEXTE_JEV, c.QUESTIONS_JEV, 10.0, {"jev": lambda *a: {"reponse": reponse}})
    assert c.audits_jev(tmp_path)[-1]["cout_usd"] == round(1000 / 1e6 * c.JEV["prix_entree"], 4)


# ---------- C2 : identifiant de session nu ; nom de variable courant ----------

def test_c2_artefact_identifiant_nu(c):
    assert [n for n, _ in c.motifs_trouves("trace 01" + "a1B2c3D4e5F6g7H8i9J0kL")] == ["identifiant de session"]


def test_c2_sain_nom_de_variable(c):
    assert c.motifs_trouves("la matrice session_embeddings et session_level") == []


# ---------- C3 : épreuves par retrait qui ne cassaient rien ----------

def test_c3_verifier_signale_un_motif_dans_un_prompt_archive(c, tmp_path, capsys):
    sortie = tmp_path / "run"
    faits = tmp_path / "faits.md"
    faits.write_text("Fait 1 (HYPOTHÈSE) : texte sain.\n", encoding="utf-8")
    argv = ["etage1", "--fable", "--argon", "--cle-anthropic", "MA_CLE", "--faits", str(faits), "--sortie", str(sortie)]
    assert c.principal(argv, appelants=doublures(c, [])) == c.CODE_FINI
    prompt = sorted((sortie / "essais").glob("*.prompt.txt"))[0]
    texte = prompt.read_text(encoding="utf-8") + "Voir session_0123456789abcdefFAUX.\n"
    prompt.write_text(texte, encoding="utf-8")
    Path(str(prompt) + ".sha256").write_text(f"{c.empreinte(texte)}  {prompt.name}\n", encoding="utf-8")
    journal_brut = (sortie / "journal.jsonl").read_text(encoding="utf-8").replace(
        c.empreinte(texte.rsplit("Voir session_", 1)[0]), c.empreinte(texte))
    (sortie / "journal.jsonl").write_text(journal_brut, encoding="utf-8")
    problemes = c.verifier(sortie)
    assert any("motif interdit dans le prompt envoyé" in p for p in problemes)


def test_c3_jev_test_garde_de_motifs(c, monkeypatch, capsys):
    appels = []
    monkeypatch.setattr(c, "MOTIFS_INTERDITS", c.MOTIFS_INTERDITS + (("témoin", c.re.compile("connexion")),))
    assert c.principal(["jev-test"], appelants={"jev": lambda *a: appels.append(a)}) == c.CODE_MOTIF
    assert appels == []


def test_c3_adresse_tierce_d_openai_refusee_sans_appel(c, monkeypatch):
    t = FauxTransport()
    c.TRANSPORT = t
    monkeypatch.setenv("OPENAI_BASE_URL", "https://tiers.exemple/v1")
    c.fixer_composition(["astra", "kimi"])
    rep = c.appeler_openai(c.MODELES["B"], SAIN, 100)
    assert rep.echec and not rep.interrompue and t.appels == []


# ---------- C4 : entrée à 2,5 caractères par jeton, contrôlée pour toutes les espèces ----------

@pytest.mark.parametrize("espece", ["fable", "opus", "astra", "kimi"])
def test_c4_table_a_deux_et_demi(c, espece):
    assert c.CATALOGUE[espece]["car_par_jeton"] == (2.0 if espece == "kimi" else 2.5)  # v9-v3 : Kimi à 2


def test_c4_sain_entree_a_la_borne_chez_fable(c, tmp_path):
    c.TRANSPORT = FauxTransport(flux_anthropic(entree=1600))  # 4 000 caractères / 2,5
    assert executer(c, tmp_path, "fable") == "OK"


@pytest.mark.parametrize("espece", ["fable", "astra", "kimi"])
def test_c4_artefact_entree_au_dela_de_la_garde_hors_google(c, tmp_path, espece):
    au_dela = c.garde_entree(1600) + 1  # v9-v3 : garde comptée (compte 1 600 plus tolérance)
    if espece == "fable":
        actions = [flux_anthropic(entree=au_dela)]
    elif espece == "astra":
        final = final_openai()
        final.corps["usage"]["input_tokens"] = au_dela
        actions = [cree_openai(), final]
    else:
        k = corps_kimi()
        k.corps["usage"]["prompt_tokens"] = 2001  # v9-v3 : Kimi, estimation 4 000 / 2 = 2 000, sans tolérance
        actions = [k]
    c.TRANSPORT = FauxTransport(*actions)
    with pytest.raises(c.Arret) as e:
        executer(c, tmp_path, espece)
    assert e.value.code == c.CODE_GARDE and journal(c, tmp_path)[-1]["statut"] == "ENTREE_HORS_GARDE"


# ---------- C5 : adresse locale reconnue par son nom d'hôte ----------

@pytest.mark.parametrize("url,attendu", [("http://127.0.0.1:8789", True), ("http://localhost:8789/v1", True),
                                         ("http://127.0.0.1:1@tiers.exemple/", False),
                                         ("http://localhost:1@tiers.exemple:80/", False),
                                         ("https://127.0.0.1:8789", False), ("http://127.0.0.1", False),
                                         ("http://127.0.0.1.tiers.exemple:80", False)])
def test_c5_adresse_locale(c, url, attendu):
    assert c.adresse_locale(url) is attendu


def test_c5_artefact_relais_kimi_tiers_refuse_sans_appel(c, monkeypatch):
    t = FauxTransport()
    c.TRANSPORT = t
    monkeypatch.setenv("KIMI_RELAIS_URL", "http://127.0.0.1:1@tiers.exemple/")
    c.fixer_composition(["kimi", "astra"])
    rep = c.appeler_kimi(c.MODELES["A"], SAIN, 100)
    assert rep.echec and t.appels == []


def test_c5_artefact_openai_tiers_deguise_refuse_sans_appel(c, monkeypatch):
    t = FauxTransport()
    c.TRANSPORT = t
    monkeypatch.setenv("OPENAI_BASE_URL", "http://127.0.0.1:1@tiers.exemple/v1")
    c.fixer_composition(["astra", "kimi"])
    rep = c.appeler_openai(c.MODELES["B"], SAIN, 100)
    assert rep.echec and t.appels == []


# ======================================================================================================================
# v9-v3 : comptage de l'entrée avant l'envoi, ligne de dépense, plafond de Fable, reprise. Chaque garde neuve : un cas
# sain et un artefact (R5). Aucun réseau : comptages par FauxCompteur, envois par FauxTransport.
# ======================================================================================================================

# v9-v5 (comme v9-v4) : jamais de lecture sous runs/ ; seule une copie du run, désignée par COPIE_RUN_DOPAMINE, est lue
# (absente : essai sauté). L'assertion 49 000 de cet essai valait à l'état du run de 14:05Z, le 20 novembre.
RUN_REEL = Path(os.environ.get("COPIE_RUN_DOPAMINE", "/chemin/absent/copie-run-dopamine"))


class SuiteCompteur(FauxCompteur):
    """Doublure qui lève, dans l'ordre, les erreurs données, puis compte normalement."""

    def __init__(self, *erreurs):
        super().__init__()
        self.suite = list(erreurs)

    def __call__(self, requete, delai, locale=False):
        if self.suite:
            self.erreur = self.suite.pop(0)
        else:
            self.erreur = None
        return super().__call__(requete, delai, locale)


@pytest.mark.parametrize("espece,adresse,champ", [
    ("fable", "https://api.anthropic.com/v1/messages/count_tokens", "input_tokens"),
    ("opus", "https://api.anthropic.com/v1/messages/count_tokens", "input_tokens"),
    ("carbon", "https://generativelanguage.googleapis.com/v1beta/models/gemini-4-carbon:countTokens", "totalTokens"),
    ("argon", "https://generativelanguage.googleapis.com/v1beta/models/gemini-4-argon:countTokens", "totalTokens"),
    ("astra", "https://api.openai.com/v1/responses/input_tokens", "input_tokens")])
def test_v3_sain_compte_par_l_interface_avant_l_envoi(c, tmp_path, espece, adresse, champ):
    flux = {"fable": lambda: [flux_anthropic()], "opus": lambda: [flux_anthropic(modele="claude-opus-5-5")],
            "carbon": lambda: [flux_gemini()], "argon": lambda: [flux_gemini(modele="gemini-4-argon")],
            "astra": lambda: [cree_openai(), final_openai()]}[espece]()
    ordre = []
    compteur = c.TRANSPORT_COMPTE
    t = FauxTransport(*flux)
    c.TRANSPORT_COMPTE = lambda r, d, l=False: (ordre.append("compte"), compteur(r, d, l))[1]
    c.TRANSPORT = lambda r, d, l=False: (ordre.append("envoi"), t(r, d, l))[1]
    assert executer(c, tmp_path, espece) == "OK"
    assert ordre[0] == "compte" and ordre.count("compte") == 1
    a = compteur.appels[0]
    assert a["url"] == adresse and a["delai"] == c.DELAI_COMPTE_S
    envoye = t.appels[0]["corps"]
    if espece in ("fable", "opus"):
        assert a["corps"] == {"model": c.CATALOGUE[espece]["id"], "messages": envoye["messages"]}
        assert a["entetes"]["x-api-key"] == CLE_ANTHROPIC and a["entetes"]["anthropic-version"] == "2023-06-01"
    elif espece == "astra":
        assert a["corps"] == {"model": "gpt-6.2-astra", "input": envoye["input"]}
        assert a["entetes"]["authorization"] == f"Bearer {CLE_OPENAI}"
    else:
        assert a["corps"] == {"contents": envoye["contents"]} and a["entetes"]["x-goog-api-key"] == CLE_GEMINI
    d = journal(c, tmp_path)[-1]
    m = c.CATALOGUE[espece]
    assert d["compte_entree"] == 1600 and d["garde_entree"] == c.garde_entree(1600) == 1648
    assert d["compte_par_interface"] is True and d["source_compte"]
    assert d["cout_pire_usd"] == round(1648 / 1e6 * m["prix"][0] + (m["max"] + m["provision"]) / 1e6 * m["prix"][1], 4)


def test_v3_kimi_sans_interface_estimation_prudente(c, tmp_path):
    c.TRANSPORT = FauxTransport(corps_kimi())
    assert executer(c, tmp_path, "kimi") == "OK"
    assert c.TRANSPORT_COMPTE.appels == []  # aucune interface de comptage pour Kimi
    d = journal(c, tmp_path)[-1]
    assert d["compte_entree"] == d["garde_entree"] == 2000 and d["compte_par_interface"] is False


ERREURS_COMPTE = {"400": http_erreur(400, f"clé {CLE_ANTHROPIC} refusée"), "503": http_erreur(503, "surcharge"),
                  "connexion": urllib.error.URLError(ConnectionRefusedError("refusée")),
                  "délai": socket.timeout("délai dépassé")}


@pytest.mark.parametrize("espece", ["fable", "carbon", "astra"])
@pytest.mark.parametrize("cas", sorted(ERREURS_COMPTE))
def test_v3_artefact_comptage_impossible_rien_n_est_envoye(c, tmp_path, espece, cas):
    c.TRANSPORT_COMPTE = FauxCompteur(erreur=ERREURS_COMPTE[cas])
    c.TRANSPORT = FauxTransport()  # aucun envoi permis
    with pytest.raises(c.Arret) as e:
        executer(c, tmp_path, espece)
    assert e.value.code == c.CODE_COMPTE and "COMPTE_IMPOSSIBLE" in str(e.value)
    assert c.TRANSPORT.appels == [] and len(c.TRANSPORT_COMPTE.appels) == 1  # pas de reprise hors 429
    assert journal(c, tmp_path) == [] and not (tmp_path / "essais").exists()
    refus = [x for x in c.lire_journal(tmp_path) if "refus_avant_envoi" in x]
    assert len(refus) == 1 and refus[0]["motif"] == "COMPTE_IMPOSSIBLE"
    assert CLE_ANTHROPIC not in json.dumps(refus) and CLE_ANTHROPIC not in str(e.value)
    assert c.depense(tmp_path) == 0


@pytest.mark.parametrize("corps", [{}, {"input_tokens": -1}, {"input_tokens": True}, {"input_tokens": "1600"},
                                   ["liste"]])
def test_v3_artefact_reponse_de_comptage_mal_formee(c, tmp_path, corps):
    c.TRANSPORT_COMPTE = FauxCompteur(corps=corps)
    c.TRANSPORT = FauxTransport()
    with pytest.raises(c.Arret) as e:
        executer(c, tmp_path, "fable")
    assert e.value.code == c.CODE_COMPTE and c.TRANSPORT.appels == []


def test_v3_comptage_repris_sur_429_seulement(c, tmp_path):
    c.TRANSPORT_COMPTE = SuiteCompteur(http_erreur(429, "trop"))  # sain : 429 puis compte
    c.TRANSPORT = FauxTransport(flux_anthropic())
    assert executer(c, tmp_path, "fable") == "OK"
    assert len(c.TRANSPORT_COMPTE.appels) == 2 and c.dormis == [10]


def test_v3_garde_invraisemblance_sain_et_artefact(c, tmp_path):
    c.TRANSPORT_COMPTE = FauxCompteur(compte=500)  # sain : 4 000 / 8, à la borne
    c.TRANSPORT = FauxTransport(flux_anthropic(entree=500))
    assert executer(c, tmp_path / "sain", "fable") == "OK"
    c.TRANSPORT_COMPTE = FauxCompteur(compte=499)  # artefact : sous la borne
    c.TRANSPORT = FauxTransport()
    with pytest.raises(c.Arret) as e:
        executer(c, tmp_path / "artefact", "fable")
    assert e.value.code == c.CODE_COMPTE and "COMPTE_INVRAISEMBLABLE" in str(e.value) and c.TRANSPORT.appels == []


def test_v3_incident_du_tour_2_pire_cas_sur_le_compte_exact(c, tmp_path):
    """Le cas du 20 novembre : l'estimation par les caractères (4 000 / 2,5 = 1 600) sous-estimait l'entrée réelle.
    Le pire cas se calcule sur le compte (3 000) : un plafond entre les deux refuse l'envoi avant l'envoi."""
    c.fixer_composition(["fable", "kimi"], nom_cle_anthropic="MA_CLE")
    m = c.MODELES["A"]
    pire_estime = c.cout_pire_cas(m, len(SAIN), m["max"])
    pire_compte = c.cout_pire_garde(m, c.garde_entree(3000), m["max"])
    assert pire_compte > pire_estime
    c.TRANSPORT_COMPTE = FauxCompteur(compte=3000)
    c.TRANSPORT = FauxTransport()  # artefact : plafond entre l'estimation et le compte → refus, rien n'est envoyé
    with pytest.raises(c.Arret) as e:
        c.executer_cellule(tmp_path / "artefact", "E1-T1", "A", SAIN, [], (pire_estime + pire_compte) / 2, c.APPELANTS)
    assert e.value.code == c.CODE_PLAFOND and "PLAFOND" in str(e.value) and c.TRANSPORT.appels == []
    assert [x["motif"] for x in c.lire_journal(tmp_path / "artefact")] == ["PLAFOND"]
    c.TRANSPORT = FauxTransport(flux_anthropic(entree=3000))  # sain : plafond au-dessus, entrée facturée = compte
    assert c.executer_cellule(tmp_path / "sain", "E1-T1", "A", SAIN, [], pire_compte + 0.001, c.APPELANTS) == "OK"
    d = journal(c, tmp_path / "sain")[-1]
    assert d["statut"] == "OK" and d["cout_pire_usd"] == round(pire_compte, 4)


def test_v3_verification_apres_coup_gardee(c, tmp_path):
    c.TRANSPORT_COMPTE = FauxCompteur(compte=3000)
    c.TRANSPORT = FauxTransport(flux_anthropic(entree=c.garde_entree(3000)))  # sain : à la garde
    assert executer(c, tmp_path / "sain", "fable") == "OK"
    c.TRANSPORT = FauxTransport(flux_anthropic(entree=c.garde_entree(3000) + 1))  # artefact : au-delà, après coup
    with pytest.raises(c.Arret) as e:
        executer(c, tmp_path / "artefact", "fable")
    assert e.value.code == c.CODE_GARDE and journal(c, tmp_path / "artefact")[-1]["statut"] == "ENTREE_HORS_GARDE"


def test_v3_ligne_sain_et_artefact(c, tmp_path):
    c.fixer_composition(["fable", "kimi"], nom_cle_anthropic="MA_CLE")
    m = c.MODELES["A"]
    pire = c.cout_pire_garde(m, c.garde_entree(1600), m["max"])
    tmp_path.mkdir(exist_ok=True)
    c.ajouter_journal(tmp_path, {"cellule": "X", "essai": 1, "statut": "OK", "cout_usd": 4.10, "sha256_script": "x"})
    c.ouvrir_ligne(tmp_path, pire - 0.001)  # artefact : ligne juste sous le pire cas
    lg = c.ligne_ouverte(tmp_path)
    assert lg["depense_avant"] == 4.10 and c.depense_ligne(tmp_path, lg) == 0
    c.TRANSPORT = FauxTransport()
    with pytest.raises(c.Arret) as e:
        c.executer_cellule(tmp_path, "E1-T1", "A", SAIN, [], 100.0, c.APPELANTS)
    assert e.value.code == c.CODE_PLAFOND and "LIGNE" in str(e.value) and c.TRANSPORT.appels == []
    with pytest.raises(c.Arret) as e:  # un run garde sa ligne
        c.ouvrir_ligne(tmp_path, pire + 0.001)
    assert e.value.code == c.CODE_USAGE
    autre = tmp_path / "sain"
    autre.mkdir()
    c.ajouter_journal(autre, {"cellule": "X", "essai": 1, "statut": "OK", "cout_usd": 4.10, "sha256_script": "x"})
    c.ouvrir_ligne(autre, pire + 0.001)  # sain : ligne juste au-dessus
    c.ouvrir_ligne(autre, pire + 0.001)  # même montant : pas de seconde ouverture
    assert len([x for x in c.lire_journal(autre) if "ligne_ouverte" in x]) == 1
    c.TRANSPORT = FauxTransport(flux_anthropic())
    assert c.executer_cellule(autre, "E1-T1", "A", SAIN, [], 100.0, c.APPELANTS) == "OK"


def test_v3_ligne_comptee_depuis_son_ouverture(c, tmp_path):
    """La ligne ne compte que la dépense faite depuis son ouverture : 4,10 USD dépensés avant ne la diminuent pas."""
    c.fixer_composition(["fable", "kimi"], nom_cle_anthropic="MA_CLE")
    c.ajouter_journal(tmp_path, {"cellule": "X", "essai": 1, "statut": "OK", "cout_usd": 4.10, "sha256_script": "x"})
    c.ouvrir_ligne(tmp_path, 3.0)
    c.TRANSPORT = FauxTransport(flux_anthropic())
    assert c.executer_cellule(tmp_path, "E1-T1", "A", SAIN, [], 100.0, c.APPELANTS) == "OK"


# ---------- reprise d'un run v9-v2 arrêté au tour 2, simulée de bout en bout ----------

def charger_v2():
    spec = importlib.util.spec_from_file_location("collisionneur_v9_v2_pour_reprise",
                                                  Path(__file__).with_name("collisionneur_v9_v2.py"))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def run_v2_arrete_au_tour_2(tmp_path, monkeypatch):
    """Tour III.1 complet sous le v9-v2, puis la cellule III.2 de Fable arrêtée par ENTREE_HORS_GARDE (le cas réel)."""
    v2 = charger_v2()
    monkeypatch.setattr(v2, "DORMIR", lambda s: None)
    v2.TRANSPORT = FauxTransport(flux_anthropic(), flux_gemini(),
                                 flux_anthropic(fin="max_tokens", entree=10 ** 6, texte="Critique coupée"))
    faits, question = tmp_path / "faits.md", tmp_path / "question.md"
    faits.write_text("Fait sain : un énoncé neutre.\n", encoding="utf-8")
    question.write_text("Question saine : quelle expérience trancherait ?\n", encoding="utf-8")
    dossier = tmp_path / "run"
    code = v2.principal(["etage3", "--fable", "--carbon", "--cle-anthropic", "MA_CLE", "--sortie", str(dossier),
                         "--faits", str(faits), "--question", str(question), "--plafond-usd", "30"])
    assert code == v2.CODE_GARDE
    assert v2.statut_courant(dossier, "E3-T2-critique-croisee-A") == "ENTREE_HORS_GARDE"
    return v2, dossier


def test_v3_reprise_sans_declaration_refusee(c, tmp_path, monkeypatch):
    _, dossier = run_v2_arrete_au_tour_2(tmp_path, monkeypatch)
    c.TRANSPORT = FauxTransport()
    code = c.principal(["etage3", "--fable", "--carbon", "--cle-anthropic", "MA_CLE", "--sortie", str(dossier),
                        "--plafond-usd", "30", "--ligne-usd", "25.90"])
    assert code == c.CODE_USAGE and c.TRANSPORT.appels == [] and c.TRANSPORT_COMPTE.appels == []
    assert not any("ligne_ouverte" in x or "changement_script" in x for x in c.lire_journal(dossier))


def test_v3_reprise_declaree_rejoue_les_tours_2_et_3_sans_le_tour_1(c, tmp_path, monkeypatch):
    v2, dossier = run_v2_arrete_au_tour_2(tmp_path, monkeypatch)
    essai1 = dossier / "essais" / "E3-T2-critique-croisee-A.essai1.prompt.txt"
    avant = {p.name: p.read_bytes() for p in (dossier / "essais").iterdir()}
    cellules_t1 = {p.name: p.read_bytes() for p in (dossier / "cellules").iterdir()}
    c.TRANSPORT = FauxTransport(flux_anthropic(), flux_gemini(), flux_anthropic(), flux_gemini())
    code = c.principal(["etage3", "--fable", "--carbon", "--cle-anthropic", "MA_CLE", "--sortie", str(dossier),
                        "--plafond-usd", "30", "--ligne-usd", "25.90", "--reprise"])
    assert code == c.CODE_FINI
    assert len(c.TRANSPORT.appels) == 4 and len(c.TRANSPORT_COMPTE.appels) == 4  # tours 2 et 3 seulement
    assert not list((dossier / "essais").glob("E3-T1-*.essai2.*"))  # aucun essai neuf au tour 1
    for nom, octets in avant.items():  # l'essai arrêté et le tour 1 restent tels quels
        assert (dossier / "essais" / nom).read_bytes() == octets
    for nom, octets in cellules_t1.items():
        assert (dossier / "cellules" / nom).read_bytes() == octets
    assert essai1.exists() and (dossier / "essais" / "E3-T2-critique-croisee-A.essai2.prompt.txt").exists()
    assert essai1.read_text(encoding="utf-8") == (dossier / "essais" /
                                                  "E3-T2-critique-croisee-A.essai2.prompt.txt").read_text(encoding="utf-8")
    j = c.lire_journal(dossier)
    ch = [x for x in j if "changement_script" in x]
    assert len(ch) == 1 and ch[0]["changement_script"]["vers"] == c.empreinte_script()
    assert ch[0]["changement_script"]["de"] == v2.empreinte_script()
    assert [x["essai"] for x in c.essais_journal(dossier, "E3-T2-critique-croisee-A")] == [1, 2]
    assert c.essais_journal(dossier, "E3-T2-critique-croisee-A")[-1]["max_tokens"] == c.MAX_FABLE_V3
    assert c.verifier(dossier) == []  # sain : changement déclaré
    # artefact : la même trace sans la déclaration du changement de script
    lignes = (dossier / "journal.jsonl").read_text(encoding="utf-8").splitlines()
    (dossier / "journal.jsonl").write_text("\n".join(l for l in lignes if "changement_script" not in l) + "\n",
                                           encoding="utf-8")
    problemes = c.verifier(dossier)
    assert problemes and all("le script a changé pendant le run" in p for p in problemes)


def test_v3_reprise_second_lancement_sans_nouvelle_declaration(c, tmp_path, monkeypatch):
    _, dossier = run_v2_arrete_au_tour_2(tmp_path, monkeypatch)
    c.TRANSPORT = FauxTransport()  # le passage s'arrête au plafond avant tout envoi
    args = ["etage3", "--fable", "--carbon", "--cle-anthropic", "MA_CLE", "--sortie", str(dossier),
            "--plafond-usd", "0.01", "--ligne-usd", "25.90", "--reprise"]
    assert c.principal(args) == c.CODE_PLAFOND
    assert c.principal(args[:-1]) == c.CODE_PLAFOND  # déjà déclarée : --reprise n'est plus exigée
    assert len([x for x in c.lire_journal(dossier) if "changement_script" in x]) == 1
    assert c.TRANSPORT.appels == []


# ---------- devis de reprise et plafond de Fable ----------

def test_v3_devis_reprise_sain_et_artefact(c, tmp_path, monkeypatch, capsys):
    _, dossier = run_v2_arrete_au_tour_2(tmp_path, monkeypatch)
    r = c.devis_reprise(dossier, 25.90)
    totaux = list(r["essais"].values())
    assert totaux == sorted(totaux)  # le pire cas croît avec le plafond de Fable
    assert r["retenu"] is not None and r["essais"][r["retenu"]] <= 25.90
    assert r["retenu"] == max(r["essais"]) or r["essais"][r["retenu"] + 1000] > 25.90
    assert all(not x["valide"] for x in r["detail"]["cellules"])  # tours 2 et 3 entiers à faire
    assert c.principal(["devis-reprise", str(dossier), "--ligne-usd", "0.5"]) == c.CODE_PLAFOND  # artefact
    assert "Plafond de Fable retenu : None" in capsys.readouterr().out


@pytest.mark.skipif(not RUN_REEL.exists(), reason="copie du run absente (COPIE_RUN_DOPAMINE)")
def test_v3_plafond_de_fable_calcule_sur_le_run_reel(c, capsys):
    """Lecture seule du run réel : le plafond de la table est le plus grand qui tient sous 25,90 USD."""
    avant = {p: p.stat().st_mtime_ns for p in RUN_REEL.rglob("*")}
    r = c.devis_reprise(RUN_REEL, 25.90)
    assert r["retenu"] == c.MAX_FABLE_V3 == 49000
    assert r["essais"][49000] <= 25.90 < r["essais"][50000]
    assert {p: p.stat().st_mtime_ns for p in RUN_REEL.rglob("*")} == avant
    assert not any(x["motifs"] for x in r["detail"]["cellules"] if x.get("motifs") is not None)


# ======================================================================================================================
# Complément 1 des essais v9-v3 (test_collisionneur_v9_v3_complement_1.py, 58ddaa24…), versé ici sans changement : quatre
# artefacts et leurs cas sains (R5). Seule différence : les doublures sont celles de ce fichier (plus d'import).
# ======================================================================================================================

@pytest.mark.parametrize("adresse", ["https://tiers.exemple/v1", "http://127.0.0.1:1@tiers.exemple/v1"])
def test_complement_artefact_comptage_openai_vers_un_tiers_refuse_sans_appel(c, tmp_path, monkeypatch, adresse):
    """La clé d'OpenAI ne part jamais vers un tiers, pas même pour un comptage."""
    monkeypatch.setenv("OPENAI_BASE_URL", adresse)
    c.TRANSPORT = FauxTransport()
    with pytest.raises(c.Arret) as e:
        executer(c, tmp_path, "astra")
    assert e.value.code == c.CODE_COMPTE and "COMPTE_IMPOSSIBLE" in str(e.value)
    assert c.TRANSPORT_COMPTE.appels == [] and c.TRANSPORT.appels == []


def test_complement_sain_comptage_openai_par_la_boucle_locale(c, tmp_path, monkeypatch):
    monkeypatch.setenv("OPENAI_BASE_URL", "http://127.0.0.1:8123/v1")
    c.TRANSPORT = FauxTransport(cree_openai(), final_openai())
    assert executer(c, tmp_path, "astra") == "OK"
    a = c.TRANSPORT_COMPTE.appels[0]
    assert a["url"] == "http://127.0.0.1:8123/v1/responses/input_tokens" and a["locale"] is True


def test_complement_suivre_scripts_sain_et_artefact(c):
    essai = lambda h, n: {"cellule": "X", "essai": n, "sha256_script": h}  # noqa: E731
    sain = [essai("a", 1), {"changement_script": {"de": "a", "vers": "b"}}, essai("b", 2)]
    assert c.suivre_scripts(sain) == ("b", [])
    artefact = [essai("a", 1), {"changement_script": {"de": "z", "vers": "b"}}, essai("b", 2)]  # déclaré depuis un autre
    courant, problemes = c.suivre_scripts(artefact)
    assert courant == "b" and len(problemes) == 1 and "déclaré depuis z" in problemes[0]


@pytest.mark.parametrize("garde", ["LIGNE", "PLAFOND"])
def test_complement_relance_refusee_avant_l_envoi_par_la_ligne_ou_le_plafond(c, tmp_path, garde):
    """Première passe coupée (2,451 USD), relance au pire à 3,2165 USD : 5,6675 USD. Une ligne ou un plafond de 5 USD
    refuse la relance avant l'envoi ; à 6 USD, la relance part."""
    c.fixer_composition(["fable", "kimi"], nom_cle_anthropic="MA_CLE")
    coupe = lambda: flux_anthropic(fin="max_tokens", sortie=c.MAX_FABLE_V3, texte="Texte coupé")  # noqa: E731

    def lancer(dossier, montant, *flux):
        dossier.mkdir()
        if garde == "LIGNE":
            c.ouvrir_ligne(dossier, montant)
        c.TRANSPORT = FauxTransport(*flux)
        return c.executer_cellule(dossier, "E1-T1", "A", SAIN, [], montant if garde == "PLAFOND" else 100.0, c.APPELANTS)

    with pytest.raises(c.Arret) as e:  # artefact
        lancer(tmp_path / "artefact", 5.0, coupe())
    assert e.value.code == c.CODE_PLAFOND and garde in str(e.value) and len(c.TRANSPORT.appels) == 1
    assert [x["motif"] for x in c.lire_journal(tmp_path / "artefact") if "refus_avant_envoi" in x] == [garde]
    assert [x["statut"] for x in c.essais_journal(tmp_path / "artefact")] == ["TRONQUE"]
    assert lancer(tmp_path / "sain", 6.0, coupe(), flux_anthropic()) == "OK"  # sain
    assert [a["corps"]["max_tokens"] for a in c.TRANSPORT.appels] == [c.MAX_FABLE_V3, 64000]


# ======================================================================================================================
# v9-v5 (GO-2026-11-21-57) : espèce Neon, règle du plafond large (Carbon et Neon), option --cle-openai. Chaque garde neuve :
# un cas sain et un artefact (R5). Aucun réseau : comptages par FauxCompteur, envois par FauxTransport.
# ======================================================================================================================

import hashlib  # noqa: E402
import itertools  # noqa: E402

CLE_OPENAI_2 = "cle-openai-deux-secrete-000"


def lettre_de(c, espece):
    return next(l for l in c.LETTRES if c.MODELES[l]["espece"] == espece)


def charger_v3():
    spec = importlib.util.spec_from_file_location("collisionneur_v9_v3_reference", CHEMIN.with_name("collisionneur_v9_v3.py"))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


# ---------- v9-v5, 1. Neon au catalogue ----------

def test_v5_neon_au_catalogue_seule_difference_avec_la_v3(c):
    v3 = charger_v3()
    assert c.CATALOGUE["neon"] == {"id": "gemini-4-neon", "fournisseur": "gemini", "prix": (3.0, 15.0), "max": 65536,
                                   "max_relance": 65536, "budget": 32768,  # v9-v7 : budget = provision
                                   "provision": 32768, "car_par_jeton": 2.5, "delai_s": 5400}
    assert set(c.CATALOGUE) == set(v3.CATALOGUE) | {"neon"}
    changes = {"carbon": dict(provision=49152, budget=32768),  # v9-v6, v9-v7 (correction 2)
               "argon": dict(prix=(4.0, 20.0), max=32768, max_relance=32768, budget=8192, provision=16384),  # v9-v7 (3)
               "opus": dict(max=64000)}  # v9-v7 (correction 4)
    for espece in v3.CATALOGUE:  # aucune autre espèce ne change
        assert c.CATALOGUE[espece] == dict(v3.CATALOGUE[espece], **changes.get(espece, {}))
    assert c.ORDRE_CATALOGUE == v3.ORDRE_CATALOGUE + ("neon",)  # Neon en fin d'ordre
    assert c.NOMS_CLES == v3.NOMS_CLES and c.VERSION == "collisionneur-v9-v7"  # v9-v7
    for nom in ("TOLERANCE_COMPTE", "CAR_PAR_JETON_MAX", "ATTENTES_429", "PLAFOND_DEFAUT_USD", "RATIO_PROJECTION_ENTREE",
                "CAR_SORTIE_MAX", "MAX_FABLE_V3", "CODE_GARDE", "CODE_COMPTE", "STATUTS_GARDE", "REFUS_GEMINI"):
        assert getattr(c, nom) == getattr(v3, nom), nom
    assert c.CODE_REGLAGE == 9 and c.CODE_REGLAGE not in (0, 1, 2, 3, 4, 5, 6, 7, 8)


def test_v5_lettres_des_compositions_sans_neon_inchangees(c):
    v3 = charger_v3()
    for n in (2, 3, 6):
        for especes in itertools.combinations(v3.ORDRE_CATALOGUE, n):
            attendu = {l: m["espece"] for l, m in v3.fixer_composition(list(especes), "MA_CLE").items()}
            assert {l: m["espece"] for l, m in c.fixer_composition(list(especes), "MA_CLE").items()} == attendu
    c.fixer_composition(list(c.ORDRE_CATALOGUE), "MA_CLE")  # les sept
    assert c.LETTRES == tuple("ABCDEFG") and c.MODELES["G"]["espece"] == "neon"
    assert c.MODELES["G"]["nom_cle"] == "GEMINI_API_KEY"


def test_v5_prix_de_neon_egal_a_la_page_versee(c):
    page = CHEMIN.resolve().parents[3] / "docs" / "sources" / "prix" / "page-prix-gemini-api-20261121T134918Z.html"
    brut = page.read_bytes()
    assert hashlib.sha256(brut).hexdigest().startswith("40202cdd")
    texte = brut.decode("utf-8")
    i = texte.index("## Gemini 4 Neon")
    section = texte[i:texte.index("\n## ", i + 5)]
    standard = section[section.index('title="Standard"'):section.index('title="Batch"')]
    entree = standard[standard.index("* Input price"):standard.index("* Output price")]
    sortie = standard[standard.index("* Output price"):standard.index("* Context caching price")]
    assert "$3.00" in entree and "$15.00" in sortie and "including thinking tokens" in sortie
    assert c.CATALOGUE["neon"]["prix"] == (3.0, 15.0)
    assert "40202cdd" in CHEMIN.read_text(encoding="utf-8")


def test_v5_identifiant_de_neon_dans_la_liste_versee(c):
    liste = json.loads(CHEMIN.with_name("liste-modeles-gemini-20261121T134904Z.json").read_text(encoding="utf-8"))
    assert liste["point"] == "GET v1beta/models (models.list)"
    modeles = {m["name"]: m for m in liste["modeles"]}
    neon = modeles["models/" + c.CATALOGUE["neon"]["id"]]
    assert neon["outputTokenLimit"] == c.CATALOGUE["neon"]["max"] == 65536 and neon["thinking"] is True
    assert "countTokens" in neon["supportedGenerationMethods"]


def test_v5_option_neon_au_devis_et_aux_etages(c, tmp_path, capsys):
    faits = tmp_path / "faits.md"
    faits.write_text("Fait sain.\n", encoding="utf-8")
    assert c.principal(["devis", "--neon", "--faits", str(faits)]) == c.CODE_USAGE  # une seule espèce : refus
    assert c.principal(["devis", "--carbon", "--neon", "--faits", str(faits)]) == c.CODE_FINI
    out = capsys.readouterr().out
    assert "B = neon (gemini-4-neon) : prix 3 / 15 USD par million, sortie 65536 (relance 65536), provision 32768" in out
    assert "A = carbon (gemini-4-carbon)" in out


# ---------- v9-v5, 2. Neon : cas sain, garde de dépense, ligne ----------

def test_v5_neon_cas_sain_budget_plafond_cle_et_cout(c, tmp_path):
    t = FauxTransport(flux_gemini(modele="gemini-4-neon", pensees=32768, candidats=16000))
    c.TRANSPORT = t
    assert executer(c, tmp_path, "neon") == "OK"
    assert len(t.appels) == 1
    a = t.appels[0]
    assert a["url"].endswith("/gemini-4-neon:streamGenerateContent?alt=sse")
    assert a["entetes"]["x-goog-api-key"] == CLE_GEMINI
    assert a["corps"]["generationConfig"] == {"maxOutputTokens": 65536,
                                              "thinkingConfig": {"thinkingBudget": 32768, "includeThoughts": True}}
    compte = c.TRANSPORT_COMPTE.appels[0]
    assert compte["url"].endswith("/gemini-4-neon:countTokens") and compte["entetes"]["x-goog-api-key"] == CLE_GEMINI
    e = journal(c, tmp_path)[-1]
    assert e["statut"] == "OK" and e["modele_demande"] == "gemini-4-neon" and e["espece"] == "neon"
    assert e["cout_usd"] == round(500 * 3 / 1e6 + (16000 + 32768) * 15 / 1e6, 4)
    assert e["max_tokens"] == 65536 and e["provision_reflexion"] == 32768
    assert c.chemin_cellule(tmp_path, e["cellule"]).exists()
    assert CLE_GEMINI not in (tmp_path / "journal.jsonl").read_text(encoding="utf-8")


def test_v5_neon_garde_de_depense_comptee_avant_l_envoi(c, tmp_path):
    c.fixer_composition(["neon", "kimi"])
    m = c.MODELES[lettre_de(c, "neon")]
    garde = c.garde_entree(int(len(SAIN) / 2.5))
    pire = c.cout_pire_garde(m, garde, 65536)
    assert pire == pytest.approx(garde * 3 / 1e6 + (65536 + 32768) * 15 / 1e6)  # provision comptée au prix de sortie
    c.TRANSPORT = FauxTransport()  # artefact : plafond juste sous le pire cas → aucun envoi
    with pytest.raises(c.Arret) as e:
        executer(c, tmp_path, "neon", plafond=pire - 1e-6)
    assert e.value.code == c.CODE_PLAFOND and c.TRANSPORT.appels == []
    refus = [x for x in c.lire_journal(tmp_path) if "refus_avant_envoi" in x]
    assert [x["motif"] for x in refus] == ["PLAFOND"] and journal(c, tmp_path) == []
    c.TRANSPORT = FauxTransport(flux_gemini(modele="gemini-4-neon"))  # sain : plafond juste au-dessus
    assert executer(c, tmp_path, "neon", plafond=pire + 1e-6) == "OK"
    assert journal(c, tmp_path)[-1]["cout_pire_usd"] == round(pire, 4)


def test_v5_neon_ligne_de_depense_sain_et_artefact(c, tmp_path):
    c.fixer_composition(["neon", "kimi"])
    pire = c.cout_pire_garde(c.MODELES[lettre_de(c, "neon")], c.garde_entree(int(len(SAIN) / 2.5)), 65536)
    dossier = tmp_path / "artefact"
    dossier.mkdir()
    c.ouvrir_ligne(dossier, pire - 1e-6)
    c.TRANSPORT = FauxTransport()
    with pytest.raises(c.Arret) as e:
        executer(c, dossier, "neon")
    assert e.value.code == c.CODE_PLAFOND and "LIGNE" in str(e.value) and c.TRANSPORT.appels == []
    dossier = tmp_path / "sain"
    dossier.mkdir()
    c.ouvrir_ligne(dossier, pire + 1e-6)
    c.TRANSPORT = FauxTransport(flux_gemini(modele="gemini-4-neon"))
    assert executer(c, dossier, "neon") == "OK"


def test_v5_neon_budget_refuse_par_google_echec_sans_renvoi(c, tmp_path):
    """Le budget de réflexion n'a jamais été envoyé à Neon : un refus (400) est un échec avant traitement, coût 0, un seul
    envoi, aucune relance ni aucun repli ; la clé n'est pas écrite."""
    corps = json.dumps({"error": {"code": 400, "message": f"thinking_budget is not supported (key {CLE_GEMINI})"}})
    c.TRANSPORT = FauxTransport(http_erreur(400, corps))
    with pytest.raises(c.Arret) as e:
        executer(c, tmp_path, "neon")
    assert e.value.code == c.CODE_ECHEC and len(c.TRANSPORT.appels) == 1
    d = journal(c, tmp_path)[-1]
    assert d["statut"] == "ECHEC" and d["cout_usd"] == 0 and not d["interrompue"]
    assert CLE_GEMINI not in (tmp_path / "journal.jsonl").read_text(encoding="utf-8") and CLE_GEMINI not in str(e.value)


# ---------- v9-v5, 3. arrêt en MAX_TOKENS ----------

@pytest.mark.parametrize("espece", ["neon", "carbon"])
def test_v5_max_tokens_sans_texte_arret_defaut_de_reglage(c, tmp_path, espece):
    """Artefact : MAX_TOKENS sans texte, réflexion lue dans la provision. Défaut de réglage, pas une réponse : code 9, un seul
    envoi (aucune relance au même réglage), aucune cellule, coût réel compté."""
    modele = c.CATALOGUE[espece]["id"]
    c.TRANSPORT = FauxTransport(flux_gemini(texte="", modele=modele, fin="MAX_TOKENS", candidats=0, pensees=32768))
    with pytest.raises(c.Arret) as e:
        executer(c, tmp_path, espece)
    assert e.value.code == c.CODE_REGLAGE and "défaut de réglage" in str(e.value)
    assert len(c.TRANSPORT.appels) == 1
    d = journal(c, tmp_path)[-1]
    prix = c.CATALOGUE[espece]["prix"]
    assert d["statut"] == "MAX_TOKENS_SANS_TEXTE" and d["fin"] == "MAX_TOKENS"
    assert d["cout_usd"] == round(500 * prix[0] / 1e6 + 32768 * prix[1] / 1e6, 4)
    assert not c.chemin_cellule(tmp_path, d["cellule"]).exists()


def test_v5_max_tokens_sans_texte_temoin_argon_hors_regle_relance_comme_la_v3(c, tmp_path):
    """Argon n'est pas sous la règle : comportement v3 inchangé (sortie vide → relance au plafond de relance)."""
    c.TRANSPORT = FauxTransport(flux_gemini(texte="", modele="gemini-4-argon", fin="MAX_TOKENS", candidats=0, pensees=100),
                                flux_gemini(texte="", modele="gemini-4-argon", fin="MAX_TOKENS", candidats=0, pensees=100))
    assert executer(c, tmp_path, "argon") == "VIDE"
    assert [a["corps"]["generationConfig"]["maxOutputTokens"] for a in c.TRANSPORT.appels] == [32768, 32768]  # v9-v7


def test_v5_neon_max_tokens_sortie_hors_compte_reste_garde_de_depense(c, tmp_path):  # v9-v7 (V-1)
    """Ordre des gardes gardé : une sortie facturée au-delà de la sortie comptée est REFLEXION_HORS_PROVISION (code 6),
    avant le défaut de réglage. Sain : des pensées au-delà du budget qui mangent tout le plafond envoyé, sans texte, sont
    le défaut de réglage (code 9), au coût réel."""
    m = c.CATALOGUE["neon"]
    c.TRANSPORT = FauxTransport(flux_gemini(texte="", modele="gemini-4-neon", fin="MAX_TOKENS", candidats=0,
                                            pensees=m["max"] + m["provision"] + 1))
    with pytest.raises(c.Arret) as e:
        executer(c, tmp_path / "artefact", "neon")
    assert e.value.code == c.CODE_GARDE and len(c.TRANSPORT.appels) == 1
    assert journal(c, tmp_path / "artefact")[-1]["statut"] == "REFLEXION_HORS_PROVISION"
    c.TRANSPORT = FauxTransport(flux_gemini(texte="", modele="gemini-4-neon", fin="MAX_TOKENS", candidats=0,
                                            pensees=m["max"]))
    with pytest.raises(c.Arret) as e:
        executer(c, tmp_path / "sain", "neon")
    assert e.value.code == c.CODE_REGLAGE and len(c.TRANSPORT.appels) == 1
    assert journal(c, tmp_path / "sain")[-1]["statut"] == "MAX_TOKENS_SANS_TEXTE"


def test_v5_neon_max_tokens_avec_texte_partiel_relance_comme_la_v3(c, tmp_path):
    """Sain : un texte coupé (TRONQUE) n'est pas le défaut de réglage ; la relance de la v3 part au plafond de relance, avec
    le même budget ; la seconde réponse, complète, est retenue."""
    c.TRANSPORT = FauxTransport(flux_gemini(texte="Début coupé", modele="gemini-4-neon", fin="MAX_TOKENS",
                                            candidats=32768, pensees=32768),
                                flux_gemini(modele="gemini-4-neon"))
    assert executer(c, tmp_path, "neon") == "OK"
    configs = [a["corps"]["generationConfig"] for a in c.TRANSPORT.appels]
    assert [g["maxOutputTokens"] for g in configs] == [65536, 65536]
    assert [g["thinkingConfig"]["thinkingBudget"] for g in configs] == [32768, 32768]
    assert [e["statut"] for e in journal(c, tmp_path)] == ["TRONQUE", "OK"]


# ---------- v9-v5, 4. règle du plafond large ----------

def test_v5_regle_plafond_large_sain_et_bord(c):
    assert c.REGLE_TEXTE_MIN == {"carbon": 16000, "neon": 16000}
    c.fixer_composition(["carbon", "neon"])
    for l in c.LETTRES:
        m = c.MODELES[l]
        for plafond in (m["max"], m["max_relance"]):
            assert c.ecart_regle_texte(m, plafond) is None and plafond - m["provision"] >= 16000
    m = dict(c.MODELES[lettre_de(c, "neon")], provision=65536 - 16000)  # bord : exactement 16 000 jetons de texte, accepté
    assert c.ecart_regle_texte(m, 65536) is None
    assert "15999 jetons de texte < 16000" in c.ecart_regle_texte(m, 65535)
    assert c.ecart_regle_texte(dict(m, provision=0), 65536).endswith("exige une réflexion bornée")
    c.fixer_composition(["argon", "kimi"])  # Argon n'est pas sous la règle
    assert c.ecart_regle_texte(c.MODELES[lettre_de(c, "argon")], 1) is None


@pytest.mark.parametrize("espece", ["carbon", "neon"])
@pytest.mark.parametrize("champ", ["max", "max_relance"])
def test_v5_regle_plafond_large_artefact_refus_a_la_composition(c, monkeypatch, espece, champ):
    reglage = dict(c.CATALOGUE[espece])
    reglage[champ] = reglage["provision"] + 15999
    monkeypatch.setitem(c.CATALOGUE, espece, reglage)
    with pytest.raises(c.Arret) as e:
        c.fixer_composition([espece, "kimi"])
    assert e.value.code == c.CODE_USAGE and "règle du plafond large" in str(e.value)
    assert c.LETTRES == ()  # rien n'est fixé


def test_v5_regle_plafond_large_temoin_argon_non_soumis(c, monkeypatch):
    monkeypatch.setitem(c.CATALOGUE, "argon", dict(c.CATALOGUE["argon"], max=8192 + 100, max_relance=8192 + 100))
    c.fixer_composition(["argon", "kimi"])  # aucun refus : la règle ne vaut que pour Carbon et Neon
    assert c.MODELES[lettre_de(c, "argon")]["max"] == 8292


@pytest.mark.parametrize("champ", ["max", "max_relance"])
def test_v5_regle_plafond_large_artefact_refus_avant_comptage_et_envoi(c, tmp_path, champ):
    """Un réglage changé après la composition est refusé avant tout comptage et tout envoi, consigné au journal."""
    c.fixer_composition(["neon", "kimi"])
    l = lettre_de(c, "neon")
    c.MODELES[l][champ] = c.MODELES[l]["provision"] + 15999
    c.TRANSPORT = FauxTransport()
    with pytest.raises(c.Arret) as e:
        c.executer_cellule(tmp_path, "E1-T1", l, SAIN, [], 100.0, c.APPELANTS)
    assert e.value.code == c.CODE_USAGE and "REGLE_TEXTE_MIN" in str(e.value)
    assert c.TRANSPORT.appels == [] and c.TRANSPORT_COMPTE.appels == []
    assert not (tmp_path / "essais").exists()
    assert [x["motif"] for x in c.lire_journal(tmp_path) if "refus_avant_envoi" in x] == ["REGLE_TEXTE_MIN"]


# ---------- v9-v5, 5. --cle-openai ----------

def test_v5_cle_openai_par_defaut_inchangee(c):
    c.fixer_composition(["astra", "kimi"])
    assert c.MODELES[lettre_de(c, "astra")]["nom_cle"] == "OPENAI_API_KEY"


def test_v5_cle_openai_lue_par_son_nom_pour_le_comptage_et_l_envoi(c, tmp_path, monkeypatch, capsys):
    monkeypatch.setenv("OPENAI_API_KEY_2", CLE_OPENAI_2)
    monkeypatch.delenv("OPENAI_API_KEY")
    c.fixer_composition(["astra", "kimi"], nom_cle_openai="OPENAI_API_KEY_2")
    l = lettre_de(c, "astra")
    assert c.MODELES[l]["nom_cle"] == "OPENAI_API_KEY_2"
    c.verifier_cles()
    t = FauxTransport(cree_openai(), final_openai())
    c.TRANSPORT = t
    assert c.executer_cellule(tmp_path, "E1-T1", l, SAIN, [], 100.0, c.APPELANTS) == "OK"
    assert c.TRANSPORT_COMPTE.appels[0]["entetes"]["authorization"] == f"Bearer {CLE_OPENAI_2}"
    assert len(t.appels) == 2 and all(a["entetes"]["authorization"] == f"Bearer {CLE_OPENAI_2}" for a in t.appels)
    sorties = capsys.readouterr()
    assert CLE_OPENAI_2 not in sorties.out + sorties.err
    for p in tmp_path.rglob("*"):
        if p.is_file():
            assert CLE_OPENAI_2 not in p.read_text(encoding="utf-8", errors="replace")


def test_v5_cle_openai_nommee_absente_comptage_et_envoi_refuses(c, monkeypatch):
    monkeypatch.delenv("OPENAI_API_KEY_2", raising=False)
    c.fixer_composition(["astra", "kimi"], nom_cle_openai="OPENAI_API_KEY_2")
    m = c.MODELES[lettre_de(c, "astra")]
    with pytest.raises(c.RefusCompte) as e:  # OPENAI_API_KEY est présente : elle n'est pas lue à la place
        c.compter_openai(m, SAIN)
    assert e.value.motif == "COMPTE_IMPOSSIBLE" and "OPENAI_API_KEY_2 absente" in str(e.value)
    rep = c.appeler_openai(m, SAIN, 100)
    assert rep.echec.startswith("OPENAI_API_KEY_2 absente") and not rep.interrompue
    assert c.TRANSPORT_COMPTE.appels == []
    with pytest.raises(c.Arret) as e:
        c.verifier_cles()
    assert e.value.code == c.CODE_USAGE and "OPENAI_API_KEY_2" in str(e.value) and CLE_OPENAI not in str(e.value)


@pytest.mark.parametrize("etage", ["etage1", "etage2", "etage3"])
def test_v5_option_cle_openai_aux_trois_etages(c, tmp_path, capsys, monkeypatch, etage):
    """Artefact : la variable nommée est absente → refus d'usage, par son nom, avant toute écriture ; la clé par défaut,
    présente, n'est pas lue à sa place."""
    monkeypatch.delenv("OPENAI_API_KEY_2", raising=False)
    faits = tmp_path / "faits.md"
    faits.write_text("Fait sain.\n", encoding="utf-8")
    sortie = tmp_path / "run"
    args = [etage, "--astra", "--kimi", "--cle-openai", "OPENAI_API_KEY_2", "--sortie", str(sortie)]
    args += {"etage1": ["--faits", str(faits)], "etage2": ["--arbitrage", str(faits)],
             "etage3": ["--faits", str(faits), "--question", str(faits)]}[etage]
    assert c.principal(args) == c.CODE_USAGE
    err = capsys.readouterr().err
    assert "OPENAI_API_KEY_2" in err and CLE_OPENAI not in err
    assert not sortie.exists()


def test_v5_option_cle_openai_nom_mal_forme_refuse_sans_echo(c, tmp_path, capsys):
    """Artefact : une valeur passée par erreur à la place d'un nom est refusée, et jamais répétée."""
    faits = tmp_path / "faits.md"
    faits.write_text("Fait sain.\n", encoding="utf-8")
    valeur = "sk-proj-ceci-ressemble-a-une-cle-0123"
    args = ["etage1", "--astra", "--kimi", "--cle-openai", valeur, "--faits", str(faits), "--sortie", str(tmp_path / "r")]
    assert c.principal(args) == c.CODE_USAGE
    sorties = capsys.readouterr()
    assert valeur not in sorties.out + sorties.err and "mal formé" in sorties.err
    with pytest.raises(c.Arret):
        c.fixer_composition(["astra", "kimi"], nom_cle_openai="mauvais nom")


def test_v5_nom_de_cle_openai_hors_du_sceau_de_composition(c, tmp_path):
    """Changer de clé d'OpenAI entre deux commandes d'un même run ne change pas sa composition scellée."""
    c.fixer_composition(["astra", "neon"])
    c.sceller_composition(tmp_path)
    c.fixer_composition(["astra", "neon"], nom_cle_openai="OPENAI_API_KEY_2")
    c.sceller_composition(tmp_path)  # même composition : aucun arrêt
    assert "OPENAI_API_KEY" not in (tmp_path / "especes.json").read_text(encoding="utf-8")


# ======================================================================================================================
# v9-v6 : corrections de la contre-lecture du v9-v5 (contre-lecture-collisionneur-v9-v5-v1.md, 77041a13…), au code exact
# qu'elle donne (CO-1, CO-2, CO-3), puis les décisions de la mère : préfixe de --cle-openai, réglages de Carbon du v9-v4.
# ======================================================================================================================

def _vide_max(modele):
    return flux_gemini(texte="", modele=modele, fin="MAX_TOKENS", candidats=0, pensees=32768)


# ---------- CO-1 : un défaut de réglage n'est jamais renvoyé au même réglage ----------

def test_v6_defaut_de_reglage_jamais_renvoye_au_meme_reglage(c, tmp_path, monkeypatch, capsys):
    faits = tmp_path / "faits.md"
    faits.write_text("Fait 1 (HYPOTHÈSE) : texte sain.\n", encoding="utf-8")
    sortie = tmp_path / "run"
    argv = ["etage1", "--carbon", "--neon", "--faits", str(faits), "--sortie", str(sortie)]
    c.TRANSPORT = FauxTransport(_vide_max("gemini-4-carbon"))
    assert c.principal(argv) == c.CODE_REGLAGE  # premier lancement : arrêt au code 9, un envoi
    # Artefact : la même commande ne renvoie rien à Carbon ; Neon part ; porte fermée après le tour.
    c.TRANSPORT = FauxTransport(flux_gemini(modele="gemini-4-neon"))
    assert c.principal(argv) == c.CODE_PORTE
    assert [a["url"].split("/")[-1].split(":")[0] for a in c.TRANSPORT.appels] == ["gemini-4-neon"]
    assert [e["statut"] for e in c.essais_journal(sortie, "E1-T1-meta-A")] == ["MAX_TOKENS_SANS_TEXTE"]
    assert "non renvoyée" in capsys.readouterr().out
    # Sain 1 : l'absence acceptée par l'arbitre laisse l'étage finir, sans envoi à Carbon au tour 1.
    c.TRANSPORT = FauxTransport(flux_gemini(modele="gemini-4-carbon"), flux_gemini(modele="gemini-4-neon"))
    assert c.principal(argv + ["--accepter-absence", "E1-T1-meta-A"]) == c.CODE_FINI
    assert [e["statut"] for e in c.essais_journal(sortie, "E1-T1-meta-A")] == ["MAX_TOKENS_SANS_TEXTE"]


def test_v6_defaut_de_reglage_renvoye_si_le_reglage_a_change(c, tmp_path, monkeypatch):
    """Sain 2 : sous un réglage différent, la cellule repart."""
    c.TRANSPORT = FauxTransport(_vide_max("gemini-4-carbon"))
    with pytest.raises(c.Arret) as e:
        executer(c, tmp_path, "carbon")
    assert e.value.code == c.CODE_REGLAGE
    l = lettre_de(c, "carbon")
    cid = c.id_cellule("E1-T1", l)
    assert c.reglage_en_defaut(tmp_path, cid, c.MODELES[l]) is True
    assert c.reglage_en_defaut(tmp_path, cid, dict(c.MODELES[l], provision=24576)) is False
    assert c.reglage_en_defaut(tmp_path, cid, dict(c.MODELES[l], max_relance=131072)) is False
    assert c.reglage_en_defaut(tmp_path, c.id_cellule("E1-T2", l), c.MODELES[l]) is False  # cellule jamais lancée


# ---------- CO-2 : aucun repli sur la clé par défaut, même sans nom dans la composition ----------

def test_v6_cle_openai_sans_nom_dans_la_composition_aucun_repli(c):
    c.fixer_composition(["astra", "kimi"], nom_cle_openai="OPENAI_API_KEY_2")
    m = dict(c.MODELES[lettre_de(c, "astra")], nom_cle=None)  # OPENAI_API_KEY est présente : elle n'est pas lue
    c.TRANSPORT = FauxTransport()
    rep = c.appeler_openai(m, SAIN, 100)
    assert rep.echec and "absent de la composition" in rep.echec and c.TRANSPORT.appels == []
    with pytest.raises(c.RefusCompte) as e:
        c.compter_openai(m, SAIN)
    assert e.value.motif == "COMPTE_IMPOSSIBLE" and c.TRANSPORT_COMPTE.appels == []


# ---------- CO-3 : une sortie vide dont la fin est « STOP » n'est pas le défaut de réglage ----------

@pytest.mark.parametrize("espece", ["carbon", "neon"])
def test_v6_sortie_vide_fin_stop_relancee_comme_la_v3(c, tmp_path, espece):
    modele = c.CATALOGUE[espece]["id"]
    c.TRANSPORT = FauxTransport(flux_gemini(texte="", modele=modele, fin="STOP", candidats=0, pensees=100),
                                flux_gemini(modele=modele))
    assert executer(c, tmp_path, espece) == "OK"
    assert [e["statut"] for e in journal(c, tmp_path)] == ["VIDE", "OK"] and len(c.TRANSPORT.appels) == 2


# ---------- décision de la mère : --cle-openai commence par OPENAI_API_KEY ----------

@pytest.mark.parametrize("nom", ["GEMINI_API_KEY", "TYPESAFE_API_KEY", "MA_CLE", "CLE_OPENAI_API_KEY", "OPENAI_KEY"])
def test_v6_cle_openai_hors_prefixe_refusee(c, tmp_path, capsys, monkeypatch, nom):
    """Artefact : la clé d'un autre fournisseur (présente dans l'environnement) ne part jamais vers OpenAI ; refus au code 1,
    avant toute écriture et tout appel, à la composition comme par la ligne de commande."""
    monkeypatch.setenv("OPENAI_KEY", "cle-quelconque-0000")
    monkeypatch.setenv("CLE_OPENAI_API_KEY", "cle-quelconque-0001")
    with pytest.raises(c.Arret) as e:
        c.fixer_composition(["astra", "kimi"], nom_cle_anthropic="MA_CLE", nom_cle_openai=nom)
    assert e.value.code == c.CODE_USAGE and "OPENAI_API_KEY" in str(e.value) and c.LETTRES == ()
    faits = tmp_path / "faits.md"
    faits.write_text("Fait sain.\n", encoding="utf-8")
    sortie = tmp_path / "run"
    c.TRANSPORT = FauxTransport()
    assert c.principal(["etage1", "--astra", "--kimi", "--cle-openai", nom, "--faits", str(faits), "--sortie",
                        str(sortie)]) == c.CODE_USAGE
    err = capsys.readouterr().err
    assert CLE_GEMINI not in err and CLE_ANTHROPIC not in err and "doit commencer par OPENAI_API_KEY" in err
    assert nom not in err  # le nom refusé n'est pas répété
    assert not sortie.exists() and c.TRANSPORT.appels == [] and c.TRANSPORT_COMPTE.appels == []


@pytest.mark.parametrize("nom", ["OPENAI_API_KEY", "OPENAI_API_KEY_2", "OPENAI_API_KEY2"])
def test_v6_cle_openai_prefixe_accepte(c, nom):
    c.fixer_composition(["astra", "kimi"], nom_cle_openai=nom)
    assert c.MODELES[lettre_de(c, "astra")]["nom_cle"] == nom and c.PREFIXE_CLE_OPENAI == "OPENAI_API_KEY"


# ---------- décision de la mère : réglages de Carbon du v9-v4 ----------

def test_v6_carbon_reprend_les_reglages_du_v4_et_tient_la_regle(c):
    spec = importlib.util.spec_from_file_location("collisionneur_v9_v4_reference", CHEMIN.with_name("collisionneur_v9_v4.py"))
    v4 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(v4)
    assert c.CATALOGUE["carbon"] == dict(v4.CATALOGUE["carbon"], budget=32768)  # ligne du v9-v4, budget v9-v7 en plus
    assert (c.CATALOGUE["carbon"]["max"], c.CATALOGUE["carbon"]["max_relance"], c.CATALOGUE["carbon"]["provision"]) \
        == (65536, 65536, 49152)
    c.fixer_composition(["carbon", "kimi"])
    m = c.MODELES[lettre_de(c, "carbon")]
    for plafond in (m["max"], m["max_relance"]):
        assert c.ecart_regle_texte(m, plafond) is None and plafond - m["provision"] == 16384


def test_v6_carbon_reponse_du_20_novembre_gardee_et_artefact_au_dela(c, tmp_path):
    """Sain : la critique de Carbon du 20 novembre (39 953 jetons de pensées, arrêtée sous 32 768) est gardée sous 49 152 ;
    budget envoyé 49 152. v9-v7 (V-1) : le dépassement relevé ce jour-là (× 1,22), reporté sur 49 152, soit 59 930 jetons
    de pensées et 5 606 de texte sous le plafond envoyé, est gardé. Artefact : sortie facturée au-delà de la sortie comptée
    (65 536 + 49 152) → garde de dépense, code 6, un seul envoi."""
    t = FauxTransport(flux_gemini(entree=27122, pensees=39953, candidats=10298))
    c.TRANSPORT = t
    assert executer(c, tmp_path / "sain", "carbon", prompt="mot " * 20000) == "OK"
    assert t.appels[0]["corps"]["generationConfig"]["thinkingConfig"]["thinkingBudget"] == 32768  # v9-v7 (correction 2)
    c.TRANSPORT = FauxTransport(flux_gemini(pensees=59930, candidats=5606))
    assert executer(c, tmp_path / "depassement", "carbon") == "OK"
    d = c.essais_journal(tmp_path / "depassement")[-1]
    assert d["cout_usd"] == round(500 * 4 / 1e6 + 65536 * 20 / 1e6, 4) and d["cout_usd"] <= d["cout_pire_usd"]
    c.TRANSPORT = FauxTransport(flux_gemini(pensees=65536 + 49152 - 50 + 1))
    with pytest.raises(c.Arret) as e:
        executer(c, tmp_path / "artefact", "carbon")
    assert e.value.code == c.CODE_GARDE and len(c.TRANSPORT.appels) == 1
    assert c.essais_journal(tmp_path / "artefact")[-1]["statut"] == "REFLEXION_HORS_PROVISION"


# ---------- v9-v7 (remarque du vérificateur) : le défaut de réglage se lit sur le dernier essai ----------

def test_v7_defaut_de_reglage_lu_sur_le_dernier_essai(c, tmp_path):
    c.TRANSPORT = FauxTransport(flux_gemini(texte="", fin="STOP", candidats=0, pensees=100), _vide_max("gemini-4-carbon"))
    with pytest.raises(c.Arret) as e:
        executer(c, tmp_path, "carbon")
    assert e.value.code == c.CODE_REGLAGE and [x["statut"] for x in journal(c, tmp_path)] == ["VIDE", "MAX_TOKENS_SANS_TEXTE"]
    l = lettre_de(c, "carbon")
    assert c.reglage_en_defaut(tmp_path, c.id_cellule("E1-T1", l), c.MODELES[l]) is True


# ======================================================================================================================
# v9-v7 : section neuve. Corrections de la réflexion d'Opus en effort maximal (section 8) et de la vérification de Fable.
# ======================================================================================================================

import subprocess  # noqa: E402


def flux_anthropic_credit(apres_texte=False, apres_usage=False, type_erreur="invalid_request_error",
                          message="Your credit balance is too low to access the Anthropic API. Please go to Plans & "
                                  "Billing to upgrade or purchase credits."):
    """v9-v7 : forme relevée le 21 novembre (journaux des runs « méthodes maths » et « dérive v1 ») : message_start,
    début d'un bloc de réflexion, puis une erreur de crédit dans le flux ; aucun texte, aucun usage final."""
    ev = [{"type": "message_start", "message": {"id": "msg_c", "model": "claude-fable-5-2",
                                                 "usage": {"input_tokens": 58000, "output_tokens": 1}}},
          {"type": "content_block_start", "index": 0, "content_block": {"type": "thinking"}}]
    if apres_texte:
        ev += [{"type": "content_block_start", "index": 1, "content_block": {"type": "text", "text": ""}},
               {"type": "content_block_delta", "index": 1, "delta": {"type": "text_delta", "text": "Début"}}]
    if apres_usage:
        ev.append({"type": "message_delta", "delta": {}, "usage": {"output_tokens": 300}})
    ev.append({"type": "error", "error": {"details": None, "type": type_erreur, "message": message}})
    lignes = []
    for e in ev:
        lignes += [f"event: {e['type']}", "data: " + json.dumps(e), ""]
    return FauxFlux(lignes)


def reponse_gemini_lot(texte="Réponse. FIN-DE-CELLULE", entree=500, candidats=50, pensees=100, fin="STOP",
                       modele="gemini-4-carbon"):
    return {"candidates": [{"content": {"parts": [{"text": "je réfléchis", "thought": True}, {"text": texte}]},
                            "finishReason": fin}],
            "usageMetadata": {"promptTokenCount": entree, "candidatesTokenCount": candidats,
                              "thoughtsTokenCount": pensees, "totalTokenCount": entree + candidats + pensees},
            "modelVersion": modele, "responseId": "lot-r1"}


def lot_cree(nom="batches/abc123"):
    return FauxFlux(corps={"name": nom, "metadata": {"state": "BATCH_STATE_PENDING"}})


def lot_en_cours(nom="batches/abc123"):
    return FauxFlux(corps={"name": nom, "metadata": {"state": "BATCH_STATE_RUNNING"}})


def lot_fini(reponse=None, etat="BATCH_STATE_SUCCEEDED", nom="batches/abc123", erreur=None, imbrique=True):
    rep = reponse if reponse is not None else reponse_gemini_lot()
    inl = [{"response": rep, "metadata": {"key": "cellule"}}] if erreur is None else [{"error": erreur}]
    corps = {"name": nom, "done": True, "metadata": {"state": etat},
             "response": {"inlinedResponses": {"inlinedResponses": inl} if imbrique else inl}}
    return FauxFlux(corps=corps)


class TransportParAdresse:
    """v9-v7 : doublure qui répond selon l'adresse (l'ordre des espèces n'a plus d'importance) ; compte les envois."""

    def __init__(self, lot_etats=("BATCH_STATE_SUCCEEDED",)):
        self.appels, self.lot_etats = [], list(lot_etats)

    def __call__(self, requete, delai, locale=False):
        url, corps = requete.full_url, (json.loads(requete.data) if requete.data else None)
        self.appels.append({"url": url, "methode": requete.get_method(), "corps": corps,
                            "entetes": {k.lower(): v for k, v in requete.header_items()}})
        if url.endswith("/v1/messages"):
            return flux_anthropic(modele=corps["model"])
        if ":streamGenerateContent" in url:
            return flux_gemini(modele=url.split("/models/")[1].split(":")[0])
        if url.endswith(":batchGenerateContent"):
            return lot_cree()
        if "/batches/" in url and requete.get_method() == "GET":
            etat = self.lot_etats.pop(0) if self.lot_etats else "BATCH_STATE_SUCCEEDED"
            return lot_fini() if etat == "BATCH_STATE_SUCCEEDED" else lot_en_cours()
        if url.endswith("/responses") and requete.get_method() == "POST":
            return cree_openai()
        if "/responses/resp_1" in url:
            return final_openai()
        raise AssertionError(f"adresse inattendue : {url}")

    def generations(self):
        """Envois de génération (créations), relevés exclus."""
        return [a for a in self.appels if a["methode"] == "POST"]


# ---------- correction 1 (V-1) : la garde porte sur la sortie comptée, au plafond de CET envoi ----------

def test_v7_v1_seuil_lu_sur_le_plafond_de_l_envoi(c, tmp_path, monkeypatch):
    """Le seuil est le plafond envoyé plus la provision : sous un premier plafond plus bas que la relance, une sortie au-delà
    de ce premier plafond plus la provision arrête (code 6), même si elle tiendrait sous la relance."""
    monkeypatch.setitem(c.CATALOGUE, "argon", dict(c.CATALOGUE["argon"], max=20000))
    m = c.CATALOGUE["argon"]
    c.TRANSPORT = FauxTransport(flux_gemini(modele="gemini-4-argon", pensees=20000 + m["provision"] - 50 + 1))
    with pytest.raises(c.Arret) as e:
        executer(c, tmp_path / "artefact", "argon")
    assert e.value.code == c.CODE_GARDE and journal(c, tmp_path / "artefact")[-1]["max_tokens"] == 20000
    c.TRANSPORT = FauxTransport(flux_gemini(modele="gemini-4-argon", pensees=20000 + m["provision"] - 50))
    assert executer(c, tmp_path / "sain", "argon") == "OK"


def test_v7_v1_juger_sans_plafond_lit_la_relance(c):
    c.fixer_composition(["carbon", "kimi"])
    m = c.MODELES[lettre_de(c, "carbon")]
    rep = c.lire_reponse_gemini({"parts": [{"text": "x FIN-DE-CELLULE"}], "finishReason": "STOP",
                                 "usageMetadata": {"promptTokenCount": 10, "candidatesTokenCount": 10,
                                                   "thoughtsTokenCount": 65536 + 49152 - 10,
                                                   "totalTokenCount": 65536 + 49152 + 10},
                                 "modelVersion": "gemini-4-carbon"})
    assert c.juger(m, rep, SAIN, 9.0, 100)[0] == "OK"
    assert c.juger(m, rep, SAIN, 9.0, 100, max_tokens=1000)[0] == "REFLEXION_HORS_PROVISION"


# ---------- correction 2 : budget envoyé, séparé de la provision, journalisé, lu par reglage_en_defaut ----------

@pytest.mark.parametrize("espece,budget,provision,plafond", [("carbon", 32768, 49152, 65536),
                                                             ("argon", 8192, 16384, 32768),
                                                             ("neon", 32768, 32768, 65536)])
def test_v7_budget_envoye_journalise_et_provision_comptee(c, tmp_path, espece, budget, provision, plafond):
    t = FauxTransport(flux_gemini(modele=c.CATALOGUE[espece]["id"]))
    c.TRANSPORT = t
    assert executer(c, tmp_path, espece) == "OK"
    gc = t.appels[0]["corps"]["generationConfig"]
    assert gc == {"maxOutputTokens": plafond, "thinkingConfig": {"thinkingBudget": budget, "includeThoughts": True}}
    d = journal(c, tmp_path)[-1]
    assert (d["budget_reflexion"], d["provision_reflexion"], d["max_tokens"], d["mode_envoi"]) == \
        (budget, provision, plafond, "flux")
    m = c.CATALOGUE[espece]
    assert d["cout_pire_usd"] == round(d["garde_entree"] * m["prix"][0] / 1e6 + (plafond + provision) * m["prix"][1] / 1e6,
                                       4)


@pytest.mark.parametrize("budget", [None, 0, 49153, 32768.0, True])
def test_v7_budget_hors_borne_refuse_a_la_composition(c, monkeypatch, budget):
    ligne = dict(c.CATALOGUE["carbon"])
    if budget is None:
        del ligne["budget"]
    else:
        ligne["budget"] = budget
    monkeypatch.setitem(c.CATALOGUE, "carbon", ligne)
    with pytest.raises(c.Arret) as e:
        c.fixer_composition(["carbon", "kimi"])
    assert e.value.code == c.CODE_USAGE and "budget" in str(e.value)


def test_v7_budget_egal_a_la_provision_accepte(c, monkeypatch):
    monkeypatch.setitem(c.CATALOGUE, "carbon", dict(c.CATALOGUE["carbon"], budget=49152))
    assert c.fixer_composition(["carbon", "kimi"])


def test_v7_reglage_en_defaut_lit_le_budget(c, tmp_path):
    c.TRANSPORT = FauxTransport(_vide_max("gemini-4-carbon"))
    with pytest.raises(c.Arret):
        executer(c, tmp_path, "carbon")
    l = lettre_de(c, "carbon")
    cid = c.id_cellule("E1-T1", l)
    assert c.reglage_en_defaut(tmp_path, cid, c.MODELES[l]) is True
    assert c.reglage_en_defaut(tmp_path, cid, dict(c.MODELES[l], budget=24576)) is False  # budget changé : renvoyée


def test_v7_reglage_en_defaut_essai_du_v6_au_budget_49152_renvoye(c, tmp_path, monkeypatch):
    """Un arrêt au code 9 sous le v9-v6 (budget envoyé = provision = 49 152) : le v9-v7 envoie 32 768, réglage changé,
    la cellule repart (et l'essai du v6 reste tel quel)."""
    spec = importlib.util.spec_from_file_location("collisionneur_v9_v6_reference", CHEMIN.with_name("collisionneur_v9_v6.py"))
    v6 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(v6)
    v6.TRANSPORT_COMPTE = FauxCompteur()
    v6.TRANSPORT = FauxTransport(_vide_max("gemini-4-carbon"))
    v6.fixer_composition(["carbon", "kimi"])
    l = next(x for x in v6.LETTRES if v6.MODELES[x]["espece"] == "carbon")
    with pytest.raises(v6.Arret) as e:
        v6.executer_cellule(tmp_path, "E1-T1", l, SAIN, [], 100.0, v6.APPELANTS)
    assert e.value.code == 9 and "budget_reflexion" not in v6.essais_journal(tmp_path)[-1]
    c.fixer_composition(["carbon", "kimi"])
    assert c.reglage_en_defaut(tmp_path, c.id_cellule("E1-T1", l), c.MODELES[l]) is False


# ---------- correction 3 : Argon ----------

def test_v7_argon_reglages_prix_et_sources(c):
    m = c.CATALOGUE["argon"]
    assert (m["max"], m["max_relance"], m["budget"], m["provision"], m["prix"]) == (32768, 32768, 8192, 16384,
                                                                                     (4.0, 20.0))
    texte = CHEMIN.read_text(encoding="utf-8")
    assert "lignes 347 et 354" in texte and "40202cdd" in texte
    page = CHEMIN.resolve().parents[3] / "docs" / "sources" / "prix" / "page-prix-gemini-api-20261121T134918Z.html"
    if not page.exists():
        pytest.skip("page de prix versée absente")
    lignes = page.read_text(encoding="utf-8").splitlines()
    assert "Gemini 4 Argon" in lignes[304]  # ligne 305 : titre de la section
    assert lignes[346].strip() == "$4.00 starting December 1, 2026." and "Input price" in lignes[343]
    assert lignes[353].strip() == "$20.00 starting December 1, 2026." and "including thinking tokens" in lignes[350]
    assert all("## " not in l for l in lignes[305:410])  # lignes 347 à 410 : toujours dans la section d'Argon
    assert lignes[402].strip() == "$2.00 starting December 1, 2026." and lignes[409].strip() == \
        "$10.00 starting December 1, 2026."  # onglet « Batch » : moitié
    assert "Batch API (50% cost reduction)" in lignes[42]
    liste = json.loads(CHEMIN.with_name("liste-modeles-gemini-20261121T134904Z.json").read_text(encoding="utf-8"))
    modeles = {x["name"]: x for x in liste["modeles"]}
    assert modeles["models/gemini-4-argon"]["outputTokenLimit"] == 32768
    assert "batchGenerateContent" in modeles["models/gemini-4-carbon"]["supportedGenerationMethods"]


def test_v7_argon_pire_cas_et_cout_reel(c, tmp_path):
    t = FauxTransport(flux_gemini(modele="gemini-4-argon", pensees=12000, candidats=9000))
    c.TRANSPORT = t
    assert executer(c, tmp_path, "argon") == "OK"
    d = journal(c, tmp_path)[-1]
    assert d["cout_usd"] == round(500 * 4 / 1e6 + 21000 * 20 / 1e6, 4)
    assert d["cout_pire_usd"] == round(d["garde_entree"] * 4 / 1e6 + (32768 + 16384) * 20 / 1e6, 4)


# ---------- correction 4 : Opus à 64 000 dès le premier envoi ----------

def test_v7_opus_plafond_64000_des_le_premier_envoi(c, tmp_path):
    t = FauxTransport(flux_anthropic(modele="claude-opus-5-5"))
    c.TRANSPORT = t
    assert executer(c, tmp_path, "opus") == "OK"
    assert [a["corps"]["max_tokens"] for a in t.appels] == [64000]
    d = journal(c, tmp_path)[-1]
    assert d["max_tokens"] == 64000 and d["cout_pire_usd"] == round(d["garde_entree"] * 4 / 1e6 + 64000 * 20 / 1e6, 4)


# ---------- correction 5 : --rejuger-essai CELLULE:N, sans réseau ----------

CID_T2_CARBON = "E3-T2-critique-croisee-B"


def run_v3_carbon_arrete(tmp_path, monkeypatch, **flux):
    """Run fabriqué par le v9-v3 lui-même (850df311…) : étage III, Fable et Carbon ; tour III.1 complet ; au tour III.2,
    Fable OK, puis Carbon arrêté par l'ancienne garde des pensées (pensées au-delà de 32 768), code 6. Par défaut, la
    réponse du run « percée » : 44 101 jetons de pensées, sortie facturée 55 125, fin STOP, marqueur présent."""
    v3 = charger_v3()
    assert v3.empreinte_script().startswith("850df311")
    monkeypatch.setattr(v3, "DORMIR", lambda s: None)
    v3.TRANSPORT_COMPTE = FauxCompteur()
    reglage = dict(pensees=44101, candidats=11024)
    reglage.update(flux)
    v3.TRANSPORT = FauxTransport(flux_anthropic(), flux_gemini(), flux_anthropic(), flux_gemini(**reglage))
    faits, question = tmp_path / "faits.md", tmp_path / "question.md"
    faits.write_text("Fait sain : un énoncé neutre.\n", encoding="utf-8")
    question.write_text("Question saine : quelle expérience trancherait ?\n", encoding="utf-8")
    dossier = tmp_path / "run"
    code = v3.principal(["etage3", "--fable", "--carbon", "--cle-anthropic", "MA_CLE", "--sortie", str(dossier),
                         "--faits", str(faits), "--question", str(question), "--plafond-usd", "30",
                         "--ligne-usd", "28"])
    assert code == v3.CODE_GARDE or code == v3.CODE_MODELE
    return v3, dossier


ARGV_REPRISE = ["etage3", "--fable", "--carbon", "--cle-anthropic", "MA_CLE", "--plafond-usd", "30", "--ligne-usd", "28",
                "--reprise"]


def test_v7_rejugement_sain_cellule_ecrite_sans_envoi_puis_tour_3(c, tmp_path, monkeypatch, capsys):
    _, dossier = run_v3_carbon_arrete(tmp_path, monkeypatch)
    e = c.essais_journal(dossier, CID_T2_CARBON)[-1]
    assert e["statut"] == "REFLEXION_HORS_PROVISION" and e["usage"]["sortie"] == 55125
    avant = {p.name: p.read_bytes() for p in (dossier / "essais").iterdir()}
    depense_avant = c.depense(dossier)
    t = TransportParAdresse()
    c.TRANSPORT = t
    code = c.principal(ARGV_REPRISE + ["--sortie", str(dossier), "--rejuger-essai", f"{CID_T2_CARBON}:1"])
    assert code == c.CODE_FINI
    # aucun envoi ni comptage pour la cellule rejugée : seuls les deux envois du tour III.3
    assert len(t.generations()) == 2 and len(c.TRANSPORT_COMPTE.appels) == 2
    assert not list((dossier / "essais").glob(f"{CID_T2_CARBON}.essai2.*"))
    cellule, h = c.lire_sceau(c.chemin_cellule(dossier, CID_T2_CARBON))
    assert h == e["sha256_texte"] and cellule == (dossier / "essais" / f"{CID_T2_CARBON}.essai1.reponse.md").read_text(
        encoding="utf-8")
    for nom, octets in avant.items():
        assert (dossier / "essais" / nom).read_bytes() == octets
    rej = c.rejugements(dossier)
    assert len(rej) == 1 and rej[0]["essai_rejuge"] == 1 and rej[0]["cout_usd"] == 0.0
    assert (rej[0]["sortie_facturee"], rej[0]["sortie_comptee"]) == (55125, 65536 + 32768)
    assert c.verifier(dossier) == []
    assert c.depense(dossier) == round(depense_avant + sum(x["cout_usd"] for x in c.essais_journal(dossier)
                                                            if x["cellule"].startswith("E3-T3")), 4)
    assert "rejugé OK" in capsys.readouterr().out
    assert "OK (rejugement de l'essai 1)" in (dossier / "etat.md").read_text(encoding="utf-8")
    # E3-T3 de Fable a reçu la critique rejugée de Carbon, empreinte comprise
    t3 = c.essais_journal(dossier, "E3-T3-reponse-A")[-1]
    assert {"cellule": CID_T2_CARBON, "sha256": h} in t3["pieces"]


def test_v7_rejugement_idempotent(c, tmp_path, monkeypatch):
    _, dossier = run_v3_carbon_arrete(tmp_path, monkeypatch)
    c.TRANSPORT = TransportParAdresse()
    argv = ARGV_REPRISE + ["--sortie", str(dossier), "--rejuger-essai", f"{CID_T2_CARBON}:1"]
    assert c.principal(argv) == c.CODE_FINI
    journal_avant = (dossier / "journal.jsonl").read_bytes()
    c.TRANSPORT = FauxTransport()  # plus aucun envoi permis
    assert c.principal(argv) == c.CODE_FINI
    assert (dossier / "journal.jsonl").read_bytes() == journal_avant and c.TRANSPORT.appels == []
    assert c.rejuger_essai(dossier, CID_T2_CARBON, 1) is False


def test_v7_rejugement_ligne_ecrite_sans_cellule_reprise_sans_doublon(c, tmp_path, monkeypatch):
    """Arrêt entre la ligne de journal et la cellule : la relance écrit la cellule, sans seconde ligne."""
    _, dossier = run_v3_carbon_arrete(tmp_path, monkeypatch)
    c.fixer_composition(["fable", "carbon"], nom_cle_anthropic="MA_CLE")
    assert c.rejuger_essai(dossier, CID_T2_CARBON, 1) is True
    c.chemin_cellule(dossier, CID_T2_CARBON).unlink()
    Path(str(c.chemin_cellule(dossier, CID_T2_CARBON)) + ".sha256").unlink()
    assert any("rejugement au journal sans cellule" in p for p in c.verifier(dossier))
    assert c.rejuger_essai(dossier, CID_T2_CARBON, 1) is True
    assert len(c.rejugements(dossier)) == 1


ARTEFACTS_REJUGEMENT = {
    "fin MAX_TOKENS": dict(fin="MAX_TOKENS"),
    "marqueur absent": dict(texte="Réponse sans marqueur."),
    "sortie au-delà de la sortie comptée": dict(pensees=65536 + 32768 - 50 + 1, candidats=50),
    "écart de total non nul": dict(total=500 + 11024 + 44101 + 1),
    "entrée au-delà de la garde": dict(entree=10 ** 6),
    "modèle non conforme": dict(modele="gemini-4-argon"),
}


@pytest.mark.parametrize("cas", sorted(ARTEFACTS_REJUGEMENT))
def test_v7_rejugement_artefacts_refuses_rien_n_est_ecrit(c, tmp_path, monkeypatch, cas):
    _, dossier = run_v3_carbon_arrete(tmp_path, monkeypatch, **ARTEFACTS_REJUGEMENT[cas])
    c.TRANSPORT = FauxTransport()  # aucun envoi permis
    code = c.principal(ARGV_REPRISE + ["--sortie", str(dossier), "--rejuger-essai", f"{CID_T2_CARBON}:1"])
    assert code == c.CODE_USAGE and c.TRANSPORT.appels == []
    assert not c.chemin_cellule(dossier, CID_T2_CARBON).exists() and c.rejugements(dossier) == []


def test_v7_rejugement_artefact_statut_ok_ou_autre_refuse(c, tmp_path, monkeypatch):
    """Un essai qui n'est pas REFLEXION_HORS_PROVISION (ici MODELE_DIFFERENT sous le v3) ne se rejuge pas."""
    v3, dossier = run_v3_carbon_arrete(tmp_path, monkeypatch, modele="gemini-4-argon")
    assert v3.statut_courant(dossier, CID_T2_CARBON) == "MODELE_DIFFERENT"
    c.fixer_composition(["fable", "carbon"], nom_cle_anthropic="MA_CLE")
    with pytest.raises(c.Arret) as e:
        c.rejuger_essai(dossier, CID_T2_CARBON, 1)
    assert e.value.code == c.CODE_USAGE and "statut MODELE_DIFFERENT" in str(e.value)


def test_v7_rejugement_artefact_sceau_change(c, tmp_path, monkeypatch):
    _, dossier = run_v3_carbon_arrete(tmp_path, monkeypatch)
    rep = dossier / "essais" / f"{CID_T2_CARBON}.essai1.reponse.md"
    rep.write_text(rep.read_text(encoding="utf-8") + " ajout", encoding="utf-8")
    c.TRANSPORT = FauxTransport()
    code = c.principal(ARGV_REPRISE + ["--sortie", str(dossier), "--rejuger-essai", f"{CID_T2_CARBON}:1"])
    assert code == c.CODE_USAGE and c.TRANSPORT.appels == [] and not c.chemin_cellule(dossier, CID_T2_CARBON).exists()


def test_v7_rejugement_artefact_texte_et_sceau_remplaces_ensemble(c, tmp_path, monkeypatch):
    """Réponse et sceau remplacés ensemble : le sceau tient, mais l'empreinte n'est plus celle du journal."""
    _, dossier = run_v3_carbon_arrete(tmp_path, monkeypatch)
    rep = dossier / "essais" / f"{CID_T2_CARBON}.essai1.reponse.md"
    texte = "Autre réponse. FIN-DE-CELLULE"
    rep.write_text(texte, encoding="utf-8")
    Path(str(rep) + ".sha256").write_text(f"{hashlib.sha256(texte.encode()).hexdigest()}  {rep.name}\n",
                                          encoding="utf-8")
    c.fixer_composition(["fable", "carbon"], nom_cle_anthropic="MA_CLE")
    with pytest.raises(c.Arret) as e:
        c.rejuger_essai(dossier, CID_T2_CARBON, 1)
    assert "empreintes" in str(e.value) and not c.chemin_cellule(dossier, CID_T2_CARBON).exists()


def test_v7_rejugement_artefact_pas_le_dernier_essai(c, tmp_path, monkeypatch):
    _, dossier = run_v3_carbon_arrete(tmp_path, monkeypatch)
    c.fixer_composition(["fable", "carbon"], nom_cle_anthropic="MA_CLE")
    lignes = (dossier / "journal.jsonl").read_text(encoding="utf-8")
    e = json.loads([x for x in lignes.splitlines() if CID_T2_CARBON in x and '"essai"' in x][-1])
    e.update(essai=2, statut="VIDE")
    (dossier / "journal.jsonl").write_text(lignes + json.dumps(e) + "\n", encoding="utf-8")
    with pytest.raises(c.Arret) as x:
        c.rejuger_essai(dossier, CID_T2_CARBON, 1)
    assert "pas le dernier essai" in str(x.value)


@pytest.mark.parametrize("valeur", ["kimi:1", CID_T2_CARBON, f"{CID_T2_CARBON}:0", f"{CID_T2_CARBON}:x",
                                    "E3-T2-critique-croisee-Z:1", f"{CID_T2_CARBON}:7"])
def test_v7_rejugement_forme_refusee(c, tmp_path, monkeypatch, valeur):
    _, dossier = run_v3_carbon_arrete(tmp_path, monkeypatch)
    avant = (dossier / "journal.jsonl").read_bytes() if valeur != f"{CID_T2_CARBON}:7" else None
    c.TRANSPORT = FauxTransport()
    code = c.principal(ARGV_REPRISE + ["--sortie", str(dossier), "--rejuger-essai", valeur])
    assert code == c.CODE_USAGE and c.TRANSPORT.appels == [] and c.rejugements(dossier) == []
    if avant is not None:  # forme refusée avant toute écriture
        assert (dossier / "journal.jsonl").read_bytes() == avant


def test_v7_verifier_artefacts_du_rejugement(c, tmp_path, monkeypatch):
    _, dossier = run_v3_carbon_arrete(tmp_path, monkeypatch)
    c.fixer_composition(["fable", "carbon"], nom_cle_anthropic="MA_CLE")
    c.rejuger_essai(dossier, CID_T2_CARBON, 1)
    assert c.verifier(dossier) == []
    chemin = dossier / "journal.jsonl"
    sain = chemin.read_text(encoding="utf-8")
    # artefact 1 : l'essai rejugé ne tient plus les conditions au journal (marqueur effacé)
    lignes = []
    for l in sain.splitlines():
        e = json.loads(l)
        if e.get("cellule") == CID_T2_CARBON and "essai" in e:
            e["marqueur_fin"] = False
        lignes.append(json.dumps(e, ensure_ascii=False, sort_keys=True))
    chemin.write_text("\n".join(lignes) + "\n", encoding="utf-8")
    assert any("rejugement hors conditions" in p for p in c.verifier(dossier))
    # artefact 2 : deux rejugements de la même cellule
    chemin.write_text(sain + [l for l in sain.splitlines() if '"rejugement"' in l][0] + "\n", encoding="utf-8")
    assert any("rejugement(s)" in p for p in c.verifier(dossier))
    # artefact 3 : rejugement d'un essai absent
    chemin.write_text(sain.replace('"essai_rejuge": 1', '"essai_rejuge": 9'), encoding="utf-8")
    assert any("rejugement d'un essai absent" in p for p in c.verifier(dossier))


# ---------- correction 6 : --repli-lot après une coupure de flux chez Google ----------

def coupe_puis(c, tmp_path, espece="carbon"):
    """Premier essai en flux, coupé (code 5) ; renvoie le dossier."""
    c.TRANSPORT = FauxTransport(flux_gemini(modele=c.CATALOGUE[espece]["id"], coupure=True))
    with pytest.raises(c.Arret) as e:
        executer(c, tmp_path, espece)
    assert e.value.code == c.CODE_ECHEC and journal(c, tmp_path)[-1]["statut"] == "INTERROMPU"
    return tmp_path


def executer_lot(c, dossier, espece="carbon", repli=True):
    lettre = lettre_de(c, espece)
    return c.executer_cellule(dossier, "E1-T1", lettre, SAIN, [], 100.0, c.APPELANTS, repli_lot=repli)


def test_v7_lot_sain_apres_coupure(c, tmp_path):
    dossier = coupe_puis(c, tmp_path)
    rep = reponse_gemini_lot(pensees=40000, candidats=9000)
    t = FauxTransport(lot_cree(), ConnectionResetError("relevé coupé"), lot_en_cours(), lot_fini(rep))
    c.TRANSPORT = t
    assert executer_lot(c, dossier) == "OK"
    assert [(a["methode"], a["url"].rsplit("/", 1)[-1]) for a in t.appels] == [
        ("POST", "gemini-4-carbon:batchGenerateContent"), ("GET", "abc123"), ("GET", "abc123"), ("GET", "abc123")]
    demande = t.appels[0]["corps"]["batch"]["input_config"]["requests"]["requests"][0]["request"]
    assert demande["generationConfig"] == {"maxOutputTokens": 65536,
                                           "thinkingConfig": {"thinkingBudget": 32768, "includeThoughts": True}}
    assert demande["contents"][0]["parts"][0]["text"] == SAIN
    assert t.appels[1]["corps"] is None and t.appels[1]["entetes"]["x-goog-api-key"] == CLE_GEMINI
    assert c.dormis == [c.INTERVALLE_RELEVE_LOT_S] * 3
    d = journal(c, dossier)[-1]
    assert (d["essai"], d["mode_envoi"], d["nom_lot"], d["prix"]) == (2, "lot", "batches/abc123", [2.0, 10.0])
    assert d["cout_usd"] == round(500 * 2 / 1e6 + 49000 * 10 / 1e6, 4)
    assert d["cout_pire_usd"] == round(d["garde_entree"] * 2 / 1e6 + (65536 + 49152) * 10 / 1e6, 4)
    assert c.chemin_cellule(dossier, d["cellule"]).exists()
    assert CLE_GEMINI not in (dossier / "journal.jsonl").read_text(encoding="utf-8")


def test_v7_lot_reponse_non_imbriquee_lue(c, tmp_path):
    dossier = coupe_puis(c, tmp_path)
    c.TRANSPORT = FauxTransport(lot_cree(), lot_fini(imbrique=False))
    assert executer_lot(c, dossier) == "OK"


def test_v7_lot_temoins_sans_option_ou_sans_coupure_en_flux(c, tmp_path):
    dossier = coupe_puis(c, tmp_path / "sans-option")
    c.TRANSPORT = FauxTransport(flux_gemini())
    assert executer_lot(c, dossier, repli=False) == "OK"
    assert c.TRANSPORT.appels[0]["url"].endswith(":streamGenerateContent?alt=sse")
    assert journal(c, dossier)[-1]["mode_envoi"] == "flux"
    c.TRANSPORT = FauxTransport(flux_gemini())
    c.fixer_composition(["carbon", "kimi"])
    assert executer_lot(c, tmp_path / "sans-coupure") == "OK"  # aucune coupure : flux, même avec l'option
    assert c.TRANSPORT.appels[0]["url"].endswith(":streamGenerateContent?alt=sse")


def test_v7_lot_relance_apres_lot_tronque_reste_en_lot(c, tmp_path):
    dossier = coupe_puis(c, tmp_path)
    c.TRANSPORT = FauxTransport(lot_cree(), lot_fini(reponse_gemini_lot(fin="MAX_TOKENS", texte="Coupé")),
                                lot_cree("batches/b2"), lot_fini(nom="batches/b2"))
    assert executer_lot(c, dossier) == "OK"
    assert [e["mode_envoi"] for e in journal(c, dossier)] == ["flux", "lot", "lot"]


def test_v7_lot_artefact_non_abouti_au_delai_annule_compte_au_pire(c, tmp_path):
    dossier = coupe_puis(c, tmp_path)
    instants = iter([0.0, 10.0, 10.0 + c.CATALOGUE["carbon"]["delai_s"] + 1])
    c.HORLOGE = lambda: next(instants)
    t = FauxTransport(lot_cree(), lot_en_cours(), FauxFlux(corps={}))
    c.TRANSPORT = t
    with pytest.raises(c.Arret) as e:
        executer_lot(c, dossier)
    d = journal(c, dossier)[-1]
    assert e.value.code == c.CODE_ECHEC and d["statut"] == "INTERROMPU" and d["cout_usd"] == d["cout_pire_usd"] > 0
    assert d["nom_lot"] == "batches/abc123" and "annulation demandée" in d["echec"]
    assert [a["url"].rsplit("/", 1)[-1] for a in t.appels] == ["gemini-4-carbon:batchGenerateContent", "abc123",
                                                                "abc123:cancel"]


@pytest.mark.parametrize("fin", ["echoue", "erreur_requete", "sans_reponse", "nom_illisible", "creation_coupee",
                                 "releve_refuse"])
def test_v7_lot_artefacts_comptes_au_pire(c, tmp_path, fin):
    dossier = coupe_puis(c, tmp_path)
    actions = {"echoue": [lot_cree(), lot_fini(etat="BATCH_STATE_FAILED")],
               "erreur_requete": [lot_cree(), lot_fini(erreur={"code": 400, "message": "mauvais budget"})],
               "sans_reponse": [lot_cree(), FauxFlux(corps={"name": "batches/abc123", "done": True,
                                                            "metadata": {"state": "BATCH_STATE_SUCCEEDED"}})],
               "nom_illisible": [FauxFlux(corps={"name": "ailleurs/1"})],
               "creation_coupee": [ConnectionResetError("coupure")],
               "releve_refuse": [lot_cree(), http_erreur(404, "inconnu")]}[fin]
    c.TRANSPORT = FauxTransport(*actions)
    with pytest.raises(c.Arret) as e:
        executer_lot(c, dossier)
    d = journal(c, dossier)[-1]
    assert e.value.code == c.CODE_ECHEC and d["statut"] == "INTERROMPU" and d["cout_usd"] == d["cout_pire_usd"]
    assert d["mode_envoi"] == "lot" and not c.chemin_cellule(dossier, d["cellule"]).exists()


def test_v7_lot_creation_refusee_avant_traitement_cout_zero(c, tmp_path):
    dossier = coupe_puis(c, tmp_path)
    c.TRANSPORT = FauxTransport(http_erreur(400, "refus"))
    with pytest.raises(c.Arret) as e:
        executer_lot(c, dossier)
    d = journal(c, dossier)[-1]
    assert e.value.code == c.CODE_ECHEC and d["statut"] == "ECHEC" and d["cout_usd"] == 0


def test_v7_lot_modele_controle(c, tmp_path):
    dossier = coupe_puis(c, tmp_path)
    c.TRANSPORT = FauxTransport(lot_cree(), lot_fini(reponse_gemini_lot(modele="gemini-4-argon")))
    with pytest.raises(c.Arret) as e:
        executer_lot(c, dossier)
    assert e.value.code == c.CODE_MODELE and journal(c, dossier)[-1]["statut"] == "MODELE_DIFFERENT"


def test_v7_lot_option_en_ligne_de_commande(c, tmp_path, monkeypatch):
    """--repli-lot passe de la ligne de commande à la cellule coupée ; les autres restent en flux."""
    faits = tmp_path / "faits.md"
    faits.write_text("Fait 1 (HYPOTHÈSE) : texte sain.\n", encoding="utf-8")
    sortie = tmp_path / "run"
    argv = ["etage1", "--carbon", "--argon", "--faits", str(faits), "--sortie", str(sortie)]
    c.TRANSPORT = FauxTransport(flux_gemini(modele="gemini-4-argon"), flux_gemini(coupure=True))
    assert c.principal(argv) == c.CODE_ECHEC
    t = TransportParAdresse()
    c.TRANSPORT = t
    assert c.principal(argv + ["--repli-lot"]) == c.CODE_FINI
    modes = {(e["cellule"], e["essai"]): e["mode_envoi"] for e in c.essais_journal(sortie)}
    assert modes[("E1-T1-meta-B", 2)] == "lot" and modes[("E1-T2-critique-meta-B", 1)] == "flux"
    assert modes[("E1-T2-critique-meta-A", 1)] == "flux"
    assert c.verifier(sortie) == []


# ---------- correction 7 : refus de crédit dans le flux d'Anthropic ----------

def test_v7_refus_de_credit_echec_cout_zero(c, tmp_path):
    c.TRANSPORT = FauxTransport(flux_anthropic_credit())
    with pytest.raises(c.Arret) as e:
        executer(c, tmp_path, "fable")
    d = journal(c, tmp_path)[-1]
    assert e.value.code == c.CODE_ECHEC and d["statut"] == "ECHEC" and d["cout_usd"] == 0.0
    assert d["interrompue"] is False and len(c.TRANSPORT.appels) == 1 and "refus de crédit" in d["echec"]
    assert "entrée 58000" in d["echec"] and not c.chemin_cellule(tmp_path, d["cellule"]).exists()


@pytest.mark.parametrize("cas", ["texte reçu", "usage final reçu", "autre erreur", "autre message"])
def test_v7_refus_de_credit_artefacts_comptes_au_pire(c, tmp_path, cas):
    flux = {"texte reçu": flux_anthropic_credit(apres_texte=True),
            "usage final reçu": flux_anthropic_credit(apres_usage=True),
            "autre erreur": flux_anthropic_credit(type_erreur="overloaded_error"),
            "autre message": flux_anthropic_credit(message="Something else went wrong")}[cas]
    c.TRANSPORT = FauxTransport(flux)
    with pytest.raises(c.Arret) as e:
        executer(c, tmp_path, "fable")
    d = journal(c, tmp_path)[-1]
    assert e.value.code == c.CODE_ECHEC and d["statut"] == "INTERROMPU" and d["cout_usd"] == d["cout_pire_usd"] > 0


def test_v7_refus_de_credit_type_facturation_reconnu(c):
    assert c.refus_de_credit({"type": "billing_error", "message": "Credit balance is too low"})
    assert not c.refus_de_credit({"type": "api_error", "message": "credit balance"})
    assert not c.refus_de_credit("credit balance") and not c.refus_de_credit(None)


# ---------- correction 8 : --accepter-absence n'accepte qu'une cellule ----------

@pytest.mark.parametrize("valeur", ["kimi", "E3-T3-reponse-Z", "E9-T1-x-A", "", "E3-T3-reponse"])
def test_v7_accepter_absence_hors_cellule_refusee_rien_n_est_ecrit(c, tmp_path, capsys, valeur):
    faits = tmp_path / "faits.md"
    faits.write_text("Fait 1 (HYPOTHÈSE) : texte sain.\n", encoding="utf-8")
    sortie = tmp_path / "run"
    c.TRANSPORT = FauxTransport()
    code = c.principal(["etage1", "--carbon", "--argon", "--faits", str(faits), "--sortie", str(sortie),
                        "--accepter-absence", valeur])
    assert code == c.CODE_USAGE and c.TRANSPORT.appels == [] and not sortie.exists()
    assert "n'accepte qu'une cellule" in capsys.readouterr().err


def test_v7_accepter_absence_hors_cellule_refusee_sur_un_run_existant(c, tmp_path, monkeypatch):
    _, dossier = run_v3_carbon_arrete(tmp_path, monkeypatch)
    avant = (dossier / "journal.jsonl").read_bytes()
    c.TRANSPORT = FauxTransport()
    assert c.principal(ARGV_REPRISE + ["--sortie", str(dossier), "--accepter-absence", "kimi"]) == c.CODE_USAGE
    assert (dossier / "journal.jsonl").read_bytes() == avant


def test_v7_accepter_absence_cellule_acceptee(c, tmp_path):
    faits = tmp_path / "faits.md"
    faits.write_text("Fait 1 (HYPOTHÈSE) : texte sain.\n", encoding="utf-8")
    sortie = tmp_path / "run"
    c.TRANSPORT = FauxTransport(flux_gemini(modele="gemini-4-argon"), flux_gemini(modele="gemini-4-argon"))
    code = c.principal(["etage1", "--carbon", "--argon", "--faits", str(faits), "--sortie", str(sortie),
                        "--accepter-absence", "E1-T1-meta-B", "--accepter-absence", "E1-T2-critique-meta-B"])
    assert code == c.CODE_FINI
    assert [e["cellule"] for e in c.lire_journal(sortie) if e.get("decision") == "absence_acceptee"] == [
        "E1-T1-meta-B", "E1-T2-critique-meta-B"]


# ---------- correction 9 : copies des quatre dossiers à reprendre ----------
# Les copies sont fabriquées depuis les seuls journaux et compositions des runs (branche des versements, lue par git ;
# jamais une réponse de modèle) : chaque essai du journal est rejoué en fichiers neufs, prompts construits par le script,
# réponses factices de la longueur journalisée (marqueur compris s'il y était), cellules écrites pour les essais OK ;
# empreintes et pièces du journal recalculées, tout le reste gardé (statuts, usages, coûts, plafonds, ligne, scripts).
# Absente : essais sautés.

REF_RUNS = os.environ.get("REF_RUNS_COLLISIONNEURS", "origin/runs/collisionneurs-reprise-minuit-v1")
DEPOT = Path(os.environ.get("DEPOT_COLLISIONNEURS", CHEMIN.resolve().parents[3]))  # dépôt qui porte la branche
CINQ = ["--fable", "--opus", "--argon", "--astra", "--carbon"]
DOSSIERS_A_REPRENDRE = {
    # nom : (dossier, ligne L, plafond P, option, cellules envoyées attendues)
    "percee": ("collisionneur-percee-controle-securite-v1-20261121-114810", 28, 27.5,
               ["--rejuger-essai", "E3-T2-critique-croisee-E:1"], 5),
    "derive-v2": ("collisionneur-derive-de-regime-v2-20261121-131044", 24, 23.2,
                  ["--rejuger-essai", "E3-T2-critique-croisee-E:1"], 5),
    "anteriorite": ("collisionneur-anteriorite-pilier-v1-20261121-131029", 28, 26.4, ["--repli-lot"], 1),
    "maths": ("collisionneur-methodes-maths-v1-20261121-093850", 28, 28, [], 10),
}


def git_show(chemin):
    r = subprocess.run(["git", "-C", str(DEPOT), "show", f"{REF_RUNS}:{chemin}"], capture_output=True)
    return r.stdout if r.returncode == 0 else None


def git_taille(chemin):
    r = subprocess.run(["git", "-C", str(DEPOT), "cat-file", "-s", f"{REF_RUNS}:{chemin}"], capture_output=True,
                       text=True)
    return int(r.stdout) if r.returncode == 0 else None


def mots(n):
    """Texte factice de n caractères, en mots (un texte d'une seule lettre répétée rend la garde de motifs quadratique)."""
    return ("mot " * (n // 4 + 1))[:max(n, 0)]


def fabriquer_copie(c, nom_run, cible):
    base = f"runs/{nom_run}"
    journal_reel, especes, sceau = git_show(f"{base}/journal.jsonl"), git_show(f"{base}/especes.json"), \
        git_show(f"{base}/especes.json.sha256")
    tailles = {f: git_taille(f"{base}/{f}") for f in ("faits.md", "question-etage3.md")}
    if None in (journal_reel, especes, sceau) or None in tailles.values():
        pytest.skip(f"journal du run absent ({REF_RUNS})")
    cible.mkdir(parents=True)
    (cible / "especes.json").write_bytes(especes)
    (cible / "especes.json.sha256").write_bytes(sceau)
    c.lire_composition(cible)
    for f, n in tailles.items():  # contenu factice, longueur du fichier versé
        c.ecrire_neuf(cible / f, mots(n))
    lignes = []
    for l in journal_reel.decode("utf-8").splitlines():
        e = json.loads(l)
        if "essai" in e:
            cid, n = e["cellule"], e["essai"]
            for k in range(1, n):  # essai parti sans ligne de journal (prompt seul), comme au run « percée »
                p = cible / "essais" / f"{cid}.essai{k}.prompt.txt"
                if not p.exists():
                    c.ecrire_neuf(p, "prompt factice")
            prompt, pieces = c.construire_prompt(cible, cid[:5], cid[-1], [], set())
            longueur = e["caracteres"]
            texte = (mots(longueur - len(c.MARQUEUR)) + c.MARQUEUR) if e["marqueur_fin"] else mots(longueur)
            e["sha256_prompt"] = c.ecrire_neuf(cible / "essais" / f"{cid}.essai{n}.prompt.txt", prompt)
            e["sha256_texte"] = c.ecrire_neuf(cible / "essais" / f"{cid}.essai{n}.reponse.md", texte)
            e["pieces"] = pieces
            if e["statut"] == "OK":
                c.ecrire_neuf(c.chemin_cellule(cible, cid), texte)
        lignes.append(json.dumps(e, ensure_ascii=False, sort_keys=True))
        (cible / "journal.jsonl").write_text("\n".join(lignes) + "\n", encoding="utf-8")
    return cible


@pytest.mark.parametrize("nom", sorted(DOSSIERS_A_REPRENDRE))
def test_v7_copie_des_dossiers_a_reprendre(c, tmp_path, monkeypatch, capsys, nom):
    dossier_run, ligne, plafond, option, attendues = DOSSIERS_A_REPRENDRE[nom]
    d = fabriquer_copie(c, dossier_run, tmp_path / dossier_run)
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)  # la clé par défaut n'existe pas : seule la clé nommée sert
    monkeypatch.setenv("OPENAI_API_KEY_2", CLE_OPENAI)
    # 1. vérification avant reprise, par la v9-v7
    assert c.verifier(d) == []
    # 2. devis de reprise : sans réseau, sans écriture, sous le reste de la ligne
    journal_avant = (d / "journal.jsonl").read_bytes()
    c.TRANSPORT = FauxTransport()
    res = c.devis_reprise(d, ligne)
    assert (d / "journal.jsonl").read_bytes() == journal_avant and c.TRANSPORT.appels == []
    assert res["restant"] == pytest.approx(ligne - c.depense(d))
    detail = res["detail"]
    sortie_devis = capsys.readouterr().out
    print(f"{nom} : reste {res['restant']:.2f} ; pire sans relance {detail['tour2'] + detail['tour3']:.2f} ; "
          f"avec relances {detail['avec_relances']:.2f}")
    assert "Devis de reprise" in sortie_devis
    # 3. reprise par la commande de la réflexion d'Opus (section 7), faux fournisseurs ; envois comptés
    t = TransportParAdresse()
    c.TRANSPORT = t
    c.TRANSPORT_COMPTE = FauxCompteur()
    argv = ["etage3"] + CINQ + ["--cle-anthropic", "MA_CLE", "--cle-openai", "OPENAI_API_KEY_2", "--sortie", str(d),
                                "--plafond-usd", str(plafond), "--ligne-usd", str(ligne), "--reprise"] + option
    essais_avant = {x.name: x.read_bytes() for x in (d / "essais").iterdir()}
    cellules_avant = {x.name: x.read_bytes() for x in (d / "cellules").iterdir()}
    assert c.principal(argv) == c.CODE_FINI
    cellules_envoyees = {a["url"].rsplit("/", 1)[-1] for a in t.generations()}
    assert len(t.generations()) == attendues  # une création par cellule envoyée (Astra : relevés en plus, non comptés)
    assert len(c.TRANSPORT_COMPTE.appels) == attendues  # un comptage par cellule envoyée, aucun pour une cellule rejugée
    for a in t.appels:  # clé d'OpenAI lue par son nom (OPENAI_API_KEY_2), la clé par défaut étant absente
        if "/responses" in a["url"]:
            assert a["entetes"]["authorization"] == f"Bearer {CLE_OPENAI}"
    for nom_f, octets in essais_avant.items():  # rien d'avant n'est touché
        assert (d / "essais" / nom_f).read_bytes() == octets
    for nom_f, octets in cellules_avant.items():
        assert (d / "cellules" / nom_f).read_bytes() == octets
    assert (d / "journal.jsonl").read_bytes().startswith(journal_avant)
    # 4. vérification après reprise ; les quinze cellules ; un seul changement de script déclaré
    assert c.verifier(d) == []
    assert len(list((d / "cellules").glob("*.md"))) == 15
    assert len([x for x in c.lire_journal(d) if "changement_script" in x]) == 1
    if nom == "anteriorite":
        e = c.essais_journal(d, "E3-T3-reponse-E")[-1]
        assert (e["essai"], e["mode_envoi"], e["prix"]) == (3, "lot", [2.0, 10.0]) and cellules_envoyees == {
            "gemini-4-carbon:batchGenerateContent"}
    if nom in ("percee", "derive-v2"):
        assert len(c.rejugements(d)) == 1 and not list((d / "essais").glob("E3-T2-critique-croisee-E.essai2.*"))
    # 5. la même commande relancée : aucun envoi
    c.TRANSPORT = FauxTransport()
    assert c.principal(argv) == c.CODE_FINI and c.TRANSPORT.appels == []
