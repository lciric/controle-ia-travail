"""Essais du portier neuf (lot 5 du véhicule NA-1) : ordre forme, modèle, hors case (D6) ; étiquettes de D3 seules ; deux
sortes d'appel ; passeports ; journal sans contenu ; refus écrits ; arrêt n° 4 ; champ `case` ; « autre, à nommer » ;
fiche hors contrat de longueur (conception v5, § 2.4, § 2.13, § 6.1, § 6.2). Données factices seules ; consigne de D3 et
bornes en brouillon d'essai factice, déclaré comme tel."""

import json
import os
import sys

import pytest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import aides_na_lot5_v1 as A5  # noqa: E402
from pole import aiguilleur_v53  # noqa: E402
from pole import contrat_fiche_na_v1 as ct  # noqa: E402
from pole import garde_motifs_na_v4 as gm  # noqa: E402
from pole import journal_na_v3 as jn  # noqa: E402
from pole import lecteur_fiches_na_v1 as lf  # noqa: E402
from pole import portier_na_v1 as pt  # noqa: E402

NIVEAU = A5.etiquette("niveau de l'idée")
CONCRET = A5.etiquette("concret")


def lue(c, extras=()):
    return lf.lire_fiches(A5.en_lignes(c, extras=extras)).fiches[0]


@pytest.fixture
def dossier(tmp_path):
    d = tmp_path / "sortie"
    d.mkdir()
    return str(d)


class TestDeclarationEtLecture:
    def test_brouillon_declare_comme_tel(self):
        assert "brouillon d'essai factice" in A5.DECLARATION_ESSAI.statut

    @pytest.mark.parametrize("sens,texte", [(pt.NIVEAU_IDEE, "niveau de l'idée"), (pt.CONCRET, "concret")])
    def test_etiquettes_de_l_appel_fiche(self, sens, texte):
        lu = pt.lire_etiquette(A5.etiquette(texte), pt.SORTE_FICHE, A5.DECLARATION_ESSAI)
        assert lu.sens == sens and lu.cause == "lue"

    @pytest.mark.parametrize("sens", pt.SENS_REPONSE)
    def test_etiquettes_de_l_appel_reponse_sans_fiche(self, sens):
        lu = pt.lire_etiquette(A5.etiquette(sens), pt.SORTE_REPONSE, A5.DECLARATION_ESSAI)
        assert lu.sens == sens

    @pytest.mark.parametrize("texte,cause", [
        (A5.etiquette("a_corriger"), "hors liste"),
        (A5.etiquette("niveau_methode"), "hors liste"),
        ('{"classe": "niveau_methode"}', "absente"),
        ("Texte factice sans étiquette.", "absente"),
        (A5.etiquette("niveau de l'idée") + "étiquette : concret\n", "double"),
        (A5.etiquette("niveau de l'idée") + "étiquette : niveau de l'idée\n", "double"),
        (A5.etiquette("réponse vide motivée"), "hors liste"),  # étiquette de l'autre sorte d'appel
        (A5.etiquette("Niveau de l'idée"), "hors liste"),
        ("", "absente"),
    ])
    def test_hors_liste_absente_ou_double_vaut_illisible(self, texte, cause):
        lu = pt.lire_etiquette(texte, pt.SORTE_FICHE, A5.DECLARATION_ESSAI)
        assert lu.sens is None and lu.cause == cause

    @pytest.mark.parametrize("texte", ["", "x", "étiquette :", "\n\n", "étiquette : concret\nétiquette : concret"])
    def test_la_lecture_rend_toujours_un_objet(self, texte):
        for sorte in (pt.SORTE_FICHE, pt.SORTE_REPONSE):
            assert isinstance(pt.lire_etiquette(texte, sorte, A5.DECLARATION_ESSAI), pt.LectureEtiquette)

    def test_declaration_mal_formee_refusee(self):
        with pytest.raises(pt.PortierRefuse):
            pt.declaration_de(forme="bloc json", cle="étiquette", fiche={}, reponse_sans_fiche={}, statut="x")
        with pytest.raises(pt.PortierRefuse):
            pt.declaration_de(forme=pt.FORME_LIGNE_ANCREE, cle="étiquette",
                              fiche={pt.NIVEAU_IDEE: "même", pt.CONCRET: "même"},
                              reponse_sans_fiche=dict(A5.DECLARATION_ESSAI.reponse_sans_fiche), statut="x")


class TestPortierFormeEtNeuf:
    def test_fiche_a_douze_champs_va_au_portier_et_passe_avec_passeport(self, dossier):
        p, appel = A5.portier(dossier, [NIVEAU])
        issue = p.classer_fiche(lue(A5.contenu()), identifiant=A5.mot_fiche(1), case=A5.CASE)
        assert issue.classe == pt.PASSEE and issue.passeport is not None
        assert p.appels_au_modele == 1 and appel.requetes[0].sorte == "portier_fiche"
        assert issue.passeport.empreinte == pt.empreinte_texte_classe(A5.contenu())

    def test_temoin_a_champ_de_plus_au_coffre_sans_autre_cause_ni_appel(self, dossier):
        p, appel = A5.portier(dossier, [])
        issue = p.classer_fiche(lue(A5.contenu(), extras=[("comment_faire", "valeur factice")]),
                                identifiant=A5.mot_fiche(2), case=A5.CASE)
        assert issue.classe == pt.AU_COFFRE and issue.cause == ct.CAUSE_CHAMP_EN_PLUS
        assert p.appels_au_modele == 0 and appel.requetes == []

    @pytest.mark.parametrize("texte", [A5.etiquette("a_corriger"), A5.etiquette("hors liste factice"),
                                       A5.etiquette("niveau de l'idée") + "étiquette : concret\n", "sans étiquette"])
    def test_etiquette_illisible_fiche_au_coffre_comptee_a_part(self, dossier, texte):
        p, _ = A5.portier(dossier, [texte])
        issue = p.classer_fiche(lue(A5.contenu()), identifiant=A5.mot_fiche(3), case=A5.CASE)
        assert issue.classe == pt.AU_COFFRE and issue.cause == pt.CAUSE_ETIQUETTE_ILLISIBLE and issue.passeport is None
        assert p.comptes()["causes_fiche"] == {pt.CAUSE_ETIQUETTE_ILLISIBLE: 1}

    def test_concret_au_coffre(self, dossier):
        p, _ = A5.portier(dossier, [CONCRET])
        assert p.classer_fiche(lue(A5.contenu()), identifiant=A5.mot_fiche(4), case=A5.CASE).classe == pt.AU_COFFRE

    def test_l_aiguilleur_du_noyau_jamais_appele(self, dossier, monkeypatch):
        compte = {"n": 0}

        def espion(*a, **k):
            compte["n"] += 1
            raise AssertionError("aiguilleur du noyau appelé")

        monkeypatch.setattr(aiguilleur_v53.Aiguilleur, "classer", espion)
        monkeypatch.setattr(aiguilleur_v53, "lire_classe", espion)
        p, _ = A5.portier(dossier, [NIVEAU, A5.etiquette("réponse vide motivée")])
        p.classer_fiche(lue(A5.contenu()), identifiant=A5.mot_fiche(5), case=A5.CASE)
        p.classer_reponse_sans_fiche("Réponse factice.", identifiant_reponse=A5.mot_fiche(6), case=A5.CASE)
        assert compte["n"] == 0
        with open(pt.__file__, encoding="utf-8") as f:
            assert "aiguilleur_v53" not in f.read().split('"""', 2)[2]

    def test_requetes_du_portier_passent_la_garde_et_se_journalisent(self, dossier):
        p, appel = A5.portier(dossier, [NIVEAU, A5.etiquette("refus du modèle")])
        p.classer_fiche(lue(A5.contenu()), identifiant=A5.mot_fiche(7), case=A5.CASE)
        p.classer_reponse_sans_fiche("Réponse factice qui décline.", identifiant_reponse=A5.mot_fiche(8), case=A5.CASE)
        lignes = jn.verifier_journal(appel.journal.chemin)
        assert [l["sorte"] for l in lignes] == ["portier_fiche", "portier_reponse_sans_fiche"]
        garde = A5.A.garde_essai()
        for r in appel.requetes:
            assert isinstance(garde.garder_requete(r.octets), gm.RequeteGardee)

    def test_forme_de_la_reponse_sans_fiche_servie(self, dossier):
        p, appel = A5.portier(dossier, [A5.etiquette("réponse vide motivée")])
        texte = "Réponse factice\nsur deux lignes ```"
        p.classer_reponse_sans_fiche(texte, identifiant_reponse=A5.mot_fiche(9), case=A5.CASE)
        octets = appel.requetes[0].octets.decode("utf-8")
        attendu = "\n\n## La réponse\n```json\n" + json.dumps({"reponse": texte}, ensure_ascii=False, indent=1) + "\n```\n"
        assert octets.endswith(attendu)

    def test_identifiant_hexadecimal_ou_redit_refuse(self, dossier):
        p, _ = A5.portier(dossier, [NIVEAU])
        with pytest.raises(pt.PortierRefuse):
            p.classer_fiche(lue(A5.contenu()), identifiant="f0123456789ab", case=A5.CASE)
        p.classer_fiche(lue(A5.contenu()), identifiant=A5.mot_fiche(10), case=A5.CASE)
        with pytest.raises(pt.PortierRefuse):
            p.classer_fiche(lue(A5.contenu()), identifiant=A5.mot_fiche(10), case=A5.CASE)


class TestClassesDIssueDAppel:
    def test_reponse_a_fiches_par_programme(self, dossier):
        p, _ = A5.portier(dossier, [NIVEAU, NIVEAU])
        texte = A5.en_lignes(A5.contenu()) + "\n---\n" + A5.en_lignes(A5.contenu(idee="Autre idée factice."))
        r = p.traiter_reponse(texte, case=A5.CASE, identifiant_reponse=A5.mot_fiche(20),
                              identifiant_fiche=lambda rang: A5.mot_fiche(20 + rang))
        assert r.classe_appel == pt.FICHES_RENDUES and len(r.fiches) == 2
        assert all(f.classe == pt.PASSEE for f in r.fiches)

    @pytest.mark.parametrize("sens", pt.SENS_REPONSE)
    def test_chaque_etiquette_a_sa_classe_jamais_l_arret_1(self, dossier, sens):
        p, appel = A5.portier(dossier, [A5.etiquette(sens)])
        r = p.traiter_reponse("Je ne connais que des variantes factices.", case=A5.CASE,
                              identifiant_reponse=A5.mot_fiche(30), identifiant_fiche=A5.mot_fiche)
        assert r.classe_appel == sens and r.fiches == ()
        assert appel.requetes[0].sorte == "portier_reponse_sans_fiche"

    def test_temoin_vide_motivee_et_son_artefact(self, dossier):
        p, _ = A5.portier(dossier, [A5.etiquette("réponse vide motivée"), A5.etiquette("refus du modèle")])
        r1 = p.classer_reponse_sans_fiche("Témoin factice motivé.", identifiant_reponse=A5.mot_fiche(31), case=A5.CASE)
        r2 = p.classer_reponse_sans_fiche("Témoin factice qui décline.", identifiant_reponse=A5.mot_fiche(32), case=A5.CASE)
        assert (r1.classe_appel, r2.classe_appel) == (pt.VIDE_MOTIVEE, pt.REFUS_DU_MODELE)

    def test_etiquette_illisible_reponse_illisible_sous_compte(self, dossier):
        p, _ = A5.portier(dossier, [A5.etiquette("niveau de l'idée")])
        r = p.classer_reponse_sans_fiche("Réponse factice.", identifiant_reponse=A5.mot_fiche(33), case=A5.CASE)
        assert r.classe_appel == pt.ILLISIBLE and r.sous_compte == pt.SOUS_COMPTE_PORTIER
        assert p.comptes()["sous_comptes_reponse_illisible"] == {pt.SOUS_COMPTE_PORTIER: 1}

    def test_morceau_non_reconnu_compte(self, dossier):
        c = A5.contenu()
        del c["idee"]
        p, _ = A5.portier(dossier, [A5.etiquette("réponse illisible")])
        r = p.traiter_reponse(A5.en_lignes(c), case=A5.CASE, identifiant_reponse=A5.mot_fiche(34),
                              identifiant_fiche=A5.mot_fiche)
        assert r.classe_appel == pt.ILLISIBLE and r.non_reconnus == (lf.CAUSE_MANQUANT,)
        assert p.comptes()["morceaux_non_reconnus"] == 1


class TestArret4HorsCase:
    def test_fiche_dans_sa_case_passe(self, dossier):
        p, _ = A5.portier(dossier, [NIVEAU])
        assert p.classer_fiche(lue(A5.contenu()), identifiant=A5.mot_fiche(40), case=A5.CASE).classe == pt.PASSEE

    def test_temoin_hors_case_refuse_et_compte(self, dossier):
        p, _ = A5.portier(dossier, [NIVEAU, NIVEAU])
        autre = A5.contenu(case=A5.case_de((2, 2, 2), 99))
        autre["case"] = A5.CASE.identifiant
        i1 = p.classer_fiche(lue(autre), identifiant=A5.mot_fiche(41), case=A5.CASE)
        c = A5.contenu()
        c["etage_de_lecture"] = c["etage_de_lecture"] + "."
        i2 = p.classer_fiche(lue(c), identifiant=A5.mot_fiche(42), case=A5.CASE)
        assert (i1.classe, i2.classe) == (pt.HORS_CASE, pt.HORS_CASE)
        assert i1.passeport is None and i2.passeport is None
        assert p.comptes()["classes_fiche"][pt.HORS_CASE] == 2

    def test_hors_case_a_champ_de_plus_au_coffre(self, dossier):
        p, _ = A5.portier(dossier, [])
        c = A5.contenu(menace_du_programme="menace factice autre")
        i = p.classer_fiche(lue(c, extras=[("comment_faire", "v")]), identifiant=A5.mot_fiche(43), case=A5.CASE)
        assert i.classe == pt.AU_COFFRE

    def test_hors_case_et_concret_au_coffre_ordre_D6(self, dossier):
        p, _ = A5.portier(dossier, [CONCRET])
        c = A5.contenu(menace_du_programme="menace factice autre")
        i = p.classer_fiche(lue(c), identifiant=A5.mot_fiche(44), case=A5.CASE)
        assert i.classe == pt.AU_COFFRE and i.cause == pt.CAUSE_CONCRET

    def test_le_modele_est_appele_avant_la_comparaison_hors_case(self, dossier):
        p, _ = A5.portier(dossier, [NIVEAU])
        c = A5.contenu(menace_du_programme="menace factice autre")
        p.classer_fiche(lue(c), identifiant=A5.mot_fiche(45), case=A5.CASE)
        assert p.appels_au_modele == 1


class TestChampCaseEtAutreANommer:
    def test_champ_case_different_consigne_compte_classe_inchangee(self, dossier):
        p, _ = A5.portier(dossier, [NIVEAU])
        c = A5.contenu()
        c["case"] = A5.CASE_AUTRE.identifiant
        i = p.classer_fiche(lue(c), identifiant=A5.mot_fiche(50), case=A5.CASE)
        assert i.classe == pt.PASSEE and i.case_differe
        assert p.comptes()["champ_case_different"] == 1
        lignes = pt.relire_ajout_seul(p.journal.chemin)
        assert lignes[0]["case_differe"] is True and lignes[0]["classe"] == pt.PASSEE

    def test_autre_a_nommer_supposition_dans_idee_passe(self, dossier):
        p, _ = A5.portier(dossier, [NIVEAU])
        c = A5.contenu(case=A5.CASE_AUTRE, idee="Supposition factice nommée : un trait factice neuf. Idée factice.")
        assert p.classer_fiche(lue(c), identifiant=A5.mot_fiche(51), case=A5.CASE_AUTRE).classe == pt.PASSEE

    def test_autre_a_nommer_supposition_dans_le_champ_ferme_hors_case(self, dossier):
        p, _ = A5.portier(dossier, [NIVEAU])
        c = A5.contenu(case=A5.CASE_AUTRE, ce_que_le_moniteur_suppose="un trait factice neuf")
        assert p.classer_fiche(lue(c), identifiant=A5.mot_fiche(52), case=A5.CASE_AUTRE).classe == pt.HORS_CASE


class TestHorsContratDeLongueur:
    def test_au_coffre_compte_sans_appel_texte_inchange(self, dossier):
        p, _ = A5.portier(dossier, [])
        idee = "y" * (A5.BORNES_ESSAI.borne("idee") + 1)
        i = p.classer_fiche(lue(A5.contenu(idee=idee)), identifiant=A5.mot_fiche(60), case=A5.CASE)
        assert i.classe == pt.AU_COFFRE and i.cause == ct.CAUSE_LONGUEUR and p.appels_au_modele == 0
        assert i.contenu["idee"] == idee
        k = p.comptes()
        assert k["hors_contrat_de_longueur"] == 1 and k["fiches_rendues"] == 1  # rendu obtenu : au dénominateur de M3


class TestRefusEcritEtAppelsSansLecture:
    def test_refus_ecrit_fiche_au_coffre_classe_ecrite_comptee(self, dossier):
        p, _ = A5.portier(dossier, ["refus écrit"])
        i = p.classer_fiche(lue(A5.contenu()), identifiant=A5.mot_fiche(70), case=A5.CASE)
        assert i.classe == pt.AU_COFFRE and i.cause == pt.CAUSE_REFUS_ECRIT_FICHE
        k = p.comptes()
        assert k["au_coffre_par_refus_du_portier"] == 1 and k["fiches_rendues"] == 1

    def test_refus_ecrit_reponse_sans_fiche_illisible(self, dossier):
        p, _ = A5.portier(dossier, ["refus écrit"])
        r = p.classer_reponse_sans_fiche("Réponse factice.", identifiant_reponse=A5.mot_fiche(71), case=A5.CASE)
        assert r.classe_appel == pt.ILLISIBLE and r.sous_compte == pt.SOUS_COMPTE_PORTIER
        assert r.cause == pt.CAUSE_REFUS_ECRIT_REPONSE

    def test_refus_ecrit_d_une_autre_sorte_refuse(self, dossier):
        j = jn.JournalRequetes(dossier, "autre.jsonl")
        faux = j.journaliser_refus_ecrit(sorte="juge", role="r", generation=1, case="", garde="g", cause="c")
        p, _ = A5.portier(dossier, [faux])
        with pytest.raises(pt.PortierRefuse):
            p.classer_fiche(lue(A5.contenu()), identifiant=A5.mot_fiche(72), case=A5.CASE)

    @pytest.mark.parametrize("issue,cause", [(None, pt.CAUSE_NON_LANCE), ({"lu": None}, pt.CAUSE_NON_LUE)])
    def test_non_lance_ou_non_lu_au_coffre(self, dossier, issue, cause):
        p, _ = A5.portier(dossier, [issue])
        i = p.classer_fiche(lue(A5.contenu()), identifiant=A5.mot_fiche(73), case=A5.CASE)
        assert i.classe == pt.AU_COFFRE and i.cause == cause

    def test_lecture_d_une_autre_fonction_refusee(self, dossier):
        autre = pt.LectureEtiquette(pt.SORTE_REPONSE, pt.VIDE_MOTIVEE, "lue")
        p, _ = A5.portier(dossier, [{"lu": autre}, {"lu": "niveau de l'idée"}])
        with pytest.raises(pt.PortierRefuse):
            p.classer_fiche(lue(A5.contenu()), identifiant=A5.mot_fiche(75), case=A5.CASE)
        with pytest.raises(pt.PortierRefuse):
            p.classer_fiche(lue(A5.contenu()), identifiant=A5.mot_fiche(76), case=A5.CASE)

    def test_fiche_servie_d_une_autre_empreinte_que_le_texte_classe_refusee(self, dossier, monkeypatch):
        monkeypatch.setattr(pt, "empreinte_texte_classe", lambda contenu: "0" * 64)
        p, _ = A5.portier(dossier, [NIVEAU])
        with pytest.raises(pt.PortierRefuse):
            p.classer_fiche(lue(A5.contenu()), identifiant=A5.mot_fiche(77), case=A5.CASE)

    def test_issue_inconnue_refusee(self, dossier):
        p, _ = A5.portier(dossier, [{"autre": 1}])
        with pytest.raises(pt.PortierRefuse):
            p.classer_fiche(lue(A5.contenu()), identifiant=A5.mot_fiche(74), case=A5.CASE)

    def test_aucune_fiche_rendue_sans_classe(self, dossier):
        issues = [NIVEAU, CONCRET, "refus écrit", None, {"lu": None}, "illisible factice"]
        p, _ = A5.portier(dossier, issues)
        for k in range(len(issues)):
            p.classer_fiche(lue(A5.contenu()), identifiant=A5.mot_fiche(80 + k), case=A5.CASE)
        k = p.comptes()
        assert k["fiches_rendues"] == 6 and sum(k["classes_fiche"].values()) == 6
        assert all(f.classe in pt.CLASSES_FICHE for f in p.issues_fiches())

    def test_trois_reponses_illisibles_de_suite_aucun_arret(self, dossier):
        p, _ = A5.portier(dossier, ["illisible un", "illisible deux", "illisible trois", "illisible quatre"])
        for k in range(3):
            p.classer_fiche(lue(A5.contenu()), identifiant=A5.mot_fiche(90 + k), case=A5.CASE)
        p.classer_reponse_sans_fiche("Réponse factice.", identifiant_reponse=A5.mot_fiche(93), case=A5.CASE)
        assert p.appels_au_modele == 4
        assert p.comptes()["classes_fiche"][pt.AU_COFFRE] == 3


class TestPasseportExige:
    def test_passee_munie_de_son_passeport(self, dossier):
        p, _ = A5.portier(dossier, [NIVEAU])
        i = p.classer_fiche(lue(A5.contenu()), identifiant=A5.mot_fiche(100), case=A5.CASE)
        assert p.exiger_passeport(i.identifiant, A5.contenu()) == i.passeport

    @pytest.mark.parametrize("issue", [CONCRET, "illisible factice", "refus écrit"])
    def test_sans_passeport_arret_A17(self, dossier, issue):
        p, _ = A5.portier(dossier, [issue])
        i = p.classer_fiche(lue(A5.contenu()), identifiant=A5.mot_fiche(101), case=A5.CASE)
        with pytest.raises(pt.ArretSansPasseportNA):
            p.exiger_passeport(i.identifiant, A5.contenu())

    def test_hors_case_sans_passeport(self, dossier):
        p, _ = A5.portier(dossier, [NIVEAU])
        c = A5.contenu(menace_du_programme="menace factice autre")
        i = p.classer_fiche(lue(c), identifiant=A5.mot_fiche(102), case=A5.CASE)
        with pytest.raises(pt.ArretSansPasseportNA):
            p.exiger_passeport(i.identifiant, c)

    def test_texte_change_apres_classement_arret(self, dossier):
        p, _ = A5.portier(dossier, [NIVEAU])
        i = p.classer_fiche(lue(A5.contenu()), identifiant=A5.mot_fiche(103), case=A5.CASE)
        with pytest.raises(pt.ArretSansPasseportNA):
            p.exiger_passeport(i.identifiant, A5.contenu(idee="Idée factice changée."))

    def test_passeport_de_l_aiguilleur_du_noyau_ne_vaut_rien(self, dossier, tmp_path):
        p, _ = A5.portier(dossier, [])
        fiche_noyau = {"ident": "F0123456789ab", "contenu": A5.contenu(), "passe": "niveau_methode"}
        with pytest.raises(pt.ArretSansPasseportNA):
            p.exiger_passeport(fiche_noyau["ident"], fiche_noyau["contenu"])
        with pytest.raises(pt.ArretSansPasseportNA):
            p.exiger_passeport(A5.mot_fiche(104), A5.contenu())

    def test_passeport_d_un_autre_portier_ne_vaut_rien(self, dossier, tmp_path):
        p1, _ = A5.portier(dossier, [NIVEAU])
        i = p1.classer_fiche(lue(A5.contenu()), identifiant=A5.mot_fiche(105), case=A5.CASE)
        d2 = tmp_path / "sortie2"
        d2.mkdir()
        p2, _ = A5.portier(str(d2), [])
        with pytest.raises(pt.ArretSansPasseportNA):
            p2.exiger_passeport(i.identifiant, A5.contenu())


class TestJournalSansContenu:
    def test_journal_scelle_sans_aucun_contenu(self, dossier):
        p, _ = A5.portier(dossier, [NIVEAU, A5.etiquette("réponse vide motivée")])
        c = A5.contenu(idee="Marqueur inerte factice zqxv dans l'idée.")
        p.classer_fiche(lue(c), identifiant=A5.mot_fiche(110), case=A5.CASE)
        p.classer_reponse_sans_fiche("Marqueur inerte factice wqyk dans la réponse.", identifiant_reponse=A5.mot_fiche(111),
                                     case=A5.CASE)
        p.sceller()
        with open(p.journal.chemin, encoding="utf-8") as f:
            brut = f.read()
        assert "zqxv" not in brut and "wqyk" not in brut and "grandeur factice" not in brut
        lignes = pt.relire_ajout_seul(p.journal.chemin, exiger_sceau=True)
        assert {k for l in lignes for k in l} <= set(pt.JournalPortier.CHAMPS_PERMIS) | {"rang", "precedente", "version"}
        with pytest.raises(pt.AjoutSeulRefuse):
            p.journal.ajouter({"identifiant": "x"})

    def test_journal_reecrit_refuse(self, dossier):
        p, _ = A5.portier(dossier, [NIVEAU, NIVEAU])
        p.classer_fiche(lue(A5.contenu()), identifiant=A5.mot_fiche(112), case=A5.CASE)
        with open(p.journal.chemin, "ab") as f:
            f.write(b"x")
        with pytest.raises(pt.AjoutSeulRefuse):
            p.classer_fiche(lue(A5.contenu()), identifiant=A5.mot_fiche(113), case=A5.CASE)
