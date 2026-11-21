"""Essais du lot 4 du véhicule NA-1 — adaptateur Claude neuf (sans texte système ; réponses brutes conservées), faux
fournisseur (boucle locale), analyse du relevé. Le kit d'agent est imité (`FauxKit`) : aucun appel, aucune clé. Le relevé
réel, par l'outil, contre le faux fournisseur, est joué à part (`releve_sans_systeme_na_v1.py direct`)."""

import http.client
import json
import os
import shutil
import sys
import tempfile
import unittest

ICI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ICI)

import aides_na_lot4_v1 as H  # noqa: E402
from pole import adaptateur_claude_na_v1 as ac  # noqa: E402
from pole import adaptateurs as ad  # noqa: E402
from pole import faux_fournisseur_na_v1 as ff  # noqa: E402
from pole import releve_sans_systeme_na_v1 as rl  # noqa: E402
from pole.relais import NOMS_DE_CLE, CleDansEnvironnement  # noqa: E402

MODELE = ad.MODELES_REELS_PERMIS[0]
URL = "http://127.0.0.1:9"
CONSIGNE = "Consigne d'essai inerte, « accentuée ».\n"


class Base(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp(prefix="essais-na-lot4-ad-")
        self.addCleanup(shutil.rmtree, self.tmp, True)
        self.reponses = os.path.join(self.tmp, "sortie", "reponses-brutes")
        os.makedirs(self.reponses)
        self.dossier = os.path.join(self.tmp, "course", "sessions", "session-essai")
        os.makedirs(self.dossier)

    def adaptateur(self, kit, forme="chaine_vide", **kw):
        return ac.AdaptateurClaudeNA(URL, self.reponses, forme_sans_systeme=forme, arme=True, sdk=kit, environnement={},
                                     **kw)

    def conservees(self):
        rendu = []
        for f in sorted(os.listdir(self.reponses)):
            if f.endswith(".json"):
                with open(os.path.join(self.reponses, f), "rb") as fh:
                    octets = fh.read()
                with open(os.path.join(self.reponses, f + ".sha256"), encoding="utf-8") as fh:
                    compagnon = fh.read().split()
                rendu.append((f, json.loads(octets.decode("utf-8")), compagnon == [H.sha(octets), f]))
        return rendu


class TestSansTexteSysteme(Base):
    def test_options_sans_texte_systeme_chaine_vide(self):
        kit = H.FauxKit(H.script_normal())
        self.adaptateur(kit).lancer("proposeur_ideation", CONSIGNE, self.dossier, 0.5, 1, modele=MODELE)
        self.assertEqual(kit.options_recues[0].reglages["system_prompt"], "")
        self.assertEqual(kit.consignes_recues, [CONSIGNE])

    def test_options_sans_texte_systeme_absent(self):
        kit = H.FauxKit(H.script_normal())
        self.adaptateur(kit, forme="absent").lancer("juge_ideation", CONSIGNE, self.dossier, 0.5, 1, modele=MODELE)
        self.assertIsNone(kit.options_recues[0].reglages["system_prompt"])

    def test_reste_du_transport_garde(self):
        for role in ac.ROLES_NA:
            o = ac.construire_options_na(self.dossier, 0.5, 1, url_relais=URL, modele=MODELE, role=role)
            d = ad.construire_options(self.dossier, 0.5, 1, url_relais=URL, modele=MODELE, role=role)
            for k in d:
                if k not in ("system_prompt", "crochets"):
                    self.assertEqual(o[k], d[k], k)
            self.assertEqual((o["tools"], o["max_turns"], o["fallback_model"]), ([], 1, None))
            self.assertTrue(o["sandbox"]["enabled"])
            self.assertEqual(o["system_prompt"], "")

    def test_adaptateur_d_origine_pose_son_texte(self):
        for role in ac.ROLES_NA:
            d = ad.construire_options(self.dossier, 0.5, 1, url_relais=URL, modele=MODELE, role=role)
            self.assertEqual(d["system_prompt"], ad.CONSIGNES_SYSTEME[role])
            self.assertTrue(d["system_prompt"])

    def test_roles_et_formes_refuses(self):
        with self.assertRaises(ValueError):
            ac.construire_options_na(self.dossier, 0.5, 1, url_relais=URL, modele=MODELE, role="experimentateur")
        with self.assertRaises(ValueError):
            ac.construire_options_na(self.dossier, 0.5, 1, url_relais=URL, modele=MODELE, role="juge_ideation",
                                     forme_sans_systeme="texte")
        with self.assertRaises(ValueError):
            self.adaptateur(H.FauxKit(), forme="texte")
        with self.assertRaises(ValueError):
            ac.AdaptateurClaudeNA(URL, "relatif", arme=True)
        with self.assertRaises(TypeError):
            self.adaptateur(H.FauxKit(H.script_normal())).lancer("juge_ideation", b"octets", self.dossier, 0.5, 1,
                                                                 modele=MODELE)

    def test_non_arme_cle_dans_l_environnement_modele_non_permis(self):
        kit = H.FauxKit(H.script_normal())
        with self.assertRaises(ad.MoteurNonArme):
            ac.AdaptateurClaudeNA(URL, self.reponses, sdk=kit, environnement={}).lancer(
                "juge_ideation", CONSIGNE, self.dossier, 0.5, 1, modele=MODELE)
        with self.assertRaises(CleDansEnvironnement):
            ac.AdaptateurClaudeNA(URL, self.reponses, sdk=kit, environnement={NOMS_DE_CLE[0]: "x"}, arme=True).lancer(
                "juge_ideation", CONSIGNE, self.dossier, 0.5, 1, modele=MODELE)
        with self.assertRaises(ad.ModeleNonPermis):
            self.adaptateur(kit).lancer("juge_ideation", CONSIGNE, self.dossier, 0.5, 1, modele="modele-essai")
        self.assertEqual(kit.options_recues, [])
        self.assertEqual(self.conservees(), [])

    def test_lu_comme_adaptateur_reel_par_le_noyau(self):
        from pole import adaptateurs_v56 as ad56
        self.assertTrue(ad56.est_adaptateur_reel(self.adaptateur(H.FauxKit())))


class TestReponsesBrutes(Base):
    def test_reponse_normale_conservee(self):
        kit = H.FauxKit(H.script_normal("Réponse factice inerte, « rendue »."))
        r = self.adaptateur(kit).lancer("proposeur_ideation", CONSIGNE, self.dossier, 0.5, 1, modele=MODELE)
        self.assertEqual((r.statut, r.texte_brut, r.modele_servi), ("ok", "Réponse factice inerte, « rendue ».", MODELE))
        [(nom, objet, compagnon)] = self.conservees()
        self.assertEqual(nom, "reponse-brute-session-essai.json")
        self.assertTrue(compagnon)
        self.assertEqual((objet["statut"], objet["texte_brut"], objet["session"]),
                         ("ok", "Réponse factice inerte, « rendue ».", "session-essai"))
        self.assertNotIn("consigne", json.dumps(objet))

    def test_refus_et_erreur_conserves(self):
        for script, statut in ((H.script_refus(), "refus"), (H.script_erreur(), "erreur")):
            kit = H.FauxKit(script)
            r = self.adaptateur(kit).lancer("proposeur_ideation", CONSIGNE, self.dossier, 0.5, 1, modele=MODELE)
            self.assertEqual(r.statut, statut)
        objets = {o["statut"]: o for _, o, c in self.conservees() if c}
        self.assertEqual(sorted(objets), ["erreur", "refus"])
        self.assertEqual(objets["refus"]["refus"]["evenement"], "assistant.stop_reason")
        self.assertEqual(objets["erreur"]["texte_brut"], "erreur factice inerte")

    def test_noms_jamais_ecrases(self):
        kit = H.FauxKit(H.script_normal())
        a = self.adaptateur(kit)
        a.lancer("juge_ideation", CONSIGNE, self.dossier, 0.5, 1, modele=MODELE)
        a.lancer("juge_ideation", CONSIGNE, self.dossier, 0.5, 1, modele=MODELE)
        self.assertEqual([n for n, _, _ in self.conservees()],
                         ["reponse-brute-session-essai-2.json", "reponse-brute-session-essai.json"])

    def test_exception_conservee_puis_relevee(self):
        kit = H.FauxKit(lever=RuntimeError("panne factice du kit"))
        with self.assertRaises(RuntimeError):
            self.adaptateur(kit).lancer("juge_ideation", CONSIGNE, self.dossier, 0.5, 1, modele=MODELE)
        [(_, objet, compagnon)] = self.conservees()
        self.assertEqual((objet["statut"], objet["erreur"], compagnon), ("exception", "RuntimeError", True))

    def test_conservation_impossible_rien_n_est_rendu(self):
        kit = H.FauxKit(H.script_normal())
        a = self.adaptateur(kit)
        shutil.rmtree(self.reponses)
        with self.assertRaises(ac.ConservationImpossible) as cm:
            a.lancer("proposeur_ideation", CONSIGNE, self.dossier, 0.5, 1, modele=MODELE)
        self.assertNotIn("Réponse", str(cm.exception))

    def test_conservation_impossible_par_un_fichier_a_la_place(self):
        kit = H.FauxKit(H.script_normal())
        a = self.adaptateur(kit)
        shutil.rmtree(self.reponses)
        with open(self.reponses, "w", encoding="utf-8"):
            pass
        with self.assertRaises(ac.ConservationImpossible):
            a.lancer("proposeur_ideation", CONSIGNE, self.dossier, 0.5, 1, modele=MODELE)


class TestFauxFournisseur(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp(prefix="essais-na-lot4-ff-")
        self.addCleanup(shutil.rmtree, self.tmp, True)

    def faux(self, **kw):
        f = ff.FauxFournisseur(**kw).demarrer()
        self.addCleanup(f.fermer)
        return f

    def poster(self, f, corps, chemin="/v1/messages?beta=true", cle="jeton-factice"):
        port = int(f.url.rsplit(":", 1)[1])
        c = http.client.HTTPConnection("127.0.0.1", port, timeout=10)
        try:
            c.request("POST", chemin, body=json.dumps(corps).encode(), headers={"Content-Type": "application/json",
                                                                               "x-api-key": cle})
            r = c.getresponse()
            return r.status, r.read().decode("utf-8")
        finally:
            c.close()

    def test_n_ecoute_que_sur_la_boucle_locale(self):
        with self.assertRaises(ff.FauxFournisseurRefuse):
            ff.FauxFournisseur(hote="0.0.0.0")
        self.assertTrue(self.faux().url.startswith("http://127.0.0.1:"))

    def test_modes(self):
        f = self.faux()
        corps = {"model": "modele-essai", "max_tokens": 10, "messages": [{"role": "user", "content": "x"}]}
        statut, texte = self.poster(f, corps)
        self.assertEqual((statut, json.loads(texte)["content"][0]["text"]), (200, ff.TEXTE_INERTE))
        statut, texte = self.poster(f, dict(corps, stream=True))
        self.assertEqual(statut, 200)
        self.assertIn('"stop_reason": "end_turn"', texte)
        self.assertIn('"model": "modele-essai"', texte)
        f.changer_mode("classifieur")
        self.assertIn('"stop_reason": "refusal"', self.poster(f, dict(corps, stream=True))[1])
        f.changer_mode("coupee")
        self.assertIn('"stop_reason": "max_tokens"', self.poster(f, dict(corps, stream=True))[1])
        f.changer_mode("credit")
        self.assertEqual(self.poster(f, corps)[0], 400)
        f.changer_mode("acces")
        self.assertEqual(self.poster(f, corps)[0], 401)
        self.assertEqual(self.poster(f, corps, chemin="/v1/messages/count_tokens")[0], 200)
        self.assertEqual(self.poster(f, corps, chemin="/autre")[0], 404)
        with self.assertRaises(ff.FauxFournisseurRefuse):
            f.changer_mode("inconnu")

    def test_garde_et_journal_sans_secret(self):
        journal = os.path.join(self.tmp, "journal-faux.jsonl")
        f = self.faux(journal=journal)
        self.poster(f, {"model": "m", "messages": []}, cle="valeur-a-ne-pas-garder")
        [r] = ff.lire_journal(journal)
        self.assertEqual(r["en_tetes"]["x-api-key"], "présent")
        self.assertNotIn("valeur-a-ne-pas-garder", json.dumps(r))
        self.assertEqual(f.requetes[0]["corps_sha256"], r["corps_sha256"])
        with self.assertRaises(ff.FauxFournisseurRefuse):
            ff.FauxFournisseur(journal=journal)


class TestAnalyseDuReleve(unittest.TestCase):
    MODELE = "modele-essai-releve"

    def test_corps_sans_ajout(self):
        corps = {"model": self.MODELE, "messages": [{"role": "user", "content": rl.CONSIGNE_INERTE}], "max_tokens": 5}
        a = rl.analyser_corps(corps, rl.CONSIGNE_INERTE, self.MODELE)
        self.assertEqual((a["texte_systeme_recu"], a["textes_ajoutes_aux_messages"], a["consigne"], a["modele"]),
                         (False, [], "retrouvée à l'octet", rl.MODELE_ECRIT))
        self.assertTrue(a["modele_egal_au_demande"])

    def test_corps_avec_texte_systeme_et_ajout(self):
        corps = {"model": self.MODELE, "system": [{"type": "text", "text": "Texte d'outil."}],
                 "messages": [{"role": "user", "content": [{"type": "text", "text": rl.CONSIGNE_INERTE.rstrip()}]},
                              {"role": "system", "content": [{"type": "text", "text": f"Modèle : {self.MODELE}."}]}],
                 "tools": [], "metadata": {"user_id": "u"}}
        a = rl.analyser_corps(corps, rl.CONSIGNE_INERTE, self.MODELE)
        self.assertTrue(a["texte_systeme_recu"])
        self.assertEqual(a["consigne"], "retrouvée sans son blanc final")
        self.assertEqual(a["textes_ajoutes_aux_messages"], [f"Modèle : {rl.MODELE_ECRIT}."])
        self.assertEqual(a["messages"][1]["blocs"][0]["identifiant_de_modele_masque"], 1)
        self.assertEqual(a["autres_champs"]["metadata"], {"cles": ["user_id"]})
        self.assertNotIn(self.MODELE, json.dumps(a))

    def test_masquer(self):
        self.assertEqual(rl.masquer("a M b M", "M"), (f"a {rl.MODELE_ECRIT} b {rl.MODELE_ECRIT}", 2))
        self.assertEqual(rl.masquer(None, "M"), (None, 0))

    def test_masquer_le_dossier_du_releve(self):
        ancien = list(rl._RACINES)
        self.addCleanup(rl._RACINES.__setitem__, slice(None), ancien)
        rl._RACINES[:] = ["/racine/factice/du/releve"]
        texte = "Primary working directory: /racine/factice/du/releve/course/sessions/s1 ; modèle M"
        self.assertEqual(rl.masquer(texte, "M"),
                         (f"Primary working directory: {rl.RACINE_ECRITE}/course/sessions/s1 ; modèle {rl.MODELE_ECRIT}", 1))


if __name__ == "__main__":
    unittest.main()
