"""Véhicule NA-1, lot 6 v5 — faux fournisseur des clés Claude derrière l'**adaptateur direct réel** du lot 4 v3
(`simulation_na_v5`). Aucune clé, aucun réseau, aucune dépense : un faux client de l'interface des messages, sans réseau.

- `FauxClientSimuleNA` : la forme que lit `adaptateur_claude_direct_na_v2` (`max_retries`, `messages.with_raw_response.
  create`). Le texte de chaque réponse servie est celui du moteur simulé du lot 6 (`simulation_na_v1.AdaptateurSimuleNA`,
  inchangé : fiches inertes, étiquettes du portier, verdicts) ; un `scenario(sorte, modele, rang_appel)` d'essai choisit,
  avant le texte, « servie », « refus » (raison `refusal`, catégorie d'essai ou absente) ou « erreur » (statut 500, sans
  réponse). Usage d'essai fixe ; barème d'essai : **valeurs d'essai, non opposables**.
- `fabrique_adaptateurs_na_v5(table, …)` : la fabrique `f(sortie) -> (adaptateurs, portes)` que la course appelle une fois la
  sortie créée : pour chaque adaptateur d'une clé Claude, un `AdaptateurClaudeDirectNA` réel (armé, environnement vide,
  réponses brutes dans la sortie) sur un faux client ; pour les autres clés, l'adaptateur simulé du v1.
"""

import json
import os

from pole import adaptateur_claude_direct_na_v2 as ad
from pole import simulation_na_v1 as sim

VERSION = "simulation-na-v5"
SERVIE, REFUS, ERREUR = "servie", "refus", "erreur"
EFFORTS_ESSAI = ("bas", "moyen", "haut")  # valeurs d'essai, non opposables
USAGE_ESSAI = {"input_tokens": 1000, "output_tokens": 500}
CATEGORIE_ESSAI = "categorie-essai"


class FausseErreurStatutNA(Exception):
    """Une erreur de statut du faux client (500, sans réponse) : classée « erreur de statut » par l'adaptateur direct."""

    def __init__(self, status_code=500):
        super().__init__(f"statut factice {status_code}")
        self.status_code, self.body, self.type = status_code, {"type": "error", "error": {"type": "api_error"}}, "api_error"


ERREURS_API = (FausseErreurStatutNA,)


class _Brut:
    def __init__(self, message):
        self._m = message
        self.http_response = type("ReponseHTTP", (), {"text": json.dumps(message, ensure_ascii=False)})()

    def parse(self):
        return dict(self._m)


class _Messages:
    def __init__(self, client):
        self._c = client
        self.with_raw_response = type("AvecBrut", (), {"create": staticmethod(self._create)})()

    def _create(self, **corps):
        return _Brut(self._c.repondre(corps))


class FauxClientSimuleNA:
    """Le faux client d'un adaptateur direct ; garde le nombre de corps reçus et leurs empreintes, jamais leur texte."""

    def __init__(self, simule, *, scenario=None, max_retries=0):
        self.simule = simule
        self.scenario = scenario
        self.max_retries = max_retries
        self.messages = _Messages(self)
        self.recus = []

    def repondre(self, corps):
        consigne = corps["messages"][0]["content"]
        sorte = sim.sorte_de_requete(consigne)
        modele = corps["model"]
        rang = len(self.recus)
        self.recus.append({"sorte": sorte, "modele": modele})
        choix = self.scenario(sorte, modele, rang) if self.scenario is not None else SERVIE
        if choix == ERREUR:
            raise FausseErreurStatutNA(500)
        if choix == REFUS or (isinstance(choix, tuple) and choix[0] == REFUS):
            cat = choix[1] if isinstance(choix, tuple) else CATEGORIE_ESSAI
            return {"id": "msg-essai", "type": "message", "role": "assistant", "content": [], "model": modele,
                    "stop_reason": "refusal", "stop_sequence": None, "usage": dict(USAGE_ESSAI),
                    "stop_details": {"type": "refusal", "category": cat, "explanation": None}}
        if choix != SERVIE:
            raise ValueError("scénario d'essai : « servie », « refus » ou « erreur »")
        role_kit = "juge_ideation" if sorte != "proposeur" else "proposeur_ideation"
        r = self.simule.lancer(role_kit, consigne, None, 1.0, 1, modele=modele)
        return {"id": "msg-essai", "type": "message", "role": "assistant",
                "content": [{"type": "text", "text": r.texte_final}] if r.texte_final else [], "model": modele,
                "stop_reason": "end_turn", "stop_sequence": None, "usage": dict(USAGE_ESSAI), "stop_details": None}


def reglages_essai(modeles):
    return {r: {m: {"max_tokens": 8000, "effort": "haut" if r == "proposeur_ideation" else "moyen", "reflexion": "adaptive",
                    "flux": False} for m in modeles} for r in ad.ROLES_NA}


def admis_essai(modeles):
    return {m: {"max_tokens_max": 128_000, "efforts": list(EFFORTS_ESSAI), "reflexions": ["adaptive", "omise"]}
            for m in modeles}


def bareme_essai(modeles):
    return {m: [1.0, 2.0, 0.0, 0.0] for m in modeles}


def fabrique_adaptateurs_na_v5(table, *, declaration, items, modeles_claude, cout_par_appel_usd=0.01, scenario=None,
                               decider=None, clients=None):
    """La fabrique de la course : `f(sortie) -> (adaptateurs, None)`. `modeles_claude` : la liste fermée des modèles
    admis par chaque adaptateur direct (modèles des rôles et deux de repli). `scenario` : {nom d'adaptateur: f(sorte,
    modele, rang)} pour les adaptateurs directs. `clients` (essais) : un dictionnaire rempli des faux clients."""
    scenario = scenario or {}

    def fabrique(sortie):
        dossier = os.path.join(sortie, "reponses-brutes")
        os.makedirs(dossier, exist_ok=False)
        simules = sim.adaptateurs_simules_na(table, declaration=declaration, items=items,
                                             cout_par_appel_usd=cout_par_appel_usd, decider=decider)
        rendu = {}
        for nom, a in simules.items():
            cles = [c for c in table.cles.values() if nom in c.adaptateurs]
            if cles and cles[0].type == "claude_sdk":
                client = FauxClientSimuleNA(a, scenario=scenario.get(nom))
                if clients is not None:
                    clients[nom] = client
                d = ad.AdaptateurClaudeDirectNA(cles[0].relais, dossier, modeles_admis=tuple(modeles_claude),
                                                reglages=reglages_essai(modeles_claude), admis=admis_essai(modeles_claude),
                                                bareme=bareme_essai(modeles_claude), environnement={}, arme=True,
                                                fabrique_client=lambda url, delai, c=client: (c, ERREURS_API))
                rendu[nom] = d
            else:
                rendu[nom] = a
        return rendu, None

    return fabrique


__all__ = ("FauxClientSimuleNA", "FausseErreurStatutNA", "fabrique_adaptateurs_na_v5", "SERVIE", "REFUS", "ERREUR",
           "reglages_essai", "admis_essai", "bareme_essai")
