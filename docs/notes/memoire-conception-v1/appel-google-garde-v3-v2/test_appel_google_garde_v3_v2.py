"""Essais sans réseau de appel_google_garde_v3_v2.py (cas sain et artefacts, R5). Lancer :
. .venv/bin/activate && PYTHONPATH=src python -m pytest -q docs/notes/memoire-conception-v1/appel-google-garde-v3-v2/"""
import datetime as dt
import importlib.util
import io
import json
import os
import urllib.error

import pytest

ICI = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("appel_v2", os.path.join(ICI, "appel_google_garde_v3_v2.py"))
appel = importlib.util.module_from_spec(spec)
spec.loader.exec_module(appel)

JOUR = dt.datetime(2026, 11, 22, 13, 0, tzinfo=dt.timezone.utc)
SAIN = "Contre-lis ces fiches du mémo contre leurs sources. Réponds en 2000 mots au plus.\nFiche : le plancher d'audit."


def flux(*objets, brut=()):
    lignes = [f"data: {json.dumps(o)}\n".encode() for o in objets] + [b for b in brut]
    return lignes


def bonne(servi="gemini-4-argon", fin="STOP", pensees=120, texte="Verdict : juste."):
    return {"candidates": [{"content": {"parts": [{"text": "réflexion", "thought": True}, {"text": texte}]},
                            "finishReason": fin}],
            "usageMetadata": {"promptTokenCount": 100, "candidatesTokenCount": 50, "thoughtsTokenCount": pensees},
            "modelVersion": servi, "responseId": "r1"}


class Reponse:
    def __init__(self, lignes, status=200):
        self.lignes, self.status = lignes, status

    def __enter__(self):
        return self

    def __exit__(self, *a):
        return False

    def __iter__(self):
        return iter(self.lignes)


def ouvreur(lignes=None, exc=None, status=200):
    def _o(req, timeout=None):
        assert req.get_header("X-goog-api-key") == "cle-factice"
        if exc:
            raise exc
        return Reponse(lignes, status)
    return _o


@pytest.fixture
def lieu(tmp_path, monkeypatch):
    monkeypatch.setenv("GEMINI_API_KEY", "cle-factice")
    e = tmp_path / "enonce.md"
    e.write_text(SAIN, encoding="utf-8")
    return tmp_path, e


def lancer(lieu, enonce_txt=None, lignes=None, exc=None, extra=(), journal=None):
    d, e = lieu
    if enonce_txt is not None:
        e.write_text(enonce_txt, encoding="utf-8")
    j = journal or str(d / "journal.jsonl")
    argv = ["argon", str(e), str(d / "sortie.md"), str(d / "sortie.json"), "--journal", j, *extra]
    return appel.main(argv, ouvrir=ouvreur(lignes, exc), maintenant=JOUR), d


def meta(d):
    return json.loads((d / "sortie.json").read_text())


def test_cas_sain(lieu):
    rc, d = lancer(lieu, lignes=flux(bonne()))
    m = meta(d)
    assert rc == 0 and m["verdict"] == "reponse" and m["defaut"] is None
    assert (d / "sortie.md").read_text() == "Verdict : juste."
    assert (d / "sortie.md.sha256").exists() and (d / "sortie.json.sha256").exists()
    assert m["prix_usd_par_million"] == {"entree": 2.0, "sortie": 10.0}
    assert m["mots_enonce"] == 2000 and m["prix_source_sha256"] == appel.PAGE_PRIX_SHA256
    lignes = [json.loads(l) for l in (d / "journal.jsonl").read_text().splitlines()]
    assert [l["etat"] for l in lignes] == ["reserve", "solde"]
    assert abs(sum(l["cout_compte_usd"] for l in lignes) - m["cout_compte_usd"]) < 1e-6


def test_tarif_apres_bascule(lieu, monkeypatch):
    d, e = lieu
    argv = ["argon", str(e), str(d / "s.md"), str(d / "s.json"), "--journal", str(d / "j.jsonl")]
    assert appel.main(argv, ouvrir=ouvreur(flux(bonne())),
                      maintenant=dt.datetime(2026, 12, 1, 0, 0, tzinfo=dt.timezone.utc)) == 0
    assert json.loads((d / "s.json").read_text())["prix_usd_par_million"] == {"entree": 4.0, "sortie": 20.0}


def test_motif_refuse(lieu):
    rc, d = lancer(lieu, enonce_txt=SAIN + "\nécrire à quelqu'un@exemple.fr", lignes=flux(bonne()))
    assert rc == 1 and not (d / "journal.jsonl").exists() and not (d / "sortie.json").exists()


def test_identifiant_de_session_refuse(lieu):
    rc, _ = lancer(lieu, enonce_txt=SAIN + "\nsession_01XJ6Mgr4LgbMsg5zLyRZCpG", lignes=flux(bonne()))
    assert rc == 1


def test_sans_limite_de_mots(lieu):
    rc, _ = lancer(lieu, enonce_txt="Contre-lis ces fiches.", lignes=flux(bonne()))
    assert rc == 1


def test_mots_discordants(lieu):
    rc, _ = lancer(lieu, lignes=flux(bonne()), extra=["--mots", "0"])
    assert rc == 1


def test_limite_de_mots_trop_haute(lieu):
    rc, _ = lancer(lieu, enonce_txt="Réponds en 9000 mots.", lignes=flux(bonne()))
    assert rc == 1   # 9000 × 5,1 ≥ 16 384 jetons de texte


def test_plafond_course_au_dela_de_3(lieu):
    rc, _ = lancer(lieu, lignes=flux(bonne()), extra=["--plafond-usd", "3.5"])
    assert rc == 1


def test_plafond_cumule(lieu):
    d, _ = lieu
    j = d / "journal.jsonl"
    j.write_text(json.dumps({"etat": "solde", "cout_compte_usd": 2.5}) + "\n")
    rc, _ = lancer(lieu, lignes=flux(bonne()), journal=str(j))
    assert rc == 1   # 2,5 + pire cas (≈ 0,98) > 3


def test_journal_illisible(lieu):
    d, _ = lieu
    j = d / "journal.jsonl"
    j.write_text("pas du json\n")
    rc, _ = lancer(lieu, lignes=flux(bonne()), journal=str(j))
    assert rc == 1


def test_page_prix_alteree(lieu, monkeypatch):
    monkeypatch.setattr(appel, "PAGE_PRIX_SHA256", "0" * 64)
    rc, _ = lancer(lieu, lignes=flux(bonne()))
    assert rc == 1


def test_flux_illisible(lieu):
    rc, d = lancer(lieu, lignes=flux(bonne(), brut=[b"data: {pas du json\n"]))
    assert rc == 3 and meta(d)["defaut"] == "FLUX_ILLISIBLE"
    assert (d / "sortie.md.defaut.md").exists() and not (d / "sortie.md").exists()


def test_erreur_dans_le_flux(lieu):
    rc, d = lancer(lieu, lignes=flux(bonne(), {"error": {"code": 500, "message": "interne"}}))
    assert rc == 3 and meta(d)["defaut"] == "ERREUR_FLUX"


def test_modele_servi_different(lieu):
    rc, d = lancer(lieu, lignes=flux(bonne(servi="gemini-4-carbon")))
    assert rc == 3 and meta(d)["defaut"] == "MODELE_SERVI_DIFFERENT"


def test_modele_servi_absent(lieu):
    o = bonne()
    del o["modelVersion"]
    rc, d = lancer(lieu, lignes=flux(o))
    assert rc == 3 and meta(d)["defaut"] == "MODELE_SERVI_ABSENT"


def test_modele_servi_variante_admise(lieu):
    rc, d = lancer(lieu, lignes=flux(bonne(servi="gemini-4-argon-001")))
    assert rc == 0


def test_max_tokens(lieu):
    rc, d = lancer(lieu, lignes=flux(bonne(fin="MAX_TOKENS")))
    assert rc == 3 and meta(d)["defaut"] == "MAX_TOKENS"


def test_sans_pensees(lieu):
    rc, d = lancer(lieu, lignes=flux(bonne(pensees=0)))
    assert rc == 3 and meta(d)["defaut"] == garde_statut()


def garde_statut():
    return appel.garde.STATUT_SANS_PENSEES


def test_reseau(lieu):
    rc, d = lancer(lieu, exc=urllib.error.URLError("hors ligne"))
    m = meta(d)
    assert rc == 3 and m["defaut"] == "RESEAU_URLError"
    assert m["cout_compte_usd"] == m["pire_cas_usd"]   # sans usage, le pire cas reste compté


def test_http_erreur_masque_la_cle(lieu):
    exc = urllib.error.HTTPError("u", 400, "x", {}, io.BytesIO(b"erreur cle-factice"))
    rc, d = lancer(lieu, exc=exc)
    m = meta(d)
    assert rc == 3 and m["defaut"] == "HTTP_400" and "cle-factice" not in json.dumps(m)


def test_r12_sortie_existante(lieu):
    d, _ = lieu
    (d / "sortie.json").write_text("{}")
    rc, _ = lancer(lieu, lignes=flux(bonne()))
    assert rc == 1


def test_cle_absente(lieu, monkeypatch):
    monkeypatch.delenv("GEMINI_API_KEY")
    d, e = lieu
    argv = ["argon", str(e), str(d / "s.md"), str(d / "s.json"), "--journal", str(d / "j.jsonl")]
    assert appel.main(argv, ouvrir=ouvreur(flux(bonne())), maintenant=JOUR) == 1
