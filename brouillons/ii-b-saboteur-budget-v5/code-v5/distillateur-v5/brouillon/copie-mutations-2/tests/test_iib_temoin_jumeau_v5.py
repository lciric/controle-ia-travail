"""Témoin-jumeau redéfini pour chaque oracle, v5 (texte scellé, section 11 ; section 13, `temoin_jumeau_v5.py`)."""
import pytest

from controle_ia.gardes import GardeArret
from controle_ia.iib import configuration_v5 as cf
from controle_ia.iib import jumeau_v5 as jm
from controle_ia.iib import oracle_v5 as ov
from controle_ia.iib import regenere_v5 as rg
from controle_ia.iib import temoin_jumeau_v5 as tj
from controle_ia.iib.jouet_v5 import SIGNAL_MAITRE, EnvironnementJouet, ModeleJouetDeLangue
from controle_ia.iib.lecture_cout_v5 import lire_action_v5, lire_fenetre

CFG = cf.gabarit("jouet")
FINS = frozenset({0})


def _maitre(part_illisible=0.04, entropie=31):
    m = ModeleJouetDeLangue({"part_illisible": part_illisible})
    g = jm.Graines(entropie)
    ep = rg.jouer_lot(m, [EnvironnementJouet("t1", consigne=SIGNAL_MAITRE)], ["t1/tour1"], [g.entiers("a", 10)], 400, 1.0)[0]
    o = ov.oracles_episode(m, EnvironnementJouet("t1"), ep["actions"], g, CFG, "maitre", "t1/tour1")
    return m, g, ep, o


def _hors_cout(tok, ids):
    t = tok.decode(ids)
    i = t.index("COST:")
    return t[:i + 5], t[i:].split("\n", 1)[1]


def test_N_le_temoin_porte_la_suite_retenue_par_la_reecriture_couplee():
    m, g, ep, o = _maitre()
    tok = m.fmt.tok
    t = tj.episode_temoin("N", tok, ep["actions"], g, "t1/tour1", CFG, FINS, retenues=o["retenues"])
    assert [a["ids"] for a in t["actions"]] == [a["ids"] for a in o["reecrites"]]      # ce qui est entré dans le contexte du jumeau
    assert t["actions"][0]["ids"] == ep["actions"][0]["ids"]                            # premier coût à l'octet
    for k in range(10):
        assert _hors_cout(tok, t["actions"][k]["ids"]) == _hors_cout(tok, ep["actions"][k]["ids"])   # tout champ hors coût à l'octet


def test_P_la_suite_prise_est_une_des_huit_de_l_action_et_non_la_mediane():
    m, g, ep, o = _maitre()
    tok = m.fmt.tok
    lect = [l["suites"] for l in o["sorties"]["P"]]
    t = tj.episode_temoin("P", tok, ep["actions"], g, "t1/tour1", CFG, FINS, suites=o["suites"]["P"], lectures_suites=lect)
    assert t["actions"][0]["ids"] == ep["actions"][0]["ids"] and not t["consignes"][0]["remplacee"]
    pas_la_mediane = 0
    for k in range(1, 10):
        n = t["consignes"][k]
        assert n["remplacee"] and 0 <= n["indice"] < 8
        assert _hors_cout(tok, t["actions"][k]["ids"]) == _hors_cout(tok, ep["actions"][k]["ids"])
        lu = lire_action_v5(tok, t["actions"][k]["ids"], FINS)
        prise = lire_fenetre(tok, o["suites"]["P"][k][n["indice"]], FINS)
        assert lu["cout_declare"] == prise["valeur"]                                    # le coût du témoin est celui de la suite prise
        pas_la_mediane += int(prise["valeur"] != o["sorties"]["P"][k]["estimation"])
    assert pas_la_mediane >= 1
    assert tj.episode_temoin("P", tok, ep["actions"], jm.Graines(31), "t1/tour1", CFG, FINS, suites=o["suites"]["P"], lectures_suites=lect)["actions"] == t["actions"]
    autre = tj.episode_temoin("P", tok, ep["actions"], jm.Graines(99), "t1/tour1", CFG, FINS, suites=o["suites"]["P"], lectures_suites=lect)
    assert autre["actions"] != t["actions"]                                             # tirée au hasard par graine


def test_cout_illisible_suite_illisible_ou_vide():
    lisible, illisible = {"lisible": True}, {"lisible": False}
    g = jm.Graines(2)
    assert tj.choisir_suite_P([lisible] * 5 + [illisible] + [lisible] * 2, False, g.generateur("k")) == 5
    assert tj.choisir_suite_P([lisible] * 8, False, g.generateur("k")) is None           # aucune suite illisible : valeur vide
    assert tj.choisir_suite_P([lisible] * 8, True, g.generateur("k")) in range(8)
    m = ModeleJouetDeLangue({"part_illisible": 0.0})
    tok = m.fmt.tok
    texte = "ACTION: ADD\nTITLE: A2\nPROPOSAL: test 2\nCONTROLS: seeds\nCOST: a lot\nPREDICTION: ok"
    actions = [{"ids": tok(texte.replace("a lot", "100"))["input_ids"] + [0]}] + [{"ids": tok(texte)["input_ids"] + [0]}] * 9
    suites = [[tok(" 120\n")["input_ids"]] * 8] * 10
    lect = [[lire_fenetre(tok, s, FINS) for s in ss] for ss in suites]
    t = tj.episode_temoin("P", tok, actions, g, "e", CFG, FINS, suites=suites, lectures_suites=lect)
    assert all(n["vide"] for n in t["consignes"][1:]) and "COST:\nPREDICTION" in tok.decode(t["actions"][3]["ids"])


def test_gardes_du_temoin():
    m, g, ep, o = _maitre()
    with pytest.raises(GardeArret, match="suites retenues"):
        tj.episode_temoin("N", m.fmt.tok, ep["actions"], g, "e", CFG, FINS)
    with pytest.raises(GardeArret, match="huit suites"):
        tj.episode_temoin("P", m.fmt.tok, ep["actions"], g, "e", CFG, FINS, suites=o["suites"]["P"])
    with pytest.raises(GardeArret, match="ni N ni P"):
        tj.episode_temoin("Q", m.fmt.tok, ep["actions"], g, "e", CFG, FINS)
