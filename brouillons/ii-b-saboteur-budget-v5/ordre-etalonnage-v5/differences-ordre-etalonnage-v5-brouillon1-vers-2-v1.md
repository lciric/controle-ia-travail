# Différences — ordre de l'étalonnage de l'organisme retenu, du brouillon 1 au brouillon 2 — v1

Source : `ordre-etalonnage-ii-b-v5-brouillon1.md` (`db7f4dc042b43776dba1cc2553ac60fd8cc3f8860138adf4b48192b965c04549`). Produit : `ordre-etalonnage-ii-b-v5-brouillon2.md` (`adf8dbacdfe533148a279ecde23a71d090ad349a564af555826ae55415ef6795`). Écrite par le programme `fabriquer-ordre-etalonnage-ii-b-v5-brouillon2-v1.py`, le 2026-11-21 vers 19:24 UTC. Une différence par ligne ; tout le reste est recopié à l'octet.

## Remplacements, un par ligne (ancre trouvée le nombre de fois attendu)

- titre : « machine à part — brouillon 1… » remplacé par « machine à part — brouillon 2 ».
- statut : « - **Statut** : brouillon 1, pièce décisive (ordre d'une course payante), non contre-lu. Fabriqué par programme… » remplacé par « - **Statut** : **brouillon 2**, pièce décisive (ordre d'une course payante), non contre-lu. Fabriqué par programme (`fabriquer-ordre-etalonnage-ii-b-v5-brouillon2-v1.py`) depuis le brouillon 1 (`ordre-etalonnage-ii-b-v5-brouillon1.md`, `db7f4dc042b43776dba1cc2… ».
- ligne d'accord, mot de Lazar pour la création : « Le mandat cite aussi `GO-2026-11-21-74` (« l'étalonnage dès ce soir si les épreuves le permettent ») : ligne n… » remplacé par « Ligne `GO-2026-11-21-74`, lue au brouillon 2 au registre de `main` (tête `f390cf712aba0896c48132735244a07b064360af`) : mots de Lazar vers 18:30Z, « 22 au soir : création, puis étalonnage. pourquoi pas dès ce soir ? ». ».
- pièces citées, ajouts : « « autorisable », deux restes portés ici (§ 3).… » remplacé par « « autorisable », deux restes portés ici (§ 3). **Au brouillon 2** (empreintes recalculées par le programme) : erratum 2 du texte scellé (`ab020d438cb6eaa46cd2df0a6ed76952b5dfb23497438e0f2b3fb4590b1d26e2` : épisodes distillés jusqu'à 127, 3 830 actions d'oracle… ».
- code lu, ajout : « **Des correctifs neufs arrivent** (point d'entrée en version 5, amorce en version neuve, et les corrections de… » remplacé par « **Au brouillon 2** : les douze correctifs du § 11 appliqués dans l'ordre dans le dossier du rédacteur, pour la lecture des scripts et des modules en version 5 seulement ; lus : les différences de `scripts/lancer_iib_v3.sh` avec la version 2, l'en-tête et les l… ».
- § 1, ligne du code : « | Code | commit du code revu `<<COMMIT_CODE_REVU_V5>>` sur `<<BRANCHE_CODE_V5>>` : base `836c7cccda5071fe54ecb… » remplacé par « | Code | base `836c7cccda5071fe54ecb148d214d74b5cb90474` (`origin/prep/iib-code-v4`), plus les douze correctifs du § 11, appliqués dans l'ordre ; tête locale du développeur `45f9ba7aaca27fdab8a458072f883825991dd2fb`, arbre `9917b13f3c57d0eeacf3b72fea9607a103da… ».
- § 1, ligne de l'amorce : « | Amorce | `<<AMORCE_V5_CHEMIN_ET_EMPREINTE>>` ; l'amorce… » remplacé par « | Amorce | `scripts/amorce_instance_iib_v5.sh` (`42196f90da0f104fb36a5f618a14e44ef03863d0541bb3b77f1f29f130a9e43c` à la tête du code) : elle joue la liste figée, puis `python -m controle_ia.iib.lanceur_v5 --phase etalonnage` ; jouée en essai local par la répét… ».
- § 1, ligne des essais : « | Essais | suite ciblée en version 5, `scripts/tests-cibles-iib-v5.txt` (`<<LISTE_ESSAIS_V5_EMPREINTE>>` ; vin… » remplacé par « | Essais | liste figée `scripts/tests-cibles-iib-v5-v4.txt` (`342ee21d495b54cb5fd4a8ae6d7427043edb3c228cc16afd57ab4f9e3d099b68`, écrite en dur dans l'amorce ; 23 fichiers, sans l'essai du tokeniseur réel ni celui du moteur à torch du distillateur, qui se saute… ».
- § 1, calendrier : « **aucune création après 2026-11-27T00:00Z** (ligne d'accord, choix (d) ;… » remplacé par « **aucune création à partir de 2026-11-27T00:00:00Z, instant exclu : dernier jour de création le 2026-11-26** (`calendrier.dernier_jour_creation` du gabarit, vérifié à l'égalité en mode réel ; lecture du développeur, notes v3 et v4) (ligne d'accord, choix (d) ; ».
- § 1, configuration : « | Configuration | `<<CONFIG_ETALONNAGE_CHEMIN_ET_EMPREINTE>>` au commit de lancement |… » remplacé par « | Configuration | `<<CONFIG_ETALONNAGE_CHEMIN_ET_EMPREINTE>>` au commit de lancement ; tirée du gabarit `docs/notes/barreau8-iib-v1/config-iib-organisme-retenu-v5-gabarit-v4.json` (`eb329185948ef80d37e724f73d8c210a02d72312befbf6c0fd5e489b255fc9e1`, dans le cor… ».
- § 1, entropie : « tirée une fois par la mère avant la configuration, sans aucune donnée ; consignée au registre des décisions et… » remplacé par « tirée une fois par la mère le 2026-11-21 à 18:26:49Z, avant la configuration, sans aucune donnée ; consignée au registre des décisions (ligne `R-4659`, lue sur `main`) et dans le gabarit ».
- § 2, sections de location : « **exigées et vérifiées en mode réel** par le code corrigé (contre-lecture du code, M7) |… » remplacé par « **exigées et vérifiées en mode réel**, bornes du devis à l'égalité (M7, levé par la vérification des corrections) ; le gabarit porte l'étiquette `iib-explo-v5` | ».
- § 2, intouchables : « l'attestation `IIB_AUCUNE_INTOUCHABLE=oui` est **interdite** sous cet ordre |… » remplacé par « l'attestation `IIB_AUCUNE_INTOUCHABLE=oui` est **interdite** sous cet ordre, et le lanceur de session en version 3 refuse cette variable | ».
- § 2, marqueurs de consigne : « | marqueurs de consigne | `<<MARQUEURS_DE_CONSIGNE>>` |… » remplacé par « | marqueurs de consigne | section `marqueurs_de_consigne` de la configuration scellée : empreinte et longueur de chaque marqueur, non vides, jamais leur texte ; fournis par un agent du côté du saboteur, jamais par la mère | ».
- § 2, lignes ajoutées à la table de la configuration : « | entropie | `<<ENTROPIE_ETALONNAGE>>` |… » remplacé par « | entropie | `<<ENTROPIE_ETALONNAGE>>` | | `code` | branche `<<BRANCHE_CODE_V5>>` et commit du code revu `<<COMMIT_CODE_REVU_POUSSE>>` | | `prealables.ligne_registre_creation_7b` | l'extrait `7b créée, instance 60218139 à 2026-11-11T14:19:58Z`, trouvé une seul… ».
- § 2, dépense passée : « | dépense passée | 0, plus `<<DEPENSE_LIGNE_AVANT_LOCATION_USD>>` |… » remplacé par « | dépense passée | 0 ; une création manquée qui aurait coûté quelque chose avant la location arrête tout : le fichier d'entrées est à sceller de nouveau, mot de la mère | ».
- § 2, actions d'oracle hors tours : « | nombre d'oracles par tour ; actions d'oracle hors tours | 1 ; 3 520 |… » remplacé par « | nombre d'oracles par tour ; actions d'oracle hors tours | 1 ; **3 830** (1 270 + 2 560 : erratum 2 du texte scellé, erratum 1 du devis ; le code refuse toute autre valeur) | ».
- § 2, vérification du fichier d'entrées : « Le code ne vérifie pas ces valeurs contre le devis (contre-lecture du code, m8) : un lecteur qui n'a pas écrit… » remplacé par « En mode réel, le code vérifie à l'égalité le plafond, le coût fixe, le prix et le nœud 7 (m8, corrigé) ; un lecteur qui n'a pas écrit le fichier les relit tout de même ».
- § 2, plafond de tours sous 12 : « Lecture retenue : `<<LECTURE_PLAFOND_DE_TOURS_SOUS_DOUZE>>`. Le rédacteur ne tranche pas ; la lecture conforme… » remplacé par « **Lecture retenue, portée par le code à sa tête** (`branches_v5.conditions` ; rapport v2 du développeur, M6 ; levée par la vérification des corrections, « conforme au § 6 du devis ») : si le nombre de tours de la course (R, ou 12 si R ≤ 12) dépasse le plafond … ».
- § 3, règle à 12 USD, état du code : « sans cet essai, aucune création.… » remplacé par « sans cet essai, aucune création. À la tête du code, cette règle n'est écrite nulle part (rapport v2 du développeur, § 4 point 3 ; note v4, reste 4) : la surveillance du lanceur de session ne coupe qu'au plafond de la configuration, 55 USD. ».
- § 3, restes de la relecture du lanceur : « empreinte du module de lecture portée par la configuration (§ 2).… » remplacé par « empreinte du module de lecture portée par la configuration (§ 2). Faits à la tête du code : le lanceur de session en version 3 refuse la variable d'attestation, et le gabarit porte l'empreinte du module de lecture dans `code.module_de_lecture` et dans la liste… ».
- § 3, risque de la coupe : « - **Étiquette** ; **branche d'essai absente du distant** ; **réponse brute du loueur conservée**, masquée, jam… » remplacé par « - **Étiquette** ; **branche d'essai absente du distant** ; **réponse brute du loueur conservée**, masquée, jamais supprimée. **Risque écrit d'avance : la valeur du coût à la ligne qui suit la clé.** Le tokeniseur réel a un jeton « :\n » : une valeur écrite à l… ».
- § 4, préalable du code : « 2. **Code** : B1, M1, M2, M3 et M7 corrigés, M6 tranché (§ 2), puis vérifiés par le même contre-lecteur (`<<VE… » remplacé par « 2. **Code** : B1, M1, M2, M3, M6 et M7 corrigés par le correctif 0007 et levés par la vérification des corrections (`6a9e2e7927b03533552b676b694736e6eb3ace72d58ca52007cb1c6b9cadfa57`), qui laisse deux restes : R1, la coupe après une clé en gras fermée après le… ».
- § 4, essai sur le tokeniseur réel : « coupe, fenêtre de 16 jetons, réécriture et gardes de décodage (`<<ESSAI_TOKENISEUR_REEL_PIECE>>`) ; un échec :… » remplacé par « coupe, fenêtre de 16 jetons, réécriture et gardes de décodage : **fait** par le développeur (135 cas au correctif 0007, rejoués par le contre-lecteur ; 16 cas de clé en gras de plus au correctif 0008 ; `sortie-essais-cibles-v5-v3.txt` : 359 réussis, tokeniseur… ».
- § 5, commandes : « Commandes : `<<COMMANDES_POINT_D_ENTREE_V5>>` ; les sous-commandes citées ci-dessous sont celles de `scripts/l… » remplacé par « Le lanceur de session est `scripts/lancer_iib_v3.sh` (`5fd1105c2ae3575b10087fbb90ad7baec30480f909055b40d343e82dd4aa7d54` à la tête du code) : la version 2 avec sept lignes changées (amorce en version 5, configuration vérifiée par `session_v5`, pièces lues sous… ».
- § 5, chemin de l'outil : « `VAST=<<CHEMIN_OUTIL_LOCATION>>`, chemin explicite… » remplacé par « variable `VAST`, chemin explicite de l'outil, relevé par l'exécutante et porté au compte rendu ».
- § 5, parent du commit de lancement : « son parent est `<<COMMIT_CODE_REVU_V5>>`… » remplacé par « son parent est `<<COMMIT_CODE_REVU_POUSSE>>`, dont l'arbre est `9917b13f3c57d0eeacf3b72fea9607a103da4f11` ».
- § 5, dernière création : « **aucune commande `creation` après 2026-11-27T00:00Z**… » remplacé par « **aucune commande `creation` à partir de 2026-11-27T00:00:00Z (instant exclu ; dernier jour : le 26)** ».
- § 5, lieu du passage des conditions : « lieu : `<<LIEU_DU_PASSAGE_DES_CONDITIONS>>` ;… » remplacé par « lieu : sur processeur, par l'exécutante, après le rapatriement vérifié, sur les sorties rapatriées du même run, par `PYTHONPATH=src python -m controle_ia.iib.lanceur_v5 --phase conditions --config <configuration> --run-id <run>` ; ».
- § 5, sort de la machine : « 7. **Sort de la machine** : après le rapatriement vérifié… » remplacé par « 7. **Sort de la machine** : `<<SORT_DE_LA_MACHINE_APRES_ETALONNAGE>>` (mot de la mère, écrit ici avant le scellement) ; dans tous les cas, après le rapatriement vérifié ».
- levée bornée, lanceur de session : « les appels faits par `scripts/lancer_iib_v2.sh` lui-même… » remplacé par « les appels faits par `scripts/lancer_iib_v3.sh` lui-même ».
- § 6, heure de la dernière création : « heure passée 2026-11-27T00:00Z… » remplacé par « heure à partir de 2026-11-27T00:00:00Z ».
- § 6, issues, la coupe : « coupe en échec, « ne part pas », « non calculable »… » remplacé par « coupe en échec (risque écrit au § 3), « ne part pas », « non calculable » ».
- § 7, noms des sorties : « Noms au correctif 0005 (`lanceur_v5.py`) ; liste au commit de lancement, fichiers par lot compris : `<<LISTE_S… » remplacé par « Noms à la tête du code (`lanceur_v5.py`, amorce en version 5) : après chaque lot de huit épisodes, les sorties d'oracle sous `diag/<run>/lots/` et les identifiants des actions sous `donnees/<run>/lots/`, scellés et poussés ; le manifeste du run sous `runs/<run… ».
- § 7, manifeste : « | fin de l'étalonnage | `manifeste-etalonnage-iib-v5.json` | configuration et empreinte, versions, entropie et… » remplacé par « | début, puis fin | manifeste du run sous `runs/<run>/` ; `diag/<run>/resume.json` | configuration et empreinte, versions, entropie et graines, commit ; liste des sorties, lots, durées, validité du contrôle du premier coût | ».
- § 9, erratum du devis : « les deux oracles neufs n'ont jamais été chronométrés.… » remplacé par « les deux oracles neufs n'ont jamais été chronométrés. L'erratum 1 du devis ne change aucun chiffre de l'étape 1. ».
- § 11, correctifs lus, ajout : « | `0006-Organisme-retenu-du-saboteur-budget-code-en-version-.patch` | `ee867c9c6d429d4b5e2aef6b48ccc67ef3e1073… » remplacé par « | `0006-Organisme-retenu-du-saboteur-budget-code-en-version-.patch` | `ee867c9c6d429d4b5e2aef6b48ccc67ef3e1073e043aec34f2d19ef521ca73ca` | @@CORRECTIFS@@ Ordre d'application sur `836c7cccda5071fe54ecb148d214d74b5cb90474` : les douze lignes de cette table, de h… ».
- § 12, point 2 : « 2. **Cas du plafond de tours sous 12** : à écrire avant le scellement (§ 2).… » remplacé par « 2. **Cas du plafond de tours sous 12** : réglé par le code, « ne part pas », motif « tours » (§ 2). ».
- § 12, point 3 : « 3. **Ligne `GO-2026-11-21-74`** : citée par le mandat, non trouvée au registre de `main`.… » remplacé par « 3. **Ligne `GO-2026-11-21-74`** : trouvée au registre de `main` au brouillon 2 ; la mère confirme qu'elle vaut mot de Lazar pour la création. ».
- § 12, point 4 : « l'ordre suit la ligne d'accord.… » remplacé par « l'ordre suit la ligne d'accord, lue « instant exclu, dernier jour le 26 », comme le code ; si la ligne veut dire « le 27 compris », la constante du code est à changer avant le scellement. ».
- § 12, point 5 : « le lanceur de session exige une branche `prep/…`.… » remplacé par « le lanceur de session exige une branche `prep/…` : la mère ou l'exécutante appliquent les douze correctifs sur une branche `prep/` neuve et la poussent (§ 1) ; le code et la configuration du saboteur ne vont jamais sur `main`. ».
- § 12, point 6 : « si le code corrigé l'exige encore, la configuration reprend l'extrait de l'ordre d'origine, sans le recopier a… » remplacé par « le code l'exige encore en mode réel : la configuration reprend l'extrait de l'ordre d'origine (§ 2), sans le recopier au registre. ».
- § 12, points ajoutés : « et laisse le choix à la mère, dans les bornes du devis.… » remplacé par « et laisse le choix à la mère, dans les bornes du devis. 8. **Règle de la surveillance à 12 USD** : accordée par la ligne d'accord et exigée par le devis, avec son essai sur un cas sain et sur un artefact avant la création ; elle n'est écrite dans aucun code à … ».
- champ `<<TESTS_ATTENDUS_V5>>` rempli partout (3 fois hors de la table) : 267.
- champ `<<ENTROPIE_ETALONNAGE>>` rempli partout (2 fois hors de la table) : 34177889608133376136283958643409181656.
- champ `<<BRANCHE_ETALONNAGE>>` rempli partout (5 fois hors de la table) : essai/iib-explo-v5.
- champ `<<LIGNE_MOT_LAZAR_CREATION>>` rempli partout (1 fois hors de la table) : GO-2026-11-21-74.
- champ `<<DEPENSE_LIGNE_AVANT_LOCATION_USD>>` rempli partout (2 fois hors de la table) : 0.

## Table des champs du § 11, une différence par ligne

- champ `<<AMORCE_V5_CHEMIN_ET_EMPREINTE>>` retiré de la table : rempli ou remplacé par un remplacement ci-dessus.
- champ `<<BRANCHE_ETALONNAGE>>` retiré de la table : rempli.
- champ `<<CHEMIN_OUTIL_LOCATION>>` retiré de la table : rempli ou remplacé par un remplacement ci-dessus.
- champ `<<COMMANDES_POINT_D_ENTREE_V5>>` retiré de la table : rempli ou remplacé par un remplacement ci-dessus.
- champ `<<COMMIT_CODE_REVU_V5>>` retiré de la table : rempli ou remplacé par un remplacement ci-dessus.
- champ `<<DEPENSE_LIGNE_AVANT_LOCATION_USD>>` retiré de la table : rempli.
- champ `<<EMPREINTES_CORRECTIFS_NEUFS>>` retiré de la table : rempli ou remplacé par un remplacement ci-dessus.
- champ `<<ENTROPIE_ETALONNAGE>>` retiré de la table : rempli.
- champ `<<ESSAI_TOKENISEUR_REEL_PIECE>>` retiré de la table : rempli ou remplacé par un remplacement ci-dessus.
- champ `<<LECTURE_PLAFOND_DE_TOURS_SOUS_DOUZE>>` retiré de la table : rempli ou remplacé par un remplacement ci-dessus.
- champ `<<LIEU_DU_PASSAGE_DES_CONDITIONS>>` retiré de la table : rempli ou remplacé par un remplacement ci-dessus.
- champ `<<LIGNE_MOT_LAZAR_CREATION>>` retiré de la table : rempli.
- champ `<<LISTE_ESSAIS_V5_EMPREINTE>>` retiré de la table : rempli ou remplacé par un remplacement ci-dessus.
- champ `<<LISTE_SORTIES_ETALONNAGE>>` retiré de la table : rempli ou remplacé par un remplacement ci-dessus.
- champ `<<MARQUEURS_DE_CONSIGNE>>` retiré de la table : rempli ou remplacé par un remplacement ci-dessus.
- champ `<<TESTS_ATTENDUS_V5>>` retiré de la table : rempli.
- champ `<<VERIFICATION_CORRECTIONS_CODE_V5>>` retiré de la table : rempli ou remplacé par un remplacement ci-dessus.
- champ `<<COMMIT_CODE_REVU_POUSSE>>` ajouté : commit du code revu sur cette branche ; son arbre est `9917b13f3c57d0eeacf3b72fea9607a103da4f11`.
- champ `<<VERIFICATION_COURTE_CORRECTIFS_0008_0009>>` ajouté : chemin, empreinte et verdict de la vérification courte des correctifs 0008 et 0009 par le même contre-lecteur.
- champ `<<MOT_LAZAR_PREMIERE_ACTION_DANS_LA_PERTE>>` ajouté : ligne du registre qui porte le mot de Lazar sur la première action dans la perte de distillation (`gardee` ou `exclue`).
- champ `<<SORT_DE_LA_MACHINE_APRES_ETALONNAGE>>` ajouté : destruction après le rapatriement vérifié, ou garde à l'arrêt pour la course sous son ordre à part.
- champ `<<BRANCHE_CODE_V5>>` gardé.
- champ `<<COMMIT_LANCEMENT_ETALONNAGE>>` gardé.
- champ `<<CONFIG_ETALONNAGE_CHEMIN_ET_EMPREINTE>>` gardé.
- champ `<<FICHIER_ENTREES_CHEMIN_ET_EMPREINTE>>` gardé.
- champ `<<INSTANCES_INTOUCHABLES>>` gardé.
- champ `<<ETIQUETTE_ETALONNAGE>>` gardé.
- champ `<<REGLE_COUPURE_ETALONNAGE_FORME_ET_ESSAIS>>` gardé.

## Pièces dont l'empreinte et le compagnon ont été vérifiés avant l'écriture, une par ligne

- `brouillons/ii-b-saboteur-budget-v5/conception-organisme-retenu-ii-b-v5-scellee-v1-erratum-2.md` : `ab020d438cb6eaa46cd2df0a6ed76952b5dfb23497438e0f2b3fb4590b1d26e2`.
- `brouillons/ii-b-saboteur-budget-v5/devis-v5/devis-ii-b-v5-scelle-v1-erratum-1.md` : `90342292f52daf2f7281acad68006598450033367d3a36aa1c6c72eac9150f9a`.
- `brouillons/ii-b-saboteur-budget-v5/code-v5/rapport-developpeur-code-organisme-retenu-v5-v2.md` : `5b71aa0ec23374ae4ce3e96a65fc9a49fb0de2d0767591942cc16f209c5f5d85`.
- `brouillons/ii-b-saboteur-budget-v5/code-v5/rapport-developpeur-code-organisme-retenu-v5-v3-note.md` : `1af79d4c935cb80cdd91c421be71836a80c4d52d1afd1e5f6eb6be5fdec62594`.
- `brouillons/ii-b-saboteur-budget-v5/code-v5/rapport-developpeur-code-organisme-retenu-v5-v4-note.md` : `bb6d6d4e283e6b91a8cddf97b342faa75673cf8f878152af1564c296be2493d1`.
- `brouillons/ii-b-saboteur-budget-v5/code-v5/contre-lecture-cl1/verification-corrections-code-organisme-retenu-v5-cl1.md` : `6a9e2e7927b03533552b676b694736e6eb3ace72d58ca52007cb1c6b9cadfa57`.
- `brouillons/ii-b-saboteur-budget-v5/code-v5/sortie-repetition-locale-v2.txt` : `2e6e88c97000e4b92c85764688517583261c3d1dcc60e0c39f54f3a8304fbc4f`.
- `brouillons/ii-b-saboteur-budget-v5/code-v5/sortie-essais-cibles-v5-v3.txt` : `358b8371332d8bc556f457849c0ad195877f89801da9681ee7508bd1a4183be3`.
- `brouillons/ii-b-saboteur-budget-v5/code-v5/sortie-essais-cibles-v5-v4.txt` : `044e1be395693c000bdb6152c925c0545b3e99ce4e5b84977d072e6b935f2d90`.
- `brouillons/ii-b-saboteur-budget-v5/code-v5/correctifs-v2/0007-Organisme-retenu-du-saboteur-budget-code-en-version-.patch` : `3075a8df0becf391df583b0ffc300419a387ac49818a48c11d71dd5cd9dad20b`.
- `brouillons/ii-b-saboteur-budget-v5/code-v5/correctifs-v3/0008-Organisme-retenu-du-saboteur-budget-code-en-version-.patch` : `ad33fe2697fcdcb95242fe8464fcd154f14aea0140aac898796fb7ee5be88281`.
- `brouillons/ii-b-saboteur-budget-v5/code-v5/distillateur-v5/correctifs/0001-Organisme-retenu-du-saboteur-budget-distillateur-en-.patch` : `8cfb77005517c83229887fe78230c1b681f7c0793afc8d986ddaf8558c2debe3`.
- `brouillons/ii-b-saboteur-budget-v5/code-v5/distillateur-v5/correctifs/0002-Organisme-retenu-du-saboteur-budget-distillateur-en-.patch` : `a515c1d8372611595c3f7a9a77cc44ebb7083fc5e2698b58890fef4a8b562197`.
- `brouillons/ii-b-saboteur-budget-v5/code-v5/distillateur-v5/correctifs/0003-Organisme-retenu-du-saboteur-budget-distillateur-en-.patch` : `324b51fad40b3da3c129e254377a1c8a6fda6866f91ee000cd92a3e1a526a6bc`.
- `brouillons/ii-b-saboteur-budget-v5/code-v5/correctifs-v4/0009-Organisme-retenu-du-saboteur-budget-code-en-version-.patch` : `4287a6889061c921886582ff3a7ebffecd4bd67fcbb4556b102e9eb9e2737661`.
