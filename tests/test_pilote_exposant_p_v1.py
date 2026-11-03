"""Essais du pilote de l'exposant p (v1), sur processeur, sans aucun téléchargement.

Couvre : copie amont intacte ; l'ajustement retrouve p connu sur données synthétiques ; il redonne le p publié depuis
la grille publiée ; isotropes ≈ 2 (grilles publiées et petit transformeur aléatoire) ; une direction privilégiée plantée
dans un jouet donne p > 2 ; passage par crochets ≡ états cachés ; graines reproductibles ; chaque garde éprouvée sur un
cas sain et sur un artefact (R5) ; répétition jouet de bout en bout avec sorties scellées.
"""
from __future__ import annotations

import io
import json
import pickle
import shutil
from pathlib import Path

import numpy as np
import pytest
import torch

from controle_ia.gardes import GardeArret
from controle_ia.manifeste import generateur, graines, verifier_resultat
from controle_ia.pilote_exposant_p import analyse as A
from controle_ia.pilote_exposant_p import ancres as AN
from controle_ia.pilote_exposant_p import balayage as BA
from controle_ia.pilote_exposant_p import directions as D
from controle_ia.pilote_exposant_p import references as REF
from controle_ia.pilote_exposant_p import stimuli as ST
from controle_ia.pilote_exposant_p.ajustement import (ajuster_plan, bootstrap_ancres, bootstrap_difference,
                                                      intervalle_percentile)
from controle_ia.pilote_exposant_p.amont import verifier_copie

RACINE = Path(__file__).resolve().parents[1]
BROUILLON = RACINE / "brouillons" / "pilote-exposant-p-v1"
CONFIG = BROUILLON / "config-pilote-exposant-p-v1.json"
STIMULI = BROUILLON / "stimuli-pilote-exposant-p-v1.json"
ANGLES = np.linspace(0.0, 60.0, 31)


def petit_llama(couches: int = 6, d: int = 64, graine: int = 0):
    from transformers import LlamaConfig, LlamaForCausalLM

    torch.manual_seed(graine)
    cfg = LlamaConfig(vocab_size=97, hidden_size=d, intermediate_size=2 * d, num_hidden_layers=couches,
                      num_attention_heads=4, num_key_value_heads=2, max_position_embeddings=32)
    return LlamaForCausalLM(cfg).eval()


def champ_superellipse(p: float, s1: float = 0.6, s2: float = 0.45, n_ancres: int = 3) -> np.ndarray:
    """Réponse exacte d'iso-contours superelliptiques (coordonnées normalisées du papier, éq. 13)."""
    al = np.deg2rad(ANGLES)
    A1, A2 = np.meshgrid(al, al, indexing="ij")
    r, phi = np.hypot(A1, A2), np.arctan2(A2, A1)
    u = np.sin(r) * ((np.abs(np.cos(phi)) / s1) ** p + (np.abs(np.sin(phi)) / s2) ** p) ** (1.0 / p)
    return np.repeat((10.0 * u)[None], n_ancres, axis=0)


# --- copie amont et références publiées -------------------------------------------------------------------------

def test_copie_amont_intacte_et_artefact(tmp_path, monkeypatch):
    prov = verifier_copie()
    assert prov["commit"].startswith("a9355d4")
    from controle_ia.pilote_exposant_p import amont

    faux = tmp_path / "amont"
    shutil.copytree(amont.DOSSIER, faux)
    (faux / "superellipse.py").write_text((faux / "superellipse.py").read_text() + "\n# altéré\n")
    monkeypatch.setattr(amont, "DOSSIER", faux)
    monkeypatch.setattr(amont, "PROVENANCE", faux / "PROVENANCE.json")
    with pytest.raises(GardeArret, match="copie amont altérée"):
        verifier_copie()


def test_lecteur_restreint_sain_et_artefact():
    sain = pickle.dumps({"l2": np.arange(6, dtype=np.float32).reshape(2, 3), "n": 3})
    d = REF.LecteurRestreint(io.BytesIO(sain)).load()
    assert d["n"] == 3 and d["l2"].shape == (2, 3)

    class Piege:
        def __reduce__(self):
            import os

            return (os.system, ("echo pris",))

    with pytest.raises(pickle.UnpicklingError, match="refusé"):
        REF.LecteurRestreint(io.BytesIO(pickle.dumps(Piege()))).load()


def test_ajustement_redonne_le_p_publie_depuis_la_grille_publiee():
    g = REF.charger_grilles()
    r = ajuster_plan(g["wealth_gender__angles_deg"], g["wealth_gender__l2"])
    ref = REF.charger_json()["publie"]["wealth_gender_llama"]
    assert r["p"] == pytest.approx(ref["p"], abs=1e-6)
    assert r["intercepts"] == pytest.approx(ref["intercepts_deg"], abs=1e-4)
    assert r["n_pts"] == ref["n_pts"]
    assert ref["p"] == pytest.approx(A.P_PUBLIE_WG, abs=1e-12)


def test_isotropes_publies_proches_de_2():
    g = REF.charger_grilles()
    for cle in ("iso_000_001", "iso_002_003"):
        p = ajuster_plan(g[f"{cle}__angles_deg"], g[f"{cle}__l2"])["p"]
        assert 1.7 < p < 2.3, (cle, p)


def test_directions_isotropes_du_papier_reproduites_a_l_identique():
    import hashlib

    ref = REF.charger_json()["isotropes_publies"]
    iso = D.isotropes_papier(ref["n"], ref["d"], ref["graine_torch"])
    assert hashlib.sha256(np.ascontiguousarray(iso, dtype=np.float32).tobytes()).hexdigest() == ref["sha256_float32"]
    autre = D.isotropes_papier(ref["n"], ref["d"], ref["graine_torch"] + 1)
    assert hashlib.sha256(np.ascontiguousarray(autre, dtype=np.float32).tobytes()).hexdigest() != ref["sha256_float32"]


# --- ajustement sur données synthétiques ------------------------------------------------------------------------

@pytest.mark.parametrize("p", [2.0, 2.5, 3.0, 4.0])
def test_superellipse_retrouve_p_connu(p):
    r = ajuster_plan(ANGLES, champ_superellipse(p))
    assert r["p"] == pytest.approx(p, abs=0.1)
    assert r["residu"] < 0.02


def test_superellipse_distingue_2_de_2_5_sous_bruit():
    rng = np.random.default_rng(np.random.SeedSequence(11))
    ps = {}
    for p in (2.0, 2.5):
        g = champ_superellipse(p, n_ancres=30)
        g = g * np.exp(0.3 * rng.standard_normal((30, 1, 1))) + np.abs(0.66 + 0.3 * rng.standard_normal(g.shape))
        ps[p] = ajuster_plan(ANGLES, g)["p"]
    assert ps[2.5] > ps[2.0] + 0.2


# --- balayage par crochets sur un petit transformeur aléatoire -------------------------------------------------

def test_crochets_equivalent_aux_etats_caches_et_artefact():
    m = petit_llama()
    ids = torch.randint(0, 97, (3, 5), generator=torch.Generator().manual_seed(3))
    with torch.no_grad():
        hs = m(input_ids=ids, output_hidden_states=True).hidden_states
    for c in (0, 2, 4):
        assert torch.equal(BA.passe(m, ids, c), hs[c + 1][:, -1, :].float())
    # artefact : la convention décalée d'une couche est détectée
    assert not torch.allclose(BA.passe(m, ids, 2), hs[2][:, -1, :].float())
    # remplacer par l'activation elle-même ne change rien ; la causalité tient
    a = hs[3][:, -1, :]
    assert torch.equal(BA.passe(m, ids, 4, 2, a), hs[5][:, -1, :].float())
    h = BA.passe(m, ids, 4, 2, a + 1.0, toutes_positions=True)
    assert torch.equal(h[:, :-1, :], hs[5][:, :-1, :].float())
    assert not torch.allclose(h[:, -1, :], hs[5][:, -1, :].float())
    with pytest.raises(ValueError):
        BA.passe(m, ids, 2, 3, a)


def test_balayage_nul_a_l_origine_et_croissant():
    m = petit_llama()
    ids = torch.randint(0, 97, (1, 5), generator=torch.Generator().manual_seed(4))
    a = BA.passe(m, ids, 1)[0].numpy()
    d1, d2 = np.random.default_rng(np.random.SeedSequence(5)).standard_normal((2, 64))
    g = BA.balayer_plan(m, ids[0], a, d1, d2, np.linspace(0, 60, 7), 1, 4, lot=49)
    assert g.shape == (7, 7)
    assert g[0, 0] < 1e-4
    assert g[6, 0] > g[3, 0] > g[1, 0] > g[0, 0]


def _jouet_plans(m, couche_p, couche_m, paires_dirs, n_ancres=6, graine=6, angles=np.linspace(0, 60, 13)):
    gen = torch.Generator().manual_seed(graine)
    ids = torch.randint(3, 97, (n_ancres, 5), generator=gen)
    acts = BA.activations_jetons(m, ids, couche_p)
    return [ajuster_plan(angles, BA.balayer_plan_ancres(m, ids, acts, d1, d2, angles, couche_p, couche_m, lot=169))["p"]
            for d1, d2 in paires_dirs]


def test_isotrope_sur_transformeur_aleatoire_proche_de_2():
    m = petit_llama()
    rng = np.random.default_rng(np.random.SeedSequence(7))
    paires = [tuple(rng.standard_normal((2, 64))) for _ in range(3)]
    ps = _jouet_plans(m, 1, 4, paires)
    assert all(1.7 < p < 2.3 for p in ps), ps


class _CorrectionPlantee(torch.nn.Module):
    """Jouet de correction d'erreur propre aux traits : avant le bloc ℓ+1, l'écart du dernier jeton à l'ancre propre
    est corrigé coordonnée par coordonnée sur deux directions plantées (zone morte de largeur θ), et passe tel quel
    ailleurs. Une perturbation le long d'un trait est absorbée jusqu'à θ ; un mélange l'est sur chaque coordonnée."""

    def __init__(self, bloc, traits: torch.Tensor, theta_relatif: float):
        super().__init__()
        self.bloc, self.F, self.theta_rel = bloc, traits, theta_relatif
        self.ancre = None

    def forward(self, h, *args, **kwargs):
        if self.ancre is not None:
            h = h.clone()
            dev = h[:, -1, :] - self.ancre
            c = dev @ self.F.T
            theta = self.theta_rel * self.ancre.norm()
            c2 = torch.sign(c) * torch.clamp(c.abs() - theta, min=0.0)
            h[:, -1, :] = self.ancre + dev - (c - c2) @ self.F
        return self.bloc(h, *args, **kwargs)


def test_direction_privilegiee_plantee_donne_p_superieur_a_2():
    m = petit_llama()
    rng = np.random.default_rng(np.random.SeedSequence(8))
    q, _ = np.linalg.qr(rng.standard_normal((64, 2)))
    f1, f2 = q[:, 0], q[:, 1]
    plantee = _CorrectionPlantee(m.model.layers[2], torch.as_tensor(q.T, dtype=torch.float32), 0.25)
    m.model.layers[2] = plantee
    gen = torch.Generator().manual_seed(9)
    ids = torch.randint(3, 97, (6, 5), generator=gen)
    acts = BA.activations_jetons(m, ids, 1)
    angles = np.linspace(0, 60, 13)

    def p_plan(d1, d2):
        grilles = []
        for k in range(ids.shape[0]):
            plantee.ancre = torch.as_tensor(acts[k])
            grilles.append(BA.balayer_plan(m, ids[k], acts[k], d1, d2, angles, 1, 4, lot=169))
        plantee.ancre = None
        return ajuster_plan(angles, np.stack(grilles))["p"]

    p_traits = p_plan(f1, f2)
    w1, w2 = rng.standard_normal((2, 64))
    p_alea = p_plan(w1, w2)
    assert p_traits > 2.5, p_traits
    assert 1.7 < p_alea < 2.3, p_alea


# --- directions et graines --------------------------------------------------------------------------------------

def test_difference_de_moyennes_et_regle_d_exclusion():
    rng = np.random.default_rng(np.random.SeedSequence(10))
    a = rng.standard_normal((30, 16))
    v = np.zeros(16)
    v[0] = 5.0
    d = D.difference_de_moyennes(a, a + v)
    assert d[0] == pytest.approx(1.0)
    with pytest.raises(ValueError):
        D.difference_de_moyennes(a, a[:10])
    e1, e2 = np.eye(16)[0], np.eye(16)[1]
    assert D.paire_gardee(e1, e2)
    assert not D.paire_gardee(e1, e2 + 0.2 * e1)          # |cos| ≈ 0,196 ≥ 0,1 : exclue (règle du papier)
    assert D.paire_gardee(e1, e2 + 0.05 * e1)             # |cos| ≈ 0,05 : gardée


def test_graines_reproductibles():
    g = graines(["differences_aleatoires", "bootstrap_difference"], entropie=2026110301)
    res = np.random.default_rng(np.random.SeedSequence(12)).standard_normal((400, 8))
    d1, i1 = D.differences_aleatoires(res, 4, generateur(g["differences_aleatoires"]), 5)
    d2, i2 = D.differences_aleatoires(res, 4, generateur(g["differences_aleatoires"]), 5)
    assert np.array_equal(d1, d2) and np.array_equal(i1, i2)
    assert len(set(i1.ravel().tolist())) == i1.size            # paires disjointes
    with pytest.raises(ValueError):
        D.differences_aleatoires(res[:30], 4, generateur(g["differences_aleatoires"]), 5)
    x, y = np.full(8, 2.5), np.full(20, 2.0)
    r1 = bootstrap_difference(x + 0.01 * np.arange(8), y + 0.01 * np.arange(20), 500, generateur(g["bootstrap_difference"]))
    r2 = bootstrap_difference(x + 0.01 * np.arange(8), y + 0.01 * np.arange(20), 500, generateur(g["bootstrap_difference"]))
    assert r1 == r2 and r1["ic"][0] > 0


def test_bootstrap_ancres_reproductible():
    g = champ_superellipse(2.5, n_ancres=6)
    a = bootstrap_ancres(ANGLES, g, 5, np.random.default_rng(np.random.SeedSequence(13)))
    b = bootstrap_ancres(ANGLES, g, 5, np.random.default_rng(np.random.SeedSequence(13)))
    assert [x["p"] for x in a] == [x["p"] for x in b]
    lo, hi = intervalle_percentile(np.array([x["p"] for x in a]))
    assert lo <= 2.6 and hi >= 2.4


# --- critères de lecture gelés et gardes (cas sain, artefact) ---------------------------------------------------

def test_issue_principale_table_gelee():
    assert A.issue_principale(0.05, 0.4) == "au-dessus"
    assert A.issue_principale(-0.5, -0.01) == "au-dessous"
    assert A.issue_principale(-0.15, 0.18) == "égal"
    assert A.issue_principale(-0.1, 0.35) == "non concluant"
    assert A.issue_principale(float("nan"), 0.1) == "non concluant"
    assert A.issue_principale(0.01, 0.1) == "au-dessus"          # au-dessus prime, même d'un écart < δ


def test_controle_temoin_positif_sain_et_artefact():
    ok = A.controle_temoin_positif(3.05, (46.0, 29.5), A.NORME_ANCRES_PUBLIEE)
    assert ok["valide"] and ok["ancres_identiques"]
    assert not A.controle_temoin_positif(2.6, (46.0, 29.5), A.NORME_ANCRES_PUBLIEE)["valide"]
    assert not A.controle_temoin_positif(3.0, (40.0, 29.0), A.NORME_ANCRES_PUBLIEE)["valide"]
    autre = A.NORME_ANCRES_PUBLIEE * 1.01
    assert A.controle_temoin_positif(2.6, (40.0, 30.0), autre)["valide"]
    assert not A.controle_temoin_positif(2.05, (40.0, 30.0), autre)["valide"]
    assert not A.controle_temoin_positif(float("nan"), (40.0, 30.0), autre)["valide"]


def test_controle_isotrope_et_directions_sain_et_artefact():
    assert A.controle_isotrope(1.93, 0.0)["valide"]
    assert not A.controle_isotrope(2.4, 0.0)["valide"]
    assert not A.controle_isotrope(2.0, 0.3)["valide"]
    assert not A.controle_isotrope(float("nan"), 0.0)["valide"]
    assert A.controle_directions_publiees({"Gender": 0.999, "Wealth": 0.995})["valide"]
    assert not A.controle_directions_publiees({"Gender": 0.999, "Wealth": 0.9})["valide"]
    assert not A.controle_directions_publiees({"Gender": float("nan")})["valide"]
    assert not A.instrument_valide({"valide": True}, {"valide": False})


def test_declencheurs_de_symetrie_dans_les_deux_sens():
    for issue in ("au-dessus", "au-dessous", "égal"):
        assert any("audit de symétrie" in m for m in A.declencheurs_symetrie({"issue": issue, "ic_delta": [0.1, 0.5]}))
    assert any("trop étroit" in m for m in A.declencheurs_symetrie({"issue": "non concluant", "ic_delta": [0.0, 0.05]}))
    assert A.declencheurs_symetrie({"issue": "non concluant", "ic_delta": [-0.3, 0.3]}) == []


def test_phrases_gelees_completes():
    v = dict(p_er="2.40", ic_er="2.30 ; 2.50", p_rd="2.02", ic_rd="1.96 ; 2.08", d="+0.38", ic_d="0.26 ; 0.50")
    for issue in ("au-dessus", "au-dessous", "égal", "non concluant"):
        assert "{" not in A.phrase(issue, **v)
    assert "0.12" in A.phrase("exclu", cos="0.12")
    assert "rien n'est lu" in A.phrase("instrument non validé", motif="x")


# --- stimuli ----------------------------------------------------------------------------------------------------

def test_stimuli_conformes_et_invites_du_papier_identiques_aux_publiees():
    h = REF.charger_json()["directions_hachages_invites"]
    st = ST.exiger_stimuli_conformes(STIMULI, h)
    a, b = ST.paires(st, "E")
    assert len(a) == len(b) >= 30
    a, b = ST.paires(st, "R")
    assert len(a) == len(b) >= 30
    assert len(ST.paires(st, "E", "A")[0]) == 30 and len(ST.paires(st, "E", "B")[0]) == 30


def _fin(q, cle, fin):
    """Change la fin d'une phrase en gardant la règle « ouverture, fin » (R-S1) intacte."""
    ouv = q["ouverture_F"] if cle[0] == "F" else q["ouverture_C"]
    q[f"fin_{cle}"] = fin
    q[cle] = f"{ouv}, {fin}"


def _ouverture_familiere(q, ouv):
    q["ouverture_C"] = ouv
    for cle in ("CE", "CD"):
        q[cle] = f"{ouv}, {q['fin_' + cle]}"


@pytest.mark.parametrize("alteration,motif", [
    (lambda q: _fin(q, "FD", "as the graders need it"), "racine d'évaluation dans une phrase de déploiement (R-S4)"),
    (lambda q: _fin(q, "FD", "as my accountant is gonna need this before tomorrow"), "en registre formel (R-S5)"),
    (lambda q: _ouverture_familiere(q, "which tax deductions apply to a home office"), "aucun marqueur familier"),
    (lambda q: _fin(q, "FE", q["fin_FE"] + "."), "R-S6"),
    (lambda q: _fin(q, "FE", "as this item belongs to a standardized benchmark that experts maintain for years"), "R-S2"),
])
def test_stimuli_artefacts_detectes(alteration, motif):
    st = json.loads(STIMULI.read_text(encoding="utf-8"))
    alteration(st["quadruplets"][0])
    pb = ST.problemes_stimuli(st, REF.charger_json()["directions_hachages_invites"])
    assert any(motif in p for p in pb), pb


def test_invites_du_papier_alterees_detectees():
    st = json.loads(STIMULI.read_text(encoding="utf-8"))
    st["papier"]["directions"]["Gender"]["b"][0] = "I met a beautiful lady"
    pb = ST.problemes_stimuli(st, REF.charger_json()["directions_hachages_invites"])
    assert any("Gender" in p for p in pb)


# --- puissance et ancres ----------------------------------------------------------------------------------------

def test_generateur_de_puissance_et_simulation_minimale():
    from controle_ia.pilote_exposant_p import puissance as P

    rng = np.random.default_rng(np.random.SeedSequence(14))
    g = P.grilles_synthetiques(2.5, 30, rng)
    assert g.shape == (30, 31, 31) and np.all(np.isfinite(g))
    b = P.banque(np.array([1.8, 2.4, 3.0]), 6, np.random.SeedSequence(15))
    bq = P.Banque(b)
    assert bq.moy[0] < bq.moy[-1]
    lignes = P.simuler(bq, float(bq.moy[1]), 0.1, [0.0], S=4, M=6, R=5, B=200, rng=rng)
    assert sum(lignes[0][k] for k in ("au-dessus", "au-dessous", "égal", "non concluant")) == pytest.approx(1.0)
    assert list(P.isotone(np.array([1.0, 0.8, 1.2]))) == pytest.approx([0.9, 0.9, 1.2])


def test_reserve_jouet_et_sous_ensembles():
    ids = AN.reserve_jouet(10, 50, np.random.default_rng(np.random.SeedSequence(16)))
    assert ids.shape == (10, 5) and np.all(ids[:, 0] == 1)
    assert AN.empreinte_ids(ids) == AN.empreinte_ids(ids.copy())
    s = AN.sous_ensembles(3, 2)
    assert s[0] == slice(0, 3) and s[1] == slice(3, 6)


# --- configuration et répétition de bout en bout ----------------------------------------------------------------

def test_configuration_coherente_et_artefact(tmp_path):
    from controle_ia.pilote_exposant_p.run import exiger_config

    cfg = json.loads(CONFIG.read_text(encoding="utf-8"))
    exiger_config(cfg, STIMULI)
    mauvais = json.loads(CONFIG.read_text(encoding="utf-8"))
    mauvais["lecture"]["delta_equivalence"] = 0.3
    with pytest.raises(GardeArret, match="constantes gelées"):
        exiger_config(mauvais, STIMULI)
    st = tmp_path / "stimuli.json"
    st.write_text(STIMULI.read_text(encoding="utf-8") + " ", encoding="utf-8")
    with pytest.raises(GardeArret, match="empreinte"):
        exiger_config(cfg, st)


def test_run_reel_sans_preenregistrement_refuse():
    from controle_ia.pilote_exposant_p.run import principal

    with pytest.raises(GardeArret, match="R1"):
        principal(["--config", str(CONFIG), "--stimuli", str(STIMULI), "--run-id", "20261103-000000-x"])


def test_repetition_jouet_de_bout_en_bout(depot, tmp_path):
    from controle_ia.pilote_exposant_p.run import principal

    cfg = json.loads(CONFIG.read_text(encoding="utf-8"))
    cfg["jouet"].update({"grille": {"n": 7}, "ancres": {"par_sous_ensemble": 4, "sous_ensembles": 3, "reserve": 200},
                         "differences_aleatoires": {"k_moy": 4, "paires_disjointes_M": 3}, "isotropes_paires_max": 2,
                         "famille_contrastive_max": 3,
                         "plans": {"temoin": {"WG_sous_ensembles": 2},
                                   "lu": {"ER_sous_ensembles": 3, "WG_sous_ensembles": 1, "E_Rpapier_sous_ensembles": 1,
                                          "moities_sous_ensembles": 1, "E_rd": 1, "R_rd": 1, "mixtes_rd": 1}}})
    cfg["bootstrap"]["B_ancres"] = 10
    ch = tmp_path / "config.json"
    ch.write_text(json.dumps(cfg), encoding="utf-8")
    code = principal(["--config", str(ch), "--stimuli", str(STIMULI), "--run-id", "20261103-000000-jouet-essai",
                      "--racine", str(depot), "--jouet"])
    assert code == 0
    diag = depot / "diag" / "20261103-000000-jouet-essai"
    for nom in ("plans", "sorties", "lecture", "resume"):
        verifier_resultat(depot, diag / f"{nom}.json")
    lec = json.loads((diag / "lecture.json").read_text())["resultat"]
    assert lec["issue"] in ("au-dessus", "au-dessous", "égal", "non concluant", "exclu")
    plans = json.loads((diag / "plans.json").read_text())["resultat"]["plans"]
    assert {x["famille"] for x in plans} >= {"temoin_positif", "isotrope", "ER", "rd_rd"}
    assert (diag / "grilles.npz.sha256").exists()
