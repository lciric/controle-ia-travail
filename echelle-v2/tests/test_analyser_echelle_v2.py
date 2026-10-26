"""Gardes et lecture de `analyser_echelle_v2.py` (R5, CLX-01, CLX-02, CLX-04, CLX-06, CLX-10, CLX-11) :
- lecture mécanique sur des intervalles fabriqués, une branche par issue ;
- intégration sur des activations synthétiques à vérité connue (positif, nul, invariance par translation, témoin de
  permutation sensible à une fuite générique) ;
- gardes d'identité et d'intégrité en mode décisif (cas sain et artefacts).
Lancement : python -m pytest -q echelle-v2/tests
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


AN = charger("analyser_echelle_v2")
N_BOOT_ESSAI = 300  # les intégrations courent avec 300 tirages ; le run décisif en a 2 000
PETITS = {"petit": {"modele": "essai/petit", "revision": "r-petit", "couches": [4, 6], "dimension": 64},
          "grand": {"modele": "essai/grand", "revision": "r-grand", "couches": [4, 6], "dimension": 64}}


@pytest.fixture(scope="module")
def stimuli(tmp_path_factory):
    d = tmp_path_factory.mktemp("stim") / "s"
    subprocess.run([sys.executable, "-I", "-B", str(SCRIPTS / "construire_echelle_v2.py"), str(d)], check=True,
                   capture_output=True)
    return d / "echelle-v2.json"


@pytest.fixture(autouse=True)
def tirages_reduits(monkeypatch):
    monkeypatch.setattr(AN, "N_BOOT", N_BOOT_ESSAI)
    monkeypatch.setattr(AN, "ATTENDUS", PETITS)


def sha(p):
    return hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()


def sceller(f):
    f = pathlib.Path(f)
    (f.parent / (f.name + ".sha256")).write_text(f"{sha(f)}  {f.name}\n", encoding="utf-8")


def fabriquer(dossier, stimuli, alpha, graine, nom="petit", force_c=4.0, beta=0.0, tau=0.15, translation=0.0,
              d=64, couches=(4, 6), **manifeste):
    """x = contenu + s_f·F + s_c·C + cadrage + bruit (+ translation), F = alpha·C + F⊥ + beta·(fuite générique sur les
    particularités des paires du jeu a). La couche 4 porte un contexte deux fois plus faible. λ vrai ≈ alpha."""
    doc = json.loads(pathlib.Path(stimuli).read_text(encoding="utf-8"))
    st = doc["stimuli"]
    rng = np.random.default_rng(graine)
    base = np.linalg.qr(rng.normal(size=(d, 4)))[0].T
    C, Fp = base[0] * force_c, base[2] * 2.0
    contenus = rng.normal(size=(64, d))
    cadrage = {}
    for s in st:
        cle = (s["jeu"], s["paire"], s["classe"])
        if cle not in cadrage:
            cadrage[cle] = rng.normal(size=d) * tau
    signes = rng.choice([-1.0, 1.0], size=6)
    gen = sum(signes[j] * (cadrage[("a", j, "eval")] - cadrage[("a", j, "reel")]) for j in range(6))
    gen = gen / np.linalg.norm(gen) * force_c if np.linalg.norm(gen) > 0 else gen
    decal = rng.normal(size=d)
    decal = decal / np.linalg.norm(decal) * translation
    dossier = pathlib.Path(dossier)
    dossier.mkdir(parents=True)
    ids, sorties = [s["id"] for s in st], {}
    bruit = rng.normal(size=(len(st), d))
    for k, c in enumerate(couches):
        ech = 0.5 if k == 0 else 1.0
        F = alpha * C * ech + Fp + beta * gen
        X = np.empty((len(st), d))
        for i, s in enumerate(st):
            sf = 0.5 if s["format"] == "qcm" else -0.5
            sc = 0.5 if s["classe"] == "eval" else -0.5
            X[i] = contenus[s["contenu"]] + sf * F + sc * C * ech + cadrage[(s["jeu"], s["paire"], s["classe"])] \
                + bruit[i] + decal
        f = dossier / f"activations-L{c}.npy"
        np.save(f, X.astype(np.float16))
        sceller(f)
        sorties[f.name] = sha(f)
    f_ids = dossier / "ids.json"
    f_ids.write_text(json.dumps(ids) + "\n", encoding="utf-8")
    sceller(f_ids)
    sorties["ids.json"] = sha(f_ids)
    m = {"modele": PETITS[nom]["modele"], "revision": PETITS[nom]["revision"], "couches": list(couches), "dimension": d,
         "type_nombre": "bfloat16", "limite": None, "sha256_stimuli": sha(stimuli), "rendu_premier": "<gabarit>",
         "dernier_jeton": "<fin>", "sha256_sorties": sorties}
    m.update(manifeste)
    (dossier / "manifeste-mesure.json").write_text(json.dumps(m), encoding="utf-8")
    sceller(dossier / "manifeste-mesure.json")
    return dossier


def analyser(tmp_path, stimuli, petit, grand, nom="sortie", repetition=False):
    sortie = tmp_path / nom
    args = [str(stimuli), str(petit), str(grand), "12345", str(sortie)] + (["--repetition"] if repetition else [])
    code = AN.principal(args)
    lu = json.loads((sortie / "analyse-echelle-v2.json").read_text(encoding="utf-8")) if code == 0 else None
    return code, lu


# ---------- lecture mécanique (CLX-01, CLX-04, CLX-10) ----------

def r_fictif(lp, lg, dl, sp=(0.1, 0.5), cert=(0.8, 0.8)):
    return {"petit": {"A_ctx_fixe_ic": [cert[0], 0.95], "lambda_ic": list(lp)},
            "grand": {"A_ctx_fixe_ic": [cert[1], 0.95], "lambda_ic": list(lg)},
            "delta_lambda_ic": list(dl), "specificite_ic": list(sp)}


@pytest.mark.parametrize("lp, lg, dl, sp, cert, attendu, reserve", [
    ((0.7, 1.1), (0.0, 0.2), (0.5, 1.0), (0.1, 0.6), (0.8, 0.8), "positif", False),
    ((0.7, 1.1), (0.0, 0.2), (0.5, 1.0), (-0.1, 0.6), (0.8, 0.8), "positif", True),
    ((1.6, 2.1), (1.0, 1.3), (0.4, 0.9), (0.1, 0.6), (0.8, 0.8), "indécis", False),      # λ(grand) ≥ 1 : refusé
    ((-1.1, -0.9), (-1.0, -0.85), (-0.2, 0.2), (0, 1), (0.8, 0.8), "fuite de signe inverse", False),  # CLX-01 (a)
    ((-0.1, 0.1), (-0.65, -0.5), (0.47, 0.64), (0, 1), (0.8, 0.8), "fuite de signe inverse", False),  # CLX-01 (b)
    ((-0.7, -0.5), (-0.1, 0.1), (-0.69, -0.52), (0, 1), (0.8, 0.8), "fuite de signe inverse", False),  # CLX-01 (c)
    ((0.0, 0.2), (0.7, 0.9), (-0.9, -0.5), (-0.6, -0.1), (0.8, 0.8), "inverse", False),
    ((0.0, 0.2), (0.7, 0.9), (-0.9, -0.5), (-0.6, 0.1), (0.8, 0.8), "inverse", True),
    ((-0.1, 0.2), (-0.2, 0.2), (-0.2, 0.3), (0, 1), (0.8, 0.8), "pas de fuite", False),
    ((0.3, 0.6), (0.35, 0.6), (-0.2, 0.2), (0, 1), (0.8, 0.8), "nul", False),
    ((0.3, 0.9), (0.1, 0.6), (-0.1, 0.6), (0, 1), (0.8, 0.8), "indécis", False),
    ((0.7, 1.1), (0.0, 0.2), (0.5, 1.0), (0.1, 0.6), (0.6, 0.65), "non certifiable", False),
    ((0.7, 1.1), (0.0, 0.2), (0.5, 1.0), (0.1, 0.6), (0.6, 0.8), "certification asymétrique (grand seulement)", False),
    ((0.7, 1.1), (0.0, 0.2), (0.5, 1.0), (0.1, 0.6), (0.8, 0.6), "certification asymétrique (petit seulement)", False),
])
def test_lire(lp, lg, dl, sp, cert, attendu, reserve):
    lecture, reserves = AN.lire(r_fictif(lp, lg, dl, sp, cert))
    assert lecture == attendu and bool(reserves) == reserve


def test_aire_ponderee_egale_aire_dupliquee():
    rng = np.random.default_rng(0)
    pos, neg = rng.normal(size=7).round(1), rng.normal(size=9).round(1)
    wp, wn = rng.integers(0, 3, size=7).astype(float), rng.integers(1, 3, size=9).astype(float)
    dup_p, dup_n = np.repeat(pos, wp.astype(int)), np.repeat(neg, wn.astype(int))
    attendu = np.mean([(a > b) + 0.5 * (a == b) for a in dup_p for b in dup_n])
    assert AN.auroc_pondere(pos, wp, neg, wn) == pytest.approx(attendu)


def test_intervalle_non_fini():
    with pytest.raises(AN.Arret):
        AN.intervalle([0.1, float("nan")])


def test_partitions():
    assert len(AN.PARTITIONS) == 10 and all(sum(p) == 0 and p[0] == 1 for p in AN.PARTITIONS)


# ---------- intégration sur activations synthétiques ----------

def test_positif(tmp_path, stimuli):
    code, r = analyser(tmp_path, stimuli, fabriquer(tmp_path / "p", stimuli, 1.0, 1),
                       fabriquer(tmp_path / "g", stimuli, 0.1, 2, nom="grand"))
    assert code == 0 and r["lecture"] == "positif" and r["reserves"] == []
    assert r["petit"]["lambda"] == pytest.approx(1.0, abs=0.25) and r["grand"]["lambda"] == pytest.approx(0.1, abs=0.25)
    assert r["petit"]["couche"] == 6 and r["grand"]["couche"] == 6
    assert r["petit"]["A_ctx_fixe"] == pytest.approx(r["petit"]["A_ctx"])  # au point, direction fixe = réapprise


def test_nul_strict(tmp_path, stimuli):
    code, r = analyser(tmp_path, stimuli, fabriquer(tmp_path / "p", stimuli, 0.5, 3, tau=0.05),
                       fabriquer(tmp_path / "g", stimuli, 0.5, 4, nom="grand", tau=0.05))
    assert code == 0 and r["lecture"] == "nul"


def test_invariance_par_translation(tmp_path, stimuli):
    """CLX-02 : une translation de toutes les activations ne change ni les aires, ni λ, ni la lecture."""
    a = analyser(tmp_path, stimuli, fabriquer(tmp_path / "p0", stimuli, 0.6, 5),
                 fabriquer(tmp_path / "g0", stimuli, 0.2, 6, nom="grand"), nom="s0")[1]
    b = analyser(tmp_path, stimuli, fabriquer(tmp_path / "p1", stimuli, 0.6, 5, translation=60.0),
                 fabriquer(tmp_path / "g1", stimuli, 0.2, 6, nom="grand", translation=60.0), nom="s1")[1]
    for nom in ("petit", "grand"):
        for k in ("A_ctx_fixe", "A_ctx", "A_conf", "lambda"):
            assert b[nom][k] == pytest.approx(a[nom][k], abs=0.02), (nom, k)
    assert a["lecture"] == b["lecture"]


def test_temoin_de_permutation_sensible(tmp_path, stimuli):
    """CLX-04 : une fuite générique (sur les particularités des paires) fait monter ν ; sans elle, ν reste bas."""
    r0 = analyser(tmp_path, stimuli, fabriquer(tmp_path / "p0", stimuli, 1.0, 7),
                  fabriquer(tmp_path / "g0", stimuli, 0.1, 8, nom="grand"), nom="s0")[1]
    r1 = analyser(tmp_path, stimuli, fabriquer(tmp_path / "p1", stimuli, 1.0, 7, beta=3.0),
                  fabriquer(tmp_path / "g1", stimuli, 0.1, 8, nom="grand"), nom="s1")[1]
    assert r1["petit"]["nu"] > r0["petit"]["nu"] + 0.3
    assert r1["specificite"] < r0["specificite"]


# ---------- gardes d'identité et d'intégrité (mode décisif) ----------

def paire_saine(tmp_path, stimuli, **kw):
    return fabriquer(tmp_path / "p", stimuli, 1.0, 21, **kw), fabriquer(tmp_path / "g", stimuli, 0.1, 22, nom="grand")


def test_decisif_sain(tmp_path, stimuli):
    code, r = analyser(tmp_path, stimuli, *paire_saine(tmp_path, stimuli))
    assert code == 0 and not r["repetition"] and r["numpy"] and r["python"]


def test_artefact_dossiers_inverses(tmp_path, stimuli):
    p, g = paire_saine(tmp_path, stimuli)
    assert analyser(tmp_path, stimuli, g, p)[0] == 1


def test_artefact_autres_stimuli(tmp_path, stimuli):
    p, g = paire_saine(tmp_path, stimuli, sha256_stimuli="0" * 64)
    assert analyser(tmp_path, stimuli, p, g)[0] == 1


def test_artefact_mesure_limitee(tmp_path, stimuli):
    p, g = paire_saine(tmp_path, stimuli, limite=100)
    assert analyser(tmp_path, stimuli, p, g)[0] == 1


def test_artefact_gabarit_different(tmp_path, stimuli):
    p, g = paire_saine(tmp_path, stimuli, rendu_premier="<autre gabarit>")
    assert analyser(tmp_path, stimuli, p, g)[0] == 1


def test_artefact_type_nombre(tmp_path, stimuli):
    p, g = paire_saine(tmp_path, stimuli, type_nombre="float32")
    assert analyser(tmp_path, stimuli, p, g)[0] == 1


def test_artefact_ordre(tmp_path, stimuli):
    p, g = paire_saine(tmp_path, stimuli)
    ids = json.loads((p / "ids.json").read_text())
    ids[0], ids[1] = ids[1], ids[0]
    (p / "ids.json").write_text(json.dumps(ids) + "\n")
    sceller(p / "ids.json")
    assert analyser(tmp_path, stimuli, p, g)[0] == 1  # empreinte d'ids ≠ manifeste


def test_artefact_compagnon_absent(tmp_path, stimuli):
    p, g = paire_saine(tmp_path, stimuli)
    (p / "activations-L6.npy.sha256").unlink()
    assert analyser(tmp_path, stimuli, p, g)[0] == 1


def test_artefact_empreinte(tmp_path, stimuli):
    p, g = paire_saine(tmp_path, stimuli)
    X = np.load(p / "activations-L6.npy")
    X[0, 0] += 1
    np.save(p / "activations-L6.npy", X)
    assert analyser(tmp_path, stimuli, p, g)[0] == 1


def resceller_activations(p, X, nom="activations-L6.npy"):
    np.save(p / nom, X)
    sceller(p / nom)
    m = json.loads((p / "manifeste-mesure.json").read_text())
    m["sha256_sorties"][nom] = sha(p / nom)
    (p / "manifeste-mesure.json").write_text(json.dumps(m))
    sceller(p / "manifeste-mesure.json")


def test_artefact_non_fini(tmp_path, stimuli):
    p, g = paire_saine(tmp_path, stimuli)
    X = np.load(p / "activations-L6.npy")
    X[3, 2] = np.nan
    resceller_activations(p, X)
    assert analyser(tmp_path, stimuli, p, g)[0] == 1


def test_artefact_forme(tmp_path, stimuli):
    p, g = paire_saine(tmp_path, stimuli)
    resceller_activations(p, np.load(p / "activations-L6.npy")[:-1])
    assert analyser(tmp_path, stimuli, p, g)[0] == 1


def test_sortie_presente(tmp_path, stimuli):
    (tmp_path / "sortie").mkdir()
    assert AN.principal([str(stimuli), "x", "y", "1", str(tmp_path / "sortie")]) == 2


def test_repetition_marquee(tmp_path, stimuli):
    p = fabriquer(tmp_path / "p", stimuli, 1.0, 31, modele="autre", revision=None)
    g = fabriquer(tmp_path / "g", stimuli, 0.1, 32, nom="grand", modele="autre", revision=None)
    assert analyser(tmp_path, stimuli, p, g, nom="d")[0] == 1          # décisif : identité refusée
    code, r = analyser(tmp_path, stimuli, p, g, nom="r", repetition=True)
    assert code == 0 and r["repetition"] and r["lecture"].startswith("répétition, non décisive")


def test_tirage_paires_a_conditionne():
    """Un tirage des paires du jeu a qui ne garde qu'une paire rend le témoin indéfini : il est rejeté et compté."""

    class Rng:
        def __init__(self):
            self.n = 0
            self.vrai = np.random.default_rng(0)

        def choice(self, *a, **k):
            return self.vrai.choice(*a, **k)

        def integers(self, lo, hi, size):
            self.n += 1
            return np.zeros(size, dtype=int) if self.n == 1 else self.vrai.integers(lo, hi, size=size)

    AN.REJETS["tirages_paires_a_rejetes"] = 0
    moities = (np.arange(0, 24), np.arange(24, 48))
    wc, wp = AN.tirer(Rng(), moities)
    assert (wp["a"] > 0).sum() >= 2 and AN.REJETS["tirages_paires_a_rejetes"] == 1
    rng = np.random.default_rng(1)
    assert all((AN.tirer(rng, moities)[1]["a"] > 0).sum() >= 2 for _ in range(20000))
