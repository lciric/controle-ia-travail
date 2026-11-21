"""Essais du validateur neuf du contrat d'une fiche (lot 5 du véhicule NA-1) : type, borne en octets, champ en plus ;
comparaison « hors case » à l'octet ; champ `case` (conception v5, § 2.4, § 5.4, § 6.2). Données factices seules."""

import os
import sys

import pytest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import aides_na_lot5_v1 as A5  # noqa: E402
from pole import contrat_fiche_na_v1 as ct  # noqa: E402
from pole import lecteur_fiches_na_v1 as lf  # noqa: E402


def lue(c, extras=()):
    return lf.lire_fiches(A5.en_lignes(c, extras=extras)).fiches[0]


class TestBornes:
    def test_bornes_des_douze_champs_exactement(self):
        d = dict(A5.BORNES_DICT)
        assert ct.bornes_de(d, "brouillon").borne("idee") == 1200
        del d["idee"]
        with pytest.raises(ct.ContratRefuse):
            ct.bornes_de(d, "brouillon")
        with pytest.raises(ct.ContratRefuse):
            ct.bornes_de(dict(A5.BORNES_DICT, autre=3), "brouillon")
        with pytest.raises(ct.ContratRefuse):
            ct.bornes_de(dict(A5.BORNES_DICT, idee=0), "brouillon")
        with pytest.raises(ct.ContratRefuse):
            ct.bornes_de(A5.BORNES_DICT, "")

    def test_statut_du_brouillon_dit(self):
        assert "brouillon d'essai factice" in A5.BORNES_ESSAI.statut


class TestHorsContratDeLongueur:
    def _a_la_borne(self):
        c = A5.contenu()
        for n in ("idee", "filiation", "ecart_au_voisin"):
            b = A5.BORNES_ESSAI.borne(n)
            c[n] = ("é" * (b // 2)) + ("x" * (b % 2))
            assert len(c[n].encode("utf-8")) == b
        return c

    def test_chaque_champ_a_sa_borne_suit_son_chemin(self):
        v = ct.verifier(lue(self._a_la_borne()), A5.BORNES_ESSAI)
        assert v.au_contrat and v.cause is None

    @pytest.mark.parametrize("champ", ["idee", "filiation"])
    def test_un_octet_de_trop_hors_contrat_texte_inchange(self, champ):
        c = self._a_la_borne()
        c[champ] = c[champ] + "y"
        f = lue(c)
        v = ct.verifier(f, A5.BORNES_ESSAI)
        assert not v.au_contrat and v.hors_longueur == (champ,) and v.cause == ct.CAUSE_LONGUEUR
        assert f.valeur(champ) == c[champ]  # jamais coupé


class TestFormeEtType:
    def test_champ_en_plus(self):
        v = ct.verifier(lue(A5.contenu(), extras=[("comment_faire", "valeur factice")]), A5.BORNES_ESSAI)
        assert not v.au_contrat and v.champs_en_plus == ("comment_faire",) and v.cause == ct.CAUSE_CHAMP_EN_PLUS

    def test_valeur_qui_n_est_pas_une_chaine(self):
        c = A5.contenu()
        c["piece_produite"] = ["liste factice"]
        f = lf.lire_fiches(A5.en_json(c)).fiches[0]
        v = ct.verifier(f, A5.BORNES_ESSAI)
        assert v.types_faux == ("piece_produite",) and v.cause == ct.CAUSE_TYPE

    def test_ordre_des_causes(self):
        c = A5.contenu(idee="x" * 1201)
        v = ct.verifier(lue(c, extras=[("autre", "v")]), A5.BORNES_ESSAI)
        assert v.cause == ct.CAUSE_CHAMP_EN_PLUS and v.hors_longueur == ("idee",)


class TestHorsCaseArret4:
    def test_fiche_dans_sa_case(self):
        assert ct.champs_fermes_differents(A5.contenu(), A5.CASE) == ()

    @pytest.mark.parametrize("champ", list(ct.CHAMPS_FERMES))
    def test_un_octet_de_difference(self, champ):
        c = A5.contenu()
        c[champ] = c[champ] + " "
        assert ct.champs_fermes_differents(c, A5.CASE) == (champ,)

    def test_casse_differente_hors_case(self):
        c = A5.contenu()
        c["menace_du_programme"] = c["menace_du_programme"].upper()
        assert ct.champs_fermes_differents(c, A5.CASE) == ("menace_du_programme",)

    def test_forme_unicode_differente_hors_case(self):
        case = A5.case_de((0, 3, 0), 55)  # « menace factice quatre, avec virgule » ; « étage factice un »
        c = A5.contenu(case=case)
        c["etage_de_lecture"] = c["etage_de_lecture"].replace("é", "é")  # même rendu, autres octets
        assert ct.champs_fermes_differents(c, case) == ("etage_de_lecture",)

    def test_autre_a_nommer_valeur_attendue_cette_chaine(self):
        c = A5.contenu(case=A5.CASE_AUTRE)
        assert c["ce_que_le_moniteur_suppose"] == "autre, à nommer"
        assert ct.champs_fermes_differents(c, A5.CASE_AUTRE) == ()
        c2 = A5.contenu(case=A5.CASE_AUTRE, ce_que_le_moniteur_suppose="une supposition factice nommée")
        assert ct.champs_fermes_differents(c2, A5.CASE_AUTRE) == ("ce_que_le_moniteur_suppose",)

    def test_ligne_de_case_mal_formee_refusee(self):
        mauvaise = A5.rq.CaseServie(A5.CASE.triplet, A5.CASE.identifiant, A5.CASE.ligne.replace(" ; ", " | ", 1))
        with pytest.raises(ct.ContratRefuse):
            ct.valeurs_de_la_case(mauvaise)


class TestChampCase:
    def test_case_egale(self):
        assert not ct.case_differe(A5.contenu(), A5.CASE.identifiant)

    def test_case_differente(self):
        c = A5.contenu()
        c["case"] = A5.CASE_AUTRE.identifiant
        assert ct.case_differe(c, A5.CASE.identifiant)
