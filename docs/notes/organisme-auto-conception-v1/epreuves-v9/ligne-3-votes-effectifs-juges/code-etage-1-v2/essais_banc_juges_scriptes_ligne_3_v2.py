"""Essais du banc de juges scriptés de la ligne 3, étage 1 — v2.

Gardes de la liste d'arrêt qui touchent l'étage 1, chacune sur un cas sain et sur un artefact (R5) ; essais de
formules de l'annexe A (grand n, corrélation estimée contre valeur plantée par loi ; erreur équilibrée contre les
formules du § 0 ; taux exacts du double rendu et écarts vrais du monde de puissance contre
`calcul_predictions_ligne_3_v2.py` et sa sortie) ; garde des graines ; essai final : aucune graine des racines
2026111931 à 2026111937 dérivée dans le processus des essais.

Seule la racine des essais (2026111930) est dérivée. Lancement :
    TMPDIR=<dossier de travail> PYTHONDONTWRITEBYTECODE=1 python3 -B -m pytest -q CE_FICHIER
Variables facultatives : BANC_LIGNE_3_CHEMIN (copie du banc à éprouver, pour le contrôle des défauts réintroduits),
CHRONOMETRAGE_LIGNE_3_CHEMIN, CALCUL_PREDICTIONS_LIGNE_3 (chemin du calcul des prédictions v2).
Version 2 (corrections de la contre-lecture `contre-lecture-code-etage-1-ligne-3-v1.md`, 3aed6849…) : C1, essais
sain et artefact qui épinglent les règles de lecture et les constantes gelées (mot de fa38f9faa24e0, branches (2)
et (3) de fefca0bd94064, clause (i), tolérances et constantes du « Seuil », poids des bras C et P, règles des bras
N et R, centiles des intervalles, stabilité, garde de cadrage, test entier du monde de puissance, alarme à
seuils serrés sur un générateur factice) ; C2, la lettre « à partir de laquelle » de la branche (2) ; C3, essai
sain et artefacts de `verifier_autorisation` seule, sans aucune dérivation. Banc éprouvé : v2.

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
import statistics
import sys
import types
import warnings
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
CHEMIN_BANC = Path(os.environ.get("BANC_LIGNE_3_CHEMIN", str(ICI / "banc_juges_scriptes_ligne_3_v2.py")))
CHEMIN_CHRONO = Path(os.environ.get("CHRONOMETRAGE_LIGNE_3_CHEMIN", str(ICI / "chronometrer_banc_ligne_3_v2.py")))
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


banc = _charger("banc_juges_scriptes_ligne_3_v2", CHEMIN_BANC)


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
# Version 2 — correction C3 : garde des graines, essai sain et artefacts de `verifier_autorisation` seule.
# Ces essais n'appellent que `verifier_autorisation` (fonction pure) : aucune dérivation, aucune racine décisive.
# =================================================================================================================
def _additif_valide(tmp_path):
    additif = tmp_path / "additif-de-code-factice.md"
    additif.write_text("additif de code factice (essai)\n", encoding="utf-8")
    return additif, _sha256(additif)


@pytest.mark.parametrize("racine", [2026111931, 2026111932, 2026111933])
def test_verifier_autorisation_cas_sain_additif_valide_accepte_sans_derivation(racine, tmp_path):
    additif, emp = _additif_valide(tmp_path)
    avant_journal, avant_entropies = len(banc.JOURNAL_GRAINES), len(_ENTROPIES_CREEES)
    assert banc.verifier_autorisation(banc.Autorisation(additif, emp), racine) is None
    assert banc.verifier_autorisation(banc.Autorisation(str(additif), emp), racine) is None
    assert len(banc.JOURNAL_GRAINES) == avant_journal
    assert len(_ENTROPIES_CREEES) == avant_entropies


def _artefact_autorisation(cas, tmp_path):
    additif, emp = _additif_valide(tmp_path)
    autre = tmp_path / "autre-fichier.md"
    autre.write_text("autre contenu\n", encoding="utf-8")
    return {
        "aucune_autorisation": (None, "sans autorisation"),
        "type_inattendu": ((str(additif), emp), "type inattendu"),
        "empreinte_en_majuscules": (banc.Autorisation(additif, emp.upper()), "mal formée"),
        "empreinte_courte": (banc.Autorisation(additif, emp[:63]), "mal formée"),
        "empreinte_absente": (banc.Autorisation(additif, None), "mal formée"),
        "chemin_absent": (banc.Autorisation(tmp_path / "absent.md", emp), "additif absent"),
        "chemin_d_un_dossier": (banc.Autorisation(tmp_path, emp), "additif absent"),
        "empreinte_d_un_autre_fichier": (banc.Autorisation(additif, _sha256(autre)), "différente de l'attendue"),
    }[cas]


@pytest.mark.parametrize("cas", ["aucune_autorisation", "type_inattendu", "empreinte_en_majuscules", "empreinte_courte",
                                 "empreinte_absente", "chemin_absent", "chemin_d_un_dossier",
                                 "empreinte_d_un_autre_fichier"])
def test_verifier_autorisation_artefacts_refuses_sans_derivation(cas, tmp_path):
    autorisation, motif = _artefact_autorisation(cas, tmp_path)
    avant_journal, avant_entropies = len(banc.JOURNAL_GRAINES), len(_ENTROPIES_CREEES)
    with pytest.raises(banc.RefusGraine, match=motif):
        banc.verifier_autorisation(autorisation, banc.RACINE_ETAGE_1_DECISIF)
    assert len(banc.JOURNAL_GRAINES) == avant_journal
    assert len(_ENTROPIES_CREEES) == avant_entropies


# =================================================================================================================
# Version 2 — correction C1 : règles de lecture et constantes gelées, épinglées (essai sain et essai artefact)
# =================================================================================================================
CONSTANTES_DU_TEXTE = {
    "TOL_BIAIS": 0.05, "TOL_EQM": 0.10, "TOL_COUVERTURE": (0.90, 0.98), "TOL_PART_INDEFINI": 0.02,
    "NIVEAU_HOLM": 0.05, "MARGE_COMPARAISON": 0.05, "PUISSANCE_EXIGEE": 0.5, "TAUX_MOYEN_PUISSANCE": 0.20,
    "D_MAX": 0.20, "ECARTS_PUISSANCE": (0.05, 0.10, 0.15), "NIVEAU_ALARME": 0.05 / 11, "GENERATIONS": 12,
    "MARGE_VRAIS_REJETES": 0.05, "SEUIL_REFERENCE_SANS_PRISE": 0.02, "MARGE_SURFACE": 0.05,
    "SEUILS_CADRAGE": (0.10, 0.15, 0.20, 0.25, 0.30), "P_FOND": 0.15, "RHO_PRIME_FOND": 0.5,
    "RHOS": (0.0, 0.15, 0.3, 0.45, 0.6, 0.75, 0.9), "N_GRILLE": (50, 100, 200, 400),
    "TAUX_EGAUX": (0.05, 0.10, 0.20, 0.30), "RHOS_PRIME_R": (0.0, 0.5, 0.9), "F_DIFFICILE": 0.25,
    "RHO_MAX_LOI_3": 0.75, "ECARTS_RHO_PRIME": (0.2, 0.3, 0.5), "TAILLES_D_ETALONNAGE": (25, 50, 100, 200),
}


def _ecarts_aux_constantes(module):
    return sorted(nom for nom, valeur in CONSTANTES_DU_TEXTE.items() if getattr(module, nom, None) != valeur)


def test_constantes_du_texte_cas_sain():
    assert _ecarts_aux_constantes(banc) == []


def test_constantes_du_texte_artefact_constante_alteree_vue():
    faux = types.SimpleNamespace(**{nom: getattr(banc, nom) for nom in CONSTANTES_DU_TEXTE})
    faux.NIVEAU_HOLM = 0.10
    faux.TOL_COUVERTURE = (0.80, 0.98)
    assert _ecarts_aux_constantes(faux) == ["NIVEAU_HOLM", "TOL_COUVERTURE"]


def test_configuration_decisive_aux_valeurs_du_texte():
    attendue = {
        "repliques": 2000,
        "tirages_reechantillonnage": 2000,
        "estimateur": {"J": [2, 5], "lois_J2": [1, 2, 3], "lois_J5": [1, 4],
                       "profils": ["egal_0.05", "egal_0.1", "egal_0.2", "egal_0.3", "severe", "indulgent", "inegal"],
                       "rhos": [0.0, 0.15, 0.3, 0.45, 0.6, 0.75, 0.9], "n": [50, 100, 200, 400]},
        "puissance": {"ecarts": [0.05, 0.10, 0.15], "lois": [1, 3], "rhos": [0.0, 0.15, 0.3, 0.45, 0.6, 0.75, 0.9],
                      "rhos_prime": [0.0, 0.5, 0.9], "n": 100},
        "ecart_rho_prime": {"ecarts": [0.2, 0.3, 0.5], "rhos": [0.0, 0.15, 0.3, 0.45, 0.6, 0.75, 0.9], "taux": 0.20,
                            "n": 100},
        "double_rendu": {"n": [50, 100, 200, 400], "s": [0.0, 0.5, 1.0], "deltas": [0.0, 0.2, 0.5]},
        "cadrage": {"t": [20, 40], "deltas": [0.0, 0.2, 0.5], "seuils": [0.10, 0.15, 0.20, 0.25, 0.30]},
        "alarme": {"m": [10, 20, 40], "suites": 2000},
    }
    assert banc.CONFIGURATION_DECISIVE == attendue
    altere = json.loads(json.dumps(attendue))
    altere["alarme"]["m"] = [10, 20]
    assert banc.CONFIGURATION_DECISIVE != altere


# --- Qualité de l'estimateur : tolérance gelée (|biais| ≤ 0,05 ; erreur quadratique ≤ 0,10 ; couverture 0,90–0,98 ;
# part « indéfini » ≤ 0,02), couverture comptée sur les répliques définies -------------------------------------
def _qualite(erreurs, couvrants, indef=(), intervalle_indefini=(), plantee=0.30):
    e = np.asarray(erreurs, dtype=float)
    couvrants = np.asarray(couvrants, dtype=bool)
    rho = plantee + e
    lo = np.where(couvrants, plantee - 0.01, plantee + 0.01)
    hi = lo + 0.02
    ind = np.zeros(rho.size, dtype=bool)
    ind[list(indef)] = True
    rho = np.where(ind, np.nan, rho)
    lo = np.where(ind, np.nan, lo)
    hi = np.where(ind, np.nan, hi)
    for i in intervalle_indefini:
        lo[i] = np.nan
        hi[i] = np.nan
    return banc.qualite_estimateur(rho, ind, lo, hi, plantee)


def test_qualite_estimateur_tolerance_gelee_cas_sain():
    q = _qualite([0.04] * 20, [True] * 19 + [False])
    assert q["tient"] is True
    assert q["biais"] == pytest.approx(0.04) and q["eqm"] == pytest.approx(0.04) and q["couverture"] == 0.95
    assert _qualite([0.09, -0.09] * 10, [True] * 18 + [False] * 2)["tient"] is True      # couverture 0,90 incluse
    q = _qualite([0.0] * 50, [True] * 46 + [False] * 4, indef=[0])                          # part « indéfini » 0,02
    assert q["part_indefini"] == pytest.approx(0.02) and q["tient"] is True


def test_qualite_estimateur_tolerance_gelee_artefacts():
    assert _qualite([0.06] * 20, [True] * 19 + [False])["tient"] is False                   # biais 0,06
    assert _qualite([0.11, -0.11] * 10, [True] * 19 + [False])["tient"] is False            # erreur quadratique 0,11
    assert _qualite([0.0] * 20, [True] * 17 + [False] * 3)["tient"] is False                # couverture 0,85
    q = _qualite([0.0] * 20, [True] * 20)                                                   # couverture 1,00
    assert q["tient"] is False and q["audit_trop_propre_aucune_replique_hors_intervalle"] is True
    assert _qualite([0.0] * 50, [True] * 46 + [False] * 4, indef=[0, 1])["tient"] is False  # part « indéfini » 0,04


def test_qualite_estimateur_couverture_sur_les_seules_repliques_definies():
    # 20 répliques définies (la 20ᵉ à intervalle indéfini, comptée « non couvrante »), une réplique indéfinie écartée.
    q = _qualite([0.0] * 21, [True] * 21, indef=[20], intervalle_indefini=[19])
    assert q["couverture"] == pytest.approx(19 / 20)
    assert q["couverture"] != pytest.approx(19 / 21)
    assert q["part_indefini"] == pytest.approx(1 / 21)


# --- Intervalles : centiles 2,5 et 97,5 -----------------------------------------------------------------------
def test_centiles_du_reechantillonnage_2_5_et_97_5():
    v = np.arange(1001, dtype=float)[:, None]
    lo, hi = banc._centiles(v, 0)
    assert lo[0] == pytest.approx(25.0) and hi[0] == pytest.approx(975.0)
    v2 = np.vstack([v, [[np.nan]]])
    lo2, hi2 = banc._centiles(v2, 0)
    assert lo2[0] == pytest.approx(25.0) and hi2[0] == pytest.approx(975.0)
    assert lo[0] != pytest.approx(np.percentile(v, 5))


def test_intervalle_des_repliques_centiles_2_5_et_97_5():
    a = _gens("essais_formules", 40)[20]
    b = _gens("essais_formules", 40)[20]
    valeurs = np.r_[np.linspace(-0.2, 0.3, 37) ** 3, np.nan, np.inf]
    moy, lo, hi = banc.intervalle_moyenne_repliques(valeurs, a, 500)
    v = valeurs[np.isfinite(valeurs)]
    idx = b.integers(0, v.size, size=(500, v.size))
    moyennes = v[idx].mean(axis=1)
    bas, haut = np.percentile(moyennes, [2.5, 97.5])
    assert moy == pytest.approx(float(v.mean()), abs=1e-15)
    assert lo == pytest.approx(float(bas), abs=1e-15) and hi == pytest.approx(float(haut), abs=1e-15)
    bas5, haut95 = np.percentile(moyennes, [5, 95])
    assert abs(bas5 - bas) > 1e-6 and abs(haut95 - haut) > 1e-6
    assert banc.intervalle_moyenne_repliques(np.array([np.nan]), a, 10) == (None, None, None)


# --- Critère de fa38f9faa24e0 (bras P) ---------------------------------------------------------------------------
def test_mot_fa38_regle_gelee_cas_sains():
    f = banc.mot_fa38
    refs = [(0.20, 0.10), (0.30, 0.12)]
    assert f(0.84 * 0.20, 0.10, refs) == "tient sur le banc"            # 16 % sous la plus basse des deux
    assert f(0.10, 0.10 + 0.04, refs) == "tient sur le banc"            # vrais rejetés accrus de 0,04 seulement
    assert f(0.001, 0.10, [(0.021, 0.10), (0.30, 0.12)]) == "tient sur le banc"   # référence à 0,021 : avec prise


def test_mot_fa38_regle_gelee_artefacts():
    f = banc.mot_fa38
    refs = [(0.20, 0.10), (0.30, 0.12)]
    assert f(0.86 * 0.20, 0.10, refs) == "réfuté sur le banc"           # 14 % seulement sous la première
    assert f(0.84 * 0.30, 0.10, refs) == "réfuté sur le banc"           # sous la seconde, pas sous la première
    assert f(0.10, 0.10 + 0.06, refs) == "sans prise"                   # vrais rejetés accrus de plus de 0,05
    assert f(0.001, 0.10, [(0.019, 0.10), (0.30, 0.12)]) == "sans prise"  # référence sous 0,02
    assert f(0.001, 0.30, [(0.019, 0.10), (0.30, 0.12)]) == "sans prise"  # « sans prise » lu avant tout


# --- Clause (i) du double rendu ----------------------------------------------------------------------------------
def test_mot_clause_i_regle_gelee_cas_sains_et_artefacts():
    f = banc.mot_clause_i
    # (fa1, borne basse de fa1 − fa2, fa2, vr1, vr4, borne basse de fa2 − fa1)
    assert f(0.03, -0.09, 0.10, 0.30, 0.26, 0.04) == "tient sur le banc"      # vrais rejetés : + 0,04 < 0,05
    assert f(0.03, -0.09, 0.10, 0.32, 0.26, 0.04) == "réfuté sur le banc"     # vrais rejetés : + 0,06 > 0,05
    assert f(0.03, -0.09, 0.019, 0.30, 0.26, 0.04) == "sans prise"            # bras 2 sous 0,02
    assert f(0.03, -0.09, 0.021, 0.30, 0.26, 0.004) == "tient sur le banc"    # bras 2 à 0,021 : avec prise
    assert f(0.12, 0.01, 0.10, 0.30, 0.26, -0.03) == "réfuté sur le banc"     # bras 1 au-dessus, intervalle > 0
    assert f(0.11, -0.01, 0.10, 0.30, 0.26, -0.03) == "réfuté sur le banc"    # ni au-dessus ni au-dessous : réfuté
    assert f(0.12, 0.01, 0.019, 0.30, 0.26, -0.03) == "réfuté sur le banc"    # « réfuté » lu avant « sans prise »


# --- Seuil au milieu, poids du bras C, poids du bras P -----------------------------------------------------------
def test_seuil_au_milieu_des_deux_moyennes_de_classe():
    y = np.array([True, True, False, False])
    assert banc.seuil_milieu(np.array([[4.0, 2.0, 1.0, -1.0]]), y)[0] == pytest.approx(1.5)
    y3 = np.array([True, True, True, False])
    s = banc.seuil_milieu(np.array([[3.0, 3.0, 3.0, -1.0]]), y3)[0]
    assert s == pytest.approx(1.0)
    assert s != pytest.approx(2.0) and s != pytest.approx(3.0)       # ni la moyenne globale, ni celle des bons


def _poids_c_reference(V, y, facteur_lambda=0.1):
    """Calcul indépendant des poids du bras C pour une réplique (texte, tableau des bras)."""
    V = np.asarray(V, dtype=float)
    n, J = V.shape
    S = np.zeros((J, J))
    for masque in (y, ~y):
        X = V[masque] - V[masque].mean(axis=0)
        S += X.T @ X
    S /= n - 2
    d = V[y].mean(axis=0) - V[~y].mean(axis=0)
    lam = facteur_lambda * np.trace(S) / J
    w = np.linalg.solve(S + lam * np.eye(J), d)
    moyenne = w.mean()
    return np.clip(w, 0.2 * moyenne, 5.0 * moyenne)


def test_bras_c_poids_contre_un_calcul_independant():
    rng = _gens("essais_gardes", 40)[24]
    n_c, R = 40, 6
    y = banc.classes(n_c)
    p = np.array([0.05, 0.25, 0.45])
    E = banc.tirer_erreurs(1, rng, R, n_c, p, p, 0.0)
    V = 2.0 * banc.votes_depuis_erreurs(E, y) - 1.0
    w, repli = banc.poids_covariance(V, y)
    assert not repli.any()
    for r in range(R):
        assert np.allclose(w[r], _poids_c_reference(V[r], y), atol=1e-10, rtol=0.0)
        assert not np.allclose(w[r], _poids_c_reference(V[r], y, facteur_lambda=0.5), atol=1e-6, rtol=0.0)
    assert np.all(w[:, 0] > w[:, 2])          # le juge le plus exact pèse plus que le plus faible
    assert not np.allclose(w, 1.0)


def test_bras_p_plancher_0_05_et_seuil_de_paire_0_5():
    n_c = 100
    y = banc.classes(n_c)
    E = np.zeros((1, 2 * n_c, 3), dtype=bool)
    for debut in (0, n_c):
        E[0, debut + np.arange(10), 0] = True                                # juge 1 : 10 % d'erreurs
        E[0, debut + np.r_[np.arange(7), np.arange(20, 23)], 1] = True       # juge 2 : 7 erreurs communes au juge 1
        E[0, debut + np.arange(50, 100), 2] = True                           # juge 3 : 50 % d'erreurs, disjointes
    S = banc.cov_intra_classes(E.astype(float), y)
    r12, r13, r23 = (banc.rho_paire(S, j, k)[0][0] for j, k in ((0, 1), (0, 2), (1, 2)))
    assert 0.5 < r12 < 0.9 and r13 < 0.5 and r23 < 0.5
    V = banc.votes_depuis_erreurs(E, y)
    w = banc.poids_precision(V, y, E)
    assert w[0].tolist() == pytest.approx([0.2, 0.2, 0.05])   # paire à 0,67 divisée par 2 ; plancher 0,05


# --- Branche (2) de fefca0bd94064 : seuil 0,02, taille d'étalonnage n / 2, « à partir de laquelle » (C2) -------
def _cellules_branche_2(tient_par_taille, ecart_qui_ne_tient_pas=0.03, ecart_qui_tient=-0.01):
    cellules = []
    for n in banc.N_GRILLE:
        taille = n // 2
        if taille not in tient_par_taille:
            continue
        for loi in (1, 4):
            for nom in ("egal_0.2", "severe"):
                for rho in (0.0, 0.6):
                    ecart = 0.0
                    if (loi, nom, rho) == (4, "severe", 0.6):
                        ecart = ecart_qui_tient if tient_par_taille[taille] else ecart_qui_ne_tient_pas
                    cellules.append({"J": 5, "loi": loi, "profil": nom, "rho_grille": rho, "n": n,
                                     "bras": {"C": {"erreur_equilibree": 0.25 + ecart},
                                              "poids_egaux": {"erreur_equilibree": 0.25}}})
    hors = {"bras": {"C": {"erreur_equilibree": 0.9}, "poids_egaux": {"erreur_equilibree": 0.1}},
            "profil": "egal_0.2", "rho_grille": 0.0, "n": 100}
    cellules.append(dict(hors, J=2, loi=1))       # deux juges : sans prise, ne compte pas
    cellules.append(dict(hors, J=5, loi=2))       # loi hors de la branche : ne compte pas
    return cellules


def test_branche_2_seuil_de_0_02_par_cellule():
    tout = {25: True, 50: True, 100: True, 200: True}
    r = banc.criteres_branche_2(_cellules_branche_2(tout, ecart_qui_tient=0.015))
    assert r["par_cellule"]["4|severe|0.6|50"]["mot"] == "tient sur le banc"
    r = banc.criteres_branche_2(_cellules_branche_2({25: True, 50: False, 100: True, 200: True},
                                                    ecart_qui_ne_tient_pas=0.025))
    assert r["par_cellule"]["4|severe|0.6|50"]["mot"] == "réfuté sur le banc"
    assert r["par_cellule"]["4|severe|0.6|25"]["mot"] == "tient sur le banc"
    assert r["a_deux_juges"].startswith("sans prise")
    assert all(cle.split("|")[0] in ("1", "4") for cle in r["par_cellule"])


def test_branche_2_taille_d_etalonnage_n_sur_2():
    r = banc.criteres_branche_2(_cellules_branche_2({25: False, 50: True, 100: True, 200: True}))
    assert {cle.split("|")[-1] for cle in r["par_cellule"]} == {"25", "50", "100", "200"}
    assert r["tient_dans_toutes_les_cellules_par_taille_d_etalonnage"] == {"25": False, "50": True, "100": True,
                                                                           "200": True}
    assert r["plus_petite_taille_d_etalonnage_a_partir_de_laquelle_la_branche_tient_partout"] == 50


def test_branche_2_lettre_a_partir_de_laquelle_cas_sains():
    f = banc.plus_petite_taille_a_partir_de_laquelle
    assert f({25: True, 50: True, 100: True, 200: True}) == (25, [])
    assert f({25: False, 50: True, 100: True, 200: True}) == (50, [])
    assert f({25: False, 50: False, 100: False, 200: True}) == (200, [])
    cle = "plus_petite_taille_d_etalonnage_a_partir_de_laquelle_la_branche_tient_partout"
    assert banc.criteres_branche_2(_cellules_branche_2({25: False, 50: True, 100: True, 200: True}))[cle] == 50


def test_branche_2_lettre_a_partir_de_laquelle_artefacts():
    # Une taille intermédiaire tient, une plus grande ne tient pas : la lecture « plus petite taille où tout tient »
    # rendrait 25 ; la lettre du texte exige les tailles plus grandes.
    f = banc.plus_petite_taille_a_partir_de_laquelle
    assert f({25: True, 50: False, 100: True, 200: True}) == (100, [])
    assert f({25: True, 50: True, 100: False, 200: True}) == (200, [])
    assert f({25: True, 50: True, 100: True, 200: False}) == (None, [])
    assert f({25: True, 50: True}) == (None, [100, 200])
    cle = "plus_petite_taille_d_etalonnage_a_partir_de_laquelle_la_branche_tient_partout"
    r = banc.criteres_branche_2(_cellules_branche_2({25: True, 50: False, 100: True, 200: True}))
    assert r[cle] == 100
    r = banc.criteres_branche_2(_cellules_branche_2({25: True, 50: True, 100: True, 200: False}))
    assert r[cle] is None
    r = banc.criteres_branche_2(_cellules_branche_2({25: True, 50: True}))
    assert isinstance(r[cle], str) and r[cle].startswith("incomplet")


# --- Branche (3) de fefca0bd94064 : rondes saines (δ = 0) et rondes à δ = 0,5 ---------------------------------
def _cadrage_factice(parts, t=40):
    return [{"t": t, "delta": delta,
             "par_loi": {loi: {"part_des_rondes_declenchees": {str(c): p for c in banc.SEUILS_CADRAGE}}
                         for loi in banc.LOIS_LECTEUR}}
            for delta, p in parts.items()]


def test_branche_3_lit_les_rondes_a_delta_0_5_cas_sain():
    r = banc.criteres_branche_3(_cadrage_factice({0.0: 0.05, 0.2: 0.30, 0.5: 0.60}))
    assert r["suiveur_seduisant|t=40|c=0.1"] == {"part_saine": 0.05, "part_delta_0.5": 0.60, "mot": "tient sur le banc"}
    assert r["suiveur_repoussant|t=40|c=0.3"]["mot"] == "tient sur le banc"
    assert r["seduit_sinon_fond|t=40|c=0.2"]["mot"] == "rapporté sans mot (tient sur le banc)"
    assert len(r) == 3 * len(banc.SEUILS_CADRAGE)
    assert banc.mot_branche_3(0.10, 0.5) == "tient sur le banc"        # « plus de 10 % » : 0,10 ne réfute pas


def test_branche_3_lit_les_rondes_a_delta_0_5_artefacts():
    r = banc.criteres_branche_3(_cadrage_factice({0.0: 0.05, 0.2: 0.60, 0.5: 0.30}))
    assert r["suiveur_seduisant|t=40|c=0.1"]["mot"] == "sans prise"     # la colonne δ = 0,2 n'est pas lue
    r = banc.criteres_branche_3(_cadrage_factice({0.0: 0.11, 0.2: 0.60, 0.5: 0.90}))
    assert r["suiveur_seduisant|t=40|c=0.1"]["mot"] == "réfuté sur le banc"
    assert banc.mot_branche_3(0.1000001, 0.9) == "réfuté sur le banc"


# --- Cellule à cinq juges rejouée sur les mêmes tirages : stabilité (centile 95 de |écart|), bras N (≥ q),
# bras R à cinq votes (majorité ≥ 3), références du mot de fa38f9faa24e0 ------------------------------------------
def _moyenne_finie(v):
    v = np.asarray(v, dtype=float)
    return float(v[np.isfinite(v)].mean())


def test_cellule_cinq_juges_stabilite_porteuse_r_et_mot_fa38_rejoues():
    J, loi, nom, rho, n, R, B = 5, 1, "egal_0.2", 0.45, 100, 200, 20
    c = banc.cellule_estimateur_agregation(_gens("essais_gardes", 40)[20], _gens("essais_formules", 40)[21],
                                           loi, J, nom, rho, n, R, B)
    t2 = _gens("essais_gardes", 40)[20]
    n_c = n // 2
    y = banc.classes(n_c)
    p_b, p_m = banc.profil(nom, J)
    E = banc.tirer_erreurs(loi, t2, R, n_c, p_b, p_m, rho)
    cal, lec = banc.indices_moities(n_c)
    y_cal, y_lec = y[cal], y[lec]

    # Stabilité : centile 95 de |ρ(étalonnage) − ρ(lecture)|.
    r_cal, i_cal = banc.rho_moyenne(banc.cov_intra_classes(E[:, cal], y_cal))
    r_lec, i_lec = banc.rho_moyenne(banc.cov_intra_classes(E[:, lec], y_lec))
    ok = (~i_cal) & (~i_lec)
    ecarts = np.abs(r_cal - r_lec)[ok]
    attendu = float(np.percentile(ecarts, 95))
    assert c["stabilite_centile_95_ecart_moities"] == pytest.approx(attendu, abs=1e-15)
    assert abs(float(np.percentile(ecarts, 90)) - attendu) > 1e-6
    assert abs(float(np.percentile((r_cal - r_lec)[ok], 95)) - attendu) > 1e-6

    # Bras N : notable chez au moins q juges.
    Vl = banc.votes_depuis_erreurs(E, y)[:, lec]
    q = banc.q_porteuse(banc.tronquer_votes(banc.votes_effectifs(r_cal, J), J))

    def taux_moyens(notable, masque=None):
        fa, vr, ee = banc.taux_erreurs(notable, y_lec)
        if masque is not None:
            fa, vr, ee = (np.where(masque, np.nan, t) for t in (fa, vr, ee))
        return {"faux_acceptes": _moyenne_finie(fa), "vrais_rejetes": _moyenne_finie(vr),
                "erreur_equilibree": _moyenne_finie(ee)}

    attendu_n = taux_moyens(Vl.sum(axis=-1) >= q[:, None], q < 0)
    for cle, valeur in attendu_n.items():
        assert c["bras"]["N"][cle] == pytest.approx(valeur, abs=1e-12)
    strict = taux_moyens(Vl.sum(axis=-1) > q[:, None], q < 0)
    assert abs(strict["erreur_equilibree"] - attendu_n["erreur_equilibree"]) > 1e-6

    # Bras R, k = 5, majorité (au moins 3 votes), sur les tirages qui suivent ceux des erreurs.
    p_juge_1 = np.where(y, p_b[0], p_m[0])
    for rp in banc.RHOS_PRIME_R:
        Er = banc.repetitions(t2, E[..., 0], p_juge_1, rp, 5)
        Vr = banc.votes_depuis_erreurs(Er, y)[:, lec]
        attendu_r = taux_moyens(Vr.sum(axis=-1) >= 3)
        for cle, valeur in attendu_r.items():
            assert c["bras"][f"R_k5_rp{rp}"][cle] == pytest.approx(valeur, abs=1e-12)
        a_deux = taux_moyens(Vr.sum(axis=-1) >= 2)
        assert abs(a_deux["erreur_equilibree"] - attendu_r["erreur_equilibree"]) > 1e-6

    # Mot de fa38f9faa24e0 : références « poids égaux » et R à k = J, un mot par ρ′.
    pe = c["bras"]["poids_egaux"]
    for rp in banc.RHOS_PRIME_R:
        rr = c["bras"][f"R_k5_rp{rp}"]
        refs = [(pe["faux_acceptes"], pe["vrais_rejetes"]), (rr["faux_acceptes"], rr["vrais_rejetes"])]
        assert c["mot_fa38f9faa24e0_par_rho_prime"][str(rp)] == banc.mot_fa38(
            c["bras"]["P"]["faux_acceptes"], c["bras"]["P"]["vrais_rejetes"], refs)


# --- Garde de cadrage rejouée : « dépasse » strict ---------------------------------------------------------------
def test_garde_de_cadrage_depasse_strict_rejouee():
    R, t, delta = 2000, 20, 0.0
    c = banc.cellule_cadrage(_gens("essais_gardes", 40)[21], t, delta, R)
    monde = banc.tirer_monde_double_rendu(_gens("essais_gardes", 40)[21], R, t, 1.0, delta, juges=2)
    distingue = False
    for loi in banc.LOIS_LECTEUR:
        v1, v2 = banc.votes_double_rendu(monde, loi)
        inversion = (v1 != v2).mean(axis=(1, 2))
        assert c["par_loi"][loi]["taux_d_inversion_moyen"] == pytest.approx(float(inversion.mean()), abs=1e-15)
        for seuil in banc.SEUILS_CADRAGE:
            assert c["par_loi"][loi]["part_des_rondes_declenchees"][str(seuil)] == float((inversion > seuil).mean())
            distingue = distingue or float((inversion >= seuil).mean()) != float((inversion > seuil).mean())
    assert distingue        # des rondes tombent exactement sur un seuil : « ≥ » s'en distinguerait


# --- Puissance de la lecture « positif » de ρ′ − ρ rejouée : borne basse au centile 2,5 ----------------------------
def test_puissance_rho_prime_borne_basse_centile_2_5_rejouee():
    R, B, ecart, rho, n, p = 60, 400, 0.2, 0.3, 100, 0.20
    c = banc.cellule_ecart_rho_prime(_gens("essais_gardes", 40)[22], _gens("essais_formules", 40)[22],
                                     ecart, rho, R, B, n=n, p=p)
    b_t, b_r = _gens("essais_gardes", 40)[22], _gens("essais_formules", 40)[22]
    rho_prime = rho + ecart
    n_c = n // 2
    y = banc.classes(n_c)
    E = np.concatenate([banc.tirer_quatre_rendus(b_t, R, n_c, p, rho, rho_prime),
                        banc.tirer_quatre_rendus(b_t, R, n_c, p, rho, rho_prime)], axis=1)
    X = banc.motifs(4)
    cb, cm = banc.comptes_configurations(E[:, y]), banc.comptes_configurations(E[:, ~y])
    lo25 = np.full((R, 2), np.nan)
    lo5 = np.full((R, 2), np.nan)
    for debut in range(0, R, banc.TAILLE_PAQUET):
        fin = min(R, debut + banc.TAILLE_PAQUET)
        S = banc.cov_depuis_comptes(banc.tirer_comptes(b_r, cb[debut:fin], B), banc.tirer_comptes(b_r, cm[debut:fin], B),
                                    X)
        r12, _ = banc.rho_paire(S, 0, 1)
        for juge, (i, k) in enumerate(((0, 2), (1, 3))):
            rp, _ = banc.rho_paire(S, i, k)
            with warnings.catch_warnings():
                warnings.simplefilter("ignore", category=RuntimeWarning)
                lo25[debut:fin, juge] = np.nanpercentile(rp - r12, 2.5, axis=0)
                lo5[debut:fin, juge] = np.nanpercentile(rp - r12, 5, axis=0)
    positif = np.nan_to_num(lo25, nan=-np.inf) > 0
    assert c["puissance_juge_1"] == float(positif[:, 0].mean())
    assert c["puissance_juge_2"] == float(positif[:, 1].mean())
    assert c["puissance_les_deux"] == float(positif.all(axis=1).mean())
    assert ((np.nan_to_num(lo5, nan=-np.inf) > 0) != positif).any()     # le centile 5 s'en distinguerait


# --- Monde de puissance rejoué : test entier (valeurs de probabilité, Holm à 0,05, marge 0,05), R lié au juge 2 ---
def test_monde_de_puissance_test_entier_rejoue():
    comparaison, ecart, loi, rho, rp, R, B, n = "juge_repete_trois_votes_majorite", 0.10, 1, 0.0, 0.5, 80, 300, 100
    c = banc.cellule_puissance(_gens("essais_gardes", 40)[23], _gens("essais_formules", 40)[23],
                               comparaison, ecart, loi, rho, rp, R, B, n=n)
    b_t, b_r = _gens("essais_gardes", 40)[23], _gens("essais_formules", 40)[23]
    d = banc.resoudre_dissymetrie(comparaison, ecart, rho, rp)
    a, b = 0.2 + d, 0.2 - d
    n_c = n // 2
    y = banc.classes(n_c)
    E = banc.tirer_erreurs(loi, b_t, R, n_c, np.array([a, a]), np.array([b, b]), rho)
    Er = banc.repetitions(b_t, E[..., 1], np.where(y, a, b), rp, 3)
    cal, lec = banc.indices_moities(n_c)
    y_cal, y_lec = y[cal], y[lec]
    V = banc.votes_depuis_erreurs(E, y)
    Vc_pm, Vl_pm = 2.0 * V[:, cal] - 1.0, 2.0 * V[:, lec] - 1.0
    w_c, _ = banc.poids_covariance(Vc_pm, y_cal)
    s_c = banc.seuil_milieu(banc.score(Vc_pm, w_c), y_cal)
    notable = {"C": banc.appliquer_seuil(banc.score(Vl_pm, w_c), s_c, w_c), "U": V[:, lec].all(axis=-1),
               "S_1": V[:, lec, 0], "S_2": V[:, lec, 1],
               "R_3": banc.votes_depuis_erreurs(Er, y)[:, lec].sum(axis=-1) >= 2}
    noms = ("C", "U", "S_1", "S_2", "R_3")
    erreurs = np.stack([notable[k] != y_lec[None, :] for k in noms], axis=-1)
    ee = 0.5 * (erreurs[:, ~y_lec].mean(axis=1) + erreurs[:, y_lec].mean(axis=1))
    ecarts_obs = ee[:, 1:] - ee[:, :1]
    for i, nom in enumerate(noms[1:]):
        assert c["ecart_observe_moyen"][nom] == pytest.approx(float(ecarts_obs[:, i].mean()), abs=1e-12)
    X = banc.motifs(len(noms))
    cb, cm = banc.comptes_configurations(erreurs[:, y_lec]), banc.comptes_configurations(erreurs[:, ~y_lec])
    nb, nm = int(y_lec.sum()), int((~y_lec).sum())
    pv = np.zeros((R, 4))
    for debut in range(0, R, banc.TAILLE_PAQUET):
        fin = min(R, debut + banc.TAILLE_PAQUET)
        db, dm = banc.tirer_comptes(b_r, cb[debut:fin], B), banc.tirer_comptes(b_r, cm[debut:fin], B)
        e = 0.5 * ((dm @ X) / nm + (db @ X) / nb)
        diff = e[..., 1:] - e[..., :1]
        pv[debut:fin] = (1.0 + (diff <= 1e-12).sum(axis=0)) / (B + 1.0)

    def puissances(niveau, marge):
        rejet = banc.holm(pv, niveau)
        gagne = rejet & (ecarts_obs >= marge - 1e-12)
        return {nom: float(gagne[:, i].mean()) for i, nom in enumerate(noms[1:])}

    attendu = puissances(0.05, 0.05)
    assert c["puissance_par_comparaison"] == pytest.approx(attendu, abs=1e-15)
    assert puissances(0.10, 0.05) != attendu        # Holm à 0,10 s'en distinguerait
    assert puissances(0.05, 0.10) != attendu        # marge de 0,10 s'en distinguerait


# --- Alarme à seuils serrés, générateur factice (comptes écrits d'avance, appels enregistrés) -------------------
class _RngAlarmeFactice:
    """Remplace le générateur de `cellule_alarme` : enregistre chaque appel, rend des comptes écrits d'avance."""

    def __init__(self, g_change, plans):
        self.g_change = np.asarray(g_change)
        self.plans = plans
        self.appels_integers = []
        self.appels_binomial = []

    def integers(self, low, high, size=None):
        self.appels_integers.append((low, high, size))
        return self.g_change.copy()

    def binomial(self, n, p):
        rang = len(self.appels_binomial)
        p = np.asarray(p, dtype=float)
        self.appels_binomial.append((n, p.copy()))
        plan = self.plans.get(rang)
        if plan is None:
            return np.zeros(np.broadcast(n, p).shape, dtype=np.int64)
        return np.asarray(plan, dtype=np.int64).copy()


def _z_deux_proportions(x, base, M):
    pool = (base + x) / (2.0 * M)
    return (x / M - base / M) / np.sqrt(pool * (1 - pool) * 2.0 / M)


def test_alarme_comparaisons_a_seuils_serres_generateur_factice():
    R, m, G = 8, 40, banc.GENERATIONS
    gens = np.arange(1, G + 1)
    g_change = np.array([5, 7, 9, 10, 4, 4, 4, 4])
    extreme = np.zeros((R, G), dtype=bool)
    extreme[0, gens >= 6] = True      # suite à effet, changement en 5 : alarme en 6, délai 1
    extreme[2, gens == 9] = True      # suite sans effet, changement en 9 : alarme en 9
    extreme[3, gens == 3] = True      # suite sans effet, changement en 10 : alarme avant le changement
    extreme[4, gens == 12] = True     # suite sans changement : fausse alarme en 12
    ancres_moitie = np.where(extreme, 10, 2)
    production = np.full((R, G), 50)
    production[4:6, 1:] = 69
    production[6:8, 1:] = 71
    rng = _RngAlarmeFactice(g_change, {0: np.full(R, 5), 1: np.full(R, 5), 2: ancres_moitie, 3: ancres_moitie,
                                       4: production})

    # Le dessin du test : 69 entre le seuil unilatéral et le seuil bilatéral, 71 au-delà ; bras D jamais en alarme ;
    # 4 erreurs sur 40 ancres jamais en alarme, 20 toujours.
    nd = statistics.NormalDist()
    z_bilateral = nd.inv_cdf(1 - banc.NIVEAU_ALARME / 2)
    z_unilateral = nd.inv_cdf(1 - banc.NIVEAU_ALARME)
    assert z_unilateral < _z_deux_proportions(69, 50, 100) < z_bilateral < _z_deux_proportions(71, 50, 100)
    assert _z_deux_proportions(71, 50, 100 + m) < z_unilateral
    table = banc.table_p_valeurs_binomiales(m, 0.10)
    assert table[4] > banc.NIVEAU_ALARME and table[20] <= banc.NIVEAU_ALARME

    c = banc.cellule_alarme(rng, m, R)

    # Appels : génération du changement dans 4..10 ; référence 50 + 50 ; ancres m/2 + m/2 ; production 70 + 30 ;
    # bras D : m cartes de plus, 70 % de bonnes ; taux du monde du texte.
    assert rng.appels_integers == [(4, 11, R)]
    bons_extra = int(round(0.7 * m))
    assert [n for n, _ in rng.appels_binomial] == [50, 50, m // 2, m - m // 2, 70, 30, bons_extra, m - bons_extra]
    idx = np.arange(R)
    change, effet = idx < R // 2, idx < R // 4
    profil_a = (idx < R // 4) | ((idx >= R // 2) & (idx < (3 * R) // 4))
    vr0, fa0 = np.where(profil_a, 0.10, 0.05), np.where(profil_a, 0.10, 0.15)
    apres = change[:, None] & (gens[None, :] >= g_change[:, None])
    vr = np.where(apres, np.where(effet, 0.25, 0.15)[:, None], vr0[:, None])
    fa = np.where(apres, np.where(effet, 0.25, 0.05)[:, None], fa0[:, None])
    for (_, p), attendu in zip(rng.appels_binomial, [vr0, fa0, vr, fa, 1 - vr, fa, 1 - vr, fa]):
        assert p.shape == attendu.shape and np.allclose(p, attendu)

    b = c["par_bras"]["B"]
    assert b["detection_changement_a_effet"] == 0.5
    assert b["detection_changement_sans_effet"] == 0.5
    assert b["delai_moyen_changement_a_effet"] == 1.0
    assert b["fausse_alarme_suites_sans_changement"] == 0.25
    assert b["alarme_avant_changement_suites_changees"] == 0.25
    assert b["part_des_detections_sur_changement_a_effet"] == 0.5
    cc = c["par_bras"]["C"]
    assert cc["fausse_alarme_suites_sans_changement"] == 0.5          # 71 seulement, pas 69
    assert cc["detection_changement_a_effet"] == 0.0 and cc["detection_changement_sans_effet"] == 0.0
    assert cc["delai_moyen_changement_a_effet"] is None and cc["part_des_detections_sur_changement_a_effet"] is None
    assert cc["alarme_avant_changement_suites_changees"] == 0.0
    assert c["par_bras"]["D"]["fausse_alarme_suites_sans_changement"] == 0.0
    a = c["par_bras"]["A"]
    assert a["detection_changement_a_effet"] == 0.0 and a["fausse_alarme_suites_sans_changement"] == 0.0


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
    chemin_res = sortie / "resultat-etage-1-ligne-3-v2.json"
    chemin_man = sortie / "manifeste-etage-1-ligne-3-v2.json"
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
    assert man["fichiers"]["resultat-etage-1-ligne-3-v2.json"] == _sha256(chemin_res)
    assert man["programme_sha256"] == _sha256(CHEMIN_BANC)
    crit = resultat["criteres_mecaniques"]
    # À 16 répliques, la garde P2 peut se déclencher sur le bruit : « invalide » est alors la bonne sortie.
    assert crit["estimateur"]["verdict_mecanique_estimateur"].startswith(("incomplet", "invalide"))
    assert crit["branche_1_fefca0bd94064"].startswith("non jouée")
    with pytest.raises(banc.RefusExecution):
        banc.executer_etage_1(banc.Contexte("essais"), CONFIGURATION_D_ESSAI, sortie)


def test_chronometrage_n_imprime_que_des_durees(tmp_path):
    chrono = _charger("chronometrer_banc_ligne_3_v2", CHEMIN_CHRONO)
    tampon = io.StringIO()
    with contextlib.redirect_stdout(tampon):
        code = chrono.main(["--essai", "--manifeste", str(tmp_path / "chrono"), "--repliques-echantillon", "2",
                            "--tirages-essai", "20"])
    assert code == 0
    lignes = tampon.getvalue().strip().splitlines()
    assert lignes
    for ligne in lignes:
        assert re.fullmatch(r"duree_[a-z0-9_]+_secondes: [0-9]+\.[0-9]{3}", ligne), ligne
    assert (tmp_path / "chrono" / "manifeste-chronometrage-ligne-3-v2.json").is_file()


def test_chronometrage_refuse_sans_autorisation(tmp_path):
    chrono = _charger("chronometrer_banc_ligne_3_v2", CHEMIN_CHRONO)
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
