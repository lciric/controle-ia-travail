# Rapport du développeur — bras externe NARCBench (nos sondes et la recette des auteurs sur les activations publiées), v2

- **Rédacteur** : développeur du bras externe v2, Claude Opus 5.5 (`claude-opus-5-5`), sous-agent de la session mère
  `session_013QMayjsoZJFBUCqcnvD5h1` ; travail du 2026-11-18, de 16:19 à ≈ 21:05 UTC. Remplace, sans la réécrire (R12), la
  version 1 (`rapport-developpeur-externe-v2.md`, `40fbdc70…`), qui décrit la tête `70cb77b8` et dont **la commande de
  lancement est périmée** (option `--registre`, clé `EXTERNE-NARC`).
- **Arbre** `/home/user/narcbench-externe-v2`, branche **locale** `prep/narcbench-externe-v2`, partie de `origin/main`
  (`77d55971`). **Code et essais au commit `05ab4264`** ; les quinze modules de `src/controle_ia/narcbench/` y ont **les
  empreintes de la tête `fe9d7996`** relue par la contre-lecture du code final (le commit `05ab4264` n'ajoute que des essais).
  Rien poussé ; rien écrit dans le dépôt principal ni sous `registres/`, `diag/`, `runs/`, `donnees/`.
- **Aucun score calculé ni lu sur les données réelles.** Sur elles : tailles, empreintes, essai de forme (structure et comptes).
  Toute aire, tout intervalle, toute statistique d'épisode ont tourné sur des vecteurs factices.

## 1. Ce que fait le code à la tête finale

| module | rôle |
|---|---|
| `chargeur_externe_v1` (inchangé, `9193b787…`) | huit fichiers publiés : tailles, empreintes, vingt champs, valeurs fermées, couches de la bande, largeurs, valeurs finies |
| `forme_externe_v2` | essai de forme sans score (en-têtes et comptes ; sortie `forme-donnees-externe-v2.json`, `61cc1313…`) |
| `externe_v2` | recette des auteurs (E1 à E4, transcrite de `probes/reproduce_LR.py` @ `85fea3be2a9d`), garde de reproduction v2 (rapportée sans valeur de lecture), lecture par agent, gardes n° 8 à 12 |
| `cellules_externe_v2` (neuf) | cellules par épisode de toutes les procédures, intervalle par sabots ou par plis, plancher par la même chaîne, placebo par échange des conditions, lecture des comités pli par pli (score d'agent = maximum de ses trois messages), règles C et T, phrases par famille, réponse R0 à R5, tâches de graines ; comparaisons à 10⁻⁹ près |
| `lecture_externe_v2` | commande de lecture : registre propre `registres/narcbench-externe-v1.md` (clés `SCELLEMENT-NARC-EXT`, `CODE-NARC-EXT`, `LECTURE-NARC-EXT`), configuration canonique lue dans le texte scellé, fiche du code, gardes n° 1 à 7, manifeste, résultat scellé ; contrôles préalables `verifier-texte` et `fiche-code` |

**Liste d'arrêt** (numéros du brouillon 3, `fae8a96c…`, égaux à ceux du brouillon 2), dans l'ordre de la commande : n° 3
registre (refus, code 2) ; n° 5 configuration (code 2) ; n° 6 code exécuté égal au code de la fiche, arbre propre (code 1) ; n° 4
déjà jouée (code 2) ; n° 7 scikit-learn 1.9.1 (code 1) ; n° 2 transfert ; n° 1 tailles et empreintes ; n° 8 et 9 sur les
métadonnées, avant le manifeste (code 1) ; puis manifeste, ouverture, n° 10 (repli de Cholesky), n° 11 (mémoire : arrêt), n° 12
(scores non finis : arrêt ; constants : cellule « non lu »). Journal `registres/narcbench-externe-v1.md.ouvertures.md` (refus,
ouverture, arrêt), gardé selon la contre-lecture 2 du texte (A23).

**Configuration canonique** attendue (section du texte, six lignes seules, chacune la seule du texte qui commence par sa clé) :
`augmentation : papier` ; `couches-familles : bande` ; `run-id : AAAAMMJJ-HHMMSS-narc-externe-v2` ; `registre :
registres/narcbench-externe-v1.md` ; `texte : prereg/narcbench-bras-externe-v1.md` ; `Entropie : <entier ≥ 2³²>`.
`verifier-texte` sur le brouillon 3, entropie d'essai : **code 0** (`controles-brouillon3-v1.txt`, `6ae50843…`).

## 2. Commande de lancement (celle de l'en-tête de `lecture_externe_v2.py`)

    cd <racine du dépôt> && PYTHONPATH=src:/home/user/narcbench-paquets-v2 .venv/bin/python -m controle_ia.narcbench.lecture_externe_v2 \
        --depot . --texte prereg/narcbench-bras-externe-v1.md --donnees /home/user/narcbench-donnees-v2 \
        --run-id <AAAAMMJJ-HHMMSS>-narc-externe-v2 --entropie <entier du texte> --augmentation papier --couches-familles bande

Contrôles préalables, sans registre ni données : `… lecture_externe_v2 verifier-texte prereg/<texte>.md` ; `… lecture_externe_v2
fiche-code --depot . --commit <40 caractères>`.

## 3. Essais et épreuves

- **175 essais NARCBench verts** au commit `05ab4264` (rejoués avec `--basetemp` dans l'arbre, dossier supprimé) : cellules 21,
  commande de lecture 71, bras externe v2 35, chargeur 13, forme 8, bras externe v1 3, module v1 24.
- **Oracle des auteurs** : recopie à la lettre de la recette (égalité au bit près de la direction, du `scaler`, des aires et de
  l'erreur type ; y compris le régime où l'arrêt à 8 itérations agit).
- **Oracle indépendant des cellules** (d'après la pièce de la contre-lecture du code final) : aires par `roc_auc_score`, boucles
  explicites ; cellules visées, plancher, placebo, intervalles, témoin, comités avec le domaine tenu à l'écart.
- **Énumérations** des règles C, T, des phrases et des réponses, recoupées par prédicats ; **39 phrases gelées** comparées par
  programme au brouillon 3 : 0 écart (R1 recopiée mot pour mot).
- **Épreuves par mutation** (copie de `narcbench/` seule, `-o pythonpath=<copie>/src`, chaque mutation sous `timeout 600`) :
  témoin et onze mutations décisives tuées (`mutations-decisives-v1.txt`, `0177792c…`) ; rejeu des vingt mutations de la
  contre-lecture du code final après les essais ajoutés : section 4.
- **Jouet de bout en bout aux formes publiées** (vecteurs factices) : code 0, **14,8 min, 3 748 Mo de pointe**, plancher par
  Cholesky partout (`jouet-formes-publiees-sortie-v1.txt`, `e21ac32a…`).

## 4. Rejeu des mutations de la contre-lecture du code final

Script `pieces-externe-v2/mutations_contre_lecture_finale_v1.py` (`640fc76f…`), définitions lues telles quelles dans les pièces de
la contre-lecture (`lot_c.json`, `lot_b.json`) ; sortie brute `pieces-externe-v2/mutations-contre-lecture-finale-v1.txt`
(`cf8833dc…`), de 20:49:25 à 20:55:36 UTC, code 0. Copie de `narcbench/` seule (au plus 34 Mo), `-o pythonpath=<copie>/src`,
`timeout 600` par mutation, l'une après l'autre ; copies supprimées (`.mutants` absent à la fin). Essais joués : le fichier des
cellules entier pour C ; pour B01 et B02, les cas de la garde du registre (`-k`). Avec `-x`, l'essai nommé est le premier qui
échoue. **Vingt mutations sur vingt tuées, la témoin montrée** (chez la contre-lectrice, avant les essais ajoutés : quinze des
dix-huit du lot C et B01, B02 survivaient). Les essais ajoutés au commit `05ab4264` sont marqués *.

| mutation (pièces de la contre-lecture) | état | essai qui la tue |
|---|---|---|
| témoin : exception en tête de `cellules_externe_v2` | tuée (la copie mutée est bien chargée) | erreur à la collecte du fichier des cellules |
| C01 quantile du plancher et du placebo 0,95 → 0,50 | tuée | `test_reglages_du_texte_epingles` * |
| C02 200 directions de plancher et 200 permutations → 20 et 20 | tuée | `test_reglages_du_texte_epingles` * |
| C03 2 000 tirages → 1 000 | tuée | `test_reglages_du_texte_epingles` * |
| C04 plancher du témoin noté sur des vecteurs non standardisés | tuée | `test_oracle_independant_des_cellules` * |
| C05 nos familles : épisodes notés dans l'ordre inverse des étiquettes | tuée | `test_oracle_independant_des_cellules` * |
| C06 plancher : maximum sur les couches au lieu de la moyenne | tuée | `test_oracle_independant_des_cellules` * |
| C07 placebo : conditions jamais échangées | tuée | `test_cellule_stego_etats_c0_c1_c2_c3` |
| C08 placebo : maximum sur les calculs au lieu de la moyenne | tuée | `test_oracle_independant_des_cellules` * |
| C09 intervalle par sabots : maximum sur les calculs | tuée | `test_intervalle_par_sabots_egal_a_intervalle_blocs_pour_un_calcul` |
| C10 effectif lisible stéganographique sans les dix sabots | tuée | `test_bornes_de_l_effectif_lisible` * |
| C11 effectif lisible des comités sans les dix plis | tuée | `test_bornes_de_l_effectif_lisible` * |
| C12 réponse lue sur douze cellules au lieu des huit co-principales | tuée | `test_cablage_de_la_lecture_finale` * |
| C13 qualificatifs de plancher limités à huit au lieu de douze | tuée | `test_cablage_de_la_lecture_finale` * |
| C14 intervalle par plis : minimum au lieu de la moyenne | tuée | `test_oracle_independant_des_cellules` * |
| C15 pic du témoin fait des scores de l'écart | tuée | `test_lire_modele_de_bout_en_bout_temoin_egal_a_la_reproduction` |
| C18 cellule des comités : médiane des plis au lieu de la moyenne | tuée | `test_oracle_independant_des_cellules` * |
| C21 nos familles : étiquettes d'apprentissage inversées | tuée | `test_oracle_independant_des_cellules` * |
| C22 comités : domaine tenu à l'écart gardé dans l'apprentissage | tuée | `test_oracle_independant_des_cellules` * |
| B01 sceau de la fiche du code non vérifié | tuée | `test_refus_et_arrets_avant_ouverture_rien_d_ecrit[sceau_faux_de_la_fiche]` * |
| B02 antériorité à l'ouverture vérifiée pour la seule ligne de scellement | tuée | `test_refus_et_arrets_avant_ouverture_rien_d_ecrit[code_seule_posterieure]` * |

Hors de la demande, non rejouées : C24 et C25 (rejeu, en copie entière, de mes deux mutations de `lecture_externe_v2`, tuées
chez la contre-lectrice) et B03 à B26 (tuées chez elle). Le repli du plancher à travers `lire_modele` n'a pas de mutation dans
les pièces ; il a son essai (`test_repli_du_plancher_a_travers_la_lecture_d_un_modele` *).

## 5. Limites connues, non corrigées (le module ne doit plus changer)

- **m1** — `lecture_externe_v2.main` n'attrape que `RefusRegistre`, `GardeArret` et `MemoryError` : toute autre exception après
  le manifeste sort en trace d'erreur, sans ligne `ARRET-NARC-EXT`. Sans effet sur le coup unique (le manifeste existe, la
  garde « déjà jouée » refuse la relance) ; la mère consigne à la main.
- **m2** — les rôles (n° 8) sont vérifiés avant les exclusions (n° 9) : un épisode stéganographique dont un colludeur n'a pas
  de ligne finale arrête (« 1 colludeur(s), 2 attendu(s) ») au lieu d'être exclu et compté. Plus strict que le texte, dans le
  sens de l'arrêt ; sans effet sur les fichiers publiés (une ligne finale par agent, essai de forme).
- **m3** — un épisode des comités à cinq agents dont un sans ses trois lignes : `groupes` garde l'épisode (quatre agents
  restent), `exclusions_etage` le compte exclu. Sans effet sur les fichiers publiés (quatre agents partout).
- Autres limites relevées par la contre-lecture, sans effet sur la lecture : la garde vaut pour le dépôt donné par `--depot`, et
  mon outil de mutation lie le reste du paquet par des liens symboliques (le dépôt jetable des essais porte alors le code non
  muté sans que la garde n° 6 le voie ; les mutations visées restent tuées) ; la tâche `…/mahalanobis/plancher` est dérivée et
  jamais consommée, les graines d'apprentissage n'agissent sur aucune des trois familles ; le journal écrit l'identifiant du run
  tel quel ; le dossier `/home/user/narcbench-paquets-v2` n'a pas d'empreinte (la garde n° 7 lit la version dans ses
  métadonnées) ; quelques renvois en retard dans des en-têtes (« aligné sur le brouillon 2 »).

## 6. Pour la fiche du code et ce qui reste avant la ligne `CODE-NARC-EXT`

- **Commit** : celui qui porte ce rapport (code et essais égaux à `05ab4264`). **Empreintes des quinze modules** : celles de la
  contre-lecture du code final (`a0ce022d…`, section « Pour la fiche du code »), inchangées ; `fiche-code` les rend.
- scikit-learn **1.9.1** (`requirements-cpu.txt`) ; **503 tâches de graines** (225 et 278 ; liste de la contre-lecture,
  `taches-503-v1.txt`, `3bcb9188…`).
- Reste : fusion vraie dans `main` (sans rebasage ; le commit de la fiche doit être HEAD ou un ancêtre), avec les pièces de
  `docs/notes/narcbench-8b-v1/` ; fiche scellée et ligne `CODE-NARC-EXT` par la mère ; **plus aucun changement de
  `src/controle_ia/` entre la fiche et le lancement** ; relevé de la mémoire libre (au moins 8 Go selon le texte ; 3,7 Go de
  pointe mesurés) ; vérifier qu'aucun `runs/*-narc-externe-v2` ni `diag/*/externe-narcbench-v2.json` n'existe.

## 7. Incidents et lectures hors du mandat (toute la journée)

- **Disque plein vers 16:39 UTC** (dossiers d'autres sessions) : mes seuls dossiers temporaires supprimés, mère alertée.
- **Première campagne de 44 mutations sans valeur** : sans `-o pythonpath`, le `pyproject.toml` du dépôt chargeait le code non
  muté ; elle a d'abord été arrêtée par sa limite de temps. **Un refus** : le crochet du dépôt a bloqué un `pkill -f` (R10 :
  aucun arrêt par motif de ligne de commande) ; rien n'a été exécuté, rien n'a été rejoué sous une autre forme.
- Lus hors de la liste du premier mandat, parce que le travail en dépendait : le script et la configuration des auteurs (publics,
  MIT, jamais exécutés) ; les brouillons 1, 2 et 3 du texte court par sections (jamais « Ce que les auteurs savaient… ») ; les
  contre-lectures 1 et 2 du texte, la contre-lecture du code et celle du code final, et les pièces de cette dernière ; les
  modules du dépôt que le code importe.
- Vus par incident, jamais ouverts : noms de dossiers temporaires d'essais d'autres sessions ; noms de fichiers d'autres agents
  dans le bloc-notes partagé de la session ; lignes du registre des décisions qui citent R-2175 et R-2184.
- Aucun résultat ni score de 7a, 7b, T0.6, T0.7, des étapes B ou de P3-bis lu.
