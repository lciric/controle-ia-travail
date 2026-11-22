"""Essais des gardes des quatre invariants (rang 8, section 6) : cas sains et artefacts de la table du point 6."""
import numpy as np
import pytest

from controle_ia.audit_apres_coup_v2.attaque_choisie import TYPES_ILLUSTRATION
from controle_ia.audit_apres_coup_v2 import gardes_invariants as gi
from controle_ia.audit_apres_coup_v2.oracle_simule import OracleSimule
from controle_ia.audit_apres_coup_v2.regle_audit import CONFIG_SANS_PLANCHER, RegleAudit, g_identite
from controle_ia.audit_apres_coup_v2.simulateur import Monde, politique_constante, simuler
from controle_ia.gardes import GardeArret

E = 20261122
N = 3000


def _monde(**kw):
    return Monde(30, E, TYPES_ILLUSTRATION, 1.6, politique_constante(0.01), 0.3, **kw)


R_ = RegleAudit(0.02, 0.015, 0.1, g_identite, 1.6)
O_ = OracleSimule(0.8, 0.0, 0, "signature")


# --- 1. Audit après coup ---------------------------------------------------------------------------
def test_audit_apres_coup_cas_sain():
    res = simuler(_monde(), R_, O_, 0, N)
    gi.garde_audit_apres_coup(res.journal)
    e = gi.empreintes_enregistrements(res)
    gi.garde_copie_oracle(e, list(e))
    assert gi.garde_pieces_appariees(_monde(), R_, O_, 0, N) > 0


def test_artefact_latence_qui_depend_de_la_piece():
    with pytest.raises(GardeArret, match="diffère"):
        gi.garde_pieces_appariees(_monde(), R_, O_, 0, N, canal_retour=gi.canal_latence_selon_piece)


def test_artefact_copie_d_empreinte_differente():
    res = simuler(_monde(), R_, O_, 0, N)
    e = gi.empreintes_enregistrements(res)
    with pytest.raises(GardeArret, match="empreinte différente"):
        gi.garde_copie_oracle(e, e[:-1] + ["0" * 64])


# --- 2. Plancher indépendant du score --------------------------------------------------------------
def test_plancher_cas_sain_et_permutation():
    res = simuler(_monde(), R_, O_, 0, N)
    gi.garde_plancher(res.journal, R_)
    rp = gi.rejeu_permute(_monde(), R_, O_, 0, N, 1, canaux=("score",))
    gi.garde_plancher_permutation(res, rp)


def test_artefact_plancher_fonction_du_score():
    art = lambda x: np.where(x < 0.3, 0.01, 0.02)
    res = simuler(_monde(), R_, O_, 0, N, plancher_artefact=art)
    with pytest.raises(GardeArret, match="plancher"):
        gi.garde_plancher(res.journal, R_)
    rp = gi.rejeu_permute(_monde(), R_, O_, 0, N, 1, canaux=("score",), plancher_artefact=art)
    with pytest.raises(GardeArret, match="permute"):
        gi.garde_plancher_permutation(res, rp)


def test_artefact_ligne_a_pi_nul_hors_sans_plancher():
    sans = RegleAudit(0.0, 0.0, 0.1, g_identite, 1.6, configuration=CONFIG_SANS_PLANCHER)
    res = simuler(_monde(), sans, O_, 0, N)
    gi.garde_plancher(res.journal, sans)  # journal étiqueté « sans plancher : aucune borne » : admis
    res.journal.etiquette = ""
    with pytest.raises(GardeArret, match="étiquette"):
        gi.garde_plancher(res.journal, sans)
    with pytest.raises(GardeArret, match="π_i < π_min|part du plancher"):
        gi.garde_plancher(res.journal, RegleAudit(0.02, 0.0, 0.1, g_identite, 1.6))


# --- 3. Part selon l'enjeu -------------------------------------------------------------------------
def test_enjeu_cas_sain():
    res = simuler(_monde(), R_, O_, 0, N)
    gi.garde_enjeu(res.journal, R_, enjeux_egaux_declares=False, enjeux_egaux_loi=_monde().enjeux_egaux())


def test_artefact_enjeu_ecrit_apres_la_fin():
    m = _monde(enjeu_ecrit_apres=True)
    res = simuler(m, R_, O_, 0, N)
    with pytest.raises(GardeArret, match="après le début"):
        gi.garde_enjeu(res.journal, R_, False, False)


def test_artefact_enjeux_egaux_non_declares():
    m = Monde(31, E, ((1.0, 2.0),), 2.0, politique_constante(0.01), 0.3)
    r = RegleAudit(0.02, 0.015, 0.1, g_identite, 2.0)
    res = simuler(m, r, O_, 0, 500)
    gi.garde_enjeu(res.journal, r, True, m.enjeux_egaux())
    with pytest.raises(GardeArret, match="égaux"):
        gi.garde_enjeu(res.journal, r, False, m.enjeux_egaux())


# --- 4. Aucun retour à l'agent ---------------------------------------------------------------------
def test_aucun_retour_cas_sain():
    assert gi.garde_aucun_retour(_monde(), R_, O_, 0, N, cle_permutation=2) > 0


def test_artefact_relance_declenchee_par_un_audit():
    with pytest.raises(GardeArret, match="diffère"):
        gi.garde_aucun_retour(_monde(), R_, O_, 0, N, cle_permutation=2, canal_retour=gi.canal_relance_sur_audit)
