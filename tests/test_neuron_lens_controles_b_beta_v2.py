"""Essais de `controles_b_beta_v2` : cas sain et artefact de chaque garde constatée sur la machine (texte gelé de la tranche, P.4,
« Branches des gardes », et « gardes du montage » de la commande)."""
import math

import numpy as np
import pytest

from controle_ia.neuron_lens import controles_b_beta_v2 as c


# ---------------------------------------------------------------- P.1 et rows_sha256

def _rows_factices(n=932, longueur=128, decalage=0):
    return [[128000] + [(i * 7 + j + decalage) % 128000 for j in range(longueur - 1)] for i in range(n)]


def test_rows_sha256_forme_drowse():
    assert c.rows_sha256([[1, 2], [3]]) == c.sha256_octets(repr([[1, 2], [3]]).encode())


def test_p1_artefacts():
    rel, pb = c.controle_p1(_rows_factices())
    assert rel["docs"] == 932 and rel["moities"] == [466, 466] and rel["longueurs"] == [128]
    assert any("rows_sha256" in p for p in pb)  # lignes factices : empreinte différente (artefact « altéré »)
    _, pb931 = c.controle_p1(_rows_factices(931))
    assert any("931 documents" in p for p in pb931) and any("moitiés" in p for p in pb931)
    _, pbl = c.controle_p1(_rows_factices()[:-1] + [[1] * 127])
    assert any("longueurs" in p for p in pbl)


def test_p1_sain_par_constantes(monkeypatch):
    rows = _rows_factices()
    monkeypatch.setattr(c, "ROWS_SHA256", c.rows_sha256(rows))
    monkeypatch.setattr(c, "ROWS_SHA256_MOITIES", (c.rows_sha256(rows[0::2]), c.rows_sha256(rows[1::2])))
    assert c.controle_p1(rows)[1] == []
    altere = [list(r) for r in rows]
    altere[5][3] += 1  # un jeton altéré : l'empreinte change
    assert any("rows_sha256" in p for p in c.controle_p1(altere)[1])


# ---------------------------------------------------------------- banc

@pytest.mark.parametrize("s,att", [(11.5, "part"), (14.2, "part"), (15.0, "compte_rendu"), (23.6, "compte_rendu"), (24.0, "arret"),
                                   (float("nan"), "arret"), (0, "arret"), (True, "arret"), (None, "arret")])
def test_banc(s, att):
    assert c.regle_banc(s) == att


# ---------------------------------------------------------------- (d)

def test_garde_d():
    sain = {"a": {"code": 0, "resume": "7 passed in 6.98s"}, "fumee": {"code": 0}}
    assert c.garde_d(sain) == []
    assert c.garde_d({"a": {"code": 0, "resume": "6 passed, 1 skipped in 2s"}})
    assert c.garde_d({"a": {"code": 1, "resume": "1 failed, 6 passed"}})
    assert c.garde_d({"a": {"code": 0, "resume": "no tests ran"}})
    assert c.garde_d({"fumee": {"code": 2}})
    assert c.garde_d({})


# ---------------------------------------------------------------- (e), (n)

def test_garde_e():
    rng = np.random.default_rng(0)
    lent = {l: rng.normal(size=(4, 4)).astype(np.float32) for l in range(31)}
    assert c.garde_e_matrices(lent, "x") == []
    lent[10] = np.eye(4, dtype=np.float32) + 1e-7
    assert c.garde_e_matrices(lent, "x") == ["(e) x : matrice de la couche 10 égale à l'identité"]
    del lent[3]
    assert any("couche 3 absente" in p for p in c.garde_e_matrices(lent, "x"))
    lent2 = {l: np.eye(4, dtype=np.float32) for l in range(28, 31)} | {l: rng.normal(size=(4, 4)) for l in range(28)}
    assert c.garde_e_matrices(lent2, "x") == []  # identité aux couches 28 à 30 : hors de la garde


def test_garde_n():
    rng = np.random.default_rng(1)
    a = {l: rng.normal(size=(3, 3)).astype(np.float32) for l in range(31)}
    b = {l: rng.normal(size=(3, 3)).astype(np.float32) for l in range(31)}
    assert c.garde_n(a, b, "1", "2") == []
    b[7] = a[7].copy()
    assert c.garde_n(a, b, "1", "2") == ["(n) matrice de notre R égale à celle de la lentille R publique, couche 7"]
    assert any("empreinte égale" in p for p in c.garde_n(a, a | {7: b[7] + 1}, "h", "h"))


# ---------------------------------------------------------------- (g), split_half

def _sommes(seed=0, L=3, d=4, egales=False):
    rng = np.random.default_rng(seed)
    a = rng.normal(size=(L, d, d)).astype(np.float32)
    b = a.copy() if egales else rng.normal(size=(L, d, d)).astype(np.float32)
    return a, b


def test_split_half_recopie_du_depot():
    a, b = _sommes()
    v = c.split_half(a, b, 466, 466)
    l = 1
    att = np.linalg.norm(a[l] / 466 - b[l] / 466) / np.linalg.norm((a[l] + b[l]) / 932)
    assert math.isclose(v[l], float(att), rel_tol=1e-5)
    assert c.split_half(*_sommes(egales=True), 466, 466) == [0.0, 0.0, 0.0]
    assert all(math.isnan(x) for x in c.split_half(a, b, 0, 466))


META_SAINE = {"lens": "R", "docs": 932, "rows_sha256": c.ROWS_SHA256, "full_length": True, "model": c.MODELE}


def test_garde_g():
    sain = dict(meta=META_SAINE, next_doc=932, n_docs=[466, 466], longueurs=[128] * 932, diffs={"out": [0.05] * 31},
                matrices_finies=True, lentille="R")
    assert c.garde_g_fit(**sain) == []
    for modif, motif in ((dict(diffs={"out": [0.05] * 30 + [float("nan")]}), "non finie"),
                         (dict(matrices_finies=False), "non finie"),
                         (dict(meta=META_SAINE | {"full_length": False}), "full_length"),
                         (dict(longueurs=[128] * 931 + [127]), "longueurs"),
                         (dict(n_docs=[465, 467]), "par moitié"),
                         (dict(next_doc=400), "next_doc"),
                         (dict(meta=META_SAINE | {"rows_sha256": "0" * 64}), "rows_sha256"),
                         (dict(lentille="S"), "lentille")):
        pb = c.garde_g_fit(**(sain | modif))
        assert any(motif in p for p in pb), (modif, pb)


def test_garde_h():
    assert c.garde_h({"out": 31, "mid": 32}, "R") == []
    assert c.garde_h({"mid": 32, "out": 32}, "S") == []
    assert c.garde_h({"mid": 31, "out": 32}, "S") == ["(h) S, cible mid : 31 couches au lieu de 32"]
    assert c.garde_h_export(range(31)) == []
    assert c.garde_h_export(range(30))


# ---------------------------------------------------------------- (i)

PUB_AJ = {"repo": c.REPO_DCLM, "revision": c.REVISION_DCLM, "file": "dclm.jsonl", "rows": [0, 1000],
          "ids": [f"a{i}" for i in range(1000)]}
PUB_ACT = {"repo": c.REPO_DCLM, "config": None, "split": "train", "revision": c.REVISION_DCLM, "file": "act-dclm.jsonl",
           "skip": 1000, "n": 40000, "ids": [f"b{i}" for i in range(40000)]}


def test_garde_i():
    assert c.garde_i(dict(PUB_AJ), None, PUB_AJ, PUB_ACT) == []
    assert c.garde_i(dict(PUB_AJ), dict(PUB_ACT), PUB_AJ, PUB_ACT, ["x", "y"], ["z"]) == []
    autre_rev = dict(PUB_AJ, revision="f" * 40)
    assert c.garde_i(autre_rev, None, PUB_AJ, PUB_ACT)
    permute = dict(PUB_AJ, ids=["a1", "a0"] + PUB_AJ["ids"][2:])
    assert c.garde_i(permute, None, PUB_AJ, PUB_ACT)
    assert c.garde_i(dict(PUB_AJ), dict(PUB_ACT, skip=999), PUB_AJ, PUB_ACT)
    assert c.garde_i(dict(PUB_AJ), dict(PUB_ACT), PUB_AJ, PUB_ACT, ["texte commun", "y"], ["texte commun"])
    commun = dict(PUB_ACT, ids=["a3"] + PUB_ACT["ids"][1:])
    assert any("identifiant" in p for p in c.garde_i(dict(PUB_AJ), commun, PUB_AJ, commun))


# ---------------------------------------------------------------- (k)

def test_garde_k():
    assert c.garde_k(("hub", "hub"), "hub") == []
    noms = (c.FIT_NOMS_ARCH["R"][:-3], c.FIT_NOMS_ARCH["S"][:-3])
    assert c.garde_k(noms, "hub")  # nos noms avant la passe d'activations
    assert c.garde_k(noms, "noms", {"R": "1", "S": "2"}, {"R": "1", "S": "2"}) == []
    assert c.garde_k(("hub", "hub"), "noms", {"R": "1", "S": "2"}, {"R": "1", "S": "2"})  # cas (viii)
    assert c.garde_k(noms, "noms", {"R": "1", "S": "3"}, {"R": "1", "S": "2"})
    with pytest.raises(ValueError):
        c.garde_k(noms, "autre")
    assert c.message_hub_present("12:00:00 " + c.MOTIF_HUB)
    assert not c.message_hub_present("rien")


# ---------------------------------------------------------------- (o)

def test_garde_o():
    rng = np.random.default_rng(2)
    moy = {l: rng.normal(size=(4, 4)) for l in range(31)}
    assert c.garde_o({l: m.astype(np.float32) for l, m in moy.items()}, moy, "R:x") == []
    trou = dict(moy)
    trou[12] = None
    assert c.garde_o(trou, moy, "R:x") == ["(o) R:x : None à la couche 12"]
    loin = dict(moy)
    loin[5] = moy[5] * 1.01
    assert any("couche 5" in p for p in c.garde_o(loin, moy, "R:x"))
    assert c.garde_o(None, moy, "R:x", erreur="FileNotFoundError: no R-lens")


# ---------------------------------------------------------------- (p), (q), (r), (s)

def test_gardes_p_q_r_s():
    assert c.garde_p_measure({"contexts": 16}) == [] and c.garde_p_measure({"contexts": 15})
    assert c.garde_p_pilotes({"dclm": 4, "code": 2, "chat": 2}) == []
    assert c.garde_p_pilotes({"dclm": 3, "code": 2, "chat": 2})
    assert c.garde_q_avant([]) == [] and c.garde_q_avant([c.FIT_NOMS["R"]])
    assert c.garde_q_relance(META_SAINE, "R") == []
    assert c.garde_q_relance(META_SAINE | {"rows_sha256": "b" + c.ROWS_SHA256[1:]}, "R")
    assert c.garde_q_relance(META_SAINE, "S")
    k = list(range(100))
    h = c.empreinte_liste_gardee(k)
    assert c.garde_r(h, h, "lens_compare.py") == []
    assert c.garde_r(c.empreinte_liste_gardee(k[:-1] + [1000]), h, "lens_compare.py")
    assert c.garde_s([]) == [] and c.garde_s([f"data/checks/reads_at_firings-{c.STEM}.pt"])


# ---------------------------------------------------------------- audits A2, A3, A4

def test_controles_a2_a3():
    sain = dict(n_docs={"R": [466, 466], "S": [466, 466]}, empreintes_moities=list(c.ROWS_SHA256_MOITIES),
                ecarts_sommes={"R|out": 0.3, "R|mid": 0.2, "S|mid": 0.1, "S|out": 0.1},
                matrices_moities={l: (f"p{l}", f"i{l}") for l in range(31)})
    assert c.controles_a2_a3(**sain) == (True, [])
    assert c.controles_a2_a3(**sain, longueurs=[128] * 932, full_length=True, avec_a3=True) == (True, [])
    assert not c.controles_a2_a3(**(sain | {"ecarts_sommes": {"R|out": 0.0}}))[0]  # (vi-d) : sommes égales
    assert not c.controles_a2_a3(**(sain | {"n_docs": {"R": [465, 467]}}))[0]
    egales = {l: (f"p{l}", f"i{l}") for l in range(31)} | {4: ("x", "x")}
    assert not c.controles_a2_a3(**(sain | {"matrices_moities": egales}))[0]  # M-1 : mêmes matrices sous d'autres noms
    assert not c.controles_a2_a3(**(sain | {"matrices_moities": {l: ("a", "b") for l in range(30)}}))[0]
    assert not c.controles_a2_a3(**sain, longueurs=[127] + [128] * 931, full_length=True, avec_a3=True)[0]


def test_points_fixes_et_a4():
    pytest.importorskip("torch")
    pf = c.points_fixes_permutation(f=64, couches=3)
    assert len(pf) == 3 and all(0 <= x <= 128 for x in pf)
    assert c.points_fixes_permutation(f=64, couches=3) == pf  # déterministe
    assert c.controle_a4([2] * 32, "s", "s") == {"permutation_ok": True, "lentille_S_ok": True}
    assert c.controle_a4([2] * 31 + [11], "s", "s")["permutation_ok"] is False  # dégénérée
    assert c.controle_a4([28672] * 32, "s", "t") == {"permutation_ok": False, "lentille_S_ok": False}  # identité


# ---------------------------------------------------------------- intervalles

def _poles(seed=0):
    rng = np.random.default_rng(seed)
    out = []
    for l in range(32):
        for k in range(64):
            lect = {}
            for cible in ("steer 1x", "ablate win"):
                lect[cible] = {s: ({"r": float(rng.uniform(-1, 1)), "motif": "retenu"} if k % 9 else {"motif": "effet nul"})
                               for s in ("R:dclm-llama", "logit", "J", "npJpp", "npR")}
            out.append({"couche": l, "aleatoire": k < 60, "lectures": lect})
    return out


def test_intervalles_deterministes_et_ordonnes():
    gens = lambda: {t: np.random.default_rng(i) for i, t in enumerate(c.TACHES_INTERVALLES)}
    a, b = c.intervalles(_poles(), gens(), 200), c.intervalles(_poles(), gens(), 200)
    assert a == b
    assert set(a) == {"n_tirages", *c.TACHES_INTERVALLES}
    iv = a["b-beta-intervalles-B-2"]["steer 1x|R:dclm-llama"][5]
    assert iv[0] <= iv[1]
    assert set(a["b-beta-intervalles-B-4"]) == {"steer 1x|R:dclm-llama−J", "steer 1x|R:dclm-llama−npJpp"}


# ---------------------------------------------------------------- assemblage

def test_gardes_booleennes():
    pb = {g: [] for g in c.GARDES_MACHINE + ("identite",)}
    out = c.gardes_booleennes(pb | {"k": ["(k) x"]})
    assert out["k"] is True and out["d"] is False and all(type(v) is bool for v in out.values())
    with pytest.raises(ValueError):
        c.gardes_booleennes({"d": []})


def test_lectures_de_sorties():
    sortie = {"neurons": {"layers": [{"layer": l, "read_S": 0.1 * (l == 0), "silent": 0.0} for l in range(32)]}}
    rs, si = c.reads_depuis_sortie(sortie)
    assert len(rs) == 32 and rs[0] == 0.1
    with pytest.raises(ValueError):
        c.reads_depuis_sortie({"neurons": {"layers": sortie["neurons"]["layers"][:31]}})
    lc = {"layers": {str(l): {"R:dclm-llama-even vs R:dclm-llama-odd": {"top1_agree": 0.9, "rows": 28672}} for l in (2, 7, 12, 18, 23, 28)}}
    assert c.accord_depuis_lens_compare(lc) == {l: 0.9 for l in (2, 7, 12, 18, 23, 28)}
    lc["layers"]["12"]["R:dclm-llama-even vs R:dclm-llama-odd"]["rows"] = 14336  # m-12
    with pytest.raises(ValueError):
        c.accord_depuis_lens_compare(lc)


def test_valeurs_versees_et_empreinte_matrice():
    rng = np.random.default_rng(3)
    lent = {l: rng.normal(size=(3, 3)).astype(np.float32) for l in range(28)}
    lent[2] = np.eye(3, dtype=np.float32)
    e = c.ecarts_identite(lent)
    assert e[2] == 0.0 and e[3] > 0
    assert c.ecarts_npr(lent, lent)[5] == 0.0
    m = {l: lent.get(l, np.ones((3, 3))) for l in range(31)}
    r = c.ecarts_aller_retour(m, m)
    assert all(v == 0.0 for v in r.values()) and len(r) == 31
    a = rng.normal(size=(4, 4)).astype(np.float32)
    assert c.empreinte_matrice(a) == c.empreinte_matrice(a.copy()) != c.empreinte_matrice(a + 1)


def test_jeton_de_debut_et_pilotes():
    comptes = np.zeros(128256, dtype=np.int64)
    comptes[128000], comptes[5], comptes[6], comptes[7] = 40, 100, 40, 3
    j = c.jeton_de_debut(comptes, [5, 6, 7, 128000])
    assert j["compte"] == 40 and j["garde"] is True and j["rang_par_compte"] == 2  # égalité avec 6 : 1 + un seul plus grand
    assert c.jeton_de_debut(comptes, [5, 6])["rang_par_compte"] is None
    tables = [f"data/catalog/llama/neurons/drivers/L{l:02d}.parquet" for l in range(32)] + ["data/catalog/llama/heads/drivers.parquet"]
    assert c.tables_pilotes(tables) == []
    assert c.tables_pilotes(tables[1:]) == ["table des pilotes absente : couche 0"]
    assert c.tables_pilotes(tables[:-1]) == ["table des pilotes des têtes absente"]
