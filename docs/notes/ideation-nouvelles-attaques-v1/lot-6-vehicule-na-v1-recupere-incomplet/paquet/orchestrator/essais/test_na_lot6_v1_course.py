"""Essais du lot 6 du véhicule NA-1 (1/2) : trois générations en moteur simulé, régime, gardes héritées une par une,
étapes neutralisées, `hors_course`, mémoire déclarée, journal des arrêts et des générations (E5), ligne de la génération
(E6), table « artefact » (E7), faux fournisseur et égalité avec le journal (E8, version 2), lanceur de l'orchestrateur.
Chaque garde a son cas sain et son artefact (règle R5). Données factices seules ; aucune clé ; aucun appel."""

import copy
import json
import os
import sys
import unittest

ICI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ICI)

import aides_na_lot6_v1 as A6  # noqa: E402
from aides_na_lot6_v1 import CE  # noqa: E402
from pole import appel_garde_na_v1 as ag  # noqa: E402
from pole import configuration_course_na_v1 as cfn  # noqa: E402
from pole import course_na_v1 as cn  # noqa: E402
from pole import journal_na_v3 as jn  # noqa: E402
from pole import routage_na_v1 as rt  # noqa: E402
from pole import simulation_na_v1 as sim  # noqa: E402
from pole.budget_v53 import RETIREE  # noqa: E402

_ANNEXE = os.path.join(os.path.dirname(ICI), "demonstrations", "lancer_orchestrateur_na_v1.py")
import importlib.util  # noqa: E402

_spec = importlib.util.spec_from_file_location("lancer_orchestrateur_na_v1_essais", _ANNEXE)
LO = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(LO)

PROPOSEURS = [r for r, (s, e, c, a) in CE.ROLES_ESSAI.items() if s == "proposeur" and c != "hors_course"]


def capturer(liste):
    def f(g, gen):
        liste.append(gen)
    return f


class TestTroisGenerations(unittest.TestCase):
    """Cas sain de bout en bout : trois générations, 55 appels de proposeur chacune, registre servi aux générations 2 et 3,
    six étapes déclarées (trois avec appels, une sans appel, deux retirées), journaux scellés."""

    @classmethod
    def setUpClass(cls):
        cls.m = A6.Montage()
        cls.gens = []
        cls.bilan = cls.m.lancer(crochets={"avant_execution": capturer(cls.gens)})

    def test_trois_generations_completes(self):
        self.assertEqual([l["generation"] for l in self.bilan], [1, 2, 3])
        self.assertIsNone(self.m.bilan()["arret"])

    def test_cinquante_cinq_appels_de_proposeur_par_generation(self):
        for gen in self.gens:
            self.assertEqual(sum(gen.comptes_lot6["appels_proposeur"].values()), 55)
            self.assertEqual(set(gen.comptes_lot6["appels_proposeur"]), set(PROPOSEURS))
        self.assertEqual(len(self.m.recus("proposeur")), 165)

    def test_six_etapes_trois_jouees_avec_appels(self):
        for l in self.bilan:
            e = l["etapes"]
            for n in ("proposition", "aiguillage", "juges", "etiquettes"):
                self.assertEqual(e[n], "jouee", n)
            for n in ("passe_tableau", "fusions"):
                self.assertEqual(e[n], RETIREE, n)

    def test_registre_servi_aux_generations_2_et_3(self):
        self.assertIsNone(self.bilan[0]["registre_servi"])
        for l in self.bilan[1:]:
            self.assertEqual(l["registre_servi"]["section"], "servi")
            self.assertEqual(l["registre_servi"]["requetes_l_ayant_recu"], 55)
            self.assertGreater(l["registre_servi"]["lignes_tentative"], 0)

    def test_journal_du_lot_3_ferme_a_ses_quatre_evenements(self):
        for g in (1, 2, 3):
            lignes = jn.verifier_journal(self.m.chemin_sortie("journaux", f"journal-requetes-g{g}.jsonl"), exiger_sceau=True)
            self.assertTrue({l["evenement"] for l in lignes} <= set(jn.EVENEMENTS))

    def test_journal_des_arrets_et_des_generations_scelle(self):
        lignes = self.m.journal_arrets(exiger_sceau=True)
        evts = [l["evenement"] for l in lignes]
        self.assertEqual(evts[0], "départ")
        self.assertEqual(evts.count("génération"), 3)
        self.assertEqual(evts[-1], "clôture")
        self.assertNotIn("arrêt", evts)

    def test_ligne_de_generation_fusionne_sans_renommer(self):
        for l, gen in zip(self.bilan, self.gens):
            self.assertEqual(l["comptes_melange_lot_4"], gen.na_comptes)
            self.assertEqual(l["comptes_portier_lot_5"], gen.portier.comptes())
            lignes = jn.verifier_journal(self.m.chemin_sortie("journaux", f"journal-requetes-g{l['generation']}.jsonl"))
            self.assertEqual(l["comptes_journal_lot_3"], jn.comptes(lignes))
            self.assertEqual(l["au_coffre_par_refus_du_portier"], gen.portier.comptes()["au_coffre_par_refus_du_portier"])
            self.assertIn("au_coffre_par_refus_du_portier", l["comptes_portier_lot_5"])

    def test_aucune_fiche_rendue_sans_classe(self):
        for gen in self.gens:
            self.assertEqual(gen.verifier_aucune_fiche_sans_classe(), gen.portier.comptes()["fiches_rendues"])

    def test_les_fiches_passees_sont_jugees(self):
        for gen in self.gens:
            self.assertEqual(gen.comptes_lot6["fiches_jugees"], len(gen.passees_na))
            self.assertGreater(len(gen.passees_na), 0)

    def test_fournisseurs_requis_sans_hors_course(self):
        conf = self.gens[0].conf
        self.assertEqual(cn.GenerationNA.fournisseurs_requis(conf), {"ad_a", "ad_b", "ad_c1", "ad_c2", "ad_d"})

    def test_memoire_tourne_ecrite_dans_la_generation(self):
        for g in (1, 2, 3):
            self.assertTrue(os.path.isfile(self.m.chemin_sortie(f"generation-{g}", "memoire.json")))

    def test_aiguilleur_du_noyau_jamais_appele(self):
        for gen in self.gens:
            self.assertEqual(gen.aiguilleur.decisions, {})

    def test_copies_de_configuration_journalisees(self):
        lignes = self.m.journal_arrets()
        copies = [l["copies"] for l in lignes if l["evenement"] == "copies de configuration"][0]
        for l in self.bilan:
            self.assertEqual(copies[str(l["generation"])], l["copie_configuration_sha256"])
        self.assertEqual(len(set(copies.values())), 3)


class TestRegime(unittest.TestCase):
    """Le régime nommé, trois générations, aucun étage, la ligne d'accord au montant exact, l'additif épinglé : permis
    (cas sain : `TestTroisGenerations`) ; tout autre jeu refusé avant toute écriture."""

    def _refus(self, **kw):
        m = A6.Montage()
        with self.assertRaises(cfn.RegimeRefuse):
            m.lancer(**kw)
        self.assertFalse(os.path.exists(m.sortie))

    def test_autre_nom(self):
        self._refus(regime="trois_generations_sans_etage")

    def test_deux_generations(self):
        self._refus(nombre_generations=2)

    def test_ligne_d_accord_d_un_autre_montant(self):
        self._refus(ligne_accord_usd=449.99)

    def test_additif_d_une_autre_empreinte(self):
        self._refus(additif_sha256="0" * 64)

    def test_un_etage(self):
        m = A6.Montage()
        with self.assertRaises(cfn.RegimeRefuse):
            cfn.verifier_regime(m.config, regime=cfn.REGIME, nombre_generations=3, ligne_accord_usd=450.0,
                                additif_sha256=CE.additif_essai_sha256(), additif_epingle_sha256=CE.additif_essai_sha256(),
                                etage={"plafond_etage_usd": 5.0})

    def test_plafond_de_course_autre_que_trois_fois_s17(self):
        m = A6.Montage(modifier=lambda o: o.update(plafond_course_usd=449.0))
        with self.assertRaises(cfn.RegimeRefuse):
            m.lancer(ligne_accord_usd=449.0)


class TestGardesHeritees(unittest.TestCase):
    """§ 2.13, une par une : la configuration porte la valeur que l'additif déclare (cas sain : `TestTroisGenerations`) ;
    toute autre valeur est refusée au départ, par le nom de la garde, avant toute écriture."""

    def _refus(self, modifier, garde, table=None):
        m = A6.Montage(modifier=modifier, table=table)
        with self.assertRaises(cfn.GardeHeriteeRefusee) as cm:
            m.lancer()
        self.assertEqual(cm.exception.garde, garde)
        self.assertFalse(os.path.exists(m.sortie))

    def test_a3_valeur_heritee(self):
        self._refus(lambda o: o["noyau"]["arrets"].update(a3_echecs_consecutifs=3), "A3, échecs consécutifs")

    def test_a3_autre_valeur_que_celle_de_l_additif(self):
        self._refus(lambda o: o["noyau"]["arrets"].update(a3_echecs_consecutifs=999), "A3, échecs consécutifs")

    def test_a3_valeur_declaree_sans_le_nom_de_desactivation(self):
        self._refus(lambda o: o["gardes_heritees"].update(a3_echecs_consecutifs=1000), "a3_echecs_consecutifs")

    def test_a3_desactivation_a_la_valeur_heritee(self):
        def f(o):
            o["gardes_heritees"]["a3_echecs_consecutifs"] = {cfn.NOM_DESACTIVATION: 3}
            o["noyau"]["arrets"]["a3_echecs_consecutifs"] = 3
        self._refus(f, "A3, échecs consécutifs")

    def test_a14_valeur_heritee(self):
        self._refus(lambda o: o["noyau"]["arrets"].update(a14_part_max=0.34), "A14, part d'inexploitables")

    def test_a14_desactivation_autre_que_un(self):
        def f(o):
            o["gardes_heritees"]["a14_part_max"] = {cfn.NOM_DESACTIVATION: 0.9}
            o["noyau"]["arrets"]["a14_part_max"] = 0.9
        self._refus(f, "A14, part d'inexploitables")

    def test_delai_herite(self):
        self._refus(lambda o: o["noyau"]["arrets"].update(a3_delai_s={"*": 1800}), "A3, délai")

    def test_delai_declare_sous_celui_du_kit(self):
        def f(o):
            o["gardes_heritees"]["a3_delai_s"] = 1800
            o["noyau"]["arrets"]["a3_delai_s"] = {"*": 1800}
        self._refus(f, "A3, délai")

    def test_delai_d_un_adaptateur_different(self):
        self._refus(lambda o: o["noyau"]["arrets"].update(a3_delai_s={"*": 3600, "ad_a": 1800}), "A3, délai")

    def test_a11_liste_non_vide(self):
        self._refus(lambda o: o["noyau"]["arrets"].update(a11_modeles=[CE.MODELE_ESSAI]), "A11")

    def test_nom_reserve_dans_le_noyau(self):
        def f(o):
            o["noyau"]["proposeurs"][0]["fournisseur"] = "kimi"
        self._refus(f, "S12, nom d'adaptateur réservé")

    def test_nom_reserve_dans_la_table(self):
        t = CE.objet_table()
        for c in t["cles"]:
            if c["nom"] == "cle_sans_part":
                c["adaptateurs"] = ["kimi"]
        self._refus(None, "S12, nom d'adaptateur réservé", table=t)

    def test_borne_de_remplacement_nulle(self):
        self._refus(lambda o: o["gardes_heritees"].update(garde_remplacement_refus_ecrits_proposeur=0),
                    "garde de remplacement")


class TestGardesHeriteesEnCourse(unittest.TestCase):
    """A3 et A14 désactivées : plus de onze réponses sans texte de suite d'un proposeur, du portier, d'un juge ; aucun
    rôle arrêté, aucun appel sauté, chacune classée et comptée ; le délai d'A3 actif."""

    def _roles_arretes(self, m):
        rendu = {}
        for g in (1, 2, 3):
            with open(m.chemin_sortie(f"generation-{g}", "manifeste-fin.json"), encoding="utf-8") as f:
                fin = json.load(f)
            rendu.update({r: v["arrete"] for r, v in fin["suivi_roles"]["roles"].items() if v["arrete"]})
            self.assertEqual(fin["appels_sautes"], {})
        return rendu

    def test_proposeurs_sans_texte_jamais_arretes(self):
        m, gens = A6.Montage(decider=A6.toujours("vide")), []
        bilan = m.lancer(crochets={"avant_execution": capturer(gens)})
        self.assertEqual(len(bilan), 3)
        self.assertEqual(self._roles_arretes(m), {})
        for gen, l in zip(gens, bilan):
            self.assertEqual(sum(d.get(cn.ISSUE_TEXTE_RENDU, 0) for d in gen.comptes_lot6["issues_proposeur"].values()), 55)
            self.assertEqual(l["comptes_portier_lot_5"]["classes_appel"]["réponse illisible"], 55)

    def test_portier_illisible_jamais_arrete(self):
        m = A6.Montage(decider=A6.toujours("vide_motivee"), par_adaptateur={"ad_b": {"portier_illisible": True}})
        bilan = m.lancer()
        self.assertEqual(self._roles_arretes(m), {})
        for l in bilan:
            c = l["comptes_portier_lot_5"]
            self.assertEqual(c["classes_appel"]["réponse illisible"], 55)
            self.assertEqual(c["sous_comptes_reponse_illisible"]["étiquette du portier illisible"], 55)

    def test_juges_illisibles_jamais_arretes(self):
        m = A6.Montage(decider=A6.toujours("fiches_json"),
                       par_adaptateur={"ad_a": {"juge_illisible": True}, "ad_c1": {"juge_illisible": True}})
        bilan = m.lancer()
        self.assertEqual(self._roles_arretes(m), {})
        for l in bilan:
            absents = l["comptes_lot_6"]["verdicts_absents"]
            self.assertEqual(absents["juge-espece-3"]["verdict illisible"], 55)
            self.assertEqual(absents["juge-espece-1"]["verdict illisible"], 55)

    def _horloge(self, pas):
        t = [0.0]

        def horloge():
            t[0] += pas
            return t[0]
        return horloge

    def test_appel_plus_long_que_le_delai_herite_mais_sous_celui_du_kit_lu(self):
        m, gens = A6.Montage(decider=A6.toujours("fiches_json")), []
        m.lancer(horloge=self._horloge(2000.0), crochets={"avant_execution": capturer(gens)})
        for gen in gens:
            self.assertEqual(sum(d.get(cn.ISSUE_TEXTE_RENDU, 0) for d in gen.comptes_lot6["issues_proposeur"].values()), 55)

    def test_appel_au_dela_du_delai_coupe_reponse_illisible(self):
        m, gens = A6.Montage(decider=A6.toujours("fiches_json")), []
        m.lancer(horloge=self._horloge(4000.0), crochets={"avant_execution": capturer(gens)})
        for gen in gens:
            self.assertEqual(sum(d.get(cn.ISSUE_ILLISIBLE_NON_LUE, 0)
                                 for d in gen.comptes_lot6["issues_proposeur"].values()), 55)
        self.assertEqual(self._roles_arretes(m), {})


class TestEtapesNeutralisees(unittest.TestCase):
    def test_passe_tableau_jouee_est_un_arret(self):
        def f(o):
            for e in o["noyau"]["budget"]["etapes"]:
                if e["nom"] == "passe_tableau":
                    e["plafond_relais_usd"] = 1.0
        m = A6.Montage(modifier=f)
        with self.assertRaises(cn.EtapeNeutraliseeJouee):
            m.lancer()
        self.assertEqual(m.arrets()[0]["type"], "EtapeNeutraliseeJouee")


class TestHorsCourse(unittest.TestCase):
    def test_appel_plante_d_un_lecteur_refuse_numero_12(self):
        vus = []

        def planter(g, gen):
            if g != 1:
                return
            requete = next(iter(gen.course_na.requetes.values()))
            etat = {"cout": 0.0, "reste": 10.0, "coupee": False, "etape": "etiquettes", "plafond_dur_usd": 10.0}
            try:
                gen.appel(etat, role="lecteur-etiquettes-1", role_kit="juge_ideation", fournisseur="hors_course",
                          modele=CE.MODELE_ESSAI, consigne=requete, plafond_role="lecteur",
                          session=("etiquettes", requete.identifiant_case, "plante"))
            except rt.ArretPartCle as e:
                vus.append(e)
            vus.append(etat["cout"])
        m = A6.Montage()
        m.lancer(crochets={"avant_execution": planter})
        self.assertIsInstance(vus[0], rt.ArretPartCle)
        self.assertEqual(vus[1], 0.0)
        lignes = jn.verifier_journal(m.chemin_sortie("journaux", "journal-requetes-g1.jsonl"))
        self.assertEqual([l["arret"] for l in lignes if l["evenement"] == "non envoyé"], [rt.NUMERO_ARRET_PART])


class MemoireFactice:
    def detecter(self, lot):
        return {"memoire": "factice d'essai"}

    def ajouter_memoire(self, lot, generation):
        return None


class TestMemoireDeclaree(unittest.TestCase):
    """La mémoire tourne, n'est servie à personne : avec une mémoire factice, registres, journaux et requêtes égaux à
    l'octet."""

    def test_memoire_factice_rien_ne_change(self):
        a = A6.Montage()
        a.lancer()
        b = A6.Montage()

        def remplacer(g, gen):
            gen.memoire = MemoireFactice()
        b.lancer(crochets={"avant_execution": remplacer})
        for g in (1, 2, 3):
            for nom in (f"registre-tentatives-g{g}.jsonl", f"journal-portier-g{g}.jsonl"):
                with open(a.chemin_sortie(f"generation-{g}", nom), "rb") as f1, \
                        open(b.chemin_sortie(f"generation-{g}", nom), "rb") as f2:
                    self.assertEqual(f1.read(), f2.read(), nom)
            la = [(l["sha256"], l["taille"]) for l in jn.verifier_journal(
                a.chemin_sortie("journaux", f"journal-requetes-g{g}.jsonl")) if l["evenement"] == "envoi"]
            lb = [(l["sha256"], l["taille"]) for l in jn.verifier_journal(
                b.chemin_sortie("journaux", f"journal-requetes-g{g}.jsonl")) if l["evenement"] == "envoi"]
            self.assertEqual(la, lb)
        sa = [l["registre_servi"] for l in a.lignes_generation()]
        sb = [l["registre_servi"] for l in b.lignes_generation()]
        self.assertEqual(sa, sb)
        with open(b.chemin_sortie("generation-1", "memoire.json"), encoding="utf-8") as f:
            self.assertEqual(json.load(f), {"memoire": "factice d'essai"})


class TestRienNeFuit(unittest.TestCase):
    """Hors du dossier des générations, les journaux de la course ne portent aucun contenu de réponse ni de fiche."""

    def test_marqueur_et_idee_absents_des_journaux_de_la_course(self):
        marqueur = "MARQUEURINERTEDULOTSIX"
        m = A6.Montage(marqueur=marqueur)
        m.lancer()
        for chemin in [m.chemin_sortie(cn.NOM_JOURNAL_ARRETS), m.chemin_sortie(cn.NOM_BILAN)] + \
                [m.chemin_sortie("journaux", f"journal-requetes-g{g}.jsonl") for g in (1, 2, 3)]:
            with open(chemin, encoding="utf-8") as f:
                texte = f.read()
            self.assertNotIn(marqueur, texte)
            self.assertNotIn(sim.IDEE_INERTE, texte)


class TestTableArtefact(unittest.TestCase):
    """E7 : une table de routage marquée « artefact » refuse le départ ; dans le contexte d'une génération aussi
    (mutation Z4-25 de la vérification du lot 4)."""

    def test_table_artefact_refusee_au_depart(self):
        m = A6.Montage(table=CE.objet_table(marque="artefact"))
        with self.assertRaises(rt.TableRefusee):
            m.lancer()
        self.assertFalse(os.path.exists(m.sortie))

    def test_table_artefact_refusee_dans_le_contexte_de_la_generation(self):
        o = CE.octets_table(CE.objet_table(marque="artefact"))
        t = rt.lire_table(o, cfn.sha256_octets(o), rt.MARQUE_ARTEFACT)
        m = A6.Montage()
        j = jn.JournalRequetes(m.dossier, "journal-essai-e7.jsonl")
        from aides_na_v4 import garde_essai
        pires = {r: 1.0 for r, e in t.roles.items() if e.cle != "hors_course"}
        for numero, parts in ((1, dict(CE.PARTS_ESSAI)), (None, dict(CE.PARTS_ESSAI)), (None, {})):
            with self.assertRaises(ag.ContexteRefuse) as cm:
                ag.ContexteAppelGardeNA(numero_generation=numero, table=t, parts=parts, pires_par_role=pires, journal=j,
                                        garde=garde_essai(), identifiant_case_de_session=lambda s: s[1],
                                        cumul=rt.CumulParCle(t), lire_etat_relais=lambda c: {})
            self.assertIn("table", str(cm.exception))

    def test_table_de_course_admise(self):
        m = A6.Montage()
        self.assertEqual(cfn.table_de_course(m.config).marque, rt.MARQUE_COURSE)


class TestFauxFournisseur(unittest.TestCase):
    """E8 (erratum versé v2) : le faux fournisseur garde la taille et l'empreinte du corps reçu et de la chaîne de contenu
    de chaque message ; l'égalité avec le journal s'éprouve, appel par appel."""

    def test_egalite_journal_et_chaine_recue(self):
        faux = sim.FauxFournisseurNA().demarrer()
        try:
            m = A6.Montage()
            noms = list(m.adaptateurs)
            m.adaptateurs = {n: sim.AdaptateurBoucleLocaleNA(faux.url) for n in noms}
            m.lancer()
            recues = faux.requetes_na()
        finally:
            faux.fermer()
        envois = [l for g in (1, 2, 3) for l in jn.verifier_journal(
            m.chemin_sortie("journaux", f"journal-requetes-g{g}.jsonl")) if l["evenement"] == "envoi"]
        self.assertEqual(len(envois), len(recues))
        self.assertGreater(len(envois), 165)
        for l, r in zip(envois, recues):
            self.assertEqual(len(r["messages"]), 1)
            self.assertEqual((r["messages"][0]["contenu_sha256"], r["messages"][0]["contenu_taille"]),
                             (l["sha256"], l["taille"]))
            self.assertEqual(len(r["corps_sha256"]), 64)
            self.assertGreater(r["corps_taille"], l["taille"])

    def test_empreintes_des_messages_en_blocs(self):
        corps = {"messages": [{"role": "user", "content": [{"type": "text", "text": "a"}, {"type": "text", "text": "bc"}]},
                              {"role": "system", "content": "d"}]}
        e = sim.empreintes_messages(corps)
        self.assertEqual([(x["rang"], x["bloc"], x["contenu_taille"]) for x in e], [(1, 1, 1), (1, 2, 2), (2, None, 1)])
        self.assertEqual(e[2]["contenu_sha256"], cfn.sha256_octets(b"d"))

    def test_boucle_locale_seule(self):
        with self.assertRaises(ValueError):
            sim.AdaptateurBoucleLocaleNA("http://exemple.invalid:80")


class TestLanceur(unittest.TestCase):
    """Le lanceur lève le refus du moteur réel pour ce seul régime, aux quatre conditions et confirmé ; le moteur simulé
    n'est permis qu'à l'essai à blanc ; tout autre jeu d'options est refusé avant toute écriture."""

    def _argv(self, m, sortie, **change):
        a = {"--configuration": m.chemin, "--empreinte-configuration": m.sha, "--sortie": sortie, "--regime": cfn.REGIME,
             "--generations": "3", "--ligne-accord-usd": "450", "--additif": m.config.pieces_epinglees[0].chemin,
             "--empreinte-additif": CE.additif_essai_sha256()}
        a.update({k: v for k, v in change.items() if v is not None})
        return [x for k, v in a.items() for x in (k, v)]

    def test_decider_moteur(self):
        self.assertEqual(LO.decider_moteur("simule", essai_a_blanc=True, confirmer_moteur_reel=False), "simule")
        self.assertEqual(LO.decider_moteur("reel", essai_a_blanc=False, confirmer_moteur_reel=True), "reel")
        for moteur, blanc, confirme in (("simule", False, False), ("simule", True, True), ("reel", False, False),
                                        ("reel", True, True), (None, True, False)):
            with self.assertRaises(LO.LancementRefuseNA):
                LO.decider_moteur(moteur, essai_a_blanc=blanc, confirmer_moteur_reel=confirme)

    def test_essai_a_blanc_simule(self):
        m = A6.Montage()
        sortie = os.path.join(m.dossier, "sortie-lanceur")
        self.assertEqual(LO.principal(self._argv(m, sortie) + ["--moteur", "simule", "--essai-a-blanc"]), 0)
        self.assertTrue(os.path.isfile(os.path.join(sortie, cn.NOM_BILAN)))

    def test_refus_avant_toute_ecriture(self):
        m = A6.Montage()
        sortie = os.path.join(m.dossier, "sortie-lanceur")
        cas = [(self._argv(m, sortie, **{"--regime": "autre"}), ["--moteur", "simule", "--essai-a-blanc"]),
               (self._argv(m, sortie), ["--moteur", "simule"]),
               (self._argv(m, sortie), ["--moteur", "reel"]),
               (self._argv(m, sortie, **{"--ligne-accord-usd": "449"}), ["--moteur", "reel", "--confirmer-moteur-reel"]),
               (self._argv(m, sortie, **{"--empreinte-additif": "0" * 64}), ["--moteur", "reel", "--confirmer-moteur-reel"]),
               (self._argv(m, sortie, **{"--generations": "2"}), ["--moteur", "reel", "--confirmer-moteur-reel"])]
        appels = []
        for argv, moteur in cas:
            self.assertEqual(LO.principal(argv + moteur, fabrique_reelle=lambda *a: appels.append(a)), 2)
            self.assertFalse(os.path.exists(sortie))
        self.assertEqual(appels, [])

    def test_moteur_reel_aux_quatre_conditions_atteint_la_fabrique(self):
        m = A6.Montage()
        sortie = os.path.join(m.dossier, "sortie-lanceur")
        appels = []

        def fabrique_reelle(config, table, base):
            appels.append(table.marque)
            return lambda s: (m.adaptateurs, None)
        rc = LO.principal(self._argv(m, sortie) + ["--moteur", "reel", "--confirmer-moteur-reel"],
                          fabrique_reelle=fabrique_reelle)
        self.assertEqual(rc, 0)
        self.assertEqual(appels, ["course"])

    def test_verifier_seulement_n_ecrit_rien(self):
        m = A6.Montage()
        sortie = os.path.join(m.dossier, "sortie-lanceur")
        rc = LO.principal(self._argv(m, sortie) + ["--moteur", "simule", "--essai-a-blanc", "--verifier-seulement"])
        self.assertEqual(rc, 0)
        self.assertFalse(os.path.exists(sortie))


if __name__ == "__main__":
    unittest.main()
_ = copy
