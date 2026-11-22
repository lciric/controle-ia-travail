"""Essais du lot 7 — export hors quarantaine à champs fermés (arrêt n° 17, premier temps) ; cas sain et artefacts (R5)."""

import copy
import os

import pytest

import aides_na_lot7_v1 as A
from pole import commun_na_lot7_v1 as cm
from pole import export_na_v1 as ex
from pole import quarantaine_na_v1 as qu

ROLES_CONF = ("prop-e1",)


@pytest.fixture
def mesures(tmp_path):
    sortie, att, ca, cant = A.course_entiere(str(tmp_path))
    return A.lire(sortie, ca, cant), sortie


def _verifier(objet, m):
    return ex.verifier_export(objet, ex.identifiants_permis_de(m), ROLES_CONF)


class TestExportSain:
    def test_export_aux_seuls_champs_permis(self, mesures, tmp_path):
        m, sortie = mesures
        chemin = os.path.join(str(tmp_path), ex.NOM_EXPORT)
        e = ex.ecrire_export(chemin, m, ROLES_CONF)
        assert cm.lire_json_scelle(chemin, e)["version"] == ex.VERSION

    def test_rien_ne_fuit_marqueur_noms_enonces_modeles_categories(self, mesures, tmp_path):
        m, sortie = mesures
        chemin = os.path.join(str(tmp_path), ex.NOM_EXPORT)
        ex.ecrire_export(chemin, m, ROLES_CONF)
        fiches = m["identifiants"]["fiches_gardees"]
        textes = [A.MARQUEUR, "id-repli-1", "cyber", "filiation-invalide", "énoncé inerte"] + fiches[:5]
        assert qu.rechercher_textes([chemin], textes) == {}
        assert qu.rechercher_textes([sortie], [A.MARQUEUR])  # le marqueur est bien dans la quarantaine

    def test_course_arretee_s_exporte(self, tmp_path):
        sortie, att = A.fabriquer_sortie(str(tmp_path), completes=1,
                                         arret={"type": "ArretGardeCoffre", "numero": 5, "nom": "garde du coffre"})
        ca, et = A.ecrire_attestation(str(tmp_path), att)
        cant = A.ecrire_anteriorite(str(tmp_path), et, branche="sans")
        m = A.lire(sortie, ca, cant)
        ex.ecrire_export(os.path.join(str(tmp_path), ex.NOM_EXPORT), m, ROLES_CONF)


class TestExportArtefacts:
    """Chaque artefact : un champ libre planté ; l'export est refusé (n° 17), le chemin est nommé, la valeur jamais."""

    def _plante(self, m, f):
        o = ex.construire_export(m)
        f(o)
        return o

    @pytest.mark.parametrize("nom, f", [
        ("champ libre à la racine", lambda o: o.__setitem__("note", "texte libre")),
        ("texte dans un compte", lambda o: o.__setitem__("M3_relecture_au_coffre", "trois")),
        ("titre libre", lambda o: o.__setitem__("titre", "course arrêtée par " + A.MARQUEUR)),
        ("clé en plus dans C1", lambda o: o["C1"].__setitem__("commentaire", True)),
        ("identifiant hors liste en clé", lambda o: o["M6"]["1"].__setitem__("inconnu", {})),
        ("rôle hors liste", lambda o: o["M4"]["1"]["cout_par_role_usd"].__setitem__("Minuit", 1.0)),
        ("empreinte libre", lambda o: o["empreintes_des_entrees"].__setitem__("bilan", A.MARQUEUR)),
        ("part mal formée", lambda o: o["lectures"]["scellée"]["M7"].__setitem__("autres cases", {"numerateur": 3})),
        ("part à numérateur au-dessus", lambda o: o["lectures"]["scellée"]["M7"].__setitem__(
            "autres cases", {"numerateur": 3, "denominateur": 2})),
        ("issue de témoin libre", lambda o: o["M5"]["temoins"].__setitem__("temoin-vide", "texte")),
        ("booléen en texte", lambda o: o["C1"].__setitem__("trente_trois_cases_servies", "oui")),
    ])
    def test_champ_libre_refuse(self, mesures, nom, f):
        m, _ = mesures
        o = self._plante(m, f)
        with pytest.raises(ex.ArretQuarantaineRompueNA17) as e:
            _verifier(o, m)
        assert A.MARQUEUR not in str(e.value) and "texte libre" not in str(e.value)

    def test_role_de_configuration_non_declare_refuse(self, mesures):
        m, _ = mesures
        with pytest.raises(ex.ArretQuarantaineRompueNA17, match="M6_sous_comptes"):
            ex.verifier_export(ex.construire_export(m), ex.identifiants_permis_de(m))

    def test_liste_permise_qui_porte_un_texte_refusee(self, mesures):
        m, _ = mesures
        with pytest.raises(ex.ArretQuarantaineRompueNA17):
            ex.verifier_export(ex.construire_export(m), ex.identifiants_permis_de(m) | {"une phrase libre"}, ROLES_CONF)

    def test_export_jamais_ecrase(self, mesures, tmp_path):
        m, _ = mesures
        chemin = os.path.join(str(tmp_path), ex.NOM_EXPORT)
        ex.ecrire_export(chemin, m, ROLES_CONF)
        with pytest.raises(cm.ScelleRefuse):
            ex.ecrire_export(chemin, copy.deepcopy(m), ROLES_CONF)
