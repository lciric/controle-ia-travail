"""Invite « qwen-boxed », lecture de MATH500 et vérificateur de réponse en boîte (exploratoire). R5 : cas sain et artefact."""
import json

import pytest

from controle_ia.dopamine_exploratoire import math500_v1 as m
from controle_ia.gardes import GardeArret


def test_invite_litterale_est_le_gabarit_qwen_boxed():
    t = m.invite("What is $1+1$?", "litteral")
    assert t.startswith("<|im_start|>system\nYou are a helpful assistant.<|im_end|>\n<|im_start|>user\nWhat is $1+1$?")
    assert t.endswith("put your final answer within \\boxed{}.<|im_end|>\n<|im_start|>assistant\n")


def test_invite_gabarit_du_modele_par_defaut_exige_un_gabarit():
    t = m.invite("x", gabarit_du_modele=lambda s, u: f"<{s}>[{u}]")
    assert t == "<You are a helpful assistant.>[x\nPlease reason step by step, and put your final answer within \\boxed{}.]"
    with pytest.raises(GardeArret):
        m.invite("x")
    with pytest.raises(GardeArret):
        m.invite("x", "autre")
    with pytest.raises(GardeArret):
        m.invite("  ")


@pytest.mark.parametrize("texte,boite", [
    ("so \\boxed{5}.", "5"),
    ("\\boxed{1} then \\boxed{\\frac{1}{2}}", "\\frac{1}{2}"),
    ("\\boxed{\\sqrt{2}+{3}}", "\\sqrt{2}+{3}"),
    ("\\fbox{7}", "7"),
    ("\\boxed 9$", "9"),
    ("no box", None),
    ("cut \\boxed{12", None),
])
def test_derniere_boite(texte, boite):
    assert m.derniere_boite(texte) == boite


@pytest.mark.parametrize("obtenue,attendue,egal", [
    ("\\dfrac{1}{2}", "\\frac12", True),
    ("0.5", "\\frac{1}{2}", True),
    ("1,000", "1000", True),
    ("10^\\circ", "10", True),
    ("\\text{(A)}", "(A)", True),
    ("x=3", "3", True),
    ("\\left(1,2\\right)", "(1,2)", True),
    ("3", "4", False),
    ("\\frac{1}{3}", "0.33", False),
    (None, "1", False),
])
def test_reponses_egales(obtenue, attendue, egal):
    assert m.reponses_egales(obtenue, attendue) is egal


def test_noter_strict_drapeaux_et_plafond():
    n = m.noter("... \\boxed{\\dfrac{3}{4}}", "\\frac{3}{4}")
    assert n == {"boite": "\\dfrac{3}{4}", "recompense": 1, "recompense_stricte": 1, "sans_boite": False,
                 "au_plafond": False}
    assert m.noter("\\boxed{0.75}", "\\frac{3}{4}")["recompense_stricte"] == 0          # désaccord compté
    assert m.noter("... \\boxed{2}", "3")["recompense"] == 0
    assert m.noter("bonne valeur 3 hors du cadre", "3") == {"boite": None, "recompense": 0, "recompense_stricte": 0,
                                                         "sans_boite": True, "au_plafond": False}
    assert m.noter("\\boxed{3}", "3", au_plafond=True)["recompense"] == 0                  # coupée au plafond : r = 0


def test_garde_d_invite_sain_et_artefacts():
    from controle_ia.dopamine_exploratoire.jouet_v1 import DecoupeurJouet
    d = DecoupeurJouet()
    t = m.invite("1+2", "litteral")
    m.exiger_invite(t, d.encoder(t), d, "<|im_start|>assistant\n")
    with pytest.raises(GardeArret, match="en-tête"):
        m.exiger_invite(t[:-1], d.encoder(t[:-1]), d, "<|im_start|>assistant\n")      # en-tête ôté
    with pytest.raises(GardeArret, match="recodée"):
        m.exiger_invite(t, d.encoder(t) + [d.eos_id], d, "<|im_start|>assistant\n")   # jetons qui ne se recodent pas


def _jeu(tmp_path, lignes):
    p = tmp_path / "test.jsonl"
    p.write_text("".join(json.dumps(x) + "\n" for x in lignes), encoding="utf-8")
    return p


def test_lire_math500_sain_et_artefacts(tmp_path):
    q = [{"problem": f"p{i}", "answer": str(i), "unique_id": f"u{i}"} for i in range(3)]
    qs, sha = m.lire_math500(_jeu(tmp_path, q), effectif_attendu=3)
    assert [x["id"] for x in qs] == ["u0", "u1", "u2"] and len(sha) == 64
    with pytest.raises(GardeArret, match="questions"):
        m.lire_math500(_jeu(tmp_path, q), effectif_attendu=500)
    with pytest.raises(GardeArret, match="double"):
        m.lire_math500(_jeu(tmp_path, q + [q[0]]), effectif_attendu=None)
    with pytest.raises(GardeArret, match="answer"):
        m.lire_math500(_jeu(tmp_path, [{"problem": "p", "unique_id": "u"}]), effectif_attendu=None)
