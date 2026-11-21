"""Essais de l'addendum de concentration **scellé** (`prereg/lecture-sondes-bbis-par-lentilles-v1-addendum-concentration-v1.md`,
`7c7387088dd5956d3e75bd8e859346dd4db560582fd2f239d2c892b4d2c22970`), § 3, EC-1 à EC-5, avec les couples C1, C2, C3 et C5 :
statistique des directions nulles sans elles-mêmes (cas sain, artefact, artefact de taux à petite taille), arrêts (variance
des autres nulle, moins de trois directions), clé `ADDENDUM-CONCENTRATION-LENTILLES-BBIS` (registre jouet), bornes de
calibration (exemples du plan, 41 bornes du § 7, programme de l'addendum), précision de la comparaison C(u_j) ≥ C(v).
La garde d'égalité au vingtième rang (EC-6) est éprouvée dans `test_lentilles_sondes_bbis_garde_egalite_v1.py`.
Graines : `numpy.random.SeedSequence`, clés `lentilles-bbis/essai/<garde>` (texte, plan, point 3)."""
from __future__ import annotations

import hashlib
import importlib.util
import json

import numpy as np
import pytest

torch = pytest.importorskip("torch")

import lentilles_sondes_bbis_jouets_v4 as J  # noqa: E402
from controle_ia.lentilles_sondes_bbis import audits_v1 as au  # noqa: E402
from controle_ia.lentilles_sondes_bbis import constantes_v1 as K  # noqa: E402
from controle_ia.lentilles_sondes_bbis import entrees_v3 as en  # noqa: E402
from controle_ia.lentilles_sondes_bbis import nuls_v1 as nu  # noqa: E402
from controle_ia.lentilles_sondes_bbis import statistiques_v1 as origine  # noqa: E402
from controle_ia.lentilles_sondes_bbis import statistiques_v3 as st  # noqa: E402
from controle_ia.lentilles_sondes_bbis.constantes_v1 import Arret, Refus  # noqa: E402

EMPREINTE_ADDENDUM = "7c7387088dd5956d3e75bd8e859346dd4db560582fd2f239d2c892b4d2c22970"
EMPREINTE_BROUILLON = "0a862760025caf11ff66578dc47c53143ee480c173a733920b9f4b9425d59546"
CLE = "ADDENDUM-CONCENTRATION-LENTILLES-BBIS"


def _rng(garde: str) -> np.random.Generator:
    return nu.Graines().rng(nu.cle_essai(garde))


def _scores(garde: str, jetons: int, m: int) -> torch.Tensor:
    return torch.from_numpy(_rng(garde).standard_normal((jetons, m)).astype(np.float32))


# --- l'empreinte de l'addendum dans le code ---------------------------------------------------------------------------------------
def test_le_code_porte_l_empreinte_de_l_addendum_scelle_jamais_celle_du_brouillon():
    assert en.EMPREINTE_ADDENDUM == EMPREINTE_ADDENDUM != EMPREINTE_BROUILLON
    assert en.ADDENDUM == "prereg/lecture-sondes-bbis-par-lentilles-v1-addendum-concentration-v1.md"
    paquet = J.RACINE / "src" / "controle_ia" / "lentilles_sondes_bbis"
    for module in ("entrees_v3.py", "statistiques_v3.py", "lanceur_v4.py"):
        assert EMPREINTE_BROUILLON not in (paquet / module).read_text(encoding="utf-8"), module
    fichier = J.RACINE / en.ADDENDUM
    if fichier.is_file():                                   # l'addendum scellé est sur cette branche : son empreinte est la constante
        assert hashlib.sha256(fichier.read_bytes()).hexdigest() == en.EMPREINTE_ADDENDUM


# --- EC-1 et EC-2, cas sain : égalité à un calcul direct sur les M − 1 autres -----------------------------------------------------------
def _direct(y: np.ndarray, k: int = 20):
    """Calcul direct, direction par direction : moyenne, écart type de population et quantile 0,99 par interpolation linéaire
    (rang fractionnaire h = 0,99 × (n − 1), écrit en toutes lettres) sur les M − 1 autres directions."""
    m = y.shape[1]
    c, compte = np.empty(m), np.empty(m, dtype=np.int64)
    for j in range(m):
        autres = np.delete(y, j, axis=1)
        moyenne = autres.sum(1) / (m - 1)
        ecart = np.sqrt(((autres - moyenne[:, None]) ** 2).sum(1) / (m - 1))        # population : diviseur M − 1 pour M − 1 valeurs
        c[j] = ((y[:, j] - moyenne) / ecart).max()
        haut = np.argsort(-y[:, j], kind="stable")[:min(k, y.shape[0])]
        x = np.sort(autres[haut], axis=1)
        h = 0.99 * (m - 2)
        bas = int(np.floor(h))
        q = x[:, bas] + (h - bas) * (x[:, min(bas + 1, m - 2)] - x[:, bas])
        compte[j] = int((y[haut, j] > q).sum())
    return c, compte


@pytest.mark.parametrize("n_jetons,m", [(300, 200), (50, 37), (120, 2000), (60, 3)])
def test_sain_concentration_et_part_de_chaque_direction_nulle_egales_a_un_calcul_direct(n_jetons, m):
    a_nul = _scores(f"sans-soi-calcul-direct-{n_jetons}-{m}", n_jetons, m) * (1 + torch.arange(n_jetons)[:, None] / n_jetons)
    resume = st.resumer_nul(a_nul, {})
    c, compte = _direct(a_nul.double().numpy())
    assert resume.n_marquees == 0
    assert np.allclose(resume.concentration.numpy(), c, rtol=1e-5, atol=1e-5)
    assert np.array_equal(resume.compte_part_min.numpy(), compte) and np.array_equal(resume.compte_part_max.numpy(), compte)
    assert np.allclose(resume.part_max.numpy(), compte / min(20, n_jetons))


def test_sain_rang_fractionnaire_du_quantile_des_autres_a_la_taille_du_texte():
    """EC-2 : pour une direction nulle, n = M − 1 = 1 999 valeurs, h = 0,99 × 1 998 = 1 978,02 ; pour v et les témoins,
    n = M = 2 000, h = 1 979,01."""
    assert 0.99 * (K.M_NUL - 2) == pytest.approx(1978.02) and 0.99 * (K.M_NUL - 1) == pytest.approx(1979.01)
    a_nul = _scores("quantile-a-la-taille-du-texte", 30, K.M_NUL)
    haut = a_nul.topk(20, dim=0)
    q = st.quantiles_sans_soi(a_nul, haut.indices, haut.values)
    j, i = 7, 3
    autres = np.sort(np.delete(a_nul[haut.indices[i, j]].double().numpy(), j))
    assert autres.size == 1999
    assert float(q[i, j]) == pytest.approx(autres[1978] + 0.02 * (autres[1979] - autres[1978]), rel=1e-6)
    resume = st.resumer_nul(a_nul, {})
    t = np.sort(a_nul[0].double().numpy())
    assert float(resume.quantile[0]) == pytest.approx(t[1979] + 0.01 * (t[1980] - t[1979]), rel=1e-6)


def test_artefact_la_statistique_du_texte_d_origine_rend_des_concentrations_strictement_plus_petites():
    """EC-5, artefact : direction nulle comprise dans sa moyenne et son écart type, la concentration est strictement plus
    petite (le plus grand z de chaque direction nulle est ici positif) ; la moyenne, l'écart type et le quantile des M
    directions, qui servent à la direction lue et aux témoins, ne changent pas."""
    a_nul = _scores("statistique-d-origine-plus-petite", 500, 400)
    masques = {"nombres": torch.from_numpy(_rng("statistique-d-origine-familles").random(500) < 0.1)}
    neuf, ancien = st.resumer_nul(a_nul, masques), origine.resumer_nul(a_nul, masques)
    assert bool((ancien.concentration > 0).all()) and bool((ancien.concentration < neuf.concentration).all())
    assert torch.equal(neuf.moyenne, ancien.moyenne) and torch.equal(neuf.ecart_type, ancien.ecart_type)
    assert torch.equal(neuf.quantile, ancien.quantile) and torch.equal(neuf.familles_max["nombres"], ancien.familles["nombres"])
    assert bool((neuf.part_max >= ancien.part - 1e-7).all()) and not torch.allclose(neuf.part_max, ancien.part)


def test_relation_exacte_entre_le_z_sans_soi_et_le_z_avec_soi():
    """EC-1 : C(u_j) = φ(max_t d), φ(d) = d · √(M/(M − 1)) / √(1 − d²/(M − 1)), d étant le z avec elle-même."""
    m = 50
    a_nul = _scores("relation-exacte", 80, m).double()
    d = ((a_nul - a_nul.mean(1, keepdim=True)) / a_nul.std(1, correction=0, keepdim=True)).max(0).values
    phi = d * np.sqrt(m / (m - 1)) / torch.sqrt(1 - d ** 2 / (m - 1))
    assert torch.allclose(st.concentrations_sans_soi(a_nul.float()).double(), phi, rtol=1e-5)


# --- EC-5, artefact de taux à petite taille (couple C3) ----------------------------------------------------------------------------------
def _taux(module, garde: str, repliques: int = 2000, m: int = 19, jetons: int = 128) -> float:
    """Part des témoins à p ≤ 0,05 sur des scores gaussiens indépendants : **chaque réplique tire ses propres `m` directions
    nulles et sa direction témoin** (un tirage de `m + 1` colonnes par réplique)."""
    rng = _rng(garde)
    petits = 0
    for _ in range(repliques):
        tirage = torch.from_numpy(rng.standard_normal((jetons, m + 1)).astype(np.float32))
        nul, temoin = tirage[:, :m].contiguous(), tirage[:, m:].contiguous()
        petits += int(module.p_temoins(temoin, module.resumer_nul(nul, {}))[0] <= 0.05)
    return petits / repliques


def test_taux_a_petite_taille_sous_la_statistique_corrigee():
    """M = 19, 128 jetons, 2 000 répliques : part exigée entre 0,03 et 0,065 (≈ 0,045 selon la simulation de l'addendum)."""
    assert 0.03 <= _taux(st, "taux-a-petite-taille") <= 0.065


def test_artefact_de_taux_a_petite_taille_sous_la_statistique_du_texte_d_origine():
    """Mêmes tirages, statistique du texte d'origine (direction nulle comprise) : ≈ 0,47, loin hors de l'intervalle exigé."""
    taux = _taux(origine, "taux-a-petite-taille")
    assert taux > 0.3 and not 0.03 <= taux <= 0.065


# --- EC-5, arrêts (couple C2) ----------------------------------------------------------------------------------------------------------
def test_arret_variance_des_autres_nulle_pour_un_jeton():
    a = _scores("jeton-constant-sur-les-autres", 10, 5)
    a[4] = torch.tensor([1.0, 1.0, 1.0, 1.0, 7.0])       # constant une fois la cinquième direction retirée
    with pytest.raises(Arret, match="autres directions nulles"):
        st.resumer_nul(a, {})
    a[4] = torch.tensor([1.0, 1.0 + 1e-7, 1.0, 1.0, 7.0])    # variance des autres ≤ 10⁻¹⁰ fois celle des M : arrêt aussi
    with pytest.raises(Arret, match="autres directions nulles"):
        st.resumer_nul(a, {})


def test_arret_deux_directions_nulles_et_sain_trois_directions_de_scores_distincts():
    with pytest.raises(Arret, match="au moins trois directions"):
        st.resumer_nul(torch.tensor([[1.0, 2.0], [0.5, 3.0]]), {})
    resume = st.resumer_nul(torch.tensor([[1.0, 2.0, 4.0], [0.5, 3.0, -1.0]]), {})         # trois directions, scores distincts
    assert resume.m == 3 and bool(torch.isfinite(resume.concentration).all())


# --- EC-4 (couple C1) : clé de l'addendum, registre jouet ----------------------------------------------------------------------------------
def _registre(tmp_path, lignes: list[tuple[str, str, str, str]]):
    p = tmp_path / "lecture-sondes-bbis-par-lentilles-v1.md"
    p.write_text("# Registre propre jouet\n\n" + "".join(f"| {c} | {h} | {ch} | {s} |\n" for c, h, ch, s in lignes), encoding="utf-8")
    return p


H1, H2, H3, H4 = "2026-11-19T00:00:00Z", "2026-11-19T00:00:01Z", "2026-11-19T00:00:02Z", "2026-11-19T00:00:03Z"
SCELLEMENT = ("SCELLEMENT-LENTILLES-BBIS", H1, K.TEXTE, K.EMPREINTE_TEXTE)
GO = ("GO-LENTILLES-BBIS", H1, "registres/jouet.md", "4" * 64)
ADDENDUM_SAIN = (CLE, H2, en.ADDENDUM, en.EMPREINTE_ADDENDUM)
CODE = ("CODE-LENTILLES-BBIS", H3, "registres/jouet.md", "4" * 64)
ENTREES = ("ENTREES-LENTILLES-BBIS", H4, "diag/x/entrees-lentilles-bbis.json", "6" * 64)


def test_cle_de_l_addendum_saine_acceptee(tmp_path):
    propre = _registre(tmp_path, [SCELLEMENT, GO, ADDENDUM_SAIN, CODE, ENTREES])
    ligne = en.exiger_addendum(propre, en.ADDENDUM, en.EMPREINTE_ADDENDUM)
    assert (ligne.cle, ligne.heure, ligne.chemin, ligne.sha256) == ADDENDUM_SAIN
    assert set(en.exiger_registre_propre(propre)) == {"SCELLEMENT-LENTILLES-BBIS", "GO-LENTILLES-BBIS", "CODE-LENTILLES-BBIS", CLE}
    # même seconde que CODE-LENTILLES-BBIS, mais placée avant elle : inscrite avant (précision de lecture déclarée)
    (tmp_path / "s").mkdir()
    meme_seconde = _registre(tmp_path / "s", [SCELLEMENT, GO, (CLE, H3, en.ADDENDUM, en.EMPREINTE_ADDENDUM), CODE])
    assert en.exiger_addendum(meme_seconde, en.ADDENDUM, en.EMPREINTE_ADDENDUM).heure == H3


@pytest.mark.parametrize("lignes,motif", [
    ([SCELLEMENT, GO, CODE], "absente"),
    ([SCELLEMENT, GO, ADDENDUM_SAIN, ADDENDUM_SAIN, CODE], "plusieurs lignes"),
    ([SCELLEMENT, GO, ADDENDUM_SAIN, (CLE, H2, en.ADDENDUM, "9" * 64), CODE], "plusieurs lignes"),
    ([SCELLEMENT, GO, CODE, (CLE, H4, en.ADDENDUM, en.EMPREINTE_ADDENDUM)], "inscrite après CODE-LENTILLES-BBIS"),
    ([SCELLEMENT, GO, (CLE, H4, en.ADDENDUM, en.EMPREINTE_ADDENDUM), CODE], "inscrite après CODE-LENTILLES-BBIS"),      # heure postérieure
    ([SCELLEMENT, GO, ("ENTREES-LENTILLES-BBIS", H1, "diag/x/e.json", "6" * 64), ADDENDUM_SAIN, CODE],
     "inscrite après ENTREES-LENTILLES-BBIS"),
    ([SCELLEMENT, GO, (CLE, H2, en.ADDENDUM, EMPREINTE_BROUILLON), CODE], "ne cite pas l'addendum scellé"),
    ([SCELLEMENT, GO, (CLE, H2, "prereg/autre-texte.md", en.EMPREINTE_ADDENDUM), CODE], "ne cite pas l'addendum scellé")])
def test_cle_de_l_addendum_artefacts_refus(tmp_path, lignes, motif):
    propre = _registre(tmp_path, lignes)
    with pytest.raises(Refus, match=motif):
        en.exiger_addendum(propre, en.ADDENDUM, en.EMPREINTE_ADDENDUM)
    with pytest.raises(Refus, match=motif):
        en.exiger_registre_propre(propre)


def test_cle_de_l_addendum_d_une_autre_empreinte_que_celle_de_la_fiche_du_code_refus(tmp_path):
    propre = _registre(tmp_path, [SCELLEMENT, GO, ADDENDUM_SAIN, CODE])
    with pytest.raises(Refus, match="que ceux que porte la fiche du code"):
        en.exiger_addendum(propre, en.ADDENDUM, EMPREINTE_BROUILLON)
    with pytest.raises(Refus, match="que ceux que porte la fiche du code"):
        en.exiger_addendum(propre, "prereg/autre-texte.md", en.EMPREINTE_ADDENDUM)


def test_seules_les_cles_nommees_sortent_du_registre(tmp_path):
    propre = _registre(tmp_path, [SCELLEMENT, ("LIGNE-JAMAIS-LUE", H1, "diag/secret.json", "2" * 64), ADDENDUM_SAIN, CODE])
    lignes = en.lignes_ordonnees(propre, (CLE, "CODE-LENTILLES-BBIS"))
    assert [l.cle for _, l in lignes] == [CLE, "CODE-LENTILLES-BBIS"] and lignes[0][0] < lignes[1][0]
    with pytest.raises(Refus):
        en.lignes_ordonnees(tmp_path / K.REGISTRE_INTERDIT, (CLE,))


def test_ouverture_et_recuperation_refusees_sans_la_cle_de_l_addendum(tmp_path):
    """Rien n'est ouvert ni demandé sans la clé : cas sain, puis registre propre sans la ligne de l'addendum."""
    m = J.monde_entrees(tmp_path)
    assert len(en.ouvrir_entrees(m.racine, m.registre_bbis, m.registre_propre, J.LARGEUR).sondes) == 20
    _, sans = J.ecrire_registres(tmp_path / "sans-addendum", m.sha_e2, propres=(
        "ABSENCE-VERDICT-LENTILLES-BBIS", "SCELLEMENT-LENTILLES-BBIS", "GO-LENTILLES-BBIS", "CODE-LENTILLES-BBIS"))
    with pytest.raises(Refus, match=f"{CLE} absente"):
        en.ouvrir_entrees(m.racine, m.registre_bbis, sans, J.LARGEUR)
    with pytest.raises(Refus, match=f"{CLE} absente"):
        en.recuperer_entrees("url-jamais-contactee", tmp_path / "recuperation", m.registre_bbis, sans)
    assert not (tmp_path / "recuperation").exists()


# --- EC-4 : fiche du code, montage, ligne de commande (lanceur) ---------------------------------------------------------------------------
pytest.importorskip("transformers")
pytest.importorskip("safetensors")
from controle_ia.lentilles_sondes_bbis import lanceur_v4 as la  # noqa: E402


def test_fiche_du_code_qui_porte_l_addendum_saine(tmp_path):
    _, propre = J.ecrire_registres(tmp_path / "r")
    J.ecrire_fiche_code(tmp_path / "depot", propre)
    rendu = la.exiger_fiche_code(tmp_path / "depot", propre)
    assert rendu["addendum"] == {"chemin": en.ADDENDUM, "sha256": EMPREINTE_ADDENDUM, "heure_de_la_ligne": J.HEURE}
    assert "entrees_v3" in la.MODULES and "statistiques_v3" in la.MODULES and "lanceur_v4" in la.MODULES


@pytest.mark.parametrize("addendum,motif", [
    (None, "sans le chemin et l'empreinte de l'addendum"),
    ({"chemin": "prereg/x.md"}, "sans le chemin et l'empreinte de l'addendum"),
    ({"chemin": en.ADDENDUM, "sha256": EMPREINTE_BROUILLON}, "que ceux que porte la fiche du code"),
    ({"chemin": "prereg/autre-texte.md", "sha256": EMPREINTE_ADDENDUM}, "que ceux que porte la fiche du code")])
def test_fiche_du_code_sans_l_addendum_ou_d_une_autre_empreinte_refus(tmp_path, addendum, motif):
    _, propre = J.ecrire_registres(tmp_path / "r")
    J.ecrire_fiche_code(tmp_path / "depot", propre, addendum=addendum)
    with pytest.raises(Refus, match=motif):
        la.exiger_fiche_code(tmp_path / "depot", propre)


def _sans_la_ligne(propre, cle=CLE, ajouter: str | None = None):
    lignes = [l for l in propre.read_text(encoding="utf-8").splitlines() if not l.startswith(f"| {cle} |")]
    propre.write_text("\n".join(lignes + ([ajouter] if ajouter else [])) + "\n", encoding="utf-8")


@pytest.mark.parametrize("cas,motif", [("absente", "absente"), ("double", "plusieurs lignes"), ("apres-code", "inscrite après"),
                                       ("autre-empreinte", "ne cite pas l'addendum scellé")])
def test_montage_rien_ne_part_sans_la_cle_de_l_addendum_avant_toute_requete(tmp_path, cas, motif):
    m = J.monde(tmp_path)
    ligne = f"| {CLE} | {J.HEURE} | {en.ADDENDUM} | {en.EMPREINTE_ADDENDUM} |"
    propre = m.registre_propre
    if cas == "absente":
        _sans_la_ligne(propre)
    elif cas == "double":
        texte = propre.read_text(encoding="utf-8")
        propre.write_text(texte.replace(ligne + "\n", ligne + "\n" + ligne + "\n"), encoding="utf-8")
    elif cas == "apres-code":
        _sans_la_ligne(propre, ajouter=ligne)
    else:
        propre.write_text(propre.read_text(encoding="utf-8").replace(en.EMPREINTE_ADDENDUM, EMPREINTE_BROUILLON), encoding="utf-8")
    with pytest.raises(Refus, match=motif):
        la.monter(m.ctx)
    assert m.transport.appels == [] and not m.ctx.travail.exists()        # avant toute requête, rien n'est créé


def test_ligne_de_commande_recuperer_refuse_sans_la_cle_de_l_addendum(tmp_path, capsys):
    bbis, propre = J.ecrire_registres(tmp_path / "r")
    J.ecrire_fiche_code(tmp_path / "depot", propre)
    _sans_la_ligne(propre)
    code = la.principal(["recuperer", "--url", "url-jamais-contactee", "--entrees", str(tmp_path / "e"), "--registre-bbis", str(bbis),
                         "--registre-propre", str(propre), "--depot", str(tmp_path / "depot")])
    sortie = capsys.readouterr()
    assert code == 3 and sortie.err.startswith(f"ARRÊT : {CLE} absente") and sortie.out == "" and not (tmp_path / "e").exists()


def test_calcul_refuse_sans_la_cle_de_l_addendum_sans_rien_ouvrir(tmp_path):
    """Calcul refusé avant le départ : aucun fichier des sondes n'est ouvert, rien n'est versé."""
    m = J.monde(tmp_path)
    (m.ctx.travail).mkdir(parents=True)
    (m.ctx.travail / la.MARQUE).write_text("jouet\n")
    _sans_la_ligne(m.registre_propre)
    with pytest.raises(Refus, match=f"{CLE} absente"):
        la.calculer(m.ctx, m.entrees, m.registre_bbis)
    assert not (m.ctx.sortie / "versement").exists()


def test_calcul_rapport_du_montage_absent_rien_ne_part(tmp_path):
    """Remarque non bloquante de la vérification de la version 2 du code, reprise dans `lanceur_v4` : le rapport du montage
    est exigé au départ du calcul (le manifeste le cite toujours) ; absent : rien ne part, rien n'est versé ni supprimé.
    Cas sain : `test_bout_en_bout_l_addendum_cite_a_cote_du_texte` (garde d'égalité), où le manifeste cite le rapport."""
    m = J.monde(tmp_path)
    la.monter(m.ctx)
    rapport = m.ctx.sortie / "diag" / J.RUN / "montage-lentilles-bbis.json"
    rapport.rename(tmp_path / "rapport-deplace.json")
    with pytest.raises(Arret, match="rapport du montage absent du dossier de sortie"):
        la.calculer(m.ctx, m.entrees, m.registre_bbis)
    assert not (m.ctx.sortie / "versement").exists() and (m.ctx.travail / la.MARQUE).is_file()
    assert not (m.ctx.sortie / "diag" / J.RUN / "tables-lentilles-bbis.json").exists()


# --- EC-3 et EC-5 : bornes de calibration ----------------------------------------------------------------------------------------------------
# Addendum scellé, § 7 : nombre k de jeux de 200 témoins mis en commun → [q_bas, q_haut] ; valeurs recopiées du texte scellé.
BORNES_JEUX_DE_200 = {
    1: (1, 24), 2: (6, 39), 3: (12, 53), 4: (18, 66), 5: (26, 79), 6: (33, 92), 7: (41, 104), 8: (48, 116), 9: (56, 128),
    10: (64, 140), 11: (72, 152), 12: (81, 164), 13: (89, 176), 14: (97, 187), 15: (106, 199), 16: (114, 210), 17: (123, 222),
    18: (131, 233), 19: (140, 245), 20: (149, 256), 21: (157, 267), 22: (166, 279), 23: (175, 290), 24: (183, 301),
    25: (192, 312), 26: (201, 323), 27: (210, 335), 28: (219, 346), 29: (228, 357), 30: (236, 368), 31: (245, 379),
    32: (254, 390), 33: (263, 401), 34: (272, 412), 35: (281, 423), 36: (290, 434), 37: (299, 445), 38: (308, 456),
    39: (317, 467), 40: (326, 478)}
BORNE_UN_JEU_DE_1000 = (23, 85)
PIECES = J.RACINE / "prereg" / "pieces-lecture-sondes-bbis-par-lentilles-v1"
PROGRAMME_BORNES = ("bornes_calibration_statistique_corrigee_v2.py", "0f31484b5e2c0fe98a584d8011bede8734fca62eae1f2b6d36d17638638ed34c")
SORTIE_BORNES = ("sortie-bornes-calibration-statistique-corrigee-v2.txt", "39a410e46c4cd938e082a6d9ed3bdcc8b9a0b7365e80ad9efcd5de60b53d540e")


def test_bornes_egales_aux_exemples_du_plan():
    assert au.parametres_beta(2000) == (100, 1901)
    assert (au.bornes_calibration([1000]), au.bornes_calibration([200]), au.bornes_calibration([200] * 3),
            au.bornes_calibration([200] * 5)) == ((23, 85), (1, 24), (12, 53), (26, 79))


def test_les_41_bornes_du_paragraphe_7_de_l_addendum_egales_a_celles_du_code():
    assert au.bornes_calibration([1000]) == BORNE_UN_JEU_DE_1000
    assert sorted(BORNES_JEUX_DE_200) == list(range(1, 41)) and 1 + len(BORNES_JEUX_DE_200) == 41
    for k, attendue in BORNES_JEUX_DE_200.items():
        assert au.bornes_calibration([200] * k) == attendue, k


def test_artefact_une_loi_decalee_d_un_cran_change_des_bornes():
    """Loi faussée d'un cran (99 au lieu de 100 directions nulles au-dessus du seuil) : l'essai des 41 bornes le verrait."""
    def bornes_faussees(jeux):
        pmf = [1.0]
        for n in jeux:
            pmf = au.convoluer(pmf, au.pmf_beta_binomiale(n, 99, 1902))
        return au.bornes(pmf)
    assert any(bornes_faussees([200] * k) != b for k, b in BORNES_JEUX_DE_200.items())


def test_bornes_egales_a_la_sortie_scellee_du_programme_de_l_addendum():
    """EC-3 : bornes « égales à celles du programme `bornes_calibration_statistique_corrigee_v2.py` de l'addendum » : la
    sortie scellée du programme (empreinte de l'addendum) porte les 41 bornes ; elles égalent le texte et le code."""
    sortie = PIECES / SORTIE_BORNES[0]
    if not sortie.is_file():
        pytest.skip("sortie du programme des bornes de l'addendum absente de cette branche")
    assert hashlib.sha256(sortie.read_bytes()).hexdigest() == SORTIE_BORNES[1]
    lues = {}
    for ligne in sortie.read_text(encoding="utf-8").splitlines():
        cellules = [c.strip() for c in ligne.split("|")]
        if len(cellules) > 3 and cellules[2].startswith("[") and (cellules[0].startswith("nul isotrope partagé") or "jeu(x) de 200" in cellules[0]):
            cle = "isotrope" if cellules[0].startswith("nul isotrope") else int(cellules[0].split()[0])
            lues.setdefault(cle, tuple(json.loads(cellules[2])))
    assert lues.pop("isotrope") == BORNE_UN_JEU_DE_1000 == au.bornes_calibration([1000])
    assert lues == BORNES_JEUX_DE_200


def test_bornes_recalculees_par_le_programme_de_l_addendum(tmp_path):
    """EC-3 : le programme de l'addendum (`loi_du_compte`, `bornes`), rejoué ici : ses 41 bornes égalent celles du code.
    Il est joué sur une copie, hors du dépôt : rien n'est écrit à côté de la pièce scellée."""
    programme = PIECES / PROGRAMME_BORNES[0]
    if not programme.is_file():
        pytest.skip("programme des bornes de l'addendum absent de cette branche")
    assert hashlib.sha256(programme.read_bytes()).hexdigest() == PROGRAMME_BORNES[1]
    copie = tmp_path / "bornes_de_l_addendum.py"
    copie.write_bytes(programme.read_bytes())
    spec = importlib.util.spec_from_file_location("bornes_de_l_addendum", copie)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    assert tuple(module.bornes(module.loi_du_compte([1000]))) == au.bornes_calibration([1000]) == BORNE_UN_JEU_DE_1000
    for k in range(1, 41):
        assert tuple(module.bornes(module.loi_du_compte([200] * k))) == au.bornes_calibration([200] * k) == BORNES_JEUX_DE_200[k], k


def test_les_tables_disent_la_loi_de_reference_approchee():
    """EC-3 : la loi des bornes est « de référence », « approchée, non exacte » ; le mot « exacte » de la docstring de
    `audits_v1` (module inchangé : l'addendum ne demande aucun `audits_v2`) n'est pas repris dans ce que le code écrit."""
    assert "de référence" in la.LOI_CALIBRATION and "approchée, non exacte" in la.LOI_CALIBRATION
    assert "exacte" in (au.__doc__ or "")                   # la docstring d'origine, non réécrite (R12), est celle que la note déclare


# --- EC-1, couple C5 : précision de la comparaison C(u_j) ≥ C(v) ----------------------------------------------------------------------
def test_concentrations_nulles_rendues_en_simple_precision():
    resume = st.resumer_nul(_scores("precision-de-la-comparaison", 40, 30), {})
    assert resume.concentration.dtype == torch.float32


def test_comparaison_des_concentrations_en_simple_precision_une_egalite_compte_contre_v():
    """C(u_j), calculé en double précision, puis rendu en simple précision : une direction nulle dont la concentration ne
    diffère de C(v) qu'au-delà de la simple précision est à égalité avec v, et l'égalité compte contre v."""
    c_v = np.float32(4.25)
    juste_dessous = np.float64(c_v) - 1e-12                 # strictement plus petit en double précision, égal en simple précision
    assert juste_dessous < np.float64(c_v) and np.float32(juste_dessous) == c_v
    nulles = torch.tensor([3.0, float(np.float32(juste_dessous)), 5.0], dtype=torch.float32)
    assert st.p_concentration(nulles, torch.tensor(c_v)) == (1 + 2) / 4                  # 5,0 et l'égalité
    assert st.p_concentration(nulles, float(c_v)) == (1 + 2) / 4
    # artefact : la même comparaison faite en double précision ne compterait pas l'égalité
    assert (1 + int((np.array([3.0, juste_dessous, 5.0]) >= np.float64(c_v)).sum())) / 4 == (1 + 1) / 4
    # un C(v) passé en double précision est ramené en simple précision avant la comparaison
    assert st.p_concentration(nulles, float(np.float64(c_v) + 1e-12)) == (1 + 2) / 4
    with pytest.raises(Arret, match="simple précision"):
        st.p_concentration(nulles.double(), float(c_v))


def test_p_de_concentration_de_la_direction_lue_et_des_temoins_selon_la_meme_regle():
    """La direction lue et les témoins sont jugés avec m_t et s_t des M directions ; p = (1 + #{C(u_j) ≥ C}) / (M + 1)."""
    a_nul = _scores("p-de-concentration-nul", 200, 60)
    t = _scores("p-de-concentration-temoins", 200, 9)
    resume = st.resumer_nul(a_nul, {})
    z = (t - resume.moyenne[:, None]) / resume.ecart_type[:, None]
    attendu = [(1 + int((resume.concentration >= z[:, i].max()).sum())) / 61 for i in range(9)]
    assert np.allclose(st.p_temoins(t, resume), attendu)
    ids = np.arange(200)
    lecture = st.lecture_signe(t[:, 0], {K.NUL_ISOTROPE: (a_nul, resume)}, {}, ids)
    assert lecture["nuls"][K.NUL_ISOTROPE]["p_concentration"] == pytest.approx(attendu[0])
    assert lecture["nuls"][K.NUL_ISOTROPE]["concentration"] == pytest.approx(float(z[:, 0].max()))
