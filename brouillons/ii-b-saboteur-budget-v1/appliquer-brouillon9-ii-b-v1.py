"""Fabrique le brouillon 9 de l'ordre exploratoire du saboteur à budget (ii-b) — v1. EXPLORATOIRE, NON OPPOSABLE (R-522).

Usage (depuis la racine du dépôt, après `git fetch` des deux branches citées plus bas) :
    python3 -I -B brouillons/ii-b-saboteur-budget-v1/appliquer-brouillon9-ii-b-v1.py
    python3 -I -B brouillons/ii-b-saboteur-budget-v1/appliquer-brouillon9-ii-b-v1.py --a-blanc DOSSIER_EXISTANT
        (jeu à blanc : mêmes contrôles, les quatre sorties écrites dans DOSSIER_EXISTANT, rien dans le dépôt)

Ce que fait ce programme, et rien d'autre :
1. il vérifie l'empreinte du brouillon 8 de l'ordre ;
2. il lit la configuration de la course par `git show COMMIT_DE_LANCEMENT:CHEMIN`, recalcule son empreinte, la compare à
   l'empreinte attendue, et y prend les valeurs des 30 marqueurs ; aucune valeur de marqueur n'est écrite à la main
   dans ce programme : les textes « après » portent des places `@@NOM@@`, remplies par ces valeurs ;
3. il vérifie par `git` : le parent direct du commit de lancement est le commit du code que la configuration nomme ;
   ce commit a pour parent direct le commit du code revu d'alors ; le commit de lancement n'ajoute que la configuration
   et son sceau ; il vérifie au registre des décisions (lecture seule) que la ligne de l'entropie porte la valeur de
   la configuration et que la ligne citée pour le mot de création existe une seule fois ;
4. il recalcule l'empreinte de chaque pièce citée (par `git show` pour les pièces de la branche de l'exécutante, sur
   le disque pour les autres) et la compare à son compagnon `.sha256` ; pour la conception et pour le texte de
   lecture des sondes, il ne lit QUE le compagnon, jamais le fichier ;
5. il applique au brouillon 8 les couples « avant » / « après » écrits plus bas, dans l'ordre ; chaque « avant » doit
   être présent exactement une fois au moment de son application, sinon arrêt sans rien écrire ;
6. il contrôle : chaque « après » présent exactement une fois à la fin ; application inverse égale au brouillon 8 à
   l'octet ; aucun marqueur entre chevrons doubles restant ; aucune place `@@NOM@@` restante ; chaque bloc de
   `diff -u` rattaché à au moins un couple et chaque couple à un bloc ; sinon arrêt sans rien écrire ;
7. il écrit `ordre-exploratoire-ii-b-v1-brouillon9.md` ; il joue `compter-marqueurs-ii-b-v1.py` et
   `comparer-marqueurs-ordre-configuration-ii-b-v1.py` sur ce fichier et écrit leurs sorties sous
   `sortie-compter-marqueurs-ii-b-v4.txt` et `sortie-comparer-marqueurs-ordre-configuration-ii-b-v1.txt` ; il écrit
   `differences-brouillon8-vers-9-v1.md` (chaque bloc de `diff -u` rattaché à son changement, puis le bloc lui-même).

Il n'écrase jamais (R12) : arrêt si l'un des quatre fichiers de sortie existe ; création exclusive. Il n'ouvre ni la
consigne privée, ni la conception, ni le texte de lecture des sondes, ni aucun résultat. Aucun repli silencieux (R5).
Aucun texte de consigne ni fragment n'y est écrit : la configuration n'en porte pas (chemin et empreinte seulement).
"""
from __future__ import annotations

import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

DOSSIER = Path(__file__).resolve().parent
RACINE = DOSSIER.parent.parent
SOURCE = DOSSIER / "ordre-exploratoire-ii-b-v1-brouillon8.md"
EMPREINTE_SOURCE = "eb83e9444df3bdfa822ef3bf76efe4039b450a7a8458fe4c91ba20f73d4eb76e"
# Jeu à blanc : `--a-blanc DOSSIER_EXISTANT` écrit les quatre sorties dans ce dossier, hors du dépôt, et nulle part ailleurs.
DESTINATION = Path(sys.argv[2]).resolve() if len(sys.argv) == 3 and sys.argv[1] == "--a-blanc" else DOSSIER
SORTIE = DESTINATION / "ordre-exploratoire-ii-b-v1-brouillon9.md"
COMPTEUR = DOSSIER / "compter-marqueurs-ii-b-v1.py"
COMPARATEUR = DOSSIER / "comparer-marqueurs-ordre-configuration-ii-b-v1.py"
SORTIE_COMPTE = DESTINATION / "sortie-compter-marqueurs-ii-b-v4.txt"
SORTIE_COMPARAISON = DESTINATION / "sortie-comparer-marqueurs-ordre-configuration-ii-b-v1.txt"
NOTE = DESTINATION / "differences-brouillon8-vers-9-v1.md"
REGISTRE = RACINE / "registres/decisions.md"

COMMIT_LANCEMENT = "836c7cccda5071fe54ecb148d214d74b5cb90474"
COMMIT_CODE_D_ALORS = "ec3b0329cd59db676007bd6c9ea3f0c36cf3ce95"
CHEMIN_CONFIG = "docs/notes/barreau8-iib-v1/config-iib-reel-v1.json"
EMPREINTE_CONFIG_ATTENDUE = "1bd2e16a79def36de945359bb64e34beb899410dfe2964d28da1f1b85e3f6a17"
TETE_EXECUTANTE = "68c1b734c5b5676640ff562e28bb408271f5b372"  # tête rapatriée de `claude/iib-executante-v1`
LIGNE_ENTROPIE = "R-3525"
HEURE = "08:05"  # heure d'écriture, relevée par `date -u` au lancement de ce programme

CIRCULAIRE = "hors configuration (circulaire)"
MOTIF_MARQUEUR = re.compile(r"<<([A-Z0-9_]+)>>")
MOTIF_PLACE = re.compile(r"@@([A-Za-z0-9_:.\-]+)@@")
MOTIF_BLOC = re.compile(r"^@@ -(\d+)(?:,(\d+))? \+(\d+)(?:,(\d+))? @@")

# Pièces citées avec leur empreinte entière, recalculée par ce programme et comparée au compagnon `.sha256`.
# (clé de la place, origine, chemin) ; origine « ex » : `git show TETE_EXECUTANTE:chemin` ; « disque » : fichier du
# dépôt ; « compagnon » : compagnon seul, le fichier n'est pas ouvert.
EX = "registres/iib-executante/"
PIECES = [
    ("contre-lecture", "disque", "docs/notes/barreau8-iib-v1/contre-lecture-correctif-lanceur-taches-f9a8aaeb-v1.md"),
    ("mandat", "disque", EX + "mandat-executante-iib-v1.md"),
    ("journal-v1", "ex", EX + "journal-v1.md"),
    ("journal-v5", "ex", EX + "journal-v5.md"),
    ("journal-v6", "ex", EX + "journal-v6.md"),
    ("empreintes-code", "ex", EX + "blanc-836c7ccc-v1/empreintes-code-iib-836c7ccc-v1.txt"),
    ("journal-blanc", "ex", EX + "blanc-836c7ccc-v1/journal-blanc-836c7ccc-v1.txt"),
    ("suite-v1", "ex", EX + "blanc-836c7ccc-v1/suite-ciblee-v1-836c7ccc-v1.txt"),
    ("suite-v2", "ex", EX + "blanc-836c7ccc-v1/suite-ciblee-v2-836c7ccc-v1.txt"),
    ("difference-config", "ex", EX + "blanc-836c7ccc-v1/difference-configuration-968a5151-vers-836c7ccc-v1.txt"),
    ("lancement-controles", "ex", EX + "blanc-836c7ccc-v1/lancement-controles-836c7ccc-v1.txt"),
    ("journal-blanc-ec3b", "ex", EX + "blanc-ec3b0329-v1/journal-blanc-ec3b0329-v1.txt"),
    ("journal-extraction-ec3b", "ex", EX + "blanc-ec3b0329-v1/journal-blanc-extraction-run-ec3b0329-v2.txt"),
    ("journal-blanc-968a", "ex", EX + "blanc-968a5151-v1/journal-blanc-968a5151-v1.txt"),
    ("sondes", "compagnon", "prereg/lecture-sondes-barreau8-v1.md"),
    ("conception", "compagnon", "brouillons/ii-b-saboteur-budget-v1/conception-ii-b-v1.md"),
]
EMPREINTE_SONDES_ATTENDUE = "8e432cdc3d6998324281467e1bac5df3adb93ff7ba803b8ad7f877ffd5e8feb4"

CHANGEMENTS = {
    1: "titre, citation d'en-tête, statut, accords, pièces citées, code lu ; section « Ce que le brouillon 9 change »",
    2: "marqueurs en attente remplis par les valeurs de la configuration du commit de lancement",
    3: "état vrai du code : commit du code revu `f9a8aaeb` sur `prep/iib-code-v4`, soit `ec3b0329` plus le correctif du lanceur ; premier commit de lancement abandonné",
    4: "§ 4 : étapes 4 à 7, état et pièces ; délégation des contrôles à blanc, écart déclaré",
    5: "§ 5 : commandes exactes au commit de lancement",
    6: "texte de lecture des sondes scellé (§ 8, § 13)",
    7: "§ 8 : exclus ajoutés",
    8: "§ 11 : table des états, table des valeurs à l'octet, comptes",
}

# Chaque couple : nom, numéro du changement, lieu, texte « avant », texte « après ».
COUPLES = [
    {
        "nom": "B9-1a", "changement": 1, "lieu": "titre",
        "avant": "# Ordre — saboteur à budget (ii-b), **course exploratoire**, instance à part — v1, brouillon 8\n",
        "apres": "# Ordre — saboteur à budget (ii-b), **course exploratoire**, instance à part — v1, brouillon 9\n",
    },
    {
        "nom": "B9-1b", "changement": 1, "lieu": "citation d'en-tête",
        "avant": "Cet ordre reste un brouillon : il n'est ni scellé comme ordre ni remis tant que les marqueurs en attente (§ 11) ne sont pas remplis.",
        "apres": "Cet ordre reste un brouillon, candidat au scellement : ses marqueurs en attente sont remplis (§ 11) ; il n'est ni scellé comme ordre ni remis avant sa vérification courte par un autre lecteur et son scellement par la session mère (§ 4 étape 7).",
    },
    {
        "nom": "B9-1c", "changement": 1, "lieu": "en-tête, statut",
        "avant": "- **Statut** : **brouillon 8**, scellé comme brouillon, non contre-lu. Fabriqué par programme (`appliquer-brouillon8-ii-b-v1.py`, scellé dans ce dossier) depuis le brouillon 7 (",
        "apres": (
            "- **Statut** : **brouillon 9**, candidat au scellement, scellé comme brouillon, non contre-lu. Fabriqué par programme (`appliquer-brouillon9-ii-b-v1.py`, scellé dans ce dossier) depuis le brouillon 8 (`ordre-exploratoire-ii-b-v1-brouillon8.md`, `eb83e9444df3bdfa822ef3bf76efe4039b450a7a8458fe4c91ba20f73d4eb76e`, intact, R12), recopié à l'octet hors des changements listés dans `differences-brouillon8-vers-9-v1.md`. "
            "Écrit le 2026-11-19 vers @@HEURE@@ UTC (`date -u`) par un rédacteur neuf (sous-agent de la session mère `session_013QMayjsoZJFBUCqcnvD5h1`, modèle Claude Fable 5.2), **qui travaille du côté du saboteur à budget et est donc exclu de tout rôle côté sondes du barreau 8** (rédaction, contre-lecture, lecture, verdict ; § 8). "
            "Il n'a écrit ni la conception, ni le code, ni la configuration, ni leurs contre-lectures, ni les brouillons 1 à 8 ; il n'a ouvert ni la consigne privée, ni la conception, ni le texte de lecture des sondes, ni l'enveloppe de la huitième tâche ; il n'a lu aucun résultat. "
            "Il n'a lu, pour ce brouillon, que : le brouillon 8 en entier ; du brouillon 3, les passages que cet ordre reprend par renvoi au § 5 étape 2 et au § 8 ; les lignes des registres dites à la ligne « Accords » ; la configuration au commit de lancement, par programme, pour ses marqueurs et pour les valeurs libres du § 2 seulement ; le code dit à la ligne « Code lu » ; les pièces dites à la ligne « Pièces citées ». "
            "Ce qu'il change est dit à la section « Ce que le brouillon 9 change ». "
            "Le brouillon 8 a été fabriqué par programme (`appliquer-brouillon8-ii-b-v1.py`, scellé dans ce dossier) depuis le brouillon 7 ("
        ),
    },
    {
        "nom": "B9-1d", "changement": 1, "lieu": "en-tête, accords et lignes de registre lues",
        "avant": "réserve P7-R1 acceptée par la mère comme réserve écrite).\n- **Pièces citées**",
        "apres": (
            "réserve P7-R1 acceptée par la mère comme réserve écrite). "
            "Au brouillon 9, lues : dans `registres/go.md`, la ligne `GO-2026-11-10-08` et la ligne `GO-2026-11-19-04` (mot de Lazar pour la création de la course, donné dans la session mère ; la dépense reste sous `GO-2026-11-10-08`) ; "
            "dans le registre des décisions, les lignes `R-3525` (entropie, rôle du lecteur, mandat de l'exécutante), `R-3527` (conception scellée), `R-3535` (contrôle de la différence des brouillons 7 et 8), `R-3556` (dernière ligne des essais fixée à « 456 passed », durée exclue), `R-3612` (texte de lecture des sondes scellé), `R-3614` (mot de Lazar pour la création, redit dans la session exécutante), `R-3619` et `R-3622` (défaut du lanceur trouvé aux contrôles à blanc ; premier commit de lancement laissé sans suite), `R-3625` (correctif du lanceur), `R-3630` (contre-lecture du correctif, « AUTORISABLE » ; depuis cette ligne, le commit du code revu est `@@COMMIT_CODE_IIB@@`) et `R-3635` (commit de lancement et contrôles à blanc conformes) ; "
            "en partie seulement, les lignes `R-3571` et `R-3572` ; et, par recherche, le début des lignes qui nomment le saboteur à budget depuis `R-3476`.\n"
            "- **Pièces citées**"
        ),
    },
    {
        "nom": "B9-3-pieces", "changement": 3, "lieu": "en-tête, pièces citées : le contrôle court de `ec3b0329`",
        "avant": "contrôle court de la tête `ec3b0329`, commit du code revu, `docs/notes/barreau8-iib-v1/controle-court-code-iib-v7-v1.md`",
        "apres": "contrôle court de la tête `ec3b0329`, commit du code revu d'alors, `docs/notes/barreau8-iib-v1/controle-court-code-iib-v7-v1.md`",
    },
    {
        "nom": "B9-1e", "changement": 1, "lieu": "en-tête, pièces citées au brouillon 9",
        "avant": "(lignes de CC-02 à CC-05 seules).\n- **Code lu**",
        "apres": (
            "(lignes de CC-02 à CC-05 seules). "
            "Au brouillon 9 : conception scellée, `@@CHEMIN_CONCEPTION_IIB@@` (`@@EMPREINTE_CONCEPTION_IIB@@`, `R-3527` ; jamais ouverte par le rédacteur, pas même par programme : empreinte lue dans son compagnon `.sha256`, égale à celle que porte la configuration) ; "
            "configuration de la course au commit de lancement, `@@CHEMIN_CONFIG_IIB@@` (`@@EMPREINTE_CONFIG@@`, recalculée par `git show @@COMMIT_LANCEMENT@@:@@CHEMIN_CONFIG_IIB@@ | sha256sum`) ; "
            "contre-lecture du correctif du lanceur, `docs/notes/barreau8-iib-v1/contre-lecture-correctif-lanceur-taches-f9a8aaeb-v1.md` (`@@P:contre-lecture@@`) ; "
            "mandat de l'exécutante, `registres/iib-executante/mandat-executante-iib-v1.md` (`@@P:mandat@@`) ; "
            "pièces de l'exécutante, lues sur sa branche `claude/iib-executante-v1` à sa tête `@@TETE_EXECUTANTE@@`, chacune recalculée et égale à son compagnon `.sha256` : "
            "ses journaux `registres/iib-executante/journal-v1.md` (`@@P:journal-v1@@`), `registres/iib-executante/journal-v5.md` (`@@P:journal-v5@@`) et `registres/iib-executante/journal-v6.md` (`@@P:journal-v6@@`), les journaux v2 à v4, lus aussi, ne servant pas de source ici ; "
            "sous `registres/iib-executante/blanc-836c7ccc-v1/` : `empreintes-code-iib-836c7ccc-v1.txt` (`@@P:empreintes-code@@`), `journal-blanc-836c7ccc-v1.txt` (`@@P:journal-blanc@@`), `suite-ciblee-v1-836c7ccc-v1.txt` (`@@P:suite-v1@@`), `suite-ciblee-v2-836c7ccc-v1.txt` (`@@P:suite-v2@@`), `difference-configuration-968a5151-vers-836c7ccc-v1.txt` (`@@P:difference-config@@`) et `lancement-controles-836c7ccc-v1.txt` (`@@P:lancement-controles@@`) ; "
            "sous `registres/iib-executante/blanc-ec3b0329-v1/` : `journal-blanc-ec3b0329-v1.txt` (`@@P:journal-blanc-ec3b@@`) et `journal-blanc-extraction-run-ec3b0329-v2.txt` (`@@P:journal-extraction-ec3b@@`) ; "
            "sous `registres/iib-executante/blanc-968a5151-v1/` : `journal-blanc-968a5151-v1.txt` (`@@P:journal-blanc-968a@@`) ; "
            "texte de lecture des sondes du barreau 8, `prereg/lecture-sondes-barreau8-v1.md` (`@@P:sondes@@`), **jamais ouvert par le rédacteur** : empreinte recalculée une fois par programme, sans affichage, et égale à son compagnon ; ligne `SCELLEMENT-SONDES-IIB` du registre `registres/sondes-iib-v1.md` comptée une fois, sans être affichée.\n"
            "- **Code lu**"
        ),
    },
    {
        "nom": "B9-1f", "changement": 1, "lieu": "en-tête, code lu au brouillon 9 ; règle de lecture « à `ec3b0329` »",
        "avant": "le lanceur et l'amorce (`scripts/lancer_iib_v1.sh`, `scripts/amorce_instance_iib_v1.sh`) ; aucun essai rejoué.\n",
        "apres": (
            "le lanceur et l'amorce (`scripts/lancer_iib_v1.sh`, `scripts/amorce_instance_iib_v1.sh`) ; aucun essai rejoué. "
            "Au brouillon 9 : **le commit du code revu est `@@COMMIT_CODE_IIB@@`, sur la branche `@@BRANCHE_CODE_IIB@@`** (`R-3625`, `R-3630`) : c'est le commit `ec3b0329cd59db676007bd6c9ea3f0c36cf3ce95`, dont il est l'enfant direct, plus le correctif du seul lanceur `scripts/lancer_iib_v1.sh` ; la différence entre les deux commits ne porte que sur trois fichiers, `scripts/lancer_iib_v1.sh`, `scripts/tests-cibles-iib-v2.txt` et `tests/test_iib_taches_v2.py` (`git diff`, rejoué par le rédacteur : 185 lignes, `faa7f33feeded870266624c236d926948027f0f4f82977d4cb98ad7861f7cb08`). "
            "**Règle de lecture de ce texte** : « commit du code revu » y désigne désormais `f9a8aaeb` ; là où le texte écrit « à `ec3b0329` », « tête `ec3b0329` » ou « code revu d'alors », il rapporte un contrôle, une lecture ou une vérification faits à ce commit, cités tels qu'ils ont été faits ; ils valent au commit du code revu pour tout fichier autre que le lanceur : les 33 autres fichiers du code ont la même empreinte aux deux commits (§ 11). "
            "Le **commit de lancement** est `@@COMMIT_LANCEMENT@@`, enfant direct du commit du code revu, sur la même branche (`R-3635`). "
            "Le rédacteur du brouillon 9 a lu au code, au commit de lancement : le lanceur `scripts/lancer_iib_v1.sh` en entier, pour les commandes du § 5 ; dans l'amorce `scripts/amorce_instance_iib_v1.sh`, trouvées par recherche de mots, les lignes du nombre d'essais attendu et de la liste des essais (l. 315 et 371-393) ; la différence du lanceur entre `ec3b0329` et `f9a8aaeb` ; il a recalculé les empreintes des 34 fichiers du code aux trois commits ; aucun essai rejoué, aucun modèle chargé.\n"
        ),
    },
    {
        "nom": "B9-1g", "changement": 1, "lieu": "section neuve, placée avant « Ce que le brouillon 8 change »",
        "avant": "## Ce que le brouillon 8 change (détail : `differences-brouillon7-vers-8-v1.md`), et ce que le brouillon 7 avait changé",
        "apres": (
            "## Ce que le brouillon 9 change (détail : `differences-brouillon8-vers-9-v1.md`)\n"
            "\n"
            "- **Marqueurs remplis** (étape 7 du § 4) : les 13 marqueurs encore ouverts au brouillon 8 sont remplis. Douze sont des marqueurs de la configuration : chacun reçoit la valeur que la configuration du commit de lancement porte pour lui, prise par programme, sauf `EMPREINTE_CONFIG_IIB`, que la configuration ne peut pas porter et qui reçoit l'empreinte recalculée de la configuration à ce commit. Le treizième, `COMMIT_LANCEMENT_IIB`, propre à l'ordre, reçoit le commit de lancement. Il ne reste aucun marqueur entre chevrons doubles dans ce texte (§ 11).\n"
            "- **Code revu** : `@@COMMIT_CODE_IIB@@` sur `@@BRANCHE_CODE_IIB@@`, soit `ec3b0329` plus le correctif du seul lanceur (`R-3625` ; contre-lecture « AUTORISABLE », `R-3630`). Un premier commit de lancement, `968a5151c5eb31014114e5093ba675a46fcd5414` sur `prep/iib-code-v3`, a été fait puis abandonné, sans suite : aux contrôles à blanc, le contrôle « aucune tâche commune » du lanceur sortait en code 2 (`R-3619`, `R-3622`). Les contrôles et vérifications faits à `ec3b0329` restent cités à `ec3b0329` (règle de lecture : ligne « Code lu »).\n"
            "- **Commit de lancement** : `@@COMMIT_LANCEMENT@@`, enfant direct du commit du code revu, qui n'ajoute que la configuration et son sceau (`R-3635`). Contrôles à blanc à ce commit : conformes, code 0.\n"
            "- **§ 4** : étapes 4 à 6 dites faites, avec leurs pièces ; les contrôles à blanc ont été délégués à l'exécutante par son mandat, écart déclaré à la lettre du brouillon 8 ; trois écarts relevés à l'étape 6.\n"
            "- **§ 5** : branche du code, commit du code revu, commit de lancement et chemin de la configuration écrits dans les commandes, relues contre le lanceur au commit de lancement.\n"
            "- **Texte de lecture des sondes** : scellé le 2026-11-19 à 06:32:25Z, avant toute création de cette course (`R-3612`) ; dit au § 8 et au § 13.\n"
            "- **Exclus de la lecture des sondes** (§ 8) : quatre ajouts, chacun avec sa source.\n"
            "- **§ 11** : table des états mise à jour ; table neuve des valeurs à l'octet, écrite par programme depuis la configuration et comparée à elle par un second programme ; comptes refaits par programme.\n"
            "\n"
            "## Ce que le brouillon 8 change (détail : `differences-brouillon7-vers-8-v1.md`), et ce que le brouillon 7 avait changé"
        ),
    },
    # ------------------------------------------------------------------ § 1
    {
        "nom": "B9-2a", "changement": 2, "lieu": "§ 1, ligne « Conception, consigne, devis »",
        "avant": "| Conception, consigne, devis | `<<CHEMIN_CONCEPTION_IIB>>` (`<<EMPREINTE_CONCEPTION_IIB>>`) ;",
        "apres": "| Conception, consigne, devis | `@@CHEMIN_CONCEPTION_IIB@@` (`@@EMPREINTE_CONCEPTION_IIB@@`) ;",
    },
    {
        "nom": "B9-3a", "changement": 3, "lieu": "§ 1, ligne « Code de (ii-b) »",
        "avant": "| Code de (ii-b) | commit du code revu `ec3b0329cd59db676007bd6c9ea3f0c36cf3ce95` sur `prep/iib-code-v3` (contrôle court `064b8b9c…4af7`, « autorisable », `R-3497`), empreintes `<<EMPREINTES_CODE_IIB>>` ; il porte les corrections du relais et de la poussée (§ 4 quater) : il descend, sur la même branche, du commit `a31b8970fedb745c993fe23df18bba4a2d9e3cf4` (contrôle court `02962a4a…c3a2`), vérifié par le rédacteur (`git merge-base --is-ancestor`) : `COMMIT_CORRECTIONS_RELAIS_POUSSEE_IIB` (§ 11) est rempli sans réserve ; **commit de lancement** `<<COMMIT_LANCEMENT_IIB>>` : enfant direct du commit du code revu, même branche, qui n'ajoute que la configuration et son sceau |",
        "apres": (
            "| Code de (ii-b) | commit du code revu `@@COMMIT_CODE_IIB@@` sur `@@BRANCHE_CODE_IIB@@` : enfant direct du commit `ec3b0329cd59db676007bd6c9ea3f0c36cf3ce95` (code revu d'alors, sur `prep/iib-code-v3` ; contrôle court `064b8b9c…4af7`, « autorisable », `R-3497`), auquel il n'ajoute que le correctif du seul lanceur `scripts/lancer_iib_v1.sh` et ses essais (`R-3625` ; contre-lecture neuve, « AUTORISABLE », `docs/notes/barreau8-iib-v1/contre-lecture-correctif-lanceur-taches-f9a8aaeb-v1.md`, `@@P:contre-lecture@@`, `R-3630`) ; "
            "empreintes : § 11, bloc « Valeur de `EMPREINTES_CODE_IIB` » (34 fichiers ; recalculées par le rédacteur du brouillon 9 au commit du code revu et au commit de lancement : 34 égales sur 34) ; "
            "il porte les corrections du relais et de la poussée (§ 4 quater) : `ec3b0329` descend, sur `prep/iib-code-v3`, du commit `a31b8970fedb745c993fe23df18bba4a2d9e3cf4` (contrôle court `02962a4a…c3a2`), vérifié par le rédacteur (`git merge-base --is-ancestor`), et de nouveau, pour le commit du code revu, par le rédacteur du brouillon 9 : `COMMIT_CORRECTIONS_RELAIS_POUSSEE_IIB` (§ 11) est rempli sans réserve ; "
            "**commit de lancement** `@@COMMIT_LANCEMENT@@` : enfant direct du commit du code revu, même branche, qui n'ajoute que la configuration et son sceau (`R-3635` ; parent et fichiers du commit relus par le rédacteur du brouillon 9) ; "
            "un premier commit de lancement, `968a5151c5eb31014114e5093ba675a46fcd5414` sur `prep/iib-code-v3`, enfant direct de `ec3b0329`, a été fait puis abandonné, sans suite (`R-3619`, `R-3622`) |"
        ),
    },
    {
        "nom": "B9-3b", "changement": 3, "lieu": "§ 1, ligne « Essais »",
        "avant": "relue au commit du code revu `ec3b0329` : inchangée, recalculée par le rédacteur avec `git show ec3b0329:scripts/tests-cibles-iib-v1.txt | sha256sum`, et égale à celle que l'amorce porte à ce commit) ; dernière ligne sur processeur `<<DERNIERE_LIGNE_TESTS_IIB_PROCESSEUR>>`, rejouée à l'identique au commit de lancement ; jouée d'office par l'amorce ; `IIB_TESTS_ATTENDUS` vide |",
        "apres": (
            "relue au commit `ec3b0329`, code revu d'alors : inchangée, recalculée par le rédacteur avec `git show ec3b0329:scripts/tests-cibles-iib-v1.txt | sha256sum`, et égale à celle que l'amorce porte à ce commit ; relue de même au commit du code revu `f9a8aaeb` et au commit de lancement `836c7ccc` par le rédacteur du brouillon 9 : inchangée, et l'amorce a la même empreinte aux trois commits, `5d78e7e4b6466fd61fac423ec4dd1d9a3fb87d97c4ad99f345b624ac97beb433`) ; "
            "dernière ligne sur processeur `@@DERNIERE_LIGNE_TESTS_IIB_PROCESSEUR@@` (durée exclue, `R-3556`), rejouée à l'identique au commit de lancement : « 456 passed in 570.86s (0:09:30) », code 0 (pièce `suite-ciblee-v1-836c7ccc-v1.txt`) ; "
            "une liste v2, `scripts/tests-cibles-iib-v2.txt` (`2f531cf6be94babc70f44ac17449c4112841e3186d4e3f082b1ae53c799c19c8` ; la v1 plus `tests/test_iib_taches_v2.py`, les 13 essais du correctif), existe pour le processeur : « 469 passed » au commit de lancement, code 0 (pièce `suite-ciblee-v2-836c7ccc-v1.txt`) ; l'amorce joue la liste v1, dont elle porte l'empreinte en dur : la suite jouée sur l'instance garde 456 essais (`R-3625`) ; "
            "jouée d'office par l'amorce ; `IIB_TESTS_ATTENDUS` vide |"
        ),
    },
    {
        "nom": "B9-2b", "changement": 2, "lieu": "§ 1, ligne « Configuration »",
        "avant": "| Configuration | `<<CHEMIN_CONFIG_IIB>>` (`<<EMPREINTE_CONFIG_IIB>>`) au commit de lancement |",
        "apres": "| Configuration | `@@CHEMIN_CONFIG_IIB@@` (`@@EMPREINTE_CONFIG@@`) au commit de lancement |",
    },
    {
        "nom": "B9-2c", "changement": 2, "lieu": "§ 1, ligne « Entropie (R9) »",
        "avant": "| Entropie (R9) | `<<ENTROPIE_IIB>>`, tirée une fois par la mère par `numpy.random.SeedSequence()` **avant d'écrire la configuration**, donc avant le commit de lancement et avant le scellement de l'ordre, sans aucune donnée de la course ; consignée au registre des décisions et dans la configuration |",
        "apres": "| Entropie (R9) | `@@ENTROPIE_IIB@@`, tirée une fois par la mère par `numpy.random.SeedSequence()` **avant d'écrire la configuration**, donc avant le commit de lancement et avant le scellement de l'ordre, sans aucune donnée de la course ; consignée au registre des décisions (ligne `R-3525`) et dans la configuration |",
    },
    {
        "nom": "B9-2d", "changement": 2, "lieu": "§ 1, ligne « Outil de location »",
        "avant": "| Outil de location | `vastai==<<VERSION_VASTAI>>`, relevé",
        "apres": "| Outil de location | `vastai==@@VERSION_VASTAI@@`, relevé",
    },
    {
        "nom": "B9-2e", "changement": 2, "lieu": "§ 1, ligne « Exécutante »",
        "avant": "| Exécutante | `<<EXECUTANTE_IIB>>` ; mot de Lazar pour la création : `<<MOT_LAZAR_CREATION_IIB>>` (référence de la ligne du registre où la mère l'a consigné ; Lazar le redit dans la session qui dépense) |",
        "apres": "| Exécutante | `@@EXECUTANTE_IIB@@` ; mot de Lazar pour la création : `@@MOT_LAZAR_CREATION_IIB@@` (référence de la ligne du registre où la mère l'a consigné ; Lazar l'a redit dans la session qui dépense, le 2026-11-19 à 06:30:18Z, verbatim « go création de la course », d'après cette ligne ; il l'avait donné d'abord dans la session mère : `registres/go.md`, ligne `GO-2026-11-19-04`) |",
    },
    # ------------------------------------------------------------------ § 2
    {
        "nom": "B9-3c", "changement": 3, "lieu": "§ 2, nombres de la lecture (2) : commit nommé",
        "avant": "État au commit du code revu `ec3b0329` : le code garde pour la lecture (2)",
        "apres": "État au commit `ec3b0329`, code revu d'alors : le code garde pour la lecture (2)",
    },
    {
        "nom": "B9-3d", "changement": 3, "lieu": "§ 2, nombres de la lecture (2) : inchangés au commit du code revu",
        "avant": "tout autre nombre demanderait un code neuf, donc un autre commit du code revu. Les versions",
        "apres": "tout autre nombre demanderait un code neuf, donc un autre commit du code revu. Le commit du code revu `f9a8aaeb` ne change pas ces nombres : `configuration_v1.py` y a la même empreinte qu'à `ec3b0329` (§ 11), et la configuration du commit de lancement les porte à sa clé `lecture_2` (lus par programme par le rédacteur du brouillon 9). Les versions",
    },
    {
        "nom": "B9-3e", "changement": 3, "lieu": "§ 2, valeurs libres, ligne « code »",
        "avant": "| `code` | `branche` « prep/iib-code-v3 » ; `commit` = commit du code revu (la configuration ne peut pas citer le commit qui la contient) |",
        "apres": "| `code` | `branche` « @@BRANCHE_CODE_IIB@@ » ; `commit` = commit du code revu, `@@COMMIT_CODE_IIB@@` (la configuration ne peut pas citer le commit qui la contient) |",
    },
    # ------------------------------------------------------------------ § 3
    {
        "nom": "B9-3f", "changement": 3, "lieu": "§ 3, titre : commit nommé",
        "avant": "CC-01, majeur ; au commit du code revu `ec3b0329` : CC-02 à CC-05 corrigés",
        "apres": "CC-01, majeur ; au commit `ec3b0329`, code revu d'alors : CC-02 à CC-05 corrigés",
    },
    {
        "nom": "B9-3g", "changement": 3, "lieu": "§ 3, titre : état au commit du code revu",
        "avant": "tête « autorisable » sans bloquant, majeur ni mineur (`R-3497`))\n",
        "apres": "tête « autorisable » sans bloquant, majeur ni mineur (`R-3497`) ; au commit du code revu `f9a8aaeb` : les mêmes gardes, plus le correctif du contrôle « aucune tâche commune » du lanceur, éprouvé sur la forme réelle des fichiers de tâches, cas sain et artefacts (`tests/test_iib_taches_v2.py`, 13 essais ; `R-3625`, `R-3630`))\n",
    },
    {
        "nom": "B9-3h", "changement": 3, "lieu": "§ 3, garde « Tâches disjointes »",
        "avant": "- **Tâches disjointes** : aucune tâche de réserve dans l'évaluation → sinon aucune création.\n",
        "apres": "- **Tâches disjointes** : aucune tâche de réserve dans l'évaluation → sinon aucune création. À `ec3b0329`, ce contrôle du lanceur sortait en code 2 sur les fichiers réels, qui portent la liste des tâches sous `resultat.taches` : il attendait une liste au premier niveau du fichier (défaut trouvé aux contrôles à blanc, avant toute dépense, `R-3619`, `R-3622`). Corrigé au commit du code revu `f9a8aaeb` : même lecture que la course (`resultat.taches` si présent, sinon `taches`), refus en code 2 avec son motif (`R-3625`). L'exécutante a vérifié à part, par programme : 32 tâches de réserve, 64 d'évaluation, aucune commune (son journal v5).\n",
    },
    # ------------------------------------------------------------------ § 4
    {
        "nom": "B9-3i", "changement": 3, "lieu": "§ 4 étape 2 : défaut, correctif, commit du code revu",
        "avant": "; **commit du code revu** `ec3b0329cd59db676007bd6c9ea3f0c36cf3ce95` : il porte CC-01 (levé, `R-3485`), CC-02 à CC-05 (corrigés, vérification courte `4ef2101e…af8e`), le portage, P6-01 et P6-02 ; empreintes `<<EMPREINTES_CODE_IIB>>`, dernière ligne `<<DERNIERE_LIGNE_TESTS_IIB_PROCESSEUR>>` (à ce commit, le contrôle court rapporte pour la suite ciblée 456 essais réussis, aucun saut) ; répétition jouet identique à l'octet à ce commit (48 fichiers comparés, 0 différent ; configuration jouet `2e65c31b…`, entropie 20261118, d'après le contrôle court ; l'empreinte entière de cette configuration n'est écrite dans aucune pièce lue par le rédacteur).\n",
        "apres": (
            "; **commit `ec3b0329cd59db676007bd6c9ea3f0c36cf3ce95`, code revu d'alors** : il porte CC-01 (levé, `R-3485`), CC-02 à CC-05 (corrigés, vérification courte `4ef2101e…af8e`), le portage, P6-01 et P6-02 ; à ce commit, le contrôle court rapporte pour la suite ciblée 456 essais réussis, aucun saut, et l'exécutante relève au processeur « 456 passed », code 0 (`R-3556`) ; répétition jouet identique à l'octet à ce commit (48 fichiers comparés, 0 différent ; configuration jouet `2e65c31b…`, entropie 20261118, d'après le contrôle court ; l'empreinte entière de cette configuration n'est écrite dans aucune pièce lue par le rédacteur) ; "
            "**défaut trouvé aux contrôles à blanc** du premier commit de lancement (étape 6 ; `R-3619`, `R-3622`) : sur les fichiers réels des tâches, le contrôle « aucune tâche commune » du lanceur `scripts/lancer_iib_v1.sh` sortait en code 2 ; rien créé, rien cherché, rien dépensé ; "
            "**correctif du seul lanceur** : commit `@@COMMIT_CODE_IIB@@` sur la branche neuve `@@BRANCHE_CODE_IIB@@`, enfant direct de `ec3b0329` (`R-3625`) ; trois fichiers : le lanceur, la liste neuve `scripts/tests-cibles-iib-v2.txt` (la v1 plus une ligne) et `tests/test_iib_taches_v2.py` (13 essais, dont 11 échouent sur le lanceur d'avant) ; ni le module partagé qui lit les tâches pour la course ni la répétition jouet ne sont touchés ; "
            "contre-lecture neuve par un lecteur d'un autre modèle que le développeur : **« AUTORISABLE »**, deux réserves mineures, non bloquantes (`docs/notes/barreau8-iib-v1/contre-lecture-correctif-lanceur-taches-f9a8aaeb-v1.md`, `@@P:contre-lecture@@` ; `R-3630`) ; "
            "**commit du code revu : `@@COMMIT_CODE_IIB@@`** ; il porte tout ce que portait `ec3b0329`, plus ce correctif ; empreintes : § 11, bloc « Valeur de `EMPREINTES_CODE_IIB` » (34 fichiers, relevées par l'exécutante, pièce `empreintes-code-iib-836c7ccc-v1.txt` ; seule celle du lanceur diffère de `ec3b0329`) ; "
            "dernière ligne `@@DERNIERE_LIGNE_TESTS_IIB_PROCESSEUR@@` pour la liste v1, celle que joue l'instance, et « 469 passed » pour la liste v2 : au commit du code revu d'après la contre-lecture (`R-3630`), au commit de lancement d'après les pièces de l'exécutante (`suite-ciblee-v1-836c7ccc-v1.txt`, `suite-ciblee-v2-836c7ccc-v1.txt`).\n"
        ),
    },
    {
        "nom": "B9-2f", "changement": 2, "lieu": "§ 4 étape 3 : conception",
        "avant": "conception (`<<CHEMIN_CONCEPTION_IIB>>`, `<<EMPREINTE_CONCEPTION_IIB>>`), qui porte",
        "apres": "conception (`@@CHEMIN_CONCEPTION_IIB@@`, `@@EMPREINTE_CONCEPTION_IIB@@` ; scellée, `R-3527`), qui porte",
    },
    {
        "nom": "B9-4a", "changement": 4, "lieu": "§ 4 étape 4 : titre",
        "avant": "4. **Faits de la remise, connus de la mère avant la configuration** :\n",
        "apres": "4. **Faits de la remise, connus de la mère avant la configuration** — **étape faite** (source à chaque point) :\n",
    },
    {
        "nom": "B9-2g", "changement": 2, "lieu": "§ 4 étape 4 : exécutante, lecteur, outil, mot de Lazar",
        "avant": "   - Exécutante désignée (`<<EXECUTANTE_IIB>>` : nom de la session) ; lecteur désigné (`<<LECTEUR_IIB>>` : rôle) ; version de l'outil relevée (`<<VERSION_VASTAI>>`) ; mot de Lazar pour la création consigné (`<<MOT_LAZAR_CREATION_IIB>>`).\n",
        "apres": "   - Exécutante désignée (`@@EXECUTANTE_IIB@@` : nom de la session) ; lecteur désigné (`@@LECTEUR_IIB@@` : rôle) ; version de l'outil relevée (`@@VERSION_VASTAI@@`) ; mot de Lazar pour la création consigné (`@@MOT_LAZAR_CREATION_IIB@@`). **Fait** : mandat de l'exécutante et rôle du lecteur, `R-3525` ; version relevée par l'exécutante, par le seul appel `vastai --version` (son journal v1) ; mot de Lazar redit dans la session exécutante et consigné, `R-3614` (`registres/go.md`, ligne `GO-2026-11-19-04`).\n",
    },
    {
        "nom": "B9-2h", "changement": 2, "lieu": "§ 4 étape 4 : longueurs de la consigne",
        "avant": "   - Longueurs de la consigne (`<<LONGUEURS_CONSIGNE_IIB>>`) mesurées au jetoniseur réel **sur processeur**, nombres seuls ; si ses fichiers ne s'obtiennent pas sans dépense : valeur déclarée « mesurées sur l'instance, au journal (§ 4 ter, J6) », nombres au compte rendu.\n",
        "apres": "   - Longueurs de la consigne (`@@LONGUEURS_CONSIGNE_IIB@@`) mesurées au jetoniseur réel **sur processeur**, nombres seuls ; si ses fichiers ne s'obtiennent pas sans dépense : valeur déclarée « mesurées sur l'instance, au journal (§ 4 ter, J6) », nombres au compte rendu. **Fait** : mesurées par l'exécutante sur processeur, au jetoniseur réel obtenu sans dépense, nombres seuls, dans l'ordre que dit son journal v1 (`R-3619`) ; la valeur déclarée n'a pas servi.\n",
    },
    {
        "nom": "B9-2i", "changement": 2, "lieu": "§ 4 étape 4 : entropie",
        "avant": "   - Entropie tirée (`<<ENTROPIE_IIB>>`) et consignée.\n",
        "apres": "   - Entropie tirée (`@@ENTROPIE_IIB@@`) et consignée. **Fait** : tirée par la mère le 2026-11-18 à 23:26:12Z, avant toute configuration (`R-3525`).\n",
    },
    {
        "nom": "B9-4b", "changement": 4, "lieu": "§ 4 étape 5 : commit de lancement fait ; premier commit abandonné",
        "avant": "5. **Configuration** (§ 2) écrite, scellée, commise **seule** dans un enfant direct du commit du code revu, sur `prep/iib-code-v3`, poussé : **commit de lancement** `<<COMMIT_LANCEMENT_IIB>>`. Il contient `registres/go.md` avec la ligne `GO-2026-11-10-08` (présente une fois à `d88e3d94`), les tâches, la consigne, `prereg/P3-consignes-v1.md` et leurs sceaux.\n",
        "apres": (
            "5. **Configuration** (§ 2) écrite, scellée, commise **seule** dans un enfant direct du commit du code revu, sur `@@BRANCHE_CODE_IIB@@`, poussé : **commit de lancement** `@@COMMIT_LANCEMENT@@`. Il contient `registres/go.md` avec la ligne `GO-2026-11-10-08` (présente une fois à `d88e3d94`, et une fois au commit de lancement), les tâches, la consigne, `prereg/P3-consignes-v1.md` et leurs sceaux. "
            "**Étape faite** (`R-3635` ; journal v6 de l'exécutante) : configuration `@@CHEMIN_CONFIG_IIB@@` (`@@EMPREINTE_CONFIG@@`), écrite et scellée par l'exécutante ; la garde du code (`iib/session_v1 config`) la dit conforme (mode reel, variante B) ; le commit de lancement a pour parent direct le commit du code revu et n'ajoute que la configuration et son sceau (rejoué par le rédacteur du brouillon 9) ; poussé ; tête de la branche distante vérifiée par la mère, et égale à ce commit au rapatriement fait par le rédacteur du brouillon 9. "
            "**Histoire, sans suite** : un premier commit de lancement, `968a5151c5eb31014114e5093ba675a46fcd5414` sur `prep/iib-code-v3`, enfant direct de `ec3b0329`, portait la même configuration à cinq valeurs près (`ebab1fb051890def13c2b7981c291c7cc2cea0b797bff6255b95066f5ad94fb7`, recalculée par le rédacteur du brouillon 9 ; diffèrent : `code.branche`, `code.commit`, et les marqueurs `BRANCHE_CODE_IIB`, `COMMIT_CODE_IIB` et `EMPREINTES_CODE_IIB`, ce dernier par le commit qu'il nomme et par la seule empreinte du lanceur ; pièce `difference-configuration-968a5151-vers-836c7ccc-v1.txt`) ; il a été abandonné après le défaut du lanceur (étape 2 ; `R-3619`, `R-3622`) et reste en place sur `prep/iib-code-v3`, sans suite.\n"
        ),
    },
    {
        "nom": "B9-4c", "changement": 4, "lieu": "§ 4 étape 6 : contrôles à blanc faits ; délégation ; trois écarts",
        "avant": "sont **jouées à blanc d'abord**, sans dépense, par la mère : une première fois dès le commit du code revu `ec3b0329` (le couple de la contre-lecture disait « dès la tête `a31b8970` », tête d'alors ; leur forme ne dépend pas du commit de lancement), puis au commit de lancement, avant le scellement de l'ordre ; issue consignée (codes de sortie, place prise, fichiers extraits) ; tout écart → forme corrigée et ordre en version nouvelle (O-M5 ; contrôle court, § 4, point 1).\n",
        "apres": (
            "sont **jouées à blanc d'abord**, sans dépense : une première fois dès le commit `ec3b0329`, code revu d'alors (le couple de la contre-lecture disait « dès la tête `a31b8970` », tête d'alors ; leur forme ne dépend pas du commit de lancement), puis au commit de lancement, avant le scellement de l'ordre ; issue consignée (codes de sortie, place prise, fichiers extraits) ; tout écart → forme corrigée et ordre en version nouvelle (O-M5 ; contrôle court, § 4, point 1). "
            "**Écart déclaré à la lettre du brouillon 8**, qui attribuait ces jeux à blanc à la mère : la mère les a délégués à l'exécutante par son mandat (`registres/iib-executante/mandat-executante-iib-v1.md`, `@@P:mandat@@`, § 3 point 6 ; `R-3525`). "
            "**Étape faite**, en trois temps, chacun sans instance, sans recherche d'offre et sans dépense (journaux v1, v5 et v6 de l'exécutante ; pièces à la ligne « Pièces citées ») :\n"
            "   - **à `ec3b0329`** (journal v1) : extractions réduites de `main` et du code en code 0 ; extraction des fichiers du run jouée sur un dépôt jouet fidèle, la branche du run n'existant pas encore : toutes les commandes en code 0, 2 fichiers listés, 2 vérifiés, aucun absent ni sans compagnon ; artefact « fichier listé absent » : `verifier` en code 1 ; place prise : 7,3 Mo (`main`), 390 Mo (code), 538 Mo (code et dossiers du run) ;\n"
            "   - **au premier commit de lancement `968a5151`**, abandonné depuis (journal v5 ; `R-3619`) : garde de la configuration en code 0 ; suite ciblée « 456 passed » ; extractions réduites en code 0 ; contrôles du lanceur en **code 2**, sur le contrôle « aucune tâche commune » (étape 2) ;\n"
            "   - **au commit de lancement `@@COMMIT_LANCEMENT@@`** (journal v6 ; `R-3635`) : garde de la configuration conforme ; suite ciblée rejouée, même dernière ligne, « 456 passed », code 0 (liste v2 : « 469 passed », code 0) ; extraction réduite de `main` : clonage et extraction en code 0, ligne `GO-2026-11-10-08` comptée 1, lignes `R-3614` et `R-3630` comptées 1 chacune ; extraction réduite du code : clonage, `sparse-checkout` et extraction en code 0, tête distante de `@@BRANCHE_CODE_IIB@@` égale au commit de lancement, parent égal au commit du code revu, deux fichiers dans le commit (la configuration et son sceau), ligne d'accord comptée 1 au commit, branche du run absente (code 2, attendu) ; contrôles du lanceur (`controles-explo`, sans outil de location) : **code 0, « CONTRÔLES CONFORMES »**, `lancement.txt` écrit (copie : pièce `lancement-controles-836c7ccc-v1.txt`) ; place prise : 7,3 Mo (`main`), 390 Mo (code), 0,4 Mo (dossier des contrôles) ; place libre avant : 14 260 328 ko, plus que les 3 Go exigés ;\n"
            "   - **relecture des valeurs libres** : faite par programme par le rédacteur du brouillon 9, qui n'a pas écrit la configuration : les valeurs libres de la table du § 2, transcrites dans le programme de comparaison, sont égales, clé par clé, à celles de la configuration du commit de lancement (programme et sortie : § 11) ; **commandes du § 5** : relues par le même rédacteur au commit de lancement (§ 5) ;\n"
            "   - **trois écarts relevés par le rédacteur du brouillon 9, déclarés, portés à la mère** : **(i)** l'extraction des fichiers du run (forme de l'étape 5) a été jouée à blanc à `ec3b0329` seulement, sur un dépôt jouet ; elle n'est pas rejouée au commit de lancement ; sa forme ne dépend pas de ce commit (dit plus haut) ; **(ii)** la commande `--verifier-go-seulement` de l'étape 1 du § 5 n'apparaît dans aucun journal des contrôles à blanc ; les contrôles du lanceur vérifient la même ligne d'accord par la même fonction, et leur message le dit (« GO-2026-11-10-08 conforme ») ; **(iii)** la pièce `lancement-controles-836c7ccc-v1.txt` porte `tests_attendus 456` : l'exécutante a joué ces contrôles avec un nombre d'essais attendu de 456, alors que cet ordre fixe `IIB_TESTS_ATTENDUS` vide (§ 1, § 5 étape 1). Aux contrôles, le lanceur ne lit de cette variable que sa forme et la recopie dans `lancement.txt` : l'issue « CONTRÔLES CONFORMES » n'en dépend pas. À la création, il la passe à l'instance : non vide, l'amorce arrête la course si la dernière ligne des essais n'est pas « 456 passed » ; vide, elle n'exige que la réussite de la suite. À la lettre de l'étape 1 du § 5, l'exécutante rejoue les contrôles dans un dossier neuf, avec les variables de cet ordre, et c'est ce dossier neuf que lit la création.\n"
        ),
    },
    {
        "nom": "B9-4d", "changement": 4, "lieu": "§ 4 étape 7 : marqueurs remplis",
        "avant": "7. **Marqueurs de l'ordre remplis**, vérification courte de l'ordre (autre lecteur), **scellement**.",
        "apres": "7. **Marqueurs de l'ordre remplis**, vérification courte de l'ordre (autre lecteur), **scellement**. **Marqueurs : remplis au brouillon 9**, et comparés par programme à la configuration du commit de lancement (§ 11) ; restent la vérification courte et le scellement.",
    },
    # ------------------------------------------------------------------ § 4 bis, § 4 quater
    {
        "nom": "B9-3j", "changement": 3, "lieu": "§ 4 bis point 6 : code corrigé",
        "avant": "- **avec le code corrigé** (commit du code revu `ec3b0329`, qui descend de `a31b8970`) :",
        "apres": "- **avec le code corrigé** (commit du code revu `f9a8aaeb`, enfant direct de `ec3b0329`, qui descend de `a31b8970`) :",
    },
    {
        "nom": "B9-3k", "changement": 3, "lieu": "§ 4 quater, titre",
        "avant": "contrôlée, puis commit du code revu `ec3b0329cd59db676007bd6c9ea3f0c36cf3ce95`, « autorisable », `R-3497`)\n",
        "apres": "contrôlée, puis commit `ec3b0329cd59db676007bd6c9ea3f0c36cf3ce95`, « autorisable », `R-3497`, code revu d'alors ; le commit du code revu `@@COMMIT_CODE_IIB@@`, son enfant direct, ne touche ni le relais ni la poussée : l'amorce et `lanceur_v1.py` y ont les mêmes empreintes, § 11)\n",
    },
    {
        "nom": "B9-3l", "changement": 3, "lieu": "§ 4 quater, état à `a31b8970` : commit du code revu",
        "avant": "le commit du code revu, `COMMIT_CODE_IIB`, est `ec3b0329cd59db676007bd6c9ea3f0c36cf3ce95`, `R-3497`)",
        "apres": "le commit du code revu d'alors était `ec3b0329cd59db676007bd6c9ea3f0c36cf3ce95`, `R-3497` ; le commit du code revu, `COMMIT_CODE_IIB`, est depuis `@@COMMIT_CODE_IIB@@`, son enfant direct, `R-3630`)",
    },
    # ------------------------------------------------------------------ § 5
    {
        "nom": "B9-5a", "changement": 5, "lieu": "§ 5, consignes permanentes : relecture des commandes",
        "avant": "Commandes vérifiées contre `scripts/lancer_iib_v1.sh` à `d88e3d94` ; relues au commit de lancement (§ 4 étape 6).\n",
        "apres": "Commandes vérifiées contre `scripts/lancer_iib_v1.sh` à `d88e3d94` ; relues au commit de lancement (§ 4 étape 6) : par le rédacteur du brouillon 9, contre le lanceur à ce commit (`3279e3dcc631519e574c2011f9f143d956d3b668c729a176cd8efc0e99dece8f`) et contre la pièce `lancement-controles-836c7ccc-v1.txt` ; sous-commandes, ordre des arguments, variables exigées, messages et codes de sortie conformes ; un écart, sur le nombre d'essais attendu (§ 4 étape 6, écart (iii)).\n",
    },
    {
        "nom": "B9-5b", "changement": 5, "lieu": "§ 5 étape 1 : version de l'outil",
        "avant": "- `vastai --version` → `<<VERSION_VASTAI>>` ; sinon arrêt.",
        "apres": "- `vastai --version` → `@@VERSION_VASTAI@@` ; sinon arrêt.",
    },
    {
        "nom": "B9-5c", "changement": 5, "lieu": "§ 5 étape 1 : extraction réduite du code",
        "avant": "--single-branch --branch prep/iib-code-v3 https://github.com/lciric/controle-ia-travail.git \"$W/depot\"` ; `git -C \"$W/depot\" sparse-checkout set --no-cone /scripts/ /src/ /.claude/ /registres/` ; `git -C \"$W/depot\" checkout --detach <<COMMIT_LANCEMENT_IIB>>` ; la branche distante `refs/remotes/origin/prep/iib-code-v3` doit exister",
        "apres": "--single-branch --branch @@BRANCHE_CODE_IIB@@ https://github.com/lciric/controle-ia-travail.git \"$W/depot\"` ; `git -C \"$W/depot\" sparse-checkout set --no-cone /scripts/ /src/ /.claude/ /registres/` ; `git -C \"$W/depot\" checkout --detach @@COMMIT_LANCEMENT@@` ; la branche distante `refs/remotes/origin/@@BRANCHE_CODE_IIB@@` doit exister",
    },
    {
        "nom": "B9-5d", "changement": 5, "lieu": "§ 5 étape 1 : parent, fichiers du commit, empreintes, ligne d'accord",
        "avant": "- `git -C \"$W/depot\" rev-parse HEAD^` = `ec3b0329cd59db676007bd6c9ea3f0c36cf3ce95` ; `git -C \"$W/depot\" diff --name-only ec3b0329cd59db676007bd6c9ea3f0c36cf3ce95 <<COMMIT_LANCEMENT_IIB>>` = la configuration et son sceau seulement ; empreintes `<<EMPREINTES_CODE_IIB>>` recalculées par `git show <<COMMIT_LANCEMENT_IIB>>:<chemin> | sha256sum` ; `git show <<COMMIT_LANCEMENT_IIB>>:registres/go.md | grep -c '^| GO-2026-11-10-08 |'` = 1 ; tout écart → arrêt.",
        "apres": "- `git -C \"$W/depot\" rev-parse HEAD^` = `@@COMMIT_CODE_IIB@@` ; `git -C \"$W/depot\" diff --name-only @@COMMIT_CODE_IIB@@ @@COMMIT_LANCEMENT@@` = la configuration et son sceau seulement ; empreintes du § 11, bloc « Valeur de `EMPREINTES_CODE_IIB` » (34 fichiers), recalculées par `git show @@COMMIT_LANCEMENT@@:<chemin> | sha256sum` ; `git show @@COMMIT_LANCEMENT@@:registres/go.md | grep -c '^| GO-2026-11-10-08 |'` = 1 ; tout écart → arrêt.",
    },
    {
        "nom": "B9-5e", "changement": 5, "lieu": "§ 5 étape 1 : variables communes",
        "avant": "IIB_BRANCHE_CODE=prep/iib-code-v3 IIB_BRANCHE=essai/iib-explo-v1",
        "apres": "IIB_BRANCHE_CODE=@@BRANCHE_CODE_IIB@@ IIB_BRANCHE=essai/iib-explo-v1",
    },
    {
        "nom": "B9-5f", "changement": 5, "lieu": "§ 5 étape 1 : contrôles du lanceur",
        "avant": "controles-explo \"$W/iib\" <<COMMIT_LANCEMENT_IIB>> <<CHEMIN_CONFIG_IIB>>`",
        "apres": "controles-explo \"$W/iib\" @@COMMIT_LANCEMENT@@ @@CHEMIN_CONFIG_IIB@@`",
    },
    {
        "nom": "B9-5g", "changement": 5, "lieu": "§ 5 étape 2 : commit et configuration passés à l'instance",
        "avant": "(`-e COMMIT=<<COMMIT_LANCEMENT_IIB>>`, `-e ECHEANCE_UTC_S=1795816800`",
        "apres": "(`-e COMMIT=@@COMMIT_LANCEMENT@@`, `-e CONFIG=@@CHEMIN_CONFIG_IIB@@`, `-e ECHEANCE_UTC_S=1795816800`",
    },
    {
        "nom": "B9-5h", "changement": 5, "lieu": "§ 5 étape 2 : marqueurs restés dans le brouillon 3",
        "avant": "jetons par leur nom, aucune variable du mandataire). L'exécuter une seule fois",
        "apres": "jetons par leur nom, aucune variable du mandataire ; le brouillon 3 y porte encore, pour le commit et pour la configuration, deux marqueurs entre chevrons doubles : leurs valeurs sont les deux premières de cette parenthèse). L'exécuter une seule fois",
    },
    {
        "nom": "B9-3m", "changement": 3, "lieu": "§ 5 étape 5 : second démarrage, commit de la relecture et ligne du lanceur",
        "avant": "relu dans le code au commit du code revu `ec3b0329` (`scripts/amorce_instance_iib_v1.sh`, l. 128-180 et 323 ; second démarrage joué en essai local, sans minuterie, par le vérificateur des brouillons 6) : l'amorce est le point d'entrée du conteneur (`scripts/lancer_iib_v1.sh`, l. 167)",
        "apres": "relu dans le code au commit `ec3b0329`, code revu d'alors (`scripts/amorce_instance_iib_v1.sh`, l. 128-180 et 323 ; second démarrage joué en essai local, sans minuterie, par le vérificateur des brouillons 6 ; l'amorce a la même empreinte au commit du code revu `f9a8aaeb`, § 11) : l'amorce est le point d'entrée du conteneur (`scripts/lancer_iib_v1.sh`, l. 167 à `ec3b0329`, l. 174 au commit du code revu)",
    },
    # ------------------------------------------------------------------ § 7, § 8
    {
        "nom": "B9-3n", "changement": 3, "lieu": "§ 7 : colonne « poussé par l'amorce »",
        "avant": "au commit `a31b8970` (contrôle court, § 4) et au commit du code revu `ec3b0329`, qui en descend**",
        "apres": "au commit `a31b8970` (contrôle court, § 4), au commit `ec3b0329`, qui en descend, et au commit du code revu `f9a8aaeb`, enfant direct de `ec3b0329`, où l'amorce est la même**",
    },
    {
        "nom": "B9-6a", "changement": 6, "lieu": "§ 8 : texte de lecture des sondes scellé",
        "avant": "Comme au brouillon 3, § 8. **Exclus de toute lecture des sondes du barreau 8** :",
        "apres": (
            "Comme au brouillon 3, § 8, où le rôle du lecteur, que le brouillon 3 porte encore en marqueur, est la valeur de `LECTEUR_IIB` (§ 11). "
            "**Depuis le brouillon 3** : son § 8 exige, avant toute lecture de sonde, un préenregistrement scellé à part, le verdict scellé de P3-bis et un accord à part ; de ces trois, le premier existe : le texte de lecture des sondes du barreau 8 est scellé depuis le 2026-11-19 à 06:32:25Z, `prereg/lecture-sondes-barreau8-v1.md` (`@@P:sondes@@`), ligne `SCELLEMENT-SONDES-IIB` du registre `registres/sondes-iib-v1.md` (`R-3612`). Ce scellement précède la création de cette course, donc toute sortie de la course ; cette course ne lit toujours aucune sonde. "
            "**Exclus de toute lecture des sondes du barreau 8** :"
        ),
    },
    {
        "nom": "B9-7", "changement": 7, "lieu": "§ 8 : exclus ajoutés au brouillon 9",
        "avant": "(mandat de la session mère, `R-3523`, suite), qui ont lu cet ordre. Le § 2 porte",
        "apres": "(mandat de la session mère, `R-3523`, suite), qui ont lu cet ordre. **Ajouts du brouillon 9**, chacun avec sa source (le registre « qui a lu quoi » fait foi) : l'exécutante de la course, qui a écrit la configuration (son mandat, § 1 ; `R-3525`) ; le développeur du correctif du lanceur (`R-3619`, `R-3625`) ; le contre-lecteur de ce correctif (en-tête de son rapport ; `R-3630`) ; le rédacteur du brouillon 9 (`R-3635`), qui a lu cet ordre et les marqueurs de la configuration. Le § 2 porte",
    },
    # ------------------------------------------------------------------ § 11
    {
        "nom": "B9-8a", "changement": 8, "lieu": "§ 11, règle de remplissage : faite",
        "avant": "la colonne de droite dit quel fait il attend et à quelle étape ce fait existe.\n",
        "apres": "la colonne de droite dit quel fait il attend et à quelle étape ce fait existe. **Fait au brouillon 9** : plus aucun marqueur n'est en attente ; la colonne de droite dit la valeur ou son lieu, et la table des valeurs à l'octet, plus bas, porte chacune des 30 valeurs.\n",
    },
    {
        "nom": "B9-8b", "changement": 8, "lieu": "§ 11, ligne `BRANCHE_CODE_IIB`",
        "avant": "| `BRANCHE_CODE_IIB` | rempli, sous réserve | `prep/iib-code-v3`, tant que le code revu reste sur cette branche |",
        "apres": "| `BRANCHE_CODE_IIB` | rempli | `@@BRANCHE_CODE_IIB@@` ; la réserve du brouillon 8 a joué : le code revu a quitté `prep/iib-code-v3`, qui garde l'état d'avant (`R-3630`) |",
    },
    {
        "nom": "B9-8c", "changement": 8, "lieu": "§ 11, ligne `EMPREINTE_LISTE_TESTS_IIB`",
        "avant": "| `EMPREINTE_LISTE_TESTS_IIB` | rempli | `847676ef…e3b6`, relue au commit du code revu `ec3b0329` : inchangée (§ 1) |",
        "apres": "| `EMPREINTE_LISTE_TESTS_IIB` | rempli | `847676ef…e3b6`, relue au commit `ec3b0329`, au commit du code revu `f9a8aaeb` et au commit de lancement : inchangée (§ 1) |",
    },
    {
        "nom": "B9-8d", "changement": 8, "lieu": "§ 11, ligne `COMMIT_CODE_IIB`",
        "avant": "| `COMMIT_CODE_IIB` | rempli | `ec3b0329cd59db676007bd6c9ea3f0c36cf3ce95` : commit du code revu, après les corrections de CC-01 à CC-05, le portage, P6-01 et P6-02 ; contrôle court « autorisable » (`064b8b9c…4af7`) ; `R-3497` |",
        "apres": "| `COMMIT_CODE_IIB` | rempli | `@@COMMIT_CODE_IIB@@` : commit du code revu, sur `@@BRANCHE_CODE_IIB@@` ; enfant direct de `ec3b0329cd59db676007bd6c9ea3f0c36cf3ce95` (code revu d'alors, après les corrections de CC-01 à CC-05, le portage, P6-01 et P6-02 ; contrôle court « autorisable », `064b8b9c…4af7` ; `R-3497`), plus le correctif du seul lanceur (`R-3625` ; contre-lecture « AUTORISABLE », `R-3630`) |",
    },
    {
        "nom": "B9-8e", "changement": 8, "lieu": "§ 11, ligne des empreintes du code et de la dernière ligne des essais",
        "avant": "| `EMPREINTES_CODE_IIB`, `DERNIERE_LIGNE_TESTS_IIB_PROCESSEUR` | en attente | à relever par la mère au commit du code revu `ec3b0329` (§ 4 étape 2) ; à ce commit, le contrôle court rapporte pour la suite ciblée 456 essais réussis, aucun saut |",
        "apres": "| `EMPREINTES_CODE_IIB`, `DERNIERE_LIGNE_TESTS_IIB_PROCESSEUR` | remplis | empreintes : bloc plus bas, 34 fichiers au commit du code revu, relevées par l'exécutante (§ 4 étape 2) et recalculées par le rédacteur du brouillon 9 : 34 égales sur 34 au commit du code revu et au commit de lancement, 33 à `ec3b0329`, où seule celle du lanceur diffère ; dernière ligne : `@@DERNIERE_LIGNE_TESTS_IIB_PROCESSEUR@@`, durée exclue (`R-3556`), relevée au processeur à `ec3b0329`, rejouée au commit de lancement (§ 1) |",
    },
    {
        "nom": "B9-8f", "changement": 8, "lieu": "§ 11, ligne de la conception",
        "avant": "| `CHEMIN_CONCEPTION_IIB`, `EMPREINTE_CONCEPTION_IIB` | en attente | conception scellée (§ 4 étape 3) |",
        "apres": "| `CHEMIN_CONCEPTION_IIB`, `EMPREINTE_CONCEPTION_IIB` | remplis | conception scellée (§ 4 étape 3 ; `R-3527`) : `@@CHEMIN_CONCEPTION_IIB@@`, `@@EMPREINTE_CONCEPTION_IIB@@` |",
    },
    {
        "nom": "B9-8g", "changement": 8, "lieu": "§ 11, ligne de l'exécutante, du lecteur, de l'outil et du mot de Lazar",
        "avant": "| `EXECUTANTE_IIB`, `LECTEUR_IIB`, `VERSION_VASTAI`, `MOT_LAZAR_CREATION_IIB` | en attente | la mère, **avant le commit de lancement** (la configuration les exige remplis) : nom de la session exécutante ; rôle du lecteur ; version relevée ; référence de la ligne du registre où le mot de Lazar pour cette création est consigné |",
        "apres": "| `EXECUTANTE_IIB`, `LECTEUR_IIB`, `VERSION_VASTAI`, `MOT_LAZAR_CREATION_IIB` | remplis | la mère, **avant le commit de lancement** (la configuration les exige remplis) : nom de la session exécutante, `@@EXECUTANTE_IIB@@` ; rôle du lecteur, à la table des valeurs (`R-3525`) ; version relevée, `@@VERSION_VASTAI@@` ; référence de la ligne du registre où le mot de Lazar pour cette création est consigné, `@@MOT_LAZAR_CREATION_IIB@@` |",
    },
    {
        "nom": "B9-8h", "changement": 8, "lieu": "§ 11, ligne `LONGUEURS_CONSIGNE_IIB`",
        "avant": "| `LONGUEURS_CONSIGNE_IIB` | en attente | jetoniseur réel sur processeur avant le commit de lancement, ou valeur déclarée (§ 4 étape 4) |",
        "apres": "| `LONGUEURS_CONSIGNE_IIB` | rempli | `@@LONGUEURS_CONSIGNE_IIB@@` : jetoniseur réel sur processeur avant le commit de lancement (§ 4 étape 4) ; la valeur déclarée n'a pas servi |",
    },
    {
        "nom": "B9-8i", "changement": 8, "lieu": "§ 11, ligne `ENTROPIE_IIB`",
        "avant": "| `ENTROPIE_IIB` | en attente | tirage de la mère **avant d'écrire la configuration** |",
        "apres": "| `ENTROPIE_IIB` | rempli | `@@ENTROPIE_IIB@@` : tirage de la mère **avant d'écrire la configuration** (`R-3525`) |",
    },
    {
        "nom": "B9-8j", "changement": 8, "lieu": "§ 11, ligne de la configuration",
        "avant": "| `CHEMIN_CONFIG_IIB`, `EMPREINTE_CONFIG_IIB` | en attente | configuration au commit de lancement (proposé : `docs/notes/barreau8-iib-v1/config-iib-reel-v1.json`) |",
        "apres": "| `CHEMIN_CONFIG_IIB`, `EMPREINTE_CONFIG_IIB` | remplis | configuration au commit de lancement : `@@CHEMIN_CONFIG_IIB@@`, `@@EMPREINTE_CONFIG@@` ; pour son empreinte, la configuration porte « hors configuration (circulaire) » : la valeur écrite ici est celle du fichier à ce commit, recalculée |",
    },
    {
        "nom": "B9-8k", "changement": 8, "lieu": "§ 11, ligne `COMMIT_CORRECTIONS_RELAIS_POUSSEE_IIB`",
        "avant": "| `COMMIT_CORRECTIONS_RELAIS_POUSSEE_IIB` (propre) | rempli | `ec3b0329cd59db676007bd6c9ea3f0c36cf3ce95` : commit du code revu, qui porte ces corrections ; il descend, sur la même branche, de `a31b8970fedb745c993fe23df18bba4a2d9e3cf4` (contrôle court de cette tête, `02962a4a…c3a2`) ; réserve du brouillon 5 levée (`R-3497`) |",
        "apres": "| `COMMIT_CORRECTIONS_RELAIS_POUSSEE_IIB` (propre) | rempli | `ec3b0329cd59db676007bd6c9ea3f0c36cf3ce95` : commit, code revu d'alors, qui porte ces corrections ; il descend, sur la même branche, de `a31b8970fedb745c993fe23df18bba4a2d9e3cf4` (contrôle court de cette tête, `02962a4a…c3a2`) ; réserve du brouillon 5 levée (`R-3497`) ; le commit du code revu `f9a8aaeb`, son enfant direct, les porte aussi : le correctif ne touche ni l'amorce ni `lanceur_v1.py` |",
    },
    {
        "nom": "B9-8l", "changement": 8, "lieu": "§ 11, ligne `COMMIT_LANCEMENT_IIB`",
        "avant": "| `COMMIT_LANCEMENT_IIB` (propre) | en attente | § 4 étape 5 : enfant direct du commit du code revu `ec3b0329cd59db676007bd6c9ea3f0c36cf3ce95`, qui n'ajoute que la configuration et son sceau ; il n'existe pas tant que la configuration n'est pas écrite, et elle attend les faits de la remise (§ 4 étape 4) ; le code n'est plus en cause |",
        "apres": "| `COMMIT_LANCEMENT_IIB` (propre) | rempli | `@@COMMIT_LANCEMENT@@` : § 4 étape 5 : enfant direct du commit du code revu `@@COMMIT_CODE_IIB@@`, sur `@@BRANCHE_CODE_IIB@@`, qui n'ajoute que la configuration et son sceau (`R-3635`) ; le premier commit de lancement, `968a5151c5eb31014114e5093ba675a46fcd5414`, enfant direct de `ec3b0329`, est abandonné, sans suite (`R-3619`, `R-3622`) |",
    },
    {
        "nom": "B9-8m", "changement": 8, "lieu": "§ 11, ligne `REGLAGES_PORTAGE_BASE_TEXTUELLE_IIB`",
        "avant": "portés par le code au commit du code revu `ec3b0329` (contrôles courts des têtes `6e05a9d9` et `ec3b0329`, `R-3485`, `R-3497`), sous la réserve P7-R1 (§ 2, point 1) |",
        "apres": "portés par le code au commit `ec3b0329` (contrôles courts des têtes `6e05a9d9` et `ec3b0329`, `R-3485`, `R-3497`) et, sans changement, au commit du code revu `f9a8aaeb`, sous la réserve P7-R1 (§ 2, point 1) |",
    },
    {
        "nom": "B9-8n", "changement": 8, "lieu": "§ 11, table des valeurs à l'octet, bloc des empreintes du code, comptes",
        "avant": "Comptes : sur les 30, **16 remplis, 12 en attente, 2 hors de ce texte** (au brouillon 5 : 14, 14, 2 ; `COMMIT_CODE_IIB` est rempli depuis ; au brouillon 7 : 15, 13, 2 ; `LIGNE_REGISTRE_CREATION_7B` est rempli depuis) ; plus 6 propres : **5 remplis** (`MOT_LAZAR_ACTIVITE_INTERNE_IIB`, `COMMIT_CORRECTIONS_RELAIS_POUSSEE_IIB`, `REGLAGES_PORTAGE_BASE_TEXTUELLE_IIB`, `FORMAT_ACTIONS_PORTAGE_IIB`, `TIRAGES_PERMUTATIONS_LECTURE2_IIB`), **1 en attente** (`COMMIT_LANCEMENT_IIB`). Compté par programme (`compter-marqueurs-ii-b-v1.py`, scellé dans ce dossier, qui ne cherche que le motif des marqueurs ; sortie sous un nom neuf, `sortie-compter-marqueurs-ii-b-v3.txt`) : **13 marqueurs distincts restent dans ce texte** = les 12 en attente des 30 + le propre en attente ; aucun marqueur rempli n'y reste. Vérification au scellement : `grep -o '<<[A-Z0-9_]*>>' ordre-…` vide.\n",
        "apres": (
            "**Valeurs à l'octet des 30 marqueurs**, telles que la configuration du commit de lancement les porte ; table écrite par programme depuis la configuration, lue par `git show @@COMMIT_LANCEMENT@@:@@CHEMIN_CONFIG_IIB@@` :\n"
            "\n"
            "| marqueur | valeur à l'octet |\n"
            "|---|---|\n"
            "@@TABLE_DES_VALEURS@@"
            "\n"
            "Valeur de `EMPREINTES_CODE_IIB`, à l'octet, sur une seule ligne (34 fichiers ; pour chacun, son chemin, un espace, son empreinte ; séparateur « ; ») :\n"
            "\n"
            "```\n"
            "@@EMPREINTES_CODE_IIB@@\n"
            "```\n"
            "\n"
            "**Brouillon 3 lu par renvoi** : là où un passage du brouillon 3 que cet ordre reprend porte encore un marqueur entre chevrons doubles (commande de création, § 5 étape 2 ; rôle du lecteur, § 8), sa valeur est celle de cette table, ou, pour le commit de lancement, celle de la ligne `COMMIT_LANCEMENT_IIB` de la table des états.\n"
            "\n"
            "Comptes : sur les 30, **28 remplis, 0 en attente, 2 hors de ce texte** (au brouillon 5 : 14, 14, 2 ; au brouillon 7 : 15, 13, 2 ; au brouillon 8 : 16, 12, 2 ; les 12 qui restaient sont remplis au brouillon 9) ; plus 6 propres : **6 remplis** (`MOT_LAZAR_ACTIVITE_INTERNE_IIB`, `COMMIT_CORRECTIONS_RELAIS_POUSSEE_IIB`, `COMMIT_LANCEMENT_IIB`, `REGLAGES_PORTAGE_BASE_TEXTUELLE_IIB`, `FORMAT_ACTIONS_PORTAGE_IIB`, `TIRAGES_PERMUTATIONS_LECTURE2_IIB`), **0 en attente**. "
            "Compté par programme (`compter-marqueurs-ii-b-v1.py`, scellé dans ce dossier, qui ne cherche que le motif des marqueurs ; sortie sous un nom neuf, `sortie-compter-marqueurs-ii-b-v4.txt`) : **aucun marqueur entre chevrons doubles ne reste dans ce texte** (0 occurrence ; au brouillon 8 : 31 occurrences, 13 marqueurs distincts) ; les deux marqueurs hors de ce texte n'y sont nommés que sans chevrons. "
            "**Comparé par programme à la configuration du commit de lancement** (`comparer-marqueurs-ordre-configuration-ii-b-v1.py`, scellé dans ce dossier ; sortie `sortie-comparer-marqueurs-ordre-configuration-ii-b-v1.txt`, qui n'affiche aucune valeur) : des 30 marqueurs de la configuration, 27 ont dans ce texte une valeur égale à l'octet ; les 3 autres sont ceux que la configuration porte comme « hors configuration (circulaire) » : les deux marqueurs hors de ce texte, et `EMPREINTE_CONFIG_IIB`, égal ici à l'empreinte recalculée du fichier. Le même programme recompte les états de la table ci-dessus, compare les valeurs libres du § 2 à la configuration et cherche au § 5 les fragments de commandes attendus. "
            "Vérification au scellement : `grep -o '<<[A-Z0-9_]*>>' ordre-…` vide.\n"
        ),
    },
    # ------------------------------------------------------------------ § 13
    {
        "nom": "B9-6b", "changement": 6, "lieu": "§ 13, « Ce qu'elle rend » : texte de lecture des sondes scellé",
        "avant": "et le verdict scellé du témoin positif planté de la chaîne (P3-bis ; conception, § 1 et § 6.3 ; R-2044).\n",
        "apres": "et le verdict scellé du témoin positif planté de la chaîne (P3-bis ; conception, § 1 et § 6.3 ; R-2044). Le texte de lecture des sondes du barreau 8 est scellé depuis le 2026-11-19 à 06:32:25Z (`prereg/lecture-sondes-barreau8-v1.md`, `@@P:sondes@@` ; registre `registres/sondes-iib-v1.md`, ligne `SCELLEMENT-SONDES-IIB` ; `R-3612`) : ce scellement précède toute sortie de cette course.\n",
    },
]

# Ce que le rédacteur a relevé sans le corriger : écrit tel quel dans la note des différences.
NON_CORRIGE = [
    "`R-3535` (contrôle de la différence des brouillons 7 et 8) nomme deux corrections facultatives « à porter à la version suivante de l'ordre » : l'heure du brouillon 8, « vers 23:30 », deviendrait « vers 23:24 » ; l'exclusion du rédacteur du brouillon 8, au § 8, citerait `R-3524` et non `R-3523`. Elles ne sont pas appliquées : le mandat du brouillon 9 borne ses changements aux faits qu'il liste, et cette ligne n'en est pas. Les deux couples sont prêts : « Écrit le 2026-11-18 vers 23:30 UTC » → « Écrit le 2026-11-18 vers 23:24 UTC » (une seule place, à la ligne « Statut ») ; « le rédacteur du brouillon 8 (mandat de la session mère, `R-3523`, suite) » → « le rédacteur du brouillon 8 (mandat de la session mère, `R-3524`) ».",
    "§ 1, § 5 étape 1 : `IIB_TESTS_ATTENDUS` reste vide, comme au brouillon 8 ; la pièce `lancement-controles-836c7ccc-v1.txt` porte `tests_attendus 456`, et le journal v6 de l'exécutante dit le dossier des contrôles à blanc « gardé pour la création ». Écart déclaré au § 4 étape 6, (iii) ; à trancher par la mère avant le scellement.",
    "§ 4 étape 6 : l'extraction des fichiers du run n'est pas rejouée à blanc au commit de lancement, et `--verifier-go-seulement` n'est dans aucun journal des contrôles à blanc. Écarts déclarés au § 4 étape 6, (i) et (ii).",
    "§ 5 étape 5 : « la commande de cette lecture [du disque d'une instance arrêtée] est nommée et jouée à blanc par la mère avant le scellement de l'ordre » : aucune ligne lue par le rédacteur ne la nomme. Phrase laissée telle ; elle dit elle-même que, sans cette commande, le remède n'existe pas.",
    "§ 4 étape 3 : « devis contre-lu, scellé, puis inscrit en complément de la ligne d'accord » : la ligne `GO-2026-11-10-08`, relue, ne porte pas ce complément ; phrase laissée telle (étape de la mère). De même, trois lignes de la table du § 11 disent encore « proposé » ou « proposés » (dernier jour de création ; consigne ; devis, « sous réserve de la contre-lecture du devis »), alors que la configuration du commit de lancement porte ces valeurs : laissées telles.",
    "§ 8 : la liste des exclus ne reçoit que les quatre personnes que les faits du mandat font apparaître. Deux autres exclusions lues au registre ne sont pas ajoutées : le fabricant de la conception finale (`R-3527`) et le contrôleur de la différence des brouillons 7 et 8 (`R-3535`). Le registre « qui a lu quoi » fait foi.",
    "§ 13, « Ce qu'elle exige avant de partir » : le rédacteur, exclu du côté des sondes, n'a pas ouvert le texte de lecture des sondes et ne sait pas s'il tient lieu aussi du préenregistrement de la passe de recalcul (« quoi enregistrer ») ; phrase laissée telle.",
    "§ 7 : la question posée à la mère sur la copie publique (`donnees/*-iib-*`) reste ouverte, telle qu'au brouillon 8.",
    "§ 0 bis, § 9-10 : le devis reste au brouillon 6, intact ; aucun chiffre de dépense n'est touché.",
]


class Arret(Exception):
    """Un contrôle a échoué : le programme s'arrête sans rien écrire (ou le dit, s'il a déjà écrit)."""


def empreinte(octets: bytes) -> str:
    return hashlib.sha256(octets).hexdigest()


def git(*arguments: str) -> bytes:
    r = subprocess.run(["git", "-C", str(RACINE), *arguments], capture_output=True)
    if r.returncode != 0:
        raise Arret(f"git {' '.join(arguments[:2])} : code {r.returncode}")
    return r.stdout


def lire_verifie(chemin: Path, attendue: str) -> str:
    octets = chemin.read_bytes()
    if empreinte(octets) != attendue:
        raise Arret(f"empreinte de {chemin.name} : {empreinte(octets)} ≠ {attendue}")
    return octets.decode("utf-8")


def lire_configuration() -> tuple[dict, str]:
    brut = git("show", f"{COMMIT_LANCEMENT}:{CHEMIN_CONFIG}")
    e = empreinte(brut)
    if e != EMPREINTE_CONFIG_ATTENDUE:
        raise Arret(f"empreinte de la configuration au commit de lancement : {e} ≠ {EMPREINTE_CONFIG_ATTENDUE}")
    sceau = git("show", f"{COMMIT_LANCEMENT}:{CHEMIN_CONFIG}.sha256").decode().split()[0]
    if sceau != e:
        raise Arret("le sceau de la configuration au commit de lancement ne porte pas son empreinte")
    config = json.loads(brut.decode("utf-8"))
    marqueurs = config["marqueurs"]
    if len(marqueurs) != 30:
        raise Arret(f"{len(marqueurs)} marqueurs dans la configuration, 30 attendus")
    circulaires = sorted(n for n, v in marqueurs.items() if v == CIRCULAIRE)
    if circulaires != ["CHEMIN_ORDRE_IIB", "EMPREINTE_CONFIG_IIB", "EMPREINTE_ORDRE_IIB"]:
        raise Arret(f"marqueurs circulaires inattendus : {circulaires}")
    for nom, valeur in marqueurs.items():
        if not isinstance(valeur, str) or not valeur or "`" in valeur or "|" in valeur.replace(" | sha256sum", "") \
                or "\n" in valeur or "@@" in valeur or MOTIF_MARQUEUR.search(valeur):
            raise Arret(f"valeur du marqueur {nom} : forme inattendue (vide, accent grave, barre, saut de ligne ou marqueur)")
    if marqueurs["CHEMIN_CONFIG_IIB"] != CHEMIN_CONFIG:
        raise Arret("le marqueur du chemin de la configuration n'est pas le chemin lu")
    return config, e


def controler_git(config: dict) -> None:
    marqueurs = config["marqueurs"]
    parent = git("rev-parse", f"{COMMIT_LANCEMENT}^").decode().strip()
    if not (parent == marqueurs["COMMIT_CODE_IIB"] == config["code"]["commit"]):
        raise Arret("le parent du commit de lancement n'est pas le commit du code de la configuration")
    if config["code"]["branche"] != marqueurs["BRANCHE_CODE_IIB"]:
        raise Arret("la branche du code de la configuration n'est pas celle de son marqueur")
    if git("rev-parse", f"{parent}^").decode().strip() != COMMIT_CODE_D_ALORS:
        raise Arret("le commit du code revu n'est pas l'enfant direct du commit du code revu d'alors")
    fichiers = sorted(git("diff", "--name-only", parent, COMMIT_LANCEMENT).decode().split())
    if fichiers != [CHEMIN_CONFIG, CHEMIN_CONFIG + ".sha256"]:
        raise Arret(f"le commit de lancement ajoute autre chose que la configuration et son sceau : {fichiers}")
    if str(config["entropie"]) != marqueurs["ENTROPIE_IIB"]:
        raise Arret("l'entropie de la configuration n'est pas celle de son marqueur")
    registre = REGISTRE.read_text(encoding="utf-8").split("\n")
    lignes = [l for l in registre if l.startswith(f"- {LIGNE_ENTROPIE} (")]
    if len(lignes) != 1 or f"**{marqueurs['ENTROPIE_IIB']}**" not in lignes[0]:
        raise Arret(f"la ligne {LIGNE_ENTROPIE} du registre des décisions ne porte pas l'entropie de la configuration")
    mot = marqueurs["MOT_LAZAR_CREATION_IIB"]
    if not re.fullmatch(r"R-\d+", mot) or len([l for l in registre if l.startswith(f"- {mot} (")]) != 1:
        raise Arret("la ligne citée pour le mot de Lazar n'est pas une ligne unique du registre des décisions")
    extrait = marqueurs["LIGNE_REGISTRE_CREATION_7B"]
    if len([l for l in registre if extrait in l]) != 1:
        raise Arret("l'extrait de la ligne de création de 7b n'est pas porté par une seule ligne du registre")


def empreintes_des_pieces(config: dict) -> dict[str, str]:
    e: dict[str, str] = {}
    for cle, origine, chemin in PIECES:
        if origine == "ex":
            octets = git("show", f"{TETE_EXECUTANTE}:{chemin}")
            sceau = git("show", f"{TETE_EXECUTANTE}:{chemin}.sha256").decode().split()[0]
            if empreinte(octets) != sceau:
                raise Arret(f"pièce de l'exécutante {chemin} : empreinte ≠ compagnon")
        elif origine == "disque":
            octets = (RACINE / chemin).read_bytes()
            sceau = (RACINE / (chemin + ".sha256")).read_text(encoding="utf-8").split()[0]
            if empreinte(octets) != sceau:
                raise Arret(f"pièce {chemin} : empreinte ≠ compagnon")
        else:  # compagnon seul : le fichier n'est pas ouvert
            sceau = (RACINE / (chemin + ".sha256")).read_text(encoding="utf-8").split()[0]
        if not re.fullmatch(r"[0-9a-f]{64}", sceau):
            raise Arret(f"compagnon de {chemin} illisible")
        e[cle] = sceau
    if e["sondes"] != EMPREINTE_SONDES_ATTENDUE:
        raise Arret("le compagnon du texte de lecture des sondes ne porte pas l'empreinte attendue")
    if e["conception"] != config["marqueurs"]["EMPREINTE_CONCEPTION_IIB"]:
        raise Arret("le compagnon de la conception ne porte pas l'empreinte que porte la configuration")
    return e


def table_des_valeurs(marqueurs: dict[str, str], empreinte_config: str) -> str:
    lignes = []
    for nom in sorted(marqueurs):
        if nom in ("CHEMIN_ORDRE_IIB", "EMPREINTE_ORDRE_IIB"):
            cellule = "hors de ce texte : compagnon de l'ordre et ligne d'engagement ; la configuration porte « hors configuration (circulaire) »"
        elif nom == "EMPREINTE_CONFIG_IIB":
            cellule = f"`{empreinte_config}` : empreinte du fichier au commit de lancement, recalculée ; la configuration, qui ne peut pas porter sa propre empreinte, porte « hors configuration (circulaire) »"
        elif nom == "EMPREINTES_CODE_IIB":
            cellule = "bloc ci-dessous, sur une seule ligne"
        elif nom == "LIGNE_REGISTRE_CREATION_7B":
            cellule = "l'extrait écrit au § 1 (ligne « Préalable ») et au § 4 étape 4, et nulle part ailleurs dans ce texte"
        else:
            cellule = f"`{marqueurs[nom]}`"
        lignes.append(f"| `{nom}` | {cellule} |\n")
    return "".join(lignes)


def remplir(texte: str, valeurs: dict[str, str]) -> str:
    def place(m: re.Match) -> str:
        if m.group(1) not in valeurs:
            raise Arret(f"place @@{m.group(1)}@@ sans valeur")
        return valeurs[m.group(1)]
    return MOTIF_PLACE.sub(place, texte)


def appliquer(source: str, couples: list[dict]) -> str:
    texte = source
    for c in couples:
        n = texte.count(c["avant"])
        if n != 1:
            raise Arret(f"couple {c['nom']} : « avant » présent {n} fois au moment de l'application")
        texte = texte.replace(c["avant"], c["apres"])
    return texte


def controler(source: str, resultat: str, couples: list[dict], extrait_7b: str) -> None:
    for c in couples:
        n = resultat.count(c["apres"])
        if n != 1:
            raise Arret(f"couple {c['nom']} : « après » présent {n} fois à la fin")
    retour = resultat
    for c in reversed(couples):
        if retour.count(c["apres"]) != 1:
            raise Arret(f"couple {c['nom']} : application inverse impossible")
        retour = retour.replace(c["apres"], c["avant"])
    if retour != source:
        raise Arret("l'application inverse ne rend pas le brouillon 8 à l'octet")
    restes = MOTIF_MARQUEUR.findall(resultat)
    if restes:
        raise Arret(f"marqueurs entre chevrons doubles restants : {sorted(set(restes))}")
    if "@@" in resultat:
        raise Arret("une place @@NOM@@ reste dans le résultat")
    if resultat.count(f"`{extrait_7b}`") != 2:
        raise Arret("l'extrait de la ligne de création de 7b n'est pas écrit exactement deux fois")
    if source.count("\n") != 303 or not resultat.endswith("\n"):
        raise Arret("nombre de lignes de la source inattendu, ou résultat sans saut de ligne final")


def sortie_diff(resultat: str) -> str:
    r = subprocess.run(["diff", "-u", "--label", SOURCE.name, "--label", SORTIE.name, str(SOURCE), "-"],
                       input=resultat.encode("utf-8"), capture_output=True)
    if r.returncode != 1:
        raise Arret(f"diff -u : code {r.returncode} (1 attendu : des différences)")
    return r.stdout.decode("utf-8")


def decouper_blocs(diff: str) -> list[dict]:
    blocs: list[dict] = []
    for ligne in diff.split("\n")[2:]:
        m = MOTIF_BLOC.match(ligne)
        if m:
            debut = int(m.group(3))
            longueur = int(m.group(4)) if m.group(4) is not None else 1
            blocs.append({"entete": ligne, "debut": debut, "fin": debut + longueur - 1, "lignes": [], "couples": []})
        elif blocs:
            blocs[-1]["lignes"].append(ligne)
    if blocs and blocs[-1]["lignes"] and blocs[-1]["lignes"][-1] == "":
        blocs[-1]["lignes"].pop()
    return blocs


def rattacher(blocs: list[dict], resultat: str, couples: list[dict]) -> None:
    for c in couples:
        position = resultat.index(c["apres"])
        c["ligne"] = resultat.count("\n", 0, position) + 1
        derniere = c["ligne"] + c["apres"].rstrip("\n").count("\n")
        dans = [n for n, b in enumerate(blocs, 1) if not (derniere < b["debut"] or c["ligne"] > b["fin"])]
        if len(dans) != 1:
            raise Arret(f"couple {c['nom']} : rattaché à {len(dans)} blocs de diff")
        c["bloc"] = dans[0]
        blocs[dans[0] - 1]["couples"].append(c["nom"])
    for n, b in enumerate(blocs, 1):
        if not b["couples"]:
            raise Arret(f"bloc {n} de diff sans couple : un changement n'est pas déclaré")


def jouer(programme: Path) -> tuple[int, str]:
    r = subprocess.run([sys.executable, "-I", "-B", str(programme), str(SORTIE)], capture_output=True, cwd=str(DOSSIER))
    return r.returncode, r.stdout.decode("utf-8") + r.stderr.decode("utf-8")


def ecrire_note(resultat: str, couples: list[dict], diff: str, blocs: list[dict], compte: str, comparaison: str,
                pieces: dict[str, str], empreinte_config: str) -> str:
    retirees = sum(1 for b in blocs for l in b["lignes"] if l.startswith("-"))
    ajoutees = sum(1 for b in blocs for l in b["lignes"] if l.startswith("+"))
    t = []
    t.append("# Différences du brouillon 8 au brouillon 9 de l'ordre exploratoire du saboteur à budget — v1\n")
    t.append("Note fabriquée par programme (`appliquer-brouillon9-ii-b-v1.py`, dans ce dossier), en même temps que le brouillon 9. EXPLORATOIRE, NON OPPOSABLE (R-522). Aucun sujet, aucun mécanisme, aucun texte de consigne ni fragment n'y est écrit. Le devis reste au brouillon 6, intact. Le rédacteur du brouillon 9 travaille du côté du saboteur à budget : il est exclu de tout rôle côté sondes du barreau 8.\n")
    t.append("## 1. Pièces\n")
    t.append(f"- Brouillon 8 de l'ordre (intact, R12) : `{SOURCE.name}`, `{EMPREINTE_SOURCE}`.")
    t.append(f"- Brouillon 9 de l'ordre : `{SORTIE.name}`, `{empreinte(resultat.encode('utf-8'))}`.")
    t.append(f"- Programme : `{Path(__file__).name}`, `{empreinte(Path(__file__).read_bytes())}`.")
    t.append(f"- Programme de compte des marqueurs : `{COMPTEUR.name}`, `{empreinte(COMPTEUR.read_bytes())}` ; sa sortie : `{SORTIE_COMPTE.name}`, `{empreinte(compte.encode('utf-8'))}`.")
    t.append(f"- Programme de comparaison des marqueurs à la configuration : `{COMPARATEUR.name}`, `{empreinte(COMPARATEUR.read_bytes())}` ; sa sortie, qui n'affiche aucune valeur : `{SORTIE_COMPARAISON.name}`, `{empreinte(comparaison.encode('utf-8'))}`.")
    t.append(f"- Configuration de la course, lue par `git show {COMMIT_LANCEMENT}:{CHEMIN_CONFIG}` : `{empreinte_config}` (branche `prep/iib-code-v4`).")
    t.append(f"- Pièces de l'exécutante, lues par `git show` sur sa branche `claude/iib-executante-v1`, tête `{TETE_EXECUTANTE}`, chacune égale à son compagnon `.sha256` :")
    for cle, origine, chemin in PIECES:
        if origine == "ex":
            t.append(f"  - `{chemin}`, `{pieces[cle]}`.")
    t.append("- Pièces lues sur le disque (branche de travail), chacune égale à son compagnon `.sha256` :")
    for cle, origine, chemin in PIECES:
        if origine == "disque":
            t.append(f"  - `{chemin}`, `{pieces[cle]}`.")
    t.append("- Pièces dont seul le compagnon `.sha256` est lu, jamais le fichier :")
    for cle, origine, chemin in PIECES:
        if origine == "compagnon":
            t.append(f"  - `{chemin}`, `{pieces[cle]}`.")
    t.append("- Registre des décisions, lu seul, pour les lignes que la ligne « Accords » du brouillon 9 nomme : `registres/decisions.md` (fichier vivant : empreinte non citée). Registre des accords, lignes `GO-2026-11-10-08` et `GO-2026-11-19-04` : `registres/go.md` (fichier vivant).")
    t.append("- Brouillon 3 de l'ordre, lu aux passages repris par renvoi : `ordre-exploratoire-ii-b-v1-brouillon3.md`, `eed42f07329c5f064554b799f0d49ff0a1ed6e4571545c94dca3d6783f0c165f`.\n")
    t.append("## 2. Ce qui est appliqué\n")
    t.append(f"{len(couples)} couples « avant » / « après », écrits dans le programme, appliqués dans l'ordre, pour {len(CHANGEMENTS)} changements. Lignes du brouillon 8 retirées ou réécrites : **{retirees}** ; lignes du brouillon 9 neuves ou réécrites : **{ajoutees}** ; le brouillon 8 a 303 lignes, le brouillon 9 en a {resultat.count(chr(10))}. `diff -u` rend {len(blocs)} blocs.\n")
    for n, quoi in CHANGEMENTS.items():
        t.append(f"- Changement {n} : {quoi}.")
    t.append("")
    t.append("| couple | changement | lieu | ligne du brouillon 9 | bloc |")
    t.append("|---|---|---|---|---|")
    for c in couples:
        t.append(f"| {c['nom']} | {c['changement']} | {c['lieu']} | {c['ligne']} | {c['bloc']} |")
    t.append("")
    t.append("## 3. Valeurs prises par programme\n")
    t.append("Aucune valeur de marqueur n'est écrite à la main dans le programme. Les textes « après » portent des places, remplies : par les valeurs du dictionnaire `marqueurs` de la configuration du commit de lancement (30 marqueurs) ; par l'empreinte recalculée de la configuration, pour `EMPREINTE_CONFIG_IIB` ; par le commit de lancement, constante du programme, dont le parent direct est vérifié égal au commit du code que la configuration nomme ; par les empreintes des pièces, recalculées. La table des valeurs à l'octet du § 11 et le bloc du marqueur des empreintes du code sont écrits de même.\n")
    t.append("## 4. Ce que le programme a contrôlé\n")
    t.append("- empreinte du brouillon 8 ; empreinte de la configuration au commit de lancement, égale à l'empreinte attendue et à son sceau ; 30 marqueurs, dont trois « hors configuration (circulaire) » ;")
    t.append("- par `git` : le parent direct du commit de lancement est le commit du code de la configuration ; ce commit est l'enfant direct de `ec3b0329` ; le commit de lancement n'ajoute que la configuration et son sceau ;")
    t.append("- au registre des décisions : la ligne `R-3525` porte l'entropie de la configuration ; la ligne citée pour le mot de Lazar existe une seule fois ; l'extrait de la ligne de création de 7b n'est porté que par une ligne ;")
    t.append("- chaque « avant » présent exactement une fois au moment de son application ; chaque « après » présent exactement une fois à la fin ; application inverse égale au brouillon 8 à l'octet ;")
    t.append("- aucun marqueur entre chevrons doubles restant ; aucune place restante ; l'extrait de la ligne de création de 7b écrit exactement deux fois, comme au brouillon 8 ;")
    t.append("- chaque bloc de `diff -u` rattaché à au moins un couple, chaque couple à un seul bloc ;")
    t.append("- le programme de compte rend 0 occurrence ; le programme de comparaison rend le code 0.\n")
    t.append("## 5. Relevé sans être corrigé\n")
    t.append("Le rédacteur ne change que ce que les faits de son mandat imposent. Ce qu'il a relevé d'autre, il le porte ici et à la mère, sans y toucher :\n")
    for n, quoi in enumerate(NON_CORRIGE, 1):
        t.append(f"{n}. {quoi}")
    t.append("")
    t.append("## 6. Sortie du programme de compte\n")
    t.append("~~~~")
    t.append(compte.rstrip("\n"))
    t.append("~~~~\n")
    t.append("## 7. Sortie du programme de comparaison\n")
    t.append("~~~~")
    t.append(comparaison.rstrip("\n"))
    t.append("~~~~\n")
    t.append("## 8. Changements, bloc par bloc, tirés de `diff -u`\n")
    t.append(f"Commande : `diff -u {SOURCE.name} {SORTIE.name}`. Les lignes de l'ordre sont longues : chaque ligne changée est rendue entière.\n")
    for n, b in enumerate(blocs, 1):
        noms = ", ".join(b["couples"])
        numeros = sorted({c["changement"] for c in couples if c["nom"] in b["couples"]})
        t.append(f"### Bloc {n} — lignes {b['debut']} à {b['fin']} du brouillon 9 — couples {noms} — changement(s) {', '.join(map(str, numeros))}\n")
        t.append("~~~~diff")
        t.append(b["entete"])
        t.extend(b["lignes"])
        t.append("~~~~\n")
    return "\n".join(t)


def creer(chemin: Path, octets: bytes) -> None:
    with open(chemin, "xb") as f:
        f.write(octets)


def main() -> int:
    try:
        for chemin in (SORTIE, SORTIE_COMPTE, SORTIE_COMPARAISON, NOTE):
            if chemin.exists():
                raise Arret(f"{chemin.name} existe déjà : on n'écrase jamais (R12)")
        source = lire_verifie(SOURCE, EMPREINTE_SOURCE)
        config, empreinte_config = lire_configuration()
        controler_git(config)
        pieces = empreintes_des_pieces(config)
        marqueurs = config["marqueurs"]
        valeurs = dict(marqueurs)
        valeurs.update({f"P:{cle}": e for cle, e in pieces.items()})
        valeurs.update({
            "COMMIT_LANCEMENT": COMMIT_LANCEMENT, "EMPREINTE_CONFIG": empreinte_config, "HEURE": HEURE,
            "TETE_EXECUTANTE": TETE_EXECUTANTE, "TABLE_DES_VALEURS": table_des_valeurs(marqueurs, empreinte_config),
        })
        for interdit in ("CHEMIN_ORDRE_IIB", "EMPREINTE_ORDRE_IIB", "EMPREINTE_CONFIG_IIB"):
            del valeurs[interdit]  # jamais écrits comme valeur : circulaires dans la configuration
        couples = [dict(c, apres=remplir(c["apres"], valeurs)) for c in COUPLES]
        resultat = appliquer(source, couples)
        controler(source, resultat, couples, marqueurs["LIGNE_REGISTRE_CREATION_7B"])
        diff = sortie_diff(resultat)
        blocs = decouper_blocs(diff)
        rattacher(blocs, resultat, couples)
    except (Arret, OSError, KeyError, ValueError) as arret:
        print(f"ARRÊT, rien n'est écrit : {arret}", file=sys.stderr)
        return 1
    creer(SORTIE, resultat.encode("utf-8"))
    try:
        code_compte, compte = jouer(COMPTEUR)
        attendu = f"{SORTIE.name}  {empreinte(resultat.encode('utf-8'))}\n  occurrences 0 ; distincts 0\n"
        if code_compte != 0 or compte != attendu:
            raise Arret("la sortie du programme de compte n'est pas « 0 occurrence, 0 distinct »")
        code_comparaison, comparaison = jouer(COMPARATEUR)
        creer(SORTIE_COMPTE, compte.encode("utf-8"))
        creer(SORTIE_COMPARAISON, comparaison.encode("utf-8"))
        if code_comparaison != 0:
            raise Arret(f"le programme de comparaison rend le code {code_comparaison} : voir {SORTIE_COMPARAISON.name}")
        note = ecrire_note(resultat, couples, diff, blocs, compte, comparaison, pieces, empreinte_config)
    except (Arret, OSError) as arret:
        print(f"ARRÊT après l'écriture du brouillon 9 : {arret}", file=sys.stderr)
        return 1
    creer(NOTE, note.encode("utf-8"))
    for chemin in (SORTIE, SORTIE_COMPTE, SORTIE_COMPARAISON, NOTE):
        print(f"{chemin.name}  {empreinte(chemin.read_bytes())}")
    retirees = sum(1 for b in blocs for l in b["lignes"] if l.startswith("-"))
    ajoutees = sum(1 for b in blocs for l in b["lignes"] if l.startswith("+"))
    print(f"couples appliqués : {len(couples)} ; blocs de diff : {len(blocs)} ; lignes retirées ou réécrites : {retirees} ; lignes neuves ou réécrites : {ajoutees}")
    print(compte, end="")
    return 0


if __name__ == "__main__":
    sys.exit(main())
