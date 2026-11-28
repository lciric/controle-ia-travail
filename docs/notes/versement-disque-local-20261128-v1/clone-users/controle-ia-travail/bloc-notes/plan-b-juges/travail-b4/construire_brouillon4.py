"""Construit le brouillon 4 du préenregistrement du plan B des juges (T0.5) à partir du brouillon 3, sans le modifier.

Chaque changement est un remplacement exact : le texte ancien doit figurer une seule fois dans le brouillon 3, sinon
arrêt. Tout le reste, annexe A comprise, est recopié octet pour octet.
Usage : python3 -I construire_brouillon4.py <brouillon 3> <brouillon 4 à écrire>
"""
import hashlib
import sys
from pathlib import Path

SOURCE, CIBLE = Path(sys.argv[1]), Path(sys.argv[2])
if CIBLE.exists():
    sys.exit(f"{CIBLE} existe déjà : on n'écrase jamais (R12)")
texte = SOURCE.read_text(encoding="utf-8")
print("brouillon 3 :", hashlib.sha256(texte.encode("utf-8")).hexdigest())

SHA = {
    "b3": "8747ea81b1bc78f30e6d0990c441ad44d3f213f0e93944f6d1d3dac280c151c3",
    "manifeste_pilote": "8c3d7985eb65cd7b1dd239f8633e552b6af5fc14f44caaa801d1b85249e5e932",
    "episodes": "45616303dc740b66c42095cd5317a8ddd63e89123e64dd86490e43429c7cd15c",
    "taches": "287e83485cba550098b80db809589398d8f2826c02dfa9cc2719a1063795d5aa",
    "manifeste_notations": "9f143f7c1c9fd9d75f21807a0fa41035ae7110abe686fc7819130d3f6b435d38",
    "resume_notations": "994d542aafd224fc9347b2186979916c3e0a799c6edbefa28a7c9d6e972f44fc",
    "notations_8B": "b103835bcd3bfc3117a53e335be6f37a1259102cc2a2a134acfc6e114cb3f1c4",
    "notations_3B": "51548526c7590231b76473c2b4c9e619a092616b5f948830e735c466b037adab",
    "rs1": "b1e3e003daf2c64bb317fe5623495f73ec25e7a703c5d799ceb1ab8c1eb042e7",
    "index_rs1": "c61df3db8efce13295f9ba0cd1fb005fe8a1ef235d6977eacf004926ceeb4bda",
}


def remplacer(ancien: str, nouveau: str) -> None:
    global texte
    n = texte.count(ancien)
    if n != 1:
        sys.exit(f"texte ancien trouvé {n} fois (1 attendu) : {ancien[:90]!r}")
    texte = texte.replace(ancien, nouveau, 1)


def ligne_qui_commence_par(debut: str) -> str:
    lignes = [x for x in texte.split("\n") if x.startswith(debut)]
    if len(lignes) != 1:
        sys.exit(f"{len(lignes)} lignes commencent par {debut!r} (1 attendue)")
    return lignes[0]


# --------------------------------------------------------------------------------------------------- en-tête
remplacer("rejeu de la cause profonde — v1 (brouillon 3)\n", "rejeu de la cause profonde — v1 (brouillon 4)\n")

remplacer(
    "- **Auteur** : sous-agent rédacteur, en routine sur processeur (R-212). Il n'a écrit ni le pilote, ni le complément "
    "des notations, ni leur code, ni leurs verdicts, ni l'audit, ni la contre-lecture, ni la vérification courte. "
    "Brouillon 3 du 2026-10-19, vers 18:45 UTC : le brouillon 2",
    "- **Auteur** : sous-agents rédacteurs, en routine sur processeur (R-212). Ils n'ont écrit ni le pilote, ni le "
    "complément des notations, ni leur code, ni leurs verdicts, ni l'audit, ni la contre-lecture, ni la vérification "
    "courte. Le rédacteur du brouillon 4, sous-agent neuf, n'a écrit non plus ni le code du plan B, ni ses relectures "
    "R2, ni ses corrections. Brouillon 4 du 2026-10-20, vers 04:30 UTC : le brouillon 3 "
    f"(`{SHA['b3']}`, gardé tel quel), plus R-225 transcrite (vérification des corrections du brouillon 3, constat "
    "VC3-01) et les décisions de la session sur les questions de l'intégration du code et sur les constats des trois "
    "relectures R2 du code (R-249 ; numérotées D-1 à D-15 dans le traitement) ; traitement constat par constat : "
    "`traitement-R2-code-plan-B-v1.md` (bloc-notes, dossier `plan-b-code/corrections-v1/`, à verser). Le brouillon 3, "
    "du 2026-10-19 vers 18:45 UTC, était le brouillon 2")

remplacer(
    "des fichiers scellés l'ont été (section « Transparence »). Pièces jointes, même dossier : "
    "`notes-de-conception-v1.md`, `traitement-contre-lecture-v1.md`, `traitement-verification-courte-v1.md`, `travail/`.",
    "des fichiers scellés l'ont été (section « Transparence » ; pour le brouillon 4, seules des empreintes ont été "
    "recalculées). Pièces jointes, même dossier : `notes-de-conception-v1.md`, `traitement-contre-lecture-v1.md`, "
    "`traitement-verification-courte-v1.md`, `travail/`, `travail-b4/` (construction et contrôles du brouillon 4).")

remplacer(
    "- **Commit du code d'analyse** : fixé au candidat. Le code n'existe pas encore (section « Code à écrire et tests ») ; "
    "aucun module gelé n'est modifié.\n"
    "- **Tests attendus** : fixé au candidat (toute la suite de `tests/` au commit du code ; le script de l'instance "
    "exige la dernière ligne « N passed[, M warning(s)] in X s[ (h:mm:ss)] », rien d'autre).\n"
    "- **Scripts de l'instance, gelés par le commit du code** : `scripts/amorce_instance_t05_planb.sh` et "
    "`scripts/planb_t05_instance.sh` ; empreintes sha256 fixées au candidat, comparées par les contrôles avant dépense "
    "et par le lanceur.\n",
    "- **Lignes de citation** (R-249 ; relecture R2 du code, R2-04 ; question I-3 de l'intégration). Le lanceur les "
    "exige avant le manifeste (`requalifier_juges.py` : `CITATIONS` et `NOTATIONS_CITEES` ; motifs gelés "
    "`COMMIT_CITE`, `TACHES_CITEES` et `ENTROPIE_CITEE`). Chacune tient sur une ligne simple, « Intitulé : `valeur` », "
    "sans gras, au format du complément scellé des notations (`prereg/T0.5-pilote-notations-v1.md`, l. 6 et "
    "l. 22-28). Chaque intitulé n'a qu'une valeur dans tout le texte ; le lanceur la compare à celle qu'il recalcule "
    "(liste d'arrêt, « Avant le manifeste »).\n"
    "  - **Marqueurs à remplir au candidat**, au commit du code. Tant qu'il en reste un, les gardes de citation refusent "
    "le texte : aucun motif ne lit un marqueur (essai : « Avant le scellement »). `<<COMMIT_CODE>>` : commit du code "
    "d'analyse, 40 caractères hexadécimaux ; `<<EMPREINTE_CONFIG>>` : empreinte canonique de la configuration, 64 ; "
    "`<<ENTROPIE>>` : entier, tiré au scellement. Pour la chaîne de lancement : `<<TESTS_ATTENDUS>>` (nombre de tests "
    "de la suite au commit du code), `<<SHA256_AMORCE>>` et `<<SHA256_SCRIPT_INSTANCE>>` (empreintes des deux scripts "
    "de l'instance).\n"
    "- Commit du code d'analyse : `<<COMMIT_CODE>>`\n"
    "  - Code neuf, gelé par ce commit : `src/controle_ia/environnements/rubrique_simplifiee.py`, "
    "`juges_simplifies.py`, `requalifier_juges.py` et `lire_requalification.py` ; tests "
    "`tests/test_plan_b_rubrique_simplifiee.py`, `test_plan_b_juges_simplifies.py`, `test_plan_b_requalifier.py`, "
    "`test_plan_b_lecteur.py` et `test_plan_b_integration.py` ; invite `docs/sources/invites-plan-b-v1/` ; chaîne de "
    "lancement (section « Code à écrire et tests », point 6). Aucun module gelé n'est modifié.\n"
    "- Configuration du plan B (empreinte canonique) : `<<EMPREINTE_CONFIG>>`\n"
    "  - fichier `prereg/T0.5-plan-B-juges-config-v1.json` ; table clé → valeur au « Plan d'analyse », "
    "« Configuration ».\n"
    "- Run du pilote requalifié : `20261012-105125-t05-pilote-reel`\n"
    f"- Manifeste du pilote requalifié : `{SHA['manifeste_pilote']}`\n"
    f"- Épisodes du pilote requalifié : `{SHA['episodes']}`\n"
    f"- Tâches du pilote : `{SHA['taches']}`\n"
    "- Run des notations rejoué : `20261017-193648-t05-notations-reel`\n"
    f"- Manifeste des notations rejoué : `{SHA['manifeste_notations']}`\n"
    f"- Résumé des notations rejoué : `{SHA['resume_notations']}`\n"
    f"- Notations rejouées du juge 8B : `{SHA['notations_8B']}`\n"
    f"- Notations rejouées du juge 3B : `{SHA['notations_3B']}`\n"
    f"- Invite RS1 : `{SHA['rs1']}`\n"
    f"- Index de l'invite RS1 : `{SHA['index_rs1']}`\n"
    "  - fichiers `docs/sources/invites-plan-b-v1/invites/RS1.txt` et `index.json`, scellés ; texte complet en annexe A. "
    "L'index garde sa provenance (`texte_extrait_de` : le brouillon 3, `8747ea81…`). Il n'est pas réécrit au "
    "scellement pour citer ce texte : l'index et le texte se citeraient l'un l'autre. Le brouillon 3 est versé avec "
    "les pièces, pour que cette provenance se résolve (R6 ; R2-2-05, R-249).\n"
    "- Entropie : `<<ENTROPIE>>`\n"
    "  - tirée au scellement par `numpy.random.SeedSequence`, écrite une seule fois (R9). Les graines du rejeu ne "
    "viennent pas de cette entropie : ce sont celles, scellées, du pilote (« Plan d'analyse », « Graines »).\n"
    "- Tests attendus : `<<TESTS_ATTENDUS>>`\n"
    "  - toute la suite de `tests/` au commit du code ; le script de l'instance exige la dernière ligne « N passed[, M "
    "warning(s)] in X s[ (h:mm:ss)] », rien d'autre.\n"
    "- **Scripts de l'instance, gelés par le commit du code** : `scripts/amorce_instance_t05_planb.sh` "
    "(`<<SHA256_AMORCE>>`, sha256) et `scripts/planb_t05_instance.sh` (`<<SHA256_SCRIPT_INSTANCE>>`, sha256) ; "
    "comparés par les contrôles avant dépense et par le lanceur.\n")

remplacer(
    "et R-221 (suites de la vérification courte du brouillon 2, dont l'ancrage au noyau « math » rangé parmi les "
    "instruments de Q1, la couverture comptée en jetons générés, la règle des intervalles et la forme de la condition de "
    "crédit) ; la session consigne aussi, au registre, ce qu'elle retient de ce brouillon 3.",
    "et R-221 (suites de la vérification courte du brouillon 2, dont l'ancrage au noyau « math » rangé parmi les "
    "instruments de Q1, la couverture comptée en jetons générés, la règle des intervalles et la forme de la condition de "
    "crédit) ; puis R-224 (ce que la session retient du brouillon 3) et R-225 (corrections du brouillon 3 vérifiées ; "
    "VC3-01 : une valeur qui continue, après le premier nombre, par « , », « ; », « and » ou « ( » suivis d'un chiffre "
    "est invalide) ;\n"
    "  - décisions de la session du 2026-10-20 : R-247 (code du plan B écrit, intégré et relu sous trois angles) et R-249 "
    "(décisions sur les questions de l'intégration et sur les constats des trois relectures R2 du code ; brouillon 4) ; "
    "la session consigne aussi, au registre, ce qu'elle retient de ce brouillon 4.")

remplacer("Relus pour ce brouillon à la tête `1ac04b8`", "Relus pour le brouillon 3 à la tête `1ac04b8`")
remplacer("Relu de nouveau à la fin de ce brouillon, à la tête `ed5b166`",
          "Relu de nouveau à la fin du brouillon 3, à la tête `ed5b166`")

remplacer(
    "sans toucher aux lignes citées ; `go.md` et `depenses.md` sont inchangés.\n",
    "sans toucher aux lignes citées ; `go.md` et `depenses.md` sont inchangés. Relu pour le brouillon 4 à la tête "
    "`7cd8b65` (2026-10-20) : `registres/decisions.md` (`6341a938b5e91e0d309af666f1194479bad15da9da1213dca60081b674903331`) "
    "porte en plus les lignes R-224 à R-249, dont R-225, R-247 et R-249 sur ce plan B, sans toucher aux lignes citées ; "
    "`go.md` est inchangé ; `depenses.md` (`1ab0b039878a80731ce1869dcddb2156659dd9e041ff2176b45a0aabe6868a93`) porte "
    "deux lignes de plus, sur P3 (l. 87-88), et ses lignes citées (l. 84-86) sont inchangées. Les montants du devis "
    "(cumul de la phase 0, crédit) n'ont pas été recomptés pour ce brouillon (« Calcul et devis »).\n")

remplacer(
    "- **Pièces scellées dont l'étape part** (chemin et sha256 complets) :\n",
    "- **Pièces scellées dont l'étape part** (chemin et sha256 complets ; les mêmes valeurs, une par ligne, dans les "
    "lignes de citation ci-dessus) :\n")

remplacer(
    "aucun de ces modules n'a changé de `c63d4f1` à la tête `ed5b166`, vérifié par `git diff`).",
    "aucun de ces modules n'a changé de `c63d4f1` à la tête `ed5b166`, vérifié par `git diff` ; vérifié de nouveau "
    "pour le brouillon 4, à la tête `7cd8b65` du dépôt et dans le clone du code du plan B, tête `cb14316`).")

remplacer(
    "- **Entropie** : tirée au scellement par `numpy.random.SeedSequence`, écrite une seule fois (R9). Les graines du "
    "rejeu ne viennent pas de cette entropie : ce sont celles, scellées, du pilote (« Plan d'analyse », « Graines »).\n"
    "- **Configuration de l'étape** : `prereg/T0.5-plan-B-juges-config-v1.json`, empreinte canonique fixée au "
    "scellement (table clé → valeur au « Plan d'analyse »).\n"
    "- **Invite RS1** : `docs/sources/invites-plan-b-v1/invites/RS1.txt`, avec son index scellé (texte complet en "
    "annexe A ; empreinte fixée au scellement).\n",
    "")

# --------------------------------------------------------------------------------------------------- prédictions
remplacer(
    "ni sa clause de réfutation (« défaut du chemin ») n'est vraie (décision de la session, R-221).",
    "ni sa clause de réfutation (« défaut du chemin ») n'est vraie (décision de la session, R-221). Une grandeur "
    "illisible (NaN) au palier du chemin se lit « non concluant (contrôles) », jamais « défaut » (table C ; R-249) : "
    "PB8 ne peut donc pas être réfutée par un NaN, comme le veut la règle « sur des grandeurs définies ».")

# --------------------------------------------------------------------------------------------------- métrique
ancienne_etape5 = ligne_qui_commence_par("  5. **valeur** : pour une occurrence chiffrée,")
coupe = " Ensuite, la valeur est l'entier que rend la fonction gelée"
assert ancienne_etape5.count(coupe) == 1
debut_etape5 = ancienne_etape5[:ancienne_etape5.index(coupe)]
remplacer(
    debut_etape5,
    "  5. **valeur** : pour une occurrence chiffrée, d'abord un **contrôle de la suite du premier nombre** (intervalles "
    "et seconds nombres), neuf, fait avant la fonction gelée et sans la toucher (décisions de la session, R-221 et "
    "R-225). La valeur nettoyée (signe « − » lu « - », comme dans la fonction gelée) est invalide si elle continue, "
    "après son premier nombre et d'éventuelles espaces, par l'un des séparateurs listés, puis, après d'éventuelles "
    "espaces, par un chiffre, éventuellement signé (+, - ou −), comme à l'étape 4 (R-249) ; casse indifférente. "
    "Séparateurs : « - », « – », « — », « to » ou « or » (occurrence comptée « intervalle », R-221) ; « , », « ; », "
    "« and » ou « ( » (occurrence comptée « second nombre », à part, R-225). Le premier nombre est ce que reconnaissent "
    "les motifs gelés `_FRACTION` et `_ENTIER` (`rubrique.py`, l. 40-41) : l'entier, avec son échelle écrite (« 4/5 ») "
    "ou ses décimales nulles (« 4.0 ») s'il en a. Sont donc invalides, comptés « intervalle » : « 3 - 4 », « 3 – 4 », "
    "« 3 to 4 », « 3 or 4 », « 4/5 - 5/5 », « 4.0 to 5.0 », et, avec un signe, « 3 to -4 », « 3 to −4 », « 3 - +4 » ; "
    "comptés « second nombre » : « 3, 4 », « 3; 4 », « 3 and 4 », « 3 (4) », « 3/5, 4/5 », « 3, -1 ». Ne le sont pas : "
    "« 3 - solid », « 3 (competent) », « 3 or more », « 3, solid », « 3 (out of 5) » (intervalles : essai du rédacteur "
    "sur des valeurs écrites à la main, motifs gelés recopiés sans importer le dépôt : `travail/essai_intervalles.py`, "
    "`3568548c14cd1f05b5863d188be14e9842242f0afe9f54540211d6c5110bfec9`, sortie `travail/sortie-essai-intervalles.txt`, "
    "`d6000ba924b066f109a01ca94ce4b98af38706ea286ec4c7c01abb1b87891dbd` ; seconds nombres et signes : tests du code, "
    "`test_intervalles_invalides`, `test_seconds_nombres_invalides_r225` et `test_cas_sains_du_controle`). Sans ce "
    "contrôle, la fonction gelée lirait « 3 - 4 », « 3 to 4 », « 3 or 4 », « 3, 4 » et « 3 (4) » comme 3, car elle "
    "accepte un entier suivi d'une espace, de « , », « ; », « ) » ou « ] » (l. 41 ; essai de la vérification courte, "
    "VC-06, et vérification de ses corrections, VC3-01). **Limites écrites** : (a) une prose qui suit une note et "
    "commence par un séparateur listé puis un chiffre (« 5 - 1 weak point », « 4 (2 weak points) ») est aussi rendue "
    "invalide (limite élargie par R-225) ; (b) tout second nombre relié au premier autrement que par les séparateurs "
    "listés, Markdown compris, n'est pas vu par ce contrôle, et la fonction gelée lit le premier (R-249). Formes "
    "trouvées par les relectures R2 du code, toutes lues sur le premier nombre : « 3 vs 4 », « 3 **or** 4 », "
    "« 3 -- 4 », « 3 [4] », « 3/5 4/5 », « 3 → 4 » (liste complète dans la docstring de `rubrique_simplifiee.py` et "
    "dans le test `test_limite_ecrite_second_nombre_relie_autrement_lu_sur_le_premier`) ; le descriptif « lues dont la "
    "suite porte un chiffre » en majore le nombre (descriptifs, ci-dessous). Les occurrences rendues invalides par ce "
    "contrôle sont comptées et rapportées, par catégorie (« intervalle », « second nombre »).")

remplacer(
    "  - la règle retenue ignore la prose sans chiffre, refuse toute note invalide, tout intervalle et toute "
    "contradiction, et ne choisit jamais entre deux nombres. Une prose qui commence par un nombre (« Specificity: 2 of "
    "the proposals… ») est lue comme une note : si elle contredit le bloc, la réponse est incomplète. Le nombre de ces "
    "cas est rapporté ;",
    "  - la règle retenue ignore la prose sans chiffre, refuse toute note invalide, tout intervalle, tout second nombre "
    "et toute contradiction, et ne choisit jamais entre deux nombres reliés par l'un des séparateurs listés ; un second "
    "nombre relié autrement n'est pas vu, et le premier est lu (limite écrite, étape 5 ; R-225, R-249). Une prose qui "
    "commence par un nombre (« Specificity: 2 of the proposals… ») est lue comme une note : si elle contredit le bloc, "
    "la réponse est incomplète. Ces cas entrent dans le compte descriptif « lues suivies de texte », qui compte aussi "
    "les gloses de la ligne de note elle-même (« 3 (competent) ») : il ne les isole donc pas (descriptifs, ci-dessous ; "
    "R-249) ;")

remplacer(
    "comptes des anomalies par motif, nombre d'occurrences non chiffrées, d'intervalles et de contradictions, part de la "
    "somme la plus fréquente",
    "comptes des anomalies par motif, nombre d'occurrences non chiffrées, d'intervalles, de seconds nombres et de "
    "contradictions ; « lues suivies de texte » (`lues_suivies_de_texte`) : occurrences lues dont la valeur nettoyée "
    "porte, après le premier nombre, au moins un caractère de mot (lettre, chiffre ou souligné), où qu'elles soient, "
    "gloses de la ligne de note comprises (« 3 (competent) ») ; une ponctuation seule (« 3. ») n'y compte pas ; « lues "
    "dont la suite porte un chiffre » (`lues_suite_avec_chiffre`, neuf, R-249) : occurrences lues dont la suite, après "
    "le premier nombre, porte encore un chiffre. Ce dernier compte est sans effet sur la lecture. Il majore la limite "
    "écrite (b) de l'étape 5 (seconds nombres non vus), mais compte aussi les gloses saines chiffrées (« 3 (out of 5) ») : "
    "il se lit donc dans les deux sens (R4) ; part de la somme la plus fréquente")

remplacer(
    "- Les rapports de la garde sont écrits dans le fichier des notations RS1 de chaque juge (champ `garde`), avec les "
    "notations : ils sont scellés ensemble, « tout ou rien ».",
    "- **Sondes d'audit** de chaque rangée gardée, comme au rejeu (`sonde_de_comparaison` : tableaux distincts, une "
    "unité au dernier rang vue) ; une sonde fausse se lit à la table A (R-249).\n"
    "- Les rapports de la garde sont écrits dans le fichier des notations RS1 de chaque juge (champ `garde`), avec les "
    "notations : ils sont scellés ensemble, « tout ou rien ».")

remplacer(
    "passe unique de chaque rangée au même noyau ;",
    "passe unique de chaque rangée au même noyau ; décalage passé (0) consigné à chaque lot (`decalages_passes`), "
    "rapporté sans être exigé (R-249) ;")

remplacer(
    "sur tous les jetons des 16 rangées (fonction gelée `repere_precision`, `harnais/validation_reelle.py`, l. 526 ; "
    "rôles après la conversion : « Ordre des phases ») ;",
    "sur tous les jetons des 16 rangées, par les fonctions gelées `passe_unique` et `ecarts_par_jeton` "
    "(`harnais/activations.py`, l. 99 et l. 124), agrégées comme `repere_precision` (`harnais/validation_reelle.py`, "
    "l. 526-541 : quantiles 0,5 et 0,99 et maximum des écarts par jeton mis bout à bout, par couche) ; rôles : "
    "numérateur ‖a_demi − a_simple‖, dénominateur ‖a_simple‖, la passe en simple précision étant la référence "
    "(R2-03, R-249 ; « Ordre des phases ») ;")

remplacer(
    "- **ancrage du seuil du chemin dans ce domaine** : la plus longue rangée de L1 (en positions) passe une fois",
    "- **ancrage du seuil du chemin dans ce domaine** : la plus longue rangée de L1 (en positions), choisie avant le "
    "repère (« Ordre des phases »), passe une fois")

remplacer(
    "au noyau par défaut ; 16 rangées capturées ; passe unique en simple précision ;",
    "au noyau par défaut, sans décalage ; 16 rangées capturées ; passe unique en simple précision ; le lanceur consigne, "
    "à chaque lot, le décalage réellement passé (`decalages_passes` : 0 à L1 et à L2), que la lecture exige (R-249) ;")

remplacer(
    "(positions décodées décalées de +1 : `decalage_positions=1`, `harnais/episode.py`, l. 109) ;",
    "(positions décodées décalées de +1 : `decalage_positions=1`, `harnais/episode.py`, l. 109 ; décalage réellement "
    "passé consigné, `decalages_passes` : `decalage_d1` à L3, exigé à la lecture, R-249) ;")

# --------------------------------------------------------------------------------------------------- seuil
remplacer(
    "- **classement de chaque dépassement** (rangée r et couche ℓ où G_S(r, ℓ) > 3e-3), sur les maxima par zone "
    "(contexte, zone générée) de `profil_ecarts`, dans cet ordre (localisation reprise de T0.4 v3, l. 277-278 et "
    "l. 284) :\n",
    "- **classement de chaque dépassement** (rangée r et couche ℓ où G_S(r, ℓ) > 3e-3, ou G_S(r, ℓ) illisible), sur "
    "les maxima par zone (contexte, zone générée) de `profil_ecarts`, dans cet ordre (localisation reprise de T0.4 v3, "
    "l. 277-278 et l. 284). D'abord, une grandeur illisible (NaN), G_S, un maximum de zone ou R_S de la couche, n'est "
    "classée nulle part : classe « illisible », lue avec les contrôles (table C, première ligne : « grandeur illisible "
    "(NaN) »), jamais comme un défaut (R-249 : une valeur illisible ne passe aucun seuil, mais n'établit aucun défaut). "
    "Sinon :\n")

remplacer(
    "- conditions de retenue de RS1 ajoutées à la règle du plan B : garde en ligne conforme ; rejeu sans « défaut du "
    "chemin » ;",
    "- conditions de retenue de RS1 ajoutées à la règle du plan B : garde en ligne conforme, sondes d'audit de la garde "
    "justes (R-249) ; rejeu sans « défaut du chemin » ;")

remplacer(
    "dans un sens ou dans l'autre ; borne de 1e-2) ; ancrage, couche par couche,",
    "dans un sens ou dans l'autre ; borne de 1e-2 ; classe « illisible » d'une grandeur NaN, lue « non concluant "
    "(contrôles) », R-249) ; ancrage, couche par couche,")

remplacer(
    "- règle de lecture d'une réponse sous RS1, contrôle des intervalles compris (« Métrique »).",
    "- règle de lecture d'une réponse sous RS1, contrôle de la suite du premier nombre compris : intervalles (R-221), "
    "seconds nombres (R-225), chiffre éventuellement signé après le séparateur (R-249) (« Métrique », étape 5) ;\n"
    "- gardes neuves (R-249) : annexe A du texte scellé égale à `RS1.txt`, avant le manifeste et à la lecture ; tirage "
    "des lots du rejeu recalculé, et décalages réellement passés, à la lecture (« Liste d'arrêt »).")

# --------------------------------------------------------------------------------------------------- plan d'analyse
remplacer(
    "1. avant le manifeste : gardes (liste d'arrêt) ; manifeste ;",
    "1. avant le manifeste : gardes (liste d'arrêt ; lignes de citation et annexe A comprises, R-249) ; manifeste ;")

remplacer(
    "5. **rejeu du 3B** (le 3B reste chargé) : palier de production sur L1 et L2, puis `rejeu-3B-demi.json` ; réglages "
    "effectifs relus ; conversion en simple précision, type des poids relu ; repère sur les 16 transcriptions (rôles : la "
    "passe en demi-précision est celle du palier de production, gardée ; la référence est la passe en simple précision du "
    "modèle converti ; `repere_precision` calcule la passe du modèle courant, attendu en demi-précision, contre des "
    "références de plus haute précision, `validation_reelle.py`, l. 526-541 : son emploi après la conversion est un point "
    "nommé pour la relecture R2 du code) ; ancrage au noyau « math » ;",
    "5. **rejeu du 3B** (le 3B reste chargé) : palier de production sur L1 et L2, puis `rejeu-3B-demi.json` ; réglages "
    "effectifs relus ; rangée d'ancrage choisie avant le repère : la plus longue de L1, en positions (R-249) ; conversion "
    "en simple précision, type des poids relu ; repère sur les 16 transcriptions, par les fonctions gelées "
    "`passe_unique` et `ecarts_par_jeton`, agrégées comme `repere_precision` (quantiles 0,5 et 0,99, maximum). Rôles : "
    "la passe en demi-précision est celle du palier de production, gardée jusque-là ; la référence, au dénominateur, est "
    "la passe en simple précision du modèle converti (numérateur ‖a_demi − a_simple‖, dénominateur ‖a_simple‖). "
    "`repere_precision` elle-même n'est pas appelée : après la conversion, elle prendrait la passe du modèle courant, en "
    "simple précision, pour la passe comparée, et la passe en demi-précision pour la référence, rôles inversés ; avant, "
    "la référence n'existe pas (relecture R2 du code, R2-03 ; le point nommé VC-15 est clos, R-249). Chaque passe en "
    "demi-précision est rendue dès ses écarts calculés ; seule la passe en simple précision de la rangée d'ancrage est "
    "gardée (R-249) ; ancrage au noyau « math » ;")

remplacer(
    "- **Lignes de progression** : comme au complément des notations (l. 85) : rang et durée de chaque lot, fin de chaque "
    "phase ; **aucun compte de réponses, aucune grandeur d'équivalence**.\n",
    "- **Lignes de progression** : comme au complément des notations (l. 85) : rang et durée de chaque lot, fin de chaque "
    "phase ; **aucun compte de réponses, aucune grandeur d'équivalence**.\n"
    "- **Champs des fichiers fixés par R-249** : `decalages_passes` (décalage réellement passé à chaque lot) dans "
    "`rejeu-<J>-demi.json`, et dans `chemin` et `d1` de `rejeu-<J>-simple.json` ; `annexe_a` (« égale à RS1.txt », avec "
    "l'empreinte) dans `resume.json` et dans le partiel d'`arret.json` ; `lues_suite_avec_chiffre` dans la lecture RS1 "
    "(`lecture_rs1`) de chaque notation RS1. La lecture écrit en plus, dans `lecture-planb.json`, `annexe_a`, le tirage "
    "des lots recalculé de chaque juge (`rejeu.<J>.tirage`) et le descriptif `lues_suite_avec_chiffre` de la "
    "requalification.\n")

remplacer(
    "plus les passes uniques en demi-précision des 16 rangées, gardées pour le repère (environ 8 Go au plus). Le lanceur "
    "les rend après chaque lot (ou, pour le repère, après la phase), et elles ne s'accumulent pas d'un lot à l'autre "
    "(test). Pic estimé du palier en simple précision : environ 57 Gio pour le 8B (pic H.4 de 28,42 Gio en "
    "demi-précision, doublé), sous la garde de 75 Gio ; une panne de mémoire y est un arrêt consigné (nœud), après le "
    "rejeu du 3B. Mémoire vive exigée : au moins 64 Go (estimation : environ 8 Go de passes gardées pour le repère, "
    "environ 8 Go pour un lot en cours, des deux côtés, plus les modèles chargés sur le processeur).",
    "plus les passes uniques en demi-précision des 16 rangées, gardées jusqu'au repère (environ 8 Go au plus). Le "
    "lanceur rend les activations d'un lot après ce lot, et elles ne s'accumulent pas d'un lot à l'autre (test). Au "
    "repère (R-249 ; relecture R2 du code, R2-05), chaque passe en demi-précision est rendue dès ses écarts calculés : "
    "ces 8 Go décroissent ; une seule passe en simple précision est tenue à la fois (au plus environ 0,5 Go : 3 couches "
    "× 10 075 positions × 4 096 valeurs × 4 octets), plus celle de la rangée d'ancrage, seule gardée jusqu'à l'ancrage "
    "(test de la mémoire du repère). Pic estimé du palier en simple précision : environ 57 Gio pour le 8B (pic H.4 de "
    "28,42 Gio en demi-précision, doublé), sous la garde de 75 Gio ; une panne de mémoire y est un arrêt consigné "
    "(nœud), après le rejeu du 3B. **Pic de l'ancrage au noyau « math »** (8B, une rangée d'au plus 10 075 positions ; "
    "R2-10, R-249) : ce noyau tient en même temps les scores d'attention et leur softmax, environ 2 × 13 Go "
    "(32 têtes × 10 075² × 4 octets, environ 13 Go chacun), plus 32 Go de poids du 8B en simple précision, soit environ "
    "60 Go ; estimation à mesurer dans les bancs de la chaîne (8B, 10 075 positions, simple précision, noyau « math ») "
    "et à écrire au candidat. Mémoire vive exigée : au moins 64 Go (estimation : environ 8 Go de passes en "
    "demi-précision gardées jusqu'au repère, puis rendues une à une, plus une passe en simple précision à la fois et "
    "celle de l'ancrage, environ 0,5 Go chacune ; environ 8 Go pour un lot en cours, des deux côtés ; plus les modèles "
    "chargés sur le processeur).")

remplacer(
    "l'ancrage compare les deux noyaux sur une seule rangée (environ 13 Go de scores pour 10 000 positions), ce qui "
    "tient ;",
    "l'ancrage compare les deux noyaux sur une seule rangée : environ 2 × 13 Go de scores et de softmax pour 10 000 "
    "positions, plus 32 Go de poids du 8B, soit environ 60 Go sur une carte de 80 Go (estimation corrigée par la "
    "relecture R2 du code, R2-10 ; pic à mesurer dans les bancs : « Mémoire ») ;")

remplacer(
    "`rejeu/8B/lots` et `rejeu/3B/lots` (L1, L2, L3, tirés sans remise dans le cadre trié, dans l'ordre du tirage) ;",
    "`rejeu/8B/lots` et `rejeu/3B/lots` (L1, L2, L3, tirés sans remise dans le cadre trié, dans l'ordre du tirage ; le "
    "lecteur refait ce tirage et le compare au tirage consigné, R-249) ;")

remplacer(
    "il ne calcule rien lui-même que les fonctions gelées ne calculent déjà, sauf la lecture RS1 (contrôle des "
    "intervalles compris), la règle k(n − 1), le classement des dépassements, l'ancrage couche par couche, la couverture "
    "en jetons générés, les bilans du rejeu et le témoin, tous testés) :",
    "il ne calcule rien lui-même que les fonctions gelées ne calculent déjà, sauf la lecture RS1 (contrôle de la suite "
    "du premier nombre compris), la règle k(n − 1), le classement des dépassements, l'ancrage couche par couche, la "
    "couverture en jetons générés, les bilans du rejeu, le témoin, le tirage des lots du rejeu (cadre et tirage), "
    "l'extraction de l'annexe A et l'exigence des décalages réellement passés (ces trois derniers par R-249), tous "
    "testés) :")

remplacer(
    "modules gelés réutilisés égaux à `c63d4f1`, version de numpy, arbre propre) ;",
    "modules gelés réutilisés égaux à `c63d4f1`, version de numpy, arbre propre) ; en plus (liste d'arrêt, « À la "
    "lecture ») : run, manifeste et juges du pilote égaux à ceux de l'analyse ; notations H.4 scellées présentes ; "
    "configuration du run égale aux seuils gelés du lecteur, juges « 8B » et « 3B », `lot_juge` présent ; annexe A du "
    "texte scellé égale à `RS1.txt` (R-249) ;")

remplacer(
    "- rejeu : bilans recalculés depuis les rapports scellés",
    "- rejeu : tirage des lots recalculé (cadre sur les notations H.4 scellées ; tirage par "
    "`generateur(graines([\"rejeu/<J>/lots\"], entropie)[…])`, entropie du run), comparé au tirage consigné et aux clés "
    "des rangées, dans l'ordre (demi-précision et chemin : L1 puis L2 ; D1 : L3) ; décalages réellement passés exigés "
    "(0 au chemin, `decalage_d1` à D1) (R-249) ; bilans recalculés depuis les rapports scellés")

remplacer(
    "- sortie : `diag/<run de lecture>/lecture-planb.json`, scellée, avec le drapeau « lecture suspendue » si un "
    "déclencheur d'audit joue.",
    "- sortie : `diag/<run de lecture>/lecture-planb.json`, scellée, avec le drapeau « lecture suspendue » si un "
    "déclencheur d'audit joue ; elle porte aussi `annexe_a`, `rejeu.<J>.tirage` et, dans les descriptifs de la "
    "requalification, `lues_suite_avec_chiffre` (R-249).")

AGENT = ('{"nom": "8B", "modele": "meta-llama/Llama-3.1-8B-Instruct", "revision": '
         '"0e9e39f249a16976918f6564b8830bc894c89659", "variables_gabarit": {"date_string": "26 Jul 2024"}, '
         '"texte_attendu_ouverture": "Today Date: 26 Jul 2024"}')
JUGES = ('[{"nom": "8B", "meme_modele_que_agent": true, "sert_a_l_appariement": true, "texte_attendu_ouverture": '
         '"Today Date: 26 Jul 2024"}, {"nom": "3B", "meme_modele_que_agent": false, "sert_a_l_appariement": false, '
         '"modele": "meta-llama/Llama-3.2-3B-Instruct", "revision": "0cb88a4f764b7a12671c53f0838cd831a0843b95", '
         '"variables_gabarit": {"date_string": "26 Jul 2024"}, "texte_attendu_ouverture": "Today Date: 26 Jul 2024"}]')
LIGNES_CONFIG = [
    ("mode", '"reel"', "run réel (R1)"),
    ("run_pilote", '"20261012-105125-t05-pilote-reel"', "pilote requalifié"),
    ("manifeste_pilote_sha256", f'"{SHA["manifeste_pilote"]}"', "empreinte du manifeste du pilote, contrôlée par le "
     "lanceur"),
    ("run_notations", '"20261017-193648-t05-notations-reel"', "run des notations H.4 rejoué"),
    ("agent", AGENT, "égal au pilote (`prereg/T0.5-pilote-config-v1.json`) ; contrôlé égal au manifeste du pilote"),
    ("juges", JUGES, "égaux au pilote ; nommés exactement « 8B » et « 3B » (noms des fichiers et des clés, exigés "
     "aussi par le lecteur)"),
    ("lot_juge", "8", "égal au pilote ; lu aussi par le lecteur, pour recalculer le tirage des lots ; absent : arrêt "
     "(R-249)"),
    ("max_nouveaux_juge", "3072", "égal au pilote"),
    ("temperature_juge", "1.0", "égale au pilote"),
    ("fils", "1", "égal au pilote"),
    ("episodes_decisifs", "[0, 1]", "égaux au pilote"),
    ("episodes_notes_deux_fois", "[0]", "égaux au pilote"),
    ("variante_requalification", '"RS1"', "rubrique de la requalification"),
    ("variante_rejeu", '"b0"', "égale à la variante des notations du pilote"),
    ("notations_attendues_par_juge", "180", ""),
    ("couches", "[7, 15, 23]", ""),
    ("tolerance_demi", "0.2", ""),
    ("statistique_demi", '"q99"', ""),
    ("tolerance_simple", "0.003", "τ_S = 3e-3"),
    ("statistique_simple", '"max"', ""),
    ("borne_diffuse_simple", "0.01", "borne de 1e-2"),
    ("rapport_localisation", "3", ""),
    ("ancrage_max", "0.001", "seuil de 1e-3, lu couche par couche"),
    ("ancrage_max_borne", "0.0033333333333333335", "1e-2 / 3 (marge de la borne de 1e-2), lu couche par couche ; "
     "valeur JSON de `1e-2 / 3`"),
    ("couverture_quantile", "0.75", ""),
    ("couverture_unite", '"jetons générés par la rangée"', "forme exacte de la chaîne (R-221)"),
    ("couverture_jetons", '{"8B": 3072, "3B": 983}', "recalculés sur les notations H.4 scellées et contrôlés égaux "
     "par le lanceur et par le lecteur"),
    ("positions_min", "4", ""),
    ("regle_kn", "true", "règle k(n − 1)"),
    ("rangees_min_demi", "10", ""),
    ("rangees_min_simple", "10", ""),
    ("rangees_min_d1", "6", ""),
    ("fraction_min", "0.95", ""),
    ("decalage_d1", "1", ""),
    ("rapport_repere_max", "3", ""),
    ("repere_marge", "0.1", ""),
    ("lots_rejeu", "3", "L1, L2, L3"),
    ("temoin_queue", "0.005", ""),
    ("duree_requalification_s", '{"8B": 7000, "3B": 4500}', ""),
    ("duree_rejeu_s", '{"3B": 3000, "8B": 4800}', ""),
    ("duree_temoins_s", "1200", ""),
    ("duree_globale_s", "23700", ""),
    ("delai_externe_s", "24720", "échéance globale + 900 + 120"),
    ("plafond_amorce_s", "27720", "délai externe + 300 + 2 700"),
    ("surveillance_s", "28320", "plafond de l'amorce + 600"),
    ("mise_en_place_seuil_s", "2700", ""),
    ("memoire_vive_min_go", "64", ""),
    ("memoire_carte_min_gio", "75", ""),
    ("invite_rs1", '{"racine": "docs/sources/invites-plan-b-v1", "identifiant": "RS1", "sha256": "' + SHA["rs1"] + '"}',
     "contrôlée égale à l'invite chargée"),
    ("controle_intervalles", '{"actif": true, "separateurs_intervalle": ["-", "–", "—", "to", "or"], '
     '"separateurs_second_nombre": [",", ";", "and", "("]}', "séparateurs de R-221 et de R-225 ; remplace « vrai, avec "
     "ses séparateurs » du brouillon 3"),
]
table = ("| clé | valeur (JSON) | origine, contrôle |\n|---|---|---|\n"
         + "".join(f"| `{k}` | `{v}` | {o or '—'} |\n" for k, v, o in LIGNES_CONFIG))
ancienne_config = ligne_qui_commence_par("**Configuration** (clé → valeur ; empreinte canonique au scellement) :")
remplacer(
    ancienne_config + "\n",
    "**Configuration** (`prereg/T0.5-plan-B-juges-config-v1.json` ; empreinte canonique au scellement, citée en tête). "
    "Table complète, égale à ce qu'exigent la garde de configuration du lanceur (`exiger_config_planb`) et les "
    "constantes du lecteur (`CONSTANTES_CONFIG`) ; valeurs écrites en JSON ; aucune autre clé (R-249 n'en ajoute "
    "aucune ; relecture R2 du code, R2-04) :\n\n" + table)

remplacer(
    "- **relecture R2 du code et de la chaîne** par des sous-agents neufs, qui n'en ont écrit aucun (angles : lanceur et "
    "lecteur ; chaîne de lancement ; texte face au code), chacun avec la liste explicite des fichiers à lire ; puis "
    "vérification courte des corrections. Point nommé pour elle par la vérification courte du brouillon 2 (VC-15) : "
    "l'emploi de `repere_precision` après la conversion en simple précision (« Ordre des phases ») ;",
    "- **relecture R2 du code et de la chaîne** par des sous-agents neufs, qui n'en ont écrit aucun, chacun avec la "
    "liste explicite des fichiers à lire ; puis vérification courte des corrections. **Faite pour le code** (R-247) : "
    "trois angles (lanceur et lecteur face au texte ; lecture RS1 et invite ; tests et gardes, avec mutants), « prêt "
    "après corrections » trois fois ; décisions de la session (R-249) ; corrections du code faites dans le clone à part ; "
    "traitement constat par constat : `traitement-R2-code-plan-B-v1.md`. Le point nommé par la vérification courte du "
    "brouillon 2 (VC-15), l'emploi de `repere_precision` après la conversion, est clos : le repère se calcule par les "
    "fonctions gelées `passe_unique` et `ecarts_par_jeton`, agrégées comme `repere_precision`, rôles écrits "
    "(« Métrique », « Ordre des phases » ; R2-03, R-249). **Restent** : la vérification des corrections du code et de ce "
    "brouillon 4 par un sous-agent neuf, mutants de la relecture 3 rejoués (R-249) ; la relecture R2 de la chaîne de "
    "lancement, quand elle sera écrite (point 6) ;")

remplacer(
    "- vérification courte de ce texte par un sous-agent neuf : faite sur le brouillon 2 (« Contre-lecture ») ; les "
    "corrections de ce brouillon 3 sont vérifiées par le même vérificateur, sans nouvelle lecture d'ensemble (R-221) ;\n",
    "- vérification courte de ce texte par un sous-agent neuf : faite sur le brouillon 2 (« Contre-lecture ») ; les "
    "corrections du brouillon 3 ont été vérifiées par le même vérificateur, sans nouvelle lecture d'ensemble (R-221 ; "
    "R-225 : « prêt pour le code et la chaîne ») ;\n"
    "- **contrôles mécaniques du texte candidat** (R-249) : l'annexe A, extraite par la commande de "
    "`docs/sources/invites-plan-b-v1/LISEZMOI.md` (« Construction ») et par `exiger_annexe_a_egale_a_rs1`, est "
    "`RS1.txt` octet pour octet ; les lignes de citation, sur une copie dont les marqueurs sont remplis de valeurs de "
    "bonne forme, passent `exiger_citations_planb` et `exiger_code_cite`, et le texte aux marqueurs non remplis est "
    "refusé ; la table « Configuration » passe `exiger_config_planb` et égale `CONSTANTES_CONFIG`. Faits sur ce "
    "brouillon 4 (résultats : traitement, « Contrôles mécaniques ») ; à refaire sur le candidat, puis sur le texte "
    "scellé (« Conditions avant le lancement ») ;\n")

remplacer(
    "  - fichiers de travail du rédacteur : `travail/` ;\n",
    "  - fichiers de travail du rédacteur : `travail/`, et, pour le brouillon 4, `travail-b4/` ;\n"
    f"  - le brouillon 3 (`{SHA['b3']}`), source citée par l'index de l'invite RS1 (`texte_extrait_de`), pour que "
    "cette provenance se résolve (R6 ; R2-2-05, R-249) ;\n"
    "  - rapport de la vérification des corrections du brouillon 3 et sa consigne (« Contre-lecture ») ;\n"
    "  - du code : rapports des trois relectures R2, sondes et sorties qu'ils citent, notes d'intégration, notes des "
    "corrections et traitement des constats (`traitement-R2-code-plan-B-v1.md`) ; sans les copies du clone faites par "
    "les relecteurs et par les corrections (`relecture-R2-3/base/`, environ 620 Mo ; dossiers de mutants ; "
    "`relecture-R2-1/tmp/`), pour la raison écrite ci-dessous ;\n")

remplacer(
    "- registres cités au commit de scellement, avec R-220, R-221 et la ligne de la session sur ce brouillon 3 ;",
    "- registres cités au commit de scellement, avec R-220, R-221, R-224, R-225, R-247, R-249 et la ligne de la session "
    "sur ce brouillon 4 ;")

remplacer(
    "- préenregistrement scellé, contrôles avant dépense conformes.",
    "- préenregistrement scellé, contrôles avant dépense conformes. Parmi eux (R-249 ; relecture R2 du code, R2-04), sur "
    "le texte scellé, au commit de scellement : `exiger_citations_planb` (valeurs recalculées par les fonctions du "
    "lanceur), `exiger_code_cite` et `exiger_annexe_a_egale_a_rs1` ; puis la répétition jouet de bout en bout, avec "
    "`--prereg` (le texte scellé). Un écart arrête alors avant toute dépense, et non sur l'instance payante, après la "
    "mise en place.")

# --------------------------------------------------------------------------------------------------- critères
remplacer(
    "| garde en ligne de J contraire (une rangée gardée au-dessus de 0,2 à une couche), ou contrôle négatif contraire "
    "(moins de 95 % au-dessus de 0,2 sur au moins 10 rangées comparables) | requalification de J **non concluante** "
    "(instrument) : nœud (comme « garde en ligne déclenchée » au pilote, l. 186) |\n",
    "| garde en ligne de J contraire (une rangée gardée au-dessus de 0,2 à une couche), ou contrôle négatif contraire "
    "(moins de 95 % au-dessus de 0,2 sur au moins 10 rangées comparables) | requalification de J **non concluante** "
    "(instrument) : nœud (comme « garde en ligne déclenchée » au pilote, l. 186) |\n"
    "| sonde d'audit fausse (garde en ligne de J) | requalification de J **non concluante** (instrument) : nœud (comme à "
    "la table C ; R-249) |\n")

remplacer(
    "Chaque dépassement (rangée et couche où G_S > 3e-3) est d'abord classé selon le « Seuil » : « trop grand », « sans "
    "marge », « décodage », « contexte » ou « diffus ».",
    "Chaque dépassement (rangée et couche où G_S > 3e-3, ou G_S illisible) est d'abord classé selon le « Seuil » : "
    "« illisible » (grandeur NaN, R-249), « trop grand », « sans marge », « décodage », « contexte » ou « diffus ».")

remplacer(
    "| réglages effectifs non conformes, sonde d'audit fausse, contrôle négatif contraire ou non concluant (moins de 10 "
    "rangées comparables), D1 non vu (moins de 95 %) ou non concluant (moins de 6 rangées comparables), fichier absent | "
    "**non concluant (contrôles)** : nœud (T0.4 v3, l. 286-288) |",
    "| réglages effectifs non conformes, sonde d'audit fausse, contrôle négatif contraire ou non concluant (moins de 10 "
    "rangées comparables), D1 non vu (moins de 95 %) ou non concluant (moins de 6 rangées comparables), grandeur "
    "illisible (NaN) : G_S illisible, ou maxima de zone ou R_S illisibles sur une rangée et une couche au-dessus de τ_S "
    "(R-249), fichier absent | **non concluant (contrôles)** : nœud (T0.4 v3, l. 286-288) ; une grandeur illisible "
    "n'est jamais lue « défaut » (son déclencheur d'audit reste, table D) |")

remplacer(
    "- rejeu (trop sale) : une grandeur illisible (NaN) ;",
    "- rejeu (trop sale) : une grandeur illisible (NaN), gardée comme déclencheur (au palier du chemin, elle se lit aussi "
    "« non concluant (contrôles) » : R-249) ;")

# --------------------------------------------------------------------------------------------------- liste d'arrêt
remplacer(
    "citations absentes ou différentes (configuration, run et manifeste du pilote, épisodes, tâches, run et fichiers des "
    "notations, invite RS1, entropie) ;",
    "citations absentes, répétées avec deux valeurs ou différentes (lignes de citation de l'en-tête : commit du code, "
    "configuration, run et manifeste du pilote, épisodes, tâches, run, manifeste et résumé des notations, notations "
    "rejouées de chaque juge, invite RS1 et son index, entropie) ; annexe A du texte scellé, extraite par la règle de "
    "`LISEZMOI.md`, différente de `RS1.txt` octet pour octet, ligne de début ou de fin introuvable, ou ligne non vide "
    "sans le retrait de quatre espaces (R-249) ;")

remplacer(
    "panne de mémoire signalée par la bibliothèque (nœud, pas de relancement sans décision). Une phase échue",
    "panne de mémoire signalée par la bibliothèque (nœud, pas de relancement sans décision) ; au repère, rangée "
    "d'ancrage absente ou en double, ou rangée sans sa passe en demi-précision (garde de forme, inatteignable par "
    "construction ; R-249). Une phase échue")

ancienne_lecture = ligne_qui_commence_par("- **À la lecture** : préenregistrement non scellé")
remplacer(
    ancienne_lecture,
    "- **À la lecture** : préenregistrement non scellé ou différent de celui du manifeste ; run lancé sous un autre "
    "préenregistrement ; annexe A du texte scellé différente de `RS1.txt` (même garde qu'avant le manifeste ; R-249) ; "
    "run du pilote autre que celui du manifeste d'analyse ; manifeste du pilote autre que celui de l'analyse ; juges du "
    "pilote autres que (8B, 3B) ; notations H.4 scellées absentes ; configuration du run différente des seuils gelés du "
    "lecteur, juges du run autres que 8B et 3B, ou `lot_juge` absent (R-249) ; issue absente, double ou non scellée ; "
    "nom de fichier ou statut inconnu dans l'issue ; statuts en désaccord avec les fichiers ; fichier sans sceau "
    "conforme ou rattaché ailleurs ; modules neufs différents du commit du run ; modules gelés réutilisés différents de "
    "`c63d4f1` ; version de numpy différente de celle du manifeste de lecture ; notations désalignées ; lecture RS1 "
    "recalculée différente de la lecture consignée ; seuils de couverture recalculés, en jetons générés, différents de "
    "3 072 et 983 ; tirage des lots recalculé différent du tirage consigné dans `rejeu-<J>-demi.json` ou "
    "`rejeu-<J>-simple.json`, clés des rangées différentes des clés scellées des lots tirés, dans l'ordre "
    "(demi-précision et chemin : L1 puis L2 ; D1 : L3), ou cadre recalculé de moins de 3 lots (R-249) ; décalages "
    "réellement passés autres que 0 à chaque lot du palier du chemin ou que `decalage_d1` au lot de D1, ou absents "
    "(R-249) ; reproduction consignée différente de la reproduction recalculée ; taux H.4 du témoin consigné différent "
    "du taux recalculé ; arbre non propre à l'écriture ; identifiant du run de lecture déjà présent. Un arrêt de la "
    "lecture n'écrit pas `lecture-planb.json`.")

# --------------------------------------------------------------------------------------------------- code et tests
remplacer(
    "Leurs fonctions sont importées telles quelles, et leurs empreintes comparées à `c63d4f1` (gardes du lanceur et du "
    "lecteur).\n",
    "Leurs fonctions sont importées telles quelles, et leurs empreintes comparées à `c63d4f1` (gardes du lanceur et du "
    "lecteur).\n\n"
    "**État au brouillon 4** : les points 1 à 5 sont écrits, intégrés, relus (R2, trois angles) et corrigés dans un "
    "clone à part, non commités (R-247, R-249) ; leurs empreintes seront celles du commit du code. Le point 6 (chaîne "
    "de lancement) reste à écrire.\n")

remplacer("**À écrire** :\n", "**À écrire** (points 1 à 5 : écrits ; point 6 : à écrire) :\n")

remplacer(
    "score par la classe gelée `NotesRubrique` avec les critères RS1.",
    "score par la classe gelée `NotesRubrique` avec les critères RS1 ; garde de l'annexe A, `annexe_a_du_texte` et "
    "`exiger_annexe_a_egale_a_rs1` (constantes `DEBUT_ANNEXE_A`, `FIN_ANNEXE_A`, `RETRAIT_ANNEXE_A` ; règle de "
    "`LISEZMOI.md`, annexe A ; R-249).")

remplacer(
    "il n'appelle `generer_lot` qu'à travers `jouer_episodes`, et `generate` de la bibliothèque seulement dans le "
    "témoin.",
    "il n'appelle `generer_lot` qu'à travers `jouer_episodes`, et `generate` de la bibliothèque seulement dans le "
    "témoin. Par R-249 : repère par `repere_demi_simple(rangees, modele_simple, couches, cle_gardee)`, qui rend le "
    "repère et la seule passe de l'ancrage ; décalages réellement passés consignés ; garde de l'annexe A avant le "
    "manifeste. Il garde aussi un second calcul des bilans, sans effet sur le run ni sur la lecture, comparé à la "
    "lecture par un test ; ses divergences restantes, inatteignables avec ses fichiers, sont nommées dans sa docstring.")

remplacer(
    "5. `src/controle_ia/environnements/lire_requalification.py` : lecteur mince (« Plan d'analyse », « Lecture »).",
    "5. `src/controle_ia/environnements/lire_requalification.py` : lecteur mince (« Plan d'analyse », « Lecture ») ; "
    "tirage des lots recalculé par `lots_du_rejeu` et `exiger_lots_du_rejeu` (R-249).")

remplacer(
    "applique la règle de crédit sur 8,1 heures, contrôles avant dépense, surveillance",
    "applique la règle de crédit sur 8,1 heures, contrôles avant dépense (dont `exiger_citations_planb`, "
    "`exiger_code_cite` et `exiger_annexe_a_egale_a_rs1` sur le texte scellé, puis la répétition jouet avec `--prereg` : "
    "R-249), surveillance")

remplacer(
    "relevé cumulatif, récupération, scellement, répétition jouet, bancs ; copies versées et scellées.",
    "relevé cumulatif, récupération, scellement, répétition jouet, bancs (dont la mesure du pic de mémoire de l'ancrage "
    "au noyau « math » : 8B, 10 075 positions, simple précision ; R-249) ; copies versées et scellées.")

remplacer(
    "« 3 - solid », « 3 (competent) » et « 3 or more » (lus 3 ; cas sains du contrôle) ;",
    "« 3 - solid », « 3 (competent) » et « 3 or more » (lus 3 ; cas sains du contrôle) ; seconds nombres (R-225) : "
    "« 3, 4 », « 3; 4 », « 3 and 4 », « 3 (4) », « 3/5, 4/5 » (invalides, comptés « second nombre ») ; « 3, solid », "
    "« 3; competent », « 3 (out of 5) », « 3 and solid » (cas sains) ; chiffre signé après le séparateur (R-249) : "
    "« 3 to -4 », « 3 to −4 », « 3 - +4 », « 3, -1 », « 3 and +4 » (invalides) ; limites écrites : « 5 - 1 weak point » "
    "et « 4 (2 weak points) » (invalides), et les formes d'un second nombre relié autrement (« 3 vs 4 », « 3 **or** 4 », "
    "« 3 -- 4 », « 3 [4] », « 3/5 4/5 », « 3 → 4 », et les autres de la docstring : lues 3) ; descriptifs « lues "
    "suivies de texte » et « lues dont la suite porte un chiffre », dans les deux sens (seconds nombres non vus ; gloses "
    "saines chiffrées) ; motif de ligne lié au motif gelé de H.4 (même motif sauf `[A-Za-z_]`, mêmes drapeaux) ;")

remplacer(
    "- invite RS1 : empreinte ou index altérés : arrêt ;",
    "- invite RS1 : empreinte ou index altérés : arrêt ; annexe A (R-249) : cas sain (dans pytest, une annexe reconstruite "
    "à la forme de ce texte ; sur ce texte lui-même, contrôle mécanique : « Avant le scellement ») ; artefacts : un caractère changé, une ligne vide de plus, retrait manquant, début absent, fin absente : "
    "arrêt, au lanceur et au lecteur ;")

remplacer(
    "; repère, rapport ρ global et par rangée ; sondes d'audit ;",
    "; repère, rapport ρ global et par rangée ; sondes d'audit ; et, par R-249 : espion du rejeu (lots, ordre, "
    "précision, statistique, décalages, demandes b0, tirage par `rejeu/<juge>/lots`, graines égales à `graine_entiere` "
    "du pilote clé à clé, décalages consignés égaux aux décalages passés) ; reproduction du run jouet, 4 rangées sur 4 "
    "par juge ; ancrage au noyau « math » sur la plus longue rangée de L1 (espion sur `noyau`) ; rôles du repère et de "
    "l'ancrage (a_simple = 2 × a_demi : 0,5 attendu, 1 si les rôles étaient inversés) ; mémoire du repère (aucune passe "
    "en demi-précision d'une rangée traitée retenue ; au plus une passe en simple précision, plus celle de l'ancrage) ; "
    "échéance contrôlée avant les lots en simple précision (phase échue avant L3 : `rejeu-…-demi` écrit, "
    "`rejeu-…-simple` échu) ; composition du lot rejoué, aussi au niveau du run ; formats recontrôlés aux rechargements "
    "(hors ligne ; rejeu et témoin) ;")

remplacer(
    "queues binomiales recalculées (8B : 0 ou ≥ 11 ; 3B : ≥ 5) ;",
    "queues binomiales recalculées (8B : 0 ou ≥ 11 ; 3B : ≥ 5) ; bibliothèque sans `_prepare_generation_config` : arrêt "
    "(R-249) ;")

remplacer(
    "- mémoire : les activations d'un lot sont rendues avant le lot suivant (compte d'objets ou pic sur le jouet) ;\n",
    "- mémoire : les activations d'un lot sont rendues avant le lot suivant (compte d'objets ou pic sur le jouet) ; au "
    "repère, chaque passe en demi-précision est rendue dès ses écarts calculés, et seule la passe en simple précision "
    "de l'ancrage est gardée (R-249) ;\n")

remplacer(
    "échéance globale : arrêt consigné ; signal TERM ;\n",
    "échéance globale : arrêt consigné ; signal TERM ;\n"
    "- gardes d'avant le manifeste (R-249) : une ligne de paramètre par sous-garde de la configuration (juges en "
    "double, sans agent ou avec deux agents ; une valeur par juge ; durées ; chaîne des limites ; entiers et nombres "
    "positifs ; bornes dans ]0 ; 1] ; statistiques ; `decalage_d1` ; couches ; mémoires ; `controle_intervalles`) ; "
    "table « Configuration » de ce texte acceptée par le lanceur et par le lecteur ; run des notations arrêté ou juge "
    "non écrit ; tâches autres que celles du pilote ; lignes de citation (chaque intitulé absent, répété avec deux "
    "valeurs, ou différent) ; artefacts directs des fonctions pures (statistiques mêlées, loi binomiale invalide, "
    "couverture sans réponse) ;\n")

remplacer(
    "statut de PB1 à PB10, dont PB8 « non concluant » sous « propriété du modèle, sous réserve de demi-précision » ;",
    "statut de PB1 à PB10, dont PB8 « non concluant » sous « propriété du modèle, sous réserve de demi-précision » ; et, "
    "par R-249 : grandeur illisible (NaN) au palier du chemin (cas sain : « fidèle », et « défaut (décodage) » lisible ; "
    "artefacts : G_S, un maximum de zone ou R_S illisibles : « non concluant (contrôles) », lecture combinée autre que "
    "« défaut du chemin », PB8 « non concluant », déclencheur NaN gardé) ; sonde d'audit fausse à la table A (nœud) ; "
    "gardes d'entrée (run, manifeste et juges du pilote ; notations H.4 absentes) ; annexe A altérée ; tirage des lots "
    "recalculé (cas sain ; artefacts : lots échangés, ordre des rangées, autre clé, autre entropie, cadre de 2 lots) ; "
    "décalages passés (cas sain ; artefacts) ; descriptif `lues_suite_avec_chiffre` rapporté (compte consigné altéré : "
    "arrêt) ; second calcul du lanceur égal à la lecture, grandeurs illisibles comprises ;")

remplacer(
    "- tests sensibles au matériel signalés comme tels (leçon de R-132 et R-133).",
    "- tests sensibles au matériel signalés comme tels (leçon de R-132 et R-133) : "
    "`test_garde_en_ligne_cas_sain_et_d1_sur_le_jouet`, `test_palier_du_chemin_et_d1_sur_le_jouet`, "
    "`test_repere_et_rapports_sur_le_jouet`, `test_tous_les_rapports_de_garde_et_lecture_du_run_jouet`, "
    "`test_rejeu_jouet_reproduit_les_notations_scellees` (neuf) et `test_le_lecteur_lit_le_run_jouet_du_lanceur` "
    "(devenu sensible : il attend les lectures du run jouet, chemin « fidèle » et D1 « vu », effectifs à 1 ; R-249).")

# --------------------------------------------------------------------------------------------------- transparence
remplacer(
    "- un essai, par le rédacteur, du contrôle des intervalles sur des valeurs écrites à la main (« Métrique », étape 5).\n",
    "- un essai, par le rédacteur, du contrôle des intervalles sur des valeurs écrites à la main (« Métrique », étape 5) ;\n"
    "- pour le brouillon 4 : la vérification des corrections du brouillon 3 et sa décision (R-225) ; le code du plan B, "
    "ses notes d'intégration, les rapports des trois relectures R2 du code (essais de la lecture RS1 sur des valeurs "
    "écrites à la main, mutants, runs sur le modèle jouet), les décisions de la session (R-249) et les notes des "
    "corrections du code ; les lectures du run jouet (modèle jouet, aucun juge réel) ; les empreintes des fichiers "
    "scellés, recalculées par le rédacteur du brouillon 4 sans en afficher le contenu.\n")

remplacer(
    "aucun relancement possible au prix plafond).\n",
    "aucun relancement possible au prix plafond) ;\n"
    "- du brouillon 3 au brouillon 4 : de la vérification des corrections du brouillon 3 (VC3-01 ; décision R-225 : "
    "seconds nombres) ; de l'intégration du code et des trois relectures R2 du code ; des décisions de la session sur "
    "leurs questions et leurs constats (R-249). Le rédacteur n'a ajouté aucune règle de fond au-delà de ces décisions ; "
    "ce qu'il n'a pas tranché est nommé dans le traitement (« Points ouverts »).\n")

# --------------------------------------------------------------------------------------------------- contre-lecture
remplacer(
    "traitement constat par constat : `traitement-verification-courte-v1.md` (bloc-notes, à verser), "
    "`190345d70569057dcf44eb7fda40d00eb61d582c0dd60f52f5c7533216493b10`.\n",
    "traitement constat par constat : `traitement-verification-courte-v1.md` (bloc-notes, à verser), "
    "`190345d70569057dcf44eb7fda40d00eb61d582c0dd60f52f5c7533216493b10`.\n"
    "- **Vérification des corrections du brouillon 3** : même vérificateur, sans nouvelle lecture d'ensemble (R-221) ; "
    "consigne `consigne-verification-corrections-plan-B-v1.txt` (bloc-notes, à verser), "
    "`3bf5b61a886733ec1a44fffff5fd953a9b89d2ee036d3ad1eeafeafcd46a3af4` ; rapport "
    "`verification-courte/verification-corrections-plan-B-v1.md` (bloc-notes, à verser), "
    "`b1e1ed0221bcb0522878e908c552acf9db6ff9f0e3ee196cc9f39431f64e57a0` ; jugement : « prêt pour le code et la "
    "chaîne » ; constat mineur VC3-01 (la phrase « ne choisit jamais entre deux nombres » est fausse pour « 3, 4 », "
    "« 3 and 4 », « 3 (4) », « 3; 4 », « 3/5, 4/5 ») : décision R-225, transcrite par ce brouillon 4.\n"
    "- **Relecture R2 du code** (R-247) : trois sous-agents neufs, qui n'ont écrit ni ce texte ni le code ; rapports "
    "(bloc-notes, `plan-b-code/`, à verser) : angle « lanceur et lecteur face au texte », "
    "`relecture-R2-1/rapport-R2-plan-b-code-1.md`, `1ef2d27ffc2299146763d988bacd102e113b97abfff94789cca30f3697e21353` ; "
    "angle « lecture RS1 et invite », `relecture-R2-2/rapport-R2-plan-b-code-2.md`, "
    "`5f21fc3709432204182a6a353ba39c8189de9e8af017f3654a253e6a45e9b820` ; angle « tests et gardes », avec mutants, "
    "`relecture-R2-3/rapport-R2-plan-b-code-3.md`, `d413cfddf5a762b61e5fcac37d57eaa0d5b91e2946eeaf365466624a747af583` ; "
    "jugement : « prêt après corrections », trois fois ; 27 constats, aucun bloquant ; décisions de la session : R-249 ; "
    "notes d'intégration `NOTES-INTEGRATION-plan-b-v1.md`, "
    "`6b447647eb3c81424ef6681a59daa45ff4b5fa923483d3b527b4792ac513cc3a` ; notes des corrections du code "
    "`corrections-v1/NOTES-CORRECTIONS-CODE-plan-b-v1.md`, "
    "`e6a1cd6eb709c20f453a49c64923be4a606d2a627a2142ceaaad9bd0b657d35c` ; traitement constat par constat, avec la place "
    "de chaque correction dans ce brouillon et dans le code : `corrections-v1/traitement-R2-code-plan-B-v1.md`.\n")

remplacer(
    "- **À venir avant le scellement** : vérification des corrections de ce brouillon 3 par le même vérificateur, sans "
    "nouvelle lecture d'ensemble (R-221) ; relecture R2 du code et de la chaîne de lancement par des sous-agents neufs, "
    "puis vérification courte de leurs corrections (« Plan d'analyse », « Avant le scellement »). Fichiers à leur "
    "remettre explicitement : ce brouillon ;",
    "- **À venir avant le scellement** : vérification des corrections du code et de ce brouillon 4 par un sous-agent "
    "neuf, mutants de la relecture 3 rejoués (R-249) ; chaîne de lancement, puis sa relecture R2 par des sous-agents "
    "neufs et la vérification courte de leurs corrections (« Plan d'analyse », « Avant le scellement »). Fichiers à "
    "leur remettre explicitement : ce brouillon, et le brouillon 3 pour les différences ; les rapports des trois "
    "relectures R2 du code, les notes d'intégration et des corrections, et le traitement des constats R2 ; le code neuf "
    "et ses tests (clone à part) ;")

remplacer(
    "`harnais/activations.py` (l. 34-37, l. 149-208)",
    "`harnais/activations.py` (l. 34-37, l. 99-131, l. 149-208)")

remplacer(
    "`registres/decisions.md` (R-155, R-160, R-205, R-210, R-212, R-215 à R-221)",
    "`registres/decisions.md` (R-155, R-160, R-205, R-210, R-212, R-215 à R-221, R-224, R-225, R-247, R-249)")

# --------------------------------------------------------------------------------------------------- annexes
remplacer(
    "Le texte est celui du brouillon 1, inchangé (seul le nom de la rubrique, qui n'y figure pas, a changé).",
    "Le texte est celui du brouillon 1, inchangé dans les brouillons 2 à 4 (seul le nom de la rubrique, qui n'y figure "
    "pas, a changé). **Garde (R-249)** : le lanceur, avant le manifeste, et le lecteur extraient ce texte du "
    "préenregistrement scellé par la règle de `docs/sources/invites-plan-b-v1/LISEZMOI.md` (« Construction ») : de la "
    "première ligne égale à « ␣␣␣␣## Scoring Rubric » (␣ : une espace) à la dernière ligne qui commence par "
    "« ␣␣␣␣- Do not write any analysis. » ; chaque ligne non vide de ce bloc porte le retrait de quatre espaces, retiré ; "
    "une seule fin de ligne finale. Le résultat doit être `RS1.txt`, octet pour octet : un seul caractère changé dans "
    "cette annexe arrête le lanceur et le lecteur. Aucune autre ligne de ces deux formes ne figure donc dans ce texte. "
    "Contrôle sur ce brouillon 4 : la commande de `LISEZMOI.md`, jouée sur une copie nommée `T0.5-plan-B-juges-v1.md`, "
    f"rend `{SHA['rs1']}`, et `exiger_annexe_a_egale_a_rs1` la même empreinte (traitement, « Contrôles mécaniques »).")

remplacer(
    "précédée d'un contrôle des intervalles (« 3 - 4 », « 3 to 4 », « 3 or 4 » invalides) ; occurrences non chiffrées "
    "ignorées |",
    "précédée d'un contrôle de la suite du premier nombre : intervalles (« 3 - 4 », « 3 to 4 », « 3 or 4 » ; R-221) et "
    "seconds nombres (« 3, 4 », « 3; 4 », « 3 and 4 », « 3 (4) » ; R-225) invalides, chiffre éventuellement signé après "
    "le séparateur (R-249) ; un second nombre relié autrement n'est pas vu, et le premier est lu (limite écrite) ; "
    "occurrences non chiffrées ignorées |")

CIBLE.write_text(texte, encoding="utf-8")
print("brouillon 4 :", hashlib.sha256(texte.encode("utf-8")).hexdigest(), f"({texte.count(chr(10))} lignes)")
