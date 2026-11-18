# Quatre lectures sans dépense de l'inventaire des courses anciennes — mode d'emploi du dossier (v1)

- **Écrit** le 18 novembre 2026 vers 06:10 UTC par le sous-agent critique de complétude (Claude Opus 5.5), sous l'autonomie GO-2026-11-18-05 et le « go » de Lazar aux quatre lectures (R-3168, R-3170). Inventaire : `docs/notes/inventaire-collisionneurs-organismes-v1/inventaire-v1.md` (`b49dc246…`), section B, points 1 à 4, et section E, nœuds 1 à 4.
- **Règle de lecture** : la version 2 de chaque note a été écrite par son contre-lecteur, après le verdict « à corriger ». Elle porte des corrections de fait, et la version 1 reste intacte (R12). **Aucune version 2 n'a été revue par un tiers.** Tout ce que disent les modèles est un avis (R7 : chiffres de l'état de l'art non vérifiés ; R8 : zone dite vierge = question).
- **Critique de complétude** : `critique-de-completude-v1.md`, sha256 `a7ad1b91f015e8b00b470b605efd5688d280ae59a6bca4b7e8391cb0e2cda0c8`. Quinze manques, aucun qui invalide une note.

## 1. Tours du collisionneur du 26 octobre : intégration de l'explorateur de neurones, et « déjà propre » (inventaire B.1, nœud 1)

- **Note en vigueur** : `collisionneur-26-octobre-v2.md`, sha256 `2a0febbaaf519e659edc21fc2c26b15c49bd650d41b5bec3624e48adc7f36eb0`. Version 1 : `collisionneur-26-octobre-v1.md`, `dac5edd1…`.
- **Contre-lecture** : `contre-lecture-collisionneur-26-octobre-v1.md`, `0a4e97d0…`. Verdict : **à corriger**, six corrections de fait. Une réserve de cloisonnement (ligne 314 de la conception de B, tour « déjà propre ») attend le choix de la mère.
- **Sources** : branches `donnees/collisionneur-neuron-explorer-v1` (`191a658`) et `donnees/collisionneur-already-clean-v1` (`08e6b31`). Les 18 cellules ont été lues, moins 66 passages exclus (famille 2). Aucun critère n'a été scellé avant l'ouverture (manque 10 de la critique).
- **Ce qu'elle apporte et à qui** :
  1. *Lecture par lentille neuronale* : dix-neuf idées absentes de la lecture du 13 novembre (témoin de format, sonde de la couche 0, modèle à poids aléatoires, sondes à étiquettes permutées, divergence par direction). Dix questions sont posées à la tranche en cours, mais son texte gelé a été scellé à 04:22:35Z (R-3175) : elles ne peuvent plus servir qu'à un addendum ou à la tranche suivante.
  2. *Sondes* : à préenregistrer d'abord sur des sondes de recettes publiques. La grille thème × format × état, le nul du maximum à longueur égale, les sondes permutées lues au maximum. La poussée reste une mesure (N-015). « Une détection non lue est fragile » est une prédiction de B, à rapprocher de H8.
  3. *Papier B* : rien de direct. Trois leçons de statistique : le nul du pic par agent doit être apparié en longueur ; le nombre de témoins borne la plus petite valeur p atteignable ; ne rapporter que le maximum des tirages biaise vers le haut.

## 2. Collisionneur à cinq espèces du 2 novembre : sélection d'une génération à l'autre, et vérification non circulaire du bac à sable (inventaire B.2, nœud 2)

- **Note en vigueur** : `collisionneur-2-novembre-v2.md`, sha256 `e18a3ec6b7b56cdf775139a6f9aa493d12fa2230b4d1fd15f4bbb0c152f4f0ad`. Version 1 : `collisionneur-2-novembre-v1.md`, `c4980860…`. Critères scellés avant ouverture : `criteres-lecture-collisionneur-2-novembre-v1.md`, `4f5604b5…`.
- **Contre-lecture** : `contre-lecture-collisionneur-2-novembre-v1.md`, `65dc2312…`. Verdict : **à corriger**, quatorze corrections de fait. Les comptes d'accord ont été ramenés à ce que prévoient les critères, et six oublis ajoutés.
- **Sources** : branche `donnees/collisionneur-v8-runs-v2` (`0e7b3e5`), 30 cellules présentes et valides. L'espèce B est Opus 4.6 (R-1050). **Les dix critiques croisées n'ont été lues par personne**, alors que les critères les prévoyaient (manque 1).
- **Ce qu'elle apporte et à qui** :
  1. *Organisme à plusieurs générations, sélection* : neuf points attribués et préenregistrables. Plus de deux états de fiche ; seule la fiche promue se reproduit ; épreuve de confirmation jamais vue ; la mémoire transmise est un second canal de fuite ; audit terminal commun avec un bras de parents aléatoires. C borne la course à deux générations tant que l'héritage n'est pas montré.
  2. *Organisme à plusieurs générations, tests de mort dans le bac à sable* : sept points. Le chiffre `RESULTAT:` est une auto-déclaration ; « survit » n'est pas « correct » ; la boucle de retour est le canal qui compte ; le dossier de travail est partagé entre exécutions ; E signale un défaut de la sonde réseau sur le code du 1er novembre. Rien n'est encore confronté à la conception v4 ni au brouillon 3 du préenregistrement (R-3051).
  3. *Lazar* : quatre points sans recommandation. Le sort de la fiche non concluante ; le rang du juge servi ou non aux proposeurs (le lien avec N-053 est une remarque du lecteur) ; le cache entre exécutions ; le libellé du verdict des tests de mort.

## 3. Avis d'Argon sur la porte G0 (inventaire B.3, nœud 4)

- **Note en vigueur** : `avis-argon-g0-v2.md`, sha256 `815d19be6db72b567de411e7f13059a85a2c88655cf5d693fa825767b36b6c76`. Version 1 : `avis-argon-g0-v1.md`, `833d0a45…`.
- **Contre-lecture** : `contre-lecture-avis-argon-g0-v1.md`, `800958de…`. Verdict : **à corriger**, huit corrections de fait (chronologie, contre-lecture 7 attestée hors de `main`, citations, une interprétation devenue question).
- **Sources** : `main`, commit `2005f3ae`. Avis connu **de seconde main** seulement, par la lecture de Fable du 31 octobre (`be2b3c4d…`). Les réponses brutes d'Argon, sur `donnees/sauvegardes-restaurees-2026-10-31-v1`, ne sont pas lues (manque 3). La question A et une partie de C sont exclues (famille 2).
- **Ce qu'elle apporte et à qui** :
  1. *Grille de lecture de G0* : aucun critère n'est changé. Rapportés à la v8, la plupart des points d'Argon sont déjà traités. Quatre questions neuves : les quatre points « condition contre réserve » à trancher ensemble ; le critère visé par D-G0-5 ; l'invalidation volontaire qui échapperait au gel ; une règle pour les trois causes sans ouverture.
  2. *Grille de lecture de G0, après la v8* : dates du 15 et du 30 novembre périmées par le décalage à fin décembre (GO-2026-11-18-01). Il manque le filtre par dose du critère 3 (N-063 v2). N-062, N-066 et N-068 sont absentes de la grille. La contre-lecture 7 est à verser sur `main`.
  3. *Lazar* : dix-sept questions pour la prochaine version de la grille, toutes des nœuds sans défaut. Les deux premières portent sur les nouvelles échéances et sur la borne du 31 janvier 2027 (R-750, R-765). Rien n'est encore repris dans la grille (manque 11).

## 4. Courses de l'organisme et tours du collisionneur sur les questions des mentors du 3 novembre (inventaire B.4, nœud 3)

- **Note en vigueur** : `mentors-releve-d-ensemble-v1.md`, sha256 `f7eaec6f097859864433f69413233a756ebf241ea541f7eb54b3648818caf9c0`. Elle est faite **seulement** à partir des six relevés ci-dessous, en version 2, sans source rouverte.
- **Contre-lecture** : **aucune** pour le relevé d'ensemble (manque 7 ; quatre contrôles par sondage dans la critique). Les six relevés par question ont chacun la leur, toutes au verdict **à corriger**, chacune avec une version 2 :

| question | relevé en vigueur | sha256 | contre-lecture (verdict) |
|---|---|---|---|
| Heimersheim, question 1 | `mentors-heimersheim-v2.md` | `806b61eacc27659e008f8a21fed330ea6115d2764c290b5c21cf463f54d7a910` | `contre-lecture-mentors-heimersheim-v1.md`, `c4d32891…` (à corriger, sept) |
| Kirchner, question 2 | `mentors-kirchner-q2-v2.md` | `f03397782d314a371b487b2439462411dbb1e9563251a99a7fe6db39fd376e84` | `contre-lecture-mentors-kirchner-q2-v1.md`, `497d1f45…` (à corriger, dix ; **version 2 conditionnelle**, retraits de cloisonnement) |
| Ibrahim, question 1 | `mentors-ibrahim-q1-v2.md` | `4fe650ba38c5141bd01c8295931265baeee77bd777ee53ecd6ef83dda00f11ed` | `contre-lecture-mentors-ibrahim-q1-v1.md`, `d9583950…` (à corriger, huit) |
| Scheurer | `mentors-scheurer-v2.md` | `2c320c940ce3eab43e1ad837e04848470330089e129a525b966b5e83127eab1b` | `contre-lecture-mentors-scheurer-v1.md`, `52b8922c…` (à corriger, onze ; **version 2 conditionnelle**, retraits de cloisonnement) |
| Colognese et Ward, question 2 | `mentors-colognese-ward-q2-v2.md` | `65993b4857b7e4589675c59fa83dc5ffb4f6c37bb68a0b29672f4005a28866c3` | `contre-lecture-mentors-colognese-ward-q2-v1.md`, `5caecc22…` (à corriger, huit) |
| Jang et Feng | `mentors-jang-feng-v2.md` | `4218672fdbcaf5cfd306ac17c43dee3f6be1561e21a77565434e61d725ba957e` | `contre-lecture-mentors-jang-feng-v1.md`, `31cd2bf1…` (à corriger, dix) |

- **Sources** : les 22 branches de l'inventaire (dix courses, douze branches de tours), toutes citées. Ne sont pas lus : les critiques croisées des tours, au-delà de leurs titres (manque 2), et les deux appels seuls d'Astra et d'Argon sur Heimersheim (manque 4). À Scheurer, 10 fiches sur 22 sont exclues.
- **Ce qu'elle apporte et à qui** :
  1. *Atelier d'idées de l'organisme* (rôle 2 de N-065) : 93 idées sans classement, chacune avis d'un proposeur, et seize fils communs. Parmi eux : la dose-réponse, les planchers de sondes aléatoires appariées en covariance, « lisible n'est pas causal », rejouer la sélection dans la loi nulle, calibrer le seuil sur la bonne population.
  2. *Papier C* (rôle 1 de N-065) : par le thème, surtout Kirchner et Colognese-Ward. Comme données réelles de courses, sous réserves : deux courses seulement sont complètes à cinq espèces, Kimi est refusé au format dans quatre courses, juges et lecteurs ne viennent que de deux espèces, aucun témoin planté, étiquette « jouee » à vérifier.
  3. *Sondes et mère* : les fils sur les sondes rejoignent la reconception (N-062) et la famille tenue à l'écart. Six montants de course, environ 41,82 USD, manquent au registre des dépenses : les inscrire est un geste de la mère. Six entrées restent en réserve de cloisonnement, à trancher par elle.

## Autres fichiers du dossier

Les versions 1 des notes et des relevés, conservées (R12), et leurs compagnons `.sha256`. Tous les fichiers sont scellés et vérifiés OK au 18 novembre vers 06:00 UTC.
