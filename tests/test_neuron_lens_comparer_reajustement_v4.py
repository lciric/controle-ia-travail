"""Essais du programme de comparaison du réajustement v4 : les 123 essais de la v3, adaptés (commit des résultats vrai, chemin du
lanceur neuf, nom du programme), plus, pour chaque garde neuve portée du critère d'identité v5 (§ 7, K1, K2, K5, arrêt sur une
erreur, `audit_requis`, mineures), un cas sain et au moins un artefact. Les gardes qui lisent le dépôt (K1, K2) sont essayées sur
de vrais dépôts git temporaires : un petit dépôt à un commit pour les fonctions de lecture, et un dépôt neuf, adossé au magasin
d'objets du dépôt de travail (pour que le commit du 18 y soit lisible), pour la comparaison de bout en bout."""
import copy
import hashlib
import json
import os
import subprocess
from pathlib import Path

import pytest

from controle_ia.neuron_lens import comparer_reajustement_v4 as c

RACINE = Path(__file__).resolve().parents[1]
DIAG = RACINE / "diag/20261118-164930-neuron-lens-b-beta"
MANIF = RACINE / "runs/20261118-164930-neuron-lens-b-beta/manifeste.json"
CHEMIN_LANCEUR = "src/controle_ia/neuron_lens/b_beta_lancer_v3.py"
LANCEUR = RACINE / CHEMIN_LANCEUR
COMMIT_18 = "5e5cb65b4daf8726ebe1c4032a836b850de7ea2f"          # commit du dépôt réduit que porte le manifeste du 18
COMMIT_PIECES = "467e85ce07674c650010121510a93b42d29419ee"      # commit du dépôt de travail qui a versé les pièces du 18

pytestmark = pytest.mark.skipif(not (DIAG / "b-beta-ajustement-R.json").exists(), reason="pièces du 18 absentes")


def _sha(obj) -> str:
    return hashlib.sha256(json.dumps(obj, sort_keys=True).encode()).hexdigest()


_CHARGE = {}


def _base(L):
    """Référence lue depuis les fichiers du 18 (empreintes vraies) ; côté neuf = copie d'une course distincte, octets égaux.
    Les relevés de rattachement (K1, K2) sont ceux que `charger` a vraiment lus dans le dépôt de travail : les pièces du 18 au
    commit qui les a versées, le lanceur du 18 au commit du manifeste du 18. La lecture est faite une fois par lentille."""
    if L not in _CHARGE:
        _CHARGE[L] = c.charger(DIAG / f"b-beta-ajustement-{L}.json", DIAG / f"b-beta-ajustement-{L}.json", MANIF, MANIF, LANCEUR,
                               LANCEUR, DIAG / "b-beta-export.json" if L == "R" else None,
                               DIAG / "b-beta-export.json" if L == "R" else None, depot=RACINE, commit_resultats=COMMIT_PIECES,
                               chemin_lanceur_neuf=CHEMIN_LANCEUR)
    cc = copy.deepcopy(_CHARGE[L])
    cc["env_neuf"] = copy.deepcopy(cc["env_ref"])
    cc["neuf"] = cc["env_neuf"]["resultat"]
    cc["env_neuf"]["run_id"] = "20261120-120000-neuron-lens-reajustement"
    cc["neuf"]["debut_utc"] = "2026-11-20T13:00:00Z"
    cc["mneuf"] = copy.deepcopy(cc["mref"])
    cc["mneuf"]["commit"] = "f" * 40
    cc["mneuf"]["run_id"] = cc["env_neuf"]["run_id"]
    sha_m = _sha(cc["mneuf"])
    cc["sha_pieces"]["manifeste_neuf"] = sha_m
    cc["rattachement"]["manifeste_neuf"]["sha256_au_commit"] = sha_m       # le manifeste neuf simulé, tenu pour versé tel quel
    cc["env_neuf"]["manifeste_sha256"] = sha_m
    if L == "R":
        cc["env_eneuf"] = copy.deepcopy(cc["env_eneuf"])
        cc["env_eneuf"]["run_id"] = cc["env_neuf"]["run_id"]
        cc["env_eneuf"]["manifeste_sha256"] = sha_m
        cc["eneuf"] = cc["env_eneuf"]["resultat"]
        cc["sha_pieces"]["export_neuf"] = "e" * 64
        cc["rattachement"]["export_neuf"]["sha256_au_commit"] = "e" * 64   # l'export neuf simulé, tenu pour versé tel quel
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
            "--lanceur-neuf", str(LANCEUR), "--sortie", str(s), "--depot", str(RACINE), "--commit-resultats", COMMIT_PIECES,
            "--chemin-lanceur-neuf", CHEMIN_LANCEUR]
    c.main(args)
    sortie = json.loads(s.read_text())
    assert sortie["mention"] == c.SUSPENDU
    with pytest.raises(SystemExit):
        c.main(args)
    assert sortie["ligne_de_commande"][0] == "comparer_reajustement_v4"


# --- contrôles portés du critère v4 (H1 à H7) et sondes du rédacteur Fable (T1 à T4) ---------------------------------------
def test_h1_pieces_lues_et_commit_en_sortie():
    r = c.comparer(_base("R"))
    for k in ("ajustement_ref", "ajustement_neuf", "manifeste_ref", "manifeste_neuf", "export_ref", "export_neuf", "lanceur_neuf",
              "lanceur_ref"):
        assert k in r["pieces_lues"], k
    assert r["commit_resultats"] == COMMIT_PIECES


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


# =============================================================================================================================
# Gardes neuves de la v4, portées du critère d'identité v5 (§ 7) : pour chacune, un cas sain et au moins un artefact (R5)
# =============================================================================================================================
RID = "20261120-120000-neuron-lens-reajustement"
CHEMIN_LANCEUR_NEUF = "src/controle_ia/neuron_lens/reajustement_lancer_essai_v1.py"


def _g(depot, *args, entree=None, env=None) -> str:
    r = subprocess.run(["git", "-C", str(depot), "-c", "user.name=essai", "-c", "user.email=essai@exemple.invalid",
                        "-c", "commit.gpgsign=false", *args], check=True, capture_output=True, input=entree, env=env)
    return r.stdout.decode("utf-8").strip()


def _ecrire(chemin: Path, obj) -> Path:
    chemin.parent.mkdir(parents=True, exist_ok=True)
    chemin.write_bytes(obj if isinstance(obj, bytes) else (json.dumps(obj, ensure_ascii=False, indent=1) + "\n").encode("utf-8"))
    return chemin


class _Course:
    """Une course neuve simulée, versée dans un vrai dépôt git temporaire : un commit du code (l'arbre du commit du 18, plus un
    lanceur neuf) et un commit des résultats (manifeste, résultat d'ajustement, export pour R)."""

    def __init__(self, dossier: Path, L: str, octets_egaux: bool):
        self.L, self.dossier = L, dossier
        d = self.depot = dossier / "depot"
        d.mkdir(parents=True)
        _g(d, "init", "-q", "-b", "main")
        commun = Path(_g(RACINE, "rev-parse", "--git-common-dir"))
        commun = commun if commun.is_absolute() else RACINE / commun
        # dépôt adossé au magasin d'objets du dépôt de travail, en lecture seule : le commit du manifeste du 18 y est lisible
        (d / ".git/objects/info/alternates").write_text(str((commun / "objects").resolve()) + "\n")
        self.texte_lanceur = LANCEUR.read_bytes() + b"\n# lanceur de la course de reajustement (essai)\n"
        blob = _g(d, "hash-object", "-w", "--stdin", entree=self.texte_lanceur)
        env = dict(os.environ, GIT_INDEX_FILE=str(dossier / "index-du-code"))
        _g(d, "read-tree", COMMIT_18, env=env)
        _g(d, "update-index", "--add", "--cacheinfo", f"100644,{blob},{CHEMIN_LANCEUR_NEUF}", env=env)
        self.commit_code = _g(d, "commit-tree", _g(d, "write-tree", env=env), "-m", "code de la course neuve")
        self.lanceur_neuf = _ecrire(dossier / "lanceur_neuf.py", self.texte_lanceur)
        m = json.loads(MANIF.read_text(encoding="utf-8"))
        m.update(commit=self.commit_code, run_id=RID, cree_le="2026-11-20T12:00:00+00:00")
        self.manifeste = _ecrire(d / "runs" / RID / "manifeste.json", m)
        sha_m = hashlib.sha256(self.manifeste.read_bytes()).hexdigest()
        e = json.loads((DIAG / f"b-beta-ajustement-{L}.json").read_text(encoding="utf-8"))
        e.update(run_id=RID, manifeste_sha256=sha_m)
        e["resultat"]["debut_utc"] = "2026-11-20T13:00:00Z"
        if not octets_egaux:
            e["resultat"]["sha256"] = "0" * 64
        self.ajustement = _ecrire(d / "diag" / RID / f"b-beta-ajustement-{L}.json", e)
        self.export = None
        if L == "R":
            x = json.loads((DIAG / "b-beta-export.json").read_text(encoding="utf-8"))
            x.update(run_id=RID, manifeste_sha256=sha_m)
            x["resultat"]["debut_utc"] = "2026-11-20T18:00:00Z"
            self.export = _ecrire(d / "diag" / RID / "b-beta-export.json", x)
        _g(d, "add", "-A")
        _g(d, "commit", "-q", "-m", "resultats de la course neuve")
        self.commit_resultats = _g(d, "rev-parse", "HEAD")

    def arguments(self, **remplace) -> dict:
        a = dict(ref_ajustement=DIAG / f"b-beta-ajustement-{self.L}.json", neuf_ajustement=self.ajustement, ref_manifeste=MANIF,
                 neuf_manifeste=self.manifeste, lanceur_ref=LANCEUR, lanceur_neuf=self.lanceur_neuf,
                 ref_export=DIAG / "b-beta-export.json" if self.L == "R" else None, neuf_export=self.export, depot=self.depot,
                 commit_resultats=self.commit_resultats, chemin_lanceur_neuf=CHEMIN_LANCEUR_NEUF)
        a.update(remplace)
        return a

    def comparer(self, **remplace) -> dict:
        return c.comparer(c.charger(**self.arguments(**remplace)))

    def ligne(self, sortie: Path, **remplace) -> list[str]:
        """Les mêmes arguments, pour la ligne de commande."""
        out = ["--sortie", str(sortie)]
        for k, v in self.arguments(**remplace).items():
            if v is not None:
                out += ["--" + k.replace("_", "-"), str(v)]
        return out


_COURSES = {}


@pytest.fixture
def course(tmp_path_factory):
    """Rend la fabrique des courses neuves ; chaque dépôt n'est bâti qu'une fois, et aucun essai n'y écrit."""
    def fabrique(L="S", octets_egaux=False) -> _Course:
        if (L, octets_egaux) not in _COURSES:
            _COURSES[(L, octets_egaux)] = _Course(tmp_path_factory.mktemp(f"course-{L}-{int(octets_egaux)}"), L, octets_egaux)
        return _COURSES[(L, octets_egaux)]
    return fabrique


def _modifie(src: Path, dst: Path, f) -> Path:
    obj = json.loads(src.read_text(encoding="utf-8"))
    r = f(obj)
    return _ecrire(dst, obj if r is None else r)


# --- de bout en bout sur un vrai dépôt : cas sains ---------------------------------------------------------------------------
@pytest.mark.parametrize("L", ["R", "S"])
def test_v4_sain_de_bout_en_bout_palier_2(course, L):
    k = course(L)
    r = k.comparer()
    assert r["preconditions_toutes_tenues"], [p for p in r["preconditions"] if not p["tenu"]]
    assert r["mention"] == c.PALIER_2 and r["arret_sur_erreur"] is False
    ratt = r["rattachement_aux_commits"]
    attendues = {"commit_resultats", "ajustement_neuf", "manifeste_neuf", "commit_manifeste_ref", "commit_manifeste_neuf",
                 "lanceur_neuf"} | ({"export_neuf"} if L == "R" else set())
    assert set(ratt) == attendues and all(v["tenu"] is True for v in ratt.values())
    assert ratt["ajustement_neuf"]["chemin"] == f"diag/{RID}/b-beta-ajustement-{L}.json"
    assert ratt["ajustement_neuf"]["origine_du_chemin"].startswith("déduit")
    assert ratt["ajustement_neuf"]["commit"] == k.commit_resultats and ratt["lanceur_neuf"]["commit"] == k.commit_code
    assert ratt["lanceur_neuf"]["sha256_au_commit"] == r["pieces_lues"]["lanceur_neuf"] != r["pieces_lues"]["lanceur_ref"]
    for piece in ("ajustement_neuf", "manifeste_neuf"):
        assert ratt[piece]["sha256_au_commit"] == r["pieces_lues"][piece]


@pytest.mark.parametrize("L", ["R", "S"])
def test_v4_sain_de_bout_en_bout_palier_1(course, L):
    r = course(L, octets_egaux=True).comparer()
    assert r["preconditions_toutes_tenues"], [p for p in r["preconditions"] if not p["tenu"]]
    assert r["mention"] == c.PALIER_1 and r["declencheurs"] == ["(i) palier 1 obtenu"] and r["audit_requis"] is True


def test_v4_cli_saine_de_bout_en_bout(course, tmp_path, capsys):
    k = course("R")
    s = tmp_path / "sortie.json"
    c.main(k.ligne(s))
    sortie = json.loads(s.read_text(encoding="utf-8"))
    assert sortie["mention"] == c.PALIER_2 and sortie["preconditions_toutes_tenues"] and sortie["arret_sur_erreur"] is False
    assert sortie["programme"] == "comparer_reajustement_v4" and "v5" in sortie["critere"]
    assert sortie["commit_resultats"] == k.commit_resultats
    assert c.PALIER_2 in capsys.readouterr().out


# --- point 1, K2 : `depot_propre` -----------------------------------------------------------------------------------------
@pytest.mark.parametrize("cote", ["neuf", "ref"])
@pytest.mark.parametrize("val", [False, None, "absent", "true", 1])
def test_v4_k2_depot_propre(cote, val):
    assert MANIF.exists() and json.loads(MANIF.read_text(encoding="utf-8"))["depot_propre"] is True     # cas sain : le 18
    for egaux, mention in ((False, c.NON_COMPARABLE), (True, c.SUSPENDU)):
        cc = _base("S") if egaux else _octets_differents(_base("S"))
        if val == "absent":
            del cc[f"m{cote}"]["depot_propre"]
        else:
            cc[f"m{cote}"]["depot_propre"] = val
        r = c.comparer(cc)
        assert r["mention"] == mention and _pre_manque(r, f"`depot_propre` vrai dans le manifeste ({cote})")
        assert [p["nom"] for p in r["preconditions"] if not p["tenu"]] == [f"K2 : `depot_propre` vrai dans le manifeste ({cote})"]


def test_v4_k2_depot_propre_faux_dans_le_fichier_du_manifeste(course, tmp_path):
    # sonde U1 du rédacteur du critère v5 : manifeste neuf avec `depot_propre` faux, au deuxième palier
    k = course("S")
    m = _modifie(k.manifeste, tmp_path / "manifeste.json", lambda o: o.update(depot_propre=False))
    r = k.comparer(neuf_manifeste=m)
    assert r["mention"] == c.NON_COMPARABLE and _pre_manque(r, "`depot_propre` vrai dans le manifeste (neuf)")


# --- point 2, K5 : champs du haut du manifeste, sans critère --------------------------------------------------------------
def test_v4_k5_haut_sain_seul_l_identifiant_de_course_differe():
    r = c.comparer(_octets_differents(_base("S")))
    assert set(r["differences_des_manifestes_sans_critere"]["haut"]) == {"run_id"}
    assert r["mention"] == c.PALIER_2


@pytest.mark.parametrize("champ,val", [("graines", {"autre": 1}), ("preenregistrement", {"chemin": "autre.md", "sha256": "0" * 64}),
                                       ("commande", "autre commande"), ("cree_le", "2026-11-20T12:00:00+00:00"), ("decisif", False),
                                       ("reserves", ["une réserve"]), ("config_sha256", "1" * 64)])
def test_v4_k5_haut_champ_change_rapporte_sans_critere(champ, val):
    # sondes U2 et U3 : rien ne paraissait dans la table ; le palier ne change pas (sans critère)
    cc = _octets_differents(_base("S"))
    cc["mneuf"][champ] = val
    r = c.comparer(cc)
    h = r["differences_des_manifestes_sans_critere"]["haut"]
    assert champ in h and h[champ]["present_ref"] and h[champ]["present_neuf"]
    assert h[champ]["sha256_valeur_ref"] != h[champ]["sha256_valeur_neuf"] and h[champ]["neuf"] == str(val)[:200]
    assert r["mention"] == c.PALIER_2 and r["preconditions_toutes_tenues"]


def test_v4_k5_haut_champ_present_d_un_seul_cote():
    cc = _octets_differents(_base("S"))
    cc["mneuf"]["champ_neuf"] = None
    del cc["mneuf"]["reserves"]
    r = c.comparer(cc)
    h = r["differences_des_manifestes_sans_critere"]["haut"]
    assert (h["champ_neuf"]["present_ref"], h["champ_neuf"]["present_neuf"]) == (False, True)
    assert h["champ_neuf"]["ref"] is None and h["champ_neuf"]["sha256_valeur_ref"] is None and h["champ_neuf"]["neuf"] == "None"
    assert (h["reserves"]["present_ref"], h["reserves"]["present_neuf"]) == (True, False)
    assert r["mention"] == c.PALIER_2


def test_v4_k5_haut_difference_au_dela_du_debut_de_la_valeur():
    # deux valeurs longues qui ne diffèrent qu'après le 200e caractère : le champ paraît, et les empreintes des valeurs diffèrent
    cc = _octets_differents(_base("S"))
    cc["mref"]["commande"] = "x" * 300 + "a"
    cc["mneuf"]["commande"] = "x" * 300 + "b"
    h = c.differences_manifestes(cc["mref"], cc["mneuf"])["haut"]["commande"]
    assert h["ref"] == h["neuf"] and h["sha256_valeur_ref"] != h["sha256_valeur_neuf"]


def test_v4_k5_haut_ne_double_pas_les_tables_existantes_et_montre_depot_propre():
    cc = _octets_differents(_base("S"))
    cc["mneuf"]["depot_propre"] = False
    d = c.comparer(cc)["differences_des_manifestes_sans_critere"]
    assert "depot_propre" in d["haut"] and not {"versions", "commit", "config"} & set(d["haut"])
    assert set(d) == {"versions", "commit", "config", "haut"}


# --- point 3, K1 : fonctions de lecture du dépôt, sur un vrai petit dépôt git à un commit ----------------------------------
@pytest.fixture
def petit_depot(depot):
    """Le dépôt jetable de `conftest.py` (un `git init` dans `tmp_path`), avec un fichier, un dossier et un second commit."""
    _ecrire(depot / "pieces/resultat.json", b'{"a": 1}\n')
    _g(depot, "add", "-A")
    _g(depot, "commit", "-q", "-m", "pieces")
    premier = _g(depot, "rev-parse", "HEAD")
    _ecrire(depot / "pieces/resultat.json", b'{"a": 2}\n')
    _g(depot, "add", "-A")
    _g(depot, "commit", "-q", "-m", "pieces retouchees")
    return depot, premier, _g(depot, "rev-parse", "HEAD")


def test_v4_k1_commit_lisible(petit_depot, tmp_path_factory):
    d, premier, second = petit_depot
    assert c.commit_lisible(d, premier) == (True, premier) and c.commit_lisible(d, second) == (True, second)     # cas sains
    arbre = _g(d, "rev-parse", f"{second}^{{tree}}")
    for artefact in ("d" * 40, "main", "HEAD", second[:12], second.upper(), "n'importe quoi", "", None, 12, arbre,
                     "--help", second + "\n"):
        ok, motif = c.commit_lisible(d, artefact)
        assert ok is False and motif, artefact
    assert c.commit_lisible(None, second)[0] is False                                      # aucun dépôt donné
    assert c.commit_lisible(tmp_path_factory.mktemp("pas-un-depot"), second)[0] is False   # un dossier qui n'est pas un dépôt


def test_v4_k1_octets_au_commit(petit_depot):
    d, premier, second = petit_depot
    assert c.octets_au_commit(d, premier, "pieces/resultat.json") == (b'{"a": 1}\n', "")
    assert c.octets_au_commit(d, second, "pieces/resultat.json") == (b'{"a": 2}\n', "")
    for commit, chemin in ((second, "pieces/absent.json"), (second, "pieces"), (second, ""), (second, None), (second, 3),
                           (second, str(d / "pieces/resultat.json")), ("d" * 40, "pieces/resultat.json"),
                           ("main", "pieces/resultat.json")):
        b, motif = c.octets_au_commit(d, commit, chemin)
        assert b is None and motif, (commit, chemin)


def test_v4_k1_rattacher(petit_depot):
    d, premier, second = petit_depot
    sain = c.rattacher(d, second, "pieces/resultat.json", b'{"a": 2}\n')
    assert sain["tenu"] is True and sain["sha256_lu"] == sain["sha256_au_commit"] == hashlib.sha256(b'{"a": 2}\n').hexdigest()
    assert sain["chemin"] == "pieces/resultat.json" and sain["commit"] == second
    # artefacts : les octets d'un autre commit ; un octet de plus ; un commit absent ; un chemin absent
    autre = c.rattacher(d, premier, "pieces/resultat.json", b'{"a": 2}\n')
    assert autre["tenu"] is False and autre["sha256_lu"] != autre["sha256_au_commit"] and "octets différents" in autre["detail"]
    assert c.rattacher(d, second, "pieces/resultat.json", b'{"a": 2}\n ')["tenu"] is False
    absent = c.rattacher(d, "d" * 40, "pieces/resultat.json", b'{"a": 2}\n')
    assert absent["tenu"] is False and absent["sha256_au_commit"] is None and "illisible" in absent["detail"]
    assert c.rattacher(d, second, None, b'{"a": 2}\n')["tenu"] is False
    assert c.rattacher(None, second, "pieces/resultat.json", b'{"a": 2}\n')["tenu"] is False


def test_v4_k1_chemin_dans_depot(petit_depot, tmp_path_factory):
    d, _, _ = petit_depot
    assert c.chemin_dans_depot(d, d / "pieces/resultat.json", None)[0] == "pieces/resultat.json"
    assert c.chemin_dans_depot(d / "pieces", d / "pieces/resultat.json", None)[0] == "pieces/resultat.json"    # depuis la racine
    assert c.chemin_dans_depot(d, d / "pieces/resultat.json", "autre/chemin.json") == ("autre/chemin.json", "donné en argument")
    dehors = tmp_path_factory.mktemp("dehors")
    assert c.chemin_dans_depot(d, dehors / "resultat.json", None)[0] is None                 # hors du dépôt, non déductible
    assert c.chemin_dans_depot(dehors, d / "pieces/resultat.json", None)[0] is None          # le « dépôt » n'en est pas un


def test_v4_empreintes_correctifs_formes(petit_depot):
    d, _, second = petit_depot
    assert c.empreintes_correctifs(d, second, ["pieces/resultat.json"]) == {
        "pieces/resultat.json": hashlib.sha256(b'{"a": 2}\n').hexdigest()}
    for artefact in (None, [], "pieces/resultat.json", [["pieces/resultat.json"]], [1], {"pieces/resultat.json": 1}, [""],
                     ["pieces/absent.json"], ["pieces"]):
        assert c.empreintes_correctifs(d, second, artefact) is None, artefact
    assert c.empreintes_correctifs(d, "d" * 40, ["pieces/resultat.json"]) is None
    assert c.empreintes_correctifs(d, None, ["pieces/resultat.json"]) is None


# --- point 3, K1 : de bout en bout ----------------------------------------------------------------------------------------
@pytest.mark.parametrize("commit", ["d" * 40, "main", "HEAD", "n'importe quoi", None, "abrege"])
def test_v4_k1_commit_des_resultats_absent_ou_mal_forme(course, commit):
    # sonde U4 : un commit quelconque était recopié sans contrôle
    for egaux, mention in ((False, c.NON_COMPARABLE), (True, c.SUSPENDU)):
        k = course("S", octets_egaux=egaux)
        r = k.comparer(commit_resultats=k.commit_resultats[:10] if commit == "abrege" else commit)
        assert r["mention"] == mention
        for nom in ("K1 : commit de la branche de résultats", "K1 : résultat d'ajustement neuf", "K1 : manifeste neuf"):
            assert _pre_manque(r, nom), nom


def test_v4_k1_commit_d_avant_les_resultats(course):
    k = course("S")
    r = k.comparer(commit_resultats=k.commit_code)       # un vrai commit, mais les pièces n'y sont pas
    assert r["mention"] == c.NON_COMPARABLE and not _pre_manque(r, "K1 : commit de la branche de résultats")
    assert _pre_manque(r, "K1 : résultat d'ajustement neuf") and _pre_manque(r, "K1 : manifeste neuf")


@pytest.mark.parametrize("piece", ["ajustement", "export", "manifeste"])
def test_v4_k1_piece_neuve_modifiee_d_un_octet_apres_le_commit(course, tmp_path, piece):
    k = course("R")
    src = {"ajustement": k.ajustement, "export": k.export, "manifeste": k.manifeste}[piece]
    chemin = src.relative_to(k.depot).as_posix()
    cle_f = "neuf_manifeste" if piece == "manifeste" else f"neuf_{piece}"
    # cas sain : la même pièce, copiée hors du dépôt, avec son chemin donné en argument
    copie = _ecrire(tmp_path / "copie.json", src.read_bytes())
    r = k.comparer(**{cle_f: copie, f"chemin_neuf_{piece}": chemin})
    assert r["mention"] == c.PALIER_2 and r["rattachement_aux_commits"][f"{piece}_neuf"]["origine_du_chemin"] == "donné en argument"
    # artefact : un octet de plus
    r = k.comparer(**{cle_f: _copie_modifiee(src, tmp_path / "modifiee.json"), f"chemin_neuf_{piece}": chemin})
    assert r["mention"] == c.NON_COMPARABLE and _pre_manque(r, "K1 : " + {"ajustement": "résultat d'ajustement neuf",
                                                                           "export": "export neuf", "manifeste": "manifeste neuf"}[piece])
    if piece != "manifeste":           # le manifeste retouché manque aussi le préalable « égal à celui que porte le résultat »
        assert sum(1 for p in r["preconditions"] if not p["tenu"]) == 1


def test_v4_k1_piece_hors_du_depot_sans_chemin(course, tmp_path):
    k = course("S")
    r = k.comparer(neuf_ajustement=_ecrire(tmp_path / "copie.json", k.ajustement.read_bytes()))
    assert r["mention"] == c.NON_COMPARABLE and _pre_manque(r, "K1 : résultat d'ajustement neuf")
    assert "non déductible" in r["rattachement_aux_commits"]["ajustement_neuf"]["origine_du_chemin"]


@pytest.mark.parametrize("chemin", ["diag/absent.json", "diag", "runs/20261120-120000-neuron-lens-reajustement/manifeste.json"])
def test_v4_k1_chemin_donne_faux(course, chemin):
    r = course("S").comparer(chemin_neuf_ajustement=chemin)       # absent, dossier, ou une autre pièce du même commit
    assert r["mention"] == c.NON_COMPARABLE and _pre_manque(r, "K1 : résultat d'ajustement neuf")


def test_v4_k1_octets_egaux_piece_non_versee_suspend(course, tmp_path):
    k = course("S", octets_egaux=True)
    r = k.comparer(neuf_ajustement=_copie_modifiee(k.ajustement, tmp_path / "m.json"),
                   chemin_neuf_ajustement=k.ajustement.relative_to(k.depot).as_posix())
    assert r["mention"] == c.SUSPENDU and any(d.startswith("(v)") and "K1" in d for d in r["declencheurs"])


def test_v4_sans_depot_rien_n_est_rattache(course):
    r = course("S").comparer(depot=None)
    assert r["mention"] == c.NON_COMPARABLE and r["rattachement_aux_commits"] == {}
    for nom in ("K1 : commit", "K1 : résultat", "K1 : manifeste", "K2 : commit du manifeste lisible dans le dépôt (ref)",
                "K2 : commit du manifeste lisible dans le dépôt (neuf)", "K2 : lanceur neuf", "correctifs"):
        assert _pre_manque(r, nom), nom


@pytest.mark.parametrize("cle", ["commit_resultats", "ajustement_neuf", "manifeste_neuf", "export_neuf", "commit_manifeste_ref",
                                 "commit_manifeste_neuf", "lanceur_neuf"])
@pytest.mark.parametrize("artefact", ["faux", "absent", "pas_un_releve", "tenu_non_booleen"])
def test_v4_k1_k2_releve_de_rattachement_manque(cle, artefact):
    noms = {"commit_resultats": "K1 : commit de la branche de résultats", "ajustement_neuf": "K1 : résultat d'ajustement neuf",
            "manifeste_neuf": "K1 : manifeste neuf", "export_neuf": "K1 : export neuf",
            "commit_manifeste_ref": "K2 : commit du manifeste lisible dans le dépôt (ref)",
            "commit_manifeste_neuf": "K2 : commit du manifeste lisible dans le dépôt (neuf)", "lanceur_neuf": "K2 : lanceur neuf"}
    for egaux, mention in ((False, c.NON_COMPARABLE), (True, c.SUSPENDU)):
        cc = _base("R") if egaux else _octets_differents(_base("R"))
        assert cc["rattachement"][cle]["tenu"] is True                 # cas sain : lu pour de vrai dans le dépôt de travail
        if artefact == "faux":
            cc["rattachement"][cle]["tenu"] = False
        elif artefact == "absent":
            del cc["rattachement"][cle]
        elif artefact == "pas_un_releve":
            cc["rattachement"][cle] = True
        else:
            cc["rattachement"][cle]["tenu"] = "oui"
        r = c.comparer(cc)
        assert r["mention"] == mention
        assert [p["nom"] for p in r["preconditions"] if not p["tenu"]] == [next(p["nom"] for p in r["preconditions"]
                                                                                 if p["nom"].startswith(noms[cle]))]


@pytest.mark.parametrize("cle", ["ajustement_neuf", "manifeste_neuf", "export_neuf", "lanceur_neuf"])
def test_v4_k1_k2_empreinte_au_commit_egale_a_celle_que_porte_la_sortie(cle):
    # K1, à la lettre : « chaque empreinte de pièce neuve que porte la sortie est égale à celle du fichier du même chemin à ce commit »
    cc = _octets_differents(_base("R"))
    cc["sha_pieces"][cle] = "a" * 64
    r = c.comparer(cc)
    assert r["mention"] == c.NON_COMPARABLE and any(not p["tenu"] and p["nom"].startswith(("K1", "K2")) for p in r["preconditions"])
    cc = _octets_differents(_base("R"))
    del cc["sha_pieces"][cle]
    assert c.comparer(cc)["mention"] == c.NON_COMPARABLE


def test_v4_rattachement_absent_ou_mal_forme():
    for val in ({}, None, [], "oui"):
        cc = _octets_differents(_base("S"))
        cc["rattachement"] = val
        r = c.comparer(cc)
        assert r["mention"] == c.NON_COMPARABLE and _pre_manque(r, "K1 : commit") and _pre_manque(r, "K2 : lanceur neuf")


# --- point 4, K2 : lanceur neuf rattaché à sa course ----------------------------------------------------------------------
def test_v4_k2_lanceur_neuf_qui_n_est_pas_celui_du_commit(course, tmp_path):
    k = course("S")
    # même fonction (le préalable sur le texte de la fonction tient), mais un autre fichier que celui du commit du manifeste neuf
    autre = _ecrire(tmp_path / "lanceur.py", k.texte_lanceur + b"# une ligne de plus\n")
    r = k.comparer(lanceur_neuf=autre)
    assert r["mention"] == c.NON_COMPARABLE
    assert [p["nom"] for p in r["preconditions"] if not p["tenu"]] == [
        "K2 : lanceur neuf égal, à l'octet, au fichier du commit du manifeste neuf"]
    # le lanceur du 18 donné comme lanceur neuf : même fonction, autre fichier
    assert _pre_manque(k.comparer(lanceur_neuf=LANCEUR), "K2 : lanceur neuf")


@pytest.mark.parametrize("chemin", [None, "src/absent.py", "src", CHEMIN_LANCEUR])
def test_v4_k2_chemin_du_lanceur_faux(course, chemin):
    # absent, dossier, ou le lanceur du 18 (présent au commit, mais ce n'est pas le fichier donné)
    r = course("S").comparer(chemin_lanceur_neuf=chemin)
    assert r["mention"] == c.NON_COMPARABLE and _pre_manque(r, "K2 : lanceur neuf")


def test_v4_k2_lanceur_lu_au_commit_du_manifeste_et_non_a_celui_des_resultats(course, tmp_path):
    # le manifeste neuf porte le commit du 18, où le lanceur neuf n'existe pas : le lanceur n'est pas rattaché
    k = course("S")
    m = _modifie(k.manifeste, tmp_path / "manifeste.json", lambda o: o.update(commit=COMMIT_18))
    r = k.comparer(neuf_manifeste=m)
    assert _pre_manque(r, "K2 : lanceur neuf") and not _pre_manque(r, "K2 : commit du manifeste lisible dans le dépôt (neuf)")
    assert not _pre_manque(r, "correctifs")


@pytest.mark.parametrize("commit", ["f" * 40, "main", None, 7])
def test_v4_k2_commit_du_manifeste_neuf_illisible(course, tmp_path, commit):
    k = course("S")
    m = _modifie(k.manifeste, tmp_path / "manifeste.json", lambda o: o.update(commit=commit))
    r = k.comparer(neuf_manifeste=m)
    assert r["mention"] == c.NON_COMPARABLE and r["arret_sur_erreur"] is False
    for nom in ("K2 : commit du manifeste lisible dans le dépôt (neuf)", "K2 : lanceur neuf", "correctifs"):
        assert _pre_manque(r, nom), nom
    assert not _pre_manque(r, "K2 : commit du manifeste lisible dans le dépôt (ref)")


def test_v4_k2_octets_egaux_lanceur_non_rattache_suspend(course):
    r = course("S", octets_egaux=True).comparer(lanceur_neuf=LANCEUR)
    assert r["mention"] == c.SUSPENDU and any("K2 : lanceur neuf" in d for d in r["declencheurs"])


def test_v4_lanceur_neuf_illisible_comme_python(course, tmp_path):
    r = course("S").comparer(lanceur_neuf=_ecrire(tmp_path / "lanceur.py", b"def (:\n"))
    assert r["mention"] == c.NON_COMPARABLE and r["arret_sur_erreur"] is False
    p = next(p for p in r["preconditions"] if "F2" in p["nom"])
    assert not p["tenu"] and "illisible" in p["detail"]
    assert c.empreinte_fonction_dans(LANCEUR.read_bytes()) == (c.REFERENCES["fonction"], "")              # cas sain
    assert c.empreinte_fonction_dans(b"x = 1\n")[0] is None and c.empreinte_fonction_dans(b"\xff\xfe")[0] is None


# --- point 5 : pièces mal formées, jamais d'exception ---------------------------------------------------------------------
_FORMES = {
    "enveloppe neuve en liste": (lambda cc: cc.update(env_neuf=[]), "enveloppe du résultat d'ajustement en dictionnaire (neuf)"),
    "enveloppe de référence en chaîne": (lambda cc: cc.update(env_ref="x"), "enveloppe du résultat d'ajustement en dictionnaire (ref)"),
    "résultat neuf en liste": (lambda cc: cc.update(neuf=[1, 2]), "résultat d'ajustement en dictionnaire (neuf)"),
    "résultat neuf absent": (lambda cc: cc.update(neuf=None), "résultat d'ajustement en dictionnaire (neuf)"),
    "résultat de référence en nombre": (lambda cc: cc.update(ref=3), "résultat d'ajustement en dictionnaire (ref)"),
    "manifeste neuf en liste": (lambda cc: cc.update(mneuf=[]), "manifeste en dictionnaire (neuf)"),
    "manifeste de référence absent": (lambda cc: cc.update(mref=None), "manifeste en dictionnaire (ref)"),
    "config en liste": (lambda cc: cc["mneuf"].update(config=["a"]), "`config` du manifeste en dictionnaire (neuf)"),
    "config en chaîne, référence": (lambda cc: cc["mref"].update(config="a"), "`config` du manifeste en dictionnaire (ref)"),
    "versions en liste": (lambda cc: cc["mneuf"].update(versions=["torch"]), "`versions` du manifeste en dictionnaire (neuf)"),
    "versions en liste, référence": (lambda cc: cc["mref"].update(versions=[["torch", "2"]]), "`versions` du manifeste en dictionnaire (ref)"),
    "correctifs non hachable": (lambda cc: cc["mneuf"]["config"].update(correctifs=[["a.diff"]]), "`config.correctifs` en liste non vide de chemins (neuf)"),
    "correctifs en dictionnaires": (lambda cc: cc["mneuf"]["config"].update(correctifs=[{"chemin": "a.diff"}]), "`config.correctifs` en liste non vide de chemins (neuf)"),
    "correctifs en chaîne": (lambda cc: cc["mneuf"]["config"].update(correctifs="a.diff"), "`config.correctifs` en liste non vide de chemins (neuf)"),
    "correctifs en dictionnaire, référence": (lambda cc: cc["mref"]["config"].update(correctifs={"a": 1}), "`config.correctifs` en liste non vide de chemins (ref)"),
    "correctifs vides": (lambda cc: cc["mneuf"]["config"].update(correctifs=[]), "`config.correctifs` en liste non vide de chemins (neuf)"),
    "correctifs avec un nombre": (lambda cc: cc["mneuf"]["config"].update(correctifs=[1]), "`config.correctifs` en liste non vide de chemins (neuf)"),
    "meta en liste": (lambda cc: cc["neuf"].update(meta=["R"]), "meta présent"),
    "diffs en liste": (lambda cc: cc["neuf"].update(diffs=[0.1]), "mêmes cibles"),
    "empreinte en liste": (lambda cc: cc["neuf"].update(sha256=["0" * 64]), "empreinte du fichier d'ajustement bien formée (neuf)"),
    "lentille en dictionnaire": (lambda cc: cc.update(lentille={"R": 1}), "champ `etape` conforme à la lentille"),
    "lentille en liste": (lambda cc: cc.update(lentille=["R"]), "pièce d'ajustement de référence"),
    "empreintes des pièces absentes": (lambda cc: cc.update(sha_pieces=None), "manifeste de référence"),
    "correctifs lus en liste": (lambda cc: cc.update(correctifs_neuf=["x"]), "contenu des correctifs"),
    "enveloppe de l'export en liste": (lambda cc: cc.update(env_eneuf=[]), "enveloppe de l'export neuf en dictionnaire"),
    "export neuf en liste": (lambda cc: cc.update(eneuf=[]), "export de R présent"),
    "export de référence en chaîne": (lambda cc: cc.update(eref="x"), "export de R présent"),
    "matrices en liste": (lambda cc: cc["eneuf"].update(matrices_moities=[1]), "export de R présent"),
    "valeurs en liste": (lambda cc: cc["eneuf"].update(valeurs=[1]), "série npR_notre_R présente"),
    "série en liste": (lambda cc: cc["eneuf"]["valeurs"].update(npR_notre_R=[0.1] * 28), "série npR_notre_R présente"),
    "clé de série non entière": (lambda cc: cc["eneuf"]["valeurs"]["npR_notre_R"].update({"x": 0.1}), "série npR_notre_R"),
}


@pytest.mark.parametrize("cas", list(_FORMES))
def test_v4_piece_mal_formee_rend_non_comparable_avec_motif(cas):
    f, morceau = _FORMES[cas]
    for egaux in (False, True):
        cc = _base("R") if egaux else _octets_differents(_base("R"))
        assert not any(not p["tenu"] for p in c.preconditions(cc))                    # cas sain
        f(cc)
        r = c.comparer(cc)                                                             # aucune exception
        assert r["arret_sur_erreur"] is False and _pre_manque(r, morceau), [p["nom"] for p in r["preconditions"] if not p["tenu"]]
        assert r["mention"] in (c.NON_COMPARABLE, c.SUSPENDU) and r["audit_requis"] is True
        if not egaux:
            assert r["mention"] == c.NON_COMPARABLE and r["declencheurs"] == ["(iv) non comparable"]
        json.dumps(r)                                                                  # la sortie reste écrivable


@pytest.mark.parametrize("c_entier", [None, [], "x", {}])
def test_v4_entree_qui_n_est_pas_le_dictionnaire_attendu(c_entier):
    r = c.comparer(c_entier)
    assert r["mention"] == c.NON_COMPARABLE and r["arret_sur_erreur"] is False and not r["preconditions_toutes_tenues"]


_FICHIERS = {
    # sondes U11 à U14 du rédacteur du critère v5 : quatre arrêts sur une erreur du programme v3
    "U11 résultat neuf en liste": ("neuf_ajustement", lambda o: [], "enveloppe du résultat d'ajustement en dictionnaire (neuf)"),
    "U11 bis résultat intérieur en liste": ("neuf_ajustement", lambda o: o.update(resultat=[1]), "résultat d'ajustement en dictionnaire (neuf)"),
    "U12 manifeste neuf en liste": ("neuf_manifeste", lambda o: [], "manifeste en dictionnaire (neuf)"),
    "U13 versions en liste": ("neuf_manifeste", lambda o: o.update(versions=["torch"]), "`versions` du manifeste en dictionnaire (neuf)"),
    "U14 correctifs non hachable": ("neuf_manifeste", lambda o: o["config"].update(correctifs=[["a.diff"]]), "`config.correctifs`"),
    "U14 bis correctifs en chaîne": ("neuf_manifeste", lambda o: o["config"].update(correctifs="a.diff"), "`config.correctifs`"),
    "manifeste en chaîne": ("neuf_manifeste", lambda o: "manifeste", "manifeste en dictionnaire (neuf)"),
    "config nulle": ("neuf_manifeste", lambda o: o.update(config=None), "`config` du manifeste en dictionnaire (neuf)"),
    "export neuf en liste": ("neuf_export", lambda o: [], "enveloppe de l'export neuf en dictionnaire"),
    "export neuf sans résultat": ("neuf_export", lambda o: o.update(resultat="x"), "export de R présent"),
}


@pytest.mark.parametrize("cas", list(_FICHIERS))
def test_v4_cli_fichier_mal_forme_ecrit_une_sortie_non_comparable(course, tmp_path, cas):
    cle, f, morceau = _FICHIERS[cas]
    k = course("R")
    src = k.arguments()[cle]
    s = tmp_path / "sortie.json"
    c.main(k.ligne(s, **{cle: _modifie(src, tmp_path / src.name, f)}))                # aucune exception, aucun arrêt
    sortie = json.loads(s.read_text(encoding="utf-8"))
    assert sortie["mention"] == c.NON_COMPARABLE and sortie["arret_sur_erreur"] is False and sortie["audit_requis"] is True
    assert _pre_manque(sortie, morceau), [p["nom"] for p in sortie["preconditions"] if not p["tenu"]]
    assert sortie["ligne_de_commande"][0] == "comparer_reajustement_v4"


_ILLISIBLES = {
    "manifeste qui n'est pas du JSON": ("neuf_manifeste", b"{pas du json", "JSONDecodeError"),
    "résultat vide": ("neuf_ajustement", b"", "JSONDecodeError"),
    "résultat qui n'est pas de l'UTF-8": ("neuf_ajustement", b"\xff\xfe{}", "UnicodeDecodeError"),
    "export tronqué": ("neuf_export", b'{"resultat": {', "JSONDecodeError"),
    "manifeste de référence illisible": ("ref_manifeste", b"[", "JSONDecodeError"),
    "lanceur neuf absent": ("lanceur_neuf", None, "FileNotFoundError"),
    "résultat neuf absent": ("neuf_ajustement", None, "FileNotFoundError"),
}


@pytest.mark.parametrize("cas", list(_ILLISIBLES))
@pytest.mark.parametrize("egaux", [False, True])
def test_v4_cli_arret_sur_une_erreur_ecrit_la_sortie_et_le_motif(course, tmp_path, capsys, cas, egaux):
    cle, octets, type_erreur = _ILLISIBLES[cas]
    k = course("R", octets_egaux=egaux)
    fichier = tmp_path / "piece"
    if octets is not None:
        fichier.write_bytes(octets)
    s = tmp_path / "sortie.json"
    with pytest.raises(SystemExit) as arret:
        c.main(k.ligne(s, **{cle: fichier}))
    assert arret.value.code == 2
    sortie = json.loads(s.read_text(encoding="utf-8"))
    # « mention suspendue » si le résultat neuf porte l'empreinte du 18 (critère v5, § 4) ; le résultat neuf illisible n'en porte aucune
    porte_le_18 = egaux and cle != "neuf_ajustement"
    assert sortie["mention"] == (c.SUSPENDU if porte_le_18 else c.NON_COMPARABLE)
    assert sortie["declencheurs"][0].startswith("(v) arrêt sur une erreur" if porte_le_18 else "(iv) non comparable : arrêt sur une erreur")
    assert sortie["arret_sur_erreur"] is True and sortie["audit_requis"] is True and sortie["preconditions_toutes_tenues"] is False
    assert sortie["erreur"]["type"] == type_erreur and sortie["erreur"]["message"] and sortie["erreur"]["etape"] == "lecture des pièces"
    assert "nœud de Lazar" in sortie["noeud_de_lazar"] and sortie["ligne_de_commande"][0] == "comparer_reajustement_v4"
    assert sortie["commit_resultats"] == k.commit_resultats and sortie["lentille"] == "R"
    assert sortie["pieces_lues"]["ajustement_ref"] == c.REFERENCES["ajustement-R"]
    if octets is None:
        assert sortie["pieces_lues"][cle.split("_")[1] + "_" + cle.split("_")[0]].startswith("illisible")
    assert "arrêt sur une erreur" in capsys.readouterr().err
    with pytest.raises(SystemExit) as refus:                       # et la sortie écrite n'est jamais écrasée (R12)
        c.main(k.ligne(s))
    assert refus.value.code != 2 and json.loads(s.read_text(encoding="utf-8")) == sortie


def test_v4_cli_arret_reference_illisible_le_resultat_neuf_porte_l_empreinte_du_18(course, tmp_path):
    # la pièce de référence n'est pas lisible : l'empreinte du 18 est alors celle des constantes du critère (§ 2)
    k = course("S", octets_egaux=True)
    s = tmp_path / "sortie.json"
    with pytest.raises(SystemExit):
        c.main(k.ligne(s, ref_ajustement=_ecrire(tmp_path / "ref.json", b"{")))
    assert json.loads(s.read_text(encoding="utf-8"))["mention"] == c.SUSPENDU
    for L in ("R", "S"):
        assert c.EMPREINTES_FICHIERS_18[L] == json.loads((DIAG / f"b-beta-ajustement-{L}.json").read_text())["resultat"]["sha256"]


@pytest.mark.parametrize("sha_neuf,sha_ref,mention", [
    ("0" * 64, "0" * 64, c.SUSPENDU), (c.EMPREINTES_FICHIERS_18["R"], None, c.SUSPENDU), (c.EMPREINTES_FICHIERS_18["S"], "1" * 64, c.SUSPENDU),
    ("0" * 64, "1" * 64, c.NON_COMPARABLE), (None, None, c.NON_COMPARABLE), ("abc", "abc", c.NON_COMPARABLE), (["x"], ["x"], c.NON_COMPARABLE)])
def test_v4_sortie_arret_sur_erreur_choix_de_la_mention(sha_neuf, sha_ref, mention):
    r = c.sortie_arret_sur_erreur(RuntimeError("panne"), sha_neuf=sha_neuf, sha_ref=sha_ref, etape="essai")
    assert r["mention"] == mention and r["arret_sur_erreur"] is True and r["erreur"] == dict(r["erreur"], type="RuntimeError", message="panne")
    assert "panne" in r["declencheurs"][0] and r["preconditions"] == []


@pytest.mark.parametrize("egaux", [False, True])
def test_v4_erreur_inattendue_dans_la_comparaison_rattrapee(monkeypatch, egaux):
    cc = _base("S") if egaux else _octets_differents(_base("S"))
    sain = c.comparer(copy.deepcopy(cc))
    assert sain["arret_sur_erreur"] is False and sain["mention"] == (c.PALIER_1 if egaux else c.PALIER_2)        # cas sain

    def panne(*a, **k):
        raise RuntimeError("panne inattendue")
    monkeypatch.setattr(c, "_table", panne)
    r = c.comparer(cc)                                                                 # aucune exception
    assert r["arret_sur_erreur"] is True and r["mention"] == (c.SUSPENDU if egaux else c.NON_COMPARABLE)
    assert r["erreur"]["type"] == "RuntimeError" and "panne inattendue" in r["erreur"]["message"] and r["erreur"]["etape"] == "comparaison"
    assert "panne" in r["erreur"]["trace"] and r["audit_requis"] is True and r["lentille"] == "S"
    assert r["commit_resultats"] == COMMIT_PIECES and r["pieces_lues"] == cc["sha_pieces"]
    json.dumps(r)


def test_v4_cli_erreur_inattendue_dans_la_comparaison_ecrit_la_sortie(course, tmp_path, monkeypatch):
    def panne(*a, **k):
        raise ZeroDivisionError("panne")
    monkeypatch.setattr(c, "_max_abs", panne)
    s = tmp_path / "sortie.json"
    with pytest.raises(SystemExit) as arret:
        c.main(course("S").ligne(s))
    sortie = json.loads(s.read_text(encoding="utf-8"))
    assert arret.value.code == 2 and sortie["mention"] == c.NON_COMPARABLE and sortie["erreur"]["type"] == "ZeroDivisionError"


def test_v4_cli_chemin_du_lanceur_neuf_obligatoire(course, tmp_path):
    k = course("S")
    ligne = k.ligne(tmp_path / "s.json")
    i = ligne.index("--chemin-lanceur-neuf")
    with pytest.raises(SystemExit):
        c.main(ligne[:i] + ligne[i + 2:])
    assert not (tmp_path / "s.json").exists()


# --- point 6 : `audit_requis` dès qu'un déclencheur est rendu (critère v5, § 6) --------------------------------------------
def _cas_audit(nom):
    if nom == "palier 2 sans déclencheur":
        cc = _octets_differents(_base("S"))
        cc["neuf"]["diffs_float64"]["mid"][0] += 1e-5
        return cc, None
    if nom == "(i) palier 1":
        return _base("S"), "(i)"
    if nom == "(ii) écart nul, octets différents":
        return _octets_differents(_base("S")), "(ii)"
    if nom == "(iii) différente":
        cc = _octets_differents(_base("S"))
        cc["neuf"]["diffs_float64"]["mid"][0] += 5e-3
        return cc, "(iii)"
    if nom == "(iv) non comparable":
        cc = _octets_differents(_base("S"))
        cc["neuf"]["n_docs"] = [1, 1]
        return cc, "(iv)"
    if nom == "(v) anomalie à empreinte égale":
        cc = _base("S")
        cc["neuf"]["taille"] += 1
        return cc, "(v)"
    if nom == "(vi) trop propre":
        cc = _octets_differents(_base("R"))
        cc["neuf"]["diffs_float64"]["mid"][0] += 1e-5
        return cc, "(vi)"
    cc = _octets_differents(_base("S"))
    cc["neuf"]["diffs_float64"]["mid"][0] += 1e-5
    cc["neuf"]["diffs"]["out"][2] += 0.05
    return cc, "(vii)"


@pytest.mark.parametrize("nom", ["palier 2 sans déclencheur", "(i) palier 1", "(ii) écart nul, octets différents", "(iii) différente",
                                 "(iv) non comparable", "(v) anomalie à empreinte égale", "(vi) trop propre", "(vii) écart sur diffs"])
def test_v4_audit_requis_pour_tout_declencheur(nom):
    cc, attendu = _cas_audit(nom)
    r = c.comparer(cc)
    if attendu is None:
        assert r["declencheurs"] == [] and r["audit_requis"] is False and r["mention"] == c.PALIER_2      # cas sain : aucun audit dû
    else:
        assert [d for d in r["declencheurs"] if d.startswith(attendu)] and r["audit_requis"] is True
        assert len({d.split(" ")[0] for d in r["declencheurs"]} - {"(i)"} - {attendu}) == 0


# --- point 7, mineures ----------------------------------------------------------------------------------------------------
@pytest.mark.parametrize("cote", ["neuf", "ref"])
@pytest.mark.parametrize("val", ["ajustement-R", "Export", None, "absent", ["export"]])
def test_v4_etape_de_l_export(cote, val):
    cc = _octets_differents(_base("R"))
    assert cc["eref"]["etape"] == "export" and cc["eneuf"]["etape"] == "export"        # cas sain : la pièce du 18
    if val == "absent":
        del cc[f"e{cote}"]["etape"]
    else:
        cc[f"e{cote}"]["etape"] = val
    r = c.comparer(cc)
    assert r["mention"] == c.NON_COMPARABLE
    assert [p["nom"] for p in r["preconditions"] if not p["tenu"]] == [f"champ `etape` de l'export égal à « export » ({cote})"]
    assert "series_export_R_sans_critere" in r and "matrices_moities_egales" in r     # les tables de R restent rendues


def test_v4_etape_de_l_export_au_premier_palier_suspend():
    cc = _base("R")
    cc["eneuf"]["etape"] = "autre"
    assert c.comparer(cc)["mention"] == c.SUSPENDU


def test_v4_etape_de_l_export_sans_objet_pour_s():
    assert not any("export" in p["nom"] for p in c.comparer(_base("S"))["preconditions"])


def test_v4_empreinte_du_lanceur_de_reference_versee_sans_critere(course):
    r = course("S").comparer()
    assert r["pieces_lues"]["lanceur_ref"] == hashlib.sha256(LANCEUR.read_bytes()).hexdigest()
    assert r["pieces_lues"]["lanceur_ref"].startswith("582fd9ef")
    # sans critère (critère v5, § 0.2, E1) : une autre empreinte de fichier ne change pas la mention ; seule la fonction est exigée
    cc = _octets_differents(_base("S"))
    cc["sha_pieces"]["lanceur_ref"] = "0" * 64
    r2 = c.comparer(cc)
    assert r2["mention"] == c.PALIER_2 and r2["pieces_lues"]["lanceur_ref"] == "0" * 64


def test_v4_etiquettes_nomment_le_critere_en_vigueur():
    source = Path(c.__file__).read_text(encoding="utf-8")
    assert "critère v3" not in source and "v4 et suivants" not in source
    assert "critère en vigueur" in source and "50657b89" in c.CRITERE and "v5" in c.CRITERE
    r = c.comparer(_base("S"))
    assert r["critere"] == c.CRITERE and r["programme"] == c.PROGRAMME == "comparer_reajustement_v4"


def test_v4_aucune_regle_de_decision_ne_change():
    assert (c.TOLERANCE, c.COHERENCE_PALIER_1, c.DIFFS_PALIER_1, c.DIFFS_PALIER_2, c.SEUIL_STABILITE) == (1e-3, 1e-9, 1e-6, 1e-3, 0.10)
    assert c.PALIER_1 == "palier 1 — même lentille, octets identiques"
    assert c.PALIER_2 == "palier 2 — différences entre moitiés concordantes à 10⁻³ près ; octets différents ; matrices non comparables"
    assert (c.DIFFERENTE, c.NON_COMPARABLE, c.SUSPENDU) == ("différente", "non comparable (traitée comme différente)",
                                                           "mention suspendue : anomalie (nœud de Lazar)")
    assert c.REFERENCES == {"ajustement-R": "129c43b020854fd395cb0e969dd7f8956844417684e1e3a1099fee5e7f16d2ab",
                            "ajustement-S": "2dce646e32177941c02987a8ba3a0a67fd45d17f335e58ba9e321d3e0367c297",
                            "export-R": "17304c936792e4b79e9a47d78abf5bb6966310c36b92f387b3303b23891eedf1",
                            "manifeste": "b90c15140074e9d41a3cf93e8bcaf55f80cc025d07d2d46432239d1c6b6e3444",
                            "fonction": "a5495c68779bb67059cade18b3a92aaf7cf7fd0200f1770b038d8c5d0e62703c"}
