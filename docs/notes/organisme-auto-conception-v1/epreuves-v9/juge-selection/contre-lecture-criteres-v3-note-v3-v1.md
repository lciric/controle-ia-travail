# Contre-lecture des critères de choix v3 et de la note sur le juge v3 — v1

- **Contre-lecteur** : modèle O, neuf. Je n'ai écrit ni les critères v3, ni la note v3, ni aucun rejeu, ni aucune carte (règle R2). Écrit le 2026-11-19 (`date -u` : 2026-11-19T14:37:35Z). Hors ligne, processeur seul, aucune dépense, aucun appel de modèle.
- **Pièces contre-lues**, empreintes recalculées, égales à leur compagnon `.sha256`, et vérifiées par `controle_ia.scellement verifier` :
  - `criteres-choix-cartes-v9-v3.md`, sha256 `1ce419031644eac6060378ed283bdd2966477d6d444fa54637f8866b4ee01b6e` (commit `5b32b99e`, 2026-11-19T14:28:23Z, seul avec son compagnon) ;
  - `note-conception-juge-selection-cartes-ecartees-v3.md`, sha256 `de9d144d753d2fa28e327ababa9f27c230789275db7f2287464bbb9a06256622` (commit `33749139`, 2026-11-19T14:31:51Z).
- **Lus en plus** : la contre-lecture précédente `contre-lecture-juge-v2-criteres-v2-rejeux-v1.md` (`c75a9abc40e3dd8fef5e17ac9cae61bc7d6f0fa53bc375358e6ad344ea34bc95`) ; les critères v2 (`4ae09b15e2816fcda0ba0ba008ca11b58906d7712351253d04f52214e9a629c1`), par différence ; sur `main` (commit `d494392d`) : la note de littérature `docs/notes/organisme-auto-conception-v1/juge/litterature-juges-preference-pour-soi-v1.md` (`bb54b685dfcec23b0c6ec6813dc87385ea1cebac1ed311319e190183bce8bac9`), les critères v1 (`8881dbb2f63bdfedba34c971e5fb7081fc244ab5c3555307482589b84d837326`), les lignes GO-2026-11-19-60, -63, -65, -67, -68, -69 et -73 de `registres/go.md` ; six sources de `docs/sources/juges-de-cartes-v1/`, empreintes égales à leur compagnon : `nature-2018-sinkjaer-golden-ticket.pdf` (`915ffea75e753638…`), `villum-experiment-selection-process.pdf` (`5ab9cde12ec1b9b6…`), `arxiv-2102.09958.pdf` (`1b5b34af4acad508…`), `arxiv-2605.29800.pdf` (`2d124db474e91a7d…`), `arxiv-2609.17857.pdf` (`142e0b811ad4fd28…`), `arxiv-2409.04109.pdf` (`fc1d14afd403c19b…`), en texte extrait ; sur la branche, les lignes 9 et 28 de `ordre-de-passage-epreuves-v9-v3.md` (`b19f550b525fe5696321167bd43a35fa5ece180fd2f97dad5dfc6e970a8c0f67`), pour ce qu'elles disent de la définition scellée de l'« amélioration considérable » (`4eae96bc…`, que je n'ai pas ouverte).
- **Non lus** : aucune carte, aucun fichier de cartes, aucun fichier de sélections, aucun rejeu, aucun verdict de juge, le classement, le coffre, le champ de l'espèce.

## Ce qui est vérifié et tient

**Scellés avant toute lecture de carte de ce cycle.** Ordre sur `lot/compte-organisme-v1` : contre-lecture précédente `8b4fa90a` (14:20:38Z), critères v3 `5b32b99e` (14:28:23Z), note v3 `33749139` (14:31:51Z). Aucun rejeu des critères v3 n'existe à cette heure. Les critères ne portent aucun identifiant de carte ; la note n'en porte que dans le texte repris de la v2. Le rédacteur n'a lu le contenu d'aucune carte, mais il a vu les tableaux par carte des rejeux (identifiants, titres, notes) et deux fragments cités par la contre-lecture (« sinon couper »). Il le déclare (critères, limite 1 ; note, en-tête). Il n'est donc pas aveugle à la v9. Un rejeu de la v3 sur la v9 n'est pas une épreuve tenue à l'écart, et c'est écrit.

**Les huit constats de la contre-lecture `c75a9abc…` portant sur la note et les critères sont appliqués.** Ce sont les « constats 1 à 6 » du mandat ; la contre-lecture les numérote de 1 à 8. Je les ai vérifiés un à un contre le § 8 de la note :
- 1 : tableau du veto refait sur sept titulaires ;
- 2 : veto des lecteurs porté aux confirmations (critères § 13, point 1 ; note § 9) ;
- 3 : GO-69 intégré, rapport de coût obligatoire (critères § 0, § 7, § 13) ;
- 4 : faits des rejeux dans le verdict, le § 2 bis, le § 5 et la fiche ;
- 5 : parenthèse du C5 de la v1 rétablie mot pour mot (« garder, retirer ou régler un module »), conforme aux critères v1 ;
- 6 : construction du tirage fixée (§ 9). Je l'ai exécutée : `SeedSequence([int(h1, 16), int(h2, 16)])`, `spawn(3)` puis `PCG64` tournent, et deux constructions identiques donnent les mêmes tirages ;
- 7 : X1 non séparable rendue à Lazar, défaut écrit. C'est conforme à GO-63, point 1, et au précédent de GO-73 ;
- 8 : les cinq questions en toutes lettres, identiques mot pour mot au C2 des critères v1 ; (c) en trois sous-strates ; garde du tiers.

Les constats 9 à 12 (erratum du rejeu O, précisions du rejeu F) sont hors de ces deux pièces. Je ne trouve aucun erratum versé dans le dossier : c'est à la mère de les suivre.

**Ce qui n'est pas un critère.** Le texte tient sur les points suivants :
- le coût, le nombre de bras et la dépendance au branchement ne sont dans aucune note, aucun plancher et aucune clé (§ 0, § 10) ;
- aucune espèce n'est lue par un lecteur ; le filtre de lignée du veto et les comptes par espèce se font par programme, après dépôt ;
- le verdict des juges et le classement de l'orchestrateur sont exclus (§ 0, § 10) ;
- le plancher est celui de la v2, et rien de l'échelle fine n'y entre (§ 4, § 5.3) ;
- le rang n'existe qu'à l'intérieur d'une voie ; les places réservées et le tour de rôle protègent chaque voie (§ 6). **Aucune question de l'échelle ne peut peser contre une voie dans la proposition.**

**GO et décisions.**
- GO-60 : tenu pour le coût. L'axe A pose un problème, au constat 2.
- GO-63 : tenu (point 1 par X1, point 4 par la dépendance au branchement rapportée).
- GO-67 : tenu (K donné d'après la charge).
- GO-68 : tenu. V vaut 2 ou 3, dans la lettre « deux ou trois » ; l'écart « par juge » est dit et porté aux confirmations.
- GO-69 : tenu à la lettre (le coût est écrit à côté de la note, n'élimine rien, sert à l'ordre de passage ; « il ne sort pas entièrement des critères » : § 7 obligatoire).
- N-058 : le veto, les lecteurs et la règle proposent, l'épreuve tranche. Le taux de réussite des veto ne choisit ni ne pondère personne.

**Littérature citée fidèlement.** Tout est conforme à la note `bb54b685…`, et je l'ai vérifié sur les six sources :
- un « golden ticket » par évaluateur (Sinkjær, p. 143) ;
- « A reviewer can cast one decisive vote », « The panel doesn't meet or interact » (Villum, p. 1) ;
- tirage parmi les propositions dont l'intervalle crédible chevauche la ligne de financement (Heyard et al., p. 1) ;
- neuf juges de sept familles, nombre effectif de votes de 2,0 à 2,5 (Kohli, p. 1-2) ;
- quatre familles, lecture par colonne, et un « independent human-consensus anchor » comme contrôle de qualité (Awuni et al., p. 1-2) : la « référence de qualité extérieure aux juges », que le § 12 des critères rattache à ce papier, y est donc bien ;
- style uniformisé avant la relecture (Si, Yang et Hashimoto, p. 2).

« Devenu vote décisif » est une lecture permise : le ticket figure chez Sinkjær, le vote décisif dans le schéma actuel de la fondation.

**Tableau du veto juste.** Je l'ai recalculé :
- 4 et 6 cartes (4 % et 6 % de 94) ; 14 et 21 (15 % et 22 %) ;
- par rapport aux neuf lignes visées : moins de la moitié, une fois et demie, deux tiers, plus du double ;
- par lignée, à deux titulaires : 4 et 6, ou 2 et 3 pour la lignée d'un lecteur ;
- par lignée, à sept titulaires : 12 et 18 pour une lignée qui n'a qu'un titulaire (six hors d'elle), 10 et 15 pour la lignée d'un lecteur (cinq hors d'elle) ;
- charge à deux scellements par jour : 2, 7, 3 et plus de 10 jours.

Les options (a), (b) et (c) de la décision 2 reprennent ces nombres sans erreur, et les « 10 » et « 15 » de la v2 ont disparu.

**Comptes de la note.** Ceux du § 2 bis correspondent à la contre-lecture `c75a9abc…` : 28 cartes à 12, 60 à 11, 2 à 10 et 2 à 9 ; 1 sur 9 ; 0 sur 3 ; 4 en commun ; 3 sur 9 ; 46 et 25 ; 16 sur 23 ; aucune Astra, aucune Argon, aucune Opus, 1 Carbon, 2 Fable et 25 sans espèce. La lecture par colonne du § 4 bis est exacte : écarts de 7, 3, 2 et 4, et aucun pour Astra, à plafond.

**Fiche au format** (décision en une phrase, enjeu, trois options avec avantage et inconvénient, recommandation et confiance, défaut sous 48 heures) pour les deux décisions. Verdict d'abord. Aucun identifiant de modèle dans les deux pièces.

## Constats

**1. Moyen — l'échelle fine ouvre un canal par la manière d'écrire, et sa seule garde est un rapport.** Plusieurs items demandent ce qu'un préenregistrement ajoute sans toucher au mécanisme :
- T3 : statistique et seuil chiffré, alors que la note, § 6, dit que « les seuils se fixent au préenregistrement » ;
- B2 : quantité appariée nommée ;
- B3 : plusieurs doses ;
- B4 : contrôle positif ;
- S1 : réglage ;
- S3 : issue intermédiaire ;
- S4 : autre ligne nommée.

Une carte brève y reçoit « non » ou « indécidable », qui comptent tous deux 0. La règle « oui si cela suit sans rien inventer » ne couvre pas ce qui ne peut pas se déduire. C'est en tension avec le § 5.1 (« sur l'épreuve que la carte permet, non sur sa prose ») et avec la logique du critère E, où ce qui « peut être ajouté sans toucher au mécanisme » n'abaisse la note que d'un point. L'axe B récompense en outre les épreuves à plus de bras (B1, B3, B4), contre le § 0, qui sort le nombre de bras des critères. Or les pièces versées disent que les cartes d'Astra sont les plus courtes et ne citent pas. Le rang, qui décide de ce qui est proposé en premier, est précisément la porte par laquelle la sévérité est revenue en v2 (constat 5 de `c75a9abc…`). La v3 le déclare (limite 2, § 5.3, § 11), mais ses gardes ne font que rapporter, et ne sont pas définies :
- « un item qui sépare les espèces plus qu'il ne sépare les cartes à l'intérieur d'une espèce » n'a ni statistique ni seuil ;
- « un écart fort » non plus.

Ce n'est pas une sévérité contre une voie, ni une lecture d'espèce, de coût ou de verdict. Mais la question de Lazar (« trop sévères pour astra et carbon ») peut revenir par là sans que rien ne s'arrête : les deux conditions d'adoption de la décision 1, option (a), ne mesurent que le pouvoir de ranger.

**Correction** :
- (i) définir ces deux gardes par une statistique et un seuil écrits avant l'ouverture, dans le programme d'assemblage scellé (§ 1) ou dans des critères v4 ;
- (ii) dans la fiche, décision 1, option (a) : si l'audit de la règle R4 se déclenche, pour toute espèce et dans les deux sens, retour à Lazar **avant** adoption. Ce n'est pas une condition de réussite, et cela ne retouche aucun item : cela n'est pas viser un signe (règle R3) ;
- (iii) proposer à Lazar, comme option et non comme réglage, de répondre « oui » aux items qui peuvent s'ajouter au préenregistrement sans toucher au mécanisme, à l'image du critère E ; ou de ranger d'abord sur les items qui portent sur l'idée (T1, T2, T4, A, S2).

**2. Moyen — l'axe A se dit « l'amélioration attendue de GO-2026-11-19-60 », qui est liée à une définition scellée.** GO-60 : « "Considérable" est défini par un lecteur […] et scellé avant qu'il ouvre les cartes ». D'après l'ordre de passage v3 (ligne 28), cette définition (`4eae96bc…`) mesure plus de lois vraies promues ou moins de lois fausses promues, à budget apparié, face à un témoin. Elle exclut d'avance « un instrument qui mesure sans changer ce qui est promu ». La variante de A1 pour la voie I (« l'instrument commande une décision d'adoption ») ne coïncide pas avec cette exclusion. Le § 7 dit bien que l'axe A ne remplace pas la définition, mais le § 5.2 écrit « C'est l'amélioration attendue ». Deux lectures de la même notion de GO pourraient se contredire à l'ordre de passage. **Correction** : écrire « voisine de l'amélioration attendue », et dire que la définition scellée fait foi à l'ordre de passage tant que Lazar n'en décide pas autrement.

**3. Moyen — la sévérité contre une voie peut revenir par l'ordre de passage, et seul le compte par espèce y est demandé.** Si l'ordre de passage applique la définition scellée, qui exclut l'instrument qui mesure sans changer ce qui est promu, la voie I passe en dernier. Or la voie I est celle où les instruments tombaient par construction en v1 (écart 2 de la proposition `a2cd45ad…`). Le § 7 des critères et le § 9 de la note ne demandent que la part de chaque espèce dans chaque tiers de l'ordre. **Correction** : demander aussi, par programme et après coup, la part de chaque voie et sous-strate dans chaque tiers, dans les deux sens, et le dire dans la fiche (« ce que tu dois savoir »).

**4. Mineur — des cas que le programme d'assemblage doit trancher par écrit, pour que deux applications donnent le même résultat** (même nature que le constat 6 de `c75a9abc…`) :
- un veto déposé sur une carte qui se trouve ensuite dans le nombre visé ou dans le lot : est-il consommé, ou remplacé par la suppléante suivante ? Les rejeux v2 ont eu ce cas ;
- les cartes « X1 non séparables » sont-elles dans les n lignes de la permutation de l'enfant 1 ?
- **départage du porteur d'une fusion** : à note fine égale, le porteur est choisi par numéro de tirage. Or ce numéro est attribué aux lignes, dont l'identité dépend du porteur. C'est circulaire : il faut permuter les cartes, non les lignes, ou départager le porteur par l'ordre canonique ;
- les clés 3 à 6 du § 10 portent-elles sur les seuls items gardés ?
- une carte rangée dans deux voies par les deux lecteurs : A1 et A4 y sont répondus sous deux définitions (voie I ou non), puis sommés ;
- deux lecteurs qui voient X1 tous deux, mais en désaccord sur la séparabilité ;
- « chez les deux lecteurs », dans la garde du tiers (§ 3) : chez chacun, ou chez l'un ?

**5. Mineur — accord brut sans correction du hasard.** Un item dont la part de « oui » dépasse environ 0,854 atteint 0,75 d'accord au hasard. Entre 0,854 et 0,9, il est donc gardé sans être déclaré « sans pouvoir de ranger ». Le bruit est petit. Rapporter un kappa à côté, comme l'a fait `c75a9abc…`.

**6. Mineur — la clé 7 (plus petit écart de note fine entre lecteurs) n'est pas un contenu de la carte.** Elle abaisse la part comptée « au tirage » sans rien dire de l'épreuve, et elle peut suivre la manière d'écrire (une carte brève appelle plus d'« indécidable » chez l'un que chez l'autre). La garde « le rang est un tirage » (§ 6) devrait compter aussi, à part, les places décidées par la clé 7.

**7. Mineur — note, § 1 : « presque toutes les cartes ont la note maximale ».** C'est vrai chez le lecteur O (90 sur 94), non chez le lecteur F (28 sur 92, toutes à un point du maximum). À écrire ainsi.

**8. Mineur — les six confirmations de la note, § 9, n'ont pas de défaut écrit.** Les choix de conception de la sélection sont « proposer avec recommandation ». Écrire le défaut : tel qu'écrit dans les critères v3, pour le rejeu seulement.

## Verdict

Scellable après corrections.

Les critères v3 ont été versés avant toute lecture de carte de ce cycle, par un rédacteur qui n'a lu le contenu d'aucune carte et qui déclare ce qu'il a vu des rejeux. Les huit constats de la contre-lecture précédente qui portaient sur ces deux pièces sont appliqués. La règle range désormais à l'intérieur d'une voie seulement : sans espèce, sans coût, sans nombre de bras dans les clés, sans verdict de juge. Elle tient GO-60 pour le coût, ainsi que GO-63, GO-67, GO-68, GO-69, GO-73 et N-058. La littérature est citée fidèlement, vérifiée sur six sources. Le tableau du veto est juste, et la fiche est au format.

Les critères v3 sont scellés et aucune carte n'a été ouverte : les corrections se font sans les réécrire (règle R12), avant le rejeu, par des critères v4 ou par une pièce de précisions scellée avec le programme d'assemblage. Pour la note, il faut une v4 ou un ajout scellé. Six points :
- les deux gardes de l'échelle fine définies d'avance, et le retour à Lazar avant adoption si l'audit de la règle R4 se déclenche (constat 1) ;
- l'axe A dit « voisin » de la définition scellée de GO-60 (constat 2) ;
- la part de chaque voie dans chaque tiers de l'ordre de passage (constat 3) ;
- les cas d'assemblage tranchés par écrit, dont le départage circulaire du porteur d'une fusion (constat 4) ;
- le kappa rapporté et la clé 7 comptée (constats 5 et 6) ;
- deux retouches de la note (constats 7 et 8).

L'échelle fine n'est pas éprouvée. Qu'elle range, et sans lire une manière d'écrire, reste à voir au rejeu, puis à la course suivante.
