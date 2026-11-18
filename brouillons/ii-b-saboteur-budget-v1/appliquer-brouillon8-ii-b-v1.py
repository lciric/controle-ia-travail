"""Fabrique le brouillon 8 de l'ordre exploratoire du saboteur à budget (ii-b) — v1.

Usage (depuis la racine du dépôt) :
    python3 -I -B brouillons/ii-b-saboteur-budget-v1/appliquer-brouillon8-ii-b-v1.py

Ce que fait ce programme, et rien d'autre :
1. il vérifie l'empreinte du brouillon 7 de l'ordre ;
2. il lit dans `registres/decisions.md` (lecture seule) la ligne `R-3521`, présente une seule fois, et y
   prend l'extrait qui commence à « 7b » et finit à l'heure en Z ; il vérifie que cet extrait n'est porté
   que par cette ligne du registre et qu'il a la forme que l'ordre décrit au § 4 étape 4 ; l'extrait n'est
   écrit nulle part dans ce programme ;
3. il applique au brouillon 7 les couples « avant » / « après » écrits plus bas, dans l'ordre ; chaque
   « avant » doit être présent exactement une fois au moment de son application, sinon arrêt sans rien
   écrire ;
4. il contrôle : chaque « après » présent exactement une fois à la fin ; application inverse égale au
   brouillon 7 à l'octet ; l'extrait présent exactement deux fois (les deux places du marqueur rempli) ;
   13 marqueurs distincts `<<NOM>>` restants, celui de la ligne de création de 7b absent ; chaque hunk de
   `diff -u` rattaché à au moins un couple ; sinon arrêt sans rien écrire ;
5. il écrit `ordre-exploratoire-ii-b-v1-brouillon8.md`, puis joue `compter-marqueurs-ii-b-v1.py` sur ce
   fichier et écrit sa sortie dans `sortie-compter-marqueurs-ii-b-v3.txt`, puis écrit
   `differences-brouillon7-vers-8-v1.md` (chaque hunk rattaché à son changement, puis la sortie entière de
   `diff -u`).

Il n'écrase jamais (R12) : arrêt si l'un des trois fichiers de sortie existe ; création exclusive. Il
n'ouvre que le brouillon 7 de l'ordre, le registre des décisions, le programme de compte (qu'il lance) et
lui-même (pour son empreinte). Aucun repli silencieux (R5). Aucun sujet ni mécanisme n'y est écrit.
"""
from __future__ import annotations

import hashlib
import re
import subprocess
import sys
from collections import Counter
from pathlib import Path

DOSSIER = Path(__file__).resolve().parent
RACINE = DOSSIER.parent.parent
SOURCE = DOSSIER / "ordre-exploratoire-ii-b-v1-brouillon7.md"
EMPREINTE_SOURCE = "1ed0e736ed15f24e66a918815820ea73452a341c97004f6b21113eca22dd9766"
REGISTRE = RACINE / "registres/decisions.md"
COMPTEUR = DOSSIER / "compter-marqueurs-ii-b-v1.py"
SORTIE = DOSSIER / "ordre-exploratoire-ii-b-v1-brouillon8.md"
SORTIE_COMPTE = DOSSIER / "sortie-compter-marqueurs-ii-b-v3.txt"
NOTE = DOSSIER / "differences-brouillon7-vers-8-v1.md"

EMPREINTE_BROUILLON6 = "1f65acf781638bfa786c928a7927be8f730c646b55f3b7a3e3676c6d71277db0"
EMPREINTE_PROGRAMME7 = "4254df7bbd1fbb9150c4ed50d39f871bfd9f1cd8d879fbbd392ad43ca64f2735"
EMPREINTE_DIFFERENCES7 = "0616935bd82800b2d00e2ddf1a24bcb2383c8196e077682592a8d8a1eb175465"
RAPPORT_VERIFICATION = "docs/notes/barreau8-iib-v1/verification-ordre-et-devis-iib-brouillon6-v1.md"
EMPREINTE_RAPPORT_VERIFICATION = "bd7941ecec095fec470df9cb07e7ba488ac5a6a3060b7c6e5a115b3f435a9127"
NOTE_CHEMIN = "docs/notes/barreau8-iib-v1/chemin-critique-saboteurs-discrets-entretien-v1.md"
EMPREINTE_NOTE_CHEMIN = "398215789b8a81c2fc1a167344b2a57f4c77c0f82304d22fea18c5627bf8d6fa"

LIGNE_CONSTAT = "R-3521"
MARQUEUR_7B = "LIGNE_REGISTRE_CREATION_7B"
PLACE = "@@EXTRAIT_DE_LA_LIGNE_DE_CONSTAT@@"  # remplacé par l'extrait lu au registre
MARQUEURS_ATTENDUS = 13
OCCURRENCES_ATTENDUES = 31
MOTIF_MARQUEUR = re.compile(r"<<([A-Z0-9_]+)>>")
MOTIF_EXTRAIT = re.compile(r"7b[^\n]*?\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z")
MOTIF_FORME = re.compile(r"7b créée, instance \d+ à \d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z")
MOTIF_DU_CODE = re.compile(r"7b.*\binstance\s+\d+", re.I)  # motif que l'ordre cite au § 4 étape 4
MOTIF_HUNK = re.compile(r"^@@ -(\d+)(?:,(\d+))? \+(\d+)(?:,(\d+))? @@")

SANS_OBJET = "sans objet : 7b créée le 11 novembre (R-2369, R-2413 ; constat R-3521)"

CHANGEMENTS = {
    1: "titre, statut et section « Ce que le brouillon 8 change »",
    2: "couple du § 13 (`R-3523`)",
    3: "marqueur de la ligne de création de 7b rempli ; branche « 7b non créée » sans objet (`R-3521`)",
    4: "exclus du § 8 complétés",
    5: "comptes des marqueurs du § 11",
}

# Chaque couple : nom, numéro du changement, lieu, texte « avant », texte « après ».
COUPLES = [
    {
        "nom": "B8-1a", "changement": 1, "lieu": "titre",
        "avant": "# Ordre — saboteur à budget (ii-b), **course exploratoire**, instance à part — v1, brouillon 6\n",
        "apres": "# Ordre — saboteur à budget (ii-b), **course exploratoire**, instance à part — v1, brouillon 8\n",
    },
    {
        "nom": "B8-1b", "changement": 1, "lieu": "en-tête, statut",
        "avant": (
            "- **Statut** : **brouillon 6**, scellé comme brouillon, non contre-lu. Fabriqué par programme "
            "(`appliquer-brouillon6-ii-b-v1.py`, scellé dans ce dossier) depuis le brouillon 5 ("
        ),
        "apres": (
            "- **Statut** : **brouillon 8**, scellé comme brouillon, non contre-lu. Fabriqué par programme "
            "(`appliquer-brouillon8-ii-b-v1.py`, scellé dans ce dossier) depuis le brouillon 7 "
            f"(`{SOURCE.name}`, `{EMPREINTE_SOURCE}`, intact, R12), recopié à l'octet hors des changements listés "
            "dans `differences-brouillon7-vers-8-v1.md`. Écrit le 2026-11-18 vers 23:30 UTC (`date -u`) par un "
            "rédacteur neuf (sous-agent de la session mère `session_013QMayjsoZJFBUCqcnvD5h1`, modèle Claude "
            "Fable 5.2), qui n'a écrit ni la conception, ni le code, ni leurs contre-lectures, ni les brouillons "
            "1 à 7, qui n'a ouvert ni la consigne privée ni la conception, et qui n'a lu, pour ce brouillon, que "
            "le brouillon 7, sa note des différences, le programme du brouillon 7, le programme de compte des "
            "marqueurs et sa sortie précédente, les lignes `R-3310`, `R-3312`, `R-3509`, `R-3518` et `R-3520` à "
            f"`R-3523` du registre des décisions, et le point 2 du § 7 de la note du chemin critique "
            f"(`{NOTE_CHEMIN}`, `{EMPREINTE_NOTE_CHEMIN}`). Ce qu'il change est dit à la section « Ce que le "
            "brouillon 8 change ». Le brouillon 7 a été fabriqué par programme (`appliquer-brouillon7-ii-b-v1.py`, "
            f"`{EMPREINTE_PROGRAMME7}`, scellé dans ce dossier) depuis le brouillon 6 "
            f"(`ordre-exploratoire-ii-b-v1-brouillon6.md`, `{EMPREINTE_BROUILLON6}`, intact, R12), par un autre "
            "rédacteur neuf de la même session mère (même modèle ; registre des décisions, ligne `R-3520`) : il "
            "a appliqué les 14 couples de la vérification des brouillons 6 et rien d'autre "
            f"(`differences-brouillon6-vers-7-v1.md`, `{EMPREINTE_DIFFERENCES7}`) ; son titre et son statut "
            "étaient restés « brouillon 6 ». Le brouillon 6 a été fabriqué par programme "
            "(`appliquer-brouillon6-ii-b-v1.py`, scellé dans ce dossier) depuis le brouillon 5 ("
        ),
    },
    {
        "nom": "B8-1c", "changement": 1, "lieu": "section neuve, placée avant « Ce que le brouillon 6 change »",
        "avant": "## Ce que le brouillon 6 change (détail : `differences-brouillon5-vers-6-v1.md`)\n",
        "apres": (
            "## Ce que le brouillon 8 change (détail : `differences-brouillon7-vers-8-v1.md`), et ce que le "
            "brouillon 7 avait changé (détail : `differences-brouillon6-vers-7-v1.md`)\n"
            "\n"
            "- **Brouillon 7** : les 14 couples V-1 à V-14 de la vérification des brouillons 6 "
            f"(`{RAPPORT_VERIFICATION}` (`{EMPREINTE_RAPPORT_VERIFICATION}`) ; verdict : « après ces couples "
            "exacts » ; registre des décisions, ligne `R-3518`), appliqués mot pour mot par programme, et rien "
            "d'autre : un majeur (V-1, § 5 étape 5 : le remède au fichier manquant est de lire le disque sans "
            "démarrer l'instance), quatre couples qui portent la décision `R-3509` (V-2 à V-5 : phrase périmée "
            "sur CC-08 retirée, marqueur des tirages et permutations de la lecture (2) rempli, comptes du § 11), "
            "neuf mineurs (V-6 à V-14). Deux écarts y étaient restés, déclarés dans sa note des différences et "
            "en `R-3520` : titre et statut encore « brouillon 6 » ; sortie du compte des marqueurs citée, non "
            "écrite.\n"
            "- **En-tête** (brouillon 8) : titre et statut mis à jour ; cette section ajoutée.\n"
            "- **Couple du § 13** (`R-3523`), mot pour mot : les fichiers de la passe de recalcul ne sont pas lus "
            "avant le préenregistrement de la lecture des sondes, scellé à part et contre-lu, et le verdict "
            "scellé du témoin positif planté de la chaîne ; les mots « test de transfert » sont retirés.\n"
            f"- **Préalable de 7b** : le marqueur `{MARQUEUR_7B}` est rempli, à ses deux places (§ 1 ; § 4 "
            f"étape 4), par l'extrait que porte la ligne de constat `{LIGNE_CONSTAT}` du registre des décisions, "
            "lu par programme dans le registre et écrit nulle part ailleurs ; la branche « 7b non créée le 25 » "
            "est dite sans objet (§ 1 ; § 4 étape 1) ; le § 4 étape 4 nomme la ligne de constat ; le § 11 dit le "
            "marqueur rempli.\n"
            "- **Exclus de la lecture des sondes** (§ 8) : liste complétée, chaque ajout avec sa ligne source.\n"
            "- **Marqueurs** (§ 11) : 13 distincts restent dans ce texte (14 au brouillon 7) ; la sortie du "
            "programme de compte est écrite sous le nom que le brouillon 7 citait, "
            "`sortie-compter-marqueurs-ii-b-v3.txt`.\n"
            "\n"
            "## Ce que le brouillon 6 change (détail : `differences-brouillon5-vers-6-v1.md`)\n"
        ),
    },
    {
        "nom": "B8-3a", "changement": 3, "lieu": "§ 1, ligne « Préalable » : marqueur rempli, branche sans objet",
        "avant": (
            f"| Préalable | 7b créée : `<<{MARQUEUR_7B}>>` (forme : § 4 étape 4) ; si 7b n'est pas créée le 25 : "
            "la course ne part pas sous cette ligne ; on laisse passer le 27 et une ligne neuve sera à demander à "
            "Lazar (nœud 2 (a), `GO-2026-11-18-56`, point 3) |"
        ),
        "apres": (
            f"| Préalable | 7b créée : `{PLACE}` (forme : § 4 étape 4) ; branche « si 7b n'est pas créée le 25 » "
            f"(nœud 2 (a), `GO-2026-11-18-56`, point 3) : {SANS_OBJET} |"
        ),
    },
    {
        "nom": "B8-3b", "changement": 3, "lieu": "§ 4 étape 1, nœud 2 (a) : branche sans objet",
        "avant": (
            "**2 (a)** attendre 7b ; si elle n'est pas créée le 25, laisser passer le 27, une ligne neuve sera à "
            "demander ; **3 (a)**"
        ),
        "apres": (
            "**2 (a)** attendre 7b ; si elle n'est pas créée le 25, laisser passer le 27, une ligne neuve sera à "
            f"demander — {SANS_OBJET} ; **3 (a)**"
        ),
    },
    {
        "nom": "B8-3c", "changement": 3, "lieu": "§ 4 étape 4 : marqueur rempli",
        "avant": f"Forme de l'extrait cité (`<<{MARQUEUR_7B}>>`)",
        "apres": f"Forme de l'extrait cité (`{PLACE}`)",
    },
    {
        "nom": "B8-3d", "changement": 3, "lieu": "§ 4 étape 4 : la ligne de constat existe",
        "avant": "« instance <chiffres> » ; sinon, une ligne neuve de constat de cette forme. **Ne jamais",
        "apres": (
            "« instance <chiffres> » ; sinon, une ligne neuve de constat de cette forme. **Fait** : la ligne "
            f"neuve de constat est `{LIGNE_CONSTAT}` (7b créée le 11 novembre, `R-2369`, `R-2413`) ; elle seule "
            "porte l'extrait au registre. **Ne jamais"
        ),
    },
    {
        "nom": "B8-4", "changement": 4, "lieu": "§ 8, exclus de toute lecture des sondes",
        "avant": "et leur vérificateur (brouillons 6)**. Le § 2 porte des réglages",
        "apres": (
            "et leur vérificateur (brouillons 6)**. **Liste complétée au brouillon 8**, chaque ajout avec sa "
            f"ligne source (« note du chemin critique » : `{NOTE_CHEMIN}`, `{EMPREINTE_NOTE_CHEMIN}`, § 7 "
            "point 2 ; les autres références sont des lignes du registre des décisions) : le contrôleur des "
            "contrôles courts du code, déjà dit plus haut (note du chemin critique ; ses contrôles : `R-3485`, "
            "`R-3497`) ; les contre-lecteurs des brouillons 5 et 6 de cet ordre et du devis (note du chemin "
            "critique) ; le vérificateur des brouillons 6 (`R-3518` : exclu de tout rôle de lecteur des sondes "
            "du barreau 8 et de toute contre-lecture qui les touche) ; les développeurs du code, Opus 4.6 puis "
            "Fable (note du chemin critique) ; l'explorateur de l'état des barreaux 6, 7 et 8 (`R-3310`) ; "
            "l'auteur du code du bras A des organismes discrets (`R-3312`) ; le planificateur du chemin critique "
            "(`R-3520` : exclu du texte des sondes du barreau 8, de sa contre-lecture, de la lecture et du "
            "verdict) ; l'agent autorisé à ouvrir la conception qui a nommé le « test de transfert » (`R-3522`, "
            "point 3 ; `R-3523`) ; le vérificateur de la conception en cours, agent autorisé à l'ouvrir "
            "(`R-3523`, suite) ; le rédacteur du brouillon 7 (`R-3520`) et le rédacteur du brouillon 8 (mandat "
            "de la session mère, `R-3523`, suite), qui ont lu cet ordre. Le § 2 porte des réglages"
        ),
    },
    {
        "nom": "B8-3e", "changement": 3, "lieu": f"§ 11, ligne `{MARQUEUR_7B}`",
        "avant": f"| `{MARQUEUR_7B}` | en attente | création de 7b (§ 4 étape 4) |",
        "apres": (
            f"| `{MARQUEUR_7B}` | rempli | l'extrait que porte la ligne de constat `{LIGNE_CONSTAT}` du registre "
            "des décisions, écrit au § 1 et au § 4 étape 4 seulement ; 7b créée le 11 novembre (`R-2369`, "
            "`R-2413`) |"
        ),
    },
    {
        "nom": "B8-5a", "changement": 5, "lieu": "§ 11, comptes sur les 30",
        "avant": (
            "Comptes : sur les 30, **15 remplis, 13 en attente, 2 hors de ce texte** (au brouillon 5 : 14, 14, 2 ; "
            "`COMMIT_CODE_IIB` est rempli depuis)"
        ),
        "apres": (
            "Comptes : sur les 30, **16 remplis, 12 en attente, 2 hors de ce texte** (au brouillon 5 : 14, 14, 2 ; "
            f"`COMMIT_CODE_IIB` est rempli depuis ; au brouillon 7 : 15, 13, 2 ; `{MARQUEUR_7B}` est rempli "
            "depuis)"
        ),
    },
    {
        "nom": "B8-5b", "changement": 5, "lieu": "§ 11, marqueurs distincts restants",
        "avant": "**14 marqueurs distincts restent dans ce texte** = les 13 en attente des 30 + le propre en attente",
        "apres": "**13 marqueurs distincts restent dans ce texte** = les 12 en attente des 30 + le propre en attente",
    },
    {
        "nom": "B8-2", "changement": 2, "lieu": "§ 13, « Ce qu'elle rend »",
        "avant": (
            "fichiers scellés à part, non lus avant le préenregistrement de la lecture des sondes et le verdict du "
            "test de transfert."
        ),
        "apres": (
            "fichiers scellés à part, non lus avant le préenregistrement de la lecture des sondes, scellé à part "
            "et contre-lu, et le verdict scellé du témoin positif planté de la chaîne (P3-bis ; conception, § 1 "
            "et § 6.3 ; R-2044)."
        ),
    },
]


class Arret(Exception):
    """Arrêt."""


def empreinte(octets: bytes) -> str:
    return hashlib.sha256(octets).hexdigest()


def lire_verifie(chemin: Path, attendue: str) -> str:
    octets = chemin.read_bytes()
    if empreinte(octets) != attendue:
        raise Arret(f"empreinte inattendue pour {chemin.name} : {empreinte(octets)}")
    return octets.decode("utf-8")


def lire_extrait() -> str:
    """Extrait porté par la ligne de constat du registre des décisions, de « 7b » à l'heure en Z."""
    lignes = REGISTRE.read_bytes().decode("utf-8").split("\n")
    constats = [ligne for ligne in lignes if ligne.startswith(f"- {LIGNE_CONSTAT} ")]
    if len(constats) != 1:
        raise Arret(f"ligne {LIGNE_CONSTAT} trouvée {len(constats)} fois en tête de ligne au registre, une attendue")
    m = MOTIF_EXTRAIT.search(constats[0])
    if m is None:
        raise Arret(f"ligne {LIGNE_CONSTAT} : aucun extrait de « 7b » à une heure en Z")
    extrait = m.group(0)
    if MOTIF_FORME.fullmatch(extrait) is None:
        raise Arret(f"ligne {LIGNE_CONSTAT} : l'extrait n'a pas la forme dite au § 4 étape 4 de l'ordre")
    if MOTIF_DU_CODE.search(extrait) is None or "<<" in extrait or ">>" in extrait or extrait != extrait.strip():
        raise Arret(f"ligne {LIGNE_CONSTAT} : l'extrait ne satisfait pas ce que l'ordre dit que le code exige")
    porteuses = sum(1 for ligne in lignes if extrait in ligne)
    if porteuses != 1 or constats[0].count(extrait) != 1:
        raise Arret(f"l'extrait est porté par {porteuses} lignes du registre, une attendue")
    return extrait


def couples_remplis(extrait: str) -> list[dict]:
    couples = []
    for c in COUPLES:
        if PLACE in c["avant"]:
            raise Arret(f"{c['nom']} : la place de l'extrait est dans un texte « avant »")
        d = dict(c)
        d["apres"] = c["apres"].replace(PLACE, extrait)
        if not d["avant"] or d["avant"] == d["apres"]:
            raise Arret(f"{c['nom']} : couple vide ou sans changement")
        couples.append(d)
    if sum(c["apres"].count(extrait) for c in couples) != 2:
        raise Arret("l'extrait n'est pas écrit dans exactement deux textes « après »")
    return couples


def appliquer(texte: str, couples: list[dict]) -> str:
    for c in couples:
        n = texte.count(c["avant"])
        if n != 1:
            raise Arret(f"{c['nom']} : texte « avant » trouvé {n} fois, une attendue")
        texte = texte.replace(c["avant"], c["apres"])
    return texte


def controler(source: str, resultat: str, couples: list[dict], extrait: str) -> Counter:
    if extrait in source:
        raise Arret("l'extrait est déjà dans le brouillon 7")
    for c in couples:
        n = resultat.count(c["apres"])
        if n != 1:
            raise Arret(f"{c['nom']} : texte « après » trouvé {n} fois à la fin, une attendue")
    retour = resultat
    for c in reversed(couples):
        if retour.count(c["apres"]) != 1:
            raise Arret(f"{c['nom']} : application inverse impossible")
        retour = retour.replace(c["apres"], c["avant"])
    if retour != source:
        raise Arret("l'application inverse ne rend pas le brouillon 7 à l'octet")
    if resultat.count(extrait) != 2:
        raise Arret(f"l'extrait est écrit {resultat.count(extrait)} fois dans le brouillon 8, deux attendues")
    if PLACE in resultat:
        raise Arret("la place de l'extrait est restée dans le brouillon 8")
    marqueurs = Counter(MOTIF_MARQUEUR.findall(resultat))
    if MARQUEUR_7B in marqueurs:
        raise Arret(f"le marqueur {MARQUEUR_7B} reste dans le brouillon 8")
    if len(marqueurs) != MARQUEURS_ATTENDUS or sum(marqueurs.values()) != OCCURRENCES_ATTENDUES:
        raise Arret(f"marqueurs restants : {sum(marqueurs.values())} occurrences, {len(marqueurs)} distincts ; "
                    f"attendus : {OCCURRENCES_ATTENDUES}, {MARQUEURS_ATTENDUS}")
    return marqueurs


def ligne_de(texte: str, extrait: str) -> tuple[int, int]:
    """Première et dernière ligne (à partir de 1) qu'occupe l'extrait, présent une fois."""
    position = texte.index(extrait)
    premiere = texte.count("\n", 0, position) + 1
    return premiere, premiere + extrait.rstrip("\n").count("\n")


def sortie_diff(resultat: str) -> str:
    # `diff -u` compare le brouillon 7 sur disque au texte obtenu, passé par l'entrée standard.
    p = subprocess.run(
        ["diff", "-u", "--label", SOURCE.name, "--label", SORTIE.name, str(SOURCE), "-"],
        input=resultat.encode("utf-8"), capture_output=True, check=False,
    )
    if p.returncode != 1 or p.stderr:
        raise Arret(f"diff : code {p.returncode}, {p.stderr.decode('utf-8', 'replace')}")
    return p.stdout.decode("utf-8")


def decouper_hunks(diff: str) -> list[dict]:
    hunks: list[dict] = []
    for ligne in diff.splitlines():
        m = MOTIF_HUNK.match(ligne)
        if m:
            hunks.append({"entete": ligne, "lignes": [], "courante": int(m.group(3)), "ajoutees": []})
            continue
        if not hunks:
            continue
        h = hunks[-1]
        h["lignes"].append(ligne)
        if ligne.startswith("+"):
            h["ajoutees"].append(h["courante"])
            h["courante"] += 1
        elif ligne.startswith(" "):
            h["courante"] += 1
    return hunks


def rattacher(hunks: list[dict], resultat: str, couples: list[dict]) -> None:
    for h in hunks:
        h["couples"] = []
    for c in couples:
        premiere, derniere = ligne_de(resultat, c["apres"])
        touches = [h for h in hunks if any(premiere <= n <= derniere for n in h["ajoutees"])]
        if len(touches) != 1:
            raise Arret(f"{c['nom']} : rattaché à {len(touches)} hunks, un attendu")
        touches[0]["couples"].append(c)
        c["ligne"] = premiere
    for h in hunks:
        if not h["couples"]:
            raise Arret(f"hunk {h['entete']} : aucun couple, changement hors mandat")


def jouer_compteur() -> str:
    p = subprocess.run(
        [sys.executable, "-I", "-B", str(COMPTEUR), str(SORTIE)], capture_output=True, check=False,
    )
    if p.returncode != 0 or p.stderr:
        raise Arret(f"programme de compte : code {p.returncode}, {p.stderr.decode('utf-8', 'replace')}")
    return p.stdout.decode("utf-8")


def ecrire_note(resultat: str, couples: list[dict], marqueurs: Counter, diff: str, hunks: list[dict],
                compte: str) -> str:
    cloture = "~~~~"
    if cloture in diff or cloture in compte:
        raise Arret("la sortie de diff ou du compte contient la clôture de la note")
    t: list[str] = []
    t.append("# Différences du brouillon 7 au brouillon 8 de l'ordre exploratoire du saboteur à budget — v1\n")
    t.append("Note fabriquée par programme (`appliquer-brouillon8-ii-b-v1.py`, dans ce dossier), en même temps que le "
             "brouillon 8. Aucun sujet ni mécanisme n'y est écrit. Le devis reste au brouillon 6, intact.\n")
    t.append("## 1. Pièces\n")
    t.append(f"- Brouillon 7 de l'ordre (intact, R12) : `{SOURCE.name}`, `{EMPREINTE_SOURCE}`.")
    t.append(f"- Brouillon 8 de l'ordre : `{SORTIE.name}`, `{empreinte(resultat.encode('utf-8'))}`.")
    t.append(f"- Sortie du programme de compte des marqueurs : `{SORTIE_COMPTE.name}`, "
             f"`{empreinte(compte.encode('utf-8'))}` ; programme `{COMPTEUR.name}`, "
             f"`{empreinte(COMPTEUR.read_bytes())}`.")
    t.append(f"- Programme : `{Path(__file__).name}`, `{empreinte(Path(__file__).read_bytes())}`.")
    t.append(f"- Registre des décisions, lu seul, pour l'extrait de la ligne `{LIGNE_CONSTAT}` : "
             f"`{REGISTRE.relative_to(RACINE)}` (fichier vivant : empreinte non citée).")
    t.append(f"- Note du chemin critique, § 7 point 2 : `{NOTE_CHEMIN}`, `{EMPREINTE_NOTE_CHEMIN}`.")
    t.append("- Décisions qui commandent ce brouillon : registre des décisions, lignes `R-3520` (deux écarts du "
             "brouillon 7), `R-3521` (constat), `R-3523` (couple du § 13 et suite).\n")
    t.append("## 2. Ce qui est appliqué\n")
    t.append(f"{len(couples)} couples « avant » / « après », écrits dans le programme, appliqués dans l'ordre, pour "
             "cinq changements. Contrôles passés par programme : chaque « avant » présent exactement une fois au "
             "moment de son application ; chaque « après » présent exactement une fois à la fin ; application "
             "inverse égale au brouillon 7 à l'octet ; chaque hunk de `diff -u` rattaché à au moins un couple, "
             "chaque couple à un seul hunk. Rien d'autre n'est changé.\n")
    for numero, nom in CHANGEMENTS.items():
        t.append(f"- Changement {numero} : {nom}.")
    t.append("")
    t.append("| couple | changement | lieu | ligne du brouillon 8 | hunk |")
    t.append("|---|---|---|---|---|")
    for c in couples:
        rang = next(i for i, h in enumerate(hunks, 1) if c in h["couples"])
        t.append(f"| {c['nom']} | {c['changement']} | {c['lieu']} | {c['ligne']} | {rang} |")
    t.append("")
    t.append("### Extrait du constat de 7b\n")
    t.append(f"Lu par programme dans la ligne `{LIGNE_CONSTAT}` du registre des décisions (présente une fois en tête "
             "de ligne) : de « 7b » à l'heure en Z. Vérifié : forme dite au § 4 étape 4 de l'ordre ; motif que "
             "l'ordre dit exigé par le code ; aucune autre ligne du registre ne le porte ; il est écrit deux fois "
             "dans le brouillon 8, aux deux places du marqueur (couples B8-3a et B8-3c), et dans aucune autre "
             "phrase. Il n'est écrit ni dans le programme ni dans cette note, hors des sorties de `diff` ci-dessous, "
             "qui recopient les lignes changées.\n")
    t.append("### Phrases corrigées au changement 3 (7b n'est plus à créer)\n")
    for c in couples:
        if c["changement"] == 3:
            t.append(f"- {c['nom']}, ligne {c['ligne']} du brouillon 8 : {c['lieu']}.")
    t.append("- Laissées telles quelles, parce qu'elles ne disent pas que 7b reste à créer : la garde « 7b "
             "d'abord » du § 3 ; la ligne `prealables` de la table du § 2 ; le titre « 7b créée » du § 4 étape 4 ; "
             "la forme et l'artefact de la ligne (§ 3, § 4 étapes 2 et 4) ; les résumés des brouillons 5 et 6.\n")
    t.append("### Exclus ajoutés au § 8 et leur source (changement 4)\n")
    t.append("| ajout | source |")
    t.append("|---|---|")
    for ajout, source in (
        ("contrôleur des contrôles courts du code (déjà dans la liste ; source ajoutée)",
         "note du chemin critique, § 7 point 2 ; `R-3485`, `R-3497`"),
        ("contre-lecteurs des brouillons 5 et 6", "note du chemin critique, § 7 point 2"),
        ("vérificateur des brouillons 6 (déjà dans la liste ; source ajoutée)", "`R-3518`"),
        ("développeurs du code (Opus 4.6, puis Fable)", "note du chemin critique, § 7 point 2"),
        ("explorateur de l'état des barreaux 6, 7 et 8", "`R-3310`"),
        ("auteur du code du bras A", "`R-3312`"),
        ("planificateur du chemin critique", "`R-3520`"),
        ("agent qui a nommé le « test de transfert »", "`R-3522`, point 3 ; `R-3523`"),
        ("vérificateur de la conception en cours", "`R-3523`, suite"),
        ("rédacteur du brouillon 7", "`R-3520`"),
        ("rédacteur du brouillon 8", "mandat de la session mère ; `R-3523`, suite"),
    ):
        t.append(f"| {ajout} | {source} |")
    t.append("")
    t.append("## 3. Marqueurs restants\n")
    t.append(f"Compté par ce programme, par le seul motif des marqueurs (`<<[A-Z0-9_]+>>`) : "
             f"**{sum(marqueurs.values())} occurrences, {len(marqueurs)} marqueurs distincts** dans le brouillon 8 "
             f"(brouillon 7 : 33 occurrences, 14 distincts ; `{MARQUEUR_7B}`, deux occurrences, est rempli).\n")
    t.append("| marqueur restant | occurrences |")
    t.append("|---|---|")
    for nom in sorted(marqueurs):
        t.append(f"| `{nom}` | {marqueurs[nom]} |")
    t.append("")
    t.append(f"Sortie de `{COMPTEUR.name}` jouée sur le brouillon 8, écrite dans `{SORTIE_COMPTE.name}` :\n")
    t.append(f"{cloture}text")
    t.append(compte.rstrip("\n"))
    t.append(f"{cloture}\n")
    t.append("## 4. Écarts déclarés\n")
    t.append("- **Suite du statut.** Après le couple B8-1b, la suite de la ligne « Statut » (« Écrit le 2026-11-18 "
             "vers 22:55 UTC […] ») décrit le rédacteur du brouillon 6, comme avant ; elle est recopiée à l'octet.")
    t.append("- **Résumé du brouillon 6 laissé.** La section « Ce que le brouillon 6 change » dit encore « 15 "
             "distincts restent dans ce texte » : c'est le compte du brouillon 6, non touché.")
    t.append("- **Sources des exclus.** Le contre-lecteur du brouillon 5 et les développeurs du code n'ont pour "
             "source, parmi les pièces du mandat, que la note du chemin critique. Les lignes `R-3509` à `R-3523` ne "
             "nomment aucun contre-lecteur du brouillon 6 distinct de son vérificateur : l'ajout suit la lettre de "
             "la note. Le rédacteur du brouillon 8 n'a pas encore de ligne propre au registre.")
    t.append("- **Comptes du § 11.** « 16 remplis, 12 en attente » est obtenu en déplaçant un marqueur de la "
             "colonne « en attente » à la colonne « rempli » ; la table n'est pas recomptée ligne à ligne.\n")
    t.append("## 5. Chaque hunk, rattaché à son ou ses changements\n")
    for i, h in enumerate(hunks, 1):
        numeros = sorted({c["changement"] for c in h["couples"]})
        t.append(f"### Hunk {i} — changement{'s' if len(numeros) > 1 else ''} "
                 f"{', '.join(str(n) for n in numeros)}\n")
        for c in h["couples"]:
            t.append(f"- {c['nom']} (changement {c['changement']} : {CHANGEMENTS[c['changement']]}) : {c['lieu']}")
        t.append("")
        t.append(f"{cloture}diff")
        t.append(h["entete"])
        t.extend(h["lignes"])
        t.append(f"{cloture}\n")
    t.append("## 6. Sortie entière de `diff -u`\n")
    t.append(f"Commande : `diff -u {SOURCE.name} {SORTIE.name}` (étiquettes des deux fichiers sans date).\n")
    t.append(f"{cloture}diff")
    t.append(diff.rstrip("\n"))
    t.append(f"{cloture}")
    return "\n".join(t) + "\n"


def creer(chemin: Path, octets: bytes) -> None:
    with open(chemin, "xb") as f:  # création exclusive : n'écrase jamais
        f.write(octets)


def main() -> int:
    try:
        for chemin in (SORTIE, SORTIE_COMPTE, NOTE):
            if chemin.exists():
                raise Arret(f"{chemin.name} existe déjà : on n'écrase jamais (R12)")
        source = lire_verifie(SOURCE, EMPREINTE_SOURCE)
        extrait = lire_extrait()
        couples = couples_remplis(extrait)
        resultat = appliquer(source, couples)
        marqueurs = controler(source, resultat, couples, extrait)
        diff = sortie_diff(resultat)
        hunks = decouper_hunks(diff)
        rattacher(hunks, resultat, couples)
    except Arret as arret:
        print(f"ARRÊT, rien n'est écrit : {arret}", file=sys.stderr)
        return 1
    creer(SORTIE, resultat.encode("utf-8"))
    try:
        compte = jouer_compteur()
        attendu = f"{SORTIE.name}  {empreinte(resultat.encode('utf-8'))}\n" \
                  f"  occurrences {sum(marqueurs.values())} ; distincts {len(marqueurs)}\n"
        if not compte.startswith(attendu):
            raise Arret("la sortie du programme de compte ne s'accorde pas avec le compte de ce programme")
        note = ecrire_note(resultat, couples, marqueurs, diff, hunks, compte)
    except Arret as arret:
        print(f"ARRÊT après l'écriture du seul {SORTIE.name} : {arret}", file=sys.stderr)
        return 1
    creer(SORTIE_COMPTE, compte.encode("utf-8"))
    creer(NOTE, note.encode("utf-8"))
    for chemin in (SORTIE, SORTIE_COMPTE, NOTE):
        print(f"{chemin.name}  {empreinte(chemin.read_bytes())}")
    print(f"couples appliqués : {len(couples)} ; hunks : {len(hunks)}")
    print(compte, end="")
    return 0


if __name__ == "__main__":
    sys.exit(main())
