"""Fabrique le brouillon 11 de l'ordre exploratoire du saboteur à budget (ii-b) — v1. EXPLORATOIRE, NON OPPOSABLE (R-522).

Usage (depuis la racine du dépôt) :
    python3 -I -B brouillons/ii-b-saboteur-budget-v1/appliquer-brouillon11-ii-b-v1.py [--a-blanc DOSSIER_EXISTANT]

Il vérifie l'empreinte du brouillon 10 et celle de la vérification courte qui fonde la correction, relit par `git show`
le lanceur au commit de lancement (empreinte, puis les lignes qui fondent chaque citation de dossier changée ou gardée),
applique au brouillon 10, dans l'ordre, les couples « avant » / « après » écrits plus bas (chaque « avant » présent
exactement une fois au moment de son application ; chaque « après » présent exactement une fois à la fin ; application
inverse égale au brouillon 10 à l'octet ; chaque bloc de `diff -u` rattaché à un couple), contrôle qu'aucun marqueur
entre chevrons doubles n'y reste et que les citations du dossier des contrôles sont celles attendues (une pour le
dossier de l'étape 1, trois pour le dossier du rejeu, dans les commandes), écrit le brouillon 11, joue le programme de
compte, écrit sa sortie et la note des différences. Il n'écrase jamais (R12). Il n'ouvre que le brouillon 10, la
vérification courte du brouillon 10, le lanceur au commit de lancement, le programme de compte et lui-même. Aucun texte
de consigne ni fragment n'y est écrit. Il n'applique qu'un défaut : celui du point 3 de la vérification courte du
brouillon 10, avec le nom de dossier décidé par la session mère dans son message au rédacteur.
"""
from __future__ import annotations

import hashlib
import re
import subprocess
import sys
from pathlib import Path

DOSSIER = Path(__file__).resolve().parent
RACINE = DOSSIER.parent.parent
DEST = Path(sys.argv[2]).resolve() if len(sys.argv) == 3 and sys.argv[1] == "--a-blanc" else DOSSIER
SOURCE = DOSSIER / "ordre-exploratoire-ii-b-v1-brouillon10.md"
EMPREINTE_SOURCE = "a52cb18534ebd635343e262d4ebc56b06619f35b2c4c1643204c74e02387d4ca"
SORTIE = DEST / "ordre-exploratoire-ii-b-v1-brouillon11.md"
COMPTEUR = DOSSIER / "compter-marqueurs-ii-b-v1.py"
SORTIE_COMPTE = DEST / "sortie-compter-marqueurs-ii-b-v6.txt"
SORTIE_COMPTE_PRECEDENTE = DOSSIER / "sortie-compter-marqueurs-ii-b-v5.txt"
NOTE = DEST / "differences-brouillon10-vers-11-v1.md"
VERIF10 = "docs/notes/barreau8-iib-v1/verification-courte-ordre-iib-brouillon10-v1.md"
EMPREINTE_VERIF10 = "cf9c0d4c883f507f48b8ff847bec9fa2ab2457b8480c0185d27367dc93327207"
COMMIT = "836c7cccda5071fe54ecb148d214d74b5cb90474"  # commit de lancement
LANCEUR = "scripts/lancer_iib_v1.sh"
EMPREINTE_LANCEUR = "3279e3dcc631519e574c2011f9f143d956d3b668c729a176cd8efc0e99dece8f"
CONFIG = "docs/notes/barreau8-iib-v1/config-iib-reel-v1.json"
HEURE = "08:26"
ETAPE1 = '"$W/iib"'
REJEU = '"$W/iib-rejeu"'
COMMANDE_REJEU = '"${ENVI[@]}" bash scripts/lancer_iib_v1.sh controles-explo ' + REJEU + " " + COMMIT + " " + CONFIG
MOTIF_MARQUEUR = re.compile(r"<<([A-Z0-9_]+)>>")
MOTIF_BLOC = re.compile(r"^@@ -(\d+)(?:,(\d+))? \+(\d+)(?:,(\d+))? @@")
MOTIF_DOSSIER = re.compile(r'"\$W/iib(-rejeu)?"')

# Lignes du lanceur au commit de lancement qui fondent les citations ; (numéro, fragment qui doit s'y trouver, ce que la ligne fait).
LIGNES_LANCEUR = [
    (76, '[ -e "$D" ] && { echo "$D existe déjà (R12)"; exit 2; }', "`controles-explo` refuse un dossier qui existe déjà, code 2"),
    (126, '>> "$D/lancement.txt"', "`controles-explo` écrit `lancement.txt` dans le dossier qu'on lui passe"),
    (129, 'D=$(realpath -m "${5:?dossier des contrôles}")', "`creation` prend le dossier des contrôles pour cinquième argument"),
    (133, '[ -f "$D/lancement.txt" ] && grep -q \'^controles-explo \' "$D/lancement.txt" && [ -f "$D/config.json" ]', "`creation` exige le `lancement.txt` et la configuration de ce dossier"),
    (134, 'S=$(champ commit "$D/lancement.txt")', "`creation` lit le commit dans ce `lancement.txt`"),
    (170, '"$(champ amorce "$D/lancement.txt")"', "`creation` compare l'amorce à l'empreinte relevée par les contrôles de ce dossier"),
    (173, 'TA="$(champ tests_attendus "$D/lancement.txt")"', "`creation` lit le nombre d'essais attendu dans ce `lancement.txt`"),
    (174, 'apres-creation \\"$D/creation-brute.json\\" \\$? \\"$D\\"', "la commande imprimée par `creation` appelle `apres-creation` avec ce même dossier, écrit par le lanceur"),
    (180, '>> "$D/lancement.txt"', "`creation` écrit l'offre, les prix, l'échéance et le plafond dans ce `lancement.txt`"),
    (191, 'printf \'instance %s\\ncreation %s\\n\' "$ID" "$CR" >> "$D/lancement.txt"', "`apres-creation` écrit l'identifiant de l'instance et l'heure de création dans ce `lancement.txt`"),
    (192, 'surveillance $ID $D"', "`apres-creation` imprime la commande de surveillance avec ce dossier"),
    (197, 'creation auto $(champ carte "$D/lancement.txt") $(champ anterieure "$D/lancement.txt") $D $(champ echeance "$D/lancement.txt")', "au code 5, `apres-creation` imprime la commande du rang suivant avec ce dossier"),
    (204, '[ -f "$D/lancement.txt" ] || { echo "dossier sans lancement.txt"; exit 2; }', "`surveillance` exige un `lancement.txt` dans le dossier qu'on lui passe"),
    (205, '[ "$(champ instance "$D/lancement.txt")" = "$ID" ]', "`surveillance` refuse un identifiant qui n'est pas celui que porte ce `lancement.txt`"),
    (206, 'CR=$(champ creation "$D/lancement.txt"); PC=$(champ prix_carte "$D/lancement.txt")', "`surveillance` lit la création et les prix dans ce `lancement.txt`"),
    (237, 'stop instance $ID"', "à l'arrêt, `surveillance` imprime une commande d'arrêt par le seul identifiant, sans dossier"),
    (238, 'stop instance $ID"', "à la fin, `surveillance` imprime une commande d'arrêt par le seul identifiant, sans dossier"),
]

CHANGEMENTS = {
    0: "titre, statut, section « Ce que le brouillon 11 change »",
    1: "couple 1 de la vérification courte : commande exacte du rejeu des contrôles, dans le dossier neuf " + "`" + REJEU + "`" + " (§ 5 étape 2)",
    2: "couple 2 de la vérification courte : `creation` cite le dossier du rejeu (§ 5 étape 2)",
    3: "couple 3 de la vérification courte : `surveillance` cite le dossier du rejeu (§ 5 étape 3)",
}

SECTION = (
    "## Ce que le brouillon 11 change (détail : `differences-brouillon10-vers-11-v1.md`)\n"
    "\n"
    "Un seul défaut, celui que relève la vérification courte du brouillon 10 (`" + VERIF10 + "`, `" + EMPREINTE_VERIF10 + "`, point 3 ; verdict : un défaut, six points conformes, scellable après trois couples) ; le nom du dossier est décidé par la session mère (message au rédacteur) ; rien d'autre ne change.\n"
    "\n"
    "- **Le défaut** : à l'étape 2 du § 5, l'exécutante rejoue les contrôles du lanceur dans un dossier neuf, mais les commandes `creation` et `surveillance` citaient encore le dossier de l'étape 1. Le lanceur refuse un dossier qui existe déjà pour `controles-explo` (`scripts/lancer_iib_v1.sh` au commit de lancement, l. 76), et `creation` lit le `lancement.txt` et la configuration du dossier qu'on lui passe (l. 133-134) : les contrôles rejoués n'auraient pas été lus.\n"
    "- **§ 5 étape 2** : le dossier du rejeu s'appelle `" + REJEU + "` ; la commande exacte du rejeu est écrite, avec son issue attendue (code 0, « CONTRÔLES CONFORMES … ») et l'arrêt sur tout autre code ; `creation` cite ce dossier.\n"
    "- **§ 5 étape 3** : `surveillance` cite ce dossier : elle lit dans son `lancement.txt` l'identifiant de l'instance, l'heure de création, les prix et le plafond, que `creation` et `apres-creation` y écrivent (lanceur, l. 180, 191 et 204-208).\n"
    "- **Citation gardée** : celle de l'étape 1 du § 5, où `controles-explo` crée le dossier `" + ETAPE1 + "`. Aucune autre commande des § 5 à 7 ne cite le dossier des contrôles : `apres-creation`, la commande du rang suivant (code 5) et les commandes d'arrêt sont imprimées par le lanceur, avec le dossier passé à `creation` ou avec le seul identifiant de l'instance (l. 174, 192, 197, 237 et 238) ; le rapatriement ne lit que `\"$W/depot\"`.\n"
    "- **En-tête** : titre et statut mis à jour ; cette section ajoutée. Le § 11 n'est pas touché : il nomme encore la sortie du compte des marqueurs du brouillon 10 et la sortie du programme de comparaison, jouées sur le brouillon 10 ; le compte rejoué sur ce brouillon est `sortie-compter-marqueurs-ii-b-v6.txt` (0 occurrence), citée dans la note des différences ; le programme de comparaison n'est pas rejoué par le rédacteur.\n"
    "\n"
)

COUPLES = [
    {"nom": "B11-0a", "c": 0, "lieu": "titre",
     "avant": "instance à part — v1, brouillon 10\n", "apres": "instance à part — v1, brouillon 11\n"},
    {"nom": "B11-0b", "c": 0, "lieu": "en-tête, statut",
     "avant": "- **Statut** : **brouillon 10**, candidat au scellement, scellé comme brouillon, non contre-lu. Fabriqué par programme (`appliquer-brouillon10-ii-b-v1.py`, scellé dans ce dossier) depuis le brouillon 9 (",
     "apres": "- **Statut** : **brouillon 11**, candidat au scellement, scellé comme brouillon, non contre-lu. Fabriqué par programme (`appliquer-brouillon11-ii-b-v1.py`, scellé dans ce dossier) depuis le brouillon 10 (`ordre-exploratoire-ii-b-v1-brouillon10.md`, `" + EMPREINTE_SOURCE + "`, intact, R12), recopié à l'octet hors des changements listés dans `differences-brouillon10-vers-11-v1.md`. Écrit le 2026-11-19 vers " + HEURE + " UTC (`date -u`) par un rédacteur neuf (sous-agent de la session mère `session_013QMayjsoZJFBUCqcnvD5h1`, modèle Claude Fable 5.2), **qui travaille du côté du saboteur à budget et est donc exclu de tout rôle côté sondes du barreau 8** (rédaction, contre-lecture, lecture, verdict ; § 8). Il n'a écrit ni la conception, ni le code, ni la configuration, ni leurs contre-lectures, ni les brouillons 1 à 10 ; il n'a ouvert ni la consigne privée, ni la conception, ni le texte de lecture des sondes, ni l'enveloppe de la huitième tâche ; il n'a lu aucun résultat. Il applique le seul défaut que relève la vérification courte du brouillon 10 (`" + VERIF10 + "`, `" + EMPREINTE_VERIF10 + "`, vérifiée, lue en entier ; verdict : un défaut, six points conformes, scellable après trois couples), avec le nom de dossier décidé par la session mère (message au rédacteur), et rien d'autre. Il n'a lu, pour ce brouillon, que : le brouillon 10 en entier ; cette vérification courte ; le lanceur `scripts/lancer_iib_v1.sh` au commit de lancement, en entier (`" + EMPREINTE_LANCEUR + "`, recalculée) ; pour la forme, le programme du brouillon 10, le début de sa note des différences, le programme de compte des marqueurs et sa sortie. Ce qu'il change est dit à la section « Ce que le brouillon 11 change ». Le brouillon 10 a été fabriqué par programme (`appliquer-brouillon10-ii-b-v1.py`, scellé dans ce dossier) depuis le brouillon 9 ("},
    {"nom": "B11-0c", "c": 0, "lieu": "section neuve, placée avant « Ce que le brouillon 10 change »",
     "avant": "## Ce que le brouillon 10 change (détail : `differences-brouillon9-vers-10-v1.md`)\n",
     "apres": SECTION + "## Ce que le brouillon 10 change (détail : `differences-brouillon9-vers-10-v1.md`)\n"},
    {"nom": "B11-1", "c": 1, "lieu": "§ 5 étape 2 : commande exacte du rejeu, dossier neuf",
     "avant": "(dit par la mère, `R-3655`). Puis : `",
     "apres": "(dit par la mère, `R-3655`). Commande exacte du rejeu, dans le dossier neuf `" + REJEU + "` (le lanceur refuse un dossier qui existe déjà, et celui de l'étape 1 existe) : `" + COMMANDE_REJEU + "` → code 0, « CONTRÔLES CONFORMES … » ; tout autre code → arrêt. Puis : `"},
    {"nom": "B11-2", "c": 2, "lieu": "§ 5 étape 2 : dossier cité par `creation`",
     "avant": "creation auto course 0 " + ETAPE1 + " 1795816800`", "apres": "creation auto course 0 " + REJEU + " 1795816800`"},
    {"nom": "B11-3", "c": 3, "lieu": "§ 5 étape 3 : dossier cité par `surveillance`",
     "avant": "surveillance <ID> " + ETAPE1 + "`", "apres": "surveillance <ID> " + REJEU + "`"},
]

# Citations attendues du dossier des contrôles dans le brouillon 11 : (fragment de la ligne, dossier, sort, raison).
CITATIONS = [
    ("lancer_iib_v1.sh controles-explo " + ETAPE1 + " " + COMMIT, ETAPE1, "gardée",
     "§ 5 étape 1 : `controles-explo` crée ce dossier-là et y écrit `lancement.txt` (lanceur, l. 76 et 126) ; rien n'y renvoie après le rejeu"),
    ("lancer_iib_v1.sh controles-explo " + REJEU + " " + COMMIT, REJEU, "neuve",
     "§ 5 étape 2 : commande exacte du rejeu ; le lanceur refuse un dossier qui existe déjà (l. 76), d'où un nom neuf"),
    ("lancer_iib_v1.sh creation auto course 0 " + REJEU + " 1795816800", REJEU, "changée",
     "§ 5 étape 2 : `creation` lit `lancement.txt` et `config.json` du dossier qu'on lui passe (l. 129, 133-134, 170, 173) et y écrit l'offre, les prix, l'échéance et le plafond (l. 180)"),
    ("lancer_iib_v1.sh surveillance <ID> " + REJEU, REJEU, "changée",
     "§ 5 étape 3 : `surveillance` lit dans `lancement.txt` l'identifiant et l'heure de création, écrits par `apres-creation` (l. 191) dans le dossier passé à `creation` (l. 174), et refuse tout autre identifiant (l. 204-208)"),
]


class Arret(Exception):
    pass


def h(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def creer(p: Path, b: bytes) -> None:
    with open(p, "xb") as f:
        f.write(b)


def main() -> int:
    try:
        for p in (SORTIE, SORTIE_COMPTE, NOTE):
            if p.exists():
                raise Arret(f"{p.name} existe déjà (R12)")
        if "@" in HEURE:
            raise Arret("heure d'écriture non renseignée")
        brut = SOURCE.read_bytes()
        if h(brut) != EMPREINTE_SOURCE:
            raise Arret("empreinte du brouillon 10")
        if (RACINE / (VERIF10 + ".sha256")).read_text().split()[0] != EMPREINTE_VERIF10 or h((RACINE / VERIF10).read_bytes()) != EMPREINTE_VERIF10:
            raise Arret("empreinte de la vérification courte du brouillon 10")
        lanceur = subprocess.run(["git", "-C", str(RACINE), "show", f"{COMMIT}:{LANCEUR}"], capture_output=True, check=True).stdout
        if h(lanceur) != EMPREINTE_LANCEUR:
            raise Arret("empreinte du lanceur au commit de lancement")
        ll = lanceur.decode("utf-8").split("\n")
        for num, fragment, _ in LIGNES_LANCEUR:
            if fragment not in ll[num - 1]:
                raise Arret(f"lanceur, ligne {num} : fragment attendu absent")
        source = brut.decode("utf-8")
        if EMPREINTE_LANCEUR not in source:
            raise Arret("le brouillon 10 ne cite pas cette empreinte du lanceur")
        t = source
        for c in COUPLES:
            if t.count(c["avant"]) != 1:
                raise Arret(f"{c['nom']} : « avant » présent {t.count(c['avant'])} fois")
            t = t.replace(c["avant"], c["apres"])
        retour = t
        for c in reversed(COUPLES):
            if retour.count(c["apres"]) != 1:
                raise Arret(f"{c['nom']} : « après » présent {retour.count(c['apres'])} fois")
            retour = retour.replace(c["apres"], c["avant"])
        if retour != source:
            raise Arret("application inverse ≠ brouillon 10")
        if MOTIF_MARQUEUR.search(t):
            raise Arret("marqueur restant")
        lt = t.split("\n")
        citations = []
        for fragment, dossier, sort, raison in CITATIONS:
            ou = [k for k, l in enumerate(lt, 1) if fragment in l]
            if t.count(fragment) != 1 or len(ou) != 1:
                raise Arret(f"citation attendue présente {t.count(fragment)} fois : {fragment}")
            citations.append((ou[0], dossier, sort, raison, fragment))
        # Toute occurrence du dossier dans une commande du lanceur doit être l'une des quatre attendues.
        dans_commandes = len(re.findall(r'lancer_iib_v1\.sh (?:controles-explo|creation auto course 0|surveillance <ID>) "\$W/iib(?:-rejeu)?"', t))
        if dans_commandes != len(CITATIONS):
            raise Arret(f"{dans_commandes} commandes du lanceur citent un dossier des contrôles ({len(CITATIONS)} attendues)")
        occurrences = [(k, m.group(0)) for k, l in enumerate(lt, 1) for m in MOTIF_DOSSIER.finditer(l)]
        occ_source = [(k, m.group(0)) for k, l in enumerate(source.split("\n"), 1) for m in MOTIF_DOSSIER.finditer(l)]
        d = subprocess.run(["diff", "-u", "--label", SOURCE.name, "--label", SORTIE.name, str(SOURCE), "-"],
                           input=t.encode(), capture_output=True)
        if d.returncode != 1:
            raise Arret("diff")
        blocs = []
        for l in d.stdout.decode().split("\n")[2:]:
            m = MOTIF_BLOC.match(l)
            if m:
                deb = int(m.group(3)); lon = int(m.group(4)) if m.group(4) is not None else 1
                blocs.append({"e": l, "deb": deb, "fin": deb + lon - 1, "l": [], "c": []})
            elif blocs:
                blocs[-1]["l"].append(l)
        if blocs[-1]["l"] and blocs[-1]["l"][-1] == "":
            blocs[-1]["l"].pop()
        couples = [dict(c) for c in COUPLES]
        for c in couples:
            pos = t.index(c["apres"]); c["ligne"] = t.count("\n", 0, pos) + 1
            der = c["ligne"] + c["apres"].rstrip("\n").count("\n")
            dans = [n for n, b in enumerate(blocs, 1) if not (der < b["deb"] or c["ligne"] > b["fin"])]
            if len(dans) != 1:
                raise Arret(f"{c['nom']} rattaché à {len(dans)} blocs")
            c["bloc"] = dans[0]; blocs[dans[0] - 1]["c"].append(c["nom"])
        if any(not b["c"] for b in blocs):
            raise Arret("bloc de diff sans couple")
        precedente = SORTIE_COMPTE_PRECEDENTE.read_text(encoding="utf-8")
    except (Arret, OSError, subprocess.CalledProcessError) as a:
        print(f"ARRÊT, rien n'est écrit : {a}", file=sys.stderr)
        return 1
    creer(SORTIE, t.encode())
    r = subprocess.run([sys.executable, "-I", "-B", str(COMPTEUR), str(SORTIE)], capture_output=True, cwd=str(DOSSIER))
    code1, compte = r.returncode, r.stdout.decode() + r.stderr.decode()
    creer(SORTIE_COMPTE, compte.encode())
    # Même chose que la sortie précédente, aux noms de fichiers près : toutes les lignes après la première sont égales.
    meme = compte.split("\n")[1:] == precedente.split("\n")[1:] and compte.split("\n")[0] == f"{SORTIE.name}  {h(t.encode())}"
    if code1 != 0 or "occurrences 0 ; distincts 0" not in compte or not meme:
        print(f"ARRÊT après écriture : compte code {code1}, égal à la sortie précédente hors première ligne : {meme}", file=sys.stderr)
        return 1
    ret = sum(1 for b in blocs for l in b["l"] if l.startswith("-")); aj = sum(1 for b in blocs for l in b["l"] if l.startswith("+"))
    n = ["# Différences du brouillon 10 au brouillon 11 de l'ordre exploratoire du saboteur à budget — v1\n",
         "Note fabriquée par programme (`appliquer-brouillon11-ii-b-v1.py`, dans ce dossier), en même temps que le brouillon 11. EXPLORATOIRE, NON OPPOSABLE (R-522). Aucun sujet, aucun mécanisme, aucun texte de consigne ni fragment n'y est écrit. Le rédacteur, neuf, travaille du côté du saboteur à budget : il est exclu de tout rôle côté sondes du barreau 8. Le changement applique un seul défaut, celui du point 3 de la vérification courte du brouillon 10, avec le nom de dossier décidé par la session mère (message au rédacteur) : `" + REJEU + "` ; rien d'autre ne change.\n",
         "## 1. Pièces\n",
         f"- Brouillon 10 (intact, R12) : `{SOURCE.name}`, `{EMPREINTE_SOURCE}`.",
         f"- Brouillon 11 : `{SORTIE.name}`, `{h(t.encode())}`.",
         f"- Programme : `{Path(__file__).name}`, `{h(Path(__file__).read_bytes())}`.",
         f"- Programme de compte : `{COMPTEUR.name}`, `{h(COMPTEUR.read_bytes())}` ; sortie `{SORTIE_COMPTE.name}`, `{h(compte.encode())}` ; égale à la sortie précédente (`{SORTIE_COMPTE_PRECEDENTE.name}`, `{h(precedente.encode())}`) hors de sa première ligne, qui porte le nom et l'empreinte du fichier compté.",
         f"- Vérification courte du brouillon 10, lue en entier, empreinte recalculée et égale à son compagnon : `{VERIF10}`, `{EMPREINTE_VERIF10}`.",
         f"- Lanceur, lu en entier par `git show {COMMIT}:{LANCEUR}` (commit de lancement), empreinte recalculée, égale à celle que le brouillon 10 cite : `{EMPREINTE_LANCEUR}`.",
         "- Le programme de comparaison des marqueurs à la configuration (v2) n'est pas rejoué : hors de la tâche reçue (§ 5, point 2).\n",
         "## 2. Ce qui est appliqué\n",
         f"{len(couples)} couples, appliqués dans l'ordre. Lignes du brouillon 10 retirées ou réécrites : **{ret}** ; lignes du brouillon 11 neuves ou réécrites : **{aj}** ; {source.count(chr(10))} lignes deviennent {t.count(chr(10))}. `diff -u` rend {len(blocs)} blocs. Contrôles passés : chaque « avant » présent une fois à son application, chaque « après » une fois à la fin, application inverse égale au brouillon 10 à l'octet, aucun marqueur entre chevrons doubles, quatre commandes du lanceur citent un dossier des contrôles et ce sont les quatre attendues, chaque bloc rattaché à un couple.\n"]
    n += [f"- Changement {k} : {q}." for k, q in CHANGEMENTS.items()]
    n += ["", "| couple | changement | lieu | ligne du brouillon 11 | bloc |", "|---|---|---|---|---|"]
    n += [f"| {c['nom']} | {c['c']} | {c['lieu']} | {c['ligne']} | {c['bloc']} |" for c in couples]
    n += ["", "## 3. Citations du dossier des contrôles, une par une\n",
          "Dans les commandes du lanceur (§ 5), au brouillon 11 :\n",
          "| ligne du brouillon 11 | dossier cité | sort | raison, prise du lanceur au commit de lancement |", "|---|---|---|---|"]
    n += [f"| {k} | `{dossier}` | {sort} | {raison} |" for k, dossier, sort, raison, _ in sorted(citations)]
    n += ["", f"Toutes les occurrences du motif du dossier, commandes ou prose : au brouillon 10, {len(occ_source)} (" + ", ".join(f"l. {k} `{e}`" for k, e in occ_source) + f") ; au brouillon 11, {len(occurrences)} (" + ", ".join(f"l. {k} `{e}`" for k, e in occurrences) + "). Celles qui ne sont pas dans une commande sont dans la section « Ce que le brouillon 11 change » et dans la phrase qui introduit la commande du rejeu.\n",
          "Commandes des § 5 à 7 qui dépendent du dossier passé à `creation` sans le citer dans l'ordre (rien à changer) :\n",
          "- `apres-creation` : appelée par la commande que `creation` imprime, avec le dossier passé à `creation`, écrit par le lanceur (l. 174) ; elle y écrit l'identifiant et l'heure de création (l. 191) ;",
          "- la commande de surveillance imprimée par `apres-creation` porte ce même dossier (l. 192) : elle est égale à celle de l'étape 3, à `\"${ENVI[@]}\"` et `INTERVALLE=60` près ;",
          "- la commande du rang suivant, au code 5 (§ 5 étape 2, « Fenêtre »), est imprimée par `apres-creation` avec ce même dossier (l. 197) ;",
          "- les commandes d'arrêt imprimées par la surveillance (§ 5 étapes 4 et 5) ne portent que l'identifiant de l'instance (l. 237 et 238) ;",
          "- le rapatriement (§ 5 étape 5), la destruction (étape 6) et le § 7 ne citent que `\"$W/depot\"`, la branche du run et l'identifiant : aucun ne lit le dossier des contrôles.\n",
          "Lignes du lanceur relues par le programme (numéro, fragment présent, ce que la ligne fait) :\n",
          "| ligne du lanceur | ce qu'elle fait |", "|---|---|"]
    n += [f"| {num} | {quoi} |" for num, _, quoi in LIGNES_LANCEUR]
    n += ["", "## 4. Écarts aux couples proposés par la vérification courte\n",
          "1. Nom du dossier : la vérification propose `\"$W/iib-creation\"`, « ou le chemin choisi pour le rejeu » ; la session mère a choisi `" + REJEU + "`.",
          "2. Couple 1 : la vérification demande de nommer le dossier neuf dans la commande de `controles-explo` ; la session mère demande la commande exacte, son issue attendue et l'arrêt sur tout autre code. La phrase du brouillon 10 (« étape 1, dossier neuf, variables de cet ordre ») est gardée telle ; la commande est ajoutée après elle.\n",
          "## 5. Relevé sans être corrigé (hors de la tâche reçue : un défaut et rien d'autre)\n",
          "1. **Rejeu et fenêtre de création** : l'étape 2 dit de rejouer les contrôles « juste avant de créer », et sa ligne « Fenêtre » fait rejouer `creation` toutes les 15 minutes au code 3. Le rejeu ne peut se jouer qu'une fois : à la seconde, le dossier `" + REJEU + "` existe et le lanceur rend le code 2 (l. 76), ce que la phrase neuve lit comme un arrêt. Les essais suivants de `creation` doivent garder le même dossier : il porte le compte des essais et les machines refusées (l. 151-153, 180, 196). Le texte ne dit pas « une seule fois, avant la première commande `creation` » : à trancher par la mère.",
          "2. **§ 11** : il cite encore `sortie-compter-marqueurs-ii-b-v5.txt` et la sortie du programme de comparaison, jouées sur le brouillon 10. Le compte est rejoué ici (`sortie-compter-marqueurs-ii-b-v6.txt`) ; le programme de comparaison ne l'est pas : le rédacteur ne l'a pas ouvert et ne sait pas quels fichiers il lit. Le § 5 n'y perd aucun des fragments que le brouillon 10 portait, sauf le dossier des deux commandes changées : si le programme de comparaison cherche ces deux commandes avec leur dossier, il rendra un écart sur le brouillon 11 ; à rejouer par la mère ou par un lecteur qui peut l'ouvrir.",
          "3. **§ 4 étape 6, dernière phrase** : elle dit « À l'étape 1 du § 5, l'exécutante rejoue les contrôles dans un dossier neuf […] et c'est ce dossier neuf que lit la création » ; le rejeu est désormais écrit à l'étape 2, sous un nom propre. La phrase reste vraie pour le dossier que lit la création ; son renvoi à l'étape 1 est laissé tel.",
          "4. **§ 8** : le rédacteur du brouillon 11 n'est pas ajouté à la liste des exclus de toute lecture des sondes ; son exclusion est dite à la ligne « Statut ». La mère l'inscrit au registre « qui a lu quoi ».",
          "5. **Statut** : « non contre-lu » est gardé pour le brouillon 11 lui-même ; le brouillon 10 a eu sa vérification courte, le brouillon 11 n'en a pas encore.",
          "6. Aucune ligne du registre des décisions n'est citée pour ce brouillon : le rédacteur n'en a reçu aucune ; la décision de la mère est citée comme « message au rédacteur ».",
          "7. Le redémarrage du conteneur de l'exécutante (§ 5 étape 2) reste écrit sur la parole de la mère, comme au brouillon 10.\n",
          "## 6. Sortie du programme de compte\n", "~~~~", compte.rstrip("\n"), "~~~~\n",
          "## 7. Changements, bloc par bloc, tirés de `diff -u`\n"]
    for k, b in enumerate(blocs, 1):
        n += [f"### Bloc {k} — lignes {b['deb']} à {b['fin']} du brouillon 11 — couples {', '.join(b['c'])}\n", "~~~~diff", b["e"], *b["l"], "~~~~\n"]
    creer(NOTE, "\n".join(n).encode())
    for p in (SORTIE, SORTIE_COMPTE, NOTE):
        print(f"{p.name}  {h(p.read_bytes())}")
    print(f"couples {len(couples)} ; blocs {len(blocs)} ; retirées {ret} ; neuves {aj}")
    for k, dossier, sort, raison, _ in sorted(citations):
        print(f"citation, ligne {k} : {dossier} ({sort})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
