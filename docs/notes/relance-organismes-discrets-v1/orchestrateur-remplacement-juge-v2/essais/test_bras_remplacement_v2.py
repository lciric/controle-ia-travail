"""Essais du bras différé avec remplacement déclaré du modèle d'un juge externe (`pole/bras_remplacement_v2.py`).

Cas sain et artefacts (R5), sur une course simulée montée par les aides de `essais/test_v7_ideation_v2.py` :
remplacement déclaré admis (trois juges, manifeste et lecture marqués, auto-préférence au modèle joué) ; refus sans
remplacement, pour une autre étiquette, avec un modèle de la course faux, un modèle joué égal à celui de la course, une
ligne de GO mal formée, un mot vide, un champ en trop, un modèle donné différent du modèle déclaré ; le bras d'origine
refuse toujours le modèle changé ; jamais rejoué après dépense.
"""
import json
import os

import importlib.util

from essais.test_v7_ideation_v2 import FauxAdaptateur, TestCommandeExterne, TestV42, fiche_brute
from pole import bras_remplacement_v2 as brv
from pole import ideation_v2 as idn

COURSE, JOUE, GO = "autre-lignee-x", "autre-lignee-y", "GO-2026-11-18-99"


def decl(**ecarts):
    r = {"modele_course": COURSE, "modele_joue": JOUE, "go": GO, "mot": "go 6.2"}
    r.update(ecarts)
    return {"argon": r}


class TestBrasRemplacement(TestCommandeExterne):
    def monter(self, nom):
        from pole.adaptateurs import AdaptateurCommandeExterne
        c = self.cours()
        fiches = {"opus": [fiche_brute(nom="O1"), fiche_brute(nom="O2")], "fable": [fiche_brute(nom="F1")]}
        ad = FauxAdaptateur(fiches, notes_par_juge={"juge-fable": c.notes_temoins_ok, "juge-opus": c.notes_temoins_ok})
        externe = AdaptateurCommandeExterne(self.commande(self.SCRIPT_OK), environnement={})
        budgets = dict(c.budgets())
        budgets[("juge_ideation", COURSE)] = 1.0
        budgets[("juge_ideation", JOUE)] = 1.0
        res = c.lancer(ad, nom, budgets=budgets, juges_externes=[("argon", COURSE)], budget_externe_usd=2.0)
        self.assertTrue(res["en_attente_bras"])
        sortie = os.path.join(self.tmp, nom)
        att = self.attester(os.path.join(self.tmp, f"att-{nom}.json"), sortie)
        return sortie, att, budgets, externe

    def jouer(self, sortie, att, budgets, externe, remplacements, modele=JOUE):
        return brv.executer_bras_differe_avec_remplacement(
            sortie, remplacements_modele_juge=remplacements, attestation_lecture_humaine=att, budgets=budgets,
            juges_externes=[("argon", modele, externe)])

    def test_cas_sain_remplacement_declare(self):
        sortie, att, budgets, externe = self.monter("rx")
        apres = self.jouer(sortie, att, budgets, externe, decl())
        self.assertFalse(apres["sans_bras"])
        self.assertTrue(all(l["nombre_juges"] == 3 for l in apres["classement"]))
        with open(os.path.join(sortie, "manifeste-bras-rapporte.json"), encoding="utf-8") as f:
            m = json.load(f)["reglages"]
        self.assertEqual(m["remplacements_modele_juge"], decl())
        self.assertEqual(m["juges"][0][:2], ["argon", JOUE])
        with open(os.path.join(sortie, "lecture.json"), encoding="utf-8") as f:
            lecture = json.load(f)
        r = lecture["remplacement_modele_juge"]
        self.assertEqual(r["mention"], brv.MENTION_REMPLACEMENT)
        self.assertEqual(r["juges"], decl())
        self.assertIn("auto_preference_au_modele_de_la_course", r)
        self.assertEqual(lecture["auto_preference"]["argon"]["modele"], JOUE)
        self.assertEqual(r["auto_preference_au_modele_de_la_course"]["argon"]["modele"], COURSE)
        self.assertTrue(idn.verifier_scelle(os.path.join(sortie, "lecture.json")))
        with self.assertRaises(idn.CourseInterrompue):  # jamais rejoué après dépense
            self.jouer(sortie, att, budgets, externe, decl())

    def test_artefacts_refuses_avant_tout_appel(self):
        sortie, att, budgets, externe = self.monter("ra")
        cas = {
            "aucun remplacement": ({}, JOUE),
            "pas un dictionnaire": (None, JOUE),
            "autre étiquette": ({"astra": decl()["argon"]}, JOUE),
            "modèle de la course faux": (decl(modele_course="autre-lignee-z"), JOUE),
            "modèle joué égal à celui de la course": (decl(modele_joue=COURSE), COURSE),
            "ligne de GO mal formée": (decl(go="GO-2026-11-18"), JOUE),
            "ligne de GO vide": (decl(go=""), JOUE),
            "mot vide": (decl(mot=" "), JOUE),
            "champ en trop": ({"argon": dict(decl()["argon"], famille="x")}, JOUE),
            "champ manquant": ({"argon": {k: v for k, v in decl()["argon"].items() if k != "mot"}}, JOUE),
            "modèle donné ≠ modèle déclaré": (decl(), "autre-lignee-z"),
            "modèle de la course donné malgré le remplacement": (decl(), COURSE),
            "ligne de GO à chiffres non ASCII": (decl(go="GO-٢٠٢٦-١١-١٨-٠١"), JOUE),
        }
        for nom, (remplacements, modele) in cas.items():
            with self.subTest(nom), self.assertRaises(idn.CourseInterrompue):
                self.jouer(sortie, att, budgets, externe, remplacements, modele=modele)
        for nom in ("manifeste-bras-rapporte.json", "bras-rapporte-controle", "classement.json", "lecture.json"):
            self.assertFalse(os.path.exists(os.path.join(sortie, nom)), nom)
        with self.assertRaises(idn.CourseInterrompue):  # le bras d'origine refuse toujours le modèle changé
            idn.executer_bras_differe(sortie, attestation_lecture_humaine=att, budgets=budgets,
                                      juges_externes=[("argon", JOUE, externe)])
        with self.assertRaises(idn.CourseInterrompue):  # v2 (constat 1) : étiquette en double, avant tout appel
            brv.executer_bras_differe_avec_remplacement(
                sortie, remplacements_modele_juge=decl(), attestation_lecture_humaine=att, budgets=budgets,
                juges_externes=[("argon", "non-declare-z", externe), ("argon", JOUE, externe)])
        self.assertFalse(os.path.exists(os.path.join(sortie, "manifeste-bras-rapporte.json")))
        self.assertFalse(os.path.exists(os.path.join(sortie, "bras-rapporte-controle")))
        apres = self.jouer(sortie, att, budgets, externe, decl())  # la course reste jouable après les refus
        self.assertFalse(apres["sans_bras"])


class TestTentatives(TestBrasRemplacement):
    """v2 (constat 2) : une tentative payée avant tout envoi porte la déclaration du remplacement."""

    def test_tentative_payee_porte_le_remplacement(self):
        from pole.adaptateurs import AdaptateurCommandeExterne
        sortie, att, budgets, _ = self.monter("rt")
        ko = AdaptateurCommandeExterne(self.commande(
            "import sys, json\nsys.stdin.read()\nprint(json.dumps({'texte': 'KO', 'cout_usd': 0.05}))\n", "ko.py"), environnement={})
        with self.assertRaises(idn.CourseInterrompue):
            self.jouer(sortie, att, budgets, ko, decl())
        with open(os.path.join(sortie, "bras-tentative-1.json"), encoding="utf-8") as f:
            self.assertEqual(json.load(f)["reglages"]["remplacements_modele_juge"], decl())
        self.assertFalse(os.path.exists(os.path.join(sortie, "manifeste-bras-rapporte.json")))

    def test_jamais_rejoue_croise(self):
        sortie, att, budgets, externe = self.monter("rc")
        self.jouer(sortie, att, budgets, externe, decl())
        with self.assertRaises(idn.CourseInterrompue):
            idn.executer_bras_differe(sortie, attestation_lecture_humaine=att, budgets=budgets,
                                      juges_externes=[("argon", COURSE, externe)])

    test_cas_sain_remplacement_declare = None
    test_artefacts_refuses_avant_tout_appel = None


class TestLanceurV9(TestV42):
    """Bout en bout par la ligne de commande : course par le lanceur d'origine, bras par le lanceur v9."""

    REMPLACEMENT = ["--remplacement-modele-juge", "argon-j=gemini-argon=gemini-argon-2=GO-2026-11-18-99",
                    "--mot-remplacement", "argon-j=go 6.2"]

    def v9(self):
        ici = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "demonstrations", "ideation_v9.py")
        spec = importlib.util.spec_from_file_location("ideation_v9_essai", ici)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module

    def monter(self, nom):
        v41 = self.v41()
        prep = self.cours().preparer()
        sortie = os.path.join(self.tmp, nom)
        ok = " ".join(self.cmd().commande(self.cmd().SCRIPT_OK))
        code, out, err = v41.principal(v41.lanceur(), v41.base(sortie, prep, None, "--commande-externe", ok,
                                                                "--budget-externe-usd", "9"))
        self.assertEqual(code, 0, err)
        att = self.cmd().attester(os.path.join(self.tmp, f"att-{nom}.json"), sortie, "argon-j")
        bras = [sortie, "--bras-rapporte-differe", "--attestation-lecture-humaine", att, "--commande-externe", ok]
        return v41, sortie, bras

    def test_bras_par_le_lanceur_v9(self):
        v41, sortie, bras = self.monter("l9")
        v9 = self.v9()
        joue = ["--juge-externe", "argon-j=gemini-argon-2"]
        refus = {
            "sans le bras": [sortie] + joue + self.REMPLACEMENT,
            "juge donné au modèle de la course": bras + ["--juge-externe", "argon-j=gemini-argon"] + self.REMPLACEMENT,
            "mot manquant": bras + joue + self.REMPLACEMENT[:2],
            "mot sans remplacement": bras + joue + self.REMPLACEMENT[2:],
            "remplacement mal formé": bras + joue + ["--remplacement-modele-juge", "argon-j=gemini-argon-2", "--mot-remplacement",
                                                     "argon-j=go"],
            "modèle changé sans déclaration (lanceur v8)": bras + joue,
            "ligne de GO mal formée": bras + joue + ["--remplacement-modele-juge", "argon-j=gemini-argon=gemini-argon-2=GO-x",
                                                     "--mot-remplacement", "argon-j=go"],
            "juge externe donné deux fois": bras + ["--juge-externe", "argon-j=non-declare-z"] + joue + self.REMPLACEMENT,
            "même juge externe répété": bras + joue + joue + self.REMPLACEMENT,
        }
        for nom, argv in refus.items():
            with self.subTest(nom):
                code, out, err = v41.principal(v9, argv)
                self.assertEqual(code, 2, nom + " : " + err)
                self.assertIs(v9.lanceur_v2.idn, idn)  # cœur d'origine en place après chaque refus
        self.assertFalse(os.path.exists(os.path.join(sortie, "manifeste-bras-rapporte.json")))
        code, out, err = v41.principal(v9, bras + joue + self.REMPLACEMENT)
        self.assertIn(code, (0, 4), err)
        with open(os.path.join(sortie, "manifeste-bras-rapporte.json"), encoding="utf-8") as f:
            m = json.load(f)["reglages"]
        self.assertEqual(m["remplacements_modele_juge"], {"argon-j": {
            "modele_course": "gemini-argon", "modele_joue": "gemini-argon-2", "go": "GO-2026-11-18-99", "mot": "go 6.2"}})
        with open(os.path.join(sortie, "lecture.json"), encoding="utf-8") as f:
            lecture = json.load(f)
        self.assertEqual(lecture["remplacement_modele_juge"]["mention"], brv.MENTION_REMPLACEMENT)
        self.assertEqual(lecture["auto_preference"]["argon-j"]["modele"], "gemini-argon-2")
        self.assertEqual(lecture["auto_preference"]["argon-j"]["n_propre_modele"], 0)
        self.assertGreater(
            lecture["remplacement_modele_juge"]["auto_preference_au_modele_de_la_course"]["argon-j"]["n_propre_modele"], 0)
        self.assertIs(v9.lanceur_v2.idn, idn)  # le cœur d'origine est remis en place

    def test_sans_remplacement_le_lanceur_v9_est_le_v8(self):
        v41, sortie, bras = self.monter("l9b")
        code, out, err = v41.principal(self.v9(), bras + ["--juge-externe", "argon-j=gemini-argon"])
        self.assertIn(code, (0, 4), err)
        with open(os.path.join(sortie, "manifeste-bras-rapporte.json"), encoding="utf-8") as f:
            self.assertNotIn("remplacements_modele_juge", json.load(f)["reglages"])
        with open(os.path.join(sortie, "lecture.json"), encoding="utf-8") as f:
            self.assertNotIn("remplacement_modele_juge", json.load(f))


# seuls les essais de ce fichier : les essais hérités de la classe mère sont ceux de `test_v7_ideation_v2.py`
for _nom in [n for n in dir(TestCommandeExterne) if n.startswith("test_")]:
    setattr(TestBrasRemplacement, _nom, None)
for _nom in [n for n in dir(TestV42) if n.startswith("test_")]:
    setattr(TestLanceurV9, _nom, None)
del TestCommandeExterne, TestV42
