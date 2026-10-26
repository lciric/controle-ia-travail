"""Gardes et lecture de `analyser_echelle_v1.py` sur des activations synthétiques à vérité connue (R5) :
cas sains (positif, nul, pas de fuite, inverse, non certifiable, fuite non spécifique) et artefacts (ordre des
identifiants, empreinte, valeur non finie, sortie déjà présente). Lancement : python -m pytest -q echelle-v1/tests
"""
import hashlib
import importlib.util
import json
import pathlib
import subprocess
import sys

import numpy as np
import pytest

ICI = pathlib.Path(__file__).resolve().parent
SCRIPTS = ICI.parent / "scripts"


def charger(nom):
    spec = importlib.util.spec_from_file_location(nom, SCRIPTS / f"{nom}.py")
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


AN = charger("analyser_echelle_v1")


@pytest.fixture(scope="module")
def stimuli(tmp_path_factory):
    d = tmp_path_factory.mktemp("stim") / "s"
    subprocess.run([sys.executable, "-I", "-B", str(SCRIPTS / "construire_echelle_v1.py"), str(d)], check=True,
                   capture_output=True)
    return d / "echelle-v1.json"


def sha(p):
    return hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()


def sceller(f):
    f = pathlib.Path(f)
    (f.parent / (f.name + ".sha256")).write_text(f"{sha(f)}  {f.name}\n", encoding="utf-8")


def fabriquer(dossier, stimuli, alpha, graine, force_c=4.0, alpha_placebo=0.0, d=64, couches=(4, 6)):
    """x = contenu + s_f·F + s_c·C + s_p·P + cadrage + bruit, avec F = alpha·C + alpha_placebo·P + F⊥ (à la couche
    principale, la dernière ; la première porte un contexte deux fois plus faible). λ vrai = alpha."""
    doc = json.loads(pathlib.Path(stimuli).read_text(encoding="utf-8"))
    st = doc["stimuli"]
    rng = np.random.default_rng(graine)
    base = np.linalg.qr(rng.normal(size=(d, 4)))[0].T  # quatre directions orthonormées
    C, P, Fp = base[0] * force_c, base[1] * 2.0, base[2] * 2.0
    contenus = rng.normal(size=(64, d)) * 1.0
    cadrage = {}
    dossier = pathlib.Path(dossier)
    dossier.mkdir(parents=True)
    ids, sorties = [s["id"] for s in st], {}
    for k, c in enumerate(couches):
        echelle_c = 0.5 if k == 0 else 1.0
        F = alpha * C * echelle_c + alpha_placebo * P + Fp
        X = np.empty((len(st), d))
        for i, s in enumerate(st):
            sf = 0.5 if s["format"] == "qcm" else -0.5
            sc = {"eval": 0.5, "reel": -0.5}.get(s["classe"], 0.0)
            sp = {"mer": 0.5, "montagne": -0.5}.get(s["classe"], 0.0)
            cle = (s["jeu"], s["paire"], s["classe"])
            if cle not in cadrage:
                cadrage[cle] = rng.normal(size=d) * 0.15
            X[i] = (contenus[s["contenu"]] + sf * F + sc * C * echelle_c + sp * P + cadrage[cle]
                    + rng.normal(size=d) * 1.0)
        f = dossier / f"activations-L{c}.npy"
        np.save(f, X.astype(np.float16))
        sceller(f)
        sorties[f.name] = sha(f)
    f_ids = dossier / "ids.json"
    f_ids.write_text(json.dumps(ids) + "\n", encoding="utf-8")
    sceller(f_ids)
    sorties["ids.json"] = sha(f_ids)
    m = {"modele": f"synthetique-{alpha}", "revision": None, "couches": list(couches), "dimension": d,
         "sha256_sorties": sorties}
    (dossier / "manifeste-mesure.json").write_text(json.dumps(m), encoding="utf-8")
    sceller(dossier / "manifeste-mesure.json")
    return dossier


def analyser(tmp_path, stimuli, petit, grand, nom="sortie"):
    sortie = tmp_path / nom
    code = AN.principal([str(stimuli), str(petit), str(grand), "12345", str(sortie)])
    lu = json.loads((sortie / "analyse-echelle-v1.json").read_text(encoding="utf-8")) if code == 0 else None
    return code, lu


def test_aire_ponderee_egale_aire_dupliquee():
    rng = np.random.default_rng(0)
    pos, neg = rng.normal(size=7).round(1), rng.normal(size=9).round(1)
    wp, wn = rng.integers(0, 3, size=7).astype(float), rng.integers(1, 3, size=9).astype(float)
    dup_p, dup_n = np.repeat(pos, wp.astype(int)), np.repeat(neg, wn.astype(int))
    attendu = np.mean([(a > b) + 0.5 * (a == b) for a in dup_p for b in dup_n])
    assert AN.auroc_pondere(pos, wp, neg, wn) == pytest.approx(attendu)


def test_positif(tmp_path, stimuli):
    code, r = analyser(tmp_path, stimuli, fabriquer(tmp_path / "p", stimuli, 1.0, 1), fabriquer(tmp_path / "g", stimuli, 0.1, 2))
    assert code == 0
    assert r["lecture"] == "positif" and r["reserves"] == []
    assert r["petit"]["lambda"] == pytest.approx(1.0, abs=0.25) and r["grand"]["lambda"] == pytest.approx(0.1, abs=0.25)
    assert r["petit"]["couche"] == 6 and r["grand"]["couche"] == 6  # la couche au contexte le plus fort


def test_nul(tmp_path, stimuli):
    code, r = analyser(tmp_path, stimuli, fabriquer(tmp_path / "p", stimuli, 0.5, 3), fabriquer(tmp_path / "g", stimuli, 0.5, 4))
    assert code == 0 and r["lecture"] in ("nul", "indécis")
    assert r["delta_lambda_ic"][0] < 0 < r["delta_lambda_ic"][1]


def test_pas_de_fuite(tmp_path, stimuli):
    code, r = analyser(tmp_path, stimuli, fabriquer(tmp_path / "p", stimuli, 0.0, 5), fabriquer(tmp_path / "g", stimuli, 0.0, 6))
    assert code == 0 and r["lecture"] == "pas de fuite"


def test_inverse(tmp_path, stimuli):
    code, r = analyser(tmp_path, stimuli, fabriquer(tmp_path / "p", stimuli, 0.1, 7), fabriquer(tmp_path / "g", stimuli, 1.0, 8))
    assert code == 0 and r["lecture"] == "inverse"


def test_non_certifiable(tmp_path, stimuli):
    code, r = analyser(tmp_path, stimuli, fabriquer(tmp_path / "p", stimuli, 1.0, 9, force_c=0.05),
                       fabriquer(tmp_path / "g", stimuli, 0.1, 10, force_c=0.05))
    assert code == 0 and r["lecture"] == "non certifiable"


def test_certification_asymetrique(tmp_path, stimuli):
    code, r = analyser(tmp_path, stimuli, fabriquer(tmp_path / "p", stimuli, 1.0, 19, force_c=0.05),
                       fabriquer(tmp_path / "g", stimuli, 0.1, 20))
    assert code == 0 and r["lecture"] == "certification asymétrique (grand seulement)"
    assert r["delta_A_ctx_ic"][0] > 0


def test_fuite_non_specifique(tmp_path, stimuli):
    # au petit modèle, le format s'aligne aussi fort sur le placebo que sur le contexte : réserve
    code, r = analyser(tmp_path, stimuli, fabriquer(tmp_path / "p", stimuli, 1.0, 11, alpha_placebo=1.0),
                       fabriquer(tmp_path / "g", stimuli, 0.1, 12))
    assert code == 0 and r["lecture"] == "positif"
    assert r["reserves"] and "non spécifique" in r["reserves"][0]


def test_artefact_ordre(tmp_path, stimuli):
    p = fabriquer(tmp_path / "p", stimuli, 1.0, 13)
    ids = json.loads((p / "ids.json").read_text())
    ids[0], ids[1] = ids[1], ids[0]
    (p / "ids.json").write_text(json.dumps(ids) + "\n")
    sceller(p / "ids.json")
    code, _ = analyser(tmp_path, stimuli, p, fabriquer(tmp_path / "g", stimuli, 0.1, 14))
    assert code == 1 and not (tmp_path / "sortie").exists()


def test_artefact_empreinte(tmp_path, stimuli):
    p = fabriquer(tmp_path / "p", stimuli, 1.0, 15)
    X = np.load(p / "activations-L6.npy")
    X[0, 0] += 1
    np.save(p / "activations-L6.npy", X)
    code, _ = analyser(tmp_path, stimuli, p, fabriquer(tmp_path / "g", stimuli, 0.1, 16))
    assert code == 1


def test_artefact_non_fini(tmp_path, stimuli):
    p = fabriquer(tmp_path / "p", stimuli, 1.0, 17)
    X = np.load(p / "activations-L6.npy")
    X[3, 2] = np.nan
    np.save(p / "activations-L6.npy", X)
    sceller(p / "activations-L6.npy")
    m = json.loads((p / "manifeste-mesure.json").read_text())
    m["sha256_sorties"]["activations-L6.npy"] = sha(p / "activations-L6.npy")
    (p / "manifeste-mesure.json").write_text(json.dumps(m))
    sceller(p / "manifeste-mesure.json")
    code, _ = analyser(tmp_path, stimuli, p, fabriquer(tmp_path / "g", stimuli, 0.1, 18))
    assert code == 1


def test_sortie_presente(tmp_path, stimuli):
    (tmp_path / "sortie").mkdir()
    code = AN.principal([str(stimuli), "x", "y", "1", str(tmp_path / "sortie")])
    assert code == 2
