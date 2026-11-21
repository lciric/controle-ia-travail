"""Sondes du vérificateur du lot 10 a (hostiles) : à jouer dans la copie neuve, à côté des essais du lot."""

import dataclasses
import os
import shutil
import sys
import tempfile

import pytest

ICI = os.path.dirname(os.path.abspath(__file__))
for _p in (ICI, os.path.dirname(ICI)):
    if _p not in sys.path:
        sys.path.insert(0, _p)

import aides_na_lot10a_v1 as M  # noqa: E402
import aides_na_lot3_v3 as L3  # noqa: E402
import aides_na_lot4_v1 as L4  # noqa: E402
import aides_na_v4 as A  # noqa: E402
from pole import appel_garde_na_v1 as ag  # noqa: E402
from pole import journal_na_v3 as jn  # noqa: E402
from pole import matiere_premiere_na_v1 as mp  # noqa: E402
from pole import routage_na_v1 as rt  # noqa: E402


@pytest.fixture
def dossier():
    d = tempfile.mkdtemp(prefix="verif-lot10a-")
    yield d
    shutil.rmtree(d, ignore_errors=True)


# V-A : séparateurs de ligne autres que \n : la ligne entière doit mordre (str.splitlines)
@pytest.mark.parametrize("sep", [" ", " ", "\x85", "\x0b", "\x0c", "\x1c", "\r"])
def test_va_separateurs_de_ligne_unicode_mordent(sep):
    col = M.colonne()
    constats = col.examiner_texte("avant" + sep + M.enonce(11) + sep + "après")
    assert [c.rang_ligne for c in constats] == [2]


# V-B : E4, attendue absente et manifeste « empreinte nulle » : refusé
def test_vb_e4_attendue_none_et_manifeste_null(dossier):
    man = {"format": mp.FORMAT_MANIFESTE_LECTURE_FIN, mp.CLE_EMPREINTE_ADDITIF: None}
    c = dataclasses.replace(M.conditions(dossier, manifeste=man), empreinte_additif_attendue=None)
    with pytest.raises(mp.EtatRefuseNA):
        M.depart(2, conditions_allumage=c)


def test_vb2_e4_attendue_non_hexa_egale_au_manifeste(dossier):
    man = {"format": mp.FORMAT_MANIFESTE_LECTURE_FIN, mp.CLE_EMPREINTE_ADDITIF: "abc"}
    c = dataclasses.replace(M.conditions(dossier, manifeste=man), empreinte_additif_attendue="abc")
    with pytest.raises(mp.EtatRefuseNA):
        M.depart(2, conditions_allumage=c)


# V-C : E4, quatre artefacts de la lettre + variantes
def test_vc_e4_les_quatre_artefacts_et_variantes(dossier):
    conf = {mp.CLE_EMPREINTE_ADDITIF: M.EMPREINTE_ADDITIF_ESSAI}
    # absent
    with pytest.raises(mp.EtatRefuseNA):
        M.depart(2, conditions_allumage=M.conditions(dossier, manifeste=None))
    # chemin = dossier
    d2 = tempfile.mkdtemp(dir=dossier)
    with pytest.raises(mp.EtatRefuseNA):
        M.depart(2, conditions_allumage=dataclasses.replace(M.conditions(d2), chemin_manifeste_lecture_fin=d2))
    # config seule, aucune condition
    with pytest.raises(mp.EtatRefuseNA):
        M.depart(2, configuration=conf, conditions_allumage=None)
    # manifeste illisible
    d3 = tempfile.mkdtemp(dir=dossier)
    chemin = os.path.join(d3, "m.json")
    with open(chemin, "w", encoding="utf-8") as f:
        f.write("{pas du json")
    with pytest.raises(mp.EtatRefuseNA):
        M.depart(2, conditions_allumage=dataclasses.replace(M.conditions(tempfile.mkdtemp(dir=dossier)),
                                                            chemin_manifeste_lecture_fin=chemin))
    # empreinte en majuscules : égalité stricte, refus
    man = {"format": mp.FORMAT_MANIFESTE_LECTURE_FIN, mp.CLE_EMPREINTE_ADDITIF: M.EMPREINTE_ADDITIF_ESSAI.upper()}
    with pytest.raises(mp.EtatRefuseNA):
        M.depart(2, conditions_allumage=M.conditions(tempfile.mkdtemp(dir=dossier), manifeste=man))
    # cas sain
    assert M.depart(2, conditions_allumage=M.conditions(tempfile.mkdtemp(dir=dossier))).etat == 2


# V-D : fragment d'environnement « COLONNE_MATIERE » sans « MATIERE_PREMIERE »
def test_vd_environnement_colonne_matiere_sans_premiere():
    with pytest.raises(mp.EtatRefuseNA):
        M.depart(1, environ={"COLONNE_MATIERE_ETAT": "1"})


# V-E : tronquer la requête examinée (faute par construction) : l'énoncé planté loin dans la requête doit mordre
def test_ve_enonce_en_fin_de_requete_mord():
    m = M.MontageColonne(M.depart(1))
    r = L4.requete_proposeur(1, 0, M.synthese_avec(M.enonce(12)))
    assert len(r.octets) > 2000
    with pytest.raises(mp.ArretColonneNA):
        m.appeler("proposeur-espece-3", r)


# V-F : câblage : un contexte de lot 4 dont le journal est celui du lot 3 laisse partir une ligne égale (nothing refuses it)
def test_vf_cablage_journal_ordinaire_laisse_partir():
    class MontageOrdinaire(M.MontageColonne):
        def __init__(self, depart_colonne):
            super().__init__(depart_colonne)
            self.journal = jn.JournalRequetes(self.sortie, "journal-ordinaire.jsonl")
            self.contexte = ag.ContexteAppelGardeNA(
                numero_generation=1, table=self.table, parts=L4.parts(self.table), pires_par_role=L4.pires(self.table),
                journal=self.journal, garde=self.garde, identifiant_case_de_session=L4.case_de_session, cumul=self.cumul,
                lire_etat_relais=lambda cle: dict(L4.etat_relais_sain()), portee_arret_1="appel")
            self.gen = L4.GenerationEssai(self.ad, self.dossier, contexte_na=self.contexte)

    m = MontageOrdinaire(M.depart(1))
    r = L4.requete_proposeur(1, 0, M.synthese_avec(M.enonce(12)))
    a = m.appeler("proposeur-espece-3", r)
    # constat : la ligne égale à une entrée est partie (aucun refus au câblage) ; c'est une affaire de lot 6 / 8
    assert a["issue_na"] == "ok" and len(m.recus()) == 1


# V-G : normalisation : formes que la garde de motifs ramène ou non (relevé, sans assertion de verdict)
def test_vg_releve_formes_non_testees(capsys):
    col = M.colonne()
    e = M.enonce(3)
    formes = {"pleine largeur": e.replace("E", "Ｅ").replace("n", "ｎ"), "point final ajouté": e + ".",
              "numérotée": "1. " + e, "guillemets": "« " + e + " »", "NUL au milieu": e.replace(" ", "\x00", 1),
              "cyrillique": e.replace("e", "е", 1)}
    rendu = {k: bool(col.examiner_ligne(v)) for k, v in formes.items()}
    print("RELEVE_V_G", rendu)
    assert isinstance(rendu, dict)
