"""Essais du programme de comparaison du réajustement v3 : ceux de la v2 (D1 à D4), adaptés, plus un essai par contrôle porté du
critère v4 (H1 à H7) et par sonde du rédacteur Fable (T1 à T4)."""
import copy
import hashlib
import json
from pathlib import Path

import pytest

from controle_ia.neuron_lens import comparer_reajustement_v3 as c

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
                   DIAG / "b-beta-export.json" if L == "R" else None, DIAG / "b-beta-export.json" if L == "R" else None,
                   depot=RACINE, commit_resultats="c" * 40)
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
        cc["env_eneuf"] = copy.deepcopy(cc["env_eneuf"])
        cc["env_eneuf"]["run_id"] = cc["env_neuf"]["run_id"]
        cc["env_eneuf"]["manifeste_sha256"] = sha_m
        cc["eneuf"] = cc["env_eneuf"]["resultat"]
        cc["sha_pieces"]["export_neuf"] = "e" * 64
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
    # H6 : pour R, 31 matrices égales et séries inchangées avec des octets différents : trop propre, audit requis
    assert (any(d.startswith("(vi)") for d in r["declencheurs"]) and r.get("audit_requis")) == (L == "R")


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
    cc = c.charger(DIAG / "b-beta-ajustement-S.json", DIAG / "b-beta-ajustement-S.json", MANIF, MANIF, LANCEUR, LANCEUR, depot=RACINE)
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
    # la valeur au-dessus de 0,10 la plus proche du seuil, déplacée de moins de 10⁻³ (H7 tenu)
    i = min((i for i, x in enumerate(cc["neuf"]["diffs"]["mid"]) if x > 0.10), key=lambda i: cc["neuf"]["diffs"]["mid"][i])
    assert cc["neuf"]["diffs"]["mid"][i] - 0.0999 < 1e-3
    cc["neuf"]["diffs"]["mid"][i] = 0.0999
    r = c.comparer(cc)
    assert r["mention"] == c.PALIER_2 and any(x["rang"] == i for x in r["changements_de_cote_du_seuil_0_10_sur_diffs"])


# --- ligne de commande -----------------------------------------------------------------------------------------------------
def test_cli_refuse_de_comparer_la_reference_a_elle_meme_et_n_ecrase_pas(tmp_path):
    s = tmp_path / "s.json"
    args = ["--ref-ajustement", str(DIAG / "b-beta-ajustement-S.json"), "--neuf-ajustement", str(DIAG / "b-beta-ajustement-S.json"),
            "--ref-manifeste", str(MANIF), "--neuf-manifeste", str(MANIF), "--lanceur-ref", str(LANCEUR),
            "--lanceur-neuf", str(LANCEUR), "--sortie", str(s), "--depot", str(RACINE), "--commit-resultats", "c" * 40]
    c.main(args)
    sortie = json.loads(s.read_text())
    assert sortie["mention"] == c.SUSPENDU
    with pytest.raises(SystemExit):
        c.main(args)
    assert sortie["ligne_de_commande"][0] == "comparer_reajustement_v3"


# --- contrôles portés du critère v4 (H1 à H7) et sondes du rédacteur Fable (T1 à T4) ---------------------------------------
def test_h1_pieces_lues_et_commit_en_sortie():
    r = c.comparer(_base("R"))
    for k in ("ajustement_ref", "ajustement_neuf", "manifeste_ref", "manifeste_neuf", "export_ref", "export_neuf", "lanceur_neuf"):
        assert k in r["pieces_lues"], k
    assert r["commit_resultats"] == "c" * 40


def test_t1_h2_export_du_18_passe_comme_export_neuf():
    cc = _octets_differents(_base("R"))
    # l'enveloppe d'export du 18, telle quelle (identifiant de course et manifeste du 18)
    cc["env_eneuf"] = json.loads((DIAG / "b-beta-export.json").read_text(encoding="utf-8"))
    cc["eneuf"] = cc["env_eneuf"]["resultat"]
    cc["sha_pieces"]["export_neuf"] = c.REFERENCES["export-R"]
    r = c.comparer(cc)
    assert r["mention"] == c.NON_COMPARABLE and _pre_manque(r, "H2")


def test_t1bis_h2_export_neuf_au_premier_palier_suspendu():
    cc = _base("R")
    cc["env_eneuf"]["run_id"] = "autre"
    r = c.comparer(cc)
    assert r["mention"] == c.SUSPENDU and _pre_manque(r, "H2")


def test_h2_manifeste_de_l_export_neuf():
    cc = _octets_differents(_base("R"))
    cc["env_eneuf"]["manifeste_sha256"] = "5" * 64
    assert c.comparer(cc)["mention"] == c.NON_COMPARABLE


def test_t2_h3_cle_de_serie_differente():
    cc = _octets_differents(_base("R"))
    s = cc["eneuf"]["valeurs"]["npR_notre_R"]
    s["99"] = s.pop("0")
    r = c.comparer(cc)
    assert r["mention"] == c.NON_COMPARABLE and _pre_manque(r, "H3")


def test_h4_serie_qui_change_au_premier_palier():
    cc = _base("R")
    cc["eneuf"]["valeurs"]["identite_notre_R"]["3"] += 1e-12
    r = c.comparer(cc)
    assert r["mention"] == c.SUSPENDU and any("H4" in d for d in r["declencheurs"])


@pytest.mark.parametrize("champ,val", [("drowse", {"version": "6.1.5"}), ("precision", "fp32")])
def test_t3_h5_drowse_et_precision(champ, val):
    cc = _octets_differents(_base("S"))
    cc["mneuf"]["config"][champ] = val
    r = c.comparer(cc)
    assert r["mention"] == c.NON_COMPARABLE and _pre_manque(r, "H5")


def test_t3_h5_versions_hors_plateforme():
    cc = _octets_differents(_base("S"))
    cc["mneuf"]["versions"] = dict(cc["mneuf"]["versions"], plateforme="autre noyau")
    assert c.comparer(cc)["mention"] == c.PALIER_2            # la plateforme seule ne compte pas
    cc["mneuf"]["versions"] = dict(cc["mneuf"]["versions"], torch="2.15.0")
    r = c.comparer(cc)
    assert r["mention"] == c.NON_COMPARABLE and _pre_manque(r, "versions")


def test_t3_h5_contenu_des_correctifs():
    cc = _octets_differents(_base("S"))
    k = next(iter(cc["correctifs_neuf"]))
    cc["correctifs_neuf"] = dict(cc["correctifs_neuf"], **{k: "6" * 64})
    r = c.comparer(cc)
    assert r["mention"] == c.NON_COMPARABLE and _pre_manque(r, "correctifs")


def test_h5_correctifs_lus_au_commit_du_18():
    cc = _base("S")
    assert cc["correctifs_ref"] is not None and len(cc["correctifs_ref"]) == 5
    assert all(len(v) == 64 for v in cc["correctifs_ref"].values())


def test_h5_correctifs_non_lus():
    cc = _octets_differents(_base("S"))
    cc["correctifs_ref"] = cc["correctifs_neuf"] = None
    assert c.comparer(cc)["mention"] == c.NON_COMPARABLE


def test_t4_h7_diffs_deplace_au_deuxieme_palier():
    cc = _octets_differents(_base("S"))
    cc["neuf"]["diffs"]["out"][2] += 0.05
    r = c.comparer(cc)
    assert r["mention"] == c.SUSPENDU and any(d.startswith("(vii)") for d in r["declencheurs"])


def test_h7_bord_au_deuxieme_palier():
    cc = _octets_differents(_base("S"))
    cc["neuf"]["diffs"]["out"][2] += 0.9e-3
    assert c.comparer(cc)["mention"] == c.PALIER_2


def test_h7_diffs_au_premier_palier():
    cc = _base("S")
    cc["neuf"]["diffs"]["mid"][1] += 2e-6
    r = c.comparer(cc)
    assert r["mention"] == c.SUSPENDU and any(d.startswith("(vii)") for d in r["declencheurs"])


def test_h6_pas_trop_propre_si_une_matrice_et_les_series_bougent():
    cc = _octets_differents(_base("R"))
    cc["eneuf"]["matrices_moities"]["4"] = ["7" * 64, "7" * 64]
    for s in ("npR_notre_R", "identite_notre_R"):
        cc["eneuf"]["valeurs"][s]["2"] += 1e-4
    r = c.comparer(cc)
    assert r["mention"] == c.PALIER_2 and not any(d.startswith("(vi)") for d in r["declencheurs"])


def test_ecart_relatif_sans_reference_non_nulle():
    cc = _octets_differents(_base("S"))
    for t_ in cc["ref"]["diffs_float64"]:
        cc["ref"]["diffs_float64"][t_] = [0.0] * len(cc["ref"]["diffs_float64"][t_])
        cc["neuf"]["diffs_float64"][t_] = [0.0] * len(cc["neuf"]["diffs_float64"][t_])
    assert c.comparer(cc)["ecart_max_rel_diffs_float64"] is None


# --- vérification du programme v2 (F1 à F6) -------------------------------------------------------------------------------
def test_f1_export_neuf_rattache_mais_fichier_du_18():
    cc = _octets_differents(_base("R"))
    cc["sha_pieces"]["export_neuf"] = c.REFERENCES["export-R"]     # identifiant et manifeste neufs, mais le fichier du 18
    r = c.comparer(cc)
    assert r["mention"] == c.NON_COMPARABLE and _pre_manque(r, "export neuf différent")


def test_f1_export_neuf_d_une_autre_course_t2b():
    cc = _octets_differents(_base("R"))
    cc["env_eneuf"]["run_id"] = "20261121-000000-autre"
    r = c.comparer(cc)
    assert r["mention"] == c.NON_COMPARABLE and _pre_manque(r, "H2")


def test_f2_fonction_modifiee_des_deux_cotes_t1():
    cc = _octets_differents(_base("S"))
    cc["fref"] = cc["fneuf"] = "9" * 64
    r = c.comparer(cc)
    assert r["mention"] == c.NON_COMPARABLE and _pre_manque(r, "F2")
    assert c.REFERENCES["fonction"] == c.empreinte_fonction(LANCEUR.read_text(encoding="utf-8"))


@pytest.mark.parametrize("cas", ["t3c_decalees", "t3b_aucune_commune", "t3_series_decalees"])
def test_f3_memes_couches(cas):
    cc = _octets_differents(_base("R"))
    if cas == "t3c_decalees":
        mm = cc["eneuf"]["matrices_moities"]
        cc["eneuf"]["matrices_moities"] = {str(int(k) + 1): v for k, v in mm.items()}
    elif cas == "t3b_aucune_commune":
        s = cc["eneuf"]["valeurs"]["npR_notre_R"]
        cc["eneuf"]["valeurs"]["npR_notre_R"] = {str(int(k) + 100): v for k, v in s.items()}
    else:
        s = cc["eneuf"]["valeurs"]["identite_notre_R"]
        cc["eneuf"]["valeurs"]["identite_notre_R"] = {str(int(k) + 1): v for k, v in s.items()}
    r = c.comparer(cc)                      # aucune erreur levée
    assert r["mention"] == c.NON_COMPARABLE


def test_f4_serie_deplacee_de_0_01_au_premier_palier_p6b():
    cc = _base("R")
    cc["eneuf"]["valeurs"]["npR_notre_R"]["9"] += 0.01
    assert c.comparer(cc)["mention"] == c.SUSPENDU


def test_f5_t8_differences_des_manifestes_rapportees():
    cc = _octets_differents(_base("S"))
    cc["mneuf"]["versions"] = dict(cc["mneuf"]["versions"], plateforme="autre noyau")
    cc["mneuf"]["config"]["tranche"] = "autre"
    r = c.comparer(cc)
    d = r["differences_des_manifestes_sans_critere"]
    assert "plateforme" in d["versions"] and "tranche" in d["config"] and d["commit"] == [cc["mref"]["commit"], "f" * 40]
    assert r["mention"] == c.PALIER_2


def test_mineure_1_etape_t11():
    cc = _octets_differents(_base("S"))
    cc["neuf"]["etape"] = "ajustement-R"
    r = c.comparer(cc)
    assert r["mention"] == c.NON_COMPARABLE and _pre_manque(r, "etape")


# F6, 1 : déclencheurs (iii) et (iv)
def test_f6_declencheurs_iii_et_iv():
    cc = _octets_differents(_base("S"))
    cc["neuf"]["diffs_float64"]["mid"][0] += 5e-3
    r = c.comparer(cc)
    assert r["mention"] == c.DIFFERENTE and "(iii) lentille différente" in r["declencheurs"]
    cc2 = _octets_differents(_base("S"))
    cc2["neuf"]["n_docs"] = [1, 1]
    r2 = c.comparer(cc2)
    assert r2["mention"] == c.NON_COMPARABLE and "(iv) non comparable" in r2["declencheurs"]


# F6, 2 : empreintes calculées sur les octets lus (vrais fichiers modifiés d'un octet)
def _copie_modifiee(src, dst):
    b = bytearray(src.read_bytes())
    i = b.rindex(b"}")
    b[i:i] = b" "                        # JSON toujours lisible, un octet de plus
    dst.write_bytes(bytes(b))
    return dst


@pytest.mark.parametrize("piece", ["ajustement_ref", "manifeste_ref", "export_ref"])
def test_f6_piece_de_reference_modifiee_d_un_octet(tmp_path, piece):
    aj = DIAG / "b-beta-ajustement-R.json"
    ex = DIAG / "b-beta-export.json"
    args = dict(ref_ajustement=aj, neuf_ajustement=aj, ref_manifeste=MANIF, neuf_manifeste=MANIF, lanceur_ref=LANCEUR,
                lanceur_neuf=LANCEUR, ref_export=ex, neuf_export=ex, depot=RACINE)
    cle = {"ajustement_ref": "ref_ajustement", "manifeste_ref": "ref_manifeste", "export_ref": "ref_export"}[piece]
    args[cle] = _copie_modifiee(args[cle], tmp_path / "m.json")
    cc = c.charger(**args)
    assert cc["sha_pieces"][piece] != c.REFERENCES[{"ajustement_ref": "ajustement-R", "manifeste_ref": "manifeste",
                                                    "export_ref": "export-R"}[piece]]
    r = c.comparer(cc)
    assert not r["preconditions_toutes_tenues"]


def test_f6_manifeste_neuf_modifie_apres_coup(tmp_path):
    # le résultat neuf porte l'empreinte du manifeste du 18 ; le manifeste neuf donné est modifié d'un octet
    aj = DIAG / "b-beta-ajustement-S.json"
    m2 = _copie_modifiee(MANIF, tmp_path / "manifeste.json")
    cc = c.charger(aj, aj, MANIF, m2, LANCEUR, LANCEUR, depot=RACINE)
    assert cc["sha_pieces"]["manifeste_neuf"] != cc["env_neuf"]["manifeste_sha256"]
    r = c.comparer(cc)
    assert _pre_manque(r, "manifeste neuf")


# F6, 3 : borne de cohérence du premier palier
@pytest.mark.parametrize("delta,suspendu", [(2e-9, True), (5e-10, False)])
def test_f6_coherence_premier_palier(delta, suspendu):
    cc = _base("S")
    cc["neuf"]["diffs_float64"]["out"][7] += delta
    assert (c.comparer(cc)["mention"] == c.SUSPENDU) is suspendu
    assert c.COHERENCE_PALIER_1 == 1e-9


# F6, 4 : course distincte jugée sur l'identifiant et l'heure
@pytest.mark.parametrize("meme", ["identifiant", "heure"])
def test_f6_course_distincte(meme):
    cc = _octets_differents(_base("S"))
    if meme == "identifiant":
        cc["env_neuf"]["run_id"] = cc["env_ref"]["run_id"]
    else:
        cc["neuf"]["debut_utc"] = cc["ref"]["debut_utc"]
    r = c.comparer(cc)
    assert r["mention"] == c.NON_COMPARABLE and _pre_manque(r, "course neuve distincte")


# F6, 5 : taille absente au deuxième palier
def test_f6_taille_absente():
    cc = _octets_differents(_base("S"))
    cc["neuf"]["taille"] = None
    r = c.comparer(cc)
    assert r["mention"] == c.NON_COMPARABLE and _pre_manque(r, "taille")


# F6, 6 : champ de configuration absent des deux côtés ; liste des six champs
def test_f6_champ_de_configuration_absent_des_deux_cotes():
    cc = _octets_differents(_base("S"))
    del cc["mref"]["config"]["graines"]
    del cc["mneuf"]["config"]["graines"]
    assert c.comparer(cc)["mention"] == c.NON_COMPARABLE
    assert c.CHAMPS_CONFIG == ("ajustement", "correctifs", "graines", "modele", "revision", "corpus")


# F6, 7 : empreinte de matrice mal formée ; cible à liste vide des deux côtés
def test_f6_empreinte_de_matrice_mal_formee():
    cc = _octets_differents(_base("R"))
    cc["eneuf"]["matrices_moities"]["3"] = ["xyz", cc["eneuf"]["matrices_moities"]["3"][1]]
    assert c.comparer(cc)["mention"] == c.NON_COMPARABLE


def test_f6_cible_a_liste_vide_des_deux_cotes():
    cc = _octets_differents(_base("S"))
    cc["ref"]["diffs_float64"]["out"] = []
    cc["neuf"]["diffs_float64"]["out"] = []
    assert c.comparer(cc)["mention"] == c.NON_COMPARABLE


# F6, 8 : plage des séries du 18 lue du côté de la référence
def test_f6_plage_des_series_du_18():
    cc = _octets_differents(_base("R"))
    s18 = cc["eref"]["valeurs"]["npR_notre_R"]
    for k in cc["eneuf"]["valeurs"]["npR_notre_R"]:
        cc["eneuf"]["valeurs"]["npR_notre_R"][k] += 0.5
    r = c.comparer(cc)
    s = r["series_export_R_sans_critere"]["npR_notre_R"]
    assert s["ref_min"] == min(s18.values()) and s["ref_max"] == max(s18.values())


# F6, 9 : garde de finitude du maximum, appel direct
def test_f6_garde_de_finitude_du_maximum():
    with pytest.raises(ValueError):
        c._max_abs([{"ecart": 0.1}, {"ecart": float("nan")}])
    assert c._max_abs([{"ecart": -0.2}, {"ecart": 0.1}]) == 0.2
