"""Essais de `lecture_entree_v1` et de `comparaisons_lentilles_v1` (texte de lecture v2 scellé, `a2bbed7a…`, « Code neuf »,
essais « lecture », « comparaisons », et, du brouillon 4, la garde de la fonction de lecture aux rangs 10 et 11, la référence
« plongements seuls » et les listes du témoin de couche sous la règle de départage). Cas sain et artefact pour chacun (R5).
Tout sur jouets ; graines `lentilles-bbis-v2/essai/<garde>`."""
from __future__ import annotations

import numpy as np
import pytest

torch = pytest.importorskip("torch")

import lentilles_sondes_bbis_seconde_passe_jouets_v1 as J  # noqa: E402
from controle_ia.lentilles_sondes_bbis import audits_v1 as au  # noqa: E402
from controle_ia.lentilles_sondes_bbis import comparaisons_lentilles_v1 as co  # noqa: E402
from controle_ia.lentilles_sondes_bbis import constantes_v1 as K  # noqa: E402
from controle_ia.lentilles_sondes_bbis import constantes_v2 as K2  # noqa: E402
from controle_ia.lentilles_sondes_bbis import lecture_entree_v1 as li  # noqa: E402
from controle_ia.lentilles_sondes_bbis import lecture_v1 as le  # noqa: E402
from controle_ia.lentilles_sondes_bbis import montage_v1 as mo  # noqa: E402
from controle_ia.lentilles_sondes_bbis import nos_lentilles_v1 as nl  # noqa: E402
from controle_ia.lentilles_sondes_bbis import nuls_v1 as nu  # noqa: E402
from controle_ia.lentilles_sondes_bbis import statistiques_v4 as st  # noqa: E402
from controle_ia.lentilles_sondes_bbis.constantes_v1 import Arret  # noqa: E402

D, T, F, M = 48, 300, 96, 60
IDS = np.arange(7000, 7000 + T)


def _n(garde: str, *forme) -> torch.Tensor:
    return torch.from_numpy(J.rng(garde).standard_normal(forme).astype(np.float32))


@pytest.fixture(scope="module")
def monde():
    """Llama miniature en mémoire : lignes de sortie, plongements (non liés), γ, `W_down`, notre R et notre S par couche."""
    r = {c: torch.eye(D) + 0.5 * _n(f"monde-R-{c}", D, D) for c in K.COUCHES}
    s = {c: _n(f"monde-S-{c}", D, D) for c in K.COUCHES}
    return {"wu": _n("monde-wu", T, D), "e": _n("monde-e", T, D), "gamma": 1 + 0.2 * _n("monde-gamma", D),
            "w_down": _n("monde-w-down", D, F), "R": r, "S": s, "read": mo.charger_read_voisin(J.RACINE / K.COPIE_READOUT)}


def _colonnes(monde, couche):
    return monde["w_down"][:, torch.as_tensor(nu.colonnes_garde(nu.Graines(), couche, F))]


def _suivante(couche):
    couches = sorted(K.COUCHES)
    return couches[(couches.index(couche) + 1) % 3]


# === lecture par notre R : la fonction de la première passe ================================================================================
@pytest.mark.parametrize("couche", K.COUCHES)
def test_notre_r_par_la_fonction_de_la_v1_cas_sain_contre_read_du_voisin_et_artefact_couche_suivante(monde, couche):
    r = li.garde_fonction_lecture_notre_r(monde["read"], _colonnes(monde, couche), monde["gamma"], monde["wu"], monde["R"][couche],
                                          monde["R"][_suivante(couche)], K2.LENTILLE_NOTRE_R, couche)
    assert r["tenue"] and r["colonnes"] == 64 and r["colonnes_differentes_sur_artefact"] >= 32 and r["lentille"] == K2.LENTILLE_NOTRE_R


def test_notre_r_artefact_invisible_ou_ecart_sur_le_cas_sain_arret(monde):
    c = _colonnes(monde, 15)
    with pytest.raises(Arret, match="artefact vu sur 0 colonnes"):
        li.garde_fonction_lecture_notre_r(monde["read"], c, monde["gamma"], monde["wu"], monde["R"][15], monde["R"][15],
                                          K2.LENTILLE_NOTRE_R, 15)

    def voisin_d_une_autre_couche(colonnes, wu, gamma, jacobienne, k):
        return monde["read"](colonnes, wu, gamma, monde["R"][23], k=k)
    with pytest.raises(Arret, match="écart sur le cas sain"):
        li.garde_fonction_lecture_notre_r(voisin_d_une_autre_couche, c, monde["gamma"], monde["wu"], monde["R"][15],
                                          monde["R"][23], K2.LENTILLE_NOTRE_R, 15)


def _voisin_qui_echange(monde, wu, a, b):
    """Voisin jouet : `read`, puis, là où un seul des jetons `a` et `b` est gardé, garde l'autre à sa place."""
    def lire(colonnes, wu_, gamma, jacobienne, k):
        valeurs, ids = monde["read"](colonnes, wu, gamma, jacobienne, k=k)
        ids = ids.clone()
        for j in range(ids.shape[0]):
            garde = set(ids[j].tolist()) & {a, b}
            if len(garde) == 1:
                ids[j][ids[j] == garde.pop()] = b if a in ids[j].tolist() else a
        return valeurs, ids
    return lire


@pytest.mark.parametrize("nuls", [False, True], ids=["scores égaux", "scores nuls"])
def test_garde_de_lecture_deux_jetons_de_meme_score_aux_rangs_10_et_11_ecart_compte_sans_arret(monde, nuls):
    """Cas sain du brouillon 4 : deux jetons de même ligne de sortie (donc de même score pour toute colonne), notre code et
    `read` du voisin gardant chacun l'un des deux : écart compté et rapporté, sans arrêt (scores nuls compris)."""
    wu = monde["wu"].clone()
    c = _colonnes(monde, 7)
    scores, _ = le.lire(c, monde["R"][7], monde["gamma"], wu)
    a, b = (int(x) for x in scores[:, 0].topk(11).indices[9:11])
    wu[b] = wu[a]
    if nuls:
        wu[a], wu[b] = 0.0, 0.0                              # deux lignes nulles : scores nuls, différence relative nulle
        wu[:9] *= 1.0
    scores, _ = le.lire(c, monde["R"][7], monde["gamma"], wu)
    concernees = [j for j in range(64) if {a, b} & set(scores[:, j].topk(10).indices.tolist())
                  and float(scores[a, j]) == float(scores[:, j].topk(10).values[-1])]
    r = le.garde_fonction_lecture(_voisin_qui_echange(monde, wu, a, b), c, monde["gamma"], wu, monde["R"][7], monde["R"][15],
                                  K2.LENTILLE_NOTRE_R, 7)
    assert r["tenue"] and r["ecarts_de_quasi_egalite"] <= len(concernees)
    if not nuls:
        assert r["ecarts_de_quasi_egalite"] >= 1


def test_garde_de_lecture_artefact_ecart_sur_deux_jetons_de_scores_eloignes_arret(monde):
    """Artefact du brouillon 4 : l'écart porte sur deux jetons dont les scores diffèrent de plus de 10⁻⁴ en valeur relative."""
    c = _colonnes(monde, 7)
    scores, _ = le.lire(c, monde["R"][7], monde["gamma"], monde["wu"])
    a, b = (int(x) for x in scores[:, 0].topk(11).indices[9:11])
    assert abs(float(scores[a, 0] - scores[b, 0])) > 1e-4 * abs(float(scores[a, 0]))
    with pytest.raises(Arret, match="écart sur le cas sain"):
        le.garde_fonction_lecture(_voisin_qui_echange(monde, monde["wu"], a, b), c, monde["gamma"], monde["wu"], monde["R"][7],
                                  monde["R"][15], K2.LENTILLE_NOTRE_R, 7)


# === lecture par notre S ======================================================================================================================
@pytest.mark.parametrize("couche", K.COUCHES)
def test_notre_s_cas_sain_contre_le_chemin_independant_et_ses_trois_artefacts(monde, couche):
    r = li.garde_fonction_lecture_entree(_colonnes(monde, couche), monde["S"][couche], monde["S"][_suivante(couche)], monde["e"],
                                         monde["wu"], couche, plongements_lies=False)
    assert r["tenue"] and r["colonnes"] == 64 and r["lentille"] == K2.LENTILLE_NOTRE_S
    assert set(r["colonnes_differentes_sur_artefact"]) == {li.ARTEFACT_COUCHE_SUIVANTE, li.ARTEFACT_TRANSPOSEE, li.ARTEFACT_LIGNES_DE_SORTIE}
    assert all(n >= 32 for n in r["colonnes_differentes_sur_artefact"].values())


def test_notre_s_scores_egaux_au_chemin_independant_en_double_precision(monde):
    c = _colonnes(monde, 15)
    scores, calculable = li.lire_entree(c, monde["S"][15], li.centrer(monde["e"]))
    independant = li.relire_par_chemin_independant(c.T.numpy(), monde["S"][15].numpy(), monde["e"].numpy()).T
    assert calculable.all() and np.allclose(scores.numpy(), independant, rtol=1e-4, atol=1e-5)
    direct = ((c[:, 0].double() @ monde["S"][15].double()) / (c[:, 0].double() @ monde["S"][15].double()).norm()) @ \
        (monde["e"].double() - monde["e"].double().mean(0)).T
    assert np.allclose(scores[:, 0].numpy(), direct.numpy(), rtol=1e-4, atol=1e-5)


@pytest.mark.parametrize("artefact", ["couche suivante", "transposée", "lignes de sortie"])
def test_notre_s_artefact_invisible_arret(monde, artefact):
    """Chaque artefact doit changer la lecture. Rendus invisibles (même matrice ; matrice symétrique ; plongements à la place
    des lignes de sortie), chacun arrête."""
    k = monde["S"][15]
    k_sym = k + k.T
    cas = {"couche suivante": dict(k=k, k_suivante=k, lignes=monde["wu"]),
           "transposée": dict(k=k_sym, k_suivante=monde["S"][23], lignes=monde["wu"]),
           "lignes de sortie": dict(k=k, k_suivante=monde["S"][23], lignes=monde["e"])}[artefact]
    with pytest.raises(Arret, match="vu sur 0 colonnes"):
        li.garde_fonction_lecture_entree(_colonnes(monde, 15), cas["k"], cas["k_suivante"], monde["e"], cas["lignes"], 15, False)


def test_notre_s_ecart_sur_le_cas_sain_arret(monde, monkeypatch):
    """Notre code lit par K, le chemin indépendant par une autre matrice : écart sur le cas sain, arrêt."""
    origine = li.relire_par_chemin_independant
    monkeypatch.setattr(li, "relire_par_chemin_independant", lambda c, k, e: origine(c, monde["S"][23].numpy(), e))
    with pytest.raises(Arret, match="écart sur le cas sain"):
        li.garde_fonction_lecture_entree(_colonnes(monde, 15), monde["S"][15], monde["S"][23], monde["e"], monde["wu"], 15, False)


def test_plongements_lies_artefact_iii_sans_objet_ecrit_et_non_lies_artefact_joue(monde):
    assert li.plongements_lies(monde["wu"], monde["wu"].clone()) and not li.plongements_lies(monde["e"], monde["wu"])
    lies = li.garde_fonction_lecture_entree(_colonnes(monde, 7), monde["S"][7], monde["S"][15], monde["wu"], monde["wu"], 7, True)
    assert lies["colonnes_differentes_sur_artefact"][li.ARTEFACT_LIGNES_DE_SORTIE] == li.SANS_OBJET_PLONGEMENTS_LIES
    assert lies["colonnes_differentes_sur_artefact"][li.ARTEFACT_TRANSPOSEE] >= 32
    non_lies = li.garde_fonction_lecture_entree(_colonnes(monde, 7), monde["S"][7], monde["S"][15], monde["e"], monde["wu"], 7, False)
    assert non_lies["colonnes_differentes_sur_artefact"][li.ARTEFACT_LIGNES_DE_SORTIE] >= 32


def test_imparite_de_s(monde):
    c = _n("imparite", D)
    plus, _ = li.lire_entree(c, monde["S"][7], li.centrer(monde["e"]))
    moins, _ = li.lire_entree(-c, monde["S"][7], li.centrer(monde["e"]))
    assert torch.equal(moins, -plus)


def test_independance_de_s_a_la_norme(monde):
    """c et 10⁻⁴·c rendent les mêmes scores (à l'arrondi de la simple précision près) et les mêmes vingt premiers jetons."""
    c = _n("norme", D)
    centres = li.centrer(monde["e"])
    un, _ = li.lire_entree(c, monde["S"][15], centres)
    petit, _ = li.lire_entree(1e-4 * c, monde["S"][15], centres)
    assert torch.allclose(un, petit, rtol=1e-5, atol=1e-6)
    assert st.premiers_departages(un[:, 0], IDS, 20)["ids"].tolist() == st.premiers_departages(petit[:, 0], IDS, 20)["ids"].tolist()
    rho = le.rapport_epsilon(le.transporter(1e-4 * c, monde["R"][15]))
    assert rho[0] < 100                                           # la même norme lève la garde du rapport à ε d'une lentille R


def test_norme_nulle_de_c_k_non_calculable(monde):
    k = monde["S"][7].clone()
    c = torch.zeros(D)
    c[3] = 1.0
    k[3, :] = 0.0                                                 # c · K = 0
    scores, calculable = li.lire_entree(torch.stack([c, _n("norme-nulle", D)], 1), k, li.centrer(monde["e"]))
    assert calculable.tolist() == [False, True] and bool((scores[:, 0] == 0).all())
    assert "non calculable" in li.MOTIF_NORME_NULLE
    with pytest.raises(Arret, match="valeur non finie dans un nul"):
        li.lire_entree_exigee(c, k, li.centrer(monde["e"]))


def test_reference_plongements_seuls_k_identite_memes_scores_que_la_lecture_par_s(monde):
    c = _n("plongements-seuls", D, 5)
    centres = li.centrer(monde["e"])
    seuls, _ = li.lire_plongements_seuls(c, centres)
    par_identite, _ = li.lire_entree(c, torch.eye(D), centres)
    assert torch.allclose(seuls, par_identite, rtol=1e-6, atol=1e-6)
    direct = (c[:, 0] / c[:, 0].norm()) @ centres.T
    assert torch.allclose(seuls[:, 0], direct, rtol=1e-5, atol=1e-6)


def test_reference_plongements_seuls_et_temoin_de_couche_meme_regle_de_departage(monde):
    """Deux jetons de mêmes plongements (donc de même score d'entrée pour toute direction) placés aux rangs 20 et 21 : le
    plus petit identifiant est gardé, par notre S, par les plongements seuls et par la lecture à une autre couche."""
    e = monde["e"].clone()
    c = _n("departage-entree", D)
    for lire in (lambda x, e_: li.lire_plongements_seuls(x, li.centrer(e_))[0][:, 0],
                 lambda x, e_: li.lire_entree(x, monde["S"][7], li.centrer(e_))[0][:, 0],
                 lambda x, e_: li.lire_entree(x, monde["S"][23], li.centrer(e_))[0][:, 0]):
        e = monde["e"].clone()
        a, b = (int(i) for i in lire(c, e).topk(21).indices[19:21])
        e[b] = e[a]
        scores = lire(c, e)
        if float(scores[a]) != float(scores[b]) or sorted(scores.topk(21).indices[19:21].tolist()) != sorted([a, b]):
            raise AssertionError("jouet à refaire : le recentrage a déplacé les rangs")
        h = st.premiers_departages(scores, IDS, 20)
        assert h["egalite"] and int(IDS[min(a, b)]) in h["ids"].tolist() and int(IDS[max(a, b)]) not in h["ids"].tolist()


# --- indice de couche de nos lentilles, à signature --------------------------------------------------------------------------------------
def _lentille_a_signature(lettre: str) -> nl.NotreLentille:
    """Fausse lentille dont la matrice de la couche ℓ porte une signature propre : J_ℓ = I + ℓ·10⁻²·E, E fixe."""
    e = np.zeros((D, D), dtype=np.float32)
    e[0, 1] = 1.0
    sommes = {c: tuple(((3 * (np.eye(D, dtype=np.float32) + c * 1e-2 * e)) + h * 1e-3 * e.T).astype(np.float32) for h in (0, 1))
              for c in K.COUCHES}
    lentille = nl.NotreLentille(lettre, sommes, (3, 3))
    lentille.relever_empreintes()
    return lentille


@pytest.mark.parametrize("lettre", ["R", "S"])
def test_indice_de_couche_de_nos_lentilles_la_lecture_d_une_sonde_de_couche_l_rend_la_signature_l(lettre):
    lentille = _lentille_a_signature(lettre)
    for couche in K.COUCHES:
        m, indice, _ = lentille.matrice_verifiee(couche)
        assert indice == couche and round(float(m[0, 1]) / 1e-2) == couche
    lentille.decalage = 1
    with pytest.raises(Arret, match="d'un autre indice que la couche"):
        lentille.matrice_verifiee(15)


# --- garde du rapport à ε étendue ---------------------------------------------------------------------------------------------------------
def test_rapport_a_epsilon_une_lentille_sous_100_nuls_refaits_pour_trois_lentilles_moities_non_calculables():
    r = li.garde_rapport_epsilon({K.LENTILLE_PUBLIQUE: 250.0, K.LENTILLE_LOGITS: 300.0, K2.LENTILLE_NOTRE_R: 99.0,
                                  K2.MOITIE_PAIRE: 120.0, K2.MOITIE_IMPAIRE: 130.0})
    assert r["repli"] and r["lentilles_refaites"] == [K.LENTILLE_PUBLIQUE, K.LENTILLE_LOGITS, K2.LENTILLE_NOTRE_R]
    assert r["moities"].startswith("non calculable") and "sans objet" in r["notre_s"]
    moitie = li.garde_rapport_epsilon({K.LENTILLE_PUBLIQUE: 250.0, K.LENTILLE_LOGITS: 300.0, K2.LENTILLE_NOTRE_R: 400.0,
                                       K2.MOITIE_PAIRE: 99.9, K2.MOITIE_IMPAIRE: 130.0})
    assert moitie["repli"] and len(moitie["lentilles_refaites"]) == 3


def test_rapport_a_epsilon_cas_sain_toutes_au_dessus_rien_n_est_refait_et_bord():
    r = li.garde_rapport_epsilon({K.LENTILLE_PUBLIQUE: 100.0, K.LENTILLE_LOGITS: 101.0, K2.LENTILLE_NOTRE_R: 1e4})
    assert not r["repli"] and r["lentilles_refaites"] == [] and r["moities"] is None
    with pytest.raises(Arret, match="notre S n'est pas concernée"):
        li.garde_rapport_epsilon({K2.LENTILLE_NOTRE_S: 1.0})


# === comparaisons ==============================================================================================================================
def test_recouvrement_sur_des_listes_jouets():
    a = list(range(20))
    assert co.recouvrement(a, a) == 20 and co.recouvrement(a, range(100, 120)) == 0 and co.recouvrement(a, range(13, 33)) == 7
    with pytest.raises(Arret, match="doublon"):
        co.recouvrement([1, 1, 2], [1, 2, 3])


def test_recouvrement_des_directions_nulles_egal_a_un_calcul_direct_sur_les_listes_departagees():
    ya, yb = _n("recouvrement-A", T, M), _n("recouvrement-B", T, M)
    yb[:, :10] = ya[:, :10]                                       # dix directions lues de même par les deux lentilles
    ordre = torch.argsort(ya[:, 20], descending=True)
    ya[ordre[20], 20] = ya[ordre[19], 20]                         # une égalité à la limite, départagée
    ra, rb = (st.premiers_departages_colonnes(y, IDS, 20)["rangs"] for y in (ya, yb))
    o = co.recouvrements_colonnes(ra, rb)
    direct = [len(set(sorted(range(T), key=lambda t: (-float(ya[t, j]), int(IDS[t])))[:20])
                  & set(sorted(range(T), key=lambda t: (-float(yb[t, j]), int(IDS[t])))[:20])) for j in range(M)]
    assert o.tolist() == direct and o[:10].tolist() == [20] * 10


def test_p_de_recouvrement_avec_egalites_conservateur_et_mediane():
    nuls = torch.tensor([0, 1, 1, 2, 2, 2, 5, 20])
    assert co.p_recouvrement(nuls, 2) == pytest.approx((1 + 5) / 9)       # les trois égalités comptent contre la direction
    assert co.p_recouvrement(nuls, 3) == pytest.approx((1 + 2) / 9)
    assert co.p_recouvrement(nuls, 21) == pytest.approx(1 / 9)
    assert co.mediane(nuls) == 2.0 and co.mediane(torch.tensor([0, 1, 2, 3])) == 1.5


def test_comparer_une_direction_p_et_mediane_sous_les_deux_nuls():
    rv = (list(range(20)), list(range(5, 25)))
    iso = (torch.arange(20)[:, None].repeat(1, 4), torch.stack([torch.arange(20), torch.arange(10, 30), torch.arange(15, 35),
                                                              torch.arange(100, 120)], 1))
    c = co.comparer(co.PAIRE_PRINCIPALE, rv, {K.NUL_ISOTROPE: iso, K.NUL_SIGNES: iso})
    assert c["recouvrement"] == 15 and c["nuls"][K.NUL_ISOTROPE]["recouvrements_nuls"].tolist() == [20, 10, 5, 0]
    assert c["nuls"][K.NUL_ISOTROPE]["p"] == pytest.approx(2 / 5) and c["nuls"][K.NUL_SIGNES]["mediane"] == 7.5


def test_paires_permises_et_notre_s_comparee_a_aucune_lentille_r():
    for paire in co.PAIRES:
        co.exiger_paire(*paire)
    for paire in co.PAIRES_INTERDITES + ((K.LENTILLE_PUBLIQUE, K.LENTILLE_LOGITS), (K2.PLONGEMENTS_SEULS, K2.LENTILLE_NOTRE_R)):
        with pytest.raises(Arret):
            co.exiger_paire(*paire)
    with pytest.raises(Arret, match="nul isotrope partagé seulement"):
        co.comparer(co.PAIRE_MOITIES, ([1], [1]), {K.NUL_SIGNES: (torch.zeros(1, 2), torch.zeros(1, 2))})


def test_appariement_des_nuls_memes_directions_pour_toutes_les_lentilles_verifie_par_empreinte():
    u = nu.nul_isotrope(nu.Graines(), 15, largeur=D, m=M)
    e = co.empreinte_tirage(u)
    assert co.exiger_appariement({l: co.empreinte_tirage(u.copy()) for l in K2.LENTILLES_V2}) == e
    autre = u.copy()
    autre[0, 0] += 1e-3
    with pytest.raises(Arret, match="non appariées"):
        co.exiger_appariement({K.LENTILLE_PUBLIQUE: e, K2.LENTILLE_NOTRE_R: co.empreinte_tirage(autre)})
    assert co.empreinte_tirage(nu.nul_isotrope(nu.Graines(), 15, largeur=D, m=M)) == e      # mêmes clés de graine, mêmes directions


C, I, N = st.LIBELLE_CONCENTREE, st.LIBELLE_INTERMEDIAIRE, st.LIBELLE_NON_DISTINCTE


@pytest.mark.parametrize("publique, notre_r, recouvrement, attendu", [
    (C, C, co.RECOUVREMENT_AU_DELA, {"libelle": co.LECTURE_COMMUNE}),
    (C, N, co.RECOUVREMENT_NON_DISTINCT, {"libelle": co.LECTURE_PROPRE, "lentille": K.LENTILLE_PUBLIQUE, "autre": K2.LENTILLE_NOTRE_R}),
    (N, C, co.RECOUVREMENT_AU_DELA, {"libelle": co.LECTURE_PROPRE, "lentille": K2.LENTILLE_NOTRE_R, "autre": K.LENTILLE_PUBLIQUE}),
    (N, N, co.RECOUVREMENT_AU_DELA, {"libelle": co.DEUX_NON_DISTINCTES}),
    (C, C, co.RECOUVREMENT_INTERMEDIAIRE, {"libelle": co.MIXTE}),
    (C, C, co.RECOUVREMENT_NON_DISTINCT, {"libelle": co.MIXTE}),
    (C, I, co.RECOUVREMENT_AU_DELA, {"libelle": co.MIXTE}),
    (I, N, co.RECOUVREMENT_NON_DISTINCT, {"libelle": co.MIXTE}),
])
def test_libelles_de_comparaison_sur_cas_jouets(publique, notre_r, recouvrement, attendu):
    assert co.libelle_comparaison(publique, notre_r, recouvrement) == attendu


def test_libelle_du_recouvrement_aux_niveaux_de_la_concentration_et_non_calculable():
    assert co.libelle_recouvrement(0.001, 0.01) == co.RECOUVREMENT_AU_DELA
    assert co.libelle_recouvrement(0.0011, 0.01) == co.RECOUVREMENT_INTERMEDIAIRE
    assert co.libelle_recouvrement(0.001, 0.051) == co.RECOUVREMENT_NON_DISTINCT
    assert co.libelle_recouvrement(0.05, 0.05) == co.RECOUVREMENT_INTERMEDIAIRE
    for motif in (co.MOTIF_CALIBRATION_RECOUVREMENT, co.MOTIF_NUL_REFAIT, co.MOTIF_LENTILLE_NON_LUE, co.MOTIF_LIBELLE_DIFFERENT):
        assert co.non_calculable(motif) == {"libelle": "non calculable", "motif": motif, "en_clair": f"non calculable : {motif}"}
    with pytest.raises(Arret, match="motif de comparaison non calculable inconnu"):
        co.non_calculable("autre")
    with pytest.raises(Arret, match="libellé de lecture inconnu"):
        co.libelle_comparaison("commune", C, co.RECOUVREMENT_AU_DELA)


def test_calibration_du_recouvrement_nul_sain_sous_la_borne_haute_et_recouvrements_forces_au_dessus():
    """Nul sain : témoins et directions nulles lus par deux lentilles jouets indépendantes ; artefact : recouvrements des
    témoins forcés à 20."""
    ya, yb, ta, tb = (_n(f"calibration-{x}", T, n) for x, n in (("A", M), ("B", M), ("tA", 200), ("tB", 200)))
    rangs = lambda y: st.premiers_departages_colonnes(y, IDS, 20)["rangs"]  # noqa: E731
    o_nuls = co.recouvrements_colonnes(rangs(ya), rangs(yb))
    sain = co.calibration_recouvrement([co.p_recouvrement_temoins(rangs(ta), rangs(tb), o_nuls)], m=M)
    haut = au.bornes_calibration([200], M)[1]
    assert sain["tenue"] and sain["q_haut"] == haut and sain["q_bas"] == co.SANS_OBJET_BORNE_BASSE and sain["n"] == 200
    force = co.calibration_recouvrement([co.p_recouvrement_temoins(rangs(ta), rangs(ta), o_nuls)], m=M)
    assert not force["tenue"] and force["compte_p_sous_0_05"] == 200
    assert co.p_recouvrement_temoins(rangs(ta), rangs(tb), o_nuls)[0] == pytest.approx(
        co.p_recouvrement(o_nuls, int(co.recouvrements_colonnes(rangs(ta), rangs(tb))[0])))


def test_correlation_de_pearson_et_son_resume_sous_le_nul_isotrope():
    a, b = _n("correlation-A", T, 5), _n("correlation-B", T, 5)
    r = co.correlation(a, b)
    assert np.allclose(r.numpy(), [np.corrcoef(a[:, j].numpy(), b[:, j].numpy())[0, 1] for j in range(5)], atol=1e-6)
    assert float(co.correlation(a[:, 0], 3 * a[:, 0] + 2)[0]) == pytest.approx(1.0)
    resume = co.resume_correlation(float(r[0]), r)
    assert resume["mediane_nul_isotrope"] == pytest.approx(float(np.median(r.numpy())))
    assert resume["quantile_0_99_nul_isotrope"] <= float(r.max()) + 1e-12
    with pytest.raises(Arret, match="valeur non finie dans une corrélation"):
        co.correlation(torch.ones(T), a[:, 0])


def test_comparaison_des_deux_recouvrements_cote_a_cote():
    assert co.comparer_les_deux_recouvrements(12, 18) == {"publique_et_notre_r": 12, "moities_de_notre_r": 18, "difference": -6}
    assert co.comparer_les_deux_recouvrements(12, None)["difference"] is None


def test_calibration_du_recouvrement_un_compte_sous_la_borne_basse_ne_fait_rien_tomber():
    """La borne basse n'a pas de sens pour le recouvrement (p_O conservateur) : un compte nul, sous la borne basse d'un jeu de
    1 000 témoins, reste tenu. Artefact visé : un code qui applique la borne basse."""
    assert au.bornes_calibration([1000])[0] > 0
    r = co.calibration_recouvrement([np.ones(1000)])
    assert r["compte_p_sous_0_05"] == 0 and r["tenue"] and r["q_bas"] == co.SANS_OBJET_BORNE_BASSE
