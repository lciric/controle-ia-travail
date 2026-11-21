"""Essais du lot 2 du véhicule NA-1 : `pole/garde_motifs_na_v1.py`.

Sur la liste d'essai (`liste-motifs-essai-na-v1.json`, deux familles, motifs inertes) : la liste réelle n'est pas de ce lot.
Arrêt n° 16 par famille, cas sain et artefact (R5) ; une requête assemblée qui passe ; une qui porte un motif, refusée au
dernier point avant l'envoi ; aucun octet changé après la garde. Données factices seules ; aucun réseau, aucune clé.
"""

import hashlib
import os
import sys
import unittest

ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(ICI)
for _p in (ICI, RACINE):
    if _p not in sys.path:
        sys.path.insert(0, _p)

import aides_na_v1 as A  # noqa: E402
from pole import garde_motifs_na_v1 as gm  # noqa: E402
from pole import identifiants_na_v1 as ident  # noqa: E402
from pole import tirage_na_v1 as tn  # noqa: E402

FAM1, FAM2 = gm.FAMILLES


class TestFormatDeLaListe(unittest.TestCase):

    def test_liste_d_essai_lue_a_son_empreinte(self):
        liste = A.liste_essai()
        self.assertEqual(liste.sha256, A.EMPREINTE_LISTE_ESSAI)
        self.assertEqual([nom for nom, _ in liste.familles], [FAM1, FAM2])
        self.assertEqual([len(m) for _, m in liste.familles], [3, 2])

    def test_empreinte_differente_refusee(self):
        with self.assertRaises(gm.ListeMotifsRefusee) as c:
            gm.charger_liste_motifs(A.CHEMIN_LISTE_ESSAI, "0" * 64)
        self.assertIn("empreinte", str(c.exception))

    def refus(self, familles=None, octets=None):
        if octets is None:
            octets, sha = A.liste_octets(familles)
        else:
            sha = hashlib.sha256(octets).hexdigest()
        with self.assertRaises(gm.ListeMotifsRefusee) as c:
            gm.lire_liste_motifs(octets, sha)
        return str(c.exception)

    def test_cas_sain_construit(self):
        octets, sha = A.liste_octets(A.familles_saines())
        self.assertEqual(len(list(gm.GardeMotifs(gm.lire_liste_motifs(octets, sha)).motifs())), 2)

    def test_deux_familles_dans_l_ordre(self):
        f = A.familles_saines()
        self.refus([f[0]])
        self.refus([f[1], f[0]])
        f[1]["nom"] = "autre famille"
        self.refus(f)

    def test_famille_vide_refusee(self):
        f = A.familles_saines()
        f[1]["motifs"] = []
        self.assertIn("vide", self.refus(f))

    def test_cles_en_plus_ou_en_double(self):
        f = A.familles_saines()
        f[0]["motifs"][0]["commentaire"] = "x"
        self.refus(f)
        octets, _ = A.liste_octets(A.familles_saines())
        double = octets.replace(b'"format": "liste-motifs-na-v1"',
                                b'"format": "liste-motifs-na-v1", "format": "liste-motifs-na-v1"', 1)
        self.assertIn("double", self.refus(octets=double))

    def test_rangs_sans_trou(self):
        f = A.familles_saines()
        f[0]["motifs"][0]["rang"] = 2
        self.refus(f)

    def test_type_motif_temoin(self):
        for cle, valeur in (("type", "autre"), ("motif", ""), ("temoin_positif", "")):
            f = A.familles_saines()
            f[0]["motifs"][0][cle] = valeur
            self.refus(f)

    def test_expression_invalide_ou_accord_vide(self):
        for motif in ("(", "a*", r"\b", "x?|"):
            f = A.familles_saines()
            f[0]["motifs"][0].update({"type": "expression_reguliere", "motif": motif, "temoin_positif": "aaa"})
            self.refus(f)

    def test_litteral_vide_apres_normalisation(self):
        f = A.familles_saines()
        f[0]["motifs"][0]["motif"] = "​­"
        self.assertIn("vide après normalisation", self.refus(f))

    def test_liste_illisible(self):
        self.refus(octets=b"\xff\xfe{")
        self.refus(octets=b"[]")


class TestNormalisation(unittest.TestCase):

    def test_formes_ramenees(self):
        self.assertEqual(gm.normaliser("ＧＲＡＩＮＥ ＦＡＣＴＩＣＥ"), "graine factice")
        self.assertEqual(gm.normaliser("Graine \t\n  Factice"), "graine factice")
        self.assertEqual(gm.normaliser("gra​ine­ fac﻿tice"), "graine factice")
        self.assertEqual(gm.normaliser("a–b—c−d‑e"), "a-b-c-d-e")
        self.assertEqual(gm.normaliser("STRASSE Straße"), "strasse strasse")

    def test_refuse_autre_chose_qu_une_chaine(self):
        with self.assertRaises(TypeError):
            gm.normaliser(b"octets")


class TestTemoinsPositifs(unittest.TestCase):

    def test_cas_sain_chaque_motif_mord_sur_son_temoin(self):
        garde = A.garde_essai()
        garde.verifier_temoins()
        for motif in garde.motifs():
            constat = garde.examiner(motif.temoin_positif)
            self.assertIsNotNone(constat)

    def test_un_motif_qui_ne_mord_pas_refuse_le_depart(self):
        f = A.familles_saines()
        f[1]["motifs"].append({"rang": 2, "type": "litteral", "motif": "tirage factice", "temoin_positif": "rien ici"})
        octets, sha = A.liste_octets(f)
        liste = gm.lire_liste_motifs(octets, sha)
        with self.assertRaises(gm.TemoinPositifManque) as c:
            gm.GardeMotifs(liste)
        self.assertEqual((c.exception.famille, c.exception.rang), (FAM2, 2))

    def test_temoins_rejoues_a_chaque_depart(self):
        garde = A.garde_essai()
        motif = next(iter(garde.motifs()))
        abime = gm.Motif(motif.famille, motif.rang, motif.type, motif.motif, "rien", motif._forme)
        garde.liste = gm.ListeMotifs(garde.liste.sha256, ((FAM1, (abime,)), garde.liste.familles[1]))
        with self.assertRaises(gm.TemoinPositifManque):
            garde.verifier_temoins()


class TestArret16ParFamille(unittest.TestCase):
    """Par famille : en clair, puis sous une forme que la normalisation ramène ; le refus nomme la famille et le rang."""

    @classmethod
    def setUpClass(cls):
        cls.garde = A.garde_essai()
        cls.sortie = A.sortie_factice()
        cls.saine = A.requete_factice(cls.sortie["generations"]["1"][0]["ligne"])

    def refus(self, octets):
        with self.assertRaises(gm.ArretMotifInterdit) as c:
            self.garde.garder_requete(octets)
        e = c.exception
        self.assertEqual(e.numero, 16)
        self.assertNotIn(e.texte_trouve, str(e))
        return e.famille, e.rang, e.texte_trouve

    def test_cas_sain_les_trente_trois_requetes_passent(self):
        for g in "123":
            for c in self.sortie["generations"][g]:
                rg = self.garde.garder_requete(A.requete_factice(c["ligne"]))
                self.assertEqual(rg.sha256, hashlib.sha256(rg.octets).hexdigest())
        self.garde.garder_texte(A.GABARIT_FACTICE.decode("utf-8"))
        self.garde.garder_texte(A.SYNTHESE_FACTICE.decode("utf-8"))

    def test_famille_identite_et_depot_en_clair(self):
        self.assertEqual(self.refus(self.saine + "Personne Factice Alpha.".encode())[:2], (FAM1, 1))
        self.assertEqual(self.refus(self.saine + b" 89abcdef0 ")[:2], (FAM1, 2))
        self.assertEqual(self.refus(self.saine + b" dossier-essai/fichier-factice.txt")[:2], (FAM1, 3))

    def test_famille_identite_et_depot_forme_ramenee(self):
        self.assertEqual(self.refus(self.saine + "PERSONNE fac​tice\n\talpha".encode())[:2], (FAM1, 1))
        self.assertEqual(self.refus(self.saine + "ＤＥＡＤＢＥＥＦ".encode())[:2], (FAM1, 2))
        self.assertEqual(self.refus(self.saine + "Dossier–Essai/Fichier‑Factice.TXT".encode())[:2], (FAM1, 3))

    def test_famille_composition_et_tenue_en_clair(self):
        self.assertEqual(self.refus(self.saine + b" graine factice ")[:2], (FAM2, 1))
        self.assertEqual(self.refus(self.saine + " tirage d'essai numéro trois".encode())[:2], (FAM2, 2))

    def test_famille_composition_et_tenue_forme_ramenee(self):
        self.assertEqual(self.refus(self.saine + "ＧＲＡＩＮＥ factice".encode())[:2], (FAM2, 1))
        self.assertEqual(self.refus(self.saine + "TIRAGE  d'essai\nNUMÉRO­ trois".encode())[:2], (FAM2, 2))

    def test_identifiants_reencodes_passent_et_le_jeton_du_noyau_mord(self):
        for octets in (bytes(6), b"\xff" * 6, b"\x12\x34\x56\x78\x9a\xbc"):
            self.assertIsNone(self.garde.examiner(ident.encoder_octets(octets)))
        self.assertEqual(self.refus(self.saine + b" f123456789abc")[:2], (FAM1, 2))


class TestDernierPointAvantEnvoi(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.garde = A.garde_essai()
        cls.sortie = A.sortie_factice()
        cls.saine = A.requete_factice(cls.sortie["generations"]["2"][3]["ligne"])

    def test_une_requete_assemblee_qui_passe(self):
        journal, envois = [], []
        rendu = gm.envoyer_apres_garde(self.garde, bytearray(self.saine), lambda o: (envois.append(o), "ok")[1],
                                       journal.append, {"role": "proposeur", "case": "factice"})
        self.assertEqual(rendu, "ok")
        self.assertEqual(len(envois), 1)
        self.assertIs(type(envois[0]), bytes)
        self.assertEqual(envois[0], self.saine)
        self.assertEqual(journal, [{"role": "proposeur", "case": "factice", "evenement": "envoi",
                                    "taille": len(self.saine), "sha256": hashlib.sha256(envois[0]).hexdigest()}])

    def test_une_requete_qui_porte_un_motif_refusee_avant_l_envoi(self):
        journal, envois = [], []
        porteuse = self.saine + b"\nune graine factice ici\n"
        with self.assertRaises(gm.ArretMotifInterdit) as c:
            gm.envoyer_apres_garde(self.garde, porteuse, envois.append, journal.append, {"role": "juge"})
        self.assertEqual(envois, [])
        self.assertEqual(journal, [{"role": "juge", "evenement": "non envoyé", "arret": 16, "famille": FAM2,
                                    "rang": 1, "texte_trouve": "graine factice"}])
        self.assertNotIn("graine factice", str(c.exception))

    def test_aucun_octet_change_apres_la_garde(self):
        tampon = bytearray(self.saine)
        rg = self.garde.garder_requete(tampon)
        tampon[0:5] = b"XXXXX"  # l'appelant change son tampon après la garde
        self.assertEqual(rg.octets, self.saine)
        self.assertEqual(rg.sha256, hashlib.sha256(self.saine).hexdigest())
        self.assertEqual(hashlib.sha256(rg.octets).hexdigest(), rg.sha256)
        with self.assertRaises(gm.EcartApresGarde):
            gm.verifier_avant_envoi(rg, bytes(tampon))
        gm.verifier_avant_envoi(rg, rg.octets)

    def test_ligne_de_journal_qui_ne_s_ecrit_pas_rien_ne_part(self):
        envois = []

        def journal_en_panne(_ligne):
            raise OSError("journal en lecture seule")

        with self.assertRaises(OSError):
            gm.envoyer_apres_garde(self.garde, self.saine, envois.append, journal_en_panne)
        self.assertEqual(envois, [])

    def test_requete_illisible_ou_qui_n_est_pas_en_octets(self):
        with self.assertRaises(gm.RequeteIllisible):
            self.garde.garder_requete(b"\xff\xfe requete")
        with self.assertRaises(TypeError):
            self.garde.garder_requete(self.saine.decode("utf-8"))


class TestEmpreinteDuProgramme(unittest.TestCase):

    def test_empreinte_du_programme(self):
        with open(gm.__file__, "rb") as f:
            self.assertEqual(gm.empreinte_programme(), hashlib.sha256(f.read()).hexdigest())


if __name__ == "__main__":
    unittest.main()
