"""Essais de la version 32 : la course d'idéation (prise « idéation » : proposer et classer seulement).

Cas sains : fiche au gabarit validée et empreintée ; liste blanche par empreinte acceptée ; anonymisation par juge
(permutations différentes, clé hors des fiches servies, aucune empreinte servie) ; notes complètes agrégées (moyenne
nommée à deux juges, porte fixée d'avance, porte « unanimité », départage par empreinte) ; course entière avec faux
adaptateur : manifeste de départ scellé avant le premier appel, témoins lus à part, classement lisible, lectures par juge ;
seconde passe qui ajoute (ne remplace pas) et sert le matériau après ; appel de contrôle conforme.
Artefacts (R5) : champ hors gabarit, énumération hors valeurs, bloc JSON absent, liste vide, fiches en trop, note hors
borne, note manquante, pièce hors liste blanche ou à empreinte différente, lien symbolique, variantes de chemin (accents,
`_`, « données »), paraphrases devant la garde, secret caviardé, session en erreur (arrêt dur, code d'erreur), juge
invalide (arrêt), plafond total, appel de contrôle refusé (statut, texte, coût, relais muet), url du relais en https ou
avec chemin, étiquettes invalides, absence de témoins, max_tours trop grand — tous refusés avec un motif.
"""

import json
import os
import re
import sys
import unittest

from essais.aides import CasAvecDossier
from pole import ideation as idn
from pole.adaptateurs import Resultat, construire_options
from pole.relais import RelaisInvalide


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
    """Rend des fiches pour un proposeur, des notes pour un juge, « OK » pour l'appel de contrôle ; coût fixe ; peut
    simuler une erreur ou des notes données par une fonction (identifiants → objet)."""
    nom = "faux-ideation"

    def __init__(self, fiches_par_etiquette, notes_par_juge=None, cout=0.5, notes_base=2, erreur_pour=(),
                 texte_controle="OK", cout_controle=0.01, statut_controle="ok"):
        self.fiches = fiches_par_etiquette
        self.notes = notes_par_juge or {}
        self.cout, self.notes_base = cout, notes_base
        self.erreur_pour = set(erreur_pour)
        self.texte_controle, self.cout_controle, self.statut_controle = texte_controle, cout_controle, statut_controle
        self.appels = []

    def lancer(self, role, consigne, dossier, budget_usd, max_tours, modele=None):
        self.appels.append({"role": role, "consigne": consigne, "dossier": dossier, "modele": modele,
                            "budget": budget_usd, "max_tours": max_tours})
        if consigne == idn.APPEL_DE_CONTROLE_CONSIGNE:
            return Resultat(self.texte_controle, [], self.cout_controle, self.statut_controle)
        etiquette = os.path.basename(os.path.dirname(dossier)) if role == "proposeur_ideation" else os.path.basename(dossier)
        passe = os.path.basename(dossier)
        if (etiquette, passe) in self.erreur_pour or etiquette in self.erreur_pour:
            return Resultat("API Error: 400 Bad request version", [], 0.0, "erreur", "APIError")
        if role == "proposeur_ideation":
            fiches = self.fiches[etiquette]
            if callable(fiches):
                fiches = fiches(passe, consigne)
            elif passe == "passe-2":
                fiches = [dict(f, nom=f["nom"] + " (revue)") for f in fiches]
            texte = "Voici.\n```json\n" + json.dumps({"fiches": fiches}, ensure_ascii=False) + "\n```"
            return Resultat(texte, [], self.cout, "ok")
        if role == "juge_ideation":
            idents = sorted(set(re.findall(r'"identifiant": "(T\d\d)"', consigne)))
            objet = self.notes.get(etiquette)
            if callable(objet):
                objet = objet(idents, consigne)
            if objet is None:
                objet = notes_pour(idents, base=self.notes_base)
            return Resultat("```json\n" + json.dumps(objet) + "\n```", [], self.cout, "ok")
        raise AssertionError(role)


class TestFiche(unittest.TestCase):
    def test_fiche_valide_et_empreinte_stable(self):
        a = idn.valider_fiche_ideation(fiche_brute(), "a", 1)
        b = idn.valider_fiche_ideation(fiche_brute(), "b", 7, passe=2)
        self.assertEqual(a["empreinte"], b["empreinte"])
        self.assertEqual(a["identifiant_auteur"], "a-p1-01")
        self.assertEqual(b["identifiant_auteur"], "b-p2-07")
        self.assertNotIn("empreinte", idn.vue_servie(a))
        self.assertNotIn("auteur", idn.vue_servie(a))

    def test_artefacts_refuses_avec_motif(self):
        cas = {"champ hors gabarit": fiche_brute(extra="x"), "type hors valeurs": fiche_brute(type="idee"),
               "signe hors valeurs": fiche_brute(loi_predictive={"signe": "±"}),
               "source hors valeurs": fiche_brute(avantage={"source": "chance"}),
               "incopiable manquant": fiche_brute(avantage={"incopiable_parce_que": ""}),
               "questions vides": fiche_brute(questions_servies=[]),
               "antériorité sans statut": fiche_brute(anteriorite=[{"reference": "x"}]),
               "champ trop long": fiche_brute(piege="x" * (idn.LONGUEUR_MAX_CHAMP + 1))}
        for nom, brut in cas.items():
            with self.assertRaises(idn.FicheIdeationInvalide, msg=nom):
                idn.valider_fiche_ideation(brut, "a", 1)

    def test_secret_caviarde(self):
        faux = "sk-" + "ant-" + "abcdefghijklmnop"  # construit à l'exécution : la recherche de clés du dépôt reste propre
        f = idn.valider_fiche_ideation(fiche_brute(piege="clé " + faux + " dans le texte"), "a", 1)
        self.assertNotIn(faux, json.dumps(f))

    def test_garde_niveau_methode_paraphrases(self):
        self.assertEqual(idn.signaux_niveau_methode(idn.vue_servie(idn.valider_fiche_ideation(fiche_brute(), "a", 1))), [])
        for phrase in ("Étape 1 : exécute le script suivant", "Étape 1. ouvrir", "Première étape — préparer",
                       "Phase 1 : préparer", "1) ceci est long\n2) cela", "afin de contourner le moniteur de sortie",
                       "pour échapper au détecteur", "to evade the probe", "injection de consigne", "exploiter la faille",
                       "une porte dérobée", "exfiltration lente"):
            self.assertTrue(idn.signaux_niveau_methode(phrase), phrase)
        for phrase in ("La première famille tenue à l'écart", "un moniteur boîte noire par épisode",
                       "le juge figé à borne", "une sonde linéaire sur la dernière couche"):
            self.assertEqual(idn.signaux_niveau_methode(phrase), [], phrase)


class TestPieces(CasAvecDossier):
    def ecrire(self, nom, contenu="x"):
        chemin = os.path.join(self.tmp, nom)
        os.makedirs(os.path.dirname(chemin), exist_ok=True)
        with open(chemin, "w", encoding="utf-8") as f:
            f.write(contenu)
        return chemin

    def test_liste_blanche_acceptee_et_variantes_refusees(self):
        p = self.ecrire("piece-a.md", "# A")
        liste = idn.construire_liste_blanche([p], os.path.join(self.tmp, "lb.json"))
        self.assertEqual(idn.verifier_pieces([p], liste), [os.path.realpath(p)])
        for nom in ("donnees/banque.json", "x/mode-tenu-a-l-ecart-v1.md", "x/bras_attaque/a.md", "x/bras-d-attaque/a.md",
                    "données/a.md", "x/mode_tenu_à_l_écart/a.md", "docs/carte-hypotheses-v1.md", "x/banques/a.md",
                    "x/banque_v3.json", "prereg/P3-consignes-v1.md"):
            c = self.ecrire(nom)
            liste2 = dict(liste, **{os.path.realpath(c): idn.sha256_fichier(c)})
            with self.assertRaises(idn.PieceInterdite, msg=nom):
                idn.verifier_pieces([c], liste2)

    def test_hors_liste_empreinte_differente_lien(self):
        p = self.ecrire("piece-b.md", "# B")
        with self.assertRaises(idn.PieceInterdite):
            idn.verifier_pieces([p], {})
        with self.assertRaises(idn.PieceInterdite):
            idn.verifier_pieces([p], {os.path.realpath(p): "0" * 64})
        liste = idn.construire_liste_blanche([p], os.path.join(self.tmp, "lb2.json"))
        with open(p, "a") as f:
            f.write("modifié")
        with self.assertRaises(idn.PieceInterdite):
            idn.verifier_pieces([p], liste)
        lien = os.path.join(self.tmp, "lien.md")
        os.symlink(p, lien)
        liste3 = idn.construire_liste_blanche([p], os.path.join(self.tmp, "lb3.json"))
        with self.assertRaises(idn.PieceInterdite):
            idn.verifier_pieces([lien], dict(liste3, **{os.path.realpath(lien): liste3[os.path.realpath(p)]}))

    def test_url_relais_ideation(self):
        self.assertEqual(idn.valider_url_relais_ideation("http://127.0.0.1:8787"), "http://127.0.0.1:8787")
        for url in ("https://127.0.0.1:8787", "http://127.0.0.1:8787/v1", "http://relais.exemple.org", "http://127.0.0.1:1?x=1"):
            with self.assertRaises(RelaisInvalide, msg=url):
                idn.valider_url_relais_ideation(url)


class TestAnonymisationEtNotes(unittest.TestCase):
    def setUp(self):
        self.fiches = [idn.valider_fiche_ideation(fiche_brute(nom=f"F{i}"), "a" if i < 3 else "b", i) for i in range(1, 7)]

    def test_anonymisation_par_juge(self):
        a1, cle1 = idn.anonymiser(self.fiches, 1, "juge-1")
        a2, cle2 = idn.anonymiser(self.fiches, 1, "juge-2")
        self.assertEqual(sorted(cle1.values()), sorted(f["identifiant_auteur"] for f in self.fiches))
        self.assertNotEqual([a["nom"] for a in a1], [a["nom"] for a in a2])
        for a in a1:
            for champ in idn.CHAMPS_INTERNES:
                self.assertNotIn(champ, a)
        encore, _ = idn.anonymiser(self.fiches, 1, "juge-1")
        self.assertEqual([a["nom"] for a in a1], [a["nom"] for a in encore])

    def test_notes_valides_et_artefacts(self):
        idents = ["T01", "T02"]
        notes, doubles = idn.valider_notes(notes_pour(idents), idents)
        self.assertEqual(set(notes), set(idents))
        with self.assertRaises(idn.NotesInvalides):
            idn.valider_notes(notes_pour(["T01"]), idents)
        trop = notes_pour(idents)
        trop["notes"][0]["criteres"]["avantage"] = 4
        with self.assertRaises(idn.NotesInvalides):
            idn.valider_notes(trop, idents)
        with self.assertRaises(idn.NotesInvalides):
            idn.valider_notes(notes_pour(idents + ["T99"]), idents)
        booleen = notes_pour(idents)
        booleen["notes"][1]["criteres"]["robustesse"] = True
        with self.assertRaises(idn.NotesInvalides):
            idn.valider_notes(booleen, idents)
        demi = notes_pour(idents)
        demi["notes"][0]["criteres"]["avantage"] = 2.5
        with self.assertRaises(idn.NotesInvalides):
            idn.valider_notes(demi, idents)

    def test_agregation_nommee_porte_unanimite_departage(self):
        par = {f["identifiant_auteur"]: f for f in self.fiches}
        ids = list(par)
        j1 = {i: {"criteres": {k: 1 for k in idn.CRITERES}} for i in ids}
        j2 = {i: {"criteres": {k: 1 for k in idn.CRITERES}} for i in ids}
        j1[ids[0]]["criteres"]["avantage"] = 3  # un seul juge élève : moyenne 2 → éligible, unanimité fausse
        j1[ids[1]]["criteres"]["originalite"] = 3
        j2[ids[1]]["criteres"]["originalite"] = 3  # unanimité vraie
        cl = idn.agreger({"j1": j1, "j2": j2}, par)
        parl = {l["identifiant_auteur"]: l for l in cl}
        self.assertEqual(parl[ids[0]]["nom_agregat"], "moyenne")
        self.assertTrue(parl[ids[0]]["eligible"])
        self.assertFalse(parl[ids[0]]["eligible_unanimite"])
        self.assertTrue(parl[ids[1]]["eligible_unanimite"])
        self.assertEqual([l["identifiant_auteur"] for l in cl][:2], [ids[1], ids[0]])  # totaux 7 puis 6
        # les quatre autres fiches sont à égalité stricte (1 partout, inéligibles) : départage par empreinte, déterministe
        reste = [l["identifiant_auteur"] for l in cl][2:]
        self.assertEqual(reste, sorted(reste, key=lambda i: par[i]["empreinte"]))
        trois = idn.agreger({"j1": j1, "j2": j2, "j3": j2}, par)
        self.assertEqual(trois[0]["nom_agregat"], "mediane")


class TestCourse(CasAvecDossier):
    def preparer(self, temoins_json=None):
        p = os.path.join(self.tmp, "piece-a.md")
        with open(p, "w", encoding="utf-8") as f:
            f.write("# Pièce A\nTexte de contexte.")
        q = os.path.join(self.tmp, "question.md")
        with open(q, "w", encoding="utf-8") as f:
            f.write("Quelles questions ?")
        m = os.path.join(self.tmp, "materiau.md")
        with open(m, "w", encoding="utf-8") as f:
            f.write("# Matériau\nTour interne.")
        t = os.path.join(self.tmp, "temoins.json")
        with open(t, "w", encoding="utf-8") as f:
            json.dump(temoins_json or {"temoins": [
                {"fiche": fiche_brute(nom="Sobre fort"), "attendu": "eligible"},
                {"fiche": fiche_brute(nom="Verbeux vide", enonce="Long " * 50), "attendu": "ineligible",
                 "note_max": {"falsifiabilite": 1}},
                {"fiche": fiche_brute(nom="Jumeau"), "attendu": "eligible", "jumeau_de": "Sobre fort"}]}, f,
                ensure_ascii=False)
        lb = os.path.join(self.tmp, "liste-blanche.json")
        idn.construire_liste_blanche([p, q, m, t], lb)
        return dict(liste_blanche=lb, question=q, pieces=[p], materiau=[m], temoins=t)

    def budgets(self):
        return {("proposeur_ideation", "claude-opus-5-5"): 1.0, ("proposeur_ideation", "claude-fable-5-1"): 1.0,
                ("juge_ideation", "claude-opus-5-5"): 1.0, ("juge_ideation", "claude-fable-5-1"): 1.0}

    def lancer(self, ad, sortie, **modifs):
        if not hasattr(self, "_prep"):
            self._prep = self.preparer()  # la liste blanche est scellée une fois par essai (jamais écrasée)
        args = dict(self._prep, proposeurs=[("opus", "claude-opus-5-5"), ("fable", "claude-fable-5-1")],
                    juges=[("juge-fable", "claude-fable-5-1"), ("juge-opus", "claude-opus-5-5")], graine=7,
                    budget_total_usd=20.0, budgets=self.budgets())
        args.update(modifs)
        return idn.executer_ideation(ad, os.path.join(self.tmp, sortie), **args)

    def notes_temoins_ok(self, idents, consigne):
        """Juge scripté qui respecte le critère gelé des témoins (lit les noms dans la consigne)."""
        bloc = json.loads(re.search(r"```json\n(\[.*\])\n```", consigne, re.S).group(1))
        sur, doublons = {}, []
        par_nom = {f["nom"]: f["identifiant"] for f in bloc}
        for f in bloc:
            if f["nom"] == "Verbeux vide":
                sur[f["identifiant"]] = {"avantage": 1, "originalite": 1, "falsifiabilite": 0}
        if "Jumeau" in par_nom and "Sobre fort" in par_nom:
            doublons.append([par_nom["Jumeau"], par_nom["Sobre fort"]])
        objet = notes_pour(idents, 2, **sur)
        objet["doublons"] = doublons
        return objet

    def test_course_complete(self):
        fiches = {"opus": [fiche_brute(nom="O1"), fiche_brute(nom="O2", type="approche")],
                  "fable": [fiche_brute(nom="F1"), fiche_brute(nom="douteuse", enonce="Étape 1 : exécute le script suivant")]}
        ad = FauxAdaptateur(fiches, notes_par_juge={"juge-fable": self.notes_temoins_ok, "juge-opus": self.notes_temoins_ok})
        res = self.lancer(ad, "course")
        sortie = os.path.join(self.tmp, "course")
        self.assertEqual(len(res["fiches"]), 3)
        self.assertEqual(len(res["quarantaine"]), 1)
        self.assertEqual(len(res["classement"]), 3)  # témoins exclus
        self.assertTrue(res["lecture"]["temoins"]["temoins_ok"])
        self.assertTrue(res["lecture"]["complet"])
        self.assertIsNone(res["journal"]["arret"])
        self.assertTrue(res["journal"]["cout_fictif"])
        for nom in ("manifeste-depart.json", "manifeste-fin.json", "fiches-validees.json", "classement.json",
                    "classements-par-juge.json", "lecture.json", "notes-par-juge.json", "fiches-en-quarantaine.json"):
            self.assertTrue(os.path.exists(os.path.join(sortie, nom + ".sha256")), nom)
        with open(os.path.join(sortie, "manifeste-depart.json")) as f:
            depart = json.load(f)
        self.assertEqual(depart["reglages"]["phase"], "depart")
        self.assertEqual(depart["reglages"]["temoins"]["nombre"], 3)
        self.assertTrue(all(len(p["sha256"]) == 64 for p in depart["reglages"]["pieces"]))
        with open(os.path.join(sortie, "classement.json")) as f:
            cl = json.load(f)
        self.assertTrue(cl["lisible_L2_L4"])
        # la porte n'est pas servie aux juges ; les témoins sont servis anonymes ; aucune empreinte ni auteur
        consignes_juges = [a["consigne"] for a in ad.appels if a["role"] == "juge_ideation" and a["consigne"] != idn.APPEL_DE_CONTROLE_CONSIGNE]
        self.assertEqual(len(consignes_juges), 2)
        for c in consignes_juges:
            self.assertNotIn("éligibilité", c)
            self.assertNotIn("identifiant_auteur", c)
            self.assertNotIn('"empreinte"', c)
            self.assertIn("Sobre fort", c)
        self.assertNotEqual(consignes_juges[0].split("## Les fiches")[1], consignes_juges[1].split("## Les fiches")[1])
        # aucun outil, deux tours au plus, l'orchestrateur n'écrit rien dans le dossier de l'agent
        self.assertTrue(all(a["max_tours"] <= idn.MAX_TOURS_IDEATION for a in ad.appels))
        self.assertEqual(os.listdir(os.path.join(sortie, "proposeurs", "opus", "passe-1")), [])
        # lecture d'auto-préférence présente pour chaque juge
        self.assertEqual(set(res["lecture"]["auto_preference"]), {"juge-fable", "juge-opus"})

    def test_seconde_passe_ajoute_et_sert_le_materiau_apres(self):
        ad = FauxAdaptateur({"opus": [fiche_brute(nom="O1")], "fable": [fiche_brute(nom="F1")]},
                            notes_par_juge={"juge-fable": self.notes_temoins_ok, "juge-opus": self.notes_temoins_ok})
        res = self.lancer(ad, "c2", seconde_passe=True)
        consignes = [a["consigne"] for a in ad.appels if a["role"] == "proposeur_ideation"]
        self.assertEqual(len(consignes), 4)
        self.assertNotIn("Tour interne", consignes[0])
        self.assertIn("Tour interne", consignes[2])
        self.assertEqual(sorted(f["passe"] for f in res["fiches"]), [1, 1, 2, 2])
        self.assertEqual(sorted(l["passe"] for l in res["classement"]), [1, 1, 2, 2])

    def test_fiche_en_quarantaine_non_resservie(self):
        def opus(passe, consigne):
            if passe == "passe-2":
                assert "douteuse" not in consigne
                return [fiche_brute(nom="O2")]
            return [fiche_brute(nom="douteuse", enonce="Phase 1 : préparer ; afin de contourner le moniteur")]
        ad = FauxAdaptateur({"opus": opus, "fable": [fiche_brute(nom="F1")]},
                            notes_par_juge={"juge-fable": self.notes_temoins_ok, "juge-opus": self.notes_temoins_ok})
        res = self.lancer(ad, "c3", seconde_passe=True)
        self.assertEqual(len(res["quarantaine"]), 1)

    def test_session_en_erreur_arrete(self):
        ad = FauxAdaptateur({"opus": [fiche_brute(nom="O1")], "fable": [fiche_brute(nom="F1")]}, erreur_pour=("fable",))
        with self.assertRaises(idn.CourseInterrompue):
            self.lancer(ad, "c4")
        with open(os.path.join(self.tmp, "c4", "manifeste-fin.json")) as f:
            fin = json.load(f)
        self.assertIn("statut 'erreur'", fin["reglages"]["erreur"])
        self.assertEqual(len([a for a in ad.appels if a["role"] == "juge_ideation" and a["consigne"] != idn.APPEL_DE_CONTROLE_CONSIGNE]), 0)

    def test_fiches_en_trop_liste_vide_refusees(self):
        ad = FauxAdaptateur({"opus": [fiche_brute(nom=f"O{i}") for i in range(10)], "fable": [fiche_brute(nom="F1")]})
        with self.assertRaises(idn.CourseInterrompue) as cm:
            self.lancer(ad, "c5")
        self.assertIn("10 fiches rendues", str(cm.exception))
        ad2 = FauxAdaptateur({"opus": [], "fable": [fiche_brute(nom="F1")]})
        with self.assertRaises(idn.CourseInterrompue) as cm2:
            self.lancer(ad2, "c6")
        self.assertIn("vide", str(cm2.exception))

    def test_juge_invalide_arrete_et_classement_absent(self):
        ad = FauxAdaptateur({"opus": [fiche_brute(nom="O1")], "fable": [fiche_brute(nom="F1")]},
                            notes_par_juge={"juge-fable": self.notes_temoins_ok, "juge-opus": {"notes": []}})
        with self.assertRaises(idn.CourseInterrompue):
            self.lancer(ad, "c7")
        self.assertFalse(os.path.exists(os.path.join(self.tmp, "c7", "classement.json")))

    def test_temoins_echoues_rendent_illisible(self):
        ad = FauxAdaptateur({"opus": [fiche_brute(nom="O1")], "fable": [fiche_brute(nom="F1")]})  # juges à 2 partout
        res = self.lancer(ad, "c8")
        self.assertFalse(res["lecture"]["temoins"]["temoins_ok"])
        with open(os.path.join(self.tmp, "c8", "classement.json")) as f:
            self.assertFalse(json.load(f)["lisible_L2_L4"])

    def test_plafond_total_arrete_avant_depense(self):
        ad = FauxAdaptateur({"opus": [fiche_brute(nom="O1")], "fable": [fiche_brute(nom="F1")]}, cout=1.0)
        with self.assertRaises(idn.CourseInterrompue):
            self.lancer(ad, "c9", budget_total_usd=1.5)
        self.assertLessEqual(ad.appels[-1]["budget"], 1.0)

    def test_reglages_refuses(self):
        ad = FauxAdaptateur({"opus": [fiche_brute(nom="O1")]})
        with self.assertRaises(idn.CourseInterrompue):
            self.lancer(ad, "c10", temoins=None)
        with self.assertRaises(idn.CourseInterrompue):
            self.lancer(ad, "c11", juges=[("Juge Opus", "claude-opus-5-5")])
        with self.assertRaises(idn.CourseInterrompue):
            self.lancer(ad, "c12", max_tours=6)
        with self.assertRaises(idn.CourseInterrompue):
            self.lancer(ad, "c13", budgets={})

    def test_appel_de_controle(self):
        sortie = os.path.join(self.tmp, "ctrl")
        etat = {"appels": 0, "depense_usd": 0.0}

        def relais():
            return dict(etat)
        ad = FauxAdaptateur({})
        orig = ad.lancer

        def lancer_compte(*a, **k):
            r = orig(*a, **k)
            etat["appels"] += 1
            etat["depense_usd"] += 0.01
            return r
        ad.lancer = lancer_compte
        lecture = idn.appel_de_controle(ad, ["claude-opus-5-5"], sortie, 0.1, relais)
        self.assertEqual(lecture["claude-opus-5-5"]["problemes"], [])
        for mauvais in (dict(texte_controle="Bonjour"), dict(statut_controle="erreur"), dict(cout_controle=0.0)):
            with self.assertRaises(idn.CourseInterrompue):
                idn.appel_de_controle(FauxAdaptateur({}, **mauvais), ["claude-opus-5-5"], sortie, 0.1, None)
        with self.assertRaises(idn.CourseInterrompue):  # relais muet
            idn.appel_de_controle(FauxAdaptateur({}), ["claude-fable-5-1"], sortie, 0.1, lambda: {"appels": 0, "depense_usd": 0.0})

    def test_options_sans_outil_pour_les_roles_ideation(self):
        dossier = os.path.join(self.tmp, "course", "proposeurs", "opus", "passe-1")
        os.makedirs(dossier)
        for role in ("proposeur_ideation", "juge_ideation"):
            o = construire_options(dossier, 1.0, 2, url_relais="http://127.0.0.1:8787", modele="claude-opus-5-5",
                                   role=role, interdire_lecture=[os.path.join(self.tmp, "course")])
            self.assertEqual(o["allowed_tools"], [])
            self.assertEqual(o["max_turns"], 2)


if __name__ == "__main__":
    unittest.main()


class TestJugeExterne(CasAvecDossier):
    """v33 : juge d'une autre lignée en bras rapporté (adaptateur à commande)."""

    def commande(self, script):
        chemin = os.path.join(self.tmp, "juge.py")
        with open(chemin, "w", encoding="utf-8") as f:
            f.write(script)
        return [sys.executable, "-I", chemin]

    SCRIPT_OK = (
        "import sys, json, re\n"
        "consigne = sys.stdin.read()\n"
        "idents = sorted(set(re.findall(r'\"identifiant\": \"(T\\d\\d)\"', consigne)))\n"
        "if 'exactement OK' in consigne:\n"
        "    print(json.dumps({'texte': 'OK', 'cout_usd': 0.001})); sys.exit(0)\n"
        "bloc = json.loads(re.search(r'```json\\n(\\[.*\\])\\n```', consigne, re.S).group(1))\n"
        "par_nom = {f['nom']: f['identifiant'] for f in bloc}\n"
        "notes = []\n"
        "for f in bloc:\n"
        "    c = {k: 2 for k in ('avantage','originalite','falsifiabilite','traitabilite','robustesse')}\n"
        "    if f['nom'] == 'Verbeux vide': c.update({'avantage': 1, 'originalite': 1, 'falsifiabilite': 0})\n"
        "    notes.append({'identifiant': f['identifiant'], 'criteres': c, 'justifications': {}})\n"
        "doublons = [[par_nom['Jumeau'], par_nom['Sobre fort']]] if 'Jumeau' in par_nom and 'Sobre fort' in par_nom else []\n"
        "print(json.dumps({'texte': '```json\\n' + json.dumps({'notes': notes, 'doublons': doublons}) + '\\n```', 'cout_usd': 0.3}))\n")

    def test_commande_factice_notes_et_controle(self):
        from pole.adaptateurs import AdaptateurJugeExterne
        ad = AdaptateurJugeExterne(self.commande(self.SCRIPT_OK), environnement={})
        r = ad.lancer("juge_ideation", idn.APPEL_DE_CONTROLE_CONSIGNE, self.tmp, 0.1, 1, modele="autre-lignee-x")
        self.assertEqual((r.statut, r.texte_final, r.cout_declare_usd), ("ok", "OK", 0.001))
        with self.assertRaises(ValueError):
            ad.lancer("proposeur_ideation", "x", self.tmp, 1.0, 1)

    def test_artefacts_de_la_commande(self):
        from pole.adaptateurs import AdaptateurJugeExterne
        for script, attendu in (("import sys; sys.exit(3)", "erreur"), ("print('pas du json')", "erreur"),
                                ("import json; print(json.dumps({'texte': 'x', 'cout_usd': 9.0}))", "budget_depasse"),
                                ("import json; print(json.dumps({'texte': 'x'}))", "ok"),
                                ("import json; print(json.dumps({'cout_usd': 1}))", "erreur")):
            ad = AdaptateurJugeExterne(self.commande(script), environnement={})
            r = ad.lancer("juge_ideation", "consigne", self.tmp, 1.0, 1)
            self.assertEqual(r.statut, attendu, script)
        from pole.relais import CleDansEnvironnement
        ad = AdaptateurJugeExterne(self.commande("print(1)"), environnement={"ANTHROPIC_API_KEY": "x"})
        with self.assertRaises(CleDansEnvironnement):
            ad.lancer("juge_ideation", "consigne", self.tmp, 1.0, 1)

    def test_bras_rapporte_dans_la_course(self):
        from pole.adaptateurs import AdaptateurJugeExterne
        cours = TestCourse("test_course_complete")
        cours.tmp = self.tmp
        fiches = {"opus": [fiche_brute(nom="O1"), fiche_brute(nom="O2")], "fable": [fiche_brute(nom="F1")]}
        ad = FauxAdaptateur(fiches, notes_par_juge={"juge-fable": cours.notes_temoins_ok, "juge-opus": cours.notes_temoins_ok})
        externe = AdaptateurJugeExterne(self.commande(self.SCRIPT_OK), environnement={})
        budgets = dict(cours.budgets())
        budgets[("juge_ideation", "autre-lignee-x")] = 1.0
        res = cours.lancer(ad, "cx", budgets=budgets, juges_externes=[("argon", "autre-lignee-x", externe)])
        self.assertIn("bras_rapporte", res["lecture"])
        br = res["lecture"]["bras_rapporte"]
        self.assertEqual(br["juges"], {"argon": "autre-lignee-x"})
        self.assertTrue(br["temoins"]["temoins_ok"])
        self.assertIn("argon", br["accord_avec_le_classement_agrege"])
        # jamais agrégé : le classement principal ne compte que les deux juges Claude
        self.assertTrue(all(l["nombre_juges"] == 2 for l in res["classement"]))
        sortie = os.path.join(self.tmp, "cx")
        self.assertTrue(os.path.exists(os.path.join(sortie, "notes-bras-rapporte.json.sha256")))
        self.assertTrue(os.path.exists(os.path.join(sortie, "juges-bras-rapporte", "traces-argon", "consigne.md")))
