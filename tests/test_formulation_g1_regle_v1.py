"""Règle de choix gelée et contrôles de lecture : toutes les issues, gardes sur cas sain et sur artefact."""
import pytest

from controle_ia.formulation_g1 import lecture_v1 as le
from controle_ia.gardes import GardeArret


def _ind(a, b, e=(0.0, 1.0, 0.8)):
    f = lambda v: {"faux_positifs_empreinte_seule": v[0], "faux_positifs_avance_vehiculaire": v[1],
                   "couverture_de_puissance": v[2], "puissance_moyenne": v[2]}
    return {"A": f(a), "B": f(b), "E": f(e)}


@pytest.mark.parametrize("a, b, e, issue", [
    ((0.02, 0.02, 0.7), (0.02, 0.60, 0.7), (0, 1, 0.8), le.A_RETENUE),                      # validité nette pour A
    ((0.02, 0.02, 0.4), (0.02, 0.60, 0.7), (0, 1, 0.8), le.NON_TRANCHE_VALIDITE_PUISSANCE),  # mais puissance très en retrait
    ((0.02, 0.60, 0.7), (0.02, 0.02, 0.7), (0, 1, 0.8), le.C_RETENUE),                      # validité nette pour B
    ((0.02, 0.60, 0.8), (0.02, 0.02, 0.5), (0, 1, 0.8), le.NON_TRANCHE_VALIDITE_PUISSANCE),
    ((0.02, 0.02, 0.8), (0.02, 0.02, 0.6), (0, 1, 0.8), le.A_RETENUE),                      # puissance seule
    ((0.02, 0.02, 0.6), (0.02, 0.02, 0.8), (0, 1, 0.8), le.C_RETENUE),
    ((0.02, 0.10, 0.7), (0.02, 0.15, 0.75), (0, 1, 0.8), le.NON_TRANCHE_EGALITE),
    ((0.30, 0.02, 0.7), (0.02, 0.60, 0.7), (0, 1, 0.8), le.C_RETENUE),                      # A invalide
    ((0.02, 0.02, 0.7), (0.30, 0.60, 0.7), (0, 1, 0.8), le.A_RETENUE),                      # B invalide
    ((0.30, 0.02, 0.7), (0.30, 0.60, 0.7), (0, 1, 0.8), le.AUCUNE_INVALIDES),
    ((0.02, 0.02, 0.1), (0.30, 0.60, 0.7), (0, 1, 0.8), le.AUCUNE_SANS_PUISSANCE),
    ((0.02, 0.02, 0.1), (0.02, 0.02, 0.7), (0, 1, 0.8), le.C_RETENUE),                      # A sans puissance utile
    ((0.02, 0.02, 0.0), (0.02, 0.02, 0.0), (0, 1, 0.0), le.NON_INFORMATIF),
])
def test_regle_toutes_issues(a, b, e, issue):
    assert le.regle_de_choix(_ind(a, b, e)) == issue
    assert issue in le.ISSUES


def test_regle_symetrique():
    """Échanger A et B échange « A retenue » et « C retenue » : la règle ne vise aucun signe (R3)."""
    import itertools

    valeurs = [(f1, f2, c) for f1 in (0.02, 0.3) for f2 in (0.02, 0.1, 0.6) for c in (0.0, 0.3, 0.5, 0.75, 0.8)]
    miroir = {le.A_RETENUE: le.C_RETENUE, le.C_RETENUE: le.A_RETENUE}
    for a, b in itertools.product(valeurs, valeurs):
        x, y = le.regle_de_choix(_ind(a, b)), le.regle_de_choix(_ind(b, a))
        assert miroir.get(x, x) == y


def _monde(bloc, etiquette, classe, taches, comptes, r=1000, imperfection=0.0, **k):
    return {"parametres": {"bloc": bloc, "etiquette": etiquette, "taches": taches, "imperfection_temoin": imperfection},
            "classe": classe, "repetitions": r, "comptes": comptes, **k}


def _comptes(e, a, b, lectures=("pari", "student")):
    return {le.cle(l, al, c): v for l in lectures for al in (0.025, 0.05) for c, v in (("E", e), ("A", a), ("B", b))}


def test_indicateurs_sain_et_grille_incomplete():
    mondes = {"1": _monde("principal", "grille", "empreinte_seule", 400, _comptes(900, 10, 20)),
              "2": _monde("principal", "grille", "avance_vehiculaire", 400, _comptes(900, 30, 700)),
              "3": _monde("principal", "grille", "sabotage", 400, _comptes(950, 900, 500)),
              "4": _monde("principal", "grille", "sabotage", 400, _comptes(950, 700, 900)),
              "5": _monde("principal", "grille", "frontiere", 400, _comptes(300, 200, 400))}
    ind = le.indicateurs(mondes, 400)
    assert ind["A"]["faux_positifs_empreinte_seule"] == 0.01 and ind["B"]["faux_positifs_avance_vehiculaire"] == 0.7
    assert ind["A"]["couverture_de_puissance"] == 0.5 and ind["E"]["couverture_de_puissance"] == 1.0
    assert le.regle_de_choix(ind) == le.A_RETENUE
    assert ind["B"]["passages_frontiere_rapportes"] == 0.4
    del mondes["2"]
    with pytest.raises(GardeArret):
        le.indicateurs(mondes, 400)


def test_taux_garde():
    m = _monde("principal", "grille", "sabotage", 400, {"x": 5}, r=10)
    assert le.taux(m, "x") == 0.5
    with pytest.raises(GardeArret):
        le.taux(m, "absent")
    with pytest.raises(GardeArret):
        le.taux({**m, "comptes": {"x": 11}}, "x")


def test_concordance_reech():
    def m(pa, pb, ra, rb):
        return _monde("reechantillonnage", "grille", "sabotage", 400,
                      {le.cle("pari", 0.025, "A"): pa, le.cle("pari", 0.025, "B"): pb,
                       le.cle("reech", 0.025, "A"): ra, le.cle("reech", 0.025, "B"): rb})
    sain = {str(k): m(800, 300, 850, 320) for k in range(10)}
    assert le.concordance_reech(sain)["concordant"]
    artefact = {**sain, "a": m(800, 300, 300, 800), "b": m(800, 300, 300, 800)}
    assert not le.concordance_reech(artefact)["concordant"]
    with pytest.raises(GardeArret):
        le.concordance_reech({})


def test_alertes_de_symetrie():
    sain = {"1": _monde("principal", "grille", "sabotage", 400, _comptes(900, 800, 300)),
            "2": _monde("principal", "grille", "sabotage", 400, {**_comptes(900, 500, 900), le.cle("student", 0.025, "E"): 910})}
    assert le.alertes_de_symetrie(sain) == []
    artefact = {"1": _monde("principal", "grille", "sabotage", 400, _comptes(1000, 1000, 1000))}
    assert len(le.alertes_de_symetrie(artefact)) == 4


def test_validation_exigee_monde_absent():
    with pytest.raises(GardeArret):
        le.exiger_validation({})


def test_effectifs_minimaux_et_mesures():
    def m(t, v, classe="sabotage"):
        return {"parametres": {"bloc": "effectifs", "etiquette": "grille", "taches": t, "imperfection_temoin": 0.0,
                               "sabotage_blanche": 2.0, "empreinte_blanche": 0.0, "episodes_par_tache": 3},
                "classe": classe, "repetitions": 1000, "comptes": {le.cle("pari", 0.025, "A"): v}}
    mondes = {"a": m(100, 300), "b": m(200, 850), "c": m(400, 990)}
    (ligne,) = le.effectifs_minimaux(mondes, "A")
    assert ligne["taches_minimales"] == 200 and ligne["monotone_ensuite"]
    mondes["c"] = m(400, 700)
    assert not le.effectifs_minimaux(mondes, "A")[0]["monotone_ensuite"]
    with pytest.raises(GardeArret):
        le.effectifs_minimaux({"a": m(100, 300, "frontiere")}, "A")
    monde = {"parametres": {"bruit": "normal", "sabotage_blanche": 0.0, "sabotage_noire": 0.0}, "repetitions": 4,
             "sommes": {"rappel_blanche_seuil_temoin": 0.08, "taux_alerte_temoin": 0.04},
             "carres": {"rappel_blanche_seuil_temoin": 0.0016, "taux_alerte_temoin": 0.0004}}
    r = le.mesures_rapportees(monde)
    assert r["rappel_blanche_seuil_temoin"]["biais"] == pytest.approx(0.01)
    assert r["taux_alerte_temoin"]["biais"] is None
