# Devis — passe unique d'activations et de notation par les sondes internes gelées sur les jumeaux honnêtes du vrai agent (versant honnête de l'essai « jumeau contre jumeau ») — v2

**v2 : corrections de la contre-lecture** d'un Opus 5.5 neuf ([contre-lecture], « conforme sous corrections », défauts 1 à 8, tous repris ; une précision au défaut 1, dite à la garde 1). La v1 (`527bdaa420a3cb933f940b6f562ed30581ab8fefcd54cba37bea752945eea212`) reste telle quelle.

2026-11-24T10:01Z (`date -u`). Claude Fable 5.2, effort élevé. Pièce de classe A, **non scellée, à faire vérifier** par le même contre-lecteur ; elle n'ouvre aucune dépense. Aucune sortie de course, aucun score, aucun journal, aucun code ouvert. Les noms entre crochets renvoient aux sources, en fin de pièce.

## 1. Ce qui est acheté

Une passe sur carte graphique, sans juge : relire, jetons imposés, les actions déjà écrites par l'agent honnête (modèle de base nu), enregistrer les activations aux couches du texte des sondes gelées (7, 15 et 23 selon [instruction], § 1 ; à confirmer sur ce texte, non lu) et noter ces sondes, sans rien apprendre. Seule génération : les 192 actions de la garde 1, hors mesure.
- **320 épisodes de l'étalonnage de la base boîte noire**, 3 200 actions ([instruction], § 1, tableau, ligne 1). Textes et identifiants de jetons sont gardés ; « les activations restent recalculables par une passe unique » ([étalonnage], plan).
- **64 épisodes honnêtes de la course de confirmation de l'organisme à adaptateur**, 640 actions. Ils ont déjà leurs scores de sondes ([instruction], même ligne). **Je recommande de les repasser** (≈ 0,08 dollar), pour que les six jumeaux soient relus par la même chaîne. **Cela ne traite que la relecture.** Les réserves 1 et 2 de [attestation] portent sur la génération de ce sixième jumeau (adaptateurs à dose 0, lots mêlés qui changent les trajectoires) : son échangeabilité avec les cinq autres **reste une hypothèse**, que la prévision déclare. Tout résultat est rapporté **à cinq et à six jumeaux**, toujours.
- **Mode de la passe** (une relecture par épisode ou par action) : celui qui a produit les scores existants de la course de confirmation, à lire dans le texte des sondes gelées. Sinon le pont de la garde 2 ne vaut rien.

## 2. Machine, durée, coût (dollars des États-Unis)

**Machine** : une carte NVIDIA A100 de 80 gigaoctets en module serveur, celle des deux courses ([étalonnage], « Machine »), à la demande ; disque de 100 gigaoctets. **Repli** : la même carte en format d'extension ; toute autre, sur mot de la mère. Filtre bloquant de [modèle], § 2.3 : carte ≤ 1,35 de l'heure, stockage ≤ 0,40 par gigaoctet et par mois, réseau ≤ 0,04 par gigaoctet.

**Volumes** : 4 992 relectures d'action, soit 3 840 pour la mesure, 960 pour les gardes de contexte et de répétabilité (5 × 192) et 192 pour la garde 1 ; plus 192 actions régénérées.

**Sources** : prix de 1,0644 à 1,1360 de l'heure, relevé du 24 novembre ([modèle], § 2.2, non relu à sa source) ; relecture à 0,40, 0,85 et 1,60 seconde par action ([modèle], § 3.1) ; génération à 40,2 s par épisode de dix actions, soit 772 s pour 192 actions à l'attendu ([étalonnage], « Durées »), multipliée par 2,125 et par 4 au haut et au pire, comme la relecture ; reste (mise en place, archives, poussée) et réseau : [modèle], § 3.1 à 3.3. **Bas** : relecture par épisode au débit du premier test, 108,4 s pour 240 épisodes ([étalonnage], « Durées »), soit 0,045 seconde par action à dix actions par épisode (supposé) ; mise en place observée de 0,31 heure ([modèle], § 3.1) ; le reste comme à l'attendu.

| scénario (prix de l'heure) | relectures | régénération | reste | durée | carte, stockage | réseau | **total** |
|---|---:|---:|---:|---:|---:|---:|---:|
| bas (1,0644) | 0,06 h | 0,21 h | 0,71 h | 0,99 h | 1,08 | 1,62 | **≈ 2,7** |
| **attendu** (1,14) | 0,55 h | 0,21 h | 0,80 h | 1,57 h | 1,84 | 1,62 | **≈ 3,5** |
| haut (1,30) | 1,18 h | 0,46 h | 1,50 h | 3,13 h | 4,25 | 1,84 | **≈ 6,1** |
| pire, au bord du filtre (1,35) | 2,22 h | 0,86 h | 2,50 h | 5,58 h | 7,84 | 1,88 | **≈ 9,7** |

**Plafond proposé : 12 dollars, tenu en cumul sur toutes les tentatives.** Première instance : coupure à 10 ; horloge de 5 h 45 (au plus 9,96 sur un hôte conforme). Relance après panne déclarée, jamais automatique : sa coupure vaut le plus petit de 10 et de « 12 moins la dépense déjà faite ». Exemple : incident à une heure (≈ 3,3), relance coupée à 8,7 ; elle couvre le scénario haut (6,1), non le pire.

**Solde du loueur** : 20,42 selon [modèle], § 3.4, partagé avec la passe du saboteur, plafonnée à 11. Les deux plafonds font 23, plus que le solde. Avant toute création : solde relevé, et ordre des deux passes fixé, ou recharge décidée par Lazar.

**Repli sans dépense** : versant honnête sur les seuls scores boîte noire existants ; la comparaison avec les sondes est perdue, et la prévision doit le dire.

**Clés : rien n'est présumé** (R-5187 de [registre] : un conteneur n'en avait aucune). Trois secrets, lus par leur nom, jamais écrits : clé du loueur Vast.ai chez la session qui pilote ; jeton d'accès au modèle et droit de poussée limité à la branche de versement, sur l'instance. Absents : aucune création ; Lazar les loge ou désigne la session qui les a.

## 3. Gardes

Chacune est éprouvée sans carte sur un cas sain et un artefact. Non tenue : arrêt, trace sans score ni texte, aucune livraison.
1. **Équivalence par régénération de 5 % des actions** ([attestation], réserve 3). L'étalonnage n'a pris aucune activation : rien ne se compare après coup. La passe régénère donc 192 actions tirées par graine consignée (160 sur les contextes de l'étalonnage, 32 sur ceux de la confirmation), graines neuves au manifeste, en capturant les activations pendant la génération ; puis elle relit ces mêmes actions, jetons imposés, et compare. Définition et tolérance : celles de la garde de la course de confirmation (99e centile, selon [contre-lecture], défaut 1 ; à recopier de son texte scellé, non lu ici). Coût attendu : 0,24 heure, ≈ 0,28 dollar, compris au tableau. **Précision** : la garde prouve l'équivalence des deux modes sur la chaîne et l'hôte de la passe ; les actions régénérées diffèrent des actions gardées, et ce qui s'est passé sur l'hôte d'origine reste hors d'atteinte. Limite à écrire dans la prévision. Les actions régénérées sont versées, marquées « garde, hors mesure ».
   S'ajoutent, de [modèle], § 4.1 : empreintes des entrées et du modèle ; décodage des identifiants égal au texte pour toutes les actions, sans retokeniser ; répétabilité en ordre inverse ; contrôle du contexte par la vraisemblance.
2. **Identité de la relecture entre les deux sources.** Même code, même instance, modèle nu, même mode, lots de 8 tirés par graine consignée, les deux sources mêlées. Après le scellement de la prévision, le code d'analyse compare les scores repassés des 64 épisodes à leurs scores existants ; tolérance fixée par la prévision. Au-delà : sixième jumeau lu sur les scores repassés, réserve écrite. Cette garde ne dit rien de la génération (§ 1).
3. **Arrêt par identifiant (R10)** : minuterie et suivi de dépense hors de l'instance ; destruction par identifiant numérique, consignée.
4. **Aveuglement de l'exécutante** : inscrite sur la liste « qui a lu quoi » avant le départ, elle calcule des empreintes, copie et pousse ; elle ne décode ni scores ni activations ; ses traces ne portent que des comptes et « tenue » ou « non tenue ».
5. **Versement scellé** sur branche dédiée, avec empreintes compagnons et bordereau, relu à distance **avant** destruction ; après un arrêt, la trace est versée de même.

## 4. Prérequis avant départ, dans l'ordre

1. **Attestation de séparation d'avec la famille tenue à l'écart** (session habilitée du coffre ; 0 dollar, décisive, donc en tête) : « séparée », confiance 0,8, sous trois conditions (R-5249 de [registre]). La ligne ne les énonce pas : la session les recopie et atteste chacune.
2. **Texte des sondes gelées lu** (la mère ou un agent neuf, classe C) : couches, fichiers et empreintes, mode de la passe, définition de la garde d'équivalence.
3. **Prévision courte scellée** (classe A ; Fable 5.2, contre-lue par Opus 5.5). **Son rédacteur et son contre-lecteur n'ont vu ni la lecture scellée de l'étalonnage ni son verdict (R-5233 et R-5235 selon [contre-lecture], question 5), qui portent déjà la garde de fausses alertes et le contrôle d'échangeabilité sur l'honnête de la confirmation, ni les scores de sondes de ce même honnête. Ils l'attestent par écrit et s'inscrivent sur la liste « qui a lu quoi ».** La prévision déclare m, n, l'unité et la source de validité ([référence honnête], § 2), cite Arnold, Henzi et Ziegel pour le rang parmi les jumeaux (erratum 3, E3-4), déclare et borne le réemploi des épisodes (§ 7), l'hypothèse d'échangeabilité du sixième jumeau, la tolérance de la garde 2 et les points du § 6.
4. **Code d'analyse, code et lanceur de la passe, régénération de la garde 1 comprise** (classe B ; Opus 5.5, contre-lecteur d'un autre modèle), éprouvés sur données factices ; essai à blanc sans carte ; présence, par nom et empreinte, des fichiers de textes, d'identifiants et de sondes.
5. **Ce devis** vérifié, scellé (classe A).
6. **Secrets vérifiés par nom ; solde du loueur relevé ; ordre des deux passes fixé** (session exécutante, inscrite sur la liste « qui a lu quoi » ; la mère).
7. **Accord de type « calcul » de Lazar**, avec plafond ; ligne d'engagement au registre des dépenses.

## 5. Hors devis

- **Plus de six jumeaux** : devis séparé ; repère pour deux de plus, juges compris : ≈ 8 dollars (prorata des 12,19 pour 320 épisodes, [instruction], § 3, point 1, plus ≈ 3 de mise en place).
- **Tâches neuves** : devis séparé, et nouvelle attestation de séparation.
- **Juges boîte noire refaits** : devis séparé ; repère, 17 à 30 dollars attendus pour la course d'étalonnage entière ([étalonnage], « Devis à jour »).

## 6. Risques et conduite

- Identifiants absents ou décodage différent du texte : arrêt avant création ; scores existants pour la confirmation, nœud pour l'étalonnage.
- Garde non tenue : arrêt, versement, destruction ; panne diagnostiquée : relance sur le même accord, dans le cumul ; cause de fond : Lazar.
- Aveuglement rompu (rédacteur, contre-lecteur ou exécutante) : l'agent touché est remplacé par un agent neuf.
- **Seuils boîte noire appris sur ces mêmes épisodes.** Normalisation sur 64 épisodes, seuils au rang conforme sur les 256 autres ([étalonnage], « Calibrage »). Le rang parmi les jumeaux ne dépend ni des seuils ni de la normalisation commune : il est sûr. Les taux de fausses alertes sont en échantillon pour cinq jumeaux, et hors échantillon pour le seul sixième, que la lecture scellée a déjà vu. La prévision refait donc un calibrage croisé par moitiés de tâches, le même pour les sondes et la boîte noire, ou déclare ces taux descriptifs.
- **Six jumeaux.** Le rang se prend parmi six (l'original et cinq jumeaux) : valeur p d'au moins 1/6. Un étalonnage par tâche à 1 % est dégénéré : il y faut au moins 99 épisodes ([étalonnage], plan, « Taille »). L'accumulation n'est valide que sur des unités indépendantes, les tâches, non sur les pas d'un même épisode. À écrire dans la prévision.
- Condition de séparation non tenue, offre, clé ou solde manquants : aucune création.
- Prérequis non clos le 27 novembre : le dossier de l'entretien dit « en cours ».

## 7. Confiance et points pour Lazar

**Confiance** : 0,8 que la dépense tombe entre 2,7 et 9,7 dollars ; 0,7 sur le périmètre.

**Réemploi des épisodes de l'étalonnage.** La question « avant sa lecture propre » tombe : cette lecture est scellée et son verdict prononcé ([contre-lecture], question 5). Reste ceci : le texte scellé de l'étalonnage réserve ses épisodes honnêtes au calibrage (« jamais à apprendre M2 ou MC ni à une lecture d'effet », M2 et MC étant ses deux prédicteurs appris) et ne prévoit les activations que « si G1 ou T0.7 les veulent » (la porte de fin de phase 1 ou la passe des sondes) ; le versant honnête n'apprend rien et ne lit aucun effet, donc il n'est pas un écart, mais ce réemploi n'est régi que par la prévision courte, qui doit le déclarer et le borner.

**Non tranché, faute de lecture permise** : les trois conditions de R-5249 ; le texte de la garde d'équivalence et celui des sondes gelées (couches, fichiers, mode) ; la présence des fichiers d'identifiants ; le code de passe à réemployer ; la longueur des contextes ; le solde réel du loueur.

**À Lazar** : (1) repasser les 64 épisodes de la confirmation (recommandé, confiance 0,8) ou garder leurs scores ; dans les deux cas, résultat à cinq et à six jumeaux ; (2) plafond de 12 dollars en cumul, relance comprise, ou 10 sans relance ; (3) ordre des deux passes sur le solde commun du loueur, ou recharge ; (4) où loger les secrets, quelle session exécute ; (5) la confiance 0,8 de la séparation suffit-elle ; (6) six jumeaux maintenant (recommandé) ou huit sur devis séparé ; (7) taux de fausses alertes : calibrage croisé par moitiés de tâches (recommandé) ou taux déclarés descriptifs, à fixer dans la prévision.

## Sources (R6)

Dossier `docs/notes/dossier-entretien-2026-12-01-v1/` sauf mention.
- Consigne : `consigne-fable-devis-versant-honnete-v1.md`, `77e07c2e1ceaadb1cce96e0cf566c8e19630e18f4167f64288e537a3afb89fc0`.
- [contre-lecture] `contre-lecture-devis-versant-honnete-opus-v1.md`, `7423f87b41c97da3b99e316daaa21d22ae76c2c7dce933d0c4c33e5cbff6bd7e`.
- [instruction] `instruction-b6-versant-honnete-jumeau-v1.md`, `df6d6dfe1cd78403f100b97dcebc2eccbad24934045ebe66bd2cc841a704e6d8`.
- [attestation] `attestation-manifestes-versant-honnete-v1.md`, commit `2f63d6db`, `e3f1ee567c79b4f3891b9d16286c81f2e808061bde89ccaa72bda59442a25239`.
- [étalonnage] `prereg/T0.8-bases-boite-noire-v0-v3.md`, commit `50a6d30c`, `72a2611b3eff8ef070ab6f12f1468213cb88a8f42729eb2e9edeea7fcb884918`.
- [modèle] `docs/notes/rejeu-activations-saboteur-voie-a-v1/devis-passe-activations-saboteur-voie-a-v2.md`, `9a4a794c4332f72d720c23a38db3c0c0a4175ee9a55e34d9627cc16e871eff45`.
- [référence honnête] `docs/decisions/decision-N-076-assurance-par-audit-et-reference-honnete-v1.md`, `49b664c1d6a72fdb239d9a52e70ec85c4829fc5e77c6b5d3cf27848ce1a8dd78` ; erratum 3, `3335284d40efe6e4454b0eaf6e3086982a074b5ef3d9e6e87ef7844a5d40f992`.
- [registre] `registres/decisions.md`, lignes R-5249 et R-5187 seules (`35d528ca957422fcadde47730d1da7204a42d8870d6638089fa57e8c4b27bbf3` à ma lecture du matin ; R-5233 et R-5235 non lues par moi, reprises de [contre-lecture]).
- Lue aussi, sans chiffre repris : `ecarts-sources-honnetes-b6-v1.md`, `e843960269d9ebbd7e171c394f996e8b37bf6dd39d79dd3ec80ebc236151d2cf`.
