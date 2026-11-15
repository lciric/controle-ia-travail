"""Essais de `controle_ia.neuron_lens.grandeurs_b_alpha_v1` (R5 : cas sain et artefacts), sans modèle ni réseau ni code voisin."""
import json

import numpy as np
import pytest
import torch

from controle_ia.neuron_lens import grandeurs_b_alpha_v1 as g
from controle_ia.neuron_lens.verdicts_b_alpha_v3 import CIBLES, N_COUCHES, random_neurons

F, NV, V, K = 40, 45, 50, 8
SPECS = ("logit", "npR")


def faux_causal(seed=0, meta_seed=None):
    gen = torch.Generator().manual_seed(7 + seed)
    picks = random_neurons(N_COUCHES, F, 32, seed)
    P = len(picks)
    steer = torch.randn(P, 2, 2, V, generator=gen).half()
    ablate_pos = torch.randn(P, 2, V, generator=gen).half()
    ablate_win = torch.randn(P, 2, V, generator=gen).half()
    fired = (torch.rand(P, 2, K, generator=gen) + 0.1)
    fired[3, 1] = 0  # pôle sans contexte
    ablate_pos[3, 1] = 0
    ablate_win[3, 1] = 0
    steer[5, 0, 0] = 0  # pilotage 1× sans effet
    ablate_win[9, 0, :NV] = 0  # ablation sans effet sur les nv lignes (effet hors du tokeniseur seulement)
    meta = {"per_layer": 32, "doses": [1.0, 4.0]} | ({"seed": meta_seed} if meta_seed else {})
    return {"meta": meta, "picks": picks, "steer": steer, "ablate_pos": ablate_pos, "ablate_win": ablate_win, "fired": fired,
            "alpha": torch.rand(P, 2, generator=gen) * 3, "top_doc": torch.randint(0, 100, (P, 2, K), generator=gen),
            "top_pos": torch.randint(0, 60, (P, 2, K), generator=gen).short(), "contexts": torch.zeros(1)}


def faux_lire():
    gen = torch.Generator().manual_seed(11)
    W = {s: torch.randn(N_COUCHES, F, NV, generator=gen) for s in SPECS}
    return lambda layer, neurones, s: W[s][layer, neurones]


KEEP = torch.ones(NV, dtype=torch.bool)
KEEP[[0, 7, 30]] = False


@pytest.fixture(scope="module")
def res():
    return g.grandeurs(faux_causal(), faux_lire(), SPECS, NV, KEEP, F)


def table_depuis_poles(res):
    """Agrégation indépendante, depuis les seuls enregistrements par pôle versés (r arrondis à 10⁻⁶)."""
    out = {}
    for c in CIBLES:
        out[c] = {}
        for s in SPECS:
            thr = res["centile_temoin"][f"{c}|{s}"]
            t = {"layer": [], "pass_threshold": round(thr, 4)}
            for l in range(N_COUCHES):
                ps = [p["lectures"][c][s] for p in res["poles"] if p["couche"] == l and p["aleatoire"]
                      and p["lectures"][c][s]["motif"] == g.RETENU]
                r = torch.tensor([p["r"] for p in ps])
                rc = torch.tensor([p["r_temoin"] for p in ps])
                ov = torch.tensor([p["overlap"] for p in ps])
                t["layer"].append(l)
                for key, v in (("r_q25", r.quantile(0.25)), ("r_med", r.median()), ("r_q75", r.quantile(0.75)),
                               ("control_med", rc.median()), ("overlap", ov.mean()), ("pass", (r > thr).float().mean()),
                               ("pass_control", (rc > thr).float().mean())):
                    t.setdefault(key, []).append(round(v.item(), 4))
            out[c][s] = t
    return out


def test_sain_table_et_poles(res):
    assert len(res["poles"]) == 2 * 32 * N_COUCHES
    assert g.comparer_a_score(res["table"], {"targets": table_depuis_poles(res)}) == []
    assert res["seed"] == 0 and res["nv"] == NV and set(res["centile_temoin"]) == {f"{c}|{s}" for c in CIBLES for s in SPECS}


def test_pearson_overlap_contre_numpy():
    gen = torch.Generator().manual_seed(3)
    x, y = torch.randn(4, 30, generator=gen), torch.randn(4, 30, generator=gen)
    attendu = [np.corrcoef(a, b)[0, 1] for a, b in zip(x.numpy(), y.numpy())]
    assert np.allclose(g.pearson(x, y).numpy(), attendu, atol=1e-6)
    a = torch.arange(20.0)[None]
    b = torch.cat([torch.arange(10.0) + 100, torch.arange(10.0)])[None]  # 10 premiers de b : indices 0-9 ; de a : 10-19
    assert g.overlap(a, b).tolist() == [0.0] and g.overlap(a, a).tolist() == [1.0]


def test_motifs(res):
    picks = faux_causal()["picks"]
    p = {(q["couche"], q["neurone"], q["signe"]): q for q in res["poles"]}
    def pole(i, signe):
        return p[(picks[i][0], picks[i][1], signe)]
    for s in SPECS:
        assert pole(3, -1)["lectures"]["ablate pos"][s] == {"motif": g.SANS_CONTEXTE}
        assert pole(3, -1)["lectures"]["ablate win"][s] == {"motif": g.SANS_CONTEXTE}
        assert pole(3, -1)["lectures"]["steer 1x"][s]["motif"] == g.RETENU
        assert pole(5, 1)["lectures"]["steer 1x"][s] == {"motif": g.EFFET_NUL}
        assert pole(5, 1)["lectures"]["steer 4x"][s]["motif"] == g.RETENU
        assert pole(9, 1)["lectures"]["ablate win"][s] == {"motif": g.EFFET_NUL}
    l3 = picks[3][0]
    assert res["n"]["ablate pos"][l3] == 63 and res["ecartes"]["ablate pos"]["sans contexte"][l3] == 1
    assert res["n"]["steer 1x"][picks[5][0]] == 63


def test_temoin_et_doses(res):
    picks = faux_causal()["picks"]
    saved = faux_causal()
    q = [x for x in res["poles"] if x["couche"] == 0 and x["signe"] == 1]
    neur = [n for l, n in picks if l == 0]
    assert [x["neurone"] for x in q] == neur
    assert [x["temoin"] for x in q] == [neur[-1]] + neur[:-1]  # le témoin : le tiré précédent de la couche (roll(1))
    a = saved["alpha"][0, 0].item()
    assert q[0]["doses"] == [round(a, 6), round(4 * a, 6)] and q[0]["top_doc"] == saved["top_doc"][0, 0].tolist()


@pytest.mark.parametrize("abime", ["valeur", "couche", "cle", "seuil", "lentille"])
def test_comparer_artefacts(res, abime):
    ref = json.loads(json.dumps(res["table"]))
    t = ref["steer 1x"]["npR"]
    if abime == "valeur":
        t["r_med"][12] = round(t["r_med"][12] + 2e-4, 4)
    elif abime == "couche":
        for key in ["layer", *g.CLES_STATS]:
            t[key] = t[key][:-1]
    elif abime == "cle":
        del t["pass_control"]
    elif abime == "seuil":
        t["pass_threshold"] += 1e-3
    else:
        del ref["ablate win"]["logit"]
    assert g.comparer_a_score(res["table"], {"targets": ref}) != []
    assert g.comparer_a_score(res["table"], {"targets": res["table"]}) == []
    assert g.comparer_a_score(res["table"], {}) == ["JSON de score sans « targets »"]


def test_ecrire(res, tmp_path):
    with pytest.raises(ValueError, match="fidélité"):
        g.ecrire(tmp_path / "x.json", res, "a" * 64, "b" * 64, ["écart"])
    assert not (tmp_path / "x.json").exists()
    g.ecrire(tmp_path / "x.json", res, "a" * 64, "b" * 64, [])
    lu = json.loads((tmp_path / "x.json").read_text(encoding="utf-8"))
    assert lu["causal_sha256"] == "a" * 64 and len(lu["poles"]) == len(res["poles"])
    assert g.empreinte_fichier(tmp_path / "x.json") == __import__("hashlib").sha256((tmp_path / "x.json").read_bytes()).hexdigest()


def test_gardes_d_entree():
    saved = faux_causal()
    with pytest.raises(ValueError, match="keep_vocab"):
        g.grandeurs(saved, faux_lire(), SPECS, NV, KEEP[:-1], F)
    with pytest.raises(ValueError, match="keep_vocab"):
        g.grandeurs(saved, faux_lire(), SPECS, NV, KEEP.int(), F)
    with pytest.raises(ValueError, match="lecture"):
        g.grandeurs(saved, lambda l, n, s: torch.zeros(len(n), NV + 1), SPECS, NV, KEEP, F)
    with pytest.raises(ValueError, match="lecture"):
        g.grandeurs(saved, lambda l, n, s: torch.full((len(n), NV), float("nan")), SPECS, NV, KEEP, F)
    double = dict(saved, picks=saved["picks"][:-1] + [saved["picks"][0]])
    with pytest.raises(ValueError, match="doublon"):
        g.grandeurs(double, faux_lire(), SPECS, NV, KEEP, F)


def test_graine_de_l_audit():
    """Cas sain : fichier tiré à la graine 1 et méta « seed: 1 » ; artefact : mêmes picks sans la graine dans la méta → refus."""
    r1 = g.grandeurs(faux_causal(seed=1, meta_seed=1), faux_lire(), SPECS, NV, KEEP, F)
    assert r1["seed"] == 1 and all(p["aleatoire"] for p in r1["poles"])
    with pytest.raises(ValueError):
        g.grandeurs(faux_causal(seed=1, meta_seed=None), faux_lire(), SPECS, NV, KEEP, F)
