"""Essais du lot 6 v4 du véhicule NA-1 : registre alimenté (filiation, espèce, case, repli), comptes de M6, M3, M4 et des
replis, garde du coffre (n° 5) avec les fiches servies par repli, n° 31, n° 34, A6, contrôle du code chargé (n° 33, C-3),
différentiel avec le v3. Chaque garde : un cas sain et un artefact (R5). Moteur simulé, faux fournisseur ; aucun appel."""

import decimal
import hashlib
import os
import sys
import types

import pytest

from pole import course_na_v4 as c4
from pole import simulation_na_v4 as sm

D = decimal.Decimal


@pytest.fixture
def config():
    return sm.configuration_factice()


@pytest.fixture
def ff(config):
    return sm.FauxFournisseurReplis(config)


@pytest.fixture
def registre(tmp_path):
    return sm.RegistreFactice(str(tmp_path), "registre.jsonl")


@pytest.fixture
def alim(registre, config):
    return c4.AlimentationRegistreNA(registre, config, sm.CHAMPS_FERMES_FACTICES)


def fiche(i, classe=c4.PASSEE, filiation="aucune"):
    return {"identifiant": f"fiche-{i}", "classe": classe, "fermes": {c: "v" for c in sm.CHAMPS_FERMES_FACTICES},
            "idee": "une  idée\nfactice", "filiation": filiation}


def consigner(alim, ff, espece, scenario, *, g=1, case="case-00", classe=None, fiches=(), ident=None, categorie=None):
    return alim.consigner_chaine(identifiant_chaine=ident or f"g{g}-{case}-{espece}-{scenario}", generation=g,
                                 espece=espece, case=case, a=ff.chaine(espece, scenario, categorie), classe_servie=classe,
                                 fiches=fiches)


# --- configuration, n° 34 -------------------------------------------------------------------------------------------

class TestConfiguration:
    def test_saine(self, config):
        assert config.suite("espece-3") == ("m-espece-3", "m-repli-premier", "m-repli-second")
        assert config.suite("espece-1") == ("m-espece-1",)
        assert config.verifier_pires() > 0

    def test_replis_identiques_refuses(self):
        with pytest.raises(c4.DefautLot6V4, match="deux, distincts"):
            sm.configuration_factice(modeles_de_repli=("m-repli-premier", "m-repli-premier"))

    def test_repli_egal_au_modele_d_une_espece_refuse(self):
        with pytest.raises(c4.DefautLot6V4, match="aucune espèce"):
            sm.configuration_factice(modeles_de_repli=("m-espece-1", "m-repli-second"))

    def test_identifiant_en_clair_refuse(self):
        mr = {e: f"m-{e}" for e in c4.ESPECES}
        mr["espece-2"] = "Modele Majuscule 4.5"
        with pytest.raises(c4.DefautLot6V4, match="identifiant par rôle"):
            sm.configuration_factice(modele_du_role=mr)

    def test_n34_pire_de_repli_manquant(self, config):
        pires = dict(config.pires)
        del pires[("espece-3", "m-repli-second")]
        with pytest.raises(c4.ArretPireManquantNA) as e:
            sm.configuration_factice(pires=pires).verifier_pires()
        assert e.value.numero == 34


# --- lecture de la chaîne : A6, n° 31, coûts --------------------------------------------------------------------------

class TestLectureChaine:
    @pytest.mark.parametrize("scen,n", [("servie", 1), ("refus-servie-1", 2), ("refus-refus-servie-2", 3),
                                        ("trois-refus", 3), ("refus-erreur", 2), ("erreur", 1)])
    def test_scenarios_sains(self, config, ff, scen, n):
        t = c4.tentatives_de_l_appel(ff.chaine("espece-3", scen), "espece-3", config)
        assert [x.rang_repli for x in t] == list(range(n))

    def test_dictionnaire_du_lot_4_v1_refuse(self, config):
        with pytest.raises(c4.DefautLot6V4, match="tentatives_na"):
            c4.tentatives_de_l_appel({"r": object(), "lu": "texte", "issue_na": "ok"}, "espece-3", config)

    def test_rangs_desordonnes_refuses(self, config, ff):
        a = ff.chaine("espece-3", "refus-servie-1")
        a["tentatives_na"].reverse()
        with pytest.raises(c4.DefautLot6V4, match="rangs"):
            c4.tentatives_de_l_appel(a, "espece-3", config)

    def test_a6_repli_apres_une_tentative_servie(self, config, ff):
        a = ff.chaine("espece-3", "refus-servie-1")
        a["tentatives_na"][0]["raison_arret"] = "end_turn"
        a["tentatives_na"][0]["categorie_refus"] = None
        with pytest.raises(c4.ArretRepliNonPermisNA, match="pas refusée"):
            c4.tentatives_de_l_appel(a, "espece-3", config)

    def test_a6_repli_apres_une_raison_inconnue(self, config, ff):
        a = ff.chaine("espece-3", "refus-servie-1")
        a["tentatives_na"][0]["raison_arret"] = "pause_turn"
        with pytest.raises((c4.ArretRepliNonPermisNA, c4.DefautLot6V4)):
            c4.tentatives_de_l_appel(a, "espece-3", config)

    def test_repli_sur_une_espece_sans_repli(self, config):
        ff3 = sm.FauxFournisseurReplis(config)
        a = ff3.chaine("espece-3", "refus-servie-1")
        with pytest.raises(c4.ArretRepliNonPermisNA, match="sans repli"):
            c4.tentatives_de_l_appel(a, "espece-1", config)

    def test_modele_demande_hors_suite(self, config, ff):
        a = ff.chaine("espece-3", "refus-refus-servie-2")
        a["tentatives_na"][1]["modele_demande"] = "m-repli-second"
        with pytest.raises(c4.ArretRepliNonPermisNA, match="suite fermée"):
            c4.tentatives_de_l_appel(a, "espece-3", config)

    def test_n31_sain_meme_modele(self, config, ff):
        t = c4.tentatives_de_l_appel(ff.chaine("espece-3", "refus-servie-1"), "espece-3", config)
        assert t[1].modele_servi == config.modele_reel["m-repli-premier"]

    def test_n31_modele_servi_absent(self, config, ff):
        a = ff.chaine("espece-3", "refus-servie-1")
        a["tentatives_na"][1]["modele_servi"] = None
        with pytest.raises(c4.ArretModeleServiNA) as e:
            c4.tentatives_de_l_appel(a, "espece-3", config)
        assert e.value.numero == 31 and e.value.cause == "modèle servi absent"

    def test_n31_modele_servi_autre(self, config, ff):
        a = ff.chaine("espece-3", "refus-servie-1")
        a["tentatives_na"][1]["modele_servi"] = config.modele_reel["m-repli-second"]
        with pytest.raises(c4.ArretModeleServiNA, match="différent"):
            c4.tentatives_de_l_appel(a, "espece-3", config)

    def test_usage_manquant_au_pire_sain(self, config, ff):
        t = c4.tentatives_de_l_appel(ff.chaine("espece-3", "erreur"), "espece-3", config)
        assert t[0].cout_compte_usd == D("6.05")

    def test_usage_manquant_sous_le_pire_refuse(self, config, ff):
        a = ff.chaine("espece-3", "erreur")
        a["tentatives_na"][0]["cout_compte_usd"] = "0"
        with pytest.raises(c4.DefautLot6V4, match="pire"):
            c4.tentatives_de_l_appel(a, "espece-3", config)

    def test_categorie_hors_refus_refusee(self, config, ff):
        a = ff.chaine("espece-3", "servie")
        a["tentatives_na"][0]["categorie_refus"] = "cyber"
        with pytest.raises(c4.DefautLot6V4, match="catégorie"):
            c4.tentatives_de_l_appel(a, "espece-3", config)

    @pytest.mark.parametrize("v", [True, -1, "nan", "inf", None, "abc"])
    def test_cout_hors_forme(self, v):
        with pytest.raises(c4.DefautLot6V4):
            c4.montant(v)


# --- registre : champs de l'interface ---------------------------------------------------------------------------------

class TestRegistre:
    def test_chaque_tentative_ecrite_avec_les_champs_de_l_interface(self, alim, ff, registre):
        consigner(alim, ff, "espece-3", "refus-refus-servie-2", classe=c4.VIDE_MOTIVEE, categorie="cyber")
        l = registre.lignes()
        assert len(l) == 3
        for x in l:
            assert set(c4.CHAMPS_INTERFACE) <= set(x) and x["classe"] is None and x["filiation"] is None
        assert [x["rang_repli"] for x in l] == [0, 1, 2]
        assert [x["modele_demande"] for x in l] == ["m-espece-3", "m-repli-premier", "m-repli-second"]
        assert [x["classe_issue"] for x in l] == [c4.SERVI_PAR_REPLI, c4.SERVI_PAR_REPLI, c4.VIDE_MOTIVEE]
        assert [x["categorie_refus"] for x in l] == ["cyber", "cyber", None]
        assert [x["raison_arret"] for x in l] == ["refusal", "refusal", "end_turn"]
        assert all(x["espece"] == "espece-3" and x["case"] == "case-00" and x["generation"] == 1 for x in l)

    def test_servie_au_rang_0_classe_du_portier(self, alim, ff, registre):
        consigner(alim, ff, "espece-1", "servie", classe=c4.REFUS_DU_MODELE)
        assert registre.lignes()[0]["classe_issue"] == c4.REFUS_DU_MODELE

    def test_trois_refus_et_refus_erreur(self, alim, ff, registre):
        consigner(alim, ff, "espece-3", "trois-refus")
        consigner(alim, ff, "espece-4", "refus-erreur")
        l = registre.lignes()
        assert [x["classe_issue"] for x in l[:3]] == [c4.CLASSE_ARRET_1] * 3
        assert [x["classe_issue"] for x in l[3:]] == [c4.ILLISIBLE, c4.ILLISIBLE]
        assert l[4]["modele_servi"] == c4.SANS_REPONSE and l[4]["raison_arret"] is None

    def test_fiches_servies_par_repli_portent_la_tentative_servie(self, alim, ff, registre, config):
        consigner(alim, ff, "espece-3", "refus-servie-1", classe=c4.FICHES_RENDUES,
                  fiches=[fiche(1), fiche(2, c4.AU_COFFRE), fiche(3, filiation="fiche-mere-7")])
        l = registre.lignes()
        t, f = l[:2], l[2:]
        assert [x["classe"] for x in f] == [c4.PASSEE, c4.AU_COFFRE, c4.PASSEE]
        assert all(x["rang_repli"] == 1 and x["modele_servi"] == config.modele_reel["m-repli-premier"] for x in f)
        assert all(x["cout_compte_usd"] == "0" for x in f) and t[1]["cout_compte_usd"] == "0.25"
        assert [x["filiation"] for x in f] == [None, None, "fiche-mere-7"]
        assert f[0]["enonce"] == "une idée factice" and f[0]["nom"] == "fiche-1"

    def test_passe_x_sans_case_saine(self, alim, ff, registre):
        consigner(alim, ff, "passe-x", "servie", case=None)
        assert registre.lignes()[0]["case"] is None

    def test_passe_x_avec_case_refusee(self, alim, ff):
        with pytest.raises(c4.DefautLot6V4, match="passe X"):
            consigner(alim, ff, "passe-x", "servie", case="case-00")

    def test_proposeur_sans_case_refuse(self, alim, ff):
        with pytest.raises(c4.DefautLot6V4, match="case servie"):
            consigner(alim, ff, "espece-1", "servie", case=None, classe=c4.VIDE_MOTIVEE)

    def test_classe_servie_manquante_refusee(self, alim, ff):
        with pytest.raises(c4.DefautLot6V4, match="quatre de la V9"):
            consigner(alim, ff, "espece-1", "servie")

    def test_role_non_proposeur_sans_classe(self, alim, ff, registre):
        consigner(alim, ff, "portier", "refus-servie-1")
        assert [x["classe_issue"] for x in registre.lignes()] == [c4.SERVI_PAR_REPLI, c4.CLASSE_HORS_M6]

    def test_role_non_proposeur_servi_au_rang_0(self, alim, ff, registre):
        consigner(alim, ff, "juge-2", "servie")
        assert [x["classe_issue"] for x in registre.lignes()] == [c4.CLASSE_HORS_M6]

    def test_rien_n_est_ecrit_si_une_fiche_est_hors_forme(self, alim, ff, registre):
        mauvaise = fiche(2)
        del mauvaise["idee"]
        with pytest.raises(c4.DefautLot6V4):
            consigner(alim, ff, "espece-3", "refus-servie-1", classe=c4.FICHES_RENDUES, fiches=[fiche(1), mauvaise])
        assert registre.lignes() == []

    def test_fiches_sans_classe_fiches_rendues_refusees(self, alim, ff):
        with pytest.raises(c4.DefautLot6V4, match="si et seulement si"):
            consigner(alim, ff, "espece-1", "servie", classe=c4.VIDE_MOTIVEE, fiches=[fiche(1)])

    def test_registre_factice_refuse_un_champ_hors_liste(self, registre):
        with pytest.raises(sm.RegistreRefuseFactice):
            registre.ajouter({k: None for k in c4.CHAMPS_INTERFACE} | {"score": 1})


# --- comptes ------------------------------------------------------------------------------------------------------------

def jeu(alim, ff):
    consigner(alim, ff, "espece-3", "refus-servie-1", case="case-00", classe=c4.VIDE_MOTIVEE)
    consigner(alim, ff, "espece-3", "servie", case="case-01", classe=c4.REFUS_DU_MODELE)
    consigner(alim, ff, "espece-4", "refus-refus-servie-2", case="case-00", classe=c4.FICHES_RENDUES,
              fiches=[fiche("a"), fiche("b", c4.AU_COFFRE)])
    consigner(alim, ff, "espece-4", "trois-refus", case="case-01")
    consigner(alim, ff, "espece-3", "refus-erreur", case="case-02")
    consigner(alim, ff, "espece-1", "erreur", case="case-00")
    consigner(alim, ff, "espece-1", "servie", case="case-01", classe=c4.FICHES_RENDUES, fiches=[fiche("c")])


class TestComptes:
    def test_m6_par_role_case_espece(self, alim, ff, registre, config):
        jeu(alim, ff)
        m6 = c4.comptes_m6(registre.lignes(), config)["1"]
        assert m6["par_espece"] == {"espece-3": {c4.SERVI_PAR_REPLI: 1, c4.REFUS_DU_MODELE: 1, c4.ILLISIBLE: 1},
                                    "espece-4": {c4.SERVI_PAR_REPLI: 1}, "espece-1": {c4.ILLISIBLE: 1}}
        assert m6["par_role"]["proposeur-espece-3"] == m6["par_espece"]["espece-3"]
        assert m6["par_case"] == {"case-00": {c4.SERVI_PAR_REPLI: 2, c4.ILLISIBLE: 1},
                                  "case-01": {c4.REFUS_DU_MODELE: 1}, "case-02": {c4.ILLISIBLE: 1}}
        assert m6["par_case_et_espece"]["case-00"] == {"espece-3": {c4.SERVI_PAR_REPLI: 1},
                                                       "espece-4": {c4.SERVI_PAR_REPLI: 1}, "espece-1": {c4.ILLISIBLE: 1}}
        assert m6["sous_comptes"] == {"espece-3": {c4.SOUS_COMPTE_EN_REPLI: 1}}

    def test_m6_une_chaine_un_appel(self, alim, ff, registre, config):
        consigner(alim, ff, "espece-3", "refus-refus-servie-2", classe=c4.VIDE_MOTIVEE)
        assert c4.comptes_m6(registre.lignes(), config)["1"]["par_espece"] == {"espece-3": {c4.SERVI_PAR_REPLI: 1}}

    def test_m6_hors_proposeurs(self, alim, ff, registre, config):
        consigner(alim, ff, "portier", "refus-servie-1")
        consigner(alim, ff, "juge-1", "erreur")
        assert c4.comptes_m6(registre.lignes(), config) == {}

    def test_replis_par_espece_et_modele_servi(self, alim, ff, registre, config):
        jeu(alim, ff)
        r = c4.comptes_replis(registre.lignes())["1"]
        p, s = config.modele_reel["m-repli-premier"], config.modele_reel["m-repli-second"]
        assert r["par_espece_et_modele_servi"]["espece-3"] == {
            p: {"nombre": 1, "cout_usd": D("0.25")}, c4.SANS_REPONSE: {"nombre": 1, "cout_usd": D("6.05")}}
        assert r["par_espece_et_modele_servi"]["espece-4"] == {p: {"nombre": 2, "cout_usd": D("0.50")},
                                                               s: {"nombre": 2, "cout_usd": D("0.50")}}
        assert r["par_modele_demande"]["m-repli-premier"]["nombre"] == 4
        assert r["servies_par_repli"][p] == {"tentatives": {c4.VIDE_MOTIVEE: 1}, "fiches": {}}
        assert r["servies_par_repli"][s] == {"tentatives": {c4.FICHES_RENDUES: 1},
                                             "fiches": {c4.PASSEE: 1, c4.AU_COFFRE: 1}}

    def test_m3_scellee_et_especes_seules(self, alim, ff, registre):
        jeu(alim, ff)
        m3 = c4.comptes_m3(registre.lignes())["1"]
        assert m3["scellee"]["case-00"] == {"rendues": 2, c4.AU_COFFRE: 1, c4.HORS_CASE: 0}
        assert "case-00" not in m3["especes_seules"]
        assert m3["especes_seules"]["case-01"] == {"rendues": 1, c4.AU_COFFRE: 0, c4.HORS_CASE: 0}
        assert list(m3["servies_par_repli"]) == [sm.configuration_factice().modele_reel["m-repli-second"]]

    def test_m4_premiere_tentative_seule_et_ligne_replis(self, alim, ff, registre):
        jeu(alim, ff)
        m4 = c4.comptes_m4(registre.lignes())["1"]
        assert m4["par_espece"]["espece-3"] == {"cout_usd": D("0.75"), "fiches_passees": 0}
        assert m4["par_espece"]["espece-4"] == {"cout_usd": D("0.50"), "fiches_passees": 0}
        assert m4["par_espece"]["espece-1"] == {"cout_usd": D("6.30"), "fiches_passees": 1}
        assert m4["replis"]["cout_usd"] == D("7.30") and m4["replis"]["fiches_passees"] == 1
        total = sum(D(l["cout_compte_usd"]) for l in registre.lignes())
        assert total == sum(e["cout_usd"] for e in m4["par_espece"].values()) + m4["replis"]["cout_usd"]

    def test_comptes_serialisables_et_ecrits(self, alim, ff, registre, config, tmp_path):
        jeu(alim, ff)
        ch = c4.ecrire_comptes(str(tmp_path), c4.comptes_v4(registre.lignes(), config))
        assert os.path.basename(ch) == "comptes-tentatives-et-replis-na-v4.json"
        with pytest.raises(FileExistsError):
            c4.ecrire_comptes(str(tmp_path), {})


# --- garde du coffre (n° 5) -------------------------------------------------------------------------------------------

class TestGardeDuCoffre:
    def test_un_quart_exactement_part(self, alim, ff, registre):
        consigner(alim, ff, "espece-1", "servie", classe=c4.FICHES_RENDUES,
                  fiches=[fiche(1, c4.AU_COFFRE), fiche(2), fiche(3), fiche(4)])
        k = c4.garde_du_coffre_v4(registre.lignes(), 1)
        assert (k.au_coffre, k.rendues, k.depasse) == (1, 4, False)

    def test_fiche_servie_par_repli_au_coffre_compte(self, alim, ff, registre):
        consigner(alim, ff, "espece-1", "servie", classe=c4.FICHES_RENDUES, fiches=[fiche(1, c4.AU_COFFRE), fiche(2),
                                                                                    fiche(3)])
        consigner(alim, ff, "espece-3", "refus-servie-1", case="case-01", classe=c4.FICHES_RENDUES,
                  fiches=[fiche(4, c4.AU_COFFRE)])
        with pytest.raises(c4.ArretGardeCoffreV4) as e:
            c4.garde_du_coffre_v4(registre.lignes(), 1)
        assert (e.value.au_coffre, e.value.rendues, e.value.dont_repli, e.value.numero) == (2, 4, 1, 5)

    def test_les_lignes_de_tentative_ne_diluent_pas(self, alim, ff, registre):
        # 2 au coffre sur 4 fiches, plus des lignes de tentative sans fiche : compter toutes les lignes donnerait 2/9
        consigner(alim, ff, "espece-1", "servie", classe=c4.FICHES_RENDUES,
                  fiches=[fiche(1, c4.AU_COFFRE), fiche(2, c4.AU_COFFRE), fiche(3), fiche(4)])
        for i in range(4):
            consigner(alim, ff, "espece-3", "trois-refus", case=f"case-{i + 1:02d}")
        lignes = registre.lignes()
        assert 4 * 2 <= len([l for l in lignes if l["generation"] == 1])  # la lecture du lot 5 v1 ne lèverait pas
        with pytest.raises(c4.ArretGardeCoffreV4):
            c4.garde_du_coffre_v4(lignes, 1)

    def test_troisieme_generation_consignee(self, alim, ff, registre):
        consigner(alim, ff, "espece-1", "servie", g=3, classe=c4.FICHES_RENDUES, fiches=[fiche(1, c4.AU_COFFRE)])
        k = c4.garde_du_coffre_v4(registre.lignes(), 3)
        assert k.depasse and k.consigne


# --- contrôle du code chargé (n° 33, C-1 à C-4) ----------------------------------------------------------------------

def _module(nom, fichier):
    m = types.ModuleType(nom)
    m.__file__ = fichier
    return m


@pytest.fixture
def paquet(tmp_path):
    racine = tmp_path / "paquet"
    (racine / "pole").mkdir(parents=True)
    a = racine / "pole" / "a.py"
    a.write_text("X = 1\n")
    table = racine / "table.txt"
    table.write_text(f"{hashlib.sha256(a.read_bytes()).hexdigest()}  pole/a.py\n")
    t = c4.lire_table_empreintes(str(table), hashlib.sha256(table.read_bytes()).hexdigest())
    return racine, t, {"pole.a": _module("pole.a", str(a)), "json": sys.modules["json"]}


class TestCodeCharge:
    def test_table_egale_depart(self, paquet):
        racine, t, mods = paquet
        assert c4.verifier_code_charge(t, str(racine), "départ", modules=mods) == ["pole/a.py"]

    def test_module_plante_hors_table(self, paquet):
        racine, t, mods = paquet
        b = racine / "pole" / "plante.py"
        b.write_text("Y = 2\n")
        mods["pole.plante"] = _module("pole.plante", str(b))
        with pytest.raises(c4.ArretCodeChargeNA, match="hors table") as e:
            c4.verifier_code_charge(t, str(racine), "génération 2", modules=mods)
        assert e.value.numero == 33

    def test_module_sous_la_racine_sans_espace_protege(self, paquet):
        racine, t, mods = paquet
        b = racine / "autre.py"
        b.write_text("Z = 3\n")
        mods["autre"] = _module("autre", str(b))
        with pytest.raises(c4.ArretCodeChargeNA, match="hors table"):
            c4.verifier_code_charge(t, str(racine), "départ", modules=mods)

    def test_fichier_modifie_autre_empreinte(self, paquet):
        racine, t, mods = paquet
        (racine / "pole" / "a.py").write_text("X = 2\n")
        with pytest.raises(c4.ArretCodeChargeNA, match="autre empreinte"):
            c4.verifier_code_charge(t, str(racine), "départ", modules=mods)

    def test_module_protege_hors_racine(self, paquet, tmp_path):
        racine, t, mods = paquet
        b = tmp_path / "ailleurs.py"
        b.write_text("W = 4\n")
        mods["pole.ailleurs"] = _module("pole.ailleurs", str(b))
        with pytest.raises(c4.ArretCodeChargeNA, match="hors de la racine"):
            c4.verifier_code_charge(t, str(racine), "départ", modules=mods)

    def test_module_protege_sans_source(self, paquet):
        racine, t, mods = paquet
        mods["pole.compile"] = _module("pole.compile", str(racine / "pole" / "x.pyc"))
        with pytest.raises(c4.ArretCodeChargeNA, match="source"):
            c4.verifier_code_charge(t, str(racine), "départ", modules=mods)

    def test_table_d_une_autre_empreinte(self, paquet):
        racine, _, _ = paquet
        with pytest.raises(c4.ArretCodeChargeNA, match="table d'une autre empreinte"):
            c4.lire_table_empreintes(str(racine / "table.txt"), "0" * 64)

    def test_espace_de_noms_sous_la_racine_sain_et_hors_racine_refuse(self, paquet, tmp_path):
        racine, t, mods = paquet
        ns = types.ModuleType("pole")
        ns.__file__ = None
        ns.__path__ = [str(racine / "pole")]
        assert c4.verifier_code_charge(t, str(racine), "départ", modules=dict(mods, pole=ns)) == ["pole/a.py"]
        ns.__path__ = [str(tmp_path)]
        with pytest.raises(c4.ArretCodeChargeNA, match="espace de noms"):
            c4.verifier_code_charge(t, str(racine), "départ", modules=dict(mods, pole=ns))

    def test_sur_le_vrai_sys_modules(self):
        """Le paquet de ce lot, vérifié sur l'interpréteur des essais, avec la table écrite à la volée."""
        racine = os.path.dirname(os.path.dirname(os.path.abspath(c4.__file__)))
        t = {}
        for nom in ("course_na_v4.py", "simulation_na_v4.py"):
            with open(os.path.join(racine, "pole", nom), "rb") as f:
                t[os.path.join("pole", nom)] = hashlib.sha256(f.read()).hexdigest()
        mods = {k: v for k, v in sys.modules.items() if k in ("pole.course_na_v4", "pole.simulation_na_v4")}
        assert c4.verifier_code_charge(t, racine, "départ", modules=mods) == sorted(t)

    def test_limite_c3_modification_en_memoire_non_vue(self, paquet):
        """C-3, réserve déclarée : ce que le contrôle ne voit pas, éprouvé comme non vu (et non comme refusé)."""
        racine, t, mods = paquet

        def f():
            return 1

        def g():
            return 2

        m = mods["pole.a"]
        m.f = f
        f.__code__ = g.__code__
        assert c4.verifier_code_charge(t, str(racine), "génération 2", modules=mods) == ["pole/a.py"]
        assert "mémoire" in c4.RESERVE_C3


# --- course simulée, différentiel avec le v3 ------------------------------------------------------------------------

class TestCourseSimulee:
    def test_trois_generations_rejouables(self, tmp_path):
        (tmp_path / "a").mkdir()
        (tmp_path / "b").mkdir()
        ra, ka, ca = sm.course_simulee(str(tmp_path / "a"))
        rb, kb, cb = sm.course_simulee(str(tmp_path / "b"))
        assert ca == cb and len(ka) == 3 and ra.sceller() == rb.sceller()
        lignes = ra.lignes()
        chaines = {l["identifiant"].rsplit(".t", 1)[0] for l in c4.lignes_tentatives(lignes)}
        assert len(chaines) == 3 * 11 * 5
        assert len([l for l in c4.lignes_tentatives(lignes) if l["rang_repli"] == 0]) == len(chaines)

    def test_garde_du_coffre_arrete_la_course_simulee(self, tmp_path):
        with pytest.raises(c4.ArretGardeCoffreV4) as e:
            sm.course_simulee(str(tmp_path), part_coffre=0.9)
        assert e.value.generation == 1

    def test_partition_des_chaines(self, tmp_path):
        registre, _, c = sm.course_simulee(str(tmp_path))
        reg = registre.lignes()
        rang0 = [l for l in c4.lignes_tentatives(reg) if l["rang_repli"] == 0]
        m6 = sum(n for g in c["m6"].values() for d in g["par_espece"].values() for n in d.values())
        hors = sum(1 for l in rang0 if l["classe_issue"] in (c4.FICHES_RENDUES, c4.CLASSE_ARRET_1))
        assert m6 + hors == len(rang0)


def issues_v3(appels):
    """Oracle : `_classer_retour_proposeur` du v3 (C3:415-445), recopié pour ses seules issues, sur les dictionnaires du
    lot 4 v1 (une tentative, pas de repli : un refus est l'arrêt n° 1)."""
    c = {}
    for a in appels:
        k = {"ok": "texte rendu, au portier", "arrêt n° 1, consigné, non relancé": "arrêt n° 1, consigné, non relancé",
             "réponse illisible, cause non établie": "réponse illisible, cause non établie"}[a["issue_na"]]
        c[k] = c.get(k, 0) + 1
    return c


class TestDifferentielV3:
    SCEN_V1 = {"servie": "ok", "trois-refus": "arrêt n° 1, consigné, non relancé",
               "erreur": "réponse illisible, cause non établie"}

    def test_sans_repli_memes_comptes_que_le_v3(self, alim, ff, registre):
        scen = ["servie", "erreur", "servie", "servie", "erreur"]
        for i, s in enumerate(scen):
            consigner(alim, ff, "espece-1", s, case=f"case-{i:02d}", classe=c4.VIDE_MOTIVEE if s == "servie" else None)
        v3 = issues_v3([{"issue_na": self.SCEN_V1[s]} for s in scen])
        r0 = [l for l in c4.lignes_tentatives(registre.lignes()) if l["rang_repli"] == 0]
        assert v3["texte rendu, au portier"] == sum(1 for l in r0 if l["raison_arret"] not in (None, "refusal"))
        assert v3["réponse illisible, cause non établie"] == sum(1 for l in r0 if l["classe_issue"] == c4.ILLISIBLE)

    def test_avec_repli_l_ecart_au_v3_est_celui_de_p12(self, alim, ff, registre, config):
        consigner(alim, ff, "espece-3", "refus-servie-1", classe=c4.VIDE_MOTIVEE)
        v3 = issues_v3([{"issue_na": "arrêt n° 1, consigné, non relancé"}])  # le v3 s'arrête au premier refus
        m6 = c4.comptes_m6(registre.lignes(), config)["1"]["par_espece"]["espece-3"]
        assert v3 == {"arrêt n° 1, consigné, non relancé": 1} and m6 == {c4.SERVI_PAR_REPLI: 1}
