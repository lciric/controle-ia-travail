"""Essais de la pièce 6 — statistique : Z, maximum, p-valeur, borne basse."""
import numpy as np
import pytest
from scipy.stats import kstest

from controle_ia.devin_v1 import RefusDevin
from controle_ia.devin_v1.graines import graine_tache, generateur_tache
from controle_ia.devin_v1.statistique import (borne_basse, controler_standardisation, forme_observee_lecture,
                                              p_valeur, rangs_centres, epreuve_globale_lecture, epreuve_globale_piece,
                                              z_piece)
from controle_ia.devin_v1.tirage import TireurLecture, TireurPiece, propension_constante

RACINE = 0x94D0_49BB_1331_11EB_BF58_476D_1CE4_E5B9


def racine(*cles):
    """Racine de 128 bits dérivée par tâche (essais reproductibles)."""
    g = graine_tache(RACINE, *cles) if len(cles) == 1 else graine_tache(RACINE, cles[0], *cles[1:])
    v = int.from_bytes(g.generate_state(4, dtype=np.uint32).tobytes(), "big")
    return v | (1 << 127)


def test_cas_sain_p_valeurs_uniformes_sur_1000_repliques():
    n, J, B = 100, 3, 99
    tir = TireurPiece(propension_constante(0.5), depend_du_passe=False)
    ps = []
    for k in range(1000):
        ids = [f"r{k}:{t}" for t in range(n)]
        j = tir.tirer(racine("piece", k), ids, [{}] * n)
        sorties = generateur_tache(RACINE, f"traits{k}").normal(size=(J, n))
        ps.append(epreuve_globale_piece(sorties, j, tir, racine("rejeu", k), B)["p"])
    ps = np.array(ps)
    assert (ps <= 0.05).sum() <= 72          # test de mort 1
    assert kstest(ps, "uniform").pvalue > 0.001


def test_cas_sain_rejeu_dans_l_ordre_valide():
    n, B = 80, 99

    def pi_passe(t, e, passe):
        return np.full(passe.shape[0], 0.3) if passe.shape[1] == 0 else np.where(passe[:, -1] == 1, 0.15, 0.4)

    tir = TireurPiece(pi_passe, True, frozenset({"entrees_consignees", "pieces_passees"}))
    rej = 0
    for k in range(300):
        ids = [f"o{k}:{t}" for t in range(n)]
        j = tir.tirer(racine("po", k), ids, [{}] * n)
        # Prédicteur qui « voit » la pièce précédente : corrélé à π, pas à A − π.
        s = np.r_[0, j.pieces[:-1]][None, :] + 1e-3 * generateur_tache(RACINE, f"b{k}").normal(size=(1, n))
        rej += epreuve_globale_piece(s, j, tir, racine("ro", k), B)["p"] <= 0.05
    assert rej <= 300 * 0.05 + 3 * np.sqrt(300 * 0.05 * 0.95) + 1


def test_artefact_fuite_retrouvee():
    n = 400
    tir = TireurPiece(propension_constante(0.5), False)
    ids = [f"f{t}" for t in range(n)]
    j = tir.tirer(racine("pf"), ids, [{}] * n)
    bruit = generateur_tache(RACINE, "bruit").normal(size=(4, n))
    bruit[2] += 0.6 * j.pieces
    r = epreuve_globale_piece(bruit, j, tir, racine("rf"), 999)
    assert r["p"] <= 0.002 and int(np.argmax(r["Z"])) == 2 and r["exacte"]


def test_artefact_standardisation_sur_les_tirages_nuls_refusee():
    def analytique(R, A, pi, A_nul, pi_nul):
        return z_piece(R, A, pi)

    def sur_les_nuls(R, A, pi, A_nul, pi_nul):
        num = (A - pi) @ R.T
        nul = (A_nul - pi_nul) @ R.T
        return (num - nul.mean(axis=0)) / nul.std(axis=0)

    controler_standardisation(analytique, graine_tache(RACINE, "std"))
    with pytest.raises(RefusDevin, match="standardisation"):
        controler_standardisation(sur_les_nuls, graine_tache(RACINE, "std"))


def test_lecture_exacte_et_forme_observee_non_exacte():
    n = 300
    temoins = generateur_tache(RACINE, "temoins").normal(size=400)
    tl = TireurLecture(temoins, "service")
    ids = [f"l{t}" for t in range(n)]
    j = tl.tirer(racine("pl"), ids)
    sorties = generateur_tache(RACINE, "sl").normal(size=(3, n))
    r0 = epreuve_globale_lecture(sorties, j, tl, racine("rl"), 499)
    sorties[1] += j.lectures
    r1 = epreuve_globale_lecture(sorties, j, tl, racine("rl"), 499)
    assert r0["exacte"] and r1["p"] <= 0.004 and r1["M"] > r0["M"]
    fo = forme_observee_lecture(sorties, j.lectures, [t % 5 for t in range(n)], graine_tache(RACINE, "fo"), 199)
    assert fo["exacte"] is False and "non exacte" in fo["nature"]


def test_predicteur_constant_nomme_et_z_nul():
    n = 50
    tir = TireurPiece(propension_constante(0.5), False)
    j = tir.tirer(racine("pc"), [f"c{t}" for t in range(n)], [{}] * n)
    s = np.vstack([np.ones(n), generateur_tache(RACINE, "c").normal(size=n)])
    r = epreuve_globale_piece(s, j, tir, racine("rc"), 99)
    assert r["predicteurs_constants"] == [0] and r["Z"][0] == 0.0


def test_aucun_repli():
    with pytest.raises(RefusDevin, match="non finie"):
        rangs_centres(np.array([[1.0, np.nan]]))
    with pytest.raises(RefusDevin, match="dégénérées"):
        z_piece(rangs_centres(np.arange(4.0)), np.array([0, 1, 0, 1]), np.array([0.0, 1.0, 0.0, 1.0]))
    assert p_valeur(3.0, np.array([1.0, 2.0, 3.0])) == 0.5


def test_borne_basse_clopper_pearson():
    rng = generateur_tache(RACINE, "bb")
    ya, ye = rng.integers(0, 2, 2000), rng.integers(0, 2, 2000)
    sa, se = rng.normal(size=(2, 2000)), rng.normal(size=(2, 2000))
    saine = borne_basse(sa, ya, se, ye)
    sa[1] += 1.0 * ya; se[1] += 1.0 * ye
    fuite = borne_basse(sa, ya, se, ye, p=0.05)
    assert saine["borne_basse_vt"] < 0.02 and fuite["predicteur"] == 1
    assert 0.25 < fuite["borne_basse_vt"] < fuite["tpr"] - fuite["fpr"]
    assert fuite["biais_au_pire_minimal"] == pytest.approx(0.95 * fuite["borne_basse_vt"])
    with pytest.raises(RefusDevin):
        borne_basse(sa, np.zeros(2000), se, ye)
