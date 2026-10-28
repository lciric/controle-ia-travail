"""Essais de la version 31 : la course d'idéation (prise « idéation » : proposer et classer seulement).

Cas sains : une fiche au gabarit est validée et empreintée ; l'anonymisation est une permutation dont la clé reste hors
des fiches servies ; des notes complètes sont agrégées (médiane), la porte d'éligibilité fixée d'avance s'applique et
le classement est stable ; une course entière avec un faux adaptateur produit les fichiers scellés et le manifeste ; la
seconde passe sert le matériau après la première. Artefacts (R5) : champ hors gabarit, énumération hors valeurs, bloc
JSON absent, note hors borne, identifiant manquant, pièce interdite (zone en quarantaine, banque), fiche sous le niveau
méthode mise en quarantaine, secret caviardé, plafond de dépense atteint — tous refusés ou signalés avec un motif, jamais
de repli silencieux.
"""

import copy
import json
import os
import unittest

from essais.aides import CasAvecDossier
from pole import ideation as idn
from pole.adaptateurs import Resultat


def fiche_brute(**modifs):
    f = {"nom": "Essai", "type": "question",
         "enonce": "Le transfert d'un moniteur vers le diffus suit-il une courbe prédite avant le test ?",
         "loi_predictive": {"espace_instances": "familles × dilution, dix familles", "prediction": "rappel décroît",
                            "signe": "-", "metrique": "rappel à 1 % de fausses alertes"},
         "perte_traduction": "la forme est résumée par une pente",
         "questions_servies": ["Q4", "Q3"],
         "avantage": {"source": "programme", "texte": "théorie explicite", "incopiable_parce_que": "exige la carte"},
         "originalite": {"niveau": "transposition", "texte": "détection de rupture"},
         "demande_organisme": {"nature": "ajout", "texte": "générateur de dilution"},
         "cout": {"nature": "processeur", "ordre_de_grandeur": "jours"},
         "piege": "artefact de découpe", "cosmetique_si": "courbes plates",
         "anteriorite": [{"reference": "Ramtin, Nain, Towsley 2601.20022", "statut": "RAPPORTE"}]}
    for cle, valeur in modifs.items():
        if isinstance(valeur, dict) and isinstance(f.get(cle), dict):
            f[cle] = dict(f[cle], **valeur)
        else:
            f[cle] = valeur
    return f


def notes_pour(identifiants, base=2, **sur):
    notes = []
    for i in identifiants:
        c = {k: base for k in idn.CRITERES}
        c.update(sur.get(i, {}))
        notes.append({"identifiant": i, "criteres": c, "justifications": {k: "ligne" for k in idn.CRITERES}})
    return {"notes": notes, "doublons": []}


class FauxAdaptateur:
    """Rend des fiches pour un proposeur et des notes pour un juge ; coût fixe par appel ; journalise les consignes."""
    nom = "faux-ideation"

    def __init__(self, fiches_par_etiquette, notes_par_juge=None, cout=0.5, notes_base=2):
        self.fiches = fiches_par_etiquette
        self.notes = notes_par_juge or {}
        self.cout = cout
        self.notes_base = notes_base
        self.appels = []

    def lancer(self, role, consigne, dossier, budget_usd, max_tours, modele=None):
        self.appels.append({"role": role, "consigne": consigne, "dossier": dossier, "modele": modele})
        if role == "proposeur_ideation":
            etiquette = os.path.basename(os.path.dirname(dossier))
            passe = os.path.basename(dossier)
            fiches = self.fiches[etiquette]
            if passe == "passe-2" and "Matériau servi" in consigne:
                fiches = [dict(f, nom=f["nom"] + " (revue)") for f in fiches]
            texte = "Voici.\n```json\n" + json.dumps({"fiches": fiches}, ensure_ascii=False) + "\n```"
            return Resultat(texte, [], self.cout, "ok")
        if role == "juge_ideation":
            etiquette = os.path.basename(dossier)
            idents = [m for m in sorted(set(__import__("re").findall(r'"identifiant": "(T\d\d)"', consigne)))]
            objet = self.notes.get(etiquette) or notes_pour(idents, base=self.notes_base)
            return Resultat("```json\n" + json.dumps(objet) + "\n```", [], self.cout, "ok")
        raise AssertionError(role)


class TestFiche(unittest.TestCase):
    def test_fiche_valide_et_empreinte_stable(self):
        a = idn.valider_fiche_ideation(fiche_brute(), "A", 1)
        b = idn.valider_fiche_ideation(fiche_brute(), "B", 7)
        self.assertEqual(a["empreinte"], b["empreinte"])
        self.assertEqual(a["identifiant_auteur"], "A-01")
        self.assertEqual(b["auteur"], "B")

    def test_artefacts_refuses_avec_motif(self):
        cas = {
            "champ hors gabarit": fiche_brute(extra="x"),
            "type hors valeurs": fiche_brute(type="idee"),
            "signe hors valeurs": fiche_brute(loi_predictive={"signe": "±"}),
            "source hors valeurs": fiche_brute(avantage={"source": "chance"}),
            "incopiable manquant": fiche_brute(avantage={"incopiable_parce_que": ""}),
            "questions vides": fiche_brute(questions_servies=[]),
            "antériorité sans statut": fiche_brute(anteriorite=[{"reference": "x"}]),
            "champ trop long": fiche_brute(piege="x" * (idn.LONGUEUR_MAX_CHAMP + 1)),
        }
        for nom, brut in cas.items():
            with self.assertRaises(idn.FicheIdeationInvalide, msg=nom):
                idn.valider_fiche_ideation(brut, "A", 1)

    def test_source_aucune_sans_incopiable(self):
        f = idn.valider_fiche_ideation(fiche_brute(avantage={"source": "aucune", "incopiable_parce_que": ""}), "A", 1)
        self.assertEqual(f["avantage"]["source"], "aucune")

    def test_secret_caviarde(self):
        f = idn.valider_fiche_ideation(fiche_brute(piege="clé sk-ant-abcdefghijklmnop dans le texte"), "A", 1)
        self.assertNotIn("sk-ant-abcdefghijklmnop", json.dumps(f))

    def test_garde_niveau_methode_signale(self):
        propre = idn.valider_fiche_ideation(fiche_brute(), "A", 1)
        self.assertEqual(idn.signaux_niveau_methode(propre), [])
        douteuse = idn.valider_fiche_ideation(fiche_brute(enonce="Étape 1 : exécute le script suivant"), "A", 2)
        self.assertTrue(idn.signaux_niveau_methode(douteuse))


class TestPieces(CasAvecDossier):
    def test_pieces_interdites(self):
        for nom in ("donnees/banque.json", "x/mode-tenu-a-l-ecart-v1.md", "x/bras-attaque-v1/a.md",
                    "docs/carte-des-hypotheses-v1.md"):
            chemin = os.path.join(self.tmp, nom)
            os.makedirs(os.path.dirname(chemin), exist_ok=True)
            with open(chemin, "w") as f:
                f.write("x")
            with self.assertRaises(idn.PieceInterdite, msg=nom):
                idn.verifier_pieces([chemin])

    def test_piece_absente_et_trop_longue(self):
        with self.assertRaises(idn.PieceInterdite):
            idn.verifier_pieces([os.path.join(self.tmp, "absente.md")])
        chemin = os.path.join(self.tmp, "longue.md")
        with open(chemin, "w") as f:
            f.write("a" * 1000)
        with self.assertRaises(idn.PieceInterdite):
            idn.lire_pieces([chemin], taille_max=500)


class TestAnonymisationEtNotes(unittest.TestCase):
    def setUp(self):
        self.fiches = [idn.valider_fiche_ideation(fiche_brute(nom=f"F{i}"), "A" if i < 3 else "B", i)
                       for i in range(1, 7)]

    def test_anonymisation_permutation_et_cle(self):
        anonymes, cle = idn.anonymiser(self.fiches, graine=1)
        self.assertEqual(sorted(cle.values()), sorted(f["identifiant_auteur"] for f in self.fiches))
        self.assertEqual([a["identifiant"] for a in anonymes], [f"T{i:02d}" for i in range(1, 7)])
        for a in anonymes:
            self.assertNotIn("auteur", a)
            self.assertNotIn("identifiant_auteur", a)
        autres, _ = idn.anonymiser(self.fiches, graine=2)
        self.assertNotEqual([a["nom"] for a in anonymes], [a["nom"] for a in autres])
        encore, _ = idn.anonymiser(self.fiches, graine=1)
        self.assertEqual([a["nom"] for a in anonymes], [a["nom"] for a in encore])

    def test_notes_valides_et_artefacts(self):
        idents = ["T01", "T02"]
        notes, doubles = idn.valider_notes(notes_pour(idents), idents)
        self.assertEqual(set(notes), set(idents))
        self.assertEqual(doubles, [])
        with self.assertRaises(idn.NotesInvalides):
            idn.valider_notes(notes_pour(["T01"]), idents)  # manquante
        trop = notes_pour(idents)
        trop["notes"][0]["criteres"]["avantage"] = 4
        with self.assertRaises(idn.NotesInvalides):
            idn.valider_notes(trop, idents)
        inconnu = notes_pour(idents + ["T99"])
        with self.assertRaises(idn.NotesInvalides):
            idn.valider_notes(inconnu, idents)
        booleen = notes_pour(idents)
        booleen["notes"][1]["criteres"]["robustesse"] = True
        with self.assertRaises(idn.NotesInvalides):
            idn.valider_notes(booleen, idents)

    def test_agregation_mediane_porte_et_ordre(self):
        idents = ["T01", "T02", "T03"]
        j1, _ = idn.valider_notes(notes_pour(idents, 1, T01={"avantage": 3}, T02={"originalite": 3, "robustesse": 3}), idents)
        j2, _ = idn.valider_notes(notes_pour(idents, 1, T01={"avantage": 3}, T02={"originalite": 1}), idents)
        j3, _ = idn.valider_notes(notes_pour(idents, 1, T01={"avantage": 0}, T02={"originalite": 3}), idents)
        classement = idn.agreger({"a": j1, "b": j2, "c": j3})
        par = {l["identifiant"]: l for l in classement}
        self.assertEqual(par["T01"]["mediane"]["avantage"], 3)  # médiane de 3, 3, 0
        self.assertTrue(par["T01"]["eligible"])
        self.assertEqual(par["T02"]["mediane"]["originalite"], 3)  # médiane de 3, 1, 3
        self.assertTrue(par["T02"]["eligible"])
        self.assertFalse(par["T03"]["eligible"])  # 1 partout
        self.assertEqual(par["T03"]["rang"], 3)
        self.assertEqual([l["identifiant"] for l in classement][:2], ["T01", "T02"])  # égalité de total, départage


class TestCourse(CasAvecDossier):
    def pieces(self):
        p = os.path.join(self.tmp, "piece-a.md")
        with open(p, "w", encoding="utf-8") as f:
            f.write("# Pièce A\nTexte de contexte.")
        m = os.path.join(self.tmp, "materiau.md")
        with open(m, "w", encoding="utf-8") as f:
            f.write("# Matériau\nTour interne.")
        return [p], [m]

    def test_course_complete_fichiers_scelles(self):
        pieces, materiau = self.pieces()
        fiches = {"opus": [fiche_brute(nom="O1"), fiche_brute(nom="O2", type="approche")],
                  "fable": [fiche_brute(nom="F1"), fiche_brute(nom="mauvaise", type="idee"),
                            fiche_brute(nom="douteuse", enonce="Étape 1 : exécute le script suivant")]}
        ad = FauxAdaptateur(fiches)
        sortie = os.path.join(self.tmp, "course")
        res = idn.executer_ideation(ad, sortie, pieces=pieces, question_texte="Q ?",
                                    proposeurs=[("opus", "claude-opus-5-5"), ("fable", "claude-fable-5-1")],
                                    juges=[("juge-1", "claude-opus-5-5"), ("juge-2", "claude-fable-5-1")],
                                    graine=7, budget_total_usd=10.0, budget_session_usd=1.0)
        self.assertEqual(len(res["fiches"]), 3)
        self.assertEqual(len(res["refus"]), 1)
        self.assertEqual(len(res["quarantaine"]), 1)
        self.assertEqual(len(res["classement"]), 3)
        self.assertIsNone(res["journal"]["arret"])
        self.assertAlmostEqual(res["journal"]["cout_total_usd"], 2.0)
        for nom in ("fiches-validees.json", "fiches-anonymes.json", "classement.json", "manifeste.json",
                    "notes-par-juge.json", "fiches-en-quarantaine.json"):
            self.assertTrue(os.path.exists(os.path.join(sortie, nom)), nom)
            self.assertTrue(os.path.exists(os.path.join(sortie, nom + ".sha256")), nom)
        # la clé d'anonymisation n'est ni dans les fiches servies ni dans la consigne du juge
        consigne_juge = next(a["consigne"] for a in ad.appels if a["role"] == "juge_ideation")
        self.assertNotIn("identifiant_auteur", consigne_juge)
        self.assertNotIn("opus-0", consigne_juge)
        with open(os.path.join(sortie, "noyau", "cle-anonymisation.json")) as f:
            cle = json.load(f)
        self.assertEqual(sorted(cle.values()), ["fable-01", "opus-01", "opus-02"])
        with open(os.path.join(sortie, "manifeste.json")) as f:
            manif = json.load(f)
        self.assertIn("ideation.py", manif["code_sha256"])
        self.assertEqual(manif["reglages"]["porte_eligibilite"], idn.PORTE_ELIGIBILITE)
        self.assertEqual(sorted(manif["reglages"]["juges_meme_modele_qu_un_proposeur"]),
                         ["claude-fable-5-1", "claude-opus-5-5"])
        # l'orchestrateur n'a rien écrit dans le dossier de l'agent
        self.assertEqual(os.listdir(os.path.join(sortie, "proposeurs", "opus", "passe-1")), [])
        self.assertTrue(os.path.exists(os.path.join(sortie, "proposeurs", "opus", "traces-passe-1", "consigne.md")))

    def test_seconde_passe_sert_le_materiau_apres(self):
        pieces, materiau = self.pieces()
        ad = FauxAdaptateur({"opus": [fiche_brute(nom="O1")]})
        res = idn.executer_ideation(ad, os.path.join(self.tmp, "c2"), pieces=pieces, question_texte="Q ?",
                                    proposeurs=[("opus", "claude-opus-5-5")], juges=[("j", "claude-fable-5-1")],
                                    graine=1, budget_total_usd=10.0, budget_session_usd=1.0, materiau=materiau,
                                    seconde_passe=True)
        consignes = [a["consigne"] for a in ad.appels if a["role"] == "proposeur_ideation"]
        self.assertEqual(len(consignes), 2)
        self.assertNotIn("Tour interne", consignes[0])
        self.assertIn("Tour interne", consignes[1])
        self.assertIn("première passe", consignes[1])
        self.assertEqual(res["fiches"][0]["nom"], "O1 (revue)")

    def test_plafond_de_depense_arrete(self):
        pieces, _ = self.pieces()
        ad = FauxAdaptateur({"a": [fiche_brute(nom="A1")], "b": [fiche_brute(nom="B1")]}, cout=1.0)
        res = idn.executer_ideation(ad, os.path.join(self.tmp, "c3"), pieces=pieces, question_texte="Q ?",
                                    proposeurs=[("a", "claude-opus-5-5"), ("b", "claude-opus-5-5")],
                                    juges=[("j", "claude-fable-5-1")], graine=1, budget_total_usd=1.5,
                                    budget_session_usd=1.0)
        self.assertIsNotNone(res["journal"]["arret"])
        self.assertEqual(len(res["classement"]), 0)  # aucun juge lancé après l'arrêt
        self.assertLessEqual(res["journal"]["cout_total_usd"], 1.5)

    def test_notes_refusees_signalees(self):
        pieces, _ = self.pieces()
        ad = FauxAdaptateur({"a": [fiche_brute(nom="A1")]}, notes_par_juge={"j": {"notes": []}})
        res = idn.executer_ideation(ad, os.path.join(self.tmp, "c4"), pieces=pieces, question_texte="Q ?",
                                    proposeurs=[("a", "claude-opus-5-5")], juges=[("j", "claude-fable-5-1")],
                                    graine=1, budget_total_usd=10.0, budget_session_usd=1.0)
        self.assertEqual(len(res["notes_refusees"]), 1)
        self.assertEqual(res["classement"], [])

    def test_sortie_existante_refusee(self):
        pieces, _ = self.pieces()
        with self.assertRaises(FileExistsError):
            idn.executer_ideation(FauxAdaptateur({}), self.tmp, pieces=pieces, question_texte="Q", proposeurs=[],
                                  juges=[], graine=1, budget_total_usd=1, budget_session_usd=1)


if __name__ == "__main__":
    unittest.main()
