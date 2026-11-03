# Groupement aveugle des fiches — piste Ibrahim, question 1 (ensemble v2), version 1

Entrée : `/home/claude/scratch/soir-rapport/ibrahim-q1-ensemble-v2/piste/fiches-a-grouper-v1.json` (sha256 `dac9a132df81c61110285e6c5031c8f091c6105d4f1d21256c7107bb9f9d7ab9`, vérifiée avant lecture), 32 fiches (IB-01 à IB-32).
Groupeur neuf, aveugle au classement ; aucun autre fichier lu.

## Définitions des groupes

Écrites le 2026-11-03 à 20:16:25 UTC (heure de `date -u`), avant toute affectation ; non modifiées ensuite.
Chaque groupe est un type d'expérience, défini par la question que la première expérience tranche.

### G1 — Tenue après renforcement
- Définition : la première expérience tranche si ce que l'entraînement de caractère installe (persona, son excès d'erreur ou de validation, sa sensibilité sociale) survit à un apprentissage par renforcement ultérieur, et dans quelle mesure.
  Elle compare avant et après renforcement (ou plusieurs doses, recettes d'installation ou tours de conversation), le contenu de la récompense n'étant pas la cause étudiée.
- Critère : la prédiction principale porte sur la conservation, l'érosion ou l'évolution d'une quantité liée à la persona entre avant et après renforcement (ou selon la dose, la recette, le tour), le type de récompense étant fixé et n'étant pas l'hypothèse testée.

### G2 — Cause par la récompense
- Définition : la première expérience tranche si le contenu de la récompense (préférences humaines apprises, composante de chaleur) cause ou amplifie la sycophancie.
  La variable manipulée est la nature de la récompense, opposée à une récompense vérifiable, à un témoin à étiquettes permutées ou non informatif, à déplacement de politique apparié.
- Critère : la prédiction principale porte sur l'effet propre d'une récompense de préférences ou de chaleur (comparée à une autre récompense, à un témoin, ou dans son interaction avec la persona), ou prédit qu'une récompense sans préférence ne déplace pas une quantité supposée venir des préférences ; l'hypothèse testée est « les préférences causent ou amplifient la sycophancie ».

### G3 — Validité de la mesure
- Définition : la première expérience tranche si l'instrument (classifieur de persona, juge de sycophancie, détecteur lexical) ou le codage (refus, abstentions, longueur jugée, ton) lit bien la position de fond.
  Elle vérifie qu'un effet mesuré n'est pas fabriqué ou masqué par le style ou par les conventions de notation.
- Critère : la prédiction principale porte sur l'accord entre un instrument et une référence, sur la sensibilité d'un effet à un choix de codage ou à la neutralisation du ton, ou sur la remplaçabilité du juge — et non sur le comportement du modèle lui-même.

### G4 — Fragmentation du construit
- Définition : la première expérience tranche si les composantes de la sycophancie d'une persona (sociale contre factuelle, forme chaleureuse contre substance) existent séparément.
  Elle demande si ces composantes bougent ensemble ou séparément, notamment sous renforcement.
- Critère : la prédiction principale compare deux composantes ou cellules du construit (ou leur couplage, conversation par conversation ou à travers des points de contrôle), ou porte sur la présence d'une composante (factuelle) que la persona pourrait ne pas avoir.

### G5 — Forme de la réponse à la pression
- Définition : la première expérience tranche quel mécanisme décrit le déplacement d'un modèle fixé sous pression sociale (mélange contre contraction, dimension concédée, médiateur de refus, point fixe contre gain de la loi d'attraction).
  L'entraînement n'y est pas la variable manipulée.
- Critère : la prédiction principale oppose deux modèles de la réponse à la pression sur un point de contrôle donné (ou entre persona et base sans entraînement), à propos de la structure de la loi d'attraction — et non de sa tenue après renforcement ni de la validité du juge.

### G6 — Effacement ou masquage
- Définition : la première expérience tranche, quand un comportement de persona ou de sycophancie semble disparu après renforcement, s'il est effacé ou seulement masqué.
  Elle recourt à une intervention qui révèle l'état latent (réapprentissage court, sondes, greffe d'activations).
- Critère : la prédiction principale porte sur la récupérabilité d'un comportement apparemment disparu (économie de réapprentissage, restauration par greffe, décodage par sonde), et non sur la mesure de la disparition elle-même.

## Affectations

Une fiche, un groupe (son idée principale) ; « second choix » quand une fiche relève presque autant d'un autre groupe.

| Fiche | Groupe | Raison | Second choix |
|---|---|---|---|
| IB-01 | G1 | Prédit la tenue, après renforcement à récompense vérifiable, de l'excès de validation injustifiée de conduite de Loving. | G4 |
| IB-02 | G1 | Prédit la conservation de l'écart de persona Loving − base après renforcement à récompense vérifiable, à divergence KL appariée. | — |
| IB-03 | G4 | Oppose la capitulation dans le domaine social et dans le domaine factuel (double différence persona × renforcement). | G1 |
| IB-04 | G3 | Teste si le classifieur de persona et le juge séparent la position du style sur des paires annotées par des humains. | — |
| IB-05 | G5 | Oppose un modèle de mélange à un modèle de contraction continue pour le déplacement des notes sous pression. | — |
| IB-06 | G2 | Teste si une récompense sans préférence humaine laisse le gain g inchangé, comme le prédit « le gain vient des préférences ». | G1 |
| IB-07 | G2 | Teste si un renforcement contre un modèle de récompense de préférences amplifie l'erreur de Loving plutôt que d'agir de façon additive. | G1 |
| IB-08 | G5 | Prédit que la persona déplace le point fixe c sans changer le gain g de la loi d'attraction, sans entraînement. | — |
| IB-09 | G2 | Compare un renforcement par préférences à un renforcement vérifiable à divergence KL appariée, avec témoin à étiquettes permutées. | — |
| IB-10 | G4 | Teste si la persona Sycophantic a une composante factuelle de capitulation ou n'est qu'un ton social. | G3 |
| IB-11 | G5 | Teste si le taux de refus ou de prise de distance médie la descente sous éloge des items bien notés. | G3 |
| IB-12 | G3 | Teste si un détecteur lexical figé reproduit le déplacement mesuré par le juge, donc si le juge est remplaçable. | — |
| IB-13 | G5 | Oppose une concession sur la forme (écriture) à une capitulation globale du verdict sous critique. | — |
| IB-14 | G1 | Prédit la tenue, après renforcement vérifiable, de l'excès d'erreur de Loving sous fausse croyance hors domaine de la récompense. | — |
| IB-15 | G1 | Prédit que Loving reste, après renforcement arithmétique, plus sensible que la base à l'intensification d'une pression flatteuse. | G4 |
| IB-16 | G4 | Prédit que Sycophantic élève plus la sycophancie sociale que la capitulation factuelle et que les deux ne covarient pas. | — |
| IB-17 | G1 | Prédit que l'adhésion à la persona décroît davantage du premier au cinquième tour après renforcement qu'avant. | G3 |
| IB-18 | G1 | Prédit une remontée de capitulation aux tours tardifs après renforcement plus forte chez Loving que chez la base. | — |
| IB-19 | G4 | Oppose couplage et découplage entre capitulation tardive et chute de chaleur, conversation par conversation. | G1 |
| IB-20 | G3 | Prédit qu'une part de la baisse apparente de capitulation vient du traitement des abstentions, non des réponses substantielles. | — |
| IB-21 | G4 | Prédit le couplage proportionnel entre érosion de la persona et recul de son excès d'erreur (erreur attachée à la persona ou au style). | G1 |
| IB-22 | G3 | Prédit qu'un juge validé avant renforcement perd sa validité sur les sorties après renforcement. | — |
| IB-23 | G3 | Prédit que le signe de l'effet du renforcement change sous un codage raisonnable des refus et de la longueur jugée. | — |
| IB-24 | G6 | Distingue masquage de surface et effacement par sondes et greffe de l'état résiduel après un renforcement anti-sycophancie. | — |
| IB-25 | G3 | Prédit qu'une part du déplacement du point fixe attribué à Loving disparaît à ton neutralisé : le juge lit le style comme un accord. | G5 |
| IB-26 | G1 | Prédit que la perte de persona croît avec la dose d'optimisation (courbe dose–réponse). | — |
| IB-27 | G1 | Prédit que la recette d'installation (introspective de rang 64 contre supervisée sans introspection) commande la tenue après renforcement. | — |
| IB-28 | G3 | Teste si la hausse de g après renforcement par préférences survit à la neutralisation du ton (effet de fond contre artefact du juge). | G2 |
| IB-29 | G6 | Teste par économie de réapprentissage si une persona disparue après long renforcement est masquée plutôt qu'effacée. | G1 |
| IB-30 | G2 | Isole la composante chaleur de la récompense contre une récompense d'exactitude seule. | — |
| IB-31 | G1 | Prédit que, après renforcement vérifiable, la sensibilité de Loving à l'éloge sur le fond augmente plus que celle de la base (interaction sur g). | G4 |
| IB-32 | G4 | Prédit que la sycophancie sociale et de cadrage évolue plus défavorablement que la capitulation factuelle sous renforcement. | G3 |

Effectifs : G1 9 ; G2 4 ; G3 7 ; G4 6 ; G5 4 ; G6 2 (total 32). Fiches à second choix : 15.

## Limites

- Ordre de travail : les fiches ont été lues avant l'écriture des définitions (il fallait connaître les questions pour définir des types) ; les définitions ont été écrites et horodatées avant toute affectation, puis laissées telles quelles.
- G1 est large (9 fiches) : il réunit des axes distincts — tenue simple (IB-01, IB-02, IB-14), dose (IB-26), recette d'installation (IB-27), tour de conversation (IB-17, IB-18), sensibilité sociale résiduelle (IB-15, IB-31). Les tours de conversation auraient pu faire un groupe propre ; le plafond de six groupes m'a fait garder plutôt « Effacement ou masquage » à part, parce que le dispositif expérimental (réapprentissage, sondes, greffe) y diffère, alors que les tours restent un protocole avant/après.
- G6 ne compte que 2 fiches ; IB-24 y entre alors que son renforcement vise la sycophancie de surface (et non une récompense vérifiable) : le critère de G6 porte sur la récupérabilité, pas sur le type de récompense.
- Frontière G1/G2 : IB-06 mesure un avant/après sous récompense vérifiable (forme de G1) mais sert de test nul de la cause « le gain vient des préférences » (clause de G2) ; IB-07 fixe la récompense de préférences et compare persona et base, il n'entre dans G2 que par la clause « interaction avec la persona ». À l'inverse IB-26 se fait sous renforcement par préférences mais reste en G1, l'hypothèse testée étant la dose, pas la cause.
- Frontière G1/G4 : plusieurs fiches après renforcement touchent à la dissociation chaleur/substance. J'ai mis en G4 celles dont la prédiction compare deux composantes ou leur couplage (IB-03, IB-19, IB-21, IB-32), en G1 celles dont la prédiction porte sur la tenue d'une seule quantité, même si leur mécanisme invoque la dissociation (IB-15, IB-31, IB-01).
- Frontière G3/G5 : IB-25 (point fixe et juge) et IB-11 (refus notés au milieu par le juge) mêlent mécanisme du modèle et artefact de notation ; tranché selon l'objet de la prédiction principale.
- IB-10 n'entre en G4 que par la clause « présence d'une composante (factuelle) » ; c'est aussi un contrôle de prise de la manipulation, d'où le second choix G3.
- IB-31 touche trois groupes (tenue, dissociation chaleur/susceptibilité, neutralisation du ton) ; un seul second choix retenu (G4).
- Presque toutes les fiches portent un élément « ce qui rendrait le résultat trompeur » relevant de G3 ; G3 n'a été attribué en premier que lorsque la prédiction principale porte sur la mesure elle-même, sinon au mieux en second choix.
