"""Essais de `nos_lentilles_v1` (texte de lecture v2 scellé, `a2bbed7a…`, « Code neuf ») : lignes de registre et fiche de
rangement, place de la ligne de l'addendum de concentration, issue des nœuds N12 et N17, condition de lecture (un cas par
mention du critère d'identité), phrase du déclencheur (vi), fiche muette, première passe lancée et non achevée, accès,
archive de `torch.save` lue en flux, contrôles de `meta`, de l'état et des matrices. Cas sain et artefact pour chacun (R5).
Tout sur jouets ; graines `lentilles-bbis-v2/essai/<garde>`."""
from __future__ import annotations

import io
import re
import json
import zipfile

import numpy as np
import pytest

torch = pytest.importorskip("torch")

import lentilles_sondes_bbis_seconde_passe_jouets_v1 as J  # noqa: E402
from controle_ia.lentilles_sondes_bbis import constantes_v1 as K  # noqa: E402
from controle_ia.lentilles_sondes_bbis import constantes_v2 as K2  # noqa: E402
from controle_ia.lentilles_sondes_bbis import montage_v1 as mo  # noqa: E402
from controle_ia.lentilles_sondes_bbis import nos_lentilles_v1 as nl  # noqa: E402
from controle_ia.lentilles_sondes_bbis.constantes_v1 import Arret, FormeMalComprise, Refus  # noqa: E402

H = J.H


# === lignes de registre ======================================================================================================================
def test_sain_les_trois_lignes_de_la_v2_presentes(tmp_path):
    etat = nl.exiger_registre_v2(J.monde(tmp_path))
    assert etat.premiere_passe == nl.PREMIERE_PASSE_JAMAIS_LANCEE
    assert etat.derniere(K2.CLE_SCELLEMENT_V2).sha256 == K2.EMPREINTE_TEXTE_V2


@pytest.mark.parametrize("cle", [K2.CLE_SCELLEMENT_V2, K2.CLE_GO_V2, K2.CLE_CODE_V2])
def test_artefact_une_ligne_de_la_v2_absente_refus(tmp_path, cle):
    with pytest.raises(Refus, match=f"{cle} absente"):
        nl.exiger_registre_v2(J.monde(tmp_path, sans=(cle,)))


def test_artefact_scellement_qui_cite_un_autre_texte_refus(tmp_path):
    autre = (K2.CLE_SCELLEMENT_V2, H["scellement_v2"], K2.TEXTE_V2, "0" * 64)
    with pytest.raises(Refus, match="ne cite pas le texte scellé"):
        nl.exiger_registre_v2(J.monde(tmp_path, remplace={K2.CLE_SCELLEMENT_V2: autre}))


def test_abandon_ou_non_lues_inscrite_rien_ne_part(tmp_path):
    for i, cle in enumerate((K2.CLE_ABANDON_V2, K2.CLE_NON_LUES)):
        with pytest.raises(Refus, match=cle):
            nl.exiger_registre_v2(J.monde(tmp_path / str(i), plus=((cle, H["noeud"], "docs/x.md", "2" * 64),)))


def test_ouverture_de_la_premiere_passe_avant_le_scellement_de_la_v2_refus_et_apres_permis(tmp_path):
    avant = (K2.CLE_OUVERTURE_V1, "2026-11-20T09:00:00Z", "docs/x.md", "2" * 64)
    with pytest.raises(Refus, match="exposée à la première"):
        nl.exiger_registre_v2(J.monde(tmp_path / "a", plus=(avant,)))
    apres = (K2.CLE_OUVERTURE_V1, H["noeud"], "docs/x.md", "2" * 64)
    assert nl.exiger_registre_v2(J.monde(tmp_path / "b", plus=("entrees_v1", "tables_v1", apres)))


def test_ouverture_d_une_table_par_le_code_avant_le_scellement_refus_apres_permise(tmp_path):
    with pytest.raises(Refus, match="ouverture d'une table par le code avant"):
        nl.exiger_ouverture_permise_des_tables(J.monde(tmp_path / "a", sans=(K2.CLE_SCELLEMENT_V2,)))
    nl.exiger_ouverture_permise_des_tables(J.monde(tmp_path / "b"))
    abandon = (K2.CLE_ABANDON_V2, H["noeud"], "docs/x.md", "2" * 64)
    nl.exiger_ouverture_permise_des_tables(J.monde(tmp_path / "c", sans=(K2.CLE_SCELLEMENT_V2,), plus=(abandon,)))


def test_la_cle_retiree_de_l_addendum_de_recopie_n_est_ni_lue_ni_exigee():
    assert K2.CLE_RETIREE_ADDENDUM_DE_RECOPIE not in nl.CLES_LUES and K2.CLE_RETIREE_ADDENDUM_DE_RECOPIE not in K2.CLES_V2


# --- ligne de l'addendum de concentration (registre jouet) -------------------------------------------------------------------------------
def test_addendum_present_d_une_ligne_de_l_empreinte_citee_anterieur_aux_cles_de_la_v2_accepte(tmp_path):
    assert nl.exiger_registre_v2(J.monde(tmp_path)).derniere(K2.CLE_ADDENDUM).sha256 == K2.EMPREINTE_ADDENDUM


def test_addendum_artefacts_refus(tmp_path):
    saine = (K2.CLE_ADDENDUM, H["addendum"], K2.ADDENDUM, K2.EMPREINTE_ADDENDUM)
    cas = {"absente": dict(sans=(K2.CLE_ADDENDUM,)),
           "en plusieurs lignes": dict(plus=(saine,)),
           "d'un autre chemin ou d'une autre empreinte": dict(remplace={K2.CLE_ADDENDUM: saine[:3] + ("0" * 64,)}),
           "postérieure à une ligne": dict(sans=(K2.CLE_ADDENDUM,), plus=((K2.CLE_ADDENDUM, H["noeud"], K2.ADDENDUM, K2.EMPREINTE_ADDENDUM),)),
           "postérieure à une ligne d'une clé de la v2": dict(remplace={K2.CLE_ADDENDUM: (K2.CLE_ADDENDUM, "2026-11-20T10:39:18Z") + saine[2:]})}
    for i, (motif, plus) in enumerate(cas.items()):
        with pytest.raises(Refus, match=motif.split(" d'une clé")[0]):
            nl.exiger_registre_v2(J.monde(tmp_path / str(i), **plus))


# --- première passe lancée et non achevée (registre jouet) -------------------------------------------------------------------------------
def test_etat_de_la_premiere_passe_lu_au_registre(tmp_path):
    assert nl.exiger_registre_v2(J.monde(tmp_path / "a")).premiere_passe == nl.PREMIERE_PASSE_JAMAIS_LANCEE
    assert nl.exiger_registre_v2(J.monde(tmp_path / "b", plus=("entrees_v1", "tables_v1"))).premiere_passe == nl.PREMIERE_PASSE_ACHEVEE
    assert nl.exiger_registre_v2(J.monde(tmp_path / "c", plus=("entrees_v1",))).premiere_passe == nl.PREMIERE_PASSE_NON_ACHEVEE


def test_artefact_ligne_des_tables_sans_ligne_des_entrees_arret_forme_mal_comprise(tmp_path):
    with pytest.raises(FormeMalComprise, match="TABLES-LENTILLES-BBIS inscrite au registre propre sans ENTREES-LENTILLES-BBIS"):
        nl.exiger_registre_v2(J.monde(tmp_path, plus=("tables_v1",)))


# === issue des nœuds N12 et N17 ============================================================================================================
def test_sain_piece_qui_recopie_les_deux_issues_avec_une_ligne_d_accord_anterieure(tmp_path):
    etat = nl.exiger_registre_v2(J.monde(tmp_path))
    issue = nl.exiger_issue_des_noeuds(tmp_path, etat)
    assert issue["phrases_de_tete"] == [] and set(issue["recopiees"]) == {"N12", "N17"}
    assert issue["recopiees"]["N12"] == {"ligne_d_accord": "GO-2026-11-20-18", "heure": H["accord"]}


def test_la_forme_du_code_accepte_les_deux_lignes_de_la_piece_inscrite():
    """Les deux lignes relevées, par recherche de « N12 : » et « N17 : », dans la pièce que nomme la ligne inscrite."""
    piece = ("N12 : option (a) ; ligne d'accord GO-2026-11-20-18, 2026-11-20T05:34:13Z\n\n"
             "N17 : option (a) au premier palier ; option (a) au deuxième palier ; ligne d'accord GO-2026-11-20-18, 2026-11-20T05:34:13Z\n")
    assert nl.controler_issue_des_noeuds(piece, "2026-11-20T10:39:17Z")["phrases_de_tete"] == []


ARTEFACTS_NOEUDS = {
    "ligne d'accord datée après le scellement": (J.N12_SAINE.replace(H["accord"], "2026-11-20T10:39:18Z"), "strictement antérieure"),
    "ligne d'accord de la même seconde": (J.N12_SAINE.replace(H["accord"], H["scellement_v2"]), "strictement antérieure"),
    "heure absente": (J.N12_SAINE.rsplit(",", 1)[0], "nœud N12"),
    "heure illisible": (J.N12_SAINE.replace(H["accord"], "le 20 novembre au matin"), "nœud N12"),
    "N12 option (b)": (J.N12_SAINE.replace("option (a)", "option (b)"), "une autre issue"),
    "N12 option (c)": (J.N12_SAINE.replace("option (a)", "option (c)"), "une autre issue"),
    "N17 option (b) au deuxième palier": (J.N17_SAINE.replace("option (a) au deuxième", "option (b) au deuxième"), "une autre issue"),
    "N17 option (b) au premier palier": (J.N17_SAINE.replace("option (a) au premier", "option (b) au premier"), "une autre issue"),
    "ligne d'une autre forme": ("N12 : retenu (a), voir GO-2026-11-20-18", "autre forme"),
}


@pytest.mark.parametrize("cas", sorted(ARTEFACTS_NOEUDS))
def test_artefacts_de_l_issue_des_noeuds_chacun_un_arret_nomme(tmp_path, cas):
    ligne, motif = ARTEFACTS_NOEUDS[cas]
    saine = J.N17_SAINE if ligne.startswith("N12") else J.N12_SAINE
    etat = nl.exiger_registre_v2(J.monde(tmp_path, piece_go=f"# Pièce\n\n{ligne}\n\n{saine}\n"))
    with pytest.raises(Arret, match=nl.MESSAGE_ISSUE_DES_NOEUDS) as e:
        nl.exiger_issue_des_noeuds(tmp_path, etat)
    assert motif in str(e.value)


@pytest.mark.parametrize("muette_sur", ["N12", "N17"])
def test_piece_muette_sur_un_noeud_aucun_arret_la_phrase_est_rendue_pour_la_tete(tmp_path, muette_sur):
    """Artefact visé : un code qui se tait. La phrase « Issue du nœud […] : non recopiée […] » doit sortir."""
    garde = J.N17_SAINE if muette_sur == "N12" else J.N12_SAINE
    etat = nl.exiger_registre_v2(J.monde(tmp_path, piece_go=f"# Pièce qui parle du nœud {muette_sur} sans le recopier\n\n{garde}\n"))
    issue = nl.exiger_issue_des_noeuds(tmp_path, etat)
    assert issue["phrases_de_tete"] == [f"Issue du nœud {muette_sur} : non recopiée par la pièce de `GO-LENTILLES-BBIS-V2` ; celle "
                                        "du texte scellé vaut."]


def test_piece_du_go_d_une_autre_empreinte_que_sa_ligne_arret(tmp_path):
    etat = nl.exiger_registre_v2(J.monde(tmp_path))
    J.ecrire(tmp_path, J.PIECE_GO, "N12 : option (b)\n")
    with pytest.raises(Arret, match="autre empreinte que celle de sa ligne"):
        nl.exiger_issue_des_noeuds(tmp_path, etat)


# === fiche de rangement =====================================================================================================================
def _fiche(tmp_path, fiche=None, **plus):
    etat = nl.exiger_registre_v2(J.monde(tmp_path, fiche, **plus))
    return nl.lire_fiche(tmp_path, etat), etat


def test_sain_fiche_lue_sur_l_empreinte_de_sa_ligne(tmp_path):
    fiche, _ = _fiche(tmp_path)
    assert fiche["lentilles"]["R"]["verdict_identite"] == K2.PALIER_1


def test_artefact_ligne_de_rangement_absente_rien_ne_part(tmp_path):
    with pytest.raises(Refus, match="RANGEMENT-NOS-LENTILLES-BBIS absente"):
        _fiche(tmp_path, sans=(K2.CLE_RANGEMENT,))


def test_artefact_fiche_alteree_d_un_octet_arret(tmp_path):
    etat = nl.exiger_registre_v2(J.monde(tmp_path))
    p = tmp_path / J.FICHE
    o = bytearray(p.read_bytes())
    o[10] ^= 1
    p.write_bytes(bytes(o))
    with pytest.raises(Refus, match="autre empreinte que celle de sa ligne"):
        nl.lire_fiche(tmp_path, etat)


@pytest.mark.parametrize("revision", [None, "0123456789abcdef", "0123456789ABCDEF0123456789abcdef01234567"])
def test_artefact_revision_absente_ou_courte_arret(tmp_path, revision):
    with pytest.raises(Refus, match="révision absente ou courte"):
        _fiche(tmp_path, J.fiche(r=J.lentille("R", revision=revision)))


def test_artefact_deux_sha256_differents_dans_la_fiche_arret(tmp_path):
    with pytest.raises(Refus, match="les deux SHA-256"):
        _fiche(tmp_path, J.fiche(s=J.lentille("S", sha256_avant_envoi="f" * 64)))


def test_artefact_verdict_absent_pour_les_deux_lentilles_rien_ne_part(tmp_path):
    with pytest.raises(Refus, match="sans verdict d'identité pour aucune"):
        _fiche(tmp_path, J.fiche(r=J.lentille("R", verdict=None), s=J.lentille("S", verdict=None)))


def test_verdict_absent_pour_une_seule_lentille_celle_la_non_lue_l_autre_lue(tmp_path):
    c = J.condition(tmp_path, J.fiche(s=J.lentille("S", verdict=None)))
    assert c["R"].lue and not c["S"].lue
    assert c["S"].motif == "Non lue : notre lentille S sans verdict d'identité dans la fiche de rangement"


def test_plusieurs_lignes_de_rangement_la_derniere_designe_la_fiche(tmp_path):
    registre = J.monde(tmp_path)
    neuve = J.ecrire(tmp_path, "docs/fiche-v2.json", json.dumps(J.fiche(r=J.lentille("R", verdict=K2.DIFFERENTE))))
    with open(registre, "a", encoding="utf-8") as f:
        f.write(f"| {K2.CLE_RANGEMENT} | {H['noeud']} | docs/fiche-v2.json | {neuve} |\n")
    etat = nl.exiger_registre_v2(registre)
    assert nl.lire_fiche(tmp_path, etat)["lentilles"]["R"]["verdict_identite"] == K2.DIFFERENTE


# === condition de lecture, un cas par mention ===============================================================================================
def test_premier_palier_avec_audit_lue(tmp_path):
    c = J.condition(tmp_path, J.fiche())
    assert c["R"].lue and c["S"].lue and c["R"].palier == 1 and c["R"].motif is None and c["course"] == nl.COURSE_AJUSTEMENT_SEUL
    assert all(c["R"].lue_a(couche) for couche in K.COUCHES)


@pytest.mark.parametrize("audit", [None, {"chemin": "docs/a.md", "sha256": "court"}, dict(J.AUDIT, controles_manques=1)])
def test_premier_palier_sans_audit_non_lue(tmp_path, audit):
    c = J.condition(tmp_path, J.fiche(r=J.lentille("R", audit=audit)))
    assert not c["R"].lue and c["R"].motif == "Non lue : notre lentille R au premier palier sans audit versé"
    assert c["S"].lue


def test_premier_palier_avec_une_empreinte_autre_que_celle_du_18_novembre_arret(tmp_path):
    autre = "f" * 64
    with pytest.raises(Arret, match="empreinte autre que celle du 18 novembre"):
        J.condition(tmp_path, J.fiche(r=J.lentille("R", sha256_avant_envoi=autre, sha256_relecture=autre)))


def test_premier_palier_suivi_de_reprise_sur_sauvegarde_notee_lu_comme_le_premier_palier(tmp_path):
    c = J.condition(tmp_path, J.fiche(r=J.lentille("R", verdict=K2.PALIER_1 + " ; reprise sur sauvegarde notée")))
    assert c["R"].lue and c["R"].palier == 1 and c["R"].reprise is True


@pytest.mark.parametrize("verdict", [K2.PALIER_1 + " ; reprise", K2.PALIER_1 + " ; à l'octet près", "palier 3 — autre", "équivalente"])
def test_un_autre_ajout_au_libelle_ou_un_libelle_inconnu_arret_forme_mal_comprise(tmp_path, verdict):
    with pytest.raises(FormeMalComprise, match="libellé inconnu"):
        J.condition(tmp_path, J.fiche(r=J.lentille("R", verdict=verdict)))


def _palier_2(lettre="R", **plus):
    return J.lentille(lettre, verdict=K2.PALIER_2, **plus)


def _rejouee(r=None, s=None, seconde_course=K2.SECONDE_COURSE_ENTIERE):
    return J.fiche(r=r, s=s, variante=K2.VARIANTE_COURSE_REJOUEE, seconde_course=seconde_course)


def test_deuxieme_palier_course_rejouee_les_deux_lignes_presentes_lue(tmp_path):
    c = J.condition(tmp_path, _rejouee(r=_palier_2()), plus=("avertissement", "lecture_seconde_course"))
    assert c["R"].lue and c["R"].palier == 2 and c["R"].mesures_refaites is True and not c["R"].phrase_sans_mesure
    assert c["course"] == nl.COURSE_REJOUEE and c["R"].couches[7]["limite"] == K2.AUCUNE_LIMITE


def test_deuxieme_palier_course_rejouee_sans_la_ligne_d_avertissement_non_lue(tmp_path):
    c = J.condition(tmp_path, _rejouee(r=_palier_2()), plus=("lecture_seconde_course",))
    assert not c["R"].lue and "sans la ligne AVERTISSEMENT-PALIER-2-LENTILLES-BBIS" in c["R"].motif


def test_deuxieme_palier_course_rejouee_sans_la_ligne_de_la_lecture_de_la_seconde_course_non_lue(tmp_path):
    c = J.condition(tmp_path, _rejouee(r=_palier_2()), plus=("avertissement",))
    assert not c["R"].lue and "sans la ligne LECTURE-SECONDE-COURSE-NOS-LENTILLES-BBIS" in c["R"].motif


def test_deuxieme_palier_ajustement_seul_sans_la_ligne_du_mot_de_lazar_non_lue(tmp_path):
    c = J.condition(tmp_path, J.fiche(r=_palier_2()), plus=("avertissement",))
    assert not c["R"].lue
    assert c["R"].motif == ("Non lue : notre lentille R au deuxième palier, sans mesure propre ; aucune lecture sans nœud de Lazar")


def test_deuxieme_palier_ajustement_seul_avec_la_ligne_du_mot_de_lazar_lue_phrase_n_ont_pas_ete_refaites(tmp_path):
    c = J.condition(tmp_path, J.fiche(r=_palier_2()), plus=("avertissement", J.ligne_du_noeud(tmp_path)))
    assert c["R"].lue and c["R"].mesures_refaites is False and c["R"].phrase_sans_mesure is True
    assert nl.PHRASE_SANS_MESURE.startswith("Cette lentille n'a pour mesure à elle que la différence entre moitiés")


@pytest.mark.parametrize("verdict, motif", [(K2.DIFFERENTE, "au verdict d'identité « différente »"),
                                            (K2.NON_COMPARABLE, "au verdict d'identité « non comparable (traitée comme différente) »"),
                                            (K2.SUSPENDUE, "au verdict d'identité « mention suspendue : anomalie (nœud de Lazar) »"),
                                            ("R non réajustée", "absente")])
def test_autres_mentions_non_lue_l_autre_lue_motif_ecrit(tmp_path, verdict, motif):
    c = J.condition(tmp_path, J.fiche(r=J.lentille("R", verdict=verdict)))
    assert not c["R"].lue and c["R"].motif == f"Non lue : notre lentille R {motif}" and c["S"].lue


def test_non_reajustee_de_l_autre_lettre_forme_mal_comprise(tmp_path):
    with pytest.raises(FormeMalComprise):
        J.condition(tmp_path, J.fiche(r=J.lentille("R", verdict="S non réajustée")))


def test_critere_non_scelle_a_l_empreinte_citee_ou_verdict_non_scelle_non_lue(tmp_path):
    f = J.fiche(critere_identite={"chemin": K2.CRITERE_IDENTITE, "sha256": "0" * 64})
    c = J.condition(tmp_path / "a", f)
    assert not c["R"].lue and not c["S"].lue and "critère d'identité" in c["R"].motif
    c = J.condition(tmp_path / "b", J.fiche(s=J.lentille("S", verdict_scelle=None)))
    assert c["R"].lue and c["S"].motif == "Non lue : notre lentille S dont le verdict d'identité n'est pas scellé"


# --- stabilité par couche --------------------------------------------------------------------------------------------------------------------
@pytest.mark.parametrize("valeur, lue", [(0.10, True), (0.1001, False)])
@pytest.mark.parametrize("ajustement", ["ajustement_du_18_novembre", "reajustement"])
def test_couche_non_stable_dans_l_un_des_deux_ajustements_bord(tmp_path, valeur, lue, ajustement):
    diffs = {"ajustement_du_18_novembre": {"7": 0.05, "15": 0.03, "23": 0.01}, "reajustement": {"7": 0.05, "15": 0.03, "23": 0.01}}
    diffs[ajustement]["15"] = valeur
    c = J.condition(tmp_path, J.fiche(r=J.lentille("R", diffs_out=diffs)))
    assert c["R"].lue and c["R"].lue_a(7) and c["R"].lue_a(23) and c["R"].lue_a(15) is lue
    if not lue:
        assert c["R"].couches[15]["motif"] == "Non lue à la couche 15 : stabilité non tenue dans les deux ajustements"


def test_valeur_de_stabilite_absente_de_la_fiche_lentille_non_lue_a_cette_couche(tmp_path):
    diffs = {"ajustement_du_18_novembre": {"7": 0.05, "15": 0.03}, "reajustement": {"7": 0.05, "15": 0.03, "23": 0.01}}
    c = J.condition(tmp_path, J.fiche(r=J.lentille("R", diffs_out=diffs)))
    assert c["R"].lue_a(7) and not c["R"].lue_a(23) and "absente de la fiche" in c["R"].couches[23]["motif"]


def test_couche_ecartee_par_la_lecture_de_la_seconde_course_non_lue_a_cette_couche(tmp_path):
    limites = {"7": {"limite": "couche 7 écartée : garde (n) non tenue", "ecartee": True},
               "15": {"limite": "lue sous réserve de la marge", "ecartee": False}, "23": {"limite": K2.AUCUNE_LIMITE, "ecartee": False}}
    c = J.condition(tmp_path, _rejouee(r=_palier_2(seconde_course_par_couche=limites)), plus=("avertissement", "lecture_seconde_course"))
    assert c["R"].lue and not c["R"].lue_a(7) and c["R"].lue_a(15)
    assert c["R"].couches[7]["motif"] == "Non lue à la couche 7 : couche 7 écartée : garde (n) non tenue"
    assert c["R"].couches[15]["limite"] == "lue sous réserve de la marge"


# --- seconde course incomplète, fiche muette, audit au deuxième palier -----------------------------------------------------------------------
def test_seconde_course_incomplete_sans_la_ligne_du_mot_de_lazar_non_lue_et_avec_elle_lue(tmp_path):
    f = _rejouee(r=_palier_2(), seconde_course=K2.SECONDE_COURSE_INCOMPLETE)
    c = J.condition(tmp_path / "a", f, plus=("avertissement", "lecture_seconde_course"))
    assert not c["R"].lue and "sans mesure propre" in c["R"].motif and c["course"] == nl.COURSE_REJOUEE_INCOMPLETE
    c = J.condition(tmp_path / "b", f, plus=("avertissement", J.ligne_du_noeud(tmp_path / "b")))
    assert c["R"].lue and c["R"].mesures_refaites is False and c["R"].phrase_sans_mesure


@pytest.mark.parametrize("avec_le_mot_de_lazar", [False, True])
def test_fiche_muette_non_lue_sous_son_motif_propre_avec_la_ligne_du_mot_de_lazar_comme_sans_elle(tmp_path, avec_le_mot_de_lazar):
    """Artefact visé : un code qui lit la fiche muette comme incomplète et ouvre la voie du mot de Lazar."""
    plus = ("avertissement", "lecture_seconde_course") + ((J.ligne_du_noeud(tmp_path),) if avec_le_mot_de_lazar else ())
    c = J.condition(tmp_path, _rejouee(r=_palier_2(), seconde_course=None), plus=plus)
    assert not c["R"].lue and c["course"] == "course rejouée, achèvement de la seconde course non dit par la fiche"
    assert c["R"].motif == ("Non lue : notre lentille R au deuxième palier, fiche muette sur l'achèvement de la seconde course ; "
                            "aucune lecture sans nœud de Lazar")
    assert "sans mesure propre" not in c["R"].motif


def test_fiches_qui_disent_menee_en_entier_ou_incomplete_chacune_selon_sa_regle(tmp_path):
    plus = ("avertissement", "lecture_seconde_course")
    assert J.condition(tmp_path / "a", _rejouee(r=_palier_2()), plus=plus)["R"].lue
    assert not J.condition(tmp_path / "b", _rejouee(r=_palier_2(), seconde_course=K2.SECONDE_COURSE_INCOMPLETE), plus=plus)["R"].lue
    with pytest.raises(FormeMalComprise, match="achèvement de la seconde course"):
        J.condition(tmp_path / "c", _rejouee(r=_palier_2(), seconde_course="presque"), plus=plus)
    with pytest.raises(FormeMalComprise, match="variante de la course"):
        J.condition(tmp_path / "d", J.fiche(variante="autre"))


def test_deuxieme_palier_avec_un_declencheur_rendu_sans_audit_non_lue_avec_audit_lue_sans_declencheur_ni_audit_lue(tmp_path):
    plus = ("avertissement", "lecture_seconde_course")
    ii = ["(ii) écart maximal exactement nul avec des octets différents"]
    c = J.condition(tmp_path / "a", _rejouee(s=_palier_2("S", declencheurs=ii, audit=None)), plus=plus)
    assert not c["S"].lue and c["S"].audit_du and "audit est dû" in c["S"].motif
    assert J.condition(tmp_path / "b", _rejouee(s=_palier_2("S", declencheurs=ii)), plus=plus)["S"].lue
    c = J.condition(tmp_path / "c", _rejouee(s=_palier_2("S", audit=None)), plus=plus)
    assert c["S"].lue and not c["S"].audit_du


def test_chiffres_du_deuxieme_palier_absents_de_la_fiche_arret(tmp_path):
    sortie = J.sortie_du_programme("R")
    del sortie["ecart_max_abs_diffs_float64"]
    with pytest.raises(FormeMalComprise, match="crochets obligatoires"):
        J.condition(tmp_path, J.fiche(r=_palier_2(sortie_du_programme=sortie)), plus=("avertissement",))


# --- règle de N12 ------------------------------------------------------------------------------------------------------------------------------
@pytest.mark.parametrize("fiche", [J.fiche(r=_palier_2()), _rejouee(r=_palier_2(), seconde_course=K2.SECONDE_COURSE_INCOMPLETE)],
                         ids=["ajustement seul", "seconde course incomplète"])
def test_regle_de_n12_lue_avec_la_ligne_posterieure_a_l_avertissement_non_lue_autrement(tmp_path, fiche):
    """Artefact visé : un code qui lit sur le seul avertissement, ou sur une ligne antérieure à l'avertissement."""
    assert J.condition(tmp_path / "a", fiche, plus=("avertissement", J.ligne_du_noeud(tmp_path / "a")))["R"].lue
    assert not J.condition(tmp_path / "b", fiche, plus=())["R"].lue                              # sans rien
    assert not J.condition(tmp_path / "c", fiche, plus=("avertissement",))["R"].lue              # le seul avertissement
    anterieure = J.ligne_du_noeud(tmp_path / "d", heure="2026-11-22T09:30:00Z")
    assert not J.condition(tmp_path / "d", fiche, plus=(anterieure, "avertissement"))["R"].lue   # ligne antérieure à l'avertissement
    meme_seconde = J.ligne_du_noeud(tmp_path / "e", heure=H["avertissement"])
    assert not J.condition(tmp_path / "e", fiche, plus=("avertissement", meme_seconde))["R"].lue


def test_regle_de_n12_le_mot_n_ouvre_que_la_lentille_qu_il_nomme(tmp_path):
    f = J.fiche(r=_palier_2(), s=_palier_2("S"))
    c = J.condition(tmp_path / "a", f, plus=("avertissement", J.ligne_du_noeud(tmp_path / "a", "S")))
    assert c["S"].lue and not c["R"].lue
    c = J.condition(tmp_path / "b", f, plus=("avertissement", J.ligne_du_noeud(tmp_path / "b", "R et S")))
    assert c["S"].lue and c["R"].lue
    sans_nom = (K2.CLE_NOEUD_AJUSTEMENT_SEUL, H["noeud"], "docs/mot.md", J.ecrire(tmp_path / "c", "docs/mot.md", "go\n"))
    c = J.condition(tmp_path / "c", f, plus=("avertissement", sans_nom))
    assert not c["S"].lue and not c["R"].lue


# --- règle de N17 ------------------------------------------------------------------------------------------------------------------------------
def test_regle_de_n17_aucune_ligne_d_addendum_de_recopie_n_est_exigee_a_aucun_palier(tmp_path):
    """Lentille au deuxième palier lue sans elle (cas sain) ; artefact visé : un code qui l'exige, ou qui écrit un motif
    « addendum de recopie […] absent »."""
    c = J.condition(tmp_path, _rejouee(r=_palier_2(), s=J.lentille("S")), plus=("avertissement", "lecture_seconde_course"))
    assert c["R"].lue and c["S"].lue
    motifs = [getattr(nl, n) for n in dir(nl) if n.startswith("MOTIF_")]
    assert not any("addendum de recopie" in m for m in motifs)


# --- étiquettes du programme ---------------------------------------------------------------------------------------------------------------------
def test_etiquette_du_programme_la_version_du_critere_reste_la_version_8(tmp_path):
    """Sortie jouet dont le champ `critere` nomme la version 5 : il n'est ni lu ni recopié. Artefact visé : un code qui le
    recopie."""
    c = J.condition(tmp_path, J.fiche())
    assert "critere" not in c["R"].chiffres and "v5" not in json.dumps(c["R"].table(), ensure_ascii=False)
    assert K2.VERSION_CRITERE_IDENTITE == 8 and K2.CRITERE_IDENTITE.endswith("critere-identite-reajustement-lentilles-v8.md")


# === phrase du déclencheur (vi) =============================================================================================================
VI = ["(vi) trop propre au deuxième palier : 31 matrices égales ou série inchangée à zéro exact"]
D_, F_ = nl.VI_DEBUT, nl.VI_FIN
F1 = "31 matrices des moitiés égales sur 31"
F2 = "série des écarts à la lentille publique inchangée"
F3 = "séries des écarts à la lentille publique et à l'identité inchangées"
FORMES_ADMISES = [F1, F2, F3, f"{F1} et {F2}", f"{F2} et {F1}", f"{F1} et {F3}", f"{F3} et {F1}"]


@pytest.mark.parametrize("milieu", FORMES_ADMISES)
@pytest.mark.parametrize("s", [None, "palier 2"], ids=["notre R seule", "nos deux lentilles"])
def test_phrase_vi_cas_sain_lue_dans_son_champ_dans_chacune_de_ses_formes_admises(tmp_path, milieu, s):
    phrase = D_ + milieu + F_
    r = _palier_2(declencheurs=VI, phrase_du_declencheur_vi=phrase)
    c = J.condition(tmp_path, _rejouee(r=r, s=_palier_2("S") if s else None), plus=("avertissement", "lecture_seconde_course"))
    assert c["R"].lue and c["R"].phrase_vi == phrase and c["S"].phrase_vi is None


def test_phrase_vi_cas_sain_deuxieme_palier_sans_declencheur_vi_champ_aucune_rien_n_est_ajoute(tmp_path):
    c = J.condition(tmp_path, _rejouee(r=_palier_2()), plus=("avertissement", "lecture_seconde_course"))
    assert c["R"].lue and c["R"].phrase_vi is None


def _arret_vi(tmp_path, r=None, s=None):
    with pytest.raises(FormeMalComprise, match=re.escape(nl.MESSAGE_PHRASE_VI)):
        J.condition(tmp_path, _rejouee(r=r, s=s), plus=("avertissement", "lecture_seconde_course"))


def test_phrase_vi_artefacts_de_place_chacun_un_arret(tmp_path):
    saine = D_ + F1 + F_
    sans_champ = _palier_2(declencheurs=VI)
    del sans_champ["phrase_du_declencheur_vi"]
    _arret_vi(tmp_path / "champ-absent", r=sans_champ)
    _arret_vi(tmp_path / "aucune-alors-que-vi", r=_palier_2(declencheurs=VI))
    _arret_vi(tmp_path / "phrase-sans-vi", r=_palier_2(phrase_du_declencheur_vi=saine))
    _arret_vi(tmp_path / "pour-notre-s", s=_palier_2("S", declencheurs=VI, phrase_du_declencheur_vi=saine))
    _arret_vi(tmp_path / "premier-palier", r=J.lentille("R", phrase_du_declencheur_vi=saine))
    _arret_vi(tmp_path / "audit-avec-controle-manque",
              r=_palier_2(declencheurs=VI, phrase_du_declencheur_vi=saine, audit=dict(J.AUDIT, controles_manques=2)))


AUTRES_FORMES = {
    "début changé d'un mot": "pour notre R, " + F1 + F_,
    "milieu changé d'un mot": D_ + "31 matrices des moitiés identiques sur 31" + F_,
    "fin changée d'un mot": D_ + F1 + " malgré des octets d'ajustement différents ; audit sans contrôle raté",
    "jointes par un autre mot que et": D_ + F1 + " ou " + F2 + F_,
    "jointes par une virgule": D_ + F2 + ", " + F1 + F_,
    "la même forme deux fois (1)": D_ + F1 + " et " + F1 + F_,
    "la même forme deux fois (2)": D_ + F2 + " et " + F2 + F_,
    "formes (2) et (3) jointes": D_ + F2 + " et " + F3 + F_,
    "série au singulier, inchangées au pluriel": D_ + "série des écarts inchangées" + F_,
    "rien entre les deux": D_.rstrip() + F_,
}


@pytest.mark.parametrize("cas", sorted(AUTRES_FORMES))
def test_phrase_vi_d_une_autre_forme_arret_forme_mal_comprise(tmp_path, cas):
    assert not nl.forme_de_la_phrase_vi(AUTRES_FORMES[cas])
    _arret_vi(tmp_path, r=_palier_2(declencheurs=VI, phrase_du_declencheur_vi=AUTRES_FORMES[cas]))


# === accès ====================================================================================================================================
def _url(l):
    return mo.url_fichier(l["depot"], l["revision"], l["chemin"])


def test_essai_d_un_octet_de_nos_fichiers_avec_la_cle_a_la_revision_de_la_fiche(tmp_path):
    l = J.lentille("R")
    cible = nl.cible_un_octet("R", l)
    assert l["revision"] in cible.url and cible.avec_cle
    t = J.TransportJouet({cible.url: b"PK\x03\x04"})
    assert mo.essais_un_octet(t, mo.Cle("fausse-cle"), [cible])[0]["tenu"]
    assert t.demandes == [("octets", cible.url, True)]


def test_essai_d_un_octet_refuse_arret_aucun_autre_fichier_tente(tmp_path):
    r, s = nl.cible_un_octet("R", J.lentille("R")), nl.cible_un_octet("S", J.lentille("S"))
    t = J.TransportJouet({s.url: b"PK"}, refus=(r.url,))
    with pytest.raises(Arret, match="essai d'un octet refusé"):
        mo.essais_un_octet(t, mo.Cle("fausse-cle"), [r, s])
    assert [d[1] for d in t.demandes] == [r.url]


def test_fichier_introuvable_a_la_revision_arret_aucun_repli(tmp_path):
    l = J.lentille("R")
    octets = J.ecrire_ajustement(tmp_path / "r.pt", "R")
    autre_revision = mo.url_fichier(l["depot"], "f" * 40, l["chemin"])
    t = J.TransportJouet({autre_revision: octets, _url(l).replace("r-llama", "export-r"): octets})
    with pytest.raises(mo.RefusReseau):
        nl.lire_ajustement_en_flux(t, _url(l), mo.Cle("fausse-cle"), J.attendu("R"), tmp_path / "m", len(octets), J.sha(octets), reprises=0)
    assert {d[1] for d in t.demandes} == {_url(l)} and not list((tmp_path / "m").glob("*"))


# === archive ==================================================================================================================================
@pytest.mark.parametrize("lettre", ["R", "S"])
@pytest.mark.parametrize("bloc", [1, 64, 997, 10 ** 6])
def test_extraction_en_flux_egale_au_chargement_entier(tmp_path, lettre, bloc):
    """Faux fichier d'ajustement écrit par `torch.save` (petites dimensions, mêmes clés) : les matrices extraites en flux
    égalent, à l'octet, celles du chargement entier, et la matrice lue est (S₀ + S₁) / (n₀ + n₁)."""
    octets = J.ecrire_ajustement(tmp_path / "f.pt", lettre)
    d = J.extraire(octets, lettre, tmp_path / "m", bloc=bloc)
    entier = torch.load(tmp_path / "f.pt", weights_only=True)
    lentille = nl.charger_notre_lentille(tmp_path / "m", d)
    for couche in J.COUCHES_JOUET:
        for h in (0, 1):
            assert np.array_equal(lentille.sommes[couche][h], entier["state"]["sums"][("out", h)][couche].numpy())
        s = entier["state"]["sums"]
        assert np.array_equal(lentille.matrice(couche), ((s[("out", 0)][couche] + s[("out", 1)][couche]) / 6).numpy())
        assert np.array_equal(lentille.matrice(couche, 1), (s[("out", 1)][couche] / 3).numpy())
    assert d["n_docs"] == [3, 3] and d["next_doc"] == 6 and d["meta"]["lens"] == lettre
    assert sorted(p.name for p in (tmp_path / "m").iterdir()) == sorted(d["fichiers"].values()) and len(d["fichiers"]) == 6
    assert d["enregistrements"][0]["nom"].endswith("data.pkl")


def test_lecture_en_flux_par_le_transport_reprise_comprise(tmp_path):
    l = J.lentille("S")
    octets = J.ecrire_ajustement(tmp_path / "s.pt", "S")
    t = J.TransportJouet({_url(l): octets})
    d = nl.lire_ajustement_en_flux(t, _url(l), mo.Cle("fausse-cle"), J.attendu("S"), tmp_path / "m", len(octets), J.sha(octets))
    assert d["sha256"] == J.sha(octets) and d["taille"] == len(octets) and t.demandes == [("flux", _url(l), True)]


def test_artefact_un_octet_change_arret_sur_l_empreinte_aucune_matrice_gardee(tmp_path):
    octets = bytearray(J.ecrire_ajustement(tmp_path / "f.pt", "R"))
    saine = J.sha(bytes(octets))
    octets[len(octets) // 2] ^= 1
    ex = nl.ExtracteurAjustement(J.attendu("R"), tmp_path / "m")
    ex.recevoir(bytes(octets))
    with pytest.raises(Arret, match="SHA-256 ou taille calculés sur le flux différents de la fiche"):
        ex.conclure(len(octets), saine)
    assert not list((tmp_path / "m").iterdir())


def test_artefact_premier_palier_empreinte_du_flux_differente_de_celle_du_18_novembre_arret(tmp_path):
    octets = J.ecrire_ajustement(tmp_path / "f.pt", "R")
    ex = nl.ExtracteurAjustement(J.attendu("R"), tmp_path / "m")
    ex.recevoir(octets)
    with pytest.raises(Arret, match="différent de l'empreinte du 18 novembre"):
        ex.conclure(len(octets), J.sha(octets), K2.EMPREINTE_18_NOVEMBRE["R"])


@pytest.mark.parametrize("octets", [b"ceci n'est pas une archive, mais un texte assez long pour un en-tete", b"PK\x05\x06" + bytes(18)])
def test_artefact_archive_illisible_arret(tmp_path, octets):
    with pytest.raises(Arret, match="archive illisible"):
        J.extraire(octets, "R", tmp_path / "m")


def test_artefact_archive_tronquee_arret(tmp_path):
    octets = J.ecrire_ajustement(tmp_path / "f.pt", "R")[:3000]
    with pytest.raises(Arret, match="archive illisible"):
        J.extraire(octets, "R", tmp_path / "m")


def _rezipper(source, compression=zipfile.ZIP_STORED, premier: str | None = None) -> bytes:
    """Réécrit l'archive avec `zipfile` (autre ordre ou compression) : artefacts de forme."""
    z = zipfile.ZipFile(source)
    noms = z.namelist()
    if premier:
        noms = [n for n in noms if n.endswith(premier)] + [n for n in noms if not n.endswith(premier)]
    tampon = io.BytesIO()
    with zipfile.ZipFile(tampon, "w", compression) as sortie:
        for n in noms:
            sortie.writestr(n, z.read(n))
    return tampon.getvalue()


def test_sain_archive_dont_l_en_tete_local_porte_les_tailles(tmp_path):
    """Autre écrivain (tailles dans l'en-tête local, sans descripteur) : même extraction."""
    J.ecrire_ajustement(tmp_path / "f.pt", "R")
    octets = _rezipper(tmp_path / "f.pt")
    d = J.extraire(octets, "R", tmp_path / "m")
    entier = torch.load(tmp_path / "f.pt", weights_only=True)
    assert np.array_equal(nl.charger_notre_lentille(tmp_path / "m", d).sommes[2][0], entier["state"]["sums"][("out", 0)][2].numpy())


def test_artefact_enregistrement_compresse_arret(tmp_path):
    J.ecrire_ajustement(tmp_path / "f.pt", "R")
    with pytest.raises(Arret, match="enregistrement compressé"):
        J.extraire(_rezipper(tmp_path / "f.pt", zipfile.ZIP_DEFLATED), "R", tmp_path / "m")


def test_artefact_data_pkl_qui_n_est_pas_le_premier_enregistrement_arret(tmp_path):
    J.ecrire_ajustement(tmp_path / "f.pt", "R")
    with pytest.raises(Arret, match="n'est pas le premier enregistrement"):
        J.extraire(_rezipper(tmp_path / "f.pt", premier="version"), "R", tmp_path / "m")


def test_artefact_tenseur_non_contigu_arret(tmp_path):
    sommes = J.sommes_jouet("R")
    sommes[("out", 0)] = sommes[("out", 0)].transpose(1, 2)
    with pytest.raises(Arret, match="non contigu"):
        J.extraire(J.ecrire_ajustement(tmp_path / "f.pt", "R", sommes), "R", tmp_path / "m")


def test_artefact_decalage_non_nul_inattendu_arret(tmp_path):
    sommes = J.sommes_jouet("R")
    grand = torch.cat([sommes[("out", 1)][:1], sommes[("out", 1)]])
    sommes[("out", 1)] = grand[1:]
    with pytest.raises(Arret, match="décalage non nul inattendu"):
        J.extraire(J.ecrire_ajustement(tmp_path / "f.pt", "R", sommes), "R", tmp_path / "m")


def test_artefact_data_pkl_qui_demande_une_classe_hors_de_la_liste_arret(tmp_path):
    octets = J.ecrire_ajustement(tmp_path / "f.pt", "R", meta=J.meta_jouet("R") | {"rules": complex(1, 2)})
    with pytest.raises(Arret, match="classe hors de la liste blanche"):
        J.extraire(octets, "R", tmp_path / "m")
    assert ("builtins", "complex") not in nl.CLASSES_PERMISES and ("collections", "OrderedDict") in nl.CLASSES_PERMISES


def test_artefact_forme_ou_precision_fausse_arret(tmp_path):
    octets = J.ecrire_ajustement(tmp_path / "f.pt", "R")
    with pytest.raises(Arret, match="forme de `sums"):
        J.extraire(octets, "R", tmp_path / "a", n_couches=5)
    sommes = {k: v.double() for k, v in J.sommes_jouet("R").items()}
    with pytest.raises(Arret, match="simple précision"):
        J.extraire(J.ecrire_ajustement(tmp_path / "g.pt", "R", sommes), "R", tmp_path / "b")


# --- `meta` et état -----------------------------------------------------------------------------------------------------------------------------
def _decrit(tmp_path, lettre="R", **plus):
    return J.extraire(J.ecrire_ajustement(tmp_path / f"{lettre}.pt", lettre, **plus), lettre, tmp_path / f"m{lettre}")


def test_sain_meta_et_etat_conformes(tmp_path):
    for lettre in ("R", "S"):
        r = nl.controler_meta_et_etat(_decrit(tmp_path, lettre), J.attendu(lettre))
        assert r["meta"]["lens"] == lettre and "rules" not in r["meta"] and r["n_docs"] == [3, 3]


def test_artefact_meta_de_s_chargee_comme_r_arret(tmp_path):
    with pytest.raises(Arret, match="`meta` différente de celle attendue"):
        nl.controler_meta_et_etat(_decrit(tmp_path, "S"), J.attendu("R", n_couches=5))


@pytest.mark.parametrize("champ, valeur", [("rows_sha256", "b7" * 32), ("docs", 931), ("dtype", "float16"), ("targets", ["out"])])
def test_artefact_un_champ_de_meta_faux_arret(tmp_path, champ, valeur):
    with pytest.raises(Arret, match=champ):
        nl.controler_meta_et_etat(_decrit(tmp_path, "R", meta=J.meta_jouet("R") | {champ: valeur}), J.attendu("R"))


@pytest.mark.parametrize("plus", [dict(n_docs=(3, 2)), dict(next_doc=5)])
def test_artefact_n_docs_ou_next_doc_faux_arret(tmp_path, plus):
    with pytest.raises(Arret, match="`n_docs` ou `next_doc`"):
        nl.controler_meta_et_etat(_decrit(tmp_path, "R", **plus), J.attendu("R"))


def test_meta_de_s_lue_dans_la_piece_du_18_novembre_champ_meta_seul(tmp_path):
    piece = {"fichier": "s.pt", "sha256": "0" * 64, "meta": J.meta_jouet("S"), "longueurs": [1, 2, 3]}
    s = J.ecrire(tmp_path, "piece-S.json", json.dumps(piece))
    meta = nl.meta_attendue_de_s(tmp_path / "piece-S.json", s)
    assert set(meta) == set(K2.CHAMPS_META) and meta["lens"] == "S" and meta["targets"] == ["mid", "out"]
    nl.controler_meta_et_etat(_decrit(tmp_path, "S"), J.attendu("S", meta=meta))


def test_artefact_piece_du_18_novembre_d_une_autre_empreinte_arret(tmp_path):
    J.ecrire(tmp_path, "piece-S.json", json.dumps({"meta": J.meta_jouet("S")}))
    with pytest.raises(Arret, match="autre empreinte que celle citée par le texte"):
        nl.meta_attendue_de_s(tmp_path / "piece-S.json")


def test_artefact_meta_de_s_differente_de_celle_de_la_piece_du_18_novembre_arret(tmp_path):
    s = J.ecrire(tmp_path, "piece-S.json", json.dumps({"meta": J.meta_jouet("S") | {"seq_len": 64}}))
    with pytest.raises(Arret, match="seq_len"):
        nl.controler_meta_et_etat(_decrit(tmp_path, "S"), J.attendu("S", meta=nl.meta_attendue_de_s(tmp_path / "piece-S.json", s)))


# --- matrices -----------------------------------------------------------------------------------------------------------------------------------
def _lentille(tmp_path, lettre="R", **plus):
    return nl.charger_notre_lentille(tmp_path / f"m{lettre}", _decrit(tmp_path, lettre, **plus))


def _publique(garde="publique"):
    return {c: (2 * np.eye(J.D) + J.rng(f"{garde}-{c}").standard_normal((J.D, J.D))).astype(np.float32) for c in J.COUCHES_JOUET}


def test_sain_controles_des_matrices_et_empreintes_relevees(tmp_path):
    r, s = _lentille(tmp_path, "R"), _lentille(tmp_path, "S")
    rapport = nl.controler_matrices(r, publique=_publique())
    assert len(rapport["empreintes_des_matrices_decodees"]) == 6 and set(rapport["couches"]) == {"1", "2", "3"}
    assert rapport["couches"]["2"]["ecart_relatif_a_la_lentille_publique"] > 1e-3
    rapport_s = nl.controler_matrices(s, notre_r=r)
    assert rapport_s["couches"]["2"]["ecart_relatif_a_la_transposee_de_notre_r"] > 1e-3
    assert "sans objet" in nl.controler_matrices(_lentille(tmp_path / "x", "S"))["couches"]["1"]["controle_contre_notre_r"]


def _sommes_avec(lettre, couche, moitie0, moitie1):
    sommes = J.sommes_jouet(lettre)
    for h, m in ((0, moitie0), (1, moitie1)):
        t = sommes[("out", h)].clone()
        t[couche] = torch.as_tensor(m, dtype=torch.float32)
        sommes[("out", h)] = t
    return sommes


def test_artefact_matrice_non_finie_arret(tmp_path):
    m = J.sommes_jouet("R")[("out", 0)][2].clone()
    m[0, 0] = float("nan")
    with pytest.raises(Arret, match="non finie"):
        nl.controler_matrices(_lentille(tmp_path, sommes=_sommes_avec("R", 2, m, m + 1)), publique=_publique())


def test_artefact_deux_moities_egales_arret(tmp_path):
    m = J.sommes_jouet("R")[("out", 0)][2]
    with pytest.raises(Arret, match="deux moitiés égales"):
        nl.controler_matrices(_lentille(tmp_path, sommes=_sommes_avec("R", 2, m, m)), publique=_publique())


def test_artefact_notre_r_egale_a_l_identite_ou_a_la_lentille_publique_arret(tmp_path):
    identite = 3 * torch.eye(J.D)
    with pytest.raises(Arret, match="notre R égale à l'identité"):
        nl.controler_matrices(_lentille(tmp_path / "a", sommes=_sommes_avec("R", 2, identite, identite + 1e-4)), publique=_publique())
    publique = _publique()
    p = 3 * torch.from_numpy(publique[3])
    with pytest.raises(Arret, match="notre R égale à la lentille publique"):
        nl.controler_matrices(_lentille(tmp_path / "b", sommes=_sommes_avec("R", 3, p, p + 1e-4)), publique=publique)


@pytest.mark.parametrize("transposee", [False, True])
def test_artefact_notre_s_egale_a_notre_r_ou_a_sa_transposee_arret(tmp_path, transposee):
    r = _lentille(tmp_path, "R")
    m0, m1 = (torch.from_numpy(x) for x in r.sommes[2])
    if transposee:
        m0, m1 = m0.T, m1.T
    s = _lentille(tmp_path, "S", sommes=_sommes_avec("S", 2, m0, m1))
    with pytest.raises(Arret, match="notre S égale à notre R de même couche ou à sa transposée"):
        nl.controler_matrices(s, notre_r=r)


def test_indice_de_couche_de_nos_lentilles_un_decalage_d_un_cran_est_arrete(tmp_path):
    r = _lentille(tmp_path, "R")
    nl.controler_matrices(r, publique=_publique())
    m, indice, empreinte = r.matrice_verifiee(2)
    assert indice == 2 and empreinte == r.empreintes_montage["2/entiere"] and r.matrice_verifiee(2, 1)[2] == r.empreintes_montage["2/moitie1"]
    r.decalage = 1
    with pytest.raises(Arret, match="matrice lue d'un autre indice que la couche 2"):
        r.matrice_verifiee(2)
