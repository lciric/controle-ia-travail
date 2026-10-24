"""Le contrat entre le noyau et l'organisme : la seule chose que l'essaim reçoit, avec la mission et les tâches.

Le noyau ne donne ni organisation, ni règles, ni récompense, ni base de connaissances, ni boîte à outils : l'organisme
construit tout lui-même, y compris ses concepts et ses méthodes, et écrit son propre successeur. Le contrat ne fixe
que ce sans quoi rien ne peut être exécuté ni jugé : un point d'entrée, l'interface d'appel des espèces, les fichiers
que le noyau lit, le budget.
"""
from __future__ import annotations

import json
import pathlib
import re

ESPECES_DISPONIBLES = ["CLAUDE_FABLE_5_1", "CLAUDE_OPUS_5_5", "GEMINI_ARGON"]
EXTENSIONS_PERMISES = {".py", ".md", ".txt", ".json", ".jsonl", ".csv", ".yaml", ".yml", ".tex"}
TAILLE_MAX_OCTETS = 2_000_000
FICHIERS_MAX = 200
MOTIF_FICHIER = re.compile(r"<<<FICHIER (organisme/[A-Za-z0-9_./-]+)>>>\n(.*?)\n<<<FIN FICHIER>>>", re.S)

CONTRAT = """\
CONTRAT ENTRE LE NOYAU ET L'ORGANISME (version 1)

1. Forme. L'organisme est un dossier `organisme/` de fichiers texte (Python, Markdown, JSON…), au plus 200 fichiers
   et 2 Mo, avec un fichier `organisme/manifeste.json` : {"nom": "…", "version": "…", "entree": "module:fonction",
   "description": "…"}. `module` est un module Python de `organisme/` (par exemple "principal"), `fonction` une
   fonction `executer(contexte)` qu'il définit. Les chemins sont relatifs ; aucun lien symbolique ; aucun binaire.

2. Exécution. Le noyau lance `executer(contexte)` dans un bac à sable : sous-processus Python sans réseau, sans
   clé, sans accès hors de son dossier de travail, avec une limite de temps, de mémoire et de disque. `contexte`
   est un dictionnaire :
   - "generation" (entier), "lignee" (texte), "mission" (texte),
   - "dossier_travail" (chemin, le seul en écriture), "dossier_archive" (chemin en lecture seule : toutes les
     générations passées de toutes les lignées, avec leur code, leurs sorties, leur score),
   - "taches_entrainement" : liste de {"id", "famille", "texte", "etiquettes", "verite"},
   - "taches_test" : liste de {"id", "famille", "texte", "etiquettes"} (sans vérité),
   - "budget" : {"appels_max", "usd_max", "temps_max_s"} pour cette génération,
   - "historique" : liste de {"generation", "lignee", "score", "statut", "cout_usd", "n_appels"} pour cette lignée.

3. Appels aux espèces. Dans le bac à sable, le module `noyau_client` (fourni) expose :
   - `appeler(espece, prompt, max_tokens=None, role="")` → dict {"statut", "texte", "modele_servi", "fin", "usage",
     "cout_usd", "identifiant", "echec"} ; `statut` vaut "OK" quand `texte` est une réponse complète ; sinon
     ("VIDE", "TRONQUE", "REFUS", "ANOMALIE", "ECHEC_API", "MODELE_NON_CONFORME", "PLAFOND") `texte` est vide.
     Le noyau ne remplace jamais une espèce par une autre et ne renvoie jamais une erreur comme un texte.
   - `especes()` → liste des espèces disponibles ; `budget()` → {"appels_restants", "usd_restants"}.
   Chaque appel est journalisé par le noyau (modèle demandé et servi, raison d'arrêt, usage, coût, empreintes).

4. Sorties lues par le noyau, dans `dossier_travail` :
   - `reponses_test.json` : {"<id de tâche>": {"etiquette": "…", "confiance": 0.0}} pour les tâches de test ;
     une tâche sans réponse compte comme une erreur ;
   - `successeur/organisme/` : l'organisme complet de la génération suivante (même forme) ; s'il est absent, la
     lignée s'arrête ;
   - `metrique_proposee.json` (facultatif) : {"nom": "…", "definition": "…", "valeur": nombre, "justification": "…"} —
     la métrique que l'organisme propose pour juger un essaim, calculée par lui sur sa propre génération ; le noyau
     l'archive et la rapporte sans l'utiliser ;
   - `metrique/` (facultatif, pour la confrontation entre organismes) : `definition.md` (en français simple),
     `calculer.py` définissant `calculer(dossier_sorties) -> float` (du code objectif appliqué aux sorties d'un autre
     organisme, exécuté par le noyau dans un bac à sable, sans réseau ; jamais une auto-note), et `attaques.json`
     (tâches d'attaque : {"id", "famille", "texte", "etiquettes", "verite"}) que le noyau soumet à l'autre organisme
     en les faisant porter par des espèces d'une autre famille de fournisseur que la lignée du défendeur. Le noyau
     applique la métrique de A aux sorties de B et celle de B aux sorties de A ; l'humain gèle ces métriques par un
     préenregistrement avant la confrontation, et le score sur tâches cachées reste la mesure témoin ;
   - tout le reste (`CONCEPTION.md`, journaux, connaissances, tests…) est libre et archivé tel quel.

5. Jugement. Le noyau calcule le score externe sur les tâches de test (exactitude équilibrée par famille, puis
   moyenne), l'archive avec la génération, et le rend à la génération suivante dans `historique`. Il n'applique
   aucune règle de sélection : ce que l'organisme fait du score est à lui.

6. Fin. Le noyau s'arrête quand aucune lignée n'a de successeur, quand le nombre maximal de générations ou le
   budget total fixés par l'humain sont atteints, ou sur ordre de l'humain.
"""


def mission_texte(mission: str, familles: dict[str, tuple[str, str]]) -> str:
    fam = "\n".join(f"- {f} : étiquettes {list(e)}" for f, e in familles.items())
    return f"{mission.strip()}\n\nFamilles de tâches soumises au jugement externe :\n{fam}"


def prompt_amorcage(mission: str, familles: dict[str, tuple[str, str]], budget: dict, exemples: list[dict]) -> str:
    ex = "\n".join(f"- [{t['id']}] ({t['famille']}, vérité : {t['verite']}) {t['texte']}" for t in exemples[:6])
    return (
        "Tu écris la génération 0 d'un organisme : un essaim d'agents qui apprend seul son organisation, construit "
        "seul ses connaissances et devient plus compétent de génération en génération. Rien ne t'est imposé en dehors "
        "du contrat ci-dessous : ni rôles, ni règles d'apprentissage, ni signal de récompense, ni mémoire, ni boucles, "
        "ni concepts. Tu identifies toi-même les concepts mathématiques et les méthodes qui se rattachent à la "
        "question, et tu écris le code qui les met en œuvre, les teste, et réécrit le successeur. Le nombre d'agents "
        "à recruter (cellules, appels, mitose, castes) est à toi, dans la seule limite du budget ; de même le nombre "
        "d'essaims et leur composition — monocultures par famille de fournisseur, hybrides entre familles, ou les deux — "
        "et la façon dont ils se parlent.\n\n"
        f"MISSION (mots de l'humain) :\n{mission_texte(mission, familles)}\n\n"
        f"BUDGET PAR GÉNÉRATION : {budget['appels_max']} appels, {budget['usd_max']} USD, {budget['temps_max_s']} s.\n\n"
        f"ESPÈCES DISPONIBLES : {ESPECES_DISPONIBLES}.\n\n"
        f"EXEMPLES D'ENTRAÎNEMENT (la liste complète est dans `contexte['taches_entrainement']`) :\n{ex}\n\n"
        f"{CONTRAT}\n"
        "FORMAT DE RÉPONSE : chaque fichier entre les marqueurs suivants, chemin relatif commençant par `organisme/` :\n"
        "<<<FICHIER organisme/manifeste.json>>>\n{…}\n<<<FIN FICHIER>>>\n<<<FICHIER organisme/principal.py>>>\n…\n<<<FIN FICHIER>>>\n"
        "Inclus `organisme/CONCEPTION.md` : ta conception, en français, et ce que tu feras du score externe."
    )


CLIENT_SOURCE = '''"""noyau_client — fourni par le noyau dans le bac à sable ; seul accès aux espèces."""
import json, os, socket

_CHEMIN = os.environ["ESSAIM_SOCKET"]


def _echanger(requete):
    with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as s:
        s.connect(_CHEMIN)
        s.sendall((json.dumps(requete, ensure_ascii=False) + "\\n").encode("utf-8"))
        tampon = b""
        while not tampon.endswith(b"\\n"):
            morceau = s.recv(65536)
            if not morceau:
                break
            tampon += morceau
    return json.loads(tampon.decode("utf-8"))


def appeler(espece, prompt, max_tokens=None, role=""):
    return _echanger({"op": "appeler", "espece": espece, "prompt": prompt, "max_tokens": max_tokens, "role": role})


def especes():
    return _echanger({"op": "especes"})["especes"]


def budget():
    return _echanger({"op": "budget"})
'''


def extraire_fichiers(texte: str) -> dict[str, str]:
    """Fichiers `organisme/…` d'une réponse ; chemins validés ; dictionnaire chemin → contenu."""
    fichiers = {}
    for chemin, contenu in MOTIF_FICHIER.findall(texte or ""):
        p = pathlib.PurePosixPath(chemin)
        if ".." in p.parts or p.is_absolute() or p.suffix.lower() not in EXTENSIONS_PERMISES:
            continue
        fichiers[str(p)] = contenu
    return fichiers


def ecrire_organisme(fichiers: dict[str, str], racine: pathlib.Path) -> list[str]:
    """Écrit les fichiers sous `racine` (qui contiendra `organisme/`) ; rend les problèmes de validation."""
    for chemin, contenu in fichiers.items():
        cible = racine / chemin
        cible.parent.mkdir(parents=True, exist_ok=True)
        cible.write_text(contenu, encoding="utf-8")
    return valider_organisme(racine / "organisme")


def valider_organisme(dossier: pathlib.Path) -> list[str]:
    p: list[str] = []
    if not dossier.is_dir():
        return [f"dossier absent : {dossier}"]
    fichiers = [f for f in dossier.rglob("*") if f.is_file() or f.is_symlink()]
    if any(f.is_symlink() for f in fichiers):
        p.append("lien symbolique interdit")
    if len(fichiers) > FICHIERS_MAX:
        p.append(f"trop de fichiers : {len(fichiers)} > {FICHIERS_MAX}")
    taille = sum(f.stat().st_size for f in fichiers if f.is_file())
    if taille > TAILLE_MAX_OCTETS:
        p.append(f"trop volumineux : {taille} > {TAILLE_MAX_OCTETS} octets")
    for f in fichiers:
        if f.suffix.lower() not in EXTENSIONS_PERMISES:
            p.append(f"extension interdite : {f.relative_to(dossier)}")
    manifeste = dossier / "manifeste.json"
    if not manifeste.is_file():
        return p + ["manifeste.json absent"]
    try:
        m = json.loads(manifeste.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, UnicodeDecodeError) as e:
        return p + [f"manifeste.json illisible : {e}"]
    if not isinstance(m, dict) or not isinstance(m.get("entree"), str) or ":" not in m["entree"]:
        return p + ["manifeste.json : champ `entree` « module:fonction » absent"]
    module, fonction = m["entree"].split(":", 1)
    if not re.fullmatch(r"[A-Za-z_][A-Za-z0-9_.]*", module) or not re.fullmatch(r"[A-Za-z_][A-Za-z0-9_]*", fonction):
        p.append("manifeste.json : `entree` mal formée")
    elif not (dossier / (module.replace(".", "/") + ".py")).is_file():
        p.append(f"manifeste.json : module d'entrée introuvable : {module}")
    for py in dossier.rglob("*.py"):
        try:
            compile(py.read_text(encoding="utf-8"), str(py), "exec")
        except (SyntaxError, UnicodeDecodeError) as e:
            p.append(f"syntaxe : {py.relative_to(dossier)} : {str(e)[:120]}")
    return p
