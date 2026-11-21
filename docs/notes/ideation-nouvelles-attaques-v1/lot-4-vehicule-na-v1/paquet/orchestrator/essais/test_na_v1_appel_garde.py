"""Essais du lot 4 du véhicule NA-1 — table des rôles et des clés, surcharge d'`appel` (`AppelGardeNA`), contre le vrai `appel`
du noyau (`OrchestreV56.appel`, porté par `NoyauEssai`) et, pour la composition, contre la classe de génération v56.

Chaque garde : un cas sain et un artefact (R5). Arrêts n° 1, n° 12 (D11), n° 13, n° 16 au point d'envoi ; envoi refusé sans
coût ; `hors_course` ; journal égal à l'octet à l'envoi ; égalité refusée après la ligne « envoi » (erratum 2) ; journal en
panne (erratum 3) ; refus écrits ; A2. Données factices seules ; aucun appel, aucune clé.
"""

import os
import re
import shutil
import sys
import unittest
from unittest import mock

ICI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ICI)

import aides_na_lot4_v1 as H  # noqa: E402
import aides_na_v4 as A  # noqa: E402
from pole import appel_garde_na_v1 as ag  # noqa: E402
from pole import journal_na_v3 as jn  # noqa: E402
from pole import routage_na_v1 as rt  # noqa: E402


class Base(unittest.TestCase):
    def montage(self, **kw):
        m = H.Montage(**kw)
        self.addCleanup(shutil.rmtree, m.dossier, True)
        return m

    def assertSansCout(self, m, role):
        self.assertEqual(m.dernier_etat["cout"], 0.0)
        self.assertEqual(m.gen.coffre.consommations(), [])
        self.assertNotIn(role, m.gen.suivi.roles)
        self.assertEqual(m.gen.suivi.depassements_a14(), {})
        self.assertEqual(m.cumul.etat(), {k: "0.000000" for k in m.cumul.etat()})
        self.assertEqual(m.recus(), [])


# --- la table ----------------------------------------------------------------------------------------------------------

class TestTable(Base):
    def test_table_de_course_lue_a_son_empreinte(self):
        t = H.table()
        self.assertEqual(t.marque, "course")
        self.assertEqual(t.entree("juge-espece-3").cle, "cle_a")
        self.assertEqual(t.entree("proposeur-espece-3").cle, "cle_a")
        self.assertEqual(t.cles["cle_c"].adaptateurs, ("ad_c1", "ad_c2"))
        self.assertEqual(t.cles["cle_a"].part_micro, 156_560_000)

    def test_empreinte_differente_refusee(self):
        o, s = H.octets_table(H.objet_table_course())
        with self.assertRaises(rt.EmpreinteTableDifferente) as cm:
            rt.lire_table(o + b" ", s, "course")
        self.assertEqual(cm.exception.numero, 14)
        self.assertIn("table des rôles et des clés", str(cm.exception))

    def test_artefact_jamais_charge_comme_course(self):
        o, s = H.octets_table(H.objet_table_artefact())
        with self.assertRaises(rt.TableRefusee):
            rt.lire_table(o, s, "course")
        with self.assertRaises(rt.TableRefusee):
            rt.lire_table(o, s, "ligne à part")
        self.assertEqual(rt.lire_table(o, s, "artefact").marque, "artefact")
        m = self.montage()
        with self.assertRaises(ag.ContexteRefuse):
            ag.ContexteAppelGardeNA(numero_generation=1, table=rt.lire_table(o, s, "artefact"), parts={}, pires_par_role={},
                                    journal=m.journal, garde=m.garde, identifiant_case_de_session=H.case_de_session,
                                    cumul=m.cumul)

    def test_formes_refusees(self):
        def refusee(changer):
            o = H.objet_table_course()
            changer(o)
            octets, s = H.octets_table(o)
            with self.assertRaises(rt.TableRefusee):
                rt.lire_table(octets, s, "course")

        refusee(lambda o: o["cles"].pop())  # hors_course absent
        refusee(lambda o: o["cles"][1]["adaptateurs"].append("ad_a"))  # un adaptateur sur deux clés
        refusee(lambda o: o["roles"][0].update(cle="cle_sans_part", adaptateur="ad_sans_part"))  # rôle sur une clé sans part
        refusee(lambda o: o["cles"][0].update(part_usd=156.555))  # part plus fine que le centime
        refusee(lambda o: o["cles"][0].update(relais=None))  # clé Claude sans relais
        refusee(lambda o: o["cles"][0].update(relais="http://exemple.invalid:9"))  # relais non local
        refusee(lambda o: o["roles"][0].update(adaptateur="ad_b"))  # adaptateur qui n'est pas celui de la clé
        refusee(lambda o: o["roles"].append(dict(o["roles"][0])))  # étiquette en double
        refusee(lambda o: o["cles"][4].update(part_usd=1.0))  # clé sans part qui porte une part
        refusee(lambda o: o.update(plafond_ligne_usd=5.0))  # plafond de ligne sur une table de course

    def test_parts_et_pires_exiges(self):
        t = H.table()
        self.assertEqual(rt.lire_parts(t, H.parts(t))["cle_d"], 17_010_000)
        with self.assertRaises(rt.TableRefusee):
            rt.lire_parts(t, dict(H.parts(t), cle_d=17.02))  # autre que la table scellée
        with self.assertRaises(rt.TableRefusee):
            rt.lire_parts(t, {k: v for k, v in H.parts(t).items() if k != "cle_a"})
        p = H.pires(t)
        self.assertEqual(rt.lire_pires(t, p)["proposeur-espece-2"], 6_050_000)
        with self.assertRaises(rt.TableRefusee):
            rt.lire_pires(t, {k: v for k, v in p.items() if k != "aiguilleur"})
        with self.assertRaises(rt.TableRefusee):
            rt.lire_pires(t, dict(p, aiguilleur=0))

    def test_lignes_a_part_lues(self):
        for objet, plafond in ((H.objet_table_temoins(), 5_000_000), (H.objet_table_sonde(), 1_000_000)):
            t = H.table(objet, "ligne à part")
            self.assertEqual(t.plafond_ligne_micro, plafond)
            self.assertEqual(rt.lire_parts(t, {}), {})
            with self.assertRaises(rt.TableRefusee):
                rt.lire_parts(t, {"cle_a": 1.0})


# --- arrêt n° 12 (D11) -------------------------------------------------------------------------------------------------

class TestArret12(Base):
    def test_cas_sain_chaque_cle_lance_et_compte(self):
        m = self.montage()
        for i, (role, cle) in enumerate((("proposeur-espece-3", "cle_a"), ("proposeur-espece-4", "cle_b"),
                                         ("proposeur-espece-1", "cle_c"), ("proposeur-espece-2", "cle_d"))):
            a = m.appeler(role, H.requete_proposeur(1, i))
            self.assertEqual(a["issue_na"], "ok")
            self.assertEqual(m.cumul.cumul(cle), 10_000)
        self.assertEqual(len(m.recus()), 4)

    def test_cas_sain_neuf_juge_et_proposeur_espece_3_sur_la_meme_cle(self):
        m = self.montage()
        m.appeler("proposeur-espece-3", H.requete_proposeur(1, 0))
        m.appeler("juge-espece-3", H.requete_juge(1, 0))
        self.assertEqual(m.cumul.cumul("cle_a"), 20_000)
        self.assertEqual([r["role_kit"] for r in m.ad["ad_a"].recus], ["proposeur_ideation", "juge_ideation"])

    def test_part_egale_permise_un_centime_de_trop_refuse(self):
        m = self.montage()
        m.cumul.ajouter("cle_d", 10_960_000)  # 10,96 + 6,05 = 17,01 : égal à la part
        m.appeler("proposeur-espece-2", H.requete_proposeur(1, 0))
        self.assertEqual(m.cumul.cumul("cle_d"), 10_970_000)
        with self.assertRaises(rt.ArretPartCle) as cm:  # 10,97 + 6,05 = 17,02 : un centime de trop
            m.appeler("proposeur-espece-2", H.requete_proposeur(1, 1))
        e = cm.exception
        self.assertEqual((e.numero, e.clause, e.cle), (12, "première", "cle_d"))
        self.assertEqual(re.findall(r"\d+", str(e)), ["12"])  # aucun montant dans le message
        self.assertEqual((e.cumul_micro, e.pire_micro, e.limite_micro), (10_970_000, 6_050_000, 17_010_000))
        ligne = m.lignes()[-1]
        self.assertEqual((ligne["evenement"], ligne["arret"], ligne["cle"], ligne["clause"], ligne["cout_usd"]),
                         ("non envoyé", 12, "cle_d", "première", 0.0))
        self.assertEqual(len(m.ad["ad_d"].recus), 1)

    def refuse_12(self, m, role, requete, fournisseur, cle_dite):
        with self.assertRaises(rt.ArretPartCle) as cm:
            m.appeler(role, requete, fournisseur=fournisseur)
        self.assertEqual((cm.exception.clause, cm.exception.cle), ("seconde", cle_dite))
        self.assertEqual(m.lignes()[-1]["evenement"], "non envoyé")
        self.assertEqual(m.lignes()[-1]["arret"], 12)
        return cm.exception

    def test_artefact_en_course_aiguilleur_sur_la_cle_de_l_espece_3(self):
        m = self.montage()
        self.refuse_12(m, "aiguilleur", H.requete_portier(1, 0), "ad_a", "cle_a")
        self.assertSansCout(m, "aiguilleur")

    def test_artefact_table_plantee_juge_espece_3_sur_la_cle_du_proposeur(self):
        t = H.table(H.objet_table_artefact(), "artefact")
        self.assertEqual(t.router("juge-espece-3", "ad_x").cle, "cle_x")
        self.assertEqual(t.router("proposeur-espece-3", "ad_a").cle, "cle_a")
        with self.assertRaises(rt.ArretPartCle) as cm:
            t.router("juge-espece-3", "ad_a")
        self.assertEqual((cm.exception.clause, cm.exception.cle), ("seconde", "cle_a"))

    def test_proposeur_espece_2_sur_le_deuxieme_relais_refuse(self):
        m = self.montage()
        self.refuse_12(m, "proposeur-espece-2", H.requete_proposeur(1, 0), "ad_c1", "cle_c")
        self.refuse_12(m, "proposeur-espece-2", H.requete_proposeur(1, 0), "ad_a", "cle_a")

    def test_envoi_a_la_cle_sans_part_refuse(self):
        m = self.montage()
        e = self.refuse_12(m, "proposeur-espece-3", H.requete_proposeur(1, 0), "ad_sans_part", "cle_sans_part")
        self.assertTrue(e.motif.startswith("envoi adressé à une clé sans part"))

    def test_adaptateur_hors_table_refuse(self):
        m = self.montage()
        e = self.refuse_12(m, "proposeur-espece-3", H.requete_proposeur(1, 0), "ad_inconnu", "adaptateur hors table")
        self.assertEqual(e.motif, "adaptateur absent de la table")

    def test_juge_espece_3_sur_la_cle_de_l_aiguilleur_refuse(self):
        m = self.montage()
        self.refuse_12(m, "juge-espece-3", H.requete_juge(1, 0), "ad_b", "cle_b")

    def test_autre_adaptateur_de_la_meme_cle_refuse(self):
        m = self.montage()
        self.refuse_12(m, "proposeur-espece-1", H.requete_proposeur(1, 0), "ad_c2", "cle_c")

    def test_role_absent_de_la_table_refuse(self):
        m = self.montage()
        self.refuse_12(m, "proposeur-espece-9", H.requete_proposeur(1, 0), "ad_a", "cle_a")

    def test_lignes_a_part_par_leur_table_non_refusees(self):
        from pole import requete_na_v3 as rq
        import aides_na_lot3_v3 as L3
        c = H.cases()["reserve"]
        m = self.montage(objet=H.objet_table_temoins(), marque="ligne à part", journal_nom="journal-temoins.jsonl")
        req = rq.assembler_portier_fiche(L3.consigne_portier(), L3.contenu_fiche(c), c.identifiant)
        self.assertEqual(m.appeler("aiguilleur", req, fournisseur="ad_a")["issue_na"], "ok")
        self.assertEqual(m.cumul.cumul("épreuve des témoins"), 10_000)
        s = self.montage(objet=H.objet_table_sonde(), marque="ligne à part", journal_nom="journal-sonde.jsonl")
        sonde = rq.assembler_sonde_refus(L3.gabarit(), c)
        self.assertEqual(s.appeler("proposeur-espece-4", sonde, fournisseur="ad_a")["issue_na"], "ok")
        with self.assertRaises(rt.ArretPartCle):  # le même rôle, présenté à la table de la course : refusé
            self.montage().appeler("proposeur-espece-4", H.requete_proposeur(1, 0), fournisseur="ad_a")

    def test_ligne_a_part_a_son_plafond(self):
        from pole import requete_na_v3 as rq
        import aides_na_lot3_v3 as L3
        c = H.cases()["reserve"]
        s = self.montage(objet=H.objet_table_sonde(), marque="ligne à part", journal_nom="journal-sonde.jsonl")
        sonde = rq.assembler_sonde_refus(L3.gabarit(), c)
        s.cumul.ajouter("sonde de refus", 0)
        s.contexte.pires_micro["proposeur-espece-4"] = 1_000_000  # pire égal au plafond : permis
        self.assertEqual(s.appeler("proposeur-espece-4", sonde, fournisseur="ad_a")["issue_na"], "ok")
        with self.assertRaises(rt.ArretPartCle) as cm:
            s.appeler("proposeur-espece-4", sonde, fournisseur="ad_a")
        self.assertEqual((cm.exception.clause, cm.exception.cle), ("première", "cle_a"))
        self.assertIn("plafond de la ligne", str(cm.exception))


# --- hors_course -------------------------------------------------------------------------------------------------------

class TestHorsCourse(Base):
    def test_lecteur_etiquettes_plante_refuse_sans_erreur_de_dictionnaire(self):
        m = self.montage()
        del m.gen.ad["hors_course"]  # le noyau n'a pas d'adaptateur de ce nom : une fuite serait une KeyError
        with self.assertRaises(rt.ArretPartCle) as cm:
            m.appeler("lecteur-etiquettes-1", H.requete_juge(1, 0), fournisseur="hors_course")
        self.assertEqual(cm.exception.clause, "seconde")
        self.assertTrue(cm.exception.motif.startswith("rôle routé vers hors_course"))
        self.assertEqual(m.lignes()[-1]["evenement"], "non envoyé")
        self.assertSansCout(m, "lecteur-etiquettes-1")

    def test_consigne_en_chaine_d_un_role_hors_course(self):
        m = self.montage()
        with self.assertRaises(rt.ArretPartCle):
            m.appeler("lecteur-etiquettes-1", "consigne du noyau, en chaîne", fournisseur="hors_course",
                      session=("etiquettes", "kaku", "lecteur"))
        self.assertEqual(m.lignes()[-1]["arret"], 12)


# --- envoi refusé sans coût --------------------------------------------------------------------------------------------

class TestEnvoiRefuseSansCout(Base):
    def test_appel_permis_compte_sur_sa_cle(self):
        m = self.montage()
        m.appeler("proposeur-espece-3", H.requete_proposeur(1, 0))
        self.assertAlmostEqual(m.dernier_etat["cout"], 0.01)
        self.assertEqual(len(m.gen.coffre.consommations()), 1)
        self.assertEqual(m.cumul.cumul("cle_a"), 10_000)
        self.assertEqual(m.gen.suivi.roles["proposeur-espece-3"]["appels"], 1)

    def test_refus_12_sans_cout(self):
        m = self.montage()
        with self.assertRaises(rt.ArretPartCle):
            m.appeler("proposeur-espece-2", H.requete_proposeur(1, 0), fournisseur="ad_c1")
        self.assertSansCout(m, "proposeur-espece-2")
        ligne = m.lignes()[-1]
        self.assertEqual((ligne["arret"], ligne["cle"], ligne["cout_usd"]), (12, "cle_c", 0.0))
        self.assertEqual(m.gen.na_comptes["non_envoyes"], {"proposeur-espece-2": {"12": 1}})

    def test_refus_16_sans_cout(self):
        m = self.montage()
        req = H.requete_proposeur(1, 0, synthese_octets=A.SYNTHESE_FACTICE + "la graine factice\n".encode())
        with self.assertRaises(ag.ArretMotifNA):
            m.appeler("proposeur-espece-3", req)
        self.assertSansCout(m, "proposeur-espece-3")
        self.assertEqual(m.gen.na_comptes["non_envoyes"], {"proposeur-espece-3": {"16": 1}})

    def test_premiere_clause_sans_cout(self):
        m = self.montage()
        m.cumul.ajouter("cle_d", 10_970_000)
        with self.assertRaises(rt.ArretPartCle):
            m.appeler("proposeur-espece-2", H.requete_proposeur(1, 0))
        self.assertEqual(m.dernier_etat["cout"], 0.0)
        self.assertEqual(m.gen.coffre.consommations(), [])
        self.assertEqual(m.cumul.cumul("cle_d"), 10_970_000)
        self.assertNotIn("proposeur-espece-2", m.gen.suivi.roles)


# --- arrêt n° 16 au point d'envoi --------------------------------------------------------------------------------------

class TestArret16(Base):
    def test_requetes_saines_passent(self):
        m = self.montage()
        m.appeler("proposeur-espece-3", H.requete_proposeur(1, 0))
        m.appeler("aiguilleur", H.requete_portier(1, 0))
        m.appeler("juge-espece-1", H.requete_juge(1, 0))
        self.assertEqual([l["evenement"] for l in m.lignes()], ["envoi", "envoi", "envoi"])

    def refuse_16(self, m, role, req, famille, rang):
        with self.assertRaises(ag.ArretMotifNA) as cm:
            m.appeler(role, req)
        e = cm.exception
        self.assertEqual((e.numero, e.famille, e.rang), (16, famille, rang))
        ligne = m.lignes()[-1]
        self.assertEqual((ligne["evenement"], ligne["arret"], ligne["famille"], ligne["rang_motif"]),
                         ("non envoyé", 16, famille, rang))
        return e, ligne

    def test_motif_en_clair_refuse_famille_et_rang(self):
        m = self.montage()
        req = H.requete_proposeur(1, 0, synthese_octets=A.SYNTHESE_FACTICE + "la graine factice\n".encode())
        self.refuse_16(m, "proposeur-espece-3", req, "composition et tenue", 1)

    def test_motif_sous_forme_normalisee_refuse(self):
        for forme in ("graine-factice", "graine factice", "graine_factice", "graine—factice", "GRAINE  factice",
                      "grai​ne factice"):
            m = self.montage()
            req = H.requete_proposeur(1, 0, synthese_octets=A.SYNTHESE_FACTICE + f"une {forme}\n".encode())
            self.refuse_16(m, "proposeur-espece-3", req, "composition et tenue", 1)

    def test_motif_dans_une_fiche_servie_au_juge(self):
        import aides_na_lot3_v3 as L3
        from pole import requete_na_v3 as rq
        m = self.montage()
        c = H.cases()["1"][0]
        contenu = dict(L3.contenu_fiche(c), idee="une empreinte 0123abcd4567 dans une idée factice")
        req = rq.assembler_juge(L3.consigne_juge(), contenu, L3.identifiant_juge(), c.identifiant, 1)
        self.refuse_16(m, "juge-espece-1", req, "identité et dépôt", 2)

    def test_texte_trouve_seulement_au_journal(self):
        m = self.montage()
        req = H.requete_proposeur(1, 0, synthese_octets=A.SYNTHESE_FACTICE + "la graine-factice\n".encode())
        e, ligne = self.refuse_16(m, "proposeur-espece-3", req, "composition et tenue", 1)
        self.assertEqual(ligne["texte_trouve"], "graine factice")
        for porteur in (str(e), repr(e), repr(e.args), repr(vars(e))):
            self.assertNotIn("graine", porteur)
        self.assertIsNone(e.__context__)
        self.assertIsNone(e.__cause__)


# --- égalité et journal ------------------------------------------------------------------------------------------------

class TestEgalite(Base):
    def test_journal_egal_a_l_octet_a_l_envoi(self):
        m = self.montage(generation=2)
        cas = [("proposeur-espece-3", H.requete_proposeur(2, 0)), ("aiguilleur", H.requete_portier(2, 1)),
               ("aiguilleur", H.requete_portier_sans_fiche(2, 2)), ("juge-espece-1", H.requete_juge(2, 3))]
        for role, req in cas:
            m.appeler(role, req)
        envois = [l for l in m.lignes() if l["evenement"] == "envoi"]
        recus = m.recus()
        self.assertEqual(len(envois), 4)
        par_role = {}
        for r in recus:
            par_role.setdefault(r["role_kit"], []).append(r)
        recus_ordonnes = m.ad["ad_a"].recus + m.ad["ad_b"].recus + m.ad["ad_c1"].recus
        for (role, req), ligne, recu in zip(cas, envois, recus_ordonnes):
            octets = recu["consigne"].encode("utf-8")
            self.assertEqual(octets, req.octets)
            self.assertEqual((H.sha(octets), len(octets)), (ligne["sha256"], ligne["taille"]))
            self.assertEqual(ligne["role"], role)
        self.assertEqual(ag.comptes_envois_na(m.lignes())["partis"],
                         {"proposeur-espece-3": 1, "aiguilleur": 2, "juge-espece-1": 1})

    def test_divergence_refusee_apres_la_ligne_envoi(self):
        m = self.montage()
        req = H.requete_proposeur(1, 0)
        with mock.patch.object(H.GenerationEssai, "_chaine_pour_noyau_na",
                               lambda self, envoi: envoi.octets.decode("utf-8") + " "):
            with self.assertRaises(ag.ArretRequeteJournaliseeNA) as cm:
                m.appeler("proposeur-espece-3", req)
        self.assertEqual(cm.exception.cause, "égalité")
        lignes = m.lignes()
        self.assertEqual([l["evenement"] for l in lignes], ["envoi", "non envoyé"])
        self.assertEqual(lignes[1]["arret"], ag.ARRET_REQUETE_JOURNALISEE)
        self.assertTrue(lignes[1]["cause"].endswith(f"renvoi à la ligne « envoi » de rang {lignes[0]['rang']}"))
        self.assertEqual((lignes[1]["sha256"], lignes[1]["cout_usd"]), (lignes[0]["sha256"], 0.0))
        self.assertSansCout(m, "proposeur-espece-3")
        c = ag.comptes_envois_na(lignes)
        self.assertEqual((c["partis"], c["journalises_puis_refuses"]), ({}, {"proposeur-espece-3": 1}))

    def test_comptes_refusent_un_renvoi_faux(self):
        m = self.montage()
        m.appeler("proposeur-espece-3", H.requete_proposeur(1, 0))
        lignes = list(m.lignes())
        faux = dict(lignes[0], evenement="non envoyé", arret=ag.ARRET_REQUETE_JOURNALISEE, rang=2,
                    cause=ag.CAUSE_EGALITE + " ; renvoi à la ligne « envoi » de rang 9")
        with self.assertRaises(jn.JournalReecrit):
            ag.comptes_envois_na(lignes + [faux])

    def test_requete_non_assemblee_refusee(self):
        m = self.montage()
        req = H.requete_proposeur(1, 0)
        with self.assertRaises(ag.ArretRequeteJournaliseeNA) as cm:
            m.appeler("proposeur-espece-3", req.octets.decode("utf-8"), session=H.session_de(req))
        self.assertEqual(cm.exception.cause, "requête non assemblée")
        self.assertEqual(m.lignes()[-1]["arret"], ag.ARRET_REQUETE_JOURNALISEE)
        self.assertSansCout(m, "proposeur-espece-3")

    def test_case_incoherente_refusee(self):
        m = self.montage()
        req = H.requete_proposeur(1, 0)
        autre = H.requete_proposeur(1, 1)
        with self.assertRaises(ag.ArretRequeteJournaliseeNA) as cm:
            m.appeler("proposeur-espece-3", req, session=H.session_de(autre))
        self.assertEqual(cm.exception.cause, "case incohérente")
        self.assertSansCout(m, "proposeur-espece-3")

    def test_generation_incoherente_refusee(self):
        m = self.montage(generation=1)
        with self.assertRaises(ag.ArretRequeteJournaliseeNA) as cm:
            m.appeler("proposeur-espece-3", H.requete_proposeur(2, 0))
        self.assertEqual(cm.exception.cause, "génération incohérente")
        self.assertSansCout(m, "proposeur-espece-3")


class TestJournalEnPanne(Base):
    def panne(self, m):
        with self.assertRaises(ag.ArretRequeteJournaliseeNA) as cm:
            m.appeler("proposeur-espece-3", H.requete_proposeur(1, 0))
        self.assertEqual(cm.exception.cause, "journal")
        self.assertSansCout(m, "proposeur-espece-3")
        self.assertEqual(m.gen.na_comptes["non_envoyes"], {"proposeur-espece-3": {ag.ARRET_REQUETE_JOURNALISEE: 1}})

    def test_fichier_supprime(self):
        m = self.montage()
        os.remove(m.journal.chemin)
        self.panne(m)

    def test_fichier_remplace_par_un_dossier(self):
        m = self.montage()
        os.remove(m.journal.chemin)
        os.mkdir(m.journal.chemin)
        self.panne(m)

    def test_ecriture_en_panne(self):
        m = self.montage()
        with mock.patch.object(jn.os, "write", side_effect=OSError(5, "panne simulée")):
            self.panne(m)

    def test_journal_reecrit_d_une_autre_main(self):
        m = self.montage()
        with open(m.journal.chemin, "ab") as f:
            f.write(b"{}\n")
        self.panne(m)


class TestNonLance(Base):
    def test_coupure_au_plafond_dur(self):
        m = self.montage()
        a = m.appeler("proposeur-espece-3", H.requete_proposeur(1, 0), etat=m.etat(reste=1.0, cout=1.0))
        self.assertIsNone(a)
        lignes = m.lignes()
        self.assertEqual([l["evenement"] for l in lignes], ["envoi", "non lancé"])
        self.assertEqual(lignes[1]["cause"], jn.CAUSE_NON_LANCE)
        self.assertEqual(m.recus(), [])
        self.assertEqual(m.cumul.cumul("cle_a"), 0)
        self.assertEqual(m.gen.na_comptes["non_lances"], {"proposeur-espece-3": 1})
        self.assertEqual(ag.comptes_envois_na(lignes)["journalises_non_lances"], {"proposeur-espece-3": 1})


# --- refus écrits ------------------------------------------------------------------------------------------------------

class TestRefusEcrit(Base):
    def test_aucun_role_arrete_aucun_refus_ecrit(self):
        m = self.montage()
        a = m.appeler("proposeur-espece-3", H.requete_proposeur(1, 0))
        self.assertNotIn("refus_ecrit", a)
        self.assertEqual(m.gen.na_comptes["refus_ecrits"], {})

    def test_role_arrete_refus_ecrit_par_sorte(self):
        cas = [("proposeur-espece-3", H.requete_proposeur(1, 0), "rien"),
               ("aiguilleur", H.requete_portier(1, 1), "fiche au coffre"),
               ("aiguilleur", H.requete_portier_sans_fiche(1, 2), "réponse classée"),
               ("juge-espece-1", H.requete_juge(1, 3), "verdict absent")]
        for role, req, rendu in cas:
            m = self.montage()
            m.gen.suivi._r(role)["arrete"] = "A3 : arrêt marqué par l'essai"
            a = m.appeler(role, req)
            self.assertEqual((a["issue_na"], a["refus_ecrit"].rendu, a["lu"], a["r"]), ("refus écrit", rendu, None, None))
            ligne = m.lignes()[-1]
            self.assertEqual((ligne["evenement"], ligne["garde"], ligne["cout_usd"]), ("refus écrit", "A3", 0.0))
            self.assertEqual(m.recus(), [])
            self.assertEqual(m.dernier_etat["cout"], 0.0)
            self.assertEqual(m.gen.coffre.consommations(), [])
            self.assertEqual(m.gen.na_comptes["refus_ecrits"], {role: {"A3": 1}})


# --- arrêt n° 1 --------------------------------------------------------------------------------------------------------

class TestArret1(Base):
    REFUS = {"statut": "refus", "refus": {"evenement": "assistant.stop_reason", "motif": "refus factice"}, "texte_final": ""}

    def test_reponse_normale_lue(self):
        m = self.montage()
        a = m.appeler("proposeur-espece-3", H.requete_proposeur(1, 0), lire=lambda t: t)
        self.assertEqual((a["issue_na"], a["lu"]), ("ok", "texte factice inerte"))
        self.assertEqual(m.gen.na_arrets_consignes, [])

    def test_refus_de_classifieur_consigne_non_relance(self):
        m = self.montage(reglages={"ad_a": [self.REFUS]})
        a = m.appeler("proposeur-espece-3", H.requete_proposeur(1, 0))
        self.assertEqual(a["issue_na"], "arrêt n° 1, consigné, non relancé")
        self.assertIsNone(a["lu"])
        self.assertEqual(len(m.ad["ad_a"].recus), 1)
        self.assertEqual(m.gen.na_arrets_consignes, [{"arret": 1, "role": "proposeur-espece-3",
                                                      "evenement": "assistant.stop_reason"}])
        self.assertEqual(m.gen.na_comptes["arrets_consignes"], {"proposeur-espece-3": {"1": 1}})

    def test_portee_course_arrete(self):
        m = self.montage(portee_arret_1="course", reglages={"ad_a": [self.REFUS]})
        with self.assertRaises(ag.ArretClassifieurNA) as cm:
            m.appeler("proposeur-espece-3", H.requete_proposeur(1, 0))
        self.assertEqual(cm.exception.numero, 1)

    def test_evenement_du_kit_apres_refus(self):
        r = dict(self.REFUS, refus={"evenement": "system.model_refusal_no_fallback"})
        m = self.montage(reglages={"ad_a": [r]})
        self.assertEqual(m.appeler("proposeur-espece-3", H.requete_proposeur(1, 0))["issue_na"],
                         "arrêt n° 1, consigné, non relancé")


# --- arrêt n° 13 -------------------------------------------------------------------------------------------------------

class TestArret13(Base):
    ERREUR = {"statut": "erreur", "erreur": "erreur factice inerte", "texte_final": "", "cout_declare_usd": 0.0}
    SYNTHETIQUE = {"statut": "refus", "texte_final": "", "cout_declare_usd": 0.0,
                   "refus": {"evenement": "assistant.model", "modele_servi": ag.MODELE_SYNTHETIQUE}}

    def test_reponse_normale_aucune_lecture_du_relais(self):
        m = self.montage()
        m.appeler("proposeur-espece-3", H.requete_proposeur(1, 0))
        self.assertEqual(m.lectures_relais, [])

    def test_refus_pour_credit_au_relais_arret_13_qui_dit_la_cle(self):
        m = self.montage(etat_relais=H.etat_relais_credit(), reglages={"ad_a": [self.ERREUR]})
        with self.assertRaises(ag.ArretCreditNA) as cm:
            m.appeler("proposeur-espece-3", H.requete_proposeur(1, 0))
        self.assertEqual((cm.exception.numero, cm.exception.cle), (13, "cle_a"))
        self.assertIn("cle_a", str(cm.exception))
        self.assertEqual(m.lectures_relais, ["cle_a"])

    def test_erreur_sans_refus_au_relais_cause_non_etablie(self):
        m = self.montage(reglages={"ad_b": [self.ERREUR]})
        a = m.appeler("proposeur-espece-4", H.requete_proposeur(1, 0))
        self.assertEqual(a["issue_na"], "réponse illisible, cause non établie")
        self.assertEqual(m.gen.na_comptes["cause_non_etablie"], {"proposeur-espece-4": 1})
        self.assertEqual(m.gen.na_journal_arrets_cles["cause_non_etablie"], {"cle_b": 1})
        self.assertEqual(m.lectures_relais, ["cle_b"])

    def test_relais_illisible_compte(self):
        m = self.montage(etat_relais=ag.EtatRelaisIllisible("injoignable"), reglages={"ad_a": [self.ERREUR]})
        a = m.appeler("proposeur-espece-3", H.requete_proposeur(1, 0))
        self.assertEqual(a["issue_na"], "réponse illisible, cause non établie")
        self.assertEqual(m.gen.na_comptes["etat_relais_illisible"], {"proposeur-espece-3": 1})

    def test_message_synthetique_de_l_outil_lu_comme_erreur_non_comme_a2(self):
        m = self.montage(etat_relais=H.etat_relais_credit(), reglages={"ad_a": [self.SYNTHETIQUE]})
        with self.assertRaises(ag.ArretCreditNA):
            m.appeler("proposeur-espece-3", H.requete_proposeur(1, 0))
        m = self.montage(reglages={"ad_a": [self.SYNTHETIQUE]})
        self.assertEqual(m.appeler("proposeur-espece-3", H.requete_proposeur(1, 0))["issue_na"],
                         "réponse illisible, cause non établie")

    def test_relais_de_protocole_budget_depasse_arret_13(self):
        m = self.montage(reglages={"ad_d": [dict(self.ERREUR, statut="budget_depasse")]})
        with self.assertRaises(ag.ArretCreditNA) as cm:
            m.appeler("proposeur-espece-2", H.requete_proposeur(1, 0))
        self.assertEqual(cm.exception.cle, "cle_d")

    def test_commande_externe_en_erreur_sans_lecture_du_relais(self):
        m = self.montage(reglages={"ad_c1": [self.ERREUR]})
        self.assertEqual(m.appeler("proposeur-espece-1", H.requete_proposeur(1, 0))["issue_na"], "erreur")
        self.assertEqual(m.lectures_relais, [])

    def test_relais_montre_refus_credit(self):
        self.assertFalse(ag.relais_montre_refus_credit(H.etat_relais_sain()))
        self.assertTrue(ag.relais_montre_refus_credit(H.etat_relais_credit()))
        self.assertFalse(ag.relais_montre_refus_credit(dict(H.etat_relais_credit(), refus=0)))
        self.assertFalse(ag.relais_montre_refus_credit(dict(H.etat_relais_credit(), refus=1, refus_modele=1)))
        self.assertFalse(ag.relais_montre_refus_credit(dict(H.etat_relais_sain(), refus=3)))
        with self.assertRaises(ag.EtatRelaisIllisible):
            ag.relais_montre_refus_credit({"plafond_usd": 1.0})


# --- A2 ----------------------------------------------------------------------------------------------------------------

class TestA2(Base):
    def test_meme_modele_continue(self):
        m = self.montage()
        m.appeler("proposeur-espece-3", H.requete_proposeur(1, 0))
        self.assertEqual(m.appeler("proposeur-espece-3", H.requete_proposeur(1, 1))["issue_na"], "ok")

    def test_modele_servi_absent(self):
        m = self.montage(reglages={"ad_a": [{"modele_servi": None}]})
        with self.assertRaises(ag.ArretA2NA) as cm:
            m.appeler("proposeur-espece-3", H.requete_proposeur(1, 0))
        self.assertIn("absent", str(cm.exception))

    def test_modele_servi_change(self):
        m = self.montage(reglages={"ad_a": [{"modele_servi": "servi-un"}, {"modele_servi": "servi-deux"}]})
        m.appeler("proposeur-espece-3", H.requete_proposeur(1, 0))
        with self.assertRaises(ag.ArretA2NA):
            m.appeler("proposeur-espece-3", H.requete_proposeur(1, 1))

    def test_refus_de_transport_pour_un_autre_modele(self):
        r = {"statut": "refus", "texte_final": "", "refus": {"evenement": "assistant.model", "modele_servi": "autre"}}
        m = self.montage(reglages={"ad_a": [r]})
        with self.assertRaises(ag.ArretA2NA):
            m.appeler("proposeur-espece-3", H.requete_proposeur(1, 0))


# --- cumul, vol, exception, contexte ---------------------------------------------------------------------------------

class TestCumulEtContexte(Base):
    def test_cumul_partage_entre_generations(self):
        m1 = self.montage(generation=1)
        m1.cumul.ajouter("cle_d", 10_960_000)
        m1.appeler("proposeur-espece-2", H.requete_proposeur(1, 0))
        m2 = self.montage(generation=2, cumul=m1.cumul, journal_nom="journal-requetes-g2.jsonl")
        with self.assertRaises(rt.ArretPartCle):
            m2.appeler("proposeur-espece-2", H.requete_proposeur(2, 0))

    def test_exception_de_l_adaptateur_comptee_au_plafond(self):
        m = self.montage(reglages={"ad_a": [{"lever": True}]})
        with self.assertRaises(RuntimeError):
            m.appeler("proposeur-espece-3", H.requete_proposeur(1, 0))
        self.assertEqual(m.cumul.cumul("cle_a"), 6_050_000)
        self.assertEqual(m.cumul.en_vol("cle_a"), 0)

    def test_en_vol_compte_pendant_l_appel(self):
        m = self.montage()
        vu = []
        ad = m.ad["ad_a"]
        lancer = ad.lancer

        def lancer_et_voir(*a, **kw):
            vu.append(m.cumul.en_vol("cle_a"))
            return lancer(*a, **kw)

        ad.lancer = lancer_et_voir
        m.appeler("proposeur-espece-3", H.requete_proposeur(1, 0))
        self.assertEqual((vu, m.cumul.en_vol("cle_a")), ([6_050_000], 0))

    def test_en_vol_entre_dans_la_part(self):
        m = self.montage()
        jeton = m.cumul.ouvrir_vol("cle_d", 10_970_000)  # un appel en vol à ce pire : 10,97 + 6,05 > 17,01
        with self.assertRaises(rt.ArretPartCle) as cm:
            m.appeler("proposeur-espece-2", H.requete_proposeur(1, 0))
        self.assertEqual((cm.exception.en_vol_micro, cm.exception.cumul_micro), (10_970_000, 0))
        m.cumul.fermer_vol(jeton)
        self.assertEqual(m.appeler("proposeur-espece-2", H.requete_proposeur(1, 1))["issue_na"], "ok")

    def test_contexte_exige_et_refuse(self):
        m = self.montage()
        with self.assertRaises(ag.ContexteRefuse):
            H.GenerationEssai(m.ad, m.dossier)
        base = dict(numero_generation=1, table=m.table, parts=H.parts(m.table), pires_par_role=H.pires(m.table),
                    journal=m.journal, garde=m.garde, identifiant_case_de_session=H.case_de_session, cumul=m.cumul)
        ag.ContexteAppelGardeNA(**base)
        for changement in ({"numero_generation": 4}, {"portee_arret_1": "role"}, {"cumul": rt.CumulParCle(H.table(
                H.objet_table_sonde(), "ligne à part"))}, {"pires_par_role": {}}, {"garde": None},
                {"identifiant_case_de_session": None}):
            with self.assertRaises(ag.ContexteRefuse):
                ag.ContexteAppelGardeNA(**dict(base, **changement))

    def test_garde_d_une_autre_version_refusee(self):
        from pole import garde_motifs_na_v3 as gm3
        m = self.montage()
        n3 = gm3.Normaliseur(gm3.charger_donnees_ignorables(A.CHEMIN_DONNEES, A.EMPREINTE_DONNEES))
        garde_v3 = gm3.GardeMotifs(gm3.charger_liste_motifs(A.CHEMIN_LISTE_ESSAI, A.EMPREINTE_LISTE_ESSAI, n3))
        with self.assertRaises(ag.ContexteRefuse):
            ag.ContexteAppelGardeNA(numero_generation=1, table=m.table, parts=H.parts(m.table),
                                    pires_par_role=H.pires(m.table), journal=m.journal, garde=garde_v3,
                                    identifiant_case_de_session=H.case_de_session, cumul=m.cumul)


# --- composition avec la classe de génération v56 ----------------------------------------------------------------------

class TestCompositionV56(Base):
    """Le mélange devant la vraie classe de génération v56 (le lot 6 le placera devant `GenerationV68`, sa fille) : le refus
    ne touche ni le coffre réel, ni le suivi, ni A14 ; un appel permis passe par le noyau et le coffre réels."""

    def generation(self):
        import tempfile
        import aides_v56 as A56
        from pole import configuration_v56 as cfg
        from pole import course2_v56 as c2

        class GenerationNAEssai(ag.AppelGardeNA, c2.GenerationV56):
            pass

        d = tempfile.mkdtemp(prefix="essais-na-lot4-v56-")
        self.addCleanup(shutil.rmtree, d, True)
        conf = cfg.lire_configuration_v56(A56.configuration(d), base=d)
        m = self.montage()
        ads = dict(A56.adaptateurs())
        ads.update(m.ad)
        g = GenerationNAEssai(conf, os.path.join(d, "s"), ads, racine_sessions=os.path.join(d, "sessions"),
                              contexte_na=m.contexte)
        return g, m

    def test_refus_sans_trace_au_coffre_reel(self):
        g, m = self.generation()
        etat = m.etat()
        with self.assertRaises(rt.ArretPartCle):
            g.appel(etat, role="aiguilleur", role_kit="juge_ideation", fournisseur="ad_a", modele=H.MODELE_ESSAI,
                    consigne=H.requete_portier(1, 0), plafond_role="aiguilleur",
                    session=H.session_de(H.requete_portier(1, 0)))
        self.assertEqual(etat["cout"], 0.0)
        self.assertEqual([c for c in g.coffre.consommations() if c["role"] == "aiguilleur"], [])
        self.assertNotIn("aiguilleur", g.suivi.roles)
        self.assertEqual(g.suivi.depassements_a14(), {})

    def test_appel_permis_par_le_noyau_reel(self):
        g, m = self.generation()
        etat = m.etat()
        req = H.requete_proposeur(1, 0)
        a = g.appel(etat, role="proposeur-espece-3", role_kit="proposeur_ideation", fournisseur="ad_a",
                    modele=H.MODELE_ESSAI, consigne=req, plafond_role="proposeur", session=H.session_de(req))
        self.assertEqual(a["issue_na"], "ok")
        self.assertEqual(m.ad["ad_a"].recus[0]["consigne"].encode("utf-8"), req.octets)
        lignes = [c for c in g.coffre.consommations() if c["role"] == "proposeur-espece-3"]
        self.assertEqual(len(lignes), 1)
        self.assertEqual(m.cumul.cumul("cle_a"), 10_000)


if __name__ == "__main__":
    unittest.main()
