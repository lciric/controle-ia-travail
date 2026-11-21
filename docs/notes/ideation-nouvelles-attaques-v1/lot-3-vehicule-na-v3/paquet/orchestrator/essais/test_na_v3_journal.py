"""Essais du lot 3 du véhicule NA-1 : `pole/journal_na_v3.py`.

v3 (remplace `test_na_v2_journal`, `12666153…`, archivé sans modification) : des noms seuls changent, pour la v5 du lot 2 ;
aucun essai n'est ajouté, retiré ni changé.

Journal d'ajout seul, qui refuse une réécriture ; ligne « envoi » après la garde de motifs, avant l'envoi, un appel sans
ligne ne part pas ; requête journalisée et rejouée égale (dans ce processus et dans un autre) ; une requête changée d'un
octet après la journalisation refusée ; lignes « non envoyé » (texte trouvé au seul journal), « non lancé » et « refus
écrit », avec ce que rend un refus écrit par rôle. Données factices seules ; aucun réseau, aucune clé.
"""

import hashlib
import json
import os
import subprocess
import sys
import tempfile
import unittest

ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(ICI)
for _p in (ICI, RACINE):
    if _p not in sys.path:
        sys.path.insert(0, _p)

import aides_na_lot3_v3 as B  # noqa: E402
import aides_na_v4 as A  # noqa: E402
from pole import garde_motifs_na_v4 as gm  # noqa: E402
from pole import journal_na_v3 as jn  # noqa: E402
from pole import requete_na_v3 as rq  # noqa: E402

CLE = "cle-essai-a"


def sha(o):
    return hashlib.sha256(o).hexdigest()


def journal(nom="journal-requetes-essai.jsonl"):
    d = tempfile.mkdtemp(prefix="journal-na-essai-")
    return jn.JournalRequetes(d, nom)


def lire(j):
    with open(j.chemin, "rb") as f:
        return f.read()


def requete_avec_motif():
    s = B.synthese("Synthèse factice où la graine factice figure.\n".encode("utf-8"))
    return rq.assembler_proposeur(B.gabarit(), B.cases()["1"][0], s, 1)


class TestAjoutSeul(unittest.TestCase):

    def test_journal_neuf_dans_le_dossier_de_sortie(self):
        d = tempfile.mkdtemp()
        j = jn.JournalRequetes(d, "journal-g1.jsonl")
        self.assertEqual(lire(j), b"")
        with self.assertRaises(jn.JournalRefuse):
            jn.JournalRequetes(d, "journal-g1.jsonl")  # R12
        for nom in ("../dehors.jsonl", "sous/dossier.jsonl", "journal.txt", "", ".jsonl/.."):
            with self.assertRaises(jn.JournalRefuse):
                jn.JournalRequetes(d, nom)
        with self.assertRaises(jn.JournalRefuse):
            jn.JournalRequetes(os.path.join(d, "absent"), "journal.jsonl")

    def test_rangs_et_chainage(self):
        j = journal()
        for _ in range(3):
            j.journaliser_envoi(B.requete_generation_2(), A.garde_essai(), role="proposeur-essai", cle=CLE)
        lignes = jn.verifier_journal(j.chemin)
        self.assertEqual([l["rang"] for l in lignes], [1, 2, 3])
        brutes = lire(j).splitlines(keepends=True)
        self.assertEqual(lignes[0]["precedente"], jn.PRECEDENTE_INITIALE)
        self.assertEqual(lignes[1]["precedente"], sha(brutes[0]))
        self.assertEqual(lignes[2]["precedente"], sha(brutes[1]))

    def test_ajout_seul_les_octets_ecrits_ne_changent_pas(self):
        j = journal()
        j.journaliser_envoi(B.requete_generation_2(), A.garde_essai(), role="proposeur-essai", cle=CLE)
        avant = lire(j)
        j.journaliser_non_envoye(arret=12, role="juge-essai", generation=1, case="gaga", cle=CLE, clause="seconde")
        self.assertTrue(lire(j).startswith(avant))

    def ecrire_par_dessus(self, j, nouveau):
        with open(j.chemin, "wb") as f:
            f.write(nouveau)

    def test_reecriture_d_un_octet_refusee(self):
        j = journal()
        for _ in range(2):
            j.journaliser_envoi(B.requete_generation_2(), A.garde_essai(), role="proposeur-essai", cle=CLE)
        o = bytearray(lire(j))
        o[10] ^= 1
        self.ecrire_par_dessus(j, bytes(o))
        with self.assertRaises(jn.JournalReecrit):
            j.journaliser_non_envoye(arret=12, role="r", generation=1, case="gaga", cle=CLE)
        with self.assertRaises(jn.JournalReecrit):
            j.sceller()
        with self.assertRaises(jn.JournalReecrit):
            jn.verifier_journal(j.chemin)  # le chaînage de la ligne 2 est rompu

    def test_derniere_ligne_tenue_par_le_sceau(self):
        j = journal()
        j.journaliser_envoi(B.requete_generation_2(), A.garde_essai(), role="proposeur-essai", cle=CLE)
        with self.assertRaises(jn.JournalReecrit):
            jn.verifier_journal(j.chemin, exiger_sceau=True)  # non scellé : refusé à qui exige le sceau
        j.sceller()
        self.assertEqual(len(jn.verifier_journal(j.chemin, exiger_sceau=True)), 1)
        o = bytearray(lire(j))
        o[10] ^= 1
        self.ecrire_par_dessus(j, bytes(o))
        with self.assertRaises(jn.JournalReecrit):
            jn.verifier_journal(j.chemin, exiger_sceau=True)

    def test_troncature_et_ajout_d_une_autre_main_refuses(self):
        for change in (lambda o: o[:-1], lambda o: o[:len(o) // 2], lambda o: b"",
                       lambda o: o + b'{"evenement": "envoi"}\n', lambda o: o.replace(b"proposeur-essai", b"proposeur-autre")):
            j = journal()
            j.journaliser_envoi(B.requete_generation_2(), A.garde_essai(), role="proposeur-essai", cle=CLE)
            self.ecrire_par_dessus(j, change(lire(j)))
            with self.assertRaises(jn.JournalReecrit):
                j.journaliser_envoi(B.requete_generation_2(), A.garde_essai(), role="proposeur-essai", cle=CLE)

    def test_ligne_recalculee_d_une_autre_main_vue_a_la_relecture(self):
        j = journal()
        for _ in range(2):
            j.journaliser_envoi(B.requete_generation_2(), A.garde_essai(), role="proposeur-essai", cle=CLE)
        lignes = [json.loads(l) for l in lire(j).splitlines()]
        lignes[0]["taille"] += 1
        self.ecrire_par_dessus(j, b"".join(jn._octets_de_ligne(l) for l in lignes))
        with self.assertRaises(jn.JournalReecrit):
            jn.verifier_journal(j.chemin)  # le chaînage de la ligne 2 est rompu

    def test_scelle_plus_aucun_ajout(self):
        j = journal()
        j.journaliser_envoi(B.requete_generation_2(), A.garde_essai(), role="proposeur-essai", cle=CLE)
        empreinte = j.sceller()
        self.assertEqual(empreinte, sha(lire(j)))
        with open(j.chemin + ".sha256", encoding="utf-8") as f:
            self.assertEqual(f.read(), f"{empreinte}  {os.path.basename(j.chemin)}\n")
        with self.assertRaises(jn.JournalScelle):
            j.journaliser_envoi(B.requete_generation_2(), A.garde_essai(), role="proposeur-essai", cle=CLE)
        with self.assertRaises(jn.JournalScelle):
            j.sceller()
        self.assertEqual(len(jn.verifier_journal(j.chemin)), 1)

    def test_compagnon_qui_ne_porte_pas_l_empreinte_refuse(self):
        j = journal()
        j.journaliser_envoi(B.requete_generation_2(), A.garde_essai(), role="proposeur-essai", cle=CLE)
        j.sceller()
        with open(j.chemin + ".sha256", "w", encoding="utf-8") as f:
            f.write("0" * 64 + "  x\n")
        with self.assertRaises(jn.JournalReecrit):
            jn.verifier_journal(j.chemin)

    def test_journal_coupe_au_milieu_d_une_ligne_refuse(self):
        j = journal()
        j.journaliser_envoi(B.requete_generation_2(), A.garde_essai(), role="proposeur-essai", cle=CLE)
        with open(j.chemin, "ab") as f:
            f.write(b'{"rang": 2')
        with self.assertRaises(jn.JournalReecrit):
            jn.verifier_journal(j.chemin)


class TestEnvoi(unittest.TestCase):

    def test_ligne_envoi_apres_la_garde_avant_l_envoi(self):
        j = journal()
        r = B.requete_generation_2()
        envoi = j.journaliser_envoi(r, A.garde_essai(), role="proposeur-essai", cle=CLE)
        (ligne,) = jn.verifier_journal(j.chemin)
        self.assertEqual(ligne["evenement"], "envoi")
        self.assertEqual((ligne["taille"], ligne["sha256"]), (r.taille, r.sha256))
        self.assertEqual((ligne["generation"], ligne["role"], ligne["case"], ligne["cle"], ligne["sorte"]),
                         (2, "proposeur-essai", r.identifiant_case, CLE, "proposeur"))
        self.assertEqual(ligne["composition"], r.composition_en_lignes())
        self.assertEqual(envoi.rang, 1)
        self.assertEqual(envoi.requete_gardee.sha256, ligne["sha256"])
        self.assertEqual(envoi.octets, r.octets)
        self.assertIs(type(envoi.octets), bytes)

    def test_aucun_contenu_dans_la_ligne_envoi(self):
        j = journal()
        r = B.requete_generation_2()
        j.journaliser_envoi(r, A.garde_essai(), role="proposeur-essai", cle=CLE)
        texte = lire(j).decode("utf-8")
        for fragment in ("Synthèse factice", "ligne factice une", "Texte factice", B.TITRE_REGISTRE_FACTICE):
            self.assertNotIn(fragment, texte)

    def test_le_lot_4_rejoue_l_egalite_sur_les_octets_remis(self):
        j = journal()
        envoi = j.journaliser_envoi(B.requete_generation_2(), A.garde_essai(), role="proposeur-essai", cle=CLE)
        gm.verifier_avant_envoi(envoi.requete_gardee, envoi.octets)
        chaine = envoi.chaine_pour_le_noyau()
        self.assertEqual(chaine.encode("utf-8"), envoi.octets)

    def test_requete_changee_d_un_octet_apres_la_journalisation_refusee(self):
        j = journal()
        envoi = j.journaliser_envoi(B.requete_generation_2(), A.garde_essai(), role="proposeur-essai", cle=CLE)
        (ligne,) = jn.verifier_journal(j.chemin)
        change = bytearray(envoi.octets)
        change[-1] ^= 1
        with self.assertRaises(gm.EcartApresGarde):
            gm.verifier_avant_envoi(envoi.requete_gardee, bytes(change))
        with self.assertRaises(gm.EcartApresGarde):
            gm.verifier_avant_envoi(envoi.requete_gardee, envoi.octets + b" ")
        r2 = B.requete_generation_2()
        s = B.synthese(A.SYNTHESE_FACTICE[:-1] + b"!")
        autre = rq.assembler_proposeur(B.gabarit(), B.cases()["2"][0], s, 2, B.registre(), B.TITRE_REGISTRE_FACTICE)
        self.assertTrue(jn.verifier_rejeu(ligne, r2))
        with self.assertRaises(jn.RejeuDifferent):
            jn.verifier_rejeu(ligne, autre)

    def test_requete_rejouee_egale_depuis_les_pieces_relues(self):
        d = tempfile.mkdtemp()
        chemins = {}
        for nom, octets in (("gabarit.md", A.GABARIT_FACTICE), ("synthese.md", A.SYNTHESE_FACTICE),
                            ("registre.txt", B.REGISTRE_FACTICE)):
            chemins[nom] = os.path.join(d, nom)
            with open(chemins[nom], "wb") as f:
                f.write(octets)
        j = journal()
        j.journaliser_envoi(B.requete_generation_2(), A.garde_essai(), role="proposeur-essai", cle=CLE)
        (ligne,) = jn.verifier_journal(j.chemin)
        g = rq.lire_gabarit(chemins["gabarit.md"], A.EMPREINTE_GABARIT_FACTICE)
        s = rq.lire_piece("synthèse servie", chemins["synthese.md"], sha(A.SYNTHESE_FACTICE))
        reg = rq.lire_piece("registre servi", chemins["registre.txt"], sha(B.REGISTRE_FACTICE))
        c = rq.cases_du_tirage(A.sortie_factice(), g)["2"][0]
        rejouee = rq.assembler_proposeur(g, c, s, 2, reg, B.TITRE_REGISTRE_FACTICE)
        self.assertTrue(jn.verifier_rejeu(ligne, rejouee))

    def test_requete_rejouee_egale_dans_un_autre_processus(self):
        j = journal()
        j.journaliser_envoi(B.requete_generation_2(), A.garde_essai(), role="proposeur-essai", cle=CLE)
        (ligne,) = jn.verifier_journal(j.chemin)
        sortie = os.path.join(tempfile.mkdtemp(), "requete-rejouee.bin")
        env = {"PATH": os.environ.get("PATH", ""), "PYTHONDONTWRITEBYTECODE": "1", "LANG": "C.UTF-8",
               "PYTHONHASHSEED": "12345"}
        r = subprocess.run([sys.executable, "-B", os.path.join(ICI, "aides_na_lot3_v3.py"), sortie], env=env,
                           capture_output=True, text=True)
        self.assertEqual(r.returncode, 0, r.stderr[-400:])
        with open(sortie, "rb") as f:
            octets = f.read()
        self.assertEqual((sha(octets), len(octets)), (ligne["sha256"], ligne["taille"]))

    def test_refus_de_la_garde_ligne_non_envoye_et_texte_au_seul_journal(self):
        j = journal()
        r = requete_avec_motif()
        with self.assertRaises(gm.ArretMotifInterdit) as c:
            j.journaliser_envoi(r, A.garde_essai(), role="proposeur-essai", cle=CLE)
        e = c.exception
        for vue in (str(e), repr(e), repr(e.args)):
            self.assertNotIn("graine factice", vue)
        (ligne,) = jn.verifier_journal(j.chemin)
        self.assertEqual(ligne["evenement"], "non envoyé")
        self.assertEqual((ligne["arret"], ligne["famille"], ligne["rang_motif"], ligne["texte_trouve"]),
                         (16, "composition et tenue", 1, "graine factice"))
        self.assertEqual((ligne["cle"], ligne["cout_usd"], ligne["sha256"], ligne["taille"]), (CLE, 0.0, r.sha256, r.taille))
        self.assertIn("graine factice", lire(j).decode("utf-8"))

    def test_un_appel_sans_ligne_ne_part_pas(self):
        j = journal()
        j.sceller()
        with self.assertRaises(jn.JournalScelle):
            j.journaliser_envoi(B.requete_generation_2(), A.garde_essai(), role="proposeur-essai", cle=CLE)
        j2 = journal()
        j2.journaliser_envoi(B.requete_generation_2(), A.garde_essai(), role="proposeur-essai", cle=CLE)
        with open(j2.chemin, "ab") as f:
            f.write(b"\n")
        rendu = None
        with self.assertRaises(jn.JournalReecrit):
            rendu = j2.journaliser_envoi(B.requete_generation_2(), A.garde_essai(), role="proposeur-essai", cle=CLE)
        self.assertIsNone(rendu)

    def test_garde_du_lot_2_exigee(self):
        j = journal()

        class Passoire:
            def garder_requete(self, octets):
                return gm.RequeteGardee(bytes(octets), sha(bytes(octets)), len(octets))

        with self.assertRaises(jn.LigneRefusee):
            j.journaliser_envoi(requete_avec_motif(), Passoire(), role="proposeur-essai", cle=CLE)
        self.assertEqual(lire(j), b"")

    def test_garde_qui_lit_d_autres_octets_rien_ne_part(self):
        j = journal()

        class GardeDecalee(gm.GardeMotifs):
            def garder_requete(self, requete):
                autre = bytes(requete) + b" "
                return gm.RequeteGardee(autre, sha(autre), len(autre))

        with self.assertRaises(jn.EcartGardeRequete):
            j.journaliser_envoi(B.requete_generation_2(), GardeDecalee(A.liste_essai()), role="proposeur-essai", cle=CLE)
        self.assertEqual(lire(j), b"")

    def test_seule_une_requete_assemblee_se_journalise(self):
        j = journal()
        for faux in (B.requete_generation_2().octets, None):
            with self.assertRaises(jn.LigneRefusee):
                j.journaliser_envoi(faux, A.garde_essai(), role="proposeur-essai", cle=CLE)
        for role, cle in (("", CLE), ("r", ""), (None, CLE)):
            with self.assertRaises(jn.LigneRefusee):
                j.journaliser_envoi(B.requete_generation_2(), A.garde_essai(), role=role, cle=cle)
        self.assertEqual(lire(j), b"")


class TestNonEnvoyeEtNonLance(unittest.TestCase):

    def test_non_envoye_arret_12_cout_nul(self):
        j = journal()
        ligne = j.journaliser_non_envoye(arret=12, role="juge-essai", generation=2, case="gaga", cle=CLE, clause="seconde")
        self.assertEqual((ligne["evenement"], ligne["arret"], ligne["cout_usd"], ligne["clause"]),
                         ("non envoyé", 12, 0.0, "seconde"))

    def test_non_envoye_liste_fermee_et_formes(self):
        j = journal()
        with self.assertRaises(jn.LigneRefusee):
            j.journaliser_non_envoye(arret=12, role="r", generation=1, case="gaga", cle=CLE, contenu="libre")
        with self.assertRaises(jn.LigneRefusee):
            j.journaliser_non_envoye(arret=12, role="r", generation=1, case="gaga", cle=CLE, rang=7)
        for arret in (0, -1, None, "", 1.5):
            with self.assertRaises(jn.LigneRefusee):
                j.journaliser_non_envoye(arret=arret, role="r", generation=1, case="gaga", cle=CLE)
        for g in (0, 4, "1"):
            with self.assertRaises(jn.LigneRefusee):
                j.journaliser_non_envoye(arret=12, role="r", generation=g, case="gaga", cle=CLE)
        self.assertEqual(lire(j), b"")
        ligne = j.journaliser_non_envoye(arret="arrêt de la colonne", role="r", generation=None, case="", cle=CLE)
        self.assertEqual(ligne["arret"], "arrêt de la colonne")

    def test_non_lance_renvoie_a_sa_ligne_envoi(self):
        j = journal()
        envoi = j.journaliser_envoi(B.requete_generation_2(), A.garde_essai(), role="proposeur-essai", cle=CLE)
        ligne = j.journaliser_non_lance(envoi)
        self.assertEqual((ligne["evenement"], ligne["envoi_rang"], ligne["envoi_sha256"], ligne["cout_usd"]),
                         ("non lancé", 1, envoi.requete_gardee.sha256, 0.0))
        self.assertEqual(ligne["cause"], jn.CAUSE_NON_LANCE)
        with self.assertRaises(jn.LigneRefusee):
            j.journaliser_non_lance(envoi)

    def test_non_lance_d_un_autre_journal_refuse(self):
        j1, j2 = journal(), journal()
        envoi = j1.journaliser_envoi(B.requete_generation_2(), A.garde_essai(), role="proposeur-essai", cle=CLE)
        with self.assertRaises(jn.LigneRefusee):
            j2.journaliser_non_lance(envoi)
        with self.assertRaises(jn.LigneRefusee):
            j2.journaliser_non_lance("pas un envoi")
        self.assertEqual(lire(j2), b"")


class TestRefusEcrit(unittest.TestCase):

    def test_ce_que_rend_un_refus_ecrit_par_role(self):
        j = journal()
        attendus = {
            "proposeur": ("rien", None, "cases non jouées", False),
            "portier_fiche": ("fiche au coffre", "au coffre", "au coffre par refus du portier", True),
            "portier_reponse_sans_fiche": ("réponse classée", "réponse illisible", "étiquette du portier illisible",
                                           False),
            "juge": ("verdict absent", "passée", "verdicts absents", False),
        }
        for sorte, (rendu, classe, compte, fiche_rendue) in attendus.items():
            r = j.journaliser_refus_ecrit(sorte=sorte, role=f"{sorte}-essai", generation=1, case="gaga",
                                          garde="A3, échecs consécutifs", cause="rôle marqué arrêté par l'essai")
            self.assertEqual((r.rendu, r.classe, r.compte, r.fiche_rendue), (rendu, classe, compte, fiche_rendue))
        lignes = jn.verifier_journal(j.chemin)
        self.assertEqual([l["evenement"] for l in lignes], ["refus écrit"] * 4)
        self.assertTrue(all(l["cout_usd"] == 0.0 for l in lignes))
        self.assertEqual(lignes[1]["classe"], "au coffre")
        self.assertTrue(jn.RENDUS_REFUS_ECRIT["portier_reponse_sans_fiche"]["appel_compte_m6"])
        self.assertFalse(jn.RENDUS_REFUS_ECRIT["proposeur"]["appel_compte_m6"])

    def test_sorte_inconnue_ou_champ_vide_refuse(self):
        j = journal()
        with self.assertRaises(jn.LigneRefusee):
            j.journaliser_refus_ecrit(sorte="aiguilleur", role="r", generation=1, case="gaga", garde="g", cause="c")
        with self.assertRaises(jn.LigneRefusee):
            j.journaliser_refus_ecrit(sorte="juge", role="r", generation=1, case="gaga", garde="", cause="c")
        with self.assertRaises(jn.LigneRefusee):
            j.journaliser_refus_ecrit(sorte="juge", role="r", generation=1, case="gaga", garde="g", cause="")
        self.assertEqual(lire(j), b"")

    def test_comptes(self):
        j = journal()
        envoi = j.journaliser_envoi(B.requete_generation_2(), A.garde_essai(), role="proposeur-essai", cle=CLE)
        j.journaliser_non_lance(envoi)
        j.journaliser_non_envoye(arret=12, role="juge-essai", generation=1, case="gaga", cle=CLE)
        j.journaliser_non_envoye(arret=12, role="juge-essai", generation=1, case="gaga", cle=CLE)
        try:
            j.journaliser_envoi(requete_avec_motif(), A.garde_essai(), role="proposeur-essai", cle=CLE)
        except gm.ArretMotifInterdit:
            pass
        j.journaliser_refus_ecrit(sorte="portier_fiche", role="portier-essai", generation=1, case="gaga",
                                  garde="A3, échecs consécutifs", cause="c")
        c = jn.comptes(jn.verifier_journal(j.chemin))
        self.assertEqual(c["envois"], {"proposeur-essai": 1})
        self.assertEqual(c["non_lances"], {"proposeur-essai": 1})
        self.assertEqual(c["non_envoyes"], {"juge-essai": {"12": 2}, "proposeur-essai": {"16": 1}})
        self.assertEqual(c["refus_ecrits"], {"portier-essai": {"A3, échecs consécutifs": 1}})
        self.assertEqual(c["refus_ecrits_par_compte"], {"au coffre par refus du portier": 1})


if __name__ == "__main__":
    unittest.main()
