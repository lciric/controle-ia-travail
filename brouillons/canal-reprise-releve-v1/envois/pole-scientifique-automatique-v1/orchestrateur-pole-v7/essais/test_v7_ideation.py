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
        r = ad.lancer("juge_ideation", "consigne", self.tmp, 0.7, 1)
        self.assertEqual((r.statut, r.cout_declare_usd, r.cout_inconnu), ("erreur", 0.7, True))
        self.assertIn("délai", r.erreur)
        pid = int(open(pid_f).read())
        for _ in range(20):
            try:
                os.kill(pid, 0)
                time.sleep(0.1)
            except ProcessLookupError:
                break
        else:
            os.kill(pid, 9)
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
        self.assertTrue(all("argon" not in a["dossier"] for a in ad.appels))
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
        externe est refusé avant tout écrit ; CL35-03 : la commande est consignée."""
        c = self.cours()
        fiches = {"opus": [fiche_brute(nom="O1")], "fable": [fiche_brute(nom="F1")]}
        ad = FauxAdaptateur(fiches, notes_par_juge={"juge-fable": c.notes_temoins_ok, "juge-opus": c.notes_temoins_ok})
        ad.nom = "claude-sdk"
        budgets = dict(c.budgets())
        budgets[("juge_ideation", "autre-lignee-x")] = 1.0
        c.lancer(ad, "cr", budgets=budgets, juges_externes=[("argon", "autre-lignee-x")], budget_externe_usd=2.0,
                 moteur="claude-sdk")
        sortie = os.path.join(self.tmp, "cr")
        att = self.attester(os.path.join(self.tmp, "att-r.json"), sortie)
        simule = FauxAdaptateur({}, notes_par_juge={"argon": c.notes_temoins_ok})
        with self.assertRaises(idn.CourseInterrompue):
            idn.executer_bras_differe(sortie, attestation_lecture_humaine=att, budgets=budgets,
                                      juges_externes=[("argon", "autre-lignee-x", simule)])
        self.assertEqual(simule.appels, [])
        self.assertFalse(os.path.exists(os.path.join(sortie, "manifeste-bras-rapporte.json")))
        # et un proposeur externe simulé sur une course réelle est refusé aussi
        with self.assertRaises(idn.CourseInterrompue):
            budgets[("proposeur_ideation", "gemini-argon")] = 1.0
            c.lancer(ad, "cr2", budgets=budgets,
                     proposeurs_externes=[("argon", "gemini-argon", simule)], budget_externe_usd=2.0, moteur="claude-sdk")


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
        c.lancer(ad, "c-juste", budget_total_usd=2.5)  # sans contrôle : 1,5 + 1 = 2,5, passe
        with self.assertRaises(idn.CourseInterrompue):  # 0,07 + 1,5 + 1 > 2,5 : le contrôle compté arrête avant le dernier juge
            c.lancer(ad, "c-plafond", cout_deja_engage_usd=0.07, budget_total_usd=2.5)

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
