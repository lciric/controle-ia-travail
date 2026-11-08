"""Essais du script de lecture de l'épreuve « W2 gradué » (`demonstrations/lecture_epreuve_w2g_dose_v1.py`, fichier neuf, R12) :
chaque garde du texte (§ 6) sur un cas sain et sur au moins un artefact (R5), un essai par code de sortie, Wilson contre des
valeurs calculées à la main.

Cas sain : une **course de chaîne** réelle du script de l'épreuve (sous-processus, `python3 -I -B`), 2 répétitions, les 11 doses
de la grille gelée, `--processus 1`, `--duree-max-s 6300`, sous un texte factice scellé dans un dossier temporaire (≈ 20 s) ;
lue avec 2 répétitions et 1 processus attendus. Artefacts : copies de cette course modifiées puis **rescellées**, un dossier vide,
une console d'autre code, et les sorties exploratoires (si leur dossier de brouillon existe encore ; sinon l'essai est sauté et le
dit). Aucun réseau, aucune clé, aucun proposeur.

Usage (depuis `orchestrator/` d'une copie du dépôt public au commit 8947bc8, patch v5 appliqué) :
    python3 -B essais/test_lecture_epreuve_w2g_dose_v1.py
"""

import contextlib
import importlib.util
import io
import json
import math
import os
import shutil
import subprocess
import sys
import tempfile
import unittest

ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(ICI)
sys.path[:0] = [RACINE, ICI]

from pole import attaque_goodhart_v2 as ag  # noqa: E402
from pole import attaque_goodhart_v5 as a5  # noqa: E402
from pole.outils import ecrire_json_scelle, ecrire_scelle, sha256_fichier, verifier_scelle  # noqa: E402


def _charger(nom_fichier, nom):
    spec = importlib.util.spec_from_file_location(nom, os.path.join(RACINE, "demonstrations", nom_fichier))
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


lecteur = _charger("lecture_epreuve_w2g_dose_v1.py", "lecture_epreuve_w2g_dose_v1_essai")

# Sorties exploratoires (texte § 3) : dossiers de brouillon de la session ; empreintes des sorties relevées au texte.
BROUILLON = "/tmp/claude-0/-home-user/86976e6f-3fae-57b1-a905-26802f445363/scratchpad"
EXPLORATOIRES = {"epreuve-w2g-v1-a": "c85e59b3594050e6c7ce162721e42c19b55d890acd752ef39b268617b279b2b9",
                 "epreuve-w2g-v1-b": "a4821262e5b9507d4275c81050af2034b3f9bdb0364b97513d30bdf2cb56748e"}
Z = 1.959963984540054


_COMMUN = {}


def setUpModule():
    """Une seule course de chaîne pour tous les essais ; chaque artefact en est une copie rescellée."""
    tmp = tempfile.mkdtemp(prefix="lecture-w2g-")
    texte = os.path.join(tmp, "texte-factice-epreuve-w2g-v1.md")
    ecrire_scelle(texte, "Texte factice de la course de chaîne (essais du script de lecture) ; aucun chiffre lu.\n")
    chaine = os.path.join(tmp, "chaine")
    commande = [sys.executable, "-I", "-B", os.path.join("demonstrations", "epreuve_w2g_dose_v1.py"), chaine,
                "--entropie-texte", texte, "--repetitions", "2", "--processus", "1", "--duree-max-s", "6300"]
    p = subprocess.run(commande, cwd=RACINE, capture_output=True, text=True, timeout=600)
    console = os.path.join(tmp, "chaine-console.txt")
    ecrire_scelle(console, p.stdout + p.stderr + f"code {p.returncode}\n")
    _COMMUN.update(tmp=tmp, texte=texte, chaine=chaine, console=console, code_chaine=p.returncode, n=0)


def tearDownModule():
    shutil.rmtree(_COMMUN["tmp"], ignore_errors=True)


class Base(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        for k in ("tmp", "texte", "chaine", "console", "code_chaine"):
            setattr(cls, k, _COMMUN[k])

    def neuf(self, nom):
        _COMMUN["n"] += 1
        return os.path.join(self.tmp, f"{_COMMUN['n']:03d}-{nom}")

    def console_code(self, code):
        c = self.neuf("console.txt")
        ecrire_scelle(c, f"sortie factice\ncode {code}\n")
        return c

    def artefact(self, rapport=None, manifeste=None):
        """Copie de la course de chaîne ; `rapport(r)` et `manifeste(m)` modifient les JSON en place, puis rescellement."""
        d = self.neuf("sortie")
        shutil.copytree(self.chaine, d)
        for nom, f in (("epreuve-w2g-dose-v1.json", rapport), ("manifeste.json", manifeste)):
            if f is None:
                continue
            p = os.path.join(d, nom)
            with open(p, encoding="utf-8") as fh:
                o = json.load(fh)
            f(o)
            os.remove(p)
            os.remove(p + ".sha256")
            ecrire_json_scelle(p, o)
        return d

    def lire(self, dossier, console=None, texte=None, repetitions=2, processus=1, lecture=None, extra=()):
        lecture = lecture or self.neuf("lecture.json")
        argv = [dossier, "--texte", texte or self.texte, "--console", console or self.console, "--lecture", lecture,
                "--repetitions-attendues", str(repetitions), "--processus-attendus", str(processus), *extra]
        sortie, erreur = io.StringIO(), io.StringIO()
        with contextlib.redirect_stdout(sortie), contextlib.redirect_stderr(erreur):
            code = lecteur.principal(argv)
        contenu = None
        if os.path.isfile(lecture):
            self.assertTrue(verifier_scelle(lecture), "toute lecture écrite est scellée")
            with open(lecture, encoding="utf-8") as fh:
                contenu = json.load(fh)
        return code, contenu, sortie.getvalue() + erreur.getvalue()

    def refuse(self, dossier, garde, motif, **k):
        code, contenu, texte = self.lire(dossier, **k)
        self.assertEqual(code, lecteur.CODE_GARDE, texte)
        self.assertEqual(contenu["garde"], garde, texte)
        self.assertIn(motif, [m["motif"] for m in contenu["motifs"]], texte)
        self.assertNotIn("par_dose", contenu, "arrêt de garde : aucun chiffre écrit")
        self.assertNotIn("lambda_etoile", contenu)
        return contenu


def _ligne(r, dose, cle):
    return next(x for x in r["resultats"] if x["dose"] == dose)["lignes"][cle]


def _poser(r, dose, cle, promues):
    x = _ligne(r, dose, cle)
    x["promues"], x["taux"] = promues, promues / x["repetitions"]


# --- Wilson à la main -----------------------------------------------------------------------------------------------------------
class Wilson(unittest.TestCase):
    def test_wilson_egale_le_calcul_a_la_main(self):
        """Formes closes : x = 0 → [0 ; z²/(n + z²)] ; x = n → [n/(n + z²) ; 1] ; x = n/2 → ½ ± z/(2·√(n + z²)) ; et 809/1 000
        contre la table du texte (§ 3, [0,783 ; 0,832] à trois décimales)."""
        z2 = Z * Z
        for n in (2, 200, 1000):
            lo, hi = lecteur.wilson(0, n)
            self.assertAlmostEqual(lo, 0.0, places=15)
            self.assertAlmostEqual(hi, z2 / (n + z2), places=12)
            lo, hi = lecteur.wilson(n, n)
            self.assertAlmostEqual(lo, n / (n + z2), places=12)
            self.assertAlmostEqual(hi, 1.0, places=12)
        lo, hi = lecteur.wilson(500, 1000)
        demi = Z / (2 * math.sqrt(1000 + z2))
        self.assertAlmostEqual(lo, 0.5 - demi, places=12)
        self.assertAlmostEqual(hi, 0.5 + demi, places=12)
        self.assertAlmostEqual(demi, 0.0309304, places=7)  # calcul à la main : 1,959964 / (2 × 31,683457) = 1,959964 / 63,366914
        self.assertEqual([round(v, 3) for v in lecteur.wilson(809, 1000)], [0.783, 0.832])
        self.assertAlmostEqual(lecteur.wilson(0, 1000)[1], 0.0038268, places=7)  # 3,841459 / 1 003,841459 = 0,00382676
        self.assertEqual(lecteur.wilson(3, 7), list(ag.wilson(3, 7)), "le lecteur appelle attaque_goodhart_v2.wilson")


class RegleDeChoix(unittest.TestCase):
    def test_lambda_recalcule_regle_du_texte(self):
        def r(dose, a, b, n=1000, complete=True):
            return {"dose": dose, "complete": complete, "lignes": {"monde|v9": {"promues": a, "repetitions": n},
                                                                    "recombinaison|v9": {"promues": b, "repetitions": n}}}
        self.assertEqual(lecteur.lambda_recalcule([r(0.0, 0, 0), r(0.3, 799, 0), r(0.4, 800, 0), r(0.5, 900, 0)]), 0.4)
        self.assertIsNone(lecteur.lambda_recalcule([r(0.0, 1000, 0)]), "la dose 0 n'est jamais choisissable")
        self.assertEqual(lecteur.lambda_recalcule([r(0.4, 800, 1), r(0.5, 900, 0)]), 0.5, "(b) > 0 : la dose ne convient pas")
        self.assertIsNone(lecteur.lambda_recalcule([r(0.4, 1000, 0, complete=False)]))
        self.assertEqual(lecteur.lambda_recalcule([r(0.5, 2, 0, n=2), r(0.4, 1, 0, n=2)]), 0.5, "1/2 < 0,80 ; ordre indifférent")


# --- cas sain et codes ---------------------------------------------------------------------------------------------------------
class CasSainEtCodes(Base):
    def test_cas_sain_course_de_chaine(self):
        self.assertEqual(self.code_chaine, 0, "la course de chaîne est complète")
        with open(os.path.join(self.chaine, "epreuve-w2g-dose-v1.json"), encoding="utf-8") as fh:
            r = json.load(fh)
        lecture = self.neuf("lecture.json")
        code, contenu, texte = self.lire(self.chaine, lecture=lecture)
        attendu = lecteur.CODE_LAMBDA if r["dose_proposee_par_la_regle"] is not None else lecteur.CODE_AUCUNE_DOSE
        self.assertEqual(code, attendu, texte)
        self.assertEqual(contenu["gardes"], {str(i): "passée" for i in range(1, 7)})
        self.assertEqual(contenu["lambda_recalcule"], r["dose_proposee_par_la_regle"])
        self.assertEqual([d["dose"] for d in contenu["par_dose"]], list(a5.GRILLE_DOSES_W2G))
        for d, x in zip(contenu["par_dose"], r["resultats"]):
            for k in lecteur.LIGNES:
                self.assertEqual(d["lignes"][k]["wilson_95"], list(ag.wilson(x["lignes"][k]["promues"], 2)))
                self.assertEqual(d["lignes"][k]["clopper_pearson_95_imprime"], x["lignes"][k]["clopper_pearson_95"])
        self.assertEqual(contenu["pieces"]["texte"]["sha256"], sha256_fichier(self.texte))
        self.assertEqual(contenu["pieces"]["sortie"]["sha256"], sha256_fichier(os.path.join(self.chaine, "epreuve-w2g-dose-v1.json")))
        self.assertIn(contenu["table"], texte, "la lecture est imprimée")
        # refus d'écraser : même chemin → usage, fichier inchangé
        avant = sha256_fichier(lecture)
        code2, _, _ = self.lire(self.chaine, lecture=lecture)
        self.assertEqual(code2, lecteur.CODE_USAGE)
        self.assertEqual(sha256_fichier(lecture), avant)

    def test_code_0_lambda_lu(self):
        def f(r):
            for d in r["doses"]:
                if d > 0:
                    _poser(r, d, "monde|v9", 2 if d >= 0.10 else 1)
            r["dose_proposee_par_la_regle"] = 0.1
        code, contenu, texte = self.lire(self.artefact(f))
        self.assertEqual(code, 0, texte)
        self.assertEqual((contenu["lambda_etoile"], contenu["lambda_imprime_par_le_script"]), (0.1, 0.1))
        self.assertIn("à la limite", contenu["a_la_limite"]["mention"], "2/2 : borne basse de Wilson 0,34 < 0,80")
        self.assertIn(contenu["p10"]["mention"], ("P10 tenue par l'oracle", "P10 en tension à λ*"))
        self.assertIn("λ* = 0.1", texte)

    def test_code_3_aucune_dose(self):
        def f(r):
            for d in r["doses"]:
                _poser(r, d, "monde|v9", 1 if d > 0 else 0)  # 1/2 < 0,80 partout
            r["dose_proposee_par_la_regle"] = None
        code, contenu, texte = self.lire(self.artefact(f))
        self.assertEqual(code, 3, texte)
        self.assertIsNone(contenu["lambda_etoile"])
        self.assertIn("nœud de Lazar", contenu["statut"])

    def test_code_4_usage(self):
        sortie, erreur = io.StringIO(), io.StringIO()
        with contextlib.redirect_stdout(sortie), contextlib.redirect_stderr(erreur):
            self.assertEqual(lecteur.principal([self.chaine, "--console", self.console, "--lecture", self.neuf("l.json")]), 4)
            self.assertEqual(lecteur.principal([self.chaine, "--texte", self.texte, "--console", self.console,
                                                "--lecture", self.neuf("l.json"), "--repetitions-attendues", "0"]), 4)
            self.assertEqual(lecteur.principal([self.chaine, "--texte", self.texte, "--console", self.console,
                                                "--lecture", self.neuf("l.json"), "--repetitions-attendues", "deux"]), 4)
            dedans = os.path.join(self.chaine, "lecture.json")
            self.assertEqual(lecteur.principal([self.chaine, "--texte", self.texte, "--console", self.console, "--lecture", dedans]), 4)
            self.assertFalse(os.path.exists(dedans), "rien n'est écrit dans le dossier scellé")
            pris = self.neuf("l.json")
            ecrire_scelle(pris + ".sha256", "x\n")
            self.assertEqual(lecteur.principal([self.chaine, "--texte", self.texte, "--console", self.console, "--lecture", pris]), 4)
            self.assertFalse(os.path.exists(pris))

    def test_code_2_arret_de_garde(self):
        """Un arrêt de garde rend 2 et écrit une lecture sans chiffre (motif nommé)."""
        c = self.refuse(self.artefact(lambda r: r.update(arret="durée maximale dépassée")), 2, "arret")
        self.assertEqual(c["code"], 2)
        self.assertNotIn("table", c)


# --- artefacts : une garde chacun ------------------------------------------------------------------------------------------------
class Garde1SortieAbsente(Base):
    def test_dossier_vide(self):
        d = self.neuf("vide")
        os.makedirs(d)
        self.refuse(d, 1, "sortie_absente")

    def test_manifeste_absent(self):
        d = self.artefact()
        os.remove(os.path.join(d, "manifeste.json"))
        self.refuse(d, 1, "sortie_absente")

    def test_compagnon_non_conforme(self):
        d = self.artefact()
        with open(os.path.join(d, "epreuve-w2g-dose-v1.json"), "a", encoding="utf-8") as fh:
            fh.write(" ")
        self.refuse(d, 1, "compagnon")

    def test_illisible(self):
        d = self.artefact()
        p = os.path.join(d, "epreuve-w2g-dose-v1.json")
        os.remove(p)
        os.remove(p + ".sha256")
        ecrire_scelle(p, '{"epreuve": NaN}\n')
        self.refuse(d, 1, "illisible")

    def test_forme(self):
        self.refuse(self.artefact(lambda r: r["resultats"][2]["lignes"].pop("recombinaison|ancien")), 1, "forme")
        self.refuse(self.artefact(lambda r: _ligne(r, 0.5, "monde|v9").update(taux=0.123)), 1, "forme")

    def test_table_differente(self):
        self.refuse(self.artefact(lambda r: r.update(table=r["table"] + " ")), 1, "table")

    def test_code_de_sortie(self):
        self.refuse(self.chaine, 1, "code_de_sortie", console=self.console_code(2))
        self.refuse(self.chaine, 1, "illisible", console=self.console_code("0\ncode 0"))


class Garde2Duree(Base):
    def test_arret_non_nul(self):
        self.refuse(self.artefact(lambda r: r.update(arret="dose 0.4 : durée maximale dépassée à la répétition 1")), 2, "arret")

    def test_code_3_et_124(self):
        self.refuse(self.chaine, 2, "code_3", console=self.console_code(3))
        self.refuse(self.chaine, 2, "delai_externe", console=self.console_code(124))

    def test_dose_incomplete(self):
        def f(r):
            x = r["resultats"][4]
            x["complete"] = False
        self.refuse(self.artefact(f), 2, "dose_incomplete")

    def test_dose_manquante(self):
        self.refuse(self.artefact(lambda r: r["resultats"].pop(5)), 2, "dose_manquante")


class Garde3Graine(Base):
    def test_texte_autre(self):
        autre = self.neuf("autre-texte.md")
        ecrire_scelle(autre, "un autre texte\n")
        c = self.refuse(self.chaine, 3, "entropie", texte=autre)
        self.assertIn("texte_sha256", [m["motif"] for m in c["motifs"]])

    def test_texte_non_scelle(self):
        nu = self.neuf("texte-nu.md")
        shutil.copyfile(self.texte, nu)
        self.refuse(self.chaine, 3, "texte_non_scelle", texte=nu)

    def test_mode_exploratoire(self):
        def f(r):
            r["mode"] = "exploratoire (non décisif)"
        self.refuse(self.artefact(f, lambda m: m["reglages"].update(mode="exploratoire (non décisif)")), 3, "mode")

    def test_grille_reduite(self):
        garder = [0.3, 0.4, 0.5, 0.75]

        def f(r):
            r["doses"] = garder
            r["resultats"] = [x for x in r["resultats"] if x["dose"] in garder]
        self.refuse(self.artefact(f, lambda m: m["reglages"].update(doses=garder)), 3, "grille")

    def test_repetitions_et_processus(self):
        self.refuse(self.chaine, 3, "repetitions", repetitions=1000)
        self.refuse(self.chaine, 3, "processus", processus=4)

    def test_empreinte_de_module_changee(self):
        def m(o):
            o["reglages"]["modules_sha256"]["pole/attaque_goodhart_v5.py"] = "0" * 64
        c = self.refuse(self.artefact(manifeste=m), 3, "modules")
        self.assertIn("pole/attaque_goodhart_v5.py", c["motifs"][0]["detail"])

    def test_duree_et_versions(self):
        self.refuse(self.artefact(manifeste=lambda o: o["reglages"].update(duree_max_s=3300.0)), 3, "duree_max")
        self.refuse(self.artefact(manifeste=lambda o: o["reglages"].update(numpy="2.4.0")), 3, "versions")

    def test_sorties_exploratoires(self):
        """Les sorties exploratoires (texte § 3) refusent : graine non dérivée, grille réduite."""
        vus = 0
        for nom, empreinte in EXPLORATOIRES.items():
            d = os.path.join(BROUILLON, nom)
            if not os.path.isfile(os.path.join(d, "epreuve-w2g-dose-v1.json")):
                continue
            self.assertEqual(sha256_fichier(os.path.join(d, "epreuve-w2g-dose-v1.json")), empreinte)
            vus += 1
            c = self.refuse(d, 3, "mode", console=self.console_code(0), repetitions=1000, processus=2)
            motifs = [m["motif"] for m in c["motifs"]]
            for attendu in ("entropie", "texte_sha256", "entropie_sous_2_64", "grille"):
                self.assertIn(attendu, motifs, nom)
        if not vus:
            self.skipTest(f"sorties exploratoires absentes de {BROUILLON} (dossiers de brouillon effacés)")


class Garde4Verite(Base):
    def test_cle_verite(self):
        self.refuse(self.artefact(lambda r: r["resultats"][3].update(verite={"dose": 0.15})), 4, "cle_verite")
        self.refuse(self.artefact(manifeste=lambda m: m.update({"vérité": 1})), 4, "cle_verite")

    def test_cle_N(self):
        self.refuse(self.artefact(lambda r: r["resultats"][7]["lignes"]["monde|v9"].update(N={"type": "softmax"})), 4, "cle_N")


class Garde5Certificat(Base):
    def test_recombinaison_promue(self):
        self.refuse(self.artefact(lambda r: _poser(r, 0.5, "recombinaison|v9", 1)), 5, "recombinaison_promue")

    def test_monde_promu_a_dose_nulle(self):
        self.refuse(self.artefact(lambda r: _poser(r, 0.0, "monde|v9", 1)), 5, "monde_promu_dose_0")


class Garde6Instrument(Base):
    def test_grammaire_refusee(self):
        self.refuse(self.artefact(lambda r: r["resultats"][6].update(grammaire_servie_refusee=1)), 6, "grammaire_refusee")

    def test_desaccord_lambda(self):
        def f(r):
            imprime = r["dose_proposee_par_la_regle"]
            r["dose_proposee_par_la_regle"] = 0.05 if imprime != 0.05 else 0.1
        self.refuse(self.artefact(f), 6, "desaccord_lambda")

    def test_cle_absente_du_cas_sain(self):
        """Cas sain des gardes 4 à 6 : la course de chaîne n'a ni clé de vérité, ni (b) > 0, ni grammaire refusée."""
        with open(os.path.join(self.chaine, "epreuve-w2g-dose-v1.json"), encoding="utf-8") as fh:
            r = json.load(fh)
        self.assertEqual(lecteur.cles_interdites(r), [])
        self.assertTrue(all(x["lignes"]["recombinaison|v9"]["promues"] == 0 for x in r["resultats"]))
        self.assertTrue(all(x["grammaire_servie_refusee"] == 0 for x in r["resultats"]))
        self.assertEqual(lecteur.lambda_recalcule(r["resultats"]), r["dose_proposee_par_la_regle"])


if __name__ == "__main__":
    unittest.main()
