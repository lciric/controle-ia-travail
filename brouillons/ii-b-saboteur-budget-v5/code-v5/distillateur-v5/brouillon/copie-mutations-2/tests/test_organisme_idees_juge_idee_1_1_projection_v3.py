"""Idée 1.1 (préenregistrement scellé `3ffe1739…`) — projection par blocs : copies octet pour octet, forme scindée égale à
la forme d'origine, gardes du certificat, de la positivité (P5), des blocs, de l'accès (P4), monde de Q8. Graines d'essai
distinctes de celles du jeu (racine d'essai, jamais l'empreinte du texte)."""
import ast
import hashlib
from pathlib import Path

import numpy as np
import pytest

from controle_ia.gardes import GardeArret
from controle_ia.organisme_idees_juge import attaque_projection_extrait_v1 as AT
from controle_ia.organisme_idees_juge import banc_idee_1_1_v2 as B
from controle_ia.organisme_idees_juge import projection_bras_v1 as PB
from controle_ia.organisme_idees_juge import projection_commun_v1 as cm
from controle_ia.organisme_idees_juge import projection_methodes_v1 as me

RACINE_DEPOT = Path(__file__).resolve().parents[1]
NOTES = RACINE_DEPOT / "docs/notes/organisme-idees-juge-v1/correction-poids-v1/projection"
ICI = RACINE_DEPOT / "src/controle_ia/organisme_idees_juge"
RACINE_ESSAI = int(hashlib.sha256(b"essais idee 1.1 v1, projection").hexdigest(), 16)


def _segments(chemin):
    src = Path(chemin).read_text(encoding="utf-8")
    out = {}
    for n in ast.parse(src).body:
        if isinstance(n, (ast.FunctionDef, ast.ClassDef)):
            out[n.name] = ast.get_source_segment(src, n)
        elif isinstance(n, ast.Assign) and isinstance(n.targets[0], ast.Name):
            out[n.targets[0].id] = ast.get_source_segment(src, n)
    return out


def test_copie_octet_pour_octet_du_banc_commun():
    a, b = (NOTES / "essai_projection_commun_v1.py").read_bytes(), (ICI / "projection_commun_v1.py").read_bytes()
    assert a == b
    assert hashlib.sha256(a).hexdigest() == "1f4ada977b6cdb96378f3c913df0119bcf6fc333981217ecbbb3583b38f2ca54"


@pytest.mark.parametrize("source,copie,noms", [
    ("essai_projection_methodes_v1.py", "projection_methodes_v1.py",
     ["IT_PROJ", "IT_MV", "IT_CHAUD", "_blocs_projection", "m3_toutes_coupures", "_mv_cellule", "a1_en_ligne", "a2_moitie"]),
    ("attaque_projection_v1.py", "attaque_projection_extrait_v1.py",
     ["K", "MINI", "em_commun", "loi_commun", "projeter_commun", "projection_globale", "carte_a_memoire"])])
def test_extraits_recopies_octet_pour_octet(source, copie, noms):
    s, c = _segments(NOTES / source), _segments(ICI / copie)
    for n in noms:
        assert s[n] == c[n], n
    assert set(c) == set(noms)
    assert me.IT_PROJ == 300 and me.IT_CHAUD == 150 and AT.K == 3


def monde_jouet(graine, carte_hors=False):
    rng = np.random.default_rng(np.random.SeedSequence(entropy=RACINE_ESSAI, spawn_key=(97, 900, graine)))
    a = cm.tirer_archive(rng)
    z, g = cm.tirer_plan(rng)
    L = cm.lois_connues(a, z)
    cA, cB, c4 = cm.cellules_archive(a, z)
    M = cm.si_sinon(cA == 1, L[:, 0], L[:, 1])
    Q = cm.p_softmax(a["S1"], z) if carte_hors else M
    y = cm.tirer_issues(rng, M)
    return dict(L=L, Q=Q, y=y, z=z, g=g, cA=cA, cB=cB, c4=c4)


def _scinde(m, blocs_un_a_un=False):
    Qb = np.stack([m["Q"][a:e] for a, e in cm.BLOCS])
    qs = {b: PB.questions_j9p(m["z"], m["g"], b) for b in range(PB.NB)}
    if blocs_un_a_un:
        proj = {}
        for b in range(PB.NB):
            proj.update(PB.projeter(m["L"], Qb, qs, 2, [b]))
    else:
        proj = PB.projeter(m["L"], Qb, qs, 2, range(PB.NB))
    le = PB.valeurs_e(proj, Qb, {b: m["y"][a:e] for b, (a, e) in enumerate(cm.BLOCS)})
    return proj, le


@pytest.mark.parametrize("graine", [0, 1])
def test_forme_scindee_egale_a_la_forme_d_origine(graine):
    m = monde_jouet(graine, carte_hors=bool(graine))
    proj, le = _scinde(m)
    proc, noms = PB.processus_j9p(le, m["z"])
    assert np.max(np.abs(proc.min(0) - me.m3_toutes_coupures(m))) <= 1e-9
    _, le2 = _scinde(m, blocs_un_a_un=True)
    assert max(np.max(np.abs(le[b] - le2[b])) for b in range(8)) <= 1e-9
    B.verifier_familles_j9p(noms, m["z"])
    B.verifier_terme(le, m["z"], B.terme_projete(proc))


def test_certificat_au_moins_un_et_projection_sans_issue():
    m = monde_jouet(2)
    proj, _ = _scinde(m)
    c = np.concatenate([proj[b]["c"] for b in range(8)])
    assert c.min() >= 1 - 1e-9 and np.isfinite(c).all()
    import inspect
    assert "issue" not in inspect.signature(PB.projeter).parameters and "y" not in inspect.signature(PB.projeter).parameters


@pytest.mark.parametrize("c,ok", [([1.0, 1.2], True), ([], False), ([1.0, np.nan], False), ([1.0, 1 - 1e-8], False)])
def test_garde_certificat(c, ok):
    if ok:
        PB.exiger_certificats(c)
    else:
        with pytest.raises(GardeArret):
            PB.exiger_certificats(c)


def test_garde_positivite_p5(monkeypatch):
    m = monde_jouet(3)
    Qb = np.stack([m["Q"][a:e] for a, e in cm.BLOCS])
    qs = {0: PB.questions_lap(m["cA"], m["cB"], 0)}
    PB.projeter(m["L"], Qb, qs, 2, [0])
    monkeypatch.setattr(cm, "probas_commun", lambda *a: np.zeros((3, 25, 3)))
    with pytest.raises(GardeArret, match="P5"):
        PB.projeter(m["L"], Qb, qs, 2, [0])


def test_garde_blocs_alignes(monkeypatch):
    PB.exiger_blocs_alignes()
    monkeypatch.setattr(cm, "BLOCS", [(a + 1, e + 1) for a, e in cm.BLOCS])
    with pytest.raises(GardeArret, match="décalés"):
        PB.exiger_blocs_alignes()


def test_journal_modifie_apres_empreinte_refuse():
    m = monde_jouet(4)
    Qb = np.stack([m["Q"][a:e] for a, e in cm.BLOCS])
    proj = PB.projeter(m["L"], Qb, {0: PB.questions_lap(m["cA"], m["cB"], 0)}, 2, [0])
    PB.valeurs_e(proj, Qb, {0: m["y"][:25]})
    proj[0]["c"] = proj[0]["c"] * 1.0001
    with pytest.raises(GardeArret, match="journal"):
        PB.valeurs_e(proj, Qb, {0: m["y"][:25]})


def test_flux_frais_garde_d_acces_sous_gel():
    f = PB.FluxFrais(lambda b: [b % 3] * 25)
    assert f.passe(0) == []
    f.tirer_bloc(0)
    assert f.passe(1) == [0] * 25           # cas sain : exactement les issues des blocs < b
    with pytest.raises(PB.GardeAcces):       # artefact : la projection du bloc 0 demandée après son tirage
        f.passe(0)
    f.tirer_bloc(1)
    with pytest.raises(PB.GardeAcces):
        f.passe(1)
    with pytest.raises(GardeArret):
        f.tirer_bloc(3)


@pytest.mark.parametrize("lit,forme,ligne_h,ok", [(False, "refus", False, True), (True, "gel", True, True),
                                                   (True, "nu", True, True), (True, None, True, False),
                                                   (True, "nu", False, False), (False, "autre", False, False)])
def test_garde_p4_deux_formes_et_sans_garde_declare(lit, forme, ligne_h, ok):
    if ok:
        assert PB.exiger_garde(lit, forme, ligne_h) == forme
    else:
        with pytest.raises(GardeArret):
            PB.exiger_garde(lit, forme, ligne_h)


def test_monde_q8_egal_a_projection_globale():
    m = monde_jouet(5, carte_hors=True)
    archive = {n: {"type": "fixe", "probas": [1.0, 1.0, 1.0]} for n in ("S1", "S2", "S3", "S4")}
    monde, d = B.monde_q8(m["L"], m["Q"], archive)
    P = AT.projection_globale({"L": m["L"]}, m["Q"], np.zeros(200, int), 1, 600)
    w = np.array(d["v"]) * (1 - d["tau"])
    P_moi = np.einsum("j,sjk->sk", w, m["L"]) + d["tau"] * np.array(d["u"])[None]
    assert np.max(np.abs(P_moi / P_moi.sum(1, keepdims=True) - P)) <= 1e-12
    assert abs(sum(monde["poids"]) - 1) <= 1e-12 and len(monde["composantes"]) == 5


def test_carte_h7_gelee_ne_lit_pas_le_bloc():
    rng = np.random.default_rng(np.random.SeedSequence(entropy=RACINE_ESSAI, spawn_key=(97, 901)))
    M = rng.dirichlet(np.ones(3), size=200)
    y = np.array([int(rng.choice(3, p=p)) for p in M])
    Q_vrai = AT.carte_a_memoire("contre_exces_du_bloc", 0.3, 1.0, M, y, 25, True)
    for b in range(8):
        a, e = 25 * b, 25 * (b + 1)
        Q_b = AT.carte_a_memoire("contre_exces_du_bloc", 0.3, 1.0, M[:e], np.concatenate([y[:a], np.zeros(25, int)]), 25, True)
        assert np.array_equal(Q_b[a:e], Q_vrai[a:e])
    Q_nu = AT.carte_a_memoire("contre_exces_du_bloc", 0.3, 1.0, M, y, 25, False)
    assert not np.allclose(Q_nu, Q_vrai)
