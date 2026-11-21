"""Essais R5 hors réseau de appel_modeles_externes_v5.py : transport simulé, aucune requête, aucune clé réelle.

Partie reprise : les dix essais du v4 (essais_appel_modeles_externes_v4.py, f3181604…), rejoués tels quels sur le v5 ; seul
le module chargé change (le nom « v4 » des essais repris désigne le module v5).
Partie neuve (v5) : Neon sain ; garde de dépense de Neon ; arrêt « MAX_TOKENS » de Neon, sans texte (défaut de réglage) et
avec texte partiel ; plancher de texte de Neon ; clé d'OpenAI choisie par son nom (--cle-openai), absente, mal formée ;
option --cle-openai câblée dans la ligne de commande (réseau bloqué).
Lancer : python -I essais_appel_modeles_externes_v5.py   (ou pytest sur ce fichier)
"""
import importlib.util
import json
import os
import tempfile
from pathlib import Path

ICI = Path(__file__).resolve().parent
_spec = importlib.util.spec_from_file_location("appel_v5", ICI / "appel_modeles_externes_v5.py")
v5 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(v5)
v4 = v5  # les essais du v4 sont rejoués tels quels sur le v5

CLE_FACTICE = "sk-factice-0123456789abcdef"
ENV = {"OPENAI_API_KEY": CLE_FACTICE, "GEMINI_API_KEY": CLE_FACTICE}


def _dossier():
    d = Path(tempfile.mkdtemp(prefix="essai-v5-"))
    (d / "enonce.md").write_text("Énoncé court d'essai.", encoding="utf-8")
    return d


def _astra(final, appels):
    """Transport simulé : création -> queued, puis un relevé qui rend `final`."""
    def transport(url, corps, entetes, methode="POST"):
        appels.append((methode, url, corps))
        assert entetes["Authorization"] == f"Bearer {CLE_FACTICE}"
        if methode == "POST":
            return 200, {"id": "resp_essai_1", "status": "queued", "model": "gpt-6.2-astra"}, "{}"
        return 200, final, json.dumps(final)
    return transport


def _lancer(espece, d, **k):
    return v4.executer(espece, str(d / "enonce.md"), str(d / "rep.md"), str(d / "rep.json"), environ=ENV,
                       dormir=lambda s: None, **k)


def test_astra_sain():
    d, appels = _dossier(), []
    final = {"id": "resp_essai_1", "status": "completed", "model": "gpt-6.2-astra", "error": None,
             "output": [{"type": "reasoning"}, {"type": "message", "content": [{"type": "output_text", "text": "Avis."}]}],
             "usage": {"input_tokens": 10, "output_tokens": 300, "output_tokens_details": {"reasoning_tokens": 250}}}
    assert _lancer("astra", d, transport_json=_astra(final, appels)) == 0
    meta = json.loads((d / "rep.json").read_text())
    assert meta["verdict"] == "ok" and meta["id_reponse"] == "resp_essai_1" and meta["jetons_reflexion"] == 250
    assert (d / "rep.md").read_text() == "Avis."
    assert appels[0][2]["max_output_tokens"] == 48000 and appels[0][2]["reasoning"]["effort"] == "xhigh"


def test_astra_failed_garde_le_motif():
    d, appels = _dossier(), []
    erreur = {"code": "server_error", "message": "The model failed to generate a response. Request id req_abc."}
    final = {"id": "resp_essai_1", "status": "failed", "model": "gpt-6.2-astra", "error": erreur, "output": [],
             "usage": None}
    assert _lancer("astra", d, transport_json=_astra(final, appels)) == 1
    meta = json.loads((d / "rep.json").read_text())
    assert meta["verdict"] == "echec" and meta["fin"] == "failed"
    assert meta["id_reponse"] == "resp_essai_1"
    assert meta["erreur_fournisseur"] == erreur  # message complet, non tronqué
    assert "server_error" in meta["motif"]
    assert not (d / "rep.md").exists()


def test_astra_incomplete_signale():
    d, appels = _dossier(), []
    final = {"id": "resp_essai_1", "status": "incomplete", "incomplete_details": {"reason": "max_output_tokens"},
             "output": [{"type": "message", "content": [{"type": "output_text", "text": "Début"}]}],
             "usage": {"input_tokens": 10, "output_tokens": 48000}}
    assert _lancer("astra", d, transport_json=_astra(final, appels)) == 3
    meta = json.loads((d / "rep.json").read_text())
    assert meta["verdict"] == "tronque" and "max_output_tokens" in meta["motif"]
    assert not (d / "rep.md").exists() and (d / "rep.md.partiel.md").read_text() == "Début"


def test_astra_releves_rates_non_silencieux():
    d = _dossier()

    def transport(url, corps, entetes, methode="POST"):
        if methode == "POST":
            return 200, {"id": "resp_x", "status": "queued"}, "{}"
        return 502, None, "<html>Bad gateway</html>"
    assert _lancer("astra", d, transport_json=transport) == 1
    meta = json.loads((d / "rep.json").read_text())
    assert meta["fin"] == "releves_rates" and meta["id_reponse"] == "resp_x"
    assert sum(e["etape"] == "releve_rate" for e in meta["essais"]) == v4.RELEVES_RATES_MAX


def _flux(morceaux, appels):
    def transport(url, corps, entetes):
        appels.append((url, corps))
        assert entetes["x-goog-api-key"] == CLE_FACTICE
        return 200, iter("data: " + json.dumps(m) + "\n" for m in morceaux), None
    return transport


def test_carbon_sain():
    d, appels = _dossier(), []
    morceaux = [{"responseId": "gem_1", "modelVersion": "gemini-4-carbon",
                 "candidates": [{"content": {"parts": [{"text": "pensée", "thought": True}]}}]},
                {"candidates": [{"content": {"parts": [{"text": "Réponse."}]}, "finishReason": "STOP"}],
                 "usageMetadata": {"promptTokenCount": 20, "candidatesTokenCount": 5, "thoughtsTokenCount": 900}}]
    assert _lancer("carbon", d, transport_flux=_flux(morceaux, appels)) == 0
    cfg = appels[0][1]["generationConfig"]
    assert cfg["thinkingConfig"]["thinkingBudget"] == 24000 and cfg["maxOutputTokens"] == 40000
    assert cfg["maxOutputTokens"] - cfg["thinkingConfig"]["thinkingBudget"] >= 16000
    meta = json.loads((d / "rep.json").read_text())
    assert meta["verdict"] == "ok" and meta["id_reponse"] == "gem_1" and meta["jetons_sortie_et_reflexion"] == 905
    assert (d / "rep.md").read_text() == "Réponse."


def test_carbon_max_tokens_signale():
    d, appels = _dossier(), []
    morceaux = [{"responseId": "gem_2", "candidates": [{"content": {"parts": [{"text": "…", "thought": True}]}}]},
                {"candidates": [{"content": {"parts": []}, "finishReason": "MAX_TOKENS"}],
                 "usageMetadata": {"promptTokenCount": 11336, "thoughtsTokenCount": 32000}}]
    assert _lancer("carbon", d, transport_flux=_flux(morceaux, appels)) == 3
    meta = json.loads((d / "rep.json").read_text())
    assert meta["verdict"] == "tronque" and meta["fin"] == "MAX_TOKENS" and "MAX_TOKENS" in meta["motif"]
    assert "texte absent" in meta["motif"] and not (d / "rep.md").exists()


def test_carbon_429_corps_complet_et_cle_masquee():
    d = _dossier()
    corps = json.dumps({"error": {"code": 429, "status": "RESOURCE_EXHAUSTED",
                                  "message": f"Quota exceeded for key {CLE_FACTICE}. " + "x" * 3000}})

    def transport(url, c, entetes):
        return 429, None, corps
    assert _lancer("carbon", d, transport_flux=transport) == 1
    brut = (d / "rep.json").read_text()
    assert CLE_FACTICE not in brut and "[clé masquée]" in brut
    meta = json.loads(brut)
    assert meta["erreur_fournisseur"]["status"] == "RESOURCE_EXHAUSTED"
    assert len(meta["erreur_fournisseur"]["message"]) > 3000  # rien de tronqué


def test_garde_de_depense():
    d = _dossier()
    appele = []
    code = _lancer("astra", d, plafond_usd=0.05, transport_json=lambda *a, **k: appele.append(1))
    assert code == 1 and not appele and not (d / "rep.json").exists()
    assert _lancer("astra", d, plafond_usd=5.0, transport_json=lambda *a, **k: appele.append(1)) == 1 and not appele


def test_plancher_de_texte_carbon():
    d = _dossier()
    assert _lancer("carbon", d, texte=8000, transport_flux=lambda *a: (_ for _ in ()).throw(AssertionError)) == 1


def test_refus_d_ecraser():
    d = _dossier()
    (d / "rep.json").write_text("ancien")
    assert _lancer("astra", d, transport_json=lambda *a, **k: (_ for _ in ()).throw(AssertionError)) == 1
    assert (d / "rep.json").read_text() == "ancien"



# ======================================================================================================================
# v5 : Neon, règle du plafond large, --cle-openai. Chaque garde : un cas sain et un artefact (R5). Sans fixture de pytest,
# pour que le lanceur en bas de fichier les joue aussi.
# ======================================================================================================================
CLE_OPENAI_2 = "sk-factice-deux-fedcba9876543210"


def _neon(morceaux_fin, appels):
    morceaux = [{"responseId": "gem_n", "modelVersion": "gemini-4-neon",
                 "candidates": [{"content": {"parts": [{"text": "pensée", "thought": True}]}}]}] + morceaux_fin
    return _flux(morceaux, appels)


def test_v5_neon_au_catalogue():
    assert v5.MODELE["neon"] == "gemini-4-neon" and v5.CLE["neon"] == "GEMINI_API_KEY"
    assert v5.PRIX["neon"] == (3.0, 15.0) and v5.DEFAUTS["neon"] == (32768, 32768)
    assert {k: v5.PRIX[k] for k in ("carbon", "astra", "argon")} == {"carbon": (4.0, 20.0), "astra": (10.0, 50.0),
                                                                     "argon": (10.0, 50.0)}  # rien d'autre ne change
    assert v5.REGLE_PLAFOND_LARGE == ("carbon", "neon") and "neon" in v5.ESPECES_GEMINI


def test_v5_neon_sain():
    d, appels = _dossier(), []
    fin = [{"candidates": [{"content": {"parts": [{"text": "Réponse de Neon."}]}, "finishReason": "STOP"}],
            "usageMetadata": {"promptTokenCount": 20, "candidatesTokenCount": 5, "thoughtsTokenCount": 900}}]
    assert _lancer("neon", d, transport_flux=_neon(fin, appels)) == 0
    url, corps = appels[0]
    assert "/models/gemini-4-neon:streamGenerateContent" in url
    cfg = corps["generationConfig"]
    assert cfg == {"maxOutputTokens": 65536, "thinkingConfig": {"thinkingBudget": 32768, "includeThoughts": True}}
    assert cfg["maxOutputTokens"] - cfg["thinkingConfig"]["thinkingBudget"] >= 16000
    meta = json.loads((d / "rep.json").read_text())
    assert meta["verdict"] == "ok" and meta["modele_demande"] == "gemini-4-neon" and meta["id_reponse"] == "gem_n"
    assert meta["variable_cle"] == "GEMINI_API_KEY" and meta["version_script"] == "v5"
    assert meta["cout_usd_prix_haut"] == round(20 * 3 / 1e6 + 905 * 15 / 1e6, 4)
    assert (d / "rep.md").read_text() == "Réponse de Neon."


def test_v5_neon_garde_de_depense():
    d = _dossier()
    pire = v5.pire_cas_usd("neon", (d / "enonce.md").read_text(encoding="utf-8"), 65536)
    assert pire == (len("Énoncé court d'essai.") / 2) * 3 / 1e6 + 65536 * 1.5 * 15 / 1e6
    appele = []
    jamais = lambda *a, **k: appele.append(1)  # noqa: E731
    assert _lancer("neon", d, plafond_usd=pire - 1e-6, transport_flux=jamais) == 1  # artefact : sous le pire cas
    assert not appele and not (d / "rep.json").exists()
    assert _lancer("neon", d, texte=200000, transport_flux=jamais) == 1  # artefact : pire cas au-delà de 4 USD
    assert not appele and not (d / "rep.json").exists()
    fin = [{"candidates": [{"content": {"parts": [{"text": "Ok."}]}, "finishReason": "STOP"}],
            "usageMetadata": {"promptTokenCount": 20, "candidatesTokenCount": 2, "thoughtsTokenCount": 10}}]
    appels = []
    assert _lancer("neon", d, plafond_usd=pire + 1e-6, transport_flux=_neon(fin, appels)) == 0  # sain : juste au-dessus
    assert len(appels) == 1 and json.loads((d / "rep.json").read_text())["pire_cas_usd"] == round(pire, 4)


def test_v5_neon_max_tokens_sans_texte_defaut_de_reglage():
    d, appels = _dossier(), []
    fin = [{"candidates": [{"content": {"parts": []}, "finishReason": "MAX_TOKENS"}],
            "usageMetadata": {"promptTokenCount": 11336, "thoughtsTokenCount": 65536}}]
    assert _lancer("neon", d, transport_flux=_neon(fin, appels)) == 3
    assert len(appels) == 1  # aucun renvoi
    meta = json.loads((d / "rep.json").read_text())
    assert meta["verdict"] == "tronque" and meta["fin"] == "MAX_TOKENS" and "texte absent" in meta["motif"]
    assert "défaut de réglage, pas une réponse" in meta["motif"]
    assert not (d / "rep.md").exists() and not (d / "rep.md.partiel.md").exists()


def test_v5_neon_max_tokens_texte_partiel_a_part():
    d, appels = _dossier(), []
    fin = [{"candidates": [{"content": {"parts": [{"text": "Début"}]}, "finishReason": "MAX_TOKENS"}],
            "usageMetadata": {"promptTokenCount": 20, "candidatesTokenCount": 32768, "thoughtsTokenCount": 32768}}]
    assert _lancer("neon", d, transport_flux=_neon(fin, appels)) == 3
    meta = json.loads((d / "rep.json").read_text())
    assert meta["verdict"] == "tronque" and "texte partiel" in meta["motif"] and "défaut de réglage" not in meta["motif"]
    assert not (d / "rep.md").exists() and (d / "rep.md.partiel.md").read_text() == "Début"


def test_v5_carbon_max_tokens_sans_texte_dit_defaut_de_reglage_argon_non():
    for espece, attendu in (("carbon", True), ("argon", False)):
        code, motif = v5.verdict(espece, {"statut": "MAX_TOKENS", "texte": None, "jetons_reflexion": 40000,
                                          "erreur_fournisseur": None, "details_incomplet": None})
        assert code == v5.CODE_TRONQUE and ("défaut de réglage" in motif) is attendu


def test_v5_neon_plancher_de_texte():
    interdit = lambda *a: (_ for _ in ()).throw(AssertionError)  # noqa: E731
    assert _lancer("neon", _dossier(), texte=15999, transport_flux=interdit) == 1  # artefact
    d, appels = _dossier(), []
    fin = [{"candidates": [{"content": {"parts": [{"text": "Ok."}]}, "finishReason": "STOP"}],
            "usageMetadata": {"promptTokenCount": 20, "candidatesTokenCount": 2, "thoughtsTokenCount": 10}}]
    assert _lancer("neon", d, texte=16000, transport_flux=_neon(fin, appels)) == 0  # sain : au plancher
    assert appels[0][1]["generationConfig"]["maxOutputTokens"] == 32768 + 16000


def _astra_cle(final, appels, cle):
    def transport(url, corps, entetes, methode="POST"):
        appels.append((methode, url, corps))
        assert entetes["Authorization"] == f"Bearer {cle}"
        if methode == "POST":
            return 200, {"id": "resp_essai_2", "status": "queued", "model": "gpt-6.2-astra"}, "{}"
        return 200, final, json.dumps(final)
    return transport


def test_v5_cle_openai_choisie_par_son_nom():
    d, appels = _dossier(), []
    env = {"OPENAI_API_KEY_2": CLE_OPENAI_2, "GEMINI_API_KEY": CLE_FACTICE}  # pas de OPENAI_API_KEY
    final = {"id": "resp_essai_2", "status": "completed", "model": "gpt-6.2-astra", "error": None,
             "output": [{"type": "message", "content": [{"type": "output_text", "text": "Avis 2."}]}],
             "usage": {"input_tokens": 10, "output_tokens": 30, "output_tokens_details": {"reasoning_tokens": 20}}}
    code = v5.executer("astra", str(d / "enonce.md"), str(d / "rep.md"), str(d / "rep.json"), environ=env,
                       dormir=lambda s: None, transport_json=_astra_cle(final, appels, CLE_OPENAI_2),
                       nom_cle_openai="OPENAI_API_KEY_2")
    assert code == 0 and len(appels) == 2
    brut = (d / "rep.json").read_text()
    assert json.loads(brut)["variable_cle"] == "OPENAI_API_KEY_2" and CLE_OPENAI_2 not in brut
    assert CLE_OPENAI_2 not in (d / "rep.md").read_text()


def test_v5_cle_openai_nommee_absente_sans_repli_sur_la_cle_par_defaut():
    d = _dossier()
    interdit = lambda *a, **k: (_ for _ in ()).throw(AssertionError("aucun envoi"))  # noqa: E731
    code = v5.executer("astra", str(d / "enonce.md"), str(d / "rep.md"), str(d / "rep.json"), environ=ENV,
                       dormir=lambda s: None, transport_json=interdit, nom_cle_openai="OPENAI_API_KEY_2")
    assert code == 1 and not (d / "rep.json").exists()  # ENV porte OPENAI_API_KEY : elle n'est pas lue à la place


def test_v5_cle_openai_nom_mal_forme_refuse_sans_echo():
    import contextlib
    import io
    d = _dossier()
    valeur = "sk-proj-ceci-ressemble-a-une-cle-0123"
    interdit = lambda *a, **k: (_ for _ in ()).throw(AssertionError("aucun envoi"))  # noqa: E731
    err = io.StringIO()
    with contextlib.redirect_stderr(err):
        code = v5.executer("astra", str(d / "enonce.md"), str(d / "rep.md"), str(d / "rep.json"), environ=ENV,
                           dormir=lambda s: None, transport_json=interdit, nom_cle_openai=valeur)
    assert code == 1 and valeur not in err.getvalue() and "mal formé" in err.getvalue()
    assert not (d / "rep.json").exists()


def test_v5_option_cle_openai_cablee_reseau_bloque():
    """La ligne de commande passe --cle-openai à l'exécution : une variable nommée absente arrête avant tout envoi, alors
    qu'OPENAI_API_KEY est présente (posée ici, factice). Le réseau est bloqué pendant l'essai (aucune requête possible)."""
    import contextlib
    import io
    import socket
    import urllib.request
    d = _dossier()
    interdit = lambda *a, **k: (_ for _ in ()).throw(AssertionError("réseau interdit dans les essais"))  # noqa: E731
    sauve = urllib.request.urlopen, socket.create_connection, os.environ.get("OPENAI_API_KEY")
    urllib.request.urlopen, socket.create_connection = interdit, interdit
    os.environ["OPENAI_API_KEY"] = CLE_FACTICE
    err = io.StringIO()
    try:
        with contextlib.redirect_stderr(err):
            code = v5.main(["astra", str(d / "enonce.md"), str(d / "rep.md"), str(d / "rep.json"),
                            "--cle-openai", "VARIABLE_ABSENTE_ESSAI_V5"])
    finally:
        urllib.request.urlopen, socket.create_connection = sauve[0], sauve[1]
        if sauve[2] is None:
            os.environ.pop("OPENAI_API_KEY", None)
        else:
            os.environ["OPENAI_API_KEY"] = sauve[2]
    assert code == 1 and not (d / "rep.json").exists()
    assert "VARIABLE_ABSENTE_ESSAI_V5 absente" in err.getvalue() and CLE_FACTICE not in err.getvalue()


if __name__ == "__main__":
    n = 0
    for nom, f in sorted(globals().items()):
        if nom.startswith("test_") and callable(f):
            f()
            n += 1
            print("ok", nom)
    print(f"{n} essais passés")
