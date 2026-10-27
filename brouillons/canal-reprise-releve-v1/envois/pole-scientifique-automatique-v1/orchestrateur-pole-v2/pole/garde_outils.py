"""Garde des outils des agents (crochet `PreToolUse` du Claude Agent SDK), logique pure et testable.

Refuse toute commande Bash qui sort du dossier de l'expérience, lit l'environnement, touche au réseau ou élève ses
droits ; refuse Read, Write, Edit (et Glob, Grep) hors du dossier ; refuse tout autre outil. C'est une **première
barrière** par motifs : une commande obscurcie (chemin encodé, interpréteur détourné) peut la franchir ; la barrière
réelle reste le bac à sable (réseau coupé, dossier seul accessible) et l'absence de clé dans l'environnement de l'agent.
"""

import os
import re
import shlex

from .outils import chemin_dans

COMMANDES_RESEAU = {
    "curl", "wget", "pip", "pip3", "pipx", "git", "ssh", "scp", "sftp", "rsync", "nc", "ncat", "netcat", "telnet",
    "ftp", "apt", "apt-get", "yum", "dnf", "brew", "conda", "mamba", "micromamba", "npm", "npx", "yarn", "pnpm",
    "uv", "gh", "socat", "aria2c", "http", "https", "nslookup", "dig", "ping", "docker",
}
MOTIFS_RESEAU = ("/dev/tcp", "/dev/udp", "urllib", "http.client", "import requests", "requests.get", "requests.post",
                 "socket", "httpx", "aiohttp", "ftplib", "smtplib", "telnetlib", "paramiko", "ensurepip", "-m pip")
COMMANDES_ENV = {"env", "printenv", "compgen"}
COMMANDES_ENV_SI_NUES = {"export", "declare", "typeset", "set", "readonly"}
COMMANDES_PRIVILEGE = {"sudo", "su", "doas", "pkexec"}
CHEMINS_SYSTEME_PERMIS = {"/dev/null", "/dev/stdout", "/dev/stderr", "/dev/zero"}
VARIABLE_SENSIBLE = re.compile(r"\$\{?!?[A-Za-z_]*(?:KEY|TOKEN|SECRET|PASS|AUTH|CRED|COOKIE|SESSION)[A-Za-z_0-9]*",
                               re.I)
SEPARATEURS = {";", "&&", "||", "|", "&", "(", ")", "|&", ";;", "\n"}
OUTILS_FICHIERS = {"Read": ("file_path",), "Write": ("file_path",), "Edit": ("file_path",),
                   "MultiEdit": ("file_path",), "Glob": ("path",), "Grep": ("path",)}


def _mots(commande):
    lexeur = shlex.shlex(commande, posix=True, punctuation_chars=";&|()<>")
    lexeur.whitespace_split = True
    lexeur.commenters = ""
    return list(lexeur)


def _commandes_simples(mots):
    courant = []
    for mot in mots:
        if mot in SEPARATEURS or set(mot) <= set(";&|()"):
            if courant:
                yield courant
            courant = []
        else:
            courant.append(mot)
    if courant:
        yield courant


def _premier_mot(simple):
    """(indice, nom) du premier mot qui n'est pas une affectation VAR=valeur."""
    for indice, mot in enumerate(simple):
        if re.match(r"^[A-Za-z_][A-Za-z_0-9]*=", mot):
            continue
        return indice, os.path.basename(mot)
    return len(simple), ""


def _chemins_hors_dossier(commande, mots, dossier):
    """Chemins absolus, personnels (~) ou remontants (..) qui sortent du dossier."""
    fautifs = []
    candidats = set(re.findall(r"(?:(?<=^)|(?<=[\s'\"=:(`,;|&<>]))(/[^\s'\"`;|&<>(),]*)", commande))
    for mot in mots:
        for morceau in re.split(r"[=:,]", mot):
            if morceau.startswith("/"):
                candidats.add(morceau)
    for chemin in sorted(candidats):
        if chemin in CHEMINS_SYSTEME_PERMIS or chemin_dans(dossier, chemin):
            continue
        fautifs.append(chemin)
    if re.search(r"(?:^|[\s'\"=:(`,;|&<>])~", commande):
        fautifs.append("~ (dossier personnel)")
    for morceau in re.findall(r"[^\s'\"`;|&<>()=:,]*\.\.[^\s'\"`;|&<>()=:,]*", commande):
        if not chemin_dans(dossier, morceau):
            fautifs.append(morceau)
    return fautifs


def evaluer_commande(commande, dossier):
    """(autorisée, motif) pour une commande Bash exécutée avec `dossier` pour répertoire courant."""
    if not isinstance(commande, str) or not commande.strip():
        return False, "commande vide ou illisible"
    try:
        mots = _mots(commande)
    except ValueError as erreur:
        return False, f"commande non analysable ({erreur})"
    if "environ" in commande or "getenv" in commande:
        return False, "lecture de l'environnement (environ, getenv) interdite"
    if VARIABLE_SENSIBLE.search(commande) or "${!" in commande:
        return False, "lecture d'une variable sensible de l'environnement interdite"
    for motif in MOTIFS_RESEAU:
        if motif in commande:
            return False, f"accès réseau interdit ({motif})"
    for simple in _commandes_simples(mots):
        indice, premier = _premier_mot(simple)
        arguments = simple[indice + 1:]
        noms = {os.path.basename(m) for m in simple}
        if (noms & {"sudo", "doas", "pkexec"}) or premier in COMMANDES_PRIVILEGE:
            return False, "élévation de droits interdite (sudo, su, doas, pkexec)"
        reseau = noms & {"curl", "wget", "pip", "pip3", "git"}
        if premier in COMMANDES_RESEAU or reseau:
            return False, f"accès réseau ou dépôt interdit ({premier if premier in COMMANDES_RESEAU else sorted(reseau)[0]})"
        if premier in COMMANDES_ENV:
            return False, f"lecture de l'environnement interdite ({premier})"
        if premier in COMMANDES_ENV_SI_NUES and (not arguments or any(a.startswith("-p") for a in arguments)):
            return False, f"lecture de l'environnement interdite ({premier} sans affectation)"
        if premier == "cd" and (not arguments or arguments[0] in ("-", "~")):
            return False, "cd vers le dossier personnel ou précédent interdit"
    fautifs = _chemins_hors_dossier(commande, mots, dossier)
    if fautifs:
        return False, "chemin hors du dossier de l'expérience : " + ", ".join(fautifs[:3])
    return True, "commande autorisée"


def evaluer_appel(outil, entree, dossier):
    """(autorisé, motif) pour un appel d'outil quelconque."""
    entree = entree or {}
    if outil == "Bash":
        return evaluer_commande(entree.get("command", ""), dossier)
    if outil in OUTILS_FICHIERS:
        for cle in OUTILS_FICHIERS[outil]:
            chemin = entree.get(cle)
            if chemin is None and outil in ("Glob", "Grep"):
                continue
            if not isinstance(chemin, str) or not chemin:
                return False, f"{outil} : chemin manquant"
            if not chemin_dans(dossier, chemin):
                return False, f"{outil} : chemin hors du dossier de l'expérience ({chemin})"
        if outil in ("Glob", "Grep") and ".." in str(entree.get("pattern", "")):
            return False, f"{outil} : motif remontant hors du dossier"
        return True, f"{outil} dans le dossier"
    return False, f"outil non autorisé pour un agent du pôle : {outil}"


def fabriquer_crochet(dossier):
    """Crochet `PreToolUse` au format du Claude Agent SDK : refuse avec un motif, sinon laisse le flux normal."""
    dossier = os.path.realpath(dossier)

    async def crochet(input_data, tool_use_id, context):
        autorise, motif = evaluer_appel(input_data.get("tool_name", ""), input_data.get("tool_input") or {}, dossier)
        if autorise:
            return {}
        return {"hookSpecificOutput": {"hookEventName": "PreToolUse", "permissionDecision": "deny",
                                       "permissionDecisionReason": motif}}

    crochet.dossier = dossier
    return crochet
