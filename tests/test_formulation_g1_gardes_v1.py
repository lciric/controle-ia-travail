"""Gardes de l'étude des formulations du contraste à témoin apparié : chacune sur un cas sain et sur un artefact (R5)."""
from dataclasses import replace

import numpy as np
import pytest

from controle_ia.formulation_g1 import mondes_v1 as mo
from controle_ia.formulation_g1 import simulation_v1 as sim
from controle_ia.gardes import GardeArret
from controle_ia.manifeste import graines
from controle_ia.scellement import sceller

SAIN = mo.Monde("principal", "grille", 1.5, 0.4, 1.5, 0.2, 0.0, 60, 3, repetitions=8)


def _graine(m):
    return graines([m.nom()], entropie=3)[m.nom()]


def test_grille_effectifs_et_noms():
    g = mo.grille()
    assert len(g) == sum(mo.NOMBRE_ATTENDU.values()) == 3901
    assert len({m.nom() for m in g}) == len(g)
    assert {m.classe() for m in g} == {"empreinte_seule", "avance_vehiculaire", "sabotage"}
    assert mo.EMPREINTE_TAUX_5 == pytest.approx(0.68149, abs=1e-5)


def test_grille_garde_du_nombre(monkeypatch):
    monkeypatch.setitem(mo.NOMBRE_ATTENDU, "effectifs", 647)
    with pytest.raises(GardeArret):
        mo.grille(("effectifs",))
    with pytest.raises(GardeArret):
        mo.grille(("inconnu",))


@pytest.mark.parametrize("champ, valeur", [
    ("correlation_intra_tache", 1.0), ("imperfection_temoin", 1.5), ("bruit", "cauchy"), ("calibrage_honnete", 99),
    ("taches", 1), ("sabotage_blanche", -0.1), ("bloc", "autre"), ("tirages_reech", 50), ("correlation_moniteurs", 1.0)])
def test_monde_invalide(champ, valeur):
    assert SAIN.valider() is SAIN
    with pytest.raises(GardeArret):
        replace(SAIN, **{champ: valeur}).valider()


def test_seuil_exact_reserve_au_bruit_normal():
    assert replace(SAIN, seuil_oracle=True).valider()
    with pytest.raises(GardeArret):
        replace(SAIN, seuil_oracle=True, bruit="student5").valider()


def test_scores_non_finis():
    sim.exiger_finis("sain", np.zeros(3))
    with pytest.raises(GardeArret):
        sim.exiger_finis("artefact", np.array([0.0, np.inf]))


def test_lot_refuse_un_tirage_non_fini(monkeypatch):
    sim.simuler_monde(SAIN, _graine(SAIN))
    vrai = sim._paire

    def casse(rng, forme, r, bruit):
        z = vrai(rng, forme, r, bruit)
        z.flat[0] = np.nan
        return z

    monkeypatch.setattr(sim, "_paire", casse)
    with pytest.raises(GardeArret):
        sim.simuler_monde(SAIN, _graine(SAIN))


def test_graine_alteree():
    g = _graine(SAIN)
    sim.simuler_monde(SAIN, g)
    with pytest.raises(GardeArret):
        sim.simuler_monde(SAIN, {**g, "etat_controle": [1, 2]})


def test_rejouabilite_et_derivation_par_monde():
    a = sim.simuler_monde(SAIN, _graine(SAIN))
    b = sim.simuler_monde(SAIN, _graine(SAIN))
    assert a == b
    autre = replace(SAIN, empreinte_blanche=0.8)
    assert _graine(autre)["spawn_key"] != _graine(SAIN)["spawn_key"]


def test_structure_des_sorties():
    m = replace(SAIN, tirages_reech=100, bloc="reechantillonnage")
    s = sim.simuler_monde(m, _graine(m))
    for lecture in ("pari", "student", "reech"):
        for alpha in sim.NIVEAUX:
            for c in ("E", "A_prime", "B1", "B2", "A", "B"):
                assert 0 <= s["comptes"][f"{lecture}|{alpha}|{c}"] <= s["repetitions"]
    assert set(s["sommes"]) == set(sim.MESURES)
    sans = sim.simuler_monde(SAIN, _graine(SAIN))
    assert not any(k.startswith("reech") for k in sans["comptes"])


def test_repetitions_minimales():
    with pytest.raises(GardeArret):
        sim.simuler_monde(SAIN, _graine(SAIN), repetitions=1)


def test_prereg_final_exige(tmp_path):
    corps = "# Préenregistrement\n\n" + "".join(
        f"## {s}\n\ntexte {'a' * 64} {'b' * 64}\n\n" for s in
        ("Hypothèse", "Prédiction chiffrée et signe attendu", "Métrique", "Seuil", "Plan d'analyse",
         "Critères de lecture gelés", "Liste d'arrêt", "Contre-lecture"))
    final = tmp_path / "formulation-g1-simulation-v1.md"
    final.write_text(corps, encoding="utf-8")
    with pytest.raises(GardeArret):            # non scellé
        sim.exiger_prereg_final(final)
    sceller(final)
    assert len(sim.exiger_prereg_final(final)) == 64
    brouillon = tmp_path / "formulation-g1-simulation-v1-brouillon1.md"
    brouillon.write_text(corps, encoding="utf-8")
    sceller(brouillon)
    with pytest.raises(GardeArret):            # scellé mais brouillon
        sim.exiger_prereg_final(brouillon)


def test_jouet_borne_a_deux_repetitions():
    with pytest.raises(GardeArret):
        sim.mesurer_temps(repetitions=3)
