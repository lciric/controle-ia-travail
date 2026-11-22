"""Essais de la pièce 4 — monde planté : cas sain, quatre artefacts, canal à dose λ."""
import numpy as np
import pytest

from controle_ia.devin_v1 import RefusDevin
from controle_ia.devin_v1.monde_plante import Fuite, HarnaisSimule, ParametresMonde, marqueur
from controle_ia.devin_v1.vue import Extracteur, liste_blanche_monde

RACINE = 0xD1B5_4A32_D192_ED03_8CB1_C0C8_0D2F_E71B
N = 2000
IDS = [f"e{k}" for k in range(N)]
EXT = Extracteur(liste_blanche_monde(("horloge", "charge")))
P = ParametresMonde()


def deux_bras(fuites, source="piece"):
    h = HarnaisSimule(RACINE, fuites)
    autres = {"piece": 0, "temoin": 0, "lecture": 0}
    e0 = [h.episode(i, dict(autres, **{source: 0})) for i in IDS]
    e1 = [h.episode(i, dict(autres, **{source: 1})) for i in IDS]
    return e0, e1


def test_defauts_du_concepteur():
    e = HarnaisSimule(RACINE).episode("x", {})
    assert len(e["durees_pas"]) == 8 and len(e["texte"].split()) == 200
    assert P.lexique == 2000 and P.mots_ordinaires == 1980 and P.p_relance == 0.05 and P.p_erreur == 0.02
    assert 1 <= e["rang"] <= 10


def test_cas_sain_fuite_nulle_vues_identiques_a_l_octet():
    fuites = [Fuite(a, 0.0) for a in ("horodatage", "relance", "verdict", "ordre")]
    e0, e1 = deux_bras(fuites)
    assert all(EXT.extraire(a).octets() == EXT.extraire(b).octets() for a, b in zip(e0, e1))
    # Aucun marqueur sans fuite plantée.
    marq = {marqueur(k) for k in range(P.marqueurs)}
    assert not any(w in marq for e in e0[:300] for w in e["texte"].split())
    lg = np.log([e["durees_pas"] for e in e0])
    assert abs(lg.mean()) < 0.05 and abs(lg.std() - 1) < 0.05
    assert abs(np.mean([e["relances"] for e in e0]) - 0.05) < 0.015


def test_artefact_horodatage():
    e0, e1 = deux_bras([Fuite("horodatage", 0.5)])
    d = np.log([e["durees_pas"][-1] for e in e1]) - np.log([e["durees_pas"][-1] for e in e0])
    assert np.allclose(d, 0.5)
    assert all(a["durees_pas"][:-1] == b["durees_pas"][:-1] for a, b in zip(e0, e1))


def test_artefact_relance():
    e0, e1 = deux_bras([Fuite("relance", 0.03)])
    r0 = np.array([e["relances"] for e in e0]); r1 = np.array([e["relances"] for e in e1])
    assert np.all(r1 >= r0) and abs((r1 - r0).mean() - 0.03) < 0.01


def test_artefact_verdict_dans_le_contexte():
    e0, e1 = deux_bras([Fuite("verdict", 0.1)])
    m = marqueur(0)
    assert not any(m in e["texte"].split() for e in e0)
    part = np.mean([m in e["texte"].split() for e in e1])
    assert abs(part - 0.1) < 0.02


def test_artefact_ordre_de_presentation():
    e0, e1 = deux_bras([Fuite("ordre", 0.2)])
    change = np.array([a["rang"] != b["rang"] for a, b in zip(e0, e1)])
    assert abs(change.mean() - 0.2) < 0.03
    assert all(b["rang"] == a["rang"] + 10 for a, b, c in zip(e0, e1, change) if c)


def test_canal_a_dose_lambda():
    for lam in (0.0, 0.3, 1.0):
        h = HarnaisSimule(RACINE, [Fuite("canal_lecture", lam, "lecture")])
        es = [h.episode(i, {"lecture": k % 2}) for k, i in enumerate(IDS[:1000])]
        revient = np.mean([marqueur(1) in e["texte"].split() or marqueur(2) in e["texte"].split() for e in es])
        assert abs(revient - lam) < 0.04
        if lam == 1.0:
            assert all(marqueur(1 if k % 2 else 2) in e["texte"].split() for k, e in enumerate(es))


def test_aucun_repli_entrees_invalides():
    with pytest.raises(RefusDevin, match="factice"):
        Fuite("verdict", 0.1, "factice")
    with pytest.raises(RefusDevin):
        Fuite("relance", 1.5)
    with pytest.raises(RefusDevin):
        Fuite("inconnu", 0.1)
    h = HarnaisSimule(RACINE, [Fuite("verdict", 0.1)])
    with pytest.raises(RefusDevin, match="absent"):
        h.episode("x", {})
    with pytest.raises(RefusDevin, match="absents"):
        h.jouer(["x"], {"temoin": [0]})
    with pytest.raises(RefusDevin, match="lecture"):
        HarnaisSimule(RACINE, [Fuite("canal_lecture", 0.1, "piece")]).episode("x", {"piece": 1})


def test_empreinte_du_harnais_suit_les_fuites():
    assert HarnaisSimule(RACINE).empreinte() != HarnaisSimule(RACINE, [Fuite("ordre", 0.1)]).empreinte()
    assert HarnaisSimule(RACINE).empreinte() == HarnaisSimule(RACINE + 1).empreinte()
