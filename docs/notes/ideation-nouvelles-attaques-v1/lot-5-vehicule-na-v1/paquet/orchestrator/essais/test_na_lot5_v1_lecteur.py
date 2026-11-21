"""Essais du lecteur de fiches neuf (lot 5 du véhicule NA-1) : syntaxes déclarées, grammaire par étiquettes ancrées sans
ordre exigé, rien de complété ni de réparé (conception v5, § 2.4, § 5.4, § 6.2). Données factices seules."""

import os
import sys

import pytest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import aides_na_lot5_v1 as A5  # noqa: E402
from pole import caviardage  # noqa: E402
from pole import fiches_v53  # noqa: E402
from pole import lecteur_fiches_na_v1 as lf  # noqa: E402
from pole import requete_na_v3 as rq  # noqa: E402

PARURES = (
    "{n} : {v}",
    "{n}: {v}",
    "**{n}** : {v}",
    "**{n} :** {v}",
    "- {n} : {v}",
    "* **{n}**: {v}",
    "`{n}` : {v}",
    "> {n} : {v}",
    "1. {n} : {v}",
    "__{n}__ : {v}",
)


class TestGrammaireParEtiquettesAncrees:
    @pytest.mark.parametrize("parure", PARURES)
    def test_chaque_parure_reconnue_aux_memes_valeurs(self, parure):
        c = A5.contenu()
        lecture = lf.lire_fiches("Préambule factice.\n" + A5.en_lignes(c, parure=parure) + "\n---\nFin factice.")
        assert len(lecture.fiches) == 1
        f = lecture.fiches[0]
        assert f.syntaxe == lf.SYNTAXE_ETIQUETTES
        assert f.contenu() == c
        assert f.extras == ()

    def test_prose_finale_sans_separateur_jointe_a_la_derniere_valeur_rien_n_est_retire(self):
        c = A5.contenu()
        f = lf.lire_fiches(A5.en_lignes(c) + "\nFin factice.").fiches[0]
        assert f.valeur("piece_produite") == "publique\nFin factice."

    def test_titres_seuls_valeur_aux_lignes_suivantes(self):
        c = A5.contenu()
        texte = "\n".join(f"### {n}\n{v}" for n, v in c.items())
        f = lf.lire_fiches(texte).fiches[0]
        assert f.contenu() == c

    def test_douze_champs_dans_un_autre_ordre(self):
        c = A5.contenu()
        ordre = list(reversed(list(c.keys())))
        lecture = lf.lire_fiches(A5.en_lignes(c, ordre=ordre))
        assert len(lecture.fiches) == 1 and lecture.fiches[0].contenu() == c

    def test_ordre_melange_dans_chaque_parure(self):
        c = A5.contenu()
        ordre = list(c.keys())[6:] + list(c.keys())[:6]
        for parure in PARURES:
            assert lf.lire_fiches(A5.en_lignes(c, ordre=ordre, parure=parure)).fiches[0].contenu() == c

    def test_valeur_qui_contient_un_autre_nom_hors_tete_de_ligne_lue_juste(self):
        c = A5.contenu(idee="Une idée factice où le mot case : apparaît, et filiation : aussi.\n"
                            "Seconde ligne factice où idee : et menace_du_programme : reviennent.")
        f = lf.lire_fiches(A5.en_lignes(c)).fiches[0]
        assert f.contenu() == c

    def test_valeur_qui_porte_un_autre_nom_en_tete_de_ligne_refusee_jamais_lue_fausse(self):
        c = A5.contenu(idee="Première ligne factice.\nfiliation : une valeur glissée")
        lecture = lf.lire_fiches(A5.en_lignes(c))
        assert lecture.fiches == ()
        assert lecture.non_reconnus == (lf.CAUSE_DOUBLE,)

    def test_champ_en_double_non_reconnu(self):
        c = A5.contenu()
        texte = A5.en_lignes(c) + "\nidee : seconde idée factice"
        lecture = lf.lire_fiches(texte)
        assert lecture.fiches == () and lecture.non_reconnus == (lf.CAUSE_DOUBLE,)

    def test_onze_champs_non_reconnue(self):
        c = A5.contenu()
        del c["piece_produite"]
        lecture = lf.lire_fiches(A5.en_lignes(c))
        assert lecture.fiches == () and lecture.non_reconnus == (lf.CAUSE_MANQUANT,)

    def test_rien_n_est_complete_ni_repare(self):
        c = A5.contenu(idee="  Idée factice entourée de blancs.  ")
        f = lf.lire_fiches(A5.en_lignes(c)).fiches[0]
        assert f.valeur("idee") == "Idée factice entourée de blancs."  # blancs de tête et de queue seuls retirés
        c2 = A5.contenu(etage_de_lecture="étage factice deux.")  # un point de plus : gardé
        assert lf.lire_fiches(A5.en_lignes(c2)).fiches[0].valeur("etage_de_lecture") == "étage factice deux."

    def test_champ_en_plus_releve_par_son_nom(self):
        c = A5.contenu()
        f = lf.lire_fiches(A5.en_lignes(c, extras=[("comment_faire", "valeur factice")])).fiches[0]
        assert f.extras == ("comment_faire",)
        assert f.contenu() == c

    def test_deux_fiches_separees_par_une_regle(self):
        c1, c2 = A5.contenu(), A5.contenu(idee="Autre idée factice.")
        lecture = lf.lire_fiches(A5.en_lignes(c1) + "\n---\n" + A5.en_lignes(c2))
        assert [f.contenu() for f in lecture.fiches] == [c1, c2]
        assert [f.rang for f in lecture.fiches] == [1, 2]

    def test_deux_fiches_separees_par_un_titre(self):
        c1, c2 = A5.contenu(), A5.contenu(idee="Autre idée factice.")
        lecture = lf.lire_fiches("## Fiche factice\n" + A5.en_lignes(c1) + "\n## Autre fiche factice\n" + A5.en_lignes(c2))
        assert len(lecture.fiches) == 2

    def test_url_en_valeur_n_est_pas_une_etiquette(self):
        c = A5.contenu(voisin_le_plus_proche_connu="aucun connu\nhttps://exemple.invalid/factice")
        f = lf.lire_fiches(A5.en_lignes(c)).fiches[0]
        assert f.extras == () and f.valeur("voisin_le_plus_proche_connu") == c["voisin_le_plus_proche_connu"]


class TestObjetStructure:
    def test_bloc_json_cloture(self):
        c = A5.contenu()
        f = lf.lire_fiches("Texte factice.\n" + A5.en_json(c) + "\nFin.").fiches[0]
        assert f.syntaxe == lf.SYNTAXE_OBJET and f.contenu() == c

    def test_objet_nu_et_enveloppe_fiches(self):
        c1, c2 = A5.contenu(), A5.contenu(idee="Autre idée factice.")
        import json
        texte = json.dumps({"fiches": [c1, c2]}, ensure_ascii=False)
        assert [f.contenu() for f in lf.lire_fiches(texte).fiches] == [c1, c2]
        assert lf.lire_fiches(A5.en_json(c1, cloture=False)).fiches[0].contenu() == c1

    def test_cle_en_double_non_reconnue(self):
        c = A5.contenu()
        corps = A5.en_json(c, cloture=False)
        corps = corps.replace('"filiation": "aucune"', '"filiation": "aucune",\n  "filiation": "autre"')
        lecture = lf.lire_fiches(corps)
        assert lecture.fiches == () and lecture.non_reconnus == (lf.CAUSE_DOUBLE,)

    def test_champ_en_plus_et_type_garde(self):
        c = dict(A5.contenu(), comment_faire="valeur factice")
        c["piece_produite"] = 7
        f = lf.lire_fiches(A5.en_json(c)).fiches[0]
        assert f.extras == ("comment_faire",)
        assert f.valeur("piece_produite") == 7

    def test_onze_cles_non_reconnue(self):
        c = A5.contenu()
        del c["idee"]
        lecture = lf.lire_fiches(A5.en_json(c))
        assert lecture.fiches == () and lecture.non_reconnus == (lf.CAUSE_MANQUANT,)


class TestToujoursUnObjet:
    @pytest.mark.parametrize("texte", ["", "   ", "Une réponse factice sans fiche.", "{pas du json",
                                       "Je ne connais que des variantes factices."])
    def test_rend_un_objet_sans_fiche(self, texte):
        lecture = lf.lire_fiches(texte)
        assert isinstance(lecture, lf.Lecture) and lecture.texte_rendu and lecture.fiches == ()

    def test_autre_chose_qu_un_texte_refuse(self):
        with pytest.raises(lf.LectureRefusee):
            lf.lire_fiches(None)


class TestChampCaseEtValidateurDuNoyau:
    def test_fiche_a_douze_champs_case_en_tete_reconnue(self):
        c = A5.contenu()
        assert list(c)[0] == "case"
        assert lf.lire_fiches(A5.en_lignes(c)).fiches[0].contenu() == c

    def test_la_meme_au_validateur_du_noyau_refusee_temoin_du_defaut(self):
        with pytest.raises(fiches_v53.FicheRefusee):
            fiches_v53.valider_contenu(A5.contenu(), list(rq.CHAMPS_FICHE))

    def test_champ_ferme_qu_un_caviardage_changerait_lu_tel_que_rendu(self):
        case = A5.case_de((1, 0, 2), 77, gabarit=A5.GABARIT_CAVIARDABLE)
        c = A5.contenu(case=case, gabarit=A5.GABARIT_CAVIARDABLE)
        assert c["ce_que_le_moniteur_suppose"] == A5.VALEUR_CAVIARDABLE
        assert caviardage.caviarder(A5.VALEUR_CAVIARDABLE)[1] == 1  # le noyau la changerait
        f = lf.lire_fiches(A5.en_lignes(c)).fiches[0]
        assert f.valeur("ce_que_le_moniteur_suppose") == A5.VALEUR_CAVIARDABLE
