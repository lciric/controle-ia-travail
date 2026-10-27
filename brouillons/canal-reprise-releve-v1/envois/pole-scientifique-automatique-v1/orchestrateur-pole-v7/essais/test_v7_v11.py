"""Essais de la version 11 de v7 : corrections de la contre-lecture du code écrit sous Opus (C1 à C6, C9, C10)."""

import math
import os
import random
import sys
import unittest

from essais.aides import CasAvecDossier, fiche
from essais.test_memoire_v4 import VRAIE, issue_testee
from essais.test_v6_relais_reel import JETON_FACTICE  # noqa: F401 (import de contrôle : le relais reste testé ailleurs)
from pole import selection_pari as sp
from pole.adaptateurs import construire_options, lectures_interdites_par_defaut
from pole.cycle import Generation, appliquer_multiplicite
from pole.memoire import Memoire
from pole.relais_reel import CHEMINS_PERMIS, CHEMINS_REFUSES

RELAIS = "http://127.0.0.1:8765/v1"


class BacASableLectures(CasAvecDossier):
    """C6 : le bac à sable borne désormais les lectures (par défaut : le dossier de la course) et échoue dur s'il manque."""

    def test_lectures_interdites_par_defaut_et_echec_dur(self):
        dossier = os.path.join(self.tmp, "G0-F01", "experience")
        os.makedirs(dossier)
        o = construire_options(dossier, 1.0, 5, url_relais=RELAIS)
        s = o["sandbox"]
        self.assertTrue(s["failIfUnavailable"])
        self.assertEqual(s["filesystem"]["denyRead"], [os.path.normpath(self.tmp)])
        self.assertEqual(s["filesystem"]["allowRead"], [os.path.normpath(dossier)])
        self.assertEqual(s["filesystem"]["denyWrite"], [os.path.normpath(self.tmp)])
        self.assertEqual(s["filesystem"]["allowWrite"], [os.path.normpath(dossier)])
        self.assertEqual(lectures_interdites_par_defaut(dossier), [os.path.normpath(self.tmp)])

    def test_interdits_explicites_et_dossier_hors_interdits_refuse(self):
        dossier = os.path.join(self.tmp, "course", "G0-F01", "experience")
        os.makedirs(dossier)
        banque = os.path.join(self.tmp, "banque")
        o = construire_options(dossier, 1.0, 5, url_relais=RELAIS,
                               interdire_lecture=[os.path.join(self.tmp, "course"), banque])
        self.assertEqual(o["sandbox"]["filesystem"]["denyRead"], [os.path.join(self.tmp, "course"), banque])
        for interdits in ([], ["relatif"], [banque]):  # vide, relatif, ou ne couvrant pas le dossier de l'agent
            with self.subTest(interdits=interdits), self.assertRaises(ValueError):
                construire_options(dossier, 1.0, 5, url_relais=RELAIS, interdire_lecture=interdits)


class ReservationParRole(unittest.TestCase):
    """C1 : un rôle simulé d'un adaptateur mixte ne réserve rien ; la simulation pure réserve le plafond."""

    def test_reserve_suit_le_role_effectif(self):
        class Stub:
            pass

        class Mixte:
            roles_reels = frozenset(["proposeur"])

        g = Stub()
        g.adaptateur = Mixte()
        self.assertEqual(Generation._reserve_role(g, "experimentateur", 1.0), 0.0)
        self.assertEqual(Generation._reserve_role(g, "verificateur", 0.5), 0.0)
        self.assertEqual(Generation._reserve_role(g, "proposeur", 1.5), 1.5)
        g.adaptateur = Stub()  # simulation pure : pas de roles_reels
        self.assertEqual(Generation._reserve_role(g, "experimentateur", 1.0), 1.0)


class RegleEBHCorrigee(unittest.TestCase):
    """C5 : le filtre de marge agit avant le tri (e = 0), m est fixé avant les issues."""

    @staticmethod
    def issue(traj, marge=None):
        pari = {"trajectoire_log_w": traj}
        if marge is not None:
            pari["marge_atteinte"] = marge
        return {"verdict_final": "survit", "pari": pari}

    def test_fille_sans_marge_ne_compte_pas_dans_k_etoile(self):
        # m = 3 : seuils log(3/(0,05·k)) = 4,09 / 3,40 / 3,00 pour k = 1, 2, 3.
        # F1 (fille, marge non atteinte) à 4,1 et N1 (nulle) à 3,6 : avec l'ancienne règle, k* = 2 retenait {F1, N1} puis
        # F1 était rétrogradée après coup : N1 promue grâce à une fille filtrée. Corrigé : F1 vaut e = 0, k* = 0.
        issues = {"F1": self.issue([4.1], marge=False), "N1": self.issue([3.6]), "N2": self.issue([0.1])}
        r = appliquer_multiplicite(issues, 0.05)
        self.assertEqual(r["retenues"], [])
        self.assertEqual(issues["N1"]["verdict_final"], "eliminee")
        self.assertIsNone(issues["F1"]["pari"]["multiplicite"]["log_e"])
        # avec la marge atteinte, F1 est bien retenue, et N1 avec elle (k* = 2)
        issues = {"F1": self.issue([4.1], marge=True), "N1": self.issue([3.6]), "N2": self.issue([0.1])}
        r = appliquer_multiplicite(issues, 0.05)
        self.assertEqual(sorted(r["retenues"]), ["F1", "N1"])

    def test_m_fixe_avant_les_issues(self):
        issues = {"F1": self.issue([4.0])}
        self.assertEqual(appliquer_multiplicite(dict(issues), 0.05)["m"], 1)
        r = appliquer_multiplicite(dict(issues), 0.05, m_fixe=5)  # quatre fiches non jugées (e = 0) comptent dans m
        self.assertEqual(r["m"], 5)
        self.assertEqual(r["retenues"], [])  # log(5/0,05) = 4,6 > 4,0
        with self.assertRaises(ValueError):
            appliquer_multiplicite(dict(issues), 0.05, m_fixe=0)


class SignatureAvecMoniteur(unittest.TestCase):
    """C4 : la même loi sur deux moniteurs ne partage ni classe ni héritage ; la transposition de moniteur est jugeable."""

    def test_meme_loi_autre_moniteur_autre_classe(self):
        rng = random.Random(4)
        a = sp.loi_softmax_aleatoire(rng, force=1.5)
        m = Memoire(graine=1)
        def fp(ident, moniteur):
            return fiche(ident, enonce=VRAIE, loi_predictive=a, severite_attendue=0.05, seuil=20.0,
                         espace_instances={"nombre_issues": 3, "dimension": 2, "moniteur": moniteur})
        f1 = fp("F1", "M0")
        f1.statut = "eliminee"
        m.indexer(f1, issue_testee(2.0), 0)
        meme, autre = fp("F2", "M0"), fp("F3", "M1")
        self.assertEqual(m.chercher_classe(meme)[0], "F1")
        self.assertIsNone(m.chercher_classe(autre)[0])
        self.assertTrue(math.isinf(Memoire.divergence_moyenne(m.signature(meme), m.signature(autre))))
        m.nouvelle_generation()
        self.assertTrue(m.garde_redite(autre)["accepte"])
        self.assertIsNone(m.heritage("F3"))  # aucun héritage d'un autre moniteur


class RelaisCheminsV11(unittest.TestCase):
    """C10 : seuls les messages sont relayés ; les lots (`batches`) sont refusés."""

    def test_chemins(self):
        self.assertEqual(CHEMINS_PERMIS, ("/v1/messages",))
        self.assertIn("/v1/messages/batches", CHEMINS_REFUSES)
        permis = lambda c: c.startswith(CHEMINS_PERMIS) and not c.startswith(CHEMINS_REFUSES)  # noqa: E731
        self.assertTrue(permis("/v1/messages"))
        self.assertTrue(permis("/v1/messages?beta=true"))
        self.assertFalse(permis("/v1/messages/batches"))
        self.assertFalse(permis("/v1/complete"))
        self.assertFalse(permis("/v1/"))


class SousPopulationParDefaut(unittest.TestCase):
    """C10 : le chercheur mécanique donne une loi par défaut à `par_sous_population` ; une sous-population absente du
    développement est évaluée sans erreur."""

    def test_defaut_present_et_evaluable(self):
        import os
        import tempfile
        from essais.aides import BASE
        from exemples.generer_monde_grammaire_v1 import generer_monde
        from pole.monde_banque import MondeBanque
        from pole.outils import ecrire_json_scelle
        from pole.proposeurs_references import propositions_mecaniques
        os.makedirs(BASE, exist_ok=True)
        tmp = tempfile.mkdtemp(dir=BASE)
        banque, _, _ = generer_monde(20261103, structures=["sous_population", "sous_population", "monotone"])
        chemin = os.path.join(tmp, "banque.json")
        ecrire_json_scelle(chemin, banque)
        monde = MondeBanque(chemin, 3)
        props = propositions_mecaniques(monde.description_publique(), monde.donnees_developpement(), 12)
        vues = 0
        for p in props:
            loi = p.get("loi_predictive")
            if isinstance(loi, dict) and loi.get("type") == "par_sous_population":
                vues += 1
                self.assertIn("defaut", loi)
                self.assertIsNotNone(loi["defaut"])
                table = sp.proba(loi, {"z": [0.1, -0.2, 0.3, 0.0], "g": 999}, [], 0)  # sous-population jamais vue
                self.assertAlmostEqual(sum(table), 1.0, places=6)
        self.assertGreater(vues, 0, "aucune loi par sous-population proposée par le chercheur mécanique sur ce monde")




class CanalDeTexteFiltre(unittest.TestCase):
    """C6 du socle : les leçons ne transportent ni issues recopiées ni vocabulaire du noyau."""

    def test_lignes_du_noyau_et_listes_de_nombres_retirees(self):
        from pole.memoire import Memoire, filtrer_canal_de_texte
        texte = ("Les lois sur deux traits semblent plus robustes.\n"
                 "Issues observées : 0, 1, 2, 2, 1, 0, 1, 2, 0, 1\n"
                 "log W cumulé de la classe : 3,42\n"
                 "La richesse finale a dépassé le seuil.\n"
                 "Préférer les softmax à force modérée (1 à 2).")
        propre = filtrer_canal_de_texte(texte)
        self.assertEqual(propre.splitlines(), ["Les lois sur deux traits semblent plus robustes.",
                                               "Préférer les softmax à force modérée (1 à 2)."])
        m = Memoire(graine=1)
        self.assertNotIn("log W", m.ajouter_lecon(0, texte))
        self.assertNotIn("Issues", m.texte_consigne("recombinaison"))


class VuePubliqueSansTemoin(unittest.TestCase):
    """C5 du socle : l'énoncé servi aux agents ne dit plus « Témoin vrai : »."""

    def test_prefixe_neutralise(self):
        f = fiche("T1", enonce="Témoin vrai : la loi exacte du moniteur M0 (monotone)", temoin="vraie")
        self.assertEqual(f.vue_publique()["enonce"], "la loi exacte du moniteur M0 (monotone)")
        self.assertNotIn("temoin", f.vue_publique())
        g = fiche("T2", enonce="Témoin faux : l'issue suivrait le trait de bruit", temoin="fausse")
        self.assertFalse(g.vue_publique()["enonce"].lower().startswith("témoin"))
        self.assertEqual(f.vue_complete_gelee()["enonce"], "Témoin vrai : la loi exacte du moniteur M0 (monotone)")


if __name__ == "__main__":
    unittest.main()
