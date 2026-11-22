"""Aides des essais du lot 4 v3 du véhicule NA-1 (lisent `appel_garde_na_v3`, `adaptateur_claude_direct_na_v2`) : données
factices seules, noms de modèles neutres (`modele-role-essai`, `modele-repli-1-essai`, `modele-repli-2-essai`), aucune clé,
aucun appel à un fournisseur.

- `FauxClientMessages` : imite l'interface des messages que lit l'adaptateur direct (`messages.with_raw_response.create`,
  `messages.stream`, `max_retries`), sans réseau. Il rend, dans l'ordre d'un script, des réponses (raison d'arrêt, catégorie,
  usage, modèle servi choisis), des refus « refusal », des erreurs de statut (crédit d'amont, plafond du relais, modèle non
  permis, surcharge) ou de connexion ; il garde chaque corps reçu. Le modèle servi par défaut est le modèle demandé.
- Les jeux de réglages, la table des valeurs admises et le barème sont des **valeurs d'essai, non opposables** : aucune
  n'est une valeur du fournisseur.
- `Montage` : la génération d'essai `GenerationEssai(AppelGardeNA v3, NoyauEssai)` sur la table de course du lot 4 v1 (les
  clés `cle_a` et `cle_b` sont des clés Claude, servies par l'adaptateur direct ; les autres gardent l'adaptateur
  enregistreur), avec **le vrai `appel` du noyau** (`OrchestreV56.appel`).
"""

import json
import os
import shutil
import sys
import tempfile

ICI = os.path.dirname(os.path.abspath(__file__))
RACINE_ORCHESTRATEUR = os.path.dirname(ICI)
for _p in (ICI, RACINE_ORCHESTRATEUR):
    if _p not in sys.path:
        sys.path.insert(0, _p)

import aides_na_lot4_v1 as H1  # noqa: E402
import aides_na_v4 as A  # noqa: E402
from pole import adaptateur_claude_direct_na_v2 as ad  # noqa: E402
from pole import appel_garde_na_v3 as ag  # noqa: E402
from pole import journal_na_v3 as jn  # noqa: E402
from pole import routage_na_v1 as rt  # noqa: E402

MODELE_ROLE = "modele-role-essai"
REPLI_1, REPLI_2 = "modele-repli-1-essai", "modele-repli-2-essai"
MODELES_REPLI = (REPLI_1, REPLI_2)
MODELES_ADMIS = (MODELE_ROLE, REPLI_1, REPLI_2)
EFFORTS_ESSAI = ("bas", "moyen", "haut")  # valeurs d'essai, non opposables
ADMIS_ESSAI = {m: {"max_tokens_max": 128_000, "efforts": list(EFFORTS_ESSAI), "reflexions": ["adaptive", "omise"]}
               for m in MODELES_ADMIS}
BAREME_ESSAI = {MODELE_ROLE: [4.0, 20.0, 5.0, 0.2], REPLI_1: [5.0, 25.0, 6.25, 0.5], REPLI_2: [3.0, 15.0, 3.75, 0.3]}
JETON = "relais-local-sans-cle"


def jeu(max_tokens=8000, effort="haut", reflexion="adaptive", flux=False):
    return {"max_tokens": max_tokens, "effort": effort, "reflexion": reflexion, "flux": flux}


def reglages_essai(**par_modele):
    """Un jeu par rôle du kit et par modèle admis ; `par_modele` remplace le jeu d'un modèle pour les deux rôles."""
    return {r: {m: dict(par_modele.get(m, jeu(effort="haut" if r == "proposeur_ideation" else "moyen")))
                for m in MODELES_ADMIS} for r in ad.ROLES_NA}


# --- le faux client de l'interface des messages ---------------------------------------------------------------------------

class FauxErreurStatut(Exception):
    """Une erreur rendue par un statut (forme de `APIStatusError` : `status_code`, `body`, `type`)."""

    def __init__(self, status_code, body=None, type_=None):
        super().__init__(f"statut {status_code}")
        self.status_code, self.body, self.type = status_code, body, type_


class FauxErreurConnexion(Exception):
    """Une erreur sans statut (connexion, délai)."""


ERREURS_API_ESSAI = (FauxErreurStatut, FauxErreurConnexion)


def credit_amont():
    return FauxErreurStatut(402, {"type": "error", "error": {"type": "billing_error", "message": "inerte"}}, "billing_error")


def plafond_relais():
    return FauxErreurStatut(402, {"erreur": "plafond de dépense du relais atteint", "plafond_usd": 1.0})


def modele_refuse_relais():
    return FauxErreurStatut(403, {"erreur": "modèle non permis", "modele_demande": "x"})


MESSAGE_SOLDE_ESSAI = "Your Credit Balance is too LOW to access the interface (message d'essai, inerte)."


def credit_400(message=MESSAGE_SOLDE_ESSAI, statut=400, type_="invalid_request_error"):
    """La forme du crédit épuisé reçue ce jour sur une clé (vérification du lot 4 v2, B1) : 400, `invalid_request_error`,
    message de solde ; `message`, `statut`, `type_` changés pour les artefacts."""
    return FauxErreurStatut(statut, {"type": "error", "error": {"type": type_, "message": message}}, type_)


def acces_refuse():
    return FauxErreurStatut(403, {"type": "error", "error": {"type": "permission_error", "message": "inerte"}},
                            "permission_error")


def surcharge():
    return FauxErreurStatut(529, {"type": "error", "error": {"type": "overloaded_error", "message": "inerte"}},
                            "overloaded_error")


def reponse(texte="Réponse factice inerte.", raison="end_turn", categorie=None, usage="defaut", modele="demande",
            details=True, blocs_en_plus=(), iterations=None):
    """Une réponse du faux fournisseur ; `modele="demande"` : le modèle demandé ; `None` : champ absent."""
    return {"_reponse": True, "texte": texte, "raison": raison, "categorie": categorie, "usage": usage, "modele": modele,
            "details": details, "blocs_en_plus": list(blocs_en_plus), "iterations": iterations}


def refus(categorie=None, usage="defaut", modele="demande", details=True):
    return reponse(texte="", raison="refusal", categorie=categorie, usage=usage, modele=modele, details=details)


class _Brut:
    def __init__(self, message):
        self._message = message
        self.http_response = type("ReponseHTTP", (), {"text": json.dumps(message, ensure_ascii=False)})()

    def parse(self):
        return dict(self._message)


class _Flot:
    def __init__(self, message, erreur_en_cours=None):
        self._message, self._erreur = message, erreur_en_cours

    def __enter__(self):
        return self

    def __exit__(self, *a):
        return False

    def __iter__(self):
        yield {"type": "message_start", "message": {"model": self._message.get("model"), "usage": {}}}
        if self._erreur is not None:
            raise self._erreur
        yield {"type": "message_delta", "delta": {"stop_reason": self._message.get("stop_reason")}}

    def get_final_message(self):
        return dict(self._message)


class _Messages:
    def __init__(self, client):
        self._c = client
        self.with_raw_response = type("AvecBrut", (), {"create": staticmethod(self._create_brut)})()

    def _suivant(self, corps):
        self._c.corps_recus.append(json.loads(json.dumps(corps)))
        e = self._c.script.pop(0) if self._c.script else reponse()
        if isinstance(e, BaseException):
            raise e
        return self._c.message_de(e, corps)

    def _create_brut(self, **corps):
        return _Brut(self._suivant(corps))

    def stream(self, **corps):
        e = self._c.script[0] if self._c.script else None
        if isinstance(e, tuple) and e and e[0] == "erreur en cours de flux":
            self._c.script.pop(0)
            self._c.corps_recus.append(json.loads(json.dumps(corps)))
            return _Flot(self._c.message_de(reponse(), corps), erreur_en_cours=e[1])
        return _Flot(self._suivant(corps))


class FauxClientMessages:
    def __init__(self, script=None, max_retries=0):
        self.script, self.max_retries, self.corps_recus = list(script or []), max_retries, []
        self.messages = _Messages(self)

    @staticmethod
    def message_de(e, corps):
        modele = corps["model"] if e["modele"] == "demande" else e["modele"]
        usage = {"input_tokens": 1000, "output_tokens": 500} if e["usage"] == "defaut" else e["usage"]
        if e["iterations"] is not None and isinstance(usage, dict):
            usage = dict(usage, iterations=e["iterations"])
        m = {"id": "msg_essai", "type": "message", "role": "assistant",
             "content": ([{"type": "text", "text": e["texte"]}] if e["texte"] else []) + e["blocs_en_plus"],
             "stop_reason": e["raison"], "stop_sequence": None}
        if modele is not None:
            m["model"] = modele
        if usage is not None:
            m["usage"] = usage
        m["stop_details"] = ({"type": "refusal", "category": e["categorie"], "explanation": None}
                             if e["raison"] == "refusal" and e["details"] else None)
        return m


def fabrique(client):
    return lambda url, delai: (client, ERREURS_API_ESSAI)


def adaptateur_direct(dossier_reponses, script=None, client=None, reglages=None, admis=None, bareme=None,
                      modeles_admis=MODELES_ADMIS, environnement=None, arme=True):
    client = client if client is not None else FauxClientMessages(script)
    a = ad.AdaptateurClaudeDirectNA(H1.RELAIS_A, dossier_reponses, modeles_admis=modeles_admis,
                                    reglages=reglages if reglages is not None else reglages_essai(),
                                    admis=admis if admis is not None else ADMIS_ESSAI,
                                    bareme=bareme if bareme is not None else {m: BAREME_ESSAI[m] for m in modeles_admis},
                                    environnement={} if environnement is None else environnement, arme=arme,
                                    fabrique_client=fabrique(client))
    a.client_essai = client
    return a


# --- le contexte et le montage --------------------------------------------------------------------------------------------

def roles_claude(t):
    return [r for r, e in t.roles.items() if e.cle != rt.CLE_HORS_COURSE and t.cles[e.cle].type == "claude_sdk"]


def modeles_par_role(t):
    return {r: MODELE_ROLE for r in roles_claude(t)}


def pires_repli(t):
    p1 = H1.pires(t)
    return {r: {REPLI_1: p1[r], REPLI_2: p1[r]} for r in roles_claude(t)}


class GenerationEssai(ag.AppelGardeNA, H1.NoyauEssai):
    pass


class Montage:
    """Une génération d'essai v3 et tout ce qu'elle lit, dans un dossier temporaire neuf. `scripts` : {adaptateur Claude :
    script du faux client} ; `reglages` : {adaptateur enregistreur : réglages}."""

    def __init__(self, objet=None, marque="course", generation=1, portee_arret_1="appel", cumul=None, scripts=None,
                 reglages=None, journal_nom="journal-requetes-g1.jsonl", pires_repli_=None, modeles_repli=MODELES_REPLI,
                 classe=GenerationEssai, adaptateurs_en_plus=None):
        self.dossier = tempfile.mkdtemp(prefix="essais-na-lot4-v3-")
        self.sortie = os.path.join(self.dossier, "sortie")
        self.reponses = os.path.join(self.sortie, "reponses-brutes")
        os.makedirs(self.reponses)
        self.table = H1.table(objet, marque)
        self.journal = jn.JournalRequetes(self.sortie, journal_nom)
        self.garde = A.garde_essai()
        self.cumul = cumul if cumul is not None else rt.CumulParCle(self.table)
        self.contexte = ag.ContexteAppelGardeNA(
            numero_generation=generation if self.table.marque == rt.MARQUE_COURSE else None, table=self.table,
            parts=H1.parts(self.table), pires_par_role=H1.pires(self.table), journal=self.journal, garde=self.garde,
            identifiant_case_de_session=H1.case_de_session, cumul=self.cumul,
            modeles_par_role=modeles_par_role(self.table), modeles_repli=modeles_repli,
            pires_repli=pires_repli_ if pires_repli_ is not None else pires_repli(self.table),
            portee_arret_1=portee_arret_1)
        self.ad = H1.adaptateurs(**(reglages or {}))
        scripts = scripts or {}
        for nom in ("ad_a", "ad_b"):
            self.ad[nom] = adaptateur_direct(self.reponses, scripts.get(nom))
        self.ad.update(adaptateurs_en_plus or {})
        self.gen = classe(self.ad, self.dossier, contexte_na=self.contexte)

    def fermer(self):
        shutil.rmtree(self.dossier, True)

    def client(self, nom="ad_a"):
        return self.ad[nom].client_essai

    def etat(self, reste=50.0, cout=0.0):
        return {"cout": cout, "reste": reste, "coupee": False, "etape": "proposition", "plafond_dur_usd": reste}

    def appeler(self, role, requete, fournisseur=None, etat=None, session=None, plafond_role=None, modele=None, lire=None):
        e = self.table.entree(role)
        fournisseur = fournisseur if fournisseur is not None else e.adaptateur
        modele = modele if modele is not None else (MODELE_ROLE if role in self.contexte.modeles_par_role
                                                    else H1.MODELE_ESSAI)
        plafond_role = plafond_role or {"proposeur": "proposeur", "portier": "aiguilleur", "juge": "juge"}[
            e.sorte if e is not None else "juge"]
        role_kit = "proposeur_ideation" if (e is not None and e.sorte == "proposeur") else "juge_ideation"
        self.dernier_etat = etat if etat is not None else self.etat()
        return self.gen.appel(self.dernier_etat, role=role, role_kit=role_kit, fournisseur=fournisseur, modele=modele,
                              consigne=requete, plafond_role=plafond_role,
                              session=session if session is not None else H1.session_de(requete, role=role), lire=lire)

    def lignes(self):
        return jn.verifier_journal(self.journal.chemin)

    def envois(self):
        return [l for l in self.lignes() if l["evenement"] == "envoi"]

    def fichiers_reponses(self):
        return sorted(f for f in os.listdir(self.reponses) if f.endswith(".json"))
