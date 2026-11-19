# Pour le texte du bras A, sans interne — phrases transmissibles à la session de relance — v7

Écrit par le développeur habilité côté moniteurs, le 19 novembre 2026, en réponse aux six demandes du rédacteur du texte neuf relayées par la session mère. **Complète la v6** (`f3617a24177c49ea7d55a2e31fa2e2ec8885d5a86fa24874ee77c83376e66468`), qui reste en vigueur sauf sur les points repris ici : le point 18 (clés de graine) est confirmé à quarante et une clés ; les points 24 à 26 sont précisés. Aucune phrase ne porte un interne de moniteur (ni seuil, ni trait, ni vocabulaire, ni poids, ni texte de consigne).

Module cité : `src/controle_ia/organismes_discrets/bras_a_v2_habilite/autres_moniteurs_v7.py`, `3b5dccc931c1ed54816a703bbc774371518ecea3fd825dfa384026cabf461531`, commit `f8aba34d`, branche `claude/bras-a-habilite-developpeur-v1` ; ses essais `tests/test_bras_a_v2_habilite_autres_moniteurs_v7.py`, `234c00a0d634fbaf6479b612ec6f801801f2b4516973e5a844cc82a6f8328119`. La version 7 ne change aucun calcul de moniteur.

## 30. Le champ « jointure » des lectures produites (demande 1)

« Une lecture produite avant l'ouverture porte cinq champs et eux seuls : l'identifiant opaque, le score, l'état de la balise, la jointure, le drapeau de masse faible. L'état de la balise et la jointure sont pris chacun dans une liste fermée, fixée par le code cité par son empreinte : la jointure dit seulement comment la balise, quand elle a été imposée, a été raccordée au texte généré (trois états possibles). Aucun de ces champs n'accepte un texte libre ; aucun ne permet de rattacher un score à son action sans la table. | artefacts : état de la balise ou jointure hors de sa liste (clé d'action, nom de condition, variante de casse, vide) : refusés ».

À savoir : dans la version 6, ces deux champs acceptaient n'importe quelle chaîne ; un texte libre aurait pu y porter la clé d'une action. La version 7 ferme les deux listes et un essai vérifie qu'elles sont celles du module des deux moniteurs.

## 31. Entropie de la table des identifiants opaques (demande 2)

« La table des identifiants opaques a sa propre entropie, qui n'est pas celle de la configuration du bras et ne s'en déduit pas.
- **Où elle est tirée.** Du système, au moment où la table est tirée, par celui qui prépare les demandes des deux moniteurs à modèle de langue (côté habilité), avant toute production.
- **Qui la tient.** Elle est écrite dans le fichier de la table, avec la table, scellé dans un dossier tenu à part de l'étape de production ; personne d'autre ne la reçoit.
- **Ce qui est engagé.** L'empreinte du fichier de la table. Le manifeste scellé de chaque production la porte ; l'étape de production ne reçoit rien d'autre de la table.
- **Quand elle est révélée.** À l'ouverture de la table par la lecture commune des cinq moniteurs, après les cinq lignes d'ouverture et après le contrôle de l'empreinte des scores. La lecture commune vérifie alors que le fichier ouvert a l'empreinte engagée par les deux productions, rejoue le tirage à partir de l'entropie révélée, et refuse une table dont l'entropie est celle de la configuration du bras. L'engagement est rendu avec la preuve d'ordre.
| artefacts : production sans engagement ; table ouverte qui n'est pas celle de l'engagement ; table arrangée après coup (le tirage rejoué ne la rend pas) ; table tirée de l'entropie du bras ; fichier de la table modifié après son scellement : refusés ».

« Clés de graine du côté habilité : quarante et une (les plis, puis une permutation et un rééchantillonnage par moniteur et par dose). La clé `bras-a-v2/opaq/moniteurs` n'existe plus. »

**Limite à écrire au texte.** « Une demande de lecture porte le texte de l'action : une session qui tiendrait aussi les épisodes du rejeu retrouverait l'action d'une demande sans la table. L'opacité vaut pour l'étape de production, qui ne reçoit ni condition, ni épisodes, ni entropie, ni table, et pour les fichiers qu'elle rend. »

## 32. Réserve sur la trace du réglage fin, à la lettre (demande 3)

Texte gelé, `prereg/T0.8-base-A-mots-et-cout-v1.md` (`72b067d5b3f8c0d7f257677dbc86ace6cd1917b07f7a96e2263b91647dc6205d`), ligne BA-L3 de la table des lectures, réserve R-BA2 :

> « la base (A) apprise sur l'organisme à dose 1 range aussi l'adaptateur témoin au-dessus de l'honnête : elle peut lire la trace du réglage fin ; une dose où elle « réussit » peut l'être par l'adaptateur, non par le sabotage »

Condition de la ligne : contrôle de l'adaptateur (lecture de transfert) « au-dessus ». Suite de la ligne dans le texte gelé : « réserve R-BA2 ; la dose reste hors jugement si la règle de T0.6 le dit (sens prudent pour le critère 3) ». Le code du bras A la porte ainsi : `scripts/mots_et_cout_bras_a_v2.py` (`db124c6e29edf2e3547bf9b9f13c9fe311f0f53061baa997765efc30c429ebc1`), « réserve R-BA2 : à porter avec toute phrase des lignes de la table C quand elle s'applique ».

Sa voisine, R-BA2b (ligne BA-L3b, contrôle de l'adaptateur non calculable) : « contrôle de l'adaptateur non calculable (<motif>) : il n'est pas établi que la base (A) ne lit pas la trace du réglage fin ».

## 33. Les deux comptes de la règle du 1 % (demande 4)

« Le côté habilité rend, par moniteur et par dose, quatre comptes pour la règle du 1 % : les permutations demandées et les permutations perdues du plancher (champs `n_permutations`, `permutations_degenerees`) ; les tirages calculés et les tirages dégénérés de l'intervalle (champs `tirages`, `tirages_degeneres`). Ils sont rendus aussi quand le moniteur n'est pas calculable à la dose parce que l'un des deux dépasse 1 % ; la liste des nombres rendus les nomme. Ils restent vides quand le moniteur n'est pas calculable pour une autre raison, survenue avant (pli sans action, classe absente). »

## 34. Fichier des scores par unité : format exact, et étape où paraissent « condition » et « étiquette » (demande 5)

« `scores-par-unite-moniteurs-bras-a.jsonl` : une ligne JSON par moniteur, dose et unité ; dix champs et eux seuls, dans cet ordre : `moniteur` (l'un des cinq noms de 6.2), `dose` (`dose-0.25`, `dose-0.50`, `dose-0.75` ou `dose-1.00` : le jeu de la ligne), `cle` (clé de l'unité : l'action ; l'épisode pour l'agrégateur séquentiel), `condition` (`honnete` ou la dose), `tache`, `episode`, `pas` (nul pour l'agrégateur), `pli` (0 ou 1), `etiquette` (0 pour l'honnête, 1 pour la dose), `score`. Scellé ; jamais écrasé. »

« Deux fichiers, deux étapes. **Avant les ouvertures** : les fichiers de production des deux moniteurs à modèle de langue, à cinq champs (identifiant opaque, score, état de la balise, jointure, masse faible) ; ils ne portent ni condition ni étiquette. **Après les cinq lignes d'ouverture et l'ouverture de la table** : le fichier des scores par unité, écrit par la lecture commune ; c'est le seul fichier du côté des moniteurs qui porte `condition` et `etiquette`. »

## 35. Cas ouverts (demande 6)

- **Noyau d'attention.** La note « à citer » est corrigée par erratum : `docs/notes/bras-a-moniteurs-v1/a-citer-au-texte-moniteurs-a-modele-de-langue-v1-erratum-1.md` (empreinte au compagnon). L'agent est chargé avec `sdpa` ; la clé `noyau_attention = defaut` de la configuration de référence n'est pas lue par son lanceur.
- **Programme d'extraction.** `src/controle_ia/organismes_discrets/bras_a_v2_habilite/extraction_base_v2.py`, `d557c8396cf35acda5dfd21a8ad20cc146f337fd38f7db4cd10503d3fe7d2e0a`, commit `94c5dcbc` ; essais `tests/test_bras_a_v2_habilite_extraction_base_v2.py`, `acfa58ea452739e372ee4b114bf19a53edc7a90beebdf86ab3d9cda59046136a`.
- **Module des autres moniteurs.** Version 7, citée en tête ; notice `docs/notes/bras-a-moniteurs-v1/notice-developpeur-habilite-lot-16-v7.md` (pièce habilitée, à ne pas transmettre). Préparation des lectures : `src/controle_ia/organismes_discrets/bras_a_v2_habilite_preparation/preparation_des_lectures_v1.py`, `72d2216747c102bc5dca12227bb6e6648c20a121b72edcaefa51c817ad037dae`, commit `2ee2a8cf`.
- **« Renvoi de la base par le lecteur habilité ».** Ce n'est pas dans le mandat du développeur habilité côté moniteurs, et rien de tel n'a été écrit ni fait dans cette session : la pièce et son auteur sont à désigner par la mère.
