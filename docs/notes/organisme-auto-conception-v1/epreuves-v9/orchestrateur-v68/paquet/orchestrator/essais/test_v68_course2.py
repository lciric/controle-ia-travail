"""Essais de la v68 — course 2 réparée (`pole/course2_v68.py`), garde de budget de la course (`pole/budget_course_v68.py`),
montant requis (`pole/configuration_v68.py`), moteur simulé v68 (`pole/simulation_v68.py`), lanceur (`demonstrations/ideation_v68.py`).

Hors ligne : aucun réseau, aucun modèle, aucune clé, aucune dépense (coûts fictifs du moteur simulé). L'étage de tests de mort
est l'étage v5 réel, joué avec l'**exécuteur factice demandé explicitement** (python du système dans un processus à part, sans
`bwrap` : aucune barrière ; le vrai bac à sable n'est pas joué ici). Chaque garde et chaque refus : un cas sain et un artefact
(R5). Courses de bout en bout sur **deux générations**, interrupteurs allumés (lecture de la sélection ; tests de mort sans rien
servir) puis éteints. Aucun tirage aléatoire hors des graines de l'orchestrateur (R9 : `SeedSequence` par tâche, inchangé)."""

import contextlib
import hashlib
import importlib.util
import inspect
import io
import json
import os
import shutil
import sys
import tempfile
import unittest
from unittest import mock

ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(ICI)
sys.path.insert(0, ICI)

import aides  # noqa: E402  (`aides.BASE` lu à l'appel : redirigé par conftest)
import aides_v56 as A56  # noqa: E402
import aides_v68 as A  # noqa: E402
from aides import CasAvecDossier  # noqa: E402
from pole import budget_course_v68 as bc  # noqa: E402
from pole import configuration_v54 as c54cfg  # noqa: E402
from pole import configuration_v56 as cfg  # noqa: E402
from pole import configuration_v68 as cfg68  # noqa: E402
from pole import course2_v54 as c54  # noqa: E402
from pole import course2_v56 as c56  # noqa: E402
from pole import course2_v59 as c59  # noqa: E402
from pole import course2_v68 as c68  # noqa: E402
from pole import fiches_v54 as fv  # noqa: E402
from pole import simulation_v68 as s68  # noqa: E402
from pole import tests_de_mort_v5 as v5  # noqa: E402
from pole.boucle_fermee_v59 import HeritageRefuse, SelectionNonVerifiee  # noqa: E402
from pole.configuration_v53 import ConfigurationRefusee, GoRefuse  # noqa: E402
from pole.etage_entre_generations_v53 import MachineNonJetable  # noqa: E402
from pole.etage_entre_generations_v57 import NOM_SELECTION  # noqa: E402
from pole.etage_entre_generations_v57 import VERSION as VERSION_V57  # noqa: E402
from pole.outils import EcrasementInterdit, ecrire_json_scelle, sha256_fichier, verifier_scelle  # noqa: E402
from pole.tests_de_mort_v4 import ETIQUETTE_NOYAU  # noqa: E402

S17, PLAFOND_ETAGE = 50.0, 5.0
TITRE = c68.TITRE_HERITAGE_SELECTION


def lire(chemin):
    with open(chemin, encoding="utf-8") as f:
        return json.load(f)


def dossier_de_classe(cls):
    os.makedirs(aides.BASE, exist_ok=True)
    d = tempfile.mkdtemp(dir=aides.BASE)
    cls.addClassCleanup(shutil.rmtree, d, True)
    return d


def conf_lue(dossier, **modifs):
    return cfg.lire_configuration_v56(A.configuration(dossier, **modifs), base=dossier)


def course(dossier, nom, *, n=2, lecture, apres, etage=True, plafond=None, conf=None, classe=A.AdaptateurEnregistreurV68,
           env=None, **kw):
    """Une course v68 en moteur simulé ; rend (bilan ou exception, adaptateurs, conf, chemin de la sortie)."""
    conf = conf or conf_lue(dossier)
    ad = A.adaptateurs(conf, classe=classe)
    et = A.etage(conf, ad) if etage else None
    if plafond is None:
        e = cfg68.nombre_etages_v68(n, et is not None, apres)
        plafond = n * S17 + e * PLAFOND_ETAGE
    sortie = os.path.join(dossier, nom)
    try:
        r = c68.executer_course_v68(conf, sortie, ad, nombre_generations=n, go={"essai": True}, lecture_selection=lecture,
                                    etage_apres_derniere=apres, plafond_course_usd=plafond, etage=et,
                                    environnement=A.JETABLE if env is None else env,
                                    racine_sessions=os.path.join(dossier, "sessions-" + nom), **kw)
    except Exception as e:  # noqa: BLE001 — rendue à l'essai, jamais avalée
        r = e
    return r, ad, conf, sortie


def lignes_selection(sortie, g):
    sel = lire(os.path.join(sortie, f"etage-apres-generation-{g}", NOM_SELECTION))
    fiches = {x["identifiant_auteur"]: x for x in lire(os.path.join(sortie, f"etage-apres-generation-{g}", "fiches-validees.json"))}
    garder = [f"- {fiches[i]['nom']} : {fiches[i]['enonce']}" for i in sel["retenues"]]
    exclure = [f"- {fiches[x['identifiant_auteur']]['nom']} : " for x in sel["exclues"]]
    return garder, exclure


# --- montant requis (précision i) ------------------------------------------------------------------------------------------------


class TestMontantRequisV68(unittest.TestCase):
    CONF = {"budget": {"plafond_usd": 150.0, "portee_plafond": "par_generation"}}

    def test_cas_sain_n_generations_e_etages(self):
        self.assertEqual(cfg68.montant_requis_v68(self.CONF, 2, 5.0, nombre_etages=1), 305.0)
        self.assertEqual(cfg68.montant_requis_v68(self.CONF, 2, 5.0, nombre_etages=2), 310.0)
        self.assertEqual(cfg68.montant_requis_v68(self.CONF, 1, 5.0, nombre_etages=1), 155.0)
        self.assertEqual(cfg68.montant_requis_v68(self.CONF, 3, None, nombre_etages=0), 450.0)
        course = {"budget": {"plafond_usd": 150.0, "portee_plafond": "course"}}
        self.assertEqual(cfg68.montant_requis_v68(course, 1, None, nombre_etages=0), 150.0)

    def test_egal_a_la_v54_pour_n_moins_un_etages(self):
        for n in (1, 2, 3):
            with self.subTest(n=n):
                self.assertEqual(cfg68.montant_requis_v68(self.CONF, n, 5.0, nombre_etages=n - 1),
                                 c54cfg.montant_requis(self.CONF, n, 5.0))

    def test_artefacts_refuses(self):
        course = {"budget": {"plafond_usd": 150.0, "portee_plafond": "course"}}
        autre = {"budget": {"plafond_usd": 150.0, "portee_plafond": "generation"}}
        cas = [(course, 2, 5.0, 1), (course, 2, None, 0), (course, 1, 5.0, 1), (autre, 1, None, 0), (self.CONF, 2, 5.0, 3),
               (self.CONF, 2, 5.0, -1), (self.CONF, 2, None, 1), (self.CONF, 2, 0.0, 1), (self.CONF, 0, None, 0),
               (self.CONF, True, None, 0), (self.CONF, 2, 5.0, True)]
        for conf, n, p, e in cas:
            with self.subTest(portee=conf["budget"]["portee_plafond"], n=n, p=p, e=e), self.assertRaises(ConfigurationRefusee):
                cfg68.montant_requis_v68(conf, n, p, nombre_etages=e)

    def test_nombre_etages(self):
        self.assertEqual(cfg68.nombre_etages_v68(2, True, False), 1)
        self.assertEqual(cfg68.nombre_etages_v68(2, True, True), 2)
        self.assertEqual(cfg68.nombre_etages_v68(1, True, True), 1)
        self.assertEqual(cfg68.nombre_etages_v68(3, False, False), 0)
        for args in ((2, False, True), (0, True, True), (2, 1, False), (2, True, None)):
            with self.subTest(args=args), self.assertRaises(ConfigurationRefusee):
                cfg68.nombre_etages_v68(*args)


# --- garde de budget de la course (exigence bloquante) -------------------------------------------------------------------------


class TestGardeBudgetCourseV68(unittest.TestCase):
    def test_cas_sain_cumul_sur_la_course(self):
        g = bc.GardeBudgetCourseV68(110.0)
        g.reserver("generation-1", 50.0)
        g.compter("generation-1", 0.81)
        g.reserver("etage-apres-generation-1", 5.0)
        g.compter("etage-apres-generation-1", None, inconnu=True)  # coût inconnu : la réservation entière
        g.reserver("generation-2", 50.0)
        g.compter("generation-2", 0.81)
        e = g.etat()
        self.assertAlmostEqual(e["cumul_usd"], 6.62)
        self.assertEqual(e["depassement_usd"], 0.0)
        self.assertAlmostEqual(bc.rejouer_journal_course_v68(e), 6.62)
        self.assertEqual([j["quoi"] for j in e["journal"]], ["reserve", "compte"] * 3)

    def test_arret_au_plafond_de_la_course_avant_le_poste(self):
        g = bc.GardeBudgetCourseV68(60.0)
        g.reserver("generation-1", 50.0)
        g.compter("generation-1", 12.0)
        with self.assertRaises(bc.PlafondDeCourseAtteint):
            g.reserver("generation-2", 50.0)  # 12 + 50 > 60 : non lancé
        self.assertIsNone(g.en_cours)
        self.assertEqual(g.etat()["journal"][-1]["quoi"], "refuse")
        self.assertAlmostEqual(g.cumul, 12.0)
        g.reserver("etage-apres-generation-1", 5.0)  # 12 + 5 ≤ 60 : tient
        g.compter("etage-apres-generation-1", 5.0)

    def test_artefact_cout_au_dela_de_la_reservation(self):
        g = bc.GardeBudgetCourseV68(500.0)
        g.reserver("generation-1", 50.0)
        with self.assertRaises(bc.CumulCourseAuDela):
            g.compter("generation-1", 50.02)
        self.assertAlmostEqual(g.cumul, 50.02)  # compté en entier, jamais écrêté
        with self.assertRaises(bc.CumulCourseAuDela):
            bc.rejouer_journal_course_v68(g.etat())

    def test_artefacts_usage_fautif(self):
        for p in (0, -1, None, True, "50"):
            with self.subTest(plafond=p), self.assertRaises(bc.BudgetCourseRefuse):
                bc.GardeBudgetCourseV68(p)
        g = bc.GardeBudgetCourseV68(100.0)
        with self.assertRaises(bc.BudgetCourseRefuse):
            g.compter("generation-1", 1.0)  # sans réservation
        g.reserver("generation-1", 10.0)
        with self.assertRaises(bc.BudgetCourseRefuse):
            g.reserver("generation-2", 10.0)  # un poste encore en cours
        with self.assertRaises(bc.BudgetCourseRefuse):
            g.compter("generation-1", -1.0)
        g.compter("generation-1", 1.0)
        with self.assertRaises(bc.BudgetCourseRefuse):
            g.reserver("generation-1", 1.0)  # jamais rejoué
        with self.assertRaises(bc.BudgetCourseRefuse):
            g.reserver("generation-2", -3)

    def test_noter_arret_ne_leve_jamais(self):
        g = bc.GardeBudgetCourseV68(100.0)
        g.reserver("generation-1", 50.0)
        self.assertEqual(g.noter_arret("generation-1", None), 50.0)  # inconnu : réservation
        self.assertIsNone(g.noter_arret("generation-1", 3.0))  # plus rien en cours
        g.reserver("generation-2", 40.0)
        self.assertEqual(g.noter_arret("generation-2", 80.0), 80.0)  # au-delà : noté, sans lever

    def test_artefact_journal_trafique(self):
        g = bc.GardeBudgetCourseV68(100.0)
        g.reserver("generation-1", 50.0)
        g.compter("generation-1", 10.0)
        e = g.etat()
        e["cumul_usd"] = 1.0
        with self.assertRaises(bc.CumulCourseAuDela):
            bc.rejouer_journal_course_v68(e)


# --- la sélection lue en objet ; A4 ligne par ligne ------------------------------------------------------------------------------


def etage_ecrit(dossier, fiches, retenues, sceller_fiches=True, version=VERSION_V57):
    os.makedirs(dossier)
    chemin = os.path.join(dossier, "fiches-validees.json")
    if sceller_fiches:
        ecrire_json_scelle(chemin, fiches)
    else:
        with open(chemin, "w", encoding="utf-8") as f:
            json.dump(fiches, f)
    return ecrire_json_scelle(os.path.join(dossier, NOM_SELECTION), {"version": version, "retenues": retenues, "exclues": [],
                                                                      "regle": "essai"})


FICHES = [{"identifiant_auteur": "f1", "nom": "Fiche une", "enonce": "énoncé un"},
          {"identifiant_auteur": "f2", "nom": "Fiche  deux", "enonce": "énoncé\ndeux ## Case piégée"},
          {"identifiant_auteur": "f3", "nom": "Fiche trois", "enonce": "énoncé trois"}]


class TestLignesDepuisSelectionV68(CasAvecDossier):
    def test_cas_sain_retenues_seules_une_ligne_chacune(self):
        sha = etage_ecrit(os.path.join(self.tmp, "e"), FICHES, ["f2", "f3"])
        h = c68.lignes_depuis_selection_v68(os.path.join(self.tmp, "e"), sha, 1)
        self.assertEqual(h["lignes"], [{"identifiant_auteur": "f2", "nom": "Fiche deux", "enonce": "énoncé deux ## Case piégée"},
                                       {"identifiant_auteur": "f3", "nom": "Fiche trois", "enonce": "énoncé trois"}])
        self.assertEqual((h["selection_sha256"], h["depuis_generation"], h["type"]), (sha, 1, c68.TYPE_HERITAGE))
        c68.verifier_heritage_selection(h)
        texte59 = c59.heritage_depuis_selection(os.path.join(self.tmp, "e"), sha)  # mêmes retenues que la v59
        self.assertIn("Fiche trois : énoncé trois", texte59)
        self.assertNotIn("Fiche une", texte59)

    def test_artefacts_refuses(self):
        d = os.path.join(self.tmp, "e")
        sha = etage_ecrit(d, FICHES, ["f1"])
        with self.assertRaises(SelectionNonVerifiee):
            c68.lignes_depuis_selection_v68(d, "1" * 64, 1)  # empreinte autre que celle consignée
        with self.assertRaises(SelectionNonVerifiee):
            c68.lignes_depuis_selection_v68(d, None, 1)
        d2 = os.path.join(self.tmp, "e2")
        sha2 = etage_ecrit(d2, FICHES, ["f1"], sceller_fiches=False)
        with self.assertRaises(HeritageRefuse):
            c68.lignes_depuis_selection_v68(d2, sha2, 1)  # fiches non scellées
        d3 = os.path.join(self.tmp, "e3")
        sha3 = etage_ecrit(d3, FICHES, ["f9"])
        with self.assertRaises(HeritageRefuse):
            c68.lignes_depuis_selection_v68(d3, sha3, 1)  # retenue absente
        d4 = os.path.join(self.tmp, "e4")
        sha4 = etage_ecrit(d4, FICHES, ["f1"], version="autre")
        with self.assertRaises(HeritageRefuse):
            c68.lignes_depuis_selection_v68(d4, sha4, 1)
        d5 = os.path.join(self.tmp, "e5")
        sha5 = etage_ecrit(d5, [{"identifiant_auteur": "f1", "nom": None, "enonce": "x"}], ["f1"])
        with self.assertRaises(HeritageRefuse):
            c68.lignes_depuis_selection_v68(d5, sha5, 1)  # aucun champ inventé
        self.assertTrue(sha)


H = {"type": c68.TYPE_HERITAGE, "selection_sha256": "a" * 64, "depuis_generation": 1,
     "lignes": [{"identifiant_auteur": "f1", "nom": "Fiche une", "enonce": "énoncé sain"},
                {"identifiant_auteur": "f2", "nom": "Fiche deux", "enonce": "un témoin caché"}]}
INTERDITES, MODE = A56.INTERDITES, "prefixe"


class TestRendreHeritageV68(unittest.TestCase):
    def test_cas_sain(self):
        h = dict(H, lignes=H["lignes"][:1])
        corps, etat = c68.rendre_heritage_v68(h, INTERDITES, MODE, "arret", selection_vide="omettre", titre=TITRE)
        self.assertEqual(corps, "- Fiche une : énoncé sain")
        self.assertEqual((etat["section"], etat["retenues"], etat["servies"], etat["exclues_a4"]), ("servie", 1, 1, []))
        self.assertEqual(etat["texte_sha256"], hashlib.sha256(("## " + TITRE + "\n" + corps + "\n").encode()).hexdigest())

    def test_a4_ligne_exclue_ou_arret(self):
        vus = []
        corps, etat = c68.rendre_heritage_v68(H, INTERDITES, MODE, "fiche_exclue", selection_vide="omettre", titre=TITRE,
                                              evenement=lambda quoi, **k: vus.append((quoi, k)))
        self.assertEqual(corps, "- Fiche une : énoncé sain")
        self.assertEqual(etat["exclues_a4"], ["f2"])
        self.assertEqual(vus, [("incident-a4-heritage-ligne-exclue", {"etiquettes": ["témoin"]})])
        with self.assertRaises(fv.EtiquetteDansEntree):
            c68.rendre_heritage_v68(H, INTERDITES, MODE, "arret", selection_vide="omettre", titre=TITRE)

    def test_selection_vide_omettre_par_defaut_ou_servir(self):
        vide = dict(H, lignes=[])
        self.assertEqual(c68.SELECTION_VIDE_DEFAUT, "omettre")
        corps, etat = c68.rendre_heritage_v68(vide, INTERDITES, MODE, "arret", selection_vide="omettre", titre=TITRE)
        self.assertIsNone(corps)
        self.assertEqual((etat["section"], etat["texte_sha256"]), ("omise (sélection vide)", None))
        corps, etat = c68.rendre_heritage_v68(vide, INTERDITES, MODE, "arret", selection_vide="servir_vide", titre=TITRE)
        self.assertEqual((corps, etat["section"]), (c68.LIGNE_SELECTION_VIDE, "servie vide"))
        seule = dict(H, lignes=H["lignes"][1:])  # toutes exclues par A4
        corps, etat = c68.rendre_heritage_v68(seule, INTERDITES, MODE, "fiche_exclue", selection_vide="omettre", titre=TITRE)
        self.assertEqual((corps, etat["section"]), (None, "omise (toutes les lignes exclues par A4)"))
        with self.assertRaises(ConfigurationRefusee):
            c68.rendre_heritage_v68(vide, INTERDITES, MODE, "arret", selection_vide="vide", titre=TITRE)


# --- la génération : héritage objet seulement ; _proposer = la v54 au titre près ; le défaut de la v59 -----------------------


class TestGenerationV68(CasAvecDossier):
    def gen(self, nom="g", **kw):
        conf = conf_lue(self.tmp)
        return c68.GenerationV68(conf, os.path.join(self.tmp, nom), A.adaptateurs(conf), racine_sessions=os.path.join(self.tmp, "s-" + nom), **kw)

    def test_artefacts_heritage_texte_refuse_avant_ecriture(self):
        texte59 = "# Héritage : fiches retenues par la sélection scellée…\n- a : b\n"
        for kw in ({"heritage_texte": texte59}, {"heritage_texte": json.dumps([{"titre": "t", "resume": "r", "notable": True}])},
                   {"heritage_selection": texte59}, {"heritage_selection": dict(H, type="autre")},
                   {"heritage_selection": dict(H, lignes=[{"identifiant_auteur": "f1", "nom": "n"}])},
                   {"heritage_selection": dict(H, selection_sha256="court")}):
            with self.subTest(kw=str(kw)[:60]), self.assertRaises(c68.HeritageNonSelection):
                self.gen(nom="x", **kw)
            self.assertFalse(os.path.exists(os.path.join(self.tmp, "x")))
        for kw in ({"selection_vide": "vide"}, {"titre_heritage": ""}, {"titre_heritage": "a\nb"}):
            with self.subTest(kw=kw), self.assertRaises(ConfigurationRefusee):
                self.gen(nom="x", **kw)
            self.assertFalse(os.path.exists(os.path.join(self.tmp, "x")))

    def test_cas_sain_heritage_garde_et_etat(self):
        g = self.gen(heritage_selection=dict(H, lignes=H["lignes"][:1]))
        self.assertEqual(g._heritage_garde(), "- Fiche une : énoncé sain")
        self.assertEqual(g.heritage_lu()["section"], "servie")
        self.assertIsNone(self.gen(nom="g2")._heritage_garde())
        self.assertIsNone(self.gen(nom="g3").heritage_lu())

    def test_a4_sur_l_heritage_selon_la_configuration(self):
        g = self.gen(heritage_selection=H)  # a4.action = « arret » dans la configuration d'essai
        with self.assertRaises(fv.EtiquetteDansEntree):
            g._heritage_garde()

    def test_proposer_est_la_v54_au_titre_pres(self):
        a = inspect.getsource(c54.GenerationV54._proposer)
        b = inspect.getsource(c68.GenerationV68._proposer)
        ancien = '                    consigne += "\\n## Fiches de la génération précédente (titres, résumés, verdict agrégé)\\n" + heritage + "\\n"\n'
        neuf = ('                    consigne += "\\n## " + self.titre_heritage + "\\n" + heritage + "\\n"\n'
                '                    self.consignes_avec_heritage += 1\n')
        self.assertIn(ancien, a)
        self.assertEqual(a.replace(ancien, neuf), b)
        self.assertNotIn("verdict agrégé", b)

    def test_defaut_v59_reproduit_sur_la_seule_methode(self):
        """Le texte de la v59, lu par la garde de la v54 (héritée par la v56) : JSONDecodeError — le défaut épinglé au rang 0."""
        d = os.path.join(self.tmp, "e")
        sha = etage_ecrit(d, FICHES, ["f1"])
        texte = c59.heritage_depuis_selection(d, sha)
        conf = conf_lue(self.tmp)
        g56 = c56.GenerationV56(conf, os.path.join(self.tmp, "g56"), A.adaptateurs(conf), heritage_texte=texte,
                                racine_sessions=os.path.join(self.tmp, "s-g56"))
        with self.assertRaises(json.JSONDecodeError):
            g56._heritage_garde()
        g68 = self.gen(heritage_selection=c68.lignes_depuis_selection_v68(d, sha, 1))
        self.assertEqual(g68._heritage_garde(), "- Fiche une : énoncé un")


# --- refus de la course avant toute écriture --------------------------------------------------------------------------------------


class TestRefusAvantToutV68(CasAvecDossier):
    def setUp(self):
        super().setUp()
        self.conf = conf_lue(self.tmp)
        self.ad = A.adaptateurs(self.conf)
        self.et = A.etage(self.conf, self.ad)

    def refuse(self, motif, exc=ConfigurationRefusee, *, n=2, lecture=False, apres=False, etage="oui", plafond=105.0, env=None,
               conf=None, **kw):
        """Refus attendu **pour le motif dit** (montant requis par défaut : 2 × 50 + 1 × 5 = 105), sortie jamais créée."""
        sortie = os.path.join(self.tmp, "c")
        et = self.et if etage == "oui" else etage
        with self.assertRaises(exc) as cm:
            c68.executer_course_v68(conf or self.conf, sortie, self.ad, nombre_generations=n, go={}, lecture_selection=lecture,
                                    etage_apres_derniere=apres, plafond_course_usd=plafond, etage=et,
                                    environnement=A.JETABLE if env is None else env, **kw)
        self.assertIn(motif, str(cm.exception))
        self.assertFalse(os.path.exists(sortie))

    def test_cas_sain_les_memes_arguments_passent_les_gardes(self):
        """Témoin des refus ci-dessous : les arguments par défaut de `refuse` passent toutes les gardes d'avant écriture."""
        regime = c68.verifier_regime_v68(self.conf, nombre_generations=2, lecture_selection=False, etage_present=True,
                                         etage_apres_derniere=False, plafond_etage_usd=5.0)
        self.assertEqual(regime["montant_requis_usd"], 105.0)
        self.assertTrue(c68.verifier_etage_v68(self.et))
        from pole.etage_entre_generations_v56 import exiger_machine_jetable_v56
        self.assertTrue(exiger_machine_jetable_v56(A.JETABLE))
        self.assertTrue(c68.verifier_heritage_selection(H))

    def test_regimes_cas_sains(self):
        r = lambda **k: c68.verifier_regime_v68(self.conf, **k)["nom"]  # noqa: E731
        self.assertEqual(r(nombre_generations=2, lecture_selection=False, etage_present=False, etage_apres_derniere=False), "eteint")
        self.assertEqual(r(nombre_generations=1, lecture_selection=False, etage_present=True, etage_apres_derniere=True,
                           plafond_etage_usd=5.0), "tests_de_mort_sans_rien_servir")
        self.assertEqual(r(nombre_generations=2, lecture_selection=True, etage_present=True, etage_apres_derniere=False,
                           plafond_etage_usd=5.0), "lecture_de_la_selection")

    def test_artefacts_regime(self):
        self.refuse("nombre de générations", n=0)
        self.refuse("nombre de générations", n=True)
        self.refuse("booléens", lecture=None)
        self.refuse("booléens", apres="oui")
        self.refuse("une seule génération", n=1, lecture=True, plafond=55.0)
        self.refuse("lecture de la sélection sans étage", lecture=True, etage=None, plafond=100.0)
        self.refuse("après la dernière génération demandé sans étage", apres=True, etage=None, plafond=100.0)
        self.refuse("selection_vide", selection_vide="rien")
        for t, motif in (("", "titre"), ("deux\nlignes", "titre"), ("Fiches exploratoires", "étiquette interdite")):
            with self.subTest(titre=t):
                self.refuse(motif, titre_heritage=t)

    def test_artefact_portee_course_avec_plusieurs_generations(self):
        conf = conf_lue(self.tmp, budget__portee_plafond="course")
        self.refuse("portee_plafond « course » refusée", conf=conf, etage=None, plafond=50.0)
        self.refuse("portee_plafond « course » refusée", conf=conf, n=1, apres=True, plafond=50.0)

    def test_artefacts_plafond_de_la_course(self):
        for p in (None, 0, -1, True, 110.01):  # montant requis : 2 × 50 + 2 × 5 = 110 avec l'étage après la dernière
            with self.subTest(plafond=p):
                self.refuse("plafond de la course", apres=True, plafond=p)

    def test_artefacts_etage(self):
        sans_total = dict(self.et, reglages={k: v for k, v in self.et["reglages"].items() if k != "plafond_total_usd"})
        self.refuse("plafond_total_usd", etage=sans_total)
        self.refuse("plafond_total_usd", etage=dict(self.et, reglages=dict(self.et["reglages"], plafond_total_usd=6.0)))
        self.refuse("expérimentateur externe", etage=dict(self.et, reglages=dict(self.et["reglages"], experimentateur_externe=("x", "m", None))))
        self.refuse("expérimentateur externe", etage=dict(self.et, reglages=dict(self.et["reglages"], experimentateur_externe=("x", "m", None),
                                                                                 plafond_externe_usd=1.0)))
        self.refuse("correspondance manquant", etage={k: v for k, v in self.et.items() if k != "correspondance"})
        self.refuse("POLE_MACHINE_JETABLE_V56", MachineNonJetable, env={"PATH": "/usr/bin"})
        self.refuse("liste blanche", MachineNonJetable, env=dict(A.JETABLE, MON_JETON_API="x"))

    def test_artefact_sortie_presente(self):
        sortie = os.path.join(self.tmp, "c")
        os.makedirs(sortie)
        with self.assertRaises(EcrasementInterdit):
            c68.executer_course_v68(self.conf, sortie, self.ad, nombre_generations=1, go={}, lecture_selection=False,
                                    etage_apres_derniere=False, plafond_course_usd=50.0)
        self.assertEqual(os.listdir(sortie), [])


# --- de bout en bout : lecture de la sélection (allumé) ----------------------------------------------------------------------------


class TestCourseLectureSelectionV68(unittest.TestCase):
    """Deux générations, `lecture_selection=True`, `etage_apres_derniere=True` : étage v5 réel (exécuteur factice) après chaque
    génération ; la génération 2 lit la sélection scellée de la 1 ; la sélection de la 2 est scellée, jamais servie."""

    @classmethod
    def setUpClass(cls):
        cls.d = dossier_de_classe(cls)
        cls.bilan, cls.ad, cls.conf, cls.sortie = course(cls.d, "c", lecture=True, apres=True)

    def test_course_complete_sans_arret(self):
        self.assertIsInstance(self.bilan, list, repr(self.bilan))
        self.assertEqual([l["generation"] for l in self.bilan], [1, 2])
        b = lire(os.path.join(self.sortie, "bilan-course.json"))
        self.assertTrue(verifier_scelle(os.path.join(self.sortie, "bilan-course.json")))
        self.assertEqual((b["version"], b["arret"], b["noeud"], b["regime"]["nom"]), (c68.VERSION, None, None, "lecture_de_la_selection"))

    def test_selection_non_vide_retenues_et_exclues(self):
        sel = self.bilan[0]["etage"]["selection"]
        self.assertEqual(self.bilan[0]["etage"]["version_etage"], v5.VERSION_ETAGE_V5)
        self.assertGreaterEqual(len(sel["retenues"]), 1)
        self.assertGreaterEqual(len(sel["exclues"]), 1)
        self.assertTrue(all(x["verdict"] == "éliminée" for x in sel["exclues"]))

    def test_generation_2_lit_la_selection_heritage_lu_ecrit(self):
        l1, l2 = self.bilan
        self.assertIsNone(l1["heritage_lu"])
        h = l2["heritage_lu"]
        self.assertEqual(h["selection_sha256"], l1["selection"]["sha256"])
        self.assertEqual(h["selection_sha256"], sha256_fichier(os.path.join(self.sortie, "etage-apres-generation-1", NOM_SELECTION)))
        self.assertEqual((h["depuis_generation"], h["section"], h["exclues_a4"]), (1, "servie", []))
        self.assertEqual(h["retenues"], h["servies"])
        self.assertEqual(h["retenues"], len(l1["etage"]["selection"]["retenues"]))
        self.assertEqual(h["consignes_avec_section"], len(self.conf["cases"]) * len(self.conf["proposeurs"]))
        texte, sha, _, _ = A.section_attendue(os.path.join(self.sortie, "etage-apres-generation-1"), TITRE)
        self.assertEqual(h["texte_sha256"], sha)  # recalculé à part depuis les fichiers scellés de l'étage
        self.assertTrue(l1["selection"]["servie_a_la_suivante"])
        self.assertEqual(l1["heritage_servi_a_la_suivante"]["selection_sha256"], l1["selection"]["sha256"])

    def test_ce_qui_est_servi_aux_proposeurs(self):
        cs = A.consignes_passe1(self.ad)
        k = len(self.conf["cases"]) * len(self.conf["proposeurs"])
        self.assertEqual(len(cs), 2 * k)
        gen1, gen2 = cs[:k], cs[k:]
        garder, exclure = lignes_selection(self.sortie, 1)
        for c in gen1:
            self.assertNotIn(TITRE, c)
        for c in gen2:
            self.assertIn("\n## " + TITRE + "\n" + "\n".join(garder) + "\n", c)
            for x in exclure:
                self.assertNotIn(x, c)
        for c in cs:  # aucun verdict servi, aucun classement des juges
            for mot in ("survit", "éliminée", "verdict agrégé", "notable", "non concluant"):
                self.assertNotIn(mot, c)

    def test_etage_apres_la_derniere_jamais_servi(self):
        l2 = self.bilan[1]
        self.assertIn("etage", l2)
        self.assertFalse(l2["selection"]["servie_a_la_suivante"])
        self.assertIsNone(l2["heritage_servi_a_la_suivante"])
        self.assertTrue(verifier_scelle(os.path.join(self.sortie, "etage-apres-generation-2", NOM_SELECTION)))

    def test_budget_de_la_course_cumule(self):
        b = lire(os.path.join(self.sortie, "bilan-course.json"))["budget_course"]
        couts = [self.bilan[0]["cout_generation_usd"], self.bilan[0]["cout_etage_usd"], self.bilan[1]["cout_generation_usd"],
                 self.bilan[1]["cout_etage_usd"]]
        self.assertTrue(all(c > 0 for c in couts))
        self.assertAlmostEqual(b["cumul_usd"], sum(couts), places=5)
        self.assertEqual(b["plafond_course_usd"], 2 * S17 + 2 * PLAFOND_ETAGE)
        self.assertAlmostEqual(bc.rejouer_journal_course_v68(b), b["cumul_usd"], places=5)
        self.assertEqual([j["poste"] for j in b["journal"] if j["quoi"] == "compte"],
                         ["generation-1", "etage-apres-generation-1", "generation-2", "etage-apres-generation-2"])
        f2 = lire(os.path.join(self.sortie, "generation-2", "manifeste-fin.json"))["budget"]
        self.assertAlmostEqual(f2["cumul_usd"], self.bilan[1]["cout_generation_usd"], places=5)  # la génération : son seul coût
        self.assertLess(f2["cumul_usd"], b["cumul_usd"])  # la course : le cumul


# --- de bout en bout : tests de mort sans rien servir (allumé) et éteint --------------------------------------------------------


class TestCourseTestsDeMortSansRienServirV68(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.d = dossier_de_classe(cls)
        cls.bilan, cls.ad, cls.conf, cls.sortie = course(cls.d, "c", lecture=False, apres=True)
        cls.bilan1, cls.ad1, _, cls.sortie1 = course(cls.d, "c1", n=1, lecture=False, apres=True)

    def test_etage_apres_chaque_generation_rien_servi(self):
        self.assertIsInstance(self.bilan, list, repr(self.bilan))
        for g in (1, 2):
            l = self.bilan[g - 1]
            self.assertIsNone(l["heritage_lu"])
            self.assertIsNone(l["heritage_servi_a_la_suivante"])
            self.assertFalse(l["selection"]["servie_a_la_suivante"])
            self.assertTrue(verifier_scelle(os.path.join(self.sortie, f"etage-apres-generation-{g}", NOM_SELECTION)))
        self.assertGreaterEqual(self.bilan[0]["selection"]["retenues"], 1)  # une sélection non vide, jamais servie
        garder, _ = lignes_selection(self.sortie, 1)
        for c in A.consignes_passe1(self.ad):
            self.assertNotIn(TITRE, c)
            for x in garder:
                self.assertNotIn(x, c)
        b = lire(os.path.join(self.sortie, "bilan-course.json"))
        self.assertEqual(b["regime"]["nom"], "tests_de_mort_sans_rien_servir")
        self.assertEqual(b["regime"]["servi_aux_proposeurs"], "rien (aucun héritage)")

    def test_une_seule_generation_et_son_etage(self):
        self.assertIsInstance(self.bilan1, list, repr(self.bilan1))
        self.assertEqual(len(self.bilan1), 1)
        self.assertIn("etage", self.bilan1[0])
        self.assertTrue(os.path.isdir(os.path.join(self.sortie1, "etage-apres-generation-1")))
        self.assertFalse(os.path.exists(os.path.join(self.sortie1, "generation-2")))

    def test_memes_generations_que_la_lecture_en_generation_1(self):
        """La génération 1 ne dépend pas du régime : mêmes fiches, même classement qu'en régime de lecture (à l'octet)."""
        d = dossier_de_classe(type(self))
        _, _, _, s_lec = course(d, "lec", lecture=True, apres=False)
        for f in ("classement.json", "fiches.json", "memoire.json"):
            with self.subTest(f=f):
                self.assertEqual(sha256_fichier(os.path.join(self.sortie, "generation-1", f)), sha256_fichier(os.path.join(s_lec, "generation-1", f)))


class TestCourseEteinteV68(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.d = dossier_de_classe(cls)
        cls.bilan, cls.ad, cls.conf, cls.sortie = course(cls.d, "c", lecture=False, apres=False)

    def test_etage_entre_generations_selection_scellee_jamais_servie(self):
        self.assertIsInstance(self.bilan, list, repr(self.bilan))
        self.assertIn("etage", self.bilan[0])
        self.assertNotIn("etage", self.bilan[1])  # aucun étage après la dernière
        self.assertFalse(os.path.exists(os.path.join(self.sortie, "etage-apres-generation-2")))
        self.assertFalse(self.bilan[0]["selection"]["servie_a_la_suivante"])
        self.assertIsNone(self.bilan[1]["heritage_lu"])
        for c in A.consignes_passe1(self.ad):
            self.assertNotIn(TITRE, c)
            self.assertNotIn("verdict agrégé", c)
        self.assertEqual(lire(os.path.join(self.sortie, "bilan-course.json"))["regime"]["nom"], "eteint")

    def test_une_generation_sans_etage_egale_a_la_v56(self):
        """Éteint, une génération, sans étage, champs de fiche sans test (comme la configuration v5) : sorties de la génération
        égales à l'octet à celles de la course v56, avec le moteur simulé v56 puis avec le moteur simulé v68 (inerte ici)."""
        d = dossier_de_classe(type(self))
        conf = cfg.lire_configuration_v56(A.configuration(d, avec_test=False, etage=False), base=d)
        v56_simule = s68.AdaptateurSimuleV68.__mro__[1]
        r56 = c56.executer_course_v56(conf, os.path.join(d, "v56"), A.adaptateurs(conf, classe=v56_simule), nombre_generations=1,
                                      go={"essai": True}, racine_sessions=os.path.join(d, "sessions-v56"))
        for nom, classe in (("v68-sim56", v56_simule), ("v68-sim68", s68.AdaptateurSimuleV68)):
            r68, _, _, sortie68 = course(d, nom, n=1, lecture=False, apres=False, etage=False, conf=conf, classe=classe)
            self.assertIsInstance(r68, list, repr(r68))
            self.assertEqual(len(r56), len(r68))
            for f in ("classement.json", "fiches.json", "memoire.json", "fusions-inachevees.json"):
                with self.subTest(moteur=nom, f=f):
                    self.assertEqual(sha256_fichier(os.path.join(sortie68, "generation-1", f)),
                                     sha256_fichier(os.path.join(d, "v56", "generation-1", f)))


# --- le défaut de la v59 rejoué de bout en bout, puis réparé ----------------------------------------------------------------------


class TestDefautV59DeBoutEnBout(CasAvecDossier):
    def test_v59_casse_a_la_generation_2_la_v68_la_joue(self):
        conf = conf_lue(self.tmp)
        ad = A.adaptateurs(conf)
        with self.assertRaises(json.JSONDecodeError):
            c59.executer_course_v59(conf, os.path.join(self.tmp, "v59"), ad, nombre_generations=2, go={"essai": True},
                                    etage=A.etage(conf, ad), environnement=A.JETABLE, racine_sessions=os.path.join(self.tmp, "s59"))
        b = lire(os.path.join(self.tmp, "v59", "bilan-course.json"))
        self.assertIn("JSONDecodeError", b["arret"])
        self.assertGreaterEqual(len(b["generations"][0]["etage"]["selection"]["retenues"]), 1)  # sélection non vide
        r, _, _, _ = course(self.tmp, "v68", lecture=True, apres=False, conf=conf)
        self.assertIsInstance(r, list, repr(r))
        self.assertEqual(r[1]["heritage_lu"]["section"], "servie")


# --- budget de la course : arrêt au plafond, artefacts --------------------------------------------------------------------------


def double_etage(couts):
    """Un double de l'étage : chaque candidate « testée », verdict du noyau « survit » ; `couts` : le champ rendu (ou absent)."""
    def executer(adaptateur, sortie, resume_sortie, **reglages):
        lignes = lire(os.path.join(sortie, "classement.json"))["lignes"]
        par = [{"identifiant_auteur": l["identifiant_auteur"], "statut": "testée", "verdict": "survit",
                "verdict_noyau": {"etiquette": ETIQUETTE_NOYAU, "verdict": "survit", "motif": "double"}}
               for l in lignes if l["eligible"]][:reglages.get("nombre", 3)]
        resume_sortie.update(par_fiche=par, termine=True, version_etage="double")
        if couts is not None:
            resume_sortie["couts"] = couts
    return executer


class TestBudgetCourseDansLaCourse(CasAvecDossier):
    def test_arret_au_plafond_de_la_course(self):
        """Plafond de la course sous le montant requis (S17 + 0,5 USD) : génération 1 (réserve S17) et étage (réserve 5 USD sur
        le reste) joués ; la génération 2 réserve S17 entier sur un cumul réel de 0,9 USD : ne tient pas, arrêt avant elle
        (rien de lancé, rien d'écrit pour elle)."""
        r, _, _, sortie = course(self.tmp, "c", lecture=False, apres=True, plafond=S17 + 0.5)
        self.assertIsInstance(r, bc.PlafondDeCourseAtteint)
        self.assertFalse(os.path.exists(os.path.join(sortie, "generation-2")))
        b = lire(os.path.join(sortie, "bilan-course.json"))
        self.assertIn("PlafondDeCourseAtteint", b["arret"])
        self.assertEqual(b["budget_course"]["journal"][-1], dict(b["budget_course"]["journal"][-1], quoi="refuse", poste="generation-2"))
        self.assertLessEqual(b["budget_course"]["cumul_usd"], b["budget_course"]["plafond_course_usd"])
        self.assertEqual([l["generation"] for l in b["generations"]], [1])
        self.assertIn("etage", b["generations"][0])

    def test_artefact_generation_au_dela_de_son_plafond(self):
        class Fuyante(c68.GenerationV68):
            def executer(self):
                r = super().executer()
                self.budget.cumul += 1000.0  # un relais qui n'aurait pas tenu son plafond dur
                return r
        with mock.patch.object(c68, "GenerationV68", Fuyante):
            r, _, _, sortie = course(self.tmp, "c", n=2, lecture=False, apres=False, etage=False)
        self.assertIsInstance(r, bc.CumulCourseAuDela)
        b = lire(os.path.join(sortie, "bilan-course.json"))
        self.assertIn("CumulCourseAuDela", b["arret"])
        self.assertFalse(os.path.exists(os.path.join(sortie, "generation-2")))

    def test_artefact_etage_au_dela_de_son_plafond_et_cout_inconnu(self):
        conf = conf_lue(self.tmp)
        ad = A.adaptateurs(conf)
        trop = A.etage(conf, ad, executer=double_etage({"claude_usd": 4.0, "externe_usd": 2.0}))
        with self.assertRaises(bc.CumulCourseAuDela):
            c68.executer_course_v68(conf, os.path.join(self.tmp, "c"), ad, nombre_generations=2, go={}, lecture_selection=False,
                                    etage_apres_derniere=False, plafond_course_usd=105.0, etage=trop, environnement=A.JETABLE,
                                    racine_sessions=os.path.join(self.tmp, "s"))
        self.assertFalse(os.path.exists(os.path.join(self.tmp, "c", "generation-2")))
        inconnu = A.etage(conf, ad, executer=double_etage(None))
        bilan = c68.executer_course_v68(conf, os.path.join(self.tmp, "c2"), ad, nombre_generations=2, go={}, lecture_selection=True,
                                        etage_apres_derniere=False, plafond_course_usd=105.0, etage=inconnu,
                                        environnement=A.JETABLE, racine_sessions=os.path.join(self.tmp, "s2"))
        b = lire(os.path.join(self.tmp, "c2", "bilan-course.json"))["budget_course"]
        j = [x for x in b["journal"] if x["poste"] == "etage-apres-generation-1" and x["quoi"] == "compte"][0]
        self.assertEqual((j["cout_inconnu"], j["cout_usd"]), (True, PLAFOND_ETAGE))  # compté à sa réservation entière
        self.assertIsNone(bilan[0]["cout_etage_usd"])
        self.assertEqual(bilan[1]["heritage_lu"]["section"], "servie")


class TestMutationsV68(CasAvecDossier):
    """Les essais ont des dents (R5) : garde retirée → l'artefact passe."""

    def test_mutation_reservation_retiree_la_generation_2_part(self):
        def reserver_sans_garde(self, poste, montant_usd):
            self.en_cours = (poste, float(montant_usd))
            self.postes.add(poste)
            return float(montant_usd)
        with mock.patch.object(bc.GardeBudgetCourseV68, "reserver", reserver_sans_garde):
            r, _, _, sortie = course(self.tmp, "c", lecture=False, apres=True, plafond=S17 + 0.5)
        self.assertIsInstance(r, list)  # la course entière passe : l'arrêt au plafond tient à la réservation
        self.assertTrue(os.path.isdir(os.path.join(sortie, "generation-2")))

    def test_mutation_a4_retiree_la_ligne_interdite_passe(self):
        with mock.patch.object(fv, "trouver", lambda *a, **k: []):
            corps, _ = c68.rendre_heritage_v68(H, INTERDITES, MODE, "arret", selection_vide="omettre", titre=TITRE)
        self.assertIn("témoin", corps)

    def test_mutation_cout_non_compte_le_depassement_passe(self):
        def compter_sans_garde(self, poste, cout_usd, inconnu=False):
            self.en_cours = None
            return 0.0
        conf = conf_lue(self.tmp)
        ad = A.adaptateurs(conf)
        trop = A.etage(conf, ad, executer=double_etage({"claude_usd": 4.0, "externe_usd": 2.0}))
        with mock.patch.object(bc.GardeBudgetCourseV68, "compter", compter_sans_garde):
            bilan = c68.executer_course_v68(conf, os.path.join(self.tmp, "c"), ad, nombre_generations=2, go={},
                                            lecture_selection=False, etage_apres_derniere=False, plafond_course_usd=105.0,
                                            etage=trop, environnement=A.JETABLE, racine_sessions=os.path.join(self.tmp, "s"))
        self.assertEqual(len(bilan), 2)  # l'étage à 6 USD sous une réservation de 5 passe sans la garde du compte


# --- le lanceur v68 -------------------------------------------------------------------------------------------------------------


def lanceur():
    spec = importlib.util.spec_from_file_location("ideation_v68_essai", os.path.join(RACINE, "demonstrations", "ideation_v68.py"))
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


class TestLanceurV68(CasAvecDossier):
    def lancer(self, argv, env=None):
        m = lanceur()
        err, out = io.StringIO(), io.StringIO()
        with contextlib.redirect_stderr(err), contextlib.redirect_stdout(out):
            code = m.principal(argv, environnement=env if env is not None else dict(A.JETABLE, TMPDIR=self.tmp))
        return code, out.getvalue(), err.getvalue()

    def conf(self, nom="c.json", **modifs):
        return A.ecrire_configuration(A.configuration(self.tmp, **modifs), os.path.join(self.tmp, nom))

    def test_cablage(self):
        m = lanceur()
        self.assertIs(m.c68.executer_course_v68, c68.executer_course_v68)
        self.assertEqual(m.INTERRUPTEURS, ("lecture_selection_generation_suivante", "tests_de_mort_reels"))
        self.assertEqual(m.ADDITIF_INTERRUPTEURS_V68, (None, None))
        a = m.construire_analyseur().parse_args(["--course-2", "c", "s", "--generations", "2"])
        self.assertEqual((a.lecture_selection, a.etage_apres_derniere, a.selection_vide, a.plafond_course_usd),
                         ("non", False, "omettre", None))  # éteints par défaut ; sélection vide omise

    def test_verifier_seulement_montants_par_regime(self):
        ch = self.conf()
        for opts, montant, regime in (([], 105.0, "eteint"), (["--etage-apres-derniere"], 110.0, "tests_de_mort_sans_rien_servir"),
                                      (["--lecture-selection", "oui"], 105.0, "lecture_de_la_selection")):
            with self.subTest(opts=opts):
                code, out, err = self.lancer(["--course-2", ch, os.path.join(self.tmp, "x"), "--generations", "2",
                                              "--verifier-seulement"] + opts)
                self.assertEqual(code, 0, err)
                o = json.loads(out)
                self.assertEqual((o["montant_requis_go_usd"], o["regime"]["nom"], o["ecriture"]), (montant, regime, "aucune"))
                self.assertEqual(o["interrupteurs"], ["lecture_selection_generation_suivante", "tests_de_mort_reels"]
                                 if regime == "lecture_de_la_selection" else ["tests_de_mort_reels"])
        self.assertFalse(os.path.exists(os.path.join(self.tmp, "x")))

    def test_artefacts_refus_avant_ecriture(self):
        ch = self.conf()
        sortie = os.path.join(self.tmp, "x")
        for opts in (["--generations", "1", "--lecture-selection", "oui"], ["--generations", "2", "--plafond-course-usd", "200"],
                     ["--generations", "2", "--plafond-course-usd", "0"], ["--generations", "2"]):
            with self.subTest(opts=opts):
                code, _, err = self.lancer(["--course-2", ch, sortie] + opts)
                self.assertEqual(code, 2)
                self.assertIn("arret", err)
        code, _, err = self.lancer(["--course-2", ch, sortie, "--generations", "2", "--moteur", "simule"], env={"PATH": "/usr/bin"})
        self.assertEqual(code, 2)
        self.assertIn("MachineNonJetable", err)
        ch2 = self.conf("sans-etage.json", etage_tests_de_mort=A56.SUPPRIMER)
        code, _, err = self.lancer(["--course-2", ch2, sortie, "--generations", "2", "--etage-apres-derniere", "--verifier-seulement"])
        self.assertEqual(code, 2)
        self.assertIn("sans étage", err)
        with contextlib.redirect_stderr(io.StringIO()), self.assertRaises(SystemExit):
            lanceur().principal(["--course-2", ch, sortie, "--generations", "2", "--selection-vide", "rien"])
        self.assertFalse(os.path.exists(sortie))

    def test_moteur_reel_refuse_par_construction(self):
        ch = self.conf(etage_tests_de_mort__environnement_permis=["GO_ID"])
        sortie = os.path.join(self.tmp, "x")
        base = ["--course-2", ch, sortie, "--generations", "2", "--moteur", "reel", "--confirmer-moteur-reel"]
        code, _, err = self.lancer(base + ["--lecture-selection", "oui"])
        self.assertEqual(code, 2)
        self.assertIn("--registre-go exigé", err)
        for perimetre, attendu in (("essai auto-conception tests_de_mort_reels", "lecture_selection_generation_suivante"),
                                   ("lecture_selection_generation_suivante et tests_de_mort_reels", "refusé par construction")):
            with self.subTest(perimetre=perimetre):
                reg = A56.registre_go(self.tmp, A56.ligne_go("GO-2026-11-19-01", "105 USD", perimetre=perimetre), nom="go-essai.md")
                code, _, err = self.lancer(base + ["--lecture-selection", "oui", "--registre-go", reg],
                                           env=dict(A.JETABLE, TMPDIR=self.tmp, GO_ID="GO-2026-11-19-01"))
                self.assertEqual(code, 2)
                self.assertIn(attendu, err)
        reg = A56.registre_go(self.tmp, A56.ligne_go("GO-2026-11-19-01", "105 USD", perimetre="lecture_selection_generation_suivante "
                                                     "tests_de_mort_reels"), nom="go-essai.md")
        code, _, err = self.lancer(base + ["--lecture-selection", "oui", "--registre-go", reg],
                                   env=dict(A.JETABLE, TMPDIR=self.tmp, GO_ID="GO-2026-11-19-01"))
        self.assertIn("additif des interrupteurs non épinglé", err)
        ch2 = self.conf("sans-etage.json", etage_tests_de_mort=A56.SUPPRIMER)
        code, _, err = self.lancer(["--course-2", ch2, sortie, "--generations", "1", "--moteur", "reel", "--confirmer-moteur-reel"])
        self.assertEqual(code, 2)
        self.assertIn("refusé par construction", err)  # éteint aussi : aucun moteur réel en v68
        self.assertFalse(os.path.exists(sortie))

    def test_de_bout_en_bout_par_le_lanceur_lecture_puis_eteint(self):
        ch = self.conf()
        code, out, err = self.lancer(["--course-2", ch, os.path.join(self.tmp, "lec"), "--generations", "2", "--lecture-selection",
                                      "oui", "--moteur", "simule"])
        self.assertEqual(code, 0, err)
        o = json.loads(out)
        self.assertEqual(o["regime"], "lecture_de_la_selection")
        self.assertEqual(o["bilan"][1]["heritage_lu"]["section"], "servie")
        self.assertGreaterEqual(o["bilan"][1]["heritage_lu"]["servies"], 1)
        code, out, err = self.lancer(["--course-2", ch, os.path.join(self.tmp, "et"), "--generations", "2", "--moteur", "simule"])
        self.assertEqual(code, 0, err)
        o = json.loads(out)
        self.assertEqual((o["regime"], o["bilan"][1]["heritage_lu"]), ("eteint", None))
        self.assertFalse([n for n in os.listdir(self.tmp) if n.startswith("pole-sessions-v56-")])

    def test_sans_course_2_la_main_au_lanceur_v8(self):
        m = lanceur()
        with mock.patch.object(m.v8, "principal", return_value=7) as p:
            self.assertEqual(m.principal(["--pre-pilote", "c", "s"]), 7)
        p.assert_called_once()


# --- moteur simulé v68 : inerte sans champ test_de_mort ---------------------------------------------------------------------------


class TestSimulationV68(unittest.TestCase):
    def test_roles_de_l_etage_sont_ceux_de_la_v5(self):
        self.assertEqual((s68.ROLE_EXPERIMENTATEUR, s68.ROLE_LECTEUR), (v5.ROLE_EXPERIMENTATEUR, v5.ROLE_LECTEUR))

    def test_inerte_sans_champ_test_de_mort(self):
        champs = list(A56.CHAMPS)
        a = s68.AdaptateurSimuleV68(champs_fiche=champs, items=A56.ITEMS, cout_par_appel_usd=0.01, champ_titre="titre")
        b = s68.AdaptateurSimuleV68.__mro__[1](champs_fiche=champs, items=A56.ITEMS, cout_par_appel_usd=0.01, champ_titre="titre")
        for consigne in ("## Case\nTexte : t ; bras : b\n", "JUGE\n## La fiche\n```json\n{}\n```", "AIGUILLEUR"):
            self.assertEqual(a.reponse("x", consigne, "m"), b.reponse("x", consigne, "m"))
        self.assertEqual(a.fiche(12), b.fiche(12))

    def test_fiche_avec_test_projetable(self):
        a = s68.AdaptateurSimuleV68(champs_fiche=A.CHAMPS_V68, items=A56.ITEMS, cout_par_appel_usd=0.01, champ_titre="titre")
        f = a.fiche(5)
        v5.valider_champ_test(f["test_de_mort"])
        self.assertEqual(f["test_de_mort"]["statistique"], s68.BLOC_SIMULE)


# --- R12 : les fichiers existants sont ceux du commit a41b7b50 ------------------------------------------------------------------

EMPREINTES_A41B7B50 = {
    "pole/course2_v54.py": "ac1980d04eb88d8fbb9a073902e47146ab9eadd3375a41cd72835fa5acf20342",
    "pole/course2_v56.py": "14f655696876afc8453ec5237236b3f9daf8d87844c4acc9d5189b3e61b310f1",
    "pole/course2_v57.py": "2efc4e0ece6b5cea8354503ae476195cffb448f85bdf5db5b99b6295a22ff17d",
    "pole/course2_v59.py": "b5a19a479bba806acb71f6ba49e238b79c717c5423d8ea17a5921c57eae82262",
    "pole/noyau_v56.py": "eb5a003e8f23b0882e5588fe537e8b65b890f0d7d19560896be4e85a0731543b",
    "pole/budget_v56.py": "3a672aceeeee3cf83cd4e46ca461fdbaf3acd0a9552be24d2566627ce6b7c13e",
    "pole/configuration_v54.py": "3424ca7fa8911e5c2656cb56632f7d74c958008b9366af0ac45e6a62e4d16d66",
    "pole/etage_entre_generations_v53.py": "d568d25bf7d96011cfdcda12e7bc2c1933a61827b237f8c8c363b4055122ad4b",
    "pole/etage_entre_generations_v56.py": "f0c80e2d9801d4a928574f7f442e2950c2d130d77015b30102911bfa87dd6eba",
    "pole/etage_entre_generations_v57.py": "e4bf36819d18844079a2bb4996991fd65c233a51d76b7d3daf5b866a71328318",
    "pole/boucle_fermee_v59.py": "a2de486592fc98c14e13bb9071d272fb65d4f49de38dd188ee64857698177681",
    "pole/simulation_v56.py": "bcafca44c5117dfd30262ee520a67944d051208f1b1deac6fac016e8cb95dc76",
    "pole/tests_de_mort_v5.py": "da524871b9b498693d67cc099240acb98c4c84c800ee4c69f0a1cb5fe60b64f1",
    "pole/fiches_v54.py": "1ab0796dd5d9de14ea84953b0307a065572bc300ebe45209ca207d7880bbaebf",
    "demonstrations/ideation_v8.py": "2e2be8d72c548e183b94c14de20c971f241f998f54f64c5281b2427fdd64e9d1",
    "demonstrations/ideation_v59.py": "5419137ca0bb910b0c057a7ab1a19cd409d7c5c643bf485b6f3f9c0588523eef",
    "demonstrations/ideation_v5.py": "1894f250264eaaccbf891dfa255e71dc587fe415c8d21e283391203a2fe73444",
    "essais/aides_v56.py": "d0fc2ca3d249653d28308bfbe6d0c57c9b0c19caddb0c7f483105707e9a2b3bc",
}


class TestR12V68(unittest.TestCase):
    def test_fichiers_existants_inchanges(self):
        for rel, sha in sorted(EMPREINTES_A41B7B50.items()):
            with self.subTest(rel=rel):
                self.assertEqual(sha256_fichier(os.path.join(RACINE, rel)), sha)


if __name__ == "__main__":
    unittest.main()
