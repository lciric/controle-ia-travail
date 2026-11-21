"""Essais du lot 1 du véhicule NA-1 : `pole/tirage_na_v1.py` et `pole/identifiants_na_v1.py`.

Données factices seules : gabarit factice, racine factice (le tirage réel n'est jamais joué ici), liste de motifs d'essai.
Chaque garde : un cas sain et un artefact (R5) ; chaque refus est éprouvé pour sa cause. Aucun réseau, aucune clé.
"""

import copy
import hashlib
import json
import os
import re
import subprocess
import sys
import tempfile
import unittest
from unittest import mock

ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(ICI)
for _p in (ICI, RACINE):
    if _p not in sys.path:
        sys.path.insert(0, _p)

import numpy  # noqa: E402

import aides_na_v1 as A  # noqa: E402
from pole import garde_motifs_na_v1 as gm  # noqa: E402
from pole import identifiants_na_v1 as ident  # noqa: E402
from pole import tirage_na_v1 as tn  # noqa: E402

HEXA8 = re.compile(r"[0-9A-Fa-f]{8,}")


def rng(entropie, cle):
    return numpy.random.default_rng(numpy.random.SeedSequence(entropy=entropie, spawn_key=(cle,)))


def base60_attendue(valeur, n):
    """Écriture indépendante, pour les vecteurs connus."""
    syl = [c + v for c in "gjklmnprstvz" for v in "aeiou"]
    chiffres = []
    for _ in range(n):
        chiffres.append(valeur % 60)
        valeur //= 60
    return "".join(syl[d] for d in reversed(chiffres))


class TestIdentifiants(unittest.TestCase):
    """Réencodage (conception v4, § 5.2), éprouvé dans les deux sens (§ 6.2)."""

    def test_alphabet_et_rang_des_syllabes(self):
        self.assertEqual(len(ident.SYLLABES), 60)
        self.assertEqual(len(set(ident.SYLLABES)), 60)
        self.assertFalse(set(ident.CONSONNES) & set("abcdef0123456789"))
        for ic, c in enumerate("gjklmnprstvz"):
            for iv, v in enumerate("aeiou"):
                self.assertEqual(ident.RANG_SYLLABE[c + v], 5 * ic + iv)

    def test_vecteurs_connus_et_ordre_des_octets(self):
        self.assertEqual(ident.encoder_octets(bytes(6)), "ga" * 9)
        self.assertEqual(ident.encoder_octets(bytes(5)), "ga" * 7)
        self.assertEqual(ident.encoder_octets(b"\x00" * 5 + b"\x01"), "ga" * 8 + "ge")
        # premier octet le plus fort : 0x01 suivi de cinq zéros vaut 2 ** 40
        self.assertEqual(ident.encoder_octets(b"\x01" + b"\x00" * 5), base60_attendue(2 ** 40, 9))
        self.assertEqual(ident.encoder_octets(b"\x01\x02\x03\x04\x05"), base60_attendue(0x0102030405, 7))

    def test_longueurs_dix_huit_et_quatorze(self):
        self.assertEqual(len(ident.encoder_identifiant_fiche(b"\xff" * 6)), 18)
        self.assertEqual(len(ident.encoder_identifiant_juge(b"\xff" * 5)), 14)
        self.assertEqual(len(ident.mot_de_case(0)), 6)
        with self.assertRaises(ident.EncodageRefuse):
            ident.encoder_octets(b"\x00" * 4)
        with self.assertRaises(ident.EncodageRefuse):
            ident.encoder_identifiant_fiche(b"\x00" * 5)

    def test_aller_retour_sur_un_echantillon_tire(self):
        for n in (6, 5):
            valeurs = rng(A.ENTROPIE_ECHANTILLONS, 900 + n).integers(0, 256, size=(3000, n))
            for ligne in valeurs:
                octets = bytes(int(x) for x in ligne)
                mot = ident.encoder_octets(octets)
                self.assertEqual(len(mot), 2 * ident.SYLLABES_PAR_OCTETS[n])
                self.assertEqual(ident.decoder_octets(mot, n), octets)
                self.assertIsNone(HEXA8.search(mot))
                self.assertIsNone(re.search(r"[0-9]", mot))

    def test_decoder_puis_encoder_rend_le_mot(self):
        for n in (6, 5):
            ent = rng(A.ENTROPIE_ECHANTILLONS, 910 + n).integers(0, 256 ** n, size=2000, dtype=numpy.uint64)
            for v in ent:
                mot = ident.encoder_entier(int(v), ident.SYLLABES_PAR_OCTETS[n])
                self.assertEqual(ident.encoder_octets(ident.decoder_octets(mot, n)), mot)

    def test_bornes_zero_et_deux_cent_cinquante_cinq(self):
        for n in (6, 5):
            for octets in (bytes(n), b"\xff" * n):
                self.assertEqual(ident.decoder_octets(ident.encoder_octets(octets), n), octets)

    def test_refus_hors_alphabet(self):
        bon = ident.encoder_octets(b"\x10\x20\x30\x40\x50\x60")
        for fautif in ("b" + bon[1:], bon[:-1] + "B", bon[:4] + "G" + bon[5:], "0" + bon[1:], bon[:2] + "ef" + bon[4:]):
            with self.assertRaises(ident.MotRefuse) as c:
                ident.decoder_octets(fautif, 6)
            self.assertEqual(c.exception.cause, "hors alphabet")

    def test_refus_mauvaise_longueur(self):
        bon = ident.encoder_octets(b"\x10\x20\x30\x40\x50\x60")
        for fautif in (bon[:-2], bon + "ga", bon[:14]):
            with self.assertRaises(ident.MotRefuse) as c:
                ident.decoder_octets(fautif, 6)
            self.assertEqual(c.exception.cause, "longueur")
        with self.assertRaises(ident.MotRefuse):
            ident.decoder_octets(bon, 5)

    def test_refus_entier_au_dela_de_la_borne(self):
        for n in (6, 5):
            with self.assertRaises(ident.MotRefuse) as c:
                ident.decoder_octets("zu" * ident.SYLLABES_PAR_OCTETS[n], n)
            self.assertEqual(c.exception.cause, "entier au-delà de la borne")
        # juste à la borne : 256 ** n écrit en base 60 est refusé, 256 ** n − 1 est rendu
        for n in (6, 5):
            L = ident.SYLLABES_PAR_OCTETS[n]
            with self.assertRaises(ident.MotRefuse):
                ident.decoder_octets(base60_attendue(256 ** n, L), n)
            self.assertEqual(ident.decoder_octets(base60_attendue(256 ** n - 1, L), n), b"\xff" * n)

    def test_aucune_suite_hexadecimale_possible_entre_deux_syllabes(self):
        for s1 in ident.SYLLABES:
            for s2 in ident.SYLLABES:
                self.assertIsNone(re.search(r"[0-9a-f]{2,}", s1 + s2), s1 + s2)

    def test_reencoder_un_jeton_du_noyau(self):
        self.assertEqual(ident.decoder_octets(ident.reencoder_jeton_noyau("f0a1b2c3d4e5f", "f", 6), 6),
                         bytes.fromhex("0a1b2c3d4e5f"))
        self.assertEqual(len(ident.reencoder_jeton_noyau("F0a1b2c3d4e", "F", 5)), 14)
        for fautif in ("f0A1B2C3D4E5F", "f0a1b2c3d4e5", "g0a1b2c3d4e5f", "f0a1b2c3d4e5fz"):
            with self.assertRaises(ident.EncodageRefuse):
                ident.reencoder_jeton_noyau(fautif, "f", 6)

    def test_mot_de_case(self):
        self.assertEqual(ident.mot_de_case(0), "gagaga")
        self.assertEqual(ident.mot_de_case(215999), "zuzuzu")
        self.assertEqual(ident.rang_du_mot_de_case(ident.mot_de_case(123456)), 123456)
        with self.assertRaises(ident.EncodageRefuse):
            ident.mot_de_case(216000)


class TestLegende(unittest.TestCase):
    """La légende lue dans le gabarit, à son empreinte ; jamais la question."""

    def test_cas_sain(self):
        lg = tn.lire_legende(A.GABARIT_FACTICE, A.EMPREINTE_GABARIT_FACTICE)
        self.assertEqual([len(v) for v in lg["valeurs"]], [6, 5, 4])
        self.assertEqual(lg["axes"], list(tn.AXES))
        self.assertEqual(lg["valeurs"][0][5], "autre, à nommer")

    def test_empreinte_differente_refusee(self):
        autre = A.GABARIT_FACTICE.replace(b"inerte", b"inertE")
        with self.assertRaises(tn.TirageRefuse) as c:
            tn.lire_legende(autre, A.EMPREINTE_GABARIT_FACTICE)
        self.assertIn("empreinte du gabarit", str(c.exception))

    def test_question_refusee_par_son_nom(self):
        with self.assertRaises(tn.TirageRefuse) as c:
            tn.lire_legende(A.GABARIT_FACTICE, A.EMPREINTE_GABARIT_FACTICE,
                            nom="/x/prereg/question-course-nouvelles-attaques-v5.md")
        self.assertIn("question", str(c.exception))

    def test_empreinte_de_la_question_refusee(self):
        with mock.patch.object(tn, "EMPREINTES_INTERDITES", (A.EMPREINTE_GABARIT_FACTICE,)):
            with self.assertRaises(tn.TirageRefuse) as c:
                tn.lire_legende(A.GABARIT_FACTICE, A.EMPREINTE_GABARIT_FACTICE)
        self.assertIn("empreinte de la question", str(c.exception))

    def test_table_absente_ou_double_refusee(self):
        for g in (A.GABARIT_FACTICE.replace(b"| axe | valeurs |", b"| axe | valeur |"),
                  A.GABARIT_FACTICE + b"\n| axe | valeurs |\n"):
            with self.assertRaises(tn.TirageRefuse):
                tn.lire_legende(g, hashlib.sha256(g).hexdigest())

    def test_valeur_autre_deplacee_refusee(self):
        g = A.GABARIT_FACTICE.replace(b"trait factice cinq ; autre, \xc3\xa0 nommer",
                                      b"autre, \xc3\xa0 nommer ; trait factice cinq")
        with self.assertRaises(tn.TirageRefuse):
            tn.lire_legende(g, hashlib.sha256(g).hexdigest())

    def test_nombre_de_valeurs_refuse(self):
        g = A.GABARIT_FACTICE.replace(b" ; menace factice cinq |", b" |")
        with self.assertRaises(tn.TirageRefuse):
            tn.lire_legende(g, hashlib.sha256(g).hexdigest())


class TestRacineEtNumpy(unittest.TestCase):

    def test_racine_ecrite_a_la_lettre(self):
        self.assertEqual(tn.RACINE_ECRITE, 0x2cf2aae035beef43e999e3cd8b0fb7ba)
        empreinte_question_v3 = "2cf2aae035beef43e999e3cd8b0fb7ba3808649b3cc8b29661c1244b0540415b"
        self.assertEqual(tn.RACINE_ECRITE, int(empreinte_question_v3[:32], 16))

    def test_racine_recalculee_sur_une_autre_empreinte_refusee(self):
        recalculee = int("eaf5db8a558547aa8f5df45008a34eebf4cb7a163e12ca400176401de6f5ce0f"[:32], 16)
        with self.assertRaises(tn.TirageRefuse) as c:
            tn.TirageNA(A.GABARIT_FACTICE, empreinte_gabarit=A.EMPREINTE_GABARIT_FACTICE, racine=recalculee)
        self.assertIn("racine", str(c.exception))
        with self.assertRaises(tn.TirageRefuse):
            tn.permutation_registre(2, 5, racine=recalculee)

    def test_numpy_sous_1_25_refuse(self):
        with mock.patch.object(tn.numpy, "__version__", "1.24.4"):
            with self.assertRaises(tn.TirageRefuse) as c:
                A.tirage_factice()
        self.assertIn("1.25", str(c.exception))
        self.assertEqual(tn.verifier_numpy("1.25.0"), "1.25.0")
        for v in ("0.99", "1.9.3", "inconnue"):
            with self.assertRaises(tn.TirageRefuse):
                tn.verifier_numpy(v)


class TestTirage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.sortie = A.sortie_factice()

    def test_rejoue_deux_fois_egal_a_l_octet(self):
        self.assertEqual(tn.serialiser(A.sortie_factice()), tn.serialiser(A.sortie_factice()))

    def test_rejoue_dans_deux_processus_egal_a_l_octet(self):
        with tempfile.TemporaryDirectory() as d:
            sorties = []
            for i, graine_hachage in enumerate(("0", "12345")):
                chemin = os.path.join(d, f"tirage-{i}.json")
                env = {"PATH": os.environ.get("PATH", ""), "PYTHONHASHSEED": graine_hachage,
                       "PYTHONDONTWRITEBYTECODE": "1"}
                subprocess.run([sys.executable, "-B", os.path.join(ICI, "aides_na_v1.py"), chemin], env=env, check=True)
                with open(chemin, "rb") as f:
                    sorties.append(f.read())
        self.assertEqual(sorties[0], sorties[1])
        self.assertEqual(sorties[0], tn.serialiser(self.sortie))

    def test_sortie_deterministe_sans_heure(self):
        octets = tn.serialiser(self.sortie)
        self.assertTrue(octets.endswith(b"\n"))
        self.assertNotIn(b"\r", octets)
        self.assertNotIn("heure", json.loads(octets))
        self.assertEqual(octets, (json.dumps(json.loads(octets), ensure_ascii=False, sort_keys=True, indent=1)
                                  + "\n").encode("utf-8"))

    def test_comptes_et_partition(self):
        s = self.sortie
        servies = [tuple(c["triplet"]) for g in "123" for c in s["generations"][g]]
        famille = [tuple(c) for c in s["famille_tenue_a_l_ecart"]["cases"]]
        reserve = [tuple(c) for c in s["reserve"]["cases"]]
        self.assertEqual([len(s["generations"][g]) for g in "123"], [11, 11, 11])
        self.assertEqual((len(famille), len(reserve), s["reserve"]["compte"]), (20, 67, 67))
        self.assertEqual(sorted(servies + famille + reserve), tn.cases_canoniques())
        self.assertEqual(reserve, sorted(reserve))
        self.assertEqual(tuple(s["reserve"]["premiere"]["triplet"]), reserve[0])
        self.assertIn(s["famille_tenue_a_l_ecart"]["rang_axe_0"], range(5))

    def test_tirages_recalcules_a_part(self):
        s = self.sortie
        f = int(rng(A.RACINE_FACTICE, 0).integers(0, 5))
        self.assertEqual(s["famille_tenue_a_l_ecart"]["rang_axe_0"], f)
        restantes = [c for c in tn.cases_canoniques() if c[0] != f]
        for g, n in zip("123", (100, 89, 78)):
            self.assertEqual(len(restantes), n)
            rangs = rng(A.RACINE_FACTICE, int(g)).choice(n, size=11, replace=False)
            attendues = [restantes[int(r)] for r in rangs]
            self.assertEqual([tuple(c["triplet"]) for c in s["generations"][g]], attendues)
            restantes = [c for c in restantes if c not in set(attendues)]

    def test_cle_40_mots_de_case(self):
        s = self.sortie
        rangs = rng(A.RACINE_FACTICE, 40).choice(216000, size=120, replace=False)
        attendus = [ident.mot_de_case(int(r)) for r in rangs]
        self.assertEqual([e["identifiant"] for e in s["identifiants"]], attendus)
        self.assertEqual([tuple(e["triplet"]) for e in s["identifiants"]], tn.cases_canoniques())
        self.assertEqual(len(set(attendus)), 120)
        garde = A.garde_essai()
        for mot in attendus:
            self.assertEqual(len(mot), 6)
            self.assertIsNone(HEXA8.search(mot))
            self.assertIsNone(re.search(r"[0-9]", mot))
            self.assertIsNone(garde.examiner(mot))

    def test_cle_30_cas_sain(self):
        s = self.sortie
        servies = sorted(tuple(c["triplet"]) for g in "123" for c in s["generations"][g])
        candidates = [c for c in servies if c[1] == 0]
        self.assertEqual(s["cle_30"]["n"], len(candidates))
        self.assertGreater(len(candidates), 0)  # la racine factice en donne : sinon l'essai ne dirait rien
        r = int(rng(A.RACINE_FACTICE, 30).integers(0, len(candidates)))
        self.assertEqual(s["cle_30"]["rang"], r)
        self.assertEqual(tuple(s["cle_30"]["case"]), candidates[r])
        self.assertEqual(candidates[r][1], 0)

    def test_cle_30_aucune_case_de_sabotage_rien_n_est_tire(self):
        t = A.tirage_factice()
        t.tirer_famille()
        t.tirer_generations()
        sans = [c for c in tn.cases_canoniques() if c[1] != 0 and c[0] != t.famille]
        t.generations = {1: sans[:11], 2: sans[11:22], 3: sans[22:33]}  # tirage d'essai planté
        cles = []
        vrai = tn.rng_de_cle
        with mock.patch.object(tn, "rng_de_cle", lambda r, c: (cles.append(c), vrai(r, c))[1]):
            res = t.tirer_cle_30()
        self.assertEqual(res, {"n": 0, "rang": None, "case": "aucune"})
        self.assertNotIn(30, cles)
        with self.assertRaises(tn.SecondTirageRefuse):
            t.tirer_cle_30()

    def test_cle_30_second_tirage_refuse(self):
        t = A.tirage_factice()
        t.jouer(A.garde_essai())
        with self.assertRaises(tn.SecondTirageRefuse):
            t.tirer_cle_30()
        with self.assertRaises(tn.SecondTirageRefuse):
            t.tirer_famille()
        with self.assertRaises(tn.SecondTirageRefuse):
            t.tirer_identifiants(A.garde_essai())

    def test_cles_30_et_40_au_meme_geste_et_consignees(self):
        cles = []
        vrai = tn.rng_de_cle
        with mock.patch.object(tn, "rng_de_cle", lambda r, c: (cles.append(c), vrai(r, c))[1]):
            s = A.sortie_factice()
        self.assertEqual(cles, [0, 1, 2, 3, 30, 40])
        self.assertEqual(s["cles"]["case_mode_tenu_a_l_ecart"], 30)
        self.assertEqual(s["cles"]["identifiants"], 40)
        self.assertIn("cle_30", s)
        self.assertEqual(s["liste_motifs_sha256"], A.EMPREINTE_LISTE_ESSAI)

    def test_cle_40_mot_refuse_arrete_le_tirage_sans_second_tirage(self):
        mot = self.sortie["identifiants"][7]["identifiant"]
        familles = A.familles_saines()
        familles[1]["motifs"].append({"rang": 2, "type": "litteral", "motif": mot, "temoin_positif": "x " + mot})
        octets, sha = A.liste_octets(familles)
        garde = gm.GardeMotifs(gm.lire_liste_motifs(octets, sha))
        t = A.tirage_factice()
        cles = []
        vrai = tn.rng_de_cle
        with mock.patch.object(tn, "rng_de_cle", lambda r, c: (cles.append(c), vrai(r, c))[1]):
            with self.assertRaises(tn.TirageArreteMotRefuse) as c:
                t.jouer(garde)
        self.assertEqual((c.exception.famille, c.exception.rang), ("composition et tenue", 2))
        self.assertEqual(cles.count(40), 1)
        self.assertIsNone(t.mots)
        self.assertNotIn(mot, str(c.exception))

    def test_garde_exigee(self):
        with self.assertRaises(tn.TirageRefuse):
            A.tirage_factice().jouer(None)


class TestLigneDeCase(unittest.TestCase):
    """Ligne de case et son contrôle (V9, l. 75 ; conception v4, § 6.2)."""

    @classmethod
    def setUpClass(cls):
        cls.sortie = A.sortie_factice()
        cls.lignes = tn.lignes_du_tirage(cls.sortie)
        cls.legende = cls.sortie["legende"]

    def refus(self, lignes):
        with self.assertRaises(tn.LigneDeCaseRefusee) as c:
            tn.controler_lignes_de_case(lignes, self.legende)
        return c.exception.cause

    def plante(self, i, nouvelle):
        lignes = list(self.lignes)
        lignes[i] = (lignes[i][0], nouvelle)
        return lignes

    def test_cas_sain_trente_trois_lignes_et_la_reserve(self):
        self.assertEqual(len(self.lignes), 34)
        self.assertEqual(tn.controler_lignes_de_case(self.lignes, self.legende), 34)
        for _t, ligne in self.lignes:
            self.assertLessEqual(len(ligne.encode("utf-8")), 256)
            self.assertTrue(ligne.startswith("case : "))
        plus_longue = tn.plus_longue_ligne_possible(self.legende)
        self.assertLessEqual(max(len(l.encode("utf-8")) for _t, l in self.lignes), plus_longue)
        self.assertLessEqual(plus_longue, 256)

    def test_valeur_qui_differe_d_un_octet(self):
        t, ligne = self.lignes[3]
        self.assertEqual(self.refus(self.plante(3, ligne[:-1] + chr(ord(ligne[-1]) ^ 1))), "valeur")

    def test_identifiant_numerote_sur_un_total(self):
        t, ligne = self.lignes[0]
        reste = ligne.split(" ; ", 1)[1]
        self.assertEqual(self.refus(self.plante(0, "case : 7 sur 33 ; " + reste)), "chiffre")
        self.assertEqual(self.refus(self.plante(0, "case : septieme-sur-trente-trois ; " + reste)), "identifiant")

    def test_huit_caracteres_hexadecimaux_de_suite(self):
        t, ligne = self.lignes[5]
        self.assertEqual(self.refus(self.plante(5, ligne + " deadbeefcafe")), "hexadecimal")

    def test_identifiants_distincts(self):
        t, ligne = self.lignes[1]
        id0 = self.lignes[0][1].split(" ; ")[0][len("case : "):]
        id1 = ligne.split(" ; ")[0][len("case : "):]
        self.assertEqual(self.refus(self.plante(1, ligne.replace(id1, id0, 1))), "identifiant en double")

    def test_borne_en_octets(self):
        t, ligne = self.lignes[2]
        self.assertEqual(self.refus(self.plante(2, ligne + "x" * 300)), "borne en octets")

    def test_separateur(self):
        t, ligne = self.lignes[2]
        self.assertEqual(self.refus(self.plante(2, ligne.replace(" ; ", " | "))), "forme")


class TestC1(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.sortie = A.sortie_factice()

    def test_cas_sain(self):
        self.assertTrue(all(tn.controles_c1(self.sortie).values()))
        self.assertEqual(self.sortie["controles_C1"], tn.controles_c1(self.sortie))

    def test_case_servie_deux_fois(self):
        s = copy.deepcopy(self.sortie)
        s["generations"]["2"][0] = s["generations"]["1"][0]
        with self.assertRaises(tn.ControleC1Echoue) as c:
            tn.controles_c1(s)
        self.assertIn("aucune_case_servie_deux_fois", str(c.exception))

    def test_trente_deux_cases(self):
        s = copy.deepcopy(self.sortie)
        s["generations"]["3"].pop()
        with self.assertRaises(tn.ControleC1Echoue) as c:
            tn.controles_c1(s)
        self.assertIn("trente_trois_cases_servies", str(c.exception))

    def test_case_de_la_famille_servie(self):
        s = copy.deepcopy(self.sortie)
        s["generations"]["3"][0]["triplet"] = list(s["famille_tenue_a_l_ecart"]["cases"][0])
        with self.assertRaises(tn.ControleC1Echoue) as c:
            tn.controles_c1(s)
        self.assertIn("aucune_case_de_la_famille_tenue_a_l_ecart_servie", str(c.exception))


class TestArretDisjonction(unittest.TestCase):
    """Arrêt n° 10, premier temps : la garde, rejouée contre une copie du tirage où une case est plantée."""

    @classmethod
    def setUpClass(cls):
        cls.sortie = A.sortie_factice()

    def refus(self, tirage, g, cases=None):
        with self.assertRaises(tn.ArretDisjonction) as c:
            tn.garde_disjonction(tirage, g, cases)
        self.assertEqual(c.exception.numero, 10)
        return c.exception.cause

    def test_cas_sain_trente_trois_cases_distinctes(self):
        for g in (1, 2, 3):
            self.assertEqual(tn.garde_disjonction(self.sortie, g), 11)
            cases = [c["triplet"] for c in self.sortie["generations"][str(g)]]
            self.assertEqual(tn.garde_disjonction(self.sortie, g, cases), 11)

    def test_case_de_la_famille_plantee(self):
        s = copy.deepcopy(self.sortie)
        s["generations"]["2"][4]["triplet"] = list(s["famille_tenue_a_l_ecart"]["cases"][3])
        self.assertEqual(self.refus(s, 2), "case de la famille tenue à l'écart")

    def test_case_deja_servie_plantee(self):
        s = copy.deepcopy(self.sortie)
        s["generations"]["3"][0]["triplet"] = list(s["generations"]["1"][6]["triplet"])
        self.assertEqual(self.refus(s, 3), "case déjà servie")

    def test_case_en_double_et_hors_des_120(self):
        s = copy.deepcopy(self.sortie)
        s["generations"]["1"][1]["triplet"] = list(s["generations"]["1"][0]["triplet"])
        self.assertEqual(self.refus(s, 1), "case en double")
        s = copy.deepcopy(self.sortie)
        s["generations"]["1"][1]["triplet"] = [9, 9, 9]
        self.assertEqual(self.refus(s, 1), "case hors des 120")

    def test_cases_a_servir_qui_ne_sont_pas_celles_du_tirage(self):
        cases = [c["triplet"] for c in self.sortie["generations"]["2"]]
        cases[0] = self.sortie["reserve"]["cases"][0]
        self.assertEqual(self.refus(self.sortie, 2, cases), "cases différentes du tirage scellé")


class TestClesDeLaCourse(unittest.TestCase):
    """Clés 12, 13 et 20, exposées pour la course."""

    def test_permutations_12_et_13(self):
        for g, cle in ((2, 12), (3, 13)):
            p = tn.permutation_registre(g, 25, racine=A.RACINE_FACTICE, racine_attendue=A.RACINE_FACTICE)
            self.assertEqual(p, [int(x) for x in rng(A.RACINE_FACTICE, cle).permutation(25)])
        with self.assertRaises(tn.TirageRefuse):
            tn.permutation_registre(1, 5, racine=A.RACINE_FACTICE, racine_attendue=A.RACINE_FACTICE)

    def test_part_anteriorite_20(self):
        self.assertEqual(tn.part_anteriorite(60, racine=A.RACINE_FACTICE, racine_attendue=A.RACINE_FACTICE),
                         list(range(60)))
        p = tn.part_anteriorite(150, racine=A.RACINE_FACTICE, racine_attendue=A.RACINE_FACTICE)
        self.assertEqual(p, [int(x) for x in rng(A.RACINE_FACTICE, 20).choice(150, size=60, replace=False)])
        self.assertEqual(len(set(p)), 60)


class TestProgramme(unittest.TestCase):
    """Le programme du tirage : aucune liste par défaut, aucune écriture par-dessus, gabarit à son empreinte écrite."""

    def test_liste_des_motifs_exigee(self):
        with tempfile.TemporaryDirectory() as d:
            with self.assertRaises(SystemExit):
                tn.main(["--gabarit", "g", "--sortie", os.path.join(d, "s"), "--manifeste", os.path.join(d, "m")])

    def test_sortie_existante_refusee(self):
        with tempfile.TemporaryDirectory() as d:
            s = os.path.join(d, "s.json")
            with open(s, "w") as f:
                f.write("")
            with self.assertRaises(tn.TirageRefuse):
                tn.main(["--gabarit", "g", "--liste-motifs", A.CHEMIN_LISTE_ESSAI, "--empreinte-liste-motifs",
                         A.EMPREINTE_LISTE_ESSAI, "--sortie", s, "--manifeste", os.path.join(d, "m")])

    def test_gabarit_d_une_autre_empreinte_refuse_sans_ecriture(self):
        with tempfile.TemporaryDirectory() as d:
            g = os.path.join(d, "gabarit-factice.md")
            with open(g, "wb") as f:
                f.write(A.GABARIT_FACTICE)
            s, m = os.path.join(d, "s.json"), os.path.join(d, "m.json")
            with self.assertRaises(tn.TirageRefuse) as c:
                tn.main(["--gabarit", g, "--liste-motifs", A.CHEMIN_LISTE_ESSAI, "--empreinte-liste-motifs",
                         A.EMPREINTE_LISTE_ESSAI, "--sortie", s, "--manifeste", m])
            self.assertIn("empreinte du gabarit", str(c.exception))
            self.assertFalse(os.path.exists(s) or os.path.exists(m))


if __name__ == "__main__":
    unittest.main()
