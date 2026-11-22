"""Essais sans réseau de appel_google_garde_v3_v6.py (cas sain et artefacts, R5). Lancer :
. .venv/bin/activate && PYTHONPATH=src python -m pytest -q docs/notes/memoire-conception-v1/appel-google-garde-v3-v6/"""
import datetime as dt
import importlib.util
import io
import json
import os
import urllib.error

import pytest

ICI = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("appel_v6", os.path.join(ICI, "appel_google_garde_v3_v6.py"))
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
    with open(d / "journal.jsonl") as f:
        total, n = appel.lire_journal(f)
    assert n == 1 and abs(total - m["cout_compte_usd"]) < 1e-6 and lignes[1]["cout_compte_usd"] == m["cout_compte_usd"]


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


def test_plafond_course_au_dela_de_5(lieu):
    rc, _ = lancer(lieu, lignes=flux(bonne()), extra=["--plafond-usd", "5.5"])
    assert rc == 1


def test_plafond_cumule(lieu):
    d, _ = lieu
    j = d / "journal.jsonl"
    j.write_text(json.dumps({"id": "a", "etat": "reserve", "cout_compte_usd": 4.5}) + "\n")
    rc, _ = lancer(lieu, lignes=flux(bonne()), journal=str(j))
    assert rc == 1   # 4,5 + pire cas (≈ 0,98) > 5


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


def test_modele_servi_suffixe_non_numerique(lieu):
    rc, d = lancer(lieu, lignes=flux(bonne(servi="gemini-4-argon-lite")))
    assert rc == 3 and meta(d)["defaut"] == "MODELE_SERVI_DIFFERENT"


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


def test_flux_coupe_sans_fin_compte_le_pire(lieu):
    o = bonne()
    del o["candidates"][0]["finishReason"]
    rc, d = lancer(lieu, lignes=flux(o))
    m = meta(d)
    assert rc == 3 and m["cout_compte_usd"] == m["pire_cas_usd"]


def test_flux_illisible_compte_le_pire(lieu):
    rc, d = lancer(lieu, lignes=flux(bonne(), brut=[b"data: {pas du json\n"]))
    m = meta(d)
    assert m["cout_compte_usd"] == m["pire_cas_usd"]


def test_morceau_mal_forme_sans_exception(lieu):
    rc, d = lancer(lieu, lignes=flux({"candidates": "pas une liste d'objets"}, {"usageMetadata": [1, 2]}, bonne()))
    assert rc == 3 and meta(d)["defaut"] == "FLUX_ILLISIBLE"


@pytest.mark.parametrize("ligne", [{"id": "a", "etat": "reserve", "cout_compte_usd": float("nan")},
                                   {"id": "a", "etat": "reserve", "cout_compte_usd": -5},
                                   {"id": "b", "etat": "solde", "cout_compte_usd": 0.1},
                                   {"etat": "reserve", "cout_compte_usd": 0.1}])
def test_journal_incoherent(lieu, ligne):
    d, _ = lieu
    j = d / "journal.jsonl"
    j.write_text(json.dumps(ligne) + "\n")
    rc, _ = lancer(lieu, lignes=flux(bonne()), journal=str(j))
    assert rc == 1


def test_identifiant_repete(lieu):
    d, _ = lieu
    j = d / "journal.jsonl"
    r = json.dumps({"id": "a", "etat": "reserve", "cout_compte_usd": 0.1})
    j.write_text(r + "\n" + r + "\n")
    rc, _ = lancer(lieu, lignes=flux(bonne()), journal=str(j))
    assert rc == 1


def test_trois_appels_puis_refus(lieu):
    d, e = lieu
    j = str(d / "journal.jsonl")
    rcs = []
    for k in range(6):
        argv = ["argon", str(e), str(d / f"s{k}.md"), str(d / f"s{k}.json"), "--journal", j]
        rcs.append(appel.main(argv, ouvrir=ouvreur(exc=urllib.error.URLError("x")), maintenant=JOUR))
    assert rcs == [3, 3, 3, 3, 3, 1]   # sans usage, chaque appel compte son pire cas (≈ 0,98 USD) ; 5 × 0,98 ≤ 5


def test_appels_en_parallele(lieu):
    import multiprocessing as mp
    d, e = lieu
    j = str(d / "journal.jsonl")
    ctx = mp.get_context("fork")
    with ctx.Pool(6) as pool:
        rcs = pool.starmap(_lancer_proc, [(str(e), str(d), j, k) for k in range(6)])
    lignes = [json.loads(l) for l in open(j)]
    reserve = sum(l["cout_compte_usd"] for l in lignes if l["etat"] == "reserve")
    assert reserve <= 5.0 and rcs.count(1) >= 1


def _lancer_proc(e, d, j, k):
    os.environ["GEMINI_API_KEY"] = "cle-factice"

    def lent(req, timeout=None):
        import time
        time.sleep(0.3)
        raise urllib.error.URLError("x")
    argv = ["argon", e, os.path.join(d, f"p{k}.md"), os.path.join(d, f"p{k}.json"), "--journal", j]
    return appel.main(argv, ouvrir=lent, maintenant=JOUR)


def test_mots_en_lettres(lieu):
    rc, _ = lancer(lieu, enonce_txt="Réponds en deux mille mots, et en 2000 mots au plus.", lignes=flux(bonne()))
    assert rc == 1


def test_tarif_haut_des_le_30(lieu):
    d, e = lieu
    argv = ["argon", str(e), str(d / "s.md"), str(d / "s.json"), "--journal", str(d / "j.jsonl")]
    assert appel.main(argv, ouvrir=ouvreur(flux(bonne())),
                      maintenant=dt.datetime(2026, 11, 30, 0, 0, tzinfo=dt.timezone.utc)) == 0
    assert json.loads((d / "s.json").read_text())["prix_usd_par_million"] == {"entree": 4.0, "sortie": 20.0}


def test_garde_alteree(lieu, monkeypatch):
    monkeypatch.setattr(appel, "sha256_fichier", lambda c: "0" * 64 if c.endswith("garde_google_v3.py") else
                        __import__("hashlib").sha256(open(c, "rb").read()).hexdigest())
    rc, _ = lancer(lieu, lignes=flux(bonne()))
    assert rc == 1


def test_ligne_trop_longue(lieu):
    rc, _ = lancer(lieu, enonce_txt=SAIN + "\n" + "x" * 30000, lignes=flux(bonne()))
    assert rc == 1


def test_journal_par_identifiant(lieu):
    rc, d = lancer(lieu, lignes=flux(bonne()))
    lignes = [json.loads(l) for l in (d / "journal.jsonl").read_text().splitlines()]
    assert lignes[0]["id"] == lignes[1]["id"] == meta(d)["id_appel"]


class FluxCoupe:
    """Rend quelques lignes puis lève une coupure (http.client.IncompleteRead)."""
    status = 200

    def __init__(self, lignes):
        self.lignes = lignes

    def __enter__(self):
        return self

    def __exit__(self, *a):
        return False

    def __iter__(self):
        import http.client
        for l in self.lignes:
            yield l
        raise http.client.IncompleteRead(b"")


def test_coupure_incompleteread_garde_le_texte(lieu):
    d, e = lieu
    o = bonne(texte="début du texte")
    del o["candidates"][0]["finishReason"]
    argv = ["argon", str(e), str(d / "s.md"), str(d / "s.json"), "--journal", str(d / "j.jsonl")]
    rc = appel.main(argv, ouvrir=lambda req, timeout=None: FluxCoupe(flux(o)), maintenant=JOUR)
    m = json.loads((d / "s.json").read_text())
    assert rc == 3 and m["defaut"] == "RESEAU_IncompleteRead"
    assert (d / "s.md.defaut.md").read_text() == "début du texte" and m["cout_compte_usd"] == m["pire_cas_usd"]
    etats = [json.loads(l)["etat"] for l in (d / "j.jsonl").read_text().splitlines()]
    assert etats == ["reserve", "solde"]


def test_exception_quelconque_nommee(lieu):
    rc, d = lancer(lieu, exc=ValueError("imprévu"))
    assert rc == 3 and meta(d)["defaut"] == "ERREUR_ValueError"


@pytest.mark.parametrize("mutation", ["texte_none", "jetons_chaine", "fin_liste", "retour_chaine"])
def test_types_mal_formes(lieu, mutation):
    o = bonne()
    if mutation == "texte_none":
        o["candidates"][0]["content"]["parts"][1]["text"] = None
    elif mutation == "jetons_chaine":
        o["usageMetadata"]["thoughtsTokenCount"] = "120"
    elif mutation == "fin_liste":
        o["candidates"][0]["finishReason"] = ["STOP"]
    else:
        o["promptFeedback"] = "bloqué"
    rc, d = lancer(lieu, lignes=flux(o))
    assert rc == 3 and meta(d)["defaut"] == "FLUX_ILLISIBLE"


@pytest.mark.parametrize("texte", ["Réponds en 10k mots.", "Answer in 5000 words. Réponds en 2000 mots."])
def test_mots_k_ou_anglais(lieu, texte):
    rc, _ = lancer(lieu, enonce_txt=texte, lignes=flux(bonne()))
    assert rc == 1


def test_garde_rescellee_refusee(lieu, monkeypatch):
    monkeypatch.setitem(appel.GARDES_SHA256, "garde_google_v3.py", "1" * 64)
    rc, _ = lancer(lieu, lignes=flux(bonne()))
    assert rc == 1


def test_neon_cas_sain(lieu):
    d, e = lieu
    argv = ["neon", str(e), str(d / "n.md"), str(d / "n.json"), "--journal", str(d / "jn.jsonl")]
    assert appel.main(argv, ouvrir=ouvreur(flux(bonne(servi="gemini-4-neon"))), maintenant=JOUR) == 0
    m = json.loads((d / "n.json").read_text())
    assert m["reglage"]["thinkingConfig"]["thinkingLevel"] == "xhigh"
    assert m["prix_usd_par_million"] == {"entree": 3.0, "sortie": 15.0}


def test_neon_servi_argon_refuse(lieu):
    d, e = lieu
    argv = ["neon", str(e), str(d / "n.md"), str(d / "n.json"), "--journal", str(d / "jn.jsonl")]
    assert appel.main(argv, ouvrir=ouvreur(flux(bonne(servi="gemini-4-argon"))), maintenant=JOUR) == 3


def test_journaux_associes_cumul(lieu):
    d, e = lieu
    ja, jc = d / "ja.jsonl", d / "jc.jsonl"
    ja.write_text(json.dumps({"id": "a", "etat": "reserve", "cout_compte_usd": 2.0}) + "\n")
    jc.write_text(json.dumps({"id": "c", "etat": "reserve", "cout_compte_usd": 2.5}) + "\n")
    argv = ["neon", str(e), str(d / "n.md"), str(d / "n.json"), "--journal", str(d / "jn.jsonl"),
            "--journaux-associes", str(ja), str(jc)]
    assert appel.main(argv, ouvrir=ouvreur(flux(bonne(servi="gemini-4-neon"))), maintenant=JOUR) == 1


def test_journal_associe_illisible(lieu):
    d, e = lieu
    ja = d / "ja.jsonl"
    ja.write_text("pas du json\n")
    argv = ["argon", str(e), str(d / "s.md"), str(d / "s.json"), "--journal", str(d / "j.jsonl"),
            "--journaux-associes", str(ja)]
    assert appel.main(argv, ouvrir=ouvreur(flux(bonne())), maintenant=JOUR) == 1


def test_journal_associe_identique(lieu):
    d, e = lieu
    j = str(d / "j.jsonl")
    argv = ["argon", str(e), str(d / "s.md"), str(d / "s.json"), "--journal", j, "--journaux-associes", j]
    assert appel.main(argv, ouvrir=ouvreur(flux(bonne())), maintenant=JOUR) == 1


def test_trois_modeles_sous_5(lieu):
    d, e = lieu
    js = {k: str(d / f"j{k}.jsonl") for k in ("argon", "carbon", "neon")}
    for v in js.values():
        open(v, "w").close()
    rcs = []
    for tour in range(3):
        for esp in ("argon", "carbon", "neon"):
            autres = [v for k, v in js.items() if k != esp]
            argv = [esp, str(e), str(d / f"{esp}{tour}.md"), str(d / f"{esp}{tour}.json"), "--journal", js[esp],
                    "--journaux-associes", *autres]
            rcs.append(appel.main(argv, ouvrir=ouvreur(exc=urllib.error.URLError("x")), maintenant=JOUR))
    total = 0.0
    for v in js.values():
        with open(v) as f:
            total += appel.lire_journal(f)[0]
    assert total <= 5.0 and rcs.count(1) >= 1


def test_journal_associe_absent(lieu):
    d, e = lieu
    argv = ["argon", str(e), str(d / "s.md"), str(d / "s.json"), "--journal", str(d / "j.jsonl"),
            "--journaux-associes", str(d / "carbonn.jsonl")]
    assert appel.main(argv, ouvrir=ouvreur(flux(bonne())), maintenant=JOUR) == 1


def test_lien_symbolique_vers_soi(lieu):
    d, e = lieu
    j = d / "j.jsonl"; j.write_text("")
    lien = d / "lien.jsonl"; os.symlink(j, lien)
    argv = ["argon", str(e), str(d / "s.md"), str(d / "s.json"), "--journal", str(j), "--journaux-associes", str(lien)]
    assert appel.main(argv, ouvrir=ouvreur(flux(bonne())), maintenant=JOUR) == 1


def test_totaux_par_journal(lieu):
    d, e = lieu
    ja = d / "ja.jsonl"; ja.write_text(json.dumps({"id": "a", "etat": "reserve", "cout_compte_usd": 1.0}) + "\n")
    argv = ["argon", str(e), str(d / "s.md"), str(d / "s.json"), "--journal", str(d / "j.jsonl"), "--journaux-associes", str(ja)]
    assert appel.main(argv, ouvrir=ouvreur(flux(bonne())), maintenant=JOUR) == 0
    m = json.loads((d / "s.json").read_text())
    assert m["totaux_journaux_avant_usd"][str(ja)] == 1.0 and m["depense_cumulee_avant_usd"] == 1.0


def _proc_croise(e, d, mien, autre, k):
    os.environ["GEMINI_API_KEY"] = "cle-factice"

    def lent(req, timeout=None):
        import time
        time.sleep(0.2)
        raise urllib.error.URLError("x")
    argv = ["argon" if k % 2 else "carbon", e, os.path.join(d, f"c{k}.md"), os.path.join(d, f"c{k}.json"),
            "--journal", mien, "--journaux-associes", autre]
    return appel.main(argv, ouvrir=lent, maintenant=JOUR)


def test_croises_en_parallele_sans_interblocage(lieu):
    import multiprocessing as mp
    d, e = lieu
    j1, j2 = str(d / "j1.jsonl"), str(d / "j2.jsonl")
    open(j1, "w").close(); open(j2, "w").close()
    args = [(str(e), str(d), j1 if k % 2 else j2, j2 if k % 2 else j1, k) for k in range(8)]
    with mp.get_context("fork").Pool(8) as pool:
        res = pool.starmap_async(_proc_croise, args)
        rcs = res.get(timeout=60)
    total = 0.0
    for j in (j1, j2):
        with open(j) as f:
            total += appel.lire_journal(f)[0]
    assert total <= 5.0 and rcs.count(1) >= 1
