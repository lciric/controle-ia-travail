"""Essais du lot 6 v2 du véhicule NA-1 (2/3 ; portés du v1, montage câblé en état 1 avec le journal de la colonne) : arrêts n° 5, 6, 7, 8, 10, 14, 19 en course ; A17 ; garde de remplacement ;
ce que rend un refus écrit, par rôle (E4 compris) ; A2 ; identifiants dans les requêtes des juges. Chaque garde a son cas
sain et son artefact (règle R5). Données factices seules ; aucune clé ; aucun appel."""

import copy
import json
import os
import sys
import unittest

ICI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ICI)

import aides_na_lot6_v2 as A6  # noqa: E402
import aides_na_v4 as A  # noqa: E402
from aides_na_lot6_v2 import CE  # noqa: E402
from pole import appel_garde_na_v1 as ag  # noqa: E402
from pole import configuration_course_na_v1 as cfn  # noqa: E402
from pole import course_na_v2 as cn  # noqa: E402
from pole import garde_motifs_na_v4 as gm  # noqa: E402
from pole import identifiants_na_v1 as ident  # noqa: E402
from pole import journal_na_v3 as jn  # noqa: E402
from pole import portier_na_v1 as pt  # noqa: E402
from pole import registre_na_v1 as rg  # noqa: E402
from pole import requete_na_v3 as rq  # noqa: E402
from pole import simulation_na_v1 as sim  # noqa: E402
from pole import tirage_na_v4 as tn  # noqa: E402
from pole import verifier_registre_servi_na_v1 as vr  # noqa: E402
from pole.adaptateurs import Resultat  # noqa: E402
from pole.budget_course_v68 import CumulCourseAuDela, GardeBudgetCourseV68, PlafondDeCourseAtteint  # noqa: E402

VIDE = {"texte_final": "Aucune fiche : " + sim.MARQUE_VIDE_MOTIVEE + "."}


def capturer(liste):
    def f(g, gen):
        liste.append(gen)
    return f


def plan_par_rang(plan):
    """Un `decider` à compteur commun à tous les adaptateurs : `plan(k)` donne le comportement du k-ième appel de
    proposeur de la course (0 à 164 ; génération = k // 55 + 1)."""
    k = [0]

    def decider(identifiant, adaptateur, n):
        c = plan(k[0])
        k[0] += 1
        return c
    return decider


# --- n° 5, garde du coffre ------------------------------------------------------------------------------------------

class TestArret5(unittest.TestCase):
    def test_un_quart_exactement_la_suivante_part(self):
        m = A6.Montage(decider=plan_par_rang(lambda k: "champ_en_plus" if k == 0 else
                                             "fiches_json" if k < 4 else "vide_motivee"))
        bilan = m.lancer()
        self.assertEqual(len(bilan), 3)
        self.assertEqual((bilan[0]["coffre"]["au_coffre"], bilan[0]["coffre"]["rendues"]), (1, 4))
        self.assertFalse(bilan[0]["coffre"]["depasse"])

    def test_une_fiche_de_plus_au_coffre_la_suivante_ne_part_pas(self):
        m = A6.Montage(decider=plan_par_rang(lambda k: "champ_en_plus" if k < 2 else
                                             "fiches_json" if k < 5 else "vide_motivee"))
        with self.assertRaises(rg.ArretGardeCoffre):
            m.lancer()
        a = m.arrets()
        self.assertEqual((a[0]["numero"], a[0]["generation"]), (5, 1))
        self.assertNotIn("generation-2", {j["poste"] for j in m.bilan()["budget_course"]["journal"]})

    def test_a_la_troisieme_generation_consigne(self):
        m = A6.Montage(decider=plan_par_rang(lambda k: "champ_en_plus" if 110 <= k < 112 else
                                             "fiches_json" if 112 <= k < 113 else "vide_motivee"))
        bilan = m.lancer()
        self.assertEqual(len(bilan), 3)
        self.assertTrue(bilan[2]["coffre"]["depasse"])
        self.assertTrue(bilan[2]["coffre"]["consigne"])


# --- n° 6, plafonds ---------------------------------------------------------------------------------------------------

class TestArret6(unittest.TestCase):
    def test_reservation_egale_au_reste_permise(self):
        b = GardeBudgetCourseV68(450.0)
        for g in (1, 2):
            b.reserver(f"generation-{g}", 150.0)
            b.compter(f"generation-{g}", 150.0)
        self.assertEqual(b.reserver("generation-3", 150.0), 150.0)

    def test_reservation_d_un_centime_de_trop_refusee(self):
        b = GardeBudgetCourseV68(449.99)
        for g in (1, 2):
            b.reserver(f"generation-{g}", 150.0)
            b.compter(f"generation-{g}", 150.0)
        with self.assertRaises(PlafondDeCourseAtteint):
            b.reserver("generation-3", 150.0)
        self.assertEqual(b.journal[-1]["quoi"], "refuse")

    def test_en_course_un_poste_plus_cher_que_sa_reservation(self):
        def gonfler(g, gen):
            orig = gen.executer

            def executer():
                r = orig()
                gen.budget.cumul = 150.01
                return r
            gen.executer = executer
        m = A6.Montage()
        with self.assertRaises(CumulCourseAuDela):
            m.lancer(crochets={"avant_execution": gonfler})
        self.assertEqual(m.arrets()[0]["numero"], 6)

    def test_en_course_chaque_generation_reserve_s17_avant_ses_appels(self):
        m = A6.Montage()
        m.lancer()
        j = [x for x in m.bilan()["budget_course"]["journal"] if x["quoi"] == "reserve"]
        self.assertEqual([(x["poste"], x["reservation_usd"]) for x in j],
                         [("generation-1", 150.0), ("generation-2", 150.0), ("generation-3", 150.0)])


# --- n° 7, seuils d'une génération ------------------------------------------------------------------------------------

class TestArret7(unittest.TestCase):
    def _course(self, cout_premier):
        gens = []
        m = A6.Montage(decider=A6.toujours("vide_motivee"), cout=0.0,
                       reglages={"ad_a": [dict(VIDE, cout_declare_usd=cout_premier)]})
        return m, gens

    def test_cumul_a_135_aiguillage_lance(self):
        m, gens = self._course(135.0)
        with self.assertRaises(cn.ArretSeuilsGenerationNA) as cm:
            m.lancer(crochets={"avant_execution": capturer(gens)})
        self.assertEqual(gens[0].etapes_etat["aiguillage"], "jouee")
        self.assertEqual(cm.exception.etape, "juges")

    def test_cumul_d_un_centime_au_dessus_de_135_aiguillage_non_lance(self):
        m, gens = self._course(135.01)
        with self.assertRaises(cn.ArretSeuilsGenerationNA) as cm:
            m.lancer(crochets={"avant_execution": capturer(gens)})
        self.assertEqual(cm.exception.etape, "aiguillage")
        a = m.arrets()[0]
        self.assertEqual((a["numero"], a["etape"], a["generation"]), (7, "aiguillage", 1))

    def test_cumul_a_120_juges_lances(self):
        m, gens = self._course(120.0)
        bilan = m.lancer(crochets={"avant_execution": capturer(gens)})
        self.assertEqual(len(bilan), 3)
        self.assertEqual(gens[0].etapes_etat["juges"], "jouee")

    def test_cumul_d_un_centime_au_dessus_de_120_juges_non_lances(self):
        m, gens = self._course(120.01)
        with self.assertRaises(cn.ArretSeuilsGenerationNA) as cm:
            m.lancer(crochets={"avant_execution": capturer(gens)})
        self.assertEqual(cm.exception.etape, "juges")


# --- n° 8, consigne plus longue que sa borne ----------------------------------------------------------------------------

class TestArret8(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        a = A6.Montage()
        a.lancer()
        tailles = {g: [l["taille"] for l in jn.verifier_journal(a.chemin_sortie("journaux", f"journal-requetes-g{g}.jsonl"))
                       if l["evenement"] == "envoi" and l["sorte"] == "proposeur"] for g in (1, 2, 3)}
        cls.max_g1 = max(tailles[1])
        cls.max_tout = max(max(t) for t in tailles.values())

    def _borne(self, n):
        return lambda o: o["bornes"].update(requete_proposeur_octets=n)

    def test_requete_egale_a_sa_borne_depart(self):
        m = A6.Montage(modifier=self._borne(self.max_tout))
        self.assertEqual(len(m.lancer()), 3)

    def test_un_octet_de_plus_depart_refuse(self):
        m = A6.Montage(modifier=self._borne(self.max_g1 - 1))
        with self.assertRaises(rq.ArretConsigneTropLongue):
            m.lancer()
        self.assertEqual(m.recus(), [])
        self.assertEqual(m.bilan()["budget_course"]["journal"], [])
        self.assertEqual(m.arrets()[0]["numero"], 8)


# --- n° 9 et n° 19 en course : le registre servi vérifié avant tout envoi ----------------------------------------------

class TestRegistreServiNonConforme(unittest.TestCase):
    def test_une_marque_de_code_dans_un_enonce_la_generation_2_ne_part_pas(self):
        m = A6.Montage(decider=A6.toujours("idee_marque_code"))
        with self.assertRaises(vr.RegistreServiNonConforme) as cm:
            m.lancer()
        self.assertIn(19, cm.exception.numeros)
        a = m.arrets()[0]
        self.assertEqual((a["generation"], a["type"]), (2, "RegistreServiNonConforme"))
        self.assertNotIn("generation-2", {j["poste"] for j in m.bilan()["budget_course"]["journal"]})


# --- n° 10, disjonction --------------------------------------------------------------------------------------------------

def tirage_avec_case_de_la_famille():
    s = copy.deepcopy(A.sortie_factice())
    f = s["famille_tenue_a_l_ecart"]["rang_axe_0"]
    triplet = next(tuple(e["triplet"]) for e in s["identifiants"] if e["triplet"][0] == f)
    mot = next(e["identifiant"] for e in s["identifiants"] if tuple(e["triplet"]) == triplet)
    s["generations"]["1"][0] = {"triplet": list(triplet), "identifiant": mot,
                                "ligne": tn.ligne_de_case(mot, triplet, s["legende"])}
    return s


def tirage_avec_case_deja_servie():
    s = copy.deepcopy(A.sortie_factice())
    s["generations"]["2"][0] = copy.deepcopy(s["generations"]["1"][0])
    return s


class TestArret10(unittest.TestCase):
    def test_case_de_la_famille_tenue_a_l_ecart_depart_refuse(self):
        m = A6.Montage(tirage=tirage_avec_case_de_la_famille())
        with self.assertRaises(tn.ArretDisjonction) as cm:
            m.lancer()
        self.assertIn("famille", cm.exception.cause)
        self.assertEqual(m.arrets()[0]["numero"], 10)
        self.assertEqual(m.recus(), [])

    def test_case_deja_servie_depart_refuse(self):
        m = A6.Montage(tirage=tirage_avec_case_deja_servie())
        with self.assertRaises((tn.LigneDeCaseRefusee, tn.ArretDisjonction)):
            m.lancer()
        self.assertEqual(m.recus(), [])

    def test_garde_rejouee_contre_la_copie(self):
        """Une case d'une autre génération plantée dans la copie : l'empreinte de la copie refuse (n° 14) ; plantée
        dans une copie réempreintée : la disjonction refuse (n° 10)."""
        def planter(g, c):
            if g != 2:
                return c
            c = copy.deepcopy(c)
            c["cases"][0] = list(premiere[0])
            return c
        a = A6.Montage()
        premiere = [None]
        copie1, _ = cfn.deriver_copie_generation(a.config, rq.cases_du_tirage(cfn.lire_tirage(a.config),
                                                                               cfn.charger_pieces_servies(a.config)[0])["1"])
        premiere[0] = copie1["cases"][0]
        with self.assertRaises(cfn.ArretEmpreinteNA):
            a.lancer(crochets={"copie": planter})
        tirage = cfn.lire_tirage(a.config)
        planter_copie = copy.deepcopy(copie1)
        triplets = cfn.triplets_de_la_copie(planter_copie, tirage, 2)
        with self.assertRaises(tn.ArretDisjonction):
            tn.garde_disjonction(tirage, 2, triplets)


# --- n° 14, empreintes --------------------------------------------------------------------------------------------------

class TestArret14(unittest.TestCase):
    def _alterer(self, chemin):
        with open(chemin, "ab") as f:
            f.write(b" ")

    def test_piece_alteree_au_depart(self):
        for nom in ("gabarit", "liste_motifs", "consigne_portier", "consigne_juges", "tirage", "table_roles_cles"):
            m = A6.Montage()
            self._alterer(m.piece_fichier(nom))
            with self.assertRaises(cfn.ArretEmpreinteNA) as cm:
                m.lancer()
            self.assertEqual(cm.exception.piece, nom)
            self.assertFalse(os.path.exists(m.sortie))

    def test_additif_epingle_altere(self):
        m = A6.Montage()
        self._alterer(m.config.pieces_epinglees[0].chemin)
        with self.assertRaises(cfn.ArretEmpreinteNA) as cm:
            m.lancer()
        self.assertEqual(cm.exception.piece, "additif du véhicule")

    def test_rejoue_au_depart_de_la_generation_2(self):
        m = A6.Montage()
        with self.assertRaises(cfn.ArretEmpreinteNA) as cm:
            m.lancer(crochets={"entre_generations": lambda g: self._alterer(m.piece_fichier("gabarit")) if g == 1 else None})
        self.assertEqual(cm.exception.moment, "départ de la génération 2")
        a = m.arrets()[0]
        self.assertEqual((a["numero"], a["piece"], a["generation"]), (14, "gabarit", 2))
        self.assertEqual(len(m.lignes_generation()), 1)

    def test_configuration_de_la_course_alteree_entre_deux_generations(self):
        m = A6.Montage()
        with self.assertRaises(cfn.ArretEmpreinteNA) as cm:
            m.lancer(crochets={"entre_generations": lambda g: self._alterer(m.chemin) if g == 1 else None})
        self.assertEqual(cm.exception.piece, "configuration de la course")

    def test_copie_de_la_generation_changee(self):
        def changer(g, c):
            if g != 2:
                return c
            c = copy.deepcopy(c)
            c["plafonds_session"]["juge"] = 0.61
            return c
        m = A6.Montage()
        with self.assertRaises(cfn.ArretEmpreinteNA) as cm:
            m.lancer(crochets={"copie": changer})
        self.assertEqual(cm.exception.piece, "configuration de la génération 2")

    def test_configuration_lue_a_son_empreinte(self):
        m = A6.Montage()
        with self.assertRaises(cfn.ArretEmpreinteNA):
            cfn.lire_configuration_course(m.chemin, "0" * 64)


# --- A17, passeport du portier neuf ---------------------------------------------------------------------------------------

class TestA17(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.m = A6.Montage(decider=plan_par_rang(lambda k: "fiches_json" if k % 5 else "champ_en_plus"))
        cls.gens = []
        cls.m.lancer(crochets={"avant_execution": capturer(cls.gens)})

    def test_fiche_passee_munie_du_passeport_jugee(self):
        self.assertGreater(self.gens[0].comptes_lot6["fiches_jugees"], 0)

    def test_fiche_non_passee_presentee_a_un_juge(self):
        gen = self.gens[0]
        non = next(f for _, r in gen.issues_reponses_na for f in r.fiches if f.classe != pt.PASSEE)
        with self.assertRaises(pt.ArretSansPasseportNA):
            gen.juger(non, "essai", {"cout": 0.0, "reste": 1.0, "coupee": False, "etape": "juges"})

    def test_fiche_du_noyau_munie_d_un_passeport_de_l_aiguilleur_du_noyau(self):
        gen = self.gens[0]
        f = gen.fiches[gen.passees_na[0].identifiant]
        with self.assertRaises(pt.ArretSansPasseportNA):
            gen.juger(f, "essai", {"cout": 0.0, "reste": 1.0, "coupee": False, "etape": "juges"})

    def test_fiche_passee_d_un_autre_portier(self):
        with self.assertRaises(pt.ArretSansPasseportNA):
            self.gens[1].juger(self.gens[0].passees_na[0], "essai", {"cout": 0.0, "reste": 1.0, "coupee": False,
                                                                     "etape": "juges"})

    def test_en_course_arret_nomme(self):
        def glisser(g, gen):
            orig = gen.etape_aiguillage

            def etape(etat):
                orig(etat)
                gen.passees_na.append(next(f for _, r in gen.issues_reponses_na for f in r.fiches if f.classe != pt.PASSEE))
            gen.etape_aiguillage = etape
        m = A6.Montage(decider=plan_par_rang(lambda k: "fiches_json" if k % 5 else "champ_en_plus"))
        with self.assertRaises(pt.ArretSansPasseportNA):
            m.lancer(crochets={"avant_execution": glisser})
        self.assertEqual(m.arrets()[0]["nom"], "A17, fiche sans passeport du portier neuf")


# --- garde de remplacement et ce que rend un refus écrit, par rôle --------------------------------------------------------

def marquer(role, g_vise=1):
    def f(g, gen):
        if g == g_vise:
            gen.suivi._r(role)["arrete"] = "A3 : rôle marqué arrêté par l'essai"
    return f


class TestRefusEcrits(unittest.TestCase):
    def test_aucun_refus_ecrit_aucun_arret(self):
        m = A6.Montage()
        bilan = m.lancer()
        for l in bilan:
            self.assertEqual(l["comptes_lot_6"]["refus_ecrits_proposeur"], {})
            self.assertEqual(l["comptes_journal_lot_3"]["refus_ecrits"], {})

    def test_proposeur_arrete_des_sa_premiere_case_onze_refus_arret_nomme(self):
        role = "proposeur-espece-2"
        m, gens = A6.Montage(), []
        with self.assertRaises(cn.ArretRemplacementRefusEcritsNA) as cm:
            m.lancer(crochets={"avant_execution": lambda g, gen: (capturer(gens)(g, gen), marquer(role)(g, gen))})
        self.assertEqual((cm.exception.role, cm.exception.n), (role, 11))
        a = m.arrets()[0]
        self.assertEqual((a["role"], a["generation"]), (role, 1))
        lignes = jn.verifier_journal(m.chemin_sortie("journaux", "journal-requetes-g1.jsonl"))
        self.assertEqual(sum(1 for l in lignes if l["evenement"] == "refus écrit" and l["role"] == role), 11)
        self.assertEqual([c for c in gens[0].coffre.consommations() if c.get("role") == role], [])
        self.assertEqual([r for r in m.adaptateurs["ad_d"].recus], [])

    def test_proposeur_arrete_apres_sa_premiere_case_dix_refus_la_course_continue(self):
        role, gens = "proposeur-espece-2", []

        def decider(identifiant, adaptateur, n):
            if adaptateur == "ad_d" and n == 0:
                gens[-1].suivi._r(role)["arrete"] = "A3 : rôle marqué arrêté par l'essai, après sa première case"
            return "fiches_json"
        m = A6.Montage(decider=decider)
        bilan = m.lancer(crochets={"avant_execution": capturer(gens)})
        self.assertEqual(len(bilan), 3)
        c1 = bilan[0]["comptes_lot_6"]
        self.assertEqual((c1["refus_ecrits_proposeur"], c1["cases_non_jouees"]), ({role: 10}, {"2": 10}))
        self.assertEqual(bilan[1]["comptes_lot_6"]["refus_ecrits_proposeur"], {})
        self.assertEqual(len([c for c in gens[0].coffre.consommations() if c.get("role") == role]), 1)

    def test_portier_arrete_fiches_au_coffre_classe_ecrite_puis_arret_5(self):
        m, gens = A6.Montage(decider=A6.toujours("fiches_json")), []
        with self.assertRaises(rg.ArretGardeCoffre):
            m.lancer(crochets={"avant_execution": lambda g, gen: (capturer(gens)(g, gen), marquer("aiguilleur")(g, gen))})
        c = gens[0].portier.comptes()
        self.assertEqual(c["au_coffre_par_refus_du_portier"], c["fiches_rendues"])
        self.assertGreater(c["fiches_rendues"], 0)
        self.assertNotIn(pt.CAUSE_NON_LUE, c["causes_fiche"])
        self.assertEqual([x for x in gens[0].coffre.consommations() if x.get("role") == "aiguilleur"], [])

    def test_portier_non_arrete_classe_comme_au_lot_5(self):
        m, gens = A6.Montage(decider=A6.toujours("fiches_json")), []
        m.lancer(crochets={"avant_execution": capturer(gens)})
        c = gens[0].portier.comptes()
        self.assertEqual(c["au_coffre_par_refus_du_portier"], 0)
        self.assertEqual(c["classes_fiche"][pt.PASSEE], c["fiches_rendues"])

    def test_portier_arrete_reponse_sans_fiche_illisible(self):
        m, gens = A6.Montage(decider=A6.toujours("vide_motivee")), []
        m.lancer(crochets={"avant_execution": lambda g, gen: (capturer(gens)(g, gen), marquer("aiguilleur")(g, gen))})
        c = gens[0].portier.comptes()
        self.assertEqual(c["classes_appel"]["réponse illisible"], 55)
        self.assertEqual(c["causes_reponse"], {pt.CAUSE_REFUS_ECRIT_REPONSE: 55})

    def test_juge_arrete_verdicts_absents_comptes_aucun_arret(self):
        m, gens = A6.Montage(decider=A6.toujours("fiches_json")), []
        bilan = m.lancer(crochets={"avant_execution": lambda g, gen: (capturer(gens)(g, gen),
                                                                      marquer("juge-espece-1")(g, gen))})
        self.assertEqual(len(bilan), 3)
        n = len(gens[0].passees_na)
        self.assertEqual(bilan[0]["comptes_lot_6"]["verdicts_absents"]["juge-espece-1"], {"refus écrit": n})
        self.assertNotIn("juge-espece-3", bilan[0]["comptes_lot_6"]["verdicts_absents"])


# --- A2 ----------------------------------------------------------------------------------------------------------------

class TestA2(unittest.TestCase):
    def test_modele_servi_egal_la_course_continue(self):
        self.assertEqual(len(A6.Montage().lancer()), 3)

    def test_version_servie_d_un_juge_qui_change_entre_deux_fiches(self):
        servi = lambda sorte, k: "modele-essai-autre" if sorte == "juge" and k >= 2 else CE.MODELE_ESSAI  # noqa: E731
        m = A6.Montage(decider=A6.toujours("fiches_json"), par_adaptateur={"ad_c1": {"modele_servi": servi}})
        with self.assertRaises(ag.ArretA2NA) as cm:
            m.lancer()
        self.assertEqual(cm.exception.role, "juge-espece-1")
        self.assertEqual(m.arrets()[0]["nom"], "A2, modèle servi absent ou changé")

    def test_modele_servi_absent_pour_un_proposeur(self):
        m = A6.Montage(par_adaptateur={"ad_d": {"modele_servi": lambda s, k: ""}})
        with self.assertRaises(ag.ArretA2NA) as cm:
            m.lancer()
        self.assertEqual(cm.exception.role, "proposeur-espece-2")

    def test_surcharge_de_juger_leve_a2_elle_meme(self):
        """La surcharge de `juger` lit la version servie de chaque juge, de fiche en fiche, et lève A2 elle-même."""
        m, gens = A6.Montage(decider=A6.toujours("fiches_json")), []
        m.lancer(crochets={"avant_execution": capturer(gens)})
        gen = gens[0]
        servis = iter(["modele-x"] * 2 + ["modele-y"] * 2)
        verdict = {"items": {k: True for k in CE.ITEMS_ESSAI}, "x": 1.0, "notable": True, "note": 1}

        def appel(etat, **kw):
            return {"r": Resultat(texte_final="", statut="ok", modele_servi=next(servis)), "lu": verdict, "motif": None,
                    "duree": 0.0}
        gen.appel = appel
        gen.modele_servi_juges = {}
        etat = {"cout": 0.0, "reste": 1.0, "coupee": False, "etape": "juges"}
        gen.juger(gen.passees_na[0], "essai-a2", etat)
        with self.assertRaises(ag.ArretA2NA):
            gen.juger(gen.passees_na[1], "essai-a2", etat)


# --- identifiants dans les requêtes des juges ------------------------------------------------------------------------------

class TestIdentifiantsJuges(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.m = A6.Montage(garder_consignes=True)
        cls.gens = []
        cls.m.lancer(crochets={"avant_execution": capturer(cls.gens)})
        cls.juges = [c for a in cls.m.adaptateurs.values() for s, c in a.consignes if s == "juge"]
        cls.portier = [c for a in cls.m.adaptateurs.values() for s, c in a.consignes if s.startswith("portier")]

    def _identifiant(self, consigne):
        corps = consigne.split("\n## La fiche\n```json\n", 1)[1].rsplit("\n```", 1)[0]
        return json.loads(corps)[rq.CLE_IDENTIFIANT_JUGE]

    def test_identifiant_reencode_de_quatorze_lettres(self):
        self.assertGreater(len(self.juges), 0)
        for c in self.juges:
            mot = self._identifiant(c)
            self.assertEqual(len(mot), 14)
            self.assertEqual(len(ident.decoder_octets(mot, 5)), 5)

    def test_aucune_suite_de_huit_hexadecimaux_dans_les_requetes(self):
        for c in self.juges + self.portier:
            self.assertFalse(ident.porte_suite_hexadecimale(c))
        for g in (2, 3):
            servi = [l["registre_servi"] for l in self.m.lignes_generation() if l["generation"] == g][0]
            self.assertIsNotNone(servi)

    def test_memes_octets_que_le_jeton_du_noyau(self):
        vus = {self._identifiant(c) for c in self.juges}
        for gen in self.gens:
            for f in gen.passees_na:
                for j in gen.conf["juges"]:
                    mot, jeton = gen.identifiant_servi_juge(j["etiquette"], f)
                    self.assertEqual(ident.decoder_octets(mot, 5), bytes.fromhex(jeton[1:]))
                    self.assertIn(mot, vus)
                self.assertEqual(ident.decoder_octets(f.identifiant, 6), bytes.fromhex(gen.jetons_noyau_na[f.identifiant][1:]))

    def test_identifiant_du_noyau_le_numero_16_mord(self):
        gen = self.gens[0]
        f = gen.passees_na[0]
        mot, jeton = gen.identifiant_servi_juge(gen.conf["juges"][0]["etiquette"], f)
        requete = rq.assembler_juge(gen.course_na.consigne_juges, f.contenu, mot, f.identifiant_case, 1)
        octets = requete.octets.replace(mot.encode("utf-8"), jeton.encode("utf-8"))
        with self.assertRaises(gm.ArretMotifInterdit):
            gen.na.garde.garder_requete(octets)
        gen.na.garde.garder_requete(requete.octets)


if __name__ == "__main__":
    unittest.main()
