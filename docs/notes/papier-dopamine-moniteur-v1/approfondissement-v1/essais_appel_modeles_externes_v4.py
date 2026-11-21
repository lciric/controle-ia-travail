"""Essais R5 hors réseau de appel_modeles_externes_v4.py : transport simulé, aucune requête, aucune clé réelle.

Cas : Astra sain ; Astra « failed » qui doit garder l'identifiant et le motif complet ; Astra « incomplete » ; Carbon sain ;
Carbon « MAX_TOKENS » signalé (code 3, texte partiel à part) ; Carbon refus HTTP 429 au corps complet gardé ; garde de
dépense ; plancher de texte de Carbon ; clé masquée si le fournisseur la renvoie ; refus d'écraser.
Lancer : python -I essais_appel_modeles_externes_v4.py   (ou pytest sur ce fichier)
"""
import importlib.util
import json
import os
import tempfile
from pathlib import Path

ICI = Path(__file__).resolve().parent
_spec = importlib.util.spec_from_file_location("appel_v4", ICI / "appel_modeles_externes_v4.py")
v4 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(v4)

CLE_FACTICE = "sk-factice-0123456789abcdef"
ENV = {"OPENAI_API_KEY": CLE_FACTICE, "GEMINI_API_KEY": CLE_FACTICE}


def _dossier():
    d = Path(tempfile.mkdtemp(prefix="essai-v4-"))
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


if __name__ == "__main__":
    n = 0
    for nom, f in sorted(globals().items()):
        if nom.startswith("test_") and callable(f):
            f()
            n += 1
            print("ok", nom)
    print(f"{n} essais passés")
