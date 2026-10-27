"""Adaptateurs de moteur : interface, options du Claude Agent SDK (fonction pure) et adaptateur réel.

`AdaptateurSimule` (déterministe, pour les essais) est défini dans `simulation.py` et réexporté ici.
Le paquet `claude_agent_sdk` n'est importé que paresseusement, au premier lancement réel.
"""

import asyncio
import math
import os
from dataclasses import dataclass, field

from .caviardage import caviarder
from .garde_outils import fabriquer_crochet
from .outils import lister_fichiers
from .relais import CleDansEnvironnement, noms_de_cle_presents, valider_url_relais, variables_agent

ROLES = ("experimentateur", "verificateur", "recombinaison", "synthese", "proposeur")
# Décision de Lazar du 27 octobre 2026 (14:17, heure de Paris) : dans l'organisme, côté Claude, seulement Opus 5.5 et
# Fable 5.1. Tout autre nom de modèle est refusé avant tout appel réel (préfixes des identifiants de modèle).
MODELES_REELS_PERMIS = ("claude-opus-5-5", "claude-fable-5-1")
STATUTS_RESULTAT = ("ok", "erreur", "budget_depasse", "tours_epuises", "refuse")
OUTILS_AUTORISES = ("Read", "Write", "Edit", "Bash")
OUTILS_INTERDITS = ("WebFetch", "WebSearch", "Agent", "Task", "NotebookEdit", "Skill", "TodoWrite", "KillShell",
                    "BashOutput", "SlashCommand")
MODE_PERMISSION = "dontAsk"
CONSIGNES_SYSTEME = {
    "experimentateur": ("Tu es expérimentateur du pôle. Tu travailles seulement dans ton dossier courant, sans réseau ni "
                        "clé. Tu exécutes le test gelé tel quel ; tu ne modifies jamais fiche.json. Ta réponse finale "
                        "contient un bloc JSON conforme à la consigne."),
    "verificateur": ("Tu es vérificateur du pôle, d'un autre modèle que l'expérimentateur. Tu rejoues le code dans ton "
                     "dossier, tu vérifies que le test exécuté est le test gelé et que le verdict suit le seuil. Tu "
                     "réponds par un bloc JSON {confirme, test_conforme, motif}."),
    "recombinaison": ("Tu es l'agent de recombinaison du pôle. Tu fusionnes deux fiches survivantes en une fiche fille "
                      "qui prédit plus que ses parents. Tu réponds par un bloc JSON de fiche."),
    "synthese": ("Tu es l'agent de synthèse du pôle. À partir du résumé de l'index fourni, tu écris des leçons courtes "
                 "(causes d'élimination fréquentes, protocoles qui ont fonctionné). Aucune donnée hors du résumé."),
    "proposeur": ("Tu es le proposeur du pôle. À partir du seul contexte public fourni (monde, prédicteurs connus, "
                  "archive, catalogue), tu formules des fiches au gabarit, chacune avec une stratégie déclarée du "
                  "catalogue. Tu réponds par un bloc JSON {fiches}."),
}


@dataclass
class Resultat:
    texte_final: str
    fichiers: list = field(default_factory=list)
    cout_declare_usd: float = 0.0
    statut: str = "ok"
    erreur: object = None


class Adaptateur:
    """Interface : `lancer(role, consigne, dossier, budget_usd, max_tours) -> Resultat` (modèle en option)."""

    nom = "abstrait"

    def lancer(self, role, consigne, dossier, budget_usd, max_tours, modele=None):
        raise NotImplementedError


class MoteurIndisponible(RuntimeError):
    pass


class MoteurNonArme(RuntimeError):
    """Le moteur réel n'est lancé que s'il a été armé explicitement (ligne de commande --confirmer-moteur-reel)."""


class ModeleNonPermis(ValueError):
    """Un modèle réel hors de la liste permise (Opus 5.5, Fable 5.1) : refusé avant tout appel."""


def verifier_modele_reel(modele):
    if not isinstance(modele, str) or not modele.startswith(MODELES_REELS_PERMIS):
        raise ModeleNonPermis(f"modèle réel non permis : {modele!r} (permis : {', '.join(MODELES_REELS_PERMIS)}, "
                              "décision de Lazar du 27 octobre 2026)")
    return modele


def construire_options(dossier, budget_usd, max_tours, *, url_relais, modele=None, role="experimentateur"):
    """Options d'un agent du pôle (fonction pure, sans import du SDK) ; lève ValueError si un réglage est incohérent."""
    if not isinstance(dossier, str) or not os.path.isabs(dossier):
        raise ValueError("le dossier de l'agent doit être un chemin absolu")
    if not isinstance(budget_usd, (int, float)) or isinstance(budget_usd, bool) or not math.isfinite(budget_usd) \
            or budget_usd <= 0:
        raise ValueError("budget_usd : nombre fini strictement positif")
    if not isinstance(max_tours, int) or isinstance(max_tours, bool) or max_tours < 1:
        raise ValueError("max_tours : entier ≥ 1")
    if role not in ROLES:
        raise ValueError(f"rôle inconnu : {role!r}")
    return {
        "cwd": os.path.normpath(dossier),
        "allowed_tools": list(OUTILS_AUTORISES),
        "disallowed_tools": list(OUTILS_INTERDITS),
        "permission_mode": MODE_PERMISSION,
        "max_turns": max_tours,
        "max_budget_usd": float(budget_usd),
        "model": modele,
        "setting_sources": [],
        "verbatim_prompts": True,
        "system_prompt": CONSIGNES_SYSTEME[role],
        "sandbox": {"enabled": True, "autoAllowBashIfSandboxed": True, "allowUnsandboxedCommands": False,
                    "excludedCommands": [], "network": {"allowedDomains": [], "allowLocalBinding": False}},
        "env": variables_agent(url_relais),
        "crochets": {"PreToolUse": [{"matcher": None, "crochet": fabriquer_crochet(dossier)}]},
    }


def importer_sdk():
    try:
        import claude_agent_sdk as sdk
    except ImportError as erreur:
        raise MoteurIndisponible("le paquet claude_agent_sdk n'est pas installé : le moteur réel est indisponible "
                                 "ici (utiliser --moteur simule, ou l'installer sur l'instance de l'opérateur)") from erreur
    return sdk


class AdaptateurClaudeSDK(Adaptateur):
    """Moteur réel : `query()` du Claude Agent SDK, une session neuve par appel, dans le dossier de l'agent.

    Jamais exécuté dans ce dépôt (ni clé ni réseau) : seules `construire_options` et la garde des outils sont testées.
    """

    nom = "claude-sdk"

    def __init__(self, url_relais, environnement=None, arme=False):
        self.url_relais = valider_url_relais(url_relais)
        self._environnement = environnement
        self.arme = arme

    def lancer(self, role, consigne, dossier, budget_usd, max_tours, modele=None):
        environnement = os.environ if self._environnement is None else self._environnement
        presents = noms_de_cle_presents(environnement)
        if presents:
            raise CleDansEnvironnement("variables de clé présentes dans l'environnement de l'orchestrateur ("
                                       + ", ".join(presents) + ") : la clé doit rester dans le relais du noyau")
        if not self.arme:
            raise MoteurNonArme("moteur réel non armé : aucun agent réel n'est lancé (essais, simulation)")
        verifier_modele_reel(modele)
        sdk = importer_sdk()
        o = construire_options(os.path.abspath(dossier), budget_usd, max_tours, url_relais=self.url_relais,
                               modele=modele, role=role)
        options = sdk.ClaudeAgentOptions(
            cwd=o["cwd"], allowed_tools=o["allowed_tools"], disallowed_tools=o["disallowed_tools"],
            permission_mode=o["permission_mode"], max_turns=o["max_turns"], max_budget_usd=o["max_budget_usd"],
            model=o["model"], setting_sources=o["setting_sources"], verbatim_prompts=o["verbatim_prompts"],
            system_prompt=o["system_prompt"], sandbox=o["sandbox"], env=o["env"],
            hooks={"PreToolUse": [sdk.HookMatcher(matcher=c["matcher"], hooks=[c["crochet"]])
                                  for c in o["crochets"]["PreToolUse"]]},
        )
        texte, cout, statut, erreur = asyncio.run(self._executer(sdk, consigne, options))
        return Resultat(caviarder(texte)[0], lister_fichiers(dossier), cout, statut, erreur)

    @staticmethod
    async def _executer(sdk, consigne, options):
        morceaux, cout, statut, erreur, final = [], 0.0, "erreur", None, None
        sous_types = {"success": "ok", "error_max_budget_usd": "budget_depasse", "error_max_turns": "tours_epuises"}
        try:
            async for message in sdk.query(prompt=consigne, options=options):
                if isinstance(message, sdk.AssistantMessage):
                    morceaux.extend(b.text for b in message.content if isinstance(b, sdk.TextBlock))
                elif isinstance(message, sdk.ResultMessage):
                    cout = float(message.total_cost_usd or 0.0)
                    final = message.result
                    statut = sous_types.get(message.subtype, "erreur")
                    if message.is_error and statut == "ok":
                        statut = "erreur"
        except sdk.ClaudeSDKError as exc:
            erreur = type(exc).__name__ + " : " + caviarder(str(exc))[0][:500]
        return (final if final else "\n".join(morceaux)), cout, statut, erreur


def __getattr__(nom):
    if nom in ("AdaptateurSimule", "MondeSimule"):
        from . import simulation
        return getattr(simulation, nom)
    raise AttributeError(nom)
