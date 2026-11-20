"""Essais de la garde d'égalité au vingtième rang, option 3 (addendum de concentration scellé, `7c738708…`, § 3, EC-6, et
§ 4, point 7 ; GO-2026-11-19-78), cas sain et artefact pour chaque étage :
(i) direction lue : arrêt nommé (liste par score, liste par z, listes du témoin de couche, les deux listes de dix des pôles) ;
(ii) direction nulle : marquée, S_min et S_max, p_bas et p_haut, arrêt nommé si un libellé en dépend ;
(iii) témoin : compté, sans arrêt ; liste de moins de vingt-et-un jetons : garde sans objet, écrit ;
et le compte, au montage, des paires de jetons gardés de même ligne de sortie (couple H2), sans arrêt.
Graines : `numpy.random.SeedSequence`, clés `lentilles-bbis/essai/<garde>` (texte, plan, point 3)."""
from __future__ import annotations

import itertools
import json
from types import SimpleNamespace

import numpy as np
import pytest

torch = pytest.importorskip("torch")

from controle_ia.lentilles_sondes_bbis import audits_v1 as au  # noqa: E402
from controle_ia.lentilles_sondes_bbis import constantes_v1 as K  # noqa: E402
from controle_ia.lentilles_sondes_bbis import lecture_v1 as le  # noqa: E402
from controle_ia.lentilles_sondes_bbis import nuls_v1 as nu  # noqa: E402
from controle_ia.lentilles_sondes_bbis import statistiques_v3 as st  # noqa: E402
from controle_ia.lentilles_sondes_bbis.constantes_v1 import Arret  # noqa: E402

T, M = 200, 60
IDS = np.arange(5000, 5000 + T)
OU = {"cellule": "P-S50", "pli": "e1", "role": "sonde", "vecteur": "w", "signe": "+", "lentille": K.LENTILLE_PUBLIQUE, "couche": 15}


def _rng(garde: str) -> np.random.Generator:
    return nu.Graines().rng(nu.cle_essai(garde))


def _normales(garde: str, *forme) -> torch.Tensor:
    return torch.from_numpy(_rng(garde).standard_normal(forme).astype(np.float32))


def _rangs(valeurs: torch.Tensor) -> list[int]:
    """Indices par valeur décroissante (tri stable)."""
    return np.argsort(-valeurs.numpy(), kind="stable").tolist()


# --- la garde elle-même -----------------------------------------------------------------------------------------------------------------
def test_sain_scores_tous_distincts_aucune_egalite():
    a = _normales("garde-scores-distincts", T)
    g = st.premiers_gardes(a, 20)
    assert g["objet"] and not g["egalite"] and g["rangs_a_egalite"] is None and g["rangs"].tolist() == _rangs(a)[:20]
    assert st.exiger_sans_egalite(a, 20, st.LISTE_PAR_SCORE, IDS, OU)["valeurs"].tolist() == sorted(a.tolist(), reverse=True)[:20]


@pytest.mark.parametrize("rang", [5, 21])
def test_sain_egalite_ailleurs_dans_le_classement_ne_compte_pas(rang):
    """Égalités placées aux rangs 5 et 6, puis aux rangs 21 et 22, d'une direction lue : aucun arrêt."""
    a = _normales("garde-egalite-ailleurs", T)
    ordre = _rangs(a)
    a[ordre[rang]] = a[ordre[rang - 1]]                     # rangs `rang` et `rang + 1` (comptés depuis 1) à égalité
    haut = sorted(a.tolist(), reverse=True)
    assert haut[rang - 1] == haut[rang] and haut[19] != haut[20]
    g = st.exiger_sans_egalite(a, 20, st.LISTE_PAR_SCORE, IDS, OU)
    assert not g["egalite"] and set(g["rangs"].tolist()) == set(ordre[:20])


def test_artefact_egalite_aux_rangs_20_et_21_vue_et_arret_nomme():
    a = _normales("garde-egalite-au-vingtieme-rang", T)
    ordre = _rangs(a)
    a[ordre[20]] = a[ordre[19]]
    g = st.premiers_gardes(a, 20)
    assert g["egalite"] and set(g["rangs_a_egalite"]) == {ordre[19], ordre[20]} and g["valeur_commune"] == float(a[ordre[19]])
    with pytest.raises(st.EgaliteDirectionLue) as e:
        st.exiger_sans_egalite(a, 20, st.LISTE_PAR_SCORE, IDS, OU)
    message = str(e.value)
    assert message.startswith("égalité de score au vingtième rang d'une direction lue")
    for morceau in ("cellule P-S50", "pli e1", "rôle sonde", "vecteur w", "signe +", "lentille publique", "couche 15",
                    f"liste « {st.LISTE_PAR_SCORE} »", str(int(IDS[ordre[19]])), str(int(IDS[ordre[20]])),
                    repr(float(a[ordre[19]])), "nœud"):
        assert morceau in message, morceau
    assert set(e.value.identifiants) == {int(IDS[ordre[19]]), int(IDS[ordre[20]])} and e.value.valeur == float(a[ordre[19]])
    assert isinstance(e.value, Arret)


def test_egalite_exacte_en_simple_precision_et_non_a_une_tolerance_pres():
    """« Par égalité exacte, dans la précision où la liste est classée » : deux valeurs voisines d'un pas de la simple
    précision ne sont pas à égalité ; deux valeurs distinctes en double précision mais égales une fois en simple précision,
    où la liste est classée, le sont."""
    a = _normales("garde-egalite-exacte", T)
    ordre = _rangs(a)
    a[ordre[20]] = torch.nextafter(a[ordre[19]], torch.tensor(-float("inf")))
    assert not st.premiers_gardes(a, 20)["egalite"]
    double = a.double()
    double[ordre[20]] = double[ordre[19]] - 1e-12
    assert not st.premiers_gardes(double, 20)["egalite"] and st.premiers_gardes(double.float(), 20)["egalite"]


@pytest.mark.parametrize("n,objet", [(15, False), (20, False), (21, True)])
def test_liste_de_moins_de_vingt_et_un_jetons_garde_sans_objet_ecrit(n, objet):
    """Pas de vingt-et-unième valeur (jouets seulement) : garde sans objet, écrit ; aucun arrêt, même avec des valeurs égales."""
    a = _normales("garde-sans-objet", n)
    a[1] = a[0]
    a_nul = _normales("garde-sans-objet-nul", n, 30)
    resume = st.resumer_nul(a_nul, {})
    lecture = st.lecture_signe(a, {K.NUL_SIGNES: (a_nul, resume)}, {}, np.arange(n), contexte=OU)
    assert st.premiers_gardes(a, 20)["objet"] is objet
    assert lecture["garde_egalite"]["sans_objet"] is (not objet) and resume.garde_sans_objet is (not objet)
    assert (lecture["garde_egalite"]["note"] == st.SANS_OBJET) is (not objet)
    assert st.egalites_temoins(a_nul)["garde_sans_objet"] is (not objet) and resume.n_marquees == 0


# --- étage (i), direction lue : lentille jouet dont deux jetons ont la même ligne de sortie ------------------------------------------------
D = 24


def _lentille_jouet(garde: str):
    rng = _rng(garde)
    wu = torch.from_numpy(rng.standard_normal((T, D)).astype(np.float32))
    gamma = torch.from_numpy((1 + 0.2 * rng.standard_normal(D)).astype(np.float32))
    j = torch.from_numpy((np.eye(D) + 0.3 * rng.standard_normal((D, D))).astype(np.float16).astype(np.float32))
    v = rng.standard_normal(D).astype(np.float32)
    return wu, gamma, j, v


def _nul(garde: str, wu, gamma, j, m: int = M):
    u = torch.from_numpy(nu._isotropes(_rng(garde), D, m).astype(np.float32))
    a_nul, _ = le.lire(u, j, gamma, wu)
    return a_nul, st.resumer_nul(a_nul, {})


def test_artefact_direction_lue_deux_jetons_de_meme_ligne_de_sortie_aux_rangs_20_et_21():
    """Direction choisie pour que les deux jetons de même ligne de sortie tiennent les rangs 20 et 21 : arrêt, message (i),
    les deux identifiants rendus ; la garde appliquée aux scores de la direction de signe opposé, où ces deux jetons sont en
    queue de classement : pas d'égalité au vingtième rang."""
    wu, gamma, j, v = _lentille_jouet("garde-direction-lue-lignes-egales")
    a, _ = le.lire(v, j, gamma, wu)
    ordre = _rangs(a[:, 0])
    vingtieme, jumeau = ordre[19], ordre[120]
    wu[jumeau] = wu[vingtieme]                               # deux jetons gardés de même ligne de sortie
    assert st.paires_de_lignes_egales(wu.numpy())["paires_de_lignes_egales_octet_pour_octet"] == 1
    a, _ = le.lire(v, j, gamma, wu)
    a = a[:, 0]
    assert float(a[jumeau]) == float(a[vingtieme]) and set(_rangs(a)[19:21]) == {vingtieme, jumeau}
    nuls = {K.NUL_ISOTROPE: _nul("garde-direction-lue-nul", wu, gamma, j)}
    with pytest.raises(st.EgaliteDirectionLue) as e:
        st.lecture_signe(a, nuls, {}, IDS, contexte=OU)
    assert set(e.value.identifiants) == {int(IDS[vingtieme]), int(IDS[jumeau])} and e.value.liste == st.LISTE_PAR_SCORE
    assert str(e.value).startswith(st.MESSAGE_EGALITE_LUE) and e.value.valeur == float(a[vingtieme])
    # signe opposé : les deux jetons sont en queue de classement (rangs T − 20 et T − 19) ; pas d'égalité au vingtième rang
    oppose = st.lecture_signe(-a, nuls, {}, IDS, contexte=OU | {"signe": "-"})
    assert not {int(IDS[vingtieme]), int(IDS[jumeau])} & set(oppose["premiers_par_score"]["ids"])
    assert not st.premiers_gardes(-a, 20)["egalite"]


def test_artefact_egalite_de_z_aux_rangs_20_et_21_de_la_liste_par_z():
    """Une égalité de z aux rangs 20 et 21 de la liste par z (sous le nul isotrope) : arrêt, alors que la liste par score n'a
    aucune égalité au vingtième rang."""
    rng = _rng("garde-liste-par-z")
    echelles = torch.from_numpy(np.exp(rng.standard_normal(T)).astype(np.float32))
    a_nul = _normales("garde-liste-par-z-nul", T, M) * echelles[:, None]
    i, j = 11, 137
    a_nul[j] = a_nul[i]                                      # mêmes scores nuls : même moyenne, même écart type
    a = _normales("garde-liste-par-z-direction", T) * echelles
    resume = st.resumer_nul(a_nul, {})
    z = (a - resume.moyenne) / resume.ecart_type
    autres = sorted((float(x) for n, x in enumerate(z) if n not in (i, j)), reverse=True)
    cible = (autres[18] + autres[19]) / 2                    # entre le 19ᵉ et le 20ᵉ z des autres jetons
    a[i] = a[j] = resume.moyenne[i] + cible * resume.ecart_type[i]
    z = st.z_scores(a, resume)
    assert float(z[i]) == float(z[j]) and set(_rangs(z)[19:21]) == {i, j}
    assert not st.premiers_gardes(a, 20)["egalite"]          # la liste par score n'est pas à égalité au vingtième rang
    with pytest.raises(st.EgaliteDirectionLue) as e:
        st.lecture_signe(a, {K.NUL_ISOTROPE: (a_nul, resume)}, {}, IDS, contexte=OU)
    assert e.value.liste == st.LISTE_PAR_Z.format(nul=K.NUL_ISOTROPE) and set(e.value.identifiants) == {int(IDS[i]), int(IDS[j])}
    # sous le nul des signes, aucune liste par z n'entre en table : pas d'arrêt
    assert "premiers_par_z" not in st.lecture_signe(a, {K.NUL_SIGNES: (a_nul, resume)}, {}, IDS, contexte=OU)["nuls"][K.NUL_SIGNES]


def _poles_jouets(garde: str, neurones: int = 40):
    rng = _rng(garde)
    return torch.from_numpy(rng.standard_normal((D, neurones)).astype(np.float32)), torch.from_numpy(rng.standard_normal(D).astype(np.float32))


def test_sain_poles_sans_egalite_et_artefact_deux_colonnes_egales_au_dixieme_et_au_onzieme_cosinus():
    w_down, v = _poles_jouets("garde-poles")
    nuls = {K.NUL_ISOTROPE: torch.from_numpy(nu._isotropes(_rng("garde-poles-nul"), D, 30).astype(np.float32))}
    sain = st.poles_alignes(v, w_down, nuls, contexte=OU)
    assert len(sain["poles"]) == 10 and sain["garde_egalite_sans_objet"] is False
    dixieme = sain["poles"][9]["neurone"]
    hors = next(n for n in range(w_down.shape[1]) if n not in {p["neurone"] for p in sain["poles"]})
    w_down[:, hors] = w_down[:, dixieme]                     # deux colonnes égales de W_down
    with pytest.raises(st.EgaliteDirectionLue) as e:
        st.poles_alignes(v, w_down, nuls, contexte=OU)
    assert e.value.liste == st.LISTE_POLES and {f"neurone {dixieme} signe {sain['poles'][9]['signe']}",
                                                f"neurone {hors} signe {sain['poles'][9]['signe']}"} == set(e.value.identifiants)
    assert "dixième et la onzième valeur" in str(e.value)
    # une égalité ailleurs (cinquième et sixième cosinus) n'arrête pas
    w_down2, _ = _poles_jouets("garde-poles")
    w_down2[:, hors] = w_down2[:, sain["poles"][4]["neurone"]]
    assert len(st.poles_alignes(v, w_down2, nuls, contexte=OU)["poles"]) == 10


def test_artefact_dix_premiers_jetons_de_la_lecture_d_un_pole_egalite_entre_la_dixieme_et_la_onzieme_valeur():
    a = _normales("garde-lecture-d-un-pole", T)
    liste = st.LISTE_JETONS_POLE.format(neurone=3, signe="+")
    assert not st.exiger_sans_egalite(a, K.K_JETONS_POLE, liste, IDS, OU)["egalite"]
    ordre = _rangs(a)
    a[ordre[10]] = a[ordre[9]]
    with pytest.raises(st.EgaliteDirectionLue, match="dix premiers jetons de la lecture du pôle"):
        st.exiger_sans_egalite(a, K.K_JETONS_POLE, liste, IDS, OU)
    a[ordre[10]] = a[ordre[9]] - 1.0
    a[ordre[20]] = a[ordre[19]]                             # une égalité au vingtième rang ne concerne pas une liste de dix
    assert not st.exiger_sans_egalite(a, K.K_JETONS_POLE, liste, IDS, OU)["egalite"]


# --- étage (ii), direction nulle -------------------------------------------------------------------------------------------------------------
FAMILLE = [3, 17, 42, 77, 101, 150]                         # jetons de la famille jouet « nombres »
MASQUES = {"nombres": torch.tensor([i in FAMILLE for i in range(T)]), "cout": torch.zeros(T, dtype=torch.bool)}


def _nul_jouet(garde: str, m: int = M) -> torch.Tensor:
    return _normales(garde, T, m)


def _marquer(a_nul: torch.Tensor, j: int, plus: list[int], egaux: list[int], seuil: float = 9.0) -> None:
    """Donne à la direction nulle `j` des scores strictement plus grands que `seuil` (distincts) aux jetons `plus`, et le
    score `seuil` aux jetons `egaux` ; tous ses autres scores, gaussiens, restent plus petits."""
    assert float(a_nul[:, j].max()) < seuil
    for n, t in enumerate(plus):
        a_nul[t, j] = seuil + 1.0 + 0.125 * n
    for t in egaux:
        a_nul[t, j] = seuil


def _direction(jetons_hauts: list[int], garde: str = "garde-direction-nulle-lue") -> torch.Tensor:
    """Direction lue jouet : ses vingt premiers jetons sont `jetons_hauts`, sans aucune égalité."""
    a = _normales(garde, T)
    for n, t in enumerate(jetons_hauts):
        a[t] = 20.0 + 0.5 * n
    assert len(set(a.tolist())) == T and set(_rangs(a)[:20]) == set(jetons_hauts)
    return a


def _hors_famille(n: int, sauf=()) -> list[int]:
    return [t for t in range(T) if t not in FAMILLE and t not in sauf][:n]


def test_sain_direction_nulle_marquee_bornes_a_un_cran_libelle_egal_pas_d_arret():
    """Une direction nulle à égalité au vingtième rang, avec S_min < S(v) ≤ S_max, libellé égal aux deux bornes : pas d'arrêt,
    une direction marquée écrite, p_haut − p_bas = 1/(M + 1) ; valeur p écrite égale à p_haut ; attendu calculé sans la
    direction marquée."""
    a_nul = _nul_jouet("garde-direction-nulle-marquee")
    j = 5
    plus = FAMILLE[:2] + _hors_famille(17)                   # 19 jetons strictement plus grands, dont 2 de la famille
    egaux = [FAMILLE[2]] + _hors_famille(2, sauf=plus)       # 3 jetons à égalité au vingtième rang, dont 1 de la famille
    _marquer(a_nul, j, plus, egaux)
    resume = st.resumer_nul(a_nul, MASQUES)
    assert resume.n_marquees == 1 and bool(resume.marquee[j]) and not resume.garde_sans_objet
    assert (int(resume.familles_min["nombres"][j]), int(resume.familles_max["nombres"][j])) == (2, 3)          # S_min, S_max
    a = _direction(FAMILLE[:3] + _hors_famille(17))          # S(v) = 3 pour la famille : S_min < S(v) ≤ S_max
    t = st.lecture_signe(a, {K.NUL_SIGNES: (a_nul, resume)}, MASQUES, IDS, contexte=OU)["nuls"][K.NUL_SIGNES]
    f = t["familles"]["nombres"]
    libres = np.delete(resume.familles_max["nombres"].numpy(), j)
    assert f["n"] == 3 and f["p_haut"] - f["p_bas"] == pytest.approx(1 / (M + 1)) and f["p"] == f["p_haut"]
    assert f["p_bas"] == (1 + int((libres >= 3).sum())) / (M + 1) and f["p_haut"] == (2 + int((libres >= 3).sum())) / (M + 1)
    assert f["attendu"] == pytest.approx(libres.mean()) and t["directions_nulles_marquees"] == 1
    assert f["attendu"] != pytest.approx(resume.familles_max["nombres"].double().mean().item())               # sans la marquée
    assert t["p_part"] == t["p_part_haut"] >= t["p_part_bas"]
    bornes = {"isotrope": (K.NUL_ISOTROPE, f["p_bas"], f["p_haut"], 1), "signes": (K.NUL_SIGNES, f["p_bas"], f["p_haut"], 1)}
    assert st.libelle_sous_departage(st.sur_representee, "compte de la famille nombres", bornes, OU) is False   # libellé égal


def test_sain_direction_nulle_marquee_bornes_a_un_cran_pour_la_part():
    """La même garde pour la part au-dessus du nul : une direction marquée dont un jeton à égalité dépasse le quantile des
    autres et l'autre non (compte de la part : S_min = 19, S_max = 20), et une direction lue de compte 20 : p_haut − p_bas =
    1/(M + 1), et la valeur p écrite est p_haut."""
    a_nul = _nul_jouet("garde-direction-nulle-marquee-part")
    j = 7
    plus = _hors_famille(19)
    dessus, dessous = _hors_famille(2, sauf=plus)
    _marquer(a_nul, j, plus, [dessus, dessous])
    a_nul[dessous, :j] += 30.0                               # ce jeton à égalité ne dépasse pas le quantile 0,99 des autres
    a_nul[dessous, j + 1:] += 30.0
    resume = st.resumer_nul(a_nul, MASQUES)
    assert resume.n_marquees == 1 and (int(resume.compte_part_min[j]), int(resume.compte_part_max[j])) == (19, 20)
    a = _direction(_hors_famille(20, sauf=[dessous]), "garde-direction-nulle-lue-part")
    t = st.lecture_signe(a, {K.NUL_SIGNES: (a_nul, resume)}, MASQUES, IDS, contexte=OU)["nuls"][K.NUL_SIGNES]
    libres = np.delete(resume.compte_part_max.numpy(), j)
    assert t["part"] == 1.0 and t["p_part_bas"] == (1 + int((libres >= 20).sum())) / (M + 1)
    assert t["p_part_haut"] - t["p_part_bas"] == pytest.approx(1 / (M + 1)) and t["p_part"] == t["p_part_haut"] > t["p_part_bas"]
    assert t["directions_nulles_marquees"] == 1


def test_sain_direction_nulle_marquee_hors_de_portee_p_bas_egal_a_p_haut():
    """Une direction marquée avec S_max < S(v) : p_bas = p_haut, pas d'arrêt."""
    a_nul = _nul_jouet("garde-direction-nulle-marquee")
    plus = FAMILLE[:2] + _hors_famille(17)
    _marquer(a_nul, 5, plus, [FAMILLE[2]] + _hors_famille(2, sauf=plus))
    resume = st.resumer_nul(a_nul, MASQUES)
    a = _direction(FAMILLE[:4] + _hors_famille(16))          # S(v) = 4 > S_max = 3
    t = st.lecture_signe(a, {K.NUL_SIGNES: (a_nul, resume)}, MASQUES, IDS, contexte=OU)["nuls"][K.NUL_SIGNES]
    assert resume.n_marquees == 1 and t["familles"]["nombres"]["p_bas"] == t["familles"]["nombres"]["p_haut"]
    assert t["directions_nulles_marquees"] == 1


def test_sain_sans_direction_marquee_p_bas_egal_p_egal_p_haut():
    a_nul = _nul_jouet("garde-direction-nulle-marquee")
    resume = st.resumer_nul(a_nul, MASQUES)
    a = _direction(FAMILLE[:3] + _hors_famille(17))
    t = st.lecture_signe(a, {K.NUL_SIGNES: (a_nul, resume)}, MASQUES, IDS, contexte=OU)["nuls"][K.NUL_SIGNES]
    assert resume.n_marquees == 0 and torch.equal(resume.compte_part_min, resume.compte_part_max)
    assert t["p_part_bas"] == t["p_part"] == t["p_part_haut"] and t["directions_nulles_marquees"] == 0
    f = t["familles"]["nombres"]
    assert f["p_bas"] == f["p"] == f["p_haut"] == (1 + int((resume.familles_max["nombres"] >= 3).sum())) / (M + 1)
    assert f["attendu"] == pytest.approx(resume.familles_max["nombres"].double().mean().item())


def _enumerer(a_nul: torch.Tensor, j: int, k: int = 20) -> dict:
    """Énumération de tous les départages de la direction nulle `j` : les places des k premiers que laissent les jetons de
    score strictement plus grand que le k-ième sont données, de toutes les façons, aux jetons de score égal au k-ième. Rend le
    plus petit et le plus grand compte (part au-dessus du quantile des M − 1 autres ; famille)."""
    y = a_nul.double().numpy()
    colonne = y[:, j]
    seuil = np.sort(colonne)[::-1][k - 1]
    plus, egaux = np.flatnonzero(colonne > seuil).tolist(), np.flatnonzero(colonne == seuil).tolist()
    autres = np.delete(y, j, axis=1)
    quantile = np.quantile(autres, 0.99, axis=1)             # interpolation linéaire sur M − 1 valeurs
    parts, familles = [], []
    for choisis in itertools.combinations(egaux, k - len(plus)):
        premiers = plus + list(choisis)
        parts.append(int((colonne[premiers] > quantile[premiers]).sum()))
        familles.append(sum(1 for t in premiers if t in FAMILLE))
    return {"part": (min(parts), max(parts)), "famille": (min(familles), max(familles)), "departages": len(parts)}


@pytest.mark.parametrize("n_plus,dans_la_famille,au_dessous_du_quantile", [
    (18, (True, False, False), (False, False, False)),       # trois jetons de même score aux rangs 19 à 21 : deux places
    (18, (True, True, False), (True, False, False)),
    (19, (True, False, True), (False, True, False)),         # trois jetons aux rangs 20 à 22 : une place
    (19, (False, False, False), (True, True, False)),
    (17, (True, True, True), (False, False, True)),          # rangs 18 à 20, et un quatrième à égalité au rang 21
    (19, (False, True, False), (True, "entre", True))])      # un jeton entre le quantile des autres et celui des M directions
def test_s_min_et_s_max_egaux_a_l_enumeration_de_tous_les_departages(n_plus, dans_la_famille, au_dessous_du_quantile):
    """S_min et S_max égaux au plus petit et au plus grand S d'une énumération de tous les départages, sur un jouet à trois
    jetons de même score au vingtième rang (et, au dernier cas, quatre)."""
    a_nul = _nul_jouet("garde-enumeration")
    j = 9
    plus = FAMILLE[4:6] + _hors_famille(n_plus - 2)
    libres = iter(_hors_famille(10, sauf=plus))
    egaux = [FAMILLE[n] if dans else next(libres) for n, dans in enumerate(dans_la_famille)]
    if n_plus == 17:
        egaux.append(next(libres))
    _marquer(a_nul, j, plus, egaux)
    for t, dessous in zip(egaux, au_dessous_du_quantile):
        if dessous == "entre":                               # une seule autre direction au-dessus de lui : il dépasse le quantile
            a_nul[t, j + 1] = 15.0                           # 0,99 des M − 1 autres, non celui des M directions, lui compris
            sans, avec = np.delete(a_nul[t].double().numpy(), j), a_nul[t].double().numpy()
            assert np.quantile(sans, 0.99) < float(a_nul[t, j]) < np.quantile(avec, 0.99)
        elif dessous:                                        # ce jeton à égalité ne dépasse pas le quantile 0,99 des autres
            a_nul[t, :j] += 30.0
            a_nul[t, j + 1:] += 30.0
    resume = st.resumer_nul(a_nul, MASQUES)
    attendu = _enumerer(a_nul, j)
    assert bool(resume.marquee[j]) and attendu["departages"] > 1
    assert (int(resume.compte_part_min[j]), int(resume.compte_part_max[j])) == attendu["part"]
    assert (int(resume.familles_min["nombres"][j]), int(resume.familles_max["nombres"][j])) == attendu["famille"]
    assert float(resume.part_min[j]) == pytest.approx(attendu["part"][0] / 20) and float(resume.part_max[j]) == pytest.approx(attendu["part"][1] / 20)
    b = st.bornes_de_departage(a_nul, j, 20, MASQUES)
    assert b["jetons_plus_grands"] == n_plus and b["jetons_a_egalite"] == len(egaux) and b["places"] == 20 - n_plus
    for autre in range(M):                                   # les directions non marquées : S_min = S = S_max
        if not bool(resume.marquee[autre]):
            assert int(resume.compte_part_min[autre]) == int(resume.compte_part_max[autre])


def test_attendu_d_une_famille_sans_aucune_direction_non_marquee_arret():
    comptes = torch.tensor([1, 2, 3])
    assert st.attendu_sans_les_marquees(comptes, torch.tensor([False, True, False])) == 2.0
    with pytest.raises(Arret, match="valeur non finie"):
        st.attendu_sans_les_marquees(comptes, torch.tensor([True, True, True]))


def test_bornes_de_departage_refusees_sans_egalite():
    with pytest.raises(Arret, match="sans égalité"):
        st.bornes_de_departage(_nul_jouet("garde-enumeration"), 0, 20, MASQUES)


def test_egalite_ailleurs_dans_une_direction_nulle_ne_la_marque_pas():
    a_nul = _nul_jouet("garde-direction-nulle-egalite-ailleurs")
    ordre = _rangs(a_nul[:, 4])
    a_nul[ordre[5], 4] = a_nul[ordre[4], 4]                  # rangs 5 et 6
    a_nul[ordre[21], 4] = a_nul[ordre[20], 4]                # rangs 21 et 22
    assert st.resumer_nul(a_nul, MASQUES).n_marquees == 0


def _jouet_decisif(n_famille_de_v: int):
    """Jouet à M = 99 : sous les deux nuls, aucune direction nulle non marquée n'atteint le compte de famille de v ; une
    direction marquée du nul isotrope a S_min = 4 et S_max = 5."""
    iso, signes = _nul_jouet("garde-decisive-isotrope", 99), _nul_jouet("garde-decisive-signes", 99)
    plus = FAMILLE[:4] + _hors_famille(15)
    _marquer(iso, 12, plus, [FAMILLE[4]] + _hors_famille(1, sauf=plus))
    nuls = {K.NUL_ISOTROPE: (iso, st.resumer_nul(iso, MASQUES)), K.NUL_SIGNES: (signes, st.resumer_nul(signes, MASQUES))}
    a = _direction(FAMILLE[:n_famille_de_v] + _hors_famille(20 - n_famille_de_v))
    return st.lecture_signe(a, nuls, MASQUES, IDS, contexte=OU), nuls


def _bornes_famille(lecture: dict) -> dict:
    i, s = lecture["nuls"][K.NUL_ISOTROPE], lecture["nuls"][K.NUL_SIGNES]
    return {"isotrope": (K.NUL_ISOTROPE, i["familles"]["nombres"]["p_bas"], i["familles"]["nombres"]["p_haut"], i["directions_nulles_marquees"]),
            "signes": (K.NUL_SIGNES, s["familles"]["nombres"]["p_bas"], s["familles"]["nombres"]["p_haut"], s["directions_nulles_marquees"])}


def test_artefact_direction_nulle_marquee_decisive_pour_un_libelle_arret_nomme():
    """Jouet à M = 99 où, pour une famille, p_bas = 0,01 sous les deux nuls et p_haut = 0,02 sous l'un d'eux (une direction
    marquée avec S_min < S(v) ≤ S_max ; libellé « sur-représentée » à une borne seulement) : arrêt, message (ii)."""
    lecture, nuls = _jouet_decisif(5)
    bornes = _bornes_famille(lecture)
    assert nuls[K.NUL_ISOTROPE][1].n_marquees == 1 and nuls[K.NUL_SIGNES][1].n_marquees == 0
    assert bornes["isotrope"][1:] == (0.01, 0.02, 1) and bornes["signes"][1:] == (0.01, 0.01, 0)
    assert st.sur_representee(0.01, 0.01) is True and st.sur_representee(0.02, 0.01) is False
    with pytest.raises(st.EgaliteNulleDecisive) as e:
        st.libelle_sous_departage(st.sur_representee, "compte de la famille nombres", bornes, OU)
    message = str(e.value)
    assert message.startswith("égalité au vingtième rang d'une direction nulle, décisive pour un libellé")
    for morceau in ("cellule P-S50", "pli e1", "rôle sonde", "vecteur w", "signe +", "lentille publique", "couche 15",
                    "statistique « compte de la famille nombres »", f"nul {K.NUL_ISOTROPE} : p_bas 0.01, p_haut 0.02, 1 direction",
                    f"nul {K.NUL_SIGNES} : p_bas 0.01, p_haut 0.01, 0 direction", "nœud"):
        assert morceau in message, morceau
    assert isinstance(e.value, Arret) and (e.value.libelle_bas, e.value.libelle_haut) == (True, False)


def test_sain_le_meme_jouet_ou_la_direction_marquee_a_s_max_sous_s_de_v_pas_d_arret():
    lecture, nuls = _jouet_decisif(6)                        # S(v) = 6 > S_max = 5
    bornes = _bornes_famille(lecture)
    assert nuls[K.NUL_ISOTROPE][1].n_marquees == 1
    assert bornes["isotrope"][1:] == (0.01, 0.01, 1) and bornes["signes"][1:] == (0.01, 0.01, 0)
    assert st.libelle_sous_departage(st.sur_representee, "compte de la famille nombres", bornes, OU) is True


def test_libelle_de_la_part_calcule_aux_deux_bornes():
    """Même règle pour la part au-dessus du nul : libellés égaux aux deux bornes → ce libellé ; différents → arrêt nommé."""
    egal = {"isotrope": (K.NUL_ISOTROPE, 0.0005, 0.001, 1), "signes": (K.NUL_SIGNES, 0.005, 0.005, 0)}
    assert st.libelle_sous_departage(st.libelle, "part au-dessus du nul", egal, OU) == st.LIBELLE_CONCENTREE
    differents = {"isotrope": (K.NUL_ISOTROPE, 0.001, 0.0015, 1), "signes": (K.NUL_SIGNES, 0.005, 0.005, 0)}
    with pytest.raises(st.EgaliteNulleDecisive, match="statistique « part au-dessus du nul »"):
        st.libelle_sous_departage(st.libelle, "part au-dessus du nul", differents, OU)
    bord = {"isotrope": (K.NUL_ISOTROPE, 0.04, 0.045, 2), "signes": (K.NUL_SIGNES, 0.05, 0.0505, 1)}
    with pytest.raises(st.EgaliteNulleDecisive):
        st.libelle_sous_departage(st.libelle, "part au-dessus du nul", bord, OU)


# --- étage (iii), témoin -----------------------------------------------------------------------------------------------------------------------
def test_temoin_a_egalite_au_vingtieme_rang_compte_ecrit_pas_d_arret_calibration_inchangee():
    a_nul = _nul_jouet("garde-temoin-nul", 200)
    temoins = _normales("garde-temoin", T, 50)
    resume = st.resumer_nul(a_nul, {})
    assert st.egalites_temoins(temoins) == {"temoins": 50, "a_egalite_au_vingtieme_rang": 0, "garde_sans_objet": False}
    p_avant = st.p_temoins(temoins, resume)
    ordre = _rangs(temoins[:, 3])
    maximum_z = int(((temoins[:, 3] - resume.moyenne) / resume.ecart_type).argmax())
    assert maximum_z not in (ordre[19], ordre[20])
    temoins[ordre[20], 3] = temoins[ordre[19], 3]            # un témoin à égalité au vingtième rang
    assert st.egalites_temoins(temoins) == {"temoins": 50, "a_egalite_au_vingtieme_rang": 1, "garde_sans_objet": False}
    p_apres = st.p_temoins(temoins, resume)                  # pas d'arrêt
    assert np.array_equal(p_avant, p_apres)                  # la concentration n'emploie aucune liste de premiers
    assert au.calibration([p_avant], 200)["compte_p_sous_0_05"] == au.calibration([p_apres], 200)["compte_p_sous_0_05"]


# --- couple H2 : paires de jetons gardés de même ligne de sortie, comptées, sans arrêt --------------------------------------------------------
def test_paires_de_lignes_de_sortie_egales_octet_pour_octet():
    lignes = _rng("garde-lignes-de-sortie").standard_normal((50, 8)).astype(np.float32)
    assert st.paires_de_lignes_egales(lignes) == {"jetons": 50, "paires_de_lignes_egales_octet_pour_octet": 0,
                                                  "groupes_de_lignes_egales": 0, "jetons_dans_un_groupe": 0}
    lignes[7] = lignes[3]                                    # une paire
    lignes[20] = lignes[21] = lignes[22]                     # trois lignes égales : trois paires
    assert st.paires_de_lignes_egales(lignes) == {"jetons": 50, "paires_de_lignes_egales_octet_pour_octet": 4,
                                                  "groupes_de_lignes_egales": 2, "jetons_dans_un_groupe": 5}
    zeros = np.zeros((2, 8), dtype=np.float32)
    zeros[1, 0] = -0.0                                       # égales en valeur, différentes d'un octet : non comptées
    assert st.paires_de_lignes_egales(zeros)["paires_de_lignes_egales_octet_pour_octet"] == 0
    with pytest.raises(Arret):
        st.paires_de_lignes_egales(lignes[0])


# --- dans le lanceur : calcul d'une couche sur un monde miniature ------------------------------------------------------------------------------
pytest.importorskip("transformers")
pytest.importorskip("safetensors")
import lentilles_sondes_bbis_jouets_v5 as J  # noqa: E402
from controle_ia.lentilles_sondes_bbis import entrees_v3 as en  # noqa: E402
from controle_ia.lentilles_sondes_bbis import lanceur_v5 as la  # noqa: E402

NEURONES, COUCHE = 40, 15


def _monde_couche(tmp_path, garde: str) -> SimpleNamespace:
    """Ce qu'il faut à `lanceur_v5._Couche` : lignes de sortie, normalisation, trois matrices de lentille, `W_down`, une sonde."""
    rng = _rng(garde)
    wu = torch.from_numpy(rng.standard_normal((T, D)).astype(np.float32))
    gamma = torch.from_numpy((1 + 0.2 * rng.standard_normal(D)).astype(np.float32))
    matrices = {c: (np.eye(D) + 0.3 * rng.standard_normal((D, D))).astype(np.float16) for c in K.COUCHES}
    w_down = torch.from_numpy(rng.standard_normal((D, NEURONES)).astype(np.float32))
    v = rng.standard_normal(D)
    publique = le.LentillePublique(matrices, {c: le.empreinte_matrice(m) for c, m in matrices.items()})
    charge = SimpleNamespace(wu=wu, gamma=gamma, ids_gardes=IDS, chaines=[f" mot{i}" for i in range(T)], publique=publique,
                             w_down=lambda couche: w_down)
    sonde = en.Sonde("P-S50", "e1", "sonde", True, None, "lineaire", COUCHE, "max", "sonde-jouet", "0" * 64, v, 0.0, None)
    return SimpleNamespace(wu=wu, gamma=gamma, matrices=matrices, w_down=w_down, v=v, charge=charge, sonde=sonde, tmp=tmp_path,
                           j=lambda c: torch.from_numpy(matrices[c].astype(np.float32)))


def _calculer(m: SimpleNamespace):
    r = la.Reglages(largeur=D, m=M, n_temoins_isotrope=40, n_temoins_par_vecteur=20)
    masques = st.masques_familles(m.charge.chaines)
    tableaux: dict = {}
    couche = la._Couche(COUCHE, [(m.sonde, "w", m.v)], m.charge, nu.Graines(), r, masques, tableaux, la.Horloge(m.tmp), lambda: None)
    resume, directions = couche.calculer()
    return resume, directions, tableaux


def _lire(m, vecteur, couche=COUCHE) -> torch.Tensor:
    return le.lire(torch.as_tensor(np.asarray(vecteur, dtype=np.float32)), m.j(couche), m.gamma, m.wu)[0][:, 0]


def test_couche_saine_aucun_arret_comptes_d_egalites_ecrits(tmp_path):
    m = _monde_couche(tmp_path, "garde-couche-saine")
    resume, directions, tableaux = _calculer(m)
    for lentille in K.LENTILLES:
        e = resume["lentilles"][lentille]["egalites_au_vingtieme_rang"]
        assert set(e) == {K.NUL_ISOTROPE, K.NUL_SIGNES}
        assert e[K.NUL_ISOTROPE] == {"directions_nulles": M, "directions_nulles_marquees": 0, "temoins": 40,
                                     "temoins_a_egalite_au_vingtieme_rang": 0, "garde_sans_objet": False}
        assert e[K.NUL_SIGNES]["temoins"] == 20 and e[K.NUL_SIGNES]["directions_nulles_marquees"] == 0
        for t in directions[0]["lectures"][lentille]["signes"].values():
            for nul in t["nuls"].values():
                assert nul["p_part_bas"] == nul["p_part"] == nul["p_part_haut"] and nul["directions_nulles_marquees"] == 0
    assert not tableaux[f"directions_nulles__couche{COUCHE}__publique__{K.NUL_ISOTROPE}__marquee"].any()
    assert np.array_equal(tableaux[f"directions_nulles__couche{COUCHE}__publique__{K.NUL_ISOTROPE}__part_min"],
                          tableaux[f"directions_nulles__couche{COUCHE}__publique__{K.NUL_ISOTROPE}__part_max"])
    assert la._egalites({str(COUCHE): resume}) == {
        "directions_lues_a_egalite": 0, "directions_nulles_marquees": 0, "temoins_a_egalite": 0, "garde_sans_objet": False,
        "note": None, "detail": "couches/<couche>/lentilles/<lentille>/egalites_au_vingtieme_rang"}


def test_couche_direction_nulle_marquee_et_temoin_a_egalite_comptes_ecrits_sans_arret(tmp_path):
    """Dans le calcul d'une couche : deux jetons de même ligne de sortie aux rangs 20 et 21 de la première direction du nul
    isotrope partagé, et deux autres aux rangs 20 et 21 du premier témoin : la direction nulle est marquée, le témoin est
    compté, rien n'arrête, et les comptes sont écrits par (lentille, nul)."""
    m = _monde_couche(tmp_path, "garde-couche-nulle-et-temoin")
    nul = torch.from_numpy(nu.nul_isotrope(nu.Graines(), COUCHE, D, M))
    temoins = torch.from_numpy(nu.temoins_isotropes(nu.Graines(), COUCHE, D, 40))
    ordre_nul = _rangs(le.lire(nul[:, 0], m.j(COUCHE), m.gamma, m.wu)[0][:, 0])
    ordre_temoin = _rangs(le.lire(temoins[:, 0], m.j(COUCHE), m.gamma, m.wu)[0][:, 0])
    assert not {ordre_nul[19], ordre_nul[20]} & {ordre_temoin[19], ordre_temoin[20]}
    m.wu[ordre_nul[20]] = m.wu[ordre_nul[19]]
    m.wu[ordre_temoin[20]] = m.wu[ordre_temoin[19]]
    resume, directions, tableaux = _calculer(m)                                    # aucun arrêt
    e = resume["lentilles"][K.LENTILLE_PUBLIQUE]["egalites_au_vingtieme_rang"][K.NUL_ISOTROPE]
    assert e["directions_nulles_marquees"] >= 1 and e["temoins_a_egalite_au_vingtieme_rang"] >= 1
    marquee = tableaux[f"directions_nulles__couche{COUCHE}__publique__{K.NUL_ISOTROPE}__marquee"]
    assert bool(marquee[0]) and int(marquee.sum()) == e["directions_nulles_marquees"]
    for signe in ("+", "-"):
        t = directions[0]["lectures"][K.LENTILLE_PUBLIQUE]["signes"][signe]["nuls"][K.NUL_ISOTROPE]
        assert t["directions_nulles_marquees"] == e["directions_nulles_marquees"] and t["p_part_bas"] <= t["p_part"] == t["p_part_haut"]
    total = la._egalites({str(COUCHE): resume})
    assert total["directions_nulles_marquees"] == sum(x["directions_nulles_marquees"] for l in resume["lentilles"].values()
                                                      for x in l["egalites_au_vingtieme_rang"].values()) >= 1
    assert total["temoins_a_egalite"] == sum(x["temoins_a_egalite_au_vingtieme_rang"] for l in resume["lentilles"].values()
                                             for x in l["egalites_au_vingtieme_rang"].values()) >= 1


def _sans_egalite_a_sa_couche(m) -> None:
    """Contrôle du montage de l'essai : à la couche de la sonde, aucune liste par score n'est à égalité au vingtième rang."""
    for j in (m.j(COUCHE), None):
        a = le.lire(torch.as_tensor(m.v.astype(np.float32)), j, m.gamma, m.wu)[0][:, 0]
        assert not st.premiers_gardes(a, 20)["egalite"] and not st.premiers_gardes(-a, 20)["egalite"]


def test_couche_artefact_direction_lue_arret_avec_la_cellule_le_pli_le_role_le_vecteur_le_signe_la_lentille_la_couche(tmp_path):
    m = _monde_couche(tmp_path, "garde-couche-direction-lue")
    ordre = _rangs(_lire(m, m.v))
    m.wu[ordre[150]] = m.wu[ordre[19]]
    with pytest.raises(st.EgaliteDirectionLue) as e:
        _calculer(m)
    assert e.value.contexte == {"cellule": "P-S50", "pli": "e1", "role": "sonde", "vecteur": "w", "couche": COUCHE,
                                "lentille": K.LENTILLE_PUBLIQUE, "signe": "+"}
    assert e.value.liste == st.LISTE_PAR_SCORE and set(e.value.identifiants) == {int(IDS[ordre[19]]), int(IDS[ordre[150]])}


def test_couche_artefact_signe_oppose_arret_au_signe_moins(tmp_path):
    """Les deux jetons de même ligne de sortie aux rangs 20 et 21 de la direction de signe opposé : arrêt au signe −."""
    m = _monde_couche(tmp_path, "garde-couche-direction-lue")
    ordre = _rangs(-_lire(m, m.v))
    m.wu[ordre[150]] = m.wu[ordre[19]]
    with pytest.raises(st.EgaliteDirectionLue) as e:
        _calculer(m)
    assert e.value.contexte["signe"] == "-" and e.value.liste == st.LISTE_PAR_SCORE


def test_couche_artefact_liste_du_temoin_de_couche_arret(tmp_path):
    """Égalité au vingtième rang de la lecture de v à une autre couche (témoin de couche), sans égalité à sa couche : arrêt."""
    m = _monde_couche(tmp_path, "garde-couche-temoin-de-couche")
    autre = 7
    ordre = _rangs(_lire(m, m.v, autre))
    m.wu[ordre[150]] = m.wu[ordre[19]]
    _sans_egalite_a_sa_couche(m)
    with pytest.raises(st.EgaliteDirectionLue) as e:
        _calculer(m)
    assert e.value.liste == st.LISTE_TEMOIN_DE_COUCHE.format(couche=autre) and e.value.contexte["couche"] == COUCHE
    assert set(e.value.identifiants) == {int(IDS[ordre[19]]), int(IDS[ordre[150]])}


def test_couche_artefact_lecture_d_un_pole_arret(tmp_path):
    """Égalité entre la dixième et la onzième valeur de la lecture d'un des dix pôles par la lentille publique : arrêt."""
    m = _monde_couche(tmp_path, "garde-couche-lecture-d-un-pole")
    poles = st.poles_alignes(torch.as_tensor(m.v.astype(np.float32)), m.w_down, {})["poles"]
    premier = poles[0]
    colonne = m.w_down[:, premier["neurone"]] * (1.0 if premier["signe"] == "+" else -1.0)
    ordre = _rangs(_lire(m, colonne.numpy()))
    m.wu[ordre[150]] = m.wu[ordre[9]]
    _sans_egalite_a_sa_couche(m)
    with pytest.raises(st.EgaliteDirectionLue) as e:
        _calculer(m)
    assert e.value.liste == st.LISTE_JETONS_POLE.format(neurone=premier["neurone"], signe=premier["signe"])
    assert set(e.value.identifiants) == {int(IDS[ordre[9]]), int(IDS[ordre[150]])}


def test_couche_artefact_deux_colonnes_egales_de_w_down_arret(tmp_path):
    m = _monde_couche(tmp_path, "garde-couche-poles")
    poles = st.poles_alignes(torch.as_tensor(m.v.astype(np.float32)), m.w_down, {})["poles"]
    hors = next(n for n in range(NEURONES) if n not in {p["neurone"] for p in poles})
    m.w_down[:, hors] = m.w_down[:, poles[9]["neurone"]]
    with pytest.raises(st.EgaliteDirectionLue) as e:
        _calculer(m)
    assert e.value.liste == st.LISTE_POLES and e.value.contexte["cellule"] == "P-S50"


# --- dans le lanceur : libellés aux deux bornes ---------------------------------------------------------------------------------------------------
def _direction_etiquetable(lecture: dict) -> tuple[dict, dict]:
    signes = {"+": lecture, "-": lecture}
    d = {"sonde": "P-S50/e1/sonde", "role": "sonde", "vecteur": "w", "couche": COUCHE,
         "_ou": {"cellule": "P-S50", "pli": "e1", "role": "sonde", "vecteur": "w", "couche": COUCHE},
         "lectures": {l: {"signes": json.loads(json.dumps(signes))} for l in K.LENTILLES},
         "poles": {"p": {K.NUL_ISOTROPE: 0.5, K.NUL_SIGNES: 0.5}}}
    tenue = {"tenue": True}
    couches = {str(COUCHE): {"repli_nuls_par_direction": False, "lentilles": {
        l: {"calibration": {K.NUL_ISOTROPE: tenue, K.NUL_SIGNES: tenue}} for l in K.LENTILLES}}}
    return d, couches


def test_etiquetage_artefact_direction_nulle_decisive_arret_avant_toute_table():
    lecture, _ = _jouet_decisif(5)
    d, couches = _direction_etiquetable(lecture)
    with pytest.raises(st.EgaliteNulleDecisive) as e:
        la._etiqueter([d], couches, [f" mot{i}" for i in range(T)], IDS)
    assert e.value.statistique == "compte de la famille nombres" and e.value.contexte["lentille"] in K.LENTILLES
    assert e.value.par_nul[K.NUL_ISOTROPE] == {"p_bas": 0.01, "p_haut": 0.02, "marquees": 1}


def test_etiquetage_sain_direction_marquee_hors_de_portee_libelle_ecrit_avec_p_haut():
    lecture, _ = _jouet_decisif(6)
    d, couches = _direction_etiquetable(lecture)
    la._etiqueter([d], couches, [f" mot{i}" for i in range(T)], IDS)
    t = d["lectures"][K.LENTILLE_PUBLIQUE]["signes"]["+"]
    assert t["familles"]["nombres"]["sur_representee"] is True and t["libelle_part"] in (
        st.LIBELLE_CONCENTREE, st.LIBELLE_INTERMEDIAIRE, st.LIBELLE_NON_DISTINCTE)
    assert t["nuls"][K.NUL_ISOTROPE]["directions_nulles_marquees"] == 1
    assert t["nuls"][K.NUL_ISOTROPE]["familles"]["nombres"]["p"] == t["nuls"][K.NUL_ISOTROPE]["familles"]["nombres"]["p_haut"]


# --- bout en bout : tables, manifeste et rapport du montage -----------------------------------------------------------------------------------
@pytest.fixture(scope="module")
def bout_en_bout(tmp_path_factory):
    tmp = tmp_path_factory.mktemp("garde-egalite-bout-en-bout")
    m = J.monde(tmp, echelles={("P-S75", "e1", "sonde"): 1e-5})          # couche 7 : repli des nuls par direction
    montage = la.monter(m.ctx)
    rapport = json.loads((tmp / "sortie" / "diag" / J.RUN / "montage-lentilles-bbis.json").read_text(encoding="utf-8"))
    rendu = la.calculer(m.ctx, m.entrees, m.registre_bbis)
    tables = json.loads((tmp / "sortie" / rendu["tables"]["chemin"]).read_text(encoding="utf-8"))
    manifeste = json.loads((tmp / "sortie" / rendu["manifeste"]["chemin"]).read_text(encoding="utf-8"))
    return SimpleNamespace(m=m, tmp=tmp, montage=montage, rapport=rapport, rendu=rendu, tables=tables, manifeste=manifeste)


def test_calcul_arret_nomme_d_une_direction_lue_avant_toute_ecriture_de_table(tmp_path, monkeypatch, capsys):
    """Dans le calcul entier (Llama miniature, fausse lentille) : une égalité au vingtième rang d'une direction lue, relevée
    par la garde, arrête le calcul avant toute écriture de table ; ce qui existe est versé, rien n'est supprimé ; la ligne de
    commande rend le code 3, le nom de l'arrêt et le chemin du fichier d'arrêt, jamais le message (version 5 du lanceur).
    L'égalité est ici déclarée par la garde elle-même (la quarantième liste relevée), le reste du chemin étant celui du code."""
    m = J.monde(tmp_path)
    la.monter(m.ctx)
    origine, appels = st.premiers_gardes, {"n": 0}

    def garde_qui_voit_une_egalite(valeurs, k):
        g = origine(valeurs, k)
        appels["n"] += 1
        if appels["n"] == 40:
            g |= {"egalite": True, "rangs_a_egalite": (int(g["rangs"][-1]), int(g["rangs"][-2])), "valeur_commune": float(g["valeurs"][-1])}
        return g
    monkeypatch.setattr(st, "premiers_gardes", garde_qui_voit_une_egalite)
    with pytest.raises(st.EgaliteDirectionLue) as e:
        la.calculer(m.ctx, m.entrees, m.registre_bbis)
    assert str(e.value).startswith(st.MESSAGE_EGALITE_LUE) and e.value.contexte["cellule"] in K.CELLULES
    assert not (m.ctx.sortie / "diag" / J.RUN / "tables-lentilles-bbis.json").exists()            # aucune table écrite
    assert not (m.ctx.sortie / "runs" / J.RUN / "manifeste.json").exists()
    arret = json.loads((m.ctx.sortie / "versement" / J.RUN / "calcul-interrompu" / "arret.json").read_text(encoding="utf-8"))
    assert arret["motif"].startswith(st.MESSAGE_EGALITE_LUE) and (m.ctx.travail / la.MARQUE).is_file()
    # la ligne de commande : code 3, nom de l'arrêt et chemin du fichier d'arrêt sur la sortie d'erreur, rien sur la sortie standard
    autre = J.monde(tmp_path / "ligne-de-commande")
    la.monter(autre.ctx)
    appels["n"] = 0
    monkeypatch.setattr(la, "Contexte", lambda *a, **k: autre.ctx)
    code = la.principal(["calcul", "--travail", str(autre.ctx.travail), "--sortie", str(autre.ctx.sortie), "--run", J.RUN,
                         "--depot", str(autre.ctx.racine_depot), "--registre-propre", str(autre.registre_propre),
                         "--entrees", str(autre.entrees), "--registre-bbis", str(autre.registre_bbis)])
    sortie = capsys.readouterr()
    fichier = autre.ctx.sortie / "versement" / J.RUN / "calcul-interrompu" / "arret.json"
    assert code == 3 and sortie.err == f"ARRÊT : EgaliteDirectionLue ; fichier d'arrêt : {fichier}\n" and sortie.out == ""
    assert json.loads(fichier.read_text(encoding="utf-8"))["motif"].startswith(st.MESSAGE_EGALITE_LUE)


def test_bout_en_bout_l_addendum_cite_a_cote_du_texte(bout_en_bout):
    """EC-4 : le manifeste et les tables citent le chemin et l'empreinte de l'addendum à côté de l'empreinte du texte."""
    addendum = {"chemin": en.ADDENDUM, "sha256": en.EMPREINTE_ADDENDUM}
    b = bout_en_bout
    assert b.tables["addendum"] == addendum and b.tables["texte"]["sha256"] == K.EMPREINTE_TEXTE
    assert b.manifeste["addendum"] == addendum and b.manifeste["preenregistrement"]["sha256"] == K.EMPREINTE_TEXTE
    assert b.manifeste["config"]["addendum"] == en.EMPREINTE_ADDENDUM and b.rapport["addendum"] == addendum
    assert b.manifeste["fiche_code"]["addendum"]["sha256"] == en.EMPREINTE_ADDENDUM
    assert b.rapport["code"]["fiche_code"]["addendum"]["chemin"] == en.ADDENDUM
    assert set(b.manifeste["code"]) == {f"{m}.py" for m in la.MODULES}
    assert "ligne ADDENDUM-CONCENTRATION-LENTILLES-BBIS égale à la fiche du code" in b.rapport["gardes"]["liste"]
    # le manifeste cite toujours le rapport du montage (remarque de la vérification de la version 2 du code)
    assert b.manifeste["rapport_du_montage"] == {"chemin": f"diag/{J.RUN}/montage-lentilles-bbis.json", "sha256": b.montage["sha256"]}


def test_bout_en_bout_montage_compte_des_lignes_de_sortie_egales_sans_arret(bout_en_bout):
    assert bout_en_bout.rapport["lignes_de_sortie_egales"] == {
        "jetons": len(bout_en_bout.m.gardes), "paires_de_lignes_egales_octet_pour_octet": 0, "groupes_de_lignes_egales": 0,
        "jetons_dans_un_groupe": 0}


def test_bout_en_bout_tables_de_la_garde_d_egalite(bout_en_bout):
    tables = bout_en_bout.tables
    assert tables["egalites_au_vingtieme_rang"]["directions_lues_a_egalite"] == 0
    assert tables["egalites_au_vingtieme_rang"]["garde_sans_objet"] is False
    assert "option 3" in tables["conventions"]["garde_d_egalite_au_vingtieme_rang"]
    assert "simple précision" in tables["conventions"]["comparaison_des_concentrations"]
    assert "approchée, non exacte" in tables["conventions"]["loi_des_bornes_de_calibration"]
    for couche, info in tables["couches"].items():
        for lentille in K.LENTILLES:
            e = info["lentilles"][lentille]["egalites_au_vingtieme_rang"]
            attendus = {K.NUL_ISOTROPE, K.NUL_SIGNES} | ({K.NUL_ISOTROPE_PAR_DIRECTION} if info["repli_nuls_par_direction"] else set())
            assert set(e) == attendus, couche
            assert all(x["temoins"] > 0 and x["directions_nulles"] > 0 for x in e.values())
    assert tables["couches"]["7"]["repli_nuls_par_direction"] is True
    lues = [d for d in tables["directions"] if not d.get("non_calculable")]
    assert lues
    for d in lues:
        for lecture in d["lectures"].values():
            for t in lecture["signes"].values():
                assert t["garde_egalite"] == {"sans_objet": False, "note": None}
                for nul in t["nuls"].values():
                    if "non_calculable" in nul:
                        continue
                    assert nul["p_part_bas"] <= nul["p_part"] == nul["p_part_haut"] and "directions_nulles_marquees" in nul
                    for f in nul["familles"].values():
                        assert f["p_bas"] <= f["p"] == f["p_haut"]
        assert d["poles"]["garde_egalite_sans_objet"] is False


def test_bout_en_bout_phrases_rendues_avec_la_valeur_p_ecrite(bout_en_bout):
    """La valeur p écrite dans les tables et les phrases est p_haut ; sans direction marquée, c'est la valeur p."""
    phrases = la.rendre_phrases(bout_en_bout.tables)
    assert phrases["directions"] and all("phrases" in ligne for ligne in phrases["directions"])
