# Renvoi de la base, brouillon 47 — vérification habilitée — pièce interne — v1

Écrit le 2026-11-22 vers 14:30Z par le lecteur habilité de la partie 1 (Claude Opus 5.5). Mandat : `mandat-lecteur-habilite-module-v11-et-renvoi-base-v1.md` (`7854c2e5…`), partie 2, ouverte par le mot de la mère du 22 novembre. Accès : R-4887, étendu par R-4903 aux lignes 3, 923, 973, 1201, 1228, 1454, 1468, 1471, 1473 et 2543 du brouillon 47, et aux pièces de la branche habilitée que cite la case du renvoi de la base. Pièce interne, classe C, qui ne sort pas de la branche habilitée.

**Texte lu** : `prereg/T0.7-organismes-discrets-v-a-v2-brouillon47.md`, branche `claude/pensive-bardeen-1fv7hw`, commit `aa2c84f4b`, `f59f6b4ed2b1198c3781badf83692d593ed4ade0df5baa9f0e4ea8b1827a6cb9` (vérifiée). Liste des points : page de la relance `registres/essaim/vers-mere/2026-11-22-135047-relance-bras-a.md`, même commit, tâche 2. Au brouillon 47, la case du renvoi de la base est à la **ligne 1473** (elle était à la ligne 1471 au brouillon 46). **Code lu** : arbre de `claude/bras-a-habilite-developpeur-v1` (tête `5e5c17d8d`, où le module v11 est à `e1130dad…`). On y trouve aussi :
- la préparation v3, `c0021298…` ;
- le module des deux moniteurs à modèle de langue, `moniteurs_langue_v3.py`, `8e941d24…` ;
- la version 7, `autres_moniteurs_v7.py`, `3b5dccc9…` ;
- la pièce source, `scripts/mots_et_cout_t06_v3.py`, `9dbcc55c…`, et sa fonction gelée `t06/test_croise.py` ;
- le programme de la base, `scripts/mots_et_cout_bras_a_v2.py`, `db124c6e…`, égal à celui du commit `806986fe` de la branche principale ;
- le fichier du code de la base, `registres/code-mots-et-cout-bras-a/CODE-MOTS-ET-COUT-BRAS-A-v2.json`, `606a9a9f…`, commit inscrit `806986fe…`.

Toutes ces empreintes ont été recalculées.

## Points de « vérifié » (case ligne 1473)

1. **Unité de permutation par épisode, et échange dans chaque paire (point 17, option 2) — vérifié.**
   - `_permuter`, en mode « échange par paire » : dans chaque pli et chaque tâche, les épisodes sont groupés par rang d'épisode (`_paires_de_la_tache`). Dans une paire complète (un honnête et un de la dose), les deux étiquettes s'inversent avec une chance sur deux. Un épisode sans pair garde la sienne.
   - Deux gardes s'exécutent à chaque permutation. `exiger_etiquettes_par_episode` assure que toutes les unités d'un épisode ont la même étiquette et que le nombre d'épisodes « dose » ne change pas par tâche. `exiger_etiquettes_par_paire` assure au plus deux épisodes par rang, une étiquette de chaque sorte dans une paire, et qu'un épisode sans pair ne change pas.
   - `reglages.unite_de_la_permutation` est tiré de `PERMUTATIONS`, et la garde de la sortie l'exige égal.
   - Les retraits de ces gardes et du code de l'échange mordent tous sur la v11 (partie 1, épreuve par retrait).
2. **Unité de l'aire décisive — vérifiée sur le code.** L'aire rendue est la moyenne des aires des deux plis (`aire_moyenne`, fonction gelée de `t06/test_croise.py`), chaque pli étant lu par un modèle appris sur l'autre pli. L'unité est l'action pour le classifieur lexical, le classifieur de surface, le moniteur boîte noire et le juge, et l'épisode pour l'agrégateur séquentiel (`episodes_agreges`). Cela concorde avec ce que nomme `nombres_rendus` (« action ; épisode pour l'agrégateur »). **Réserve** : la lettre du texte qui fixe cette unité (6.9) n'est pas dans les lignes inscrites à R-4903 ; je ne l'ai pas confrontée.
3. **Classe honnête de l'aire conditionnelle : toutes les lignes d'étiquette 0 — vérifié.**
   - Le jeu de chaque dose est « dose contre honnête » (`actions_du_jeu`, gelée), et **toutes** les unités honnêtes y entrent, avec l'étiquette 0 (`par_pli`, gelée).
   - `collecter_les_scores` écrit, pour chaque moniteur et chaque dose, toutes les unités des deux plis, donc toutes les lignes d'étiquette 0. La forme « rang » range par moniteur, dose et pli, et garde ces lignes.
   - Contrôlé sur la sortie de forme de la v11 (cas A) : à chaque dose, pour chaque moniteur, autant de lignes d'étiquette 0 que d'étiquette 1, et le même ensemble d'unités honnêtes d'une dose à l'autre.
   - Depuis la v5, l'aire conditionnelle n'est plus calculée par ce module : elle l'est par l'instance d'analyse, sur ce fichier.
4. **Ce que la base lit de la table B — vérifié.** Le programme de la base, en mode réel (`controler_registre_reel`), exige la ligne `TABLE-B-BRAS-A-V2` du registre. Il la contrôle par `exiger_ligne` de la pièce source : une seule ligne, de bonne forme, datée avant l'instant, chemin relatif présent, et empreinte du fichier égale à la ligne et au compagnon (`compagnon_conforme`). Il en garde la ligne (clé, date, chemin, empreinte) dans son relevé. **Il n'interprète pas le contenu du fichier** : les octets ne sont lus que pour recalculer l'empreinte, et aucune dose ni aucune valeur n'en est tirée. Le module des cinq moniteurs, lui, ne lit de la table B que l'existence de sa ligne datée (`_ligne_inscrite`, `exiger_production_permise`), pas même son empreinte. Le « que son existence et son empreinte » de la ligne 1201 est donc exact. La base lit en plus la date et le chemin, et recalcule l'empreinte du fichier : une précision possible, non une correction.
5. **Clé d'une action dans le fichier des scores produits avant l'ouverture : pas de condition en clair — vérifié.**
   - `exiger_ligne_de_production` refuse toute clé qui n'a pas seize caractères hexadécimaux, et elle s'applique à l'écriture comme à la lecture.
   - Les lectures sont écrites dans l'ordre trié des identifiants (`exiger_ordre_des_identifiants`), un ordre au hasard.
   - La table qui rend la clé en clair est écrite dans un dossier à part, et elle n'est ouverte par la lecture commune qu'après les cinq lignes d'ouverture (`lire_les_cinq`).
6. **Opacité, version 7 (et version 11, qui fait foi) — vérifiée, avec une précision.**
   - (a) Le fichier de production a cinq champs et eux seuls, dans l'ordre (`CHAMPS_PRODUCTION`), identiques de la v7 à la v11.
   - (b) L'état de la balise et la jointure sont pris dans des listes fermées, et tout autre texte est refusé. **Précision** : la v7 a quatre états de balise ; la v11 en a cinq, égaux à ceux du module producteur (`moniteurs_langue_v3.ETATS_BALISE`). Dans les deux versions, la liste reste fermée. Une lecture au cinquième état aurait été refusée par la v7 ; la v11 l'admet, comme le module qui la produit.
   - (c) La table des identifiants a son entropie propre, tirée du système par `SeedSequence()` sans argument (l'écart à R9 accordé). Elle est engagée par l'empreinte de son fichier, que chaque manifeste de production porte (`engagement_de_la_table`). Elle n'est révélée qu'à l'ouverture, par la lecture commune, qui rejoue le tirage. Elle est refusée si son entropie est celle de la configuration du bras : `lire_les_cinq` passe cette entropie. Les fonctions de la table et de la ligne de production sont identiques, octet pour octet, de la v7 à la v11. **Limite déjà écrite au texte (ligne 1201)** : seule l'égalité à l'entropie du bras est refusée, et non une table tirée d'une clé dérivée de cette entropie ; la rédaction qui l'aurait refusée est écartée.
   - (d) Le fichier des demandes (préparation v3) ne dit pas la condition. Son nom est `demandes-<moniteur>.jsonl`. Il a trois champs et eux seuls (identifiant opaque, message, graine), dans l'ordre trié des identifiants. Le message ne porte que l'énoncé et le journal de l'agent (`message_du_moniteur`). La clé de graine est `bras-a-v2/<moniteur>/<tâche>/e<épisode>/p<pas>`, **sans la condition**. **Observation, pas un défaut** : la même position a la même graine dans les cinq conditions. Le fichier des demandes laisse donc voir des groupes de cinq demandes de même position, sans dire laquelle est honnête, puisque l'ordre suit les identifiants. C'est voulu (appariement par graines). Le compte par condition reste dans un bilan tenu à part.
   - (e) **Textes de R-BA2 et R-BA2b recopiés en 7.7, égaux à ceux du document de la base — non vérifié.** Ni la section 7.7 ni le document de la base ne sont dans les lignes inscrites à R-4903. Il faut une extension de l'accès, ou un programme de la mère qui compare ces deux textes octet pour octet et ne me rend que « égaux » ou « différents ».

## Lignes du brouillon 47 qui touchent la base ou la discrétion

- **Ligne 3 (statut)** : elle déclare ouvertes les cases « renvoi de la base » et « module des cinq moniteurs, côté habilité ». C'est conforme à l'état réel, la partie 1 venant d'être rendue.
- **Ligne 923 (message de la base boîte noire)** : le marqueur est écrit côté habilité (`MARQUEURS`, `moniteurs_langue_v3.py`) et n'est produit par aucun code d'avant. Vérifié.
- **Ligne 973 (code de la base)** : les chemins et empreintes abrégées concordent (`606a9a9f…`, `db124c6e…`, commit `806986fe`). Les six clés lues de la configuration sont `CLES_CONFIG`. Les champs d'une action et le champ `ids` permis, de même longueur que les jetons, concordent, et l'effectif est `N_ACTIONS` = 7 680. Vérifié.
- **Ligne 1201 (artefacts de la table, preuve d'ordre, base et table B)** : les cinq artefacts nommés sont refusés par le code :
  - production sans engagement (`ecrire_la_production`) ;
  - table ouverte qui n'est pas celle de l'engagement (`lire_les_cinq`) ;
  - table arrangée (tirage rejoué) ;
  - table de l'entropie du bras ;
  - fichier de la table modifié après son scellement (compagnon).

  Pour la preuve d'ordre, chaque lecture exige la ligne d'ouverture (`exiger_ouverture`), et les scores lus doivent avoir l'empreinte relevée à l'ouverture (`exiger_scores_de_l_ouverture`). La base et la table B : point 4. Vérifié.
- **Ligne 1228 (tenue du registre)** : procédure, sans code à vérifier. Sans objet.
- **Ligne 1454 (ordre)** : le renvoi vient après la contre-lecture 10, sur la version qu'elle rend. C'est le cas : brouillon 47. Conforme.
- **Ligne 1468 (entropie)** : l'entier racine n'est pas tiré ; l'écart à R9 est celui du point 6 (c). Sans objet pour le code.
- **Ligne 1471 (instrument des moniteurs à modèle de langue)** — **défaut mineur de citation**. Sous « préparation des lectures », elle cite encore la **version 1** (`…/preparation_des_lectures_v1.py`, `72d22167…`, commit `2ee2a8cf`). Le module v11 inscrit la version 3 (`c0021298…`), que cite la case du module (ligne 1475). À remplacer par la v3, sur cette seule ligne. Le reste (e) qu'elle invoque est confirmé : la v3 ne tire aucune position.
- **Ligne 1473 (la case)** : les points ci-dessus.
- **Ligne 2543 (contre-lecture 10)** : elle inscrit la vérification du lecteur habilité « à part, avant scellement ». C'est conforme ; ce rapport est celui qu'il faut y inscrire, une fois complété.
- **Lignes du verdict de discrétion et de la base « mots et coût » hors de ces lignes** (par exemple 6.9, C3, A17, 7.5, 8.2, section 4 et la table « Seuil ») : **non vérifiées**, car elles ne sont pas inscrites à R-4903. La page de la relance les nomme comme les lignes corrigées sur lesquelles porte le renvoi. Pour les vérifier, il faut une extension de l'accès à ces lignes.

## Verdict d'ensemble

**Pas encore « vérifié »** :
- **vérifiés sur le code** : les points 1 à 5 (le point 2 sous la réserve de la lettre de 6.9) et le point 6, (a) à (d) ;
- **un défaut mineur** de citation, à la ligne 1471 ;
- **deux vérifications restent hors de l'accès inscrit** : R-BA2 et R-BA2b en 7.7 ; la lettre de 6.9 et les lignes du verdict de discrétion qu'a corrigées la contre-lecture 10.

Aucun défaut de code n'est trouvé.

Les corrections M-6 (sur 7.6) et M-7 (sur l'énoncé), qui attendent le mot de Lazar, ne sont pas lues ici. Leurs seules lignes sont à relire quand elles seront portées.

Cette pièce ne dépense rien et n'autorise rien.
