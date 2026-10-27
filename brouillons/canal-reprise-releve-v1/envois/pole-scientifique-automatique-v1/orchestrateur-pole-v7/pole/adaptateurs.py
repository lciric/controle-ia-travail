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


class BacASableInactif(RuntimeError):
    """Moteur réel sans bac à sable actif : refusé avant tout appel (v7, version 5, défaut 7 du premier lancement réel :
    en (a), les agents tournaient sans bac à sable, sous root ; un agent pouvait en principe lire l'environnement d'un
    autre processus du même utilisateur, donc la clé du relais)."""


def etat_bac_a_sable(chercher=None, executer=None):
    """(actif, motif) : `bwrap` et `socat` présents, et `bwrap` s'exécute avec le réseau isolé (espaces de noms permis).
    `chercher` et `executer` sont injectables pour les essais (défaut : shutil.which, subprocess.run)."""
    import shutil
    import subprocess
    chercher = chercher or shutil.which
    executer = executer or subprocess.run
    manquants = [nom for nom in ("bwrap", "socat") if chercher(nom) is None]
    if manquants:
        return False, ("dépendances du bac à sable absentes : " + ", ".join(manquants)
                       + " (par exemple `apt install bubblewrap socat`)")
    try:
        r = executer([chercher("bwrap"), "--ro-bind", "/", "/", "--dev", "/dev", "--unshare-net", "true"],
                     capture_output=True, timeout=30)
    except (OSError, subprocess.SubprocessError) as erreur:
        return False, f"bwrap ne s'exécute pas ({type(erreur).__name__})"
    if r.returncode != 0:
        return False, (f"bwrap ne s'exécute pas dans ce conteneur (code {r.returncode}) : espaces de noms interdits ? "
                       "(essai : bwrap --ro-bind / / --dev /dev --unshare-net true)")
    return True, "bwrap et socat présents ; bwrap s'exécute, réseau isolé"


def exiger_bac_a_sable(sdk=None, accepter_sans=False, motif_sans="", etat=None, euid=None):
    """État du bac à sable consigné au manifeste ; lève BacASableInactif s'il est inactif, sauf (i) faux moteur de la
    répétition générale (aucun agent réel, aucune clé), ou (ii) acceptation explicite, motif écrit, **hors de root**."""
    if sdk is not None and getattr(sdk, "EST_FAUX_SDK", False):
        return {"actif": False, "motif": "faux moteur de la répétition générale : aucun agent réel, aucune clé"}
    actif, motif = (etat or etat_bac_a_sable)()
    if actif:
        return {"actif": True, "motif": motif}
    if not accepter_sans:
        raise BacASableInactif("moteur réel refusé : bac à sable inactif — " + motif + " ; sans bac à sable, un agent "
                               "peut lire l'environnement d'un autre processus du même utilisateur (la clé du relais)")
    if not (motif_sans or "").strip():
        raise BacASableInactif("--accepter-sans-bac-a-sable exige --motif-sans-bac-a-sable (une raison écrite)")
    if (euid or os.geteuid)() == 0:
        raise BacASableInactif("sans bac à sable, l'orchestrateur et ses agents ne tournent jamais sous root "
                               "(utilisateur 0) : lancer sous un autre utilisateur que celui du relais")
    return {"actif": False, "motif": motif, "accepte_sans_bac_a_sable": motif_sans.strip()}


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


class AdaptateurMixte(Adaptateur):
    """v7, version 9 : de vrais agents pour certains rôles seulement (le proposeur d'un duel, par exemple), la simulation
    pour les autres. Sur un monde tenu par le noyau (banque, monde caché), l'expérimentateur et le vérificateur ne font que
    ranger des issues déposées : les simuler ne change pas le verdict du juge, seulement le coût (environ 0,55 USD par fiche
    en (a) et (a) bis). Le bac à sable reste exigé pour la partie réelle."""

    nom = "mixte"

    def __init__(self, reel, simule, roles_reels):
        roles = frozenset(roles_reels or ())
        if not roles or not roles <= set(ROLES):
            raise ValueError(f"rôles réels : une partie non vide de {ROLES} (reçu {sorted(roles)})")
        self.reel, self.simule, self.roles_reels = reel, simule, roles
        self.bac_a_sable = getattr(reel, "bac_a_sable", None)

    def lancer(self, role, consigne, dossier, budget_usd, max_tours, modele=None):
        cible = self.reel if role in self.roles_reels else self.simule
        return cible.lancer(role, consigne, dossier, budget_usd, max_tours, modele=modele)


def __getattr__(nom):
    if nom in ("AdaptateurSimule", "MondeSimule"):
        from . import simulation
        return getattr(simulation, nom)
    raise AttributeError(nom)
