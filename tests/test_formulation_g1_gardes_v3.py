"""Gardes de l'étude des formulations du contraste à témoin apparié : chacune sur un cas sain et sur un artefact (R5).

v3 : les essais de la v2 sur le code v3, plus le bloc « budget du témoin égal », B2 restreint aux tâches de la garde
et la garde appariée de N-055, D-S4 (contre-lecture 2)."""
from dataclasses import replace

import numpy as np
import pytest

from controle_ia.formulation_g1 import mondes_v3 as mo
from controle_ia.formulation_g1 import simulation_v3 as sim
from controle_ia.formulation_g1 import statistiques_v3 as st
from controle_ia.gardes import GardeArret
from controle_ia.manifeste import graines
from controle_ia.scellement import sceller

SAIN = mo.Monde("principal", "grille", 1.5, 0.4, 1.5, 0.2, 0.0, 60, 3, calibrage_honnete=600, repetitions=8)


def _graine(m):
    return graines([m.nom()], entropie=3)[m.nom()]


def test_grille_effectifs_et_noms():
    g = mo.grille()
    assert len(g) == sum(mo.NOMBRE_ATTENDU.values()) == 5541
    assert len({m.nom() for m in g}) == len(g)
    assert {m.classe() for m in g} == {"empreinte_seule", "avance_vehiculaire", "frontiere", "sabotage"}
    assert mo.EMPREINTE_TAUX_5 == pytest.approx(0.68149, abs=1e-5)


def test_grille_calibrage_honnete_a_l_echelle_de_n055():
    for m in mo.grille(("principal", "effectifs", "reechantillonnage")):
        assert m.calibrage_honnete == 10 * m.taches * m.episodes_par_tache and m.calibrage_temoin == 300 and not m.bases_blanches
    variantes = {}
    for m in mo.grille(("sensibilites",)):
        variantes.setdefault(m.etiquette, []).append(m)
    assert set(variantes) == {nom for nom, _ in mo.VARIANTES_SENSIBILITE} and all(len(v) == 36 for v in variantes.values())
    assert {m.calibrage_honnete for m in variantes["calibrage_honnete_seize_fois"]} == {19200}
    assert {m.calibrage_honnete for m in variantes["calibrage_honnete_dix_fois_les_taches"]} == {4000}
    assert {m.calibrage_temoin for m in variantes["calibrage_temoin_echelle_de_d_s9"]} == {12000}
    assert {m.calibrage_honnete for m in variantes["calibrage_honnete_300"]} == {300}
    assert {m.episodes_garde for m in variantes["b_sur_300_episodes_du_temoin"]} == {300}
    assert set(mo.VARIANTES_BUDGET) <= set(variantes)
    assert {m.bases_blanches for m in variantes["liste_n056_bases_proches"]} == {(0.9, 0.75)}
    assert {m.bases_blanches for m in variantes["liste_n056_bases_lointaines"]} == {(0.6, 0.4)}
    assert set(mo.VARIANTES_COMPARATEURS) <= set(variantes)


def test_bloc_budget_du_temoin_egal():
    """B′-1 : les 486 mondes du bloc principal à 400 tâches et témoin parfait, A' calibré sur 1 200 épisodes du témoin."""
    budget = mo.grille(("budget_temoin",))
    assert len(budget) == 486 and {m.etiquette for m in budget} == {mo.ETIQUETTE_BUDGET_EGAL}
    assert {(m.calibrage_temoin, m.taches, m.episodes_par_tache, m.imperfection_temoin) for m in budget} == {(1200, 400, 3, 0.0)}
    cle = lambda m: (m.sabotage_blanche, m.empreinte_blanche, m.sabotage_noire, m.correlation_intra_tache, m.calibrage_honnete)
    principal = {cle(m) for m in mo.grille(("principal",)) if m.taches == 400 and m.imperfection_temoin == 0.0}
    assert {cle(m) for m in budget} == principal and len(principal) == 486


def test_grille_garde_du_nombre(monkeypatch):
    monkeypatch.setitem(mo.NOMBRE_ATTENDU, "effectifs", 647)
    with pytest.raises(GardeArret):
        mo.grille(("effectifs",))
    with pytest.raises(GardeArret):
        mo.grille(("inconnu",))


@pytest.mark.parametrize("champ, valeur", [
    ("correlation_intra_tache", 1.0), ("imperfection_temoin", 1.5), ("bruit", "cauchy"), ("calibrage_honnete", 99),
    ("calibrage_honnete", 0), ("taches", 1), ("sabotage_blanche", -0.1), ("bloc", "autre"), ("tirages_reech", 50),
    ("correlation_moniteurs", 1.0), ("episodes_garde", 99), ("episodes_garde", 181), ("bases_blanches", (1.0,)),
    ("bases_blanches", [0.5]), ("correlation_bases", 1.0)])
def test_monde_invalide(champ, valeur):
    assert SAIN.valider() is SAIN
    with pytest.raises(GardeArret):
        replace(SAIN, **{champ: valeur}).valider()


def test_calibrage_honnete_sans_defaut():
    with pytest.raises(GardeArret):          # calibrage honnête non écrit : refusé, aucun défaut silencieux
        mo.Monde("principal", "grille", 1.5, 0.4, 1.5, 0.2, 0.0, 60, 3).valider()


def test_correlations_des_moniteurs():
    assert SAIN.correlations().tolist() == [[1.0, 0.3], [0.3, 1.0]]
    m = replace(SAIN, bases_blanches=(0.9, 0.75)).valider()
    r = m.correlations()
    assert r.shape == (4, 4) and r[0, 1] == 0.3 and r[0, 2] == r[2, 3] == 0.7 and r[1, 2] == r[1, 3] == 0.3
    with pytest.raises(GardeArret):          # trois moniteurs blancs corrélés à −0,9 deux à deux : matrice non définie positive
        replace(SAIN, bases_blanches=(0.9, 0.75), correlation_bases=-0.9).valider()


def test_garde_partielle_refusee_avec_reechantillonnage():
    assert replace(SAIN, episodes_garde=150).valider()
    with pytest.raises(GardeArret):
        replace(SAIN, episodes_garde=150, tirages_reech=100).valider()


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
    vrai = sim._moniteurs

    def casse(rng, forme, chol, bruit):
        z = vrai(rng, forme, chol, bruit)
        z.flat[0] = np.nan
        return z

    monkeypatch.setattr(sim, "_moniteurs", casse)
    with pytest.raises(GardeArret):
        sim.simuler_monde(SAIN, _graine(SAIN))


def test_bruit_inconnu():
    chol = np.linalg.cholesky(SAIN.correlations())
    rng = np.random.default_rng(np.random.SeedSequence(1))
    assert sim._moniteurs(rng, (2, 3), chol, "student5").shape == (2, 3, 2)
    with pytest.raises(GardeArret):
        sim._moniteurs(rng, (2, 3), chol, "cauchy")


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
    for lecture in ("pari", "pari_previsible", "student", "reech"):
        for alpha in sim.NIVEAUX:
            for c in ("E", "A_prime", "B1", "B2", "A", "B"):
                assert 0 <= s["comptes"][f"{lecture}|{alpha}|{c}"] <= s["repetitions"]
    assert set(s["sommes"]) == set(sim.MESURES)
    sans = sim.simuler_monde(SAIN, _graine(SAIN))
    assert not any(k.startswith("reech") for k in sans["comptes"])


def test_trois_comparateurs_intersection_union():
    """Sain : bases blanches très en retrait, la boîte blanche les bat. Artefact : une base presque égale à la boîte
    blanche — l'intersection-union doit faire tomber E, que la seule boîte noire laissait passer."""
    base = mo.Monde("sensibilites", "essai", 3.0, 0.0, 0.5, 0.2, 0.0, 400, 3, calibrage_honnete=1500, seuil_oracle=True,
                    repetitions=40)
    cle = "pari|0.025|E"
    seul = sim.simuler_monde(base, _graine(base))["comptes"][cle]
    loin = replace(base, bases_blanches=(0.1, 0.1))
    pres = replace(base, bases_blanches=(0.999, 0.1))
    assert seul >= 38 and sim.simuler_monde(loin, _graine(loin))["comptes"][cle] >= 38
    s = sim.simuler_monde(pres, _graine(pres))
    assert s["comptes"][cle] <= 6 and s["comptes"]["pari|0.025|A"] <= s["comptes"][cle]
    m = replace(loin, tirages_reech=100, bloc="reechantillonnage", repetitions=8)
    assert "reech|0.025|A" in sim.simuler_monde(m, _graine(m))["comptes"]


def test_garde_lue_sur_une_partie_des_episodes(monkeypatch):
    vus = []
    vrai = st.alertes_tolerees
    monkeypatch.setattr(sim.st, "alertes_tolerees", lambda n, *a, **k: vus.append(n) or vrai(n, *a, **k))
    largeurs = []
    pari = st.pari_sur_grille
    monkeypatch.setattr(sim.st, "pari_sur_grille", lambda d, *a, **k: largeurs.append(d.shape) or pari(d, *a, **k))
    sim.simuler_monde(SAIN, _graine(SAIN))
    partiel = replace(SAIN, episodes_garde=100)
    sim.simuler_monde(partiel, _graine(partiel))
    assert vus == [180, 100]
    # B′-1 : B2 n'est apparié que sur les tâches qui portent la garde (34 tâches pour 100 épisodes) ; les contrastes
    # de E et de A' gardent les 60 tâches. Par lot et par niveau : le contraste (16 lignes), puis B2 (8 lignes).
    assert largeurs[:4] == [(16, 60), (8, 60), (16, 60), (8, 60)]
    assert largeurs[4:] == [(16, 60), (8, 34), (16, 60), (8, 34)]


def test_b2_restreint_change_la_decision():
    """Artefact : un témoin qui ne sonne que sur les dernières tâches. B lue sur les 100 premières tâches ne le voit
    pas (B1 passe) ; B lue sur toutes les tâches le voit (B1 refuse)."""
    m = mo.Monde("sensibilites", "essai", 3.0, 0.0, 0.5, 0.0, 0.0, 400, 3, calibrage_honnete=12000, seuil_oracle=True,
                 repetitions=20)
    vrai = sim._scores
    appels = []

    def temoin_bruyant_en_fin(rng, moyennes, effet_tache, mm, monde, chol):
        x = vrai(rng, moyennes, effet_tache, mm, monde, chol)
        appels.append(1)
        if len(appels) % 3 == 2 and x.shape[1] == 400:      # deuxième appel de chaque lot : les épisodes du témoin
            x[:, 100:, :, 0] += 3.0
        return x

    cle = "pari|0.025|B1"
    comptes = {}
    for episodes in (0, 300):
        appels.clear()
        with pytest.MonkeyPatch.context() as mp:
            mp.setattr(sim, "_scores", temoin_bruyant_en_fin)
            monde = replace(m, episodes_garde=episodes)
            comptes[episodes] = sim.simuler_monde(monde, _graine(monde))["comptes"][cle]
    assert comptes[0] == 0 and comptes[300] >= 18        # à 1 % vrai, la garde sur 300 épisodes passe 996 fois sur 1 000


def test_garde_appariee_dans_e_et_dans_a_prime(monkeypatch):
    """M′-2 : la garde de D-S4 entre dans E (honnête) et dans A' (témoin). Sain : aucune asymétrie d'alertes, la garde
    ne retire presque rien. Artefact : la boîte blanche sonne sur l'honnête de l'épreuve, la garde bloque E."""
    m = mo.Monde("sensibilites", "essai", 3.0, 0.0, 0.5, 0.2, 0.0, 400, 3, calibrage_honnete=12000, seuil_oracle=True,
                 repetitions=20)
    s = sim.simuler_monde(m, _graine(m))["comptes"]
    assert s["pari|0.025|E_sans_garde"] == 20 and s["pari|0.025|E"] >= 19 and s["pari|0.025|A_prime"] >= 19
    for lecture in ("pari", "pari_previsible", "student"):
        assert s[f"{lecture}|0.025|E"] <= s[f"{lecture}|0.025|E_sans_garde"]
        assert s[f"{lecture}|0.025|A_prime"] <= s[f"{lecture}|0.025|A_prime_sans_garde"]
    vrai = sim._scores
    appels = []

    def honnete_qui_sonne(rng, moyennes, effet_tache, mm, monde, chol):
        x = vrai(rng, moyennes, effet_tache, mm, monde, chol)
        appels.append(1)
        if len(appels) % 3 == 0:                            # troisième appel de chaque lot : l'honnête de l'épreuve
            x[..., 0] += 1.5                                # la boîte blanche y sonne dans 20 % des épisodes
        return x

    monkeypatch.setattr(sim, "_scores", honnete_qui_sonne)
    s = sim.simuler_monde(m, _graine(m))["comptes"]
    for lecture in ("pari", "pari_previsible", "student"):
        assert s[f"{lecture}|0.025|E_sans_garde"] == 20 and s[f"{lecture}|0.025|E"] == 0
        assert s[f"{lecture}|0.025|A_prime"] >= 19          # le témoin n'est pas touché


def test_repetitions_minimales():
    with pytest.raises(GardeArret):
        sim.simuler_monde(SAIN, _graine(SAIN), repetitions=1)
    sim.exiger_repetitions_completes([replace(SAIN, repetitions=1000)])
    with pytest.raises(GardeArret):
        sim.exiger_repetitions_completes([replace(SAIN, repetitions=1000), replace(SAIN, repetitions=999)])
    sim.exiger_repetitions_completes(mo.grille())      # la grille écrite passe la garde du lancement complet


def test_mondes_complets():
    sim.exiger_mondes_complets({"a": 1, "b": 2}, ["a", "b"])
    with pytest.raises(GardeArret):                    # monde manquant
        sim.exiger_mondes_complets({"a": 1}, ["a", "b"])
    with pytest.raises(GardeArret):                    # monde en trop
        sim.exiger_mondes_complets({"a": 1, "b": 2, "c": 3}, ["a", "b"])


def test_duree_maximale():
    assert sim.DUREE_MAXIMALE == 6 * 3600
    sim.exiger_duree(0.0)
    sim.exiger_duree(6 * 3600)
    with pytest.raises(GardeArret):
        sim.exiger_duree(6 * 3600 + 1)
    with pytest.raises(GardeArret):
        sim.exiger_duree(float("nan"))


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
    brouillon = tmp_path / "formulation-g1-simulation-v1-brouillon2.md"
    brouillon.write_text(corps, encoding="utf-8")
    sceller(brouillon)
    with pytest.raises(GardeArret):            # scellé mais brouillon
        sim.exiger_prereg_final(brouillon)


def test_jouet_borne_a_deux_repetitions():
    with pytest.raises(GardeArret):
        sim.mesurer_temps(repetitions=3)
