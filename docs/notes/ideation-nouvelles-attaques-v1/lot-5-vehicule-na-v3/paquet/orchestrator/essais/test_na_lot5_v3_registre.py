"""Essais du registre des tentatives d'appel v3 (lot 5 v3 du véhicule NA-1) : champs de l'interface des lots 5, 6 et 7
et de ses errata 1 et 2 ; erratum 1 (`type_ligne`, trois refus, sans réponse, rôle non proposeur servi par repli) ; chaque garde sur un cas
sain et sur un artefact (R5) ; ancien format refusé en le disant ; différentiel avec le v1 (registre servi et garde du coffre
égaux à l'octet sur les lignes de fiche). Données factices seules."""

import json
import math
import os
import sys

import pytest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import aides_na_lot5_v3 as A  # noqa: E402
from pole import portier_na_v1 as pt  # noqa: E402
from pole import registre_na_v1 as rg  # noqa: E402
from pole import registre_na_v3 as rg3  # noqa: E402
from pole import tirage_na_v4 as tn  # noqa: E402
from pole import verifier_registre_servi_na_v1 as vr  # noqa: E402
from pole import verifier_registre_servi_na_v3 as vr3  # noqa: E402
import re  # noqa: E402

RACINE = tn.RACINE_ECRITE
TENT, FICHE = rg3.TYPE_TENTATIVE, rg3.TYPE_FICHE


@pytest.fixture
def dossier(tmp_path):
    d = tmp_path / "sortie"
    d.mkdir()
    return str(d)


def refuse(r, tentatives, fiches=(), motif=None, classe=rg3.RegistreRefuse):
    """L'artefact est refusé, et rien n'est écrit."""
    avant = A.taille(r.chemin)
    with pytest.raises(classe) as e:
        r.ajouter_chaine(tentatives, fiches)
    assert A.taille(r.chemin) == avant
    if motif:
        assert motif in str(e.value)
    return e.value


def trois_refus(**k):
    return [A.refus(r, classe_issue=rg3.CLASSE_TROIS_REFUS, **k) for r in (0, 1, 2)]


def sans_reponse(rang=1, **k):
    return A.tentative(rang, raison=rg3.RAISON_SANS_REPONSE, servi=None, classe_issue=pt.ILLISIBLE, **k)


# --- écriture : cas sains ---------------------------------------------------------------------------------------------

class TestEcritureSaine:
    def test_chaine_simple_une_tentative_deux_fiches_tous_les_champs(self, dossier):
        r = A.registre(dossier)
        lignes = r.ajouter_chaine([A.tentative()], [A.issue(1), A.issue(2, pt.AU_COFFRE)])
        assert [l["type_ligne"] for l in lignes] == [TENT, FICHE, FICHE]
        for l in lignes:
            assert set(l) == set(rg3.CHAMPS_LIGNE) | {"rang", "precedente", "version"}
            assert l["version"] == rg3.VERSION_LIGNE and l["classe_issue"] == pt.FICHES_RENDUES
            assert l["espece"] == "espece-1" and l["rang_repli"] == 0 and l["categorie_refus"] is None
        assert all(lignes[0][c] is None for c in rg3.CHAMPS_DE_FICHE)
        f = lignes[1]
        assert f["nom"] == f["identifiant"] and f["enonce"] == "Idée factice, inerte, sur deux lignes."
        assert f["filiation"] is None  # « aucune »
        assert all(lignes[2][c] is None for c in ("nom", "enonce", "filiation", "etage_de_lecture"))

    def test_filiation_gardee_telle_quelle(self, dossier):
        r = A.registre(dossier)
        mere = A.mot_fiche(77)
        l1 = r.ajouter_chaine([A.tentative()], [A.issue(1, filiation=mere)])[1]
        l2 = r.ajouter_chaine([A.tentative(case=A.CASES[1])], [A.issue(2, case=A.CASES[1], filiation="Aucune ")])[1]
        assert l1["filiation"] == mere and l2["filiation"] == "Aucune "  # jamais normalisée : M1 bis en juge

    def test_chaine_a_un_repli_servi_avec_fiche(self, dossier):
        r = A.registre(dossier)
        lignes = r.ajouter_chaine([A.refus(0), A.tentative(1)], [A.issue(1)])
        assert [(l["type_ligne"], l["rang_repli"]) for l in lignes] == [(TENT, 0), (TENT, 1), (FICHE, 1)]
        assert lignes[0]["classe_issue"] == rg3.REFUS_SERVI_PAR_REPLI and lignes[0]["raison_arret"] == "refusal"
        assert lignes[0]["categorie_refus"] == "categorie-factice"
        assert lignes[2]["modele_servi"] == A.SERVI_REPLI and lignes[2]["classe"] == pt.PASSEE

    def test_chaine_a_deux_replis_servie_sans_fiche(self, dossier):
        r = A.registre(dossier)
        lignes = r.ajouter_chaine([A.refus(0), A.refus(1), A.tentative(2, classe_issue=pt.ILLISIBLE)])
        assert [l["classe_issue"] for l in lignes] == [rg3.REFUS_SERVI_PAR_REPLI] * 2 + [pt.ILLISIBLE]

    def test_trois_refus_chaine_finie_arret_1(self, dossier):
        r = A.registre(dossier)
        lignes = r.ajouter_chaine(trois_refus())
        assert [l["classe_issue"] for l in lignes] == [pt.REFUS_DU_MODELE] * 3
        ch = rg3.chaines_de(A.lire(r.chemin), r.contexte)
        assert ch[0].fin == "trois refus" and not ch[0].derniere.fiches

    def test_tentative_sans_reponse(self, dossier):
        r = A.registre(dossier)
        lignes = r.ajouter_chaine([A.refus(0, classe_issue=rg3.CLASSE_SANS_REPONSE), sans_reponse(1, cout=6.05)])
        assert lignes[1]["modele_servi"] is None and lignes[1]["raison_arret"] == "sans_reponse"
        r.ajouter_chaine([sans_reponse(0, case=A.CASES[1])])
        assert [c.fin for c in rg3.chaines_de(A.lire(r.chemin), r.contexte)] == ["sans réponse", "sans réponse"]

    def test_role_non_proposeur_servi_par_repli(self, dossier):
        r = A.registre(dossier)
        r.ajouter_chaine([A.refus(0, espece="portier"), A.tentative(1, espece="portier", classe_issue=pt.VIDE_MOTIVEE)])
        ch = rg3.chaines_de(A.lire(r.chemin), r.contexte)
        assert ch[0].par_repli and ch[0].derniere["modele_servi"] == A.SERVI_REPLI

    def test_categorie_absente_vaut_null_donnee_gardee(self, dossier):
        r = A.registre(dossier)
        t = A.refus(0)
        del t["categorie_refus"]
        l = r.ajouter_chaine([t, A.tentative(1, classe_issue=pt.VIDE_MOTIVEE)])
        assert l[0]["categorie_refus"] is None

    def test_requete_sans_case_hors_proposeur(self, dossier):
        r = A.registre(dossier)
        l = r.ajouter_chaine([A.tentative(espece="passe-x", case=None, classe_issue=pt.ILLISIBLE)])
        assert l[0]["case"] is None

    def test_cout_entier_ou_decimal(self, dossier):
        r = A.registre(dossier)
        r.ajouter_chaine([A.tentative(cout=0, classe_issue=pt.VIDE_MOTIVEE)])
        r.ajouter_chaine([A.tentative(case=A.CASES[1], cout=6.05, classe_issue=pt.REFUS_DU_MODELE)])

    def test_deux_chaines_successives_a_fiches(self, dossier):
        r = A.registre(dossier)
        r.ajouter_chaine([A.tentative()], [A.issue(1)])
        r.ajouter_chaine([A.tentative()], [A.issue(2)])
        assert len(rg3.chaines_de(A.lire(r.chemin), r.contexte)) == 2


# --- écriture : artefacts, une garde chacun ---------------------------------------------------------------------------

class TestEcritureArtefacts:
    def test_champ_manquant(self, dossier):
        r = A.registre(dossier)
        t = A.tentative()
        del t["cout_compte_usd"]
        refuse(r, [t], [A.issue(1)], "incomplète")

    def test_champ_en_plus(self, dossier):
        refuse(A.registre(dossier), [A.tentative(note=3)], [A.issue(1)], "hors de la liste fermée")

    @pytest.mark.parametrize("espece", ["espece-6", "Espece-1", None, "juge-3"])
    def test_espece_hors_liste(self, dossier, espece):
        refuse(A.registre(dossier), [A.tentative(espece=espece, classe_issue=pt.ILLISIBLE)], (), "espèce")

    @pytest.mark.parametrize("classe", ["fiche rendue", "refus par classifieur", None])
    def test_classe_issue_hors_liste(self, dossier, classe):
        refuse(A.registre(dossier), [A.tentative(classe_issue=classe)], (), "classe d'issue")

    def test_case_hors_des_cases_servies(self, dossier):
        r = A.registre(dossier, cases_servies=A.CASES[:2])
        refuse(r, [A.tentative(case=A.CASES[3], classe_issue=pt.ILLISIBLE)], (), "case hors")

    def test_proposeur_sans_case(self, dossier):
        refuse(A.registre(dossier), [A.tentative(case=None, classe_issue=pt.ILLISIBLE)], (), "sans case")

    @pytest.mark.parametrize("rang", [3, -1, True, "0", 1.0])
    def test_rang_hors_liste(self, dossier, rang):
        t = A.tentative(classe_issue=pt.ILLISIBLE, modele=A.MODELES[0])
        t["rang_repli"] = rang
        refuse(A.registre(dossier), [t], (), "rang")

    def test_modele_demande_hors_des_identifiants_par_role(self, dossier):
        refuse(A.registre(dossier), [A.tentative(modele="un-autre-identifiant", classe_issue=pt.ILLISIBLE)], (),
               "modèle demandé")

    @pytest.mark.parametrize("valeur", [None, "", " a", "a\nb", 3])
    def test_modele_servi_absent_ou_mal_forme(self, dossier, valeur):
        t = A.tentative(classe_issue=pt.ILLISIBLE)
        t["modele_servi"] = valeur
        refuse(A.registre(dossier), [t], (), "modèle servi")

    @pytest.mark.parametrize("valeur", [None, "", "end_turn\n"])
    def test_raison_d_arret_absente_ou_mal_formee(self, dossier, valeur):
        t = A.tentative(classe_issue=pt.ILLISIBLE)
        t["raison_arret"] = valeur
        refuse(A.registre(dossier), [t], (), "raison d'arrêt")

    def test_sans_reponse_avec_un_modele_servi(self, dossier):
        t = sans_reponse(0)
        t["modele_servi"] = A.SERVI
        refuse(A.registre(dossier), [t], (), "modèle servi null")

    @pytest.mark.parametrize("classe", [pt.VIDE_MOTIVEE, pt.REFUS_DU_MODELE, pt.FICHES_RENDUES])
    def test_sans_reponse_d_une_autre_classe(self, dossier, classe):
        t = sans_reponse(0)
        t["classe_issue"] = classe
        refuse(A.registre(dossier), [t], (), "réponse illisible")

    @pytest.mark.parametrize("valeur", [3, "", ["x"]])
    def test_categorie_mal_formee(self, dossier, valeur):
        refuse(A.registre(dossier), [A.refus(0, categorie_refus=valeur), A.tentative(1, classe_issue=pt.ILLISIBLE)], (),
               "catégorie")

    @pytest.mark.parametrize("cout", [-0.01, math.nan, math.inf, True, "0.25", None])
    def test_cout_hors_forme(self, dossier, cout):
        refuse(A.registre(dossier), [A.tentative(cout=cout, classe_issue=pt.ILLISIBLE)], (), "coût")

    def test_refusal_d_une_autre_classe(self, dossier):
        refuse(A.registre(dossier), [A.tentative(raison="refusal", classe_issue=pt.VIDE_MOTIVEE)], (), "raison d'arrêt `refusal`")

    def test_classe_de_repli_sans_refusal(self, dossier):
        refuse(A.registre(dossier),
               [A.tentative(classe_issue=rg3.REFUS_SERVI_PAR_REPLI), A.tentative(1, classe_issue=pt.ILLISIBLE)], (),
               "classe de repli sans")

    def test_troisieme_refus_dit_servi_par_repli(self, dossier):
        refuse(A.registre(dossier), [A.refus(0), A.refus(1), A.refus(2)], (), "troisième refus")

    def test_trois_refus_aux_classes_melees(self, dossier):
        t = trois_refus()
        t[0] = A.refus(0)
        refuse(A.registre(dossier), t, (), "chaîne de trois refus")

    def test_refus_servi_marque_refus_du_modele(self, dossier):
        refuse(A.registre(dossier), [A.refus(0, classe_issue=pt.REFUS_DU_MODELE), A.tentative(1, classe_issue=pt.ILLISIBLE)],
               (), "servi par repli")

    def test_trois_refus_avec_fiches(self, dossier):
        refuse(A.registre(dossier), trois_refus(), [A.issue(1)], "pas « fiches rendues »")

    def test_chaine_non_close(self, dossier):
        r = A.registre(dossier)
        refuse(r, [A.refus(0)], (), "non close")
        refuse(r, [A.refus(0), A.refus(1)], (), "non close")
        refuse(r, [A.refus(0, classe_issue=pt.REFUS_DU_MODELE)], (), "non close")

    def test_rangs_rompus(self, dossier):
        r = A.registre(dossier)
        refuse(r, [A.refus(0), A.tentative(2, classe_issue=pt.ILLISIBLE)], (), "repli sans le refus")
        refuse(r, [A.tentative(1, classe_issue=pt.ILLISIBLE)], (), "repli sans le refus")
        refuse(r, [A.tentative(0, classe_issue=pt.ILLISIBLE), A.tentative(0, case=A.CASES[1], classe_issue=pt.ILLISIBLE)],
               (), "rang 0")

    def test_repli_d_une_autre_espece_ou_case(self, dossier):
        r = A.registre(dossier)
        refuse(r, [A.refus(0), A.tentative(1, espece="espece-2", classe_issue=pt.ILLISIBLE)], (), "repli sans le refus")
        refuse(r, [A.refus(0), A.tentative(1, case=A.CASES[1], classe_issue=pt.ILLISIBLE)], (), "repli sans le refus")

    def test_fiches_et_classe_fiches_rendues_vont_ensemble(self, dossier):
        r = A.registre(dossier)
        refuse(r, [A.tentative(classe_issue=pt.ILLISIBLE)], [A.issue(1)], "pas « fiches rendues »")
        refuse(r, [A.tentative()], (), "sans ligne de fiche")

    def test_fiche_d_une_espece_qui_n_est_pas_un_proposeur(self, dossier):
        refuse(A.registre(dossier), [A.tentative(espece="portier")], [A.issue(1)], "espèce de proposeur")

    def test_fiche_d_une_autre_case_ou_generation(self, dossier):
        r = A.registre(dossier)
        refuse(r, [A.tentative()], [A.issue(1, case=A.CASES[1])], "autre case")
        refuse(r, [A.tentative()], [A.issue(1, generation=2)], "autre génération")

    def test_fiche_qui_n_est_pas_classee_par_le_portier(self, dossier):
        refuse(A.registre(dossier), [A.tentative()], [{"identifiant": A.mot_fiche(1)}], "classée par le portier")

    def test_fiche_passee_sans_filiation_en_chaine(self, dossier):
        refuse(A.registre(dossier), [A.tentative()], [A.issue(1, filiation=None)], "filiation")

    def test_identifiant_de_fiche_deux_fois(self, dossier):
        r = A.registre(dossier)
        r.ajouter_chaine([A.tentative()], [A.issue(1)])
        refuse(r, [A.tentative(case=A.CASES[1])], [A.issue(1, case=A.CASES[1])], "deux fois")
        refuse(r, [A.tentative(case=A.CASES[2])], [A.issue(5, case=A.CASES[2]), A.issue(5, case=A.CASES[2])], "deux fois")

    @pytest.mark.parametrize("n", [0, 4])
    def test_chaine_de_zero_ou_quatre_tentatives(self, dossier, n):
        refuse(A.registre(dossier), [A.refus(0)] * n, (), "une à trois")

    def test_tentative_qui_n_est_pas_un_dictionnaire(self, dossier):
        refuse(A.registre(dossier), [("espece-1",)], (), "dictionnaire")

    def test_ecriture_directe_refusee(self, dossier):
        r = A.registre(dossier)
        with pytest.raises(rg3.RegistreRefuse, match="écriture directe"):
            r.ajouter({c: None for c in rg3.CHAMPS_LIGNE})
        assert A.taille(r.chemin) == 0

    def test_ajouter_fiche_du_v1_refuse_en_le_disant(self, dossier):
        r = A.registre(dossier)
        with pytest.raises(rg3.RegistreAncienFormat, match="ancien format"):
            r.ajouter_fiche(A.issue(1))
        assert A.taille(r.chemin) == 0


class TestContexte:
    def test_sain(self, dossier):
        c = rg3.contexte_de(generation=2, cases_servies=A.CASES, modeles_demandes=A.MODELES)
        assert c.generation == 2 and c.cases_servies == tuple(A.CASES)

    @pytest.mark.parametrize("kw,motif", [
        ({"generation": 4}, "génération"), ({"generation": True}, "génération"),
        ({"cases_servies": []}, "cases servies"), ({"cases_servies": ["pas-un-mot"]}, "trois syllabes"),
        ({"cases_servies": None}, "cases servies"), ({"modeles_demandes": ()}, "identifiants par rôle"),
        ({"modeles_demandes": ("a", "a")}, "identifiants par rôle"), ({"modeles_demandes": ("a\nb",)}, "identifiants")])
    def test_artefacts(self, dossier, kw, motif):
        base = {"generation": 1, "cases_servies": A.CASES, "modeles_demandes": A.MODELES}
        base.update(kw)
        with pytest.raises(rg3.RegistreRefuse, match=motif):
            rg3.contexte_de(**base)

    def test_case_servie_deux_fois(self):
        with pytest.raises(rg3.RegistreRefuse, match="deux fois"):
            rg3.contexte_de(generation=1, cases_servies=[A.CASES[0]] * 2, modeles_demandes=A.MODELES)

    def test_le_registre_refuse_avant_de_creer_son_fichier(self, dossier):
        with pytest.raises(rg3.RegistreRefuse):
            A.registre(dossier, generation=0)
        assert os.listdir(dossier) == []


# --- relecture ----------------------------------------------------------------------------------------------------------

class Brut(pt.FichierAjoutSeul):
    """Un écrivain d'essai, sans garde : il fabrique les fichiers que le registre v3 doit refuser à la relecture."""

    CHAMPS_PERMIS = rg3.CHAMPS_LIGNE
    VERSION = rg3.VERSION_LIGNE


def ligne_tentative(**k):
    l = {c: None for c in rg3.CHAMPS_LIGNE}
    l.update({"type_ligne": TENT, "generation": 1, "espece": "espece-1", "case": A.CASES[0], "rang_repli": 0,
              "modele_demande": A.MODELES[0], "modele_servi": A.SERVI, "raison_arret": "end_turn", "cout_compte_usd": 0.1,
              "classe_issue": pt.ILLISIBLE})
    l.update(k)
    return l


def ligne_fiche(**k):
    base = dict(type_ligne=FICHE, classe=pt.AU_COFFRE, identifiant=A.mot_fiche(1), classe_issue=pt.FICHES_RENDUES)
    base.update(k)
    return ligne_tentative(**base)


def brut(dossier, nom, *lignes):
    b = Brut(dossier, nom)
    for l in lignes:
        b.ajouter(l)
    return b.chemin


class TestRelecture:
    def test_saine_avec_sceau(self, dossier):
        r = A.registre(dossier)
        r.ajouter_chaine([A.refus(0), A.tentative(1)], [A.issue(1), A.issue(2, pt.HORS_CASE)])
        r.ajouter_chaine([A.tentative(case=A.CASES[1], classe_issue=pt.VIDE_MOTIVEE)])
        r.sceller()
        lignes = A.lire(r.chemin, exiger_sceau=True)
        assert len(lignes) == 5
        ch = rg3.chaines_de(lignes, r.contexte)
        assert len(ch) == 2 and ch[0].par_repli and len(ch[0].derniere.fiches) == 2 and not ch[1].par_repli

    def test_ancien_format_dit_clairement(self, dossier):
        v1 = rg.RegistreTentatives(dossier, "registre-v1.jsonl")
        v1.ajouter_fiche(A.issue(1))
        with pytest.raises(rg3.RegistreAncienFormat) as e:
            A.lire(v1.chemin)
        assert "ancien format" in str(e.value) and rg3.VERSION_LIGNE in str(e.value)

    def test_ancien_format_vide_se_relit_vide(self, dossier):
        v1 = rg.RegistreTentatives(dossier, "registre-v1-vide.jsonl")
        assert A.lire(v1.chemin) == ()

    def test_version_inconnue(self, dossier):
        class Autre(Brut):
            VERSION = "registre-tentatives-na-v9"
        b = Autre(dossier, "autre.jsonl")
        b.ajouter(ligne_tentative())
        with pytest.raises(rg3.RegistreRefuse, match="version"):
            A.lire(b.chemin)

    def test_lignes_saines_brutes_relues(self, dossier):
        passee = dict(classe=pt.PASSEE, nom=A.mot_fiche(1), ce_que_le_moniteur_suppose="a", menace_du_programme="b",
                      etage_de_lecture="c", enonce="un deux", classe_issue=pt.FICHES_RENDUES)
        assert len(A.lire(brut(dossier, "sain.jsonl", ligne_tentative(classe_issue=pt.FICHES_RENDUES),
                               ligne_fiche(**passee)))) == 2

    def test_ligne_incomplete_au_fichier(self, dossier):
        l = ligne_tentative()
        del l["categorie_refus"]
        with pytest.raises(rg3.RegistreRefuse, match="incomplète"):
            A.lire(brut(dossier, "incomplet.jsonl", l))

    @pytest.mark.parametrize("valeur", ["autre", None, "Fiche"])
    def test_type_de_ligne_hors_liste(self, dossier, valeur):
        with pytest.raises(rg3.RegistreRefuse, match="type de ligne"):
            A.lire(brut(dossier, "type.jsonl", ligne_tentative(type_ligne=valeur)))

    def test_ligne_sans_type_dite_ancien_format(self, dossier):
        l = ligne_tentative()
        del l["type_ligne"]
        c = rg3.contexte_de(generation=1, cases_servies=A.CASES, modeles_demandes=A.MODELES)
        with pytest.raises(rg3.RegistreAncienFormat):
            rg3.verifier_ligne(l, c)

    def test_fiche_sans_sa_tentative_juste_avant(self, dossier):
        with pytest.raises(rg3.RegistreRefuse, match="sans la ligne de sa tentative"):
            A.lire(brut(dossier, "seule.jsonl", ligne_fiche()))
        with pytest.raises(rg3.RegistreRefuse, match="sans la ligne de sa tentative"):
            A.lire(brut(dossier, "autre-cout.jsonl", ligne_tentative(classe_issue=pt.FICHES_RENDUES), ligne_fiche(cout_compte_usd=9)))

    def test_tentative_fiches_rendues_sans_fiche_au_fichier(self, dossier):
        with pytest.raises(rg3.RegistreRefuse, match="sans ligne de fiche"):
            A.lire(brut(dossier, "vide.jsonl", ligne_tentative(classe_issue=pt.FICHES_RENDUES)))

    def test_refus_pendant_au_fichier(self, dossier):
        with pytest.raises(rg3.RegistreRefuse, match="non close"):
            A.lire(brut(dossier, "pendant.jsonl", ligne_tentative(raison_arret="refusal",
                                                                  classe_issue=rg3.REFUS_SERVI_PAR_REPLI)))

    def test_generation_autre_au_fichier(self, dossier):
        with pytest.raises(rg3.RegistreRefuse, match="génération"):
            A.lire(brut(dossier, "gen.jsonl", ligne_tentative()), generation=2)

    def test_tentative_aux_champs_de_fiche_non_null(self, dossier):
        with pytest.raises(rg3.RegistreRefuse, match="champs de fiche sont null"):
            A.lire(brut(dossier, "tent-mal.jsonl", ligne_tentative(etage_de_lecture="x")))

    def test_fiche_non_passee_qui_porte_un_enonce(self, dossier):
        with pytest.raises(rg3.RegistreRefuse, match="fiche non passée"):
            A.lire(brut(dossier, "coffre-mal.jsonl", ligne_fiche(enonce="x")))

    def test_fiche_au_mauvais_identifiant(self, dossier):
        for i, v in enumerate(("pas-un-mot", None)):
            with pytest.raises(rg3.RegistreRefuse, match="dix-huit lettres"):
                A.lire(brut(dossier, f"ident-mal-{i}.jsonl", ligne_fiche(identifiant=v)))

    def test_fiche_passee_enonce_sur_deux_lignes_ou_nom_autre(self, dossier):
        base = dict(classe=pt.PASSEE, nom=A.mot_fiche(1), ce_que_le_moniteur_suppose="a", menace_du_programme="b",
                    etage_de_lecture="c", enonce="un deux")
        for i, k in enumerate(({"enonce": "un\ndeux"}, {"nom": A.mot_fiche(2)}, {"filiation": 3})):
            with pytest.raises(rg3.RegistreRefuse, match="fiche passée|filiation"):
                A.lire(brut(dossier, f"passee-mal-{i}.jsonl", ligne_fiche(**dict(base, **k))))

    def test_classe_de_fiche_hors_liste(self, dossier):
        with pytest.raises(rg3.RegistreRefuse, match="classe de fiche"):
            A.lire(brut(dossier, "classe-mal.jsonl", ligne_fiche(classe="gardée")))

    def test_ligne_v1_donnee_a_verifier_ligne(self):
        c = rg3.contexte_de(generation=1, cases_servies=A.CASES, modeles_demandes=A.MODELES)
        with pytest.raises(rg3.RegistreAncienFormat):
            rg3.verifier_ligne({"identifiant": A.mot_fiche(1), "generation": 1, "case": A.CASES[0], "classe": "au coffre"}, c)


class TestComptesParType:
    def test_un_cout_et_un_appel_par_tentative(self, dossier):
        r = A.registre(dossier)
        r.ajouter_chaine([A.refus(0, cout=0.5), A.tentative(1, cout=2.0)], [A.issue(k) for k in (1, 2, 3)])
        r.ajouter_chaine([A.tentative(case=A.CASES[1], cout=1.0)], [A.issue(4, case=A.CASES[1])])
        lignes = A.lire(r.chemin)
        assert len(lignes) == 7
        t = rg3.lignes_tentative(lignes)
        assert [l["cout_compte_usd"] for l in t] == [0.5, 2.0, 1.0]
        assert len(rg3.lignes_fiche(lignes)) == 4

    def test_lignes_non_relues_refusees(self, dossier):
        with pytest.raises(rg3.RegistreRefuse, match="relue"):
            rg3.lignes_fiche([ligne_tentative()])  # sans `version` : pas une ligne relue
        with pytest.raises(rg3.RegistreRefuse, match="relue"):
            rg3.lignes_tentative([dict(ligne_tentative(type_ligne="autre"), version=rg3.VERSION_LIGNE)])


# --- différentiel avec le v1 --------------------------------------------------------------------------------------------

def issues_g1():
    c = A.CASES
    return [A.issue(1, case=c[0]), A.issue(2, case=c[1], etage_de_lecture="étage factice deux"),
            A.issue(3, pt.AU_COFFRE, case=c[0]), A.issue(4, pt.HORS_CASE, case=c[2]), A.issue(5, case=c[2])]


def ecrire_v1_v2(dossier, avec_sans_fiche=True, repli_sur=None):
    """Les mêmes fiches au registre v1 et au registre v3 (une chaîne par case, `repli_sur` servie par repli), dans le même
    ordre ; des chaînes sans fiche en plus au v3."""
    v1 = rg.RegistreTentatives(dossier, "v1.jsonl")
    v2 = A.registre(dossier, nom="v3.jsonl")
    par_case = {}
    for i in issues_g1():
        par_case.setdefault(i.identifiant_case, []).append(i)
    for case, fiches in par_case.items():
        for i in fiches:
            v1.ajouter_fiche(i)
        if case == repli_sur:
            v2.ajouter_chaine([A.refus(0, case=case), A.tentative(1, case=case)], fiches)
        else:
            v2.ajouter_chaine([A.tentative(case=case)], fiches)
    if avec_sans_fiche:
        v2.ajouter_chaine([A.tentative(espece="espece-2", case=A.CASES[3], classe_issue=pt.VIDE_MOTIVEE)])
        v2.ajouter_chaine([A.refus(0, espece="espece-3"), A.tentative(1, espece="espece-3", classe_issue=pt.ILLISIBLE)])
        v2.ajouter_chaine(trois_refus(espece="espece-4"))
        v2.ajouter_chaine([sans_reponse(0, espece="espece-5")])
        v2.ajouter_chaine([A.tentative(espece="portier", modele=A.MODELES[3], classe_issue=pt.ILLISIBLE)])
    v1.sceller()
    v2.sceller()
    return rg.lire_registre_tentatives(v1.chemin, exiger_sceau=True), A.lire(v2.chemin, exiger_sceau=True)


def sans_marques(octets):
    return re.sub(r" ; par_repli : (?:vrai|faux)(?= ; )", "", octets.decode("utf-8")).encode("utf-8")


SANS_FICHIER = lambda ls: [{k: v for k, v in l.items() if k not in ("rang", "precedente", "version")} for l in ls]  # noqa: E731


class TestDifferentielV1:
    def test_lignes_de_fiche_egales_a_la_forme_v1(self, dossier):
        l1, l2 = ecrire_v1_v2(dossier)
        assert rg3.lignes_v1_de(l2) == SANS_FICHIER(l1)

    @pytest.mark.parametrize("permuter", [True, False])
    @pytest.mark.parametrize("repli", [False, True])
    def test_registre_servi_egal_a_l_octet(self, dossier, permuter, repli):
        l1, l2 = ecrire_v1_v2(dossier, repli_sur=A.CASES[0] if repli else None)
        cases = {1: list(A.CASES)}
        s1 = rg.fabriquer_registre_servi(l1, cases, 2, permuter_comptes=permuter, racine=RACINE, racine_attendue=RACINE)
        s2 = rg3.fabriquer_registre_servi_v3(l2, cases, 2, permuter_comptes=permuter, racine=RACINE, racine_attendue=RACINE)
        assert sans_marques(s2.octets) == s1.octets and s2.lignes_tentative == 3 and s2.lignes_compte == 8
        assert s2.sha256 == A.sha(s2.octets) and s2.taille == len(s2.octets)
        assert rg3.marques_par_repli(s2) == ((A.mot_fiche(1),) if repli else ())
        brut_ = s2.octets.decode("utf-8")
        for interdit in ("espece", "id-role", "servi-factice", "refusal", "categorie", "0.25", "tentative\"", "fiche\""):
            assert interdit not in brut_
        assert vr3.verifier_registre_servi_v3(s2.octets, borne_registre_octets=64000, borne_enonce_octets=1200).taille \
            == len(s2.octets)

    def test_lignes_de_tentative_ne_changent_rien(self, dossier):
        _, l2 = ecrire_v1_v2(dossier, avec_sans_fiche=True)
        cases = {1: list(A.CASES)}
        s2 = rg3.fabriquer_registre_servi_v3(l2, cases, 2, permuter_comptes=True, racine=RACINE, racine_attendue=RACINE)
        fiches = rg3.lignes_fiche(l2)
        s2f = rg3.fabriquer_registre_servi_v3(fiches, cases, 2, permuter_comptes=True, racine=RACINE, racine_attendue=RACINE)
        assert s2 == s2f and len(fiches) < len(l2)

    def test_generation_3_sur_deux_generations(self, tmp_path):
        d1, d2 = tmp_path / "g1", tmp_path / "g2"
        d1.mkdir()
        d2.mkdir()
        _, l2g1 = ecrire_v1_v2(str(d1))
        c2 = A.cases(3, depart=3000)
        v2 = A.registre(str(d2), nom="v3-g2.jsonl", generation=2, cases_servies=c2)
        v1 = rg.RegistreTentatives(str(d2), "v1-g2.jsonl")
        for k, c in enumerate(c2):
            i = A.issue(100 + k, case=c, generation=2, classe=pt.PASSEE if k else pt.AU_COFFRE)
            v1.ajouter_fiche(i)
            v2.ajouter_chaine([A.tentative(case=c)], [i])
        l1g1 = rg.lire_registre_tentatives(os.path.join(str(d1), "v1.jsonl"))
        l2g2 = A.lire(v2.chemin, generation=2, cases_servies=c2)
        cases = {1: list(A.CASES), 2: c2}
        s1 = rg.fabriquer_registre_servi(list(l1g1) + list(rg.lire_registre_tentatives(v1.chemin)), cases, 3,
                                         permuter_comptes=False, racine=RACINE, racine_attendue=RACINE)
        s2 = rg3.fabriquer_registre_servi_v3(list(l2g1) + list(l2g2), cases, 3, permuter_comptes=False, racine=RACINE,
                                             racine_attendue=RACINE)
        assert sans_marques(s2.octets) == s1.octets and s2.lignes_tentative == 5

    def test_garde_du_coffre_egale_sur_les_seules_lignes_de_fiche(self, dossier):
        l1, l2 = ecrire_v1_v2(dossier)
        for g in (1, 2, 3):
            assert rg.garde_du_coffre(l1, g) == rg3.garde_du_coffre_v3(l2, g)
        assert rg3.garde_du_coffre_v3(l2, 1).rendues == 5
        # Erratum 1, point 4 : le code du v1, sur toutes les lignes du v3, compterait les lignes de tentative.
        assert rg.garde_du_coffre(l2, 1).rendues == len(l2) > 5

    def test_garde_du_coffre_compte_les_fiches_par_repli_et_arrete(self, dossier):
        r = A.registre(dossier)
        r.ajouter_chaine([A.tentative()], [A.issue(1), A.issue(2), A.issue(3)])
        r.ajouter_chaine([A.refus(0, case=A.CASES[1]), A.tentative(1, case=A.CASES[1])],
                         [A.issue(4, pt.AU_COFFRE, case=A.CASES[1])])
        assert rg3.garde_du_coffre_v3(A.lire(r.chemin), 1).rendues == 4  # 1 sur 4 : pas strictement plus d'un quart
        r.ajouter_chaine([A.tentative(case=A.CASES[2])], [A.issue(5, pt.AU_COFFRE, case=A.CASES[2])])
        with pytest.raises(rg.ArretGardeCoffre):
            rg3.garde_du_coffre_v3(A.lire(r.chemin), 1)

    def test_garde_du_coffre_ne_dilue_pas_par_les_tentatives(self, dossier):
        r = A.registre(dossier)
        r.ajouter_chaine([A.tentative()], [A.issue(1), A.issue(2, pt.AU_COFFRE)])
        for k, e in enumerate(("espece-2", "espece-3", "espece-4", "espece-5")):
            r.ajouter_chaine([A.tentative(espece=e, classe_issue=pt.VIDE_MOTIVEE)])
        with pytest.raises(rg.ArretGardeCoffre):  # 1 au coffre sur 2 fiches ; les 5 lignes de tentative n'y entrent pas
            rg3.garde_du_coffre_v3(A.lire(r.chemin), 1)
        assert not rg.garde_du_coffre(A.lire(r.chemin), 1).depasse  # le v1 sur toutes les lignes : garde diluée

    def test_v1_donne_aux_fonctions_v3_refuse_en_le_disant(self, dossier):
        l1, _ = ecrire_v1_v2(dossier)
        with pytest.raises(rg3.RegistreAncienFormat, match="ancien format"):
            rg3.fabriquer_registre_servi_v3(l1, {1: list(A.CASES)}, 2, permuter_comptes=True, racine=RACINE,
                                            racine_attendue=RACINE)
        with pytest.raises(rg3.RegistreAncienFormat, match="ancien format"):
            rg3.garde_du_coffre_v3(l1, 1)

    def test_ligne_non_relue_refusee_par_les_fonctions_v3(self, dossier):
        _, l2 = ecrire_v1_v2(dossier)
        nue = {k: v for k, v in l2[0].items() if k != "version"}
        with pytest.raises(rg3.RegistreRefuse, match="relue"):
            rg3.lignes_v1_de([nue])

    def test_le_v1_n_est_pas_touche(self, dossier):
        l1, _ = ecrire_v1_v2(dossier)
        assert all(set(l) <= set(rg.RegistreTentatives.CHAMPS_PERMIS) | {"rang", "precedente", "version"} for l in l1)
        assert json.dumps(rg.RegistreTentatives.CHAMPS_PERMIS) == json.dumps(rg3.CHAMPS_V1)


# --- erratum 2, (b) : refus, puis tentative sans réponse -------------------------------------------------------------

class TestRefusPuisSansReponse:
    def test_sain_classe_de_defaut_aux_refus(self, dossier):
        r = A.registre(dossier)
        r.ajouter_chaine([A.refus(0, classe_issue=rg3.CLASSE_SANS_REPONSE),
                          A.refus(1, classe_issue=rg3.CLASSE_SANS_REPONSE), sans_reponse(2)])
        ch = rg3.chaines_de(A.lire(r.chemin), r.contexte)
        assert ch[0].fin == "sans réponse"
        assert {t["classe_issue"] for t in ch[0].tentatives} == {rg3.CLASSE_SANS_REPONSE}
        assert rg3.REFUS_SERVI_PAR_REPLI not in {t["classe_issue"] for t in ch[0].tentatives}

    def test_artefact_refus_dit_servi_par_repli(self, dossier):
        refuse(A.registre(dossier), [A.refus(0), sans_reponse(1)], (), "jamais « servi par repli »")
        refuse(A.registre(dossier, nom="b.jsonl"), [A.refus(0, classe_issue=rg3.CLASSE_SANS_REPONSE), A.refus(1),
                                                    sans_reponse(2)], (), "jamais « servi par repli »")

    def test_artefact_classe_de_defaut_avant_un_repli_servi(self, dossier):
        refuse(A.registre(dossier), [A.refus(0, classe_issue=rg3.CLASSE_SANS_REPONSE), A.tentative(1)], [A.issue(1)],
               "servi par repli")

    def test_artefact_classe_de_defaut_dans_trois_refus(self, dossier):
        t = trois_refus()
        t[0] = A.refus(0, classe_issue=rg3.CLASSE_SANS_REPONSE)
        refuse(A.registre(dossier), t, (), "chaîne de trois refus")

    def test_artefact_fichier_v2_dit_ancien_format(self, dossier):
        class V2(Brut):
            VERSION = "registre-tentatives-na-v2"
        b = V2(dossier, "v2.jsonl")
        b.ajouter(ligne_tentative())
        with pytest.raises(rg3.RegistreAncienFormat, match="lot 5 v2"):
            A.lire(b.chemin)


# --- erratum 2, (d) : registre servi marqué `par_repli` ----------------------------------------------------------------

def servi_marque(dossier, repli=True):
    _, l3 = ecrire_v1_v2(dossier, repli_sur=A.CASES[0] if repli else None)
    return rg3.fabriquer_registre_servi_v3(l3, {1: list(A.CASES)}, 2, permuter_comptes=True, racine=RACINE,
                                           racine_attendue=RACINE)


def verifier3(octets, **kw):
    kw.setdefault("borne_registre_octets", 64000)
    kw.setdefault("borne_enonce_octets", 1200)
    return vr3.verifier_registre_servi_v3(octets, **kw)


class TestRegistreServiMarque:
    def test_sain_chaque_ligne_passee_porte_sa_marque(self, dossier):
        s = servi_marque(dossier)
        t = [l for l in s.octets.decode("utf-8").splitlines() if l.startswith(rg.TETE_TENTATIVE)]
        assert len(t) == 3
        vrai = [l for l in t if " ; passée ; par_repli : vrai ; " in l]
        faux = [l for l in t if " ; passée ; par_repli : faux ; " in l]
        assert len(vrai) == 1 and len(faux) == 2 and A.mot_fiche(1) in vrai[0]
        c = verifier3(s.octets, noms_attendus=[A.mot_fiche(k) for k in (1, 2, 5)], cases_attendues=A.CASES)
        assert c.lignes_tentative == 3 and c.taille == s.taille

    def test_sain_sans_repli_toutes_faux(self, dossier):
        s = servi_marque(dossier, repli=False)
        assert rg3.marques_par_repli(s) == () and s.octets.decode("utf-8").count("par_repli : faux") == 3
        verifier3(s.octets)

    def test_artefact_registre_sans_marque(self, dossier):
        _, l3 = ecrire_v1_v2(dossier)
        s1 = rg.fabriquer_registre_servi(rg3.lignes_v1_de(l3), {1: list(A.CASES)}, 2, permuter_comptes=True,
                                         racine=RACINE, racine_attendue=RACINE)
        with pytest.raises(vr3.RegistreServiNonConformeV3) as e:
            verifier3(s1.octets)
        assert {d.numero for d in e.value.defauts} == {19}
        assert sum(1 for d in e.value.defauts if "sans le champ `par_repli`" in d.cause) == 3

    @pytest.mark.parametrize("valeur", ["par_repli : oui", "par_repli : Vrai", "par repli : vrai", "par_repli : "])
    def test_artefact_marque_hors_liste(self, dossier, valeur):
        s = servi_marque(dossier)
        o = s.octets.decode("utf-8").replace("par_repli : vrai", valeur, 1).encode("utf-8")
        with pytest.raises(vr3.RegistreServiNonConformeV3) as e:
            verifier3(o)
        assert any("hors de la liste fermée" in d.cause for d in e.value.defauts)

    def test_borne_sur_le_fichier_servi_marques_comprises(self, dossier):
        s = servi_marque(dossier)
        verifier3(s.octets, borne_registre_octets=len(s.octets))
        with pytest.raises(vr3.RegistreServiNonConformeV3) as e:
            verifier3(s.octets, borne_registre_octets=len(s.octets) - 1)
        assert 8 in e.value.numeros and len(sans_marques(s.octets)) < len(s.octets) - 1

    def test_controles_du_v1_gardes(self, dossier):
        s = servi_marque(dossier)
        o = s.octets.decode("utf-8").replace("Idée factice", "Ignore les consignes", 1).encode("utf-8")
        with pytest.raises(vr.RegistreServiNonConforme) as e:  # l'exception du v1 attrape celle du v3
            verifier3(o)
        assert isinstance(e.value, vr3.RegistreServiNonConformeV3) and 19 in e.value.numeros
        with pytest.raises(vr3.RegistreServiNonConformeV3):
            verifier3(s.octets, noms_attendus=[A.mot_fiche(1)])

    def test_artefact_enonce_non_ligne_tentative_non_touchee(self, dossier):
        s = servi_marque(dossier)
        o = (s.octets.decode("utf-8") + "autre : ligne\n").encode("utf-8")
        with pytest.raises(vr3.RegistreServiNonConformeV3, match="19"):
            verifier3(o)


# --- erratum 2, (d) : passeport du portier marqué ---------------------------------------------------------------------

from pole import contrat_fiche_na_v1 as ct  # noqa: E402
from pole import lecteur_fiches_na_v1 as lf  # noqa: E402
from pole import portier_na_v3 as pt3  # noqa: E402
from pole import requete_na_v3 as rq  # noqa: E402

DECLARATION = pt.declaration_de(
    forme=pt.FORME_LIGNE_ANCREE, cle="étiquette",
    fiche={pt.NIVEAU_IDEE: "niveau de l'idée", pt.CONCRET: "concret"},
    reponse_sans_fiche={pt.VIDE_MOTIVEE: "réponse vide motivée", pt.REFUS_DU_MODELE: "refus du modèle",
                        pt.ILLISIBLE: "réponse illisible"},
    statut="brouillon d'essai factice")
BORNES = ct.bornes_de({c: 1200 for c in rq.CHAMPS_FICHE}, "brouillon d'essai factice")


def case_servie():
    c = A.contenu(A.CASES[0])
    ligne = tn.PREFIXE_LIGNE + tn.SEPARATEUR_LIGNE.join(
        [A.CASES[0], c["ce_que_le_moniteur_suppose"], c["menace_du_programme"], c["etage_de_lecture"]])
    return rq.CaseServie((0, 0, 0), A.CASES[0], ligne)


def fiche_lue():
    c = A.contenu(A.CASES[0], idee="Idée factice sur une ligne.")
    return lf.lire_fiches("\n".join(f"{n} : {v}" for n, v in c.items())).fiches[0]


def portier(dossier, issues):
    file = list(issues)

    def appeler(requete, lire):
        texte, marque = file.pop(0)
        d = {"r": None, "lu": lire(f"Texte factice.\nétiquette : {texte}\n"), "motif": None, "duree": 0.0}
        if marque is not ...:
            d[pt3.CLE_PAR_REPLI] = marque
        return d

    consigne = rq.Piece("consigne factice", b"consigne factice", A.sha(b"consigne factice"))
    return pt3.PortierNAV3(consigne=consigne, declaration=DECLARATION, bornes=BORNES, appeler=appeler,
                           dossier_sortie=dossier, nom_journal="journal-portier-v3.jsonl", generation=1)


class TestPasseportMarque:
    def test_sain_marque_lue_vrai_et_faux(self, dossier):
        p = portier(dossier, [("niveau de l'idée", True), ("niveau de l'idée", False)])
        i1 = p.classer_fiche(fiche_lue(), identifiant=A.mot_fiche(1), case=case_servie())
        i2 = p.classer_fiche(fiche_lue(), identifiant=A.mot_fiche(2), case=case_servie())
        assert i1.classe == pt.PASSEE and isinstance(i1.passeport, pt3.PasseportV3)
        assert i1.passeport.par_repli is True and i2.passeport.par_repli is False
        assert p.exiger_passeport(A.mot_fiche(1), i1.contenu).par_repli is True
        assert p.issues_fiches()[0].passeport.par_repli is True
        assert p.comptes()["passeports_par_repli"] == 1 and p.comptes()["passeports"] == 2

    def test_sain_au_coffre_sans_passeport(self, dossier):
        p = portier(dossier, [("concret", True)])
        i = p.classer_fiche(fiche_lue(), identifiant=A.mot_fiche(1), case=case_servie())
        assert i.classe == pt.AU_COFFRE and i.passeport is None
        with pytest.raises(pt.ArretSansPasseportNA):
            p.exiger_passeport(A.mot_fiche(1), i.contenu)

    @pytest.mark.parametrize("marque", [..., None, "vrai", 1])
    def test_artefact_marque_absente_ou_mal_formee(self, dossier, marque):
        p = portier(dossier, [("niveau de l'idée", marque)])
        with pytest.raises(pt.PortierRefuse, match="par_repli"):
            p.classer_fiche(fiche_lue(), identifiant=A.mot_fiche(1), case=case_servie())

    def test_l_issue_marquee_entre_au_registre(self, dossier):
        p = portier(dossier, [("niveau de l'idée", True)])
        i = p.classer_fiche(fiche_lue(), identifiant=A.mot_fiche(1), case=case_servie())
        r = A.registre(dossier)
        r.ajouter_chaine([A.refus(0, espece="portier"), A.tentative(1, espece="portier", classe_issue=pt.VIDE_MOTIVEE)])
        r.ajouter_chaine([A.tentative()], [i])
        assert len(rg3.lignes_fiche(A.lire(r.chemin))) == 1
