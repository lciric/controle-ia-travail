# Note au rapport du développeur — code de l'organisme retenu, version 5 — v3 (deux restes avant l'ordre de l'étalonnage)

Date : 2026-11-21. Pièce d'instrument (classe B). Même développeur, même mandat, même arbre (branche locale `prep/iib-code-v5-local`, jamais poussée). Complète les rapports v1 (`109fc082…`) et v2 (`5b71aa0e…`), intacts. Vérification traitée : `brouillons/ii-b-saboteur-budget-v5/code-v5/contre-lecture-cl1/verification-corrections-code-organisme-retenu-v5-cl1.md` (compagnon vérifié), lue en entier : « autorisable après deux restes ».

- **Commit de tête** : `38a7475f5`, par-dessus `74438c4fc`. `correctifs-v3/0008-….patch` (`git format-patch --start-number 8 74438c4fc..HEAD`).
- Rien poussé, aucune dépense, aucune machine, aucun appel à un loueur (faux outil seulement), aucun fichier supprimé, aucune consigne privée lue, aucun refus d'outil.

## Table de traitement

| reste | traitement | où | essais |
|---|---|---|---|
| **R1**, clé en gras fermée après les deux-points | **corrigé** : règle de coupe de la version 1 reprise — le plus petit rang dont le décodage, nettoyé du gras, finit par la clé ; la coupe peut tomber après les marques qui ferment la clé et les espaces, jamais après un saut de ligne ; la fenêtre commence après elles. Le jeton « :\n » ne change pas : aucune coupe conforme, l'action est comptée. | `lecture_cout_v5.coupe_du_prefixe` | tokeniseur réel : 16 cas neufs par décodage (« **COST:** » et « __COST:__ » × quatre valeurs : coupe conforme, lecture égale des deux côtés, réécriture retrouvée avec les marques gardées à la clé, multiplication) ; trois formes de clé de plus dans l'essai de la coupe ; le constat « :\n » reste écrit |
| **R2**, amorce v5 et lanceur de session v3 jamais joués | **joué** : `scripts/repetition_locale_iib_v5.py`, bout en bout, mode jouet, faux outil de location, origine locale. Sortie : `sortie-repetition-locale-v1.txt`. | script neuf | voir ci-dessous |
| n1, attestation « aucune intouchable » | **corrigé** dans `scripts/lancer_iib_v3.sh` : la variable posée est un refus ; la liste vide ou absente est un refus, sans attestation possible. | `lancer_iib_v3.sh` (destruction) | deux artefacts joués dans la répétition (code 2) ; différences bornées (15 lignes retirées de la version 2) |
| n2, calendrier | **corrigé** : en mode réel, `calendrier` égal aux dates de la ligne : `dernier_jour_creation` 2026-11-26, `fin_go_utc` 2026-12-01T00:00:00Z. | `configuration_v5.exiger_location` | `test_sections_de_location_…` (cinq artefacts de calendrier) |
| entropie de la mère | **portée** : gabarit en version 3, `docs/notes/barreau8-iib-v1/config-iib-organisme-retenu-v5-gabarit-v3.json` (`d561776e…`), entropie 34177889608133376136283958643409181656, calendrier rempli. Les versions 1 et 2 restent, intactes. | gabarit v3 | `test_gabarit_de_configuration_verse_au_depot` |

**Lecture à confirmer (n2).** « Dernière création le 2026-11-27T00:00Z » est lue comme : dernier jour de création le 26 (le contrôle de session admet une création tant que le jour ne dépasse pas ce jour-là). Si la ligne veut dire « le 27 compris », la constante est à changer avant l'ordre. L'échéance du 30 donne une fin de ligne au 1er décembre 00:00Z, comme le contrôle de session l'exige.

## La répétition locale (R2)

Ce qu'elle joue, dans l'ordre : lanceur de session v3 `outil`, `controles-explo`, `creation` (la commande est imprimée, jamais exécutée) ; l'amorce v5 telle que la création l'a relevée au commit, en essai local (`AMORCE_ESSAI_LOCAL=1` : ni minuterie ni loueur), qui clone l'origine locale, relit l'accord et le calendrier, joue la suite d'essais, puis lance le vrai `lanceur_v5 --phase etalonnage` sur le monde jouet, consigne et pousse ; puis `apres-creation`, `surveillance`, trois refus de `destruction` et la destruction par identifiant ; enfin `--phase conditions` sur un clone des sorties poussées, et son second passage refusé.

- Premier passage, suite d'essais courte : réussi (étalonnage en 28 lots poussés, 28 lots d'identifiants, résumé ; inventaire après destruction : la seule machine de l'autre chantier ; aucun appel de création ; issue de la désignation P, 12 tours).
- Deuxième passage, liste d'essais figée entière : **en échec, et utile** (`sortie-repetition-locale-passage-en-echec-v1.txt`). Deux causes, toutes deux corrigées : (a) mon dépôt factice ne portait pas le gabarit de configuration que lit un essai (sur la machine réelle, `docs/notes/` est cloné) ; (b) **constat pour l'ordre** : l'essai du tokeniseur réel, sauté sur la machine, donne une dernière ligne « N passed, 1 skipped », que le contrôle du nombre de tests attendus de l'amorce refuse. La liste figée passe donc en version 3 (`scripts/tests-cibles-iib-v5-v3.txt`, 20 fichiers, sans cet essai ; la version 2 reste). L'amorce a fini proprement sur cet échec : arrêt consigné, branche poussée, aucun run.
- Troisième passage, liste figée en version 3 et `TESTS_ATTENDUS=205` : voir la fin de `sortie-repetition-locale-v1.txt`.

**Ce que la répétition n'éprouve pas** : le mode réel (carte, modèle, consignes, tâches réelles) ; la minuterie de destruction et les appels au loueur de l'amorce (coupés par l'essai local) ; la commande de création elle-même (imprimée seulement) ; la règle de surveillance à 12 dollars, non écrite. En essai local et mode jouet, l'amorce retire `IIB_GO_ID` de l'environnement du lanceur ; sur une machine réelle, le mode jouet est refusé.

## Essais (fichier `sortie-essais-cibles-v5-v3.txt`)

Les vingt fichiers en version 5 hors l'essai long, tokeniseur réel compris, au commit `38a7475f5` : **359 réussis** (voir le fichier). L'essai long (200 graines) est rejoué par l'amorce dans la répétition à liste figée.

## Pour l'ordre

- Liste des essais de l'amorce : `scripts/tests-cibles-iib-v5-v3.txt` (20 fichiers, empreinte en dur dans l'amorce) ; nombre de tests attendus : **205** (`IIB_TESTS_ATTENDUS=205`), essai long compris (environ sept minutes de carte).
- Le risque « :\n » reste à écrire dans l'ordre (vérification, point 2).

## La configuration de l'étalonnage sert-elle aussi à la course ? (question de la session mère, sur le rapport du distillateur)

**Oui.** `lanceur_v5.phase_course` reçoit la configuration de l'étalonnage et en dérive celle de la course par `designation_v5.configuration_de_course` : une copie où seul `oracle_de_la_regle` est écrit (issue et empreinte du résultat scellé de la désignation) ; elle refuse une configuration qui en porte déjà un. Aucune autre section n'est ajoutée à ce moment-là.

**Dans le code rendu (tête `38a7475f5`), il n'y a pas de place pour `distillation_evaluation`** : `configuration_v5.exiger_config_v5` refuse toute clé inconnue, donc la configuration de l'étalonnage ne peut pas la porter, même vide. Je n'ai rien changé pour cela, comme commandé.

**Ce qu'il faudrait pour y laisser une place sans la remplir**, au choix :
1. *La place dans la configuration de l'étalonnage* : ajouter `distillation_evaluation` aux clés permises et non exigées de `exiger_config_v5` (une ligne), valeur `null` au gabarit, non lue par l'étalonnage ; le distillateur exigerait qu'elle soit remplie et vérifiée avant la course. Mais la remplir ensuite change le fichier de configuration, donc son empreinte : la configuration de la course ne serait plus celle que le manifeste de l'étalonnage a scellée, plus la désignation. Pour que ce soit la même, la section doit être **remplie et scellée dès l'étalonnage**, ce qui n'est pas « sans la remplir ».
2. *La place à la course* (ce que le code fait déjà pour l'oracle de la règle) : laisser la configuration de l'étalonnage telle quelle, et faire écrire la section par la fonction qui dérive la configuration de course, à partir d'une pièce scellée à part citée par son chemin et son empreinte. La configuration de l'étalonnage reste alors inchangée et son empreinte tient ; il faut seulement que `exiger_config_v5` permette la clé, et qu'aucune vérification n'exige l'égalité stricte des deux configurations hors `oracle_de_la_regle` (aucune ne le fait aujourd'hui).
À noter pour ce choix : rien, dans le code rendu, ne compare la configuration passée à `phase_course` à celle du manifeste de l'étalonnage ; si l'on veut « la même configuration », cette garde est à écrire avec la course.
