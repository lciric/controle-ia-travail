"""Essais demandés par l'addendum « concentration » du texte scellé (EC-5), **préparés avant son scellement** : l'artefact de
taux à petite taille et les 41 bornes de calibration de son § 7. Addendum lu au brouillon candidat
`prereg/lecture-sondes-bbis-par-lentilles-v1-addendum-concentration-v1.md` (`0a862760…`) ; à accorder au texte scellé."""
from __future__ import annotations

import pytest

torch = pytest.importorskip("torch")

from controle_ia.lentilles_sondes_bbis import audits_v1 as au  # noqa: E402
from controle_ia.lentilles_sondes_bbis import statistiques_v1 as origine  # noqa: E402
from controle_ia.lentilles_sondes_bbis import statistiques_v2 as st  # noqa: E402

# Addendum, § 7 : nombre k de jeux de 200 témoins mis en commun → [q_bas, q_haut] ; valeurs recopiées du texte.
BORNES_JEUX_DE_200 = {
    1: (1, 24), 2: (6, 39), 3: (12, 53), 4: (18, 66), 5: (26, 79), 6: (33, 92), 7: (41, 104), 8: (48, 116), 9: (56, 128),
    10: (64, 140), 11: (72, 152), 12: (81, 164), 13: (89, 176), 14: (97, 187), 15: (106, 199), 16: (114, 210), 17: (123, 222),
    18: (131, 233), 19: (140, 245), 20: (149, 256), 21: (157, 267), 22: (166, 279), 23: (175, 290), 24: (183, 301),
    25: (192, 312), 26: (201, 323), 27: (210, 335), 28: (219, 346), 29: (228, 357), 30: (236, 368), 31: (245, 379),
    32: (254, 390), 33: (263, 401), 34: (272, 412), 35: (281, 423), 36: (290, 434), 37: (299, 445), 38: (308, 456),
    39: (317, 467), 40: (326, 478)}
BORNE_UN_JEU_DE_1000 = (23, 85)


def test_les_41_bornes_de_l_addendum_egales_a_celles_du_code():
    assert au.bornes_calibration([1000]) == BORNE_UN_JEU_DE_1000
    assert sorted(BORNES_JEUX_DE_200) == list(range(1, 41))
    for k, attendue in BORNES_JEUX_DE_200.items():
        assert au.bornes_calibration([200] * k) == attendue, k


def test_artefact_une_borne_decalee_d_un_cran_est_vue():
    """Loi faussée d'un cran (99 au lieu de 100 directions nulles au-dessus du seuil) : des bornes changent."""
    def bornes_faussees(jeux):
        pmf = [1.0]
        for n in jeux:
            pmf = au.convoluer(pmf, au.pmf_beta_binomiale(n, 99, 1902))
        return au.bornes(pmf)
    assert any(bornes_faussees([200] * k) != b for k, b in BORNES_JEUX_DE_200.items())


def _taux(module, repliques: int = 2000, m: int = 19, jetons: int = 128) -> float:
    """Part des témoins à p ≤ 0,05 : scores gaussiens indépendants, `m` directions nulles, un témoin frais par réplique."""
    g = torch.Generator().manual_seed(20261119)
    petits = 0
    for _ in range(repliques):
        nul, temoin = torch.randn(jetons, m, generator=g), torch.randn(jetons, 1, generator=g)
        petits += int(module.p_temoins(temoin, module.resumer_nul(nul, {}))[0] <= 0.05)
    return petits / repliques


def test_taux_a_petite_taille_sous_la_statistique_corrigee():
    """Addendum, EC-5 : M = 19, 128 jetons, 2 000 répliques : part entre 0,03 et 0,065 (≈ 0,045 attendu)."""
    assert 0.03 <= _taux(st) <= 0.065


def test_artefact_de_taux_a_petite_taille_sous_la_statistique_d_origine():
    """La statistique du texte d'origine (direction nulle comprise) : part ≈ 0,47, loin hors de l'intervalle."""
    taux = _taux(origine)
    assert taux > 0.3 and not 0.03 <= taux <= 0.065
