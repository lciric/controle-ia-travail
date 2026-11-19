"""Fabrique le brouillon 10 de l'ordre exploratoire du saboteur à budget (ii-b) — v1. EXPLORATOIRE, NON OPPOSABLE (R-522).

Usage (depuis la racine du dépôt) :
    python3 -I -B brouillons/ii-b-saboteur-budget-v1/appliquer-brouillon10-ii-b-v1.py [--a-blanc DOSSIER_EXISTANT]

Il vérifie l'empreinte du brouillon 9, lui applique dans l'ordre les couples « avant » / « après » écrits plus bas
(chaque « avant » présent exactement une fois au moment de son application ; chaque « après » présent exactement une
fois à la fin ; application inverse égale au brouillon 9 à l'octet ; chaque bloc de `diff -u` rattaché à un couple),
contrôle qu'aucun marqueur entre chevrons doubles et aucun emplacement de pièce entre crochets n'y reste, recalcule
par `git show` l'empreinte des deux pièces à blanc de l'exécutante et la compare à leur compagnon, écrit le
brouillon 10, joue le programme de compte et la v2 du programme de comparaison (code 0 attendu : tout conforme,
aucun emplacement ouvert), écrit leurs sorties et la note des différences. Il n'écrase jamais (R12). Il n'ouvre que le brouillon 9, les deux programmes qu'il lance, le
compagnon de la vérification des brouillons 6 et lui-même. Aucun texte de consigne ni fragment n'y est écrit.
Les décisions appliquées sont celles de deux messages de la session mère au rédacteur (ligne du registre à venir : R-3655).
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
SOURCE = DOSSIER / "ordre-exploratoire-ii-b-v1-brouillon9.md"
EMPREINTE_SOURCE = "f07a39ee89c93e4caf0b3284e58a6ab2e07cd34674c2906bbb32ccbb72783e28"
SORTIE = DEST / "ordre-exploratoire-ii-b-v1-brouillon10.md"
COMPTEUR = DOSSIER / "compter-marqueurs-ii-b-v1.py"
COMPARATEUR = DOSSIER / "comparer-marqueurs-ordre-configuration-ii-b-v2.py"
SORTIE_COMPTE = DEST / "sortie-compter-marqueurs-ii-b-v5.txt"
SORTIE_COMPARAISON = DEST / "sortie-comparer-marqueurs-ordre-configuration-ii-b-v2.txt"
NOTE = DEST / "differences-brouillon9-vers-10-v1.md"
VERIF6 = "docs/notes/barreau8-iib-v1/verification-ordre-et-devis-iib-brouillon6-v1.md"
EMPREINTE_VERIF6 = "bd7941ecec095fec470df9cb07e7ba488ac5a6a3060b7c6e5a115b3f435a9127"
SONDES = "8e432cdc3d6998324281467e1bac5df3adb93ff7ba803b8ad7f877ffd5e8feb4"
HEURE = "07:56"
TETE_EXECUTANTE = "a0ce3f3eedadf218908b5fc2149ab44ea7c895d7"  # tête rapatriée de `claude/iib-executante-v1`
P1 = "registres/iib-executante/blanc-836c7ccc-v1/journal-blanc-extraction-run-836c7ccc-v1.txt"
H1 = "afc5aca838fde30c8ae779fb7946b690a9803e7419681850f86f52b8f319e77d"
P2 = "registres/iib-executante/blanc-836c7ccc-v1/journal-blanc-verifier-go-836c7ccc-v1.txt"
H2 = "0297f3ac9a33277429451615081a55df3ec298625bde0a38cafd562ea7b3f730"
E1 = "pièce `" + P1 + "` (`" + H1 + "`), branche `claude/iib-executante-v1`, tête `" + TETE_EXECUTANTE + "`"
E2 = "pièce `" + P2 + "` (`" + H2 + "`), même branche, même tête"
MOTIF_MARQUEUR = re.compile(r"<<([A-Z0-9_]+)>>")
MOTIF_BLOC = re.compile(r"^@@ -(\d+)(?:,(\d+))? \+(\d+)(?:,(\d+))? @@")
PREFIXE_ECARTS = "   - **trois écarts relevés par le rédacteur du brouillon 9, déclarés, portés à la mère** :"

CHANGEMENTS = {
    0: "titre, citation d'en-tête, statut, section « Ce que le brouillon 10 change », noms des programmes et sorties au § 11",
    1: "point 1 : nombre d'essais attendu, 456 (§ 1, § 4 étape 6, § 5)",
    2: "points 2 et 3 : deux jeux à blanc joués par l'exécutante avant le scellement, pièces citées, aucun emplacement ouvert (§ 4 étapes 6 et 7)",
    3: "ajout demandé par la mère : contrôles du lanceur rejoués juste avant de créer (§ 5 étape 2)",
    4: "point 4 : pas de lecture du disque d'une instance arrêtée ; l'exécutante s'arrête et rend la main (§ 5 étape 5)",
    5: "point 5 : devis inscrit par la ligne d'engagement ; « proposé(s) » devient « retenu(s) par la mère » (§ 4 étape 3, § 11)",
    6: "point 6 : deux corrections facultatives de `R-3535`",
    7: "point 7 : deux exclusions ajoutées au § 8",
    8: "point 8 : le texte scellé des sondes est aussi le préenregistrement de la passe de recalcul (§ 13)",
    9: "point 9 : exclusions de toute copie publique (§ 7)",
    11: "défaut 1 du brouillon 9 : heure d'écriture",
    12: "défaut 2 du brouillon 9 : parenthèse du § 11 complétée",
}

COUPLES = [
    {"nom": "B10-0a", "c": 0, "lieu": "titre",
     "avant": "instance à part — v1, brouillon 9\n", "apres": "instance à part — v1, brouillon 10\n"},
    {"nom": "B10-0b", "c": 0, "lieu": "citation d'en-tête",
     "avant": "ses marqueurs en attente sont remplis (§ 11) ; il n'est ni scellé",
     "apres": "ses marqueurs en attente sont remplis (§ 11), et aucun emplacement de pièce n'y est ouvert ; il n'est ni scellé"},
    {"nom": "B10-0c", "c": 0, "lieu": "en-tête, statut",
     "avant": "- **Statut** : **brouillon 9**, candidat au scellement, scellé comme brouillon, non contre-lu. Fabriqué par programme (`appliquer-brouillon9-ii-b-v1.py`, scellé dans ce dossier) depuis le brouillon 8 (",
     "apres": "- **Statut** : **brouillon 10**, candidat au scellement, scellé comme brouillon, non contre-lu. Fabriqué par programme (`appliquer-brouillon10-ii-b-v1.py`, scellé dans ce dossier) depuis le brouillon 9 (`ordre-exploratoire-ii-b-v1-brouillon9.md`, `" + EMPREINTE_SOURCE + "`, intact, R12), recopié à l'octet hors des changements listés dans `differences-brouillon9-vers-10-v1.md`. Écrit le 2026-11-19 vers " + HEURE + " UTC (`date -u`) par le rédacteur du brouillon 9, du côté du saboteur à budget, exclu de tout rôle côté sondes du barreau 8 : il applique les décisions de la session mère sur les dix points et les deux défauts qu'il lui avait rendus (deux messages de la mère au rédacteur ; ligne du registre des décisions à venir, `R-3655`), et rien d'autre ; il n'a lu de plus, pour ce brouillon, que les deux pièces à blanc citées au § 4 étape 6, et n'a pas ouvert la vérification citée au § 5 étape 5, dont il a seulement recalculé l'empreinte. Ce qu'il change est dit à la section « Ce que le brouillon 10 change ». Le brouillon 9 a été fabriqué par programme (`appliquer-brouillon9-ii-b-v1.py`, scellé dans ce dossier) depuis le brouillon 8 ("},
    {"nom": "B10-11", "c": 11, "lieu": "en-tête, statut : heure d'écriture du brouillon 9",
     "avant": "Écrit le 2026-11-19 vers 07:55 UTC", "apres": "Écrit le 2026-11-19 vers 07:48 UTC"},
    {"nom": "B10-6a", "c": 6, "lieu": "en-tête, statut : heure d'écriture du brouillon 8 (`R-3535`)",
     "avant": "Écrit le 2026-11-18 vers 23:30 UTC", "apres": "Écrit le 2026-11-18 vers 23:24 UTC"},
    {"nom": "B10-0d", "c": 0, "lieu": "section neuve, placée avant « Ce que le brouillon 9 change »",
     "avant": "## Ce que le brouillon 9 change (détail : `differences-brouillon8-vers-9-v1.md`)\n",
     "apres": "## Ce que le brouillon 10 change (détail : `differences-brouillon9-vers-10-v1.md`)\n\n"
              "Décisions de la session mère sur les points que le rédacteur du brouillon 9 lui avait rendus (routine ; ligne du registre à venir, `R-3655`) ; rien d'autre ne change.\n\n"
              "- **Nombre d'essais attendu** : `IIB_TESTS_ATTENDUS` = 456 (§ 1, § 5 étapes 1 et 2) ; changement par rapport aux brouillons 3 à 9, qui laissaient cette variable vide.\n"
              "- **Deux jeux à blanc demandés par la mère, joués par l'exécutante** (§ 4 étape 6) : l'extraction des fichiers du run au commit de lancement, et la vérification de l'accord ; leurs pièces sont citées ; aucun emplacement de pièce ne reste ouvert, et le programme de comparaison refuserait le scellement s'il en restait un (§ 11).\n"
              "- **§ 5 étape 2** : l'exécutante rejoue les contrôles du lanceur juste avant de créer.\n"
              "- **Disque d'une instance arrêtée** (§ 5 étape 5) : aucune commande de lecture n'est nommée ; l'exécutante s'arrête et rend la main à la mère.\n"
              "- **Devis** (§ 4 étape 3) : inscrit par la ligne d'engagement du registre des dépenses, après le scellement ; au § 11, « proposé(s) » devient « retenu(s) par la mère ».\n"
              "- **Corrections de `R-3535`** : heure d'écriture du brouillon 8 ; ligne citée pour l'exclusion de son rédacteur.\n"
              "- **§ 8** : deux exclusions ajoutées (`R-3527`, `R-3535`). **§ 13** : le texte scellé des sondes est aussi le préenregistrement de la passe de recalcul. **§ 7** : exclusions de toute copie publique.\n"
              "- **Deux défauts du brouillon 9 corrigés** : son heure d'écriture (« vers 07:48 ») ; la parenthèse de la phrase « Brouillon 3 lu par renvoi » du § 11.\n\n"
              "## Ce que le brouillon 9 change (détail : `differences-brouillon8-vers-9-v1.md`)\n"},
    {"nom": "B10-1a", "c": 1, "lieu": "§ 1, ligne « Essais »",
     "avant": "; jouée d'office par l'amorce ; `IIB_TESTS_ATTENDUS` vide |",
     "apres": "; jouée d'office par l'amorce ; **`IIB_TESTS_ATTENDUS` = 456** : passé à l'instance, ce nombre fait arrêter la course par l'amorce si la dernière ligne des essais n'est pas « 456 passed » ; **changement par rapport aux brouillons 3 à 9**, qui laissaient cette variable vide, décidé par la mère (routine, `R-3655`) : les contrôles à blanc conformes ont été joués avec 456, le fichier de lancement le porte, et la garde la plus stricte est retenue |"},
    {"nom": "B10-5a", "c": 5, "lieu": "§ 4 étape 3 : devis",
     "avant": "inscrit en complément de la ligne d'accord (exigé par elle).",
     "apres": "inscrit en complément de la ligne d'accord (exigé par elle) : il est inscrit par la ligne d'engagement du registre des dépenses, que la mère écrit après le scellement (étape 8 ; `R-3655`)."},
    {"nom": "B10-2a", "c": 2, "lieu": "§ 4 étape 6 : les trois écarts du brouillon 9, tranchés ; deux emplacements ouverts",
     "avant": None,
     "apres": "   - **trois écarts relevés au brouillon 9, tranchés par la mère** (routine, `R-3655`) : **(i)** l'extraction des fichiers du run (forme de l'étape 5) a été jouée à blanc à `ec3b0329` seulement, sur un dépôt jouet  ; à la demande de la mère, l'exécutante l'a **rejouée à blanc au commit de lancement** `836c7ccc`, sur un dépôt jouet local dont la branche du run est l'enfant de ce commit : toutes les commandes en code 0, 2 fichiers listés, 2 vérifiés sur 2, artefact « fichier listé absent » refusé en code 1 ; " + E1 + " ; **(ii)** la commande `--verifier-go-seulement 55` de l'étape 1 du § 5 n'apparaît dans aucun journal des contrôles à blanc  ; à la demande de la mère, l'exécutante l'a **jouée à blanc**, seule, depuis le dépôt extrait au commit de lancement : code 0, « GO VÉRIFIÉ, RIEN CRÉÉ » ; elle n'appelle ni l'outil de location ni le réseau du loueur ; " + E2 + " ; **(iii)** nombre d'essais attendu : **456** ; la pièce `lancement-controles-836c7ccc-v1.txt` porte `tests_attendus 456`, les contrôles à blanc conformes ont été joués avec ce nombre, et cet ordre fixe désormais `IIB_TESTS_ATTENDUS=456` (§ 1, § 5 étape 1) : changement par rapport aux brouillons 3 à 9, confirmé par l'exécutante. Aux contrôles, le lanceur ne lit de cette variable que sa forme et la recopie dans `lancement.txt` ; à la création, il la passe à l'instance, où l'amorce arrête la course si la dernière ligne des essais n'est pas « 456 passed ». À l'étape 1 du § 5, l'exécutante rejoue les contrôles dans un dossier neuf, avec les variables de cet ordre, et c'est ce dossier neuf que lit la création.\n"},
    {"nom": "B10-2b", "c": 2, "lieu": "§ 4 étape 7 : emplacements ouverts",
     "avant": "restent la vérification courte et le scellement.",
     "apres": "restent la vérification courte et le scellement. Les deux pièces à blanc demandées à l'étape 6 sont citées : aucun emplacement de pièce n'est ouvert (contrôlé par le programme de comparaison, § 11)."},
    {"nom": "B10-1b", "c": 1, "lieu": "§ 5, consignes permanentes : écart sur le nombre d'essais, tranché",
     "avant": "un écart, sur le nombre d'essais attendu (§ 4 étape 6, écart (iii)).",
     "apres": "le seul écart d'alors, sur le nombre d'essais attendu, est tranché : 456 (§ 4 étape 6, (iii) ; `R-3655`)."},
    {"nom": "B10-1c", "c": 1, "lieu": "§ 5 étape 1 : variables communes",
     "avant": "IIB_DEPENSE_ANTERIEURE_USD=0 IIB_TESTS_ATTENDUS= PREREG_ABSENT=1",
     "apres": "IIB_DEPENSE_ANTERIEURE_USD=0 IIB_TESTS_ATTENDUS=456 PREREG_ABSENT=1"},
    {"nom": "B10-3", "c": 3, "lieu": "§ 5 étape 2 : contrôles rejoués juste avant de créer",
     "avant": "2. **Création** : `",
     "apres": "2. **Création** : juste avant de créer, l'exécutante rejoue `controles-explo` (étape 1, dossier neuf, variables de cet ordre) : son conteneur a redémarré le 2026-11-19 à 07:51:49Z ; le fichier de lancement des contrôles à blanc y est resté intact, empreinte inchangée (dit par la mère, `R-3655`). Puis : `"},
    {"nom": "B10-1d", "c": 1, "lieu": "§ 5 étape 2 : nombre d'essais passé à l'instance",
     "avant": "config-iib-reel-v1.json`, `-e ECHEANCE_UTC_S=1795816800`",
     "apres": "config-iib-reel-v1.json`, `-e TESTS_ATTENDUS=456`, `-e ECHEANCE_UTC_S=1795816800`"},
    {"nom": "B10-1e", "c": 1, "lieu": "§ 5 étape 2 : ce que le brouillon 3 écrit encore",
     "avant": "deux marqueurs entre chevrons doubles : leurs valeurs sont les deux premières de cette parenthèse).",
     "apres": "deux marqueurs entre chevrons doubles : leurs valeurs sont les deux premières de cette parenthèse ; il y écrit aussi le nombre d'essais attendu vide : la valeur est 456, `R-3655`)."},
    {"nom": "B10-4", "c": 4, "lieu": "§ 5 étape 5 : disque d'une instance arrêtée",
     "avant": "Sur ce mot seulement : lire le disque de l'instance arrêtée sans la démarrer, puis rapatrier de nouveau ; la commande de cette lecture est nommée et jouée à blanc par la mère avant le scellement de l'ordre ; sans elle, ce remède n'existe pas et l'écart est porté au compte rendu.",
     "apres": "Aucune commande de lecture du disque d'une instance arrêtée n'est nommée : si le cas se présente, l'exécutante ne relance ni ne détruit rien, s'arrête et rend la main à la mère (écart, nœud), dans les bornes de temps dites juste avant ; voir la vérification `" + VERIF6 + "` (`" + EMPREINTE_VERIF6 + "`), § 3 (décision de la mère, `R-3655`)."},
    {"nom": "B10-9", "c": 9, "lieu": "§ 7 : copie publique",
     "avant": "**question pour la mère** : vérifier que le script de la copie publique écarte `donnees/*-iib-*` (non vérifié par le rédacteur ni par le contre-lecteur).",
     "apres": "`donnees/*-iib-*` et `brouillons/ii-b-saboteur-budget-v1/` sont exclus de toute copie publique (décision de la mère, `R-3655`)."},
    {"nom": "B10-6b", "c": 6, "lieu": "§ 8 : ligne citée pour le rédacteur du brouillon 8 (`R-3535`)",
     "avant": "le rédacteur du brouillon 8 (mandat de la session mère, `R-3523`, suite), qui ont lu cet ordre.",
     "apres": "le rédacteur du brouillon 8 (mandat de la session mère, `R-3524`), qui ont lu cet ordre."},
    {"nom": "B10-7", "c": 7, "lieu": "§ 8 : deux exclusions ajoutées",
     "avant": "le rédacteur du brouillon 9 (`R-3635`), qui a lu cet ordre et les marqueurs de la configuration.",
     "apres": "le rédacteur des brouillons 9 et 10 (`R-3635`), qui a lu cet ordre et les marqueurs de la configuration ; le fabricant de la conception finale (`R-3527`) ; le contrôleur de la différence des brouillons 7 et 8 de cet ordre (`R-3535`)."},
    {"nom": "B10-5b", "c": 5, "lieu": "§ 11, ligne `DERNIER_JOUR_CREATION_IIB`",
     "avant": "| `DERNIER_JOUR_CREATION_IIB` | rempli (proposé) |",
     "apres": "| `DERNIER_JOUR_CREATION_IIB` | rempli (retenu par la mère, routine, `R-3655`) |"},
    {"nom": "B10-5c", "c": 5, "lieu": "§ 11, ligne de la consigne",
     "avant": "| `CHEMIN_CONSIGNE_IIB`, `EMPREINTE_CONSIGNE_IIB` | remplis (proposés) |",
     "apres": "| `CHEMIN_CONSIGNE_IIB`, `EMPREINTE_CONSIGNE_IIB` | remplis (retenus par la mère, routine, `R-3655`) |"},
    {"nom": "B10-5d", "c": 5, "lieu": "§ 11, ligne du devis",
     "avant": "| `CHEMIN_DEVIS_IIB`, `EMPREINTE_DEVIS_IIB` | remplis (proposés, sous réserve de la contre-lecture du devis) |",
     "apres": "| `CHEMIN_DEVIS_IIB`, `EMPREINTE_DEVIS_IIB` | remplis (retenus par la mère, routine, `R-3655`) |"},
    {"nom": "B10-12", "c": 12, "lieu": "§ 11, « Brouillon 3 lu par renvoi » : parenthèse complétée",
     "avant": "(commande de création, § 5 étape 2 ; rôle du lecteur, § 8), sa valeur est celle de cette table, ou, pour le commit de lancement, celle de la ligne `COMMIT_LANCEMENT_IIB` de la table des états.",
     "apres": "(commande de création et levée bornée de l'interdit, § 5 ; longueurs de la consigne, § 4 ter ; rôle du lecteur, § 8 ; réglages de la lecture (2), § 2), sa valeur est celle de cette table, ou, pour un marqueur propre à l'ordre, celle de sa ligne dans la table des états."},
    {"nom": "B10-0e", "c": 0, "lieu": "§ 11, comptes : sortie du programme de compte",
     "avant": "`sortie-compter-marqueurs-ii-b-v4.txt`", "apres": "`sortie-compter-marqueurs-ii-b-v5.txt`"},
    {"nom": "B10-0f", "c": 0, "lieu": "§ 11, comptes : programme de comparaison, v2, et refus du scellement",
     "avant": "(`comparer-marqueurs-ordre-configuration-ii-b-v1.py`, scellé dans ce dossier ; sortie `sortie-comparer-marqueurs-ordre-configuration-ii-b-v1.txt`, qui n'affiche aucune valeur)",
     "apres": "(`comparer-marqueurs-ordre-configuration-ii-b-v2.py`, scellé dans ce dossier ; sortie `sortie-comparer-marqueurs-ordre-configuration-ii-b-v2.txt`, qui n'affiche aucune valeur ; la v2 vérifie aussi le nombre d'essais attendu au § 5, compte les emplacements de pièces restés ouverts et **refuse le scellement, code 3, s'il en reste un** : il n'en reste aucun)"},
    {"nom": "B10-8", "c": 8, "lieu": "§ 13, « Ce qu'elle exige avant de partir »",
     "avant": "son préenregistrement scellé et contre-lu (quoi enregistrer : couches, jetons, précision ; choix du côté des moniteurs) ;",
     "apres": "son préenregistrement scellé et contre-lu (quoi enregistrer : couches, jetons, précision ; choix du côté des moniteurs) : c'est le texte scellé `prereg/lecture-sondes-barreau8-v1.md` (`" + SONDES + "`), qui est aussi le préenregistrement de la passe de recalcul ; son titre le dit (dit par la mère, `R-3655` ; le rédacteur, exclu, ne l'a pas ouvert) ;"},
]


class Arret(Exception):
    pass


def h(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def jouer(prog: Path) -> tuple[int, str]:
    r = subprocess.run([sys.executable, "-I", "-B", str(prog), str(SORTIE)], capture_output=True, cwd=str(DOSSIER))
    return r.returncode, r.stdout.decode() + r.stderr.decode()


def creer(p: Path, b: bytes) -> None:
    with open(p, "xb") as f:
        f.write(b)


def main() -> int:
    try:
        for p in (SORTIE, SORTIE_COMPTE, SORTIE_COMPARAISON, NOTE):
            if p.exists():
                raise Arret(f"{p.name} existe déjà (R12)")
        if "@" in HEURE:
            raise Arret("heure d'écriture non renseignée")
        brut = SOURCE.read_bytes()
        if h(brut) != EMPREINTE_SOURCE:
            raise Arret("empreinte du brouillon 9")
        if (RACINE / (VERIF6 + ".sha256")).read_text().split()[0] != EMPREINTE_VERIF6 or h((RACINE / VERIF6).read_bytes()) != EMPREINTE_VERIF6:
            raise Arret("empreinte de la vérification des brouillons 6")
        source = brut.decode("utf-8")
        lignes = [l for l in source.split("\n") if l.startswith(PREFIXE_ECARTS)]
        if len(lignes) != 1:
            raise Arret("ligne des trois écarts introuvable")
        couples = [dict(c) for c in COUPLES]
        for c in couples:
            if c["avant"] is None:
                c["avant"] = lignes[0] + "\n"
        t = source
        for c in couples:
            if t.count(c["avant"]) != 1:
                raise Arret(f"{c['nom']} : « avant » présent {t.count(c['avant'])} fois")
            t = t.replace(c["avant"], c["apres"])
        retour = t
        for c in reversed(couples):
            if retour.count(c["apres"]) != 1:
                raise Arret(f"{c['nom']} : « après » présent {retour.count(c['apres'])} fois")
            retour = retour.replace(c["apres"], c["avant"])
        if retour != source:
            raise Arret("application inverse ≠ brouillon 9")
        if MOTIF_MARQUEUR.search(t) or t.count(E1) != 1 or t.count(E2) != 1 or "[PIÈCE" in t:
            raise Arret("marqueur restant, emplacement de pièce ouvert, ou pièces à blanc mal citées")
        for chemin, attendue in ((P1, H1), (P2, H2)):
            b = subprocess.run(["git", "-C", str(RACINE), "show", f"{TETE_EXECUTANTE}:{chemin}"], capture_output=True, check=True).stdout
            s = subprocess.run(["git", "-C", str(RACINE), "show", f"{TETE_EXECUTANTE}:{chemin}.sha256"], capture_output=True, check=True).stdout.decode().split()[0]
            if not (h(b) == s == attendue):
                raise Arret(f"pièce à blanc {chemin} : empreinte ≠ compagnon ou ≠ attendue")
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
        for c in couples:
            pos = t.index(c["apres"]); c["ligne"] = t.count("\n", 0, pos) + 1
            der = c["ligne"] + c["apres"].rstrip("\n").count("\n")
            dans = [n for n, b in enumerate(blocs, 1) if not (der < b["deb"] or c["ligne"] > b["fin"])]
            if len(dans) != 1:
                raise Arret(f"{c['nom']} rattaché à {len(dans)} blocs")
            c["bloc"] = dans[0]; blocs[dans[0] - 1]["c"].append(c["nom"])
        if any(not b["c"] for b in blocs):
            raise Arret("bloc de diff sans couple")
    except (Arret, OSError, subprocess.CalledProcessError) as a:
        print(f"ARRÊT, rien n'est écrit : {a}", file=sys.stderr)
        return 1
    creer(SORTIE, t.encode())
    code1, compte = jouer(COMPTEUR)
    code2, comp = jouer(COMPARATEUR)
    creer(SORTIE_COMPTE, compte.encode())
    creer(SORTIE_COMPARAISON, comp.encode())
    if code1 != 0 or "occurrences 0 ; distincts 0" not in compte or code2 != 0 or "BILAN : écarts 0" not in comp:
        print(f"ARRÊT après écriture : compte code {code1}, comparaison code {code2} (0 attendu)", file=sys.stderr)
        return 1
    ret = sum(1 for b in blocs for l in b["l"] if l.startswith("-")); aj = sum(1 for b in blocs for l in b["l"] if l.startswith("+"))
    lieux = [(n, e) for n, l in enumerate(t.split("\n"), 1) for e in (P1, P2) if e in l]
    n = ["# Différences du brouillon 9 au brouillon 10 de l'ordre exploratoire du saboteur à budget — v1\n",
         "Note fabriquée par programme (`appliquer-brouillon10-ii-b-v1.py`, dans ce dossier), en même temps que le brouillon 10. EXPLORATOIRE, NON OPPOSABLE (R-522). Aucun sujet, aucun mécanisme, aucun texte de consigne ni fragment n'y est écrit. Le rédacteur travaille du côté du saboteur à budget : il est exclu de tout rôle côté sondes du barreau 8. Les changements appliquent les décisions de la session mère (deux messages au rédacteur ; ligne du registre à venir, `R-3655`) sur les dix points et les deux défauts rendus avec le brouillon 9 ; rien d'autre ne change.\n",
         "## 1. Pièces\n",
         f"- Brouillon 9 (intact, R12) : `{SOURCE.name}`, `{EMPREINTE_SOURCE}`.",
         f"- Brouillon 10 : `{SORTIE.name}`, `{h(t.encode())}`.",
         f"- Programme : `{Path(__file__).name}`, `{h(Path(__file__).read_bytes())}`.",
         f"- Programme de compte : `{COMPTEUR.name}`, `{h(COMPTEUR.read_bytes())}` ; sortie `{SORTIE_COMPTE.name}`, `{h(compte.encode())}`.",
         f"- Programme de comparaison, v2 : `{COMPARATEUR.name}`, `{h(COMPARATEUR.read_bytes())}` ; sortie, sans aucune valeur, `{SORTIE_COMPARAISON.name}`, `{h(comp.encode())}` ; code de sortie {code2} : tout conforme, aucun emplacement ouvert.",
         f"- Vérification des brouillons 6, citée au § 5 étape 5, non ouverte, empreinte recalculée : `{VERIF6}`, `{EMPREINTE_VERIF6}`.\n",
         f"- Pièces à blanc de l'exécutante, lues par `git show` sur `claude/iib-executante-v1`, tête `{TETE_EXECUTANTE}`, égales à leur compagnon : `{P1}`, `{H1}` ; `{P2}`, `{H2}`.\n",
         "## 2. Emplacements de pièces : aucun ouvert ; les deux pièces sont citées\n"]
    n += [f"- ligne {k} du brouillon 10 (§ 4 étape 6) : `{e}`" for k, e in lieux]
    n += ["", "## 3. Ce qui est appliqué\n",
          f"{len(couples)} couples, appliqués dans l'ordre. Lignes du brouillon 9 retirées ou réécrites : **{ret}** ; lignes du brouillon 10 neuves ou réécrites : **{aj}** ; {source.count(chr(10))} lignes deviennent {t.count(chr(10))}. `diff -u` rend {len(blocs)} blocs. Contrôles passés : chaque « avant » présent une fois à son application, chaque « après » une fois à la fin, application inverse égale au brouillon 9 à l'octet, aucun marqueur entre chevrons doubles, aucun emplacement de pièce ouvert, les deux pièces à blanc citées une fois chacune, chaque bloc rattaché à un couple.\n"]
    n += [f"- Changement {k} : {q}." for k, q in CHANGEMENTS.items()]
    n += ["", "| couple | changement | lieu | ligne du brouillon 10 | bloc |", "|---|---|---|---|---|"]
    n += [f"| {c['nom']} | {c['c']} | {c['lieu']} | {c['ligne']} | {c['bloc']} |" for c in couples]
    n += ["", "## 4. Relevé sans être corrigé\n",
          "1. § 5 étape 5 : la phrase de la lecture du disque est remplacée ; deux phrases plus bas dans la même étape parlent encore de « la lecture du disque » (un fichier que les motifs de la poussée ne couvrent pas ; une relance commandée seulement après elle) : laissées telles, hors des décisions reçues. Les mots « dans les bornes de temps dites juste avant » sont ajoutés par le rédacteur pour que « ne détruit rien » ne contredise pas la borne de 48 heures de la phrase précédente : à confirmer par la mère.",
          "2. Les sections « Ce que le brouillon 9 change » et « Traitement des remarques » gardent leur texte d'alors (histoire) ; la ligne O-m13 y dit encore la question de la copie publique « portée à la mère ».",
          "3. `R-3655` est écrit sur la parole de la mère : la ligne n'existait pas au registre quand ce brouillon a été fabriqué.",
          "4. § 5 étape 2 : le redémarrage du conteneur de l'exécutante et l'état du fichier de lancement sont écrits sur la parole de la mère ; le rédacteur ne les a pas vérifiés.",
          "5. Le point 10 (« cinq » valeurs de différence entre les deux configurations) : rien à changer.\n",
          "## 5. Sortie du programme de compte\n", "~~~~", compte.rstrip("\n"), "~~~~\n",
          "## 6. Sortie du programme de comparaison, v2\n", "~~~~", comp.rstrip("\n"), "~~~~\n",
          "## 7. Changements, bloc par bloc, tirés de `diff -u`\n"]
    for k, b in enumerate(blocs, 1):
        n += [f"### Bloc {k} — lignes {b['deb']} à {b['fin']} du brouillon 10 — couples {', '.join(b['c'])}\n", "~~~~diff", b["e"], *b["l"], "~~~~\n"]
    creer(NOTE, "\n".join(n).encode())
    for p in (SORTIE, SORTIE_COMPTE, SORTIE_COMPARAISON, NOTE):
        print(f"{p.name}  {h(p.read_bytes())}")
    print(f"couples {len(couples)} ; blocs {len(blocs)} ; retirées {ret} ; neuves {aj} ; comparaison code {code2}")
    for k, e in lieux:
        print(f"pièce citée, ligne {k} : {e}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
