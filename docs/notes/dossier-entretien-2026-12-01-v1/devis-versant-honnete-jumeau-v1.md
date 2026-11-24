# Devis — passe unique d'activations et de notation par les sondes internes gelées sur les jumeaux honnêtes du vrai agent (versant honnête de l'essai « jumeau contre jumeau ») — v1

2026-11-24T09:51Z (`date -u`). Claude Fable 5.2, effort élevé, sur la consigne `consigne-fable-devis-versant-honnete-v1.md` (`77e07c2e1ceaadb1cce96e0cf566c8e19630e18f4167f64288e537a3afb89fc0`). Pièce de classe A, **non scellée, à contre-lire** par un Opus 5.5 neuf. N'ouvre aucune dépense. Aucune sortie de course, aucun score, aucun journal, aucun code ouvert.

Sources, citées ensuite par leur nom entre crochets (dossier `docs/notes/dossier-entretien-2026-12-01-v1/` sauf mention) :
- [instruction] `instruction-b6-versant-honnete-jumeau-v1.md`, `df6d6dfe1cd78403f100b97dcebc2eccbad24934045ebe66bd2cc841a704e6d8` ;
- [attestation] `attestation-manifestes-versant-honnete-v1.md` au commit `2f63d6db`, `e3f1ee567c79b4f3891b9d16286c81f2e808061bde89ccaa72bda59442a25239` ;
- [étalonnage] `prereg/T0.8-bases-boite-noire-v0-v3.md` au commit `50a6d30c`, `72a2611b3eff8ef070ab6f12f1468213cb88a8f42729eb2e9edeea7fcb884918` ;
- [modèle] `docs/notes/rejeu-activations-saboteur-voie-a-v1/devis-passe-activations-saboteur-voie-a-v2.md`, `9a4a794c4332f72d720c23a38db3c0c0a4175ee9a55e34d9627cc16e871eff45` ;
- [référence honnête] `docs/decisions/decision-N-076-assurance-par-audit-et-reference-honnete-v1.md`, `49b664c1d6a72fdb239d9a52e70ec85c4829fc5e77c6b5d3cf27848ce1a8dd78`, et son erratum 3, `3335284d40efe6e4454b0eaf6e3086982a074b5ef3d9e6e87ef7844a5d40f992` ;
- [registre] `registres/decisions.md`, `35d528ca957422fcadde47730d1da7204a42d8870d6638089fa57e8c4b27bbf3` à ma lecture, lignes R-5249 et R-5187 seules.

## 1. Ce qui est acheté

Une seule passe sur carte graphique, sans génération ni juge. Elle relit, jetons imposés, les actions déjà écrites par l'agent honnête (modèle de base nu), enregistre les activations aux couches du texte des sondes gelées (7, 15 et 23 selon [instruction], § 1 ; à confirmer sur ce texte, non lu) et note ces sondes, sans rien apprendre.
- **320 épisodes de l'étalonnage de la base boîte noire**, 3 200 actions ([instruction], § 1, tableau, ligne 1). Textes et identifiants de jetons y sont gardés ; « les activations restent recalculables par une passe unique » ([étalonnage], plan).
- **64 épisodes honnêtes de la course de confirmation de l'organisme à adaptateur**, 640 actions. Ils ont déjà leurs scores de sondes ([instruction], même ligne). **Je recommande de les repasser** : ces scores viennent d'un autre traitement (adaptateurs à dose 0, lots mêlés : [attestation], Q1, réserves 1 et 2). Surcoût : 640 × 0,40 s ≈ 0,07 heure, ≈ 0,08 dollar. Les scores existants servent de pont (§ 3, garde 2).

## 2. Machine, durée, coût (dollars des États-Unis)

**Machine** : une carte NVIDIA A100 de 80 gigaoctets en module serveur, celle des deux courses ([étalonnage], « Machine »), à la demande ; disque de 100 gigaoctets. **Repli** : la même carte en format d'extension ; toute autre, sur mot de la mère. Filtre bloquant de [modèle], § 2.3 : carte ≤ 1,35 de l'heure, stockage ≤ 0,40 par gigaoctet et par mois, réseau ≤ 0,04 par gigaoctet, fiabilité ≥ 0,97.

**Sources des prix et débits** : 1,0644 à 1,1360 de l'heure, relevé du 24 novembre ([modèle], § 2.2, non relu à sa source) ; 0,40, 0,85 et 1,60 seconde par action ([modèle], § 3.1) ; borne basse, passe par épisode du premier test, 240 épisodes en 108,4 s ([étalonnage], « Durées ») ; mise en place, archives, poussée, réseau : [modèle], § 3.1 à 3.3 (40 gigaoctets entrants à l'attendu, 45 au haut et au pire ; 20 au bas, supposé). Gardes comptées à 768 passes (4 × 5 % de 3 840 ; supposé).

| scénario (prix de l'heure) | passe et gardes | reste | durée | carte, stockage | réseau | **total** |
|---|---:|---:|---:|---:|---:|---:|
| bas (1,0644) | 0,15 h | 0,56 h | 0,71 h | 0,77 | 0,82 | **≈ 1,6** |
| **attendu** (1,14) | 0,51 h | 0,80 h | 1,31 h | 1,54 | 1,62 | **≈ 3,2** |
| haut (1,30) | 1,09 h | 1,50 h | 2,59 h | 3,51 | 1,84 | **≈ 5,4** |
| pire, au bord du filtre (1,35) | 2,05 h | 2,50 h | 4,55 h | 6,39 | 1,88 | **≈ 8,3** |

**Plafond proposé : 12 dollars**, toutes tentatives. Coupure par instance à 10, déclenchée à 9,60 ; horloge de 5 heures (au plus 8,91 sur un hôte conforme). Le plafond couvre une relance après panne déclarée (incident à une heure ≈ 3,3, puis scénario haut : ≈ 8,7), jamais automatique. **Repli sans dépense** : versant honnête sur les seuls scores boîte noire existants ; la comparaison avec les sondes est perdue, et c'est à la prévision de le dire.

**Clés : rien n'est présumé** (R-5187 de [registre] : un conteneur n'en avait aucune). Trois secrets, lus par leur nom, jamais écrits : clé du loueur Vast.ai chez la session qui pilote ; jeton d'accès au modèle et droit de poussée limité à la branche de versement sur l'instance. La session exécutante vérifie d'abord leur présence, à 0 dollar. Absents : aucune création ; Lazar les loge ou désigne la session qui les a. Solde du loueur à relever (20,42 selon [modèle], § 3.4, partagé avec la passe du saboteur).

## 3. Gardes

Chacune est éprouvée sans carte sur un cas sain et un artefact (R5). Non tenue : arrêt, trace sans score ni texte, aucune livraison.
1. **Équivalence sur une fraction des actions** ([attestation], réserve 3 : indéterminable pour l'étalonnage). La passe la joue elle-même, à la fraction de la course de confirmation, 0,05 ([étalonnage], plan) : 160 et 32 actions. Définition et tolérance : celles du texte scellé de cette course, non lu ici, **reprises sans changement**. S'ajoutent, de [modèle], § 4.1 : empreintes des entrées et du modèle ; décodage des identifiants égal au texte pour 100 % des actions, sans retokeniser ; répétabilité en ordre inverse ; contrôle du contexte par la vraisemblance.
2. **Identité de traitement** ([attestation], réserves 1 et 2). Même code, même instance, modèle nu, lots de 8 tirés par graine consignée, les deux sources mêlées. Après le scellement de la prévision, le code d'analyse compare les scores repassés des 64 épisodes à leurs scores existants. Tolérance fixée par la prévision. Au-delà : sixième jumeau lu sur les scores repassés, réserve écrite, résultat rapporté aussi à cinq jumeaux.
3. **Arrêt par identifiant (R10)** : minuterie et suivi de dépense hors de l'instance ; destruction par identifiant numérique ; consignation aux registres.
4. **Aveuglement** : la session exécutante calcule des empreintes, copie et pousse ; elle ne décode ni scores ni activations ; ses traces ne portent que des comptes et « tenue » ou « non tenue ».
5. **Versement scellé** sur branche dédiée, compagnons `.sha256`, bordereau, relecture distante **avant** destruction ; en cas d'arrêt, la trace est versée de même.

## 4. Prérequis avant départ, dans l'ordre

1. **Prévision courte scellée** (classe A ; Fable 5.2, contre-lue par Opus 5.5). Elle déclare m, n, l'unité et la source de validité ([référence honnête], § 2), cite Arnold, Henzi et Ziegel pour le rang parmi les jumeaux (erratum 3, E3-4) et fixe la tolérance de la garde 2.
2. **Code d'analyse, code et lanceur de la passe** (classe B ; Opus 5.5, contre-lecteur d'un autre modèle), éprouvés sur données factices ; essai à blanc sans carte ; présence, par nom et empreinte, des fichiers de textes, d'identifiants et de sondes.
3. **Attestation de séparation d'avec la famille tenue à l'écart** (session habilitée du coffre) : « séparée », confiance 0,8, sous trois conditions (R-5249). La ligne ne les énonce pas : la session les recopie et atteste chacune.
4. **Ce devis** contre-lu, vérifié, scellé (classe A).
5. **Accord de type « calcul » de Lazar**, avec plafond ; ligne d'engagement au registre des dépenses.

## 5. Hors devis

- **Plus de six jumeaux** : devis séparé ; repère pour deux de plus, juges compris : ≈ 8 dollars (prorata des 12,19 pour 320 épisodes, [instruction], § 3, point 1, plus ≈ 3 de mise en place).
- **Tâches neuves** : devis séparé, et nouvelle attestation de séparation.
- **Juges boîte noire refaits** : devis séparé ; repère, 17 à 30 dollars attendus pour la course d'étalonnage entière ([étalonnage], « Devis à jour »).

## 6. Risques et conduite

- Identifiants absents ou décodage différent du texte : arrêt avant création ; scores existants pour la confirmation, nœud pour l'étalonnage.
- Garde non tenue : arrêt, versement, destruction ; panne diagnostiquée : relance sur le même accord ; cause de fond : Lazar.
- Aveuglement rompu : l'auteur touché est remplacé par un agent neuf.
- Seuils boîte noire appris sur ces mêmes 320 épisodes : fausses alertes lues hors du pli qui a fixé le seuil, sinon descriptif seulement.
- Six jumeaux : le rang parmi cinq a un plancher de 1/6 par unité ; 1 % ne s'atteint que par accumulation. À écrire dans la prévision.
- Condition de séparation non tenue, offre, clé ou solde manquants : aucune création.
- Prérequis non clos le 27 novembre : le dossier de l'entretien dit « en cours ».

## 7. Confiance et points pour Lazar

**Confiance** : 0,8 que la dépense tombe entre 1,6 et 8,3 dollars ; 0,65 sur le périmètre.

**Non tranché, faute de lecture permise** : les trois conditions de R-5249 ; la définition de la garde d'équivalence ; la présence des fichiers d'identifiants ; le code de passe à réemployer ; les fichiers de sondes ; la longueur des contextes.

**À Lazar** : (1) repasser les 64 épisodes de la confirmation (recommandé, confiance 0,8) ou garder leurs scores ; (2) plafond de 12 dollars avec relance, ou 9 sans ; (3) où loger les secrets, quelle session exécute ; (4) la confiance 0,8 de la séparation suffit-elle ; (5) lire les scores de l'étalonnage ici avant sa lecture propre est-il un écart à son texte scellé — à faire vérifier par la mère, nœud si oui ; (6) six jumeaux maintenant (recommandé) ou huit sur devis séparé.
