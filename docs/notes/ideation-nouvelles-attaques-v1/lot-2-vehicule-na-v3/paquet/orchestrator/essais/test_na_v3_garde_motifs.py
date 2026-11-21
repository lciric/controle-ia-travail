"""Essais du lot 2 du véhicule NA-1, v3 : `pole/garde_motifs_na_v3.py`, `pole/extraire_ignorables_unicode_na_v1.py`,
`pole/ignorables-unicode-15.1.0-na-v1.json`.

v3 (mère, 08:54Z à 08:59Z) : ignorables par propriété, tirés de `DerivedCoreProperties.txt` 15.1.0 ; liste fermée
d'apparence vide (U+2800) ; tirets, soulignements et espaces ramenés à une espace ; contrôle des plages contre `regex` là
où il est présent ; égalité des versions d'Unicode avec l'interpréteur de la course. Les essais de la v2 sont gardés ; un
seul change de lettre (`test_formes_ramenees` : les tirets deviennent des espaces).

v2 : ajoute l'ordre « famille puis rang » du premier constat (X-33), l'empreinte prise sur la copie (X-32) et l'égalité de
`verifier_avant_envoi`, exposée pour le lot 4 (X-30) ; les essais de la v1 sont gardés tels quels.

Sur la liste d'essai (`liste-motifs-essai-na-v1.json`, deux familles, motifs inertes) : la liste réelle n'est pas de ce lot.
Arrêt n° 16 par famille, cas sain et artefact (R5) ; une requête assemblée qui passe ; une qui porte un motif, refusée au
dernier point avant l'envoi ; aucun octet changé après la garde. Données factices seules ; aucun réseau, aucune clé.
"""

import hashlib
import json
import os
import subprocess
import sys
import unicodedata
import unittest
from unittest import mock

ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(ICI)
for _p in (ICI, RACINE):
    if _p not in sys.path:
        sys.path.insert(0, _p)

import aides_na_v3 as A  # noqa: E402
from pole import extraire_ignorables_unicode_na_v1 as ex  # noqa: E402
from pole import garde_motifs_na_v3 as gm  # noqa: E402
from pole import identifiants_na_v1 as ident  # noqa: E402
from pole import tirage_na_v3 as tn  # noqa: E402

FAM1, FAM2 = gm.FAMILLES
_N = A.normaliseur()


def normaliser(texte):
    return _N.normaliser(texte)


class TestFormatDeLaListe(unittest.TestCase):

    def test_liste_d_essai_lue_a_son_empreinte(self):
        liste = A.liste_essai()
        self.assertEqual(liste.sha256, A.EMPREINTE_LISTE_ESSAI)
        self.assertEqual([nom for nom, _ in liste.familles], [FAM1, FAM2])
        self.assertEqual([len(m) for _, m in liste.familles], [3, 2])

    def test_empreinte_differente_refusee(self):
        with self.assertRaises(gm.ListeMotifsRefusee) as c:
            gm.charger_liste_motifs(A.CHEMIN_LISTE_ESSAI, "0" * 64, _N)
        self.assertIn("empreinte", str(c.exception))

    def refus(self, familles=None, octets=None):
        if octets is None:
            octets, sha = A.liste_octets(familles)
        else:
            sha = hashlib.sha256(octets).hexdigest()
        with self.assertRaises(gm.ListeMotifsRefusee) as c:
            gm.lire_liste_motifs(octets, sha, _N)
        return str(c.exception)

    def test_cas_sain_construit(self):
        octets, sha = A.liste_octets(A.familles_saines())
        self.assertEqual(len(list(gm.GardeMotifs(gm.lire_liste_motifs(octets, sha, _N)).motifs())), 2)

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
        self.assertIn("vide ou blanc après normalisation", self.refus(f))
        f = A.familles_saines()
        f[0]["motifs"][0]["motif"] = "-_— \t"  # que des tirets, soulignements et espaces : blanc après normalisation
        self.assertIn("vide ou blanc après normalisation", self.refus(f))

    def test_liste_illisible(self):
        self.refus(octets=b"\xff\xfe{")
        self.refus(octets=b"[]")


class TestNormalisation(unittest.TestCase):

    def test_formes_ramenees(self):
        self.assertEqual(normaliser("ＧＲＡＩＮＥ ＦＡＣＴＩＣＥ"), "graine factice")
        self.assertEqual(normaliser("Graine \t\n  Factice"), "graine factice")
        self.assertEqual(normaliser("gra​ine­ fac﻿tice"), "graine factice")
        self.assertEqual(normaliser("a–b—c−d‑e"), "a b c d e")  # v3 : les tirets deviennent des espaces
        self.assertEqual(normaliser("STRASSE Straße"), "strasse strasse")

    def test_refuse_autre_chose_qu_une_chaine(self):
        with self.assertRaises(TypeError):
            normaliser(b"octets")


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
        liste = gm.lire_liste_motifs(octets, sha, _N)
        with self.assertRaises(gm.TemoinPositifManque) as c:
            gm.GardeMotifs(liste)
        self.assertEqual((c.exception.famille, c.exception.rang), (FAM2, 2))

    def test_temoins_rejoues_a_chaque_depart(self):
        garde = A.garde_essai()
        motif = next(iter(garde.motifs()))
        abime = gm.Motif(motif.famille, motif.rang, motif.type, motif.motif, "rien", motif._forme)
        garde.liste = gm.ListeMotifs(garde.liste.sha256, ((FAM1, (abime,)), garde.liste.familles[1]),
                                     garde.liste.normaliseur)
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


class TamponQuiChange(bytearray):
    """Un tampon d'appelant dont la seconde lecture rend d'autres octets : il simule un appelant qui change son tampon entre
    deux lectures. La garde ne doit le lire qu'une fois."""

    def __init__(self, premiers, suivants):
        super().__init__(premiers)
        self._lectures = [bytes(premiers), bytes(suivants)]

    def __bytes__(self):
        return self._lectures.pop(0) if len(self._lectures) > 1 else self._lectures[0]


class TestCorrectionsV2(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.garde = A.garde_essai()
        cls.sortie = A.sortie_factice()
        cls.saine = A.requete_factice(cls.sortie["generations"]["3"][2]["ligne"])

    def test_x33_premier_constat_famille_puis_rang(self):
        # dans le texte, la famille 2 vient avant la famille 1, et le rang 3 avant le rang 1 de la famille 1
        porteuse = (self.saine + b" une graine factice ; voir dossier-essai/fichier-factice.txt ; "
                    + "Personne Factice Alpha.".encode())
        with self.assertRaises(gm.ArretMotifInterdit) as c:
            self.garde.garder_requete(porteuse)
        self.assertEqual((c.exception.famille, c.exception.rang), (FAM1, 1))
        self.assertEqual(self.garde.examiner(porteuse.decode("utf-8")).texte_trouve, "personne factice alpha")
        # sans le motif de la famille 1, la famille 2 est rendue ; au sein d'une famille, le plus petit rang
        seconde = self.saine + " tirage d'essai numéro neuf, puis graine factice".encode()
        constat = self.garde.examiner(seconde.decode("utf-8"))
        self.assertEqual((constat.famille, constat.rang), (FAM2, 1))

    def test_x32_empreinte_prise_sur_la_copie_en_une_seule_lecture(self):
        autre = self.saine.replace(b"Synth", b"SYNTH", 1)
        self.assertNotEqual(autre, self.saine)
        tampon = TamponQuiChange(self.saine, autre)
        rg = self.garde.garder_requete(tampon)
        self.assertEqual(rg.octets, self.saine)
        self.assertEqual(rg.sha256, hashlib.sha256(self.saine).hexdigest())
        self.assertEqual(rg.sha256, hashlib.sha256(rg.octets).hexdigest())

    def test_x30_l_egalite_a_un_objet_au_lot_4(self):
        rg = self.garde.garder_requete(self.saine)
        gm.verifier_avant_envoi(rg, self.saine)
        gm.verifier_avant_envoi(rg, bytearray(self.saine))
        for ecart in (self.saine + b" ", self.saine[:-1], self.saine.replace(b"Synth", b"synth", 1)):
            with self.assertRaises(gm.EcartApresGarde):
                gm.verifier_avant_envoi(rg, ecart)
        with self.assertRaises(gm.EcartApresGarde):
            gm.verifier_avant_envoi(rg, self.saine.decode("utf-8"))


try:
    import regex as _regex  # présent sous .venv seulement : le contrôle contre `regex` s'y joue
except ImportError:
    _regex = None


class TestUneSeuleFormeEspaceTiret(unittest.TestCase):
    """Mère, 08:54Z et 08:59Z : tiret (Pd et U+2212), soulignement (Pc) et espace (`str.isspace()`) ramenés à une espace ;
    la comparaison se fait sur cette forme ; les octets d'origine partent et sont journalisés."""

    @classmethod
    def setUpClass(cls):
        cls.garde = A.garde_essai()
        cls.saine = A.requete_factice(A.sortie_factice()["generations"]["1"][4]["ligne"])

    def refus(self, ajout):
        with self.assertRaises(gm.ArretMotifInterdit) as c:
            self.garde.garder_requete(self.saine + ajout.encode("utf-8"))
        return c.exception.famille, c.exception.rang

    def test_les_quatre_formes_demandees_sont_refusees_comme_graine_factice(self):
        for forme in ("graine-factice", "graine_factice", "graine factice", "graine  factice"):
            self.assertEqual(self.refus(" " + forme + " "), (FAM2, 1), forme)

    def test_autres_tirets_soulignements_et_espaces(self):
        for forme in ("graine—factice", "graine–factice", "graine−factice", "graine‐factice",
                      "graine﹏factice", "graine‿factice", "graine\tfactice", "graine\nfactice",
                      "graine\r\nfactice", "graine factice", "graine　factice", "graine — _ factice"):
            self.assertEqual(self.refus(" " + forme + " "), (FAM2, 1), repr(forme))

    def test_cas_sain_ce_qui_n_est_ni_tiret_ni_espace_ne_relie_pas(self):
        for forme in ("grainefactice", "graine.factice", "graine/factice", "graine~factice"):
            self.assertIsNone(self.garde.examiner(forme), forme)

    def test_une_requete_saine_passe_et_ses_octets_sont_inchanges(self):
        porteuse = self.saine + "\ntrait-d'union_et espace—et\ttabulation\n".encode("utf-8")
        journal, envois = [], []
        gm.envoyer_apres_garde(self.garde, porteuse, envois.append, journal.append)
        self.assertEqual(envois, [porteuse])
        self.assertEqual(journal[0]["sha256"], hashlib.sha256(porteuse).hexdigest())
        self.assertEqual(journal[0]["taille"], len(porteuse))

    def test_le_texte_trouve_ne_va_qu_a_la_ligne_non_envoye(self):
        journal = []
        with self.assertRaises(gm.ArretMotifInterdit) as c:
            gm.envoyer_apres_garde(self.garde, self.saine + "graine_factice".encode(), [].append, journal.append)
        self.assertEqual(len(journal), 1)
        self.assertEqual(journal[0]["evenement"], "non envoyé")
        self.assertEqual(journal[0]["texte_trouve"], "graine factice")
        self.assertNotIn("graine", str(c.exception))
        self.assertNotIn("graine", repr(c.exception.args))


class TestCaracteresInvisibles(unittest.TestCase):
    """Mère, 08:54Z à 08:59Z : Cf, plus les ignorables par défaut (par propriété, données tirées du fichier 15.1.0), plus
    la liste fermée d'apparence vide (U+2800)."""

    @classmethod
    def setUpClass(cls):
        cls.garde = A.garde_essai()
        cls.donnees = A.donnees()

    def test_les_quatre_caracteres_du_verificateur_n_empechent_plus_le_refus(self):
        for c in (0xFE0F, 0x034F, 0x3164, 0x2800):
            constat = self.garde.examiner("une grai" + chr(c) + "ne factice")
            self.assertIsNotNone(constat, f"U+{c:04X}")
            self.assertEqual((constat.famille, constat.rang), (FAM2, 1))

    def test_par_propriete_d_autres_ignorables_que_les_quatre(self):
        for c in (0x115F, 0x17B4, 0x180B, 0x180F, 0xFFA0, 0xE0100, 0xE0FFF, 0x2065):
            self.assertIn(c, self.donnees.points)
            self.assertIsNotNone(self.garde.examiner("une grai" + chr(c) + "ne factice"), f"U+{c:04X}")

    def test_cf_hors_des_ignorables_retires_aussi(self):
        for c in (0x0600, 0x06DD, 0xFFF9, 0x110BD):  # catégorie Cf, non ignorables par défaut en 15.1
            self.assertEqual(unicodedata.category(chr(c)), "Cf")
            self.assertNotIn(c, self.donnees.points)
            self.assertIsNotNone(self.garde.examiner("une grai" + chr(c) + "ne factice"), f"U+{c:04X}")

    def test_cas_sain_ces_caracteres_dans_un_texte_neutre_ne_font_pas_refuser(self):
        for c in (0xFE0F, 0x034F, 0x3164, 0x2800, 0xE0100):
            self.assertIsNone(self.garde.examiner("texte" + chr(c) + "neutre"))

    def test_liste_fermee_d_apparence_vide(self):
        self.assertEqual(gm.APPARENCE_VIDE, (0x2800,))
        for c in gm.APPARENCE_VIDE:
            ch = chr(c)
            self.assertNotIn(c, self.donnees.points)  # ni ignorable par défaut…
            self.assertNotEqual(unicodedata.category(ch), "Cf")  # … ni « Cf »…
            self.assertFalse(ch.isspace())  # … ni espace : sinon la liste serait sans objet pour lui

    def test_sans_la_liste_u2800_ferait_passer_le_motif(self):
        n = A.normaliseur()
        n._retires = self.donnees.points  # artefact : la liste d'apparence vide ôtée
        self.assertEqual(n.normaliser("grai⠀ne"), "grai⠀ne")
        self.assertEqual(A.normaliseur().normaliser("grai⠀ne"), "graine")


class TestDonneesDesIgnorables(unittest.TestCase):

    def test_donnees_lues_a_leur_empreinte_et_citant_leur_source(self):
        d = A.donnees()
        self.assertEqual(d.version_unicode, "15.1.0")
        self.assertEqual(len(d.points), 4174)
        self.assertEqual(len(d.plages), 27)
        self.assertEqual(d.source["sha256"], A.EMPREINTE_SOURCE_UNICODE)
        self.assertEqual(d.source["commit"], A.COMMIT_SOURCE_UNICODE)
        self.assertEqual(d.source["chemin"], A.CHEMIN_DEPOT_SOURCE)
        self.assertTrue(d.source["en_tete"].startswith("DerivedCoreProperties-15.1.0.txt"))
        for c in (0xFE0F, 0x034F, 0x3164, 0x00AD):
            self.assertIn(c, d.points)
        self.assertNotIn(0x2800, d.points)

    def objet(self):
        with open(A.CHEMIN_DONNEES, "rb") as f:
            return json.loads(f.read())

    def refus(self, obj):
        octets = json.dumps(obj).encode("utf-8")
        with self.assertRaises((gm.DonneesIgnorablesRefusees, gm.VersionUnicodeDifferente)) as c:
            gm.lire_donnees_ignorables(octets, hashlib.sha256(octets).hexdigest())
        return str(c.exception)

    def test_donnees_vides_refusees_au_chargement(self):
        o = self.objet()
        o["source"], o["plages"] = None, None
        self.assertIn("données vides", self.refus(o))

    def test_autre_empreinte_refusee(self):
        with self.assertRaises(gm.DonneesIgnorablesRefusees):
            gm.charger_donnees_ignorables(A.CHEMIN_DONNEES, "0" * 64)

    def test_autre_version_refusee(self):
        o = self.objet()
        o["version_unicode"] = "16.0.0"
        self.assertIn("version", self.refus(o))

    def test_plages_chevauchantes_ou_total_faux_refuses(self):
        o = self.objet()  # deux plages permutées : mêmes points, même total ; seul l'ordre est faux
        o["plages"][0], o["plages"][1] = o["plages"][1], o["plages"][0]
        self.assertIn("non triée ou chevauchante", self.refus(o))
        o = self.objet()  # une plage répétée : chevauchement, total recalculé pour qu'il ne soit pas, lui, en défaut
        o["plages"][1] = list(o["plages"][0])
        o["total"] -= 1
        self.assertIn("non triée ou chevauchante", self.refus(o))
        o = self.objet()
        o["total"] += 1
        self.assertIn("total", self.refus(o))
        o = self.objet()
        o["source"]["sha256"] = "court"
        self.assertIn("source", self.refus(o))
        o = self.objet()
        o["en_plus"] = 1
        self.refus(o)

    def test_normaliseur_et_liste_exigent_des_donnees_acceptees(self):
        with self.assertRaises(gm.DonneesIgnorablesRefusees):
            gm.Normaliseur(None)
        octets, sha = A.liste_octets(A.familles_saines())
        with self.assertRaises(gm.DonneesIgnorablesRefusees):
            gm.lire_liste_motifs(octets, sha, None)

    def test_donnees_refusees_sous_un_interprete_d_une_autre_version(self):
        with mock.patch.object(gm.unicodedata, "unidata_version", "15.0.0"):
            with self.assertRaises(gm.VersionUnicodeDifferente):
                A.donnees()


class TestVersionDeLInterpreteDeLaCourse(unittest.TestCase):
    """Essai de forme (mère, 08:55Z) : la version d'Unicode des données égale celle de `/usr/local/bin/python3` ; sinon,
    refus. L'interpréteur absent est un échec, non un saut."""

    def version_course(self):
        r = subprocess.run([A.INTERPRETE_COURSE, "-I", os.path.join(ICI, "sonde_version_unicode_na_v3.py")],
                           capture_output=True, text=True, check=True)
        return r.stdout.strip()

    def test_versions_egales(self):
        v = self.version_course()
        self.assertEqual(v, "15.1.0")
        self.assertEqual(gm.verifier_version_interprete(A.donnees().version_unicode, v), "15.1.0")
        self.assertEqual(gm.VERSION_UNICODE_ATTENDUE, v)

    def test_versions_differentes_refusees(self):
        for autre in ("16.0.0", "15.0.0", ""):
            with self.assertRaises(gm.VersionUnicodeDifferente):
                gm.verifier_version_interprete(A.donnees().version_unicode, autre)


FACTICE_DCP = (
    "# DerivedCoreProperties-15.1.0.txt\n"
    "# Date: factice, essais seulement\n"
    "0041..005A    ; Alphabetic # Lu  [26] factice\n"
    "\n"
    "# Derived Property: Default_Ignorable_Code_Point\n"
    "00AD          ; Default_Ignorable_Code_Point # Cf       factice\n"
    "034F          ; Default_Ignorable_Code_Point # Mn       factice\n"
    "FE00..FE0F    ; Default_Ignorable_Code_Point # Mn  [16] factice\n"
    "\n"
    "# Total code points: 18\n"
    "\n"
    "0300..036F    ; Grapheme_Extend # Mn [112] factice\n"
    "# Total code points: 112\n"
)


class TestExtraction(unittest.TestCase):

    def extraire(self, texte, **k):
        octets = texte.encode("utf-8")
        return ex.extraire(octets, hashlib.sha256(octets).hexdigest(), "chemin/factice", "commit-factice", **k)

    def test_cas_sain_factice(self):
        d = self.extraire(FACTICE_DCP)
        self.assertEqual(d["plages"], [[0xAD, 0xAD], [0x34F, 0x34F], [0xFE00, 0xFE0F]])
        self.assertEqual(d["total"], 18)
        self.assertEqual(d["version_unicode"], "15.1.0")

    def test_artefacts_refuses(self):
        octets = FACTICE_DCP.encode("utf-8")
        with self.assertRaises(ex.ExtractionRefusee):
            ex.extraire(octets, "0" * 64, "c", "k")
        for fautif in (FACTICE_DCP.replace("15.1.0.txt", "16.0.0.txt"),
                       FACTICE_DCP.replace("# Total code points: 18", "# Total code points: 19"),
                       FACTICE_DCP.replace("034F          ;", "00A0          ;"),
                       FACTICE_DCP.replace("# DerivedCoreProperties", "# Autre")):
            with self.assertRaises(ex.ExtractionRefusee):
                self.extraire(fautif)
        with self.assertRaises(ex.ExtractionRefusee):
            self.extraire(FACTICE_DCP, version_interprete="16.0.0")

    def test_extraction_reelle_rejouee_egale_a_l_octet(self):
        source = os.environ.get("NA_SOURCE_UNICODE_15_1_0")
        if not source:
            self.skipTest("NA_SOURCE_UNICODE_15_1_0 non donnée : chemin local du fichier versé par la mère")
        with open(source, "rb") as f:
            obj = ex.extraire(f.read(), A.EMPREINTE_SOURCE_UNICODE, A.CHEMIN_DEPOT_SOURCE, A.COMMIT_SOURCE_UNICODE)
        with open(A.CHEMIN_DONNEES, "rb") as f:
            self.assertEqual(ex.serialiser(obj), f.read())


@unittest.skipIf(_regex is None, "module `regex` absent : le contrôle se joue sous .venv")
class TestControleContreRegex(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        import controle_ignorables_regex_na_v3 as cr
        cls.cr = cr
        cls.rx = cr.points_regex()

    def test_aucun_ecart_sur_les_points_communs(self):
        r = self.cr.controler(A.donnees().points, self.rx)
        self.assertEqual(r["ecarts_sur_points_communs"], 0, r["ecarts_communs_nommes"])
        self.assertEqual(r["points_donnees"], 4174)

    def test_un_ecart_plante_est_compte_et_nomme(self):
        r = self.cr.controler(A.donnees().points - {0x034F}, self.rx)
        self.assertEqual(r["ecarts_sur_points_communs"], 1)
        self.assertEqual(r["ecarts_communs_nommes"], [{"point": "U+034F", "donnees": False, "regex": True}])


class TestEmpreinteDuProgramme(unittest.TestCase):

    def test_empreinte_du_programme(self):
        with open(gm.__file__, "rb") as f:
            self.assertEqual(gm.empreinte_programme(), hashlib.sha256(f.read()).hexdigest())


if __name__ == "__main__":
    unittest.main()
