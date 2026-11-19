"""Essais de `scripts/extrait_iib_cote_moniteurs_v1.py` (R5 : cas sain et artefacts), sur une course factice."""
import importlib.util
import json
from pathlib import Path

import pytest

from controle_ia.scellement import sceller

RACINE_DEPOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("extrait", RACINE_DEPOT / "scripts" / "extrait_iib_cote_moniteurs_v1.py")
ex = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ex)

RUN = "20991231-000000-iib-explo-factice"
COMMIT = "b" * 40


def _json(p: Path, x) -> None:
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(x), encoding="utf-8")
    sceller(p)


def _course(r: Path, etats=None, commit=COMMIT) -> None:
    d = r / "donnees" / RUN
    d.mkdir(parents=True)
    emp = {}
    for i, nom in enumerate(ex.FICHIERS_PASSE):
        (d / nom).write_bytes(f"contenu factice {i}".encode())
        emp[f"donnees/{RUN}/{nom}"] = sceller(d / nom)
    (d / "oracle-iib-evaluation.json").write_text("{}", encoding="utf-8")
    emp[f"donnees/{RUN}/oracle-iib-evaluation.json"] = sceller(d / "oracle-iib-evaluation.json")
    _json(r / "runs" / RUN / "manifeste.json", {"run_id": RUN, "commit": commit, "config": {"secret": "jamais copié"},
                                                "versions": {"python": "3.13", "torch": "2.14.1"}, "graines": {"x": 1}})
    _json(r / "diag" / RUN / "resume.json", {"run_id": RUN, "resultat": {"empreintes": emp, "acceptes": 99, "tours": 7}})
    if etats is None:
        etats = [{"condition": c, "lot": 1, "adaptateur": "eleve", "dose_avant": 0.5, "dose_apres": 0.5, "empreinte": "e" * 64}
                 for c in ex.CONDITIONS]
    _json(r / "diag" / RUN / "episodes-iib.json", {"fiches": [{"couts": [1.0]}], "etats_par_lot": etats, "effectifs": {"tour1": 3}})


def _jouer(r: Path, sortie: Path, commit=COMMIT) -> int:
    return ex.main(["--racine", str(r), "--run-id", RUN, "--commit-lancement", commit, "--sortie", str(sortie)])


def test_cas_sain_n_emporte_que_le_permis(tmp_path):
    _course(tmp_path)
    s = tmp_path / "sortie" / "extrait.json"
    assert _jouer(tmp_path, s) == 0
    x = json.loads(s.read_text(encoding="utf-8"))
    assert set(x) == {"avertissement", "run_id", "commit_lancement", "versions", "fichiers_de_la_passe", "etats_par_lot_evaluation"}
    assert set(x["fichiers_de_la_passe"]) == {f"donnees/{RUN}/{n}" for n in ex.FICHIERS_PASSE}
    texte = s.read_text(encoding="utf-8")
    for interdit in ("secret", "oracle", "graines", "acceptes", "tours", "couts", "effectifs", "fiches"):
        assert interdit not in texte
    assert (tmp_path / "sortie" / "extrait.json.sha256").is_file()


def test_artefact_commit_different(tmp_path):
    _course(tmp_path, commit="c" * 40)
    assert _jouer(tmp_path, tmp_path / "x.json") == 1
    assert not (tmp_path / "x.json").exists()


def test_artefact_fichier_de_la_passe_absent_du_resume(tmp_path):
    _course(tmp_path)
    p = tmp_path / "diag" / RUN / "resume.json"
    r = json.loads(p.read_text())
    del r["resultat"]["empreintes"][f"donnees/{RUN}/adaptateur-eleve.pt"]
    p.write_text(json.dumps(r))
    (tmp_path / "diag" / RUN / "resume.json.sha256").unlink()
    sceller(p)
    assert _jouer(tmp_path, tmp_path / "x.json") == 1


def test_artefact_fichier_altere_sur_disque(tmp_path):
    _course(tmp_path)
    (tmp_path / "donnees" / RUN / "adaptateur-temoin-jumeau.pt").write_bytes(b"altere")
    assert _jouer(tmp_path, tmp_path / "x.json") == 1


def test_artefact_resume_altere(tmp_path):
    _course(tmp_path)
    (tmp_path / "diag" / RUN / "resume.json").write_text("{}")
    assert _jouer(tmp_path, tmp_path / "x.json") == 1


@pytest.mark.parametrize("ligne", [
    {"condition": "H", "lot": 1, "adaptateur": "eleve", "dose_avant": 0.0, "dose_apres": 0.0, "empreinte": "e", "couts": [1]},
    {"condition": "maitre_iib", "lot": 1, "adaptateur": "eleve", "dose_avant": 0.0, "dose_apres": 0.0, "empreinte": "e"},
])
def test_artefact_ligne_d_etat_hors_permis(tmp_path, ligne):
    _course(tmp_path, etats=[ligne])
    assert _jouer(tmp_path, tmp_path / "x.json") == 1


def test_artefact_pas_d_ecrasement(tmp_path):
    _course(tmp_path)
    s = tmp_path / "x.json"
    s.write_text("ancien")
    assert _jouer(tmp_path, s) == 1
    assert s.read_text() == "ancien"


def test_artefact_commit_mal_forme(tmp_path):
    _course(tmp_path)
    assert _jouer(tmp_path, tmp_path / "x.json", commit="abc") == 1
