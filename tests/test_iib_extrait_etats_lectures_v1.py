"""Essais de `scripts/extrait_iib_etats_lectures_cote_moniteurs_v1.py` (R5 : cas sain et artefacts), sur des lectures factices."""
import importlib.util
import json
from pathlib import Path

import pytest

from controle_ia.scellement import sceller

RACINE_DEPOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("etats", RACINE_DEPOT / "scripts" / "extrait_iib_etats_lectures_cote_moniteurs_v1.py")
ex = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ex)

RUN = "20991231-000000-iib-explo-factice"


def _ecrire(p: Path, x) -> None:
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(x, ensure_ascii=False), encoding="utf-8")
    sceller(p)


def _l1(**ecart):
    return {"avertissement": "x", "phrase": "dommage agrégé vu", "effets": {"B100-H": {"effet": 0.123, "bas": 0.05}},
            "dose_realisee": {"0.5": 0.07, "1": 0.12}, "exces_moyen_des_donnees": 0.31, **ecart}


def _l2(**ecart):
    jeux = {k: {"etat": "échoue", "aire": 0.61, "taux_1_pour_cent": {"x": 0.02}} for k in ex.JEUX}
    unites = {u: {"etat": "échoue", "aire_a": 0.6, "base_decisive": "b"} for u in ex.UNITES}
    return {"avertissement": "x", "jeux": jeux, "phrase_par_action": "sous le seuil par action", "mots_et_cout": "échoue",
            "etat_par_unite": {"regle": "r", "unite_decisive": "B100-H", "unites": unites},
            "phrase": "diffus réalisé, à titre exploratoire, hors juge d'une autre lignée", "seuils": {"sous": 0.05}, **ecart}


def _lectures(r: Path, l1=None, l2=None) -> None:
    d = r / "diag" / RUN
    if l1 is not False:
        _ecrire(d / ex.NOM_DOMMAGE, l1 if l1 is not None else _l1())
    if l2 is not False:
        _ecrire(d / ex.NOM_DIFFUSION, l2 if l2 is not None else _l2())
    _ecrire(d / "lecture-iib-2-mots-ponderes-exploratoire-non-opposable-v1.json", {"mots": ["secretmot"]})


def _jouer(r: Path, sortie: Path) -> int:
    return ex.main(["--racine", str(r), "--run-id", RUN, "--sortie", str(sortie)])


def test_cas_sain_etats_seuls(tmp_path):
    _lectures(tmp_path)
    s = tmp_path / "sortie" / "etats.json"
    assert _jouer(tmp_path, s) == 0
    x = json.loads(s.read_text(encoding="utf-8"))
    assert set(x) == {"avertissement", "run_id", "lecture_dommage", "lecture_diffusion"}
    assert x["lecture_dommage"] == {"phrase": "dommage agrégé vu"}
    assert set(x["lecture_diffusion"]) == {"par_paire", "phrase"}
    assert set(x["lecture_diffusion"]["par_paire"]) == set(ex.UNITES) | {"B100-TJ100"}
    texte = s.read_text(encoding="utf-8")
    assert not any(c.isdigit() for c in texte.replace(ex.AVERTISSEMENT, "").replace(RUN, "").replace("B100", "").replace("B50", "")
                   .replace("TJ100", ""))
    for interdit in ("secretmot", '"aire', "taux", "effet", "seuils", "sous le seuil", "dose_realisee", "exces", "base_decisive"):
        assert interdit not in texte
    assert (tmp_path / "sortie" / "etats.json.sha256").is_file()


def test_cas_sain_phrase_de_diffusion_nulle_et_non_calculable(tmp_path):
    l2 = _l2(phrase=None)
    l2["jeux"]["traits/B50-H"]["etat"] = "non calculable"
    l2["etat_par_unite"]["unites"]["TJ100-H"]["etat"] = "réussit"
    _lectures(tmp_path, l2=l2)
    s = tmp_path / "e.json"
    assert _jouer(tmp_path, s) == 0
    x = json.loads(s.read_text(encoding="utf-8"))
    assert x["lecture_diffusion"]["phrase"] is None
    assert x["lecture_diffusion"]["par_paire"]["B50-H"]["traits"] == "non calculable"
    assert x["lecture_diffusion"]["par_paire"]["TJ100-H"]["unite"] == "réussit"


@pytest.mark.parametrize("phrase", ["dommage agrégé vu, effet 0,12", 0.12, None, True, "Dommage agrégé vu"])
def test_artefact_phrase_du_dommage_hors_vocabulaire(tmp_path, phrase, capsys):
    _lectures(tmp_path, l1=_l1(phrase=phrase))
    s = tmp_path / "e.json"
    assert _jouer(tmp_path, s) == 1
    assert not s.exists()
    assert "0,12" not in capsys.readouterr().err


@pytest.mark.parametrize("etat", ["réussit à 0,71", 0.71, None, "reussit"])
def test_artefact_etat_de_jeu_hors_vocabulaire(tmp_path, etat):
    l2 = _l2()
    l2["jeux"]["cout/B100-H"]["etat"] = etat
    _lectures(tmp_path, l2=l2)
    assert _jouer(tmp_path, tmp_path / "e.json") == 1


def test_artefact_etat_d_unite_hors_vocabulaire(tmp_path):
    l2 = _l2()
    l2["etat_par_unite"]["unites"]["B100-H"]["etat"] = "échoue (aire 0,64)"
    _lectures(tmp_path, l2=l2)
    assert _jouer(tmp_path, tmp_path / "e.json") == 1


def test_artefact_phrase_de_diffusion_libre(tmp_path):
    _lectures(tmp_path, l2=_l2(phrase="diffus réalisé à 0,3"))
    assert _jouer(tmp_path, tmp_path / "e.json") == 1


def test_artefact_jeu_en_trop_ou_manquant(tmp_path):
    l2 = _l2()
    l2["jeux"]["cout/B100-TJ100"] = {"etat": "échoue"}
    _lectures(tmp_path, l2=l2)
    assert _jouer(tmp_path, tmp_path / "e.json") == 1
    l2 = _l2()
    del l2["jeux"]["traits/TJ100-H"]
    _lectures(tmp_path / "b", l2=l2)
    assert _jouer(tmp_path / "b", tmp_path / "f.json") == 1


def test_artefact_unite_manquante(tmp_path):
    l2 = _l2()
    del l2["etat_par_unite"]["unites"]["B50-H"]
    _lectures(tmp_path, l2=l2)
    assert _jouer(tmp_path, tmp_path / "e.json") == 1


def test_artefact_phrase_de_diffusion_absente(tmp_path):
    l2 = _l2()
    del l2["phrase"]
    _lectures(tmp_path, l2=l2)
    assert _jouer(tmp_path, tmp_path / "e.json") == 1


def test_artefact_lecture_absente(tmp_path):
    _lectures(tmp_path, l2=False)
    assert _jouer(tmp_path, tmp_path / "e.json") == 1


def test_artefact_lecture_alteree_apres_sceau(tmp_path):
    _lectures(tmp_path)
    p = tmp_path / "diag" / RUN / ex.NOM_DOMMAGE
    p.write_text(json.dumps(_l1(phrase="dommage non vu à cette puissance")), encoding="utf-8")
    assert _jouer(tmp_path, tmp_path / "e.json") == 1


def test_artefact_pas_d_ecrasement(tmp_path):
    _lectures(tmp_path)
    s = tmp_path / "e.json"
    s.write_text("ancien")
    assert _jouer(tmp_path, s) == 1
    assert s.read_text() == "ancien"
