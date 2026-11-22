"""Essais du lot 6 v5 du véhicule NA-1 : course de trois générations dans `GenerationNAV5` (lot 4 v3, portier v3,
registre v4), sur l'adaptateur direct réel et le faux client ; chaînes de repli au registre ; `id_tentative` ; comptes ;
juges et portier servis par repli ; configuration des replis ; contrôle du code chargé ; différentiel avec le v3. Chaque
garde : un cas sain et un artefact (R5). Aucun appel, aucune clé, aucun réseau."""

import hashlib
import os
import re
import sys

import pytest

ICI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ICI)

import aides_na_lot6_v5 as H  # noqa: E402
from pole import appel_garde_na_v3 as ag  # noqa: E402
from pole import code_charge_na_v1 as cc  # noqa: E402
from pole import course_na_v5 as c5  # noqa: E402
from pole import registre_na_v3 as rg3  # noqa: E402
from pole import registre_na_v4 as rg4  # noqa: E402
from pole import simulation_na_v5 as s5  # noqa: E402

M = H.CE.MODELE_ESSAI
FORME = re.compile(r"^T[0-9]{2}-[0-9]{4}-[0-2]$")


def tentatives(lignes):
    return [l for l in lignes if l["type_ligne"] == "tentative"]


def fiches(lignes):
    return [l for l in lignes if l["type_ligne"] == "fiche"]


def chaines(lignes):
    d = {}
    for l in tentatives(lignes):
        d.setdefault(l["id_tentative"][:8], []).append(l)
    return d


def courir(scenario=None, **kw):
    m = H.MontageV5(scenario=scenario, **kw.pop("montage", {}))
    bilan = m.lancer(**kw)
    return m, bilan


# --- une course de trois générations, sans repli -----------------------------------------------------------------

@pytest.fixture(scope="module")
def course():
    return courir()


class TestCourseSansRepli:
    def test_trois_generations_et_sorties_en_v5(self, course):
        m, bilan = course
        assert len(bilan) == 3 and m.arrets() == []
        assert os.path.exists(m.chemin_sortie(c5.NOM_JOURNAL_ARRETS)) and os.path.exists(m.chemin_sortie(c5.NOM_BILAN))
        assert m.depart()["version"] == "course-na-v5" and m.depart()["code_charge"] == c5.CODE_CHARGE_NON_DEMANDE

    def test_id_tentative_sur_chaque_ligne(self, course):
        m, _ = course
        for g in (1, 2, 3):
            lignes = m.lignes_registre(g)
            assert lignes and all(FORME.match(l["id_tentative"]) and l["id_tentative"][1:3] == f"{g:02d}" for l in lignes)
            nums = [int(l["id_tentative"][4:8]) for l in tentatives(lignes) if l["rang_repli"] == 0]
            assert nums == list(range(1, len(nums) + 1))
            courant = None
            for l in lignes:
                if l["type_ligne"] == "tentative":
                    courant = l["id_tentative"]
                else:
                    assert l["id_tentative"] == courant

    def test_ligne_de_generation_porte_les_comptes_v4(self, course):
        _, bilan = course
        for ligne in bilan:
            c = ligne["comptes_registre_v4"]
            assert c["lignes_fiche"] == ligne["coffre"]["rendues"] == ligne["comptes_portier_lot_5"]["fiches_rendues"]
            assert ligne["coffre"]["dont_servies_par_repli"] == 0 and c["replis"]["par_espece_et_modele_servi"] == {}
            assert set(c["m6"]) == {"par_role", "par_espece", "par_case", "par_case_et_espece", "trois_refus_arret_1"}

    def test_m6_egal_aux_classes_d_appel_du_portier(self, course):
        _, bilan = course
        for ligne in bilan:
            m6 = ligne["comptes_registre_v4"]["m6"]["par_espece"]
            portier = ligne["comptes_portier_lot_5"]["classes_appel"]
            for k in ("réponse vide motivée", "refus du modèle"):
                assert sum(d.get(k, 0) for d in m6.values()) == portier[k]

    def test_registre_servi_marque(self, course):
        _, bilan = course
        assert bilan[1]["registre_servi"]["marques_par_repli"] == 0 and bilan[1]["registre_servi"]["taille"] > 0


# --- repli d'un proposeur --------------------------------------------------------------------------------------------

def scen_proposeur(*choix):
    return {"ad_a": H.selon({("proposeur", M): list(choix)})}


class TestRepliProposeur:
    def test_servi_par_repli_chaine_au_registre(self):
        m, bilan = courir(scen_proposeur(s5.REFUS))
        ch = [c for c in chaines(m.lignes_registre(1)).values() if len(c) > 1]
        assert len(ch) == 1
        t0, t1 = ch[0]
        assert (t0["rang_repli"], t1["rang_repli"]) == (0, 1)
        assert (t0["modele_demande"], t1["modele_demande"]) == (M, H.REPLI_1)
        assert t0["classe_issue"] == rg3.REFUS_SERVI_PAR_REPLI and t0["raison_arret"] == "refusal"
        assert t0["categorie_refus"] == s5.CATEGORIE_ESSAI and t1["raison_arret"] == "end_turn"
        assert t0["id_tentative"][:8] == t1["id_tentative"][:8] and t1["id_tentative"].endswith("-1")
        f = [l for l in fiches(m.lignes_registre(1)) if l["id_tentative"] == t1["id_tentative"]]
        assert all(x["rang_repli"] == 1 and x["modele_servi"] == H.REPLI_1 for x in f)
        c = bilan[0]["comptes_registre_v4"]
        assert c["replis"]["par_espece_et_modele_servi"]["espece-3"][H.REPLI_1]["nombre"] == 1
        if t1["classe_issue"] != "fiches rendues":
            assert c["m6"]["par_espece"]["espece-3"][rg3.REFUS_SERVI_PAR_REPLI] == 1
        assert bilan[0]["coffre"]["dont_servies_par_repli"] == len(f)
        assert bilan[0]["comptes_lot_6"]["issues_proposeur"]["proposeur-espece-3"][c5.ISSUE_SERVI_PAR_REPLI] == 1
        assert c["m4"]["replis"]["par_modele_demande"][H.REPLI_1] > 0

    def test_fiche_passee_par_repli_marquee_au_registre_servi(self):
        m, bilan = courir(scen_proposeur(s5.REFUS))
        passees_repli = [l for l in fiches(m.lignes_registre(1)) if l["rang_repli"] > 0 and l["classe"] == "passée"]
        assert len(passees_repli) == 1  # erratum 2, (d) : servie par repli, servie à la génération 2, marquée
        assert bilan[1]["registre_servi"]["marques_par_repli"] == len(passees_repli)
        assert bilan[0]["comptes_portier_lot_5"]["passeports_par_repli"] == 0  # le portier, lui, n'est pas en repli

    def test_trois_refus(self):
        m = H.MontageV5(scenario={"ad_a": H.selon({("proposeur", M): [s5.REFUS], ("proposeur", H.REPLI_1): [s5.REFUS],
                                                   ("proposeur", H.REPLI_2): [s5.REFUS]})})
        bilan = m.lancer()
        ch = [c for c in chaines(m.lignes_registre(1)).values() if len(c) == 3]
        assert len(ch) == 1 and all(t["classe_issue"] == "refus du modèle" and t["raison_arret"] == "refusal"
                                    for t in ch[0])
        c = bilan[0]["comptes_registre_v4"]["m6"]
        assert c["trois_refus_arret_1"] == {"espece-3": 1}
        assert bilan[0]["comptes_lot_6"]["issues_proposeur"]["proposeur-espece-3"][c5.ISSUE_ARRET_1_APRES_REPLI] == 1

    def test_refus_puis_sans_reponse(self):
        m = H.MontageV5(scenario={"ad_a": H.selon({("proposeur", M): [s5.REFUS], ("proposeur", H.REPLI_1): [s5.ERREUR]})})
        bilan = m.lancer()
        ch = [c for c in chaines(m.lignes_registre(1)).values() if len(c) == 2]
        assert len(ch) == 1
        t0, t1 = ch[0]
        assert t0["classe_issue"] == t1["classe_issue"] == "réponse illisible"
        assert t1["modele_servi"] is None and t1["raison_arret"] == "sans_reponse"
        assert bilan[0]["comptes_registre_v4"]["m6"]["par_espece"]["espece-3"]["réponse illisible"] >= 1


# --- portier et juges servis par repli -----------------------------------------------------------------------------

class TestRolesServisParRepli:
    def test_juge_servi_par_repli_sans_a2(self):
        m = H.MontageV5(scenario={"ad_a": H.selon({("juge", M): [s5.REFUS]})})
        bilan = m.lancer()
        assert m.arrets() == [] and bilan[0]["comptes_lot_6"]["verdicts_juges_par_repli"] == {"juge-espece-3": 1}

    def test_portier_servi_par_repli_passeport_marque(self):
        m = H.MontageV5(scenario={"ad_b": H.selon({("portier_fiche", M): [s5.REFUS]})})
        bilan = m.lancer()
        assert m.arrets() == [] and bilan[0]["comptes_portier_lot_5"]["passeports_par_repli"] == 1

    def test_portier_sans_marque_refuse(self):
        from pole import portier_na_v3 as pt3
        m = H.MontageV5()

        def sans_marque(g, gen):
            appeler = gen._appeler_portier

            def ap(requete, lire):
                a = appeler(requete, lire)
                if isinstance(a, dict):
                    a = {k: v for k, v in a.items() if k != "par_repli"}
                return a
            gen.portier = pt3.PortierNAV3(consigne=gen.course_na.consigne_portier, declaration=gen.course_na.declaration,
                                          bornes=gen.course_na.bornes, appeler=ap, dossier_sortie=gen.sortie,
                                          nom_journal="journal-portier-g1-bis.jsonl", generation=1)
        with pytest.raises(pt3.PortierRefuse, match="par_repli"):
            m.lancer(crochets={"avant_execution": sans_marque})


# --- registre v4 : id_tentative -------------------------------------------------------------------------------------

@pytest.fixture(scope="module")
def lignes():
    m, _ = courir(scen_proposeur(s5.REFUS))
    return list(m.lignes_registre(1))


class TestRegistreV4:
    def test_sain(self, lignes):
        assert rg4.verifier_ids(lignes, 1) >= 1

    @pytest.mark.parametrize("cas", ["absent", "forme", "generation", "rang", "saut", "fiche", "double"])
    def test_artefacts(self, lignes, cas):
        ls = [dict(l) for l in lignes]
        t = next(i for i, l in enumerate(ls) if l["type_ligne"] == "tentative" and l["rang_repli"] == 0
                 and int(l["id_tentative"][4:8]) == 2)
        f = next((i for i, l in enumerate(ls) if l["type_ligne"] == "fiche"), None)
        if cas == "absent":
            del ls[t]["id_tentative"]
        elif cas == "forme":
            ls[t]["id_tentative"] = "T1-0002-0"
        elif cas == "generation":
            ls[t]["id_tentative"] = "T02" + ls[t]["id_tentative"][3:]
        elif cas == "rang":
            ls[t]["id_tentative"] = ls[t]["id_tentative"][:-1] + "1"
        elif cas == "saut":
            ls[t]["id_tentative"] = "T01-0009-0"
        elif cas == "fiche":
            ls[f]["id_tentative"] = "T01-0999-0"
        elif cas == "double":
            ls.append(dict(ls[t]))
        with pytest.raises(rg4.RegistreRefuse):
            rg4.verifier_ids(ls, 1)

    # Artefacts isolés : chacun ne viole qu'une règle de `verifier_ids` (une garde ôtée n'est pas couverte par une autre).
    @staticmethod
    def _l(ident, rang, type_ligne="tentative"):
        return {"id_tentative": ident, "rang_repli": rang, "type_ligne": type_ligne}

    def test_isole_sain(self):
        ls = [self._l("T01-0001-0", 0), self._l("T01-0001-1", 1), self._l("T01-0001-1", 1, "fiche"),
              self._l("T01-0002-0", 0), self._l("T01-0002-0", 0, "fiche")]
        assert rg4.verifier_ids(ls, 1) == 2

    def test_isole_numero_hors_suite(self):
        with pytest.raises(rg4.RegistreRefuse, match="suite"):
            rg4.verifier_ids([self._l("T01-0002-0", 0)], 1)

    def test_isole_fiche_d_une_autre_tentative(self):
        ls = [self._l("T01-0001-0", 0), self._l("T01-0002-0", 0), self._l("T01-0001-0", 0, "fiche")]
        with pytest.raises(rg4.RegistreRefuse, match="servie"):
            rg4.verifier_ids(ls, 1)

    def test_isole_rang_autre_que_rang_repli(self):
        ls = [self._l("T01-0001-0", 0), self._l("T01-0001-1", 2)]
        with pytest.raises(rg4.RegistreRefuse, match="rang"):
            rg4.verifier_ids(ls, 1)

    def test_unicite_course(self, lignes):
        assert rg4.verifier_unicite_course({1: lignes}) == len(tentatives(lignes))
        with pytest.raises(rg4.RegistreRefuse, match="course"):
            rg4.verifier_unicite_course({1: lignes, 2: lignes})

    def test_ligne_v3_ancien_format(self, lignes):
        with pytest.raises(rg4.RegistreAncienFormatV4):
            rg4.lignes_v3_de([rg4.vers_v3(lignes[0])])

    def test_id_tentative_bornes(self):
        assert rg4.id_tentative(1, 7, 1) == "T01-0007-1"
        for a in ((0, 1, 0), (1, 0, 0), (1, 10000, 0), (1, 1, 3), (True, 1, 0)):
            with pytest.raises(rg4.RegistreRefuse):
                rg4.id_tentative(*a)


# --- chaîne au registre : classes ---------------------------------------------------------------------------------

def t(rang, issue, raison=None, servi="x", cat=None):
    return {"rang_tentative": rang, "issue": issue, "raison_arret": raison, "modele_demande": f"m{rang}",
            "modele_servi": servi, "categorie": cat, "cout_micro": 10}


class TestChaineAuRegistre:
    def test_non_lance_au_rang_1_n_est_pas_un_appel(self):
        assert c5.chaine_au_registre([t(1, "non lancé", servi=None)], espece="espece-3", case="c") is None

    def test_non_lance_en_repli_clot_sans_reponse(self):
        ch = c5.chaine_au_registre([t(1, "refus de classifieur", "refusal"), t(2, "non lancé", servi=None)],
                                   espece="espece-3", case="c")
        assert [x["classe_issue"] for x in ch] == ["réponse illisible"] * 2 and ch[1]["raison_arret"] == "sans_reponse"

    def test_categorie_non_lue_nulle(self):
        ch = c5.chaine_au_registre([t(1, "refus de classifieur", "refusal", cat="catégorie non lue"),
                                    t(2, "refus par classifieur, servi par repli", "end_turn")],
                                   espece="espece-3", case="c", classe_servie="réponse vide motivée")
        assert ch[0]["categorie_refus"] is None and ch[0]["cout_compte_usd"] == 1e-05

    def test_servie_sans_classe_refusee(self):
        with pytest.raises(c5.DefautLot6V5):
            c5.chaine_au_registre([t(1, "ok", "end_turn")], espece="espece-3", case="c")


# --- configuration des replis -----------------------------------------------------------------------------------------

class TestConfigurationReplis:
    def test_replis_absents_refuses(self):
        m = H.MontageV5(sans_replis=True)
        with pytest.raises(c5.cfn.ConfigurationCourseRefusee, match="replis"):
            m.lancer()

    def test_pire_de_repli_manquant_n34(self):
        def sans_pire(o):
            del o["replis"]["pires_repli_usd"]["aiguilleur"]
        m = H.MontageV5(modifier=sans_pire)
        with pytest.raises(ag.PireManquantNA):
            m.lancer()
        assert m.arrets()[0]["numero"] == 34


# --- contrôle du code chargé (n° 33) ------------------------------------------------------------------------------

def table_du_disque(racine):
    t = {}
    for nom, mod in list(sys.modules.items()):
        f = getattr(mod, "__file__", None)
        if isinstance(f, str) and os.path.realpath(f).startswith(os.path.realpath(racine) + os.sep) and f.endswith(".py"):
            with open(f, "rb") as h:
                t[os.path.normpath(os.path.relpath(os.path.realpath(f), os.path.realpath(racine)))] = \
                    hashlib.sha256(h.read()).hexdigest()
    return t


class TestCodeCharge:
    def test_table_egale_depart(self):
        racine = os.path.dirname(ICI)
        table = table_du_disque(racine)
        m = H.MontageV5()
        m.lancer(controle_code_charge=lambda moment: cc.verifier_code_charge(table, racine, moment))
        assert "pole/course_na_v5.py" in m.depart()["code_charge"]

    def test_empreinte_autre_refuse_avant_toute_ecriture(self):
        racine = os.path.dirname(ICI)
        table = table_du_disque(racine)
        table["pole/registre_na_v4.py"] = "0" * 64
        m = H.MontageV5()
        with pytest.raises(c5.ArretCodeChargeCourseNA) as e:
            m.lancer(controle_code_charge=lambda moment: cc.verifier_code_charge(table, racine, moment))
        assert e.value.numero == 33 and not os.path.exists(m.sortie)

    def test_module_plante_a_la_generation_2(self):
        racine = os.path.dirname(ICI)
        table = table_du_disque(racine)
        m = H.MontageV5()

        def plante(g):
            import types
            mod = types.ModuleType("pole.plante_essai_v5")
            mod.__file__ = os.path.join(racine, "pole", "plante_essai_v5.py")
            with open(mod.__file__, "w") as f:
                f.write("X = 1\n")
            sys.modules["pole.plante_essai_v5"] = mod
        try:
            with pytest.raises(c5.ArretCodeChargeCourseNA):
                m.lancer(crochets={"entre_generations": plante},
                         controle_code_charge=lambda moment: cc.verifier_code_charge(table, racine, moment))
            assert m.arrets()[0]["numero"] == 33 and m.arrets()[0]["generation"] == 2
        finally:
            sys.modules.pop("pole.plante_essai_v5", None)
            p = os.path.join(racine, "pole", "plante_essai_v5.py")
            if os.path.exists(p):
                os.remove(p)


# --- différentiel avec le v3 --------------------------------------------------------------------------------------

class TestDifferentielV3:
    def test_sans_repli_meme_portier_que_le_v3(self, course):
        m3 = H.A3.Montage()
        b3 = m3.lancer()
        _, b5 = course
        for l3, l5 in zip(b3, b5):
            assert l3["comptes_portier_lot_5"]["classes_fiche"] == l5["comptes_portier_lot_5"]["classes_fiche"]
            assert l3["comptes_portier_lot_5"]["classes_appel"] == l5["comptes_portier_lot_5"]["classes_appel"]
            assert l3["coffre"]["rendues"] == l5["coffre"]["rendues"]
            assert l3["comptes_lot_6"]["issues_proposeur"] == l5["comptes_lot_6"]["issues_proposeur"]
