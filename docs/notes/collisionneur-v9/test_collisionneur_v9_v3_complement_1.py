"""Complément 1 des essais du collisionneur v9-v3 (demandé par la contre-lecture contre-lecture-collisionneur-v9-v3-v1.md) :
quatre artefacts qui manquaient, chacun avec son cas sain (R5). Hors réseau, mêmes doublures que test_collisionneur_v9_v3.py.
Le script collisionneur_v9_v3.py (850df311…) n'est pas changé.

Lancement : PYTHONPATH=src .venv/bin/python -B -m pytest -q docs/notes/collisionneur-v9/test_collisionneur_v9_v3_complement_1.py
"""
import pytest

from test_collisionneur_v9_v3 import (SAIN, FauxTransport, c, cree_openai, executer, final_openai,  # noqa: F401
                                      flux_anthropic)


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
