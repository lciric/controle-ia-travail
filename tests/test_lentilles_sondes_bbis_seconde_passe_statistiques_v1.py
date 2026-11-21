"""Essais du module des statistiques de la seconde passe (`statistiques_v4`) : texte de lecture v2 scellé (`a2bbed7a…`),
« Code neuf », essais ajoutés par le brouillon 4 — statistique corrigée (concentration et part, chaque direction nulle jugée
sans elle-même), ses deux arrêts, règle de départage des listes de vingt et de dix (identifiant de jeton croissant,
GO-2026-11-19-92), pôles à cosinus égal, comptes d'égalités écrits. Cas sain et artefact pour chacun (R5).
Graines : `numpy.random.SeedSequence`, clés `lentilles-bbis-v2/essai/<garde>` (texte, plan, point 3)."""
from __future__ import annotations

import numpy as np
import pytest

torch = pytest.importorskip("torch")

from controle_ia.lentilles_sondes_bbis import constantes_v1 as K  # noqa: E402
from controle_ia.lentilles_sondes_bbis import nuls_v1 as nu  # noqa: E402
from controle_ia.lentilles_sondes_bbis import statistiques_v1 as origine  # noqa: E402
from controle_ia.lentilles_sondes_bbis import statistiques_v3 as premiere  # noqa: E402
from controle_ia.lentilles_sondes_bbis import statistiques_v4 as st  # noqa: E402
from controle_ia.lentilles_sondes_bbis.constantes_v1 import Arret  # noqa: E402

T, M = 200, 60
IDS = np.arange(5000, 5000 + T)


def _rng(garde: str) -> np.random.Generator:
    return nu.Graines().rng(f"lentilles-bbis-v2/essai/{garde}")


def _normales(garde: str, *forme) -> torch.Tensor:
    return torch.from_numpy(_rng(garde).standard_normal(forme).astype(np.float32))


def _ordre_total(valeurs, ids, k: int) -> list[int]:
    """Référence écrite en toutes lettres : positions des k premiers par valeur décroissante puis identifiant croissant."""
    v, i = np.asarray(valeurs, dtype=np.float32), np.asarray(ids)
    return sorted(range(len(v)), key=lambda t: (-float(v[t]), int(i[t])))[:k]


def _masques(n: int = T) -> dict:
    return {"nombres": torch.arange(n) % 3 == 0, "cout": torch.arange(n) % 7 == 0}


# === statistique corrigée, concentration et part ===========================================================================================
def _direct(y: np.ndarray, ids: np.ndarray, k: int = 20):
    """C(u_j) et le compte de la part de chaque direction nulle, direction par direction, sur les M − 1 autres : moyenne,
    écart type de population, quantile 0,99 par interpolation linéaire sur M − 1 valeurs ; liste départagée."""
    y = y.astype(np.float64)
    m = y.shape[1]
    c, compte = np.empty(m), np.empty(m, dtype=np.int64)
    for j in range(m):
        autres = np.delete(y, j, axis=1)
        z = (y[:, j] - autres.mean(1)) / autres.std(1)
        c[j] = z.max()
        premiers = _ordre_total(y[:, j], ids, k)
        tri = np.sort(autres[premiers], axis=1)
        h = 0.99 * (m - 2)
        bas = int(np.floor(h))
        q = tri[:, bas] + (h - bas) * (tri[:, min(bas + 1, m - 2)] - tri[:, bas])
        compte[j] = int((y[premiers, j] > q).sum())
    return c, compte


@pytest.mark.parametrize("n_jetons, m", [(64, 19), (200, 60), (120, 101)])
def test_sain_concentration_et_part_de_chaque_direction_nulle_egales_a_un_calcul_direct(n_jetons, m):
    y = _normales(f"calcul-direct-{n_jetons}-{m}", n_jetons, m)
    ids = np.arange(900, 900 + n_jetons)
    r = st.resumer_nul(y, {}, ids)
    c, compte = _direct(y.numpy(), ids)
    assert np.allclose(r.concentration.numpy(), c, rtol=1e-5, atol=1e-5)
    assert r.compte_part.tolist() == compte.tolist()
    assert r.concentration.dtype == torch.float32


def test_sain_formules_exactes_du_point_6_egales_au_calcul_direct():
    """z^(−j) = d·√(M/(M − 1)) / √(1 − d²/(M − 1)), d = (a − m)/s : même maximum que le calcul direct."""
    y = _normales("formules-exactes", 80, 40).double()
    m = y.shape[1]
    d = (y - y.mean(1, keepdim=True)) / y.std(1, correction=0, keepdim=True)
    z = d * np.sqrt(m / (m - 1)) / torch.sqrt(1 - d ** 2 / (m - 1))
    c, _ = _direct(y.numpy(), np.arange(80))
    assert np.allclose(z.max(0).values.numpy(), c, rtol=1e-9)
    assert np.allclose(st.resumer_nul(y.float(), {}, np.arange(80)).concentration.numpy(), c, rtol=1e-5, atol=1e-5)


def test_sain_direction_lue_et_temoins_juges_sur_les_m_directions():
    y, a = _normales("lue-sur-m", T, M), _normales("lue-sur-m-v", T)
    r = st.resumer_nul(y, _masques(), IDS)
    lecture = st.lecture_signe(a, {K.NUL_ISOTROPE: (y, r)}, _masques(), IDS)
    yn, an = y.double().numpy(), a.double().numpy()
    z = (an - yn.mean(1)) / yn.std(1)
    t = lecture["nuls"][K.NUL_ISOTROPE]
    assert t["concentration"] == pytest.approx(z.max(), rel=1e-5)
    premiers = _ordre_total(a.numpy(), IDS, 20)
    tri = np.sort(yn, axis=1)
    h = 0.99 * (M - 1)
    q = tri[:, int(h)] + (h - int(h)) * (tri[:, int(h) + 1] - tri[:, int(h)])
    assert t["part"] == pytest.approx((an[premiers] > q[premiers]).mean())
    temoins = _normales("lue-sur-m-temoins", T, 7)
    c_t = ((temoins.double().numpy() - yn.mean(1)[:, None]) / yn.std(1)[:, None]).max(0)
    assert np.allclose(st.concentrations_temoins(temoins, r).numpy(), c_t, rtol=1e-5)


def test_artefact_la_statistique_d_origine_rend_une_concentration_strictement_plus_petite():
    """Jouet où chaque direction nulle a un plus grand z positif : la statistique de la v1 (direction nulle comprise dans sa
    propre référence) est strictement plus petite, pour toute direction."""
    y = _normales("statistique-d-origine", T, M)
    ancienne = origine.resumer_nul(y, {}).concentration
    assert bool((ancienne > 0).all())
    assert bool((st.resumer_nul(y, {}, IDS).concentration > ancienne).all())


def _taux(resumer, garde: str, repliques: int = 2000, m: int = 19, jetons: int = 128) -> float:
    """Part des témoins à p ≤ 0,05, scores gaussiens indépendants ; chaque réplique tire ses propres `m` directions nulles
    et sa direction témoin (un tirage de `m + 1` colonnes par réplique)."""
    rng, petits = _rng(garde), 0
    for _ in range(repliques):
        tirage = torch.from_numpy(rng.standard_normal((jetons, m + 1)).astype(np.float32))
        nul, temoin = tirage[:, :m].contiguous(), tirage[:, m:].contiguous()
        petits += int(st.p_temoins(temoin, resumer(nul))[0] <= 0.05)
    return petits / repliques


def test_taux_a_petite_taille_sous_la_statistique_corrigee():
    assert 0.03 <= _taux(lambda nul: st.resumer_nul(nul, {}, np.arange(128)), "taux-a-petite-taille") <= 0.065


def test_artefact_de_taux_a_petite_taille_sous_la_statistique_d_origine():
    taux = _taux(lambda nul: origine.resumer_nul(nul, {}), "taux-a-petite-taille")
    assert taux > 0.3 and not 0.03 <= taux <= 0.065


def test_comparaison_des_concentrations_en_simple_precision():
    """Deux valeurs égales après arrondi en simple précision comptent contre v ; cas sain : valeurs distinctes."""
    nulles = torch.tensor([1.0, 2.0, 3.0], dtype=torch.float32)
    assert st.p_concentration(nulles, 3.0 + 1e-12) == pytest.approx(2 / 4)       # 3 + 10⁻¹² s'arrondit à 3 : compte contre v
    assert st.p_concentration(nulles, 3.5) == pytest.approx(1 / 4)                # cas sain
    with pytest.raises(Arret, match="simple précision"):
        st.p_concentration(nulles.double(), 3.0)


def test_memes_valeurs_pour_toute_lentille_a_scores_egaux_et_pour_le_nul_refait_par_direction():
    """Le point 6 vaut pour toute lentille : le module ne connaît que des scores. Les mêmes scores, présentés comme lus par la
    lentille publique, par notre R, par notre S ou sous le nul refait par direction, rendent les mêmes valeurs."""
    y, a = _normales("toute-lentille", T, M), _normales("toute-lentille-v", T)
    sorties = []
    for nul in (K.NUL_ISOTROPE, K.NUL_ISOTROPE_PAR_DIRECTION, K.NUL_ISOTROPE):
        r = st.resumer_nul(y.clone(), _masques(), IDS)
        s = st.lecture_signe(a.clone(), {nul: (y, r)}, _masques(), IDS)
        sorties.append((s["premiers_par_score"], s["nuls"][nul]))
    assert sorties[0] == sorties[1] == sorties[2]


# === ses deux arrêts =========================================================================================================================
def test_arret_variance_des_autres_nulle_pour_un_jeton():
    y = _normales("variance-des-autres", 30, 12)
    y[4, :] = 1.0
    y[4, 3] = 2.0                                     # constant sur les onze autres directions
    with pytest.raises(Arret, match="écart type nul d'un jeton sur les autres"):
        st.resumer_nul(y, {}, np.arange(30))


def test_arret_variance_des_autres_au_plus_dix_puissance_moins_dix_fois_celle_des_m():
    y = _normales("variance-relative", 30, 12).double()
    y[4, :] = 1.0 + 1e-9 * torch.arange(12, dtype=torch.float64)
    y[4, 3] = 50.0
    with pytest.raises(Arret, match="écart type nul d'un jeton sur les autres"):
        st.concentrations_sans_soi(y)


def test_arret_nul_de_deux_directions_et_sain_trois_directions_distinctes():
    with pytest.raises(Arret, match="au moins trois directions"):
        st.resumer_nul(_normales("deux-directions", 30, 2), {}, np.arange(30))
    assert st.resumer_nul(_normales("trois-directions", 30, 3), {}, np.arange(30)).m == 3


# === règle de départage, listes de vingt ====================================================================================================
def test_sain_scores_distincts_liste_d_un_tri_simple_et_comptes_nuls():
    a, y = _normales("distincts-v", T), _normales("distincts", T, M)
    h = st.premiers_departages(a, IDS, 20)
    assert h["rangs"].tolist() == torch.argsort(a, descending=True)[:20].tolist() and not h["egalite"] and h["objet"]
    c = st.premiers_departages_colonnes(y, IDS, 20)
    assert c["rangs"].tolist() == torch.argsort(y, dim=0, descending=True)[:20].tolist()
    assert int(c["egalite"].sum()) == 0
    assert st.resumer_nul(y, {}, IDS).n_egalites == 0


def _avec_egalite(garde: str, rang_a: int, rang_b: int) -> tuple[torch.Tensor, int, int]:
    """Vecteur dont les jetons de rangs `rang_a` et `rang_b` (comptés depuis 1, consécutifs) ont le même score."""
    a = _normales(garde, T)
    ordre = torch.argsort(a, descending=True)
    a[ordre[rang_b - 1]] = a[ordre[rang_a - 1]]
    return a, int(ordre[rang_a - 1]), int(ordre[rang_b - 1])


@pytest.mark.parametrize("rangs", [(5, 6), (21, 22)])
def test_sain_egalite_ailleurs_qu_a_la_limite_memes_vingt_identifiants_compte_nul(rangs):
    a, _, _ = _avec_egalite(f"egalite-ailleurs-{rangs[0]}", *rangs)
    h = st.premiers_departages(a, IDS, 20)
    assert not h["egalite"]
    assert set(h["rangs"].tolist()) == set(torch.argsort(a, descending=True)[:20].tolist())
    assert h["rangs"].tolist() == _ordre_total(a, IDS, 20)
    assert not bool(st.egalites_par_colonne(a[:, None], 20)[0])


def test_ordre_dans_la_liste_d_une_direction_nulle_identifiant_croissant_a_score_egal():
    """Égalité aux rangs 5 et 6 d'une direction nulle, identifiants décroissants avec la position : la liste écrite suit
    l'ordre total (score décroissant, puis identifiant croissant), colonne par colonne comme pour un vecteur seul."""
    y = _normales("ordre-dans-la-liste", T, M)
    ordre = torch.argsort(y[:, 11], descending=True)
    y[ordre[5], 11] = y[ordre[4], 11]
    ids = IDS[::-1].copy()
    c = st.premiers_departages_colonnes(y, ids, 20)
    assert c["rangs"].T.tolist() == [_ordre_total(y[:, j], ids, 20) for j in range(M)]
    assert int(c["egalite"].sum()) == 0


def test_artefact_egalite_aux_rangs_20_et_21_le_plus_petit_identifiant_est_garde():
    a, i, j = _avec_egalite("egalite-a-la-limite", 20, 21)
    h = st.premiers_departages(a, IDS, 20)
    petit, grand = (i, j) if IDS[i] < IDS[j] else (j, i)
    assert h["egalite"] and petit in h["rangs"].tolist() and grand not in h["rangs"].tolist()
    assert h["rangs"].tolist() == _ordre_total(a, IDS, 20)


def test_artefact_un_tri_qui_garde_le_plus_grand_identifiant_ou_l_ordre_d_arrivee_est_vu():
    """Identifiants décroissants avec la position : l'ordre d'arrivée garderait la première position, donc le plus grand
    identifiant. La règle garde le plus petit : les deux listes diffèrent, et l'essai le voit."""
    a, i, j = _avec_egalite("ordre-d-arrivee", 20, 21)
    ids = IDS[::-1].copy()
    h = st.premiers_departages(a, ids, 20)
    premier_arrive, second = min(i, j), max(i, j)
    assert ids[premier_arrive] > ids[second]
    assert second in h["rangs"].tolist() and premier_arrive not in h["rangs"].tolist()
    plus_grand = sorted(range(T), key=lambda t: (-float(a[t]), -int(ids[t])))[:20]
    assert set(plus_grand) != set(h["rangs"].tolist())


def test_trois_jetons_de_meme_score_a_cheval_sur_le_vingtieme_rang():
    a = _normales("trois-a-cheval", T)
    ordre = torch.argsort(a, descending=True)
    trois = [int(ordre[r]) for r in (18, 19, 20)]              # rangs 19, 20 et 21
    a[trois] = a[trois[0]].clone()
    h = st.premiers_departages(a, IDS, 20)
    par_id = sorted(trois, key=lambda t: IDS[t])
    assert h["egalite"] and par_id[0] in h["rangs"].tolist() and par_id[1] in h["rangs"].tolist()
    assert par_id[2] not in h["rangs"].tolist()
    assert h["ids"].tolist()[18:] == [int(IDS[par_id[0]]), int(IDS[par_id[1]])]


def test_la_liste_ne_depend_pas_de_l_ordre_des_jetons_a_l_entree():
    a, _, _ = _avec_egalite("jetons-permutes", 20, 21)
    y = _normales("jetons-permutes-nul", T, M)
    y[:, 3] = a
    perm = torch.from_numpy(_rng("jetons-permutes-ordre").permutation(T))
    h, hp = st.premiers_departages(a, IDS, 20), st.premiers_departages(a[perm], IDS[perm.numpy()], 20)
    assert h["ids"].tolist() == hp["ids"].tolist() and h["egalite"] and hp["egalite"]
    c, cp = st.premiers_departages_colonnes(y, IDS, 20), st.premiers_departages_colonnes(y[perm], IDS[perm.numpy()], 20)
    assert torch.as_tensor(IDS)[c["rangs"]].tolist() == torch.as_tensor(IDS[perm.numpy()])[cp["rangs"]].tolist()
    assert c["egalite"].tolist() == cp["egalite"].tolist() and bool(c["egalite"][3])


def test_signe_moins_la_liste_de_moins_v_n_est_pas_celle_de_v_lue_a_l_envers():
    """Deux jetons de même score aux rangs 20 et 21 de −v : la liste de −v garde le plus petit identifiant. Un classement de
    v retourné (les derniers de v pris à l'envers) garderait le plus grand : il est vu."""
    moins, i, j = _avec_egalite("signe-moins", 20, 21)
    v = -moins
    h = st.premiers_departages(-v, IDS, 20)
    petit, grand = (i, j) if IDS[i] < IDS[j] else (j, i)
    assert petit in h["rangs"].tolist() and grand not in h["rangs"].tolist()
    retourne = _ordre_total(v, IDS, T)[::-1][:20]              # classement de v lu à l'envers
    assert grand in retourne and petit not in retourne
    assert retourne != h["rangs"].tolist()


def test_liste_par_z_meme_regle_sur_une_egalite_de_z():
    """Nul de moyenne nulle et d'écart type un pour tous les jetons (construit) : une égalité de score est une égalité de z."""
    y = torch.ones(T, 4)
    y[:, 1], y[:, 2:] = -1.0, 0.0
    y = torch.cat([y, -y], dim=1)                                # moyenne 0, même écart type pour tous les jetons
    a, i, j = _avec_egalite("egalite-de-z", 20, 21)
    r = st.resumer_nul(y + 1e-3 * _normales("egalite-de-z-bruit", 1, 8), {}, IDS)
    r.moyenne, r.ecart_type = torch.zeros(T), torch.ones(T)
    s = st.lecture_signe(a, {K.NUL_ISOTROPE: (y, r)}, {}, IDS)
    petit, grand = (i, j) if IDS[i] < IDS[j] else (j, i)
    par_z = s["nuls"][K.NUL_ISOTROPE]["premiers_par_z"]
    assert s["egalite_a_la_limite"]["par_z"][K.NUL_ISOTROPE] is True
    assert int(IDS[petit]) in par_z["ids"] and int(IDS[grand]) not in par_z["ids"]


def _nul_avec_une_egalite(garde: str, colonne: int = 7) -> torch.Tensor:
    y = _normales(garde, T, M)
    ordre = torch.argsort(y[:, colonne], descending=True)
    y[ordre[20], colonne] = y[ordre[19], colonne]
    return y


def test_part_familles_et_valeurs_p_egales_a_un_calcul_direct_sur_les_listes_departagees():
    y = _nul_avec_une_egalite("direct-sur-listes")
    a, _, _ = _avec_egalite("direct-sur-listes-v", 20, 21)
    masques = _masques()
    r = st.resumer_nul(y, masques, IDS)
    assert r.egalite.tolist() == [j == 7 for j in range(M)]
    _, compte = _direct(y.numpy(), IDS)
    assert r.compte_part.tolist() == compte.tolist()
    listes = [_ordre_total(y[:, j], IDS, 20) for j in range(M)]
    assert r.rangs_premiers.T.tolist() == listes
    for nom, masque in masques.items():
        assert r.familles[nom].tolist() == [int(masque[liste].sum()) for liste in listes]
    s = st.lecture_signe(a, {K.NUL_SIGNES: (y, r)}, masques, IDS)
    premiers = _ordre_total(a, IDS, 20)
    assert s["premiers_par_score"]["rangs_gardes"] == premiers and s["egalite_a_la_limite"]["par_score"] is True
    t = s["nuls"][K.NUL_SIGNES]
    for nom, masque in masques.items():
        n = int(masque[premiers].sum())
        comptes = np.array([int(masque[liste].sum()) for liste in listes])
        assert t["familles"][nom] == {"n": n, "attendu": pytest.approx(comptes.mean()),
                                      "p": pytest.approx((1 + (comptes >= n).sum()) / (M + 1))}
    assert t["p_part"] == pytest.approx((1 + (compte >= round(t["part"] * 20)).sum()) / (M + 1))
    assert t["directions_nulles_a_egalite_a_la_limite"] == 1


def test_la_seconde_passe_ne_marque_ni_n_arrete_la_ou_la_premiere_le_fait():
    """Lien avec la première passe : sur les mêmes scores, la garde à trois étages arrête pour la direction lue et marque la
    direction nulle ; la règle de départage rend une liste et une valeur p comprise entre p_bas et p_haut."""
    y = _nul_avec_une_egalite("lien-premiere-passe")
    a, _, _ = _avec_egalite("lien-premiere-passe-v", 20, 21)
    masques = _masques()
    r1 = premiere.resumer_nul(y, masques)
    assert r1.n_marquees == 1
    with pytest.raises(premiere.EgaliteDirectionLue):
        premiere.lecture_signe(a, {K.NUL_SIGNES: (y, r1)}, masques, IDS)
    r4 = st.resumer_nul(y, masques, IDS)
    assert bool((r4.compte_part >= r1.compte_part_min).all()) and bool((r4.compte_part <= r1.compte_part_max).all())
    b = _normales("lien-premiere-passe-sans-egalite", T)
    un, quatre = premiere.lecture_signe(b, {K.NUL_SIGNES: (y, r1)}, masques, IDS), st.lecture_signe(b, {K.NUL_SIGNES: (y, r4)}, masques, IDS)
    assert un["premiers_par_score"]["ids"] == quatre["premiers_par_score"]["ids"]
    t1, t4 = un["nuls"][K.NUL_SIGNES], quatre["nuls"][K.NUL_SIGNES]
    assert t1["p_part_bas"] <= t4["p_part"] <= t1["p_part_haut"]
    assert t1["p_concentration"] == t4["p_concentration"]


# === règle de départage, listes de dix et pôles ==============================================================================================
def test_dix_premiers_jetons_d_un_pole_egalite_aux_rangs_10_et_11():
    a, i, j = _avec_egalite("jetons-d-un-pole", 10, 11)
    p = st.premiers_jetons_d_un_pole(a, IDS)
    petit, grand = (i, j) if IDS[i] < IDS[j] else (j, i)
    assert p["egalite_a_la_limite"] and int(IDS[petit]) in p["ids"] and int(IDS[grand]) not in p["ids"]
    sain = st.premiers_jetons_d_un_pole(_normales("jetons-d-un-pole-sain", T), IDS)
    assert not sain["egalite_a_la_limite"] and len(sain["ids"]) == 10
    ailleurs, _, _ = _avec_egalite("jetons-d-un-pole-ailleurs", 20, 21)
    assert not st.premiers_jetons_d_un_pole(ailleurs, IDS)["egalite_a_la_limite"]


def test_jetons_communs_par_pole_calcules_sur_les_listes_departagees():
    """Deux lentilles jouets qui rendent les mêmes scores sauf l'ordre des jetons à égalité : mêmes dix identifiants, dix
    jetons communs ; un tri par ordre d'arrivée en donnerait neuf."""
    a, i, j = _avec_egalite("communs-par-pole", 10, 11)
    perm = torch.arange(T)
    perm[[i, j]] = perm[[j, i]]                                  # l'autre lentille voit les deux jetons dans l'autre ordre
    une, autre = st.premiers_jetons_d_un_pole(a, IDS), st.premiers_jetons_d_un_pole(a[perm], IDS[perm.numpy()])
    assert st.jetons_communs(une["ids"], autre["ids"]) == 10
    arrivee = lambda x, ids: [int(ids[t]) for t in np.argsort(-x.numpy(), kind="stable")[:10]]  # noqa: E731
    assert st.jetons_communs(arrivee(a, IDS), arrivee(a[perm], IDS[perm.numpy()])) == 9


def _w_down(garde: str, largeur: int = 16, neurones: int = 40) -> torch.Tensor:
    return _normales(garde, largeur, neurones)


def test_poles_sain_colonnes_distinctes_dix_poles_d_un_tri_simple():
    w, v = _w_down("poles-sain"), _normales("poles-sain-v", 16)
    p = st.poles_alignes(v, w, {})
    cos = st.cosinus_colonnes(v, w)[:, 0]
    ordre = torch.argsort(torch.cat([cos, -cos]), descending=True)[:10].tolist()
    assert [(q["neurone"], q["signe"]) for q in p["poles"]] == [(i % 40, "+" if i < 40 else "-") for i in ordre]
    assert not p["egalite_a_la_limite"] and not p["sans_objet"]
    assert p["concentration"] == pytest.approx(float(cos.abs().max()))


def _poles_avec_colonnes_egales(garde: str, oppose: bool):
    """`W_down` jouet dont deux colonnes (égales, ou opposées) tiennent les dixième et onzième cosinus : la colonne du
    neurone de rang 11 est remplacée par celle du neurone de rang 10 (ou par son opposée)."""
    w, v = _w_down(garde), _normales(garde + "-v", 16)
    cos = st.cosinus_colonnes(v, w)[:, 0]
    ordre = torch.argsort(torch.cat([cos, -cos]), descending=True)
    n10, n11 = int(ordre[9]) % 40, int(ordre[10]) % 40
    assert n10 != n11
    w[:, n11] = -w[:, n10] if oppose else w[:, n10]
    return w, v, n10, n11


def test_poles_deux_colonnes_egales_aux_dixieme_et_onzieme_cosinus_le_plus_petit_indice_est_garde():
    w, v, n10, n11 = _poles_avec_colonnes_egales("poles-colonnes-egales", oppose=False)
    p = st.poles_alignes(v, w, {})
    neurones = [q["neurone"] for q in p["poles"]]
    assert p["egalite_a_la_limite"]
    assert min(n10, n11) in neurones and max(n10, n11) not in neurones


def test_poles_colonne_egale_a_l_opposee_d_une_autre_le_plus_petit_indice_est_garde():
    w, v, n10, n11 = _poles_avec_colonnes_egales("poles-colonne-opposee", oppose=True)
    p = st.poles_alignes(v, w, {})
    gardes = {(q["neurone"], q["signe"]) for q in p["poles"]}
    assert p["egalite_a_la_limite"]
    petit, grand = min(n10, n11), max(n10, n11)
    assert petit in {n for n, _ in gardes} and grand not in {n for n, _ in gardes}
    signes = {n: s for n, s in gardes}
    cos = st.cosinus_colonnes(v, w)[:, 0]
    assert float(cos[n10]) == pytest.approx(-float(cos[n11]))  # même cosinus, signes opposés
    assert signes[petit] == ("+" if float(cos[petit]) > 0 else "-")


def test_poles_colonne_orthogonale_cosinus_nul_aux_deux_signes_le_signe_plus_avant_le_signe_moins():
    """Jouet de moins de dix cosinus positifs : six neurones, trois orthogonaux à v ; la liste de dix s'achève sur des
    cosinus nuls, classés par indice de neurone croissant puis signe + avant signe −."""
    v = torch.zeros(8)
    v[0] = 1.0
    w = torch.zeros(8, 6)
    w[0, 0], w[0, 2], w[0, 4] = 1.0, -0.5, 0.25
    w[1, 0], w[1, 2], w[1, 4] = 0.5, 1.0, 1.0
    w[2, 1], w[3, 3], w[4, 5] = 1.0, 1.0, 1.0                    # neurones 1, 3, 5 orthogonaux à v
    o = st.ordre_des_poles(st.cosinus_colonnes(v, w)[:, 0], 10)
    poles = list(zip(o["neurones"], o["signes"]))
    assert poles[:3] == [(0, "+"), (2, "-"), (4, "+")]
    assert poles[3:9] == [(1, "+"), (1, "-"), (3, "+"), (3, "-"), (5, "+"), (5, "-")]
    assert o["cosinus"][3:9] == [0.0] * 6 and o["objet"]
    assert not o["egalite"]                                      # dixième et onzième valeurs distinctes (négatives)


def test_poles_de_moins_v_ceux_de_v_de_signe_oppose_sans_nouveau_classement():
    """Sur le jouet à cosinus nuls : les pôles de −v sont ceux de v, de signe opposé, dans le même ordre. Un nouveau
    classement de −v rangerait les pôles de cosinus nul dans un autre ordre (signe + avant signe −) : il est vu."""
    v = torch.zeros(8)
    v[0] = 1.0
    w = torch.zeros(8, 6)
    w[0, 0], w[0, 2], w[0, 4] = 1.0, -0.5, 0.25
    w[1, 0], w[1, 2], w[1, 4] = 0.5, 1.0, 1.0
    w[2, 1], w[3, 3], w[4, 5] = 1.0, 1.0, 1.0
    plus = st.poles_alignes(v, w, {})["poles"]
    moins = st.poles_opposes(plus)
    assert [(q["neurone"], q["cosinus"]) for q in moins] == [(q["neurone"], q["cosinus"]) for q in plus]
    assert all(a["signe"] != b["signe"] for a, b in zip(plus, moins))
    reclasse = st.poles_alignes(-v, w, {})["poles"]
    assert [(q["neurone"], q["signe"]) for q in reclasse] != [(q["neurone"], q["signe"]) for q in moins]
    assert {(q["neurone"], q["signe"]) for q in reclasse} == {(q["neurone"], q["signe"]) for q in moins}


# === comptes d'égalités écrits dans les tables ==============================================================================================
def _compter(a, y, temoins, cos, jetons_pole, n_jetons: int = T) -> dict:
    ids = np.arange(n_jetons)
    comptes = st.ComptesEgalites()
    r = st.resumer_nul(y, {}, ids)
    s = st.lecture_signe(a, {K.NUL_ISOTROPE: (y, r)}, {}, ids)
    e = s["egalite_a_la_limite"]
    comptes.liste_de_vingt(15, "publique", st.LISTE_PAR_SCORE, "lue", 1, int(e["par_score"]), e["sans_objet"])
    comptes.liste_de_vingt(15, "publique", K.NUL_ISOTROPE, "lue", 1, int(e["par_z"][K.NUL_ISOTROPE]), e["sans_objet"])
    comptes.liste_de_vingt(15, "publique", K.NUL_ISOTROPE, "nulle", r.m, r.n_egalites, r.sans_objet)
    comptes.liste_de_vingt(15, "publique", K.NUL_ISOTROPE, "temoin", temoins.shape[1], int(st.egalites_par_colonne(temoins).sum()),
                           r.sans_objet)
    o = st.ordre_des_poles(cos, 10)
    comptes.poles_par_cosinus(15, "lue", 1, int(o["egalite"]), not o["objet"])
    p = st.premiers_jetons_d_un_pole(jetons_pole, ids)
    comptes.jetons_d_un_pole(15, "publique", 1, int(p["egalite_a_la_limite"]), p["sans_objet"])
    return comptes.table()


def test_comptes_sain_aucune_egalite_tous_a_zero_ecrits():
    t = _compter(_normales("comptes-sain-v", T), _normales("comptes-sain", T, M), _normales("comptes-sain-t", T, 9),
                 _normales("comptes-sain-cos", 40), _normales("comptes-sain-pole", T))
    cases = t["listes_de_vingt"]["15"]["publique"]
    assert cases[st.LISTE_PAR_SCORE]["lue"] == {"listes": 1, "a_egalite_a_la_limite": 0, "sans_objet": 0}
    assert cases[K.NUL_ISOTROPE]["nulle"] == {"listes": M, "a_egalite_a_la_limite": 0, "sans_objet": 0}
    assert cases[K.NUL_ISOTROPE]["temoin"] == {"listes": 9, "a_egalite_a_la_limite": 0, "sans_objet": 0}
    assert t["listes_de_dix"]["poles_par_cosinus"]["15"]["lue"]["a_egalite_a_la_limite"] == 0
    assert t["listes_de_dix"]["jetons_d_un_pole"]["15/publique"]["a_egalite_a_la_limite"] == 0
    assert t["total_a_egalite"] == 0


def test_comptes_artefact_une_egalite_a_chaque_place_vaut_un_et_zero_ailleurs():
    a, _, _ = _avec_egalite("comptes-artefact-v", 20, 21)
    y = _nul_avec_une_egalite("comptes-artefact")
    temoins = _normales("comptes-artefact-t", T, 9)
    ordre = torch.argsort(temoins[:, 2], descending=True)
    temoins[ordre[20], 2] = temoins[ordre[19], 2]
    cos = _normales("comptes-artefact-cos", 40)
    o = torch.argsort(torch.cat([cos, -cos]), descending=True)
    i10, i11 = int(o[9]), int(o[10])
    cos[i11 % 40] = float(torch.cat([cos, -cos])[i10]) * (1.0 if i11 < 40 else -1.0)
    pole, _, _ = _avec_egalite("comptes-artefact-pole", 10, 11)
    t = _compter(a, y, temoins, cos, pole)
    cases = t["listes_de_vingt"]["15"]["publique"]
    assert cases[st.LISTE_PAR_SCORE]["lue"]["a_egalite_a_la_limite"] == 1
    assert cases[K.NUL_ISOTROPE]["nulle"]["a_egalite_a_la_limite"] == 1
    assert cases[K.NUL_ISOTROPE]["temoin"]["a_egalite_a_la_limite"] == 1
    assert t["listes_de_dix"]["poles_par_cosinus"]["15"]["lue"]["a_egalite_a_la_limite"] == 1
    assert t["listes_de_dix"]["jetons_d_un_pole"]["15/publique"]["a_egalite_a_la_limite"] == 1
    assert t["total_a_egalite"] == 5 + int(cases[K.NUL_ISOTROPE]["lue"]["a_egalite_a_la_limite"])


def test_comptes_une_egalite_ailleurs_dans_le_classement_ne_compte_pas():
    a, _, _ = _avec_egalite("comptes-ailleurs-v", 5, 6)
    y = _normales("comptes-ailleurs", T, M)
    ordre = torch.argsort(y[:, 7], descending=True)
    y[ordre[21], 7] = y[ordre[20], 7]                            # rangs 21 et 22
    pole, _, _ = _avec_egalite("comptes-ailleurs-pole", 11, 12)
    t = _compter(a, y, _normales("comptes-ailleurs-t", T, 9), _normales("comptes-ailleurs-cos", 40), pole)
    assert t["total_a_egalite"] == 0


@pytest.mark.parametrize("n_jetons, sans_objet", [(15, True), (20, True), (21, False)])
def test_comptes_liste_de_moins_de_vingt_et_un_elements_sans_objet_ecrit(n_jetons, sans_objet):
    t = _compter(_normales(f"sans-objet-v-{n_jetons}", n_jetons), _normales(f"sans-objet-{n_jetons}", n_jetons, 12),
                 _normales(f"sans-objet-t-{n_jetons}", n_jetons, 3), _normales("sans-objet-cos", 40),
                 _normales(f"sans-objet-pole-{n_jetons}", n_jetons), n_jetons)
    case = t["listes_de_vingt"]["15"]["publique"][K.NUL_ISOTROPE]["nulle"]
    assert case["sans_objet"] == (12 if sans_objet else 0) and case["a_egalite_a_la_limite"] == 0
    assert ("note" in case) is sans_objet
    onze = st.premiers_jetons_d_un_pole(_normales("sans-objet-dix", 10), np.arange(10))
    assert onze["sans_objet"] and not onze["egalite_a_la_limite"]
    assert st.ordre_des_poles(_normales("sans-objet-poles", 5), 10)["objet"] is False


def test_sorte_de_direction_inconnue_refusee():
    with pytest.raises(Arret, match="sorte de direction inconnue"):
        st.ComptesEgalites().liste_de_vingt(7, "publique", K.NUL_SIGNES, "autre", 1, 0)
