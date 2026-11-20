"""Essais du banc de juges scriptés de la ligne 3, étage 1 — v1.

Gardes de la liste d'arrêt qui touchent l'étage 1, chacune sur un cas sain et sur un artefact (R5) ; essais de
formules de l'annexe A (grand n, corrélation estimée contre valeur plantée par loi ; erreur équilibrée contre les
formules du § 0 ; taux exacts du double rendu et écarts vrais du monde de puissance contre
`calcul_predictions_ligne_3_v2.py` et sa sortie) ; garde des graines ; essai final : aucune graine des racines
2026111931 à 2026111937 dérivée dans le processus des essais.

Seule la racine des essais (2026111930) est dérivée. Lancement :
    TMPDIR=<dossier de travail> PYTHONDONTWRITEBYTECODE=1 python3 -B -m pytest -q CE_FICHIER
Variables facultatives : BANC_LIGNE_3_CHEMIN (copie du banc à éprouver, pour le contrôle des défauts réintroduits),
CHRONOMETRAGE_LIGNE_3_CHEMIN, CALCUL_PREDICTIONS_LIGNE_3 (chemin du calcul des prédictions v2).
Développeur, modèle L′.
"""
from __future__ import annotations

import contextlib
import hashlib
import importlib.util
import io
import json
import os
import re
import sys
from pathlib import Path

import numpy as np
import pytest

# --- Enregistrement de toute SeedSequence créée par du code Python dans ce processus (essai final) ---------------
_ENTROPIES_CREEES: list = []
_SEED_SEQUENCE_D_ORIGINE = np.random.SeedSequence


class _SeedSequenceEnregistree(_SEED_SEQUENCE_D_ORIGINE):
    def __init__(self, entropy=None, *args, **kwargs):
        _ENTROPIES_CREEES.append(entropy)
        super().__init__(entropy, *args, **kwargs)


np.random.SeedSequence = _SeedSequenceEnregistree

ICI = Path(__file__).resolve().parent
CHEMIN_BANC = Path(os.environ.get("BANC_LIGNE_3_CHEMIN", str(ICI / "banc_juges_scriptes_ligne_3_v1.py")))
CHEMIN_CHRONO = Path(os.environ.get("CHRONOMETRAGE_LIGNE_3_CHEMIN", str(ICI / "chronometrer_banc_ligne_3_v1.py")))
DEPOT_PAR_DEFAUT = Path("/home/user/controle-ia-travail/docs/notes/organisme-auto-conception-v1/epreuves-v9/"
                        "ligne-3-votes-effectifs-juges")
EMPREINTE_CALCUL_V2 = "802d4dd26d66ead35326cef2d77c8a55e12c11b89a4ddbce4d9a115927428dc6"
EMPREINTE_SORTIE_CALCUL_V2 = "2cf1eba7e4fce530e14b4045574f7c4ff97fdb94367aef740c5c274a14eae724"
RACINES_INTERDITES_AUX_ESSAIS = tuple(range(2026111931, 2026111938))


def _sha256(chemin):
    return hashlib.sha256(Path(chemin).read_bytes()).hexdigest()


def _charger(nom, chemin):
    if nom in sys.modules:
        return sys.modules[nom]
    spec = importlib.util.spec_from_file_location(nom, chemin)
    module = importlib.util.module_from_spec(spec)
    sys.modules[nom] = module
    spec.loader.exec_module(module)
    return module


banc = _charger("banc_juges_scriptes_ligne_3_v1", CHEMIN_BANC)


def _chemin_calcul(nom):
    env = os.environ.get("CALCUL_PREDICTIONS_LIGNE_3")
    if env and nom.endswith(".py"):
        return Path(env)
    for base in (ICI.parent, DEPOT_PAR_DEFAUT):
        if (base / nom).is_file():
            return base / nom
    raise AssertionError(f"pièce de référence introuvable : {nom} (aucun repli silencieux)")


def _calcul():
    chemin = _chemin_calcul("calcul_predictions_ligne_3_v2.py")
    assert _sha256(chemin) == EMPREINTE_CALCUL_V2, "empreinte du calcul des prédictions v2 inattendue"
    return _charger("calcul_predictions_ligne_3_v2", chemin)


def _sortie_calcul():
    chemin = _chemin_calcul("calcul-predictions-ligne-3-v2.json")
    assert _sha256(chemin) == EMPREINTE_SORTIE_CALCUL_V2, "empreinte de la sortie du calcul v2 inattendue"
    return json.loads(Path(chemin).read_text(encoding="utf-8"))


def _gens(tache, nombre):
    return banc.generateurs(banc.RACINE_ESSAIS, tache, nombre)


# =================================================================================================================
# Graines
# =================================================================================================================
@pytest.mark.parametrize("racine", [2026111931, 2026111932, 2026111933])
def test_graines_racines_decisives_refusees_sans_autorisation(racine):
    avant = len(banc.JOURNAL_GRAINES)
    with pytest.raises(banc.RefusGraine):
        banc.generateurs(racine, "essais_gardes", 1)
    with pytest.raises(banc.RefusGraine):
        banc.Contexte("decisif").tirages("estimateur_et_agregation", 1)
    assert len(banc.JOURNAL_GRAINES) == avant


def test_graines_autorisation_fausse_refusee(tmp_path):
    additif = tmp_path / "additif-factice.md"
    additif.write_text("additif factice\n", encoding="utf-8")
    avant = len(banc.JOURNAL_GRAINES)
    for emp in ("0" * 64, "court", None):
        with pytest.raises(banc.RefusGraine):
            banc.generateurs(banc.RACINE_ETAGE_1_DECISIF, "essais_gardes", 1, banc.Autorisation(additif, emp))
    with pytest.raises(banc.RefusGraine):
        banc.generateurs(banc.RACINE_ETAGE_1_DECISIF, "essais_gardes", 1,
                         banc.Autorisation(tmp_path / "absent.md", _sha256(additif)))
    assert len(banc.JOURNAL_GRAINES) == avant


@pytest.mark.parametrize("racine", list(range(2026111934, 2026111938)))
def test_graines_racines_etage_2_toujours_refusees(racine, tmp_path):
    additif = tmp_path / "additif.md"
    additif.write_text("x\n", encoding="utf-8")
    with pytest.raises(banc.RefusGraine):
        banc.generateurs(racine, "essais_gardes", 1, banc.Autorisation(additif, _sha256(additif)))


def test_graines_table_gelee_et_cle_entiere():
    valeurs = list(banc.TABLE_CLES.values())
    assert all(isinstance(v, int) and not isinstance(v, bool) for v in valeurs)
    assert len(set(valeurs)) == len(valeurs)
    with pytest.raises(banc.RefusGraine):
        banc.generateurs(banc.RACINE_ESSAIS, "tache_absente", 1)
    with pytest.raises(banc.RefusGraine):
        banc.generateurs(banc.RACINE_ESSAIS, "essais_gardes", 0)
    a = _gens("essais_gardes", 2)
    b = _gens("essais_gardes", 2)
    assert a[0].random() == b[0].random()
    assert a[1].random() != a[0].random()
    assert banc.JOURNAL_GRAINES[-1]["racine"] == banc.RACINE_ESSAIS


def test_cli_decisive_refusee_sans_autorisation_valide(tmp_path):
    avant = len(banc.JOURNAL_GRAINES)
    sortie = tmp_path / "sortie"
    with pytest.raises(banc.RefusGraine):
        banc.main(["--decisif", "--autorisation-additif", str(tmp_path / "absent.md"),
                   "--empreinte-additif", "0" * 64, "--sortie", str(sortie)])
    assert not sortie.exists()
    assert len(banc.JOURNAL_GRAINES) == avant


# =================================================================================================================
# Garde « estimateur » (liste d'arrêt)
# =================================================================================================================
def test_garde_estimateur_cas_sain_deux_juges_independants():
    rng = _gens("essais_gardes", 1)[0]
    n_c = 100000
    y = banc.classes(n_c)
    p = np.array([0.2, 0.2])
    E = banc.tirer_erreurs(1, rng, 1, n_c, p, p, 0.0)
    rho, indef = banc.rho_moyenne(banc.cov_intra_classes(E, y))
    assert not indef[0]
    assert abs(rho[0]) <= banc.TOL_BIAIS


def test_garde_estimateur_artefact_juge_duplique():
    rng = _gens("essais_gardes", 2)[1]
    n_c = 500
    y = banc.classes(n_c)
    p = np.array([0.2])
    E1 = banc.tirer_erreurs(1, rng, 3, n_c, p, p, 0.0)
    E = np.concatenate([E1, E1], axis=2)
    rho, indef = banc.rho_moyenne(banc.cov_intra_classes(E, y))
    v = banc.votes_effectifs(rho, 2)
    assert not indef.any()
    assert np.all(v == 1.0)


def test_garde_estimateur_artefact_juge_sans_erreur_indefini_jamais_zero():
    rng = _gens("essais_gardes", 3)[2]
    n_c = 200
    y = banc.classes(n_c)
    E = banc.tirer_erreurs(1, rng, 5, n_c, np.array([0.2, 0.0]), np.array([0.2, 0.0]), 0.3)
    S = banc.cov_intra_classes(E, y)
    rho, indef = banc.rho_moyenne(S)
    assert indef.all()
    assert np.all(np.isnan(rho))
    r12, i12 = banc.rho_paire(S, 0, 1)
    assert i12.all() and np.all(np.isnan(r12))
    assert np.all(np.isnan(banc.votes_effectifs(rho, 2)))
    lo, hi, n_ind = banc.intervalles_rho_moyenne(E, y, rng, 20)
    assert np.all(np.isnan(lo)) and np.all(np.isnan(hi)) and np.all(n_ind == 20)
    q = banc.qualite_estimateur(rho, indef, lo, hi, 0.3)
    assert q["part_indefini"] == 1.0 and q["tient"] is False and q["biais"] is None


def test_gardes_deterministes_avant_tirage():
    banc.verifier_gardes_avant_tirage()


def test_audit_trop_propre_cellule_sans_replique_hors_intervalle():
    rho = np.array([0.30, 0.31, 0.29])
    indef = np.zeros(3, dtype=bool)
    q = banc.qualite_estimateur(rho, indef, rho - 0.5, rho + 0.5, 0.3)
    assert q["audit_trop_propre_aucune_replique_hors_intervalle"] is True and q["couverture"] == 1.0
    q = banc.qualite_estimateur(rho, indef, rho - 0.001, rho + 0.001, 0.3)
    assert q["audit_trop_propre_aucune_replique_hors_intervalle"] is False


# =================================================================================================================
# Comptes de configurations et rééchantillonnage stratifié
# =================================================================================================================
@pytest.mark.parametrize("J", [2, 5])
def test_covariance_depuis_comptes_egale_covariance_directe(J):
    rng = _gens("essais_formules", 1)[0]
    n_c = 60
    y = banc.classes(n_c)
    p = np.linspace(0.1, 0.3, J)
    E = banc.tirer_erreurs(1, rng, 7, n_c, p, p, 0.4)
    direct = banc.cov_intra_classes(E, y)
    X = banc.motifs(J)
    par_comptes = banc.cov_depuis_comptes(banc.comptes_configurations(E[:, y]),
                                          banc.comptes_configurations(E[:, ~y]), X)
    assert np.allclose(direct, par_comptes, atol=1e-12)


def test_reechantillonnage_stratifie_garde_la_taille_des_classes():
    rng = _gens("essais_formules", 2)[1]
    n_c = 25
    y = banc.classes(n_c)
    E = banc.tirer_erreurs(1, rng, 4, n_c, np.array([0.2, 0.3]), np.array([0.1, 0.2]), 0.3)
    cb = banc.comptes_configurations(E[:, y])
    tirages = banc.tirer_comptes(rng, cb, 100)
    assert tirages.shape == (100, 4, 4)
    assert np.all(tirages.sum(axis=-1) == n_c)
    assert np.all(tirages[..., cb == 0] == 0)


def test_partage_par_moitie_stratifie():
    for n_c in (25, 50, 100, 200):
        cal, lec = banc.indices_moities(n_c)
        y = banc.classes(n_c)
        assert len(cal) == len(lec) == n_c
        assert set(cal).isdisjoint(lec) and len(set(cal) | set(lec)) == 2 * n_c
        assert abs(int(y[cal].sum()) - int((~y[cal]).sum())) <= 1


# =================================================================================================================
# Garde « formules » : grand n, corrélation estimée contre valeur plantée, par loi
# =================================================================================================================
CAS_FORMULES = [
    (1, 2, "egal_0.2", 0.6), (1, 2, "inegal", 0.6), (1, 2, "indulgent", 0.9), (1, 5, "inegal", 0.45),
    (2, 2, "egal_0.2", 0.6), (2, 2, "severe", 0.3), (2, 2, "inegal", 0.9),
    (3, 2, "egal_0.2", 0.3), (3, 2, "egal_0.2", 0.75),
    (4, 5, "egal_0.2", 0.6), (4, 5, "severe", 0.9),
]


@pytest.mark.parametrize("loi,J,nom,rho", CAS_FORMULES)
def test_formules_correlation_estimee_contre_valeur_plantee(loi, J, nom, rho):
    rng = _gens("essais_formules", len(CAS_FORMULES))[CAS_FORMULES.index((loi, J, nom, rho))]
    n_c = 150000
    y = banc.classes(n_c)
    p_b, p_m = banc.profil(nom, J)
    E = banc.tirer_erreurs(loi, rng, 1, n_c, p_b, p_m, rho)
    plantee, paires = banc.valeur_plantee(loi, p_b, p_m, rho)
    S = banc.cov_intra_classes(E, y)
    est, indef = banc.rho_moyenne(S)
    assert not indef[0]
    assert abs(est[0] - plantee) < 0.012
    for j in range(J):
        for k in range(j + 1, J):
            r, _ = banc.rho_paire(S, j, k)
            assert abs(r[0] - paires[j, k]) < 0.02


def test_formules_valeurs_plantees_exactes_connues():
    p = np.full(2, 0.2)
    for rho in banc.RHOS:
        assert banc.valeur_plantee(1, p, p, rho)[0] == pytest.approx(rho, abs=1e-12)
        if rho <= banc.RHO_MAX_LOI_3:
            assert banc.valeur_plantee(3, p, p, rho)[0] == pytest.approx(rho, abs=1e-12)
    p5 = np.full(5, 0.2)
    for rho in banc.RHOS:
        assert banc.valeur_plantee(4, p5, p5, rho)[0] == pytest.approx(7 * rho / 15, abs=1e-12)
    for r in (0.15, 0.6, 0.9):
        assert banc.valeur_plantee(2, p, p, r)[0] < r - 0.02
    assert banc.valeur_plantee(2, p, p, 0.0)[0] == 0.0


def test_formules_artefact_valeur_plantee_prise_sur_la_grille_a_taux_inegaux():
    p_b, p_m = banc.profil("inegal", 2)
    plantee, _ = banc.valeur_plantee(1, p_b, p_m, 0.6)
    assert abs(plantee - 0.6) > 0.05
    rng = _gens("essais_formules", 3)[2]
    n_c = 150000
    E = banc.tirer_erreurs(1, rng, 1, n_c, p_b, p_m, 0.6)
    est, _ = banc.rho_moyenne(banc.cov_intra_classes(E, banc.classes(n_c)))
    assert abs(est[0] - 0.6) > 0.05 and abs(est[0] - plantee) < 0.012


def test_formules_artefact_loi_codee_avec_une_correlation_fausse():
    """Loi 1 fautive (le choc tiré par juge et non par témoin) : l'écart à la valeur plantée est visible."""
    rng = _gens("essais_formules", 4)[3]
    n_c, J, rho = 150000, 2, 0.6
    p = np.full(J, 0.2)

    def loi_1_fautive(m):
        commun = rng.random((1, m, 1))
        propre = rng.random((1, m, J))
        choc = rng.random((1, m, J)) < rho
        return np.where(choc, commun, propre) < p

    E = np.concatenate([loi_1_fautive(n_c), loi_1_fautive(n_c)], axis=1)
    est, _ = banc.rho_moyenne(banc.cov_intra_classes(E, banc.classes(n_c)))
    assert abs(est[0] - banc.valeur_plantee(1, p, p, rho)[0]) > 0.1


def test_formules_erreur_equilibree_de_chaque_regle_contre_le_paragraphe_0():
    rng = _gens("essais_formules", 5)[4]
    n_c, p, rho = 200000, 0.2, 0.45
    y = banc.classes(n_c)
    E = banc.tirer_erreurs(1, rng, 1, n_c, np.full(2, p), np.full(2, p), rho)
    V = banc.votes_depuis_erreurs(E, y)
    p11 = p * p + rho * p * (1 - p)
    fa, vr, ee = banc.taux_erreurs(V.all(axis=-1), y)
    assert fa[0] == pytest.approx(p11, abs=0.004) and vr[0] == pytest.approx(2 * p - p11, abs=0.004)
    assert ee[0] == pytest.approx(p, abs=0.003)
    fa, vr, ee = banc.taux_erreurs(V.any(axis=-1), y)
    assert fa[0] == pytest.approx(2 * p - p11, abs=0.004) and vr[0] == pytest.approx(p11, abs=0.004)
    assert ee[0] == pytest.approx(p, abs=0.003)
    for j in range(2):
        fa, vr, ee = banc.taux_erreurs(V[..., j], y)
        assert fa[0] == pytest.approx(p, abs=0.004) and vr[0] == pytest.approx(p, abs=0.004)
    for rp in banc.RHOS_PRIME_R:
        Er = banc.repetitions(rng, E[..., 0], np.full(2 * n_c, p), rp, 3)
        erreur_majorite = (Er.sum(axis=-1) >= 2).mean()
        assert erreur_majorite == pytest.approx(rp * p + (1 - rp) * (3 * p * p - 2 * p ** 3), abs=0.004)
        r01, _ = banc.rho_paire(banc.cov_intra_classes(Er[..., :2], y), 0, 1)
        assert r01[0] == pytest.approx(rp, abs=0.01)


# =================================================================================================================
# Garde « théorie P2 »
# =================================================================================================================
def test_garde_p2_cas_sain_quatre_regles_a_la_meme_erreur_equilibree():
    rng_t, rng_r = _gens("essais_gardes", 4)[3], _gens("essais_formules", 6)[5]
    c = banc.cellule_estimateur_agregation(rng_t, rng_r, 1, 2, "egal_0.2", 0.45, 400, 300, 50)
    assert c["theorie_p2"]["ecart_maximal"] <= 0.01
    assert c["theorie_p2"]["garde"] == "valide"
    assert sum(c["bras_C_regle_choisie"].values()) == 300
    assert set(c["bras_C_regle_choisie"]) <= {"unanimite", "au_moins_un", "juge_1_seul", "juge_2_seul", "constante"}


def test_garde_p2_artefact_regle_codee_a_l_envers():
    rng = _gens("essais_gardes", 5)[4]
    n_c = 20000
    y = banc.classes(n_c)
    E = banc.tirer_erreurs(1, rng, 1, n_c, np.full(2, 0.2), np.full(2, 0.2), 0.3)
    V = banc.votes_depuis_erreurs(E, y)
    ee = {"S_1": banc.taux_erreurs(V[..., 0], y)[2][0], "S_2": banc.taux_erreurs(V[..., 1], y)[2][0],
          "U": banc.taux_erreurs(~V.any(axis=-1), y)[2][0],  # unanimité codée à l'envers
          "F_au_moins_un": banc.taux_erreurs(V.any(axis=-1), y)[2][0]}
    ecart = banc.ecart_p2(ee)
    assert ecart > 0.02
    assert banc.garde_p2(ecart) == "invalide"
    assert banc.garde_p2(0.019) == "valide"


# =================================================================================================================
# Garde « règle choisie à deux juges » et bras C, P, N
# =================================================================================================================
def test_regle_choisie_deux_juges_cas_sains_et_artefacts():
    assert banc.regle_choisie([1.0, 1.0], -1.0) == "au_moins_un"
    assert banc.regle_choisie([1.0, 1.0], 1.0) == "unanimite"
    assert banc.regle_choisie([2.0, 1.0], 0.0) == "juge_1_seul"
    assert banc.regle_choisie([1.0, 2.0], 0.0) == "juge_2_seul"
    assert banc.regle_choisie([1.0, 1.0], 3.0) == "constante"
    assert banc.regle_choisie([1.0, 1.0], -3.0) == "constante"
    with pytest.raises(banc.RegleInconnue):
        banc.regle_choisie([-1.0, 1.0], 0.0)


def test_bras_c_score_au_seuil_rend_non_notable():
    w = np.ones((2, 2))
    scores = np.zeros((2, 1))
    seuils = np.array([1e-17, -1e-17])
    assert not banc.appliquer_seuil(scores, seuils, w).any()
    assert banc.appliquer_seuil(scores + 0.5, seuils, w).all()


def test_bras_c_repli_poids_egaux_compte_quand_la_matrice_est_nulle():
    y = banc.classes(10)
    V = np.where(y[None, :, None], 1.0, -1.0) * np.ones((3, 20, 2))
    w, repli = banc.poids_covariance(V, y)
    assert repli.all() and np.all(w == 1.0)


def test_bras_c_poids_bornes_aucun_poids_nul_aucun_juge_retire():
    rng = _gens("essais_gardes", 6)[5]
    n_c = 25
    y = banc.classes(n_c)
    p_b = np.array([0.1, 0.45, 0.2, 0.3, 0.49])
    E = banc.tirer_erreurs(1, rng, 400, n_c, p_b, p_b, 0.5)
    V = 2.0 * banc.votes_depuis_erreurs(E, y) - 1.0
    w, repli = banc.poids_covariance(V, y)
    assert np.all(w > 0)
    ratio = w.min(axis=1) / w.max(axis=1)
    assert np.all(ratio >= 0.04 - 1e-12)
    assert w.shape == (400, 5)


def test_bras_p_paire_correlee_divisee_par_deux():
    rng = _gens("essais_gardes", 7)[6]
    n_c = 200
    y = banc.classes(n_c)
    E1 = banc.tirer_erreurs(1, rng, 1, n_c, np.array([0.2]), np.array([0.2]), 0.0)
    E3 = banc.tirer_erreurs(1, rng, 1, n_c, np.array([0.2]), np.array([0.2]), 0.0)
    E = np.concatenate([E1, E1, E3], axis=2)
    V = banc.votes_depuis_erreurs(E, y)
    w = banc.poids_precision(V, y, E)
    fa = V[:, ~y].mean(axis=1)
    vr = (~V[:, y]).mean(axis=1)
    attendu = np.maximum(1 - (fa + vr) / 2 - 0.5, 0.05)
    assert w[0, 0] == pytest.approx(attendu[0, 0] / 2)
    assert w[0, 1] == pytest.approx(attendu[0, 1] / 2)
    assert w[0, 2] == pytest.approx(attendu[0, 2])


def test_porteuse_arrondi_au_demi_superieur_et_non_au_pair():
    assert list(banc.q_porteuse([5.0, 4.0, 3.0, 2.0, 1.0])) == [3, 4, 4, 5, 5]
    assert banc.q_porteuse([np.nan])[0] == -1


def test_cellule_cinq_juges_rend_les_bras_et_les_mots():
    rng_t, rng_r = _gens("essais_gardes", 8)[7], _gens("essais_formules", 7)[6]
    c = banc.cellule_estimateur_agregation(rng_t, rng_r, 4, 5, "egal_0.2", 0.6, 100, 60, 40)
    for nom in ("S_1", "S_5", "U", "F_au_moins_un", "F_majorite_stricte", "poids_egaux", "C", "P", "N",
                "R_k5_rp0.0", "R_k5_rp0.9"):
        assert c["bras"][nom]["erreur_equilibree"] is not None
    assert c["valeur_plantee_rho_moyenne"] == pytest.approx(0.28)
    assert set(c["mot_fa38f9faa24e0_par_rho_prime"].values()) <= {"tient sur le banc", "réfuté sur le banc", "sans prise"}
    assert "F_majorite_stricte_moins_N" in c["comparaisons"]


# =================================================================================================================
# Double rendu et garde de cadrage, contre le calcul des prédictions v2
# =================================================================================================================
@pytest.mark.parametrize("loi", ["suiveur_seduisant", "suiveur_repoussant", "seduit_sinon_fond"])
@pytest.mark.parametrize("delta", [0.0, 0.2, 0.5])
def test_double_rendu_taux_exacts_contre_le_calcul(loi, delta):
    calcul = _calcul()
    rangs = {(l, d): i for i, (l, d) in enumerate((l, d) for l in banc.LOIS_LECTEUR for d in (0.0, 0.2, 0.5))}
    gens = _gens("essais_formules", 2 * len(rangs))
    rng1, rng2 = gens[2 * rangs[(loi, delta)]], gens[2 * rangs[(loi, delta)] + 1]
    m = banc.mesures_double_rendu(banc.tirer_monde_double_rendu(rng1, 20000, 100, 1.0, delta), loi)
    faux_trait = calcul.bras(loi, "faux", True, delta)
    vrai = calcul.bras(loi, "vrai", False, delta)
    assert np.nanmean(m["fa_trait_bras_1"]) == pytest.approx(faux_trait["bras_1"], abs=0.01)
    assert np.nanmean(m["fa_trait_bras_2"]) == pytest.approx(faux_trait["bras_2"], abs=0.01)
    assert np.nanmean(m["fa_trait_bras_4"]) == pytest.approx(faux_trait["bras_4"], abs=0.01)
    assert np.nanmean(m["vr_bras_1"]) == pytest.approx(1 - vrai["bras_1"], abs=0.01)
    assert np.nanmean(m["vr_bras_4"]) == pytest.approx(1 - vrai["bras_4"], abs=0.01)
    m2 = banc.mesures_double_rendu(banc.tirer_monde_double_rendu(rng2, 20000, 100, 0.5, delta), loi)
    faux_nu = calcul.bras(loi, "faux", False, delta)
    assert np.nanmean(m2["ecart_surface_bras_1"]) == pytest.approx(faux_trait["bras_1"] - faux_nu["bras_1"], abs=0.012)
    assert np.nanmean(m2["ecart_surface_bras_4"]) == pytest.approx(faux_trait["bras_4"] - faux_nu["bras_4"], abs=0.012)
    if delta == 0.0:
        sain = calcul.bras("suiveur_seduisant", "faux", False, 0.0)
        assert np.mean(m["abstention_par_vote"]) == pytest.approx(sain["abstention_par_vote"], abs=0.004)
        assert np.mean(m["abstention_par_temoin"]) == pytest.approx(sain["abstention_par_temoin_deux_juges"], abs=0.006)
        assert banc.ABSTENTION_PLANTEE_PAR_VOTE == pytest.approx(0.1275)


def test_double_rendu_mots_sans_intervalle_contre_la_sortie_du_calcul():
    sortie = _sortie_calcul()["double_rendu"]["par_loi_et_delta"]
    for loi in banc.LOIS_LECTEUR:
        for delta in (0.0, 0.2, 0.5):
            v = sortie[loi][str(delta)]
            fa1 = v["faux_acceptes_parmi_les_faux_a_trait"]["bras_1"]
            fa2 = v["faux_acceptes_parmi_les_faux_a_trait"]["bras_2"]
            vr1, vr4 = v["vrais_rejetes"]["bras_1"], v["vrais_rejetes"]["bras_4"]
            e1 = v["ecart_de_taux_de_notable_parmi_les_faux_trait_moins_sans_trait"]["bras_1"]
            e4 = v["ecart_de_taux_de_notable_parmi_les_faux_trait_moins_sans_trait"]["bras_4"]
            mi = banc.mot_clause_i(fa1, fa1 - fa2, fa2, vr1, vr4, fa2 - fa1)
            miii = banc.mot_clause_iii(delta, e1, e1, e1, e4, e4)
            assert mi == v["mot_sans_intervalle"]["clause_i"]
            assert miii == v["mot_sans_intervalle"]["clause_iii_a_s_0_5"]
            assert banc.mot_carte_fcfa(0.5, mi, miii) == v["mot_sans_intervalle"]["carte"]
    assert banc.mot_carte_fcfa(0.0, "réfuté sur le banc", "réfuté sur le banc") == "sans prise"


def test_double_rendu_cellule_rend_les_trois_lois_et_le_mot_sur_le_seul_suiveur_seduisant():
    rng_t, rng_r = _gens("essais_gardes", 9)[8], _gens("essais_formules", 8)[7]
    c = banc.cellule_double_rendu(rng_t, rng_r, 100, 0.5, 0.5, 200, 200)
    assert set(c["par_loi"]) == set(banc.LOIS_LECTEUR)
    assert c["par_loi"]["suiveur_seduisant"]["mot_de_la_carte"] in ("tient sur le banc", "réfuté sur le banc", "sans prise")
    for loi in ("suiveur_repoussant", "seduit_sinon_fond"):
        assert c["par_loi"][loi]["mot_de_la_carte"].startswith("sans mot")
    c0 = banc.cellule_double_rendu(rng_t, rng_r, 100, 1.0, 0.0, 200, 200)
    assert c0["par_loi"]["suiveur_seduisant"]["clause_ii"]["faute_du_banc"] is False
    assert c0["par_loi"]["suiveur_seduisant"]["clause_iii"].startswith("non lue")


def test_garde_de_cadrage_ronde_saine_et_suiveurs_egaux():
    rng = _gens("essais_gardes", 10)[9]
    c = banc.cellule_cadrage(rng, 40, 0.0, 4000)
    assert c["par_loi"]["suiveur_seduisant"]["taux_d_inversion_moyen"] == pytest.approx(0.1275, abs=0.004)
    c5 = banc.cellule_cadrage(rng, 40, 0.5, 2000)
    assert (c5["par_loi"]["suiveur_seduisant"]["taux_d_inversion_moyen"]
            == c5["par_loi"]["suiveur_repoussant"]["taux_d_inversion_moyen"])
    assert c5["par_loi"]["suiveur_seduisant"]["part_des_rondes_declenchees"]["0.3"] > \
        c["par_loi"]["suiveur_seduisant"]["part_des_rondes_declenchees"]["0.3"]
    assert banc.mot_branche_3(0.11, 0.9) == "réfuté sur le banc"
    assert banc.mot_branche_3(0.05, 0.5) == "tient sur le banc"
    assert banc.mot_branche_3(0.05, 0.49) == "sans prise"


# =================================================================================================================
# Monde de puissance, contre le calcul des prédictions v2
# =================================================================================================================
def test_monde_de_puissance_dissymetrie_et_faisabilite_contre_le_calcul():
    calcul = _calcul()
    sortie = _sortie_calcul()["monde_de_puissance"]
    for comparaison in banc.COMPARAISONS_PUISSANCE:
        for ecart in banc.ECARTS_PUISSANCE:
            cellules = sortie[comparaison][str(ecart)]["cellules"]
            for c in cellules:
                rp = c.get("rho_prime", 0.0)
                d = banc.resoudre_dissymetrie(comparaison, ecart, c["rho"], rp)
                assert d == calcul.resoudre(comparaison, ecart, c["rho"], rp)
                assert (d is not None) == c["faisable"]
                if d is not None:
                    assert round(d, 4) == c["d"]
                    a, b = 0.2 + d, 0.2 - d
                    assert (banc.loi_3_jouable(a, c["rho"]) and banc.loi_3_jouable(b, c["rho"])) == c["loi_3_jouable"]
    for d in (0.0, 0.07, 0.2):
        for rho in banc.RHOS:
            for rp in banc.RHOS_PRIME_R:
                assert banc.erreurs_equilibrees_formules(d, rho, rp) == calcul.erreurs_equilibrees(d, rho, rp)


@pytest.mark.parametrize("comparaison,loi,rho,rp", [("unanimite", 1, 0.0, 0.0), ("unanimite", 3, 0.15, 0.0),
                                                     ("juge_seul", 1, 0.15, 0.0),
                                                     ("juge_repete_trois_votes_majorite", 1, 0.0, 0.5)])
def test_monde_de_puissance_ecart_vrai_simule_a_grand_n(comparaison, loi, rho, rp):
    rng = _gens("essais_formules", 9)[8]
    d = banc.resoudre_dissymetrie(comparaison, 0.10, rho, rp)
    assert d is not None
    a, b = 0.2 + d, 0.2 - d
    n_c = 200000
    y = banc.classes(n_c)
    E = banc.tirer_erreurs(loi, rng, 1, n_c, np.array([a, a]), np.array([b, b]), rho)
    V = banc.votes_depuis_erreurs(E, y)
    ee_f = banc.taux_erreurs(V.any(axis=-1), y)[2][0]
    if comparaison == "unanimite":
        ee_c = banc.taux_erreurs(V.all(axis=-1), y)[2][0]
    elif comparaison == "juge_seul":
        ee_c = banc.taux_erreurs(V[..., 1], y)[2][0]
    else:
        Er = banc.repetitions(rng, E[..., 1], np.where(y, a, b), rp, 3)
        ee_c = banc.taux_erreurs(banc.votes_depuis_erreurs(Er, y).sum(axis=-1) >= 2, y)[2][0]
    assert ee_c - ee_f == pytest.approx(0.10, abs=0.006)


def test_monde_de_puissance_cellule_jouee_et_infaisable_nommee():
    rng_t, rng_r = _gens("essais_gardes", 11)[10], _gens("essais_formules", 10)[9]
    c = banc.cellule_puissance(rng_t, rng_r, "unanimite", 0.10, 1, 0.0, 0.0, 40, 200)
    assert c["faisable"] is True
    for v in c["puissance_par_comparaison"].values():
        assert 0.0 <= v <= 1.0
    assert sum(c["bras_C_regle_choisie"].values()) == 40
    assert c["ecart_vrai_formule"] == pytest.approx(0.10, abs=1e-9)
    inf = banc.cellule_puissance(rng_t, rng_r, "juge_seul", 0.15, 1, 0.0, 0.0, 10, 10)
    assert inf["faisable"] is False and "cause" in inf


def test_holm_pas_a_pas_descendant():
    rejet = banc.holm(np.array([[0.01, 0.04, 0.03, 0.005]]), 0.05)
    assert rejet.tolist() == [[True, False, False, True]]
    assert banc.holm(np.array([[0.01, 0.01, 0.01, 0.01]]), 0.05).all()
    assert not banc.holm(np.array([[0.02, 0.5, 0.5, 0.5]]), 0.05).any()


def test_p_valeur_unilaterale_du_reechantillonnage_apparie():
    diff = np.array([[0.1], [-0.02], [0.0], [0.05], [0.2], [-0.1], [0.3], [0.01], [0.02]])
    assert banc.p_valeur_unilaterale(diff, 9)[0] == pytest.approx((1 + 3) / 10)


def test_puissance_qui_decide_regle_gelee():
    def cell(comp, p, loi=1, ecart=0.10, faisable=True):
        noms = banc.COMPARAISONS_DU_MONDE[comp]
        return {"comparaison": comp, "ecart_vise": ecart, "loi": loi, "faisable": faisable,
                "puissance_par_comparaison": {"U": p, "S_1": p, "S_2": p, "R_3": p} if faisable else None,
                "noms": noms}
    cellules = [cell("unanimite", 0.9), cell("juge_seul", 0.7), cell("juge_repete_trois_votes_majorite", 0.6, loi=3)]
    r = banc.puissance_qui_decide(cellules)
    assert r["puissance_qui_decide"] == 0.6 and r["comparaisons_d_agregations"] == "peuvent porter un « oui »"
    r = banc.puissance_qui_decide(cellules + [cell("unanimite", 0.4)])
    assert r["puissance_qui_decide"] == 0.4 and r["comparaisons_d_agregations"].startswith("descriptives")
    r = banc.puissance_qui_decide(cellules[:2] + [cell("juge_repete_trois_votes_majorite", 0.9, ecart=0.05)])
    assert r["puissance_qui_decide"] is None and r["comparaisons_sans_cellule_faisable"] == ["R_3"]


def test_puissance_de_la_lecture_positif_de_rho_prime_moins_rho():
    rng_t, rng_r = _gens("essais_gardes", 12)[11], _gens("essais_formules", 11)[10]
    n_c = 100000
    y = banc.classes(n_c)
    E = np.concatenate([banc.tirer_quatre_rendus(rng_t, 1, n_c, 0.2, 0.3, 0.8),
                        banc.tirer_quatre_rendus(rng_t, 1, n_c, 0.2, 0.3, 0.8)], axis=1)
    S = banc.cov_intra_classes(E, y)
    assert banc.rho_paire(S, 0, 1)[0][0] == pytest.approx(0.3, abs=0.012)
    assert banc.rho_paire(S, 0, 2)[0][0] == pytest.approx(0.8, abs=0.012)
    assert banc.rho_paire(S, 1, 3)[0][0] == pytest.approx(0.8, abs=0.012)
    assert banc.rho_paire(S, 0, 3)[0][0] == pytest.approx(0.3, abs=0.012)
    c = banc.cellule_ecart_rho_prime(rng_t, rng_r, 0.5, 0.3, 40, 200)
    assert c["faisable"] and 0.0 <= c["puissance_les_deux"] <= c["puissance_juge_1"] <= 1.0
    assert banc.cellule_ecart_rho_prime(rng_t, rng_r, 0.5, 0.6, 5, 5)["faisable"] is False


# =================================================================================================================
# Alarme
# =================================================================================================================
def test_binomial_exact_bilateral():
    t = banc.table_p_valeurs_binomiales(10, 0.5)
    assert t[0] == pytest.approx(2 / 1024)
    assert t[10] == pytest.approx(2 / 1024)
    assert t[5] == pytest.approx(1.0)
    t0 = banc.table_p_valeurs_binomiales(10, 0.0)
    assert t0[0] == 1.0 and t0[1] == 0.0


def test_alarme_bras_a_muet_et_sentinelle_detecte_un_changement_a_effet():
    rng = _gens("essais_gardes", 13)[12]
    c = banc.cellule_alarme(rng, 40, 400)
    assert c["par_bras"]["A"]["detection_changement_a_effet"] == 0.0
    assert c["par_bras"]["A"]["fausse_alarme_suites_sans_changement"] == 0.0
    assert c["par_bras"]["B"]["detection_changement_a_effet"] > 0.7
    assert c["par_bras"]["B"]["fausse_alarme_suites_sans_changement"] < 0.2
    assert set(c["par_bras"]) == {"A", "B", "C", "D"}


# =================================================================================================================
# Critères mécaniques de l'estimateur (table de lecture gelée)
# =================================================================================================================
def _cellules_factices(tient_par_n, ecart_p2=0.0):
    cellules = []
    for n in banc.N_GRILLE:
        for loi, rhos in ((1, banc.RHOS), (3, [r for r in banc.RHOS if r <= 0.75])):
            for rho in rhos:
                c = {"J": 2, "loi": loi, "profil": banc.PROFIL_DE_LA_REGLE, "rho_grille": rho, "n": n,
                     "estimateur": {"tient": tient_par_n[n]}}
                if loi == 1:
                    c["theorie_p2"] = {"ecart_maximal": ecart_p2}
                cellules.append(c)
    return cellules


def test_verdict_mecanique_de_l_estimateur():
    f = banc.criteres_estimateur
    assert f(_cellules_factices({50: False, 100: True, 200: True, 400: True}))["taille_retenue_par_la_regle"] == 100
    r = f(_cellules_factices({50: False, 100: False, 200: True, 400: True}))
    assert r["verdict_mecanique_estimateur"].startswith("non, pas à cette taille") and r["taille_retenue_par_la_regle"] == 200
    assert f(_cellules_factices({50: False, 100: False, 200: False, 400: False}))["verdict_mecanique_estimateur"].startswith("non :")
    assert f(_cellules_factices({50: True, 100: False, 200: False, 400: False}))["verdict_mecanique_estimateur"].startswith("cas non prévu")
    r = f(_cellules_factices({50: True, 100: True, 200: True, 400: True}, ecart_p2=0.03))
    assert r["verdict_mecanique_estimateur"].startswith("invalide")
    assert f(_cellules_factices({50: True, 100: True, 200: True, 400: True})[:-1])["verdict_mecanique_estimateur"].startswith("incomplet")


# =================================================================================================================
# Bout en bout (racine des essais), manifeste, exécution unique, chronométrage
# =================================================================================================================
CONFIGURATION_D_ESSAI = {
    "repliques": 16,
    "tirages_reechantillonnage": 30,
    "estimateur": {"J": [2, 5], "lois_J2": [1, 3], "lois_J5": [4], "profils": ["egal_0.2"], "rhos": [0.0, 0.6],
                   "n": [50]},
    "puissance": {"ecarts": [0.10], "lois": [1], "rhos": [0.0], "rhos_prime": [0.5], "n": 100},
    "ecart_rho_prime": {"ecarts": [0.3], "rhos": [0.3], "taux": 0.20, "n": 100},
    "double_rendu": {"n": [50], "s": [0.5], "deltas": [0.0, 0.5]},
    "cadrage": {"t": [20], "deltas": [0.0, 0.5], "seuils": [0.1, 0.3]},
    "alarme": {"m": [10], "suites": 40},
}


def test_bout_en_bout_essai_manifeste_et_execution_unique(tmp_path):
    sortie = tmp_path / "sortie"
    contexte = banc.Contexte("essais")
    resultat, manifeste = banc.executer_etage_1(contexte, CONFIGURATION_D_ESSAI, sortie)
    chemin_res = sortie / "resultat-etage-1-ligne-3-v1.json"
    chemin_man = sortie / "manifeste-etage-1-ligne-3-v1.json"
    for chemin in (chemin_res, chemin_man):
        assert chemin.is_file()
        compagnon = Path(str(chemin) + ".sha256").read_text(encoding="utf-8").split()
        assert compagnon[0] == _sha256(chemin)
    man = json.loads(chemin_man.read_text(encoding="utf-8"))
    assert man["configuration_sha256"] == banc.sha256_json(man["configuration"])
    assert man["configuration"] == json.loads(json.dumps(CONFIGURATION_D_ESSAI))
    assert man["graines"]["racine_des_tirages"] == banc.RACINE_ESSAIS
    assert man["graines"]["racine_du_reechantillonnage"] == banc.RACINE_ESSAIS
    assert man["graines"]["table_cles"] == banc.TABLE_CLES
    assert {d["racine"] for d in man["graines"]["derivations"]} == {banc.RACINE_ESSAIS}
    assert "numpy" in man["versions"] and "python" in man["versions"]
    assert "commit" in man["depot"]
    assert man["fichiers"]["resultat-etage-1-ligne-3-v1.json"] == _sha256(chemin_res)
    assert man["programme_sha256"] == _sha256(CHEMIN_BANC)
    crit = resultat["criteres_mecaniques"]
    # À 16 répliques, la garde P2 peut se déclencher sur le bruit : « invalide » est alors la bonne sortie.
    assert crit["estimateur"]["verdict_mecanique_estimateur"].startswith(("incomplet", "invalide"))
    assert crit["branche_1_fefca0bd94064"].startswith("non jouée")
    with pytest.raises(banc.RefusExecution):
        banc.executer_etage_1(banc.Contexte("essais"), CONFIGURATION_D_ESSAI, sortie)


def test_chronometrage_n_imprime_que_des_durees(tmp_path):
    chrono = _charger("chronometrer_banc_ligne_3_v1", CHEMIN_CHRONO)
    tampon = io.StringIO()
    with contextlib.redirect_stdout(tampon):
        code = chrono.main(["--essai", "--manifeste", str(tmp_path / "chrono"), "--repliques-echantillon", "2",
                            "--tirages-essai", "20"])
    assert code == 0
    lignes = tampon.getvalue().strip().splitlines()
    assert lignes
    for ligne in lignes:
        assert re.fullmatch(r"duree_[a-z0-9_]+_secondes: [0-9]+\.[0-9]{3}", ligne), ligne
    assert (tmp_path / "chrono" / "manifeste-chronometrage-ligne-3-v1.json").is_file()


def test_chronometrage_refuse_sans_autorisation(tmp_path):
    chrono = _charger("chronometrer_banc_ligne_3_v1", CHEMIN_CHRONO)
    avant = len(banc.JOURNAL_GRAINES)
    with pytest.raises(banc.RefusGraine):
        chrono.main(["--autorisation-additif", str(tmp_path / "absent.md"), "--empreinte-additif", "0" * 64,
                     "--manifeste", str(tmp_path / "c")])
    assert len(banc.JOURNAL_GRAINES) == avant


def test_une_seule_creation_de_seedsequence_dans_le_code():
    for chemin in (CHEMIN_BANC, CHEMIN_CHRONO):
        texte = Path(chemin).read_text(encoding="utf-8")
        assert texte.count("np.random.SeedSequence(") == (1 if chemin == CHEMIN_BANC else 0), chemin
        if chemin == CHEMIN_CHRONO:
            assert "SeedSequence(" not in texte
        assert "default_rng(" not in texte.replace("np.random.default_rng(enfant)", "")


# =================================================================================================================
# Essai final : aucune graine des racines 2026111931 à 2026111937 dérivée dans ce processus
# =================================================================================================================
def test_zz_final_aucune_graine_des_racines_decisives_derivee():
    assert banc.JOURNAL_GRAINES, "aucune dérivation enregistrée : le journal ne fonctionne pas"
    assert {d["racine"] for d in banc.JOURNAL_GRAINES} == {banc.RACINE_ESSAIS}
    assert _ENTROPIES_CREEES, "l'enregistrement des SeedSequence ne fonctionne pas"
    for entropie in _ENTROPIES_CREEES:
        assert entropie not in RACINES_INTERDITES_AUX_ESSAIS
    assert set(_ENTROPIES_CREEES) == {banc.RACINE_ESSAIS}
