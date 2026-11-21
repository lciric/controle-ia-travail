"""Essais R5 de `t07bbis.commun_v1` (B bis, plan, points 5, 9, 12) : graines par clé (R9 : `SeedSequence`, clés du texte seulement,
entropie de 128 bits en marche réelle), cellules et séries fixées par le texte, grille entrelacée et départage des ex aequo, refus
de la moyenne et de la médiane sur les jetons (N-026)."""
from __future__ import annotations

import numpy as np
import pytest

from controle_ia.gardes import GardeArret
from controle_ia.manifeste import generateur, graines as graines_manifeste
from controle_ia.t07bbis import commun_v1 as cm


def test_graines_derivees_comme_le_manifeste_et_rejouables():
    e = 2 ** 127 + 12345
    g = cm.Graines(e)
    for cle in ("bbis/interne/e0", "bbis/entrainement/sonde/P-S100/e1i3/attention-c23-l2_0.1", "bbis/plancher/P-S25/e0",
                "bbis/reetiquetage/P-instruit/99", "bbis/egalite-carte", "bbis/chemin-impose", "bbis/epreuve-niveau",
                "bbis/tirages/T-instruit-S50", "bbis/tirages/BB-P6", "bbis/entrainement/nul7/P-S50/e0/lineaire-c7-l2_0.001",
                "bbis/entrainement/enc/P-instruit/e1/lineaire-c15-l2_0.01"):
        assert g.graine(cle) == graines_manifeste([cle], e)[cle]
        assert g.entier(cle) == cm.Graines(e).entier(cle)
        assert np.array_equal(g.rng(cle).integers(0, 10 ** 9, 5), generateur(g.graine(cle)).integers(0, 10 ** 9, 5))
    assert g.entier("bbis/interne/e0") != g.entier("bbis/interne/e1")
    assert len(g.derivees) == 12                     # les onze clés, plus bbis/interne/e1


def test_cle_hors_du_texte_refusee_et_entropie_courte_refusee_en_marche_reelle():
    g = cm.Graines(2 ** 127 + 1)
    for cle in ("bbis/autre", "bbis/interne/e2", "t07/plancher/x", "bbis/entrainement/sonde/P-S100/e0/lineaire-c7"):
        with pytest.raises(GardeArret, match="hors des formes"):
            g.graine(cle)
    with pytest.raises(GardeArret, match="64 bits"):
        cm.Graines(12345)
    assert cm.Graines(12345, reelle=False).entier("bbis/egalite-carte") >= 0
    for faux in (0, -3, 2 ** 128, True, 1.5):
        with pytest.raises(GardeArret):
            cm.exiger_entropie(faux, reelle=False)


def test_cellules_et_series_fixees_par_le_texte():
    c = cm.cellules(cm.DOSES_REELLES)
    assert list(c["plafond"]) == ["P-instruit", "P-S25", "P-S50", "P-S75", "P-S100"]
    assert list(c["transfert"]) == ["T-instruit-S25", "T-instruit-S50", "T-instruit-S75", "T-instruit-S100", "T-S100-instruit"]
    assert c["transfert"]["T-S100-instruit"] == {"source": "P-S100", "positifs": "saboteur", "famille": "(i-a)", "dose": None}
    assert all(v["source"] == "P-instruit" for k, v in c["transfert"].items() if k.startswith("T-instruit"))
    s = {x["serie"]: x for x in cm.series_imposees(cm.DOSES_REELLES)}
    assert list(s) == ["J25", "J50", "J75", "J100", "Jinstruit", "A25", "A50", "A75", "A100", "AT"]
    assert s["J50"] == {"serie": "J50", "textes": "S50", "environnement": "honnete", "adaptateur": None, "dose": 0.0}
    assert s["Jinstruit"]["textes"] == "saboteur" and s["Jinstruit"]["environnement"] == "honnete"
    assert s["A75"] == {"serie": "A75", "textes": "honnete", "environnement": "honnete", "adaptateur": "saboteur", "dose": 0.75}
    assert s["AT"]["adaptateur"] == "temoin" and s["AT"]["dose"] == 1.0
    assert cm.nom_jumeau("S25") == "J25" and cm.nom_jumeau("saboteur") == "Jinstruit"
    with pytest.raises(GardeArret):
        cm.nom_jumeau("honnete")


def test_configuration_reelle_doit_porter_les_doses_et_couches_du_texte():
    cfg = {"mode": "reel", "doses_saboteur": [0.25, 0.5, 0.75, 1.0], "doses_temoin": [1.0], "couches": [7, 15, 23]}
    assert cm.plan_doses_couches(cfg) == (cm.DOSES_REELLES, cm.COUCHES_REELLES)
    with pytest.raises(GardeArret, match="≠ celles du texte"):
        cm.plan_doses_couches({**cfg, "couches": [7, 16, 23]})
    with pytest.raises(GardeArret, match="dose 1"):
        cm.plan_doses_couches({**cfg, "doses_temoin": [0.5]})
    assert cm.plan_doses_couches({**cfg, "mode": "jouet", "doses_saboteur": [0.5, 1.0], "couches": [1, 2, 3]})[0] == (0.5, 1.0)


def test_grille_de_dix_huit_reglages_entrelacee_et_departage_des_ex_aequo():
    g = cm.grille(cm.COUCHES_REELLES)
    assert len(g) == 18 and len({r["nom"] for r in g}) == 18
    premiers = [r["famille"] for r in (g + g)[:20]]
    assert premiers.count("lineaire") == 10 and premiers.count("attention") == 10
    assert all(r["agregation"] == ("max" if r["famille"] == "lineaire" else "attention") for r in g)
    ordre = sorted(g, key=lambda r: cm.rang_ex_aequo(r, cm.COUCHES_REELLES))
    assert [r["nom"] for r in ordre[:4]] == ["lineaire-c15-l2_0.1", "lineaire-c15-l2_0.01", "lineaire-c15-l2_0.001",
                                            "lineaire-c7-l2_0.1"]
    assert ordre[-1]["nom"] == "attention-c23-l2_0.001"


def test_moyenne_ou_mediane_sur_les_jetons_refusees():
    for a in ("max", "attention"):
        assert cm.exiger_agregation(a) == a
    for a in ("moyenne", "mediane", "mean", "median", "somme"):
        with pytest.raises(GardeArret, match="N-026"):
            cm.exiger_agregation(a)


def test_empreinte_du_texte_scelle():
    from pathlib import Path
    from controle_ia.scellement import verifier
    racine = Path(__file__).resolve().parents[1]
    assert verifier(racine / cm.TEXTE) == cm.TEXTE_SHA256
