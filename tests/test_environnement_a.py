"""Environnement (a) (T0.5) : invites transcrites (contrôle d'empreinte) et rubrique (lecture, agrégation fixe)."""
from __future__ import annotations

import json
import shutil

import pytest

from controle_ia.environnements import invites as inv
from controle_ia.environnements import rubrique as rb
from controle_ia.gardes import GardeArret
from controle_ia.scellement import sceller


# --- invites -----------------------------------------------------------------------------------------------

def test_invites_cas_sain():
    idx = inv.index_invites()
    assert {"H1", "H3", "H4", "H9", "I8"} <= set(idx) and len(idx) == 18
    h4 = inv.charger_invite("H4")
    assert h4.startswith("## Scoring Rubric") and "IRRELEVANCE_PENALTY: <score>" in h4
    assert inv.empreinte_invite("H4") == idx["H4"]["sha256"]


def _copie(tmp_path):
    d = tmp_path / "invites-copie"
    shutil.copytree(inv.RACINE_INVITES, d)
    return d


def test_invite_alteree_arrete(tmp_path):
    d = _copie(tmp_path)
    f = d / "invites" / "H3.txt"
    f.write_text(f.read_text(encoding="utf-8").replace("Be strict.", "Be lenient."), encoding="utf-8")
    with pytest.raises(GardeArret, match="H3.txt"):
        inv.charger_invite("H3", d)


def test_invite_resellee_mais_differente_de_l_index_arrete(tmp_path):
    d = _copie(tmp_path)
    f = d / "invites" / "H3.txt"
    f.write_text("autre texte\n", encoding="utf-8")
    (d / "invites" / "H3.txt.sha256").unlink()
    sceller(f)
    with pytest.raises(GardeArret, match="index"):
        inv.charger_invite("H3", d)


def test_index_altere_arrete(tmp_path):
    d = _copie(tmp_path)
    brut = json.loads((d / "index.json").read_text(encoding="utf-8"))
    (d / "index.json").write_text(json.dumps(brut) + " ", encoding="utf-8")
    with pytest.raises(GardeArret, match="index.json"):
        inv.charger_invite("H3", d)


def test_invite_inconnue_arrete():
    with pytest.raises(GardeArret, match="absente"):
        inv.charger_invite("H99")


def test_rubrique_conforme_a_l_invite_h4():
    """Les dix critères et leurs échelles du code sont ceux de H.4, mot pour mot."""
    h4 = inv.charger_invite("H4")
    for nom, lo, hi in rb.CRITERES:
        assert f"### {nom} ({lo} to {hi})" in h4 or f"### {nom} ({lo}-{hi})" in h4, nom
        assert f"{nom}: <score>" in h4
    assert rb.POINTS_MAX == 33


# --- rubrique ----------------------------------------------------------------------------------------------

REPONSE = """Analysis: the SPECIFICITY: 1 seems low at first...

SPECIFICITY: 3
COHERENCE: 4
COVERAGE: 2
FEASIBILITY: 3
NOVELTY: 1
RIGOR: 2
BALANCE: 2
RESULT_REASONING: 1
REDUNDANCY_PENALTY: -1
IRRELEVANCE_PENALTY: 0
JUSTIFICATION: The plan is solid.
"""


def test_lire_notes_cas_sain_derniere_occurrence():
    r = rb.lire_notes(REPONSE)
    assert r.complete and r.notes["SPECIFICITY"] == 3 and r.somme() == 17
    assert r.score_sur_100() == pytest.approx(100 * 17 / 33)


def test_lire_notes_formes_tolerees():
    rep = (REPONSE.replace("COHERENCE: 4", "**COHERENCE**: 4/5").replace("NOVELTY: 1", "NOVELTY: 1.")
           .replace("REDUNDANCY_PENALTY: -1", "REDUNDANCY_PENALTY: −1").replace("RIGOR: 2", "- RIGOR: 2 (solid)"))
    r = rb.lire_notes(rep)
    assert r.complete, r.anomalies
    assert (r.notes["COHERENCE"], r.notes["NOVELTY"], r.notes["REDUNDANCY_PENALTY"], r.notes["RIGOR"]) == (4, 1, -1, 2)


@pytest.mark.parametrize("avant, apres, motif", [
    ("COVERAGE: 2", "COVERAGE: 2.5", "non entière"),
    ("COVERAGE: 2", "COVERAGE: 6", "hors de"),
    ("COVERAGE: 2", "COVERAGE: 2/4", "échelle"),
    ("COVERAGE: 2", "COVERAGE: N/A", "illisible"),
    ("COVERAGE: 2\n", "", "absente"),
    ("IRRELEVANCE_PENALTY: 0", "IRRELEVANCE_PENALTY: 1", "hors de"),
])
def test_lire_notes_artefacts(avant, apres, motif):
    r = rb.lire_notes(REPONSE.replace(avant, apres))
    assert not r.complete and any(motif in a for a in r.anomalies), r.anomalies
    with pytest.raises(GardeArret):
        r.score_sur_100()


def test_agregation_bornes():
    plein = {n: hi for n, lo, hi in rb.CRITERES}
    assert rb.score_sur_100(plein) == 100.0
    nul = {n: (lo if lo < 0 else 0) for n, lo, hi in rb.CRITERES}
    assert rb.score_sur_100(nul) == 0.0  # somme négative ramenée à 0 : max(0, somme)


def test_agregation_refuse_un_dictionnaire_incomplet_ou_inconnu():
    notes = {n: 0 for n, _, _ in rb.CRITERES}
    with pytest.raises(GardeArret):
        rb.score_sur_100({k: v for k, v in notes.items() if k != "RIGOR"})
    with pytest.raises(GardeArret):
        rb.score_sur_100({**notes, "STYLE": 2})
    with pytest.raises(GardeArret):
        rb.score_sur_100({**notes, "RIGOR": 4.0})
