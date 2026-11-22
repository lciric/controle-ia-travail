"""Essais de la pièce 3 — tirage : tireur pur et rejeu du nul."""
import numpy as np
import pytest

from controle_ia.devin_v2 import RefusDevin
from controle_ia.devin_v2.tirage import TireurLecture, TireurPiece, propension_constante

RACINE = 0xA54F_F53A_5F1D_36F1_510E_527F_ADE6_82D1
REJEU = 0x9B05_688C_2B3E_6C1F_1F83_D9AB_FB41_BD6B
IDS = [f"t{k}" for k in range(400)]
ENTREES = [{"lot": k % 4} for k in range(400)]


def propension_du_passe(t, entrees, passe):
    """Propension qui dépend des pièces passées : baisse après un audit récent."""
    base = 0.2 + 0.1 * entrees["lot"]
    if passe.shape[1] == 0:
        return np.full(passe.shape[0], base)
    return np.where(passe[:, -1] == 1, base / 2, base)


def test_cas_sain_pieces_consignees_redonnees():
    tir = TireurPiece(propension_constante(0.5), depend_du_passe=False)
    j = tir.tirer(RACINE, IDS, ENTREES)
    tir.verifier_rejeu(j, RACINE)
    assert 0.4 < j.pieces.mean() < 0.6


def test_cas_sain_rejeu_dans_l_ordre():
    tir = TireurPiece(propension_du_passe, depend_du_passe=True,
                      dependances=frozenset({"entrees_consignees", "pieces_passees"}))
    j = tir.tirer(RACINE, IDS, ENTREES)
    tir.verifier_rejeu(j, RACINE)
    A, pi = tir.rejeu_nul(j, REJEU, 300)
    assert A.shape == pi.shape == (300, 400)
    # π* recalculé depuis A*_{<t} : il suit la règle sur chaque lot rejoué.
    b = 17
    attendu = np.array([propension_du_passe(t, ENTREES[t], A[b:b + 1, :t])[0] for t in range(400)])
    assert np.array_equal(pi[b], attendu)
    assert abs((A - pi).mean()) < 0.01


def test_rejeu_independant_moyenne_propension():
    tir = TireurPiece(propension_constante(0.05), depend_du_passe=False)
    j = tir.tirer(RACINE, IDS, ENTREES)
    A, pi = tir.rejeu_nul(j, REJEU, 500)
    assert abs(A.mean() - 0.05) < 0.005
    with pytest.raises(RefusDevin, match="égale"):
        tir.rejeu_nul(j, RACINE, 10)


@pytest.mark.parametrize("dep", ["verdict_audit_non_joue", "sonde_reapprise"])
def test_artefact_dependance_non_recalculable_refusee(dep):
    with pytest.raises(RefusDevin, match="sonde gelée"):
        TireurPiece(propension_constante(0.5), depend_du_passe=False,
                    dependances=frozenset({"entrees_consignees", dep}))


def test_artefact_sonde_reapprise_cachee_trouvee_au_rejeu():
    """Propension tirée d'une sonde réapprise après coup (non déclarée) : le rejeu la trouve."""
    etat = {"poids": 0.3}

    def propension_sonde(t, entrees, passe):
        return np.full(passe.shape[0], etat["poids"])

    tir = TireurPiece(propension_sonde, depend_du_passe=False)
    j = tir.tirer(RACINE, IDS, ENTREES)
    etat["poids"] = 0.31  # la sonde est réapprise sur les épisodes audités
    with pytest.raises(RefusDevin, match="non redonnée"):
        tir.verifier_rejeu(j, RACINE)


def test_test_de_mort_5_pieces_alterees():
    tir = TireurPiece(propension_constante(0.5), depend_du_passe=False)
    j = tir.tirer(RACINE, IDS, ENTREES)
    alteree = type(j)(j.identifiants, j.entrees, j.propensions, 1 - j.pieces, j.empreinte_racine)
    with pytest.raises(RefusDevin, match="test de mort 5"):
        tir.verifier_rejeu(alteree, RACINE)
    with pytest.raises(RefusDevin, match="empreinte"):
        tir.verifier_rejeu(j, REJEU)


def test_aucun_repli_propension_invalide():
    tir = TireurPiece(lambda t, e, p: np.full(p.shape[0], 1.5), depend_du_passe=False)
    with pytest.raises(RefusDevin, match="hors de"):
        tir.tirer(RACINE, IDS, ENTREES)
    with pytest.raises(RefusDevin, match="incohérente"):
        TireurPiece(propension_constante(0.5), depend_du_passe=True)
    with pytest.raises(RefusDevin, match="double"):
        TireurPiece(propension_constante(0.5), False).tirer(RACINE, ["a", "a"], [{}, {}])


def test_ordre_des_taches_sans_effet_sur_la_piece_d_une_tache():
    tir = TireurPiece(propension_constante(0.5), depend_du_passe=False)
    a = tir.tirer(RACINE, IDS, ENTREES)
    b = tir.tirer(RACINE, IDS[::-1], ENTREES[::-1])
    assert np.array_equal(a.pieces, b.pieces[::-1])


def test_lecture_substituee_service_et_equilibre():
    temoins = np.random.default_rng(np.random.SeedSequence(RACINE, spawn_key=(1,))).normal(0.5, 1, 500)
    ts = TireurLecture(temoins, "service")
    js = ts.tirer(RACINE, IDS)
    assert np.all(np.isin(js.lectures, temoins))
    ts.verifier_rejeu(js, RACINE)
    with pytest.raises(RefusDevin, match="égale"):  # C13
        ts.rejeu_nul(js, RACINE, 5)
    te = TireurLecture(temoins, "equilibre", seuil=0.0)
    je = te.tirer(RACINE, IDS)
    assert 0.42 < (je.lectures > 0).mean() < 0.58
    S = te.rejeu_nul(je, REJEU, 200)
    assert S.shape == (200, 400) and abs((S > 0).mean() - 0.5) < 0.01
    with pytest.raises(RefusDevin):
        TireurLecture(temoins, "equilibre", seuil=100.0)
    with pytest.raises(RefusDevin):
        TireurLecture(temoins, "equilibre")
