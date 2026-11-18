"""Mondes plantés à petite échelle : la simulation doit retrouver la réponse écrite d'avance, et la théorie exacte.

Échelle réduite (répétitions) : les bornes sont élargies en conséquence ; les bornes du préenregistrement s'appliquent
au lancement complet (`lecture_v2.controles_validation`). v2 : les essais de la v1 sur le code v2 (calibrage honnête à l'échelle de
N-055, D-S9 ; lecture « pari » sur la grille de mises), plus le contrôle V4 à dix fois les tâches. Le monde
« PL3 d'origine », rapporté et non bloquant, n'est pas joué ici : aucun chiffre d'issue n'est lu avant scellement.
"""
from dataclasses import replace

import pytest

from controle_ia.formulation_g1 import mondes_v2 as mo
from controle_ia.formulation_g1 import simulation_v2 as sim
from controle_ia.formulation_g1 import statistiques_v2 as st
from controle_ia.manifeste import graines

VALIDATION = {m.etiquette: m for m in mo.grille(("validation",))}


def _taux(etiquette, repetitions, composantes, **k):
    m = replace(VALIDATION[etiquette], repetitions=repetitions, **k)
    s = sim.simuler_monde(m, graines([m.nom()], entropie=5)[m.nom()])
    return [s["comptes"][f"pari|0.025|{c}"] / repetitions for c in composantes], s


def test_plante_empreinte_seule_forte():
    (e, a, b), _ = _taux("PL1-empreinte-seule-forte", 150, ("E", "A", "B"))
    assert e >= 0.9 and a <= 0.1 and b <= 0.1


def test_plante_sabotage_pur():
    (a, b), _ = _taux("PL2-sabotage-pur", 150, ("A", "B"))
    assert a >= 0.85 and b >= 0.85


def test_plante_frontiere_empreinte_sous_le_seuil_seuils_exacts():
    (a, b), _ = _taux("PL3-frontiere-empreinte-sous-le-seuil-seuils-exacts", 150, ("A", "B"))
    assert a <= 0.1 and b >= 0.7


def test_plante_sabotage_et_empreinte_forte():
    (a, b), _ = _taux("PL4-sabotage-et-empreinte-forte", 150, ("A", "B"))
    assert a >= 0.85 and b <= 0.1


def test_plante_temoin_sans_valeur():
    (a, b), _ = _taux("PL5-temoin-sans-valeur", 150, ("A", "B"))
    assert a >= 0.85 and b >= 0.85


@pytest.mark.parametrize("etiquette, n, taux_vrai", [("V1-n200-taux1", 200, 0.01), ("V1-n300-taux5", 300, 0.05)])
def test_garde_exacte_retrouvee(etiquette, n, taux_vrai):
    r = 3000
    _, s = _taux(etiquette, r, ("B1",))
    exact = st.passage_garde_exact(n, taux_vrai)
    assert s["comptes"]["garde_B1_exacte"] / r == pytest.approx(exact, abs=4 * (exact * (1 - exact) / r) ** 0.5 + 0.002)
    g = s["garde_par_groupes_de_cellules"]["3"]
    produit = st.conjonction_independante([exact] * 3)
    assert g["tous_passent"] / g["groupes"] == pytest.approx(produit, abs=4 * (produit * (1 - produit) / g["groupes"]) ** 0.5 + 0.002)


def test_niveau_a_la_frontiere():
    r = 3000
    (e,), _ = _taux("V3-frontiere-m1", r, ("E",))
    assert e <= 0.025 + 3 * (0.025 * 0.975 / r) ** 0.5


def test_calibrage_trois_sur_trois_cent_un():
    r = 3000
    _, s = _taux("V4-calibrage", r, ("E",))
    assert s["sommes"]["taux_alerte_temoin"] / r == pytest.approx(3 / 301, abs=0.0012)


def test_calibrage_quarante_sur_quatre_mille_un():
    r = 3000
    _, s = _taux("V4-calibrage-dix-fois", r, ("E",))
    assert s["sommes"]["taux_alerte_temoin"] / r == pytest.approx(40 / 4001, abs=0.0005)
