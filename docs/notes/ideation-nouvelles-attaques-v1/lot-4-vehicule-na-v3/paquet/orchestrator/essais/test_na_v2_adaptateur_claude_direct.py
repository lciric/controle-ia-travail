"""Essais de l'adaptateur Claude direct du véhicule NA-1 (`adaptateur_claude_direct_na_v2`), exigences A1 à A7 et N2.

Au faux client de l'interface des messages (`aides_na_lot4_v3.FauxClientMessages`) ; et, pour A1, l'en-tête du relais et
l'égalité sur le corps reçu, au **client réel du kit de l'interface** (`anthropic`, s'il est installé) pointé sur un faux
serveur de la boucle locale (`127.0.0.1`), sans mandataire réseau : aucune requête ne sort de la machine, aucune clé.
"""

import http.server
import json
import os
import shutil
import sys
import tempfile
import threading
import unittest

ICI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ICI)

import aides_na_lot4_v3 as H  # noqa: E402
from pole import adaptateur_claude_direct_na_v2 as ad  # noqa: E402
from pole.adaptateurs import ModeleNonPermis, MoteurNonArme  # noqa: E402
from pole.relais import CleDansEnvironnement  # noqa: E402

try:
    import anthropic  # noqa: F401
    SDK = True
except ImportError:  # pragma: no cover
    SDK = False

CONSIGNE = "Consigne factice, inerte, pour les essais.\n"


class Base(unittest.TestCase):
    def setUp(self):
        self.dossier = tempfile.mkdtemp(prefix="essais-direct-na-")
        self.addCleanup(shutil.rmtree, self.dossier, True)
        self.reponses = os.path.join(self.dossier, "reponses")
        os.makedirs(self.reponses)
        self.session = os.path.join(self.dossier, "sessions", "s1")
        os.makedirs(self.session)

    def adaptateur(self, script=None, **kw):
        return H.adaptateur_direct(self.reponses, script, **kw)

    def lancer(self, a, modele=H.MODELE_ROLE, role="proposeur_ideation", budget=6.05, consigne=CONSIGNE):
        return a.lancer(role, consigne, self.session, budget, 1, modele=modele)

    def brute(self, nom):
        with open(os.path.join(self.reponses, nom), encoding="utf-8") as f:
            return json.load(f)


# --- corps (D2, A2) ---------------------------------------------------------------------------------------------------

class TestCorps(Base):
    def test_cas_sain_consigne_seule_sans_systeme(self):
        a = self.adaptateur()
        r = self.lancer(a)
        self.assertEqual(r.statut, "ok")
        (corps,) = a.client_essai.corps_recus
        self.assertEqual(corps["messages"], [{"role": "user", "content": CONSIGNE}])
        self.assertNotIn("system", corps)
        self.assertEqual(sorted(corps), ["max_tokens", "messages", "model", "output_config", "thinking"])
        self.assertEqual(corps["output_config"], {"effort": "haut"})
        self.assertEqual(corps["thinking"], {"type": "adaptive"})

    def test_reglages_par_role_et_par_modele(self):
        reg = H.reglages_essai(**{H.REPLI_2: H.jeu(max_tokens=4000, effort=None, reflexion="omise")})
        a = self.adaptateur(reglages=reg)
        self.lancer(a, modele=H.REPLI_2)
        self.lancer(a, modele=H.MODELE_ROLE, role="juge_ideation")
        c1, c2 = a.client_essai.corps_recus
        self.assertEqual(sorted(c1), ["max_tokens", "messages", "model"])
        self.assertEqual(c1["max_tokens"], 4000)
        self.assertEqual(c2["output_config"], {"effort": "moyen"})

    def test_artefacts_du_corps_refuses(self):
        corps = ad.construire_corps_na(H.MODELE_ROLE, CONSIGNE, H.jeu())
        ad.verifier_corps_na(dict(corps), CONSIGNE, H.MODELE_ROLE)
        for champ, valeur in (("system", ""), ("fallbacks", "default"), ("betas", ["x"]), ("tools", []),
                              ("metadata", {}), ("temperature", 1.0), ("stream", True)):
            with self.assertRaises(ad.CorpsRefuse, msg=champ):
                ad.verifier_corps_na(dict(corps, **{champ: valeur}), CONSIGNE, H.MODELE_ROLE)
        for messages in ([{"role": "user", "content": CONSIGNE + " "}], [{"role": "system", "content": CONSIGNE}],
                         [{"role": "user", "content": CONSIGNE}, {"role": "user", "content": "x"}],
                         [{"role": "user", "content": [{"type": "text", "text": CONSIGNE}]}]):
            with self.assertRaises(ad.CorpsRefuse):
                ad.verifier_corps_na(dict(corps, messages=messages), CONSIGNE, H.MODELE_ROLE)
        with self.assertRaises(ad.CorpsRefuse):
            ad.verifier_corps_na(dict(corps, model=H.REPLI_1), CONSIGNE, H.MODELE_ROLE)

    def test_refus_avant_toute_requete(self):
        a = self.adaptateur(arme=False)
        with self.assertRaises(MoteurNonArme):
            self.lancer(a)
        b = self.adaptateur(environnement={"ANTHROPIC_API_KEY": "x"})
        with self.assertRaises(CleDansEnvironnement):
            self.lancer(b)
        c = self.adaptateur()
        with self.assertRaises(ModeleNonPermis):
            self.lancer(c, modele="modele-hors-liste")
        self.assertEqual(a.client_essai.corps_recus + b.client_essai.corps_recus + c.client_essai.corps_recus, [])


# --- A1, aucune relance cachée ----------------------------------------------------------------------------------------

class TestA1(Base):
    def test_cas_sain(self):
        self.assertEqual(self.adaptateur()._client.max_retries, 0)

    def test_client_qui_relancerait_refuse_a_la_construction(self):
        with self.assertRaises(ad.RelanceCachee):
            self.adaptateur(client=H.FauxClientMessages(max_retries=2))

    def test_client_change_apres_construction_refuse_avant_l_envoi(self):
        a = self.adaptateur()
        a._client.max_retries = 1
        with self.assertRaises(ad.RelanceCachee):
            self.lancer(a)
        self.assertEqual(a.client_essai.corps_recus, [])

    @unittest.skipUnless(SDK, "kit de l'interface absent")
    def test_client_reel_construit_sans_relance(self):
        client, erreurs = ad.fabrique_client_reel("http://127.0.0.1:9", 5.0)
        self.assertEqual(client.max_retries, 0)
        self.assertTrue(erreurs)


class _Serveur:
    """Faux fournisseur sur la boucle locale : rend, dans l'ordre, (statut, corps JSON) ; garde en-têtes et corps reçus."""

    def __init__(self, script):
        self.script, self.recus = list(script), []
        moi = self

        class G(http.server.BaseHTTPRequestHandler):
            def log_message(self, *a):
                pass

            def do_POST(self):
                n = int(self.headers.get("content-length") or 0)
                corps = self.rfile.read(n)
                moi.recus.append(({k.lower(): v for k, v in self.headers.items()}, corps))
                statut, objet = moi.script.pop(0) if moi.script else moi.script_defaut
                o = json.dumps(objet).encode("utf-8")
                self.send_response(statut)
                self.send_header("content-type", "application/json")
                self.send_header("content-length", str(len(o)))
                self.end_headers()
                self.wfile.write(o)

        self.script_defaut = (529, {"type": "error", "error": {"type": "overloaded_error", "message": "inerte"}})
        self.serveur = http.server.ThreadingHTTPServer(("127.0.0.1", 0), G)
        threading.Thread(target=self.serveur.serve_forever, daemon=True).start()
        self.url = f"http://127.0.0.1:{self.serveur.server_address[1]}"

    def fermer(self):
        self.serveur.shutdown()
        self.serveur.server_close()


def _message(modele, raison="end_turn", texte="Réponse factice inerte.", categorie=None):
    return {"id": "msg_essai", "type": "message", "role": "assistant", "model": modele,
            "content": [{"type": "text", "text": texte}] if texte else [], "stop_reason": raison, "stop_sequence": None,
            "stop_details": {"type": "refusal", "category": categorie, "explanation": None} if raison == "refusal" else None,
            "usage": {"input_tokens": 10, "output_tokens": 5}}


@unittest.skipUnless(SDK, "kit de l'interface absent")
class TestClientReelBoucleLocale(Base):
    def serveur(self, script):
        s = _Serveur(script)
        self.addCleanup(s.fermer)
        return s

    def adaptateur_reel(self, s):
        return ad.AdaptateurClaudeDirectNA(s.url, self.reponses, modeles_admis=H.MODELES_ADMIS, reglages=H.reglages_essai(),
                                           admis=H.ADMIS_ESSAI, bareme=H.BAREME_ESSAI, environnement={}, arme=True,
                                           delai_s=10)

    def test_529_une_seule_requete(self):
        s = self.serveur([])
        r = self.lancer(self.adaptateur_reel(s))
        self.assertEqual(len(s.recus), 1)
        self.assertEqual(r.statut, "erreur")
        self.assertEqual(r.tentative["statut_http"], 529)

    def test_artefact_un_client_a_relances_fait_trois_requetes(self):
        """Le témoin de l'épreuve : le même faux serveur voit les relances d'un client à `max_retries=2`."""
        import anthropic
        s = self.serveur([])
        c = anthropic.Anthropic(base_url=s.url, api_key=H.JETON, max_retries=2, timeout=10,
                                http_client=anthropic.DefaultHttpxClient(trust_env=False))
        with self.assertRaises(anthropic.APIStatusError):
            c.messages.create(model=H.MODELE_ROLE, max_tokens=10, messages=[{"role": "user", "content": "x"}])
        self.assertEqual(len(s.recus), 3)

    def test_en_tetes_et_egalite_sur_le_corps_recu(self):
        s = self.serveur([(200, _message(H.MODELE_ROLE))])
        r = self.lancer(self.adaptateur_reel(s))
        self.assertEqual(r.statut, "ok")
        entetes, corps = s.recus[0]
        self.assertEqual(entetes.get("x-api-key"), H.JETON)
        self.assertNotIn("anthropic-beta", entetes)
        self.assertEqual(ad.octets_consigne_du_corps(corps), CONSIGNE.encode("utf-8"))
        objet = json.loads(corps)
        self.assertNotIn("system", objet)
        self.assertNotIn("fallbacks", objet)
        self.assertEqual(r.modele_servi, H.MODELE_ROLE)

    def test_credit_400_message_de_solde_par_le_client_reel(self):
        """B1 de la vérification du lot 4 v2 : la forme reçue ce jour (400, `invalid_request_error`, message de solde) est un
        crédit d'amont ; un 400 d'un autre message, ou le fragment sous un autre statut, ne l'est pas."""
        msg = H.MESSAGE_SOLDE_ESSAI
        s = self.serveur([
            (400, {"type": "error", "error": {"type": "invalid_request_error", "message": msg}}),
            (400, {"type": "error", "error": {"type": "invalid_request_error", "message": "max_tokens hors borne"}}),
            (429, {"type": "error", "error": {"type": "rate_limit_error", "message": msg}}),
            (402, {"type": "error", "error": {"type": "billing_error", "message": msg}})])
        a = self.adaptateur_reel(s)
        r = [self.lancer(a) for _ in range(4)]
        self.assertEqual([x.tentative["classe_erreur"] for x in r],
                         [ad.ERREUR_CREDIT_AMONT_400, ad.ERREUR_STATUT, ad.ERREUR_STATUT, ad.ERREUR_CREDIT_AMONT])
        for x in r:
            self.assertNotIn("balance", json.dumps(x.tentative, ensure_ascii=False).lower())
            self.assertNotIn("balance", str(x.erreur).lower())

    def test_refus_credit_et_relais_par_le_client_reel(self):
        s = self.serveur([
            (200, _message(H.MODELE_ROLE, raison="refusal", texte="", categorie=None)),
            (402, {"type": "error", "error": {"type": "billing_error", "message": "inerte"}}),
            (402, {"erreur": "plafond de dépense du relais atteint"}),
            (403, {"erreur": "modèle non permis", "modele_demande": H.REPLI_1}),
            (403, {"type": "error", "error": {"type": "permission_error", "message": "inerte"}})])
        a = self.adaptateur_reel(s)
        r = [self.lancer(a) for _ in range(5)]
        self.assertEqual((r[0].statut, r[0].refus["evenement"], r[0].tentative["categorie"]),
                         ("refus", ad.EVENEMENT_REFUS_CLASSIFIEUR, ad.CATEGORIE_NON_LUE))
        self.assertEqual(r[1].tentative["classe_erreur"], ad.ERREUR_CREDIT_AMONT)
        self.assertEqual(r[2].tentative["classe_erreur"], ad.ERREUR_PLAFOND_RELAIS)
        self.assertEqual((r[3].statut, r[3].refus["evenement"]), ("refus", ad.EVENEMENT_MODELE_NON_PERMIS))
        self.assertEqual(r[4].tentative["classe_erreur"], ad.ERREUR_STATUT)
        self.assertEqual(len(s.recus), 5)


# --- A3, coût ---------------------------------------------------------------------------------------------------------

class TestA3(Base):
    def test_cout_par_usage_au_bareme(self):
        r = self.lancer(self.adaptateur([H.refus(usage={"input_tokens": 2000, "output_tokens": 100,
                                                        "cache_read_input_tokens": 1000})]), modele=H.REPLI_1)
        self.assertAlmostEqual(r.cout_declare_usd, (2000 * 5.0 + 100 * 25.0 + 1000 * 0.5) / 1e6)
        self.assertFalse(r.cout_inconnu)

    def test_sans_usage_au_plafond_jamais_a_zero(self):
        for usage in (None, {}, {"input_tokens": "x", "output_tokens": 1}, {"input_tokens": -1, "output_tokens": 0},
                      {"output_tokens": 3}):
            r = self.lancer(self.adaptateur([H.refus(usage=usage)]), budget=6.05)
            self.assertTrue(r.cout_inconnu, usage)
            self.assertEqual(r.cout_declare_usd, 6.05)

    def test_erreur_de_statut_a_zero_connexion_au_plafond(self):
        r = self.lancer(self.adaptateur([H.surcharge()]))
        self.assertEqual((r.cout_declare_usd, r.cout_inconnu), (0.0, False))
        r = self.lancer(self.adaptateur([H.FauxErreurConnexion("coupée")]), budget=0.6)
        self.assertEqual((r.cout_declare_usd, r.cout_inconnu), (0.6, True))

    def test_erreur_apres_le_debut_du_flux_au_plafond(self):
        reg = H.reglages_essai(**{H.MODELE_ROLE: H.jeu(max_tokens=64000, flux=True)})
        a = self.adaptateur([("erreur en cours de flux", H.surcharge())], reglages=reg)
        r = self.lancer(a, budget=6.05)
        self.assertEqual((r.statut, r.cout_inconnu, r.cout_declare_usd), ("erreur", True, 6.05))

    def test_flux_cas_sain(self):
        reg = H.reglages_essai(**{H.MODELE_ROLE: H.jeu(max_tokens=64000, flux=True)})
        a = self.adaptateur([H.reponse("Texte en flux, inerte.")], reglages=reg)
        r = self.lancer(a)
        self.assertEqual((r.statut, r.texte_brut), ("ok", "Texte en flux, inerte."))
        self.assertIn("flux", self.brute(r.tentative["reponse_brute"])["corps_brut"])

    def test_bareme_exige_par_modele(self):
        b = dict(H.BAREME_ESSAI)
        del b[H.REPLI_2]
        with self.assertRaises(ValueError):
            self.adaptateur(bareme=b)
        with self.assertRaises(ValueError):
            self.adaptateur(bareme=dict(H.BAREME_ESSAI, **{H.REPLI_1: [1.0, -2.0, 0.0, 0.0]}))


# --- A4, réponses brutes ----------------------------------------------------------------------------------------------

class TestA4(Base):
    def test_chaque_tentative_conservee_refus_et_erreurs_compris(self):
        a = self.adaptateur([H.refus("cyber"), H.surcharge(), H.reponse()])
        rs = [self.lancer(a), self.lancer(a), self.lancer(a)]
        noms = sorted(f for f in os.listdir(self.reponses) if f.endswith(".json"))
        self.assertEqual(len(noms), 3)
        self.assertEqual(sorted(r.tentative["reponse_brute"] for r in rs), noms)
        for n in noms:
            with open(os.path.join(self.reponses, n), "rb") as f:
                octets = f.read()
            with open(os.path.join(self.reponses, n + ".sha256"), encoding="utf-8") as f:
                self.assertTrue(f.read().startswith(__import__("hashlib").sha256(octets).hexdigest()))
        self.assertEqual(self.brute(rs[0].tentative["reponse_brute"])["categorie"], "cyber")

    def test_texte_brut_non_caviarde(self):
        texte = "Texte factice token=abcdefghijklmnop fin."
        a = self.adaptateur([H.reponse(texte)])
        r = self.lancer(a)
        self.assertNotIn("abcdefghijklmnop", r.texte_final)
        brut = json.loads(self.brute(r.tentative["reponse_brute"])["corps_brut"]["corps_http"])
        self.assertEqual(brut["content"][0]["text"], texte)

    def test_conservation_impossible_rien_n_est_rendu(self):
        a = self.adaptateur([H.reponse()])
        shutil.rmtree(self.reponses)
        with self.assertRaises(ad.ConservationImpossible):
            self.lancer(a)

    def test_exception_conservee_puis_relevee(self):
        a = self.adaptateur([ValueError("panne factice")])
        with self.assertRaises(ValueError):
            self.lancer(a)
        (n,) = [f for f in os.listdir(self.reponses) if f.endswith(".json")]
        self.assertEqual(self.brute(n)["statut"], "exception")


# --- A5, A6 -----------------------------------------------------------------------------------------------------------

class TestCredit400(Base):
    def test_regle_stricte(self):
        cas = (((400, "invalid_request_error", H.MESSAGE_SOLDE_ESSAI), ad.ERREUR_CREDIT_AMONT_400),
               ((400, "invalid_request_error", "CREDIT BALANCE IS TOO LOW"), ad.ERREUR_CREDIT_AMONT_400),
               ((400, "invalid_request_error", "credit balance is low"), ad.ERREUR_STATUT),
               ((400, "invalid_request_error", None), ad.ERREUR_STATUT),
               ((400, "permission_error", H.MESSAGE_SOLDE_ESSAI), ad.ERREUR_STATUT),
               ((401, "invalid_request_error", H.MESSAGE_SOLDE_ESSAI), ad.ERREUR_STATUT),
               ((429, "rate_limit_error", H.MESSAGE_SOLDE_ESSAI), ad.ERREUR_STATUT))
        for (statut, type_, message), attendu in cas:
            self.assertEqual(ad.classer_erreur(H.credit_400(message, statut, type_))[0], attendu, (statut, type_, message))

    def test_message_garde_a_la_seule_reponse_brute(self):
        r = self.lancer(self.adaptateur([H.credit_400()]))
        self.assertEqual(r.tentative["classe_erreur"], ad.ERREUR_CREDIT_AMONT_400)
        self.assertNotIn("balance", json.dumps(r.tentative, ensure_ascii=False).lower())
        brut = self.brute(r.tentative["reponse_brute"])
        self.assertEqual(brut["corps_brut"]["erreur"]["error"]["message"], H.MESSAGE_SOLDE_ESSAI)


class TestA5A6(Base):
    def test_categorie_lue_ou_non_lue(self):
        cas = ((H.refus("cyber"), "cyber"), (H.refus(None), ad.CATEGORIE_NON_LUE), (H.refus(""), ad.CATEGORIE_NON_LUE),
               (H.refus("x", details=False), ad.CATEGORIE_NON_LUE))
        for rep, attendu in cas:
            r = self.lancer(self.adaptateur([rep]))
            self.assertEqual((r.statut, r.tentative["categorie"], r.refus["categorie"]), ("refus", attendu, attendu))
            self.assertFalse(r.tentative["servie"])

    def test_liste_fermee_des_raisons(self):
        cas = (("end_turn", "ok", None), ("refusal", "refus", None), ("max_tokens", "erreur", ad.ERREUR_REPONSE_COUPEE),
               ("pause_turn", "erreur", ad.ERREUR_RAISON_HORS_LISTE), (None, "erreur", ad.ERREUR_RAISON_HORS_LISTE),
               ("stop_sequence", "erreur", ad.ERREUR_RAISON_HORS_LISTE))
        for raison, statut, classe in cas:
            r = self.lancer(self.adaptateur([H.reponse("x", raison=raison)]))
            self.assertEqual((r.statut, r.tentative["classe_erreur"]), (statut, classe), raison)
            self.assertEqual(r.tentative["servie"], raison != "refusal")
            if statut == "refus":
                self.assertEqual(r.refus["evenement"], ad.EVENEMENT_REFUS_CLASSIFIEUR)

    def test_trace_de_repli_du_fournisseur(self):
        for rep in (H.reponse(blocs_en_plus=[{"type": "fallback"}]), H.reponse(iterations=[{"type": "fallback_message"}])):
            r = self.lancer(self.adaptateur([rep]))
            self.assertEqual((r.statut, r.refus["evenement"]), ("refus", ad.EVENEMENT_REPLI_FOURNISSEUR))
        r = self.lancer(self.adaptateur([H.reponse(iterations=[{"type": "message"}])]))
        self.assertEqual(r.statut, "ok")

    def test_modele_servi_rendu_tel_quel(self):
        r = self.lancer(self.adaptateur([H.reponse(modele="modele-autre-essai")]))
        self.assertEqual(r.modele_servi, "modele-autre-essai")


# --- A7, réglages (n° 32) ---------------------------------------------------------------------------------------------

class TestA7(Base):
    def test_cas_sain(self):
        self.assertEqual(len(self.adaptateur().reglages), 6)

    def test_reglage_non_admis_sur_le_second_modele_de_repli(self):
        with self.assertRaises(ad.ReglageNonAdmisNA) as c:
            self.adaptateur(reglages=H.reglages_essai(**{H.REPLI_2: H.jeu(effort="maximal")}))
        self.assertEqual((c.exception.numero, c.exception.reglage, c.exception.modele), (32, "effort", H.REPLI_2))

    def test_autres_reglages_non_admis(self):
        admis = dict(H.ADMIS_ESSAI, **{H.REPLI_1: dict(H.ADMIS_ESSAI[H.REPLI_1], max_tokens_max=32000,
                                                       reflexions=["omise"])})
        for reg, nom in ((H.reglages_essai(**{H.REPLI_1: H.jeu(max_tokens=64000, flux=True)}), "max_tokens"),
                         (H.reglages_essai(**{H.REPLI_1: H.jeu(reflexion="adaptive")}), "reflexion"),
                         (H.reglages_essai(**{H.MODELE_ROLE: H.jeu(max_tokens=20000, flux=False)}), "flux"),
                         (H.reglages_essai(**{H.MODELE_ROLE: dict(H.jeu(), flux="oui")}), "flux"),
                         (H.reglages_essai(**{H.MODELE_ROLE: dict(H.jeu(), temperature=1)}), "jeu")):
            with self.assertRaises(ad.ReglageNonAdmisNA, msg=nom) as c:
                self.adaptateur(reglages=reg, admis=admis)
            self.assertEqual(c.exception.reglage, nom)

    def test_jeu_manquant_pour_un_modele_admis(self):
        reg = H.reglages_essai()
        del reg["juge_ideation"][H.REPLI_1]
        with self.assertRaises(ad.ReglageNonAdmisNA):
            self.adaptateur(reglages=reg)
        admis = dict(H.ADMIS_ESSAI)
        del admis[H.REPLI_2]
        with self.assertRaises(ad.ReglageNonAdmisNA):
            self.adaptateur(admis=admis)


if __name__ == "__main__":
    unittest.main()
