"""Pièce 8 — gabarit d'inventaire (§ 6) : inventaire conforme ; champ de résultat, champ absent, valeur hors liste refusés."""
import json

import pytest

from controle_ia.hasard_defenseur_v1 import inventaire_v1 as I
from controle_ia.hasard_defenseur_v1.erreurs_v1 import RefusInventaire


def _course(**kw):
    c = {"identifiant_tache": "tache-1", "organisme": "saboteur", "regime": "non observé", "affectation_par": "harnais",
         "affectation_comment": "par lot", "graine": "absente", "engagement": "absent", "unite_affectation": "lot",
         "episodes_par_regime_et_tache": 4, "texte_etiquette": "[cadre : sans surveillance]",
         "ordre_et_date_passage": "inconnu", "juge_du_dommage": "inconnu", "episodes_manquants": 0}
    c.update(kw)
    return c


def test_gabarit_et_cas_sain():
    g = json.loads(I.gabarit())
    assert set(g["courses"][0]) == set(I.CHAMPS)
    d = I.ce_que_cela_decide({"courses": [_course(), _course(identifiant_tache="tache-2", organisme="jumeau")]})
    assert d["decisions"] and "aucune p-valeur de permutation n'est permise" in d["decisions"][0]
    assert d["taches_disponibles"] == 2 and d["p_valeur_permutation_interdite"] == ["tache-1", "tache-2"]
    d = I.ce_que_cela_decide({"courses": [_course(affectation_comment="tiré", graine="présente", engagement="présent")]})
    assert d["decisions"] == [] and d["p_valeur_permutation_interdite"] == []


def test_artefact_champ_de_resultat_refuse():
    with pytest.raises(RefusInventaire):
        I.ce_que_cela_decide({"courses": [_course(dommage_moyen=0.2)]})


def test_aucun_repli_silencieux():
    c = _course()
    del c["juge_du_dommage"]
    with pytest.raises(RefusInventaire):
        I.ce_que_cela_decide({"courses": [c]})
    with pytest.raises(RefusInventaire):
        I.ce_que_cela_decide({"courses": [_course(regime="peut-être")]})
    with pytest.raises(RefusInventaire):
        I.ce_que_cela_decide({"courses": [_course(texte_etiquette="  ")]})
    with pytest.raises(RefusInventaire):
        I.ce_que_cela_decide({"courses": []})
