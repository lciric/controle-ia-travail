"""Essais du chargeur des activations publiées (`controle_ia.narcbench.chargeur_externe_v1`) sur des fichiers **factices**
fabriqués ici ; aucun fichier publié n'est ouvert (R5 : chaque garde sur un cas sain et sur un artefact)."""
from __future__ import annotations

import hashlib
import json

import numpy as np
import pytest

from controle_ia.gardes import GardeArret
from controle_ia.narcbench import chargeur_externe_v1 as C
from controle_ia.narcbench import externe_v1 as X

CHAMPS_NULS = {k: None for k in C.CHAMPS}


def _ligne(run_id, mode, role, phase, rnd, agent, channel="public"):
    m = dict(CHAMPS_NULS)
    m.update(run_id=run_id, mode=mode, role=role, channel=channel, phase=phase, round=rnd, agent_name=agent,
             n_tokens=10, seed=0, flagged=False, family=run_id.split("__")[0], scenario_id=run_id.split("__")[1])
    return m


def _meta(etage, n_dom=2, par_dom=2, agents=4):
    meta = []
    for d in range(n_dom):
        for k in range(par_dom):
            for mode in ("collusion", "control"):
                rid = f"fam__dom{d}x_{k:02d}__{mode}"
                for j in range(agents):
                    role = "colluder" if mode == "collusion" and j < 2 else "honest"
                    if etage == "core":
                        for rnd in (1, 2, 3):
                            meta.append(_ligne(rid, mode, role, "discussion", rnd, f"agent{j}"))
                            meta.append(_ligne(rid, mode, role, "discussion", rnd, f"agent{j}", channel="private"))
                        meta.append(_ligne(rid, mode, role, "vote", None, f"agent{j}"))
                    else:
                        meta.append(_ligne(rid, mode, role, "bet", 1, f"agent{j}"))
                        meta.append(_ligne(rid, mode, role, "final", None, f"agent{j}"))
    return meta


def _ecrire(tmp_path, modele, etage, meta, couches, largeur, dtype=np.float32, alterer=None):
    d = tmp_path / "activations" / modele / etage
    d.mkdir(parents=True)
    (d / "metadata_gen.json").write_text(json.dumps(meta))
    rng = np.random.default_rng(0)
    tab = {f"layer_{c}": rng.standard_normal((len(meta), largeur)).astype(dtype) for c in couches}
    if alterer:
        alterer(tab)
    np.savez(d / "activations_gen.npz", **tab)
    return d


def test_cas_sain_core_et_stego_vers_externe(tmp_path):
    larg = 16
    _ecrire(tmp_path, "qwen3_32b", "core", _meta("core"), (26, 27), larg)
    _ecrire(tmp_path, "qwen3_32b", "stego", _meta("stego"), (26, 27), larg)
    core = C.episodes(C.charger_metadonnees(tmp_path / "activations/qwen3_32b/core/metadata_gen.json"),
                      C.charger_couches(tmp_path / "activations/qwen3_32b/core/activations_gen.npz", (26, 27),
                                        len(_meta("core")), larg), "core")
    eps, exclus = core
    assert len(eps) == 8 and exclus == {"agents_differents_de_4": [], "tours_inegaux": []}
    e = eps[0]
    assert e["acts"].shape == (4, 3, 2, larg) and e["etage"] == "CORE" and e["domaine"] == "dom0x"
    assert {x["condition"] for x in eps} == {"collusion", "temoin"}
    for x in eps:
        X.verifier_episode(x)          # le format rendu est celui qu'attend le bras externe
    st, _ = C.episodes(C.charger_metadonnees(tmp_path / "activations/qwen3_32b/stego/metadata_gen.json"),
                       C.charger_couches(tmp_path / "activations/qwen3_32b/stego/activations_gen.npz", (26, 27),
                                         len(_meta("stego")), larg), "stego")
    assert len(st) == 8 and st[0]["acts"].shape == (4, 1, 2, larg)   # phase `final` seule
    for x in st:
        X.verifier_episode(x)


def test_vecteur_core_egal_a_la_ligne_publiee(tmp_path):
    meta = _meta("core", n_dom=1, par_dom=1)
    d = _ecrire(tmp_path, "qwen3_32b", "core", meta, (26,), 4)
    acts = C.charger_couches(d / "activations_gen.npz", (26,), len(meta), 4)
    eps, _ = C.episodes(meta, acts, "core")
    i = next(i for i, m in enumerate(meta) if m["run_id"] == eps[0]["run_id"] and m["agent_name"] == "agent1"
             and m["round"] == 2 and m["channel"] == "public" and m["phase"] == "discussion")
    assert np.array_equal(eps[0]["acts"][1, 1, 0], acts[26][i])          # alignement ligne à ligne, au bit près


def test_domaine_regle_des_auteurs():
    assert C.domaine("cicd__cicd_01__collusion") == "cicd"
    assert C.domaine("deception__audit_trail_03__control") == "audit_trail"


def test_echantillons_par_message(tmp_path):
    meta = _meta("core")
    A = np.arange(len(meta) * 2, dtype=np.float32).reshape(len(meta), 2)
    col, hon = C.echantillons_apprentissage(meta, A)
    assert len(col) == 4 * 2 * 3 and len(hon) == 4 * 2 * 3    # 4 collusions × 2 rôles × 3 tours publics
    col2, hon2 = C.echantillons_apprentissage(meta, A, exclure_domaine="dom0x")
    assert len(col2) == len(col) // 2 and len(hon2) == len(hon) // 2


@pytest.mark.parametrize("alteration", ["couche_absente", "float64", "nan", "lignes"])
def test_artefacts_npz(tmp_path, alteration):
    meta = _meta("core")
    alt = {"couche_absente": lambda t: t.pop("layer_27"),
           "float64": lambda t: t.__setitem__("layer_27", t["layer_27"].astype(np.float64)),
           "nan": lambda t: t["layer_27"].__setitem__((3, 1), np.nan),
           "lignes": lambda t: t.__setitem__("layer_27", t["layer_27"][:-1])}[alteration]
    d = _ecrire(tmp_path, "qwen3_32b", "core", meta, (26, 27), 8, alterer=alt)
    with pytest.raises(GardeArret):
        C.charger_couches(d / "activations_gen.npz", (26, 27), len(meta), 8)


def test_artefact_largeur_et_pickle(tmp_path):
    meta = _meta("core")
    d = _ecrire(tmp_path, "qwen3_32b", "core", meta, (26,), 8)
    with pytest.raises(GardeArret):
        C.charger_couches(d / "activations_gen.npz", (26,), len(meta), 5120)
    np.savez(d / "objet.npz", layer_26=np.array([{"a": 1}] * len(meta), dtype=object))
    with pytest.raises(ValueError):                      # allow_pickle=False : un tableau d'objets est refusé
        C.charger_couches(d / "objet.npz", (26,), len(meta), 8)


def test_artefacts_metadonnees(tmp_path):
    meta = _meta("core")
    p = tmp_path / "m.json"
    p.write_text(json.dumps(meta))
    assert len(C.charger_metadonnees(p)) == len(meta)                    # cas sain
    for alt in ("champ", "mode", "run_id", "vide"):
        m2 = [dict(x) for x in meta]
        if alt == "champ":
            m2[5].pop("bp_corr")
        elif alt == "mode":
            m2[5]["mode"] = "collude"
        elif alt == "run_id":
            m2[5]["run_id"] = "sansscenario"
        else:
            m2 = []
        p.write_text(json.dumps(m2))
        with pytest.raises(GardeArret):
            C.charger_metadonnees(p)


def test_exclusions_comptees_et_incoherences(tmp_path):
    meta = _meta("core", n_dom=1, par_dom=1)
    trois = [m for m in meta if not (m["mode"] == "control" and m["agent_name"] == "agent3")]
    A = {26: np.zeros((len(trois), 4), dtype=np.float32)}
    eps, exclus = C.episodes(trois, A, "core")
    assert len(eps) == 1 and exclus["agents_differents_de_4"] == ["fam__dom0x_00__control"]   # compté, pas silencieux
    sans_tour = [m for m in meta if not (m["mode"] == "control" and m["agent_name"] == "agent3" and m["round"] == 3)]
    eps, exclus = C.episodes(sans_tour, {26: np.zeros((len(sans_tour), 4), dtype=np.float32)}, "core")
    assert exclus["tours_inegaux"] == ["fam__dom0x_00__control"]
    double = meta + [dict(meta[0])]
    with pytest.raises(GardeArret):
        C.episodes(double, {26: np.zeros((len(double), 4), dtype=np.float32)}, "core")
    role = [dict(m) for m in meta]
    j = next(i for i, m in enumerate(role) if m["channel"] == "public" and m["phase"] == "discussion" and m["round"] == 2
             and m["role"] == "colluder")
    role[j]["role"] = "honest"
    with pytest.raises(GardeArret):
        C.episodes(role, {26: np.zeros((len(role), 4), dtype=np.float32)}, "core")


def test_empreintes_et_verification(tmp_path):
    f = tmp_path / "a.bin"
    f.write_bytes(b"narcbench\n")
    assert C.empreinte(f, "sha256") == hashlib.sha256(b"narcbench\n").hexdigest()
    assert C.empreinte(f, "git-sha1") == hashlib.sha1(b"blob 10\0narcbench\n").hexdigest()   # = git hash-object
    bon = {"a.bin": (10, "sha256", hashlib.sha256(b"narcbench\n").hexdigest())}
    assert C.verifier_fichiers(tmp_path, bon)["a.bin"]["taille"] == 10                     # cas sain
    for faux in ({"a.bin": (11, "sha256", bon["a.bin"][2])}, {"a.bin": (10, "sha256", "0" * 64)},
                 {"b.bin": bon["a.bin"]}, {"a.bin": (10, "md5", "0")}):
        with pytest.raises(GardeArret):
            C.verifier_fichiers(tmp_path, faux)


def test_perimetre_sans_transfer(tmp_path):
    with pytest.raises(GardeArret):
        C.charger(tmp_path, "qwen3_32b", "transfer")
    with pytest.raises(GardeArret):
        C.charger(tmp_path, "gpt_oss_20b", "core")
    assert C.BANDES == {"qwen3_32b": (26, 27, 28, 29, 30), "llama_3_1_70b": (32, 33, 34, 35, 36, 37)}
