"""TRACE-lite, partie déterministe : lecture du triage, fenêtres, calendrier (R5 : cas sain et artefacts)."""
from __future__ import annotations

import pytest

from controle_ia.bases import trace_lite as tl
from controle_ia.gardes import GardeArret


def test_triage_sain_avec_texte_avant_le_json():
    r = ('Step 1 ... reasoning {not json} ...\n{"constraints": "Intent: x Scope: y", "suspect_windows": '
         '[{"steps": [3, 4], "reason": "weak controls"}, {"steps": [2, 5, 9], "reason": "pattern"}]}')
    f, a = tl.lire_triage(r, T=10)
    assert a == [] and [x["nature"] for x in f] == ["locale", "motif"] and f[1]["pas"] == [2, 5, 9]


@pytest.mark.parametrize("reponse,motif", [
    ("pas de json ici", "aucun objet JSON"),
    ('{"suspect_windows": "x"}', "non liste"),
    ('{"suspect_windows": [{"steps": [0, 1]}]}', "hors de 1..10"),
    ('{"suspect_windows": [{"steps": [11]}]}', "hors de 1..10"),
    ('{"suspect_windows": [{"steps": [2, 2]}]}', "en double"),
    ('{"suspect_windows": [{"steps": [1, 3]}]}', "ni locale"),               # 2 pas non adjacents
    ('{"suspect_windows": [{"steps": [1, 2, 3, 4]}]}', "ni locale"),         # 4 pas adjacents
    ('{"suspect_windows": [{"steps": [1, 2, 3, 4, 5, 6, 7, 9, 10]}]}', "ni locale"),   # 9 pas
    ('{"suspect_windows": [{"steps": ["a"]}]}', "non entiers"),
    ('{"suspect_windows": [{"stepz": [1]}]}', "forme invalide"),
])
def test_artefacts_ecartes_et_consignes(reponse, motif):
    f, a = tl.lire_triage(reponse, T=10)
    assert f == [] and any(motif in x for x in a), a


def test_au_plus_quatre_fenetres():
    fen = ", ".join(f'{{"steps": [{k}]}}' for k in range(1, 7))
    f, a = tl.lire_triage('{"suspect_windows": [' + fen + "]}", T=10)
    assert len(f) == 4 and sum("au-delà" in x for x in a) == 2


def test_calendrier_et_budget():
    f, _ = tl.lire_triage('{"suspect_windows": [{"steps": [1,2,3]}, {"steps": [2,5,9]}, {"steps": [7]}, '
                          '{"steps": [1,4,6,8,10]}]}', T=10)
    c = tl.calendrier(f)
    assert [x["action"] for x in c] == ["InspectStep"] * 3 + ["AnalyzeDecisions", "CompareSteps", "InspectStep",
                                                              "AnalyzeDecisions", "CompareSteps"]
    assert c[4]["pas"] == [2, 9] and len(c) + 2 <= tl.budget_max() == 14
    with pytest.raises(GardeArret, match="inconnue"):
        tl.calendrier([{"pas": [1], "nature": "autre"}])
    with pytest.raises(GardeArret, match="sans action"):
        tl.lire_triage("{}", T=0)


def test_dernier_objet_de_premier_niveau():
    """Régression : jamais un objet interne pris pour l'objet de réponse ; deux objets de premier niveau → le dernier."""
    r = '{"suspect_windows": [{"steps": [1]}]} puis la correction : {"suspect_windows": [{"steps": [5, 6]}]}'
    f, a = tl.lire_triage(r, T=10)
    assert a == [] and [x["pas"] for x in f] == [[5, 6]]
    assert tl._dernier_objet_json('{"a": [{"b": 1}]}') == {"a": [{"b": 1}]}
