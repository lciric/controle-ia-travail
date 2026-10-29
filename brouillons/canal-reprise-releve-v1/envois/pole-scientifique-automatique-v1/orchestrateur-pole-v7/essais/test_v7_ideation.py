"""Essais de la version 35 (depuis la 32) : la course d'idéation (prise « idéation » : proposer et classer seulement).

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
v35 (CL34) : attestation donnée à la course refusée ; bras différé seul chemin (attestation sans l'empreinte de la consigne
refusée, sceau faux refusé, rejeu refusé, plafond total tenu, témoins lus chez le juge externe, manifeste sur tous les
chemins) ; coût manquant du juge externe → erreur ; environnement minimal de la commande ; `tools=[]` dans les options et
`--tools ''` sur la ligne de commande du kit ; borne de temps par session ; `nombre` borné ; contrôles comptés ; manifeste de
fin sur toute exception ; pluriels devant la garde.
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


class TestTemoinsEtGardeV34(CasAvecDossier):
    def test_liste_numerotee_dans_une_fiche_signalee(self):
        f = idn.valider_fiche_ideation(fiche_brute(piege="1) préparer le terrain\n2) agir ensuite"), "a", 1)
        self.assertTrue(idn.signaux_niveau_methode(idn.vue_servie(f)))

    def test_classes_de_temoins_imposees(self):
        p = os.path.join(self.tmp, "t.json")

        def ecrire(temoins):
            with open(p, "w", encoding="utf-8") as f:
                json.dump({"temoins": temoins}, f, ensure_ascii=False)
            return idn.construire_liste_blanche([p], os.path.join(self.tmp, f"lb-{len(os.listdir(self.tmp))}.json"))
        complet = [{"fiche": fiche_brute(nom="V"), "attendu": "eligible", "classe": "vrai"},
                   {"fiche": fiche_brute(nom="F1"), "attendu": "ineligible", "classe": "faux_falsifiabilite"},
                   {"fiche": fiche_brute(nom="F2"), "attendu": "ineligible", "classe": "faux_anteriorite"},
                   {"fiche": fiche_brute(nom="J"), "attendu": "eligible", "classe": "jumeau", "jumeau_de": "V"}]
        self.assertEqual(len(idn.charger_temoins(p, ecrire(complet))), 4)
        for mauvais, motif in ((complet[:3], "classe manquante"), (complet[:1] + [dict(complet[1], classe="vrai")] + complet[2:], "faux marqué vrai"),
                               (complet[:3] + [dict(complet[3], jumeau_de=None)], "jumeau sans cible"),
                               (complet[:3] + [dict(complet[3], jumeau_de="X")], "jumeau_de inconnu"),
                               ([dict(t, classe="vrai", attendu="eligible") for t in complet], "une seule classe")):
            with self.assertRaises(idn.FicheIdeationInvalide, msg=motif):
                idn.charger_temoins(p, ecrire(mauvais))


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
                {"fiche": fiche_brute(nom="Sobre fort"), "attendu": "eligible", "classe": "vrai"},
                {"fiche": fiche_brute(nom="Verbeux vide", enonce="Long " * 50), "attendu": "ineligible",
                 "note_max": {"falsifiabilite": 1}, "classe": "faux_falsifiabilite"},
                {"fiche": fiche_brute(nom="Assuré occupé", originalite={"niveau": "inedite", "texte": "jamais vu"}),
                 "attendu": "ineligible", "note_max": {"originalite": 1}, "classe": "faux_anteriorite"},
                {"fiche": fiche_brute(nom="Jumeau"), "attendu": "eligible", "jumeau_de": "Sobre fort", "classe": "jumeau"}]},
                f, ensure_ascii=False)
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
            if f["nom"] == "Assuré occupé":
                sur[f["identifiant"]] = {"avantage": 1, "originalite": 0}
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
        self.assertEqual(res["lecture"]["juges_rendus"], 2)  # v35 : « complet » (toujours vrai) retiré
        self.assertEqual(res["lecture"]["quarantaine_par_proposeur"]["fable"], {"validees": 1, "quarantaine": 1, "taux": 0.5})
        self.assertIn("temoins_hors_fourchette", res["lecture"]["longueur_temoins_contre_fiches"])
        self.assertIsNone(res["journal"]["arret"])
        self.assertTrue(res["journal"]["cout_fictif"])
        for nom in ("manifeste-depart.json", "manifeste-fin.json", "fiches-validees.json", "classement.json",
                    "classements-par-juge.json", "lecture.json", "notes-par-juge.json", "fiches-en-quarantaine.json"):
            self.assertTrue(os.path.exists(os.path.join(sortie, nom + ".sha256")), nom)
        with open(os.path.join(sortie, "manifeste-depart.json")) as f:
            depart = json.load(f)
        self.assertEqual(depart["reglages"]["phase"], "depart")
        self.assertEqual(depart["reglages"]["temoins"]["nombre"], 4)
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
        with self.assertRaises(idn.CourseInterrompue):  # v38 (CL37-03) : somme des plafonds 4 > 1,5 → refus avant tout appel
            self.lancer(ad, "c9a", budget_total_usd=1.5)
        self.assertEqual(ad.appels, [])
        with self.assertRaises(idn.CourseInterrompue):  # tolérée : arrêt au premier dépassement, avant la dépense
            self.lancer(ad, "c9", budget_total_usd=1.5, tolerer_somme_plafonds=True)
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


class TestCommandeExterne(CasAvecDossier):
    """v33 → v36 : juge d'une autre lignée (Argon) par commande externe ; v36 : à poids égal et proposeur à égalité."""

    def commande(self, script, nom="juge.py"):
        chemin = os.path.join(self.tmp, nom)
        with open(chemin, "w", encoding="utf-8") as f:
            f.write(script)
        return [sys.executable, "-I", chemin]

    FICHE = json.dumps(fiche_brute(nom="Argon A"), ensure_ascii=False)
    SCRIPT_OK = (
        "import sys, json, re\n"
        "consigne = sys.stdin.read()\n"
        "if 'exactement OK' in consigne:\n"
        "    print(json.dumps({'texte': 'OK', 'cout_usd': 0.001})); sys.exit(0)\n"
        "if 'passe de proposition' in consigne:\n"
        "    f1 = json.loads(%r); f2 = dict(f1, nom='Argon B')\n"
        "    if 'première passe' in consigne: f1['nom'] = 'Argon A (revue)'\n"
        "    print(json.dumps({'texte': '```json\\n' + json.dumps({'fiches': [f1, f2]}, ensure_ascii=False) + '\\n```', 'cout_usd': 0.25})); sys.exit(0)\n"
        "bloc = json.loads(re.search(r'```json\\n(\\[.*\\])\\n```', consigne, re.S).group(1))\n"
        "par_nom = {f['nom']: f['identifiant'] for f in bloc}\n"
        "notes = []\n"
        "for f in bloc:\n"
        "    c = {k: 2 for k in ('avantage','originalite','falsifiabilite','traitabilite','robustesse')}\n"
        "    if f['nom'] == 'Verbeux vide': c.update({'avantage': 1, 'originalite': 1, 'falsifiabilite': 0})\n"
        "    if f['nom'] == 'Assuré occupé': c.update({'avantage': 1, 'originalite': 0})\n"
        "    if f['nom'].startswith('Argon'): c.update({'avantage': 3})\n"
        "    if f['nom'] == 'O1': c.update({'avantage': 0})\n"
        "    notes.append({'identifiant': f['identifiant'], 'criteres': c, 'justifications': {}})\n"
        "doublons = [[par_nom['Jumeau'], par_nom['Sobre fort']]] if 'Jumeau' in par_nom and 'Sobre fort' in par_nom else []\n"
        "print(json.dumps({'texte': '```json\\n' + json.dumps({'notes': notes, 'doublons': doublons}) + '\\n```', 'cout_usd': 0.3}))\n") % FICHE

    def test_commande_factice_notes_et_controle(self):
        from pole.adaptateurs import AdaptateurCommandeExterne, AdaptateurJugeExterne
        self.assertIs(AdaptateurJugeExterne, AdaptateurCommandeExterne)
        ad = AdaptateurCommandeExterne(self.commande(self.SCRIPT_OK), environnement={})
        r = ad.lancer("juge_ideation", idn.APPEL_DE_CONTROLE_CONSIGNE, self.tmp, 0.1, 1, modele="autre-lignee-x")
        self.assertEqual((r.statut, r.texte_final, r.cout_declare_usd, r.cout_inconnu), ("ok", "OK", 0.001, False))
        with self.assertRaises(ValueError):
            ad.lancer("experimentateur", "x", self.tmp, 1.0, 1)
        self.assertEqual(sorted(ad.description()), ["commande", "delai_s", "empreintes", "variables_transmises"])
        self.assertIn(ad.commande[-1], ad.description()["empreintes"])
        with self.assertRaises(ValueError):
            AdaptateurCommandeExterne(self.commande("x"), delai_s=0)

    def test_artefacts_de_la_commande(self):
        """R5 : coût absent, NaN, infini, nul, négatif, sortie non JSON, code ≠ 0 → erreur ; coût imprimé avant un échec
        compté (CL35-02) ; coût illisible → plafond de session compté et marqué inconnu."""
        from pole.adaptateurs import AdaptateurCommandeExterne
        cas = (("import sys; sys.exit(3)", "erreur", 1.0, True),
               ("print('pas du json')", "erreur", 1.0, True),
               ("import json; print(json.dumps({'texte': 'x', 'cout_usd': 9.0}))", "budget_depasse", 9.0, False),
               ("import json; print(json.dumps({'texte': 'x'}))", "erreur", 1.0, True),
               ("import json; print(json.dumps({'cout_usd': 1}))", "erreur", 1.0, True),
               ("print('{\"texte\": \"x\", \"cout_usd\": NaN}')", "erreur", 1.0, True),
               ("print('{\"texte\": \"x\", \"cout_usd\": Infinity}')", "erreur", 1.0, True),
               ("import json; print(json.dumps({'texte': 'x', 'cout_usd': 0}))", "erreur", 1.0, True),
               ("import json; print(json.dumps({'texte': 'x', 'cout_usd': -1}))", "erreur", 1.0, True),
               ("import json, sys; print(json.dumps({'texte': 'x', 'cout_usd': 0.4})); sys.exit(3)", "erreur", 0.4, False),
               ("import json; print(json.dumps({'texte': 'x', 'cout_usd': 0.5}))", "ok", 0.5, False))
        for script, attendu, cout, inconnu in cas:
            ad = AdaptateurCommandeExterne(self.commande(script), environnement={})
            r = ad.lancer("juge_ideation", "consigne", self.tmp, 1.0, 1)
            self.assertEqual((r.statut, r.cout_declare_usd, r.cout_inconnu), (attendu, cout, inconnu), script)
        from pole.relais import CleDansEnvironnement
        ad = AdaptateurCommandeExterne(self.commande("print(1)"), environnement={"ANTHROPIC_API_KEY": "x"})
        with self.assertRaises(CleDansEnvironnement):
            ad.lancer("juge_ideation", "consigne", self.tmp, 1.0, 1)

    def test_delai_arrete_tout_le_groupe(self):
        """CL35-13 : au délai, le petit-enfant de la commande est arrêté aussi ; coût inconnu → plafond compté."""
        import time
        from pole.adaptateurs import AdaptateurCommandeExterne
        pid_f = os.path.join(self.tmp, "petit-enfant.pid")
        script = ("import subprocess, sys, time\n"
                  f"p = subprocess.Popen([sys.executable, '-c', 'import time; time.sleep(60)'])\n"
                  f"open({pid_f!r}, 'w').write(str(p.pid))\n"
                  "time.sleep(60)\n")
        ad = AdaptateurCommandeExterne(self.commande(script), environnement={}, delai_s=1.5)
        debut = time.monotonic()
        r = ad.lancer("juge_ideation", "consigne", self.tmp, 0.7, 1)
        self.assertLess(time.monotonic() - debut, 10.0)  # M26 : avec `kill` au lieu de `killpg`, le tube tenu par le petit-enfant bloque 60 s
        self.assertEqual((r.statut, r.cout_declare_usd, r.cout_inconnu), ("erreur", 0.7, True))
        self.assertIn("délai", r.erreur)
        pid = int(open(pid_f).read())

        def vivant():
            try:
                with open(f"/proc/{pid}/status") as f:
                    return not any(l.startswith("State:") and "Z" in l for l in f)
            except OSError:
                return False
        for _ in range(30):
            if not vivant():
                break
            time.sleep(0.1)
        else:
            try:
                os.kill(pid, 9)
            except ProcessLookupError:
                pass
            self.fail("le petit-enfant a survécu au délai")

    def test_environnement_minimal_de_la_commande(self):
        """CL34-09 / CL35-05 : environnement explicite et minimal, plus plafond de session et rôle."""
        from pole.adaptateurs import AdaptateurCommandeExterne
        from pole.relais import CleDansEnvironnement
        script = "import os, json; print(json.dumps({'texte': ','.join(sorted(os.environ)), 'cout_usd': 0.01}))"
        env = {"PATH": os.environ.get("PATH", "/usr/bin"), "HOME": "/tmp", "LANG": "C.UTF-8", "HTTPS_PROXY": "http://x",
               "CHEMIN_CLE_JUGE": "/dev/null", "AUTRE": "1"}
        ad = AdaptateurCommandeExterne(self.commande(script), environnement=env, variables_transmises=("CHEMIN_CLE_JUGE",))
        self.assertEqual(sorted(ad.environnement_commande()), ["CHEMIN_CLE_JUGE", "HOME", "LANG", "PATH"])
        r = ad.lancer("juge_ideation", "consigne", self.tmp, 1.0, 1)
        self.assertEqual(r.statut, "ok")
        self.assertEqual(r.texte_final, "CHEMIN_CLE_JUGE,HOME,LANG,PATH,PLAFOND_SESSION_USD,ROLE_POLE")
        with self.assertRaises(CleDansEnvironnement):
            AdaptateurCommandeExterne(self.commande(script), environnement=env, variables_transmises=("ANTHROPIC_API_KEY",))

    def cours(self):
        c = TestCourse("test_course_complete")
        c.tmp = self.tmp
        return c

    def test_adaptateur_principal_externe_refuse(self):
        """CL35-06 : une commande externe ne peut pas être l'adaptateur principal (ni le rôle réel d'un mixte)."""
        from pole.adaptateurs import AdaptateurCommandeExterne
        c = self.cours()
        ad = AdaptateurCommandeExterne(self.commande(self.SCRIPT_OK), environnement={})
        with self.assertRaises(idn.CourseInterrompue):
            c.lancer(ad, "cx-principal")
        self.assertFalse(os.path.exists(os.path.join(self.tmp, "cx-principal")))

        class Mixte:
            nom = "mixte"
            reel = ad
        with self.assertRaises(idn.CourseInterrompue):
            c.lancer(Mixte(), "cx-mixte")
        # moteur réel déclaré avec un adaptateur qui n'est pas celui du kit
        faux = FauxAdaptateur({"opus": [fiche_brute()], "fable": [fiche_brute()]})
        with self.assertRaises(idn.CourseInterrompue):
            c.lancer(faux, "cx-moteur", moteur="claude-sdk")
        self.assertEqual(faux.appels, [])

    def test_proposeur_externe_dans_la_course(self):
        """n° 119 : Argon propose à égalité dans la course (question et pièces) ; sa seconde passe exige l'attestation du
        matériau ; il ne voit jamais les fiches des autres ; plafond externe séparé."""
        from pole.adaptateurs import AdaptateurCommandeExterne
        c = self.cours()
        fiches = {"opus": [fiche_brute(nom="O1")], "fable": [fiche_brute(nom="F1")]}
        ad = FauxAdaptateur(fiches, notes_par_juge={"juge-fable": c.notes_temoins_ok, "juge-opus": c.notes_temoins_ok})
        ext = AdaptateurCommandeExterne(self.commande(self.SCRIPT_OK), environnement={})
        budgets = dict(c.budgets())
        budgets[("proposeur_ideation", "gemini-argon")] = 1.0
        prop_ext = [("argon", "gemini-argon", ext)]
        with self.assertRaises(idn.CourseInterrompue):  # plafond externe nul
            c.lancer(ad, "cx-0", budgets=budgets, proposeurs_externes=prop_ext, budget_externe_usd=0.0)
        with self.assertRaises(idn.CourseInterrompue):  # seconde passe avec matériau sans attestation : refus avant tout appel
            c.lancer(ad, "cx-1", budgets=budgets, proposeurs_externes=prop_ext, budget_externe_usd=3.0, seconde_passe=True)
        self.assertEqual(ad.appels, [])
        res = c.lancer(ad, "cx-2", budgets=budgets, proposeurs_externes=prop_ext, budget_externe_usd=3.0)
        auteurs = {f["auteur"] for f in res["fiches"]}
        self.assertEqual(auteurs, {"opus", "fable", "argon"})
        self.assertAlmostEqual(res["journal"]["cout_externe_usd"], 0.25)
        self.assertAlmostEqual(res["journal"]["cout_total_usd"], 4 * 0.5)
        self.assertEqual(res["lecture"]["quarantaine_par_proposeur"]["argon"]["validees"], 2)
        # attestation du matériau scellée → seconde passe ; Argon reçoit le matériau et SES fiches seulement
        att = os.path.join(self.tmp, "attestation-materiau.json")
        prep = c._prep
        idn.ecrire_json_scelle(att, {"lecteur": "Lazar", "lu_le": "2026-10-28",
                                     "materiau_sha256": {os.path.basename(prep["materiau"][0]):
                                                         idn.sha256_fichier(prep["materiau"][0])}})
        res = c.lancer(ad, "cx-3", budgets=budgets, proposeurs_externes=prop_ext, budget_externe_usd=3.0,
                       seconde_passe=True, attestation_materiau=att)
        consigne2 = open(os.path.join(self.tmp, "cx-3", "proposeurs", "traces-argon", "passe-2", "consigne.md")
                         if os.path.exists(os.path.join(self.tmp, "cx-3", "proposeurs", "traces-argon", "passe-2", "consigne.md"))
                         else os.path.join(self.tmp, "cx-3", "proposeurs", "argon", "traces-passe-2", "consigne.md"),
                         encoding="utf-8").read()
        self.assertIn("Matériau servi", consigne2)
        self.assertIn("Argon A", consigne2)
        self.assertNotIn('"O1"', consigne2)
        self.assertNotIn('"F1"', consigne2)
        self.assertEqual(sum(1 for f in res["fiches"] if f["auteur"] == "argon" and f["passe"] == 2), 2)
        # attestation à l'empreinte fausse → refus avant tout appel
        att2 = os.path.join(self.tmp, "attestation-materiau-fausse.json")
        idn.ecrire_json_scelle(att2, {"lecteur": "Lazar", "lu_le": "2026-10-28",
                                      "materiau_sha256": {os.path.basename(prep["materiau"][0]): "0" * 64}})
        n = len(ad.appels)
        with self.assertRaises(idn.CourseInterrompue):
            c.lancer(ad, "cx-4", budgets=budgets, proposeurs_externes=prop_ext, budget_externe_usd=3.0,
                     seconde_passe=True, attestation_materiau=att2)
        self.assertEqual(len(ad.appels), n)

    def attester(self, chemin, sortie, etiquette="argon"):
        consigne = os.path.join(sortie, "juges-bras-rapporte", f"traces-{etiquette}", "consigne-en-attente.md")
        idn.ecrire_json_scelle(chemin, {"lecteur": "Lazar", "lu_le": "2026-10-28",
                                        "fiches_validees_sha256": idn.sha256_fichier(os.path.join(sortie, "fiches-validees.json")),
                                        "consignes_en_attente_sha256": {etiquette: idn.sha256_fichier(consigne)}})
        return chemin

    def test_bras_differe_a_poids_egal(self):
        """CL34-01, CL34-04, n° 118 : la course n'appelle jamais le juge externe et n'écrit aucun classement ; le bras,
        après attestation scellée, note à poids égal : classement à trois juges (médiane), accords par paire ; jamais rejoué."""
        from pole.adaptateurs import AdaptateurCommandeExterne
        c = self.cours()
        fiches = {"opus": [fiche_brute(nom="O1"), fiche_brute(nom="O2")], "fable": [fiche_brute(nom="F1")]}
        ad = FauxAdaptateur(fiches, notes_par_juge={"juge-fable": c.notes_temoins_ok, "juge-opus": c.notes_temoins_ok})
        externe = AdaptateurCommandeExterne(self.commande(self.SCRIPT_OK), environnement={})
        budgets = dict(c.budgets())
        budgets[("juge_ideation", "autre-lignee-x")] = 1.0
        # R5 : attestation donnée à la course → refus avant tout appel
        with self.assertRaises(idn.CourseInterrompue):
            c.lancer(ad, "cx-refus", budgets=budgets, juges_externes=[("argon", "autre-lignee-x")],
                     attestation_lecture_humaine=os.path.join(self.tmp, "x.json"))
        self.assertEqual(ad.appels, [])
        res = c.lancer(ad, "cx", budgets=budgets, juges_externes=[("argon", "autre-lignee-x")], budget_externe_usd=2.0)
        sortie = os.path.join(self.tmp, "cx")
        self.assertTrue(res["en_attente_bras"])
        self.assertIsNone(res["classement"])
        for nom in ("classement.json", "classements-par-juge.json", "lecture.json"):
            self.assertFalse(os.path.exists(os.path.join(sortie, nom)), nom)
        for nom in ("lecture-course.json", "notes-par-juge.json", "noyau/temoins-servis.json", "noyau/modeles.json",
                    "juges-bras-rapporte/traces-argon/consigne-en-attente.md"):
            self.assertTrue(os.path.exists(os.path.join(sortie, nom + ".sha256")), nom)
        self.assertTrue(all("argon" not in os.path.relpath(a["dossier"], sortie) for a in ad.appels))
        externes = [("argon", "autre-lignee-x", externe)]
        # attestation non scellée → refus
        att_nue = os.path.join(self.tmp, "att-nue.json")
        with open(att_nue, "w") as f:
            json.dump({"lecteur": "Lazar"}, f)
        with self.assertRaises(idn.CourseInterrompue):
            idn.executer_bras_differe(sortie, attestation_lecture_humaine=att_nue, budgets=budgets, juges_externes=externes)
        # attestation scellée mais consigne fausse → refus ; aucun manifeste du bras
        att_f = os.path.join(self.tmp, "att-fausse.json")
        idn.ecrire_json_scelle(att_f, {"lecteur": "Lazar", "lu_le": "2026-10-28",
                                       "fiches_validees_sha256": idn.sha256_fichier(os.path.join(sortie, "fiches-validees.json")),
                                       "consignes_en_attente_sha256": {"argon": "0" * 64}})
        with self.assertRaises(idn.CourseInterrompue):
            idn.executer_bras_differe(sortie, attestation_lecture_humaine=att_f, budgets=budgets, juges_externes=externes)
        att = self.attester(os.path.join(self.tmp, "att.json"), sortie)
        # juges donnés ≠ course → refus ; plafond externe insuffisant → refus AVANT le contrôle (CL35-05), sans manifeste
        with self.assertRaises(idn.CourseInterrompue):
            idn.executer_bras_differe(sortie, attestation_lecture_humaine=att, budgets=budgets,
                                      juges_externes=[("argon", "autre-modele", externe)])
        with self.assertRaises(idn.CourseInterrompue):
            idn.executer_bras_differe(sortie, attestation_lecture_humaine=att, budgets=budgets, juges_externes=externes,
                                      budget_externe_usd=0.5)
        self.assertFalse(os.path.exists(os.path.join(sortie, "manifeste-bras-rapporte.json")))
        self.assertFalse(os.path.exists(os.path.join(sortie, "bras-rapporte-controle")))
        # cas sain : trois juges
        apres = idn.executer_bras_differe(sortie, attestation_lecture_humaine=att, budgets=budgets, juges_externes=externes)
        self.assertFalse(apres["sans_bras"])
        self.assertTrue(all(l["nombre_juges"] == 3 and l["nom_agregat"] == "mediane" for l in apres["classement"]))
        o1 = next(l for l in apres["classement"] if l["identifiant_auteur"] == "opus-p1-01")
        self.assertEqual(o1["agregat"]["avantage"], 2)  # notes (2, 2, 0) : médiane 2, pas la moyenne 1,33
        self.assertEqual(o1["par_juge"]["argon"]["avantage"], 0)
        self.assertEqual(sorted(apres["lecture"]["juges_agreges"]), ["argon", "juge-fable", "juge-opus"])
        self.assertEqual(len(apres["lecture"]["accords_de_rang_par_paire"]), 3)
        self.assertTrue(apres["lecture"]["temoins"]["temoins_ok"])
        self.assertTrue(apres["lecture"]["temoins_juge_externe"]["temoins_ok"])
        self.assertTrue(apres["lecture"]["lisible_L2_L4"])
        self.assertIn("argon", apres["lecture"]["auto_preference"])
        self.assertEqual(apres["journal"]["controle"]["argon"]["texte"], "OK")
        self.assertFalse(apres["journal"]["cout_fictif"])
        for nom in ("classement.json", "classements-par-juge.json", "lecture.json", "manifeste-bras-rapporte.json",
                    "notes-bras-rapporte.json"):
            self.assertTrue(os.path.exists(os.path.join(sortie, nom + ".sha256")), nom)
        with open(os.path.join(sortie, "manifeste-bras-rapporte.json")) as f:
            m = json.load(f)["reglages"]
        self.assertEqual(m["commande_externe"][0]["commande"], externe.commande)  # CL35-03
        # rejeu → refus
        with self.assertRaises(idn.CourseInterrompue):
            idn.executer_bras_differe(sortie, attestation_lecture_humaine=att, budgets=budgets, juges_externes=externes)

    def test_bras_en_panne_classement_sans_bras(self):
        """n° 118 point 3 : Argon en panne → classement à deux juges marqué illisible, manifeste avec l'erreur, code distinct ;
        témoins échoués chez Argon → classement à trois juges illisible."""
        from pole.adaptateurs import AdaptateurCommandeExterne
        c = self.cours()
        fiches = {"opus": [fiche_brute(nom="O1"), fiche_brute(nom="O2")], "fable": [fiche_brute(nom="F1")]}
        ad = FauxAdaptateur(fiches, notes_par_juge={"juge-fable": c.notes_temoins_ok, "juge-opus": c.notes_temoins_ok})
        budgets = dict(c.budgets())
        budgets[("juge_ideation", "autre-lignee-x")] = 1.0
        panne = AdaptateurCommandeExterne(self.commande(
            "import sys, json\nc = sys.stdin.read()\n"
            "if 'exactement OK' in c: print(json.dumps({'texte': 'OK', 'cout_usd': 0.001})); sys.exit(0)\n"
            "print(json.dumps({'texte': 'x', 'cout_usd': 0.2})); sys.exit(3)\n", "panne.py"), environnement={})
        c.lancer(ad, "cp", budgets=budgets, juges_externes=[("argon", "autre-lignee-x")], budget_externe_usd=2.0)
        sortie = os.path.join(self.tmp, "cp")
        att = self.attester(os.path.join(self.tmp, "att-p.json"), sortie)
        with self.assertRaises(idn.SansJugeExterne) as cm:
            idn.executer_bras_differe(sortie, attestation_lecture_humaine=att, budgets=budgets,
                                      juges_externes=[("argon", "autre-lignee-x", panne)])
        res = cm.exception.resultat
        self.assertTrue(res["sans_bras"])
        self.assertTrue(all(l["nombre_juges"] == 2 for l in res["classement"]))
        self.assertFalse(res["lecture"]["lisible_L2_L4"])
        self.assertAlmostEqual(res["journal"]["cout_total_usd"], 0.201)  # le coût imprimé avant l'échec est compté
        self.assertTrue(os.path.exists(os.path.join(sortie, "classement-sans-bras.json.sha256")))
        self.assertFalse(os.path.exists(os.path.join(sortie, "classement.json")))
        with open(os.path.join(sortie, "manifeste-bras-rapporte.json")) as f:
            self.assertIn("code 3", json.load(f)["reglages"]["erreur"])
        # témoins échoués chez Argon : trois juges, illisible
        mauvais = AdaptateurCommandeExterne(self.commande(self.SCRIPT_OK.replace("'avantage': 1, 'originalite': 0", "'avantage': 3, 'originalite': 3"), "mauvais.py"), environnement={})
        c.lancer(ad, "ct", budgets=budgets, juges_externes=[("argon", "autre-lignee-x")], budget_externe_usd=2.0)
        sortie = os.path.join(self.tmp, "ct")
        att = self.attester(os.path.join(self.tmp, "att-t.json"), sortie)
        apres = idn.executer_bras_differe(sortie, attestation_lecture_humaine=att, budgets=budgets,
                                          juges_externes=[("argon", "autre-lignee-x", mauvais)])
        self.assertFalse(apres["lecture"]["lisible_L2_L4"])
        self.assertFalse(apres["lecture"]["temoins_juge_externe"]["temoins_ok"])
        self.assertTrue(all(l["nombre_juges"] == 3 for l in apres["classement"]))

    def test_bras_simule_sur_course_reelle_refuse(self):
        """CL35-04 : course marquée réelle (adaptateur du kit, modèles permis) → un adaptateur qui n'est pas une commande
        externe est refusé avant tout écrit ; CL35-03 : la commande est consignée ; CL36-03 : Argon obligatoire."""
        from pole.adaptateurs import AdaptateurCommandeExterne
        c = self.cours()
        fiches = {"opus": [fiche_brute(nom="O1")], "fable": [fiche_brute(nom="F1")]}
        ad = FauxAdaptateur(fiches, notes_par_juge={"juge-fable": c.notes_temoins_ok, "juge-opus": c.notes_temoins_ok})
        ad.nom = "claude-sdk"
        budgets = dict(c.budgets())
        budgets[("juge_ideation", "autre-lignee-x")] = 1.0
        budgets[("proposeur_ideation", "gemini-argon")] = 1.0
        ext = AdaptateurCommandeExterne(self.commande(self.SCRIPT_OK), environnement={})
        with self.assertRaises(idn.CourseInterrompue):  # CL36-03 : course réelle sans Argon proposeur ET juge → refus
            c.lancer(ad, "cr0", budgets=budgets, juges_externes=[("argon", "autre-lignee-x")], budget_externe_usd=2.0,
                     moteur="claude-sdk")
        self.assertEqual(ad.appels, [])
        c.lancer(ad, "cr", budgets=budgets, juges_externes=[("argon", "autre-lignee-x")], budget_externe_usd=4.0,
                 proposeurs_externes=[("argon-p", "gemini-argon", ext)], moteur="claude-sdk")
        sortie = os.path.join(self.tmp, "cr")
        att = self.attester(os.path.join(self.tmp, "att-r.json"), sortie)
        simule = FauxAdaptateur({}, notes_par_juge={"argon": c.notes_temoins_ok})
        with self.assertRaises(idn.CourseInterrompue):
            idn.executer_bras_differe(sortie, attestation_lecture_humaine=att, budgets=budgets,
                                      juges_externes=[("argon", "autre-lignee-x", simule)])
        self.assertEqual(simule.appels, [])
        self.assertFalse(os.path.exists(os.path.join(sortie, "manifeste-bras-rapporte.json")))
        # proposeur externe sans juge externe sur une course réelle : refusé (CL36-03, « juge oublié », n° 118)
        with self.assertRaises(idn.CourseInterrompue) as cm:
            c.lancer(ad, "cr1", budgets=budgets, proposeurs_externes=[("argon-p", "gemini-argon", ext)],
                     budget_externe_usd=4.0, moteur="claude-sdk")
        self.assertIn("obligatoires", str(cm.exception))
        # et un proposeur externe simulé sur une course réelle est refusé aussi (CL35-04), juge externe présent
        with self.assertRaises(idn.CourseInterrompue) as cm:
            c.lancer(ad, "cr2", budgets=budgets, juges_externes=[("argon", "autre-lignee-x")],
                     proposeurs_externes=[("argon-p", "gemini-argon", simule)], budget_externe_usd=4.0, moteur="claude-sdk")
        self.assertIn("CL35-04", str(cm.exception))


    def test_bras_non_joue_relancable(self):
        """CL36-01 : commande introuvable ou clé dans l'environnement → rien envoyé, rien dépensé : manifeste « non joué »
        numéroté, bras relançable ; puis le bras se joue."""
        from pole.adaptateurs import AdaptateurCommandeExterne
        c = self.cours()
        fiches = {"opus": [fiche_brute(nom="O1")], "fable": [fiche_brute(nom="F1")]}
        ad = FauxAdaptateur(fiches, notes_par_juge={"juge-fable": c.notes_temoins_ok, "juge-opus": c.notes_temoins_ok})
        budgets = dict(c.budgets())
        budgets[("juge_ideation", "autre-lignee-x")] = 1.0
        c.lancer(ad, "cn", budgets=budgets, juges_externes=[("argon", "autre-lignee-x")], budget_externe_usd=2.0)
        sortie = os.path.join(self.tmp, "cn")
        att = self.attester(os.path.join(self.tmp, "att-n.json"), sortie)
        introuvable = AdaptateurCommandeExterne(["/chemin/qui/n/existe/pas"], environnement={})
        with self.assertRaises(idn.CourseInterrompue) as cm:
            idn.executer_bras_differe(sortie, attestation_lecture_humaine=att, budgets=budgets,
                                      juges_externes=[("argon", "autre-lignee-x", introuvable)])
        self.assertIn("non joué", str(cm.exception))
        self.assertTrue(os.path.exists(os.path.join(sortie, "manifeste-bras-non-joue-1.json.sha256")))
        self.assertFalse(os.path.exists(os.path.join(sortie, "manifeste-bras-rapporte.json")))
        cle_env = AdaptateurCommandeExterne(self.commande(self.SCRIPT_OK), environnement={"ANTHROPIC_API_KEY": "x"})
        with self.assertRaises(idn.CourseInterrompue):
            idn.executer_bras_differe(sortie, attestation_lecture_humaine=att, budgets=budgets,
                                      juges_externes=[("argon", "autre-lignee-x", cle_env)])
        self.assertTrue(os.path.exists(os.path.join(sortie, "manifeste-bras-non-joue-2.json")))
        # attestation complète mais au sceau faux (modifiée après scellement) → refus
        att_f = os.path.join(self.tmp, "att-n-fausse.json")
        self.attester(att_f, sortie)
        with open(att_f, "a") as f:
            f.write("\n")
        with self.assertRaises(idn.CourseInterrompue) as cm:
            idn.executer_bras_differe(sortie, attestation_lecture_humaine=att_f, budgets=budgets,
                                      juges_externes=[("argon", "autre-lignee-x", introuvable)])
        self.assertIn("sceau", str(cm.exception))  # CL39-12 : le motif est bien le sceau
        self.assertFalse(os.path.exists(os.path.join(sortie, "juges-bras-rapporte", "traces-argon", "reponse.md")))  # M28
        # CL37-02 : contrôle « KO » qui a coûté 0,15 → tentative payée, coût scellé, imputé au plafond externe
        ko = AdaptateurCommandeExterne(self.commande(
            "import sys, json\nc = sys.stdin.read()\nprint(json.dumps({'texte': 'KO', 'cout_usd': 0.15}))\n", "ko.py"),
            environnement={})
        with self.assertRaises(idn.CourseInterrompue) as cm:
            idn.executer_bras_differe(sortie, attestation_lecture_humaine=att, budgets=budgets,
                                      juges_externes=[("argon", "autre-lignee-x", ko)])
        self.assertIn("0.1500 USD comptés", str(cm.exception))
        self.assertTrue(os.path.exists(os.path.join(sortie, "bras-tentative-3.json.sha256")))
        with open(os.path.join(sortie, "bras-tentative-3.json")) as f:
            self.assertAlmostEqual(json.load(f)["reglages"]["journal"]["cout_total_usd"], 0.15)
        # trois tentatives faites : plus de relance
        bon = AdaptateurCommandeExterne(self.commande(self.SCRIPT_OK), environnement={})
        with self.assertRaises(idn.CourseInterrompue) as cm:
            idn.executer_bras_differe(sortie, attestation_lecture_humaine=att, budgets=budgets,
                                      juges_externes=[("argon", "autre-lignee-x", bon)])
        self.assertIn("tentatives", str(cm.exception))
        self.assertFalse(os.path.exists(os.path.join(sortie, "manifeste-bras-rapporte.json")))
        # course neuve : une tentative payée, puis le bras joué avec le coût précédent imputé
        c.lancer(ad, "cn2", budgets=budgets, juges_externes=[("argon", "autre-lignee-x")], budget_externe_usd=2.0)
        sortie2 = os.path.join(self.tmp, "cn2")
        att2 = self.attester(os.path.join(self.tmp, "att-n2.json"), sortie2)
        with self.assertRaises(idn.CourseInterrompue):
            idn.executer_bras_differe(sortie2, attestation_lecture_humaine=att2, budgets=budgets,
                                      juges_externes=[("argon", "autre-lignee-x", ko)])
        apres = idn.executer_bras_differe(sortie2, attestation_lecture_humaine=att2, budgets=budgets,
                                          juges_externes=[("argon", "autre-lignee-x", bon)])
        self.assertFalse(apres["sans_bras"])
        self.assertAlmostEqual(apres["journal"]["cout_tentatives_precedentes_usd"], 0.15)
        self.assertEqual(apres["journal"]["tentative"], 2)
        self.assertTrue(os.path.exists(os.path.join(sortie2, "manifeste-bras-rapporte.json")))


class TestLanceurV37(CasAvecDossier):
    """CL35-07, 08, 09, CL36-03 : le lanceur refuse avec un code, jamais une trace."""

    def lanceur(self):
        import importlib.util
        chemin = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "demonstrations", "ideation_v1.py")
        spec = importlib.util.spec_from_file_location("ideation_v1_lanceur", chemin)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module

    def test_options_refusees(self):
        import contextlib
        import io
        lanceur = self.lanceur()
        base = [os.path.join(self.tmp, "s"), "--liste-blanche", "l", "--question", "q", "--temoins", "t"]
        for options in (["--commande-externe", "x"], ["--delai-session-s", "0"], ["--attestation-lecture-humaine", "a"],
                        ["--nombre", "13"], ["--delai-commande-s", "-1"]):
            with contextlib.redirect_stderr(io.StringIO()):
                with self.assertRaises(SystemExit) as cm:
                    lanceur.principal(base + options)
            self.assertEqual(cm.exception.code, 2, options)
        err = io.StringIO()
        with contextlib.redirect_stderr(err):
            code = lanceur.principal(base + ["--moteur", "claude-sdk"])  # M29 : course réelle sans Argon → refus d'abord
        self.assertEqual(code, 2)
        self.assertIn("obligatoires", err.getvalue())
        err = io.StringIO()
        with contextlib.redirect_stderr(err):  # CL35-08 : non armé → 2, pas une trace
            code = lanceur.principal(base + ["--moteur", "claude-sdk", "--proposeur-externe", "a=x", "--juge-externe", "b=x",
                                             "--commande-externe", "x"])
        self.assertEqual(code, 2)
        self.assertIn("MoteurNonArme", err.getvalue())
        # M31 : --commande-externe avec --juge-externe seul, hors bras → refusé
        with contextlib.redirect_stderr(io.StringIO()):
            with self.assertRaises(SystemExit):
                lanceur.principal(base + ["--juge-externe", "b=x", "--commande-externe", "x"])
        # M18, M21, M22, M30 : défauts du devis en vigueur
        a = lanceur.construire_analyseur()
        self.assertEqual(a.get_default("taille_max_pieces"), 750_000)
        self.assertEqual(a.get_default("delai_commande_s"), 1800.0)
        self.assertEqual(a.get_default("budget_externe_usd"), 11.6)
        self.assertEqual(lanceur.BUDGETS_PAR_DEFAUT[("juge_ideation", "claude-opus-5-5")], 4.0)
        from pole.adaptateurs import DELAI_SESSION_S, AdaptateurCommandeExterne
        self.assertEqual(DELAI_SESSION_S, 3600)
        self.assertEqual(AdaptateurCommandeExterne.DELAI_COMMANDE_S, 1800)
        self.assertEqual(lanceur.BUDGETS_PAR_DEFAUT[("proposeur_ideation", "claude-fable-5-1")], 9.3)  # CL36-04, CL37-03

    def test_controle_argon_avant_toute_passe(self):
        """CL36-02 / CL37-01 : avec une commande factice, le proposeur externe est contrôlé avant toute passe, sous son
        rôle, à la taille réelle des pièces, son coût compté ; Argon joue en tête de chaque passe. Une commande qui casse
        sur une grosse consigne arrête avant tout appel Claude de proposition."""
        import contextlib
        import io
        lanceur = self.lanceur()
        cours = TestCourse("test_course_complete")
        cours.tmp = self.tmp
        prep = cours.preparer()
        cmd = TestCommandeExterne("test_commande_factice_notes_et_controle")
        cmd.tmp = self.tmp
        commande = " ".join(cmd.commande(cmd.SCRIPT_OK))
        sortie = os.path.join(self.tmp, "lanceur-ok")
        base = [sortie, "--liste-blanche", prep["liste_blanche"], "--question", prep["question"], "--piece", prep["pieces"][0],
                "--temoins", prep["temoins"], "--proposeur-externe", "argon=gemini-argon", "--juge-externe",
                "argon-j=gemini-argon", "--commande-externe", commande, "--budget-externe-usd", "9"]
        import unittest.mock
        env_propre = {k: v for k, v in os.environ.items() if k in ("PATH", "HOME", "LANG", "LC_ALL", "TMPDIR")}
        out = io.StringIO()
        with unittest.mock.patch.dict(os.environ, env_propre, clear=True), contextlib.redirect_stdout(out):
            code = lanceur.principal(base)
        self.assertEqual(code, 0, out.getvalue())
        with open(os.path.join(sortie, "manifeste-depart.json")) as f:
            depart = json.load(f)["reglages"]
        ctrl = depart["versions"]["appel_de_controle"]["externe:argon"]
        self.assertEqual(ctrl["role"], "proposeur_ideation")
        self.assertGreater(ctrl["taille_consigne"], depart["taille_pieces_servies"]["proposeurs"])
        self.assertAlmostEqual(depart["cout_externe_deja_engage_usd"], 0.001)
        with open(os.path.join(sortie, "manifeste-fin.json")) as f:
            journal = json.load(f)["reglages"]["journal"]
        self.assertEqual(journal["appels"][0]["etiquette"], "argon")  # CL37-01 : Argon en tête
        self.assertAlmostEqual(journal["cout_externe_usd"], 0.001 + 0.25)
        # commande qui casse au-delà de 100 caractères : refus au contrôle, aucun proposeur Claude appelé
        casse = " ".join(cmd.commande("import sys, json\nc = sys.stdin.read()\n"
                                      "if len(c) > 100: sys.exit(3)\nprint(json.dumps({'texte': 'OK', 'cout_usd': 0.001}))\n",
                                      "casse.py"))
        sortie2 = os.path.join(self.tmp, "lanceur-casse")
        err = io.StringIO()
        with unittest.mock.patch.dict(os.environ, env_propre, clear=True), contextlib.redirect_stdout(io.StringIO()), \
                contextlib.redirect_stderr(err):
            code = lanceur.principal([sortie2 if x == sortie else x for x in base[:-4]] + ["--commande-externe", casse,
                                                                                            "--budget-externe-usd", "9"])
        self.assertEqual(code, 2)
        self.assertIn("appel de contrôle refusé", err.getvalue())
        self.assertFalse(os.path.exists(os.path.join(sortie2, "manifeste-depart.json")))


class TestV40(CasAvecDossier):
    """v40 (relecture CL6) : sommes externes avec le contrôle du bras, plafonds finis, tentatives de contrôle scellées,
    garde du relais avec la dépense, bras interrompu après envoi verrouillé, interruption qui arrête Argon, refus avant
    les contrôles, contrôle simulé par préfixe."""

    def cours(self):
        c = TestCourse("test_course_complete")
        c.tmp = self.tmp
        return c

    def cmd(self):
        c = TestCommandeExterne("test_commande_factice_notes_et_controle")
        c.tmp = self.tmp
        return c

    def lanceur(self):
        return TestLanceurV37("test_options_refusees").lanceur()

    def test_sommes_et_plafonds_non_finis(self):
        """M12 à M14, M17, M19 : somme externe (contrôle du bras compris) refusée au cœur et par verifier_reglages ;
        totaux et plafonds non finis refusés."""
        from pole.adaptateurs import AdaptateurCommandeExterne
        c = self.cours()
        ad = FauxAdaptateur({"opus": [fiche_brute(nom="O1")], "fable": [fiche_brute(nom="F1")]})
        ext = AdaptateurCommandeExterne(self.cmd().commande(self.cmd().SCRIPT_OK), environnement={})
        budgets = dict(c.budgets())
        budgets[("proposeur_ideation", "gemini-argon")] = 1.0
        budgets[("juge_ideation", "autre-lignee-x")] = 1.0
        ext_args = dict(budgets=budgets, proposeurs_externes=[("argon", "gemini-argon", ext)],
                        juges_externes=[("argon-j", "autre-lignee-x")], seconde_passe=False)
        # cœur : 1,0 + 1,0 + 0,2 (contrôle du bras) = 2,2 > 2,1 refusé ; 2,2 accepté
        with self.assertRaises(idn.CourseInterrompue) as cm:
            c.lancer(ad, "s-ext-refus", budget_externe_usd=2.1, **ext_args)
        self.assertIn("externes", str(cm.exception))
        self.assertEqual(ad.appels, [])
        c.lancer(ad, "s-ext-ok", budget_externe_usd=2.2, **ext_args)
        # verifier_reglages : mêmes sommes (M13, M14), plafonds non finis (M19)
        prep = c._prep
        base = dict(liste_blanche=prep["liste_blanche"], question=prep["question"], pieces=prep["pieces"], temoins=prep["temoins"],
                    budgets=budgets, proposeurs=[("opus", "claude-opus-5-5"), ("fable", "claude-fable-5-1")],
                    juges=[("juge-fable", "claude-fable-5-1"), ("juge-opus", "claude-opus-5-5")],
                    proposeurs_externes=[("argon", "gemini-argon")], juges_externes=[("argon-j", "autre-lignee-x")])
        idn.verifier_reglages(budget_total_usd=4.0, budget_externe_usd=2.2, **base)
        with self.assertRaises(idn.CourseInterrompue):
            idn.verifier_reglages(budget_total_usd=3.9, budget_externe_usd=2.2, **base)
        with self.assertRaises(idn.CourseInterrompue):
            idn.verifier_reglages(budget_total_usd=4.0, budget_externe_usd=2.1, **base)
        mauvais = dict(budgets); mauvais[("juge_ideation", "claude-opus-5-5")] = float("nan")
        with self.assertRaises(idn.CourseInterrompue):
            idn.verifier_reglages(budget_total_usd=4.0, budget_externe_usd=2.2, **dict(base, budgets=mauvais))
        with self.assertRaises(idn.CourseInterrompue):
            idn.verifier_reglages(budget_total_usd=4.0, budget_externe_usd=2.2, max_tours=3, **base)  # CL39-07
        # cœur : totaux non finis (M17)
        for champ in ("budget_total_usd", "budget_externe_usd", "cout_deja_engage_usd"):
            with self.assertRaises(idn.CourseInterrompue):
                c.lancer(ad, f"nan-{champ}", **{champ: float("nan")})
        with self.assertRaises(idn.CourseInterrompue):
            c.lancer(ad, "nan-session", budgets=mauvais)

    def test_garde_du_relais(self):
        """CL39-03, M15 : plafond − réserve − dépense ≥ total − plus petit juge."""
        lanceur = self.lanceur()
        budgets = {("juge_ideation", "claude-opus-5-5"): 4.0, ("juge_ideation", "claude-fable-5-1"): 7.0}
        juges = [("a", "claude-opus-5-5"), ("b", "claude-fable-5-1")]
        lu = lanceur.verifier_relais({"plafond_usd": 40, "reserve_par_appel_usd": 4, "depense_usd": 0.0}, 40.0, budgets, juges)
        self.assertEqual(lu["depense_usd"], 0.0)
        with self.assertRaises(idn.CourseInterrompue):  # réserve 10 : 30 < 36
            lanceur.verifier_relais({"plafond_usd": 40, "reserve_par_appel_usd": 10}, 40.0, budgets, juges)
        with self.assertRaises(idn.CourseInterrompue):  # relance après 0,4 dépensés : 35,6 < 36
            lanceur.verifier_relais({"plafond_usd": 40, "reserve_par_appel_usd": 4, "depense_usd": 0.4}, 40.0, budgets, juges)
        lanceur.verifier_relais({}, 40.0, budgets, juges)  # relais muet sur ses plafonds : rien à vérifier

    def test_tentatives_de_controle_scellees(self):
        """CL39-02, CL39-07, CL39-08, M16 : un contrôle refusé est scellé avec son coût dans SORTIE-controle, imputé à la
        relance, borné à trois ; un refus de réglage ou une SORTIE existante tombent avant tout contrôle ; la répétition
        simulée avec un proposeur externe sans commande passe."""
        import contextlib
        import io
        import unittest.mock
        lanceur = self.lanceur()
        c = self.cours()
        prep = c.preparer()
        cmd = self.cmd()
        casse = " ".join(cmd.commande("import sys, json\nc = sys.stdin.read()\nprint(json.dumps({'texte': 'KO', 'cout_usd': 0.15}))\n",
                                      "casse.py"))
        sortie = os.path.join(self.tmp, "l-tent")
        env_propre = {k: v for k, v in os.environ.items() if k in ("PATH", "HOME", "LANG", "LC_ALL", "TMPDIR")}
        base = [sortie, "--liste-blanche", prep["liste_blanche"], "--question", prep["question"], "--piece", prep["pieces"][0],
                "--temoins", prep["temoins"], "--proposeur-externe", "argon=gemini-argon", "--juge-externe",
                "argon-j=gemini-argon", "--budget-externe-usd", "11.2"]
        with unittest.mock.patch.dict(os.environ, env_propre, clear=True), contextlib.redirect_stderr(io.StringIO()):
            for n in (1, 2, 3):
                code = lanceur.principal(base + ["--commande-externe", casse])
                self.assertEqual(code, 2)
                chemin = os.path.join(sortie + "-controle", f"tentative-{n}.json")
                self.assertTrue(os.path.exists(chemin + ".sha256"), n)
                with open(chemin) as f:
                    r = json.load(f)["reglages"]
                self.assertAlmostEqual(r["cout_externe_usd"], 0.15)
                self.assertEqual(r["relancable"], n < 3)
            self.assertFalse(os.path.exists(sortie))
            err = io.StringIO()
            with contextlib.redirect_stderr(err):
                self.assertEqual(lanceur.principal(base + ["--commande-externe", casse]), 2)
            self.assertIn("tentatives", err.getvalue())
            self.assertFalse(os.path.exists(os.path.join(sortie + "-controle", "tentative-4.json")))
        # M16 / CL39-07 : réglage refusé AVANT tout contrôle (aucun dossier de contrôle, commande jamais appelée)
        sortie2 = os.path.join(self.tmp, "l-regl")
        with unittest.mock.patch.dict(os.environ, env_propre, clear=True), contextlib.redirect_stderr(io.StringIO()):
            code = lanceur.principal([sortie2 if x == sortie else x for x in base] + ["--commande-externe", casse,
                                                                                         "--taille-max-pieces", "5"])
        self.assertEqual(code, 2)
        self.assertFalse(os.path.exists(sortie2 + "-controle"))
        os.makedirs(sortie2)
        with unittest.mock.patch.dict(os.environ, env_propre, clear=True), contextlib.redirect_stderr(io.StringIO()):
            code = lanceur.principal([sortie2 if x == sortie else x for x in base] + ["--commande-externe", casse])
        self.assertEqual(code, 2)
        self.assertFalse(os.path.exists(sortie2 + "-controle"))
        # CL39-08 : répétition simulée avec proposeur externe, sans commande
        sortie3 = os.path.join(self.tmp, "l-sim")
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            code = lanceur.principal([sortie3 if x == sortie else x for x in base])
        self.assertEqual(code, 0, out.getvalue())

    def test_bras_interrompu_apres_envoi_verrouille(self):
        """CL39-04 : une exception pendant la session du juge du bras, après envoi, compte le plafond et verrouille."""
        c = self.cours()
        fiches = {"opus": [fiche_brute(nom="O1")], "fable": [fiche_brute(nom="F1")]}
        ad = FauxAdaptateur(fiches, notes_par_juge={"juge-fable": c.notes_temoins_ok, "juge-opus": c.notes_temoins_ok})
        budgets = dict(c.budgets())
        budgets[("juge_ideation", "autre-lignee-x")] = 1.0
        c.lancer(ad, "ci", budgets=budgets, juges_externes=[("argon", "autre-lignee-x")], budget_externe_usd=2.0)
        sortie = os.path.join(self.tmp, "ci")
        cmd = self.cmd()
        att = cmd.attester(os.path.join(self.tmp, "att-ci.json"), sortie)

        class Coupe:
            nom = "commande-externe"

            def lancer(self, role, consigne, dossier, budget_usd, max_tours, modele=None):
                if consigne.startswith(idn.APPEL_DE_CONTROLE_CONSIGNE):
                    return Resultat("OK", [], 0.001, "ok")
                raise RuntimeError("coupé pendant la session")

            def description(self):
                return {"commande": ["coupe"]}
        with self.assertRaises(RuntimeError):
            idn.executer_bras_differe(sortie, attestation_lecture_humaine=att, budgets=budgets,
                                      juges_externes=[("argon", "autre-lignee-x", Coupe())])
        chemin = os.path.join(sortie, "manifeste-bras-rapporte.json")
        self.assertTrue(os.path.exists(chemin))
        with open(chemin) as f:
            j = json.load(f)["reglages"]["journal"]
        self.assertAlmostEqual(j["cout_total_usd"], 1.001)  # contrôle 0,001 + plafond 1,0 de la session interrompue
        self.assertEqual(j["consigne_envoyee"], "argon")
        self.assertFalse(any(f.startswith("bras-tentative") or f.startswith("manifeste-bras-non-joue") for f in os.listdir(sortie)))
        bon = self.cmd()
        from pole.adaptateurs import AdaptateurCommandeExterne
        with self.assertRaises(idn.CourseInterrompue):  # verrouillé
            idn.executer_bras_differe(sortie, attestation_lecture_humaine=att, budgets=budgets,
                                      juges_externes=[("argon", "autre-lignee-x",
                                                       AdaptateurCommandeExterne(bon.commande(bon.SCRIPT_OK), environnement={}))])

    def test_tentative_payee_imputee_et_non_lance(self):
        """M07, M09 : « rien envoyé » exige « aucun processus parti » ; le coût d'une tentative payée réduit le plafond."""
        from pole.adaptateurs import AdaptateurCommandeExterne
        c = self.cours()
        fiches = {"opus": [fiche_brute(nom="O1")], "fable": [fiche_brute(nom="F1")]}
        ad = FauxAdaptateur(fiches, notes_par_juge={"juge-fable": c.notes_temoins_ok, "juge-opus": c.notes_temoins_ok})
        budgets = dict(c.budgets())
        budgets[("juge_ideation", "autre-lignee-x")] = 1.0
        c.lancer(ad, "cp9", budgets=budgets, juges_externes=[("argon", "autre-lignee-x")], budget_externe_usd=1.3)
        sortie = os.path.join(self.tmp, "cp9")
        cmd = self.cmd()
        att = cmd.attester(os.path.join(self.tmp, "att-cp9.json"), sortie)
        ko = AdaptateurCommandeExterne(cmd.commande("import sys, json\nsys.stdin.read()\nprint(json.dumps({'texte': 'KO', 'cout_usd': 0.15}))\n", "ko9.py"),
                                       environnement={})
        with self.assertRaises(idn.CourseInterrompue) as cm:
            idn.executer_bras_differe(sortie, attestation_lecture_humaine=att, budgets=budgets,
                                      juges_externes=[("argon", "autre-lignee-x", ko)])
        self.assertNotIn("non joué", str(cm.exception))  # M07 : un processus est parti → tentative payée, pas « non joué »
        self.assertTrue(os.path.exists(os.path.join(sortie, "bras-tentative-1.json")))
        bon = AdaptateurCommandeExterne(cmd.commande(cmd.SCRIPT_OK), environnement={})
        with self.assertRaises(idn.CourseInterrompue) as cm:  # M09 : 0,15 + 0,2 + 1,0 > 1,3 → plafond externe insuffisant
            idn.executer_bras_differe(sortie, attestation_lecture_humaine=att, budgets=budgets,
                                      juges_externes=[("argon", "autre-lignee-x", bon)])
        self.assertIn("plafond externe", str(cm.exception))

    def test_interruption_arrete_le_groupe_et_compte(self):
        """CL37-07, CL39-05, M20 : une interruption pendant la commande arrête tout son groupe ; la session interrompue
        est comptée au plafond par la course et le manifeste de fin est écrit."""
        import subprocess
        import unittest.mock
        from pole.adaptateurs import AdaptateurCommandeExterne
        cmd = self.cmd()
        ad = AdaptateurCommandeExterne(cmd.commande("import sys, time\nsys.stdin.read()\ntime.sleep(30)\n", "lent.py"), environnement={})
        tues = []
        vrai_communicate = subprocess.Popen.communicate

        lances = []

        def communicate_coupe(self_p, *a, **k):
            if not getattr(self_p, "_deja", False):
                self_p._deja = True
                lances.append(self_p)
                raise KeyboardInterrupt()
            return vrai_communicate(self_p, *a, **k)
        with unittest.mock.patch.object(subprocess.Popen, "communicate", communicate_coupe), \
                unittest.mock.patch("os.killpg", side_effect=lambda pid, sig: tues.append((pid, sig))):
            with self.assertRaises(KeyboardInterrupt):
                ad.lancer("juge_ideation", "consigne", self.tmp, 1.0, 1)
        self.assertEqual(len(tues), 1)  # M20 : le groupe est visé
        for p in lances:  # v41 : `os.killpg` était simulé — la commande lente est arrêtée ici (aucun processus survivant)
            p.kill()
            p.communicate()
        # la course compte la session interrompue au plafond et écrit le manifeste de fin
        c = self.cours()

        class Interrompt(FauxAdaptateur):
            def lancer(self, role, consigne, dossier, budget_usd, max_tours, modele=None):
                raise KeyboardInterrupt()
        ad2 = Interrompt({"opus": [fiche_brute()], "fable": [fiche_brute()]})
        with self.assertRaises(KeyboardInterrupt):
            c.lancer(ad2, "c-int")
        with open(os.path.join(self.tmp, "c-int", "manifeste-fin.json")) as f:
            j = json.load(f)["reglages"]["journal"]
        self.assertEqual(j["appels"][0]["statut"], "interrompue")
        self.assertAlmostEqual(j["cout_total_usd"], 1.0)  # plafond de la session compté
        self.assertIn("taille_consigne", j["appels"][0])


    def test_sigterm_sur_le_lanceur(self):
        """CL39-05 : SIGTERM à l'orchestrateur pendant la session d'Argon → code 2, manifeste de fin écrit avec la session
        comptée au plafond, commande et petit-enfant arrêtés."""
        import signal
        import subprocess
        import time
        c = self.cours()
        prep = c.preparer()
        cmd = self.cmd()
        pid_f = os.path.join(self.tmp, "pe.pid")
        lent = " ".join(cmd.commande(
            "import sys, json, subprocess, time\nc = sys.stdin.read()\n"
            "if 'exactement OK' in c: print(json.dumps({'texte': 'OK', 'cout_usd': 0.001})); sys.exit(0)\n"
            f"p = subprocess.Popen([sys.executable, '-c', 'import time; time.sleep(60)']); open({pid_f!r}, 'w').write(str(p.pid))\n"
            "time.sleep(60)\n", "lent2.py"))
        sortie = os.path.join(self.tmp, "l-term")
        lanceur = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "demonstrations", "ideation_v1.py")
        env = {k: v for k, v in os.environ.items() if k in ("PATH", "HOME", "LANG", "LC_ALL", "TMPDIR")}
        p = subprocess.Popen([sys.executable, "-I", "-B", lanceur, sortie, "--liste-blanche", prep["liste_blanche"], "--question",
                              prep["question"], "--piece", prep["pieces"][0], "--temoins", prep["temoins"], "--proposeur-externe",
                              "argon=gemini-argon", "--juge-externe", "argon-j=gemini-argon", "--commande-externe", lent,
                              "--budget-externe-usd", "11.2"], env=env, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        for _ in range(100):
            if os.path.exists(pid_f):
                break
            time.sleep(0.1)
        else:
            p.kill()
            self.fail("la commande lente n'a pas démarré")
        p.send_signal(signal.SIGTERM)
        out, err = p.communicate(timeout=30)
        self.assertEqual(p.returncode, 2, err.decode("utf-8", "replace"))
        self.assertIn("interruption", err.decode("utf-8", "replace"))
        with open(os.path.join(sortie, "manifeste-fin.json")) as f:
            j = json.load(f)["reglages"]["journal"]
        self.assertEqual(j["appels"][-1]["statut"], "interrompue")
        pe = int(open(pid_f).read())
        for _ in range(30):
            try:
                with open(f"/proc/{pe}/status") as f:
                    if any(l.startswith("State:") and "Z" in l for l in f):
                        break
            except OSError:
                break
            time.sleep(0.1)
        else:
            os.kill(pe, 9)
            self.fail("le petit-enfant d'Argon a survécu au SIGTERM")


def _lire(chemin):
    with open(chemin, encoding="utf-8") as f:
        return f.read()


class TestV41(CasAvecDossier):
    """v41 (relecture CL7 de la v40) : contrôle interrompu compté au plafond (CL40-02), même contrôle du bras au lanceur
    et au cœur et refus du cœur scellé (CL40-03), contrôle à la taille réelle et passe 2 d'Argon juste après sa passe 1
    (CL40-04), `relancable` calculé et contrôle Claude payé (CL40-01, code), deux tolérances, valeurs non finies du
    chemin de l'argent (CL40-05), classement sans bras après envoi (CL40-08), M07 (CL40-07), écrits (CL40-09)."""

    ENV = ("PATH", "HOME", "LANG", "LC_ALL", "TMPDIR")

    def cours(self):
        c = TestCourse("test_course_complete")
        c.tmp = self.tmp
        return c

    def cmd(self):
        c = TestCommandeExterne("test_commande_factice_notes_et_controle")
        c.tmp = self.tmp
        return c

    def lanceur(self, cout_controle_claude=None):
        """Lanceur chargé à neuf ; avec `cout_controle_claude`, le contrôle Claude simulé rend ce coût (moteur simulé payé)."""
        lanceur = TestLanceurV37("test_options_refusees").lanceur()
        if cout_controle_claude is not None:
            original = lanceur.AdaptateurIdeationSimule.lancer

            def lancer(s, role, consigne, dossier, budget_usd, max_tours, modele=None):
                if consigne.startswith(idn.APPEL_DE_CONTROLE_CONSIGNE):
                    return Resultat("OK", [], cout_controle_claude, "ok")
                return original(s, role, consigne, dossier, budget_usd, max_tours, modele)
            lanceur.AdaptateurIdeationSimule.lancer = lancer
        return lanceur

    def env_propre(self):
        return {k: v for k, v in os.environ.items() if k in self.ENV}

    def principal(self, lanceur, argv):
        """Appelle le lanceur dans un environnement sans variable de clé ; rend (code, sortie, erreur)."""
        import contextlib
        import io
        import unittest.mock
        out, err = io.StringIO(), io.StringIO()
        with unittest.mock.patch.dict(os.environ, self.env_propre(), clear=True), contextlib.redirect_stdout(out), \
                contextlib.redirect_stderr(err):
            code = lanceur.principal(argv)
        return code, out.getvalue(), err.getvalue()

    def prep_devis(self):
        """Pièces des essais, matériau attesté : réglages du devis v7 quinquies (seconde passe, Argon proposeur et juge)."""
        prep = self.cours().preparer()
        att = os.path.join(self.tmp, "att-materiau.json")
        idn.ecrire_json_scelle(att, {"lecteur": "Lazar", "lu_le": "2026-10-29", "materiau_sha256": {
            os.path.basename(prep["materiau"][0]): idn.sha256_fichier(prep["materiau"][0])}})
        return prep, att

    def base(self, sortie, prep, att=None, *options):
        b = [sortie, "--liste-blanche", prep["liste_blanche"], "--question", prep["question"], "--piece", prep["pieces"][0],
             "--temoins", prep["temoins"], "--proposeur-externe", "argon=gemini-argon", "--juge-externe", "argon-j=gemini-argon"]
        if att:
            b += ["--materiau", prep["materiau"][0], "--seconde-passe", "--attestation-materiau", att]
        return b + list(options)

    def script(self, corps, nom):
        return " ".join(self.cmd().commande(corps, nom))

    SCRIPT_PLAFOND = (  # Argon au pire cas : chaque appel rend son plafond de session
        "import sys, json, os\nc = sys.stdin.read()\ncout = float(os.environ['PLAFOND_SESSION_USD'])\n"
        "if c.startswith('Réponds exactement OK'): print(json.dumps({'texte': 'OK', 'cout_usd': cout})); sys.exit(0)\n"
        "if os.environ['ROLE_POLE'] == 'juge_ideation':\n"
        "    import re\n"
        "    bloc = json.loads(re.search(r'```json\\n(\\[.*\\])\\n```', c, re.S).group(1)); par_nom = {f['nom']: f['identifiant'] for f in bloc}\n"
        "    notes = []\n"
        "    for f in bloc:\n"
        "        k = {x: 2 for x in ('avantage', 'originalite', 'falsifiabilite', 'traitabilite', 'robustesse')}\n"
        "        if f['nom'] in ('Verbeux vide', 'Assuré occupé'): k.update({'avantage': 1, 'originalite': 0, 'falsifiabilite': 0})\n"
        "        notes.append({'identifiant': f['identifiant'], 'criteres': k, 'justifications': {}})\n"
        "    d = [[par_nom['Jumeau'], par_nom['Sobre fort']]]\n"
        "    print(json.dumps({'texte': '```json\\n' + json.dumps({'notes': notes, 'doublons': d}) + '\\n```', 'cout_usd': cout})); sys.exit(0)\n"
        "f1 = json.loads(%r); f2 = dict(f1, nom='Argon B')\n"
        "if 'première passe' in c: f1['nom'] = 'Argon A revue'; f2['nom'] = 'Argon B revue'\n"
        "print(json.dumps({'texte': '```json\\n' + json.dumps({'fiches': [f1, f2]}, ensure_ascii=False) + '\\n```', "
        "'cout_usd': cout}))\n") % json.dumps(fiche_brute(nom="Argon A"), ensure_ascii=False)

    # --- CL40-02 ---------------------------------------------------------------------------------------------------------

    def test_controle_interrompu_compte_le_plafond_et_garde_les_lectures(self):
        """CL40-02 : une exception au contrôle du second modèle compte son plafond et garde la lecture (et le coût) du
        premier ; une interruption remonte telle quelle, lectures jointes ; une clé dans l'environnement (rien lancé) compte 0."""
        from pole.relais import CleDansEnvironnement

        class Panne:
            nom = "panne"

            def __init__(self, exc):
                self.exc = exc

            def lancer(self, role, consigne, dossier, budget_usd, max_tours, modele=None):
                if modele == "claude-opus-5-5":
                    raise self.exc
                return Resultat("OK", [], 0.01, "ok")
        sortie = os.path.join(self.tmp, "ctrl-int")
        modeles = ["claude-fable-5-1", "claude-opus-5-5"]
        with self.assertRaises(idn.ControleRefuse) as cm:
            idn.appel_de_controle(Panne(RuntimeError("panne de l'adaptateur")), modeles, sortie, 0.2)
        lec = cm.exception.lecture
        self.assertAlmostEqual(lec["claude-fable-5-1"]["cout_compte_usd"], 0.01)  # premier modèle : payé, gardé
        self.assertEqual(lec["claude-opus-5-5"]["statut"], "interrompue")
        self.assertAlmostEqual(idn.cout_compte_controle(lec["claude-opus-5-5"]), 0.2)  # plafond, jamais 0
        self.assertTrue(lec["claude-opus-5-5"]["cout_inconnu"])
        self.assertAlmostEqual(sum(idn.cout_compte_controle(c) for c in lec.values()), 0.21)
        with self.assertRaises(KeyboardInterrupt) as cm2:
            idn.appel_de_controle(Panne(KeyboardInterrupt("signal 15")), modeles, sortie, 0.2)
        self.assertAlmostEqual(sum(idn.cout_compte_controle(c) for c in cm2.exception.lecture.values()), 0.21)
        with self.assertRaises(CleDansEnvironnement) as cm3:  # levée avant tout lancement : rien compté
            idn.appel_de_controle(Panne(CleDansEnvironnement("clé")), modeles, sortie, 0.2)
        self.assertEqual(idn.cout_compte_controle(cm3.exception.lecture["claude-opus-5-5"]), 0.0)
        self.assertTrue(cm3.exception.lecture["claude-opus-5-5"]["non_lance"])
        # cas sain inchangé
        self.assertEqual(idn.appel_de_controle(Panne(None), ["claude-fable-5-1"], sortie, 0.2)["claude-fable-5-1"]["problemes"], [])

    def _attendre_pids(self, pid_f, p):
        import time
        for _ in range(150):
            if os.path.exists(pid_f) and _lire(pid_f).strip():
                return
            time.sleep(0.1)
        p.kill()
        p.communicate()
        self.fail("la commande lente n'a pas démarré")

    def _morts(self, pids):
        import time
        for pe in pids:
            for _ in range(50):
                try:
                    with open(f"/proc/{pe}/status") as f:
                        if any(l.startswith("State:") and "Z" in l for l in f):
                            break
                except OSError:
                    break
                time.sleep(0.1)
            else:
                os.kill(pe, 9)
                self.fail(f"processus {pe} survivant au SIGTERM")

    SCRIPT_LENT_CONTROLE = (
        "import sys, json, os, subprocess, time\nc = sys.stdin.read()\n"
        "if c.startswith('Réponds exactement OK'):\n"
        "    p = subprocess.Popen([sys.executable, '-c', 'import time; time.sleep(60)'])\n"
        "    open(%r, 'w').write(str(os.getpid()) + ' ' + str(p.pid)); time.sleep(60)\n"
        "print(json.dumps({'texte': 'x', 'cout_usd': 0.1}))\n")

    def test_sigterm_pendant_le_controle_de_la_course(self):
        """CL40-02 (S3) : SIGTERM pendant le contrôle d'Argon dans la course → code 2, tentative scellée au plafond de la
        session de contrôle (2,5 chez Argon), message vrai, commande et petit-enfant arrêtés."""
        import signal
        import subprocess
        prep = self.cours().preparer()
        pid_f = os.path.join(self.tmp, "ctrl.pid")
        lent = self.script(self.SCRIPT_LENT_CONTROLE % pid_f, "lent-ctrl.py")
        sortie = os.path.join(self.tmp, "l-sig-ctrl")
        chemin = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "demonstrations", "ideation_v1.py")
        p = subprocess.Popen([sys.executable, "-I", "-B", chemin] + self.base(sortie, prep) + ["--commande-externe", lent],
                             env=self.env_propre(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        self._attendre_pids(pid_f, p)
        p.send_signal(signal.SIGTERM)
        _, err = p.communicate(timeout=30)
        err = err.decode("utf-8", "replace")
        self.assertEqual(p.returncode, 2, err)
        self.assertIn("contrôle compris", err)
        with open(os.path.join(sortie + "-controle", "tentative-1.json")) as f:
            r = json.load(f)["reglages"]
        self.assertTrue(idn.verifier_scelle(os.path.join(sortie + "-controle", "tentative-1.json")))
        self.assertAlmostEqual(r["cout_externe_usd"], 2.5)  # v40 : 0,0
        self.assertEqual(r["lectures"]["externe:argon"]["statut"], "interrompue")
        self.assertIn("tentative_scellee", err)
        self._morts([int(x) for x in _lire(pid_f).split()])

    def test_sigterm_pendant_le_controle_du_bras(self):
        """CL40-02 (S3b) : SIGTERM pendant le contrôle du bras → code 2, bras-tentative scellée au plafond du contrôle
        (0,2), `relancable` calculé, commande et petit-enfant arrêtés."""
        import signal
        import subprocess
        prep = self.cours().preparer()
        sortie = os.path.join(self.tmp, "l-bras-sig")
        code, out, err = self.principal(self.lanceur(), self.base(sortie, prep) + ["--commande-externe",
                                                                                   " ".join(self.cmd().commande(self.cmd().SCRIPT_OK))])
        self.assertEqual(code, 0, out + err)
        att = self.cmd().attester(os.path.join(self.tmp, "att-bras-sig.json"), sortie, "argon-j")
        pid_f = os.path.join(self.tmp, "bras.pid")
        lent = self.script(self.SCRIPT_LENT_CONTROLE % pid_f, "lent-bras.py")
        chemin = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "demonstrations", "ideation_v1.py")
        p = subprocess.Popen([sys.executable, "-I", "-B", chemin, sortie, "--bras-rapporte-differe", "--attestation-lecture-humaine",
                              att, "--juge-externe", "argon-j=gemini-argon", "--commande-externe", lent],
                             env=self.env_propre(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        self._attendre_pids(pid_f, p)
        p.send_signal(signal.SIGTERM)
        _, err = p.communicate(timeout=30)
        err = err.decode("utf-8", "replace")
        self.assertEqual(p.returncode, 2, err)
        self.assertIn("interruption", err)
        chemin_t = os.path.join(sortie, "bras-tentative-1.json")
        self.assertTrue(idn.verifier_scelle(chemin_t))
        with open(chemin_t) as f:
            r = json.load(f)["reglages"]
        self.assertAlmostEqual(r["journal"]["cout_total_usd"], 0.2)  # v40 : 0,0
        self.assertTrue(r["relancable"])  # 11,6 ≥ course + 0,2 + 3,5 + 0,2 : relance calculée possible
        self.assertFalse(os.path.exists(os.path.join(sortie, "manifeste-bras-rapporte.json")))
        self._morts([int(x) for x in _lire(pid_f).split()])

    # --- CL40-03 ---------------------------------------------------------------------------------------------------------

    def test_s9_meme_controle_du_bras_et_refus_du_coeur_scelle(self):
        """CL40-03 (S9) : `--budget-controle-usd 0.1 --budget-externe-usd 11.1`, Argon au pire cas, seconde passe : le
        lanceur et le cœur comptent le même contrôle du bras (0,1) → la course part. Un refus du cœur après des contrôles
        payés (contrôle Claude rendu « ok » au-dessus de son plafond) écrit une tentative scellée avec les coûts, relance
        calculée impossible et refusée avant tout contrôle."""
        prep, att = self.prep_devis()
        argon = self.script(self.SCRIPT_PLAFOND, "argon-plafond.py")
        sortie = os.path.join(self.tmp, "l-s9")
        code, out, err = self.principal(self.lanceur(), self.base(sortie, prep, att, "--commande-externe", argon,
                                                                   "--budget-controle-usd", "0.1", "--budget-externe-usd", "11.1"))
        self.assertIn(code, (0, 4), err)  # v40 : 2, « somme des plafonds externes 11.20 > total externe 11.1 »
        with open(os.path.join(sortie, "manifeste-depart.json")) as f:
            sommes = json.load(f)["reglages"]["somme_des_plafonds"]
        self.assertAlmostEqual(sommes["budget_controle_bras_usd"], 0.1)
        self.assertAlmostEqual(sommes["externe_avec_controle_du_bras"], 11.1)  # 2,5 + 2 × 2,5 + 3,5 + 0,1
        self.assertFalse(os.path.exists(os.path.join(sortie + "-controle", "tentative-1.json")))
        # le bras, lancé sans répéter l'option, joue le contrôle que la course a compté (0,1) : Argon 7,5 + 0,1 + 3,5 = 11,1
        att_b = self.cmd().attester(os.path.join(self.tmp, "att-s9.json"), sortie, "argon-j")
        code, out, err = self.principal(self.lanceur(), [sortie, "--bras-rapporte-differe", "--attestation-lecture-humaine", att_b,
                                                         "--juge-externe", "argon-j=gemini-argon", "--commande-externe", argon])
        self.assertIn(code, (0, 4), err)  # avant : refus « 7,5 + 3,7 > 11,1 » (contrôle du bras repris à 0,2)
        with open(os.path.join(sortie, "manifeste-bras-rapporte.json")) as f:
            jb = json.load(f)["reglages"]["journal"]
        self.assertAlmostEqual(jb["controle"]["argon-j"]["cout_compte_usd"], 0.1)
        self.assertAlmostEqual(jb["cout_externe_deja_compte_course_usd"] + jb["cout_total_usd"], 11.1)
        # refus du cœur après les contrôles payés (SUPPOSÉ : un contrôle « ok » au-dessus de son plafond, 0,5 > 0,2)
        sortie2 = os.path.join(self.tmp, "l-coeur")
        args2 = self.base(sortie2, prep, att, "--commande-externe", argon)
        code, out, err = self.principal(self.lanceur(cout_controle_claude=0.5), args2)
        self.assertEqual(code, 2)
        self.assertIn("somme des plafonds Claude", err)
        self.assertFalse(os.path.exists(sortie2))
        chemin_t = os.path.join(sortie2 + "-controle", "tentative-1.json")
        self.assertTrue(idn.verifier_scelle(chemin_t))  # v40 : aucune trace
        with open(chemin_t) as f:
            r = json.load(f)["reglages"]
        self.assertAlmostEqual(r["cout_claude_usd"], 1.0)
        self.assertAlmostEqual(r["cout_externe_usd"], 2.5)
        self.assertFalse(r["relancable"])
        code, out, err = self.principal(self.lanceur(cout_controle_claude=0.5), args2)  # relance : refus avant tout contrôle
        self.assertEqual(code, 2)
        self.assertFalse(os.path.exists(os.path.join(sortie2 + "-controle", "tentative-2.json")))
        self.assertFalse(os.path.exists(os.path.join(sortie2 + "-controle", "tentative-2")))

    # --- CL40-04 ---------------------------------------------------------------------------------------------------------

    def test_controle_a_la_taille_reelle_de_la_passe_2_et_ordre_d_argon(self):
        """CL40-04 (S5) : le contrôle d'Argon porte sa consigne de passe 2 au maximum (fiches à la taille maximale champ par
        champ × nombre, matériau) ; une passe 2 réelle à champs de 3 000 caractères n'est pas plus grosse que le contrôle ;
        sans matériau la seconde passe compte aussi ses fiches ; Argon joue sa passe 2 juste après sa passe 1, avant toute
        passe Claude."""
        c = self.cours()
        prep = c.preparer()
        c._prep = prep
        att = os.path.join(self.tmp, "att-m.json")
        idn.ecrire_json_scelle(att, {"lecteur": "Lazar", "lu_le": "2026-10-29", "materiau_sha256": {
            os.path.basename(prep["materiau"][0]): idn.sha256_fichier(prep["materiau"][0])}})
        budgets = dict(c.budgets())
        budgets[("proposeur_ideation", "gemini-argon")] = 1.0
        args = dict(liste_blanche=prep["liste_blanche"], question=prep["question"], pieces=prep["pieces"], temoins=prep["temoins"],
                    budgets=budgets, proposeurs=[("opus", "claude-opus-5-5"), ("fable", "claude-fable-5-1")],
                    juges=[("juge-fable", "claude-fable-5-1"), ("juge-opus", "claude-opus-5-5")],
                    proposeurs_externes=[("argon", "gemini-argon")], budget_total_usd=20.0, budget_externe_usd=5.0,
                    nombre_par_proposeur=8)
        taille_fiche = len(json.dumps([idn.fiche_maximale()], ensure_ascii=False, indent=1))
        self.assertGreater(taille_fiche, 13 * idn.LONGUEUR_MAX_CHAMP)
        v2 = idn.verifier_reglages(materiau=prep["materiau"], seconde_passe=True, attestation_materiau=att, **args)
        self.assertGreater(len(v2["texte_controle_externe"]), 8 * taille_fiche)  # v40 : 8 × 4 000
        self.assertIn("Tour interne", v2["texte_controle_externe"])
        v2b = idn.verifier_reglages(seconde_passe=True, **args)  # sans matériau : les fiches de passe 1 comptent
        self.assertGreater(len(v2b["texte_controle_externe"]), 8 * taille_fiche)
        v1 = idn.verifier_reglages(**args)
        self.assertLess(len(v1["texte_controle_externe"]), taille_fiche)
        # une passe 2 réelle aux champs de 3 000 caractères (8 fiches) n'est pas plus grosse que la consigne de contrôle
        controle = idn.consigne_de_controle(v2["texte_controle_externe"])
        grosse = fiche_brute(nom="Argon gros")
        for k in ("enonce", "perte_traduction", "piege", "cosmetique_si"):
            grosse[k] = "y" * idn.LONGUEUR_MAX_CHAMP
        ordre = []

        class Argon:
            nom = "argon-simule"

            def lancer(self, role, consigne, dossier, budget_usd, max_tours, modele=None):
                ordre.append(("argon", os.path.basename(dossier), len(consigne)))
                fiches = [dict(grosse, nom=f"Argon {i}") for i in range(8)]
                return Resultat("```json\n" + json.dumps({"fiches": fiches}, ensure_ascii=False) + "\n```", [], 0.1, "ok")
        ad = FauxAdaptateur({"opus": [fiche_brute(nom="O1")], "fable": [fiche_brute(nom="F1")]},
                            notes_par_juge={"juge-fable": c.notes_temoins_ok, "juge-opus": c.notes_temoins_ok})
        orig = ad.lancer

        def lancer_note(role, consigne, dossier, budget_usd, max_tours, modele=None):
            if role == "proposeur_ideation":
                ordre.append(("claude", os.path.basename(dossier), len(consigne)))
            return orig(role, consigne, dossier, budget_usd, max_tours, modele)
        ad.lancer = lancer_note
        res = c.lancer(ad, "c-ordre", budgets=budgets, proposeurs_externes=[("argon", "gemini-argon", Argon())],
                       budget_externe_usd=5.0, seconde_passe=True, attestation_materiau=att)
        self.assertEqual([(q, d) for q, d, _ in ordre][:2], [("argon", "passe-1"), ("argon", "passe-2")])  # v40 : Claude avant
        self.assertEqual([(q, d) for q, d, _ in ordre][2:], [("claude", "passe-1")] * 2 + [("claude", "passe-2")] * 2)
        self.assertLessEqual(ordre[1][2], len(controle))  # la passe 2 réelle tient dans la taille éprouvée
        # ordre des fiches écrites inchangé : passe 1 (Argon, opus, fable) puis passe 2
        self.assertEqual([f["passe"] for f in res["fiches"]], [1] * 10 + [2] * 10)
        self.assertEqual(res["fiches"][0]["auteur"], "argon")

    def test_controle_du_bras_porte_la_consigne_du_juge(self):
        """CL40-04 (S6) : le contrôle du bras envoie la consigne réelle du juge (pièces de juge et fiches comprises), pas
        41 caractères."""
        c = self.cours()
        ad = FauxAdaptateur({"opus": [fiche_brute(nom="O1")], "fable": [fiche_brute(nom="F1")]},
                            notes_par_juge={"juge-fable": c.notes_temoins_ok, "juge-opus": c.notes_temoins_ok})
        budgets = dict(c.budgets())
        budgets[("juge_ideation", "autre-lignee-x")] = 1.0
        c.lancer(ad, "cb", budgets=budgets, juges_externes=[("argon", "autre-lignee-x")], budget_externe_usd=2.0)
        sortie = os.path.join(self.tmp, "cb")
        att = self.cmd().attester(os.path.join(self.tmp, "att-cb.json"), sortie)
        with open(os.path.join(sortie, "juges-bras-rapporte", "traces-argon", "consigne-en-attente.md"), encoding="utf-8") as f:
            consigne_juge = f.read()
        recu = []

        class Enregistre:
            nom = "commande-externe"

            def lancer(self, role, consigne, dossier, budget_usd, max_tours, modele=None):
                recu.append(consigne)
                if consigne.startswith(idn.APPEL_DE_CONTROLE_CONSIGNE):
                    return Resultat("OK", [], 0.01, "ok")
                return Resultat("```json\n" + json.dumps(c.notes_temoins_ok(
                    sorted(set(re.findall(r'"identifiant": "(T\d\d)"', consigne))), consigne)) + "\n```", [], 0.3, "ok")

            def description(self):
                return {"commande": ["enregistre"]}
        apres = idn.executer_bras_differe(sortie, attestation_lecture_humaine=att, budgets=budgets,
                                          juges_externes=[("argon", "autre-lignee-x", Enregistre())])
        self.assertTrue(recu[0].startswith(idn.APPEL_DE_CONTROLE_CONSIGNE))
        self.assertIn(consigne_juge, recu[0])  # v40 : 41 caractères
        self.assertGreater(apres["journal"]["controle"]["argon"]["taille_consigne"], len(consigne_juge))
        self.assertEqual(recu[1], consigne_juge)
        self.assertFalse(apres["sans_bras"])

    # --- CL40-01 (code) : relance calculée, contrôle Claude payé ; tolérances ------------------------------------------

    SCRIPT_KO = "import sys, json\nc = sys.stdin.read()\nopen(%r, 'a').write('appel\\n')\nprint(json.dumps({'texte': 'KO', 'cout_usd': 0.15}))\n"

    def test_relancable_calcule_avec_un_controle_claude_paye(self):
        """CL40-01 (code), point 6 : contrôle Claude payé (0,01 puis 0,2 par modèle), Argon « KO » à 0,15, réglages du devis
        v7 quinquies (somme Claude 40,0 exactement) : la tentative scellée porte les coûts, `relancable` est faux (somme de
        la relance 40,02 > 40), le lanceur l'imprime, et la relance est refusée avant tout contrôle. Total relevé à 41 :
        relançable, et la relance repasse bien par les contrôles."""
        prep, att = self.prep_devis()
        for cout, somme in ((0.01, "40.0200"), (0.2, "40.4000")):
            journal = os.path.join(self.tmp, f"ko-{cout}.log")
            ko = self.script(self.SCRIPT_KO % journal, f"ko-{cout}.py")
            sortie = os.path.join(self.tmp, f"l-paye-{cout}")
            argv = self.base(sortie, prep, att, "--commande-externe", ko)
            code, out, err = self.principal(self.lanceur(cout_controle_claude=cout), argv)
            self.assertEqual(code, 2)
            chemin = os.path.join(sortie + "-controle", "tentative-1.json")
            self.assertTrue(idn.verifier_scelle(chemin))
            with open(chemin) as f:
                r = json.load(f)["reglages"]
            self.assertAlmostEqual(r["cout_claude_usd"], 2 * cout)
            self.assertAlmostEqual(r["cout_externe_usd"], 0.15)
            self.assertFalse(r["relancable"], r)  # v40 : vrai
            self.assertTrue(any(somme in m for m in r["motifs_relance"]), r["motifs_relance"])
            self.assertIn('"relancable": false', err)
            self.assertNotIn("trois tentatives", err)
            n = len(_lire(journal).splitlines())
            code, out, err = self.principal(self.lanceur(cout_controle_claude=cout), argv)
            self.assertEqual(code, 2)
            self.assertIn("somme des plafonds Claude", err)
            self.assertEqual(len(_lire(journal).splitlines()), n)  # aucun contrôle rejoué, Argon non rappelé
            self.assertFalse(os.path.exists(os.path.join(sortie + "-controle", "tentative-2.json")))
        # total relevé à 41 : relance calculée possible, et elle repasse par les contrôles (bornée à trois)
        journal = os.path.join(self.tmp, "ko-41.log")
        ko = self.script(self.SCRIPT_KO % journal, "ko-41.py")
        sortie = os.path.join(self.tmp, "l-paye-41")
        argv = self.base(sortie, prep, att, "--commande-externe", ko, "--budget-total-usd", "41", "--budget-externe-usd", "12")
        for n in (1, 2, 3):  # sommes de la relance : 40,4 puis 40,8 (≤ 41) ; la troisième atteint la borne
            code, _, err = self.principal(self.lanceur(cout_controle_claude=0.2), argv)
            self.assertEqual(code, 2)
            with open(os.path.join(sortie + "-controle", f"tentative-{n}.json")) as f:
                r = json.load(f)["reglages"]
            self.assertEqual(r["relancable"], n < 3, r["motifs_relance"])
        self.assertIn("3 tentatives faites", r["motifs_relance"][0])
        code, _, err = self.principal(self.lanceur(cout_controle_claude=0.2), argv)
        self.assertEqual(code, 2)
        self.assertIn("tentatives", err)
        self.assertEqual(len(_lire(journal).splitlines()), 3)

    def test_tolerances_separees(self):
        """CL40-01 (code), point 5 : la tolérance Claude ne désarme pas la somme externe, et inversement ; l'ancienne option
        vaut les deux et est consignée au manifeste."""
        c = self.cours()
        prep = c.preparer()
        c._prep = prep
        budgets = dict(c.budgets())
        budgets[("proposeur_ideation", "gemini-argon")] = 1.0
        budgets[("juge_ideation", "autre-lignee-x")] = 1.0
        base = dict(liste_blanche=prep["liste_blanche"], question=prep["question"], pieces=prep["pieces"], temoins=prep["temoins"],
                    budgets=budgets, proposeurs=[("opus", "claude-opus-5-5"), ("fable", "claude-fable-5-1")],
                    juges=[("juge-fable", "claude-fable-5-1"), ("juge-opus", "claude-opus-5-5")],
                    proposeurs_externes=[("argon", "gemini-argon")], juges_externes=[("argon-j", "autre-lignee-x")])
        # Claude au-dessus (4 > 3), externe au-dessus (2,2 > 2,0)
        idn.verifier_reglages(budget_total_usd=3.0, budget_externe_usd=2.2, tolerer_somme_claude=True, **base)
        with self.assertRaises(idn.CourseInterrompue) as cm:
            idn.verifier_reglages(budget_total_usd=4.0, budget_externe_usd=2.0, tolerer_somme_claude=True, **base)
        self.assertIn("externes", str(cm.exception))
        idn.verifier_reglages(budget_total_usd=4.0, budget_externe_usd=2.0, tolerer_somme_externe=True, **base)
        with self.assertRaises(idn.CourseInterrompue) as cm:
            idn.verifier_reglages(budget_total_usd=3.0, budget_externe_usd=2.2, tolerer_somme_externe=True, **base)
        self.assertIn("Claude", str(cm.exception))
        idn.verifier_reglages(budget_total_usd=3.0, budget_externe_usd=2.0, tolerer_somme_plafonds=True, **base)
        # au cœur
        ad = FauxAdaptateur({"opus": [fiche_brute(nom="O1")], "fable": [fiche_brute(nom="F1")]})
        ext = dict(budgets=budgets, juges_externes=[("argon-j", "autre-lignee-x")])
        with self.assertRaises(idn.CourseInterrompue) as cm:
            c.lancer(ad, "t-c", budget_total_usd=3.0, budget_externe_usd=1.0, tolerer_somme_claude=True, **ext)
        self.assertIn("externes", str(cm.exception))
        self.assertEqual(ad.appels, [])
        # lanceur : options séparées, ancienne option consignée
        lanceur = self.lanceur()
        sortie = os.path.join(self.tmp, "l-tol")
        argv = self.base(sortie, prep, None, "--budget-externe-usd", "11.6", "--tolerer-somme-plafonds")
        code, out, err = self.principal(lanceur, argv)
        self.assertEqual(code, 0, err)
        with open(os.path.join(sortie, "manifeste-depart.json")) as f:
            d = json.load(f)["reglages"]
        self.assertEqual(d["versions"]["tolerances"], {"claude": True, "externe": True, "option_ancienne_les_deux": True})
        self.assertTrue(d["somme_des_plafonds"]["toleree_claude"] and d["somme_des_plafonds"]["toleree_externe"])
        a = lanceur.construire_analyseur()
        ns = a.parse_args(["s", "--tolerer-somme-plafonds-externe"])
        self.assertEqual(idn.tolerances(ns.tolerer_somme_plafonds, ns.tolerer_somme_plafonds_claude,
                                        ns.tolerer_somme_plafonds_externe), (False, True))

    # --- CL40-05 ---------------------------------------------------------------------------------------------------------

    def test_chemin_de_l_argent_valeurs_non_finies(self):
        """CL40-05 : `budget_controle_bras_usd` (réglages, cœur, bras), champs du relais, coûts et sceaux des tentatives :
        NaN, ±∞, négatif, booléen refusés ; cas sains acceptés."""
        c = self.cours()
        prep = c.preparer()
        c._prep = prep
        budgets = dict(c.budgets())
        budgets[("juge_ideation", "autre-lignee-x")] = 1.0
        base = dict(liste_blanche=prep["liste_blanche"], question=prep["question"], pieces=prep["pieces"], temoins=prep["temoins"],
                    budgets=budgets, proposeurs=[("opus", "claude-opus-5-5"), ("fable", "claude-fable-5-1")],
                    juges=[("juge-fable", "claude-fable-5-1"), ("juge-opus", "claude-opus-5-5")],
                    juges_externes=[("argon-j", "autre-lignee-x")], budget_total_usd=4.0, budget_externe_usd=1.2)
        for x in (float("nan"), -float("inf"), -5.0, True):  # v40 : −5,0 faisait passer 1,2 de plafonds sous un total de 6,0
            with self.subTest(budget_controle_bras_usd=x), self.assertRaises(idn.CourseInterrompue):
                idn.verifier_reglages(budget_controle_bras_usd=x, **base)
            with self.subTest(coeur=x), self.assertRaises(idn.CourseInterrompue):
                c.lancer(FauxAdaptateur({}), f"nf-{x}", budgets=budgets, juges_externes=[("argon-j", "autre-lignee-x")],
                         budget_externe_usd=1.2, budget_controle_bras_usd=x)
        idn.verifier_reglages(budget_controle_bras_usd=0.2, **base)  # sain
        idn.verifier_reglages(budget_controle_bras_usd=0, **dict(base, budget_externe_usd=1.0))  # sain : nul permis
        # relais
        lanceur = self.lanceur()
        juges = [("a", "claude-opus-5-5"), ("b", "claude-fable-5-1")]
        bj = {("juge_ideation", "claude-opus-5-5"): 4.0, ("juge_ideation", "claude-fable-5-1"): 7.0}
        sain = {"plafond_usd": 44, "reserve_par_appel_usd": 4, "depense_usd": 0.0}
        lanceur.verifier_relais(sain, 40.0, bj, juges)
        for champ, mauvais in (("depense_usd", (float("nan"), -float("inf"), True, -1.0)),
                               ("plafond_usd", (float("nan"), float("inf"), True)),
                               ("reserve_par_appel_usd", (float("nan"), -float("inf"), True))):
            for x in mauvais:
                with self.subTest(champ=champ, valeur=x), self.assertRaises(idn.CourseInterrompue):
                    lanceur.verifier_relais(dict(sain, **{champ: x}), 40.0, bj, juges)
        lanceur.verifier_relais({}, 40.0, bj, juges)  # relais muet : inchangé
        # tentatives de contrôle : sceau, coûts, numérotation, dossier sans tentative
        d = os.path.join(self.tmp, "s-controle")
        os.makedirs(d)
        r = {"reglages": {"cout_claude_usd": 0.4, "cout_externe_usd": 0.15}}
        idn.ecrire_json_scelle(os.path.join(d, "tentative-1.json"), r)
        self.assertEqual(len(lanceur.lire_tentatives_controle(d)), 1)  # sain
        with open(os.path.join(d, "tentative-2.json"), "w") as f:  # sans sceau
            json.dump(r, f)
        with self.assertRaises(idn.CourseInterrompue):
            lanceur.lire_tentatives_controle(d)
        os.remove(os.path.join(d, "tentative-2.json"))
        idn.ecrire_scelle(os.path.join(d, "tentative-2.json"), '{"reglages": {"cout_claude_usd": NaN, "cout_externe_usd": 0}}')
        with self.assertRaises(idn.CourseInterrompue):
            lanceur.lire_tentatives_controle(d)
        for nom in ("tentative-2.json", "tentative-2.json.sha256"):
            os.remove(os.path.join(d, nom))
        idn.ecrire_json_scelle(os.path.join(d, "tentative-2.json"), {"reglages": {"cout_claude_usd": -2.5, "cout_externe_usd": 0}})
        with self.assertRaises(idn.CourseInterrompue):
            lanceur.lire_tentatives_controle(d)
        for nom in ("tentative-2.json", "tentative-2.json.sha256"):
            os.remove(os.path.join(d, nom))
        with open(os.path.join(d, "tentative-1.json"), "a") as f:  # sceau faux
            f.write(" ")
        with self.assertRaises(idn.CourseInterrompue):
            lanceur.lire_tentatives_controle(d)
        d2 = os.path.join(self.tmp, "s2-controle")
        os.makedirs(os.path.join(d2, "tentative-1"))  # dossier de contrôle sans tentative scellée (arrêt brutal, ou retrait)
        with self.assertRaises(idn.CourseInterrompue):
            lanceur.lire_tentatives_controle(d2)
        idn.ecrire_json_scelle(os.path.join(d2, "tentative-2.json"), r)  # numérotation trouée
        with self.assertRaises(idn.CourseInterrompue):
            lanceur.lire_tentatives_controle(d2)
        # bras : tentative payée au sceau absent → refus ; budget du contrôle non fini → refus
        ad = FauxAdaptateur({"opus": [fiche_brute(nom="O1")], "fable": [fiche_brute(nom="F1")]},
                            notes_par_juge={"juge-fable": c.notes_temoins_ok, "juge-opus": c.notes_temoins_ok})
        c.lancer(ad, "nf-bras", budgets=budgets, juges_externes=[("argon", "autre-lignee-x")], budget_externe_usd=2.0)
        sortie = os.path.join(self.tmp, "nf-bras")
        att = self.cmd().attester(os.path.join(self.tmp, "att-nf.json"), sortie)
        bon = Enregistreur(c)
        with self.assertRaises(idn.CourseInterrompue):
            idn.executer_bras_differe(sortie, attestation_lecture_humaine=att, budgets=budgets, budget_controle_usd=float("nan"),
                                      juges_externes=[("argon", "autre-lignee-x", bon)])
        with open(os.path.join(sortie, "bras-tentative-1.json"), "w") as f:
            json.dump({"reglages": {"journal": {"cout_total_usd": 0.15}}}, f)
        with self.assertRaises(idn.CourseInterrompue) as cm:
            idn.executer_bras_differe(sortie, attestation_lecture_humaine=att, budgets=budgets,
                                      juges_externes=[("argon", "autre-lignee-x", bon)])
        self.assertIn("sceau", str(cm.exception))
        self.assertEqual(bon.recu, [])

    # --- CL40-08, CL40-07 (M07) ------------------------------------------------------------------------------------------

    def test_bras_interrompu_apres_envoi_ecrit_le_classement_sans_bras(self):
        """CL40-08 (S8) : interruption pendant la session du juge d'Argon (consigne envoyée) → manifeste, plafond compté,
        `classement-sans-bras.json` à deux juges marqué « sans juge externe », l'interruption remonte, bras verrouillé."""
        c = self.cours()
        ad = FauxAdaptateur({"opus": [fiche_brute(nom="O1")], "fable": [fiche_brute(nom="F1")]},
                            notes_par_juge={"juge-fable": c.notes_temoins_ok, "juge-opus": c.notes_temoins_ok})
        budgets = dict(c.budgets())
        budgets[("juge_ideation", "autre-lignee-x")] = 1.0
        c.lancer(ad, "ck", budgets=budgets, juges_externes=[("argon", "autre-lignee-x")], budget_externe_usd=2.0)
        sortie = os.path.join(self.tmp, "ck")
        att = self.cmd().attester(os.path.join(self.tmp, "att-ck.json"), sortie)
        coupe = Enregistreur(c, interrompre_juge=True)
        with self.assertRaises(KeyboardInterrupt):
            idn.executer_bras_differe(sortie, attestation_lecture_humaine=att, budgets=budgets,
                                      juges_externes=[("argon", "autre-lignee-x", coupe)])
        chemin = os.path.join(sortie, "classement-sans-bras.json")
        self.assertTrue(idn.verifier_scelle(chemin))  # v40 : absent
        with open(chemin) as f:
            cl = json.load(f)
        self.assertFalse(cl["lisible_L2_L4"])
        self.assertIn("interrompu après envoi", cl["sans_juge_externe"])
        self.assertTrue(all(l["nombre_juges"] == 2 for l in cl["lignes"]))
        with open(os.path.join(sortie, "manifeste-bras-rapporte.json")) as f:
            j = json.load(f)["reglages"]["journal"]
        self.assertAlmostEqual(j["cout_total_usd"], 0.01 + 1.0)
        with self.assertRaises(idn.CourseInterrompue):  # verrouillé
            idn.executer_bras_differe(sortie, attestation_lecture_humaine=att, budgets=budgets,
                                      juges_externes=[("argon", "autre-lignee-x", Enregistreur(c))])

    def test_m07_controle_du_bras_a_cout_nul_processus_parti(self):
        """CL40-07 (M07) : un contrôle du bras où un processus est parti mais rien n'est compté (exception avec un plafond
        de contrôle nul ; ou « KO » à coût 0 d'un adaptateur fictif) est une **tentative payée** (bornée), jamais « non
        joué » ; seule une commande non lancée ou une clé dans l'environnement donnent « non joué »."""
        c = self.cours()
        ad = FauxAdaptateur({"opus": [fiche_brute(nom="O1")], "fable": [fiche_brute(nom="F1")]},
                            notes_par_juge={"juge-fable": c.notes_temoins_ok, "juge-opus": c.notes_temoins_ok})
        budgets = dict(c.budgets())
        budgets[("juge_ideation", "autre-lignee-x")] = 1.0
        for nom, adapt, plafond in (("m7a", Enregistreur(c, panne_controle=True), 0.0),
                                    ("m7b", Enregistreur(c, ko_gratuit=True), 0.2)):
            c.lancer(ad, nom, budgets=budgets, juges_externes=[("argon", "autre-lignee-x")], budget_externe_usd=2.0)
            sortie = os.path.join(self.tmp, nom)
            att = self.cmd().attester(os.path.join(self.tmp, f"att-{nom}.json"), sortie)
            with self.assertRaises(idn.CourseInterrompue) as cm:
                idn.executer_bras_differe(sortie, attestation_lecture_humaine=att, budgets=budgets, budget_controle_usd=plafond,
                                          exiger_cout_controle=False, juges_externes=[("argon", "autre-lignee-x", adapt)])
            self.assertNotIn("non joué", str(cm.exception), nom)
            self.assertTrue(os.path.exists(os.path.join(sortie, "bras-tentative-1.json")), nom)
            self.assertFalse(os.path.exists(os.path.join(sortie, "manifeste-bras-non-joue-1.json")), nom)

    def test_bras_tentative_relancable_calcule(self):
        """Point 4 (bras) : `relancable` d'une tentative payée du bras est calculé sur le plafond externe de la relance
        (coût de la tentative imputé), pas promis par le seul compte : 0,15 + 0,2 + 1,0 > 1,3 → faux dès la première."""
        c = self.cours()
        ad = FauxAdaptateur({"opus": [fiche_brute(nom="O1")], "fable": [fiche_brute(nom="F1")]},
                            notes_par_juge={"juge-fable": c.notes_temoins_ok, "juge-opus": c.notes_temoins_ok})
        budgets = dict(c.budgets())
        budgets[("juge_ideation", "autre-lignee-x")] = 1.0
        for nom, total, attendu in (("rb1", 1.3, False), ("rb2", 2.0, True)):
            c.lancer(ad, nom, budgets=budgets, juges_externes=[("argon", "autre-lignee-x")], budget_externe_usd=total)
            sortie = os.path.join(self.tmp, nom)
            att = self.cmd().attester(os.path.join(self.tmp, f"att-{nom}.json"), sortie)
            from pole.adaptateurs import AdaptateurCommandeExterne
            ko = AdaptateurCommandeExterne(self.cmd().commande(
                "import sys, json\nsys.stdin.read()\nprint(json.dumps({'texte': 'KO', 'cout_usd': 0.15}))\n", f"ko-{nom}.py"),
                environnement={})
            with self.assertRaises(idn.CourseInterrompue) as cm:
                idn.executer_bras_differe(sortie, attestation_lecture_humaine=att, budgets=budgets,
                                          juges_externes=[("argon", "autre-lignee-x", ko)])
            with open(os.path.join(sortie, "bras-tentative-1.json")) as f:
                r = json.load(f)["reglages"]
            self.assertEqual(r["relancable"], attendu, nom)  # v40 : vrai dans les deux cas
            self.assertIn("relance permise" if attendu else "plus de relance", str(cm.exception))

    # --- CL40-09 ---------------------------------------------------------------------------------------------------------

    def test_ecrits_du_lanceur(self):
        """CL40-09 : le devis en vigueur (v7 quinquies) nommé partout ; message d'interruption vrai pour les contrôles ;
        plus de promesse « trois tentatives » sans calcul."""
        chemin = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "demonstrations", "ideation_v1.py")
        with open(chemin, encoding="utf-8") as f:
            texte = f.read()
        for ancien in ("v7 bis", "v7 ter", "v7 quater", "relance permise\", qui", "bornée à trois)"):
            self.assertNotIn(ancien, texte)
        self.assertIn("devis v7 quinquies", texte)
        self.assertIn("contrôle compris", texte)


class Enregistreur:
    """Juge externe d'essai (v41) : enregistre ce qu'il reçoit ; contrôle « OK » à 0,01 ; options : panne au contrôle,
    « KO » gratuit au contrôle, interruption pendant la session du juge."""
    nom = "commande-externe"

    def __init__(self, cours, panne_controle=False, ko_gratuit=False, interrompre_juge=False):
        self.cours, self.recu = cours, []
        self.panne_controle, self.ko_gratuit, self.interrompre_juge = panne_controle, ko_gratuit, interrompre_juge

    def lancer(self, role, consigne, dossier, budget_usd, max_tours, modele=None):
        self.recu.append(consigne)
        if consigne.startswith(idn.APPEL_DE_CONTROLE_CONSIGNE):
            if self.panne_controle:
                raise RuntimeError("panne pendant le contrôle")
            return Resultat("KO" if self.ko_gratuit else "OK", [], 0.0 if self.ko_gratuit else 0.01, "ok")
        if self.interrompre_juge:
            raise KeyboardInterrupt("signal 15")
        idents = sorted(set(re.findall(r'"identifiant": "(T\d\d)"', consigne)))
        return Resultat("```json\n" + json.dumps(self.cours.notes_temoins_ok(idents, consigne)) + "\n```", [], 0.3, "ok")

    def description(self):
        return {"commande": ["enregistreur"]}


class TestReglagesV35(CasAvecDossier):
    def test_options_tools_vides_et_effort(self):
        """CL34-02 / CL34-08 : `tools=[]` (jeu disponible) pour les rôles de l'idéation, effort fixé ; les autres rôles
        gardent le jeu par défaut du kit (None)."""
        dossier = os.path.join(self.tmp, "course", "juges", "j")
        os.makedirs(dossier)
        o = construire_options(dossier, 1.0, 2, url_relais="http://127.0.0.1:8787", modele="claude-opus-5-5",
                               role="juge_ideation", interdire_lecture=[os.path.join(self.tmp, "course")])
        self.assertEqual((o["tools"], o["allowed_tools"], o["effort"]), ([], [], "medium"))
        o = construire_options(dossier, 1.0, 2, url_relais="http://127.0.0.1:8787", modele="claude-opus-5-5",
                               role="experimentateur", interdire_lecture=[os.path.join(self.tmp, "course")])
        self.assertIsNone(o["tools"])
        self.assertIsNone(o["effort"])

    def test_ligne_de_commande_du_kit_sans_outil(self):
        """CL34-02 : la ligne de commande construite par le kit porte `--tools ''` (jamais exécutée)."""
        try:
            import claude_agent_sdk as sdk
            from claude_agent_sdk._internal.transport.subprocess_cli import SubprocessCLITransport
        except ImportError:
            self.skipTest("kit d'agent absent")
        from pole.adaptateurs import AdaptateurClaudeSDK
        dossier = os.path.join(self.tmp, "course", "juges", "j")
        os.makedirs(dossier)
        o = construire_options(dossier, 1.0, 2, url_relais="http://127.0.0.1:8787", modele="claude-opus-5-5",
                               role="juge_ideation", interdire_lecture=[os.path.join(self.tmp, "course")])
        options = AdaptateurClaudeSDK.options_sdk(sdk, o)
        options.cli_path = "/bin/true"
        cmd = SubprocessCLITransport("x", options)._build_command()
        self.assertIn("--tools", cmd)
        self.assertEqual(cmd[cmd.index("--tools") + 1], "")
        self.assertNotIn("--allowedTools", cmd)
        self.assertEqual(cmd[cmd.index("--effort") + 1], "medium")
        for nom in [n for n in sys.modules if n.startswith("claude_agent_sdk")]:  # CL39-12 : ne pas laisser le kit chargé
            del sys.modules[nom]

    def test_borne_de_temps_par_session(self):
        """CL34-05 : une session qui pend au-delà du délai rend « erreur » avec un motif, sans lever."""
        import asyncio
        from pole.adaptateurs import AdaptateurClaudeSDK

        class FauxSDK:
            class ClaudeSDKError(Exception):
                pass

            class AssistantMessage:
                pass

            class ResultMessage:
                pass

            class TextBlock:
                pass

            @staticmethod
            async def query(prompt, options):
                await asyncio.sleep(5)
                yield None
        texte, cout, statut, erreur = asyncio.run(AdaptateurClaudeSDK._executer(FauxSDK, "x", None, delai_s=0.2))
        self.assertEqual((texte, cout, statut), ("", 0.0, "erreur"))
        self.assertIn("délai de session dépassé", erreur)
        with self.assertRaises(ValueError):
            AdaptateurClaudeSDK("http://127.0.0.1:8787", delai_s=0)

    def test_garde_pluriels(self):
        """CL34-10 : pluriels signalés."""
        for texte in ("Étapes 1 : préparer", "les injections de consignes", "des portes dérobées", "exécuter les scripts fournis"):
            self.assertTrue(idn.signaux_niveau_methode(texte), texte)
        self.assertFalse(idn.signaux_niveau_methode("classe exfiltration, nommée par protocole") == [], "signal assumé")


class TestCourseV35(CasAvecDossier):
    def cours(self):
        c = TestCourse("test_course_complete")
        c.tmp = self.tmp
        return c

    def test_nombre_borne_et_controles_comptes(self):
        """CL34-11 : nombre ∉ [1, 12] refusé ; CL34-07 : le coût déjà engagé (contrôles) entre au journal et au plafond."""
        c = self.cours()
        fiches = {"opus": [fiche_brute(nom="O1")], "fable": [fiche_brute(nom="F1")]}
        ad = FauxAdaptateur(fiches, notes_par_juge={"juge-fable": c.notes_temoins_ok, "juge-opus": c.notes_temoins_ok})
        for n in (0, 13, True):
            with self.assertRaises(idn.CourseInterrompue):
                c.lancer(ad, f"c-{n}", nombre_par_proposeur=n)
        with self.assertRaises(idn.CourseInterrompue):
            c.lancer(ad, "c-neg", cout_deja_engage_usd=-1)
        self.assertEqual(ad.appels, [])
        res = c.lancer(ad, "c-ok", cout_deja_engage_usd=0.07)
        self.assertAlmostEqual(res["journal"]["cout_appels_de_controle_usd"], 0.07)
        self.assertAlmostEqual(res["journal"]["cout_total_usd"], 0.07 + 4 * 0.5)
        c.lancer(ad, "c-juste", budget_total_usd=2.5, tolerer_somme_plafonds=True)  # sans contrôle : 1,5 + 1 = 2,5, passe
        with self.assertRaises(idn.CourseInterrompue):  # 0,07 + 1,5 + 1 > 2,5 : le contrôle compté arrête avant le dernier juge
            c.lancer(ad, "c-plafond", cout_deja_engage_usd=0.07, budget_total_usd=2.5, tolerer_somme_plafonds=True)
        with self.assertRaises(idn.CourseInterrompue):  # CL37-03 : sans tolérance, 4,07 > 4 refusé avant tout appel
            n = len(ad.appels)
            c.lancer(ad, "c-somme", cout_deja_engage_usd=0.07, budget_total_usd=4.0)
        self.assertEqual(len(ad.appels), n)

    def test_taille_max_pieces_bornee(self):
        """v37 : taille des pièces réglable, plafond dur, consignée au manifeste ; hors borne → refus avant tout appel."""
        c = self.cours()
        ad = FauxAdaptateur({"opus": [fiche_brute()], "fable": [fiche_brute()]})
        for t in (0, idn.TAILLE_MAX_PIECES_ABSOLUE + 1, True, 10.0):
            with self.assertRaises(idn.CourseInterrompue):
                c.lancer(ad, f"t-{t}", taille_max_pieces=t)
        self.assertEqual(ad.appels, [])
        with self.assertRaises(idn.PieceInterdite):  # pièces plus longues que le réglage
            c.lancer(ad, "t-court", taille_max_pieces=5)
        res = c.lancer(ad, "t-ok", taille_max_pieces=650_000)
        with open(os.path.join(self.tmp, "t-ok", "manifeste-depart.json")) as f:
            m = json.load(f)["reglages"]
        self.assertEqual(m["taille_max_pieces"], 650_000)
        self.assertGreater(m["taille_pieces_servies"]["proposeurs"], 0)
        self.assertIsNotNone(res["classement"])

    def test_manifeste_de_fin_sur_toute_exception(self):
        """CL34-09 : une exception qui n'est pas CourseInterrompue écrit quand même le manifeste de fin, puis remonte."""
        class AdaptateurQuiCasse(FauxAdaptateur):
            def lancer(self, role, consigne, dossier, budget_usd, max_tours, modele=None):
                raise OSError("relais injoignable")
        c = self.cours()
        ad = AdaptateurQuiCasse({"opus": [fiche_brute()], "fable": [fiche_brute()]})
        with self.assertRaises(OSError):
            c.lancer(ad, "c-casse")
        chemin = os.path.join(self.tmp, "c-casse", "manifeste-fin.json")
        self.assertTrue(os.path.exists(chemin + ".sha256"))
        with open(chemin) as f:
            self.assertIn("OSError", json.load(f)["reglages"]["erreur"])


if __name__ == "__main__":
    unittest.main()
