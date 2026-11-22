"""Essais du lot 4 v2 du véhicule NA-1 — la surcharge d'`appel` v2 (`appel_garde_na_v2`) et la règle de repli, contre le
vrai `appel` du noyau (`OrchestreV56.appel`) et l'adaptateur direct au faux client de l'interface des messages.

Chaque garde : un cas sain et un artefact (R5). Données factices seules ; aucun appel, aucune clé, aucun réseau.
"""

import os
import sys
import unittest

ICI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ICI)

import aides_na_lot4_v1 as H1  # noqa: E402
import aides_na_lot4_v2 as H  # noqa: E402
from pole import adaptateur_claude_direct_na_v1 as ad  # noqa: E402
from pole import appel_garde_na_v2 as ag  # noqa: E402
from pole import journal_na_v3 as jn  # noqa: E402
from pole import routage_na_v1 as rt  # noqa: E402

P3 = "proposeur-espece-3"


class Base(unittest.TestCase):
    def montage(self, **kw):
        m = H.Montage(**kw)
        self.addCleanup(m.fermer)
        return m

    def modeles_recus(self, m, nom="ad_a"):
        return [c["model"] for c in m.client(nom).corps_recus]


# --- la règle de repli : cas sains ------------------------------------------------------------------------------------

class TestRepliCasSain(Base):
    def test_premier_repli_servi(self):
        m = self.montage(scripts={"ad_a": [H.refus("cyber"), H.reponse("Fiche factice inerte.")]})
        q = H1.requete_proposeur()
        a = m.appeler(P3, q)
        self.assertEqual(a["issue_na"], ag.ISSUE_SERVI_PAR_REPLI)
        self.assertTrue(a["par_repli"])
        self.assertEqual(a["attribution"], "servie par repli : " + H.REPLI_1)
        self.assertEqual(a["modele_servi_repli"], H.REPLI_1)
        self.assertEqual(a["lu"], "Fiche factice inerte.")
        self.assertEqual(self.modeles_recus(m), [H.MODELE_ROLE, H.REPLI_1])
        envois = m.envois()
        self.assertEqual(len(envois), 2)
        self.assertEqual({e["sha256"] for e in envois}, {q.sha256})
        self.assertEqual(envois[1]["rang"], envois[0]["rang"] + 1)
        self.assertEqual([t["issue"] for t in a["tentatives"]], ["refus de classifieur", ag.ISSUE_SERVI_PAR_REPLI])
        self.assertEqual([t["categorie"] for t in a["tentatives"]], ["cyber", None])
        self.assertEqual(m.gen.na_comptes["replis"][P3], {"chaînes ouvertes": 1, "servies par repli": 1})
        self.assertEqual(m.gen.na_journal_arrets_cles["tentatives_de_repli"], {"cle_a": 1})
        self.assertNotIn("cle", a["tentatives"][0])

    def test_meme_consigne_et_rien_d_autre_a_chaque_tentative(self):
        m = self.montage(scripts={"ad_a": [H.refus(), H.refus(), H.reponse()]})
        q = H1.requete_proposeur()
        m.appeler(P3, q)
        corps = m.client().corps_recus
        self.assertEqual(len(corps), 3)
        for c in corps:
            self.assertNotIn("system", c)
            self.assertEqual(len(c["messages"]), 1)
            self.assertEqual(c["messages"][0]["role"], "user")
            self.assertEqual(c["messages"][0]["content"].encode("utf-8"), q.octets)
            self.assertEqual(sorted(c), sorted(k for k in ad.CLES_CORPS if k in c))

    def test_second_repli_servi(self):
        m = self.montage(scripts={"ad_a": [H.refus(), H.refus("bio"), H.reponse()]})
        a = m.appeler(P3, H1.requete_proposeur())
        self.assertEqual(a["issue_na"], ag.ISSUE_SERVI_PAR_REPLI)
        self.assertEqual(a["modele_servi_repli"], H.REPLI_2)
        self.assertEqual(self.modeles_recus(m), [H.MODELE_ROLE, H.REPLI_1, H.REPLI_2])
        self.assertEqual([t["categorie"] for t in a["tentatives"]], [ad.CATEGORIE_NON_LUE, "bio", None])

    def test_premiere_tentative_ok_sans_repli(self):
        m = self.montage()
        a = m.appeler(P3, H1.requete_proposeur())
        self.assertEqual(a["issue_na"], ag.ISSUE_OK)
        self.assertFalse(a["par_repli"])
        self.assertEqual(a["attribution"], ag.ATTRIBUTION_ESPECE)
        self.assertEqual(len(m.client().corps_recus), 1)

    def test_reponses_brutes_une_par_tentative(self):
        m = self.montage(scripts={"ad_a": [H.refus(), H.refus(), H.reponse()]})
        a = m.appeler(P3, H1.requete_proposeur())
        self.assertEqual(len(m.fichiers_reponses()), 3)
        self.assertEqual(sorted(t["reponse_brute"] for t in a["tentatives"]), m.fichiers_reponses())

    def test_verdict_de_juge_servi_par_repli_vaut_verdict_du_role(self):
        m = self.montage(scripts={"ad_a": [H.refus(), H.reponse('{"verdict": "inerte"}')]})
        a = m.appeler("juge-espece-3", H1.requete_juge(), lire=lambda t: {"lu": t})
        self.assertEqual(a["issue_na"], ag.ISSUE_SERVI_PAR_REPLI)
        self.assertEqual(a["lu"], {"lu": '{"verdict": "inerte"}'})
        self.assertEqual(a["r"].modele_servi, H.REPLI_1)

    def test_le_role_garde_son_modele_apres_un_repli(self):
        m = self.montage(scripts={"ad_a": [H.refus(), H.reponse(), H.reponse()]})
        m.appeler(P3, H1.requete_proposeur(indice=0))
        a = m.appeler(P3, H1.requete_proposeur(indice=1))
        self.assertEqual(a["issue_na"], ag.ISSUE_OK)
        self.assertEqual(self.modeles_recus(m), [H.MODELE_ROLE, H.REPLI_1, H.MODELE_ROLE])
        self.assertEqual(m.gen.na_servis, {(P3, H.REPLI_1): H.REPLI_1, (P3, H.MODELE_ROLE): H.MODELE_ROLE})

    def test_repli_aux_lignes_a_part(self):
        """Sonde de refus (R11 de NO, P11) : la chaîne vaut à la ligne à part, à son plafond ; servie par repli, l'appel est
        marqué comme tel (l'espèce n'est pas dite acceptante : lecture du lot 6)."""
        from pole import requete_na_v3 as rq
        import aides_na_lot3_v3 as L3
        c = H1.cases()["reserve"]
        m = self.montage(objet=H1.objet_table_sonde(), marque="ligne à part", journal_nom="journal-sonde.jsonl",
                         scripts={"ad_a": [H.refus(), H.reponse()]})
        a = m.appeler("proposeur-espece-4", rq.assembler_sonde_refus(L3.gabarit(), c), fournisseur="ad_a")
        self.assertEqual(a["issue_na"], ag.ISSUE_SERVI_PAR_REPLI)
        self.assertTrue(a["par_repli"])
        self.assertEqual(sorted(m.cumul.etat()), ["sonde de refus"])
        self.assertEqual(self.modeles_recus(m), [H.MODELE_ROLE, H.REPLI_1])

    def test_ligne_a_part_plafond_par_tentative(self):
        from pole import requete_na_v3 as rq
        import aides_na_lot3_v3 as L3
        c = H1.cases()["reserve"]
        cumul = rt.CumulParCle(H1.table(H1.objet_table_sonde(), "ligne à part"))
        cumul.ajouter("sonde de refus", 1_000_000 - rt.micro_exact(H1.PIRE_LIGNE_A_PART))
        m = self.montage(objet=H1.objet_table_sonde(), marque="ligne à part", journal_nom="journal-sonde.jsonl",
                         cumul=cumul, scripts={"ad_a": [H.refus(), H.reponse()]})
        with self.assertRaises(rt.ArretPartCle):
            m.appeler("proposeur-espece-4", rq.assembler_sonde_refus(L3.gabarit(), c), fournisseur="ad_a")
        self.assertEqual(len(m.client().corps_recus), 1)

    def test_comptes_envois_et_mesure_replis(self):
        m = self.montage(scripts={"ad_a": [H.refus("cyber"), H.reponse()]})
        m.appeler(P3, H1.requete_proposeur())
        c = ag.comptes_envois_na(m.lignes())
        self.assertEqual(c["partis"], {P3: 2})
        mesure = ag.comptes_replis_na(m.gen.na_replis)
        self.assertEqual(sorted((x["modele_demande"], x["modele_servi"], x["categorie"], x["issue"]) for x in mesure),
                         sorted([(H.MODELE_ROLE, H.MODELE_ROLE, "cyber", "refus de classifieur"),
                          (H.REPLI_1, H.REPLI_1, "sans objet", ag.ISSUE_SERVI_PAR_REPLI)]))


# --- la règle de repli : artefacts ------------------------------------------------------------------------------------

class TestRepliArtefacts(Base):
    def test_trois_refus_levent_l_arret_1(self):
        m = self.montage(scripts={"ad_a": [H.refus("cyber"), H.refus(), H.refus("bio")]})
        a = m.appeler(P3, H1.requete_proposeur())
        self.assertEqual(a["issue_na"], ag.ISSUE_ARRET_1_APRES_REPLI)
        self.assertEqual(len(m.client().corps_recus), 3)
        self.assertEqual(m.gen.na_arrets_consignes[-1]["categories"], ["cyber", ad.CATEGORIE_NON_LUE, "bio"])
        self.assertEqual(m.gen.na_comptes["replis"][P3]["trois refus"], 1)
        self.assertEqual(m.gen.na_comptes["arrets_consignes"][P3], {"1": 1})

    def test_portee_course_apres_trois_refus_seulement(self):
        m = self.montage(portee_arret_1="course", scripts={"ad_a": [H.refus(), H.refus(), H.refus()]})
        with self.assertRaises(ag.ArretClassifieurNA):
            m.appeler(P3, H1.requete_proposeur())
        self.assertEqual(len(m.client().corps_recus), 3)

    def test_raison_inconnue_aucun_repli(self):
        for raison in ("pause_turn", "tool_use", None, "autre"):
            m = self.montage(scripts={"ad_a": [H.reponse(texte="x", raison=raison)]})
            a = m.appeler(P3, H1.requete_proposeur())
            self.assertEqual(a["issue_na"], ag.ISSUE_ILLISIBLE, raison)
            self.assertEqual(len(m.client().corps_recus), 1)

    def test_reponse_coupee_aucun_repli(self):
        m = self.montage(scripts={"ad_a": [H.reponse(raison="max_tokens")]})
        a = m.appeler(P3, H1.requete_proposeur())
        self.assertEqual(a["issue_na"], ag.ISSUE_ILLISIBLE)
        self.assertEqual(len(m.client().corps_recus), 1)

    def test_refus_en_prose_aucun_repli(self):
        m = self.montage(scripts={"ad_a": [H.reponse("Je ne réponds pas à cette demande.")]})
        a = m.appeler(P3, H1.requete_proposeur())
        self.assertEqual(a["issue_na"], ag.ISSUE_OK)
        self.assertEqual(len(m.client().corps_recus), 1)

    def test_refus_d_une_commande_externe_arret_1_sans_repli(self):
        m = self.montage(reglages={"ad_c1": [{"statut": "refus", "refus": {"evenement": "commande.refus"},
                                              "modele_servi": None}]})
        a = m.appeler("proposeur-espece-1", H1.requete_proposeur())
        self.assertEqual(a["issue_na"], ag.ISSUE_ARRET_1)
        self.assertEqual(len(m.ad["ad_c1"].recus), 1)

    def test_refus_hors_liste_reponse_illisible(self):
        m = self.montage(reglages={"ad_c1": [{"statut": "refus", "refus": {"evenement": "inconnu"},
                                              "modele_servi": None}]})
        a = m.appeler("proposeur-espece-1", H1.requete_proposeur())
        self.assertEqual(a["issue_na"], ag.ISSUE_ILLISIBLE)
        self.assertEqual(m.gen.na_comptes["cause_non_etablie"]["proposeur-espece-1"], {"refus hors liste": 1})
        self.assertNotIn("proposeur-espece-1", m.gen.na_comptes["arrets_consignes"])

    def test_reformulation_refusee(self):
        autre = H1.requete_proposeur(indice=1)

        class Reformule(H.GenerationEssai):
            def _requete_de_tentative_na(self, consigne, rang):
                return consigne if rang == 1 else autre

        m = self.montage(classe=Reformule, scripts={"ad_a": [H.refus(), H.reponse()]})
        with self.assertRaises(ag.ArretRequeteJournaliseeNA) as c:
            m.appeler(P3, H1.requete_proposeur())
        self.assertEqual(c.exception.cause, "reformulation")
        self.assertEqual(len(m.client().corps_recus), 1)

    def test_egalite_repassee_a_chaque_tentative(self):
        class Ecart(H.GenerationEssai):
            n = 0

            def _chaine_pour_noyau_na(self, envoi):
                Ecart.n += 1
                s = super()._chaine_pour_noyau_na(envoi)
                return s if Ecart.n == 1 else s + " "

        m = self.montage(classe=Ecart, scripts={"ad_a": [H.refus(), H.reponse()]})
        with self.assertRaises(ag.ArretRequeteJournaliseeNA) as c:
            m.appeler(P3, H1.requete_proposeur())
        self.assertEqual(c.exception.cause, "égalité")
        dernier = m.lignes()[-1]
        self.assertTrue(dernier["cause"].endswith(f"de rang {m.envois()[1]['rang']}"))
        self.assertEqual(len(m.client().corps_recus), 1)

    def test_part_repassee_par_tentative(self):
        t = H1.table()
        cumul = rt.CumulParCle(t)
        part = t.cles["cle_a"].part_micro
        cumul.ajouter("cle_a", part - rt.micro_exact(H1.PIRE_PROPOSEUR))  # la première tentative tient, juste ; pas la seconde
        m = self.montage(cumul=cumul, scripts={"ad_a": [H.refus(usage={"input_tokens": 1000, "output_tokens": 0}),
                                                        H.reponse()]})
        with self.assertRaises(rt.ArretPartCle) as c:
            m.appeler(P3, H1.requete_proposeur())
        self.assertEqual(c.exception.clause, rt.CLAUSE_PART)
        self.assertEqual(len(m.client().corps_recus), 1)
        self.assertEqual(m.lignes()[-1]["evenement"], "non envoyé")
        self.assertEqual(m.gen.na_replis[-1]["issue"], "arrêt n° 12")

    def test_pire_de_la_tentative_lu_par_modele(self):
        pires = H.pires_repli(H1.table())
        pires[P3][H.REPLI_1] = 7.5
        t = H1.table()
        cumul = rt.CumulParCle(t)
        cumul.ajouter("cle_a", t.cles["cle_a"].part_micro - rt.micro_exact(7.0))
        m = self.montage(cumul=cumul, pires_repli_=pires,
                         scripts={"ad_a": [H.refus(usage={"input_tokens": 0, "output_tokens": 0}), H.reponse()]})
        with self.assertRaises(rt.ArretPartCle):
            m.appeler(P3, H1.requete_proposeur())
        self.assertEqual(self.modeles_recus(m), [H.MODELE_ROLE])

    def test_reservation_impossible_arrete_la_chaine(self):
        m = self.montage(scripts={"ad_a": [H.refus(usage=None), H.reponse()]})
        a = m.appeler(P3, H1.requete_proposeur(), etat=m.etat(reste=0.5))
        self.assertIsNone(a)
        self.assertTrue(m.dernier_etat["coupee"])
        self.assertEqual(len(m.client().corps_recus), 1)
        self.assertEqual(m.lignes()[-1]["evenement"], "non lancé")
        self.assertEqual(m.gen.na_comptes["replis"][P3]["arrêtées en repli : non lancé"], 1)

    def test_credit_en_repli_leve_13_sans_second_repli(self):
        m = self.montage(scripts={"ad_a": [H.refus(), H.credit_amont(), H.reponse()]})
        with self.assertRaises(ag.ArretCreditNA) as c:
            m.appeler(P3, H1.requete_proposeur())
        self.assertEqual(c.exception.cle, "cle_a")
        self.assertEqual(len(m.client().corps_recus), 2)

    def test_erreur_en_repli_cause_non_etablie(self):
        m = self.montage(scripts={"ad_a": [H.refus(), H.surcharge(), H.reponse()]})
        a = m.appeler(P3, H1.requete_proposeur())
        self.assertEqual(a["issue_na"], ag.ISSUE_ILLISIBLE)
        self.assertTrue(a["en_repli"])
        self.assertEqual(len(m.client().corps_recus), 2)
        self.assertEqual(m.gen.na_comptes["cause_non_etablie"][P3], {"en repli": 1})

    def test_reponse_coupee_en_repli_est_servie(self):
        m = self.montage(scripts={"ad_a": [H.refus(), H.reponse(raison="max_tokens")]})
        a = m.appeler(P3, H1.requete_proposeur())
        self.assertEqual(a["issue_na"], ag.ISSUE_SERVI_PAR_REPLI)
        self.assertEqual(a["classe_tentative_servie"], "réponse illisible")
        self.assertIsNone(a["lu"])

    def test_role_arrete_en_chaine(self):
        class Arrete(H.GenerationEssai):
            vus = 0

            def role_arrete_na(self, role):
                Arrete.vus += 1
                return None if Arrete.vus == 1 else "A3 : arrêt factice"

        m = self.montage(classe=Arrete, scripts={"ad_a": [H.refus(), H.reponse()]})
        a = m.appeler(P3, H1.requete_proposeur())
        self.assertEqual(a["issue_na"], ag.ISSUE_REFUS_ECRIT)
        self.assertEqual(len(m.client().corps_recus), 1)
        self.assertEqual(a["tentatives"][-1]["issue"], "refus écrit en chaîne")

    def test_journal_en_panne_en_repli(self):
        m = self.montage(scripts={"ad_a": [H.refus(), H.reponse()]})
        orig = m.journal.journaliser_envoi
        appels = []

        def panne(*a, **kw):
            appels.append(1)
            if len(appels) == 2:
                raise OSError("panne factice")
            return orig(*a, **kw)

        m.journal.journaliser_envoi = panne
        with self.assertRaises(ag.ArretRequeteJournaliseeNA):
            m.appeler(P3, H1.requete_proposeur())
        self.assertEqual(len(m.client().corps_recus), 1)


# --- coût par tentative (A3) ------------------------------------------------------------------------------------------

class TestCout(Base):
    def test_refus_avec_usage_compte_par_son_usage(self):
        m = self.montage(scripts={"ad_a": [H.refus(usage={"input_tokens": 1000, "output_tokens": 0}), H.reponse()]})
        a = m.appeler(P3, H1.requete_proposeur())
        attendu = rt.micro_cout(1000 * 4.0 / 1e6)
        self.assertEqual(a["tentatives"][0]["cout_micro"], attendu)
        self.assertFalse(a["tentatives"][0]["cout_inconnu"])
        self.assertEqual(rt.micro_exact(m.cumul.etat()["cle_a"]),
                         attendu + rt.micro_cout(1000 * 5.0 / 1e6 + 500 * 25.0 / 1e6))

    def test_refus_sans_usage_compte_au_pire_jamais_a_zero(self):
        m = self.montage(scripts={"ad_a": [H.refus(usage=None), H.reponse()]})
        etat = m.etat(reste=50.0)
        a = m.appeler(P3, H1.requete_proposeur(), etat=etat)
        t0 = a["tentatives"][0]
        self.assertTrue(t0["cout_inconnu"])
        self.assertGreaterEqual(t0["cout_micro"], rt.micro_exact(H1.PIRE_PROPOSEUR))
        self.assertGreater(t0["cout_micro"], 0)

    def test_cout_inconnu_sous_le_pire_releve_au_pire(self):
        """Le noyau compte le plafond de la tentative (borné au reste) ; le cumul de la clé prend le pire s'il est plus haut."""
        m = self.montage(scripts={"ad_a": [H.refus(usage=None), H.reponse()]})
        a = m.appeler(P3, H1.requete_proposeur(), etat=m.etat(reste=1.0))
        self.assertIsNone(a)
        self.assertEqual(rt.micro_exact(m.cumul.etat()["cle_a"]), rt.micro_exact(H1.PIRE_PROPOSEUR))

    def test_erreur_de_statut_sans_cout(self):
        m = self.montage(scripts={"ad_a": [H.surcharge()]})
        m.appeler(P3, H1.requete_proposeur())
        self.assertEqual(m.cumul.etat()["cle_a"], "0.000000")


# --- n° 31 (A2) -------------------------------------------------------------------------------------------------------

class TestArret31(Base):
    def test_numero(self):
        self.assertEqual(ag.ArretA2NA.numero, 31)
        self.assertEqual(ag.PireManquantNA.numero, 34)

    def test_modele_servi_autre_au_repli(self):
        m = self.montage(scripts={"ad_a": [H.refus(), H.reponse(modele=H.REPLI_2)]})
        with self.assertRaises(ag.ArretA2NA):
            m.appeler(P3, H1.requete_proposeur())

    def test_modele_servi_autre_au_premier(self):
        m = self.montage(scripts={"ad_a": [H.reponse(modele="modele-autre-essai")]})
        with self.assertRaises(ag.ArretA2NA):
            m.appeler(P3, H1.requete_proposeur())

    def test_date_stricte_admise(self):
        m = self.montage(scripts={"ad_a": [H.reponse(modele=H.MODELE_ROLE + "-20261001")]})
        self.assertEqual(m.appeler(P3, H1.requete_proposeur())["issue_na"], ag.ISSUE_OK)

    def test_modele_servi_absent(self):
        m = self.montage(scripts={"ad_a": [H.reponse(modele=None)]})
        with self.assertRaises(ag.ArretA2NA) as c:
            m.appeler(P3, H1.requete_proposeur())
        self.assertIn("absent", c.exception.cause)

    def test_modele_servi_autre_sur_un_refus(self):
        m = self.montage(scripts={"ad_a": [H.reponse(raison="max_tokens", modele="modele-autre-essai")]})
        with self.assertRaises(ag.ArretA2NA):
            m.appeler(P3, H1.requete_proposeur())

    def test_trace_de_repli_du_fournisseur(self):
        for r in (H.reponse(blocs_en_plus=[{"type": "fallback", "from": {}, "to": {}}]),
                  H.reponse(iterations=[{"type": "fallback_message"}])):
            m = self.montage(scripts={"ad_a": [r]})
            with self.assertRaises(ag.ArretA2NA):
                m.appeler(P3, H1.requete_proposeur())
            self.assertEqual(len(m.client().corps_recus), 1)

    def test_modele_refuse_par_le_relais(self):
        m = self.montage(scripts={"ad_a": [H.refus(), H.modele_refuse_relais()]})
        with self.assertRaises(ag.ArretA2NA):
            m.appeler(P3, H1.requete_proposeur())

    def test_modele_demande_autre_que_celui_du_role(self):
        m = self.montage()
        with self.assertRaises(ag.ArretA2NA):
            m.appeler(P3, H1.requete_proposeur(), modele=H.REPLI_1)
        self.assertEqual(m.client().corps_recus, [])
        self.assertEqual(m.lignes()[-1]["evenement"], "non envoyé")

    def test_changement_au_meme_modele_demande(self):
        m = self.montage(scripts={"ad_a": [H.reponse(), H.reponse(modele=H.MODELE_ROLE + "-20261001")]})
        m.appeler(P3, H1.requete_proposeur(indice=0))
        with self.assertRaises(ag.ArretA2NA):
            m.appeler(P3, H1.requete_proposeur(indice=1))


# --- n° 13 (N2) -------------------------------------------------------------------------------------------------------

class TestArret13(Base):
    def test_cas_sain(self):
        self.assertEqual(self.montage().appeler(P3, H1.requete_proposeur())["issue_na"], ag.ISSUE_OK)

    def test_credit_d_amont(self):
        m = self.montage(scripts={"ad_a": [H.credit_amont()]})
        with self.assertRaises(ag.ArretCreditNA) as c:
            m.appeler(P3, H1.requete_proposeur())
        self.assertEqual(c.exception.lu_par, ad.ERREUR_CREDIT_AMONT)

    def test_plafond_du_relais(self):
        m = self.montage(scripts={"ad_a": [H.plafond_relais()]})
        with self.assertRaises(ag.ArretCreditNA):
            m.appeler(P3, H1.requete_proposeur())

    def test_acces_refuse_n_est_pas_13(self):
        m = self.montage(scripts={"ad_a": [H.acces_refuse()]})
        a = m.appeler(P3, H1.requete_proposeur())
        self.assertEqual(a["issue_na"], ag.ISSUE_ILLISIBLE)
        self.assertEqual(m.gen.na_journal_arrets_cles["cause_non_etablie"], {"cle_a": 1})

    def test_402_sans_type_de_facturation_n_est_pas_13(self):
        m = self.montage(scripts={"ad_a": [H.FauxErreurStatut(402, {"type": "error", "error": {"type": "autre"}}, "autre")]})
        self.assertEqual(m.appeler(P3, H1.requete_proposeur())["issue_na"], ag.ISSUE_ILLISIBLE)

    def test_relais_de_protocole(self):
        m = self.montage(reglages={"ad_d": [{"statut": "budget_depasse", "modele_servi": None}]})
        with self.assertRaises(ag.ArretCreditNA):
            m.appeler("proposeur-espece-2", H1.requete_proposeur())


# --- gardes de la v1, tenues -----------------------------------------------------------------------------------------

class TestGardesV1(Base):
    def test_motif_au_point_d_envoi(self):
        m = self.montage()
        q = H1.requete_proposeur(synthese_octets=H1.A.SYNTHESE_FACTICE + "la graine factice\n".encode())
        with self.assertRaises(ag.ArretMotifNA) as c:
            m.appeler(P3, q)
        self.assertEqual((c.exception.numero, c.exception.rang), (16, 1))
        self.assertEqual(m.client().corps_recus, [])
        self.assertEqual(m.lignes()[-1]["evenement"], "non envoyé")

    def test_routage_par_role(self):
        m = self.montage()
        with self.assertRaises(rt.ArretPartCle):
            m.appeler(P3, H1.requete_proposeur(), fournisseur="ad_b")
        self.assertEqual(m.client("ad_b").corps_recus, [])

    def test_refus_ecrit_au_pas_0(self):
        class Arrete(H.GenerationEssai):
            def role_arrete_na(self, role):
                return "A3 : arrêt factice"

        m = self.montage(classe=Arrete)
        a = m.appeler(P3, H1.requete_proposeur())
        self.assertEqual(a["issue_na"], ag.ISSUE_REFUS_ECRIT)
        self.assertEqual(m.client().corps_recus, [])

    def test_hors_course(self):
        m = self.montage()
        with self.assertRaises(rt.ArretPartCle):
            m.appeler("lecteur-etiquettes-1", H1.requete_juge(), fournisseur="hors_course")

    def test_commande_externe_ok_sans_repli(self):
        m = self.montage()
        a = m.appeler("proposeur-espece-1", H1.requete_proposeur())
        self.assertEqual(a["issue_na"], ag.ISSUE_OK)
        self.assertEqual(len(a["tentatives"]), 1)


# --- le contexte (n° 34, D-N1) ----------------------------------------------------------------------------------------

class TestContexte(Base):
    def test_cas_sain(self):
        self.assertIsInstance(self.montage().contexte, ag.ContexteAppelGardeNA)

    def test_pire_de_repli_manquant(self):
        p = H.pires_repli(H1.table())
        del p[P3][H.REPLI_2]
        with self.assertRaises(ag.PireManquantNA):
            self.montage(pires_repli_=p)

    def test_role_claude_sans_pire_de_repli(self):
        p = H.pires_repli(H1.table())
        del p["aiguilleur"]
        with self.assertRaises(ag.PireManquantNA):
            self.montage(pires_repli_=p)

    def test_pire_de_repli_nul(self):
        p = H.pires_repli(H1.table())
        p[P3][H.REPLI_1] = 0
        with self.assertRaises(ag.PireManquantNA):
            self.montage(pires_repli_=p)

    def test_modeles_repli_sans_leur_forme(self):
        for mr in ((H.REPLI_1,), (H.REPLI_1, H.REPLI_1), [H.REPLI_1, H.REPLI_2], (H.MODELE_ROLE, H.REPLI_1)):
            pires = {r: {m: H1.pires(H1.table())[r] for m in mr} for r in H.roles_claude(H1.table())}
            with self.assertRaises(ag.ContexteRefuse, msg=repr(mr)):
                self.montage(modeles_repli=mr, pires_repli_=pires)
        with self.assertRaises(ag.ContexteRefuse) as c:
            self.montage(modeles_repli=(H.MODELE_ROLE, H.REPLI_1),
                         pires_repli_={r: {H.MODELE_ROLE: 1.0, H.REPLI_1: 1.0} for r in H.roles_claude(H1.table())})
        self.assertNotIsInstance(c.exception, ag.PireManquantNA)

    def test_adaptateur_non_direct_sur_une_cle_claude(self):
        with self.assertRaises(ag.ContexteRefuse):
            self.montage(adaptateurs_en_plus={"ad_a": H1.AdaptateurEnregistreur()})

    def test_adaptateur_direct_sans_les_modeles_de_repli(self):
        m = H.Montage()
        self.addCleanup(m.fermer)
        etroit = H.adaptateur_direct(m.reponses, modeles_admis=(H.MODELE_ROLE, H.REPLI_1),
                                     reglages={r: {k: v for k, v in d.items() if k != H.REPLI_2}
                                               for r, d in H.reglages_essai().items()})
        with self.assertRaises(ag.ContexteRefuse):
            self.montage(adaptateurs_en_plus={"ad_a": etroit})


if __name__ == "__main__":
    unittest.main()
