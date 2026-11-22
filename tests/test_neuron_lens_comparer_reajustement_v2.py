"""Essais du programme de comparaison du réajustement v2 (critère d'identité v3, § 6) : cas sains et artefacts (R5), y compris une
garde par altération survivante relevée par la vérification du critère v2 (D1 à D4)."""
import copy
import hashlib
import json
from pathlib import Path

import pytest

from controle_ia.neuron_lens import comparer_reajustement_v2 as c

RACINE = Path(__file__).resolve().parents[1]
DIAG = RACINE / "diag/20261118-164930-neuron-lens-b-beta"
MANIF = RACINE / "runs/20261118-164930-neuron-lens-b-beta/manifeste.json"
LANCEUR = RACINE / "src/controle_ia/neuron_lens/b_beta_lancer_v3.py"

pytestmark = pytest.mark.skipif(not (DIAG / "b-beta-ajustement-R.json").exists(), reason="pièces du 18 absentes")


def _sha(obj) -> str:
    return hashlib.sha256(json.dumps(obj, sort_keys=True).encode()).hexdigest()


def _base(L):
    """Référence lue depuis les fichiers du 18 (empreintes vraies) ; côté neuf = copie d'une course distincte, octets égaux."""
    cc = c.charger(DIAG / f"b-beta-ajustement-{L}.json", DIAG / f"b-beta-ajustement-{L}.json", MANIF, MANIF, LANCEUR, LANCEUR,
                   DIAG / "b-beta-export.json" if L == "R" else None, DIAG / "b-beta-export.json" if L == "R" else None)
    cc["env_neuf"] = copy.deepcopy(cc["env_ref"])
    cc["neuf"] = cc["env_neuf"]["resultat"]
    cc["env_neuf"]["run_id"] = "20261120-120000-neuron-lens-reajustement"
    cc["neuf"]["debut_utc"] = "2026-11-20T13:00:00Z"
    cc["mneuf"] = copy.deepcopy(cc["mref"])
    cc["mneuf"]["commit"] = "f" * 40
    cc["mneuf"]["run_id"] = cc["env_neuf"]["run_id"]
    sha_m = _sha(cc["mneuf"])
    cc["sha_pieces"]["manifeste_neuf"] = sha_m
    cc["env_neuf"]["manifeste_sha256"] = sha_m
    if L == "R":
        cc["eneuf"] = copy.deepcopy(cc["eref"])
    return cc


def _octets_differents(cc):
    cc["neuf"]["sha256"] = "0" * 64
    return cc


def _pre_manque(r, morceau):
    return any(morceau in p["nom"] for p in r["preconditions"] if not p["tenu"])


# --- cas sains -------------------------------------------------------------------------------------------------------------
@pytest.mark.parametrize("L", ["R", "S"])
def test_sain_palier_1(L):
    r = c.comparer(_base(L))
    assert r["preconditions_toutes_tenues"], [p for p in r["preconditions"] if not p["tenu"]]
    assert r["mention"] == c.PALIER_1 and r["declencheurs"] == ["(i) palier 1 obtenu"]


@pytest.mark.parametrize("L,n", [("R", 63), ("S", 64)])
def test_sain_palier_2_ecart_nul(L, n):
    r = c.comparer(_octets_differents(_base(L)))
    assert r["mention"] == c.PALIER_2
    assert "(ii) écart maximal exactement nul avec des octets différents" in r["declencheurs"]
    assert len(r["table_ecarts_diffs_float64"]) == n


def test_constantes():
    assert c.TOLERANCE == 1e-3
    assert "10⁻³" in c.PALIER_2
    assert c.REFERENCES["manifeste"].startswith("b90c1514")


# --- bords de la tolérance, signe (D4) -------------------------------------------------------------------------------------
@pytest.mark.parametrize("delta,mention", [(0.999e-3, c.PALIER_2), (-0.999e-3, c.PALIER_2), (1.001e-3, c.DIFFERENTE),
                                           (-1.001e-3, c.DIFFERENTE), (-2e-3, c.DIFFERENTE), (2e-3, c.DIFFERENTE), (-0.05, c.DIFFERENTE)])
def test_bords_et_signe(delta, mention):
    cc = _octets_differents(_base("S"))
    cc["neuf"]["diffs_float64"]["out"][4] += delta
    r = c.comparer(cc)
    assert r["mention"] == mention
    assert abs(r["ecart_max_abs_diffs_float64"] - abs(delta)) < 1e-12
    ligne = next(x for x in r["table_ecarts_diffs_float64"] if x["cible"] == "out" and x["rang"] == 4)
    assert abs(ligne["ecart"] - delta) < 1e-12           # signe gardé


def test_egalite_exacte_a_la_tolerance_est_palier_2():
    # 0.004 et 0.005 diffèrent d'exactement 1e-3 en double précision : « au plus » veut dire « ≤ »
    cc = _octets_differents(_base("S"))
    cc["ref"]["diffs_float64"]["mid"][0] = 0.004
    cc["neuf"]["diffs_float64"]["mid"][0] = 0.005
    assert 0.005 - 0.004 == c.TOLERANCE
    assert c.comparer(cc)["mention"] == c.PALIER_2


def test_ecart_relatif_et_diffs_rapportes():
    cc = _octets_differents(_base("S"))
    a = cc["ref"]["diffs_float64"]["mid"][1]
    cc["neuf"]["diffs_float64"]["mid"][1] = a * 1.005
    cc["neuf"]["diffs"]["mid"][1] = cc["ref"]["diffs"]["mid"][1] + 3e-4
    r = c.comparer(cc)
    assert abs(r["ecart_max_rel_diffs_float64"] - 0.005) < 1e-9
    assert abs(r["ecart_max_abs_diffs"] - 3e-4) < 1e-12


# --- premier palier : cohérence (D1) ---------------------------------------------------------------------------------------
def test_s1_palier_1_valeur_deplacee_suspendu():
    cc = _base("R")
    cc["neuf"]["diffs_float64"]["mid"][3] += 0.05
    r = c.comparer(cc)
    assert r["mention"] == c.SUSPENDU and any(d.startswith("(v)") for d in r["declencheurs"])


@pytest.mark.parametrize("champ,val", [("n_docs", [466, 465]), ("meta", None)])
def test_s2_palier_1_prealable_manque_suspendu(champ, val):
    cc = _base("S")
    cc["neuf"][champ] = val
    assert c.comparer(cc)["mention"] == c.SUSPENDU


def test_s2_palier_1_nan_suspendu_sans_maximum():
    cc = _base("S")
    cc["neuf"]["diffs_float64"]["out"][2] = float("nan")
    r = c.comparer(cc)
    assert r["mention"] == c.SUSPENDU and "ecart_max_abs_diffs_float64" not in r


def test_s3_palier_1_taille_differente_suspendu():
    cc = _base("R")
    cc["neuf"]["taille"] += 1
    assert c.comparer(cc)["mention"] == c.SUSPENDU


def test_s9_palier_1_export_sans_matrices_suspendu():
    cc = _base("R")
    cc["eref"] = copy.deepcopy(cc["eref"])
    cc["eref"]["matrices_moities"] = {}
    assert c.comparer(cc)["mention"] == c.SUSPENDU


def test_palier_1_matrice_differente_suspendu_et_compte():
    cc = _base("R")
    cc["eneuf"]["matrices_moities"]["7"] = ["0" * 64, "0" * 64]
    r = c.comparer(cc)
    assert r["mention"] == c.SUSPENDU
    assert r["matrices_moities_egales"] == {"couches_egales": 30, "couches_ref": 31}


def test_reprise_palier_1_notee():
    r = c.comparer(_base("S"), reprise=True)
    assert r["mention"].startswith(c.PALIER_1) and "reprise" in r["mention"]


# --- provenance (D2) -------------------------------------------------------------------------------------------------------
@pytest.mark.parametrize("val", [None, "", "abc", "G" * 64])
def test_s4_s5_empreinte_neuve_absente_ou_mal_formee(val):
    cc = _base("S")
    cc["neuf"]["sha256"] = val
    r = c.comparer(cc)
    assert r["mention"] == c.NON_COMPARABLE and _pre_manque(r, "empreinte du fichier")


def test_empreintes_absentes_des_deux_cotes_pas_de_palier_1():
    cc = _base("S")
    cc["neuf"]["sha256"] = None
    cc["ref"]["sha256"] = None
    assert c.comparer(cc)["mention"] == c.NON_COMPARABLE


def test_s8_reference_contre_elle_meme_refusee():
    cc = c.charger(DIAG / "b-beta-ajustement-S.json", DIAG / "b-beta-ajustement-S.json", MANIF, MANIF, LANCEUR, LANCEUR)
    r = c.comparer(cc)
    assert r["mention"] == c.SUSPENDU and _pre_manque(r, "course neuve distincte")


def test_s19_finies_faux():
    cc = _octets_differents(_base("S"))
    cc["neuf"]["finies"] = False
    r = c.comparer(cc)
    assert r["mention"] == c.NON_COMPARABLE and _pre_manque(r, "`finies`")


def test_s20_reference_et_neuf_echangees():
    cc = _octets_differents(_base("S"))
    cc["sha_pieces"]["ajustement_ref"] = "1" * 64          # la référence n'est plus la pièce du 18
    r = c.comparer(cc)
    assert r["mention"] == c.NON_COMPARABLE and _pre_manque(r, "pièce d'ajustement de référence")


def test_manifeste_de_reference_faux():
    cc = _octets_differents(_base("S"))
    cc["sha_pieces"]["manifeste_ref"] = "2" * 64
    assert c.comparer(cc)["mention"] == c.NON_COMPARABLE


def test_manifeste_neuf_non_porte_par_le_resultat():
    cc = _octets_differents(_base("S"))
    cc["env_neuf"]["manifeste_sha256"] = "3" * 64
    r = c.comparer(cc)
    assert r["mention"] == c.NON_COMPARABLE and _pre_manque(r, "manifeste neuf")


@pytest.mark.parametrize("champ", list(c.CHAMPS_CONFIG))
def test_champ_de_configuration_change(champ):
    cc = _octets_differents(_base("S"))
    cc["mneuf"]["config"][champ] = "autre"
    r = c.comparer(cc)
    assert r["mention"] == c.NON_COMPARABLE and _pre_manque(r, f"`{champ}`")


# --- forme et préalables du deuxième palier (D4) ---------------------------------------------------------------------------
@pytest.mark.parametrize("val", [float("nan"), float("inf"), None, "0.1", True])
@pytest.mark.parametrize("cote", ["neuf", "ref"])
@pytest.mark.parametrize("champ", ["diffs_float64", "diffs"])
def test_valeur_non_finie_ou_non_numerique(val, cote, champ):
    cc = _octets_differents(_base("S"))
    cc[cote][champ]["out"][3] = val
    r = c.comparer(cc)
    assert r["mention"] == c.NON_COMPARABLE and "ecart_max_abs_diffs_float64" not in r


@pytest.mark.parametrize("cas", ["62", "cible_en_plus", "series_vides", "pas_une_liste"])
def test_formes(cas):
    cc = _octets_differents(_base("R"))
    if cas == "62":
        cc["neuf"]["diffs_float64"]["mid"] = cc["neuf"]["diffs_float64"]["mid"][:-1]
    elif cas == "cible_en_plus":
        cc["neuf"]["diffs_float64"]["autre"] = [0.01]
    elif cas == "series_vides":
        cc["neuf"]["diffs_float64"] = {}
        cc["ref"]["diffs_float64"] = {}
    else:
        cc["neuf"]["diffs_float64"]["mid"] = 0.1
    assert c.comparer(cc)["mention"] == c.NON_COMPARABLE


def test_meta_absent_des_deux_cotes():
    cc = _octets_differents(_base("S"))
    cc["neuf"]["meta"] = None
    cc["ref"]["meta"] = None
    assert c.comparer(cc)["mention"] == c.NON_COMPARABLE


def test_meta_change():
    cc = _octets_differents(_base("S"))
    cc["neuf"]["meta"] = dict(cc["neuf"]["meta"], dim_batch=128)
    assert c.comparer(cc)["mention"] == c.NON_COMPARABLE


@pytest.mark.parametrize("champ,val", [("n_docs", [466, 465]), ("next_doc", 931), ("fichier", "autre.pt")])
@pytest.mark.parametrize("cote", ["neuf", "ref"])
def test_comptes_et_nom(champ, val, cote):
    cc = _octets_differents(_base("S"))
    cc[cote][champ] = val
    assert c.comparer(cc)["mention"] == c.NON_COMPARABLE


def test_nom_commit_fonction_absents_des_deux_cotes():
    for modif in ("fichier", "commit", "fonction"):
        cc = _octets_differents(_base("S"))
        if modif == "fichier":
            cc["ref"]["fichier"] = cc["neuf"]["fichier"] = None
        elif modif == "commit":
            cc["mref"]["config"]["commit_voisin"] = None
            cc["mneuf"]["config"]["commit_voisin"] = None
        else:
            cc["fref"] = cc["fneuf"] = None
        assert c.comparer(cc)["mention"] == c.NON_COMPARABLE, modif


def test_fonction_differente():
    cc = _octets_differents(_base("S"))
    cc["fneuf"] = "f" * 64
    assert c.comparer(cc)["mention"] == c.NON_COMPARABLE


# --- pièces d'export de R (D3) ---------------------------------------------------------------------------------------------
@pytest.mark.parametrize("cas", ["s6_sans_export_neuf", "s7_sans_export_ref", "s10_sans_series", "27_couches", "serie_nan",
                                 "export_ref_faux"])
def test_exports_r(cas):
    cc = _octets_differents(_base("R"))
    if cas == "s6_sans_export_neuf":
        cc["eneuf"] = None
    elif cas == "s7_sans_export_ref":
        cc["eref"] = None
    elif cas == "s10_sans_series":
        del cc["eneuf"]["valeurs"]["npR_notre_R"]
    elif cas == "27_couches":
        cc["eneuf"]["valeurs"]["identite_notre_R"].pop("0")
    elif cas == "serie_nan":
        cc["eneuf"]["valeurs"]["npR_notre_R"]["5"] = float("nan")
    else:
        cc["sha_pieces"]["export_ref"] = "4" * 64
    assert c.comparer(cc)["mention"] == c.NON_COMPARABLE


def test_series_r_rapportees_et_deplacement_retrouve():
    cc = _octets_differents(_base("R"))
    cc["eneuf"]["valeurs"]["npR_notre_R"]["11"] += 0.0123
    r = c.comparer(cc)
    s = r["series_export_R_sans_critere"]
    assert s["npR_notre_R"]["couches"] == 28 and s["identite_notre_R"]["couches"] == 28
    assert abs(s["npR_notre_R"]["ecarts"]["11"] - 0.0123) < 1e-12
    assert abs(s["npR_notre_R"]["ecart_max_abs"] - 0.0123) < 1e-12
    assert s["identite_notre_R"]["ecart_max_abs"] == 0.0
    assert s["npR_notre_R"]["ref_min"] < s["npR_notre_R"]["ref_max"]
    assert r["mention"] == c.PALIER_2          # les séries ne décident pas


def test_s_sans_objet():
    r = c.comparer(_octets_differents(_base("S")))
    assert r["series_export_R_sans_critere"].startswith("sans objet")


def test_changement_de_cote_du_seuil_rapporte():
    cc = _octets_differents(_base("R"))
    i = next(i for i, x in enumerate(cc["neuf"]["diffs"]["mid"]) if x > 0.10)
    cc["neuf"]["diffs"]["mid"][i] = 0.0999
    r = c.comparer(cc)
    assert r["mention"] == c.PALIER_2 and any(x["rang"] == i for x in r["changements_de_cote_du_seuil_0_10_sur_diffs"])


# --- ligne de commande -----------------------------------------------------------------------------------------------------
def test_cli_refuse_de_comparer_la_reference_a_elle_meme_et_n_ecrase_pas(tmp_path):
    s = tmp_path / "s.json"
    args = ["--ref-ajustement", str(DIAG / "b-beta-ajustement-S.json"), "--neuf-ajustement", str(DIAG / "b-beta-ajustement-S.json"),
            "--ref-manifeste", str(MANIF), "--neuf-manifeste", str(MANIF), "--lanceur-ref", str(LANCEUR),
            "--lanceur-neuf", str(LANCEUR), "--sortie", str(s)]
    c.main(args)
    sortie = json.loads(s.read_text())
    assert sortie["mention"] == c.SUSPENDU and sortie["ligne_de_commande"][0] == "comparer_reajustement_v2"
    with pytest.raises(SystemExit):
        c.main(args)
