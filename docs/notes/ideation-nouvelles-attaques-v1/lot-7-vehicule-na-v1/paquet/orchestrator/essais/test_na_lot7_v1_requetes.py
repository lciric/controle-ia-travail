"""Essais du lot 7 — chaînes de requête de la classe (i) ; paramètres gelés à remplir (traduction ; Q14). Les valeurs
de case et la « traduction » sont des valeurs d'essai inertes, non celles de la légende."""

import datetime
import os

import pytest

from pole import commun_na_lot7_v1 as cm
from pole import requetes_anteriorite_na_v1 as rq

LIGNE = "case : bacodi ; valeur-un ; valeur-deux ; valeur-trois"
TRAD = {"valeur-un": "value-one", "valeur-deux": "value-two", "valeur-trois": "value-three", "valeur-x": "value-x"}
MOTS_EN = ["mot-en-1", "mot-en-2", "mot-en-3", "mot-en-4"]


def _parametres(tmp_path, **kw):
    o = {"format": rq.FORMAT_PARAMETRES, "traduction_valeurs": TRAD, "mots_domaine_en": MOTS_EN,
         "valeur_passe_x": "valeur-x", "statut": "essai, valeurs inertes"}
    o.update(kw)
    o = {k: v for k, v in o.items() if v is not None}
    chemin = str(tmp_path / "parametres.json")
    e = cm.ecrire_json_scelle(chemin, o)
    return rq.charger_parametres(chemin, e)


class TestClasseI:
    def test_sain_francais_douze_chaines_dans_l_ordre(self):
        c = rq.chaines_classe_i(LIGNE, langues=("fr",))
        assert c["case"] == "bacodi" and len(c["fr"]) == 12
        assert c["fr"][0] == "valeur-un sonde" and c["fr"][3] == "valeur-un boîte blanche"
        assert c["fr"][-1] == "valeur-trois boîte blanche"

    def test_artefact_anglais_sans_parametres_refuse_par_son_nom(self):
        with pytest.raises(rq.ParametreGeleNonRempli, match="traduction_valeurs"):
            rq.chaines_classe_i(LIGNE)
        assert rq.PARAMETRES_GELES.traduction_valeurs is None and rq.PARAMETRES_GELES.valeur_passe_x is None

    def test_artefact_mots_anglais_manquants(self, tmp_path):
        p = _parametres(tmp_path, mots_domaine_en=None)
        with pytest.raises(rq.ParametreGeleNonRempli, match="mots_domaine_en"):
            rq.chaines_classe_i(LIGNE, p)

    def test_artefact_valeur_sans_traduction(self, tmp_path):
        p = _parametres(tmp_path, traduction_valeurs={"valeur-un": "value-one"})
        with pytest.raises(rq.ParametreGeleNonRempli, match="2 valeur"):
            rq.chaines_classe_i(LIGNE, p)

    def test_sain_deux_langues_avec_parametres_scelles(self, tmp_path):
        c = rq.chaines_classe_i(LIGNE, _parametres(tmp_path))
        assert len(c["en"]) == 12 and c["en"][0] == "value-one mot-en-1"

    def test_artefact_parametres_d_une_autre_empreinte(self, tmp_path):
        _parametres(tmp_path)
        with pytest.raises(cm.ScelleRefuse):
            rq.charger_parametres(str(tmp_path / "parametres.json"), "0" * 64)

    @pytest.mark.parametrize("entree", [
        "case : bacodi ; valeur-un ; valeur-deux",
        "case : bacodi ; valeur-un ; valeur-deux ; valeur-trois ; en-plus",
        "fiche : bacodi ; a ; b ; c",
        "case : bacodi ; valeur-un ; valeur-deux ;  ",
        LIGNE + "\nidee : texte",
        {"case": "bacodi", "idee": "texte"},
    ])
    def test_artefact_entree_qui_n_est_pas_une_ligne_de_case(self, entree):
        with pytest.raises(rq.ChainesRefusees):
            rq.chaines_classe_i(entree, langues=("fr",))


class TestPasseX:
    def test_artefact_sans_q14_refuse(self):
        with pytest.raises(rq.ParametreGeleNonRempli, match="Q14"):
            rq.chaines_passe_x()

    def test_sain_avec_q14_rempli(self, tmp_path):
        c = rq.chaines_passe_x(_parametres(tmp_path))
        assert c["case"] is None and len(c["fr"]) == 4 and c["en"][0] == "value-x mot-en-1"


class TestJournalDesChaines:
    H = staticmethod(lambda: datetime.datetime(2026, 11, 22, 12, 0, tzinfo=datetime.timezone.utc))

    def test_sain_journal_scelle_grille_base_par_chaine(self, tmp_path):
        d = tmp_path / "j"
        d.mkdir()
        e = rq.produire_journal_chaines(str(d), [LIGNE, LIGNE.replace("bacodi", "fugeli")], _parametres(tmp_path), self.H)
        o = cm.lire_json_scelle(str(d / rq.NOM_JOURNAL_CHAINES), e)
        assert len(o["cases"]) == 2 and len(o["cases"][0]["grille"]) == 24 * len(rq.BASES)
        assert o["resultats_examines"] == 30

    def test_artefact_sans_parametres_rien_n_est_ecrit(self, tmp_path):
        d = tmp_path / "j"
        d.mkdir()
        with pytest.raises(rq.ParametreGeleNonRempli):
            rq.produire_journal_chaines(str(d), [LIGNE], rq.PARAMETRES_GELES, self.H)
        assert os.listdir(str(d)) == []

    def test_artefact_case_redite_ou_journal_existant(self, tmp_path):
        d = tmp_path / "j"
        d.mkdir()
        p = _parametres(tmp_path)
        with pytest.raises(rq.ChainesRefusees):
            rq.produire_journal_chaines(str(d), [LIGNE, LIGNE], p, self.H)
        rq.produire_journal_chaines(str(d), [LIGNE], p, self.H)
        with pytest.raises(cm.ScelleRefuse):
            rq.produire_journal_chaines(str(d), [LIGNE], p, self.H)
