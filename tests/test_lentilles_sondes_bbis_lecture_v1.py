"""Essais de la lecture (texte scellé, « Code neuf », essais « lecture ») : garde de la fonction de lecture sur les deux
artefacts, indice de couche par signature, rapport à ε (bords 99 et 101), imparité."""
from __future__ import annotations

import numpy as np
import pytest

torch = pytest.importorskip("torch")

import lentilles_sondes_bbis_jouets_v1 as J  # noqa: E402
from controle_ia.lentilles_sondes_bbis import constantes_v1 as K  # noqa: E402
from controle_ia.lentilles_sondes_bbis import lecture_v1 as le  # noqa: E402
from controle_ia.lentilles_sondes_bbis import montage_v1 as mo  # noqa: E402
from controle_ia.lentilles_sondes_bbis import nuls_v1 as nu  # noqa: E402
from controle_ia.lentilles_sondes_bbis.constantes_v1 import Arret  # noqa: E402

D, T, F = 48, 300, 96


@pytest.fixture(scope="module")
def monde():
    g = torch.Generator().manual_seed(11)
    matrices = {c: (torch.eye(D) + 0.5 * torch.randn(D, D, generator=g)).to(torch.float16).numpy() for c in K.COUCHES}
    return {"wu": torch.randn(T, D, generator=g), "gamma": 1 + 0.2 * torch.randn(D, generator=g),
            "w_down": torch.randn(D, F, generator=g),
            "publique": le.LentillePublique(matrices, {c: le.empreinte_matrice(m) for c, m in matrices.items()}),
            "read": mo.charger_read_voisin(J.RACINE / K.COPIE_READOUT)}


def _garde(monde, lentille, couche, sain=None, artefact=None, lire_voisin=None):
    graines = nu.Graines()
    colonnes = monde["w_down"][:, torch.as_tensor(nu.colonnes_garde(graines, couche, F))]
    couches = sorted(K.COUCHES)
    if lentille == K.LENTILLE_PUBLIQUE:
        j = monde["publique"].matrice(couche)[0]
        j_art = monde["publique"].matrice(couches[(couches.index(couche) + 1) % 3])[0]
    else:
        j, j_art = None, le.matrice_permutation(nu.permutation_garde_logits(graines, couche, D))
    return le.garde_fonction_lecture(lire_voisin or monde["read"], colonnes, monde["gamma"], monde["wu"],
                                     j if sain is None else sain, j_art if artefact is None else artefact, lentille, couche)


# --- garde de la fonction de lecture -----------------------------------------------------------------------------------------------------
@pytest.mark.parametrize("lentille", K.LENTILLES)
@pytest.mark.parametrize("couche", K.COUCHES)
def test_garde_de_lecture_saine_et_ses_deux_artefacts_vus(monde, lentille, couche):
    r = _garde(monde, lentille, couche)
    assert r["tenue"] and r["colonnes"] == 64 and r["colonnes_differentes_sur_artefact"] >= 32


def test_garde_de_lecture_artefact_invisible_arret(monde):
    """L'artefact doit changer la lecture : la même matrice (publique) ou l'identité (logits) à sa place : arrêt."""
    j = monde["publique"].matrice(15)[0]
    with pytest.raises(Arret, match="artefact vu sur 0 colonnes"):
        _garde(monde, K.LENTILLE_PUBLIQUE, 15, artefact=j)
    with pytest.raises(Arret, match="artefact vu sur 0 colonnes"):
        _garde(monde, K.LENTILLE_LOGITS, 15, artefact=le.matrice_permutation(np.arange(D)))


def test_garde_de_lecture_ecart_sur_le_cas_sain_arret(monde):
    """Notre code lit par une autre matrice que le voisin (ici : une autre couche) : écart sur le cas sain, arrêt."""
    autre = monde["publique"].matrice(23)[0]

    def voisin_d_une_autre_couche(colonnes, wu, gamma, jacobienne, k):
        return monde["read"](colonnes, wu, gamma, autre, k=k)
    with pytest.raises(Arret, match="écart sur le cas sain"):
        _garde(monde, K.LENTILLE_PUBLIQUE, 7, lire_voisin=voisin_d_une_autre_couche)
    with pytest.raises(Arret, match="écart sur le cas sain"):
        _garde(monde, K.LENTILLE_LOGITS, 7, lire_voisin=voisin_d_une_autre_couche)


def test_garde_de_lecture_quasi_egalite_comptee_sans_arret(monde):
    """Le voisin échange le dixième et le onzième jeton, de scores égaux à 10⁻⁴ près : compté, rapporté, sans arrêt ; avec
    des scores éloignés : arrêt."""
    wu = monde["wu"].clone()
    colonnes = monde["w_down"][:, torch.as_tensor(nu.colonnes_garde(nu.Graines(), 7, F))]
    scores, _ = le.lire(colonnes[:, :1], None, monde["gamma"], wu)
    ordre = scores[:, 0].argsort(descending=True)
    wu[ordre[10]] = wu[ordre[9]] * (1 - 2e-5)                # le onzième devient un quasi-jumeau du dixième

    def voisin(colonnes, wu, gamma, jacobienne, k):
        p, ids = monde["read"](colonnes, wu, gamma, jacobienne, k=k)
        ids = ids.clone()
        ids[0, (ids[0] == ordre[9]).nonzero()[0, 0]] = ordre[10]
        return p, ids
    r = le.garde_fonction_lecture(voisin, colonnes, monde["gamma"], wu, None,
                                  le.matrice_permutation(nu.permutation_garde_logits(nu.Graines(), 7, D)), K.LENTILLE_LOGITS, 7)
    assert r["ecarts_de_quasi_egalite"] == 1 and r["tenue"]

    def voisin_loin(colonnes, wu, gamma, jacobienne, k):
        p, ids = monde["read"](colonnes, wu, gamma, jacobienne, k=k)
        ids = ids.clone()
        ids[0, 0] = ordre[200]
        return p, ids
    with pytest.raises(Arret, match="écart sur le cas sain"):
        le.garde_fonction_lecture(voisin_loin, colonnes, monde["gamma"], wu, None,
                                  le.matrice_permutation(nu.permutation_garde_logits(nu.Graines(), 7, D)), K.LENTILLE_LOGITS, 7)


def test_scores_egaux_a_la_formule_du_voisin(monde):
    """Mêmes scores que `rms_norm_columns(transport(v, J), γ)` puis W_U, en simple précision."""
    v = monde["w_down"][:, :5]
    j = monde["publique"].matrice(15)[0]
    scores, _ = le.lire(v, j, monde["gamma"], monde["wu"])
    t = j @ v
    attendu = monde["wu"] @ (t * torch.rsqrt(t.pow(2).mean(0, keepdim=True) + 1e-6) * monde["gamma"][:, None])
    assert torch.allclose(scores, attendu, rtol=1e-6, atol=1e-6) and scores.shape == (T, 5)


# --- indice de couche --------------------------------------------------------------------------------------------------------------------
def _lentille_a_signature():
    g = torch.Generator().manual_seed(2)
    e = torch.randn(D, D, generator=g).numpy()
    matrices = {c: (np.eye(D) + c * 1e-2 * e).astype(np.float16) for c in K.COUCHES}
    return e, le.LentillePublique(matrices, {c: le.empreinte_matrice(m) for c, m in matrices.items()})


@pytest.mark.parametrize("couche", K.COUCHES)
def test_indice_de_couche_la_lecture_rend_la_signature_de_la_couche(couche):
    """Fausse lentille J_ℓ = I + ℓ·10⁻²·E : le vecteur transporté pour une sonde de couche ℓ porte la signature ℓ."""
    e, publique = _lentille_a_signature()
    v = torch.randn(D, generator=torch.Generator().manual_seed(4))
    j, indice, empreinte = le.jacobienne_de(K.LENTILLE_PUBLIQUE, couche, publique)
    t = le.transporter(v, j)[:, 0].numpy()
    signature = float(np.median((t - v.numpy()) / (1e-2 * (e @ v.numpy()))))
    assert indice == couche and round(signature) == couche and abs(signature - couche) < 0.2
    assert empreinte == publique.empreintes_montage[couche]


@pytest.mark.parametrize("couche", K.COUCHES)
def test_indice_de_couche_decalage_d_un_cran_arret(couche):
    _, publique = _lentille_a_signature()
    publique.decalage = 1
    with pytest.raises(Arret, match="autre indice que la couche"):
        le.jacobienne_de(K.LENTILLE_PUBLIQUE, couche, publique)


def test_indice_de_couche_empreintes_du_montage_echangees_arret():
    _, publique = _lentille_a_signature()
    e = publique.empreintes_montage
    publique.empreintes_montage = {7: e[15], 15: e[7], 23: e[23]}
    le.jacobienne_de(K.LENTILLE_PUBLIQUE, 23, publique)
    with pytest.raises(Arret, match="autre indice"):
        le.jacobienne_de(K.LENTILLE_PUBLIQUE, 7, publique)


def test_lentille_publique_absente_jamais_de_lecture_par_les_seuls_logits():
    with pytest.raises(Arret, match="la lecture par la seule lentille des logits n'est pas rendue"):
        le.jacobienne_de(K.LENTILLE_PUBLIQUE, 7, None)
    assert le.jacobienne_de(K.LENTILLE_LOGITS, 7, None) == (None, 7, "identite")
    with pytest.raises(Arret):
        le.jacobienne_de("notre-lentille", 7, None)


# --- rapport à ε --------------------------------------------------------------------------------------------------------------------------
def _rho(v):
    return float(le.rapport_epsilon(le.transporter(v, None))[0])


def test_rapport_a_epsilon_artefact_et_cas_sain():
    g = np.random.default_rng(0)
    u = g.standard_normal(D)
    petite = (u / np.linalg.norm(u) * 1e-4).astype(np.float32)                 # v de norme 10⁻⁴, J = I : la garde se lève
    saine = (u / np.sqrt(np.mean(u ** 2))).astype(np.float32)                  # v de moyenne quadratique 1 : elle ne se lève pas
    assert _rho(petite) < K.SEUIL_RAPPORT_EPSILON and not le.independance_tenue(_rho(petite))
    assert _rho(saine) == pytest.approx(1e6, rel=1e-4) and le.independance_tenue(_rho(saine))


def test_rapport_a_epsilon_bords_99_et_101():
    u = np.ones(D)
    for rho, tenue in ((99.0, False), (101.0, True), (100.0, True)):
        v = (u * np.sqrt(rho * K.EPSILON)).astype(np.float64)
        mesure = float(le.rapport_epsilon(torch.from_numpy(v)[:, None])[0])
        assert mesure == pytest.approx(rho, rel=1e-9) and le.independance_tenue(mesure) is tenue
    assert le.independance_tenue(99.0) is False and le.independance_tenue(101.0) is True


def test_independance_a_la_norme_facteur_commun(monde):
    """ρ ≥ 100 : changer la norme de v ne change la lecture que d'un facteur commun compris entre 1 − 1/(2ρ) et 1."""
    v = monde["w_down"][:, 0]
    v = v / v.pow(2).mean().sqrt()
    grand, _ = le.lire(v * 100, None, monde["gamma"], monde["wu"])
    petit, rho = le.lire(v * 0.011, None, monde["gamma"], monde["wu"])       # ρ ≈ 121
    assert 100 <= rho[0] < 130
    rapport = (petit / grand)[grand.abs() > 1e-3]
    assert float(rapport.max() - rapport.min()) < 1e-4 and 1 - 1 / (2 * rho[0]) - 1e-4 < float(rapport.mean()) <= 1.0


# --- imparité et valeurs non finies ---------------------------------------------------------------------------------------------------------
@pytest.mark.parametrize("lentille", K.LENTILLES)
def test_imparite(monde, lentille):
    j = monde["publique"].matrice(15)[0] if lentille == K.LENTILLE_PUBLIQUE else None
    v = monde["w_down"][:, :8]
    plus, _ = le.lire(v, j, monde["gamma"], monde["wu"])
    moins, _ = le.lire(-v, j, monde["gamma"], monde["wu"])
    assert torch.equal(moins, -plus)


def test_valeur_non_finie_dans_une_lecture_arret(monde):
    v = monde["w_down"][:, :2].clone()
    v[3, 1] = float("nan")
    with pytest.raises(Arret, match="valeur non finie"):
        le.lire(v, None, monde["gamma"], monde["wu"])
    v[3, 1] = float("inf")
    with pytest.raises(Arret, match="valeur non finie"):
        le.lire(v, None, monde["gamma"], monde["wu"])
    le.lire(monde["w_down"][:, :2], None, monde["gamma"], monde["wu"])


def test_matrice_de_lentille_d_une_autre_forme_ou_precision_arret(monde):
    v = monde["w_down"][:, :2]
    with pytest.raises(Arret):
        le.transporter(v, torch.eye(D + 1))
    with pytest.raises(Arret):
        le.transporter(v, torch.eye(D, dtype=torch.float64))
    with pytest.raises(Arret):
        le.empreinte_matrice(np.eye(D, dtype=np.float32))
