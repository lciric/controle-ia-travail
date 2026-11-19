"""Fabrique le brouillon 12 de l'ordre exploratoire du saboteur à budget (ii-b) — v1. EXPLORATOIRE, NON OPPOSABLE (R-522).

Usage (depuis la racine du dépôt) :
    python3 -I -B brouillons/ii-b-saboteur-budget-v1/appliquer-brouillon12-ii-b-v1.py [--a-blanc DOSSIER_EXISTANT]

Il vérifie l'empreinte du brouillon 11, celle du programme de comparaison (v2, inchangé) et celle du lanceur au commit
de lancement, lu par `git show`, dont il relit les lignes qui fondent les phrases neuves ; il applique au brouillon 11,
dans l'ordre, les couples « avant » / « après » écrits plus bas (chaque « avant » présent exactement une fois au moment
de son application ; chaque « après » présent exactement une fois à la fin ; application inverse égale au brouillon 11
à l'octet ; chaque bloc de `diff -u` rattaché à un couple), contrôle qu'aucun marqueur entre chevrons doubles n'y reste
et que les quatre commandes du lanceur qui citent un dossier des contrôles sont inchangées, écrit le brouillon 12, joue
le programme de compte et la v2 du programme de comparaison (code 0 et « BILAN : écarts 0 » attendus), écrit leurs
sorties sous des noms neufs et la note des différences. Il n'écrase jamais (R12). Il n'ouvre que le brouillon 11, le
lanceur au commit de lancement, les deux programmes qu'il lance, leurs sorties précédentes et lui-même ; le programme de
comparaison lit, lui, l'ordre et la configuration du commit de lancement par `git show`. Aucun texte de consigne ni
fragment n'y est écrit. Il applique les trois décisions de la session mère sur les points relevés avec le brouillon 11
(message au rédacteur ; routine, consignée par elle à la ligne R-3678 du registre des décisions, non lue par le rédacteur).
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
SOURCE = DOSSIER / "ordre-exploratoire-ii-b-v1-brouillon11.md"
EMPREINTE_SOURCE = "e4c0ca6247c491504106e389de56481c25ea21900219a54c19bc164584072293"
SORTIE = DEST / "ordre-exploratoire-ii-b-v1-brouillon12.md"
COMPTEUR = DOSSIER / "compter-marqueurs-ii-b-v1.py"
COMPARATEUR = DOSSIER / "comparer-marqueurs-ordre-configuration-ii-b-v2.py"
EMPREINTE_COMPARATEUR = "e805a9c87ae8b21c5e416c6c6171b9e73b1b36025aca6e7d8a6c39ed5283f851"
NOM_COMPTE = "sortie-compter-marqueurs-ii-b-v7.txt"
NOM_COMPARAISON = "sortie-comparer-marqueurs-ordre-configuration-ii-b-v3.txt"
SORTIE_COMPTE = DEST / NOM_COMPTE
SORTIE_COMPARAISON = DEST / NOM_COMPARAISON
COMPTE_PRECEDENT = DOSSIER / "sortie-compter-marqueurs-ii-b-v6.txt"
COMPARAISON_PRECEDENTE = DOSSIER / "sortie-comparer-marqueurs-ordre-configuration-ii-b-v2.txt"
NOTE = DEST / "differences-brouillon11-vers-12-v1.md"
COMMIT = "836c7cccda5071fe54ecb148d214d74b5cb90474"  # commit de lancement
LANCEUR = "scripts/lancer_iib_v1.sh"
EMPREINTE_LANCEUR = "3279e3dcc631519e574c2011f9f143d956d3b668c729a176cd8efc0e99dece8f"
HEURE = "08:29"
REJEU = '"$W/iib-rejeu"'
MOTIF_MARQUEUR = re.compile(r"<<([A-Z0-9_]+)>>")
MOTIF_BLOC = re.compile(r"^@@ -(\d+)(?:,(\d+))? \+(\d+)(?:,(\d+))? @@")
MOTIF_COMMANDE = re.compile(r'lancer_iib_v1\.sh (?:controles-explo|creation auto course 0|surveillance <ID>) "\$W/iib(?:-rejeu)?"')

# Lignes du lanceur au commit de lancement qui fondent les phrases neuves ; (numéro, fragment qui doit s'y trouver, ce que la ligne fait).
LIGNES_LANCEUR = [
    (76, '[ -e "$D" ] && { echo "$D existe déjà (R12)"; exit 2; }', "`controles-explo` refuse un dossier qui existe déjà, code 2 : un second rejeu dans le même dossier ne peut pas passer"),
    (86, 'mkdir -p "$D"', "`controles-explo` crée le dossier avant la suite de ses contrôles : un rejeu arrêté en chemin laisse un dossier sans `lancement.txt`"),
    (126, '>> "$D/lancement.txt"', "`controles-explo` n'écrit `lancement.txt` qu'à la fin, tous contrôles passés"),
    (133, '[ -f "$D/lancement.txt" ] && grep -q \'^controles-explo \' "$D/lancement.txt" && [ -f "$D/config.json" ]', "`creation` refuse, code 2, un dossier sans `lancement.txt` de contrôles conformes"),
    (139, 'go "$REG" "$GOC" "$PLC" "$ANT")', "chaque `creation` relit la ligne d'accord au jour de la création"),
    (143, 'creation-7b "$REGDEC" "$D/config.json")', "chaque `creation` relit la ligne de création de 7b"),
    (144, 'calendrier "$D/config.json" "$REG" "$GOC" "$PGL")', "chaque `creation` rejoue le calendrier au jour de la création"),
    (151, 'ESSAIS=$(grep -c \'^essai_creation \' "$D/lancement.txt" || true)', "`creation` compte ses essais dans le `lancement.txt` du dossier : les reprises doivent garder ce dossier"),
    (153, 'EXCL=$(sed -n \'s/^machine_refusee //p\' "$D/lancement.txt"', "`creation` lit les machines refusées dans ce même `lancement.txt`"),
    (170, '"$(champ amorce "$D/lancement.txt")"', "chaque `creation` compare l'amorce à l'empreinte relevée par les contrôles du dossier"),
    (180, '"$((ESSAIS + 1))"', "`creation` écrit le rang de l'essai dans ce `lancement.txt`"),
    (196, 'printf \'machine_refusee %s\\n\'', "au code 5, `apres-creation` écrit la machine refusée dans ce `lancement.txt`"),
    (197, 'creation auto $(champ carte "$D/lancement.txt") $(champ anterieure "$D/lancement.txt") $D $(champ echeance "$D/lancement.txt")', "au code 5, la commande du rang suivant est imprimée avec ce même dossier"),
]

CHANGEMENTS = {
    0: "titre, statut, section « Ce que le brouillon 12 change »",
    1: "décision 1 : le rejeu se joue une seule fois, avant la première commande `creation` ; les reprises gardent le dossier du rejeu ; un dossier déjà là n'est pas un arrêt (§ 5 étape 2)",
    2: "décision 2 : la dernière phrase de l'étape 6 du § 4 situe le rejeu à l'étape 2 du § 5, dans le dossier du rejeu",
    3: "décision 3 : le § 11 cite les deux sorties neuves, jouées sur le brouillon 12",
}

PHRASES_REJEU = (
    "Ce rejeu se joue une seule fois, avant la première commande `creation` : toutes les reprises de `creation` (code 3, toutes les 15 minutes) et la commande du rang suivant (code 5) gardent `" + REJEU + "` et ne rejouent pas les contrôles. "
    "Si le dossier `" + REJEU + "` existe déjà quand l'exécutante va lancer le rejeu, ce n'est pas un arrêt : elle n'en fait pas un second et passe à la création. "
)

SECTION = (
    "## Ce que le brouillon 12 change (détail : `differences-brouillon11-vers-12-v1.md`)\n"
    "\n"
    "Trois décisions de la session mère sur les points relevés avec le brouillon 11 (message au rédacteur ; routine, registre des décisions, ligne `R-3678`, écrite par la mère, non lue par le rédacteur) ; rien d'autre ne change.\n"
    "\n"
    "- **§ 5 étape 2, le rejeu ne se joue qu'une fois** : avant la première commande `creation` ; les reprises de `creation` et la commande du rang suivant gardent le dossier du rejeu sans rejouer les contrôles ; un dossier du rejeu déjà là n'est pas un arrêt. Raison prise du lanceur au commit de lancement : il refuse un dossier qui existe déjà (l. 76), et `creation` tient dans le `lancement.txt` de ce dossier le compte de ses essais et les machines refusées (l. 151-153, 180, 196-197).\n"
    "- **§ 4 étape 6, dernière phrase** : elle situe désormais le rejeu à l'étape 2 du § 5, dans le dossier du rejeu ; elle le situait à l'étape 1.\n"
    "- **§ 11** : il cite les deux sorties jouées sur ce brouillon, `" + NOM_COMPTE + "` (compte des marqueurs : 0 occurrence) et `" + NOM_COMPARAISON + "` (programme de comparaison, v2, inchangé : code 0, aucun écart). Le programme de comparaison ne cherche au § 5 aucun fragment qui nomme le dossier du rejeu : il y cherche la commande des contrôles de l'étape 1, présente une fois ; aucune version neuve de ce programme n'a donc été faite. Les trois commandes qui citent le dossier du rejeu sont contrôlées par le programme qui fabrique ce brouillon.\n"
    "- **En-tête** : titre et statut mis à jour ; cette section ajoutée. La section « Ce que le brouillon 11 change » garde son texte d'alors : elle dit encore le § 11 non touché et le programme de comparaison non rejoué, ce qui était vrai du brouillon 11.\n"
    "\n"
)

COUPLES = [
    {"nom": "B12-0a", "c": 0, "lieu": "titre",
     "avant": "instance à part — v1, brouillon 11\n", "apres": "instance à part — v1, brouillon 12\n"},
    {"nom": "B12-0b", "c": 0, "lieu": "en-tête, statut",
     "avant": "- **Statut** : **brouillon 11**, candidat au scellement, scellé comme brouillon, non contre-lu. Fabriqué par programme (`appliquer-brouillon11-ii-b-v1.py`, scellé dans ce dossier) depuis le brouillon 10 (",
     "apres": "- **Statut** : **brouillon 12**, candidat au scellement, scellé comme brouillon, non contre-lu. Fabriqué par programme (`appliquer-brouillon12-ii-b-v1.py`, scellé dans ce dossier) depuis le brouillon 11 (`ordre-exploratoire-ii-b-v1-brouillon11.md`, `" + EMPREINTE_SOURCE + "`, intact, R12), recopié à l'octet hors des changements listés dans `differences-brouillon11-vers-12-v1.md`. Écrit le 2026-11-19 vers " + HEURE + " UTC (`date -u`) par le rédacteur du brouillon 11, du côté du saboteur à budget, exclu de tout rôle côté sondes du barreau 8 : il applique les trois décisions de la session mère sur les points qu'il lui avait rendus avec le brouillon 11 (message de la mère au rédacteur ; registre des décisions, ligne `R-3678`, écrite par la mère et non lue par le rédacteur), et rien d'autre ; il n'a lu de plus, pour ce brouillon, que le programme de comparaison `comparer-marqueurs-ordre-configuration-ii-b-v2.py` (`" + EMPREINTE_COMPARATEUR + "`) et sa sortie précédente. Ce qu'il change est dit à la section « Ce que le brouillon 12 change ». Le brouillon 11 a été fabriqué par programme (`appliquer-brouillon11-ii-b-v1.py`, scellé dans ce dossier) depuis le brouillon 10 ("},
    {"nom": "B12-0c", "c": 0, "lieu": "section neuve, placée avant « Ce que le brouillon 11 change »",
     "avant": "## Ce que le brouillon 11 change (détail : `differences-brouillon10-vers-11-v1.md`)\n",
     "apres": SECTION + "## Ce que le brouillon 11 change (détail : `differences-brouillon10-vers-11-v1.md`)\n"},
    {"nom": "B12-2", "c": 2, "lieu": "§ 4 étape 6, dernière phrase : lieu du rejeu",
     "avant": "À l'étape 1 du § 5, l'exécutante rejoue les contrôles dans un dossier neuf, avec les variables de cet ordre, et c'est ce dossier neuf que lit la création.",
     "apres": "À l'étape 2 du § 5, juste avant de créer, l'exécutante rejoue les contrôles dans un dossier neuf, `" + REJEU + "`, avec les variables de cet ordre, et c'est ce dossier neuf que lit la création."},
    {"nom": "B12-1", "c": 1, "lieu": "§ 5 étape 2 : rejeu joué une seule fois",
     "avant": "→ code 0, « CONTRÔLES CONFORMES … » ; tout autre code → arrêt. Puis : `",
     "apres": "→ code 0, « CONTRÔLES CONFORMES … » ; tout autre code → arrêt. " + PHRASES_REJEU + "Puis : `"},
    {"nom": "B12-3a", "c": 3, "lieu": "§ 11, comptes : sortie du programme de compte",
     "avant": "sortie sous un nom neuf, `sortie-compter-marqueurs-ii-b-v5.txt`",
     "apres": "sortie sous un nom neuf, `" + NOM_COMPTE + "`"},
    {"nom": "B12-3b", "c": 3, "lieu": "§ 11, comptes : sortie du programme de comparaison",
     "avant": "scellé dans ce dossier ; sortie `sortie-comparer-marqueurs-ordre-configuration-ii-b-v2.txt`, qui n'affiche aucune valeur",
     "apres": "scellé dans ce dossier ; sortie `" + NOM_COMPARAISON + "`, rejouée sur ce brouillon par le même programme, qui n'affiche aucune valeur"},
]


class Arret(Exception):
    pass


def h(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def creer(p: Path, b: bytes) -> None:
    with open(p, "xb") as f:
        f.write(b)


def jouer(prog: Path) -> tuple[int, str]:
    r = subprocess.run([sys.executable, "-I", "-B", str(prog), str(SORTIE)], capture_output=True, cwd=str(DOSSIER))
    return r.returncode, r.stdout.decode() + r.stderr.decode()


def lignes_differentes(avant: str, apres: str) -> list[str]:
    d = subprocess.run(["bash", "-c", 'diff <(printf %s "$0") <(printf %s "$1")', avant, apres], capture_output=True)
    return d.stdout.decode().rstrip("\n").split("\n") if d.stdout else []


def main() -> int:
    try:
        for p in (SORTIE, SORTIE_COMPTE, SORTIE_COMPARAISON, NOTE):
            if p.exists():
                raise Arret(f"{p.name} existe déjà (R12)")
        if "@" in HEURE:
            raise Arret("heure d'écriture non renseignée")
        brut = SOURCE.read_bytes()
        if h(brut) != EMPREINTE_SOURCE:
            raise Arret("empreinte du brouillon 11")
        if h(COMPARATEUR.read_bytes()) != EMPREINTE_COMPARATEUR:
            raise Arret("empreinte du programme de comparaison")
        lanceur = subprocess.run(["git", "-C", str(RACINE), "show", f"{COMMIT}:{LANCEUR}"], capture_output=True, check=True).stdout
        if h(lanceur) != EMPREINTE_LANCEUR:
            raise Arret("empreinte du lanceur au commit de lancement")
        ll = lanceur.decode("utf-8").split("\n")
        for num, fragment, _ in LIGNES_LANCEUR:
            if fragment not in ll[num - 1]:
                raise Arret(f"lanceur, ligne {num} : fragment attendu absent")
        source = brut.decode("utf-8")
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
            raise Arret("application inverse ≠ brouillon 11")
        if MOTIF_MARQUEUR.search(t):
            raise Arret("marqueur restant")
        if MOTIF_COMMANDE.findall(t) != MOTIF_COMMANDE.findall(source) or len(MOTIF_COMMANDE.findall(t)) != 4:
            raise Arret("les commandes du lanceur qui citent un dossier des contrôles ont changé")
        if "sortie-compter-marqueurs-ii-b-v5.txt" in t or "sortie-comparer-marqueurs-ordre-configuration-ii-b-v2.txt" in t:
            raise Arret("une sortie jouée sur le brouillon 10 est encore citée")
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
        compte_precedent = COMPTE_PRECEDENT.read_text(encoding="utf-8")
        comparaison_precedente = COMPARAISON_PRECEDENTE.read_text(encoding="utf-8")
    except (Arret, OSError, subprocess.CalledProcessError) as a:
        print(f"ARRÊT, rien n'est écrit : {a}", file=sys.stderr)
        return 1
    creer(SORTIE, t.encode())
    code1, compte = jouer(COMPTEUR)
    code2, comp = jouer(COMPARATEUR)
    creer(SORTIE_COMPTE, compte.encode())
    creer(SORTIE_COMPARAISON, comp.encode())
    meme = compte.split("\n")[1:] == compte_precedent.split("\n")[1:] and compte.split("\n")[0] == f"{SORTIE.name}  {h(t.encode())}"
    if code1 != 0 or "occurrences 0 ; distincts 0" not in compte or not meme or code2 != 0 or "BILAN : écarts 0" not in comp or "SCELLEMENT PERMIS" not in comp:
        print(f"ARRÊT après écriture : compte code {code1}, égal au précédent hors première ligne : {meme} ; comparaison code {code2} (0 attendu)", file=sys.stderr)
        return 1
    ecart_comp = lignes_differentes(comparaison_precedente, comp)
    ret = sum(1 for b in blocs for l in b["l"] if l.startswith("-")); aj = sum(1 for b in blocs for l in b["l"] if l.startswith("+"))
    n = ["# Différences du brouillon 11 au brouillon 12 de l'ordre exploratoire du saboteur à budget — v1\n",
         "Note fabriquée par programme (`appliquer-brouillon12-ii-b-v1.py`, dans ce dossier), en même temps que le brouillon 12. EXPLORATOIRE, NON OPPOSABLE (R-522). Aucun sujet, aucun mécanisme, aucun texte de consigne ni fragment n'y est écrit. Le rédacteur, celui du brouillon 11, travaille du côté du saboteur à budget : il est exclu de tout rôle côté sondes du barreau 8. Les changements appliquent les trois décisions de la session mère sur les points relevés avec le brouillon 11 (message au rédacteur ; routine, registre des décisions, ligne `R-3678`, écrite par la mère, non lue par le rédacteur) ; rien d'autre ne change.\n",
         "## 1. Pièces\n",
         f"- Brouillon 11 (intact, R12) : `{SOURCE.name}`, `{EMPREINTE_SOURCE}`.",
         f"- Brouillon 12 : `{SORTIE.name}`, `{h(t.encode())}`.",
         f"- Programme : `{Path(__file__).name}`, `{h(Path(__file__).read_bytes())}`.",
         f"- Programme de compte : `{COMPTEUR.name}`, `{h(COMPTEUR.read_bytes())}` ; sortie `{NOM_COMPTE}`, `{h(compte.encode())}` ; code {code1} ; égale à la sortie précédente (`{COMPTE_PRECEDENT.name}`, `{h(compte_precedent.encode())}`) hors de sa première ligne, qui porte le nom et l'empreinte du fichier compté.",
         f"- Programme de comparaison, v2, **inchangé**, lu en entier par le rédacteur : `{COMPARATEUR.name}`, `{EMPREINTE_COMPARATEUR}` ; sortie, sans aucune valeur, `{NOM_COMPARAISON}`, `{h(comp.encode())}` ; code de sortie {code2} : tout conforme, aucun emplacement ouvert ; sortie précédente, jouée sur le brouillon 10 : `{COMPARAISON_PRECEDENTE.name}`, `{h(comparaison_precedente.encode())}`.",
         f"- Lanceur, par `git show {COMMIT}:{LANCEUR}` (commit de lancement), empreinte recalculée : `{EMPREINTE_LANCEUR}`.\n",
         "## 2. Ce qui est appliqué\n",
         f"{len(couples)} couples, appliqués dans l'ordre. Lignes du brouillon 11 retirées ou réécrites : **{ret}** ; lignes du brouillon 12 neuves ou réécrites : **{aj}** ; {source.count(chr(10))} lignes deviennent {t.count(chr(10))}. `diff -u` rend {len(blocs)} blocs. Contrôles passés : chaque « avant » présent une fois à son application, chaque « après » une fois à la fin, application inverse égale au brouillon 11 à l'octet, aucun marqueur entre chevrons doubles, les quatre commandes du lanceur qui citent un dossier des contrôles inchangées, aucune sortie jouée sur le brouillon 10 encore citée, chaque bloc rattaché à un couple.\n"]
    n += [f"- Changement {k} : {q}." for k, q in CHANGEMENTS.items()]
    n += ["", "| couple | changement | lieu | ligne du brouillon 12 | bloc |", "|---|---|---|---|---|"]
    n += [f"| {c['nom']} | {c['c']} | {c['lieu']} | {c['ligne']} | {c['bloc']} |" for c in couples]
    n += ["", "## 3. Le programme de comparaison : pas de version neuve\n",
          "La mère demandait une v3 du programme si la v2 cherchait des fragments contenant le dossier de l'étape 1 et rendait un écart. Lu en entier, il ne lit que l'ordre qu'on lui passe et, par `git show`, la configuration du commit de lancement, son parent et la liste des fichiers de ce commit. À sa partie G, il cherche treize fragments dans le § 5, chacun attendu une fois. Un seul nomme un dossier des contrôles : la commande `controles-explo` de l'étape 1, avec son dossier, le commit de lancement et le chemin de la configuration. Elle est présente une fois au brouillon 12 : la commande du rejeu porte un autre dossier et n'est pas comptée. Aucun fragment ne porte sur `creation` avec son dossier ni sur `surveillance`. **Code 0, « BILAN : écarts 0 » sur le brouillon 12 ; le programme n'est donc pas modifié et aucune v3 n'est faite ; il n'y a pas de différence entre v2 et v3 à rendre.**\n",
          "Limite, dite telle : la v2 ne contrôle pas les trois commandes qui citent le dossier du rejeu (rejeu, `creation`, `surveillance`). Elles sont contrôlées par le programme du brouillon 11 (présentes une fois chacune) et par celui-ci (les quatre commandes qui citent un dossier des contrôles sont égales à celles du brouillon 11).\n",
          f"Lignes de la sortie de comparaison qui diffèrent de la sortie précédente, jouée sur le brouillon 10 ({len(ecart_comp)} lignes de `diff`) :\n",
          "~~~~", *ecart_comp, "~~~~\n",
          "Les deux comptes qui montent d'une unité (chemin de la configuration, commit de lancement, hors du § 11) viennent de la commande exacte du rejeu, ajoutée au brouillon 11 ; le programme n'y exige qu'au moins une occurrence.\n",
          "## 4. Lignes du lanceur relues par le programme (numéro, fragment présent, ce que la ligne fait)\n",
          "| ligne du lanceur | ce qu'elle fait |", "|---|---|"]
    n += [f"| {num} | {quoi} |" for num, _, quoi in LIGNES_LANCEUR]
    n += ["", "## 5. Relevé sans être corrigé\n",
          "1. **Dossier du rejeu déjà là, mais sans contrôles conformes.** La phrase neuve, écrite à la lettre de la décision, dit qu'un dossier du rejeu déjà là n'est pas un arrêt. Le lanceur crée ce dossier avant la fin de ses contrôles (l. 86) et n'y écrit `lancement.txt` qu'à la fin (l. 126) : un rejeu arrêté en chemin (code 2, déjà un arrêt d'après la phrase précédente de l'ordre) laisse un dossier sans `lancement.txt`. Dans ce cas, « passer à la création » ne crée rien : `creation` refuse en code 2 un dossier sans contrôles conformes (l. 133). La garde tient donc dans le lanceur ; l'ordre ne le dit pas.",
          "2. **Ce que les reprises revérifient sans rejeu** : chaque commande `creation` relit la ligne d'accord, la ligne de 7b, le calendrier et l'amorce (l. 139, 143, 144, 170) ; elle ne relit ni les empreintes des tâches et des consignes ni le contrôle « aucune tâche commune », que seul `controles-explo` joue. Le commit étant figé, ces contrôles ne peuvent pas changer d'issue entre deux reprises.",
          "3. La section « Ce que le brouillon 11 change » garde son texte d'alors (histoire) : elle dit le § 11 non touché et le programme de comparaison non rejoué.",
          "4. `R-3678` est cité sur la parole de la mère : le rédacteur n'a pas lu cette ligne (il a seulement compté, par programme, qu'elle figure une fois au registre des décisions).",
          "5. Les points 4 à 8 rendus avec le brouillon 11 : rien n'est fait ici, la mère les consigne elle-même.\n",
          "## 6. Sortie du programme de compte\n", "~~~~", compte.rstrip("\n"), "~~~~\n",
          "## 7. Sortie du programme de comparaison, v2\n", "~~~~", comp.rstrip("\n"), "~~~~\n",
          "## 8. Changements, bloc par bloc, tirés de `diff -u`\n"]
    for k, b in enumerate(blocs, 1):
        n += [f"### Bloc {k} — lignes {b['deb']} à {b['fin']} du brouillon 12 — couples {', '.join(b['c'])}\n", "~~~~diff", b["e"], *b["l"], "~~~~\n"]
    creer(NOTE, "\n".join(n).encode())
    for p in (SORTIE, SORTIE_COMPTE, SORTIE_COMPARAISON, NOTE):
        print(f"{p.name}  {h(p.read_bytes())}")
    print(f"couples {len(couples)} ; blocs {len(blocs)} ; retirées {ret} ; neuves {aj} ; comparaison code {code2}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
