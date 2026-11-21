"""Essais du lot 6 v3 du véhicule NA-1 (3/3 ; v3 : type exact, journaux hostiles des sondes du vérificateur, refus de
sceau du journal de la génération 1) : le refus de câblage (mot de la mère, GO-2026-11-21-69 ; mandat de reprise,
point 1). Au départ de la course et à la construction de chaque génération, le contexte d'appel est refusé si l'état de
la colonne est 1 ou 2 et que son journal n'est pas `JournalRequetesColonneNA`. Cas sains : état 1 et état 2 avec le journal
de la colonne, état 0 avec un journal ordinaire. Artefacts : états 1 et 2 avec un journal ordinaire, au départ et à la
génération 2 ; renforcement déclaré (journal de la colonne d'un autre état) ; état inconnu ; fabrique absente. Objet de
contrôle de ce que le refus protège : une ligne égale à une entrée de la colonne, plantée dans une requête de proposeur, part
avec le journal ordinaire et ne part pas avec celui de la colonne. Données factices seules ; aucune clé ; aucun appel."""

import hashlib
import os
import sys
import unittest

ICI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ICI)

import aides_na_lot6_v3 as A6  # noqa: E402
from aides_na_lot6_v3 import L10  # noqa: E402
from pole import course_na_v3 as cn  # noqa: E402
from pole import journal_na_v3 as jn  # noqa: E402
from pole import matiere_premiere_na_v1 as mp  # noqa: E402
from pole import requete_na_v3 as rq  # noqa: E402

DEPART = "départ de la course"


def capturer(liste):
    def f(g, gen):
        liste.append(gen)
    return f


def fabrique_etat_2(dossier):
    """Le journal de la colonne en état 2, toutes les conditions d'allumage d'essai du lot 10 a réunies."""
    return cn.fabrique_journal_colonne(L10.depart(2, conditions_allumage=L10.conditions(dossier)))


def montage(etat, fabrique):
    m = A6.Montage()
    m.etat_colonne = etat
    m.fabrique_journal = fabrique(m.dossier) if fabrique is fabrique_etat_2 else fabrique
    return m


class TestCablageSain(unittest.TestCase):
    """Cas sains : la course part et joue ses trois générations ; chaque génération reçoit un journal neuf de la fabrique."""

    def _course_complete(self, m, classe_attendue):
        gens = []
        bilan = m.lancer(crochets={"avant_execution": capturer(gens)})
        self.assertEqual([l["generation"] for l in bilan], [1, 2, 3])
        self.assertIsNone(m.bilan()["arret"])
        self.assertEqual(m.arrets(), [])
        self.assertEqual([type(gen.na.journal) for gen in gens], [classe_attendue] * 3)
        self.assertEqual(len({id(gen.na.journal) for gen in gens}), 3)
        depart = [l for l in m.journal_arrets() if l["evenement"] == "départ"][0]
        self.assertEqual(depart["depart"]["etat_colonne"], m.etat_colonne)
        for g in (1, 2, 3):
            jn.verifier_journal(m.chemin_sortie("journaux", f"journal-requetes-g{g}.jsonl"), exiger_sceau=True)
        return gens

    def test_etat_1_journal_de_la_colonne_depart(self):
        self._course_complete(montage(1, A6.fabrique_colonne(1)), mp.JournalRequetesColonneNA)

    def test_etat_2_journal_de_la_colonne_depart(self):
        self._course_complete(montage(2, fabrique_etat_2), mp.JournalRequetesColonneNA)

    def test_etat_0_journal_ordinaire_depart(self):
        self._course_complete(montage(0, A6.fabrique_ordinaire), jn.JournalRequetes)

    def test_etat_0_journal_de_la_colonne_eteinte_depart(self):
        self._course_complete(montage(0, A6.fabrique_colonne(0)), mp.JournalRequetesColonneNA)

    def test_refuser_cablage_rend_le_type_du_journal(self):
        m = A6.Montage()
        os.makedirs(m.sortie)
        self.assertEqual(cn.refuser_cablage(1, A6.fabrique_colonne(1)(m.sortie, "j1.jsonl"), DEPART),
                         "JournalRequetesColonneNA")
        self.assertEqual(cn.refuser_cablage(0, A6.fabrique_ordinaire(m.sortie, "j0.jsonl"), DEPART), "JournalRequetes")


class TestCablageRefuseAuDepart(unittest.TestCase):
    """Artefacts au départ de la course : l'arrêt est nommé, inscrit au journal des arrêts et des générations, au bilan ;
    aucun appel n'est parti ; le journal de la génération 1 est scellé vide ; aucune génération n'est écrite."""

    def _refus_au_depart(self, m, cause):
        with self.assertRaises(cn.ArretCablageColonneNA) as cm:
            m.lancer()
        e = cm.exception
        self.assertEqual(e.moment, DEPART)
        self.assertIn(cause, e.cause)
        arrets = m.arrets()
        self.assertEqual(len(arrets), 1)
        a = arrets[0]
        self.assertEqual(a["type"], "ArretCablageColonneNA")
        self.assertEqual(a["nom"], cn.ArretCablageColonneNA.nom)
        self.assertIsNone(a["numero"])
        self.assertEqual(a["moment"], DEPART)
        self.assertIsNone(a["generation"])
        self.assertEqual(m.bilan()["arret"]["type"], "ArretCablageColonneNA")
        self.assertEqual(m.bilan()["generations"], [])
        self.assertEqual(m.recus(), [])
        self.assertFalse(os.path.exists(m.chemin_sortie("generation-1")))
        lignes = jn.verifier_journal(m.chemin_sortie("journaux", "journal-requetes-g1.jsonl"), exiger_sceau=True)
        self.assertEqual(len(lignes), 0)
        self.assertEqual(sorted(os.listdir(m.chemin_sortie("journaux"))),
                         ["journal-requetes-g1.jsonl", "journal-requetes-g1.jsonl.sha256"])
        evts = [l["evenement"] for l in m.journal_arrets(exiger_sceau=True)]
        self.assertEqual(evts, ["départ", "copies de configuration", "arrêt", "clôture"])
        return a

    def test_etat_1_journal_ordinaire_refus_nomme(self):
        a = self._refus_au_depart(montage(1, A6.fabrique_ordinaire), "journal doit être celui de la colonne")
        self.assertEqual((a["etat_colonne"], a["type_journal"]), (1, "JournalRequetes"))

    def test_etat_2_journal_ordinaire_refus_nomme(self):
        a = self._refus_au_depart(montage(2, A6.fabrique_ordinaire), "journal doit être celui de la colonne")
        self.assertEqual((a["etat_colonne"], a["type_journal"]), (2, "JournalRequetes"))

    def test_renforcement_etat_1_journal_de_la_colonne_eteinte(self):
        self._refus_au_depart(montage(1, A6.fabrique_colonne(0)), "autre état")

    def test_renforcement_etat_2_journal_de_la_colonne_en_etat_1(self):
        self._refus_au_depart(montage(2, A6.fabrique_colonne(1)), "autre état")

    def test_renforcement_etat_1_journal_de_la_colonne_en_etat_2(self):
        m = A6.Montage()
        m.etat_colonne, m.fabrique_journal = 1, fabrique_etat_2(m.dossier)
        self._refus_au_depart(m, "autre état")

    def test_fabrique_qui_ne_rend_pas_un_journal(self):
        for etat in (0, 1):
            m = montage(etat, lambda d, n: object())
            with self.assertRaises(cn.ArretCablageColonneNA) as cm:
                m.lancer()
            self.assertEqual(cm.exception.moment, DEPART)
            self.assertIn("pas un journal des requêtes", cm.exception.cause)
            self.assertEqual(m.arrets()[0]["type_journal"], "object")
            self.assertEqual(m.recus(), [])
            self.assertEqual(os.listdir(m.chemin_sortie("journaux")), [])


class TestCablageRefuseAvantToutEcriture(unittest.TestCase):
    """Un état inconnu ou une fabrique absente : l'arrêt nommé, avant toute écriture (la sortie n'existe pas)."""

    def test_etats_inconnus(self):
        for etat in (3, -1, True, False, "1", 1.0, None):
            m = montage(etat, A6.fabrique_colonne(1))
            with self.assertRaises(cn.ArretCablageColonneNA) as cm:
                m.lancer()
            self.assertIn("état de l'interrupteur inconnu", cm.exception.cause)
            self.assertFalse(os.path.exists(m.sortie), repr(etat))

    def test_fabrique_absente(self):
        for f in (None, "fabrique", A6.fabrique_ordinaire(os.path.join(A6.Montage().dossier), "x.jsonl")):
            m = montage(1, f)
            with self.assertRaises(cn.ArretCablageColonneNA) as cm:
                m.lancer()
            self.assertIn("fabrique de journal absente", cm.exception.cause)
            self.assertFalse(os.path.exists(m.sortie))

    def test_sans_etat_ni_fabrique_la_course_ne_part_pas(self):
        m = A6.Montage()
        with self.assertRaises(TypeError):
            cn.executer_course_na_v3(m.config, m.sortie, m.adaptateurs, regime=A6.REGIME, nombre_generations=3,
                                     ligne_accord_usd=450.0, additif_sha256=A6.CE.additif_essai_sha256())
        self.assertFalse(os.path.exists(m.sortie))

    def test_fabrique_colonne_exige_le_controle_de_depart(self):
        for d in (None, 1, L10.depart(1).manifeste):
            with self.assertRaises(cn.DefautLot6):
                cn.fabrique_journal_colonne(d)


class TestCablageRefuseALaConstruction(unittest.TestCase):
    """Artefact à la construction d'une génération : la génération 1 joue avec le journal de la colonne ; la génération 2
    reçoit un journal ordinaire de la fabrique : refus nommé à sa construction, rien de la génération 2 n'est écrit, son
    journal est scellé vide ; la génération 1 est au bilan."""

    def _refus_a_la_generation_2(self, etat, fabrique_saine):
        m = A6.Montage()
        saine = fabrique_saine(m.dossier) if fabrique_saine is fabrique_etat_2 else fabrique_saine
        m.etat_colonne = etat
        m.fabrique_journal = A6.fabrique_par_generation({1: saine, 2: A6.fabrique_ordinaire, 3: saine})
        with self.assertRaises(cn.ArretCablageColonneNA) as cm:
            m.lancer()
        self.assertEqual(cm.exception.moment, "construction de la génération 2")
        a = m.arrets()[0]
        self.assertEqual((a["nom"], a["moment"], a["generation"], a["type_journal"]),
                         (cn.ArretCablageColonneNA.nom, "construction de la génération 2", 2, "JournalRequetes"))
        self.assertEqual([l["generation"] for l in m.bilan()["generations"]], [1])
        self.assertFalse(os.path.exists(m.chemin_sortie("generation-2")))
        self.assertEqual(len(jn.verifier_journal(m.chemin_sortie("journaux", "journal-requetes-g2.jsonl"),
                                                 exiger_sceau=True)), 0)
        self.assertFalse(os.path.exists(m.chemin_sortie("journaux", "journal-requetes-g3.jsonl")))

    def test_etat_1_journal_ordinaire_a_la_generation_2(self):
        self._refus_a_la_generation_2(1, A6.fabrique_colonne(1))

    def test_etat_2_journal_ordinaire_a_la_generation_2(self):
        self._refus_a_la_generation_2(2, fabrique_etat_2)

    def test_etat_0_journal_ordinaire_a_la_generation_2_part(self):
        m = A6.Montage()
        m.etat_colonne = 0
        m.fabrique_journal = A6.fabrique_par_generation({1: A6.fabrique_colonne(0), 2: A6.fabrique_ordinaire,
                                                         3: A6.fabrique_colonne(0)})
        self.assertEqual([l["generation"] for l in m.lancer()], [1, 2, 3])


class TestCeQueLeRefusProtege(unittest.TestCase):
    """Objet de contrôle : une ligne égale à une entrée du registre d'essai de la colonne, plantée en fin de synthèse dans
    la première requête de proposeur de la génération 1. Journal ordinaire (état 0) : elle part (une ligne « envoi » à son
    empreinte). Journal de la colonne (état 1) : elle ne part pas (arrêt de la garde de la colonne, une ligne « non
    envoyé », aucun envoi à son empreinte). C'est ce que le refus de câblage garantit en état 1 ou 2."""

    def _planter(self, vus):
        def f(g, gen):
            if g != 1:
                return
            cle = next(iter(gen.course_na.requetes))
            case = next(c for c in gen.course_na.cases if c.identifiant == cle[0])
            octets = gen.course_na.synthese.octets.rstrip(b"\n") + b"\n" + L10.enonce(0).encode("utf-8") + b"\n"
            synthese = rq.charger_piece(gen.course_na.synthese.nom, octets, hashlib.sha256(octets).hexdigest())
            r = rq.assembler_proposeur(gen.course_na.gabarit, case, synthese, 1)
            gen.course_na.requetes[cle] = r
            vus.append(r.sha256)
        return f

    def _envois(self, m):
        return [l["sha256"] for l in jn.verifier_journal(m.chemin_sortie("journaux", "journal-requetes-g1.jsonl"))
                if l["evenement"] == "envoi"]

    def test_journal_ordinaire_la_ligne_part(self):
        m, vus = montage(0, A6.fabrique_ordinaire), []
        m.lancer(crochets={"avant_execution": self._planter(vus)})
        self.assertIn(vus[0], self._envois(m))

    def test_journal_de_la_colonne_la_ligne_ne_part_pas(self):
        m, vus = montage(1, A6.fabrique_colonne(1)), []
        with self.assertRaises(mp.ArretColonneNA):
            m.lancer(crochets={"avant_execution": self._planter(vus)})
        self.assertNotIn(vus[0], self._envois(m))
        lignes = jn.verifier_journal(m.chemin_sortie("journaux", "journal-requetes-g1.jsonl"))
        self.assertEqual([l["arret"] for l in lignes if l["evenement"] == "non envoyé"], [mp.ARRET_COLONNE])
        self.assertEqual(m.arrets()[0]["nom"], "garde de la colonne « matière première »")


# --- v3 : journaux hostiles (sondes S0 à S8 de la vérification du lot 6 v2, reprises comme essais) -----------------------

class SurchargeEnvoi(mp.JournalRequetesColonneNA):
    """S1 : sous-classe du journal de la colonne qui surcharge l'envoi et ne garde rien."""

    def journaliser_envoi(self, requete, garde, *, role, cle):
        return jn.JournalRequetes.journaliser_envoi(self, requete, garde, role=role, cle=cle)


class SousClasseMuette(mp.JournalRequetesColonneNA):
    """Sous-classe qui ne surcharge rien : le type exact la refuse quand même (décision de la mère)."""


class ImitateurPlat:
    """S2 : imite l'interface sans hériter ; délègue à un journal ordinaire, porte un `depart` d'allure juste."""

    def __init__(self, reel, depart):
        object.__setattr__(self, "_reel", reel)
        object.__setattr__(self, "depart", depart)

    def __getattr__(self, nom):
        return getattr(object.__getattribute__(self, "_reel"), nom)


class ImitateurClasse(ImitateurPlat):
    """S3 : la même chose, qui se déclare de la classe du journal de la colonne par `__class__`."""

    @property
    def __class__(self):
        return mp.JournalRequetesColonneNA


class SousClasseLot3(jn.JournalRequetes):
    """S4 : hérite du journal du lot 3 seulement, porte un `depart` juste."""

    def __init__(self, dossier, nom, depart):
        super().__init__(dossier, nom)
        self.depart = depart


def envoi_sur_instance(depart):
    """Un journal de la colonne de type exact, dont l'envoi est remplacé sur l'instance."""
    def fabrique(dossier, nom):
        j = mp.JournalRequetesColonneNA(dossier, nom, depart=depart)
        j.journaliser_envoi = lambda requete, garde, *, role, cle: jn.JournalRequetes.journaliser_envoi(
            j, requete, garde, role=role, cle=cle)
        return j
    return fabrique


def departs(dossier):
    return {0: A6.depart_colonne(0), 1: A6.depart_colonne(1),
            2: L10.depart(2, conditions_allumage=L10.conditions(dossier))}


HOSTILES = {
    "S1 sous-classe qui surcharge l'envoi": lambda d: (lambda dos, n: SurchargeEnvoi(dos, n, depart=d)),
    "sous-classe muette": lambda d: (lambda dos, n: SousClasseMuette(dos, n, depart=d)),
    "S2 imitateur plat": lambda d: (lambda dos, n: ImitateurPlat(jn.JournalRequetes(dos, n), d)),
    "S3 imitateur qui falsifie __class__": lambda d: (lambda dos, n: ImitateurClasse(jn.JournalRequetes(dos, n), d)),
    "S4 sous-classe du lot 3, départ juste": lambda d: (lambda dos, n: SousClasseLot3(dos, n, d)),
    "envoi remplacé sur l'instance": envoi_sur_instance,
}


class TestCablageJournauxHostiles(unittest.TestCase):
    """Artefacts aux états 1 et 2 : chaque journal hostile est refusé au départ, par l'arrêt nommé, et la ligne plantée ne
    part pas (aucun envoi, aucune génération). Témoins : S0 (journal exact, la garde de la colonne arrête la ligne) ;
    état 0 inchangé (S5 journal ordinaire, S6 sous-classe qui surcharge l'envoi : la course part)."""

    def _jouer(self, etat, fabrique_de_depart):
        m = A6.Montage()
        m.etat_colonne = etat
        m.fabrique_journal = fabrique_de_depart(departs(m.dossier)[etat])
        vus = []
        return m, vus, TestCeQueLeRefusProtege()._planter(vus)

    def test_hostiles_refuses_aux_etats_1_et_2(self):
        for etat in (1, 2):
            for nom, fab in HOSTILES.items():
                with self.subTest(etat=etat, journal=nom):
                    m, vus, planter = self._jouer(etat, fab)
                    with self.assertRaises(cn.ArretCablageColonneNA) as cm:
                        m.lancer(crochets={"avant_execution": planter})
                    self.assertEqual(cm.exception.moment, DEPART)
                    a = m.arrets()[0]
                    self.assertEqual((a["nom"], a["moment"]), (cn.ArretCablageColonneNA.nom, DEPART))
                    self.assertEqual(vus, [])  # aucune génération construite : la ligne n'a pas même été plantée
                    self.assertEqual(m.recus(), [])
                    self.assertFalse(os.path.exists(m.chemin_sortie("generation-1")))

    def test_imitateur_de_classe_cause_type_exact(self):
        m, _, _ = self._jouer(1, HOSTILES["S3 imitateur qui falsifie __class__"])
        with self.assertRaises(cn.ArretCablageColonneNA) as cm:
            m.lancer()
        self.assertIn("type exact", cm.exception.cause)
        self.assertEqual(m.arrets()[0]["type_journal"], "ImitateurClasse")  # la classe réelle, non ce que dit `__class__`

    def test_envoi_remplace_sur_l_instance_cause_surcharge(self):
        m, _, _ = self._jouer(1, envoi_sur_instance)
        with self.assertRaises(cn.ArretCablageColonneNA) as cm:
            m.lancer()
        self.assertIn("surchargé", cm.exception.cause)

    def test_envoi_remplace_sur_la_classe_refuse(self):
        m = A6.Montage()
        os.makedirs(m.sortie)
        j = A6.fabrique_colonne(1)(m.sortie, "j1.jsonl")
        self.assertEqual(cn.refuser_cablage(1, j, DEPART), "JournalRequetesColonneNA")
        origine = mp.JournalRequetesColonneNA.__dict__["journaliser_envoi"]
        try:
            mp.JournalRequetesColonneNA.journaliser_envoi = lambda self, *a, **k: None
            with self.assertRaises(cn.ArretCablageColonneNA) as cm:
                cn.refuser_cablage(1, j, DEPART)
            self.assertIn("surchargé", cm.exception.cause)
        finally:
            mp.JournalRequetesColonneNA.journaliser_envoi = origine
        self.assertEqual(cn.refuser_cablage(1, j, DEPART), "JournalRequetesColonneNA")

    def test_temoin_s0_journal_exact_la_garde_arrete_la_ligne(self):
        m, vus, planter = self._jouer(1, lambda d: cn.fabrique_journal_colonne(d))
        with self.assertRaises(mp.ArretColonneNA):
            m.lancer(crochets={"avant_execution": planter})
        envois = [l["sha256"] for l in jn.verifier_journal(m.chemin_sortie("journaux", "journal-requetes-g1.jsonl"))
                  if l["evenement"] == "envoi"]
        self.assertNotIn(vus[0], envois)

    def test_etat_2_journal_exact_depart(self):
        m, _, _ = self._jouer(2, lambda d: cn.fabrique_journal_colonne(d))
        self.assertEqual([l["generation"] for l in m.lancer()], [1, 2, 3])

    def test_etat_0_inchange_s5_s6(self):
        for nom, fab in (("S5 journal ordinaire", lambda d: A6.fabrique_ordinaire),
                         ("S6 sous-classe qui surcharge l'envoi", HOSTILES["S1 sous-classe qui surcharge l'envoi"])):
            with self.subTest(journal=nom):
                m, _, _ = self._jouer(0, fab)
                self.assertEqual([l["generation"] for l in m.lancer()], [1, 2, 3])


class TestRefusDeSceauDuJournalG1(unittest.TestCase):
    """V10 : le journal de la génération 1, ouvert au départ, ne se scelle pas (fichier altéré) : le refus de sceau est dit
    à la ligne d'arrêt (`journal_requetes_g1`), jamais tu. Témoin : sans altération, la clé est absente."""

    def _refus(self, alterer):
        m = A6.Montage()
        m.etat_colonne = 1
        depart_0 = A6.depart_colonne(0)

        def fabrique(dossier, nom):
            j = mp.JournalRequetesColonneNA(dossier, nom, depart=depart_0)  # refusé au départ (renforcement E-1)
            if alterer:
                with open(j.chemin, "ab") as f:
                    f.write(b"octet plante\n")
            return j
        m.fabrique_journal = fabrique
        with self.assertRaises(cn.ArretCablageColonneNA):
            m.lancer()
        return m.arrets()[0], m.bilan()["arret"]

    def test_sceau_refuse_dit_a_la_ligne_d_arret(self):
        a, b = self._refus(True)
        self.assertEqual(a["journal_requetes_g1"], "scellement refusé (JournalReecrit)")
        self.assertEqual(b["journal_requetes_g1"], "scellement refusé (JournalReecrit)")

    def test_sans_alteration_la_cle_est_absente(self):
        a, _ = self._refus(False)
        self.assertNotIn("journal_requetes_g1", a)


if __name__ == "__main__":
    unittest.main()
