# Devis — passe unique d'activations et de notation par les sondes internes gelées sur les jumeaux honnêtes du vrai agent (versant honnête de l'essai « jumeau contre jumeau ») — v1

- **Date** : 2026-11-24T09:51Z (`date -u` de cette machine). **Auteur** : Claude Fable 5.2, effort élevé, sur la consigne `consigne-fable-devis-versant-honnete-v1.md` (`77e07c2e1ceaadb1cce96e0cf566c8e19630e18f4167f64288e537a3afb89fc0`). Dépôt à `ca7f4c8b7`.
- **Statut** : pièce de classe A, **non scellée, à contre-lire** par un Opus 5.5 neuf. Elle n'ouvre aucune dépense. Aucune sortie de course, aucun score, aucun journal, aucun code n'a été ouvert.
- **Sources** (chemin, empreinte ; citées ensuite par leur nom entre crochets) :
  - [instruction] `docs/notes/dossier-entretien-2026-12-01-v1/instruction-b6-versant-honnete-jumeau-v1.md`, `df6d6dfe1cd78403f100b97dcebc2eccbad24934045ebe66bd2cc841a704e6d8` ;
  - [écarts] `…/ecarts-sources-honnetes-b6-v1.md`, `e843960269d9ebbd7e171c394f996e8b37bf6dd39d79dd3ec80ebc236151d2cf` ;
  - [attestation] `git show 2f63d6db:docs/notes/dossier-entretien-2026-12-01-v1/attestation-manifestes-versant-honnete-v1.md`, `e3f1ee567c79b4f3891b9d16286c81f2e808061bde89ccaa72bda59442a25239` ;
  - [étalonnage] `git show 50a6d30c:prereg/T0.8-bases-boite-noire-v0-v3.md`, `72a2611b3eff8ef070ab6f12f1468213cb88a8f42729eb2e9edeea7fcb884918` ;
  - [modèle] `docs/notes/rejeu-activations-saboteur-voie-a-v1/devis-passe-activations-saboteur-voie-a-v2.md`, `9a4a794c4332f72d720c23a38db3c0c0a4175ee9a55e34d9627cc16e871eff45` (machines, durées, coûts et gardes seulement) ;
  - [référence honnête] `docs/decisions/decision-N-076-assurance-par-audit-et-reference-honnete-v1.md`, `49b664c1d6a72fdb239d9a52e70ec85c4829fc5e77c6b5d3cf27848ce1a8dd78`, avec son erratum 3 (`3335284d40efe6e4454b0eaf6e3086982a074b5ef3d9e6e87ef7844a5d40f992`), qui prime ;
  - [registre] `registres/decisions.md` (`35d528ca957422fcadde47730d1da7204a42d8870d6638089fa57e8c4b27bbf3` à ma lecture), lignes R-5249 et R-5187 seulement.

## 1. Ce qui est acheté

Une seule passe sur carte graphique, sans aucune génération de texte ni aucun juge. Elle relit, jetons imposés, les actions déjà écrites par l'agent honnête (Llama 3.1 8B Instruct, révision `0e9e39f2…`, modèle de base nu), enregistre les activations aux couches que fixe le texte des sondes gelées (7, 15 et 23 selon [instruction], § 1 ; à confirmer sur ce texte, non lu ici), et note les sondes gelées, sans rien apprendre ni recalibrer.

- **Les 320 épisodes de l'étalonnage de la base boîte noire** (course `20261123-060509-t08-reel`), soit 3 200 actions ([instruction], § 1, tableau, ligne 1). Aucune activation n'y a été enregistrée ; textes et identifiants de jetons ont été gardés et poussés, « les activations restent recalculables par une passe unique » ([étalonnage], plan, épisodes d'étalonnage).
- **Les 64 épisodes honnêtes de la course de confirmation de l'organisme à adaptateur** (`20261111-151701-t06-reel`), soit 640 actions. Ils ont déjà leurs scores de sondes ([instruction], § 1, tableau, ligne 1 : lignes `SCORES-T07` et `SCORES-BBIS`). **Je recommande de les repasser quand même**, dans la même passe : leurs scores existants viennent d'un autre traitement (adaptateurs injectés à dose 0, lots mêlés à trois conditions à consigne : [attestation], Q1, réserves 1 et 2). Surcoût attendu : 640 × 0,40 s ≈ 0,07 h, soit ≈ 0,08 dollar. Les scores existants ne sont pas jetés : ils servent de pont (§ 3, garde 2).

Total : 3 840 actions. Ne sont pas achetés : les scores boîte noire, qui existent déjà, non lus ([instruction], § 1) ; l'analyse, sur processeur, 0 dollar.

## 2. Machine, durée, coût

**Machine** : une carte NVIDIA A100 à 80 gigaoctets en module serveur (même type que les deux courses : [étalonnage], « Machine »), à la demande, jamais interruptible ; disque de 100 gigaoctets. **Repli de rang 1** : NVIDIA A100 80 gigaoctets en carte d'extension. Toute autre carte : mot de la mère. Filtre bloquant avant création, repris de [modèle], § 2.3 : offre vérifiée, fiabilité ≥ 0,97, carte ≤ 1,35 dollar de l'heure, stockage ≤ 0,40 dollar par gigaoctet et par mois, réseau ≤ 0,04 dollar par gigaoctet.

**Prix** : 1,0644 à 1,1360 dollar de l'heure relevés le 24 novembre à 03:44:56Z pour cette carte ([modèle], § 2.2, qui cite `releve-offres-vast-2026-11-24-v1.json`, `0cd4113e…`, non relu par moi). **Débits** : 0,40, 0,85 et 1,60 seconde par action en lots de 8 (attendu, haut, pire : [modèle], § 3.1) ; en borne basse, la passe unique par épisode du premier test, 240 épisodes de 4 319 jetons en 108,4 s ([étalonnage], « Durées »), soit ≈ 173 s pour 384 épisodes. **Gardes** comptées à 768 passes d'action (4 × 5 % de 3 840 ; supposé). Mise en place, archives, poussée et réseau : valeurs de [modèle], § 3.1 à 3.3.

| scénario | mise en place | passe | gardes | archives et poussée | durée | carte et stockage (dollars) | réseau (dollars) | **total (dollars)** |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| bas (passe par épisode ; 1,0644 dollar de l'heure ; 20 gigaoctets entrants) | 0,31 h | 0,05 h | 0,10 h | 0,25 h | 0,71 h | 0,77 | 0,82 | **≈ 1,6** |
| **attendu** (1,14 dollar de l'heure ; 40 gigaoctets entrants) | 0,40 h | 0,43 h | 0,09 h | 0,40 h | 1,31 h | 1,54 | 1,62 | **≈ 3,2** |
| haut (1,30 dollar de l'heure ; 45 gigaoctets entrants) | 0,75 h | 0,91 h | 0,18 h | 0,75 h | 2,59 h | 3,51 | 1,84 | **≈ 5,4** |
| pire, hôte au bord du filtre (1,35 dollar de l'heure ; 45 gigaoctets entrants) | 1,25 h | 1,71 h | 0,34 h | 1,25 h | 4,55 h | 6,39 | 1,88 | **≈ 8,3** |

**Plafond proposé : 12 dollars des États-Unis**, cumulés, toutes tentatives. Coupure dure par instance : 10 dollars tout compris, déclenchée à 9,60 ; horloge : 5 heures depuis la création (à cette horloge, un hôte conforme coûte au plus 8,91 dollars). Le plafond laisse la place d'une relance technique (incident à une heure, ≈ 3,3 dollars, puis relance au scénario haut : ≈ 8,7 dollars au total), à laquelle une panne déclarée donne droit ; la coupure de la relance est le solde restant. Aucune relance automatique.

**Repli sans dépense** : si la passe ne peut pas partir, le versant honnête se lit sur les seuls scores boîte noire existants. Il perd la comparaison entre sondes et boîte noire ; c'est à la prévision de le dire, non à ce devis.

**Clés : je ne présume rien.** La ligne R-5187 de [registre] constate qu'un conteneur n'avait ni la clé du loueur ni celles des interfaces. Trois secrets sont nécessaires, lus par leur nom, jamais écrits au dépôt ni dans une conversation : la clé du loueur Vast.ai, dans l'environnement de la session qui pilote ; le jeton d'accès au modèle (dépôt à accès contrôlé) et un droit de poussée limité à la branche de versement, sur l'instance. Premier pas à 0 dollar : la session exécutante vérifie leur présence par nom et liste les instances du compte. Absents : aucune création ; Lazar les loge dans l'environnement de cette session ou désigne celle qui les a. Solde du loueur à relever à la création (20,42 dollars selon [modèle], § 3.4, à partager avec la passe du saboteur, plafonnée à 11).

## 3. Gardes

Aucun repli silencieux ; chaque garde est éprouvée avant création, sans carte, sur un cas sain et sur un artefact (R5). Une garde non tenue arrête la passe : trace d'arrêt sans score ni texte, aucune livraison.

1. **Équivalence sur une fraction des actions** ([attestation], réserve 3). L'étalonnage ne l'exigeait pas, et on ne peut pas savoir par son manifeste si elle a tourné. La passe la joue donc elle-même, à la fraction de la course de confirmation, 0,05 ([étalonnage], plan), soit 160 actions de l'étalonnage et 32 de la confirmation, avec la définition et la tolérance du texte scellé de cette course (non lu ici : **à reprendre sans les changer**). S'y ajoutent, repris de [modèle], § 4.1 : empreintes de toutes les entrées et du modèle ; décodage des identifiants égal au texte gardé pour 100 % des actions, avant chargement des poids, sans jamais retokeniser ; répétabilité en ordre inverse ; contrôle du contexte par la vraisemblance, avec son artefact de décalage.
2. **Identité de traitement entre les deux sources** ([attestation], réserves 1 et 2). Même code, même instance, même modèle nu, lots de 8 tirés par graine consignée (R9) où les deux sources sont mêlées. Après le scellement de la prévision, et par le code d'analyse seul, les scores repassés des 64 épisodes de la confirmation sont comparés à leurs scores existants : cet écart mesure l'effet joint de la dose 0 et de la composition des lots. Tolérance fixée par la prévision. Hors tolérance : le sixième jumeau se lit sur les scores repassés, réserve écrite, et le résultat est rapporté aussi à cinq jumeaux.
3. **Arrêt par identifiant (R10)**. Minuterie et suivi de dépense tenus hors de l'instance, armés à la création ; destruction par l'identifiant numérique, jamais un simple arrêt ; relecture de la liste des instances ; consignation aux registres des dépenses et des arrêts.
4. **Aveuglement**. La prévision est scellée avant le départ (§ 4). La session exécutante calcule des empreintes, copie et pousse ; elle ne décode aucun fichier de scores ni d'activations, et ses traces ne portent que des comptes et « tenue » ou « non tenue ». Liste « qui a lu quoi » inscrite avant toute lecture.
5. **Versement scellé**. Branche dédiée (par exemple `donnees/passe-activations-versant-honnete-v1`, jamais `main`), compagnons `.sha256`, bordereau, relecture distante depuis la machine de pilotage **avant** la destruction. En cas d'arrêt : trace et journal technique versés de même.

## 4. Prérequis avant départ, dans l'ordre

| ordre | pièce | auteur, contre-lecteur | classe |
|---:|---|---|---|
| 1 | **Prévision courte scellée du versant honnête.** Elle déclare m, n, l'unité et la source de validité ([référence honnête], § 2), cite Arnold, Henzi et Ziegel pour le rang parmi les jumeaux (erratum 3, E3-4), et fixe la tolérance de la garde 2. | Fable 5.2 ; Opus 5.5 neuf, qui vérifie ensuite les corrections | A |
| 2 | **Code d'analyse**, et **code et lanceur de la passe**, contre-lus et éprouvés sur données factices (cas sain et artefact) ; essai à blanc sans carte ; présence, par nom et empreinte, des fichiers de textes et d'identifiants des deux courses et des fichiers de sondes. | Opus 5.5 ; contre-lecteur d'un autre modèle | B |
| 3 | **Attestation de séparation d'avec la famille tenue à l'écart** : rendue « séparée » pour les 64 tâches, confiance 0,8, sous trois conditions (R-5249 de [registre]). La ligne ne les énonce pas : la session habilitée les recopie et atteste, une à une, qu'elles sont tenues. | session habilitée du coffre | C, cloisonnée |
| 4 | **Ce devis** contre-lu, corrigé, vérifié, scellé. | Opus 5.5 neuf ; la mère scelle | A |
| 5 | **Accord de type « calcul » de Lazar** sur ce devis, inscrit au registre des accords avec son plafond ; ligne d'engagement au registre des dépenses ; secrets vérifiés par nom. | Lazar ; la mère | nœud |

## 5. Ce que le devis ne couvre pas

- **Plus de six jumeaux par tâche** : devis séparé. Ordre de grandeur, deux jumeaux de plus (128 épisodes, juges compris) : au prorata des 12,19 dollars des 320 épisodes ([instruction], § 3, point 1, qui cite R-5184, non relue), ≈ 5 dollars, plus mise en place et réseau ≈ 3 : **≈ 8 dollars**, et un texte neuf.
- **Tâches neuves** (extraction, génération, juges, sondes, nouvelle attestation de séparation) : devis séparé.
- **Juges boîte noire refaits** : devis séparé ; repère, la course entière de l'étalonnage était attendue à 17 à 30 dollars ([étalonnage], « Devis à jour »).
- L'écriture de la prévision et des codes, l'analyse, la lecture propre de l'étalonnage, tout le versant saboté : hors devis.

## 6. Risques et conduite

- Identifiants de jetons absents pour une course, ou décodage différent du texte : arrêt avant création ; pour la confirmation, retour aux scores existants (réserve écrite) ; pour l'étalonnage, nœud.
- Garde d'équivalence non tenue : arrêt, versement de la trace, destruction ; panne technique diagnostiquée : relance sur le même accord ; cause de fond : retour à Lazar.
- Aveuglement rompu (un auteur de la prévision ou de l'analyse a vu une sortie, ou la lecture propre de l'étalonnage circule avant le scellement) : l'auteur touché est remplacé par un agent neuf.
- Seuils boîte noire appris sur ces mêmes 320 épisodes : la prévision lit les fausses alertes hors du pli qui a fixé le seuil ; sinon ce côté n'est que descriptif.
- Six jumeaux : le rang d'un honnête parmi cinq a un plancher de 1/6 par unité ; 1 % ne s'atteint que par accumulation. À écrire dans la prévision ; sinon option « plus de jumeaux ».
- Une condition de séparation non tenue : aucun départ ; tâches neuves, devis séparé.
- Aucune offre conforme, clé absente ou solde insuffisant : aucune création ; attente, ou repli sans dépense.
- Prérequis non clos le 27 novembre : le dossier de l'entretien dit « en cours » ; aucun raccourci.

## 7. Confiance et points pour Lazar

**Confiance** : 0,8 que la dépense réelle tombe entre 1,6 et 8,3 dollars et sous le plafond ; 0,65 sur le périmètre, qui dépend de pièces que je n'avais pas à lire.

**Non tranché, faute de lecture permise** : l'énoncé des trois conditions de R-5249 ; la définition et la tolérance de la garde d'équivalence de la course de confirmation ; la présence des fichiers d'identifiants des deux courses ; le code de passe à réemployer ; les noms des fichiers de sondes gelées ; la longueur réelle des contextes (elle place la durée entre « bas » et « haut ») ; le solde du loueur.

**Pour Lazar** :
1. Repasser les 64 épisodes de la confirmation (recommandé, ≈ 0,08 dollar, confiance 0,8), ou réemployer leurs scores existants.
2. Plafond de 12 dollars, une relance technique comprise ; ou 9 dollars, sans relance.
3. Où loger les trois secrets, et quelle session exécute.
4. La confiance 0,8 de l'attestation de séparation suffit-elle pour partir ?
5. Lire les scores de l'étalonnage pour le versant honnête avant sa lecture propre : je recommande de faire vérifier par la mère que ce n'est pas un écart au texte scellé de l'étalonnage ; si c'en est un, c'est un nœud.
6. Six jumeaux maintenant (recommandé), ou huit sur devis séparé.
