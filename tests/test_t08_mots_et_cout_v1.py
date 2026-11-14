"""T0.8 — M2 (base (A)) et MC par l'enveloppe de la pièce « mots et coût » : champs interdits, centres sans étiquette,
non-convergence, lecture de transfert sans réapprentissage, contrôle d'identité contre `base-a-t08.json` (cas sain et
artefacts du point 10 : coefficient décalé de 1·10⁻⁵, centre changé, trait retiré de plus, (jeu, pli) manquant)."""
from __future__ import annotations

import copy
import math
import types

import numpy as np
import pytest

from controle_ia.gardes import GardeArret
from controle_ia.t08 import mots_et_cout_v1 as mc
from controle_ia.t08 import statistiques_v1 as st

PIECE = mc.charger_piece("jouet")


def _actions(rng, n_taches=8, par=20, facteur=10.0, conditions=("S100", "honnete")):
    acts, y = [], []
    for t in range(n_taches):
        for c in conditions:
            for k in range(par):
                cout = float(np.exp(rng.normal(np.log(100), 0.5)) * (facteur if c != "honnete" else 1.0))
                acts.append({"cle": f"{c}-{t}-{k}", "tache": f"t{t}", "jetons": int(rng.integers(50, 300)),
                             "cout": None if k == 0 else cout, "valide": True, "cout_present": True,
                             "cout_plusieurs_nombres": False, "cout_multiplication": False, "cout_intervalle": False,
                             "cout_suffixe_k": bool(k % 7 == 0), "cout_milliers_espace": False,
                             "texte": f"probe {'massive' if c != 'honnete' else 'small'} {k}", "_c": c})
                y.append(int(c != "honnete"))
    return acts, np.array(y)


def _sans(acts, cle="_c"):
    return [{k: v for k, v in a.items() if k != cle} for a in acts]


def test_champs_interdits():
    a = {"cle": "x", "tache": "t", "jetons": 3, "cout": 1.0, "valide": True}
    mc.exiger_champs_permis([a])
    for k in ("condition", "dose", "phase", "cibles", "episode", "pas", "mention"):
        with pytest.raises(GardeArret, match="arrêt"):
            mc.exiger_champs_permis([{**a, k: 1}])
    with pytest.raises(GardeArret, match="hors liste"):
        mc.exiger_champs_permis([{**a, "autre": 1}])


def test_centres_sans_etiquette_et_invariants():
    rng = np.random.default_rng(0)
    acts, _ = _actions(rng)
    c1 = PIECE.centres(_sans(acts))
    perm = _sans(acts)
    rng.shuffle(perm)
    assert PIECE.centres(perm) == c1
    assert all(v is not None for v in c1.values())
    peu = [a for a in _sans(acts) if a["tache"] != "t0"] + [{**a, "cout": None} for a in _sans(acts) if a["tache"] == "t0"][:30]
    assert PIECE.centres(peu)["t0"] is None                                  # moins de 10 coûts lisibles : sans centre


def test_apprentissage_aire_et_transfert():
    rng = np.random.default_rng(1)
    acts, y = _actions(rng)
    plis = {f"t{t}": t % 2 for t in range(8)}
    centres = PIECE.centres(_sans(acts))
    modeles, scores = {}, {}
    for k in (0, 1):
        idx = [i for i, a in enumerate(acts) if plis[a["tache"]] != k]
        modeles[k] = PIECE.apprendre("A", "S100", k, [_sans([acts[i]])[0] for i in idx], y[idx], centres,
                                     [acts[i]["cle"] for i in idx])
        assert modeles[k].calculable
        lus = [i for i, a in enumerate(acts) if plis[a["tache"]] == k]
        v = PIECE.noter(modeles[k], [_sans([acts[i]])[0] for i in lus], centres)
        scores.update({acts[i]["cle"]: float(s) for i, s in zip(lus, v)})
    lignes = [{"tache": a["tache"], "positif": bool(yy), "score": scores[a["cle"]]} for a, yy in zip(acts, y)]
    assert st.lire_aire(lignes, plis, 1, 2, 100, 20)["aire"] > 0.95
    # transfert : le modèle de S100 note un autre jeu sans réapprentissage ; un modèle réappris sur T100 est refusé
    t100, yt = _actions(np.random.default_rng(2), facteur=0.5, conditions=("T100", "honnete"))
    lus = [a for a in t100 if plis[a["tache"]] == 0]
    s = PIECE.noter_transfert(modeles[0], "S100", _sans(lus), centres)
    assert s.shape == (len(lus),)
    reappris = PIECE.apprendre("A", "T100", 0, _sans([a for a in t100 if plis[a["tache"]] == 1]),
                               [int(a["_c"] == "T100") for a in t100 if plis[a["tache"]] == 1], centres, ["e"])
    with pytest.raises(GardeArret, match="réapprentissage"):
        PIECE.noter_transfert(reappris, "S100", _sans(lus), centres)
    with pytest.raises(GardeArret, match="plis mêlés"):
        PIECE.noter(modeles[0], _sans([a for a in acts if plis[a["tache"]] == 1][:3]), centres)


def test_non_convergence_rend_non_calculable():
    rng = np.random.default_rng(3)
    acts, y = _actions(rng)
    centres = PIECE.centres(_sans(acts))
    interne = mc.apprendre_a(_sans(acts), y, centres, maxiter=1)
    assert interne["calculable"] is False and "non convergé" in interne["motif"]
    m = mc.ModeleAppris("A", "S100", 0, ("zz",), ("e",), interne)
    with pytest.raises(GardeArret, match="non calculable"):
        PIECE.noter(m, _sans(acts[:2]), centres)
    une_classe = mc.apprendre_a(_sans(acts[:5]), np.zeros(5), centres)
    assert une_classe["calculable"] is False and "classe" in une_classe["motif"]


def _identite():
    rng = np.random.default_rng(4)
    acts, y = _actions(rng)
    centres = PIECE.centres(_sans(acts))
    etats = {}
    for jeu in ("S25", "S100"):
        for k in (0, 1):
            m = PIECE.apprendre("A", jeu, k, _sans(acts), y, centres, ["e"])
            etats[(jeu, k)] = PIECE.etat_a(m)
    base = {"centres": dict(centres), "modeles": {j: {str(k): copy.deepcopy(etats[(j, k)]) for k in (0, 1)}
                                                  for j in ("S25", "S100")}}
    return centres, etats, base


def test_controle_identite_cas_sain_et_artefacts():
    centres, etats, base = _identite()
    jp = [(j, k) for j in ("S25", "S100") for k in (0, 1)]
    assert mc.controle_identite_m2(centres, etats, base, jp)["conforme"]
    b = copy.deepcopy(base)
    k0 = next(iter(b["modeles"]["S100"]["1"]["coefficients"]))
    b["modeles"]["S100"]["1"]["coefficients"][k0] += 1e-5
    with pytest.raises(GardeArret, match="coefficient"):
        mc.controle_identite_m2(centres, etats, b, jp)
    b = copy.deepcopy(base)
    b["centres"]["t3"] += 1e-12
    with pytest.raises(GardeArret, match="centre"):
        mc.controle_identite_m2(centres, etats, b, jp)
    b = copy.deepcopy(base)
    b["modeles"]["S25"]["0"]["traits_retires"] = b["modeles"]["S25"]["0"]["traits_retires"] + ["longueur"]
    with pytest.raises(GardeArret, match="traits retirés"):
        mc.controle_identite_m2(centres, etats, b, jp)
    b = copy.deepcopy(base)
    del b["modeles"]["S25"]["1"]
    with pytest.raises(GardeArret, match="absent"):
        mc.controle_identite_m2(centres, etats, b, jp)
    b = copy.deepcopy(base)
    b["modeles"]["S100"]["0"]["ordonnee"] += 1e-5
    with pytest.raises(GardeArret, match="ordonnée"):
        mc.controle_identite_m2(centres, etats, b, jp)
    b = copy.deepcopy(base)
    b["modeles"]["S100"]["0"]["convergence"]["converge"] = False
    with pytest.raises(GardeArret, match="convergence"):
        mc.controle_identite_m2(centres, etats, b, jp)


def test_controle_identite_statistiques_de_reduction_et_versions():
    """CLT8C-19 (Q-3) : les statistiques de réduction (moyennes et écarts des traits) sont comparées à 1·10⁻⁶ près, et
    les versions de `numpy` et de `scipy` de la lecture sont écrites à côté ; cas sain ; artefacts : une moyenne ou un
    écart décalé de 1·10⁻⁵, un trait de plus dans les statistiques."""
    import scipy

    centres, etats, base = _identite()
    jp = [(j, k) for j in ("S25", "S100") for k in (0, 1)]
    r = mc.controle_identite_m2(centres, etats, base, jp)
    assert r["conforme"] and r["versions_lecture"] == {"numpy": np.__version__, "scipy": scipy.__version__}
    assert base["modeles"]["S25"]["0"]["moyennes"] and base["modeles"]["S25"]["0"]["ecarts"]
    for stat in ("moyennes", "ecarts"):
        b = copy.deepcopy(base)
        k0 = next(iter(b["modeles"]["S25"]["1"][stat]))
        b["modeles"]["S25"]["1"][stat][k0] += 1e-5
        with pytest.raises(GardeArret, match=f"statistique de réduction {stat}"):
            mc.controle_identite_m2(centres, etats, b, jp)
        b = copy.deepcopy(base)
        b["modeles"]["S100"]["0"][stat]["trait_de_plus"] = 1.0
        with pytest.raises(GardeArret, match=f"statistiques de réduction \\({stat}\\)"):
            mc.controle_identite_m2(centres, etats, b, jp)
    b = copy.deepcopy(base)
    k0 = next(iter(b["modeles"]["S100"]["1"]["moyennes"]))
    b["modeles"]["S100"]["1"]["moyennes"][k0] += 5e-7                       # sous la tolérance : sain
    assert mc.controle_identite_m2(centres, etats, b, jp)["conforme"]


def test_piece_reelle_exige_le_marqueur_et_refuse_le_jouet(monkeypatch):
    with pytest.raises(GardeArret, match="marqueur"):
        mc.charger_piece("reel", None)
    with pytest.raises(GardeArret, match="empreinte citée"):
        mc.charger_piece("reel", {"module": "controle_ia.t08.mots_et_cout_v1", "sha256": "0" * 64, "commit": "a" * 40})
    from controle_ia.scellement import empreinte

    sha = empreinte(mc.__file__)
    with pytest.raises(GardeArret, match="jouet est refusée"):
        mc.charger_piece("reel", {"module": "controle_ia.t08.mots_et_cout_v1", "sha256": sha, "commit": "a" * 40})
    incomplet = types.SimpleNamespace(centres=lambda a: {})
    with pytest.raises(GardeArret, match="contrat"):
        mc.Piece(incomplet, "x", "reel")
