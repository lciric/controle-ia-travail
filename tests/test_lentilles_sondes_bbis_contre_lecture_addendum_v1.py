"""Deux essais demandés, sans blocage, par la contre-lecture du code de la première passe accordé à l'addendum de concentration
(`docs/notes/lecture-sondes-bbis-par-lentilles-v1/contre-lectures/contre-lecture-code-premiere-passe-addendum-v1.md`,
`7954d0fc54320d76ed63a634893063425683806dfb327acec1443e1ed6a96fd4`, § 5, corrections 2 et 3) :
- plusieurs directions marquées dans un même nul (addendum scellé `7c738708…`, § 12 bis, essai souhaitable) ;
- la ligne `ENTREES-LENTILLES-BBIS` placée après la ligne de l'addendum, mais d'heure antérieure (EC-4, artefact joué seul).
Aucun code n'est changé : `statistiques_v3` et `entrees_v3` sont ceux du commit `2e15977b`."""
from __future__ import annotations

import itertools

import numpy as np
import pytest

torch = pytest.importorskip("torch")

import test_lentilles_sondes_bbis_addendum_concentration_v2 as A  # noqa: E402  (jouets de registre de l'essai d'origine)
import test_lentilles_sondes_bbis_garde_egalite_v1 as G  # noqa: E402  (jouets de nuls de l'essai d'origine)
from controle_ia.lentilles_sondes_bbis import constantes_v1 as K  # noqa: E402
from controle_ia.lentilles_sondes_bbis import entrees_v3 as en  # noqa: E402
from controle_ia.lentilles_sondes_bbis import statistiques_v3 as st  # noqa: E402
from controle_ia.lentilles_sondes_bbis.constantes_v1 import Refus  # noqa: E402


def _nul_a_trois_directions_marquees():
    """Trois directions marquées du même nul, pour la famille jouet : (S_min, S_max) = (2, 3), (2, 3) et (3, 4)."""
    a_nul = G._nul_jouet("contre-lecture-plusieurs-directions-marquees")
    plus = G.FAMILLE[:2] + G._hors_famille(17)
    egaux = [G.FAMILLE[2]] + G._hors_famille(2, sauf=plus)
    G._marquer(a_nul, 5, plus, egaux)
    G._marquer(a_nul, 23, plus, egaux)
    plus3 = G.FAMILLE[:3] + G._hors_famille(16)
    G._marquer(a_nul, 41, plus3, [G.FAMILLE[3]] + G._hors_famille(1, sauf=plus3))
    return a_nul, st.resumer_nul(a_nul, G.MASQUES)


def test_plusieurs_directions_marquees_dans_un_meme_nul_bornes_egales_a_l_enumeration_conjointe():
    a_nul, resume = _nul_a_trois_directions_marquees()
    marquees = torch.nonzero(resume.marquee)[:, 0].tolist()
    assert marquees == [5, 23, 41] and resume.n_marquees == 3
    bornes = {j: (int(resume.familles_min["nombres"][j]), int(resume.familles_max["nombres"][j])) for j in marquees}
    assert bornes == {5: (2, 3), 23: (2, 3), 41: (3, 4)}
    libres = np.delete(resume.familles_max["nombres"].numpy(), marquees)
    for s_de_v, sous_s_min, sous_s_max in ((3, 1, 3), (4, 0, 1), (2, 3, 3), (5, 0, 0)):
        a = G._direction(G.FAMILLE[:s_de_v] + G._hors_famille(20 - s_de_v))
        t = st.lecture_signe(a, {K.NUL_SIGNES: (a_nul, resume)}, G.MASQUES, G.IDS, contexte=G.OU)["nuls"][K.NUL_SIGNES]
        f = t["familles"]["nombres"]
        base = 1 + int((libres >= s_de_v).sum())
        # énumération conjointe de tous les départages des trois directions : chaque S prend S_min ou S_max
        p = [(base + sum(int(s >= s_de_v) for s in choix)) / (G.M + 1) for choix in itertools.product(*bornes.values())]
        assert f["n"] == s_de_v and f["p_bas"] == min(p) == (base + sous_s_min) / (G.M + 1)
        assert f["p_haut"] == max(p) == (base + sous_s_max) / (G.M + 1) and f["p"] == f["p_haut"]
        assert f["attendu"] == pytest.approx(libres.mean()) and t["directions_nulles_marquees"] == 3


def test_artefact_une_seule_des_directions_marquees_comptee_serait_vue():
    """Si une seule des deux directions marquées de mêmes bornes entrait dans p_haut, l'écart p_haut − p_bas vaudrait 1/(M + 1)."""
    a_nul, resume = _nul_a_trois_directions_marquees()
    a = G._direction(G.FAMILLE[:3] + G._hors_famille(17))
    f = st.lecture_signe(a, {K.NUL_SIGNES: (a_nul, resume)}, G.MASQUES, G.IDS, contexte=G.OU)["nuls"][K.NUL_SIGNES]["familles"]["nombres"]
    assert f["p_haut"] - f["p_bas"] == pytest.approx(2 / (G.M + 1)) != pytest.approx(1 / (G.M + 1))


def test_ligne_des_entrees_placee_apres_l_addendum_mais_d_heure_anterieure_refus(tmp_path):
    """EC-4 : la ligne de l'addendum est placée avant `ENTREES-LENTILLES-BBIS`, mais son heure lui est postérieure : refus.
    Cas sain : la même ligne des entrées, à la même place, d'une heure postérieure à celle de l'addendum."""
    (tmp_path / "sain").mkdir()
    sain = A._registre(tmp_path / "sain", [A.SCELLEMENT, A.GO, A.ADDENDUM_SAIN, A.CODE, A.ENTREES])
    assert en.exiger_addendum(sain, en.ADDENDUM, en.EMPREINTE_ADDENDUM).heure == A.H2
    anterieure = ("ENTREES-LENTILLES-BBIS", A.H1, "diag/x/entrees-lentilles-bbis.json", "6" * 64)
    assert A.H1 < A.H2
    artefact = A._registre(tmp_path, [A.SCELLEMENT, A.GO, A.ADDENDUM_SAIN, A.CODE, anterieure])
    with pytest.raises(Refus, match="inscrite après ENTREES-LENTILLES-BBIS"):
        en.exiger_addendum(artefact, en.ADDENDUM, en.EMPREINTE_ADDENDUM)
    with pytest.raises(Refus, match="inscrite après ENTREES-LENTILLES-BBIS"):
        en.exiger_registre_propre(artefact)
