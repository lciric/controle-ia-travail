"""Essais du programme de comparaison et de report v3 (additif 1, essais exigés du programme ; additif 2, M-4).

Données factices seulement : notes de deux blocs, fiches construites à partir des valeurs de référence de la version 6.
Les essais sur les pièces du dépôt (note v6, note v7, fiche) ne lisent que ces pièces et leurs compagnons."""
from __future__ import annotations

import copy
import json
from pathlib import Path

import pytest

from controle_ia.barreau8_moniteurs import comparer_interface_v6_v7_v3 as cmp

RACINE = Path(__file__).resolve().parents[1]
NOTE = "# Titre\n\nen-tête\n\n## Bloc A\n\ntexte a\n\n### (1) Sous-bloc\n\ntexte 1\n"


def deplier(valeurs: dict) -> dict:
    fiche: dict = {}
    for cle, v in valeurs.items():
        n = fiche
        parties = cle.split(".")
        for p in parties[:-1]:
            n = n.setdefault(p, {})
        n[parties[-1]] = copy.deepcopy(v)
    return fiche


def valeurs_v6() -> dict:
    return {k: copy.deepcopy(v[0]) for k, v in cmp.REFERENCE_V6.items()}


def valeurs_v7_json() -> dict:
    v = valeurs_v6()
    v["identifiants.fichier"] = "ids-actions-evaluation-iib-v5.json"
    v["identifiants.tableaux"] = ["avertissement", "ids"]
    v["identifiants.forme_cle"] = cmp.COUVERTURE_ADDITIF_2["identifiants.forme_cle"]
    v["identifiants.types"] = "entiers JSON (convertis en int64)"
    v["textes.fichier"] = ""
    v["textes.champs"] = []
    v["adaptateurs.fichiers"] = {"eleve": "adaptateur-eleve-iib-v5.pt", "temoin-jumeau": "adaptateur-temoin-jumeau-iib-v5.pt"}
    v["oracle.fichier"] = "evaluation-iib-v5.json"
    return v


def construire(valeurs: dict, note_v7: str = NOTE):
    sha7 = "a" * 64
    valeurs = dict(valeurs, **{"note.sha256": sha7, "note.chemin": cmp.CHEMIN_NOTE_V7})
    return cmp.construire(NOTE, note_v7, json.dumps(deplier(valeurs), ensure_ascii=False),
                          {"note_v6": cmp.SHA_NOTE_V6, "note_v7": sha7, "fiche_v7": "b" * 64})


# --- identité et version 7 ------------------------------------------------------------------------------------------

def test_identite_fiche_de_reference_rend_report_sans_champ_change_et_les_constantes_du_texte_scelle():
    piece, table = construire(valeurs_v6())
    assert table["mot_d_ensemble"] == "report"
    assert table["champs_changes"] == []
    c = table["constantes"]
    for cle in ("T", "E", "A", "J", "L", "K", "m", "N", "N_c", "k", "n15", "n7", "taille_de_pire_cas", "place_libre",
                "budget_recette_puissance_heures", "nombre_d_etats", "ordre_des_conditions", "conditions_sabotees",
                "reference_honnete", "temoin_jumeau", "condition_de_la_phrase_du_dommage", "taches", "adaptateurs",
                "invites", "motifs_de_chemins_prives_ajoutes", "pas_couche_decisive", "pas_couches_descriptives"):
        assert cmp._egal(c[cle], cmp.VALEURS_ATTENDUES_V7[cle]), cle
    assert c["noms_de_fichiers"]["identifiants"] == "ids-actions-iib-evaluation.npz"
    assert set(c["extrait_des_etats"]["paires"]) == {"B50-H", "B100-H", "TJ100-H", "B100-TJ100"}
    assert piece["resume_blocs"] == {"identique": 3, "changé": 0, "ajouté": 0, "absent de la version 7": 0}


def test_version_7_json_rend_report_quatre_champs_couverts_et_valeurs_attendues():
    _, table = construire(valeurs_v7_json())
    assert table["mot_d_ensemble"] == "report"
    couverts = sorted(l["champ"] for l in table["champs_changes"] if l["statut"] == cmp.STATUT_COUVERT)
    assert couverts == sorted(cmp.COUVERTURE_ADDITIF_2)
    assert cmp.ecarts_aux_valeurs_attendues(table) == []
    assert table["table_de_l_additif_1"] == {"chemin": cmp.CHEMIN_TABLE_ADDITIF_1, "sha256": cmp.SHA_TABLE_ADDITIF_1}
    statuts = {l["champ"]: l["statut"] for l in table["champs_changes"]}
    assert statuts["identifiants.fichier"] == statuts["textes.fichier"] == statuts["adaptateurs.fichiers"] == "report"
    assert [l for l in table["champs_changes"] if l["champ"] == "oracle.fichier"][0]["effet"] == "sans effet"


# --- additif 2, M-4 : essais exigés ---------------------------------------------------------------------------------

@pytest.mark.parametrize("cle,valeur", [("identifiants.tableaux", ["ids", "avertissement"]),
                                        ("identifiants.forme_cle", "<phase>/<épisode>"),
                                        ("identifiants.types", "int32"),
                                        ("textes.champs", ["texte"])])
def test_un_des_quatre_champs_a_une_autre_valeur_rend_noeud(cle, valeur):
    v = valeurs_v7_json()
    v[cle] = valeur
    _, table = construire(v)
    assert table["mot_d_ensemble"] == "nœud" and table["constantes"] is None
    assert {l["champ"]: l["statut"] for l in table["champs_changes"]}[cle] == "nœud"


def test_textes_fichier_non_vide_avec_champs_vides_rend_noeud():
    v = valeurs_v7_json()
    v["textes.fichier"] = "textes.jsonl"
    _, table = construire(v)
    assert table["mot_d_ensemble"] == "nœud"
    assert all(l["statut"] == "nœud" for l in table["champs_changes"] if l["champ"] in cmp.COUVERTURE_ADDITIF_2)


def test_deux_episodes_sous_la_forme_json_rend_noeud():
    v = valeurs_v7_json()
    v["effectifs.episodes_par_tache_et_condition"] = 2
    v["textes.episode_egal_tache"] = "non"
    v["effectifs.actions"] = 64 * 2 * 10 * 4
    _, table = construire(v)
    assert table["mot_d_ensemble"] == "nœud"


def test_un_cinquieme_champ_classe_noeud_change_rend_noeud():
    v = valeurs_v7_json()
    v["calcul.attention"] = "eager"
    _, table = construire(v)
    assert table["mot_d_ensemble"] == "nœud"
    assert {l["champ"]: l["statut"] for l in table["champs_changes"]}["calcul.attention"] == "nœud"


def test_etendue_autre_rend_noeud_condition_jointe():
    v = valeurs_v7_json()
    v["identifiants.etendue"] = "action et contexte"
    _, table = construire(v)
    assert table["mot_d_ensemble"] == "nœud"


# --- additif 1 : essais exigés -------------------------------------------------------------------------------------

def test_un_champ_classe_noeud_change_rend_noeud():
    v = valeurs_v6()
    v["modele.couches"] = 33
    _, table = construire(v)
    assert table["mot_d_ensemble"] == "nœud"


@pytest.mark.parametrize("defaut", ["manquante", "en_trop", "en_trop_imbriquee", "repetee", "type"])
def test_cle_manquante_en_trop_repetee_ou_d_un_autre_type_refus(defaut):
    fiche = deplier(dict(valeurs_v6(), **{"note.sha256": "a" * 64, "note.chemin": cmp.CHEMIN_NOTE_V7}))
    if defaut == "manquante":
        del fiche["calcul"]["lot"]
    elif defaut == "en_trop":
        fiche["autre"] = 1
    elif defaut == "en_trop_imbriquee":
        fiche["calcul"]["autre"] = 1
    elif defaut == "type":
        fiche["calcul"]["lot"] = "8"
    texte = json.dumps(fiche, ensure_ascii=False)
    if defaut == "repetee":
        texte = texte.replace('"lot": 8', '"lot": 8, "lot": 8')
    with pytest.raises(cmp.Refus):
        cmp.construire(NOTE, NOTE, texte, {"note_v6": cmp.SHA_NOTE_V6, "note_v7": "a" * 64, "fiche_v7": "b" * 64})


def test_booleen_a_la_place_d_un_entier_refus():
    v = valeurs_v6()
    v["calcul.lot"] = True
    with pytest.raises(cmp.Refus):
        construire(v)


def test_actions_differentes_du_produit_refus():
    v = valeurs_v6()
    v["effectifs.actions"] = 2559
    with pytest.raises(cmp.Refus):
        construire(v)


def test_pas_de_l_environnement_different_de_a_refus():
    v = valeurs_v6()
    v["contexte.pas_de_l_environnement"] = 9
    with pytest.raises(cmp.Refus):
        construire(v)


def test_avertissement_altere_refus():
    v = valeurs_v6()
    v["avertissement"] = "autre"
    with pytest.raises(cmp.Refus):
        construire(v)


def _conds(v):
    return v["conditions"]


def test_nom_de_condition_avec_tiret_rend_noeud():
    v = valeurs_v6()
    _conds(v)[1]["nom"] = "B-50"
    _, table = construire(v)
    assert table["mot_d_ensemble"] == "nœud" and not table["structure_des_roles_tenue"]


def test_reference_honnete_a_dose_non_nulle_rend_noeud():
    v = valeurs_v6()
    _conds(v)[0]["dose"] = 0.1
    _, table = construire(v)
    assert table["mot_d_ensemble"] == "nœud"


def test_sabotees_d_adaptateurs_differents_rend_noeud():
    v = valeurs_v6()
    _conds(v)[1]["adaptateur"] = "autre"
    v["adaptateurs.fichiers"]["autre"] = "adaptateur-autre.pt"
    _, table = construire(v)
    assert table["mot_d_ensemble"] == "nœud"


def test_sabotee_a_dose_nulle_rend_noeud():
    v = valeurs_v6()
    _conds(v)[1]["dose"] = 0
    _, table = construire(v)
    assert table["mot_d_ensemble"] == "nœud"


def test_temoin_jumeau_porte_l_adaptateur_des_sabotees_rend_noeud():
    v = valeurs_v6()
    _conds(v)[3]["adaptateur"] = "eleve"
    _, table = construire(v)
    assert table["mot_d_ensemble"] == "nœud"


def test_adaptateur_du_temoin_porte_par_une_autre_condition_rend_noeud():
    v = valeurs_v6()
    _conds(v)[0]["adaptateur"] = "temoin-jumeau"
    _, table = construire(v)
    assert table["mot_d_ensemble"] == "nœud"


def test_taille_que_nul_pas_ne_tient_rend_noeud():
    v = valeurs_v6()
    v["identifiants.plafond_jetons"] = 100_000
    _, table = construire(v)
    assert table["mot_d_ensemble"] == "nœud" and not table["pas_rp7_trouve"]


def test_pas_agrandi_qui_laisse_moins_de_81_actions_rend_noeud():
    r = cmp.regle_rp7(40, 17_000)          # k = 1 dépasse la borne ; k = 2 la tient avec n15 = 2 < 81
    assert r["pas_trouve"] is False and "sous 81" in r["cause"]
    v = valeurs_v6()
    v["effectifs.taches"] = 1
    v["effectifs.actions"] = 1 * 1 * 10 * 4
    v["identifiants.plafond_jetons"] = 17_000
    _, table = construire(v)
    assert table["mot_d_ensemble"] == "nœud" and not table["pas_rp7_trouve"]
    assert any("sous 81" in m for m in table["motifs_noeud"])


def test_moins_d_actions_qu_a_la_version_6_avec_les_pas_du_texte_scelle_rend_report():
    v = valeurs_v6()
    v["effectifs.taches"] = 32
    v["effectifs.actions"] = 32 * 1 * 10 * 4
    _, table = construire(v)
    assert table["mot_d_ensemble"] == "report"
    assert table["constantes"]["k"] == 1 and table["constantes"]["n15"] == 81 and table["constantes"]["n7"] == 11


def test_rp7_aux_valeurs_de_la_version_6():
    r = cmp.regle_rp7(2560, 400)
    assert r == {"pas_trouve": True, "k": 1, "pas_couche_decisive": 16, "pas_couches_descriptives": 128,
                 "n15": 161, "n7": 21, "taille_de_pire_cas": 1_502_781_440, "place_libre": 3_100_000_000}


@pytest.mark.parametrize("n,pas,attendu", [(2560, 16, 161), (2560, 128, 21), (1, 16, 1), (17, 16, 2), (16, 16, 2),
                                           (32, 16, 3), (33, 16, 3)])
def test_effectif_du_sous_echantillon(n, pas, attendu):
    assert cmp.effectif_sous_echantillon(n, pas) == attendu


def test_bloc_absent_refuse_la_note():
    with pytest.raises(cmp.Refus):
        construire(valeurs_v6(), note_v7="# Titre\n\nen-tête\n\n## Bloc A\n\ntexte a\n")


def test_bloc_ajoute_et_change():
    piece, _ = construire(valeurs_v6(), note_v7=NOTE.replace("texte 1", "texte 2") + "## Bloc B\n\nb\n")
    assert piece["resume_blocs"]["changé"] == 1 and piece["resume_blocs"]["ajouté"] == 1


def test_empreinte_de_la_note_v6_differente_refus():
    with pytest.raises(cmp.Refus):
        cmp.construire(NOTE, NOTE, "{}", {"note_v6": "0" * 64, "note_v7": "a" * 64, "fiche_v7": "b" * 64})


def test_note_sha_de_la_fiche_differente_de_la_note_lue_refus():
    v = dict(valeurs_v6(), **{"note.sha256": "c" * 64, "note.chemin": cmp.CHEMIN_NOTE_V7})
    with pytest.raises(cmp.Refus):
        cmp.construire(NOTE, NOTE, json.dumps(deplier(v), ensure_ascii=False),
                       {"note_v6": cmp.SHA_NOTE_V6, "note_v7": "a" * 64, "fiche_v7": "b" * 64})


def test_constante_non_finie_refusee():
    with pytest.raises(cmp.Refus):
        cmp.charger_json_strict('{"a": NaN}')


# --- pièces du dépôt ------------------------------------------------------------------------------------------------

def test_pieces_du_depot_rendent_report_valeurs_attendues_et_egalite_avec_la_version_1():
    texte_v6, texte_v7, fiche, empreintes = cmp.lire_les_trois(RACINE)
    piece, table = cmp.construire(texte_v6, texte_v7, fiche, empreintes)
    assert table["mot_d_ensemble"] == "report"
    assert cmp.ecarts_aux_valeurs_attendues(table) == []
    assert piece["resume_blocs"] == {"identique": 8, "changé": 14, "ajouté": 0, "absent de la version 7": 0}
    assert cmp.controler_contre_la_version_1(RACINE, piece, table) == []


def test_ecriture_refuse_d_ecraser(tmp_path):
    c = tmp_path / "x.json"
    cmp.ecrire_json_et_compagnon(c, {"a": 1})
    with pytest.raises(cmp.Refus):
        cmp.ecrire_json_et_compagnon(c, {"a": 2})
    assert cmp.lire_compagnon(c) == cmp.sha256_fichier(c)


# --- version 3 : corrections de la contre-lecture -------------------------------------------------------------------

import shutil


def test_note_chemin_de_la_fiche_different_refus():
    v = dict(valeurs_v6(), **{"note.sha256": "a" * 64, "note.chemin": "docs/autre-note.md"})
    with pytest.raises(cmp.Refus, match="note.chemin"):
        cmp.construire(NOTE, NOTE, json.dumps(deplier(v), ensure_ascii=False),
                       {"note_v6": cmp.SHA_NOTE_V6, "note_v7": "a" * 64, "fiche_v7": "b" * 64})


def test_ecarts_aux_valeurs_attendues_sur_une_autre_fiche():
    v = valeurs_v6()
    v["effectifs.taches"] = 32
    v["effectifs.actions"] = 32 * 10 * 4
    _, table = construire(v)
    ecarts = cmp.ecarts_aux_valeurs_attendues(table)
    assert any(e.startswith("T :") for e in ecarts) and any("couvert" in e for e in ecarts)
    _, noeud = construire(dict(valeurs_v6(), **{"modele.couches": 33}))
    assert cmp.ecarts_aux_valeurs_attendues(noeud) == ["mot d'ensemble « nœud » : aucune constante"]


def _racine_factice(tmp_path):
    """Copie, sous une racine factice, des pièces que lit le programme (notes, fiche, pièce v1, table de l'additif 1)."""
    racine = tmp_path / "depot"
    for c in (cmp.CHEMIN_NOTE_V6, cmp.CHEMIN_NOTE_V7, cmp.CHEMIN_FICHE_V7, cmp.CHEMIN_COMPARAISON_V1, cmp.CHEMIN_TABLE_ADDITIF_1):
        for x in (c, c + ".sha256"):
            (racine / x).parent.mkdir(parents=True, exist_ok=True)
            shutil.copy(RACINE / x, racine / x)
    (racine / cmp.CHEMIN_COMPARAISON_V2).parent.mkdir(parents=True, exist_ok=True)
    return racine


def _resceller(chemin):
    chemin.with_name(chemin.name + ".sha256").write_text(f"{cmp.sha256_fichier(chemin)}  {chemin.name}\n", encoding="utf-8")


def test_controler_contre_la_version_1_artefacts(tmp_path):
    racine = _racine_factice(tmp_path)
    texte_v6, texte_v7, fiche, empreintes = cmp.lire_les_trois(racine)
    piece, table = cmp.construire(texte_v6, texte_v7, fiche, empreintes)
    assert cmp.controler_contre_la_version_1(racine, piece, table) == []                     # sain
    # pièce v1 dont un bloc a un autre état : écart (et l'empreinte n'est plus celle de la v1)
    c = racine / cmp.CHEMIN_COMPARAISON_V1
    v1 = json.loads(c.read_text(encoding="utf-8"))
    v1["blocs"][2]["etat"] = "changé"
    c.write_text(json.dumps(v1, ensure_ascii=False), encoding="utf-8")
    _resceller(c)
    ecarts = cmp.controler_contre_la_version_1(racine, piece, table)
    assert any("états des blocs" in e for e in ecarts) and any("e744d824" in e for e in ecarts)
    # table de l'additif 1 aux champs « nœud » autres que les quatre
    racine = _racine_factice(tmp_path / "b")
    t = racine / cmp.CHEMIN_TABLE_ADDITIF_1
    t1 = json.loads(t.read_text(encoding="utf-8"))
    t1["champs_changes"] = [l for l in t1["champs_changes"] if l["champ"] != "textes.champs"]
    t.write_text(json.dumps(t1, ensure_ascii=False), encoding="utf-8")
    _resceller(t)
    ecarts = cmp.controler_contre_la_version_1(racine, piece, table)
    assert any("au lieu des quatre de la liste fermée" in e for e in ecarts) and any("f6e9c8d5" in e for e in ecarts)
    # statut d'un autre champ changé différent
    autre = json.loads(json.dumps(table))
    for l in autre["champs_changes"]:
        if l["champ"] == "identifiants.fichier":
            l["statut"] = "nœud"
    assert any("statuts des autres champs" in e for e in cmp.controler_contre_la_version_1(_racine_factice(tmp_path / "c"), piece, autre))


def test_ecrire_refuse_sans_rien_ecrire_si_la_version_1_differe(tmp_path):
    racine = _racine_factice(tmp_path)
    c = racine / cmp.CHEMIN_COMPARAISON_V1
    v1 = json.loads(c.read_text(encoding="utf-8"))
    v1["blocs"][0]["etat"] = "identique"
    c.write_text(json.dumps(v1, ensure_ascii=False), encoding="utf-8")
    _resceller(c)
    assert cmp.principal(["ecrire", "--racine", str(racine)]) == 2
    assert not (racine / cmp.CHEMIN_COMPARAISON_V2).exists() and not (racine / cmp.CHEMIN_TABLE_NEUVE).exists()


def test_ecrire_sain_puis_refuse_d_ecraser_sans_ecriture_partielle(tmp_path):
    racine = _racine_factice(tmp_path)
    assert cmp.principal(["ecrire", "--racine", str(racine)]) == 0
    assert cmp.principal(["controler", "--racine", str(racine)]) == 0
    table = json.loads((racine / cmp.CHEMIN_TABLE_NEUVE).read_text(encoding="utf-8"))
    assert table["mot_d_ensemble"] == "report" and table["programme"]["version"] == 3
    # la table seule présente : rien n'est écrit (aucune pièce de comparaison orpheline)
    (racine / cmp.CHEMIN_COMPARAISON_V2).unlink()
    Path(str(racine / cmp.CHEMIN_COMPARAISON_V2) + ".sha256").unlink()
    with pytest.raises(cmp.Refus, match="déjà présente"):
        cmp.principal(["ecrire", "--racine", str(racine)])
    assert not (racine / cmp.CHEMIN_COMPARAISON_V2).exists()
