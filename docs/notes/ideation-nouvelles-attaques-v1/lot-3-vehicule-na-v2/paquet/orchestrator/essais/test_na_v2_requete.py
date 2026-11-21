"""Essais du lot 3 du véhicule NA-1 : `pole/requete_na_v2.py`.

v2 (remplace `test_na_v1_requete`, `cbc8df87…`, archivé sans modification) : des noms seuls changent, pour la v3 du lot 2 ;
aucun essai n'est ajouté, retiré ni changé.

Partie servie à l'octet ; enveloppe sans ajout (D2) ; dernier octet de chaque pièce gardé, empreinte sur la pièce entière ;
forme de la fiche servie au portier et aux juges, égale à l'octet à celle du noyau ; arrêt n° 8 (mesure de la taille),
cas sain et artefact (R5). Données factices seules ; aucun réseau, aucune clé.
"""

import hashlib
import json
import os
import sys
import tempfile
import unittest
from unittest import mock

ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(ICI)
for _p in (ICI, RACINE):
    if _p not in sys.path:
        sys.path.insert(0, _p)

import aides_na_lot3_v2 as B  # noqa: E402
import aides_na_v3 as A  # noqa: E402
from pole import fiches_v54 as fv54  # noqa: E402  (témoin : la forme du noyau)
from pole import garde_motifs_na_v3 as gm  # noqa: E402
from pole import identifiants_na_v1 as ident  # noqa: E402
from pole import requete_na_v2 as rq  # noqa: E402


def sha(o):
    return hashlib.sha256(o).hexdigest()


class TestGabarit(unittest.TestCase):

    def test_gabarit_factice_lu_a_son_empreinte(self):
        g = B.gabarit()
        self.assertEqual(g.sha256, A.EMPREINTE_GABARIT_FACTICE)
        self.assertEqual(g.octets, A.GABARIT_FACTICE)

    def test_empreinte_differente_refusee_en_nommant_la_piece(self):
        with self.assertRaises(rq.EmpreintePieceDifferente) as c:
            rq.charger_gabarit(A.GABARIT_FACTICE)  # empreinte par défaut : celle du gabarit servi
        self.assertEqual(c.exception.numero, 14)
        self.assertIn("partie servie", str(c.exception))
        with self.assertRaises(rq.EmpreintePieceDifferente):
            rq.charger_gabarit(A.GABARIT_FACTICE + b"x", A.EMPREINTE_GABARIT_FACTICE)

    def test_question_refusee_par_son_nom_avant_toute_ouverture(self):
        absent = os.path.join(tempfile.mkdtemp(), "question-course-nouvelles-attaques-v5.md")
        self.assertFalse(os.path.exists(absent))
        with self.assertRaises(rq.QuestionRefusee):
            rq.lire_gabarit(absent, A.EMPREINTE_GABARIT_FACTICE)  # refus par le nom : le fichier n'est jamais ouvert
        with self.assertRaises(rq.QuestionRefusee):
            rq.lire_piece("pièce", absent, "0" * 64)
        with self.assertRaises(rq.QuestionRefusee):
            rq.charger_gabarit(A.GABARIT_FACTICE, A.EMPREINTE_GABARIT_FACTICE, nom_fichier=absent)

    def test_question_refusee_par_son_empreinte(self):
        with mock.patch.object(rq, "EMPREINTES_QUESTION", (A.EMPREINTE_GABARIT_FACTICE,)):
            with self.assertRaises(rq.QuestionRefusee):
                rq.charger_gabarit(A.GABARIT_FACTICE, A.EMPREINTE_GABARIT_FACTICE)
            d = tempfile.mkdtemp()
            chemin = os.path.join(d, "gabarit-factice.md")
            with open(chemin, "wb") as f:
                f.write(A.GABARIT_FACTICE)
            with self.assertRaises(rq.QuestionRefusee):
                rq.lire_piece("pièce", chemin, A.EMPREINTE_GABARIT_FACTICE)

    def test_lire_gabarit_sur_le_disque(self):
        d = tempfile.mkdtemp()
        chemin = os.path.join(d, "gabarit-factice.md")
        with open(chemin, "wb") as f:
            f.write(A.GABARIT_FACTICE)
        self.assertEqual(rq.lire_gabarit(chemin, A.EMPREINTE_GABARIT_FACTICE).octets, A.GABARIT_FACTICE)

    def refus_emplacement(self, octets):
        with self.assertRaises(rq.EmplacementRefuse):
            rq.charger_gabarit(octets, sha(octets))

    def test_zero_emplacement_refuse(self):
        self.refus_emplacement(A.GABARIT_FACTICE.replace(b"{{CASE}}\n", b""))

    def test_deux_emplacements_refuses(self):
        self.refus_emplacement(A.GABARIT_FACTICE + b"{{CASE}}\n")

    def test_emplacement_hors_d_une_ligne_propre_refuse(self):
        self.refus_emplacement(A.GABARIT_FACTICE.replace(b"{{CASE}}\n", b"x {{CASE}}\n"))
        self.refus_emplacement(A.GABARIT_FACTICE.replace(b"{{CASE}}\n", b"{{CASE}} x\n"))


class TestPartieServie(unittest.TestCase):

    def test_partie_servie_a_l_octet(self):
        g, c = B.gabarit(), B.cases()["1"][0]
        p = rq.remplir_partie_servie(g, c)
        i = A.GABARIT_FACTICE.index(b"{{CASE}}")
        ligne = c.ligne.encode("utf-8")
        self.assertEqual(p.octets[:i], A.GABARIT_FACTICE[:i])
        self.assertEqual(p.octets[i:i + len(ligne)], ligne)
        self.assertEqual(p.octets[i + len(ligne):], A.GABARIT_FACTICE[i + len(b"{{CASE}}"):])
        self.assertEqual(p.octets, A.GABARIT_FACTICE.replace(b"{{CASE}}", ligne))
        self.assertEqual(p.octets[-1:], b"\n")  # le dernier octet du gabarit est gardé
        self.assertEqual(p.sha256, sha(p.octets))

    def test_trente_quatre_cases_toutes_remplies(self):
        cs = B.cases()
        toutes = [c for g in ("1", "2", "3") for c in cs[g]] + [cs["reserve"]]
        self.assertEqual(len(toutes), 34)
        for c in toutes:
            self.assertNotIn(b"{{CASE}}", rq.remplir_partie_servie(B.gabarit(), c).octets)

    def test_ligne_de_case_qui_differe_d_un_octet_refusee(self):
        c = B.cases()["1"][0]
        fausse = rq.CaseServie(c.triplet, c.identifiant, c.ligne[:-1] + chr(ord(c.ligne[-1]) ^ 1))
        with self.assertRaises(rq.tn.LigneDeCaseRefusee):
            rq.remplir_partie_servie(B.gabarit(), fausse)

    def test_ligne_qui_n_est_pas_celle_de_son_identifiant_refusee(self):
        cs = B.cases()["1"]
        melee = rq.CaseServie(cs[0].triplet, cs[1].identifiant, cs[0].ligne)
        with self.assertRaises(rq.RequeteRefusee):
            rq.remplir_partie_servie(B.gabarit(), melee)

    def test_tirage_d_un_autre_gabarit_refuse(self):
        sortie = A.sortie_factice()
        sortie["gabarit_sha256"] = "0" * 64
        with self.assertRaises(rq.RequeteRefusee):
            rq.cases_du_tirage(sortie, B.gabarit())

    def test_legende_du_tirage_differente_refusee(self):
        sortie = A.sortie_factice()
        sortie["legende"]["valeurs"][0][0] = "trait factice autre"
        with self.assertRaises(rq.RequeteRefusee):
            rq.cases_du_tirage(sortie, B.gabarit())

    def test_lignes_du_tirage_controlees(self):
        sortie = A.sortie_factice()
        sortie["generations"]["2"][3]["ligne"] += " "
        with self.assertRaises(rq.tn.LigneDeCaseRefusee):
            rq.cases_du_tirage(sortie, B.gabarit())


class TestEnveloppeSansAjout(unittest.TestCase):

    def setUp(self):
        self.g = B.gabarit()
        self.cs = B.cases()
        self.s = B.synthese()

    def test_proposeur_generation_1_exacte(self):
        c = self.cs["1"][0]
        r = rq.assembler_proposeur(self.g, c, self.s, 1)
        partie = rq.remplir_partie_servie(self.g, c).octets
        self.assertEqual(r.octets, partie + b"\n" + A.SYNTHESE_FACTICE)
        self.assertEqual([e.nom for e in r.composition], ["partie servie remplie", "séparateur", "synthèse servie"])
        self.assertEqual((r.sorte, r.generation, r.identifiant_case, r.registre), ("proposeur", 1, c.identifiant,
                                                                                  rq.REGISTRE_SANS_OBJET))

    def test_proposeur_generation_2_avec_registre(self):
        c = self.cs["2"][0]
        r = B.requete_generation_2()
        partie = rq.remplir_partie_servie(self.g, c).octets
        attendu = (partie + b"\n" + A.SYNTHESE_FACTICE + b"\n" + B.TITRE_REGISTRE_FACTICE.encode("utf-8") + b"\n"
                   + B.REGISTRE_FACTICE)
        self.assertEqual(r.octets, attendu)
        self.assertEqual(r.registre, rq.REGISTRE_SERVI)

    def test_registre_vide_section_omise(self):
        c = self.cs["3"][0]
        vide = B.registre(b"")
        r3 = rq.assembler_proposeur(self.g, c, self.s, 3, vide, B.TITRE_REGISTRE_FACTICE)
        r1 = rq.assembler_proposeur(self.g, c, self.s, 1)
        self.assertEqual(r3.octets, r1.octets)
        self.assertEqual(r3.registre, rq.REGISTRE_OMIS)
        self.assertEqual(r3.generation, 3)

    def test_registre_hors_de_sa_generation_refuse(self):
        c = self.cs["1"][0]
        with self.assertRaises(rq.RequeteRefusee):
            rq.assembler_proposeur(self.g, c, self.s, 1, B.registre(), B.TITRE_REGISTRE_FACTICE)
        with self.assertRaises(rq.RequeteRefusee):
            rq.assembler_proposeur(self.g, c, self.s, 2)
        with self.assertRaises(rq.RequeteRefusee):
            rq.assembler_proposeur(self.g, c, self.s, 2, B.REGISTRE_FACTICE, B.TITRE_REGISTRE_FACTICE)
        for g in (0, 4, "1", True, None):
            with self.assertRaises(rq.RequeteRefusee):
                rq.assembler_proposeur(self.g, c, self.s, g)

    def test_titre_du_registre_sur_une_ligne(self):
        c = self.cs["2"][0]
        for titre in (None, "", "titre\nsur deux lignes", "titre\r", " titre", "titre "):
            with self.assertRaises(rq.RequeteRefusee):
                rq.assembler_proposeur(self.g, c, self.s, 2, B.registre(), titre)

    def test_sonde_de_refus_partie_servie_seule(self):
        c = self.cs["reserve"]
        r = rq.assembler_sonde_refus(self.g, c)
        self.assertEqual(r.octets, rq.remplir_partie_servie(self.g, c).octets)
        self.assertEqual(len(r.composition), 1)
        self.assertIsNone(r.generation)

    def test_aucun_texte_du_noyau_ni_de_role(self):
        for r in (rq.assembler_proposeur(self.g, self.cs["1"][0], self.s, 1), B.requete_generation_2(),
                  rq.assembler_sonde_refus(self.g, self.cs["reserve"])):
            for fragment in (b"## Case", b"Texte : ", b" ; bras : ", b"{fiches}", b"{notes}", b"bloc JSON",
                             b"## La fiche"):
                self.assertNotIn(fragment, r.octets)
            seps = [r.octets[e.debut:e.debut + e.taille] for e in r.composition if e.sorte == "separateur"]
            self.assertTrue(all(s == b"\n" for s in seps))
            self.assertTrue(all(e.sorte in ("piece", "separateur", "titre") for e in r.composition))

    def test_la_composition_recouvre_la_requete(self):
        r = B.requete_generation_2()
        self.assertEqual(b"".join(r.octets[e.debut:e.debut + e.taille] for e in r.composition), r.octets)
        self.assertEqual(sum(e.taille for e in r.composition), r.taille)

    def test_composition_fausse_refusee(self):
        r = B.requete_generation_2()
        e0 = r.composition[0]
        faux = rq.Element(e0.nom, e0.sorte, e0.debut, e0.taille, "0" * 64, e0.piece_sha256, e0.piece_taille)
        with self.assertRaises(rq.RequeteRefusee):
            rq.RequeteAssemblee(r.sorte, r.generation, r.identifiant_case, r.octets, r.sha256, r.taille,
                                (faux,) + r.composition[1:], r.registre)
        with self.assertRaises(rq.RequeteRefusee):
            rq.RequeteAssemblee(r.sorte, r.generation, r.identifiant_case, r.octets + b"x", sha(r.octets + b"x"),
                                r.taille + 1, r.composition, r.registre)
        k = [i for i, e in enumerate(r.composition) if e.sorte == "titre"][0]
        t = r.composition[k]
        titre_faux = rq.Element(t.nom, t.sorte, t.debut, t.taille, "0" * 64)
        with self.assertRaises(rq.RequeteRefusee):  # un morceau qui n'est pas une pièce, à une autre empreinte
            rq.RequeteAssemblee(r.sorte, r.generation, r.identifiant_case, r.octets, r.sha256, r.taille,
                                r.composition[:k] + (titre_faux,) + r.composition[k + 1:], r.registre)
        partielle = rq.Element(e0.nom, e0.sorte, e0.debut, e0.taille, e0.sha256, "0" * 64, e0.piece_taille + 1)
        with self.assertRaises(rq.RequeteRefusee):  # une pièce servie en partie : refusée
            rq.RequeteAssemblee(r.sorte, r.generation, r.identifiant_case, r.octets, r.sha256, r.taille,
                                (partielle,) + r.composition[1:], r.registre)
        sep = r.composition[1]
        double = rq.Element(sep.nom, sep.sorte, sep.debut, 2, sha(b"\n\n"))
        octets = r.octets[:sep.debut] + b"\n" + r.octets[sep.debut:]
        reste = tuple(rq.Element(e.nom, e.sorte, e.debut + 1, e.taille, e.sha256, e.piece_sha256, e.piece_taille)
                      for e in r.composition[2:])
        with self.assertRaises(rq.RequeteRefusee):
            rq.RequeteAssemblee(r.sorte, r.generation, r.identifiant_case, octets, sha(octets), len(octets),
                                (r.composition[0], double) + reste, r.registre)

    def test_requete_hors_utf8_refusee(self):
        with self.assertRaises(rq.RequeteRefusee):
            rq.RequeteAssemblee("sonde_refus", None, "gaga", b"\xff", sha(b"\xff"), 1,
                                (rq.Element("x", "forme", 0, 1, sha(b"\xff")),), rq.REGISTRE_SANS_OBJET)


class TestDernierOctet(unittest.TestCase):

    def verifier_pieces(self, r, pieces):
        vues = [e for e in r.composition if e.sorte == "piece"]
        self.assertEqual(len(vues), len(pieces))
        for e, p in zip(vues, pieces):
            morceau = r.octets[e.debut:e.debut + e.taille]
            self.assertEqual(morceau, p.octets)
            self.assertEqual(morceau[-1:], p.octets[-1:])
            self.assertEqual(e.sha256, sha(p.octets))  # l'empreinte de la pièce entière
            self.assertEqual((e.piece_sha256, e.piece_taille), (p.sha256, p.taille))

    def test_dernier_octet_de_chaque_piece_garde(self):
        g, cs = B.gabarit(), B.cases()
        r = B.requete_generation_2()
        self.verifier_pieces(r, [rq.remplir_partie_servie(g, cs["2"][0]), B.synthese(), B.registre()])

    def test_fins_de_piece_non_normalisees(self):
        g, c = B.gabarit(), B.cases()["2"][1]
        for fin in (b"x", b"\n\n\n", b"  \n", b"\r\n"):
            s = B.synthese(b"Synthese factice inerte" + fin)
            reg = B.registre(b"registre factice inerte" + fin)
            r = rq.assembler_proposeur(g, c, s, 2, reg, B.TITRE_REGISTRE_FACTICE)
            self.verifier_pieces(r, [rq.remplir_partie_servie(g, c), s, reg])
            self.assertTrue(r.octets.endswith(b"registre factice inerte" + fin))
            i = [e for e in r.composition if e.nom == "synthèse servie"][0]
            self.assertEqual(r.octets[i.debut + i.taille:i.debut + i.taille + 1], b"\n")

    def test_partie_servie_et_synthese_jointes_sans_retrait(self):
        g, c = B.gabarit(), B.cases()["1"][2]
        r = rq.assembler_proposeur(g, c, B.synthese(), 1)
        p = rq.remplir_partie_servie(g, c)
        self.assertEqual(r.octets[p.taille - 1:p.taille + 1], b"\n\n")


class TestFormeFicheServie(unittest.TestCase):

    def setUp(self):
        self.c = B.cases()["1"][0]
        self.contenu = B.contenu_fiche(self.c)

    def test_portier_egal_a_la_forme_du_noyau(self):
        r = rq.assembler_portier_fiche(B.consigne_portier(), self.contenu, self.c.identifiant, 1)
        temoin = fv54.entree_une_fiche(B.CONSIGNE_PORTIER_FACTICE.decode("utf-8"), {"contenu": self.contenu}, [],
                                       "prefixe")
        self.assertEqual(r.octets, temoin.encode("utf-8"))
        self.assertEqual(r.sorte, "portier_fiche")

    def test_juge_egal_a_la_forme_du_noyau_identifiant_en_derniere_cle(self):
        idj = B.identifiant_juge()
        r = rq.assembler_juge(B.consigne_juge(), self.contenu, idj, self.c.identifiant, 2)
        temoin = fv54.entree_une_fiche(B.CONSIGNE_JUGE_FACTICE.decode("utf-8"), {"contenu": self.contenu}, [],
                                       "prefixe", identifiant_servi=idj)
        self.assertEqual(r.octets, temoin.encode("utf-8"))
        corps = [e for e in r.composition if e.nom == "fiche servie"][0]
        objet = json.loads(r.octets[corps.debut:corps.debut + corps.taille].decode("utf-8"))
        self.assertEqual(list(objet), list(rq.CHAMPS_FICHE) + ["identifiant"])
        self.assertEqual(objet["identifiant"], idj)

    def test_identifiant_du_noyau_refuse_au_juge(self):
        for faux in ("F" + "0a1b2c3d4e", "0a1b2c3d4e", ident.encoder_identifiant_fiche(bytes(6)), "", None, "GAGAGAGAGAGAGA"):
            with self.assertRaises(rq.RequeteRefusee):
                rq.assembler_juge(B.consigne_juge(), self.contenu, faux, self.c.identifiant, 1)

    def test_requete_de_juge_passe_la_garde_l_identifiant_hexadecimal_y_mordrait(self):
        garde = A.garde_essai()
        r = rq.assembler_juge(B.consigne_juge(), self.contenu, B.identifiant_juge(), self.c.identifiant, 1)
        garde.garder_requete(r.octets)
        noyau = r.octets.replace(B.identifiant_juge().encode(), b"F0a1b2c3d4e")
        with self.assertRaises(gm.ArretMotifInterdit):
            garde.garder_requete(noyau)

    def test_fiche_hors_des_douze_champs_refusee(self):
        moins = dict(self.contenu)
        del moins["filiation"]
        plus = dict(self.contenu, comment_faire="champ de plus")
        non_chaine = dict(self.contenu, idee=3)
        for contenu in (moins, plus, non_chaine, [], None):
            with self.assertRaises(rq.RequeteRefusee):
                rq.assembler_portier_fiche(B.consigne_portier(), contenu, self.c.identifiant, 1)
            with self.assertRaises(rq.RequeteRefusee):
                rq.assembler_juge(B.consigne_juge(), contenu, B.identifiant_juge(), self.c.identifiant, 1)

    def test_fin_de_consigne_retiree_par_la_forme_declaree_et_consignee(self):
        p = B.consigne_portier()
        r = rq.assembler_portier_fiche(p, self.contenu, self.c.identifiant, 1)
        e = r.composition[0]
        servie = B.CONSIGNE_PORTIER_FACTICE.decode("utf-8").rstrip().encode("utf-8")
        self.assertEqual(r.octets[:e.taille], servie)
        self.assertEqual((e.piece_sha256, e.piece_taille), (p.sha256, p.taille))
        self.assertEqual(e.sha256, sha(servie))
        ouverture = "\n\n## La fiche\n```json\n".encode("utf-8")
        self.assertEqual(r.octets[e.taille:e.taille + len(ouverture)], ouverture)
        self.assertTrue(r.octets.endswith(b"\n```\n"))

    def test_consigne_a_une_autre_empreinte_refusee(self):
        with self.assertRaises(rq.EmpreintePieceDifferente):
            rq.charger_piece("consigne du portier", B.CONSIGNE_PORTIER_FACTICE, sha(B.CONSIGNE_JUGE_FACTICE))

    def test_identifiant_de_case_verifie(self):
        for faux in ("", "gag", "abcdef12", None):
            with self.assertRaises(rq.RequeteRefusee):
                rq.assembler_portier_fiche(B.consigne_portier(), self.contenu, faux, 1)

    def test_reponse_sans_fiche_dans_la_forme_proposee(self):
        texte = "Réponse factice\n```\nsans fiche, inerte\n## titre factice"
        r = rq.assembler_portier_reponse_sans_fiche(B.consigne_portier(), texte, self.c.identifiant, 1)
        attendu = (B.CONSIGNE_PORTIER_FACTICE.decode("utf-8").rstrip() + "\n\n## La réponse\n```json\n"
                   + json.dumps({"reponse": texte}, ensure_ascii=False, indent=1) + "\n```\n").encode("utf-8")
        self.assertEqual(r.octets, attendu)
        lignes = r.octets.decode("utf-8").split("\n")
        self.assertEqual([l for l in lignes if l.startswith("```")], ["```json", "```"])
        with self.assertRaises(rq.RequeteRefusee):
            rq.assembler_portier_reponse_sans_fiche(B.consigne_portier(), b"octets", self.c.identifiant, 1)

    def test_generation_de_l_epreuve_permise_sans_numero(self):
        r = rq.assembler_portier_fiche(B.consigne_portier(), self.contenu, self.c.identifiant)
        self.assertIsNone(r.generation)
        with self.assertRaises(rq.RequeteRefusee):
            rq.assembler_portier_fiche(B.consigne_portier(), self.contenu, self.c.identifiant, 4)


class TestArret8Taille(unittest.TestCase):

    def requetes(self):
        g, cs = B.gabarit(), B.cases()
        c = cs["1"][0]
        return [rq.assembler_proposeur(g, c, B.synthese(), 1), B.requete_generation_2(),
                rq.assembler_sonde_refus(g, cs["reserve"]),
                rq.assembler_portier_fiche(B.consigne_portier(), B.contenu_fiche(c), c.identifiant, 1),
                rq.assembler_juge(B.consigne_juge(), B.contenu_fiche(c), B.identifiant_juge(), c.identifiant, 1)]

    def test_mesure_en_octets_registre_compris(self):
        for r in self.requetes():
            self.assertEqual(rq.mesurer(r), len(r.octets))
            self.assertEqual(rq.mesurer(r), sum(e.taille for e in r.composition))
        r2 = B.requete_generation_2()
        self.assertGreater(rq.mesurer(r2), len(B.REGISTRE_FACTICE) + len(A.SYNTHESE_FACTICE))

    def test_requete_egale_a_sa_borne_passe(self):
        for r in self.requetes():
            self.assertEqual(rq.verifier_borne(r, r.taille), r.taille)

    def test_un_octet_de_plus_refuse(self):
        for r in self.requetes():
            with self.assertRaises(rq.ArretConsigneTropLongue) as c:
                rq.verifier_borne(r, r.taille - 1)
            self.assertEqual(c.exception.numero, 8)
            self.assertEqual((c.exception.taille, c.exception.borne), (r.taille, r.taille - 1))
            message = str(c.exception) + repr(c.exception.args)
            self.assertNotIn("factice", message)

    def test_borne_invalide_refusee(self):
        r = B.requete_generation_2()
        for borne in (0, -1, 1.5, True, "100", None):
            with self.assertRaises(rq.RequeteRefusee):
                rq.verifier_borne(r, borne)
        with self.assertRaises(rq.RequeteRefusee):
            rq.mesurer(r.octets)

    def test_tailles_par_sorte(self):
        t = rq.tailles_par_sorte(self.requetes())
        self.assertEqual(t["proposeur"]["requetes"], 2)
        self.assertEqual(t["proposeur"]["plus_grande_taille"], B.requete_generation_2().taille)
        self.assertEqual(set(t), {"proposeur", "sonde_refus", "portier_fiche", "juge"})


class TestChaineDuNoyau(unittest.TestCase):

    def test_chaine_rend_les_octets(self):
        r = B.requete_generation_2()
        self.assertEqual(rq.chaine_pour_le_noyau(r.octets).encode("utf-8"), r.octets)
        with self.assertRaises(rq.RequeteRefusee):
            rq.chaine_pour_le_noyau(bytearray(r.octets))


if __name__ == "__main__":
    unittest.main()
