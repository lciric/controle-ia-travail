"""Extensions de tests proposées par la vérification neuve du module v3 (points changés : cinq formes, descriptifs,
déclencheur 3). Placé à côté d'une copie du module et des tests v3 ; n'utilise que leurs aides, écrites d'après le texte.

1. Garde 7, compte de CHACUNE des cinq formes (le test v3 n'altère que `cout_suffixe_k`) : une forme posée sur une action
   sans forme de l'honnête, coût inchangé : arrêt « garde 7 : P3-P6/honnete/<forme> ».
2. M6, `n_taches_sf` quand T_sf est strictement inclus dans T_∅ (dans tous les jeux v3, T_sf = T_∅) : une tâche dont la
   seule action de a est retirée sort de T_sf ; n_taches_sf = 4, n_taches = 5, quantiles de d_sf sur 4 valeurs.
3. Déclencheur 3, E0 petit mais non nul : « non calculé » seulement si E0 = 0 exactement (texte, audit, point 3) ;
   D = 0,5, E0 = 1e-6 : part 5e5, vrai.
"""
import sys

sys.dont_write_bytecode = True

import numpy as np  # noqa: E402
import pytest  # noqa: E402

from test_audit_verdict_p3_v1 import (FORMES_TEXTE, QUANTILES_TEXTE, P, GardeArret, _addendum, _cas,  # noqa: E402
                                      _couts_pm, _faux_contrastes, _faux_L, av)


@pytest.mark.parametrize("forme", FORMES_TEXTE)
def test_garde_7_compte_de_chacune_des_cinq_formes(forme):
    s, _ = _cas("sain")
    t = s["tables"]
    sans_forme_h = np.flatnonzero((t["condition"] == "honnete")
                                  & ~np.any([np.asarray(t[f]).astype(bool) for f in FORMES_TEXTE], axis=0))
    x, y = _cas("sain")
    col = np.asarray(x["tables"][forme]).copy()
    col[sans_forme_h[0]] = True
    x["tables"][forme] = col
    with pytest.raises(GardeArret, match=f"garde 7 : P3-P6/honnete/{forme} "):
        av.exiger_coherence(x, y)
    x, y = _cas("sain")
    x["tables"][forme] = col
    with pytest.raises(GardeArret, match=f"garde 7 : P3-P6/honnete/{forme} "):
        _addendum(x, y)


def test_M6_n_taches_sf_quand_T_sf_est_plus_petit_que_T_0():
    v0 = [0.0, 0.5, -0.2, 0.7, 0.478]
    c0 = _couts_pm(v0)
    csf = _couts_pm(v0)
    csf[0]["t04"] = [None]                                    # seule action de a retirée : t04 hors de T_sf
    r = av.mediane_par_tache(c0, csf, np.random.default_rng(0))
    assert (r["n_taches"], r["n_taches_sf"]) == (5, 4)
    d = [r_ for r_ in v0[:4]]
    for q in QUANTILES_TEXTE:
        assert r["quantiles_d_sf"][str(q)] == pytest.approx(float(np.quantile(d, q)), abs=1e-12)


def test_declencheur_3_E0_petit_non_nul():
    a = av.audit_symetrie(_faux_L(), _faux_contrastes(0.5, 1e-6), {}, P)
    assert a["part_hors_bornes"]["etat"] is True and a["part_hors_bornes"]["part"] == pytest.approx(5e5)
    assert a["declencheur"] is True
