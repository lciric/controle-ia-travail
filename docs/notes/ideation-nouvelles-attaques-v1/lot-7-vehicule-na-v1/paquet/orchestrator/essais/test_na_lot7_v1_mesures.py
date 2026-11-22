"""Essais du lot 7 — mesures : arrêt n° 15, course arrêtée, lecture unique, deux lectures, M1 à M7, C1, I1, replis,
M4 sans cumul par clé. Chaque garde : un cas sain et un artefact (R5)."""

import os

import pytest

import aides_na_lot7_v1 as A
from pole import commun_na_lot7_v1 as cm
from pole import export_na_v1 as ex
from pole import mesures_na_v1 as ms
from pole import quarantaine_na_v1 as qu

COFFRE = {"type": "ArretGardeCoffre", "numero": 5, "nom": "garde du coffre", "poste": None}


# --- arrêt n° 15 ------------------------------------------------------------------------------------------------------

class TestArret15:
    def test_sain_trois_generations_attestation_et_etiquettes_calcul_une_fois(self, tmp_path):
        sortie, att, ca, cant = A.course_entiere(str(tmp_path))
        m = A.lire(sortie, ca, cant)
        assert m["generations_completes"] == 3 and m["titre"] == "course complète, trois générations"
        assert os.path.isfile(os.path.join(sortie, ms.NOM_TEMOIN_LECTURE))
        assert cm.lire_json_scelle(os.path.join(sortie, ms.NOM_MESURES)) == m

    def test_bilan_a_deux_generations_sans_arret_nomme_refuse(self, tmp_path):
        sortie, att = A.fabriquer_sortie(str(tmp_path), completes=2, arret=None)
        ca, et = A.ecrire_attestation(str(tmp_path), att)
        cant = A.ecrire_anteriorite(str(tmp_path), et)
        with pytest.raises(ms.ArretMesureNA15, match="2 génération"):
            A.lire(sortie, ca, cant)
        assert not os.path.exists(os.path.join(sortie, ms.NOM_TEMOIN_LECTURE))

    def test_arret_sans_nom_refuse(self, tmp_path):
        arret = {"type": "ValueError", "numero": None, "nom": ms.NOM_ARRET_NON_NOMME}
        sortie, att = A.fabriquer_sortie(str(tmp_path), completes=1, arret=arret)
        ca, et = A.ecrire_attestation(str(tmp_path), att)
        cant = A.ecrire_anteriorite(str(tmp_path), et)
        with pytest.raises(ms.ArretMesureNA15, match="arrêt sans nom"):
            A.lire(sortie, ca, cant)

    def test_cloture_absente_refuse(self, tmp_path):
        sortie, att = A.fabriquer_sortie(str(tmp_path), cloture=False)
        ca, et = A.ecrire_attestation(str(tmp_path), att)
        cant = A.ecrire_anteriorite(str(tmp_path), et)
        with pytest.raises(ms.ArretMesureNA15, match="clôture"):
            A.lire(sortie, ca, cant)

    def test_bilan_absent_refuse(self, tmp_path):
        sortie, att = A.fabriquer_sortie(str(tmp_path), bilan=False)
        ca, et = A.ecrire_attestation(str(tmp_path), att)
        cant = A.ecrire_anteriorite(str(tmp_path), et)
        with pytest.raises(ms.ArretMesureNA15, match="bilan"):
            A.lire(sortie, ca, cant)

    def test_attestation_absente_refuse(self, tmp_path):
        sortie, att = A.fabriquer_sortie(str(tmp_path))
        _, et = A.ecrire_attestation(str(tmp_path), att, nom="autre.json")
        cant = A.ecrire_anteriorite(str(tmp_path), et)
        with pytest.raises(ms.ArretMesureNA15, match="attestation"):
            A.lire(sortie, os.path.join(str(tmp_path), "absente.json"), cant)
        assert not os.path.exists(os.path.join(sortie, ms.NOM_TEMOIN_LECTURE))

    def test_attestation_non_scellee_refuse(self, tmp_path):
        sortie, att = A.fabriquer_sortie(str(tmp_path))
        ca, et = A.ecrire_attestation(str(tmp_path), att, sceller=False)
        cant = A.ecrire_anteriorite(str(tmp_path), et)
        with pytest.raises(ms.ArretMesureNA15, match="attestation"):
            A.lire(sortie, ca, cant)

    def test_attestation_d_une_autre_empreinte_refuse(self, tmp_path):
        sortie, att, ca, cant = A.course_entiere(str(tmp_path))
        with pytest.raises(ms.ArretMesureNA15, match="attestation"):
            A.lire(sortie, ca, cant, empreinte_attestation="0" * 64)

    def test_etiquettes_d_anteriorite_absentes_refuse(self, tmp_path):
        sortie, att = A.fabriquer_sortie(str(tmp_path))
        ca, et = A.ecrire_attestation(str(tmp_path), att)
        with pytest.raises(ms.ArretMesureNA15, match="antériorité"):
            A.lire(sortie, ca, os.path.join(str(tmp_path), "absente.json"))

    def test_etiquettes_non_scellees_refuse(self, tmp_path):
        sortie, att = A.fabriquer_sortie(str(tmp_path))
        ca, et = A.ecrire_attestation(str(tmp_path), att)
        cant = A.ecrire_anteriorite(str(tmp_path), et, sceller=False)
        with pytest.raises(ms.ArretMesureNA15, match="antériorité"):
            A.lire(sortie, ca, cant)

    def test_seconde_lecture_refusee(self, tmp_path):
        sortie, att, ca, cant = A.course_entiere(str(tmp_path))
        A.lire(sortie, ca, cant)
        with pytest.raises(ms.ArretMesureNA15, match="seconde lecture"):
            A.lire(sortie, ca, cant)

    def test_seconde_lecture_refusee_avant_toute_autre_lecture(self, tmp_path):
        sortie, att, ca, cant = A.course_entiere(str(tmp_path))
        A.lire(sortie, ca, cant)
        with pytest.raises(ms.ArretMesureNA15, match="seconde lecture"):
            A.lire(sortie, os.path.join(str(tmp_path), "absente.json"), cant)

    def test_lecture_consignee_avant_le_calcul_un_echec_en_route_ne_se_relit_pas(self, tmp_path):
        sortie, att, ca, cant = A.course_entiere(str(tmp_path))
        with pytest.raises(ms.MesuresRefusees):
            A.lire(sortie, ca, cant, famille_tenue=9)
        assert os.path.isfile(os.path.join(sortie, ms.NOM_TEMOIN_LECTURE))
        with pytest.raises(ms.ArretMesureNA15, match="seconde lecture"):
            A.lire(sortie, ca, cant)


# --- course arrêtée ---------------------------------------------------------------------------------------------------

class TestCourseArretee:
    def test_sain_trois_generations(self, tmp_path):
        sortie, att, ca, cant = A.course_entiere(str(tmp_path))
        m = A.lire(sortie, ca, cant)
        assert sorted(m["lectures"]["scellée"]["M3"]) == ["1", "2", "3"]
        assert sorted(m["lectures"]["scellée"]["M1"]["par_generation"]) == ["2", "3"]

    def test_arret_pendant_la_generation_2_mesures_sur_la_seule_generation_1(self, tmp_path):
        sortie, att = A.fabriquer_sortie(str(tmp_path), completes=1, arret=COFFRE)
        ca, et = A.ecrire_attestation(str(tmp_path), att)
        cant = A.ecrire_anteriorite(str(tmp_path), et)
        m = A.lire(sortie, ca, cant)
        assert m["titre"] == "course arrêtée par garde du coffre"
        for lecture in ("scellée", "espèces seules"):
            L = m["lectures"][lecture]
            assert L["M1"] == L["M2"] == L["M1_bis"] == ms.SANS_OBJET
            assert sorted(L["M3"]) == ["1"]
        assert sorted(m["M4"]) == sorted(m["M6"]) == ["1"]
        assert m["C1"]["cases_servies"] == 11 and m["C1"]["trente_trois_cases_servies"] is False

    def test_arret_pendant_la_generation_3_mesures_sur_les_generations_1_et_2(self, tmp_path):
        sortie, att = A.fabriquer_sortie(str(tmp_path), completes=2, arret=COFFRE)
        ca, et = A.ecrire_attestation(str(tmp_path), att)
        cant = A.ecrire_anteriorite(str(tmp_path), et)
        m = A.lire(sortie, ca, cant)
        assert m["titre"] == "course arrêtée par garde du coffre"
        L = m["lectures"]["scellée"]
        assert sorted(L["M3"]) == ["1", "2"] and sorted(L["M1"]["par_generation"]) == ["2"]

    def test_le_registre_de_la_generation_arretee_n_est_pas_lu(self, tmp_path):
        # le registre partiel de la génération 2 porte une ligne que la lecture refuserait : il n'est pas lu
        sortie, att = A.fabriquer_sortie(str(tmp_path), completes=1, arret=COFFRE, registre_partiel=True)
        assert os.path.isfile(os.path.join(sortie, "generation-2", "registre-tentatives-g2.jsonl"))
        ca, et = A.ecrire_attestation(str(tmp_path), att)
        cant = A.ecrire_anteriorite(str(tmp_path), et)
        A.lire(sortie, ca, cant)
        with pytest.raises(ms.MesuresRefusees):
            ms.lire_registres(sortie, 2)


# --- valeurs ----------------------------------------------------------------------------------------------------------

class TestValeurs:
    @pytest.fixture
    def m(self, tmp_path):
        sortie, att, ca, cant = A.course_entiere(str(tmp_path))
        return A.lire(sortie, ca, cant), att

    def test_m3_lecture_scellee_et_especes_seules(self, m):
        m, att = m
        for g in (1, 2, 3):
            s = m["lectures"]["scellée"]["M3"][str(g)]["generation"]
            e = m["lectures"]["espèces seules"]["M3"][str(g)]["generation"]
            assert s["au_coffre"] == {"numerateur": att[g]["au_coffre"], "denominateur": att[g]["rendues"]}
            assert s["hors_case"]["numerateur"] == att[g]["hors_case"]
            assert e["au_coffre"]["denominateur"] == att[g]["rendues"] - att[g]["repli_fiches"]

    def test_m3_lignes_a_zero_pour_chaque_case(self, m):
        m, _ = m
        assert len(m["lectures"]["scellée"]["M3"]["1"]["par_case"]) == 11

    def test_m1_par_programme(self, m):
        m, att = m
        L = m["lectures"]["scellée"]
        den = sum(len(att[g]["passees"]) for g in (2, 3))
        assert L["M1"]["part"]["denominateur"] == den
        assert 0 < L["M1"]["part"]["numerateur"] < den
        assert L["M1_bis"] == 2  # une filiation invalide par génération 2 et 3
        assert "servies par repli : id-repli-1" in L["M1"]["par_espece"]
        E = m["lectures"]["espèces seules"]
        assert E["M1"]["part"]["denominateur"] == den - 2
        assert not any(k.startswith("servies par repli") for k in E["M1"]["par_espece"])

    def test_m4_premiere_tentative_a_l_espece_replis_a_part(self, m):
        m, att = m
        for g in (1, 2, 3):
            assert m["M4"][str(g)]["cout_par_role_usd"]["espece-3"] == pytest.approx(att[g]["cout_rang0_par_role"]["espece-3"])
            assert m["M4"][str(g)]["replis"]["id-espece-3-r1"]["fiches"] == 1
            assert m["M4"][str(g)]["replis"]["id-espece-4-r1"]["tentatives"] == 1
            c = m["M4"][str(g)]["controle_cout_generation"]
            assert c["ecart_usd"] == 0

    def test_m6_chaque_appel_une_fois_arret_1_a_part(self, m):
        m, _ = m
        g1 = m["M6"]["1"]
        assert g1[A.ident_case(1, 1)]["espece-2"][ms.VIDE_MOTIVEE] == 1
        assert g1[A.ident_case(1, 2)]["espece-3"][ms.REPLI_SERVI] == 1
        assert g1[A.ident_case(1, 3)]["espece-4"][ms.ARRET_1] == 1
        assert g1[A.ident_case(1, 3)]["espece-4"][ms.REFUS_DU_MODELE] == 0
        assert g1[A.ident_case(1, 6)]["espece-5"][ms.ILLISIBLE] == 1
        assert len(g1) == 11 and all(len(v) == 5 for v in g1.values())

    def test_m6_sous_comptes_m7_c1_i1_m5(self, m):
        m, _ = m
        assert m["M6_sous_comptes"]["1"][ms.SOUS_COMPTE_PORTIER] == 2
        assert m["lectures"]["scellée"]["M7"]["autre, à nommer"]["denominateur"] > 0
        assert m["C1"] == {"aucune_case_servie_deux_fois": True, "cases_servies": 33, "cases_attendues": 33,
                           "trente_trois_cases_servies": True, "aucune_case_de_la_famille_tenue_a_l_ecart": True}
        assert m["I1"]["titre"] == "pour information"
        assert sum(m["M5"]["par_etiquette"].values()) == 10 and m["M5"]["desaccords"] == 2

    def test_replis_par_role_modele_categorie(self, m):
        m, _ = m
        cats = {(r["role"], r["rang"], r["categorie"]) for r in m["replis"]}
        assert ("espece-3", 0, "cyber") in cats and ("espece-4", 2, "non lue") in cats
        juge = [r for r in m["replis"] if r["role"] == "juge-2" and r["rang"] == 1]
        assert juge and juge[0]["modele_servi"] == "id-repli-1"


class TestGardesDeCoherence:
    def test_sain_le_registre_et_la_ligne_comptent_les_memes_fiches(self, tmp_path):
        sortie, att, ca, cant = A.course_entiere(str(tmp_path))
        A.lire(sortie, ca, cant)

    def test_artefact_ligne_qui_compte_une_fiche_de_plus(self, tmp_path):
        def muter(g, lg):
            lg["coffre"]["rendues"] += 1
            return lg
        sortie, att = A.fabriquer_sortie(str(tmp_path), muter_ligne=muter)
        ca, et = A.ecrire_attestation(str(tmp_path), att)
        cant = A.ecrire_anteriorite(str(tmp_path), et)
        with pytest.raises(ms.MesuresRefusees, match="ne comptent pas les mêmes fiches"):
            A.lire(sortie, ca, cant)

    def test_artefact_registre_servi_d_un_autre_nombre_de_lignes(self, tmp_path):
        def muter(g, lg):
            if g == 2:
                lg["registre_servi"]["lignes_tentative"] -= 1
            return lg
        sortie, att = A.fabriquer_sortie(str(tmp_path), muter_ligne=muter)
        ca, et = A.ecrire_attestation(str(tmp_path), att)
        cant = A.ecrire_anteriorite(str(tmp_path), et)
        with pytest.raises(ms.MesuresRefusees, match="registre servi"):
            A.lire(sortie, ca, cant)

    def test_artefact_attestation_qui_omet_une_fiche_passee(self, tmp_path):
        sortie, att = A.fabriquer_sortie(str(tmp_path))
        une = att[2]["passees"][0][0]
        ca, et = A.ecrire_attestation(str(tmp_path), att, retirer=(une,))
        cant = A.ecrire_anteriorite(str(tmp_path), et)
        with pytest.raises(ms.MesuresRefusees, match="attestation"):
            A.lire(sortie, ca, cant)

    def test_artefact_plus_de_soixante_fiches_lues(self, tmp_path):
        sortie, att = A.fabriquer_sortie(str(tmp_path))
        ca, et = A.ecrire_attestation(str(tmp_path), att)
        cant = A.ecrire_anteriorite(str(tmp_path), et, lues=61)
        with pytest.raises(ms.MesuresRefusees, match="borne de lecture"):
            A.lire(sortie, ca, cant)

    def test_artefact_role_sans_espece_dite(self, tmp_path):
        sortie, att, ca, cant = A.course_entiere(str(tmp_path))
        especes = dict(A.ESPECES_DES_ROLES)
        del especes["juge-2"]
        with pytest.raises(ms.MesuresRefusees, match="sans espèce"):
            A.lire(sortie, ca, cant, especes_des_roles=especes)

    def test_artefact_case_de_la_famille_tenue(self, tmp_path):
        sortie, att, ca, cant = A.course_entiere(str(tmp_path))
        ax = A.axes()
        ax[A.ident_case(2, 4)][0] = A.FAMILLE_TENUE
        m = A.lire(sortie, ca, cant, axes_des_cases=ax)
        assert m["C1"]["aucune_case_de_la_famille_tenue_a_l_ecart"] is False

    def test_artefact_champ_hors_liste_au_registre(self, tmp_path):
        lignes, _ = A.lignes_de_generation(1, [])
        l = dict(lignes[0], champ_libre="x")
        with pytest.raises(ms.MesuresRefusees, match="champ hors"):
            ms._verifier_ligne_registre(l, 1)

    def test_sain_seules_les_lignes_de_fiche_sont_des_fiches(self):
        lignes, att = A.lignes_de_generation(1, [])
        t = ms.tentatives(lignes)
        assert sum(len(x["fiches"]) for x in t) == att["rendues"]
        assert len(t) == sum(1 for l in lignes if l["type_ligne"] == "tentative")

    def test_artefact_fiche_sans_sa_tentative(self):
        lignes, _ = A.lignes_de_generation(1, [])
        i = next(i for i, l in enumerate(lignes) if l["type_ligne"] == "tentative" and l["case"] == A.ident_case(1, 4)
                 and l["espece"] == "espece-1")
        with pytest.raises(ms.MesuresRefusees, match="sans sa tentative"):
            ms.tentatives(lignes[:i] + lignes[i + 1:])

    def test_artefact_fiche_rattachee_a_une_tentative_sans_fiche(self):
        lignes, _ = A.lignes_de_generation(1, [])
        t = next(l for l in lignes if l["type_ligne"] == "tentative" and l.get("classe_issue") == ms.VIDE_MOTIVEE)
        f = next(l for l in lignes if l["type_ligne"] == "fiche")
        f = dict(f, case=t["case"], espece=t["espece"], rang_repli=t["rang_repli"], identifiant="fiche-plantee")
        with pytest.raises(ms.MesuresRefusees, match="sans sa tentative"):
            ms.tentatives(lignes + [f])

    def test_artefact_ligne_de_tentative_qui_porte_une_fiche(self):
        lignes, _ = A.lignes_de_generation(1, [])
        t = next(l for l in lignes if l["type_ligne"] == "tentative")
        with pytest.raises(ms.MesuresRefusees, match="ne porte pas de fiche"):
            ms._verifier_ligne_registre(dict(t, classe=ms.PASSEE, identifiant="x"), 1)

    def test_artefact_deux_tentatives_au_meme_rang(self):
        lignes, _ = A.lignes_de_generation(1, [])
        t = next(l for l in lignes if l["type_ligne"] == "tentative" and l["espece"] == "espece-1")
        with pytest.raises(ms.MesuresRefusees, match="deux tentatives"):
            ms.tentatives(lignes + [dict(t)])

    def test_artefact_type_ligne_absent_ou_hors_liste(self):
        lignes, _ = A.lignes_de_generation(1, [])
        for v in (None, "autre"):
            l = dict(lignes[0])
            l.pop("type_ligne") if v is None else l.update(type_ligne=v)
            with pytest.raises(ms.MesuresRefusees, match="type_ligne"):
                ms._verifier_ligne_registre(l, 1)

    def test_artefact_sans_reponse_avec_un_modele_servi(self):
        lignes, _ = A.lignes_de_generation(1, [])
        l = next(l for l in lignes if l.get("raison_arret") == "sans_reponse")
        with pytest.raises(ms.MesuresRefusees, match="sans réponse"):
            ms._verifier_ligne_registre(dict(l, modele_servi="id-x"), 1)

    def test_chaines_de_repli_erratum_1(self):
        t = lambda r, raison, k: {"rang": r, "raison_arret": raison, "classe_issue": k}
        assert ms.classe_de_chaine([t(0, "refusal", ms.REFUS_DU_MODELE), t(1, "refusal", ms.REFUS_DU_MODELE),
                                    t(2, "refusal", ms.REFUS_DU_MODELE)]) == ms.ARRET_1
        assert ms.classe_de_chaine([t(0, "refusal", ms.REPLI_SERVI), t(1, "end_turn", ms.FICHES_RENDUES)]) == ms.REPLI_SERVI
        assert ms.classe_de_chaine([t(0, "refusal", ms.ILLISIBLE), t(1, "sans_reponse", ms.ILLISIBLE)]) == ms.ILLISIBLE
        with pytest.raises(ms.MesuresRefusees):
            ms.classe_de_chaine([t(0, "refusal", ms.ILLISIBLE), t(1, "end_turn", ms.FICHES_RENDUES)])
        with pytest.raises(ms.MesuresRefusees):
            ms.classe_de_chaine([t(0, "end_turn", ms.FICHES_RENDUES), t(1, "end_turn", ms.FICHES_RENDUES)])
        with pytest.raises(ms.MesuresRefusees):
            ms.classe_de_chaine([t(0, "refusal", ms.ILLISIBLE), t(2, "refusal", ms.REFUS_DU_MODELE)])


# --- M4 sans cumul par clé (V9, l. 156) ---------------------------------------------------------------------------------

class TestM4SansCumulParCle:
    def test_sain_absents_des_mesures_et_de_l_export_presents_au_seul_journal(self, tmp_path):
        sortie, att, ca, cant = A.course_entiere(str(tmp_path))
        m = A.lire(sortie, ca, cant)
        chemin_export = os.path.join(str(tmp_path), ex.NOM_EXPORT)
        ex.ecrire_export(chemin_export, m, roles_de_configuration=("prop-e1",))
        textes = list(A.NOMS_CLES_ESSAI) + list(A.CHAMPS_CUMUL)
        assert qu.rechercher_textes([os.path.join(sortie, ms.NOM_MESURES), chemin_export], textes) == {}
        trouves = qu.rechercher_textes([sortie], textes)
        assert list(trouves) == [os.path.join(sortie, ms.NOM_JOURNAL_ARRETS)]
        qu.exiger_absence([os.path.join(sortie, ms.NOM_MESURES), chemin_export], textes=textes)

    def test_artefact_un_nom_de_cle_dans_la_sortie_des_mesures_est_trouve(self, tmp_path):
        sortie, att, ca, cant = A.course_entiere(str(tmp_path))
        m = A.lire(sortie, ca, cant)
        m["M4"]["1"]["cout_par_role_usd"][A.NOMS_CLES_ESSAI[0]] = 1.0
        plante = os.path.join(str(tmp_path), "mesures-plantees.json")
        cm.ecrire_json_scelle(plante, m)
        with pytest.raises(ex.ArretQuarantaineRompueNA17):
            qu.exiger_absence([plante], textes=list(A.NOMS_CLES_ESSAI) + list(A.CHAMPS_CUMUL))

    def test_les_lignes_de_cumul_ne_sont_pas_lues(self, tmp_path):
        sortie, att = A.fabriquer_sortie(str(tmp_path))
        generations, cloture = ms.lire_cloture(sortie)
        assert all(not set(A.CHAMPS_CUMUL) & set(map(str, l)) for l in generations.values())
        assert A.NOMS_CLES_ESSAI[0] not in repr(generations) + repr(cloture)
